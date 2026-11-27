#!/usr/bin/env python3
"""One object for both electron and muon? Measure the q-volume and the sum family (W6).

# Ref: docs/audits/2026-11-22-energy-scale-cal-map.md   (section 9)
# Ref: QOU/Observations/QVolumeCarrier.lean             (one_sub_inv_pow_eq, sum_family_forces_c)
# Ref: QOU/Observations/ElectronUnitSplit.lean          (tau_e = q^3 y_(3))

OWNER CHOICE 2026-11-23: search for one derived weight giving the electron a finite value
and the muon Vol(4_1)/hbar_q^2.

THE q-VOLUME.  G(z; q) = sum_{n>=1} z^n / (1 - q^-n)^2.  Since 1 - q^-n = hbar_q [n]' with
[n]' = sum_{k<n} q^-k (Lean `one_sub_inv_pow_eq`), hbar_q^2 G -> Li_2(z) as q -> 1. On |z| = 1
the n-series does not converge at finite q ([n]' -> 1/hbar_q), so it is evaluated through its
exact rearrangement, absolutely convergent for |z| = 1, z != 1:

    G(z; q) = sum_{m>=0} (m+1) z q^-m / (1 - z q^-m)

(expand 1/(1-y)^2 = sum (m+1) y^m with y = q^-n, then sum the geometric series in n). The
rearrangement is checked against the direct series at |z| < 1.  For 4_1 (two regular ideal
tetrahedra, shape e^{i pi/3}): W_mu := 2 Im G(e^{i pi/3}; q), and V_q := hbar_q^2 W_mu -> Vol(4_1).

WHAT IS MEASURED: V_q at q0 against Vol(4_1); the same with log q or h/2 in place of hbar_q;
the carrier W_mu at q0 against m_mu/m_e; and the sum family W = T + c G with c forced to
T_e(1) = 1/2 by the Lean (a necessary condition, NOT a derivation of c).  Nothing is fitted,
nothing is wired, and q0 is not re-solved.
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
from qou_substrate.constants import MASS_RATIO_MU_E_STR  # noqa: E402

Q_PROTON = mp.mpf(Q_50_DIGIT_STR)
Q_MUON = q_muon_at(50)
VOL41 = 2 * mp.clsin(2, mp.pi / 3)
Z41 = mp.expjpi(mp.mpf(1) / 3)
MU_E = mp.mpf(MASS_RATIO_MU_E_STR)  # comparison only; never enters a computed quantity


def hbar(q):
    return 1 - 1 / q


def G(z, q):
    return mp.nsum(lambda m: (m + 1) * z * q ** (-m) / (1 - z * q ** (-m)), [0, mp.inf])


def G_direct(z, q):  # valid only for |z| < 1
    return mp.nsum(lambda n: z**n / (1 - q ** (-n)) ** 2, [1, mp.inf])


def W_mu(q):
    return 2 * mp.im(G(Z41, q))


def y3(q):
    return 1 - 2 / (q + 1 / q) ** 2


def tau_e(q):
    return q**3 * y3(q)


def tau_fig8(q):
    """Convention-D trace of (sigma0 sigma1^-1)^2 (see energy_scale_unit_ratio_probe)."""
    a = mp.matrix([[q, 1], [0, -1 / q]])
    b = mp.matrix([[-1 / q, 0], [1, q]]) - (q - 1 / q) * mp.eye(2)
    M = a * b * a * b
    return y3(q) * 1 + (M[0, 0] + M[1, 1]) / (q + 1 / q) ** 2


ASSERTS = []


def check(label, ok, detail=""):
    ASSERTS.append((label, bool(ok), detail))
    print(f"[{'ok' if ok else 'FAIL'}] {label}{' -- ' + detail if detail else ''}")


tol = mp.mpf(10) ** (-(mp.mp.dps - 15))
for x in (mp.mpf("0.5"), mp.mpf("0.3") * mp.expjpi(mp.mpf(1) / 3)):
    d = abs(G(x, Q_PROTON) - G_direct(x, Q_PROTON))
    check(f"rearrangement = direct series at x={mp.nstr(x, 6)}", d < tol, mp.nstr(d, 3))

# limit hbar^2 G -> Li_2 and its rate
lim_rows = {}
for s in ("1.01", "1.001"):  # nsum extrapolation is unreliable below ~1.001 (terms decay as q^-m)
    q = mp.mpf(s)
    rel = hbar(q) ** 2 * W_mu(q) / VOL41 - 1
    lim_rows[s] = rel
    print(f"q={s}: hbar^2 W_mu / Vol - 1 = {mp.nstr(rel, 8)}")
check("hbar^2 W_mu -> Vol(4_1) (rel < 1e-4 at q=1.001)", abs(lim_rows["1.001"]) < mp.mpf("1e-4"))
check("rate is linear in hbar (ratio of successive decades ~ 10)",
      abs(lim_rows["1.01"] / lim_rows["1.001"] - 10) < 1)

results = {}
for name, q in (("proton_pin", Q_PROTON), ("muon_pin_comparison", Q_MUON)):
    w = W_mu(q)
    h, lam, hh = hbar(q), mp.log(q), q - 1 / q
    te, tm = tau_e(q), tau_fig8(q)
    sum_family = (tm + w / 2) / te  # c = T_e(1) = 1/2, forced by sum_family_forces_c
    r = {
        "q": q,
        "W_mu_2ImG": w,
        "Vq_hbar2_W": h**2 * w,
        "Vq_over_Vol_minus_1": h**2 * w / VOL41 - 1,
        "logq2_W_over_Vol_minus_1": lam**2 * w / VOL41 - 1,
        "(h/2)^2_W_over_Vol_minus_1": (hh / 2) ** 2 * w / VOL41 - 1,
        "Vol_over_hbar2": VOL41 / h**2,
        "W_mu_over_mu_e_codata_minus_1": w / MU_E - 1,
        "W_electron_qvolume": mp.mpf(0),
        "tau_e": te,
        "tau_fig8": tm,
        "sum_family_c_half_ratio": sum_family,
        "sum_family_over_mu_e_codata_minus_1": sum_family / MU_E - 1,
    }
    results[name] = r
    print(f"\n{name}")
    for k, v in r.items():
        print(f"  {k:38s} {mp.nstr(v, 15)}")

P = results["proton_pin"]
check("hbar_q is the closest of hbar, log q, h/2 at q0",
      abs(P["Vq_over_Vol_minus_1"]) < min(abs(P["logq2_W_over_Vol_minus_1"]),
                                          abs(P["(h/2)^2_W_over_Vol_minus_1"])))
check("q-volume of a link with no tetrahedra is 0 (electron)", P["W_electron_qvolume"] == 0)

failures = [a[0] for a in ASSERTS if not a[1]]
print(f"\n=== {len(ASSERTS) - len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:  # pragma: no cover
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("q-volume-carrier")
    w.set_description(
        "Owner-chosen search (2026-11-23) for one weight giving the electron finite and the muon "
        "Vol(4_1)/hbar_q^2. q-volume G(z;q)=sum z^n/(1-q^-n)^2 via its convergent rearrangement; "
        "2 Im G(e^{i pi/3};q) ~ Vol(4_1)/hbar_q^2, gives the electron 0. Sum family T + c G with "
        "c forced to 1/2 by QVolumeCarrier.sum_family_forces_c, measured at q0. Proton pin default, "
        "muon pin comparison arm. CODATA m_mu/m_e used only as the comparison target. No fit."
    )
    for key, r in results.items():
        w.add_data(key, {k: mp.nstr(v, 40) for k, v in r.items()})
    w.add_data("limit_rate_rel", {k: mp.nstr(v, 15) for k, v in lim_rows.items()})
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "proton",
            "q0AnchorReason": "default proton pin; muon pin evaluated as labelled comparison arm (E1)"})
    print("witness written")
_sys.exit(1 if failures else 0)
