# The even-channel Ohtsuki expansion is exact through κ₄ — the entropy-block is a divergent-tail phenomenon

**Date:** 2026-07-12 · **Axis:** z→c_k f-map keystone (even channel) · **Tier:**
numerical-exact (targeted extraction + 2-term PSLQ) · **Discipline:** no fit to QOU
data, no Q_β c_k wired, no tier change. Follow-up to the merged
[`κ₁ = 11√3π/108`](2026-07-11-fmap-action-qsqrt3-saddle-lean.md) (#3606).

## Question

#3606 identified the **leading** rung `κ₁ = [1/N] log J_N(4₁) = 11√3π/108`
exactly. #3571 showed the **full ladder** is entropy-blocked (divergent resurgent
series `c_m ~ m!/A^m`). The two facts frame a sharp question: **is the block a
low-rung wall, or a divergent-tail phenomenon that leaves the first several rungs
exactly identifiable?**

## Method

[`qbeta_ohtsuki_higher_rungs.py`](scripts/qbeta_ohtsuki_higher_rungs.py). Strip the
exact `(3/2)log N + N·Vol/2π` pieces from `log J_N`, fit `Σ a_j (1/N)^j` through an
11-point geometric ladder (N ≤ 1572864, dps 200; `κ_n = a_n`), then a **strict**
2-term PSLQ against the single parity-appropriate generator. The parity rule is a
structural prediction from `log(1 + Σ κ_n^Oht ℏ^n)` with `ℏ = 2πi/N` and
`κ_n^Oht ∈ ℚ(√−3)` (the 4₁ trace field); the real observable `[1/N^n]` forces:

- **odd** `n` (`ℏ^n` imaginary): `κ_n ∈ ℚ·√3·π^n` (carries √3, like κ₁);
- **even** `n` (`ℏ^n` real): `κ_n ∈ ℚ·π^n` (pure rational, no √3).

Each rung is tested only against its own generator (`√3π^n` or `π^n`) — a hit
therefore *confirms* the parity by construction, a miss is honest.

## Result — exact through κ₄, parity confirmed

| rung | exact value | parity | confident digits |
|---|---|---|---|
| κ₁ | **(11/108)·√3π** | odd → √3 ✓ | 27 (also #3606-exact to 33) |
| κ₂ | **(2/27)·π²** | even → rational ✓ | 22 |
| κ₃ | **(1081/21870)·√3π³** | odd → √3 ✓ | 17 |
| κ₄ | **(98/729)·π⁴** | even → rational ✓ | 12 |

The **√3-parity alternation is exact** (odd rungs carry √3, even rungs are pure
rational), and the denominators are **3-power-dominated** — `108 = 2²·3³`,
`27 = 3³`, `21870 = 2·3⁷·5`, `729 = 3⁶` — the ℚ(√−3) torsion-3 signature of the
figure-eight trace field.

## Interpretation

**#3571's entropy-block does not bite at low rungs — it is a divergent-*tail*
phenomenon.** The even-channel Ohtsuki perturbative expansion has an exact
`ℚ(√3)·π^n` closed form at least through κ₄; #3571's PSLQ failure was on the
*full ladder* (where `c_m ~ m!/A^m` outruns any attainable precision) and on a
basis-size artifact, not on the individual low-order coefficients. Each rung is a
targeted, best-conditioned extraction, so the exact-identification frontier lies
well above κ₄ (bounded below only by attainable extraction precision, which decays
~5 digits/rung).

## Confidence

κ₁ (27 digits; independently #3606-exact) and κ₂ (22 digits, height 27) are
rock-solid. κ₃ (17 digits, height 21870) is solid. κ₄ (12 digits, height 729) is
strong but the lowest-margin (a height-729 rational at 12 digits carries a small
false-positive risk); a higher-N confirmation run (13 points, N ≤ 6.29M) is used
to raise κ₃/κ₄ confidence and is reported in the witness.

## Honest scope (anti-laundering)

These are facts about the **4₁ Kashaev/Ohtsuki asymptotic** — topological
invariants of the figure-eight knot — **not** wired Q_β production `c_k` values.
The bridge from the 4₁ resurgence action to the physical Q_β observable action
remains the open keystone. **No fit to QOU data; no c_k value wired; no tier
change.**

## Cross-references

- Leading rung κ₁ = 11√3π/108 (#3606, merged): [`2026-07-11-fmap-action-qsqrt3-saddle-lean.md`](2026-07-11-fmap-action-qsqrt3-saddle-lean.md)
- Full-ladder entropy-block (#3571): [`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
- Extraction probe + witness: [`scripts/qbeta_ohtsuki_higher_rungs.py`](scripts/qbeta_ohtsuki_higher_rungs.py)
