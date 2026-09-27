---
# qou-i2ed
title: 'LATENT: the lean.ref package registry is never configured in production, so 8 lookup sites can never resolve — masked today because every block also has a sibling .lean'
status: todo
type: bug
created_at: 2026-09-27T05:54:25Z
updated_at: 2026-09-27T05:54:25Z
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
