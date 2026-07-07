/-
Copyright (c) 2026 litlfred. All rights reserved.

# z → c_k f-map keystone — bar-parity of the z-side atoms (the z-alone exclusion)

Formalize-first structural narrowing for the **z→c_k f-map keystone**
(ledger `docs/coordination/z-ck-fmap-keystone.md`, bean `ea56`, PR #3449).

The proved pre-archimedean backbone feeding the open f-map is the Markov
parameter `z(q) = √q/(1+q)` (3-term recursion, PR #1739; bridge block
`prop:qbeta-z-recursion-to-ck-recursion-bridge`). The open c_k-recursion
kernel must have a **bar-ODD leading coefficient** `a₁ = −c₃`
(`QOU.BraidKnot.QBetaCKRecursionKernelConstraints.ck_a1_bar_odd`).

This file proves the parity bookkeeping of the z-side atoms under the fibre
bar involution (`q ↦ q⁻¹`, in the half-power coordinate `s ↦ s⁻¹`, `s² = q`):

1. `z_bar_invariant` — **`z` is exactly bar-EVEN** (twist `1`):
   `z(q⁻¹) = z(q)`. Division-free over any `CommRing`.
2. `hbar_bar_odd_twist` / `hbar_sq_bar_even_twist` — `ℏ_q = 1 − q⁻¹` is
   bar-odd up to the monomial twist `−q`; hence `ℏ_q²` (the ladder variable
   `u = b·ℏ_q²`) is bar-even up to twist `q²`.
3. `kappa21_bar_odd` — the (2,1)-block heat carrier
   `κ_{(2,1)} = (q−1)³(q+1)/q²` is **exactly bar-ODD** (twist `1`), the Lean
   certificate of the sympy-exact finding in
   `docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md` §1.
4. `bar_even_mul_bar_odd` and the exclusion
   `bar_even_and_odd_two_mul_eq_zero` / `bar_even_ne_bar_odd_of_ne_zero` —
   a bar-even scalar can never equal a bar-odd nonzero element
   (characteristic ≠ 2).

**Consequence (the z-alone exclusion, scope-(a)):** every scalar functional
built from `z` alone by ring operations (sums, products, powers — the
bar-fixed locus of the involution is a subring, `bar_fixed_add`/`_mul`/`_pow`)
is bar-EVEN; the kernel's leading coefficient `a₁` is bar-ODD and nonzero
(`a₁ = −c₃`, `c₃ ≈ 2.07 ≠ 0` empirically). Hence **no scalar rational
function of `z` alone can source `a₁`** — the surviving z→c_k f-map class
factors as (bar-even z-functional) × (bar-odd carrier), converging with the
(2,1) mode-selectivity of the heat route. This narrows the `ea56` hypothesis
class; it derives **no** c_k value, changes **no** registry tier, and wires
**nothing** (flip-flop guard §8).

Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-! ## §1. The Markov parameter `z = s/(1+s²)` is bar-invariant (`s² = q`) -/

/-- Numerator of the Markov parameter `z = √q/(1+q)` in the half-power
    coordinate `s` (`s² = q`): `zNum s = s`. -/
def zNum (s : R) : R := s

/-- Denominator of the Markov parameter: `zDen s = 1 + s²` (`= 1 + q`). -/
def zDen (s : R) : R := 1 + s ^ 2

/-- **`z` is exactly bar-EVEN (division-free, over any `CommRing`).** Under the
    bar involution `s ↦ s⁻¹` — witnessed by `s·si = 1` — the cross-multiplied
    identity `zNum si · zDen s = zNum s · zDen si` holds, i.e. `z(s⁻¹) = z(s)`
    with twist exactly `1`. In `q`-language: `z(q⁻¹) = z(q)` for
    `z = √q/(1+q)`. -/
theorem z_bar_invariant (s si : R) (h : s * si = 1) :
    zNum si * zDen s = zNum s * zDen si := by
  unfold zNum zDen
  linear_combination (s - si) * h

/-- `Field` corollary of `z_bar_invariant` in literal `a/b` form. Only
    `s ≠ 0` is needed: when `1 + s² = 0` both sides are `0` under Mathlib's
    division convention, so the identity is unconditional in the
    denominator. -/
theorem z_bar_invariant_field {F : Type*} [Field F] (s : F) (hs : s ≠ 0) :
    s⁻¹ / (1 + s⁻¹ ^ 2) = s / (1 + s ^ 2) := by
  have key : 1 + s⁻¹ ^ 2 = (1 + s ^ 2) / s ^ 2 := by
    field_simp
    ring
  have hmul : s⁻¹ * s ^ 2 = s := by
    field_simp
  rw [key, div_div_eq_mul_div, hmul]

/-! ## §2. The ladder variable's parity: `ℏ_q` bar-odd (twist `−q`), `ℏ_q²` bar-even (twist `q²`) -/

/-- **`ℏ_q = 1 − q⁻¹` is bar-ODD up to the monomial twist `−q`.** In the
    `(q, qi)` encoding (`q·qi = 1`, `ℏ = 1 − qi`, `bar(ℏ) = 1 − q`):
    `bar(ℏ) = −q·ℏ`. -/
theorem hbar_bar_odd_twist (q qi : R) (h : q * qi = 1) :
    1 - q = -(q * (1 - qi)) := by
  linear_combination -h

/-- **`ℏ_q²` is bar-EVEN up to the monomial twist `q²`.** Squaring
    `hbar_bar_odd_twist`: `bar(ℏ²) = q²·ℏ²`. Hence the ladder variable
    `u = b·ℏ_q²` (with `b` a bar-fixed constant) is bar-even up to `q²` —
    integer `u`-rungs carry even bar-parity content, and any bar-ODD ladder
    coefficient must be sourced by a genuinely bar-odd carrier, not by the
    variable itself. -/
theorem hbar_sq_bar_even_twist (q qi : R) (h : q * qi = 1) :
    (1 - q) ^ 2 = q ^ 2 * (1 - qi) ^ 2 := by
  have h1 := hbar_bar_odd_twist q qi h
  calc (1 - q) ^ 2 = (-(q * (1 - qi))) ^ 2 := by rw [h1]
    _ = q ^ 2 * (1 - qi) ^ 2 := by ring

/-! ## §3. The (2,1) heat carrier `κ_{(2,1)} = (q−1)³(q+1)/q²` is exactly bar-ODD -/

/-- Numerator of the (2,1)-block heat carrier: `(q−1)³(q+1)`. -/
def kappaNum (q : R) : R := (q - 1) ^ 3 * (q + 1)

/-- Denominator of the (2,1)-block heat carrier: `q²`. -/
def kappaDen (q : R) : R := q ^ 2

/-- **`κ_{(2,1)}` is exactly bar-ODD (division-free, over any `CommRing`).**
    Cross-multiplied form of `κ(q⁻¹) = −κ(q)` for
    `κ(q) = (q−1)³(q+1)/q²`: the Lean certificate of the sympy-exact
    `bar(κ)+κ = 0` in the 2026-06-13 heat f-map audit §1. -/
theorem kappa21_bar_odd (q qi : R) (h : q * qi = 1) :
    kappaNum qi * kappaDen q = -(kappaNum q * kappaDen qi) := by
  unfold kappaNum kappaDen
  have e1 : qi - 1 = -(qi * (q - 1)) := by linear_combination h
  have e2 : qi + 1 = qi * (q + 1) := by linear_combination -h
  rw [e1, e2]
  linear_combination (-(q - 1) ^ 3 * (q + 1) * qi ^ 2 * (q * qi + 1)) * h

/-! ## §4. Parity algebra: the bar-fixed locus is a subring; even cannot equal odd -/

variable (σ : R →+* R)

/-- Bar-fixed elements are closed under addition. -/
theorem bar_fixed_add (a b : R) (ha : σ a = a) (hb : σ b = b) :
    σ (a + b) = a + b := by rw [map_add, ha, hb]

/-- Bar-fixed elements are closed under multiplication. -/
theorem bar_fixed_mul (a b : R) (ha : σ a = a) (hb : σ b = b) :
    σ (a * b) = a * b := by rw [map_mul, ha, hb]

/-- Bar-fixed elements are closed under powers: every monomial `zᵐ` of a
    bar-even atom is bar-even. -/
theorem bar_fixed_pow (a : R) (ha : σ a = a) (n : ℕ) :
    σ (a ^ n) = a ^ n := by rw [map_pow, ha]

/-- A bar-EVEN scalar times a bar-ODD element is bar-ODD: multiplying by
    z-functionals never changes parity — the odd channel must be supplied by
    the carrier. -/
theorem bar_even_mul_bar_odd (f g : R) (hf : σ f = f) (hg : σ g = -g) :
    σ (f * g) = -(f * g) := by rw [map_mul, hf, hg]; ring

/-- **The exclusion, division-free.** An element that is simultaneously
    bar-even and bar-odd satisfies `2·a = 0`. -/
theorem bar_even_and_odd_two_mul_eq_zero (a : R)
    (heven : σ a = a) (hodd : σ a = -a) : 2 * a = 0 := by
  have h : a = -a := heven.symm.trans hodd
  linear_combination h

/-- **The exclusion (`Field` form): a bar-even scalar cannot equal a bar-odd
    NONZERO element in characteristic ≠ 2.** Applied to the keystone: every
    scalar functional of `z` alone is bar-even (§1 + §4 closure), while the
    kernel's leading coefficient `a₁ = −c₃` is bar-odd
    (`QBetaCKRecursionKernelConstraints.ck_a1_bar_odd`) and empirically
    nonzero — so `a₁` is NOT a scalar functional of `z` alone. -/
theorem bar_even_ne_bar_odd_of_ne_zero {F : Type*} [Field F] (σF : F →+* F)
    (a : F) (heven : σF a = a) (hodd : σF a = -a)
    (h2 : (2 : F) ≠ 0) : a = 0 := by
  have h := bar_even_and_odd_two_mul_eq_zero σF a heven hodd
  exact (mul_eq_zero.mp h).resolve_left h2

/-! ## §5. Parity/shadow bookkeeping for the T3-2 tension (investigation infra)

The T3-2 tension (ledger §4-ter): "a₁ exactly bar-odd" and "a₁ q=1-regular
with nonzero shadow" are jointly impossible. The two lemmas below are the
generic, reading-agnostic certificates of the impossibility direction: a
bar-compatible ring homomorphism (e.g. the q=1 evaluation) annihilates
bar-odd elements, hence any evaluation of a bar-decomposed `a = e + o`
factors through the bar-even part. Which horn resolves the tension for the
kernel coefficient `a₁ = −c₃` (odd-part reading vs q=1-singular reading vs
symbol overloading between distinct `a₁` objects) is an open investigation
item — see the 2026-07-07 investigation audit. -/

/-- **A bar-compatible evaluation kills bar-odd elements.** If `φ` is a ring
    hom with `φ ∘ σ = φ` (e.g. evaluation at the bar-fixed point `q = 1`) and
    `σ o = −o`, then `2·φ(o) = 0` — division-free form; over a target of
    characteristic ≠ 2 this is `φ(o) = 0`. This is the T3-2 tension made
    precise: an exactly-bar-odd `a₁` cannot carry the nonzero q=1 shadow. -/
theorem fixed_eval_two_mul_kills_bar_odd {S : Type*} [CommRing S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ) (o : R) (ho : σ o = -o) :
    2 * φ o = 0 := by
  have h1 : φ (σ o) = φ o := by
    have := congrArg (fun f : R →+* S => f o) hcomm
    simpa using this
  rw [ho, map_neg] at h1
  linear_combination -h1

/-- **Shadow gates test the even part.** For the bar-decomposition
    `a = e + o` (`σ e = e`, `σ o = −o`), every bar-compatible evaluation `φ`
    into a target where `2` is regular satisfies `φ(a) = φ(e)`: the q=1
    shadow of a kernel coefficient is carried entirely by its bar-even part.
    (Stated over a `Field` target with `(2 : S) ≠ 0` for the cancellation.) -/
theorem shadow_carried_by_even_part {S : Type*} [Field S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ) (a e o : R)
    (hsplit : a = e + o) (_he : σ e = e) (ho : σ o = -o)
    (h2 : (2 : S) ≠ 0) : φ a = φ e := by
  have hkill := fixed_eval_two_mul_kills_bar_odd σ φ hcomm o ho
  have hzero : φ o = 0 := (mul_eq_zero.mp hkill).resolve_left h2
  rw [hsplit, map_add, hzero, add_zero]

end QOU.QBeta
