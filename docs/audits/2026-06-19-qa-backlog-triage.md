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
