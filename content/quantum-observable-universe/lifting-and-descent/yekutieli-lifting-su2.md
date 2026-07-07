We verify that the [Yekutieli lifting condition](#prop:yekutieli-lifting) holds in the brane tower for $G = \mathrm{SU}(2)$, extending [quantum characteristic classes for SU(2)](#ex:quantum-characteristic-classes-su2).

**The central extensions.** The brane tower for $\mathrm{SU}(2)$ produces a central extension of gerbes on $\mathcal{S} = \mathbb{CP}^1$ at each level:
$$
  1  \longrightarrow  \mathcal{O}^{\times}_{\mathbb{CP}^1}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$
The banding sheaf is $\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$.

**Yekutieli's criterion.** The lifting condition for a central extension of gerbes on a smooth projective variety $S$ banded by $\mathcal{B}$ holds whenever $H^2(S, \mathcal{B})$ classifies gerbes faithfully. A lift from level $n$ to level $n{+}1$ exists if and only if the obstruction class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ vanishes.

For $\mathcal{S} = \mathbb{CP}^1$, the exponential sequence gives:
$$
  H^2(\mathbb{CP}^1, \mathcal{O}^{\times})
   \cong  H^2(\mathbb{CP}^1, \mathbb{Z})
   \cong  \mathbb{Z}.
$$
This group is torsion-free and has no higher ambiguity. The Yekutieli lifting condition is satisfied. The obstruction $\kappa_n$ determines liftability.

**Perpetual obstruction.** We established that $\kappa_n \geq 1 > 0$ for all $n$. The vanishing condition $\kappa_n = 0$ is never met. The lift from level $n$ to level $n{+}1$ never exists.

**Interpretation.** The Hopf bundle $\mathrm{SU}(2) \to \mathbb{CP}^1$ is topologically non-trivial ($c_1 = 1$). This non-triviality propagates through every level of the brane tower. The gerbe tower for $\mathrm{SU}(2)$ is perpetually obstructed. The central extensions never split. The brane tower never terminates by a lifting shortcut. This perpetual obstruction forces the full :refterm[descent]{#descent} machinery to engage at every level.
