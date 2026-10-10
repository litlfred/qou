import QOU.BraidKnot.KeystoneVerlindeSMatrixBridge
import QOU.BraidKnot.KeystoneModularTwist

/-!
# De-opaquing the keystone gate `bwS0_eq_hecke`: the concrete RT/Seifert vacuum row `S0·θ^f`

`KeystoneVerlindeSMatrixBridge.lean` carries residual-(i)'s single open piece as the class
`BWVacuumRowIsHecke`, whose gauge datum `bwS0 : List ℕ → ℝ` is an **opaque free field** and whose
open conjecture `bwS0_eq_hecke` asserts `bwS0 l = d_q(λ)/√(Σ d_q²)`.  Because `bwS0` is a *free* field,
the class is **fiat-dischargeable** (`bwS0 := d_q/D` makes `bwS0_eq_hecke` an `rfl`, as the file's own
non-vacuity `example` shows) — the gate captures **no content**.

This file **de-opaques** the gate.  It replaces the free `bwS0` with the **concrete** Reshetikhin–
Turaev / Seifert vacuum-row formula, converting an un-provable physics-fiat into a genuine, refutable
math claim.

## The concrete row (from #3652 vector 2 — no fit)

In a ribbon MTC the colored-WRT (RT) vacuum row of the *framed* Seifert manifold `S³/2I` is, in its
`λ`-dependence, the compact modular datum times the ribbon twist raised to the **forced Seifert
framing** `f : ℤ`:
`S^{RT}_{0λ} = S_{0λ} · θ_λ^{f}`, with `S_{0λ} = d_q(λ)/D` (`VerlindeModularData.S0_eq`) and the twist
`θ_λ = q^{c(λ)}` (`KeystoneModularTwist.theta`).  The framing `f = 0` carries *zero* Σ(2,3,5) data
(reduces to the compact datum — a tautology).  So the concrete, non-opaque gauge vacuum row is
`bwS0Concrete = S0 · θ^f`, and the de-opaqued gate `bwS0Concrete = d_q/D = S0` holds **iff** `θ^f = 1`
(`bwS0Concrete_eq_S0_iff`).

## What this proves — and the honest disposition

* `bwS0Concrete_eq_S0_iff` (**symbolic-exact**): the de-opaqued gate holds `↔ (S0 = 0 ∨ θ^f = 1)`.
* `bwS0Concrete_conj_mul` / `bwS0Concrete_breaks_symmetry` (**scope-(b) structural exclusion**, per
  AGENTS.md — cites a *proved invariant*): `d_q` (hence `S0`) is transpose-**invariant**
  (`qDim_conj`), but the twist `θ` is transpose-**inverting** (`theta_conjugate`).  So the concrete
  row `S0·θ^f` breaks a conjugation symmetry that `d_q/D` has, and it *cannot* equal the
  transpose-symmetric `d_q/D` for `f ≠ 0` unless `θ^f = 1`.  This is a genuine invariant, not a
  magnitude probe.
* `bwS0Concrete_eq_hecke_forces_trivial_twist` (**capstone**): if the concrete Hecke row equals the
  modular datum `d_q/√(Σ d_q²)` on **all** of `P`, then `∀ l ∈ P, (θ_λ)^f = 1` — the de-opaqued gate
  *forces* a twist-trivial framing.

**Honest disposition (scope classification per AGENTS.md "Before declaring refuted"):**
At the *observable/archimedean* real `q₀ > 1` (growth regime, `Im q₀ = 0`), `θ_λ = q₀^{c(λ)}` is a real
power of `q₀ > 1`; for the forced Seifert framing `f ≠ 0` and any non-self-conjugate block
(`c(λ) ≠ 0`) it is **not** a root of unity, so `θ^f ≠ 1` and the naive gate is **REFUTED** — a
scope-**(a)** negative for *this construction at real q₀* sharpened by the scope-**(b)** transpose-
symmetry invariant above.  The refutation does **NOT** exclude the surviving open object: the
**fibre** root-of-unity form (`|q| = 1`, hence `|θ_λ| = 1`) at the pre-`τ` categorical level,
archimedean-continued to `q₀` (AGENTS.md fibre-vs-observable-`q`).  That is `bwS0_eq_hecke` restated,
now with its content exposed.  **This file does not close the gate — it exposes and sharpens it.**
No fit; no fabricated `BWVacuumRowIsHecke` instance with `bwS0 := d_q/D` is presented as a closure.

Base ring `ℝ` (§7c): `S0`/`D` already live over `ℝ` (`D = √(Σ d_q²)`), and the twist is consumed here
as `theta q : List ℕ → ℝ` (the `GroupWithZero ℝ` instance).

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
- [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746 — non-abelian CS localization.
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators
open QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-! ## The concrete Reshetikhin–Turaev / Seifert vacuum row `S0 · θ^f` -/

/-- **The concrete RT/Seifert vacuum S-matrix row** — the compact modular datum `S_{0λ}` times the
ribbon twist `θ_λ` raised to the **forced Seifert framing** `f : ℤ`.  This is the genuine formula that
replaces the opaque, fiat-dischargeable free field `bwS0` in `BWVacuumRowIsHecke`: it is
`S^{RT}_{0λ} = S_{0λ}·θ_λ^{f}`, the colored-WRT vacuum row of the framed Seifert manifold `S³/2I`. -/
noncomputable def bwS0Concrete (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ) (p : h.Part) :
    ℝ :=
  h.S0 p * (θ p) ^ f

/-- **The `f = 0` tautology (content-free).**  Zero Seifert framing carries no Σ(2,3,5) data: the
concrete row collapses to the compact modular datum `S_{0λ}`.  This is exactly the case the opaque
gate cannot distinguish from a genuine framing. -/
@[simp] theorem bwS0Concrete_f_zero (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (p : h.Part) :
    bwS0Concrete h θ 0 p = h.S0 p := by
  unfold bwS0Concrete
  rw [zpow_zero, mul_one]

/-! ## The framing obstruction made explicit -/

/-- **The de-opaqued gate holds iff the twist power is trivial.**
`bwS0Concrete = S_{0λ} ↔ (S_{0λ} = 0 ∨ θ_λ^f = 1)`.  Factoring `S_{0λ}·θ^f = S_{0λ}·1`, either the
row vanishes or the framing twist is trivial — the framing obstruction, exact and symbolic. -/
theorem bwS0Concrete_eq_S0_iff (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ) (p : h.Part) :
    bwS0Concrete h θ f p = h.S0 p ↔ h.S0 p = 0 ∨ (θ p) ^ f = 1 := by
  unfold bwS0Concrete
  rw [mul_right_eq_self₀]
  exact or_comm

/-- **Trivial twist ⇒ the gate holds** (the clean direction, `θ^f = 1 → bwS0Concrete = S0`). -/
theorem bwS0Concrete_of_twist_pow_one (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ)
    (p : h.Part) (hθ1 : (θ p) ^ f = 1) : bwS0Concrete h θ f p = h.S0 p := by
  unfold bwS0Concrete
  rw [hθ1, mul_one]

/-! ## The conjugation-asymmetry refutation (the core honest content)

`d_q`/`S0` is transpose-INVARIANT; `θ` is transpose-INVERTING.  The concrete row therefore breaks a
symmetry the compact modular datum has — the proved invariant that refutes the `f ≠ 0` gate. -/

/-- **Conjugation product law.**  Using `S_{0λ'} = S_{0λ}` (transpose-invariance of `d_q`) and
`θ_{λ'} = θ_λ⁻¹` (transpose-inversion of the twist), the concrete row at `λ` and at the transpose `λ'`
multiply to `S_{0λ}²`:  `bwS0Concrete(λ')·bwS0Concrete(λ) = S_{0λ}²`.  The `θ^f` factors cancel — the
row's framing dependence is transpose-antisymmetric while `S0` is transpose-symmetric. -/
theorem bwS0Concrete_conj_mul (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ) (p : h.Part)
    (hconjS0 : h.S0 (h.conj p) = h.S0 p) (hconjθ : θ (h.conj p) = (θ p)⁻¹) (hθ : θ p ≠ 0) :
    bwS0Concrete h θ f (h.conj p) * bwS0Concrete h θ f p = h.S0 p ^ 2 := by
  unfold bwS0Concrete
  rw [hconjS0, hconjθ]
  have key : ((θ p)⁻¹) ^ f * (θ p) ^ f = 1 := by
    rw [← mul_zpow, inv_mul_cancel₀ hθ, one_zpow]
  calc h.S0 p * (θ p)⁻¹ ^ f * (h.S0 p * θ p ^ f)
      = (h.S0 p * h.S0 p) * ((θ p)⁻¹ ^ f * θ p ^ f) := by ring
    _ = (h.S0 p * h.S0 p) * 1 := by rw [key]
    _ = h.S0 p ^ 2 := by ring

/-- **The concrete row breaks conjugation symmetry.**  If the transpose-twist power differs from the
twist power (`(θ_λ)⁻¹^f ≠ (θ_λ)^f` — the framing asymmetry) and the row is nonzero, then
`bwS0Concrete(λ') ≠ bwS0Concrete(λ)`: the concrete RT vacuum row is **not** transpose-invariant, unlike
`d_q`/`S0`.  Hence it cannot equal the transpose-symmetric `d_q/D` for `f ≠ 0`.

At real `q₀ > 1` with `θ_λ = q₀^{c(λ)}`: `(θ_λ)⁻¹^f = q₀^{-f·c(λ)}` and `(θ_λ)^f = q₀^{f·c(λ)}` are
unequal whenever `f·c(λ) ≠ 0`, so the hypothesis holds off the self-conjugate blocks — the proved
obstruction. -/
theorem bwS0Concrete_breaks_symmetry (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ) (p : h.Part)
    (hconjS0 : h.S0 (h.conj p) = h.S0 p) (hconjθ : θ (h.conj p) = (θ p)⁻¹)
    (hS0 : h.S0 p ≠ 0) (hsym : (θ p)⁻¹ ^ f ≠ (θ p) ^ f) :
    bwS0Concrete h θ f (h.conj p) ≠ bwS0Concrete h θ f p := by
  unfold bwS0Concrete
  rw [hconjS0, hconjθ]
  intro hc
  exact hsym (mul_left_cancel₀ hS0 hc)

/-! ## Capstone: the de-opaqued gate FORCES a twist-trivial framing -/

/-- **Abstract capstone.**  If the concrete row equals `S_{0λ}` and the row is nonzero, then the
framing twist is trivial: `θ_λ^f = 1`.  (Immediate from `bwS0Concrete_eq_S0_iff` + `Or.resolve_left`.) -/
theorem bwS0Concrete_eq_S0_forces_trivial_twist
    (h : VerlindeModularData ℝ) (θ : h.Part → ℝ) (f : ℤ) (p : h.Part)
    (hS0 : h.S0 p ≠ 0) (hgate : bwS0Concrete h θ f p = h.S0 p) :
    (θ p) ^ f = 1 :=
  ((bwS0Concrete_eq_S0_iff h θ f p).mp hgate).resolve_left hS0

/-- **Hecke capstone — the de-opaqued gate forces `θ^f = 1` on every block.**

Take the concrete RT row `bwS0Concrete (heckeVerlindeData …) (theta q) f` on the Hecke Verlinde data.
If it equals the Hecke modular datum `d_q(λ)/√(Σ d_q²)` for **all** `λ ∈ P` (the de-opaqued form of
`bwS0_eq_hecke`), then `∀ l ∈ P, (theta q l)^f = 1` — the forced Seifert framing must be twist-trivial.

At real `q₀ > 1` this is **false** off the self-conjugate blocks (`theta q₀ l = q₀^{c(λ)}` is not a
root of unity for `c(λ) ≠ 0`), so for the physical forced framing `f ≠ 0` the gate is **REFUTED** at
`q₀` — the honest disposition.  The residue is the fibre root-of-unity form (`|q| = 1`), unaffected. -/
theorem bwS0Concrete_eq_hecke_forces_trivial_twist
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) (f : ℤ)
    (hgate : ∀ l ∈ P,
      bwS0Concrete (heckeVerlindeData q hq P hsorted hconj hP) (theta q) f l
        = qDim q l / Real.sqrt (∑ m ∈ P, qDim q m ^ 2)) :
    ∀ l ∈ P, (theta q l) ^ f = 1 := by
  intro l hl
  set h := heckeVerlindeData q hq P hsorted hconj hP with hh
  have hS0ne : h.S0 l ≠ 0 := div_ne_zero (qDim_pos hq l).ne' h.D_ne
  exact bwS0Concrete_eq_S0_forces_trivial_twist h (theta q) f l hS0ne (hgate l hl)

end QOU.BraidKnot.Keystone
