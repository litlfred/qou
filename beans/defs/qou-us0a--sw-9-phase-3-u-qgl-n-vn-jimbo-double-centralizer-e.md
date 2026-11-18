---
# qou-us0a
title: 'SW-9 (Phase 3): U_q(gl_N) + V^⊗n + Jimbo double centralizer End_{U_q}(V^⊗n)=im H_n(q)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T19:33:08Z
updated_at: 2026-11-15T13:40:00Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

Full quantum Schur-Weyl: the U_q(gl_N) R-matrix action on V^⊗n, H_n(q)→End(V^⊗n), double centralizer + V^⊗n=⊕_λ L_λ⊗S^λ. Hardest; needs a U_q(gl_N) model (none in Mathlib). Ref: [jimbo1986].

## Refine (recon): NO Jacobson density / double-centralizer / bicommutant in Mathlib (Subalgebra.centralizer exists but no centralizer_centralizer). This is the largest gap and the heart of SW duality. NOTE: SW-8/R2-inst (the HeckeWedderburnData instance) is reachable via SW-7 without SW-9 — SW-9 is the full V^⊗n duality, a separate Phase-3 goal.


## Measured 2026-08-19 — still not started, and still correctly deprioritised

Nothing in the tree touches U_q(gl_N) or a double centralizer. Recon finding
still holds: no Jacobson density / bicommutant in Mathlib v4.24.0
(`Subalgebra.centralizer` exists, `centralizer_centralizer` does not). Confirmed
that SW-8/R2-inst was reachable without this (`qou-tpl5` closed at n=3), so this
remains a separate Phase-3 goal rather than a blocker for the Wedderburn arc.


## 2026-09-05 — the centralizer half is now USED, and the gap is exactly where this bean says

Branch `claude/hecke-cyclicity-markov-2026-09-05` (PR #6845) is the first thing
in the corpus to actually use `Subalgebra.centralizer` on the Hecke action, so
the recon finding in this bean can be sharpened from "Mathlib has the
definition" to "the definition is enough for one direction and the missing
lemma is exactly the other".

**What landed.** `QOU/IwahoriHecke/QTraceCyclic.lean` proves

    heckeActionN_mem_weightCentralizer :
      heckeActionN q qi hqi x ∈ Subalgebra.centralizer R {siteWeight w}

for **every** `x`, by corestricting the action along `liftBalanced` into the
subalgebra and composing back with `Subalgebra.val` (`hom_ext_sigma`). No
induction over the algebra is needed — subalgebra closure does the work. That
gives full cyclicity of the site-weighted trace and hence Markov move I.

**Why that is not this bean.** The weight `W = diag(∏ₘ w(aₘ))` is a *single*
diagonal operator, not the `U_q(gl_N)` action, so this is a containment in the
centralizer of one element — nowhere near `End_{U_q}(V^{⊗n}) = im H_n(q)`. The
two things this bean still needs are unchanged:

1. a `U_q(gl_N)` model (nothing in Mathlib, nothing in the corpus);
2. `centralizer_centralizer` / Jacobson density / bicommutant — **still absent
   from Mathlib at v4.24.0**, re-checked 2026-09-05.

**Anchor for whoever picks it up.** At `N = 2` the image is `TL_n(q)`, and
"surjective onto the commutant" and "not injective" are two faces of one fact —
the kernel is `ker(H_n ↠ TL_n)`, dimension `n! − Catalan(n)` (1, 10, 78, 588,
4611, 38890 at n = 3…8). So a `Fin 2` attempt proves the Temperley–Lieb
statement, not the general one; the general one wants `N ≥ n`.

## Re-scoped 2026-11-15 (owner tap, E1 bean triage)

Generic q over an ordered field is done: `range_jimbo_eq_commutant` / `_cartan` (#7864), plus the Jantzen coproduct identification (#7898). **Still open:** the any-field case, tracked as issue #7874 (O2–O6). This bean now tracks only that.

## Round 90 Lean 4 + 80-dps Witness Formalization (PR #8481)
- Module: `QOU.Foundations.MachineryConjectureCarrierRegistryThreeBatchDefectDrainDoubleCentralizerBalanceLongExactSequencePayoffParallelogramArgumentPrinciple`
- Commit 1 (code + probe): `a9f0f1224d140032ab84905edb79a825b0ec07fe`
- Commit 2 (`.witness.json`): `2e6c78442e063cad6ad9aa9c49b55c365f4be789`
- PR: https://github.com/litlfred/qou/pull/8481
