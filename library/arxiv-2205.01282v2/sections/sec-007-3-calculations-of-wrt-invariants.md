---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-007-3-calculations-of-wrt-invariants
section_title: "Calculations of WRT invariants"
section_number: 3
pages: 8-9
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.974
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#sec:WRT label="sec:WRT"}

In this section, we calculate WRT invariants of the plumbed homology sphere $M(\Gamma)$. Our starting point is the following expression by [@GPPV].

::: prop
$$\begin{aligned}
        \mathop{\mathrm{WRT}}_k(M(\Gamma))
        =
        \frac{\bm{e}(\abs{V}/8) \zeta_{4k}^{-\sum_{v \in V} (w_{v} + 3)}}
        {2 \sqrt{2k}^{\abs{V}} (\zeta_{2k} - \zeta_{2k}^{-1})}
        \sum_{\mu \in (\Z \smallsetminus k\Z)^V/2k\Z^V} \zeta_{4k}^{{}^t\!\mu W \mu}
        \prod_{v \in V} \left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)}.
    
\end{aligned}$$
:::

We can calculate WRT invariants as follows.

::: prop
[]{#prop:WRT_expression label="prop:WRT_expression"} $$\begin{aligned}
        \mathop{\mathrm{WRT}}_k(M(\Gamma))
        = \,
        &\frac{(-1)^{\abs{V_1}} \bm{e}(\abs{V_{\ge 2}}/8) \zeta_{4k}^{-\sum_{v \in V} (w_{v} + 3) - \sum_{i \in V_1} 1/w_i}}
        {2 \sqrt{2k}^{\abs{V_{\ge 2}}} (\zeta_{2k} - \zeta_{2k}^{-1}) \prod_{i \in V_1} \sqrt{\abs{w_i}}}
        \\
        &\sum_{\mu \in (\Z \smallsetminus k\Z)^{V_{\ge 2}}/2k S(\Z^{V_{\ge 2}})}
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right)
        \prod_{v \in V_{\ge 2}} G_v \left( \zeta_{2kM_v}^{\mu_v} \right).
    
\end{aligned}$$
:::

To prove this, we need the following property called "reciprocity of Gauss sums."

::: prop
[]{#prop:reciprocity label="prop:reciprocity"} Let $L$ be a lattice of finite rank $n$ equipped with a non-degenerated symmetric $\Z$-valued bilinear form $\sprod{\cdot, \cdot}$. We write $$L' \coloneqq \{ y \in L \otimes \R \mid \sprod{x, y} \in \Z \text{ for all } x \in L \}$$ for the dual lattice. Let $0 < k \in \abs{L'/L} \Z, u \in \frac{1}{k} L$, and $h \colon L \otimes \R \to L \otimes \R$ be a self-adjoint automorphism such that $h(L') \subset L'$ and $\frac{k}{2} \sprod{y, h(y)} \in \Z$ for all $y \in L'$. Let $\sigma$ be the signature of the quadratic form $\sprod{x, h(y)}$. Then it holds that $$\begin{aligned}
        &\sum_{x \in L/kL} \bm{e} \left( \frac{1}{2k} \sprod{x, h(x)} + \sprod{x, u} \right)
        = \,
        &\frac{\bm{e}(\sigma/8) k^{n/2}}{\sqrt{\abs{L'/L} \abs{\det h}}}
        \sum_{y \in L'/h(L')} \bm{e} \left( -\frac{k}{2} \sprod{y + u, h^{-1}(y + u)} \right).
    
\end{aligned}$$
:::

::: proof
*Proof of $\cref{prop:WRT_expression}$.* Idea of our proof is the same as in [@MM Proposition 6.1] which deal with the case when $\Gamma$ is the H-graph. However, our calculation is slightly different and clearer than it. To begin with, since $\zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} = 0$ for $\mu_v \in k\Z$, we can write $$\label{eq:WRT_Gauss_sum} 
        \begin{aligned}
            &\sum_{\mu \in (\Z \smallsetminus k\Z)^V/2k\Z^V} \zeta_{4k}^{{}^t\!\mu W \mu}
            \prod_{v \in V} \left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)} \\
            = \,
            &\sum_{\mu \in (\Z/ 2k \Z)^{V_1} \oplus \left( (\Z \smallsetminus k\Z) / 2k\Z \right)^{V_{ \ge 2 }}} 
            \zeta_{4k}^{{}^t\!\mu W \mu}
            \prod_{v \in V} \left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)}.
        \end{aligned}$$ Since $$\begin{aligned}
        \prod_{i \in V_1} \left( \zeta_{2k}^{\mu_i} - \zeta_{2k}^{-\mu_i} \right)
        &= 
        \prod_{i \in V_1} \sum_{l_i \in \{ \pm 1 \} } l_i \zeta_{2k}^{l_i \mu_i}
    
\end{aligned}$$ and for $\mu = (\mu_1, \mu_{\ge 2}) \in \Z^{V}, \mu_1 \in \Z^{V_1}, \mu_{\ge 2} \in \Z^{V_{\ge 2}}$ it holds that $${}^t\!\mu W \mu
    = {}^t\!\mu_{\ge 2} W \mu_{\ge 2} + \sum_{v \in V_{\ge 2}} \sum_{i \in \overline{v}} \left( w_i \mu_i^2 + 2 \mu_v \mu_i \right),$$ the right hand side of [\[eq:WRT_Gauss_sum\]](#eq:WRT_Gauss_sum){reference-type="ref" reference="eq:WRT_Gauss_sum"} can be written as $$\begin{aligned}
        \sum_{\mu_{\ge 2} \in \left( (\Z \smallsetminus k\Z) / 2k\Z \right)^{V_{ \ge 2 }}} 
        \zeta_{4k}^{{}^t\!\mu_{\ge 2} W \mu_{\ge 2}}
        \prod_{v \in V_{\ge 2}}
        &\left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)}
        \\
        &\prod_{i \in \overline{v}} \sum_{l_i \in \{ \pm 1 \} } l_i
        \sum_{\mu_i \in \Z/ 2k \Z}
        \zeta_{4k}^{w_i \mu_i^2 + 2 (\mu_v + l_i) \mu_i}.
    
\end{aligned}$$ Since the last sum for $\mu_i$ is equal to $$\frac{\bm{e}(-1/8) \sqrt{2k}}{\sqrt{\abs{w_i}}}
    \sum_{\mu_i \in \Z/ w_i \Z}
    \zeta_{4k w_i}^{ -\left( 2k \mu_i + \mu_v + l_i \right)^2 }$$ by reciprocity of Gauss sums ([\[prop:reciprocity\]](#prop:reciprocity){reference-type="ref" reference="prop:reciprocity"}), the right hand side of [\[eq:WRT_Gauss_sum\]](#eq:WRT_Gauss_sum){reference-type="ref" reference="eq:WRT_Gauss_sum"} can be written as $$\label{eq:WRT_Gauss_sum2}
        \begin{aligned}
            \frac{\bm{e}(-\abs{V_1}/8) \sqrt{2k}^{\abs{V_1}}}{\prod_{i \in V_1} \sqrt{\abs{w_i}}}
            \sum_{\mu_{\ge 2} \in \left( (\Z \smallsetminus k\Z) / 2k\Z \right)^{V_{ \ge 2 }}} 
            \zeta_{4k}^{{}^t\!\mu_{\ge 2} W \mu_{\ge 2}}
            \prod_{v \in V_{\ge 2}}
            &\left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)}
            \\
            &\prod_{i \in \overline{v}} \sum_{l_i \in \{ \pm 1 \} } l_i
            \sum_{\mu_i \in \Z/ w_i \Z}
            \zeta_{4k w_i}^{ -\left( 2k \mu_i + \mu_v + l_i \right)^2 }.
        \end{aligned}$$ Since $\bigoplus_{i \in \overline{v}} \Z/ w_i \Z \cong \Z / M_v \Z$ by the Chinese remainder theorem and [\[lem:coprime\]](#lem:coprime){reference-type="ref" reference="lem:coprime"}, the last line in [\[eq:WRT_Gauss_sum2\]](#eq:WRT_Gauss_sum2){reference-type="ref" reference="eq:WRT_Gauss_sum2"} is equal to $$\sum_{\mu'_v \in \Z/ M_v \Z}
    \prod_{i \in \overline{v}}
    \sum_{l_i \in \{ \pm 1 \} } l_i
    \zeta_{4k w_i}^{ -\left( 2k \mu'_v + \mu_v + l_i \right)^2 }.$$ By replacing $2k \mu'_v + \mu_v$ by $\mu_v$ and using [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S5\]](#item:prop:S5){reference-type="ref" reference="item:prop:S5"}, the sum for $\mu_{\ge 2}$ in [\[eq:WRT_Gauss_sum2\]](#eq:WRT_Gauss_sum2){reference-type="ref" reference="eq:WRT_Gauss_sum2"} is written as $$\begin{aligned}
        &\sum_{\mu_{\ge 2} \in (\Z \smallsetminus k\Z)^{V_{ \ge 2 }} / 2k S \left( \Z^{V_{ \ge 2 }} \right)} 
        \zeta_{4k}^{{}^t\!\mu_{\ge 2} W \mu_{\ge 2}} 
        \prod_{v \in V_{\ge 2}}
        \left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)} 
        \prod_{i \in \overline{v}} \sum_{l_i \in \{ \pm 1 \} } l_i
        \zeta_{4k w_i}^{ -\left( \mu_v + l_i \right)^2 } 
        \\
        = \,
        &\sum_{\mu_{\ge 2} \in (\Z \smallsetminus k\Z)^{V_{ \ge 2 }} / 2k S \left( \Z^{V_{ \ge 2 }} \right)} 
        \bm{e} \left( 
        \frac{1}{4k} \left( 
        {}^t\!\mu_{\ge 2} W \mu_{\ge 2}
        - \sum_{v \in V_{\ge 2}} \sum_{i \in \overline{v}} \frac{1}{w_i} \mu_v^2
        \right) \right)
        \\
        &\prod_{v \in V_{\ge 2}}
        \left( \zeta_{2k}^{\mu_v} - \zeta_{2k}^{-\mu_v} \right)^{2-\deg(v)}
        \prod_{i \in \overline{v}} \sum_{l_i \in \{ \pm 1 \} } l_i
        \zeta_{4k w_i}^{ -2 l_i \mu_v - l_i^2 }
        \\
        = \,
        &\zeta_{4k}^{- \sum_{i \in V_1} 1/w_i}
        \sum_{\mu_{\ge 2} \in (\Z \smallsetminus k\Z)^{V_{ \ge 2 }} / 2k S \left( \Z^{V_{ \ge 2 }} \right)} 
        \bm{e} \left( 
        \frac{1}{4k} \left( 
        {}^t\!\mu_{\ge 2} W \mu_{\ge 2}
        - \sum_{v \in V_{\ge 2}} \sum_{i \in \overline{v}} \frac{1}{w_i} \mu_v^2
        \right) \right) \\
        &\prod_{v \in V_{\ge 2}} (-1)^{\abs{\overline{v}}} G_v \left( \zeta_{2kM_v}^{\mu_v} \right).
    
\end{aligned}$$ By [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S3\]](#item:prop:S3){reference-type="ref" reference="item:prop:S3"}, it holds that $${}^t\!\mu_{\ge 2} W \mu_{\ge 2}
    - \sum_{v \in V_{\ge 2}} \sum_{ i \in \overline{v} } \frac{1}{w_i} \mu_v^2
    =
    -{}^t\!\mu_{\ge 2} S^{-1} \mu_{\ge 2}.$$ Thus, we obtain the claim. ◻
:::
