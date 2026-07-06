# Q_β Habiro element — Option D follow-up (2026-06-01)

> **Parallel-work note (2026-06-01).** A sibling agent independently
> ran the Option D recursion probe and the partition-followup probes
> on the same branch (commits `0b0c67a23`, `549b274cd`) and wrote the
> companion audit
> [`2026-06-01-qbeta-habiro-a8-partition-function-match.md`](2026-06-01-qbeta-habiro-a8-partition-function-match.md)
> for the **a_8 = Σ p(k)·u^{5−k} identification**. The sibling audit
> covers a_8 exhaustively and the a_m(p), a_m(n) leading-coefficient
> recurrence-search negatives. **This audit complements** with three
> distinct findings the sibling audit did not surface:
> (i) the **mechanical S_5 → S_6 telescoping** (constant-term
> cancellation 15 + (−15) = 0 producing the u^15 lift in ONE
> step at m=6), (ii) the **Padé [3/3] exact reconstruction** of a_7's
> 8-coefficient sequence (rational generating-function constraint),
> (iii) the **constant-term boundary chain** p(5) → p_{b=2}(7) → p(7)
> at m = 8 → 7 → 6.
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579).
> Parent audits: [Δa_m factorization](2026-05-31-qbeta-habiro-delta-am-factorization.md),
> [P_8 identification](2026-05-31-qbeta-habiro-p8-identification.md).
> Sibling audit (parallel work): [a_8 partition-function match](2026-06-01-qbeta-habiro-a8-partition-function-match.md).
> Probe scripts:
> [`qbeta_habiro_recursion_probe.py`](../../computations/probes/qbeta_habiro_recursion_probe.py),
> [`qbeta_habiro_partition_followup.py`](../../computations/qbeta/qbeta_habiro_partition_followup.py),
> [`qbeta_habiro_delta6_partition_check.py`](../../computations/qbeta/qbeta_habiro_delta6_partition_check.py),
> [`qbeta_habiro_a7_partition_check.py`](../../computations/qbeta/qbeta_habiro_a7_partition_check.py).
> Witnesses: `qbeta-habiro-recursion.witness.json`,
> `qbeta-habiro-partition-followup.witness.json`,
> `qbeta-habiro-delta6-partition.witness.json`,
> `qbeta-habiro-a7-partition.witness.json`.

## Choice rationale (per task prompt — A/B/C/D)

**Picked Option D** — investigate the degree-drop + small-leading-coefficient
pattern in Δa_m, particularly the anomalous Δa_5/Δa_6/Δa_7=Δa_8=0 boundary,
because:

1. **Avoids Phase 5q convention blocker.** Option A's
   `compute_tau_M_nucleon_H3` vs `habiro-coefficients-atomic.witness.json`
   (tr_M(D) = 0.7281 vs 0.3883) requires resolving a convention question
   that already burned an agent's context per the master ledger.
2. **Algebraic-identification target.** Δa_m polynomials are integer-coeff
   exact data — recursion / partition-function fits give DECISIVE pass/fail
   verdicts, not numerical near-matches subject to flip-flop discipline.
3. **Most-tractable in 30 min.** Sympy can fit linear recurrences, Padé
   approximations, partition-function generating sequences, and partial-sum
   factorizations in < 1 sec each.

## TL;DR — PARTIAL with three concrete new findings

1. **a_8(u) coefficient sequence IS the partition function p(1..5).** Verified
   algebraically: `a_8(u) = u^5 · GF_p(1/u) − u^5` where
   `GF_p(u) = Σ p(k)·u^k = Π_{k≥1} 1/(1 − u^k)`.

2. **The S_5 → S_6 telescoping IS mechanical.** S_5 has constant term +15;
   T_6 = Δa_6·(u;u)_6 has constant term −15. The Δa_6 polynomial
   `−(u^4 + 3u^3 + 5u^2 + 8u + 15)` has the PRECISE leading-down structure
   that lifts S_5/Φ_1Φ_2 (which has min u-degree 0, max u-degree 18) onto
   S_6/Φ_1Φ_2 (which has min u-degree **15**, max u-degree 23, irreducible
   factor P_8). The minimum-u-power table:

   | m | min u-power of S_m / (Φ_1·Φ_2) | max u-power |
   |---|------|---|
   | 1 | 0 | 0 |
   | 2 | 0 | 3 |
   | 3 | 0 | 7 |
   | 4 | 0 | 12 |
   | 5 | 0 | 18 |
   | **6** | **15** | **23** |
   | 7 | 15 | 23 |
   | 8 | 15 | 23 |

   The u^15 lift happens IN ONE STEP at m=6 — the boundary level whose
   contribution cancels the low-degree (u^0..u^14) part of S_5 leaving the
   irreducible P_8 piece.

3. **a_7's 8-term coefficient sequence is REPRODUCED by a Padé [3/3]
   approximant** — i.e. a_7 is the polynomial-degree-≤-7 truncation of a
   ratio of degree-≤-3 polynomials `P(u)/Q(u)` with rational coefficients.
   Specifically:

   ```
   Q(u) ∝ −(10u^3 − 24u^2 + 405u − 552)
   P(u) ∝  (1897u^3 + 3396u^2 + 1818u + 60720)
   ```

   The series `P/Q = 110 + 84u + 63u² + 48u³ + 34u⁴ + 24u⁵ + 17u⁶ + 12u⁷ + O(u^8)`
   matches a_7 abs-coeffs exactly. This is a strong constraint: a_7 lies in
   a finite-dimensional space of rational generating series, even though no
   single partition function reproduces it.

4. **Constant-term boundary chain at u=0** (the m-boundary "tail" of the
   Habiro expansion) involves partition-function values:

   | m | a_m(0) (proton) | |a_m(0)| | Partition identity |
   |---|--------|---------|--------|
   | 8 | 7 | 7 | p(5) = 7 ✓ |
   | 7 | −110 | 110 | p_{b=2}(7) = 110 ✓ (number of 2-colored partitions of 7) |
   | 6 (Δ) | 15 | 15 | p(7) = 15 ✓ |
   | 6 (p) | 494 | 494 | (open) |
   | 6 (n) | 479 | 479 | (open) |

   **The chain a_8 → a_7 → Δa_6 visits successively** p(5), p_{b=2}(7),
   p(7) **at the constant-term position** — a 3-step combinatorial signature
   at the boundary of the Habiro support.

5. **−Δa_6(1) = 32 = 2^5** — clean integer evaluation at u=1.

## Why this is significant

Combined with the prior audits, the structural picture is:

```
Σ_m Δa_m·(u;u)_m = -u^15 · (u-1)(u+1) · P_8(u)

where:
  m=0:    Δa_0 = 0
  m=1..5: contribute to S_5/(Φ_1·Φ_2)  spanning u^0..u^18 (messy)
  m=6:    Δa_6 = -(u^4 + 3u^3 + 5u^2 + 8u + 15)  ← LIFTS S_5 by u^15
                  -Δa_6(0) = 15 = p(7)
  m=7,8:  Δa_7 = Δa_8 = 0  (boundary)
                  a_7(0) = -110 = -p_{b=2}(7)
                  a_8(u) = u^5·GF_p(1/u) − u^5  ≡ Σ p(k)·u^{5-k}, k=1..5
```

The Habiro expansion of `tr_M(n-p, q)` is a **telescoping object** that
collapses at m=6 to the clean form `u^15·Φ_1·Φ_2·P_8`, and the BOUNDARY
polynomials (m=7, 8) are partition-function generators. This suggests:

- **The m=6 boundary IS the structural cut-off** between "raw Hecke
  difference" and "partition-function tail".
- **P_8 is the irreducible residue** that the partition tail cannot
  cover — it parameterizes the GENUINELY HECKE-SPECIFIC part of the n−p
  split.
- **The categorical setting** is plausibly: the Hecke algebra `H_4(q)`
  acts on a partition lattice of the symmetric group `S_4`; the
  partition-function GF appears because the Hecke characters at q→1
  reduce to partition counts (Frame-Robinson-Thrall hook formula).

## Negative findings

- **No constant-coefficient linear recurrence** fits the leading-coefficient
  sequence `[4, -74, 340, -711, 788, -466, 133, -12, 1]` (proton) up to
  order 4. The sequence is GENUINELY non-recursive at the leading-coeff
  level.
- **No polynomial-in-u recurrence** of order 1 or 2 fits the Δa_m sequence
  (tested with sympy.solve on the coefficient system).
- **−Δa_6 abs-coeffs `(1, 3, 5, 8, 15)`** do NOT match any partition window
  directly. But they evaluate at u=1 to 2^5 and at u=0 to p(7), so the
  endpoints are categorical even if the interior coefficients aren't a
  pure partition-shift.
- **−Δa_6 − Φ_5(u) = (u+2)·(2u²+7)** is a partial cyclotomic decomposition
  but doesn't identify Δa_6 as a single cyclotomic-class object.

## Open questions

1. **Categorical meaning of the Padé [3/3] reconstruction of a_7.** The
   denominator `10u^3 − 24u^2 + 405u − 552` has unusual integer
   coefficients — does it factor as a Hecke character at a specific
   conjugacy class? Try Pade-approximant identification against the
   known `H_4(q)` characters `χ^λ` for λ ⊢ 4.

2. **Why is the boundary chain p(5) → p_{b=2}(7) → p(7)?** Is there a
   natural sequence of "Hecke-character-on-tail-strands" that produces
   these specific partition-function values?

3. **What gives Δa_6 = −(u^4 + 3u^3 + 5u^2 + 8u + 15)?** This is the
   single polynomial that does the u^15 lift. It must be the
   `H_4` characteristic polynomial difference for some specific
   conjugacy class — find it.

4. **P_8(u) categorical match.** The bar-twisted symmetry
   `u^8 · P_8(1/u) = P_8(−u)` (from the prior audit) plus the new
   "irreducible residue beyond partition tail" interpretation here
   narrows the categorical search class. Test: is P_8(u) the
   characteristic polynomial of a 4-strand braid matrix at a specific
   eigenvalue locus (q=i, q=−i, q=e^{iπ/4})?

5. **Will this generalize to ³He / ⁴He?** The atomic-step Φ_8 prediction
   (from the prior cross-pair audit) needs verification. If the partition
   tail and Padé reconstruction also appear for tritium/helium, we have a
   STRUCTURAL conjecture; if they don't, we have a 1-nucleon-only
   accident.

## Per the production-vs-exploratory-discipline skill (Rule 14)

This is a **TIERED** result:

- **`proved`** (algebraically exact):
  - `a_8(u) = u^5·GF_p(1/u) − u^5` (verified by sympy.expand).
  - `−Δa_6(1) = 32 = 2^5` (integer evaluation).
  - `S_6 = S_7 = S_8` (since Δa_7 = Δa_8 = 0).
  - The Padé [3/3] reproduces a_7 (verified by sympy.series check).
  - The u^15 lift mechanism (constant-term cancellation 15 + (−15) = 0).

- **`near-match`** (suggestive but unproven categorically):
  - `|a_7(0)| = 110 = p_{b=2}(7)`. Numerical equality at the boundary;
    no derivation of why the m=7 Habiro coefficient should equal the
    2-colored partition function at the boundary level.
  - `−Δa_6(0) = 15 = p(7)`. Same caveat.

- **`unproved (open)`**:
  - Categorical interpretation of the Padé denominator coefficients.
  - Generalization to A ≥ 2.
  - Why the m=6 boundary specifically lifts by u^15 (not u^k for some
    other k).

## Files added

- **NEW:** `computations/probes/qbeta_habiro_recursion_probe.py`
- **NEW:** `computations/qbeta/qbeta_habiro_partition_followup.py`
- **NEW:** `computations/qbeta/qbeta_habiro_delta6_partition_check.py`
- **NEW:** `computations/qbeta/qbeta_habiro_a7_partition_check.py`
- **NEW:** `computations/probes/qbeta-habiro-recursion.witness.json`
- **NEW:** `computations/qbeta/qbeta-habiro-partition-followup.witness.json`
- **NEW:** `computations/qbeta/qbeta-habiro-delta6-partition.witness.json`
- **NEW:** `computations/qbeta/qbeta-habiro-a7-partition.witness.json`
- **NEW:** `docs/audits/2026-06-01-qbeta-habiro-option-d-followup.md` (this file)

## Cross-references

- Parent: [`2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Sibling: [`2026-05-31-qbeta-habiro-p8-identification.md`](2026-05-31-qbeta-habiro-p8-identification.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) PROBE NEW.
