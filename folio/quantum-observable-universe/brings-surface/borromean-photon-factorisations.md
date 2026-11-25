*Let $h = q - q^{-1}$ with $h \ne 0$ and $h^2 + 2 \ne 0$, over a domain. Suppose two [photons](#def:photon) satisfy $\gamma(\varphi)\,\gamma(\psi) = V^3$ with $V = \sigma_0\sigma_1^{-1}$. Suppose also that, in the formal expansion of $\gamma(\varphi)\gamma(\psi)$ in the group algebra of $B_3$, the coefficients of the four braid elements $\sigma_0$, $\sigma_1$, $\sigma_0V$, $\sigma_1V$ vanish:*

$$
  \varphi_0 + \psi_0 + \varphi_{01}\psi_1 = 0,\quad \varphi_1 + \psi_1 = 0,\quad \varphi_0\psi_{01} = 0,\quad \varphi_1\psi_{01} = 0 .
$$

*Then $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = 0$, and $\{\varphi_{01}, \psi_{01}\} = \{qh, -q^{-1}h\}$, so the factorisation is the one in [the two-photon factorisation](#prop:borromean-two-photon-factorisation).*

**Proof.** Write the six coordinate equations of $\gamma(\varphi)\gamma(\psi) = V^3$ in the basis $T_e, T_0, T_1, T_{01}, T_{10}, T_{010}$. If $\psi_{01} = 0$, a combination of these equations with the four conditions gives $h^3(h^2 + 2) = 0$, which is excluded. Otherwise the last two conditions give $\varphi_0 = \varphi_1 = 0$, and then $\psi_1 = 0$ and $\psi_0 = 0$. Both photons then lie on the line $1 + R\,V$. Because $1, V, V^2$ are linearly independent and $V^3 = 1 + h^2V - h^2V^2$, the vertex weights satisfy $\varphi_{01} + \psi_{01} = h^2$ and $\varphi_{01}\psi_{01} = -h^2$. $\square$

The four braid elements above are not linking-neutral, while $1$, $V$ and $V^2$ are. Imposing linking neutrality on each term of the expansion therefore gives exactly these four conditions.
