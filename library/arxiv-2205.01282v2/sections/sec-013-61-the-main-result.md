---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-013-61-the-main-result
section_title: "The main result"
section_number: 6.1
pages: 15-16
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.732
latex_coverage_ratio: 0.829
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:proof_main label="subsec:proof_main"}

In this subsection, we state our main result without a proof.

::: prop
[]{#prop:Gauss_vanish label="prop:Gauss_vanish"}

1.  []{#item:prop:Gauss_vanish1 label="item:prop:Gauss_vanish1"} For each vertex $v \in V_{\ge 3}$, the order of $F(\bm{t})$ at $t_v=0$ satisfies $$\ord_{t_v = 0} F(\bm{t})
            \ge
            \min \{ 0, \abs{\overline{v}} + 2 - \deg(v) \}.$$

2.  []{#item:prop:Gauss_vanish2 label="item:prop:Gauss_vanish2"} If $\abs{\overline{v}} + 2 - \deg(v) > 0$ for each vertex $v \in V_{\ge 3}$, then the meromorphic function $F(f_1; t)$ is holomorphic at $t=0$ and it holds $$\label{eq:F(f_1;0)}
                F(0) 
                = 
                \frac{\bm{e} \left( \abs{V_{\ge 2}}/8 \right)}{\sqrt{2k}^{\abs{V_{\ge 2}}} \prod_{i \in V_1} \sqrt{\abs{w_i}}}
                \sum_{ \mu \in (\Z \smallsetminus k\Z)^{V_{\ge 2}} / 2kS \left(\Z^{V_{\ge 2}} \right) } 
                \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) 
                \prod_{v \in V_{\ge 2}} G_v \left( \zeta_{2kM_v}^{\mu_v} \right).$$
:::

We obtain the following corollary by [\[prop:Gauss_vanish\]](#prop:Gauss_vanish){reference-type="ref" reference="prop:Gauss_vanish"} [\[item:prop:Gauss_vanish1\]](#item:prop:Gauss_vanish1){reference-type="ref" reference="item:prop:Gauss_vanish1"}.

::: cor
[]{#cor:Gauss_vanish label="cor:Gauss_vanish"} Suppose $\abs{\overline{v}} + 2 - \deg(v) \ge 0$ for each vertex $v \in V_{\ge 3}$. Let $e \in \{ \pm 1 \}^{V_{\ge 3}}$. Then, $c_{e, n} = 0$ holds for $n \in \Z^{V_{\ge 3}}$ such that $n_v \le -1$ for some vertex $v \in V_{\ge 3}$. In particular, for a $C^\infty$ function $f \colon \R^{V_{\ge 2}} \to \bbC$ of rapid decay as $x_v \to \infty$ for each $v \in V_{\ge 2}$, the limit $\lim_{t \to +0}F_e(f; t)$ converges and it can be written as $$\lim_{t \to +0}F_e(f; t) 
    = 
    c_{e, 0}
    =
    e_v^{\deg (v) + \abs{\overline{v}}} F(0),$$ which is independent of $f$.
:::

We obtain the following proposition by combining [\[prop:Gauss_vanish\]](#prop:Gauss_vanish){reference-type="ref" reference="prop:Gauss_vanish"} [\[item:prop:Gauss_vanish2,prop:WRT_expression\]](#item:prop:Gauss_vanish2,prop:WRT_expression){reference-type="ref" reference="item:prop:Gauss_vanish2,prop:WRT_expression"}.

::: prop
[]{#prop:WRT_F(f_1;t) label="prop:WRT_F(f_1;t)"} If $\abs{\overline{v}} + 2 - \deg(v) > 0$ for any vertices $v \in V_{\ge 3}$, then it holds that $$\mathop{\mathrm{WRT}}_k(M(\Gamma))
        = 
        \frac{(-1)^{\abs{V_1}} \zeta_{4k}^{-\sum_{v \in V} (w_{v} + 3) - \sum_{i \in V_1} 1/w_i}}
        {2(\zeta_{2k} - \zeta_{2k}^{-1})}
        F(0) .$$
:::

We obtain our main result by combining [\[prop:HB_lim,cor:Gauss_vanish,prop:WRT_F(f_1;t)\]](#prop:HB_lim,cor:Gauss_vanish,prop:WRT_F(f_1;t)){reference-type="ref" reference="prop:HB_lim,cor:Gauss_vanish,prop:WRT_F(f_1;t)"}.

::: cor
[]{#cor:HB_WRT label="cor:HB_WRT"} If $\abs{\overline{v}} + 2 - \deg(v) > 0$ for any vertices $v \in V_{\ge 3}$, then it holds that $$\mathop{\mathrm{WRT}}_k(M(\Gamma))
    =
    \frac{1}{2(\zeta_{2k} - \zeta_{2k}^{-1})}
    \lim_{q \to \zeta_k} \widehat{Z}_\Gamma (q).$$
:::
