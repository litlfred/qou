# Convention-C excision, re-measured — and which closed gates rest on C compute

**Date:** 2026-09-06 · **Bean:** `qou-htsi` (parent `qou-2akx`) · **Branch:**
`claude/convention-c-excision-2026-09-06` from `9b009da0e6` ·
**Owner directive (verbatim, 2026-09-06):** *"Be suspicious of closed gates based
on compute. Lots of stale and sibling found convention C still around. Need to
excise that."* / *"As you write probes validate not dependent on convention C."*

Memory compliance: `MEMORY.md` (235 lines, `69e278d406`) +
`functional-and-bond-topology.md`, `q0-pin-migration.md` were read before any
measurement below was taken.

## 0. The one-paragraph answer

The three detectors were re-run on this HEAD. The value audit's **26 BLOCKING**
sites (the morning's 25 on `main`, plus one) are **all** sibling-added research
probes on the convention-C Q_β ladder or deliberate C-vs-D comparisons: **zero**
of them is a live producer computing a Markov-trace quantity that substituting
`z_D = q³/(q²+1)` for `z_C = √q/(q+1)` would validly migrate. So no witness
was regenerated and no `z` was swapped; the 26 were **adjudicated** into the
committed ledger with a verdict each (12 `comparison`, 14 `deliberate-c-frame`),
which is what turns "unaccounted C" into "C, with a written reason" and lets the
gate reach green honestly. Two detector blind spots were found and fixed (one a
false *positive*), two Lean C definitions were scoped by docstring, and the
survey of closed gates found that the C-dependence of the corpus's refutations
is concentrated in one place — the `c_k` ladder arc — where `AGENTS.md` already
scopes it globally but the individual audit docs do not say so.

## 1. Counts — before and after, on this HEAD

All three commands were run on `9b009da0e6` before any edit (BEFORE) and on the
branch tip (AFTER). **Re-run before quoting**; every figure in this table has
moved between sessions before.

| detector | command | BEFORE | AFTER |
|---|---|---|---|
| value audit (`.py`, by evaluation) | `python3 scripts/convention-c-value-audit.py --all` | **137 confirmed C / 111 adjudicated / 26 BLOCKING / 1 UNRESOLVED**; 509 D; exit 1 | **137 / 137 / 0 / 0**; NOT-C 5 → 6; exit 0 |
| shape audit (`.py`, by AST) | `python3 scripts/convention-c-producer-audit.py` | **13 actionable** (6 probes/exploratory, 6 `qbeta` registry-blocked on `qou-cds1`, 1 live producer) + 1 blocked-by-design + 113 deliberately C-named; 1 C-specialised closed form (measured false positive) | unchanged — the shape audit reads names, and no source was renamed (deliberately: renaming to satisfy a detector is the audit-dodging AGENTS.md §1a forbids) |
| Lean audit (`.lean` defs) | `python3 scripts/lean-markov-convention-audit.py` | **24 C defs → actionable 3 / deliberate 21**; 50 D defs; 211 sites | **23 C defs → actionable 0 / deliberate 23**; 210 sites |

The bean's morning figure was 136 / 25 on `main`; this HEAD (`9b009da0e6`,
13:18 UTC) carries one more of each — `qbeta_c_vs_d_are_different_algebras_probe.py`
(`336a35ff27`, same day). The count is moving *up* as `qou-cds1` research lands,
and every new row is in that arc.

Where the 26 came from: 8 files carry a distinct commit after 2026-08-30
(`6a8fd95c09` 08-31, `06410f19d7` 09-02, `94f32ef99f` 09-02, `d7a1638536` 09-03,
`0e64473584` and `1f3d3cae05` 09-05, `336a35ff27` / `9462d1b41c` / `bfa3179118`
09-06); the other 15 resolve only to `69e278d406` (2026-09-05 06:39), a
91,219-file tree-import commit, so their true added date is **≤ that and
unknowable from this clone**. `qou-t9r1` reported 0 BLOCKING on 2026-08-30
(#6224), so all 26 either landed after it or had their source line edited since
(the ledger key expires on any edit). Either way they were unadjudicated on
this HEAD.

## 2. The 26 sites, read one by one — none migratable, all adjudicated

Column *migrate?* is the step-2 question: is this a live producer or probe
computing a Markov-trace quantity where `z_C → z_D` is a valid migration?
`z` is unchanged in every row; the "drain" is the ledger entry.

| # | site | binding | read as | verdict entered | migrate? |
|---|---|---|---|---|---|
| 1 | `markov/weak_vertex_substitution_scale_probe.py:131` | `zC` | stale engine reduction re-summed at **both** `zC` and `zD` to show two stale W values are one defect; `fixed_D` canonical | `comparison` | no — C arm is the finding |
| 2 | `markov/weak_vertex_t35_trace.py:71` | `Z_C` | beside `Z_D = hs.z_markov` (a call — co-bind hint blind); comment *"deliberate comparison ONLY"*; W(q) derived under D | `comparison` | no |
| 3 | `probes/markov_loop_value_product_and_framing_ratio.py:78` | `zC` | thesis *"D has a clean framing ratio … C has neither"* | `comparison` | no |
| 4 | `probes/ocneanu_weights_are_sl_n_quantum_dimensions.py:207` | `zCs` | §3 *"convention C is in no member of the family"* — C is the object excluded | `comparison` | no |
| 5 | `probes/row_cap_is_one_boundary_probe.py:498` | `zC` | printed beside `zD` to show which solves `z·[N]_q = q^N` | `comparison` | no |
| 6 | `probes/the_qbeta_bridge_table_and_its_witness_compute_different_z_probe.py:108` | `z_prop()` | reproduces `prop:q-beta-spectral-bridge`'s own C definition to measure a 21 % table/witness discrepancy (`qou-i229`) | `comparison` | no |
| 7 | `probes/wenzl_bridge_self_conjugate_premise_is_false.py:222` | `zC` | *"the measurement, both conventions"*; `zD = q**2/sym_int(2)` (D spelled via `sym_int`, hint blind) | `comparison` | no |
| 8 | `qbeta/qbeta_c_vs_d_are_different_algebras_probe.py:113` | `zC` | scope-(b) symbolic: C and D are different algebras | `comparison` | no |
| 9 | `qbeta/qbeta_d_frame_bar_even_normalisation_deadend_probe.py:90` | `zC` | rescaled `z_D/q²` compared to the C form | `comparison` | no |
| 10 | `qbeta/qbeta_d_gate_inventory_is_exhausted_probe.py:48` | `zC` | check 1: `solve(zC = zD)` → only `q = 1` | `comparison` | no |
| 11 | `qbeta/qbeta_discriminant_curve_in_q_probe.py:295` | `z_C()` | helper beside `z_D()`, C-ladder phase vs D discriminant curve | `comparison` | no |
| 12 | `qbeta/qbeta_d_frame_z_determinations_experimental_budget_probe.py:174` | `z_C` | *"the excised convention"* priced beside cap / mass / decay determinations | `comparison` | no |
| 13 | `qbeta/qbeta_bring_elliptic_generator_probe.py:99` | `Z_C` | `THETA_REQ = \|(Z_C−1)H/2 − U/2\|` — the C-frame ladder's required phase | `deliberate-c-frame` | no — `qou-cds1` |
| 14 | `qbeta/qbeta_c3_derivative_vs_value_precision_probe.py:93` | `z` in `QN2` | *"N=2 truncation, convention C — the frame the extraction was done in"* | `deliberate-c-frame` | no — `qou-cds1` |
| 15 | `qbeta/qbeta_cosine_parametrisation_justification_probe.py:119` | `Z_C` | *"THE MEASUREMENT (proton pin, 50 dps, convention C)"*, `Z_D` beside it | `deliberate-c-frame` | no — `qou-cds1` |
| 16 | `qbeta/qbeta_d_eigenphase_projection_through_ladder_probe.py:109` | `zC` | derived D correction pushed through the C ladder; `zC` is the object under test | `deliberate-c-frame` | no — `qou-cds1` |
| 17 | `qbeta/qbeta_decay_functional_unification_protium_probe.py:123` | `Z_C` | the ladder reading *wants* `z = 0.4991` (= `Z_C`) vs trace reading 0.9985 | `deliberate-c-frame` | no — `qou-cds1` |
| 18 | `qbeta/qbeta_decay_operator_elliptic_spectrum_probe.py:124` | `Z_C` | `THETA_REQ` C-frame; ellipticity of Δ_L is z-independent | `deliberate-c-frame` | no — `qou-cds1` |
| 19 | `qbeta/qbeta_eigenphase_tower_and_fraction_readings_probe.py:115` | `Z_C` | `TH_REQ` C-frame (0.0565947) | `deliberate-c-frame` | no — `qou-cds1` |
| 20 | `qbeta/qbeta_holonomy_spectrum_sign_obstruction_probe.py:82` | `Z_C` | sign argument z-independent; compared target C-frame | `deliberate-c-frame` | no — `qou-cds1` |
| 21 | `qbeta/qbeta_imq_elliptic_generator_refutation_probe.py:108` | `Z_C` | `THETA` C-frame; Part-1 refutation rests on `\|q\| > 1` (z-independent) | `deliberate-c-frame` | no — `qou-cds1` |
| 22 | `qbeta/qbeta_ladder_alpha_provenance_probe.py:106` | `z_C` | asks what derives `α = (z−1)h/2`; `z_D` beside it | `deliberate-c-frame` | no — `qou-cds1` |
| 23 | `qbeta/qbeta_level_k_operator_and_real_decays_probe.py:121` | `Z_C` | `TH_REQ` C-frame; "corpus never leaves H₃" is z-independent | `deliberate-c-frame` | no — `qou-cds1` |
| 24 | `qbeta/qbeta_precision_ladder_n5.py:160` | `zC()` | **a producer** (`qbeta-precision-ladder-n5` witness); docstring: *"EVERYTHING HERE IS CONVENTION C … no number here should be quoted as a D-frame result"* | `deliberate-c-frame` | no — `qou-cds1`; its witness is C-frame |
| 25 | `qbeta/qbeta_required_phase_target_provenance_probe.py:99` | `z_C` | target `Q_exp/(Q_A(1−u²))` is z-independent; ladder phase compared to it is C-frame | `deliberate-c-frame` | no — `qou-cds1` |
| 26 | `qbeta/qbeta_wenzl_c3_candidate_audit_probe.py:88` | `z` in `ladder_N3` | *"Convention C (the frame the ledger was written in)"* | `deliberate-c-frame` | no — `qou-cds1` |

Two things the table establishes that the counts do not. First, the C surface
that is growing is **the `qou-cds1` research arc itself** — 14 of 26 are the
ladder being investigated *in its own frame*, which is the only frame it exists
in until it is re-derived. Adjudicating them `deliberate-c-frame` (a verdict
string chosen so no reader mistakes it for a comparison) is the honest record;
migrating them would make each probe report a fact about a premise it no
longer has. Second, the co-binding hint the audit uses to *propose* ledger
entries missed 11 of the 26 for four distinct reasons — D arm is a call (#2), D
spelled via `sym_int` (#7), two helpers in separate `def` scopes (#6, #11), and
no D arm at all (the ladder rows) — so a drain that took only the proposed
stubs would have left 11 blocking and read as finished.

### 2a. What was deliberately NOT touched, with bean ids

- **The `c_k` ladder and every value-level `c_k` fact** — `qou-cds1`. Not a
  z-swap, by a sorry-free Lean result; nothing here re-derives it.
- **`gram_h3_det_factorization.py` / `gram_h3_symbolic_regression.py`** —
  `qou-pmkh` items 1-2 / `qou-cds2`: under D the determinant is identically
  zero, so the substitution would prove a false statement.
- **`deltalambda_bareven_b4_magnitude_probe.py:131,137`** — `qou-pmkh` item 3:
  `z_C` is bar-even, `z_D` is bar-neither; the substitution flips the probe's
  own assertion.
- **`qbeta_c3_barodd_hs_matrix_resolvent_probe.py`, `qbeta_c3_cross_anchor_exactness_probe.py`** —
  `qou-pmkh` item 4 / `qou-cds1`; the first also carries the `TR_M[5]` bug
  that already invalidates its recorded refutation (`qou-dbau`).
- **The 13 registry `blocked_on_rederivation` rows and the 111 pre-existing
  ledger comparisons** — accounted, not excused; unchanged.
- **`qou-mass/src/qou_mass/_internal/`** — generated; not edited. No file in
  its sync cone was edited either (`computations/` is untouched on this branch),
  so `scripts/sync-qou-mass-vendor.py --check` has nothing to see.
- **`probes/nucleon-lp-convention-probe.py:87`** (`z_old`, the shape audit's
  "probes / exploratory" row) — a labelled three-convention comparison that the
  value audit cannot evaluate (taxonomy row 38); left as is, recorded.
- **The shape audit's 13 "actionable"** — 6 are the `qou-cds1` registry rows,
  6 are the value-adjudicated comparisons above under other names, 1 is
  `qbeta_ck_cache.py` (the canonical C-frame producer, `qou-cds1`). Renaming
  bindings to make that number fall is exactly what the ledger exists to avoid.

## 3. Lean

| site | before | disposition |
|---|---|---|
| `information-theory/toffoli-lp-stability.lean:590` `coneCoordRow5 q := coneRow5Numerator q / (q ^ 2 + 1) ^ 2` | `C-sqrtvar/actionable` | **detector false positive** — the regex took the applied argument `q` as the numerator and ignored the `^ 2`; the site is convention D by its own docstring. Guard added (`_sqrtvar_hit`), taxonomy row 37 |
| `lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean:1038` `markov_parameter := Real.sqrt q / (1 + q)` | `C-plain/actionable` | genuine C, the C-frame ladder's parameter (`delta_tau_M_canonical`, `c_k` Taylor orders). **Docstring-only** scoping: *"Convention C, deliberately — not the canonical Markov parameter"*, with the `qou-cds1` reason and a pointer to `QOU.BraidKnot.markovZD` |
| `mass-endomorphism/qbeta-per-block-chi-closed-forms.lean:362` (content sibling of the above) | `C-plain/actionable` | same docstring |

**Verification limit, stated plainly:** no olean tree exists in this container
(neither the worktree nor `/home/user/qou` has a `.lake` build), so the Lean
edits were **not** machine-verified. They are confined to the inside of an
existing `/-- … -/` block and introduce no `-/`; the declarations, types and
proofs are byte-identical. The content sibling's `.qa.json` sidecar hash will
drift and was not refreshed (no `folio-assistant` clone here). Both facts are
in the commit message.

## 4. Survey — closed gates whose evidence is convention-C compute

Method: not a verdict-word grep (that returns 366 candidates, most of them
"closed form"). Instead **from the C surface outward**: for each of the 147
files carrying a confirmed C binding (137 Python sites + the Lean C defs),
find every `docs/audits/*.md`, `docs/coordination/*.md` and `.beans/*.md`
that names the file's stem, count strong verdict words in that doc, and check
whether the doc scopes itself C. 139 of the 147 are cited somewhere; 101
(file, doc) pairs carry a verdict and no C-scoping; 43 of those carry a
*strong* verdict (REFUTED / ruled out / dead end / pruned / does not
reproduce / scope-(b)). Each of those was read at the citing lines. The
classification below is (i) unaffected — convention-independent statement;
(ii) C-conditional — must be re-scoped; (iii) already re-derived under D.

| verdict (doc : line) | C evidence it rests on | class | one-line reason |
|---|---|---|---|
| `2026-06-24-lw2-c2-independent-test-attempt.md` L108 *"Hopf-link Markov trace, alone, does not reproduce the selection-rule c=2 value"*; bean `z2bn` | `lw2_c2_independent_hopf_test_attempt.py:106` — C-premised (`(q−1/q)z+1 = 1+(q−1)/√q` holds only at `z_C`; `qou-t9r1` BLOCKED) | **(ii)** | the Hopf closed form tested is a C-frame object; the "does not reproduce" is a C-frame number. Doc does not say so |
| `2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md` L20-31 — swing "refuted", bar-odd sector "pruned" | `qbeta_c3_barodd_hs_matrix_resolvent_probe.py` (C ladder, `qou-pmkh` #4) **and** it carries the `TR_M[5] = z³` bug; `qou-dbau` records that correcting it flips `pairing_is_bar_even` to FALSE, "which is what that probe's conclusion rests on" | **(ii)**, and worse than C-conditional | the pruning rests on a probe that is both C-frame and mis-traced; `qou-dbau` (open) is the re-derivation |
| `2026-07-03-eta-singularity-unit-circle.md` L66 *"refuted odd-sector functional forms"* | `qbeta_eta_singularity_probe.py:180` `zq = √q/(q+1)` — registry `blocked_on_rederivation`, and one of the three `qou-t9r1` marks as C-frame **by inference** | **(ii)** | C-frame `c_k` ladder input; AGENTS.md scopes the ladder globally, this doc does not |
| `2026-06-10-qbeta-ck-state-of-play-synthesis.md` — 10× refuted, "ruled out structurally" (L84) | `qbeta_prearchimedean_z_recursion.py` (z_C satisfies the D-finite ODE; z_D leaves a residual) + the whole C-frame `c_k` family | **(ii)** | the synthesis is a C-frame document end to end; every `c_k` refutation in it is C-conditional per the `qou-cds1` banner in AGENTS.md, which this doc predates |
| `2026-06-13-reeb-phase-qbessel-identification.md` L50/L92 refuted f-map family, "numerical dead end"; `2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md` L64; `2026-08-01-c3-hypersensitivity-is-u3-extraction-artifact.md` L74 *"ruled out"* | `qbeta_utils.py::markov_parameter` (C) and `substrate_ladder_quantities` (`z = 1/(sq+1/sq)`, :268) — the extractor `c3_target_at` every one of these reads | **(ii)** for any *value* of `c₃`; **(i)** for the `1/u³` amplification argument itself (a statement about the extractor's Jacobian, frame-independent in form) | "hypersensitivity is an extraction artifact" survives a frame change; the numbers quoted do not |
| `2026-08-31-qbeta-imq-elliptic-generator-refutation.md` L113 *"refuted here — neither candidate role can do it"* | `qbeta_imq_elliptic_generator_refutation_probe.py:108` `Z_C` → `THETA` | **(i)** for the refutation, **(ii)** for its numbers | Route A is refuted by `\|q\|² = x²+y² > 1` for every Im(q) — no `z` in it. The "required correction 0.998399 / θ = 0.0566" it is set against is the C-frame ladder's; re-scope those figures, keep the verdict |
| `2026-05-30-casimir-epsilon-vacuum-investigation.md` L435 *"ruled out specific candidate forms"* | `casimir_phi_q_markov_probe.py` tabulates three z (C, `1/[2]_q`, …) | **(i)** as written | the probe already sweeps conventions ("multiple conventions; tabulate"); the ruling-out is per-form across all three. Predates the D ruling; a reader should know that |
| bean `qou-edt7` — *"THE WHOLE COORDINATION-MULTIPLICITY FAMILY IS EXCLUDED"*, "REFUTED — single-ratio (Markov-power) scaling, for EVERY r" | `binding_functional_extensivity_probe.py:104`, `coordination_weight_rise_and_turnover_probe.py:125`, `he4_body_order_shortfall_location_probe.py:108` — all **two-arm** (`z_C` beside `z_D`, ledger `comparison`) | **(iii)** | every one of these probes measures the frame difference explicitly; the exclusion is stated in D with the C arm as a check |
| bean `qou-hcas` — `y_eq_self_conjugate` "refuted 2026-09-02, dropped on owner ruling A" | `wenzl_bridge_self_conjugate_premise_is_false.py:222` — both conventions measured | **(i)** | FALSE under C *and* D; that is why the probe binds both |
| `2026-08-29-delta-fork-at-admissible-parameters.md` L92 "excluded"; bean `qou-bg3w` | `qbeta_delta_element_fork_pricing_probe.py:122` `Z_C` beside `Z_D`; the doc is built on `ConventionDAdmissibleRoots.lean` | **(iii)** | a D-frame result with a C comparison arm; the doc says *"No claim that either element is refuted. Scope-(a)"* |
| bean `qou-goc9` — "excluded ×3" | `qbeta_which_algebra_the_decay_channel_lives_in_probe.py:77` `Z_C` beside `Z_D` | **(iii)** | bean says *"Scope-(a) throughout: nothing is refuted, neither NF is declared canonical"* |
| `2026-08-08-threerow-sign-crossing-a-dependence-4he-and-lean.md` §5 REFUTED ×2; `2026-08-09-nastokes-orbit-symmetric-readout.md`; bean `qou-jtfo` | `schur_principal_mpmath.py:123` — the `_wenzl_constants_convention_C_HISTORICAL` function | **(i)** | those docs call `y_lambda_at_q0_mpmath`, the live D closed form (the doc says so at L14-16); the C function in the same file is the deliberate historical comparison and is not on their path |
| `2026-09-05-binding-law-arc-synthesis.md` (refuted ×2) | `qbeta_loop_value_pinned_probe.py:176` `1/(Q0+1/Q0)` | **(i)** — not C at all | `1/[2]_q` on a q-variable; was UNRESOLVED in the value audit until `Q0` was added to its name list |
| `2026-09-04-forced-link-normalisation-bond-counting.md` (refuted) | `forced_link_normalisation_bond_counting_probe.py:73` `W_NORM = Q/(Q**2+1)` | **(i)** — not C | `1/[2]_q` on q; the audit files it NOT-C |
| bean `qou-48is` — extremal-principle ordering "REFUTED, scope-(b)" | `GroundStateOrderingRefutation.lean:407` (Lean C def, deliberate) with `ground_state_ordering_convention_independence_probe.py` (`zC` beside `zD`, ledger) | **(iii)** | the companion probe's name and purpose is convention independence |
| `2026-07-03-trace-convention-decision-package.md` — REFUTED / PRUNED | `BorromeanCanonicalTraceDerivation.lean:242` `zMarkov t := t/(t²+1)` (deliberate) | **(iii)** | this doc *is* the C→D decision record |
| `2026-06-16-research-backlog-probes.md` L15 (refuted) | `GramMatrixH3Symbolic.lean:154` `gramEntry` (C, `qou-pmkh` #1-2) | **(i)** | the refuted item there (`cl3-zeta5` ill-posed) does not run through the Gram entries; the Gram `det ≠ 0` itself is the `qou-cds2` C-only fact and is registered |
| `2026-07-12-borel-alien-calculus-utilization-audit.md` L84 (refuted for a Borel-shaped reason); bean `qou-bg3w`, bean `qou-lo1t` | `q-beta-cos-resummation.lean:65` `markovZC` (deliberate) | **(ii)** for anything quoting the cos-resummation's numbers; **(i)** for the Borel-shape argument | the resummation is the C-frame ladder's cosine; the utilization audit's structural point does not evaluate it |
| bean `qou-do3a` (pruned / refuted) | `QBetaPerBlockChiClosedForms.lean:1116` z-recursion bridge (C) | **(ii)** where it cites the `c_k` recursion bridge as evidence | the 3-term z recursion is a C-frame fact (`qou-t9r1` measured z_D leaves a nonzero ODE residual) |

**What the survey shows, in one sentence.** Outside the `c_k` ladder arc, the
corpus's strong refutations either bind both conventions or rest on D; inside
it, the refutations are C-conditional and the individual documents do not say
so — the scoping lives in `AGENTS.md`'s `c_k` banner and in `qou-cds1`, not in
the docs a reader lands on. The (ii) rows above are the list to re-scope
(edit the doc's header, not its numbers, per AGENTS.md §"Scope, do not fix");
none was edited here because each is a dated record of its own analysis and
the scoping sentence belongs in a follow-up that also updates the citing
content blocks.

**What the survey cannot show.** It is a stem-name join: a doc that cites a
C-frame *result* without naming the *file* is invisible to it, exactly as the
corpus-grep checklist's own path 0 warns. And "C-scoped = False" was measured
by regex (`C-conditional|C-frame|convention C|z_C`), so a doc scoped in other
words is over-reported as unscoped, never under.

## 5. Detector findings (two new taxonomy rows)

- **Row 37 — Lean, false positive.** `RE_C_SQRTVAR` matched
  `coneRow5Numerator q / (q ^ 2 + 1) ^ 2`. Guarded; `--selftest` still finds
  all 18 recorded C sites.
- **Row 38 — value audit, two variable-resolution gaps.**
  `z_old = 1.0/(q0**0.5 + qi0**0.5)` (C exactly; `**0.5` + an imported inverse)
  is reported by the value audit *nowhere* and by the shape audit as
  "probes / exploratory" because it is named `z_old`; and `inv = 1/(Q0+1/Q0)`
  (not C) sat UNRESOLVED because `Q0` was not on the fallback name list. The
  second is fixed by adding the name; the first is recorded, not fixed — the
  principled fix is binding-site resolution for every variable, which the
  source already names as the outstanding job.

Also re-measured: the taxonomy table itself has **36 rows** on this tree;
AGENTS.md's "thirty-five" is stale again (sixth time), and this doc makes it
38. Re-count, do not quote.

## 6. Precision preflight

`bash scripts/precision-gates.sh --changed` → `precision-gates: 2 relevant
file(s) changed — running.` … exit 1, with (verbatim):

```
RED: q0-anchor flip q0-anchor refill ratchet import-time dps ratchet never-raises-dps ratchet float64-padding ratchet raw-float64 ratchet witness-value copy ratchet q0-value drift ratchet hardcoded braid word (self-test) mixed mpf/f64 -> serializer
```

None of the files changed on this branch is under `computations/` and none is
named anywhere in the 476-line gate output; the reds are the tree-wide ratchet
state of `main` at 0-behind (e.g. `Q0_FLIP = 1` is `hadron-knot-table`, as
AGENTS.md records). The gate's own advice was followed: the eight audit
witnesses it regenerated were reverted (`git checkout -- computations/`) and
not committed, and no baseline was widened.

## 7. Files

- `scripts/convention-c-value-audit.py` — `Q0` in `_Q_VARS`.
- `scripts/lean-markov-convention-audit.py` — `_sqrtvar_hit` guard.
- `docs/audits/convention-c-comparison-ledger.json` — 111 → 137 entries.
- `content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`,
  `content/quantum-observable-universe/mass-endomorphism/qbeta-per-block-chi-closed-forms.lean`
  — docstring only.
- `docs/audits/2026-08-15-detector-blindness-taxonomy.md` — rows 37, 38.
- `.claude/agent-memory/convention-auditor/MEMORY.md` — TRAPs + baselines.
