Let $q \in K^\times$ lie in the semisimple regime of $H_3(q)$, where $[2]_q = q + q^{-1} \neq 0$ and $[3]_q = q^2 + 1 + q^{-2} \neq 0$. The standard representation $V_{(2,1)}$ of $H_3(q)$ restricts along $H_2(q) \hookrightarrow H_3(q)$ ($\sigma_1 \mapsto \sigma_1$) as the direct sum of the two one-dimensional lepton irreps:
$$
  V_{(2,1)} \big\downarrow_{H_2}
  = V_{(2)} \oplus V_{(1,1)},
$$
where $\sigma_1$ acts as the scalar $q$ on $V_{(2)}$ and as $-q^{-1}$ on $V_{(1,1)}$. At $H_2$, the irreps $V_{(2)}$ and $V_{(1,1)}$ are separate one-dimensional eigenspaces of $\sigma_1 = \mathrm{diag}(q, -q^{-1})$. At $H_3$, the second generator $\sigma_2 = \begin{pmatrix} a & b \\ b & c \end{pmatrix}$ couples them inside the $2 \times 2$ Hoefsmit block of $V_{(2,1)}$. The off-diagonal element
$$
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
  \qquad
  a_\rho = \frac{h}{1 - q^{-2\rho}},
$$
couples the two channels; both $H_2$-subspaces $V_{(2)} = K e_1$ and $V_{(1,1)} = K e_2$ are invariant under $\sigma_2$ (so that $V_{(2,1)}$ decomposes as a direct sum of $H_3$-submodules along the $H_2$-eigenspaces) if and only if $b = 0$.

By Frobenius reciprocity, for each lepton irrep $V_\mu$ with $\mu \in \{(2), (1,1)\}$:
$$
  \langle \mathrm{Res}_{H_2}^{H_3}(V_{(2,1)}), V_\mu \rangle_{H_2}
  = \langle V_{(2,1)}, \mathrm{Ind}_{H_2}^{H_3}(V_\mu) \rangle_{H_3}
  = 1.
$$
Each lepton irrep appears with multiplicity $1$ in the restriction.
