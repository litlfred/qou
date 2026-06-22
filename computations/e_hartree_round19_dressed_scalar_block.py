#!/usr/bin/env python3
# polynomial_q_not_applicable: all characters are EXACT Laurent polynomials /
# rational functions in q (sympy); float64 appears ONLY as a cross-check of the
# exact hook formula against the existing seminormal builder at q_0.
"""
conj:e-hartree-categorical-derivation — ROUND 19 (owner-directed).

Resolves the two outstanding computational steps left open by rounds 17-18 of
the conjecture block (content/quantum-observable-universe/predicted-spectra/
e-hartree-categorical-derivation.md):

  (R18 outstanding) "the exact algebraic relation between chi_{(3,1)},
  chi_{(2,1,1)} at q_0 and the force-carrier delta_q values needs to be made
  explicit (probably via the Murphy basis / characters-as-q-rationals)."

  (R17 refinement 1) "Compute the DRESSED Wedderburn projection.  Replace
  sigma_2 in the molecular braid with the dressed form (eigenvalues
  q^5, -q^{-5}).  If the dressed (2,2) component is nonzero, the hypothesis
  survives in revised form."

RESULT 1 — bare characters are CLASSICAL (hook-support theorem), exact:
  For the Coxeter word c = sigma_1 sigma_2 sigma_3 in H_4(q) (7a convention,
  eigenvalues q, -q^{-1}),
      chi_lambda(c) = 0 unless lambda is a hook (a, 1^{4-a}), and
      chi_{(a,1^{n-a})}(c) = (-1)^{n-a} q^{2a-n-1}:
      (4): q^3,  (3,1): -q,  (2,2): 0,  (2,1,1): q^{-1},  (1^4): -q^{-3}.
  These reproduce round-17's numerical table EXACTLY (q_0^3 = 1.368,
  -q_0 = -1.110, 0.901 = q_0^{-1}, -0.731 = -q_0^{-3}) — the round-17/18
  "intertwining support" IS the classical Hecke-Coxeter hook-support theorem
  (q-Murnaghan-Nakayama; Ref: [ram1991] below), now exact for all q, not a
  q_0 numerical observation.  Consequence for R18: the bare-character product
  chi_{(3,1)} * chi_{(2,1,1)} = -1 EXACTLY (q-independent unit) — the bare
  characters carry the carriers' CHANNEL SUPPORT but NOT the delta_q
  magnitudes (h[9]_q, h[10]_q).  The R18 hoped-for magnitude identification
  is REFUTED at the bare level; the magnitude must enter through dressing /
  the q-dim decoration layer (consistent with rounds 11 and 13).

RESULT 2 — the dressed scalar block ACTIVATES, exact closed form:
  Dressing sigma_2 with eigenvalues (q^m, -q^{-m}) is affine in sigma_2:
      sigma_2^{(m)} = A_m + B_m sigma_2,
      B_m = (q^m + q^{-m})/(q + q^{-1}),   A_m = h [m-1]_q / [2]_q,
  so by linearity of characters,
      chi_lambda(sigma_1 sigma_2^{(m)} sigma_3)
          = A_m chi_lambda(sigma_1 sigma_3) + B_m chi_lambda(c).
  With the exact restriction values (Littlewood-Richardson to H_2 x H_2):
      chi_{(4)}(s1 s3) = q^2, chi_{(3,1)} = q^2 - 2, chi_{(2,2)} = q^2 + q^{-2},
      chi_{(2,1,1)} = q^{-2} - 2, chi_{(1^4)} = q^{-2}
  (q -> 1 recovers the S_4 character column of (12)(34): 1, -1, 2, -1, 1),
  the scalar block gets
      chi_{(2,2)}(sigma_1 sigma_2^{(m)} sigma_3) = h [m-1]_q [4]_q / [2]_q^2 ,
  which is NONZERO for every m >= 2 — answering R17 refinement 1 POSITIVELY —
  and at the K-shell dressing power m = 5 (= 2k+1, k = 2) specialises to
      chi_{(2,2)} = h ([4]_q/[2]_q)^2 = h (q^2 + q^{-2})^2
                  = h * (dim_q V_{(2,2)})^2 ,
  i.e. h times the PLANCHEREL SQUARE of the scalar block's q-dimension —
  a q-dimension-layer quantity surfacing in the Markov layer exactly at the
  K-shell power (m - 1 = 4 = n).  Tier: derived identity (exact); its
  physical reading (scalar-block activation under atomic dressing) stays
  conditional on the gate conjecture.

WHAT THIS DOES NOT CLOSE (honest): the alpha_EM^2 MAGNITUDE chain
  (h^4/(q^2 delta_q(T_{2,9})^2 delta_q(T_{3,5})^2)) is NOT produced — the
  dressed scalar character carries h^1 x q-dim^2, not h^4/delta^2 delta^2.
  The conjecture remains OPEN; rounds 17-18's two named computational gaps
  are now closed exactly, and the remaining gap is localised to the
  archimedean trace-ratio on the activated scalar block (plus the two
  standing transports: the m_e c^2 unit and the LP-kink smoothness).

Refs: conj:e-hartree-categorical-derivation (rounds 11-18);
prop:force-carrier-intertwining-correspondence; thm:em-spectral-completeness;
prop:torus-knot-delta-q-writhe.  Classical hook-support / q-Murnaghan-
Nakayama: A. Ram, "A Frobenius formula for the characters of the Hecke
algebras", Invent. Math. 106 (1991) 461-488.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

import sympy as sp

try:
    import mpmath as mp
    mp.mp.dps = 70
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099785955573347198997632204832250266562084087802"

# exact bare characters at n = 4 (7a convention), derived in the docstring
q = sp.symbols("q", positive=True)
h = q - 1 / q
HOOK_COXETER = {                      # chi_lambda(sigma_1 sigma_2 sigma_3)
    (4,): q ** 3, (3, 1): -q, (2, 2): sp.Integer(0),
    (2, 1, 1): 1 / q, (1, 1, 1, 1): -q ** -3,
}
S1S3 = {                              # chi_lambda(sigma_1 sigma_3), LR to H2xH2
    (4,): q ** 2, (3, 1): q ** 2 - 2, (2, 2): q ** 2 + q ** -2,
    (2, 1, 1): q ** -2 - 2, (1, 1, 1, 1): q ** -2,
}
S4_CLASS_2_2 = {(4,): 1, (3, 1): -1, (2, 2): 2, (2, 1, 1): -1,
                (1, 1, 1, 1): 1}      # S_4 character column of (12)(34)


def qint(k, q_sym=q, h_sym=h):
    return (q_sym ** k - q_sym ** (-k)) / h_sym


def main() -> None:
    w = WitnessBuilder("e-hartree-round19-dressed-scalar-block", engine="python")
    q0 = mp.mpf(Q0) if HAVE_MP else float(Q0)

    # R1a: q -> 1 limit of S1S3 equals the S_4 character column of (12)(34)
    limit_ok = all(sp.limit(expr, q, 1) == S4_CLASS_2_2[lam]
                   for lam, expr in S1S3.items())

    # R1b: float64 cross-check of BOTH exact tables against the existing
    # seminormal builder at q_0 (cross-method agreement; exact values are
    # what the witness carries).
    cross_ok, cross_err = True, 0.0
    try:
        sys.path.insert(0, str(_HERE / "hecke"))
        from hecke_characters import build_seminormal_matrices
        import numpy as np
        for lam in HOOK_COXETER:
            sig, _dim, _ = build_seminormal_matrices(lam, sparse=False,
                                                     q=float(q0))
            if not sig:
                continue
            m_cox = sig[0] @ sig[1] @ sig[2]
            m_s13 = sig[0] @ sig[2]
            for table, mat in ((HOOK_COXETER, m_cox), (S1S3, m_s13)):
                exact = float(sp.N(table[lam].subs(q, sp.Float(str(q0), 30))))
                err = abs(float(np.trace(mat)) - exact)
                cross_err = max(cross_err, err)
                cross_ok = cross_ok and err < 1e-9
    except Exception as exc:  # builder unavailable: keep exact layer, say so
        cross_ok, cross_err = None, str(exc)

    # R1c: the bare-product is the q-independent unit -1
    bare_prod = sp.simplify(HOOK_COXETER[(3, 1)] * HOOK_COXETER[(2, 1, 1)])
    bare_prod_ok = bare_prod == -1

    # R2: dressed scalar block, exact closed form
    m = sp.symbols("m", positive=True, integer=True)
    B_m = (q ** m + q ** (-m)) / (q + 1 / q)
    A_m = sp.simplify(q ** m - B_m * q)
    A_closed = sp.simplify(h * qint(m - 1) / (q + 1 / q))  # h [m-1]_q / [2]_q
    A_ok = sp.simplify(A_m - A_closed) == 0
    # eigenvalue sanity: A_m + B_m*q = q^m, A_m - B_m/q = -q^{-m}
    eig_ok = (sp.simplify(A_m + B_m * q - q ** m) == 0 and
              sp.simplify(A_m - B_m / q + q ** (-m)) == 0)

    chi22_dressed = sp.simplify(A_m * S1S3[(2, 2)])  # B_m * 0 drops
    closed = sp.simplify(h * qint(m - 1) * qint(4) / qint(2) ** 2)
    chi22_ok = sp.simplify(chi22_dressed - closed) == 0
    chi22_m5 = sp.simplify(chi22_dressed.subs(m, 5))
    plancherel = sp.simplify(h * (q ** 2 + q ** -2) ** 2)
    m5_ok = sp.simplify(chi22_m5 - plancherel) == 0
    nonzero_ms = all(sp.simplify(chi22_dressed.subs(m, k)) != 0
                     for k in (2, 3, 5, 7, 9))

    val_m5 = (mp.mpf(str(sp.N(chi22_m5.subs(q, sp.Float(str(q0), 60)), 50)))
              if HAVE_MP else float(sp.N(chi22_m5.subs(q, sp.Float(str(q0), 30)))))

    print("=" * 74)
    print("conj:e-hartree ROUND 19 — dressed scalar block (exact)")
    print("=" * 74)
    print(f"  R1 bare Coxeter = hook formula; (2,2) = 0; round-17 table exact")
    print(f"     q->1 S_4 check (sigma_1 sigma_3): {limit_ok}")
    print(f"     float64 cross-check vs seminormal builder: {cross_ok}"
          f" (max err {cross_err})")
    print(f"     bare product chi_(3,1) chi_(2,1,1) = -1 (unit): {bare_prod_ok}")
    print(f"  R2 dressing sigma_2 -> (q^m, -q^-m): A_m = h[m-1]/[2]: {A_ok}, "
          f"eigs: {eig_ok}")
    print(f"     chi_(2,2)(dressed) = h [m-1][4]/[2]^2: {chi22_ok}; "
          f"nonzero for m>=2: {nonzero_ms}")
    print(f"     K-shell m=5: chi_(2,2) = h([4]/[2])^2 = h(dim_q V_22)^2: {m5_ok}")
    print(f"     value at q0: {mp.nstr(val_m5, 12) if HAVE_MP else val_m5}")
    print()
    print("  Verdict: R17 refinement 1 answered POSITIVELY (scalar block")
    print("  activates under dressing); R18 magnitude identification REFUTED")
    print("  at bare level (product = -1). Conjecture remains OPEN; gap now")
    print("  localised to the archimedean trace-ratio on the activated block.")

    w.set_description(
        "conj:e-hartree-categorical-derivation round 19: closes the two "
        "outstanding computational steps of rounds 17-18, exactly.  (R1) The "
        "bare molecular-braid characters are the classical Hecke-Coxeter "
        "hook-support values chi_{(a,1^{4-a})}(c) = (-1)^{4-a} q^{2a-5} — "
        "round-17's numerical table is exact for all q and the (2,2) zero is "
        "the hook-support theorem (Ram 1991 q-Murnaghan-Nakayama); the bare "
        "product chi_{(3,1)} chi_{(2,1,1)} = -1 exactly, so the R18 hoped-for "
        "delta_q-magnitude identification is refuted at the bare level (the "
        "bare characters carry channel SUPPORT only).  (R2) Dressing sigma_2 "
        "with eigenvalues (q^m, -q^{-m}) is affine (A_m = h[m-1]_q/[2]_q, "
        "B_m = (q^m+q^{-m})/[2]_q-normalised), so by character linearity the "
        "scalar block ACTIVATES: chi_{(2,2)}(dressed) = h[m-1]_q[4]_q/[2]_q^2 "
        "(nonzero for all m >= 2), and at the K-shell power m = 5 equals "
        "h([4]_q/[2]_q)^2 = h (dim_q V_{(2,2)})^2 — the Plancherel square of "
        "the scalar block's q-dimension, a q-dim-layer quantity surfacing in "
        "the Markov layer exactly at m-1 = n = 4.  Restriction values "
        "chi(sigma_1 sigma_3) derived by Littlewood-Richardson to H_2 x H_2 "
        "(q -> 1 recovers the S_4 (12)(34) column).  The alpha_EM^2 magnitude "
        "chain is NOT produced (h^1 x dim_q^2, not h^4/delta^2 delta^2): the "
        "conjecture remains OPEN with the gap localised to the archimedean "
        "trace-ratio on the activated scalar block."
    )
    w.set_content_block("conj:e-hartree-categorical-derivation")
    w.add_data("q0", str(q0))
    w.add_data("bare_coxeter_exact", {str(k): str(v)
                                      for k, v in HOOK_COXETER.items()})
    w.add_data("sigma1_sigma3_exact", {str(k): str(v) for k, v in S1S3.items()})
    w.add_data("dressed_chi22_closed_form", "h*[m-1]_q*[4]_q/[2]_q^2")
    w.add_data("dressed_chi22_K_shell_m5", str(chi22_m5))
    w.add_data("dressed_chi22_K_shell_value_at_q0", str(val_m5))
    w.add_assertion(
        "q->1 limit of chi(sigma_1 sigma_3) table = S_4 character column (12)(34)",
        computed=bool(limit_ok), expected=True,
        source="Littlewood-Richardson restriction to H_2 x H_2",
    )
    w.add_assertion(
        "float64 cross-check of exact tables vs seminormal builder at q_0",
        computed=bool(cross_ok) if cross_ok is not None else False,
        expected=True,
        source=f"hecke_characters.build_seminormal_matrices; max err {cross_err}",
    )
    w.add_assertion(
        "bare product chi_(3,1)*chi_(2,1,1) = -1 exactly (R18 magnitude refuted)",
        computed=bool(bare_prod_ok), expected=True,
        source="hook formula; q-independent unit",
    )
    w.add_assertion(
        "dressing is affine: A_m = h[m-1]_q/[2]_q with correct eigenvalues",
        computed=bool(A_ok and eig_ok), expected=True,
        source="Bezout split of the dressed generator",
    )
    w.add_assertion(
        "chi_(2,2)(dressed) = h[m-1]_q[4]_q/[2]_q^2, nonzero for m >= 2 (R17 ref-1)",
        computed=bool(chi22_ok and nonzero_ms), expected=True,
        source="character linearity + LR restriction",
    )
    w.add_assertion(
        "K-shell m=5 specialisation: chi_(2,2) = h*(dim_q V_(2,2))^2",
        computed=bool(m5_ok), expected=True,
        source="[4]_q/[2]_q = q^2+q^{-2} = dim_q V_(2,2); m-1 = n = 4",
    )
    w.add_data(
        "finding",
        "Round 19 closes rounds 17-18's two open computations exactly: bare "
        "support = classical hook theorem (round-17 table exact; (2,2) zero "
        "structural); dressed scalar block activates with closed form "
        "h[m-1][4]/[2]^2, equal to h*(dim_q V_22)^2 at the K-shell power. "
        "Conjecture stays OPEN: remaining gap = archimedean trace-ratio on "
        "the activated block + the two standing transports (m_e c^2 unit; "
        "LP-kink smoothness)."
    )
    w.save()
    print("\nDone. Witness saved (e-hartree-round19-dressed-scalar-block).")


if __name__ == "__main__":
    main()
