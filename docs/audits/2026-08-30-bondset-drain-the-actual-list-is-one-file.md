# The `C(A,2)` bond-set drain, read file by file: the actual list is **one file**

**Date:** 2026-08-30 · **Bean:** `qou-gecf` · **Type:** completed triage (18 files read)
**Predecessor:** [`2026-08-30-bondset-drain-triage-is-mostly-false-positives.md`](2026-08-30-bondset-drain-triage-is-mostly-false-positives.md)

## Result

| stage | count |
|---|---:|
| grep upper bound (`qou-k12x`) | 67 |
| after automated narrowing | 18 |
| **after reading all 18** | **1** |

And the one is a **mislabelled metadata field, not a wrong number.**

## The one

**`computations/rho_k_counit_isotope_systematics.py`** had

```python
N_INTERFACES = {"D": 1, "T": 3, "3He": 3, "4He": 6}  # C(A,2) nucleon pairs
```

emitted as `"n_interfaces"`. The canonical braid wires a **chain of `A−1`**
interfaces (D 1, T 2, ³He 2, ⁴He 3), so three of the four values contradict the
field's own name. **Impact is bounded**: the field is descriptive metadata
sitting beside the actual computation (`counit_sum_chi`, `abs_ratio`), and
grep finds no other consumer of it from this producer. So no computed number is
wrong.

Fixed minimally by renaming to `N_NUCLEON_PAIRS` / `n_nucleon_pairs` — the
comment already said "nucleon pairs", so the name now agrees with the value and
**no number changes**.

## Why the other 17 are correct — six classes no grep can separate

| class | n | why it is correct |
|---|---:|---|
| **proved cap** `ρ_A ≤ C(A,2)` | 5 | an inequality *bound*, not a bond set |
| **convention-aware prose** | 4 | says "complete graph", "tree A−1", or *"the braid only wires A−1 chain bonds"* — my regex only knew "all-pairs"/"linear chain" |
| **narrative mention** | 3 | docstring describing a past result; no computational use |
| **my own probes** | 2 | reproduce the July GAP-2 result deliberately |
| **cumulant inversion** | 1 | `a4_h12_brunnian_deficit_measure_probe` inverts `mu2/mu3/mu4` and **asserts** the reconstruction is an identity — definitional, and invisible to a `b2/b3/b4` regex |
| **Coulomb all-pairs** | 1 | see below |
| **junk/null control** | 1 | `perknot_additive_sk_vs_kA_extensivity` uses `C(A,2)` deliberately as a baseline to calibrate any "match" |

**The Coulomb case is worth its own line, because it is physics rather than
bookkeeping.** `mirror_isospin_coulomb_split._cat_split` computes

```python
sig = comb(Z, 2) * L["pp"] + Z * N * L["pn"] + comb(N, 2) * L["nn"]
return E0 * (A - 1) * sig / comb(A, 2)
```

It uses `C(A,2)` as a **normalisation denominator** and `(A−1)` as the actual
bond count — i.e. the mean channel-typed weight per pair, carried by the chain.
That is *already* the chain convention, and the file is more correct than the
grep suggested. Coulomb repulsion is genuinely all-pairs (long-range) in any
case, so a `C(A,2)` in a Coulomb term needs no defence.

## What this says about the method

The automated narrowing had **1/18 precision**. Every one of the six exclusion
classes above required reading the surrounding argument; none is expressible as
a pattern. The predecessor audit estimated the true residual at "~5–6 files"
from a 3-file sample — **that estimate was too high by 5×**, and it was mine.

The general lesson, which is the durable part: a grep over a *convention* finds
every site that mentions the convention's vocabulary, and conventions are
mentioned far more often by code that is **reasoning about** them than by code
that is **wrong about** them. The ratio here was 17:1.

## Scope

Every verdict above is from reading the file. The one fix changes a name and a
comment, no arithmetic. Nothing is wired, no witness is regenerated, and no
number in the corpus moves.
