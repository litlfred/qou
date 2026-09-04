---
# qou-v1cp
title: 'HAZARD: tr_m_atom_zn is silently wrong below eta ~ 1e-10 -- flavour degeneracy'
status: completed
type: bug
priority: high
created_at: 2026-08-31T16:52:45Z
updated_at: 2026-09-04T07:20:00Z
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


## CAUSE FOUND AND FIXED — 2026-09-04

**The classifier in `chi_monotone_transfer.word_to_mpfr` used an ABSOLUTE
tolerance on a quantity whose own scale goes to zero.**

`word_to_mpfr` re-lifts each crossing's float `d` to full dps by matching it
against the four recognised templates

    0                       sigma
    -h                      sigma inverse
    -h/2                    averaged
    -h*(1/2 - delta/4)      color-weighted p-n, one per live delta convention

with `h = q - 1/q = 2*sinh(eta)`. Every template but the first is proportional
to `h`. The classifier tested them **in a fixed order against `_TOL = 1e-9`,
absolute**, so once `|h| < _TOL` every template lay within `_TOL` of every
crossing and the FIRST test won for the whole word:

    if abs(df) < _TOL:            # <-- always true once |h| < _TOL
        d_mp = mp.mpf(0)

Every `d` in the word was lifted to exactly 0, so the pp / pn / nn words became
numerically identical after lifting. No raise, no warning — exactly the
signature this bean recorded.

### The failure is STAGED, which is why the threshold looked like one number

The two nonzero templates cross `_TOL` at different eta, so the corruption
arrives in two steps. Measured at 90 dps, distinct lifted `d` for the pp word:

    eta       h = 2 sinh(eta)   #distinct d   tr_M(pp) - tr_M(nn)
    2e-9      4.0e-9                 3         2.25e-9
    1.2e-9    2.4e-9                 3         1.35e-9
    9e-10     1.8e-9                 2         6.75e-10     <- -h/2 lost
    5.1e-10   1.02e-9                2         3.825e-10
    4.9e-10   9.8e-10                1         0.0          <- -h lost too
    1e-10     2.0e-10                1         0.0

The 3 -> 2 transition lands where `h/2` crosses 1e-9 and the 2 -> 1 transition
where `h` does. The intermediate stage is worse than the total one: the answer
is wrong but still flavour-dependent, so it does not announce itself.

### Fix

`word_to_mpfr` now picks the **nearest** template rather than the first one
within `_TOL`, via a new `_d_templates(q, h)` helper. Nearest-match is
scale-free. The accept/reject set is unchanged — it still raises exactly when
no template lies within `_TOL` — so genuine convention drift still fails loudly
(the documented purpose of `_TOL`, bean `qou-j320`).

### Verification

- **Production is byte-identical.** D / T / 3He / 4He `tr_M_atom` and
  `tr_M_free` at the default pin, 30 significant digits, diffed pre- and
  post-fix: empty. Expected — at q0 the templates are separated by ~7.5e-5,
  four orders above `_TOL`, so nearest-match and first-within-tolerance agree.
- **The flavour split is now linear over ten decades**, `tr_M(pp) - tr_M(nn) =
  1.125*eta` from eta = 1e-9 down to eta = 1e-20, where it was exactly 0 below
  the threshold before.
- **Regression guard:**
  `computations/audits/word_to_mpfr_template_scale_audit.py`. Verified it
  FAILS on the pre-fix classifier (exit 1, 11 findings, catching the partial
  stage at 5e-10 as well as the total collapse) and passes after. A guard that
  was never shown to fail is not a guard.

### What this does NOT cover

- The **color-weighted** template sits only `h*delta/4 ~ (2/3)*eta^4` from
  `-h/2`, so those two are still merged by an absolute `_TOL = 1e-9` for
  `eta < ~3.5e-3`. Production q0 has `eta ~ 0.104` and a separation of
  ~7.5e-5, so it is unaffected, but any small-eta study of the color split
  specifically needs a tighter `_TOL`. Not fixed here; separate concern.
- `qou-h3qk` — the q-blind `_H3_TRANSITION_CACHE` — is a real, separate defect
  and was **tested for a causal link to this one and cleared**: with the cache
  explicitly emptied between the pp and nn calls the collapse reproduces
  identically. Still open on its own bean.
- ~~`tr_m_atom_via_transfer.py:194` computes `abs(tF) - abs(tA)` rather than
  `abs(tF - tA)`.~~ **RETRACTED 2026-09-04 — this was never a defect. See the
  section below.**


## RETRACTION — the `abs(tF) - abs(tA)` "sign bug" is not a defect

Earlier in this session I flagged `tr_m_atom_via_transfer.py:194`

    dtr = abs(tF) - abs(tA)

as a defect, on the grounds that it is not `abs(tF - tA)` and would be wrong if
either trace crossed zero. **That claim was wrong and is retracted.** It was
written into this bean, into PR #6586's body, into the commit message of
`21b3fc5ac0f`, and stated twice in chat.

Four things establish it, none of which I had checked before asserting it:

1. **The field it feeds is named `delta_tr_M_abs`** — "difference of absolute
   values". The name and the code agree exactly. The `_abs` suffix IS the
   author's disambiguator, and I read past it.
2. **Zero downstream consumers.** `grep -rn delta_tr_M_abs` over `.py`,
   `.json`, `.md`, `.ts` and `.lean` returns only the producer's own write and
   its own witness. Nothing reads it, so nothing can be misled by it.
3. **The corpus's `Delta tr_M` is a DIFFERENT quantity.**
   `QOU/BraidKnot/QBetaCategoricalPrecisionLadder.lean:402` defines it as
   `tr_M(beta_n) - tr_M(beta_p)` -- a different pair (neutron vs proton braid,
   not atom vs free) and signed. So there was never a corpus convention for
   this expression to violate.
4. **The two readings are numerically identical on every recorded row.** All
   six atoms in `tr-m-atom-via-transfer.witness.json` have `tr_M_atom > 0` and
   `tr_M_free > 0`, so `|F| - |A| == F - A` exactly (checked at 60-digit
   Decimal precision). The failure scenario I named -- "if either trace crosses
   zero" -- does not occur on this path.

**What went wrong in the reasoning.** I inferred a defect from the SHAPE of the
expression without reading the field name it feeds or grepping its consumers --
the corpus-grep failure AGENTS.md exists to prevent, committed in a PR body
while writing about being careful. Two of the four checks above are one grep
each and would have stopped it.

A caution for whoever reads the numbers above: the first pass of check 4
reported "not identical" for D, T and 3He. That was a harness artifact --
Python's `Decimal.__abs__` applies context rounding, and the default 28-digit
context was below the 30 recorded digits. At `prec = 60` all six are identical.
A rounding context is not a finding.

Nothing here is a live item. There is no work outstanding on line 194.
