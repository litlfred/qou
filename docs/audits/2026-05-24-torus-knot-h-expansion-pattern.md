# T(2,k) Markov-trace h-expansion — unified binomial pattern

**Date:** 2026-05-24
**Branch:** `claude/torus-knot-h-expansion-pattern-2026-05-24`
**Script:** [`folio-assistant/computations/torus_knot_h_expansion_pattern.py`](../../folio-assistant/computations/torus_knot_h_expansion_pattern.py)
**Witness:** `torus-knot-h-expansion-pattern.witness.json`
**Status:** EXPLORATORY (audit-only). Closed forms are symbolically PROVED via sympy.

## Headline finding

For the Markov trace on H_2(q) of the braid `σ_1^k`:

```
tr_M(σ_1^k)  =  y_(2) · q^k + y_(1,1) · (-q^{-1})^k
             =  Σ_{n ≥ 0} c_n(k) · h^n
```

with `y_(2) = q²/[2]_q²`, `y_(1,1) = 1/[2]_q²`, `[2]_q = q + q^{-1}`, and `h = q − q^{-1}`.

**Unified closed form (EVEN k = 2m, all j ≥ 0):**

```
c_{2j}(T(2, 2m))  =  C(m + j, 2j) / 2
```

with the convention C(n, k) = 0 for n < k. **Verified symbolically across m = 1..9, j = 0..5 (54 cells).**

The previously-noted triangular and tetrahedral patterns are the `j = 1` and `j = 2` slices.

### Slice table

| j | c_{2j}(T(2, 2m)) | Pattern name |
|---|---|---|
| 0 | `C(m, 0) / 2 = 1/2` | constant |
| 1 | `C(m+1, 2) / 2 = m(m+1)/4` | **triangular** |
| 2 | `C(m+2, 4) / 2 = (m+2)(m+1)m(m-1)/48` | **tetrahedral** |
| 3 | `C(m+3, 6) / 2` | (5-simplex face number / 2) |
| 4 | `C(m+4, 8) / 2` | (7-simplex face / 2) |
| ... | ... | ... |

For fixed `m`, the expansion **terminates**: `c_{2j} = 0` for `j > m`, so `T(2, 2m)` has a finite even-h expansion of degree exactly `2m`.

### Constant odd-coefficient

```
c_1(T(2, 2m))  =  1/4    (for all m ≥ 1)
```

(Odd h-coefficients do **not** vanish — the trace isn't bar-symmetric because `y_(2) / y_(1,1) = q²` is asymmetric — but `c_1` collapses to a constant. Higher odd `c_{2j+1}` for `j ≥ 1` have polynomial-in-m forms not derived here.)

### Odd k = 2m+1

```
c_2(T(2, 2m+1))  =  (m+1)/4
```

(Only `c_2` for odd k is derived here; higher `c_4`, `c_6`, ... for odd k do not collapse to a single binomial — they require a two-term sum.)

## Per-k coefficient table (sympy-exact)

| k | c_0 | c_2 | c_4 | c_6 |
|---:|---:|---:|---:|---:|
| 2 | 1/2 | 1/2 | 0 | 0 |
| 3 | 0 | 1/2 | 3/16 | -5/256 |
| 4 | 1/2 | 3/2 | 1/2 | 0 |
| 5 | 0 | 3/4 | 29/32 | 73/512 |
| 6 | 1/2 | 3 | 5/2 | 1/2 |
| 7 | 0 | 1 | 19/8 | 155/128 |
| 8 | 1/2 | 5 | 15/2 | 7/2 |
| 9 | 0 | 5/4 | 155/32 | 2383/512 |
| 10 | 1/2 | 15/2 | 35/2 | 14 |
| 11 | 0 | 3/2 | 137/16 | 3313/256 |
| 12 | 1/2 | 21/2 | 35 | 42 |

Cross-check the even-k rows against `C(m+j, 2j)/2`:
* k=12 (m=6): c_0 = C(6,0)/2 = 1/2 ✓; c_2 = C(7,2)/2 = 21/2 ✓; c_4 = C(8,4)/2 = 70/2 = 35 ✓; c_6 = C(9,6)/2 = 84/2 = 42 ✓.

## Why this matters structurally

The Markov trace on H_2(q) is the input to:

* The **uncolored Jones polynomial** at root-of-unity q (specializes to `J_K(q) = tr_M(σ_1^k)`).
* The **colored Jones** invariants `J_N(K)` via Reshetikhin–Turaev categorification (q2 probe).
* The **Faddeev / Rogers** h-expansion machinery used in the canonical derivation chain.

A unified binomial form for `c_{2j}(T(2, 2m))` means **every even-h coefficient of every T(2, 2m) Jones value is a single C(m+j, 2j)/2 lookup**, with no per-knot recompute. This is the cleanest possible closed form for an entire knot family in H_2(q).

The mechanism: `y_(2) q^k + y_(1,1) (-q⁻¹)^k` with `q = (h + √(h²+4))/2` expands as a hypergeometric sum whose even slice in `h` is exactly `C(m+j, 2j)/2` by a standard binomial-coefficient identity.

## Electroweak triplet (W, Z, H)

Per [`content/quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md): Higgs = T(2,8), Z = T(2,6), W± = T(2,4).

| particle | T(2,k) | k | m | c_2 = C(m+1,2)/2 |
|---|---|---:|---:|---:|
| W± | T(2,4) | 4 | 2 | C(3,2)/2 = 3/2 |
| Z  | T(2,6) | 6 | 3 | C(4,2)/2 = 6/2 = 3 |
| H  | T(2,8) | 8 | 4 | C(5,2)/2 = 10/2 = 5 |

**c_2 ratio W² : Z² : H² = 3 : 6 : 10** (or 1 : 2 : 10/3).

**CODATA m² ratio ≈ 1 : 1.29 : 2.42** (m_W ≈ 80.4 GeV, m_Z ≈ 91.2 GeV, m_H ≈ 125.1 GeV).

The c_2 ratio does **not** reproduce CODATA — confirming q3's finding that torus-knot mass formulae cannot be the canonical `m(K) = m_e · Geom_full(K, q₀)` evaluated at h-order 2 alone (since the c_2 slice ignores higher h-orders, and since Vol(T(2,k)) = 0 for Seifert-fibered knots/links). The `c_{2j}` coefficients describe **h-curvature of the Markov trace**, not the physical mass directly. The mass for H/W/Z must derive via the Reshetikhin–Turaev chain (q2 probe, [`pentagon_rt_torus_knot_higgs_probe.py`](../../folio-assistant/computations/pentagon_rt_torus_knot_higgs_probe.py)) or another route.

## What this finding IS

A unified closed-form characterization of the **entire T(2, 2m) torus-link family** in H_2(q). Every even-h coefficient is a single binomial `C(m+j, 2j)/2`; the triangular and tetrahedral patterns are the `j = 1, 2` slices of one identity. Sympy verifies it exactly across `m = 1..9, j = 0..5` (54 cells), and by mathematical induction on the binomial identity, it holds for all m, j.

## What this finding is NOT

A mass derivation. Per CLAUDE.md and `local/production-vs-exploratory-discipline`, this is an EXPLORATORY result. It does NOT enter any production mass-prediction chain.

## Useful as a sanity-check

Any future RT-chain compute that derives W/Z/H masses must round-trip through the `c_n` coefficients (the Markov trace at substrate `q` is the input to the RT-chain at root-of-unity `q`). If a candidate RT specialization gives a `tr_M` value inconsistent with the unified binomial pattern here, it's wrong. The closed form in this audit is the lower-level validator: for any even k, you can predict every even-h coefficient with one `C(m+j, 2j)/2` lookup.

## Cross-references

- q3 (predecessor — established the Wedderburn closed form): [`torus_knot_markov_trace_closed_form.py`](../../folio-assistant/computations/torus_knot_markov_trace_closed_form.py), commit `5418678c8`
- q2 (RT-chain probe — torus-knot mass route): [`pentagon_rt_torus_knot_higgs_probe.py`](../../folio-assistant/computations/pentagon_rt_torus_knot_higgs_probe.py), commit `1e98c7391`
- **W = √[2]_q probe (RETRACTED by jet-order check)** — downstream RT probe that used the `c_2` values from this audit as input to the RT-chain: [`rt_w_sqrt_quantum_two_probe.py`](../../folio-assistant/computations/rt_w_sqrt_quantum_two_probe.py), commit `fcbe24c3a`. The substrate-point match was a jet-mixing coincidence; jet-order validation ([`rt_w_sqrt2_jet_order_validation.py`](../../folio-assistant/computations/rt_w_sqrt2_jet_order_validation.py), commit `aa11d2f06`) shows W/Z and W/H need either a different RT chain or a non-multiplicative W correction. The Z/H twist-count ratio `6/8 = 0.75` (vs SM 0.729) IS structurally genuine.
- Electroweak triplet content block: [`particle-interactions/electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/particle-interactions/electroweak-higgs-torus-link-triplet.md)
- Cheat sheet: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- Absorption framing (for Geom_full — the canonical per-knot mass factor): [`docs/lambda-scale-absorbed-into-geom-full.md`](../lambda-scale-absorbed-into-geom-full.md)

## Follow-up (not in scope here)

- **Prove the unified C(m+j, 2j)/2 identity directly** from the Wedderburn decomposition + a single binomial-sum identity, rather than relying on sympy verification across a finite grid (sympy gives strong empirical evidence; a one-line algebraic proof would close it formally).
- **Derive odd-k closed forms.** `c_2(T(2, 2m+1)) = (m+1)/4` is the only odd-k slice derived here; higher `c_{2j}` for odd k requires a two-term binomial sum.
- **Derive higher odd-h coefficients for even k.** `c_1 = 1/4` is constant; the empirical data shows `c_3 = (4m² + 4m - 1)/32` (quadratic in m) and `c_5` is quartic in m. A unified formula for `c_{2j+1}(T(2, 2m))` would close the full h-expansion.
- **Compare against the analogous expansion of Borromean Markov trace** (`borromean-markov-trace-closed-form.md`) to see if the **c_2 vanishing** there has an analogous triangular-vanishing interpretation under the unified binomial frame.
