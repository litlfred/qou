# Plan G — Retire SnapPy `Vol_hyp(K)` shortcut for ²H / ³H / ³He / electron

**Status:** design pass. No code changes yet.
**Target:** four atomic-link entries in
[`computations/low-isotope-mass-table.witness.json`](../../computations/low-isotope-mass-table.witness.json)
that use the `manual-historical-volume-match` shortcut:

| Entry | Strategy tag | Census braid | SnapPy `Vol_hyp` used today |
|-------|--------------|--------------|-----------------------------|
| ²H | `census:6_2,ρ=m_e` | knot `6_2` | `VOL_6_2 = 4.40083` |
| ³H | `census:8_11,ρ=2m_e` | knot `8_11` | `VOL_8_11 = 8.28632` |
| ³He | `census:Borromean,ρ=2m_e` | Borromean rings | `VOL_BORROMEAN = 8 G_Catalan ≈ 7.32772` |
| electron | torus knot `T(2,3)` | trefoil | not in table — currently elided |

Each entry computes `B_pred = ρ · Vol(K)` instead of the symbolic
Markov trace `tr_M(T_w)|_{q_0}`.  The master proposition specifies
the Markov-trace path; the SnapPy volume is acknowledged in
`atom_mass_archimedean.py` as an "archimedean observation".

## Goal

For each of the four entries above, produce a symbolic
`tr_M(T_w)` expression in `q`, evaluate it at `q_0` to ≥ 50 dps
via mpmath, multiply by the dimensional carrier (the same `ρ`
prefactor in mass units), and replace the SnapPy `Vol_hyp` call
with the symbolic value.  Compare against AME-derived B values.

## Existing infrastructure — what we already have

| Asset | Path | Coverage | Gap |
|-------|------|----------|-----|
| Symbolic Markov-trace recursion | `computations/markov/markov_trace_canonical.py` | Implements canonical tr_M with cyclicity, Markov II, Hecke quadratic.  Symbolic in q. | Returns sympy expression; needs harness to feed it the four target braid words and evaluate at `q_0` mpf. |
| Memoised q-MN characters | `computations/q_mn_recursive_memoized.py` | Halverson–Ram broken-strip rule, all partitions/cycle types up to large n. | Already gives χ_λ(β) symbolically; not yet wired to ²H/³H/³He braid words. |
| Wenzl-bridge `y_λ` extension | `computations/y_lambda_wenzl_bridge_extended.py` | Symbolic `y_λ` for n=2..12 via Schur principal specialisation. | Provides the *weights*; combined with χ_λ they form `tr_M = Σ y_λ χ_λ / d_λ` (or similar) — needs explicit assembler. |
| Hoefsmit witness (k=3..11) | `hoefsmit_witness.py` + `hoefsmit_witness.json` | Pre-computed χ(4₁), χ(B³) at every λ for k=3..11. | Lacks `χ(8_11)` for ³H; lacks `χ(T(2,3))` for the electron. |
| MPFR seminormal kernel | `tools/hecke-engine/src/seminormal_mpfr.rs` | Arbitrary-precision χ_λ(β) evaluator. | Already callable from Python via `pyhecke_native`. |

## What's missing — the four braid words and their tr_M

We need to author and commit:

1. **²H = 6_2** as a Markov braid.  6_2 is the closure of
   `σ_1 σ_2^{-1} σ_1 σ_2^{-1} σ_1 σ_2^{-1}` in B_3 — verify
   against Rolfsen / SnapPy database.  Resulting word ∈ H_3(q).
2. **³H = 8_11** as a Markov braid.  8_11 is realised on
   B_4 with braid word from the Knot Atlas.  Resulting word ∈ H_4(q).
3. **³He = Borromean rings (L6a4 = 6³_2)** as a Markov closure
   of a 3-component link braid in B_3 (`(σ_1 σ_2^{-1})^3`).
4. **electron = T(2,3)** = trefoil (3_1) on B_2 (`σ_1^3`),
   already canonical; tr_M(σ_1^3) = h·z² + z (closed form,
   already in `markov_trace_canonical.py` as a unit test value).

For each braid word, we need:

- The exact `tr_M(T_w)` rational function in `q` (sympy).
- Its evaluation at `q_0` at ≥ 50 dps (mpmath).
- A side-by-side comparison with the SnapPy `Vol_hyp / (something)`
  used today, to verify dimensional consistency.

## New emitter required

A single new script
`computations/tr_m_symbolic_low_isotope.py` that:

1. Imports `markov_trace_canonical.tr_M_word`.
2. Hard-codes the four braid words above (with literature
   citations to Rolfsen / Knot Atlas — all are in
   `content/schema/references.ts` already as `[rolfsen1976]` and
   `[knotatlas]`).
3. For each: emits the sympy expression, the mpf value at `q_0`,
   the derivative `d/dq tr_M` at `q_0` (for error budget), and
   the AME-derived target.
4. Writes
   `computations/tr-m-symbolic-low-isotope.witness.json`
   with `precision: "mpfr_50dps"`.

## tr_M outputs we need (concrete table)

| Braid | Word | Closure | tr_M(T_w) symbolic | tr_M(T_w) at q₀ (target dps) | AME comparison |
|-------|------|---------|--------------------|-------------------------------|-----------------|
| `(σ_1 σ_2^{-1})^3` | B_3 | knot 6_2 | rational in q | TBD @ 50 dps | matches `M_E·Vol(6_2)` to ≥ 6 sig figs |
| 8_11 word | B_4 | knot 8_11 | rational in q | TBD @ 50 dps | matches `2 M_E·Vol(8_11)` to ≥ 6 sig figs |
| `(σ_1 σ_2^{-1})^3` | B_3 (link) | Borromean L6a4 | rational in q | TBD @ 50 dps | matches `2 M_E·8 G_Catalan` to ≥ 6 sig figs |
| `σ_1^3` | B_2 | trefoil 3_1 | `h z² + z` | `(q − q⁻¹)·z(q)² + z(q)` @ q₀ | electron mass placeholder |

(The first and third entries share the same word but different
closure conventions — knot-closure vs link-closure — and tr_M
distinguishes them via the strand-component structure.)

## Effort estimate

| Phase | Person-days |
|-------|-------------|
| Author four braid words; verify against knot atlas | 1 |
| Symbolic tr_M assembly; cross-check with q-MN witness | 1 |
| 50 dps mpmath evaluator + golden witness JSON | 1 |
| Wire into `low_isotope_binding_sweep.py` (replace VOL_* constants with `tr_M_at_q0_mpf` lookups) | 1 |
| Update mass table; rerun against AME | 0.5 |
| Documentation: replace strategy tag from `census:6_2,ρ=m_e` to `tr_M:6_2,ρ=m_e` and update prose blocks | 0.5 |
| **Total** | **5 days** |

## Smoke test / exit criterion

1. The new witness
   `tr-m-symbolic-low-isotope.witness.json` exists with all four
   entries, each carrying `tr_M_symbolic` (sympy str),
   `tr_M_at_q0_mpf_str` (50 dps decimal), and
   `agreement_with_snappy_vol` (a ratio expected to equal the
   stated `ρ` prefactor to ≥ 4 sig figs).
2. `low-isotope-mass-table.witness.json` is regenerated; the
   `strategy` tags for ²H/³H/³He change from `census:*` to
   `tr_M:*`; the `B_pred_MeV` values change by < 1 % (we expect
   the SnapPy values to be approximately correct empirically).
3. The methodology field of the underlying SDP certificate
   (`tools/hecke-engine/certificate-2h.json` etc.) flips from
   `manual-historical-volume-match` to `principled-derivation`.

## First concrete step

Pick the easiest: the electron / trefoil.  In a fresh script
`tr_m_trefoil_witness.py`:

```python
from markov_trace_canonical import tr_M_word
import sympy as sp
q = sp.symbols("q", positive=True)
h = q - 1/q
z = 1/(sp.sqrt(q) + 1/sp.sqrt(q))
expr = tr_M_word((1, 1, 1), n=2, z=z, h=h)
print(sp.simplify(expr))  # should be h*z**2 + z
```

Verify the closed form matches the expected `h z² + z` from
`markov_trace_canonical.py`'s docstring — this validates the
toolchain end-to-end on the simplest case before we tackle the
larger braids.

## Out of scope

- Plan F (50 dps everywhere) — this plan can run before or
  after Plan F; if before, the witness uses f64 evaluation of
  the symbolic tr_M and gets upgraded to mpmath later.
- Plan H (ρ derivation from Wedderburn) — the dimensional `ρ`
  prefactor stays hand-picked here; Plan H derives it.

## Risk register

- **R1.** `markov_trace_canonical.tr_M_word` is recursive with
  `max_depth=200`.  8_11 has 8 crossings on 4 strands; the
  recursion may exceed the current depth limit.  Mitigation:
  raise to 1000; also add a memoisation layer (current code
  re-evaluates sub-words).
- **R2.** Knot 8_11 has a non-unique braid word; different
  literature sources give different reduced words.  These give
  the *same* `tr_M` (cyclic invariant) but verification is
  load-bearing.  Mitigation: cross-validate by computing tr_M
  on at least two distinct words for 8_11.
- **R3.** The "²H = 6_2" assignment itself is an empirical
  fit, not a derivation.  This plan does not derive that
  assignment — it only replaces the SnapPy `Vol_hyp` lookup
  for the chosen knot with a symbolic `tr_M`.  The "why 6_2?"
  question is parked for a separate plan.
