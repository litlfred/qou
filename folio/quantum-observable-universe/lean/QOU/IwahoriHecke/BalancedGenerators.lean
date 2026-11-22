import QOU.MathlibExt.IwahoriHeckeAlgebra
import QOU.MathlibExt.SkeinFromHecke

/-!
# The §7a balanced generators of the Iwahori–Hecke algebra

Two pieces of Hecke infrastructure already live in this corpus and **nothing connected
them**. This file is that connection.

* [`QOU.MathlibExt.IwahoriHecke`](../MathlibExt/IwahoriHeckeAlgebra.lean) *constructs* the
  algebra `H(M, Q)` by generators and relations, in the **Iwahori** normalisation
  `(T_i − Q)(T_i + 1) = 0`, with its universal property and a proof that it does not
  collapse.
* [`QOU.MathlibExt.SkeinRelation`](../MathlibExt/SkeinFromHecke.lean) develops the whole
  skein calculus — explicit inverse, unit, `T − T⁻¹ = q − q⁻¹`, eigenvalue factorisation —
  for an abstract element satisfying the **symmetric** normalisation
  `σ² = (q − q⁻¹)σ + 1` that AGENTS.md §7a mandates.

The gap: the constructed algebra's own generators are **not** `IsHeckeGenerator`s. In the
Iwahori normalisation the eigenvalues are `Q` and `−1`, not `q` and `−q⁻¹`, so the skein
calculus was floating free of the only algebra the corpus actually builds. Neither file
mentions the other.

## The bridge

Take the Iwahori parameter to be `Q = q²` for scalars `q`, `qi` with `q·qi = 1`, and
rescale:

$$\sigma_i \;:=\; qi \cdot T_i .$$

Then `σ_i² = qi²((q²−1)T_i + q²) = (1 − qi²)T_i + 1 = (q − qi)σ_i + 1`, which is exactly
`IsHeckeGenerator q qi σ_i` (`isHeckeGenerator_sigma`). From that single theorem the
entire `SkeinRelation` API transfers onto the generators of the constructed algebra, and
this file spells out the consequences AGENTS.md §7a names by hand: the eigenvalue
factorisation `(σ_i − q)(σ_i + qi) = 0`, the negative crossing `σ_i⁻¹ = σ_i − (q − qi)`,
and the skein relation `L₊ − L₋ = (q − qi) L₀`.

The rescaling is a *change of generators, not of algebra*: `T_i = q σ_i`
(`T_eq_sigma`), so the `σ_i` generate, uniqueness of maps out of the algebra can be
tested on them (`hom_ext_sigma`), and a family satisfying the balanced relations lifts
(`liftBalanced`). Nothing is lost and nothing new is assumed.

Following `SkeinFromHecke`'s own design, `qi` is carried as a **separate scalar** with an
explicit `q * qi = 1` hypothesis rather than written `q⁻¹`. That keeps the base ring a
bare `CommRing` — no `Field`, no `Inv`, no ordering, nothing archimedean (AGENTS.md §7c).

## What this does NOT do

It does not construct the `T_w` basis, prove `H` free of rank `|W|`, or construct the
Markov trace. Those remain open — see `QOU.IwahoriHecke.Tw`.

-- Ref: [humphreys1990] §7.4 (both normalisations; the rescaling is standard)
-- Ref: [leitner2026] AGENTS.md §7a (Hecke-Skein convention); bean qou-k4oq
-/

namespace QOU.IwahoriHecke.Balanced

open QOU.MathlibExt.IwahoriHecke QOU.MathlibExt.SkeinRelation

variable {R : Type*} [CommRing R]

section Rescaling

variable {A : Type*} [Ring A] [Algebra R A]

/-- Scalars from the base ring are central. Used as the one commutation step in otherwise
purely associative rearrangements. -/
private theorem am_comm (r : R) (x : A) :
    x * algebraMap R A r = algebraMap R A r * x := (Algebra.commutes r x).symm

/-- Squaring a central-scalar multiple: `(r·z)² = r²·z²`. The single commutation step both
directions of the convention bridge rest on. -/
private theorem sq_am_mul (r : R) (z : A) :
    (algebraMap R A r * z) * (algebraMap R A r * z)
      = (algebraMap R A r * algebraMap R A r) * (z * z) := by
  calc (algebraMap R A r * z) * (algebraMap R A r * z)
      = algebraMap R A r * (z * algebraMap R A r) * z := by noncomm_ring
    _ = algebraMap R A r * (algebraMap R A r * z) * z := by rw [am_comm]
    _ = (algebraMap R A r * algebraMap R A r) * (z * z) := by noncomm_ring

variable {q qi : R}

/-- **Iwahori ⟹ balanced.** If `y` satisfies `(y − q²)(y + 1) = 0` then `qi·y` satisfies
the symmetric relation `x² = (q − qi)x + 1`.

Stated for an arbitrary element of an arbitrary `R`-algebra: the rescaling is a fact about
the two quadratics, not about the Hecke algebra. -/
theorem isHeckeGenerator_of_iwahori (hqi : q * qi = 1) {y : A}
    (hy : (y - algebraMap R A (q * q)) * (y + 1) = 0) :
    IsHeckeGenerator q qi (algebraMap R A qi * y) := by
  have h1 : y * y = algebraMap R A (q * q) * y - y + algebraMap R A (q * q) := by
    rw [mul_add, sub_mul, sub_mul, mul_one, mul_one] at hy
    linear_combination (norm := noncomm_ring) hy
  have s1 : qi * qi * (q * q) = 1 := by
    rw [show qi * qi * (q * q) = (q * qi) * (q * qi) from by ring, hqi, mul_one]
  show (algebraMap R A qi * y) * (algebraMap R A qi * y)
      = algebraMap R A (q - qi) * (algebraMap R A qi * y) + 1
  rw [sq_am_mul, ← map_mul, h1]
  simp only [mul_add, mul_sub, ← mul_assoc, ← map_mul, s1, hqi, map_sub, map_one, sub_mul,
    one_mul]

/-- **Balanced ⟹ Iwahori.** If `x` satisfies `x² = (q − qi)x + 1` then `q·x` satisfies the
Iwahori relation at the squared parameter, `(qx − q²)(qx + 1) = 0`. -/
theorem iwahori_of_isHeckeGenerator (hqi : q * qi = 1) {x : A}
    (hx : IsHeckeGenerator q qi x) :
    (algebraMap R A q * x - algebraMap R A (q * q)) * (algebraMap R A q * x + 1) = 0 := by
  have s2 : q * q * qi = q := by rw [mul_assoc, hqi, mul_one]
  rw [sub_mul, mul_add, mul_add, mul_one, mul_one, sq_am_mul, ← map_mul, hx.eq]
  simp only [mul_add, mul_sub, mul_one, ← mul_assoc, ← map_mul, s2, map_sub, sub_mul]
  noncomm_ring

/-- **Rescaling by a central scalar multiplies `altProd` by its power.**
`altProd (r·a) (r·b) n = rⁿ · altProd a b n`. The alternation is invisible to a central
scalar: each of the `n` factors contributes exactly one `r`, whichever of `a`, `b` it is.

This is what carries the braid relation across the rescaling. -/
theorem altProd_algebraMap_mul (r : R) :
    ∀ (n : ℕ) (a b : A),
      altProd (algebraMap R A r * a) (algebraMap R A r * b) n
        = algebraMap R A (r ^ n) * altProd a b n := by
  intro n
  induction n with
  | zero => intro a b; simp
  | succ k ih =>
    intro a b
    rw [altProd, altProd, ih b a, pow_succ', map_mul]
    calc algebraMap R A r * a * (algebraMap R A (r ^ k) * altProd b a k)
        = algebraMap R A r * (a * algebraMap R A (r ^ k)) * altProd b a k := by noncomm_ring
      _ = algebraMap R A r * (algebraMap R A (r ^ k) * a) * altProd b a k := by rw [am_comm]
      _ = algebraMap R A r * algebraMap R A (r ^ k) * (a * altProd b a k) := by noncomm_ring

end Rescaling

/-! ## The balanced generators of the constructed algebra -/

variable {B : Type*} (M : B → B → ℕ) (q qi : R)

/-- The Iwahori–Hecke algebra at the **squared** parameter `Q = q²`. Squaring is what makes
the balanced rescaling `σ = qi·T` land on the §7a eigenvalues `q`, `−qi`. -/
abbrev BalancedHecke : Type _ := HeckeAlgebra R (q * q) M

/-- **The §7a generator** `σ_i = qi·T_i`, in the symmetric (skein) normalisation. -/
noncomputable def sigma (i : B) : BalancedHecke M q :=
  algebraMap R _ qi * T R (q * q) M i

variable {M q qi}

/-- **The bridge.** The rescaled generator satisfies the *symmetric* Hecke quadratic
relation of AGENTS.md §7a:

    σ_i² = (q − qi) σ_i + 1.

Everything in `QOU.MathlibExt.SkeinRelation` applies to `σ_i` from here on: the explicit
negative crossing, invertibility, the skein relation, and the eigenvalue factorisation. -/
theorem isHeckeGenerator_sigma (hqi : q * qi = 1) (i : B) :
    IsHeckeGenerator q qi (sigma M q qi i) :=
  isHeckeGenerator_of_iwahori hqi (T_quadratic (R := R) (q := q * q) (M := M) i)

/-- The Iwahori generator recovered from the balanced one: `T_i = q σ_i`. This is what
makes the rescaling a change of *generators* rather than a passage to a subalgebra — the
`σ_i` generate everything the `T_i` do. -/
theorem T_eq_sigma (hqi : q * qi = 1) (i : B) :
    T R (q * q) M i = algebraMap R (BalancedHecke M q) q * sigma M q qi i := by
  rw [sigma, ← mul_assoc, ← map_mul, hqi, map_one, one_mul]

/-! ### What the bridge buys, spelled out

Each of the following is `SkeinRelation`'s general result specialised along
`isHeckeGenerator_sigma`. They are restated here because AGENTS.md §7a names them for the
generators of `H_n(q)` specifically, and a reader looking for them in an `IwahoriHecke`
file should not have to know that the general form lives elsewhere. -/

/-- **The negative crossing** `σ_i⁻¹ = σ_i − (q − qi)` is a two-sided inverse. -/
theorem sigma_mul_negCrossing (hqi : q * qi = 1) (i : B) :
    sigma M q qi i * negCrossing q qi (sigma M q qi i) = 1 :=
  mul_negCrossing (isHeckeGenerator_sigma hqi i)

theorem negCrossing_mul_sigma (hqi : q * qi = 1) (i : B) :
    negCrossing q qi (sigma M q qi i) * sigma M q qi i = 1 :=
  negCrossing_mul (isHeckeGenerator_sigma hqi i)

/-- **`σ_i` is a unit** — which is what makes `H(M, q²)` a quotient of the *braid group*
algebra rather than merely of the free algebra. -/
theorem isUnit_sigma (hqi : q * qi = 1) (i : B) : IsUnit (sigma M q qi i) :=
  isUnit_of_isHeckeGenerator (isHeckeGenerator_sigma hqi i)

/-- `σ_i` as a unit, with its inverse given explicitly rather than existentially. -/
noncomputable def sigmaUnit (hqi : q * qi = 1) (i : B) : (BalancedHecke M q)ˣ :=
  heckeUnit (isHeckeGenerator_sigma hqi i)

/-- **The skein relation** `σ_i − σ_i⁻¹ = q − qi`, i.e. `L₊ − L₋ = (q − qi) L₀` with the
smoothing `L₀ = 1`. Stated against an *arbitrary* right inverse: a right inverse of `σ_i`
has no choice but to be the negative crossing. -/
theorem sigma_sub_inv (hqi : q * qi = 1) (i : B) {S : BalancedHecke M q}
    (hS : sigma M q qi i * S = 1) :
    sigma M q qi i - S = algebraMap R _ (q - qi) :=
  sub_inv_eq (isHeckeGenerator_sigma hqi i) hS

/-- **The eigenvalue factorisation** `(σ_i − q)(σ_i + qi) = 0`: the symmetric channel has
eigenvalue `q` and the antisymmetric channel `−qi`, as AGENTS.md §7a states. This is the
statement that fails in the Iwahori normalisation, where the eigenvalues are `q²` and `−1`. -/
theorem sigma_eigen (hqi : q * qi = 1) (i : B) :
    (sigma M q qi i - algebraMap R _ q) * (sigma M q qi i + algebraMap R _ qi) = 0 :=
  (isHeckeGenerator_iff_factored hqi _).mp (isHeckeGenerator_sigma hqi i)

/-! ### The braid relation, and generation -/

/-- **The braid relation transfers.** Rescaling every generator by the same central scalar
leaves the braid relation intact: both sides pick up the same power of `qi`, because
`altProd` on the two sides has the same number of factors exactly when `M` is symmetric. -/
theorem sigma_braid (hM : ∀ i j, M i j = M j i) (i j : B) :
    altProd (sigma M q qi i) (sigma M q qi j) (M i j)
      = altProd (sigma M q qi j) (sigma M q qi i) (M j i) := by
  rw [sigma, sigma, altProd_algebraMap_mul, altProd_algebraMap_mul,
    T_braid (R := R) (q := q * q) (M := M) i j, hM i j]

/-- **Maps out of the algebra are determined by the balanced generators.** Since
`T_i = q σ_i`, agreeing on the `σ_i` is the same as agreeing on the `T_i`. -/
theorem hom_ext_sigma (hqi : q * qi = 1) {A : Type*} [Ring A] [Algebra R A]
    (φ ψ : BalancedHecke M q →ₐ[R] A)
    (h : ∀ i : B, φ (sigma M q qi i) = ψ (sigma M q qi i)) : φ = ψ := by
  refine hom_ext R (q * q) M φ ψ (fun i => ?_)
  rw [T_eq_sigma hqi i, map_mul, map_mul, AlgHom.commutes, AlgHom.commutes, h i]

/-- **The balanced universal property.** A family satisfying the §7a relations — the
symmetric quadratic and the braid relation — extends to an algebra map out of `H(M, q²)`
sending `σ_i` to it.

The hypothesis is stated in the normalisation a representation of this framework is
actually written in, so a consumer never has to perform the rescaling by hand. -/
noncomputable def liftBalanced {A : Type*} [Ring A] [Algebra R A] (hqi : q * qi = 1)
    (f : B → A) (hq : ∀ i, IsHeckeGenerator q qi (f i))
    (hb : ∀ i j, altProd (f i) (f j) (M i j) = altProd (f j) (f i) (M j i))
    (hM : ∀ i j, M i j = M j i) :
    BalancedHecke M q →ₐ[R] A :=
  lift R (q * q) M (fun i => algebraMap R A q * f i)
    (fun i => iwahori_of_isHeckeGenerator hqi (hq i))
    (fun i j => by
      rw [altProd_algebraMap_mul, altProd_algebraMap_mul, hb i j, hM i j])

@[simp] theorem liftBalanced_sigma {A : Type*} [Ring A] [Algebra R A] (hqi : q * qi = 1)
    (f : B → A) (hq : ∀ i, IsHeckeGenerator q qi (f i))
    (hb : ∀ i j, altProd (f i) (f j) (M i j) = altProd (f j) (f i) (M j i))
    (hM : ∀ i j, M i j = M j i) (i : B) :
    liftBalanced hqi f hq hb hM (sigma M q qi i) = f i := by
  have hT : liftBalanced (M := M) hqi f hq hb hM (T R (q * q) M i)
      = algebraMap R A q * f i := lift_T R (q * q) M _ _ _ i
  rw [T_eq_sigma hqi i, map_mul, AlgHom.commutes] at hT
  calc liftBalanced (M := M) hqi f hq hb hM (sigma M q qi i)
      = algebraMap R A qi * (algebraMap R A q
          * liftBalanced (M := M) hqi f hq hb hM (sigma M q qi i)) := by
        rw [← mul_assoc, ← map_mul, mul_comm qi q, hqi, map_one, one_mul]
    _ = algebraMap R A qi * (algebraMap R A q * f i) := by rw [hT]
    _ = f i := by rw [← mul_assoc, ← map_mul, mul_comm qi q, hqi, map_one, one_mul]

/-! ### The `q = 1` degeneration

At `q = qi = 1` the deformation parameter `q − qi` vanishes and the quadratic collapses to
`σ_i² = 1`: the balanced generators become involutions, which is the group-algebra
presentation of the Coxeter group itself. This is the algebraic shadow of the `q = 1`
classical limit used in `QOU.MassTheory.ClassicalTraceFloor`, and it is the reason the
balanced normalisation is the right one to degenerate — in the Iwahori normalisation the
same limit gives `T² = 1` only after the rescaling performed here. -/

/-- At `q = qi = 1`, `σ_i² = 1`. -/
theorem sigma_sq_one (i : B) :
    sigma M (1 : R) (1 : R) i * sigma M (1 : R) (1 : R) i = 1 := by
  have h := (isHeckeGenerator_sigma (M := M) (q := (1 : R)) (qi := (1 : R)) (by ring) i).eq
  simpa using h

/-- At `q = qi = 1` each generator is its own inverse: the negative crossing is the
positive one, which is exactly the statement that the braiding has degenerated to a
symmetry. -/
theorem negCrossing_one (i : B) :
    negCrossing (1 : R) (1 : R) (sigma M (1 : R) (1 : R) i) = sigma M (1 : R) (1 : R) i := by
  simp [negCrossing]

end QOU.IwahoriHecke.Balanced
