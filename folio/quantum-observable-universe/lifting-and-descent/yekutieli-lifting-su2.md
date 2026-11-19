The [Quantum lifting condition](#prop:yekutieli-lifting) holds in the brane tower for $G = \mathrm{SU}(2)$, extending [quantum characteristic classes for SU(2)](#ex:quantum-characteristic-classes-su2).

**The central extensions.** The brane tower for $\mathrm{SU}(2)$ produces a central extension of gerbes on $\mathcal{S} = \mathbb{CP}^1$ at each level:
$$
  1  \longrightarrow  \mathcal{O}^{\times}_{\mathbb{CP}^1}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$
The banding sheaf is $\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$.

**Yekutieli's criterion.** The lifting condition for a central extension of gerbes on a smooth projective variety $S$ banded by $\mathcal{B}$ holds whenever $H^2(S, \mathcal{B})$ classifies gerbes faithfully. A lift from level $n$ to level $n{+}1$ exists if and only if the obstruction class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ vanishes.

For $\mathcal{S} = \mathbb{CP}^1$, the exponential sequence $0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^{\times} \to 0$ gives an exact segment
$$
  H^2(\mathbb{CP}^1, \mathcal{O})
   \longrightarrow 
  H^2(\mathbb{CP}^1, \mathcal{O}^{\times})
   \longrightarrow 
  H^3(\mathbb{CP}^1, \mathbb{Z}).
$$
Both outer groups vanish: $H^2(\mathbb{CP}^1, \mathcal{O}) = 0$ because $\mathbb{CP}^1$ has complex dimension 1, and $H^3(\mathbb{CP}^1, \mathbb{Z}) = 0$ because $\mathbb{CP}^1$ has real dimension 2. Hence
$$
  H^2(\mathbb{CP}^1, \mathcal{O}^{\times}) = 0.
$$

**Consequence for the band $\mathcal{O}^{\times}$.** Every obstruction class $\kappa_n \in H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$ is zero. By the lifting criterion, the lift from level $n$ to level $n{+}1$ exists at every level. With this band the gerbe tower for $\mathrm{SU}(2)$ is **not** obstructed.

**Where the non-triviality lives.** The Hopf fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$ is a non-trivial principal $\mathrm{U}(1)$-bundle with $c_1 = 1$. That integer is a class in $H^1(\mathbb{CP}^1, \mathcal{O}^{\times}) \cong \mathbb{Z}$ (the Picard group), mapped to $H^2(\mathbb{CP}^1, \mathbb{Z})$ by $c_1$. It is one cohomological degree below the obstruction group of a gerbe banded by $\mathcal{O}^{\times}$, so it does not obstruct the lift. A perpetual obstruction for $\mathrm{SU}(2)$ would need a different band, for instance $\mathbb{Z}$ or the centre $\mathbb{Z}/2$ of $\mathrm{SU}(2)$. This example does not establish one.
