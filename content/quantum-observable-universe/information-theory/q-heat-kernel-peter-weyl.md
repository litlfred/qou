**Proposition ($q$-heat kernel spectral decomposition).**
*Applying the categorical Fourier transform ([categorical Fourier transform](#def:categorical-fourier)) to the $q$-heat equation ([$q$-heat equation](#def:q-heat-equation)) diagonalises the $q$-Laplacian on each Peter--Weyl isotypic component of $\mathbf{Rep}(\mathrm{SU}_q(2))$. This yields an explicit spectral formula for the $q$-heat kernel.*

**Spectral decomposition.** We consider a solution $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$ to $\partial_t u = -\Delta_q u$ with initial datum $u_0$. The solution decomposes as

$$
  u(t, x) \;=\; \sum_{\lambda \in \widehat{H_n(q)}}
    d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t}  \cdot \pi_\lambda(u_0)(x).
$$

The sum ranges over irreducible Wedderburn blocks of the Hecke algebra $H_n(q)$, equivalent to partitions $\lambda \vdash n$. The dimension $d_\lambda(q)$ is the Steinberg $q$-hook dimension, $\pi_\lambda$ projects onto the $V_\lambda$-isotypic component, and $\mu_\lambda(q)$ is the $q$-Laplacian eigenvalue.

**Explicit content-Casimir formula.** Given a partition $\lambda \vdash n$ with cell contents $c(\square) = j - i$, the Reeb-spin eigenvalue of $\Delta_\xi$ on $V_\lambda$ is

$$
  \boxed{\;
  \mu_\lambda(q)
  \;=\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q.
  \;}
$$

The factor $\hbar_q = (q - 1)/q$ is the quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)) and $[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer. This formula computes the eigenvalue of the pure-spin piece $(1 - q^{-1})^2 \Delta_\xi$ from the three-term expansion ([$q$-Laplacian expansion](#rem:q-laplacian-expansion)). The classical-core piece $q^{-2}\Delta$ acts on spatial modes of the base manifold $M$ and contributes a separate eigenvalue $q^{-2}|\mathbf{k}|^2$ dependent on the spatial wavenumber $\mathbf{k}$. Coriolis cross-terms vanish on Hecke-representation spaces by Schur's lemma.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, bounds, transcendental constants, or numerical evaluation at $q_0$). Any categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
