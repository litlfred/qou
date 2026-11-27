import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The fibre dimension determines the Ocneanu parameter: `z · [N]_q = q^N`

**What this settles.** `MarkovTraceTLUniqueness.lean` proves the *implication*
"the `H₃(q)` Markov trace factors through Temperley–Lieb ⟹ its Ocneanu
parameter satisfies `z · [2]_q = q²` (convention D)". Its own docstring records
what it does **not** establish:

> Nothing here shows that the *mass* fibre functor lands in `Rep(SU_q(2)) ≃ TL`
> rather than in the full `H₃(q)`.

This file supplies the missing bridge from the other side. Rather than assuming
the Temperley–Lieb quotient, it starts from the **fibre**: if the trace is the
categorical (quantum) trace on `V^{⊗n}` for a fibre `V` of quantum dimension
`dim_q V = [N]_q`, then the Ocneanu parameter is *determined by `N` alone*,

  `z · [N]_q = q^N`,

and at `N = 2` this is **literally** the hypothesis
`markovWeights_eq_jones_of_threeRow_eq_zero` concludes. So the two arguments
close a loop: "2-dimensional fibre" and "factors through Temperley–Lieb" pin the
same trace, and neither derivation touches a measured number.

## Where the input comes from

`dim_q V = [2]_q` is not assumed here for convenience — it is what the mass
chapter already says. The mass channel's Schur–Weyl decomposition
(`lem:feynman-eigenbasis-decomposition`) reads

  `V^{⊗n} ≅ ⨁_{λ ⊢ n, ℓ(λ) ≤ 2} V_λ ⊗ S_λ`,  `V` = fundamental of `SU_q(2)`,

with the row cap `ℓ(λ) ≤ 2` in the index set and `⌊n/2⌋ + 1` summands. At
`n = 3` that sum is `{(3), (2,1)}`: the three-row block `(1³)` is **absent**, so
`y_(1³) = 0` is forced and there is no residual freedom left for a `(1³)`-weight
to occupy.

## The computation

Write `[m]` for the balanced quantum integer, `[m] · (q − q⁻¹) = q^m − q^{-m}`.
For the fundamental `V` of `U_q(sl_N)`, `V ⊗ V ≅ S²V ⊕ Λ²V` with quantum
dimensions `[N][N+1]/[2]` and `[N][N−1]/[2]`, and the braiding acts as `q` on
the symmetric and `−q⁻¹` on the antisymmetric part (AGENTS §7a: `σ_i` has
eigenvalues `q`, `−q⁻¹`). The Ocneanu parameter is read off at `n = 2` from
`z · dim_q(V ⊗ V) = q · dim_q S²V − q⁻¹ · dim_q Λ²V`, and the whole computation
collapses through the single identity

  `q · [N+1] − q⁻¹ · [N−1] = q^N · [2]`      (`qNumber_shift_identity`)

whose content is that the two `q^{-N}` contributions cancel. Hence
`z · [N]² = q^N · [N]`, i.e. `z · [N] = q^N`.

Everything is **division-free**: `q⁻¹` is carried as a separate element `qi`
with `q * qi = 1`, and `q^N`, `q^{-N}` as `a`, `ai` with `a * ai = 1`. Nothing
below mentions `ℝ`, an ordering, or a numerical `q₀` — this is the fibre
(formal `q`) side of the substrate/archimedean wall, per AGENTS §7c.

## What this does NOT establish

That `dim_q V = [2]_q` is the *right* fibre for the mass channel on physical
grounds — that is an input, taken from the mass chapter's own decomposition
lemma (cited above) and from `thm:su2-emergence`. What is new here is that the
input **suffices**: once the fibre is fixed, the Ocneanu parameter has no
remaining freedom, so there is no second trace on `H₃(q)` available to the mass
channel. Colour antisymmetry, which genuinely needs a three-row block, therefore
requires a *different* (3-dimensional) fibre and a *different* functor — it is
not reachable by re-tuning this one.
-/

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R]

/-- **The shift identity behind the Ocneanu parameter.**

For the balanced quantum integers, presented division-free via
`[m] * (q − qi) = q^m − q^{-m}` with `a = q^N`, `ai = q^{-N}`:

  `q · [N+1] − qi · [N−1] = q^N · [2]`.

The content is a cancellation: `q · (a·q − ai·qi)` contributes `−ai·q·qi` and
`−qi · (a·qi − ai·q)` contributes `+ai·q·qi`, so the two `q^{-N}` terms cancel
*identically* and only the `a`-terms `a(q² − qi²) = a · [2] · (q − qi)` survive.

Stated in the `(q − qi)`-multiplied form so that no hypothesis about
`q − qi ≠ 0` is needed; `ocneanu_param_eq_of_fibre_qdim` consumes it in exactly
this form. -/
theorem qNumber_shift_identity
    (q qi a ai b2 bNsucc bNpred : R)
    (hbNsucc : bNsucc * (q - qi) = a * q - ai * qi)
    (hbNpred : bNpred * (q - qi) = a * qi - ai * q)
    (hb2 : b2 * (q - qi) = q ^ 2 - qi ^ 2) :
    (q * bNsucc - qi * bNpred) * (q - qi) = (a * b2) * (q - qi) := by
  linear_combination q * hbNsucc - qi * hbNpred - a * hb2

/-- **The fibre's quantum dimension determines the Ocneanu parameter.**

Setup: `V` is a fibre with `dim_q V = bN = [N]_q`, so
`dim_q(V ⊗ V) = bN * bN`, and `V ⊗ V ≅ S²V ⊕ Λ²V` with quantum dimensions
`dS = [N][N+1]/[2]` and `dL = [N][N−1]/[2]` — presented division-free as
`dS * b2 = bN * bNsucc` and `dL * b2 = bN * bNpred`.

The braiding acts as `q` on `S²V` and `−qi` on `Λ²V` (AGENTS §7a), so the
categorical trace of `σ₀` on `V ⊗ V` is `q * dS − qi * dL`, and the Ocneanu
parameter `z`, defined by `tr(x σ_n) = z · tr(x)`, satisfies at `n = 2`

  `htr : z * (bN * bN) = q * dS − qi * dL`.

Conclusion: `z * bN = a`, i.e. **`z · [N]_q = q^N`** — the parameter is a
function of the fibre dimension and nothing else.

The non-degeneracy hypotheses are the expected ones: `q − qi ≠ 0` (`q` is not
`±1`, so the quantum integers are not all degenerate), `b2 ≠ 0` (`[2]_q ≠ 0`)
and `bN ≠ 0` (`V` has nonzero quantum dimension). -/
theorem ocneanu_param_eq_of_fibre_qdim [IsDomain R]
    (q qi a ai b2 bN bNsucc bNpred dS dL z : R)
    (hbNsucc : bNsucc * (q - qi) = a * q - ai * qi)
    (hbNpred : bNpred * (q - qi) = a * qi - ai * q)
    (hb2 : b2 * (q - qi) = q ^ 2 - qi ^ 2)
    (hdS : dS * b2 = bN * bNsucc)
    (hdL : dL * b2 = bN * bNpred)
    (htr : z * (bN * bN) = q * dS - qi * dL)
    (hdiff : q - qi ≠ 0) (hb2ne : b2 ≠ 0) (hbNne : bN ≠ 0) :
    z * bN = a := by
  -- The shift identity, with the `(q − qi)` factor cancelled off.
  have hshift : q * bNsucc - qi * bNpred = a * b2 :=
    mul_right_cancel₀ hdiff
      (qNumber_shift_identity q qi a ai b2 bNsucc bNpred hbNsucc hbNpred hb2)
  -- Multiply the trace equation by `b2`, replace `dS·b2` and `dL·b2` by their
  -- quantum-dimension values, and apply the shift identity.
  have key : (z * bN) * (bN * b2) = a * (bN * b2) := by
    linear_combination b2 * htr + q * hdS - qi * hdL + bN * hshift
  exact mul_right_cancel₀ (mul_ne_zero hbNne hb2ne) key

/-- **A two-dimensional fibre forces convention D.**

The `N = 2` instance of `ocneanu_param_eq_of_fibre_qdim`, written out with the
quantum dimensions substituted: `dim_q V = [2] = q + qi`,
`dim_q S²V = [3] = q² + 1 + qi²`, `dim_q Λ²V = [1] = 1`, so the categorical
trace of `σ₀` on `V ⊗ V` is `q·[3] − qi·1` and the Ocneanu equation reads
`z · [2]² = q·[3] − qi`.

Conclusion: `z * (q + qi) = q ^ 2` — which is **verbatim** the third component
of `markovWeights_eq_jones_of_threeRow_eq_zero`'s conclusion, i.e. convention D.
The `[2]_q ≠ 0` hypothesis is the same non-degeneracy that file needs.

Note this is a genuine cross-check, not a restatement: there, `z·[2] = q²` is
*derived from* the Temperley–Lieb condition `y_(1³) = 0`; here it is derived from
`dim_q V = [2]_q` with no reference to the quotient. Two independent routes, one
parameter. -/
theorem ocneanu_param_of_two_dim_fibre [IsDomain R]
    (q qi z : R) (hqi : q * qi = 1) (hb2ne : q + qi ≠ 0)
    (htr : z * (q + qi) ^ 2 = q * (q ^ 2 + 1 + qi ^ 2) - qi * 1) :
    z * (q + qi) = q ^ 2 := by
  have key : (z * (q + qi)) * (q + qi) = q ^ 2 * (q + qi) := by
    linear_combination htr + (qi - q) * hqi
  exact mul_right_cancel₀ hb2ne key

/-- **Convention D's parameter forces the three-row weight to vanish.**

The converse direction of `markovWeights_eq_jones_of_threeRow_eq_zero`: there,
`y_(1³) = 0` implies `z·[2] = q²`; here, `z·[2] = q²` implies `y_(1³) = 0`.
Together the two say the Temperley–Lieb condition and the Ocneanu value are
*equivalent* labels for the same trace, so the fibre-side route of
`ocneanu_param_of_two_dim_fibre` lands on convention D's weight vector and not
merely on its parameter.

Hypotheses are the same Markov/character-table equations as in that file
(`tr 1 = 1`, `tr σ₀ = z`, `tr σ₀σ₁ = z²` expanded against the `H₃(q)`
`q`-character table), plus the two non-degeneracies the elimination needs:
`[2]_q ≠ 0` and `[2]_q² ≠ 1`. The second is exactly `[3]_q ≠ 0`, since
`[2]_q² − 1 = q² + 1 + qi² = [3]_q` when `q·qi = 1` — the root-of-unity
degeneracy at which `TL₃` itself collapses, so its exclusion is expected rather
than an artefact of the proof. -/
theorem threeRow_eq_zero_of_jones_ocneanu [IsDomain R]
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2)
    (hzD : z * (q + qi) = q ^ 2)
    (hb2ne : q + qi ≠ 0)
    (h3ne : (q + qi) ^ 2 - 1 ≠ 0) :
    y₁₃ = 0 := by
  -- Eliminate `y₃` from the `σ₀` equation.
  have hA : (q + qi) * (y₂₁ + y₁₃) = q - z := by
    linear_combination q * hnorm - hsigma
  -- Scale by `[2]_q` and use `z·[2] = q²` together with `q·qi = 1`.
  have hA' : (q + qi) ^ 2 * (y₂₁ + y₁₃) = 1 := by
    linear_combination (q + qi) * hA - hzD + hqi
  -- Eliminate `y₃` from the `σ₀σ₁` equation.
  have hB : (2 * q ^ 2 + 1) * y₂₁ + (q ^ 2 - qi ^ 2) * y₁₃ = q ^ 2 - z ^ 2 := by
    linear_combination q ^ 2 * hnorm - hsigmasigma
  -- Scale by `[2]_q²`; the right-hand side collapses to `2q² + 1` because
  -- `(z·[2])² = q⁴` and `q²·[2]² = q⁴ + 2q² + 1`.
  have hB' : (2 * q ^ 2 + 1) * ((q + qi) ^ 2 * y₂₁)
      + (q ^ 2 - qi ^ 2) * ((q + qi) ^ 2 * y₁₃) = 2 * q ^ 2 + 1 := by
    linear_combination (q + qi) ^ 2 * hB - (z * (q + qi) + q ^ 2) * hzD
      + (2 * q ^ 2 + q * qi + 1) * hqi
  -- Substituting `[2]²·y₂₁ = 1 − [2]²·y₁₃` cancels the `2q²+1` on both sides
  -- and leaves `[2]²·([2]² − 1)·y₁₃ = 0`.
  have hkill : ((q + qi) ^ 2 * ((q + qi) ^ 2 - 1)) * y₁₃ = 0 := by
    linear_combination -hB' + (2 * q ^ 2 + 1) * hA'
      + 2 * (q + qi) ^ 2 * y₁₃ * hqi
  rcases mul_eq_zero.mp hkill with h | h
  · exact absurd h (mul_ne_zero (pow_ne_zero 2 hb2ne) h3ne)
  · exact h

/-- **The composite: a two-dimensional fibre pins the whole `H₃(q)` weight
vector, with no experimental input.**

Chaining `ocneanu_param_of_two_dim_fibre` into
`threeRow_eq_zero_of_jones_ocneanu` and then into
`markovWeights_eq_jones_of_threeRow_eq_zero` (in
`MarkovTraceTLUniqueness.lean`) would give the full convention-D weight vector.
This statement records the first two links: from `dim_q V = [2]_q` alone, the
three-row weight vanishes and the two-row weight is pinned by
`[2]_q² · y_(2,1) = 1`.

Read against the mass chapter's decomposition
`V^{⊗n} ≅ ⨁_{ℓ(λ) ≤ 2} V_λ ⊗ S_λ`, this is the answer to "which trace does the
mass channel use": the one its own fibre already chose. -/
theorem twoDimFibre_pins_h3_weights [IsDomain R]
    (q qi z y₃ y₂₁ y₁₃ : R)
    (hqi : q * qi = 1)
    (hb2ne : q + qi ≠ 0)
    (h3ne : (q + qi) ^ 2 - 1 ≠ 0)
    (hfibre : z * (q + qi) ^ 2 = q * (q ^ 2 + 1 + qi ^ 2) - qi * 1)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (hsigma : q * y₃ + (q - qi) * y₂₁ + (-qi) * y₁₃ = z)
    (hsigmasigma : q ^ 2 * y₃ + (-1) * y₂₁ + qi ^ 2 * y₁₃ = z ^ 2) :
    y₁₃ = 0 ∧ (q + qi) ^ 2 * y₂₁ = 1 := by
  have hzD : z * (q + qi) = q ^ 2 :=
    ocneanu_param_of_two_dim_fibre q qi z hqi hb2ne hfibre
  have hTL : y₁₃ = 0 :=
    threeRow_eq_zero_of_jones_ocneanu q qi z y₃ y₂₁ y₁₃ hqi hnorm hsigma
      hsigmasigma hzD hb2ne h3ne
  refine ⟨hTL, ?_⟩
  -- With `y₁₃ = 0`, the `σ₀` equation gives `z = q − [2]·y₂₁`; combined with
  -- `z·[2] = q²` and `q·qi = 1` that is `[2]²·y₂₁ = 1`.
  have hA : (q + qi) * (y₂₁ + y₁₃) = q - z := by
    linear_combination q * hnorm - hsigma
  linear_combination (q + qi) * hA - hzD + hqi - (q + qi) ^ 2 * hTL

/-- Scaling the normalization equation `y₃ + 2 * y₂₁ + y₁₃ = 1` by `(q + qi)^2`
under `y₁₃ = 0` and `(q + qi)^2 * y₂₁ = 1` pins the trivial-block weight via
`(q + qi)^2 * y₃ = (q + qi)^2 - 2`. -/
theorem twoDimFibre_pins_y3_scaled
    (q qi y₃ y₂₁ y₁₃ : R)
    (hnorm : y₃ + 2 * y₂₁ + y₁₃ = 1)
    (h13 : y₁₃ = 0)
    (h21 : (q + qi) ^ 2 * y₂₁ = 1) :
    (q + qi) ^ 2 * y₃ = (q + qi) ^ 2 - 2 := by
  linear_combination (q + qi) ^ 2 * hnorm - 2 * h21 - (q + qi) ^ 2 * h13

end QOU.BraidsAndKnots
