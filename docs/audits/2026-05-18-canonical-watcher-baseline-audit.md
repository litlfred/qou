# Canonical-watcher baseline audit — 2026-05-18

**Branch:** `claude/canonical-watcher-skill-UaWnQ` (PR [#694](https://github.com/litlfred/qou/pull/694))
**Anchored to:** `prop:three-calibration-inputs` + `prop:three-calibration-discipline` + the framework's "exactly three calibration inputs" rule (CAL-1 $m_e$, CAL-2 $m_\mu/m_e \to q_0$, CAL-3 $Q_\beta(n)$).

Baseline state of the canonical-derivation discipline across the
codebase at the time the watcher armed, plus a comprehensive
working queue. Cross-references the existing aggregator
([`canonical-derivation-pipeline-compliance.witness.json`](../../computations/canonical-derivation-pipeline-compliance.witness.json))
and the sibling audits that landed during this session.

## 1  Scanner numbers (origin/main HEAD ≈ `f1275207..` then `dc0f9394`)

| Contract | Status | Count | Source |
|----------|:------:|------:|--------|
| WitnessBuilder usage (P30) | **fail** | 96 / 534 files write witnesses by hand | `compute-audit-scan.witness.json` |
| CODATA constants from registry (P31) | **warn** | 28 hardcoded literals outside the allowlist | `compute-audit-scan.witness.json` |
| 3-input canonical scheme (CAL-1/2/3) | **fail** | 14 canonical / 57 over-count / 514 classified | `canonical-script-input-audit.witness.json` |
| Vol-hyp-fitted scripts | n/a | 34 scripts (down from 54 pre-#683) | `canonical-script-input-audit.witness.json` |
| Per-chain trust-basis validation | **pass** | 91/91 assertions across 71 chains | `derivation-chain-audit.witness.json` |
| CAL-3 ↔ CODATA cross-check | **pass** | 9/9 reconciliation assertions | `codata-reconciliation.witness.json` |
| Witness reproducibility (P32) | **pass** | 11/11 builders byte-equal | `witness-reproducibility-check.witness.json` |
| LP/SDP dual variables | **pass** | 3/3 LP-flagged witnesses include duals | `lp-dual-witness-validator` (CI warn-only) |
| Aggregate infra score | n/a | **0.58 / 1.00** | aggregator |

## 2  Active sibling-PR triage (subscribed PRs, last-7-day activity)

| PR | Title | Verdict | Watcher action |
|---:|-------|---------|----------------|
| [#694](https://github.com/litlfred/qou/pull/694) | feat(skills): add canonical-watcher skill | **own** | (this baseline lives on its branch) |
| [#699](https://github.com/litlfred/qou/pull/699) | P31 (b) tranche — Q_50_DIGIT_STR refactor | **own** | 3 P31 hits resolved; awaiting review |
| [#696](https://github.com/litlfred/qou/pull/696) | Flavor-dressing functor + substrate split | **major finding logged** | `probe_flavor_dressed_mass_split.py:95` uses `M_P_MEV_VALIDATION` / `M_N_MEV_VALIDATION` as *prediction inputs* — re-introducing the CODATA m_n − m_p calibration the PR claims to eliminate. Copilot raised; watcher logged queue item `PR-696-validation-alias-as-input`. No duplicate comment from watcher (coordinate.md §5d). |
| [#692](https://github.com/litlfred/qou/pull/692) | proof-integration-watcher skill | clean | sibling watcher; no canonical scope |
| [#691](https://github.com/litlfred/qou/pull/691) → merged via #695 | y_λ ceiling n=12 → n=15 | clean | CAL-2 parametric cache extension |
| [#690](https://github.com/litlfred/qou/pull/690) | substrate m_p/m_n no-tautology | **fixing-a-violation** | Actively eliminates the proton tautology (substrate-pure C2 + flavor-split). Gemini comments on it are code-style, not canonical-discipline. |
| [#689](https://github.com/litlfred/qou/pull/689) | Operator-valued framework + 193-commit merge | clean spot-check | over_count 112→57, vol-hyp 54→34 — substantial discipline win. +2 P31 hits are class-B docstring quotes in `probe_flavor_split_subleading.py:10`. |
| [#683](https://github.com/litlfred/qou/pull/683) → MERGED | Knot-fusion Step 2 + m_p Item A | clean | Class-A opt-out properly banner-marked (`atomic_mass_via_rho_k.py` + `derive_m_p_hecke_path_a.py` docstrings). |
| [#679](https://github.com/litlfred/qou/pull/679) | Wire ρ_K consumer to LR witness + ⁶Li/⁷Li | clean | Wenzl-LR consumer bug documented and disabled. CAL-2 parametric extensions. |
| [#646](https://github.com/litlfred/qou/pull/646) | Lake build mathlib v4.24.0 | out-of-scope | toolchain only |
| [#650](https://github.com/litlfred/qou/pull/650) | q-CLT scope clarification | clean (draft) | expository, no calibration impact |

## 3  Sibling-agent canonical-discipline work landed during this session

These commits on `origin/main` between session-start (`47e07087`) and HEAD landed work directly in watcher scope. The watcher *cross-references* rather than duplicating.

| Commit | Finding | Watcher cross-reference |
|---|---|---|
| [`11ac5e6f`](https://github.com/litlfred/qou/commit/11ac5e6f) | "§13 honest distinction: derivation vs justification" — explicit DERIVATION / JUSTIFICATION / NUMERICAL OBSERVATION / TAUTOLOGY classification of m_p chain | This **IS** the watcher's vocabulary. `λ_p ≈ 5/2 − h²·G at 5.4 ppm` is *justification*, not derivation. 5 R&D items defined for closure. |
| [`74f348c3`](https://github.com/litlfred/qou/commit/74f348c3) | "review: PR #664 c_3/c_4/κ — probes tautological, formulas fit-then-interpret" | Direct watcher pattern (tautology + fit-then-interpret). Already actioned by sibling — do not duplicate. |
| [`d10441668`](https://github.com/litlfred/qou/commit/d10441668) + [`d835f51e`](https://github.com/litlfred/qou/commit/d835f51e) + [`a646ae91`](https://github.com/litlfred/qou/commit/a646ae91) | `tr_M_symbolic` was structurally Plancherel-not-Markov since day 1; deuteron migration applied | **Critical canonical-chain finding** — every prior consumer of `tr_M_symbolic` is suspect until verified. Migration to canonical Markov is the right cleanup direction. |
| [`3befb7ca`](https://github.com/litlfred/qou/commit/3befb7ca) + [`7f0fa726`](https://github.com/litlfred/qou/commit/7f0fa726) + [`e65932ff`](https://github.com/litlfred/qou/commit/e65932ff) | BW-coefficient-shadow-price framework deprecated; `prop:figure-eight-bw-coefficients` removed | Whole framework retired as fit-then-interpret. Cross-referenced as completed canonical-discipline cleanup. |
| [`dc3a8355`](https://github.com/litlfred/qou/commit/dc3a8355) | Scale-gap RESOLUTION: Borromean tower formula at 0.25 ppm | `Vol(B_3) = 8·G` is DERIVATION (Adams 1985 + standard topology). Closes the m_p 1700× scale gap structurally. |
| [`4f63dc80`](https://github.com/litlfred/qou/commit/4f63dc80) | Q6 closure: sync `Q_50_DIGIT_STR` with q-pinning witness (lifts 14-digit floor) | Affects PR #699 — refactor still correct (imports canonical); witness output will refine at digit 17+. |

## 4  Content-level marker sweep — per-file audit results

Brute grep for canonical-discipline marker words in
`content/**/*.md` produced 40 candidate files. A follow-up per-file
read classified each in context — distinguishing the marker
appearing in a legitimate context (math expression, CAL-1/2/3
provenance citation, post-Archimedean τ-image naming) from a
genuine discipline violation.

**Bottom-line:** 32 legitimate / 8 Class-A/B/C opt-out after [PR #715](https://github.com/litlfred/qou/pull/715) lands / 0 unresolved violations.

### 4a  Violations — resolved via [PR #715](https://github.com/litlfred/qou/pull/715)

All 4 files already documented the discipline concern in prose; what was missing was a machine-recognizable Class-A status banner. PR #715 adds those banners.

| File | Original verdict | Resolution |
|------|------------------|------------|
| [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) | violation (fit-then-interpret) | **Class-A banner added** after the existing "Caveat (structural form)" — explicit Workplan-0b + m_p chain closure gap audit references. Structural form correct; numerical instantiation empirical pending $\rho_K$ closure. |
| [`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md) | violation (over-count) | **No change needed** — `† LO TAUTOLOGY NOTICE` banner already in place. Class-A opt-out pending Workplan-0b. |
| [`alpha-em-categorical-trace.md`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md) | violation (PSLQ fit) | **Class-A banner added** after "Status (May 2026)" — legacy form is PSLQ uniqueness match, not derivation; cites structural supersession + Bring zero-mode lead. Block already `remark`-kind. |
| [`atomic-mass-gb-nf.md`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) | violation (multi-form) | **Class-A banner prepended** at §Statement — three forms classified: (GB-NF) production-target (open $\rho_K$); (constituent) Class-A opt-out (CODATA $m_p, m_n$ → Workplan-0b); (six-term spectral) Class-A opt-out ($E_0$ proton-calibration pending CAL-3 derivation). Substrate-pure replacement $m_n = m_p + Q_\beta + m_e$ documented. |

**Underlying discipline concerns remain blocked on**: Workplan-0b (for mass-table forms), structural derivations of $\rho_K$ + $\alpha_{\mathrm{EM}}$. The Class-A banners make the status auditable from source; the math itself is unchanged.

### 4b  Class-A/B/C opt-outs (banner verified)

| File | Class | Where the marker lives |
|------|:-----:|------------------------|
| [`gs-archimedean-agreement-residue.md`](../../content/quantum-observable-universe/braids-and-knots/gs-archimedean-agreement-residue.md) | A | Numerical-witness block with transparent `**Status (current Lean encoding)**` + explicit `sorry` — acknowledged stub. |
| [`per-braid-mass-tower.md`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md) | C | Diagnostic cross-check; line 169 banner: *"No τ-image quantities (hyperbolic volumes, Mostow rigidity, etc.) appear in the per-braid mass formula."* |
| [`recomputed-low-isotope-mass-table.md`](../../content/quantum-observable-universe/braids-and-knots/recomputed-low-isotope-mass-table.md) | A | (listed above; the † LO TAUTOLOGY NOTICE banner is in place) |
| [`kashaev-volume-conjecture.md`](../../content/quantum-observable-universe/braids-and-knots/kashaev-volume-conjecture.md) | A | The whole block is the KVC conjecture statement — external boundary condition, no algebraic-side derivation. |

### 4c  Legitimate (false-positive marker hits)

32 files where the marker was a false positive on per-file read.
Reasons fell into these patterns:

| Pattern | Count | Example |
|---------|------:|---------|
| `approx` in math context (numerical evaluation of an exact form at $q_0$) | 11 | `hook-weight-derivation.md`, `categorical-chain-convergence-mechanisms.md` |
| Vol/hyperbolic as **post-Archimedean τ-image naming**, not algebraic-side input | 9 | `atom-knot-mass-derivation.md` (lines 176–191 explicitly: *"the volume conjecture…is a **borrowed theorem**…allowing $B(H)/(m_e \nu_{\mathrm{SDP}})$ to be **named** as a hyperbolic volume"*), `vol-through-tau.md`, `geom-yekutieli-alignment.md`, `dilogarithm-archimedean-limit.md` |
| Vol(K) for the **categorical state space**, not an input | 4 | `borromean-baryon-interpretation.md`, `binding-scale-catalan.md`, `frobenius-antipode-unifies-chirality-and-tower.md` |
| External theorem cited as boundary condition (KVC, Ruberman, Gromov norm) | 4 | `conj-canonical-knot-id-sdp.md`, `geom-universality.md`, `conway-kt-vol-injectivity-test.md` |
| "non-calibrated" mode explicitly approved per discipline | 2 | `np-discrepancy-resolution.md`, `topological-mass-trefoil.md` |
| Convergence rate / complexity estimate (not a fit) | 2 | `qmn-recursive-memoized.md`, `hoefsmit-scattering-pipeline.md` |

The audit-doc reader should not chase those 32 — they're documented here so the next watcher pass doesn't repeat the work.

## 5  Working queue — prioritised next actions

In rough priority order (severity × tractability). Items here may live longer than this audit doc; the live state is in `todos/canonical-watcher-queue.json`.

### Critical (carry-forward; sibling work landing)

1. **TR_M_AT_Q0 vs Frobenius τ_M** — pre-existing registry conflict; author-escalated already; `derivation_chain.py:68-93` relabel-to-τ_SW pending. **No watcher action — wait.**
2. **PR #696 validation-alias-as-input** — `probe_flavor_dressed_mass_split.py:95` uses `M_*_MEV_VALIDATION` as prediction inputs. Copilot raised; awaiting #696 author fix. **No duplicate ping — re-check on next push.**

### Major

3. **Workplan-0b: 57 over-count scripts** — biggest remaining canonical-discipline blocker. Per-script m_n = m_p + Q_β rewire. Multi-day scope per `docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md`. Author has accepted scope.
4. **P31 (a) tranche** — 5 mass-prediction scripts blocked on Workplan-0b. Do NOT mass-noqa.
5. **P31 (c) tranche** — 18 audit/probe scripts → `M_P_MEV_VALIDATION` import migration (per-script verification: the alias must enter only as a *comparison target*, never as a downstream-witness input — see #696 violation pattern).
6. **20 content marker hits (§4a)** — per-file triage to separate legitimate uses from genuine violations.
7. **20 archimedean-candidate files (§4b)** — per-file verification.

### Minor (mechanical, ready to discharge)

8. **P31 (b) tranche** — landed in PR #699. **DONE (awaiting merge).**
9. **probe_flavor_split_subleading.py:10 (+2 P31)** — class-B docstring CODATA-target quotes; add `# noqa: P31` with class-B comment.

### Tracking-only (sibling-agent work already in flight)

10. **tr_M_symbolic Plancherel migration** — `a646ae91` started; all prior consumers need verification. *Cross-reference, do not duplicate.*
11. **BW-coefficient-shadow-price framework retirement** — `3befb7ca` + `e65932ff` removed the blocks. *Tracking complete.*
12. **m_p chain closure (5 R&D items per `11ac5e6f`)** — open conjecture-track work. Author-owned.

## 6  Watcher operational state

- **Skill home**: `.claude/skills/local/canonical-watcher.md` (now on `main` per [#703](https://github.com/litlfred/qou/pull/703) — slot-filler under the generic `integration-watcher` parent). This baseline doc was authored when PR #694 was a standalone-form watcher; the substantive content (queue + ledger + taxonomy + audit findings) is unaffected by the refactor.
- **(b) tranche PR**: [#699](https://github.com/litlfred/qou/pull/699) (rebased; Gemini's 2 threads resolved; awaiting CI)
- **Monitor**: armed on `origin/main` (persistent, 5-min poll, TICK heartbeat)
- **PR subscriptions** (11 in watchlist; 2 closed or out-of-scope leaves 9 actively monitored):
  - Own: `#694, #699`
  - Active sibling: `#692, #689, #690, #679, #650, #696`
  - Closed/merged: `#691` (merged via #695), `#683` (merged)
  - Out-of-scope: `#646` (toolchain)
- **Ledger**: `todos/canonical-watcher-ledger.md` (gitignored, working state)
- **Queue**: `todos/canonical-watcher-queue.json` (gitignored, working state)

## 7  Update protocol

This is a snapshot. Drift accrues quickly (the main burst landed 70 commits during this session alone). Refresh whenever:

- main lands ≥ 10 commits (per coordinate.md §8a)
- A subscribed PR closes or has substantive activity
- A new audit doc lands under `docs/audits/`
- The watcher's queue/ledger crosses 30 items (rebaseline)

Update by editing this file, committing on the watcher's home branch, and pushing.

## 8  Derivation-status audit (deep, 2026-05-18 evening)

Author pointed out that §4a's "violations" framing missed that
several flagged blocks **have canonical derivations** that landed
earlier on main. Re-audit produces three lists.

### 8a  Canonical derived (KEEP)

| File | Label | What's derived | Evidence |
|------|-------|----------------|----------|
| `braids-and-knots/rho-k-graded-expansion.md` | `prop:rho-k-graded-expansion` | LO piece $Z m_p + N m_n + Z m_e$ via Markov multiplicativity | Wenzl 1988 Thm 5 proved; witness at $3.2 \times 10^{-14}$ |
| `braids-and-knots/rho-k-h3a-refinement.md` | `prop:rho-k-h3a-refinement` | Single-gen binding $\alpha \sum_i \ln\lvert\hat V_i\rvert$ | Kashaev-limit derivation; 0.18% accuracy |
| `descartes-universe/alpha-em-categorical-trace-ratio.md` | `prop:alpha-em-categorical-trace-ratio` | $\alpha_{EM} = h^2 / (q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5}))$ | Categorical trace ratio; $10^{-12}$ at $q_0$ |
| `descartes-universe/em-coupling-bring-zero-mode.md` | `prop:em-coupling-bring-zero-mode` | Additive Bring zero-mode $1/\alpha = q[9]_q[10]_q + 2/(3\pi)$ | Bloch-Suslin uniqueness; Lean closes the algebraic identity at $g=4$ |
| `braids-and-knots/lambda-scale-substrate-form.md` | `conj:lambda-scale-substrate-form` | $\lambda_{\mathrm{scale}} = 5/2 - h^2 G$ (**justification**, not derivation) | 5.4 ppm match; $\mathrm{Vol}(\mathcal{B}_3) = 8G$ derived (Adams 1985); $h^2 G$ correction conjectural per audit §13 |
| `braids-and-knots/three-calibration-inputs.md` | `prop:three-calibration-inputs` | Three external calibrations CAL-1/2/3 aligned to Wedderburn blocks | 19-link chain audit |
| `observations/three-calibration-discipline.md` | `prop:three-calibration-discipline` | $\mathfrak{m}(X) = m_e^{a(X)} Q_\beta^{c(X)} Q_X(q_0)$ | Induction along chain |

### 8b  Current best mass-table compute infra (KEEP)

| Script | Role |
|--------|------|
| `rho_k_graded_expansion.py` | Production: LO + single-gen binding witness |
| `m_p_borromean_verification_50dps.py` | Production cross-check (proton Borromean at 50 dps) |
| `markov_trace_via_wenzl_lr.py` | Production: canonical Wenzl-bridge Markov-trace |
| `y_lambda_wenzl_bridge.py` | Production: Schur principal specialization for $y_\lambda$ |
| `wedderburn_jones_markov.py` | Production: hybrid 30-dps Wenzl + float64 Hoefsmit |
| `rho_k_h3a_refinement.py` | Production: full 50-dps mpmath partition-sum |
| `q_beta_spectral_bridge_witness.py` | Production: CAL-3 prediction at +0.168% vs CODATA |
| `cross_check_trM_wenzl_lr_1ppb.py` | Production: 3-path $\mathrm{tr}_M$ agreement at $\epsilon_{\mathrm{mach}}$ |
| `canonical_tr_m_via_rust.py` + `tools/hecke-engine/` | Production: Rust Hecke-engine R2-R4 (3400× speedup); R5-full prototype landed |
| `alpha_em_pslq_uniqueness.py` | Production witness (multiplicative $q$-rational family ruled out) |
| `lambda_scale_substrate_probe.py` + `lambda_scale_derivation_probes_123.py` | Experimental (conjectural λ-scale chain; tracked for closure) |

### 8c  Deprecated / legacy / probing (REMOVE — aggressive scope per author)

All have canonical replacements on main or are documented falsifications.

| File / section | Why remove | Supersedes / replaced by |
|----------------|------------|---------------------------|
| `descartes-universe/alpha-em-gluon-octet-form.md` (full file) | PSLQ-empirical fit; 100-dps extended scan ruled out multiplicative $q$-rational family | `prop:alpha-em-categorical-trace-ratio` + `prop:em-coupling-bring-zero-mode` |
| `descartes-universe/em-coupling-reeb-holonomy-falsified.md` (full file) | Falsification — Option C ruled out by Reeb-bundle analysis | (negative result; consumed by `em-coupling-bring-zero-mode`) |
| `descartes-universe/em-coupling-stratum-coupling-h3-attempt.md` (full file) | Probing attempt — Option B at $H_3$ doesn't close (3.2% off) | `em-coupling-bring-zero-mode` |
| `braids-and-knots/alpha-em-categorical-trace.md` (full file) | Legacy remark — bare PSLQ-fit, explicit "*retained for historical context*" | `prop:alpha-em-categorical-trace-ratio` (structural) + `prop:em-coupling-bring-zero-mode` (additive) |
| `braids-and-knots/delta-coupling-substrate-form.md` (full file) | **Conjecture REFUTED** at single-magic anchors | (open research; no replacement yet) |
| `braids-and-knots/recomputed-low-isotope-mass-table.md` §Calibrated form (section) | 4th/5th-calibration injection; tautological p/n rows | `prop:neutron-qvalue-symbolic` (framework prediction) |
| `braids-and-knots/rho-k-h3a-refinement.md` §pair-gen piece (section, ~lines 71-113) | Pair-coupling structure incomplete; six-term theorem requires Li₂^q form not log-formula | (open work; LO + single-gen remain) |
| BW-shadow-price family (4 scripts) | Already moved to `computations/_deprecated/` by `3befb7ca` | (already done) |

**Removal PR** (separate from this audit): 5 whole-file deletions + 2 section-level removals + `uses[]` rewires.

### 8d  Correction to PR #715 strategy

- **`alpha-em-categorical-trace.md`** — banner was the **wrong move**; this is a purely legacy block. Correct action: **REMOVE the file** (queued for the removal PR). The banner becomes moot when the file is removed.
- **`atom-knot-mass-derivation.md`** — banner stands. Block is the canonical mass-derivation entry point; its 173× shortfall is captured by ρ_K (derived) + λ_scale (conjectural at 5.4 ppm).
- **`atomic-mass-gb-nf.md`** — banner stands. Three-form classification correctly attributes derivation status per form.

PR #715's `b4c9daa1` reanalysis already updated the two stand-firm banners to cite the derived substrate machinery. The third banner (alpha-em-categorical-trace.md) is moot in the removal PR's diff.
