Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with state bundle $\mathcal{S} \to M$, and let $p \colon \mathbf{1} \to A$ be a categorical point. Let $R$ be a commutative ring containing $\mathbb{Q}$, let $h = q - q^{-1}$, and let $H_n = H_n(R[[h]], q)$ be the Hecke algebra over the formal power series ring in $h$. Write

$$
  W_1 = \mathrm{span}\{\sigma_0,\ \sigma_1,\ \sigma_0\sigma_1^{-1}\} \subset H_3
$$

for the span of the three non-identity terms of the photon $\gamma = 1 + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1}$ (the photon is defined in the chapter on Bring's surface).

An **observation** at $p$ (also called an *intent* at $p$) is a pair $(w_p, \delta q_p)$ consisting of:

1. **A probe direction** $w_p \in h\,W_1[[h]]$. It acts on a closed state $\psi$ by conjugation, $\psi \mapsto e^{w_p}\,\psi\,e^{-w_p}$. The exponential converges in the $h$-adic topology because $w_p$ is divisible by $h$. The first-order change is the commutator $[w_p, \psi]$. Conjugation preserves every trace, so the Frobenius form is preserved.
2. **A substrate deformation** $\delta q_p \in R$, which shifts the substrate parameter $q \mapsto q' = q + \delta q_p$.

Two observations at the same point with directions $w_1, w_2$ fail to commute by

$$
  e^{w_1} e^{w_2} e^{-w_1} e^{-w_2} = 1 + [w_1, w_2] + O(h^3),
$$

and the first-order term $[w_1, w_2]$ is the $q$-curvature of the two-observer parallelogram (see the remark that follows).

The direction $w_p$ is a vector in a $3$-dimensional space, not a choice between a forward crossing $\sigma_i$ and a backward crossing $\sigma_i^{-1}$. The first-order data are taken in $h\,W_1$ rather than in the $1$-jet space $\mathfrak{m}_p/\mathfrak{m}_p^2$ because that space is zero at any character of a semisimple Hecke fibre: $(\sigma - q)^2 = -(q + q^{-1})(\sigma - q)$, so $\sigma - q \in \mathfrak{m}_p^2$ whenever $q + q^{-1}$ is invertible.
