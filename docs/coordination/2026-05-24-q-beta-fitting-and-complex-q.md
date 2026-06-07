# Coordination ledger — Q_β fitting concern + complex-q substrate exploration (2026-05-24)

**Owner branch / PR**: `claude/gifted-feynman-U7ckD` → [#1127](https://github.com/litlfred/qou/pull/1127)

**Goal**: resolve whether `Q_β = |Δ(net)| · E_0` is a genuine derivation of Q_β from CAL-1 + CAL-2 OR a numerical coincidence; structurally place the framework's complex-q admissibility on the historical-trajectory of ℂ in physics; identify the projection rule (P_avg / P_skew per bar-involution.md) as the structural reason for the framework's "real q" convention.

## Scope map (2026-05-24 snapshot)

| PR | Title | Author | Branch | Classification |
|---|---|---|---|---|
| **#1127** (this) | Q_β net-ansatz fitting finding + complex-q substrate lift exploration | @litlfred | claude/gifted-feynman-U7ckD | **own** |
| #1153 | sinh-partner: bar-anti-symmetric Q_m partner of unified binomial P_m | @litlfred | claude/sinh-bar-antisymmetric-partner-probe-2026-05-24 | **scope-overlap (bar-involution / P_avg-P_skew structure)** — see [coord comment](https://github.com/litlfred/qou/pull/1153#issuecomment-4530026297) |
| #1180 | qa(arch-tag): beta_ew_delta_I_321_and_wedderburn | @litlfred | claude/qa-arch-beta-ew-321-2026-05-24 | scope-adjacent (beta-ew + Wedderburn touches same domain; no file overlap — they tag the production script as "archimedean by design", my work touches content blocks + audits) |
| #1179 | qa: respects_archimedean_wall for beta_ew_conj_pairing | @litlfred | claude/qa-arch-beta-ew-conj-pairing-2026-05-24 | scope-adjacent (beta_ew_conj_pairing.py — "conjugate pairing" name suggests bar-involution structure; no file overlap) |
| #1172 | qa: beta-decay-scale math → mp | @litlfred | claude/qa-arch-beta-decay-scale-2026-05-24 | scope-adjacent (touches beta-decay-energy-scale compute; my edit was to the .md sibling, no overlap) |
| #1160 | qa: beta-decay math → mp.sqrt | @litlfred | claude/qa-arch-beta-decay-2026-05-24 | scope-adjacent (same reasoning) |
| #1152 | docs(cheat-sheet): fold in 3 substrate→EW empirical-match hypotheses | @litlfred | claude/ew-hypotheses-cheat-sheet-fold-in-2026-05-24 | scope-overlap (empirical-match hypotheses parallel my "fitting concern"; both touch cheat-sheet) |
| #1062 | Workplan v2: Python/Rust library production-readiness coord | @copilot | copilot/analyze-python-rust-library-reuse | meta-coordinator; my work is sibling-independent per its established norm |

Other PRs (#1178, #1177, #1175, #1171, #1169, #1170, #1166, #1163, #1158, #1156, #1155, #1165): low/no overlap with Q_β / complex-q / bar-involution structure.

## Per-sibling classification (skill §2 axes)

### PR #1153 — sinh-partner (HIGH overlap, no file conflict)

| Axis | Value |
|---|---|
| **Overlap** | Both PRs explore the bar-(anti-)symmetric projection structure. #1153 derives the EXPLICIT P_skew form (`Q_m = sinh / 2 cosh`); my PR places this in the structural-physics context (Born projection / Schrödinger-trajectory) and the empirical-fitting context (+0.17% Q_β residual). |
| **Dependency** | None (no file overlap; both can land independently). |
| **Cherry-pick candidates** | My PR's Path D Hermiticity audit could cite Q_m / P_m identity; #1153 could cite my historical-trajectory doc as the place-on-the-map. Both done via cross-link comment, no code cherry-pick needed. |

### PR #1180 — qa(beta_ew + Wedderburn) (LOW overlap, no file conflict)

Mechanical qa-wall tagging on production script. The beta_ew + Wedderburn keyword overlap is at the topic level only; no shared files. **Action**: none.

### PR #1179 — qa(beta_ew_conj_pairing) (LOW overlap, name overlap)

The "conjugate pairing" terminology overlaps with my bar-involution / Hermitian-* work conceptually. Worth a quick check after this PR's reconciliation update — does the file `beta_ew_delta_I_conjugate_pairing.py` actually use the framework's bar / Hermitian involution, or is "conjugate pairing" used in a different sense? **Action**: defer — no blocker.

### PR #1172 — qa(beta-decay-scale) (LOW overlap)

Touches `beta-decay-energy-scale` compute script (the .py); my work touches the .md sibling (added ansatz disclaimer). No file conflict; both are honest improvements to the same content cluster. **Action**: none.

### PR #1160 — qa(beta-decay) (LOW overlap)

Same as #1172 — different script, same cluster, no conflict.

### PR #1152 — ew-hypotheses-cheat-sheet-fold-in (MEDIUM overlap, cheat-sheet)

Both PRs touch `docs/canonical-derivation-cheat-sheet.md` (mine added §"Adjacent open work" entry for complex-q; #1152 folds in 3 substrate→EW empirical-match hypotheses). Need to check if the cheat-sheet edits will conflict on rebase. **Action**: check + coordinate if both need to land; otherwise defer.

## Coordination comments posted

| When | PR | Comment |
|---|---|---|
| 2026-05-24 | #1153 | https://github.com/litlfred/qou/pull/1153#issuecomment-4530026297 (structural reconciliation: P_avg/P_skew already in framework; my Path D + historical-trajectory tie to the same projection structure) |

## Escalations (skill §6 — none yet)

None this cycle. The reconciliation with PR #1153 / `bar-involution.md` is a strengthening, not an inconsistency.

## Inconsistent findings caught

**My Path D audit's "modulus projection" answer was INCOMPLETE** — the framework's actual projection is sharper (`P_avg` bar-symmetric, not generic modulus). Updated `2026-05-24-q-beta-net-ansatz-fitting-finding.md` §"Path D execution" with a reconciliation-update banner; updated `2026-05-24-complex-q-historical-trajectory.md` with a stage-3.5 (P_avg) refinement of the Born-stage classification.

## Main-branch landings during session (skill §8)

| Commit | Title | Affects this PR? |
|---|---|---|
| 3f653ce8 | duality-closure(D11): Wigner SU(4) from D9 + D10 — Cluster B completion scaffold | No (different domain — duality closures, not Q_β / bar-projection). |

## Phase A v2 — DONE — Outcome (d)

`q_beta_complex_q_test1_phaseA_v2.py` (1D Apollonius parametrization, 360-sample θ scan + sign-change refinement) returned **outcome (d)**: **NO joint solution exists anywhere on the Apollonius circle** under the Q_β ansatz. Residual is positive everywhere (min +1.31 keV at θ=0 real axis; max +508 keV at θ=180°). Im(q) does NOT close the residual.

This **rules out** the simple "Im(q_0) absorbs the residual" hypothesis under the ansatz; combined with Path D's finding that the canonical mass formula uses SUPERSEDED `ρ_q = 1/ℏ_q²`, the next decisive step is the **purge** of the SUPERSEDED ρ_q and re-derivation in canonical form.

## SUPERSEDED-ρ_q purge (in progress)

Per owner directive ("aggressive removal. update coord docs. rederive mass ratio, q relationships etc."):

- Audit doc: [`2026-05-24-superseded-rho-q-purge.md`](../audits/2026-05-24-superseded-rho-q-purge.md)
- Survey: 13 content files + 2 compute scripts + 3 implicit-usage key files
- Phase 1 (banner pass): in progress this commit
- Phase 2 (compute scripts): queued
- Phase 3 (re-derivation of m_μ/m_e + Q_β in canonical form): queued analytical work

## Next concrete tasks on the queue

1. Continue SUPERSEDED-ρ_q banner pass across the remaining 11 content files
2. Audit `q_pinning_50_digit.py` and `rho_f_categorical_probe.py` for ρ_q dependence
3. Re-derive m_μ/m_e at the operator (per-braid mass tower) level — lepton variant of `prop:rho-k-graded-expansion`
4. Re-run Phase A v2 with the canonical (non-ρ_q) form
5. Reassess error attribution after re-derivation

## 2026-05-25 sweep update — new siblings + T6 progress

**New sibling: PR #1246** (cal-2 critique) — direct parallel to PR #1127's CAL-3 droppability audit:
- Posts: https://github.com/litlfred/qou/pull/1246#issuecomment-from-this-sweep
- Same author / Claude-Code session pattern
- Cites PR #1127 explicitly in its summary
- Status: classified HIGH-overlap upstream — both papers critique the calibration self-referentiality

**Sibling PR #1228** (vol-density-derivation bug squash) — implicated downstream by T6 H_3 3-channel finding:
- Their §10.1 action item (chi_lambda_braid Python wrapper) is closed by PR #1127's `per_generator_V_hat_general.py`
- Coord comment already posted: https://github.com/litlfred/qou/pull/1228#issuecomment-4531215100

**Sibling PR #1224 + #1229** (Δ_λ closure + bar-invariance probe) — related but DIFFERENT layer:
- Δ_λ = partition-level closure; T6 = lepton-mass-level closure
- Both implicate "additional structural constraint not currently in framework"

**Main movement (last cycle)**: `88f06a42 Q3(lean wire-up): name χ^{(2,1)}(β_Bor) in HeckeH3.lean §3b` — Lean H_3 infrastructure for standard rep, directly adjacent to PR #1127's `lepton-bring-surface-h3-3channel.lean` Hoefsmit-traced std-channel formula.

**T6 STATUS (after this sweep)**:
- ✓ Compute infra closed (`per_generator_V_hat_general`)
- ✓ V̂_e calibration matches paper (H_3 3-channel convention)
- ✓ Gap (a) RESOLVED — convention documented
- ⚠ Gap (c) STRONGLY IMPLICATED — factor 1.493 ≈ (3/2)/ℏ_q² is SUPERSEDED ρ_q reappearing
- ⚠ Tau T(2,7) divergent under H_3 3-channel — canonical tau braid may need re-examination

**Next analytical work** (multi-session):
- Structural derivation of the (3/2)·(1/ℏ_q²) factor from operator-level formula
- OR explicit acknowledgement that framework's mass formula IS Skein (Vol/ℏ_q²) with SUPERSEDED ρ_q openly carried

## 2026-05-25 evening sweep (post T6 closure) — new siblings + 3 coord posts

**T6 muon side CLOSED** this cycle:
- Lean: `three_halves_factor_eq_q_brackets` proves `(3+h²)/(2+h²) = [3]_q·[2]_q/[4]_q` (`three-halves-structural-factor.lean`)
- `conj:lepton-tower-h-n-plus-1-branching` content block: categorical conjecture `ξ_m = d_q((m+1,1))·[2]_q/[m+2]_q·(1/ℏ_q²)` matching muon to 0.034% CODATA
- Tau case falsified for simple extension (predicts ξ_3 ≈ 161.7 vs required ~4968)

**Three new siblings classified + coord intent posted**:

| PR | Topic | Overlap | Coord comment |
|---|---|---|---|
| **#1250** (m_τ knot prediction) | Cohomological knot hierarchy test for tau | HIGH — independent tau falsification at +1.33% confirms PR #1127's T6 tau falsification at 30× | [posted](https://github.com/litlfred/qou/pull/1250#issuecomment-4531694642) — mutual cross-check + extensions mapping |
| **#1251** (H_3-vs-H_n hardcode infra audit) | pyhecke-native Rust ABI H_3 lock | HIGH — same wall as T6 tau (needs H_5 embedding); my `per_generator_V_hat_general` is the Python-level workaround for what they identify as Layer B fix | [posted](https://github.com/litlfred/qou/pull/1251#issuecomment-4531695582) — complementary fixes |
| **#1252** (Option E Kashiwara crystal Δ_λ) | Kazhdan-Lusztig classical limit for Δ_λ(K) | MEDIUM — provides Option (C) categorical interpretation for my muon ξ_2 = [3]_q·[2]_q/[4]_q factor (d_q((3,1)) = S_4 std rep) | [posted](https://github.com/litlfred/qou/pull/1252#issuecomment-4531696668) — Kazhdan-Lusztig route may close PR #1127's "categorical derivation" open work |

**Owner action this cycle**: reversed the 2026-05-08 declination of substrate-q_0 derivation (now re-opened as in-scope research per PR #1249). PR #1127's `prop:q-zero-complex-extension` content block is now upstream-relevant to this re-opened research direction.

**No escalations**: all sibling findings mutually reinforcing; no inconsistent framings.

## Anti-patterns avoided (skill §11 review)

- ✗ Did not "split the difference" on the bar-involution reconciliation — explicitly updated the Path D audit to acknowledge P_avg/P_skew supersedes generic modulus projection.
- ✗ Did not silently merge `main` — fetched + classified the new commit (`3f653ce8`) as not-affecting-this-PR.
- ✗ Did not add a newly-opened sibling PR to scope without prompting — proposed scope map here; will run by owner if they want to expand it.
- ✗ Did not post a "stream" of comments on #1153 — single consolidated coordination comment.
