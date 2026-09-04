# lean-verifier — memory

**STABLE** (trust it) · **TRAP** (durable failure mode) · **BASELINE** (a number
— re-measure, never quote). Seeded 2026-08-29 from `AGENTS.md` +
`local/lean-environment-setup.md`; dated entries were confirmed live, the rest
are inherited and want confirming on use.

> **Only the first ~200 lines are injected — keep it under that.** Detail lives
> in the siblings, read **on demand, by symptom**. Split 2026-09-04 from 498
> lines, after the ROOT-`.lake` trap at line 313 went unread and was re-derived
> from scratch by the agent it was written for.

| sibling | read it when |
|---|---|
| `cache-restore-and-disk.md` | restoring, seeding, a warm-looking cache that compiles nothing, anything about disk |
| `v4-24-0-renames.md` | unknown identifier/constant, or `object file … does not exist` |
| `verification-harness.md` | a verdict you suspect is the harness: false greens, segfaults, cone failures |
| `session-log.md` | the trail. **Append one line per session** there: what you verified, by what method, and any entry here you confirmed or corrected. Prune the log, never the TRAPs |

## STABLE — workspace shape

- Single **root** Lake workspace (`/lakefile.toml`, `/lean-toolchain`) with three
  paper packages: `qou` → `QOU` (`content/quantum-observable-universe/lean/`),
  `ugb` → `UGB`, `fred2005` → `Fred2005`.
- **Name the targets.** A bare `lake build` at the root is a *no-op* — exit 0,
  "Build completed successfully (0 jobs)" — because the root declares no library
  and glob libraries build only when named. Use `lake build QOU UGB Fred2005`.
- Content blocks reference Lean by package-qualified URI
  (`lean: { ref: "qou:QOU.Torsion.lifting_exists" }`); the legacy `decl:`/`file:`
  shape is gone from the schema. Toolchain:
  `export PATH="$HOME/.elan/bin:$PATH"`.

## TRAP — the ROOT `.lake` is the real one; the per-paper tree is a stale decoy

**The single most re-derived entry here — read it before you measure anything.**
The cache restores to `$ROOT/.lake/`; the pre-existing
`content/quantum-observable-universe/lean/.lake/packages/**` tree is a **partial
decoy**. Do not point `LEAN_PATH` at it and do not read its counts. Measured on
one tree minutes apart (2026-09-04): subproject **1236** oleans, root **9721**,
`Data/Real/Basic.olean` MISS under the subproject and present at the root — which
nearly triggered a redundant 1.6 GB fetch. (Same shape 2026-08-29, in the sibling.)

```sh
export LEAN_PATH=$(for d in .lake/packages/*/.lake/build/lib/lean; do printf "%s:" "$(realpath $d)"; done)
```

Oleans sit at `…/build/lib/**lean**`, one level deeper than `build/lib`.
`unknown module prefix 'Mathlib'` *while listing the directory you pointed at* is
this, and the olean **count does not discriminate** — 6990 were present when such
an import failed.

## TRAP — `lake build` silently evicts a restored cache

A restored tree has oleans but **no `.trace` files**, so Lake treats every one as
stale, rebuilds from source, and deletes the restore as it goes — silently, reading
as ordinary build progress. Measured 2026-08-15 (`qou-r13s`): root mathlib
**6990 → 334**, and of 536 oleans written in ten minutes **zero** were QOU/UGB.

```sh
[ -f "$(git rev-parse --show-toplevel)/.lake/RESTORED-NO-TRACES" ] \
  && echo "restored — lean-direct only, do NOT lake build"
```

Delete the marker only once Lake has genuinely rebuilt the tree. **Absence of
the marker is not absence of a restore** — check the olean count and a specific
module. On a restored tree **verify `lean`-direct** (the sanctioned gate per
`AGENTS.md` §"QA is agent-owned"): 2.4 s against 50 minutes of nothing.

## TRAP — a warm-looking cache can be useless, and the restore skips on it

`scripts/lean-cache-restore.sh` no-ops at `>= 2000` mathlib oleans. Measured
2026-09-02: **6990** present, restore skipped, every one `Mathlib/Tactic/**` or
`Mathlib/Lean/**` infrastructure with `Data`, `Order`, `Logic` absent. The threshold
counts files, not coverage, and `lean-axiom-guard.yml` gates on the same test, so it
neutral-skips in CI too. **Test for a module you actually import, never a count.**
Recipes, partial-cone coverage, the leaked-tarball shortcut, disk →
`cache-restore-and-disk.md`.

## TRAP — a slow first `lean`-direct run is COLD PAGE CACHE, not a rebuild

Measured repeatedly: 1m16s–3m52s **wall** against 5.7–25 s **user**, warm re-run
4–8 s. The wall time is faulting in thousands of Mathlib oleans.
**The discriminator is `user` time — always `time` the run.** Reading three
minutes as "Mathlib is rebuilding from source" leads to `lake build` or a
re-restore, and `lake build` is what evicts the cache. The misdiagnosis causes
the harm; the slow run is benign. (`/usr/bin/time` is not installed — bash
builtin.)

## TRAP — false greens and corrupt oleans → `verification-harness.md`

Five ways a verdict is about the harness, not the code. **Read the sibling
before calling any module broken** — it has the evidence and the working recipe;
these are the shapes only:

1. **Stale dependency olean ⇒ FALSE GREEN.** Rebuild each changed module from
   current source, then its whole reverse-import cone. (One hid a file red on
   `main` for six days.)
2. **A partial `LEAN_PATH` overlay shadows the whole namespace** — use a complete
   `cp -al` mirror.
3. **Truncated oleans segfault**: exit **139**, zero errors, 0–1 s; size does
   *not* detect it.
4. **Most cone failures are the harness** — 8 measured, **1** real. Decisive
   test: re-run against **main's own oleans**.
5. **A dead constant hides behind `abbrev` hops**, so grepping consumers is not a
   blast-radius check.

## TRAP — a name error and a cache gap look identical → `v4-24-0-renames.md`

`unknown identifier` / `unknown constant` / `object file … does not exist` are
byte-identical between a v4.24.0 rename and a partial cache, and lead to opposite
actions. **Discriminate by grepping the mathlib SOURCE tree**, present in full
even when the oleans are not: absent `.lean` ⇒ rename or move; present `.lean`
with no olean ⇒ cache gap. Moves, renames, notation tokens (`₊`/`₋` fail to lex
in identifiers), `noncomputable`, `/-!`-before-`import` → the sibling.

## TRAP — a chapter-directory `.lean` DOES have a `.qa.json` sidecar

The "nothing but you checks library Lean" exemption is scoped to
`content/<paper>/lean/QOU/**`. A `.lean` beside a `.ts`/`.md` in a **chapter
directory** is a content-block sibling and **has** a sidecar, so editing it
stales `source_hashes.lean` — and `lean_statement` too, since a rename reaches
declaration types (2026-08-29). A green `lean`-direct verdict is **not** the whole
preflight there: the sidecar wants `qa-sweep --only <crit>` and is never
hand-edited. `qa-staleness`/`qa-sweep` take a **directory**, not a file (`ENOTDIR`
otherwise), and a chapter-scoped sweep rewrites **every** block's sidecar (128
files for a one-block change) — revert all but the block you staled, or a rename
PR silently becomes a chapter sweep.

## TRAP — a sibling `.lean` stub shadows the real declaration

`lean.ref` resolution checks the **sibling file first**. A trivial
`theorem foo : True := trivial` content-block sibling therefore shadows the real
library declaration the ref would otherwise reach. Never create or keep one when
the real formalisation exists. If the decl is in a mis-named library file, align
the filename — do not paper over it with a stub.

## TRAP — env failures are routable; "Lean is unavailable" is usually wrong

On any of: LSP "no valid project path", `leansearch` SSL error, `lake exe cache
get` 403, `elan toolchain install` SSL, empty `~/.elan/toolchains/`, `lake build`
timeout — do **not** conclude Lean is unavailable. `release.lean-lang.org` is
firewalled in some sandboxes but the **GitHub release asset is allowlisted**, and
GitHub clones work. First `grep -ri "<keyword>" .claude/skills/ AGENTS.md docs/`,
then delegate a long install to a background subagent. Only a *hard* network
block justifies a hand audit — and say so explicitly.

## STABLE — checking axioms needs no olean

Append `#print axioms <decl>` to a **copy** and run `lean` on it; works on a
restored tree with no traces. "**std-3**" throughout these files means
`[propext, Classical.choice, Quot.sound]` — the clean result. **But a copy in `/tmp` breaks elan** — `no default
toolchain configured`, exit 1 in 0.01 s, because elan resolves from the nearest
up-tree `lean-toolchain` and `/tmp` has none. Fix:
`export ELAN_TOOLCHAIN=$(cut -d: -f2- "$ROOT/lean-toolchain")` (2026-09-03).

## STABLE — the honest dispositions when a proof will not close

Exactly three, per `AGENTS.md` §1a / §"Strict Lean Discipline": **prove it**;
**queue it** (the *real* proposition with `sorry` + `-- Ref:` whose `[key]`
matches `content/schema/references.ts` exactly); or **demote it** to a
`conjecture` or a content-bearing conditional class (§3b-cond) carrying the
*hypotheses*, not the conclusion — a "theorem" projecting its own claim out of a
class field is a vacuous self-assuming projection.

Banned: `: True := trivial` in any declaration kind (including the
`def`-disguised form, `def-disguised-true`), tautological conclusions,
`native_decide` over an unproved structural claim, and an `axiom`/`class`
substituting for a proof. If you cannot close it,
`beans create "GAP: <what is open>" --type task` and report it — an honest bean
is always acceptable.

## STABLE — your verdict IS the gate; do not wait on the dead ones

Of the three Phase-4 external gates two are gone and one was misread. **CI**:
auto-triggers disabled repo-wide 2026-06-30, `build.yml` is
`workflow_dispatch`-only, no `lean_ci.yml` exists. **Gemini**: sunset 2026-08-01.
**Copilot** — *corrected 2026-08-30*: reviews **do** arrive (~3–4 min), quota-
rationed; the "never enqueues" reading came from `get_check_runs: total_count 0`,
real but not discriminating. Don't block on that poll; do expect a review wake on
a subscribed PR (`qou-gwe9`,
`docs/audits/2026-08-30-copilot-review-works-again.md`; `merge-coordinator` owns
it).

State the verification you actually ran and **never write "CI green"** unless a
run exists. A **library** file under `content/<paper>/lean/QOU/**` has no sidecar
and `lean-content-siblings.yml` does not cover it — nothing but you checks it.
That exemption is scoped to the library tree; see the sidecar TRAP above.

## BASELINE — re-measure, do not quote

| what | last seen | when |
|---|---|---|
| root mathlib oleans, healthy (`find .lake/packages/mathlib -name '*.olean' \| wc -l`) | **6990**; seeds of 3407/3470 also sufficed for QOU cones | 2026-08-29 |
| root oleans, all packages, after a leaked-tarball restore | **9721** | 2026-09-04 |
| cold vs warm `lean`-direct, one Mathlib file (`time lean <f>`) | 1m16s–3m52s cold / 4–8 s warm; `user` 5.7–25 s in **both** | 2026-09-04 |
| `lake build QOU` | red on pre-existing failures — **not** the gate; verify per-module | 2026-08 |

⚠ The `~2919 (healthy)` figure this table carried until 2026-08-29 was **wrong and
dangerous**: a tree evicted from 6990 to 2919 would have read as *healthy*, and it
contradicted a TRAP in this same file. Treat no number here as a threshold.
