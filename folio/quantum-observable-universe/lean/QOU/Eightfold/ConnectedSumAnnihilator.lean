import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Connected sum does not give a map of recurrence ideals

**Bean `qou-zhep`, the connected-sum probe, formalize-first.**

The proposed first target was a map

  `A_{K₁} × A_{K₂} → A_{K₁ # K₂}`

on recurrence ideals in the quantum torus, justified by the classical fact that
the coloured Jones is multiplicative under connected sum,
`J_{K₁ # K₂}(N) = J_{K₁}(N) · J_{K₂}(N)`. I called this "the known-easy
prototype". **This file establishes that the naive form of that map does not
exist**, before any search was run — which is what the formalize-first rule asks
for.

## Why it fails, in one line

The quantum torus acts by two operators. On a *pointwise product* of colour
towers they behave completely differently:

* `M` (diagonal multiplication by `q^n`) **passes to one factor**:
  `M(f·g) = (M f)·g`. It is "half" multiplicative.
* `L` (the colour shift) is **fully multiplicative**: `L(f·g) = (L f)·(L g)`.
  It shifts *both* factors at once.

So an operator built from `L` does not see the two towers as a tensor product —
it sees their pointwise product, and a relation satisfied by one factor is
destroyed by the other. `annihilator_not_monotone` exhibits this with an
explicit witness.

## What this does and does not exclude

**Scope-(b) for the naive map** (an AGENTS.md structural exclusion, with the
invariant exhibited rather than asserted): there is no map sending an
annihilator of `f` to an annihilator of `f·g`, because the containment
`A_f ⊆ A_{f·g}` already fails on a first-order operator over `ℚ`.

**Scope-(a) at most for the programme.** It does *not* exclude a connected-sum
construction. The classical route is the **Hadamard product / creative
telescoping** closure property: the pointwise product of two holonomic sequences
is holonomic, with an annihilator of order at most `n₁ · n₂`. That is a
*construction on operators*, not a map of ideals, and it **raises the order
multiplicatively** — which is the honest shape of the connected-sum case and the
reason it is not the cheap prototype I called it.
-- Ref: [leitner2026] bean `qou-zhep`
-- Ref: [leitner2026] `QOU.Machinery.QuantumTorusAJ` (the `act2` function model)

-/

namespace QOU.Eightfold.ConnectedSumProbe

variable {K : Type*} [CommRing K]

/-- The colour shift `L`, in the function model of `QOU.Machinery.QuantumTorusAJ`
(there `sigma a = fun N => a (N + 1)`). Colours are indexed by `ℕ` here so the
file stays over a plain `CommRing` (AGENTS.md §7c). -/
def shift (f : ℕ → K) : ℕ → K := fun n => f (n + 1)

/-- Diagonal multiplication by `q^n` — the `M` generator. -/
def mulPow (q : K) (f : ℕ → K) : ℕ → K := fun n => q ^ n * f n

/-- `P` annihilates `f`, for the first-order operator `a₀ + a₁·L`. This is the
order-1 case of `QuantumTorusAJ.act2`; order 1 suffices for the obstruction. -/
def annihilates (a₀ a₁ : K) (f : ℕ → K) : Prop :=
  ∀ n, a₀ * f n + a₁ * shift f n = 0

/-! ## The two generators behave differently on a product -/

/-- **`L` is fully multiplicative on pointwise products.** It shifts both
factors; it does not act on one tensor leg. -/
theorem shift_mul (f g : ℕ → K) :
    shift (fun n => f n * g n) = fun n => shift f n * shift g n := rfl

/-- **`M` passes to one factor.** Diagonal multiplication is "half"
multiplicative — the asymmetry with `shift_mul` is the whole obstruction. -/
theorem mulPow_mul_left (q : K) (f g : ℕ → K) :
    mulPow q (fun n => f n * g n) = fun n => mulPow q f n * g n := by
  funext n; simp [mulPow, mul_assoc]

/-- **`M` is NOT fully multiplicative**, witnessed over `ℚ`: applying it to both
factors squares the weight. Stated as a concrete inequality so it is falsifiable
rather than a slogan. -/
theorem mulPow_not_mul_both :
    (fun n => mulPow (2 : ℚ) (fun _ => 1) n * mulPow (2 : ℚ) (fun _ => 1) n) 1
      ≠ mulPow (2 : ℚ) (fun n => (fun _ : ℕ => (1 : ℚ)) n * (fun _ : ℕ => (1 : ℚ)) n) 1 := by
  norm_num [mulPow]

/-! ## The obstruction: annihilators do not survive multiplication -/

/-- The constant tower `f ≡ 1` is annihilated by `L − 1`. -/
theorem annihilates_one : annihilates (-1 : ℚ) 1 (fun _ => 1) := by
  intro n; simp [shift]

/-- **`L − 1` does NOT annihilate `1 · 2^n`.** The residual at colour `n` is
`2^n`, which is nonzero everywhere — so the failure is not an edge case at one
colour. -/
theorem not_annihilates_pow_two (n : ℕ) :
    (-1 : ℚ) * ((fun _ : ℕ => (1 : ℚ)) n * (2 : ℚ) ^ n)
      + 1 * shift (fun m => (fun _ : ℕ => (1 : ℚ)) m * (2 : ℚ) ^ m) n = 2 ^ n := by
  simp [shift, pow_succ]; ring

/-- **The recurrence ideal is not monotone under pointwise multiplication.**

There are towers `f`, `g` and a first-order operator `P` with `P ∈ A_f` and
`P ∉ A_{f·g}`. Concretely `f ≡ 1`, `g = 2^n`, `P = L − 1`: the residual is `2^n`,
nonzero at every colour.

Since `J_{K₁ # K₂} = J_{K₁} · J_{K₂}` pointwise, this is exactly the statement
that **a map `A_{K₁} × A_{K₂} → A_{K₁ # K₂}` cannot be "carry the annihilator
across"**. -/
theorem annihilator_not_monotone :
    ∃ (f g : ℕ → ℚ) (a₀ a₁ : ℚ),
      annihilates a₀ a₁ f ∧ ¬ annihilates a₀ a₁ (fun n => f n * g n) := by
  refine ⟨fun _ => 1, fun n => 2 ^ n, -1, 1, annihilates_one, ?_⟩
  intro h
  have h0 := h 0
  rw [not_annihilates_pow_two 0] at h0
  norm_num at h0

/-! ## Route D closure: pointwise product of first-order towers (`bean qou-blla`)

While `annihilator_not_monotone` shows that `A_f` is not carried into `A_{f·g}`
by the identity map on operators, the pointwise product of two first-order
shift-recurrence towers *is* annihilated by a constructed first-order operator
whose coefficients multiply the factor coefficients: if `a₀·f(n) + a₁·f(n+1) = 0`
and `b₀·g(n) + b₁·g(n+1) = 0`, then

    `-(a₀·b₀)·(f(n)·g(n)) + (a₁·b₁)·(f(n+1)·g(n+1)) = 0`

over any commutative ring `K`. For higher-order recurrences of orders `d₁` and
`d₂`, eliminating the coupled shift states `(f(n+i), g(n+j))` takes place inside
the tensor-product state space of dimension `d₁ · d₂`, which strictly exceeds
`max(d₁, d₂)` whenever `d₁, d₂ ≥ 2`. -/

/-- **Pointwise-product closure for first-order shift annihilators.**
If `a₀ + a₁·L` annihilates `f` and `b₀ + b₁·L` annihilates `g`, then the
constructed operator `-(a₀·b₀) + (a₁·b₁)·L` annihilates the pointwise product
`fun n => f n * g n`. -/
theorem annihilates_pointwise_mul {a₀ a₁ b₀ b₁ : K} {f g : ℕ → K}
    (hf : annihilates a₀ a₁ f) (hg : annihilates b₀ b₁ g) :
    annihilates (-(a₀ * b₀)) (a₁ * b₁) (fun n => f n * g n) := by
  intro n
  have hfn : a₀ * f n + a₁ * shift f n = 0 := hf n
  have hgn : b₀ * g n + b₁ * shift g n = 0 := hg n
  have h_prod : shift (fun m => f m * g m) n = shift f n * shift g n := by
    change f (n + 1) * g (n + 1) = f (n + 1) * g (n + 1)
    ring
  rw [h_prod]
  linear_combination (b₁ * shift g n) * hfn - (a₀ * f n) * hgn

/-- The geometric colour tower `g(n) = 2^n` is annihilated by `L - 2`
(`a₀ = -2`, `a₁ = 1`). -/
theorem annihilates_pow_two :
    annihilates (-2 : ℚ) 1 (fun n : ℕ => (2 : ℚ) ^ n) := by
  intro n
  have h_step : shift (fun m : ℕ => (2 : ℚ) ^ m) n = 2 * (2 : ℚ) ^ n := by
    change (2 : ℚ) ^ (n + 1) = 2 * (2 : ℚ) ^ n
    ring
  rw [h_step]
  ring

/-- Concrete repair of the `not_annihilates_pow_two` obstruction via
`annihilates_pointwise_mul`: combining `f ≡ 1` (`L - 1`) with `g(n) = 2^n`
(`L - 2`) produces the product annihilator `-( (-1)·(-2) ) + (1·1)·L = L - 2`. -/
theorem annihilates_one_mul_pow_two :
    annihilates (-((-1 : ℚ) * (-2 : ℚ))) (1 * 1)
      (fun n : ℕ => (fun _ : ℕ => (1 : ℚ)) n * (2 : ℚ) ^ n) :=
  annihilates_pointwise_mul annihilates_one annihilates_pow_two

/-- **Multiplicative order growth for coupled recurrences (`bean qou-blla`).**
When two recurrence systems have state-space orders `d₁ ≥ 2` and `d₂ ≥ 2`, the
product state-space dimension `d₁ * d₂` is strictly larger than either factor
order `d₁` or `d₂`. -/
theorem product_order_strictly_larger {d₁ d₂ : ℕ}
    (hd₁ : 2 ≤ d₁) (hd₂ : 2 ≤ d₂) :
    d₁ < d₁ * d₂ ∧ d₂ < d₁ * d₂ := by
  constructor
  · nlinarith [hd₁, hd₂]
  · nlinarith [hd₁, hd₂]

end QOU.Eightfold.ConnectedSumProbe
