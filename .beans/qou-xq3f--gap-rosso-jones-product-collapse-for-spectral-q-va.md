---
# qou-xq3f
title: 'GAP: Rosso-Jones product-collapse for spectral Q-value decomposition (Lean)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:36:58Z
updated_at: 2026-08-23T08:56:54Z
---

The corollary cor:spectral-decomposition-qvalue (content/quantum-observable-universe/predicted-spectra/spectral-decomposition-qvalue.lean) claims Q = Q_bare × Π_{τ∈E_g} F(τ,N), with (iv) the product collapsing to a single active-shell term and (v) the decomposition exact by Rosso-Jones completeness of torus-knot invariants (prop:cohomological-embedding).

STATUS: the product-collapse + exactness are NOT formalized in Lean. As of 2026-08-22 the theorem is restated §3b-cond: a RossoJonesCollapse class carries the collapse (product = activeShellTerm) as a hypothesis and the theorem DERIVES the factorization from it (replacing the prior vacuous trivial existential ∃Q_q, Q_q=rhs).

OPEN: derive the collapse itself — that the knot-operator product over the embeddable basis reduces to the single active term (all other shells cancel parent↔daughter; non-embeddable knots give F=1), from Rosso-Jones completeness. This needs the torus-knot invariant / Markov-trace machinery not yet in this Lean development. Until then the class stays uninstantiated (honestly conditional).



## PROGRESS 2026-08-22 — collapse MECHANISM now proved (sorry-free)

The opaque assumption is gone. Replaced the class field `collapse : product = activeTerm` (which *asserted* the collapse) with a proved theorem:

  knot_operator_product_collapse (E : Finset ι) (F : ι → ℝ) (active) :
    (∀ τ ∈ E, τ ≠ active → F τ = 1) → ∏ τ ∈ E, F τ = F active

via Finset.prod_eq_single. #print axioms: [propext, Classical.choice, Quot.sound] — no sorryAx. spectral_decomposition_qvalue now derives the Q-value collapse from this.

So step (iv) 'the product collapses to a single term' is DERIVED, not assumed. The assumption is reduced from 'the product equals the active term' to the strictly weaker, more primitive per-shell statement 'each inactive shell contributes F τ = 1'.

STILL OPEN (the actual Rosso-Jones content): proving that hypothesis — that each non-active shell's knot operator F τ = 1 (parent↔daughter shell-cancellation + F=1 for non-embeddable knots). That needs the F-operator (Markov trace of τ·T_β) defined in Lean + the completeness/self-duality of the torus-knot basis, none of which is in this Lean development yet. Bean stays open for that.



## PROGRESS 2026-08-22 (2) — per-shell cancellation: two inactive branches DISCHARGED

Added a ratio-level shell model + discharged the hInactive hypothesis for the two inactive branches:
- ShellState (parentTrace, daughterTrace, embeddable); shellFactor s = if embeddable then daughterTrace/parentTrace else 1.
- shellFactor_nonembeddable: non-embeddable ⇒ F=1 (definitional).
- shellFactor_unchanged: embeddable & daughterTrace=parentTrace≠0 ⇒ F=1 (div_self — the genuine 'cancels in ratio' mechanism).
- shell_product_collapse: every non-active shell non-embeddable-or-unchanged ⇒ ∏ shellFactor = shellFactor(active), with hInactive now PROVED for this model (not assumed).

#print axioms: [propext, Classical.choice, Quot.sound] — no sorryAx.

So step (iv) is now: collapse mechanism proved (progress 1) + the two INACTIVE branches (non-embeddable, unchanged) proved to give 1 (progress 2). The hInactive hypothesis is discharged for the ratio model.

STILL OPEN (the deep Rosso-Jones content):
1. The ACTIVE shell value = |tr_M(e·τ·T_β·e)|/|tr_M(T_β)| — needs the weighted Markov-trace tower (QOU.Braiding.HnMarkovTrace) wired into this file.
2. Identifying WHICH shell is active (the converting neutron's shell) and that all others are genuinely unchanged/non-embeddable — the physical shell-assignment, not yet modeled.
3. Basis completeness/self-duality (prop:cohomological-embedding) that guarantees the torus-knot basis is complete.



## PROGRESS 2026-08-22 (3) — active-shell numerator: idempotent sandwich collapse PROVED

Wired into the general Hecke Markov-trace infra (QOU.Hecke.MarkovTrace, which carries trace : A →ₗ[R] R + cyclic tr(xy)=tr(yx) + normalised). Added two generic-ring lemmas (sorry-free, #print axioms [propext, Classical.choice, Quot.sound]):
- MarkovTrace.trace_idempotent_sandwich (e x : A) (he : e*e=e) : trace (e*x*e) = trace (e*x)
- MarkovTrace.trace_idempotent_sandwich' : trace (e*x*e) = trace (x*e)

Derivation: tr(e·x·e) = tr(e·(e·x)) [cyclic] = tr((e·e)·x) = tr(e·x) [idempotency]. Pure consequence of the M2 cyclicity axiom.

This formalizes the Pauli-FULL-shell branch of F(τ,N): its numerator |tr_M(e_{(1³)}·τ·T_β·e_{(1³)})| simplifies to |tr_M(e_{(1³)}·τ·T_β)| — the outer alternating-idempotent sandwich collapses. So the active-shell F numerator STRUCTURE is now derived, not opaque.

STILL OPEN (remaining deep content):
1. The VALUE tr_M(e·τ·T_β) and the denominator tr_M(T_β) as explicit closed forms — needs the weighted Wedderburn sum tr_M = Σ_λ y_λ χ^λ instantiated for the specific τ, T_β=σ_0σ_1⁻¹, e_{(1³)} (the y_λ closed forms exist in schur_principal_mpmath / WenzlSchurElement but aren't wired to a general braid-word trace in Lean).
2. Shell-assignment (which shell active) + basis completeness (prop:cohomological-embedding).
Progress ladder so far: collapse mechanism (1) + inactive branches (2) + active-numerator idempotent collapse (3).



## ═══ TIERED WORKPLAN (2026-08-23) ═══

Goal: fully derive cor:spectral-decomposition-qvalue's F(τ,N) = |tr_M(e·τ·T_β·e)|/|tr_M(T_β)| and the exact decomposition, in Lean. Ordered by tractability.

**T0 — collapse bookkeeping [DONE].**
  - knot_operator_product_collapse (#5481): ∏ mostly-1 factors → active.
  - shellFactor + inactive branches (#5491): non-embeddable/unchanged ⇒ F=1.
  - trace_idempotent_sandwich (#5496): tr(e·x·e)=tr(e·x), numerator outer-e collapse.

**T1a — denominator closed form [DONE 2026-08-23].**
  MarkovTrace.trace_gen_mul_invGen: tr_M(σ_i·σ_j⁻¹) = z²−(q−q⁻¹)z for i<j.
  So tr_M(T_β)=tr_M(σ_0σ_1⁻¹)=z²−(q−q⁻¹)z. sorry-free, no sorryAx.

**T1b — numerator value tr_M(e_{(1³)}·τ·T_β) [NEXT, medium].**
  Needs: e_{(1³)} the alternating Young idempotent of H_3 as a concrete Hecke
  element (check QOU.Hecke for a Young-symmetrizer def; if absent, define via the
  antisymmetrizer over S_3). Then tr_M of the specific word e·τ·T_β. For the
  trefoil τ=σ_1² the σ_1²-trace closed form already exists
  (MarkovTraceTower.trM_sigma1_sq / TrMHopfSigma1SqClosedForm). Tractable for
  small specific τ; general τ needs T2.

**T2 — general braid-word tr_M via weighted Wedderburn sum [KEYSTONE, hard].**
  Wire tr_M = Σ_λ y_λ χ^λ to a general braid-word trace. y_λ closed forms exist
  in schur_principal_mpmath / WenzlSchurElement (compute side) but not as a Lean
  A→R trace on arbitrary words. This is the 08a2 keystone-de-abstraction epic.
  Prereq for the general active-shell value + exactness.

**T3 — shell-assignment [physical].**
  Model which shell is active (converting neutron's shell) and that all others
  are unchanged/non-embeddable, discharging shell_product_collapse's hypothesis
  for the real nuclear decay, not an abstract Finset.

**T4 — basis completeness [hard, conj-backed].**
  prop:cohomological-embedding (Rosso-Jones completeness + self-duality
  τ(r,s)↔τ(s,r)). Guarantees the torus-knot basis is complete ⇒ (v) exactness.
  Depends on T2.



## PROGRESS 2026-08-23 (4) — T2 keystone: first brick (weighted-trace cyclicity)

Started the T2 keystone (general braid-word tr_M = Σ_λ y_λ χ^λ) in
QOU/MathlibExt/MarkovTrace.lean §5:
- weightedCharacterTrace s dim ρ y w = Σ_{i∈s} y i · (ρ i).character w — the
  Wedderburn-weighted trace shape, per-block dimensions dim i, over a finite
  index set (the partitions λ⊢n). y_λ are the compute-side input (not fixed).
- weightedCharacterTrace_append_comm: the weighted sum inherits Markov cyclicity
  (M2) — tr_M(v++w)=tr_M(w++v) — derived block-by-block from character_append_comm
  via Finset.sum_congr. Independent of the particular y_λ.

lean-direct exit 0; #print axioms no sorryAx; audit 0 defects.

So the Wedderburn-weighted trace is now KNOWN to be a class function (M2) whatever
weights are supplied. STILL OPEN for the full tr_M: fixing the y_λ(q) values
(the deep compute-side closed forms), M1 normalisation (tr_M 1 = 1 ⟹ Σ y_λ d_λ = 1),
M3 Markov peel, and then the specific numerator tr_M(e_{(1³)}·τ·T_β). Ladder:
collapse mechanism + inactive branches + numerator idempotent collapse + denominator
+ weighted-trace cyclicity (this). The y_λ-value fix remains the 08a2 keystone core.



## PROGRESS 2026-08-23 (5) — T2 brick 2: identity value (M1 shadow)

weightedCharacterTrace_nil: tr_M(1) = Σ_λ y_λ·d_λ (χ^λ(1)=tr(𝟙_{d_λ})=d_λ via
eval_nil+trace_one+card_fin). So M1 normalisation tr_M(1)=1 ⟺ Σ y_λ d_λ = 1 —
the relation that pins y_λ given the block dims. lean-direct exit 0, no sorryAx.

T2 structural bricks now landed (PR #5528): M2 cyclicity + M1 identity-value, both
independent of the y_λ values. The Wedderburn-weighted trace has its class-function
property AND its normalisation-relation established.

HONEST WALL (08a2 keystone core, genuinely large): what remains for the full tr_M
is (a) the y_λ(q) CLOSED-FORM VALUES — the compute-side schur_principal_mpmath /
WenzlSchurElement results, which must be transcribed/derived into Lean and shown to
satisfy Σ y_λ d_λ = 1 + the M3 Markov peel; (b) M3 (Markov peel) as a theorem; (c)
the concrete e_{(1³)}, τ, T_β braid elements + the numerator value. This is
multi-session infra, not a single-session brick — the structural scaffolding (M1/M2
shadows) is now in place for it.
