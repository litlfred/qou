# Canonical-watcher baseline audit — 2026-05-18

**Branch:** `claude/canonical-watcher-skill-UaWnQ` (PR [#694](https://github.com/litlfred/qou/pull/694))
**Anchored to:** `prop:three-calibration-inputs` + `prop:three-calibration-discipline` + the framework's "exactly three calibration inputs" rule (CAL-1 $m_e$, CAL-2 $m_\mu/m_e \to q_0$, CAL-3 $Q_\beta(n)$).

Baseline state of the canonical-derivation discipline across the
codebase at the time the watcher armed, plus a comprehensive
working queue. Cross-references the existing aggregator
([`canonical-derivation-pipeline-compliance.witness.json`](../../folio-assistant/computations/canonical-derivation-pipeline-compliance.witness.json))
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

## 4  Content-level marker sweep (candidate findings — *needs per-file verification*)

Brute grep for canonical-discipline marker words in `content/**/*.md`. Each hit is a **candidate**, not a confirmed violation — many uses of "approx" / "calibrated" are legitimate (e.g. inside math, referring to CAL-1/2/3, citing PDG provenance).

### 4a  "ad hoc" / "fit to AME/CODATA/PDG" / "tuned" / "approx" / "justification" / "numerolog" markers

20 candidate files (all under `content/quantum-observable-universe/braids-and-knots/`):

```
force-carrier-intertwining-correspondence.md
np-discrepancy-resolution.md
qmn-recursive-memoized.md
atom-knot-mass-derivation.md
gs-archimedean-agreement-residue.md
unified-curvature-rank-mass-formula.md
jet-filtered-knot-factor.md
binding-knots-visual-inventory.md
hoefsmit-scattering-pipeline.md
per-braid-mass-tower.md
figure-8-archimedean-illustration.md
knot-operator-lp-selection.md
recomputed-low-isotope-mass-table.md       ← KNOWN: † tautology-banner per docs/audits/2026-05-11-three-calibration-discipline-violations.md
cl3-zeta5-pslq-independence.md
alpha-em-categorical-trace.md
y-lambda-closed-form-wenzl-bridge.md
hook-weight-derivation.md
atomic-mass-gb-nf.md
categorical-chain-convergence-mechanisms.md
eigenvalue-product-expansion.md
```

**Triage status:** **per-file verification queued.** Methodology: open each `.md`, locate the marker, classify as (i) legitimate (math context / CAL provenance / cited TODO), (ii) Class-A opt-out (acknowledged-stub with banner), or (iii) genuine discipline violation needing escalation.

### 4b  Archimedean-leak candidates (algebraic-side uses of `Vol(K)` / hyperbolic / Mostow)

20 candidate files mention `Vol(...)`, hyperbolic, or Mostow. Many are legitimate (Descartes elliptic curve chapter, Bring's surface, the explicit Vol(4_1)/(m_μ/m_e) → q_0 CAL-2 definition, the Kashaev volume conjecture context). **Per-file verification queued.** The audit rule (per `three-calibration-discipline.md §4`): an archimedean input is forbidden *only* in an algebraic-side derivation; cross-domain comparison is honest.

### 4c  "Three-route convergence" / "universal extrapolation" patterns

Zero hits from the grep — either the patterns don't exist in content, or they're phrased differently. Lower priority for the manual sweep.

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
