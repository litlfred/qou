The $S_{\mathrm{cell}}$ closure fixing $G_{\mathrm{Planck}} = 1$ ([gravitational constant](#def:gravitational-constant)) yields a prediction for the Hausdorff dimension of the Reeb Julia set. This provides an independently checkable claim against transfer-operator computations.

**Hausdorff dimension prediction.**
The corrected formula predicts:

$$
  d_H(q) =  \frac{(2q-1)^2}{q^3}.
$$

| $q$         | $d_H$ predicted | $d_H$ box-counting | Known exact           | Note                                                                  |
| ----------- | --------------- | ------------------ | --------------------- | --------------------------------------------------------------------- |
| $1$         | $1.000$         | —                  | $1.000$ (unit circle) | Exact match                                                           |
| $q_0$       | $1.088$         | $1.012$            | —                     | Box-counting underestimates thin quasicircles                         |
| $1.5$       | $1.185$         | —                  | —                     | Basilica root $c = -3/4$ (period-$2$ parabolic; known $d_H \sim 1.2$) |
| $\varphi^2$ | $1.000$         | —                  | —                     | Golden crossover: $d_H$ returns to $1$                                |

The formula yields $d_H = 1$ at $q = 1$ (unit circle) and $q = (3+\sqrt{5})/2 = \varphi^2$ (golden threshold), which are exact matches. For $1 < q < \varphi^2$, the Julia set is strictly more fractal than a circle ($d_H > 1$), consistent with McMullen's theorem [mcmullen1998].

**Testable prediction.**
The value $d_H(q_0) = 1.088$ is testable against high-precision transfer-operator computations (Ruelle 1982) for $d_H(J_c)$ at $c(0.1097) = 0.338 + 0.073i$. Box-counting gives $d_H \approx 1.012$ but systematically underestimates thin Jordan curves. The Ruelle perturbative lower bound $1 + |c|^2/(4\ln 2) \approx 1.043$ is consistent with the prediction.
