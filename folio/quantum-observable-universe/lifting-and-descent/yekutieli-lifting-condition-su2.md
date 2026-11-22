One verifies the [Quantum lifting condition](#def:yekutieli-lifting-condition) for $G = \mathrm{SU}(2)$ in [SU(2) as a QOU](#ex:qou-su2).

**The site.** Let $\mathcal{S} = \mathbb{CP}^1$ with the analytic topology. The space $\mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ is the flag variety of maximal tori in $\mathrm{SU}(2)$.

**The gerbe.** The Hopf fibration $\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$, a principal $\mathrm{U}(1)$-bundle, defines a gerbe $\mathfrak{G}$ on $\mathcal{S}$. Objects over an open $U \subseteq \mathbb{CP}^1$ are local lifts of $\pi$. Morphisms are bundle isomorphisms. The banding sheaf $\mathcal{B} = \mathcal{O}_{\mathbb{CP}^1}^{\times}$ is the sheaf of nowhere-vanishing holomorphic functions.

**The obstruction class.** The exponential sequence $0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^{\times} \to 0$ on $\mathbb{CP}^1$ yields the connecting homomorphism:
$$
  H^1(\mathbb{CP}^1, \mathcal{O}^{\times})
  \xrightarrow{c_1}
  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$
The obstruction to lifting a line bundle $L$ on $\mathbb{CP}^1$ to the total space of the gerbe is its first Chern class $\kappa(L) = c_1(L) \in H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$. This class lives in $H^2$ with $\mathbb{Z}$ coefficients, the image of $H^1(\mathbb{CP}^1, \mathcal{O}^{\times})$ under $c_1$. It does not live in $H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$, which is zero by the same exponential sequence.

**Verification.** The condition requires that $L$ admits a lift if and only if $\kappa(L) = 0$. For $\mathbb{CP}^1$:

- The tautological line bundle $\mathcal{O}(-1)$ has $c_1 = -1 \neq 0$. It does not lift.
- The trivial bundle $\mathcal{O}$ has $c_1 = 0$. It lifts via the constant section.

The group $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ is torsion-free. The condition $\kappa(L) = 0$ is necessary and sufficient for a lift. The Quantum lifting condition holds for $\mathrm{SU}(2)$.
