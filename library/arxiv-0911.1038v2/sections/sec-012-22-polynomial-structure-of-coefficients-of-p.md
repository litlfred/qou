---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-012-22-polynomial-structure-of-coefficients-of-p
section_title: "Polynomial structure of coefficients of P"
section_number: 2.2
pages: 9-12
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.917
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
::: definition
If $f$ is a symmetric function of degree $d$ and $2g\geq 2$ is an integer then the formal power series $$\label{eq:postac-F-nice}
F(t)=  \sum_{\mu}  t^{|\mu|}
\big(l(\mu) + 2g - 2\big)!\ f(\mu)\ \mathcal{R}_\mu$$ will be called *a power-sum of the first kind with degree $d$ and genus $g$* and the formal power series $$\label{eq:postac-F-vnice}
F(t)=  \sum_{\mu}  t^{|\mu|}(2g-1)^{l(\mu)}\ f(\mu)\ \mathcal{Q}_\mu$$ will be called *a power-sum of the second kind with degree $d$ and genus $g$*.
:::

::: lemma
[]{#lem:nice label="lem:nice"}  

1.  []{#case1 label="case1"} $C(t)$ is a power-sum of the first (respectively, second) kind with degree $0$ and genus $1$.

2.  []{#case1.5 label="case1.5"} If $F(t)$ is a power-sum of the first (respectively, second) kind with degree $d$ and genus $g$ then $D F(t)$ is a power-sum of the first (respectively, second) kind with degree $d+1$ and genus $g$.

3.  []{#case2 label="case2"} If $F(t)$ is a power-sum of the first (respectively, second) kind with degree $d$ and genus $g$ then $C(t) F(t)$ is a power-sum of the first (respectively, second) kind with degree $d$ and genus $g+\frac{1}{2}$.
:::

::: proof
*Proof.* In order to prove point [\[case1\]](#case1){reference-type="ref" reference="case1"} it suffices to notice that $$C(t)=\sum_{\mu}  t^{|\mu|} l(\mu)!\ 
\mathcal{R}_\mu = \sum_{\mu}  t^{|\mu|}\mathcal{Q}_\mu.$$

In order to prove point [\[case1.5\]](#case1.5){reference-type="ref" reference="case1.5"} let $F(t)$ be in the form [\[eq:postac-F-nice\]](#eq:postac-F-nice){reference-type="eqref" reference="eq:postac-F-nice"}. Then $$DF(t)=\sum_{\mu}  t^{|\mu|}
\big(l(\mu) + 2g - 2\big)!\ \big[ (p_1(\mu) f(\mu)\big] \
\mathcal{R}_\mu$$ is again of the form [\[eq:postac-F-nice\]](#eq:postac-F-nice){reference-type="eqref" reference="eq:postac-F-nice"}.

If $F(t)$ is of the form [\[eq:postac-F-vnice\]](#eq:postac-F-vnice){reference-type="eqref" reference="eq:postac-F-vnice"}, then $$DF(t)=\sum_{\mu}  t^{|\mu|}
(2g-1)^{l(\mu)}\ \big[ (p_1(\mu) f(\mu)\big] \
\mathcal{Q}_\mu$$ is again of the form [\[eq:postac-F-vnice\]](#eq:postac-F-vnice){reference-type="eqref" reference="eq:postac-F-vnice"} which shows part [\[case1.5\]](#case1.5){reference-type="ref" reference="case1.5"}.

For part [\[case2\]](#case2){reference-type="ref" reference="case2"} we can assume that the symmetric function $f$ is equal to monomial symmetric function $m_{\lambda}$ for some partition $\lambda$.

We define $$\begin{aligned}
 C_n & = \sum_{|\mu|=n} l(\mu)!\ \mathcal{R}_\mu = \sum_{|\mu|=n}
\mathcal{Q}_\mu, \\
\quad
\mathcal{C}_\mu & =\prod_{i \ge 2} \frac{C_i^{m_i(\mu)}}{m_i(\mu)!}.
\end{aligned}$$ The correspondence between these three families ($Q, R$ and $C$) is given by $$\begin{split}
Q_n&= \sum_{|\mu|=n} {(-1)}^{l(\mu)} (l(\mu)-1)!  \,  \mathcal{C}_\mu,\\
-\mathcal{R}_n&=\sum_{|\mu|=n} {(-1)}^{l(\mu)} \,  \mathcal{Q}_\mu=
\sum_{|\mu|=n} {(-1)}^{l(\mu)} l(\mu)!\,  \mathcal{C}_\mu.
\end{split}$$ Following Lassalle, [@Lassalle-preprint2007] we define the (formal) alphabet $\mathbb{A}$ by $$\mathcal{R}_i = - h_i(\mathbb{A}), \quad Q_i = - p_i(\mathbb{A}) / i, \quad
C_i = (-1)^{i} e_i(\mathbb{A}).$$ Writing $$u_{\mu} = l(\mu)! / \prod_{i \geq 1} m_i(\mu), \quad \epsilon_{\mu} =
(-1)^{n - l(\mu)}, \quad z_{\mu} = \prod_{i \geq 1} i^{m_i(\mu)}m_i(\mu)!,$$ the previous relations can be understood in a frame of symmetric functions theory, and they are merely the classical properties [@Macdonald1995 pp. 25 and 33] $$\begin{split}
p_n&=-n \sum_{|\mu|=n} {(-1)}^{l(\mu)} \,  u_\mu h_\mu/l(\mu)
=-n \sum_{|\mu|=n} \epsilon_\mu  u_\mu e_\mu/ l(\mu),\\
e_n&= \sum_{|\mu|=n} \epsilon_\mu u_\mu h_\mu= \sum_{|\mu|=n} \epsilon_\mu
z_{\mu}^{-1} p_{\mu},\\
h_n&=\sum_{|\mu|=n} z_{\mu}^{-1} p_{\mu}=
\sum_{|\mu|=n} \epsilon_\mu u_\mu e_\mu.
\end{split}$$

Using this notation, it suffices to show that for any monomial symmetric function $m_{\lambda}$ and any $g$ we have $$\begin{gathered}
\label{sym:R}
\bigg(\sum_{\mu} t^{|\mu|} m_{\lambda}(\mu) \frac{(l(\mu) + 2g -
2)!}{l(\mu)!} (-1)^{l(\mu)} u_{\mu} h_{\mu} \bigg) \bigg(\sum_{\rho} t^{|\rho|}
(-1)^{l(\rho)} u_{\rho} h_{\rho} \bigg) = \\
\bigg(\sum_{\nu} t^{|\nu|} \frac{m_{\lambda}(\nu)}{l(\lambda) + 2g -1}
\frac{(l(\nu) + 2g -
1)!}{l(\nu)!} (-1)^{l(\nu)} u_{\nu} h_{\nu} \bigg),
\end{gathered}$$ because the right hand side is a power-sum of the first kind with degree $|\lambda|$ and genus $g+\frac{1}{2}$, and it suffices to show, that for any monomial symmetric function $m_{\lambda}$ and any $g$ we have $$\begin{gathered}
\label{sym:Q}
\bigg(\sum_{\mu} t^{|\mu|} m_{\lambda}(\mu) (2g - 1)^{l(\mu)}
(-1)^{l(\mu)} z^{-1}_{\mu} p_{\mu} \bigg) \bigg(\sum_{\rho} t^{|\rho|}
(-1)^{l(\rho)} z^{-1}_{\rho} p_{\rho} \bigg) = \\
\bigg(\sum_{\nu} t^{|\nu|} \left(\frac{2g - 1}{2g}\right)^{l(\lambda)}
m_{\lambda}(\nu) (2g)^{l(\nu)} (-1)^{l(\nu)} z^{-1}_{\nu}
p_{\nu} \bigg),
\end{gathered}$$ because the right hand side is a power-sum of the second kind with degree $|\lambda|$ and genus $g+\frac{1}{2}$. In order to prove [\[sym:R\]](#sym:R){reference-type="eqref" reference="sym:R"} and [\[sym:Q\]](#sym:Q){reference-type="eqref" reference="sym:Q"} it is enough to use Lemma [\[lem:technical1\]](#lem:technical1){reference-type="ref" reference="lem:technical1"}. ◻
:::

The main result of this subsection is the following proposition.

::: proposition
[]{#prop:it-is-nice label="prop:it-is-nice"} $\frac{P_{\lambda}(t)}{C(t)}$ is a linear combination of power-sums of the first (respectively, second) kind of genus $\frac{|\lambda|}{2}$ and degree at most $|\lambda|-l(\lambda)$.
:::

::: proof
*Proof.* It is enough to apply Lemma [\[lem:admissible\]](#lem:admissible){reference-type="ref" reference="lem:admissible"} and Lemma [\[lem:nice\]](#lem:nice){reference-type="ref" reference="lem:nice"}. ◻
:::
