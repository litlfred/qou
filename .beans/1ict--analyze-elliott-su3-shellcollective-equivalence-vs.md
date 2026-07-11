---
# 1ict
title: 'Analyze: Elliott SU(3) shell↔collective equivalence vs QOU Schur-Weyl shell picture'
status: completed
type: task
priority: normal
created_at: 2026-07-06T04:46:38Z
updated_at: 2026-07-11T19:10:00Z
parent: 4lss
---

## Resolution (2026-07-11)

Corpus-grep first (per the anti-guessing/corpus-grep discipline): the Elliott
literature anchor **already existed** in `observations/q-deformed-nuclear-models-comparison.md`
§"Elliott SU(3)" — it sites Elliott 1958 via `\cite{elliott1958}` (the correct
CSL ref, DOI 10.1098/rspa.1958.0072, already in `references.ts`) and gives the
answer to the "q->1 shadow?" question: **NO** — Elliott is the undeformed (q=1)
organizing symmetry; the magic-number signal of `prop:magic-numbers-from-q` is a
genuinely q!=1 coherence effect that vanishes at q=1, so Elliott is complementary,
not the classical limit of the mechanism. So the "remark/prose block + cite" part
of the deliverable was already done; NOT re-created (would duplicate).

The one genuinely-new categorical finding — the bean's core "does our
Schur-Weyl/Wedderburn shell decomposition already encode this equivalence?"
question — landed as an enhancement to that section: Elliott's SU(3) and the
many-body Hecke trace are the **two mutual centralizers of quantum Schur-Weyl
duality** on (C^3)^{⊗n}, i.e. the U_q(gl_3) factor (Elliott, at q=1) and the
H_n(q)/partition factor (our Hecke trace), degenerating to GL(3)×S_n at q=1 —
which is exactly `prop:shell-schur-weyl-self-duality`. The duality is an algebraic
identity at every q, so it coexists with (does not contradict) the magic signal
being q!=1. Cross-ref added to `uses[]`.

**Answer:** yes — the Wedderburn shell decomposition already encodes the
Elliott equivalence categorically, via `prop:shell-schur-weyl-self-duality`, with
Elliott sitting at the q=1 corner of that same duality.

Landed: content(elliott) commit on branch `claude/elliott-su3-schur-weyl-anchor-2026-07-11`.


Elliott (1958): HO magic-number boundaries map to SU(3) irreps; single-particle shell model = collective rotation, mathematically equivalent. QOU angle: does our Schur-Weyl/Wedderburn shell decomposition (observations/magic-numbers-from-q.md, particle-interactions/shell-schur-weyl-self-duality, wigner-su4-from-spin-isospin) already encode this equivalence categorically? Test whether Elliott SU(3) is the q->1 classical shadow of the H_k(q) Hoefsmit route. Deliverable: remark/prose block siting Elliott as literature anchor + cite arXiv 9605013. §7c: keep generic ring where algebraic.

CORRECTION 2026-07-06 (Copilot review): do NOT cite arXiv 9605013 as the Elliott SU(3) anchor — 9605013 is the SU_q(2) q-ROTOR paper (Minkov-Bonatsos, bean alyr), NOT Elliott. The Elliott anchor is Elliott 1958, Proc. R. Soc. Lond. A 245, 128 (add its own CSL ref id elliott1958); no uploaded PDF for it in this batch. Supersedes the '+ cite arXiv 9605013' in the original body above.
