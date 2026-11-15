The Skein resolution obstruction provides a fourth evaluation of the universal obstruction class. Its existence as a single class rests on the [Wigner axiom](#conj:wigner-axiom): the classical-limit obstruction space is one-dimensional, $HH^2 \cong k$, spanned by a class $w(A)$ whose archimedean image is the Euler class of the base, so that its integral over the base curve is $\chi_{\mathrm{eu}}(M_0)$. Everything in this block is conditional on that axiom. It measures whether the degree-$0$ link polynomial $P_L(q)$ can be extracted from the resolution tree in polynomial depth.

Let $L = \hat{\beta}$ be a link with $c$ crossings, and let $\mathcal{R}(L)$ be its Skein resolution tree. The **Skein resolution obstruction** is the restriction of the universal class to the resolution tree:
$$
  \kappa_c^{\mathrm{comp}}(L, q)
  \;=\; 
  \mathrm{res}_{\mathcal{R}}\!\bigl(w(A)\bigr)
   \;\in\; 
  H^2(\mathcal{R}, \mathbb{G}_m).
$$
This class is proportional to the spectral, collision, and elliptic restrictions. Under the axiom a single integer, $\chi_{\mathrm{eu}}(M_0) = -6$, controls whether these computational problems persist through the classical limit.

The Kummer filtration gives:
$$
  \kappa_c^{\mathrm{comp}} \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi_{\mathrm{eu}}(M_0).
$$
The obstruction vanishes for $n \mid 6$ and persists otherwise. At root-of-unity torsion where the obstruction vanishes, the Iwahori--Hecke algebra has a radical that prunes the resolution tree. At non-vanishing torsion, even quantum interference cannot collapse the tree. Over a finite field $\mathbb{F}_p$ for $p > 7$, the obstruction persists modulo $p - 1$, but computation terminates in bounded time because the field itself is finite. Over $\mathbb{R}$ at non-torsion $q_0 \approx 1.1099$, the algebra $H_n(q_0)$ is semisimple ($\mathrm{Rad} = 0$), the full $3^c$ tree survives, and the obstruction remains non-vanishing.
