# The c₃ bar-odd S-leak: exact target + Φ_b (modular-double) diagnosis

**Date:** 2026-07-11 · **Axis:** Q_β c₃ (bar-odd part) · **Tier:** measurement + structural diagnosis.
**No c_k wired; registry untouched; flip-flop guard §8 respected.**
**Probe:** [`computations/qbeta/qbeta_c3_barodd_sleak_probe.py`](../../computations/qbeta/qbeta_c3_barodd_sleak_probe.py).

Builds on the parity-chirality split of c₃ (PR #3474/#3487) and the
[2026-07-11 keystone re-scope](2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md):
c₃ = **bar-EVEN** `−Vol(4₁)` (solved, real, amphichiral 4₁ face, anchor-stable)
+ **bar-ODD** `S` (the CAL-2 S-leak, anchor-swinging, **Subgoal-2**). This audit
pins `S` numerically and diagnoses which object it is.

## The exact open target — S at both anchors

`S = c₃ + Vol(4₁)` (`Vol(4₁) = 2.02988321`), from the committed anchor-blind
witness (`c3_muon`, `c3_proton`, 50 dps):

| anchor | c₃ | **S = c₃ + Vol(4₁)** |
|--------|-----|------|
| muon | −2.02020024 | **+0.00968298** |
| proton | −2.06934258 | **−0.03945936** |

Any future derivation of the c₃ bar-odd part **must reproduce these two
numbers** (this is the concrete Subgoal-2 target).

## New observation — S sign-flips ⇒ a zero-crossing between the anchors

`S(muon) > 0 > S(proton)` across two anchors that are both `q₀ > 1` and differ
only at ~10⁻⁸. So **S passes through zero** at a substrate value `q*` roughly
20% of the way from the muon to the proton anchor — a `q*` where `c₃ = −Vol(4₁)`
**exactly** (purely bar-even, S vanishes). `S(proton)/S(muon) ≈ −4.08`.

The anchor-blind claim formula's odd part `u − (10/3)u²` is a **fixed** `+0.00828`
at both anchors, so it **structurally cannot** produce the sign flip — which is
exactly why it near-matches muon (+0.0097) and misses proton (−0.0394). The flip
is the fingerprint of a genuinely anchor-dependent (fibre-level, bar-odd) object,
not a real anchor-blind constant.

## Diagnosis — S is the Φ_b (modular-double) decay face, not the compact Φ_q

The compact quantum dilogarithm `Φ_q(x) = ∏(1+q^{2n+1}x)^{-1}`
([`_phi_q_util.py`](../../computations/_phi_q_util.py); formalized this session in
[`QOU.MathlibExt.QuantumDilogarithm`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QuantumDilogarithm.lean)
+ [`QuantumDilogarithmInfinite`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QuantumDilogarithmInfinite.lean))
is — per its own header — the **real / mass / bar-even** face. The **decay /
bar-odd** face requires the **missing `b^{-1}` modular-dual factor**, i.e. the
Faddeev **non-compact `Φ_b`** (modular double; kernel `sinh(zb)sinh(zb^{-1})`).

This lines up the two parts of c₃ with the two dilogarithm faces:

| part of c₃ | face | dilog object | this session |
|------------|------|--------------|--------------|
| **bar-EVEN** `−Vol(4₁)` | mass / real | **compact `Φ_q`** | **T1 — built** (`QuantumDilogarithm{,Infinite}`) |
| **bar-ODD** `S` (open) | decay / CAL-2 | **`Φ_b` modular double** | **T3 — deferred** ([q-dilog workplan](../workplans/2026-07-11-q-dilog-infinite-product.md)) |

So the c₃ S-leak is **structurally the T3 (Φ_b) object** I formalize-first
deferred — and the compact-Φ_q backbone I *did* build supplies only the bar-even
`−Vol(4₁)` part, **by design**. The sign-flip / zero-crossing is a `Φ_b`
fingerprint (a `sinh`-type modular-double evaluation), consistent with #3474's
"anchor-swinging bar-odd part (S, complex, Subgoal-2)".

## Why this is a useful, non-colliding contribution

- **It does not attempt a c₃ formula** (Subgoal-2; the real-q family is refuted,
  the search space is negative-littered, and the ζ₄ f-map axis is owned by the
  live #3429). It **characterizes the target** and **names the object** (`Φ_b`).
- It grounds the diagnosis in this session's now-merged compact-`Φ_q`
  formalization, making the T1-vs-T3 boundary the operative statement: **closing
  Q_β's c₃ = building the `Φ_b` modular-double decay face**, which the compact
  backbone provably does not supply.

## Cross-references
- Parity split: [`2026-07-07-parity-chirality-dictionary-closed.md`](2026-07-07-parity-chirality-dictionary-closed.md) (#3487), #3474.
- Re-scope: [`2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md`](2026-07-11-qbeta-c3-keystone-rescope-anchor-blind.md).
- Registry: [`ck-dk-canonical-registry.md` §3](../coordination/ck-dk-canonical-registry.md).
- Live sibling (do not collide): PR #3429 (ζ₄ f-map power-class pincer).
