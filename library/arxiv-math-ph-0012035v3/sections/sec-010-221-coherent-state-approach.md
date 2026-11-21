---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-010-221-coherent-state-approach
section_title: "Coherent-state approach"
section_number: 2.2.1
pages: 17-21
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.971
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
#### Group-theoretic coherent states

According to \[ZFG90\] (see, also \[Per86\]) the group-theoretic coherent states emerge in the following construction:

1.  For $\bf g$, a semisimple Lie algebra of a Lie group $G$, we introduce the standard Cartan basis $\{H_i,E_\alpha,E_{-\alpha}\}$: $$\begin{aligned}
        \left[H_i,H_j\right]&=&0,
        \nonumber\\
        \left[H_i,E_\alpha\right]&=& \alpha_iE_\alpha,
        \nonumber\\ 
        \left[E_\alpha,E_{-\alpha}\right]&=&\alpha^iH_i,
        \nonumber\\
        \left[E_\alpha,E_\beta\right]
        &=&N_{\alpha;\beta}E_{\alpha+\beta}.
        \label{Car.bas.}
        
    \end{aligned}$$

2.  We chose a unitary irreducible representation $R$ of the group $G$, as well as a normalized state the, so-called, reference state $\left|R\right>$. The choice of the reference state is in principle arbitrary but not unessential. Usually it is an "extremal state" (the highest weight state), the state anihilated by $E_\alpha$, i.e. $E_\alpha\left|R\right>=0$.

3.  A subgroup of $G$ that consists of all the group elements $h$ that will leave the reference state $\left|R\right>$ invariant up to a phase factor is the maximum-stability subgroup $H$. Formally, $$h\left|R\right\rangle
        =
        \left|R\right\rangle e^{i\phi(h)},
        \qquad h\in H.$$ The phase factor is unimportant here because we shall generally take the expectation value of any operator in the coherent state.

4.  For every element $g\in G$, there is a unique decomposition of $g$ into a product of two group elements, one in $H$ and the other in the quotient $G/H$: $$g=\xi h,\quad g\in G,\quad h\in H,\quad \xi\in G/H.$$ In other words, we can obtain a unique coset space for a given $\left|R\right\rangle$.

5.  One can see that the action of an arbitrary group element $g\in G$ on $\left|R\right\rangle$ is given by $$g\left|R\right\rangle=
        \xi h\left|R\right\rangle=
        \xi\left|R\right\rangle e^{i\phi(h)}.$$ The combination $$\left|\xi,R\right\rangle
    \stackrel{\rm def}{=}
       \xi\left|R\right\rangle$$ is the general group definition of the coherent states. For simplicity, we will denote the coherent states as $\left|g,R\right\rangle$.

The coherent states $\left|g,R\right\rangle$ are generally non-orthogonal but normalized to unity, $$\left<g,R\right.\left|g,R\right>=1.$$ Furthermore, for an appropriately normalized measure $d\mu(g)$, we have a very important for our furher analysis identity the, so-called, resolution of unity $$\int\left|g,R\right>d\mu(g)\left<g,R\right|=I.
    \label{res.uni.}$$

#### Path integral

Our first aim is to calculate the "transition amplitude" between the two coherent states $\left|g',R\right\rangle$ and $\left|g'',R\right\rangle$ $$\begin{aligned}
    &&\left\langle g'',R\left|
{\rm P}\exp\left[i\int_{t'}^{t''}\!\!\!A(t)\,dt\right] \right|g',R\right\rangle  
\nonumber \\
    &&=\lim_{N\rightarrow\infty}    \int\ldots\int
\left\langle g_N,R\left|\left(1+i\epsilon A_N\right) \right|g_{N-1},R\right\rangle d\mu(g_{N-1})    \nonumber \\
    &&\qquad\left\langle g_{N-1},R\left|\left(1+i\epsilon A_{N-1}\right) \right|g_{N-2},R\right\rangle d\mu(g_{N-2})    \nonumber \\
    &&\qquad\ldots d\mu(g_1)\left\langle g_1,R\left|\left(1+i\epsilon A_1\right) \right|g_0,R\right\rangle,
\label{coh.pathint.}
\end{aligned}$$ where we have used [\[prel.form.\]](#prel.form.){reference-type="ref" reference="prel.form."} and [\[res.uni.\]](#res.uni.){reference-type="ref" reference="res.uni."}. To continue, one should evaluate a single amplitude (i.e. the amplitude for an infinitesimal "time" $\epsilon$), i.e. $$\begin{aligned}
    &&\left\langle g_n,R\left|\left(1+i\epsilon A_n\right)  \right|g_{n-1},R\right\rangle    \nonumber \\   
    &&=\left\langle g_n,R | g_{n-1},R\right\rangle
+i\left\langle g_n,R\left| A_n \right|g_{n-1},R\right\rangle\epsilon.
\nonumber
\end{aligned}$$ Now $$\begin{aligned}
\left\langle g_n,R | g_{n-1},R\right\rangle
    &=&\left\langle g(t_n),R|g(t_{n-1}),R\right\rangle    \nonumber \\
    &=&\left\langle R \left|g^\dagger(t_n) g(t_{n-1})\right|R\right\rangle
    =\left\langle R \left|g^\dagger(t_n) g(t_n-\epsilon)\right|R\right\rangle   \nonumber \\
    &=&\left\langle R \left|g^\dagger(t_n) \left[g(t_n)-\dot{g}(t_n)\epsilon+O\left(\epsilon^2\right)\right]\right|R\right\rangle   \nonumber \\
    &=&\left\langle R \left|g^\dagger(t_n) g(t_n)\right|R\right\rangle
-\left\langle R \left|g^\dagger(t_n) \dot{g}(t_n)\right|R\right\rangle\epsilon
+O\left(\epsilon^2\right)   \nonumber \\
    &=&1-   \left\langle R \left|g^\dagger(t_n) \dot{g}(t_n)\right|R\right\rangle\epsilon
+O\left(\epsilon^2\right),
\nonumber
\end{aligned}$$ whereas $$\begin{aligned}
    i\left\langle g_n,R\left| A_n \right|g_{n-1},R\right\rangle\epsilon
    &=&i\left\langle g(t_n),R\left| A(t_n) \right|g(t_{n-1}),R\right\rangle\epsilon   \nonumber \\
        &=&i\left\langle R\left|g^\dagger(t_n) A(t_n) g(t_n-\epsilon)\right|R\right\rangle\epsilon   \nonumber \\
&=&i\left\langle R\left|g^\dagger(t_n) A(t_n) g(t_n)\right|R\right\rangle\epsilon
+O\left(\epsilon^2\right).      
\nonumber
\end{aligned}$$ Then $$\begin{aligned}
        \lefteqn{\left\langle g_n,R\left|\left(1+i\epsilon A_n\right)   \right|g_{n-1},R\right\rangle}   \nonumber \\
    &=&1-   \left\langle R \left|g^\dagger(t_n) \dot{g}(t_n)\right|R\right\rangle\epsilon
    +i\left\langle R\left|g^\dagger(t_n) A(t_n) g(t_n)\right|R\right\rangle\epsilon
+O\left(\epsilon^2\right)   \nonumber \\
    &=&\exp{\left[\left\langle R \left|-g^\dagger(t_n) \dot{g}(t_n)
    +ig^\dagger(t_n) A(t_n) g(t_n)\right|R\right\rangle\epsilon
    +O\left(\epsilon^2\right)\right]}.
\nonumber
\end{aligned}$$ Returning to [\[coh.pathint.\]](#coh.pathint.){reference-type="ref" reference="coh.pathint."} $$\left\langle g'',R\left|
{\rm P}\exp\left[i\int_{t'}^{t''}\!\!\!A(t)\,dt\right] \right|g',R\right\rangle  
    =\int \left[D\mu(g)\right]
    \exp{\left(i\int_{t'}^{t''}\!\!\!L\, dt\right)},$$ where the "lagrangian" appearing in the path integral is defined as $$L=\left<R \left|\left[ig^\dagger(t) \dot{g}(t)
        +g^\dagger(t) A(t) g(t)\right]\right|R\right>  
        \stackrel{\rm def}{=}
        \left<R \left|A^g(t)\right|R\right>,
        \label{coh.L}$$ and $$\left[D\mu(g)\right]=\prod_{t'<t<t''} d\mu[g(t)].$$

According to \[HU00\], wee can transform $L$ in Eq.[\[coh.L\]](#coh.L){reference-type="ref" reference="coh.L"} to the form originally proposed by \[DP89\]. Namely, for any Lie-algebra element $K$ we have in the Cartan basis [\[Car.bas.\]](#Car.bas.){reference-type="ref" reference="Car.bas."} $$\left<R \left|K\right|R\right>
    =
    \left<R \left|\sum_i \lambda_i H_i
    +\ldots\right|R\right>   
    =
    \sum_i \lambda_i\left<R \left| H_i 
    \right|R\right>,$$ where dots mean $E_{\mp\alpha}$ generators vanishing between $\left|R\right>$'s. Since $$H_i\left|R\right>=m_i\left|R\right>,$$ then $$\begin{aligned}
\sum_i \lambda_i\left<R \left| H_i 
    \right|R\right>
    &=&
    \sum_i \lambda_i\left<R \left| R_i
    \right|R\right>
    =
    \sum_i \lambda_i m_i
    \nonumber\\
    &=&
    \frac{1}{\kappa}\sum_i m_i {\rm Tr}(H_iK)   
    =
    \frac{1}{\kappa} {\rm Tr}(\underline{m}
    \cdot \underline{H}\,K),
    \nonumber   
\end{aligned}$$ where the normalization $${\rm Tr}(H_i H_j)=\kappa\delta_{ij}$$ has been assumed. Thus, $$\begin{aligned}
    L&=&\left<R \left| A^g(t)\right|R\right> \nonumber\\
    &=&\frac{1}{\kappa}\sum_i{\rm Tr}
    \left[m_iH_iA^g(t)\right]\nonumber\\
    &=&\frac{1}{\kappa}{\rm Tr}
    \left\{\underline{m}\cdot\underline{H}
    \left[ig^\dagger(t) \dot{g}(t)
        +g^\dagger(t) A(t) g(t)\right]\right\}.
\end{aligned}$$

#### Non-Abelian Stokes theorem

Finally, the LHS of the non-Abelian Stokes theorem reads $$\int D\mu(g)\exp{\left(i\oint_{t'}^{t''}\!\!\!L\,
dt\right)},$$ where $$D\mu(g)=\prod_{t'\leq t<t''} d\mu[g(t)],$$ and $g(t')=g(t'')$. Or, in the language of differential forms $$\int D\mu(g)\exp{\left(i\oint_C\!\!\!L\right)},$$ where now $$D\mu(g)=\prod_{x\in C} d\mu[g(x)],$$ and $$L=\frac{1}{\kappa}\sum_i{\rm Tr}
    \left[\underline{m}\cdot\underline{H}A_i^g(x)\right]dx^i
\stackrel{\rm def}{=}
B_i\,dx^i$$ with $$A_i^g(x)=ig^\dagger(x) \partial_i g(x)
        +g^\dagger(x) A_i(x) g(x),$$ $$A^g(t)=A_i^g[x(t)]\frac{dx^i(t)}{dt}.$$ Here $B_i$ is an Abelian differential form, so obviously $$\int D\mu(g)\exp{\left(i\oint_{C=\partial S}
    \!\!\! B\right)}
 =\int D\mu(g)\exp{\left(i\int_S dB\right)}.$$
