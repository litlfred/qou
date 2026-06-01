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

**Probe:** [`meson_habiro_c4_truncation_reexam.py`](../../folio-assistant/computations/meson_habiro_c4_truncation_reexam.py)
([witness](../../folio-assistant/computations/meson-habiro-c4-truncation-reexam.witness.json))

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

**Probe:** [`ocneanu_12_route_reexam.py`](../../folio-assistant/computations/ocneanu_12_route_reexam.py)
([witness](../../folio-assistant/computations/ocneanu-12-route-reexam.witness.json))

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

**Probe:** [`yekutieli_natural_reading_precision_floor_check.py`](../../folio-assistant/computations/yekutieli_natural_reading_precision_floor_check.py)
([witness](../../folio-assistant/computations/yekutieli-natural-reading-precision-floor-check.witness.json))

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

2. **Ocneanu integer "12" = dim H_3 · 2 categorical derivation.**
   Tests whether `m_p = 2·m_μ·F_Bor − (2 dim H_3)·m_e` can be
   derived structurally. The integer 12 has 4 natural candidates;
   identifying which one is THE categorical decomposition is a clean
   target. **Effort: ~1-2 sessions** (Lean theorem + interpretive
   block).

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
