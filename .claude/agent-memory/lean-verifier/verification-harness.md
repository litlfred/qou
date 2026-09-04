# Building a trustworthy `lean`-direct harness

Read on demand from `MEMORY.md` §TRAP — false greens and corrupt oleans.
Everything here was measured on 2026-08-30 (PR #6097) unless dated otherwise.

## 1. A green run against a stale dependency olean is a FALSE GREEN

`lean`-direct resolves imports from the **on-disk oleans**. Change module `M`,
check consumer `C`, and `C` is compiled against the olean `M` had *before* your
edit. It exits 0. This is the failure mode this agent exists to prevent, and it
reads as success.

Measured: `QOU/Hecke/WedderburnRankDegeneracy.lean` gave **exit 0** against the
tree and **exit 1, 2 errors** once `QOU.Hecke.Wedderburn` was rebuilt from
current source. It had been red on `main` for six days, through several
sessions that had every reason to look at it.

The companion mistake is on the search side: a blast-radius grep for consumers
taking `[Foo …]` as a **hypothesis binder** does not find a file that
*constructs an instance*. Compute the reverse-import cone from the import
graph instead of guessing at the syntax of a use.

**A second source of the same false green needs no edit of yours: the RESTORE
ITSELF is a snapshot** — see §11, which has the full case and the diagnostic
recipe. So §1's rule extends: rebuild from source not only what you changed, but
anything the cache predates.

**The cheap content-level test, which §11 does not give:**
`strings <olean> | grep -c <an identifier the new source introduces>`. A zero is
proof of staleness that needs no timestamp (§12 on why timestamps lie). Measured
2026-09-03 on `QOU/SchurWeyl/HeckeWedderburnGeneral.olean` out of
`lake-cache/qou-v4-24-0`: **zero** occurrences of `NotRootOfUnity` while its
source defines `heckeWedderburn` with exactly that hypothesis, so a consumer
built against it reported the *new* code's own hypotheses as unknown
identifiers. Independent of §11's `KazhdanLusztigClassicalLimit` case — two
agents, same day, same trap, different files, neither aware of the other.

## 2. A partial `LEAN_PATH` overlay shadows the WHOLE namespace

The obvious cheap harness — a small dir holding only the rebuilt oleans, first
on `LEAN_PATH` — **cannot work**. Lean's `SearchPath.findWithExt` picks the
first root that *contains a directory named `QOU`* and then resolves every
`QOU.*` module under that root unconditionally:

```lean
let root? ← sp.findM? fun p => (p / pkg).isDir <||> ((p / pkg).addExtension ext).pathExists
return root?.map (fun root => modToFilePath root mod ext)
```

One file in the overlay therefore makes every *other* `QOU` module report
`object file '/tmp/ovl/QOU/X.olean' … does not exist`. The mirror must be
complete.

## 3. The harness that does work

```bash
ROOT=/home/user/qou; LEANLIB="$ROOT/content/quantum-observable-universe/lean"
BASE="$LEANLIB/.lake/build/lib/lean"
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do BASE="$BASE:$d"; done
MIRROR=/tmp/qoumir
rm -rf "$MIRROR"; cp -al "$LEANLIB/.lake/build/lib/lean" "$MIRROR"   # hardlinks: ~0 disk
export LEAN_PATH="$MIRROR:$(echo "$BASE" | cut -d: -f2-)"
# then, in topological order over the reverse-import cone:
rm -f "$MIRROR/QOU/Path/To/Mod.olean"        # break the hardlink FIRST
lean -o "$MIRROR/QOU/Path/To/Mod.olean" "$LEANLIB/QOU/Path/To/Mod.lean"
```

`rm -f` before each write is load-bearing: without it a truncate-in-place write
would corrupt the **shared inode**, i.e. the real build tree.

Compute the cone with a small Python pass over `^\s*import\s+(QOU[A-Za-z0-9_.]*)`
across `QOU/**/*.lean`, invert it, take the transitive closure of the changed
module, and topologically sort. For `QOU.Hecke.Wedderburn` that is 8 modules and
about 90 s end to end — cheap enough that there is no excuse for the grep.

## 4. A disk-full `lake build` writes TRUNCATED oleans that segfault

Distinct from the eviction trap, and it masquerades as broken source. A
truncated olean mmaps fine and dies on a pointer chase. A **zero**-length one
gives a clean `failed to read file … invalid header` — so the clean error is
the *benign* case and the segfault is the ambiguous one.

**Signature: exit 139, ZERO errors, 0–1 seconds.** Real elaboration failures
take seconds and print errors.

Measured: after the session-start background build filled this container's
disk, a whole-library `lake build` reported 11 failing modules. **Ten were this
artifact.** `QOU/MathlibExt/OctonionSU3Stabilizer.olean` was **61,440 bytes**,
written inside the disk-full window, against **1,764,224 bytes** for its
healthy sibling `OctonionDerivationsBound.olean`. Only 1 of the 11 —
`QOU.Mass.QIntegerBarParity` — was a real defect.

Reporting "11 broken modules on main" was one step away and would have been
wrong. Triage: `df` first, then olean size against a sibling, then rebuild the
suspect from source. **Never conclude a module is broken from exit 139 alone.**

## 5. Disk is the binding constraint, and `df` lies about it

`df` shows 252 G nominal; the real limit is a per-session quota near 38 G. A
full `cp -r` of the QOU build tree is **2.1 G** — three of those plus a leaked
restore tarball took this container to 740 K free, at which point the Bash
harness cannot write its own output capture and every command fails. `cp -al`
makes the same mirror for ~0 bytes. Use it.

## 6. Triaging a cone failure: three ways it is the HARNESS, not the code

Measured 2026-08-30 on a 97-module cone with 8 failures, of which **exactly one**
was a real code defect. Work this order before calling anything broken.

**(a) "object file … does not exist" — a non-cone dependency with no olean.**
The harness rebuilds cone members only. If a cone member imports something
*outside* the cone whose olean was never built, it fails with `object file
'/tmp/mir/QOU/X.olean' … does not exist` — and the mirror faithfully reproduces
the gap because `cp -al` copied a tree that never had it. Measured:
`WenzlSchurElementBridge.olean` and `MolienFakeDegreeGeneralN.olean` are absent
from `.lake/build/lib/lean` entirely, taking three dependents down with them.
**Check `ls` on the named olean before diagnosing.** Absent ⇒ harness gap.

**(b) exit 139 with zero errors — but do NOT trust the size heuristic.**
§4 above says a truncated olean segfaults, and gives 61,440 bytes against a
1.7 MB sibling as the example. **That example is not a general test, and I
misapplied it.** On this run the three segfaulting modules had oleans of 57 KB,
226 KB and 50 KB against a tree range of 33 KB–6.7 MB — entirely normal sizes.
Size flagged nothing. The reliable discriminator is the *signature* (exit 139,
zero errors, ≤1 s: it dies before elaborating) plus (c).

**(c) The decisive test for all of them: re-run against MAIN's own oleans.**
Point `LEAN_PATH` at the committed build tree with no mirror and your branch's
changes off the path. Any file your diff does not touch that still fails there
is pre-existing, full stop. This is cheap, needs no worktree, and converts
"probably not mine" into a fact. All 8 failures reproduced this way.

## 7. A dead constant hides behind `abbrev` hops — grep the DEFINITION chain

`QOU/Mathlib/QHookProduct.lean` failed with `Unknown constant
QOU.Mass.QHookDimension.qIntPoly`. That string **does not occur in the file**.
The path is `unfold QOU.BraidKnot.qInt` → `abbrev … := QOU.QInteger.qIntGeo` →
`abbrev … := QOU.Mass.QHookDimension.qIntPoly` (deleted upstream). Three hops.

So after any rename or deletion, grepping *consumers* for the old name is not a
blast-radius check — an `abbrev` whose body names a missing constant elaborates
fine until something unfolds it. Resolve the chain, or rebuild the cone. This is
the same class as §1's instance-vs-binder miss: both are "the reference has a
shape my grep did not model".

## 8. TRAP — the FQN/name-surface guards: two ways they report a clean tree

Both scripts live in `scripts/` (`lean-duplicate-fqn-audit.py`,
`lean-name-surface-audit.py`, the second importing the first's parser).
Measured 2026-08-30 on PR #6278, by running them rather than reading them:

- **`--check-baseline` without `--verify` returns 0 having examined nothing.**
  The propose-only branch `return 0`s before the baseline block, so the ratchet
  prints an unverified candidate pair and exits clean. Same shape as the bare
  root `lake build` (0 jobs, exit 0). **Fixed** — both baseline modes now imply
  `--verify`, and a missing `LEAN_PATH` exits 2 rather than 0. If you ever see
  `--check-baseline` exit 0 with no "COMPILER-CONFIRMED" line, that fix has
  been reverted and the gate is not looking.
- **`private` was invisible to both.** Lean mangles a private declaration's
  environment name per module (`_private.<module>.0.<Ns>.<name>`), so two
  modules can both declare one and be imported together. The surface audit was
  putting such a pair in `L~L`, whose printed consequence reads *"hard import
  error once anything imports both"* — false of the code it described. Live
  instance: `QOU.BraidKnot.qIntBal`, private in `H3HeckeIdempotents`, public in
  `ZeqNRhoCorrection`, both delegating to `QOU.QInteger.qIntBalCl`. **Fixed** —
  the FQN audit skips private outright (sound: mangled names cannot collide);
  the surface audit excludes them from `L~L` only and PRINTS the exclusion
  count.

**Baselines after the fix** (re-measure, do not quote): FQN propose **0** pairs,
`--check-baseline` **0** confirmed collisions; surface audit `L~L` **0/0** with
**1** private pair reported as excluded, `L~S` 76/48, `S~S` 38/25.

## 9. Skeptic checks beyond the compile (measured 2026-09-03, `MuPCorrectionAdmissibility.lean`)

A green compile + std-3 axioms says nothing about the **prose** or about whether
a `Prop`-class is doing any work. Four checks, each under a minute:

- **Docstring numbers: find the probe's literal.** The file quoted
  `t = 2.09754920524e-7`, `+209.755 ppb`, `9.534 σ`, citing
  `docs/audits/scripts/mu_p_carrier_order_window_probe.py`. That probe hardcodes
  `R_exp = mpf("206.7682830")` — CODATA **2018** — while
  `tools/qou-substrate/python/qou_substrate/constants.py::MASS_RATIO_MU_E_STR` is
  `206.7682827` (CODATA 2022, owner ruling 2026-08-22) and
  `computations/mu-substrate-tension-audit-100dps.witness.json` reports 211.165
  ppb. Re-derived at 50 dps from the proton pin `1.1099785827513808`:
  t₂₀₁₈ = 2.0975e-7 (209.755 ppb, 9.53 σ), t₂₀₂₂ = 2.1121e-7 (211.2 ppb, 9.60 σ).
  The theorem's window `[1.8e-7, 2.4e-7]` held both, so the Lean was untouched
  and only the prose was stale on arrival — the "figure survives in five other
  places" pattern, one hop earlier. Also `t = 1 − R_exp/R_pred` (probe) and
  `(R_pred − R_exp)/R_exp` differ by t² ≈ 4e-14; do not "correct" one into the
  other.
- **Inhabitation `example` for any `structure … : Prop` sold as content-bearing.**
  Appended to the scratch copy:
  `example : C (fun _ => (2:ℝ)/10^7) ((11099:ℝ)/10000) := ⟨⟨le_refl _, by norm_num⟩, fun _ _ => rfl, ⟨by norm_num, by norm_num⟩⟩`
  — it compiled, so `GapA4CorrectionAdmissible` is inhabited by every constant
  in the residual window; "the class is not claimed non-empty" was true but
  misleading. The class is a filter and membership encodes no derivation. A
  `¬ C (monomial)` theorem stays genuine (drop `hc0` and `c = t/w³` is a
  member), but wording must not let a later reader cite membership as evidence.
- **`#print axioms` on a `structure … : Prop` over `ℝ` prints the std-3**
  (`ℝ`'s construction uses them). Not a laundering signal; `sorryAx` is the only
  axiom that matters.
- **Interval honesty by re-derivation, not by reading.** mpmath 50 dps: q₀ sits
  in `[1.1099, 1.11]` with margins 7.9e-5 / 2.1e-5; the window's true `w`-image
  is `[0.010882, 0.010901]`, inside the Lean's `[0.0108, 0.011]`;
  `(1/5)(0.0108)³ = 2.519e-7 > 2.4e-7` (5 % margin), `5(0.011)⁴ = 7.32e-8 <
  1.8e-7`. Both pins (proton `1.10997858275`, muon-anchored `1.10997859564`) lie
  in the window, so "at any pin in the window" covers both layers.

## 10. Mutation test, root-directory refusal, verified-bytes == HEAD (measured 2026-09-03, `GramQuotientDetD.lean`)

**A theorem closed by `simp only [<table>]; field_simp; ring` is "about the
table" iff the same tactic script FAILS when the table changes.** Reasoning
says so (`ring` decides commutative-ring identities); the measured version costs
about 40 s and is what a skeptic can cite:

1. Stand-in parent = the real parent's `import` lines + namespace + ONLY the
   declarations the child uses (`sed -n` the line ranges; nothing re-typed).
   A second copy with ONE entry changed (`| 1, 1 => (q^4 + 1) / …` →
   `(q^4 + 2)`; a diagonal entry keeps symmetry so `isSymm` still elaborates).
2. Two complete `cp -al` mirrors of the current mirror (~0 disk), `rm -f` the
   parent olean in each, `lean -o` the stand-in into it (~12 s each, warm).
3. Compile the PRISTINE child against each: control **EXIT 0**; mutant **EXIT 1**
   at the `ring` line, goal showing two different degree-20 polynomials. The
   control run is the harness's positive control — without it a mutant failure
   could be the stripping, not the mutation. Cheap sympy companion: perturb each
   leading-block entry by `+1` and confirm the determinant moves (25/25 here).

**`lean` v4.24 refuses a source outside its root:** `input file '…' must be
contained in root directory (/home/user/qou/)`. The root is the cwd (or
`--root=dir`) and the module name is derived from the path relative to it, so a
stand-in cannot be a loose file in the scratchpad: lay it out as
`<scratch-root>/QOU/Interactions/GramMatrixH3Symbolic.lean`, `cd` to the
scratch root with `ELAN_TOOLCHAIN=leanprover/lean4:v4.24.0` exported, pass the
relative path. (Builds from `$LEANLIB/QOU/…` with cwd `/home/user/qou` get an
odd derived module name; imports resolve by search PATH, so consumers do not
care — measured: the author's mirror built that way imports fine.)

**The branch tip can move while you verify.** HEAD advanced five commits during
one 20-minute pass (`4dbfd2ee31` → `1d9f1cf9db`) and the file went from `??` to
tracked. Finish with `git hash-object <file>` against `git ls-tree HEAD --
<file>` and the remote tip: the verdict is about a BLOB and transfers to a
commit only if the blobs match (`566da678…` matched HEAD, `origin/<branch>` and
the commit the bean named). `gh` is not installed and
`mcp__github__pull_request_read` was not offered in that session; git suffices.

**Statement audit — a headline can be a tautology while every Lean statement
is not.** "The form induced on `V/rad` is nondegenerate" is automatic for ANY
symmetric form (its radical is exactly what was quotiented out). The content of
`det(5×5 minor) ≠ 0 ∀ q ∈ ℝ` is `rank G = 5` — corank EXACTLY 1 for every real
`q` (it jumps at the complex roots of the numerator) — plus the closed form and
its sign. Say the content, not the tautology, and do not cite a membership lemma
(`gramMatrixD_mulVec_radical`) for one-dimensionality: that follows from THIS
theorem together with `det = 0`, not from membership.

**"Never positive" needs the pairing named.** `gramMatrixD` is the bilinear
`tr_M(ab)`; the star pairing `tr_M(ab*)` (`L₊ ↔ L₋` in one slot) has a
positive-definite quotient under D (`QOU/QBeta/GramSignature.lean` 2026-08-09
block; bean `qou-cds2` §"The named repair"). Same bean, same word "quotient",
opposite sign — the AGENTS.md claim-shape trap, one file over. The mpmath
signature of the 5×5 minor at q₀ is (4,1), matching `GramSignature` line 139.

**A witness's 30-digit value can carry 15 digits of input** (cousin of §9's
first item). The probe did `q0 = q_at(40)` then `sp.Float(str(q0), 40)`;
`str(mpf)` formats at the ambient `mp.dps = 15`, so the witness `q0Value` is
`1.10997858275138` and `det_at_q0` is 5.6e-17 off the 50-digit proton anchor
while printing 30 digits (float64-padding class). Check: evaluate the closed
form at `qou_substrate.constants.Q_50_DIGIT_STR` at 50 dps and diff; the
witness's own `q0Value` string length gives it away at a glance. Lean quotes no
digits, so it is untouched; route the probe to the compute lane.

**A `set_option maxHeartbeats N in` may be decorative.** Delete the line into a
scratch copy and recompile: this one passed at the default 200000 against a
declared 4000000. A nit, not a defect — but say so, or the next author copies it.


---

## 11. Stale import cone — the restore is a snapshot

The restore-first recipe above gives you oleans built at whatever commit the
cache branch was seeded from, **not** at your checkout. `lean`-direct resolves
every `import QOU.X` out of those oleans, so a file whose import cone changed
since the seed is checked against the *old* declarations — silently, with no
warning and no staleness signal anywhere in the output.

**Measured 2026-09-03.** `QOU/BraidKnot/KazhdanLusztigClassicalLimit.olean` is
dated **2026-07-02**; its source last changed **2026-08-25**, in commit
`3e3d3046d1` *"repair KazhdanLusztigClassicalLimit — the conjecture field
asserted nothing"* — the commit that ADDED the load-bearing `q = 1 →`
hypothesis. Against the restored olean:

    #check @KazhdanLusztigClassicalLimit.kl_compatible_with_tau
    -- ... (T : NormalForm) -> statSign (klMap T) = 1 or = -1      <-- NO `q = 1`

so a correct `... hq T` fails with *"argument `hq` has type `q = 1` but is
expected to have type `NormalForm q`"*. The error points at your call site and
says nothing about the cache. **I first "fixed" it by blaming dot notation and
wrote that wrong diagnosis into a source comment.** The code was right the whole
time.

**How to tell**, before you trust a green or debug a red:

    ls -l <olean>            # cache seed date
    git log -1 --format=%ad -- <source>.lean
    # source newer than olean => you are NOT checking against your checkout

**The fix — build the cone from current source into a scratch dir and PREPEND
it**, which shadows the stale oleans without disturbing the restore:

    FRESH=/tmp/freshlib; rm -rf "$FRESH"; mkdir -p "$FRESH"
    export LEAN_PATH="$FRESH:$LEAN_PATH"
    for m in QOU/Basic QOU/BraidKnot/HeckeAnyonicSubstrate \
             QOU/BraidKnot/CrystalGraphRealization \
             QOU/BraidKnot/KazhdanLusztigClassicalLimit; do
      mkdir -p "$FRESH/$(dirname $m)"
      lean "$SRC/$m.lean" -o "$FRESH/$m.olean"
    done

Four modules took well under a minute here. After that the same file was
**exit 0** with clean axioms. Do NOT reach for `lake build` — it evicts the
restore (TRAP above).

**Scope note, so this is not read as wider than it is.** A stale import cone
does not invalidate every restore-based verification: check whether the
declarations you actually used moved. Two other files I verified the same day
import `QOU/Archimedean/BorromeanVolumeCatalan` (source 2026-08-30, olean
2026-07-02) — one commit touched it in the window, and `git diff` showed **zero**
changes to any `vol_B3` / `catalan_G` line, so those greens stand. Measure the
specific declarations; do not assume either way.

---

## 12. A QOU-only `LEAN_PATH` mis-reports cross-package siblings as broken

Measured 2026-09-03, sweeping all 908 content-block sibling `.lean` files.

The standard env script builds `LEAN_PATH` from the **QOU** package plus the
root `.lake/packages/*`. That is right for a QOU library file and **wrong for
a content-block sibling**, because a sibling may import another paper's
library. `content/quantum-observable-universe/climax-volume-mass/vertex-algebra-relations.lean`
opens with `import UGB.…`, and the two environments disagree on the *same file
at the same commit*:

    QOU-only LEAN_PATH  ->  error: unknown module prefix 'UGB'
    all three packages  ->  exit 0, zero errors

**2 of 14 failures in the first 317 files were this.** Its shape is
indistinguishable from a real defect — a first-line error naming a module —
so it inflates any "broken siblings" count unless you triage before quoting.
Same family as §6(a): check whether the harness could have produced the error
before calling the code broken.

Fix — include every paper package:

```bash
for pkg in quantum-observable-universe unital-groebner-bases fred2005-formal-groups; do
  d="$R/content/$pkg/lean/.lake/build/lib/lean"
  [ -d "$d" ] && LP="${LP:+$LP:}$d"
done
```

The other packages are small (UGB 21 oleans, Fred2005 2), so this costs
nothing and removes a whole false-positive class.

**And the siblings are unchecked by anything else.** They live outside the
Lake globs (`globs = ["QOU", "QOU.+"]`, `srcDir = "."` = the `lean/` dir), so
`lake build QOU` never sees them; CI is `workflow_dispatch`-only. A sibling
can be broken for months with nothing reporting it — `n-v-bring-action.lean`
was (8 parse errors, `Σ` used as a binder name, which is `Sigma` notation).

---

## 13. No Mathlib source and no LSP: grep the OLEANS for renamed declarations

Measured 2026-09-03. This container's restore gives `.lake/packages/mathlib/`
containing **only** `.lake/build` — there is no `Mathlib/` source tree — and
the `lean-lsp` MCP server does not connect here. So the two obvious ways to
resolve a Mathlib rename are both unavailable, and the third is not obvious:

```bash
D=.lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Analysis/SpecialFunctions
grep -rhoa "tendsto_log_mul_rpow[A-Za-z_0-9']*" "$D" | sort -u
#   tendsto_log_mul_rpow_nhdsGT_zero
#   tendsto_log_mul_rpow_nhds_zero
```

**Olean binaries carry declaration names as plain strings.** `grep -a` with a
prefix of the name you remember, plus `[A-Za-z_0-9']*`, enumerates the live
spellings in seconds. `grep -rloa` gives the module, which is what you need
for the import.

**Two limits, both bitten in practice.**

1. **Namespaces are stored as separate components**, so the *qualified* name is
   NOT contiguous in the file — `grep -oa "Real.tendsto_log_mul_rpow[…]"`
   returns nothing even when the declaration is there. The grep finds the last
   component only; confirm the namespace with `#check`.
2. It found `tendsto_log_mul_rpow_nhdsGT_zero` in a module the file already
   imported, while the error said `Unknown constant
   Real.tendsto_log_mul_rpow_nhdsGT_zero`. **The defect was the namespace, not
   the name** — the lemma is in the ROOT namespace. `#check @<bare name>`
   settled it. Do not conclude "renamed" from an `Unknown constant` whose last
   component greps fine.

Same run: `tendsto_id` is `Filter.tendsto_id` and is not exported to root.

**Where this stops helping.** Names are cheap; proofs are not. On
`townsend-biot-savart-strain.lean` these two fixes took 9 errors to 7, and the
remaining seven are `Application type mismatch` / `rewrite failed` / `unsolved
goals` inside a real-analysis argument — proof-level drift, not name-level.
Budget accordingly: grep the names, then expect the proof body to still need
doing.

## 14. TRAP — do NOT key staleness on mtime; `git checkout` sets source mtimes

The obvious way to automate §1 ("rebuild anything whose source is newer than its
olean") is **wrong on a fresh clone**, and wrong in the expensive direction.
`git checkout` stamps every source file with the *checkout* time, not the time
its content last changed, so an mtime comparison flags files that never moved.

Measured 2026-09-03: an mtime pass over `QOU/**` reported "21 stale oleans".
Only **one** of those was verifiable as stale by content. Worse, the same
comparison applied to `.lake/packages/mathlib` marks *every* Mathlib source
stale, so an mtime-driven dependency walker recurses into the whole ~3000-module
Mathlib import graph and hangs. **Do not quote an mtime-derived stale count and
do not build a tool on one.** Use content (§1's `strings` test, and §11), or just rebuild
the cone — §3 puts `QOU.Hecke.Wedderburn`'s 8 modules at ~90 s.

Two further mistakes made while writing that tool, both worth not repeating:

- **Decide staleness AFTER recursing, never before.** A module's own olean can be
  newer than its own source while being *older* than a transitive dependency's,
  so an early return skips the stale grandchild and the build silently
  typechecks against old code — the very false green the tool existed to
  prevent. Caught only because the tool had a `--selftest` that made a
  transitive dep stale and asserted a rebuild; it failed on the first run.
- **Write into a `cp -al` mirror, not the real build tree.** §3 already says
  this; the reason it matters is that oleans written directly into
  `.lake/build/lib/lean` carry no `.trace`, so a later `lake build` treats them
  as stale and evicts the whole restore (MEMORY.md's `lake build` TRAP).

Provenance: this was re-derived from scratch during a session that never read
this file — §1 and §2 already state both traps, §2 already naming `QOU/` and
`SearchPath.findWithExt`. Reading the memory first would have cost a minute and
saved the re-derivation and the discarded tool. Only this section was actually new.

## 13. The union mirror — when MATHLIB itself is split across the two trees

§2 says a partial overlay shadows the whole namespace, and names `QOU/`. **The
same rule applies to `Mathlib/`, and that is the case you will actually hit**,
because the root and per-paper restores are two *different partial builds*.

Measured 2026-09-04 (`MagnusSumAbsEigBound.lean`): root `.lake` had
`Mathlib/Tactic.olean` and `Mathlib/Data/Real/Sqrt.olean` but **not**
`Mathlib/Algebra/Order/Chebyshev.olean`; the per-paper tree had Chebyshev but
**not** `Mathlib.Tactic`. Concatenating the two on `LEAN_PATH` does nothing —
the first root with a `Mathlib/` dir answers for every `Mathlib.*` module — so
`lean` reports `object file '…/Chebyshev.olean' … does not exist` naming a path
in the *root* tree while the file sits in the other one.

**Do not conclude the module is unavailable, and above all do not rewrite the
proof around it.** A sibling session did exactly that here: it replaced
`sq_sum_le_card_mul_sum_sq` (Chebyshev) with `sum_mul_sq_le_sq_mul_sq`
(`Mathlib.Algebra.Order.BigOperators.Ring.Finset`, which happens to live in the
root tree) and committed a source comment reading *"whose olean is absent from
the restored set"* plus a commit subject *"route around a missing olean"*
(`67128df5dd`). Both compile; the comment is false and now permanent. Same class
as §11's dot-notation misdiagnosis.

**The fix — a hardlink union of every package build dir from both trees:**

    MIR=<scratch>/unionlib; rm -rf "$MIR"; mkdir -p "$MIR"
    for d in $ROOT/.lake/packages/*/.lake/build/lib/lean $ROOT/.lake/build/lib/lean \
             $LEANLIB/.lake/packages/*/.lake/build/lib/lean $LEANLIB/.lake/build/lib/lean; do
      [ -d "$d" ] && cp -aln "$d/." "$MIR/"      # -n: first tree wins, never clobber
    done
    env LEAN_PATH="$MIR" lean <file>

`-a -l` = hardlinks: `du` reported 4.5 G while `df` free did not move. Read-only
use is safe; if you ever write oleans into it, `rm -f` first (§3) or you truncate
the shared inode. **Precondition: confirm both `lake-manifest.json`s pin the same
mathlib rev** (here `f897ebcf72cd`, toolchain v4.24.0 both sides) — mixing oleans
from two revisions is not sound. With the union both routes compiled exit 0.

**Cheap positive control, since a union mirror could in principle mask errors:**
append `example : (1:Nat) = 2 := rfl` to a copy and confirm exit 1. A harness
that returns 0 on everything is worse than no harness.

## 14. TRAP — a reverse-cone check on the files you just WROTE is nearly signal-free

§1 says to check the reverse-import cone. It does not say *of what*, and getting that
wrong produces a check that looks rigorous and measures nothing.

**Measured 2026-09-04, and the cost was 8 red modules on `main`.** A general-field
tranche retyped `seminormalRep`'s hypothesis `q ^ 2 ≠ 1 → GenericParameter.NotRootOfUnity q`
across nine modules (commit `e526464c2d`, PR #6486). Consumers *outside* the tranche were
never enumerated, and eight of them broke: `HoefsmitRepGeneral` (2 sites),
`SeminormalBlockTrace` (4), `SeminormalBlockEquality` (5), `SeminormalCornerTrace` (2),
`MarkovAssembly` (1), `MarkovTraceInstance` (4), then `WenzlMarkovLevelR` (2) and
`WenzlMarkovTraceInstance` (15) on a second pass. A sibling session found them with a
full-cone rebuild and fixed them (`794c34897d`, `cbf2202f43`).

**The follow-on PR (#6517) DID run a reverse-cone check and it came back nearly empty —
because three of its six files were BRAND NEW and so had zero importers.** "Exactly one
consumer outside what was rebuilt" was reported as reassuring. It was an artifact of the
files being new. The tranche with real consumers was the *earlier* one, and nothing was
ever run against it.

**The rule: run the reverse cone against every declaration whose SIGNATURE you changed,
not against the files you touched.** A new file has no consumers by construction; a
retyped hypothesis on an existing declaration has as many as the corpus has callers. Those
are opposite ends of the risk scale and the same command answers only one of them.

Two corollaries from the same incident:

- **"Off the general path" does NOT mean unaffected.** The tranche's own bean recorded
  `HoefsmitRepGeneral ← OFF the general path`; it is a consumer of `seminormalRep` and it
  broke. Off-path means *this* change does not need it, never that it does not need this.
- **A count of old-typed declarations is not a defect count.** Tree-wide, 13 files still
  declare `(hq2 : q ^ 2 ≠ 1)` and most are fine — they never pass `hq2` into the
  seminormal family. Only a rebuild distinguishes them.

Do not read the incident as an argument against §1's check. It is an argument for aiming
it: the same session's #6517 check was correctly *executed* and pointed at the wrong set.

