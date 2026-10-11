---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-002-a-murnaghan-nakayama-rule-for-quantum-cohomology
section_title: "A Murnaghan\u2013Nakayama rule for quantum cohomology"
section_number: 3
pages: 8-12
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.949
---
[]{#S:qCoh label="S:qCoh"}

The (small) quantum cohomology ring $qH^*{\mathbb F}\ell_n$ of the flag manifold is a deformation of the ordinary cohomology ring $H^*{\mathbb F}\ell_n$ whose product encodes the three-point Gromov--Witten invariants of ${\mathbb F}\ell_n$. We describe this ring and extend the main objects from Section [\[sec:classic-mn-rule\]](#sec:classic-mn-rule){reference-type="ref" reference="sec:classic-mn-rule"} to the quantum setting.

## Quantum cohomology ring of the flag manifold

As a ${\mathbb Z}$-module, we have

$$qH^*{\mathbb F}\ell_n\ =\  {\mathbb Z}[q_1,\dotsc,q_{n-1}] \otimes_{\mathbb Z}H^*{\mathbb F}\ell_n\,,$$

where $q_1,\dotsc,q_{n-1}$ are indeterminates. To simplify notation, write ${\mathbb Z}[q]$ for ${\mathbb Z}[q_1,\dotsc,q_{n-1}]$, and use multiindex notation, for $\alpha\in{\mathbb N}^{n-1}$, we have ${\color{RoyalBlue}q^\alpha}\vcentcolon= q_1^{\alpha_1}\dotsb q_{n-1}^{\alpha_{n-1}}$. The Schubert classes $\{{\mathfrak S}_w\}_{w \in S_n}$ in $H^*{\mathbb F}\ell_n$ form a ${\mathbb Z}[q]$-basis of $qH^*{\mathbb F}\ell_n$. We write ${\color{RoyalBlue}{\mathfrak S}_u \ast {\mathfrak S}_v}$ for the product of Schubert classes ${\mathfrak S}_u$ and ${\mathfrak S}_v$ in $qH^*{\mathbb F}\ell_n$ to distinguish it from the product ${\color{RoyalBlue}{\mathfrak S}_u \cdot {\mathfrak S}_v}$ in $H^*{\mathbb F}\ell_n$.

The ring structure of $qH^*{\mathbb F}\ell_n$ is determined by the  [@FGP]. For every $u\in S_n$ and $1\leq k<n$ we have,

$$\label{quantum-Monk-formula}
    {\mathfrak S}_u * {\mathfrak S}_{(k,k+1)}
    \ =\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j))}} {\mathfrak S}_{u (i,j)}\ 
    \ +\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j)) + 2(j - i)}} q_{i,j} {\mathfrak S}_{u (i,j)}$$

where ${\color{RoyalBlue}q_{i,j}}\vcentcolon=q_iq_{i+1}\dotsb q_{j-1}$ for $i < j$. The summand on the left above comes from the classical Monk formula [\[classical-Monk-formula\]](#classical-Monk-formula){reference-type="eqref" reference="classical-Monk-formula"}. For example, in $qH^*{\mathbb F}\ell_4$ we have,

$$\label{Eq:q-Monk}
    {\mathfrak S}_{1432} * {\mathfrak S}_{(2,3)}
    \ =\  {\mathfrak S}_{3412} \ +\ {\mathfrak S}_{2431}
    \ +\ q_{2}{\mathfrak S}_{1342} \ +\  q_{2,3} {\mathfrak S}_{1234}\,.$$

Givental and Kim [@GiventalKim] proved that $qH^*{\mathbb F}\ell_n\simeq {\mathbb Z}[q][x] / I^q_n$ for a certain ideal $I^q_n$, establishing an analog to Borel's presentation [\[borel-presentation\]](#borel-presentation){reference-type="eqref" reference="borel-presentation"}. Fomin, Gelfand, and Postnikov [@FGP] defined ${\color{RoyalBlue}{\mathfrak S}^q_w(x)}$ in ${\mathbb Z}[q][x]$ so that the quantum product of Schubert classes satisfies ${\mathfrak S}_u \ast {\mathfrak S}_v \mapsto ({\mathfrak S}^q_u(x) + I^q_n) ({\mathfrak S}^q_v(x) + I^q_n)$, for $u,v\in S_n$, under this isomorphism. To simplify notation, for $f(x) \in {\mathbb Z}[q][x]$, we will write ${\mathfrak S}_u \ast f(x)$ for ${\mathfrak S}^q_u(x) f(x) + I^q_n$.

As explained in Section [\[cohomology-ring-of-the-flag-manifold\]](#cohomology-ring-of-the-flag-manifold){reference-type="ref" reference="cohomology-ring-of-the-flag-manifold"}, every Schur polynomial is a Schubert polynomial: more precisely, $s_\lambda(x_1, \ldots, x_k) = {\mathfrak S}_{v(\lambda, k)}(x)$, where $\lambda \subseteq R_{k, n-k}$. Analogously, we define the , for $\lambda \subseteq R_{k, n-k}$, to be ${s_\lambda^q(x_1,\dotsc,x_k)} \vcentcolon= {\mathfrak S}^q_{v(\lambda,k)}(x)$. Following Equation [\[Eq:PowerSumHook\]](#Eq:PowerSumHook){reference-type="eqref" reference="Eq:PowerSumHook"}, the is defined to be

$$\begin{gathered}
    \label{Eq:Q-powerSum}
    \qquad  {\color{RoyalBlue}p^q_r(x_1,\dotsc,x_k)}\ \vcentcolon= \\
        s^q_{(r)}(x_1,\dotsc,x_k) - s^q_{(r-1,1)}(x_1,\dotsc,x_k) +
                   \dotsb + (-1)^{r+1} s^q_{(1^r)}(x_1,\dotsc,x_k)\,.
    \qquad
\end{gathered}$$

## Quantum $k$-Bruhat order

The terms appearing in the quantum Monk formula [\[quantum-Monk-formula\]](#quantum-Monk-formula){reference-type="eqref" reference="quantum-Monk-formula"} define a ranked partial order on the (infinite) set

$${\color{RoyalBlue}S_n[q]}\  \vcentcolon=\  \big\{ q^\alpha u \mid u\in S_n \text{ and } \alpha\in{\mathbb N}^{n-1}\big\}\,.$$

The on $S_n[q]$ is defined by the following cover relations:

1.  ${\color{RoyalBlue}u\lessdot_k^q u (i,j)}$ if $i\leq k<j$ and $\ell(u)+1=\ell(u (i,j))$, so that $u\lessdot_k u (i,j)$;

2.  ${\color{RoyalBlue}u\lessdot_k^q q_{i,j} u (i,j)}$ if $i\leq k<j$ and

    $\ell(u)+1=\ell(u (i,j))+2(j{-}i)$ ; and

3.  extend $q$-multiplicatively: $u\leq_k^q q^\beta w$ if and only if $q^{\alpha} u\leq_k^q q^{\alpha+\beta} w$ for $u,w\in S_n[q]$ and any $\alpha,\beta\in {\mathbb N}^{n-1}$.

We will say that covers of type (1) and their extensions by (3) are , and covers of type (2) and their extensions by (3) are . The on $S_n[q]$ is given by ${\color{RoyalBlue}\ell(q^\alpha u)} \vcentcolon= 2 \deg q^\alpha + \ell(u)$, where $\deg q^\alpha$ is the usual degree of the monomial $q^\alpha$ in ${\mathbb Z}[q]$. Figure [1](#fig:quantum-2-Bruhat-poset){reference-type="ref" reference="fig:quantum-2-Bruhat-poset"} shows two levels of the quantum $2$-Bruhat order on $S_4[q]$ starting at the permutation $14\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}32$. We draw the classical covers in green and the quantum covers in red. Compare the first level to the example in [\[Eq:q-Monk\]](#Eq:q-Monk){reference-type="eqref" reference="Eq:q-Monk"}.

<figure id="fig:quantum-2-Bruhat-poset">
<div class="picture">
<p>(330,80)(10,0) ( 10, 70)<span><span class="math inline">$34\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}21$</span></span> ( 52, 70)<span><span class="math inline">$q_{2,3} 21\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}34$</span></span> (110, 70)<span><span class="math inline">$q_{2} 23\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}41$</span></span> (160, 70)<span><span class="math inline">$q_{2} 14\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32$</span></span> (230, 70)<span><span class="math inline">$q_{2} 31\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}42$</span></span> (290, 70)<span><span class="math inline">$q_{2,3} 13\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}24$</span></span></p>
<p>( 65,46)<span>(-2,1)<span>40</span></span> ( 72,46)<span>(0,1)<span>20</span></span> ( 80,46)<span>(2,1)<span>40</span></span></p>
<p>(150,46)<span>(-1,1)<span>20</span></span> (165,46)<span>( 1,2)<span>10</span></span></p>
<p>(240,46)<span>( 1,2)<span>10</span></span></p>
<p>(300,46)<span>( 1,2)<span>10</span></span></p>
<p>(59.4, 35)<span><span class="math inline">$24\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}31$</span></span> (140, 35)<span><span class="math inline">$q_{2} 13\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}42$</span></span> (220, 35)<span><span class="math inline">$34\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}12$</span></span> (275, 35)<span><span class="math inline">$q_{2,3} 12\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}34$</span></span></p>
<p>(150,10)<span>(-3,1)<span>60</span></span> (158,10)<span>( 0,1)<span>20</span></span> (166,10)<span>(3,1)<span>60</span></span> (174,10)<span>(5,1)<span>100</span></span> (150,0)<span><span class="math inline">$14\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32$</span></span></p>
</div>
<figcaption>Two levels of the quantum <span class="math inline">2</span>-Bruhat order on <span class="math inline"><em>S</em><sub>4</sub>[<em>q</em>]</span> above <span class="math inline">$14\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32$</span>.</figcaption>
</figure>

As with the $k$-Bruhat order (see Proposition [\[nothing-in-between-is-in-between\]](#nothing-in-between-is-in-between){reference-type="ref" reference="nothing-in-between-is-in-between"}), there is an intrinsic formulation of the cover relations for the quantum $k$-Bruhat order.

::: proposition
[]{#prop:quantum-k-bruhat-covers label="prop:quantum-k-bruhat-covers"} Let $u \in S_n$ and $q^\alpha w \in S_n[q]$. Then $u \lessdot_k^q q^\alpha w$ if and only if

1.  []{#prop:quantum-k-bruhat-classic-covers label="prop:quantum-k-bruhat-classic-covers"} $\alpha=0$ and $q^\alpha w =w= u(i, j)$ for some $i \leq k < j$ such that $u(i) < u(j)$, and\
    there does not exist $l$ such that $i < l < j$ and $u(i) < u(l) < u(j)$; or

2.  []{#prop:quantum-k-bruhat-quantum-covers label="prop:quantum-k-bruhat-quantum-covers"} $q^\alpha w = q_{i,j} u(i, j)$ for some $i \leq k < j$ such that $u(i) > u(j)$, and\
    for every $l$ such that $i < l < j$, we have $u(j) < u(l) < u(i)$.
:::

## Minimal intervals {#sec:Qminim}

As far as we know, there is no analog of the Grassmannian--Bruhat order related to the quantum $k$-Bruhat order, and so rather than speak of minimal permutations (as we did in the classical case; see Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}), we work instead with certain intervals in the quantum $k$-Bruhat order. This lack of an analog of the Grassmannian--Bruhat order necessitates the significant work we do in Section [\[left-operators\]](#left-operators){reference-type="ref" reference="left-operators"}.

Let $u, w \in S_n$ and suppose that $u \leq_k^q q^{\alpha}w$ in the quantum $k$-Bruhat order on $S_n[q]$. We say that the interval $[u,q^\alpha w]_k^q$ is if its rank $\ell(q^{\alpha}w)-\ell(u)$ equals $\#\mathop{\mathrm{supp}}(wu^{-1}) - s(wu^{-1})$. When $q^\alpha=1$, the interval $[u, w]_k^q=[u,w]_k$ is minimal if and only if $wu^{-1}$ is a minimal permutation. In the proof of Theorem [\[thm:q_hook_product\]](#thm:q_hook_product){reference-type="ref" reference="thm:q_hook_product"} we will show that if $[u,q^\alpha w]_k^q$ is minimal, then $wu^{-1}$ is a minimal permutation in the sense of Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}.

The interval on the left in Figure [\[F:k-Bruhat\]](#F:k-Bruhat){reference-type="ref" reference="F:k-Bruhat"} is a minimal interval in the quantum $5$-Bruhat order in $S_8$. Figure [2](#F:more_minimal){reference-type="ref" reference="F:more_minimal"} displays two minimal intervals in quantum $k$-Bruhat order on $S_5[q]$ for $k=2,3$.

<figure id="F:more_minimal">
<div class="picture">
<p>(100,110)(-15,0) (13,0)<span><embed src="q-int1.eps" /></span> (25,100)<span><span class="math inline">$q_{1,5}q_{2,4}12\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}354$</span></span> (-15, 75)<span><span class="math inline">$q_{2,5}52\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}314$</span></span> (38, 75)<span><span class="math inline">$q_{1,5}15\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}324$</span></span> (-15, 50)<span><span class="math inline">$q_{2,5}51\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}324$</span></span> (38, 50)<span><span class="math inline">$q_{1,5}14\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}325$</span></span> ( 0, 25)<span><span class="math inline">$54\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}321$</span></span> (38, 25)<span><span class="math inline">$q_{1,5}13\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}425$</span></span> ( 0, 0)<span><span class="math inline">$53\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}421$</span></span></p>
</div>
<div class="picture">
<p>(120,110)(-35,0) (-25,0)<span><embed src="q-int2.eps" /></span> (-10,100)<span><span class="math inline">$q_{3,5}521\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}34$</span></span> (0, 75)<span><span class="math inline">$524\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}31$</span></span> (35,75)<span><span class="math inline">$q_{3,5}421\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}35$</span></span> (-35,50)<span><span class="math inline">$514\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}32$</span></span> (0, 50)<span><span class="math inline">$523\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}41$</span></span> (45,50)<span><span class="math inline">$425\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}31$</span></span> (-35,25)<span><span class="math inline">$513\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}42$</span></span> (0, 25)<span><span class="math inline">$423\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}51$</span></span> (45,25)<span><span class="math inline">$415\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}32$</span></span> (0, 0)<span><span class="math inline">$413\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}52$</span></span></p>
</div>
<figcaption>Two minimal quantum intervals. Note that <span class="math inline"><em>q</em><sub>1, 5</sub><em>q</em><sub>2, 4</sub> = <em>q</em><sub>1, 4</sub><em>q</em><sub>2, 5</sub> = <em>q</em><sub>1</sub><em>q</em><sub>2</sub><sup>2</sup><em>q</em><sub>3</sub><sup>2</sup><em>q</em><sub>4</sub></span>.</figcaption>
</figure>

## The Murnaghan--Nakayama rule for $qH^*{\mathbb F}\ell_n$

As for Corollary [\[C:classical-schubert-times-powersum\]](#C:classical-schubert-times-powersum){reference-type="ref" reference="C:classical-schubert-times-powersum"}, we derive the quantum Murnaghan--Nakayama formula from an intermediate result describing the quantum product of a Schubert class ${\mathfrak S}_u$ by a quantum hook Schur polynomial $s_{(b, 1^{a-1})}^q(x_1,\dotsc,x_k)$.

::: theorem
[]{#thm:q_hook_product label="thm:q_hook_product"} Let $u \in S_n$ , $a \leq k$ and $b \leq n-k$. Then $${\mathfrak S}_u
        \ast
        s^q_{(b,1^{a-1})} (x_1, \dots, x_k)
        = \sum
        \left(\begin{smallmatrix} s(wu^{-1})-1 \\ \mathop{\mathrm{ht}}(wu^{-1})-a \end{smallmatrix}\right)
        q^\alpha
        {\mathfrak S}_{w}\,,$$ the sum over all minimal intervals $[u,  q^{\alpha}w]_k^q$ such that $\ell(q^\alpha w) - \ell(u)= a{+}b{-}1$.
:::

The proof depends on Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"} and Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}, which will be proved in subsequent sections.

::: proof
*Proof.* For $u,w \in S_n$, a partition $\lambda$, $k \in {\mathbb N}$ with $1\leq k$ and $\alpha\in {\mathbb N}^{n-1}$, define quantum Littlewood--Richardson coefficients $C^{q^\alpha w}_{u,v(\lambda,k)}\in q^\alpha {\mathbb N}$ by $$\label{eq-definition-Cq}
        {\mathfrak S}_u \ast s^q_\lambda(x_1, \ldots, x_k)
        \ =\ \sum_{q^\alpha w \in S_n[q]} C^{q^\alpha w}_{u,v(\lambda,k)} {\mathfrak S}_w\,.$$ We must prove that

$$C^{q^\alpha w}_{u,v((b, 1^{a-1}),k)}\ =\ 
        \begin{cases}
            q^\alpha \left(\begin{smallmatrix} s(wu^{-1})-1 \\ \mathop{\mathrm{ht}}(wu^{-1})-a \end{smallmatrix}\right),
            &
            \begin{array}[t]{lr}
                \text{if $[u, q^{\alpha}w]_k^q$ is minimal and} \\[-0.5ex]
                \qquad\qquad\qquad \text{$\ell(q^\alpha w) - \ell(u) = a{+}b{-}1$,}
            \end{array}
            
            \\
            0, &
            \begin{array}[t]{lr}
                \text{otherwise.}
            \end{array}
        \end{cases}$$

Suppose that $[u, q^{\alpha}w]_k^q$ is a minimal interval with $\ell(q^\alpha w) - \ell(u) = a{+}b{-}1$. By Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"}, there exists a hook partition $\gamma$ with $|\gamma| = \ell(q^\alpha w) - \ell(u)$ and $C^{q^\alpha w}_{u,v(\gamma,k)} \neq 0$. By Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}, there exist permutations $y, z \in S_n$ satisfying $$\label{properties-of-y-and-z}
        y\ \leq_k\ z,
        \quad
        \ell(z) - \ell(y)\ =\ \ell(q^\alpha w) - \ell(u) = a{+}b{-}1,
        \quad
        zy^{-1}\ =\ wu^{-1},$$ and such that $$\label{eq-leung-li-reduction}
        C^{q^\alpha w}_{u,v(\mu,k)}\ =\  q^\alpha c^z_{y,v(\mu,k)}
        \quad \text{for all partitions $\mu$ with $|\mu| = a{+}b{-}1$\,.}$$ This implies that $z y^{-1}$ is a minimal permutation, since $$\begin{aligned}
        \ell(z) - \ell(y)
        = \ell(q^\alpha w) - \ell(u)
        = \#\mathop{\mathrm{supp}}(w u^{-1}) - s(w u^{-1})
        = \#\mathop{\mathrm{supp}}(z y^{-1}) - s(z y^{-1}),
    
\end{aligned}$$ where the middle equality follows from the assumption that $[u, q^{\alpha}w]_k^q$ is minimal. Then $$C^{q^\alpha w}_{u,v((b, 1^{a-1}),k)}
        \ =\ q^\alpha c^z_{y,v((b, 1^{a-1}),k)}
        \ =\ q^\alpha \left(\begin{smallmatrix} s(zy^{-1})-1 \\ \mathop{\mathrm{ht}}(zy^{-1})-a \end{smallmatrix}\right)
        \ =\ q^\alpha \left(\begin{smallmatrix} s(wu^{-1})-1 \\ \mathop{\mathrm{ht}}(wu^{-1})-a \end{smallmatrix}\right),$$ where the first equality follows from [\[eq-leung-li-reduction\]](#eq-leung-li-reduction){reference-type="eqref" reference="eq-leung-li-reduction"} and the second equality follows from Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"} and that $z y^{-1}$ is a minimal permutation.

Conversely, suppose $C^{q^\alpha w}_{u,v((b, 1^{a-1}), k)} \neq 0$. By Lemma [\[L:Quantum_is_Classical\]](#L:Quantum_is_Classical){reference-type="ref" reference="L:Quantum_is_Classical"}, there exist $y, z \in S_n$ satisfying [\[properties-of-y-and-z\]](#properties-of-y-and-z){reference-type="eqref" reference="properties-of-y-and-z"} and [\[eq-leung-li-reduction\]](#eq-leung-li-reduction){reference-type="eqref" reference="eq-leung-li-reduction"}. Setting $\mu = (b, 1^{a-1})$ in [\[eq-leung-li-reduction\]](#eq-leung-li-reduction){reference-type="eqref" reference="eq-leung-li-reduction"} gives

$$C^{q^\alpha w}_{u,v((b, 1^{a-1}),k)}
        \ =\ q^\alpha c^z_{y,v((b, 1^{a-1}),k)}.$$ Since the left hand side is assumed to be nonzero, we have that $c^z_{y,v((b, 1^{a-1}),k)}$ is nonzero. It now follows from Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"} that $z y^{-1}$ is a minimal permutation so that $$\ell(q^\alpha w) - \ell(u)
        = \ell(z) - \ell(y)
        = \#\mathop{\mathrm{supp}}(z y^{-1}) - s(z y^{-1})
        = \#\mathop{\mathrm{supp}}(w u^{-1}) - s(w u^{-1}),$$ where the first and last equalities follow from [\[properties-of-y-and-z\]](#properties-of-y-and-z){reference-type="eqref" reference="properties-of-y-and-z"}. Thus, $[u, q^\alpha w]_k^q$ is a minimal interval such that $\ell(q^\alpha w) - \ell(u) = a{+}b{-}1$. ◻
:::

The following was conjectured in [@Morrison]. It follows from Theorem [\[thm:q_hook_product\]](#thm:q_hook_product){reference-type="ref" reference="thm:q_hook_product"} in the same way that Corollary [\[C:classical-schubert-times-powersum\]](#C:classical-schubert-times-powersum){reference-type="ref" reference="C:classical-schubert-times-powersum"} follows from Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"}, and is the signature result in this paper.

::: corollary
[]{#C:quantumMN label="C:quantumMN"} Let $u \in S_n$. Then $${\mathfrak S}_u \ast p_r^q(x_1,\dotsc,x_k) = \sum (-1)^{\mathop{\mathrm{ht}}(wu^{-1})+1} q^\alpha {\mathfrak S}_{w}$$ the sum over all minimal intervals $[u, q^{\alpha}w]_k^q$ of rank $r$ such that $wu^{-1}$ is a single cycle.
:::

::: example
[]{#Ex:MN_example label="Ex:MN_example"} In $qH^*{\mathbb F}\ell_8$, if $u=68235741$, then the product ${\mathfrak S}_{u}\ast p^q_4(x_1,\dotsc,x_5)$ is $$\begin{gathered}
      {\mathfrak S}_{(2,3,5,7,4)u}
    + {\mathfrak S}_{(2,4,3,5,7)u}
    + {\mathfrak S}_{(3,5,6,7,4)u}
    - {\mathfrak S}_{(2,3,5,6,7)u}
    \\
    + q_{5,7}{\mathfrak S}_{(2,3,4,7,5)u}
    + q_{5,7}{\mathfrak S}_{(3,4,6,7,5)u}
    + {\color{RoyalBlue}q_{5,8}{\mathfrak S}_{(1,6,7,3,5)u}}
    + q_{5,8}{\mathfrak S}_{(1,7,2,3,5)u}
    \\
    - q_{5,8}{\mathfrak S}_{(1,6,7,5,4)u}
    - q_{5,8}{\mathfrak S}_{(1,7,5,3,4)u}
    - q_{5,8}{\mathfrak S}_{(1,7,4,3,5)u}

    - q_{2,6}{\mathfrak S}_{(2,3,5,7,8)u}
    \\

    + q_{2,8}{\mathfrak S}_{(1,7,3,5,8)u}
    + q_{2,8}{\mathfrak S}_{(1,8,2,3,4)u}
    + q_{2,8}{\mathfrak S}_{(1,6,7,5,8)u}
    + q_{2,8}{\mathfrak S}_{(1,7,5,6,8)u}
 
    -q_{2,8}q_{5,7}{\mathfrak S}_{(1,7,5,4,8)u} \,.
\end{gathered}$$

Note that unlike in ordinary cohomology, this is not an identity among quantum Schubert polynomials ${\mathfrak S}^q_w(x)$, but rather among their images in the quotient ring ${\mathbb Z}[q][x]/I^q_n$.
:::

## Remarks regarding [@MPP Thm. 15] {#SS:R_MPP}

Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"} may be deduced from a stronger result of Mészáros, Panova, and Postnikov [@MPP Thm. 8]. There, they establish a formula for a 'lift' of the Schur polynomial $s_{(b,1^{a-1})}(x_1,\dotsc,x_k)$ to the Fomin--Kirillov [@FominKirillov] algebra ${\mathcal E}_n$, which is a subalgebra (generated by certain Dunkl elements $\theta_i$) of the quotient of a free associative algebra with generators $x_{i,j}$ for $1\leq i<j\leq n$ by certain relations, which include $x_{i,j}^2=0$. Their paper contains another result [@MPP Thm. 15] which is a quantum analog of [@MPP Thm. 8], giving a formula for a 'quantum lift' of $s^q_{(b,1^{a-1})}(x_1,\dotsc,x_k)$ to the quantum Fomin--Kirillov algebra $\mathcal{E}^q_n$ [@Postnikov]. This formula would imply Theorem [\[thm:q_hook_product\]](#thm:q_hook_product){reference-type="ref" reference="thm:q_hook_product"}. Unfortunately, as we now sketch, there is a gap in the proof of [@MPP Thm. 15] (we have communicated this to the authors).

The result [@MPP Thm. 15] is deduced from the proof of [@MPP Thm. 8] using a technical result [@MPP Lem. 13] which roughly asserts the following: If an identity involving positive terms holds in ${\mathcal E}_n$, and if no relations $x_{i,j}^2=0$ were used to deduce the identity, then the same identity holds in ${\mathcal E}^q_n$. We are convinced this lemma is correct, but it unfortunately does not apply in the case invoked to prove [@MPP Thm. 15]. The proof of [@MPP Thm. 8] uses in a fundamental way [@MPP Cor. 10], that $e_a(\theta_1,\dotsc,\theta_a)h_b(\theta_1,\dotsc,\theta_a)=0$ in $\mathcal{E}_{a+b}$ (in their notation). However, this identity can only be proven directly in $\mathcal{E}_{a+b}$ using the relations $x_{i,j}^2=0$. For example, when $a=b=1$, as $\theta_1=x_{1,2}$, it becomes $0=e_1(x_{1,2})h_1(x_{1,2})=x_{1,2}^2$.
