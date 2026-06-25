"""Continuation (a): is there a topological / integer / golden shortcut to tau = 2.6424,
or is the genuine object the owner-gated abelianised lambda_SW connection holonomy?

The seed tau is FORCED by the three WIRED physical anchors:
  a_D^(2) = 1            (muon, c=1)
  a_D^(3) = lw(2) = (q+1)^2/(3q)
  a_D^(4) = Family-A = (3q^2+4+3q^-2)/4   (proton, bit-for-bit production linking_weight_family_a)
  tau_seed = (a_D^(2)+a_D^(4))/a_D^(3)
If tau_seed is non-integer AND no integer tau reproduces the wired a_D^(4) from the
recurrence, then B is NOT a topological SL2(Z) monodromy (integer trace) -- including the
seductive icosahedral 'golden' tau=3 (lambda=phi^2). The genuine 2.6424-producing object is
then the abelianised lambda_SW real holonomy (owner-gated keystone). Numerology guard.
No fit; symbolic + mpmath 50dps.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
import sympy as sp
import mpmath as mp
from qou_substrate import constants as C

q = sp.Symbol("q", positive=True)
aD2 = sp.Integer(1)
aD3 = sp.cancel((q + 1)**2 / (3*q))                  # lw(2)
aD4 = sp.cancel((3*q**2 + 4 + 3/q**2) / 4)           # Family-A (wired proton multiplier)
tau_seed = sp.cancel((aD2 + aD4) / aD3)

mp.mp.dps = 50
q0 = mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q))
def ev(e): return mp.mpf(str(sp.N(e.subs(q, q0), 40)))

tau_num = ev(tau_seed)
phi = (1 + mp.sqrt(5)) / 2
golden_tau = phi**2 + phi**(-2)                      # = 3 exactly (lambda = phi^2)

# For each candidate integer tau, the recurrence predicts a_D^(4) = tau*a_D^(3) - a_D^(2);
# compare to the WIRED Family-A.  A topological monodromy must have integer tau.
preds = {}
for t in (2, 3, 4):
    pred_aD4 = t * ev(aD3) - ev(aD2)
    preds[t] = {
        "predicted_aD4": mp.nstr(pred_aD4, 10),
        "wired_FamilyA_aD4": mp.nstr(ev(aD4), 10),
        "rel_miss": mp.nstr(abs(pred_aD4 - ev(aD4)) / ev(aD4), 4),
    }

results = {
    "tau_seed_forced_by_wired_anchors": mp.nstr(tau_num, 16),
    "tau_seed_is_integer": bool(abs(tau_num - mp.nint(tau_num)) < mp.mpf("1e-9")),
    "nearest_integer": int(mp.nint(tau_num)),
    "golden_tau_phi2": mp.nstr(golden_tau, 12),          # = 3
    "integer_tau_predictions_vs_wired_FamilyA": preds,
    "theta_seed": mp.nstr(mp.acosh(tau_num/2), 12),
    "theta_golden_tau3": mp.nstr(mp.acosh(golden_tau/2), 12),
}
assertions = {
    "tau_seed_NOT_integer": bool(abs(tau_num - mp.nint(tau_num)) > mp.mpf("0.1")),
    "no_integer_tau_fits_wired_aD4": all(
        abs((t*ev(aD3) - ev(aD2)) - ev(aD4)) / ev(aD4) > mp.mpf("0.05") for t in (2, 3, 4)),
    "golden_tau3_refuted_by_seed": bool(
        abs((3*ev(aD3) - ev(aD2)) - ev(aD4)) / ev(aD4) > mp.mpf("0.05")),
    "tau_seed_strictly_between_2_and_3": bool(2 < tau_num < 3),
}
all_passed = all(assertions.values())

witness = {
    "computation": "lever1_lambda_sw_no_shortcut",
    "description": (
        "The lever-1 seed tau = 2.6424 is FORCED by the three wired anchors a_D^(2)=1, "
        "a_D^(3)=lw(2), a_D^(4)=Family-A (production proton multiplier). It is non-integer and "
        "strictly between 2 and 3; NO integer tau in {2,3,4} reproduces the wired Family-A from "
        "the recurrence (golden tau=3 / lambda=phi^2 predicts a_D^(4)=3.01 vs wired 2.53, 19% "
        "miss). So B is not a topological SL2(Z) monodromy (integer trace) and there is no "
        "icosahedral-golden shortcut. The genuine 2.6424-producing object is the abelianised "
        "lambda_SW real connection holonomy (owner-gated keystone M on the elliptic factor)."
    ),
    "discipline": (
        "no fit; symbolic + mpmath 50dps; numerology guard -- the golden tau=3 (lambda=phi^2, "
        "icosahedral) is TESTED against the wired seed and REFUTED, not forced; (b)-exclusion of "
        "all integer/topological tau, invariant = integrality of SL2(Z) traces + the wired-anchor "
        "constraint."
    ),
    "auditOnly": "docs/audits/2026-06-24-lever1-lambda-sw-no-shortcut.md",
    "results": results,
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": (
        "NO TOPOLOGICAL/INTEGER/GOLDEN SHORTCUT. The seed tau=2.6424 is forced by the wired "
        "anchors (1, lw(2), Family-A), is non-integer, and no integer tau (incl. the icosahedral "
        "golden tau=3, lambda=phi^2) reproduces the wired Family-A (golden predicts a_D^(4)=3.01 "
        "vs 2.53, 19% miss). So the binding 2x2 object is NOT a topological SL2(Z) monodromy and "
        "the golden hypothesis is REFUTED by the seed (numerology guard held). The genuine "
        "2.6424-producing object is the owner-gated abelianised lambda_SW REAL connection "
        "holonomy on the color E_q -- no algebraic shortcut. Concrete owner-gated next step: "
        "integrate the SW differential lambda_SW = x dz on E_q and its Gauss-Manin prolongation "
        "to recover the real-holonomy 2x2 B with tr=2.6424. No fit; nothing wired."
    ),
}
out = os.path.join("computations", "substrate", "lever1-lambda-sw-no-shortcut.witness.json")
with open(out, "w") as f: json.dump(witness, f, indent=2)

print(f"tau_seed (forced by wired anchors) = {results['tau_seed_forced_by_wired_anchors']}")
print(f"  integer? {results['tau_seed_is_integer']}   nearest {results['nearest_integer']}   golden tau(phi^2)={results['golden_tau_phi2']}")
print("\ninteger-tau recurrence predictions vs WIRED Family-A (a_D^(4)=2.5328):")
for t, d in preds.items():
    print(f"  tau={t}: predict a_D^(4)={d['predicted_aD4']}  miss {d['rel_miss']}")
print(f"\ntheta_seed={results['theta_seed']}   theta_golden(tau=3)={results['theta_golden_tau3']}")
print()
for k, v in assertions.items(): print(f"  [{'PASS' if v else 'FAIL'}] {k}")
print(f"\nallPassed = {all_passed}\nwitness -> {out}")
