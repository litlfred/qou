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

---

# The term-3 crash is FIXED — and it exposes a third blocker

`atom_character_raw` (reached via `atom_markov_trace` ← `binding_from_frobenius_pairing`)
carried the **unguarded** sparse branch:

```python
if sparse_sigmas:
    M_run = M
    for c, d, gen in chain:
        Msig = sig_sparse.T.dot(M_run.T).T   # raises once M_run is dtype object
        M_run = c * Msig + d * M_run
```

That is term 1's **pre-fix** code. The COO object-dtype fallback added to
`unified_iterative_correction` in `da645cf0f32` was never ported here. Two
occurrences of the identical block existed; **both are now fixed.**

The fix is the same one: accumulate over `sigma`'s nonzeros — `O(dim·nnz)`, the
same complexity the float64 branch gets from sparse BLAS — with the densified
COO cached per generator, and no coercion of `c`/`d` to float.

## What the fix reveals

**Term 3 no longer raises. It now does not terminate.**

Deuterium ran **> 12 minutes** without completing, where before it raised in
0.52 s. py-spy: 3/3 samples inside the new COO accumulation
(`hecke_core_legacy.py:1716` and `:1719`), in `mpmath.__add__` / `__mul__`.

So term 3 has the **identical performance wall as term 1** — Python-level
`mpmath` scalar arithmetic over partitions up to `dim 2310` — and it was hidden
behind the crash exactly as the crash was hidden behind term 1's hang.

## Blockers: three, not two

| # | blocker | status |
|---|---|---|
| 1 | seminormal family is not a representation | settled (`qou-4m9u`); moves term 1 by 71–221 % |
| 2 | term 3 object-dtype crash | **fixed here** |
| 3 | Python-mpmath performance wall in **both** term 1 and term 3 | term 1 partly (5.8× guard fix); term 3 untouched |

The Rust kernel `lp_accumulator_step_traces_mpfr` was written for term 1's loop.
Term 3's loop has the same shape — identity start, per-crossing
`M ← c(M·σ) + dM`, rescale, trace — so the same kernel should serve it, but that
is **asserted from the shape, not measured**; nothing has been wired.

## Honest status of the original task

`qou-i7ju` asked for a witness regeneration. Four sessions of work later the
accurate statement is: **the producer cannot run, for three independent
reasons, and one of them means the numbers it used to produce were computed
from matrices that do not represent the algebra.** The regeneration is not
close, and making it fast would not make it right.
