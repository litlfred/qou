#!/usr/bin/env python3
"""vector2_a5_sprime_residue_probe.py — the A5 residue of the Vector-2 double
pincer: the BN12 anti-involution S′ spectrum vs the [1⁴] exchange spectrum.

Closes the **A5 open sub-item** of
`docs/audits/2026-07-18-vector2-double-pincer-a5-b4.md` ("BN12 real-structure /
anti-involution S′ and intersection form C (8×8, SIGMA 8 (2012) 065) restricted
to the two std blocks vs S's odd ±√5 spectrum — matrices not in corpus"). The
matrices ARE now in scope: they were transcribed from the paper's rendered PDF
pages (library/sigma12-065/sigma12-065.pdf, pp. 8, 13, 14) and every claimed property is
machine-verified exactly BEFORE use (anti-guessing rule):

  V1  C  (p.13)  is antisymmetric with det C = 1 (unimodular intersection form
      of the α₁..α₈ homology basis; "precisely the matrix claimed by Riera and
      Rodríguez").
  V2  S′ (p.14)  has integer entries and S′² = I.
  V3  S′ is ANTI-symplectic w.r.t. the intersection form: S′ C S′ᵀ = −C
      (row-vector convention; an antiholomorphic involution reverses
      orientation, hence negates the intersection pairing).
  V4  B := (4.2) (p.8) canonicalises the intersection form: Bᵀ C B = J with
      J = [[0,I],[−I,0]] the canonical symplectic form.
  V5  T  (p.14)  is symplectic w.r.t. J:  Tᵀ J T = J,  det T = 1.
  V6  (T·Bᵀ) S′ (T·Bᵀ)⁻¹ = S = [[I,I],[0,−I]] — BN12's printed canonical form
      for an antiholomorphic involution with one nondividing real oval (their
      "S := TS′T⁻¹" is stated after the (4.2) basis change; the composition
      U = T·Bᵀ reproduces it exactly from the α-basis S′).
  V7  The order-5 rotation A (from the paper's stated basis structure
      α_{2k+1} = R^k α₁, α_{2k+2} = R^k α₂ and H₁^R = 0, so 1+R+…+R⁴ = 0):
      A⁵ = I, charpoly(A) = Φ₅(x)², A C Aᵀ = C (row convention), and the
      dihedral relation S′ A S′ = A⁻¹ — so {A^k S′} is the natural 5-member
      family of anti-involutions (each squares to I).

THE SURVIVING A5 QUESTION (decided here, exactly, over ℚ):
does any natural involution-twisted form on H₁(Bring) reproduce the He⁴ [1⁴]
exchange spectrum {±√5, ±1} (charpoly (x−1)(x+1)(x²−5))?  Comparison set:

  1. the 8×8 twisted intersection form  S′C  (symmetric since S′ is
     C-anti-symplectic); its charpoly is IRREDUCIBLE of degree 8 over ℚ —
     x⁸+x⁷−22x⁶−9x⁵+38x⁴+4x³−16x²+x+1 — so it has NO rational or quadratic
     eigenvalue at all (no ±1, no ±√5).
  2. the full 5-member family C·A^k·S′ (k = 0..4): none of the five exact
     charpolys is divisible by (x²−5).
  3. the two A-stable, S′-stable 4-dim blocks of H₁⊗ℚ (odd/even index —
     H₁⊗ℚ = 2 · (4-dim ℚ(ζ₅)-line), the ℚ-forms of the two 4-dim
     standard-representation blocks): the block-restricted twisted forms have
     charpolys (x²−2x−1)(x²+2x−1)  → eigenvalues ±(1+√2), ±(√2−1), the SILVER
     ratio units, field ℚ(√2);  and (x+1)(x³−3x+1) → eigenvalues −1 and
     2cos(2πk/9), field ℚ(ζ₉)⁺.  Wrong number fields entirely.
  4. the S′-eigenspace (fixed / anti-fixed) restrictions of the twisted form:
     x²(x−2)(x+3) and x²(x−1)(x+2) — rank-2 degenerate, integer spectra
     {0,0,2,−3} / {0,0,1,−2}, no match.
  5. basis-independent falsifier: eigenvalues of a bilinear form are only
     congruence-covariant, and ℚ-congruence preserves det mod squares.
     det(S′C) = 1 vs det(S_exchange) = 5 — DISTINCT square classes, so NO
     basis presentation of the Bring twisted form can ever be congruent to
     the exchange form. (Signatures agree — both 0 — so the discriminant
     class is the discriminating invariant.)

RECORDED-NOT-INTERPRETED coincidence: in the canonical frame the universal
twisted form J·S (S the canonical one-oval normal form) has charpoly
(x²+x−1)⁴ — the GOLDEN-ratio units (−1±√5)/2, each ×4. This is where a √5
does live on the real-structure side; but (i) it is universal for ANY genus-4
curve with a one-nondividing-oval real structure (depends only on the
topological type, not on Bring), (ii) the multiset {φ−1-type units} ≠
{±√5, ±1}, and (iii) it is congruent to S′C (det 1 class), hence equally
non-congruent to the exchange form.

VERDICT (scope-(a)): the natural involution-twisted forms, alone, do not
reproduce the exchange spectrum {±√5, ±1} — in any of the five natural
presentations, and provably in NO presentation (discriminant square-class
obstruction). The Bring leg of Vector 2 CLOSES at scope (a). No structural
exclusion of level-5 geometry from the Δ_λ wall is claimed (that would be a
scope-(b) claim needing a proved invariant about the wall itself); the
magnitude scalar m ∈ (0, 1/√5) remains OPEN and nothing is wired.

SOURCES:
  [BN12]     Braden–Northover, SIGMA 8 (2012) 065 (library/sigma12-065/sigma12-065.pdf):
             p.13 intersection matrix C; p.14 S′, S, T; p.8 eq (4.2).
  [b4-slater] computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py
             — the [1⁴] exchange matrix S_ex, spectrum {±√5, ±1}.
  [parent]   computations/probes/vector2_double_pincer_probe.py (A5 core).
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


def cp(M):
    """Exact factored characteristic polynomial over ℚ."""
    return sp.factor(sp.Matrix(M).charpoly(x).as_expr())


#: Transcription gates, in the order they run: (name, passed).
_GATES: list[tuple[str, bool]] = []

#: Labels of the polynomials checked for an (x²−5) factor.
_NO_X2M5: list[str] = []


def _no_x2_minus_5(label: str, p) -> bool:
    """Check `p` has no (x²−5) factor, recording that the check happened.

    The witness claims nine polynomials are checked — the five members of
    C·A^k·S', the two block restrictions, and the two S'-eigenspace
    restrictions. Collecting the labels lets the assertion pin that nine, so
    dropping one is a witness failure rather than a quieter claim.
    """
    ok = sp.rem(sp.expand(p), x**2 - 5, x) != 0
    _NO_X2M5.append(label)
    if not ok:
        raise AssertionError(f"(x²−5) | {label}")
    return ok


def _gate(name: str, ok, detail: str = "") -> bool:
    """Record a transcription gate's outcome, then enforce it.

    The gates below were bare `assert`s, and a bare `assert` aborts the run —
    leaving *nothing* in the witness. So the witness could only ever be
    written along the path where every gate held, which is how
    `add_assertion(computed="True", expected="True")` came to stand in for
    seven real checks without misreporting anything (bean `qou-26f2`): on the
    only path that reaches it, "True" is correct. It was unfalsifiable rather
    than wrong.

    Recording before raising puts the outcome in the witness and lets the
    assertions below pin the gate *count* against the number this file claims
    to run — so deleting a gate fails the witness instead of quietly shrinking
    what "all gates pass" means.
    """
    ok = bool(ok)
    _GATES.append((name, ok))
    if not ok:
        raise AssertionError(f"{name}: {detail}" if detail else name)
    return ok


def main() -> int:
    wb = WitnessBuilder("vector2-a5-sprime-residue", engine="sympy")

    # ── BN12 matrices (visually transcribed; verified below) ────────────────
    # Intersection matrix of the α basis (BN12 p.13 — "precisely the matrix
    # claimed by Riera and Rodríguez").
    C = sp.Matrix([
        [ 0,  1, -1,  1, -1,  0,  1, -1],
        [-1,  0,  1, -1,  1,  0,  0,  0],
        [ 1, -1,  0,  1, -1,  1, -1,  0],
        [-1,  1, -1,  0,  1, -1,  1,  0],
        [ 1, -1,  1, -1,  0,  1, -1,  1],
        [ 0,  0, -1,  1, -1,  0,  1, -1],
        [-1,  0,  1, -1,  1, -1,  0,  1],
        [ 1,  0,  0,  0, -1,  1, -1,  0],
    ])
    # Anti-involution of the real structure on α₁..α₈ (BN12 p.14).
    Sp_ = sp.Matrix([
        [ 0,  0,  0,  0,  0,  0, -1,  0],
        [ 0,  0,  0,  0,  0, -1,  0,  0],
        [ 0,  0,  0,  0, -1,  0,  0,  0],
        [ 0,  0,  0, -1,  0,  0,  0,  0],
        [ 0,  0, -1,  0,  0,  0,  0,  0],
        [ 0, -1,  0,  0,  0,  0,  0,  0],
        [-1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  1,  0,  1,  0,  1,  0,  1],
    ])
    # Canonical anti-involution normal form (BN12 p.14): one nondividing oval.
    I4, Z4 = sp.eye(4), sp.zeros(4, 4)
    Scan = sp.Matrix(sp.BlockMatrix([[I4, I4], [Z4, -I4]]))
    # Symplectic transformation T (BN12 p.14).
    T = sp.Matrix([
        [-1,  2,  1,  2, -1,  1,  0,  1],
        [ 0,  1,  0, -3,  0,  0,  0, -1],
        [-2,  1,  2, -1,  0,  1,  0,  0],
        [ 0,  0, -1,  0, -1,  0, -1,  0],
        [ 2, -2, -3, -2,  0, -1, -1, -1],
        [-1,  0,  1,  3,  0,  1,  0,  1],
        [ 1, -1, -1, -2,  0, -1,  0, -1],
        [-1,  2,  3,  2,  0,  1,  1,  1],
    ])
    # Basis-change matrix (4.2) (BN12 p.8): α basis → canonical {𝔞ᵢ, 𝔟ᵢ}.
    B42 = sp.Matrix([
        [1,  0, 0,  0, -2, 0,  1,  0],
        [1, -1, 0, -1, -1, 1,  1,  1],
        [1, -1, 0,  0, -1, 2,  1, -1],
        [0, -1, 0,  0,  1, 2,  0,  0],
        [1, -1, 1,  0, -1, 1, -1, -1],
        [1, -1, 1, -1,  0, 0, -1,  1],
        [1, -1, 1, -1,  0, 1,  0,  1],
        [0, -1, 0, -1,  1, 1,  1,  2],
    ])
    J = sp.Matrix(sp.BlockMatrix([[Z4, I4], [-I4, Z4]]))

    # ── V1–V6: transcription property gates (all exact) ─────────────────────
    # Grouped to match the seven gates the witness `source` string names, so
    # the count the assertion pins is the count a reader is told about.
    _gate("C_antisymmetric_det_1", C.T == -C and C.det() == 1, str(C.det()))
    # S'² = I together with charpoly(S') = (x−1)⁴(x+1)⁴ — the involution and
    # its 4+4 eigenvalue split are one structural fact, kept in one gate so
    # the total stays at the seven the `source` string enumerates.
    _gate("S_prime_is_involution_with_4_4_split",
          Sp_**2 == sp.eye(8)
          and sp.expand(cp(Sp_) - (x - 1)**4 * (x + 1)**4) == 0)
    _gate("S_prime_anti_symplectic", Sp_ * C * Sp_.T == -C)
    _gate("B42_canonicalises_C_to_J", B42.T * C * B42 == J)
    _gate("T_is_J_symplectic", T.T * J * T == J and T.det() == 1)
    U = T * B42.T
    _gate("U_conjugates_S_prime_to_Scan",
          U * Sp_ * U.inv() == Scan and Scan**2 == sp.eye(8))

    # ── V7: order-5 rotation from the stated basis structure ────────────────
    # α_{2k+1} = R^k α₁, α_{2k+2} = R^k α₂ (k = 0..3);  H₁^R = 0 (quotient is
    # ℙ¹) forces 1 + R + R² + R³ + R⁴ = 0, so R α₇ = −(α₁+α₃+α₅+α₇), etc.
    # Row-vector convention to match S′ and C.
    Acol = sp.zeros(8, 8)
    Acol[2, 0] = Acol[3, 1] = Acol[4, 2] = Acol[5, 3] = 1
    Acol[6, 4] = Acol[7, 5] = 1
    for r in (0, 2, 4, 6):
        Acol[r, 6] = -1
    for r in (1, 3, 5, 7):
        Acol[r, 7] = -1
    A = Acol.T  # row convention
    # Gate 7 of the seven named: the order-5 rotation and its dihedral
    # relation to S'. One gate, four conjuncts, matching the `source` string's
    # "A^5=I, ACA^T=C, S'AS'=A^{-1}".
    _gate("A_order_5_dihedral_with_S_prime",
          A**5 == sp.eye(8)
          and A * C * A.T == C
          and sp.expand(cp(A) - (x**4 + x**3 + x**2 + x + 1)**2) == 0
          and Sp_ * A * Sp_ == A**4
          and all((A**k * Sp_)**2 == sp.eye(8) for k in range(5)))

    # ── the comparison: natural twisted forms vs {±√5, ±1} ──────────────────
    target = sp.expand((x - 1) * (x + 1) * (x**2 - 5))
    S_ex = sp.Matrix([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, -1], [1, 1, -1, 0]])
    assert sp.expand(cp(S_ex) - target) == 0, cp(S_ex)

    SC = Sp_ * C                     # the symmetric twisted intersection form
    assert SC.T == SC, "S'C must be symmetric (S' anti-symplectic)"
    cp_SC = sp.expand(SC.charpoly(x).as_expr())
    cp_SC_expected = sp.expand(
        x**8 + x**7 - 22*x**6 - 9*x**5 + 38*x**4 + 4*x**3 - 16*x**2 + x + 1)
    assert cp_SC == cp_SC_expected, cp_SC
    assert sp.Poly(cp_SC, x).is_irreducible, "charpoly(S'C) irreducible over ℚ"
    assert SC.det() == 1

    # family C·A^k·S' — no member divisible by (x²−5)
    family = {}
    for k in range(5):
        p = sp.expand((C * A**k * Sp_).charpoly(x).as_expr())
        family[k] = p
        _no_x2_minus_5(f"charpoly(C A^{k} S')", p)

    # the two A-stable, S'-stable 4-dim blocks (odd / even index)
    odd, even = [0, 2, 4, 6], [1, 3, 5, 7]
    assert all(Sp_[r, c] == 0 for c in odd for r in even)
    assert all(Sp_[r, c] == 0 for c in even for r in odd)
    assert all(A[r, c] == 0 for c in odd for r in even)
    cp_odd = sp.factor(SC.extract(odd, odd).charpoly(x).as_expr())
    cp_even = sp.factor(SC.extract(even, even).charpoly(x).as_expr())
    assert sp.expand(cp_odd - (x**2 - 2*x - 1) * (x**2 + 2*x - 1)) == 0, cp_odd
    assert sp.expand(cp_even - (x + 1) * (x**3 - 3*x + 1)) == 0, cp_even
    _no_x2_minus_5("charpoly(S'C | odd block)", cp_odd)
    _no_x2_minus_5("charpoly(S'C | even block)", cp_even)

    # S'-eigenspace (fixed / anti-fixed) restrictions of the twisted form
    Lp = sp.Matrix.hstack(*(Sp_ - sp.eye(8)).nullspace())
    Lm = sp.Matrix.hstack(*(Sp_ + sp.eye(8)).nullspace())
    assert Lp.shape[1] == 4 and Lm.shape[1] == 4
    cp_fix = sp.factor((Lp.T * SC * Lp).charpoly(x).as_expr())
    cp_anti = sp.factor((Lm.T * SC * Lm).charpoly(x).as_expr())
    assert sp.expand(cp_fix - x**2 * (x - 2) * (x + 3)) == 0, cp_fix
    assert sp.expand(cp_anti - x**2 * (x - 1) * (x + 2)) == 0, cp_anti
    _no_x2_minus_5("charpoly(S'C | S'-fixed)", cp_fix)
    _no_x2_minus_5("charpoly(S'C | S'-anti-fixed)", cp_anti)

    # basis-independent falsifier: discriminant square class 1 vs 5
    det_twisted, det_exchange = SC.det(), S_ex.det()
    assert det_twisted == 1 and det_exchange == 5
    # 5 is squarefree and ≠ 1 ⇒ distinct classes in ℚ*/(ℚ*)²
    assert not sp.sqrt(sp.Rational(det_exchange, det_twisted)).is_rational

    # signature of S'C (numeric roots of the exact charpoly): 4+, 4− → 0
    roots = sp.Poly(cp_SC, x).nroots(n=30)
    sig = sum(1 if sp.re(r) > 0 else -1 for r in roots)
    assert sig == 0, sig

    # recorded-not-interpreted: canonical-frame golden units
    cp_JS = sp.factor((J * Scan).charpoly(x).as_expr())
    assert sp.expand(cp_JS - (x**2 + x - 1)**4) == 0, cp_JS
    assert (J * Scan).T == J * Scan

    # ── report ──────────────────────────────────────────────────────────────
    print("=" * 74)
    print(" A5 residue: BN12 anti-involution S' spectrum vs [1⁴] exchange")
    print(" audit-only / scope-(a) / no fit / nothing wired")
    print("=" * 74)
    print("transcription gates: C antisym det 1; S'^2=I; S'CS'^T=-C;")
    print("  B42^T C B42 = J; T^T J T = J, det T = 1; (T·B42^T) S' (·)^{-1} = S;")
    print("  A^5=I, ACA^T=C, charpoly(A)=Φ₅²; S'AS'=A^{-1}   — ALL PASS")
    print(f"charpoly(S'C) = {cp_SC}")
    print("  irreducible over ℚ ⇒ no rational/quadratic eigenvalues at all")
    for k in range(5):
        print(f"charpoly(C A^{k} S') = {sp.factor(family[k])}")
    print(f"blocks: odd  {cp_odd}  → ±(1+√2), ±(√2−1)  [ℚ(√2), silver units]")
    print(f"        even {cp_even}  → −1, 2cos(2πk/9)  [ℚ(ζ₉)⁺]")
    print(f"S'-eigenspace restrictions: {cp_fix}, {cp_anti}")
    print(f"disc classes: det(S'C) = {det_twisted} vs det(S_ex) = {det_exchange}"
          "  → distinct mod squares ⇒ NOT ℚ-congruent in ANY basis")
    print(f"canonical frame (universal, not Bring-specific): charpoly(J·S) = "
          f"{cp_JS} → golden units (−1±√5)/2")
    print("VERDICT: the natural involution-twisted forms, alone, do NOT")
    print("  reproduce {±√5, ±1}. The Bring leg of Vector 2 CLOSES (scope-(a)).")

    # ── witness ─────────────────────────────────────────────────────────────
    wb.set_description(
        "A5 residue of the Vector-2 double pincer: the BN12 (SIGMA 8 (2012) "
        "065) real-structure anti-involution S' and intersection form C were "
        "transcribed from the paper's rendered PDF and property-verified "
        "exactly (S'^2=I; S'CS'^T=-C; B42^T C B42=J; T symplectic; "
        "(T·B42^T)S'(T·B42^T)^{-1} = [[I,I],[0,-I]]; order-5 A with "
        "S'AS'=A^{-1}). Decision: NO natural involution-twisted form "
        "reproduces the He4 [1^4] exchange spectrum {±√5,±1} — the 8×8 "
        "twisted form S'C has an IRREDUCIBLE degree-8 charpoly over ℚ; none "
        "of the five C·A^k·S' charpolys is divisible by (x²−5); the two "
        "A-stable 4-dim block restrictions live in ℚ(√2) (silver units "
        "±(1+√2),±(√2−1)) and ℚ(ζ₉)⁺ ((x+1)(x³−3x+1)); and the "
        "basis-independent discriminant square class (det 1 vs det 5) "
        "obstructs ℚ-congruence in ANY presentation. Recorded coincidence: "
        "the canonical-frame universal twist J·S has charpoly (x²+x−1)⁴ "
        "(golden units), universal for the one-oval topological type, not "
        "Bring-specific. Scope-(a): the Bring leg of Vector 2 closes; the "
        "magnitude scalar m stays OPEN; nothing wired."
    )
    wb.set_audit_only("docs/audits/2026-07-24-vector2-residues-sprime-d5.md")
    wb.add_data("bn12_matrices_verified", {
        "source": "library/sigma12-065/sigma12-065.pdf pp.8,13,14 (visual transcription)",
        "intersection_C": [list(map(int, C.row(i))) for i in range(8)],
        "anti_involution_S_prime": [list(map(int, Sp_.row(i))) for i in range(8)],
        "symplectic_T": [list(map(int, T.row(i))) for i in range(8)],
        "basis_change_4_2": [list(map(int, B42.row(i))) for i in range(8)],
        "property_gates": "C antisym det1; S'^2=I; S'CS'^T=-C; B42^T C B42=J; "
                          "T^T J T=J det1; (T B42^T)S'(T B42^T)^-1=Scan; "
                          "A^5=I ACA^T=C charpoly=Phi5^2; S'AS'=A^-1",
        "note_on_bn12_statement": "BN12 print 'S := TS'T^{-1}'; the exact "
            "reproduction from the printed α-basis S' requires composing with "
            "the (4.2) canonicalisation first: U = T·B42^T gives USU^{-1}... "
            "US'U^{-1} = S exactly (machine-checked).",
    })
    wb.add_data("twisted_spectra_exact", {
        "charpoly_SprimeC": str(cp_SC),
        "charpoly_SprimeC_irreducible_over_Q": True,
        "family_C_Ak_Sprime": {k: str(sp.factor(v)) for k, v in family.items()},
        "block_odd": str(cp_odd) + "  (silver-ratio units, field Q(sqrt2))",
        "block_even": str(cp_even) + "  (field Q(zeta9)+)",
        "sprime_eigenspace_restrictions": [str(cp_fix), str(cp_anti)],
        "signature_SprimeC": 0,
        "det_SprimeC": 1,
        "det_exchange": 5,
        "canonical_frame_J_S": str(cp_JS) + "  (golden units (−1±√5)/2; "
            "universal for one-nondividing-oval genus-4 real structures)",
        "target_exchange_charpoly": str(sp.factor(target)),
    })
    wb.add_caveat(
        "Scope-(a): 'the natural involution-twisted forms, alone, do not "
        "reproduce the exchange spectrum {±√5, ±1}' — plus the basis-"
        "independent discriminant-class obstruction to ℚ-congruence. This "
        "does NOT structurally exclude level-5 geometry from the Δ_λ "
        "magnitude wall (that would be scope-(b), needing a proved invariant "
        "about the wall itself). m ∈ (0, 1/√5) remains OPEN; nothing wired. "
        "The J·S golden-unit coincidence is recorded, not interpreted."
    )
    # Was `computed="True", expected="True"` — unfalsifiable, because the
    # seven gates it summarised were bare `assert`s upstream and the witness
    # is only reached when they all hold (bean `qou-26f2`). They now record
    # through `_gate`, and this pins the *count* against the seven the source
    # string enumerates: remove or merge a gate and the witness fails rather
    # than silently meaning less.
    wb.add_data("transcription_gates",
                [{"name": n, "passed": ok} for n, ok in _GATES])
    wb.add_assertion(
        "sprime_transcription_property_gates",
        computed=sum(1 for _, ok in _GATES if ok),
        expected=7,
        tolerance=0,
        source="All 7 BN12 transcription gates pass exactly: C antisym det 1; "
               "S'^2=I; S'CS'^T=-C; B42^T C B42=J; T^T J T=J det T=1; "
               "(T·B42^T)S'(T·B42^T)^{-1}=[[I,I],[0,-I]]; A^5=I, ACA^T=C, "
               "S'AS'=A^{-1}.",
    )
    wb.add_assertion(
        "twisted_charpoly_irreducible_deg8",
        computed=str(cp_SC),
        expected=str(cp_SC_expected),
        tolerance=0,
        source="charpoly(S'C) is x^8+x^7-22x^6-9x^5+38x^4+4x^3-16x^2+x+1, "
               "irreducible over ℚ — no ±1 or ±√5 eigenvalues.",
    )
    # Same defect, same remedy: 5 family members + 2 block restrictions +
    # 2 S'-eigenspace restrictions = the 9 the source string claims.
    wb.add_data("no_x2_minus_5_checked", list(_NO_X2M5))
    wb.add_assertion(
        "no_x2_minus_5_factor_in_natural_family",
        computed=len(_NO_X2M5),
        expected=9,
        tolerance=0,
        source="None of charpoly(C·A^k·S') (k=0..4), the two block "
               "restrictions, or the S'-eigenspace restrictions is divisible "
               "by (x²−5).",
    )
    wb.add_assertion(
        "block_spectra_exact",
        computed=f"{cp_odd}; {cp_even}",
        expected="(x**2 - 2*x - 1)*(x**2 + 2*x - 1); (x + 1)*(x**3 - 3*x + 1)",
        tolerance=0,
        source="A-stable block twists: silver-ratio units ±(1+√2), ±(√2−1) "
               "(ℚ(√2)) and −1, 2cos(2πk/9) (ℚ(ζ₉)⁺) — wrong number fields "
               "for {±√5, ±1}.",
    )
    wb.add_assertion(
        "discriminant_class_obstruction",
        computed=f"det(S'C)={det_twisted}, det(S_ex)={det_exchange}",
        expected="det(S'C)=1, det(S_ex)=5",
        tolerance=0,
        source="ℚ-congruence preserves det mod squares; 1 and 5 are distinct "
               "square classes ⇒ the Bring twisted form is not congruent to "
               "the exchange form in ANY basis (basis-independent falsifier; "
               "signatures both 0, so disc is the discriminating invariant).",
    )
    wb.add_assertion(
        "canonical_frame_golden_units_recorded",
        computed=str(cp_JS),
        expected=str(sp.factor((x**2 + x - 1)**4)),
        tolerance=0,
        source="J·S (canonical frame) has charpoly (x²+x−1)⁴ — golden units "
               "(−1±√5)/2 ×4. Universal for the one-nondividing-oval type, "
               "not Bring-specific; ≠ {±√5, ±1}. Recorded-not-interpreted.",
    )
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
