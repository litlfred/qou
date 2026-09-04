# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + the skill (which governs where they
disagree). **NOTHING here is injected** — measured, and your definition's FIRST
ACTION section says so: you must `Read` this file yourself. The ~200-line cap is
therefore a courtesy bound on what you must read, not a truncation point.
Detail lives in sibling files, read on demand:

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

`git log -- <file>` bottoms out at the shallow graft, which shows *nearly every*
file as last-touched by one commit (`b831ff34c3` 2026-08-29; `c9c12648e4`
2026-08-31 as of 2026-09-04). So "olean dated Jul 2, source committed Aug 29" is
undecidable from git — do not argue freshness from it; rebuild the cone instead.
`git diff <merge>^1 <merge> -- '*.lean'` DOES work and is the way to scope what a
merge actually changed.

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
cwd = repo root; absolutise them (cwd resets between calls).

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

## TRAP — the restore's temp tarball is ~1.6G and nothing reaps it

One leaked `/tmp/tmp.*` survived thirteen days and drove the container to
**92K free**, where the Bash harness cannot write its own output and *every*
command fails, including the `rm`. Keep `trap 'rm -f "$TGZ"' EXIT INT TERM`.
`df` lies: ~252G nominal at 100% with ~38G used = a per-session quota near 38G.

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
(measured 2026-08-29). Refresh by passing the **BLOCK STEM** — `qa-sweep
content/<paper>/<chapter>/<block>`, no extension — which rewrites only that
block's `.qa.json` in ~1–2 min (corrected 2026-09-03, measured on six blocks;
the older "pass the directory" reading is what rewrites all 128). A bare file
path still dies `ENOTDIR`. `check-sidecars.sh` prints the stem command per
file and keeps saying "→ refresh" after a successful one — it lists applicable
criteria, it is not a staleness detector; compare `source_hashes.lean` to
`sha256(file)[:12]` yourself.

## TRAP — false greens and corrupt oleans → `verification-harness.md`

1. **Green against a STALE dependency olean is a FALSE GREEN.** Imports resolve
   from disk; a consumer compiles against the olean its dependency had *before*
   the edit (measured 2026-08-30: exit 0 → exit 1 once rebuilt; red on `main`
   six days). Rebuild each changed module from source, then its reverse-import
   cone computed from the import graph — a grep for `[Foo …]` binders misses
   files that *construct* an instance.
   **A GENERALISATION never trips this, so passing proves nothing about
   currency** (2026-09-04): the tree's olean had `(P M s c : ℝ)` while the source
   had `{R} [CommRing R] [IsDomain R] (P M s c : R)`, and the new consumer
   compiled clean against BOTH — at `R = ℝ` the generic decl specialises to the
   old one. Diagnose currency with `#check @<decl>` against each olean (a
   `grep -c -a <name>` cannot see it: the NAME is in both), never from the
   consumer's exit code.
2. **A partial `LEAN_PATH` overlay shadows the whole namespace** — the first
   root holding a `QOU/` dir wins. Use a complete `cp -al` mirror, `rm -f`-ing
   each olean before rebuilding it (else you truncate the shared inode).
3. **Disk-full builds write truncated oleans that segfault**: exit 139, zero
   errors, 0–1 s. Olean SIZE is not a test (50–226 KB inside a normal range).
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
tokens under `Mathlib.Tactic`; rename such binders.

## TRAP — a docstring figure is sourced from somewhere; check it → harness §9

A file quoted CODATA-**2018** figures (`t = 2.0975e-7`) from its cited probe's
hardcoded `R_exp` while `constants.py` serves CODATA 2022 — Lean untouched, prose
stale on arrival. 2026-09-04, same class: `Checks.refCodata = 137.035999084` is
absent from the witness its docstring names (only under `computations/_deprecated/`)
and has **no consumer**. Diff the literal against the named source; §9 also has
the inhabitation check for a `structure … : Prop` sold as content-bearing.

## TRAP — an olean is a SNAPSHOT; source newer than olean ⇒ not your checkout → harness §11

Imports resolve out of oleans built at some earlier commit (a cache-branch seed,
or just an older build), so a file whose cone moved since is checked against old
declarations — silently, error pointing at your call site. `ls -l <olean>` vs the
source mtime before trusting a green OR debugging a red (git cannot date it —
shallow graft, TRAP above). Rebuild the cone; it is cheap (13 modules, 178 s).
Worked 2026-09-04: `AlphaEM/FormLadderAnchorDominance.olean` Aug 24 against a
Sep 3 source, with its brand-new consumer `…Checks.lean` about to be "verified"
against it. Does NOT invalidate every restore.

## TRAP — DOCSTRING PROSE reads as code to any line-oriented matcher (2026-09-04)

This corpus writes long docstrings that *quote* Lean syntax, so both halves of a
"count the `sorry`s + probe every decl" task were wrong first time.
**`grep -cw sorry` counts `sorry-free`** (`-` is a non-word char): raw totals
over 8 files were `sorry`=1, `axiom`=2 — **all 4 hits prose, code-level 0**.
And a `^\s*(def|theorem|class|…)\s+(\w+)` decl regex ate `theorem below does
not…` → `below` and `class instance (the conjecture)` → `instance`, whose
`#print axioms` lines errored and one of which swallowed a real probe line by
cascading into `unexpected token '#print'`. **Print matching LINES, never a bare
count; strip comments before a decl scan, or reconcile emitted names vs output.**

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| mathlib oleans, root tree | `find .lake/packages/mathlib -name '*.olean' \| wc -l` | **3470** (6990 on 2026-09-03; 3407 on the 2026-08-29 seed) — swings widely, never a threshold | 2026-09-04 |
| QOU oleans, root vs per-paper | `find <tree> -path '*QOU*' -name '*.olean' \| wc -l` | root **2442** w/ 2441 `.trace` = a REAL build tree (no `RESTORED-NO-TRACES`); per-paper **833**. Root was the complete one | 2026-09-04 |
| cone rebuild into a `cp -al` mirror | `lean -o "$MIRROR/QOU/…" "$LEANLIB/QOU/….lean"` | 13 modules / 178 s (48 s cold first, 78 s `Mass.QIntegerBarParity`, rest 2–11 s). H3-Gram cone 2026-09-03: 330/245/69/207 s | 2026-09-04 |
| target file, lean-direct, warm | `lean <file>` | 1.6–5.6 s (8 chapter+library files). One Mathlib file cold 1m52s / warm 4.7 s; `user` 29 s / 4 s | 2026-09-04 |
| whole-library build state | `lake build QOU` | red on pre-existing failures — **not** the gate | 2026-08 |

⚠ Never treat a number here as a threshold (a stale `~2919 healthy` row once read an evicted 6990 → 2919 tree as healthy).
