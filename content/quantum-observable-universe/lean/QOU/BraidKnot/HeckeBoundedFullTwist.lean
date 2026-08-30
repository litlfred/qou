import QOU.BraidKnot.HeckeBoundedJucysMurphy
import QOU.BraidKnot.HeckeFullTwistProduct

/-!
# `∏ Lᵢ = Δ²` on the bounded presentation

The engine of `HeckeFullTwistProduct.lean` — the push law, the power identity, and
`jmProd_eq_delta_pow` — ported onto `HeckeGeneratorsBelow`.

## The bounds, and where they come from

`delta k = σ₀⋯σ_{k−1}` needs `k < n`; `run b k = σ_{b+k−1}⋯σ_b` needs `b + k < n`.  Tracing which
relation each lemma actually invokes gives:

| lemma | relation used | bound |
|---|---|---|
| `runB_peel_bot` | **none** | — |
| `sigma_comm_runB` | `far (b+i) j` | `j + 1 < n` |
| `sigma_comm_deltaB` | `far i j` | `j + 1 < n` |
| `core_braid_pushB` | `far b (m+1)`, `braid m` | `m + 2 < n` |
| `runB_push` | the three above, at `p + 1 = m` | `m + 1 < n` |
| `deltaB_pow_run` | `runB_push` | `m + 1 < n` |
| `jmRawB_eq_run_mul_delta` | **none** | — |
| `jmProdB_eq_deltaB_pow` | `deltaB_twist_step` | `k < n` |

Two of the eight need no bound at all: they are pure consequences of the `run` / `delta` / `jmRaw`
recursions, with no Hecke, braid or far relation anywhere.  So the bound bookkeeping is confined to
the relation-using half, which is why the port is tractable rather than a rewrite.

The load-bearing arithmetic is that `run_push`'s induction reaches index `p + 1 = m`, and the braid
relation at `m` needs `m + 2 < n` — hence the uniform `m + 1 < n` on the two big inductions rather
than the `m < n` a naive reading of "`delta m` is a word in `σ₀…σ_{m−1}`" would suggest.

## Recovery

As in `HeckeBoundedJucysMurphy.lean`, each ported result is followed by the recovery of its
unbounded counterpart through `HeckeGenerators.toBelow`, so the port strictly generalizes.
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-! ## §1  Runs and ascending words -/

/-- **Ascending run** `deltaB k = σ₀ σ₁ ⋯ σ_{k−1}`. -/
def deltaB (H : HeckeGeneratorsBelow R A q n) : ℕ → A
  | 0 => 1
  | (k + 1) => deltaB H k * H.σ k

/-- **Descending run** `runB b k = σ_{b+k−1} ⋯ σ_b`. -/
def runB (H : HeckeGeneratorsBelow R A q n) (b : ℕ) : ℕ → A
  | 0 => 1
  | (k + 1) => H.σ (b + k) * runB H b k

@[simp] theorem deltaB_zero (H : HeckeGeneratorsBelow R A q n) : deltaB H 0 = 1 := rfl

theorem deltaB_succ (H : HeckeGeneratorsBelow R A q n) (k : ℕ) :
    deltaB H (k + 1) = deltaB H k * H.σ k := rfl

@[simp] theorem runB_zero (H : HeckeGeneratorsBelow R A q n) (b : ℕ) : runB H b 0 = 1 := rfl

theorem runB_succ (H : HeckeGeneratorsBelow R A q n) (b k : ℕ) :
    runB H b (k + 1) = H.σ (b + k) * runB H b k := rfl

@[simp] theorem deltaB_toBelow (H : HeckeGenerators R A q) (n : ℕ) :
    ∀ k, deltaB (H.toBelow n) k = delta H k
  | 0 => rfl
  | (k + 1) => by rw [deltaB_succ, delta_succ, deltaB_toBelow H n k, toBelow_σ]

@[simp] theorem runB_toBelow (H : HeckeGenerators R A q) (n b : ℕ) :
    ∀ k, runB (H.toBelow n) b k = run H b k
  | 0 => rfl
  | (k + 1) => by rw [runB_succ, run_succ, runB_toBelow H n b k, toBelow_σ]

/-- Peeling the run from the bottom.  **No relation is used** — this is the recursion alone, so no
index bound is required. -/
theorem runB_peel_bot (H : HeckeGeneratorsBelow R A q n) (b : ℕ) :
    ∀ k : ℕ, runB H b (k + 1) = runB H (b + 1) k * H.σ b := by
  intro k
  induction k generalizing b with
  | zero => simp [runB]
  | succ i ih =>
      rw [runB_succ, ih, runB_succ]
      have e : b + 1 + i = b + (i + 1) := by omega
      rw [e, mul_assoc]

/-! ## §2  Commutation -/

/-- `σⱼ` commutes with a descending run sitting `≥ 2` below it.  Needs `σⱼ` to be a generator. -/
theorem sigma_comm_runB (H : HeckeGeneratorsBelow R A q n) (b j : ℕ) (hjn : j + 1 < n) :
    ∀ k : ℕ, b + k < j → H.σ j * runB H b k = runB H b k * H.σ j := by
  intro k
  induction k with
  | zero => simp
  | succ i ih =>
      intro h
      have hfar : H.σ (b + i) * H.σ j = H.σ j * H.σ (b + i) :=
        H.far (b + i) j (by omega) hjn
      have hih := ih (by omega)
      rw [runB_succ]
      calc H.σ j * (H.σ (b + i) * runB H b i)
          = (H.σ j * H.σ (b + i)) * runB H b i := by noncomm_ring
        _ = (H.σ (b + i) * H.σ j) * runB H b i := by rw [hfar]
        _ = H.σ (b + i) * (H.σ j * runB H b i) := by noncomm_ring
        _ = H.σ (b + i) * (runB H b i * H.σ j) := by rw [hih]
        _ = _ := by noncomm_ring

/-- `σⱼ` commutes with `deltaB m` when `m < j`.  Needs `σⱼ` to be a generator. -/
theorem sigma_comm_deltaB (H : HeckeGeneratorsBelow R A q n) (j : ℕ) (hjn : j + 1 < n) :
    ∀ m : ℕ, m < j → H.σ j * deltaB H m = deltaB H m * H.σ j := by
  intro m
  induction m with
  | zero => simp
  | succ i ih =>
      intro h
      have hfar : H.σ i * H.σ j = H.σ j * H.σ i := H.far i j (by omega) hjn
      have hih := ih (by omega)
      rw [deltaB_succ]
      calc H.σ j * (deltaB H i * H.σ i)
          = (H.σ j * deltaB H i) * H.σ i := by noncomm_ring
        _ = (deltaB H i * H.σ j) * H.σ i := by rw [hih]
        _ = deltaB H i * (H.σ j * H.σ i) := by noncomm_ring
        _ = deltaB H i * (H.σ i * H.σ j) := by rw [← hfar]
        _ = _ := by noncomm_ring

/-- The push law's core braid step.  Uses `far b (m+1)` and `braid m`, both needing `m + 2 < n`. -/
theorem core_braid_pushB (H : HeckeGeneratorsBelow R A q n) (b m : ℕ) (hbm : b < m)
    (hmn : m + 2 < n) (r : A) (hr : H.σ (m + 1) * r = r * H.σ (m + 1)) :
    H.σ (m + 1) * (H.σ m * r) * H.σ b * H.σ (m + 1)
      = H.σ m * (H.σ (m + 1) * (H.σ m * r)) * H.σ b := by
  have hbf : H.σ b * H.σ (m + 1) = H.σ (m + 1) * H.σ b :=
    H.far b (m + 1) (by omega) (by omega)
  have hbr : H.σ m * H.σ (m + 1) * H.σ m = H.σ (m + 1) * H.σ m * H.σ (m + 1) :=
    H.braid m (by omega)
  calc H.σ (m + 1) * (H.σ m * r) * H.σ b * H.σ (m + 1)
      = H.σ (m + 1) * H.σ m * r * (H.σ b * H.σ (m + 1)) := by noncomm_ring
    _ = H.σ (m + 1) * H.σ m * r * (H.σ (m + 1) * H.σ b) := by rw [hbf]
    _ = H.σ (m + 1) * H.σ m * (r * H.σ (m + 1)) * H.σ b := by noncomm_ring
    _ = H.σ (m + 1) * H.σ m * (H.σ (m + 1) * r) * H.σ b := by rw [← hr]
    _ = (H.σ (m + 1) * H.σ m * H.σ (m + 1)) * r * H.σ b := by noncomm_ring
    _ = (H.σ m * H.σ (m + 1) * H.σ m) * r * H.σ b := by rw [← hbr]
    _ = _ := by noncomm_ring

/-! ## §3  The push law and the power identity -/

/-- **The push law**, bounded.  The induction reaches index `p + 1 = m`, and the braid relation
there needs `m + 2 < n`; hence the hypothesis `m + 1 < n`. -/
theorem runB_push (H : HeckeGeneratorsBelow R A q n) : ∀ (j b m : ℕ), m = b + j → m + 1 < n →
    runB H (b + 1) j * deltaB H m * H.σ m
      = deltaB H m * runB H (b + 1) j * H.σ b := by
  intro j
  induction j with
  | zero => intro b m hm _; subst hm; simp
  | succ i ih =>
      intro b m hm hmn
      obtain ⟨p, hp, hpb⟩ : ∃ p, m = p + 1 ∧ p = b + i := ⟨b + i, by omega, rfl⟩
      subst hp
      have hrun : runB H (b + 1) (i + 1) = H.σ (p + 1) * runB H (b + 1) i := by
        rw [runB_succ]; congr 2; omega
      have hd : deltaB H (p + 1) = deltaB H p * H.σ p := deltaB_succ H p
      have hdc : H.σ (p + 1) * deltaB H p = deltaB H p * H.σ (p + 1) :=
        sigma_comm_deltaB H (p + 1) (by omega) p (by omega)
      have hih : runB H (b + 1) i * deltaB H p * H.σ p
          = deltaB H p * runB H (b + 1) i * H.σ b := ih b p hpb (by omega)
      have hcore : H.σ (p + 1) * runB H (b + 1) i * H.σ b * H.σ (p + 1)
          = H.σ p * (H.σ (p + 1) * runB H (b + 1) i) * H.σ b := by
        cases i with
        | zero =>
            have hbp : b = p := by omega
            subst hbp
            have hb : H.σ b * H.σ (b + 1) * H.σ b
                = H.σ (b + 1) * H.σ b * H.σ (b + 1) := H.braid b (by omega)
            simp only [runB_zero, mul_one]
            rw [← hb]
        | succ l =>
            have hp2 : runB H (b + 1) (l + 1) = H.σ p * runB H (b + 1) l := by
              rw [runB_succ]; congr 2; omega
            have hr : H.σ (p + 1) * runB H (b + 1) l = runB H (b + 1) l * H.σ (p + 1) :=
              sigma_comm_runB H (b + 1) (p + 1) (by omega) l (by omega)
            rw [hp2]
            exact core_braid_pushB H b p (by omega) (by omega) (runB H (b + 1) l) hr
      rw [hrun, hd]
      calc H.σ (p + 1) * runB H (b + 1) i * (deltaB H p * H.σ p) * H.σ (p + 1)
          = H.σ (p + 1) * (runB H (b + 1) i * deltaB H p * H.σ p) * H.σ (p + 1) := by
            noncomm_ring
        _ = H.σ (p + 1) * (deltaB H p * runB H (b + 1) i * H.σ b) * H.σ (p + 1) := by rw [hih]
        _ = (H.σ (p + 1) * deltaB H p) * (runB H (b + 1) i * H.σ b * H.σ (p + 1)) := by
            noncomm_ring
        _ = (deltaB H p * H.σ (p + 1)) * (runB H (b + 1) i * H.σ b * H.σ (p + 1)) := by rw [hdc]
        _ = deltaB H p
              * (H.σ (p + 1) * runB H (b + 1) i * H.σ b * H.σ (p + 1)) := by noncomm_ring
        _ = deltaB H p
              * (H.σ p * (H.σ (p + 1) * runB H (b + 1) i) * H.σ b) := by rw [hcore]
        _ = _ := by noncomm_ring

/-- **The power identity**, bounded: `(deltaB m · σ_m)^{k+1} = (deltaB m)^{k+1} · runB b (k+1)`. -/
theorem deltaB_pow_run (H : HeckeGeneratorsBelow R A q n) :
    ∀ (k b m : ℕ), m = b + k → m + 1 < n →
      (deltaB H m * H.σ m) ^ (k + 1) = (deltaB H m) ^ (k + 1) * runB H b (k + 1) := by
  intro k
  induction k with
  | zero => intro b m hm _; subst hm; simp [runB_succ]
  | succ l ih =>
      intro b m hm hmn
      have hih := ih (b + 1) m (by omega) hmn
      have hpush := runB_push H (l + 1) b m hm hmn
      have hpeel : runB H b (l + 1 + 1) = runB H (b + 1) (l + 1) * H.σ b :=
        runB_peel_bot H b (l + 1)
      calc (deltaB H m * H.σ m) ^ (l + 1 + 1)
          = (deltaB H m * H.σ m) ^ (l + 1) * (deltaB H m * H.σ m) := by rw [pow_succ]
        _ = deltaB H m ^ (l + 1) * runB H (b + 1) (l + 1) * (deltaB H m * H.σ m) := by rw [hih]
        _ = deltaB H m ^ (l + 1) * (runB H (b + 1) (l + 1) * deltaB H m * H.σ m) := by
            noncomm_ring
        _ = deltaB H m ^ (l + 1) * (deltaB H m * runB H (b + 1) (l + 1) * H.σ b) := by rw [hpush]
        _ = (deltaB H m ^ (l + 1) * deltaB H m) * (runB H (b + 1) (l + 1) * H.σ b) := by
            noncomm_ring
        _ = deltaB H m ^ (l + 1 + 1) * runB H b (l + 1 + 1) := by rw [← pow_succ, ← hpeel]

/-- **The twist step**, bounded. -/
theorem deltaB_twist_step (H : HeckeGeneratorsBelow R A q n) (k : ℕ) (hk : k + 1 < n) :
    deltaB H (k + 1) ^ (k + 1) = deltaB H k ^ (k + 1) * runB H 0 (k + 1) := by
  have h := deltaB_pow_run H k 0 k (by omega) hk
  rw [← deltaB_succ] at h
  exact h

/-! ## §4  `∏ Lᵢ = Δ²` -/

/-- `Lₖ = runB 0 k · deltaB k`.  **No relation is used** — the recursion alone, so no bound. -/
theorem jmRawB_eq_run_mul_delta (H : HeckeGeneratorsBelow R A q n) (k : ℕ) :
    jmRawB H k = runB H 0 k * deltaB H k := by
  induction k with
  | zero => simp
  | succ i ih =>
      rw [jmRawB_succ, ih, runB_succ, deltaB_succ]
      simp only [Nat.zero_add]
      noncomm_ring

/-- The ordered product `L₀L₁⋯L_{k−1}`. -/
def jmProdB (H : HeckeGeneratorsBelow R A q n) : ℕ → A
  | 0 => 1
  | (k + 1) => jmProdB H k * jmRawB H k

theorem jmProdB_succ (H : HeckeGeneratorsBelow R A q n) (k : ℕ) :
    jmProdB H (k + 1) = jmProdB H k * jmRawB H k := rfl

/-- **`∏Lᵢ = Δ²` on the bounded presentation.**  `L₀⋯L_k = (deltaB k)^{k+1}`, the full twist of
`B_{k+1}`, for every `k < n`.

At `n = 3` this is `L₀L₁L₂ = (σ₀σ₁)³` — the `H₃(q)` case, now available on a presentation the
2-dimensional representation actually satisfies. -/
theorem jmProdB_eq_deltaB_pow (H : HeckeGeneratorsBelow R A q n) (k : ℕ) (hk : k < n) :
    jmProdB H (k + 1) = deltaB H k ^ (k + 1) := by
  induction k with
  | zero => simp [jmProdB]
  | succ m ih =>
      rw [jmProdB_succ, ih (by omega), jmRawB_eq_run_mul_delta]
      calc deltaB H m ^ (m + 1) * (runB H 0 (m + 1) * deltaB H (m + 1))
          = (deltaB H m ^ (m + 1) * runB H 0 (m + 1)) * deltaB H (m + 1) := by noncomm_ring
        _ = deltaB H (m + 1) ^ (m + 1) * deltaB H (m + 1) := by
            rw [← deltaB_twist_step H m (by omega)]
        _ = deltaB H (m + 1) ^ (m + 1 + 1) := (pow_succ _ _).symm

/-! ## §5  Recovery of the unbounded statements -/

@[simp] theorem jmProdB_toBelow (H : HeckeGenerators R A q) (n : ℕ) :
    ∀ k, jmProdB (H.toBelow n) k = jmProd H k
  | 0 => rfl
  | (k + 1) => by rw [jmProdB_succ, jmProd_succ, jmProdB_toBelow H n k, jmRawB_toBelow]

/-- Recovers `jmProd_eq_delta_pow` from the bounded form: take `n` past `k`. -/
theorem jmProd_eq_delta_pow_of_below (H : HeckeGenerators R A q) (k : ℕ) :
    jmProd H (k + 1) = delta H k ^ (k + 1) := by
  have := jmProdB_eq_deltaB_pow (H.toBelow (k + 1)) k (by omega)
  rwa [jmProdB_toBelow, deltaB_toBelow] at this

/-! ## §6  The payoff: the engine now runs on the 2-dimensional representation -/

section StdThree

variable {K : Type*} [Field K]

theorem stdTwoBelow3_deltaB_two (q : K) (hq : q ≠ 0) :
    deltaB (stdTwoBelow3 q hq) 2 = stdTwo0 q * stdTwo1 q := by
  rw [deltaB_succ, deltaB_succ, deltaB_zero, one_mul]
  rfl

/-- **What the port bought.**  `L₀L₁L₂ = (σ₀σ₁)³` — the full twist of `B₃` — holds on the
2-dimensional `(2,1)` representation of `H₃(q)`.

`HeckeStableScalarCascade.stdTwo_no_stable_extension` proves the *unbounded* presentation cannot
host this representation at all, so this instance of `∏Lᵢ = Δ²` is unreachable from
`jmProd_eq_delta_pow`.  It is exactly the content the bounded port adds. -/
theorem stdTwoBelow3_jmProd_eq_fullTwist (q : K) (hq : q ≠ 0) :
    jmProdB (stdTwoBelow3 q hq) 3 = (stdTwo0 q * stdTwo1 q) ^ 3 := by
  have h := jmProdB_eq_deltaB_pow (stdTwoBelow3 q hq) 2 (by omega)
  rwa [stdTwoBelow3_deltaB_two] at h

end StdThree

end QOU.BraidKnot.Hecke
