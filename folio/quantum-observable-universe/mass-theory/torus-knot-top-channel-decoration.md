**Definition (top-channel decoration of a torus knot).**
*Let $T_{m,p}$ be a positive torus knot presented on its braid index, so that $m \le p$, as the closure of the braid $\beta_{m,p} = (\sigma_1\sigma_2\cdots\sigma_{m-1})^{p} \in B_m$. Its writhe is $w = (m-1)p$. In the trivial one-dimensional representation of $H_m(q)$, where every $\sigma_i$ acts by $q$, the braid acts by $q^{w}$. The :defterm[top-channel decoration]{#torus-knot-top-channel-decoration} of $T_{m,p}$ is the bar-odd part of this eigenvalue under the bar involution $q \mapsto q^{-1}$:*

$$
  \delta^{\mathrm{top}}_q(T_{m,p})
  \;:=\;
  q^{w} - q^{-w},
  \qquad
  w = (m-1)p.
$$

The braid-index condition $m \le p$ is part of the definition. $T_{m,p}$ and $T_{p,m}$ are the same knot, but $(m-1)p \ne (p-1)m$ when $m \ne p$, so without the condition one knot would receive two values.

This is a scalar in $R = \mathbb{Z}[q^{\pm 1}]$. It is a different object from the $q$-dimension decoration $\delta_q(b) = (\chi_\lambda(b))_{\lambda \vdash n}$ of [delta-q-decoration definition](#def:delta-q-decoration), which is a tuple of characters, and it is not the sum of that tuple. The two agree for $m = 2$: for odd $p$ the characters of $\beta_{2,p} = \sigma_1^{p}$ on $V_{(2)}$ and $V_{(1,1)}$ are $q^{p}$ and $(-q^{-1})^{p} = -q^{-p}$, whose sum is $q^{p} - q^{-p}$. They disagree for $m = 3$. For $T_{3,5}$ the characters of $(\sigma_1\sigma_2)^{5}$ on $V_{(3)}$, $V_{(2,1)}$, $V_{(1,1,1)}$ are $q^{10}$, $-1$, $q^{-10}$, whose sum is $q^{10} - 1 + q^{-10}$, while $\delta^{\mathrm{top}}_q(T_{3,5}) = q^{10} - q^{-10}$.
