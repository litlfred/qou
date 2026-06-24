"""Lever-1: the binding monodromy B is HYPERBOLIC, not a compact-SU(2) trefoil holonomy.

Probe only — no fit, no production wiring. Sharpens the lever-1 `tr B` frontier
(docs/audits/2026-06-24-lever1-trB-geometric-target.md) with a structural (b)-exclusion
and a corpus synthesis:

  * The rank-2 object `B` acts on is the S5-Hodge MULTIPLICITY space of the irreducible
    4-dim S5 rep `W` in H^1(Bring) = W (x) C^2 (Riera-Rodriguez; the M-workplan
    2026-06-06, Lean `sl2_prolongation_recurrence`, det B = 1).
  * The coral elliptic curve E_z (brings-surface/coral-elliptic.md) has monodromy around
    its singular fibres = the trefoil holonomy generators H_1=sigma_1, H_2=sigma_2 in
    SU(2) (holonomy-trefoil.md), with (H_1 H_2)^3 = id  =>  |trace| <= 2 (compact/elliptic).
  * tau_binding = tr B = 2.6424 > 2  =>  B is HYPERBOLIC in SL2(R); a compact SU(2)
    element has |trace| <= 2 in the 2-dim rep, so B CANNOT be a compact trefoil-holonomy
    generator.  B is the NON-COMPACT (SU_q(2) -> E_q(2)) hyperbolic continuation at the
    substrate q0 > 1 -- the SAME growth-regime arena the keystone reached from the
    W_lambda / modular-category side (s5-so3-keystone ledger, 2026-06-22).

(b)-exclusion invariant cited: the trace dichotomy of SL2(R) / the |trace|<=2 bound on the
2-dim rep of compact SU(2).  This does NOT exclude the coral E_z as the rank-2 W (the curve
is fine; its monodromy is merely evaluated in the non-compact regime at q0>1) -- only the
COMPACT evaluation is excluded.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools", "qou-substrate", "python"))
import mpmath as mp
from qou_substrate import constants as C

mp.mp.dps = 50
q = mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q))
eta = mp.log(q)

# --- selection-rule values a_D^(n) = lw(n-1) (binding_selection_rule_tau_closure.py) ---
lw1 = mp.mpf(1)                       # c=1 (muon)
lw2 = (q + 1) ** 2 / (3 * q)          # c=2 closed form
lw3 = (3 * q ** 2 + 4 + 3 / q ** 2) / 4  # c=3 = Family-A
aD2, aD3, aD4 = lw1, lw2, lw3

tau_rule = (aD2 + aD4) / aD3
tau_cf = 3 * (3 * q ** 4 + 8 * q ** 2 + 3) / (4 * q * (q + 1) ** 2)
tau_torus = 2 * mp.cosh(2 * eta)      # = q^2 + q^-2 (multiplicative/Chebyshev torus sector)

theta_b = mp.acosh(tau_cf / 2)
theta_t = mp.acosh(tau_torus / 2)
lam_b = mp.exp(theta_b)               # hyperbolic eigenvalue lambda (B ~ diag(lambda, 1/lambda))
k_b = theta_b / eta                   # tau = q^k + q^-k would need integer k

# trefoil holonomy in SU(2): (H1 H2)^3 = id (3-cycle) => trace in {-1, +1}; all |.| <= 2
tr_H1H2 = 2 * mp.cos(2 * mp.pi / 3)   # = -1

results = {
    "q0": mp.nstr(q, 20),
    "eta0_ln_q0": mp.nstr(eta, 20),
    "tau_binding_selection_rule": mp.nstr(tau_rule, 20),
    "tau_binding_closed_form": mp.nstr(tau_cf, 20),
    "tau_rule_minus_closed_form": mp.nstr(abs(tau_rule - tau_cf), 5),
    "tau_torus_2cosh_2eta0": mp.nstr(tau_torus, 20),
    "theta_binding_acosh_tau_over_2": mp.nstr(theta_b, 20),
    "theta_torus_eq_2eta0": mp.nstr(theta_t, 20),
    "two_eta0": mp.nstr(2 * eta, 20),
    "lambda_binding_exp_theta": mp.nstr(lam_b, 20),
    "k_binding_theta_over_eta0": mp.nstr(k_b, 15),
    "theta_b_over_theta_t": mp.nstr(theta_b / theta_t, 15),
    "trefoil_tr_H1H2_3cycle": mp.nstr(tr_H1H2, 6),
}

assertions = {
    "rule_equals_closed_form": bool(abs(tau_rule - tau_cf) < mp.mpf(10) ** -40),
    "tau_binding_gt_2_hyperbolic": bool(tau_cf > 2),
    "tau_torus_gt_2_hyperbolic": bool(tau_torus > 2),
    "binding_ne_torus": bool(abs(tau_cf - tau_torus) > mp.mpf("0.5")),
    "trefoil_compact_abs_trace_le_2": bool(abs(tr_H1H2) <= 2),
    "binding_excluded_from_compact_su2": bool(tau_cf > 2),  # |tr|>2 => not compact SU(2)
    "k_binding_non_integer": bool(abs(k_b - mp.nint(k_b)) > mp.mpf("0.01")),
    "theta_torus_eq_2eta0": bool(abs(theta_t - 2 * eta) < mp.mpf(10) ** -40),
}
all_passed = all(assertions.values())

witness = {
    "computation": "lever1_binding_monodromy_hyperbolicity",
    "description": (
        "Lever-1 sharpening: the rank-2 binding monodromy B (tr B = tau = "
        "3(3q^4+8q^2+3)/(4q(q+1)^2) = 2.6424 at q0) is HYPERBOLIC (tau>2), so it is "
        "structurally excluded from the compact-SU(2) trefoil holonomy (|trace|<=2, "
        "(H1H2)^3=id) that is the coral elliptic E_z monodromy. B is the non-compact "
        "SU_q(2)->E_q(2) hyperbolic continuation at q0>1 -- the keystone's growth-regime "
        "arena reached from the binding side. Corpus synthesis of the 2026-06-06 M-workplan "
        "(H^1(Bring)=W(x)C^2, B in SL2, det=1) + coral-elliptic.md + holonomy-trefoil.md."
    ),
    "discipline": (
        "no fit; symbolic+mpmath 50dps; (b)-exclusion cites the SL2(R) trace dichotomy / "
        "compact-SU(2) |trace|<=2 invariant; does NOT exclude coral E_z as the rank-2 W "
        "(only its compact evaluation); not owner-gated (pure trace arithmetic)."
    ),
    "auditOnly": "docs/audits/2026-06-24-lever1-binding-monodromy-hyperbolicity.md",
    "results": results,
    "assertions": assertions,
    "allPassed": all_passed,
    "verdict": (
        "BINDING MONODROMY IS HYPERBOLIC, NOT COMPACT-SU(2). tau_binding=2.6424>2 puts B in "
        "the hyperbolic SL2(R) class; the trefoil holonomy (= coral E_z monodromy, compact "
        "SU(2), (H1H2)^3=id, tr=-1) is elliptic with |trace|<=2, so B is structurally "
        "excluded from being a compact trefoil-holonomy generator (b-exclusion, trace "
        "invariant). B is the non-compact SU_q(2)->E_q(2) continuation at q0>1 -- the SAME "
        "arena the keystone reached from the W_lambda side (independent convergence, binding "
        "vs generation). The rank-2 W is the S5-Hodge multiplicity space (= candidate H^1 of "
        "the coral elliptic E_z, Riera-Rodriguez isotypic factor), NOT a compact object. Open "
        "(rank-2, tractable, NOT genus-4): the coral E_z Picard-Fuchs hyperbolic rapidity "
        "theta_binding=0.7815 (k=7.489 non-integer, not a substrate q-power). No fit."
    ),
}

out = os.path.join(os.path.dirname(__file__), "lever1-binding-monodromy-hyperbolicity.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2)

for k, v in results.items():
    print(f"  {k:32s} = {v}")
print()
for k, v in assertions.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")
print(f"\nallPassed = {all_passed}")
print(f"witness  -> {out}")
