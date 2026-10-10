import sys
sys.path.insert(0, 'computations')
from hecke_core import tr_M_at_q0
print(tr_M_at_q0(1, 0, False)[0])
