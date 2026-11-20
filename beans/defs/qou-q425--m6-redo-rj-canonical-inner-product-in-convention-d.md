---
# qou-q425
title: 'M6: redo rj-canonical-inner-product in convention D'
status: todo
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-11-20T09:30:00Z
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


## 2026-10-11 — MiddleWeightTraces proved for every coprime (r, s) (branch claude/rj-middle-weight-2026-10-11)

New QOU/Archimedean/RossoJonesMiddle.lean. It is sorry-free and works over a generic [Field R]. Checked lean-direct with -DautoImplicit=false -s 65536: exit 0, against a private shadow in which the RossoJonesGeneral cone was rebuilt. #print axioms gives propext, Classical.choice, Quot.sound only.
- middleWeightTraces_of_coprime (hq : q ≠ 0) (hcop : Nat.Coprime (n+1) p) : MiddleWeightTraces q n p.
- rossoJones_of_coprime: unconditional Rosso–Jones on V^{(x)(n+1)} for gcd(n+1, p) = 1.
- markov_rossoJones: the same, for every normalised cyclic Markov trace with z_D on any Hecke family, for coprime (r, s). Open item (1) of the previous entry is therefore CLOSED for coprime (r, s).
- How it works. gam_eq_G gives an explicit matrix for γ. Three identities hold: γ = ρ + E K, ρ E = E ρ', K E = γ − ρ'. Here E is the U_q(sl2) raising operator and ρ, ρ' are weighted cyclic rotations. pow_decomp turns them into a telescoping identity. That gives T_{m+1}(γ^p) = T_{m+1}(ρ^p) + T_m(γ^p) − T_m(ρ'^p). Under gcd(n+1, p) = 1, rot^p fixes only the constant states, so the middle traces of ρ^p and ρ'^p vanish. Then T_m(γ^p) = q^{np} − (q^{n} q^{-2})^p for every 0 < m < n+1.
STILL OPEN: the non-coprime case (torus links). The probe shows MiddleWeightTraces FAILS there, so a different statement is needed. Items (2) and (3) of the previous entry are untouched: explicit W_{r,j}, and quantum Schur–Weyl tr_q = Σ_j [j+1] tr_{W_{r,j}} / [2]^r. This bean stays open.


## 2026-10-12 — torus links, gcd(r,s) > 1: PROVED (branch claude/rosso-jones-torus-links-2026-10-12, PR #7737, commit bdea7900f1)

New file QOU/Archimedean/RossoJonesTorusLink.lean, sorry-free; axioms are only propext, Classical.choice and Quot.sound.
- T_gam_eq_sum: T_m(γ^p) = Σ_{j≤m} T_j(ρ^p) − Σ_{j<m} T_j(ρ'^p) for every p. The telescoping step pow_decomp / T_gam_succ never needed coprimality.
- rho_eq_wRot / rho'_eq_wRot: the weight of ρ (and ρ') at b depends only on (ones b, last letter of b).
- lastOnes_mul: a double count gives (n+1)·S = p·ones b for every rot^p-fixed b.
- card_fixSet: #{weight-j states fixed by rot^p} = C(d, j/e) if e | j, else 0. Here d = gcd(n+1,p) and e = (n+1)/d. The proof goes through Bezout and the d-periodic ↔ length-d word bijection perExt/restr.
- T_gam_pow, rossoJones_torusLink, markov_rossoJones_torusLink: tr(W γ^p) and every Markov trace with z_D on (s0⋯s_{n−1})^p, given as explicit finite sums for ALL (r,s).
- Closed form (d=gcd(r,p), e=r/d, a=p/d, j=ke): T_j(ρ^p) = C(d,k) q^{a[(r−j−1)(d−k)+(j−3)k]} and T_j(ρ'^p) = C(d,k) q^{a[(r−j−3)(d−k)+(j−1)k]}.
- Probe computations/probes/rj_torus_link_periodic_probe.py does exact Laurent-polynomial arithmetic with ints: 1350/1350 checks pass for r ≤ 6, p ≤ 2r+2. precision-gates.sh could not run in the sparse worktree (mpmath and qou_substrate missing), so its preflight failed and that is not a gate result. The probe contains no float.
- Verification: lean -DautoImplicit=false -s 65536 exits 0 against a shadow holding JonesNormalForm, MarkovTransfer, TensorMarkovModel, RossoJonesGeneral and RossoJonesMiddle. Those five oleans were missing from the restored cache.
- Still open: (2) the Schur–Weyl trace split T_m(X) = Σ_j tr(X|W_{r,j}) for q not a root of unity; (3) the modules W_{r,j}. The torus-link result does not depend on either.


## 2026-10-12 (later): items (2) and (3) PROVED, except the full-twist scalar (PR #7737, commit 4b3439b86d)
File: QOU/Archimedean/SchurWeylTrace.lean. Sorry-free; axioms are only propext, Classical.choice and Quot.sound. The hypothesis is QIntNonzero q r, i.e. [k]_q ≠ 0 for 1 ≤ k ≤ r. It covers q = 1 in characteristic 0.
- (2) trace_split: tr(X|V_m) = Σ_{j≤min(m,r−m)} tr(X|W_{r,j}), with W_{r,j} := ker E ∩ V_{r−j} (Wmod). It holds for every weight-preserving X with XE = EX.
  - Fm is the lowering operator. Em_Fm_comm and Dg_eq show [E,F] = diag([2·ones − r]).
  - qZ is the signed q-integer, with qZ_mul and sum_qZ.
  - Epow_inj: E^k is injective on V_m when 2m+k ≤ r.
  - Em_transpose: E^T(q) = cmp·E(q⁻¹)·cmp. With a rank argument this gives El_surj on the upper half.
  - trace_eq_trace_ker_add: trace across an intertwining surjection.
- (3) Proved: WP_gam and gam_comm_Em; gamW (γ^p on W_{r,j}); T_gam_pow_split; trace_W_gam_pow_split, which says tr(Wγ^p) = Σ_{2j≤r}(Σ_{m=j}^{r−j} q^{2m}) tr(γ^p|W_{r,j}).
- Probe computations/probes/rj_schur_weyl_trace_split_probe.py: 22504/22504 exact checks pass.
- STILL OPEN: the full twist γ^r acts on W_{r,j} by a scalar. The probe finds the scalar q^{r(r−1) − 2j(r−j+1)} for r ≤ 6. The proof needs the ribbon element (Δ² as a function of the quantum Casimir via Jucys–Murphy elements) or irreducibility of W_{r,j} under B_r. Neither is formalised.


## 2026-10-12 (later still): full-twist scalar PROVED (PR #7737, commit d4678e2306)
- SchurWeylTrace.lean §10–11, sorry-free; axioms are only propext, Classical.choice and Quot.sound. The hypothesis is QIntNonzero q r.
- gamW_fullTwist: γ^{rt} acts on W_{r,j} (for 2j ≤ r) as (twistScalar)^t, where twistScalar = q^{r(r−1)−2j(r−j+1)}.
  - Route: the telescoping γ^r = ρ^r + E K_r, with ρ^r the scalar s_j on V_j.
  - Then w = E^{r−2j} v, and γ^r w − s_j w = E^{r−2j+1} y. This vector is killed by E, so Epow_inj gives y = 0.
  - No ribbon element and no irreducibility were needed.
- finrank_Wmod (char 0): dim W_{r,j} = C(r,j) − C(r,j−1).
- trace_W_fullTwist and markov_fullTwist: per-module Rosso–Jones for the full twists.
- The probe's exact checks now also compare the scalar with the Lean twistScalar and the dims with the binomial formula: 22624/22624 pass.
- Not done: per-module Rosso–Jones for general s, not a multiple of r. That needs the action of γ (not only γ^r) on W_{r,j}, e.g. its eigenvalues. The torus-link formula itself is already proved in RossoJonesTorusLink.


## 2026-10-12: per-module trace of γ^p for EVERY p, PROVED (PR #7737, commit 61b4fc2a10)
SchurWeylTrace §12, sorry-free.
- trace_gamW (2j ≤ r): tr(γ^p|W_{r,0}) = q^{np}. For j ≥ 1, tr(γ^p|W_{r,j}) = rhoTr q n p j − rho'Tr q n p (j−1), where rhoTr and rho'Tr are the periodic-state closed forms. Proof: invert the triangular system T_gam_pow_split at m = j and m = j−1, then apply T_gam_succ.
- trace_W_gam_pow_explicit and markov_gam_pow_explicit: the per-module Rosso–Jones formula for every torus link T(r,p).
- Probe check (f) added: 22932/22932 exact checks pass.

**2026-10-12 — Jones normal words are linearly independent in Pres (sorry-free).** New file `QOU/IwahoriHecke/JonesWordsIndependent.lean`: `presEquivHecke : Pres N (q-qi) (q*qi) ≃ₐ[R] QOU.SchurWeyl.Hecke R q qi N` (same presentation, generator to generator; any CommRing R, any q qi); `presBasis` (via `HeckeCoset.stdBasisAny`, regular rep); `card_words_pres`: exactly (N+1)! distinct normal words; `words_pres_linearIndependent` and `wordsBasis` (words are a basis), `words_pres_linearIndependent_of_le` (every level n ≤ N). Hypotheses: [CommRing R] [Nontrivial R]; quadratic of the form s²=(q−qi)s+q·qi — covers convention D (qi=q⁻¹) and the unbalanced (qi=1) relation. NOT covered: a general pair (a,b) not of that form. Proof: span + rank condition gives |words| ≥ (N+1)!, with card_words_le equality; surjective endomorphism of R^{words} injective (OrzechProperty). Verified lean -DautoImplicit=false -s 65536 exit 0; #print axioms = propext, Classical.choice, Quot.sound. The remaining q425 items (closed Rosso–Jones for general r) are untouched.

**2026-10-12 — quantum Schur–Weyl for the whole braid algebra (sorry-free; branch `claude/rj-schur-weyl-2026-10-12`).** New file `QOU/IwahoriHecke/TensorSchurWeyl.lean`, importing `SchurWeylTrace` (qou-gd90). It does not restate anything that file already proves. Contents:
- The U_q(sl₂) coproduct built recursively on V^{⊗n} by Kronecker products: E_{n+1} = E_n⊗k + 1⊗e, F_{n+1} = F_n⊗1 + K⁻¹⊗f, K_{n+1} = K_n⊗k.
- `S_comm_E` / `S_comm_F` / `S_comm_K` / `S_comm_Ki`: every strand braid S q N i commutes with E, F, K and K⁻¹. Proved by induction on N (each braid is either S⊗1 or 1⊗Ř).
- `braidAlg_spec`: the same for every element of adjoin(range S), which also preserves weight.
- `E_eq_Em`: the coproduct E_{n+1} equals RossoJonesMiddle's `Em q n`.
- `trace_W_split`: tr(W X) = Σ_{2j≤r} (Σ_{m=j}^{r−j} q^{2m}) tr(X|W_{r,j}) for any weight-preserving X with X Em = Em X. This generalises `trace_W_gam_pow_split` from γ^p to all such X.
- `braidAlg_trace_split` and `braidAlg_trace_W_split`: both forms for every element of the braid algebra, under `QIntNonzero`.
- Verification: lean -DautoImplicit=false -s 65536 exit 0. `#print axioms` = propext, Classical.choice, Quot.sound.

Still open:
- The individual tr(X|W_{r,j}) are not computed for X other than γ^p.
- F-side / lowest-weight mirror. Not needed for the split.
- Status unchanged.


## 2026-10-12 — torus links re-checked; coprime and full-twist specialisations added (branch claude/rj-torus-links-2026-10-12)
A session was sent to prove the torus-link Rosso–Jones formula on the premise that the earlier attempt was lost in a container restart. It was not lost: RossoJonesTorusLink.lean (c35183cdca) is on main and already proves T_gam_pow, card_fixSet, rossoJones_torusLink and markov_rossoJones_torusLink for every gcd(r, s). This session first re-proved the same results independently in a standalone RossoJonesLinks.lean. That version used Euclid's gcd induction where main uses Bezout, and it also compiled sorry-free. It was then cut down, because it duplicated main's declaration names in the same namespace. What remains is new: it imports RossoJonesTorusLink and adds
- fixCount_zero, fixCount_mid_of_coprime: for gcd(n+1, p) = 1, fix(0) = 1 and fix(j) = 0 for 0 < j < n+1;
- T_gam_mid_of_torusLink, middleWeightTraces_of_torusLink: the coprime case derived from the general T_gam_pow, giving T_m(γ^p) = q^{np} − (q^n q^{-2})^p and MiddleWeightTraces;
- fixCount_full_twist: for p = (n+1)k, fix(j) = C(n+1, j).
Verification: lean -DautoImplicit=false -s 65536, exit 0, against a private shadow (the RossoJonesTorusLink cone was rebuilt there because its oleans are missing from the restored cache). #print axioms gives at most [propext, Classical.choice, Quot.sound]. Scratch probes re-run: rjlinks_probe.py reports ALL OK (N ≤ 6, p ≤ 8, every m), and rjlinks_plethysm.py reports bad 0 (N ≤ 7, p ≤ 12; the ratio to Rosso–Jones with ψ^e is a monomial framing factor).
Still open: the Adams-operation form of Rosso–Jones (Σ_k c_k [k+1] θ_k^{p/r} with ψ^e) is checked only by the probe and is not stated in Lean. The plethysm cross-check also leaves the framing monomial unidentified.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released. The D restatement and r = 2, 3 Lean landed (#7562; Rosso–Jones / Schur–Weyl work incl. #7737 merged). Open items per the last entries: general-r per-module Rosso–Jones for s not a multiple of r, and the Adams-operation form. These are open research, so the bean stays open.
