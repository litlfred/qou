---
# qou-ns02
title: 'Witness integrity: 1 unparseable, 1 non-object root, 2 anchor-without-value'
status: todo
type: task
created_at: 2026-08-19T20:54:16Z
updated_at: 2026-08-19T20:54:16Z
---


## Found by

`q0_anchor_consistency_audit` on a clean tree, 2026-08-19, while checking
the arc's other work. Four items, all small, all in the
witness-provenance lane:

| item | file | what |
|---|---|---|
| `Q0_PARSE_ERROR` | `computations/_deprecated/qbeta-gb-filtration-residues.witness.json` | malformed JSON — `Expecting value: line 28 column 22`. Under `_deprecated/`, so low priority, but it is the only unparseable witness in the corpus. |
| root not an object | `computations/iterative-knot-builder.witness.json` | **not** deprecated. Every audit that does `body.get(...)` skips it silently. |
| `Q0_VALUE_MISSING` | `computations/atomic-tr-m-mpfr-50dps.witness.json` | declares an anchor with no `q0Value` to check it against |
| `Q0_VALUE_MISSING` | `computations/atomic-tr-m-mpfr-50dps-proton.witness.json` | same |

## Why it is worth doing rather than ignoring

None of these is a wrong number. They are witnesses that **no checker can
read**, which is the same failure shape as the arc's other findings: an
artifact that is skipped reports as clean. The `iterative-knot-builder`
one is the live case — a non-object root means every `q0`, precision and
staleness audit passes over it without a verdict.

The two `atomic-tr-m-mpfr-50dps` pair are more interesting than the count
suggests: one is muon-named and one proton-named, so they are a
deliberate two-layer comparison, and neither records the value it used.
That is exactly the layer-straddle case AGENTS.md warns about, in the one
place it would be hardest to detect by eye.

## Scope

Small. Each is a producer re-run or a one-field fix, except the malformed
JSON, which needs its producer identified first — it may be an
interrupted write rather than a code defect.

## 2026-08-19 — two of four closed, and one was a hidden Q0_FLIP

### The `atomic-tr-m-mpfr-50dps` pair was the serious one

Filed here as "two witnesses declaring an anchor with no value". It was
worse than that: the muon-labelled witness carried **proton numbers**.

Proof, independent of timestamps (its `computedAt` is 66 s *before* the
corrupting commit, so timing alone proves nothing — a commit time is not
a write time): its recorded q0 is **byte-identical** to what
`q-pinning-50-digit.witness.json` held AFTER `9a9c6b31c7` corrupted it,
and differs from what that file held before. `q0_for("ideal")` reads that
pin file directly, so the run consumed the corrupted keystone.

Confirmed the numbers and not just the label: before the re-run the
muon-labelled and proton-labelled witnesses agreed **to 49 digits**. Two
pins 11.54 ppb apart cannot do that — they were the same run twice, so
the pair that exists to BE the two-layer comparison was comparing proton
against proton.

**Why nothing caught it for four days.** The audit reads `q0Value`; the
producer wrote the same string under `q_0_50dps`. With no value to check
the anchor against, a genuine `Q0_FLIP` — the CI-failing class — was
filed as the benign `Q0_VALUE_MISSING`. The value was there the whole
time, under a name nothing reads.

Fixed at both levels: re-ran at `--anchor ideal` against the restored
pin, and taught the producer to emit `q0Value`.

    q0 shift  11.537 ppb exactly (the mu-p tension)
    tr_M      p 77.9 / n 69.1 / d 148.2 / t 190.8 / 3He 246.2 ppb

The tr_M response exceeds 11.537 because tr_M is a polynomial in q whose
degree grows with the braid word, so the shift is amplified by
d(ln tr_M)/d(ln q). Measured, that sensitivity rises monotonically with
word length: 6.0-6.8 at 11 crossings, 12.9 at 23, 16.5-21.3 at 35.
Checked rather than assumed — my first pass flagged these as "unexpected"
against a naive 11.54 ppb expectation, which was my error, not a finding.

    Q0_VALUE_MISSING  2 -> 0
    Q0_OK           658 -> 660

**Blast radius, checked before claiming a wave.** 14 witnesses carry the
corrupted 70-digit string, but that string is also the legitimate
70-digit rendering of the proton pin. Only **one** claims the muon layer
while holding it. Seven legitimately declare proton; six declare no
anchor (part of the 1906 `ANCHOR_MISSING` population). One witness, not a
wave.

### `iterative-knot-builder` — investigated, NOT fixed here

Deliberate: `iterative_knot_builder.py` is on the R3 off-canon list in
the convention-D owner ruling (it uses `pn_convention="strict_averaged"`)
and is therefore claimed by bean `qou-cds4`. Whoever fixes the convention
re-runs it, and that is the right moment to fix the envelope too rather
than touch the file twice.

Recording what I found, because none of it is in `qou-cds4`'s scope:

- **No witness envelope at all.** `json.dump(results, f)` of a plain
  list — the P30 raw-emit class. No provenance, so no staleness
  detection. `derivation_chain_validator.py` carries an explicit special
  case to tolerate the array shape.
- **`reduced_crossings` is `initial_crossings`.** Both are `len(word)`,
  the same expression. `build_and_reduce` performs no reduction, and
  `reduced_knot_name` is the constant `"q-clt-proxy"`. A file named
  "iterative knot builder" records a reduction it does not do.
- **`volume` is not a volume.** It is `Σ log|V_i|` — a log of a product.
  Values run 7.8e6 to 1.3e8, which is not a hyperbolic volume of
  anything.
- **A timeout stored as a result row.** Record 5 is
  `{"Z":6,"N":5,"A":11,"error":"Timeout after 300s"}`, sitting in the
  same array as the results — the "a failed run journalled as done"
  pattern the tnjb sweep called out as a driver bug.
- **A hardcoded muon q0 float64 literal**, line 16:
  `HA = 1.10997859555733471989976 - (1/1.10997859555733471989976)`.
  No pin import, no anchor declared. Its one use is a classification at
  1e-6 tolerance, so float64 does not harm *that* decision — but the
  `volume` log-sum is accumulated with `math.log` over float64, which
  AGENTS.md rule 2 names directly.

Nothing consumes the numbers — the validator only mines the file for
`scriptFile` — so this is not urgent. It is, though, a witness that
claims things it does not do, unnoticed because no audit can read it.

### Remaining

`computations/_deprecated/qbeta-gb-filtration-residues.witness.json` —
malformed JSON, `Expecting value: line 28 column 22`. Under
`_deprecated/`, lowest priority of the four.
