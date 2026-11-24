import Mathlib.Analysis.Complex.Liouville
import Mathlib.LinearAlgebra.Basis.Defs
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.Algebra.Order.Floor.Defs

/-!
# Liouville for doubly-periodic entire functions

A holomorphic function on `ℂ` that is periodic under two `ℝ`-linearly independent
complex periods is constant — the classical "an elliptic function with no poles is
constant". This is the analytic content the Faddeev–Volkov pentagon rigidity buys
(`QOU.QBeta.CyclicDilogPentagon`): the ratio of two `FaddeevPhi` solutions is
invariant under *both* the compact `ib`-shift and the modular-dual `i/b`-shift, so
where it is entire it is doubly-periodic, hence constant. That is exactly the step
the L4 file carried as the open hypothesis `PentagonRigidity.uniqueUpToScalar` (the
"doubly-periodic ⇒ constant" Liouville input said to be *absent from Mathlib*).

This file supplies that step from Mathlib primitives, closing the *analytic-Liouville*
half of the open input honestly:

* `periodic_zsmul` — periodicity under a period propagates to its integer multiples;
* `const_of_doublyPeriodic` — reducing each `ℝ`-coordinate `b.repr z i` modulo `1`
  (`Int.fract`) lands every `z` in the *bounded* half-open parallelepiped
  `∑ᵢ [0,1)·bᵢ` up to an integer-lattice translation that `f` ignores; that
  parallelepiped sits in a closed ball, compact because `ℂ` is a `ProperSpace`, so the
  range of `f` is bounded and Liouville
  (`Differentiable.exists_const_forall_eq_of_bounded`) forces constancy. No measure
  theory / `ZLattice` machinery — only `Basis.repr`, `Int.fract`, and a closed ball.

What this does **not** do: it does not prove the *ratio is entire* (the zeros of the
two `Φ_b` solutions coincide) or that the two periods are `ℝ`-independent at the
substrate `b` — those remain the genuine analytic-`Φ_b` inputs. It converts the
bespoke `uniqueUpToScalar` hypothesis into two smaller, standard facts (entire ratio +
independent periods), with the Liouville-elliptic step now a proved lemma.

-- Ref: [leitner2026] docs/audits/2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md (G3, Liouville input)
-/

namespace QOU.MathlibExt.DoublyPeriodicLiouville

open Complex Bornology Submodule Module

variable {f : ℂ → ℂ}

/-- **Periodicity under a single period propagates to its integer multiples.** If
`f (z + c) = f z` for all `z`, then `f (z + a • c) = f z` for every `a : ℤ`. -/
theorem periodic_zsmul {c : ℂ} (h : ∀ z, f (z + c) = f z) (a : ℤ) (z : ℂ) :
    f (z + a • c) = f z := by
  induction a using Int.induction_on with
  | zero => simp
  | succ n ih =>
      have hstep : ((n : ℤ) + 1) • c = (n : ℤ) • c + c := add_one_zsmul _ _
      rw [hstep, ← add_assoc, h (z + (n : ℤ) • c), ih]
  | pred n ih =>
      have hstep : (-(n : ℤ) - 1) • c = (-(n : ℤ)) • c - c := sub_one_zsmul _ _
      rw [hstep, ← add_sub_assoc]
      -- `f (w - c) = f w` from `f (w + c) = f w`
      have hsub : ∀ w : ℂ, f (w - c) = f w := by
        intro w; rw [← h (w - c)]; congr 1; ring
      rw [hsub (z + (-(n : ℤ)) • c), ih]

/-- Single-coordinate `fract`/`floor` split for a `ℝ`-scalar acting on `ℂ`:
`Int.fract r • v + ⌊r⌋ • v = r • v` (the integer part is a `ℤ`-multiple, the
fractional part stays in `[0,1)`). -/
theorem fract_smul_add_floor_zsmul (r : ℝ) (v : ℂ) :
    Int.fract r • v + (⌊r⌋ : ℤ) • v = r • v := by
  rw [← Int.cast_smul_eq_zsmul ℝ ⌊r⌋ v, ← add_smul, Int.fract_add_floor]

/-- **Liouville for doubly-periodic entire functions.** A differentiable
`f : ℂ → ℂ` periodic under both vectors of an `ℝ`-basis `b` of `ℂ` is constant.
Reducing the two `ℝ`-coordinates of `z` modulo `1` lands `z`, up to a lattice
translation `f` ignores, in the closed ball of radius `‖b 0‖ + ‖b 1‖`; that ball is
compact (`ℂ` proper), so `range f` is bounded and Liouville forces a constant. -/
theorem const_of_doublyPeriodic {b : Basis (Fin 2) ℝ ℂ}
    (hf : Differentiable ℂ f)
    (h : ∀ i, ∀ z, f (z + b i) = f z) :
    ∃ c, ∀ z, f z = c := by
  set M : ℝ := ‖b 0‖ + ‖b 1‖ with hM
  have hsub : Set.range f ⊆ f '' (Metric.closedBall 0 M) := by
    rintro _ ⟨z, rfl⟩
    set r0 := b.repr z 0 with hr0
    set r1 := b.repr z 1 with hr1
    set z0 : ℂ := Int.fract r0 • b 0 + Int.fract r1 • b 1 with hz0
    have hfract0 : |Int.fract r0| ≤ 1 :=
      abs_le.mpr ⟨by linarith [Int.fract_nonneg r0], le_of_lt (Int.fract_lt_one r0)⟩
    have hfract1 : |Int.fract r1| ≤ 1 :=
      abs_le.mpr ⟨by linarith [Int.fract_nonneg r1], le_of_lt (Int.fract_lt_one r1)⟩
    refine ⟨z0, ?_, ?_⟩
    · rw [Metric.mem_closedBall, dist_zero_right, hz0]
      calc ‖Int.fract r0 • b 0 + Int.fract r1 • b 1‖
          ≤ ‖Int.fract r0 • b 0‖ + ‖Int.fract r1 • b 1‖ := norm_add_le _ _
        _ = |Int.fract r0| * ‖b 0‖ + |Int.fract r1| * ‖b 1‖ := by
            rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
        _ ≤ 1 * ‖b 0‖ + 1 * ‖b 1‖ :=
            add_le_add (mul_le_mul_of_nonneg_right hfract0 (norm_nonneg _))
              (mul_le_mul_of_nonneg_right hfract1 (norm_nonneg _))
        _ = M := by rw [one_mul, one_mul, hM]
    · have hzsum : z0 + ((⌊r0⌋ : ℤ) • b 0 + (⌊r1⌋ : ℤ) • b 1) = z := by
        rw [hz0]
        have hrepr : r0 • b 0 + r1 • b 1 = z := by
          rw [hr0, hr1, ← Fin.sum_univ_two (fun i => b.repr z i • b i), b.sum_repr z]
        rw [← hrepr, ← fract_smul_add_floor_zsmul r0 (b 0),
          ← fract_smul_add_floor_zsmul r1 (b 1)]
        abel
      rw [← hzsum, ← add_assoc,
        periodic_zsmul (h 1) ⌊r1⌋ (z0 + (⌊r0⌋ : ℤ) • b 0),
        periodic_zsmul (h 0) ⌊r0⌋ z0]
  have hbdd : IsBounded (f '' Metric.closedBall 0 M) :=
    ((isCompact_closedBall (0 : ℂ) M).image hf.continuous).isBounded
  exact hf.exists_const_forall_eq_of_bounded (hbdd.subset hsub)

/-- **Rigidity bridge — the reduced form of `PentagonRigidity.uniqueUpToScalar`.**
If two entire functions `Φ, Ψ` with `Φ` nowhere zero have a ratio that is genuinely
periodic (prefactors cancelled) under both vectors of an `ℝ`-basis of `ℂ`, then
`Ψ = c · Φ` for a constant `c`. This is exactly the Faddeev–Volkov rigidity content
the L4 pentagon file (`QOU.QBeta.CyclicDilogPentagon`) carried as an open hypothesis:
the two remaining inputs are now explicit and *smaller* — `Ψ/Φ` is entire (the zeros
coincide) and the two quasi-period ratios cancel to genuine periods with independent
periods (`b` a basis) — while the doubly-periodic ⇒ constant Liouville step is proved
above. -/
theorem ratio_const_of_doublyPeriodic {Φ Ψ : ℂ → ℂ} {b : Basis (Fin 2) ℝ ℂ}
    (hΦ : Differentiable ℂ Φ) (hΨ : Differentiable ℂ Ψ) (hΦ0 : ∀ z, Φ z ≠ 0)
    (hper : ∀ i, ∀ z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z) :
    ∃ c, ∀ z, Ψ z = c * Φ z := by
  have hdiff : Differentiable ℂ (fun z => Ψ z / Φ z) := hΨ.div hΦ hΦ0
  obtain ⟨c, hc⟩ := const_of_doublyPeriodic hdiff hper
  exact ⟨c, fun z => (div_eq_iff (hΦ0 z)).mp (hc z)⟩

/-- **Rigidity bridge, divisor form — the shape the Faddeev application actually
has.** `ratio_const_of_doublyPeriodic` above requires `Φ` to be *nowhere zero*.
Faddeev's quantum dilogarithm `Φ_b` does **not** satisfy that: it is meromorphic
with a genuine zero/pole lattice (poles at `c_b + i(mb + nb⁻¹)`, zeros at the
reflected lattice), so the bridge as stated does not apply to it directly — a
hypothesis/application mismatch worth naming rather than working around.

What the open input `hratio` (bean `qou-cons`) actually delivers is weaker and
better matched: two `FaddeevPhi` solutions **share** their divisor, so the
*ratio* is entire even though neither factor is zero-free. This variant takes
exactly that as its hypothesis, and is therefore the form a discharged `hratio`
plugs into. Together with `hibinv` (bean `qou-rp5f`, supplying `hper` off the
dual pole lattice) it yields constancy of the ratio.

Strictly weaker than `ratio_const_of_doublyPeriodic`: it assumes nothing about
the zeros of `Φ`, and correspondingly concludes about the ratio rather than
about `Ψ` pointwise (see `eq_const_mul_of_entire_ratio` for the pointwise form
away from the divisor). -/
theorem ratio_const_of_entire_ratio {Φ Ψ : ℂ → ℂ} {b : Basis (Fin 2) ℝ ℂ}
    (hr : Differentiable ℂ (fun z => Ψ z / Φ z))
    (hper : ∀ i, ∀ z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z) :
    ∃ c, ∀ z, Ψ z / Φ z = c :=
  const_of_doublyPeriodic hr hper

/-- Pointwise form of `ratio_const_of_entire_ratio`, valid **off the divisor**:
wherever `Φ` is nonzero, `Ψ = c · Φ` with the same constant. This is how the
rigidity conclusion is consumed in practice — the identity is asserted on the
complement of the pole/zero lattice, not on all of `ℂ`. -/
theorem eq_const_mul_of_entire_ratio {Φ Ψ : ℂ → ℂ} {b : Basis (Fin 2) ℝ ℂ}
    (hr : Differentiable ℂ (fun z => Ψ z / Φ z))
    (hper : ∀ i, ∀ z, Ψ (z + b i) / Φ (z + b i) = Ψ z / Φ z) :
    ∃ c, ∀ z, Φ z ≠ 0 → Ψ z = c * Φ z := by
  obtain ⟨c, hc⟩ := ratio_const_of_entire_ratio hr hper
  exact ⟨c, fun z hz => (div_eq_iff hz).mp (hc z)⟩

end QOU.MathlibExt.DoublyPeriodicLiouville
