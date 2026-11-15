/-
Copyright (c) 2026 litlfred. All rights reserved.

# What the base q-shift actually DOES to the colour curve's `[k]_z` ladder (W1)

Two W1 bricks (bean `qou-d8de`) already stand and they do not touch:

* `QOU.Mass.QDiffProlongationBaseOperator` — the base Jackson operator, and the fact
  that it names the quantum integer: `(q·z)^n − z^n = [n]_q·(q−1)·z^n`, i.e.
  `D_q(z^n) = [n]_q·z^{n−1}` where the classical derivative gives `n·z^{n−1}`.
* `QOU.Mass.ColorCurveQIntegerForm` — the colour spectral cubic **is** a q-integer
  curve: `C_z(X) = [1]_z·X³ + [2]_z·X² + [3]_z·X + [4]_z`.

The second file says, in prose, that *"the base q-shift `z ↦ q·z` acts on each
coefficient through the q-integer functional equations, i.e. `Σ` carries a natural
q-shift structure"* — and proves only the coefficient identity. **What neither file
computes is the composite: what `D_q` does to `[n]_z`.** That is this file.

## The identity

`jackson_zInt_numerator`, over any `CommRing`, in the cleared form the base-operator
file uses (no division, so no `Field` and no `z ≠ 0`):

  `[n+1]_{q·z} − [n+1]_z  =  (q − 1)·z·∑_{k<n} [k+1]_q · z^k`

Dividing by the Jackson denominator `(q−1)z`:

  **`D_q [n+1]_z = ∑_{k<n} [k+1]_q·z^k`**

— the **q-graded z-integer** `gradedZInt`. Read it beside the classical
`d/dz [n+1]_z = ∑_{k<n} (k+1)·z^k`: the Jackson operator puts `[k+1]_q` exactly where
the classical derivative puts `k+1`, and `gradedZInt_one` confirms the two agree at
`q = 1`. This is the mechanism by which the substrate parameter `q` enters data that is
itself **q-free** — the gap named by the 2026-06-25 z2bn audit, which excluded the
classical prolongation precisely because `Σ`'s spectral data carries no `q` while the
anchors do.

## The consequence for the curve: the ladder shifts by one and stays in the class

`qshift_colorSpectralCubic`:

  `C_{q·z}(X) − C_z(X) = (q−1)·z·( g₁·X² + g₂·X + g₃ )`,  `gᵢ = gradedZInt q z i`

so the Jackson q-derivative of the colour cubic is

  **`D_q C(X) = g₁·X² + g₂·X + g₃`**   against   `C_z(X) = [1]_z·X³ + [2]_z·X² + [3]_z·X + [4]_z`

— the same shape with the ladder index dropped by one and `[k]_z` replaced by
`gradedZInt q z (k−1)`. The operator **preserves the q-integer-curve class**. That
closure is what makes the base operator the geometrically adapted one rather than a
convenient choice, and it is a computation, not an assertion.

## Why this needs no branch, which is the whole point

`QOU.Mass.QGaugeSpectralRigidity` (and #6769/#7185 before it) establish that the
`z ↦ q·z` correspondence admits **no** single-valued lift to `Σ`: individual sheet
values `X_i(q·z)` are not canonically matched to `X_j(z)`. The bean records this as
obstruction (ii) — *"a single-valued `D_q` on the jet bundle requires choosing a branch
of the `z↦qz` correspondence on `Σ`"*.

The coefficients are **symmetric functions of the sheets**, hence single-valued rational
functions of `z`, so `a_k(q·z)` is unambiguous with no choice made. Everything here is
therefore branch-free by construction: the prolongation is taken on the symmetric /
coefficient data, where the obstruction does not live.

## Scope — what this is NOT

* **Not the jet-tower prolongation.** `D_q : Jⁿ E → Jⁿ⁺¹ E` compatible with the SW
  connection is untouched, as in both predecessor files. `λ_SW^{(n)}` is not constructed
  and no period `∮ λ_SW^{(n)}` is computed.
* **Not a base-level operator ON `Σ`.** Everything here lives on `ℂ(z)`, applied to `Σ`'s
  coefficients. That is consistent with `QGaugeSpectralRigidity`, which places the
  q-difference structure on the base rather than on the curve — it is not a workaround
  for that result, it is the same conclusion from the constructive side.
* **No comparison with the anchors `a_D^{(n)}`, deliberately.** `a_D^{(n)}` is a *period*
  — a function of `q` alone — while `D_q [n]_z` is a function of `z` and `q`. The two are
  not of the same type, and matching them would require the `∮` that does not exist yet.
  Reporting a coincidence between them would be numerology; none is asserted.
* No fit, no wiring, no conjecture-class asserting an identification.

§7c: everything is over a generic `[CommRing R]`; the `[n]_q` naming specialisation lives
in the predecessor files and is not repeated. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-25-z2bn-prolongation-qdifference-constraint.md
-/
import QOU.Mass.QDiffProlongationBaseOperator
import QOU.Mass.ColorCurveQIntegerForm

namespace QOU.Mass.QShiftColorCoefficientLadder

open Finset
open QOU.Mass.QDiffProlongationBaseOperator (jackson_monomial_numerator_commRing)
open QOU.Mass.ColorCurveQIntegerForm (colorSpectralCubic)

variable {R : Type*} [CommRing R]

/-- The **q-graded z-integer** `∑_{k<n} [k+1]_q · z^k`.

It is the Jackson q-derivative of `[n+1]_z` (`jackson_zInt_numerator`), and it is the
q-deformation of the classical `d/dz [n+1]_z = ∑_{k<n} (k+1)·z^k`: the coefficient of
`z^k` is `[k+1]_q` where the classical one is `k+1` (`gradedZInt_one`). Written with the
bare geometric sum `∑_{j<k+1} q^j` rather than `qInt`, so the definition lives over a
`CommRing`; see the predecessor files for the `[·]_q` naming over a `Field`. -/
def gradedZInt (q z : R) (n : ℕ) : R :=
  ∑ k ∈ range n, (∑ j ∈ range (k + 1), q ^ j) * z ^ k

@[simp] theorem gradedZInt_zero (q z : R) : gradedZInt q z 0 = 0 := by
  simp [gradedZInt]

/-- The ladder step: `gradedZInt` grows by one term of `[n+1]_q·z^n`. -/
theorem gradedZInt_succ (q z : R) (n : ℕ) :
    gradedZInt q z (n + 1) = gradedZInt q z n + (∑ j ∈ range (n + 1), q ^ j) * z ^ n := by
  simp [gradedZInt, Finset.sum_range_succ]

/-- **The Jackson q-derivative of a z-integer, cleared.**

`[n+1]_{q·z} − [n+1]_z = (q−1)·z·∑_{k<n} [k+1]_q·z^k`.

Dividing by the Jackson denominator `(q−1)z` gives `D_q [n+1]_z = gradedZInt q z n`. The
induction step is exactly the base-operator file's monomial identity
`jackson_monomial_numerator_commRing`, applied one degree at a time — so this is the
composite of the two existing W1 bricks and nothing more. -/
theorem jackson_zInt_numerator (q z : R) (n : ℕ) :
    (∑ i ∈ range (n + 1), (q * z) ^ i) - (∑ i ∈ range (n + 1), z ^ i)
      = (q - 1) * z * gradedZInt q z n := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hmon := jackson_monomial_numerator_commRing q z (n + 1)
      rw [Finset.sum_range_succ (fun i => (q * z) ^ i) (n + 1),
        Finset.sum_range_succ (fun i => z ^ i) (n + 1), gradedZInt_succ]
      linear_combination ih + hmon

/-- **`q → 1` degeneration.** `gradedZInt 1 z n = ∑_{k<n} (k+1)·z^k`, the classical
`d/dz [n+1]_z`. So the q-graded ladder limits to the classical one, exactly as the base
operator's `[n]_1 = n` does. -/
theorem gradedZInt_one (z : R) (n : ℕ) :
    gradedZInt 1 z n = ∑ k ∈ range n, ((k : R) + 1) * z ^ k := by
  unfold gradedZInt
  refine Finset.sum_congr rfl ?_
  intro k _
  simp

/-- The first three rungs, written out. `D_q [2]_z = 1`, `D_q [3]_z = 1 + [2]_q·z`,
`D_q [4]_z = 1 + [2]_q·z + [3]_q·z²` — the three coefficients of the colour cubic. -/
theorem gradedZInt_one_eq (q z : R) : gradedZInt q z 1 = 1 := by
  simp [gradedZInt, Finset.sum_range_succ]

theorem gradedZInt_two_eq (q z : R) : gradedZInt q z 2 = 1 + (1 + q) * z := by
  simp [gradedZInt, Finset.sum_range_succ]

theorem gradedZInt_three_eq (q z : R) :
    gradedZInt q z 3 = 1 + (1 + q) * z + (1 + q + q ^ 2) * z ^ 2 := by
  simp [gradedZInt, Finset.sum_range_succ]

/-- **The q-shift of the colour spectral cubic, in closed form.**

`C_{q·z}(X) − C_z(X) = (q−1)·z·( g₁·X² + g₂·X + g₃ )` with `gᵢ = gradedZInt q z i`.

Dividing by `(q−1)z`, the Jackson q-derivative of the colour cubic is

  `D_q C(X) = gradedZInt q z 1 · X² + gradedZInt q z 2 · X + gradedZInt q z 3`

against `C_z(X) = [1]_z·X³ + [2]_z·X² + [3]_z·X + [4]_z`: **the same shape, ladder index
dropped by one, `[k]_z` replaced by `gradedZInt q z (k−1)`.** The operator preserves the
q-integer-curve class.

Branch-free by construction: the coefficients are symmetric functions of the sheets,
so `a_k(q·z)` involves no choice of sheet — which is where obstruction (ii) of the W1
bean lives, and why it is absent here. -/
theorem qshift_colorSpectralCubic (q z X : R) :
    colorSpectralCubic (q * z) X - colorSpectralCubic z X
      = (q - 1) * z * (gradedZInt q z 1 * X ^ 2 + gradedZInt q z 2 * X
          + gradedZInt q z 3) := by
  unfold colorSpectralCubic
  rw [gradedZInt_one_eq, gradedZInt_two_eq, gradedZInt_three_eq]
  ring

/-- **The `X³` coefficient is untouched**, which is why the degree drops: it is the
constant `[1]_z = 1`, carrying no `z`, so the q-shift annihilates it. The classical
derivative does the same thing for the same reason. -/
theorem qshift_leading_coeff_invariant (q z : R) :
    (∑ i ∈ range 1, (q * z) ^ i) - (∑ i ∈ range 1, z ^ i) = 0 := by
  simp

/-- **`q → 1`: the q-shift difference degenerates to the classical derivative.** At
`q = 1` the whole difference is zero (the shift is trivial), and the *quotient* — the
bracket on the right — becomes `∑ (k+1)z^k` rungwise by `gradedZInt_one`. Stated as the
bracket identity so that no division by `q − 1` is needed. -/
theorem qshift_bracket_at_one (z X : R) :
    gradedZInt 1 z 1 * X ^ 2 + gradedZInt 1 z 2 * X + gradedZInt 1 z 3
      = X ^ 2 + (1 + 2 * z) * X + (1 + 2 * z + 3 * z ^ 2) := by
  rw [gradedZInt_one_eq, gradedZInt_two_eq, gradedZInt_three_eq]
  ring

end QOU.Mass.QShiftColorCoefficientLadder
