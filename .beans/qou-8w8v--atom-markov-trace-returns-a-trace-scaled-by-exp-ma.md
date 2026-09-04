---
# qou-8w8v
title: atom_markov_trace returns a trace scaled by exp(-max_ln) and DISCARDS max_ln, so its caller subtracts two differently-scaled quantities
status: completed
type: bug
priority: normal
created_at: 2026-09-03T20:28:03Z
updated_at: 2026-09-04T21:15:31Z
---

Found while verifying my own change under bean `qou-uiut`, not by looking for
it. The Rust path masks it; the pure-Python fallback still has it.

## The defect

`hecke_core_legacy.atom_markov_trace` recombines per-partition characters as

    max_ln = max(log_norm over partitions)
    chi_eff = chi_q * exp(log_norm - max_ln)
    trace  += w_lambda * chi_eff / d_lambda

so what it returns is the true Markov trace multiplied by `exp(-max_ln)` — and
**`max_ln` is not returned**, so no caller can undo it.

Its only consumer subtracts two such values:

    atom_tr = atom_markov_trace(Z, N, k_cap, include_inter=True)
    free_tr = atom_markov_trace(Z, N, k_cap, include_inter=False)
    return E_0_CALIBRATION_MEV * (abs(free_tr) - abs(atom_tr))
                                 # hecke_core_legacy.binding_from_frobenius_pairing

Two SEPARATE calls. Each computes its own `max_ln` over its own chain
(`include_inter` differs, so the log_norms differ, so the maxima differ). The
subtraction is therefore between quantities on two different scales, and the
result is not `E_0 * (|tr_M(W_free)| - |tr_M(W_atom)|)` — which is the formula
the function documents and the derivation requires.

## The sibling function shows the correct pattern

`atom_frobenius_norm_sq`, twelve lines below, does the same rescaling and
**returns `(norm_sq, per, max_ln)`** — it hands the scale factor back so a
caller can un-scale. `atom_markov_trace` returns a bare number. The right shape
was already in the file.

## Why it is not currently biting

`log_norm` is only non-zero once a running product exceeds 1e80, which happens
for large-dim partitions at high A. And since bean `qou-uiut` the default path
is the Rust kernel, which returns `log_norm = 0` by construction (MPFR's
exponent range makes the rescaling unnecessary) — so `max_ln = 0`, no scaling
is applied, and the subtraction is valid.

**The pure-Python fallback (`use_rust=False`, or any environment without
`pyhecke_native`) still has the defect.** That path is not exotic: the wheel is
ephemeral and dies with the container, so a fresh session that skips
`scripts/build-pyhecke-native.sh` runs on it.

## Measured

Not directly, and the reason matters. `log_norm` stays 0 for every case cheap
enough to run both ways — measured at A=28 with a dim-6 partition it is still
0.0 — and the cases where it is non-zero are exactly the ones the pure-Python
path cannot finish. So this is established from the code's structure plus the
sibling function's contrasting signature, NOT from a numerical demonstration.

What IS measured: `atom_markov_trace` agrees between the two paths to ~1e-49
at A = 2, 3, 4 in both `include_inter` conventions, pinned in
`tests/test_unified_correction_rust_parity.py`. That is the log_norm = 0
regime, i.e. precisely where the defect is inert.

## Fix

- [ ] Either return `max_ln` alongside the trace (matching
      `atom_frobenius_norm_sq`) and make `binding_from_frobenius_pairing`
      bring both onto a common scale before subtracting, or drop the
      rescaling from `atom_markov_trace` entirely — mpf has the range, which
      is why the Rust path needs no rescaling at all.
- [ ] Dropping it is probably right, but it changes pure-Python results at
      high A. Do not land it without deciding whether any committed witness
      was produced on that path.
- [x] Checked `atom_frobenius_norm_sq`'s callers. **They do not use it.**


## Update — the sibling is no better in practice

I cited `atom_frobenius_norm_sq` as showing the correct pattern because it
returns `(norm_sq, per, max_ln)` rather than a bare number. Checked its
callers: there is exactly one, and it discards the factor.

    computations/hecke_core_legacy.py:2614
        norm_sq, _, _ = atom_frobenius_norm_sq(Z, N, k_cap, include_inter=False)
        return norm_sq
    # inside free_nucleon_frobenius_norm_sq

So `free_nucleon_frobenius_norm_sq` returns a norm-squared scaled by
`exp(-2*max_ln)` and presents it as the norm. Returning the scale factor is
not the same as anyone applying it — the right SHAPE was in the file, and the
one caller threw it away.

That makes this two instances of one defect rather than a defect and a good
example:

    atom_markov_trace            scale discarded at the SOURCE (never returned)
    atom_frobenius_norm_sq       scale discarded at the CALL SITE

Both are inert while `log_norm` is 0, which the Rust path guarantees and every
cheap case satisfies. Both bite on the pure-Python path at high A.

Note `free_nucleon_frobenius_norm_sq`'s own docstring says the intended value
is `||W_free||^2 = sum_lambda w_lambda = 1` — an identity limit. If the
intended answer is exactly 1, a silently rescaled return is easy to miss,
because a wrong value still looks like a plausible number near 1. Worth
checking what it actually returns as part of this fix.

## 2026-09-04 — FIXED, and the "worth checking" line turned up a second defect

### The fix

Both instances corrected at the point where the scale was lost:

* `atom_markov_trace` now returns `trace * _mp.exp(max_ln)`. The shifted
  accumulation stays — it is a stability device and still worth having; only
  the return was wrong.
* `free_nucleon_frobenius_norm_sq` now applies the third element instead of
  discarding it: `norm_sq * _mp.exp(2 * max_ln)`. The factor is uniform across
  the sum (every term carries `(chi*exp(ln-max_ln))^2`), so it survives.
* `per[...]['chi_rescaled']` deliberately left in the shifted domain: it exists
  to compare magnitudes across partitions, which is what a common exponent is
  for.

Measured rather than asserted — `max_ln = 0.0` for D, T and He3 on the default
Rust path, so both new factors are exactly 1 and `norm_sq_raw == free_norm_sq`
to every digit. **No published value moves.** The correction bites only on the
pure-Python fallback at high A, which is where it was wrong. 64 tests pass,
including the 19 Rust/Python parity tests.

### The second defect this exposed

The last line of this bean asked what `free_nucleon_frobenius_norm_sq`
actually returns, given its docstring claims the identity limit
`||W_free||^2 = sum_lambda w_lambda = 1`. Measured:

    D    1.988392799
    T    0.991042245
    He3  0.869097004

It is **not 1**, and the three do not agree with each other. D is off by
essentially a factor of two.

This is NOT the rescaling bug — `max_ln = 0` throughout, so the scaling was
inert for these atoms and the numbers above are the same before and after
today's fix. It is a separate, larger problem with what the function computes:
it evaluates `sum_lambda w_lambda * (chi_lambda(W_free)/d_lambda)^2`, and that
equals `sum_lambda w_lambda = 1` only if `chi_lambda(W_free)/d_lambda = 1` for
every lambda — i.e. only if W_free is the IDENTITY braid. It is not: "free"
removes the inter-nucleon crossings but keeps the intra-nucleon ones. The
docstring's own "TODO: proper tensor-product decomposition via H_3(q)^A
restriction" is exactly this gap, and the "for now, use the empirical simpler
form ... = 1" it settles for is not what the code does either.

The warning written in this bean was right about the failure mode: T at 0.991
and He3 at 0.869 both look like plausible numbers near 1 and would pass a
casual glance. D at 1.988 is what makes it unmissable.

Filed separately as **qou-fop2** — it needs the tensor-product decomposition,
not a scaling correction, so it does not belong in this bean's fix.
