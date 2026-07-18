---
# cmiy
title: 'Integration: canonical watcher - P30 WitnessBuilder rollup'
status: todo
type: task
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-07-03T00:45:00Z
---

## Canonical bean for the P30 WitnessBuilder rollup (dedup 2026-06-28)

`1j39` ("I-infra-no-witnessbuilder-P30 batch port") is the **same work** —
both are the P30 WitnessBuilder rollup (~133 scripts that emit raw witness
JSON instead of routing through `WitnessBuilder`). Treat **this bean
(`cmiy`) as canonical**; `1j39` is its duplicate. (Owner-close `1j39` when
convenient — resolve is human-only.)

## DEFERRED — high collision with the active compute-PR storm

A big-bang witness regen across ~133 scripts conflicts with 8–12 in-flight
compute PRs (e.g. #2993 λ_A-excision, #3009 lever-1 kernel, #2985 z2bn,
#2970 canonical-derivation, #3016 dashboard, #3013/#3007 Cl3Zeta5, #2747
ct80 codata) — a repo-wide regen now would create merge churn across all of
them. Per `/coordinate` (2026-06-28): **defer the big-bang** until the
compute-PR storm settles, then do it in small per-cluster batches (or one
sweep once `main` is quiet). Prior triage also classes much of the rollup as
acceptable Class-B/C/D (`docs/audits/2026-06-25-session-bean-triage.md`).

## 2026-06-30 — re-confirmed DEFERRED (not started)
The ~133-script WitnessBuilder big-bang regen remains a high-collision sweep
to be done in small per-cluster batches once main is quiet — explicitly not a
late-session big-bang. No work taken here. Duplicate 1j39 still open (owner-close).

## 2026-06-30 — batch 1 (1 script) + migration gotchas documented
Routed meson_vol_density.py off raw json.dump onto WitnessBuilder provenance
(PROV_MISSING 280 → 279). Stays OPEN (multi-batch). Surfaced 3 non-mechanical
gotchas that gate a bigger sweep — full recipe in
docs/audits/2026-06-30-cmiy-witnessbuilder-rollup-batch1.md:
  1. wrap_legacy DROPS flat assertions/allPassed (data loss) → use
     stamp_staleness_metadata for assertion-bearing payloads.
  2. regen refreshes stale data (q0 drift) → full regen, not provenance-only;
     pyhecke_native producers need the canonical env (skip in ad-hoc env).
  3. some raw-emit scripts pre-crash (magic_A_formula mpf-format) → separate fix.

## 2026-06-30 — batch 2 (3 scripts, wrap_legacy)
3 pure-Python zero-consumer raw-emit scripts migrated via wrap_legacy (none
carries flat assertions, so wrap_legacy is safe per batch-1 gotcha #1):
rt_route_cross_particle_ratio_quantum_dim, bw_chirality_isotopes,
canonical_lepton_braid_words. Each: exit 0, PROV_OK, original keys preserved.

## 2026-06-30 — batch 3 (2 scripts, wrap_legacy)
delta_lambda_borromean_ascaling, crystal_yekutieli_probes_abcd — pure-Python,
zero content-consumers, no flat assertions. crystal lacked a sys.path entry
for substrate/ (witness_base home); added it inline before the import.
Both: exit 0, PROV_OK, original keys preserved.

## 2026-06-30 — batch 4 (1 script) + easy-tail exhausted note
q_beta_complex_q_test1_phaseA_v2 migrated via wrap_legacy (0 consumers, no
assertions, exit 0, PROV_OK). NOTE: the clean single-output / zero-consumer /
no-assertion / fast tail is now EXHAUSTED — ~1 in 12 triaged this round.
Remaining raw-emit scripts need per-script handling: multi-emit (≥3 witnesses),
flat-assertions (→ stamp), many-consumer (restructure risk), slow/Hecke regen
(canonical-env), or NOFILE (would add a witness, not fix one). Future batches
are the harder tail the bean's deferral anticipated.
## 2026-06-30 — batch 5 (3 scripts, stamp — the assertion-bearing case)
First "harder tail" batch: 3 assertion-bearing substrate/ probes migrated via
stamp_staleness_metadata (NOT wrap_legacy, which drops flat assertions):
lever1_lambda_sw_no_shortcut, lever1_color_eq_monodromy_integrality,
lever1_binding_monodromy_hyperbolicity. Each: exit 0, PROV_OK, assertions
preserved, original keys kept. (lambda_sw also: fixed a fragile cwd-relative
output path → os.path.dirname(__file__).)

## 2026-07-01 — batch 6 (3 scripts, stamp)
3 more assertion-bearing substrate/ probes via stamp_staleness_metadata:
lever1_color_eq_intrinsic_tau_rapidity, zeta4_complex_volume_moderator_probe,
lever1_color_eq_lambda_sw_rapidity. Each: exit 0, PROV_OK, assertions preserved,
keys kept. (zeta4 also: fixed cwd-relative output path → dirname(__file__).)

## 2026-07-02 — batch 7 (3 scripts, stamp)
3 more assertion-bearing substrate/ probes migrated via stamp_staleness_metadata
(preserves flat assertions per gotcha #1): lever1_lw_depth2_recurrence_test,
lever1_qinvolution_kernel_test, lever1_binding_habiro_qexponential. Each:
exit 0, PROV_OK, assertions preserved, original keys kept; all three also fix
the fragile cwd-relative output path → dirname(__file__). PROV_MISSING 276→273
pre-rebase (batch 6 #3198 merged first; post-rebase audit refresh → 270).

## 2026-07-02 — batch 8 (4 scripts, stamp) — substrate stamp-tail EXHAUSTED
The last 4 assertion-bearing substrate/ raw-emit probes migrated via
stamp_staleness_metadata: frakV_descent_zeta4_partner_probe,
frakV_zeta4_fibre_vs_observable_probe, lever1_trB_geometric_target,
lever1_trB_quantum_integer_form. Each: exit 0, PROV_OK, assertions preserved,
original keys kept; the two frakV also fix cwd-relative output paths →
dirname(__file__). PROV_MISSING 270→266. The trB-geometric "consumer" hit is
a docstring mention of an audit doc, not a file read — all 4 are 0-consumer.
Remaining substrate/ raw-emit tail (~14) is all assertion-FREE (wrap_legacy
path) but includes input-witness chains (lever1_binding_core_* read the
cyclotomic witness) — next batch.

## 2026-07-02 — batch 8b (4 scripts, wrap_legacy; non-substrate + wlambda)
Post-substrate-vein: 4 no-assertion single-output probes via wrap_legacy —
meson_gen3_eta_phi, binding_bar_even_odd_probe, rt_w_sqrt2_jet_order_validation,
substrate/wlambda_identity_i_structure_probe. Each: exit 0, PROV_OK, keys kept.
(Confirms the clean vein extends beyond the lever1/zeta4/frakV substrate family.)

## 2026-07-02 — batch 9 (5 scripts, wrap_legacy) + gotcha #5
5 root-computations probes: knot_factor_skein_verification,
metallic_q_symbolic_galois_proofs, sigma_shell_characterization,
six_fifths_categorical_proof_attempt, rt_habiro_borromean_cross_validation.
Each: exit 0, PROV_OK, keys kept. Two needed the substrate/ path insert
(gotcha #4). NEW GOTCHA #5: save()'s drift-protection treats commitSha/
scriptCommitSha/computedAt/durationMs as ephemeral, so a witness missing ONLY
those never gets them added in place ("substantively identical" → preserved).
Fix: delete the stale witness first, then run (save writes fresh).
PROV_MISSING → 258.
## 2026-07-02 — batch 9b (4 scripts, wrap_legacy) — cyclotomic chain cluster
(Numbered 9b: a sibling batch 9 landed on main concurrently — no script overlap.)
lever1_binding_correction_cyclotomic_structure plus its two witness-readers
lever1_binding_core_characterization / lever1_binding_core_root_distribution
(regenerated in dependency order), and standalone
lever1_binding_habiro_single_element_test. All assertion-free → wrap_legacy
safe. Each: exit 0, PROV_OK, original keys kept; `computation` normalized
{script:…} → name-string per the batch-2 precedent (path preserved in
scriptFile). Copilot review fix: chain-readers now record the upstream via
builder.add_upstream → data.upstream_witness_hashes; plus sibling-first path
resolution in witness_dependency_drift.py (substrate upstreams were false
upstream_missing). PROV_MISSING 258→254 post-rebase. Remaining substrate tail
~9 (qaskey, qholonomic ×2, z2bn ×3, + non-substrate).

## 2026-07-03 — Batch 10 SHIPPED (5 more producers via wrap_legacy; PROV_MISSING 254→249)
borromean_binding_recompute, borromean_h3_2_1_irrep_derivation,
canonical_tr_m_three_path_comparison, probes/bowtie_q_channel_projection_probe,
chebyshev_pairing_engine_witness — all plain payloads → wrap_legacy; dropped
manual scriptCommitSha/scriptHash/computedAt/dead "computation" keys + now-dead
git_sha_of/file_hash helpers and subprocess imports. All 5 rerun exit 0;
provenance triple (engine/scriptFile/commitSha) verified on each witness.
NOTE: bring-coordinate-linking-weight-probe.witness.json is an ORPHAN (no
producer script in tree) — needs a disposition pass, not a wrap.

> **Investigated 2026-07-05 (swarm 2, PR #3344) — deferred, kept OPEN.** WitnessBuilder ports need running the producer (regen witness w/ provenance); WitnessBuilder imports mpmath → unimportable in sandbox (compute-blocked). Easy tail drained (batches 1–10); hard tail (qaskey/qholonomic/z2bn) needs canonical env.

## 2026-07-03 — batch 11 (6 scripts, wrap_legacy) — substrate/ raw-emit DRAINED
The last 6 substrate/ raw-emit scripts, all assertion-free, via wrap_legacy:
binding_qaskey_product_probe, lever1_qholonomic_kernel_fit,
lever1_qholonomic_order3_fit, z2bn_pf_monodromy_synthesis,
z2bn_prolongation_qdifference_constraint, z2bn_tau_derivation_probe.
Each: exit 0, PROV_OK, original keys kept (only wrap_legacy-standard meta
added); cwd-relative paths eliminated via save(). Followed sibling gotcha #5
(delete stale witness first). PROV_MISSING 249→243. computations/substrate/
now has ZERO raw json.dump witness emitters — remaining rollup work is the
root-computations tail (~30+ scripts, per-script triage: many-consumer,
multi-emit, canonical-env, NOFILE classes).

## 2026-07-17 — CORRECTION of the 2026-07-05 deferral note (stale)
That note's "hard tail (qaskey/qholonomic/z2bn) needs canonical env" is stale:
#3246 (merged 2026-07-03) drained exactly those — substrate/ has zero raw
emitters since. The remaining tail is the ROOT-computations set, and most of
it is pure-Python (no canonical env needed) — do not skip on that note.

## 2026-07-17 — reevaluation + batch 12 (6 scripts) — root Δλ probe family
REEVALUATION FINDINGS (post-week):
1. PROV_MISSING regressed 243→268 while the corpus grew 1545→1868 — new probe
   families (deltalambda/, qbeta/, probes/) land raw faster than batches drain.
   RECOMMENDATION (needs owner sign-off): add a preflight/CI guard flagging raw
   json.dump-to-*.witness.json in changed compute scripts (check-sidecars.sh is
   the natural home) — without stopping the inflow the drain cannot converge.
2. deltalambda/ subdir probes are ALREADY PROV_OK (hand-rolled provenance
   satisfies the audit) — do not "migrate" them for the count.
3. Worklist recipe: map by_verdict.PROV_MISSING stems → unique live producer via
   grep over non-deprecated raw-emit scripts; currently 132 one-producer pairs.

BATCH 12 (root delta_lambda_* family, all 0-consumer, no native deps):
stamp (assertion-bearing): dim_weight_proof, multi_atom_crosscheck,
qlommel_recurrence_precheck, sign_rule_proof; wrap_legacy (+_T0 durationMs
anchor per #3246 lesson): magnitude_deficit_profile, qdim_route_probe. All:
exit 0, prov triple present, keys + assertions preserved. PROV_MISSING 268→262.
Root scripts need the substrate/ sys.path insert (gotcha #4); _T0 must go AFTER
`from __future__` (new micro-gotcha #6). Deferred (1 consumer-hit each):
cancellation_ascaling_probe, l1_ceiling_sign_prune.

## 2026-07-17 — batch 13 (3 scripts) + P30 PREFLIGHT GUARD (the converging fix)
GUARD: scripts/check-sidecars.sh computations/*.py case now flags a changed
producer that writes a *.witness.json via raw json.dump/write_text with NO
WitnessBuilder (⚠, action=1). This is the inflow-stopper the batch-12
reevaluation flagged — new raw emits are now caught at authoring/pre-commit
time instead of drained after the fact. Tested both ways (fires on raw,
silent on migrated).
BATCH 13 (3 root scripts, wrap_legacy + _T0): delta_lambda_cancellation_
ascaling_probe (a REAL upstream — its witness is read by delta_lambda_
borromean_ascaling as _CANON_WITNESS; migration preserves all data keys, only
adds meta, consumer re-run exit 0), delta_lambda_l1_ceiling_sign_prune
(docstring-only "consumers", 0 real), binomial_pattern_chebyshev_derivation.
All: exit 0, keys preserved, real durationMs. PROV_MISSING 262→259.

## 2026-07-17 — batch 14 (2 probes) + GOTCHA #7 (hoefsmit_symbolic canonical-env dep)
NEW GOTCHA #7: many computations/probes/*.py import `hoefsmit_symbolic` (a
substrate/ module) at the TOP of main(), BEFORE any P30 path-insert can run —
so they crash with ModuleNotFoundError in an ad-hoc env and can only be
migrated+verified under the canonical env (substrate on PYTHONPATH from start).
Triaged 6 probes this batch; 4 hit this (bn_minus_bp_brane_tower_parity,
bn_minus_bp_winding_iterate, chi_content_eigenbasis, chi_content_single_mode) →
DEFERRED to a canonical-env batch. Only self-contained mpmath probes migrated:
chirality_topology_binding_probe, binding_triangle_3body_cluster_probe (both
wrap_legacy + _T0; exit 0, keys preserved, prov triple + real durationMs).
PROV_MISSING 260→258. WORKLIST REFINEMENT: filter candidates by
`grep -L hoefsmit_symbolic` too, not just native/consumers, when in ad-hoc env.

## 2026-07-17 — batch 15 (2 scripts) + gotcha #8 (TRANSITIVE native dep)
octonion_su3_stabilizer_probe (wrap_legacy; also fixed a cwd-relative literal
"computations/..." output path) + habiro_borromean_cyclotomic_coefficients
(wrap_legacy + add_upstream(q-pinning-50-digit) — it READS the canonical
substrate pin, so the upstream edge is now machine-checkable; supersedes its
hand-rolled provenance which had left it PROV_MISSING on the stale committed
witness). Both exit 0, keys preserved, real durationMs, upstream verified.
NEW GOTCHA #8: torus_knot_markov_trace_closed_form passed the direct
grep -L native filter but imports markov_trace_for_knot which TRANSITIVELY
imports pyhecke_native → ModuleNotFoundError in sandbox. The worklist native
filter must follow first-level local imports, not just grep the producer body.
Reverted torus → canonical-env batch. PROV_MISSING drift is inflow (new main
landings) not regression; the batch-13 guard now catches new raw emits at
pre-commit.

## 2026-07-17 — batch 15 fail-loud hardening (PR #3862 review) + LATENT BUG fix
Owner chose "harden to fail-loud" on Gemini's habiro upstream comment. Made
q0_value() REQUIRE the canonical pin (raises FileNotFoundError/KeyError instead
of falling back to a hardcoded literal) and add_upstream unconditional. This
SURFACED A LATENT BUG: the pin carries q0 at nested derived_50_digit.q, but the
old lookup only tried FLAT keys (q0/q_0/q/value) → never found it → silently
used a 17-digit literal fallback that happened to match the pin to 17 digits
(so the miss was invisible). Fixed the lookup to read derived_50_digit.q →
the script now consumes the FULL 50-digit canonical q0. Data change: witness
cyclotomic_coefficients_at_q0 + q0_used gain precision (17→50 digits); upstream
edge is now genuine. GENERAL LESSON: fail-loud provenance is not just hygiene —
it caught a script that had been silently ignoring its canonical input.

## 2026-07-18 — batch 16 (6 scripts, wrap_legacy + _T0 + explicit output_dir)
6 clean zero-consumer scripts (2 root, 4 probes/), all mpmath, assertion-free:
keystone_wlambda_defect_dn_subleading, t6_lepton_h3_3channel_convention,
probes/{flavor_split_3strand_derivation,flavor_split_partial_derivation,
interface_factor_enhancing_check,zhabiro_phiq}. Heterogeneous emit dirs — used
explicit output_dir on wrap_legacy so each witness lands where the old code
wrote (probes/ writers that targeted the parent computations/ dir → output_dir
= HERE.parent/COMP). keystone also fixed a cwd-relative "computations/..." path.
All: exit 0, keys preserved, prov triple, real durationMs, correct location, no
strays. Avoided deuteron_* candidates (active #3808-lineage sibling scope).
PROV_MISSING 261→256. Worklist: 49 clean PROV_MISSING+zero-consumer picks
remained pre-batch (minus the deuteron set + slow z_habiro_increment which
times out in-sandbox).

## 2026-07-18 — batch 17 (3 scripts, wrap_legacy + explicit output_dir)
3 clean single-emit zero-consumer root scripts: dilog_archimedean_partA_witness
(mpmath), f_ell_derivation_via_per_braid_mass_tower (mpmath),
figure_eight_aj_operator (sympy). All wrap_legacy + _T0 anchor + substrate
sys.path insert; each passes explicit output_dir to land the witness where the
old code wrote it. Exit 0, computed values bit-identical, prov triple + real
durationMs. NOTE (gotcha #2 benign instance): f_ell's committed witness
re-serialized one CODATA input (206.768283) with mpmath trailing digits
(...2999...) — SAME number, all computed physics values identical; cosmetic
only. PROV_MISSING 256→253. Avoided deuteron_* (sibling #3808 scope).

## 2026-07-18 — batch 18 (2 scripts) — the input-witness-chain tail
Two single-output producers that READ input witnesses (the harder tail):
- probes/binding_cluster_operator_vs_mayer_probe (wrap_legacy + add_upstream):
  reads three-body-joint-trace-a3 as input → genuine data.upstream_witness_hashes
  edge recorded (the #3862 lesson applied). engine mpmath, output_dir=COMP.
- deltalambda/perknot_pn_bond_mayer_grounding_probe (stamp, assertions): the
  "extensivity-gap-synthesis" name in it is docstring-only, not a file read →
  clean single output. NOTE: stamp path has no start_time param, so NO _T0
  anchor (durationMs not tracked by stamp) — gotcha #9: don't add _T0 to
  stamp-path scripts (unused var).
Both: exit 0, keys/assertions preserved, prov triple. PROV_MISSING 255→253.
Sandbox-clean tail now ~single digits; remainder is native/multi-emit/deuteron.

## 2026-07-18 — batch 19 (3 scripts, stamp) — wlambda_* deltalambda cluster
3 assertion-bearing deltalambda/wlambda_* probes via stamp_staleness_metadata:
wlambda_jet_tower_connected_probe, wlambda_level_selection_kA_probe,
wlambda_wstd_growth_bound_probe. All exit 0 (needed `pip install numpy` —
hecke_characters imports it; ordinary sandbox dep, NOT a native blocker),
keys+assertions preserved, all 3 confirmed PROV_OK in the audit. jet_tower's
output is read by deltalambda_extensivity_gap_synthesis_probe — migration is
data-preserving (meta-only add), consumer re-run exit 0. Skipped
wlambda_transfer_matrix_connected (dep=3, native) + wlambda_nuclear_braid
(reads q-pinning, needs stamp+manual upstream — defer). NOTE: absolute
PROV_MISSING count is noisy (corpus grew 1868→1947 from concurrent main
landings); per-witness PROV_OK confirmation is the reliable check, not the
aggregate. gotcha #10: hecke_characters needs numpy in-sandbox.
