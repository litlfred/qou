*Proof.* Since $P_L + P_R = 1$, every element $x$ satisfies $x = x P_L + x P_R$. By definition $W P_L = \sigma^{-1} P_L$ and $W P_R = \sigma P_R$. Hence

$$
W - \sigma \;=\; (\sigma^{-1} - \sigma)\, P_L \;=\; -(q - q^{-1})\, P_L ,
$$

using $\sigma^{-1} = \sigma - h$, which follows from the Hecke relation. For consequence 1, use $P_L P_R = 0$ and $P_L^2 = P_L$. For consequence 2, write $x = a + b\,\sigma$. If $x P_R = 0$, then $x = x P_L = (a + b\mu)\, P_L$, where $\mu$ is the eigenvalue of $\sigma$ on the left line. The converse is $P_L P_R = 0$. For consequence 3, expand $t\,\sigma - t^{-1}\sigma^{-1}$ with $\sigma^{-1} = \sigma - h$. This gives $(t - t^{-1})(\sigma + t^{-1})$, which equals $(t - t^{-1})(t + t^{-1})$ times the projector onto the eigenvalue-$t$ line, and that line is $P_L$ by the choice of $t$.

The knot-level value is an exact symbolic computation over the three Wedderburn blocks of $H_3(q)$, with the convention-D weights $y_{(3)} = (q^4+1)/(q^2+1)^2$, $y_{(2,1)} = q^2/(q^2+1)^2$ and $y_{(1^3)} = 0$. The same computation reproduces $\tau_D\bigl((\sigma_1\sigma_2)^5\bigr) = q^2(q^{12}+q^8-1)/(q^2+1)^2$.

For the trace characterisation, let $\sigma_1$ and $\sigma_2$ act on the two-dimensional block by explicit matrices that satisfy the Hecke and braid relations. Then $\tau(P_R) = y_{(2,1)} + y_{(1^3)}$ and $\tau(\sigma_2 P_R) = y_{(2,1)}\,q^3/(q^2+1) - y_{(1^3)}\,q^{-1}$. If both vanish, then $y_{(2,1)}(q^4+q^2+1) = 0$, so $y_{(2,1)} = y_{(1^3)} = 0$ when $[3]_q \neq 0$. Conversely, $P_R$ is zero on the trivial block, so the remaining term $y_{(3)}\chi_{(3)}(x P_R)$ vanishes for every $x$. $\square$
