# Closed-route re-examination roundup

**Date:** 2026-06-01
**Branch:** `claude/three-dashboard-probes-2026-05-31` (PR #1581)
**Trigger:** Author 2026-05-31 — "what options for new avenues?
Ocneanu route, and other closed ones, lets briefly re-explore.
maybe new compute/math is correct and was wrongly ruled out."

## Motivation

The discovery that **meson Habiro c=4** had been ruled out on a
precision-floor artifact (audit 2026-05-29 measured 0.77% miss at
audit-time precision; at 50 dps the actual miss is 0.15% with a
clean c_3 = −0.715 absorbing the residual cleanly) raised the
question: how many other "closed" routes were similarly framed
by binary "ruled-out" verdicts under wrong precision floors, or
under wrong framings (the same flip-flop pattern as Q_β c_3)?

This audit consolidates the 50 dps re-examinations of three
previously-closed routes:

1. **Meson Habiro c=4** (audit 2026-05-29)
2. **Ocneanu −1/12** (audit 2026-05-04 / correction commit 6766b40b9 on 2026-05-26)
3. **Yekutieli natural reading +0.5** (audit 2026-05-23, PR #976)

Plus a brief revisit of PR #701's central falsification of
`λ_scale = 5/2 − G·h²`.

## Summary table

| Route | Original verdict | 50 dps re-exam | Status change |
|---|---|---|---|
| **Meson Habiro c=4** | RULED OUT (0.77% miss vs integer 4) | 0.15% miss; c_3 = −0.715 absorbs (|c_3·u³|/|c_2·u²| = 0.0015) | **REOPENED** — precision-floor + flip-flop framing |
| **Ocneanu −1/12** | RULED OUT (pole order 4 not 10; coeff −1 not −1/12) | k_required = 11.9996 (32 ppm to integer 12); 4 natural categorical candidates hit 12 exactly | **AUDIT STANDS** + nuance — pole-order verdict correct, but tightness deserves categorical work, not "empirical" |
| **Yekutieli +0.5** | RULED OUT (natural reading gives +0.5, not −G) | +0.5 is exact rational from partition combinatorics; no truncation parameter could absorb the sign flip | **AUDIT STANDS** unchanged — genuine structural mismatch |
| **PR #701 `5/2 − G·h²`** | FALSIFIED (Family A gives `+(3/4)·h²` exact) | (not re-tested; Family A theorem is Lean-proved) | **AUDIT STANDS** — proved fact |

## Detail per route

### 1. Meson Habiro c=4 — **REOPENED**

**Probe:** [`meson_habiro_c4_truncation_reexam.py`](../../computations/meson_habiro_c4_truncation_reexam.py)
([witness](../../computations/meson-habiro-c4-truncation-reexam.witness.json))

**Setup:** The path tested `R = 1 + c·u²` with `u = b·ℏ_q²`,
`b² = (h² + 3)/(h² + 4)`. Audit 2026-05-29 measured `C/u² = 4.031`,
called the 0.77% miss to integer 4 a "numerical coincidence", and
ruled out the Habiro identification.

**Re-exam at 50 dps:**

- `C/u² = 4.00606` (only 0.15% off integer 4 — better than 5× the
  audit's number)
- Assume `c_2 = 4` exactly. Required `c_3` to absorb residual:
  `c_3 = −0.7156`
- `|c_3·u³|/|c_2·u²| = 0.0015` — well within natural truncation
  bounds (|c_3·u| ≪ |c_2|)
- `c_3 = −0.7156` is approximately −J·b where J = 2, b ≈ 0.866 —
  i.e. natural-magnitude Hopf-link-times-Bring-factor

**Verdict change:** The 0.77% audit-time miss was a precision-floor
artifact + framing error parallel to the Q_β c_3 flip-flop (PR
#1452/#1479). Treating an unmatched residual as evidence the leading
coefficient is wrong, rather than as a bounded higher-rung truncation
contribution, is exactly the framing error the **Q_β c_k canonical
framing** (audit 2026-05-31, Rule 3+4) was created to prevent.

**Action:** REOPEN the meson Habiro c=4 ansatz at **tier=near-match**
in the canonical framing. The current `c_3 = −0.7156` should be
formally identified to a categorical quantity (candidate: `−J · b` —
Hopf-link evaluation times the Bring scaling).

### 2. Ocneanu −1/12 — **STANDS + nuance**

**Probe:** [`ocneanu_12_route_reexam.py`](../../computations/ocneanu_12_route_reexam.py)
([witness](../../computations/ocneanu-12-route-reexam.witness.json))

**Setup:** The proton-mass identity `m_p = 2·m_μ·F_Bor(q_0) − 12·m_e`
originally attributed the "12" to the reciprocal of the Ocneanu
−1/12 cancellation coefficient. Commit 6766b40b9 (2026-05-26)
ruled this out by direct numerical check of the Lean-proved
Borromean Markov trace closed form: pole order at q → 0 is 4 (not
10), leading coefficient is −1 (not −1/12).

**Re-exam at 50 dps:**

- Pole-order claim **CONFIRMED**: `tr_M(β_Bor, q) ~ −q^{−4}` as
  q → 0, leading coefficient exactly −1.
- BUT: the empirical `k_required` in `m_p = 2·m_μ·F_Bor − k·m_e`
  is **11.9996** at q_0 — only **32 ppm** off integer 12.
- Four natural categorical candidates hit 12 EXACTLY:
  - `3! · [2]_q at q=1 = 6 · 2 = 12` (S_4 dimension × Hopf
    rep dim)
  - `Σ d_λ² · 2 at H_3 = 6 · 2 = 12` (Plancherel × 2)
  - `4 · 3 = 12` (Yekutieli 𝓑_3 edge cells × strands)
  - `dim H_3 · 2 = 6 · 2 = 12`

**Verdict change:** Pole-order verdict stands (the Ocneanu −1/12
attribution is correctly ruled out). But the 32 ppm tightness of
k_required to integer 12 is comparable to the Reading-A tightness
(13.8 ppm) — both deserve categorical investigation, not just
"empirical integer near-match" tags.

**Action:** Pick ONE of the four natural categorical candidates and
attempt a Lean-style structural derivation. The strongest candidate
on physical grounds is `dim H_3 · 2`: the integer 12 then reads as
"twice the Hecke-algebra dimension at H_3" — directly tying the
Borromean structure to the n=3 strand count.

### 3. Yekutieli natural reading +0.5 — **STANDS** unchanged

**Probe:** [`yekutieli_natural_reading_precision_floor_check.py`](../../computations/yekutieli_natural_reading_precision_floor_check.py)
([witness](../../computations/yekutieli-natural-reading-precision-floor-check.witness.json))

**Setup:** Audit 2026-05-23 tested whether Reading-A's conjectural
`−G·h²` could be recovered from a natural categorical π_HS
projection at H_4. The conjugation-averaged classes-projection sum
gave 0.5 (exact rational), not −G ≈ −0.916.

**Re-exam at 50 dps:**

- κ_λ values are EXACT integers (0, 1, 1, 1, 0 for partitions of 4)
- Conjugation-averaged sum / 4 = 0.5 EXACTLY (50 dps confirms)
- |natural − (−G)| ≈ 1.42 (huge structural gap)
- NO meson-Habiro-style precision-floor reduction is possible

**Verdict change:** None. The +0.5 result is a hard rational from
partition combinatorics. There's no truncation parameter to absorb
the sign flip. Different in kind from the meson Habiro c=4 issue.

**Note (open question):** +0.5 IS a legitimate categorical quantity
((1/4) · Σ_classes (κ_λ + κ_λ^T)/2 at H_4). It just doesn't
contribute to m_p closure at h² order. **WHICH physical observable
does +0.5·h² actually contribute to?** Exact rationals from partition
combinatorics don't appear by accident. Candidates worth probing:
- Higher-isotope binding-energy linking_weight (m_He, m_Li)
- The Frobenius dual-pairing residual
- Multi-strand Habiro residue at the H_4 level

This is a constructive R&D pointer, not a re-opening of the m_p
gap derivation.

### 4. PR #701 `5/2 − G·h²` central falsification — STANDS

**Setup:** Audit 2026-05-18 falsified the conjectural form
`λ_scale = 5/2 − G·h²` by computing Family A's natural π_HS gives
`5/2 + (3/4)·h²` exactly (closed-form rational).

**Why no re-exam needed:** Family A's `+(3/4)·h²` is now a Lean-proved
theorem (`YLambdaQSchur.lean § lambda_qSchur_at_h_zero_eq_five_halves`
etc., and contributing decomposition `(1/4) · Σ_λ dim_q V_λ`). The
falsification of the simple `5/2 − G·h²` ansatz is structural fact, not
empirical near-match.

**However:** Reading-A's `5/2 − G·h²` STILL gives a 13.8 ppm residual
to the CODATA closure target at q_0 (per `reading_a_residual_at_50dps.py`).
The 99.981% gap closure is a substantive empirical signal, but the
**categorical mechanism** that would produce `−G·h²` from substrate
data remains the open Reading-A question. The structural reading
hypothesis can be **either**:

- Reading A: `−G·h²` is the categorical truth; Family A's `+(3/4)·h²`
  is not the relevant projection (the `(1/4)·Σ dim_q V_λ` is NOT what
  contributes to m_p closure).
- Reading B: Family A IS the right projection; an additional term
  `−(3/4 + G)·h² = −Reading-A's value` is missing (a structural
  contribution that exactly cancels Family A's `+3/4` and adds `−G`).

Neither has a derived categorical mechanism. This is the **persistent
open hole** in the m_p sub-1ppb closure path.

## Meta-pattern across the four routes

| Pattern | Routes |
|---|---|
| **Precision-floor artifact** (audit precision below the cliff) | Meson Habiro c=4 |
| **Tier-near-match framing error** (binary ruled-out instead of tier-near-match per Rule 4) | Meson Habiro c=4 |
| **Tightness deserves categorical investigation** (10⁻⁵ to 10⁻⁴ match to natural integer/rational/quantity) | Ocneanu "12" (32 ppm), Reading-A (13.8 ppm) |
| **Exact rational from combinatorics — genuine structural mismatch** | Yekutieli +0.5 |
| **Lean-proved structural fact — re-exam not applicable** | PR #701 Family A |

**Key takeaway:** The Q_β c_3 flip-flop framing error (PR #1452 ↔
#1479) is a **generic** failure mode — not a one-off Q_β issue. The
**Q_β c_k canonical framing** (audit 2026-05-31, Rule 3+4) should be
applied to EVERY ruled-out route as a discriminator before
classifying a residual as evidence the leading coefficient is wrong.

The meson Habiro c=4 re-exam reveals this is the second case where
this framing matters (Q_β c_3 being the first). Looking forward:
when re-classifying any "near-match" residual, ask explicitly:
- Is the precision floor below the cliff for this observable?
- Is there a higher-rung c_k of natural magnitude that could absorb
  the residual?
- Is the binary ruled-out verdict actually a tier-near-match
  classification?

## Cross-references

- audit 2026-05-04-ocneanu-cancellation-numerical-verification.md
- audit 2026-05-18-conjecture-falsification.md (PR #701)
- audit 2026-05-23-yekutieli-bijection-natural-reading-negative.md
- audit 2026-05-25-non-abelian-stokes-reading-a-exploration.md
- audit 2026-05-25-proton-mass-identity-12-me-ocneanu.md
- audit 2026-05-29-meson-mK-mpi-residual-derivation-attempt.md
- audit 2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md
  (sibling-PR finding, landed on main 2026-06-01): the Q_β c_3 = −2
  Rule-A identification is a NUMERICAL coincidence between two
  different ε-orders (per-block at ε¹, ladder at ε⁶ — 5 orders
  apart) — independent structural diagnosis CONSISTENT with this
  branch's Probe B tier=near-match verdict. Reinforces (does not
  invalidate) the canonical-framing Rule 4 tiered classification.
- audit 2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
- commit 6766b40b9 (Ocneanu correction)
- PR #1452 / #1479 (Q_β c_3 flip-flop history)
- PR #1581 (the three-dashboard probes that surfaced the framing)

## What's next (recommended ordering)

1. **Meson Habiro c_3 = −0.7156 categorical identification.**
   Highest-leverage: tests whether the REOPENED meson Habiro path can
   produce a Lean-proved closure at tier=near-match. Best categorical
   candidate: −J · b ≈ −2 · 0.866 ≈ −1.73 — doesn't match the
   numerical −0.7156. Search for `c_3` candidates of the form
   `−J · b^k` or `−J_Hopf(q=1) · scaling factor` from H_4 Wedderburn
   data. **Effort: ~1 session.**

   **Update 2026-06-01 — RESULT: NULL.**
   [`meson_habiro_c3_categorical_search.py`](../../computations/meson_habiro_c3_categorical_search.py)
   scanned 40+ natural candidates (integer/rational fractions,
   Catalan-G variants, b-powers, J·b combinations, q-bracket ratios
   including the q-deformation `−[5]_q/[7]_q`). Only candidate
   within 0.5% is the **classical integer fraction −5/7** at 0.103%;
   the q-deformed `−[5]_q/[7]_q` at q_0 is −0.6846 (off by 4.25%),
   so the −5/7 hit is at the q=1 limit, NOT a clean Hecke
   q-deformation. At 50 dps precision a true categorical identity
   would land below 0.05%; the −5/7 near-match looks empirical, not
   structural.

   **Implications for the REOPENED status of meson Habiro c=4:** the
   leading coefficient c_2 = 4 (= J² with J = 2) is still plausibly
   the right framing, AND the |c_3·u³|/|c_2·u²| = 0.0015 ratio is
   well within natural truncation bounds — but **no clean categorical
   identification for c_3 = −0.7156 has been found in the natural
   q-arithmetic basis**. The route stays REOPENED at
   **tier=near-match-without-c_k-identification**, parallel to Q_β's
   pre-Habiro-element state where c_3 = −2 was wired before its
   Habiro-element categorical home was established.

   Productive follow-up directions:
   - Wider basis search (continued fractions, Bring-radical-style
     algebraic numbers, Hopf-link evaluations at different braid
     words)
   - Try identifying c_3 as a SUM of two natural quantities
     (analogous to how m_K/m_π's closure required adding the
     (3q²−1)/(2q²) EM correction)
   - Identify the underlying Habiro element (if any) whose Taylor
     series gives (c_2, c_3) = (4, c_3_unknown) at q=1

   **Update 2026-06-01 — STEP 1b (PSLQ wider search): STRONG NULL.**
   [`meson_habiro_c3_pslq_search.py`](../../computations/meson_habiro_c3_pslq_search.py)
   ran PSLQ integer-relation search over **24 natural substrate basis
   elements** (G, π, ln 2, h-powers, b-powers, q-brackets, ℏ_q-powers,
   J_Hopf, G·b, G/π, …) — pairwise, triples (top-12), and full-basis
   — at 60 dps, tol 1e-12 to 1e-25, maxcoeff up to 10000. **Zero
   integer relations found.** This is a MUCH stronger NULL than the
   hand-curated 40-candidate scan: PSLQ would have found ANY clean
   rational combination of substrate quantities with small integer
   coefficients.

   **Diagnostic implications:** Two routes remain for c_3:
   - **Either** c_3 is genuinely transcendental in q (involves a
     non-standard arithmetic object — Bloch-Wigner dilog,
     Mahler measure of a Borromean-like polynomial, regulator of
     a number-field tower, etc.). Searching such transcendental
     candidates requires problem-specific basis construction.
   - **Or** the leading c_2 = 4 framing itself is wrong: the 0.15%
     miss is NOT a c_3 truncation residual, but rather c_2 is
     slightly off-integer (e.g. c_2 = 4·b_correction, c_2 =
     4·(1 + α·h²), etc.) — in which case the meson Habiro c=4
     re-opening should be RE-CLOSED.

   **Net update to the REOPENED status:** the meson Habiro c=4
   re-opening stays REOPENED but with **lower confidence** —
   the PSLQ NULL suggests that EITHER a problem-specific
   transcendental search is needed OR the framing needs revision.
   Recommend: pivot to a c_2-off-integer hypothesis (test
   `c_2 = 4·(1 + ε·h²)` with PSLQ on ε) before further c_3 work.

2. **Ocneanu integer "12" = dim H_3 · 2 categorical derivation.**
   Tests whether `m_p = 2·m_μ·F_Bor − (2 dim H_3)·m_e` can be
   derived structurally. The integer 12 has 4 natural candidates;
   identifying which one is THE categorical decomposition is a clean
   target. **Effort: ~1-2 sessions** (Lean theorem + interpretive
   block).

   **Update 2026-06-01 — STEP 2a (q-deformation discriminator): NULL.**
   [`ocneanu_12_qdeformation_discriminator.py`](../../computations/ocneanu_12_qdeformation_discriminator.py)
   scanned 14 q-deformations of the 4 candidates against k_required
   = 11.99961221. The bare INTEGER 12 wins (32 ppm); every natural
   q-deformation (3! · [2]_q, [3]_q!·[2]_q, Σ d²_q·[2]_q, etc.)
   OVERSHOOTS in the wrong direction (5000+ ppm). This is the
   signature of an ADDITIVE missing correction, parallel to m_K/m_π's
   Bring-zero-mode EM closure.

   **Update 2026-06-01 — STEP 2b (EM-correction candidate): NEAR-MATCH.**
   [`ocneanu_12_em_correction_candidate.py`](../../computations/ocneanu_12_em_correction_candidate.py)
   tests `k = 12 − (α_em/π) / dim H_3`. Result:

   - `(α_em/π) / dim H_3 = (α_em/π) / 6 ≈ 3.871e-4`
   - residual `12 − k_required ≈ 3.878e-4`
   - **k_predicted matches k_required to 54 ppb (0.054 ppm)** —
     a **600× improvement** over the bare integer 12 (32 ppm)
   - Variants with the m_K/m_π shape `(3q²−1)/(2q²)` REGRESS to
     2984 ppb — the bare `(α_em/π) / dim H_3` is the cleanest
     match in the tested basis

   **Tier classification (per production-vs-exploratory-discipline):**
   `tier = near-match`. NOT a derivation — the Bring-zero-mode
   projection argument that pins the `(3q²−1)/(2q²)` shape in
   m_K/m_π hasn't been applied to the proton-mass `12·m_e` term.
   Both factors are structurally motivated:
   - `(α_em/π)` from m_K/m_π's PR #1442 closure
   - `1/dim H_3 = 1/|S_3| = 1/6` from the natural Plancherel
     normalization over the H_3 Wedderburn block

   **The full form is now:**
   ```
   m_p = 2·m_μ·F_Bor(q_0) − (12 − (α_em/π)/dim H_3) · m_e
       = 2·m_μ·F_Bor(q_0) − 12·m_e + (α_em/π) · m_e / dim H_3
   ```

   **Critical guard:** 0.054 ppm is between the 1 ppm structural-
   identity threshold and the 1% empirical-fit threshold. Do NOT
   wire to production without:
   - a Bring zero-mode (or analog) categorical derivation, OR
   - independent cross-validation at higher precision (e.g. 100 dps
     refresh of all CODATA anchors), OR
   - alternative-form scan ruling out a tighter near-match

   **Effort to close (estimate):** 1 session on the Bring-analog
   derivation, parallel to PR #1442's m_K/m_π closure (the EM
   correction there was derived from the projection of the
   α-EM coupling onto the Bring radical-equation zero-mode).
   Result would promote tier=near-match → tier=proved.

3. **Yekutieli +0.5 observable hunt.** Test whether `+0.5·h²` shows
   up in m_He, m_Li, or higher-isotope linking_weight predictions.
   Constructive R&D, low ranking — important only if a positive
   match would unlock multi-observable closure. **Effort: 1 session
   speculative.**

4. **Reading-A categorical mechanism search (deferred).** The 13.8
   ppm residual remains the largest open empirical signal but is
   widely investigated and unbroken. Defer until items 1-3 are
   resolved or one of them yields structural insight into the
   `−G·h²` projection.

The recommended pivot is **(1) meson Habiro c_3 categorical
identification** — it both validates the Q_β c_k framing as a
general discriminator AND has the cleanest categorical target.
