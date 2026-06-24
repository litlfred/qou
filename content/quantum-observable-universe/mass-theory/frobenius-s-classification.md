**Proposition.**
*Under the Frobenius--Hopf antipode $S \colon \sigma \leftrightarrow
\sigma^{-1}$ on the Hecke algebra $H_n(R, q)$, the three log-functionals
in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) carry
exactly the following $S$-eigenvalues:*

See [Table 1](#tbl:frobenius-s-classification-table1-data).

*Together with the $S$-classification of every coefficient in the
formula:*

See [Table 2](#tbl:frobenius-s-classification-table2-data).

*Term by term, the binding correction
$\alpha\bigl(\Phi_1 - 2[3]_q\,\Phi_2 + H_A^2\,\Phi_3\bigr)$
decomposes as:*

$$
\begin{aligned}
\text{Term 1: } & \underbrace{1}_{+1} \cdot \underbrace{\Phi_1}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 2: } & \underbrace{-2[3]_q}_{+1} \cdot \underbrace{\Phi_2}_{+1} = +1 & \text{($S$-even)} \\
\text{Term 3: } & \underbrace{H_A^2}_{+1} \cdot \underbrace{\Phi_3}_{-1} = -1 & \text{($S$-odd)}
\end{aligned}
$$

*Exactly **one** of the three terms is $S$-anti-invariant, namely
the chirality term $H_A^2 \Phi_3$.  Consequently, any
$S$-symmetric ansatz for the binding correction (such as the
2-term $\alpha$-blend $\alpha V_{\mathrm{Frob}} + (1-\alpha) V_{\det}$)
necessarily lives in the 2-dimensional $S$-invariant subspace and
**cannot capture chirality** regardless of the mixing parameter.*

**Consequence.** The signed sum

$$
  \mathfrak{m}(S(\beta)) - \mathfrak{m}(\beta)
  = -2 \alpha H_A^2 \Phi_3(\beta)
$$

isolates the chirality channel as the unique source of $S$-odd
contribution to the categorical mass.  Numerically, since $S$
maps the proton braid (uud) to a braid with quark content (ddu)
(modulo strand ordering equivalent to the neutron's udd content),
this provides the structural origin of the proton-neutron mass
splitting at the Wedderburn formula level.

**Witness**:
[`computations/wedderburn_3term_inter_only.py`](#)
verifies the eigenvalue assignments numerically at $q_0$ and
confirms that $\Phi_3 \approx 0$ for inter-nucleon-only chains in
free $A=1$ nucleons (consistent with the $S$-eigenspace
decomposition).
