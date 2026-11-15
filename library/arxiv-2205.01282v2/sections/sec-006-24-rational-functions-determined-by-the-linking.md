---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-006-24-rational-functions-determined-by-the-linking
section_title: "Rational functions determined by the linking matrix"
section_number: 2.4
pages: 6-8
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.962
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:rat_func label="subsec:rat_func"}

In this subsection, we introduce rational functions determined by the linking matrix and prove its basic properties.

For a vertex $v \in V_{\ge 2}$ and complex variable $q$, define a rational function $$G_v (q) \coloneqq (q^{M_{v}} - q^{-M_{v}})^{2 - \deg(v)} \prod_{i \in \overline{v}} \left( q^{M_{v} / w_{i}} - q^{-M_{v} / w_{i}} \right).$$

It has the following Laurent expansion.

::: rem
[]{#rem:G_v_symmetry label="rem:G_v_symmetry"} $G_v(q^{-1}) = (-1)^{\deg (v) + \abs{\overline{v}}} G_v(q)$.
:::

The rational function $G_v (q)$ has the following Laurent expansion.

::: lem
[]{#lem:expansion_v label="lem:expansion_v"} For a vertex $v \in V_{\ge 2}$, $G_{v} (q)$ is expanded as $$G_{v} (q)
    =
    \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) \sum_{n_{v} = 0}^{\infty} \binom{n_{v} + \deg(v) - 3}{n_{v}} q^{2M_{v}(n_{v} + \alpha_{v})}$$ for $0 < \abs{q}^{\sgn{M_v}} < 1$. Here we define $$\label{eq:binomial}
        \pmat{m \\ l}
        \coloneqq
        \begin{dcases}
            \frac{m!}{l! (m-l)!} & \text{ if } 0 \le l \le m, \\
            1 & \text{ if } m=-1, \\
            0 & \text{ otherwise}.
        \end{dcases}$$
:::

::: proof
*Proof.* The claim follows from [\[lem:epsilon\]](#lem:epsilon){reference-type="ref" reference="lem:epsilon"} [\[item:lem:epsilon4\]](#item:lem:epsilon4){reference-type="ref" reference="item:lem:epsilon4"} and the binomial theorem $$(1-q)^{-d} = \sum_{n=0}^{\infty} \pmat{n+d-1 \\n} q^n$$ which holds for any integer $d \ge 0$. ◻
:::

The rational function $G_v (q)$ is expanded at $q=1$ as follows.

::: lem
[]{#lem:G_v_at_1 label="lem:G_v_at_1"} For a vertex $v \in V_{\ge 2}$, it holds that $$G_v(q) = 2^{2 - \deg(v) + \abs{\overline{v}}} (M_v)^{1 - \deg(v) + \abs{\overline{v}}} (q-1)^{2 - \deg(v) + \abs{\overline{v}}}
    +O((q-1)^{3 - \deg(v) + \abs{\overline{v}}}).$$
:::

::: proof
*Proof.* The idea of our proof is due to Akihito Mori. The claim follows from $$\begin{aligned}
        G_v(q)
        &= q^{(\deg(v) - 1 - \sum_{i \in \overline{v}} 1/w_i) M_v} 
        (q^{2M_{v}} - 1)^{2 - \deg(v)} (q-1)^{\overline{v}}
        \prod_{i \in \overline{v}} \frac{q^{2M_{v} / w_{i}} - 1}{q-1} \\
        &= q^{(\deg(v) - 1 - \sum_{i \in \overline{v}} 1/w_i) M_v}
        (1 + q + \cdots + q^{2M_v - 1})^{2 - \deg(v)} (q-1)^{2 - \deg(v) + \overline{v}} 
        \prod_{i \in \overline{v}} \frac{q^{2M_{v} / w_{i}} - 1}{q-1}
    
\end{aligned}$$ and $$\lim_{q \to 1} \frac{q^{2M_{v} / w_{i}} - 1}{q-1}
    = \lim_{q \to 1} \left( 1 + q + \cdots + q^{2M_v / w_i - 1} \right)
    = \frac{2M_{v}}{w_i}.$$ ◻
:::

[\[lem:FIMT\]](#lem:FIMT){reference-type="ref" reference="lem:FIMT"} follows from [\[lem:G_v_at_1\]](#lem:G_v_at_1){reference-type="ref" reference="lem:G_v_at_1"}. Thus, [\[lem:G_v_at_1\]](#lem:G_v_at_1){reference-type="ref" reference="lem:G_v_at_1"} is a refinement of [\[lem:FIMT\]](#lem:FIMT){reference-type="ref" reference="lem:FIMT"}.

::: proof
*Proof of $\cref{lem:FIMT}$.* Since $$G_{v} (q)
    =
    (q^{2M_{v}} - 1)^{2 - \deg(v)}
    \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) q^{2M_{v} \alpha_{v}},$$ we have $$G_{v} (e^{-t})
    =
    \left( t^{2 - \deg(v)} + O(t^{3 - \deg(v)}) \right) 
    \sum_{n = 0}^{\infty} \frac{(-2M_v t)^{n}}{n!}
    \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) \alpha_v^n.$$ Since $G_{v} (e^{-t}) = O(t^{2 - \deg(v) + \abs{\overline{v}}})$ by [\[lem:G_v_at_1\]](#lem:G_v_at_1){reference-type="ref" reference="lem:G_v_at_1"}, we obtain the claim. ◻
:::

At the end of this section, we consider products for vertices.

For $n \in \Z^{V_{\ge 3}}$, we denote $$\label{eq:prod_vertices}
    P(n) \coloneqq \prod_{v \in V_{\ge 4}} \frac{(n_{v} + \deg(v) - 3)(n_{v} + \deg(v) - 4) \cdots (n_v +1)}{(\deg(v) - 3)!}.$$ We remark that for $n \in \Z_{\ge -1}^{V_{\ge 3}}$ it holds that $$P(n) = \prod_{v \in V_{\ge 4}} \binom{n_{v} + \deg(v) - 3}{n_{v}}
= \prod_{v \in V_{\ge 3}} \binom{n_{v} + \deg(v) - 3}{n_{v}}$$ by our definition of binomial coefficients in [\[eq:binomial\]](#eq:binomial){reference-type="ref" reference="eq:binomial"}.

For each complex number $z$, we denote $\bm{e}(z) \coloneqq e^{2\pi\iu z}$. We fix a positive integer $k$ and denote $\zeta_k \coloneqq e^{2\pi\iu/k}$.

Then, the following holds by [\[lem:expansion_v\]](#lem:expansion_v){reference-type="ref" reference="lem:expansion_v"}.

::: lem
[]{#lem:expansion label="lem:expansion"} For $\mu \in \Z^{V_{\ge 2}}$ and $t \in \R^{V_{\ge 2}}_{>0}$, it holds that $$\prod_{v \in V_{\ge 2}} G_{v} \left( \zeta_{2k M_v}^{\mu_v} e^{-t_v/2M_v} \right) 
    =
    \sum_{\alpha \in \calS} \veps(\alpha)
    \sum_{n \in \Z_{\ge 0}^{V_{\ge 3}}} P(n) \bm{e} \left( \frac{1}{k} {}^t\!(n + \alpha) \mu \right) \exp \left( -{}^t\!(n + \alpha) t \right) .$$
:::
