We verify the structural properties of the main theorem for $G = \mathrm{SU}(2)$, extending [Yekutieli lifting for SU(2)](#ex:yekutieli-lifting-su2).

**Hypotheses.** The quantum universe is $(\mathrm{Rep}(\mathrm{SU}(2)), \mathcal{O}(\mathrm{SU}(2)), \tau)$ with substrate parameter $q$ ([SU(2) QOU](#ex:qou-su2)). Observability holds: $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ because $\mathrm{Ad}(\mathrm{SU}(2)) \cong \mathfrak{su}(2)$ has no trivial sub-representation. The adjoint representation is irreducible.

**(1) :refterm[Descent]{#descent} terminates.** The center of the endomorphism algebra is $Z(\mathrm{End}_{\mathbf{C}}(A)) \cong \mathcal{O}(\mathrm{SU}(2))^{\mathrm{SU}(2)}$. This ring of $\mathrm{SU}(2)$-invariant functions has Krull dimension $\mathrm{rank}(\mathrm{SU}(2)) = 1$. The geometric :refterm[descent]{#descent} tower is:
$$
  \mathbb{CP}^1  \longrightarrow  \mathrm{pt},
$$
which terminates in $1$ step. At each step, the $G_q$-action is faithful. Observability ensures strict dimension reduction.

**(2) First obstruction equals the Euler class.** The Yekutieli obstruction $\kappa_0 \in H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ equals the Euler class of the Reeb bundle. For the Hopf fibration, this is $c_1(\text{Hopf}) = 1$. Under the trace map:
$$
  \kappa_0  \longmapsto  \chi(A)
  =  \mathrm{tr}(\mathrm{id}_A)
  =  \chi(\mathbb{CP}^1) =  2.
$$

**(3) Perpetual obstruction.** We established that $\kappa_0 = 1 \in \mathbb{Z}$ is non-torsion. The jet corrections at level $n$ are non-negative. We have $\kappa_n \geq 1 > 0$ for all $n \geq 0$. The gerbe tower is perpetually obstructed.

**(4) Branch point formula.** The projective line object is $\mathbb{P}(V) = \mathbb{CP}^1$. The :refterm[descent]{#descent} map $\mathbb{CP}^1 \to \mathbb{CP}^1$ has degree $d = 1$. The Riemann--Hurwitz formula gives:
$$
  R_{\mathrm{tot}} =  2d + |\chi(A)|
  =  2 \cdot 1 + |2| =  4,
$$
with $B = 2$ branch points (the north and south poles of $\mathbb{CP}^1 \cong S^2$). Each has ramification index $e = 2$.

**(5) Terminal fiber data.** At each branch point $p \in \{0, \infty\} \subset \mathbb{CP}^1$, the QOU reduces to fiber data $(\mathcal{O}(\mathrm{SU}(2)), \tau, q(p))$ with the involution:
$$
  \sigma \colon \mathbb{CP}^1
   \hookrightarrow 
  \mathrm{Ad}(\mathrm{SU}(2))
  =  \mathfrak{su}(2).
$$
This embedding realizes $\mathbb{CP}^1 \cong S^2$ as the unit sphere in $\mathfrak{su}(2) \cong \mathbb{R}^3$. At the north pole $p = 0$, the involution acts as $\sigma(v) = e_3 v e_3^{-1}$. This is the identity on $\mathrm{U}(1)$-invariant sections and negation on off-diagonal components. The fiber data at $p = \infty$ is conjugate via the Weyl group element $w \colon e_3 \mapsto -e_3$.

**Conclusion.** All five properties hold for $\mathrm{SU}(2)$. The quantum universe $(\mathrm{Rep}(\mathrm{SU}(2)), \mathcal{O}(\mathrm{SU}(2)), \tau)$ with observability and the Yekutieli lifting condition is a quantum observable universe. Descent terminates in $1$ step, the brane tower is perpetually obstructed, there are $2$ branch points on $\mathbb{CP}^1$, and the fiber data is governed by the adjoint embedding $S^2 \hookrightarrow \mathfrak{su}(2)$.
