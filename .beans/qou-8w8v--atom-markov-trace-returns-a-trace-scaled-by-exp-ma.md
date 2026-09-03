---
# qou-8w8v
title: atom_markov_trace returns a trace scaled by exp(-max_ln) and DISCARDS max_ln, so its caller subtracts two differently-scaled quantities
status: todo
type: bug
created_at: 2026-09-03T20:28:03Z
updated_at: 2026-09-03T20:28:03Z
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
