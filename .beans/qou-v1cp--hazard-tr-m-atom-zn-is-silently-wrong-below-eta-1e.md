---
# qou-v1cp
title: 'HAZARD: tr_m_atom_zn is silently wrong below eta ~ 1e-10 -- flavour degeneracy'
status: todo
type: bug
priority: high
created_at: 2026-08-31T16:52:45Z
updated_at: 2026-08-31T16:52:45Z
---


## The hazard

`tr_m_atom_via_transfer.tr_m_atom_zn(Z, N, q=exp(η))` returns **silently wrong**
values for `η ≲ 1e-10`. It does not raise, does not warn, and returns
plausible-looking numbers.

Measured — `(Δtr − c₀(A))/ℏ_q` for the three 2-nucleon bond types, `dps = 90`:

    eta      pp                  pn                  nn
    1e-3     2.38616994236196    2.32513115457367    2.26361229176631
    1e-5     2.37511156385174    2.31262594121742    2.25013562995339
    1e-7     2.37500111562514    2.31250125937537    2.25000135625050
    1e-9     2.37500001115625    2.31250001259375    2.25000001356250
    ───────────────────────────── discontinuity ─────────────────────────────
    1e-11    3.75000000041063    3.75000000041063    3.75000000041063
    1e-13    3.75000000000411    3.75000000000411    3.75000000000411
    1e-15    3.75000000000004    3.75000000000004    3.75000000000004

Two independent tells that the lower block is the broken one:

1. **A limit does not jump.** The upper block converges cleanly at `O(η)` —
   errors `1.1e-4 → 1.1e-6 → 1.1e-8` for a `100×` cut in `η` each time — to
   `19/8`, `37/16`, `9/4`. Then the value discontinuously changes.
2. **The three flavours become identical.** `pp`, `pn` and `nn` return the *same*
   number below the threshold. The flavour distinction lives entirely in the `d`
   coefficients of the braid word (`d ∈ {0, −h, −h/2}`, `h = q − 1/q`), so its
   disappearance means those coefficients have stopped contributing.

**It is not an mpmath precision problem.** `dtr` at `η = 1e-13` is bit-identical
at `dps = 60` and `dps = 90`:

    dps=60  0.125000000000375000000000391875
    dps=90  0.125000000000375000000000391875

so raising working precision does not help and does not signal anything. The
loss is upstream of the trace evaluation — in the word construction or the
transfer kernel, where something is comparing against a fixed tolerance rather
than scaling with `h`.

## Why it matters

Every `ℏ_q`-order measurement in this session's binding work
(`hbar_q_order_of_binding_observables_probe`,
`classical_floor_derivation_probe`, `binding_chain_floor_corrected_probe`) is a
`q → 1` extrapolation. **The natural instinct — "push `η` smaller for a better
limit" — silently corrupts the answer**, and the corrupted answer looks *more*
converged, not less, because it is stable to 12 digits across three decades.

This nearly landed a wrong result: a re-check at `η = 1e-12/1e-13` reported `c₁`
values 58–72 % away from the committed ones and, taken at face value, would have
falsified `QOU/MassTheory/PairwiseChainLeadingOrder.lean`. The committed values
are the correct ones; the "higher precision" run was the artefact.

## Safe practice, until this is fixed

* **Stay in `η ∈ [1e-3, 1e-9]`.** Every result in the beans above was taken at
  `1e-3 … 1e-6`, inside the good range.
* **Always scan several decades and look for a monotone `O(η^k)` trend.** A value
  that is suddenly stable to 12 digits after being stable to 6 is a warning, not
  a success.
* **Cross-check flavour non-degeneracy.** `pp`, `pn`, `nn` must differ. If they
  coincide, the deformation has been lost.

## Not diagnosed here

Where exactly the threshold comes from. Candidates, in order of suspicion:

1. a fixed absolute tolerance in `reduced_block_kernel` / `chi_free_via_lr`
   comparing Hecke coefficients against something like `1e-9` or `1e-12`;
2. `y_lambda_at` / `y_lambda_su_n`, where `q_int(m,q) = (q^m − q^{−m})/(q − 1/q)`
   is `0/0`-shaped as `q → 1` and may be guarded by a tolerance;
3. `atom_braid_word_3A` dropping letters whose `d` falls below a cutoff.

(2) is the most likely — that expression already raised `ZeroDivisionError` at
exactly `q = 1` earlier in this work, so it is known to be the fragile point.

**Fixing it is worth doing**: a guard that raises instead of returning degenerate
values would have turned a near-miss into an error message.

## Narrowed 2026-09-04 — 3 of the 4 candidate sites EXCLUDED by measurement

The bean says the loss is "in the word construction or the transfer kernel".
Measured at `dps = 90`, sweeping eta across the threshold, it is **not the word
construction** — that half can be dropped.

**1. `flavor_split_leading(q)` is clean.** Smooth through the threshold, no
discontinuity, delta ~ (4/3)*eta^3 all the way down:

    eta      delta
    1e-9     1.3333333320000000017e-27
    1e-10    1.3333333332e-30
    1e-11    1.33333333332e-33      <- threshold is here; nothing happens
    1e-13    1.3333333333332e-39

Its body is two lines of exact mpf arithmetic with no tolerance and no float64.

**2. The BRAID WORDS still differ by flavour BELOW the threshold.** This is the
decisive exclusion. At eta = 1e-13, well inside the broken regime:

    flavour   word length   distinct d values
    pp        22            4
    pn        23            5
    nn        22            4

Identical structure at 1e-9 (correct regime) and 1e-13 (broken regime). So the
`d in {0, -h, -h/2}` coefficients that carry the flavour distinction are still
present and still distinct when the answer has already collapsed. **The flavour
information reaches the trace and is destroyed there.**

**3. The `y_lambda` weights are not it either.** `y_lambda_at(6, q)` returns 11
non-zero weights with identical values (to 8 digits) at eta = 1e-7, 1e-9, 1e-11
and 1e-13 — the same above and below the threshold, so they cannot produce a
discontinuity that appears only below it.

**Remaining suspect: `chi_all_lambda_reduced_block`** — the reduced-block
character kernel, the one factor in `_trM = sum y[lam] * chi[lam]` not yet
cleared. That is the "transfer kernel" half of the original hypothesis, now
isolated.

## A SEPARATE defect found while reading, not the same bug

`tr_m_atom_via_transfer.py:194` computes

    dtr = abs(tF) - abs(tA)

which is **not** `abs(tF - tA)`. If either trace crosses zero the difference is
wrong in a way no tolerance would reveal. This is in `main()`, which runs at the
production q0 (~1.11) rather than on the eta-sweep path, so it is NOT the cause
of the threshold collapse — recorded so it is not conflated with it, and so it
gets its own look.

## What was ruled out and should not be re-tried

The `1e-12` cache tolerance at lines 54-61 is **not** the culprit, despite
matching the cached-accessor shape AGENTS.md warns about. At eta ~ 1e-11 the
caller's q is ~1 + 2e-11, which is ~0.11 away from the witness's recorded q0 —
eight orders of magnitude outside the gate. The cache is missed, not hit.
