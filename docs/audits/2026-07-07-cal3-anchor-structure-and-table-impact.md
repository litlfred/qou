# CAL-3 anchoring of c_3 — provable structure + (null) impact on the mass/binding tables

**Date:** 2026-07-07 · **Axis:** Q_β c_3 / z→c_k f-map keystone · **Tier:** proved-lean + audit
· **Discipline:** no fit, no c_k value, nothing wired, no tier change. "Sorry-free ≠ derived" (registry §1) applies throughout.

## What "CAL-3-anchoring c_3" is

`c_3` is a **near-match, not a derivation** (registry §3): value ≈ −2, but a 2.42 %
cross-anchor swing. Its odd channel factors as

    c_3^odd  =  κ_(2,1)(q_0) · S ,

a **derived, pure-q, bar-odd carrier** `κ_(2,1)(q) = (q−1)³(q+1)/q²`
(`QOU.QBeta.kappa21_bar_odd`) times a **single archimedean scalar `S`**. Live numbers:

| anchor | q₀ | κ_(2,1)(q₀) | c_3 | S = c_3/κ |
|---|---|---|---|---|
| proton | 1.109978595 | 0.00227810 | −2.06934 | **−908.36** |
| muon | 1.109975 | 0.00227789 | −2.02019 | **−886.87** |

The carrier `κ` is anchor-rigid (swing `9.3×10⁻⁵`); **the entire c_3 swing (2.42 %)
lives in `S`** (`S_p/S_μ = 1.0242`). So the un-derived content of c_3 is one real
number, `S ≈ −900` — "the single archimedean leak."

## What is Lean-proved (the scaffolding — NOT the value)

[`QOU/QBeta/CAL3AnchorStructure.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CAL3AnchorStructure.lean),
sorry-free, `lean`-direct exit 0:

| lemma | content |
|---|---|
| `kappa21_ne_zero` | the carrier is nonzero away from `q ∈ {0,1,−1}` ⇒ `S := c_3^odd/κ` is well-defined |
| `c3odd_bar_odd_of_factor` | `κ·S` (κ bar-odd, S bar-fixed) is bar-odd: the channel inherits parity from the *carrier*, not from `S` (standing reading KC6/KC10) |
| `c3_swing_factorization` | `(κa·Sa)/(κb·Sb) = (κa/κb)·(Sa/Sb)`: the swing separates into a pure-q ratio × the scalar ratio |
| `S_welldefined` | `κ·(c_3^odd/κ) = c_3^odd` (defining ratio well-formed) |

**These are theorems about the *shape* of the anchor, not about c_3's value.** None
makes c_3 derived or anchor-stable. The one thing that would matter — the
identification `S = g(𝔇_π)` (that `S` is fixed by the CAL-3 pion/meson datum rather
than read off Q_β) — is **deliberately NOT axiomatised** as a Lean class: a class
`S = g 𝔇_π` is vacuously satisfiable (any `S` is `g(𝔇_π)` for some `g`), so
formalising it would be laundering, not proof. The real open content is cross-anchor
rigidity of a *single categorical* `g`, which no Lean scaffold establishes.

## Impact on the mass and binding tables: **none**

Production-wiring audit (probe
[`qbeta_cal3_anchor_table_impact.py`](../../computations/qbeta/qbeta_cal3_anchor_table_impact.py),
5/5; source: `canonical_mass.py` builds `m_n = m_p + q_beta_kashiwara_n2_mev() + m_e`
— the **c_2/N2-level** Q_β):

| observable | uses Q_β? | uses c_3? | effect of CAL-3-anchoring c_3 |
|---|---|---|---|
| m_e, m_μ, m_π, m_p | no | **no** | none (CAL-1 / Vol(4₁) / CAL-3 scale / muon-anchored Hecke) |
| m_n, Δ_pn | yes | **no** | none in production (Q_β at c_2/N2 level) |
| Q_β | yes | **no** | *reclassify only if wired*: predicted → CAL-3-calibrated |
| binding B_AME | no | **no** | none (tr_M Jones-Markov trace, weak-sector Q_β not involved) |

**No table row moves.** c_3 is not wired anywhere; the mass table has no Q_β
dependence at all, m_n/Δ_pn use the c_2-level Q_β, and binding uses `tr_M` (strong
sector, disjoint from the weak-sector Q_β). Proving structural lemmas about the
factorization changes zero entries — the standard "sorry-free ≠ derived" separation.

**If** c_3 were ever wired into Q_β, that would be a **calibration**, not a
prediction: Q_β/m_n/Δ_pn would reclassify from "predicted (failing 100×)" to
"CAL-3-anchored," which *removes* them from the predicted-observable 100× count
rather than improving the accuracy score. Anchoring buys a cleaner *bookkeeping*
story (the swing is explained as one calibrated scalar), not a table improvement.

## Bottom line

We Lean-proved the anchor's **scaffolding** (carrier well-defined, odd-channel
parity, swing algebra), not the anchor. c_3's value stays empirical and unwired;
the mass/binding tables are unchanged. The single open object is the scalar `S ≈
−900` and whether it descends from the CAL-3 datum — the same irreducibly-archimedean
input the whole f-map arc localized.

## Cross-references

- Lean: [`CAL3AnchorStructure.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CAL3AnchorStructure.lean); carrier parity `QOU.QBeta.kappa21_bar_odd` (ZBarParity §3)
- Factorization origin: [2026-06-13 heat f-map audit](2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md) §1
- Eval-map / odd channel: [KC18 audit](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- Wiring: `computations/canonical_mass.py`; registry [§3 / §9](../coordination/ck-dk-canonical-registry.md)
