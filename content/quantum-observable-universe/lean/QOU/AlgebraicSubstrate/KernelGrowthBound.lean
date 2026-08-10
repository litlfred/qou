import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.AlgebraicSubstrate.KernelGrowthBound — growth from the kernel, algebraically

**The claim being made good.**
[`prop:binding-genfun-qdifference`](../../../quantum-observable-universe/mass-theory/binding-genfun-qdifference.md)
states that if the binding generating function satisfies a fibre-level
q-difference equation `G(qx;q) = R(q,x)·G(x;q)` of bounded depth `d`, then the
body terms obey a depth-`d` linear recurrence, and — its words —

> *the empirical "ρ·A" scale rule governing the growth of the terms is the
> **solution of the recurrence — an output of `R`, not a fitted constant***.

This file proves that growth statement for depth 2, from the kernel alone. The
input is **algebraic** (two coefficients of the recurrence); the output is an
**archimedean growth bound** on every solution. No analysis, no limit, no
standard-part map — the bound falls out of the recursion by induction.

That is the shape asked for: *most of the work on the algebraic side.*

## ⚠ This is the **slope-0** case — corrected 2026-08-10

An earlier draft of this docstring claimed *"the minimal colored-Jones recursion
for `4₁` has order 2, so a depth-2 kernel is exactly the `4₁` case."* **That was
an overclaim and is withdrawn.** Two independent reasons:

1. **Constant vs. `n`-dependent coefficients.** The theorem below fixes `a₀, a₁`
   once and for all. The colored-Jones recursion's coefficients are functions of
   `qⁿ`, so it is *not* an instance of this theorem regardless of its order.
2. **Wrong growth shape — the slope.** For a genuine q-difference equation the
   relevant invariant is the **q-Gevrey order** (the Newton polygon's *q-slope*),
   and `QOU.Mathlib.QGevreyOrder.IsQGevreyOrder q s a` records what that means:
   `‖aₙ‖ ∼ Cⁿ · q^{s·n²/2}` — **super-geometric**, with `n²` in the exponent.
   `growth_bound_depth2` concludes `|Bₙ| ≤ C·Rⁿ`, which is purely geometric. So
   it is precisely the **`s = 0`** corner of that scale and says nothing about a
   positive-slope solution.

**Where it does apply, and it is not vacuous:** a recursion whose kernel is
*constant in the index*. The corpus has one —
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../../quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md):
`c_{k+1} = Σ_{j=1}^{d} a_j(q₀)·c_{k+1-j}` with `a_j(q₀) ∈ ℚ(q₀)`, fixed in `k`.
That is slope 0 and squarely in scope.

**A tension that same block raises**, worth settling with the slope: it also says
the `c_k` *"obey the q-Bessel second-order q-difference equation"* (Hahn–Exton,
fibre-level). A constant-kernel linear recursion has slope 0; a genuine
second-order q-difference equation generically does not. Those are different
growth classes, so either the q-Bessel equation degenerates at `q₀` or the two
sentences describe different objects. The q-Gevrey order is exactly the
invariant that decides it. Recorded, not resolved here.

## Newton-polygon reading

`R := |a₀| + |a₁|` is the crudest supporting functional on the kernel's Newton
polygon — the `ℓ¹` bound, i.e. the horizontal face. `growth_bound_depth2` says
that face already bounds the growth exponent. Sharper faces (the actual lower
hull, giving the characteristic roots) give sharper exponents; that refinement
is the content of `PolyhedralDomination.Face`, and picking the face is picking
which bound you get.

**Worked calibration of exactly that, already in the corpus.** The Morgan–Voyce
continuant of the lepton tower ([`lepton-continuant-recurrence`](../../../quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md))
is `b_{n+1} = h·b_n + b_{n-1}` with `h = q − q⁻¹` — constant kernel, slope 0, in
scope here. The `ℓ¹` face gives `R = 1 + |h| ≈ 1.209` at `q₀`. The *sharp* face
gives the characteristic roots of `x² − (q−q⁻¹)x − 1`, which are exactly `q` and
`−q⁻¹` — the Hecke eigenvalues — so the true rate is `q₀ ≈ 1.110`.
`QOU.Archimedean.lepton_continuant_binet` already proves the resulting exact
Binet form `bₙ·(q+q⁻¹) = qⁿ − (−1)ⁿq⁻ⁿ`, sorry-free. That is **stronger than
anything this file provides for that sequence**, and is the concrete measure of
how much the crude face costs.

## Connection to the surreal side (`ordω` as a growth tracker)

The corpus tracks bounded growth on the archimedean side with
`QOU.AppendixSurreals.OmegaOrder` (`Asymptotics.lean`): `Ow` is an `ω`-adic
order, `x ≼ y := Ow x ≤ Ow y` is surreal Big-O and `x ≺ y` is little-o. Its
axiom `Ow_ofReal_mul` — *rescaling by a non-zero real leaves the leading
exponent unchanged* — is exactly the blindness that
`QOU.Archimedean.SurrealGradingPrune.grade_eq_of_pos` shows is **forced**, not
optional: `ℝ` is one archimedean class, so no grading can separate inside it.
`ow_const_on_rescales` below records that consequence abstractly.

So the two sides line up: `ordω` classifies growth but cannot see real
constants; the kernel supplies the actual constant. Growth *rate* is algebraic
(kernel/polygon); growth *scale* is archimedean and must come from elsewhere.

## Scope — what is NOT done

The specific kernel `R` for the QOU binding generating function **does not
exist yet**: `prop:binding-genfun-qdifference` says so itself — *"What is open
is the existence and identity of the kernel `R` for the binding `G`"*, and it
adds that `R` may **not** be fixed by fitting the `Bₙ` (the `c_k` information
bound), but must be derived from the fibre root-of-unity singularity structure.

So this file supplies the machine, not a `4₁`/`5₂` binding instance. Feeding it
a real kernel is blocked at that stated gap, not at anything here.
-/

namespace QOU.AlgebraicSubstrate

/-! ## §1  Growth from a depth-2 kernel -/

/-- **Growth bound from the kernel alone.**

For any solution of the depth-2 recurrence `B(n+2) = a₁·B(n+1) + a₀·B(n)`, if
the initial window is bounded by `C` and `R ≥ 1` dominates the kernel's `ℓ¹`
norm `|a₀| + |a₁|`, then `|B n| ≤ C·Rⁿ` for every `n`.

The growth exponent is read off the **coefficients**; nothing about the
solution's analytic behaviour is used. This is the depth-2 case of
`prop:binding-genfun-qdifference`(1): the scale rule is an output of the
kernel, not a fitted constant. -/
theorem growth_bound_depth2 (a₀ a₁ C R : ℝ) (B : ℕ → ℝ)
    (hrec : ∀ n, B (n + 2) = a₁ * B (n + 1) + a₀ * B n)
    (hR1 : 1 ≤ R) (hker : |a₀| + |a₁| ≤ R)
    (h0 : |B 0| ≤ C) (h1 : |B 1| ≤ C) :
    ∀ n, |B n| ≤ C * R ^ n := by
  have hC : 0 ≤ C := le_trans (abs_nonneg _) h0
  have hR0 : (0 : ℝ) ≤ R := le_trans zero_le_one hR1
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 => simpa using h0
    | 1 => simpa using (by nlinarith [h1, hR1, hC] : |B 1| ≤ C * R ^ 1)
    | (m + 2) =>
        have hm1 : |B (m + 1)| ≤ C * R ^ (m + 1) := ih (m + 1) (by omega)
        have hm0 : |B m| ≤ C * R ^ m := ih m (by omega)
        have hpow : (0 : ℝ) ≤ R ^ m := pow_nonneg hR0 m
        -- `|B (m+2)| ≤ |a₁|·|B(m+1)| + |a₀|·|B m| ≤ (|a₀|+|a₁|)·C·R^(m+1)`
        have hstep : |B (m + 2)| ≤ |a₁| * |B (m + 1)| + |a₀| * |B m| := by
          rw [hrec m]
          calc |a₁ * B (m + 1) + a₀ * B m|
              ≤ |a₁ * B (m + 1)| + |a₀ * B m| := abs_add_le _ _
            _ = |a₁| * |B (m + 1)| + |a₀| * |B m| := by rw [abs_mul, abs_mul]
        have hb1 : |a₁| * |B (m + 1)| ≤ |a₁| * (C * R ^ (m + 1)) :=
          mul_le_mul_of_nonneg_left hm1 (abs_nonneg _)
        have hb0 : |a₀| * |B m| ≤ |a₀| * (C * R ^ (m + 1)) := by
          refine mul_le_mul_of_nonneg_left (hm0.trans ?_) (abs_nonneg _)
          have : R ^ m ≤ R ^ (m + 1) := by
            simpa [pow_succ] using
              (le_mul_of_one_le_right hpow hR1)
          nlinarith [this, hC]
        have hsum : |B (m + 2)| ≤ (|a₀| + |a₁|) * (C * R ^ (m + 1)) := by
          nlinarith [hstep, hb0, hb1]
        have hfin : (|a₀| + |a₁|) * (C * R ^ (m + 1)) ≤ R * (C * R ^ (m + 1)) := by
          refine mul_le_mul_of_nonneg_right hker ?_
          positivity
        calc |B (m + 2)| ≤ (|a₀| + |a₁|) * (C * R ^ (m + 1)) := hsum
          _ ≤ R * (C * R ^ (m + 1)) := hfin
          _ = C * R ^ (m + 2) := by ring

/-- **Sub-geometric kernels give bounded solutions.** If the kernel's `ℓ¹` norm
is at most `1`, no solution can grow at all — the bound is uniform in `n`.

The contrapositive is the useful direction for an obstruction argument: an
*unbounded* solution certifies `|a₀| + |a₁| > 1`, a purely algebraic conclusion
drawn from archimedean data. -/
theorem bounded_of_kernel_le_one (a₀ a₁ C : ℝ) (B : ℕ → ℝ)
    (hrec : ∀ n, B (n + 2) = a₁ * B (n + 1) + a₀ * B n)
    (hker : |a₀| + |a₁| ≤ 1) (h0 : |B 0| ≤ C) (h1 : |B 1| ≤ C) :
    ∀ n, |B n| ≤ C := by
  intro n
  simpa using growth_bound_depth2 a₀ a₁ C 1 B hrec le_rfl (by simpa using hker) h0 h1 n

/-! ## §2  `ordω` cannot supply the constant

The abstract form of `OmegaOrder.Ow_ofReal_mul` (`Asymptotics.lean`): a grading
invariant under rescaling assigns one value to a whole rescaling orbit. So the
growth *class* is visible to `ordω` while the growth *constant* is not — the
constant has to come from the kernel, which is what §1 provides. -/

/-- If a grading is invariant under rescaling by non-zero reals, then every
rescaling of an element shares its grade: `ordω` sees the growth class, never
the constant.

This is `OmegaOrder.Ow_ofReal_mul` stated without the surreal-field scaffolding,
and it is the same phenomenon `SurrealGradingPrune` proves is *forced* rather
than assumed. -/
theorem ow_const_on_rescales {K Γ : Type*} (Ow : K → Γ) (scale : ℝ → K → K)
    (hinv : ∀ (r : ℝ), r ≠ 0 → ∀ x, Ow (scale r x) = Ow x)
    (r s : ℝ) (hr : r ≠ 0) (hs : s ≠ 0) (x : K) :
    Ow (scale r x) = Ow (scale s x) := by
  rw [hinv r hr, hinv s hs]

end QOU.AlgebraicSubstrate
