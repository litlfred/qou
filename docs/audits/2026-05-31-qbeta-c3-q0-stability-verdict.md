# Q_β c_3 q_0-stability verdict (5th and final settlement)

**Date:** 2026-05-31
**PR:** #1580 (claude/coord-infra-1ppq-2026-05-31)
**Probe ID:** `probe-c3-q0-stability` in `.beans/1ppq-qbeta-queue.json`
**Status:** SETTLED

## TL;DR

The Q_β third Taylor coefficient `c_3 = J_Hopf(q=1) = -2` is a
**structural near-match, not a Taylor-EXACT derivation**. The
question "is the 2.98% cross-anchor swing the true q-dependence
of c_3(q) or a fitting artifact?" was answered by rerunning the
existing diagnostic at 65 dps default: the swing exceeds 10⁻⁵⁰
compute precision by 48 orders of magnitude, and the J_Hopf(q=1)
= -2 nominal value does NOT match the empirical c_3 at EITHER
anchor (0.48% off at muon-pin, 3.46% off at m_p-pin).

c_3 is therefore neither (a) Taylor-exact constant, nor (b)
Taylor-exact q-dependent function via J_Hopf(q) − ℏ_q²(q). It
is a near-match whose closure requires identifying the **Q_β
Habiro element**, parallel to the α_EM Habiro element
`[2]_q · (1 - h² α)` derived in PR #1511.

This is the **fifth settlement** of c_3 in five days
(b2f908731 → 41b8d4a4c → f4930df95 → c1f7487df/b3c92844d → this).
The flip-flop history is documented in
`docs/coordination/1ppq-qbeta.md` to prevent a sixth.

## Evidence

### Diagnostic rerun (2026-05-31, 65 dps default)

Ran [`computations/qbeta/qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py)
at 65 dps default compute precision. The script's Part D output:

```
PART D: q₀-stability floor diagnosis

c_3 = J_Hopf(q=1) nominal:    -2.0000
c_3 empirical @ muon-pin q₀:  -2.0097  (0.48% off nominal)
c_3 empirical @ m_p-pin  q₀:  -2.0693  (3.46% off nominal)
swing across anchors:         2.98%

A 3% cross-anchor swing >> compute precision (10⁻⁵⁰) ⟹ c_3=-2
is a STRUCTURAL NEAR-MATCH, not a Taylor-EXACT coefficient.
```

Also Part C showed the N=4 → N=5 non-monotonicity that's the
experimental signature of near-match c_k≥3:

```
N=4 residual:  +0.055 ppb
N=5 residual:  +0.633 ppb   ← non-monotone (would be impossible
                              for a convergent series with EXACT c_k)
```

### Distinguishing (a) constant vs (b) q-dependent function

The open question this probe asked was whether the 2.98% swing
is:

- **(a)** evidence that c_3 has a TRUE q-dependence and we're
  evaluating "c_3(q)" at different q's, OR
- **(b)** a fitting artifact: c_3 is approximately a constant
  but the fit catches different higher-order leakage at each q.

**Test:** If (a), then `c_3(q_0) = J_Hopf(q_0) − ℏ_q²(q_0)`
(per `c1f7487df` re-derivation) should EXACTLY match the empirical
value at each anchor — independent of which anchor.

**Result (Part D verbatim):**
- nominal at q=1: `-2.0000`
- empirical at muon-pin: `-2.0097` (diff: +0.0097, 0.48%)
- empirical at m_p-pin: `-2.0693` (diff: +0.0693, 3.46%)

The CONSTANT formula c_3 = -2 (J_Hopf(q=1)) is what's in production
wiring. The diff at the m_p-pin (3.46%) substantially exceeds the
diff at the muon-pin (0.48%). Neither is sub-compute-precision.

If c_3 were a Taylor-exact constant, the diff would be < 10⁻⁵⁰ at
both. If c_3 were a Taylor-exact q-dependent function evaluated by
some formula F(q), then `F(q_proton) - F(q_muon)` would equal
`-2.0693 - (-2.0097) = -0.0596`, and we could test whether a
candidate formula F(q) like `J_Hopf(q) − ℏ_q²(q)` reproduces this
exact difference (Kauffman-bracket J_Hopf(q) = -(q^(5/2) + q^(1/2))
gives F(q_proton) ≈ -2.356, F(q_muon) ≈ -2.355, difference ≈ -0.001
— **off by 60×** from the empirical -0.0596).

**Verdict (b)** — fitting artifact. c_3 is neither a Taylor-exact
constant nor a Taylor-exact function via the candidate J_Hopf(q)
formula.

### Compute precision floor

Per `computations/substrate/_precision.py`: default is 65 dps
compute / 50 dps serialization, truncation to 10⁻⁵⁰ absolute. The
2.98% swing at 10⁻² scale dwarfs this floor by 10⁴⁸ — there is no
plausible compute-precision explanation for the swing.

## Resolution path

Per the existing diagnostic Part E: **identify the Q_β Habiro
element**. Pattern from α_EM PR #1511 (merged 2026-05-27):

- α_EM at next order: factor `[2]_q · (1 - h²α)` is a **Habiro
  element** whose Taylor coefficients ARE the α_EM correction
  c_k.
- Specifically: `c_k = 2 · C(1/2, k/2) · (1/4)^(k/2)` (binomial-exact).
- Once the Habiro element is named, the c_k become exact,
  q_0-independent, and `|c_{N+1} · u^{N+1}|` is a rigorous
  truncation bound.

The Q_β ladder needs the same treatment. Per `b502b9b83` audit:
"6 mechanisms ruled out, 1 direction left". Per PR #1521
(claude/alpha-em-habiro-categorical-1loop-2026-05-30): the
categorical-1-loop interpretation of `[2]_q · (1 - h²α)` may
extend to Q_β.

This becomes the **new keystone probe**:
[`probe-qbeta-habiro-element-search`](../../.beans/1ppq-qbeta-queue.json)
in the queue.

Until the Q_β Habiro element is identified:

- **c_2 stays `tier: proved`** (Taylor-exact).
- **c_3+ stay `tier: near-match`** (NOT Taylor-exact).
- **N=3 truncation still beats 100× experimental** (residual ≈
  6 ppb < 7.8 ppb target). This is a real engineering fact, NOT
  a derivation. Report tiered.
- **1ppQ (10⁻¹⁵) is unreachable** without the Habiro element —
  the truncation bound only goes as low as the floor of the
  near-match c_3+ swings.

## Flip-flop prevention rule

For the next session reading this: **do not re-wire c_3 as a
derivation.** The five prior settlements all ended at "near-match,
not Taylor-exact". The pattern is:

1. A clean-looking formula matches numerically near one q_0
   anchor (J_Hopf(q=1) at muon-pin: 0.48% off).
2. Treating that match as a derivation, wire c_3 into the
   production ladder.
3. Re-pin to a different anchor (e.g. m_p re-pin 2026-05-29 per
   PR #1422). The "match" becomes "off by 3.46%". Retract.
4. Find another clean-looking formula with different q-dependence
   (e.g. J_Hopf(q) − ℏ_q²(q)). Goto 1.

The exit from this loop is **identifying the Habiro element**, not
finding yet another canonical-looking formula at q=1.

If you arrive at this audit thinking you've found a sixth
derivation: re-read Part D of the diagnostic at 65 dps and check
that your derivation matches BOTH anchors to within compute
precision (10⁻⁵⁰), not just the production anchor. If it doesn't,
it's a sixth near-match, not a derivation.

## Cross-refs

- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — master ledger (flip-flop history table now shows 5 entries)
- [`computations/qbeta/qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py) — the diagnostic (rerun at 65 dps as part of this verdict)
- [`computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json`](../../computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json) — the witness (unchanged on disk; rerun confirmed same conclusions)
- [`.beans/1ppq-qbeta-queue.json`](../../.beans/1ppq-qbeta-queue.json) — queue with this probe `status: done`, new keystone `probe-qbeta-habiro-element-search` added
- PR #1511 — α_EM Habiro element (the canonical template)
- PR #1521 — Habiro categorical 1-loop (in-flight, hints at Q_β extension)
- CLAUDE.md §Q_β c_k truncation order canonical framing (already documents this; this audit is the per-coefficient settlement record)
