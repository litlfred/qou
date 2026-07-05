import Mathlib.Data.Matrix.Mul
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

/-!
# Keystone value step, input (B): the Perron–Frobenius ground state is `d_q` (§3b-cond)

`KeystoneSelfDualSpectralNarrowing.lean` proved the **(C)** leg of the value-step reframe: a self-dual
`S` (`S² = C`) has `S⁴ = 1`, eigenvalues are 4th roots of unity, and on the `C = +1` self-dual sector
they tighten to `±1` (`eigenvalue_selfdual_sector_pm_one`).  What that leg leaves open — and what this
file closes, **conditionally** — is input **(B)**: *why the `+1` ground state of that sector is the
quantum-dimension vector `d_q` and not some other positive eigenvector.*

The answer is the **Perron–Frobenius / Ocneanu–Wenzl selection**: the fusion (branching) operator `N`
is entrywise non-negative, and a non-negative operator has, up to scale, a **unique** positive
eigenvector at its Frobenius eigenvalue — the Markov-trace weights, i.e. `d_q` (Ocneanu; Wenzl).  This
is a *cited* theorem, not one this file re-proves; so it is axiomatised as a **§3b-cond primary
conjecture class** `PerronFrobeniusGroundState`, following the repo's conditional-class convention: a
**`Prop`-valued** hypothesis over the **explicit data** `N`, `rho`, `d` (as `HeckeBraid (H : …) : Prop`
in `IwahoriHeckeAPI.lean`), whose content field `pf_proportional` carries the PF up-to-scale
uniqueness as an explicit, parameter-quantified hypothesis (§3b-tax: a primary conjecture — it binds
no other conjecture class — with real content, not `True`).

**What is *derived* (sorry-free, genuine work — not a self-assuming projection).**  Given the class,
`eq_d_of_normalized` proves that a positive ground eigenvector *normalised to agree with `d` at any one
index* is **equal** to `d` — sharpening the cited "proportional" input to a **unique pin**.  The
derivation is real: it exhibits the proportionality constant, evaluates at the normalising index, and
cancels the (positive, hence nonzero) `d`-component to force `c = 1`.  This is the §3b-cond
non-degeneracy requirement (the class carries the *hypothesis* — PF up-to-scale uniqueness — and the
theorem derives the strictly stronger *normalised* conclusion — the pin to `d_q`).

**Scope.** Keystone value step (s013), input (B).  Conditional on the class instance (the physical
fusion category being the one whose PF eigenvector is the *Hecke* `d_q`), which is the owner-gated
open content (narrow Subgoal-2 reversal, #2503/#2524).  A `Unit`-block model instance over any ordered
field witnesses non-vacuity (the conditional results are not conditional-on-`False`).

Base ring: an ordered field `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — positivity of the
quantum dimensions (`0 < d i`) is genuinely archimedean (§7c); the `d_q` numerical evaluation at `q₀`
lives downstream.  (`LinearOrderedField` is deprecated as a class binder in Mathlib v4.24.0.)

Audit: `docs/audits/2026-07-05-keystone-selfduality-spectral-narrowing.md` (follow-up item 1).

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 — Hecke-algebra Markov trace / positive weights.
-- Ref: [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (Verlinde/PF vacuum).
-/

namespace QOU.BraidKnot.Keystone

open Matrix

/-- **Perron–Frobenius / Ocneanu–Wenzl ground-state selection** (§3b-cond primary conjecture, `Prop`).

A `Prop`-valued hypothesis class over the **explicit** data `N` (fusion operator), `rho` (Frobenius
eigenvalue), `d` (quantum-dimension vector) — the repo's conditional-class convention
(`HeckeBraid (H : …) : Prop`), keeping the data explicit and the conjectural assumption
proof-irrelevant.  Content: `N` non-negative, `d` positive, `d` the Frobenius eigenvector, and — the
conjectural field — that **any** positive eigenvector at `rho` is a scalar multiple of `d` (PF
up-to-scale uniqueness).  Primary conjecture (binds no other conjecture class); the content is the
parameter-quantified `pf_proportional`, not a `True`/empty marker. -/
class PerronFrobeniusGroundState {ι R : Type*} [Fintype ι] [DecidableEq ι]
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (N : Matrix ι ι R) (rho : R) (d : ι → R) : Prop where
  /-- `N` is entrywise non-negative (the Markov / fusion structure). -/
  N_nonneg : ∀ i j, 0 ≤ N i j
  /-- The quantum dimensions are positive. -/
  d_pos : ∀ i, 0 < d i
  /-- `d` is the Frobenius eigenvector: `N d = rho · d`. -/
  d_eigen : N.mulVec d = rho • d
  /-- **Cited PF / Ocneanu–Wenzl uniqueness** (the conjectural input): every positive eigenvector at
  the Frobenius eigenvalue is a scalar multiple of `d`. -/
  pf_proportional :
    ∀ v : ι → R, (∀ i, 0 < v i) → N.mulVec v = rho • v → ∃ c : R, v = c • d

namespace PerronFrobeniusGroundState

variable {ι R : Type*} [Fintype ι] [DecidableEq ι] [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  {N : Matrix ι ι R} {rho : R} {d : ι → R} [self : PerronFrobeniusGroundState N rho d]

/-- **The pin (derived, sorry-free): a normalised positive ground eigenvector equals `d_q`.**

Given the PF class, any positive eigenvector `v` at the Frobenius eigenvalue that is *normalised* to
agree with `d` at a single index `k` is **equal** to `d` — not merely proportional.  This closes
input (B): the value-map target (the `+1` self-dual PF ground state of
`KeystoneSelfDualSpectralNarrowing`) is uniquely `d_q`.  The proof is genuine (exhibit `c`, evaluate
at `k`, cancel the nonzero `d k`), so this is a §3b-cond conditional theorem, not a self-assuming
projection of `pf_proportional`. -/
theorem eq_d_of_normalized (v : ι → R) (hv_pos : ∀ i, 0 < v i)
    (hv_eig : N.mulVec v = rho • v) (k : ι) (hnorm : v k = d k) : v = d := by
  obtain ⟨c, hc⟩ := self.pf_proportional v hv_pos hv_eig
  have hk : v k = c * d k := by
    have := congrFun hc k; simpa [Pi.smul_apply, smul_eq_mul] using this
  have hcd : c * d k = d k := by rw [← hk, hnorm]
  have hc1 : c = 1 :=
    mul_right_cancel₀ (self.d_pos k).ne' (hcd.trans (one_mul (d k)).symm)
  rw [hc, hc1, one_smul]

/-- Corollary: two normalised positive ground eigenvectors are **equal** (uniqueness of the pinned
value-map target). -/
theorem ground_state_unique (v w : ι → R)
    (hv_pos : ∀ i, 0 < v i) (hv_eig : N.mulVec v = rho • v)
    (hw_pos : ∀ i, 0 < w i) (hw_eig : N.mulVec w = rho • w)
    (k : ι) (hvk : v k = d k) (hwk : w k = d k) : v = w := by
  rw [eq_d_of_normalized v hv_pos hv_eig k hvk,
      eq_d_of_normalized w hw_pos hw_eig k hwk]

end PerronFrobeniusGroundState

/-! ## Non-vacuity: the class is inhabited (single-block `Unit` model) -/

/-- **Non-vacuity — the `Unit`-block model over any ordered field.**  One fusion block (`ι = Unit`),
`N = 1` (the `1×1` identity), `rho = 1`, `d = 1`.  Every positive `v` on `Unit` is `(v ()) • d`, so
`pf_proportional` holds.  Witnesses that `PerronFrobeniusGroundState` is inhabitable over any ordered
field, so `eq_d_of_normalized` / `ground_state_unique` are not conditional-on-`False`.  The OPEN
content is the *physical* instance where `N` is the actual Hecke fusion operator and `d` the Hecke
`d_q`. -/
instance pfGroundState_unit {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R] :
    PerronFrobeniusGroundState (1 : Matrix Unit Unit R) 1 (fun _ => 1) where
  N_nonneg := fun i j => by fin_cases i; fin_cases j; simp [Matrix.one_apply_eq]
  d_pos := fun _ => one_pos
  d_eigen := by rw [Matrix.one_mulVec, one_smul]
  pf_proportional := fun v _ _ =>
    ⟨v (), by funext i; fin_cases i; simp [Pi.smul_apply, smul_eq_mul]⟩

end QOU.BraidKnot.Keystone
