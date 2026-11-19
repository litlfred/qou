Applying the categorical Fourier transform to the $q$-heat equation diagonalises the $q$-Laplacian on each Peter--Weyl isotypic component of $\mathbf{Rep}(\mathrm{SU}_q(2))$, yielding an explicit spectral formula for the $q$-heat kernel in two parts.

1. **Spectral decomposition.** A solution $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$ to $\partial_t u = -\Delta_q u$ with initial datum $u_0$ decomposes as
$$
  u(t, x) = \sum_{\lambda \in \widehat{H_n(q)}} d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t} \cdot \pi_\lambda(u_0)(x).
$$
The sum ranges over irreducible Wedderburn blocks of the Hecke algebra $H_n(q)$, equivalently indexed by partitions $\lambda \vdash n$. The dimension $d_\lambda(q)$ is the Steinberg $q$-hook dimension, $\pi_\lambda$ projects onto the $V_\lambda$-isotypic component, and $\mu_\lambda(q)$ denotes the $q$-Laplacian eigenvalue.

2. **Explicit content-Casimir formula.** Given a partition $\lambda \vdash n$ with cell contents $c(\square) = j - i$, the Reeb-spin eigenvalue of $\Delta_\xi$ on $V_\lambda$ is
$$
  \mu_\lambda(q) = \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q.
$$
The factor $\hbar_q = (q - 1)/q$ is the quantum Planck constant, and $[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer. This formula computes the eigenvalue of the pure-spin piece $(1 - q^{-1})^2 \Delta_\xi$ from the three-term expansion. The classical-core piece $q^{-2}\Delta$ acts exclusively on spatial modes of the base manifold $M$, contributing a separate eigenvalue $q^{-2}|\mathbf{k}|^2$ dependent on the spatial wavenumber $\mathbf{k}$. Coriolis cross-terms vanish identically on Hecke-representation spaces by Schur's lemma.
