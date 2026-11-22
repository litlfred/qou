## Proof (one-line ring identity)

Substitute the bias hypothesis for both $\hat c_k$ and $\hat c_{k+1}$:

$$
\hat c_k^{\mathrm{corr}}
\;=\; \hat c_k - \hat c_{k+1} \cdot u_0
\;=\; (c_k^{\mathrm{alg}} + c_{k+1}^{\mathrm{alg}} \cdot u_0)
    - (c_{k+1}^{\mathrm{alg}} + c_{k+2}^{\mathrm{alg}} \cdot u_0) \cdot u_0
$$

$$
\;=\; c_k^{\mathrm{alg}} + c_{k+1}^{\mathrm{alg}} \cdot u_0
    - c_{k+1}^{\mathrm{alg}} \cdot u_0 - c_{k+2}^{\mathrm{alg}} \cdot u_0^2
\;=\; c_k^{\mathrm{alg}} - c_{k+2}^{\mathrm{alg}} \cdot u_0^2.
$$

The cross-talk at order $u_0^2$ remains; modulo $u_0^2$, the
bias-corrected value equals $c_k^{\mathrm{alg}}$. $\blacksquare$

## canonical confirmation at $q_0$

The canonical evaluation the canonical formalism
applies this identity to the SDP-extracted $\hat c_k$ at the proton-pinned
$q_0$:

| Rung | $\hat c_k$ (SDP extracted) | $\hat c_k^{\mathrm{corr}}$ (this proposition) | Algebraic target |
|---|---|---|---|
| $k = 2$ | $-1.0171$ | $-0.9999932$ | $-1$ (canonical, [$c_2 = -1$ in the $\mathfrak{Q}_\beta$ precision ladder is structural](q-beta-c-2-eq-neg-one-structural.md)) |
| $k = 3$ | $-2.0097$ | $-1.9999968$ | $-2 = J_{\mathrm{Hopf}}(q=1)$ |

The bias correction recovers the canonical $c_2 = -1$ to $7\,\mathrm{ppm}$ and
the empirical near-match $c_3 = -2 = J_{\mathrm{Hopf}}(q=1)$ to $3\,\mathrm{ppm}$
— both within the $O(u_0^2)$ residual predicted by this proposition
(with $u_0 \approx 0.00852$, $u_0^2 \approx 7.3 \times 10^{-5}$).
