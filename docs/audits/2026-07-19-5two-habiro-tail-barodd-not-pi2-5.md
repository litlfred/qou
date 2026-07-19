# The 5₂ bar-odd Habiro-tail action is NOT a π²/5-analog — chirality changes the resummation class

**Date:** 2026-07-19 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (5₂ Habiro tail) ·
**Tier:** numerical scope-(a) structural finding · **Discipline:** no fit, no c_k
wired, nothing to production, no tier change.

## Context (now unblocked)

The merged b3ix result derived the **4₁ bar-even** Habiro-tail action = **π²/5**
(golden-ratio dilog), and flagged the bar-**odd** channel needs the chiral **5₂** tail —
which was gated on the authoritative 5₂ cyclotomic coefficients. A sibling has now
landed those (`qbeta_5two_masbaum_cyclotomic_probe.py`, Masbaum 2003; b3ix
"odd datum = cyclotomic-coefficient asymmetry"). This closes the gate and lets the exact
route finally run.

## Construction

Built on the authoritative Masbaum `C_{5₂,n}(q)` (`C₁=−(q⁴+q²)`, `C₂=q¹¹+q⁸+q⁷+q⁵`,
`C₃=−(q²¹+…)`; verified in-probe against the printed values), the archimedean (`ρ_∞`,
real-q) Habiro tail is

> `S(q) = Σ_n C_{5₂,n}(q) · ∏_{j=1}^n (1−q^j)(1−q^{−j})`,   `q = a²`.

The `∏` factor is **bar-symmetric** (`q↔q⁻¹`), so the bar-odd part comes **entirely from
the C_n asymmetry** — the bar-odd tail term is `[C_n(a)−C_n(a⁻¹)]/2 · ∏(…)`. This
independently confirms the sibling's "odd datum = cyclotomic-coefficient asymmetry".

## Result — no clean π²/5-analog

The optimal-truncation bar-odd action `A_odd = −t·ln|δ_odd|` **drifts** and does not
settle:

| t | 0.5 | 0.4 | 0.3 | 0.25 | 0.2 | 0.16 |
|---|---|---|---|---|---|---|
| N\* | 1 | 1 | 1 | 1 | 1 | 2 |
| A_odd | −0.102 | 0.255 | 0.491 | 0.560 | 0.591 | 0.644 |

The minimal term is stuck at **small n** (N\* ≤ 2) because the Masbaum `C_n` carry a
**Gaussian growth** — leading `a^{3n²+5n} = q^{(3n²+5n)/2}` — that dominates the
`∏`-factor decay. So there is **no clean golden-dilog constant** like 4₁'s
`π²/5 = 1.974`; the drift heads toward `~Vol(5₂)/π = 0.900` (the *geometric* value).

## Conclusion

The **chirality** (the `C_n` asymmetry) **fundamentally changes the bar-odd channel's
resummation class**: it is **not** the amphichiral-4₁ `π²/5`-analog. Where the bar-even
4₁ tail (`C_n = 1`) has minimal term at large `n* ~ 1/t` and a clean archimedean dilog
action, the chiral 5₂ tail's Gaussian `C_n` collapses the optimal truncation to small
`n`, giving a drifting, geometric-leaning action — no simple closed form. This
complements the φ_odd findings (the bar-odd datum is genuinely resurgent / full-Z, not a
leading-saddle or clean-tail object): **the bar-odd action has no π²/5-style closed
form** — the exact route that worked for the amphichiral 4₁ does not transfer to the
chiral 5₂.

## Scope (anti-laundering)

Builds the authoritative tail; reports the drift + the structural conclusion. Does
**not** claim a bar-odd action value. No fit; no c_k; no tier change.

## Cross-references

- Authoritative Masbaum C_n: `qbeta_5two_masbaum_cyclotomic_probe.py` (b3ix)
- 4₁ bar-even template (π²/5): b3ix merged 2026-07-18
- ℚ(√−7) home + Theorem 3: [`2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md`](2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md)
- φ_odd is full-Z (not classical/2-loop): [`2026-07-18-5two-phi-odd-purely-2loop.md`](2026-07-18-5two-phi-odd-purely-2loop.md)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
