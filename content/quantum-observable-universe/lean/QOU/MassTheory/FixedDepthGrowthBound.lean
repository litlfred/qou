import Mathlib.Tactic
import Mathlib.Analysis.SpecificLimits.Basic
import QOU.MassTheory.BodyOrderRecurrenceDepth

/-!
# A fixed-depth recurrence grows at most geometrically — so not factorially

`prop:prolonged-periods-fixed-depth` derives, by Cayley–Hamilton on the
jet-prolongation operator acting on a finite-rank Gauss–Manin space, that the
prolonged Seiberg–Witten periods satisfy

    a^(n+d) = ∑_{j<d} c_j · a^(n+j)   for every `n`,   with **`n`-independent** kernel `c`.

A separate corpus line (`QOU/Mass/SWPeriodSuperExponential.lean`, PR #6052) proves
sorry-free that the same periods, read at `q = 1` as `I(n)/n` via
`prop:sw-classical-jet-exactness`, grow **at least factorially**:
`factorial_le_involution_two_mul : n ! ≤ I (2n)`.

This file shows the two are incompatible, and does so at the level where the
incompatibility actually lives.

## The bound

`abs_le_geometric` — a sequence satisfying a depth-`d` recurrence with constant
kernel obeys `|a n| ≤ M · Kⁿ`, where `M` bounds the `d` initial terms and
`K ≥ max(1, ∑_{j<d} |c_j|)`. Elementary strong induction: the recurrence can
multiply the running bound by at most `∑|c_j|` per step.

## The incompatibility

`not_factorial_growth` — no such sequence can satisfy `(Nat.factorial n : ℝ) ≤ a (2n)` for
all `n`. Via `tendsto_pow_div_factorial_atTop`, `x ⁿ / n !` → 0, so the factorial
outruns every geometric and the two bounds cross.

## A correction to how this was first stated

The first write-up of this argument (bean `qou-9yqb`) said the *unbounded
two-step ratio* (`involution_ratio_unbounded`) is what contradicts the geometric
bound. **That is too quick, and it is wrong as stated.** A geometric *upper*
bound does not by itself forbid unbounded ratios: a sequence may dip far below
`Kⁿ` at some `n` and jump back, making `a(n+2)/a(n)` arbitrarily large while
never exceeding `M·Kⁿ`. Ruling that out needs a lower bound as well.

The **factorial** statement is a genuine lower bound and does contradict the
geometric one. So the incompatibility is real, but it rests on
`factorial_le_involution_two_mul`, not on `involution_ratio_unbounded`. This file
proves the version that survives.

## What this does and does not settle

It does **not** say which premise is false. One of these must go:

* the identification `a_D^(n) = I(n)/n` (`prop:sw-classical-jet-exactness`) —
  which PR #6052's own docstring records as resting on `∑_{λ⊢n} f^λ = I(n)`,
  **open** in the corpus (beans `qou-m3xr`, `qou-jlam`);
* that `a_D^(n) = φ(Mⁿ v₀)` for a *fixed finite-rank* `M`
  (`prop:mi-sw-abelianisation`) — a super-exponential sequence cannot be the
  orbit of one, whatever the rank;
* the `n`-independence of the kernel. Note the involution recurrence
  `I(n+2) = I(n+1) + (n+1)·I(n)` *is* depth 2 with an `n`-**dependent**
  coefficient, which is consistent with everything here and inconsistent with
  the proposition.

This is the second independent crack in `prop:prolonged-periods-fixed-depth`.
The first is `BodyOrderRecurrenceDepth.no_equivariant_prolongation`, which
reaches the same "something must give" from S₅-equivariance and Schur rather
than from growth.

Base ring: `ℝ`, and the archimedean setting is genuinely required — the content
is an order/limit statement (AGENTS.md §7c).
-/

namespace QOU.MassTheory.FixedDepthGrowthBound

open QOU.MassTheory.BodyOrderRecurrenceDepth

variable {d : ℕ} {c a : ℕ → ℝ}

/-- **A constant-kernel recurrence grows at most geometrically.** `M` bounds the
`d` initial terms; `K` dominates both `1` and the kernel's ℓ¹ norm. -/
theorem abs_le_geometric (h : IsDepthRecurrence d c a) (hd : 0 < d)
    {K M : ℝ} (hK : 1 ≤ K) (hcK : ∑ j ∈ Finset.range d, |c j| ≤ K)
    (hM0 : 0 ≤ M) (hMinit : ∀ j, j < d → |a j| ≤ M) :
    ∀ n, |a n| ≤ M * K ^ n := by
  obtain ⟨e, rfl⟩ : ∃ e, d = e + 1 := ⟨d - 1, by omega⟩
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    by_cases hn : n < e + 1
    · calc |a n| ≤ M := hMinit n hn
        _ = M * 1 := (mul_one M).symm
        _ ≤ M * K ^ n := by
            exact mul_le_mul_of_nonneg_left (one_le_pow₀ hK) hM0
    · push_neg at hn
      obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
      have hrw : e + 1 + m = m + (e + 1) := by omega
      rw [hrw, h m]
      calc |∑ j ∈ Finset.range (e + 1), c j * a (m + j)|
          ≤ ∑ j ∈ Finset.range (e + 1), |c j * a (m + j)| :=
            Finset.abs_sum_le_sum_abs _ _
        _ = ∑ j ∈ Finset.range (e + 1), |c j| * |a (m + j)| := by
            simp [abs_mul]
        _ ≤ ∑ j ∈ Finset.range (e + 1), |c j| * (M * K ^ (m + e)) := by
            refine Finset.sum_le_sum fun j hj => ?_
            have hje : j ≤ e := by
              have := Finset.mem_range.mp hj; omega
            have hlt : m + j < e + 1 + m := by omega
            have h1 : |a (m + j)| ≤ M * K ^ (m + j) := ih (m + j) hlt
            have h2 : M * K ^ (m + j) ≤ M * K ^ (m + e) :=
              mul_le_mul_of_nonneg_left (pow_le_pow_right₀ hK (by omega)) hM0
            exact mul_le_mul_of_nonneg_left (h1.trans h2) (abs_nonneg _)
        _ = (∑ j ∈ Finset.range (e + 1), |c j|) * (M * K ^ (m + e)) := by
            rw [Finset.sum_mul]
        _ ≤ K * (M * K ^ (m + e)) := by
            refine mul_le_mul_of_nonneg_right hcK ?_
            have : (0:ℝ) ≤ K ^ (m + e) := pow_nonneg (by linarith) _
            positivity
        _ = M * K ^ (m + (e + 1)) := by ring

/-- **No constant-kernel recurrence grows factorially.** If `a` satisfies a
depth-`d` recurrence with `n`-independent kernel, it cannot also satisfy
`n ! ≤ a (2n)` for every `n`. -/
theorem not_factorial_growth (h : IsDepthRecurrence d c a) (hd : 0 < d)
    (hfac : ∀ n : ℕ, (Nat.factorial n : ℝ) ≤ a (2 * n)) : False := by
  set K : ℝ := max 1 (∑ j ∈ Finset.range d, |c j|) with hKdef
  set M : ℝ := max 0 (Finset.sup' (Finset.range d) ⟨0, Finset.mem_range.mpr hd⟩
      (fun j => |a j|)) with hMdef
  have hK : 1 ≤ K := le_max_left _ _
  have hcK : ∑ j ∈ Finset.range d, |c j| ≤ K := le_max_right _ _
  have hM0 : 0 ≤ M := le_max_left _ _
  have hMinit : ∀ j, j < d → |a j| ≤ M := fun j hj =>
    le_trans (Finset.le_sup' (fun j => |a j|) (Finset.mem_range.mpr hj)) (le_max_right _ _)
  have hbound := abs_le_geometric h hd hK hcK hM0 hMinit
  have hK0 : (0:ℝ) < K := lt_of_lt_of_le zero_lt_one hK
  -- `(K²)ⁿ / n!` is summable, so its terms tend to `0`: the factorial outruns
  -- every geometric.
  have hlim := (Real.summable_pow_div_factorial (K ^ 2)).tendsto_atTop_zero
  have hev : ∀ᶠ n : ℕ in Filter.atTop,
      (K ^ 2) ^ n / (Nat.factorial n : ℝ) < 1 / (M + 1) := by
    refine hlim.eventually (gt_mem_nhds ?_)
    positivity
  obtain ⟨n, hn⟩ := hev.exists
  have hfacpos : (0:ℝ) < (Nat.factorial n : ℝ) := by positivity
  have hpos : (0:ℝ) < (K ^ 2) ^ n := pow_pos (pow_pos hK0 2) n
  have hkey : (Nat.factorial n : ℝ) ≤ M * (K ^ 2) ^ n := by
    calc (Nat.factorial n : ℝ) ≤ a (2 * n) := hfac n
      _ ≤ M * K ^ (2 * n) := (le_abs_self _).trans (hbound (2 * n))
      _ = M * (K ^ 2) ^ n := by rw [← pow_mul, mul_comm 2 n]
  rw [div_lt_div_iff₀ hfacpos (by positivity)] at hn
  have hexp : (K ^ 2) ^ n * (M + 1) = M * (K ^ 2) ^ n + (K ^ 2) ^ n := by ring
  rw [hexp, one_mul] at hn
  linarith

end QOU.MassTheory.FixedDepthGrowthBound
