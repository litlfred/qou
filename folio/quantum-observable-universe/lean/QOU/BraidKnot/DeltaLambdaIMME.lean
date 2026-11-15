import Mathlib.Tactic

/-
  Δ_λ residual as a degree-2 isospin polynomial (IMME) — exact algebra.

  Follow-up to `DeltaLambdaExponentKeystone.lean` (PR #3089). The canonical
  residual `log_{q₀} Δ_λ` is, as a function of the isospin projection
  `T₃ = (Z−N)/2`, the Wigner Isobaric Multiplet Mass Equation shape

      f(T₃) = a + b·T₃ + c·T₃²

  with `a` the bar-even isoscalar (leading `10A−5`, A≤4), `b·T₃` the bar-ODD
  linear writhe Z-correction (#3089), and `c·T₃²` the bar-EVEN QUADRATIC.

  This file is the exact parity bookkeeping that explains WHY mirror pairs
  measure only `b` and triplets are needed for `c`:

  - the mirror difference `f(T₃) − f(−T₃) = 2·b·T₃` cancels both even terms
    (`a` and `c·T₃²`) — the explicit-quadratic refinement of
    `DeltaLambdaExponentKeystone.mirror_baseline_cancels`;
  - the triplet symmetric 2nd difference `f(1) + f(−1) − 2·f(0) = 2·c`
    isolates the quadratic;
  - the third finite difference vanishes — the Wigner "rank-≤2 isotensor" /
    Askey–Racah truncation made falsifiable (`Δ³ = 0`, no `d·T₃³`).

  All `ring` over a generic `[CommRing R]` (§7c: pure algebra, no archimedean
  construct — the residual values live in `ℝ` only at the evaluation site).

  -- Ref: [leitner2026] docs/audits/2026-06-29-delta-lambda-imme-askey.md;
  --      Wigner (1957), isobaric multiplet mass equation.
-/

namespace QOU.BraidKnot

/-- The IMME form: a degree-2 polynomial in the isospin projection `T₃`,
`a + b·T₃ + c·T₃²`. -/
def imme {R : Type*} [CommRing R] (a b c T3 : R) : R := a + b * T3 + c * T3 ^ 2

/-- **The isoscalar.** The central (`T₃ = 0`) value is `a`. -/
theorem imme_at_zero {R : Type*} [CommRing R] (a b c : R) :
    imme a b c 0 = a := by
  unfold imme; ring

/-- **Mirror difference isolates the linear coefficient.** The bar-even `a` and
`c·T₃²` cancel, leaving `2·b·T₃`. This is the explicit-quadratic refinement of
`mirror_baseline_cancels` (#3089): a mirror pair can only ever measure `b`,
never `c`, no matter how large the quadratic. -/
theorem imme_mirror_diff {R : Type*} [CommRing R] (a b c T3 : R) :
    imme a b c T3 - imme a b c (-T3) = 2 * b * T3 := by
  unfold imme; ring

/-- **Triplet 2nd difference isolates the quadratic.** For an isobaric triplet
`T₃ ∈ {−1, 0, +1}`, the symmetric second difference `f(1) + f(−1) − 2·f(0)`
cancels `a` and `b·T₃`, leaving `2·c`. This is why measuring `c` requires three
multiplet members, not a mirror pair. -/
theorem imme_triplet_2nd_diff {R : Type*} [CommRing R] (a b c : R) :
    imme a b c 1 + imme a b c (-1) - 2 * imme a b c 0 = 2 * c := by
  unfold imme; ring

/-- **Askey–Racah / Wigner truncation, made falsifiable.** A degree-2 IMME has a
**vanishing third finite difference**
`Δ³f(x) = f(x+3) − 3 f(x+2) + 3 f(x+1) − f(x) = 0`. Equivalently: no `d·T₃³`
term can hide in the residual — the "charge-dependent forces are rank-≤2
isotensors" statement (the Askey–Racah cutoff) is the testable identity that a
fourth multiplet member must satisfy. -/
theorem imme_third_diff_zero {R : Type*} [CommRing R] (a b c x : R) :
    imme a b c (x + 3) - 3 * imme a b c (x + 2) + 3 * imme a b c (x + 1)
      - imme a b c x = 0 := by
  unfold imme; ring

end QOU.BraidKnot
