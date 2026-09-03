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
