# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + `local/lean-environment-setup.md`.
Entries marked (verified <date>) were confirmed live; the rest are inherited
and should be confirmed on first use.

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
untarring. Nothing reaped it until 2026-08-28: one leaked `/tmp/tmp.*` from
2026-08-15 survived thirteen days and drove the container to **92K free**,
where the Bash harness cannot write its output capture and *every* command
fails — including the `rm` that would fix it. The
`trap 'rm -f "$TGZ"' EXIT INT TERM` is load-bearing; keep it.

`df` reads deceptively: ~252G nominal at 100% with ~38G used, because the
real limit is a per-session quota near 38G. "Avail 0, low Used" = allowance
spent, not machine broken.

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
release asset is allowlisted** — install the toolchain by hand. GitHub
clones work; only the release server and `lake exe cache get` are blocked,
both sidesteppable. First
`grep -ri "<error keyword>" .claude/skills/ AGENTS.md docs/`, then delegate
a long install to a background subagent. Only a *hard* network block
justifies a hand audit — and then say so explicitly. Mathlib cache 403
fallback (shallow local clone + `git config --global
url."file:///…".insteadOf`) is in the skill.

## TRAP — a sibling `.lean` stub shadows the real declaration

`lean.ref` resolution checks the **sibling file first**. A trivial
`theorem foo : True := trivial` content-block sibling therefore shadows the
real library declaration the ref would otherwise reach. Never create or
keep one when the real formalisation exists. If the decl is in a mis-named
library file, align the filename — do not paper over it with a stub.

## STABLE — the honest dispositions when a proof will not close

Exactly three, per `AGENTS.md` §1a / §"Strict Lean Discipline":

1. **Prove it.**
2. **Queue it** — the *real* proposition with `sorry` + `-- Ref:` whose
   `[key]` matches `content/schema/references.ts` exactly.
3. **Demote it** — a `conjecture`, or a content-bearing conditional class
   (§3b-cond) carrying the *hypotheses*, not the conclusion. A "theorem"
   projecting its own claim out of a class field is a vacuous
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
  Actions billing). `build.yml` is `workflow_dispatch`-only; no
  `lean_ci.yml` exists. Branches routinely show zero runs.
- **Gemini review** — consumer Gemini Code Assist sunset 2026-08-01.
- **Copilot review** — measured n=5 (bean `qou-gwe9`): zero reviews every
  time, `get_check_runs` returns `total_count: 0`, nothing is enqueued.
  `prepare-merge-auto` Phase 1b polls 15 min for a check run that is never
  created — **skip it and record why**, citing `qou-gwe9`.

So your `lean`-direct verdict *is* the gate. State the verification you
actually ran. Never write "CI green" unless a run exists.

For a **library** file under `content/<paper>/lean/QOU/**` there is no
`.qa.json` sidecar and `lean-content-siblings.yml` does not cover it —
nothing but you checks it.

## STABLE — `lean`-direct recipe that works (verified 2026-08-29)

From the repo root, for a file whose imports are Mathlib-only:

```sh
export PATH="$HOME/.elan/bin:$PATH"
export LEAN_PATH=$(ls -d .lake/packages/*/.lake/build/lib/lean | tr '\n' ':')$(pwd)/.lake/build/lib/lean
lean <path/to/file.lean>; echo "EXIT=$?"
```

Globbing `.lake/packages/*/` picks up all eight dep packages (mathlib,
batteries, aesop, Qq, proofwidgets, plausible, importGraph,
LeanSearchClient) without hardcoding the list. `exit 0` with no diagnostics
= the file checks. No `lake build`, so nothing is evicted.

## STABLE — `#print axioms` on a file that is not an importable module

A content-block sibling `.lean` (under `content/<paper>/<chapter>/`) is on
no module path, so it cannot be `import`ed to audit it. Copy it to the
scratchpad, append `#print axioms <Namespace>.<decl>` lines to the **copy**,
`lean`-direct the copy. Never append to the tracked file. ~4 s warm. Clean =
`depends on axioms: [propext, Classical.choice, Quot.sound]`; `sorryAx` is
the failure.

## TRAP — a slow first `lean`-direct run is COLD PAGE CACHE, not a rebuild

Measured 2026-08-29 on one Mathlib-importing file: **2m50s** wall on the
first run, **4.4s** on the second — with `user` time ~5s in *both*. The
wall time is I/O, faulting in ~7000 mathlib oleans; `lean`-direct never
compiles Mathlib.

The misdiagnosis this prevents: seeing ~3 minutes, concluding "something is
rebuilding Mathlib from source", and reaching for `lake build` or a
re-restore — either of which is the actual harm. **Check `user` time before
you conclude anything.** `user` ≈ seconds ⇒ waiting on disk; `user` ≈ wall
and climbing for minutes ⇒ then you are genuinely compiling.

## TRAP — editing a content-block sibling `.lean` staleifies its `.qa.json`

The "no sidecar covers library Lean" rule is about
`content/<paper>/lean/QOU/**`. A `.lean` beside a `.ts`/`.md` in a
**chapter** directory *does* have a `<block>.qa.json`, whose
`source_hashes.lean` (12-char sha256 prefix) drifts the moment you touch
the file — as does `lean_statement` when the edit reaches a declaration's
type, which a rename does. Verified 2026-08-29: a 5-token rename moved it
`20d0f5b771ae` → `74278be4c9f7`.

A green `lean`-direct verdict is **not** the whole preflight for these
files. Report the sidecar stale and hand it to `qa-sweep`; never hand-edit
the hash.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| root mathlib oleans, healthy tree, v4.24.0 | `find .lake/packages/mathlib -name '*.olean' \| wc -l` | **6990** | 2026-08-29 |
| cold vs warm `lean`-direct wall time, one Mathlib-importing file | `time lean <file>` | 2m50s cold / 4.4s warm; `user` ≈ 5s in **both** | 2026-08-29 |
| whole-library build state | `lake build QOU` | red on pre-existing failures — **not** the gate; verify per-module | 2026-08 |

⚠ The `~2919 (healthy)` figure this table carried until 2026-08-29 was
**wrong and dangerous**, and it contradicted the TRAP above it in this same
file (which cites 6990 as the pre-eviction count). A tree evicted from 6990
down to 2919 would have read as *healthy* under the old row. Re-measure;
do not treat any number here as a threshold.

---

## Session log

Append one line per session: what you verified, by what method, and any
entry above you confirmed or corrected. Keep this file under ~200 lines —
prune the log, never the TRAPs.
