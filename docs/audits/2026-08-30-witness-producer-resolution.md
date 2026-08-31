# Which witnesses actually have no producer? 19 — and every prior count was wrong

**Date:** 2026-08-30 · **Bean:** `qou-agvb` · **Detector:**
[`computations/audits/witness_producer_resolution_audit.py`](../../computations/audits/witness_producer_resolution_audit.py)

## The count

**19 of 2940 live witnesses have no producer anywhere in the tree.** Each of the
nineteen was verified individually, not sampled.

| verdict | count | meaning |
|---|--:|---|
| `RESOLVED` | 2707 | the witness **cites** a `.py` that exists |
| `FOUND_BY_CONVENTION` | 188 | id snake_cased (± `_probe`/`_audit`/…) **is** a real script |
| `FOUND_BY_PRODUCER_CALL` | 25 | a live script **constructs** this witness id |
| `NAMED_BUT_MISSING` | 0 | cites a `.py` that does not exist |
| `PRODUCER_DEPRECATED_ONLY` | 1 | only `_deprecated/` produces it |
| **`ORPHAN`** | **19** | nothing in the tree produces it |

## Every prior count over-reported, including two of my own

| method | orphans | vs. 19 |
|---|--:|--:|
| `scriptFile` key only (`qou-tekx`) | 298 | 15.7× |
| + `computation` (`qou-bake`'s correction) | 145 | 7.6× |
| + `producer` (`qou-agvb`, my last turn) | **139** | **7.3×** |
| value-based, *cites* a real `.py` | **233** | **12.3×** |
| + convention + producer-call (this audit) | **19** | — |

Two things in that table are worth more than the final number.

**My own "139" was an over-report by 7×**, and I published it. The correction I
made to `qou-bake` was real — `producer` *is* a third spelling it missed — but
adding a fourth key to a method that was wrong in kind does not fix it.

**The value-based method was WORSE than the key-based one it replaced** (233 vs
139), which is the opposite of what I predicted when I proposed it. Asking
"does the witness cite a `.py` that exists?" is a *stricter* question than
"does some provenance key exist?", so it flags more. Strictness is not accuracy.
The key-based count was accidentally closer because `computation` is present on
91 % of witnesses, and a witness with a `computation` usually does have a
producer — for a reason unrelated to what that field contains.

## Why key-presence cannot work: the fields are polymorphic

| key | carriers | names a real `.py` |
|---|--:|--:|
| `computation` | 2679 | **46** |
| `scriptFile` | 2642 | 2635 |
| `producer` | 64 | 56 |
| `source` | 51 | 4 |
| `scriptPath` | 8 | 8 |

`computation` is present on 91 % of witnesses and names a producer on **1.7 %**
of those — in the standard `WitnessBuilder` format it holds the witness **id**
(`yekutieli-volume-join`), not a script. It holds a path only in the
hand-written `docs/audits/scripts/` family `qou-bake` found, which is why that
correction looked right on its five and does not generalise. `source` is
polymorphic the other way: usually a literature PDF, occasionally a `.py`.

## What the detector does, and the two bugs found in it

It decides by **value, then by existence**: does any candidate field hold a
resolvable `.py`; failing that, does a script exist by naming convention;
failing that, does any live script *construct* this witness id.

Two false-positive classes were found in my own first version, in **opposite
directions**, and both are recorded in the script:

- **`ORPHAN` over-reported.** `gswz_52_symmetrization.witness.json` is produced
  by `gswz_52_symmetrization_probe.py` — the `_probe` **suffix**. Worse, the
  mention index tokenised only *hyphenated* ids, so every underscore-named
  witness was invisible to it. That miss accounted for most of a 30-item list.
- **`FOUND_BY_MENTION` over-reported.** `4he-binding-full-pipeline.witness.json`
  — whose own `scriptFile` reads *"(legacy — no matching producer found)"* —
  was rescued by `witness_provenance_audit.py`, an audit that **reads** it and
  writes its own witness. "Mentions the id and writes something" is not a
  producer signature. Replaced by `WitnessBuilder("<id>")` / writes
  `<id>.witness.json`.

The six near-miss orphans were each checked by hand rather than by prefix:
`canonical_mass_table_extended.py` writes `canonical-mass-table-extended` and
`mass-table-ppb`, **not** `-242ppb`; `meson_spectrum_predictions.py` writes
`meson-spectrum-predictions`, **not** `meson-spectral-analysis`;
`tau_hat_n_proton_realisation.py` writes `-realisation`, **not**
`-level-1-empty`; `forward_ref_classifier.py`, `hecke_core_symbolic.py` and
`whitehead_volume_search.py` write no witness at all. A similar name is not a
producer.

## Scope

This says a producer **exists**, not that it **reproduces** the witness — that
is [`witness_provenance_audit.py`](../../computations/witness_provenance_audit.py),
which asks whether a `scriptFile` actually writes its witness and is strictly
stronger where it applies. The two compose: it needs a `scriptFile` to start
from and therefore cannot see the 213 witnesses resolved here by convention or
producer-call. Neither audit rewrites a witness or proposes a canonical
spelling; naming one is the owner's call.

Entry in [`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md):
same shape as the convention-C sqrt-variable spelling and the `sys.path[:0]`
miss — a detector keyed on one way of writing a thing, in a corpus that writes
it several ways. The novelty here is that the *fix* had the same defect twice
before it was right.
