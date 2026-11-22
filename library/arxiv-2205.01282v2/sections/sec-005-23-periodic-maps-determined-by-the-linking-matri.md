---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-005-23-periodic-maps-determined-by-the-linking-matri
section_title: "Periodic maps determined by the linking matrix"
section_number: 2.3
pages: 5-6
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.881
latex_coverage_ratio: 0.973
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:char label="subsec:char"}

In this subsection, we introduce periodic maps determined by the linking matrix and prove its basic properties.

For each vertex $v \in V_{\ge 2}$, let $$\calS_v
\coloneqq
\left\{ \frac{1}{2}\deg(v) - 1 + \sum_{i \in \overline{v}} \frac{l_i}{2w_i} \relmiddle{|} (l_i)_{i \in \overline{v}} \in \{ \pm 1 \}^{\overline{v}} \right\}$$ Here we set $\calS_v \coloneqq \left\{ \deg(v)/2 - 1 \right\}$ if $\overline{v} = \emptyset$. We also define the periodic map $\veps_v \colon \frac{1}{2M_v}\Z/\Z \to \{ 0, \pm 1 \}$ by $$\veps_v(\alpha_v) \coloneqq 
\begin{dcases}
    \prod_{i \in \overline{v}} l_i 
    & \text{ if } \alpha_v \equiv \frac{1}{2}\deg(v) - 1 + \sum_{i \in \overline{v}} \frac{l_i}{2w_i}  \bmod \Z 
    \text{ for some } (l_i)_{i \in \overline{v}} \in \{ \pm 1 \}^{\overline{v}}, \\
    0 & \alpha_{v} \notin (\calS_v + \Z)/\Z.
\end{dcases}$$ This map is well-defined by the following lemma.

::: lem
[]{#lem:bij_calS_v label="lem:bij_calS_v"} For a vertex $v \in V_{\ge 2}$ such that $\overline{v} \neq \emptyset$, the followings hold.

1.  []{#item:lem:bij_calS_v1 label="item:lem:bij_calS_v1"} The map $$\begin{array}{ccc}
                \{ \pm 1 \}^{\overline{v}} & \longrightarrow & \calS_v \\
                (l_i)_{i \in \overline{v}} & \longmapsto & \displaystyle \frac{1}{2}\deg(v) - 1 + \sum_{i \in \overline{v}} \frac{l_i}{2w_i}
            \end{array}$$ is bijective.

2.  []{#item:lem:bij_calS_v2 label="item:lem:bij_calS_v2"} The natural projection $\calS_v \to \frac{1}{2M_{v}} \Z/\Z$ is injective. Thus, the map $\veps_v$ is well-defined.

3.  []{#item:lem:bij_calS_v3 label="item:lem:bij_calS_v3"}

    For any $\alpha_v \in \calS_v$, it holds that $\gcd(2M_v \alpha_v, M_v) = 1$.
:::

::: proof
*Proof.* By [\[lem:coprime\]](#lem:coprime){reference-type="ref" reference="lem:coprime"}, there exists $i_0 \in \overline{v}$ such that $w_i$ is odd for any $i \in \overline{v} \smallsetminus \{ i_0 \}$. Then, we have $$\Z/2M_v \Z 
        \cong 
        \Z/ 2w_{i_0} \Z \oplus \bigoplus_{i \in \overline{v} \smallsetminus \{ i_0 \}} \Z/w_i \Z$$ by the Chinese remainder theorem. For each $$\alpha_v =
    \frac{1}{2}\deg(v) - 1 + \sum_{i \in \overline{v}} \frac{l_i}{2w_i}
    \in \calS_v, \quad
    (l_i)_{i \in \overline{v}} \in \{ \pm 1 \}^{\overline{v}},$$ it holds that $$2 M_v \alpha_v
    \equiv
    \left\{
    \begin{alignedat}{3}
        &\frac{M_v}{w_i} l_i &
        &\bmod w_i &
        &\quad
        \text{ if }
        i \in \overline{v} \smallsetminus \{ i_0 \}, \\
        &M_v \deg(v) + \frac{M_v}{w_{i_0}} l_{i_0} 
        + \sum_{i \in \overline{v} \smallsetminus \{ i_0 \} } \frac{M_v}{w_i} &
        &\bmod 2w_{i_0} &
        &\quad
        \text{ if }
        i = i_0.
    \end{alignedat}
    \right.$$ Here $M_v / w_i \not\equiv - M_v / w_i \bmod w_i$ for any vertex $i \in \overline{v} \smallsetminus \{ i_0 \}$ since $w_i$ is odd. We also have $M_v / w_{i_0} \not\equiv - M_v / w_{i_0} \bmod w_{i_0}$ since we assume $w_{i_0} \le -2$ in [\[subsec:graph\]](#subsec:graph){reference-type="ref" reference="subsec:graph"}. Thus, we obtain [\[item:lem:bij_calS_v2\]](#item:lem:bij_calS_v2){reference-type="ref" reference="item:lem:bij_calS_v2"}. By this argument, we can prove injectivity of the composition of the map $\{ \pm 1 \}^{\overline{v}} \to \calS_v$ in [\[item:lem:bij_calS_v1\]](#item:lem:bij_calS_v1){reference-type="ref" reference="item:lem:bij_calS_v1"} and the map $\calS_v \to \Z/2M_{v}\Z, \, \alpha_v \mapsto 2M_v \alpha_v$ which is injective by [\[item:lem:bij_calS_v2\]](#item:lem:bij_calS_v2){reference-type="ref" reference="item:lem:bij_calS_v2"}. Hence, we obtain [\[item:lem:bij_calS_v1\]](#item:lem:bij_calS_v1){reference-type="ref" reference="item:lem:bij_calS_v1"}.

Moreover, we have [\[item:lem:bij_calS_v3\]](#item:lem:bij_calS_v3){reference-type="ref" reference="item:lem:bij_calS_v3"} since $\gcd(M_v / w_i, w_i) = 1$ for each $i \in \overline{v}$. ◻
:::

In the above lemma, [\[item:lem:bij_calS_v1\]](#item:lem:bij_calS_v1){reference-type="ref" reference="item:lem:bij_calS_v1"} was first proved by Akihito Mori. The proof presented here is due to the author.

The following lemma follows from the definition immediately.

::: lem
[]{#lem:epsilon label="lem:epsilon"} For any vertex $v \in V_{\ge 2}$, the followings hold.

1.  []{#item:lem:epsilon2 label="item:lem:epsilon2"} $$\sum_{\alpha_v \in \frac{1}{2 M_v} \Z / \Z} \veps_v (\alpha_v) = 0.$$

2.  []{#item:lem:epsilon3 label="item:lem:epsilon3"} For each $\alpha_v \in \frac{1}{2 M_v} \Z / \Z$ such that $\veps_v (\alpha_v) \neq 0$, $M_v \alpha_v, M_v \alpha_v^2 \bmod \Z$ are independent of $\alpha_v$ respectively.

3.  []{#item:lem:epsilon4 label="item:lem:epsilon4"} $$\sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) q^{\alpha_{v}}
            =
            q^{\deg(v)/2 - 1} \prod_{i \in \overline{v}} \left( q^{1 / 2w_{i}} - q^{-1 / 2w_{i}} \right).$$
:::

The following lemma is very important for our proof of our main theorem. We use it in a proof of [\[prop:Gauss_vanish\]](#prop:Gauss_vanish){reference-type="ref" reference="prop:Gauss_vanish"} later.

::: lem
[]{#lem:FIMT label="lem:FIMT"} For $0 \le n \le \abs{\overline{v}} - 1$, it holds that $$\sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) \alpha_v^n
    = 0.$$
:::

In the next subsection, we give a proof of this lemma by a different method from [@FIMT].

At the end of this section, we consider products for vertices. Let $\calS \coloneqq \prod_{v \in V_{\ge 2}} \calS_v$ and the map $\veps \colon (2S)^{-1}(\Z^{V_{\ge 2}}) / \Z^{V_{\ge 2}} \to \{ 0, \pm 1 \}$ be $$\veps \left((\alpha_v)_{v \in V_{\ge 2}} \right) \coloneqq \prod_{v \in V_{\ge 2}} \veps_v( \alpha_v).$$ This is well-defined since $\calS \subset (2S)^{-1}(\Z^{V_{\ge 2}})$ by [\[prop:S\]](#prop:S){reference-type="ref" reference="prop:S"} [\[item:prop:S5\]](#item:prop:S5){reference-type="ref" reference="item:prop:S5"}.

The following lemma follows from [\[lem:bij_calS_v\]](#lem:bij_calS_v){reference-type="ref" reference="lem:bij_calS_v"}.

::: lem
[]{#lem:bij_calS label="lem:bij_calS"}

1.  []{#item:lem:bij_calS1 label="item:lem:bij_calS1"} The map $$\begin{array}{ccc}
                \{ \pm 1 \}^{V_1} & \longrightarrow & \calS \\
                (l_i)_{i \in V_1} & \longmapsto & \displaystyle \left( \frac{1}{2}\deg(v) - 1 + \sum_{i \in \overline{v}} \frac{l_i}{2w_i} \right)_{v \in V_{\ge 2}}
            \end{array}$$ is bijective.

2.  []{#item:lem:bij_calS1 label="item:lem:bij_calS1"} The natural projection $\calS \to (2S)^{-1}(\Z^{V_{\ge 2}}) / \Z^{V_{\ge 2}}$ is injective.
:::
