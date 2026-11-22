---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-014-62-a-proof-of-the-main-result
section_title: "A proof of the main result"
section_number: 6.2
pages: 16-17
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.959
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:Gauss_vanish_proof label="subsec:Gauss_vanish_proof"}

Finally, we prove [\[prop:Gauss_vanish\]](#prop:Gauss_vanish){reference-type="ref" reference="prop:Gauss_vanish"}. We need the following lemma.

::: lem
[]{#lem:Gauss_sum_indep label="lem:Gauss_sum_indep"} Let $k, M \in \Z \smallsetminus \{ 0 \}$ and $a, b \in \Z$ be integers such that $\gcd(a, M) = 1$. For $\alpha \in \frac{1}{2M}\Z$ such that $\gcd(2M \alpha, M) = 1$, the complex number $$\sum_{\mu \in \Z/k\Z + \alpha} \bm{e} \left( \frac{M}{k} \left( a \mu^2 + b \mu \right) \right)$$ depends only on $M\alpha^2, M\alpha \bmod \Z$.
:::

This lemma is a little generalisation of [@MM Lemma 4.7 and 4.8] which is based on the proof of [@BMM_high_depth Theorem 4.1]. In this lemma, we remove the assumption $\gcd(2M, 2M \alpha) = 1$ in [@MM Lemma 4.7 and 4.8]. Although our proof is essentially the same as in [@MM Lemma 4.7 and 4.8], we give a proof for the convenience of readers.

::: proof
*Proof.* **Case 1**: Suppose $\gcd(M, k) > 1$. We can write $$\sum_{\mu \in \Z/k\Z + \alpha} \bm{e} \left( \frac{M}{k} \left( a \mu^2 + b \mu \right) \right)
    =
    \bm{e} \left( \frac{M}{k} \left( a \alpha^2 + b \alpha \right) \right)
    \sum_{\mu \in \Z/k\Z} \bm{e} \left( \frac{1}{k} \left( Ma \mu^2 + (2M \alpha a + Mb) \mu \right) \right).$$ By the assumption, we have $\gcd(a, M) = 1, \, \gcd(2M \alpha, M) = 1$ and thus, $\gcd(2M \alpha a + Mb, M) = 1$ holds. By combining with $\gcd(M, k) \mid \gcd(Ma, k)$ and $1 < \gcd(M, k) \mid M$, we obtain $\gcd(Ma, k) \nmid 2M \alpha a + Mb$. Thus, it is $0$ by the well-known vanishing result of one-variable Gauss sums ([@MM Lemma 4.3]).

**Case 2**: Suppose $\gcd(M, k) = 1$. Let $M^* \in \Z$ be an integer such that $MM^* \equiv 1 \bmod k$. For any $\mu \in \Z$, we have $$\begin{aligned}
        &M \left( a (\mu + \alpha)^2 + b (\mu + \alpha) \right)
        - M \left( a (\mu + M M^* \alpha)^2 + b (\mu + M M^* \alpha) \right) & & \\
        = \,
        &M \left( (1 - (MM^*)^2) a \alpha^2 + (1 - M M^*) (b + 2a \mu) \alpha \right) & & \\
        \equiv \,
        &(1 - M M^*) \left( (1 + MM^*) a \alpha^2 + b \alpha \right) & &\bmod k\Z.
    
\end{aligned}$$ Thus, we obtain $$\begin{aligned}
        &\sum_{\mu \in \Z/k\Z + \alpha} \bm{e} \left( \frac{M}{k} \left( a \mu^2 + b \mu \right) \right)\\
        = \,
        &\bm{e} \left( \frac{1 - M M^*}{k}  M  \left( (1 + MM^*) a \alpha^2 + b \alpha \right) \right)
        \sum_{m \in \Z/k\Z + M M^* \alpha} \bm{e}\left( \frac{M}{k} \left( a \mu^2 + b \mu \right) \right).
    
\end{aligned}$$ Since this sum depends only on $M\alpha^2 \bmod \Z$ and $M\alpha \bmod \Z$, we obtain the claim. ◻
:::

::: proof
*Proof of $\cref{prop:Gauss_vanish}$.* For [\[item:prop:Gauss_vanish1\]](#item:prop:Gauss_vanish1){reference-type="ref" reference="item:prop:Gauss_vanish1"}, fix a vertex $v \in V_{\ge 3}$ and let $$\begin{aligned}
        F(t) 
        &\coloneqq
        \left( 2k \bm{e} \left( -1/8 \right) \right)^{\abs{V_{\ge 2}}} \sqrt{\det S} F(f_1; t)
        \\
        F_v(t)
        &\coloneqq 
        \sum_{ \mu \in \left. \left( \Z^{V_{\ge 2} \smallsetminus \{ v \} } \oplus k\Z \right) \middle/ 2kS \left(\Z^{V_{\ge 2}} \right) \right. } 
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) 
        \prod_{v' \in V_{\ge 2}} G_{v'} \left( \zeta_{2kM_{v'}}^{\mu_{v'}} e^{-t_{v'}/2M_{v'}} \right).
    
\end{aligned}$$ By [\[lem:F(f_1;t)\]](#lem:F(f_1;t)){reference-type="ref" reference="lem:F(f_1;t)"}, we can write $$\begin{aligned}
        &F(t) - F_v(t) \\
        = \,
        &\sum_{ \mu \in \left. \left( \Z^{V_{\ge 2} \smallsetminus \{ v \} } \oplus \left( \Z \smallsetminus k\Z \right) \right) \middle/ 2kS \left(\Z^{V_{\ge 2}} \right) \right. } 
        \bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) 
        \prod_{v' \in V_{\ge 2}} G_{v'} \left( \zeta_{2kM_{v'}}^{\mu_{v'}} e^{-t_{v'}/2M_{v'}} \right).
    
\end{aligned}$$ Since the rational function $$G_v (\zeta_{2k}^{\mu_v} e^{-t_v/2}) = 
    (\zeta_{2k}^{\mu_v} e^{-t_v/2} - \zeta_{2k}^{-\mu_v} e^{t_v/2})^{2 - \deg(v)} 
    \prod_{i \in \overline{v}} 
    \left(
    \left( \zeta_{2k}^{\mu_v} e^{-t_v/2} \right)^{M_{v} / w_{i}} - \left( \zeta_{2k}^{\mu_v} e^{-t_v/2} \right)^{-M_{v} / w_{i}} 
    \right)$$ is holomorphic at $t_v = 0$ for any $\mu_v \in \Z \smallsetminus k\Z$, the rational function $F(t) - F_v(t)$ is also holomorphic at $t_v = 0$. Thus, it suffices to show $\ord_{t_v = 0} F_v(t)
    \ge
    \abs{\overline{v}} + 2 - \deg(v)$. Let $$a_v \coloneqq M_v \left( -w_v + \sum_{i \in \overline{v}} \frac{1}{w_i} \right), \quad
    b_v \coloneqq \sum_{v' \in V_{\ge 3}, \, \{ v, v' \} \in E} \mu_{v'}$$ for each $\mu' \in \Z^{V_{\ge 2} \smallsetminus \{ v \} }$. Under this notations, we can write $$\label{eq:F_v_expression}
        \begin{aligned}
            F_v(t)
            \coloneqq \, 
            &\sum_{ \mu' \in \bigoplus_{v' \in V_{\ge 2} \smallsetminus \{ v \} } \Z / 2k M_{v'} \Z } 
            \bm{e} \left( -\frac{1}{4k} {}^t\!\mu' S^{-1} \mu' \right) 
            \left( 
            \prod_{ v \in V_{\ge 2} \smallsetminus \{ v \} } G_{v'} \left( \zeta_{2kM_{v'}}^{\mu_{v'}} e^{-t_{v'}/2M_{v'}} \right) 
            \right) \\
            &\sum_{ \mu_v \in \Z / 2 M_{v} \Z } 
            \bm{e} \left( -\frac{1}{4k} \left( \frac{k a'_v}{M_v} \mu_v^2 + 2b_v \mu_v \right) \right) 
            G_v \left( \zeta_{2M_v}^{\mu_v} e^{-t_v/2M_v} \right).
        \end{aligned}$$ Since we have $$G_{v} (q)
    =
    (q^{2M_{v}} - 1)^{2 - \deg(v)}
    \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) q^{2M_{v} \alpha_{v}}$$ by the definition of $G_v(q)$, the last line of [\[eq:F_v_expression\]](#eq:F_v_expression){reference-type="ref" reference="eq:F_v_expression"} is equal to $$\begin{aligned}
        &(e^{-t_v} - 1)^{2 - \deg(v)}
        \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) e^{-\alpha_{v} t_v}
        \sum_{ \mu_v \in \Z / 2 M_{v} \Z } 
        \bm{e} \left( -\frac{k a'_v}{4 M_v} \mu_v^2 + \left( \alpha_v - \frac{b_v}{2} \right) \mu_v \right).
    
\end{aligned}$$ By applying reciprocity of Gauss sums ([\[prop:reciprocity\]](#prop:reciprocity){reference-type="ref" reference="prop:reciprocity"}), this can be written as $$\begin{aligned}
 \label{eq:alpha_indep}
        &\frac{\bm{e} (1/8) \sqrt{k a_v}}{\sqrt{2 \abs{M_v}}}
        (e^{-t_v} - 1)^{2 - \deg(v)}
        \sum_{\alpha_{v} \in \calS_{v}} \veps_{v}(\alpha_{v}) e^{-\alpha_{v} t_v}
        \sum_{ \mu_v \in \Z / k a_v \Z } 
        \bm{e} \left( -\frac{M_v}{k a'_v} \left( \mu_v + \alpha_v - \frac{b_v}{2} \right)^2 \right).
    
\end{aligned}$$ Since the second summation is independent of $\alpha_v$ by [\[lem:epsilon\]](#lem:epsilon){reference-type="ref" reference="lem:epsilon"} [\[item:lem:epsilon3\]](#item:lem:epsilon3){reference-type="ref" reference="item:lem:epsilon3"}, [\[lem:bij_calS_v\]](#lem:bij_calS_v){reference-type="ref" reference="lem:bij_calS_v"} [\[item:lem:bij_calS_v3\]](#item:lem:bij_calS_v3){reference-type="ref" reference="item:lem:bij_calS_v3"}, and [\[lem:Gauss_sum_indep\]](#lem:Gauss_sum_indep){reference-type="ref" reference="lem:Gauss_sum_indep"}, [\[eq:alpha_indep\]](#eq:alpha_indep){reference-type="ref" reference="eq:alpha_indep"} is the multiplication of $G_v(e^{-t_v / 2M_v})$ by a constant independent of $\alpha_v$. Thus, we obtain $\ord_{t_v = 0} F_v(t) \ge \ord_{t_v = 0} G_v(e^{-t_v / 2M_v})$. Since $\ord_{t_v = 0} G_v(e^{-t_v / 2M_v}) = 2 - \deg(v) + \abs{\overline{v}}$ holds by [\[lem:G_v_at_1\]](#lem:G_v_at_1){reference-type="ref" reference="lem:G_v_at_1"}, the claim holds.

Finally we prove [\[item:prop:Gauss_vanish2\]](#item:prop:Gauss_vanish2){reference-type="ref" reference="item:prop:Gauss_vanish2"}. If $\abs{\overline{v}} + 2 - \deg(v) > 0$ for each vertex $v \in V_{\ge 3}$, then $G_v(e^{-t_v / 2M_v})$ has a zero at $t_v = 0$ by [\[lem:G_v_at_1\]](#lem:G_v_at_1){reference-type="ref" reference="lem:G_v_at_1"}, thus $F_v(t)$ also has a zero. Thus, we obtain $$\restrict{F(t)}{t_v = 0}
    =
    \restrict{F(t) - F_v(t)}{t_v = 0}.$$ Fix any vertex $v' \in V_{\ge 2} \smallsetminus \{ v \}$ and let $$\begin{aligned}
        F_{v, v'}(t)
        \coloneqq 
        F(t) - F_v(t) -
        \sum_{ \mu \in 
            \left. \left( \Z^{V_{\ge 2} \smallsetminus \{ v, v' \} } \oplus \left( \Z \smallsetminus k\Z \right)^{\{ v, v' \}} \right) 
            \middle/ 2kS \left(\Z^{V_{\ge 2}} \right) \right. } 
        &\bm{e} \left( -\frac{1}{4k} {}^t\!\mu S^{-1} \mu \right) 
        \\
        &\prod_{v' \in V_{\ge 2}} G_{v'} \left( \zeta_{2kM_{v'}}^{\mu_{v'}} e^{-t_{v'}/2M_{v'}} \right).
    
\end{aligned}$$ By the same argument in a proof of [\[item:prop:Gauss_vanish1\]](#item:prop:Gauss_vanish1){reference-type="ref" reference="item:prop:Gauss_vanish1"}, the rational function $F_{v, v'}(t)$ has a zero at $t_{v'} = 0$. By induction, we obtain the claim. ◻
:::
