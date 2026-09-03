# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the regime structure, and why BDJ is the *edge* (not the global variance rate)

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bulk-sine-kernel-rate-2026-08-29` · **Tier:**
literature synthesis + primary-source regime analysis · **Discipline:** no fake closure; this maps the
regime structure precisely and states honestly that no single existing paper hands over the (CS)
variance rate. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

## The quantity the (CS) margin needs, precisely

`V_A(θ) = Var(Σ|c|)/θ²`, the variance of a **global** linear statistic (the sum over *all* boxes) of
the Poissonized Plancherel measure, and its convergence to `8/π²` with a rate. This is a **Kerov-CLT
(global) object**, governed by the whole diagram — **not** an edge object.

## Two different regimes — do not conflate them

| regime | statistic | limit law | in corpus |
|---|---|---|---|
| **edge** | `λ₁` (longest increasing subsequence), largest part | Tracy–Widom (Airy), `θ^{1/6}` scale | **`baik-deift-johansson1999`** (new), `tracy-widom` Airy, DIK §11 |
| **global / Kerov CLT** | linear statistics `Σ f(content)` (`Σ\|c\|`, `Σc²`, `ΣD²`) | Gaussian, `θ^{1/2}`–`θ` scale | `ivanov-olshanski2003` |

`baik-deift-johansson1999` (JAMS 1999) — the paper the owner just supplied — is the **edge** result:
`(λ₁ − 2√θ)/θ^{1/6} → TW`, with moment convergence, via the Riemann–Hilbert double-scaling analysis of
the Plancherel Toeplitz determinant. It is foundational and supplies the **RH double-scaling method**
and the **edge half** of the Toeplitz asymptotic — but it does **not** state the global
linear-statistic variance rate. Confirmed from BDJ's own title/results and from `qou-tvok`'s
observation that the `V_A` remainder is `θ^{−1}` (a global-fluctuation scale), not `θ^{1/6}` (edge).

## The regime structure of the (CS) variance rate (what each ingredient gives)

1. **Leading variance `V_A = 8/π²`:** the IO Kerov CLT mode sum `Σ_k Â_k²/k` — **cited**
   (`ivanov-olshanski2003`; derived in PR #5969). IO proves the first and second **moments** of each
   Chebyshev mode converge (§ read at source).
2. **Qualitative variance convergence `V_A(θ) → 8/π²`:** IO gives it **mode-by-mode**; the full sum
   for the *non-smooth* test function `|x|` additionally needs **uniform high-mode tail control** (the
   `|x|` cusp spreads over all modes). So the qualitative `DescentDPPMarginConvergence.*_tendsto`
   fields are *IO + one uniform-tail argument*, not IO alone. Partly citable, one analytic gap.
3. **The rate (`θ^{−1}`, the explicit finite-n threshold `N₀`):** the finite-size correction to the
   Kerov CLT for non-smooth statistics. This is the second `s`-derivative of the **full** Plancherel
   Toeplitz-determinant asymptotic, which combines a **bulk** part (strong Szegő / Widom-arc,
   `deift-its-krasovsky2012` + Widom 1971) and an **edge** part (BDJ / double-scaling,
   `baik-deift-johansson1999` + DIK §11). The `qou-tvok` annulus probe (honest negative) showed the two
   regions *compensate*, so both contribute and neither alone gives the rate.

## Honest bottom line: the toolkit is complete; the last step is original research

With this upload the corpus now holds **every** ingredient of the derivation — IO (leading + modes),
BOO (descent DPP = Toeplitz), Johansson (tail + de-Poisson), Gorbunov (Kac–Akhiezer continuous
template), DIK (Toeplitz-with-error + the double-scaling identification of the Plancherel determinant),
BDJ (edge double-scaling + RH method), TW Airy/Bessel (edge kernels) — plus the one journal reference
(Widom 1971) for the bulk-arc piece.

**No single further paper closes it.** The (CS) variance rate for `Σ|c|, Σc², ΣD²` under Poissonized
Plancherel + de-Poissonization is a *specific* quantity that no cited paper states directly: BDJ gives
`λ₁`, IO gives the leading variance and the modes, DIK/Gorbunov give the Toeplitz machinery, but
**assembling them into the global variance rate for these non-smooth statistics is an original
Riemann–Hilbert computation.** That computation is well-defined and fully sourced; it is genuine
research, and — per the anti-laundering discipline — it will **not** be fabricated as a "derivation"
here. `qou-tvok` gives the *measured* `θ^{−1}`; the *rigorous* exponent+constant is the open work.

## Status of `qou-k5r5`

Gap **OPEN**, now with the regime structure fully mapped: leading variance **cited**, qualitative
convergence **IO + uniform-tail**, rate **= the assembled bulk+edge Toeplitz double-scaling analysis**
(all ingredients in corpus, the assembly is research). Leading margin **proved**; tail and
de-Poissonization **cited**. The honest terminus is unchanged in kind — an original RH computation —
but the toolkit for it is now complete and every piece is named.

## Sources

- `baik-deift-johansson1999` = `library/arxiv-math-9810105v2`; `baik2022kpz` = `library/arxiv-2206.14086v3`;
  `baik-rains2001` = `library/arxiv-math-9910019v1`.
- `ivanov-olshanski2003` (moment convergence, `library/arxiv-math-0304010v1`); `deift-its-krasovsky2012`
  (§11 double-scaling); Widom 1971 (bulk arc, journal).

## Cross-references

- Predecessor (double-scaling correction): [`2026-08-29-covariance-kernel-M1-k5r5-derivation-attempt-double-scaling.md`](2026-08-29-covariance-kernel-M1-k5r5-derivation-attempt-double-scaling.md)
- Cited-inputs Lean class: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/M1DescentDPPConvergence.lean`
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
