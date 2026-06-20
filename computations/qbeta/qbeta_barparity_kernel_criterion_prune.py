#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic bar-parity (sympy) of the Q_β c_k
# ladder; a CONSTRAINT/pruning result for the open fibre-kernel axis, no value-hunt.
"""
Q_β open-axis criterion 2(b) check: can the fibre kernel F(q) be bar-even in the
documented expansion variable u = b·ℏ_q²?

The open axis (docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
seeks a fibre-level Habiro element F(q) with F(qξ)=R(q,ξ)F(ξ), and lists as a
hard invariant (criterion 2b):
    "bar-evenness / q↦q⁻¹ symmetry of any F(q) (the c_2 = -1 rung is bar-even)".

This probe PRUNES that criterion symbolically (this is the sanctioned
"narrow before you scan" step 3 of the open-axis doc — a constraint on R, NOT a
real-q closed-form value-hunt, which is the gated/forbidden activity).

Substrate forms (qbeta_c3_jhopf_q0_vs_q1_comparison.py):
    b(q) = (q - q⁻¹)/(q + q⁻¹)        Hoefsmit base
    ℏ_q² = (1 - q⁻¹)²
    u    = b · ℏ_q²                    the c_k expansion variable
    J_Hopf(q) = -(q² + q⁻²)            Jones poly of the Hopf link, J_Hopf(1)=-2

Bar-parity bookkeeping (q↦q⁻¹):
    b(q) is bar-ODD  (b(q⁻¹) = -b(q), since (q-q⁻¹) odd / (q+q⁻¹) even)
    ℏ_q² ↦ q²ℏ_q²    (bar-covariant)
    ⇒ u ↦ -q²·u      (bar-ODD-covariant)
A bar-EVEN F(q)=Σ c_k u^k then forces, term by term,
    c_k(q⁻¹) = (-1)^k q^{-2k} c_k(q).
This probe tests whether the documented c_k satisfy it.

Exploratory; no fit, nothing wired.  Run:
  python3 -u computations/qbeta/qbeta_barparity_kernel_criterion_prune.py 2>&1 | tee /tmp/barp.log
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)


def bar(e):
    return e.subs(q, 1 / q)


def parity(e):
    """'even' if bar-orig=0, 'odd' if bar+orig=0, else 'mixed'."""
    if sp.simplify(bar(e) - e) == 0:
        return "even"
    if sp.simplify(bar(e) + e) == 0:
        return "odd"
    return "mixed"


def main() -> int:
    b = (q - 1 / q) / (q + 1 / q)
    h2 = (1 - 1 / q) ** 2
    u = b * h2
    J = -(q ** 2 + 1 / q ** 2)

    print("\n  Q_β CRITERION-2(b) PRUNE — can the fibre kernel be bar-even in u?\n")
    print("  | quantity | bar-parity | note |")
    print("  |---|---|---|")
    print(f"  | b(q)=(q-q⁻¹)/(q+q⁻¹) | {parity(b).upper()} | odd/even |")
    print(f"  | ℏ_q² | covariant (×q²) | (q-1)² type |")
    u_covar = sp.simplify(bar(u) - (-q ** 2 * u)) == 0
    print(f"  | u=b·ℏ_q² | ODD-covariant (→ -q²u): {u_covar} | b odd × ℏ² covariant |")
    print(f"  | J_Hopf=-(q²+q⁻²) | {parity(J).upper()} | classical Jones, J(1)=-2 |\n")

    # bar-even-F covariance law: c_k(1/q) = (-1)^k q^(-2k) c_k(q)
    candidates = [(2, sp.Integer(-1), "c2 = -1 (proved-exact)"),
                  (3, -2 - h2, "c3 = -2 - ℏ_q² (near-match)"),
                  (3, J, "c3 = J_Hopf(q) (near-match)")]
    print("  bar-even-F law  c_k(q⁻¹) = (-1)^k q^(-2k) c_k(q):")
    print("  | k | candidate | residual | satisfies? |")
    print("  |---|---|---|---|")
    results = {}
    any_pass = False
    for k, ck, lab in candidates:
        resid = sp.simplify(bar(ck) - (-1) ** k * q ** (-2 * k) * ck)
        ok = resid == 0
        any_pass = any_pass or ok
        results[lab] = {"k": k, "residual": str(resid), "satisfies": bool(ok)}
        print(f"  | {k} | {lab} | {resid} | {ok} |")

    print("\n  ---------------------------------------------------------------")
    print("  VERDICT (criterion-2b prune, no fit)")
    print("   * b(q) is bar-ODD ⇒ u = b·ℏ_q² is bar-ODD-covariant (u → -q²u).")
    print("   * The documented c₂=-1 (proved-exact) and BOTH c₃ candidates (-2-ℏ²,")
    print("     J_Hopf(q)) all VIOLATE the bar-even-F law c_k(q⁻¹)=(-1)^k q^(-2k)c_k(q).")
    print("   => Open-axis criterion 2(b) ('F(q) bar-even') CANNOT be imposed on the")
    print("      c_k ladder in the variable u: the bar-oddness of b(q) is incompatible")
    print("      with a bar-even kernel there.  The criterion's justification ('c₂=-1")
    print("      is bar-even') conflates bar-INVARIANCE of the constant with the")
    print("      covariance law a bar-even F needs in the bar-odd-covariant u.")
    print("   * Consistent picture: the bar-symmetry lives in the FULL Q_β (the bar-ODD")
    print("     sinh partner), not in F(q) over u.  Narrowing for the kernel hunt:")
    print("     drop the 'F bar-even in u' requirement; either work a bar-INVARIANT")
    print("     variable v (replacing u) or track Q_β's overall bar-ODD parity with")
    print("     b(q) bar-odd.  A constraint on R(q,ξ), not a value — within discipline.\n")

    w = WitnessBuilder("qbeta-barparity-kernel-criterion-prune", engine="python")
    w.set_description(
        "Prunes open-axis criterion 2(b) for the Q_β fibre kernel. b(q)="
        "(q-q⁻¹)/(q+q⁻¹) is bar-ODD, so u=b·ℏ_q² is bar-odd-covariant (u→-q²u). "
        "The documented c₂=-1 and both c₃ candidates (-2-ℏ², J_Hopf) all VIOLATE the "
        "bar-even-kernel law c_k(q⁻¹)=(-1)^k q^(-2k)c_k(q). So criterion 2(b) cannot "
        "be imposed on the c_k ladder in u; the bar-symmetry lives in the full Q_β "
        "(bar-odd sinh partner). Constraint/pruning, not a value-hunt; nothing wired.")
    w.add_data("b_bar_parity", parity(b))
    w.add_data("u_is_bar_odd_covariant_minus_q2", bool(u_covar))
    w.add_data("J_hopf_bar_parity", parity(J))
    w.add_data("bar_even_F_law", "c_k(q^-1) = (-1)^k q^(-2k) c_k(q)")
    w.add_data("candidates", results)
    w.add_data("any_candidate_satisfies", bool(any_pass))
    w.add_assertion("b_is_bar_odd", float(parity(b) == "odd"), 1.0,
                    source="(q-q⁻¹)/(q+q⁻¹): odd/even")
    w.add_assertion("no_documented_ck_satisfies_bar_even_law",
                    float(not any_pass), 1.0,
                    source="c₂=-1, c₃=-2-ℏ², c₃=J_Hopf all violate the law")
    w.add_caveat(
        "Pruning/constraint result for the gated fibre-kernel axis (qkhc) — NOT a "
        "real-q closed-form value-hunt (which is forbidden) and NOT a refuted "
        "mechanism. Sharpens/corrects open-axis criterion 2(b). The c_k vs the "
        "cos(α_eff)/Q_A factors of the full ladder may share bar-parity bookkeeping; "
        "this probe isolates the Π(1+c_k u^k) factor. Nothing wired.")
    path = w.save()
    print(f"  witness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
