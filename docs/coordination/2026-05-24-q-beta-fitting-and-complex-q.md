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

## Next concrete task on the queue

Per the PR conversation, the next user-prioritized item is **Test 1** (simultaneous CAL-2 + CAL-3 fit for complex `q = u + iv ∈ ℂ`). With the reconciliation update folded in, the structurally-cleaner version of Test 1 is:

1. **Phase A (cheap; current session)** — use the existing closed-form ansatz `Q_β = m_e · |q²−2q−1|·(q+1)/(2q³)` extended to complex `q`; solve `|Q_β(u+iv)| = 0.78233` ∧ `Vol(4_1)·(u²+v²)/((u−1)²+v²) = 206.768` with mpmath. ~30 min.
2. **Phase B (heavier; queued)** — wire the canonical P_avg per-braid tower (with Li_2^q replacing Φ_q, per the reconciliation finding) for proton + neutron + electron; compute Q_β directly; compare to CODATA. ~1-2 hours.

Phase A's outcome:
- If a complex (u, v) with v ≠ 0 closes both CAL fits with the ANSATZ form, that motivates Phase B.
- If only the real solution closes the ansatz, the +0.17% residual is intrinsic to the ansatz (not Im(q)) and we need Phase B to disambiguate ansatz-vs-tower-function-choice.

## Anti-patterns avoided (skill §11 review)

- ✗ Did not "split the difference" on the bar-involution reconciliation — explicitly updated the Path D audit to acknowledge P_avg/P_skew supersedes generic modulus projection.
- ✗ Did not silently merge `main` — fetched + classified the new commit (`3f653ce8`) as not-affecting-this-PR.
- ✗ Did not add a newly-opened sibling PR to scope without prompting — proposed scope map here; will run by owner if they want to expand it.
- ✗ Did not post a "stream" of comments on #1153 — single consolidated coordination comment.
