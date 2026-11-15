---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-015-relation-with-the-works-of-joyce-and-of-bridgela
section_title: "Relation with the works of Joyce, and of Bridgeland and Toledano-Laredo"
section_number: null
pages: 38-43
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.97
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\g, \Gamma$ be as in Section 2.1. We assume that the ground field is $\C$. Suppose that $C\subset \Gamma_{\R}$ is a strict convex cone. We are interested in such stability data $(Z,a)$ that $\op{Supp}a\subset C\cup (-C)$. We define $D$ as an open subset of $\op{Hom}(\Gamma, \C)$ which consists of additive maps such that $C\cap \Gamma$ is mapped into the upper-half plane ${\cal{H}}_+=\{
z\in \C\,|\,\op{Im}(z)>0\}$. We interpret $D$ as an open subset of $Stab(\g)$. Every $\alpha\in C\cap {\Gamma}$ gives rise to an invertible function (coordinate) $z_{\alpha}\in {\cal O}(D)^{\times}$ such that $z_{\alpha}(Z,a)=Z(\alpha)$.

Recall the pro-nilpotent Lie algebra $\g_C=\prod_{\gamma \in C\cap \Gamma}\g_{\gamma}$ and the corresponding pro-nilpotent group $G_C$.

In the paper [@Jo1] by D. Joyce the following system of differential equations for a collection of holomorphic functions $(f_{\alpha})_{\alpha \in C\cap {\Gamma}}, f_{\alpha}\in {\cal O}(D)\otimes \g_{\alpha}$ was considered: $$\forall \alpha \in C\cap \Gamma\,\,\,\,\,\,\,df_{\alpha}=-{1\over{2}}\sum_{\beta+\gamma=\alpha}[f_{\beta},f_{\gamma}]\,\,d\log{z_{\beta}
\over{z_{\gamma}}}\,\,.$$

It follows that if $(f_{\alpha})$ satisfies the above system of equations then the differential $1$-form $$\omega=\sum_{\alpha}f_{\alpha}d\log\,z_{\alpha}\in \Omega^1(D)\widehat{\otimes} {\g}_C:=\prod_{\alpha \in C\cap \Gamma}(\Omega^1(\g)\otimes \g_{\alpha})$$ gives rise to the flat connection, since $$d\omega+{1\over{2}}[\omega,\omega]=0\,\,.$$ Moreover, setting $F=\sum_{\alpha}f_{\alpha}$ we observe that $$dF+[\omega,F]=0\,\,,$$ i.e. $F$ is a flat section of this connection in the adjoint representation.

One can check by induction that there exists a unique solution to the above system of differential equations (modulo constants for each function $f_{\alpha}$). This means that the set of solutions is isomorphic to ${\g}_C$ (non-canonically).

For any $n\geqslant 0$ and pairwise different numbers $x_i\in \C\setminus \{0,1\},\,i=1,\dots,n$ we introduce the following function (multilogarithm) which is holomorphic when all $x_i$ lie outside of the interval $[0,1]$: $$L_n(x_1,\dots,x_n):=v.p.\int_{0<t_1<t_2<\dots<t_n<1}\prod_{1\le i\le n}{dt_i\over{t_i-x_i}}\,\,,$$ where $v.p.$ means "principal value\". Then $L_0=1,L_1(x)=\log(1-1/x)$ where we define the branch of the logarithm by taking the cut along the ray $(-\infty,0)$.

For a given collection $(f_{\alpha})$ as above, Joyce defined a collection of functions ${\cal E}_{\alpha}$ on $D$ with values in the completed universal enveloping algebra $U(\g_C)$: $${\cal E}_{\alpha}=\sum_{n\geqslant 1}\sum_{\alpha_1+\dots+\alpha_n=\alpha}f_{\alpha_1}\dots
f_{\alpha_n}I_n(z_{\alpha_1},z_{\alpha_2},\dots,z_{\alpha_n})\,\,,$$ where for $z_1,\dots,z_n\in \C$ such that $0<\op{Im}z_1<\op{Im}z_2<\dots<\op{Im}z_n$ we set[^1]

$$\begin{array}{l}
I_n(z_1,z_2,\dots,z_n):=\\
{}=2\pi i(-1)^{n-1} L_{n-1}\left({z_1\over{z_1+\dots+z_n}},{z_1+z_2\over{z_1+\dots+z_n}},\dots,
{z_1+z_2+\dots+z_{n-1}\over{z_1+\dots+z_n}}\right)\,\,.
\end{array}$$

One can show that in fact ${\cal E}_{\alpha}\in \g_C$, and it is a locally constant along strata of the stratification defined by the walls $z_{\beta}/z_{\gamma}\in \R$ where $\alpha=\beta+\gamma$ with $\beta,\gamma\in C\cap \Gamma$ and $\beta$ is not parallel to $\gamma$.

For a solution $(f_{\alpha})$ of the above system of differential equations we define a differential $1$-form on $D\times \C^{\ast}$ such that $$\widehat{\omega}:=\sum_{\alpha}f_{\alpha} e^{vz_{\alpha}}d\log(vz_{\alpha})\,\,,$$ where $v$ is the standard coordinate on $\C^{\ast}$.

Then one checks that $$d\widehat{\omega}+{1\over{2}}[\widehat{\omega},\widehat{\omega}]=0\,\,.$$ Let $M_{(f_{\alpha})}\in {G}_C$ be the monodromy of the corresponding flat connection computed along a closed loop in the complex $v$-plane, which starts at $+i\infty$ and goes in the anti-clockwise direction around $v=0$. The flatness implies that the monodromy does not depend on the point of $D$.

On the other hand let us consider the element $N_{(f_{\alpha})}\in {G}_C$ defined as $$\prod_{l\subset {\cal H}_+}^{\longrightarrow}\exp\left(\sum_{\alpha\in C\cap {\Gamma},z_{\alpha}\in l}{\cal E}_{\alpha}\right),$$ where the product is taken over all rays $l\subset {\cal H}_+$ with the vertex at the origin.

::: conj
We have $M_{(f_{\alpha})}=N_{(f_{\alpha})}$.
:::

The conjecture implies that the elements $a_{\alpha}:={\cal E}_{\alpha}$ satisfy the wall-crossing formula. The element $M_{(f_{\alpha})}$ is equal (in our notation) to the element $A_V$, where $V$ is a strict sector in ${\cal H}_+$ containing $Z(C)$. We will discuss below a sequence of identities which imply the conjecture. But we need to introduce certain functions first.

Let $\varphi:(0,1)\to \C\setminus\{0\}$ be the infinite contour which starts and ends at $+i\infty$, goes in the anti-clockwise direction and surrounds the point $0\in \C$. With the contour $\varphi$ we associate the following function on $\left({\cal H}_+\right)^n,\,n\geqslant 1$: $$K_n(z_1,\dots,z_n):=\int_{0<t_1<\dots<t_n<1}\exp\left(\sum_{1\le i\le n}\varphi(t_i)z_i\right)\prod_{1\le i\le n}\varphi^{\prime}(t_i)/\varphi(t_i)dt_i\,\,.$$ Notice that this function can be written as a Chen iterated integral

$$K_n(z_1,\dots,z_n)=\int_{\varphi}\omega_1\circ\omega_2\circ\dots\circ \omega_n\,\,,$$ where $\omega_i=e^{v z_i}dv/v, 1\le i\le n,\,\, v\in \C\setminus \{0\}$.

Let us fix $n\geqslant 1$ and a collection of complex numbers $z_i\in {\cal H}_+, \,1\le i\le n$. We call a sequence $0=i_0<i_1<\dots<i_{k-1}<i_k$ *admissible* if $$\op{Arg}(z_1+\dots+z_{i_1})\geqslant  \op{Arg}(z_{i_1+1}+\dots+z_{i_2})\geqslant \dots\geqslant \op{Arg}(z_{i_{k-1}+1}+\dots+z_{i_k})\,\,.$$ For a fixed admissible sequence we have a partition $k=l_1+\dots+l_m$ where $l_1,l_2,\dots,l_m$ are the numbers of consecutive equalities in the above sequence of inequalities for the arguments. Let $\Omega_{k,l_1,\dots,l_m}(z_1,\dots,z_n)$ be the set of all admissible sequences $0=i_0<i_1<\dots<i_{k-1}<i_k$ with the given partition $k=l_1+\dots+l_m$. Under these assumptions and notation one can see that the previous Conjecture 2 is equivalent to

::: conj
We have $$K_n(z_1,\dots,z_n)=\sum_{\Omega_{k,l_1,\dots,l_m}(z_1,\dots,z_n)}
\prod_{1\le j\le m}{1\over{l_j!}}{I}_{i_1}(z_1,\dots,z_{i_1})\cdot{I}_{i_2-i_1}(z_{i_1+1},\dots,z_{i_2})\cdot\dots$$ $$\cdot{I}_{i_k-i_{k-1}}(z_{i_{k-1}+1},\dots,z_{n})\,\,.$$
:::

Indeed, for $z_i=z_{\alpha_i},\,i=1,\dots,n$ the l.h.s. of the formula is the contribution of the term $f_{\alpha_1}\dots f_{\alpha_n}$ in the expansion of $M_{(f_{\alpha})}$. Similarly, the r.h.s. is the contribution of the same term in $N_{(f_{\alpha})}$.

Here we give a proof of the above conjecture in the special case:

::: prp
If $0<\op{Arg}\,z_1<\dots<\op{Arg}\,z_n<\pi$ then $$K_n(z_1,\dots,z_n)=I_n(z_1,z_2,\dots,z_n)\,\,.$$
:::

*Proof.* For $n=1$ both sides are equal to $2\pi i$. For $n\geqslant 2$ we proceed by induction. First one checks directly that $$dK_n(z_1,\dots,z_n)=-\sum_{i=1}^{n-1}d\log\left(\frac{z_{i+1}}{z_i}\right)\, K_{n-1}(z_1,\dots, z_i+z_{i+1},\dots,z_n)\,\,.$$ The same formula holds if we replace $K_n,K_{n-1}$ by $I_n,I_{n-1}$ respectively. Thus we see by induction that $K_n-I_n=const_n$. We want to prove that $const_n=0$. In order to do that we take $z_j=z_j(\varepsilon), 1\le j\le n$, such as follows: $$z_1(\varepsilon)=i+{1\over {\varepsilon}},\, z_n(\varepsilon)=i-{1\over {\varepsilon}},\,z_k(\varepsilon)=i-k, \,
2\le k\le n-1\,\,.$$ Here $i=\sqrt{-1}$. Then $$0<\op{Arg}\,z_1(\varepsilon)<\op{Arg}\,z_2(\varepsilon)<\dots<\op{Arg}\,z_n(\varepsilon)<\pi$$ and $|\sum_{1\le j\le k}z_j(\varepsilon)|\to \infty$ as $\varepsilon\to 0$ for $k=1,\dots,n-1$, and moreover $|\sum_{1\le j\le n}z_j(\varepsilon)|$ is a constant function of $\epsilon$. Therefore, $$I_n(z_1(\varepsilon),\dots, z_n(\varepsilon))\to 0$$ as $\varepsilon\to 0$, since all the arguments of the function $L_{n-1}$ in the definition of $I_n$ approach infinity.

Hence in order to finish the proof it suffices to show that $$K_n(z_1(\varepsilon),\dots, z_n(\varepsilon))\to 0$$ as $\varepsilon\to 0$. Here is the sketch of the proof.[^2] Notice that $$\int_{+i\infty}^{v_2}e^{v_1z_1(\varepsilon)}dv_1/v_1={1\over{z_1(\varepsilon)}}e^{v_1z_1(\varepsilon)}/v_2+
r_1(\varepsilon)\,\,,$$ where $r_1(\varepsilon)\to 0$ as $\varepsilon\to 0$. Repeating we obtain that $$K_n(z_1(\varepsilon),\dots, z_n(\varepsilon))={1\over{z_1(\varepsilon)}}
{1\over{z_1(\varepsilon)+z_2(\varepsilon)}}\dots{1\over{z_1(\varepsilon)+z_2(\varepsilon)+\dots+z_{n-1}(\varepsilon)}}\times$$ $${}\times\int_{\varphi}e^{v_n(z_1(\varepsilon)+\dots+z_n(\varepsilon))}dv_n/v_n+r_n(\varepsilon)\,\,,$$ where the integral is taken over the contour $\varphi$ described before, and $r_n(\varepsilon)\to 0$ as $\varepsilon\to 0$. It follows from our choice of numbers $z_j(\varepsilon), 1\le j\le n$ that $K_n(z_1(\varepsilon),\dots, z_n(\varepsilon))\to 0$ as $\varepsilon\to 0$. $\blacksquare$

One can hope that the technique developed in [@Jo1] helps in proving the general case.

A relationship between Joyce formulas and iterated integrals is discussed in [@BrTL] in a slightly different form. In that paper the elements $N_{(f_{\alpha})}$ are interpreted as Stokes multipliers for a different system of differential equations on $\C$ (with coordinate $t$) with values in the Lie algebra which is an extension of $\g_C$ by the abelian Lie algebra $\op{Hom}(\Gamma,\C)$ (an analog of the Cartan subalgebra). It has irregular singularity at the origin given by $Z\over{t^2}$, where $Z$ is the central charge of the stability structure. In fact the connection from [@BrTL] reduces to our connection after the change of variables $v=1/t$ and the conjugation by $\exp(-vZ)$.

[^1]: This formula was proposed in [@BrTL] as the inversion of the Joyce formula which expressed $f_{\alpha}$'s in terms of ${\cal E}_{\alpha}$'s.

[^2]: We thank Andrei Okounkov for the idea of the proof.
