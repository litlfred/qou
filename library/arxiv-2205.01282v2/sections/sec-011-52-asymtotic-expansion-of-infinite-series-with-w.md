---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-011-52-asymtotic-expansion-of-infinite-series-with-w
section_title: "Asymtotic expansion of infinite series with weighted Gauss sums"
section_number: 5.2
pages: 13-15
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.955
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:asymp_Gauss label="subsec:asymp_Gauss"}

In this subsection, we study a family of infinite series $F(f; t)$ with weighted Gauss sums, which involves both WRT invariants and homological blocks. We start with the following asymptotic formula following from [\[prop:Euler\--Maclaurin_poly\]](#prop:Euler--Maclaurin_poly){reference-type="ref" reference="prop:Euler--Maclaurin_poly"}. In the following statement, we use notations $\varepsilon, \calS, Q$ and so on, which we prepared in [\[sec:fund_data,sec:HB_false\]](#sec:fund_data,sec:HB_false){reference-type="ref" reference="sec:fund_data,sec:HB_false"}.

::: cor
[]{#cor:asymp_F(f; t) label="cor:asymp_F(f; t)"} For $e \in \{ \pm 1 \}^{V_{\ge 3}}$ and a $C^\infty$ function $f \colon \R^{V_{\ge 2}} \to \bbC$ of rapid decay as $x_v \to \infty$ for each $v \in V_{\ge 2}$, let $$F_e(f; t) \coloneqq 
    \sum_{\alpha \in \calS} \veps(\alpha)
    \sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}}
    \bm{e}\left( \frac{1}{k} Q(e(n + \alpha)) \right) P(n) f(t(n + \alpha))$$ be a series for a variable $t \in \R_{>0}$. Then, it holds that $$\begin{aligned}
 \label{eq:asymp_F(f; t)}
        F_e(f; t) 
        \sim
        &\sum_{n \in \Z^{V_{\ge 2}}} c_{e, n} f^{(n)}(0) t^{\sum_{v \in V_{\ge 2}} n_v}
    
\end{aligned}$$ as $t \to +0$, where we define $$\begin{aligned}
        c_{e, n} = \,
        &\sum_{\alpha \in \calS} \veps(\alpha)
        \left( \prod_{v \in V_2} \frac{\alpha_v^{n_v}}{n_v!} \right)
        \sum_{m \in \Z_{\ge 0}^{V_{\ge 3}}} p_m \left( \prod_{v \in V_{\ge 3}} k^{m_v + n_v} \right)
        \sum_{\lambda \in \{ 0, \dots, k-1 \}^{V_{\ge 3}}}
        \bm{e}\left( \frac{1}{k} Q(e(\lambda + \alpha)) \right) \bbB_{m, n}(\alpha, \lambda)
    
\end{aligned}$$ for $n \in \Z^{V_{\ge 2}}$.
:::

We define two $C^\infty$ function of rapid decay $f_1, f_2 \colon \R^{V_{\ge 2}} \to \bbC$ as $f_1(x) \coloneqq \exp(-\sum_{v \in V_{\ge 2}} x_v)$ and $f_2 \coloneqq \exp(-Q(x))$ respectively. Then, WRT invariants and limit values of homological blocks can be written as limit values of $F(f_1; t)$ and $F(f_2; t)$ as $t \to 0$ shown later in [\[prop:WRT_F(f_1;t),prop:HB_lim\]](#prop:WRT_F(f_1;t),prop:HB_lim){reference-type="ref" reference="prop:WRT_F(f_1;t),prop:HB_lim"}, respectively.

Here, we need to prove that $F(f; t)$ has a limit as $t \to 0$, that is, $c_n$ vanishes for $n \in \Z^{V_{\ge 3}}$ with non-positive components. Such a result is called "a vanishing result of weighted Gauss sums" in [@MM], and it is the most important part in a proof of the conjecture of Gukov--Pei--Putrov--Vafa [@GPPV Conjecture 2.1, Equation (A.28)]. In the previous works [@BMM_high_depth; @MM], it is proved by direct calculations ([@BMM_high_depth Theorem 4.1],[@MM Proposition 4.2]). On the other hand, our proof is based on the above asymptotic expansion in [\[cor:asymp_F(f; t)\]](#cor:asymp_F(f; t)){reference-type="ref" reference="cor:asymp_F(f; t)"}. Since $c_n$ is independent of $f$ in this asymptotic expansion, it suffices to consider not for any $f$, but for $f_1$. Since $F(f_1; t)$ is a rational function shown later in [\[lem:F(f_1;t)\]](#lem:F(f_1;t)){reference-type="ref" reference="lem:F(f_1;t)"}, vanishings results of $c_n$ is equivalent to holomorphy of $F(f_1; t)$, which is proved in [\[sec:proof_main\]](#sec:proof_main){reference-type="ref" reference="sec:proof_main"}.

The homological block $\widehat{Z}_{\Gamma} (\zeta_k e^{-t^2})$ can be written in term of $F(f_2; t)$ as follows.

::: prop
[]{#prop:HB_lim label="prop:HB_lim"} It holds that $$\restrict{\left(
        (-1)^{\abs{V_1}} q^{-(\sum_{v \in V} (w_{v} + 3) + \sum_{i \in V_1} 1/w_i)/4} 
        \widehat{Z}_{\Gamma} (q) 
        \right)}{q =\zeta_k e^{-t^2}}
    = 
    \sum_{e \in \{ \pm 1 \}^{V_{\ge 3}}} \left( \prod_{v \in V_{\ge 3}} e_v^{\deg (v) + \abs{\overline{v}}} \right)
    F_e(f_2; t).$$
:::

This proposition follows from [\[prop:HB_false\]](#prop:HB_false){reference-type="ref" reference="prop:HB_false"} for $C(n) = \bm{e}\left( Q(e(n + \alpha))/k \right)$.

In the last of this subsection, we prove that $F(f_1; t)$ is a rational function related to WRT invariants. To begin with, we replace quadratic forms $Q(n + \alpha)$ as linear forms in the indices of $\zeta_k$ in the definition of $F(f; t)$.

::: lem
[]{#lem:F(f;t) label="lem:F(f;t)"} For $e \in \{ \pm 1 \}^{V_{\ge 3}}$ and a $C^\infty$ function $f \colon \R^{V_{\ge 2}} \to \bbC$ of rapid decay as $x_v \to \infty$ for each $v \in V_{\ge 2}$, it holds that $$\begin{aligned}
        F_e(f; t) = 
        &\frac{\bm{e} \left( \abs{V_{\ge 2}}/8 \right)}{\sqrt{2k}^{\abs{V_{\ge 2}}} \prod_{i \in V_1} \sqrt{\abs{w_i}}}
        \sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) \\
        &\sum_{\alpha \in \calS} \veps(\alpha)
        \sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}}
        \bm{e}\left( \frac{1}{k} {}^t\!\mu e(n + \alpha) \right) P(n) f(t(n + \alpha)).
    
\end{aligned}$$
:::

::: proof
*Proof.* Let $$G(2kS) \coloneqq
    \sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
    \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right).$$ Then, we have $G(2kS) = \left( \sqrt{2k} \bm{e} \left( -1/8 \right) \right)^{\abs{V_{\ge 2}}} \sqrt{\det S}$ by [\[prop:reciprocity\]](#prop:reciprocity){reference-type="ref" reference="prop:reciprocity"}. Here we remark $\det S = \prod_{i \in V_1} \abs{w_i}$ by [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S2\]](#item:prop:S2){reference-type="ref" reference="item:prop:S2"}. Then, we can write $$\begin{aligned}
        &G(2kS) F_e(f; t)  \\
        = \,
        &\sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
        \sum_{\alpha \in \calS} \veps(\alpha)
        \sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}}
        \bm{e}\left( \frac{1}{k} \left( Q(e(n + \alpha)) - \frac{1}{4} {}^t\!\mu S^{-1} \mu \right) \right) P(n) f(t(n + \alpha)).
    
\end{aligned}$$ By replacing $\mu$ by $\mu - 2Se(n + \alpha)$, we obtain the claim. ◻
:::

By this lemma, we obtain the following representation.

::: lem
[]{#lem:F(f_1;t) label="lem:F(f_1;t)"} For $e \in \{ \pm 1 \}^{V_{\ge 3}}$, $$\begin{aligned}
        F_e(f_1; t) = 
        e_v^{\deg (v) + \abs{\overline{v}}}
        \frac{\bm{e} \left( \abs{V_{\ge 2}}/8 \right)}{(2k)^{\abs{V_{\ge 2}}} \prod_{i \in V_1} \sqrt{\abs{w_i}}}
        \sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) 
        \prod_{v \in V_{\ge 2}} G_v \left( \zeta_{2kM_v}^{\mu_v} e^{-e_v t/2M_v} \right).
    
\end{aligned}$$ In particular, $F_e(f_1; t)$ is a meromorphic function.
:::

::: proof
*Proof.* By [\[lem:F(f;t)\]](#lem:F(f;t)){reference-type="ref" reference="lem:F(f;t)"}, we have $$\begin{aligned}
        G(2kS) F_e(f_1; t)
        = \,
        &\sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) \\
        &\sum_{\alpha \in \calS} \veps(\alpha)
        \sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}}
        \bm{e}\left( \frac{1}{k} {}^t\!\mu e(n + \alpha) \right) P(n) \exp \left( - \sum_{ v \in V_{\ge 3} } t_v (n_v + \alpha_{v}) \right).
    
\end{aligned}$$ By applying [\[lem:expansion\]](#lem:expansion){reference-type="ref" reference="lem:expansion"} for this, we have $$G(2kS) F_e(f_1; t)
    = 
    \sum_{ \mu \in \Z^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
    \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right)
    \prod_{v \in V_{\ge 2}} G_v \left( \zeta_{2kM_v}^{e_v \mu_v} e^{-t/2M_v} \right).$$ By [\[rem:G_v_symmetry\]](#rem:G_v_symmetry){reference-type="ref" reference="rem:G_v_symmetry"}, we obtain the claim. ◻
:::
