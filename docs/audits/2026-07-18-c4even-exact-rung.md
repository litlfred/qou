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

## Discipline

`c_k^even` here is the **net-route bar-even (binding-side) ladder**, distinct
from the Q_β production `c_k` (with `c₂=−1` Taylor-exact). No `c_k` wired to
production; any `c_k≥3` wiring would require owner approval + the proton+muon
cross-anchor test (registry §8). auditOnly.
