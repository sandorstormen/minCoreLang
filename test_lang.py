from pprint import pprint
from maltoolbox.language import LanguageGraph

import sys
first_arg = sys.argv[1] if len(sys.argv) > 1 else None
print("Loading language graph from", first_arg)
lang = LanguageGraph.from_mar_archive(first_arg)
print("Lang loaded successfully")
steps_causal = {}
for asset in lang.assets.values():
    for step in asset.attack_steps.values():
        steps_causal[step.full_name] = step.causal_mode
pprint(steps_causal)