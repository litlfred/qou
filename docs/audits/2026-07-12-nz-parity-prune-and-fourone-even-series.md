# NZ parity prune + the exact 4₁ even deformation series (PR #3622)

**Date:** 2026-07-12 · **Branch:** `claude/ck-qbeta-closure-avenues-mu8471`
**Scope:** the c₃ bar-odd `S` frontier. One Lean-proved structural prune +
one geometric-exact probe. No c_k value proposed; nothing wired
(flip-flop guard §8). Owner steer: "work on frontier", "ok to duplicate —
different context", "review lit".

## 1. The prune (Lean, sorry-free)

[`QOU/Knot/NeumannZagierParity.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/NeumannZagierParity.lean):
an even polynomial has vanishing odd coefficients (generic `CommRing`,
two-torsion-free via `[NoZeroDivisors] [NeZero 2]`); the
`NeumannZagierEvenPotential` hypothesis class carries NZ85's parity (v(u)
odd ⇒ potential even) with **no fabricated instance**; derived
`no_cubic_rung` / `no_odd_rung`.

**Consequence (scope-(b), invariant = parity):** the geometric NZ series of
a one-cusped deformation has **no u³ (or any odd) rung**. The 2026-07-11
NZ-u³ proposal (posted on #3562 by this session) is killed twice over: it
targeted a coefficient that vanishes identically, and it conflated the
ladder variable `u_ladder = b·ℏ_q²` with the NZ deformation variable.
Self-correction posted on #3562.

## 2. The probe (geometric-exact, convention-free)

[`qbeta_nz_even_series_fourone_probe.py`](../../computations/probes/qbeta_nz_even_series_fourone_probe.py)
→ [`qbeta-nz-even-series-fourone.witness.json`](../../computations/probes/qbeta-nz-even-series-fourone.witness.json)
(4/4 assertions, 60 dps, exit 0). From the CCGLS A-polynomial of 4₁ alone
(quadratic in L; analytic branch through the double root at the complete
structure via tracked `sqrt(disc)/u`; Cauchy/FFT coefficient extraction on
`|u| = 0.06`, closure defect 3e-62):

| quantity | numeric (40 dps in witness) | exact recognition |
|---|---|---|
| τ = v₁ | −1.7320508…·i | **−i√3** — the ℚ(√−3) cusp modulus (matches merged `barOdd(ω)² = −3`) |
| v₃ | −0.5773502…·i | **−i√3/3** |
| v₅ | −0.2213176…·i | −23·i√3/180 (hand-recognized; witness carries the numeric) |
| v₀, v₂, v₄, v₆ | < 2e-54 | **0** — v is odd (NZ85, corroborated from the A-polynomial with no sign conventions) |
| Φ₄/Φ₂ ratio v₃/(2τ) | 0.1666…(59 digits) | **1/6** — convention-free next-order NZ correction: `corr(u) = 1 ± u²/6` |

Method note (recorded because the naive version fails): Newton continuation
from `L(0) = −1` hops branches — the complete structure is a **double root**
where the geometric branch meets its conjugate, and the principal sqrt flips
between rays. The tracked-sqrt construction is the correct analytic branch;
its closure around the contour is asserted.

## 3. Anchor evaluation (report-only, scope-(a))

Against the #3573 coordinates (`z_ED = ln q₀`, `HA = 2 ln q₀`) and S-leak
targets, the exact u⁴ correction `1 ± u²/6`:

| anchor · ray | miss before → after | direction |
|---|---|---|
| muon (z_ED), real-u | 2.54% → **2.36%** | toward S |
| muon (z_ED), imag-u | 2.54% → 2.72% | away |
| proton (HA), real-u | 4.08% → **3.38%** | toward S |
| proton (HA), imag-u | 4.08% → 4.78% | away |

Reading: the **real-u ray improves at both anchors but does not close** —
the even NZ series converges toward S while leaving a ~2.4%/3.4% residual
at fourth order. Scope-(a): this constrains magnitudes of the geometric
even channel; the odd/archimedean channel (KC17: irreducibly archimedean;
Φ_b phase, 1-loop torsion) remains the open carrier of the residual. It
also *selects the real-u ray* over the imaginary one as the geometric
embedding that cooperates with S — a new, falsifiable orientation datum for
the #3562/#3544 argument searches.

## 4. Literature verification status

A background verification agent (NZ85 lemma numbers, published 4₁ NZ
coefficients, A-polynomial source conventions, parity of odd-in-u quantum
corrections) is being run; its verdicts will be appended here before merge.
Everything above is machine-computed from the stated A-polynomial and does
not depend on the pending citations; the NZ85 attribution of v-oddness is
corroborated numerically in §2 independent of the citation.

## 5. Non-derivation disclaimer

`1/6`, `−i√3`, `−i√3/3` are exact **geometric** constants of the 4₁
deformation variety — not Q_β ladder coefficients. No identification with
c_k is made or implied; the anchor comparison is a magnitude probe of the
sibling's u² law one order deeper.
