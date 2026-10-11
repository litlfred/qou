# v9 `tr_markov_*` (retired from main, 2026-10-11)

Owner ruling on issue litlfred/qou#7685, bean `qou-m7py`: delete the field from `main`, keep the old version here, and make v9 compute the real trace.

## What the field computed

    tr_markov_f64 = (1/2^pn) · Σ_w c_w · z^len(w),   z = 1/(t + 1/t),  t = q^{1/2}

where `w` runs over v9's normal-form words, including words absorbed by its Pauli strip. That is wrong in two ways:

1. **z is convention C.** That convention was excised on 2026-08-15; convention D is `z = q³/(q²+1)`.
2. **A sum of z^len(w) is not a Markov trace.** The Ocneanu trace satisfies `tr(x σ_{n−1} y) = z·tr(xy)`, so for example `tr(σ₀σ₁σ₀) = h z² + z`, not `z³`. The two agree only on words that use each generator at most once.

`tr_markov_cleared` and `tr_markov_denom_power` are the same quantity in a different form: the sum is multiplied through by `(t+t⁻¹)^L`, with `L` the maximum word length.

## Files

- `excised.rs`: the removed Rust code, verbatim, from `tools/hecke-engine/src/bin/v9.rs` and `src/certificate.rs`.
- `values.json`: every certificate's `tr_markov_*` values, in two versions:
  - as committed before the 2026-10-11 regeneration (34 of those certificates used the pre-fix crossing `t⁴σ + t − t³`);
  - after the regeneration with the current crossing (commit `bd6e0dcb86`).

## Replacement

On `main`, v9 emits `tr_markov_d`: the exact Ocneanu trace at convention D, computed when the element is the full crossing product. It is cross-checked against `computations/probes/v9_markov_trace_convention_d_probe.py`.
