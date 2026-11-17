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

/-- **`q`-Weyl commutation in the function model (`qou-zhep`):**
Shifting after diagonal multiplication by `q^n` multiplies by an extra factor of `q`:
`L(M_q f)(n) = q · M_q(L f)(n)`. -/
theorem shift_mulPow_comm (q : K) (f : ℕ → K) (n : ℕ) :
    shift (mulPow q f) n = q * mulPow q (shift f) n := by
  simp [shift, mulPow, pow_succ', mul_assoc]

/-- **Hadamard multiplicative closure of first-order annihilators (`qou-zhep`):**
While `A_f ⊆ A_{f·g}` fails (`annihilator_not_monotone`), if `(L - a₁)` annihilates `f`
and `(L - b₁)` annihilates `g`, then `(L - a₁·b₁)` annihilates the pointwise product `f · g`. -/
theorem annihilates_pointwise_mul {f g : ℕ → K} {a₁ b₁ : K}
    (hf : annihilates (-a₁) 1 f) (hg : annihilates (-b₁) 1 g) :
    annihilates (-(a₁ * b₁)) 1 (fun n => f n * g n) := by
  intro n
  have hfn : shift f n = a₁ * f n := by
    have h := hf n
    linear_combination h
  have hgn : shift g n = b₁ * g n := by
    have h := hg n
    linear_combination h
  change -(a₁ * b₁) * (f n * g n) + 1 * (shift f n * shift g n) = 0
  rw [hfn, hgn]
  ring

end QOU.Eightfold.ConnectedSumProbe
