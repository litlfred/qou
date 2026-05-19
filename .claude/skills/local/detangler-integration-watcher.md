---
name: detangler-integration-watcher
roles: [reader, collaborator, owner]
user_invocable: true
inherits: local/integration-watcher
description: >
  Structural-QA integration watcher — watches origin/main + open
  active PRs + newly-opened PRs for organisational changes (paper /
  chapter manifest edits, new blocks, edited `uses[]` / `kind` /
  `label` / `interprets` / `defines` / `tags`, block renames) and
  runs the editor's detanglement skill suite (`content-graph` H1-H7,
  `chapter-complexity-review` graph energy, `block-density-audit`
  R1-R3, `critical-path-analysis` chains) on every detected change.
  Queues findings, auto-discharges mechanical fixes (intra-section
  swap, table extraction R3), escalates section splits / merges /
  cross-chapter moves / new sections to the author. Inherits shared
  mechanics (Monitor, subscriptions, queue, ledger, idle sweep,
  author-ask, watch-prepared-PRs, witness-drift recovery,
  billing-quick-fail flake, post-completion one-voice, sibling-PR
  comment protocol) from `local/integration-watcher`.
allowed-tools: Read Edit Write Bash Grep Glob Agent Monitor Skill
---

# /detangler-integration-watcher

A concrete instance of [`local/integration-watcher`](integration-watcher.md).
The parent encodes the shared mechanics. This file fills the nine
domain-specific slots A–I.

**Setup:** use `NAME=detangler-integration-watcher` everywhere the
parent's §1 references `${NAME}`. Files land at
`todos/detangler-integration-watcher-queue.json` and
`todos/detangler-integration-watcher-ledger.md`.

**Additional baseline cache.** Beyond the parent's §1 setup, this
watcher caches a graph baseline so per-event deltas are comparable:

```bash
( cd content && python3 pipeline/content-graph-analysis.py --json ) \
  > /tmp/_detangler_watcher_graph_baseline.json 2>/dev/null
```

Refresh the baseline after a clean event by overwriting with the
post-event snapshot (see Slot D).

## Slot A — Goal statement

Zero new forward references on landing commits (**excluding refs
sourced from `intro` / `notation` chapters — see §Preview-chapter
exclusion below**), no section pushed out of the 3–18 block band,
no new cross-chapter forward edges, no new topic-mixed blocks, and
`docs/reorganization-map.md` updated alongside every move. The
section graph trends toward lower energy. Forward edges that exist
for architectural reasons (the archimedean wall in
[`models-of-qous/sec:archimedean-models`](../../content/quantum-observable-universe/models-of-qous/),
deliberate cross-chapter callbacks) are accepted and recorded as
`wontfix: architectural`.

### Preview-chapter exclusion (STRICT)

Forward references whose **source** lives in a *preview chapter*
are info-only — never findings, never invariant violations,
never auto-discharge targets. Preview chapters preview future
material (intro motivates the paper) or are reference lookups
(notation is a symbol index); forward refs from them are the
expected reading pattern.

The preview list is hard-coded in this watcher (not yet a
content-schema field):

```python
PREVIEW_CHAPTERS = {'introduction', 'notation'}
```

When filtering H1 / H2 findings from `content-graph-analysis.py`,
**drop any finding whose source block's `chapter_dir` is in
`PREVIEW_CHAPTERS`**. Apply this filter in Slot B (event trigger
delta), Slot C (graph-delta synthesis), Slot D (taxonomy), and
Slot I (invariants).

### Archimedean wall awareness

The paper's structural cut is the archimedean wall: pre-wall
content uses generic `{R : Type*}` (categorical, q-deformed,
combinatorial); post-wall content specialises to `ℝ` for numerical
evaluation. The wall is implemented as the
**`models-of-qous/sec:archimedean-models`** section, which contains
the canonical bridge constructions (Calabi-Yau, ALE, Seiberg-Witten,
Brings-surface archimedean specialisation, categorical-action ↔
Chern-Simons).

In the paper's reading order, the wall **must** sit between
`braids-and-knots` (last pre-wall chapter) and `descartes-universe`
(first post-wall chapter). Forward edges crossing the wall in the
wrong direction (post-wall → pre-wall categorical content silently)
are a finding (`archimedean-wall-violation`, minor) unless the
target block carries `tags: ['archimedean-bridge']` or an explicit
banner. See Slot D.

## Slot B — §3 trigger filter

For a `MAIN <sha> <msg>` line (or PR commit event):

```bash
SHA=<event sha>
# -M enables rename detection so block renames (one of this skill's
# stated triggers) show up as R-status entries instead of silent
# add/delete pairs.
changed=$(git diff-tree -M --no-commit-id --name-only -r "$SHA")

is_struct_event=false

# B.1 — Paper manifest OR nested chapter manifest. Both define
# ordering. Paper manifests live at content/<paper>/<paper>.ts;
# chapter manifests live at content/<paper>/<chapter>/<chapter>.ts.
echo "$changed" | grep -qE 'content/[^/]+/([^/]+\.ts|[^/]+/[^/]+\.ts)$' \
  && is_struct_event=true

# B.2 — Block manifest edits that touch graph-topology fields.
# The fields below are the ones content-graph-analysis.py reads.
for ts in $(echo "$changed" | grep -E 'content/.*\.ts$'); do
  [ -f "$ts" ] || continue
  if git show "$SHA" -- "$ts" 2>/dev/null \
       | grep -qE '^[+-][[:space:]]*(uses:|interprets:|proofs:|examples:|kind:|label:|defines:|tags:)'; then
    is_struct_event=true
    break
  fi
done

# B.3 — New blocks (A-status .ts files under content/)
git diff-tree -M --no-commit-id --diff-filter=A --name-only -r "$SHA" \
  | grep -qE 'content/.*\.ts$' && is_struct_event=true

# B.4 — Block renames (R-status — requires -M above)
git diff-tree -M --no-commit-id --diff-filter=R --name-only -r "$SHA" \
  | grep -qE 'content/' && is_struct_event=true

# B.5 — Reorganisation-map staleness: a structural change above with
# `docs/reorganization-map.md` NOT in the same commit. The map
# staleness is itself a finding (see Slot D `reorg-map-stale`), not
# a skip condition — still run the pipeline.
if [ "$is_struct_event" = true ] \
   && ! echo "$changed" | grep -q '^docs/reorganization-map.md$'; then
  reorg_map_stale=true
fi
```

For PR review-comment events, pass through if the comment body
mentions: `forward ref`, `section`, `reorder`, `split`, `merge`,
`move`, `topic`, `dense`, `sparse`, OR cites a content block label.

## Slot C — §4b dispatch table

| Specialist | When to run | What it checks |
|------------|-------------|----------------|
| `content-graph` (`python3 pipeline/content-graph-analysis.py --json` + `--proposals`) | **Always** | H1–H7 heuristics, split / merge / move / reverse proposals for the affected scope |
| `chapter-complexity-review` | Whenever a chapter manifest changed, OR ≥ 1 block's `uses[]` changed inside a single chapter | Graph energy delta + optimal section ordering |
| `block-density` (`python3 pipeline/block-density-audit.py <paper-dir>`) | Whenever a block `.md` was edited, added, or renamed | R1 (single topic), R2 (≤ 40 lines), R3 (embedded tables > 5 rows) |
| `critical-path-analysis` | Whenever a `definition` / `theorem` / `lemma` / `proposition` / `corollary` block's `uses[]` changed | Whether the change breaks a logical chain |
| `content-validation` (`cd content && bun run validate`) | Always | Schema constraint rules (`uses-resolve`, `remark-interprets`, `defterm-declared`, …) |

Launch the parallel calls in a single response with multiple `Agent`
tool uses (NOT sequentially). Cap each agent's report at ~400 words.

**Graph-delta synthesis (after dispatch).** Compute the delta
against the cached baseline. Derive metrics from the `findings[]`
array exported by `content-graph-analysis.py --json` (the script
does **not** export summary scalars like `forward_refs_count` — they
must be counted from the findings list):

```bash
# Snapshot post-event graph (run from repo root, not from content/)
( cd content && python3 pipeline/content-graph-analysis.py --json ) \
  > /tmp/_detangler_watcher_graph_current.json 2>/dev/null

python3 <<'PY'
import json
b = json.load(open('/tmp/_detangler_watcher_graph_baseline.json'))
c = json.load(open('/tmp/_detangler_watcher_graph_current.json'))

def summarise(g):
    f = g.get('findings', [])
    h1 = [x for x in f if x['heuristic'] == 'H1']
    h2 = [x for x in f if x['heuristic'] == 'H2']
    h4 = [x for x in f if x['heuristic'] == 'H4']
    h5 = [x for x in f if x['heuristic'] == 'H5']
    # Section sizes derived from chapters[].sections[].blocks[]
    sizes = {}
    for ch in g.get('chapters', []):
        for s in ch.get('sections', []):
            sizes[s['label']] = len(s.get('blocks', []))
    return dict(forward_refs=len(h1), cross_chapter_fwd=len(h2),
                sparse_sections=len(h4), dense_sections=len(h5),
                section_sizes=sizes)

bs, cs = summarise(b), summarise(c)
print(f"forward_refs: {bs['forward_refs']} -> {cs['forward_refs']}")
print(f"cross_chapter_fwd: {bs['cross_chapter_fwd']} -> {cs['cross_chapter_fwd']}")
print(f"sparse: {bs['sparse_sections']} -> {cs['sparse_sections']}")
print(f"dense: {bs['dense_sections']} -> {cs['dense_sections']}")
for sec, n in cs['section_sizes'].items():
    bn = bs['section_sizes'].get(sec, n)
    if (3 <= bn <= 18) and not (3 <= n <= 18):
        print(f"section-band-violation: {sec} {bn}->{n}")
PY
```

If the event is clean (no regressions), promote the snapshot to
baseline:

```bash
mv /tmp/_detangler_watcher_graph_current.json \
   /tmp/_detangler_watcher_graph_baseline.json
```

## Slot D — §4c finding taxonomy

| Finding | Severity | Description |
|---------|----------|-------------|
| `uses-resolve-broken` | critical | `uses[]` cites a missing target (schema constraint failure) |
| `critical-path-break` | critical | Moved / removed block broke a logical chain reaching a downstream `theorem`/`proposition` (per `critical-path-analysis`) |
| `cross-chapter-forward` | critical | New forward cross-chapter edge to a non-existent block, OR a new H2 forward edge crossing the categorical/archimedean wall in an unintended direction (per PR4) |
| `defterm-undeclared` | critical | New `:refterm`/`\refterm` with no matching `defines` declaration (per CLAUDE.md §4c) |
| `forward-ref` | major | New H1 forward reference (block A uses block B, B appears later) — span > 3 OR cross-section |
| `dense-section` | major | Section pushed > 18 blocks by this commit (H5) |
| `sparse-section` | major | Section dropped below 3 non-prose blocks (H4) — excludes intro/overview sections |
| `topic-mixing` | major | New / edited block violates `block-density` R1 (single-topic) |
| `placement-violation` | major | New block violates PR1–PR4 of `content-graph.md` (wrong chapter, forward dep, density overrun, cross-chapter forward) |
| `reorg-map-stale` | major | Structural change committed without updating `docs/reorganization-map.md` (PR7) |
| `oversized-block` | minor | Block exceeds R2 length limit (40 non-blank lines) without topic-mixing |
| `embedded-table` | minor | Block embeds a table > 5 rows (R3) — extract to `table` block |
| `intra-chapter-energy` | minor | `chapter-complexity-review` graph energy increased without a new forward-ref finding (suggests room for section reordering) |
| `cross-section-coupling` | minor | New H3 cross-section edge crossing > 3 sections |
| `isolated-block` | minor | H6 isolated block — no incoming or outgoing edges |
| `archimedean-wall-violation` | minor | A post-wall block (in `descartes-universe` and later chapters) is referenced from a pre-wall block via `uses[]` without the target carrying `tags: ['archimedean-bridge']` or an explicit conditional banner — the pre-wall block has silently leaked an `ℝ`-specific dependency into generic-`R` content |
| `remark-ratio` | info | H7 remark/example ratio drifted outside the 2:1 band |
| `preview-source-fwd-ref` | info | H1 forward ref sourced from a preview chapter (`intro` / `notation`) — info-only, never escalated (see §Preview-chapter exclusion) |

### Excluded forward-reference patterns (STRICT)

Two classes of pattern are **never** flagged as H1 forward references,
even if the target block's source position is strictly later than
the source block's. Both classes encode authoring conventions that
are correct by design, so flagging them produces only false positives.

1. **Statement → own proof.** A `prf:foo` block is the proof of its
   statement `prop:foo` / `lem:foo` / `thm:foo` / `cor:foo`. The
   proof block belongs **after** the statement; this is the correct
   reading order, not a forward reference. Patterns matched (any of):

   ```
   prop:foo  → prf:foo                  (exact suffix match)
   prop:foo  → prf:foo-proof            (with -proof suffix stripped)
   prop:foo  → prf:foo-<qualifier>      (qualified-variant proofs
                                         like prf:foo-categorical)
   lem:foo   → prf:foo                  (same shape for each of the
   thm:foo   → prf:foo                   four provable-kind prefixes)
   cor:foo   → prf:foo
   ```

   The qualified-variant rule accepts any `prf:` block whose name
   starts with `<statement-suffix>-`. The pre-2026-05-19 heuristic
   flagged 145 such pairs as H1 false positives on QOU paper main;
   the filter (added 2026-05-19 to `content-graph-analysis.py`'s
   `_is_statement_to_own_proof`) eliminates that class.

2. **Preview-chapter source.** Forward refs whose **source** block
   lives in a preview chapter (`introduction`, `notation`) are
   info-only — see §Preview-chapter exclusion above. Tagged
   `preview-source-fwd-ref` if surfaced for awareness, never
   escalated to a finding.

When adding a new exclusion class, document the pattern here, the
empirical false-positive count it eliminates, and the corresponding
filter location in the graph-analysis script.

## Slot E — §4d discharge bands (examples)

| Band | Examples |
|------|----------|
| **Auto-discharge** | `embedded-table` — extract via mechanical `kind: "table"` block creation per `block-density` R3; `intra-chapter-energy` where `chapter-complexity-review` reports an **intra-section** block swap that resolves a span-1 forward edge AND `block-density-audit` reports no R1 hit on either swapped block AND `bun run validate` exits clean post-swap |
| **Author-assist** | Section split (H5 dense), section merge (H4 sparse — section labels disappear, surrounding `uses[]` may need touch-up, judgement call), cross-chapter block move (H2 / PR4 violation), new section creation, `topic-mixing` split (R1), `critical-path-break`, `reorg-map-stale` requiring author to choose canonical move description |
| **Defer** | Architectural backward edge across the Archimedean ↔ categorical wall (`wontfix: architectural`); single-occurrence span-1 forward edge between adjacent sections; `isolated-block` flagged for content-pass not structure-pass; `remark-ratio` within ±20% of the band edge |

**Auto-discharge safety net (STRICT).** Every auto-discharge MUST:

1. Run `cd content && bun run validate` post-edit and exit clean.
2. Re-snapshot the graph and verify (a) H1 finding count did not
   increase, (b) no section moved out of the 3–18 band, (c) H2
   finding count did not increase.
3. If either check fails, **revert** the change via
   `git checkout -- <edited-files>` and reclassify the finding as
   `needs-author`.

**Section merge is deliberately NOT auto-discharge.** Although the
parent's discharge-band table lists "mechanical fix" as the
auto-discharge criterion, section merges rename section labels and
ripple through every `interprets` / cross-reference. That's
semantic, not mechanical — always escalate via Slot F.

## Slot F — §4e author-ask templates

For `dense-section` (H5):

> Section `<sec-label>` in chapter `<chap>` has grown to N blocks
> (limit 18) after `<commit-sha-or-pr>`. `content-graph
> --proposals` suggests splitting along `<natural-boundary>` into
> `<S₁-label>` (N₁ blocks) + `<S₂-label>` (N₂ blocks). Question:
> 1) accept the proposed split, 2) propose a different split,
> 3) defer (mark section as deliberately dense, wontfix).

For `sparse-section` (H4):

> Section `<sec-label>` in chapter `<chap>` has N < 3 non-prose
> blocks after `<commit-sha-or-pr>`. Adjacent sections are
> `<prev-label>` (N_prev blocks) and `<next-label>` (N_next
> blocks). Question: 1) merge with `<prev-label>`, 2) merge with
> `<next-label>`, 3) keep separate (mark as deliberately sparse —
> e.g. intro / capstone).

For `cross-chapter-forward` / `placement-violation`:

> New block `<label>` in chapter `<C₁>` depends (via `uses[]`) on
> `<dep-label>` in chapter `<C₂>` where `<C₁>` precedes `<C₂>` —
> this is a forward cross-chapter edge (PR4 violation). Question:
> 1) move `<label>` to chapter `<C₂>`, 2) move `<dep-label>` to
> chapter `<C₁>`, 3) accept as architectural cross-callback
> (wontfix: architectural, document in `reorganization-map.md`).

For `critical-path-break`:

> Block `<moved-or-removed>` was on the logical chain from
> `<upstream-def>` to `<downstream-thm>`. After `<commit-sha>` the
> chain no longer reaches `<downstream-thm>`. Question: 1) add a
> replacement bridge block, 2) restore the upstream edge in
> `<moved-block>.ts uses[]`, 3) confirm the chain is intentionally
> broken (mark `<downstream-thm>` for proof-watcher escalation).

For `reorg-map-stale`:

> Structural change in `<commit-sha>` (moved `<block>` from
> `<from-sec>` to `<to-sec>`, OR split/merged `<sec>`) but
> `docs/reorganization-map.md` was not updated. Question:
> 1) append a one-line entry now (suggested wording: `<…>`),
> 2) the move is being staged for a larger PR (defer map update
> to that PR), 3) revert the move.

## Slot G — §5a backlog discovery

```bash
# 1. Run the full graph analysis with proposals (the workhorse).
( cd content && python3 pipeline/content-graph-analysis.py --proposals ) \
  > /tmp/_detangler_backlog_proposals.md 2>/dev/null
( cd content && python3 pipeline/content-graph-analysis.py --json ) \
  > /tmp/_detangler_backlog_graph.json 2>/dev/null

# 2. Run block-density audit across every paper.
for paper in $(ls content/ 2>/dev/null | grep -v schema | grep -v pipeline); do
  paper_dir="content/$paper"
  [ -d "$paper_dir" ] || continue
  ( cd content && python3 pipeline/block-density-audit.py "$paper" ) \
    >> /tmp/_detangler_backlog_density.txt 2>/dev/null
done

# 3. Reorganisation-map freshness — list block moves on origin/main
# in the last 30 days that aren't reflected in the map.
git log --since='30 days ago' origin/main --pretty=format:'%H' \
  --diff-filter=R --name-only \
  -- 'content/' \
  > /tmp/_detangler_recent_renames.txt 2>/dev/null
```

Convert each finding (from `findings[]` in the JSON), each
`--proposals` entry, and each density-audit hit into a queue item
with `source: backlog`.

## Slot H — §5b prioritisation

Override the parent's default rule with this structure-specific
ordering:

1. **Severity** — critical → major → minor → info.
2. **Forward-ref span** — `chapter_span > 0` first, then
   `section_span > 3`, then `section_span ≤ 3` last. (The
   `description` field of an H1 finding carries
   `chapter_span=N, section_span=M`.)
3. **Downstream impact** — count blocks that transitively depend on
   the affected block via `uses[]`. Use the `blocks` field of
   findings + walk `edges[]` from the graph JSON.
4. **Section density distance** — sections farthest outside the
   3–18 band first (sort by `|size - clamp(size, 3, 18)|`).
5. **Last-audit recency** — older `audited[]` entry first.
6. **Alphabetical** as tie-breaker.

## Slot I — §6 invariants

Every check derives from the post-edit graph + density snapshots —
the script does **not** export summary scalars, so counts come from
the `findings[]` array.

| Invariant | Check |
|-----------|-------|
| H1 forward-ref count never increases on own-branch commits **(excluding preview-chapter sources)** | `count_nonpreview(current.H1) <= count_nonpreview(baseline.H1)` where `count_nonpreview(H) = len([f for f in H if by_label[f.blocks[0]]['chapter_dir'] not in PREVIEW_CHAPTERS])` |
| No section newly leaves the 3–18 band | For every section S, if pre-edit `len(S.blocks) in [3,18]` then post-edit `len(S.blocks) in [3,18]` |
| H2 cross-chapter forward edges don't grow **(excluding preview-chapter sources)** | `count_nonpreview(current.H2) <= count_nonpreview(baseline.H2)` |
| No new `archimedean-wall-violation` (silent post-wall → pre-wall leak) | Walk every new / changed block whose `chapter_dir` precedes `models-of-qous` in the paper's chapter order; for each `uses[]` target whose `chapter_dir` is `descartes-universe` or later, the target must carry `tags: ['archimedean-bridge']` OR the source's `.md` must contain an explicit `Theorem (conditional on archimedean specialisation)` banner |
| No new R1 topic-mix | `python3 pipeline/block-density-audit.py <paper>` exit code 0 AND `grep -c 'R1' stdout` does not increase vs baseline (the script prints `R1`/`R2`/`R3` per-violation lines on stdout — there is no `--json` mode) |
| `docs/reorganization-map.md` updated alongside every block move | `git diff --name-only HEAD~1 HEAD` includes both the chapter manifest AND `docs/reorganization-map.md` whenever a block changed sections |
| Schema clean | `cd content && bun run validate` exits 0 |

If any invariant fails on a proposed commit, **block the commit**,
queue the violation as `critical`, revert the working tree changes,
and ask the author (per parent §6).

## Domain-specific anti-patterns (extends parent)

- Auto-execute a section **split**. Splits introduce new section
  labels and require a name; that's a judgement call. Always
  escalate via Slot F.
- Auto-execute a section **merge**. Merges remove a section label
  and may ripple through `interprets` / cross-references. Always
  escalate via Slot F. (The auto-discharge band in Slot E
  deliberately excludes section merges to resolve the apparent
  tension with this anti-pattern — auto-discharge is intra-section
  swaps + `R3` table extraction only.)
- Forget `docs/reorganization-map.md`. PR7 of `content-graph.md`
  is enforced as a hard invariant (Slot I) — never let a move land
  without the map update.
- Discharge a finding that lives downstream of a proof gap without
  consulting the proof watcher's queue. A `critical-path-break`
  may be a proof issue, not a structural one — coordinate via
  `/coordinate` before fixing.
- Treat architectural backward edges (Archimedean ↔ categorical)
  as fixable. They are `wontfix: architectural` by design.

## Checklist (extends parent)

- [ ] Graph baseline JSON cached at `/tmp/_detangler_watcher_graph_baseline.json`
- [ ] Slot B trigger filter covers BOTH paper and nested chapter
      manifests (`content/<paper>/<paper>.ts` AND
      `content/<paper>/<chapter>/<chapter>.ts`) AND uses
      `git diff-tree -M` for rename detection
- [ ] Slot C dispatch uses real CLIs
      (`content-graph-analysis.py`, `block-density-audit.py`) —
      never invents a `--json` flag that doesn't exist
- [ ] Slot D finding kinds map 1-to-1 to `content-graph.md`
      heuristics H1–H7 + `block-density` R1–R3 + PR1–PR7
- [ ] Preview-chapter filter applied to every H1 / H2 finding
      (forward refs sourced from `intro` / `notation` are info-only)
- [ ] Archimedean-wall check applied to every new pre-wall block
      with `uses[]` targeting post-wall content
- [ ] Slot E auto-discharge band is **only** intra-section swaps
      + R3 table extraction (NO section merge / split)
- [ ] Slot I invariants derive from `findings[]` array — not
      from invented summary scalars
- [ ] `docs/reorganization-map.md` updated alongside every block
      move (Slot I)
