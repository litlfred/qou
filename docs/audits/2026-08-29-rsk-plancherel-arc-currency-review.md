# RSK / Plancherel arc — currency review against main (2026-08-29)

The arc landed 2026-08-23 as six PRs (#5538, #5549, #5553, #5554, #5556, #5561), ending at
`ee04275f4f`. Main has since advanced **3323 commits**. This is the re-verification: what still
holds, what a sibling has already superseded, and what was stale in my own records.

**Nothing here re-plans the forward work.** A sibling's
[`2026-08-28-M1-arc-revised-workplan.md`](../workplans/2026-08-28-M1-arc-revised-workplan.md)
already sequences it and reads this arc correctly, including the deflationary caveat that matters
(quoted in §3). This document only establishes currency.

## 1. The Lean survives — verified, not assumed

All four modules are present and **compile on current main**, axiom-clean:

| declaration | axioms |
|---|---|
| `ContentSqSumBridge.contentSqSum_ofRowLens` | `propext, Classical.choice, Quot.sound` |
| `PlancherelSnDataGeneral.plancherelSnDataGeneral` | `propext, Classical.choice, Quot.sound` |
| `PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general` | `propext, Classical.choice, Quot.sound` |
| `KeystoneDefectGeneral.defect_closedform_plancherel` | `propext, Classical.choice, Quot.sound` |
| `SecondMomentKernelVanishes.secondMomentKernel_eq_zero` | `propext, Classical.choice, Quot.sound` |
| `SecondMomentKernelVanishes.nuV_top_closed_form` | `propext, Classical.choice, Quot.sound` |

**A first pass at this was worthless and is worth recording.** Running `lean` against the restored
olean cache returns exit 0 for all four — but that cache is 6 days old and encodes the *old* main.
That is the same class of error as the off-pin platform clone this arc already got caught by
(`qou-a5p6`): a green check against stale inputs. The check only means something after establishing
what actually moved.

**What moved:** of the **132 QOU modules** in the arc's import cone, exactly **one** changed —
`BraidsAndKnots/YoungDiagramKernel.lean`, in `83c6c7db72` ("Resolve sorry gaps via class field
enrichment"). Its `covariance_kernel_conjecture` went from a bare `sorry` theorem to the §3b-cond
class form (`CovarianceKernelConjecture` + an instance-hypothesis theorem). It touches none of
`secondMomentKernel` / `omega3` / `contentSq` / `sytDim` / `partsOf`. Its olean was rebuilt and
`SecondMomentKernelVanishes` re-verified **against the rebuilt olean** — exit 0.

`SecondMomentKernelVanishes`'s scope note ("the kernel conjecture … remains open") is still accurate:
a class with no instance is open. The change is in the honest direction — it removes a bare `sorry`.

## 2. The keystone chain is intact

`rskBurnsideHolds` is still a sorry-free theorem in `SchenstedRSKBurnside`;
`SnIsotypicSpechtSplitInstance` still inhabits the split. The
[2026-08-25 OV audit](2026-08-25-ov-general-n-chain-is-closed.md) independently tabulates three of
these declarations as axiom-clean.

## 3. A sibling has already scoped it — correctly, and more narrowly than I would have

The M₁ workplan lists this arc under DONE and adds the caveat that matters:

> **First-moment / dim²-sum infra — it does NOT provide a Plancherel covariance, a free cumulant
> beyond `R₄ = 3ω₃ − k`, or any second-order object.**

That is right, and it is the correct deflation. `secondMomentKernel_eq_zero` is a *first-moment*
identity (`Σ_λ (f^λ)² ω₃ = 0`) despite the name; M₁ needs a genuine second-order Plancherel
covariance. The arc did not move the M₁ nub, and this document does not claim it did. Extending the
substrate to a covariance is that plan's **Track C**, explicitly lower priority than the analytic
sign in Track A.

## 4. My own records were stale — corrected

- **`qou-zjfs` sidecar measurement.** Re-measured on today's main: 3614 blocks, **330** top-level
  `source_hashes` stale, **23** criterion-level stale, **307** false positives. Was 3612 / 376 / 51 /
  325. The real drainable backlog fell 51 → 23; the **false-positive rate rose from 86 % to 93 %**, so
  the finding is stronger, not weaker.
- **`qou-a5p6`** said "not done here: bumping the pin". It was done — #5561, merged; main carries
  `428ca5c98c` and the `report_off_ref` guard is silent against it.
- **`qou-efzm`** named the wrong block. `mass-theory/q-clt-jsj-mass-scaling` **gained its `.ts`**
  in `6d4bb17ccc` ("restore two manifests the bulk import dropped") — fixed by a sibling, not by me.
  The surviving `.md`-without-`.ts` case is `lean/AUDIT-REPORT`, which I had dismissed at the time as
  a "stray non-block path"; it is the same orphan class. The four `*/section-title-audit` sidecars
  (neither sibling) are unchanged.
- **`qou-nrex`** was still `in-progress` with its target — general-`n` `RSKBurnsideHolds`, brick 42 —
  landed and sorry-free on main.

## 5. Net

The arc needs no repair. One dependency moved benignly, one of its follow-up items was closed by a
sibling, and the forward plan belongs to the M₁ workplan rather than here. The corrections above are
to my own bookkeeping, not to the mathematics.
