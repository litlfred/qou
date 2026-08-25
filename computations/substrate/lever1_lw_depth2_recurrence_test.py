"""Option 3: does a_D^(n)=lw(n-1) satisfy a CONSTANT-coefficient depth-2 recurrence?

The M-workplan (2026-06-06) posits B in SL2, det=1, tau=tr B, with prolonged periods
a_D^(n)=lw(n-1) and a "verification" a_D^(5)=tau*a_D^(4)-a_D^(3). tau is SOLVED from the
n<=4 seed, so the n>=5 checks are the real test. Any a_D^(n)=phi(M^n v0) MUST satisfy the
depth-2 recurrence exactly (Cayley-Hamilton: M^2=tau M - I). So if lw fails it, lw is NOT
the prolonged periods of a fixed 2x2 M -- the audit fork (b).

lw(c) = (1/(c+1)) Sum_{lam|-c+1} dim_q(lam),  dim_q = [n]_q!/prod[hook]_q, symmetric
[k]_q = (q^k-q^-k)/(q-q^-1).  No fit; symbolic in q + 50-dps at q0.
"""

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402
import json, os, sys
sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
import sympy as sp
import mpmath as mp
from qou_substrate import constants as C

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from young_qdim import q, S  # noqa: E402

# lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q(λ) = S(c+1)/(c+1) (shared cached machinery; bean z3a2, PR #2952)
def lw(c):
    return sp.cancel(S(c + 1) / (c + 1))

LW = {c: lw(c) for c in range(1, 7)}                 # lw(1..6)
tau_seed = sp.cancel((LW[1] + LW[3]) / LW[2])        # solved from n=2,3,4
tau_cf = sp.cancel(3*(3*q**4 + 8*q**2 + 3) / (4*q*(q+1)**2))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
q0 = mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q))
def ev(e): return mp.mpf(str(sp.N(e.subs(q, q0), 40)))

# windowed tau_k = (a_D^(k)+a_D^(k+2))/a_D^(k+1) = (lw(k-1)+lw(k+1))/lw(k)
def tau_window(k): return sp.cancel((LW[k-1] + LW[k+1]) / LW[k])   # k>=2
tau_w = {k: tau_window(k) for k in (2, 3, 4)}        # 3 overlapping windows

# residuals lw(c+1) - (tau_seed*lw(c) - lw(c-1)) for c=3,4,5  (a_D n=5,6,7 checks)
res = {c+2: sp.cancel(LW[c+1] - (tau_seed*LW[c] - LW[c-1])) for c in (3, 4, 5)}

results = {
    "lw": {c: mp.nstr(ev(LW[c]), 16) for c in range(1, 7)},
    "tau_seed_n234": mp.nstr(ev(tau_seed), 16),
    "tau_closed_form": mp.nstr(ev(tau_cf), 16),
    "tau_seed_eq_closed_form": bool(sp.cancel(tau_seed - tau_cf) == 0),
    "tau_windows": {f"n{k},{k+1},{k+2}": mp.nstr(ev(tau_w[k]), 12) for k in (2, 3, 4)},
    "recurrence_residuals_seed_tau": {f"n={n}": mp.nstr(ev(res[n]), 8) for n in (5, 6, 7)},
    "residual_rel_to_lw_at_n5": mp.nstr(ev(res[5]) / ev(LW[4]), 6),
    "theta_binding_seed": mp.nstr(mp.acosh(ev(tau_seed)/2), 12),
}
assertions = {
    "tau_seed_eq_closed_form": bool(sp.cancel(tau_seed - tau_cf) == 0),
    "n5_recurrence_FAILS": bool(res[5] != 0),
    "n6_recurrence_FAILS": bool(res[6] != 0),
    "n7_recurrence_FAILS": bool(res[7] != 0),
    "windowed_kernel_NOT_constant": bool(sp.cancel(tau_w[2] - tau_w[3]) != 0),
    "lw2_matches_corpus": bool(sp.cancel(LW[2] - (q+1)**2/(3*q)) == 0),
    "lw3_matches_familyA": bool(sp.cancel(LW[3] - (3*q**2 + 4 + 3/q**2)/4) == 0),
}
all_passed = all(assertions.values())

witness = {
    "computation": "lever1_lw_depth2_recurrence_test",
    "description": (
        "Tests whether a_D^(n)=lw(n-1) satisfies a CONSTANT-coefficient depth-2 recurrence "
        "(R=x^2-tau x+1). tau solved from the n<=4 seed = 2.6424 (= closed form), but the n=5 "
        "check lw(4)=tau*lw(3)-lw(2) FAILS (residual 0.0205, 0.4% of lw(4)); n=6 fails by 14%; "
        "n=7 worse. The windowed kernel drifts (tau_{n2,3,4}=2.6424 vs tau_{n3,4,5}=2.6505). A "
        "const-coeff depth-2 recurrence has a window-independent kernel, so lw(c) does NOT "
        "satisfy one => lw(n-1) != phi(M^n v0) for any fixed 2x2 M (Cayley-Hamilton). The "
        "a_D=lw prolonged-period identification is seed-deep only. lw(2)=(q+1)^2/(3q) and "
        "lw(3)=Family-A match the corpus exactly (convention validated)."
    ),
    "discipline": (
        "no fit; sympy symbolic in q + mpmath 50dps at q0; (b)-exclusion of the const-coeff "
        "depth-2 model, invariant = window-independence of a const-coeff linear-recurrence "
        "kernel; scoped: refutes a_D=lw-as-prolonged-periods BEYOND the seed + the n=5 "
        "verification claim, NOT the Jac(Bring)~E^4 isogeny or the existence of a 2x2 M."
    ),
    "auditOnly": "docs/audits/2026-06-24-lever1-lw-depth2-recurrence-falsified.md",
    "results": results,
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": (
        "DEPTH-2 CONSTANT-COEFFICIENT RECURRENCE FALSIFIED FOR lw(c) BEYOND THE SEED. tau fit to "
        "n<=4 (=2.6424, the closed form) fails the n=5 verification (lw(4) off by 0.0205 = 0.4%), "
        "n=6 by 14%, n=7 worse; the windowed kernel drifts 2.6424 -> 2.6505. So the selection-rule "
        "values lw(c) are NOT the prolonged periods phi(M^n v0) of a fixed 2x2 SL2 M (those satisfy "
        "the recurrence exactly by Cayley-Hamilton). theta_binding=arccosh(tau/2)=0.7815 is a "
        "3-point SEED-FIT artifact, not a derived recurrence rate -- this is the audit fork (b), "
        "concrete. The a_D=lw identification holds only at the n=2,3,4 anchors (a near-match, not a "
        "derivation, exactly the cross-anchor pattern the canonical discipline flags). Does NOT "
        "refute the Jac(Bring)~E^4 isogeny (sibling mass-open-keystone, correct) or the 2x2 M's "
        "existence -- it refutes that the lw values ARE that M's prolonged periods. No fit."
    ),
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "lever1-lw-depth2-recurrence-test.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2)
    f.write("\n")

for c in range(1, 7): print(f"  lw({c}) = {results['lw'][c]}")
print(f"\n  tau_seed = {results['tau_seed_n234']}  (closed form {results['tau_closed_form']})")
print(f"  tau windows: {results['tau_windows']}")
print(f"  residuals (seed tau): {results['recurrence_residuals_seed_tau']}")
print()
for k, v in assertions.items(): print(f"  [{'PASS' if v else 'FAIL'}] {k}")
print(f"\nallPassed = {all_passed}\nwitness -> {out}")
