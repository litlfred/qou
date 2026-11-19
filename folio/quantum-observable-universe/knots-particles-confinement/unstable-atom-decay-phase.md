**Decay channel.**
*An unstable atom must drop to a lower confinement level. It either adjoins a higher-energy operator (which then becomes available, raising $\ell$ and enlarging the ILP search space) or transitions to a different atom-knot $K'$ at the same or lower level. The decay product is determined by:*

1. *Identifying the violated constraint $\gamma^* = \arg\min_\gamma (\mathrm{G}(q) x)_\gamma$ over all ILP-attempted $x$. This is the constraint with the smallest shadow price contribution.*
2. *Identifying the decay channel as the operator $e_{\lambda^*}$ whose contribution to $\gamma^*$ is most negative. This is the operator that fails to satisfy Frobenius positivity.*
3. *Obtaining the daughter atom $K'$ by removing $e_{\lambda^*}$ from the normal form and re-running the ILP on the reduced primitive set.*

*This matches the classical $\beta$-decay picture. An unstable nucleus emits the operator that violates positivity, and the daughter has fewer constraints.*

**Phase boundary.**
*An atom that is stable at $q_1$ and unstable at $q_2$ necessarily has a boundary point $q^* \in [q_1, q_2]$ where the relevant shadow price vanishes:*

$$
  E(\lambda^*, q^*)
  \;=\;
  |y_{\lambda^*}(q^*)|
  \;=\;
  0.
$$

*Crossing $q^*$ is a categorical phase transition. The operator $\lambda^*$ disappears from the LP-dual basis, the filtration restructures, and the ILP feasibility flips. This is the operator-theoretic origin of the empirical observation that isotope stability changes abruptly between adjacent $A$ values (e.g. ${}^{12}\mathrm{C}$ is stable, but ${}^{14}\mathrm{C}$ is unstable).*

**Computational shortcut (phase interior).**
*For an atom $K$ deep inside a phase (i.e. $\min_\lambda |u_\lambda(q)| \gg 0$ at the operating $q$), the ILP is **strictly feasible** with a wide margin. The per-generator $\hat V_i^{\mathrm{full}}$ values ([mass-endomorphism tower](#prop:mass-endomorphism-tower)) are locally constant in $q$. They can be **interpolated linearly** between magic-number anchors without re-running the full Wedderburn decomposition. Exact per-generator extraction is required only **at phase boundaries** (where a shadow price vanishes). This justifies computing exact tower data only at magic configurations and interpolating elsewhere.*
