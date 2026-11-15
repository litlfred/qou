---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-008-4-expressions-of-homological-blocks-as-false-the
section_title: "Expressions of homological blocks as false theta functions"
section_number: 4
pages: 9-11
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.946
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#sec:HB_false label="sec:HB_false"}

In this section, we represent the homological block of $M(\Gamma)$ as a false theta function.

For the plumbed homology sphere $M(\Gamma)$, the homological block $\widehat{Z}_{\Gamma} (q)$ is defined as follows.

::: dfn
The homological block of the plumbed homology sphere $M(\Gamma)$ is defined as $$\widehat{Z}_{\Gamma} (q) 
    = 
    2^{-\abs{V}} q^{-\sum_{v \in V} (w_{v} + 3)/4} 
    \mathrm{p.v.} \int_{\abs{z_{v}}=1, v \in V} \Theta_{-W,\delta }(q; z)
    \prod_{v \in V} (z_{v} - 1/z_{v})^{2 - \deg(v)} \frac{dz_{v}}{2\pi\sqrt{-1}z_{v}},$$ where $\mathrm{p.v.}$ is the Cauchy principal value defined as $$\begin{aligned}
        \mathrm{p.v.} \int_{\abs{z} = 1}
        \coloneqq \lim_{\veps \to +0} \left( \int_{\abs{z} = 1+\veps} + \int_{\abs{z} = 1-\veps} \right),
    
\end{aligned}$$ $\delta \coloneqq (\deg(v))_{v \in V} \in \Z^V$, and $$\Theta_{-W, \delta} (q; z) \coloneqq 
    \sum_{l \in 2\Z^V + \delta} q^{-{}^t\!l W^{-1} l/4} \prod_{v \in V} z_v^{l_v}$$ is the theta function.
:::

Here we remark that our definition of the Cauchy principal value is half of the previous definition in [@GPPV] ([@GPPV p.55]). However, our definition of the homological block $\widehat{Z}_{\Gamma} (q)$ is the same as [@GPPV] since we multiply it by $2^{-\abs{V}}$.

Our main result in this section is the following.

::: prop
[]{#prop:HB_false label="prop:HB_false"} It holds $$\begin{aligned}
        \widehat{Z}_{\Gamma} (q) 
        = \,
        &(-1)^{\abs{V_1}} 2^{-\abs{V_{\ge 3}}} q^{-(\sum_{v \in V} (w_{v} + 3) + \sum_{i \in V_1} 1/w_i)/4} \\
        &\sum_{e \in \{ \pm 1 \}^{V_{\ge 3}}} \left( \prod_{v \in V_{\ge 3}} e_v^{\deg (v) + \abs{\overline{v}}} \right)
        \sum_{\alpha \in \calS} \veps(\alpha)
        \sum_{n \in \Z^{V_{\ge 3}}} P(n) q^{Q(e(n + \alpha))},
    
\end{aligned}$$ where $P(n)$ is the polynomial defined in [\[eq:prod_vertices\]](#eq:prod_vertices){reference-type="ref" reference="eq:prod_vertices"}, $Q(x) \coloneqq {}^t\!x S x$ and $ex \coloneqq ((x_v)_{v \in V_{2}}, (e_v x_v)_{v \in V_{\ge 3}})$ for $x \in \Z^{V_{\ge 2}}$ and $e \in \{ \pm 1 \}^{V_{\ge 3}}$.
:::

To prove this proposition, we need the following lemma.

::: lem
[]{#lem:Cauchy_principal_value label="lem:Cauchy_principal_value"} For $d \in \Z_{>0}$ and $l \in \Z$, it holds that $$\mathrm{p.v.} \int_{\abs{z}=1} \frac{z^{l-1}}{(z - 1/z)^{d - 2}} \frac{dz}{2\pi\sqrt{-1}}
    =
    \begin{dcases}
        -2l & d=1, l \in \{ \pm 1 \}, \\
        2 & d=2, l=0, \\
        \sgn(l)^d \binom{m+d-3}{d-3} & d \ge 3, \pm l \in d - 2 + 2m \text{ for some } m \in \Z_{\ge 0}, \\
        0 & \text{ otherwise.}
    \end{dcases}$$
:::

::: proof
*Proof of $\cref{prop:HB_false}$.* By definition, we have $$\begin{aligned}
        &2^{\abs{V}} q^{\sum_{v \in V} (w_{v} + 3)/4}
        \widehat{Z}_{\Gamma} (q) \\
        = \,
        &\sum_{l \in 2\Z^V + \delta} q^{-{}^t\!l W^{-1} l/4} 
        \prod_{v \in V}
        \mathrm{p.v.} \int_{\abs{z_v}=1}
        \frac{ z_v^{l_v - 1} }{(z_v - 1/z_v)^{\deg(v) - 2}} \frac{dz_v}{2\pi\sqrt{-1}}.
    
\end{aligned}$$ By [\[lem:Cauchy_principal_value\]](#lem:Cauchy_principal_value){reference-type="ref" reference="lem:Cauchy_principal_value"}, this is equal to $$\begin{aligned}
        \sum_{\substack{
                l = (l_1, l_2, l_{\ge 3}), \\
                l_1 \in \{ \pm 1 \}^{V_1}, \,
                l_2 = 0, \\
                \pm l_{\ge 3} \in 2\Z_{\ge -1}^{V_{\ge 3}} + \delta_{\ge 3}
        }}
        &q^{-{}^t\!l W^{-1} l/4} 
        \left( \prod_{i \in V_1} (-2l_i) \right)  2^{\abs{V_2}} \\
        &\prod_{v \in V_{\ge 3}} \sgn(l_v)^{\deg (v)} \binom{(\abs{l_v} - \deg(v) + 2)/2 + \deg(v)-3}{\deg(v)-3},
    
\end{aligned}$$ where $\delta_{\ge 3} \coloneqq (\deg(v))_{v \in V_{\ge 3}} \in \Z^{V_{\ge 3}}$. For $l = {}^t\!(\varepsilon_1, l_2, l_{\ge 3})$ with $l_2 = 0$, we have $$-{}^t\!l W^{-1} l
    = Q( l_{\ge 3} + {}^t\!T l_1) - \sum_{i \in V_1} \frac{l_i^2}{w_i}$$ by [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S1\]](#item:prop:S1){reference-type="ref" reference="item:prop:S1"}. By letting $$l_i = e_v \varepsilon_i, \quad
    l_v = e_v (n_v + \deg(v) - 2), \quad
    e_v, \varepsilon_i \in \{ \pm 1 \}, \quad
    n_v \in \Z_{\ge 0}$$ for $v \in V_{\ge 3}$ and $i \in \overline{v}$, we obtain $$\begin{aligned}
        &(-1)^{\abs{V_1}} 2^{\abs{V_{\ge 3}}} q^{(\sum_{v \in V} (w_{v} + 3) + \sum_{i \in V_1} 1/w_i)/4}
        \widehat{Z}_{\Gamma} (q) \\
        = \,
        &\sum_{e \in \{ \pm 1 \}^{V_{\ge 3}}} \left( \prod_{v \in V_{\ge 3}} e_v^{\deg (v)} \right)
        \sum_{\varepsilon \in \{ \pm 1 \}^{V_1}}
        \left( \prod_{v \in V_{\ge 3}} \prod_{i \in \overline{v}} e_v \varepsilon_i \right) \\
        &\sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}}
        q^{Q( e(n + \delta_{\ge 3}/2 + {}^t\!T \varepsilon/2 - (1, \dots, 1)) )}
        \prod_{v \in V_{\ge 3}} \binom{n_{v} + \deg(v) - 3}{n_{v}}.
    
\end{aligned}$$ Since $W^{-1} \in \Aut(\Z^V)$, every matrix entries of $S {}^t\!T$ is integers by [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S1\]](#item:prop:S1){reference-type="ref" reference="item:prop:S1"}. Thus, for any $\varepsilon \in \{ \pm 1 \}^{V_1}$, we have ${}^t\!T \varepsilon/2 \in (2S)^{-1}(\Z^{V_{\ge 2}})$. Since $$\frac{1}{2} {}^t\!T \varepsilon = \left( \sum_{i \in \overline{v}} \frac{\varepsilon_i}{2w_i} \right)_{v \in V_{\ge 2}}$$ by the definition of $T$ in [\[subsec:S\]](#subsec:S){reference-type="ref" reference="subsec:S"}, the map $$\begin{array}{ccc}
        \{ \pm 1 \}^{V_1} & \longrightarrow & \calS \\
        \varepsilon & \longmapsto & \delta_{\ge 3}/2 + {}^t\!T \varepsilon/2 - (1, \dots, 1) 
    \end{array}$$ is bijective by [\[lem:bij_calS\]](#lem:bij_calS){reference-type="ref" reference="lem:bij_calS"} [\[item:lem:bij_calS1\]](#item:lem:bij_calS1){reference-type="ref" reference="item:lem:bij_calS1"}. Thus, the claim follows by letting $\alpha = \delta_{\ge 3}/2 + {}^t\!T \varepsilon/2 - (1, \dots, 1)$. ◻
:::
