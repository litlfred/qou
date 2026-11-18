*Let $K$ be a field and $q\in K^\times$ with $q^2+1\ne0$ and $q^4+q^2+1\ne0$. Let $H_3=H_3(K,q)$ have generators $\sigma_1,\sigma_2$ with $\sigma_i^2=(q-q^{-1})\sigma_i+1$ and standard basis $\{T_w\}_{w\in S_3}$. Write $h=q-q^{-1}$, $[2]_q=q+q^{-1}$, and let $\kappa(\lambda)$ be the content sum of $\lambda$. The canonical symmetrising form is $\tau_0(T_w)=\delta_{w,1}$, with dual basis $T_w^\vee=T_{w^{-1}}$. Its Frobenius Casimir is $C_{\mathrm{Frob}}:=\sum_{w\in S_3}T_wT_{w^{-1}}$. For $z\in K$, $\mathrm{tr}^z$ is the Ocneanu trace ($\mathrm{tr}^z(1)=1$, $\mathrm{tr}^z(x\sigma_2)=z\,\mathrm{tr}^z(x)$ for $x\in H_2$), and convention D is $z_D=q^3/(q^2+1)$. Then:*

1. *(Casimir.) $C_{\mathrm{Frob}} = 6+3h(T_{s_1}+T_{s_2})+h^2(T_{s_1s_2}+T_{s_2s_1})+(q^3-q^{-3})T_{w_0}$. It is central and acts on the block $\lambda$ by $c_\lambda d_\lambda$, where $d_\lambda$ is the block dimension and the Schur elements of $\tau_0$ are $c_\lambda = q^{\kappa(\lambda)}\prod_{x\in\lambda}[h_x]_q$: $c_{(3)}=q^3[3]_q!$, $c_{(2,1)}=[3]_q$, $c_{(1^3)}=q^{-3}[3]_q!$.*
2. *(Markov weights.) $\mathrm{tr}^z=\sum_\lambda y_\lambda(z)\chi_\lambda$ with*
$$
y_{(3)}=\frac{(qz+1)(q^3z+qz+1)}{(q^2+1)(q^4+q^2+1)},\qquad
y_{(2,1)}=\frac{q(q-z)(qz+1)}{q^4+q^2+1},\qquad
y_{(1^3)}=\frac{q^2(z-q)(q^2z+z-q^3)}{(q^2+1)(q^4+q^2+1)}.
$$
*At $z_D$: $y_{(3)}=(q^4+1)/(q^2+1)^2$, $y_{(2,1)}=1/[2]_q^2$ and $y_{(1^3)}=0$.*
3. *(Trace of the Casimir.)*
$$
\mathrm{tr}^z(C_{\mathrm{Frob}}) = 6+6hz+2h^2z^2+(q^3-q^{-3})(hz^2+z),
$$
*and under convention D*
$$
\mathrm{tr}^{z_D}(C_{\mathrm{Frob}})=\frac{(q^4+q^2+1)(q^6+q^4+q^2+5)}{(q^2+1)^2},\qquad
\mathrm{tr}^{z_D}(C_{\mathrm{Frob}})-\Bigl(2+\frac1{[2]_q}\Bigr)=\frac{q^{10}+2q^8+3q^6+5q^4-q^3+2q^2-q+3}{(q^2+1)^2}.
$$
*In particular $\mathrm{tr}^{z_D}(C_{\mathrm{Frob}})\ne 2+1/[2]_q$ as rational functions of $q$ (at $q=1$ the two sides are $6$ and $5/2$).*
4. *(Inverse $q$-dimension sum.) With $\dim_q\lambda=[3]_q!/\prod_{x\in\lambda}[h_x]_q$,*
$$
\sum_{\lambda\vdash 3}\frac{1}{\dim_q\lambda} = \frac{1}{[3]_q!}\sum_{\lambda\vdash3}q^{-\kappa(\lambda)}c_\lambda = 2+\frac{1}{[2]_q},
$$
*and over the blocks on which $\mathrm{tr}^{z_D}$ is nonzero the sum is $1+1/[2]_q=(q^2+q+1)/(q^2+1)$.*
5. *(The element $C_{\dim_q}$ is not the Frobenius Casimir.) For any trace $t$ on $H_3$ with $t(e_\lambda)\ne0$ for all $\lambda$, the central element $C_{\dim_q}=\sum_\lambda e_\lambda/(\dim_q(\lambda)\,t(e_\lambda))$ of [`thm:frobenius-codim-universal`](#thm:frobenius-codim-universal) has $t(C_{\dim_q})=\sum_\lambda 1/\dim_q\lambda$ by construction. Under convention D it is undefined, because $\mathrm{tr}^{z_D}(e_{(1^3)})=0$.*

Two inputs are cited rather than formalised: that $C_{\mathrm{Frob}}$ acts on block $\lambda$ by the scalar $c_\lambda d_\lambda$ in item 1, which the Lean checks only through the trace identity it implies, and the associativity of the six-dimensional matrix model of $H_3$ used to compute in it.

So the identity $\sum_\lambda 1/\dim_q\lambda=2+1/[2]_q$ used in [`conj:partition-sum-proton-residual`](#conj:partition-sum-proton-residual) is a formal sum (item 4), and it is not the Markov trace of the Frobenius Casimir (item 3).
