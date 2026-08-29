# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the bulk-rate toolkit is now complete; the derivation route via Toeplitz + Fisher–Hartwig

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-sine-kernel-rate-2026-08-29` · **Tier:**
literature assembly + derivation-route scaffold (formalize-first) · **Discipline:** no fake closure —
this lays out the route and marks the one remaining computation; it does **not** claim the bulk rate is
derived. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

## The one open input, restated

The (CS) margin's bulk `Tendsto` fields need an effective rate `|Var_n(Σ g·η)/n^d − V_g| ≤ C_g n^{−a}`
for the content statistics `Σ|c|, Σc², ΣD²`, which are linear statistics of the BOO descent
determinantal point process (discrete Bessel kernel). The pointwise kernel error is oscillatory
(`bulk_kernel_rate_probe.py`), so the rate must be read off the **integrated** object — the Toeplitz
determinant that the linear-statistic Laplace transform *is* (BOO Remark 1.6; Widom).

## The toolkit is now complete (owner uploads 2026-08-29)

| ingredient | in-corpus | role in the bulk-rate derivation |
|---|---|---|
| descent DPP = Toeplitz determinant | `borodin-okounkov-olshanski2000` (Rem 1.6) | the linear-statistic generating function is a Toeplitz determinant `D_n(φ)` |
| Kac–Akhiezer variance + Berry–Esseen for the Bessel-kernel DPP | `gorbunov2024` | the *continuous* template: variance and rate from the Toeplitz/Borodin–Okounkov identity |
| **Toeplitz asymptotics WITH error term** | **`deift-its-krasovsky2012`** (new) | strong Szegő (smooth φ → exponentially small remainder via Borodin–Okounkov); **Fisher–Hartwig** (jump/arc φ → ALGEBRAIC `n^{−a}` remainder) |
| discrete-sine Toeplitz for arcs | Widom, Indiana U. Math. J. 21 (1971) 271–283 (BOO ref `[41]`) — **journal, not in corpus** | the *discrete-sine* arc case specifically |
| Bessel tail + de-Poissonization | `johansson2001` (Lem 3.9, 3.8) | tail (Olver-free) + fixed-n transfer `C/N²` |
| edge (Airy/Bessel) Painlevé | `tracy-widom` Airy/Bessel (batch) | bounds the oscillatory *edge* part of the remainder |

## The derivation route (formalize-first scaffold)

1. **Generating function → Toeplitz determinant.** The Laplace/exponential transform of the linear
   statistic `Σ g·η` over the descent DPP is a Toeplitz determinant `D_n(φ_g)` with symbol
   `φ_g = e^{s·g(·)}` restricted to the spectral arc `[−2√θ, 2√θ]` (BOO Rem 1.6, Widom). **Status:
   structurally established (BOO), symbol not yet written out for each `g`.**
2. **The symbol has a jump (arc) → Fisher–Hartwig.** The bulk sine kernel corresponds to a symbol
   supported on an arc of the circle; the arc endpoints are **jump (Fisher–Hartwig) singularities**.
   By DIK §"Fisher–Hartwig singularities" the Toeplitz asymptotic then carries an **algebraic** error
   term `n^{−a}` (not the exponentially small Szegő remainder that a smooth symbol gives). **Status:
   the regime is identified (arc ⇒ Fisher–Hartwig ⇒ algebraic rate); the Fisher–Hartwig exponents for
   each `φ_g` are not yet computed.**
3. **Read the variance rate off the second `s`-derivative.** `Var = ∂²_s log D_n(φ_g)|_{s=0}`; the
   `n`-dependence of the Fisher–Hartwig / Borodin–Okounkov remainder gives the exponent `a` and, in
   principle, the constant `C_g`. Cross-check against the measured `θ^{−1}` for `V_A` (`qou-tvok`).
   **Status: the mechanism is standard (Gorbunov does exactly this for the continuous Bessel case);
   transporting it to the discrete arc symbol is the remaining computation.**
4. **De-Poissonize** (Johansson Lem 3.8, `C/N²`) to pass from the Poissonized Toeplitz asymptotic to
   the fixed-n (CS) variance. **Status: citable.**

## What is and is not done

- **Done:** the toolkit is assembled and the route is precise — every arrow above cites an in-corpus
  result (except Widom 1971, a journal article), and the regime is pinned (arc ⇒ Fisher–Hartwig ⇒
  algebraic rate), consistent with the measured `θ^{−1}`.
- **Not done — the one remaining computation:** writing the Toeplitz symbol `φ_g` for each of
  `Σ|c|, Σc², ΣD²`, extracting its Fisher–Hartwig data, and running the DIK/Borodin–Okounkov
  asymptotic to get `(a, C_g)`. This is a genuine multi-step derivation (the discrete analogue of
  Gorbunov's continuous computation), **not** a probe, and it is **not faked here**. It is the content
  of the two open `DescentDPPMarginConvergence.*_tendsto` Lean fields.

No fake closure. Gap `qou-k5r5` **OPEN**, with the route now fully sourced and the remaining step a
well-defined Fisher–Hartwig computation rather than a missing citation.

## Sources

- `deift-its-krasovsky2012` = `library/arxiv-1207.4990v3` (strong Szegő pp. 5–6; Fisher–Hartwig
  section; Borodin–Okounkov identity).
- `gorbunov2024` (`sm10137`), `borodin-okounkov-olshanski2000` (`arxiv-math-9905032v2`),
  `johansson2001` (`arxiv-math-9906120v3`); Widom 1971 (journal, BOO ref `[41]`).
- Probe: `wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py` (pointwise oscillatory → integrated route).

## Cross-references

- Prior batch routing + the `9303139`=Morozov correction: [`2026-08-29-covariance-kernel-M1-k5r5-second-lit-batch-routing.md`](2026-08-29-covariance-kernel-M1-k5r5-second-lit-batch-routing.md)
- Cited-inputs Lean class: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/M1DescentDPPConvergence.lean`
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
