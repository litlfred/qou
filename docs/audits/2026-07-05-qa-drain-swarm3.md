# QA drain — swarm lane 3 (2026-07-05)

Branch: `claude/qa-drain-swarm3-2026-07-05` · PR #3371. QA-drain lane
only (`.qa.json` sidecars + this audit doc). Fails needing content /
Lean / compute fixes are documented here, not fixed in-lane.
`particle-interactions/electroweak-*` is owned by another agent and is
untouched.

## Beans

| Bean | Title | Outcome this session |
|---|---|---|
| **qsb2** | Apply stub dispositions from 2026-07-02 triage | Residuals all require Lean edits → **out of lane, documented** below |
| **9pxo** | Triage QA fails surfaced by PR #3327 sidecar refresh | **Verified all resolved on main**; disposition stamped via `qa-merge-findings` |
| **l7n4** | Aggregate + run `qa-merge-findings.ts` | **Ran** on the 9pxo triage batch (4 blocks) |

---

## 9pxo — triage of PR #3327-surfaced fails (VERIFIED RESOLVED)

PR #3327 (`chore(qa-sweep): refresh stale sidecars after exposition
drain`, merged 2026-07-04) refreshed batch-1 sidecars and surfaced five
verdict flips that were *already live on `main`* (the exposition-drain
`.md` edits were merged; stale sidecars had been hiding them). Current
committed state on my base (`origin/main` @ `95377cbd9d`):

| Block | Criterion | #3327 flip | Current | Resolved by |
|---|---|---|---|---|
| `appendix-atomic-mass-calculations/amc-method` | `voice-editorializing` | pass→fail | **pass** | script re-verdict 2026-07-05 |
| `introduction/intro` | `voice-editorializing` | pass→fail | **pass** | script re-verdict 2026-07-04 |
| `measurement-observation/observation-braid` | `q-usage-narrative-chapter-mismatch` | pass→warn | **pass** | human verdict (litlfred) 2026-07-05 |
| `measurement-observation/torsion-knot-flow` | `wall-side-correct` | pass→fail | **pass** | §7c banner restored; re-verdict 2026-07-05 |
| `gravity-spacetime/lqg-entropy-qdim-partition-pole` | 7 criteria | n/a→pass | pass | benign applicability reclass (already OK per #3327) |

**Conclusion:** every #3327-surfaced automated fail is resolved on
`main` (four via subsequent content edits + re-sweeps, one via a human
fix). No open automated fail remains from the #3327 refresh.

**Residual (out of lane):** `torsion-knot-flow` still carries a
`q-usage-narrative-chapter-mismatch: warn` (script, 2026-07-05). A warn,
not a fail; resolving it needs an `.md` chapter-context edit (out of the
QA-drain lane). Flagged for the q-usage / detangler lane.

The residual `da-*` (devils-advocate) agent verdicts on these blocks
(e.g. `torsion-knot-flow` `da-referee-verdict: fail critical`,
`da-reproducibility`, `da-lean-narrative-divergence`) are **not**
#3327-surfaced — they are separate agent-review items authored by
`local/qa-agent-drain`, requiring `.md`/`.lean` content work (out of
lane). Recorded for the devils-advocate watcher.

---

## l7n4 — `qa-merge-findings.ts` aggregate (RAN)

There is no standing findings backlog waiting to be merged — the
`.beans/qa-agent-drain-queue.json` is a queue of *audits to perform*,
not *completed findings to merge*. The genuine in-lane input this
session produced is the 9pxo triage disposition, which was aggregated:

```
bun run folio-assistant/content/pipeline/qa-merge-findings.ts \
  --file /tmp/swarm3-triage-findings.json
→ { added: 4, skipped: 0 }
```

Four confirmatory agent entries (`reviewer.id = local/qa-drain-swarm3`)
were appended to the four #3327 blocks' sidecars, each `result: pass`
with a triage note citing the #3327 provenance + resolution source.
Multi-reviewer history preserved (no prior entries deleted); `paths`
stayed canonical `../qou/…` (the merge only rewrites paths when
bootstrapping a brand-new sidecar; all four pre-existed). Committed as
`chore(qa-merge-findings): record 9pxo triage …`.

---

## qsb2 — stub-disposition residuals (OUT OF LANE)

Per [`docs/audits/2026-07-02-stub-triage.md`](2026-07-02-stub-triage.md)
plus the bean's 2026-07-03 round-2 progress note, the qsb2 worklist has
been drained to **6 projection residuals**, each of which requires a
**`.lean` edit** (de-project a self-assuming projection into a genuine
derivation). All are out of the QA-drain lane and are recorded here for
the Lean lane (cf. sibling PRs #3370 `do-lean-backlog`, #3299
`lean-qa-backlog`):

1. `prop:demand-stability`
2. `prop:confinement-universality`
3. `prop:brane-tower-q-laplacian-decay`
4. `prop:q-plancherel-asymptotic-skeleton`
5. `prop:strangelet-crossing-energy`
6. `prop:substrate-consistency-window` (near-tautological window encoding)

Target shape (worked exemplars named in the triage doc): the
molecular-construction quartet (`h2/ch4/co2-lp-dual-binding`,
`benzene-threading-emergence`) and `prop:sdp-regime-switch`
("Disposition (derived, not projected)"). No sidecar action is
appropriate until the Lean is de-projected and re-swept.

---

## Stale-sidecar inventory (NOT refreshed here — see hazard below)

A `qa-staleness.ts` scan of `content/quantum-observable-universe`
(2704 blocks) found **17 whole-block `[STALE]`** sidecars with genuine
source-hash drift (mostly `.lean` content drift). 16 are refreshable
(the 17th, `conj:electroweak-higgs-torus-link-triplet`, is EW —
off-limits):

| Section | Stale blocks |
|---|---|
| `braids-and-knots` | `skein-resolution-obstruction`, `frobenius-lepton-meson-bridge` |
| `quantum-universes` | `quantum-universe-exists`, `tannaka-krein-overview`, `fundamental-object-explication`, `snake-identity`, `rigid-monoidal-category`, `quantum-universes-intro`, `scheme-notation`, `simple-objects-V`, `quantum-universe-su2` |
| `lifting-and-descent` | `descent-lemma`, `brane-boundary-structure` |
| `mass-theory` | `spin-involution`, `y-lambda-recipe-from-partition`, `markov-trace-product` |

(Example verified drift: `markov-trace-product` sidecar `lean` hash
`ef98db625ec8` vs actual `edef31f1a30c`.)

These were **deliberately not refreshed in this session** — see the
environmental hazard below. They belong to the qsb3 stale-refresh lane
(PR #3338, merged; batches ongoing) and should be swept in an
environment where reference resolution is correct. Handed off to qsb3.

---

## ⚠ Environmental hazard — `qa-sweep` via the folio-assistant clone produces FALSE `bib-cite-resolves` criticals

`scripts/setup-folio-assistant.sh` symlinks the platform pipeline in and
the sweep resolves `REPO_ROOT` to the **folio-assistant clone**, not the
running worktree. In this clone,
`folio-assistant/content/schema/references.ts` is a symlink pointing at a
**different agent's worktree**
(`…/agent-aa8427059fd9e4602/content/schema/references.ts`), whose target
does not even resolve (`readlink -f` → empty). Consequently the
cross-repo checker `bib-cite-resolves` cannot find *any* reference and
flips **every** cited block to `fail critical`.

Demonstrated: a dry `qa-sweep` of `quantum-universes` reported **12
`bib-cite-resolves: fail critical`** (e.g. `quantum-universe-exists`:
`\cite{kassel1995} … does not resolve in references.ts`) — yet the
committed sidecar on `main` has `bib-cite-resolves: pass`, and
`kassel1995` is present in the worktree's `references.ts`. The fails are
**artifacts of the wrong `references.ts`**, not real QA regressions.

**Implication:** committing sweep output from this environment would
poison sidecars with false `bib-cite-resolves` criticals (and any other
repo-global cross-reference criterion). Section/whole-paper sweeps in
this sandbox configuration are unsafe until the clone's
`content/schema/references.ts` symlink points at the *running* worktree.
`qa-merge-findings.ts` is **not** affected — it re-runs no checkers and
resolves blocks via `git rev-parse --show-toplevel` (the running
worktree).

Recommended fix for the stale-refresh lane: either (a) run
`qa-sweep --only <criteria>` restricted to self-contained
(single-triple) criteria, excluding `bib-*` and other repo-global
checks, or (b) repoint the clone's `references.ts` symlink to the
running worktree before sweeping.

---

## Verified vs blocked

- **Verified / done:** 9pxo triage (all #3327 fails resolved on main);
  l7n4 aggregate ran, 4 sidecars updated, diffs clean + canonical paths.
- **Out of lane (documented, not fixed):** qsb2's 6 Lean projection
  residuals; `torsion-knot-flow` q-usage warn; residual `da-*` agent
  verdicts.
- **Blocked (handed to qsb3):** the 16 refreshable `[STALE]` sidecars —
  cannot be safely swept in this sandbox because the folio-assistant
  clone's `references.ts` symlink resolves to another worktree, yielding
  false `bib-cite-resolves` criticals.
