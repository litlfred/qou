import mpmath as mp
import sys
mp.mp.dps = 50
sys.path.insert(0, '/Users/litlfred/space_cats/qou/computations/probes')
from hecke_channel_binding_probe import Q0, E0
from deuteron_fpn_wlambda_wiring import gate_qdim, gate_qfact, gate_Z

f_req = mp.exp(-mp.mpf("2.224566") / E0)

# Check AGENTS.md for "fibre"
with open("/Users/litlfred/space_cats/qou/AGENTS.md") as f:
    for line in f:
        if "fibre" in line.lower() or "root-of-unity" in line.lower() or "observable" in line.lower():
            print(line.strip())

