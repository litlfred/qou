# `binding_energy` cannot succeed for any A ≥ 2 on `main` today

**Measured 2026-08-31** on `origin/main` `ac21a59e63`. Follow-on from
[the braid-relation audit](2026-08-31-ysn-matrices-are-not-a-representation.md)
(`qou-sv7h`, `qou-4m9u`). This is the second half of `qou-sv7h` step 2: measure
the other two terms of `binding_energy`.

## The finding

`binding_energy` is three terms, applied in this order:

```python
B = unified_iterative_correction(Z, N)                 # term 1
if sdp:       B += sdp_cross_channel_contribution(Z, N)[0]   # term 2
if frobenius: B += binding_from_frobenius_pairing(Z, N)      # term 3
```

- **Term 1 never returns** for A ≥ 2 (measured previously: > 50 min on
  deuterium, projected ~40 days pre-fix).
- **Term 3 raises in 0.52 s**, on `main`'s own code:
  `TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))`
  — the scipy-refuses-object-dtype error.

So term 3's failure is **latent, masked by term 1's hang**: control never
reaches it.

**Demonstrated by stubbing term 1 and leaving terms 2 and 3 exactly as `main`
has them:**

```
  binding_energy(1,1) [deuterium] RAISES TypeError: no supported conversion ...
  binding_energy(1,2) [tritium  ] RAISES TypeError: no supported conversion ...
  binding_energy(2,2) [he4      ] RAISES TypeError: no supported conversion ...
  binding_energy(3,4) [li7      ] RAISES TypeError: no supported conversion ...
```

**Four of four.** So `binding_energy(Z,N)` for A ≥ 2 has **two independent
blockers**, and fixing only the performance one converts a hang into a crash.

## Term 2 is unaffected — and is zero

`sdp_cross_channel_contribution(1,1)` returns **`0.0`**, both with the current
matrices and with the corrected (Rust MPFR) family. Measured 27.9 s current /
67.1 s corrected. So for deuterium the SDP term contributes nothing and the
representation defect does not move it.

That is measured **at A = 2 only**. `sdp_cross_channel.py` consumes
`_build_ysn_matrices` directly, so at larger A it may well be affected — that
is untested and should not be assumed either way.

## What this means for `qou-i7ju`

The `hadron-knot-table` regeneration was never merely slow: **it is impossible
on the current code**, and would be impossible even with the performance work
finished. Consistent with the committed witness:

```
computations/hadron-knot-table.witness.json
  computedAt      2026-06-17T04:13:13
  scriptCommitSha 08ec1c0d0999b6b6d8c902a4ec8fa5344a383a2d
```

**Two and a half months old.** Its binding values date from before whatever
broke term 3, and nothing since has been able to reproduce them.

## Ordered blockers, corrected again

The `qou-sv7h` list is now:

1. **The seminormal family** — derived and settled (`qou-4m9u`): the Python
   build is not a representation; the correct entries are
   `a = −1/(q(q²+1))`, `b = √(q⁴+q²+1)/(q²+1)`. Moves term 1 by **71–221 %**.
2. **Term 3's object-dtype crash** — NEW, this document. Same failure class the
   COO accumulator fixed in term 1, unfixed here.
3. Term 1's performance (guard fix landed, 5.8×; Rust kernel built, unwired).
4. Only then regenerate.

## Not established

- The corrected-family run of term 3 had not completed at 10 min and is **not
  reported**. Whether the crash is independent of which matrices are used is
  untested — though the error is a dtype conversion, which suggests it is.
- No corrected binding value has been produced for any atom, so **no comparison
  against AME2020 exists**. Whether the corrected framework agrees better or
  worse with experiment remains unmeasured, and nothing here bears on it.
