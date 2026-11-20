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

This chapter introduces the **quantum universe** (QU): a
:refterm[braided monoidal category]{#braided-monoidal-category} equipped with a Frobenius--Hopf object,
a fibre functor, and a differential calculus.  Duals are not part of
this definition.  They are imposed in Chapter 2, on the quantum
observable universe, where they carry the antiparticles; the
constructions later in this chapter that do use duals — the
involutive structure, the categorical Hodge star, the internal
Poisson object — say so in their own hypotheses.  The chapter begins with
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
[Chapter 3](#chap:qou).
