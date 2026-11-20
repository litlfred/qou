## Derivation paths

Three formal derivation paths stand open:

1. **Khovanov–Rozansky polynomial at finite $q$**: Compute $\mathrm{Kh}(L)(q, t)$ for the typed-$\mathbf{B}_3$ Markov-closure link $L$ at the substrate $q_0$ (not merely $q = 1$). The Taylor coefficients should return $c_4, c_5, c_6, c_7$.
2. **KLR canonical-basis trace formula**: Calculate the per-Wedderburn-block canonical-basis Markov trace at orders $\varepsilon^8, \varepsilon^{10}, \varepsilon^{12}$. The Hecke–KLR bridge supplies scaffolding ([As $q \to 1$, the KLR canonical basis flattens to the Kazhdan–Lusztig basis of $S_n$, recovering Pauli/Bose statistics](#conj:kazhdan-lusztig-classical-limit)). We require the explicit per-block trace formula.
3. **Spectral-sequence stratification**: Currently declined; the framework lacks a suitable candidate spectral sequence.

## Comparison with extracted values

| Rung | Conjectured closed form | Residual against extraction | Categorical interpretation |
|:----:|:-----------------------:|:---------------:|----------------------------|
| $c_4$ | $c_3 \cdot b^4 = -2 \cdot b^4$ | **0.9%** residual | Hopf Jones $\times$ Kashiwara $b^4$ correction (multiplicative mixing) |
| $c_5$ | $-(b^2 + 1/2)$ | **2.4%** residual | Kashiwara $b^2$ + half-Hopf integer offset (mixed) |
| $c_6$ | $c_3^2 \cdot b^2 = 4 \cdot b^2$ | **14%** residual | Hopf Jones squared $\times$ Kashiwara $b^2$ |
| $c_7$ | $c_3^3 = -8$ | **signed error $+114\%$** | Hopf Jones cubed |

Match quality degrades at higher $k$. For $c_7$, the signed relative error is approximately $114\%$ (magnitude error $86\%$). We retain the conjecture because the $N=7$ correction's leverage on the cumulative $\mathfrak{Q}_\beta$ residual operates at the $10^{-13}$ scale. Any $c_7 \in [-100, +100]$ closes the gap to within $10^{-4}$ ppb, leaving the numerical value highly under-determined.

## Precision

The $+6.02$ ppb residual at $N=3$ recorded for this ladder, and the sub-$1$ ppb
figures the higher rungs ($c_4$ to $c_7$) reach, are **not** a current statement
that the $100\times$ accuracy target for $\mathfrak{Q}_\beta$ is met. Both are
properties of a cell the framework has since retired, and they are quoted here as
a record of that cell, not as a prediction.

Two scopings apply, and neither was present when those figures were first
written:

1. **Convention.** The ladder was built with the Markov parameter
   $z_C = \sqrt{q}/(q+1)$ (convention **C**), which is excised; the canonical
   parameter is $z_D = q^3/(q^2+1)$. No convention-D counterpart exists to
   compare against, so the figure is *unreproducible* under the canonical
   convention.
2. **Functional.** The published form rests on $z = 1$, which is
   **inadmissible**: it is the coordinate sum, and provably not a Markov root
   under convention D (`ConventionDAdmissibleRoots.lean`).

Against the same $7.797$ ppb target, the live per-observable dashboard scores
$\mathfrak{Q}_\beta$ on the ruled base at $1.668\times10^{8}$ ppb — a miss of
$2.139\times10^{7}$, the largest in the table. That figure and the $+6.02$ ppb
above are *different objects*: the dashboard evaluates the ruled $z_D$ base with
**zero** $c_k$ rungs, while the figure above is the five-rung ladder on the
retired $z = 1$ cell. The comparison is stated so a reader meets both, not to
present either as the other's correction.

Under the three-calibration discipline, the higher rungs are calibration-anchored
fits: they encode the CODATA datum they are matched to, so they are a calibration
record rather than a prediction, and any downstream claim relying on them must
declare that dependency. 


## Evidence

A direct SDP-$T_\beta$ extraction at 50 decimal places was recorded as
reproducing the conjectured $c_k$. **The table is a historical record and is
reproduced with its provenance, because one entry is superseded and the rest have
no live producer.**

```text
c_2 extracted = -1.0171   (vs framework -1)
c_3 extracted = -2.0098   ← SUPERSEDED; see below
c_4 extracted = -1.1435   (matches empirical sweep exactly)
c_5 extracted = -1.2229   (matches empirical sweep exactly)
c_6 extracted = +3.4976   (matches empirical sweep exactly)
c_7 extracted = +57.149   (matches empirical sweep exactly)
```

**$c_3$: the recorded $-2.0098$ matches no value the corpus now carries.** It is
a superseded figure, retired when the substrate anchors were re-derived. The
live convention-C extractions are

| anchor | $c_3$ |
|---|---|
| proton (the canonical compute pin) | $-2.06934257711516783787971951725$ |
| muon, CODATA 2022 | $-2.019860311874005$ |
| muon, CODATA 2018 | $-2.020200233$ |

Since this block states no anchor, the proton value is the one to read here: it
is the pin all production compute defaults to. All
three are convention **C**; under convention D the same extraction gives
$-974.43$, which is the scoping the previous section describes.

**The other five entries are recorded, not verified.** No current computation publishes $-1.1435$, $-1.2229$, $+3.4976$ or $+57.149$ today —
the canonical extraction stops after one rung by design, because
extracting a rung by inverting the target drives the next residual to exactly
zero. They are retained as the calibration record they were, and should not be
cited as current extractions.

The empirical $c_k$ from `binding_q_target_sweep` are **fits**: each is extracted
by matching the truncated product to the measured CODATA $\mathfrak{Q}_\beta$
value, so it encodes the datum it is matched against. That is a calibration
tautology, not a derivation, and it is why the rungs carry no predictive content.
What the conjectures above propose is a *categorical interpretation* of those
extracted constants — a closed form that would make them derived rather than
matched. Until such a form is exhibited, the ladder is a calibration record.
