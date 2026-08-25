import Mathlib.Tactic

/-!
# Parity-modulated geometric sequences — why a one-step ratio test lies

The mechanism behind bean `qou-64jx`. A `q`-Borel radius estimate for the C1
recurrence was read off the one-step ratio `c_{m+1}/c_m` at a single `m`, and
came out **branch-dependent at `3.7e-4`**. That was labelled "two nearby
singularities … consistent with the two-sector structure". It is not: the
parity-free estimator is branch-independent to `3.1e-25`
(`computations/qbeta/c3_w2_c1_parity_artifact.py`).

This file isolates the algebra that makes that happen, in a model with no
asymptotics in it. The numerics establish that the actual C1 Borel coefficients
fit this model to 25 digits; what is proved here is the model's behaviour, and
that is what explains the reading.

## The model

    parityGeom γ α β m = γ ^ m * (if Even m then α else β)

a geometric sequence whose amplitude is modulated by the parity of the index.
The two-step decoupling of a recurrence that couples `m` to `m + 2` produces
exactly this shape, with `α` and `β` fixed by the initial conditions — i.e.
**`α/β` is the branch datum**.

## What the three theorems say

* `twoStepRatio_eq` — the two-step ratio is `γ ^ 2`, **for every `m`, with no
  hypothesis relating `α` and `β`**. The branch datum cancels identically. This
  is why the parity-free estimator is branch-independent, and it is exact
  rather than asymptotic.
* `oneStepRatio_even` / `oneStepRatio_odd` — the one-step ratio is `γ * (β/α)`
  at even `m` and `γ * (α/β)` at odd `m`. So it is **2-periodic**, and each
  phase carries the branch datum. Sampling one parity therefore reports a
  branch-dependent number no matter how far out in `m` you go — the estimator
  is not converging slowly, it is converging to the wrong thing.
* `oneStepRatio_mul_eq` — the two phases multiply to `γ ^ 2`. The branch datum
  appears as `β/α` in one and `α/β` in the other and cancels in the product.
  This is the punchline: the geometric mean of the two phases recovers `γ`
  exactly, which is why that is the canonical repair rather than an ad-hoc one.

`oneStepRatio_ne_iff` records when the 2-cycle is visible at all: precisely
when `α ^ 2 ≠ β ^ 2`. At `α = ±β` the modulation is invisible to the one-step
ratio and no spurious branch-dependence appears — consistent with the observed
amplitude vanishing as the branch approaches that balance.

## Scope

This is a statement about `parityGeom`, not about the C1 recurrence. It does
**not** prove that the C1 Borel coefficients have this form; that is the
numerical finding, and it is recorded as such in the witness. What this file
does is remove any doubt about the *interpretation* of that finding: given the
shape, branch-dependence of the one-step ratio is forced and carries no
information about singularity count.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_parity_artifact.py
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-/

namespace QOU.QBeta.ParityRatio

variable {R : Type*} [Field R]

/-- A geometric sequence whose amplitude alternates with the parity of the
index: `α` on even indices, `β` on odd. The two-step decoupling of a recurrence
coupling `m` to `m + 2` produces this shape, with `α/β` fixed by the initial
conditions — so `α/β` is the *branch* datum. -/
def parityGeom (γ α β : R) (m : ℕ) : R :=
  γ ^ m * (if Even m then α else β)

@[simp] theorem parityGeom_even (γ α β : R) {m : ℕ} (h : Even m) :
    parityGeom γ α β m = γ ^ m * α := by
  unfold parityGeom; rw [if_pos h]

@[simp] theorem parityGeom_odd (γ α β : R) {m : ℕ} (h : ¬ Even m) :
    parityGeom γ α β m = γ ^ m * β := by
  unfold parityGeom; rw [if_neg h]

/-- **The two-step ratio is `γ ^ 2`, always.**

No hypothesis relates `α` and `β`: the branch datum cancels identically, at
every `m`, for both parities. This is the exact statement behind
"the parity-free radius is branch-independent" — and it is an identity, not a
limit. -/
theorem twoStepRatio_eq (γ α β : R) (hγ : γ ≠ 0) (hα : α ≠ 0) (hβ : β ≠ 0)
    (m : ℕ) :
    parityGeom γ α β (m + 2) / parityGeom γ α β m = γ ^ 2 := by
  have key : Even (m + 2) ↔ Even m := by simp [Nat.even_add]
  unfold parityGeom
  by_cases hm : Even m
  · rw [if_pos hm, if_pos (key.mpr hm), pow_add]
    field_simp
  · rw [if_neg hm, if_neg (fun hc => hm (key.mp hc)), pow_add]
    field_simp

/-- At **even** `m` the one-step ratio is `γ * (β/α)` — it carries the branch
datum. -/
theorem oneStepRatio_even (γ α β : R) (hγ : γ ≠ 0) (hα : α ≠ 0)
    {m : ℕ} (hm : Even m) :
    parityGeom γ α β (m + 1) / parityGeom γ α β m = γ * (β / α) := by
  have h1 : ¬ Even (m + 1) := by simp [Nat.even_add_one, hm]
  unfold parityGeom
  rw [if_pos hm, if_neg h1, pow_succ]
  field_simp

/-- At **odd** `m` the one-step ratio is `γ * (α/β)` — the same branch datum,
inverted. Together with `oneStepRatio_even` this is the 2-cycle. -/
theorem oneStepRatio_odd (γ α β : R) (hγ : γ ≠ 0) (hβ : β ≠ 0)
    {m : ℕ} (hm : ¬ Even m) :
    parityGeom γ α β (m + 1) / parityGeom γ α β m = γ * (α / β) := by
  have h1 : Even (m + 1) := by
    simpa [Nat.even_add_one] using hm
  unfold parityGeom
  rw [if_neg hm, if_pos h1, pow_succ]
  field_simp

/-- **The punchline.** The two phases of the one-step ratio multiply to `γ ^ 2`:
the branch datum enters one as `β/α` and the other as `α/β`, and cancels.

So the geometric mean of the two phases recovers `γ` exactly, for every branch.
That is why averaging the parities is the *canonical* repair of the estimator
rather than an ad-hoc patch — and why a single-parity sample cannot be fixed by
going to larger `m`. -/
theorem oneStepRatio_mul_eq (γ α β : R) (hα : α ≠ 0) (hβ : β ≠ 0) :
    (γ * (β / α)) * (γ * (α / β)) = γ ^ 2 := by
  field_simp

/-- The 2-cycle is **visible exactly when `α ^ 2 ≠ β ^ 2`.** At `α = ±β` the
modulation is invisible to the one-step ratio and no spurious branch-dependence
appears at all — the estimator is only misleading off that balance. -/
theorem oneStepRatio_eq_iff (γ α β : R) (hγ : γ ≠ 0) (hα : α ≠ 0) (hβ : β ≠ 0) :
    γ * (β / α) = γ * (α / β) ↔ α ^ 2 = β ^ 2 := by
  constructor
  · intro h
    have h1 : β / α = α / β := mul_left_cancel₀ hγ h
    field_simp at h1
    linear_combination -h1
  · intro h
    have h1 : β / α = α / β := by
      field_simp
      linear_combination -h
    rw [h1]

theorem oneStepRatio_ne_iff (γ α β : R) (hγ : γ ≠ 0) (hα : α ≠ 0) (hβ : β ≠ 0) :
    γ * (β / α) ≠ γ * (α / β) ↔ α ^ 2 ≠ β ^ 2 :=
  not_congr (oneStepRatio_eq_iff γ α β hγ hα hβ)

/-- **A one-step ratio that is constant in `m` forces the modulation away.**

Contrapositive of the above, and the sanity check on the whole diagnosis: if
the one-step ratio really had settled to a single branch-independent limit,
the parity amplitude would have to be trivial. Observing a stable 2-cycle is
therefore incompatible with "the estimator converged", however stable
consecutive same-parity samples look. -/
theorem oneStepRatio_const_imp (γ α β : R) (hγ : γ ≠ 0) (hα : α ≠ 0) (hβ : β ≠ 0)
    (h : γ * (β / α) = γ * (α / β)) : α ^ 2 = β ^ 2 := by
  by_contra hne
  exact (oneStepRatio_ne_iff γ α β hγ hα hβ).mpr hne h

end QOU.QBeta.ParityRatio
