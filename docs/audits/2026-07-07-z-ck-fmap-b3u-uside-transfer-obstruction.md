# B3-U — the u-side transfer obstruction: fibre parity does not descend to the c_k by re-expansion

**Date:** 2026-07-07 · **Bean:** `z61d` · **Axis:** z→c_k f-map keystone, I-B step B3-U
· **Gates pre-stated:** [scope doc §3](../scope/2026-07-07-z-ck-fmap-b3-uside-transfer-scope.md) (merged PR #3455, BEFORE this run)
· **Tier:** structural-exact (symbolic + one proved-lean lemma) · **Verdict:** OBSTRUCTION (scope-(a))

## Result

The three pre-stated gates (probe
[`qbeta_b3u_uside_transfer_probe.py`](../../computations/qbeta/qbeta_b3u_uside_transfer_probe.py)
→ [witness](../../computations/qbeta/qbeta-b3u-uside-transfer.witness.json),
4/4) show the fibre parity structure (KC15 `D(q)`, KC16 index-alternating
basis) **does not descend to the observable `c_k` via a naive re-expansion in
`u = b·ℏ_q²`**:

| gate | finding |
|---|---|
| **B3-U1** basis image | `bar(u) = q²·u` is a **scaling**, not KC16's inversion `q ↦ q⁻¹`. The `(u;u)_m` Habiro basis carries **no clean monomial bar-twist**: `P_m(q²u)/P_m(u)` **fails already at `m=1`** — `(q²u−1)/(u−1)`, a two-term ratio with no common factor since `q² ≠ 1` — verified `m=1..4` by the probe. |
| **B3-U2** per-rung twist | Overall-`F` bar-evenness (KC7) under `(q↦q⁻¹, u↦q²u)` would force `c_k(q⁻¹) = q^(−2k)·c_k(q)`. This is **contradicted by the derived `c_2 = −1`** (a bar-trivial real constant: `c_2(q⁻¹) = −1 ≠ −q⁻⁴`). |
| **B3-U3** carrier placement | `u ~ (q−1)²` vanishes to **even order 2** in `(q−1)`; a bar-odd carrier (e.g. `κ_(2,1)`, `D(q)`) vanishes to **odd order** at `q=1`. So bar-odd fibre content **cannot** be a real power series in `u` — parities mismatch. |

Lean handle (proved this tranche):
[`QOU.QBeta.uPow_bar_twist`](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean)
(§8) — `(t·u)^k = t^k·u^k`, so the `u`-monomial twist `q^(2k)` is
degree-dependent (a scaling), in contrast to the constant/Gauss-sum twists of
the `q`-side bases (KC12/KC16). Sorry-free, `lean`-direct exit 0.

## Reading (what it prunes, what it sharpens)

**Scope-(a).** The **naive re-expansion route is excluded** as the descent
mechanism — not the KC15/KC16 ingredients themselves. The `u→q²u` scaling
entangles the rung index with the twist (U1/U2), and `u`'s even-order-in-`(q−1)`
character blocks bar-odd content from mapping to real `u`-powers (U3). All three
are facets of the same fact: **`u` is a real archimedean composite, and the
fibre bar involution acts on it by a degree-dependent scaling, not an
involutive symmetry of the `u`-grading.**

**Where the odd channel actually enters.** The obstruction localizes the
remaining keystone precisely: the `c_k` are **fibre `q`-functions evaluated by
the archimedean map** (the τ-functor / Markov pairing at unit normalization —
owner ruling 2026-06-16, recorded in the c_k state-of-play synthesis §8), **not**
coefficients read off a fibre basis re-expansion. The bar-odd carrier `D(q)`
(KC15) and the index-alternating basis (KC16) are *inputs to that evaluation*,
not summands of a `u`-series. This is consistent with the AGENTS.md
"Im(q) at fibre vs observable level" wall: parity is a fibre notion, the `c_k`
are archimedean evaluations, and the two are bridged only by the evaluation
map — which is where the real work remains.

## Consequence for the next tranche

The productive B3 direction is **no longer** "re-expand the 4₁ element in the
`u`-ladder basis" (excluded here). It is: **exhibit the archimedean evaluation
map** (Markov pairing at `Vol=1`) that takes the fibre parity data (`D(q)`,
KC16) to the observed `c_k`, and check whether it reproduces `c_2 = −1`
(bar-even part) and the `c_3 → −2` shadow. That is the same object the
2026-06-16 owner note named; this obstruction is the formalize-first argument
that rules out the cheaper basis-re-expansion alternative before any such
evaluation is built.

## Cross-references

- Gates pre-stated: [scope §3](../scope/2026-07-07-z-ck-fmap-b3-uside-transfer-scope.md)
- Fibre parity inputs: registry [KC15/KC16](../coordination/ck-dk-canonical-registry.md §9)
- `u`-twist lemma: [`ZBarParity.lean` §8](../../content/quantum-observable-universe/lean/QOU/QBeta/ZBarParity.lean)
- Archimedean-evaluation framing: [c_k state-of-play synthesis §8](2026-06-10-qbeta-ck-state-of-play-synthesis.md)
- Fibre↔archimedean wall: AGENTS.md §"Im(q) at fibre vs observable level"
