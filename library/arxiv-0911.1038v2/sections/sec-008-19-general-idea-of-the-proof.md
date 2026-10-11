---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-008-19-general-idea-of-the-proof
section_title: "General idea of the proof"
section_number: 1.9
pages: 7-12
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.872
---
For a given positive integer $g$ we define a symmetric function $k(\mu) := |\mu|+2g-1 = p_1(\mu) + 2g - 1$, therefore for a given symmetric functions $f_g$ and $h_g$ we can define symmetric functions $\tilde{f}_g(\mu) := k(\mu) \binom{k(\mu)+1}{3} f_g(\mu)$ and $\tilde{h}_g(\mu) := k(\mu) \binom{k(\mu)+1}{3} h_g(\mu)$. We notice that in equations [\[eq:lassalle1\]](#eq:lassalle1){reference-type="eqref" reference="eq:lassalle1"} and [\[eq:lassalle6\]](#eq:lassalle6){reference-type="eqref" reference="eq:lassalle6"} we sum over all partitions $\mu$ which satisfy $k(\mu) = k$. Therefore the following proposition is an immediate consequence of Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"}.

::: proposition
[]{#prop:main-prop label="prop:main-prop"} For any $g\geq 1$ there exist inhomogeneous symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$, having maximal degree $4g$, such that $$\begin{aligned}
k\ K_{k,k+1-2g} &=  \sum_{|\mu|=k+1-2g}
\big(l(\mu) + 2g - 2\big)! \ \tilde{f}_g(\mu) \mathcal{R}_\mu \\ 
 &= \sum_{|\mu|=k+1-2g}
(2g - 1)^{l(\mu)}\ \tilde{h}_g(\mu) \mathcal{Q}_\mu,
\end{aligned}$$ where $\tilde{f}_g(\mu) = \tilde{f}_g(\mu_1,\mu_2,\dots)$ and $\tilde{h}_g(\mu)
= \tilde{h}_g(\mu_1,\mu_2,\dots)$. These symmetric functions are independent of $k$.
:::

In fact, the opposite implication holds true as well and Theorem [\[theo:main\]](#theo:main){reference-type="ref" reference="theo:main"} is a consequence of Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}: roughly speaking we will show that the symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$ are divisible by the polynomial $k \binom{k+1}{3}$. One can notice that Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"} stated that $\tilde{f}_g$ and $\tilde{h}_g$ are independent of $k$, so the divisibility which we will show is a divisibility of symmetric functions $\tilde{f}_g$ and $\tilde{h}_g$ by the symmetric function $K$ which has a property that for any partition $\mu$ such that $|\mu| = k +1 - 2g$ we have that $K(\mu) = k
\binom{k+1}{3}$. We shall explain precisely what this divisibility means and show in Section [\[sec:divisibility\]](#sec:divisibility){reference-type="ref" reference="sec:divisibility"} that it holds indeed by studying the arithmetic properties of Kerov polynomials and their divisibility by prime numbers.

The remaining difficulty is to prove Proposition [\[prop:main-prop\]](#prop:main-prop){reference-type="ref" reference="prop:main-prop"}. We shall do it in Section [1](#sec:existence){reference-type="ref" reference="sec:existence"} by analysis of the Goulden-Rattan formula.

Section [\[sec:technical\]](#sec:technical){reference-type="ref" reference="sec:technical"} is a presentation of technical and complicated proofs of lemmas which are used in the previous sections.

# Goulden-Rattan formula and existence of symmetric polynomials {#sec:existence}

## Power series $P_\lambda$

Following Goulden and Rattan [@GouldenRattan2007] we define

$$C(t)=\frac{1}{1-\sum_{i\geq 2}\mathcal{R}_i t^i} = 



\sum_{\mu} t^{|\mu|} l(\mu)!\ \mathcal{R}_\mu.$$ Let $D=t \frac{d}{dt}$

and define for $m\geq 1$

$$P_m(t)=-\frac{1}{m!}C(t)\big(D+m-2\big)C(t)\cdots
\big(D+1\big)C(t)DC(t).$$

For example, we have $$\begin{aligned}
\nonumber P_1(t)&=-C(t),\\ 
\nonumber P_2(t)&=-\frac{1}{2}C(t)DC(t),\\
\nonumber

P_3(t)&
=-\frac{1}{6}
C(t)(D+1)C(t)DC(t) \\
\nonumber &= -\frac{1}{6}\left[C(t)DC(t)DC(t) + C(t)^2DC(t)\right] \\
\nonumber &= 
-\frac{1}{6}
\left[C(t)D\big(C(t)\cdot DC(t)\big) + C(t)^2DC(t)\right] \\
\nonumber &=
-\frac{1}{6}\left[C(t)\big(DC(t)\big)^2+C(t)^2D^2C(t)+C(t)^2DC(t)\right] .
\end{aligned}$$ Finally, for a partition $\lambda$, we write $P_{\lambda}(t)=\prod_{j=1}^{l(\lambda)} P_{\lambda_j}(t)$.

For $p = (p_0,\dots,p_l) \in \mathbb{N}^{l+1}$ we define

$$E(p) := C(t)^{p_0} D C(t)^{p_1} \cdots D C(t)^{p_l}.$$

::: lemma
[]{#lem:admissible label="lem:admissible"}  

1.  []{#admissible:A label="admissible:A"} Let $p \in \mathbb{N}^{l+1}, q \in \mathbb{N}^{m+1}$ and denote by $|p| := p_0 + \cdots + p_l$ ($|q| = q_0 + \cdots q_m$ respectively). Then $$E(p)\cdot E(q) = \sum_{\substack{r \in \mathbb{N}^{l+m+1}, \\ |r| = |p|+|q|}}c^{p,q}_r
    E(r),$$ where $c^{p,q}_r \in \mathbb{Z}$.

2.  []{#admissible:B label="admissible:B"} For any partition $\lambda$ the fraction $\frac{P_{\lambda}(t)}{C(t)}$ is a linear combination of terms $E(p)$ where $p \in \mathbb{N}^k$ such that $|p| =
    |\lambda|-1$ and $k \leq| \lambda|-l(\lambda)+1$.
:::

::: proof
*Proof.* Let $p = (p_0,\dots,p_l) \in \mathbb{N}^{l+1}$, $q = (q_0,\dots,q_m) \in \mathbb{N}^{m+1}$. We will show part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"} by induction on $l$. It is obvious for $l = 0$. For $l = 1$

we have: $$E(p)\cdot E(q) = E(p_0,p_1 + q_0, q_1,q_2,\dots,q_m) -
E(p_0+p_1,q_0,q_1,\dots,q_m)$$

by the Leibniz rule. Let us assume, that the inductive assertion holds for some $l \geq 1$ and let $p =
(p_0, \dots,p_{l+1})$. Then by the Leibniz rule we have that $$\label{leibnizA}
E(p)\cdot E(q) = C(t)^{p_0}D \left[ E(p')\cdot E(q)\right] -
C(t)^{p_0+p_1}\left[ E(p'')\cdot E(q')\right],$$ where $p' = (p_1,\dots,p_{l+1})$, $p'' = (0,p_2,\dots,p_{l+1})$, $q' =
(0,q_0,\dots,q_m)$.

By the inductive assertion, the right hand side of [\[leibnizA\]](#leibnizA){reference-type="eqref" reference="leibnizA"} is equal to $$\sum_{\substack{\alpha \in \mathbb{N}^{l+m+1}, \\ |\alpha| = |p|+|q|-p_0}} c_\alpha
C(t)^{p_0} D
E(\alpha) - \sum_{\substack{ \beta \in \mathbb{N}^{l+m+2}, \\|\beta| = |p|+|q|}}c_\beta
E(\beta),$$ where $c_\alpha,c_\beta \in \mathbb{Z}$. But it means that $$E(p)\cdot E(q) = \sum_{\substack{r \in \mathbb{N}^{l+m+2}, \\|r| = |p|+|q|}} c^{p,q}_r
E(r),$$ where $c^{p,q}_r \in \mathbb{Z}$ which finishes the proof of part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"}.

For part [\[admissible:B\]](#admissible:B){reference-type="ref" reference="admissible:B"} we notice that each function $P_m(t)$ is a linear combination of $E(p)$, where $p \in \mathbb{N}^k, |p| = m$ and $k \leq m-1$ and we apply part [\[admissible:A\]](#admissible:A){reference-type="ref" reference="admissible:A"}. ◻
:::

## Polynomial structure of coefficients of $P_\lambda$

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
