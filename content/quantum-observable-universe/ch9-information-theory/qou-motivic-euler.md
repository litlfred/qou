The **motivic Euler characteristic** of the
[QOU locus](#def:qou-locus) is determined by the Yekutieli
obstruction class $\kappa_0 \in H^2(\mathcal{S}, \mathbb{G}_m)$
with $\mathrm{tr}(\kappa_0) = \chi(A)$:

$$
  \chi_{\mathrm{mot}}(\mathfrak{M}_{\mathrm{QOU}})
  \;=\; \sum_{\substack{n \geq 1 \\ n \mid \chi(A)}}
  \mu_q\!\bigl(\mathfrak{M}_{\mathrm{QOU}}^{(n)}\bigr)
  \cdot L_q^{-n}
  \;\in\; K_0(\mathbf{C})[L_q^{-1}]
$$

where $\mathfrak{M}_{\mathrm{QOU}}^{(n)}$ is the QOU locus at
Kummer level $n$.

The **Yekutieli obstruction controls which levels contribute**.
At Kummer level $n$, the obstruction class reduces to
$\kappa_0 \bmod n$. The perpetual-obstruction theorem gives:

- If $n \mid \chi(A)$: then $\kappa_0 \bmod n = 0$ and the
  motivic contribution $\mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(n)})$
  is **non-zero** — lifts through the brane tower exist.
- If $n \nmid \chi(A)$: then $\kappa_0 \bmod n \neq 0$ and the
  contribution **vanishes** — the obstruction kills the entire
  Kummer level.

Since $\chi(A) = -6$, only levels $n \in \{1, 2, 3, 6\}$ survive.
**The sum is finite** — a four-term expression:

$$
  \chi_{\mathrm{mot}}(\mathfrak{M}_{\mathrm{QOU}})
  \;=\; \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(1)}) \cdot L_q^{-1}
  \;+\; \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(2)}) \cdot L_q^{-2}
  \;+\; \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(3)}) \cdot L_q^{-3}
  \;+\; \mu_q(\mathfrak{M}_{\mathrm{QOU}}^{(6)}) \cdot L_q^{-6}
$$

This finiteness is the motivic expression of QOU rigidity:

1. **Fibre-functor rigidity**
   ([rigidity](#rem:fibre-functor-rigidity)): observability
   forces $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$, so
   the tangent space to $\mathfrak{M}_{\mathrm{QOU}}$ at each
   point has dimension zero. No continuous deformations.

2. **Gauge universality**: the volume constraint forces
   $G = \mathrm{SU}(2)$; no moduli from gauge group choice.

3. **Substrate extraction**: the braiding eigenvalue determines
   $q$; no moduli from the substrate parameter.

The Yekutieli class $\kappa_0$ plays a dual role: it generates
the perpetual obstruction (killing levels $n \nmid 6$) and
simultaneously determines the surviving divisor structure
($n \mid 6$) that gives the Euler characteristic its specific
value.

In the archimedean realisation, the cohomological embedding
theorem (genus forced to $4$, $\chi = -6$) further constrains
the four surviving levels to a **single rigid point**:

$$
  \chi_{\mathrm{mot}}(\mathfrak{M}_{\mathrm{QOU}}^{\mathrm{arch}})
  \;=\; [\mathrm{pt}]
$$
