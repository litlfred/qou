**What is proved.** Let $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ be the gauge group of [the emergence theorem](#thm:su2-emergence), with simple objects $V_j$ labelled by [spin](#prop:spin-labels) and adjoint $V_1 \cong \mathrm{Ad}(A)$. By Clebsch–Gordan \cite{fulton-harris1991},

$$
  \mathrm{Sym}^2(V_1) \;\cong\; V_0 \oplus V_2,
  \qquad
  \dim:\; 6 = 1 + 5 .
$$

The summand $V_0$ is the trace part: the invariant symmetric form on the odd-dimensional adjoint. Removing it leaves one summand,

$$
  V_2 \;=\; \mathrm{Sym}^2(V_1) \ominus V_0 ,
$$

the unique traceless symmetric summand of $V_1 \otimes V_1$. It has spin $2$ and dimension $5$, which is the [spin-$2$ entry](#ex:spin-labels-su2) of the dimension table. The Lean statement `QOU.Eightfold.Sym2AdjointSpinTwo.adjoint_sym2_traceless_is_spin_two` records all four facts: the singlet occurs, exactly one summand remains after removing it, the remaining summand has label $2j = 4$, and $\dim V_2 = 5$.

**The existing spin encoding cannot hold this label.** The electroweak spin label $2s$ of [the charge–spin theorem](#thm:ew-triplet-charge-spin-from-involution) is defined from a two-valued sector, singlet or doublet, so it takes only the values $0$ and $2$. The Lean sibling of that theorem proves that it never takes the value $4$ (`spinDouble_ne_four`). It also proves that any two-valued sector map gives the same value to two of the spins $0, 1, 2$ (`bool_sector_not_injective_on_spins`), so the obstruction comes from having only two values, not from the particular values chosen. The extension `GradedSpin` lets $2s$ be any natural number, as in the $2j$ convention of the spin labels. On the electroweak carriers it agrees with the existing label (`GradedSpin.ofSector_twoS`, `GradedSpin.toSector_spinDouble`), and it contains the new value $2s = 4$ (`GradedSpin.spinTwo_not_ofSector`).

**Caveat: this is gauge spin, not spacetime spin.** Everything above is representation theory of the gauge group $\mathrm{Aut}^{\otimes}(\tau)$. "Spin $2$" here means that $V_2$ is the five-dimensional irreducible representation of that group. A graviton is a spin-$2$ field for the rotation group $\mathrm{SO}(3)$ of spacetime, inside the Lorentz group $\mathrm{SO}(3,1)$. The two statements are about different groups. The corpus does not prove that $\mathrm{Aut}^{\otimes}(\tau)$ is, covers, or acts as a spacetime rotation group. No such identification appears in any statement used here, and none is assumed.

So $V_2$ is a graviton candidate only after an identification that QOU has not proved. That identification would need:

1. a map from $\mathrm{Aut}^{\otimes}(\tau)$ to spacetime rotations, together with a reason why the gauge adjoint $V_1$ transforms as a spacetime vector;
2. a reason why the symmetric traceless tensor built from $V_1$, rather than from a spacetime vector representation, carries the metric fluctuation.

Without these, the same group theory applies equally to any $\mathrm{SU}(2)$ gauge theory, and it says nothing specifically about gravity. As an example, in the electroweak $\mathrm{SU}(2)_L$, $\mathrm{Sym}^2$ of the $W$ triplet contains a weak-isospin-$2$ quintet. That quintet is not a graviton.

**What this remark does not claim.** It makes no claim that any object of $\mathbf{C}$ is a graviton, no claim about a coupling, a mass, or a field equation, and no empirical prediction.
