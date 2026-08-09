# Re-analysis: the self-assuming-projection campaign (issue #2472)

**Date:** 2026-08-09
**Supersedes:** [`2026-06-18-self-assuming-projection-triage.json`](2026-06-18-self-assuming-projection-triage.json)
(the 201-candidate queue that issue [#2472](https://github.com/litlfred/qou/issues/2472) batches over)
**Producer of the new pass:** [`scripts/lean-self-assuming-typematch-scan.mjs`](../../scripts/lean-self-assuming-typematch-scan.mjs)
**Machine-readable queue:** [`2026-08-09-self-assuming-projection-reanalysis.json`](2026-08-09-self-assuming-projection-reanalysis.json)

## Summary

Issue #2472's batch plan is built on a 2026-06-18 triage of **201** candidates
(199 degenerate + 2 legitimate) and defines completion as *"the scanner reports
`proof-no-self-assuming-projection: 0`"*. Seven weeks of Lean work later, both
halves of that framing need restating:

1. **The 201-candidate queue is effectively closed.** Exactly **1** of the
   original 201 is still reported as a non-exempt defect.
2. **The completion criterion is not valid.** The scanner's counter can reach
   `0` while genuine self-assuming projections remain, because
   `detectSelfAssuming` gates on the projected field's **name**. A
   name-independent pass over the same corpus finds **84 genuine
   self-assuming projections that the scanner does not report at all** —
   neither counted nor exempt.

Net: the campaign as scoped is done; the defect class it targets is not.

## 1. Where the original 201 went

Current scan: 2701 `.lean` files, 128 non-exempt defect candidates across 157
files (78 exempt). `proof-no-self-assuming-projection: 8`.

Matching the 2026-06-18 triage rows against the current scan by
`<path>::<decl>` (the triage stores lean-tree-relative paths such as
`QOU/Archimedean/…`; these normalise under `content/quantum-observable-universe/lean/`):

| status of the 201 | count |
|---|---:|
| still reported as a non-exempt defect | **1** |
| now reported **exempt** | 50 |
| no longer reported at all | 150 |

The single survivor is
[`hecke_baer_star_generic`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeBaerStarGeneric/hecke_baer_star_generic.lean)
(line 108, `degenerate(tuple-split)`).

**The 50 exemptions are deferral, not repair.** 47 fall under
`canonical §3b placeholder projection (tracked; derivation pending)`, a
carve-out the scanner introduced deliberately and documents in its own source
([`lean-vacuity-axiom-audit.ts:782-795`](../../content/pipeline/lean-vacuity-axiom-audit.ts)):

> Emit them EXEMPT (tracked-not-counted) so the coverage blindspot is closed
> WITHOUT turning the vacuity CI gate red on ~99 files. Promoting these to a
> hard failure — once the honest-placeholder vs. dishonest-dodge line is
> codified — is a deliberate follow-up, not a silent side effect of closing the
> blindspot.

That follow-up has not happened. The remaining 3 are the
`legitimate iff-from-directions conditional-class` precision-fix from #2462.

Of the 150 that dropped off, a coarse body-classification pass puts 63 on
**derive** (recipe-1 / §3b-cond restate), 16 on an honest `sorry` (the #2477
rubric's "queued-for-Lean" disposition), 8 with the declaration removed and 2
with the file deleted; the remaining 61 were not classifiable by that pass
(multi-line bodies its regex mis-slices) and are not asserted either way here.

What *is* checked for all 150 is the thing that matters: only **3** still
type-match their carrier's field, i.e. were never repaired and merely became
invisible — `knot_operator_selection`, `pair_skein_mass_formula`,
`cat_eigenspace_decomposition`. Their history shows no rename-to-dodge; each
was rewritten (file moves into the library tree) with the projection
reintroduced under a field name the gate does not cover. So the campaign's
repair work is real, and the leak below is a detector limitation rather than
evidence the drain was faked.

## 2. The name gate leaks — the completion criterion is invalid

`detectSelfAssuming` returns `undefined` unless the projected field name matches:

```ts
const CONCLUSION_FIELD =
  /^(exists_|claim_|is_|has_|selects_|are_|satisfies_|holds_|equals_)|(_holds|_eq|_iff|_property|_spec|_result)$|^(holds|property|spec|result|main|claim)$/;
```

A class field named outside that convention is invisible **no matter how
plainly it posits the conclusion**. The skill doc already records this
(`lean-proof-vacuity-audit.md` §8, the `confinement_ident` /
`factorization_ident` pair found by hand on 2026-08-08); what was missing was
the size of the population.

### Method

[`scripts/lean-self-assuming-typematch-scan.mjs`](../../scripts/lean-self-assuming-typematch-scan.mjs)
replaces the name gate with the structural test the skill doc names as the real
discriminator: **does the projected field's declared type match the theorem's
conclusion?** For every provable-kind declaration (plus Prop-valued `def`s;
`instance`s and data `def`s excluded) whose body is a bare projection of an
instance/structure binder field, it compares the carrier's field type against
the conclusion after stripping the binder prefix and collapsing whitespace.

The comparison is character-exact, so the pass is **conservative** — it
under-counts. Anything needing unification beyond whitespace is not reported.

### Result

| | count |
|---|---:|
| type-matched self-assuming projections | 134 |
| — caught by the name gate | 43 |
| — **leaked past the name gate** | **91** |
| of the leaked: already reported by the scanner under some exemption | 7 |
| of the leaked: **invisible to the scanner entirely** | **84** |
| — of those, in `lean/QOU/**` library files (no `.qa.json` sidecar) | 48 |
| — in content-block siblings | 36 |

The 48 library-tree cases have no sidecar, so — per AGENTS.md §"QA is
agent-owned; CI is a backup" — nothing but an agent ever checks them. They are
also invisible to the review ledger: `--check-ledger` currently exits **0**,
because the ledger only enforces agent review over what the detector finds.

### Verification

Six of the 84 were read in full by hand; all six are true positives. The
cleanest is [`mi-sw-abelianisation.lean`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation.lean):

```lean
structure MISWAbelianisation where
  mi_norm   : ℝ
  sw_period : ℝ
  abelianisation : mi_norm = sw_period      -- ← the CONCLUSION, as a field

theorem sw_determines_mi (data : MISWAbelianisation) :
    data.mi_norm = data.sw_period :=
  data.abelianisation                       -- ← P ⊢ P
```

The others: `mi_sw_nonneg` (same file, field `mi_nonneg`),
`qInt_ratio_bound_small` (`QHookBound.lean:406`, field `bound`),
`knot_operator_selection` (field `operator_selection`),
`pair_skein_mass_formula` (field `pair_skein_mass_ident` — the documented
`_ident` escape), `cat_eigenspace_decomposition` (field `decomposition`).

The detector discriminates correctly against the legitimate pattern sitting
right next to one of these: in
[`acoustic-horizon-conditions.lean`](../../content/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.lean),
`acoustic_horizon_regularity` projects two conclusion-fields and is reported,
while `acoustic_horizon_hawking_temperature` (`rw [ctx.hawking, ctx.hbar_brane]; field_simp`)
derives and is not.

Precision is **not** established at 84/84 — 6 were verified. The residual
requires the per-candidate agent inspection the skill mandates.

## 3. Consequences for issue #2472

- **The batch plan is obsolete.** Its 37 batches are keyed to the 2026-06-18
  triage's `tree` column; 150 of those rows no longer correspond to a defect.
- **"Done when the scanner reports 0" must be retired** as the completion
  test. On the current corpus the scanner reports 8; the honest count of
  type-matched self-assuming projections is 134, of which 84 are unreported.
- **The 47 deferred `§3b placeholder` exemptions are the campaign's real
  Phase 1 remainder**, and promoting them is an owner decision the scanner
  source explicitly reserves.

## 4. Recommended next steps (not taken here)

1. **Wire the type-match test into the scanner** as an additional pattern,
   emitting `EXEMPT` (tracked-not-counted) on first landing — the same
   blindspot-closing-without-reddening-CI move PR #3363 used for the
   def-disguised projections. This puts all 84 into the review ledger, which
   is what makes the agent-inspection gate bite.
2. **Then triage the 84** per the #2477 rubric (restate-to-derive /
   queued-for-Lean `sorry` / demote to conjecture), library-tree cases first
   since they have no sidecar coverage.
3. **Decide the 47 deferred exemptions** — the codification the scanner
   comment defers to.

Steps 1 and 3 change what CI reports and what the corpus claims, so both are
owner calls rather than drain work.
