**Proposition.** *Let $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ be the gauge group of [the emergence theorem](#thm:su2-emergence), with simple objects $V_j$ labelled by [spin](#prop:spin-labels) and adjoint $V_1 \cong \mathrm{Ad}(A)$. Then*

$$
  \mathrm{Sym}^2(V_1) \;\cong\; V_0 \oplus V_2,
  \qquad
  \dim:\; 6 = 1 + 5 ,
$$

*so the traceless part $\mathrm{Sym}^2(V_1) \ominus V_0$ is the single simple object $V_2$, of spin $2$ and dimension $5$.*

**Proof.** By Clebsch–Gordan \cite{fulton-harris1991}, $V_1 \otimes V_1 \cong V_0 \oplus V_1 \oplus V_2$, and the summand $V_k$ of $V_j \otimes V_j$ lies in $\mathrm{Sym}^2(V_j)$ exactly when $k \equiv 2j \pmod 2$. For $j = 1$ this places $V_0$ and $V_2$ in $\mathrm{Sym}^2(V_1)$ and $V_1$ in $\Lambda^2(V_1)$. The summand $V_0$ is spanned by the invariant symmetric form on $V_1$, so removing it leaves $V_2$. Its dimension is $2 \cdot 2 + 1 = 5$, the [spin-$2$ entry](#ex:spin-labels-su2) of the dimension table, and $1 + 5 = 6 = \binom{4}{2}$. $\square$

**Scope of the formalisation.** The Lean declaration `QOU.Eightfold.Sym2AdjointSpinTwo.adjoint_sym2_traceless_is_spin_two` does not prove the Clebsch–Gordan decomposition. That decomposition enters as the definition `Sym2GateParity.sym2Indices`, the set of $k \le 2j$ with $k \equiv 2j \pmod 2$. On this index model the Lean proves four facts: the singlet index $0$ occurs for $2j = 2$; removing it leaves exactly the index $2$; that index carries the spin label $2j = 4$; and the dimensions sum to $6 = 1 + 5$.

**Encoding of the label.** The electroweak spin label $2s$ of [the charge–spin theorem](#thm:ew-triplet-charge-spin-from-involution) is defined from a two-valued sector, singlet or doublet, so it takes only the values $0$ and $2$. The Lean sibling of that theorem proves that it never takes the value $4$ (`spinDouble_ne_four`), and that any map from doubled spin to a two-valued sector gives the same value to two of the spins $0, 1, 2$ (`bool_sector_not_injective_on_spins`). The obstruction therefore comes from having two values, not from the particular values chosen. The same file defines `GradedSpin`, a label $2s \in \mathbb{N}$ in the $2j$ convention of the spin labels. Its projection to the sector recovers the sector of every electroweak carrier (`GradedSpin.toSector_spinDouble`), and the value $2s = 4$ lies outside the image of the two-valued encoding (`GradedSpin.spinTwo_not_ofSector`). `GradedSpin` and the label of this proposition share the $2j$ convention; no Lean statement connects them.
