**Conjecture (diagrammatic double-magic LR-fusion rigidity).**
*Let $Z, N \in \mathfrak{M}$. By [Categorical neutrality of saturated shells: full-twist identity action on $\Phi_n$ at magic $n$](../mass-endomorphism/categorical-neutrality-saturated-shells.md), the categorical mass at level $Z$ is supported on a single self-conjugate partition $\lambda_Z \vdash Z$, and $\Phi_N$ is similarly supported on $\mu_N \vdash N$ with $\mu_N = \mu_N'$. The LR-fusion at level $A = Z + N$ is **rigid**:*

$$
  V_{\lambda_Z} \otimes V_{\mu_N}
  \;\cong\;
  V_{\nu_{ZN}}(A)
$$

*for a uniquely determined self-conjugate $\nu_{ZN} \vdash A$ with $\nu_{ZN} = \nu_{ZN}'$ and $c(\nu_{ZN}) = 0$. The LR multiplicity is one ($c^{\nu_{ZN}}_{\lambda_Z, \mu_N} = 1$), and all other LR coefficients vanish. Equivalently, $\sum_{x \in \nu_{ZN}} c(x) = 0$: the categorical mass at the double-magic level $A$ is supported strictly on the single self-conjugate Specht module $V_{\nu_{ZN}}$, with no off-diagonal Wedderburn capacity to absorb crossing energy beyond the Coulomb, Casimir, and pairing terms already present at $\lambda_Z$ and $\mu_N$.*

**Remark (the rigidity fails for genuine LR coefficients).** With $c^{\nu}_{\lambda\mu}$ the Littlewood–Richardson coefficient, counted as LR tableaux of shape $\nu/\lambda$ and content $\mu$, the statement above cannot hold for any $Z, N \in \mathfrak{M}$. For nonempty $\lambda, \mu$ the row sum $\lambda + \mu$ (row lengths added) always occurs, $c^{\lambda+\mu}_{\lambda\mu} \geq 1$: fill row $i$ of $(\lambda+\mu)/\lambda$ with the value $i$. Rigidity therefore forces $\nu_{ZN} = \lambda_Z + \mu_N$. The first row of $\lambda + \mu$ has $\lambda_1 + \mu_1$ cells, while its first column has $\max(\lambda_1, \mu_1)$ cells when $\lambda = \lambda'$ and $\mu = \mu'$, so $\lambda + \mu$ is not self-conjugate. Self-conjugacy of $\nu_{ZN}$ follows from rigidity and the conjugation symmetry $c^{\nu'}_{\lambda'\mu'} = c^{\nu}_{\lambda\mu}$, so the two requirements are incompatible.
