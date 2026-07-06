## Proof

The formula $C_q = FE + (qK + q^{-1}K^{-1} - (q + q^{-1}))/(q - q^{-1})^2$ defines an element of $\mathcal{U}_q(\mathfrak{su}(2))$ provided $(q - q^{-1})$ is invertible in the ground ring $R$. We verify centrality directly using the Hecke relation $[E, F] = (K - K^{-1})/(q - q^{-1})$ and the Serre relations $KEK^{-1} = q^2 E$, $KFK^{-1} = q^{-2} F$. This computation is standard (Kassel VI.4).

Evaluating $C_q$ on the highest-weight vector $v_j$ of the spin-$j$ irrep yields its eigenvalue. Applying $K v_j = q^{2j} v_j$ and $E v_j = 0$, the $K + K^{-1}$ term simplifies to give $C_q v_j = [j]_q[j+1]_q v_j$. Therefore, $C_q|_{V_j} = [j]_q[j+1]_q \cdot \mathrm{id}$.

Over $\mathbb{F}_p, \mathbb{Q}_p, \mathbb{C}_p$, the formula holds exactly when $(q - q^{-1})$ is invertible, excluding roots of unity of small order.
