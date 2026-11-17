---
# qou-enn6
title: Convention-C weights survive in the reader-facing three-channel H_3 table (alt weight 0.02 vs 0 exactly)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T19:55:48Z
updated_at: 2026-10-10T07:47:07Z
parent: qou-cdx1
---

Found 2026-08-30 draining `qou-58zw`'s tolerance-floor audit. The producer
`computations/atom_mass_full_hecke_qdeformed.py` is fixed (`f61deb33bf`); the
**content blocks are not**, and one part of the fix is not available to me.

## What is wrong

The reader-facing block
[`observations/atom-mass-full-hecke.md`](https://github.com/litlfred/qou/blob/claude/convention-c-migration-tranche-1-2026-08-30/folio/quantum-observable-universe/observations/atom-mass-full-hecke.md)
states, in prose:

> At $q \approx 1.11$, $\hat y_{\mathrm{sym}} \approx 0.42$,
> $\hat y_{\mathrm{std}} \approx 0.56$, and $\hat y_{\mathrm{alt}} \approx 0.02$.

All three are **convention-C** values. Under the derived two-row cap the live
producer gives **0.5054 / 0.4946 / 0 exactly** — `y_lambda_at(3, Q)` routes to
`y_lambda_su_n(n, q, 2)`, the SU(2) specialisation, whose rank cap *is* the cap
(`FibreDimensionForcesTL.lean`, `qou-n1dj`).

Its "Key observations" §2 says the alternating block is **suppressed**. Under D
it is **absent**: identically zero, not small. That is an interpretive claim,
not just a number.

The sibling table block `atom-mass-full-hecke-table-data.md` carries the C-era
`tr_full` column **verbatim** — every entry matches the pre-fix witness exactly.
Measured shift, committed witness (C, 2026-06-22) vs the regenerated one (D):

| atom | tr_full C | tr_full D | rel |
|---|---|---|---|
| 4He | 0.516 | 0.577 | 11.7 % |
| 7Li | 0.294 | 0.397 | 35.0 % |
| 9Be | 0.343 | 0.371 | 8.0 % |
| 11B | 0.245 | 0.353 | 44.1 % |
| 12C | 0.533 | 0.615 | 15.4 % |
| 14N | 0.512 | 0.660 | 28.7 % |
| 16O | 0.677 | 0.766 | 13.1 % |
| 19F | 0.170 | 0.322 | **89.6 %** |
| 20Ne | 0.932 | 1.027 | 10.2 % |

## Why I did not update the blocks

The table's **`B/A_Skein`** and **`Δ (MeV)`** columns are derived from
`tr_full`, and I could find **no live producer** for them — every grep hit is
under `computations/_deprecated/`. So I can regenerate one of the table's three
number columns and not the other two. Updating `tr_full` alone would leave the
table internally inconsistent in a way that reads as correct, which is worse
than the present state where all three columns are consistently stale.

The prose weights and observation §2 *could* be fixed independently of that, and
are the cheaper half.

## Options

1. **Fix the prose only** (weights `0.42/0.56/0.02` → `0.5054/0.4946/0`, and §2
   "suppressed" → "absent, by the two-row cap"). Cheap, self-contained, no
   producer needed. Leaves the table stale but does not make it *more*
   inconsistent. **Recommended** — this is my judgement, not a finding.
2. **Also fix `tr_full`, and mark `B/A_Skein` / `Δ` as unrefreshed.** Honest but
   leaves a table whose columns come from two different conventions, flagged in
   prose. Cheap; risks a reader taking a row as coherent.
3. **Find or rebuild the `B/A_Skein` producer and regenerate the whole table.**
   Correct, and the only option that ends with a coherent table. Unknown cost —
   the formula's provenance is not in the live tree.
4. **Do nothing.** The default. The block keeps stating convention-C weights and
   a "suppressed" alt channel that is actually zero, in a reader-facing
   observations block. The producer is fixed either way, so the witness and the
   prose now disagree.

## Related but distinct

`qou-5ll9` hits the **same block** from the other input: `atomic-tr-m-helium4`
is 7.55 % stale pre-C→D, feeding the per-channel `|tr_M|` traces. That is the
*trace* leg; this is the *weights* leg. Both would have to land for the table to
be right, which is an argument for doing them together under option 3.


---

## RE-SCOPED 2026-08-30 — main fixed the prose half, and better than my option 1

Rebasing onto `origin/main` brought in a sibling's fix to
`observations/atom-mass-full-hecke.md`. It does more than correct the numbers:
it gives a **two-convention table** (D `0.5054 / 0.4946 / 0` beside C
`0.42 / 0.56 / 0.02`), states that the alternating weight is *exactly zero*
under the canonical convention rather than small, names a nonzero
`ŷ_alt` as **itself a convention-C signature**, and then closes the honesty
gap explicitly:

> The convention-C row is retained because the results tabulated below were
> computed in it and have not been recomputed under D. They are reported as
> measured, in the frame that produced them.

That is option 1 done better than I proposed it, plus the flag I could not
supply. **Options 1 and 2 are therefore gone**, and the priority drops from
high to normal: the block no longer *misstates* anything, it declares its own
frame.

## What is left, and it is now genuinely optional

The table's `tr_full` column is still convention C, correctly labelled as such.
**I have the D values** (regenerated in `f61deb33bf`, producer fixed and
re-run):

| atom | tr_full C (labelled) | tr_full D (measured) | rel |
|---|---|---|---|
| 4He | 0.516 | 0.577 | 11.7 % |
| 7Li | 0.294 | 0.397 | 35.0 % |
| 9Be | 0.343 | 0.371 | 8.0 % |
| 11B | 0.245 | 0.353 | 44.1 % |
| 12C | 0.533 | 0.615 | 15.4 % |
| 14N | 0.512 | 0.660 | 28.7 % |
| 16O | 0.677 | 0.766 | 13.1 % |
| 19F | 0.170 | 0.322 | **89.6 %** |
| 20Ne | 0.932 | 1.027 | 10.2 % |

Supplying them alone still leaves `B/A_Skein` and `Δ (MeV)` in C, and those
still have **no live producer** — every grep hit is under `_deprecated/`. So
the remaining choice is only between:

3. **Rebuild the `B/A_Skein` producer and regenerate the whole table.** The
   only option that ends with a coherent D table. Unknown cost; the formula's
   provenance is not in the live tree. `qou-5ll9` hits the same block from the
   trace leg (`atomic-tr-m-helium4` 7.55 % stale pre-C→D), so both would have
   to land together.
4. **Leave it.** Now the *reasonable* default rather than a silent defect: the
   block declares its frame, the D weights are on the page, and the D
   `tr_full` values are recorded here and in the regenerated witness for
   whoever does option 3.

**Recommendation (judgement, not finding): 4 for now, 3 bundled with
`qou-5ll9`** when someone takes the trace leg. Half-migrating a three-column
table is the one move worth avoiding.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Convention-C weights surviving in the READER-FACING three-channel H_3 table
(alt weight 0.02 vs 0.0x). The producer is fixed; the content blocks are not.
Live, and it is reader-facing, which ranks it above most of this list.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


---

## 2026-10-10 — the prose half was NOT fully fixed: §2 still asserted the word this block's own line 27 names as a convention-C signature. FIXED.

Re-audit of the C→D migration tracker (session epic `qou-am5t`). The
RE-SCOPED note above is right that a sibling's two-convention table is option 1
done better than I proposed it. **But it credits the sibling with the whole of
option 1, and option 1 had two halves.** The weights half landed; the
"suppressed" half did not.

### The self-contradiction, in one reader-facing block

`observations/atom-mass-full-hecke.md`, as it stood on `main`:

- **line 27** — *"Any statement that the alternating block is **suppressed**
  describes convention C; under convention D that channel does not contribute
  at all, and a nonzero $\hat y_{\mathrm{alt}}$ is itself a convention-C
  signature."*
- **line 48**, Key observations §2, twenty-one lines later — *"Under canonical
  $q$-deformed weights, the alternating block is **suppressed**."*

So the block named "suppressed" as a C-signature and then asserted it about the
canonical convention, in the same block, in prose a reader reads top to bottom.
This is what the RE-SCOPED note meant by *"an interpretive claim, not just a
number"* — and that claim was the one part the sibling's fix did not reach,
presumably because the fix was aimed at the weights table.

### What §2 now says, and why it is corpus-derived rather than my reading

The heading *"Alternating channel sign flips"* was describing something real —
`tr_alt` genuinely alternates in sign across the table (`+1.022, −1.460,
+1.692, −1.984, …`). The defect was conflating the **trace** with the
**contribution**. §2 now separates them: the trace alternates; its contribution
is zero, because

```
QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows
```

is sorry-free for general `n` over any field with `q² + 1 ≠ 0`, and the
alternating channel is the sign representation, whose partition `(1^n)` has
`n ≥ 3` rows. So `ŷ_alt = 0` **exactly** and `tr_alt` cannot reach `tr_full` at
all — "absent", not "small". The final sentence keeps the true part: the
apparent sign variation *in the total* was a classical-weighting artifact.

Independently corroborated inside the corpus, which is what makes this
exemption 2 rather than my judgement:
`braids-and-knots/jones-markov-trace.md:29` already states the same thing for a
reader — *"Under convention D that scalar **vanishes** precisely when
`ℓ(λ) ≥ 3`… The degeneracy is not a defect convention D introduced; it is what
convention D means"* — citing `TemperleyLiebTower.lean`, sorry-free. Two
reader-facing blocks now agree instead of one contradicting itself.

### Also fixed in passing: a real render-QA hit in the same block

The display-math block at `:11-16` had two lines beginning `+` inside `$$ … $$`
(two spaces of indent, which a markdown list parser still takes). That is a
named item in the AGENTS.md render-QA battery — the list-parser hijack.
Operators moved to end-of-line; **0 hits remain**.

One note for anyone re-running that battery: the naive Python guard
`line.strip()[:1] in '+-*'` returns **True for an empty line**, because
`'' in '+-*'` is `True`. That produced a phantom residual hit after the fix was
already correct, and it is the same class as every other row in the
detector-blindness taxonomy — the checker reporting about itself. Guard with
`s and s[0] in '+-*'`.

### Verification actually run (not "CI will catch it" — there is no CI)

Platform `folio-assistant` at the pin `717aa19a6`, cloned via
`scripts/setup-folio-assistant.sh`:

| check | result |
|---|---|
| `bun run scripts/run-validate.ts folio/quantum-observable-universe` | **✓ Valid — 9 issue(s)**, byte-identical to the 9 the pin's own notes record as expected. My edit adds none. |
| `qa-sweep … atom-mass-full-hecke.ts` (all **120** criteria) | **0 critical, 0 major, 0 minor**; 43 `needs-agent`, all pre-existing agent-judgement items |
| `qa-sweep … --only render-math-mode-envelope` | **0 findings** |
| grep battery by hand | `$` 76 (even), `$$` 2 (even), braces 57/57, `\bigl`/`\bigr` 0/0, `\begin`/`\end` 0/0, list-hijack **0** |

**What I did NOT do, and it is not an oversight.** `source_hashes.md` in
`atom-mass-full-hecke.qa.json` is now stale (`760156a395ce` → `277d3a409be7`)
and **qa-sweep did not re-stamp it** — it wrote nothing, and no `.qa.json`
anywhere in the tree is dirty after the sweep. The in-repo sidecars are frozen
at `updated_at: 2026-08-30`; the derived QA corpus moved to the cat-harness
`qa-reports` branch on an owner ruling of 2026-10-04 (`run-validate` says so in
its own `no-orphan-sidecar` warning, and `.folio-assistant-pin` records the
ruling). Hand-editing a frozen sidecar to make a hash match would be writing to
a surface the owner moved, so it waits.

Also noting `render-latex.ts` has **no CLI** at this pin — invoking it directly
exits 0 having run nothing. A silent `exit 0` from it is not a render check,
and I nearly recorded it as one.

### What remains, unchanged from the RE-SCOPED note

Option 3 only, and its blocker is confirmed **stronger** than recorded. The
bean says every `B/A_Skein` grep hit is under `_deprecated/`. Measured
2026-10-10: `grep -rln "B_over_A_Skein\|BA_Skein\|B/A_Skein\|ba_skein"
--include=*.py` returns **nothing at all** — not in `computations/`, not in
`_deprecated/`, nowhere. A looser case-insensitive `skein` grep returns only
Hecke/Skein-*relation* code and audit scripts, no `B/A` producer. So the
formula has no implementation in the tree under any of those names, and option
3's cost is genuinely unknown rather than merely unmeasured.

The `tr_full` D values are still recorded in the table above and in the
regenerated witness for whoever takes option 3 with `qou-5ll9`.

**Status: staying `todo`**, priority unchanged. The interpretive defect this
bean's first half was about is now closed; what is left is the three-column
table, which is `qou-5ll9`'s arc as much as this one's.

### Progress (Round 73 — PR litlfred/qou#8318)
- Formalized in PR `litlfred/qou#8318` (`feat/round73-symsquare-fibretl-mu3slot-sleak-deuteronz-43c1`, Commit 1 `d5360fac6f1464f5fd03c06ef76e726e30c785fd`, Head `e58aca150b7054a3222889e8bb9937602e515ca4`, `scriptHash: 19f0b8589c79`).
