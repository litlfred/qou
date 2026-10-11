---
# qou-q425
title: 'M6: redo rj-canonical-inner-product in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-11T07:42:51Z
parent: qou-d8c7
---

predicted-spectra/rj-canonical-inner-product.md:8 defines tr_M with z = z_C into Q(q^1/2) (4 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: restated in D on PR #7562: tr_M into Q(q), z = q^2/[2]_q, d_lambda = sl2 hook-content dim prod[2+c]/[h], w_lambda = d_lambda/[2]^r (sympy-checked n=3, normalisation 1). Form degenerate: radical = classes with >2 rows. OPEN: part (iii) Rosso-Jones not re-verified (antisymmetric eigenvalue sign -q^-1 missing from omega_lambda = q^c). Uniqueness claim in (ii) restricted to the two-row part.


2026-10-10 (branch claude/rj-inner-product-d-2026-10-10): part (iii) re-verified in exact sympy over Q(q), probe computations/probes/rj_inner_product_conventionD_torus_probe.py. Normalisation: (sigma-q)(sigma+q^-1)=0, [n]=(q^n-q^-n)/(q-q^-1); block's z=q^2/[2] IS z_D=q^3/(q^2+1) symbolically (no rescaling). Ocneanu weights solved from the Markov conditions on Hoefsmit seminormal irreps equal d_lambda/[2]^r for r=2,3,4 (all 3+-row weights 0). Torus braids (sigma_1..sigma_{r-1})^s traced directly: printed form sum_{lambda|-r} d_lambda q^{c s} holds ONLY for r=2, s even (links); 'add the -q^-1 sign' fixes r=2 but fails at r=3 -- the sign was not the only defect (wrong index set: all partitions vs hooks; wrong exponent c*s vs 2cs/r). Verified form, every coprime (r,s) tested at r=2,3,4: [2]^r tr_M(gamma^s) = sum_hooks (-1)^j d theta^{s/r} = [r+1] q^{s(r-1)} - [r-1] q^{s(r-3)}, theta=q^{2c} (full twist checked at s=r). Unknot-normalised [2]^{r-1} q^{-2e} tr_M = Jones at t=q^-2 (trefoil). Block (iii) rewritten to this. (ii): 'every diagonal form compatible with tr_M(1)=1 is a scalar multiple' is FALSE (one free entry per two-row class); restated as form = [2]^r tr_M(p_lambda p_mu), unique because the Markov trace is unique given z. NOT DONE: Lean carrier QOU/Archimedean/rj_canonical_inner_product.lean still has fields claim_unique_up_to_scalar (false as stated) and jonesPoly_eq_eval (old wrong RJ shape) -- a self-assuming context with a false field; needs a Lean follow-up (slv0 is completed and predates this). .qa.json sidecar now stale. Closeable for the .md once merged; the Lean carrier is the remaining work.

2026-10-10 Lean follow-up (commit 53f1f43fd): HeckeRepRingContext removed from QOU/Archimedean/rj_canonical_inner_product.lean (no Lean consumers anywhere; scripts/unbounded-quantifier-audit.py and docs/audits/2026-08-29-rosso-jones-index-set-probe.lean carry standalone copies, untouched). Now sorry-free over a generic Field, imports QOU.MathlibExt.QIntegerCanonical (qIntBal): markovZD_eq (q^2/[2] = z_D); hookContent_row (prod [2+i] = [r+1] prod [r-i]); hookContent_hook (d_(m,1)=[m], cleared); h2Trace_rossoJones: in H_2(q) with sigma^2=(q-q^-1)sigma+1, tr(1)=1, tr(sigma)=z_D, [2]^2 tr(sigma^s) = [3]q^s + (-q^-1)^s for every s; h2Trace_rossoJones_odd = block's [r+1]q^{s(r-1)}-[r-1]q^{s(r-3)} at r=2; old_form_ii_false_r2 refutes the old field at r=2. lean-direct -DautoImplicit=false -s 65536 exit 0, axioms propext/Classical.choice/Quot.sound only. STILL OPEN: (iii) for general r (cited, probe r<=4) and Markov uniqueness for (ii) are not formalised; deliberately not encoded as a class field (unconstrained trace datum = self-assuming). Needs general-r Markov trace infra (QOU.IwahoriHecke.MarkovTrace). Do not close.

2026-10-10 (branch claude/rj-general-r-lean-2026-10-10, commit edc058fa8c): r = 3 formalised sorry-free over a generic Field in QOU/Archimedean/rj_canonical_inner_product.lean. H_3(q) coordinates on {1,s1,s2,s1s2,s2s1,s1s2s1}; right-mult tables derived from Hecke s^2=(q-q^-1)s+1 and braid relation in ANY R-algebra (H3.eval_rs1, H3.eval_rs2, H3.eval_gammaPow: (s1s2)^s = eval(gammaPow s)). Markov values on the basis forced by t1=1, t s1=z, cyclicity, Markov t((c+d s1)s2)=z t(c+d s1) (H3.markov3_unique). Spanning of the generated subalgebra + uniqueness: H3.exists_eval_of_mem_adjoin, H3.markov3_unique_adjoin (= (ii) at r=3). Value: h3Trace_rossoJones: [2]^3 tr_M((s1s2)^s) = [4]q^{2s} + [2] chi(s), chi=2 if 3|s else -1, every s (proof: trivial character multiplicative => q^{2s}; residual [2]^3 tr - [4] triv invariant under the full twist gamma^3 as a 6-variable identity; three base cases). h3Trace_rossoJones_coprime = [r+1]q^{s(r-1)} - [r-1]q^{s(r-3)} at r=3; h3_markov_rossoJones states it for every Markov trace. lean-direct -DautoImplicit=false -s 65536 exit 0; #print axioms propext/Classical.choice/Quot.sound. STILL OPEN: general r for (iii) and for Markov uniqueness (needs an H_r normal-form/spanning theorem; QOU.Hecke.markov_trace_unique rests on markov_trace_unique_axiom, an axiom, and the other MarkovTrace modules carry the trace as class data, so none can be built on). r=4 (24-dim H_4) not attempted. Do not close.


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


## 2026-10-10 — general-n spanning + Markov uniqueness PROVED (branch claude/hecke-spanning-theorem-2026-10-10)

New library files (sorry-free, lean-direct -DautoImplicit=false exit 0; #print axioms = propext, Classical.choice, Quot.sound):
- QOU/IwahoriHecke/JonesNormalForm.lean — any R-algebra with s : N -> A satisfying HeckeFamily N a b s (s_i^2 = a s_i + b, braid, far-commute; convention D is a = q - q^-1, b = 1). adjoin_eq_level: adjoin(s_0..s_{n-1}) = span(words s n), words(n+1) = {x * s_n...s_j : x in words n, j <= n+1}; card_words_le: card <= (n+1)!. markov_unique / markov_unique_of_adjoin_eq_top: normalised, cyclic, Markov (t(x s_k) = z t(x) for x in adjoin(s_<k)) functionals with equal z agree on every level <= N.
- QOU/IwahoriHecke/JonesNormalFormQuot.lean — markov_unique_quot on the presented QOU.Hecke.IwahoriHecke K q N (verified against a freshly rebuilt Hecke cone, since the Aug-30 cache predates source edits).

STILL OPEN: (1) Rosso–Jones for general r — uniqueness reduces tr((s_0...s_{r-2})^s) to a normal-form computation, but a closed form for general r needs the Wedderburn/Ocneanu-weight structure (or the full-twist centrality + hook-character argument), not formalised; only r = 2, 3 proved. (2) Existence of the Markov trace (Ocneanu) and linear independence of the words (T_w basis) — not proved. (3) markov_trace_unique_axiom NOT discharged: the class QOU.Hecke.MarkovTrace lacks the cross-level Markov field. Replacing it would need: add that field, then instantiate s i := embed <i> (0 above n), a := q - q^-1, b := 1, adjoin = top from HeckeAlgebra.spans, and apply markov_unique_of_adjoin_eq_top. Unverified suspicion: as stated (only tr(sigma_i) and tr(sigma_i sigma_j) fixed) the axiom's hypotheses are too weak at n >= 3 generators (H_4: 5 irreducible characters vs 3 constraints), which would make it refutable — not checked.
Not closeable: general-r Rosso–Jones open.


## 2026-10-10 — Rosso–Jones at r = 4 proved; torus-braid trace shown algebra-independent for every r (branch claude/rosso-jones-general-r-2026-10-10, head d84e6b9c5e)

Sorry-free over a generic Field (q != 0, q^2 != 1, q^2+1 != 0). lean-direct -DautoImplicit=false -s 65536 exit 0 against a shadow with JonesNormalForm, QIntegerCanonical and its cone rebuilt (cached oleans predate the sources). #print axioms: propext, Classical.choice, Quot.sound.

- QOU/Archimedean/RossoJonesH4.lean. H4 coordinates as four H3 vectors (cosets 1, s3, s3s2, s3s2s1). Right multiplication by s1, s2, s3 is derived in any R-algebra from the Hecke, braid and far-commutation relations (H4.eval_rs1/2/3). H4.markov4_unique: a normalised, cyclic functional that is Markov at levels 2 and 3 is forced to H4.markovTr. Existence: tau = ([5] chi_(4) + [3] tr_W(4,2) + tr_W(4,0))/[2]^4 on R x M3 x M2, with s_i = q - e_i on the TL standard modules, satisfies every Markov condition with z_D (RJ4.tau_*). On those modules gamma^4 = q^4 and gamma^2 = 1. Result (h4_markov_rossoJones, every s, every Markov trace on every algebra): [2]^4 t((s1s2s3)^s) = [5] q^{3s} + [3] q^s chi4(s) + chi2(s), with chi4 = 3 if 4|s else -1 and chi2 = 2 if 2|s else 0. For odd s (h4Trace_rossoJones_coprime): [5]q^{3s} - [3]q^s = [r+1]q^{s(r-1)} - [r-1]q^{s(r-3)} at r = 4. Cross-checked in exact sympy beforehand (identity [2]^4 markovTr4 = [5]triv + [3]tr_B + tr_C on all 24 coordinates; s = 0..8).
- QOU/IwahoriHecke/MarkovTransfer.lean. The presented algebra Pres N a b is RingQuot of FreeAlgebra R (Fin N) by the type-A relations, generated by its generators. lift maps it to any HeckeFamily algebra. markov_transfer: Markov traces with the same z on two different Hecke-family algebras agree on lift of every element. markov_transfer_cox: t((s0...s_{n-1})^p) is the same number in every such algebra, for every n <= N and every p. So for general r the torus-braid trace depends only on (a, b, z, r, s), and a closed form at a given r needs one model with a computable Markov trace.
- Docstrings in rj_canonical_inner_product.lean and JonesNormalForm.lean and the block .ts status note are updated to point here. No .md changed. markov_trace_unique_axiom and the MarkovTrace class are untouched.

STILL OPEN (general r): the general-r model. That means the TL standard modules W_{r,j}, a proof that sum_j [j+1] tr_{W_{r,j}} / [2]^r is Markov with z_D for every r, and tr(gamma_r^s) on each W_{r,j}. The expected answer is: Delta^2 = gamma^r acts on W_{r,j} by a scalar, and for coprime s the trace is nonzero only on the hook modules j = r and j = r-2. With those three inputs, markov_transfer_cox gives the general-r theorem. Also open: Ocneanu existence on the presented algebra and linear independence of the words. Do not close.


## 2026-10-10 — markov_trace_unique_axiom was FALSE; removed and replaced (branch claude/markov-axiom-check-2026-10-10, head c2b2848e01)

**Verdict.** `QOU.Hecke.markov_trace_unique_axiom` (two `MarkovTrace n q A` with equal `z_param` have equal `trace`) is false as stated, so as an `axiom` it made the environment inconsistent. The class fields (normalised, cyclic, trace_gen, trace_prod_gen) fix only 4 of the 5 class-function coordinates of a cyclic trace on H_4(q) (classes 1, s0, s0s2, s0s1, s0s1s2); the 4-cycle coordinate s0s1s2 is free.

**Counterexample (Lean, sorry-free):** `QOU/Hecke/MarkovTraceClassNotUnique.lean`. On the tree's own H4A (instHeckeAlgebraH4A, any field K, any q), with tr_w = markovTraceH4A K q w (cyclic for every w): t_Z = 4 tr_Z - 3 tr_{Z+1} - tr_{Z-1} + tr_{Z+2}. Weights (4,-3,-1,1) at offsets (0,1,-1,2) have moments sum a = 1, sum a d = 0, sum a d^2 = 0, sum a d^3 = 6. So t_Z(1)=1, t_Z(s_i)=Z, t_Z(s_i s_j)=Z^2 (every class field holds, z_param = Z), but t_Z(s0 s1 s2) = Z^3 + 6 while tr_Z(s0 s1 s2) = Z^3. `mixMarkov_trace_ne` (needs 6 != 0 in K); `markov_trace_unique_axiom_false` = negation of the axiom statement at universe 0 (QQ, q=2, Z=0). #print axioms: propext, Classical.choice, Quot.sound.

**Repair.** Axiom deleted. `markov_trace_unique` now takes `MarkovTrace.IsMarkov` (cross-level (M3): tr(x * s_i) = z tr(x) for x in adjoin of generators with idx < i) for both traces and is proved from `JonesNormalForm.markov_unique_of_adjoin_eq_top` via `genSeq` (HeckeFamily (n-1) (q - q^-1) 1 from the class relations; adjoin = top from HeckeAlgebra.spans). Class `MarkovTrace` unchanged; no code used the axiom or the old theorem. Same axioms as above.

**Verified (lean-direct, -DautoImplicit=false -s 65536, shadow over the restored cache):** JonesNormalForm, Hecke/MarkovTrace, Shared/MarkovTraceClaim, Hecke/MarkovTraceOnH4A, Hecke/MarkovTraceClassNotUnique (built with -o); direct importers hecke_mass_trace, tmli_constituent_composite_agreement, Hecke.lean, MarkovTraceH2, MarkovTraceOnH3A, Hecke/Wedderburn, MarkovBondFactor, ClosedFormInterfaceFactors, plus comment-edited rj_canonical_inner_product, BorromeanCanonicalTraceDerivation, JonesNormalFormQuot: all exit 0.

**Still open.** No instance in the tree is yet proved to satisfy IsMarkov (markovTraceH2 / H3A / H4A would be the first); until one is, markov_trace_unique has no proved application. Dated audit docs citing the axiom were left as historical records.



## 2026-10-11 — the concrete Markov traces satisfy (M3); markov_trace_unique now has applications (branch claude/markov-crosslevel-instances-2026-10-11, head 4add0ad405)

New QOU/Hecke/MarkovTraceIsMarkov.lean, sorry-free, lean-direct -DautoImplicit=false -s 65536 exit 0 against a private shadow with the whole 43-module import cone rebuilt (cached oleans dated 2026-08-24 predate the sources). #print axioms on all 7 results: propext, Classical.choice, Quot.sound.
- isMarkov_H2 / isMarkov_H3A / isMarkov_H4A: (markovTraceH2 R q z).IsMarkov, (markovTraceH3A K q z).IsMarkov, (markovTraceH4A K q z).IsMarkov, for EVERY z (Ocneanu's trace exists for every z; convention D is one specialisation). No instance failed (M3).
- Method: closure lemma mem_of_mem_adjoin_of_mul_mem (a submodule containing 1 and closed under right multiplication by S contains adjoin S). Level 0: K·1. H3 level 1: coords 2..5 vanish, peel = H3.trM_markov_σ₁. H4 level 2: image of iota34, peel = trM4_markov_σ₂ + trM4_iota34_stabilizes. H4 level 1: iota34 of the H3 level-1 subspace, iota34_mulσ₁ + H3.trM_markov_σ₁. No word enumeration needed.
- Payoff: markovTraceH2_unique / markovTraceH3A_unique / markovTraceH4A_unique — every MarkovTrace on the tree's H_n (n = 2,3,4) satisfying IsMarkov equals the concrete trace at its own z_param (first applications of markov_trace_unique). mixMarkov_not_isMarkov: the class-satisfying counterexample t_Z of MarkovTraceClassNotUnique is NOT (M3) (over fields with 6 != 0) — IsMarkov is exactly the missing condition.
- Docstrings updated: Hecke/MarkovTrace.lean, IwahoriHecke/JonesNormalForm.lean, Archimedean/rj_canonical_inner_product.lean (comment-only). Recompiled importers: MarkovTransfer, MarkovBondFactor, hecke_mass_trace, tmli_constituent_composite_agreement, RossoJonesH4 (exit 0). NOT rebuilt (comment-only upstream change): JonesNormalFormQuot, Hecke/Wedderburn, ClosedFormInterfaceFactors, QOU/Hecke.lean.
STILL OPEN: general-r Rosso–Jones; Ocneanu existence on H_n for n >= 5 (no MarkovTrace constructed there); linear independence of Jones words.


## 2026-10-11 — general-r infrastructure (branch claude/tl-standard-modules-2026-10-11, head 2842f35b43)

Route taken: the V^{(x)r} Jimbo R-matrix model (V = R^2), uniformly in r, rather than explicit link-state W_{r,j}. All sorry-free, lean-direct exit 0 with -DautoImplicit=false, axioms propext/Classical.choice/Quot.sound. Generic [Field R], convention D z_D = q^3/(q^2+1).

- QOU/IwahoriHecke/TensorMarkovModel.lean: strand_heckeFamily (HeckeFamily N (q-q^-1) 1 at every N); trace_markov (CROSS-LEVEL Markov: tr(W (X S_k)) = z_D tr(W X) for X in adjoin(S_0..S_{k-1}), every k<N); tau / presTrace normalised+cyclic+Markov (Ocneanu existence on Pres N for every N); markov_cox_eq_quantumTrace' (every normalised cyclic Markov trace with z_D on any Hecke-family algebra equals the quantum trace at n+1 sites on (s_0..s_{n-1})^p).
- QOU/IwahoriHecke/TensorTemperleyLieb.lean: tlRep : TLFin R (q+q^-1) N ->a End(V^{(x)(N+1)}), tlRep(e_a) = q - sigma_a (S_eq_q_sub_tlRep). The adjacency relation is the 8x8 identity F12F/F21F (needs dim V = 2), transported by embedTriple.
- QOU/Archimedean/RossoJonesGeneral.lean: extremal weight spaces proved (T_0 = T_r = q^{s(r-1)}); markov_rossoJones_of_middle: under the NAMED hypothesis MiddleWeightTraces q n p, q^{2p}(q^2+1)^{n+1} t(gamma^p) = (sum_{m=0}^{n+1} q^{2m}) q^{p(n+2)} - (sum_{m=1}^{n} q^{2m}) q^{pn}, i.e. [2]^r tr(gamma^s) = [r+1] q^{s(r-1)} - [r-1] q^{s(r-3)}.
- computations/probes/rj_weight_space_trace_probe.py (exact sympy): MiddleWeightTraces (q^{2s} T_m = q^{s(r+1)} - q^{s(r-1)}, 0<m<r) holds for every coprime (r,s), r=2..5, s<=2r+1, and FAILS for every non-coprime case tested.

STILL OPEN (not proved): (1) MiddleWeightTraces for general coprime (r,s) — the coprime vanishing is now isolated to this single weight-space statement; (2) explicit standard modules W_{r,j} as separate objects; (3) quantum Schur-Weyl identification tr_q = sum_j [j+1] tr_{W_{r,j}} / [2]^r. The task's piece 3 (traces on each W_{r,j}) is therefore not done in its stated form.
