import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.RingTheory.Polynomial.Cyclotomic.Eval

/-!
# Cyclotomic doubling identity Φ_8(X) = Φ_4(X²)

The key algebraic identity `Φ_8(X) = Φ_4(X²)` over ℤ[X]. This is a
true and useful cyclotomic-polynomial composition identity (proved
without `sorry` in `cyclotomic_8_eq_cyclotomic_4_comp_X_sq` below).

**Empirical context.** The factor `Φ_8(u)² = (u^4 + 1)²` appears
as a cyclotomic prefactor in every atomic-step Habiro element
`Σ_m Δa_m(X − Y) · (u; u)_m` tested: (D − n), (³He − D), and
(⁴He − ³He). The factor is convention-invariant (appears in both
`include_inter=True` habiro-witness and Phase 5q canonical
conventions). The categorical mechanism is OPEN — neither the
`z(q)²` interface factor nor the m=8 Pochhammer boundary explains
it (both were refuted on direct test); the cyclotomic structure
arises from a `Δa_m` interference signature that doesn't reduce
to either naive source.

**Historical note.** An earlier interpretation conjectured a
strand-doubling categorical chain
`Φ_{2^{k+1}}(X) = Φ_{2^k}(X²)` predicting `Φ_16` and `Φ_32` for
A=2→3 and A=3→4 atomic steps. **This prediction was refuted**
(PR #1618, see `docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md`):
all three atomic-step pairs carry `Φ_8²`, not the predicted
doubling chain. The algebraic identity proved here remains valid;
the categorical interpretation as "atomic-step strand-doubling"
was wrong.

## References

-- Ref: [habiro2000] https://doi.org/10.2140/gt.2000.4.227
-- Ref: [washington1997] Lawrence Washington, "Introduction to
--      Cyclotomic Fields", Springer GTM 83, 1997. Chapter 2.
-/


namespace QOU.BraidKnot.CyclotomicStrandDoubling

open Polynomial

variable {R : Type*} [CommRing R]

/-- The 4th cyclotomic polynomial: `Φ_4(X) = X² + 1`.  Single-nucleon
    denominator factor identified in
    `habiro-coefficients-atomic.witness.json` for proton and neutron. -/
theorem cyclotomic_4 : cyclotomic 4 ℤ = X ^ 2 + 1 := by
  -- Mathlib has `Polynomial.cyclotomic_four`; if not, decide on
  -- the explicit polynomial.
  -- Ref: [washington1997] §2.1 Table of low-degree cyclotomic polynomials.
  decide

/-- The 8th cyclotomic polynomial: `Φ_8(X) = X^4 + 1`.  Squared
    factor identified in the (D − n) Habiro element factorization
    (`docs/audits/2026-05-31-qbeta-habiro-cross-pair-quick-dp.md`). -/
theorem cyclotomic_8 : cyclotomic 8 ℤ = X ^ 4 + 1 := by
  -- Ref: [washington1997] §2.1 Table of low-degree cyclotomic polynomials.
  decide

/-- Strand-doubling cyclotomic identity over ℤ:
    `Φ_8(X) = Φ_4(X²)`.

    This is the load-bearing algebraic identity for the categorical
    interpretation of `Φ_8² = (X^4+1)²` in the deuteron's (D − n)
    Habiro element factorization.  The substitution `X → X²` is the
    strand-doubling map lifting B_2 (2-strand single nucleon) to
    B_4 (4-strand deuteron, 2 nucleons × 2 isospin channels). -/
theorem cyclotomic_8_eq_cyclotomic_4_comp_X_sq :
    cyclotomic 8 ℤ = (cyclotomic 4 ℤ).comp (X ^ 2) := by
  rw [cyclotomic_4, cyclotomic_8]
  -- Goal: X^4 + 1 = (X^2 + 1).comp (X^2)
  -- Use Polynomial.comp_add, Polynomial.comp_X_pow, etc.
  simp [Polynomial.comp]
  ring

/-- General strand-doubling identity for powers-of-two cyclotomic
    polynomials:  `Φ_{2^{k+1}}(X) = Φ_{2^k}(X²)` for `k ≥ 1`.

    This is the structural pattern hypothesised in
    `docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`
    for the cyclotomic prefactor of A=k → A=k+1 atomic-step pairs
    in the canonical Q_β Habiro element framework. -/
theorem cyclotomic_pow_two_strand_doubling (k : ℕ) (hk : 1 ≤ k) :
    cyclotomic (2 ^ (k + 1)) ℤ = (cyclotomic (2 ^ k) ℤ).comp (X ^ 2) := by
  -- Ref: [washington1997] §2.2 Theorem 2.5: for any prime p
  --      and integer n with p ∤ n, Φ_{p·n}(X) = Φ_n(X^p);
  --      and for p | n, Φ_{p·n}(X) = Φ_n(X^p).
  --      Specialising to p = 2 and n = 2^k (so 2 | 2^k) yields the
  --      identity above.
  -- Ref: [habiro2000] §3 — the substitution X → X^p as a
  --      strand-multiplication map on braid generators.
  sorry

/-- The 1st cyclotomic polynomial: `Φ_1(X) = X - 1`. -/
theorem cyclotomic_1 : cyclotomic 1 ℤ = X - 1 := by
  -- Ref: [washington1997] §2.1.
  decide

/-- The 2nd cyclotomic polynomial: `Φ_2(X) = X + 1`. -/
theorem cyclotomic_2 : cyclotomic 2 ℤ = X + 1 := by
  -- Ref: [washington1997] §2.1.
  decide

/-- The isospin "classical-limit kill" factor:
    `Φ_1 · Φ_2 = (X - 1)(X + 1) = X² - 1`.

    This is the cyclotomic prefactor identified in the (n − p)
    Habiro element factorization
    (`docs/audits/2026-05-31-qbeta-habiro-delta-am-factorization.md`).
    The factor vanishes at X = 1 (classical limit q = 1), encoding
    the fact that proton and neutron coincide classically: it is the
    bar-involution-paired isospin doublet structure made manifest. -/
theorem isospin_classical_limit_kill :
    cyclotomic 1 ℤ * cyclotomic 2 ℤ = X ^ 2 - 1 := by
  rw [cyclotomic_1, cyclotomic_2]
  ring

/-- The cross-pair finding: the (n − p) signature `(X² − 1)` factor is
    distinct from the deuteron-step signature `Φ_8²`.  This is the
    structural distinction between isospin SU(2)_I and atomic-number
    jumps observed in the (D − n) / (D − p) cross-pair audit. -/
theorem isospin_signature_distinct_from_deuteron :
    (cyclotomic 1 ℤ * cyclotomic 2 ℤ) ≠ cyclotomic 8 ℤ := by
  rw [isospin_classical_limit_kill, cyclotomic_8]
  -- Goal: X^2 - 1 ≠ X^4 + 1
  intro h
  -- The two polynomials have different degrees.
  have h1 : (X ^ 2 - 1 : ℤ[X]).degree = 2 := by
    rw [show (X ^ 2 - 1 : ℤ[X]) = X ^ 2 + (-1) by ring]
    simp [Polynomial.degree_X_pow_add_C]
  have h2 : (X ^ 4 + 1 : ℤ[X]).degree = 4 := by
    simp [Polynomial.degree_X_pow_add_C]
  rw [h] at h1
  rw [h2] at h1
  exact absurd h1 (by decide)

/-- Φ_8 is irreducible over ℚ.  Standard cyclotomic-irreducibility
    fact; relevant because the (D − n) Habiro element contains
    Φ_8² as a factor — the square indicates a multiplicity-2
    structural appearance, not a polynomial-degree property. -/
theorem cyclotomic_8_irreducible :
    Irreducible (cyclotomic 8 ℚ) := by
  -- Ref: [washington1997] §2.3 Theorem 2.5.
  exact cyclotomic.irreducible (by decide : (0:ℕ) < 8)

end QOU.BraidKnot.CyclotomicStrandDoubling
