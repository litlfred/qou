The classical Young seminormal form (Young \cite{young1901}, Rutherford
\cite{rutherford1948}) represents the symmetric group $S_n$ on the basis
of standard Young tableaux with diagonal entry $1/\rho$ for the
transposition $(i, i{+}1)$, where $\rho$ is the axial distance.
Hoefsmit \cite{hoefsmit1974} and independently Wenzl \cite{wenzl1988}
showed that the $q$-deformation replaces $1/\rho$ with

$$
  a_\rho = \frac{h}{1 - q^{-2\rho}},
  \quad h = q - q^{-1},
$$

which at $q = 1$ (where $h \to 0$, $q^{-2\rho} \to 1$) recovers
$a_\rho \to 1/\rho$ by l'H\^{o}pital's rule.

The Hecke relation follows from the $2 \times 2$ block structure:
for a pair of tableaux $(s, s_i)$ related by swapping $i \leftrightarrow i{+}1$,
the block

$$
  \begin{pmatrix} a_\rho & b \\ b & a_{-\rho} \end{pmatrix}
$$

has eigenvalues $q$ and $-q^{-1}$ (the two eigenvalues of $\sigma_i$), and
determinant $a_\rho \cdot a_{-\rho} - b^2 = -1$.  The off-diagonal
$b^2 = a_\rho \cdot a_{-\rho} + 1$ ensures $\det = -1$, which is
equivalent to the Hecke relation.

When the swap $s_i$ is not a valid standard tableau, the entry is
$1 \times 1$ with value $a_\rho = q$ (if $i$ and $i{+}1$ are in
the same row) or $a_\rho = -q^{-1}$ (same column).

**Connection to the $R$-matrix.**
In the quantum group $U_q(\mathfrak{sl}_2)$, the universal $R$-matrix
$\mathcal{R} \in U_q(\mathfrak{sl}_2)^{\otimes 2}$ acts on the tensor
product $V_\lambda \otimes V_\mu$ of irreducible representations.  The
Hoefsmit matrix $\rho_\lambda(\sigma_i)$ is the evaluation of $\check{R}
= P \circ \mathcal{R}$ (the braiding map) on the $i$-th and
$(i{+}1)$-th tensor factors in the $n$-fold tensor product
$V^{\otimes n}$, restricted to the isotypic component of type $\lambda$.

This identification is what allows the Hecke algebra trace
$\mathrm{tr}_M(\rho_\lambda(\beta))$ to compute the Jones polynomial
$J_K(q) = \sum_\lambda w_\lambda \cdot \chi_\lambda(\beta) / d_\lambda$,
where $\beta$ is the braid whose closure is the knot $K$.

**Application to figure-eight BW coefficients.**
The trace $\chi_{4_1}([2{,}1]) = \mathrm{tr}(\rho_{[2,1]}(\sigma_1 \sigma_2^{-1}
\sigma_1^{-1} \sigma_2)) = 2 - [3]_q$ is computed by multiplying four $2 \times 2$
Hoefsmit matrices in the standard representation of $H_3(R, q)$.  The
result $2 - [3]_q = -1 - h^2$ lands on a $q$-integer expression
because each matrix entry is a rational function of $q$, and the
trace is a Laurent polynomial in $q$.
$\qquad\blacksquare$
