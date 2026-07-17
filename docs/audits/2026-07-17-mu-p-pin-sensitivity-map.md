# μ–p root cause — pin-sensitivity map of the mass chain (W_λ is pin-blind)

**Date:** 2026-07-17 · **Axis:** L2 / μ–p substrate tension (m_p ~437×, m_μ ~964×) ·
**Tier:** assessment / diagnostic map. **No fit; nothing wired to production; the μ–p
tension is NOT resolved.** Scope-(a) per AGENTS.md refute-honestly.
**PR:** #3847 · **Producer:** `computations/mu_p_pin_sensitivity_map.py`
(witness `mu-p-pin-sensitivity-map.witness.json`) · **Lean:**
`QOU/BraidKnot/PinRobustnessOfRatios.lean` (sorry-free, lean-direct exit 0).

## Motivation

The Habiro-interpolation result (#3830) established that `W_λ(q₀)` is a **pin-robust
ratio** — its cross-pin swing is ~10⁴× smaller than the 11.5 ppb μ–p pin gap — so the
entire McKay / `W_λ` keystone route is **blind** to the μ–p tension. If the keystone
observable cannot see the tension, the m_p/m_μ discriminant must live in an
**absolute-scale** quantity, not a dimensionless ratio. This note maps *where* the pin
sensitivity actually lives and grades whether any corpus route can adjudicate the split.

## 1. The pin-sensitivity map (exact)

Relative pin-sensitivity `S(O) := d(log O)/d(log q₀)` of the canonical mass chain
(`ℏ_q = (q−1)/q`, `m_μ = m_e·Vol(4₁)/ℏ_q²`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`,
`m_p = 2(m_μ·F_Bor − 6m_e)`, `m_n = m_p + Q_β + m_e`, `W_λ = [mark λ]²_q/Σ_μ[mark μ]²_q`),
computed by 4th-order central finite difference against the **production** closed forms at
60 dps. Proton pin `q₀ = 1.10997858275…`; `1/(q₀−1) = 9.0927`.

| observable | class | S = dlogO/dlogq₀ | induced by 11.5 ppb pin gap |
|---|---|--:|--:|
| ℏ_q² = ((q−1)/q)² | anchor | **+18.185** = 2/(q−1) (exact) | 209 ppb |
| Vol(4₁) = 2Cl₂(π/3) | const | 0 (≈1e-40 noise) | ~0 |
| **m_μ = m_e·Vol(4₁)/ℏ_q²** | **ABS anchor** | **−18.185** = −2/(q−1) (exact) | 209 ppb |
| **m_p** | **ABS** | **−20.997** | 241 ppb |
| **m_n** | **ABS** | **−20.970** | 241 ppb |
| \|tr_M(β_Bor)\| | ratio | −0.0555 | 0.6 ppb |
| [3]_q! | ratio | +0.380 | 4.4 ppb |
| F_Bor | ratio | −2.675 | 31 ppb |
| Q_β | near-ratio | −2.632 | 30 ppb |
| **W_λ(mark 5)** | McKay ratio | **+0.185** | **2.1 ppb** |
| W_λ(mark 2) | McKay ratio | −1.246 | 14 ppb |
| **m_p/m_μ** | RATIO | **−2.812** | 32 ppb |
| **m_n/m_p** | RATIO | **+0.027** | **0.3 ppb** |
| m_μ/m_e | (m_e fixed) | −18.185 | 209 ppb |

The muon-pin run (`q₀ = 1.10997859556…`) reproduces every `S` to the plotted digits — the
sensitivity is a property of the formula, not the pin. The exact anchor sensitivities
`S(m_μ) = −2/(q−1)` and `S(ℏ_q²) = +2/(q−1)` are verified to 40 digits.

### 1a. The structural decomposition

`S(O) = ν_ℏ(O)·[−1/(q−1)] + S_smooth(O)`, where `ν_ℏ(O)` is the net power of `ℏ_q` in `O`.
**Only the `ℏ_q`-power carries the `1/(q−1) ≈ 9.1` amplification.**

- **Absolute muon anchor** `m_μ ∝ ℏ_q⁻²`: `ν_ℏ = −2` → `S = −2/(q−1) = −18.185`.
- **m_p, m_n** inherit it (`ν_ℏ ≈ −2`): `S ≈ −21`. The extra `−2.8` beyond `−18.2` is the
  `F_Bor` factor (`−2.675`) plus a small `−12 m_e`-term contamination (`≈ −0.14`), scaled by
  `(m_p + 12m_e)/m_p = 1.0065`: `S(m_p) = 1.0065·(−18.185 − 2.675) = −20.997`. ✓
- **Every dimensionless ratio of two `ℏ_q⁻²`-masses has `ν_ℏ = 0`** → the anchor cancels:
  `S(m_p/m_μ) = S(m_p) − S(m_μ) = −2.81`; `S(m_n/m_p) = +0.027`.
- **W_λ** (McKay q-Verlinde measure, a q-integer ratio) has `ν_ℏ = 0` → `S ≈ 0.19` (mark 5),
  ~100× below the absolute anchor. This is the generalized, quantified form of #3830.
- **Caveat — `m_μ/m_e` is NOT pin-robust** (`S = −18.185`) because `m_e` is a fixed scale,
  not an `ℏ_q⁻²`-mass; `ν_ℏ(m_μ/m_e) = −2`. **Pin-robustness ⟺ `ℏ_q`-homogeneity degree 0.**

The Lean carrier proves the exact structural extremes sorry-free (Mathlib `logDeriv`):
`ratio_shared_factor_eq`, `logDeriv_ratio_indep_of_shared_factor` (a ratio's pin-sensitivity
is independent of any shared anchor), `logDeriv_pure_anchor_ratio_eq_zero` (a ratio of two
pure-anchor observables is pin-constant).

## 2. The reframed question

Because ratios are pin-blind, **the μ–p tension is a statement about the absolute anchor**:
the proton pin and muon pin disagree on `q₀` by 11.5 ppb, inducing ~210 ppb on `m_μ` and
~242 ppb on `m_p` (both absolute), but ≤ ~32 ppb on any ratio and only 0.3 ppb on `m_n/m_p`.
**No ratio observable can adjudicate the split** — its induced swing is dominated by the
`F_Bor` residual, never the 210 ppb anchor difference.

What *would* adjudicate: an **independent, absolute (non-ratio, non-anchor-inverted)
determination of `q₀` to < 11.5 ppb**. The `m_μ/m_e` and `m_p/m_e` inversions **cannot** —
they *are* the two sides of the tension.

## 3. Grading the corpus candidates for an absolute q₀

| candidate | absolute & independent? | precision to adjudicate 11.5 ppb? | verdict |
|---|---|---|---|
| **q\*** (S=0 decay-sector point; bar-odd `S=h·D(ũ)` zero) | **Yes** — from the Φ_b/D-ladder geometry, *not* an anchor inversion | **No** — σ(q\*) today ≈ **296 ppb** (25.7× coarser than the 11.5 ppb spread); needs σ(Q_β) ≈ 0.024 eV (~26× better neutron measurement) | independent arbiter **in principle**, but 25.7× too coarse today and gated on a next-gen decay measurement, not a derivation |
| **Vol(4₁) = 2Cl₂(π/3)** | No — a q-independent **constant** (S=0 in the map) | n/a | not a determination of `q₀`; it is the fixed geometric numerator of the anchor inversion `q₀ = f(Vol(4₁), m_μ/m_e)`, not an independent handle |
| **μ pin** (invert `m_μ/m_e = Vol(4₁)/ℏ_q²`) | No — **anchor inversion** | n/a | one side of the tension; cannot break it |
| **p pin** (invert `m_p/m_e`) | No — **anchor inversion** | n/a | the other side of the tension; cannot break it |
| **Substrate-first geometric q₀** (Murakami deformed VC / C2; GGM 3d-index Stokes integer, #3805 G3; Bring exact quintic root) | **Yes** — absolute algebraic/geometric, anchor-free | **Not yet** — all OPEN/unowned; no value at any precision | the only route that could give `q₀` to < 11.5 ppb independent of both anchors; Subgoal-2, **open for all** (2026-07-11), currently unowned |

The registry's "three decay-sector determinations (μ–p–Q_β three-way)" (KC21) resolve into
**two anchor inversions (μ, p) + one genuine independent (q\*)**; only q\* is a real arbiter,
and it is 25.7× too coarse today.

## 4. Tiered verdict

1. **Structural (proved, this PR).** The μ–p tension lives entirely in the absolute anchor
   `ℏ_q⁻²`. Every ratio observable — `W_λ`, `m_p/m_μ`, `m_n/m_p`, and the whole McKay keystone
   route — is pin-blind to it (`ν_ℏ = 0`, Lean-proved cancellation). **No ratio can adjudicate
   the 11.5 ppb split.** This closes the #3830 finding: the keystone route being pin-blind is
   not a limitation of the current construction, it is structural.

2. **Corpus survey (scope-(a)).** **There is NO route in the current corpus that determines
   `q₀` absolutely to < 11.5 ppb independent of the μ and p anchors.** The one genuinely
   independent handle, the decay-sector `q\*`, is 25.7× too coarse today (296 ppb) and gated on
   a next-generation neutron `Q_β` measurement (σ(Q_β) ≈ 0.024 eV), not on a derivation. The
   geometric substrate derivations (Murakami VC, GGM Stokes integer, Bring root) that *would*
   give an anchor-free `q₀` are all open/unowned.

3. **Not resolved.** The μ–p tension requires **either** (i) a next-gen decay-sector
   measurement (σ(Q_β) ≈ 0.024 eV → q\* arbitrates), **or** (ii) a substrate-first absolute
   `q₀` derivation (Subgoal-2, open for all). Nothing here resolves it or is wired.

## 5. What the next session should do

- **Highest-leverage, in scope:** pursue the substrate-first absolute `q₀` — the Murakami
  deformed volume-conjecture dictionary (C2 in `docs/scope/2026-07-12-mq0-literature-candidates.md`,
  "structurally richest") needs the **categorical selection of `N`** (no fit) before evaluation:
  a formalize-first item. This is the only route to an anchor-free `q₀` < 11.5 ppb.
- **Do NOT** chase `W_λ` / the Lawrence–Rozansky modulus as the μ–p discriminant — this map
  proves it is pin-blind (`S ≈ 0.19`). The modulus ID is worth finishing for the keystone's own
  sake, but it will **not** move the μ–p needle.
- **Support #3805's GGM Stokes integer (G3)** — an anchor-free geometric datum on the same
  bar-odd locus that carries `q\*`.
- The decay-sector route is measurement-limited, not derivation-limited: flag for the
  experimental-budget ledger, not for compute.

## Cross-references

- Reassessment: [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md) §"the reassessed path" (μ–p row)
- Habiro pin-robustness origin: #3830; keystone carriers `QOU/BraidKnot/BWVacuumRow*.lean`
- q\* budget: [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md) §"Route 3"
- Absolute-q₀ candidates: [`docs/scope/2026-07-12-mq0-literature-candidates.md`](../scope/2026-07-12-mq0-literature-candidates.md)
- Mass guardrail: [`docs/canonical-mass-formula-guardrail.md`](../canonical-mass-formula-guardrail.md)
- q₀ convention (μ vs p pin): AGENTS.md §"q₀ anchor convention"; Subgoal-2 open-for-all [`2026-07-11-subgoal2-owner-reversal-open-for-all.md`](2026-07-11-subgoal2-owner-reversal-open-for-all.md)
