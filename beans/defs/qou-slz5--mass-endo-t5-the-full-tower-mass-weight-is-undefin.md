---
# qou-slz5
title: 'MASS-ENDO T5: the full-tower mass weight is undefined (D7 scopes convention D to decay only)'
status: todo
type: epic
priority: normal
created_at: 2026-10-10T06:48:53Z
updated_at: 2026-10-10T15:10:00Z
---

Thread (session https://claude.ai/code/session_01ST9RpvTF7JHNdUNafrjf9J). OWNER DECISION gating this thread: D7 (docs/coordination/2026-09-05-owner-gated-bean-triage.md, 2026-09-07) puts mass/binding on the full tower, but production tr_M_via_wenzl_bridge still applies D's two-row cap (keeps 0.0434% of H_12 at 4He). No full-tower mass weight is defined. Candidates: Molien (ruled only for Phi_k), C y_λ (excised), Ocneanu N≠2 (changes the trace).
Children: qou-oots, qou-fq0f, qou-24w9, qou-zf9n, qou-8jq2. Results built on D-weights for mass (zf9n TL-support 16.48%, 24w9 option table) lapse or need re-statement once the weight is chosen.


## 2026-10-10 rerun results
zf9n: TL support survives; the 3.4× cancellation, 16.48% capture and the 10A−5 near-match are grouped-word artifacts (sign flips on borromean words). Two committed witnesses (rho-w-crystal-vertex-trace, delta-lambda-canonical-residual) are stale — regeneration is owner-gated.


## 2026-10-10 — owner said 'try both': two-arm probe (session_01ST9RpvTF7JHNdUNafrjf9J)
computations/deltalambda/full_tower_weight_two_arm_probe.py (+witness), 8/8 checks; control reproduces binding_canonical Δtr < 1e-51. Arms are measures μ_λ (Σμ=1) entering tr = Σ(μ_λ/f^λ)χ^λ; borromean words; all p(3A) partitions; proton q0. Molien uses the Lean-proved balanced form f·q^{−κ_λ}·dim_q (molienSum_eq_qFactorial); the untwisted f·dim_q/[n]_q! sums to 0.922/0.824/0.703 at n=6/9/12.
TL-quotient |share| of Δtr: Molien 7.3% / 0.54% / 0.79% / 0.011% (D/T/³He/⁴He); Plancherel 16.9% / 3.4% / 4.5% / 0.35%. Under either full-tower weight the closure is NOT TL-supported. Molien tr(W_atom) ≈ 1e-75 at ³He/⁴He (zero to working precision; consistent with the regular trace picking the identity coefficient; exact vanishing NOT proved) so B_log undefined there. No ranking, no adoption (anti-fit).


## 2026-10-10 — relation to qou-d8c7 (session_01ST9RpvTF7JHNdUNafrjf9J)
Kept: this thread is cross-chapter (mass-theory / binding compute), outside qou-d8c7's scope rule ('a chapter block or its Lean/library module is the subject'). qou-d8c7 lists some of these beans as links (M6/M7/M9); chapter-subject beans stay with qou-d8c7.


Note qou-d8c7's M7 correction (#7552): the Molien ruling is scoped to the Φ_k functional, not to H_3 Wedderburn weights. This thread's question — what weight the FULL-TOWER mass/binding channel uses under D7 — is therefore still undefined, not settled by that ruling. Two-arm data (Molien balanced / Plancherel) is in computations/deltalambda/full-tower-weight-two-arm-probe.witness.json.


## 2026-10-10 OWNER RESPONSE (session_01ST9RpvTF7JHNdUNafrjf9J)
Owner: 'i think it may be plancherel. see what else in corpus' + D (derive first). So: corpus-search everything bearing on Plancherel (d_q^2/D^2) as the full-tower mass/binding weight, and attempt a derivation rather than adopt by result. Owner leaning is a hypothesis, not a ruling; no production change.


## 2026-10-10 — derivation step 1: structural conditions on a full-tower weight (session_01ST9RpvTF7JHNdUNafrjf9J)
Probe `computations/deltalambda/full_tower_trace_coherence_probe.py` (10/10, exact in Q(q,y); no float64).
- **Branching coherence** (one trace on the whole tower, w_λ = Σ_{μ=λ+□} w_μ) fails for **quantum Plancherel dim_q²/D²**, first at λ=(3) (26 failing λ for n ≤ 6; defect at q0 −1.298e-5). It holds at n = 1, 2. So Plancherel is not the weight of a single trace on the full tower. That is a structural exclusion *if* the mass functional must be one trace on H_∞. It is not excluded if the functional may be an unrelated per-n functional; owner to confirm which reading of D7 applies.
- **Molien f q^{−κ} dim_q/[n]!** is coherent, and so is its mirror (q^{+κ}). These are the two canonical traces (τ(σ_w) = δ for σ, resp. for σ⁻¹).
- **Ocneanu/Markov family at imaginary rank x = iy**: coherent, every weight > 0 (faithful on all λ), with z(y) = (q−q⁻¹)y²/(y²+1). y→0 gives Molien and y→∞ gives mirror Molien. Real rank gives a negative weight (sample x=3: column of length 12). So for real q>1, the positive Markov traces that are faithful on every partition are exactly z ∈ [0, q−q⁻¹] (≈ [0, 0.2091] at q0). Convention D's z_D = 0.6127 lies outside, consistent with D7.
- **Not selected:** which point of that interval. Candidates are an endpoint (a canonical trace, i.e. Molien) or the self-dual midpoint y=1, z=(q−q⁻¹)/2, fixed by σ ↦ −σ⁻¹ / λ ↦ λ'. That choice needs a further principle and is not made here.
- Checked for n ≤ 6 / n ≤ 5, not proved for all n. Next: formalise the λ=(3) Plancherel incoherence and the interval statement in Lean.


## 2026-10-10 — corpus-grep result (session_01ST9RpvTF7JHNdUNafrjf9J; paths 1-6, corpus_search MCP unavailable)
- **In the held literature, 'the Plancherel measure of a Hecke algebra' is the measure of the canonical symmetrising trace Tr(T_w)=δ_{w,1}.** Sources: Parkinson arxiv-1110.6212v2 sec-001:148-180; Geck/Chlouveraki hdr sec-002:47 and sec-025 Rem 6.21/6.43; Féray–Méliot arxiv-1001.2180v2 sec-017 (q-Plancherel = the Thoma point ω_q); Kerov q-Plancherel arxiv-2105.09342v1. Lean already proves this trace is Molien = z=0 Markov (qou-we2d: MolienSymmetrisingTrace.lean molienMarkovTrace_symmetrising, eq_molien_of_zero, sum_addable_molienWeight). So the owner's 'Plancherel', in the literature's sense, is the Molien endpoint; d_q²/D² is the RT/Verlinde weight (conjectural keystone origin) and is not coherent.
- Already proved: markovTrace_unique (determined by z); the Wenzl lattice; the D trace is not faithful (not_isFaithful_trLim); markov_param_eq_half_h (transpose-symmetric weights give z=h/2).
- Absent: no Lean statement of the faithful positive window [0, h]. The generic-z Markov property is one evaluation step from MolienSymmetrisingTrace's eval_zero_eq_of_eval_pow.
- Tension: qou-za3q (2026-09-13) adopted Wenzl z_D for the Ω₂ binding pairing, after D7. Not reconciled.
- Stale pre-D7 statements: TwoRowCapDerived.lean frames mass as two-row; the trace-convention-registry lists mass/binding as D. The z=h/2 Ocneanu measure is close to, but not equal to, d_q²/D² (agent's check at q=111/100).


## 2026-10-10 — Lean results (session_01SVz9wTyu9X4uLbfvEKADVH, PR #7612, issue #7611)
- **Plancherel incoherence, formalised** (`MathlibExt/PlancherelRestrictionIncoherent.lean`, sorry-free): d_q²/f weights on λ⊢4 restrict to a multiple of those on μ⊢3 iff [3]_q·(q−q⁻¹)⁴ = 0 (generic char-0 field). So for real q>0, q≠1, no tower trace carries them. This is the n=4→3 case of the probe's λ=(3) failure above. Do not re-formalise it.
- **Bond-letter identity** (`Hecke/TauBondLetter.lean`, sorry-free): τ(a·(cσ_i+d)·b) = d·τ(ab) for a,b avoiding σ_i. Under Molien = τ this gives tr_atom/tr_free = ∏ d_k (Markov ∏(z+d_k) at z=0). The pp letter is a bare σ, so the Molien trace is EXACTLY 0 at ³He/⁴He. At D the ratio is d_pn < 0. So the Molien endpoint makes B_log undefined at D, ³He and ⁴He. Matches the two-arm witness to 1e-51. Stated on the TwBasis carrier; port to HeckeCoset.symTrace is queued after #7596.
- Consequence for the interval [0, q−q⁻¹]: for 0 < z ≤ q−q⁻¹ the connected-sum ratio ∏(z+d_k) has z+d_pp = z > 0, but z+d_pn = z − h(1/2−δ/4) and z+d_nn = z − h, where h = q−q⁻¹. So z+d_nn ≤ 0 on the whole window, which is a sign obstruction for any log-binding with an nn bond. Not formalised.


## 2026-10-10 — Lean landed on this branch (1975a8f400, session_01ST9RpvTF7JHNdUNafrjf9J)
QOU/SchurWeyl/FullTowerTraceWindow.lean (sorry-free; axioms are standard only):
- **T2 (new; not on #7612):** every Ocneanu weight is a full-tower Markov trace for generic z with q²−1−qz≠0: normalisation, branching coherence and the Markov corner all hold. SeminormalRep.ocneanuMarkovTraceAt : MarkovTraceFamily R q q⁻¹ z, and eq_ocneanu_of_markov (every z-Markov trace is the Ocneanu-weighted one). This closes the 'Markov at general n open / proved only at n=3' caveat that #7612's OcneanuWeightPositiveWindow carries.
- T1 qPlancherel_not_coherent and T3 ocneanuWeight_pos_of_le duplicate #7612 (PlancherelRestrictionIncoherent, and OcneanuWeightPositiveWindow, which is the stronger iff). They are independent second proofs; #7612 is the reference for those two.
- Not proved here: the z=q−q⁻¹ endpoint trace; the window converse (done in #7612).
**Derivation status:** coherent Markov trace on H_∞ + positive + faithful on every λ ⟺ z∈[0,h], with Molien (z=0, the literature's Hecke Plancherel measure) at one end. The point is still not selected. Note from #7612 TauBondLetter: Molien gives tr exactly 0 at ³He/⁴He, so B_log is undefined there.


## 2026-10-10 — B_log on the faithful window: OPEN PROBLEM (owner: "leave as open problem"; session_01SVz9wTyu9X4uLbfvEKADVH)
Owner rejected evaluating B_log at z_D (option A) and asked to explore changing the functional (C), left open.
- **Where the collision comes from (upstream).** The live law `B = E_0·log(|tr_free|/|tr_atom|) = −E_0 Σ_bonds log f_b` (binding_log_free_energy.py, 2026-09-05 arc) was built on the convention-D trace, where every bond factor is positive (z_D+d: pp 0.613, nn 0.404, pn 0.508). D7 (2026-09-07) then moved mass/binding to the full tower. The two were never reconciled. Note the live code already takes absolute values.
- **Structural form.** The bond letters are pp=σ, nn=σ⁻¹=σ−h, pn≈σ−h/2. Bond factors at Markov parameter z: tr(σ)=z, tr(σ⁻¹)=z−h. Faithful positive window is z∈[0,h] (#7612 iff + FullTowerTraceWindow T2). So on every faithful trace, σ and σ⁻¹ have traces of opposite sign (or one is 0). A log of a product of crossings of both chiralities cannot be real on a faithful trace. General-z bond formula ∏(z+d_k) checked exactly in H_6 (1 and 2 bonds), not proved.
- **b₃ under any per-bond additive law (A, or C2 = Σ g(f_b)) is exactly 0** (no connected three-body term). It is not specific to A.
- **C1 `1−∏f` is already refuted in the corpus**: it is the linear Δtr law (Δtr/tr_free = 1−∏f), intensive, saturates, 1592× AME spread (binding_canonical.py banner). Do not revive.
- **C2 `Σ g(f_b)`**: defined on the window, extensive, b₃=0; g must be derived (anti-fit).
- **Ordering fact**: d_nn < d_pn < d_pp, so any monotone-decreasing functional of the factor binds nn most, pp least, at every z. The two-nucleon spectrum (only pn binds) cannot come from the functional; it is in the letters (qou-kj4v).
- **Unexplored C3 (speculative, not computed):** per-block determinant `Σ_λ μ_λ log|det ρ_λ(·)|`, multiplicative for any word and defined on faithful traces since σ is invertible. Owner consent needed before any code.
- **Literature:** none found in library/ (INDEX + sections grep) on log-of-Markov-trace binding with signed factors. The nearest precedent for "log of a quantum trace" is the volume conjecture, which takes log|J_N|. Positivity of Markov traces is classical (Wenzl 1988, not held); Orellana arxiv-math-9806163v1 gives the weights.

## 2026-10-10 — stepping stones (story)

The B_log-on-the-faithful-window problem stays OPEN. Stones, in dependency order:

1. `qou-5zl1` general-z bond formula in Lean (in progress, worker on #7612).
2. `qou-oc6i` C3 trace-of-log probe: measured; pp = -nn at every z, both 0 only at z = h/2; pn weakly anti-bound (-0.0054 alpha). The functional inherits the letters' isospin antisymmetry.
3. `qou-v47j` letter provenance (done): pp = sigma, nn = sigma^-1 are assumed (no ruling); delta/4 underived; delta convention-C only.
4. `qou-ulj0` pn letter from a spin x isospin projector (S=1, T=0): the untried door through both proved escapes.
5. `qou-1jg0` selection principle for the functional (log tr / 1 - prod / tr log; b3 trilemma qou-edt7).
6. `qou-wktw` which z in [0, h].
7. `qou-3tz5` rebase #7612 onto #7596.

Reading (judgement): every functional tried so far reproduces the letters' sign pattern, so the letters (stones 3-4) are the upstream place to dig.
