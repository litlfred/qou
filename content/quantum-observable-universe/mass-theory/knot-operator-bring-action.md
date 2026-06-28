The six Gröbner-Shirshov normal-form basis elements of $H_3(q)$
act on the Bring surface $\Sigma_4$ (genus $4$, $\chi = -6$) via
the Hecke representation. This remark makes the action explicit.

## Knot-operator action on the Bring surface

### The six basis operators

The Hecke algebra $H_3(q)$ has dimension $3! = 6$. In the
Gröbner-Shirshov normal form, the basis elements are:

| $k$ | Name | Word | Permutation | $\operatorname{tr}_M$ at $q_0$ |
|---|---|---|---|---|
| 0 | $\gamma$ (identity) | $$ | $e$ | $1.000$ |
| 1 | $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.499$ |
| 2 | $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.499$ |
| 3 | $L_+$ | $(0, 1)$ | $(1\;2\;3)$ | $0.249$ |
| 4 | $L_-$ | $(1, 0)$ | $(1\;3\;2)$ | $0.249$ |
| 5 | $e^-$ | $(0, 1, 0)$ | $(1\;3)$ | $0.551$ |

The Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$
encodes the inner-product structure: $G$ is a $6 \times 6$
symmetric positive-definite matrix whose inverse $G^{-1}$ defines
the Frobenius dual basis.

### Action on the Bring surface

Bring's surface $\Sigma_4$ has the structure of a degree-5
algebraic curve with $S_5$ symmetry. The three quark strands of a
baryon braid thread through the color-tube cubic
$\Delta(z) = z^3 + p z + r = 0$ on $\Sigma_4$, with the three
roots $z_1, z_2, z_3$ representing the quark positions on the
surface.

Each basis operator $b_k \in H_3(q)$ acts on the root triple
$(z_1, z_2, z_3)$ by permuting and $q$-deforming the roots:

| Operator | Action on roots | Geometric interpretation |
|---|---|---|
| $\gamma$ | $(z_1, z_2, z_3) \mapsto (z_1, z_2, z_3)$ | Identity — no crossing |
| $\sigma_0$ | $(z_1, z_2, z_3) \mapsto (q z_2, q^{-1} z_1, z_3)$ | Strands 1–2 cross; $q$-deformation shifts the roots along the color tube |
| $\sigma_1$ | $(z_1, z_2, z_3) \mapsto (z_1, q z_3, q^{-1} z_2)$ | Strands 2–3 cross |
| $L_+$ | $\sigma_0 \sigma_1$ | Full 3-cycle: $(1 \to 2 \to 3 \to 1)$ |
| $L_-$ | $\sigma_1 \sigma_0$ | Reverse 3-cycle: $(1 \to 3 \to 2 \to 1)$ |
| $e^-$ | $\sigma_0 \sigma_1 \sigma_0$ | Transposition $(1\;3)$ via braid relation |

The $q$-deformation factors distinguish this from the classical
$S_3$ permutation action: at $q = 1$, the action is pure
permutation; at $q = q_0 \neq 1$, each crossing
shifts the root positions along the color-tube fibre by a factor
of $q$ or $q^{-1}$.
