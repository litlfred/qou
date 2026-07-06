# α_EM Habiro element — q-difference / root-of-unity structure

**Date:** 2026-06-01
**Probe:** [`alpha_em_q_difference_fourier.py`](../../computations/alpha/alpha_em_q_difference_fourier.py)
→ `alpha-em-q-difference-fourier.witness.json`
**Goal arm:** α_EM canonical derivation.
**Transfers:** the Q_β q-difference / Fourier / root-of-unity machinery
(PRs #1593/#1602/#1622) to the α_EM Habiro element.
**Status:** exact characterization. Sharpens the α_EM modular target; the
open *derived form* (alpha-em ledger) is unchanged.

---

## TL;DR

Applying the Q_β machinery to the α_EM Habiro element
`H = [2]_q·(1−h²α) = (q+q⁻¹)(1−(q−q⁻¹)²α)` gives exact structure:

- **H is a fixed point of the bar involution** `q↦q⁻¹` — an exact
  algebraic fact over the **formal fibre variable** (no reality assumed).
  This is the clean charge-conjugation-symmetric sector PR #1602 said the
  Q_β scaling map `f` must occupy. **α_EM is the clean case (a bar fixed
  point); Q_β's `Δtr_M` is NOT a bar fixed point — it carries a
  bar-anti-invariant part to cancel.**
- **H(ζ_4) = 0** — a ZERO at the 4th root of unity, the exact dual of
  Q_β's **POLE** at ζ_4 (PR #1622). Same q-difference machinery, dual
  modular node.

## Level discipline (fibre vs observable)

Per AGENTS.md *"Im(q) at fibre vs observable level"*: this probe works
at the **fibre / categorical level** — `q` and `α` are **formal**, with
`Im` **unconstrained**, and the operative symmetry is the **bar
involution `q↦q⁻¹`** (the framework/tower involution structure), NOT a
reality assumption. The root-of-unity spectrum below is exact in the
**cyclotomic field** `ℚ(ζ_d)` with `α` a formal parameter. The
**observable component is real ONLY at the archimedean `q₀` evaluation**
(the h-Taylor / truncation step), where `Im(q₀)=0` is the verified
`lusztig_q_0_imaginary_part_zero` constraint. Forcing `q` or `α` real at
the fibre level would conflate the two levels — a registered audit flag.

## The root-of-unity spectrum (Fourier modes of σ_q)

| d | `H(ζ_d)` (exact) | reading |
|---|---|---|
| 1 | `2` | classical → α/(4π) leading term |
| 2 | `−2` | bar / charge-conjugation mode |
| 3 | `−3α − 1` | cyclotomic ℚ(ζ_3) |
| 4 | `0` | **modular node (ZERO)** |
| 5 | `√5·α + (√5−1)/2` | cyclotomic ℚ(ζ_5), √5 field constant |
| 6 | `3α + 1` | |
| 8 | `√2·(2α+1)` | cyclotomic ℚ(ζ_8), √2 field constant |

The spectrum is exact and the cyclotomic-field constants (`√5` at ζ_5,
`√2` at ζ_8) appear cleanly — the modular data of the α_EM element.

## Why α_EM is the clean template

- **`[2]_q = q + q⁻¹` is manifestly bar-symmetric** → `H` is a fixed
  point of the bar involution `q↦q⁻¹` (witness assertion
  `alpha_em_habiro_is_bar_involution_fixed_point`). No bar-even
  extraction needed (unlike Q_β, where `Δtr_M` mixed sectors).
- **`H` is a Laurent polynomial (no poles)** → finite, exact
  root-of-unity spectrum. Its h-Taylor recursion `c_k = c_k^{[2]_q} −
  α·c_{k−2}^{[2]_q}` is the mode generator, and the `c_k` are **α-linear
  rationals** — q₀-stable, NOT q₀-dependent near-matches (contrast the
  Q_β `c_k` flip-flop). q₀ truncation error at k≤8 is `4.4×10⁻¹²`.

## Dual picture: Q_β pole ↔ α_EM zero

| | Q_β (PR #1622) | α_EM (this probe) |
|---|---|---|
| bar-symmetry | mixed (not a bar fixed point) | **bar-involution fixed point** |
| ζ_4 special value | **POLE** (residue ∓i/2) | **ZERO** |
| `c_k` stability | q₀-dependent near-matches | q₀-stable α-linear rationals |
| object type | rational (Δtr_M) | Laurent polynomial |

The two are dual instances of one q-difference structure. α_EM's
cleanliness (bar-even, polynomial, q₀-stable) is *why* its next-order
form was identifiable as a Habiro element (#1511) while Q_β's was not.

## What this sharpens (and what stays open)

**Sharpens:** any derivation of the α_EM next-order form must reproduce
the **`H(ζ_4)=0` modular node** and the exact bar-even root-of-unity
spectrum. This is a hard structural target, parallel to Q_β's `∓i/2`
modular residue.

**Open (unchanged):** the α_EM next-order *derived form* — the alpha-em
ledger has the empirical `[2]_q·(1−h²α)` candidate at ~0.31 ppb but the
RT-2-loop structural justification (Bring zero-mode / Habiro framing) is
still open. This probe does not close it; it adds the modular constraint.

## Discipline

Exact symbolic; both assertions pass; **no fitted form; no closure of the
derived form.** `h = q−q⁻¹` (Hecke differential) kept distinct
from the spinor rate `\check{q} = q^{1/2}` (= Habiro literature
name `u`, retired 2026-06-04) and the ladder `u_ladder = b·ℏ²`
per `notation-collisions.md §\check{q}`.

## Cross-references

- Q_β q-difference spectrum (the template): [`2026-06-01-habiro-q-difference-fourier-spectrum.md`](2026-06-01-habiro-q-difference-fourier-spectrum.md)
- Q_β mode solve: [`2026-06-01-habiro-q-difference-mode-solve.md`](2026-06-01-habiro-q-difference-mode-solve.md)
- Q_β ladder bridge: [`2026-06-01-habiro-ladder-bridge.md`](2026-06-01-habiro-ladder-bridge.md)
- Eigenphase ≠ f (bar-even constraint): [`2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md`](2026-06-01-qbeta-eigenphase-not-f-falsified-at-u1.md)
- α_EM Habiro Taylor (the prior, Taylor-only treatment): `alpha_em_habiro_taylor_investigation.py`
- α_EM ledger: [`docs/coordination/alpha-em.md`](../coordination/alpha-em.md)
