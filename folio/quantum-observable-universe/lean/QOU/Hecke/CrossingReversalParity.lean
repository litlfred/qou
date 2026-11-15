/-
Copyright (c) 2026 litlfred. All rights reserved.

# The crossing reversal `σ^k − σ^{−k}` is a scalar only at ODD `k`

## What this is for

`QOU.FlavorSplit.topological_flavor_split_of_central`
(`mass-theory/flavor-split-habiro-derivation.lean`) proves that the proton/neutron
crossing reversal `σ³ − σ⁻³` is the **central scalar** `h(h² + 3) = q³ − q⁻³`, and
`conj:flavor-split-habiro-derivation` builds on that to propose an `H₄`
alternating-channel route to the substrate flavour split

    δ  =  (q−1)²(1 − q⁻⁴)/3  =  ℏ_q² · h · [2]_q / 3 ,   [2]_q = q + q⁻¹ .

This file asks the formalize-first question that route needs answered before it is
run: **at which `k` is `σ^k − σ^{−k}` a scalar at all?**  The answer is a parity
obstruction sitting exactly between the mechanism and the quantity it is aimed at.

## The mechanism, in one line

Reduce both generators by their own quadratics — `σ² = hσ + 1` and the conjugate
`σ⁻² = 1 − hσ⁻¹` — so that `σ^k = A_k σ + B_k` and `σ^{−k} = (−1)^{k+1} A_k σ⁻¹ +
(−1)^k B_k` with `A_k, B_k` polynomials in `h`.  Subtracting,

* **`k` odd**  →  `D_k = A_k·(σ − σ⁻¹) + 2B_k = A_k h + 2B_k` — a polynomial in
  `h`, hence **central**, since `σ − σ⁻¹ = h`;
* **`k` even** →  `D_k = A_k·(σ + σ⁻¹)` — a central multiple of the **resolvent**
  `u := σ + σ⁻¹ = 2σ − h`, which is *not* central unless `σ` is.

So `σ³ − σ⁻³ = h(h²+3)` is not a fact about the number three; it is the `k = 3`
instance of a parity.  `reversal_five` is the next one, `h(h⁴ + 5h² + 5)`; the even
cases `reversal_two` and `reversal_four` are `h·u` and `h(h²+2)·u`.

`resolvent_sq` records the invariant underneath: `u² = h² + 4` is central, so even
powers of `u` are central and odd ones are not — which is the same statement read
through the recursion `D_{k+2} = u·D_{k+1} − D_k` (`reversal_rec`).

## What it prunes — and this is the point

`δ`'s numerator is `h · [2]_q = q² − q⁻²`, i.e. the **`k = 2`** member of the
family `q^k − q^{−k} = h·[k]_q` that the odd reversals realise as scalars.  And
`k = 2` is exactly where the parity fails:

    σ² − σ⁻²  =  h · (σ + σ⁻¹)                       (`reversal_two`)

is **not** a scalar.  Its two values on the Hecke generator's spectrum
`{q, −q⁻¹}` are `+(q² − q⁻²)` and `−(q² − q⁻²)` — the right magnitude with an
undetermined sign.  So obtaining `δ`'s numerator from a crossing reversal requires
**choosing the symmetric channel**, and the algebra does not supply that choice:
`reversal_two_forces_resolvent_central` says a central value at `k = 2` forces the
resolvent `u` to be central (given `h` invertible), i.e. forces `σ` central, which
fails in `H_n(q)` for `n ≥ 3`.

**Scope (b), invariant named** (the parity above), and **narrow**: within the
single-generator family `σ^k − σ^{−k}` only.  Nothing here excludes `h·[2]_q`
arising from some other Hecke element — it says that the *one* exact result
`conj:flavor-split-habiro-derivation` rests on does not reach it, and names the
step (channel selection) that any repair must supply.

**What is proved here is the parity's INSTANCES at `k = 2, 4` (even) and `k = 5`
(odd), plus the recursion and the invariant — not the general-`k` statement.**
The general form is verified symbolically for `k ≤ 11` in
`computations/qbeta/crossing_reversal_parity_probe.py` (6/6), together with the
two channel values at `k = 2` and the odd subsequence's central recursion; it is
not formalised, and should not be cited as though it were.

## A tactic note, because the statements look odd

`reversal_four` reads `h * (h² + 1 + 1) * u` and `reversal_five` writes `5h²` and
`5` as repeated sums.  That is **not** a different claim — it is the same
polynomial — and it is deliberate: `noncomm_ring` normalises an integer
coefficient to `n • x` and cannot commute the resulting `n •` past a ring
element, so `5 • (h·h·h)` and `h · 5 • (h·h)` do not match in its normal form
even though numerals are central in any ring.  Writing the coefficients as sums
keeps every step inside what the tactic can close.  Restoring `h * (h² + 2) * u`
was tried and fails for exactly that reason, not for a mathematical one.

## Provenance

`u² = h² + 4` is elementary and standard in the Chebyshev / Jones–Wenzl literature;
the claim here is only that **this corpus does not carry it** — grepped over
`content/`, `computations/`, `docs/` and `.beans/`, where the sole crossing-reversal
result is the `k = 3` one cited above.  The `library/` tier was not searched, so
this is not a claim about the literature.

## 🛑 RETRACTED — this section said the conjecture's OWN channel gives the wrong sign

**Superseded 2026-09-13, in the same arc.  The mathematics below is untouched and
correct; the sentence that read it onto the block was wrong.**

What this section said: that `conj:flavor-split-habiro-derivation` "states its
channel choice, and it is the *alternating* one", quoting *"The weak interaction
is strictly left-handed, so it projects onto the fully alternating channel of
`H₄`"*, and concluded that the block's own channel therefore gives the flavour
split backwards.

**What is actually true: that conflated the block's two LEVELS.**  The block has
a baseline and a residual, and the alternating channel is claimed for the
*residual* — the ≈ 1.76e-6, 0.128 % Schwinger-analogue refinement sitting on top
of the baseline, in structural parallel with the `α_EM` `(1 − h²α)` term.  It is
**not** claimed for the baseline, which the block carries channel-free as a
central scalar.  So there is no wrong-sign claim to make against the block here.

**What replaces it, and it is sharper.**  The block's *narrative* half derives
the reversal at `k = 3` (`q³ − q⁻³`, central — the odd case of `reversal_rec`)
while its *formula* half displays `X_baseline = (q−1)²(1−q⁻⁴)/3`, which is the
reversal at `k = 2`.  Those are different numbers — `ℏ_q²(q³−q⁻³)/3` is +51.17 %
against the measured split where the displayed baseline is −0.128 % — related by
an undeclared factor ≈ 1.5136.  So the quantity the block actually uses sits at
`k = 2`, where by `reversal_two` the reversal is **not** central, and needs a
trace rather than a channel.  That trace is `2hz − h²`, and it reproduces the
baseline **exactly** at the augmentation `z = q` and `α = (q⁴+1)/(q²+1)²` times
it at the canonical `z_D`.  See `QOU/Hecke/MarkovCrossingReversal.lean` and
`computations/qbeta/flavour_split_baseline_is_augmentation_trace_probe.py`.

**What survives here unchanged.**  `alternatingSplit_neg`, `symmetricSplit_pos`,
`alternating_eq_neg_symmetric` and `splits_sum_zero` are all correct and are used
downstream: they are what make the equal-weight sym/alt channel average vanish
identically (`MarkovCrossingReversal.channelAverage_eq_zero'`, against the
`w_sym = w_alt` of `docs/audits/2026-06-17-hecke-channel-chirality-binding.md`).
Read the theorems below as statements about the two one-dimensional channels —
which is all they ever were — and not as a claim about what the block asserts.

**Conditional on an identification the block does not make.**  That `δ`'s
numerator *is* the `k = 2` crossing reversal is a reading — the natural one given
the block derives its one exact result that way, but it is mine, not the block's,
which calls `(q−1)²(1−q⁻⁴)/3` "a structured near-match, not a derived closed
form".  Read the pair of outcomes rather than one: if the reading is right, the
stated channel points the wrong way; if it is wrong, the block owes an account of
where `h·[2]_q` comes from, since it is then not the reversal.

§7c: the main body is generic `Ring R` with `h` central — no ordering, no
`Real.sqrt`, no archimedean construct, and **no commutativity of the ambient
ring**, matching the 2026-09-03 strengthening of
`topological_flavor_split_of_central` (`H_n(q)` is not commutative for `n ≥ 3`;
`h = q − q⁻¹` is a scalar and so is central there).  Only a **left** inverse is
assumed; the quadratic upgrades it.  The closing `Archimedean` section — and only
that section — is over `ℝ`, because the sign statements use the ordering `1 < q`;
that is the archimedean side of the wall and is where it belongs.  Sorry-free
throughout.

-- Ref: [leitner2026] conj:flavor-split-habiro-derivation
-/
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Abel
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

namespace QOU.Hecke.CrossingReversalParity

variable {R : Type*} [Ring R] (σ σinv h : R)

/-- The mirror generator is `σ - h`: the quadratic upgrades a **left** inverse to
an explicit formula.  Same argument as
`QOU.FlavorSplit.topological_flavor_split_of_central`, reproved locally because
that declaration lives in a content-block sibling rather than a library module and
so cannot be imported. -/
theorem inv_eq (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) : σinv = σ - h := by
  have h1 : σ ^ 2 - h * σ = 1 := by rw [hq]; noncomm_ring
  calc σinv = σinv * 1 := by rw [mul_one]
    _ = σinv * (σ ^ 2 - h * σ) := by rw [h1]
    _ = (σinv * σ) * σ - (σinv * h) * σ := by noncomm_ring
    _ = (σinv * σ) * σ - (h * σinv) * σ := by rw [hcen σinv]
    _ = (σinv * σ) * σ - h * (σinv * σ) := by noncomm_ring
    _ = σ - h := by rw [hl]; noncomm_ring

/-- `σ - σ⁻¹ = h`: the odd cases collapse through this. -/
theorem sub_eq (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) : σ - σinv = h := by
  rw [inv_eq σ σinv h hcen hq hl]; noncomm_ring

/-- The **conjugate quadratic**: the mirror generator satisfies `σ⁻² = 1 - hσ⁻¹`.
This is what lets every power of `σ⁻¹` be reduced without any binomial expansion,
and it is where the alternating sign that produces the parity comes from. -/
theorem inv_quad (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) :
    σinv ^ 2 = 1 - h * σinv := by
  have hi := inv_eq σ σinv h hcen hq hl
  rw [hi]
  have hx : (σ - h) ^ 2 = σ ^ 2 - (h * σ + σ * h) + h ^ 2 := by noncomm_ring
  rw [hx, ← hcen σ, hq]
  noncomm_ring

/-- **The invariant.**  The resolvent `u = σ + σ⁻¹` squares to the central scalar
`h² + 4`.  This is what makes the parity work: every *even* power of `u` is
central, every odd one carries `σ`. -/
theorem resolvent_sq (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) :
    (σ + σinv) ^ 2 = h ^ 2 + 4 := by
  have hqi := inv_quad σ σinv h hcen hq hl
  have hs := sub_eq σ σinv h hcen hq hl
  have hprod : σ * σinv = 1 := by
    rw [inv_eq σ σinv h hcen hq hl]
    have e : σ * (σ - h) = σ ^ 2 - σ * h := by noncomm_ring
    rw [e, ← hcen σ, hq]; noncomm_ring
  have hprod' : σinv * σ = 1 := hl
  have e : (σ + σinv) ^ 2 = σ ^ 2 + σinv ^ 2 + (σ * σinv + σinv * σ) := by
    noncomm_ring
  rw [e, hq, hqi, hprod, hprod']
  have e2 : h * σ + 1 + (1 - h * σinv) + (1 + 1) = h * (σ - σinv) + 4 := by
    noncomm_ring; try simp; try abel; try noncomm_ring
  rw [e2, hs]
  noncomm_ring

/-! ## The even cases: a central multiple of the resolvent, never a scalar -/

/-- **`k = 2` is NOT central**: the square reversal is `h·u`, and `u = σ + σ⁻¹`
carries `σ`.  Contrast `σ³ − σ⁻³ = h(h² + 3)`. -/
theorem reversal_two (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) :
    σ ^ 2 - σinv ^ 2 = h * (σ + σinv) := by
  rw [hq, inv_quad σ σinv h hcen hq hl]; noncomm_ring

/-- **The obstruction.**  If the `k = 2` reversal equals an element `z`, then
`h·u = z`.  So when `h` is invertible, a *central* value at `k = 2` forces the
resolvent `u = σ + σ⁻¹` — hence `σ` itself — to be central.  In `H_n(q)` with
`n ≥ 3` the generators do not commute, so `σ` is not central and the square
reversal is not a scalar.  This is what the `k = 2` route into `δ` has to get
past, and it is the step `conj:flavor-split-habiro-derivation` does not supply. -/
theorem reversal_two_forces_resolvent_central (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) (hinv : R)
    (hhinv : hinv * h = 1) (z : R) (hz : σ ^ 2 - σinv ^ 2 = z) :
    σ + σinv = hinv * z := by
  rw [reversal_two σ σinv h hcen hq hl] at hz
  calc σ + σinv = 1 * (σ + σinv) := by rw [one_mul]
    _ = (hinv * h) * (σ + σinv) := by rw [hhinv]
    _ = hinv * (h * (σ + σinv)) := by noncomm_ring
    _ = hinv * z := by rw [hz]

/-- **`k = 4` has the same shape** — `h(h²+2)·u`, still carrying `σ`.  So the
failure at `k = 2` is parity, not a small-exponent accident. -/
theorem reversal_four (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) :
    σ ^ 4 - σinv ^ 4 = h * (h ^ 2 + 1 + 1) * (σ + σinv) := by
  have hqi := inv_quad σ σinv h hcen hq hl
  have h3 : σ ^ 3 = (h ^ 2 + 1) * σ + h := by
    have e : σ ^ 3 = σ ^ 2 * σ := by noncomm_ring
    rw [e, hq]
    have e2 : (h * σ + 1) * σ = h * σ ^ 2 + σ := by noncomm_ring
    rw [e2, hq]; noncomm_ring
  have h4 : σ ^ 4 = (h ^ 3 + h + h) * σ + (h ^ 2 + 1) := by
    have e : σ ^ 4 = σ ^ 3 * σ := by noncomm_ring
    rw [e, h3]
    have e2 : ((h ^ 2 + 1) * σ + h) * σ = (h ^ 2 + 1) * σ ^ 2 + h * σ := by noncomm_ring
    rw [e2, hq]; noncomm_ring
  have i3 : σinv ^ 3 = (h ^ 2 + 1) * σinv - h := by
    have e : σinv ^ 3 = σinv ^ 2 * σinv := by noncomm_ring
    rw [e, hqi]
    have e2 : (1 - h * σinv) * σinv = σinv - h * σinv ^ 2 := by noncomm_ring
    rw [e2, hqi]; noncomm_ring
  have i4 : σinv ^ 4 = -((h ^ 3 + h + h) * σinv) + (h ^ 2 + 1) := by
    have e : σinv ^ 4 = σinv ^ 3 * σinv := by noncomm_ring
    rw [e, i3]
    have e2 : ((h ^ 2 + 1) * σinv - h) * σinv = (h ^ 2 + 1) * σinv ^ 2 - h * σinv := by
      noncomm_ring
    rw [e2, hqi]; noncomm_ring
  rw [h4, i4]; noncomm_ring

/-! ## The odd case beyond `k = 3`: still a scalar -/

/-- **`k = 5` IS central**, at `h(h⁴ + 5h² + 5)` — the odd case one step past the
`k = 3` result the corpus already carries, which is what shows `k = 3`'s
centrality is a parity rather than a coincidence. -/
theorem reversal_five (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) :
    σ ^ 5 - σinv ^ 5 = h * (h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + h ^ 2 + h ^ 2 + 1 + 1 + 1 + 1 + 1) := by
  have hqi := inv_quad σ σinv h hcen hq hl
  have hs := sub_eq σ σinv h hcen hq hl
  have h3 : σ ^ 3 = (h ^ 2 + 1) * σ + h := by
    have e : σ ^ 3 = σ ^ 2 * σ := by noncomm_ring
    rw [e, hq]
    have e2 : (h * σ + 1) * σ = h * σ ^ 2 + σ := by noncomm_ring
    rw [e2, hq]; noncomm_ring
  have h4 : σ ^ 4 = (h ^ 3 + h + h) * σ + (h ^ 2 + 1) := by
    have e : σ ^ 4 = σ ^ 3 * σ := by noncomm_ring
    rw [e, h3]
    have e2 : ((h ^ 2 + 1) * σ + h) * σ = (h ^ 2 + 1) * σ ^ 2 + h * σ := by noncomm_ring
    rw [e2, hq]; noncomm_ring
  have h5 : σ ^ 5 = (h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + 1) * σ + (h ^ 3 + h + h) := by
    have e : σ ^ 5 = σ ^ 4 * σ := by noncomm_ring
    rw [e, h4]
    have e2 : ((h ^ 3 + h + h) * σ + (h ^ 2 + 1)) * σ
        = (h ^ 3 + h + h) * σ ^ 2 + (h ^ 2 + 1) * σ := by noncomm_ring
    rw [e2, hq]; noncomm_ring
  have i3 : σinv ^ 3 = (h ^ 2 + 1) * σinv - h := by
    have e : σinv ^ 3 = σinv ^ 2 * σinv := by noncomm_ring
    rw [e, hqi]
    have e2 : (1 - h * σinv) * σinv = σinv - h * σinv ^ 2 := by noncomm_ring
    rw [e2, hqi]; noncomm_ring
  have i4 : σinv ^ 4 = -((h ^ 3 + h + h) * σinv) + (h ^ 2 + 1) := by
    have e : σinv ^ 4 = σinv ^ 3 * σinv := by noncomm_ring
    rw [e, i3]
    have e2 : ((h ^ 2 + 1) * σinv - h) * σinv = (h ^ 2 + 1) * σinv ^ 2 - h * σinv := by
      noncomm_ring
    rw [e2, hqi]; noncomm_ring
  have i5 : σinv ^ 5 = (h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + 1) * σinv - (h ^ 3 + h + h) := by
    have e : σinv ^ 5 = σinv ^ 4 * σinv := by noncomm_ring
    rw [e, i4]
    have e2 : (-((h ^ 3 + h + h) * σinv) + (h ^ 2 + 1)) * σinv
        = -((h ^ 3 + h + h) * σinv ^ 2) + (h ^ 2 + 1) * σinv := by noncomm_ring
    rw [e2, hqi]; noncomm_ring
  rw [h5, i5]
  have e : (h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + 1) * σ + (h ^ 3 + h + h)
      - ((h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + 1) * σinv - (h ^ 3 + h + h))
      = (h ^ 4 + h ^ 2 + h ^ 2 + h ^ 2 + 1) * (σ - σinv) + ((h ^ 3 + h + h) + (h ^ 3 + h + h)) := by noncomm_ring
  rw [e, hs]; noncomm_ring

/-! ## The recursion the parity rides on -/

/-- `D_{k+2} = u·D_{k+1} − D_k` with `u = σ + σ⁻¹`.  Together with
`resolvent_sq` (`u² = h² + 4` central) this is the general mechanism: `D_k` is `h`
times a Chebyshev polynomial in `u` of degree `k−1`, carrying only powers of `u`
congruent to `k−1` mod 2.  The general-`k` conclusion is **not** formalised here —
see the probe named in the header. -/
theorem reversal_rec (hcen : ∀ x : R, h * x = x * h)
    (hq : σ ^ 2 = h * σ + 1) (hl : σinv * σ = 1) (k : ℕ) :
    σ ^ (k + 2) - σinv ^ (k + 2)
      = (σ + σinv) * (σ ^ (k + 1) - σinv ^ (k + 1)) - (σ ^ k - σinv ^ k) := by
  have hprod : σ * σinv = 1 := by
    rw [inv_eq σ σinv h hcen hq hl]
    have e : σ * (σ - h) = σ ^ 2 - σ * h := by noncomm_ring
    rw [e, ← hcen σ, hq]; noncomm_ring
  have hcomm : σ * σinv = σinv * σ := by rw [hprod, hl]
  have e1 : σ * σinv ^ (k + 1) = σinv ^ k := by
    have : σinv ^ (k + 1) = σinv * σinv ^ k := pow_succ' σinv k
    rw [this, ← mul_assoc, hprod, one_mul]
  have e2 : σinv * σ ^ (k + 1) = σ ^ k := by
    have : σ ^ (k + 1) = σ * σ ^ k := pow_succ' σ k
    rw [this, ← mul_assoc, hl, one_mul]
  have expand : (σ + σinv) * (σ ^ (k + 1) - σinv ^ (k + 1))
      = σ ^ (k + 2) - σ * σinv ^ (k + 1) + σinv * σ ^ (k + 1) - σinv ^ (k + 2) := by
    have a : σ * σ ^ (k + 1) = σ ^ (k + 2) := (pow_succ' σ (k + 1)).symm
    have b : σinv * σinv ^ (k + 1) = σinv ^ (k + 2) := (pow_succ' σinv (k + 1)).symm
    calc (σ + σinv) * (σ ^ (k + 1) - σinv ^ (k + 1))
        = σ * σ ^ (k + 1) - σ * σinv ^ (k + 1) + σinv * σ ^ (k + 1)
          - σinv * σinv ^ (k + 1) := by noncomm_ring
      _ = σ ^ (k + 2) - σ * σinv ^ (k + 1) + σinv * σ ^ (k + 1) - σinv ^ (k + 2) := by
            rw [a, b]
  rw [expand, e1, e2]
  noncomm_ring

/-! ## The archimedean specialisation: the two channel values, and their signs

§7c: this section — and only this section — is over `ℝ`, because it uses the
ordering (`1 < q`).  Everything above is generic.

**The point** — corrected 2026-09-13; see the 🛑 retraction in the file header.
These are statements about the two **one-dimensional** representations of the
Hecke algebra, `σ ↦ q` (symmetric, trivial) and `σ ↦ −q⁻¹` (alternating, sign),
and that is all they have ever been.  The `k = 2` reversal evaluates on them to
exact negatives (`alternating_eq_neg_symmetric`), so the symmetric one is
positive and the alternating one negative for every `q > 1`.

They are **not** a claim about what `conj:flavor-split-habiro-derivation`
asserts.  An earlier version of this paragraph read the block's "the weak
interaction is strictly left-handed, so it projects onto the fully alternating
channel of `H₄`" as its channel choice *for the flavour split*.  It is the
block's channel choice for the **residual**, the 0.128 % refinement, not for the
baseline.  Retracted in full in the header.

**Where these two theorems are actually used.**  `splits_sum_zero` is what makes
the equal-weight symmetric/alternating channel average vanish identically, given
the corpus's own `w_sym = w_alt = q²/(q⁴+4q²+1)`
(`docs/audits/2026-06-17-hecke-channel-chirality-binding.md`).  That excludes the
averaged reading of the split — scope (b), invariant = the weight equality plus
the exact negation — and is stated as
`MarkovCrossingReversal.channelAverage_eq_zero'`.

**The identification is still mine, not the block's.**  That `δ`'s numerator *is*
the `k = 2` crossing reversal is a reading; the block calls `(q−1)²(1−q⁻⁴)/3` "a
structured near-match, not a derived closed form".  What changed is that the
reading now has a *trace* behind it rather than a channel:
`tr_z(σ²−σ⁻²) = 2hz − h²` reproduces that expression exactly at the augmentation
`z = q` (`MarkovCrossingReversal.baselineX_eq_augmentation_trace`).
-/

section Archimedean

/-- The `k = 2` reversal evaluated on the **symmetric** eigenvalue `σ ↦ q`. -/
noncomputable def symmetricValue (q : ℝ) : ℝ := q ^ 2 - (q ^ 2)⁻¹

/-- The `k = 2` reversal evaluated on the **alternating** (sign) eigenvalue
`σ ↦ −q⁻¹` — the channel `conj:flavor-split-habiro-derivation` selects. -/
noncomputable def alternatingValue (q : ℝ) : ℝ := (q ^ 2)⁻¹ - q ^ 2

/-- The two channels differ by a sign and nothing else: same magnitude. -/
theorem alternating_eq_neg_symmetric (q : ℝ) :
    alternatingValue q = -symmetricValue q := by
  unfold alternatingValue symmetricValue; ring

/-- On the substrate branch `1 < q` the symmetric value is positive. -/
theorem symmetricValue_pos {q : ℝ} (hq : 1 < q) : 0 < symmetricValue q := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have h2 : (1:ℝ) < q ^ 2 := by nlinarith
  have hpos : (0:ℝ) < q ^ 2 := by positivity
  have : (q ^ 2)⁻¹ < 1 := by
    rw [inv_lt_one_iff₀]; right; exact h2
  unfold symmetricValue; linarith

/-- **The flavour split is the symmetric-channel value**, exactly:
`δ = ℏ_q²·(q² − q⁻²)/3` with `ℏ_q = 1 − q⁻¹`.  Same identity the probe checks
symbolically; here so the sign statement below has something to be about. -/
theorem flavourSplit_eq_hbarSq_symmetric_div_three {q : ℝ} (hq : q ≠ 0) :
    (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3 = (1 - q⁻¹) ^ 2 * symmetricValue q / 3 := by
  unfold symmetricValue
  field_simp

/-- The split built from the symmetric channel. -/
noncomputable def symmetricSplit (q : ℝ) : ℝ := (1 - q⁻¹) ^ 2 * symmetricValue q / 3

/-- The split built from the **alternating** (sign) one-dimensional channel
`σ ↦ −q⁻¹`.  (Earlier docstring: "the one the conjecture's own left-handedness
argument selects" — retracted, see the file header; the block selects that
channel for its *residual*, not for the split.) -/
noncomputable def alternatingSplit (q : ℝ) : ℝ :=
  (1 - q⁻¹) ^ 2 * alternatingValue q / 3

/-- **The alternating channel gives the split negative**: `alternatingSplit q < 0`
for every `1 < q`, i.e. a neutron *lighter* than the proton, where
`δ = (m_n − m_p)/M_N` is positive.  With `symmetricSplit_pos` this is what makes
`splits_sum_zero` bite: the two one-dimensional channels cancel under the
corpus's equal weights `w_sym = w_alt`.  Conditional on the identification
described in the section header, which is not the block's. -/
theorem alternatingSplit_neg {q : ℝ} (hq : 1 < q) : alternatingSplit q < 0 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hs : 0 < symmetricValue q := symmetricValue_pos hq
  have hne : q ≠ 0 := ne_of_gt hq0
  have hlt : q⁻¹ < 1 := by rw [inv_lt_one_iff₀]; right; exact hq
  have hhb : 0 < (1 - q⁻¹) ^ 2 := pow_pos (by linarith) 2
  unfold alternatingSplit
  rw [alternating_eq_neg_symmetric]
  nlinarith [mul_pos hhb hs]

/-- And the symmetric channel gives it with the right sign. -/
theorem symmetricSplit_pos {q : ℝ} (hq : 1 < q) : 0 < symmetricSplit q := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  have hs : 0 < symmetricValue q := symmetricValue_pos hq
  have hlt : q⁻¹ < 1 := by rw [inv_lt_one_iff₀]; right; exact hq
  have hhb : 0 < (1 - q⁻¹) ^ 2 := pow_pos (by linarith) 2
  unfold symmetricSplit
  exact div_pos (mul_pos hhb hs) (by norm_num)

/-- The two are exact negatives, so the channel choice is the whole content: the
magnitude is settled and only the sign is at stake. -/
theorem splits_sum_zero (q : ℝ) : symmetricSplit q + alternatingSplit q = 0 := by
  unfold symmetricSplit alternatingSplit
  rw [alternating_eq_neg_symmetric]; ring

end Archimedean

end QOU.Hecke.CrossingReversalParity
