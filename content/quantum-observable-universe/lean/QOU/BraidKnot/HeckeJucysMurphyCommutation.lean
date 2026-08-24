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

end QOU.BraidKnot.Hecke
