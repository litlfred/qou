# Saddle-offset zero-location — what is q≈0.08, does q=1 survive, and the c₃ hook (`qou-q86o`)

**Date:** 2026-08-02
**Branch/PR:** `claude/qou-q86o-offset-zero-location-2026-08-02` / #4583
**Bean:** [`qou-q86o`](../../.beans/qou-q86o--gap-saddle-offset-origin-centred-only-at-q1-leg-un.md)
**Kind:** exploratory numerical probe + sorry-free structural lemma (derive-then-check, anti-fit, honest-negative)
**Parents:** #4578 (saddle-offset probe), #4577 (Lean gate `offset = 0 ⇔ ι-fixed`), #4573 / `qou-fk19` (red-flag ledger)
**Steering:** coordinator (connect Q3 to the c₃ Borel/fibre program — Fantini–Wheeler reframe [`2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`](2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md), AGENTS.md Im(q) fibre/observable banner)

## The open leg under test

The merged probe #4578 confirmed the DT-limit legs of the owner's saddle-vector
picture (5₂ ι-odd offset `o(0) = c⁺(0)−c⁻(0) = 1`, amphichiral 4₁ `= 0`) but
left one leg open: the owner says the saddle is **origin-centred only at q = 1**,
yet the certified offset `o(q) = c⁺(q) − c⁻(q)` crosses zero at a **small finite
q ≈ 0.08**, and the series diverge at q = 1. This probe answers three honest,
open-outcome questions.

## Method — certified corpus only, no recompute

[`computations/probes/saddle_offset_zero_location_probe.py`](../../computations/probes/saddle_offset_zero_location_probe.py)
imports the certified 5₂ Stokes sandwich
([`qbeta_g3_5two_stokes_sandwich.py`](../../computations/probes/qbeta_g3_5two_stokes_sandwich.py),
K1/K2/K3 ✓) **unchanged** and reads the same off-diagonal series #4578 used. It
avoids every `qou-fk19` red-flag (no `v_offset(q)` ODE, no `q = exp(2πiτ)` pin,
no invented θ-function). Expectations E1–E4 were **locked before** the compute.

## Findings

### Q1 — what is q ≈ 0.08? A stable DT-series root, NOT a substrate quantity.

The offset series (exact `Fraction` coefficients) is
`o(q) = 1 − 9q − 28q² + 25q³ + 126q⁴ + …`. Its smallest positive real root:

| truncation order N | q*(N) |
|---|---|
| 2 | 0.087365 |
| 3 | 0.088614 |
| 6 → 18 | **0.089311** (flat) |

**q\* is truncation-stable** — it converges by N = 6, spread over N ≥ 3 is
`7.0×10⁻⁴`. It is pinned by the quadratic balance `1 − 9q − 28q² = 0`, whose root
is the closed form `q_quad = (−9+√193)/56 = 0.087365` (the higher-order terms are
`O(10⁻²)` at q ≈ 0.09, shifting the root by only `1.95×10⁻³`).

**But q\* is NOT a substrate quantity.** Derive-then-check against every natural
candidate (expectation E2, locked before compute):

| candidate | value | rel. err vs q\* |
|---|---|---|
| q₀ − 1 | 0.109979 | 18.8 % |
| ℏ_q = 1 − 1/q₀ | 0.099082 | **9.9 %** (closest) |
| ℏ_q² | 0.009817 | 810 % |
| 1/q₀ | 0.900918 | 90 % |
| series radius (root test) | ~0.57–0.63 | 84 % |

The closest, ℏ_q, still misses by ~10 %. Root-of-unity moduli are all `|ζ| = 1`,
irrelevant. **q\* is the DT expansion's own convergence-region root**, set by the
low-order Stokes coefficients `{9, 28}` (which encode the `{3,4}` datum) — it
carries no independent substrate meaning. Honest negative on Q1.

### Q2 — is q = 1 recoverable? Only as the trivial bar-fixed-point vanishing.

The certified `o(q) = c⁺(q) − c⁻(q)` has constant term `o(0) = 1 ≠ 0`. A
genuinely **bar-covariant** object — one antisymmetric under the bar involution
`q ↔ q⁻¹` (which acts on Laurent coefficients by `n ↦ −n`) — satisfies
`g(1/q) = −g(q)`, which **forces its constant coefficient to vanish**
(`g(0) = −g(0) ⇒ g(0) = 0`). Since `o(0) = 1 ≠ 0`, the certified offset is a
**cross-chirality difference at the same q**, NOT a `q ↔ q⁻¹`-antisymmetric
object.

**Consequence.** The "origin-centred only at q = 1" leg would need the offset to
vanish at the bar-fixed point `q = q⁻¹ = 1`. That mechanism (any genuinely
bar-odd object → 0 at q = 1) is real but **trivial** — it is #4577's gate applied
to `q` itself — and it does **not** apply to the certified DT offset, which is
not bar-odd-in-q. So the *specific* claim "the DT saddle-offset vanishes **at**
q = 1" is **refuted as an independent reading** [scope-(a)]: the DT offset lives
at q → 0 with its own root at q\* ≈ 0.089; q = 1 is a different locus for a
different object.

This is formalized sorry-free (see §Lean below).

**Two-level reconciliation (fibre vs archimedean).** Per the coordinator and the
AGENTS.md Im(q) banner, the owner's "centred at q = 1" is most naturally a
**fibre-level** statement: q = 1 is the bar-fixed point of the *formal* q, where a
bar-covariant Habiro/fibre element vanishes **by construction**. That is
consistent with the picture — but it is a **different object** from the
**archimedean** q → 0 DT series this probe measures. So the q ≈ 0.08 crossing
does **not refute** a fibre-level q = 1 centring; it is an archimedean-series
feature. The two levels do not conflict — they are different objects. The Lean
lemma below is precisely the *archimedean-coefficient* obstruction.

### Q3 — c₃ hook: offset and c₃ sit on opposite sides of the Borel transform.

Direct evaluation of `o(q)` at the substrate q₀ ≈ 1.1097 **diverges** (partial
sums `−43, +559, −1.3×10⁴, +6.6×10⁵` through order 18; q₀ > 1 is far outside the
radius). So a c₃ hook via direct q₀ evaluation is inaccessible, and the q → 0
datum `o(0) = 1` has no clean/derived relation to `Q_β c₃ = −2` (`o(0)/c₃ =
−0.5`, a bare ratio, **not** fitted, **nothing wired**).

Following the steering to engage the Borel program: c₃ is a coefficient of the
**divergent perturbative series Φ_5₂**, which is Borel–Laplace summable
(Fantini–Wheeler 2024, [arXiv:2410.20973](https://arxiv.org/abs/2410.20973);
[`2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`](2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md)).
The **offset**, by contrast, is built from the certified Stokes **sandwich** —
the **resummed** Stokes constants `S±(q)`, i.e. the `Z[q^±]` *output* of
Borel–Laplace, not the divergent *input*. The offset coefficients grow
**geometrically** (finite radius ≈ 0.6), not factorially:

| model | fit | R² |
|---|---|---|
| geometric `log\|aₙ\| ~ 2.38 + 0.464 n` | radius ≈ 0.63 | 0.887 |
| factorial `log\|aₙ\| ~ 3.44 + 0.146 (n ln n)` | Borel/Gevrey-1 | 0.869 |

**Honesty caveat:** with only 18 oscillating-sign coefficients the growth-model
discrimination is *weak* (0.887 vs 0.869). The decisive argument is
**structural, not the fit**: the offset is a difference of *resummed Stokes
constants*, categorically on the resummed side of the Borel transform, whereas
c₃ is a coefficient of the *divergent* Φ. **Opposite sides ⇒ no direct
Borel-level offset↔c₃ identity.** Honest negative on Q3. Nothing is wired to the
Q_β ladder or any dashboard.

## Lean — the archimedean-coefficient obstruction (sorry-free)

[`QOU/QBeta/SaddleOffsetBarGrade.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SaddleOffsetBarGrade.lean)
(verified `lean`-direct against restored `lake-cache/qou-v4-24-0` oleans:
**exit 0, sorry-free**; generic `{R} [CommRing R] [Invertible 2]`, concrete over
`ℤ`; reuses the certified `chiralityOdd 4 3 = 1` datum from
`FiveTwoDTSpectrumSplit`, not a fresh number):

- `barAntisym_const_zero` — a `q ↔ q⁻¹`-odd Laurent object has zero constant
  coefficient (the bar-fixed-point vanishing mechanism the q = 1 leg would need).
- `certified_offset_not_barAntisym` (headline) — no Laurent object whose constant
  coefficient equals the certified offset datum (`= 1`) can be bar-odd-in-q; so
  the certified offset's q = 1 vanishing is **not** delivered by that mechanism.
- `barAntisym_nontrivial` — anti-vacuity: `g n = n` is genuinely bar-odd (so the
  hypothesis is satisfiable, the distinction is real).

This distinguishes the **chirality grade** (#4577's gate: offset is odd under
`c⁺ ↔ c⁻`) from the **q ↔ q⁻¹ Laurent bar-grade** (which the offset is **not**
odd under) — the exact conflation #4577's narrative made by *modelling* the
chirality swap as the bar involution.

## Verdict (scope-labelled, honest)

- **q ≈ 0.08** = q\* ≈ 0.08931, a truncation-stable root pinned by the quadratic
  balance `(−9+√193)/56`; it is the DT series' **own** convergence-region root,
  **not** a substrate quantity (closest miss ℏ_q at ~10 %). No substrate meaning.
- **q = 1 does not survive** as an independent placement of the DT offset
  [scope-(a) refutation]: the certified offset is a cross-chirality difference
  (`o(0)=1≠0`), not bar-covariant, so its q=1 vanishing is only the trivial
  bar-fixed-point one — a *different object*. The owner's picture is recoverable
  only at the **fibre** level (formal-q Habiro element), which the q → 0 DT
  series neither tests nor refutes.
- **c₃ relation: absent.** Offset (resummed Stokes constants, geometric growth)
  and c₃ (coefficient of the divergent Φ) sit on opposite sides of the Borel
  transform. No identity; nothing fitted; nothing wired.

Scope-(a) throughout: this **narrows the reading** of the picture (where the
offset-zero sits, which grade the offset lives in, which side of Borel it is on)
— it invokes no proved invariant to exclude an ingredient, derives no physical
number, wires no `c_k`, inverts no `Q_β`/CODATA.

## Anti-numerology guards respected

Definitions + `expected` assertions locked before the compute; E1–E4 all met
(exit 0). Reuses the certified sandwich (no recompute); avoids all `qou-fk19`
red-flags. No fit; no `c_k` wired; no axiomatization; nothing wired to any
dashboard / the Q_β ladder.
