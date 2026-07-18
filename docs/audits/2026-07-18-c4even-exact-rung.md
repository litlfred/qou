# c₄^even promoted to a validated exact rung (2026-07-18)

**Tier:** exact-rational measurement; follow-on to bean `9fnm` /
[`2026-07-03-9fnm-c3even-exact-rational-measurement.md`](2026-07-03-9fnm-c3even-exact-rational-measurement.md).
Audit-only; no production wiring; no fit; scope-(a).

## What this closes

Bean `9fnm` extracted `c₂^even` and `c₃^even` exactly and left `c₄^even` as a
bare **s⁸ "scale check"** — labelled "not a claimed rung" because that probe
capped at `KC=3`, so `log(1+c₄u⁴)` was never folded and the s⁸ residual carried
no conditioning check. This probe
([`qbeta_c4even_exact_sseries_probe.py`](../../computations/qbeta/qbeta_c4even_exact_sseries_probe.py)
+ witness) extends the exact-rational Taylor extraction to `KC=4` (series order
`s¹⁰`), folds `c₄` at its own order, and reads the next order as a stability
residual — promoting `c₄^even` to a **validated rung**.

## Result (exact-rational Taylor coefficients of the net-route ladder)

| rung | value | status |
|---|---|---|
| `c₂^even` | −8.0064100587 | gate (reproduces the established rung) |
| `c₃^even` | 86.6611630647 | gate (matches the `9fnm` witness to <1e-6) |
| **`c₄^even`** | **−1819.7406725229** | **validated exact rung** |
| `c₅^even` (scale) | ≈ 63240.995 | s¹⁰ conditioning check — **not** a rung claim |

The ladder is a rapidly-growing alternating sequence (−8 → +87 → −1820 →
+63241; successive ratios ≈ 11, 21, 35 — super-geometric), the expected
divergent-ladder signature. Every value is a Taylor coefficient of the exact
object `R(q) = Q_b/[Q_A·cos(α_eff)]` with `R(1)=1` — no fit.

## Casoratian follow-on

The Auslander–Wenzl one-recurrence positivity test needs
`W₃ = c₃^even·c₄^odd − c₄^even·c₃^odd`. With `c₄^even` now a real rung, the
**only** remaining input is `c₄^odd` (which sits beyond the CAL-anchored tier —
still gated). `W₂ ≈ 102.67` (odd shadow `c₂^odd=−1` proved, `c₃^odd→−2`). AW
positivity predicts `W₃/W₂ > 0`; that test is one `c₄^odd` measurement away.

## c₄^even *used* in a laddered reconstruction — representation vs accuracy (2026-07-18)

Follow-on probe
[`qbeta_c4even_ladder_reconstruction_probe.py`](../../computations/qbeta/qbeta_c4even_ladder_reconstruction_probe.py)
+ witness. This actually **wires** the merged c₄^even rung — folds it into the
even partial sum `R_even = Π_{k≥2}(1+c_k^even u^k)` at the substrate anchor —
and sizes what it buys, separating the two legs that get conflated:

| measurement | result |
|---|---|
| **M1: c₄^even is a real sub-leading even rung** | at `u(q₀)≈0.00852`, `|c₂u²|=5.81e-4 > |c₃u³|=5.35e-5 > |c₄u⁴|=9.58e-6` (ratios 0.092, 0.179) — a well-behaved asymptotic series; c₄^even's incremental effect on the reconstructed Q_β is **0.0075 keV** |
| **M2: the odd channel dominates the whole even ladder** | `log R_exact=+7.37e-3`, `log R_even(N=4)=−5.37e-4`; the odd factor `R_exact/R_even` is `log=+7.91e-3` — **14.7× larger and opposite sign** to the entire even ladder |
| **accuracy vs CODATA** | odd-channel-controlled: the exact object misses by `+0.75%` (≈6.2 keV gap); c₄^even's 0.0075 keV is **~830× too small** to touch it |

**Wiring verdict.** c₄^even is correctly *used* and is a genuine sub-leading
even rung, but the accuracy vs CODATA is bottlenecked by the bar-odd channel —
a proved representational prune (swings 2.44% between the proton/muon q₀
anchors, `dc₃/dq≈4.6e6`;
[`2026-07-07-c3-even-solved-s-complex-volume-rigidity.md`](2026-07-07-c3-even-solved-s-complex-volume-rigidity.md)).
Running the L2 dashboard confirms production **unchanged**: `beats_100x = 2/7`
(m_e, m_K/m_π), Q_β still `160.1×` miss. The even ladder cannot — and does
not — move `beats_100x`. This is the honest answer to "wire c₄^even": the rung
is real, sized, and folded, and its measured effect is dwarfed by the gated
odd channel.

## Discipline

`c_k^even` here is the **net-route bar-even (binding-side) ladder**, distinct
from the Q_β production `c_k` (with `c₂=−1` Taylor-exact). No `c_k` wired to
production; any `c_k≥3` wiring would require owner approval + the proton+muon
cross-anchor test (registry §8). auditOnly.
