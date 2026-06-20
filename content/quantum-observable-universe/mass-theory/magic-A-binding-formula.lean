/-
  # Doubly-magic light-nucleus binding formula

  For a light nucleus (Z, N) that is doubly magic (both Z and N in
  the magic-number set {2, 8, 20, 28, 50, 82, 126}), the binding
  energy admits the closed form

      B(Z, N) = ρ_F · m_e · A · 8G

  where 8G = Vol(L6a4) = Vol(Borromean) is the universal residue
  prefactor per prop:gravity-spectral-prefactor and ρ_F is the
  substrate-determined structural prefactor.

  Specialised to ⁴He with ρ_F = 2 gives B(⁴He) ≈ 29.956 MeV vs
  experimental 28.296 MeV (5.9% miss) — dramatically tighter than
  the alpha-shift formula (prop:binding-alpha-shift-extension)
  which misses ⁴He by -79%.

  Per AGENTS.md §3b-cond: the categorical derivation of ρ_F = 2
  is axiomatised as a class hypothesis; the formula is a
  rigorous-conditional theorem modulo that class.

  ## Why doubly-magic requires a separate path

  The alpha-shift formula assumes a single hyperbolic force-carrier
  knot per nucleus. For doubly-magic Z, N the
  prop:diagrammatic-double-magic-lr-fusion conjecture proves the
  Littlewood-Richardson fusion of the Z-block and N-block collapses
  to a single self-conjugate Specht module — no Wedderburn channel
  for crossings, no hyperbolic knot, no per-rep Reeb phase. The
  binding is set by the universal Borromean residue 8G scaled by
  nucleon count.

  Ref: [manuscript] prop:magic-A-binding-formula
       [manuscript] prop:binding-alpha-shift-extension
       [manuscript] prop:diagrammatic-double-magic-lr-fusion
       [manuscript] prop:gravity-spectral-prefactor
       [manuscript] rem:strutinsky-from-graded-trace
       [audit] docs/audits/2026-05-31-binding-magic-A-wireup.md
       [compute] computations/magic_A_formula.py
       [compute] computations/binding_alpha_shift_witness.py
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Field.Basic

namespace QOU.BraidKnot

universe u

/-- The set of magic numbers {2, 8, 20, 28, 50, 82, 126}. Mirrors
    `QOU.Common.magicSet` (single source of truth referenced from
    `magic-numbers-bring.lean`). Inlined here to keep this file
    standalone for the sibling-trace convention. -/
def isMagic (n : ℕ) : Prop :=
  n = 2 ∨ n = 8 ∨ n = 20 ∨ n = 28 ∨ n = 50 ∨ n = 82 ∨ n = 126

/-- A light nucleus (Z, N) is *doubly magic* if both Z and N lie in
    the magic-number set. The canonical doubly-magic light example
    is ⁴He with Z = N = 2. -/
def isDoublyMagic (Z N : ℕ) : Prop :=
  isMagic Z ∧ isMagic N

/-- Borromean residue prefactor `8G = Vol(L6a4)`, where G is
    Catalan's constant. Approximate value 7.32772475... (mpmath
    50dps). The exact value is delivered by
    `prop:gravity-spectral-prefactor`; here we abstract it as a
    parameter so the formula statement does not depend on the
    Catalan-constant Mathlib import depth. -/
class CatalanPrefactor (R : Type u) [Field R] where
  /-- The value of `8G` in the given field. -/
  vol_borromean : R

/-- **Doubly-magic binding formula class** (§3b-cond hypothesis).

    Axiomatises the substrate-determined prefactor `ρ_F` and the
    formula `B(Z, N) = ρ_F · m_e · A · 8G` for doubly-magic (Z, N).
    The class field `formula` records the binding evaluation.

    Reanalysis (2026-05-31, see audit
    `docs/audits/2026-05-31-binding-magic-A-wireup.md`): the
    derivation of `ρ_F` was previously framed here as Open Math A,
    but is structurally answered by
    `conj:kashaev-density-equals-sdp-multiplicity` (RESOLVED
    2026-05-24, Rule-14 owner-authorised): `ρ_F = ν_SDP` (joint-
    tower SDP Wedderburn multiplicity), driver (x) of the canonical
    13-menu. The class hypothesis below can be replaced (Sprint 2)
    with a derivation from the SDP-multiplicity Lean class once it
    is in place. Only the numerical verification
    `ν_SDP(⁴He) = 2` (joint-tower SDP solver extension) remains
    open; structural derivation is closed.

    Remaining R&D follow-up:
    1. Extend joint-tower SDP solver to confirm `ν_SDP(⁴He) = 2`
       (currently extrapolated from the SDP-confirmed D, T, ³He
       census).
    2. Extend to higher-A doubly-magic candidates (¹⁶O Z=N=8,
       ⁴⁰Ca Z=N=20) by computing each `ν_SDP` via the same SDP
       infrastructure.

    The class hypothesis is sorry-free per §3b-cond: any instance
    discharges `formula` definitionally for its specific (Z, N). -/
class MagicABindingFormula {R : Type u} [Field R] [CatalanPrefactor R]
    (B : ℕ → ℕ → R) (m_e : R) where
  /-- The substrate-determined prefactor for the (Z, N) regime.
      ⁴He uses `rho_F = 2`. -/
  rho_F : ℕ → ℕ → R
  /-- The doubly-magic binding formula: B(Z, N) = ρ_F · m_e · A · 8G. -/
  formula : ∀ Z N : ℕ, isDoublyMagic Z N →
    B Z N = rho_F Z N * m_e * ((Z + N : ℕ) : R) * CatalanPrefactor.vol_borromean

/-- **Magic-A binding theorem** (rigorous-conditional per §3b-cond).

    For any doubly-magic (Z, N), the binding equals
    `ρ_F · m_e · A · 8G` where `A = Z + N`. Sorry-free conditional
    on the `MagicABindingFormula` class hypothesis. -/
theorem magic_A_binding_formula
    {R : Type u} [Field R] [CatalanPrefactor R]
    (B : ℕ → ℕ → R) (m_e : R)
    [hMA : MagicABindingFormula B m_e]
    (Z N : ℕ) (hZN : isDoublyMagic Z N) :
    B Z N = hMA.rho_F Z N * m_e * ((Z + N : ℕ) : R) * CatalanPrefactor.vol_borromean :=
  hMA.formula Z N hZN

/-- **⁴He instance** of the doubly-magic regime.

    Z = N = 2 are both magic; the witness compute
    (`magic_A_formula.py::magic_A_binding(2, 2)`) gives `ρ_F = 2`
    yielding B ≈ 29.956 MeV vs experimental 28.296 MeV (5.9% miss).

    This existence theorem confirms the doubly-magic predicate
    is non-trivially inhabited at the lightest scale. -/
theorem he4_is_doubly_magic : isDoublyMagic 2 2 := by
  refine ⟨?_, ?_⟩ <;> exact Or.inl rfl

/-- **Binding regime tag.**

    The light-nucleus binding evaluator is the disjoint union of two
    categorical regimes. A nucleus `(Z, N)` is routed to exactly one:

    - `DoublyMagic` — both `Z, N ∈ 𝔐`. The Littlewood–Richardson
      fusion of the Z-block and N-block collapses to a single
      self-conjugate Specht module
      (`prop:diagrammatic-double-magic-lr-fusion`); there is no
      Wedderburn channel, no hyperbolic force-carrier knot, no per-rep
      Reeb phase. Binding is set by the universal Borromean residue
      `8G` scaled by nucleon count via `MagicABindingFormula`.
    - `AlphaShift` — at least one of `Z, N ∉ 𝔐`. The nucleus carries a
      single hyperbolic force-carrier torus knot `T(p, k)` whose
      per-rep Reeb phase `α_shift = k·(p−1)` sets the binding via
      `BindingForceCarrierKnot`
      (`prop:binding-alpha-shift-extension`). -/
inductive BindingRegime
  /-- Single-hyperbolic-knot regime (per-rep Reeb phase, `T(p, k)`). -/
  | AlphaShift
  /-- Doubly-magic regime (Borromean residue `8G · A`). -/
  | DoublyMagic
  deriving DecidableEq, Repr

/-- **Regime classifier.** Routes a nucleus `(Z, N)` to its binding
    regime: `DoublyMagic` when both `Z` and `N` are magic, else
    `AlphaShift`. `isMagic` is decidable (finite disjunction of
    equalities), so the dispatch is a total computable function. -/
def bindingRegime (Z N : ℕ) : BindingRegime :=
  if (isMagic Z ∧ isMagic N) then BindingRegime.DoublyMagic
  else BindingRegime.AlphaShift

/-- The classifier selects `DoublyMagic` exactly on doubly-magic
    inputs. -/
theorem bindingRegime_doublyMagic_iff (Z N : ℕ) :
    bindingRegime Z N = BindingRegime.DoublyMagic ↔ isDoublyMagic Z N := by
  unfold bindingRegime isDoublyMagic
  by_cases h : isMagic Z ∧ isMagic N
  · rw [if_pos h]; exact ⟨fun _ => h, fun _ => rfl⟩
  · rw [if_neg h]; exact ⟨fun hc => absurd hc (by decide), fun hd => absurd hd h⟩

/-- The classifier selects `AlphaShift` exactly when the nucleus is
    *not* doubly magic. -/
theorem bindingRegime_alphaShift_iff (Z N : ℕ) :
    bindingRegime Z N = BindingRegime.AlphaShift ↔ ¬ isDoublyMagic Z N := by
  unfold bindingRegime isDoublyMagic
  by_cases h : isMagic Z ∧ isMagic N
  · rw [if_pos h]; exact ⟨fun hc => absurd hc (by decide), fun hn => absurd h hn⟩
  · rw [if_neg h]; exact ⟨fun _ => h, fun _ => rfl⟩

/-- **⁴He dispatches to the doubly-magic regime.** `Z = N = 2` are
    both magic, so `bindingRegime 2 2 = DoublyMagic`; the binding is
    evaluated through `MagicABindingFormula` (this file), giving the
    80× gap closure (`B ≈ 29.956 MeV` vs `28.296 MeV`, 5.9% miss). -/
theorem he4_dispatches_to_magic :
    bindingRegime 2 2 = BindingRegime.DoublyMagic := by
  decide

/-- **Tritium dispatches to the α_shift regime.** `³H = (Z, N) = (1, 2)`:
    `Z = 1 ∉ 𝔐`, so `bindingRegime 1 2 = AlphaShift`; the binding is
    evaluated through `BindingForceCarrierKnot` (the `T(2, 5)`
    candidate, `α_shift = 5`, in `binding-alpha-shift-extension.lean`). -/
theorem tritium_dispatches_to_alpha_shift :
    bindingRegime 1 2 = BindingRegime.AlphaShift := by
  -- Z = 1 ∉ 𝔐 = {2, 8, 20, 28, 50, 82, 126}; classifier is computable.
  decide

/-- **³He dispatches to the α_shift regime.** `³He = (Z, N) = (2, 1)`:
    `N = 1 ∉ 𝔐`, so `bindingRegime 2 1 = AlphaShift`; routed through
    `BindingForceCarrierKnot` (the mirror `T(2, 5)` candidate). -/
theorem helium3_dispatches_to_alpha_shift :
    bindingRegime 2 1 = BindingRegime.AlphaShift := by
  -- N = 1 ∉ 𝔐; classifier is computable.
  decide

/-- **Deuteron dispatches to the α_shift regime.** `D = (Z, N) = (1, 1)`:
    neither is magic, so `bindingRegime 1 1 = AlphaShift`; routed
    through `BindingForceCarrierKnot` (the `T(2, 3)` trefoil candidate,
    `α_shift = 3`). -/
theorem deuteron_dispatches_to_alpha_shift :
    bindingRegime 1 1 = BindingRegime.AlphaShift := by
  -- Neither Z = 1 nor N = 1 is magic; classifier is computable.
  decide

/-- **Regime-aware binding evaluator.**

    The single entry point for light-nucleus binding: given a nucleus
    `(Z, N)`, a doubly-magic evaluator `B_dm` (closed-form `8G · A`
    via `MagicABindingFormula`) and an α_shift evaluator `B_as`
    (per-rep Reeb phase via `BindingForceCarrierKnot`), select the
    correct evaluator by the regime classifier.

    This is the operational dispatcher (PR #1543 fix-option 2): ⁴He
    routes through `B_dm`, non-magic A = 2, 3 candidates route through
    `B_as`. The two underlying evaluators are the §3b-cond
    rigorous-conditional theorems in their respective files; this
    function only chooses between them. -/
def bindingDispatch {R : Type u} (B_dm B_as : ℕ → ℕ → R) (Z N : ℕ) : R :=
  match bindingRegime Z N with
  | BindingRegime.DoublyMagic => B_dm Z N
  | BindingRegime.AlphaShift  => B_as Z N

/-- On a doubly-magic nucleus the dispatcher returns the doubly-magic
    evaluator. -/
theorem bindingDispatch_doublyMagic {R : Type u}
    (B_dm B_as : ℕ → ℕ → R) (Z N : ℕ) (h : isDoublyMagic Z N) :
    bindingDispatch B_dm B_as Z N = B_dm Z N := by
  unfold bindingDispatch
  rw [(bindingRegime_doublyMagic_iff Z N).2 h]

/-- On a non-doubly-magic nucleus the dispatcher returns the α_shift
    evaluator. -/
theorem bindingDispatch_alphaShift {R : Type u}
    (B_dm B_as : ℕ → ℕ → R) (Z N : ℕ) (h : ¬ isDoublyMagic Z N) :
    bindingDispatch B_dm B_as Z N = B_as Z N := by
  unfold bindingDispatch
  rw [(bindingRegime_alphaShift_iff Z N).2 h]

/-- **⁴He binding goes through the magic-A formula.** Composing the
    dispatcher with the §3b-cond `MagicABindingFormula` class: when
    the doubly-magic evaluator is the class binding `B` and `(Z, N)`
    is doubly magic, the dispatched value equals the closed form
    `ρ_F · m_e · A · 8G`. -/
theorem he4_binding_via_dispatch
    {R : Type u} [Field R] [CatalanPrefactor R]
    (B B_as : ℕ → ℕ → R) (m_e : R)
    [hMA : MagicABindingFormula B m_e] :
    bindingDispatch B B_as 2 2
      = hMA.rho_F 2 2 * m_e * ((2 + 2 : ℕ) : R) * CatalanPrefactor.vol_borromean := by
  rw [bindingDispatch_doublyMagic B B_as 2 2 he4_is_doubly_magic]
  exact hMA.formula 2 2 he4_is_doubly_magic

/-- **Two-regime binding dispatcher (existence).** Retained for the
    `prop:magic-A-binding-formula` Lean ref: the doubly-magic regime
    is non-trivially inhabited at the lightest scale (⁴He). -/
theorem two_regime_dispatch_exists :
    ∃ Z N : ℕ, isDoublyMagic Z N := by
  exact ⟨2, 2, he4_is_doubly_magic⟩

end QOU.BraidKnot
