---
# qou-tpdg
title: The library sweep points at the wrong Mathlib tree — 22 false REDs, and the 2.3GB shadow is redundant
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T11:48:55Z
updated_at: 2026-10-04T15:14:12Z
parent: qou-5vkl
---

## 2026-09-05 — measured, fixed, verified. PR #6827

`scripts/lean-library-sweep.py` is the gate AGENTS.md adopted TODAY for any
branch touching `.lean`, and in this container it was measuring itself.

**The mechanism (the reusable part).** Lean commits to the FIRST `LEAN_PATH`
root containing the module's TOP-LEVEL NAMESPACE DIRECTORY and never consults a
later root for anything under it. Measured 3 ways on one import whose olean IS
present in the real tree (476544 B):

  first root has no `QOU/`                    -> exit 0  (falls through)
  first root has `QOU/` + 1 unrelated module  -> exit 1  "does not exist"
  real tree only (control)                    -> exit 0

So a PARTIAL overlay MASKS the tree behind it. The error names the OVERLAY
path, so it reads as "missing from the corpus" when the module is present and
merely unreachable.

**Defect 1 — wrong Mathlib tree.** LEAN_PATH globbed `ROOT/.lake/packages/*`
plus each paper's own BUILD OUTPUT, never each paper's `.lake/packages/` — which
is the one the documented restore fills:

  ROOT  mathlib: Tactic.olean 0 BYTES (Aug 7), Data/Real/Basic MISSING, 1212
  PAPER mathlib: Tactic.olean 68040 B (Aug 29), Data/Real/Basic 785328 B, 3477

=> 22 REDs entirely about the environment, formatted like real findings.

**Defect 2 — the 2.3 GB copy.** `copytree` needs ~2.3 GB; 1.1 GB free against a
per-session quota, so the sweep died on ENOSPC having judged nothing. Now
hardlinked: `du` says 2.3 GB, `df` does not move. `build()` unlinks its target
(+ same-stem .olean.hash/.ilean) before `lean -o`, so no write through a shared
inode. Real-copy fallback on OSError.

**A claim of mine the measurement REFUTED.** I first read the copy as
REDUNDANT (shadow first, real tree last => should fall through). It does not —
see the mechanism. The full tree in the shadow is NECESSARY; hardlinking is what
makes it cheap. Shipping the first reading would have left the sweep judging
almost nothing while looking greener.

**Result.** RED 22 -> 0, skipped 15 -> 0, 22/22 ok, 33 s, 0 blocks of disk.
Safety verified not argued: the real tree's 2660 oleans snapshotted by inode,
size and mtime before and compared after — IDENTICAL on all 2660.

**Bonus:** `QOU.Braiding.SkeinNormalisation` reports `ok`, an independent
confirmation of the file merged in #6820.

**Still open / not done.** The AGENTS.md `lean`-direct recipe carries the same
overlay-masking trap (`LEAN_PATH="$SP/oleans:$LP"`, overlay first) and is NOT
edited here — changing the primary Lean verification guidance is not a passing
change. And `scripts/lean-content-sweep.sh` was not audited for the same
LEAN_PATH defect.


## 2026-09-05 (cont.) — the SIBLING gate had the same pair, plus two more

`scripts/lean-content-sweep.sh` delegates its whole LEAN_PATH + shadow build to
`scripts/lean-shadow-verify.sh`, which carried BOTH defects (root-only package
glob; real `cp -a`) plus two of its own:

3. **The documented `SHADOW=<dir>` reuse path never created its directory** —
   `$SHADOW` was only made by `mktemp -d` in the branch where SHADOW is UNSET,
   so the advertised form failed on first use with `cp: cannot create
   directory`. Pre-existing.
4. **My own fix to (1) reintroduced the bug it fixed.** I wrote
   `ls -d <paper-pat> <root-pat>` and **`ls` SORTS its arguments**:
   `$ROOT/.lake/...` sorts before `$ROOT/content/...`, so the broken root tree
   came back FIRST and Mathlib still resolved against it. Replaced with a loop
   (glob expansion keeps written order). The original was safe only because it
   had ONE pattern.

## 🛑 CREDIT — the mechanism was ALREADY DOCUMENTED; I re-derived it

Line 27 of `lean-shadow-verify.sh`: *"Lean resolves a module from the first
LEAN_PATH root holding that package directory, so the shadow must be complete,
not a sparse overlay."* So my three-way measurement CONFIRMS a documented fact
rather than discovering one, and my empty-shadow experiment tested a question
the comment two lines from the code already answered. Audit doc corrected. What
is new is the quantification, and that the Python sweep carries no such comment
— which is why it was re-derived there.

**Verified (shell path):** `SHADOW=<dir> lean-shadow-verify.sh
QOU/Braiding/SkeinNormalisation.lean` -> EXIT 0, both dirty cone modules
rebuilt, target clean; real tree's 2660 oleans IDENTICAL in inode, size and
mtime before/after. Disk moved 1 MB across the run.


## 2026-09-05 — 🛑 REVIEW CORRECTION: my defect-1 claim was one container generalised

The sweep scripts' author reviewed #6827 and caught a real over-claim. On THEIR
container the ROOT mathlib tree is FINE:

  ROOT,  their container: Tactic.olean 68040 B, Data/Real/Basic 785328 B, 6990 oleans
  PAPER, their container: Tactic.olean 68040 B, Data/Real/Basic 785328 B, 3477 oleans

Byte-identical, and root is a SUPERSET. That is why their sweeps returned real
findings rather than 22 environment-REDs, and why they never hit this.

**So "the root tree is broken" is FALSE as a general claim** — true of this
container only. The defensible statement, which holds on both, is **"the root
tree is not GUARANTEED to be populated"**: AGENTS.md §"Mathlib cache 403
fallback" fills the PAPER tree, so that is the one the documented restore
guarantees. Globbing the root alone makes the gate correct BY LUCK OF
ENVIRONMENT, which is not a gate.

The fix is unchanged and still right; only its justification needed narrowing.
Corrected in the audit doc and in BOTH script comments (the comments matter
more — that is where the next agent reads it). This is the
absence-of-evidence discipline failing in the other direction: I measured one
environment and wrote a universal.

**Two of my other findings were CONFIRMED by the same reviewer**, from the
opposite side:

- **Defect 3 (`SHADOW=<dir>` never mkdir'ing) was LATENT for them, not absent.**
  They used that reuse form repeatedly and it worked — because their PYTHON
  sweep runs `shadow.mkdir(parents=True, exist_ok=True)` and they happened to
  run it first, leaving the directory for the shell one. They note they would
  have reported it as evidence against me had I not measured it.
- **Defect 2 bit them too.** The 2.3 GB copy drove their container to 2.2 GB
  free; they handled it by deleting shadows between runs, and call hardlinking
  strictly better. They also say the inode/size/mtime snapshot over all 2660
  files is the check they should have written when first pointing a script at
  the real olean tree.

They also confirm the namespace-pinning comment at line 27 is load-bearing
BECAUSE they got it wrong first: their initial shell version wrote into a
SPARSE shadow, Lean masked the real tree, and the comment is what they left
after debugging it. So the credit note was right and the three-way measurement
is the evidence that comment never had.

**Overlap settled:** main carries their LIB generalisation (#6830) plus 14
content-block and 1 UGB fix; I have merged the LIB half and nothing further
conflicts. They are explicitly NOT merging #6827 — it is mine to land.


## 2026-09-06 — full content sweep run to completion: 938 swept, 8 RED, 0 corpus defects

Retires the 'Not claimed' line in #6827's body. Three separate results:

1. **Scope**: the sweep is **938** files, not 261. AGENTS.md carried the
   pre-coverage-fix population (the `import QOU` filter reaches 262 of 938).
   Corrected; the sibling's script header already recorded the fix.
2. **All 8 REDs are a CACHE GAP, not corpus defects.** Exactly 4 of the 252
   distinct Mathlib modules the content corpus imports are absent from the
   restored cache (FiberBundle.Basic, HopfAlgebra.Basic, UpperHalfPlane.Basic,
   Real.Pi.Bounds); those 4 account for all 8. Absent from BOTH olean trees, and
   reproducible with no shadow and no sweep on a plain restored cache. So:
   930/938 verifiable and green, 8 unverifiable here.
3. **The real olean tree moved 2660 -> 2713 mid-sweep and NEITHER SWEEP DID IT.**
   scripts/lean-build-bg.sh, re-fired by this session's compaction, ran lake build
   concurrently. Read naively the diff accuses this PR's own fix of write-through.
   Methodology: quiesce the SessionStart build before trusting that invariant.

BONUS: that background lake build **independently confirms #6909** from the
canonical path — sole failure in 6459 modules, same six source positions — on a
branch carrying no .lean change.

Also corrected: this PR's body called an earlier '8 REDs' set 'artifacts of that
experiment'. Given the cache gap (reproducible with no shadow), that attribution
is unestablished and most likely wrong.

Audit: docs/audits/2026-09-06-full-content-sweep-938-and-the-cache-gap.md


## 2026-09-08 — first full QOU run since the fixes: 0 RED, and two things the summary line hides

Ran `scripts/lean-library-sweep.py --package QOU` on this container after editing
nine `QOU/Archimedean/*` modules (bean `qou-w3eg`). Verdict line:

```
=== library sweep: 539 ok, 0 RED, 0 TIMEOUT + 10 UNVERIFIED (NOT failing),
    31 skipped (dependency red), 961s ===
library modules 2787 | source-changed 161 | never built (new) 276
DIRTY CLOSURE 580 | snapshot-current 2207
```

**The fixes hold.** 0 RED across a 580-module closure, against the 22 false REDs
this bean was opened for. All nine edited modules green, including the two whose
signatures changed. 961 s wall.

### 1. `skipped (dependency red)` says RED when it means UNVERIFIED

The summary reads `0 RED … 31 skipped (dependency red)`, which contradicts
itself, and the per-line form is `SKIPPED X (red dependency: Y)`. Every one of
the 31 traces back to one of the 10 UNVERIFIED (environment) roots, directly or
through another skipped module — `TraceIsWeighted` and `RegTraceGramProduct` are
named as "red dependency" and appear nowhere in the log as ok/RED/UNVERIFIED,
i.e. they were themselves skipped.

So **zero** of the 31 is a corpus failure, and the word a reader sees is "red".
This is the same defect class the bean already documents one level up: an
environment condition formatted like a finding. A reader who trusts the summary
line concludes 31 modules are broken; the true count is 0.

Not fixed here — a label change to the shared gate is an owner call under the
2026-09-07 ASK-BEFORE-CHANGING directive, and this is a report, not a sweep.

### 2. The Mathlib cache gap is NOT closed for the library tree

[`docs/audits/2026-09-07-mathlib-cache-gap-closed.md`](docs/audits/2026-09-07-mathlib-cache-gap-closed.md)
is titled *"the gap is 3 targets / 7 modules … and it is closed"*, and its own
§ notes the population it measured: `import` lines of **content blocks**.

The **library** tree has a different, unrecorded gap. Four of the 10 UNVERIFIED
are `missing olean … (mathlib cache)` naming modules that appear nowhere in that
audit:

| absent Mathlib module | blocked QOU module |
|---|---|
| `LinearAlgebra.CrossProduct` | `QOU.Mass.TorusInflection` |
| `LinearAlgebra.PiTensorProduct` | `QOU.MassTheory.PiTensorMonomialBasis` |
| `RepresentationTheory.Homological.GroupCohomology.LowDegree` | `QOU.Eightfold.ObstructionH2Mathlib` |
| `RingTheory.SimpleRing.Matrix` | `QOU.MathlibExt.RegTraceGramNondegenerate` |

Verified absent from **every** mathlib olean tree in the container (`find -path
'*/mathlib/Mathlib/<m>.olean'` → 0 copies each).

**Do not read this as a retraction of that audit.** Its three targets are also
absent here, because `scripts/lean-restore-gap-oleans.sh` has not been run in
this container — so this run says nothing about whether the restore works. The
correction is to the audit's *scope*, not its result: "closed" is closed for
content blocks, and the library sweep needs four more targets nobody has seeded.

### 3. Six segfaults (`killed by signal 11`)

`QBetaWenzlDecomposition`, `WhiteheadLinkScaffold`, `PivotalCategory`,
`TwistedQuantumDimension`, `HeckeAlgebra.MarkovTrace`, `BraidKnot`. This is the
truncated-olean class already on the record (a 192512-byte
`ComplexDilogarithmSlit.olean` against a true 279688 killed its whole cone with
exit 139 and zero output). Six more cones, not yet diagnosed to a specific
truncated file. Container-scoped like everything else here.


## 2026-09-11 — RETRACTING two things from my 2026-09-08 entry above

Both are mine, both were inferred rather than measured, and a sibling session
(`qou-ed8a` / `qou-g5sp`, commits `ef2e7d9d710`, `61d93c97ff0`, `9df38bc4548`)
independently named the move on the same day: *"a property inferred from a
neighbour instead of measured on the thing itself."*

### 1. The six `signal 11` modules — attribution WITHDRAWN

I wrote that they are *"the truncated-olean class already on the record"*. I did
not measure that on any of the six. I matched a symptom (SIGSEGV) to a cone I had
diagnosed earlier in a different area and carried the attribution across.

The sibling refuted the structurally identical inference the same day: `#7124`'s
audit had listed the `QOU.Hecke*` H4 cluster as *"the same H4 family a sibling
measured as SIGSEGV"*, and both members then compiled **clean** — `HeckeH4BlockMap211`
ok in 1049 s, `HeckeH4BlockMap31` ok in 974 s. Whatever was measured elsewhere did
not transfer.

**A second hypothesis I never excluded, and it is now the more likely one.** I ran
`lean-library-sweep.py --package QOU` with **no `--jobs`**, i.e. the default 3, so
three `lean` processes shared this container. The sibling established that the
sweep's four TIMEOUTs were exactly that — `Witness12B` needs 1471 s of exclusive
CPU against an 1800 s budget charged as WALL CLOCK. Contention is a live
alternative for a signal-11 under memory pressure too, and my run cannot
distinguish it.

**So the standing claim is only:** six modules were killed by signal 11 under a
3-job sweep in this container, cause unmeasured. Re-running them alone
(`--jobs 1`) is what would settle it, and that is the sibling's in-flight work on
`qou-ed8a` — not duplicated here.

### 2. "Four more targets nobody has seeded" — STALE, by hours

That clause was wrong when written. `beec4c420ef` landed
[`scripts/lean-build-mathlib-gap-cone.py`](scripts/lean-build-mathlib-gap-cone.py)
the same day: it builds missing Mathlib oleans **from source** (79 modules,
188 s, 57 MB for its cone) and is additive by construction. One of my four —
`Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree` — is the
exact case it was written for.

**The scope correction to the 2026-09-07 audit still stands**: that audit measured
content-block `import` lines, and the library tree has its own gap. What does not
stand is that nobody had addressed it.

**One measurement to hand back rather than act on.** Run on my three remaining
seeds in this container, the script fails in about a second:

```
$ python3 scripts/lean-build-mathlib-gap-cone.py QOU.Mass.TorusInflection
dest     .../lean/.lake/packages/mathlib/.lake/build/lib/lean
MISSING  1 module(s) in 1 layer(s)
  [1/1] FAIL QOU.Mass.TorusInflection  (exit 1)
```

It classifies the **seed itself** as the missing module and tries to build a `QOU`
module into the *mathlib* destination tree; the Mathlib modules actually absent
(`LinearAlgebra.CrossProduct`, `LinearAlgebra.PiTensorProduct`,
`RingTheory.SimpleRing.Matrix`) are never reached. Same on all three.

The premise is fine — Mathlib **sources are present** here (6996 `.lean` against
3472 oleans), so these are buildable gaps, not container limits, exactly as
`beec4c420ef` argues. The difference from the case it was written for is that my
seeds have **no olean of their own** (they are in the sweep's dirty closure),
which is what appears to put the seed into the missing set.

Not fixed here: it is a sibling's script on a sibling's live bean, and the
duplication rule reserves settled mechanical work to one owner. Handing over the
repro.


## 2026-09-13 — §3's open question is SETTLED for two named modules: not contention, not the module

§3 above withdrew the truncated-olean attribution for the six `signal 11` modules
and named a second hypothesis — `--jobs 3` contention under memory pressure —
closing with *"my run cannot distinguish it."* This run distinguishes it, on two
**different** modules, and the answer is neither hypothesis.

Hit while verifying #7281 (`qou-qqm4`), `--only-exact QOU.Mass.ProductionChainBondProduct`:

    [2/12] UNVERIFIED  QOU.Mass.StrandLayoutForcesChain        (killed by signal 11)
    [5/12] UNVERIFIED  QOU.MathlibExt.DisjointBlockTraceLaw    (killed by signal 11)

**Reproducible across four configurations**, all after `lean-sync-olean-trees.sh`
(both mathlib trees at 3477, 1780 linked, 3 zero-byte oleans repaired) and after
`lean-restore-gap-oleans.sh` (86 oleans into both trees):

| configuration | result |
|---|---|
| `--jobs 2` (4 of 4 cores, 2 threads each) | signal 11, both |
| `--jobs 1` (4 threads) | signal 11, both |
| `--jobs 1` + caller `LEAN_NUM_THREADS=1` | signal 11, both |
| **lean-direct, same container, minutes later** | **exit 0, 0 errors, both** |

### What that excludes

- **Contention / memory pressure — REFUTED for these two.** `--jobs 1` with
  `LEAN_NUM_THREADS=1` is a single `lean` process with a single elaboration
  thread, and it still dies. This is the hypothesis §3 could not test.
- **A module defect — REFUTED.** Both compile clean under
  `lean -DautoImplicit=false -s 65536`, exit 0, zero errors. `DisjointBlockTraceLaw`
  emits four `unnecessarySimpa` linter warnings and nothing else.
- **The 0-byte truncation subclass — EXCLUDED here.** `find -name '*.olean' -size 0`
  returns **0** in the shadow and **0** across both real trees. (Partial truncation
  at nonzero length is NOT excluded — that needs reference sizes I did not have.)
- **Flag difference — EXCLUDED.** The sweep passes the same `LEAN_OPTS`
  (`-DautoImplicit=false`, `-s 65536`, line 71), so it is not the stack or
  auto-implicit.

### What remains — the shadow is the only difference left

lean-direct resolves imports against the **real** olean trees; the sweep resolves
them against its **hardlinked shadow**, from which it unlinks the dirty modules to
force a rebuild. Both segfaulters are `never built (new)` in the paper tree. So the
live candidate is that the shadow presents these two an import environment the real
trees do not — not tested here, and I am not asserting it.

### The consequence that matters, and it sharpens §1

§1 records that `skipped (dependency red)` says RED when it means UNVERIFIED, across
31 unrelated modules. **The sharper form: the sweep printed `0 RED` while never
compiling the module it was invoked for by name.**

    === library sweep: 4 ok, 0 RED, ... 6 skipped (dependency red) ===
    SKIPPED QOU.Mass.ProductionChainBondProduct  (red dependency: ...)

`--only-exact QOU.Mass.ProductionChainBondProduct` is a request to verify exactly one
module. That module was **skipped**, cascaded from the two segfaults, and the summary
line reads `0 RED`. An agent quoting that summary as its Phase-4 Lean gate reports a
green for a module the gate never looked at. That is a **false-green channel in the
documented gate**, not merely a mislabel.

Workaround used for #7281, and it is general: build the cone by hand into a
persistent `--shadow`, in dependency order, with lean-direct `-o`. All seven cone
modules exit 0, then the target compiles against them — exit 0, 0 errors, 0 warnings,
and `#print axioms` clean on all four theorems.

Not fixed here: both the label and the cascade are changes to the shared gate, which
is an owner call under the 2026-09-07 ASK-BEFORE-CHANGING directive.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
