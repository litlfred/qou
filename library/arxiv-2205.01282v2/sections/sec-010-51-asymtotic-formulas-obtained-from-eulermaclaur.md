---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-010-51-asymtotic-formulas-obtained-from-eulermaclaur
section_title: "Asymtotic formulas obtained from Euler–Maclaurin summation formula"
section_number: 5.1
pages: 11-13
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.971
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:Euler--Maclaurin label="subsec:Euler--Maclaurin"}

Some useful methods have been developed to calculate radial limits of false theta functions. The method of Lawrence--Zagier [@LZ p. 98, Proposition] is the beginning of these. Lawrence--Zagier [@LZ] developed it by using $L$-functions for periodic maps. Zagier [@Zagier_asymptotic] collected many techniques to calculate asymptotic expansions of infinite series. In particular, [@Zagier_asymptotic Equation (44)] is the very powerful method followed by the Euler--Maclaurin summation formula. In our setting, these methods deal with the case when $\abs{V_{\ge 2}} = 1$ (in this case, $M(\Gamma)$ is a Seifert $3$-manifold). Bringmann--Kaszian--Milas [@BKM Equation (2.8)] and Bringmann--Mahlburg--Milas [@BMM_high_depth Lemma 2.2] stated the two-variable case of [@Zagier_asymptotic Equation (44)].

In this subsection, we develop a more general formula ([\[prop:Euler\--Maclaurin_poly\]](#prop:Euler--Maclaurin_poly){reference-type="ref" reference="prop:Euler--Maclaurin_poly"}) to deal with $n$-variable case with polynomial weights.

To begin with, we prepare the notation for asymptotic expansion by Poincaré.

::: dfn
Let $L$ be a positive number, $f \colon \R_{>0} \to \bbC$ be maps, $t$ be a variable of $\R_{>0}$, and $(a_n)_{n \ge -L}$ be a family of complex numbers. Then, we write $$f(t) \sim \sum_{n \ge -L} a_n t^{n} \text{ as } t \to +0$$ if for any positive number $M$ there exist positive numbers $K_M$ and $\varepsilon$ such that $$\abs{ f(t) - \sum_{-L \le n \le M} a_n t^{n} }
    \le K_M \abs{ t^{M+1}}$$ for any $0 < t < \varepsilon$. In this case, we call the infinite series $\sum_{n \ge -L} a_n t^{n}$ as the **asymptotic expansion** of $f(t)$ as $t \to +0$.
:::

Here we remark that asymptotic expansions are typically divergent series.

We also need the following terminology.

::: dfn
A function $f \colon \R \to \bbC$ is called of **rapid decay** as $x \to \infty$ if $x^m f^{(n)} (x)$ is bounded as $x \to \infty$ for any $m, n \in \Z_{\ge 0}$.
:::

Our starting point is the following lemma followed by the Euler--Maclaurin summation formula.

::: lem
[]{#lem:Euler--Maclaurin label="lem:Euler--Maclaurin"} Let $N$ be a positive number and $f \colon \R^N \to \bbC$ be a $C^\infty$ function of rapid decay as $x_1, \dots, x_N \to \infty$. Fix $\alpha \in \R^N$. Then, for a variable $t \in \R_{>0}$, an asymptotic expansion as $t \to +0$ $$\sum_{n \in \Z_{\ge 0}^N} f(t(n+\alpha))
    \sim \sum_{-1 \le n_i, \, 1 \le i \le N} \left( \prod_{1 \le i \le N} \frac{B_{n_i+1}(\alpha_i)}{(n_i+1)!} \right)
    f^{(n)}(0) t^{n_1 + \cdots + n_N}$$ holds. Here, $F(t) \sim G(t)$ means that $F(t) = G(t) + O(t^R)$ for any positive number $R$, $B_i(x)$ is the $i$-th Bernoulli polynomial, and $$g^{(-1)}(x) = \frac{d^{-1}}{d x^{-1}} g(x) \coloneqq -\int_x^\infty g(x') dx', \quad
    f^{(n)}(x) \coloneqq \frac{\partial^{n_1 + \cdots + n_N} f}{\partial x_1^{n_1} \cdots \partial x_r^{n_N}} (x).$$
:::

Here we remark that Zagier [@Zagier_asymptotic Equation (44)] stated for the case $N=1$ and Bringmann--Kaszian--Milas [@BKM Equation (2.8)] and Bringmann--Mahlburg--Milas [@BMM_high_depth Lemma 2.2] stated for the case $N=2$.

By [\[lem:Euler\--Maclaurin\]](#lem:Euler--Maclaurin){reference-type="ref" reference="lem:Euler--Maclaurin"}, we obtain the following asymptotic expansion formula.

::: prop
[]{#prop:Euler--Maclaurin_poly label="prop:Euler--Maclaurin_poly"} Let $N$ and $N'$ be non-negative integers, $f \colon \R^{N+N'} \to \bbC$ be a $C^\infty$ function of rapid decay as $x_1, \dots, x_N \to \infty$, and $P(x) = \sum_{m \in \Z_{\ge 0}^N} p_m x_1^{m_1} \cdots x_N^{m_N}$ be a polynomial. Fix $\alpha, \lambda \in \R^N$ and $\alpha' \in \R^{N'}$. Then, for a variable $t \in \R_{>0}$, an asymptotic expansion as $t \to +0$ $$\sum_{n \in \Z_{\ge 0}^N} P(\lambda + n) f(t(\alpha + \lambda + n), t\alpha')
    \sim \sum_{n \in \Z^N \times \Z_{\ge 0}^{N'}} t^{n_1 + \cdots + n_{N+N'}} f^{(n)}(0) 
    \frac{{\alpha_1'}^{n_{N+1}} \cdots {\alpha_{N'}'}^{n_{N+N'}}}{n_{N+1}! \cdots n_{N+N'}!} 
    \sum_{m \in \Z_{\ge 0}^N} p_m \bbB_{m, n}(\alpha, \lambda)$$ holds. Here we define $$\begin{aligned}
        \bbB_{m, n}(\alpha, \lambda)
        &\coloneqq
        \prod_{1 \le i \le N} \bbB_{m_i, n_i} (\alpha_i, \lambda_i), \\
        \bbB_{m_i, n_i} (\alpha_i, \lambda_i)
        &\coloneqq
        \begin{dcases}
            \sum_{0 \le l \le m_i + n_i + 1} b_{m_i, n_i, l} B_{m_i + n_i + 1 - l}(\lambda_i) \alpha_i^l & \text{ if } n_i \ge 0, \\
            \frac{m_i!}{(m_i + n_i + 1)!} (-\alpha_i)^{m_i + n_i + 1} & \text{ if } -m_i - 1 \le n_i \le -1, \\
            0 & \text{ if } n_i \le -m_i - 2,
        \end{dcases}
        \\
        b_{m_i, n_i, l} 
        &\coloneqq 
        \frac{m_i!}{(m_i + n_i + 1- l)!} \sum_{0 \le k \le l} \pmat{m_i + n_i - k \\ n_i} \frac{(-1)^k}{k! (l-k)!}.
    
\end{aligned}$$
:::

::: proof
*Proof.* It suffices to show the case when $(N, N') = (1, 0)$ or $(0,1)$. In the last case, the claim follows from the Taylor's formula. In the following, we assume $(N, N') = (1, 0)$. Let $g_\alpha(m, f; x) \coloneqq (x-\alpha)^m f(x)$. By [\[lem:Euler\--Maclaurin\]](#lem:Euler--Maclaurin){reference-type="ref" reference="lem:Euler--Maclaurin"}, we have $$\begin{aligned}
        \sum_{n \ge 0} P(\lambda + n) f(t(\alpha + \lambda + n))
        &= \sum_{m \ge 0} p_m t^{-m} \sum_{n \ge 0} \left( t(\alpha + \lambda + n) - t \alpha \right)^m f(t(\alpha + \lambda + n)) \\
        &= \sum_{m \ge 0} p_m t^{-m} \sum_{n \ge 0} g_{t \alpha}(m, f; t(\alpha + \lambda + n)) \\
        &\sim \sum_{m \ge 0} p_m t^{-m} \sum_{n \ge -1} \frac{B_{n+1}(\alpha + \lambda)}{(n+1)!} g_{t \alpha}^{(n)} (m, f; 0) t^n \\
        &= \sum_{n > - \infty} t^n \sum_{m \ge 0} p_m \frac{B_{m+n+1}(\alpha + \lambda)}{(m+n+1)!} g_{t \alpha}^{(m+n)} (m, f; 0).
    
\end{aligned}$$ We need the following lemma.

::: lem
[]{#lem:g_diff label="lem:g_diff"} For any $n \ge -1$, it holds that $$\begin{aligned}
            g_{\alpha}^{(n)}(m, f; 0)
            &=
            \sum_{0 \le l \le m} \pmat{m \\ l} \pmat{n \\ l} l! (-\alpha)^{m - l} f^{(n-l)} (0) \\
            &=
            m! \sum_{0 \le l \le m} \pmat{n \\ l} \frac{(-\alpha)^{m-l}}{(m-l)!} f^{(n-l)} (0).
        
\end{aligned}$$
:::

::: proof
*Proof.* We recall that $\binom{n}{l} = 1$ for $n=-1$ by our definition of binomial coefficients in [\[eq:binomial\]](#eq:binomial){reference-type="ref" reference="eq:binomial"}. If $n \ge 0$, then by the Leibnitz rule, we have $$g_{\alpha}^{(n)} (m, f; 0)
        =
        \sum_{0 \le l \le n} \pmat{n \\ l} \restrict{\frac{d^l}{dx^l} (x - \alpha)^m}{x=0} f^{(n-l)}(0).$$ Thus, we obtain the claim. If $n = -1$, then the claim follows by induction and $$g_{\alpha}^{(-1)} (m, f; 0)
        = (-\alpha)^m f^{(-1)} (0) + m g_{\alpha}^{(-1)} \left(m-1, f^{(-1)}; 0 \right)$$ which follows from an integration by parts. ◻
:::

We turn back to the proof of [\[prop:Euler\--Maclaurin_poly\]](#prop:Euler--Maclaurin_poly){reference-type="ref" reference="prop:Euler--Maclaurin_poly"}. By [\[lem:g_diff\]](#lem:g_diff){reference-type="ref" reference="lem:g_diff"}, we have $$\begin{aligned}
        &\sum_{n \ge 0} P(\lambda + n) f(t(\alpha + \lambda + n)) \\
        \sim 
        &\sum_{n > - \infty} t^n \sum_{m \ge 0} p_m \frac{B_{m+n+1}(\alpha + \lambda)}{(m+n+1)!}
        m! \sum_{0 \le l \le m} \pmat{m+n \\ l} \frac{(-t\alpha)^{m-l}}{(m-l)!} f^{(m+n-l)} (0).
    
\end{aligned}$$ By replacing $m+n-l$ by $n$, this can be written as $$\sum_{n > - \infty} t^n f^{(n)} (0) \sum_{m \ge 0} p_m 
    m! \sum_{0 \le l \le m} \frac{B_{n+l+1}(\alpha + \lambda)}{(n+l+1)!} \pmat{n+l \\ l} \frac{(-\alpha)^{m-l}}{(m-l)!}.$$ Thus, it suffices to show that $$\label{eq:bbB}
        \bbB_{m, n}(\alpha, \lambda)
        = 
        m! \sum_{0 \le l \le m} \frac{B_{n+l+1}(\alpha + \lambda)}{(n+l+1)!} \pmat{n+l \\ l} \frac{(-\alpha)^{m-l}}{(m-l)!}.$$ By the addition formula of Bernoulli polynomials (for example, see [@Handbook_formulas Equation 23.1.7]) $$B_i(\alpha + \lambda) = \sum_{0 \le j \le i} \pmat{i \\ j} B_j(\lambda) \alpha^j,$$ the right hand side of [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} is equal to $$m! \sum_{0 \le l \le m} \pmat{n+l \\ l} \frac{(-\alpha)^{m-l}}{(m-l)!}
    \sum_{0 \le k \le n+l+1} \frac{B_{n+l+1-k}(\lambda)}{(n+l+1-k)!} \frac{\alpha^k}{k!}.$$ By letting $i \coloneqq m+k-l, j \coloneqq m-l$, this is written as $$\sum_{0 \le i \le m+n+1} B_{m+n+1-i}(\lambda) \alpha^i
    \frac{m!}{(m+n+1-i)!} \sum_{0 \le j \le i} \pmat{m+n-j \\ n} \frac{(-1)^{j}}{j! (i-j)!}.$$ Thus, we obtain [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} for the case when $n \ge 0$. Assume $n \le -1$. Then, the right hand side of [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} is $0$ unless $m+n-j = -1$ for some $0 \le j \le i \le m+n+1$. It occurs only for the case when $i = j = m+n+1$. Thus, if $m+n+1 < 0$ then the right hand side of [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} is $0$ and [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} holds. If $m+n+1 \ge 0$, the right hand side of [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} is written as $$\frac{m!}{(m+n+1)!} (-\alpha)^{m+n+1}$$ and thus, [\[eq:bbB\]](#eq:bbB){reference-type="ref" reference="eq:bbB"} also holds in this case. ◻
:::

::: rem
If $m_i = 0$, then since $b_{0, n_i, l} = 1/l! (n_i + 1 - l)!$ we have $$\bbB_{0, n_i} (\alpha_i, \lambda_i) = B_{n_i + 1} (\lambda_i + \alpha_i)$$ by the addition formula of Bernoulli polynomials (for example, see [@Handbook_formulas Equation 23.1.7]). Thus, in this case, [\[prop:Euler\--Maclaurin_poly\]](#prop:Euler--Maclaurin_poly){reference-type="ref" reference="prop:Euler--Maclaurin_poly"} coincides with [@Zagier_asymptotic Equation (44)], [@BKM Equation (2.8)], and [@BMM_high_depth Lemma 2.2].
:::
