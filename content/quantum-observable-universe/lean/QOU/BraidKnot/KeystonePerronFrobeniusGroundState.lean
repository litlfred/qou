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
conjecture class** `PerronFrobeniusGroundState` whose content field `pf_proportional` carries the PF
up-to-scale uniqueness as an explicit, parameter-quantified hypothesis (§3b-tax: a primary conjecture
— it binds no other conjecture class — with real content, not `True`).

**What is *derived* (sorry-free, genuine work — not a self-assuming projection).**  Given the class,
`eq_d_of_normalized` proves that a positive ground eigenvector *normalised to agree with `d` at any one
index* is **equal** to `d` — sharpening the cited "proportional" input to a **unique pin**.  The
derivation is real: it exhibits the proportionality constant, evaluates at the normalising index, and
cancels the (positive, hence nonzero) `d`-component to force `c = 1`.  This is the §3b-cond
non-degeneracy requirement (the class carries the *hypothesis* — PF up-to-scale uniqueness — and the
theorem derives the strictly stronger *normalised* conclusion — the pin to `d_q`).

**Scope.** Keystone value step (s013), input (B).  Conditional on the class instance (the physical
fusion category being the one whose PF eigenvector is the *Hecke* `d_q`), which is the owner-gated
open content (narrow Subgoal-2 reversal, #2503/#2524).  A `Unit`-block model instance witnesses
non-vacuity (the conditional results are not conditional-on-`False`).

Base ring: an ordered field `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — positivity of the
quantum dimensions (`0 < d i`) is genuinely archimedean (§7c); the `d_q` numerical evaluation at `q₀`
lives downstream.

Audit: `docs/audits/2026-07-05-keystone-selfduality-spectral-narrowing.md` (follow-up item 1).

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 — Hecke-algebra Markov trace / positive weights.
-- Ref: [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (Verlinde/PF vacuum).
-/

namespace QOU.BraidKnot.Keystone

open Matrix

/-- **Perron–Frobenius / Ocneanu–Wenzl ground-state selection** (§3b-cond primary conjecture).

Axiomatises the *cited* PF input: a non-negative fusion operator `N`, its Frobenius eigenvalue `rho`,
the positive quantum-dimension eigenvector `d`, and — the content field — that **any** positive
eigenvector at `rho` is a scalar multiple of `d` (PF up-to-scale uniqueness).  This is a primary
conjecture (binds no other conjecture class); its content is the parameter-quantified
`pf_proportional`, not a `True`/empty marker. -/
class PerronFrobeniusGroundState (ι R : Type*)
    [Fintype ι] [DecidableEq ι] [Field R] [LinearOrder R] [IsStrictOrderedRing R] where
  /-- The fusion / branching operator. -/
  N : Matrix ι ι R
  /-- `N` is entrywise non-negative (the Markov / fusion structure). -/
  N_nonneg : ∀ i j, 0 ≤ N i j
  /-- The Frobenius (Perron) eigenvalue. -/
  rho : R
  /-- The quantum-dimension vector `d_q`. -/
  d : ι → R
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
  [P : PerronFrobeniusGroundState ι R]

/-- **The pin (derived, sorry-free): a normalised positive ground eigenvector equals `d_q`.**

Given the PF class, any positive eigenvector `v` at the Frobenius eigenvalue that is *normalised* to
agree with `d` at a single index `k` is **equal** to `d` — not merely proportional.  This closes
input (B): the value-map target (the `+1` self-dual PF ground state of
`KeystoneSelfDualSpectralNarrowing`) is uniquely `d_q`.  The proof is genuine (exhibit `c`, evaluate
at `k`, cancel the nonzero `d k`), so this is a §3b-cond conditional theorem, not a self-assuming
projection of `pf_proportional`. -/
theorem eq_d_of_normalized (v : ι → R) (hv_pos : ∀ i, 0 < v i)
    (hv_eig : P.N.mulVec v = P.rho • v) (k : ι) (hnorm : v k = P.d k) : v = P.d := by
  obtain ⟨c, hc⟩ := P.pf_proportional v hv_pos hv_eig
  have hk : v k = c * P.d k := by
    have := congrFun hc k; simpa [Pi.smul_apply, smul_eq_mul] using this
  have hcd : c * P.d k = P.d k := by rw [← hk, hnorm]
  have hc1 : c = 1 :=
    mul_right_cancel₀ (P.d_pos k).ne' (hcd.trans (one_mul (P.d k)).symm)
  rw [hc, hc1, one_smul]

/-- Corollary: two normalised positive ground eigenvectors are **equal** (uniqueness of the pinned
value-map target). -/
theorem ground_state_unique (v w : ι → R)
    (hv_pos : ∀ i, 0 < v i) (hv_eig : P.N.mulVec v = P.rho • v)
    (hw_pos : ∀ i, 0 < w i) (hw_eig : P.N.mulVec w = P.rho • w)
    (k : ι) (hvk : v k = P.d k) (hwk : w k = P.d k) : v = w := by
  rw [eq_d_of_normalized v hv_pos hv_eig k hvk,
      eq_d_of_normalized w hw_pos hw_eig k hwk]

end PerronFrobeniusGroundState

/-! ## Non-vacuity: the class is inhabited (single-block `Unit` model) -/

/-- **Non-vacuity — the `Unit`-block model over `ℝ`.**  One fusion block (`ι = Unit`), `N = [1]`,
`rho = 1`, `d = 1`.  Every positive `v` on `Unit` is `(v ()) • d`, so `pf_proportional` holds.
Witnesses that `PerronFrobeniusGroundState` is inhabitable, so `eq_d_of_normalized` /
`ground_state_unique` are not conditional-on-`False`.  The OPEN content is the *physical* instance
where `N` is the actual Hecke fusion operator and `d` the Hecke `d_q`. -/
noncomputable instance pfGroundState_unit : PerronFrobeniusGroundState Unit ℝ where
  N := 1
  N_nonneg := fun i j => by fin_cases i; fin_cases j; simp [Matrix.one_apply_eq]
  rho := 1
  d := fun _ => 1
  d_pos := fun _ => one_pos
  d_eigen := by rw [Matrix.one_mulVec, one_smul]
  pf_proportional := fun v _ _ =>
    ⟨v (), by funext i; fin_cases i; simp [Pi.smul_apply, smul_eq_mul]⟩

end QOU.BraidKnot.Keystone
