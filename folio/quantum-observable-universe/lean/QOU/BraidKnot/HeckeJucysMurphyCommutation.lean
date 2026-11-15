import QOU.BraidKnot.HeckeJucysMurphyElements

/-!
# JM commutation relations, and where the general-`λ` derivation actually stops

`HeckeJucysMurphyElements.lean` split the `JucysMurphySpectrum` assumption into a **structural**
half and a **spectral** half, and proved the structural half at `n = 2, 3`.  This file pushes the
structural half further and — more importantly — locates precisely where the general-`λ`
derivation stops, so the remaining gap is one statement rather than a vague "seminormal form".

## The two exchange relations (proved, from the Hecke relation alone)

With `h := q − q⁻¹` and `L_{i+1} = σᵢ Lᵢ σᵢ`:

* `sigma_mul_jm_succ`  :  `σᵢ L_{i+1} = h L_{i+1} + Lᵢ σᵢ`
* `jm_succ_mul_sigma`  :  `L_{i+1} σᵢ = h L_{i+1} + σᵢ Lᵢ`

Each is one application of `σᵢ² = hσᵢ + 1`.  They are the engine for everything below.

## Consequences (proved)

* **`sigma_comm_add`** — `σᵢ` commutes with `Lᵢ + L_{i+1}`.  The two exchange relations differ by
  exactly the term that cancels in the sum.  This is the classical statement that `σᵢ` commutes with
  the *symmetric* functions of the adjacent JM pair, and it is the first genuinely general
  commutation fact in this corpus (the `n = 3` results were single instances).
* **`sigma_mul_jm_prod`** — `σᵢ (Lᵢ L_{i+1}) = (L_{i+1} Lᵢ) σᵢ`.  Note the **order swap on the
  right**: this is *not* yet "σᵢ commutes with the product", and it becomes that exactly when
  `Lᵢ` and `L_{i+1}` commute — which is the open problem, not an input.
* **`jmRaw_comm_sigma_far`** — `σⱼ Lᵢ = Lᵢ σⱼ` for `j ≥ i + 1`, at every `i`, by induction on the
  recursion.  This is the far half of commutativity in general, superseding the single instance
  proved previously.

## Where the derivation stops — stated exactly

**Adjacent commutativity `Lᵢ L_{i+1} = L_{i+1} Lᵢ` is NOT proved here, and I could not reduce it to
the relations above.**  The obstruction is recorded honestly rather than papered over, because it is
easy to think one has it:

Writing `u := Lᵢσᵢ` and `v := σᵢLᵢ`, the exchange relations give `u = (σᵢ − h)L_{i+1}` and
`v = L_{i+1}(σᵢ − h)`, and then `Lᵢ L_{i+1} = u²` while `L_{i+1} Lᵢ = v²`.  So the goal becomes
`(σᵢ−h)w = w(σᵢ−h)` with `w := L_{i+1}(σᵢ−h)L_{i+1}` — i.e. it reduces to *another* commutation of
the same shape, not to anything already proved.  `sigma_comm_add` gives the **sum**; the **product**
needs strictly more.

Consequently `∏Lᵢ = Δ²` remains proved only at `n = 2, 3`, and the general-`λ` twist
`θ_λ = q^{c(λ)}` remains **conditional**.

## What this changes for `JucysMurphySpectrum`

Nothing is discharged, but the residual assumption is now **one identified statement** — adjacent
commutativity, plus the spectral eigenvalue property — rather than an opaque bundle.  See bean
`qou-u9o1`.

Refs:
- [wenzl1988] Hecke algebra representations (seminormal form; JM spectrum).
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-! ## The two exchange relations -/

/-- **`σᵢ L_{i+1} = h L_{i+1} + Lᵢ σᵢ`**, with `h = q − q⁻¹`.  One application of the Hecke
relation `σᵢ² = hσᵢ + 1` to the leading `σᵢ·σᵢ`. -/
theorem sigma_mul_jm_succ (H : HeckeGenerators R A q) (i : ℕ) :
    H.σ i * jmRaw H (i + 1) = (q - q⁻¹) • jmRaw H (i + 1) + jmRaw H i * H.σ i := by
  rw [jmRaw_succ,
    show H.σ i * (H.σ i * jmRaw H i * H.σ i) = (H.σ i * H.σ i) * jmRaw H i * H.σ i from by
      noncomm_ring,
    H.hecke i, ← Algebra.smul_def]
  simp [add_mul]

/-- **`L_{i+1} σᵢ = h L_{i+1} + σᵢ Lᵢ`** — the mirror relation, from the trailing `σᵢ·σᵢ`. -/
theorem jm_succ_mul_sigma (H : HeckeGenerators R A q) (i : ℕ) :
    jmRaw H (i + 1) * H.σ i = (q - q⁻¹) • jmRaw H (i + 1) + H.σ i * jmRaw H i := by
  rw [jmRaw_succ,
    show H.σ i * jmRaw H i * H.σ i * H.σ i = H.σ i * jmRaw H i * (H.σ i * H.σ i) from by
      noncomm_ring,
    H.hecke i, ← Algebra.smul_def]
  simp [mul_add, mul_assoc]

/-! ## `σᵢ` commutes with the adjacent SUM -/

/-- **`σᵢ` commutes with `Lᵢ + L_{i+1}`.**

The two exchange relations carry the *same* `h·L_{i+1}` term, so it cancels in the sum:

    σᵢ(Lᵢ + L_{i+1}) = σᵢLᵢ + (h·L_{i+1} + Lᵢσᵢ)
                     = (L_{i+1}σᵢ − h·L_{i+1}) + h·L_{i+1} + Lᵢσᵢ
                     = (Lᵢ + L_{i+1})σᵢ.

This is the classical fact that `σᵢ` commutes with the *symmetric functions* of the adjacent JM
pair.  It holds at **every** `i` — the first general commutation statement in this corpus. -/
theorem sigma_comm_add (H : HeckeGenerators R A q) (i : ℕ) :
    H.σ i * (jmRaw H i + jmRaw H (i + 1)) = (jmRaw H i + jmRaw H (i + 1)) * H.σ i := by
  have h1 := sigma_mul_jm_succ H i
  have h2 := jm_succ_mul_sigma H i
  have hσL : H.σ i * jmRaw H i = jmRaw H (i + 1) * H.σ i - (q - q⁻¹) • jmRaw H (i + 1) := by
    rw [h2]; abel
  rw [mul_add, add_mul, hσL, h1]
  abel

/-- **`σᵢ (Lᵢ L_{i+1}) = (L_{i+1} Lᵢ) σᵢ`.**

Note the **order swap** on the right: this is not yet "σᵢ commutes with the product".  It becomes
that precisely when `Lᵢ` and `L_{i+1}` commute — which is the open problem, so this identity must
not be quoted as commutation. -/
theorem sigma_mul_jm_prod (H : HeckeGenerators R A q) (i : ℕ) :
    H.σ i * (jmRaw H i * jmRaw H (i + 1)) = (jmRaw H (i + 1) * jmRaw H i) * H.σ i := by
  have h1 := sigma_mul_jm_succ H i
  have h2 := jm_succ_mul_sigma H i
  have hσL : H.σ i * jmRaw H i = jmRaw H (i + 1) * H.σ i - (q - q⁻¹) • jmRaw H (i + 1) := by
    rw [h2]; abel
  calc H.σ i * (jmRaw H i * jmRaw H (i + 1))
      = (H.σ i * jmRaw H i) * jmRaw H (i + 1) := by noncomm_ring
    _ = (jmRaw H (i + 1) * H.σ i - (q - q⁻¹) • jmRaw H (i + 1)) * jmRaw H (i + 1) := by rw [hσL]
    _ = jmRaw H (i + 1) * (H.σ i * jmRaw H (i + 1))
          - (q - q⁻¹) • (jmRaw H (i + 1) * jmRaw H (i + 1)) := by
        simp [sub_mul, mul_assoc]
    _ = jmRaw H (i + 1) * ((q - q⁻¹) • jmRaw H (i + 1) + jmRaw H i * H.σ i)
          - (q - q⁻¹) • (jmRaw H (i + 1) * jmRaw H (i + 1)) := by rw [h1]
    _ = (jmRaw H (i + 1) * jmRaw H i) * H.σ i := by
        simp [mul_add, mul_smul_comm, mul_assoc]

/-! ## Far commutation, in general -/

/-- **`σⱼ` commutes with `Lᵢ` whenever `j > i`** (strictly).

`jmRaw H i` is a word in `σ₀ … σ_{i−1}`, so `j > i` puts `σⱼ` at distance `≥ 2` from every letter
and the presentation's `far` relation applies at each one.  Induction on `i`.

**The strictness is not a technicality.**  At `j = i` the generator `σᵢ` is *adjacent* to the
outermost letter of `L_{i+1}`, `far` does not apply, and that boundary case is exactly the open
adjacent-commutativity problem this file could not close.  An earlier draft of this theorem stated
`i ≤ j` and was mathematically wrong for that reason; the Lean caught it. -/
theorem jmRaw_comm_sigma_far (H : HeckeGenerators R A q) :
    ∀ i j : ℕ, i < j → H.σ j * jmRaw H i = jmRaw H i * H.σ j := by
  intro i
  induction i with
  | zero => intro j _; rw [jmRaw_zero, mul_one, one_mul]
  | succ k ih =>
      intro j hj
      have hfar : H.σ k * H.σ j = H.σ j * H.σ k := H.far k j (by omega)
      have hk : H.σ j * jmRaw H k = jmRaw H k * H.σ j := ih j (by omega)
      rw [jmRaw_succ]
      calc H.σ j * (H.σ k * jmRaw H k * H.σ k)
          = (H.σ j * H.σ k) * jmRaw H k * H.σ k := by noncomm_ring
        _ = (H.σ k * H.σ j) * jmRaw H k * H.σ k := by rw [← hfar]
        _ = H.σ k * (H.σ j * jmRaw H k) * H.σ k := by noncomm_ring
        _ = H.σ k * (jmRaw H k * H.σ j) * H.σ k := by rw [hk]
        _ = H.σ k * jmRaw H k * (H.σ j * H.σ k) := by noncomm_ring
        _ = H.σ k * jmRaw H k * (H.σ k * H.σ j) := by rw [hfar]
        _ = H.σ k * jmRaw H k * H.σ k * H.σ j := by noncomm_ring

/-! ## The hook-word form of `Lᵢ`

The exchange relations above are exhausted for the adjacent case.  The standard next tool is the
explicit *hook word*

    L_k = (σ_{k−1} ⋯ σ₁) σ₀ σ₀ (σ₁ ⋯ σ_{k−1}),

which exhibits `L_k` as a palindrome around `σ₀²` and makes the letters it contains visible — the
fact `jmRaw_comm_sigma_far` uses implicitly and the fact any braid-relation attack on adjacent
commutativity needs explicitly. -/

/-- Descending product `σ_{k−1} σ_{k−2} ⋯ σ₁`, empty for `k ≤ 1`. -/
def descProd (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | 1 => 1
  | (k + 1) => H.σ k * descProd H k

/-- Ascending product `σ₁ ⋯ σ_{k−1}`, empty for `k ≤ 1`. -/
def ascProd (H : HeckeGenerators R A q) : ℕ → A
  | 0 => 1
  | 1 => 1
  | (k + 1) => ascProd H k * H.σ k

@[simp] theorem descProd_one (H : HeckeGenerators R A q) : descProd H 1 = 1 := rfl
@[simp] theorem ascProd_one (H : HeckeGenerators R A q) : ascProd H 1 = 1 := rfl

theorem descProd_succ (H : HeckeGenerators R A q) (k : ℕ) (hk : 1 ≤ k) :
    descProd H (k + 1) = H.σ k * descProd H k := by
  cases k with
  | zero => omega
  | succ m => rfl

theorem ascProd_succ (H : HeckeGenerators R A q) (k : ℕ) (hk : 1 ≤ k) :
    ascProd H (k + 1) = ascProd H k * H.σ k := by
  cases k with
  | zero => omega
  | succ m => rfl

/-- **The hook-word form**: `L_k = (σ_{k−1}⋯σ₁) σ₀² (σ₁⋯σ_{k−1})` for `k ≥ 1`.

A palindrome around `σ₀²`.  Proved by induction directly on the recursion
`L_{k+1} = σ_k L_k σ_k`, which appends `σ_k` to each side — so the two products grow in step and
the centre never moves. -/
theorem jmRaw_hook (H : HeckeGenerators R A q) :
    ∀ k : ℕ, 1 ≤ k → jmRaw H k = descProd H k * (H.σ 0 * H.σ 0) * ascProd H k := by
  intro k hk
  induction k with
  | zero => omega
  | succ m ih =>
      rcases Nat.eq_or_lt_of_le hk with h1 | hm
      · -- k = 1
        have : m = 0 := by omega
        subst this
        rw [jmRaw_succ, jmRaw_zero]
        simp
      · -- k = m + 1 with m ≥ 1
        have hm1 : 1 ≤ m := by omega
        rw [jmRaw_succ, ih hm1, descProd_succ H m hm1, ascProd_succ H m hm1]
        noncomm_ring

/-! ## The first genuine instance of ADJACENT commutativity

The exchange relations could not reach the adjacent case, but the **half-twist** does at `i = 1`.
The route is worth recording because it is not the one the exchange relations suggest: it goes
through `Δ = σ₀σ₁σ₀ = σ₁σ₀σ₁` and the fact that `Δ²` is a *palindrome-insensitive* square. -/

/-- **`(σ₀σ₁)³ = (σ₁σ₀)³`** — both are `Δ·Δ` for the half-twist `Δ = σ₀σ₁σ₀ = σ₁σ₀σ₁`.

`(σ₀σ₁)³` groups as `(σ₀σ₁σ₀)(σ₁σ₀σ₁)` and `(σ₁σ₀)³` as `(σ₁σ₀σ₁)(σ₀σ₁σ₀)`; the braid relation
turns each factor into the other, so both collapse to the same square. -/
theorem fullTwist3_symm (H : HeckeGenerators R A q) :
    (H.σ 0 * H.σ 1) ^ 3 = (H.σ 1 * H.σ 0) ^ 3 := by
  have hb : H.σ 0 * H.σ 1 * H.σ 0 = H.σ 1 * H.σ 0 * H.σ 1 := H.braid 0
  calc (H.σ 0 * H.σ 1) ^ 3
      = (H.σ 0 * H.σ 1 * H.σ 0) * (H.σ 1 * H.σ 0 * H.σ 1) := by noncomm_ring
    _ = (H.σ 0 * H.σ 1 * H.σ 0) * (H.σ 0 * H.σ 1 * H.σ 0) := by rw [← hb]
    _ = (H.σ 1 * H.σ 0 * H.σ 1) * (H.σ 0 * H.σ 1 * H.σ 0) := by rw [hb]
    _ = (H.σ 1 * H.σ 0) ^ 3 := by noncomm_ring

/-- `L₃L₂ = (σ₁σ₀)³` — the mirror of `jmRaw_prod_three`, by one braid application. -/
theorem jmRaw_two_mul_one (H : HeckeGenerators R A q) :
    jmRaw H 2 * jmRaw H 1 = (H.σ 1 * H.σ 0) ^ 3 := by
  have hb : H.σ 0 * H.σ 1 * H.σ 0 = H.σ 1 * H.σ 0 * H.σ 1 := H.braid 0
  simp only [jmRaw_succ, jmRaw_zero, one_mul, mul_one]
  calc H.σ 1 * (H.σ 0 * H.σ 0) * H.σ 1 * (H.σ 0 * H.σ 0)
      = (H.σ 1 * H.σ 0) * (H.σ 0 * H.σ 1 * H.σ 0) * H.σ 0 := by noncomm_ring
    _ = (H.σ 1 * H.σ 0) * (H.σ 1 * H.σ 0 * H.σ 1) * H.σ 0 := by rw [hb]
    _ = (H.σ 1 * H.σ 0) ^ 3 := by noncomm_ring

/-- **Adjacent commutativity at `i = 1`: `L₂L₃ = L₃L₂`.**

The first genuine instance of the case the exchange relations could not reach.  Both products are
the full twist, approached from opposite sides — `L₂L₃ = (σ₀σ₁)³` (`jmRaw_prod_three`) and
`L₃L₂ = (σ₁σ₀)³` (`jmRaw_two_mul_one`) — and `fullTwist3_symm` identifies those.

**This is one instance, not the general theorem.**  It works because at `i = 1` both products are
*the whole* full twist of `B₃`, so the half-twist symmetry closes it; for `i ≥ 2` the products are
proper sub-words and that argument does not apply.  General adjacent commutativity remains open
(bean `qou-u9o1`). -/
theorem jmRaw_comm_adjacent_one (H : HeckeGenerators R A q) :
    jmRaw H 1 * jmRaw H 2 = jmRaw H 2 * jmRaw H 1 := by
  have h1 : jmRaw H 1 * jmRaw H 2 = (H.σ 0 * H.σ 1) ^ 3 := by
    have := jmRaw_prod_three H
    rw [jmRaw_zero, one_mul] at this
    simpa [fullTwist3] using this
  rw [h1, jmRaw_two_mul_one, fullTwist3_symm]

end QOU.BraidKnot.Hecke
