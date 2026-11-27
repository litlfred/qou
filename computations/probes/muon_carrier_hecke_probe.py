#!/usr/bin/env python3
"""Is there a canonical Hecke / trace reading of the muon carrier Vol(4_1)/hbar_q^2?  (bean qou-91w7)

# Ref: QOU/Transcendental/MassTheory/MuonCarrierHeckeObstruction.lean
# Ref: QOU/Observations/ElectronUnitSplit.lean, QOU/Observations/QVolumeCarrier.lean
# Ref: docs/audits/2026-11-22-energy-scale-cal-map.md  (sections 8, 9, 10)

Measures, at the proton pin, the candidates the Lean module treats structurally:

1. the q-volume G(z;q) as the q-log-derivative of the quantum dilogarithm
   P(z;q) = prod_{k>=0}(1 - z q^-k):  G(z;q) = (q d/dq log P)(zq; q)  (checked to working precision);
2. the "energy reading" w = q d/dq log Z applied to both electron (Z = tau_e) and muon:
   w_e(1) = 3 (the writhe), so the reading's carrier is ~ Vol/(3 hbar^2), not Vol/hbar^2;
3. the volume-conjecture reading (Kashaev invariant of 4_1 at q = e^{2 pi i/N}): the volume
   sits at order 1/hbar in the exponent, log <4_1>_N ~ N Vol/(2 pi), not at order 1/hbar^2.

Model quantities only. Nothing is fitted; the muon pin is not used. The numbers are diagnostics
for the audit, never inputs to the Lean.
"""
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
for _p in (_Path(__file__).resolve().parent.parent,
           _Path(__file__).resolve().parent.parent / "substrate"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0 = mp.mpf(Q_50_DIGIT_STR)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)
Z6 = mp.expjpi(mp.mpf(1) / 3)  # e^{i pi/3}, shape of both tetrahedra of 4_1

ASSERTS = []


def check(label, ok, detail=""):
    ASSERTS.append((label, bool(ok), detail))
    print(f"[{'ok' if ok else 'FAIL'}] {label}{' -- ' + detail if detail else ''}")


def hbar(q):
    return 1 - 1 / q


def G(z, q):
    """q-volume, Lambert form (as in q_volume_carrier_probe): sum_m (m+1) z q^-m/(1 - z q^-m)."""
    return mp.nsum(lambda m: (m + 1) * z * q ** (-m) / (1 - z * q ** (-m)), [0, mp.inf])


def log_P(w, q):
    """log prod_{k>=0} (1 - w q^-k), |q| > 1."""
    return mp.nsum(lambda k: mp.log(1 - w * q ** (-k)), [0, mp.inf])


def tau_e(q):
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


tol = mp.mpf(10) ** (-(mp.mp.dps - 15))

# 1. G = q d/dq log P, z held fixed in the derivative, then evaluated at w = z q.
wq = Z6 * Q0
dlogP = Q0 * mp.diff(lambda t: log_P(wq, t), Q0)
g0 = G(Z6, Q0)
err = abs(g0 - dlogP)
check("G(z;q) = (q d/dq log P)(zq;q) at q0, z = e^{i pi/3}", err < mp.mpf(10) ** -30, mp.nstr(err, 5))

carrier = VOL41 / hbar(Q0) ** 2
w_mu = 2 * mp.im(g0)

# 2. energy reading on the electron
w_e0 = Q0 * mp.diff(lambda t: mp.log(tau_e(t)), Q0)
w_e1 = mp.diff(lambda t: mp.log(tau_e(t)), mp.mpf(1))
check("q d/dq log tau_e at q = 1 equals 3 (writhe)", abs(w_e1 - 3) < tol, mp.nstr(w_e1, 30))
y3 = lambda q: (q**4 + 1) / (q**2 + 1) ** 2  # noqa: E731
w_y3_1 = mp.diff(lambda t: mp.log(y3(t)), mp.mpf(1))
check("unframed part y3 contributes 0 at q = 1 (bar-invariance)", abs(w_y3_1) < tol, mp.nstr(w_y3_1, 5))
ratio_energy = w_mu / w_e0
check("energy-reading carrier is not Vol/hbar^2 (ratio to carrier < 1/2)",
      ratio_energy / carrier < mp.mpf(1) / 2, mp.nstr(ratio_energy / carrier, 12))

# 3. Kashaev invariant of 4_1: <4_1>_N = sum_{k<N} |(q;q)_k|^2, q = e^{2 pi i/N}
kash = {}
for N in (50, 100, 200, 400):
    qN = mp.expjpi(mp.mpf(2) / N)
    s, prod = mp.mpf(0), mp.mpc(1)
    for k in range(N):
        s += abs(prod) ** 2
        prod *= 1 - qN ** (k + 1)
    lg = mp.log(s)
    kash[N] = {"log_kashaev": lg, "N_Vol_over_2pi": N * VOL41 / (2 * mp.pi),
               "abs_hbar": abs(1 - 1 / qN)}
    print(f"N={N:4d}  log<4_1>_N = {mp.nstr(lg, 12)}  N Vol/2pi = {mp.nstr(N*VOL41/(2*mp.pi), 12)}")
# slope of log <4_1>_N in N tends to Vol/(2 pi): first order in 1/hbar
slope = (kash[400]["log_kashaev"] - kash[200]["log_kashaev"]) / 200
check("Kashaev slope d log<4_1>_N / dN -> Vol/(2 pi) (within 2%)",
      abs(slope / (VOL41 / (2 * mp.pi)) - 1) < mp.mpf("0.02"), mp.nstr(slope / (VOL41 / (2 * mp.pi)), 8))

row = {"q0": Q0, "hbar_q0": hbar(Q0), "Vol41": VOL41, "carrier_Vol_over_hbar2": carrier,
       "two_Im_G_e_ipi3": w_mu, "two_Im_G_over_carrier": w_mu / carrier,
       "w_e_energy_q0": w_e0, "energy_reading_ratio": ratio_energy,
       "energy_reading_over_carrier": ratio_energy / carrier}
print()
for k, v in row.items():
    print(f"  {k:30s} {mp.nstr(v, 20)}")

failures = [a[0] for a in ASSERTS if not a[1]]
print(f"\n=== {len(ASSERTS) - len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:  # pragma: no cover
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("muon-carrier-hecke")
    w.set_description(
        "Diagnostics for the canonical-chart question of the muon carrier Vol(4_1)/hbar_q^2 "
        "(bean qou-91w7). Checks G = q d/dq log P (quantum dilogarithm), the energy reading "
        "w = q d/dq log Z on electron and muon (electron weight -> 3, the writhe; carrier off "
        "by ~1/3), and that the Kashaev invariant of 4_1 carries the volume at order 1/hbar in "
        "the exponent. Proton pin; nothing fitted."
    )
    w.add_data("proton_pin", {k: mp.nstr(v, 40) for k, v in row.items()})
    w.add_data("kashaev_4_1", {str(N): {k: mp.nstr(v, 30) for k, v in d.items()} for N, d in kash.items()})
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "proton", "q0AnchorReason": "default proton pin; muon pin not used"})
    print("witness written")
_sys.exit(1 if failures else 0)
