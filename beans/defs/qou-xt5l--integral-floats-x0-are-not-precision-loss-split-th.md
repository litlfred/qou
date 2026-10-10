---
# qou-xt5l
title: 'Integral floats (X.0) are not precision loss: split them out of the float64 ratchet into a separate integer-field gate with a declared registry'
status: completed
type: task
priority: normal
created_at: 2026-08-24T13:45:38Z
updated_at: 2026-08-24T14:12:22Z
---


## What was wrong

`witness_raw_float64_audit` asks one question: did a value lose digits a double
cannot hold? An integral float — `0.0`, `54.0` — answers **no**, because
integers are exact in binary64. It counted them anyway, so a JSON serialisation
detail was indistinguishable from a dropped digit.

The cost was concrete. Re-running eight producers on 2026-08-24 flipped 82
fields and the ratchet called every one a REGRESSION. Checked pair by pair:

```
int -> float pairs whose VALUE is unchanged : 80
int -> float pairs whose value CHANGED      :  0
```

46 were literally `0` -> `0.0`; 2 were genuinely new fields. None of the eight
producers was modified by the branch — the flip came from this container's
library versions. The gate was red on a serialisation artifact while the same
branch drained 3,555 real fields.

## Why the obvious rule is wrong

"A float whose value is integral should have been an int" is wrong ~99% of the
time here: **225,385 integral floats across 856 live witnesses, 218,697 of them
exactly 0.0**, overwhelmingly `matrix_im` / `matrix_re`. The imaginary part of a
real number is a REAL that is zero — `0.0` is the correct encoding and `0` would
be a false claim.

The converse fails too, and both failures are live:

| field | int | float-integral | fractional | naive verdict | truth |
|---|---|---|---|---|---|
| `matrix_im` | 0 | 160,704 | 0 | "always whole ⇒ integer field" | a REAL, always exactly 0.0 |
| `word_cd` | 165 | 247 | **83** | "braid word ⇒ integer field" | has fractional entries |
| `dim_S_lambda` | 77 | 100 | 0 | — | genuinely a count, written both ways |

So intent is **declared**, never inferred.

## What was built

- **`computations/witness-integer-fields.json`** — the registry. Declared
  integer fields (`dim_S_lambda`, `A`, `N`), each with a reason a reader can
  check and corpus evidence; plus `known_real_fields` so the candidate detector
  stops re-proposing `matrix_im` and a future reader does not "fix" it.
- **`computations/witness_integer_field_audit.py`** — the gate. A declared
  field serialised as a float is a violation. Wired into
  `scripts/precision-gates.sh`, because a gate wired nowhere is a gate nobody
  runs — the exact failure that script's own header was written about.
- **Float ratchet**: integral floats moved to their own `INTEGRAL` bucket,
  reported but not counted as raw float64.

**Integrality only excuses a float when nothing contradicts it.** The ratchet's
self-test caught my first attempt: a `0.0` beside a `_str` companion reading
`4.2e-44` is not an exact integer, it is a value that rounded away to nothing —
the worst loss this gate can find. So when a companion is present and does not
agree, every float underneath counts, integral or not. Self-test 25/25.

The candidate detector uses **"written both ways, nothing fractional"** rather
than "always integral" — a genuine real is not written as a bare int by
accident. It immediately found `N` (28,029 int / **1** float) and `A` (28,033 /
**1**), both nucleon counts, both stray in one witness.

## Two producer defects it found

1. `chi_lambda_multi_block_first_measurement` and
   `chi_lambda_he4_full_partition_table` both did `"dim_S_lambda": float(dim)` —
   a Specht dimension explicitly cast to float, 100 fields. Now `_as_dim`,
   which **refuses** a non-whole value rather than rounding it away, because a
   fractional dimension would be a finding about the character routine.
2. The `N`/`A` strays live in `4he-binding-full-pipeline`, which self-declares
   `scriptFile: "(legacy — no matching producer found)"` and whose only producer
   is under `_deprecated/`. "Fix at the producer" is impossible there, so the
   gate reports **no-live-producer** violations separately instead of failing.
   That is a RULE, not a per-file carve-out: it cannot hide a new defect,
   because a newly written witness has a live producer by construction.

## And one the split exposed

With the ratchet no longer drowning in integral floats,
`witness_float64_padding_audit` went RED on `inverse-markov-qvalues` — **mine**,
introduced by regenerating it. `Q_TRITIUM_MEV` shipped as

```
0.01861000000000000154098955817971727810800075531005859375   (40 fabricated digits)
```

The producer states the rule in its own comments — "Precision must be raised
BEFORE the module-scope constants" — and then calls `set_compute_dps()` at line
156 while building those constants at line 57. An `mpf` created at the default
dps=15 holds ~53 bits, so printing it later at dps 50 shows the binary64
expansion rather than the value, and raising dps afterwards cannot recover what
was never stored. Moving the call above the block gives `0.01861`.

## Measured

```
raw-float64 ratchet    NEW 0, REGRESSED 0            (was REGRESSED 8)
  integral-valued      225,078 fields in 852 witnesses, reported not counted
  drain caveat printed so +228,450 is not read as work done
integer-field gate     0 violations; 2 in a no-producer witness; 13 candidates
scripts/precision-gates.sh   All blocking precision gates green
```
