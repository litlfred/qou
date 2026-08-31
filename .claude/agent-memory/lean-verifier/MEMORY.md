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

## TRAP — a slow first `lean`-direct run is COLD PAGE CACHE, not a rebuild

Measured 2026-08-29 on one Mathlib-importing file: first run **2m50s wall but
only 5.7s `user`**; second run **4.4s wall**. The wall time is faulting in
~7000 Mathlib oleans, nothing more.

**The discriminator is `user` time — always `time` the run.** Seeing three
minutes and concluding "Mathlib is rebuilding from source" leads straight to
`lake build` or a re-restore, and `lake build` is the thing that evicts the
cache (TRAP above). The misdiagnosis causes the harm; the slow run is benign.

## TRAP — a chapter-directory `.lean` DOES have a `.qa.json` sidecar

The "nothing but you checks library Lean" exemption is scoped to
`content/<paper>/lean/QOU/**`. A `.lean` sitting beside a `.ts`/`.md` in a
**chapter directory** is a content-block sibling and **has** a sidecar, so
editing it stales `source_hashes.lean` — and `lean_statement` too, since a
rename reaches declaration types. Measured 2026-08-29 on
`categorical-chain-convergence-mechanisms.lean`: `20d0f5b771ae → 74278be4c9f7`
and `4803c6f9d272 → 33891c65fd26`.

A green `lean`-direct verdict is **not** the whole preflight there. The sidecar
wants `qa-sweep --only <crit>` and must never be hand-edited. Two cautions
measured the same day: `qa-staleness`/`qa-sweep` take a **directory**, not a
file (a file path dies `ENOTDIR`), and a chapter-scoped sweep rewrites **every**
block's sidecar — 128 files for a one-block change — so revert all but the
block you actually staled, or a rename PR silently becomes a chapter sweep.

## TRAP — false greens and corrupt oleans → `verification-harness.md`

Three ways a `lean`-direct verdict is about the harness, not the code. Evidence
and the working recipe are in the sibling file; the shapes:

1. **Green against a STALE dependency olean is a FALSE GREEN.** Imports resolve
   from disk, so a consumer compiles against the olean your changed module had
   *before* the edit. Measured 2026-08-30: exit 0 against the tree, **exit 1**
   once the dependency was rebuilt — a file red on `main` for six days.
   **Rebuild each changed module from source, then check its whole
   reverse-import cone, computed from the import graph.** Companion mistake: a
   grep for `[Foo …]` *hypothesis binders* misses a file that *constructs an
   instance*.
2. **A partial `LEAN_PATH` overlay shadows the whole namespace** —
   `SearchPath.findWithExt` commits to the first root holding a `QOU/` dir. Use
   a complete `cp -al` mirror, `rm -f`-ing each olean before rebuilding it.
3. **A disk-full `lake build` writes truncated oleans that segfault.** Signature
   **exit 139, zero errors, 0–1 s**; 10 of 11 "failing" modules were this. Never
   call a module broken from exit 139 alone. **Do NOT use olean size as the
   test** — 2026-08-30, three segfaulters measured 50–226 KB inside a normal
   33 KB–6.7 MB range, so size flagged nothing.
4. **Most cone failures are the harness, not the code.** Measured 8, of which
   **1** was a real defect. `object file … does not exist` usually means a
   *non-cone* dependency has no olean at all — `ls` it. Decisive test for every
   one: re-run against **main's own oleans**, your changes off `LEAN_PATH`.
5. **A dead constant hides behind `abbrev` hops.** A consumer can fail on a
   deleted constant whose name does not appear in it (three hops, measured), so
   grepping consumers is not a blast-radius check. Same class as 1.

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

## STABLE — your verdict IS the gate; do not wait on the dead ones

All three Phase-4 external gates are gone: **CI** (auto-triggers disabled
repo-wide 2026-06-30, `build.yml` is `workflow_dispatch`-only, no `lean_ci.yml`
exists), **Gemini** (sunset 2026-08-01), **Copilot** — **CORRECTED 2026-08-30: reviews DO arrive**
(~3-4 min) and are **quota-rationed**; the old "never enqueues" reading came
from `get_check_runs: total_count 0`, which is real but does not discriminate.
Do not block on that poll; do expect a review wake on a subscribed PR. Bean
`qou-gwe9` (reopened), `docs/audits/2026-08-30-copilot-review-works-again.md`.
Full detail lives in `merge-coordinator`'s memory, which owns this.

So state the verification you actually ran and **never write "CI green"**
unless a run exists. A **library** file under `content/<paper>/lean/QOU/**` has
no `.qa.json` sidecar and `lean-content-siblings.yml` does not cover it —
nothing but you checks it. **But see the sidecar TRAP above: that exemption is
scoped to the library tree, and a chapter-directory `.lean` DOES have a
sidecar.**

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

## TRAP — v4.24.0 module moves + subscript ± are notation tokens

Two authoring mistakes that block a NEW file but are trivial, correct fixes
(no statement/witness change) — seen 2026-08-29 on
`QOU/MassTheory/MagnusPairingSignStructure.lean`:

- `import Mathlib.Data.Matrix.Notation` **does not exist** in mathlib
  v4.24.0. The `!![a,b;c,d]` matrix literal notation lives in
  `Mathlib.LinearAlgebra.Matrix.Notation`. (`Mathlib.Data.Matrix.Notation`
  has neither olean nor source in the tree; the olean error is a red
  herring for "cache is partial" — the module is gone, not uncached.)
- **`import Mathlib.Data.Matrix.Kronecker` ALSO does not exist in v4.24.0**
  (confirmed 2026-08-31). The Kronecker content — `⊗ₖ` notation (`open scoped
  Kronecker`), `Matrix.mul_kronecker_mul`, `Matrix.trace_kronecker`,
  `Matrix.one_kronecker_one` — lives in `Mathlib.LinearAlgebra.Matrix.Kronecker`.
  Decisive discriminator vs "uncached": the mathlib **source** tree is present
  under `.lake/packages/mathlib/Mathlib/...`, and `Data/Matrix/Kronecker.lean`
  is absent while `LinearAlgebra/Matrix/Kronecker.lean` exists and the
  `Data/Matrix/` dir is otherwise full. So: `object file … does not exist` for a
  `Data.Matrix.*` import in v4.24.0 → check the source tree; several `Data.Matrix`
  modules moved to `LinearAlgebra.Matrix`.
- Under a full `import Mathlib.Tactic`, `₊`/`₋` (U+208A/U+208B subscript
  plus/minus) are **notation tokens** (PosPart etc.), so a bound-variable
  name like `ρ₊` fails to lex: `unexpected token '₊'; expected ','`. Rename
  the binder (`ρ₊`→`ρp`) — pure alpha-renaming, the proposition is
  identical. Fine in comments/docstrings, not in identifiers.
- `import Mathlib.Algebra.BigOperators.Ring` **is not a module** in v4.24.0.
  It is a *directory* `Ring/` (`Finset.lean`, `List.lean`, `Multiset.lean`,
  `Nat.lean`) with no `Ring.lean` aggregator; zero mathlib files import the
  bare path. `Finset.mul_sum` lives in `Mathlib.Algebra.BigOperators.Ring.Finset`
  — the correct import. Symptom is identical to a cache miss (`object file
  …/BigOperators/Ring.olean … does not exist`), so distinguish source-bug
  from cache-gap by checking the mathlib *source* tree for a `.lean` and
  grepping whether any mathlib file imports the exact path. Seen 2026-08-31
  on `QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`.

## TRAP — this cache branch restores to ROOT `.lake`, and the per-paper tree is a stale decoy

`lake-cache/qou-v4-24-0` (25 parts) extracts to `$ROOT/.lake/` (root
workspace layout: `.lake/packages/*/.lake/build/lib/lean` + `.lake/build/lib/lean`).
Measured 2026-08-29: **3407 mathlib oleans** + 2275 QOU-library oleans,
`Mathlib.Tactic.olean` and `Matrix/Trace.olean` present. The pre-existing
`content/quantum-observable-universe/lean/.lake/packages/**` tree is a
**partial decoy** (~726 mathlib, QOU lib = 0) — do NOT point LEAN_PATH at
it. Build LEAN_PATH from the ROOT `.lake` package `build/lib/lean` dirs.
(The prior log's "6990 mathlib" was not what THIS restore produced; 3407 is
the QOU-cone partial and it is sufficient for QOU + Mathlib.Tactic files.)

---

## Session log

Append one line per session: what you verified, by what method, and any
entry above you confirmed or corrected. Keep this file under ~200 lines —
prune the log, never the TRAPs.

- 2026-08-30: authored+verified `QOU/StandardModel/BrunnianIsotypeExclusion.lean`
  (sign-isotype exclusion, statement-B). lean-direct EXIT 0, `#print axioms` =
  `[propext, Classical.choice, Quot.sound]`, no `sorryAx`. TRAP: cache tarball is
  now **2.3G** (was 1.6G) and restore ran out at ~2.2G free — extraction cut off
  in the QOU library files, but mathlib extracted 3407 oleans, ENOUGH for a
  Mathlib-only import cone. Lesson: a Mathlib-only file needs no complete restore
  — probe the import cone with a minimal `example` first. Gotcha: `omit [inst] in`
  must precede the docstring, not sit between docstring and `theorem`.
- 2026-08-29 (cool-johnson): orphan-branch restore WORKS; the blocked host is
  Azure blob `lakecache.blob.core.windows.net`, which the restore never uses.
  Confirmed the cold-cache and sidecar TRAPs.
- 2026-08-30 (torus-knots): restored `lake-cache/qou-v4-24-0` fresh (3407
  mathlib oleans this seed — vs 6990 in the baseline; cone was sufficient),
  verified new `QOU/Interactions/EmCouplingBarParity.lean` lean-direct exit 0
  + `#print axioms` (std 3 only). One fix: `/-!` docstring preceded imports —
  Lean rejects any `import` after a module doc; imports must be first.
- 2026-08-30: found `QOU/Hecke/WedderburnRankDegeneracy.lean` red on `main` for
  six days behind a FALSE GREEN — my own #5710 removed a field its instance
  discharged. Rebuilt the 8-module reverse-import cone: ALL-GREEN after repair.
  Found a second red file the same way (`QOU/Mass/QIntegerBarParity.lean`, one
  stale `open`). Added `verification-harness.md` with all three traps measured.
  PR #6097.
- 2026-08-31 (milnor-tl-brick2): verified new `QOU/MassTheory/QuantumTraceTower.lean`
  (Mathlib-only; `qtr`/`muDiag`/`qtrDiag` defs + 5 theorems). One fix, NOT a
  tactic/statement change: `import Mathlib.Data.Matrix.Kronecker` → `.LinearAlgebra.`
  (v4.24.0 module move, see TRAP above). All tactic blocks compiled as authored.
  lean-direct EXIT 0, zero diagnostics/sorries. `#print axioms` on qtr_kron,
  qtr_kron_one, qtrDiag_one all = `[propext, Classical.choice, Quot.sound]`, no
  sorryAx. Cache already restored (3407 mathlib oleans, RESTORED-NO-TRACES marker).
  Confirmed cold-cache TRAP again: file real 1m16s but user only 5.7s. File is
  untracked (new, uncommitted) — the import fix lives in the working tree.
- 2026-08-30 (milnor-v7ro): verified new `QOU/MassTheory/DeficitRecursionReduction.lean`
  (Mathlib.Tactic-only, no QOU imports; `deficit` def + 2 field-algebra theorems).
  lean-direct EXIT 0, zero errors/sorries. `#print axioms` on BOTH theorems =
  `[propext, Classical.choice, Quot.sound]`, no sorryAx. Cache already restored
  (3407 mathlib oleans, RESTORED-NO-TRACES marker present). Confirmed cold-cache
  TRAP again: wall 3m31s but `user` only 10s — page faulting, not a rebuild.
- 2026-08-31: verified NEW `QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`
  (Mathlib-only, 4 decls). As-written FAILS: line 41/42 `import
  Mathlib.Algebra.BigOperators.Ring` is a non-existent module in v4.24.0 (it's a
  dir, no `Ring.lean`) — a SOURCE bug, not a cache gap. With that one import
  fixed to `...Ring.Finset` (verified on a temp copy; source left unedited),
  lean-direct EXIT 0, all 4 axiom-clean {propext, Quot.sound[, Classical.choice]},
  no sorryAx. 3 harmless `unusedSectionVars [DecidableEq n]` linter warnings only.
  New TRAP added (BigOperators.Ring). Restore note: QOU-cone seed is a PARTIAL
  mathlib (3469 oleans, not 6990) — it lacks mathlib modules QOU never imports;
  full extract ran the 38G quota out mid-QOU-lib (didn't matter, mathlib is first).
- 2026-08-30: re-verified 3 new files on `claude/milnor-a4-exact-tight-slice`
  after +254-commit rebase (main changed `MilnorOrderLawGeneral.lean` via w4gn).
  Chain is self-contained (only QOU dep is Milnor). Rebuilt Milnor from CURRENT
  source FIRST (avoids false-green), then Borromean/Brunnian against the fresh
  olean: all exit 0. Magnus standalone exit 0. All 9 key theorems axiom-clean
  {propext,Classical.choice,Quot.sound}. No instance of `BrunnianDeficitRecursion`
  (content-bearing class, honest §3b-cond open state). No rebase breakage; Milnor
  still exports leadingOrder/leadingOrder_four/tauBorromean/borromean_deficit_factor/
  MilnorExactOrderConjecture. Confirmed: cache restores to ROOT `.lake` (2277 QOU
  oleans), the per-paper `content/.../lean/.lake` tree is a 3-olean decoy — the
  harness §3 base path must be ROOT, not $LEANLIB.
