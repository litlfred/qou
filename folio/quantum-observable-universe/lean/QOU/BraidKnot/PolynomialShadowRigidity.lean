import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Algebra.Polynomial.Roots

/-!
# Rigidity of the polynomial / rational shadow from its root-of-unity values

`QOU/BraidKnot/BWVacuumRowHabiroRigidity.lean` states the keystone's "rigidity ⇒
no fit" content as a §3b class `HabiroRigidity`, whose content field
`root_injective` is **Habiro's injectivity theorem, carried as an unproved
hypothesis**. This file discharges that hypothesis — *not* for the Habiro ring,
but for the carrier the keystone's actual candidate lives on, where the same
conclusion is elementary and provable.

## Why the carrier matters (the dichotomy this file resolves)

The candidate boundary datum of `computations/habiro_interpolation_wlambda.py` is

    F_λ(q) = [mark λ]²_q / D(q)²,     D(q)² = Σ_{9 McKay nodes} [mark μ]²_q

Since `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`, the `(q − q⁻¹)` factors cancel and `F_λ` is
a **ratio of Laurent polynomials with integer coefficients** — as bean `qou-2v7k`
already recorded ("`d_q = [mark]_q` is a global Laurent polynomial, `Z(q)` is
rational; continuation is trivial"). That splits the two carriers cleanly:

| carrier | rigidity from root values | evaluable at `q₀ ≈ 1.10998` |
|---|---|---|
| Habiro ring `Ẑ[q]` | yes (Habiro injectivity, unproved here) | **no** — `HabiroDomainVanishing.lean` |
| polynomial / rational shadow | **yes — proved below** | yes (it is a rational function) |

The Habiro ring is *not* `q₀`-evaluable: its `(q;q)_k`-adic completion diverges at
real `q > 1`, which is the content of `qPochSelf_ne_zero_of_no_root_of_unity` in
`HabiroDomainVanishing.lean`. So the `evalQ0` field of `HabiroRigidity` is not
innocuous on that carrier — it postulates a map that does not exist there. On the
rational shadow, by contrast, both columns hold, and the rigidity needs no
miracle: it is `Polynomial.eq_of_infinite_eval_eq` plus the infinitude of the
roots of unity.

## What is proved here (sorry-free)

* `Complex.setOf_isRootOfUnity_infinite` — the roots of unity in `ℂ` form an
  infinite set. Proved by injecting `ℕ`, `n ↦ exp(2πi/(n+1))`, injective because a
  primitive `k`-th root has multiplicative order exactly `k`.
* `eq_of_eval_eq_on_rootsOfUnity` — two polynomials agreeing at every root of
  unity are **equal as polynomials**.
* `eval_eq_of_agree_on_rootsOfUnity` — hence they agree at *every* point, in
  particular at the substrate anchor `q₀`. This is the honest, unconditional
  analogue of `q0_value_unique`.
* `mul_eq_of_ratio_agree_on_rootsOfUnity` / `ratio_eval_eq_of_mul_eq` — the same
  for a **ratio** `N/D`, which is the shape `F_λ` actually has: agreement at the
  roots of unity forces `N₁·D₂ = N₂·D₁`, hence equal values wherever both
  denominators are nonzero.

## What this does NOT do — the gate stays open, and by a measured margin

This proves rigidity from agreement at **all** roots of unity, of which there are
infinitely many. The Σ(2,3,5) fibre geometry supplies **five** values and cannot
supply more: the Poincaré sphere has exactly three exceptional fibres
`(p₁,p₂,p₃) = (2,3,5)` and exactly two irreducible `SU(2)` flat connections
(`D(2,3,5) = 2`, Fintushel–Stern), and since `ℓ₂ = ℓ₃ = 1` for both connections
that is 1 + 1 + 2 = 4 nontrivial roots, plus `q = 1`.

Five is not close to enough, and the shortfall is quantitative rather than a
matter of computing harder. Reducing `F_λ = (q^m − q^{−m})² / Σ_μ (q^{m_μ} −
q^{−m_μ})²` to lowest terms (marks `1,2,3,4,5,6,4,2,3`) gives, per mark `m`:

    m:            1    2    3    4    5    6
    deg numer:   10   12   14   16   18   20
    deg denom:   20   20   20   20   20   20
    values to pin (deg N + deg D + 1):  31   33   35   37   39   41

So elementary rigidity on the rational shadow needs **31–41** values where the
geometry offers **5**. The interpolation probe's own docstring says the roots
"CONSTRAIN but do not UNIQUELY PIN `F_λ`"; the table above is that statement made
numerical. Closing the gate therefore requires *either* a source of ~26+ further
independent values that is not the three exceptional fibres, *or* a bridge
showing the WRT Habiro element and the rational shadow agree at all roots of
unity — at which point the theorems below, not Habiro's theorem, supply the
rigidity.

Scope-(a) throughout: this constrains what the *fibre data* can pin. It excludes
no ingredient and refutes no route.

-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-- Ref: [fintushelstern1990] https://doi.org/10.1112/plms/s3-61.1.109
-- Ref: [leitner2026] docs/audits/2026-07-17-habiro-interpolation-wlambda.md
-/

namespace QOU.BraidKnot.Keystone

open Polynomial

/-- `z` is a root of unity: some strictly positive power of it is `1`. -/
def IsRootOfUnity (z : ℂ) : Prop := ∃ n : ℕ, 0 < n ∧ z ^ n = 1

/-- The explicit primitive `(n+1)`-st roots of unity, used to inject `ℕ` into the
set of roots of unity. -/
private noncomputable def zeta (n : ℕ) : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / ((n : ℂ) + 1))

private theorem isPrimitiveRoot_zeta (n : ℕ) : IsPrimitiveRoot (zeta n) (n + 1) := by
  have h : ((n : ℂ) + 1) = ((n + 1 : ℕ) : ℂ) := by push_cast; ring
  rw [zeta, h]
  exact Complex.isPrimitiveRoot_exp (n + 1) (Nat.succ_ne_zero n)

private theorem zeta_injective : Function.Injective zeta := by
  intro n m h
  have hn : n + 1 = orderOf (zeta n) := (isPrimitiveRoot_zeta n).eq_orderOf
  have hm : m + 1 = orderOf (zeta m) := (isPrimitiveRoot_zeta m).eq_orderOf
  rw [h] at hn
  omega

/-- **The roots of unity in `ℂ` are infinite.** This is the input that makes the
rigidity below elementary: a polynomial identity may be tested on them. -/
theorem setOf_isRootOfUnity_infinite : {z : ℂ | IsRootOfUnity z}.Infinite := by
  refine Set.infinite_of_injective_forall_mem (f := zeta) zeta_injective ?_
  intro n
  exact ⟨n + 1, Nat.succ_pos n, (isPrimitiveRoot_zeta n).pow_eq_one⟩

/-- **Rigidity of the polynomial shadow.** Two polynomials over `ℂ` that agree at
every root of unity are equal. Contrast `HabiroRigidity.root_injective`, which
asserts the analogous statement for the Habiro ring as an unproved hypothesis:
here it is a theorem, because the carrier is a polynomial ring and the roots of
unity are an infinite test set. -/
theorem eq_of_eval_eq_on_rootsOfUnity {p q : Polynomial ℂ}
    (h : ∀ z : ℂ, IsRootOfUnity z → p.eval z = q.eval z) : p = q := by
  refine Polynomial.eq_of_infinite_eval_eq p q ?_
  exact setOf_isRootOfUnity_infinite.mono (fun z hz => h z hz)

/-- **The value is forced — unconditionally.** If two polynomial shadows carry the
same root-of-unity data then they take the same value at *every* point, in
particular at the substrate anchor `q₀`. This is the honest analogue of
`q0_value_unique`: same conclusion, no class hypothesis. -/
theorem eval_eq_of_agree_on_rootsOfUnity {p q : Polynomial ℂ}
    (h : ∀ z : ℂ, IsRootOfUnity z → p.eval z = q.eval z) (x : ℂ) :
    p.eval x = q.eval x := by
  rw [eq_of_eval_eq_on_rootsOfUnity h]

/-- **Rigidity for a ratio**, which is the shape `F_λ = [mark]²_q / D(q)²` has.
Agreement of the two quotients at every root of unity (where the denominators are
nonzero) forces the cross-multiplied polynomial identity. -/
theorem mul_eq_of_ratio_agree_on_rootsOfUnity {n₁ d₁ n₂ d₂ : Polynomial ℂ}
    (hd₁ : ∀ z : ℂ, IsRootOfUnity z → d₁.eval z ≠ 0)
    (hd₂ : ∀ z : ℂ, IsRootOfUnity z → d₂.eval z ≠ 0)
    (h : ∀ z : ℂ, IsRootOfUnity z → n₁.eval z / d₁.eval z = n₂.eval z / d₂.eval z) :
    n₁ * d₂ = n₂ * d₁ := by
  refine eq_of_eval_eq_on_rootsOfUnity ?_
  intro z hz
  have h₁ := hd₁ z hz
  have h₂ := hd₂ z hz
  have hz' := h z hz
  field_simp at hz'
  simp only [Polynomial.eval_mul]
  linear_combination hz'

/-- The cross-multiplied identity transports the value to any point where both
denominators are nonzero — the substrate anchor included. -/
theorem ratio_eval_eq_of_mul_eq {n₁ d₁ n₂ d₂ : Polynomial ℂ}
    (hmul : n₁ * d₂ = n₂ * d₁) {x : ℂ} (h₁ : d₁.eval x ≠ 0) (h₂ : d₂.eval x ≠ 0) :
    n₁.eval x / d₁.eval x = n₂.eval x / d₂.eval x := by
  have := congrArg (Polynomial.eval x) hmul
  simp only [Polynomial.eval_mul] at this
  field_simp
  linear_combination this

end QOU.BraidKnot.Keystone
