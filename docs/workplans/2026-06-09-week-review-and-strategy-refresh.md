# Workplan: Week-in-review + strategy refresh (2026-06-09)

**Author.** Claude (session resumed after week away)
**Trigger.** User asked: "lots of work in a week — please update workplan after
review of main and siblings for relevant commits and overall strategy."
**Scope.** Refresh strategic prioritization based on origin/main activity
since 2026-06-01 (~150 commits, 8+ merged PRs).
**Status of this doc.** Strategic — points at active ledgers, doesn't
duplicate them.

## Sibling coordination — overlapping strategic workplans (2026-06-09)

This doc was authored in the same ~30-minute window as three other
strategic workplans from sibling Claude sessions:

- **#2034** — `claude/workplan-strategic-review-2026-06-09` — generic
  strategic review post-prior-session; covers Lean v4.24.0 + Option-E
  Phase 2 + α_EM Habiro + sidecar staleness.
- **#2035** — `claude/week-status-workplan-2026-05-31` — cross-axis
  status synthesizing 222 commits + 20 open PRs into 8 strategic axes.
- **#2036** — `claude/qbeta-precision-thread-workplan-2026-06-09` — Q_β
  precision-thread review with α_EM #1521 transferable-bridge findings.

**This doc's distinct contribution:** the **Casimir-axis status
reconciliation** — none of the sibling workplans address the
`ξ_2 = 0` retraction (`2026-05-31-casimir-xi-2-reconciliation.md`) or
explicitly park Casimir behind N_⊙ construction.

**For cross-axis priorities**, defer to #2034 / #2035 / #2036; this
doc's Tier-1..5 list is the **Casimir-axis-aware** view from one
returning session. Where they disagree, the cross-axis PRs win on
breadth; this PR wins on the Casimir specifics.

## TL;DR

- Casimir conjecture (PR #1540) is **merged**, but `ξ_2 = 0` closure was
  **retracted** by [`2026-05-31-casimir-xi-2-reconciliation.md`](../audits/2026-05-31-casimir-xi-2-reconciliation.md).
  Current state: `ξ_0 = 1`, `ξ_odd = 0`, `ξ_{even ≥ 2}` **OPEN**, gated on
  the N_⊙ construction (sub-problem 1). No further flip-flop allowed.
- **Lean v4.24.0 migration is ~80% complete** with residual timeouts in
  numeric witness blocks. The lake-cache/qou-v4-24-0 orphan branch is the
  workaround for the `release.lean-lang.org` egress block.
- **Three foundational pieces of infrastructure landed**: molecular-assembly
  projector (`e_{λ,μ}`), bibliography human-review pipeline, α-cluster
  wire-up (PR #1756 → 7 atoms moved B=0 → α-recursion, mass error 10×
  better).
- **STATUS.md is stale** (last updated 2026-06-01). Two listed active
  sessions completed; the L-goal table is broadly correct but the
  "Active sessions" row needs clearing.

## Themes on main this week (7 clusters)

| # | Theme | Commits | Direction signal |
|---|---|---|---|
| A | Lean v4.24.0 toolchain repairs | ~20 | Migration ~80% done; residual whnf/timeout issues in `Witness12C`, `HeckeEngine`, `PauliWitness A≥8` |
| B | Witness pipeline + proof-rater QA | ~18 | Up-to-scalar narrative alignment for q-casimir uniqueness; build-verify green; Frobenius co-Casimir T4 validated |
| C | Bibliography human-review workflow | 6 | Phase 1 live: `references.review.json` + entryHash + `bib-human-review` criterion + `bib-photo-ingestion-watcher` |
| D | Content reorg + chapter splits | ~25 | Mass-theory / mass-endomorphism / QOU split into sub-sections; 9 orphan blocks rehomed; non-abelian Stokes subsumed into Brings-surface |
| E | Detangler + quark-sector move | ~12 | Quark sector Ch13 → Ch9 (PR #2021); 62 cross-chapter forward-refs remain (~35% closed) |
| F | Molecular-assembly projector + H₂O | ~18 | Foundational infra: `e_{λ,μ}` Wenzl idempotent on Wedderburn blocks; H₂O build active on `claude/h2o-molecular-braid-2026-06-08`; bond orders O₂/N₂/CO predicted + verified |
| G | Mass-sweep wire-up + metallic q-hierarchy | ~16 | α-cluster recursion landed (#1756); 7 atoms moved B=0 → α-recursion; m_err 10× better; metallic-ratio hierarchy machine-checked in Lean |

## Casimir status reconciliation (the flip-flop closed)

Three reversals inside PR #1540 — chronologically:

1. `b1f467f5c`: `ξ_k = 0` via "ε ∝ ℏ_q² cancellation" — **bar-asymmetric calibration, wrong**
2. `ac3fae543`: `ξ_odd = 0` only; `ξ_{even ≥ 2}` open — **correct retraction of #1**
3. `665aa7eb1`: `ξ_k = 0` again via "Casimir doesn't go through Hecke" — **contradicts conjecture block's own framing**, retracted

Final reconciliation ([`2026-05-31-casimir-xi-2-reconciliation.md`](../audits/2026-05-31-casimir-xi-2-reconciliation.md))
settles: `ξ_2` is OPEN and gated on the N_⊙ construction. The "dig-deeper"
witness shows the value depends on **which trace functional N_⊙ realises**:

- Reading 1 (normalized Markov trace of identity): `≡ 1` tautologically (no Casimir-specific content).
- Reading 2 (unnormalized weight sum `Σ y_λ(q)`): n-dependent, h²-coef diverges with n.

Either reading is consistent with the bar-symmetry and tree-level
constraints; **only N_⊙'s construction can pick one**.

**Casimir is OFF the active-work list** until someone wants to construct
N_⊙. Not a blocker for any L-goal. Parked as a clean open problem with
documented invariants.

## Active sibling branches

| Branch | Last commit | Activity | Action |
|---|---|---|---|
| `origin/claude/casimir-conjecture-followup-2026-05-31` | `665aa7eb1 close(casimir): ξ_2 = 0` (stale, retracted upstream) | 9 days idle | **Close / delete**: was merged via PR #1540 + the closure was retracted; no further work |
| `origin/claude/ecstatic-maxwell-CZgQh` | `7b8f67388 qa(proof): figure-eight + q-casimir` | within 7 days | Tracking proof QA; let it run |
| `origin/claude/h2o-molecular-braid-2026-06-08` | active (per agent report) | active | H₂O build in progress; not merged |
| `origin/claude/brave-mendel-FPxFl` (PR #1579) | per STATUS.md (CAL-3 hunt) | 9 days idle | Check if still relevant; STATUS.md table likely stale |
| `origin/claude/coord-infra-1ppq-2026-05-31` | per STATUS.md | 9 days idle | Check status; coord infra was the kickoff phase |

## STATUS.md priorities — current state

From the L-goal table (last updated 2026-06-01, mostly still valid):

| Goal | State |
|---|---|
| L1 (1 ppb compute) | **MET** |
| L2 (per-observable 100×) | 3/7; **m_μ at 209.8 ppb** is the next-largest L2 open problem (per `fe6cfcd0 coord: open m_μ thread`) |
| 1 ppQ — Q_β only | OPEN; c_3 q_0-dependent (NOT Taylor); c_4–c_7 §3b-cond classes locked |
| Δ_λ closure (Option-E) | deuteron CLOSED; A=3 at 0.11% near-match; (1+q)/2 NOT yet derived |
| α_EM canonical | RT Phase 3 + Schwinger; Habiro `[2]_q·(1-h²α)` derived; Bring residue → resolvent landed |
| Q_β c_k flip-flop prevention | enforcement live |
| Lean uniqueness | ~18% witness coverage |
| Mass-sweep gap (A ≥ 4) | α-cluster landed (#1756) → m_err 10× better; A > 12 (32 atoms) gated on H_{3A} kernel |

## Active probes / open workplans worth flagging

From `docs/workplans/` files modified in last 7 days:

| Workplan | Status / next step |
|---|---|
| `2026-06-09-surreal-rescope-execution.md` | 2/2 tasks done — close out |
| `2026-06-09-detangler-axis-handover.md` | 62 actionable forward-refs remain |
| `2026-06-08-h2o-molecular-braid-build.md` | WIP branch — drive to merge |
| `2026-06-08-bib-human-review-workflow-design.md` | Phase 1 live; phase 2 underway |
| `2026-06-05-delta-lambda-sw-residue-qdifference-attack.md` | Formalize-first preflight only; not launched |
| `2026-06-08-zeta5-goncharov-avenue-b-scaffold.md` | Preflight only; depth-3 at ℚ(ζ₅) via Markov-trace |
| `2026-06-04-mass-vol-density-stokes-delta-formalization.md` | Replace VolDensity black box with Mass = Vol × Density + δ from non-abelian Stokes |
| `2026-06-08-optical-fibre-1d-qou-information-theory.md` | 1D quantum channel + photon-propagation remarks |
| `2026-06-08-qa-backlog-proof-braids.md` | 20-block proof-rater batch |
| `2026-06-08-phase-transitions-h2o-knot-hierarchy.md` | Phase transitions + H₂O + knot-symmetry survey |

## Recommended priority order (next session)

Tiered by L2 impact + tractability:

### Tier 1 — biggest L2 gap closure

1. **m_μ 100× gap** (209.8 ppb, the next-largest L2 open problem after the 2026-05-28 re-pin). Independent μ–p floor, not the Q_β chain. Per `fe6cfcd0 coord: open m_μ thread`, a coord thread was opened but I haven't read it. **First action**: read [`docs/coordination/`](../coordination/) for `m_mu` ledger if it exists, otherwise check the coord commit's full message.

### Tier 2 — Lean migration cleanup

2. **Residual v4.24.0 timeouts**: `Witness12C`, `HeckeEngine`, `PauliWitness A≥8`. Per recent commits (`8424d7db7`, `0111d438b`), these have foldr-over-list refactors landed but the underlying whnf heartbeat issue may surface again on larger probes. **First action**: skim those files to see if any new timeouts have surfaced.

### Tier 3 — finish open infrastructure

3. **Detangler 62 forward-refs**: continue cross-chapter edge closure per [`2026-06-09-detangler-axis-handover.md`](2026-06-09-detangler-axis-handover.md).
4. **H₂O molecular-braid build**: drive `claude/h2o-molecular-braid-2026-06-08` to merge.
5. **Mass-formalization**: execute [`2026-06-04-mass-vol-density-stokes-delta-formalization.md`](2026-06-04-mass-vol-density-stokes-delta-formalization.md) statements-first.

### Tier 4 — research-grade open

6. Δ_λ step-9b SW/q-difference attack — formalize-first preflight done; needs a concrete launch decision.
7. ζ₅ Goncharov depth-3 via Markov-trace — preflight only.
8. Mass-sweep A > 12 gated on H_{3A} kernel — major dependency.

### Tier 5 — parked

9. **Casimir conjecture sub-problems 1 + 4 (ξ_2)**: parked behind N_⊙ construction. Not blocking any L-goal. Touch only if a tractable angle appears.

## STATUS.md housekeeping recommendation

The "Active sessions" table needs a refresh:

- `claude/coord-infra-1ppq-2026-05-31` (Claude, 2026-05-31) — should be **completed**.
- `claude/brave-mendel-FPxFl` (PR #1579) (Claude, 2026-05-31) — check whether CAL-3 hunt resolved.

Also the "Last updated" stamp should bump from 2026-06-01 to 2026-06-09 once
this workplan lands. (Doing that as a separate small edit is the right
size.)

## Sibling branch cleanup recommendation

`claude/casimir-conjecture-followup-2026-05-31`: PR #1540 merged, follow-up
audit landed on main (`2026-05-31-casimir-xi-2-reconciliation.md`). Branch
can be deleted from origin to reduce noise in the coordinate-sweep output.

Same for any other stale `claude/*` branches whose PRs are merged + the
follow-up is on main.

## Honest meta-note

A week off-branch means I missed a lot of context. The triage agent's
report (saved in subagent transcript) is the source of truth for "what
landed". This workplan condenses + prioritises. It does NOT try to
unilaterally close goals or pick a specific Tier-1 task — that's the
author's call.

**Recommended first author decision:** pick which Tier-1/Tier-2 path
gets the next session. m_μ is the largest open L2 gap; Lean cleanup is
lower-cost; detangler is incremental.
