---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-003-22-properties-of-analytic-functions
section_title: "Properties of analytic functions"
section_number: 2.2
pages: 4-6
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.932
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
We shortly recall some basic characteristics of analytic functions. More information on analytic functions can be found for instance in [@E98 Chap. 6.4] and [@F95 Chap. 1, D].

It is well-known that analytic functions can be characterized by [@KP02 Prop. 2.2.10] and a standard covering argument as follows:

::: thm
[]{#thm:Tayloranalytic label="thm:Tayloranalytic"} A function $f\in C^\infty (\Omega,\mathbb{R}^n)$ on $\Omega \subseteq \mathbb{R}^m$ open, $n,m \geq 1$, is analytic on $\Omega$ if and only if for every compact set $K \subseteq \Omega$ there are positive constants $r_K$ and $C_K$ such that $$\begin{aligned}
    \|\partial^\alpha f\|_{L^\infty(K)} \leq C_K \frac{|\alpha|!}{r_K^{|\alpha|}}
    
\end{aligned}$$ holds for every multiindex $\alpha \in \mathbb N_0^m$.
:::

The previous theorem, together with the embedding of the classical Sobolev space $W^{k}=W^{k,2}$ into $C^0$ for $k\in \mathbb N$ with $k>\frac m2$, yields the following:

::: cor
A function $f\in C^\infty (\Omega,\mathbb{R}^n)$ on $\Omega \subseteq \mathbb{R}^m$ open, $n,m \geq 1$, is analytic on $\Omega$ if for every compact set $K \subset \Omega$ there are positive constants $r_K$ and $C_K$ such that $$\begin{aligned}
    \|\partial^\alpha f\|_{W^1(K)} \leq C_K \frac{|\alpha|!}{r_K^{|\alpha|}}
    
\end{aligned}$$ holds for every multiindex $\alpha \in \mathbb N_0^m.$
:::

By the equivalence of the $W^1$- and the $H^1$-norm on $\mathbb R / \mathbb Z$ as well as the embedding $H^s\subseteq H^t$ for any $t < s$ we obtain:

::: cor
[]{#cor:TayloranalyticSob label="cor:TayloranalyticSob"} Let $f\in C^\infty (\mathbb R / \mathbb Z,\mathbb{R}^n)$ and $s\in (0,1)$. Then the function $f$ is analytic on $\mathbb{R}/ \mathbb{Z}$ if there are positive constants $r$ and $C$ such that $$\begin{aligned}
    \|\partial^k f\|_{H^{1+s}} \leq C \frac{k!}{r^{k}}
    
\end{aligned}$$ holds for all integers $k \geq 0$.
:::

Furthermore, we will need a ODE version of the theorem of Cauchy-Kovalevskaya, which is originally an existence and uniqueness theorem for analytic nonlinear partial differential equations associated with Cauchy initial value problems.

::: thm
[]{#CK label="CK"} Suppose the function $g: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is real analytic around $0$ and the function $f \in C^\infty((-\varepsilon, \varepsilon),\mathbb{R}^n)$ of the form $f(x)= (f_1(x),\ldots,f_n(x))$, for any $\varepsilon > 0$, is a solution of the initial value problem $$\begin{aligned}
    \dot{f}(x) & = g (f(x)) \textnormal{ for } x \in (-\varepsilon,\varepsilon) \textnormal{ with}\\
    f(0)& =0.
    
\end{aligned}$$ Then the function $f$ is real analytic around $0$.
:::

One possible method to prove the theorem of Cauchy-Kovalevskaya is the *method of majorants* (c.f. [@F95 Chap. 1, D] or [@E98 Chap. 4.6.3, Theor. 2]). This method turns out to be useful in proving the main result of this article.

## Faà di Bruno's formula

The $k$-th derivative of the composition of two functions $f, g\in C^k (\mathbb{R},\mathbb{R})$ can be expressed by Faà di Bruno's formula which is given by $$\begin{aligned}
    &\left(\frac{d}{dt}\right)^k g(f(t)) = \\
    &\sum_{\substack{m_1+2m_2+ \cdots km_k=k, \\ m_1,\ldots,m_k\in\mathbb{N}_0}} \frac{k!}{m_1!1!^{m_1}m_2!2!^{m_2}\ldots m_k!k!^{m_k}} g^{(m_1+\cdots +m_k)}(f(t))\prod_{j=1}^{k} (f^{(j)} (t))^{m_j}.
    
\end{aligned}$$ This formula can be generalized to the multivariate case by a result of [@M00]. In our case the precise generalized Faà di Bruno's formula is not required. Nonetheless we will make use of the the following that can be easily proven from scratch by induction:

For any functions $f \in C ^k (\mathbb R, \mathbb R ^n)$ and $g \in C^k(\mathbb R ^n, \mathbb R)$, for integers $n\geq 1$ and $k\geq 0$, there exists a universial polynomial $p_k^{(n)}$ with non-negative coefficients, which are independent of $f$ and $g$, such that $$\label{eqn:FdB}
    \partial^k g(f(x)) = p_k^{(n)} (\{\partial^\alpha g\}_{|\alpha|\leq k}, \{\partial^j f_i\}_{i=1, \ldots, n, j=1, \ldots, k} ).$$ In addition, $p_k^{(n)}$ is one-homogeneous in the first entries.
