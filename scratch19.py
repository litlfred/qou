import sys
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from keystone_valuemap_qbessel_gate_s013 import run
res = run()
for a, c in res["derived_characters"].items():
    print(f"alpha={a}: support={c['support_1_30']} signs={c['signs_on_support']}")
