# Two-term proton q₀ re-pin (2026-11-20) — REVERTED the same day; kept as a named comparison

> **🛑 OWNER RULING, later on 2026-11-20 (Carl): *"Revert to 1-term default"*.** The default q₀ stays the **one-term** proton pin (`q_at()`, `Q`, `Q_MP`, `Q_50_DIGIT_STR` = `1.10997858275138080759…`). The two-term pin survives only as a **named comparison**: `qou_substrate.constants.q_proton_two_term_at()`, `Q_PROTON_TWO_TERM_50_DIGIT_STR`, and `check_proton_pin_self_consistency()`, which checks both identities. The witness sweep is dropped.
>
> **Why.** At the two-term pin α_em⁻¹ (form B) moves from **+0.365 ppb to +75.97 ppb (495σ)** (PR #8562), while covariant QED insertions give **zero** proton self-energy (PR #8565). So the two-term term buys the μ–p improvement below at the price of breaking α_em, from a term the covariant calculation does not produce. The μ–p residual points at the muon relation instead (bean `qou-6gf9`).
>
> **What the revert (PR #8554, second half) did.** It restored main's version of every file the branch changed, except: the comparison-pin API in `constants.py` (additions only; `q_at()`'s body is byte-identical to main's), the scorecard's m_μ row now **derived** from the live one-term pin instead of the frozen literal `105.658397811` (it reproduces that literal; scored payload equal to main's), and the scorecard's two-term diagnostic now using the exact comparison root instead of the linearised one (7.5e-15 low, with the sign of the shift wrong in its note). Reverted: the default switch, the gate prefixes (`witness._Q0_PREFIXES`, `q0_anchor_consistency_audit._EXPECTED_PREFIX`), `q0_value_drift_audit.PIN_TOL_PPB` (back to 0.5 ppb: at the one-term pin the CODATA-2018 and retired muon pins are ~11.6 ppb away, so the tighter window had no job), the `codata_truncation_audit` fixture, the two-term canonical m_p / m_n / Q_β / Δ_pn in `canonical_mass` and the m_p substrate-identity producer (main's labelled `two_term_borromean_qed_diagnostics` fields remain the comparison), and all ~204 Stage-C witness re-pins. The remaining-sweep ledger `2026-11-20-two-term-repin-sweep-remaining.tsv` is deleted as obsolete (it lives in commit `fc4b391176`).
>
> **Everything below is the record of the re-pin as it was made**, kept because the numbers (the +11.1709 ppb shift, the 495σ α_em cost, the μ–p arithmetic) are the comparison's content. Where it says "default", read "comparison pin". Hazards 1, 2 and 4 no longer apply.

**Ruling.** Owner (Carl, 2026-11-20): *"Put two term in scorecards and ALL compute"*. He selected options 2 (facade m_n via `canonical_mass`) and 3 (FULL q₀ re-pin through the two-term proton identity). Option 1, the scorecard only, is #8549. Option 4, the μ̄ front, is a separate agent's.

The scope was stated with the ruling and accepted. The two-term term is **selection-scoped**: plain weighting at the m_e scale; adjacent insertion is non-covariant; the covariant all-pairs projection gives b = 0. A re-pin builds that choice into q₀.

Implemented in PR #8554.

## The identity

The retired one-term pin, 2026-05-28 → 2026-11-20:

    m_p/m_e = 2·Vol(4₁)/ℏ_q²·F_Bor(q) − 12,   F_Bor = |tr_M(β_Bor)|·[2]_q[3]_q/q³

The two-term pin, now the default `q_at()`:

    m_p/m_e = 2·Vol(4₁)/ℏ_q²·F_Bor(q) − 12 + |tr_conn(p, V³)|(q),
    tr_conn(p, V³) = −2(q−1)⁴(q+1)⁴(q⁴+q²+1)/(27 q⁶)

The second term comes from Lean `QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`, so M_p^QED = m_e·|tr_conn|.

## The numbers

Solved exactly with mpmath `findroot` at dps + 15 guard digits.

| pin | q₀ |
|---|---|
| retired one-term | `1.10997858275138080759166909561076887987449912187357873607` |
| **two-term (default)** | `1.10997859515088599908756520359868262121410348054121621148890` |
| linearised (old scorecard diagnostic) | `1.109978595150878501566165` |
| CODATA-2022 muon `q_muon_at()` | `1.10997859564273904668179512938…` |

- Shift two-term − one-term: **+11.1709409390 ppb**. q **increases**, because d(m_p^QCD/m_e)/dq < 0 at q₀. The scorecard diagnostic's note said q decreases by 2.23e-7; both the sign and the magnitude were wrong.
- Linearised value: 7.50e-15 below the exact root (relative 6.75e-15).
- Two-term − muon: **−0.4431 ppb**. On the one-term pin it was −11.6 ppb.
- Self-consistency at 60 dps: the identity residual is −5.4e-77. The independent Newton solver `q_two_term_borromean_at` agrees to the last digit.

## What moved

Producers were re-run and baselined from git.

| observable | main (one-term pin) | two-term pin |
|---|---|---|
| m_μ pred | 105.658397811 MeV, +211.2 ppb, miss 970.2× | 105.658376347 MeV, **+8.058 ppb**, miss 37.0× |
| m_n (substrate identity) | +501.4 ppb | +148.4 ppb |
| m_K/m_π | 51.48 ppb (0.195×) | 55.89 ppb (0.212×) |
| Q_β / m_n / Δ_pn primary rows | — | unchanged at quoted digits |
| L2 headline | 1/6 scoreable | 1/6 scoreable |

**How to read the m_μ figure.** The μ–p tension shrinks from 9.5σ to about 0.36σ (ratio σ). That is the arithmetic consequence of a selection-scoped term chosen at the m_e scale. It is **not** independent evidence for that term (§NO FITTING: accuracy is not evidence of correctness). Any claim that the two-term QED term "resolves the μ–p tension" would have to show the selection is derived, and the ruling records that it is not.

## Hazards introduced

1. **The 10-digit muon prefix no longer identifies the muon pin.** Both live pins now begin `1.109978595`, so the four-row counting method in AGENTS.md (§q₀ anchor convention, the `1.109978595` row) now counts proton witnesses as muon. Updated here:
   - `witness._Q0_PREFIXES`: proton `1.10997859515`.
   - `q0_anchor_consistency_audit._EXPECTED_PREFIX`: proton `1.109978595150`.
   - `q0_value_drift_audit.PIN_TOL_PPB`: 0.5 → 0.05 ppb. The old window would have classified the CODATA-2018 muon (−0.080 ppb) and the retired frozen muon (−0.077 ppb) as proton.
2. **Blast radius.** **1845 / 3622** tracked witnesses carry the retired one-term literal (`1.109978582751`), over about 1545 producers; **637** non-witness files carry it too. Until each producer is re-run, its witness reports `Q0_FLIP` and `STALE`. That is deliberate and is not masked.
3. **The scorecard `m_mu` row was a frozen literal** (`105.658397811`). It is now derived from the live pin, and the derived one-term value reproduces the old literal exactly.
4. **Canonical m_n is two-term.** Code that adds Δm_QED to `nucleon_mass_mev("n")` double-counts. The one-term value is `canonical_mass.nucleon_mass_one_term_mev()`.
