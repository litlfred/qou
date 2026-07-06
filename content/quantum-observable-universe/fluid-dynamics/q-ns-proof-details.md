**Proof of (a): q-Ladyzhenskaya inequality.**
In the eigenbasis $v = \sum_k \hat{v}_k z^k$, the advection is $\widehat{B(v)}_m = \sum_{k+\ell=m} [k]_q \hat{v}_k \hat{v}_\ell$.
By Young's convolution inequality:

$$
  \lVert B(v) \rVert_A
  \leq \lVert [k]_q \hat{v}_k \rVert_{\ell^2}
       \cdot \lVert \hat{v}_\ell \rVert_{\ell^1}
  = \lVert d_q v \rVert_A \cdot \lVert v \rVert_{\ell^1}.
$$

Cauchy--Schwarz bounds the $\ell^1$ norm: $\lVert \hat{v} \rVert_{\ell^1} \leq C_q \lVert v \rVert_{H^1_q}$. This gives the result.

**Proof of (b): Enstrophy evolution.**
We differentiate $\Omega = \sum_k [k]_q^2 |\hat{v}_k|^2$ along the q-NS flow. The dissipation term is $-2\nu_q \lVert \Delta_q v \rVert_A^2$ with $\lVert \Delta_q v \rVert_A^2 \geq \Omega$. The stretching term is bounded by the q-Ladyzhenskaya inequality. Young's inequality $ab \leq \varepsilon a^2 + b^2/(4\varepsilon)$ absorbs the stretching into the dissipation. This leaves

$$
  \frac{d\Omega}{dt}
  \leq -\nu_q\Omega + \frac{C_q^2 E_0}{\nu_q}\Omega
  = \Lambda_q\Omega.
$$

Since $\Lambda_q < \infty$ for $q > 1$, Gronwall gives at most exponential growth. There is no finite-time blowup.
At $q = 1$, we have $\nu_1 = 0$ and $C_1 = \infty$. Thus $\Lambda_1 = +\infty$. The bound gives no information.

**Proof of (c): Uniqueness.**
Set $w = v_1 - v_2$. The energy method gives

$$
\frac{d}{dt}\lVert w \rVert_A^2
\leq 2C_q (\lVert v_1 \rVert_{H^1_q}
+ \lVert v_2 \rVert_{H^1_q}) \lVert w \rVert_A^2.
$$

Gronwall with $w(0) = 0$ gives $w(t) = 0$.

