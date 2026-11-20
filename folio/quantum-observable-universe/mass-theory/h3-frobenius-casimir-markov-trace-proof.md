The proof is a finite computation in the six-dimensional left regular module, with left multiplication $T_sT_w=T_{sw}$ if $\ell(sw)>\ell(w)$ and $T_sT_w=hT_w+T_{sw}$ otherwise.

**Duality.** $\tau_0(T_vT_{w^{-1}})=\delta_{v,w}$ on all 36 pairs, so $T_w^\vee=T_{w^{-1}}$.

**Item 1.** Expanding $\sum_wT_wT_{w^{-1}}$ gives the stated coordinates, using $h^3+3h=q^3-q^{-3}$. Centrality is checked against $\sigma_1$ and $\sigma_2$. The characters are $q^{\ell(w)}$ (trivial), $(-q^{-1})^{\ell(w)}$ (sign) and $(2,h,h,-1,-1,0)$ on $(1,s_1,s_2,s_1s_2,s_2s_1,w_0)$ (reflection, from an explicit $2\times2$ representation). Solving $\tau_0=\sum_\lambda\chi_\lambda/c_\lambda$ on the basis gives the $c_\lambda$. The block scalar $c_\lambda d_\lambda$ is the standard fact $\sum_ib_ib_i^\vee\big|_{V_\lambda}=c_\lambda\chi_\lambda(1)$ for a symmetric algebra.

**Item 2.** By the Markov property and $\sigma_1\sigma_2\sigma_1\sim\sigma_1^2\sigma_2$, $\mathrm{tr}^z(T_w)=1,z,z,z^2,z^2,hz^2+z$. Solving $\mathrm{tr}^z=\sum_\lambda y_\lambda\chi_\lambda$ gives the $y_\lambda$. At $z_D$ the factor $q^2z+z-q^3$ vanishes.

**Item 3.** Apply $\mathrm{tr}^z$ to the coordinates of item 1. Substituting $z_D$ and subtracting $2+1/[2]_q=(2q^2+q+2)/(q^2+1)$ gives the remainder; at $q=1$ the left side is $6$ and the right side is $5/2$. As a check, $\mathrm{tr}^z(C_{\mathrm{Frob}})=\sum_\lambda c_\lambda d_\lambda\cdot d_\lambda y_\lambda(z)$.

**Item 4.** The hook products are $[3]_q[2]_q$, $[3]_q$ and $[3]_q[2]_q$, so the quotients of $[3]_q!$ by them are $1$, $1/[2]_q$ and $1$; and $q^{-\kappa(\lambda)}c_\lambda=\prod_x[h_x]_q$.

**Item 5.** $t(e_\lambda/(\dim_q(\lambda)t(e_\lambda)))=1/\dim_q\lambda$ for each $\lambda$.

That the multiplication rule above defines $H_3$ with its standard basis (in particular, that it is associative) is the standard textbook fact, and uniqueness of the Ocneanu trace is cited from [Jones 1987]. $\blacksquare$
