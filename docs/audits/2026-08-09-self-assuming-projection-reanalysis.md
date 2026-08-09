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

## 4. The test is now wired into the scanner

`detectSelfAssuming` no longer drops a projection at the name gate without
asking the structural question. Where the field name escapes
`CONCLUSION_FIELD`, the scanner now resolves the binder to its carrier,
looks up the projected field's declared type, and compares it to the
conclusion; on a match it emits

```
EXEMPT(type-matched projection (field name escapes CONCLUSION_FIELD; tracked, triage pending))
```

**EXEMPT on landing, deliberately** — mirroring the §3b placeholder carve-out
this document criticises above, and for the same stated reason: closing an
84-candidate blindspot must not turn the CI gate red in the same commit that
discovers it. The difference from that carve-out is that this one has a
draining plan (§5) rather than an open-ended deferral. Corpus effect:

| | before | after |
|---|---:|---:|
| non-exempt defects (the CI-relevant count) | 128 | **128** |
| exempt / tracked | 78 | **162** |
| files flagged | 157 | 217 |

Tracked-not-counted now enters the **review ledger**, so `--check-ledger`
demands a fresh agent verdict on each of the 84 — which is the whole point,
and is what the name gate was silently denying them.

**That required a second fix, and the first version of this section was wrong
about it.** Ledger seeding skipped every exempt hit (`if (h.exempt) continue`),
on the reasonable principle that an exemption *is* a verdict — a shadow stub, an
`@marker` opt-out, a legitimate iff-from-directions derive need no human call.
But an exemption reading *"tracked, triage pending"* asserts the opposite: that
the call is still owed. Under the blanket skip, emitting EXEMPT would have
**buried** the 84 rather than queued them — the exact failure mode this audit
exists to catch, reintroduced by the fix for it. Seeding now keeps exempt hits
whose reason matches `triage pending`. Ledger: 128 → 212 entries, of which 92
are self-assuming (8 non-exempt + the 84).

Consequence to expect: **`--check-ledger` now exits 1** until those verdicts are
written. That is the gate working, not a regression — but it is a real
transition from green, and it is why §5 is the immediate follow-on rather than a
someday item. The 47 deferred `§3b placeholder` exemptions are deliberately
*not* swept in by the `triage pending` predicate; whether they should be is §5
step 2's decision.

One parsing gap was found and fixed while wiring this. `DECL_START` requires a
name after the keyword, so an **anonymous `instance : C where`** — idiomatic
directly below the class it instantiates — starts no new declaration, and the
class's text swallows the instance body. `classFields` then reads each
`field := value` line as a re-declaration whose "type" is `= value`, so
last-wins lookup silently replaced the real field type. The type-match helper
therefore takes **first declaration wins** and drops `:=` assignment lines.
This affected 3 of the 84 (e.g. `beta3_via_class` in
[`Infra/Polylogarithm.lean`](../../content/quantum-observable-universe/lean/QOU/Infra/Polylogarithm.lean)).

**Residual:** the wired pass and the standalone script disagree on exactly one
candidate each way — the scanner additionally catches
`MathlibExt/SDP.lean::strong_duality`, and does not yet catch
`Encounter/MostowRigidity.lean::mass_eigenvalue_isolated` (field
`mostow_gap_pos : 0 < mostow_gap` against conclusion `0 < h.mostow_gap`; cause
not diagnosed). 84 tracked either way; the disagreement is noise-level and
recorded rather than papered over.

## 5. Triage — 69 of 92 adjudicated

The ledger's self-assuming queue is 92 (the 84 new + the 8 the name gate
already caught). Verdicts now written for **69**; **23 deliberately left
`needs-agent`.**

### The second discriminator: is the carrier ever inhabited?

Type-match alone is not enough to call a defect. A `structure`/`class`
bundling data with its defining properties, plus a `theorem` projecting one of
them, is the ordinary Mathlib accessor idiom (`IsCompact.foo`) — perfectly
legitimate, **provided something builds the bundle**. What turns it into the
audit's target is that nothing does: the declaration is then a restatement
presented as a result, quantified over a hypothesis nobody has exhibited.

| | count | verdict |
|---|---:|---|
| carrier never inhabited — `class` (§3b-cond) | 38 | **genuine** |
| carrier never inhabited — `structure` | 30 | **genuine** |
| carrier never inhabited — kind unresolved | 1 | **genuine** |
| carrier inhabited | 20 | `needs-agent` |
| carrier unresolved | 3 | `needs-agent` |

For the 38 uninhabited **classes**, uninhabited is *expected* — an open
conjecture's instance is the gap — so that is not the defect. The defect is
AGENTS.md §3b-cond item 5 directly: the class carries the **conclusion**
rather than the hypotheses, so the theorem derives nothing. Disposition:
restate so the class carries the genuine sub-hypotheses and the theorem
composes them (exemplar `q_bkm_criterion.lean`); demote to conjecture only
where no honest derivation exists — a claim change needing sign-off.

For the 30 uninhabited **structures**, disposition: construct a witness
instance and prove the property there, or drop the pseudo-theorem and project
the field at use sites.

### The inhabited 20, adjudicated: 3 legit, 9 genuine, 8 still open

Reading the instance bodies showed inhabitation splits three ways, and only
one kind carries content:

| instance shape | supplies content? | example |
|---|---|---|
| **`Fact`-wrapper** — `[hf : Fact P] … := ⟨hf.out⟩` | **no** | `branchingConverges_of_fact`, `nobleGasMultiOperator_of_fact` |
| **degenerate slice** — `…_refl … f f` | **no** | `convergenceBound_refl`; the bound reads `0 ≤ …` and closes by `positivity` |
| **trivial witness** — stipulates a constant, closes by `norm_num`/`rfl` | **no** | `term7ShellCorrectionInstance` (`alpha5_value = -1`), `zHabiroConvergenceInstance` (`fun _ => 1`) |
| **substantive** — real proofs covering the class's parameter domain | **yes** | `QIntRatioBoundSmall`'s four instances |

A `Fact`-wrapper is the sharpest of these: it relabels the assumption as an
instance, so whoever must discharge `Fact P` is exactly where the gap already
was. A `_refl` instance inhabits only the diagonal while the projected theorem
quantifies over arbitrary arguments, so the general claim is untouched.

**Legit (3):** `QIntRatioBoundSmall` and `QFactRatioBound` — four instances
each, discharging `m = 1,2,3,4` from `qInt_ratio_bound_m1..m4` with real
analytic work, and since the class binds `_hm4 : m ≤ 4` they **exhaust** its
domain; `GBResidueSpectralSum` — `fromCrystalData` is a general builder.

**Genuine (9):** `BranchingConverges`, `ConvergenceRate`,
`KnotInvariantConvergence` (Fact-wrapper + diagonal), `ConvergenceBound`,
`SkeinMultisetInvariant`, `ShellClosureMonotone` (diagonal only),
`NobleGasMultiOperator` (Fact-wrapper only), `Term7ShellCorrectionClass`,
`ZHabiroConvergenceClass` (trivial witness).

**Still open (11):** 8 whose instances look substantive under the automated
shape test but were **not read by hand**, plus 3 with an unresolved carrier. A
wrong `legit` closes the gate on a real defect while a wrong `genuine` only
makes work, so the unread ones stay open rather than being blessed by
heuristic. Each records what would close it: confirm the instances prove the
property across the class's parameter domain rather than at a convenient
slice.

Hand verdicts override the shape test in
[`scripts/lean-self-assuming-adjudicate.mjs`](../../scripts/lean-self-assuming-adjudicate.mjs),
because where the two disagreed the reading was right every time —
`ZHabiroConvergenceClass`'s constant witness reads as substantive to the test
only because `unfold brane_tower_pole` names an identifier.

**Ledger now: 78 genuine, 3 legit, 11 needs-agent** across the 92.

### Why the remaining ones are left open rather than blanket-blessed

Inhabitation is necessary but **not sufficient**, and the remaining call
differs case by case, so resolving it by rule would be the rubber stamp the
ledger exists to prevent:

- `QIntRatioBoundSmall` — **substantive.** Its four instances (`m = 1…4`) are
  genuinely proved from `qInt_ratio_bound_m1`. The content lives in the
  instances; `qInt_ratio_bound_small := hi.bound` is a real accessor. Legit.
- `Term7ShellCorrectionClass` — **placeholder.** Its single instance
  discharges `alpha5_derived` with a stipulated `alpha5_value = -1`, which its
  own docstring calls a placeholder ("sign witness only"). The projection
  inherits that emptiness. Genuine.

Each of the 23 carries its open question in the ledger `evidence` field.

Two counting corrections were made while doing this, both found by checking
rather than by assumption, and both in the dangerous direction at first:

1. A line-anchored inhabitation regex missed instances whose type sits on a
   continuation line, reporting 79 uninhabited (over-reporting defects).
2. Re-running it over whitespace-collapsed text then bridged from an
   `instance` keyword to a **binder** `(d : C R)` in a later declaration,
   reporting only 52 (under-reporting).

Neither regex was right. The final count parses declarations and reads the
conclusion at the first **top-level** colon — which by construction skips
binder colons — and asks whether a value-producing declaration's conclusion
head is the carrier. That is the 69/20 split above.

## 6. Remaining steps

1. **Fix the 69.** Not started — each needs its restate/demote decision
   applied and `lean`-direct verification. The ledger holds the disposition
   per candidate.
2. **Adjudicate the 23** inhabited candidates (substantive vs. placeholder
   instance).
3. **Decide the 47 deferred `§3b placeholder` exemptions** — the codification
   of the honest-placeholder vs. dishonest-dodge line that the scanner comment
   defers to.

Steps 1 and 3 change what the corpus claims where demotion is involved, so
those are owner calls.
