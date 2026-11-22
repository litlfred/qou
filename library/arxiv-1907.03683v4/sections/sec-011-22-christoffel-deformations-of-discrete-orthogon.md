---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-011-22-christoffel-deformations-of-discrete-orthogon
section_title: "Christoffel deformations of discrete orthogonal polynomials"
section_number: 2.2
pages: 6-8
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.963
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
Let $\omega$ be a discrete measure on $\mathbb{R}$ with infinite support and finite moments of all orders: $$\begin{aligned}
\int_{\mathbb{R}}|x|^nd\omega(x) < +\infty \quad \text{for all $n  \in \mathbb{N}$}.
\end{aligned}$$ We denote by $\{p_n\}_{n\in \mathbb{N}}$ a family of orthogonal polynomials with respect to $\omega$. The number $c_n$ stands for the leading coefficient of $p_n$, and its squared norm will be denoted by $h_n$: $$\begin{aligned}
p_n(x)&= c_nx^n + \text{terms of degree less than $n$}, \\
\int_{\mathbb{R}} p_n(x)p_m(x) d\omega(x) & = \begin{cases} 0 \quad \text{if $n \neq m$},\\
 h_n \quad \text{if $n=m$}
 \end{cases}.
\end{aligned}$$ Let $k$ be a non-negative integer and let $u_1$,\...,$u_k$ be pairwise distinct real numbers.

::: defi
The Christoffel deformation $\omega^k$ of $\omega$ of order $k$ at points $u_1$,\...,$u_k$ is the discrete measure on $\mathbb{R}$ defined by: $$\begin{aligned}
d\omega^k(x) = \prod_{j=1}^k (x-u_j)^2d\omega(x)
\end{aligned}$$
:::

Let $\{p_n^k \}_{n \in \mathbb{N}}$ be the family of monic orthogonal polynomials with respect to $\omega^k$. We have the following

::: prop
[]{#propchristoffel label="propchristoffel"} The following explicit formula holds: $$\begin{aligned}
p_n^k(x)=\left(\prod_{i=1}^k(x-u_i)^2.\delta_n^k.c_{n+2k}\right)^{-1}D_n^k(x)
\end{aligned}$$ where $$\begin{aligned}
        D_n^k(x)&= \begin{vmatrix}
        p_n(u_1) & p_{n+1}(u_1) & \dots & p_{n+2k}(u_1) \\          \vdots & \vdots & \ddots & \vdots \\
        p_n(u_k) & \dots & \dots &  p_{n+2k}(u_k) \\
        p'_n(u_1) & p'_{n+1}(u_1) & \dots & p'_{n+2k}(u_1) \\
        \vdots & \vdots & \ddots & \vdots \\
        p'_n(u_k) & \dots & \dots &  p'_{n+2k}(u_k) \\
        p_n(x) & p_{n+1}(x) & \dots & p_{n+2k}(x)
        \end{vmatrix} ; \\
        \\
        \delta_n^k &= \begin{vmatrix}
        p_n(u_1) & p_{n+1}(u_1) & \dots & p_{n+2k-1}(u_1) \\            \vdots & \vdots & \ddots & \vdots \\
        p_n(u_k) & \dots & \dots  &  p_{n+2k-1}(u_k) \\
        p'_n(u_1) & p'_{n+1}(u_1) & \dots & p'_{n+2k-1}(u_1) \\
        \vdots & \vdots & \ddots & \vdots \\
        p'_n(u_k) & p'_{n+1}(u_k) & \dots & p'_{n+2k-1}(u_k)
        \end{vmatrix}.
        
\end{aligned}$$ Its squared $l^2(\omega^k)$-norm is given by $$\begin{aligned}
h_n^k=\frac{h_n\delta_{n+1}^k}{\delta_n^k.c_{n+2k}.c_n}
\end{aligned}$$
:::

::: proof
*Proof.* We slightly adapt the proof from [@ismail], where it is assumed that the $u_i$ are outside the support of the measure $\omega$, to the case when the measure $\omega$ has infinite support, see also [@szego] and [@baikdeiftstrahov]. We first prove that $\delta_n^k \neq 0$. Let $\alpha_1, \dots, \alpha_{2k} \in \mathbb{R}$ be $2k$ real numbers such that the polynomial $$P(x):= \sum_{i=1}^{2k} \alpha_i p_{n+i-1}(x)$$ and its derivative vanish for $x \in \{u_1, \dots , u_k\}$. Then there exists a polynomial $Q$ of degree at most or equal to $n-1$ such that $$P(x)= Q(x) \prod_{i=1}^k (x-u_i)^2.$$ Since the polynomials $p_{n +i-1}$, $i=1,\dots,2k$ are orthogonal to any polynomial of degree less than or equal to $n-1$ with respect to $\omega$, we have $$\begin{aligned}
 \label{eq:orthochristoffel1} \int_\mathbb{R}Q(x) P(x) d\omega(x) = \int_\mathbb{R}Q^2(x) d\omega^k(x) = 0.
\end{aligned}$$ Since the support of the measure $\omega$ is infinite, so is the support of the measure $\omega^k$, and thus Equation ([\[eq:orthochristoffel1\]](#eq:orthochristoffel1){reference-type="ref" reference="eq:orthochristoffel1"}) implies $Q=0$ and so $P=0$ i.e. $\alpha_1=\dots=\alpha_{2k}=0$. This implies that $\delta_n^k \neq 0$.

The fact that $\delta_n^k \neq 0$ tells us that $D_n^k(x)$ is a polynomial of degree $n+2k$. Since $D_n^k(x)$ and its derivative vanish for $x \in \{u_1,\dots,u_k \}$, the rational function $p_n^k(x)$ is in facts a monic polynomial of degree $n$.

Let $q(x)$ be a polynomial of degree strictly less than $n$. From the orthogonality of the polynomials $p_n$ with respect to $\omega$, we have $$\begin{aligned}
\int_\mathbb{R}p_n^k(x) q(x) d\omega^k(x) = \frac{1}{c_{n+2k}\delta_n^k} \int_\mathbb{R}D_n^k(x) q(x) d\omega(x) = 0,
\end{aligned}$$ and the polynomials $p_n^k$ are thus orthogonal with respect to $\omega^k$. The squared norm $h_n^k$ is computed in [@bufetovqiupickrell Prop. 4.2.]. ◻
:::
