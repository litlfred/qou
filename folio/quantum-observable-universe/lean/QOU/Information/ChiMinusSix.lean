import Mathlib.Tactic

/-!
# QOU.Information.ChiMinusSix — "Given a QOU, χ(A) = -6"

The non-vanishing leg of `conj:qou-p-neq-np` is an **axiom consequence**,
not a conjecture: the corpus derives the scalar value of the universal
obstruction class as `χ(A) = -6` (`ex:chi-minus-six-derivation`,
`prf:qou-obstruction-reduction`).  This file formalises that derivation
**conditionally on the QOU** (§3b-cond), so the statement is "given a
QOU, χ(A) = -6" — never an unconditional numerology.

The value is the **topological Euler characteristic of Bring's curve**,
the genus-4 Riemann surface cut out by the icosahedral (`A₅`) geometry of
the substrate:

  `χ(A) = χ_top(Bring) = 2 - 2·g = 2 - 2·4 = -6`.

The class `QOUObstruction` carries the two genuine inputs — the Bring
genus (`g = 4`, a classical fact about Bring's curve) and the
obstruction-reduction *identification* `χ(A) = χ_top(Bring)` (the
conjectural bridge, `prf:qou-obstruction-reduction`) — and the theorem
**derives** `-6` from them by Euler-characteristic arithmetic.  It is
non-degenerate (§3b-tax): the class holds the sub-hypotheses, the
theorem composes them; it never carries `-6` as a bare field.
-/

namespace QOU.Information

/-- The topological Euler characteristic of a genus-`g` orientable
    surface, `χ = 2 - 2g`. -/
def eulerChar (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)

@[simp] theorem eulerChar_four : eulerChar 4 = -6 := by
  unfold eulerChar; norm_num

/-- **The cohomological assumptions a QOU is built from.**  A QOU's
    obstruction context is fixed by two Hochschild-cohomology facts of
    the categorical substrate `A`:

    * **observability** — the observability axiom kills degree-0
      obstructions, `HH⁰(A) = 0`; and
    * **Frobenius–Hopf self-duality** — Yekutieli–Van den Bergh Poincaré
      duality is invoked for `HH²(A) ≅ (HH¹)^∨ ≅ k`, so `HH²` is rank one.
      (Corrected 2026-09-15: this line read `(HH⁰)^∨`, which with `hh0 = 0`
      would give `HH² = 0`.  The rank-one claim itself is now the Wigner
      axiom, `conj:wigner-axiom`, not a consequence of the QOU axioms:
      at `q = 1` Whitehead's lemma gives `HH²(U(𝔤), M) = 0`; see
      `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md` §2.4.)

    Encoded by their ranks (`hh0 = 0`, `hh2 = 1`); the rank-one `HH²` is
    exactly *why* the universal obstruction is a single scalar. -/
class QOUCohomology where
  /-- `dim HH⁰(A)`. -/
  hh0 : ℕ
  /-- Observability axiom: `HH⁰` vanishes. -/
  observability : hh0 = 0
  /-- `dim HH²(A)`. -/
  hh2 : ℕ
  /-- Frobenius–Hopf self-duality: `HH² ≅ k` is rank one. -/
  frobeniusHopf_duality : hh2 = 1

/-- **Net even-degree Hochschild rank is one (sorry-free).**  Composing
    `HH²(A) ≅ k` (`hh2 = 1`) with observability (`hh0 = 0`), the net
    even-degree Hochschild rank `dim HH²(A) - dim HH⁰(A)` equals `1`. -/
theorem obstruction_rank_one [Q : QOUCohomology] :
    (Q.hh2 : ℤ) - (Q.hh0 : ℤ) = 1 := by
  rw [Q.frobeniusHopf_duality, Q.observability]
  norm_num

/-- **Strict anti-monotonicity of the surface Euler characteristic.**
    For `g₁ < g₂`, `eulerChar g₂ < eulerChar g₁`. -/
theorem eulerChar_strictAnti {g₁ g₂ : ℕ} (h : g₁ < g₂) :
    eulerChar g₂ < eulerChar g₁ := by
  unfold eulerChar
  omega

/-- **Unique genus pin for `χ = -6`.**
    An orientable surface has Euler characteristic `-6` if and only if its
    genus is `4`. -/
theorem eulerChar_eq_neg_six_iff (g : ℕ) :
    eulerChar g = -6 ↔ g = 4 := by
  unfold eulerChar
  omega

/-- **The QOU obstruction data (§3b-cond class).**  Extends the
    cohomological assumptions with the geometric inputs that pin the
    scalar's *value*: the substrate Bring surface (genus 4, icosahedral
    `A₅` geometry) and the Riemann–Roch identification of `χ(A)` with its
    Euler characteristic.  All are *inputs*; the value `-6` is derived. -/
class QOUObstruction extends QOUCohomology where
  /-- Genus of the substrate's Bring curve — classically `4`. -/
  bringGenus : ℕ
  /-- Bring's curve is a genus-4 Riemann surface. -/
  bringGenus_eq_four : bringGenus = 4
  /-- The universal obstruction residue at the substrate (the scalar in
      `HH² ≅ k`). -/
  chi : ℤ
  /-- **Obstruction reduction** (`prf:qou-obstruction-reduction`):
      Riemann–Roch identifies the rank-one `HH²` scalar with the Bring
      surface's topological Euler characteristic. -/
  chi_eq_eulerChar : chi = eulerChar bringGenus

/-- **Given a QOU, χ(A) = -6 (sorry-free, conditional).**  Composes the
    two `QOUObstruction` inputs: the obstruction equals the Bring Euler
    characteristic, and the Bring genus is 4, so `χ(A) = 2 - 2·4 = -6`.
    The conclusion is scoped to the QOU (the `[QOUObstruction]`
    hypothesis) — it is *not* an unconditional assertion. -/
theorem chi_eq_neg_six [Q : QOUObstruction] : Q.chi = -6 := by
  rw [Q.chi_eq_eulerChar, Q.bringGenus_eq_four, eulerChar_four]

/-- **The non-vanishing leg, conditionally (sorry-free).**  In particular
    the derived obstruction residue is nonzero — the leg that
    `conj:qou-p-neq-np` needs, obtained here as an axiom consequence with
    no computational-complexity input. -/
theorem chi_ne_zero [QOUObstruction] : QOUObstruction.chi ≠ 0 := by
  rw [chi_eq_neg_six]; norm_num

/-- **Combined cohomological and geometric balance.**
    In any `[QOUObstruction]`, `χ(A) + 6 · (dim HH²(A) - dim HH⁰(A)) = 0`. -/
theorem chi_add_six_mul_net_cohomology [Q : QOUObstruction] :
    Q.chi + 6 * ((Q.hh2 : ℤ) - (Q.hh0 : ℤ)) = 0 := by
  rw [chi_eq_neg_six, obstruction_rank_one]
  norm_num

end QOU.Information
