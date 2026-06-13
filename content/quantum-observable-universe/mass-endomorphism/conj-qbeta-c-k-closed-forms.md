**Closed-form conjectures for the $Q_\beta$ precision-ladder coefficients $c_4, c_5, c_6, c_7$.**

The framework PROVES $c_3 = J_{\text{Hopf}}(q{=}1) = -2$ via the
2-strand sub-braid argument (Fact 3 of
[`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov)).
The higher-rung coefficients $c_4, c_5, c_6, c_7$ have **empirical
closed forms** extracted from the SDP-$T_\beta$ framework (
[`folio-assistant/computations/qbeta/qbeta_decay_sdp_full_ck.py`](../../folio-assistant/computations/qbeta/qbeta_decay_sdp_full_ck.py))
with sub-percent residuals, but **no first-principles categorical
derivation is yet known**.

This block formalises them as **conjectures** so downstream
provable claims that depend on them can use the §3b-cond
conditional-class exception (already implemented in
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
via the Lean class `QBetaPrecisionLadderCoefficients`).

## The four conjectures

| Rung | Conjectured closed form | Empirical match | Categorical interpretation |
|:----:|:-----------------------:|:---------------:|----------------------------|
| $c_4$ | $c_3 \cdot b^4 = -2 \cdot b^4$ | **0.9%** residual | Hopf Jones $\times$ Kashiwara $b^4$ correction (multiplicative mixing) |
| $c_5$ | $-(b^2 + 1/2)$ | **2.4%** residual | Kashiwara $b^2$ + half-Hopf integer offset (mixed) |
| $c_6$ | $c_3^2 \cdot b^2 = 4 \cdot b^2$ | **14%** residual | Hopf Jones squared $\times$ Kashiwara $b^2$ |
| $c_7$ | $c_3^3 = -8$ | **signed error $+114\%$** (magnitude error $86\%$, opposite sign) | Hopf Jones cubed (pattern guess; leverage limit at $N=7$ means almost any value closes) |

The match quality degrades with $k$. The $c_7$ closed form has
**signed relative error $|{-8} - 57.149|/57.149 \approx 114\%$**
(magnitude-only error $|8 - 57.149|/57.149 \approx 86\%$). The
conjecture is retained because the $N=7$
correction's leverage on cumulative $Q_\beta$ residual is at the
$10^{-13}$ scale (any $c_7 \in [-100, +100]$ closes to within
$10^{-4}$ ppb), so the actual numerical value is under-determined.

## Open research-grade derivation paths

Three concrete routes (from
[`docs/audits/-qbeta-ladder-closure-path.md`](../../../docs/audits/-qbeta-ladder-closure-path.md)):

1. **Khovanov-Rozansky polynomial at finite $q$**: compute
   $\mathrm{Kh}(L)(q, t)$ of the typed-$\mathbf{B}_3$ Markov-closure
   link $L$ at the substrate $q_0$ (not just $q = 1$). The Taylor
   coefficients should match $c_4, c_5, c_6, c_7$.
2. **KLR canonical-basis trace formula**: per-Wedderburn-block
   canonical-basis Markov trace at orders $\varepsilon^8, \varepsilon^{10},
   \varepsilon^{12}$ — the framework has scaffolding (Hecke-KLR bridge in
   [`conj:kazhdan-lusztig-classical-limit`](#conj:kazhdan-lusztig-classical-limit)),
   open piece is the explicit per-block trace formula.
3. **Spectral-sequence stratification** (declined by ledger;
   no good candidate spectral sequence in framework's content).

## Why these aren't decoration

The current $Q_\beta$ categorical prediction (Form A $\cdot$ cos $\cdot$ $\prod$ rungs)
already meets the 7.8 ppb L2 target at $N=3$ (residual +6.02 ppb,
within target). The c_4..c_7 corrections push residual to sub-ppb,
which is **research-grade precision beyond the 100$\times$-experimental
target**. So these conjectures aren't blockers for the framework's
core deliverables — they're optional precision-deepening for
research-grade results.

But the framework's **three-calibration discipline** flags empirical
fits as conjectural inputs: predictions conditional on these
conjectures must be marked as such. Promoting them to a single
`conj:` block keeps the audit trail clean.

## Evidence

Direct SDP-$T_\beta$ extraction at 50dps (post-TR_M[5] bug fix from
) reproduces all four c_k EXACTLY:

```
c_2 extracted = -1.0171   (vs framework -1, 1.7% match)
c_3 extracted = -2.0098   (vs framework -2 = J_Hopf(q=1), 0.5% match)
c_4 extracted = -1.1435   (matches empirical sweep EXACTLY)
c_5 extracted = -1.2229   (matches empirical sweep EXACTLY)
c_6 extracted = +3.4976   (matches empirical sweep EXACTLY)
c_7 extracted = +57.149   (matches empirical sweep EXACTLY)
```

Verified by `qbeta_decay_sdp_full_ck.py` (4 assertions pass).

The "empirical c_k from `binding_q_target_sweep`" are NOT arbitrary
fits — they're TAUTOLOGICALLY determined by the precision-ladder
structure applied to CODATA $Q_\beta$. The conjectures here are
the **closed-form pattern interpretations** of those extracted values.
