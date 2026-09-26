---
# cmiy
title: 'Integration: canonical watcher - P30 WitnessBuilder rollup'
status: todo
type: task
priority: normal
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-09-03T20:28:32Z
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

## 2026-07-18 — batch 20 (6 scripts, stamp) — deltalambda sign/grho/nuclear cluster
6 assertion-bearing deltalambda/ probes via stamp (identical _HERE+json.dump
emit; each already carried a manual _sha()/now provenance the audit didn't
recognize — stamp adds the canonical engine/scriptFile/commitSha):
deltalambda_grho_jet_order_derivation_probe, deltalambda_magnitude_graded_trace_probe,
deltalambda_sign_cyclotomic_locus_probe, deltalambda_sign_operator_narrowing_probe,
deltalambda_sign_pivotal_grading_capstone_probe, nuclear_quotient_jones_torus_link_probe.
All 6: exit 0, keys+assertions preserved, confirmed PROV_OK. The cross-family
witness-name duplicates in grep are docstring cross-refs (reads=0), not file
reads. Largest single batch since the substrate drain.

## 2026-07-18 — batch 21 (3 scripts, mixed) — three distinct emit patterns
Low-collision picks (avoided qbeta/keystone/meson sibling-hot areas):
- deltalambda/alpha_cluster_volume_additivity_probe (stamp, pathlib _HERE, var=wit)
- markov_trace_weights_wenzl (wrap_legacy + _T0, here-based)
- he4_9_3_interface_operator_probe (wrap_legacy + _T0; FIXED a hardcoded
  cwd-relative "computations/probes/..." path → output_dir=Path(__file__).parent/"probes";
  the script lives in computations/ but writes to probes/).
All exit 0, correct output location (verified no strays), keys preserved,
confirmed PROV_OK. Remaining clean tail is now mostly sibling-hot (qbeta G3,
keystone s5-so3, meson λ_A) or native/SDP — good stopping point.

## 2026-07-18 — batch 22 (5 deltalambda probes, all stamp)
Cleared the remaining clean (non-native) deltalambda tail:
- wlambda_nuclear_braid_connected_probe (stamp, os _HERE, var=witness)
- wlambda_transfer_matrix_connected_probe (stamp, os _HERE, var=witness)
- deuteron_coupling_s00_probe (stamp, pathlib, var=wit)
- deuteron_wall_alien_resummation_probe (stamp, pathlib, var=wit)
- deuteron_wall_full_transseries_probe (stamp, pathlib, var=wit)
All assertion-bearing (allPassed preserved), engine=mpmath. Exit 0, keys
preserved, PROV_OK. Native deltalambda producers (he4_vol4_prediction_test,
vol4_4he_snappy_falsification) deferred — need pyhecke-native harness.

## 2026-07-18 — batch 23 (2 snappy deltalambda + 5 probes/ cluster)
23a: he4_vol4_prediction_test + vol4_4he_snappy_falsification (stamp; snappy 3.3.2
     pip-installed in-env to run them). deltalambda/ now fully PROV_OK.
23b: probes/ brane-tower+eigenbasis cluster via stamp (out var, writes to ../ =
     computations/): bn_minus_bp_brane_tower_parity, bn_minus_bp_winding_iterate,
     chi_content_eigenbasis, chi_content_single_mode, eigenbasis_structural_lemmas.
     GOTCHA: these import hoefsmit_symbolic from computations/ but live in probes/,
     so must run as `PYTHONPATH=. python3 probes/x.py` (script-dir-only sys.path
     misses computations/). Also: `echo exit=$(...)` clobbers $? via the $()
     substitution — the PROV_OK re-audit is the real gate, not the echo. All 5
     confirmed PROV_OK, keys preserved, no strays.

## 2026-07-18 — batch 24 (meson/kaon sector, 4 scripts via stamp) + 1 orphan cleanup
- meson_mass_from_hecke, meson_per_knot_density (ROOT, HERE=computations)
- probes/kaon_pion_ratio_7_8_probe (HERE=probes → writes to probes/)
- probes/meson_lepton_knot_dictionary_probe
All stamp (var=witness, default=str preserved). Run with PYTHONPATH=. for probes.
CLEANUP: deleted orphan root copy computations/meson-lepton-knot-dictionary-probe.witness.json
— stale duplicate, no producer (script writes to probes/ via Path(__file__).parent),
no consumer; it was a permanent PROV_MISSING nothing could refresh. All 4 PROV_OK.

## 2026-07-18 — batch 25 (interface + alpha, 2 scripts via stamp)
- probes/interface_4body_assembly_probe (COMP-based, indent4, var=witness, mpmath)
- alpha/alpha_k_jones_markov_h3 (module-level, var=out, mpmath)
alpha needed pyhecke (Layer 2b) — pip install -e tools/pyhecke/ (0.1.1) in-env.
This unblocks the remaining pyhecke-dependent tail (keystone_*, probe_q_beta_wenzl).
Both PROV_OK, keys preserved.

## 2026-07-18 — batch 26 (3 keystone_wlambda_* via stamp + 2 path fixes)
- keystone_wlambda_defect_cn_closedform_crosscheck (var=out, mpmath) — FIXED fragile
  CWD-relative "computations/..." hardcoded path -> __file__-relative
- keystone_wlambda_defect_coeff_ladder (var=out, mpmath) — same path fix
- keystone_wlambda_ladder_higher_rungs (var=witness, already __file__-relative)
All exit 0, keys preserved, PROV_OK, no nested computations/computations/ stray.
Coordinated-with: keystone epic 08a2 (mechanical witness wiring only, no math touched).

## 2026-07-18 — batch 27 (deltalambda-probes pair via stamp)
- probes/h6_deuteron_free_word_chi_lambda_probe (var=out, here/.. → computations/)
  — needed qou_substrate (Layer 2a); pip install -e tools/qou-substrate/ (0.1.2)
- probes/delta_lambda_m_pi_constraint_probe (var=witness, HERE=probes)
Both PROV_OK, keys preserved. Env now has snappy + pyhecke + qou_substrate installed,
which covers the runtime deps for the remaining qbeta tail.

## 2026-07-18 — batch 28 (qbeta cluster + SDP, 5 via stamp; +1 path fix, +1 SKIP)
Coordinated: posted intent on sibling #3927 (c4even qbeta ladder) before touching.
- probes/qbeta_habiro_phi8_interpretation_probe (var=out, dumps to_jsonable(out);
  PRESERVED script's own durationMs across the stamp)
- probes/qbeta_modular_resurgence_stokes_probe (var=witness, root-based; script
  returns 1 on 3/4 assertions but WRITES the witness first — exit!=0 is a verdict)
- probes/qbeta_root_of_unity_probe (var=out)
- probe_q_beta_wenzl_projectors (var=witness) — FIXED hardcoded CWD path -> HERE-relative
- joint_tower_sdp_solver_v2 (var=witness, base-based) [cons=11 but emit-metadata only]
All 5 PROV_OK, keys preserved, no strays.
SKIPPED qbeta/qbeta_reeb_tower_jacobi_anger_physical_weight: it has NO file-write
(only print(json.dumps(out))); its committed witness was captured manually. Wiring
it means ADDING a writer = behavior change, not mechanical stamping. Needs a
separate, coordinated change (flagged to leave for the qbeta owner). This is the
last cmiy single-write-clean producer; remaining PROV_MISSING are multi-write /
read+write / native-only / no-writer scripts needing bespoke handling.

## 2026-07-18 — batch 30 (auto-stamper — chunk 1: 8 producers)
Built a verified auto-stamper (scratchpad/autostamp.py): locates the single
write site, inserts a depth-independent stamp block (walks up to find substrate/),
re-runs the producer, and KEEPS the edit only if the audit flips the witness to
PROV_OK with keys preserved — else auto-reverts. Chunk 1: 10 attempted, 8 OK,
2 safely auto-reverted (brane_tower_isospin_diagnosis: exit1; d_u_closed_form_proof:
writes a shared witness → not-prov-ok). 8 wired: binding_bring_enhancement_compare,
figure_eight_kashaev_volume, d14_theta_bar_side, deuteron_fpn_wlambda_wiring,
ew_couplings_substrate_derivation, geom_leading_alt_q_locality, h4_h2_cross_algebra_bridge,
h3_markov_trace_cyclicity_preflight. 76 clean single-write mapped total.

## 2026-07-18 — batch 31 (auto-stamper chunk 2: 19 producers, 6 auto-reverted)
19 wired incl. the 5 alpha_em/ probes, alpha_k_jones_markov_h4, habiro_coefficients_interpolate,
he-nu-sdp psd-count, he3 brane-tower/charge-asymmetry, hecke_channel_binding, higgs (2),
m_tau_knot, markov_weights_symbolic, metallic_q_wenzl_sign_sweep, murakami_deformed_vc_q0,
binding_alpha_shift, alphaem_dilog_bloch. 6 auto-reverted (shared-witness / input-needing
scripts). 68 clean remained at chunk start.

## 2026-07-18 — batch 32 (auto-stamper chunk 3: 23 producers, 2 reverted)
Heavy qbeta/qbessel cluster (coordinated on #3927): 8 qbessel_* + 10 qbeta_* incl.
qbeta_reeb_tower_jacobi_anger (the one WITH a writer, distinct from the physical_weight
one skipped in batch 28), plus habiro_coefficients_extended, metallic_q_jones_sign_sweep,
3 pentagon/per-knot h4 probes, poly_q_proof, pyhecke_h3_vs_h3a. 2 reverted
(pentagon_rt_torus_knot_higgs, per_knot_density_borromean_q_locality — exit 1).

## 2026-07-18 — batch 33 (auto-stamper chunk 4: 17 producers) — CLEAN SINGLE-WRITE SET EXHAUSTED
17 wired (rt_*/t3n/t6_*/vol_density_*/su4/qm_channel/xi_ell/vhat/metallic_q_quark/
yekutieli/qbeta_silver_rationals/six_fifths/z_habiro). 4 reverted (brane_tower_full_channel,
two/three-quark sweeps — exit1/shared). Clean single-write set now fully drained:
67 wired via stamper across chunks 1-4. NEXT: read+write class (~55).

## 2026-07-18 — batch 34 (auto-stamper chunk 5: read+write class, 16 producers, 9 reverted)
First read+write chunk (reads inputs, writes 1 output; stamper targets the output write).
16 wired (adjacent_vs_full, delta_lambda_h6_branching, e0_lambda_composite,
habiro_coefficients_atomic, inter_cluster_bond_term, mirror_pair_coulomb, mu_p_pin_sensitivity,
multi_layer_gap, option_e_kl_betti/h6_entry, qbessel_reeb_order, qbeta c8-c10/closed-form-wiring/
qbessel_contiguity, rho_k_h3a_refinement, alpha_blend_tower). 9 reverted — mostly option_e_v5-v9
+ deuteron_real_sdp + mass_formula_6term (exit 1, need absent inputs).

## 2026-07-18 — batch 35 (read+write class drained to runnable limit: 2 more)
2 wired (alpha_activation_brunnian, rho_k_h3a_crystal). Remaining 9 read+write are the
persistent non-runnable residue (option_e_v5-v9, option_e_probe1, probe_isospin_mirror_v9,
deuteron_real_sdp, mass_formula_6term) — all exit 1 (need absent input witnesses/deps),
auto-reverted. read+write runnable class DONE: 18 wired across chunks 5-6.
NEXT: the 69 unmapped (computed-name / f-string producers).

## 2026-07-18 — batch 36 + SESSION-BOUNDARY RESIDUE MAP
+1 wired: deuteron_tr_M_symbolic. This session (batches 20-36) drained the entire
mechanically-safe, sandbox-runnable portion: ~86 producers hand+auto-stamped,
PROV_MISSING 232 -> 164. The verified auto-stamper (scratchpad/autostamp.py) is the
reusable tool: insert stamp at single write site, re-run, keep iff PROV_OK+keys, else revert.

REMAINING 164 — genuinely blocked, NOT mechanical:
- 67 no-py-producer: .sage scripts (bring_jacobian_isogeny, lever1_bring_period — need
  Sage), fully-computed f-string names (need loop-aware bespoke stamping), and orphans
  (some deletable like the meson-lepton orphan cleaned in batch 24).
- 53 single-write-nonrunnable: exit!=0 in a clean checkout — need input witnesses/deps
  regenerated FIRST (dependency ordering); e.g. option_e_v5-v9, deuteron_real_sdp.
- 27 wired-but-reads-missing-input: producer ALREADY wired; clears automatically once
  its upstream input witness is fixed (pure dependency ordering — no code change needed).
- 16 native: chi-*/nucleus-sdp rust + snappy — need pyhecke-native wheel built; the
  canonical chi-*/nucleus muon-q0 set also overlaps the tnjb owner-gate.
- 1 multi-write.

TO CLOSE cmiy fully: (a) build pyhecke-native wheel for the 16 native; (b) run producers
in dependency order so the 53+27 input-dependent ones see fresh inputs; (c) loop-aware
stamper for multi-output computed-name producers; (d) owner call on the canonical
muon-q0 chi/nucleus set (tnjb). None are blind-stampable.

## 2026-07-18 — batch 37 (native unblock: built pyhecke-native wheel)
Built pyhecke-native 0.9.0 (cargo 1.94 + maturin build --release, ~3min) and pip-installed
the wheel — unlocks the native producer class. Ran stamper over native single-write set:
5 wired (he4_binding_k_presentation_correction, torus_knot_markov_trace_closed_form,
ame_registry_routing_triage, kl_betti_cell_dependence, items_1_2_3_mw_strongforce_anchor_asymmetry).
1 (he4_binding_k_stage2) timed out at 400s stamper limit — reverted cleanly (needs longer run).
NOTE: stamper EXC path does NOT auto-revert (only the PROV-fail path does) — manually reverted.
Remaining native are computed-name (chi-*/nucleus-sdp) multi-output — need loop-aware stamping
+ tnjb owner-gate. PROV_MISSING 164 -> 160.

## 2026-07-18 — batch 38 (IN-PLACE stamp: 59 unambiguous-producer witnesses, VALUE-PRESERVING)
Per owner "1 2": stamp-in-place (no re-run) + hard value-verification. Built inplace_stamp.py:
adds ONLY provenance fields to the committed witness JSON, refuses if any non-provenance
key/value would change. Pre-validated 59 witnesses with EXACTLY ONE literal writer (correct
scriptFile, not a consumer — the mis-attribution trap that made me revert the first attempt:
rho_w_crystal_vertex_trace READS chi-deuteron, doesn't produce it). Fixes across 3 iterations:
ensure_ascii=False (preserve unicode bytes), preserve trailing newline, preserve existing
engine/engineVersion (was clobbering numpy+scipy->python). Final: 59 OK, 0 value-integrity
violations (every non-provenance key byte-identical vs HEAD). Includes nonrunnable scripts
(he_nu_sdp_*, option_e sweeps) since in-place needs no run. PROV_MISSING 159 -> 100.
Remaining 100 = computed-name/orphan (canonical chi-*-at-q0 set: f-string producers, no
unambiguous literal writer) — still need the chi-pipeline producer map or owner input.

## 2026-07-18 — SESSION CLOSE (232 -> 101 PROV_MISSING; batches 20-38, 19 PRs merged)
Remaining 101 = the canonical chi-*-at-q0 / nucleus-sdp set. Attribution wall CONFIRMED:
these producers write via `_pb.witness_path(<computed name>, HERE).write_text(...)` — the
witness name is built (f-string / name_map) and passed through the witness_path() helper,
so it never sits adjacent to the write call. Neither literal-writer nor f-string-template
matching resolves a UNIQUE producer (0/101 auto-resolved). Reliable scriptFile attribution
now requires per-script reading of each producer's naming logic — bespoke, and error-prone
on the GATED canonical set (mis-attribution writes false provenance; already reverted once
when rho_w_crystal_vertex_trace, a READER, was picked as the chi-deuteron producer).

TOOLS LEFT FOR NEXT PASS (all in scratchpad, reusable):
- autostamp.py: re-run + audit-gated stamp (for runnable single/read-write producers)
- inplace_stamp.py: value-preserving metadata-only stamp (0 value violations guarantee);
  feed it a hand-built {witness: correct_producer.py} map for the chi/nucleus set.
NEXT STEP to finish cmiy: build the chi/nucleus producer map by reading the ~6 pipeline
scripts (chi_*_lossless, chi_at_q0_via_matrix_m_mpfr, nucleus_real_sdp, ...) to see which
computed name each emits, then run inplace_stamp.py with that map. Owner input optional
since in-place is value-preserving, but the map itself is the gated/bespoke work.

## 2026-07-18 — batch 39 (verified chi/nucleus producers: 7 more in-place)
Read the pipeline scripts to attribute producers CORRECTLY (not regex-guess): verified
chi_4he_via_rust_lossless.py hardcodes atom="helium-4" (so it produces ONLY
chi-helium-4-h12-matrix-m — the regex over-match to deuteron/lithium/etc was a trap I
caught), and nucleus_real_sdp.py loops its 6-atom ATOMS dict writing nucleus-real-sdp-<atom>.
Stamped those 7 in-place, 0 value violations, all PROV_OK. PROV_MISSING 101 -> 94.
The remaining ~94 each need this same per-producer read (atom/name scope) to attribute
safely — genuine per-script work, not a bulk sweep; the hardcoded-atom trap proves regex
attribution is unsafe on the canonical set.

## 2026-07-19 — CLOSED. Load-bearing PROV_MISSING 232 -> 0 (ratio 1.000).
Final floor of 3 documented + audit-exempted (PROV_EXEMPT_ACKNOWLEDGED, reasons in
computations/audits/provenance-acknowledged-floor.json), so they are on the record
and NEVER re-chased:
- canonical-mass-table-242ppb: hand-authored by design (self-documents "no producer
  script was run"); auto-resolves when a Delta_lambda-backed producer regenerates it.
- wenzl-y-lambda-h9 / h12: legacy y_λ caches at an old muon pin (1.109978595554,
  differs at digit 12); producer removed; still read by nucleus_real_sdp.py. Resolve
  only via an owner-gated regenerate at the live q0.
Session arc: mechanical batches + auto-stamper + native wheel + in-place stamper +
per-producer map + rust-producer archaeology; q0 parameterized (q0Anchor/q0Value on
every witness), backfilled on 573, flip-detector CI-gated. Discussion CLOSED — do not
revisit the floor of 3; each has a documented reason + resolution path.


## 2026-09-03 — RE-MEASURED: the port is **23 producers, not ~133**, and the duplicate's worked example is already done

Fresh measurement against `main` `95d9b62368`. **Quote these with the command, not the old figures.**

**Command:** parse `computations/audits/witness-provenance-audit.witness.json`
for entries with a non-empty `missing_fields`, resolve each witness to its
producer (via the witness's own `scriptFile`, else a name heuristic), and
classify the producer as WitnessBuilder-routed iff it both mentions
`WitnessBuilder` and calls one of `.build(` / `.save(` / `stamp_staleness_metadata`.

```
TOTAL witnesses with missing provenance      347

by missing-field pattern
  250  commitSha, engine, scriptFile
   49  commitSha
   28  scriptFile
   18  commitSha, scriptFile
    1  engine
    1  HAND-AUTHORED by design (its own provenance field says no producer was run)

by producer route — the discriminator qou-1j39 names
  255  producer USES WitnessBuilder  -> STALE; a re-run stamps it
   23  producer is HAND-ROLLED       -> re-running NEVER stamps it
   69  producer not located          -> MY RESOLVER'S LIMIT, not a finding
```

**This contradicts the framing the duplicate bean `qou-1j39` carries.** It
presents the hand-rolled class as the scope and cites "~133 scripts". Measured,
the hand-rolled class is **23 (7 %)**; **255 (73 %)** are ordinary staleness that
self-heals on the next producer run, needing no port at all.

**Honest bound:** 23 is a **lower** bound. The 69 unlocated are witnesses that
exist on disk (only **1** audit-named witness is missing from disk) but whose
producer my name heuristic could not find — some of those may be hand-rolled too.
Classifier spot-checked against source on 3 of the 23
(`milnor_a4_deficit_h_form`, `aggregator_convexity_divided_difference_probe`,
`qcollatz_cycle_census`): all three genuinely hand-roll `json.dump`/`json.dumps`
with no `WitnessBuilder` anywhere.

**`qou-1j39`'s worked example is stale and should not be re-done.** It names four
producers as the measured instance of the never-stamps class. All four now carry
`WitnessBuilder`, and all four witnesses are **stamped** (`scriptHash`,
`commitSha`, `engine`, `q0Anchor` all present):
`birkhoff-barodd-pythagoras-bridge`, `deuteron-interface-handle-curvature`,
`yekutieli-trefoil-surface2form-discretization`, `a3-branching-asymmetry-vs-required`.

**The 23:**

```
computations/deltalambda/milnor_a4_deficit_h_form.py
computations/deltalambda/milnor_a5_a6_recursion_test.py
computations/deltalambda/milnor_recursion_capcup_weight_probe.py
computations/deltalambda/milnor_recursion_forall_A_proof_probe.py
computations/deltalambda/milnor_recursion_forall_A_reduction_probe.py
computations/deltalambda/milnor_recursion_tl_derivation_probe.py
computations/doorv_barparity_guardrail.py
computations/hh1_h5_dim.py
computations/probes/aggregator_convexity_divided_difference_probe.py
computations/probes/aggregator_family_exclusion_probe.py
computations/probes/aomega_m2_bps_cohomology.py
computations/probes/b3_charge_decomposition_a3_probe.py
computations/probes/pair_locality_shortfall_probe.py
computations/qcollatz_backward_tree_structure_probe.py
computations/qcollatz_block_structure_probe.py
computations/qcollatz_cycle_census.py
computations/qcollatz_divergence_probe.py
computations/qcollatz_height_criterion_coverage.py
computations/qcollatz_vtwo_domain_stable_probe.py
computations/qcollatz_vzero_block_probe.py
computations/qou_mass_canonical_wiring_example.py
computations/sigma_f_electron_shell_chain.py
computations/witness_staleness_triage.py
```

**Deliberately NOT ported in this pass.** The deferral reason (high collision
with the active compute-PR storm) still holds — the storm is live, and **6 of
the 23 are `deltalambda/milnor_*`, which is `qou-v7ro`'s active area**. A
23-file sweep through `computations/` mid-storm is the collision the deferral
exists to avoid. But the scope is now small enough that the deferral is worth
**re-deciding** rather than renewed by default, which is the point of this entry.

**Judgement, marked as such:** I would port the **17 non-`milnor_*`** files as one
commit when the storm quiets, and leave the 6 `milnor_*` to whoever owns
`qou-v7ro`. That splits cleanly along ownership and keeps the diff reviewable.
