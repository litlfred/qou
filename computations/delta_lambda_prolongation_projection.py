#!/usr/bin/env python3
"""
EXPLORATORY — Delta_lambda: Projection from the Prolongation Kernel (Dual Route)
Project the super-exponentially decaying weights w_n(K) back onto the H_{3A} partition basis lambda.
"""
from __future__ import annotations
import sys
from pathlib import Path
import mpmath as mp
import json

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
import _path_bridge
from q_parameter import q_at
from _precision import set_compute_dps
from codata_constants import (
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION)
from coulomb_energy import coulomb_energy_mev
try:
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except Exception:
    _HAVE_WB = False

set_compute_dps()
q = q_at(mp.mp.dps)
M_E = mp.mpf(str(M_E_MEV))
_NS = mp.mp.dps

def qint(k): return (q ** k - q ** (-k)) / (q - 1 / q)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n + 1): p *= qint(k)
    return p

def partitions(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k): yield (k,) + r

def hooks(lam):
    n = len(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hs = []
    for i in range(n):
        for j in range(lam[i]):
            hs.append((lam[i] - j - 1) + (conj[j] - i - 1) + 1)
    return hs

def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam): d /= qint(h)
    return d

def S_qinv(n): return mp.fsum(dimq(l) for l in partitions(n))
def a_D(n): return S_qinv(n + 1) / (n + 1)

AME_B = {"D": mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
         "T": mp.mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
         "3He": mp.mpf(str(AME_B_HE3_MEV_VALIDATION)),
         "4He": mp.mpf(str(AME_B_HE4_MEV_VALIDATION))}
ZA = {"D": (1, 2), "T": (1, 3), "3He": (2, 3), "4He": (2, 4)}

def load_chi(filename):
    path = _path_bridge.witness_path(filename, HERE)
    w = json.loads(path.read_text())
    return w["by_partition"], mp.mpf(w["tr_M_at_q0"])

def main() -> int:
    aD = {n: a_D(n) for n in (2, 3, 4)}
    Bstrong = {}
    for K, (Z, A) in ZA.items():
        ec = mp.mpf(str(coulomb_energy_mev(Z, A)))
        Bstrong[K] = AME_B[K] + ec

    B3 = (Bstrong["T"] + Bstrong["3He"]) / 2
    w = {}
    w[2] = Bstrong["D"] / (M_E * aD[2])
    w[3] = (B3 / M_E - aD[2] * w[2]) / aD[3]
    w[4] = (Bstrong["4He"] / M_E - aD[2] * w[2] - aD[3] * w[3]) / aD[4]

    print("Projection from Prolongation Kernel:")
    print("w_2 =", w[2])
    print("w_3 =", w[3])
    print("w_4 =", w[4])

    part_D, tr_D = load_chi("chi-deuteron-h6-at-q0-50dps.witness.json")
    print(f"Deuteron: B_strong = {Bstrong['D']}, tr_M_at_q0 = {tr_D}")
    
    # We want to solve for Delta_lambda: m_e * sum(y_l * chi_l * Delta_l) = Bstrong['D'] = m_e * aD[2] * w[2]
    # This implies the dual projection constraint: sum(y_l * chi_l * Delta_l) = aD[2] * w[2]
    
    sum_y_chi = sum(mp.mpf(p["y_lambda"]) * mp.mpf(p["chi_lambda"]) for p in part_D)
    print(f"sum(y_l * chi_l) = {sum_y_chi}")
    print(f"Target: aD[2] * w[2] = {aD[2] * w[2]}")
    
    # Check if a single w_n assigns to the trace
    print(f"tr_M * w_2 = {tr_D * w[2]}")

    if _HAVE_WB:
        wb = WitnessBuilder("delta-lambda-prolongation-projection", engine="mpmath", output_dir=HERE)
        wb.set_description("Project w_n(K) onto H_3A partition basis to algebraically constrain Delta_lambda.")
        wb.add_parameter("w2", mp.nstr(w[2], _NS))
        wb.add_parameter("w3", mp.nstr(w[3], _NS))
        wb.add_parameter("w4", mp.nstr(w[4], _NS))
        wb.add_data("deuteron_constraint", {
            "sum_y_chi": mp.nstr(sum_y_chi, _NS),
            "target": mp.nstr(aD[2] * w[2], _NS)
        })
        wb.save()
        
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
