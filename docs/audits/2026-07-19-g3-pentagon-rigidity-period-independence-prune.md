# G3 formalize-first prune: the substrate periods `ib, i/b` are ℝ-independent — `PentagonRigidity` shrinks to one named analytic fact

**Date:** 2026-07-19 · **Branch:** `claude/agent-pickup-stalled-rtugin` ·
**Axis:** G3 / argument→S resurgent-monodromy keystone · **Tier:** formalize-first
structural prune (Lean, sorry-free) · **Discipline:** proves an unconditional
linear-algebra fact; does **not** close `PentagonRigidity`, does not touch `A_ω`,
nothing wired, no fit.
**Lean:** [`QOU/QBeta/SubstratePeriodsIndependent.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SubstratePeriodsIndependent.lean)
(`scripts/lean-verify.sh` exit 0, sorry-free; wired into `QOU.lean`).

## Context — the two open legs of `PentagonRigidity`

The G3 keystone is the argument→S continuation from the fibre-level (formal-`q`)
categorical complex volume to the archimedean bar-odd decay projection `S`. Its
Lean lane (`MonodromyDatumRigidity`, `CyclicDilogPentagon`) proves the monodromy
datum is *forced, not fitted* — **conditional on** the open hypothesis
`PentagonRigidity.uniqueUpToScalar` (the Faddeev–Volkov content the pentagon
buys). The recently-proved `DoublyPeriodicLiouville.ratio_const_of_doublyPeriodic`
(doubly-periodic ⇒ constant, from Mathlib primitives) **reduced** that open
hypothesis to exactly **two** named analytic facts:

1. the ratio `Φ₁/Φ₂` of two `FaddeevPhi` solutions is **entire** (the zeros of the
   two `Φ_b` coincide); and
2. the two periods `ib` and `i/b` of that ratio are **ℝ-linearly independent** at
   the substrate modulus `b`.

## What this discharges — leg (2)

`periods_linearIndependent (b : ℂ) (hb : b ≠ 0) (himb2 : (b^2).im ≠ 0) :
LinearIndependent ℝ ![Complex.I * b, Complex.I / b]`.

The two periods span `ℂ` over `ℝ` exactly when their `ℝ`-ratio `b² = (ib)/(i/b)` is
not real. Proof: an `ℝ`-relation `s•(ib) + t•(i/b) = 0` factors through `I` and,
after clearing `b`, gives `s·b² + t = 0`; taking imaginary parts (`t` real) yields
`s·Im(b²) = 0`, so `s = 0`, whence `t = 0`. Unconditional given `Im(b²) ≠ 0`. The
companion `periods_card_eq_finrank` (`2 = finrank ℝ ℂ`) makes the `Basis (Fin 2) ℝ ℂ`
that `ratio_const_of_doublyPeriodic` consumes a mechanical corollary.

At the substrate the modulus is `b = √β·e^{iπ/4}` (the `PhiBProd` convergence
branch), so `b² = iβ` and `Im(b²) = β > 0` — the hypothesis holds, and the
Liouville step applies.

## Effect: the standing-open hypothesis is now a single fact

With leg (2) proved, `PentagonRigidity` shrinks to **exactly one** honest open
analytic input — leg (1), *the ratio is entire (zeros of the two `Φ_b` coincide)*.
This is the formalize-first win: a wide search is replaced by a single named
structural gap. What stays open (not laundered): leg (1); the pentagon's downstream
`A_ω` value; and the capstone `Im 𝔙_q → N_odd` normalization. None is axiomatized.

## Connection to this session's `𝔙_q(5₂)` (PR #4099)

Separately usable for G3: the framing-invariant `𝔙_q(5₂)` bar-odd datum built in
#4099 — `(q−1)³(q+1)(q²+1)(q²−q+1)(q²+q+1)²/(2q⁶)` — is the **intrinsic,
prefactor-free** bar-odd 5₂ carrier that `qbeta_g3_5two_barodd_substrate.py`
flagged as its remaining open step (its raw state-integral bar-split is degenerate,
exp-suppressed by a classical prefactor). Being the 0-framing knot invariant, the
Jones datum is framing-normalized by construction. It is the odd **ingredient**
(correct parity, triple zero at `q=1` matching the `u³` ladder), **not** the
observable `S` — it sits ~10⁶× the `N_odd` scale, exactly as the measurement-limited
value leg (`no_anchor_invariant_realizes_swing`) and the normalization capstone
require. Its use must not cross into that still-open normalization.
