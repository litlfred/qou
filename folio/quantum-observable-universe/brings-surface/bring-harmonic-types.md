*Let $\mathcal{B}$ be Bring's surface with $\mathrm{Aut}^+(\mathcal{B}) \cong S_5$, presented by [the Bring map](#lem:bring-map-euler-characteristic). Let $E$ be any finite-dimensional $S_5$-module of functions or forms on $\mathcal{B}$, for instance an eigenspace $E_\lambda$ of the Laplacian.*

1. *(Exhaustiveness.) The character of $E$ is $\sum_\rho m_\rho\,\chi_\rho$ for unique integers $m_\rho \ge 0$, where $\rho$ runs over the seven types $[5], [1^5], [4,1], [2,1^3], [3,2], [2^2,1], [3,1^2]$. There is no other type.*
2. *(Quotients.) For $H \le S_5$, the $H$-invariant part of $E$ has dimension $d_H = \sum_\rho \dim\rho^H\, m_\rho$, and the $19 \times 7$ table $\dim \rho^H$ satisfies $\sum_\rho \dim\rho \cdot \dim\rho^H = [S_5 : H]$. The column of $[2,1^3] = \mathrm{std}\otimes\mathrm{sgn}$ is the genus of $\mathcal{B}/H$, so a quotient that is a sphere sees no harmonic of that type.*
3. *(Recovery.) For $H = S_3,\ S_3 \times S_2,\ A_4,\ F_{20},\ S_4,\ A_5,\ S_5$ the $7 \times 7$ block is unimodular, and*
$$
\begin{aligned}
m_{[5]} &= d_{S_5}, & m_{[1^5]} &= d_{A_5} - d_{S_5}, & m_{[4,1]} &= d_{S_4} - d_{S_5}, \\
m_{[3,2]} &= d_{S_3\times S_2} - d_{S_4}, & m_{[2^2,1]} &= d_{F_{20}} - d_{S_5}, & m_{[2,1^3]} &= d_{A_4} - d_{S_4} - d_{A_5} + d_{S_5}, \\
m_{[3,1^2]} &= d_{S_3} - d_{S_3\times S_2} - d_{S_4} + d_{S_5}. &&&&
\end{aligned}
$$
*So the typed Laplace spectrum of $\mathcal{B}$ is determined by the untyped spectra of six sphere orbifolds and one torus orbifold $\mathcal{B}/A_4$. The 19 rows are pairwise distinct, so $S_5$ contains no Sunada pair (item 1 of [the isospectrality question](#conj:bring-isospectrality-question)).*
4. *(One quotient suffices up to translation.) Every type has a vector fixed by $\langle(01)(23)\rangle$ and by $C_3$, so every harmonic of $\mathcal{B}$ is a sum of $S_5$-translates of lifts from the genus-2 quotient $\mathcal{B}/\langle(01)(23)\rangle$. No sphere or torus quotient has this property.*
5. *(Cellular harmonics.) The harmonic $1$-cochains of the Bring map form $2\cdot[2,1^3]$, and its vertex functions form $[5] + [4,1] + [2,1^3] + [3,2] + 2\,[2^2,1] + [3,1^2]$.*
