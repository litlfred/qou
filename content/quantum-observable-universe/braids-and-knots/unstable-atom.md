**Definition.**
*An atom-knot $K$ is **unstable at $q$** iff it fails to satisfy
the [stable atom](#def:stable-atom) condition: no $x \in
\mathbb{Z}_{\geq 0}^N$ exists with $\mathrm{G}(q) x \geq 0$ within the
confinement filtration $J^{\ell(K, q)}(q)$.*

**Decay channel.**
*An unstable atom must drop to a lower confinement level —
either by adjoining a higher-energy operator (which then becomes
available, raising $\ell$ and enlarging the ILP search space)
or by transitioning to a different atom-knot $K'$ at the same or
lower level.  The decay product is determined by:*

1. *Identifying the violated constraint:
   $\gamma^* = \arg\min_\gamma (\mathrm{G}(q) x)_\gamma$ over all
   ILP-attempted $x$ — this is the constraint with the smallest
   shadow price contribution.*

2. *The decay channel is the operator
   $e_{\lambda^*}$ whose contribution to $\gamma^*$ is most
   negative — this is the operator that fails to satisfy
   Frobenius positivity.*

3. *The daughter atom $K'$ is obtained by removing
   $e_{\lambda^*}$ from the NF and re-running ILP on the
   reduced primitive set.*

*This matches the classical β-decay picture: an unstable nucleus
emits the operator that violates positivity; the daughter has
fewer constraints.*

**Phase boundary.**
*An atom that is stable at $q_1$ and unstable at $q_2$
necessarily has the boundary point $q^* \in [q_1, q_2]$ where
the relevant shadow price vanishes:*

$$
  E(\lambda^*, q^*)
  \;=\;
  |y_{\lambda^*}(q^*)|
  \;=\;
  0.
$$

*Crossing $q^*$ is a categorical phase transition: the operator
$\lambda^*$ disappears from the LP-dual basis, the filtration
restructures, and the ILP feasibility flips.  This is the
operator-theoretic origin of the empirical observation that
isotope stability changes abruptly between adjacent $A$ values
(e.g. ${}^{12}\mathrm{C}$ stable, ${}^{14}\mathrm{C}$ unstable).*

**Computational shortcut (phase interior).**
*For an atom $K$ deep inside a phase — i.e.,
$\min_\lambda |u_\lambda(q)| \gg 0$ at the operating $q$ —
the ILP is **strictly feasible** with a wide margin.  This means
the per-generator $\hat V_i^{\mathrm{full}}$ values
([mass-endomorphism-tower](#prop:mass-endomorphism-tower)) are
locally constant in $q$: they can be **interpolated linearly**
between magic-number anchors without re-running the full
Wedderburn decomposition.  Only **at phase boundaries** ($q^*$
where a shadow price vanishes) does one need exact per-generator
extraction.  This justifies computing exact tower data only at
magic configurations and interpolating elsewhere.*
