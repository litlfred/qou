# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + the skill (governs where they disagree).
NOTHING is auto-injected here (measured) — read this yourself. Sibling files:

- `verification-harness.md` — false greens, partial overlays, exit-139, cone triage, FQN guards
- `authoring-traps-v4-24-0.md` — module moves, lexer tokens, the small-determinant recipe
- `session-log.md` — per-session ledger (append there, not here; restructured 2026-09-03)

---

## TRAP — the LEAN_PATH answer: oleans live one level DEEPER than you think

If `lean` reports `unknown module prefix 'Mathlib'` while listing the directory
you pointed at, the path is one level too shallow: oleans live in
`.lake/packages/*/.lake/build/lib/lean`, not `.../build/lib`. The olean COUNT
does not discriminate (6990 present at the moment the import failed).

`#print axioms` needs no olean: append to a COPY and run `lean` on it from cwd
`/home/user/qou` (or `export ELAN_TOOLCHAIN=leanprover/lean4:v4.24.0`), else `no default toolchain configured`.

## TRAP — the clone is SHALLOW: git cannot date a source against its olean, and presence ≠ currency

`git log -- <file>` bottoms out at the shallow-boundary merge (`b831ff34c3`,
2026-08-29, which shows *every* file as "new file"), so "olean dated Jul 2,
source committed Aug 29" is undecidable from git. Do not argue freshness from it.

**Presence is not currency either.** 2026-09-03: `QOU/Interactions/
GramMatrixH3Symbolic.olean` was present (55 MB, mtime Jul 2) and held ZERO of
the convention-D declarations added 2026-08-15; its import
`HeckeH3GramNondegeneracy.olean` was absent; `Mathlib/Tactic.olean` (Jul 18) was
newer than the QOU oleans built against it. **The 1-second currency test is
`grep -c -a <declName> <olean>`** for a declaration you need. Fix: rebuild the
changed file's whole QOU import cone from current source into a `cp -al`
mirror (`verification-harness.md` §3), never the shared tree — ~4 min for a
light 4-module cone; 207 s for one parent carrying four 40M-heartbeat proofs.

## TRAP — WHERE the QOU oleans live varies per container

2026-08-29: `lake-cache/qou-v4-24-0` extracted to ROOT `.lake/` (3407 mathlib
+ 2275 QOU oleans) and the per-paper `content/…/lean/.lake` tree was a partial
decoy (~726 mathlib, QOU = 0). 2026-09-03, same repo, different container: root
mathlib 6990 but the QOU oleans were ONLY in the per-paper tree (942, 168 of
them rebuilt lean-direct 2026-08-29). **Look at both.** An orchestrator-supplied
`LEAN_PATH.txt` may carry RELATIVE `.lake/packages/…` entries — valid only with
cwd = repo root; absolutise them (cwd resets between calls). 2026-09-04, a third
container: per-paper **1236**, root **9721**, with `Data/Real/Basic.olean` MISS
under the per-paper tree and present at the root — the mirror image of the
2026-09-03 reading, and reading only one of them nearly triggered a redundant
1.6 GB fetch.

## TRAP — MATHLIB oleans split across the two trees; "object file does not exist" ≠ absent

Generalises §2/§6(a) from `QOU/` to **`Mathlib/`**. 2026-09-04: root held
`Mathlib/{Tactic,Data/Real/Sqrt}.olean` but NOT `Algebra/Order/Chebyshev.olean`;
the per-paper tree held Chebyshev but not `Mathlib.Tactic`. Both roots contain a
`Mathlib/` dir, so the **first one on `LEAN_PATH` resolves every `Mathlib.*`
module** and the rest are reported missing. A sibling agent read that error as
*"this Mathlib module is absent from the restored set"*, rewrote a working proof
to route around it, and wrote the false claim into a **source comment and a
commit message** (`67128df5dd`) — the §11 mistake, one library over.
**Fix: `cp -aln` a hardlink UNION mirror of every `.lake/build/lib/lean` from
both trees** (harness §13) — ~0 disk, and both proof routes then compile.
Check the manifests agree on the mathlib rev first; here both were `f897ebcf72cd`.

## STABLE — workspace shape

- Single **root** Lake workspace (`/lakefile.toml`, `/lean-toolchain`); packages
  `qou`→`QOU` (`content/quantum-observable-universe/lean/`), `ugb`→`UGB`, `fred2005`→`Fred2005`.
- A bare root `lake build` is a **no-op** (exit 0, "0 jobs"); name the targets.
- `lean.ref` URIs are package-qualified (`qou:QOU.Torsion.lifting_exists`).
- Toolchain: `export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1`.
- `/usr/bin/time` is not installed; use the bash `time` builtin.
- Root `.lake/packages/mathlib/` is **oleans only**; the Mathlib SOURCE is under
  the per-paper `content/…/lean/.lake/packages/mathlib/Mathlib/`. Find lemma
  names by grepping that source, or the oleans with `grep -rl
  --binary-files=text -F <name>` (single-component names only — dotted names
  are stored as components), then confirm with a `#check` scratch from cwd `$ROOT`.

## STABLE — the restore-first recipe (the whole point of this agent)

**RESTORE → verify lean-direct → SEED.** From-source Mathlib is the last resort.
Prebuilt oleans: orphan branches `lake-cache/<pkg>-<toolchain-slug>` (`v4.24.0`
→ `v4-24-0`), ~2 min vs 30–60 min. Command block: skill §"PROVEN sandbox build
recipe" / §"PRESERVE THE BUILD" — derive the slug from the file. Verification
is `lean`-direct with `LEAN_PATH` at the restored dirs; `exit 0` = checks.

## TRAP — `lake build` silently evicts a restored cache

A restored tree has oleans but **no `.trace` files**; Lake treats every one as
stale, rebuilds from source and deletes the restore, silently. Measured
2026-08-15 (bean `qou-r13s`): root mathlib oleans **6990 → 334**, and of 536
oleans written in ten minutes **zero** were QOU/UGB/Fred2005. Guard:
`[ -f "$ROOT/.lake/RESTORED-NO-TRACES" ] && echo "restored — do NOT lake build"`.
(The marker is absent in some containers; its absence is NOT proof of traces.)

**And there are TWO mathlib trees, so the guard can read clean and still be
worthless** (measured 2026-09-05). `lake build` run from
`content/<paper>/lean/` builds *that* directory's own
`.lake/packages/mathlib` — a near-empty second copy, no marker — while
`scripts/lean-direct-env.sh` puts the **repo-root** `.lake/packages/mathlib`
(5.4 G, marker present) on `LEAN_PATH`. So it does not evict the restore; it
burns 40 min and +1.4 G on an 88 %-full disk rebuilding a tree nothing verifies
against, and would not have finished. Same file, `lean`-direct: **5.0 s**.
Check `du -sh` on both before believing a `lake build` is doing what you want.

## STABLE — cache shortcuts and hazards → `restore-shortcuts.md`

Before fetching 1.6 GB, check whether a **leaked `/tmp/tmp.*`** already IS the
cache (it was, 2026-09-04). Run the restore **serially** — the global
`FETCH_HEAD` makes a concurrent fetch silently truncate the tarball. And a
partial restore is normal: 2970 of Mathlib's 6996 modules, so outside that cone
`object file … does not exist` is a gap, not a defect. Detail in the sibling.

## TRAP — `/tmp/lean-v4.24.0` IS the toolchain; "reclaiming" it bricks Lean

`~/.elan` is only **13 MB**: both `~/.elan/toolchains/lean-v4.24.0` and
`…/leanprover--lean4---v4.24.0` are **symlinks to `/tmp/lean-v4.24.0`** (2.5 G),
wired by the SessionStart `setup-elan-symlinks.sh`. So the top `du` entry under
`/tmp` is load-bearing and `rm`-ing it destroys the environment. Measured
2026-09-04 while triaging a container at **1013 M free / 98 %**, one step from
writing "3.2 G recoverable" into a report. Only the **697 M
`/tmp/lean-v4.24.0-linux.zip`** is genuinely reclaimable. `readlink -f
~/.elan/toolchains/*` before proposing any `/tmp` cleanup.

## TRAP — the restore's temp tarball is ~1.6G and nothing reaps it

One leaked `/tmp/tmp.*` survived thirteen days and drove the container to
**92K free**, where the Bash harness cannot write its own output and *every*
command fails, including the `rm`. Keep `trap 'rm -f "$TGZ"' EXIT INT TERM`.
`df` lies: ~252G nominal at 100% with ~38G used = a per-session quota near 38G.

## TRAP — a "N modules are missing" count taken from a two-root `LEAN_PATH` is WRONG (2026-09-05)

The overlay-shadowing trap below, in its most expensive form: a coordinator
measured `QOU.lean`'s 864 direct imports as **820 present / 44 missing** and
handed me the 44 as a build list. The true figure, testing each module against
**both** olean roots, is **19 missing / 845 present**. The other 25 were present
in `content/…/lean/.lake/build/lib/lean` and invisible because the root
`.lake/build/lib/lean` comes first on `LEAN_PATH` and also holds a `QOU/` dir,
so it resolves every `QOU.*` and the second root is never consulted. Their list
named `MathlibExt.ManifoldVolumePositive`, six `MassTheory.*`, nine
`SchurWeyl.*`; **none of those needed building** — all were on disk.

**So `lean`'s "does not exist" is a statement about ONE root, never about the
tree.** Test presence with `os.path.isfile` against every root before believing
a missing-module list — including one handed to you by another agent. It also
mis-transcribes: their list said `SchurWeyl.HeckeSemisimple{,General,Real}` and
no `HeckeSemisimple.lean` exists at all.

**The fix is the union mirror, and it is cheap:** `cp -aln` each
`build/lib/lean` (root, per-paper, ugb, and all 16 package dirs) into one
`$ROOT/.lake/union/lean`. Measured: **6234 oleans for 26 MB** of real disk.
Then `LEAN_PATH` is that one directory and nothing shadows anything.

## TRAP — `environment already contains 'C' from M` = a stale olean holding a MOVED declaration

A *second*, distinct stale-cache symptom, and the one that actually blocked
`lean QOU.lean` after every missing module was built. Not "file absent" —
**two oleans both define `C`**, because the declaration moved between modules
after the cache was seeded and only the destination's olean was rebuilt.
Measured: `S1_eq_seminormalParam` present in both `SchurWeyl.SeminormalParam`
(olean Aug 24) and `SchurWeyl.SeminormalParamAnchorReal` (olean Sep 5), while
current source declares it in the second only.

Sibling symptom, same root cause: `` `squares_sum` is not a field of structure
`StandardYoungCount` `` / `Fields missing: squares_sum_factorial,
squares_sum_holds`. **That is NOT a defect on `main`** — `HeckeAlgebra.lean`
(source Sep 3) declares exactly `squares_sum`; its olean was Aug 30 and carried
the superseded shape. Rebuilding the one parent made the consumer compile in
**2 s**. I nearly reported it as a real finding; the discriminator is *read the
current source of the module that defines the symbol*, then check the olean's
date against it.

**Fix both by rebuilding the implicated module's whole QOU import cone from
current source**, topologically, not the single file — a single-file rebuild
just moves the mismatch one level up. Driver that converges automatically:
loop `lean QOU.lean`, regex the first error for the module name, rebuild its
cone, repeat. Converged in **2 iterations / 53 modules / ~13 min** here.

## STABLE — `lean QOU.lean` (root library, current source) is GREEN — recipe + cache (2026-09-05)

**exit 0, 10.9 s warm, zero output**, against the union mirror. Two addon
branches are needed together and both are plain-`tar`, untraced, lean-direct:

| branch | holds |
|---|---|
| `lake-cache/ugb-v4-24-0` | 29 UGB oleans — without them every `import QOU` dies at `unknown module prefix 'UGB'` |
| `lake-cache/qou-v4-24-0-root-import-closure` | 53 QOU oleans: 19 genuinely missing (4 `Hecke.*`, 2 `Mathlib.*`, 13 `QBeta.*`) + 34 rebuilt for staleness (the SchurWeyl/Specht/MathlibExt cone + `Mathlib.HeckeAlgebra`) |

Restore = build the union mirror, then `tar xzf "$T" -C "$MIR" --unlink-first`.
**`--unlink-first` is load-bearing**: mirror entries are hardlinks shared with
the real trees, and extracting through one rewrites the shared inode and
corrupts the source tree. Same rule for `lean -o`: `rm -f` the mirror olean
first. Full recipe in each branch's `README.md`.

**It certifies the import GRAPH, not the library.** The other ~2500 QOU oleans
are still the seed snapshot; full certification is the dirty-closure rebuild.

## TRAP — mtime is not a staleness test in this tree, and another agent may be building beside you

`source newer than olean` by mtime flagged **1774 of 2619** QOU modules — a
checkout artifact (they cluster at a uniform ~26 d), not staleness. Use git
commit time. And mid-build I found `lean -o` processes writing
`Archimedean/PauliWitness/Witness12B.olean` into the per-paper tree that were
**not mine** — a sibling session building in the same worktree. Consequences:
shared disk pressure, a one-core box running two heavy `lean`s, and a
half-written olean visible through your hardlink mirror (exit 139, harness §3).
Check `ps aux | grep '[l]ean -o'` before blaming your own harness.

## STABLE — UGB is NOT in the qou cache; build it lean-direct in ~4 min (2026-09-05)

`lake-cache/qou-v4-24-0` carries Mathlib + QOU oleans and **no UGB**, so `lean`
on anything doing `import QOU` dies at `unknown module prefix 'UGB'` —
`QOU/PhotonThreading.lean` imports `UGB.GrobnerShirshov.HeckeGS`. Verified as a
two-sided control 2026-09-05: UGB dir on `LEAN_PATH` → exit 0; off it → exit 1
with that exact error.

**Do not `lake build` the ugb package to fix this.** It has no `.lake/` at all,
so Lake would clone and build Mathlib from source (~3.3 GB) — infeasible at the
674 MB free this container had. All three manifests (root / qou / ugb) pin the
same mathlib rev `f897ebcf72cd`, so the restored oleans serve UGB directly.

Recipe: topologically order the 29 modules (`UGB.lean` + 28 under `UGB/`) by
their `import UGB.` lines, then from `content/unital-groebner-bases/lean`
`lean -o .lake/build/lib/lean/<M>.olean -i …ilean <M>.lean` with `LEAN_PATH` =
that output dir + every `.lake/packages/*/.lake/build/lib/lean` under BOTH the
repo root and `content/quantum-observable-universe/lean`. **29/29 exit 0, ~4 min
total, 31 MB** — 1-5 s each except `GrobnerShirshov.HeckeCompletion` at 170 s.
Preserved (plain `tar`, untraced, restore-only-for-lean-direct) on
**`lake-cache/ugb-v4-24-0`**, single 11 MB blob `addon-oleans.tgz`, no chunking:

    git fetch --depth=1 origin lake-cache/ugb-v4-24-0
    git show FETCH_HEAD:addon-oleans.tgz > "$T" && tar xzf "$T" -C "$ROOT"

`HeckeGS` and `HeckeCompletion` are **not reachable from `UGB.lean`** — the
lakefile widens `globs` for exactly that reason; a root-only build misses the
whole Hecke GS development including the `hecke_is_gs_basis` refutation.

**`import QOU` costs 7m27s COLD, 11.5 s warm — `user` was 3.7 s both times.**
Textbook cold-page-cache (§TRAP above): do not read the 7 minutes as a rebuild.

## TRAP — seed a cache branch with git PLUMBING, never a checkout

Seeding from a mid-merge working branch must not touch the index or worktree.
`git hash-object -w` each payload → `git mktree` → `git commit-tree` (no `-p`,
that is what makes it an orphan) → `git update-ref refs/heads/lake-cache/<x>` →
`git push origin refs/heads/…:refs/heads/…`. Measured 2026-09-05: `git status`
stayed at 0 lines throughout. A `git checkout --orphan` would have stashed or
clobbered the in-flight merge.

## TRAP — seeding route depends on how you built

`lake build` output → `scripts/lean-olean-cache-seed.sh`. `lean`-direct output
writes **no `.trace`**, so that script correctly *refuses*; never force it (bean
`02kc`). Preserve lean-direct output as a plain-`tar` addon orphan branch
(e.g. `lake-cache/qou-v4-24-0-h4-wedderburn-cone`), restored with `tar xzf`.

## TRAP — env failures are routable; "Lean is unavailable" is usually wrong

LSP "no valid project path", `leansearch` SSL, `lake exe cache get` 403 on
every shard, `elan toolchain install` SSL, empty `~/.elan/toolchains/`, `lake
build` timeout — none means Lean is unavailable. `release.lean-lang.org` may be
firewalled but the **GitHub release asset is allowlisted**; the blocked cache
host is Azure blob `lakecache.blob.core.windows.net`, which the orphan-branch
restore never touches. First `grep -ri "<error>" .claude/skills/ AGENTS.md docs/`.

## TRAP — a sibling `.lean` stub shadows the real declaration

`lean.ref` resolution checks the **sibling file first**; a `: True := trivial`
sibling shadows the library decl. Align a mis-named library file; never stub it.

## TRAP — a slow first `lean`-direct run is COLD PAGE CACHE, not a rebuild

First run 1m50s–3m34s wall but 5–30 s `user`; second ~5 s. **`time` it; `user`
is the discriminator.** Concluding "rebuilding" leads to `lake build` = eviction.

## TRAP — a chapter-directory `.lean` DOES have a `.qa.json` sidecar

The "nothing but you checks library Lean" exemption is scoped to
`content/<paper>/lean/QOU/**`. A `.lean` beside a `.ts`/`.md` in a chapter dir
has a sidecar; editing it stales `source_hashes.lean` and `lean_statement`
(measured 2026-08-29). Refresh with `qa-sweep --only <crit>` on the
**directory** (a file path dies `ENOTDIR`); a chapter sweep rewrites EVERY
block's sidecar (128 files for one block) — revert all but yours.

## TRAP — false greens and corrupt oleans → `verification-harness.md`

1. **Green against a STALE dependency olean is a FALSE GREEN.** Imports resolve
   from disk; a consumer compiles against the olean its dependency had *before*
   the edit (measured 2026-08-30: exit 0 → exit 1 once rebuilt; red on `main`
   six days). Rebuild each changed module from source, then its reverse-import
   cone computed from the import graph — a grep for `[Foo …]` binders misses
   files that *construct* an instance.
2. **A partial `LEAN_PATH` overlay shadows the whole namespace** — the first
   root holding a `QOU/` dir wins. Use a complete `cp -al` mirror, `rm -f`-ing
   each olean before rebuilding it (else you truncate the shared inode).
3. **Truncated oleans segfault**: exit 139, zero errors, 0–1 s. Olean SIZE is
   not a test (50–226 KB inside a normal range). Two causes: a disk-full local
   build, **and the restored cache itself** — so a clean `df` does NOT clear it
   (measured 2026-09-05, `ComplexDilogarithmSlit` 192,512 vs 279,688 B on a
   healthy disk). One bad olean segfaults its whole downstream cone while every
   consumer's source is clean; bisect to the deepest module whose own deps all
   pass, recompile that one. Harness §4a.
4. **Most cone failures are the harness** (8 measured, 1 real). `object file …
   does not exist` usually = a non-cone dependency with no olean; `ls` it.
   Decisive test: re-run against main's own oleans with your changes off the path.
5. **A dead constant hides behind `abbrev` hops** (three, measured); grepping
   consumers is not a blast-radius check.
6. **`lean -o` refuses a source outside its root** (cwd, or `--root`): stand-in /
   mutant modules go under a scratch root laid out `QOU/…/Mod.lean` — harness §10.

## STABLE — the honest dispositions when a proof will not close

Exactly three (AGENTS.md §1a / §"Strict Lean Discipline"): **prove it**;
**queue it** — the *real* proposition with `sorry` + `-- Ref: [key]` matching
`content/schema/references.ts`; **demote it** — a `conjecture`, or a
content-bearing conditional class carrying the *hypotheses*. Banned: `: True :=
trivial` in any declaration kind (incl. `def`-disguised), tautologies,
`native_decide` over an unproved structural claim, an `axiom`/`class`
substituting for a proof. Otherwise `beans create "GAP: …" --type task`.

## STABLE — your verdict IS the gate; do not wait on the dead ones

CI auto-triggers are disabled (2026-06-30; `build.yml` dispatch-only, no
`lean_ci.yml`); Gemini is sunset (2026-08-01); Copilot reviews DO arrive (3–4
min) but are quota-rationed, and `get_check_runs` = 0 does not discriminate
(bean `qou-gwe9`, owned by `merge-coordinator`). Never write "CI green"; say
which verification you ran. A library file under `content/<paper>/lean/QOU/**`
has no sidecar — nothing but you checks it.

## STABLE — small explicit determinants → `authoring-traps-v4-24-0.md` §Recipe

`QOU.Shared.DetFin` has `Matrix.det_fin_four/five/six` (sorry-free, generic).
`rw [Matrix.det_fin_five]; simp only […, Fin.reduceCastSucc, <table def>];
field_simp; ring` closed a 5×5 rational-entry determinant in 14 s wall
(2026-09-03, `GramQuotientDetD.lean`). The core dsimproc `Fin.reduceCastSucc`
reduces `castSucc` numerals — no `fin_cases` needed. `sympy` is absent;
`pip install --user` works. Validate a tactic route on a stand-in scratch
against Mathlib-only oleans while the real import cone rebuilds.

## TRAP — v4.24.0 module moves + notation tokens → `authoring-traps-v4-24-0.md`

`Mathlib.Data.Matrix.Notation` and `Mathlib.Data.Matrix.Kronecker` do not exist
(→ `Mathlib.LinearAlgebra.Matrix.*`); `Mathlib.Algebra.BigOperators.Ring` is a
directory (→ `.Ring.Finset`); `Finset.sum_powerset_card` does not exist (→
`Finset.sum_powerset`). Symptom is identical to a cache miss — check the
mathlib **source** tree before diagnosing the cache. `₊`/`₋` are notation
tokens under `Mathlib.Tactic`; rename such binders. `ring` needs a *commutative*
ring: over `[Ring A]` it fails on mere associativity with the misleading
`ring_nf made no progress` — use explicit `mul_assoc` (or `noncomm_ring`).

## TRAP — docstring figures inherit the probe's hardcoded constants → `verification-harness.md` §9

A new file quoted CODATA-**2018** residual figures (`t = 2.0975e-7`, from
`R_exp = 206.7682830` in its cited probe) while `constants.py` serves CODATA 2022
(211.2 ppb); the Lean window covered both — only the prose was stale on arrival.
Diff the probe's literal against `constants.py`; §9 has the inhabitation check.

## TRAP — restored oleans are a SNAPSHOT of the seed commit → `verification-harness.md` §11

Imports resolve out of oleans built at the cache branch's **seed** commit, so a
file whose cone moved since is checked against old declarations — silently, error
pointing at your call site. `ls -l <olean>` vs `git log -1 -- <source>` before
trusting a green OR debugging a red. Does NOT invalidate every restore.

## STABLE — library rebuild: the DIRTY CLOSURE, and which criterion is sound (2026-09-04, corrected the same day)

Single-file `lean`-direct certifies against on-disk oleans, so the only way to
know `main` is green is to rebuild what the cache cannot vouch for. Recipe
(bean `qou-n9j7`, PRs #6649/#6674), from `content/quantum-observable-universe/lean`:

1. Full topological order of `QOU/**/*.lean` → `/tmp/full_topo_all.txt`
   (regenerate it; `main` adds modules daily).
2. **Dirty = source changed since the cache's SEED COMMIT, or olean missing,
   or an import dirty.** Seed commit = last `main` commit before the OLDEST
   olean mtime in the restored tree (2026-08-16 `19e299946a` for
   `lake-cache/qou-v4-24-0` as of 2026-09-04). Measured: **1,494 of 2,600**.
3. `tools/full_rebuild.sh` over that list (put `Archimedean/PauliWitness/*`
   LAST — 25 modules at 10+ min each, nothing imports them — so the rest
   reports in ~90 min); Monitor on `^FAIL|^progress|^DONE`.

**TRAP — the per-module mtime criterion (`tools/dirty_closure.py`) is
UNSOUND and under-verified a merged claim.** It treats a module as clean when
its source's last commit is older than its olean's mtime. But a restored
tarball gives many oleans the EXTRACTION time, so an olean built from an old
source looks fresh. Measured: `QOU.KnotTheory` had `BraidWord.writhe` in its
source (line 86) and NOT in its cached olean; a sibling importing it was
reported "real red: the environment does not contain BraidWord.writhe" and
beaned as such (`qou-isps`) — it was green the moment the dependency was
rebuilt. The "157/158 library green" of #6674 was measured under that
criterion and is therefore a LOWER BOUND on staleness, not a verification;
the seed-closure rerun is the honest one. The mtime script stays only as a
fast pre-filter, never as the gate.

Other traps, each one cost a relaunch: an olean's mtime may be your OWN
earlier rebuild — derive nothing from one file's stamp; `pkill -f <script
name>` kills the shell that mentions the name (exit 144) — kill by PID; do
not run a second heavy `lean` beside the rebuild on this one-core box; the
sibling checker needs the UGB build dir on `LEAN_PATH` or two files fail
falsely; a file `main` deleted since your list was written reports as a FAIL.
Warm rate ~3-4 s/module. Content-block siblings (907+) are not modules; run
`tools/sibling_check.sh` after the library. Classify every red as
**mechanical port** vs **real** — and before beaning a real one, rebuild its
import cone under the SOUND criterion, then grep `.beans/` for it.

## TRAP — grep `.beans/` BEFORE opening a bean for a red list (2026-09-04)

The sibling pass of `qou-n9j7` found 41 red content-block `.lean` files and I
opened an umbrella bean (`qou-isps`) listing 35 of them as "real drift, not
touched". Bean `qou-e7xv` — a different session, PR #6540 and follow-ups —
had ALREADY swept the same 38 files to 1 (`qou-0xrn` the survivor) and landed
the repairs on `main` while my pass was running; my seven "mechanical fixes"
collided with theirs on rebase and were dropped for `main`'s versions. Corpus-
grep path 6 (`grep -rl <file stem> .beans/`) would have shown it in one
command. A red list is a *claim about the corpus*; it goes through the
checklist like any other, and a rebuild result older than the last `main`
merge is not a current claim.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| root mathlib oleans, healthy tree | `find .lake/packages/mathlib -name '*.olean' \| wc -l` | **3470** (6990 on 2026-09-03; 3407 on the 2026-08-29 seed) | 2026-09-04 |
| per-paper mathlib oleans (the OTHER half — always check both) | `find content/quantum-observable-universe/lean/.lake/packages -name '*.olean' \| wc -l` | **2846**; union mirror 5733 | 2026-09-04 |
| cold vs warm `lean`-direct, one Mathlib file | `time lean <file>` | 1m52s cold / 4.7 s warm; `user` 29 s / 4 s | 2026-09-03 |
| lean-direct rebuild of the H3-Gram cone (cold) | `lean -o … QOU/{Shared/DetFin,Machinery/MarkovTraceOnHecke,Machinery/HeckeH3GramNondegeneracy,Interactions/GramMatrixH3Symbolic}.lean` | 330 / 245 / 69 / 207 s | 2026-09-03 |
| whole-library build state | `lake build QOU` | red on pre-existing failures — **not** the gate | 2026-08 |

⚠ Never treat a number here as a threshold (a stale `~2919 healthy` row once read an evicted 6990 → 2919 tree as healthy).

## TRAP — `lean`-direct exit 0 certifies against the oleans ON DISK, which after a restore are a SNAPSHOT (2026-09-03)

A file that imports a module changed on `main` since the cache was seeded will
"check" against the OLD olean and pass. Measured: `MarkovIdentificationInstance`
got exit 0; rebuilding its 96-module QOU cone from current source with `lean -o`
in dependency order found `main` red in SEVEN modules from two commits
(`e526464c2d` retyped a hypothesis in nine modules but not their consumers;
`6164a8ab6e` deleted a lemma on a wrong "zero consumers" grep). Neither was
visible to a single-file check. Before claiming a cone is untouched:
`git diff --stat <branch-point>..origin/main -- lean/QOU/<dirs>`; if non-empty,
rebuild the changed modules and everything downstream (scratchpad script
`compile_order.sh`: `lean -o <olean> -i <ilean> <src>` per module, warm cache
makes each 2-8 s; the first is ~100 s). A helper that treats ANY output as
failure will stop on pre-existing linter warnings (`HeckeCoset`: 76) — filter
on `error`. Also: a big `git fetch` of a cache branch can fill the session
quota mid-rebuild and leave a 1.5G `.git/objects/pack/tmp_pack_*` that
`rm .git/objects/pack/tmp_pack_*` recovers. And the cone can change AGAIN
between your rebuild and your push: the same session then found the base
file of its own new module restructured on `main` (a class removed) — re-run
the diff at check-in time, not once.

## BASELINE — seed-closure library rebuild, 2026-09-05 (re-measure, do not quote)

`main` `60d79979ed`, seed `19e299946a`, `tools/full_rebuild.sh` over the
seed-commit closure: **1,497 of 2,600 modules, 13,940 s (3 h 52 min)**, of
which the 22 `Archimedean/PauliWitness/*` at the end took ~30 min total (not
10 min each this time — they had been rebuilt earlier in the day) and the
`Machinery/HeckeH4*` block maps ~85 min for one hundred modules. Result:
**1,495 green; 1 real red** (`ParticleInteractions/silver_ratio_beta_decay_null`,
3 proof errors, bean `qou-4a7a`); 1 false red from a missing `UGB` path (fixed
in the script). So the library on that `main` is green except one module.
Command to reproduce is the recipe above; expect ~4 h on this box.

