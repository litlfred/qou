---
name: lean-environment-setup
roles: [collaborator, owner]
description: >
  Sets up and troubleshoots the Lean 4 environment for Claude Code sessions.
  Ensures elan, lake, lean are installed so the paper-assistant MCP's Lean
  tools are operational. Handles sandboxed/cloud environments where downloads
  may be restricted.
allowed-tools: Read Edit Bash Grep Glob
---

# Lean Environment Setup

## ⮕ FAST ROUTE — read this BEFORE declaring Lean "unavailable"

> On **any** Lean env/tool failure — `lean_run_code`/LSP "no valid project
> path", `leansearch` SSL error, `lake exe cache get` 403, `elan toolchain
> install` SSL/`failed to parse release data`, empty `~/.elan/toolchains/`,
> `lake build` timeout — **do NOT conclude "Lean is unavailable."** Several of
> these (cache-403, toolchain-host-firewalled, leansearch/loogle SSL) have
> **documented workarounds in this very file** (§"Mathlib cache 403 fallback"
> + §"Web-sandbox addendum" + §"Offline Mathlib search"). The recurring
> failure mode is *agents re-deriving these
> workarounds — or giving up — instead of grepping for them.*
>
> **Discipline (generalises the corpus-grep / formalize-first rules):** when a
> tool or environment operation fails, FIRST
> `grep -ri "<error keyword>" .claude/skills/ CLAUDE.md docs/` (e.g. `release.lean-lang.org`,
> `cache get 403`, `insteadOf`, `elan toolchain`) **before** declaring the
> capability unavailable. Only after the documented workarounds are tried and
> hit a *hard* network block may you fall back to a rigorous hand-audit — and
> then say so explicitly (per the §"Web-sandbox addendum" bottom line).
>
> **If the install is long/uncertain, DELEGATE it to a sub-agent** (see
> §"Delegate the install to a sub-agent" near the foot of this file) so the
> main task is not blocked on a multi-minute toolchain fetch + mathlib build.

## Architecture

All MCP functionality — including Lean tools — is served through a single
`paper-assistant` MCP server (`./scripts/start-folio-assistant.sh`). There is
**no separate lean-lsp MCP entry**. The paper-assistant detects lean/lake
on the PATH and enables Lean tools automatically.

## When to Use This Skill

- At session start when the Lean build status (`/tmp/qou-lean-build-status.json`,
  written by `setup-lean-toolchain.sh` / `lean-build-bg.sh`) reports Lean as unavailable
- When paper-assistant Lean tools fail with "No such file or directory: 'lake'"
- When a user says "set up Lean" or "install Lean"

## Prerequisites

The paper-assistant's Lean tools require these on the PATH:

1. **elan** — Lean toolchain manager (`~/.elan/bin/`)
2. **lean** — the Lean compiler (installed via elan)
3. **lake** — the Lean build tool (installed with lean)
4. **uv** — Python package manager (optional, for uvx-based tools)
5. **ripgrep** — for local symbol search (optional)

## Setup Procedure

### Step 1: Check current state

Use the `lean_status` MCP tool. It reports the current mode
(local/remote/local-degraded/none) and what's missing.

### Step 2: Install Lean toolchain

Use the `lean_setup` MCP tool. It handles the full installation:
elan, lean, lake, uv, ripgrep, lake update, Mathlib cache, and build.
Safe to re-run — skips already-installed components.

If `lean_setup` fails (e.g., 403 errors from network restrictions in
sandboxed environments), proceed to Step 3.

### Step 3: Diagnose network restrictions

In sandboxed/cloud environments (GitHub Codespaces, Claude Code cloud,
CI runners), outbound HTTPS to `github.com` or `raw.githubusercontent.com`
may be blocked. Test:

```bash
curl -sSf --max-time 5 https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /dev/null && echo "OK" || echo "BLOCKED"
curl -sSf --max-time 5 https://github.com/leanprover/lean4/releases -o /dev/null && echo "OK" || echo "BLOCKED"
```

If blocked, local Lean installation is impossible. Inform the user that
Lean tools require running Claude Code locally where lean/lake are installed.

### Step 4: Verify Lean tools via paper-assistant

After setup, verify with the `lean_status` MCP tool. If mode is
`local`, Lean is fully operational.

## Docker-based setup (offline)

If the paper-assistant Docker image is available, all tools (Lean, TeX,
Bun) are pre-installed and ready to use without any network access:

```bash
# Pull once (requires network)
docker pull ghcr.io/litlfred/qou/paper-assistant:latest

# Run with repo mounted — full toolchain available
docker run --rm --entrypoint "" \
  -v $(pwd):/work -w /work \
  ghcr.io/litlfred/qou/paper-assistant:latest \
  bash -c "lean --version && lake --version && pdflatex --version | head -1"
```

The render hooks (`render-on-change.sh`, `render-pre-commit.sh`) auto-detect
Docker and use the image as a fallback when local tools are missing. See
`scripts/lib/docker-tex.sh` for the helper library.

## Fallback: Structural Analysis Without Lean

When Lean is not installed, agents can still:

- Read `.lean` files with the Read tool
- Search for `sorry` with Grep
- Validate content object schemas via `paper-assistant` MCP
- Check cross-references between `.ts` manifests and `.lean` files
- Verify naming conventions (label → declaration mapping)
- Audit `status` fields against file contents

What agents **cannot** do without Lean:

- Type-check proofs
- Get goal states at positions
- Search Mathlib via the hosted leansearch/loogle services — but the
  **offline grep substitute** below works with or without Lean (see
  *Offline Mathlib search*)
- Verify axiom dependencies
- Get autocompletions or hover info

### Offline Mathlib search — when hosted leansearch/loogle are SSL-blocked

In the Claude Code web sandbox the hosted search services
(`loogle.lean-lang.org`, `leansearch.net`) fail with
`SSL: CERTIFICATE_VERIFY_FAILED` (self-signed cert in the proxy chain), so
the `lean_loogle` / `lean_leansearch` MCP tools error out. Use these
**offline** substitutes — they need no network:

1. **Grep the Mathlib source** (closest analogue to a loogle name/substring
   search; works *with or without* Lean installed). The full source ships
   with any clone and with the `lake-cache/*` restore — ~7 000 `.lean` files
   under `.lake/packages/mathlib/Mathlib/`:
   ```bash
   grep -rn "theorem det_succ_row_zero" .lake/packages/mathlib/Mathlib/
   grep -rn "det_fin" .lake/packages/mathlib/Mathlib/LinearAlgebra/Matrix/
   ```
2. **`lean_local_search` (MCP)** — offline; searches declarations in the
   current project + imported modules (once a file is loaded).
3. **`lean_hover_info` / `lean_declaration_file` (MCP)** — offline once a
   file is loaded; type signature / source of a known name.

**Why not run loogle locally?** loogle is a Lean exe that imports and indexes
*all* of Mathlib, so it needs Mathlib oleans for **its own** toolchain.
loogle HEAD pins a newer toolchain (e.g. `v4.30.0-rc1`) than the repo cache
(`v4.24.0`), and `lake exe cache get` is network-blocked here — so standing
up local loogle means a from-source Mathlib rebuild (~30–60 min) that
**cannot reuse** the `lake-cache/*` oleans (they are Mathlib-commit-pinned;
even a v4.24 loogle commit would need the repo's *exact* Mathlib commit).
Not worth it for ad-hoc search — the grep route answers the same questions
in seconds.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| "No such file or directory: 'lake'" | lean not on PATH | `export PATH="$HOME/.elan/bin:$PATH"` or install elan |
| elan install 403 | Network restrictions | Run Claude Code locally where lean is installed |
| "lake update" hangs | Git fetch blocked | Check `git ls-remote` works for mathlib4 |
| Lean tools timeout | Workspace not built | Run `lake build` at the **repo root** (root workspace builds all paper packages) |
| **`lake exe cache get` → 403 on all shards (7335+ failures)** | **Mathlib cache host blocked from this network** | **See "Mathlib cache 403 fallback" below — clone mathlib source locally + git insteadOf** |
| **`lean_diagnostic_messages` MCP times out at 60s** | **No prebuilt oleans + cache 403** | **Same fix as cache 403 above — local clone unblocks LSP** |
| "toolchain not installed" | Wrong lean version | `elan toolchain install $(cat lean-toolchain)` from the repo root |
| paper-assistant shows `✗ lean` | lean not on PATH | Add `$HOME/.elan/bin` to PATH in shell profile |

## Mathlib cache 403 fallback (proven workaround, 2026-06-03)

**Symptom.** In sandboxed cloud environments (Claude Code on the web,
GitHub Actions billing-blocked, etc.), `lake exe cache get` returns
403 forbidden on every mathlib oleans shard (typically 7335+ download
failures), and `lean_diagnostic_messages` MCP times out at 60 s
because no prebuilt oleans are available.

The CLAUDE.md "Local Mathlib cache" section documents the *intent*
that the build tools auto-detect a clone at `../mathlib4`, but in
practice the auto-detection requires manual git redirect setup when
elan / cache hosts are network-restricted.

> **⚡ FIRST RESORT — restore prebuilt oleans (≈2 min). Do NOT build from
> source until you have tried this.** A full build is already preserved on
> the orphan branch `lake-cache/qou-v4-24-0` (lean `v4.24.0`); restoring it
> skips the 30–60 min from-source Mathlib build entirely. **This is the
> single most common wasted hour for agents in this repo** (the from-source
> sections below are a *fallback*, not the default). RESTORE before anything
> else:
>
> ```bash
> # Derive the cache branch from the pinned toolchain — do NOT hard-code the slug
> # (works from any subdir; CRLF-safe):
> ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
> SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
> BR="lake-cache/qou-$SLUG"
> git fetch --depth=1 origin "$BR" \
>   && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
>      | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
>   && tar xzf "$TGZ" -C "$ROOT" \
>   && echo "restored .lake oleans from $BR — NO rebuild needed"
> ```
>
> The `SLUG` line derives the branch from the pinned toolchain so it never goes
> stale (`leanprover/lean4:v4.24.0` → `lake-cache/qou-v4-24-0`); the tarball
> goes to a `mktemp` file and extracts with `-C "$ROOT"` (repo root), not the
> current directory. Full restore/seed details (incl. how to **SEED** after a
> fresh build) are in the **🗄️ PRESERVE THE BUILD** section further down this file.
> Only if the fetch fails (branch unseeded) or the oleans are a
> toolchain/`lakefile.toml` **miss** do you fall back to the source-clone +
> from-source build below — and **SEED the cache branch afterwards** so the
> next agent restores in 2 min instead of rebuilding.

**Fallback workaround — source clone + from-source build (only when the
cache-branch restore above misses; battle-tested on PR #1761 + PR #1772):**

```bash
# Step 1: Clone mathlib source locally (shallow OK, ~144 MB).
cd .. && git clone --depth 1 https://github.com/leanprover-community/mathlib4.git
cd -

# Step 2: Set a global git insteadOf so Lake's mathlib fetches go to
# the local clone instead of the network.
git config --global url."file:///home/user/mathlib4".insteadOf \
  "https://github.com/leanprover-community/mathlib4"

# Step 3: Verify by running an LSP query on a mathlib-importing file.
# The first query will still be slow (cold workspace) but should
# return real diagnostics rather than timing out.
```

After Step 3 succeeds, `lean_diagnostic_messages` returns real error /
warning items (not the `success: false, items: []` timeout sentinel),
unblocking iterative Lean proof development.

**Why this is the right diagnostic step.** Without LSP feedback, blind
proof iteration is the c_3-flip-flop trap — agents push speculative
"plausible" proofs that fail to compile, and the trust-but-verify rule
forces reverts. The local mathlib clone is the cheapest path to a warm
LSP when the cache is unreachable.

**History.** Captured 2026-06-03 after PR #1761 (general H_n lift of
T_β = S·1) iterated proofs for ~10 turns with sorry-scaffold-and-revert
before this workaround was applied; once LSP was warm, the LSP
diagnostics caught 4 real bugs (LinearOrderedField deprecation,
h_smul_one_sq rewrite-chain failure, h_tau_expand brittle ordering,
linear_combination sign error) within 3 turns and the proofs became
sorry-free. The same pattern is being tracked in PR #1763 (axiom
tractability triage) where the cache-host blocker is a recorded
blocker.

### Build-from-source path (when you don't need iterative LSP)

If your task is **bulk diagnostics regen** or **one-shot
build-everything**, the local clone + `git insteadOf` above is
sufficient — you don't need the cache at all. `lake build` happily
compiles Mathlib from source; it's just slower.

```bash
# After Steps 1-2 above (clone + insteadOf):
nohup lake build QOU > /tmp/lake-build.log 2>&1 &
# Monitor:
tail -f /tmp/lake-build.log
# Or sample progress:
grep -c '^✔' /tmp/lake-build.log
```

**Observed throughput (PR #1783 session, 2026-06-03):**

| Time | Modules built | `.lake/` disk |
|---:|---:|---:|
| 1.5 min | 302 | 1.0 GB |
| 5 min | 663 | 1.3 GB |
| 7 min | 894 | 1.4 GB |

Throughput slows as Mathlib modules get heavier (Algebra, Data, then
Topology / Analysis). Plausible full-Mathlib build: **1–3 hours**;
plus ~10 min for QOU. Once the build finishes, `lake exe cache get`
becomes irrelevant — the oleans are local.

### Web-sandbox addendum — three failure modes the recipe above omits (2026-06-04)

A Claude-Code-on-the-web session (PR #1802) hit a **stricter** network
policy than the PR #1783 build-from-source run, surfacing three gaps:

1. **The elan toolchain host is firewalled too — not just the cache.**
   `release.lean-lang.org` returns `Host not in allowlist`, so
   `lean_setup` / `elan toolchain install` aborts with
   `failed to parse release data … Unexpected character: H` (an HTML
   error page, not JSON). The table's "elan install 403 → run locally"
   row has a workaround: the **GitHub release asset is allowlisted**
   (`github.com/leanprover/lean4/releases/...` → 200). Install the
   toolchain by hand:

   ```bash
   apt-get install -y zstd            # tarballs are .tar.zst
   TC=$HOME/.elan/toolchains/leanprover--lean4---v4.24.0   # elan's name for the pinned toolchain
   mkdir -p "$TC" /tmp/lx
   curl -sSL -o /tmp/lean.tar.zst \
     https://github.com/leanprover/lean4/releases/download/v4.24.0/lean-4.24.0-linux.tar.zst
   tar --use-compress-program=unzstd -xf /tmp/lean.tar.zst -C /tmp/lx
   cp -a /tmp/lx/lean-4.24.0-linux/. "$TC/"
   elan toolchain list   # should now list leanprover/lean4:v4.24.0
   ```

2. **A `--depth 1` shallow mathlib clone BREAKS lake's checkout.** Lake
   pins a mathlib revision (e.g. `f897ebcf…`); a shallow clone lacks it,
   so the checkout dies with `external command 'git' exited with code
   128`. Use a **full** clone, or `cd ../mathlib4 && git fetch
   --unshallow` before building. (Step 1's "shallow OK" applies only to
   the LSP-warm path, not to `lake build`.)

3. **The global `insteadOf` can trigger a destructive re-clone loop.**
   With the Step-2 redirect set, lake may decide the mathlib remote
   "URL has changed", then **delete `.lake/packages/mathlib` and
   re-clone on every build** — wiping progress each run. If you see
   repeated `info: mathlib: URL has changed; deleting … cloning again`,
   unset the redirect (`git config --global --unset
   url."file:///home/user/mathlib4".insteadOf`) and let lake fetch
   normally, or pre-populate `.lake/packages/mathlib` from the local
   clone once and leave the redirect off.

**Bottom line for the strictest sandboxes:** if even a full clone +
un-shallow can't get `lake build QOU` past the transitive-dep fetch
(observed in PR #1802), Lean is **not mechanically compilable** in that
session — fall back to a rigorous hand-audit and say so explicitly
rather than claiming a green build you could not run.

### Two more gotchas after a `lake-cache/*` restore (2026-06-08, PR #1999)

Both cost a session **even though the restore itself succeeded**, and
both occur with **no** `insteadOf` redirect set (so they are additive to
"addendum point 3" above):

1. **The cache omits the root `Mathlib.olean`.** `lake-cache/qou-v4-24-0`
   ships thousands of Mathlib *submodule* oleans but **not** the root
   aggregator (the QOU lib never imports bare `Mathlib`, so it was never
   built/cached). A NEW file doing `import Mathlib` fails with
   `object file '…/Mathlib.olean' … does not exist` despite
   `find … -name '*.olean' | wc -l` showing ~2919 present. **Fix:** import
   specific modules — e.g. `import Mathlib.Analysis.SpecialFunctions.Sqrt`
   `+ import Mathlib.Tactic` — never bare `Mathlib` (also the §8
   minimal-imports rule).

2. **`lake env lean` / `lake build` re-resolves deps and WIPES the
   restored oleans.** On the restored tree, lake decides several
   packages' remote URLs "have changed" (the cache was seeded in another
   env) → `deleting … cloning again` → the Mathlib olean count drops to
   ~1. **This happens without any `insteadOf` redirect.** **Fix for
   verifying a single self-contained file: bypass lake** — run `lean`
   directly with a manual `LEAN_PATH`:
   ```bash
   LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
   # for a file that imports other QOU.* modules, also add the workspace + paper oleans:
   LP="$LP$ROOT/.lake/build/lib/lean:$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
   env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean path/to/File.lean   # EXIT 0 = checks
   ```
   lake never runs ⇒ nothing re-resolves. (Whole-lib builds still need
   lake; then expect the re-clone and budget for it.) Worked example +
   sibling scope map:
   [`docs/coordination/2026-06-08-lean-cache-architecture.md`](../../../docs/coordination/2026-06-08-lean-cache-architecture.md).

<a id="verify-a-single-file-with-lean-direct"></a>
> **🟥 VERIFY a single file with `lean`-direct — NEVER `lake build`
> (2026-06-13, cost a session ~40 min).** To *verify* a PR's one or two
> changed `.lean` files, run `lean`-direct (the gotcha-#2 recipe above).
> Do **not** reach for `lake build <Module>`: even for a single module it
> re-resolves the dependency graph and **rebuilds Mathlib from source**
> — the `import Mathlib.Tactic` closure alone is ~3000 modules / 40+ min —
> *and* it wipes the restored oleans (gotcha #2). The Mathlib oleans **are
> reachable**: they ship on the `lake-cache/qou-<toolchain-slug>` branch
> (e.g. `lake-cache/qou-v4-24-0`, ~2919 oleans incl. the `Mathlib.Tactic`
> aggregator) — `git fetch --depth=1` + extract is ~2 min. Do not conclude
> "Mathlib is unreachable / Lean uncompilable" until the cache restore +
> `lean`-direct path has been tried.
>
> **Recovery if you already ran `lake build` and it started rebuilding:**
> the wipe is partial-to-total — check
> `find .lake/packages/mathlib -name '*.olean' | wc -l`; if it is well
> below ~2919 (observed `2919 → 2204`, taking out `Mathlib/Tactic.olean`),
> **kill lake and RE-RESTORE the cache branch** (the Step-0 fetch+extract)
> *before* `lean`-direct — otherwise it fails with
> `object file '…/Mathlib/Tactic.olean' … does not exist`. (To kill lake
> without the `pkill -f` pattern matching its own argv, use a bracket
> escape: `pkill -f 'lake buil[d]'`.)

**When to use which:**

- LSP iteration on one or two files → cache 403 fallback above (warm
  workspace, ~minutes to first useful diagnostic).
- Mass regen of `docs/audits/lean-compile-diagnostics.json` across all
  ~700 `.lean` files → from-source build first, then per-file
  `mcp__lean-lsp__lean_diagnostic_messages` pass; budget 2-3 hours
  end-to-end.
- Single-PR proof discharge → cache fallback; from-source build is
  overkill.

**Container-restart caveat.** In Claude Code on the web, the
container may restart between sessions and lose `/tmp/` and `.lake/`.
The mathlib clone at `../mathlib4` typically persists (it lives in
the working tree's parent). On resume: re-confirm the `git insteadOf`
redirect, then re-launch the build if needed. The build is fully
incremental — only changed modules rebuild.

### ✅ PROVEN sandbox build recipe (2026-06-04, PR #1834 session)

A web session **less-firewalled than #1802** built from source cleanly.
This is the fast path to try FIRST — it often needs no clone at all:

```bash
# 0. The toolchain is frequently ALREADY installed by a prior lean_setup —
#    it's just not on PATH. Check before reinstalling:
export PATH="$HOME/.elan/bin:$PATH"
lake --version           # if this prints "Lake version … (Lean 4.24.0)", you're set
ls .lake/packages/mathlib/Mathlib/Data/Real/Basic.lean   # mathlib SOURCE usually already fetched

# 1. Build a SINGLE module (its dep cone only), NOT all of QOU — far less to compile.
#    Use -R: a stale "compiled configuration is invalid" error means reconfigure.
ELAN_NO_OVERRIDE_NOTICE=1 nohup lake build -R QOU.Mass.MassVolDensity \
  > /tmp/lake.log 2>&1 &
# 2. Watch for completion with a backgrounded until-loop (NOT foreground tail):
( while pgrep -f "lake build -R" >/dev/null; do sleep 30; done; tail -25 /tmp/lake.log ) &
```

**What works / what's blocked in this class of sandbox:**
- ✅ `github.com` dep clones (aesop, Qq, batteries, **mathlib**) — succeed.
- ✅ Building Mathlib **from source** — works (toolchain already installed,
  so the `release.lean-lang.org` block is irrelevant).
- ❌ `lake exe cache get` — **hangs** (olean cache server unreachable); don't
  wait on it, go straight to from-source.
- A single-module dep cone is ~420 Mathlib modules (Real + sinh/cosh + log +
  field_simp/ring), ~tens of minutes; full QOU is 1–3 h.

> **⚠️ CACHE FALSE-POSITIVE GREEN — verify a real recompile before trusting
> exit 0 (2026-06-05, PR #1871).** After RESTORING the `lake-cache/*` orphan
> branch (below), the restored `.lake/build` oleans for a module you then
> *edit* can be treated as up-to-date by Lake's trace check, so
> `lake build -R <Module>` returns **exit 0 with an empty log without
> recompiling your new code** — a false-positive green. A red proof
> (`unsolved goals`) only surfaces on a genuine rebuild. This bit PR #1871:
> SO(3) lemmas "built green" off the restored olean, then a real recompile
> exposed `unsolved goals` (Mathlib's `Real.cosh_two_mul` is `cosh²+sinh²`,
> not `2cosh²−1`). **Rule: after restoring the cache, force a real recompile
> of any module you changed before trusting green** — `touch <file>.lean`
> first, and confirm the log actually ends with
> `Build completed successfully (N jobs)` (a recompile shows tactic-timing
> lines; a skipped build shows nothing). Do NOT infer success from exit code
> alone, and beware compound commands: a trailing `grep -c …` prints `0` but
> **exits 1** when there are zero matches, which can masquerade as a build
> failure. Prefer `grep -c … ; true` or read the explicit "Build completed"
> line.

### 🗄️ PRESERVE THE BUILD — seed/restore the `lake-cache/*` orphan branch

**Every agent rebuilding Mathlib from scratch is the waste to avoid.** Per
the cache strategy ([`docs/workplans/2026-05-24-lean-cache-strategy.md`](../../../docs/workplans/2026-05-24-lean-cache-strategy.md)),
durable cross-container preservation lives on **orphan branches**
`lake-cache/<package>-<toolchain-slug>` (slug for `v4.24.0` =
`v4-24-0`). These survive container reclaim (git-versioned), unlike
`.lake/` (ephemeral) or `../mathlib4` (parent-tree, often persists but not
guaranteed).

> **Two restore paths now wired end-to-end.** Pick the one that
> matches the branch format:
>
> ```bash
> # MONOLITHIC qou cache (production today, chunked-tgz):
> ./scripts/lake-cache-fetch.sh
>
> # PER-PACKAGE caches (PR #1957 producer's output, .olean.xz
> # + cache-index.json regen recipe):
> ./scripts/lake-cache-fetch-multi.py
> ```
>
> `lake-cache-fetch.sh` (PR #1950) auto-runs on SessionStart via
> `setup-lean-toolchain.sh` and consumes the monolithic
> `lake-cache/qou-v4-24-0` branch in either format: (a) legacy
> chunked-tgz (`lake-oleans.tgz.partNN`, current production reseed
> 2026-06-04), or (b) per-file `.lake/` tree (what
> `lake-cache-refresh.yml` writes if CI ever runs it).
>
> `lake-cache-fetch-multi.py` (PR #1967 end-to-end pair to the
> producer) walks `lake-manifest.json`, fetches each per-package
> `lake-cache/<pkg>-v4-24-0` branch in turn, decompresses each
> `.olean.xz` via the `cache-index.json` regen recipe
> (decompress_xz → compute_hashes → touch_trace), and atomic-renames
> each package's `.lake/packages/<pkg>/` into place. Verified
> end-to-end on Qq: 13 oleans round-tripped through the produce →
> push → fetch → restore → regen cycle.
>
> **SEED — `scripts/lake-cache-produce.py` (PR #1957).** Writes a
> separate orphan branch per package (`lake-cache/<pkg>-v4-24-0`)
> with per-file `.olean.xz` blobs + a `cache-index.json` master-index:
>
> ```bash
> # Dry-run all 9 packages — safe, shows planned content + sizes:
> ./scripts/lake-cache-produce.py
>
> # Push to a TEST suffix (doesn't touch production):
> ./scripts/lake-cache-produce.py --push --branch-suffix test
>
> # Push to the canonical branch names (live cutover):
> ./scripts/lake-cache-produce.py --push
> ```
>
> Cutover from monolithic → per-package is a single `--push` run.
> After cutover, sessions auto-restore via `lake-cache-fetch-multi.py`
> instead of `lake-cache-fetch.sh`. Production-branch overwrite is
> still an owner decision; agents should use `--branch-suffix test`
> for experimentation.
>
> See [`docs/audits/2026-06-07-lake-cache-only-new-content-design.md`](../../../docs/audits/2026-06-07-lake-cache-only-new-content-design.md)
> for the full architecture (strip + xz benchmarks + zstd-shared-dict
> head-to-head). Bash one-liner below remains documented as the
> manual / audit path.

The cache branch stores the oleans as a **compressed tarball split into
<100 MB chunks** (`lake-oleans.tgz.part00…`), because GitHub hard-rejects
any single file > 100 MB on push (the qou+mathlib oleans compress to
~364 MB → 5 parts). NOT the raw `.lake/` tree (a raw multi-GB tree push is
hostile). Both restore and seed use a **separate `git worktree`** so your
main working tree is never disturbed — do NOT `git switch --orphan` in the
main tree (it leaves every file untracked and traps you with "untracked
working tree files would be overwritten" on switch-back; Copilot #1857).

> **Seeded 2026-06-04:** `lake-cache/qou-v4-24-0` holds a real build
> (1838-job from-source build of `QOU.Mass.MassVolDensity`'s dep cone).
> RESTORE from it before rebuilding.

**RESTORE first (before any from-source build):**
```bash
if git fetch --depth=1 origin lake-cache/qou-v4-24-0 2>/dev/null; then
  git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
    | while read -r p; do git show "FETCH_HEAD:$p"; done > /tmp/lake-oleans.tgz \
    && tar xzf /tmp/lake-oleans.tgz \
    && echo "restored .lake from cache branch — skip the rebuild"
else
  echo "cache branch not seeded yet — build from source, then SEED it (below)"
fi
```

> **⚠ Post-restore hazard — verify mathlib's origin URL BEFORE running
> lake (2026-06-10, found on PR #2094).** The tar carries
> `.lake/packages/mathlib/.git` from the *seeding* container; if its
> `origin` URL differs from the manifest URL (e.g. it recorded the
> seeder's git proxy), the first `lake` invocation prints
> `mathlib: URL has changed` and **deletes the restored package —
> including its 2.8 GB of oleans — before re-cloning**. Check first:
>
> ```bash
> git -C .lake/packages/mathlib remote get-url origin   # must match lake-manifest.json
> # mismatch → fix it instead of letting lake delete the build:
> git -C .lake/packages/mathlib remote set-url origin \
>   https://github.com/leanprover-community/mathlib4
> ```
>
> If lake already deleted it: after the re-clone completes (rev will
> match the manifest pin), re-extract **only the build dir** from the
> still-fetched cache objects — `tar xzf <tgz> -C "$ROOT"
> ".lake/packages/mathlib/.lake/build"` — and the oleans replay
> (trace hashes are content-based, so the fresh clone's sources match).
>
> **Variant: packages restored with NO `.git` at all (2026-06-10, PR
> #2094 continuation).** If the seed tar carries package sources +
> oleans but no `.git` dirs (check: `git -C .lake/packages/mathlib
> remote get-url origin` falls through to the PARENT repo's origin —
> a misleading proxy URL), do **not** let lake touch the tree (it
> deletes and re-clones, losing the oleans). **Graft** valid git
> state in place first — per `lake-manifest.json` entry: `git init` +
> `git remote add origin <url>` + `git fetch --depth=1 origin <rev>`
> (GitHub is allowlisted) + `git checkout -qf <rev>` inside each
> package dir. Lake then accepts every package untouched and the
> first build runs straight off the restored oleans (verified:
> Qq probe build, 2947 mathlib oleans intact). A package dir missing
> entirely (e.g. `Cli`) is fine — lake clones just that one.

**SEED after a successful build** (so the NEXT agent restores in ~2 min
instead of rebuilding in ~30+) — worktree-based, tarball created in-repo:
```bash
WT=/tmp/lake-cache-wt
# 1. Pack the built oleans (compressed). Create the tarball where the
#    worktree can `git add` it — git cannot add a path outside its tree.
tar czf /tmp/lake-oleans.tgz .lake/build .lake/packages/*/.lake/build 2>/dev/null
# 2. Orphan branch in a SEPARATE worktree (main tree untouched, no trap).
git worktree add --orphan -b lake-cache/qou-v4-24-0 "$WT" 2>/dev/null \
  || { git worktree add --detach "$WT"; git -C "$WT" checkout --orphan lake-cache/qou-v4-24-0; \
       git -C "$WT" rm -rfq --cached . 2>/dev/null; git -C "$WT" clean -fdxq; }
# 3. Split into <100 MB chunks INSIDE the worktree (GitHub rejects >100 MB files).
( cd "$WT" && split -b 90m -d /tmp/lake-oleans.tgz lake-oleans.tgz.part )
git -C "$WT" add 'lake-oleans.tgz.part*'
git -C "$WT" commit -qm "seed lean cache: qou+mathlib oleans @ lean v4.24.0 (chunked <100MB)"
git -C "$WT" push -u origin lake-cache/qou-v4-24-0
git worktree remove --force "$WT"                      # main branch never left
```
> **HTTP 413 on the seed push (2026-06-10).** The web-sandbox git
> proxy caps a single push payload — an ~800 MB one-commit pack is
> rejected with `RPC failed; HTTP 413`. Workaround (verified): commit
> **each ~90 MB chunk as its own commit** inside the worktree and
> `git push` after each one (`--force` on the first push to replace
> the old cache history). Restorers are unaffected — the restore
> recipe reads the tip tree, which contains all chunks.

Keep ≤ 8 such branches (owner cap); the
[`lake-cache-refresh.yml`](../../../.github/workflows/lake-cache-refresh.yml)
workflow prunes/refreshes on `lean-toolchain`/`lakefile.toml` changes — if
CI billing is up, prefer triggering it over an ad-hoc multi-GB agent push.

**Rule for agents going forward:** RESTORE → (build only if miss) → SEED.
Never silently rebuild Mathlib and throw the oleans away.

## Delegate the install to a sub-agent (recommended for the main task)

The full bootstrap (elan + GitHub-toolchain workaround + full mathlib clone
+ from-source olean build) is **long, fiddly, and frequently blocked** — it
should **not** run in the foreground of a content/proof task. Kick off a
**background sub-agent** so the main session keeps moving, then verify the
target file(s) when it reports back.

```text
Agent(
  subagent_type = "general-purpose",
  run_in_background = true,
  description = "Bootstrap Lean + verify <file>",
  prompt = <the runbook below + the specific file/lemma to compile>
)
```

**Sub-agent runbook (give it these env facts so it doesn't re-derive them):**

1. **Probe the network first:** `curl -sI https://github.com` (usually 200)
   vs `curl -sI https://release.lean-lang.org` (often 403 in web sandboxes).
   This decides the toolchain path: if `release.lean-lang.org` is blocked,
   use the **GitHub-release manual install** in §"Web-sandbox addendum" item 1
   (`apt-get install -y zstd`; curl the `lean-<ver>-linux.tar.zst` asset from
   `github.com/leanprover/lean4/releases/...`; extract into
   `~/.elan/toolchains/leanprover--lean4---<ver>/`). Set `ELAN_UPDATE_CHECK=0`
   to suppress `release.lean-lang.org` pings.
2. **Mathlib:** a **full** clone (NOT `--depth 1` — item 2 of the addendum:
   shallow breaks `lake`'s rev checkout) at the repo-pinned commit
   (`grep inputRev lake-manifest.json`). For a *single-file* check, a scratch
   lake project with `require mathlib from "<local path>"` (path dep) sidesteps
   the `insteadOf` re-clone loop (item 3).
3. **Build is slow** (no cache → oleans from source). Let it run; report
   progress. Compile the **statement** first (`sorry` ⇒ only a sorry warning),
   then the proof.
4. **Report findings even if blocked** — the exact failing step + whether it
   is a *hard* network block vs. just slow. Per the §"Web-sandbox addendum"
   bottom line: if even a full clone can't get past the transitive-dep fetch,
   Lean is **not mechanically compilable** in that session — say so explicitly
   and fall back to a rigorous hand-audit; do **not** claim a green build you
   could not run.

**Why a sub-agent:** the install can take many minutes (toolchain fetch) to
hours (full mathlib from source). Foreground-blocking the main task on it is
the anti-pattern; the sub-agent isolates the wait and returns a clean verdict
(verified / blocked-where).

## PATH Configuration

All session scripts source `scripts/lib/lean-env.sh`, which sets:

```bash
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$HOME/.bun/bin:$PATH"
```

The paper-assistant inherits the shell's PATH when launched via `.mcp.json`.
Ensure elan's bin directory is on the PATH in the shell profile
(`~/.bashrc`, `~/.zshrc`, or `~/.profile`).
