/-
Copyright (c) 2026 litlfred. All rights reserved.

# The roots-of-unity gate cannot reach `q₀` without an analytic bridge

Companion to the sibling keystone result (PR #4973,
`KeystoneRootsOfUnityReduction` / `KeystoneFramingTrivialAtRootsOfUnity`), which
proved:

* if **both** sides of `bwS0_eq_hecke` are *rational* in `q`, agreement at all
  roots of unity already forces agreement at the substrate `q₀`; and
* the concrete RT/Seifert row (monomial twist `θ_λ = q^{c(λ)}`) is rational, so
  the gate forces `f · c(λ) = 0`, hence `f = 0` — the tautological framing.

That is a scope-(b) exclusion of the **rational** row only. It explicitly leaves
open the **non-rational** BW rows (non-monomial / root-dependent / correction-term
twists), and the natural vehicle for those is the analytic route — the Faddeev /
Andersen–Kashaev state integral, whose kernel is transcendental (so it is *not*
pinned by roots of unity) and which converges at the substrate anchor
(`τ = b² = −0.0166i`, in-domain; route-selection probe
`state_integral_domain_substrate_anchor_probe.py`).

**This file prices that escape.** The result is a dichotomy: the very property
that lets a candidate evade the sibling's `f = 0` horn — failure of an analytic
bridge from the gate set to `q₀` — is *also* what destroys the gate's ability to
say anything at `q₀`.

* `gate_does_not_determine_q0` — the sharp statement: for **any** gate set `S`
  with `q₀ ∉ S` and any target `f`, there are two functions agreeing with `f`
  everywhere on `S` whose values at `q₀` differ (indeed take any prescribed
  values). Set-theoretic and unconditional: no regularity, no analyticity.
* `q0_value_arbitrary_on_gate` — the constructive form (any prescribed value at
  `q₀` is attainable while matching on `S`).

Read together with the sibling's rational horn, the trilemma for any candidate
BW row `B` matching the Hecke row at all roots of unity is:

| horn | hypothesis | consequence |
|---|---|---|
| (i) rational / analytic across the gate | analytic bridge to `q₀` | equals the Hecke row ⇒ concrete monomial case gives `f = 0` (sibling #4973) |
| (ii) natural boundary on `|q| = 1` | no continuation to real `q₀ > 1` | the Habiro horn (#4957/#4962): `(q;q)_k`-adic completion diverges at `q₀` |
| (iii) defined separately at `q₀` (state integral) | no bridge | **this file**: the gate constrains nothing at `q₀` |

**Consequence for the state-integral route (the honest price).** Convergence of
the state integral at `q₀` is *not* an identification: matching the Hecke row at
roots of unity does **not** transfer to `q₀` in the absence of an analytic
bridge. Any state-integral construction must therefore supply an **independent**
identification at `q₀` — it cannot inherit one from the root-of-unity gate. This
is the formal version of the route-selection caveat "convergence ≠ identification
of `W_λ`".

**Honest scope (STRICT).** This does **not** close `bwse`, and it does **not**
refute the state-integral route — it prices it, and it is deliberately *weak by
design*: horn (iii) is a triviality about arbitrary functions, and that is
precisely the point (the gate has no purchase without regularity). It also does
**not** claim the three horns are exhaustive for every conceivable candidate; it
names the two known escapes and shows each is paid for. Scope-(a). No fit;
nothing wired; L2 unchanged.

Base ring (§7c): horn (iii) is set-theoretic over arbitrary types (no `ℝ`); horn (i)
is genuinely archimedean/analytic and so lives over `ℂ`, as it must.

-- Ref: [leitner2026] docs/coordination/s5-so3-keystone.md
-/
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Complex.Basic

namespace QOU.BraidKnot.KeystoneRootsToQ0Bridge

open Set Filter

variable {α β : Type*}

/-- **The gate value at `q₀` is arbitrary.** If the substrate point `q₀` is not
itself in the gate set `S`, then for any target `f` and any prescribed value `v`
there is a function agreeing with `f` at every gate point yet taking the value `v`
at `q₀`.

This is the formal price of leaving the analytic (rational) class: a candidate
that is merely *defined* at `q₀` — rather than analytically continued there —
inherits **no** constraint from matching at roots of unity. -/
theorem q0_value_arbitrary_on_gate
    (S : Set α) (q0 : α) (hq0 : q0 ∉ S) (f : α → β) (v : β) :
    ∃ g : α → β, (∀ z ∈ S, g z = f z) ∧ g q0 = v := by
  classical
  refine ⟨fun z => if z = q0 then v else f z, ?_, ?_⟩
  · intro z hz
    have hzq : z ≠ q0 := fun h => hq0 (h ▸ hz)
    simp [hzq]
  · simp

/-- **The gate does not determine the substrate value.** For any gate set `S` with
`q₀ ∉ S` and any two distinct values `v₁ ≠ v₂`, there exist two functions that
agree with each other (and with the target `f`) at **every** point of `S` but
disagree at `q₀`.

So "matches the Hecke row at all roots of unity" is, by itself, consistent with
*any* value at the substrate anchor. Determination requires an extra hypothesis
tying `q₀` to `S` — rationality (the sibling's route, which then forces `f = 0`)
or an analytic bridge. Absent that, the root-of-unity gate is silent at `q₀`. -/
theorem gate_does_not_determine_q0
    (S : Set α) (q0 : α) (hq0 : q0 ∉ S) (f : α → β) {v₁ v₂ : β} (hv : v₁ ≠ v₂) :
    ∃ g₁ g₂ : α → β,
      (∀ z ∈ S, g₁ z = f z) ∧ (∀ z ∈ S, g₂ z = f z) ∧
      (∀ z ∈ S, g₁ z = g₂ z) ∧ g₁ q0 ≠ g₂ q0 := by
  obtain ⟨g₁, hg₁S, hg₁q⟩ := q0_value_arbitrary_on_gate S q0 hq0 f v₁
  obtain ⟨g₂, hg₂S, hg₂q⟩ := q0_value_arbitrary_on_gate S q0 hq0 f v₂
  refine ⟨g₁, g₂, hg₁S, hg₂S, fun z hz => ?_, ?_⟩
  · rw [hg₁S z hz, hg₂S z hz]
  · rw [hg₁q, hg₂q]; exact hv

/-! ### Horn (i) — with an analytic bridge, the gate *does* reach `q₀`

The converse half of the dichotomy, over `ℂ` (genuinely archimedean, §7c). If the
candidate row and the Hecke row are both analytic on one preconnected open set `U`
containing a point `z₀` at which the gate set accumulates **and** containing `q₀`,
then agreement on the gate forces agreement at `q₀` — by the identity theorem
(`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`).

Since the roots of unity are dense in the unit circle, *any* candidate analytic on
a neighbourhood of an arc of `|q| = 1` together with the real point `q₀ ≈ 1.10998`
falls into this horn — and is therefore pinned to the (rational) Hecke row, which
in the concrete monomial-twist case forces `f = 0` (sibling #4973). Escaping that
conclusion requires failing this hypothesis, which is exactly horn (iii). -/
theorem q0_determined_of_analytic_bridge
    {f g : ℂ → ℂ} {U : Set ℂ} {z₀ q0 : ℂ} (S : Set ℂ)
    (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U)
    (hU : IsPreconnected U) (hz₀ : z₀ ∈ U)
    (hSfreq : ∃ᶠ z in nhdsWithin z₀ {z₀}ᶜ, z ∈ S)
    (hagree : ∀ z ∈ S, f z = g z)
    (hq0 : q0 ∈ U) :
    f q0 = g q0 :=
  hf.eqOn_of_preconnected_of_frequently_eq hg hU hz₀ (hSfreq.mono hagree) hq0

end QOU.BraidKnot.KeystoneRootsToQ0Bridge
