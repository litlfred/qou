# Overall strategy update — 2026-06-09

**Status:** Active strategy document. Supersedes the older workplans listed below.
**Branch / PR:** `claude/overall-strategy-update-2026-06-09` (PR #TBD)
**Coverage window:** ~2,481 commits to `main` over the past 7 days; 4 sessions worth of in-flight PRs.

This document consolidates the per-area workplans from the past week + the strategic shifts visible in main's commit log + open PR activity. Treat it as the **single source of truth** for the next session's work-tranche planning.

## Superseded workplans

The following workplan documents are superseded by this strategy doc. They remain on-disk for historical reference but **agents should consult this document first** for "what's next" routing:

| File | Status | Subsumed scope |
|---|---|---|
| `docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md` | ✅ **DONE** (Sprints 1-5 all merged) | Phase 2 IwahoriHecke infra |
| `docs/workplans/2026-05-30-source-conjecture-closure-plan.md` | ⚠ **partially superseded** (6 closures landed; remaining: Tier-B continued) | Conjecture-closure campaign |
| `docs/workplans/2026-05-30-mathlib-upstream-tracker.md` | ⚠ **still active** (Lean v4.24.0 work folds in) | Mathlib upstream tracking |
| `docs/workplans/2026-05-31-real-sdp-wiring-per-nucleus.md` | ⚠ **active** — folded into Phase 1 below | Per-nucleus real-SDP wiring |
| `docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md` | ⚠ **active** — folded into Phase 4 below | Witness-side `lean_uniqueness_ref` campaign |

## Week-in-review (2,481 commits)

### Top themes

| Theme | Commits | What |
|---|---:|---|
| `qa` | 1,107 | self-emitting per-block audits (qa-sweep.ts running constantly) |
| `review` | 211 | Copilot + Gemini review fixes |
| `fix` | 173 | mostly Lean v4.24.0 migration (`λ→lam`, imports, heartbeats) |
| `probe` | 88 | exploratory probes (mostly α_EM / Q_β / option-e Δ_λ) |
| `audit` | 75 | new audit scripts + ledgers |
| `lean` | 72 | Lean structural work (Iwahori sprints, Hoefsmit, etc.) |
| `docs` | 69 | workplan + audit doc updates |
| `content` | 45 | content block additions / kind cascades |
| `phase` | 21 | Phase 1/2 IwahoriHecke milestones |

### Strategic shifts visible in the week

1. **Lean v4.24.0 migration is essentially done.** Most-recent ~40 main commits are reserved-keyword (`λ→lam`), `maxRecDepth/maxHeartbeats` tuning, import-set repair, and 1-by-1 file fixes across `MarkovTrace`, `Wedderburn`, `HeckeRep`, `ShellNeutrality`, `BringShellBinding`, `EmCoupling`, `HeckeEngine`, `BringShellBinding`, etc. Baseline is now stable.

2. **Iwahori-Hecke Sprints 1-5 all merged** (#1506, #1512, #1518, #1524, #1525). The `IsHeckeAlgebraMap`, `Quotient`, `TypeA`, `MarkovTrace`, `Hoefsmit`, `Tw` modules are on main. **6 Tier-A/B conjectures closed**: `conj:pontryagin-dual-coxeter-character`, `conj:averaging-resonance-rule`, `conj:hecke-anyonic-substrate`, `conj:reverse-limit-q-to-infinity`, `conj:gs-graded-markov-trace-existence`, `conj:hoefsmit-ew-cell-content`.

3. **Q_β c_k saga closing** — 4 flip-flop rounds collapsed into a "truncation-order canonical framing" (commits `6ace8153e`, `7f02c22e4`, `9e45f6d48`). The c_k coefficients are now framed as truncation-order, not stale-q₀ artifacts. `CLAUDE.md` got a "read first" note. **Discipline lesson**: framing matters; future agents should not re-litigate.

4. **Atom-braid extension** to ⁶Li/⁹Be/¹¹B verified cases via Sprint 2 atom-braid extension.

5. **SDP-uniqueness infrastructure** (my session's 17 PRs): meson m_K/m_π wire, SnapPy migration, parameterised SDP-uniqueness covering 12,804 isotopes, atlas wiring, AtomicMass refactor sweep, 30 producer scripts wired with `lean_uniqueness_ref`, CI audit step.

6. **Bib-human-review pipeline phase 1-2** — `references.review.json` status model, audit script, issue template, `bib-photo-ingestion-watcher` skill. New workflow track; not in my scope but worth coordinating.

7. **Option-e mirror-pair breakthrough** — v8/v9 commits close mirror pair to 0.11% (cheat-sheet's "2% claim" essentially found). Material for the Δ_λ closure path.

8. **α_EM self-consistent fixed-point solve** — most-recent commit (`629d8d265`) achieves α to 0.31 ppb = 2.09× σ_α. Significant for the α_EM closure track.

## Phased forward plan

### Phase 0 — baseline confirmation (1 PR, ~2 hours)

Re-establish ground truth after the week of v4.24.0 repair + 14 merged session PRs:

- Re-run sorry-count audit (last baseline was 50 sorries; v4.24.0 work likely changed it)
- Re-run `audit_lean_uniqueness_ref_wiring.py` for post-merge coverage of #1572 (was ~18%)
- Re-run `conjectural-propagation-audit.ts` (last refresh was #1541 at 1,868 blocks; expected ~1,900+)
- Re-run `per_observable_100x_status.py` (Q_β truncation-order canonical framing should affect numbers)

### Phase 1 — real per-nucleus SDP wiring (multi-PR, ~7 weeks for 7 light nuclei)

Per `docs/workplans/2026-05-31-real-sdp-wiring-per-nucleus.md` (folded into this strategy):

Drop the abstract empty-constraint SDP layer (which is already merged + sorry-free across 12,804 isotopes) and wire the **real** per-nucleus SDP with multi-term cost from the mass formula + non-empty constraints from quark composition.

**Order**:
1. **Deuteron** (²H, A=2, n=6) — smallest case, Hoefsmit-H_3 already available
2. **³He** (Z=2, A=3, n=9) — already partially wired via `_unique_of_dualSlack_posDef`
3. **⁴He** (Z=2, A=4, n=12) — multi-term cost from atom-braid Sprint 2
4. **Tritium** (³H, A=3, n=9) — gated on Hoefsmit-H_5 (Sprint 5 partial)
5. **⁶Li, ⁹Be, ¹¹B** — Sprint 2 extension nuclei

**Per-nucleus phases** (Phase A-D from #1575):
- A. Cost matrix structural (1-2 days)
- B. Constraints (1 day)
- C. Strong-duality witness — SDP solve + dualSlack PosDef check (1-2 days)
- D. Lean wiring — replace `_emptySDP` with `_realSDP` (1 day)

### Phase 2 — Q_β k=3 closure (multi-PR, ~1-2 weeks)

The L2 audit found that 3 failing observables (Q_β, m_n, Δ_pn) all share ONE structural input: the τ_M Kashiwara derivation of Q_β truncated at k=2. Closing k=3 closes all three.

**Approach**: Option E (Kashiwara crystal extension to k ≥ 3 with canonical non-fitted rung-selection rule).

**Gating**:
- Phase 2 IwahoriHecke `Hoefsmit.lean` provides the basis (landed)
- Cell-content recurrence is the open math
- Connect to `option-e v3/v4/v5/v6/v7/v8/v9` probe series on main (v8/v9 = mirror-pair closure to 0.11%, in flight)

**Discipline guard** (from the c_k flip-flop saga): any c_k / d_k claim must use the truncation-order canonical framing per `CLAUDE.md`'s "read first" note. Future agents must not re-litigate the c_3 form.

### Phase 3 — completion of the witness wiring campaign (mechanical, ~5-10 PRs)

Per `docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md`:

- Current coverage: ~30/163 producers (~18%) after #1572
- Remaining: ~127 per-nucleus producers + ~20 atom-binding probes
- Mechanism: bulk wiring helper (proven pattern from #1572)
- CI audit (#1573, warn-only) flips to `--strict` once coverage > 80%

### Phase 4 — α_EM precision push to CAL-2 floor (multi-PR, indefinite)

The most-recent main commit (`629d8d265`) reports α to **0.31 ppb = 2.09× σ_α**. Per the precision goals in `CLAUDE.md`:

- CAL-2 anchor σ_α ≈ 0.15 ppb → α_EM should close to ≤ 0.0015 ppb for 100× target
- Current 0.31 ppb is 2× σ_α; needs ~200× further closure
- Path: RT 2-loop derivation roadmap (#1487 + #1495 + #1508 + #1521 + #1527 + #1538)
- This is a multi-PR campaign; each phase 1-6 from #1495 is its own work unit

### Phase 5 — extend AtomicMass parameterisation pattern (1 PR)

Per #1568 (AtomicMass full sweep merged): the parameterisation pattern can be applied to other duplicated proof patterns in the codebase. Audit Opportunity 4 from `docs/audits/2026-05-30-parameterisation-opportunities.md`:

- Per-knot Hecke-character closed forms across `BraidKnot/`
- Per-isotope binding-energy chains
- Per-nucleus mass-formula assembly

Each is its own focused refactor PR.

## Cross-cutting principles (new for 2026-06-09)

### Discipline guards added since 2026-05-30

1. **Truncation-order canonical framing** for any c_k / d_k claim (per the Q_β saga). Future agents must read `CLAUDE.md`'s "read first" note before re-litigating.

2. **No `λ` as a binder name** (Lean v4.24.0 reserved keyword). All new Lean code must use `lam` for partition-index binders. Existing repair pattern at #1525-and-prior shows the migration.

3. **`maxRecDepth` / `maxHeartbeats` budget** — large PauliWitness files (A ≥ 8) need explicit `set_option`. Pattern landed in `002024f59`.

4. **§3b-cond lean-stub-kind-check** rule landed in `validate` (commit `efb3b04df`). Provable-kind blocks downstream of conjectures must be `conjecture` per §3b-cond.

### Coordination with sibling tracks

The session generating this workplan operates alongside:

- **Bib-human-review pipeline** (#2011 + #2024 + Phase 1/2 watcher work) — not in scope; cross-link when bibliographic references in workplans need refresh
- **α_EM precision push** (multi-PR thread #1444 onwards) — coordinate when SDP-uniqueness or Q_β work touches α_EM derivation
- **Option-e Δ_λ probe campaign** (v1-v9, mirror-pair breakthroughs) — Phase 2 above depends on this landing

## What's NOT in scope

- Substantive new math (each Phase 1/2/4 step is itself a research-grade effort; this document organises the work, doesn't do the research)
- Lean Mathlib upstream contributions (tracked separately in `mathlib-upstream-tracker.md`)
- Paper rendering / PDF build improvements (separate publish.yml track)

## Active session PRs awaiting merge

| PR | Theme | Status |
|---|---|---|
| #1568 | AtomicMass complete sweep (115 elements) | open |
| #1572 | Bulk witness wiring (~18% coverage) | open |
| #1573 | CI audit warn-only step | open |
| #1575 | Real-SDP wiring workplan (folded into Phase 1 above) | open |
| **#TBD** | **This strategy update** | **opening now** |

After this strategy doc lands, the four-PR backlog should merge in dependency order: #1568 → #1572 → #1573 → #1575.

## Cross-references

- `CLAUDE.md` — Q_β c_k "read first" note (added this week)
- `docs/coordination/2026-05-30-sdp-uniqueness-status.md` — SDP uniqueness layer status
- `docs/audits/2026-05-30-parameterisation-opportunities.md` — refactor opportunities ledger
- `docs/audits/2026-05-30-conjecture-closure-session-audit.md` — conjecture-closure findings
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md` — Q_β shared-root-cause analysis
- `docs/precision-goals.md` — L1 / L2 targets

## Maintenance

This document is the **active** strategy. When updating:

1. Update the per-phase status as PRs land
2. Add new strategic shifts in "Week-in-review" sections (or open a new strategy doc dated forward)
3. Mark older strategy docs as superseded with banner pointing to this doc
4. Don't delete superseded workplans — keep for historical reference
