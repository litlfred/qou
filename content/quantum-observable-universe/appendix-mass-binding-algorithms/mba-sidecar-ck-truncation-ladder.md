**Algorithm ($c_k$ truncation ladder).**
*Compute the coefficients of the convergent $\mathfrak{Q}_\beta$ series
$\mathfrak{Q}_\beta = Q_{\mathrm{base}} \cdot \prod_{k = 2}^{N} (1 + c_k\, u^k)$
and report each $c_k$ with its **tiered classification**.*

### Input

- *Target precision $\varepsilon \in \mathbb{R}_{> 0}$.*
- *Substrate $q_0$ (CAL-2 anchor).*

### Output

- *Truncation order $N \geq \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$.*
- *Tuple $\{(k, c_k, \mathrm{tier})\}_{k = 2}^{N}$ with tier one
  of `proved`, `near-match`, or `fitted`.*

### Tier classification (STRICT)

| $k$ | $c_k$ | Tier | Notes |
|---|---|---|---|
| 2 | $-1$ | **structural** | Taylor coefficient of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$; no fit, no CODATA, no $q_0$. Not "proved" — the Lean re-reads the $N{=}2$ factor rather than deriving it. For the normalised series (cosine factor inside) the coefficient is $\tilde c_2 = c_2 - 1/8 = -9/8$ |
| 3 | $-2 = J_{\mathrm{Hopf}}(q = 1)$ | **near-match** | swings $\leq 3.47\%$ at m_p-pin $q_0$ |
| $\geq 4$ | $q_0$-dependent | **near-match** | N=4→N=5 non-monotonicity is the experimental signature |
| any | empirical fit | **fitted** | flagged as discipline violation |

*The $c_k$ are a truncation order, not an inclusion/exclusion criterion: a tier is
reported as a tier, never collapsed to a binary keep-or-discard verdict.*

### Algorithm

```
1. Choose N from target precision.
2. For k = 2:
   c_2 = -1   (structural: the u^2 coefficient of the explicit-factor
              product, fixed by the N=2 factor's form -- not derived).
3. For k = 3, …, N:
   compute c_k from the categorical-precision-ladder formula at q_0;
   classify as `near-match` if within 5% of a closed-form q=1
   limit, else as `fitted` and flag for discipline review.
```

### Correctness conditions

*[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
establishes the convergent ladder, the truncation-order
inequality, and that $c_2$ is the exact $u^2$ coefficient of the
explicit-factor product. That is a re-reading of the $N{=}2$ factor's
form, not a derivation of it; and it is a statement about *that*
series — the normalised series' coefficient is $\tilde c_2 = -9/8$.*

### Python API entry point

*Canonical compute is the script
[`computations/q_beta_predicted.py`](../../../computations/q_beta_predicted.py),
which records each $c_k$ with its tier in the witness JSON.
Higher-precision regenerations use
[`build_cal_3_q_beta_witness.py`](../../../computations/build_cal_3_q_beta_witness.py).*

### Witness contract

*Canonical witness:
[`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json).
**Must** record each $c_k$ alongside its tier.*

### Notes

*Permanent fix path is the $\mathfrak{Q}_\beta$ Habiro element parallel to
$\alpha_{\mathrm{EM}}$'s $[2]_q \cdot (1 - h^2 \alpha)$
The classification of $c_3$ has been reversed repeatedly, and is the
canonical example of why tiered classification is mandatory.*
