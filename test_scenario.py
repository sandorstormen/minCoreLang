import sys
from malsim import Scenario, MalSimulator
from malsim.config import MalSimulatorSettings
from malsim.config.sim_settings import RewardMode, TTCMode

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
simulator.run()
print(simulator.results)
