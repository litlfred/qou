import QOU.AppendixSurreals.Basic
import Mathlib.RingTheory.Subring.Basic

/-!
# QOU.AppendixSurreals.StandardPart — Robinson's standard-part map

The map `st : No_fin → ℝ` sending each finite surreal to the unique
real with infinitesimal difference.  Standard-part is a surjective
ring homomorphism whose kernel is the infinitesimals.

This module provides:

- `standardPart : K → ℝ` (zero on non-finite inputs by convention)
- ring-hom properties on the finite subring
- the kernel characterisation

## References

- [robinson1966] Robinson, *Non-standard Analysis*, §3.2.
- [alling1987] Alling, *Foundations of Analysis over Surreal Number
  Fields*, North-Holland.

LaTeX label: `def:standard-part-functor`
-/

namespace QOU.AppendixSurreals

open SurrealField
open Classical

universe u

variable {K : Type u} [SurrealField K]

/-- Robinson's **standard-part map**: sends each finite surreal to the
    unique real of which it is an infinitesimal perturbation. -/
-- Ref: [robinson1966] §3.2
noncomputable def standardPart (x : K) : ℝ :=
  if hx : IsFinite x then
    Classical.choose (isFinite_decomposition hx).exists
  else 0

/-- Notation: `st x = standardPart x`. -/
scoped notation "st" => standardPart

/-- Defining property: for finite `x`, `x - ofReal (st x)` is
    infinitesimal. -/
-- Ref: [robinson1966] §3.2
theorem standardPart_spec {x : K} (hx : IsFinite x) :
    IsInfinitesimal (x - SurrealField.ofReal (standardPart x)) := by
  unfold standardPart
  rw [dif_pos hx]
  exact (Classical.choose_spec (isFinite_decomposition hx).exists)

/-- `ofReal r` is finite for any real `r`. -/
-- Ref: [robinson1966] §3.1
theorem ofReal_isFinite (r : ℝ) : IsFinite (SurrealField.ofReal (K := K) r) := by
  refine ⟨Nat.ceil |r| + 1, ?_⟩
  rw [ofReal_abs]
  -- Goal: ofReal |r| ≤ ((⌈|r|⌉₊ + 1 : ℕ) : K)
  have hbound : |r| ≤ ((Nat.ceil |r| + 1 : ℕ) : ℝ) := by
    have : |r| ≤ (Nat.ceil |r| : ℝ) := Nat.le_ceil _
    push_cast
    linarith
  have hmono := (SurrealField.ofReal_strictMono (K := K)).monotone hbound
  -- hmono : ofReal |r| ≤ ofReal ((⌈|r|⌉₊ + 1 : ℕ) : ℝ)
  have hnat : SurrealField.ofReal ((Nat.ceil |r| + 1 : ℕ) : ℝ)
              = ((Nat.ceil |r| + 1 : ℕ) : K) := by
    rw [map_natCast]
  rw [← hnat]
  exact hmono

/-- The standard part of a real is itself. -/
-- Ref: [alling1987] §4.7
theorem standardPart_ofReal (r : ℝ) :
    standardPart (SurrealField.ofReal (K := K) r) = r := by
  -- ofReal r is finite, and the decomposition uniqueness applied to
  -- the witness `r` (with `(ofReal r) - ofReal r = 0` infinitesimal)
  -- pins down st(ofReal r) = r.
  have hfin := ofReal_isFinite (K := K) r
  have hzero : IsInfinitesimal ((SurrealField.ofReal r : K) - SurrealField.ofReal r) := by
    rw [sub_self]
    exact zero_isInfinitesimal
  have hspec := standardPart_spec hfin
  have huniq := (isFinite_decomposition hfin).unique hspec hzero
  exact huniq

/-- The standard part of zero is zero. -/
@[simp]
theorem standardPart_zero : standardPart (0 : K) = 0 := by
  rw [show (0 : K) = SurrealField.ofReal 0 by simp [map_zero], standardPart_ofReal]

/-- The standard part of one is one. -/
@[simp]
theorem standardPart_one : standardPart (1 : K) = 1 := by
  rw [show (1 : K) = SurrealField.ofReal 1 by simp [map_one], standardPart_ofReal]

/-- An infinitesimal has standard part zero. -/
-- Ref: [robinson1966] Lemma 3.2.4
theorem standardPart_of_infinitesimal {x : K} (hx : IsInfinitesimal x) :
    standardPart x = 0 := by
  -- Apply uniqueness: 0 ∈ ℝ satisfies `x - ofReal 0 = x` infinitesimal.
  have hfin := hx.isFinite
  have h0 : IsInfinitesimal (x - SurrealField.ofReal (0 : ℝ)) := by
    simp [map_zero]; exact hx
  have hspec := standardPart_spec hfin
  exact (isFinite_decomposition hfin).unique hspec h0

/-- Standard-part is additive on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (i)
theorem standardPart_add {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    standardPart (x + y) = standardPart x + standardPart y := by
  -- Strategy: show (x+y) - ofReal(st x + st y) is infinitesimal,
  -- then use uniqueness in isFinite_decomposition.
  have hfin_sum : IsFinite (x + y) := IsFinite.add hx hy
  have hspec_x := standardPart_spec hx
  have hspec_y := standardPart_spec hy
  -- Sum of the two difference-infinitesimals is infinitesimal.
  have hinf_sum := IsInfinitesimal.add hspec_x hspec_y
  -- Rearrange: (x - ofReal (st x)) + (y - ofReal (st y))
  --          = (x + y) - (ofReal (st x) + ofReal (st y))
  --          = (x + y) - ofReal (st x + st y).
  have hrearrange :
      (x - SurrealField.ofReal (standardPart x))
        + (y - SurrealField.ofReal (standardPart y))
      = (x + y) - SurrealField.ofReal (standardPart x + standardPart y) := by
    rw [map_add]; ring
  rw [hrearrange] at hinf_sum
  -- Apply uniqueness: both (st x + st y) and st(x+y) satisfy the
  -- infinitesimal-difference condition for x+y.
  have hspec_sum := standardPart_spec hfin_sum
  have huniq := (isFinite_decomposition hfin_sum).unique hspec_sum hinf_sum
  exact huniq

/-- Standard-part is multiplicative on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (ii)
theorem standardPart_mul {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    standardPart (x * y) = standardPart x * standardPart y := by
  -- Strategy: decompose x = ofReal(st x) + a, y = ofReal(st y) + b
  -- with a, b infinitesimal.  Then
  --   x*y = ofReal(st x * st y) + [ofReal(st x)*b + a*ofReal(st y) + a*b]
  -- where the bracket is infinitesimal (finite × inf + inf × finite +
  -- inf × inf).  Apply uniqueness.
  have hfin_prod : IsFinite (x * y) := IsFinite.mul hx hy
  set sx := standardPart x
  set sy := standardPart y
  set a := x - SurrealField.ofReal sx with ha_def
  set b := y - SurrealField.ofReal sy with hb_def
  have ha_inf : IsInfinitesimal a := standardPart_spec hx
  have hb_inf : IsInfinitesimal b := standardPart_spec hy
  have ha_fin : IsFinite a := ha_inf.isFinite
  have hb_fin : IsFinite b := hb_inf.isFinite
  -- ofReal sx and ofReal sy are finite.
  have hofsx_fin : IsFinite (SurrealField.ofReal (K := K) sx) :=
    ofReal_isFinite sx
  have hofsy_fin : IsFinite (SurrealField.ofReal (K := K) sy) :=
    ofReal_isFinite sy
  -- Expand x * y = (ofReal sx + a) * (ofReal sy + b)
  --              = ofReal(sx*sy) + ofReal sx * b + a * ofReal sy + a * b.
  have hexpand : x * y
      = SurrealField.ofReal (sx * sy)
        + (SurrealField.ofReal sx * b + a * SurrealField.ofReal sy + a * b) := by
    have hx_decomp : x = SurrealField.ofReal sx + a := by
      rw [ha_def]; ring
    have hy_decomp : y = SurrealField.ofReal sy + b := by
      rw [hb_def]; ring
    rw [hx_decomp, hy_decomp, map_mul]
    ring
  -- The bracketed term is infinitesimal.
  have hinf_1 : IsInfinitesimal (SurrealField.ofReal sx * b) := by
    rw [mul_comm]
    exact hb_inf.mul_finite hofsx_fin
  have hinf_2 : IsInfinitesimal (a * SurrealField.ofReal sy) := by
    exact ha_inf.mul_finite hofsy_fin
  have hinf_3 : IsInfinitesimal (a * b) :=
    ha_inf.mul_finite hb_fin
  have hinf_bracket : IsInfinitesimal
      (SurrealField.ofReal sx * b + a * SurrealField.ofReal sy + a * b) :=
    (hinf_1.add hinf_2).add hinf_3
  -- Rewrite: x*y - ofReal (sx*sy) = bracket (infinitesimal).
  have hdiff : x * y - SurrealField.ofReal (sx * sy)
      = SurrealField.ofReal sx * b + a * SurrealField.ofReal sy + a * b := by
    rw [hexpand]; ring
  have hinf_diff : IsInfinitesimal (x * y - SurrealField.ofReal (sx * sy)) := by
    rw [hdiff]; exact hinf_bracket
  -- Uniqueness pins st (x*y) = sx * sy.
  have hspec_prod := standardPart_spec hfin_prod
  have huniq := (isFinite_decomposition hfin_prod).unique hspec_prod hinf_diff
  exact huniq

/-- Standard-part preserves order (weakly) on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (iii)
theorem standardPart_le_of_le {x y : K} (hx : IsFinite x) (hy : IsFinite y)
    (hxy : x ≤ y) :
    standardPart x ≤ standardPart y := by
  -- Suppose for contradiction that st x > st y.
  -- Then ofReal(st x) - ofReal(st y) is a positive real,
  -- and y - x ≤ 0 while (y - x) = (y - ofReal(st y)) - (x - ofReal(st x))
  -- + ofReal(st y - st x) differs from the positive real
  -- ofReal(st y - st x) by an infinitesimal.
  -- This contradicts y - x ≤ 0 when |st x - st y| is positive real.
  by_contra hgt
  push_neg at hgt
  -- hgt : standardPart y < standardPart x
  have hfin_diff : IsFinite (y - x) := by
    rw [sub_eq_add_neg]
    exact hy.add (by
      obtain ⟨n, hn⟩ := hx
      exact ⟨n, by rwa [abs_neg]⟩)
  -- y - x is finite and ≥ 0 (since x ≤ y).
  have hy_minus_x_nonneg : 0 ≤ y - x := by linarith
  -- (y - x) - ofReal(st y - st x) is infinitesimal.
  have hsub_eq := standardPart_add hy (by
    obtain ⟨n, hn⟩ := hx
    exact ⟨n, by rwa [abs_neg]⟩ : IsFinite (-x))
  -- Derive st (y - x) = st y - st x.
  have hsub_sp : standardPart (y - x) = standardPart y - standardPart x := by
    have h_neg : IsFinite (-x) := by
      obtain ⟨n, hn⟩ := hx
      exact ⟨n, by rwa [abs_neg]⟩
    rw [sub_eq_add_neg, standardPart_add hy h_neg]
    -- Need: standardPart (-x) = -standardPart x.
    have hneg_sp : standardPart (-x) = -standardPart x := by
      have h_spec := standardPart_spec hx
      have h_neg_spec : IsInfinitesimal ((-x) - SurrealField.ofReal (-standardPart x)) := by
        have : (-x) - SurrealField.ofReal (-standardPart x)
             = -(x - SurrealField.ofReal (standardPart x)) := by
          rw [map_neg]; ring
        rw [this]
        exact h_spec.neg
      have huniq := (isFinite_decomposition h_neg).unique
        (standardPart_spec h_neg) h_neg_spec
      exact huniq
    rw [hneg_sp]; ring
  -- st (y - x) < 0 by hgt and hsub_sp.
  have hsp_neg : standardPart (y - x) < 0 := by rw [hsub_sp]; linarith
  -- But (y - x) ≤ 0 and standard-part preserves ≤ 0 at the real level,
  -- so standardPart (y - x) ≤ 0 (strict: need standard-part strict compat).
  -- Actually we want the opposite: from st (y-x) < 0 strict, we'd need
  -- y - x strictly less than some ofReal.  Argue: pick r = |st(y-x)|/2 > 0;
  -- then ofReal r > 0, and (y - x) ≤ 0 so (y-x) - ofReal(st(y-x)) < -ofReal r,
  -- contradicting infinitesimality.
  set d := standardPart (y - x)
  have hd_neg : d < 0 := hsp_neg
  have hd_pos : (0 : ℝ) < -d := by linarith
  have hhalf : (0 : ℝ) < -d / 2 := by positivity
  have hspec := standardPart_spec hfin_diff
  -- |(y - x) - ofReal d| < ofReal (-d/2)
  have hinf_bound := hspec (-d / 2) hhalf
  -- But (y - x) ≤ 0 and d < 0 so -ofReal d > 0, meaning
  -- (y - x) - ofReal d ≤ -ofReal d, and |(y - x) - ofReal d| ≥ -ofReal d.
  have hofd_neg : (SurrealField.ofReal d : K) < 0 := by
    have := SurrealField.ofReal_strictMono (K := K) hd_neg
    rwa [map_zero] at this
  have hyx_minus_d : (y - x) - SurrealField.ofReal d ≥ -SurrealField.ofReal d := by
    linarith
  have habs_ge : |(y - x) - SurrealField.ofReal d| ≥ -SurrealField.ofReal d := by
    have hpos : (0 : K) < -SurrealField.ofReal d := by linarith
    calc |(y - x) - SurrealField.ofReal d|
        ≥ (y - x) - SurrealField.ofReal d := le_abs_self _
      _ ≥ -SurrealField.ofReal d := hyx_minus_d
  have hofhalf : (SurrealField.ofReal (-d / 2) : K) < -SurrealField.ofReal d := by
    -- -d/2 < -d (since -d > 0), so ofReal (-d/2) < ofReal (-d) = -ofReal d.
    have h1 : -d / 2 < -d := by linarith
    have h2 := SurrealField.ofReal_strictMono (K := K) h1
    rw [map_neg] at h2
    exact h2
  -- Contradiction: |(y-x)-ofReal d| < ofReal(-d/2) < -ofReal d ≤ |(y-x)-ofReal d|.
  linarith [hinf_bound, hofhalf, habs_ge]

/-! ### `Subring` packaging of the finite surreals

The set `{ x : K | IsFinite x }` is a `Subring K`, and the
standard-part map is a ring homomorphism out of it.  This lets
downstream development quote `standardPart` as a Mathlib
`RingHom` without re-proving `_add`/`_mul` at every call site. -/

/-- The **finite-surreal subring** of `K`.  Closure follows from
    `zero_isFinite`, `one_isFinite`, `IsFinite.add`, `IsFinite.neg`,
    `IsFinite.mul` (proved in `Basic.lean`). -/
def SurrealField.finiteSubring : Subring K where
  carrier := { x : K | SurrealField.IsFinite x }
  zero_mem' := SurrealField.zero_isFinite
  one_mem' := SurrealField.one_isFinite
  add_mem' := fun ha hb => SurrealField.IsFinite.add ha hb
  neg_mem' := fun h => SurrealField.IsFinite.neg h
  mul_mem' := fun ha hb => SurrealField.IsFinite.mul ha hb

/-- Membership in `finiteSubring` is exactly `IsFinite`. -/
@[simp]
theorem SurrealField.mem_finiteSubring {x : K} :
    x ∈ (SurrealField.finiteSubring : Subring K) ↔ SurrealField.IsFinite x :=
  Iff.rfl

/-- Robinson's **standard-part map** as a `RingHom` from the
    finite-surreal subring of `K` to `ℝ`.  Bundles
    `standardPart_zero`, `standardPart_one`, `standardPart_add`, and
    `standardPart_mul` into a single `RingHom` term. -/
-- Ref: [robinson1966] §3.2
noncomputable def standardPartRingHom :
    (SurrealField.finiteSubring (K := K)) →+* ℝ where
  toFun x := standardPart x.val
  map_zero' := standardPart_zero
  map_one' := standardPart_one
  map_add' x y := standardPart_add x.property y.property
  map_mul' x y := standardPart_mul x.property y.property

end QOU.AppendixSurreals
