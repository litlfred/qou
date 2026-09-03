# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + `local/lean-environment-setup.md`.
Entries marked (verified <date>) were confirmed live; the rest are inherited
and should be confirmed on first use.

---

## TRAP — the LEAN_PATH answer is in this file, under the CACHE heading

If `lean` reports `unknown module prefix 'Mathlib'` **while listing the
directory you pointed at**, the path is one level too shallow: oleans live in
`.lake/packages/*/.lake/build/lib/lean`, not `.../build/lib`. The olean COUNT
does not discriminate — 6990 were present at the moment the import failed.

This is recorded below under the cache-restore section ("Build LEAN_PATH from
the ROOT `.lake` package `build/lib/lean` dirs"), which is where an agent
looking for a *path* problem does not look. Re-derived from scratch on
2026-08-31 for exactly that reason; duplicated here as a findable heading
rather than moved, since the cache section needs it in place too.

Also: `#print axioms` needs no olean. Append the lines to a COPY of the source
and run `lean` on the copy — works on a restored tree with no traces.

**But a copy in `/tmp` breaks elan:** `lean f.lean` there dies instantly with
`no default toolchain configured` (exit 1, 0.01s) because elan resolves the
toolchain from the nearest up-tree `lean-toolchain`, and `/tmp` has none. Fix:
`export ELAN_TOOLCHAIN=leanprover/lean4:v4.24.0` (read the version from
`$ROOT/lean-toolchain`). Verified 2026-09-03.

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
wants `qa-sweep` and must never be hand-edited. **Pass the BLOCK STEM, not the
directory** (corrected 2026-09-03, measured on six blocks):
`bun run folio-assistant/content/pipeline/qa-sweep.ts content/<paper>/<chapter>/<block>`
(no extension) refreshes **only that block's** `.qa.json` — `source_hashes`
plus every script-kind criterion re-run — in ~1–2 min. The 2026-08-29 note
that it "takes a directory and rewrites every block's sidecar (128 files)" is
what happens when you pass the *chapter*; a bare file path still dies
`ENOTDIR`. `scripts/check-sidecars.sh` prints the exact stem command per file,
and keeps printing "→ refresh" even after the refresh (it lists applicable
criteria; it is not a staleness detector) — verify freshness by comparing
`source_hashes.lean` to `sha256(file)[:12]` yourself.

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

## TRAP — v4.24.0 renames seen on a 4×4 complex-matrix file (2026-09-03)

Four mechanical, statement-preserving fixes, all on
`QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`:

- **`Matrix.dotProduct` does not exist** — it is root-namespace `dotProduct`
  (`Mathlib/Data/Matrix/Mul.lean:66`). Symptom: `Unknown constant` printed 4×
  (once per `fin_cases` branch) and the simp set silently loses the unfold.
- **`Matrix.smul_mulVec_assoc` is a deprecated alias** (since 2025-08-14) of
  `Matrix.smul_mulVec`, identical statement `(b • M) *ᵥ v = b • M *ᵥ v`.
- **A `def` of a `Matrix _ _ ℂ` built with `*` must be `noncomputable`** —
  `Finset.sum` over ℂ hits `Complex.instNormedAddCommGroup` (no executable
  code). `!![…]` literals and `•`/`+` alone did not need it; `*` did.
- **`Complex.I ^ 2` is created by `ring_nf`, not by `simp`.** After `simp`
  the `I`s sit as `n₂ * I * (n₂ * I)`, so `Complex.I_mul_I` AND `Complex.I_sq`
  both report "unused" and `ring` fails with `I ^ 2` in the goal. Working
  chain: `simp [...] <;> ring_nf <;> simp [Complex.I_sq] <;> ring`.
  **Do not obey the `unnecessarySeqFocus` linter here** — rewriting the tail
  as `(simp [Complex.I_sq]; ring)` fails `No goals to be solved` because
  `simp` closes some branches outright. Keep `<;>`; the lint is cosmetic.
- `vecHead (vecTail …)` residue after `!![…]`/`![…]` simp: add
  `Matrix.vecHead, Matrix.vecTail` to the simp set.

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
## TRAP — the vacuity audit's `--review-ledger` rewrites the WHOLE ledger; port your entries by hand
`bun run content/pipeline/lean-vacuity-axiom-audit.ts content/quantum-observable-universe
--review-ledger <ledger>` (2026-09-03, ~6 min over 3421 files) pruned **28
entries in files I never touched** and reset 6 others to `needs-agent`, because
it recomputes the candidate set corpus-wide and "resolved candidates are pruned".
It also only *produces* six categories; the borrowed-name / zero-placeholder /
docstring-body-mismatch / vacuous-hypotheses entries (source
`scripts/lean-borrowed-name-audit.py`, which has **no ledger mode**) are
preserved untouched with a stale `file_sha`. So: run it against a **copy**
(`--review-ledger $S/ledger-copy.json --json $S/vacuity.json`), read the diff,
and hand-edit only your keys in the committed ledger. Key format
`<relpath>::<decl>::<category>`; `file_sha` = `sha256(file bytes)[:12]`
(verified against two existing entries); verdicts `genuine|legit|advisory|
needs-agent`. Its `conjecture_graph` reads the dependency edge from
`[Instance]` **binders** only — a class taking the upstream class as a *field*
is classified primary (fixed by moving it to a binder, per §3b-tax).
## TRAP — small authoring facts that cost a compile each (v4.24.0)
- `deriving Fintype` needs `import Mathlib.Tactic.DeriveFintype` (the handler is
  not in `Mathlib.Data.Fintype.Card`): *"No deriving handlers have been
  implemented for class `Fintype`"*.
- `div_add_div_same` is **deprecated** → `← add_div`.
- `field_simp` often closes a determinant/ratio goal outright; a trailing
  `ring` then errors *"No goals to be solved"* — that is a success signal, drop
  the `ring`.
- `Mathlib.Algebra.Algebra.Basic` alone gives neither `ring` nor `field_simp`
  nor `add_div`; add `Mathlib.Tactic.Ring`, `Mathlib.Tactic.FieldSimp`,
  `Mathlib.Algebra.Field.Basic`.
- `beans create --parent <task>` is refused (*"task beans can only have
  milestone, epic, or feature as parent"*) — parent to the session milestone
  and name the task bean in the body. Backticks in a `--body "…"` string are
  command substitution; use `--body-file`.
- `scripts/check-sidecars.sh` flags a file of recorded CODATA/witness
  decimals typed `ℝ` as "§7c gratuitous ℝ". That is the §7c CODATA row, not a
  defect; say so in the file header and move on.

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

## Session log

Append one line per session: what you verified, by what method, and any
entry above you confirmed or corrected. Keep this file under ~200 lines —
prune the log, never the TRAPs. (Pruned 2026-09-03: entries 08-29 → 09-03
collapsed; every distinct lesson from them lives in a TRAP above.)

- 2026-09-03 (magnus-o6ov gauge-hook): verified committed
  `QOU/MassTheory/MagnusGaugeCurvatureHookColumn.lean` (HEAD 11e80b8a39; def
  `curvatureSum` + 2 thms over generic CommRing/Algebra, `tr : A →ₗ[R] R`).
  All 4 imports (`BigOperators.Ring.Finset`, `Module.LinearMap.Defs`,
  `Algebra.Algebra.Defs`, `Tactic`) have BOTH olean and source in v4.24.0 — the
  LinearMap/Algebra module names are real. lean-direct EXIT 0, zero diagnostics,
  AS AUTHORED (no fix). Both thms `#print axioms` = `[propext, Classical.choice,
  Quot.sound]`, no sorryAx. Cold-cache TRAP again: 3m52s wall / 10s user, warm
  4.0s. Cache was already present in root `.lake` (3470 mathlib oleans) WITHOUT
  the `RESTORED-NO-TRACES` marker — absence of the marker ≠ absence of the
  restore; check the olean count. Disk was 2.1G free: too little for a
  re-restore tarball (~1.6–2.3G), so a "restore first" reflex would have failed.
- 2026-09-03 (braid-twist-flip): verified two changed content-block `.lean`
  files realizing trefoil monodromy S₃≅D₃, both lean-direct EXIT 0, no sorryAx,
  no refs to removed `w4_fixed`/`twist_flip_pow_three`/`twist_flip_ne_id`/`Fin 4`.
  File 2 (`lean/QOU/BraidTwistFlip.lean`, `α×α×α`, all `rfl`, imports
  Mathlib.Tactic): all 6 decls "do not depend on any axioms". File 1
  (`braids-and-knots/braid-twist-flip.lean`, `Fin 3`, imports `QOU.Basic`):
  built QOU.Basic.olean lean-direct first (5s), then elaborated source against
  it — 5 decls = std-3 `[propext, Classical.choice, Quot.sound]`, `rotation_ne_id`
  (via `decide`) = `[propext, Quot.sound]`. Confirmed cold-cache TRAP (File 2 warm
  run 1m45s wall / 11s user; first attempt timed out at 2m). New: ELAN_TOOLCHAIN
  note above. Cache already restored (6990 mathlib oleans, RESTORED-NO-TRACES).
- 2026-09-02 (qtr-kron-consolidation): verified edited (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-09-02 (magnus-o6ov): verified `QOU/MassTheory/MagnusHookExteriorPower.lean` (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-08-30: authored+verified `QOU/StandardModel/BrunnianIsotypeExclusion.lean` (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-08-29 (cool-johnson): orphan-branch restore WORKS; the blocked host is (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-08-30 (torus-knots): restored `lake-cache/qou-v4-24-0` fresh (3407 (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-08-30: found `QOU/Hecke/WedderburnRankDegeneracy.lean` red on `main` for (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-08-31 (milnor-tl-brick2): verified new `QOU/MassTheory/QuantumTraceTower.lean` (details pruned 2026-09-03; lessons live in the TRAPs above)
- 2026-09-03 (sm-surface sweep, bean qou-08zf): 58 files on the SM/eightfold/
  α_EM surface, all lean-direct exit 0 (50 unchanged, 7 rewritten, 1 new
  companion `AlphaEM/FormLadderAnchorDominanceChecks.lean`); `#print axioms` on
  every new/changed decl = std-3 or none, no sorryAx. Rebuilt the changed
  library module into a `cp -al` mirror before compiling its consumer. Cache
  state: no RESTORED marker but 3470 mathlib + 2443 root oleans were live;
  never ran `lake build`. Cold-cache TRAP confirmed again (probe 3m26s wall /
  6.5s user). Report: docs/audits/2026-09-03-sm-surface-lean-best-practices-sweep.md.
  (older milnor-brick / magnus / deficit-recursion single-file verifications
  pruned 2026-09-02 — their distinct lessons are captured in the TRAPs above:
  v4.24.0 module moves incl. `BigOperators.Ring`→`Ring.Finset`; rebuild-from-
  current-source-first to avoid false green; cache restores to ROOT `.lake`,
  the per-paper `.lake` tree is a decoy.)
- 2026-09-03 (two-nucleon-sign-defect): NEW `QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`
  (Mathlib-only). As authored exit 1 — 4 mechanical fixes, see the "4×4
  complex-matrix" TRAP; no statement touched, no sorry. Final: lean-direct EXIT 0,
  8/8 decls std-3 axioms, 0 sorryAx. Part (B) `Real.sqrt` lemmas compiled as
  authored. Cold 3m29s wall / 25s user; warm 8s. Cache already restored.
- 2026-09-03 (braid-twist-flip): two content-block `.lean` (S₃≅D₃ trefoil
  monodromy) EXIT 0, no sorryAx; one needed `QOU.Basic.olean` built lean-direct
  first. Found the `/tmp` → `ELAN_TOOLCHAIN` trap (top of file).
- 2026-09-02 (qtr-kron / magnus-o6ov): `QuantumTraceTower.lean` (first QOU import;
  rebuilt the dep olean from CURRENT source first to avoid a false green) and
  `MagnusHookExteriorPower.lean` (`Finset.sum_powerset_card` does not exist →
  `Finset.sum_powerset`; aggregator `Mathlib.olean` ABSENT from this partial
  restore, so a literal `import Mathlib` errors — verify via a temp copy with
  narrowed imports). Both EXIT 0, std-3 axioms. `/usr/bin/time` not installed;
  use the bash builtin.
- 2026-08-29 → 08-31: orphan-branch restore works (blocked host is Azure blob,
  never used); this seed = 3407 mathlib oleans, sufficient for QOU + Mathlib.Tactic;
  `BrunnianIsotypeExclusion` / `EmCouplingBarParity` / `QuantumTraceTower` verified
  std-3; `/-!` before `import` is rejected; `omit [inst] in` precedes the docstring;
  `WedderburnRankDegeneracy` red on main 6 days behind a false green → PR #6097 and
  `verification-harness.md`.
