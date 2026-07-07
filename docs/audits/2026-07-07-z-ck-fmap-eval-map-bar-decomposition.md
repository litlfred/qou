# Archimedean evaluation map — bar-decomposition: the standing reading, realized

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (the archimedean evaluation)
· **Follows:** the [B3-U obstruction](2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md)
(naive u-re-expansion excluded ⇒ the `c_k` come from the archimedean evaluation)
· **Tier:** proved-lean + symbolic-exact · **No `c_k` value, no wiring, no tier change.**

## Result

The B3-U obstruction localized the remaining keystone to the **archimedean
evaluation map** — the Frobenius counit `ε` / Markov trace `tr_M` on the `N=0`
nucleon Hecke normal-form difference (`QOU.Interactions.QBetaCounitTrace`,
Lean-proved, `q-beta` net-ansatz):

```
ε(n−p)    = h²/2 − h        (identity term h²/2, unweighted crossing −h)
tr_M(n−p) = h²/2 − h·z      (crossing weighted by the Markov loop z)
```

with `h = q − q⁻¹` the Hecke parameter and `z = √q/(1+q)` the Markov loop
parameter. The bar involution `q ↦ q⁻¹` acts as **`h ↦ −h`** (`h` is bar-ODD)
and fixes `z` (`z` is bar-EVEN, KC13). So the evaluation map splits **exactly**:

| channel | term | bar-parity | role |
|---|---|---|---|
| **even** | `h²/2` (identity `γ = 𝟙`) | bar-EVEN | shadow / mass channel |
| **odd** | `−h` (`ε`) resp. `−h·z` (`tr_M`, the Markov loop/crossing) | bar-ODD | **the odd channel** |

Probe [`qbeta_eval_map_bar_decomposition_probe.py`](../../computations/qbeta/qbeta_eval_map_bar_decomposition_probe.py)
→ [witness](../../computations/qbeta/qbeta-eval-map-bar-decomposition.witness.json)
(8/8, exact). Lean (sorry-free, `lean`-direct exit 0):
[`epsNP_decomp` / `epsNP_bar_image` / `trMNP_decomp` / `trMNP_bar_image`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean).

## Why this matters

This is the **archimedean realization of the standing reading**
(owner-granted 2026-07-07; registry KC6/KC10: parity gates test the bar-odd
part, shadow gates the bar-even part). On the actual evaluation map:

- the **even identity term `h²/2` carries the shadow** (the mass / magnitude
  channel — consistent with `c_2 = −1` being the identity-term rung);
- the **odd channel is the Markov loop/crossing term `−h·z`** — so the bar-odd
  carrier `D(q)` (KC15) feeds the observable *through the crossing term*, not
  the identity term.

It bridges the two halves the B3-U obstruction separated: the fibre parity data
(KC13–KC16) and the observable `c_k`. The evaluation map does **not** re-expand
a fibre element in `u` (excluded, KC17); it applies the counit/trace pairing,
whose bar-decomposition is clean and now proved. The remaining keystone is
sharpened once more: derive the **higher-order** crossing weight (beyond the
leading `z`) whose odd part reproduces the `c_3 → −2` shadow's odd-channel
signature — a bounded, well-posed target on the trace side, no longer a search
for a `u`-series.

## Scope / discipline

This is a **structural identification of the channel decomposition**, not a
`c_k` value. `c_2 = −1` remains the one derived rung; `c_3+` remain open
(precision floor). Nothing is wired; no tier changes. The leading result
(`ε = h²/2 − h`, phase `cos(α_eff) = τ_M(M_β)`) was already in the corpus
(net-ansatz / counit-transition); this audit adds the **bar-decomposition** and
its identification with the standing reading.

## Cross-references

- Evaluation map (Lean): [`qbeta_counit_vs_trace.lean`](../../content/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean)
- B3-U obstruction: [`2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md`](2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md)
- Standing reading: registry [KC6/KC10](../coordination/ck-dk-canonical-registry.md §9)
- `z` bar-even: `QOU.QBeta.z_bar_invariant` (KC13)
- Net-ansatz origin: [`2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md`](2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md)
