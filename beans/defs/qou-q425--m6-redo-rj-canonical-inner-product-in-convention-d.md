---
# qou-q425
title: 'M6: redo rj-canonical-inner-product in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-10T18:34:21Z
parent: qou-d8c7
---

predicted-spectra/rj-canonical-inner-product.md:8 defines tr_M with z = z_C into Q(q^1/2) (4 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: restated in D on PR #7562: tr_M into Q(q), z = q^2/[2]_q, d_lambda = sl2 hook-content dim prod[2+c]/[h], w_lambda = d_lambda/[2]^r (sympy-checked n=3, normalisation 1). Form degenerate: radical = classes with >2 rows. OPEN: part (iii) Rosso-Jones not re-verified (antisymmetric eigenvalue sign -q^-1 missing from omega_lambda = q^c). Uniqueness claim in (ii) restricted to the two-row part.


2026-10-10 (branch claude/rj-inner-product-d-2026-10-10): part (iii) re-verified in exact sympy over Q(q), probe computations/probes/rj_inner_product_conventionD_torus_probe.py. Normalisation: (sigma-q)(sigma+q^-1)=0, [n]=(q^n-q^-n)/(q-q^-1); block's z=q^2/[2] IS z_D=q^3/(q^2+1) symbolically (no rescaling). Ocneanu weights solved from the Markov conditions on Hoefsmit seminormal irreps equal d_lambda/[2]^r for r=2,3,4 (all 3+-row weights 0). Torus braids (sigma_1..sigma_{r-1})^s traced directly: printed form sum_{lambda|-r} d_lambda q^{c s} holds ONLY for r=2, s even (links); 'add the -q^-1 sign' fixes r=2 but fails at r=3 -- the sign was not the only defect (wrong index set: all partitions vs hooks; wrong exponent c*s vs 2cs/r). Verified form, every coprime (r,s) tested at r=2,3,4: [2]^r tr_M(gamma^s) = sum_hooks (-1)^j d theta^{s/r} = [r+1] q^{s(r-1)} - [r-1] q^{s(r-3)}, theta=q^{2c} (full twist checked at s=r). Unknot-normalised [2]^{r-1} q^{-2e} tr_M = Jones at t=q^-2 (trefoil). Block (iii) rewritten to this. (ii): 'every diagonal form compatible with tr_M(1)=1 is a scalar multiple' is FALSE (one free entry per two-row class); restated as form = [2]^r tr_M(p_lambda p_mu), unique because the Markov trace is unique given z. NOT DONE: Lean carrier QOU/Archimedean/rj_canonical_inner_product.lean still has fields claim_unique_up_to_scalar (false as stated) and jonesPoly_eq_eval (old wrong RJ shape) -- a self-assuming context with a false field; needs a Lean follow-up (slv0 is completed and predates this). .qa.json sidecar now stale. Closeable for the .md once merged; the Lean carrier is the remaining work.

2026-10-10 Lean follow-up (commit 53f1f43fd): HeckeRepRingContext removed from QOU/Archimedean/rj_canonical_inner_product.lean (no Lean consumers anywhere; scripts/unbounded-quantifier-audit.py and docs/audits/2026-08-29-rosso-jones-index-set-probe.lean carry standalone copies, untouched). Now sorry-free over a generic Field, imports QOU.MathlibExt.QIntegerCanonical (qIntBal): markovZD_eq (q^2/[2] = z_D); hookContent_row (prod [2+i] = [r+1] prod [r-i]); hookContent_hook (d_(m,1)=[m], cleared); h2Trace_rossoJones: in H_2(q) with sigma^2=(q-q^-1)sigma+1, tr(1)=1, tr(sigma)=z_D, [2]^2 tr(sigma^s) = [3]q^s + (-q^-1)^s for every s; h2Trace_rossoJones_odd = block's [r+1]q^{s(r-1)}-[r-1]q^{s(r-3)} at r=2; old_form_ii_false_r2 refutes the old field at r=2. lean-direct -DautoImplicit=false -s 65536 exit 0, axioms propext/Classical.choice/Quot.sound only. STILL OPEN: (iii) for general r (cited, probe r<=4) and Markov uniqueness for (ii) are not formalised; deliberately not encoded as a class field (unconstrained trace datum = self-assuming). Needs general-r Markov trace infra (QOU.IwahoriHecke.MarkovTrace). Do not close.


## 2026-10-10: sidecar refresh NOT done, because the procedure no longer exists (no files changed)

**No sanctioned route refreshes the in-tree `<block>.qa.json` at platform pin `717aa19a`.** `cat-harness/content/pipeline/qa-paths.ts` (owner decision 2026-09-19) makes `test/results/block-qa/<mirror>.qa.json` the only WRITE target ("read both, prefer the new, write only the new"); the in-tree sibling is a read-fallback. Script verdicts go there and are gitignored (`qou.json` `qa` entry, owner ruling 2026-10-04 decision 11). Agent and human verdicts go to `test/attestations/block-qa/` on main (`cat-harness/schemas/qa-attestations.ts`, owner ruling D2(a) 2026-10-01). So AGENTS.md's remedy ("delete the stale `criteria.<crit>` entry and re-run qa-sweep") is obsolete, and hand-editing the in-tree file would fake currency (same call as `qou-99fk`). `scripts/check-sidecars.sh` does not measure staleness at all. It lists cached criteria from the in-tree file and always prints the qa-sweep line, so it cannot report these blocks "clean" whatever is done.

**Why the judgement half was not written either.** The platform design says to commit agent verdicts under `test/attestations/block-qa/`, and main has carried 9 such files since `896ded7a48` (today). But `qou-99fk` (todo, high) frames whether block-qa attestations belong in the tracked store as an owner call. `qou.json` describes `test/attestations/` as holding only the two bib ledgers. And no CLI records an agent verdict for a block-qa criterion: only qa-sweep and translation-block-qa call `writeCriteriaAttestations`, so the entry would have to be hand-written JSON. That is ambiguous, so nothing changed.

**Agent verdicts on the four `needs-agent` trap criteria**, from reading the .md and .ts at origin/main `ee2b758144`. They are recorded here, not in any store.

`prop:rj-canonical-inner-product`:
- thesis-restatement **pass**.
- performed-warmth **pass**.
- superlative **pass on the criterion itself**, but there is a real overclaim next to it. The opening sentence says the Markov trace "induces a **unique inner product**". Part (i) proves the form is degenerate: its radical is spanned by the classes with more than two rows. Part (ii) says diagonality does not determine the form, and that the only uniqueness is that of the Markov trace for a given z. The title "Canonical inner product" has the same tension. Suggested opening: "a symmetric bilinear form, determined by z".
- nonspeakable **pass**.

A real problem outside these four criteria: the final paragraph ("Until 2026-10-10 this proposition used …") is a dated revision note in scholarly prose. AGENTS.md §4d and one-voice Category H put such notes in `authorNotes` with `kind: "refined-framing"`. Neither problem was fixed, because content edits are out of scope here.
