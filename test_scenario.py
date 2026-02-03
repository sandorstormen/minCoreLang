import sys
from malsim import Scenario, MalSimulator
from malsim.config import MalSimulatorSettings
from malsim.config.sim_settings import RewardMode, TTCMode
from maltoolbox.attackgraph import AttackGraphNode

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

    state = simulator.reset()[attacker_name]
    for line in lines:
        try:
            node: AttackGraphNode = next(node for node in state.action_surface if node.full_name == line)
        except StopIteration:
            print(f"Skipping {line}")
            continue
        if node.causal_mode == "action":
            state = simulator.step({attacker_name: [node]})[attacker_name]
            if node in state.performed_nodes:
                print(f"Node {node.full_name} performed")
            else:
                print(f"Node {node.full_name} not performed")
                raise Exception(f"Node {node.full_name} not performed")
        elif node.causal_mode == "effect":
            print(f"Skipping effect {node.full_name}")
        