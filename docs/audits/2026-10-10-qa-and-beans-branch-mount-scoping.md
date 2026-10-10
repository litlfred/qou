# QA to `cat/cat-harness/qa-reports`, beans to a mounted branch — scoping

**Date:** 2026-10-10. **Scope:** read-only scoping. Nothing was moved, no
branch was seeded, no bean or sidecar was edited.

**Owner's asks (2026-10-10):** (1) *"make sure qou QA is in
cat/cat-harness/qa-reports"*, (2) *"beans are branch mounted too"*.

**Measured against:** qou `origin/main` `3b8cef881` (shallow clone, 142
commits deep, so history counts below are bounded by that window);
platform `litlfred/folio-assistant` main `05fcf008ea` (2026-10-10) checked out
at `/home/user/fa-main` with its layers mounted; qou's pinned platform
`717aa19a6` (2026-10-06, `.folio-assistant-pin`, `build.yml:27`). Where the
pin and platform main differ, both are stated.

---

## 0. Summary

| | QA (move 1) | Beans (move 2) |
|---|---|---|
| Platform layout | `qa-reports` branch, keyed **by commit**: `main/<sha>/` and `pr/<n>/<sha>/`, each holding `manifest.json` + `test/results/**` byte-identical to the checkout. Block verdicts stored **as-is** (`block-qa/v1`) at `test/results/block-qa/<repo-relative block path>.qa.json`. **Judgements are not on the branch**: by owner ruling D2(a) every non-script verdict stays on `main` under `test/attestations/block-qa/…attestations.json` (`qa-attestations/v1`). | Orphan branch keyed **by tip** (one live copy): `manifest.json` (`state-manifest/v1`) + `README.md` + `beans/**` mirroring the checkout. Mounted at `beans/` by `state:mount` (session-start hook); writes go back by `branch-store push --id beans` (splice with `expect`, no force). `/beans/**` is gitignored on `main`. |
| qou today | 3,653 `block-qa/v1` sidecars, **210.7 MB**, all **beside their blocks** under `folio/**` (legacy location). `qa-reports` on qou holds **one** entry, `pr/7518/…`, compute-QA only (19 files). No `main/<sha>` entry exists. | 5,554 files / 40 MB at `beans/defs` on `main` (5,541 beans + 13 queue/aux files). No `beans` directory in `qou.json`, no state branch, no mount. **61 of the last 113 `main` commits (24 h) touch `beans/defs`.** |
| Already broken today | **Yes — split-brain.** Since the pin bump to `37a36ce` (2026-09-26), the platform `qa-sweep` writes to `test/results/block-qa/…` (gitignored in qou) and reads the legacy sibling only as a fallback. So a sweep in qou refreshes nothing that is committed, and in any checkout where a sweep has run, a verdict an agent later appends to the sibling is **shadowed** for every platform reader (results tree is read first). | No. |
| Blocking prerequisite | Platform pin bump (the attestation migrator exists at the pin, but `qa-refresh`/`qa-working-copy`-era readers and the reader migration post-date it). | Platform pin bump: `state:seed --cutover` / `--repo-root` exist only after **2026-10-08** (`283ba67e76`); at the pin, `state-seed.ts` defaults to the **platform** checkout and would seed the wrong repo. Also qou must declare `fsh-guts` at a branch tip (the cutover refuses otherwise). |
| My recommendation (judgement) | Do the platform's split, not "everything on the branch": derived reports → `qa-reports`; the 126,315 agent/human verdicts → `test/attestations/` on `main`. Fix the split-brain first; remove from `main` last, as its own owner-approved commit. | Do it, on `cat/qou/beans`, after the pin bump; cut over in one freeze window; it removes the bean-append merge-collision problem by construction. |

---

## 1. Move 1 — QA to `cat/cat-harness/qa-reports`

### 1a. The platform's canonical layout

**Declaration.** qou already declares it (`qou.json`, directory `qa`):
`path: test/results/`, `graphTypologies: [qa]`,
`storage: { branch: cat/cat-harness/qa-reports, keyedBy: commit }`. Same as the
platform's own `cat-harness/cat-harness.json` (`id: "qa"`, lines 662-676).
`test/results/*` is gitignored in qou (`.gitignore:284-285`, `.gitkeep` kept).

**Branch layout** (`cat-harness/scripts/qa-store.ts:7-16`):

```
cat/cat-harness/qa-reports   (orphan; never merged; author folio-qa-bot)
├── index.json                       qa-reports-index/v1: newest entry per ref
├── main/<commit-sha>/               one tree per main commit that published
│   ├── manifest.json                qa-reports-manifest/v1
│   └── <instance>/test/results/**   byte-identical to the checkout's layout
└── pr/<number>/<head-sha>/…
```

Paths are repo-relative, so for qou (instance root = repo root) the entry is
`main/<sha>/test/results/**` — exactly what qou's one existing entry looks like.

**Block verdict format: stored as-is, not converted.** The block family's path
rule is `cat-harness/content/pipeline/qa-paths.ts:53-69`:
`blockQaPath(repoRoot, blockRoot) = <repo>/test/results/block-qa/<relative(repo, blockRoot)>.qa.json`.
So `folio/quantum-observable-universe/mass-theory/x.qa.json` becomes
`test/results/block-qa/folio/quantum-observable-universe/mass-theory/x.qa.json`,
still `block-qa/v1`. It is **not** converted to `kg-qa/v1` (that schema is the
knowledge-graph subject family, `cat-harness/schemas/kg-qa.ts`). Read falls back
to the legacy sibling, write never does (`qa-paths.ts:31-43`).

**The judgement half stays on `main`.** `cat-harness/schemas/qa-attestations.ts:1-25, 90-108`:
owner ruling D2(a), 2026-10-01 — *derived script verdicts move to the branch;
anything a reviewer judged stays on main*. For `block-qa`, every criteria entry
whose `reviewer.kind` is not `script` is copied (never stripped) to
`test/attestations/block-qa/<same mirror>.attestations.json`
(`qa-attestations/v1`), and the derived report keeps a **projection** because
~30 readers take `criteria[id][0]`. qou already declares
`test/attestations/` (`qou.json`, id `attestations`) but holds only the two
bibliography families there (`bib-verification/`, `bib-human-review/`).

**How the platform itself does it today.** Fetched trees-only
(`git fetch --depth=1 --filter=blob:none`):

| | platform `cat/cat-harness/qa-reports` | qou `cat/cat-harness/qa-reports` |
|---|---|---|
| tip | `adb4eb3a` 2026-10-10, folio-qa-bot | `c804129b` 2026-10-05, folio-qa-bot |
| `main/<sha>` entries | **423** | **0** |
| `pr/<n>` entries | 383 | 1 (`pr/7518/e36739a…`) |
| files | 2,172,125 | 21 |

One platform entry, `main/fff84e86…`, by family: `cat-harness/test/results/kg-qa`
488, `witnesses` 221, **`block-qa` 172**, `detangle` 70, `library-qa` 66,
`translation-qa` 35, … A block file there opens
`{"$schema": "block-qa/v1", "label": …, "paths": …, "source_hashes": …, "criteria": …}`
— i.e. the sidecar unchanged. Its `manifest.json` carries a
`completeness` block (`mode: computed`, `files: 1338`, per-family counts) written
by `qa:refresh`. On platform `main`, `git ls-files | grep -c '\.qa\.json$'` = **0**:
the platform has already removed its sidecars from `main`.

Who writes it on the platform: `code-quality-gates.yml:4051`,
`bun run cat qa:publish --github --completeness build/qa-refresh.json`, after
`qa:refresh` (`cat-harness-tools/scripts/qa-refresh.ts`) runs every declared
writer — including `qa-sweep` over the authored docs (`qa-refresh.ts:172-177`)
— into the empty working tree. Readers: `docs-site.yml:226-240` fetches
`main/<sha>` (fallback newest `main`) before generating;
`folio-staging.yml:411-469` fetches `pr/<n>`, optionally sweeps, then
`publish-block-qa.ts` summarises for the review heat map.

**One constraint that shapes the plan:** an entry is written **once**. A second
publish to the same key is `present` and *"the first write stands"*
(`qa-store.ts:835, 901-902`). qou's `compute-qa.yml:72-76` already publishes
`main/<sha>` with `--root test/results/compute-qa` only. If block QA is published
by a different job for the same commit, whichever runs second is silently dropped.

### 1b. Every qou reader and writer of the current location, and what breaks

**What qou holds** (`git ls-files`, re-runnable):

| family | files | bytes | where |
|---|---:|---:|---|
| `*.qa.json` (`block-qa/v1`, 3,653/3,653) | 3,653 | 210,737,100 | all under `folio/` (QOU 3,596, UGB 33, Fred2005 12, bach2013 9, visualizer 3) |
| `*.script-qa.json` | 1,798 | 14,180,741 | `computations/**` (568 in `_deprecated/`) — **not in this request's scope**, flagged |

Entries inside the 3,653 block files (python over every file):
**219,090 `script`, 126,299 `agent`, 16 `human`, 128 with no `reviewer.kind`**.
3,608 of 3,653 files carry at least one non-script entry. This reproduces bean
`qou-6ccl`'s 126,315 agent+human figure exactly. `expo-milnor-clarity` alone: 2,604
agent entries already on `main`, plus the sibling branch
`claude/milnor-voice-audit-ch1-ch2-2026-10-10`, which changes **376** sidecars
(+11,793 lines) and nothing else but one audit doc.

**The split-brain that already exists.** At the qou pin `717aa19a6`,
`cat-harness/content/pipeline/qa-sweep.ts:425` sets
`qaPath = blockQaPath(contentRepoRoot, block.root)`, `:434` reads
`existingBlockQaPath(...) ?? qaPath`, `:793` `saveQaReport(qaPath, report)`.
`blockQaPath(` first appears in `qa-sweep.ts` at platform `37a36ce` (qou pin since
2026-09-26; absent at `df28d02`). Consequences, from code, not from a run:

1. `qa-sweep` on qou writes into the **gitignored** `test/results/block-qa/`. The
   committed sidecars are never refreshed by a sweep — AGENTS.md §work-plan 4
   ("refresh stale sidecars … running `qa-sweep`") now produces nothing
   committable. `scripts/check-sidecars.sh:117,126` then re-reads `$base.qa.json`
   and keeps reporting it stale.
2. `existingBlockQaPath` returns the results-tree file **first**
   (`qa-paths.ts:82-93`). In a checkout where a sweep has run, every qou writer
   that appends to the sibling (list below) writes a verdict no platform reader
   sees there.
3. The pin's own release note in `.folio-assistant-pin` already records the
   symptom: *"no-orphan-sidecar could not check test/results/block-qa (absent here)"*.

Not measured: whether any agent has actually been bitten (the main checkout
`/home/user/qou/test/results/` is empty right now). The defect is latent per
checkout, live by construction.

**qou WRITERS of the sibling location** (compose `<root>.qa.json` by hand; none
calls `qa-paths.ts`):

| file:line | what |
|---|---|
| `folio/pipeline/qa-agent-entry.ts:88` | the agent-verdict appender (used by the milnor audit and `skills/local/language-trap-agent-audit.md`) |
| `scripts/reaudit_verdict.py:3,40` | appends agent verdicts |
| `folio/pipeline/definition-clarity-audit.ts:1044,1157` | `clarity-*` sidecar entries |
| `folio/pipeline/language-trap-audit.ts:330,536` | |
| `folio/pipeline/trace-convention-audit.ts:695` | |
| `folio/pipeline/lean-vacuity-axiom-audit.ts:3161` | `--write-sidecars` |
| `folio/pipeline/qa-evidence-migrate.ts:88` | globs `**/*.qa.json` |
| `scripts/expire-unhashed-agent-verdicts.py:72` | rglob, rewrites |
| `scripts/qa-sidecar-agent-union.py:104` | union-merge of sidecars at merge time |
| `scripts/split_amalgamated.py:37,63` | |

**qou READERS:**

| file:line | note |
|---|---|
| `scripts/check-sidecars.sh:117,317` | the AGENTS.md pre-commit preflight |
| `scripts/lean-qa-progress-table.py:246-266` | sibling glob + sibling-of-sidecar lookup |
| `scripts/qa-duplicate-verdict-check.py:91` | `folio/**/*.qa.json` |
| `scripts/reaudit-da-compile-claims.py:148` | |
| `folio/pipeline/qa-evidence-audit.ts:91`, `qa-flag-preservation-audit.ts:159`, `trace-convention-audit.ts:677` | |
| `computations/ab_methodology_metrics.py:137` | rglob under `folio/` |
| `scripts/qa-evidence-provenance-gate.py:118`, `scripts/qa-stale-agent-evidence.py:94`, `scripts/reaudit-proof-deterministic.py:148` | **already find nothing**: they glob `content/**`, which does not exist since the `content/`→`folio/` move (2026-09-27). Pre-existing defect, independent of this move. |
| filters that merely skip `.qa.json`: `arity-conflation-candidates.ts:412`, `superseded-block-lean-audit.ts:90`, `count-actionable-placeholders.ts:55` | unaffected |

Plus **24** skill/agent-memory/command files and **8** AGENTS.md sites
(lines 585, 777, 784, 1442, 1506, 4020, 4584, 5966) that describe the sibling
convention. Platform readers that matter for qou: `qa-sweep` (reads both),
`publish-block-qa.ts` (reads both), `validate.ts` `no-orphan-sidecar`
(results tree only), `qa:verify-moved` (results tree only — see below).
qou's published build (`build.yml` → platform `publish.yml@717aa19a6`) does not
read block QA at all (grep for `qa-sweep|publish-block-qa|qa-store|qa.json`: 0).
qou has no staging workflow that calls `folio-staging.yml`.

**If the 3,653 files left `main` today, without the steps below:** every
reader above returns empty and reads as clean (the `dh4f` failure the platform
code warns about), every writer recreates siblings, and the 126,315 agent/human
verdicts would exist only on a branch that has no `main/<sha>` entry for qou at
all — i.e. nowhere.

**`qa:verify-moved` does not see the sidecars where they are.** Its moved set is
*"every file under every directory an instance declares as a `qa` graph"*
(`qa-verify-moved.ts:11-15`). qou's `qa` directory is `test/results/`; the
sidecars are under `folio/`. So the platform's hash-verification gate cannot be
run until the files are first materialised into `test/results/block-qa/`.

### 1c. Migration steps (ordered), each with its check

0. **Settle in-flight writers.** Land or rebase the milnor branch (376
   sidecars) first, and announce a write freeze on `*.qa.json` for the window of
   steps 3-6. *Check:* `git diff --name-only origin/main...<branch> | grep -c .qa.json`
   is 0 on every open sibling branch you can see.
1. **Bump the platform pin** past the reader migration (`qa-working-copy.ts`
   does not exist at `717aa19a6`). This is the post-2026-10-08 platform, where
   `cat-harness` / `cat-harness-tools` are remote-mounted layers
   (`index.config.json`), so `scripts/setup-folio-assistant.sh` must run
   `mount-from-lock`. *Check:* the pin file's own protocol — `run-validate
   folio/quantum-observable-universe` before/after on the same corpus commit,
   issue lines identical; `bash scripts/folio-pin-coupling-check.sh` exit 0.
2. **Copy the judgements to the attestation store on `main`.**
   `bun run cat qa:attestations:migrate --family block-qa --dry-run`, then without
   `--dry-run` (`cat-harness-tools/scripts/migrate-qa-attestations.ts`; present at
   the pin too). Copy-never-strip for block-qa. *Check:*
   `qa:attestations:migrate:check` exit 0; count of entries across
   `test/attestations/block-qa/**` = 126,315 (+ however the 128 kind-less entries
   are ruled, decision Q2); a parity check that no `folio/**` `.md`/`.ts`/`.lean`
   byte changed (owner hard rule on `qou-5lsb`).
3. **Materialise the derived tree byte-for-byte.** Copy each
   `folio/**/X.qa.json` to `test/results/block-qa/folio/**/X.qa.json` with `cp`,
   **not** by running `qa-sweep` (a sweep rewrites the files and the result would
   not be the record being moved). *Check:*
   `bun run cat qa:verify-moved --inventory` lists 3,653 block-qa paths (plus
   compute-qa if present).
4. **Publish ONE entry per commit carrying both families.**
   `bun run folio-assistant/cat-harness/scripts/qa-store.ts publish --ref main/<sha> --root test/results/block-qa --root test/results/compute-qa`
   — single publisher, because the first write stands. Either fold this into
   `compute-qa.yml` (dispatch-only) or run it from a container. *Check:*
   `qa-store.ts read --ref main/<sha> test/results/block-qa/folio/…/<any>.qa.json`
   exit 0; `bun run cat qa:verify-moved --key main/<sha>` exit **0 (identical)** —
   exit 2 (unknown) is not a pass.
5. **Migrate the qou readers/writers** in 1b to the platform resolver
   (`existingBlockQaPath` for reads, `blockQaPath` + `qa-attestations`
   `finalizeCriteria` for writes), fix the three `content/**` globs, and update
   AGENTS.md / the 24 skill files. *Check per tool:* a two-block fixture (one
   sibling-only, one results-only) where each reader reports both blocks and
   each writer lands its agent entry in `test/attestations/block-qa/…` and the
   projection in the results tree; `publish-block-qa.ts --folio folio/quantum-observable-universe`
   gives the same `counts` before and after.
6. **Remove from `main`** — one commit, `git rm` of the 3,653 sidecars, only
   after an owner ruling (Q3), only with step 4's IDENTICAL verdict for the
   commit being removed from, and with `fsh-guts` holding the pack if the
   owner wants the cutover-snapshot rule applied here too. *Check:* after
   `qa:fetch --ref main/<that sha> --into test/results`, `publish-block-qa`
   counts equal the pre-removal counts; `qa:attestations:migrate:check` still 0.
7. **Keep it current.** Sessions read QA from `qa:fetch --ref main` (newest) into
   `test/results/` before any QA reader; whoever publishes main entries must run
   per merged commit, or readers silently use an older commit's verdicts (the
   newest-`main` fallback is labelled, not exact). *Check:* `index.json`'s
   `main.sha` equals `origin/main` after each publish.

### 1d. Risks, reversibility, decisions

**Risks.** (i) Steps 3-4 are reversible (nothing leaves `main`); step 2 adds
~3,608 files to `main`; step 6 is reversible only by `git revert` while the
commit exists. (ii) First-write-stands means a mistaken publish for a commit
cannot be corrected under the same key — use a new commit. (iii) Readers that
fall back to the newest `main` entry can read verdicts against a different
corpus commit; hash freshness (`source_hashes`) mitigates but `qa-sweep`
freshness is per-criterion. (iv) CI is dispatch-only (AGENTS.md billing
directive), so "per commit" publishing depends on an agent or a manual dispatch —
qou may have long stretches with no `main/<sha>` entry, and every reader must
treat that as unknown, not clean. (v) The branch grows by a tree per published
commit; blobs dedupe, and `qa:prune` exists.

#### Q1 — What does "QA is in qa-reports" mean for the judgement half?

- **A. Platform split (D2(a)).** *Means:* the full `block-qa/v1` reports (with
  their judgement projection) go to the branch; the 126,315 agent/human verdicts
  are also kept on `main` in `test/attestations/block-qa/`. *Costs:* ~3,608 new
  files on `main` (smaller than today's 3,653 because script entries leave);
  steps 2-5. *Risks:* two copies of a judgement until readers stop using the
  projection; the platform owns that reconciliation (`resolvePrior`). *Commits
  to:* the platform convention every other instance follows; judgements survive a
  `git rm` of derived results.
- **B. Everything on the branch, nothing on `main`.** *Means:* agent and human
  verdicts exist only in `main/<sha>` entries. *Costs:* step 2 skipped.
  *Risks:* the platform's reason for D2(a) is measured — deleting the derived
  tree re-baselined judgements, findings 13 → 0 (`qa-attestations.ts:15-21`); a
  regeneration cannot recreate an agent's reading of a block. It also diverges
  from every platform reader. *Commits to:* a qou-only layout.
- **Default if no answer:** nothing moves; the split-brain in 1b persists.
- **Recommendation (judgement):** A. "QA in qa-reports" is satisfied for
  everything a script can regenerate; the judgements are the expensive part and
  the platform keeps them on `main` for a measured reason.

#### Q2 — The 128 entries with no `reviewer.kind`

*Means:* they are neither `script` nor a typed judgement; the migrator treats
"not script" as a judgement, but `CriteriaAttestationsSchema` may refuse an
untyped reviewer. *Options:* (a) classify by hand (128 entries, ~an hour), (b)
treat as `agent`, (c) leave them in the derived report only. *Default:* the
migrator decides, possibly by refusing — step 2 stops. *Recommendation
(judgement):* (a); it is small and it is the same call bean `qou-6ccl` already
lists as needing a ruling.

#### Q3 — When do the 3,653 sidecars leave `main`?

- **A. After steps 2-5 and an IDENTICAL verify (recommended, judgement).**
  *Costs:* the reader migration (~13 code sites, 24 skills, AGENTS.md).
  *Risks:* lowest. *Commits to:* `test/results/` being a working copy that must
  be fetched before reading.
- **B. Never — keep them on `main` and only also publish.** *Means:* the branch
  is a mirror. *Costs:* step 4 only. *Risks:* the split-brain stays unless the
  writers are migrated anyway, and two locations can disagree.
- **Default:** B in effect (nothing is removed without a ruling — §ASK THE OWNER).

#### Q4 — Who publishes `main/<sha>`?

*Options:* (a) extend `compute-qa.yml` to also stage block-qa and publish once,
still dispatch-only; (b) an agent-run publish from a container after merges;
(c) re-enable a push trigger (contradicts the 2026-06-30 billing directive).
*Default:* (a)/(b) do not happen on their own; readers fall back to the newest
entry. *Recommendation (judgement):* (a) plus (b) as the documented manual path,
since a second publisher for the same key loses.

---

## 2. Move 2 — beans branch-mounted

### 2a. The platform's canonical layout

**Declaration** (platform `cat-harness/cat-harness.json:914-933`):

```json
{ "id": "beans", "path": "beans/", "scope": "repository",
  "graphTypologies": ["beans"],
  "source": { "kind": "branch", "branch": "cat/cat-harness/beans", "keyedBy": "tip" } }
```

`scope: "repository"` entries are **not inherited** by dependents
(`cat-harness/schemas/cat-harness.ts` ~4815: skipped unless `own`), so qou does
not get this from the platform; it must declare its own. qou's `qou.json`
declares no `beans` directory today; only `beans/beans.json` (the inner
`defs` node) and `.beans.yml` exist.

**Branch layout** (`cat-harness/scripts/branch-store.ts:30-45`), as on the
platform today (fetched):

```
cat/cat-harness/beans   tip 6848e5d8, 2026-10-10   (1,790 files)
├── README.md
├── manifest.json   state-manifest/v1, status active, authoritative: true,
│                   keyedBy tip, graphs: [{path: beans, tree: aa807ab…, files: 1783}]
└── beans/{beans.json, defs/ (632 under defs/archive), notes/, queue/, surveys/, workflows/}
```

Platform `main` has **no** `beans/` at all; `.gitignore:251-254` ignores
`/beans/**` so a mount is never committed. `.beans.yml` stays on `main`
(`path: beans/defs`) because the third-party `beans` CLI reads only that file.

**Naming for a folio.** `instanceStateBranch(instance, id) = cat/<instance>/<id>`
(`cat-harness/schemas/subgraph-source.ts:336-338`), the rule
`directory-conventions.md:890-899` owns: e.g. `cat/dpi-h-ra/beans`. For qou that
is **`cat/qou/beans`**. Note the inconsistency already on qou's remote: a sibling
session today (2026-10-10 13:27) seeded `cat/cat-harness/fsh-guts` on qou (seed,
`authoritative: false`), not `cat/qou/fsh-guts`; and `qa-reports` is a fixed name
(`QA_BRANCH`) for every instance. See decision B1.

**Mount at session start.** Platform `.claude/settings.json:9` runs
`cat-harness/scripts/session-start-coord-sweep.sh`, whose §3.5 (lines 517-546)
runs `mount-from-lock.ts` then `state-mount.ts`. `state-mount.ts` fans out over
every tip-keyed declared directory and calls `mountTip` for each
(`state-mount.ts:56-90`): plain files at the declared path (bytes, modes,
symlinks round-tripped), a marker in `<git-dir>/branch-mounts/<id>.json`. Every
failure is loud — it prints that an empty `beans list` must not be believed, and
exits non-zero. A mount holding unpushed edits is left alone and reported
`stale`.

**Writes.** `branch-store.ts push --id beans` (`pushMount`, :1223-1241):
local edits are spliced onto the tip with `expect` = the blob mounted; the push
never forces; on rejection it rebuilds on the new tip (3 attempts). Two writers
of the **same file** → `conflict`, nothing pushed, caller re-reads. `beans:claim`
(`claim-bean.ts:328-420`) writes the claim **directly to the branch** with
`expect` when beans are branch-kept, so a claim is visible to sibling sessions
immediately — the `35nj` defect (two sessions claimed one bean 61 s apart) is
closed by construction.

**Does the `beans` CLI work against it?** Yes, by design: the mount is ordinary
files at `beans/defs`, and `.beans.yml`'s `path: beans/defs` is unchanged. The
platform documents the end-to-end check *"init, seed, mount, `beans create`,
`branch-store push --id beans`, `beans:claim`"* on a fresh repo with a bare remote
(`directory-conventions.md:925-927`). The CLI itself never pushes — a
`beans create`/`update` is lost if the session ends before `push --id beans`.

### 2b. qou readers and writers of `beans/defs`, and what breaks

**Hooks and scripts:**

| file | effect after cutover |
|---|---|
| `scripts/session-start-coord-sweep.sh:69-98` (SessionStart) | reads `beans/defs/*.md` directly; with no mount step it prints **no active beans** — the empty-vs-unreachable failure the platform's mount exists to prevent. Must call `state-mount` before §4b. |
| `scripts/precommit-bean-id-warn.sh:49-65` (PreToolUse) | keys on `git status -- beans/defs`; an ignored mount shows nothing → silently inert. |
| `scripts/prebranch-bean-loss-warn.sh` (PreToolUse) | exists because branch switches change `beans/defs` in the worktree; after cutover beans are not in git → obsolete. |
| `scripts/bean-append-merge.py` | resolves git conflict markers in `beans/defs/*.md` at merge time; obsolete (no merges of bean files). |
| `scripts/check-beans.sh`, `bean-completion-candidates.py`, `bean-dangling-path-audit.py`, `bean-declaration-audit.py`, `bean-staleness-triage.py`, `bean-status-outlier-triage.py`, `pqmw-queue-recheck.py`, `resweep-placeholder-beans.ts`, `stale-audit-discriminator.py`, `migrate-uploads-to-library.py`, `known-constant-literal-audit.py`, `pn-convention-audit.py`, two `computations/` audits | read files at `beans/defs`; work if mounted, read empty if not. `git log -- beans/defs` history-based ones lose history after the cutover commit. |
| `scripts/install-beans.sh` | unchanged. |

**Rules:** AGENTS.md cites `beans/defs` at 10 sites (573, 591-592, 770-773,
1918, 5987-5988), including corpus-grep **path 6** (`grep -rl <topic> beans/defs/`),
the bean-append collision note, and the watcher queues
(`beans/defs/*-queue.json`, 13 non-bean files that would move with the graph).
One skill references `beans/defs` and 6 skills use `beans create|update|list`.

**The behavioural change that matters most: bean edits leave pull requests.**
Today a bean edit is a commit in a PR and lands on merge — which is why
**61 of the last 113 `main` commits** touch `beans/defs` and why AGENTS.md
records `qou-brng` conflicting three times in forty minutes. After cutover a
bean edit is a direct push to `cat/qou/beans`: visible immediately, never in a
PR diff, never merge-conflicted. Concurrent appends to one bean become a
`conflict` the second writer must re-read and retry (the CLI's file write is
not itself conflict-aware; only the push is). Open PRs that carry bean edits at
cutover time will conflict with the `git rm` and must re-apply those edits to the
branch — **not measured** (needs `gh pr list --json files`, which failed
unauthenticated here; the MCP route works per PR).

### 2c. Migration steps (ordered), each with its check

0. **Bump the platform pin** to ≥ `283ba67e76` (2026-10-08): `state-seed.ts` at
   the pin has no `--cutover` and no `--repo-root` (grep count 0 vs 12 on main),
   and before `hp54` it defaulted to the platform checkout, i.e. it would refresh
   the **platform's** branch. Same layer-mount caveat as 1c step 1. *Check:* as 1c
   step 1, plus `bun run cat state:seed --help` shows `--cutover` and
   `--repo-root`.
1. **Declare** in `qou.json`:
   `{ "id": "beans", "path": "beans/", "scope": "repository", "graphTypologies": ["beans"], "source": { "kind": "branch", "branch": "cat/qou/beans", "keyedBy": "tip" } }`,
   and declare `fsh-guts` with a branch source too (the cutover refuses unless the
   instance's own `fsh-guts` is kept at a branch tip). *Check:*
   `bun run folio-assistant/cat-harness/scripts/branch-store.ts where --id beans`
   resolves to the branch; `check:declared-dirs` clean.
2. **Seed** the orphan branch by hand — *"No platform command creates a new
   state branch … seeding is a steward act"* (`directory-conventions.md:906-924`):
   a commit holding `manifest.json` (`state-manifest/v1`, `keyedBy: tip`,
   `authoritative: false`, `graphs: [{path: beans, tree: <HEAD:beans>}]`),
   `README.md`, and `beans/` = `HEAD:beans` (both `beans.json` and `defs/`;
   `beans:claim` refuses without `beans.json`). *Check:* branch `beans` tree id ==
   `git rev-parse origin/main:beans`.
3. **Freeze and refresh.** Announce a bean-write freeze on `main`; then
   `state:seed --id beans --repo-root .` to bring the seed to `main`'s current
   tree. *Check:* tree ids equal again (the cutover re-checks this).
4. **Make the branch authoritative:** `state:seed --id beans --authoritative`.
   *Check:* `branch-store.ts read --branch cat/qou/beans manifest.json` shows
   `authoritative: true`.
5. **Cut over `main`:** `state:seed --id beans --cutover` (dry run: files, bytes,
   deposit), then `--commit`: deposits a tar of `beans/` at `HEAD` into
   `fsh-guts` (`retired/cutover-qou-beans-<tree12>.tar.gz` + `.md`), verified to
   extract to the same tree id; then one commit `git rm -r beans` +
   `/beans/**` in `.gitignore`. It never pushes `main`. *Check:* the deposit
   re-reads; `git ls-files beans | wc -l` = 0; `.beans.yml` still present.
6. **Mount and wire the session:** add `state-mount` to
   `scripts/session-start-coord-sweep.sh` before §4b and print its failure loudly.
   *Check:* fresh worktree → `bun run cat state:mount` → `ls beans/defs | wc -l`
   equals the seed's count; `beans list` non-empty; `beans create` + `branch-store
   push --id beans` → `pushed`; a second worktree editing the same bean →
   `conflict`.
7. **Migrate rules and tools:** AGENTS.md (10 sites) and the 7 skill files to
   "edit, then `push --id beans`"; retire `bean-append-merge.py` and
   `prebranch-bean-loss-warn.sh`; re-key `precommit-bean-id-warn.sh` on the
   mount; keep the `check before create` rule (the CLI is still not idempotent).
   *Check:* each hook's own self-test where it has one; a session-end check that
   `pendingMountChanges("beans")` is empty.

### 2d. Risks, reversibility, decisions

**Risks.** (i) Unpushed bean edits are lost when a container is reclaimed —
today they at least sit in a commit on a feature branch. (ii) A session whose
mount failed and that ignores the loud block reads an empty work plan. (iii)
Bean history (`git log -- beans/defs`) on `main` ends at the cutover; history
continues on the branch. (iv) Reversible: the branch holds the tree and
`fsh-guts` holds a verified pack, so restoring `beans/` to `main` is a
checkout of either plus removing the ignore line; the reverse of step 5 is one
commit. (v) The `todos/`-style ignore means a mount can never be committed by
accident, which also means a bean edit cannot ride along with the work that
motivated it.

#### B1 — Branch name

- **A. `cat/qou/beans`** — the documented folio convention
  (`instanceStateBranch`, `folio_init`). *Costs:* none extra. *Risks:* qou's
  remote then has two prefixes (`cat/cat-harness/qa-reports`,
  `cat/cat-harness/fsh-guts` and `cat/qou/beans`). *Commits to:* the platform's
  rule for every future qou state graph (`todos`, `fsh-guts`).
- **B. `cat/cat-harness/beans`** — matches the platform repo's name and the
  fsh-guts seed made today. *Risks:* contradicts `directory-conventions.md`;
  any platform tool that composes the name from the instance computes
  `cat/qou/beans` and must be overridden by the declaration everywhere.
- **Default:** whatever the declaration says; nothing is created until then.
- **Recommendation (judgement):** A, and re-seed `fsh-guts` as
  `cat/qou/fsh-guts` before its cutover so qou has one prefix for its own state
  (`qa-reports` stays as is: its name is a platform constant).

#### B2 — Do beans leave PR review?

*Means:* bean edits stop appearing in PR diffs and on `main`; they go straight
to the branch. *Costs:* AGENTS.md's workflow text, 7 skills, 4 hooks.
*Risks:* (i) above; reviewers lose the bean diff beside the code. *Commits to:*
the platform's model, and it removes the measured bean-append merge collisions
(AGENTS.md: four of five collision surfaces in one cluster were two bean files).
*Default:* beans stay on `main`, collisions continue. *Recommendation
(judgement):* yes — it is what "branch mounted" means, and the collision cost is
measured while the review loss is mostly bookkeeping.

#### B3 — Freeze window and open PRs carrying bean edits

*Options:* (a) announce a short freeze, cut over, and have each open PR
re-apply its bean edits with `push --id beans`; (b) cut over and let the
`git rm` conflicts surface at each PR's next rebase. *Default:* (b) by
accident. *Recommendation (judgement):* (a); first measure how many open PRs
touch `beans/defs` (not measured here).

---

## 3. Sequencing across the two moves

Both need the same pin bump (to post-2026-10-08 platform main, with remote
layer mounts), so do that once, first, as its own PR with before/after
`run-validate` counts. Then beans (smaller: one graph, platform has done it,
mechanical cutover command exists) and QA (larger: reader migration plus
judgement split). The QA split-brain in 1b is live **now** and is worth a
narrow fix independent of either move: either stop running `qa-sweep` on qou
until the migration, or move the qou writers to `blockQaPath` + attestations
(step 5) first.

## 4. Out of scope, flagged

- 1,798 `*.script-qa.json` (14.2 MB) under `computations/` are QA too and are
  not addressed by either ask.
- Three qou QA scripts (`qa-evidence-provenance-gate.py`,
  `qa-stale-agent-evidence.py`, `reaudit-proof-deterministic.py`) already read
  nothing because they glob `content/**`.
- Bean `qou-6ccl` (`[CONTENT C4] Split the 3,653 sidecars`, `todo`,
  `needs-owner`) and `qou-4rhu` (S3, `in-progress`) already scope move 1; this
  document is the measured detail for them, not a new tranche.
