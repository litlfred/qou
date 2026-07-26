/-
Copyright (c) 2026 litlfred. All rights reserved.

# Bar-odd carrier rigidity — the c₃ Im(q) swing is not a free per-anchor knob

Generic-ring, bar-parity-native companion to the **Im(q)-as-c₃-carrier** analysis
(capstone #4297). Context (KC21): the c₃ cross-anchor swing is structurally
bar-ODD, `S(−ε) = −S(ε)` for `q = q₀ + iε`, so the fibre-level `Im(q)` is the
bar-odd carrier. The reframe's honesty guardrail — *the varying `Im(q)` must be
constrained across observables, never a free per-anchor knob* — has two halves,
and this file is the **structural** one.

> **Route status (2026-07-26): the Im(q) reframe is CLOSED — not a lead.** The
> quantitative half was run and merged: [`ImQAnchorCarrier.lean`](ImQAnchorCarrier.lean)
> / [`2026-07-26-q0-varies-imq-c3.md`](../../../../../docs/audits/2026-07-26-q0-varies-imq-c3.md)
> (PR #4326) prove **at ℝ** with the actual phase model
> (`S = (√3/2)r²sin 2φ`, `k = ∂ε→φ = 0.6514`) that a single global `Im(q₀)`
> is `6.6×10⁶`× too small to realize the swing, and that a per-anchor `Im(q)`
> fits anything (opposite sign, free scale) ⇒ **FIT**. `conj:algebraic-
> geometric-dilog-equivalence` stays open; the resurgent D-ladder (KC22) is the
> live route.

This file is **not a competing lead** — it is the *generic* structural reason
behind that concrete verdict: composing the merged graded-split canonicity
(`QOU.QBeta.EvenFaceMassShadow`, PR #4275) with `QOU.QBeta.ZBarParity`, it shows
over **any** `CommRing` (no phase model, no numbers) that the bar-odd carrier is
rigidly pinned by the fibre element — the parity content of "not a free
per-anchor knob." Reusable bar-parity infrastructure; `ImQAnchorCarrier` is its
concrete ℝ instance.

All sorry-free, generic `{R : Type*} [CommRing R]` with an abstract bar involution
`σ : R →+* R` (the fibre `q ↦ q⁻¹`), char-`≠ 2` supplied on a `Field` target only
where cancellation is needed (§7c — fibre-level algebra, no `ℝ`, consistent with
the archimedean `lusztig_q_0_imaginary_part_zero`: `Im(q₀) = 0` post-τ, the carrier
is fibre).

The results:

1. `swing_bar_odd` — two fibre elements sharing the **same** bar-even part (same
   mass shadow) differ by a **bar-odd** element: the cross-anchor swing lives
   entirely in the Im(q) carrier.
2. `swing_shadow_null` — hence the swing has **vanishing q=1 (classical) shadow**:
   the mass is anchor-invariant while c₃ swings — exactly the observed pattern.
3. `carrier_unique` — **rigidity.** Over a char-`≠ 2` field, the bar-odd carrier of
   a fibre element is **uniquely determined by the element**: `E = e + o = e' + o'`
   (bar-even + bar-odd) forces `o = o'`. The carrier is a *function of the physics*,
   not a free parameter — no per-anchor DOF.
4. `single_carrier_bar_odd` — the **constrained-Im(q) shape**: one shared bar-odd
   generator `g` scaled by an observable-specific bar-**even** weight `w` is bar-odd
   (`bar_even_mul_bar_odd`). This is the "one Im(q) carrier across observables"
   form; combined with `carrier_unique` it is the *canonical* representative, and
   the free per-anchor alternative is excluded once the shadows are fixed.

**Honest scope.** Reusable generic-ring parity infrastructure; the concrete Im(q)
route it abstracts is already CLOSED (merged, above). It captures the *structural*
reason (bar-odd carrier rigidity) — it does not derive the swing magnitude (that
was the merged `∂S/∂φ` order-check that closed the route). No `c_k` value; no Im(q)
fitted; nothing wired; no registry tier changed.

-- Ref: [manuscript] docs/audits/2026-07-26-1ppq-l2-two-front-survey.md
-/
import QOU.QBeta.EvenFaceMassShadow

namespace QOU.QBeta.BarOddCarrierRigidity

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **The cross-anchor swing is bar-ODD.** If two fibre elements `E₁`, `E₂` share
the same bar-even part `e` (the same mass shadow) and have bar-odd carriers `o₁`,
`o₂`, then their difference `E₁ − E₂ = o₁ − o₂` is bar-odd: the entire swing lives
in the Im(q) carrier, none of it in the shadow. -/
theorem swing_bar_odd (E₁ E₂ e o₁ o₂ : R)
    (h1 : E₁ = e + o₁) (h2 : E₂ = e + o₂)
    (ho1 : σ o₁ = -o₁) (ho2 : σ o₂ = -o₂) :
    σ (E₁ - E₂) = -(E₁ - E₂) := by
  have hdiff : E₁ - E₂ = o₁ - o₂ := by rw [h1, h2]; ring
  rw [hdiff, map_sub, ho1, ho2]; ring

/-- **The swing carries no classical (q=1) shadow.** Being bar-odd
(`swing_bar_odd`), the cross-anchor difference is annihilated by every
bar-compatible evaluation `φ` (`φ ∘ σ = φ`) into a characteristic-`≠ 2` field:
`φ(E₁ − E₂) = 0`. The mass shadow is anchor-invariant while c₃ swings — the
empirically-required pattern (masses do not swing per anchor; only the c₃/decay
channel does). -/
theorem swing_shadow_null {S : Type*} [Field S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ)
    (E₁ E₂ e o₁ o₂ : R) (h1 : E₁ = e + o₁) (h2 : E₂ = e + o₂)
    (ho1 : σ o₁ = -o₁) (ho2 : σ o₂ = -o₂) (h2ne : (2 : S) ≠ 0) :
    φ (E₁ - E₂) = 0 :=
  QOU.QBeta.EvenFaceMassShadow.oddFace_shadow_null σ φ hcomm (E₁ - E₂)
    (swing_bar_odd σ E₁ E₂ e o₁ o₂ h1 h2 ho1 ho2) h2ne

/-- **Carrier rigidity.** Over a characteristic-`≠ 2` field, the bar-odd carrier of
a fibre element is **uniquely determined by the element**: if `E = e + o = e' + o'`
with `e, e'` bar-even and `o, o'` bar-odd, then `o = o'`. The Im(q) carrier is a
function of the physics `E`, **not a free per-anchor parameter** — the structural
content of #4326's honesty guardrail. Immediate from the graded-split canonicity
(`parity_decomposition_unique`). -/
theorem carrier_unique {F : Type*} [Field F] (σF : F →+* F)
    (E e o e' o' : F) (h : E = e + o) (h' : E = e' + o')
    (he : σF e = e) (ho : σF o = -o) (he' : σF e' = e') (ho' : σF o' = -o')
    (h2 : (2 : F) ≠ 0) : o = o' :=
  (QOU.QBeta.EvenFaceMassShadow.parity_decomposition_unique σF E e o e' o'
    h h' he ho he' ho' h2).2

/-- **The constrained-Im(q) shape.** One shared bar-odd generator `g` (the single
Im(q) carrier) scaled by an observable-specific bar-**even** weight `w` (the mass
shadow's own parity) is itself bar-ODD: `σ(w·g) = −(w·g)`. This is the "one Im(q)
carrier across observables" form #4326 needs; by `carrier_unique` it is the
canonical representative, so the free per-anchor alternative is excluded once the
shadows are fixed. -/
theorem single_carrier_bar_odd (g w : R) (hg : σ g = -g) (hw : σ w = w) :
    σ (w * g) = -(w * g) :=
  QOU.QBeta.bar_even_mul_bar_odd σ w g hw hg

/-- **Rigidity, packaged for the reframe.** Two anchors whose fibre elements share
the same bar-even shadow `e` have their entire cross-anchor swing equal to the
bar-odd carrier difference `o₁ − o₂`, which (by `carrier_unique` applied to each
element's canonical split) is fixed by the two elements — there is no additional
freedom to tune. Stated as the algebraic pin plus the parity certificate. -/
theorem swing_carrier_pinned {F : Type*} [Field F] (σF : F →+* F)
    (E₁ E₂ e o₁ o₂ : F) (h1 : E₁ = e + o₁) (h2 : E₂ = e + o₂)
    (ho1 : σF o₁ = -o₁) (ho2 : σF o₂ = -o₂) :
    E₁ - E₂ = o₁ - o₂ ∧ σF (E₁ - E₂) = -(E₁ - E₂) :=
  ⟨by rw [h1, h2]; ring, swing_bar_odd σF E₁ E₂ e o₁ o₂ h1 h2 ho1 ho2⟩

end QOU.QBeta.BarOddCarrierRigidity
