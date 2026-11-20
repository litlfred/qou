Applying the categorical Fourier transform to the $q$-heat equation diagonalises the $q$-Laplacian on each Peter--Weyl isotypic component of $\mathbf{Rep}(\mathrm{SU}_q(2))$, yielding an explicit spectral formula for the $q$-heat kernel in two parts.

1. **Spectral decomposition.** A solution $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$ to $\partial_t u = -\Delta_q u$ with initial datum $u_0$ decomposes as
$$
  u(t, x) = \sum_{\lambda \in \widehat{H_n(q)}} d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t} \cdot \pi_\lambda(u_0)(x).
$$
The sum ranges over irreducible Wedderburn blocks of the Hecke algebra $H_n(q)$, equivalently indexed by partitions $\lambda \vdash n$. The dimension $d_\lambda(q)$ is the Steinberg $q$-hook dimension, $\pi_\lambda$ projects onto the $V_\lambda$-isotypic component, and $\mu_\lambda(q)$ denotes the $q$-Laplacian eigenvalue.

2. **Explicit content-Casimir formula.** Given a partition $\lambda \vdash n$ with cell contents $c(\square) = j - i$, the Reeb-spin eigenvalue on $V_\lambda$ is
$$
  \mu_\lambda(q) = \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q,
$$
where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the symmetric quantum integer. It is the eigenvalue on $V_\lambda$ of the Reeb-holonomy Laplacian
$$
  \Delta_\xi^{(q)} = (q - q^{-1})^{-2} \sum_{k=0}^{n-1} \bigl( q\,H_k + q^{-1} H_k^{-1} - (q + q^{-1}) \bigr), \qquad H_k = (\Delta^2_{k-1})^{-1}\Delta^2_k,
$$
where $\Delta^2_k$ is the full twist of the first $k+1$ strands. Each $H_k$ is the $k$-th Jucys--Murphy element of $H_n(q)$, and $\Delta_\xi^{(q)}$ is central. Writing $q = e^{h}$, each summand is a symmetric second difference of step $h$, and as $h \to 0$ the operator tends to $\sum_k X_k(X_k+1)$, where $X_k$ are the classical Jucys--Murphy elements. So $\Delta_\xi^{(q)}$ is the finite-step form of the Reeb Laplacian $\mathcal{L}_\xi^*\mathcal{L}_\xi$, with a half-integer shift. The Reeb part of $\Delta_q$ enters with weight $1$, not $\hbar_q^2$: on a mode with no horizontal derivative, $d_q$ and $\delta_q$ reduce to $d$ and $\delta$, because $q^{-1} + \hbar_q = 1$. The classical-core and cross-coupling terms of rem:q-laplacian-expansion act on such modes as well, and the three coefficients sum to $(q^{-1} + \hbar_q)^2 = 1$. The spatial part contributes a separate eigenvalue $q^{-2}|\mathbf{k}|^2$, dependent on the spatial wavenumber $\mathbf{k}$.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
