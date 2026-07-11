Evaluating the $q$-Reeb rotation angle $\theta(q) = \arg\lambda_{4_1}$, where $2\cos\theta = \mathrm{tr}M_{4_1}$, at the substrate modulus $q_0$ gives a definite value. Building the $2\times 2$ Hoefsmit seminormal block of $\sigma_1,\sigma_2$ on $V_{(2,1)}$ explicitly — $\sigma_1 = \mathrm{diag}(q, -q^{-1})$, with $\sigma_2$ fixed by the braid and Hecke relations — the trace of $M_{4_1} = (\sigma_1\sigma_2^{-1})^2$ is the Laurent polynomial

$$
  \mathrm{tr}M_{4_1}(q) \;=\; q^4 - 2q^2 + 1 - 2q^{-2} + q^{-4}.
$$

At the classical point $q=1$ this trace is $-1$, so $|\mathrm{tr}| = 1 < 2$ and the eigenvalue is a primitive cube root of unity: the classical $q$-Reeb angle is $\theta(1) = 2\pi/3 = 120^\circ$ exactly. This is the amphichiral anchor of the figure-eight knot, where the Chern–Simons invariant vanishes.

At the substrate modulus $q_0 \approx 1.10998$ the same trace evaluates to $\mathrm{tr}M_{4_1}(q_0) \approx -0.91068$, giving

$$
  \theta(q_0) \;\approx\; 117.09^\circ,
  \qquad
  \Delta\theta \;=\; \theta(q_0) - \tfrac{2\pi}{3} \;\approx\; -2.91^\circ.
$$

The $q$-deformation moves the rotation angle off its classical amphichiral value by the small $\Delta\theta$; this departure is the parameter-free measure of the symmetry breaking that seeds the bar-odd part $S$ of the $\beta$-decay observable. The angle $\theta(q)$ is a smooth function of $q$ ($\mathrm{d}\theta/\mathrm{d}q \approx -51^\circ$ per unit $q$), so $\theta(q_0)$ fixes the carrier scale of the deformation phase but is not itself the source of the observed hypersensitivity in the truncation coefficient $c_3$; that hypersensitivity resides in the substrate-to-deformation map, which remains conjectural.

The values are computed to full working precision in [`qbeta_c3_reeb_rotation_phase_probe.py`](../../../computations/qbeta/qbeta_c3_reeb_rotation_phase_probe.py). The unit-modulus property $|\lambda_{4_1}| = 1$ and the classical anchor $\theta(1) = 2\pi/3$ (primitive cube root of unity) are established sorry-free in the Lean file.
