# `qou-tsnp`'s queue is 5, not 12 — and five successive parsers got it wrong

**Date:** 2026-09-05
**Branch:** `claude/qou-tsnp-queue-remeasure-2026-09-05`
**Beans:** `qou-tsnp` (12 `holds : Prop` carriers), `qou-hprp` (23, live)
**Status:** re-measurement of an existing queue, plus a method trap.
**No carriers repaired here. No content written.**

---

## VERDICT

**Of `qou-tsnp`'s twelve carriers, six are already repaired, one is a mis-ref, and the
genuine content-repair queue is five. The re-measurement took five parsers, each of
which returned a plausible number and was wrong on a different Lean surface feature —
including one that would have sent me to "fix" the two carriers I had repaired an hour
earlier, which is precisely the failure `qou-hprp` had already recorded.**

---

## The queue, by direct reading

Established by reading each declaration, not by a matcher — see the trap below for why.

| carrier | state |
|---|---|
| `IsospinFromCanonicalBowtie` (D9) | **repaired** — #6671 |
| `SpinFromSo3Fiber` (D10) | **repaired** — #6683 |
| `PoincareLefschetzBorromean` | **repaired** — 3 fields, not by this session |
| `BorromeanBlochGroupElement` | **repaired** — `{B : Type*} [AddCommGroup B]`, parameterised |
| `LusztigCanonicalBasisQEq1` | **repaired** — `(R : Type u) [CommRing R] (q : R)` |
| `TFromTraceCyclicity` | **done differently** — stub deleted; the `.ts` ref `qou:QOU.BraidsAndKnots.TFromTraceCyclicity` matches the library carrier's namespace exactly |
| `WignerSu4FromSpinIsospin` (D11) | **mis-ref**, not a vacuity — #6711 |
| `DimMasterPentagon` | open — `holds : Prop` |
| `KashaevDensityEqualsSdpMultiplicity` | open — `holds : Prop` |
| `PFromBraidMirror` | open — `holds : Prop` |
| `TypeBFoldingCpt` | open — `holds : Prop` |
| `Mirror3d3dCorrespondence` | open — `holds : Prop` |

Each of the five open ones was confirmed to have **exactly one** `^class` declaration in
its file, whose sole field is `holds : Prop`. That check matters, because four of the six
"repaired" rows above have a *second* `class` line in the file that is not a declaration.

`TFromTraceCyclicity` is worth separating: the census already noted it as repaired, and
this confirms *how* — the stub was deleted and the ref points at the library carrier,
which is the disposition D11 has not had applied. So the queue already contains a worked
example of D11's outstanding decision.

## The trap: five parsers, five different Lean features

Each returned a number that looked reasonable. Each was caught by **reading the output**,
never by the count looking wrong.

| # | what it did | what it missed | measured effect |
|---|---|---|---|
| 1 | matched `class X … where` + indented lines | didn't find the file it was pointed at | reported **3** content-free carriers corpus-wide; true figure **17** |
| 2 | added a field extractor | read **docstring continuation lines** as fields (`'∈ R_{>1} implies substrate C*-Frobenius positivity (Müger /'`) | mis-split 20 / 18 into 13 / 25 |
| 3 | skipped field docstrings | didn't skip **module** docstrings `/-! … -/` | read a *quoted example of the old carrier* as a live class — reported D9 and D10 as unrepaired **one hour after repairing them** |
| 4 | stripped block comments | required `where` on the declaration line | called `BorromeanBlochGroupElement` and `LusztigCanonicalBasisQEq1` MISSING; both are repaired with **multi-line signatures** |
| 5 | — | — | replaced by direct reading, which is what the table above rests on |

**Parser 3 is the one that matters**, because the corpus had already predicted it.
`qou-hprp` records exactly this, in advance:

> A 39 % false-positive rate for the naive grep. The false positives are docstrings
> describing a stub that was *already replaced* … A grep that reads comments as code
> would have sent an agent to fix the one file in the chapter that is already correct.

That is verbatim what parser 3 did, to two files, in a session that had read that bean.
Recording it because a trap already written down and then walked into is worth more than
one discovered fresh.

## Practical rule

For a queue this size, **read the declarations**. Twelve carriers is roughly ten minutes
of reading and it is exact; five attempts at a matcher cost more than that and were still
wrong. A matcher earns its place at corpus scale — `scripts/free-prop-field-audit.py`
covers 105 carriers and no one is reading those by hand — but its output needs a control
that would fail loudly, and the control that would have caught parsers 1, 3 and 4 is the
same one each time: **a carrier known to be repaired must not come back as unrepaired.**

## Consequence

`qou-tsnp`'s title says twelve and its body's live count is eleven. Neither is the number
of carriers **needing the repair**, which is **five**. The bean is updated rather than
re-titled, since its census is what makes the re-measurement checkable.

## References

- `.beans/qou-tsnp…` — the census and its 18 → 16 → 12 count corrections.
- `.beans/qou-hprp…` — the 23-carrier live count, and the comment-as-code warning above.
- [`2026-08-23-free-prop-field-census.md`](2026-08-23-free-prop-field-census.md) — PR #5562, the corpus-wide census and its detector.
- **#6711** — the D11 finding. Its audit doc,
  `2026-09-05-d11-is-a-mis-ref-not-a-vacuous-carrier.md`, is on that PR's branch and is
  deliberately *not* linked by path here: it is not on `main` yet, and a path link would
  dangle until it merges.
- #6671 (D9), #6683 (D10) — the two repairs from this session.
