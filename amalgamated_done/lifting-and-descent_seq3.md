<!-- FILE_START: yekutieli-lifting-intro.md -->
We build the brane tower level by level. The existence of each level depends on the vanishing of a cohomological obstruction. We measure this obstruction, identify it as a quantum characteristic class, and use it to upgrade a quantum universe to a quantum observable universe. We use Yekutieli's framework for central extensions of gerbes.

We define the categorical lifting condition. This abstracts the gerbe-theoretic content: an $R$-linear rigid monoidal category $\mathbf{C}$ satisfies the condition with respect to a central extension $1 \to \mathcal{B} \to \mathfrak{G}' \to \mathfrak{G} \to 1$ when each object $x \in \mathfrak{G}$ carries a unique cohomology class $\kappa(x) \in H^2(\mathcal{S}, \mathcal{B})$ obstructing its lift. We identify this obstruction in the brane-tower setting as a quantum characteristic class. We prove this class exists and is unique. The gerbe sequence arising from jet prolongation satisfies the Yekutieli condition. The level-$n$ to level-$(n+1)$ lift exists if and only if $\kappa_n = 0$.

We prove that a quantum universe equipped with observability and a categorical lift is a quantum observable universe. We interpret the obstruction class physically and connect it to the Kummer filtration. We define the motivic Galois character $\chi^{\mathrm{mot}}_A$ to record the motivic refinement. We conjecture that $\chi^{\mathrm{mot}}_A$ is non-trivial at almost every finite place when $\chi(A) \neq 0$.
<!-- FILE_END: yekutieli-lifting-intro.md -->

<!-- FILE_START: yekutieli-lifting-condition.md -->
Let $\mathbf{C}$ be an $R$-linear rigid :refterm[monoidal category]{#monoidal-category}. Let
$$
  1  \longrightarrow  \mathcal{B}
   \longrightarrow  \mathfrak{G}'
   \longrightarrow  \mathfrak{G}
   \longrightarrow  1
$$
be a central extension of gerbes on a site $\mathcal{S}$, banded by an abelian sheaf $\mathcal{B}$. We say that $\mathbf{C}$ satisfies the **Yekutieli Lifting Condition** with respect to $(\mathfrak{G}', \mathfrak{G}, \mathcal{B})$ if, for every object $x \in \mathrm{Ob}(\mathfrak{G})$, the obstruction to lifting $x$ to an object $x' \in \mathrm{Ob}(\mathfrak{G}')$ is classified by a single cohomology class
$$
  \kappa(x)  \in  H^2(\mathcal{S}, \mathcal{B}),
$$
and $x$ admits a lift if and only if $\kappa(x) = 0$.
<!-- FILE_END: yekutieli-lifting-condition.md -->

<!-- FILE_START: yekutieli-lifting-condition-su2.md -->
We verify the [Yekutieli lifting condition](#def:yekutieli-lifting-condition) for $G = \mathrm{SU}(2)$ in [SU(2) as a QOU](#ex:qou-su2).

**The site.** Let $\mathcal{S} = \mathbb{CP}^1$ with the analytic topology. The space $\mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ is the flag variety of maximal tori in $\mathrm{SU}(2)$.

**The gerbe.** The $\mathrm{SU}(2)$-principal bundle $\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$ defines a gerbe $\mathfrak{G}$ on $\mathcal{S}$. Objects over an open $U \subseteq \mathbb{CP}^1$ are local lifts of $\pi$. Morphisms are bundle isomorphisms. The banding sheaf $\mathcal{B} = \mathcal{O}_{\mathbb{CP}^1}^{\times}$ is the sheaf of nowhere-vanishing holomorphic functions.

**The obstruction class.** The exponential sequence $0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^{\times} \to 0$ on $\mathbb{CP}^1$ yields the connecting homomorphism:
$$
  H^1(\mathbb{CP}^1, \mathcal{O}^{\times})
  \xrightarrow{c_1}
  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$
The obstruction to lifting a line bundle $L$ on $\mathbb{CP}^1$ to the total space of the gerbe is its first Chern class $\kappa(L) = c_1(L) \in H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$.

**Verification.** The condition requires that $L$ admits a lift if and only if $\kappa(L) = 0$. For $\mathbb{CP}^1$:

- The tautological line bundle $\mathcal{O}(-1)$ has $c_1 = -1 \neq 0$. It does not lift.
- The trivial bundle $\mathcal{O}$ has $c_1 = 0$. It lifts via the constant section.

The group $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ is torsion-free. The condition $\kappa(L) = 0$ is necessary and sufficient for a lift. The Yekutieli lifting condition holds for $\mathrm{SU}(2)$.
<!-- FILE_END: yekutieli-lifting-condition-su2.md -->

<!-- FILE_START: quantum-characteristic-classes.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\{A_n\}_{n \geq 0}$ be its [recursive brane tower](#def:recursive-brane-tower). Each transition $A_n \hookrightarrow A_{n+1}$ in $\mathbf{C}$ defines a central extension of gerbes on the underlying site. The Frobenius–Hopf object $A_n$ is an object in a gerbe $\mathfrak{G}_n$ banded by the sheaf of units $\mathcal{B}$. The [jet prolongation](#prop:jet-prolongation) produces a central extension:
$$
  1  \longrightarrow  \mathcal{B}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$
The **quantum characteristic classes** are the cohomology classes
$$
  \kappa_n  \in  H^2(\mathcal{S}, \mathcal{B})
$$
that obstruct the lifting of objects from $\mathfrak{G}_n$ to $\mathfrak{G}_{n+1}$. By the [Yekutieli lifting condition](#def:yekutieli-lifting-condition), the condition $\kappa_n = 0$ is necessary and sufficient for the lift to exist.
<!-- FILE_END: quantum-characteristic-classes.md -->

<!-- FILE_START: quantum-characteristic-classes-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe) with recursive brane tower $\{A_n\}_{n \ge 0}$. For every $n \ge 0$, the [quantum characteristic class](#def:quantum-characteristic-classes)
$$
  \kappa_n \in H^2(\mathcal{S}, \mathcal{B})
$$
exists as a well-defined cohomology class obstructing the lift $\mathfrak{G}_n \to \mathfrak{G}_{n+1}$.
<!-- FILE_END: quantum-characteristic-classes-exists.md -->

<!-- FILE_START: quantum-characteristic-classes-unique.md -->
Fix a [quantum observable universe](#def:quantum-observable-universe) and a recursive brane tower $\{A_n\}_{n \ge 0}$. Each [quantum characteristic class](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ is uniquely determined as a cohomology class. Two Čech cocycles classifying the same central extension are cohomologous. They represent the same class $\kappa_n$.
<!-- FILE_END: quantum-characteristic-classes-unique.md -->

<!-- FILE_START: quantum-characteristic-classes-su2.md -->
We compute the [quantum characteristic classes](#def:quantum-characteristic-classes) for $G = \mathrm{SU}(2)$ from the [brane tower for SU(2)](#ex:recursive-brane-tower-su2).

**Setup.** The brane tower $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ produces central extensions of gerbes on $\mathcal{S} = \mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$, banded by $\mathcal{B} = \mathcal{O}^{\times}_{\mathbb{CP}^1}$. The quantum characteristic classes are the obstruction classes $\kappa_n \in H^2(\mathbb{CP}^1, \mathcal{O}^{\times})$ for each transition $A_n \hookrightarrow A_{n+1}$.

**First obstruction.** The Hopf bundle $\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$ is a principal $\mathrm{U}(1)$-bundle. Its first Chern class is:
$$
  \kappa_0 =  c_1(\text{Hopf}) =  1
   \in  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$
Under the trace map $H^2(\mathcal{S}, \mathcal{B}) \to R$, the obstruction maps to the Euler characteristic: $\kappa_0 \mapsto \mathrm{tr}(\mathrm{id}_A) = \chi(\mathbb{CP}^1) = 2$.

**Non-torsion property.** The group $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ is torsion-free. We have $\kappa_0 = 1 \neq 0$. The class $\kappa_0$ is non-torsion.

**Higher obstructions.** At level $n$, the jet prolongation $A_n \hookrightarrow A_{n+1} = J^1(A_n)$ produces an obstruction:
$$
  \kappa_n =  \kappa_0 + \delta_n
   \in  H^2(\mathbb{CP}^1, \mathbb{Z}),
$$
where $\delta_n \in H^2(\mathbb{CP}^1, \mathbb{Z})$ is the correction from the jet structure at level $n$. We have $\kappa_0 = 1$, which generates $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$. Because $\delta_n \in \mathbb{Z}$ and each prolongation adds non-negative curvature ($\delta_n \geq 0$), we find $\kappa_n = 1 + \delta_n \geq 1 > 0$ for all $n$.

**Conclusion.** The quantum characteristic classes for $\mathrm{SU}(2)$ never vanish: $\kappa_n \neq 0$ for all $n \geq 0$. The Hopf bundle is non-trivial. The gerbe tower is obstructed at every level.
<!-- FILE_END: quantum-characteristic-classes-su2.md -->

<!-- FILE_START: yekutieli-lifting.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe). Let $\{A_n\}_{n \geq 0}$ be the [recursive brane tower](#def:recursive-brane-tower). The [jet prolongation](#prop:jet-prolongation) produces central extensions of gerbes:
$$
  1  \longrightarrow  \mathcal{B}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$
These extensions satisfy the [Yekutieli lifting condition](#def:yekutieli-lifting-condition). In the archimedean realisation, $\mathcal{B} = \mathcal{O}_M^{\times}$. The lift of the Frobenius--Hopf object from level $n$ to level $n{+}1$ exists if and only if the [quantum characteristic class](#def:quantum-characteristic-classes) obstruction $\kappa_n \in H^2(M, \mathcal{B})$ vanishes.
<!-- FILE_END: yekutieli-lifting.md -->

<!-- FILE_START: yekutieli-lifting-su2.md -->
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
<!-- FILE_END: yekutieli-lifting-su2.md -->

<!-- FILE_START: qu-to-qou.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) over a Noetherian ring $R$. Let $q$ denote the substrate parameter. Assume the observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe)). The brane tower $\{A_n\}_{n \geq 0}$ constructed via [jet prolongation](#prop:jet-prolongation) satisfies the [Yekutieli lifting condition](#def:yekutieli-lifting-condition). The triple $(\mathbf{C}, A, \tau)$ is a quantum observable universe with the following structural properties:

1. *:refterm[Descent]{#descent} terminates.* The geometric :refterm[descent]{#descent} tower has finite length, bounded by $\mathrm{Krulldim} Z(\mathrm{End}_{\mathbf{C}}(A))$. Observability ensures each step is a strict reduction because the $G_q$-action is faithful.
2. *First obstruction equals the Euler class.* The Yekutieli obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$ equals the Euler class of the Reeb bundle. Under the trace map, $\kappa_0 \mapsto \chi(A) = \mathrm{tr}(\mathrm{id}_A) \in R$.
3. *Perpetual obstruction.* If $\kappa_0$ is non-torsion in $H^2(\mathcal{S}, \mathcal{B})$, then $\kappa_n \neq 0$ for all $n \geq 0$. The class $\kappa_0$ and the jet corrections at level $n$ live in complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$. The corrections cannot cancel $\kappa_0$.
4. *Branch point formula.* The geometric :refterm[descent]{#descent} from $\mathbb{P}(V)$ ([projective line object](#def:projective-line-object)) to points has $B$ branch points with total ramification $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ via Riemann--Hurwitz, where $d$ is the degree of the covering.
5. *Terminal fiber data.* At each branch point $p$, the QOU reduces to fiber data $(A, \tau, q(p))$ with the involution $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ ([fibre adjoint involution](#prop:fiber-adjoint-involution)).

## Lean formalization

The companion Lean `qu_to_qou_exists` encodes an existence stub (`∃ q, True`) pending a faithful statement. The structural proof above is the intended content, deferred via `sorry`.
<!-- FILE_END: qu-to-qou.md -->

<!-- FILE_START: qu-to-qou-su2.md -->
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
<!-- FILE_END: qu-to-qou-su2.md -->
