# QA Idle-Backlog Triage — 2026-06-19

**Context.** An idle-backlog drain was requested this session (branch
`claude/affectionate-keller-x9xzv4`). A read-only triage agent plus
foreground verification surveyed stale QA sidecars (`*.qa.json`) and
compute witnesses (`computations/*.witness.json`). This doc records the
**verified** findings, because the backlog turned out to be *blocked* on
one axis and *potentially substantive* on the other — not a safe blind
chore. The two load-bearing claims below (tooling absent; one witness
drift) were re-verified in the foreground; the bulk counts come from the
triage agent's `sha256` + `git` scan and are labelled as such.

## Finding 1 (BLOCKER) — sidecar-refresh tooling is absent from `main`

CLAUDE.md §idle-policy item 4 and the `/integration-audit` /
`/integration-watch` skills refresh stale sidecars via
`bun run content/pipeline/qa-sweep.ts <path> --only <crit>` and detect
staleness via `content/pipeline/qa-staleness.ts`. **Neither script is on
`main`:**

```
$ git ls-files | grep -iE 'qa-sweep|qa-staleness'    # (empty)
$ git ls-files content/pipeline/
content/pipeline/lean-vacuity-axiom-audit.ts
content/pipeline/qa-agent-drain-queue.ts
```

The triage agent located them only on an unmerged review branch
(`530cf7b3`). **Consequence:** the sidecar half of the backlog cannot be
drained as documented; any agent routed to "refresh stale sidecars" will
dead-end here.

**Recommendation:** either land `qa-sweep.ts` / `qa-staleness.ts` (and
their `schemas/block-qa.ts` producers) on `main`, or correct CLAUDE.md
§idle-policy item 4 and the skill-routing table to reflect the actual
pipeline location. Until then, the sidecar-refresh idle item should be
treated as blocked.

> Note: the repo layout has drifted from several CLAUDE.md paths —
> `schemas/lean-packages.ts` is now at repo root (doc says
> `folio-assistant/schemas/`), and `content/package.json` still defines
> `migrate-lean-refs[:dry]` pointing at a now-deleted
> `pipeline/migrate-lean-refs.ts`. Low priority, but same doc-currency
> class as Finding 1.

### Sidecar staleness scale (triage scan; pure `sha256` + `git`, no `bun`)

- 443 / 2266 `*.qa.json` with `source_hashes.{md,ts,lean}` drift
- 8 with reviewer `script_hash` drift — all criterion
  `proof-no-self-assuming-projection` (reviewer
  `content/pipeline/lean-vacuity-axiom-audit.ts`, hash
  `bbdd1b3cd73d → 3d6da1d6f221`); a single re-sweep of that one
  criterion fixes the set
- ~12 orphaned (sibling block deleted/renamed, `.qa.json` left behind) —
  needs a human deletion decision, not a sweep

## Finding 2 — 739 / 777 witnesses stale; root cause = 2026-06-17 producer touch

A sweeping 2026-06-17 workplan commit touched many `computations/*.py`
producers without regenerating their witnesses. Verified spot-check
(`atomic-tr-m-helium4-canonical`):

| field | witness | producer (current) |
|---|---|---|
| `scriptCommitSha` | `782c44d5` (2026-05-25) | `ad8bfc54` (2026-06-17) |
| `scriptHash` | `22f4488cc097` | `e62cc6ada70a` |

**Caveat — this is NOT a blind chore.** The top stale witnesses are
canonical mass / `tr_M` producers (`markov_peel.tr_M_atomic`, A ≥ 4 ⇒
> 5-min compute each). Re-running them may change **paper numbers**, not
just provenance fields, which would require:

- re-running both precision dashboards (`onepb-status-dashboard`,
  `per-observable-100x-status`) and reporting the deltas
  (CLAUDE.md §Precision goals); and
- the mass/binding appendix sync (CLAUDE.md §Mass-and-Binding-Algorithms
  appendix).

So a **value-drift probe on one canonical witness** should precede any
batch refresh — if only provenance changed, the fix is hygiene; if values
changed, it is a substantive correction with downstream obligations.

### Top-3 witness queue (per CLAUDE.md ≤ 3 / idle pass)

1. `computations/atomic-tr-m-helium4-canonical.witness.json`
   ← `computations/atomic_tr_m_helium4_canonical.py`
2. `computations/applied-uniqueness-mass-table.witness.json`
   ← `computations/applied_uniqueness_mass_table.py`
3. `computations/atom-mass-derived.witness.json`
   ← `computations/atom_mass_derived.py`

Re-run discipline (long-compute logging):
`python3 -u <producer> 2>&1 | tee /tmp/<name>.log`.

## Net

- **Sidecar drain: blocked** — refresh tooling is not on `main`
  (Finding 1).
- **Witness drain: executable but substantive + large** — needs an owner
  decision on scope (single value-drift probe vs. batch refresh) before
  burning compute or committing mass-value changes.

## Update (2026-06-19, later) — one root cause; cross-references; probe result

A sweep of in-flight QA PRs shows both backlog axes trace to **one root
cause** and are already partly characterized — so manual nibbling is the
wrong instrument.

- **Root cause: the witness-pipeline / QA CI is billing-blocked.** The CI
  step that would auto-regenerate witnesses and re-sweep sidecars fails in
  ~3 s on every PR (the documented GitHub-Actions billing outage,
  CLAUDE.md §"CI billing failures"). Both axes drift with nothing to
  refresh them; no manual cadence keeps up.

- **Witness drift splits into TWO classes — only one is benign.**
  - *Class 1 (2026-06-05) — benign,* verified by
    [PR #1878](https://github.com/litlfred/qou/pull/1878): a detector
    hashing producers as `WitnessBuilder` does found ~681/1022 witnesses
    with `scriptHash` drift; re-running showed the change is a
    `precisionMetadata` default bump (`65/50/15 → 70/60/10`) + a new
    `environment` block — schema/config, **not** math (data unchanged or
    sub-assertion-threshold). Hazard (from #1878): several mass producers
    (`d_from_scratch`, `b_over_a_evaluator`, `probe_1b_li6_orthogonality`)
    fail/time-out on re-run yet write *partial* witnesses — never commit
    those. Audit: `docs/audits/2026-06-05-witness-metadata-drift-audit.md`.
  - *Class 2 (2026-06-17 workplan touch) — SUBSTANTIVE,* shown this session
    by building `pyhecke-native` 0.9.0 (`maturin build --release`, 39 s) and
    re-running `atomic_tr_m_helium4_canonical.py` with the real kernel. The
    `tau` values **changed at the 8th significant figure**:
    `tau_p 1.220362889·0866930 → ·1122446`, `tau_n 1.194862425772554 →
    ·799856`, `tau_4he 0.1538719675·41095 → ·51499` — Δ ≈ **2–7×10⁻⁸
    relative**, far above the 10⁻¹⁵ compute floor (not precision
    truncation), plus a new `lean_uniqueness_ref` field and a 15×
    H₃-baseline slowdown (0.31 s → 4.8 s). The producer was **created** in
    the big 2026-06-18 commit `ad8bfc54` ("brick 2 … n=3 minimality
    Lean-proved"; 1236 insertions across producer + `closed_form_tau_M` +
    `hecke_characters`), so the committed witness (2026-05-25) predates it
    and carries **stale values**. Assertions pass only because tolerance is
    0.1. **The regenerated witness was NOT committed** — a mass-value change
    needs owner review (is `ad8bfc54` canonical or WIP?) + dashboard reruns
    + appendix sync (CLAUDE.md §Precision goals). The other 06-17-touched
    witnesses may carry the same substantive class.

- **Sidecar tooling is a subsystem, not 2 files (Finding 1, refined).**
  `qa-staleness.ts` imports `./qa-utils` (`hashBlockFiles`, `walkBlocks`,
  `loadQaReport`, `summariseFreshness`) + `./qa-criteria-registry`
  (criterion registry + per-axis watcher lists); `qa-sweep.ts` additionally
  pulls the criterion checkers, the rater-rubric framework (#1939), and
  `schemas/block-qa.ts`. Landing it is a subsystem port, and
  [PR #1928](https://github.com/litlfred/qou/pull/1928) shows the refresh
  is "red by design" (surfaces 17 pre-existing criticals). The tooling is
  entangled across stale/conflicted PRs — #1928 (469 files, base 900+
  commits behind) and [#2187](https://github.com/litlfred/qou/pull/2187)
  (supersedes #1918/#1941; notes 933-commit / 2147-`.qa.json` drift) — so
  it cannot be landed unilaterally without stepping on in-flight work.

### Recommended owner decision

1. **Restore Actions billing** — the single fix that lets CI auto-regen
   both axes; everything else is symptomatic nibbling.
2. **Or designate one canonical QA-tooling PR** to land the `qa-*.ts`
   subsystem (with the 17 criticals triaged), superseding the stale ones,
   rather than re-deriving on a fresh branch.

Sidecar sweeps below the CI fix are low-leverage. Witness re-runs are
**not** uniformly benign: Class-1 (06-05) is, but Class-2 (06-17 producer
touches) carries substantive 2–7×10⁻⁸ value drift (helium4 kernel-verified
this session) and needs owner review before any batch refresh.
