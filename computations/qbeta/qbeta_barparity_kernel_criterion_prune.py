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

This probe PRUNES that criterion symbolically (the sanctioned "narrow before you
scan" step 3 of the open-axis doc — a constraint on R, NOT a real-q closed-form
value-hunt, which is the gated/forbidden activity).

CORRECTION (2026-06-20, docs/audits/2026-06-20-hoefsmit-b-bar-parity-correction.md):
an earlier version used b = (q-q⁻¹)/(q+q⁻¹), which is bar-ODD and gives the WRONG
substrate value u ≈ 0.00102 (off by ~8× from the documented u ≈ 0.00852). The
canonical Hoefsmit base — the one matching u ≈ 0.00852, the mainstream c_k probes,
and SilverAnchorGrounding.lean (b² = (q⁴+q²+1)/(q²+1)²) — is

    b(q) = √( (h²+3)/(h²+4) ) = √(q⁴+q²+1)/(q²+1),   h = q − q⁻¹,

which is BAR-EVEN (b(q⁻¹)=b(q); verified in Lean QOU.QBeta.hoefsmitBSq_bar_even).
Hence:

Substrate forms:
    b(q) = √((h²+3)/(h²+4))            Hoefsmit base, BAR-EVEN
    ℏ_q² = (1 - q⁻¹)²                  bar-covariant (↦ q²ℏ_q²)
    u    = b · ℏ_q²                    the c_k expansion variable
    J_Hopf(q) = -(q² + q⁻²)            Jones poly of the Hopf link, J_Hopf(1)=-2

Bar-parity bookkeeping (q↦q⁻¹):
    b(q) is bar-EVEN (b(q⁻¹) = b(q), since b² is a function of h² and h is bar-odd)
    ℏ_q² ↦ q²ℏ_q²    (bar-covariant)
    ⇒ u ↦ +q²·u      (bar-EVEN-covariant — NO sign; QOU.QBeta.uSq_bar_covariance)
A bar-EVEN F(q)=Σ c_k u^k then forces, term by term,
    c_k(q⁻¹) = q^{-2k} c_k(q)          (NO (-1)^k — u has no per-rung sign).
This probe tests whether the documented c_k satisfy it.

VERDICT is UNCHANGED by the correction: criterion 2(b) still cannot be imposed
(c₂=-1 gives residual q^{-4}-1 ≠ 0 under the corrected law too). What changes is
the MECHANISM: there is no "parity-split ladder" — u is uniformly bar-even-
covariant, so the prune of criterion 2b follows from the c_k values failing the
(unsigned) law, not from any bar-oddness of u.

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
    h = q - 1 / q
    b = sp.sqrt((h ** 2 + 3) / (h ** 2 + 4))   # canonical Hoefsmit base (bar-EVEN)
    h2 = (1 - 1 / q) ** 2
    u = b * h2
    J = -(q ** 2 + 1 / q ** 2)

    # Check b's parity via b² (avoids sqrt-branch ambiguity in sp.simplify):
    bsq_parity = parity(b ** 2)

    print("\n  Q_β CRITERION-2(b) PRUNE — can the fibre kernel be bar-even in u?\n")
    print("  | quantity | bar-parity | note |")
    print("  |---|---|---|")
    print(f"  | b(q)=√((h²+3)/(h²+4)) | {bsq_parity.upper()} (via b²) | h=q-q⁻¹ bar-odd ⇒ b² bar-even |")
    print(f"  | ℏ_q² | covariant (×q²) | (1-q⁻¹)² type |")
    u_covar_plus = sp.simplify(bar(u) - (q ** 2 * u)) == 0
    print(f"  | u=b·ℏ_q² | EVEN-covariant (→ +q²u): {u_covar_plus} | b even × ℏ² covariant |")
    print(f"  | J_Hopf=-(q²+q⁻²) | {parity(J).upper()} | classical Jones, J(1)=-2 |\n")

    # bar-even-F covariance law (CORRECTED, no (-1)^k): c_k(1/q) = q^(-2k) c_k(q)
    candidates = [(2, sp.Integer(-1), "c2 = -1 (proved-exact)"),
                  (3, -2 - h2, "c3 = -2 - ℏ_q² (near-match)"),
                  (3, J, "c3 = J_Hopf(q) (near-match)")]
    print("  bar-even-F law  c_k(q⁻¹) = q^(-2k) c_k(q):")
    print("  | k | candidate | residual | satisfies? |")
    print("  |---|---|---|---|")
    results = {}
    any_pass = False
    for k, ck, lab in candidates:
        resid = sp.simplify(bar(ck) - q ** (-2 * k) * ck)
        ok = resid == 0
        any_pass = any_pass or ok
        results[lab] = {"k": k, "residual": str(resid), "satisfies": bool(ok)}
        print(f"  | {k} | {lab} | {resid} | {ok} |")

    print("\n  ---------------------------------------------------------------")
    print("  VERDICT (criterion-2b prune, no fit)")
    print("   * b(q) is bar-EVEN ⇒ u = b·ℏ_q² is bar-EVEN-covariant (u → +q²u).")
    print("   * The documented c₂=-1 (proved-exact) and BOTH c₃ candidates (-2-ℏ²,")
    print("     J_Hopf(q)) all VIOLATE the bar-even-F law c_k(q⁻¹)=q^(-2k)c_k(q).")
    print("   => Open-axis criterion 2(b) ('F(q) bar-even') CANNOT be imposed on the")
    print("      c_k ladder in the variable u: the documented c_k do not satisfy the")
    print("      (unsigned) covariance a bar-even kernel needs in u.  The criterion's")
    print("      justification ('c₂=-1 is bar-even') conflates bar-INVARIANCE of the")
    print("      constant with the covariance law a bar-even F needs in u.")
    print("   * NOTE (correction): there is NO 'parity-split ladder' — u carries no")
    print("     per-rung sign (b is bar-even, not bar-odd).  The prune stands on the")
    print("     c_k values failing the law, independent of any bar-oddness of u.\n")

    w = WitnessBuilder("qbeta-barparity-kernel-criterion-prune", engine="python")
    w.set_description(
        "Prunes open-axis criterion 2(b) for the Q_β fibre kernel. The canonical "
        "Hoefsmit base b(q)=√((h²+3)/(h²+4)) (h=q-q⁻¹) is bar-EVEN, so u=b·ℏ_q² is "
        "bar-EVEN-covariant (u→+q²u). The documented c₂=-1 and both c₃ candidates "
        "(-2-ℏ², J_Hopf) all VIOLATE the bar-even-kernel law c_k(q⁻¹)=q^(-2k)c_k(q). "
        "So criterion 2(b) cannot be imposed on the c_k ladder in u. CORRECTION of an "
        "earlier version that used a non-canonical bar-ODD b=(q-q⁻¹)/(q+q⁻¹) (wrong "
        "u≈0.00102): the verdict is unchanged but there is no parity-split (u carries "
        "no per-rung sign). Constraint/pruning, not a value-hunt; nothing wired. See "
        "docs/audits/2026-06-20-hoefsmit-b-bar-parity-correction.md.")
    w.add_data("b_bar_parity", bsq_parity)
    w.add_data("u_is_bar_even_covariant_plus_q2", bool(u_covar_plus))
    w.add_data("J_hopf_bar_parity", parity(J))
    w.add_data("bar_even_F_law", "c_k(q^-1) = q^(-2k) c_k(q)")
    w.add_data("candidates", results)
    w.add_data("any_candidate_satisfies", bool(any_pass))
    w.add_assertion("b_is_bar_even", float(bsq_parity == "even"), 1.0,
                    source="b²=(q⁴+q²+1)/(q²+1)²: function of h² (h bar-odd) ⇒ bar-even")
    w.add_assertion("no_documented_ck_satisfies_bar_even_law",
                    float(not any_pass), 1.0,
                    source="c₂=-1, c₃=-2-ℏ², c₃=J_Hopf all violate the (unsigned) law")
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
