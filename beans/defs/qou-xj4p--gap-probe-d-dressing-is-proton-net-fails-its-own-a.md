---
# qou-xj4p
title: 'GAP: probe_d_dressing_is_proton_net fails its own assertion after refresh'
status: completed
type: task
priority: normal
created_at: 2026-11-24T20:49:37Z
updated_at: 2026-11-25T16:22:14Z
---

Found by the 2026-11-24 paper-compute refresh (PR #9395, branch `claude/compute-refresh-2026-11-24`, main `dd5f163edbd`). `computations/probes/probe-d-dressing-is-proton-net.witness.json` was self-stale. Re-running the current producer `computations/probes/probe_d_dressing_is_proton_net.py` (exit 0) writes `allPassed: false`. The refreshed witness was **NOT committed** (owner decision 2026-11-24, "D2 commit all 42": hold producers that fail their own assertion). Main still carries the old passing witness.

Before (committed) → after (fresh run):

- assertion 1 `binding_candidate_subpercent` (`B_D = E₀·net(p)·Δtr` vs AME2020): **True → False**
- `data/numerical/B_cand_E0_netp_dtr_MeV`: `2.23094304357897479` → `0.55119272426415506`
- `data/numerical/B_cand_err_vs_AME_pct`: `0.28665559959396997` → `-75.22246250688538`
- `data/numerical/Delta_tr`: `0.59516889262234348652` → `0.14704667798040846911` (factor ~4.05)
- `data/numerical/B_via_kashiwara_qbeta_MeV`: `2.2272095331670547` → `0.550601110315296747`
- `data/numerical/Qbeta_kashiwara_MeV`: `0.782334386518171885` → `0.782804713582601608`

The deuteron candidate falls from a 0.29 % hit to a 75 % miss. The driver is `Delta_tr`, which shrank by about 4x, so an upstream trace or word changed. Which one is not established here. Under the anti-fit rule the earlier 0.29 % should not be treated as evidence that the old input was right.

Log: `/tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/logs/probe_d_dressing_is_proton_net.py.log`. It is in session scratchpad and may not survive; re-run with `PYTHONPATH=computations:tools/qou-substrate/python:tools/pyhecke/python python3 -u computations/probes/probe_d_dressing_is_proton_net.py`.

Next honest step: trace where `Delta_tr` comes from and which upstream change moved it, then decide whether the probe's conclusion is withdrawn or its input is wrong.

## 2026-11-24 root cause (agent, session 01Eucf, claimed)
Delta_tr = tr_free - tr_atom from tr_m_atom_zn(1,1). Live (borromean word) gives 0.147046678; with atom_braid_word_3A(intra_order='grouped') it gives 0.556544660, against the old witness value 0.5952. About 93% of the move is the 2026-09-05 word ruling (7db032fb482, qou-hu1f); the remaining ~7% is unattributed (the old witness, 2026-07-04, predates the convention-D cascade). The input is correct per the corpus, so the 0.29% deuteron hit was a property of the superseded word: an honest negative, and the probe's conclusion should be withdrawn.


## 2026-11-25 attribution COMPLETE (agent, session 01Eucf, branch claude/xj4p-delta-tr-attribution-20261125)
Reproduced the old Delta_tr 0.59516889262234348652 exactly in a worktree at 581c176f480 (the witness's rewritten commitSha 4dfe838c398). E0 and net(p) did not move (B/(net_p*Dtr) = 4.18598136329447589 in both witnesses). Path old -> live, each step measured, mpmath 70 dps:
- (c) float64-built interface d -> 70-digit: -1.35e-20.
- (b) y_lambda pin retired muon -> proton: -1.415e-9. The old run read y_lambda from the muon-built y-lambda-at-q0 cache through the trivially satisfied |q - Q| < 1e-12 gate: a layer straddle (y at muon, chi at proton). CODATA-2018 and CODATA-2022 muon pins also move Dtr only in the 10th digit.
- (a) Markov convention C -> D (2026-08-09): -0.0386242308025191344 (8.62% of the total move; 4.80% in log terms). THIS is the previously unattributed ~7%.
- word ruling grouped -> alternating (2026-09-05): -0.409497982424029743 (91.38%; 95.20% log).
Not additive: in the other order, the word step under C is -0.49643 and C->D on the alternating word is +0.04830 (opposite sign). Shares are path-dependent.
B_cand vs AME by configuration: C+grouped +0.287% (old); D+grouped -6.22%; C+alternating -83.36%; D+alternating (canonical) -75.22%. The sub-percent hit holds only on the superseded word under the excised convention.
Script + RESULTS: computations/probes/probe_d_dressing_is_proton_net/attribution/. Next step is an owner decision: withdraw the probe's conclusion, or re-scope it. Kept in-progress until then.


PR #9416 (draft): https://github.com/litlfred/qou/pull/9416. Owner decision options: (1) WITHDRAW the probe's conclusion (mark the probe as a recorded negative, assertion stays false, refresh the witness). Cost: one witness refresh plus a note in the audit doc docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md. Risk: none numeric, since nothing is wired. (2) RE-SCOPE: keep the exact ℚ(q) identities (Δ(net) = −h·net(p), Q_β = E₀·h·net(p)) as the probe's content, and drop only binding_candidate_subpercent. That would change the assertion, which needs the owner. (3) Default/no-op: main keeps the stale passing witness, which still claims a 0.29% hit produced by excised inputs. Recommendation (judgement): 1 plus 2, i.e. keep the identities and record the binding match as a negative.


## 2026-11-25T10:49:08Z — DONE. Owner ruling '1+2 together' (2026-11-25) implemented in PR #9417 (merged)
Attribution merged in #9416: the unattributed ~7% is the Markov convention C -> D change (exact, path-dependent split). Probe: binding_candidate_subpercent assertion removed, binding recorded as NEGATIVE (-75.22% on the ruled inputs), exact Q(q) identities kept, witness refreshed, audit doc updated.


## 2026-11-25 — source of the -75% (measured, no fit)

The candidate is B = E0·net(p)·(tr_free − tr_atom), a RAW trace difference. The pipeline's own
leading-order form (binding_single_pipeline_comparison.py:215) divides by tr_free:
s = 1 − tr_atom/tr_free. The two agree only when tr_free ≈ 1.

- Old inputs (conv C, grouped word): tr_free = 0.9835, so the raw Δtr 0.5952 ≈ s 0.6051. Result 2.2309 MeV, +0.29 %.
- Current inputs (conv D, alternating word): tr_free = 0.2990, tr_atom = 0.1520. Raw Δtr 0.1470, but s = 0.4918 (1/tr_free = 3.344). Result 0.5512 MeV, −75.2 %.

Same E0 (4.18598 MeV) and the same Δtr as binding-single-pipeline-comparison.witness.json, so traces agree across producers.
On current inputs: E0·net(p)·s = 1.8434 (−17.1 %), E0·s = 2.0585 (−7.5 %), E0·ln(tf/ta) = 2.8332 (+27.4 %).
So ~3.3× of the miss is the missing tr_free normalisation; the old 0.29 % depended on tr_free happening to be ≈ 1.
Choosing among these by residual would be selection against the target; not done. Decision for owner.


2026-11-25 follow-up: the three normalised forms analysed. The corpus already derives the log form (docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md §10a: Markov multiplicativity + extensivity => Cauchy => c·ln). Lean: logForm_extensive, linearForm_not_extensive, interface_scalar (QOU/Nuclear/InterfaceScalar.lean), InteriorMarkov from BraidedTower (sorry-free). Not formalised: the uniqueness half (continuous additive f on (R>0,x) is c·ln). Under D the deuteron log form is zero-parameter +27.4% (C-era was +74.85%). Under D, z_D > mu_req = exp(-B_AME/E0) = 0.5878, so the C-era mu_unreachable obstruction no longer applies (reported, not a proposal to pick d).


2026-11-25 owner: '1y, 2y, 3y sibling'. (1) #9421: probe-d + probe-d-cross-a report E0*log law (D +27.36 %), stale subpercent assertion in cross-a removed (July C-era witness), prop:deuteron-binding-dressing-proton-net prose updated, skill Antipattern 7, owner-rulings row. (2) #9423: QOU.Nuclear.LogFormUniqueness, sorry-free, standard axioms. (3) interactive child session_01EucfRqaU3YESdx7nHnDgpD on the +27.4 % (E0 scale vs p-n interface weight). Keep open: the deuteron overshoot is unexplained.


2026-11-25 SOURCE OF THE +27.4 %: the input, not the law. (1) Scope correction: mu_pn = z_D + d_pn comes from the single-crossing interface letter that the 2026-11-15 owner ruling (gamma-gamma covers bond letters) supersedes, so +27.36 % is a record, not a prediction (corrected in #9421, ff62e233cf8). (2) Pre-registered probe computations/probes/gg_deuteron_bond (prereg a06ae62c2b2): 6 strands, nucleons V^3/V^6, bonds V(s)^k. Only V^3 at either junction passes reading 3, with ratio 0.9985, giving B = 0.0063 MeV, -99.7 % vs AME. V and V^2 bonds would give 5.2-6.0 MeV but fail reading 3. So on the ruled bond the deuteron is essentially unbound in this cell; the +27 % came from the non-gg letter. p = n in this cell (flavour-blind). Open.


2026-11-25T16:2xZ: owner 'go' on card 1 (A). Selected deuteron in the gamma-gamma cell: V^3 x V^3, bond V(2)^3, B = 0.0063 MeV (-99.7 %) (#9426, 963c58bc0b4). Deep error-budget analysis launched as interactive child session_01EucfRntKGFoPCof8huHo3z. Siblings Phase B / intervals / E0 had stopped on the 5-hour usage limit at ~11:50Z; resumed.
