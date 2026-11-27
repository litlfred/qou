import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The Temperley–Lieb condition pins the `H₃(q)` Markov trace uniquely

**What this settles.** Two normalised Markov traces on `H₃(q)` circulate in the
corpus and give *different* values on the Borromean braid `β_Bor` (they differ
by `1.9554e-4` at the substrate — the "convention D vs convention C" split of
[`docs/audits/2026-06-09-binding-trace-convention-split.md`]):

* **convention D** — the Jones / Temperley–Lieb closure, weight vector
  `y = ([4]_q/[2]_q³, 1/[2]_q², 0)`; this is what the production absolute-mass
  facade consumes (`m_p_substrate_identity_50dps.trM_borromean` → `F_Bor` →
  `canonical_mass.py`);
* **convention C** — the full-Hecke Ocneanu / Wenzl `z`-trace at
  `z = 1/(q^{1/2} + q^{-1/2})`, whose three-row weight is *nonzero*.

Since the two agree to `195 ppm` and D is the one that lands on CODATA, the
question (bean `qou-3qrv`) is whether D is **forced** or **selected**. This
file answers the *mathematical half*: **given** that the trace factors through
Temperley–Lieb and is faithful there, D is forced — uniquely, with no residual
freedom and no experimental input.

## The setup

A normalised Markov trace on `H₃(q)` is determined by its Ocneanu parameter `z`
through its values on the three class representatives,

  `tr 1 = 1`,   `tr σ₀ = z`,   `tr σ₀σ₁ = z²`,

expanded in the Frobenius basis `tr = Σ_λ y_λ χ^λ` over `λ ⊢ 3`. The `H₃(q)`
`q`-character table on those representatives is

| `λ`     | `χ^λ(1)` | `χ^λ(σ₀)` | `χ^λ(σ₀σ₁)` |
|---------|----------|-----------|-------------|
| `(3)`   | `1`      | `q`       | `q²`        |
| `(2,1)` | `2`      | `q − q⁻¹` | `−1`        |
| `(1³)`  | `1`      | `−q⁻¹`    | `q⁻²`       |

(computed by `hecke_character_symbolic.q_character_on_braid_word`; the three
hypotheses `hnorm`, `hsigma`, `hsigmasigma` below are exactly these three
equations). `q⁻¹` is carried as a separate element `qi` with `q * qi = 1`, so
every statement here is **division-free** and lives over a generic commutative
domain — the fibre (formal `q`) side of the substrate/archimedean wall, per
AGENTS §7c. Nothing below mentions `ℝ`, an ordering, or a numerical `q₀`.

## The result

`markovWeights_eq_jones_of_threeRow_eq_zero`: the Temperley–Lieb condition
`y_(1³) = 0` **together with** faithfulness on `TL₃` (`y_(2,1) ≠ 0`) forces

  `[2]_q² · y_(2,1) = 1`,   `y_(3) = 1 − 2·y_(2,1)`,   `z · [2]_q = q²`

where `[2]_q = q + q⁻¹`. Both hypotheses are load-bearing:
`markovWeights_degenerate_root` exhibits the *other* solution of `y_(1³) = 0`,
namely `z = q` with `y = (1, 0, 0)` — the trivial character, which annihilates
the two-row block as well and so is not a faithful trace on `TL₃`. Dropping
`y_(2,1) ≠ 0` therefore makes the conclusion false, not merely unprovable.

`threeRow_ne_zero_of_ocneanu_ne`: the contrapositive that matters in practice —
any faithful normalised Markov trace whose parameter satisfies `z·[2]_q ≠ q²`
has `y_(1³) ≠ 0`, i.e. does **not** factor through Temperley–Lieb. This is the
structural separation of convention C from convention D.

## What this file does NOT establish — and where the premise WAS established

This file proves the implication only. The premise — that the *mass* fibre
functor lands in `Rep(SU_q(2)) ≃ TL` rather than in the full `H₃(q)` — is not
shown here.

**It is shown in the file next to this one.** `FibreDimensionForcesTL.lean`
(same directory, sorry-free, `lean`-direct exit 0) proves the chain from the
fibre dimension instead of assuming the cap:

* `ocneanu_param_eq_of_fibre_qdim` — `z·[N]_q = q^N`: the fibre's quantum
  dimension DETERMINES the Ocneanu parameter, leaving no residual freedom;
* `ocneanu_param_of_two_dim_fibre` — `N = 2 ⟹ z(q+q⁻¹) = q²`, i.e. `z_D`;
* `threeRow_eq_zero_of_jones_ocneanu` — `z_D ⟹ y_(1³) = 0`, the cap itself;
* `twoDimFibre_pins_h3_weights` — the composite.

And `dim = 2` is not an extra assumption: `lem:feynman-eigenbasis-decomposition`
states the mass channel's decomposition as
`V^⊗n ≅ ⊕_{λ⊢n, ℓ(λ)≤2} V_λ ⊗ S_λ` with `V` the fundamental of `SU_q(2)` — the
row cap is already in its index set, so `(1³)` is absent at `n = 3` by
construction. Bean `qou-n1dj`, resolved 2026-08-08; analysis in
[`docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md`].

The paragraph this replaces said the premise was unestablished and the corpus
inconsistent, and pointed only at
[`docs/audits/2026-08-08-borromean-trace-convention-forcing.md`] — the audit that
POSED the question. That audit's §5 ("What would close it") was answered the same
day by the file in this directory, and the note here was never updated. It was
read as current by at least one later session (2026-08-30), which spent an arc
concluding "the cap is a ruling, not a derivation" on the strength of it.
-/

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R] [IsDomain R]

/-- **The Temperley–Lieb condition pins the `H₃(q)` Markov trace uniquely.**

Let `y₃, y₂₁, y₁₃` be the Frobenius weights of a normalised Markov trace on
`H₃(q)` with Ocneanu parameter `z`, i.e. `tr = Σ_λ y_λ χ^λ` satisfying
`tr 1 = 1`, `tr σ₀ = z`, `tr σ₀σ₁ = z²` against the `H₃(q)` character table
(the three hypotheses `hnorm`, `hsigma`, `hsigmasigma`).

If the trace **factors through Temperley–Lieb** (`hTL : y₁₃ = 0`, the three-row
block is annihilated) and is **faithful on `TL₃`** (`hfaith : y₂₁ ≠ 0`), then
the weight vector and the Ocneanu parameter are completely determined:

  `[2]_q² · y₂₁ = 1`,   `y₃ = 1 − 2 y₂₁`,   `z · [2]_q = q²`,

with `[2]_q = q + qi`. Solving the first for `y₂₁` recovers the Jones-closure
vector `([4]_q/[2]_q³, 1/[2]_q², 0)` — convention D. -/
theorem markovWeights_eq_jones_of_threeRow_eq_zero
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hTL : y₁₃ = 0)
    (hfaith : y₂₁ ≠ 0) :
    (q + qi) ^ 2 * y₂₁ = 1 ∧ y₃ = 1 - 2 * y₂₁ ∧ z * (q + qi) = q ^ 2 := by
  subst hTL
  -- Normalisation gives `y₃` in terms of `y₂₁`.
  have hy₃ : y₃ = 1 - 2 * y₂₁ := by linear_combination hnorm
  subst hy₃
  -- The `σ₀` equation collapses to `z = q − [2]_q · y₂₁`.
  have hz : z = q - (q + qi) * y₂₁ := by linear_combination -hsigma
  subst hz
  -- Substituting into the `σ₀σ₁` equation and expanding, every term without a
  -- factor of `y₂₁` cancels, leaving `y₂₁ = [2]_q² · y₂₁²`.
  have key : y₂₁ * ((q + qi) ^ 2 * y₂₁) = y₂₁ * 1 := by
    linear_combination -hsigmasigma + 2 * y₂₁ * hqi
  -- Cancelling the (nonzero) `y₂₁` is exactly where the degenerate branch dies.
  have hy₂₁ : (q + qi) ^ 2 * y₂₁ = 1 := mul_left_cancel₀ hfaith key
  refine ⟨hy₂₁, rfl, ?_⟩
  -- `z·[2]_q = q·[2]_q − [2]_q²·y₂₁ = (q² + q·qi) − 1 = q²`.
  linear_combination hqi - hy₂₁

omit [IsDomain R] in
/-- **The faithfulness hypothesis is not decorative.**

The Temperley–Lieb condition `y₁₃ = 0` alone has a *second* solution: the
trivial character `y = (1, 0, 0)` at `z = q`. It satisfies all three Markov
equations, so `markovWeights_eq_jones_of_threeRow_eq_zero` genuinely needs
`y₂₁ ≠ 0` — without it the conclusion `z·[2]_q = q²` is false (here
`z·[2]_q = q² + 1 ≠ q²`). This solution annihilates the two-row block too, so
it is not a faithful trace on `TL₃`; that is what rules it out. -/
theorem markovWeights_degenerate_root (q qi : R) (hqi : q * qi = 1) :
    ((1 : R) + 2 * 0 + 0 = 1) ∧
    (q * 1 + (q - qi) * 0 + (-qi) * 0 = q) ∧
    (q ^ 2 * 1 + (-1) * 0 + qi ^ 2 * 0 = q ^ 2) ∧
    q * (q + qi) = q ^ 2 + 1 := by
  refine ⟨by ring, by ring, by ring, ?_⟩
  linear_combination hqi

/-- **Convention C does not factor through Temperley–Lieb.**

Contrapositive of the uniqueness theorem, in the form that separates the two
production conventions: a faithful normalised Markov trace whose Ocneanu
parameter fails `z·[2]_q = q²` necessarily has a **nonzero** three-row weight.
Applied to the Wenzl `z`-trace (convention C, `z = 1/(q^{1/2}+q^{-1/2})`), this
says C carries the `(1³)` block and so is not the Jones/TL trace. -/
theorem threeRow_ne_zero_of_ocneanu_ne
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hfaith : y₂₁ ≠ 0)
    (hz : z * (q + qi) ≠ q ^ 2) :
    y₁₃ ≠ 0 := fun hTL =>
  hz (markovWeights_eq_jones_of_threeRow_eq_zero q qi z y₃ y₂₁ y₁₃ hqi hnorm
    hsigma hsigmasigma hTL hfaith).2.2

/-- **Converse direction (`D ⟹ TL`): convention D's Ocneanu parameter forces
`y₁₃ = 0` (`bean qou-6moa`).**

`markovWeights_eq_jones_of_threeRow_eq_zero` proves `TL + faithful ⟹ D`
(`y₁₃ = 0 ∧ y₂₁ ≠ 0 ⟹ z · [2]_q = q²`); citing it as proof of `y₁₃ = 0` would
cite a theorem for its own hypothesis. The converse implication `D ⟹ TL`
(`z · [2]_q = q² ⟹ y₁₃ = 0` when `[2]_q ≠ 0` and `[3]_q = [2]_q² − 1 ≠ 0`)
holds unconditionally without any faithfulness assumption on `y₂₁` (and is also
proved as `FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`). -/
theorem threeRow_eq_zero_of_conventionD
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hzD : z * (q + qi) = q ^ 2)
    (hb2ne : q + qi ≠ 0)
    (h3ne : (q + qi) ^ 2 - 1 ≠ 0) :
    y₁₃ = 0 := by
  have hA : (q + qi) * (y₂₁ + y₁₃) = q - z := by
    linear_combination q * hnorm - hsigma
  have hA' : (q + qi) ^ 2 * (y₂₁ + y₁₃) = 1 := by
    linear_combination (q + qi) * hA - hzD + hqi
  have hB : (2 * q ^ 2 + 1) * y₂₁ + (q ^ 2 - qi ^ 2) * y₁₃ = q ^ 2 - z ^ 2 := by
    linear_combination q ^ 2 * hnorm - hsigmasigma
  have hB' : (2 * q ^ 2 + 1) * ((q + qi) ^ 2 * y₂₁)
      + (q ^ 2 - qi ^ 2) * ((q + qi) ^ 2 * y₁₃) = 2 * q ^ 2 + 1 := by
    linear_combination (q + qi) ^ 2 * hB - (z * (q + qi) + q ^ 2) * hzD
      + (2 * q ^ 2 + q * qi + 1) * hqi
  have hkill : ((q + qi) ^ 2 * ((q + qi) ^ 2 - 1)) * y₁₃ = 0 := by
    linear_combination -hB' + (2 * q ^ 2 + 1) * hA'
      + 2 * (q + qi) ^ 2 * y₁₃ * hqi
  rcases mul_eq_zero.mp hkill with h | h
  · exact absurd h (mul_ne_zero (pow_ne_zero 2 hb2ne) h3ne)
  · exact h

end QOU.BraidsAndKnots
