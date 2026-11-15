# lean-verifier — memory

Entry types: **STABLE** (trust it) · **TRAP** (durable failure mode) ·
**BASELINE** (a number — re-measure, never quote from here).

Seeded 2026-08-29 from `AGENTS.md` + the skill (governs where they disagree).
NOTHING is auto-injected here (measured) — read this yourself. Sibling files:

- `verification-harness.md` — false greens, partial overlays, exit-139, cone triage, FQN guards
- `authoring-traps-v4-24-0.md` — module moves, lexer tokens, the small-determinant recipe
- `session-log.md` — per-session ledger (append there, not here; restructured 2026-09-03)

---

## STABLE — staleness by LAKE'S OWN SOURCE HASH, not mtime/commit time (2026-10-05)

Every olean in the `a792c46d01b` seed has a `.trace` whose `inputs` holds
`["<abs path>.lean", "<Hash.ofText of the source>"]`. `import Lake` +
`(Lake.Hash.ofText (← IO.FS.readFile p)).val` reproduces it exactly
(KnotTheory: `10187092109162527967` both sides). Equal ⇒ own-fresh; then take the
import closure. Measured: 2540 fresh / 190 changed / 253 no-olean of 2983;
dirty closure 628; only **76** fell in the blocks' cone (rebuilt green in 3.5 min).
Driver: `scripts/lean-blocks-baseline/` (L3, bean `qou-1f1w`).

## TRAP — after a cache restore, `lean-direct-cone.sh` WITHOUT `-B` calls stale oleans "up-to-date" (2026-10-12)

Measured: on a fresh `lake-cache/qou-v4-24-0` restore, the cone tool reported all 21 modules of
#7612 `up-to-date` (313/313), yet `lean` on `QOU/Hecke/MarkovBondLetterColimit.lean` failed with
7 type errors — the restored `SchurWeyl/MarkovTraceInstance.olean` predated `e0adbb6c347`
(`ocneanuMarkovTrace` generalised from ℝ to any field). `scripts/lean_freshness.py` trusts the
restored olean. **Verify a PR against current main with `-B`** (forced rebuild of the QOU cone;
187 modules, 643 s, 4 jobs) or at least compile each changed file directly — a green
"up-to-date" after a restore is evidence about the cache, not the source. A PR (#7750) merged on
the unforced check before this was caught; the `-B` rebuild later confirmed it. (Stream 4, #7735.)

## TRAP — cache tarball stores `content/…` paths; the tree is `folio/…` (2026-10-05)

Extract with `tar xzf - --transform 's,^content/,folio/,'`, or the 2703 QOU oleans
land in a `content/` dir nothing reads. `lean-content-sweep.sh`,
`lean-library-sweep.py`, `lean-shadow-verify.sh`, `lean-restore-gap-oleans.sh`
still glob `content/*` (read, not run) — the first finds zero targets.

## TRAP — `git push` from the shallow main clone streamed GIGABYTES (2026-10-05)

A 2-commit branch: `pack-objects --shallow` had written 1.87 GB after 16 min.
Push instead from a throwaway bare repo: `fetch --depth=1 --filter=blob:none`
the base sha, `fetch` the branch from the local repo, `fetch --deepen=30
--filter=blob:none origin main` until the base is an ancestor of
`origin/main` (check `rev-list --objects br --not origin/main | wc -l` is tiny
— 16 here), then push: 2.6 s. Also: a sibling session may switch the shared
worktree's branch under you — commit with a private `GIT_INDEX_FILE` +
`commit-tree` + `update-ref`.

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
  `qou`→`QOU` (`folio/quantum-observable-universe/lean/`), `ugb`→`UGB`, `fred2005`→`Fred2005`.
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

## STABLE — the 6-line control that PROVES `-DautoImplicit=false` is live (2026-09-13)

A bare `lean` is a **weaker** check than `lake build`: it does not read the
lakefile, so `autoImplicit` stays at Lean's default `true` while both lakefiles
set it `false`, and an unbound identifier is silently auto-bound instead of
erroring. Don't take that on trust in a new container — it is a 10-second
two-sided control, and `scripts/lean-direct-env.sh` does **not** set the flag
for you:

```lean
import Mathlib.Algebra.Ring.Defs
theorem ctl (x : Unbound) : x = x := rfl   -- `Unbound` declared nowhere
```

Measured here: bare `lean` **exit 0**; `lean -DautoImplicit=false` **exit 1,
`Unknown identifier `Unbound``**. Always pass `-DautoImplicit=false -s 65536`
(the `-s` mirrors the paper lakefile's `moreLeanArgs`; one generated module
overflows the default stack and aborts as a bare exit 134 with no source error).

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

## TRAP — `lean-build-bg.sh`'s anti-eviction guard CANNOT FIRE on a trace-paired restore (2026-09-13)

The SessionStart script has a guard that skips `lake build` when it sees a
restored cache. **It is keyed on `n_olean > 100 && n_trace == 0`** — so it
protects only the *untraced* restores the old blanket rule described. The live
seed `a792c46d01b` is **100 % trace-paired**, so `n_trace == 1` and the guard
**falls through to `lake build` every session start / compaction.**

Worse, it picks the tree wrongly for this purpose: `mathlib_lib` is the
**per-paper** `packages/mathlib/.lake/build/lib/lean` when that dir exists, and
after a `lake update` that dir holds **5** oleans (`Cache/*`, the `cache` exe) —
under the 100 threshold, so the guard cannot fire on that branch either. The
restored 3480 at the ROOT are never looked at.

So on a restored container the guard is inert in both directions. First move in
a session: read `/tmp/qou-lean-build-status.json` (it names the step without any
`pgrep` self-match) and **kill the chain by PID** — the script, `lake update`,
and the `cache get` child. `cache get` is guaranteed futile here anyway: the
Azure blob 403s every shard (measured 1655 failed / 0 downloaded of 7335).

## TRAP — a guard whose regex needs MORE path components than your listing has is VACUOUS (2026-09-13, mine)

Before extracting the cache I listed the archive truncated to **4** path
components and grepped it for `^content/[^/]+/lean/\.lake/packages` — which
needs **5**. It could never match; the "GUARD OK" it printed was about nothing,
and I nearly extracted 1.7 GiB over a live Mathlib source clone on the strength
of it. **Prefer a mechanical guard to a check you can fool yourself with:**
`tar xzvf - --exclude='content/*/lean/.lake/packages/*'` makes the property true
by construction regardless of what the archive holds, costs nothing, and `v`
into a file gives you the full manifest to audit afterwards (tar cannot list and
extract in one stream any other way). Same family as the `sed`-matching-nothing
false green in §19.

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

## STABLE — stream the parts INTO `tar`; do not materialise the tarball (2026-09-11)

The leak trap below exists only because the documented recipe writes one
~1.7 GiB temp file. It does not have to. Fetch into a **throwaway** repo under
`/tmp` (a fetch into the real `.git` is unreclaimable without gc — and `.git`
here is already 12 G), then pipe:

```sh
T=/tmp/cachefetch; rm -rf $T; git init -q $T
git -C $T remote add origin https://github.com/litlfred/qou   # proxy supplies auth
git -C $T fetch --depth=1 -q origin lake-cache/qou-v4-24-0    # 95 s, 1.7 G
C=$(git -C $T rev-parse FETCH_HEAD)
P=$(git -C $T ls-tree --name-only $C | grep '^lake-oleans\.tgz\.part' | sort)
( for p in $P; do git -C $T show "$C:$p"; done ) | tar xzf - -C /home/user/qou
echo "PIPESTATUS=${PIPESTATUS[*]}"   # must be '0 0'; a truncated stream is silent
rm -rf $T
```

Measured 2026-09-11 on a fresh container: fetch 1m35s, extract **50 s**, peak
disk 32 G used / 6.0 G free, back to 7.7 G free after `rm -rf $T`. **Nothing to
leak, so no `trap` needed** — but keep the `trap` if you do use `$TGZ`.

## TRAP — the restore's temp tarball is ~1.6G and nothing reaps it

One leaked `/tmp/tmp.*` survived thirteen days and drove the container to
**92K free**, where the Bash harness cannot write its own output and *every*
command fails, including the `rm`. Keep `trap 'rm -f "$TGZ"' EXIT INT TERM`.
`df` lies: ~252G nominal at 100% with ~38G used = a per-session quota near 38G.

## TRAP — when the disk fills, the LEAN TOOLCHAIN ITSELF is the biggest /tmp entry, and deleting it breaks Lean (2026-09-12)

Hit the 0-free state the TRAP above describes, and the instinct "clear the big
things in /tmp" is a trap of its own. Measured this container:

    2471 MB  /tmp/lean-v4.24.0          <- THE LIVE TOOLCHAIN. DO NOT DELETE.
     697 MB  /tmp/lean-v4.24.0-linux.zip  <- already extracted; safe
      56 MB  /tmp/claude-code.log         <- safe
     173 MB  /tmp/claude-0                <- task outputs + scratchpad

`~/.elan/toolchains/lean-v4.24.0` and `leanprover--lean4---v4.24.0` are both
**symlinks into `/tmp/lean-v4.24.0`**, so `rm -rf` on that directory removes the
compiler while leaving elan believing it is installed. Verify before deleting
anything large in /tmp:

    readlink -f ~/.elan/toolchains/*     # anything pointing into /tmp is LIVE

**The good reclaims, in order of value.** A merged sibling **git worktree** is
usually the largest safe one — 1500 MB here — because each carries its own
`.lake`. Check it is clean first, then use `git worktree remove` (not `rm -rf`,
which leaves a stale registration):

    git worktree list
    git -C <wt> status --short | wc -l       # must be 0
    git -C <wt> log --oneline @{u}..HEAD | wc -l   # must be 0
    git worktree remove <wt>

That removes the checkout, **not the branch ref** — so it does not violate the
never-delete-merged-branches rule. Zip + log + worktree freed 2.3 G here.

**Two harness facts that make this confusing while you are in it.** The Bash
tool writes its output capture under `/tmp/claude-*/tasks`, so at 0 free
*every* command reports "output could not be read" even when it ran fine —
issue deletes blind and check `df` afterwards. And a background job that was
mid-run when the disk filled dies with its output lost; re-run it after
clearing rather than assuming it finished.

**Cost of the cleanup, so budget it:** clearing `tasks/*.output` also removes
the subagent transcripts, and `rm -rf $SHADOW/QOU` removes the lean-direct
oleans — so the next `lean`-direct verification needs the dependency chain
rebuilt from the restored cache before the file under test will compile.

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

## STABLE — UGB *IS* in the qou cache as of the 2026-09-06 reseed (corrected 2026-09-11)

**The heading below is SUPERSEDED; the recipe under it is still the fallback.**
`lake-cache/qou-v4-24-0` head **`a792c46d01b`** (the 2026-09-06 gap-filled,
20-part, 1.70 GiB seed) extracts **6492 oleans** and carries all three paper
packages: root packages **3758**, QOU **2703**, **UGB 29**, **Fred2005 2** —
plus the seven `mathlib-gap` modules (`RingTheory/HopfAlgebra/Basic`,
`Topology/FiberBundle/Basic`, `Analysis/Complex/UpperHalfPlane/Basic`, … all
verified PRESENT). So on a fresh container **one restore is the whole job**:
no `lake-cache/ugb-v4-24-0`, no `…-root-import-closure`, no
`scripts/lean-restore-gap-oleans.sh`. Verify by counting before fetching an
addon. Trace coverage measured **100.0 % in all three trees** (3758/3758,
2703/2703, 29/29) — so `.lake/RESTORED-NO-TRACES` is correctly ABSENT, and
the old blanket "a restored tree has no traces" is false for this seed.

### superseded (2026-09-05): UGB is NOT in the qou cache; build it lean-direct in ~4 min

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
their `import UGB.` lines, then from `folio/unital-groebner-bases/lean`
`lean -o .lake/build/lib/lean/<M>.olean -i …ilean <M>.lean` with `LEAN_PATH` =
that output dir + every `.lake/packages/*/.lake/build/lib/lean` under BOTH the
repo root and `folio/quantum-observable-universe/lean`. **29/29 exit 0, ~4 min
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
   each olean before rebuilding it (else you truncate the shared inode). The
   same rule has a **second failure direction**: an overlay placed *after* the
   real tree is **inert**, not layered — `lean` never falls through to it for a
   module the earlier root also has (measured 2026-09-14; harness §2).
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

## TRAP — a theorem that IS a refutation needs more than the gate → `verification-harness.md` §19

**A `False`-CONCLUDING theorem is a different animal — §19a.** The stock
instruction *"prove `0 = 1` from the same hypotheses; if you can, they are
contradictory and the theorem is vacuous"* **cannot discriminate**: `False.elim`
gives you `0 = 1` for every *true* such theorem, and the hypothesis set is
unsatisfiable *necessarily* (else the theorem is false). Both questions are
answered before you open the file. The discriminating test is **DROP-ONE** — for
each hypothesis, a witness satisfying the other `n−1` **and refuting that one**,
stated as one conjunction so the second half is forced. Measured 2026-09-14: 6/6
on `no_triangle_of_triples`. And put a **negative control on your own adversarial
file** (4-5 deliberately false `example`s, require exit 1 at each seeded line) —
the §19 guard-the-harness rule, which does not otherwise apply when nothing is
`sed`-mutated.

`exit 0` + clean `#print axioms` does **not** detect an unused or unsatisfiable
hypothesis, and for a refutation that failure mode "proves" a route dead on
nothing. A red mutant proves only **syntactic** dependence (`rewrite failed`);
the claim worth making needs a concrete instance where the hypothesis **fails
and the conclusion fails with it** — `A = R = ℚ` + `norm_num` does it in three
lines. Also check whether a restrictive-looking binder is actually *free* (here
`u : Rˣ` is forced by the quadratic, which WIDENS the refutation), and
`grep` every backticked declaration the docstring cites: one was dangling, and
a `section` name is not part of a full name. Guard the mutation harness — a
`sed` that matches nothing yields a green run reported as a pass.

## STABLE — the honest dispositions when a proof will not close

Exactly three (AGENTS.md §1a / §"Strict Lean Discipline"): **prove it**;
**queue it** — the *real* proposition with `sorry` + `-- Ref: [key]` matching
`folio/schema/references.ts`; **demote it** — a `conjecture`, or a
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
(bean `qou-n9j7`, PRs #6649/#6674), from `folio/quantum-observable-universe/lean`:

1. Full topological order of `QOU/**/*.lean` → `/tmp/full_topo_all.txt`
   (regenerate it; `main` adds modules daily).
2. **Dirty = source changed since the cache's SEED COMMIT, or olean missing,
   or an import dirty.** Seed commit = last `main` commit before the OLDEST
   olean mtime in the restored tree. **Re-measure it per container** — it is
   `bbb4127145` (2026-08-23 17:00Z) here on 2026-09-14, against the
   2026-08-16 `19e299946a` this line carried since 2026-09-04. Measured then:
   **1,494 of 2,600**.

   **The oldest-olean heuristic is a LOWER BOUND on the seed, and on a
   RESEEDED cache it can be far too old (2026-09-14).** `tar` preserves the
   archive's mtimes, which are *build* times, and a reseed from an
   incremental `lake build` rewrites only what was dirty — so one tarball
   holds oleans built across weeks. Measured in one restored tree: oldest
   **QOU** olean 2026-08-23, oldest **mathlib** olean 2026-09-06, a 14-day
   spread in a cache the branch describes as one 2026-09-06 seed. Too-old a
   seed **over**-reports staleness, which is the safe direction (you rebuild
   more than needed) — unlike the mtime criterion below, which under-reports.
   Do not read a closure count as the true dirty set in either direction.
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
| root mathlib oleans, healthy tree | `find .lake/packages/mathlib -name '*.olean' \| wc -l` | **3480** on the `a792c46d01b` seed — REPRODUCED exactly 2026-09-13 (3470 on 2026-09-04; 6990 on 2026-09-03) | 2026-09-13 |
| per-paper mathlib oleans (the OTHER half — check, but it may not EXIST) | `find folio/quantum-observable-universe/lean/.lake/packages -name '*.olean' \| wc -l` | **10**, and NONE is a `Mathlib/` olean — a `lake update` clones the deps and builds only the `cache` exe (5 `mathlib/Cache/*` + 3 batteries + 2 `lakefile.olean`). So still **ONE `Mathlib/` olean root, no shadowing, no union mirror** — but the SOURCE clone now lives here and a restore must not clobber it (0 on 2026-09-11; 2846 on 2026-09-04) | 2026-09-13 |
| whole restore, fresh container | `find . -name '*.olean' \| wc -l` | **6492** = root 3758 (mathlib 3480) + QOU 2703 + UGB 29 + Fred2005 2; archive = 32461 entries / 6492 olean / 6493 trace. Tree read 6502 = those +10 pre-existing. Trace coverage **100.0 % (3758/3758)** | 2026-09-13 |
| restore cost, streamed (no tarball on disk) | §STABLE streaming recipe | fetch **1m33s** (1.70 GiB, 20 parts), extract **58 s**; disk 16 G → 25 G used, 14 G free | 2026-09-13 |
| lean-direct, 3-import Mathlib-only file (`Mathlib.Tactic` + `Ring.Defs` + `Fin.VecNotation`) | `time lean -DautoImplicit=false -s 65536 <f>` | **19.8 s cold / 2.9 s warm**; `user` 2.0 s BOTH — cold page cache, not a rebuild | 2026-09-13 |
| restore ALREADY present + bg build running | as above | **6502** = root packages 3758 (mathlib 3480) + per-paper build 2703 + per-paper packages 10 + UGB 28 + Fred2005 2. Root 3758 AND per-paper-build 2703 both matched the seed EXACTLY ⇒ restore in place, **no fetch** (10408 on 2026-09-12, when per-paper packages held 3813). Root mathlib **100 % trace-paired** (3480/3480) | 2026-09-14 |
| union mirror over both trees, one `MathlibExt` file | `cp -aln` per §17 | **6687 oleans, 5.1 G apparent, `df` free UNMOVED** (12 G before AND after `rm -rf`) — hardlinks; also immune to the concurrent `lake build`. Real trees unchanged after removal (3758 / 2816 / 3813), so the `rm -f`-before-write rule held | 2026-09-12 |
| lean-direct, `MathlibExt/HeckeTowerWitness.lean` (warm) | `time lean -DautoImplicit=false -s 65536 <f>` | **2.9 s** wall / 4.0 s user; dep rebuilds 51 s cold (user 5.6 s — page cache) and 2.8 s warm | 2026-09-12 |
| cold vs warm lean-direct, `QBeta/ConventionDAdmissibleRoots.lean` | `time lean -DautoImplicit=false -s 65536 <f>` | **1m05s cold / 4.5 s warm**; `user` 3.3 s both — cold PAGE CACHE, not a rebuild | 2026-09-11 |
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

## TRAP — a segfaulting `lean` can be the TOOLCHAIN, not the olean cache (2026-09-06)

`import Mathlib.*` exiting **139** here was diagnosed for days as a cache problem. It
was not. The **toolchain's own core oleans** under `/tmp/lean-v4.24.0/lib/lean` were
byte-inconsistent, and `gdb` put the fault in `ImportedModule_getData_x3f` — reading an
imported module's mmapped region. Scope: `Init`, `Lean.Expr`, `Lean.Parser`,
`Lean.Environment` all exit 0, but ~40 of 89 `Lean/Elab/*` modules segfault, so anything
needing the elaborator dies, and every Mathlib module reaches it via `Mathlib.Init`.

**🛑 The artifact-count discriminator OVER-FIRES — measured 2026-09-11.** This
container's `/tmp/lean-v4.24.0/lib/lean` holds **1885 `.olean` / 1885 `.ilean` /
0 `.trace` / 0 `.c`** — two of the four at zero, which the rule below calls
corrupt — and the toolchain is **healthy**: `theorem t : 1+1=2 := by decide` plus
`#eval` exits 0, and every Mathlib-importing file compiles. The GitHub-release
zip simply does not ship `.trace`/`.c`. **Run the elaborator, don't count files:**
a 2-line scratch with a `by decide` and an `#eval` is the sound 15-second test;
fall back to counting only to explain a segfault you have already observed.

**The (weaker) count check:** count the FOUR artifact
types under the toolchain's `lib/lean`. A healthy 4.24 core has all four in near-equal
numbers (measured: 1885 / 1884 / 1884 / 1884). Mathlib itself legitimately has
`.olean` only and **zero** of the other three — it is not module-system'd at
`f897ebcf72cd` — so zeros there are NOT a defect and the cache branch has never carried
them. Do not "fix" the cache on the strength of that.

**The repair, measured end to end, ~10 min and NON-destructive if staged:**

```sh
C=$(git rev-parse FETCH_HEAD)     # after: git fetch --depth=1 origin lake-cache/toolchain-v4-24-0
P=$(git ls-tree --name-only "$C" | grep '^lean-toolchain\.tgz\.part' | sort)
mkdir -p /tmp/lean-tc-stage
( for p in $P; do git show "$C:$p"; done ) | tar xzf - -C /tmp/lean-tc-stage   # no archive stored
# TEST the staged binary BEFORE swapping, then repoint both elan symlinks:
ln -sfn /tmp/lean-tc-stage/leanprover--lean4---v4.24.0 /root/.elan/toolchains/lean-v4.24.0
ln -sfn /tmp/lean-tc-stage/leanprover--lean4---v4.24.0 /root/.elan/toolchains/leanprover--lean4---v4.24.0
```

Same file, same `LEAN_PATH`: staged **EXIT 0**, old **EXIT 139**. Stage to a NEW path and
test first — then nothing working is at risk, and a failed restore costs only disk.

**`scripts/lean-toolchain-cache-restore.sh` will NOT do this for you.** It skips when a
toolchain matching the pinned version is already installed, and a corrupt toolchain still
prints `Lean (version 4.24.0, …)` perfectly. Version match is not health.

**Budget ~2.2 G to stage.** This container hit **223 MB free**. Hardlinking the 28,063
byte-identical oleans shared by the root and per-paper mathlib trees (SHA-256 compared,
identical files only, neither tree deleted) reclaimed **2.76 GiB**.

## TRAP — `pkill -f <script>` kills the shell running it (2026-09-06)

The shell's own command line contains the pattern, so `pkill -f ptolemy_class_sweep`
terminates the caller. `ps | awk '/[p]tolemy.../'` does not help: the bracket trick stops
the awk PROGRAM matching itself, not the surrounding bash command line. Cost two turns.
Kill by PID.

**Same defect in the DETECTION direction, and AGENTS.md hands it to you (2026-09-12).**
§17a says *"First move in a fresh session: `pgrep -f 'lake build'`"* — and that command
**self-matches**, because the harness wraps every call in a `bash -c` whose command line
contains the pattern. Measured: it returned two PIDs, both my own shell, alongside a
`lean -o` query that did the same; the genuinely-running `lake` was a *third* process the
noise nearly buried. **Filter the harness out** —
`ps -eo pid,etime,cmd | grep -E '(lake|lean) ' | grep -v shell-snapshots` — or read
`/tmp/qou-lean-build-status.json`, which names the step (`update`/`build`) and the attempt
count without any matching at all.

## STABLE — the SessionStart `lake build` log may already CONFIRM your diagnosis (2026-09-12)

AGENTS.md notes `/tmp/qou-lake-build.log` is kept; the point worth having is that it is an
**independent second opinion from the canonical path**, free. Verifying one new file, the
background build (not commissioned by me, and *failed* — status `attempts: 5`) had reached
`✖ [6641/6642] Building QOU.MathlibExt.HeckeTowerWitness` with the **identical** error my
lean-direct gate found, at the same `188:59`. One `grep '✖'` turned a single-harness claim
into two agreeing methods, and simultaneously showed the other **6641** modules building.
A `status: failed` in that JSON is therefore not a reason to ignore the log — read it
*first* and check whether the sole failure is the file you were sent to verify.

**🛑 DATE THE LOG BEFORE BELIEVING IT — measured the SAME DAY, on the same file.** The
entry above is true of the run that produced it and reads as though the log is always
current. It is not: it is written **once per session start** and never refreshed. Second
pass on `HeckeTowerWitness.lean`, the log was stamped **18:43 UTC** against a fix commit at
**19:00** and a further edit at **19:08**, so its `✖` — same module, same `188:59`, same
`Set.image_subset` deprecation — described a file **two revisions dead**. Quoting it would
have reported a fixed defect as live, with the authority of "two agreeing methods".
Discriminator, three cheap fields: `ls -la /tmp/qou-lake-build.log` vs
`git log -1 --format=%ci` on the file **and** its `ls -la` mtime. Older than either ⇒ it is
history, not a second opinion. (The `timestamp` in `/tmp/qou-lean-build-status.json` dates
the same run.)

## TRAP — `lean-library-sweep.py` measures the CONTAINER when the olean tree is empty (2026-09-07)

The sweep's value comes from its *dirty closure*: rebuild only modules whose olean
predates their source. In a container whose QOU olean tree was never populated, every
module is "never built (new)", so the closure is the **whole library** and the sweep
becomes a full from-source rebuild without Lake's ordering. Measured here:

```
library modules        2775
  source-changed          1
  never built (new)    2773
  DIRTY CLOSURE        2774
```

In the ~12 % it covered before being stopped it reported **195 RED / 147 ok**. That is
irreconcilable with the **0 red** whole-corpus result recorded on `main` on 2026-09-05
(261 content blocks + 74 dirty library modules), and the discriminator is the closure
size, not the code. **A high red rate from this script is a symptom of an empty olean
tree — do not report it as a corpus finding.**

Two further mechanics worth having:

- **Read the header before the verdicts.** `DIRTY CLOSURE` ≈ `library modules` means the
  run is a full rebuild and its runtime and reds are both about the container.
- **Do not pipe it through `tail`.** The per-module verdicts stream but the summary is at
  the TOP; `| tail -30` discards every verdict before the alphabetical tail and leaves
  only `SKIPPED … (red dependency: …)` lines, which read as a corpus-wide failure. Cost a
  15-minute re-run.

**What to do instead when the branch touches few files.** Verify the changed module's
actual import cone from source. `LEAN_PATH` with a scratch dir FIRST, rebuild each QOU
dependency from source into it, then compile the changed file against that. For a module
whose only QOU import was one file this was **55 s + 5 s** against an hour of sweep, and
it is the stronger claim — an `exit 0` against the restored cache is a statement about
the snapshot, this one is about the source. Mind the partial-overlay rule already in this
file: the scratch root captures the namespace it contains, so it must hold every
`QOU.<Ns>.*` module the file imports.

## TRAP — an "incomplete" olean tree may be one a `lake build` is WRITING (2026-09-08)

`scripts/lean-build-bg.sh` is started by a **SessionStart hook** and runs `lake
build` with cwd = the paper package, so the per-paper tree is under construction
from minute one of a fresh session. Measured over ~40 min, one session: per-paper
went 2 -> 17 QOU oleans and 2352 -> 3007 mathlib oleans while root sat unchanged
at 2442 / 3469. So a count is a snapshot of a moving target, and a "missing"
`Mathlib/Tactic.olean` can be a TIMING fact rather than a fact about the restore.
The root restore is NOT evicted by this build (its cwd is the paper package).

It reached the GATE: `lean-shadow-verify.sh` picked a **2**-olean tree over the
restored **2442**-olean one and died on the first Mathlib import, reporting a
failure entirely its own. Fixed on
`claude/w1-route2-fibre-monodromy-order-2026-09-07` (pick by count, rank package
locations, warn on a running build).

**First move in a fresh session: `pgrep -f 'lake build'`.** Full detail, and why
§17's union mirror is still the stronger tool than ranking:
`verification-harness.md` §17a.

- **TRAP (2026-10-12, PR #7747): a partial extra olean root SHADOWS the full one.** Lean resolves a module by the FIRST `LEAN_PATH` root that contains its top-level directory (`Mathlib/`), not the first that contains the file. So prepending a scratch dir holding only 2 newly built Mathlib oleans made every other Mathlib import fail with "object file … does not exist". **Fix:** `cp -al` the whole `.lake/packages/mathlib/.lake/build/lib/lean/Mathlib` into the scratch root, unlink each target before writing it with `lean -o`, then build into it. Also: the root `.lake/packages/mathlib` holds oleans only, with no `.lean` sources; sources are in `folio/quantum-observable-universe/lean/.lake/packages/mathlib` (same rev, f897ebc). A module that no QOU file imported (e.g. `GroupTheory.GroupExtension.Defs`, `GroupTheory.SemidirectProduct`) is ABSENT from the cache and must be built this way.
