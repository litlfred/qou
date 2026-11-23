#!/usr/bin/env python3
"""How far apart are the corpus's two electron units at q0?  (W6, beans qou-91w7 / qou-6gf9)

# Ref: docs/audits/2026-11-22-energy-scale-cal-map.md  (section 3 item 4, section 6)
# Ref: QOU/Observations/EnergyScaleMap.lean           (Chart.calibration_does_not_fix_unit)
# Ref: QOU/QBeta/E0WeightCandidates.lean               (tau_electron)

WHAT THIS MEASURES.  The audit shows that CAL-1 fixes the map from categorical
energy to MeV only once the electron's categorical weight w_e is fixed, and that
the corpus uses two different w_e:

  trace pipeline : w_e = tau_e(q) = q^3 (q^4 + 1) / (q^2 + 1)^2
                   (convention-D Markov trace of sigma0 sigma1 sigma0, Hopf closure)
  mass formula   : w_e = hbar_q^2,  hbar_q = 1 - 1/q

Each chart sets unit = m_e / w_e, so the ratio of the two units is

  R(q) = unit_mass / unit_trace = tau_e(q) / hbar_q^2 .

R is the factor by which a categorical weight read in one pipeline and converted
with the other pipeline's unit comes out wrong.  It is a ratio of two model
quantities: no measured value enters it except through q0 itself.

WHAT IT DOES NOT DO.  It does not say which unit is canonical; the calibrations
cannot decide that (Chart.calibration_does_not_fix_unit).  It fits nothing.

PINS.  The proton pin is the default (owner directive 2026-08-07).  The muon pin
(CAL-2, CODATA 2022) is evaluated as a labelled comparison arm, exception E1, to
show that R is insensitive to the pin at the digits quoted.
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
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402

Q_PROTON = mp.mpf(Q_50_DIGIT_STR)
Q_MUON = q_muon_at(50)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)  # Vol(4_1) = 2 Cl_2(pi/3) = 6 Lambda(pi/3)


def tau_e(q):
    return q**3 * (q**4 + 1) / (q**2 + 1) ** 2


def hbar(q):
    return 1 - 1 / q


def row(q):
    t = tau_e(q)
    h2 = hbar(q) ** 2
    return {
        "q": q,
        "tau_e": t,
        "hbar_sq": h2,
        "R_unit_mass_over_unit_trace": t / h2,
        "E0_over_me": 1 / (q * (q - 1)),
        "c_q_sq": 1 / (q - 1) ** 2,
        "Vol41_over_hbar_sq": VOL41 / h2,
    }


ASSERTS = []


def check(label, ok, detail=""):
    ASSERTS.append((label, bool(ok), detail))
    print(f"[{'ok' if ok else 'FAIL'}] {label}{' -- ' + detail if detail else ''}")


P = row(Q_PROTON)
M = row(Q_MUON)
for name, r in (("proton pin (default)", P), ("muon pin (comparison)", M)):
    print(f"\n{name}")
    for k, v in r.items():
        print(f"  {k:30s} {mp.nstr(v, 20)}")

# Exact symbolic checks at q = 1 (the obstruction in the Lean): tau_e(1) = 1/2,
# hbar(1) = 0, so R has a double pole there.  Checked with exact rationals.
check("tau_e(1) = 1/2 (traceD_one: 2^(c-n), c=2, n=3)", tau_e(mp.mpf(1)) == mp.mpf(1) / 2)
check("hbar(1) = 0", hbar(mp.mpf(1)) == 0)

# Identity cross-check: R = tau_e * q^2 * c_q^2, to working precision.
for r in (P, M):
    lhs = r["R_unit_mass_over_unit_trace"]
    rhs = r["tau_e"] * r["q"] ** 2 * r["c_q_sq"]
    check(f"R = tau_e q^2 c_q^2 at q={mp.nstr(r['q'], 12)}",
          abs(lhs - rhs) < mp.mpf(10) ** (-(mp.mp.dps - 10)))

rel = abs(P["R_unit_mass_over_unit_trace"] / M["R_unit_mass_over_unit_trace"] - 1)
print(f"\nrelative pin sensitivity of R: {mp.nstr(rel, 6)}")
check("R pin-insensitive below 1e-6 relative", rel < mp.mpf("1e-6"), mp.nstr(rel, 6))

failures = [a[0] for a in ASSERTS if not a[1]]
print(f"\n=== {len(ASSERTS) - len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:  # pragma: no cover
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("energy-scale-unit-ratio")
    w.set_description(
        "Ratio of the two electron units in the corpus at q0: the mass-formula unit "
        "m_e/hbar_q^2 over the trace-pipeline unit m_e/tau_e, i.e. R = tau_e/hbar_q^2 "
        "with tau_e = q^3(q^4+1)/(q^2+1)^2 the convention-D trace of sigma0 sigma1 "
        "sigma0 with Hopf closure. Model quantities only; nothing fitted. Proton pin "
        "default, muon pin (CODATA 2022) as a labelled comparison arm. Measures how "
        "far apart the two normalisations are; does not decide which is canonical."
    )
    for key, r in (("proton_pin", P), ("muon_pin_comparison", M)):
        w.add_data(key, {k: mp.nstr(v, 40) for k, v in r.items()})
    w.add_data("pin_sensitivity_rel", mp.nstr(rel, 10))
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "proton",
            "q0AnchorReason": "default proton pin; muon pin evaluated as labelled comparison arm (E1)"})
    print("witness written")
_sys.exit(1 if failures else 0)
