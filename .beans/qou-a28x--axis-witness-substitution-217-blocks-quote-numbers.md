---
# qou-a28x
title: 'AXIS: witness-substitution -- 217 blocks quote numbers no declared witness carries'
status: todo
type: task
priority: normal
created_at: 2026-08-10T03:43:44Z
updated_at: 2026-08-16T11:31:13Z
---


## What

New QA axis `content/pipeline/witness-substitution-audit.ts` (selftest 19/19).

A block declares `computation.witness: [...]`, then its prose quotes decimals.
**Nothing checked the second came from the first.** There is no substitution
mechanism in this corpus — no `{{witness:…}}`, no macro — so every quoted value
is a decimal somebody typed once, and the declaration is a citation, not a check.

That is how convention C survived in content after the producers moved:
`markov_trace_recursive.py` was migrated and re-run, its witness says the proton
trace is `1.884319467254976`, and the block still said `1.633154…` — the C value.
`trace-convention-audit` cannot catch it, because `1.633154` is not one of the
registry fingerprints and never could be: the registry lists `z` and the `y_λ`,
not every number computed downstream from them.

The fingerprint axis asks *"is this a known-bad number?"* — a list only as
complete as somebody's memory. This axis asks **"where did this number come
from?"**, which needs no list.

## First sweep

    2705 blocks scanned, 251 quoting high-precision literals, 217 failing

| detector | blocks | literals |
|---|---|---|
| `unsourced-literal` — matches no declared witness | 31 | 13325 → 3238 after the atlas fix |
| `no-witness-declared` — precise values, no `computation.witness` | 186 | — |
| `externally-attributed` — CODATA / knot table / citation (reported, not failing) | 11 | 19 |

## Already fixed here

`rem:recursive-atom-knot-atlas-registry` declared one unrelated witness while its
per-element table is, in its own words, *"auto-rendered from per-Z shards
`canonical-isotope-witness-Z<NN>.witness.json`"*. Under-declaration, not
unsourced data — the numbers had a producer, the block never named it. Declaring
the 119 shards took it from 13250 → 3163.

## Next

1. The 186 `no-witness-declared` blocks — triage: which have a producer that was
   never declared (cheap, like the atlas) vs which quote numbers with no producer
   at all (the real finding).
2. The 3163 residual atlas literals — AME reference columns and derived B/A
   ratios; decide whether the shards should carry them.
3. `prop:markov-trace-recursive-reducer` declares TWO witnesses that disagree by
   17% — one migrated to D, one still C. Suggests a `witness-disagreement`
   detector.
4. Sidecar upsert. Deliberately not written yet: the first sweep touches a large
   fraction of the corpus and would bury the tuning diff in generated JSON.

---

## Re-measured on main, and triaged (2026-08-15)

    2721 blocks scanned, 254 quoting high-precision literals, 221 failing
      unsourced-literal      31 blocks, 3242 literals
      no-witness-declared   190 blocks
      externally-attributed  12 blocks, 22 literals

The `unsourced-literal` count fell 13325 -> 3242 because the atlas
under-declaration fix landed with #4899; the residual 3163 there are AME
reference columns and derived B/A ratios.

### The 190 undeclared blocks are three different jobs

New `--suggest` mode. It indexes every decimal token in every witness
(2930 files, ~215k distinct 8-dp tokens) and greedily covers each block's
literals, so the pile separates mechanically instead of by survey:

| | | |
|---|---|---|
| **78** | fully coverable | a declaration away from traceable |
| **45** | partial | some literals witnessed, some not |
| **53** | **orphan** | literals appear in **no witness anywhere** |

The orphans are the real finding. `prf:spectral-decomposition-qvalue`,
`rem:F3-eps6-leading-eq-neg-2b-cubed`, `rem:q-beta-gamma-gamma-canonical-derivation`
quote precise values that no producer in the repo emits.

**The output is a proposal, not an edit,** and the code says so: a witness that
happens to contain a matching decimal is not necessarily the witness the block
means — `0.612688037146` is `z` at the proton pin and appears in dozens of
unrelated files. Coverage narrows candidates for a human; it does not decide.

### A worked example, and why it is not a simple fix

`prf:categorical-mass-markov` has 9/9 literals witnessed somewhere and declares
nothing. But its numbers are a **correctly labelled C-vs-D comparison table**
(headers "convention C (was)" / "convention D (now)", inside a marked
2026-08-09 convention-change note) — not a defect on the convention axis.

And the reproducer it names in prose, `computations/markov/markov_trace_canonical.py`,
**emits no witness at all** — no `WitnessBuilder`. So the block cannot declare
the thing it cites; its values happen to live in `alpha-k-jones-markov-h3`,
`gram-matrix-dual` and others. "Under-declared" and "declarable" are not the
same thing.

## Next

1. The 53 orphans, individually — each is a number with no producer.
2. The 78 coverable, from `--suggest` output, human-checked rather than applied
   in bulk.
3. `markov_trace_canonical.py` emits no witness while being cited as a
   reproducer. Worth a bean of its own.

---

## The orphan list had a false-positive class: identifiers

Working the 53 orphans turned up `prf:confinement-phase-stratification` with
"one literal in NO witness: **10.1017**". That is not a measurement — it is the
Cambridge University Press **DOI prefix**, from

    [Boyd-Vandenberghe](https://doi.org/10.1017/CBO9780511804441)

The scope regex ends a literal at any non-`[\w.]` character, and `/` qualifies,
so `10.1017` matched and no witness will ever contain it. Same shape for arXiv
ids (`arXiv:2601.05136`) and bare `doi:` references.

Fixed narrowly — a decimal butted directly against `/`, or immediately preceded
by `arXiv:`/`doi:`, is an identifier rather than a quantity. Checked against the
surrounding text, not the literal, because the literal itself is
indistinguishable from a real number.

**221 -> 214 failing; `no-witness-declared` 190 -> 183.** Seven blocks were
failing purely on citation identifiers.

One fixture pins the thing that would make this too broad: *a real value on a
line that ALSO carries a DOI stays in scope*. The exclusion is per-literal, not
per-line — a citation on the line is not licence to stop checking the numbers
beside it. Selftest 19 -> 23.

### What the remaining orphans look like

Now that identifiers are gone, the residue sorts into recognisable kinds:

* **external constants** — `137.0359351` (1/alpha) in `prop:meson-em-sinh-closed-form`,
  `7.32772` in `rem:gas-constant-derivation`. Real values, external sources, but
  the line never names one, so `externally-attributed` cannot see them.
* **derived-by-hand** — `0.1134` in `prf:hecke-satisfies-blitvic-hypothesis` is
  `|z_D - z_C|`, arithmetic on two witnessed values that no witness stores.
* **genuinely unsourced** — the rest.

Those are three different fixes (name the source / declare the arithmetic /
find a producer), so the next pass should split them before touching any.

---

## CORRECTION: the orphan count was wrong by a factor of 18

I reported **53 orphans**. The real number is **3**. Two bugs in `--suggest`,
both of the same kind — the triage tool was weaker than the detector it
triages for.

### Bug 1: key lengths did not match

The index bucketed witness tokens on **8** fraction digits; a literal was keyed
on **its own** length. So `137.0359351` (7 decimals) could never match a
witness token indexed as `137.03593513`, and *every literal with fewer than 8
decimals was reported ORPHAN regardless of what the corpus contained*. That is
most of them, which is why the first orphan list was full of four-decimal
values like `0.5904`, `1.1073`, `0.1134`.

Fixed by bucketing on `MIN_DECIMALS` and confirming with a full prefix check.
**53 -> 7.**

### Bug 2: no numeric fallback

`isSourced` — the real detector — matches by prefix **or** numerically to
within half a unit in the literal's last place, because prose sometimes rounds
instead of truncating. `--suggest` only did prefix. So `1.1099786` in
`prop:alpha-em-categorical-trace-ratio`, which is q0 rounded to eight
significant figures, was reported as a value no producer emits.

**7 -> 3.**

### How it was caught

Not by the selftest — by pulling on `137.0359351` and finding the block says
*"the framework's own **derived** value … No measured constant is imported"*.
That contradicted my own triage note, which had filed it under "external
constants whose line never names a source". Checking the contradiction instead
of widening `EXTERNAL_SOURCE_LINE` is what exposed the indexing bug — widening
the regex would have *suppressed* a real finding and left the bug in place.

### The three real orphans

| block | literals |
|---|---|
| `rem:binding-alpha-shift-extension-context` | `14.6673` |
| `prop:habiro-residue-sum-equivalence` | `2.1225825095`, `1.5893934460`, `0.1774369242` |
| `rem:pair-creation-energy` | `0.9010` |

The Habiro one is the substantive case: three ten-decimal values, which is a
precision claim, with no producer emitting any of them.

### Current triage

    151 fully coverable by declaration
     20 partial
      3 orphan

## Next

- The three orphans, individually.
- The 151 coverable are a mechanical pass, but `prf:categorical-mass-markov`
  showed why they cannot be applied in bulk: it was "fully coverable" and the
  right fix was still a new witness plus a `literal-source` marker, because the
  reproducer it cited emitted nothing and half its numbers were preserved
  convention C.

---

## The three orphans, worked

### 1. `rem:pair-creation-energy` — FIXED, a misrounded constant

The block wrote `E_cross(e+) = -3q^{-1} ≈ -3 × 0.9010 = -2.703`.

`q_0^{-1} = 0.90091828395574149216`, which rounds to **0.9009**, not `0.9010`.
Both documented pins agree (`muon: 0.90091827356…`), so this is not a pin
question — it is a misrounded intermediate. The downstream `-2.703` is fine
either way (`3 × 0.90091828 = 2.70275`), so only the quoted intermediate was
wrong, which is why nothing downstream ever contradicted it.

Corrected to `0.9009`.

### 2. `prop:habiro-residue-sum-equivalence` — beaned, not fixable here

Split out as **`qou-uabo`**. Its three values come from a **deprecated**
producer; the "cross-pipeline witness" the prose cites does not exist; and the
nearest live value is **95x outside the block's own 1e-9 tolerance**. A
proposition whose whole content is "these two paths agree to machine epsilon"
cannot be checked while the run that produced it is gone. Deliberately did not
attach a plausible-looking witness.

### 3. `rem:binding-alpha-shift-extension-context` — `14.6673` MeV/rad, no source

`14.6673` appears in **no witness and no producer**, live or deprecated. It is
used twice in the block, as a conversion factor
(`rho_full(D) = 14.6673 MeV/rad`, then "re-multiplied by the 14.6673 MeV/rad").

Unlike the Habiro case there is no deprecated producer to point at, and unlike
the pair-creation case there is no constant it is a rounding of. It is simply a
number with no provenance in the repo. Left as-is and recorded: inventing a
source would be worse than the flag.

## Orphans: 3 -> 2

One fixed, one escalated to its own bean, one recorded as genuinely
provenance-free.

---

## Name correspondence: 152 "coverable" is really 1 confident + 151 to judge

Working the coverable pile showed coverage alone proposes nonsense. Single-
literal blocks match almost anything — one shared decimal is the whole test:

    rem:collatz-hausdorff-comparison  <- meson-mass-from-hecke.witness.json
    conj:diophantine-birthday         <- meson-mass-from-hecke.witness.json

Neither has anything to do with meson mass. That is exactly the false
attribution `--suggest`'s own docstring warns about, arriving in its own output.

The one signal that is not arithmetic is **name correspondence**: when
`prop:meson-em-sinh-closed-form` is covered by
`meson-em-sinh-closed-form.witness.json`, the witness is *named after the
block*. `--suggest` now marks those **CONFIDENT** and prints
`[named after the block]` on the line.

    152 fully coverable (1 CONFIDENT — witness named after the block), 20 partial, 2 orphan

**1 of 152.** That is the honest reading of the pile: 151 are suggestions a
human must judge, and exactly one is provenance. Reporting "152 coverable"
without that split invited precisely the bulk-apply this axis exists to prevent.

### The confident one, declared

`prop:meson-em-sinh-closed-form`. Three independent confirmations, not just
the decimal:

* the witness is named after the block;
* the witness's own `computation` field is `meson-em-sinh-closed-form`, the
  block's slug;
* the producer `computations/meson_em_sinh_closed_form.py` exists.

Its `alpha_em^-1 ~ 137.0359351` is the witness's `137.03593508992864` rounded —
and the block states this is the framework's **derived** value, *"No measured
constant is imported"*, so it is exactly the sort of number that must be
traceable to a producer rather than waved at CODATA. That was the literal whose
investigation exposed the key-length bug.

Block: 1 unsourced-literal -> 0. `run-validate` still `✓ Valid`.

## Next

The 151 non-confident coverable blocks need per-block judgement, and the tool
now says so rather than implying a mechanical pass. A reasonable next cut:
extend name correspondence to the block's `script` slug and to directory
proximity, which would likely promote more than one — but each promotion has to
be justifiable the way this one was, on three signals rather than a shared
decimal.


---

## 2026-08-16 — "151 fully coverable" was not a work queue. The real queue is 13.

`--suggest` reported **151 fully coverable / 0 CONFIDENT**, which reads as 151
blocks waiting to be declared. It is not. Coverage alone is nearly worthless on
a single-literal block: *any* witness containing that decimal "covers" it.

Measured on `def:jet-stratified-reduction`, which quotes one literal, `1.1097`:
**29 witnesses carry it** under the axis's own matching rule. The greedy cover
picked `higgs-h6-correction-probe.witness.json` — a Higgs probe, for a
Gröbner-basis jet-reduction block — and printed it as though it were the source.

**Declaring that would attach false provenance, and this axis could never
afterwards detect it**, because the axis only asks whether the declared witness
*contains* the number. A wrong declaration passes forever. That is the same
shape as every other trap in this campaign: a check satisfiable by something
other than the truth.

### The fix: report ambiguity, which was computed and thrown away

`cover` already held each literal's candidate set; only its *size* was unused.
`--suggest` now buckets:

```
151 fully coverable by declaration — but coverable is NOT a work queue:
    0 CONFIDENT  witness is named after the block (provenance, not arithmetic)
   13 UNIQUE     every literal has exactly ONE candidate witness
  138 AMBIGUOUS  some literal occurs in several witnesses; the cover picks one arbitrarily
```

**The actionable set is 13, not 151** — an 11.6x correction, and the same
magnitude of error as the earlier "53 orphans -> 3".

### UNIQUE is necessary, not sufficient — do not batch-declare the 13 either

Uniqueness says the number is rare in the corpus, not that the block took it
from there. Two blocks can independently quote the same rare constant. Of the 13:

- **Coherent, worth declaring after a read:** four Q-value blocks
  (`ex:qvalue-benchmark-table`, `rem:qvalue-derivation-chain`,
  `rem:qvalue-observation`, `prf:spectral-decomposition-qvalue`) all resolve to
  `sublemma-2-1-A-operator-extract-h9-pn.witness.json`; two Hausdorff blocks to
  `A-operator-extract-h9-pp.witness.json`; `prf:crystal-isospin-degeneracy` to
  `term7-alpha5-crystal-derivation.witness.json`; `rem:F3-eps6-leading-eq-neg-2b-cubed`
  to `qbeta-ck-sseries-exact-rational.witness.json`.
- **UNIQUE but subject-matter implausible — do NOT declare:**
  `rem:q-beta-gamma-gamma-canonical-derivation` resolves to
  `chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json`. Unique, and unrelated.
  Also weak: `conj:n-v-bring-action` -> `binding-reeb-phase-decomposition`,
  `rem:groebner-nf-computation` -> `joint-tower-sdp-rust`.

So the remaining check is **subject-matter coherence**, which is judgement, not
arithmetic — roughly 10 of 13 look declarable, and that is the honest queue.

### Verification

`coverageTag()` extracted as a pure function so the distinction is testable
rather than buried in the `--suggest` branch. Selftest **23 -> 29**; the six new
cases pin that a named witness stays CONFIDENT even when the literal is common,
that one candidate is UNIQUE and 29 is AMBIGUOUS, and that a single ambiguous
literal poisons an otherwise-unique block. Main axis unchanged at 213 failing —
this is triage only.


### CORRECTION to the note above — the queue is 2, not 13, and "~10 of 13 coherent" was wrong

I wrote above that "roughly 10 of 13 look declarable" on the strength of
topic-name proximity. **Checking the semantics killed the best-looking cluster.**

The four Q-value blocks — `ex:qvalue-benchmark-table`,
`rem:qvalue-derivation-chain`, `rem:qvalue-observation`,
`prf:spectral-decomposition-qvalue` — were UNIQUE against
`sublemma-2-1-A-operator-extract-h9-pn.witness.json` on the literal `0.5904`.
The block states that value is *"the Rosso–Jones weighted average over the two
degree-2 torus knots τ(2,9) and τ(3,4)"*. The witness carries
`0.5904453769109197` as `A_per_pair.((5,1),(1,1,1)).frobenius_norm`. **Unrelated
quantities agreeing to four decimals, with exactly one candidate in the corpus.**
Uniqueness proposed a false source for four blocks at once.

**The discriminator uniqueness was standing in for is MATCHED PRECISION.** Four
decimals coincide; nineteen do not. Added `STRONG_MATCH_DECIMALS = 10` and a
`WEAK` bucket:

```
    0 CONFIDENT  witness named after the block
    2 UNIQUE     one candidate AND >=10 matched decimals
   11 WEAK       one candidate, but too few decimals to be evidence
  138 AMBIGUOUS  literal occurs in several witnesses; cover picks one arbitrarily
```

**151 -> 13 -> 2.** The original headline overstated the actionable work by 75x.

### One declaration landed, and it is proof rather than coincidence

`prf:crystal-isospin-degeneracy` now declares
`computations/term7-alpha5-crystal-derivation.witness.json`. Its literal
`0.0020612874779541296` sits at **both** `data.atoms[1].S_crystal_at_q_zero` and
`data.atoms[2].S_crystal_at_q_zero` — atoms[1] is ³He, atoms[2] is T, the
isospin mirror pair. Their sharing it to 19 digits **is the degeneracy the block
proves**, so the witness contains the claim, not merely the number. Producer
`computations/term7_alpha5_crystal_derivation.py` exists.

Corpus: 213 -> 212 failing, `no-witness-declared` 182 -> 181.

The second UNIQUE (`rem:q-beta-gamma-gamma-canonical-derivation` ->
`chi-helium-4-h12-at-q0-50dps-matrix-m`, 10dp, exactly at threshold) is **not
declared**: a q-beta γγ derivation sourced to a helium-4 χ matrix is not
coherent on its face, and I could not locate the matching field to confirm
either way. Left for a human read.

### A false-positive class found by walking into it

My first declaration *raised* a finding: the explanatory comment I wrote in the
`.ts` quoted `0.5904`, and **this axis scans `.ts` comments**, so the file
flagged itself. Reworded to avoid the numeral rather than change the axis —
a comment is not published prose, so arguably it should be out of scope like
fenced code blocks, but that is a scope decision for the axis owner and
silencing it to make my own edit pass is exactly the wrong instinct.

### Verification

Selftest **23 -> 33**. The new cases pin the threshold from both sides (10dp
UNIQUE, 9dp WEAK), that 4dp with one candidate is WEAK not UNIQUE, that a named
witness outranks a weak digit count, and that a single ambiguous literal poisons
an otherwise-unique block.


---

## 2026-08-16 (cont.) — the WEAK bucket is exhausted: 0 of 11 declarable

Every one of the 11 WEAK candidates matches at **4 or 5 decimal places**. Not
some — all. Two were checked semantically, chosen as the most plausible, and
both are false:

**The Q-value cluster (4 of the 11, 4dp).** `ex:qvalue-benchmark-table`,
`rem:qvalue-derivation-chain`, `rem:qvalue-observation`,
`prf:spectral-decomposition-qvalue` → `sublemma-2-1-A-operator-extract-h9-pn`
on `0.5904`. The block calls it *"the Rosso–Jones weighted average over the two
degree-2 torus knots"*; the witness stores `0.5904453769109197` as
`A_per_pair.((5,1),(1,1,1)).frobenius_norm`. Already recorded above.

**`rem:F3-eps6-leading-eq-neg-2b-cubed` (5dp) — and this one is a NEW failure
class.** The block writes `≈ −1.29904`; the witness has
`.data.c1_inclusive_rungs_numeric.1 = 1.2990381056766579701`. The signs differ,
and the value is **`3√3/4 = 1.299038105676658`** — a pure geometric constant.

That is not a decimal coincidence in the earlier sense. Both quantities
*genuinely equal* `3√3/4`, for unrelated reasons, because both live over ℚ(√3).
**A match can be arbitrarily exact and still carry no provenance when the shared
value is a constant the corpus derives independently in many places.** Precision
does not rescue that: pushing `STRONG_MATCH_DECIMALS` higher would not have
caught it, because the agreement is real.

### Where that leaves the axis

Coverage-based triage is **exhausted**. Across 151 nominally coverable blocks it
produced exactly **one** declarable result — `prf:crystal-isospin-degeneracy`,
declared, and it succeeded on a signal none of the others had: 19 matched digits
*plus* the witness carrying the block's actual claim (³He and T sharing
`S_crystal_at_q_zero`, which IS the degeneracy being proved).

So the remaining 212 failing blocks will not be closed by matching numbers. What
would close them is provenance stated at the source — a block naming the script
it took its values from, or a producer declaring which blocks consume its
outputs. That is a different mechanism, not a better threshold, and it should be
scoped as its own bean rather than pursued by tightening this one.

**No further declarations made.** Batch-declaring the WEAK bucket would have
attached eleven false sources that this axis could never afterwards detect,
which is the failure mode the whole triage exists to prevent.
