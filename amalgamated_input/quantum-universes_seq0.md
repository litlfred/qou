<!-- FILE_START: quantum-universes-intro.md -->
A **quantum universe** is the purely categorical substrate from which
the framework later reads off physics: its axioms are chosen so that,
once observability and a volume constraint are imposed, they *force*
$\mathrm{SU}_2(R)$ as the physical gauge group rather than assuming it.
Before the axioms, it helps to have one instance in hand:
$\mathbf{Rep}(\mathrm{SU}_q(2))$, the category of representations of the
quantum group, is a rigid :refterm[braided monoidal category]{#braided-monoidal-category}
carrying a Frobenius--Hopf object, and it is the guiding example
throughout this chapter — worked concretely in its classical symmetric
($q \to 1$) limit $\mathrm{SU}(2)$.

This chapter introduces the **quantum universe** (QU): a rigid
:refterm[braided monoidal category]{#braided-monoidal-category} equipped with a Frobenius--Hopf object,
a fibre functor, and a differential calculus.  We begin with
categorical preliminaries
([§ Rigid monoidal categories](#sec:rigid-monoidal)), state the
core axioms ([§ The Quantum Universe](#sec:quantum-universe)),
and derive their first consequences — the Frobenius relation,
involutive structure, and Tannaka--Krein reconstruction
([§ Consequences](#sec:qu-consequences)).

The QU axioms also support differential-geometric structures:
categorical connections, jet objects, and the Hodge star
([§ Structures](#sec:qu-structures)).  The passage from a quantum
universe to a *quantum observable universe* — adding observability,
measurability, and the volume constraint that forces
$\mathrm{SU}_2(R)$ as the gauge group — is the subject of
[Chapter 2](#chap:qou).
<!-- FILE_END: quantum-universes-intro.md -->

<!-- FILE_START: scheme-notation.md -->
Every construction in this paper is formulated once over an
arbitrary commutative ring $R$ and specialises to any base — a
reader working over $\mathbb{Z}_p$, $\mathbb{F}_q$, or
$\mathbb{C}$ reads the same axioms and the same proofs, only the
ground ring changes. To keep that substitution visible, all
algebraic groups and projective spaces are written with their
base ring $R$ explicit:

| Object                                                        | Notation                       | Over $\mathbb{C}$         |
| ------------------------------------------------------------- | ------------------------------ | ------------------------- |
| Special unitary group                                         | $\mathrm{SU}_2(R)$             | $\mathrm{SU}(2)$          |
| Maximal torus / :refterm[Reeb gauge group]{#reeb-gauge-group} | $U_1(R)$                       | $U(1)$                    |
| Quantum group                                                 | $\mathrm{SU}_{q,2}(R)$         | $\mathrm{SU}_q(2)$        |
| Projective line                                               | $\mathbb{P}^1(R)$              | $\mathbb{CP}^1 \cong S^2$ |
| Multiplicative group                                          | $\mathbb{G}_m(R) = R^{\times}$ | $\mathbb{C}^{\times}$     |

When the base ring is clear from context, we may write
$\mathrm{SU}_2$ for $\mathrm{SU}_2(R)$ and $\mathbb{P}^1$
for $\mathbb{P}^1(R)$.  The category-theoretic definitions
([quantum universe](#def:quantum-universe),
[quantum observable universe](#def:quantum-observable-universe))
are stated at this level of generality.
<!-- FILE_END: scheme-notation.md -->

