import sys
from malsim import Scenario, MalSimulator
from malsim.config import MalSimulatorSettings
from malsim.config.sim_settings import RewardMode, TTCMode
from maltoolbox.attackgraph import AttackGraphNode
from malsim.mal_simulator.agent_state import MalSimAgentState

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

def state2performed_node_names(state: MalSimAgentState) -> list[str]:
    return [node.full_name for node in state.performed_nodes]

first_arg = sys.argv[1] if len(sys.argv) > 1 else None
scenario = Scenario.load_from_file(first_arg)
simulator = MalSimulator.from_scenario(
    scenario,
    sim_settings=MalSimulatorSettings(
        ttc_mode=TTCMode.DISABLED,
        run_defense_step_bernoullis=False,
        run_attack_step_bernoullis=False,
        attack_surface_skip_unnecessary=False,
        compromise_entrypoints_at_start=True,
        attacker_reward_mode=RewardMode.EXPECTED_TTC,
    ),
)
second_arg = sys.argv[2] if len(sys.argv) > 2 else None
if not second_arg:
    simulator.run()
    print(simulator.results)
else:
    lines = open(second_arg, 'r').readlines()
    lines = [line.strip() for line in lines if not line.startswith('#')]
    attacker_name = list(simulator.agent_states.keys())[0]

    green_lines = 0
    yellow_lines = 0

    state = simulator.reset()[attacker_name]
    for line in lines:
        try:
            node: AttackGraphNode = next(node for node in state.action_surface if node.full_name == line)
        except StopIteration:
            if line in state2performed_node_names(state):
                print_yellow(line)
                yellow_lines += 1
            else:
                print_red(line)
            continue
        state = simulator.step({attacker_name: [node]})[attacker_name]
        print_green(line)
        green_lines += 1
 
    print(f"Green lines: {green_lines}")
    print(f"Yellow lines: {yellow_lines}")