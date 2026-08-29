# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + `.claude/skills/local/lean-environment-setup.md`.
Nothing below has been re-verified by me in a live session yet; the first
session to use each entry should confirm it and mark it verified.

---

## STABLE — workspace shape

- Single **root** Lake workspace: `/lakefile.toml`, `/lean-toolchain`.
  Three paper packages: `qou` → `QOU` (`content/quantum-observable-universe/lean/`),
  `ugb` → `UGB`, `fred2005` → `Fred2005`.
- **Name the targets.** A bare `lake build` at the root is a *no-op*: it
  exits 0 with "Build completed successfully (0 jobs)". The root package
  declares no library of its own and glob libraries build only when named.
  Use `lake build QOU UGB Fred2005`.
- Content blocks reference Lean by package-qualified URI:
  `lean: { ref: "qou:QOU.Torsion.lifting_exists" }`. The legacy
  `decl:`/`file:` shape is removed from the schema.
- Toolchain on PATH via `export PATH="$HOME/.elan/bin:$PATH"`.

## STABLE — the restore-first recipe (the whole point of this agent)

Order is: **RESTORE → verify lean-direct → SEED**. A from-source Mathlib
build is the last resort, not the first move.

Prebuilt oleans live on orphan branches `lake-cache/<pkg>-<toolchain-slug>`
(slug derived from `lean-toolchain`: `v4.24.0` → `v4-24-0`). Restore is
~2 min against a 30–60 min rebuild. Full command block is in
`.claude/skills/local/lean-environment-setup.md` §"PROVEN sandbox build
recipe" / §"PRESERVE THE BUILD" — read it there rather than reconstructing
it, and derive the slug from the file rather than hardcoding a version.

Verification is `lean`-direct with `LEAN_PATH` pointed at the restored
olean dirs: `exit 0` means the file checks. Not `lake build`.

## TRAP — `lake build` silently evicts a restored cache

A restored tree has oleans but **no `.trace` files**, so Lake treats every
one as stale, rebuilds from source, and deletes the restore. It is silent:
the output reads as ordinary build progress.

Measured 2026-08-15 (bean `qou-r13s`), `lake build QOU UGB Fred2005` against
a freshly restored tree: root mathlib oleans **6990 → 334**, and of 536
oleans written in ten minutes **zero** were QOU/UGB/Fred2005.

Guard: the restore recipe touches `.lake/RESTORED-NO-TRACES`. Before any
build step, check for it:
`[ -f "$ROOT/.lake/RESTORED-NO-TRACES" ] && echo "restored — do NOT lake build"`.
Delete the marker only once Lake has genuinely rebuilt the tree.

## TRAP — the restore's temp tarball is ~1.6G and nothing reaps it

The recipe streams every `lake-oleans.tgz.part` into one temp file before
untarring. Until 2026-08-28 nothing deleted it; a single leaked
`/tmp/tmp.*` from 2026-08-15 was still present thirteen days later and
drove the container to **92K free**, at which point the Bash harness cannot
write its own output capture and *every* command fails — including the `rm`
that would fix it. The `trap 'rm -f "$TGZ"' EXIT INT TERM` in the recipe is
load-bearing; keep it.

Disk reads deceptively here: `df` shows ~252G nominal at 100% with ~38G
used, because the real limit is a per-session quota near 38G. "Avail 0 with
low Used" means the allowance is spent, not that the machine is broken.

## TRAP — seeding route depends on how you built

- Built with `lake build` → seed the monolithic branch via
  `scripts/lean-olean-cache-seed.sh`.
- Built `lean`-direct → **no `.trace` files are written**, so that script's
  guard correctly *refuses*. Never force it past: Lake treats untraced
  oleans as stale, rebuilds, and evicts them (bean `02kc`). Preserve
  lean-direct output as a plain `tar` addon orphan branch instead
  (e.g. `lake-cache/qou-v4-24-0-h4-wedderburn-cone`), restored with
  `tar xzf` and consumed via `LEAN_PATH`.

## TRAP — env failures are routable; "Lean is unavailable" is usually wrong

On any of: LSP "no valid project path", `leansearch` SSL error, `lake exe
cache get` 403 on every shard, `elan toolchain install` SSL / "failed to
parse release data", empty `~/.elan/toolchains/`, `lake build` timeout —
do **not** conclude Lean is unavailable.

`release.lean-lang.org` is firewalled in some sandboxes but the **GitHub
release asset is allowlisted**, so the toolchain can be installed by hand.
GitHub clones work; only the release server and `lake exe cache get` are
blocked, and both are sidesteppable. First
`grep -ri "<error keyword>" .claude/skills/ AGENTS.md docs/`, then delegate
a long install to a background subagent so the foreground task is not
blocked. Only a *hard* network block justifies falling back to a hand
audit — and then say so explicitly.

Mathlib cache 403 fallback (shallow local clone + `git config --global
url."file:///…".insteadOf`) is in the skill under §"Mathlib cache 403
fallback".

## TRAP — a sibling `.lean` stub shadows the real declaration

`lean.ref` resolution checks the **sibling file first**. A trivial
`theorem foo : True := trivial` content-block sibling therefore shadows the
real library declaration the ref would otherwise reach. Never create or
keep one when the real formalisation exists. If the decl is in a mis-named
library file, align the filename — do not paper over it with a stub.

## STABLE — the honest dispositions when a proof will not close

Exactly three, per `AGENTS.md` §1a / §"Strict Lean Discipline":

1. **Prove it.**
2. **Queue it** — the *real* proposition with `sorry` + a `-- Ref:` citation
   whose `[key]` matches `content/schema/references.ts` exactly.
3. **Demote it** — a `conjecture`, or a content-bearing conditional class
   (§3b-cond). The class must carry the *hypotheses*, not the conclusion; a
   "theorem" that projects its own claim out of a class field is a vacuous
   self-assuming projection.

Banned: `: True := trivial` in any declaration kind (including the
`def`-disguised form, which is detected as `def-disguised-true`),
tautological conclusions, `native_decide` over an unproved structural
claim, and an `axiom`/`class` substituting for a proof. If you cannot
close it: `beans create "GAP: <what is open>" --type task` and report the
gap. An honest bean is always acceptable.

## STABLE — verification is the only merge gate; do not wait on the dead ones

All three original Phase-4 gates are gone. Do not block on any:

- **CI** — auto-triggers disabled repo-wide (owner directive 2026-06-30,
  Actions billing). `build.yml` is `workflow_dispatch`-only; there is no
  `lean_ci.yml` in the tree. Feature branches routinely show zero runs.
- **Gemini review** — the consumer Gemini Code Assist on GitHub was sunset
  2026-08-01.
- **Copilot review** — measured n=5 (bean `qou-gwe9`): requested explicitly,
  zero reviews every time, and `get_check_runs` returns `total_count: 0`,
  so nothing is ever enqueued. `prepare-merge-auto` Phase 1b still
  prescribes a 15-minute poll for a check run that is never created —
  **skip it and record why**, citing `qou-gwe9`.

So your `lean`-direct verdict *is* the gate. State the verification you
actually ran. Never write "CI green" unless a run exists.

For a **library** file under `content/<paper>/lean/QOU/**` there is no
`.qa.json` sidecar and `lean-content-siblings.yml` does not cover it —
nothing but you checks it.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| restored root mathlib oleans | `find .lake/packages/mathlib -name '*.olean' \| wc -l` | ~2919 (healthy); ≪2919 ⇒ a stray `lake build` evicted the cache, re-restore | 2026-06-13 |
| whole-library build state | `lake build QOU` | red on pre-existing failures — **not** the gate; verify per-module | 2026-08 |

---

## Session log

Append one line per session: what you verified, by what method, and any
entry above you confirmed or corrected. Keep this file under ~200 lines —
prune the log, never the TRAPs.
