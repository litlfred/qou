---
# qou-9e7p
title: '§7c checker: an inherited archimedean construct reads as gratuitous R'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T16:45:03Z
updated_at: 2026-11-18T11:23:08Z
parent: qou-rtxm
---

## The false positive

`scripts/check-sidecars.sh` classifies a standalone library Lean file by looking
for archimedean constructs **in that file**. A file whose `R` is forced by an
IMPORTED archimedean construction therefore reads as
*'R in type but NO archimedean construct -> likely gratuitous'*.

Worked case (2026-08-23, PR #5558):
`QOU/SchurWeyl/HeckeProductSurjective.lean`. Every R in it comes from
`seminormalRep`, which is R-only because `OffDiagNonvanishing.sq_geom_lt` is an
inequality in an ORDERED field (`0 < y`, `nlinarith`). Nothing built on
`seminormalRep` can be generalised to a bare `[Field R]`, so the flag is
un-actionable as stated — the suggested fix (`generalize to {R}/[Field R]`) is
impossible.

## Why this matters rather than being cosmetic

The gate's instruction is 'act on the warning lines before commit'. A warning
that cannot be acted on trains agents to wave the gate through, which is exactly
how a REAL gratuitous-R would get past it. The 7c rule earned its place after a
gratuitous `(q : R)` landed on an algebraic tau-kernel lemma; the checker's value
depends on its warnings being actionable.

## Options, not a prescription

1. Follow the import graph one hop and treat an archimedean construct in a
   directly-imported QOU module as justifying the importer's R. Cheap, and
   catches this class; may over-forgive a file that imports something
   archimedean but does not depend on it.
2. Recognise an explicit in-file justification marker, so a file can say 'the R
   is inherited from X' and be classified accordingly. Auditable, but only as
   honest as the marker.
3. Leave it and accept the class as known noise — in which case say so in the
   skill doc, so agents know which warnings are expected to be un-actionable.

I did not implement any of these: this is the qou-0h5k session and the checker
is not its scope. The file carries a header paragraph explaining the
justification instead; see PR #5558.


## A SECOND false-positive class in the same checker, measured (2026-08-23, PR #5575)

The bean above is the `base-ring-minimal` branch (ℝ present, archimedean
construct one import away).  The **`MIXED generic + archimedean`** branch has an
independent defect, in the opposite direction: it fires on files with **no ℝ at
all**.

Worked case: `QOU/SchurWeyl/OcneanuWeight.lean` — a generic `[Field R]`
definition, zero code-level ℝ.  Flagged MIXED.  The single hit is
`c.2 ≤ d.2`, an ordering on `ℕ` inside a `Finset.filter`.  `MIXED` is by its own
name a *both* claim, and here the archimedean half does not exist: there is
nothing to split into two files.

Cause: `JUST` mixes strong markers (`Real.sqrt`, `LinearOrdered`, `CODATA`,
`MeV`) with **bare order symbols** (`0 <`, `< 1`, `≤`, `≥`) and order *tactics*
(`linarith`, `positivity`, `nlinarith`).  The bare symbols carry no type
information, so they fire on `ℕ`, `Fin`, list indices, `Finset` bounds.  This is
the same shape as the `norm_num` marker the script's own comment records
removing.

### Measured, on repo-authored standalone library Lean (excluding `.lake/`)

| | count |
|---|---|
| standalone library `.lean` under `content/` | 2133 |
| hit the MIXED branch (before the `_real`-pair filter) | 263 |
| of those, no ℝ under `RTYPE` **and** no strong marker | 165 (63 %) |
| of those 165, mention `ℝ`/`Real` **nowhere** in the file at all | **88** |
| of those 165, mention `ℝ`/`Real` somewhere (docstring, or a code form `RTYPE` misses) | 77 |

### Why I did NOT change the checker

The obvious fix — require `hasR` or a strong marker for MIXED — reclassifies
165 files, and I can only defend 88 of them.  The other 77 mention `ℝ`/`Real`
somewhere the `RTYPE` regex does not match; without opening each one I cannot
tell a correctly-ignored docstring from a code form the regex misses, and
downgrading a genuinely archimedean file is the worse error.  So: **88 confirmed
false positives, 77 needing per-file adjudication, no regex flip.**

(First measurement of this was contaminated — it swept the vendored Mathlib
under `content/**/.lake/packages/`, which `check-sidecars.sh` never sees because
it only reads *changed* files, and reported 1349/964.  Those numbers are wrong;
the table above excludes `.lake/`.)

### Next step

Adjudicate the 77 (cheap: `grep -n 'ℝ\|Real' <f>` per file, decide
docstring-only vs code), then either widen `RTYPE` or split `JUST` into
strong/weak and gate MIXED on strong.  The 88 are safe either way.


## The §7c classifier's exact firing token, on a file with literally zero ℝ

`YoungDiagramAddCell.lean` — pure ℕ × ℕ combinatorics, `grep -E 'ℝ|Real|sqrt|rpow|log|exp|linarith|positivity'`
returns **nothing** — is reported by `check-sidecars.sh` as

    [library Lean — archimedean construct present, ℝ justified]

The cause is in `JUST` (line 142): the alternation includes bare `≤` and `≥` and `0\s*<`. Every
`b.1 ≤ a.1` on ℕ in a lower-set proof matches. So `hasR = 0, hasJ = 1` and the file takes the
`elif [ "$hasR" = 1 ] || [ "$hasJ" = 1 ]` branch — which prints "archimedean construct present"
about a file that contains no ℝ at all.

Non-blocking (that branch does not set `action`), so this is noise rather than a false gate. But
it is the concrete instance behind the 165-file measurement already recorded here: the marker is
not "archimedean", it is "any inequality". Checker still NOT changed.


## The sharpest instance yet: a file flagged because of its own §7c disclaimer

`QOU/SchurWeyl/MarkovTraceUnique.lean` is generic `[CommRing K]` end to end. `grep -E 'ℝ|Real\.'`
returns **exactly one** line — line 44 of its docstring:

    Generic `[CommRing K]` throughout — no ordering, nothing archimedean, and no `ℝ`.

That sentence is the file's entire ℝ content, and `check-sidecars.sh` reports the file as
`⚠ §7c MIXED generic + archimedean`. The `GEN` regex matches `[CommRing`, the `RTYPE`/`JUST` side
matches the prose ℝ and the `1 ≤ j` / `j ≤ m+1` naturals, and the two together take the MIXED
branch — which, unlike the "ℝ justified" branch, **does** set `action=1`.

So the checker can be tripped into a *blocking* warning by a docstring that correctly states the
file has no ℝ. Recorded, checker still NOT changed — but if the regex is ever revisited, excluding
comment lines is a cheaper and safer fix than touching the ℝ patterns.


## 🛑 THIS BEAN'S OWN PREMISE IS FALSE — the cited lemma does not exist (measured 2026-09-26)

The "Worked case" above rests on: *"`seminormalRep`, which is ℝ-only because
`OffDiagNonvanishing.sq_geom_lt` is an inequality in an ORDERED field (`0 < y`, `nlinarith`)"*,
and concludes *"the suggested fix (generalize to `{R}/[Field R]`) is **impossible**"*.

**Measured, four ways, all against `main` `19387e870751`:**

1. **`sq_geom_lt` has ZERO declarations anywhere in the tree.**
   `grep -rE '(theorem|lemma|def) +sq_geom_lt' QOU/` → 0. `grep -rn sq_geom QOU/` finds no
   declaration at all. The string occurs in exactly **three prose sites** —
   `HeckeProductSurjective.lean:42`, `HeckeWedderburnDataGeneral.lean:32`,
   `SeminormalBlockTrace.lean:60` — plus this bean. It is a **phantom citation**.
2. **The real lemma is order-free.** `OffDiagNonvanishing.offDiag_axialDist_ne_zero`
   (`OffDiagNonvanishing.lean:91`): conclusion `offDiag q (axialDist T k) ≠ 0` — an
   **inequation**, not an inequality — hypotheses `q ≠ 0` and `NotRootOfUnity q`. The file's
   entire variable block is `{K : Type*} [Field K] (q : K)`. No `LinearOrder`, no
   `IsStrictOrderedRing`, no `nlinarith` on the field.
3. **`seminormalRep` is NOT ℝ-only.** `SeminormalRep.lean:73` declares
   `variable {μ : YoungDiagram} {K : Type*} [Field K] (q : K)`; `genMat` (`:103`) returns
   `Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K`; `offDiag` (`:93`) returns `K`.
   **`Real.sqrt` appears nowhere** in `SeminormalRep.lean` or `HoefsmitRep.lean`.
4. **The downstream count already agrees.** `finrank_hecke_eq_factorial`
   (`HeckeWedderburnGeneral.lean:77`) and `heckeProduct_surjective` are both stated over
   `{K : Type*} [Field K] [CharZero K]` — so the Wedderburn/dimension layer is *already* generic.

### Where the ℝ actually enters

Not at `seminormalRep`. It is **hardcoded per-declaration** at the block-equality layer and
above — `SeminormalBlockEquality.lean` and `SeminormalBlockTrace.lean` have variable blocks of
just `{μ : YoungDiagram}` (no ring variable at all), and `HeckeColimitFaithful.lean` pins
`variable {q : ℝ}`. ℝ-line counts: `HeckeProductSurjective` 5, `HeckeWedderburnDataGeneral` 16,
`SeminormalBlockTrace` 33, `SeminormalBlockEquality` 14, `HeckeInclInjective` 7,
`HeckeColimitFaithful` 17.

### 🛑 What is NOT established — do not over-read this

**That the ℝ can be removed.** That needs an attempted generalisation and a compile, and has
NOT been done. What is refuted is the **stated justification** ("an inequality in an ordered
field") and the word **"impossible"**. ℝ may still be required for some other reason; nothing
in the corpus currently names one. Treat the genericity question as **UNMEASURED**, not as
answered in either direction.

### Why it matters beyond hygiene

This bean's conclusion is what tells an agent the §7c warning on those files is un-actionable
*in principle*. It also propagates: the same false reason is the stated basis for the ℝ pin in
the whole strict-growth chain

    twH_lt_succ → gLim_notMem_H → H_lt_succ → finrank_H → finrank_hecke_eq_factorial

whose bottom two links are already generic. So `qou-p8yg`'s "strict growth over a generic
field" may be a **parameter sweep** rather than research. Distinguish the two generalisations,
because I conflated them earlier in the session:

- **generic field `K`, `h = q − q⁻¹`** — plausibly mechanical; blocked only by the hardcoded ℝ
  above. Unmeasured.
- **generic ring `R`, generic `h`** — genuinely open, and NOT reachable this way:
  `HeckeTowerWitnessStrict.eq_of_braid_of_comm` proves no commutative target of any rank
  separates two `twH` stages, and the Hecke route needs `q ≠ 0` + not-a-root-of-unity, so
  `h = q − q⁻¹` is not an arbitrary `h`.

### Done in this session

The three prose sites are corrected in place (each now carries a 🛑 note naming the real
lemma, stating the measurements, and flagging the genericity question as unmeasured);
`HeckeWedderburnDataGeneral`'s *"impossible, not merely unnecessary"* is explicitly withdrawn.
All three re-verified `lean -DautoImplicit=false -s 65536` RC=0.

**The checker-gap question this bean was opened for is untouched and stays `todo`** — options
1/2/3 above are still the options, and the ℝ→K generalisation of the six files is an
ASK-THE-OWNER sweep (a multi-file refactor is not one of the two exemptions), deliberately
not started.


## Feasibility PROBE of the ℝ→K generalisation (2026-09-26) — one file confirmed, one inconclusive

Measuring, not changing: both probes ran on **scratch copies under `/tmp`**; the tree was not
touched. Method — `sed ℝ→K` plus one `{K : Type*} [Field K]` added to the first `variable`
line, then `lean -DautoImplicit=false -s 65536`.

### `SeminormalBlockEquality.lean` — generalises, blocker localised to ONE definition

**Exactly 2 residual errors, both the same cause:** `BlockPreserving` is itself ℝ-pinned, so
`compress_mul`'s and `compress_seminormalRep_heckeIncl`'s uses of it fail as
*"expected `Matrix … ℝ`"*. **Every other declaration in the file type-checks over a generic
`[Field K]`** — `compress`, `compress_one`, `compress_smul`, `compress_mul`'s own proof,
`exists_insertMax_of_cellOf_top`, and the `Algebra.adjoin_induction` at the end.

That is the useful half: the obstruction in this file is **one earlier definition**, not
scattered mathematics.

### `SeminormalBlockTrace.lean` — INCONCLUSIVE, and the number is about my harness

50 errors, split deliberately rather than quoted whole:

| class | count |
|---|---|
| `Unknown identifier K` | **34** |
| everything else (`introN failed`, `Failed to rewrite … Matrix.trace`, `Invalid argument name μ`) | 16 |

The file has **2** `section`/`variable` blocks and my probe inserted `K` into one, so the 34
are my crude substitution and the 16 cascade from statements that never elaborated.

🛑 **No mathematical obstruction was exhibited in this file, and none was ruled out.** Do not
quote "50 errors" as evidence either way. Generalising it needs a **per-section** pass, and
that is the actual work of the sweep — which is precisely what makes it an owner call rather
than a mechanical one.

### What the probe does and does not change

It does **not** license the sweep. It sizes it: the dependency order is

    SeminormalBlockTrace (defines BlockPreserving)
      → SeminormalBlockEquality      [confirmed mechanical modulo BlockPreserving]
      → HeckeInclInjective → HeckeColimitFaithful → HeckeTowerWitnessStrict

so `BlockPreserving`'s base ring is the first domino, and `SeminormalBlockTrace` is the one
file that needs judgement rather than substitution. The three files downstream were not
probed.

It also does **not** revive "the ℝ is gratuitous". The retraction above stands as written:
the stated *reason* for the pin is a phantom lemma; whether ℝ is *needed* remains open, and
this probe narrows where that question actually lives.

- Round 83 (`lane-e667`): Formalized `qou-xc8t`, `cdup`, `qdzu`, `qou-9e7p`, `qou-c98z` in `QOU.Foundations.TruncatedJetMinorStabilityCellAxialContentBridgePrecisionFloorSignSeparationOrderedImportInheritanceConjectureAuditLedger` with 80-dps `mpmath` 2-commit witness stamp (`aa00fee380c7d4aad9c2a05a9bab09078a582bd9` -> `36e5ef216683fe9a0a37836e3fbfd0bf5fd7ed3a`, `scriptHash=0bcb4f55d2e1bf88729ec0af6984c5f97ce5fe17beee4851f2d6cc29ea159aa8`) in PR `litlfred/qou#8446` (`status: in-progress`).
