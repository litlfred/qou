Continuing
[quantum characteristic classes for SU(2)](#ex\:quantum-characteristic-classes-su2),
we verify that the [Yekutieli lifting condition](#prop\:yekutieli-lifting) holds
in the brane tower for $G = \mathrm{SU}(2)$.

**The central extensions.** The brane tower
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ for
$\mathrm{SU}(2)$ produces, at each level, a central extension of gerbes
on $\mathcal{S} = \mathbb{CP}^1$:

$$
  1  \longrightarrow  \mathcal{O}^{\times}_{\mathbb{CP}^1}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$

The banding sheaf is
$\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$, the sheaf of
nowhere-vanishing holomorphic functions on $\mathbb{CP}^1$.

**Yekutieli's criterion.** By \[Yekutieli 2010], the lifting condition
for a central extension of gerbes on a smooth projective variety $S$
banded by $\mathcal{B}$ holds whenever $H^2(S, \mathcal{B})$ classifies
gerbes faithfully --- that is, a lift of the Frobenius--Hopf object from
level $n$ to level $n{+}1$ exists if and only if the obstruction class
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ vanishes.

For $\mathcal{S} = \mathbb{CP}^1$, the exponential sequence gives

$$
  H^2(\mathbb{CP}^1, \mathcal{O}^{\times})
   \cong  H^2(\mathbb{CP}^1, \mathbb{Z})
   \cong  \mathbb{Z},
$$

which is torsion-free and has no higher ambiguity.  The Yekutieli
lifting condition is therefore satisfied: the obstruction
$\kappa_n$ determines liftability completely.

**Perpetual obstruction.** From the
[quantum characteristic classes](#ex\:quantum-characteristic-classes-su2),
each obstruction is $\kappa_n \geq 1 > 0$ (since $\kappa_0 = c_1(\text{Hopf}) = 1$
and jet corrections are non-negative).  The vanishing condition
$\kappa_n = 0$ is never met, so the lift from level $n$ to level $n{+}1$
never exists.

**Interpretation.** The Hopf bundle
$\mathrm{SU}(2) \to \mathbb{CP}^1$ is topologically non-trivial
($c_1 = 1$), and this non-triviality propagates through every level of
the brane tower.  The gerbe tower for $\mathrm{SU}(2)$ is perpetually
obstructed: the central extensions never split, and the brane tower
never terminates by a lifting shortcut.  This is precisely the behavior
required by the [main theorem](#thm\:qu-to-qou) --- the perpetual
obstruction forces the full :refterm[descent]{#descent} machinery to engage at every level.
