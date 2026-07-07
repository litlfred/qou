Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU, let $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a brane point $p$, and let $\mathcal{R}_p$ be the Reeb bundle over $\mathcal{S}_p$.

In the QOU, the formal variable $z$ of the vertex operator algebra is the affine coordinate $z = v_1/v_2$ on the projective line $\mathcal{S}_p$. This matches the contact affine coordinate $Z = \alpha_H / \iota_\xi\alpha$ restricted to the fibre $\mathcal{S}_p$. On the affine chart $v_2 \neq 0$, $z$ generates $\mathbb{C}[z]$.

The **vertex operator algebra** at $p$ is the triple $(V, Y, |0\rangle)$. The $\mathbb{Z}_{\geq 0}$-graded state space is the brane tower:

$$
  V = \bigoplus_{n \geq 0} V_n, \qquad V_n = A_n = J^n(A_0),
$$

where $A_0 = \mathcal{O}(\mathrm{SU}_q(2))$ and $J^n$ is the $n$-th jet prolongation. The grading $n$ is the conformal weight, defined as the eigenvalue of the zero-mode Reeb charge operator $L_0 = \xi_q^{(0)}$.

The map $Y \colon V \longrightarrow (\mathrm{End}V)[\![z, z^{-1}]\!]$ assigns to each state $a \in V_n$ the **vertex operator**:

$$
  Y(a, z) = \sum_{m \in \mathbb{Z}} a_m z^{-m-1},
$$

where the modes $a_m \in \mathrm{End}V$ derive from the $R$-matrix insertion:

$$
  a_m = \oint_{|z| = 1} Y(a, z) z^m \frac{dz}{2\pi i} = \mathrm{tr}_M\!\bigl(\check{R}_{(a)} z^m\bigr).
$$

Here $\check{R}_{(a)} = P \circ \mathcal{R}$ applies the braid operator to the state $a$, and $\mathrm{tr}_M$ is the Markov trace. The contour integral traces a fibre of the Reeb bundle $\mathcal{R}_p$.

The vacuum is the unknot $|0\rangle = 1 \in A_0$. The translation operator $T = L_{-1} = j \colon A_n \to A_{n+1}$ advances one level in the brane tower.

When insertion points $z$ and $w$ collide on $\mathcal{S}_p$, the operator product expansion

$$
  Y(a, z) Y(b, w) \sim \sum_{n \geq 0} \frac{Y(c_n, w)}{(z - w)^{n+1}}
$$

has its leading singularity governed by the Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. This corresponds to the Skein relation $L_+ - L_- = (q - q^{-1}) L_0$. The collision represents two strands meeting on $\mathcal{S}_p$. The resolution into $L_+$, $L_-$, $L_0$ forms the OPE decomposition. The eigenvalues $q$ and $-q^{-1}$ of $\sigma_i$ correspond to the symmetric and antisymmetric OPE channels.
