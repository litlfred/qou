# sinh bar-anti-symmetric partner of the unified binomial pattern

**Date:** 2026-05-24
**Branch:** `claude/sinh-bar-antisymmetric-partner-probe-2026-05-24`
**Script:** [`computations/sinh_bar_antisymmetric_partner.py`](../../computations/sinh_bar_antisymmetric_partner.py)
**Witness:** `sinh-bar-antisymmetric-partner.witness.json`
**Status:** EXPLORATORY (audit-only). Identities PROVED symbolically + numerically.

## Headline

PR #1125 / PR #1129 established the **bar-symmetric** trace polynomial

```
P_m(h) := Σ_{j=0}^m C(m+j, 2j) / 2 · h^{2j}
        = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)
        = cosh((2m+1) η_0) / (2 cosh η_0)             at substrate (η_0 = log q_0).
```

This probe defines and verifies the **bar-anti-symmetric partner**

```
Q_m(h) := (q^{2m+1} − q^{-(2m+1)}) / (2 [2]_q)
        = sinh((2m+1) η_0) / (2 cosh η_0)             at substrate.
```

and characterizes its role as the **Coulomb / EM / charge-distinguishing channel** that the canonical `P_avg` projection (per [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md)) discards.

## Proved structural identities

All sympy-exact across `m = 1..9` (54 cells total).

| identity | meaning |
|---|---|
| `P_m(q^{-1}) = P_m(q)` | P bar-SYMMETRIC (even in h) |
| `Q_m(q^{-1}) = −Q_m(q)` | Q bar-ANTI-symmetric (odd in h) |
| `P_m(h) + Q_m(h) = q^{2m+1} / [2]_q` | "right" bar-piece |
| `P_m(h) − Q_m(h) = q^{-(2m+1)} / [2]_q` | "left" bar-piece |
| `Q_m(h)` has only odd-h coefficients | structural h-parity |

The two-piece decomposition is the **q-bar-projection** of `tr_M(σ_1^{2m})` on H_2(q) into its `q ↦ q^{-1}`-fixed (P) and `q ↦ q^{-1}`-sign-reversing (Q) parts.

## Clean per-knot identity at substrate

The probe also notices a clean closed form for the **per-knot EM/strong ratio**:

```
Q_m(h_0) / P_m(h_0)  =  tanh((2m+1) η_0)
```

This **generalizes** the existing framework identity `EM/strong ratio = tanh(ln q_0) ≈ 0.104` for the e⁺e⁻ pair (per [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md)) to a per-torus-knot ratio indexed by `2m+1`:

| knot / particle | 2m+1 | `tanh((2m+1) η_0)` | `Q_m(h_0)` | `P_m(h_0)` |
|---|---:|---:|---:|---:|
| trivial (m=0) | 1 | 0.10396 | 0.05198 | 0.50000 |
| Hopf (m=1, T(2,2)) | 3 | 0.30318 | 0.15822 | 0.52185 |
| W± (m=2, T(2,4)) | 5 | 0.47901 | 0.27137 | 0.56651 |
| Z (m=3, T(2,6)) | 7 | 0.62330 | 0.39638 | 0.63594 |
| H (m=4, T(2,8)) | 9 | 0.73479 | 0.53872 | 0.73315 |
| (m=5, T(2,10)) | 11 | 0.81701 | 0.70460 | 0.86241 |
| (m=6, T(2,12)) | 13 | 0.87556 | 0.90127 | 1.02936 |

(Numerical values use the canonical 50-digit substrate pin `q_0 = 1.10997859555418057528159407960950937799328227995870` from `qou_substrate.constants.Q_50_DIGIT_STR`; `η_0 = log q_0 ≈ 0.10434073`, `h_0 ≈ 0.20906032`.)

So the **EM-channel fraction grows with knot complexity**, asymptotically saturating at 1 as `(2m+1) η_0` becomes large.

## Pythagorean identity (PROVED by sibling commit `596b500f5`)

After this probe landed, a sibling derivation on `main` (commit `596b500f5` — [`p_q_pythagorean_identity.py`](../../computations/p_q_pythagorean_identity.py)) proved a clean **m-INDEPENDENT** structural identity relating `P_m` and `Q_m`:

```
P_m(h)² − Q_m(h)²  =  1 / [2]_q²            (PROVED for all m via sympy trigsimp).
```

(Equivalently `cosh²((2m+1)η)/(2 cosh η)² − sinh²((2m+1)η)/(2 cosh η)² = (cosh² − sinh²)/(4 cosh² η) = 1/(2 cosh η)² = 1/[2]_q²`.)

This says the bar-symmetric and bar-anti-symmetric projections are **categorically orthogonal in the `cosh² − sinh² = 1` sense, scaled by `1/[2]_q²`** — every torus knot `T(2, 2m)` satisfies the same constraint independent of `m`. At substrate `q_0`, `1/[2]_q² ≈ 0.2257` for all `m`.

The sibling also derived a clean closed form for the per-knot EM/strong ratio `Q_m / P_m = tanh((2m+1) η)` from the sinh/cosh definitions, and a one-sided decomposition `P_m − Q_m = q^{-(2m+1)} / [2]_q` (for `m ≥ 1`).

## Why this matters — what the canonical chain throws away

Per [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md), the `P_avg` projection on the canonical chain **keeps** the bar-symmetric kernel (`cos, cosh, Li_2^q`) and **discards** the bar-anti-symmetric companion (`sin, sinh, Φ_q`). For neutral, isospin-symmetric observables (`m_p` alone, `m_n` alone in the symmetric limit), this is correct — those are bar-symmetric by construction.

For **charge-distinguishing observables** (`Δm_{n-p}`, EM self-energy, isospin-breaking widths), the Q-channel is in principle a natural carrier on a `T(2, 2m)` knot: per [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md), `sinh(ln q)` is the Coulomb / electromagnetic channel; the EM Cottingham contribution to `Δm_{n-p}` ≈ 1.293 MeV sits here in spirit.

> **Refined-framing note (added 2026-05-24, post-commit `596b500f5`).** An earlier version of this section claimed that sibling PR #1139's "305 ppm substrate flavor split `Δm/M_N`" IS structurally the Q-channel residual on the Borromean braid `𝓑₃`. The sibling commit `596b500f5` proves `Q_Borromean = 0` (the Borromean Markov trace is purely even in `h`, so its bar-anti-symmetric projection vanishes identically). The bare-Q hypothesis on `𝓑₃` is therefore **falsified**: the 305 ppm split is NOT a `Q_{𝓑₃}` residual.
>
> What survives: the **operator-valued `⋈_K` extension** to unlike-isospin `pn` pairs flagged in PR #1139 introduces a bar-anti-symmetric piece **at the operator level** (not the bare-braid level). The Q-channel framework here characterizes the *kinematic* structure of bar-anti-symmetric residuals; the *carrier* for `Δm_{n-p}` is whatever operator the `⋈_K` extension lifts the projection onto, not the bare `𝓑₃` trace.

## What this probe IS

A **structural characterization** of the bar-anti-symmetric channel that P_avg discards, with:
- closed-form `sinh` representation,
- explicit per-knot EM/strong ratio `tanh((2m+1) η_0)`,
- numerical evaluation at substrate (50-dps mpmath), and
- structural cross-references to existing framework documents that classify sinh as the Coulomb / EM channel.

## What this probe is NOT

A **derivation of `Δm_{n-p}`**. The torus-knot family `T(2, 2m)` doesn't carry the proton/neutron content (`𝓑₃` is the Borromean braid, not a torus knot). What this probe proves is a *parameterized lower bound on the bar-anti-symmetric channel structure*; closing the n-p mass gap from Q requires:

1. The Borromean-side bar-anti-symmetric expansion (not derived here — see [`borromean-markov-trace-closed-form.md`](2026-05-09-borromean-markov-trace-closed-form.md) for the bar-symmetric side; the bar-anti-symmetric analog needs the same treatment).
2. The operator-valued `⋈_K` extension to unlike-isospin `pn` pairs (per the sibling D9 closure audit).
3. A relaxation of `P_avg` projection for charge-distinguishing observables, or an explicit operator that **selects** the Q-channel residual.

These are research-grade follow-ups, not in scope here.

## Cross-references

- **Bar-involution canonical reference:** [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md) §"P_avg vs P_skew" (defines the projection that discards Q).
- **EM/strong channel split:** [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md) (`sinh(ln q) = Coulomb`, `cosh(ln q) = strong binding`, `tanh(ln q) = EM/strong ratio = 0.104` baseline).
- **Pair-creation antisymmetric channel:** [`pair-creation-energy.md`](../../content/quantum-observable-universe/observations/pair-creation-energy.md) ("symmetric binding (cosh) + antisymmetric Coulomb (sinh)").
- **Bar-symmetric partner (P_m closed form):** [`torus-knot-h-expansion-pattern.md`](2026-05-24-torus-knot-h-expansion-pattern.md) (PR #1125; the cosh form proved + applied).
- **Cheat sheet:** [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §4 (the three-avatars synthesis: `Li_2^q ↔ cos_q ↔ cosh`) — Q is the *sinh* avatar.
- **Sibling PR #1139 D9 isospin closure:** [`isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md) (open work that Q can inform).

## Follow-up (NOT in scope)

- Derive the bar-anti-symmetric companion of the Borromean Markov trace (the `𝓑₃`-side Q-analog) and check whether `Δm_{n-p} / M_N` matches its substrate evaluation at the appropriate index.
- Formalize the per-knot identity `Q_m / P_m = tanh((2m+1) η_0)` as a Lean theorem under the `CategoricalHiggsIdempotent` class (it's a one-line algebraic identity, but the `class`-conditional packaging makes it part of the duality-tracker D9 closure surface).
- Test whether the operator-valued `⋈_K` extension (per the sibling D9 audit) projects onto the Q-channel in a controlled way (Section 3 of `isospin-categorical-source.md` flags this as the open mechanism).

## Sympy + mpmath verification summary

- **54 sympy cells** verifying bar-symmetry + decomposition identities across `m = 1..9`.
- **7 mpmath cells** verifying `sinh((2m+1)η_0)/(2 cosh η_0) = (q_0^{2m+1} - q_0^{-(2m+1)})/(2 [2]_q_0)` at 50-dps precision for `m = 0..6`; agreement `< 10⁻³⁰` on every cell.
- Wall time: ≤ 2 s.
