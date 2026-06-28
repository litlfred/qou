**Proposition ($q$-heat kernel spectral decomposition).**
Applying the categorical Fourier transform
([categorical Fourier transform](#def:categorical-fourier)) to the
$q$-heat equation ([$q$-heat equation](#def:q-heat-equation))
diagonalises the $q$-Laplacian on each Peter--Weyl isotypic
component of $\mathbf{Rep}(\mathrm{SU}_q(2))$ (or more generally
of any quantum group acting on the substrate), giving an
explicit spectral formula for the $q$-heat kernel.

**Spectral decomposition.**  For $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbb{C}$
solving $\partial_t u = -\Delta_q u$ with initial datum $u_0$:

$$
  u(t, x) \;=\; \sum_{\lambda \in \widehat{H_n(q)}}
    d_\lambda(q) \cdot e^{-\mu_\lambda(q)\,t}  \cdot \pi_\lambda(u_0)(x),
$$

where the sum ranges over irreducible Wedderburn blocks of the
Hecke algebra $H_n(q)$ — equivalently partitions $\lambda \vdash n$
of the number of strands $n$ —
$d_\lambda(q)$ is the Steinberg $q$-hook dimension,
$\pi_\lambda$ is the projection onto the $V_\lambda$-isotypic
component, and $\mu_\lambda(q)$ is the $q$-Laplacian eigenvalue.

**Explicit content-Casimir formula.**  For a partition
$\lambda \vdash n$ with cell contents $c(\square) = j - i$, the
**Reeb-spin eigenvalue** of $\Delta_\xi$ on $V_\lambda$ is:

$$
  \boxed{\;
  \mu_\lambda(q)
  \;=\;
  \hbar_q^2  \sum_{\square \in \lambda}  [c(\square)]_q \, [c(\square) + 1]_q,
  \;}
$$

where $\hbar_q = (q - 1)/q$ is the quantum Planck constant
([quantum Planck constant](#def:quantum-planck-constant)) and
$[k]_q = (1 - q^k)/(1 - q)$ is the Jackson integer.  This is the
eigenvalue of the pure-spin piece $(1 - q^{-1})^2 \Delta_\xi$ from
the three-term expansion
([$q$-Laplacian expansion](#rem:q-laplacian-expansion)).  The
classical-core piece $q^{-2}\Delta$ acts on spatial modes of the
base manifold $M$ and contributes a *separate* eigenvalue
$q^{-2}|\mathbf{k}|^2$ depending on the spatial wavenumber
$\mathbf{k}$, not on the partition $\lambda$.  Coriolis cross-terms
vanish on Hecke-representation spaces by Schur's lemma.
