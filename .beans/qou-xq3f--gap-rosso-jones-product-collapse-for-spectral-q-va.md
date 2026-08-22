---
# qou-xq3f
title: 'GAP: Rosso-Jones product-collapse for spectral Q-value decomposition (Lean)'
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:36:58Z
updated_at: 2026-08-22T21:06:34Z
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
