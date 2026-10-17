---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-009-33-minimal-intervals
section_title: "Minimal intervals"
section_number: 3.3
pages: 10-12
source_pdf: 2406.05311v1.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 1.0
doc_brief: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small)"
---
[]{#sec:Qminim label="sec:Qminim"}

As far as we know, there is no analog of the Grassmannian--Bruhat order related to the quantum $k$-Bruhat order, and so rather than speak of minimal permutations (as we did in the classical case; see Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}), we work instead with certain intervals in the quantum $k$-Bruhat order. This lack of an analog of the Grassmannian--Bruhat order necessitates the significant work we do in Section [\[left-operators\]](#left-operators){reference-type="ref" reference="left-operators"}.

Let $u, w \in S_n$ and suppose that $u \leq_k^q q^{\alpha}w$ in the quantum $k$-Bruhat order on $S_n[q]$. We say that the interval $[u,q^\alpha w]_k^q$ is if its rank $\ell(q^{\alpha}w)-\ell(u)$ equals $\#\mathop{\mathrm{supp}}(wu^{-1}) - s(wu^{-1})$. When $q^\alpha=1$, the interval $[u, w]_k^q=[u,w]_k$ is minimal if and only if $wu^{-1}$ is a minimal permutation. In the proof of Theorem [\[thm:q_hook_product\]](#thm:q_hook_product){reference-type="ref" reference="thm:q_hook_product"} we will show that if $[u,q^\alpha w]_k^q$ is minimal, then $wu^{-1}$ is a minimal permutation in the sense of Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}.

The interval on the left in Figure [\[F:k-Bruhat\]](#F:k-Bruhat){reference-type="ref" reference="F:k-Bruhat"} is a minimal interval in the quantum $5$-Bruhat order in $S_8$. Figure [1](#F:more_minimal){reference-type="ref" reference="F:more_minimal"} displays two minimal intervals in quantum $k$-Bruhat order on $S_5[q]$ for $k=2,3$.

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
