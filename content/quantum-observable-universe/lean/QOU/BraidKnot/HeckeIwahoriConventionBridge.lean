import QOU.BraidKnot.HeckeBoundedJMComm
import QOU.BraidKnot.HeckeStableScalarCascade

/-!
# Iwahori normalisation → the corpus's `σ` convention

The corpus states the Hecke relation as `σ² = (q − q⁻¹)σ + 1` (AGENTS.md §7a), so `σ` has
eigenvalues `q` and `−q⁻¹`.  The Iwahori–Hecke literature — and `QOU/IwahoriHecke/` — states it as
`(T − Q)(T + 1) = 0`, so `T` has eigenvalues `Q` and `−1`.  Bridging the two is the one obstacle
between the Jucys–Murphy arc (`HeckeGeneratorsBelow` and everything over it) and the constructed
algebra.

## The rescaling is exact, and needs no square root

Write `σ = c · T`.  From `T² = (Q − 1)T + Q`,

    σ² = c²T² = c(Q − 1)·(cT) + c²Q = c(Q − 1)·σ + c²Q,

so matching `σ² = (q − q⁻¹)σ + 1` requires **both**

    c²Q = 1        and        c(Q − 1) = q − q⁻¹.

Taking `Q = q²` and `c = q⁻¹` satisfies both identically: `q⁻² · q² = 1`, and
`q⁻¹(q² − 1) = q − q⁻¹`.

**So the parameter, not the generator, is what moves.**  One does not adjoin `√q` to the base ring
and rescale `T`; one instantiates the Iwahori algebra at `Q = q²` — the corpus's `q` is already the
square root of the Iwahori parameter — and rescales by `q⁻¹`, which is in the field whenever
`q ≠ 0`.

This matters for §7c: the "adjoin a square root" reading forces a base-ring extension (and, if done
carelessly, `ℝ`).  Nothing here leaves a generic `[Field R]`.

## Scale-invariance of the other two relations

The braid and far-commutation relations are homogeneous of the same degree on both sides, so a
scalar rescaling cannot disturb them:

* braid — degree 3 each side, `c³` cancels (`braid_of_scaled`);
* far — degree 2 each side, `c²` cancels (`far_of_scaled`).

Together with `hecke_of_iwahori` this gives `heckeGeneratorsBelow_of_iwahori`: **any family
satisfying the Iwahori relations at `Q = q²` is a `HeckeGeneratorsBelow` at `q`.**  That is the
whole convention half of the bridge (bean `qou-0o6j`); what it still needs from
`QOU/IwahoriHecke/` is a family whose *braid* relations actually hold, which today they do not —
`heckeRel` imposes the quadratic relation only (bean `qou-ayyi`).
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A]

/-- **The quadratic bridge.**  If `T` satisfies the Iwahori relation at `Q = q²`, then `q⁻¹ · T`
satisfies the corpus relation at `q`.  No square root, no base-ring extension: `q ≠ 0` suffices.

Stated with the scalar action `•` rather than `algebraMap … * …`: the two agree by
`Algebra.smul_def` (see `hecke_of_iwahori_algebraMap`), and `•` is what `smul_smul` /
`smul_mul_assoc` / `mul_smul_comm` are stated for, so the scalars move without fighting
`algebraMap`'s centrality. -/
theorem hecke_of_iwahori (q : R) (hq : q ≠ 0) (T : A)
    (hT : (T - (q * q) • (1 : A)) * (T + 1) = 0) :
    (q⁻¹ • T) * (q⁻¹ • T) = (q - q⁻¹) • (q⁻¹ • T) + 1 := by
  have hTsq : T * T = (q * q) • T + (q * q) • (1 : A) - T := by
    have h : T * T + T - (q * q) • T - (q * q) • (1 : A) = 0 := by
      have := hT
      simp only [sub_mul, mul_add, mul_one, smul_mul_assoc, one_mul] at this
      linear_combination (norm := noncomm_ring) this
    linear_combination (norm := noncomm_ring) h
  have hinv : q⁻¹ * q⁻¹ * (q * q) = 1 := by field_simp
  have hmix : (q - q⁻¹) * q⁻¹ = 1 - q⁻¹ * q⁻¹ := by field_simp
  calc (q⁻¹ • T) * (q⁻¹ • T)
      = (q⁻¹ * q⁻¹) • (T * T) := by
        rw [smul_mul_assoc, mul_smul_comm, smul_smul]
    _ = (q⁻¹ * q⁻¹) • ((q * q) • T + (q * q) • (1 : A) - T) := by rw [hTsq]
    _ = (q⁻¹ * q⁻¹ * (q * q)) • T + (q⁻¹ * q⁻¹ * (q * q)) • (1 : A)
          - (q⁻¹ * q⁻¹) • T := by
        rw [smul_sub, smul_add, smul_smul, smul_smul]
    _ = T + 1 - (q⁻¹ * q⁻¹) • T := by rw [hinv, one_smul, one_smul]
    _ = (1 - q⁻¹ * q⁻¹) • T + 1 := by rw [sub_smul, one_smul]; abel
    _ = ((q - q⁻¹) * q⁻¹) • T + 1 := by rw [hmix]
    _ = _ := by rw [smul_smul]

/-- The same statement in `algebraMap` form — the shape `HeckeGeneratorsBelow.hecke` expects. -/
theorem hecke_of_iwahori_algebraMap (q : R) (hq : q ≠ 0) (T : A)
    (hT : (T - algebraMap R A (q * q)) * (T + 1) = 0) :
    (algebraMap R A q⁻¹ * T) * (algebraMap R A q⁻¹ * T)
      = algebraMap R A (q - q⁻¹) * (algebraMap R A q⁻¹ * T) + 1 := by
  have hT' : (T - (q * q) • (1 : A)) * (T + 1) = 0 := by
    rwa [Algebra.smul_def, mul_one]
  have := hecke_of_iwahori q hq T hT'
  simpa only [Algebra.smul_def, mul_one] using this

/-- **Braid is scale-invariant** — degree 3 on both sides, so `c³` cancels. -/
theorem braid_of_scaled (c : R) (S T : A) (h : S * T * S = T * S * T) :
    (c • S) * (c • T) * (c • S) = (c • T) * (c • S) * (c • T) := by
  simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [h]

/-- **Far commutation is scale-invariant** — degree 2 on both sides, so `c²` cancels. -/
theorem far_of_scaled (c : R) (S T : A) (h : S * T = T * S) :
    (c • S) * (c • T) = (c • T) * (c • S) := by
  simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [h]

/-! ## The bridge, assembled

Given a family `T : ℕ → A` satisfying the **Iwahori** relations at parameter `Q = q²` — quadratic,
braid and far — the rescaled family `σ i := q⁻¹ • T i` satisfies the **corpus** relations at `q`,
i.e. it is a `HeckeGeneratorsBelow R A q n`.

This is the convention half of bean `qou-0o6j`.  It is stated against a hypothesised `T`-family
rather than against `QOU.IwahoriHecke` because that construction does not yet impose the braid
relations (bean `qou-ayyi` / `qou-phir`); the moment it does, this is the instance. -/
def heckeGeneratorsBelow_of_iwahori {n : ℕ} (q : R) (hq : q ≠ 0) (T : ℕ → A)
    (hquad : ∀ i, i + 1 < n → (T i - (q * q) • (1 : A)) * (T i + 1) = 0)
    (hbraid : ∀ i, i + 2 < n → T i * T (i + 1) * T i = T (i + 1) * T i * T (i + 1))
    (hfar : ∀ i j, i + 1 < j → j + 1 < n → T i * T j = T j * T i) :
    HeckeGeneratorsBelow R A q n where
  σ := fun i => q⁻¹ • T i
  hecke := fun i hi => by
    have := hecke_of_iwahori q hq (T i) (hquad i hi)
    simpa only [Algebra.smul_def, mul_one] using this
  braid := fun i hi => braid_of_scaled q⁻¹ (T i) (T (i + 1)) (hbraid i hi)
  far := fun i j hij hjn => far_of_scaled q⁻¹ (T i) (T j) (hfar i j hij hjn)

/-- **The payoff, demonstrated.**  An Iwahori-normalised family at `Q = q²` inherits Jucys–Murphy
commutativity with no further hypotheses — the arc's theorems reach it through the bridge.

`jmRawB_comm` is the arc's result; everything this needed from the Iwahori side is the three
relations at `Q = q²`.  The same composition carries `jmProdB_eq_deltaPowB`, `IsJMWeightB` and the
theta tie-in. -/
theorem iwahori_jm_comm {n : ℕ} (q : R) (hq : q ≠ 0) (T : ℕ → A)
    (hquad : ∀ i, i + 1 < n → (T i - (q * q) • (1 : A)) * (T i + 1) = 0)
    (hbraid : ∀ i, i + 2 < n → T i * T (i + 1) * T i = T (i + 1) * T i * T (i + 1))
    (hfar : ∀ i j, i + 1 < j → j + 1 < n → T i * T j = T j * T i)
    (i k : ℕ) (hi : i < n) (hk : k < n) :
    jmRawB (heckeGeneratorsBelow_of_iwahori q hq T hquad hbraid hfar) i
        * jmRawB (heckeGeneratorsBelow_of_iwahori q hq T hquad hbraid hfar) k
      = jmRawB (heckeGeneratorsBelow_of_iwahori q hq T hquad hbraid hfar) k
        * jmRawB (heckeGeneratorsBelow_of_iwahori q hq T hquad hbraid hfar) i :=
  jmRawB_comm _ i k hi hk

/-! ## The bridge runs both ways, and here is a concrete instance

Everything above is stated against a *hypothesised* Iwahori family.  A bridge nobody can feed is
worth little, so this section closes the loop:

* `iwahori_of_hecke` — the **inverse** rescaling.  A corpus-convention `σ` gives an
  Iwahori-convention `T = q·σ` satisfying `(T − q²)(T + 1) = 0`.
* `stdTwoIw` — the explicit `2×2` Young seminormal matrices of `HeckeStableScalarCascade`,
  pushed into Iwahori normalisation.
* `stdTwoIw_isHeckeGeneratorsBelow` — they satisfy the three Iwahori relations at `n = 3`, so the
  bridge applies to them.
* `stdTwoIw_roundTrip` — and what comes back out is `stdTwo` again, on the nose.

The round trip is the falsifiability check: a bridge with the scaling inverted, or with `Q = q`
instead of `q²`, would fail it. -/

/-- **The inverse rescaling.**  If `S` satisfies the corpus relation at `q`, then `q·S` satisfies
the Iwahori relation at `Q = q²`.

No `q ≠ 0` needed, unlike `hecke_of_iwahori`: this direction multiplies by `q` rather than by
`q⁻¹`, and the identity survives `q = 0` (where Lean's `q⁻¹ = 0` makes both sides collapse). -/
theorem iwahori_of_hecke (q : R) (S : A)
    (hS : S * S = (q - q⁻¹) • S + 1) :
    (q • S - (q * q) • (1 : A)) * (q • S + 1) = 0 := by
  have hcoef : q * q * (q - q⁻¹) + q - q * q * q = 0 := by field_simp; ring
  have expand : (q • S - (q * q) • (1 : A)) * (q • S + 1)
      = (q * q) • (S * S) + q • S - (q * q * q) • S - (q * q) • (1 : A) := by
    simp only [sub_mul, mul_add, mul_one, one_mul, smul_mul_assoc, mul_smul_comm]
    module
  have collapse : (q * q) • ((q - q⁻¹) • S + 1) + q • S - (q * q * q) • S - (q * q) • (1 : A)
      = (q * q * (q - q⁻¹) + q - q * q * q) • S := by module
  rw [expand, hS, collapse, hcoef, zero_smul]

variable {K : Type} [Field K]

/-- The explicit `2×2` seminormal generators in **Iwahori** normalisation: `T i = q · σ i`. -/
noncomputable def stdTwoIw (q : K) : ℕ → Matrix (Fin 2) (Fin 2) K
  | 0 => q • stdTwo0 q
  | 1 => q • stdTwo1 q
  | _ => 1

/-- They satisfy the Iwahori relations at `Q = q²`, so `heckeGeneratorsBelow_of_iwahori` applies —
the bridge has a concrete `dim = 2` input, not merely a hypothesised one. -/
noncomputable def stdTwoIw_isHeckeGeneratorsBelow (q : K) (hq : q ≠ 0) :
    HeckeGeneratorsBelow K (Matrix (Fin 2) (Fin 2) K) q 3 :=
  heckeGeneratorsBelow_of_iwahori q hq (stdTwoIw q)
    (by
      intro i hi
      have hi2 : i < 2 := by omega
      interval_cases i
      · exact iwahori_of_hecke q _ (stdTwo_hecke0 hq)
      · exact iwahori_of_hecke q _ (stdTwo_hecke1 hq))
    (by
      intro i hi
      have hi1 : i < 1 := by omega
      interval_cases i
      · exact braid_of_scaled q _ _ (stdTwo_braid hq))
    (by intro i j hij hjn; omega)

/-- **The round trip.**  Rescaling `σ ↦ q·σ` into Iwahori normalisation and back through the bridge
returns `σ`.  This is what would break if the scaling were inverted, or if the bridge used `Q = q`
rather than `Q = q²`. -/
theorem stdTwoIw_roundTrip (q : K) (hq : q ≠ 0) :
    (stdTwoIw_isHeckeGeneratorsBelow q hq).σ 0 = stdTwo0 q
      ∧ (stdTwoIw_isHeckeGeneratorsBelow q hq).σ 1 = stdTwo1 q := by
  constructor <;>
    · show q⁻¹ • (stdTwoIw q _) = _
      simp only [stdTwoIw, smul_smul, inv_mul_cancel₀ hq, one_smul]

end QOU.BraidKnot.Hecke
