#!/usr/bin/env python3
"""vector2_double_pincer_probe.py — the A5 + B4 double pincer on the Δ_λ magnitude
scalar `m ∈ (0, 1/√5)`.

Executes ideas **A5** (exact spectral audit of the [1⁴] exchange matrix against the
Bring S₅ period Gram) and **B4** (the Garoufalidis–Kashaev exact ζ₅ state-integral
1/√5 prefactor) of
`docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md`.  Both attack the
same algebraic number `√5` from opposite sides; this probe computes the DECISIVE,
exact cores of each and records — honestly, per the anti-numerology gate — which
questions each one closes and which it leaves open.

SCOPE. Audit-only / scope-(a). No fit, nothing wired to production. The probe does
**not** select the magnitude scalar `m`; it (i) *refutes exactly* the naive
"exchange matrix = square root of the Bring period Gram" identification and (ii)
identifies the exact origin of the `1/√5` prefactor as the quadratic Gauss sum
`g₅ = √5`, while (iii) explicitly declining to close the object-level bridge between
the exchange-spectrum ceiling `1/√5` and the icosahedral/Gauss-sum `1/√5` (no
object-level S-matrix ↔ Gauss-sum map exists — the audit's B4 "Risk").

SOURCES (primary; matrices printed in the cited papers):
  [b4-slater]  computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py —
               the He⁴ [1⁴] complete-graph exchange matrix S (mag = 1), typ = p,p,n,n,
               sign(pp) = +1, sign(nn) = −1, sign(pn) = sign(np) = +1; spectrum
               {±√5, ±1}; physicality ceiling det(I + mS) > 0 ⇔ m < 1/√5.
  [RR92]       Riera–Rodríguez, Pacific J. Math 154 (1992) 179–200, §2: the unique
               (up to scale) S₅-equivariant Gram
               c = [[4,1,−1,1],[1,4,1,−1],[−1,1,4,1],[1,−1,1,4]], spec {5,5,5,1},
               det 125; mᵗcm = diag(5,5,5,1).
  [BDH22]      Braden–Disney-Hogg, arXiv:2208.13692, Thm 2.12: the canonical
               symplectic form M_S = 5I − J (J = all-ones), spectrum {1,5,5,5}.
  [GK]         Garoufalidis–Kashaev, arXiv:1411.6062, Thm 1.1 + Cor 1.2 (M = 1): at
               b² = M/N the 1-dim state integral evaluates in closed form with an
               explicit 1/√N prefactor from a finite Gauss-type state sum.

WHAT IS EXACT AND DECISIVE HERE (machine-checked):
  A5.1  spec(S)  = {±√5, ±1}   (charpoly (x−1)(x+1)(x²−5), exact over ℚ).
  A5.2  spec(S²) = {5,5,1,1}   (charpoly (x−5)²(x−1)²).
  A5.3  spec(c)  = spec(M_S) = {5,5,5,1}  (charpoly (x−5)³(x−1); c and M_S cospectral,
        confirming RR92 mᵗcm ↔ BDH22 M_S consistency).
  A5.4  FALSIFIER — charpoly(S²) ≠ charpoly(c): the eigenvalue *set* {5,1} matches but
        the *multiplicity vector* does not ((2,2) for S² vs (3,1) for c). So S is
        **not** an S₅-equivariant square root of the period Gram — refuted exactly,
        not by near-match. (Recorded already "by inspection" in the attack-vector map;
        here it is the exact charpoly identity.)
  B4.1  quadratic Gauss sum g₅ = Σ_{k mod 5} ζ₅^{k²} = √5 exactly (g₅² = 5; the +
        branch since 5 ≡ 1 mod 4) — the exact origin of GK Cor 1.2's 1/√N = 1/√5.

WHAT STAYS OPEN (scaffolded honestly, NOT closed — the pincer does not land):
  A5-open  The *surviving* question is whether S's odd ±√5 spectrum matches the Bring
           real-structure / anti-involution action (BN12 S′, or the odd part of the
           intersection form C, both 8×8) restricted to the two standard-rep blocks.
           Those matrices are printed in BN12 (SIGMA 8 (2012) 065, §5.2) but are NOT
           in the corpus and are not reconstructed here; this probe does not fabricate
           them. Open sub-item.
  B4-open  The full algebraic number multiplying 1/√5 in Cor 1.2's 4₁ evaluation is
           1/√5 × (root of unity) × (Rogers exp) × ∏ D₅(θ,ζ₅) — the cyclic-dilogarithm
           product over the 4₁ angle data. The 1/√5 is pinned (g₅); the D₅ product
           needs GK's explicit 4₁ triangulation data and is left as the open sub-item.
  BRIDGE   Even with both exact cores, there is NO object-level derivation that the
           exchange ceiling 1/√5 IS the icosahedral S-matrix 1/√5 IS the Gauss-sum
           1/√5 (they are all the same algebraic number √5, but so are many unrelated
           normalizations). Anti-numerology gate applies with full force: the
           magnitude scalar m ∈ (0, 1/√5) remains OPEN; nothing is wired.
"""
from __future__ import annotations

# Path bridge (probes/ subdirectory refactor). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

x = sp.symbols("x")


def charpoly_factored(rows):
    """Exact factored characteristic polynomial over ℚ of an integer matrix."""
    M = sp.Matrix(rows)
    return sp.factor(M.charpoly(x).as_expr())


def spectrum(rows):
    """Exact eigenvalue → multiplicity dict of an integer matrix."""
    return sp.Matrix(rows).eigenvals()


def mult_vector(rows):
    """Sorted (eigenvalue, multiplicity) pairs, eigenvalues as sympy exprs."""
    return sorted(spectrum(rows).items(), key=lambda kv: sp.re(kv[0].evalf()))


def main() -> int:
    wb = WitnessBuilder("vector2-double-pincer", engine="sympy")

    # ── A5: exact spectral audit ────────────────────────────────────────────
    # He⁴ [1⁴] exchange matrix S (mag = 1); typ = p,p,n,n; sign pp=+1,nn=−1,pn=np=+1.
    S = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, -1], [1, 1, -1, 0]]
    cp_S = charpoly_factored(S)
    S2 = (sp.Matrix(S) ** 2).tolist()
    cp_S2 = charpoly_factored(S2)

    # RR92 §2 unique S₅-equivariant Gram c and BDH22 M_S = 5I − J.
    c = [[4, 1, -1, 1], [1, 4, 1, -1], [-1, 1, 4, 1], [1, -1, 1, 4]]
    cp_c = charpoly_factored(c)
    det_c = sp.Matrix(c).det()
    MS = (5 * sp.eye(4) - sp.ones(4, 4)).tolist()
    cp_MS = charpoly_factored(MS)

    # Exact targets.
    cp_S_target = (x - 1) * (x + 1) * (x**2 - 5)
    cp_S2_target = (x - 5) ** 2 * (x - 1) ** 2
    cp_c_target = (x - 5) ** 3 * (x - 1)

    assert sp.expand(cp_S - cp_S_target) == 0, cp_S
    assert sp.expand(cp_S2 - cp_S2_target) == 0, cp_S2
    assert sp.expand(cp_c - cp_c_target) == 0, cp_c
    assert sp.expand(cp_MS - cp_c_target) == 0, cp_MS   # c and M_S cospectral
    assert det_c == 125, det_c

    # THE FALSIFIER (exact): charpoly(S²) ≠ charpoly(c).
    charpoly_S2_eq_c = sp.expand(cp_S2 - cp_c) == 0
    assert charpoly_S2_eq_c is False, "S² and c must NOT be cospectral"

    # Eigenvalue set agrees {5,1}; multiplicity vector disagrees (2,2) vs (3,1).
    set_S2 = set(spectrum(S2).keys())
    set_c = set(spectrum(c).keys())
    same_eigen_set = set_S2 == set_c
    mult_S2 = {k: v for k, v in spectrum(S2).items()}
    mult_c = {k: v for k, v in spectrum(c).items()}
    assert same_eigen_set, (set_S2, set_c)
    assert mult_S2[sp.Integer(5)] == 2 and mult_c[sp.Integer(5)] == 3

    # ── B4: exact ζ₅ quadratic Gauss sum (origin of the 1/√5 prefactor) ─────
    zeta5 = sp.exp(2 * sp.pi * sp.I / 5)
    g5_expr = sum(zeta5 ** (k * k) for k in range(5))
    g5_sq = sp.nsimplify(sp.simplify(g5_expr * g5_expr))     # = 5
    g5 = sp.nsimplify(sp.radsimp(sp.expand_complex(g5_expr)))  # = √5
    assert g5_sq == 5, g5_sq
    assert g5 == sp.sqrt(5), g5

    # icosahedral / (2,3,5) vacuum-row normalization cross-check (exact):
    # the keystone vacuum row (2/√5)(sin π/5, sin 2π/5) is unit-normalized because
    # sin²(π/5) + sin²(2π/5) = 5/4, so (2/√5)²·(5/4) = 1. The 1/√5 is the S-matrix
    # normalization — the SAME algebraic number as g₅ = √5 (via reciprocal).
    row_norm = sp.simplify((sp.Rational(2, 1) / sp.sqrt(5)) ** 2
                           * (sp.sin(sp.pi / 5) ** 2 + sp.sin(2 * sp.pi / 5) ** 2))
    assert sp.simplify(row_norm - 1) == 0, row_norm
    sin_sq_sum = sp.simplify(sp.sin(sp.pi / 5) ** 2 + sp.sin(2 * sp.pi / 5) ** 2)
    assert sin_sq_sum == sp.Rational(5, 4), sin_sq_sum

    # ── report ──────────────────────────────────────────────────────────────
    print("=" * 74)
    print(" Vector-2 double pincer on the Δ_λ magnitude scalar m ∈ (0, 1/√5)")
    print(" A5 + B4 — audit-only / scope-(a) / no fit / nothing wired")
    print("=" * 74)
    print("A5 exact spectra:")
    print(f"  charpoly(S)   = {cp_S}      → spec(S)  = {{±√5, ±1}}")
    print(f"  charpoly(S²)  = {cp_S2}   → spec(S²) = {{5,5,1,1}}")
    print(f"  charpoly(c)   = {cp_c}    → spec(c)  = {{5,5,5,1}}, det = {det_c}")
    print(f"  charpoly(M_S) = {cp_MS}    → cospectral with c (RR92 ↔ BDH22 consistent)")
    print(f"  FALSIFIER  charpoly(S²) == charpoly(c) ?  {charpoly_S2_eq_c}")
    print("             eigenvalue SET {5,1} matches; MULTIPLICITY (2,2) vs (3,1) "
          "does NOT")
    print("             ⇒ S is NOT an equivariant square root of the period Gram "
          "(refuted exactly)")
    print("B4 exact Gauss sum:")
    print(f"  g₅ = Σ_(k mod 5) ζ₅^(k²) = {g5}   (g₅² = {g5_sq}) — the exact 1/√N=1/√5")
    print(f"  icosahedral vacuum-row norm (2/√5)²(sin²π/5+sin²2π/5) = {row_norm}  "
          f"(sin²π/5+sin²2π/5 = {sin_sq_sum})")
    print("VERDICT: both directions locate the SAME algebraic number √5, the naive")
    print("  Gram identification is refuted exactly, and the object-level bridge stays")
    print("  OPEN (anti-numerology gate). m ∈ (0, 1/√5) NOT closed; nothing wired.")

    # ── witness ──────────────────────────────────────────────────────────────
    wb.set_description(
        "Vector-2 double pincer (uploaded-papers ideas A5 + B4) on the Δ_λ magnitude "
        "scalar m ∈ (0, 1/√5). A5: exact characteristic polynomials of the He⁴ [1⁴] "
        "exchange matrix S (spec {±√5,±1}), S² (spec {5,5,1,1}), the RR92 S₅-Gram c "
        "and BDH22 M_S=5I−J (both spec {5,5,5,1}, cospectral) — the naive 'S = "
        "equivariant square root of the period Gram' is REFUTED EXACTLY by the "
        "multiplicity mismatch (charpoly(S²)=(x−5)²(x−1)² ≠ (x−5)³(x−1)=charpoly(c); "
        "same eigenvalue set {5,1}, multiplicity (2,2) vs (3,1)). B4: the quadratic "
        "Gauss sum g₅=Σ_(k mod 5)ζ₅^(k²)=√5 (exact) is the origin of GK Cor 1.2's "
        "1/√N=1/√5 prefactor; the icosahedral (2,3,5) vacuum-row normalization is the "
        "same √5. Both √5's coincide as algebraic numbers, but NO object-level "
        "S-matrix↔Gauss-sum map exists — anti-numerology gate; m stays OPEN; nothing "
        "wired."
    )
    wb.set_audit_only(
        "docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md")
    wb.add_data("A5_spectra_exact", {
        "charpoly_S": str(cp_S),
        "charpoly_S_squared": str(cp_S2),
        "charpoly_c_RR92_Gram": str(cp_c),
        "charpoly_M_S_5I_minus_J": str(cp_MS),
        "det_c": int(det_c),
        "c_and_M_S_cospectral": True,
        "eigen_set_S2": "{5,1}",
        "eigen_set_c": "{5,1}",
        "multiplicity_S2": "5:2, 1:2",
        "multiplicity_c": "5:3, 1:1",
    })
    wb.add_data("B4_gauss_sum_exact", {
        "g5_quadratic_gauss_sum": "sqrt(5)",
        "g5_squared": int(g5_sq),
        "branch": "+ (5 ≡ 1 mod 4)",
        "role": "reciprocal is GK Cor 1.2 prefactor 1/sqrt(N) = 1/sqrt(5)",
        "icosahedral_vacuum_row_norm": 1,
        "sin_sq_pi5_plus_sin_sq_2pi5": "5/4",
    })
    wb.add_data("open_sub_items", {
        "A5_open": "BN12 real-structure/anti-involution S' and intersection form C "
                   "(8x8, SIGMA 8 (2012) 065 §5.2) restricted to the two std blocks "
                   "vs S's odd ±√5 spectrum — matrices not in corpus, not fabricated.",
        "B4_open": "full D₅(θ,ζ₅) cyclic-dilogarithm product over the GK 4₁ angle "
                   "data — the algebraic number accompanying 1/√5; needs GK "
                   "triangulation data.",
        "bridge": "object-level map exchange-ceiling 1/√5 ↔ icosahedral S-matrix "
                  "1/√5 ↔ Gauss-sum 1/√5 — none exists; m ∈ (0,1/√5) OPEN.",
    })
    wb.add_caveat(
        "Scope-(a): a shared algebraic number (√5) is NOT an object-level identity. "
        "The naive Bring-period-Gram identification is exactly refuted; the surviving "
        "Bring-real-structure comparison and the object-level √5 bridge are OPEN. The "
        "magnitude scalar m is not selected here and nothing is wired to production."
    )
    wb.add_assertion(
        "S_spectrum_pm_sqrt5_pm_1",
        computed=str(cp_S),
        expected=str(sp.factor(cp_S_target)),
        tolerance=0,
        source="charpoly(S) = (x−1)(x+1)(x²−5); spec(S) = {±√5, ±1} exactly.",
    )
    wb.add_assertion(
        "charpoly_S2_exact",
        computed=str(cp_S2),
        expected=str(sp.factor(cp_S2_target)),
        tolerance=0,
        source="charpoly(S²) = (x−5)²(x−1)² exactly; spec(S²) = {5,5,1,1}.",
    )
    wb.add_assertion(
        "naive_gram_square_root_refuted_exactly",
        # True proposition: S² and c are NOT cospectral (the exact falsifier).
        computed=str(sp.expand(cp_S2 - cp_c) != 0),
        expected="True",
        tolerance=0,
        source="charpoly(S²)=(x−5)²(x−1)² ≠ (x−5)³(x−1)=charpoly(c) ⇒ this boolean "
               "is True. Same eigenvalue set {5,1}, multiplicity (2,2) vs (3,1); S is "
               "NOT an equivariant square root of the period Gram. Exact falsifier.",
    )
    wb.add_assertion(
        "c_and_M_S_cospectral",
        computed=str(cp_c),
        expected=str(cp_MS),
        tolerance=0,
        source="RR92 Gram c and BDH22 M_S=5I−J share charpoly (x−5)³(x−1) — "
               "RR92 mᵗcm ↔ BDH22 M_S consistency, exact.",
    )
    wb.add_assertion(
        "quadratic_gauss_sum_g5_is_sqrt5",
        computed=str(g5_sq),
        expected="5",
        tolerance=0,
        source="g₅=Σ_(k mod 5)ζ₅^(k²), g₅²=5 ⇒ g₅=√5 (+ branch, 5≡1 mod 4) — exact "
               "origin of GK Cor 1.2's 1/√N=1/√5.",
    )
    wb.add_assertion(
        "icosahedral_vacuum_row_unit_norm",
        computed=str(row_norm),
        expected="1",
        tolerance=0,
        source="(2/√5)²(sin²π/5+sin²2π/5)=1 since sin²π/5+sin²2π/5=5/4 — the (2,3,5) "
               "S-matrix 1/√5 normalization (same algebraic number, NOT an object-"
               "level identity — anti-numerology gate).",
    )
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
