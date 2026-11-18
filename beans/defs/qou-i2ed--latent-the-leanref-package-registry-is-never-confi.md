---
# qou-i2ed
title: 'LATENT: the lean.ref package registry is never configured in production, so 8 lookup sites can never resolve — masked today because every block also has a sibling .lean'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-27T05:54:25Z
updated_at: 2026-10-04T15:15:44Z
parent: qou-5vkl
---


## 2026-09-27 — measured on platform pin `37a36ce9296`; sibling of `qou-7ko6`

Found while measuring where the theorem/proposition/proof schemas live. **This
is a latent defect, not a live one — say so when quoting it.**

### The mechanism

`cat-harness/schemas/lean-packages.ts` holds the `lean.ref` grammar
(`package:Declaration`) and a registry of which packages exist. Until
2026-09-18 it shipped `DEFAULT_LEAN_PACKAGES = [qou, ugb, fred2005]` hardcoded
at import — one folio family's data in the platform — and that default was
**correctly removed**. Its own docstring records the replacement contract:

> *"a folio injects those with `configureLeanPackages`"*
> *"**Unconfigured is not empty.** The registry starts empty and stays empty
> until a folio configures it, and those two states are different facts:
> **nobody has said** is not **there are none**. `leanPackagesConfigured` is
> how a caller tells them apart, so a pipeline can report 'not checked' rather
> than silently skipping every library-tree `lean.ref` and looking clean while
> doing so."*

### What is actually true

Measured across the whole platform tree, excluding `node_modules`:

| claim | measured |
|---|---|
| `configureLeanPackages` callers in production | **0** — the only call is `cat-harness/scripts/tests/lean-ref-coverage.test.ts:62` |
| `leanPackagesConfigured()` callers anywhere | **0** — the function the docstring calls the whole point of the design is dead |
| any config key read for the package list | **0** — `grep leanPackages` across `cat-harness/**/*.ts` returns only its own definition and its own docstring; no `.json` in qou declares one either |
| production sites calling `leanPackageByName(...)` | **8** |

So `LEAN_PACKAGES` is `[]`, `leanPackageByName("qou")` is `undefined`, and
`isLeanPackageName("qou")` is `false` in **every real run**. The docstring's own
explanation of why the default existed — *"keeping it here as a default
unbreaks the pipeline **without a config-discovery mechanism**"* — names the
missing half exactly: the default was removed and the mechanism was never
built. Same shape as the q₀ manifest split AGENTS.md records: *"land them
together or not at all."*

### The 8 sites split TWO WAYS, which matters

- **Fails closed** — `schemas/constraints.ts:734`, rule `definition-lean-exists`.
  With `pkg === undefined` both Lake-tree resolution paths are skipped and it
  falls through to *"Definition X requires Lean formalization"*. A **false
  positive** on exactly the blocks AGENTS.md §0a tells you to author *without* a
  sibling (*"no shadowing stubs"*).
- **Fails open** — `content/pipeline/conjectural-propagation-audit.ts:156`,
  `if (!pkg) return false;` inside `isClassAxiomatised`. Reports "not
  class-axiomatised" for any conjecture whose class lives only in the library
  tree, so its downstream conditional theorem lands in `violators` instead of
  `conditional_on_class` (§3b-cond). Also a false positive, one layer up.
- Six more: `qa-utils.ts:658`, `conditional-class-banner-audit.ts:148`,
  `export-json.ts:138`, `adapters/mcp-server/server.ts:355` and `:368`,
  `adapters/document/resolver.ts:417` and `:429`. Not individually triaged.

### Why it bites NOTHING in qou today — the honest negative

Both consequential paths are reached only when a block has a `lean.ref` and
**no** sibling `.lean`. Measured over `content/`:

```
blocks with a lean.ref                                          1306
definition blocks with a lean.ref and NO sibling .lean             0
conjecture blocks with a lean.ref and NO sibling .lean             0
```

Every relevant block has a sibling, so path (a) succeeds and the registry is
never consulted. **The defect is latent.**

And the thing masking it is itself a deviation: AGENTS.md §0a says a sibling
`.lean` must **not** exist when the real declaration lives at
`<lakeRoot>/<Decl/Path>.lean`, because a trivial sibling *shadows* it. The
corpus is currently in the state §0a says it should not be in, and that is
precisely what keeps this registry's emptiness invisible. **Draining the
shadowing stubs would make this defect live.** So the two items are coupled and
should not be worked in either order blind.

### Options

1. **Build the config-discovery mechanism** in the platform — a `leanPackages`
   array in `<name>.config.json`, read once at pipeline start, passed to
   `configureLeanPackages`. *Costs:* platform PR + a pin bump here + a
   `leanPackages` block in qou's config declaring `qou`/`ugb`/`fred2005` with
   their `lakeRoot`s. *Risks:* turns 0 false positives into 0 false positives
   today — the value is entirely in not breaking when §0a is enforced.
2. **Give the 8 sites the guard the docstring promises** — have each report
   *"not checked"* via `leanPackagesConfigured()` instead of silently taking
   the `undefined` branch. Cheaper, no config surface, and it makes the
   emptiness *visible* rather than fixing it. Complements 1; does not replace it.
3. **Re-add a default** — rejected; that is the genericity failure the
   2026-09-18 change correctly removed.
4. **No-op** — nothing changes, and nothing breaks until the shadowing-stub
   drain lands.

**My judgement, not a finding:** **2 then 1** — wire the guard first, because
it converts a silent wrong answer into a loud "unconfigured", which is the
thing the module was designed to be able to say and currently cannot. Doing 1
first fixes the symptom while leaving eight sites that would go quiet again the
next time a folio forgets to configure.

**Default if nothing is decided:** nothing breaks today. The 1,306 `lean.ref`s
keep validating against `LEAN_REF_PATTERN` (a regex, which does work) and never
against the package registry.

**Blast radius.** All 8 sites are in the **platform repo**
(`litlfred/folio-assistant`), pinned here at
`.folio-assistant-pin` = `37a36ce9296b95a9ad4862d51dc496ac44053143`. Two of
them are load-bearing for qou's own review discipline:
`definition-lean-exists` is what `scripts/check-sidecars.sh` leans on, and
`conjectural-propagation-audit.ts` is what enforces AGENTS.md §3b-cond —
the rule separating a rigorous conditional result from an unproved conjecture.


---

## 2026-09-27 (later the same day) — 🛑 THIS BEAN WAS WRONG IN BOTH DIRECTIONS, and both corrections are mine

Measured with [`/tmp` probe recorded below] against qou `main` content and the
platform branch `claude/sci-owns-lean-grammar-probe-2026-09-27`:

```
distinct lean.refs in content/ : 1301
resolved with NO layer          : 0
resolved WITH layer installed   : 745
  unchanged 556  gained 745  lost 0  moved 0
```

### Correction 1 — the title's "0 callers in production" is FALSE

`configureLeanPackages` has **two** production callers. They are in **this**
repo, not the platform:

- `scripts/preload-registry.ts:25`
- `scripts/run-validate.ts:27`

Both pass `LEAN_PACKAGES` from qou's own `schemas/lean-packages.ts`, which is
exactly the contract the platform docstring describes (*"a folio injects those
with `configureLeanPackages`"*). The original measurement was
`grep configureLeanPackages` **across the platform tree**, and it reported an
absence there as an absence everywhere — the same error class as the `publish.yml`
retraction on `qou-9olr` / `qou-w5av` the same morning, in a different tree.
**`leanPackagesConfigured()` having zero callers is unaffected and still true.**

### Correction 2 — and it is the sharper one: "LATENT, masked" understates it

For every pipeline reached through those two entry points, the registry IS
configured and resolution works. But **three consumers call
`resolveCanonicalLean` while configuring nothing at all**, verified by reading
their imports:

| consumer | configures? |
|---|---|
| `scripts/check-base-ring.ts` | **no** |
| `scripts/check-wall-side.ts` | **no** |
| `content/pipeline/qa-agent-entry.ts:128` | **no** |

In those three, resolution is not degraded — it is **total**: `0 of 1301`. The
mechanism is provable from the code rather than merely measured: `byName` is
empty until `configureLeanPackages`, so `leanPackageByName` returns `undefined`
and `resolveCanonicalLean` returns at its first branch. That argument holds
identically at pin `37a36ce9296`, so this is not an artifact of the branch the
745 was measured on.

So: **latent for the validator and the sweep; live and complete for those three
checkers.** Say which, and never quote this bean's title.

### What that costs, and what is NOT established

`check-wall-side.ts`'s own header states the stake: a checker that *"scores a
different file from the sweep it is meant to reproduce is worse than no checker
script"*, citing 77/1191 blocks mis-resolved onto import-only aggregators and
*"reporting PASS on live fails"*. Unresolved refs put these three on the sibling
`.lean` instead of the library declaration named by `lean.ref` — and per
AGENTS.md §0a a sibling may legitimately be a `True := trivial` shadow stub.

**NOT measured, and needed before quoting a verdict impact:** how many of the
745 have a sibling `.lean` at all. With a sibling, the script scores the wrong
file; without one, it skips. Those are different failure modes and only the
count separates them.

**Also unexplained: 556 refs resolve to nothing even WITH the layer installed**
(43 % of the corpus). Some of that is `qou-cu0a` working as designed — a ref
naming a decl that exists nowhere correctly returns `undefined` rather than the
library root. How much is its own question.

### Status

Stays **open**. The fix is two lines per consumer and it is gated on the
platform pin advancing past `folio-assistant#…` (the `formal-ref` injection
point), because after that commit the layer must be *installed*, not merely
configured — see `qou-7ko6`. Mechanism made audible in the meantime:
`schemas/formal-ref.ts` now emits a one-shot stderr warning when anything
resolves against no installed layer, which is what printed above the numbers in
this very measurement.
