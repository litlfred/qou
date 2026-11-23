/-
# B2 τ-lift — interface SHARPENING: the shadow lift collapses to ONE open field

Bean `qou-demm`. Follows the two 2026-08-02 audits
`2026-08-02-hodge-lift-bring-h1-model.md` (§3 the minimal open core) and
`2026-08-02-alpha-em-perloop-clauses-obstruction.md` (§Correction). Compute
`computations/alpha_em/hodge_lift_bring_model.py` (10/10 PASS) proved that two of
the B2 lift's would-be-open ingredients are **automatic** (moduli-independent):

* (i) the involution match `ρ ↔ Hodge conjugation` — `c = SWAP∘conj` is the
  canonical Weil real structure, carrying **no arithmetic content**;
* (ii) the nome anti-holomorphic equivariance `τ(q̄) = −conj(τ(q))` — **forced**
  by the nome `q = e^{2πiτ}`.

So the merged 2-field lift interface (`TauRhoHodgeLiftInterface.lean`, fields
`hermitian` + `conjugated`) collapses to a **single** open field: the minimal
open core (MOC),

> **(MOC)** the categorical τ-functor produces a holomorphic period map
> `Φ : q ↦ H¹(E_{τ(q)}) ⊂ H¹(Bring)` landing in the rank-2 conjugate-pair
> sub-object, carrying the conformal Laplacian (B3) as a **real self-adjoint
> weight**.

This file builds that reduction **at the shadow level** — the Gaussian-integer /
discrete model of `TauRhoHodgeShadow.lean` + `PerLoopMeasureShadowAssembly.lean`
(Lean core, no Mathlib, no continuous Hodge theory invented). It:

* declares a **single-field** class `PeriodMapWeight w` carrying only the MOC
  (the period-map image weight is real self-adjoint = ρ-symmetric — the shadow
  of the conformal Laplacian's reality);
* **derives** the equal-split and doubled-total conclusions from that single
  field by **reusing the merged sorry-free lemmas** `rho_forced_equal_split` /
  `channel_share_is_half` (the ½ that was the `conjugated` field is now DERIVED);
* records the involution-match and the nome-equivariance as **automatic**
  unconditional theorems (reusing `shadow_intertwines` /
  `bar_exchanges_degenerate_pair` / `transpose_fixes_degenerate_pair`), so they
  are *derived*, not open fields;
* reconstructs the full B5 target (`shadow_assembly`) from the SINGLE field
  `[PeriodMapWeight w]`, DISCHARGING the merged assembly's open `f/hnorm/hint`
  triple via the forced `hodgeShadow` + automatic `shadow_norm` /
  `shadow_intertwines`.

Honesty (STRICT, AGENTS.md §"Axiomatization is NOT a Proof"): this is an
**interface sharpening — fewer open fields, NOT a closure.** The class has **no
instance** anywhere: exhibiting the specific `w` that the categorical period map
`Φ` produces for the actual α_EM loop weight IS the single remaining wall (the
MOC), and leaving `PeriodMapWeight` uninstantiated is the honest open state. The
single field IS the open premise; nothing here derives the lift or wires
`1/(8π)` to production — the identification stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Init.Data.Int.Basic
import QOU.Archimedean.SigmaJGeometricCarrier
import QOU.Archimedean.TauRhoHodgeShadow
import QOU.Archimedean.PerLoopMeasureShadowAssembly

namespace QOU.Archimedean.PeriodMapWeightReduction

open QOU.Archimedean.SigmaJGeometricCarrier
open QOU.Archimedean.SigmaJGeometricCarrier.GInt
open QOU.Archimedean.TauRhoHodgeShadow
open QOU.Archimedean.PerLoopMeasureShadowAssembly

/-- **Primary conjecture — the B2 lift, minimal open core (MOC), shadow form.**

Parameter: `w : GInt → Int`, the period-map image weight on the degenerate
conjugate pair `{i, −i}` (the shadow of the conformal Laplacian carried by `Φ`
onto the rank-2 sub-object `H¹(E_{τ(q)})`).

The single field `selfAdjoint` asserts the MOC's one substantive content: the
weight is **real self-adjoint = ρ-symmetric** (`w (conj z) = w z`), i.e. the
Laplacian data is real. This is the shadow of the matrix interface's `hermitian`
field; the second matrix field `conjugated` (the `H^{0,1}` weight is the
conjugate of the `H^{1,0}` weight) is now DERIVED — see `equal_split` — and the
involution-match + nome-equivariance are AUTOMATIC (`involution_match_automatic`,
`nome_equivariance_automatic`), so neither is a field.

OPEN: **no instance is declared.** The conjecture is exhibiting the specific `w`
that the categorical τ-functor's period map `Φ` produces for the actual α_EM
loop weight — the framework's foundational q↔period bridge. Leaving this class
uninstantiated is the honest open state (the MOC). Per §"Axiomatization is NOT a
Proof" the class axiomatises the lift's *input* (reality of the weight); every
theorem below derives its conclusion from that input, none closes the wall. -/
class PeriodMapWeight (w : GInt → Int) : Prop where
  /-- The period-map image weight is real self-adjoint (ρ-symmetric): the shadow
  of the conformal Laplacian's reality. This is the single open MOC field. -/
  selfAdjoint : ∀ z, w (GInt.conj z) = w z

namespace PeriodMapWeight

variable {w : GInt → Int}

/-- **Derived — this was the merged interface's second field (`conjugated`).**
Given the single MOC field, the loop weight splits equally across the conjugate
pair `{i, −i}`: `w(−i) = w(i)`. The ½ of the per-loop measure is now ρ-FORCED
from the reality field alone — reusing the merged sorry-free
`rho_forced_equal_split`. -/
theorem equal_split [h : PeriodMapWeight w] : w (neg I) = w I :=
  rho_forced_equal_split w h.selfAdjoint

/-- **Derived (doubled total).** The selected channel `H^{1,0}` carries exactly
half the pair total: `w(i) + w(−i) = 2·w(i)` — reusing the merged sorry-free
`channel_share_is_half`. -/
theorem doubled_total [h : PeriodMapWeight w] : w I + w (neg I) = 2 * w I :=
  channel_share_is_half w h.selfAdjoint

/-- **Derived (vanishing pair asymmetry).** Under `PeriodMapWeight w`, the
asymmetry between the `H^{1,0}` and `H^{0,1}` channels vanishes identically:
`w(i) - w(−i) = 0`. -/
theorem pair_diff_eq_zero [h : PeriodMapWeight w] : w I - w (neg I) = 0 := by
  have heq : w (neg I) = w I := equal_split
  omega

/-- **Additive closure of `PeriodMapWeight`.** The sum of any two ρ-symmetric
period-map weights is again ρ-symmetric. -/
theorem add_closed {w₁ w₂ : GInt → Int}
    [h₁ : PeriodMapWeight w₁] [h₂ : PeriodMapWeight w₂] :
    PeriodMapWeight (fun z => w₁ z + w₂ z) :=
  ⟨fun z => by rw [h₁.selfAdjoint z, h₂.selfAdjoint z]⟩

/-- **Scalar-multiple closure of `PeriodMapWeight`.** Any integer multiple of a
ρ-symmetric period-map weight is again ρ-symmetric. -/
theorem smul_closed (c : Int) {w : GInt → Int} [h : PeriodMapWeight w] :
    PeriodMapWeight (fun z => c * w z) :=
  ⟨fun z => by rw [h.selfAdjoint z]⟩

end PeriodMapWeight

/-- **Automatic — NOT a field: the involution match `ρ ↔ Hodge conjugation`.**
The FORCED shadow assignment satisfies the ρ-intertwining unconditionally
(`hodgeShadow (conj i) = ¬ hodgeShadow i`), reusing `shadow_intertwines`. Audit
(2) `2026-08-02-hodge-lift-bring-h1-model.md`: `c = SWAP∘conj` is the canonical
Weil real structure for ANY moduli, so this match carries no arithmetic content
and is not an open field. -/
theorem involution_match_automatic :
    hodgeShadow (GInt.conj I) = !(hodgeShadow I) :=
  shadow_intertwines.1

/-- **Automatic — NOT a field: the nome anti-holomorphic equivariance shadow.**
The reality doubling is carried by `bar = conj`, which EXCHANGES the degenerate
pair (`conj i = −i`), while the transpose role-swap FIXES each point
(`−conj i = i`) — reusing `bar_exchanges_degenerate_pair` /
`transpose_fixes_degenerate_pair`. Audit §2: `τ(q̄) = −conj(τ(q))` is forced by
the nome `q = e^{2πiτ}`, so this is derived, not open. -/
theorem nome_equivariance_automatic :
    GInt.conj I = neg I ∧ neg (GInt.conj I) = I :=
  ⟨bar_exchanges_degenerate_pair.1, transpose_fixes_degenerate_pair.1⟩

/-- **Sharpened assembly — the full B5 target from the SINGLE open field.**
The merged `shadow_assembly` took an open `f/hnorm/hint` triple (the Hodge
assignment and its normalization + ρ-intertwining) as explicit hypotheses. Here
those are DISCHARGED — `f := hodgeShadow` with `shadow_norm` and
`shadow_intertwines.1` (both automatic, from the FORCED assignment) — so the B4
target `[2]_q · w(i) = w(i) + w(−i)` (the q→1 one-loop restoring the doubled
unit) follows from ONLY `[PeriodMapWeight w]`, i.e. the single MOC field. -/
theorem sharpened_assembly (w : GInt → Int) [h : PeriodMapWeight w] :
    klEigenvalueAtOne * w I = w I + w (neg I) :=
  (shadow_assembly hodgeShadow shadow_norm shadow_intertwines.1 w h.selfAdjoint).2

end QOU.Archimedean.PeriodMapWeightReduction
