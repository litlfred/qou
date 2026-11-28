# q₀ anchor: 80-dps Newton polish and round-trip cut (bean `qou-y7ek`)

Date: 2026-11-27. Precision change only (AGENTS.md exemption 1). **The value of
q₀ does not move.**

## What was measured

Producer: `computations/probes/q0_80dps_anchor_roundtrip_probe.py`, witness
`computations/probes/q0-80dps-anchor-roundtrip.witness.json` (7/7 assertions,
mpmath, no float64).

q₀ is the root of the one-term proton substrate identity
F(q) = 2·(Vol(4₁)/ℏ_q²)·|tr_M(β_Bor)|·[3]_q!/q³ − 12 = (m_p/m_e)_CODATA.

| quantity | value |
|---|---|
| q₀, 80 digits | `1.1099785827513808075916690956107688798744991218735787360728142401817989635744830` |
| Newton steps (120 dps) | 2.75e-9, 1.05e-16, 1.52e-31, 3.22e-61, 1.37e-120 (quadratic) |
| round-trip F(q₀)/(m_p/m_e) − 1 | 1.55e-120 |
| same, from the 50-digit `Q_50_DIGIT_STR` | 4.02e-49 |
| rounds to `Q_50_DIGIT_STR` / `Q_MP` (70) | yes / yes |
| agreement with `q_at(95)` | 120 digits |

**Error as a cut.** `lo = ⌊q₀·10⁸⁵⌋/10⁸⁵`, `hi = lo + 10⁻⁸⁵`. The residual is
+1.33e-81 at `lo` and −2.14e-81 at `hi`, identical at 120 and 240 dps. So
q₀ ∈ (lo, hi): the cut `QOU.Core.LawvereCut.Cut.ofInterval lo hi` over ℚ, located
at resolution 10⁻⁸⁰. This is a numerical certificate at two precisions, not an
interval-arithmetic proof.

The two-term pin (`q_proton_two_term_at`, a named comparison only, owner ruling
2026-11-20) gets the same treatment: residual 2.13e-120, cut brackets the root.

## Dashboard fix

`per_observable_100x_status.py` reported the m_p anchor round trip as
0.002852 ppb. That number is CODATA's own rounding: the round trip was measured
against the separately rounded 11-digit MeV entry 938.27208943, not against the
quantity that pinned q₀, m_e × (m_p/m_e) = 938.27208942732424736394. The row now
measures `roundtrip_residual_ppb` against the anchor (**7.197e-43 ppb**, the
50-digit floor of the upstream witness), and reports the CODATA rounding gap
separately as `codata_rounding_ppb` (0.002852). `err_ppb` is unchanged. The row
stays unscored.

## What this does not claim

A round trip through the defining identity checks arithmetic, not physics. The
CODATA ratio is the CAL-2 input of a computation and enters no proof.

## Left open

The m_p substrate-identity producer still reads q₀ from the 50-digit
`Q_50_DIGIT_STR` (the second 50-dps channel of bean `qou-5eg1`), which is why the
dashboard floor is 7e-43 ppb rather than 1e-110. Raising it touches m_n, Q_β and
Δ_pn in a witness other threads consume, so it is not done here.
