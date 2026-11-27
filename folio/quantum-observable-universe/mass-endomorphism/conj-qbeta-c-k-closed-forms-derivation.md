## Derivation paths

Three formal derivation paths stand open:

1. **Khovanov–Rozansky polynomial at finite $q$**: Compute $\mathrm{Kh}(L)(q, t)$ for the typed-$\mathbf{B}_3$ Markov-closure link $L$ at the aether $q_0$ (not merely $q = 1$). The Taylor coefficients should return $c_4, c_5, c_6, c_7$.
2. **KLR canonical-basis trace formula**: Calculate the per-Wedderburn-block canonical-basis Markov trace at orders $\varepsilon^8, \varepsilon^{10}, \varepsilon^{12}$. The explicit per-block trace formula is required.
3. **Spectral-sequence stratification**: Currently declined; the framework lacks a suitable candidate spectral sequence.

## Comparison with extracted values

| Rung | Conjectured closed form | Residual against extraction | Categorical interpretation |
|:----:|:-----------------------:|:---------------:|----------------------------|
| $c_4$ | $c_3 \cdot b^4 = -2 \cdot b^4$ | **0.9%** residual | Hopf Jones $\times$ Kashiwara $b^4$ correction (multiplicative mixing) |
| $c_5$ | $-(b^2 + 1/2)$ | **2.4%** residual | Kashiwara $b^2$ + half-Hopf integer offset (mixed) |
| $c_6$ | $c_3^2 \cdot b^2 = 4 \cdot b^2$ | **14%** residual | Hopf Jones squared $\times$ Kashiwara $b^2$ |
| $c_7$ | $c_3^3 = -8$ | **signed error $+114\%$** | Hopf Jones cubed |

Match quality degrades at higher $k$. For $c_7$, the signed relative error is approximately $114\%$ (magnitude error $86\%$). One retains the conjecture because the $N=7$ correction's leverage on the cumulative $\mathfrak{Q}_\beta$ residual operates at the $10^{-13}$ scale. Any $c_7 \in [-100, +100]$ closes the gap to within $10^{-4}$ ppb, leaving the numerical value highly under-determined.

## Precision

The $+6.02$ ppb residual at $N=3$ recorded for this ladder, and the sub-$1$ ppb
figures the higher rungs ($c_4$ to $c_7$) reach, are **not** a current statement
that the $100\times$ accuracy target for $\mathfrak{Q}_\beta$ is met. Both are
properties of a cell the framework has since retired, and they are quoted here as
a record of that cell, not as a prediction.

Two scopings apply, and neither was present when those figures were first
written:

1. **Loop parameter.** The ladder above was built with the auxiliary loop parameter
   $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$, whereas the canonical Markov parameter is
   $z = q^3/(q^2+1)$. No counterpart of the $c_k$ ladder at $z = q^3/(q^2+1)$ has
   yet been derived.
2. **Functional.** The single-wrap baseline underlying that ladder evaluates at
   $z = 1$ (the coordinate sum), which is not a root of the two-row Markov
   faithfulness condition $y_{(1^3)}(z) = 0$.

Against the $7.797$ ppb target, the bare Markov-trace evaluation at $z = q^3/(q^2+1)$
with **zero** $c_k$ rungs sits at $1.668\times10^{8}$ ppb — a miss of
$2.139\times10^{7}$ relative to target — whereas the $+6.02$ ppb figure above
evaluates the five-rung $z_{\mathrm{aux}}$ ladder on the $z = 1$ coordinate-sum cell.
The two numbers evaluate distinct functionals and must not be conflated.

Under the three-calibration discipline, the higher rungs are calibration-anchored
fits: they encode the CODATA datum they are matched to, so they are a calibration
record rather than a prediction, and any downstream claim relying on them must
declare that dependency. 


## Evidence

A 50-decimal-place SDP-$T_\beta$ sweep at $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$ recorded the following numerical extractions:

```text
c_2 extracted = -1.0171   (vs framework -1)
c_3 extracted = -2.0098   (pre-reanchoring value; see anchor table below)
c_4 extracted = -1.1435   (empirical sweep)
c_5 extracted = -1.2229   (empirical sweep)
c_6 extracted = +3.4976   (empirical sweep)
c_7 extracted = +57.149   (empirical sweep)
```

**Anchor dependence of $c_3$.** At $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$, re-evaluating $c_3$ across the aether anchors gives:

| anchor | $c_3$ at $z_{\mathrm{aux}} = \sqrt{q}/(q+1)$ |
|---|---|
| proton ($m_{\mathfrak{p}}/m_e$ anchor) | $-2.06934257711516783787971951725$ |
| muon, CODATA 2022 | $-2.019860311874005$ |
| muon, CODATA 2018 | $-2.020200233$ |

With the eigenphase evaluated instead at $z = q^3/(q^2+1)$ on the proton anchor, the same ratio gives $-974.43$, reflecting the loop-parameter sensitivity quantified in the previous section.

**The other five entries are recorded, not verified.** No current computation publishes $-1.1435$, $-1.2229$, $+3.4976$ or $+57.149$ today —
the canonical extraction stops after one rung by design, because
extracting a rung by inverting the target drives the next residual to exactly
zero. They are retained as the calibration record they were, and should not be
cited as current extractions.

The empirical $c_k$ are **fits**: each is extracted
by matching the truncated product to the measured CODATA $\mathfrak{Q}_\beta$
value, so it encodes the datum it is matched against. That is a calibration
tautology, not a derivation, and it is why the rungs carry no predictive content.
What the conjectures above propose is a *categorical interpretation* of those
extracted constants — a closed form that would make them derived rather than
matched. Until such a form is exhibited, the ladder is a calibration record.
