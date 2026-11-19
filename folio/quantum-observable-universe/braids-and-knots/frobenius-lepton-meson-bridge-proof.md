**Proof.** Assume $q \in K^\times$ satisfies the semisimplicity conditions $[2]_q = q + q^{-1} \neq 0$ and $[3]_q = q^2 + 1 + q^{-2} \neq 0$, so that $H_2(q)$ and $H_3(q)$ are semisimple over $K$.

**Step 1: Explicit $H_2(q)$-restriction of $V_{(2,1)}$.** In the Hoefsmit seminormal basis $\{e_1, e_2\}$ of the two-dimensional standard representation $V_{(2,1)}$ of $H_3(q)$ (indexed by the two standard Young tableaux of shape $(2,1)$), the generator $\sigma_1 \in H_2(q) \subset H_3(q)$ acts diagonally as
$$
  \sigma_1 = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix}.
$$
Since $q - (-q^{-1}) = q + q^{-1} = [2]_q \neq 0$, the eigenvalues $q$ and $-q^{-1}$ are distinct. The first basis line $K e_1$ carries the action $\sigma_1 e_1 = q e_1$, which is the one-dimensional trivial/symmetric representation $V_{(2)}$ of $H_2(q)$, and the second basis line $K e_2$ carries $\sigma_1 e_2 = -q^{-1} e_2$, which is the one-dimensional sign/antisymmetric representation $V_{(1,1)}$ of $H_2(q)$. Consequently, the coordinate map $(x_1, x_2) \mapsto x_1 e_1 + x_2 e_2$ is an explicit $H_2(q)$-equivariant linear isomorphism
$$
  \mathrm{Res}_{H_2}^{H_3}\bigl(V_{(2,1)}\bigr) \;\cong\; V_{(2)} \oplus V_{(1,1)}.
$$
Combo-theoretically, this matches the Pieri branching rule for $H_3(q) \downarrow H_2(q)$ obtained by removing one box from the outer corners of each partition $\lambda \vdash 3$:
$$
  V_{(3)} \big\downarrow_{H_2} = V_{(2)}, \qquad
  V_{(2,1)} \big\downarrow_{H_2} = V_{(2)} \oplus V_{(1,1)}, \qquad
  V_{(1^3)} \big\downarrow_{H_2} = V_{(1,1)}.
$$

**Step 2: Coupling via $\sigma_2$ and decoupling criterion $b = 0$.** On $V_{(2,1)} = K e_1 \oplus K e_2$, the second generator $\sigma_2 \in H_3(q)$ acts by the Hoefsmit matrix
$$
  \sigma_2 = \begin{pmatrix} a & b \\ b & c \end{pmatrix},
  \qquad
  \sigma_2(e_1) = a e_1 + b e_2,
  \qquad
  \sigma_2(e_2) = b e_1 + c e_2.
$$
The subspace $V_{(2)} = K e_1$ is invariant under $\sigma_2$ if and only if the $e_2$-component of $\sigma_2(e_1)$ vanishes, which is $b = 0$; likewise $V_{(1,1)} = K e_2$ is invariant under $\sigma_2$ if and only if the $e_1$-component of $\sigma_2(e_2)$ vanishes, which is $b = 0$. Thus the two $H_2(q)$-channels decouple under the full $H_3(q)$-action if and only if $b = 0$.

**Step 3: Frobenius reciprocity.** For the subalgebra inclusion $\iota \colon H_2(q) \hookrightarrow H_3(q)$, restriction $\mathrm{Res}_{H_2}^{H_3}$ is right adjoint to induction $\mathrm{Ind}_{H_2}^{H_3}(U) = H_3(q) \otimes_{H_2(q)} U$ (and left adjoint to coinduction $\mathrm{Hom}_{H_2(q)}(H_3(q), U)$, which is isomorphic to $\mathrm{Ind}_{H_2}^{H_3}(U)$ because $H_3(q)$ is a symmetric Frobenius algebra over $H_2(q)$ of free rank $[3:1] = 3$). In the semisimple regime, the intertwining multiplicity pairing $\langle W_1, W_2 \rangle_A := \dim_K \mathrm{Hom}_A(W_1, W_2)$ satisfies the Frobenius adjunction identity
$$
  \langle \mathrm{Res}_{H_2}^{H_3}(V_{(2,1)}), V_\mu \rangle_{H_2}
  = \dim_K \mathrm{Hom}_{H_2(q)}\bigl(\mathrm{Res}_{H_2}^{H_3}(V_{(2,1)}), V_\mu\bigr)
  = \dim_K \mathrm{Hom}_{H_3(q)}\bigl(V_{(2,1)}, \mathrm{Ind}_{H_2}^{H_3}(V_\mu)\bigr)
  = \langle V_{(2,1)}, \mathrm{Ind}_{H_2}^{H_3}(V_\mu) \rangle_{H_3}
$$
for each $\mu \in \{(2), (1,1)\}$. By Schur's lemma and Step 1, since $V_{(2)}$ and $V_{(1,1)}$ are non-isomorphic one-dimensional simple $H_2(q)$-modules ($q \neq -q^{-1}$),
$$
  \mathrm{Hom}_{H_2(q)}\bigl(V_{(2)} \oplus V_{(1,1)}, V_\mu\bigr) \;\cong\; K,
$$
so both multiplicities equal $1$ (corresponding to the induced decompositions $\mathrm{Ind}_{H_2}^{H_3}(V_{(2)}) \cong V_{(3)} \oplus V_{(2,1)}$ and $\mathrm{Ind}_{H_2}^{H_3}(V_{(1,1)}) \cong V_{(2,1)} \oplus V_{(1,1,1)}$, each of dimension $1 + 2 = 3$). $\square$
