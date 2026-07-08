import sys
import os
sys.path.append(os.path.abspath('tools/qou-substrate/python'))
import qou_substrate.constants as qconstants
print(f"u: {qconstants.u_substrate}")
print(f"hbar_q^2: {qconstants.HBAR_Q**2}")
print(f"h_0^2: {qconstants.HA**2}")
