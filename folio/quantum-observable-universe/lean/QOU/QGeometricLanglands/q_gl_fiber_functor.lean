import Mathlib.Tactic

/-!
# QOU.QGeometricLanglands.q_gl_fiber_functor — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:q-gl-fiber-functor`](../../../quantum-observable-universe/q-geometric-langlands/q-gl-fiber-functor.md):
*Fibre-functor mediation of the $q$-Langlands correspondence.*

This is a **conjecture**: the class carries the conjecture's actual
content as the `uniqueness` field ($\tau$-rigidity forces $\mathbb{L}_q$
unique up to natural isomorphism), and **no instance is supplied** — the
absent instance *is* the open conjecture (per AGENTS.md §3b-tax), NOT a
missing proof. The candidate equivalences are abstracted as a class
parameter; "unique up to natural iso" is modelled as equality on the set
of $\tau$/Hecke-compatible equivalences.
-/

namespace QOU.QGeometricLanglands

/-- **Fibre-functor mediation of the $q$-Langlands correspondence.**

    Conjectural class — see
    [`conj:q-gl-fiber-functor`](../../../quantum-observable-universe/q-geometric-langlands/q-gl-fiber-functor.md). -/
class q_gl_fiber_functor where
  /-- Candidate $q$-GL equivalences $\mathbb{L}_q$. -/
  Equivalence : Type
  /-- Compatibility with the Hecke-eigensheaf structure and the fibre
      functor $\tau$. -/
  compatible : Equivalence → Prop
  /-- **The conjecture**: the rigidity of $\tau$ forces $\mathbb{L}_q$
      to be unique — any two $\tau$/Hecke-compatible equivalences are
      connected by a unique natural isomorphism (modelled as equality). -/
  uniqueness : ∀ L L' : Equivalence, compatible L → compatible L' → L = L'

namespace q_gl_fiber_functor

variable [h : q_gl_fiber_functor]

/-- **The subtype of $\tau$-compatible equivalences is a subsingleton.** -/
theorem compatible_subsingleton :
    Subsingleton { L : h.Equivalence // h.compatible L } :=
  ⟨fun ⟨L₁, h₁⟩ ⟨L₂, h₂⟩ => Subtype.ext (h.uniqueness L₁ L₂ h₁ h₂)⟩

/-- **Any observable functional on candidate equivalences is constant across
    $\tau$-compatible realisations.** -/
theorem compatible_apply_eq {α : Type*} (f : h.Equivalence → α)
    {L₁ L₂ : h.Equivalence} (h₁ : h.compatible L₁) (h₂ : h.compatible L₂) :
    f L₁ = f L₂ :=
  congrArg f (h.uniqueness L₁ L₂ h₁ h₂)

/-- **Pointed characterisation of $\tau$-compatibility.**
    Once a base $\tau$-compatible equivalence $L_0$ is given, another
    candidate $L$ is $\tau$-compatible if and only if $L = L_0$. -/
theorem compatible_iff_eq_of_base {L₀ : h.Equivalence} (h₀ : h.compatible L₀)
    (L : h.Equivalence) :
    h.compatible L ↔ L = L₀ :=
  ⟨fun hL => h.uniqueness L L₀ hL h₀, fun hEq => hEq ▸ h₀⟩

end q_gl_fiber_functor

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the class fields above, which
-- is exactly the open conjecture; supplying one asserts it.
--
-- History: this file previously carried
--     axiom q_gl_fiber_functor_conjecture : q_gl_fiber_functor
--     noncomputable instance : q_gl_fiber_functor := q_gl_fiber_functor_conjecture
-- so every downstream `[q_gl_fiber_functor]` resolved for free and the assumption was
-- invisible outside `#print axioms`.  Removed, not
-- completed.  Downstream results must take `[q_gl_fiber_functor]` as an explicit
-- hypothesis.

end QOU.QGeometricLanglands
