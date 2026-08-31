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

---

# Blocker 3 is solved: full `k = 11` deuterium in 278 s

`lp_accumulator_step_traces_mpfr` (merged #6337) driving the per-partition
accumulation, deuterium, increasing truncation:

```
  k_exact= 4     28.37s   (first call — includes materialising the partition table)
  k_exact= 5      0.00s
  k_exact= 6      0.01s
  k_exact= 7      0.04s
  k_exact= 8      0.21s
  k_exact= 9      1.83s
  k_exact=10     21.33s
  k_exact=11    278.44s   <-- the PRODUCTION truncation
```

**Python could not complete `k = 11` at all** — measured > 50 min and projected
~40 days pre-guard-fix. The Rust kernel does it in **4 minutes 38 seconds**.

The kernel builds its seminormal matrices internally via
`seminormal_matrices_mpfr`, so wiring it in addresses **blocker 1 and blocker 3
together**: the correct representation and the tractability arrive in the same
change.

## 🛑 The VALUES above are NOT `unified_iterative_correction`

Stated prominently because the numbers are seductive and wrong to quote.

The driver used here is a **reimplementation** of the accumulation, and it
**omits Pass 2 — the final-state complementary-slackness gate**, under which a
partition whose Frobenius constraint is slack "contributes 0". It also does not
reproduce the free-nucleon baseline subtraction. So `-17.69` is **not**
`unified_iterative_correction(1,1)` and must not be reported as a binding
number.

Independent evidence that the reimplementation is unfaithful, not merely
imprecise: at `k_exact = 4` it gives `-0.4122`, where the *real* function driven
by the *same* corrected matrices gave `-0.0896` — a factor of 4.6. Both use the
correct family, so the gap is the missing gate, not the mathematics.

## What is and is not established

**Established:**
- The Rust kernel completes the full `k = 11` per-partition accumulation for
  deuterium in 278 s. Blocker 3 is tractable.
- It carries the correct seminormal family by construction.

**Not established:**
- **No binding value.** Nothing here is `unified_iterative_correction`,
  `binding_energy`, or a `B(K)`.
- **No AME2020 comparison.** Whether the corrected framework agrees better or
  worse with experiment remains completely unmeasured.
- Whether the same kernel serves term 3's loop — asserted from its shape, still
  not measured.

## The remaining work, precisely

1. Wire `lp_accumulator_step_traces_mpfr` into `unified_iterative_correction`
   **preserving Pass 2** — the gate is the part a reimplementation drops, and it
   is what makes the result an LP dual rather than a log-trace sum.
2. Wire it into `atom_character_raw` (term 3) likewise.
3. Gate both with a value-equality check at small `k`, the way the sparse-guard
   fix was gated — noting that exact equality against the *current* code is
   impossible by construction, since the corrected matrices deliberately change
   the answer. The gate has to be against a *reference implementation on the
   corrected family*, not against `main`.
4. Then, and only then, regenerate and report what moved against AME2020.

Point 3 is the subtle one and is why this stops here rather than pressing on.

---

# Blocker 4 resolved: the kernel is verified

I earlier framed the gate's reference as a decision for the author. **It is not
— it is work, and this is it.** The right reference is the same recurrence in
pure mpmath over the *corrected* matrices, and building it is unambiguous.

[`computations/audits/lp_accumulator_kernel_gate.py`](../../computations/audits/lp_accumulator_kernel_gate.py),
re-runnable, exit 0 today:

```
partitions: 43  (k <= 7)   ordering: ['p', 'n']
  checked 86 (partition, step) traces
  1 cancelled to numerically zero on BOTH sides (excluded from the ratio)
  worst relative deviation = 7.092e-48
VERDICT: kernel agrees with the pure-mpmath reference to ~50 dps.
```

Two design points the script documents, because both are easy to get wrong and
I got each wrong once:

- **Both sides must use the SAME (Rust) matrices.** My first attempt compared
  the kernel against mpmath-over-the-*Python* matrices and mismatched — but that
  mismatch was the braid defect, not a kernel error. Comparing against `main` is
  likewise invalid: the corrected matrices deliberately change the answer, so
  equality with `main` would mean the correction had not been applied.
- **The tolerance must be mixed absolute/relative.** One step trace cancels to
  ~1e-51 — numerically zero at 50 dps — and a relative test there compares noise
  to noise and reported a 1.58 "deviation" that meant nothing. That was my gate
  failing, not the kernel. Production guards the same quantity the same way
  (`abs(tr_run) > 1e-300`).

## Where the arc stands

| # | blocker | status |
|---|---|---|
| 1 | seminormal family is not a representation | settled; fixed *by* the kernel, which builds the correct family |
| 2 | term 3 object-dtype crash | fixed |
| 3 | performance wall | solved — full `k = 11` deuterium in 278 s |
| 4 | the equality gate | **built and passing (7.09e-48)** |

**What remains is one change and it moves published numbers:** wire the kernel
into `unified_iterative_correction` and `atom_character_raw` **preserving Pass 2**
(the complementary-slackness gate — the part a reimplementation drops), then
regenerate and report the movement against AME2020.

That is a deliberate stopping point, not an unfinished one. Everything up to it
is verified; the step itself changes what the paper reports, and its result —
better or worse agreement with experiment — is still completely unmeasured.
