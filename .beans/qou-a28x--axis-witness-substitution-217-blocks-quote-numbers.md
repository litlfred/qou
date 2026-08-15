---
# qou-a28x
title: 'AXIS: witness-substitution -- 217 blocks quote numbers no declared witness carries'
status: todo
type: task
created_at: 2026-08-10T03:43:44Z
updated_at: 2026-08-10T03:43:44Z
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
