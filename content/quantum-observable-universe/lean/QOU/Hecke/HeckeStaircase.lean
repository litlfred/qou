import QOU.Hecke.HeckeTower

/-!
# QOU.Hecke.HeckeStaircase — the descending runs `σ_n σ_{n-1} ⋯ σ_{n-k+1}`

Second brick of the type-`A` spanning argument (bean `qou-twwf`).  The tower
decomposition `H_{n+1}(q) = Σ_k incl(H_n(q)) · c_k` needs three algebraic facts
about the runs `c_k`, and this file proves them.

## Why an ℕ-indexed generator layer

The runs are indexed by `n - k`, and every side condition is an inequality
between such indices.  Stated over `Fin (n+1)` those become `Fin.mk` juggling;
stated over `ℕ` they are `omega` calls.  So `gen m` is `σ_m` for `m ≤ n` and
junk (`1`) above, exactly as `QOU.Hecke.SymmetricCoxeter.gen` does for the
group side, and everything below is ℕ arithmetic.

## What is proved

* `stair_comm` — a generator strictly below the run commutes past the whole run.
* `stair_fold` — re-applying the run's last letter folds back:
  `c_{k+1} σ_{n-k} = (q-1)·c_{k+1} + q·c_k`.  This is where the quadratic
  relation enters, and it is the only place a coefficient appears.
* `stair_push` — a generator above the run's foot passes through with its index
  dropped by one: `c_k σ_i = σ_{i-1} c_k`.  Braid on one letter, commutation on
  the rest; the Hecke analogue of `SymmetricCoxeter.t_push`.  Its hypothesis is
  `n + 1 - k < i`, **not** `n - k + 1 < i`: the two agree for `k ≤ n` and differ
  at the full run, where the second is off by one against truncated subtraction.

Together with `c_k σ_{n-k} = c_{k+1}` (definitional) these are the four cases of
the closure argument.  **The closure itself, the submodule, and the induction on
`n` are not here.**
-/

namespace QOU.Hecke.IwahoriHecke

variable (K : Type*) [CommRing K] (q : K) (n : ℕ)

/-- `σ_m` for `m ≤ n`, and `1` above — an ℕ-indexed generator layer, so every
    side condition below is `omega`-shaped rather than `Fin`-shaped. -/
noncomputable def gen (m : ℕ) : IwahoriHecke K q (n + 1) :=
  if h : m < n + 1 then σ K q (n + 1) ⟨m, h⟩ else 1

theorem gen_eq_σ {m : ℕ} (h : m < n + 1) :
    gen K q n m = σ K q (n + 1) ⟨m, h⟩ := dif_pos h

/-- The quadratic relation, ℕ-indexed. -/
theorem gen_sq {m : ℕ} (hm : m ≤ n) :
    gen K q n m * gen K q n m = (q - 1) • gen K q n m + q • 1 := by
  rw [gen_eq_σ K q n (by omega)]
  exact σ_quadratic K q (n + 1) _

/-- The braid relation, ℕ-indexed. -/
theorem gen_braid {m : ℕ} (hm : m + 1 ≤ n) :
    gen K q n m * gen K q n (m + 1) * gen K q n m
      = gen K q n (m + 1) * gen K q n m * gen K q n (m + 1) := by
  rw [gen_eq_σ K q n (show m < n + 1 by omega),
    gen_eq_σ K q n (show m + 1 < n + 1 by omega)]
  have h := σ_braid K q (n + 1) (⟨m, by omega⟩ : Fin (n + 1)) (by simpa using hm)
  convert h using 3

/-- The commutation relation, ℕ-indexed. -/
theorem gen_comm {a b : ℕ} (ha : a ≤ n) (hab : b + 2 ≤ a) :
    gen K q n a * gen K q n b = gen K q n b * gen K q n a := by
  rw [gen_eq_σ K q n (show a < n + 1 by omega),
    gen_eq_σ K q n (show b < n + 1 by omega)]
  exact σ_commute K q (n + 1) _ _ (by simpa using hab)

/-- The descending run `c_k = σ_n σ_{n-1} ⋯ σ_{n-k+1}`. -/
noncomputable def stair : ℕ → IwahoriHecke K q (n + 1)
  | 0 => 1
  | (k + 1) => stair k * gen K q n (n - k)

@[simp] theorem stair_zero : stair K q n 0 = 1 := rfl

theorem stair_succ (k : ℕ) :
    stair K q n (k + 1) = stair K q n k * gen K q n (n - k) := rfl

/-- **A generator strictly below the run commutes past it.** -/
theorem stair_comm (k i : ℕ) (h : i + 2 ≤ n - k + 1) :
    stair K q n k * gen K q n i = gen K q n i * stair K q n k := by
  induction k with
  | zero => simp [stair_zero]
  | succ k ih =>
      have hik : i + 2 ≤ n - k := by omega
      rw [stair_succ, mul_assoc, gen_comm K q n (by omega) hik, ← mul_assoc,
        ih (by omega), mul_assoc]

/-- **Re-applying the run's last letter folds back**, at the cost of the only
    coefficient in the whole argument. -/
theorem stair_fold (k : ℕ) (hk : k ≤ n) :
    stair K q n (k + 1) * gen K q n (n - k)
      = (q - 1) • stair K q n (k + 1) + q • stair K q n k := by
  rw [stair_succ, mul_assoc, gen_sq K q n (by omega), mul_add, mul_smul_comm,
    mul_smul_comm, mul_one]

/-- **A generator above the run's foot passes through with its index dropped.**
    The Hecke analogue of `SymmetricCoxeter.t_push`.

    The foot of `c_k = σ_n ⋯ σ_{n-k+1}` is `σ_{n+1-k}`, and `n + 1 - k` is the
    right way to write it: `n - k + 1` agrees for `k ≤ n` but is **off by one at
    the full run** `k = n+1`, where truncated subtraction turns `n - (n+1) + 1`
    into `1` while the actual foot is `σ_0`.  That would silently exclude
    `i = 1` from the last case of the closure argument, where it is needed and
    where it is true — at `n = 1`, `c₂ σ₁ = σ₁σ₀σ₁ = σ₀σ₁σ₀ = σ₀ c₂`. -/
theorem stair_push (k : ℕ) (hk : k ≤ n + 1) : ∀ i : ℕ, i ≤ n → n + 1 - k < i →
    stair K q n k * gen K q n i = gen K q n (i - 1) * stair K q n k := by
  induction k with
  | zero => intro i hi h; omega
  | succ k ih =>
      intro i hi h
      rcases eq_or_lt_of_le (show n - k + 1 ≤ i by omega) with heq | hlt
      · -- `i = n - k + 1`: braid on the run's last letter, then commute the rest
        -- of the run past the new letter.  This case forces `k ≥ 1`.
        obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := by
          cases k with
          | zero => omega
          | succ k' => exact ⟨k', rfl⟩
        have hi1 : i = n - k' := by omega
        have hlast : n - (k' + 1) = n - k' - 1 := by omega
        subst hi1
        have hbr : gen K q n (n - k' - 1) * gen K q n (n - k')
              * gen K q n (n - k' - 1)
            = gen K q n (n - k') * gen K q n (n - k' - 1) * gen K q n (n - k') := by
          have h0 := gen_braid K q n (m := n - k' - 1) (by omega)
          rwa [show n - k' - 1 + 1 = n - k' by omega] at h0
        have hcm : stair K q n k' * gen K q n (n - k' - 1)
            = gen K q n (n - k' - 1) * stair K q n k' :=
          stair_comm K q n k' _ (by omega)
        rw [stair_succ, stair_succ, hlast]
        simp only [mul_assoc] at hbr ⊢
        rw [← hbr, ← mul_assoc, hcm, mul_assoc]
      · -- `i ≥ n - k + 2`: commute past the run's last letter, then induct.
        have hcom : gen K q n i * gen K q n (n - k)
            = gen K q n (n - k) * gen K q n i :=
          gen_comm K q n (by omega) (by omega)
        rw [stair_succ, mul_assoc, ← hcom, ← mul_assoc,
          ih (by omega) i hi (by omega), mul_assoc]

/-- **The full run, which is the case the old hypothesis missed.**  For
    `c_{n+1} = σ_n ⋯ σ_0` every generator except `σ_0` itself passes through.
    Stated separately because it is the instance the closure argument's last
    case needs, and the instance `n - k + 1 < i` would have excluded. -/
theorem stair_push_full (i : ℕ) (hi : i ≤ n) (h0 : 0 < i) :
    stair K q n (n + 1) * gen K q n i
      = gen K q n (i - 1) * stair K q n (n + 1) :=
  stair_push K q n (n + 1) le_rfl i hi (by omega)

/-- **The generators below the top one lie in the tower subalgebra.**  `gen m`
    for `m < n` is `incl (σ_m)`, so the whole closure argument's "commute past
    and absorb" cases land back in `(incl K q n).range`. -/
theorem gen_mem_inclRange {m : ℕ} (hm : m < n) :
    gen K q n m ∈ (incl K q n).range := by
  refine ⟨σ K q n ⟨m, hm⟩, ?_⟩
  show incl K q n (σ K q n ⟨m, hm⟩) = gen K q n m
  rw [incl_σ, gen_eq_σ K q n (by omega)]
  congr 1

end QOU.Hecke.IwahoriHecke
