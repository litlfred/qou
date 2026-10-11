---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-001-a-murnaghan-nakayama-rule-for-classic-cohomology
section_title: "A Murnaghan\u2013Nakayama rule for (classic) cohomology"
section_number: 2
pages: 2-8
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.956
---
[]{#sec:classic-mn-rule label="sec:classic-mn-rule"}

We review combinatorial models for the cohomology ring of the flag manifold. We omit the precise definitions of the flag manifold and its cohomology as the combinatorial models will suffice for our purposes; the interested reader can consult [@Fu97].

Then we deduce a formula for the product of a Schubert polynomial and a hook Schur function from which we deduce the Murnaghan--Nakayama rule in the cohomology of the flag manifold, resulting in a different proof than that given by Morrison and Sottile [@MorrisonSottile]. Our proof of the Murnaghan--Nakayama rule in quantum cohomology is analogous.

## Cohomology of the flag manifold {#cohomology-ring-of-the-flag-manifold}

Let $n\in{\mathbb N}$ be a positive integer and write ${\mathbb F}\ell_n$ for the manifold of complete flags in ${\mathbb C}^n$. We let $H^*{\mathbb F}\ell_n$ denote its cohomology ring with coefficients in ${\mathbb Z}$. This is a free ${\mathbb Z}$-module with a distinguished basis $\{{\mathfrak S}_w\}_{w \in S_n}$ of which are indexed by elements of the symmetric group $S_n$. Borel [@Borel] described the ring structure of $H^*{\mathbb F}\ell_n$ as a quotient of a polynomial ring,

$$\label{borel-presentation}
    H^* {\mathbb F}\ell_n\ \simeq\ {\mathbb Z}[x_1,\dotsc,x_n] / I_n\,,
    \qquad I_n\ =\ \big\langle e_a(x_1,\dotsc,x_n)\mid a \in [n] \big\rangle\,,$$

where $e_a$ is the $a$th elementary symmetric polynomial and ${\color{RoyalBlue}[n]}\vcentcolon=\{1,\dots,n\}$. Lascoux and Schützenberger [@LaSch82] defined a set of polynomials in ${\mathbb Z}[x_1, \ldots, x_n]$ called that correspond to the Schubert classes ${\mathfrak S}_w$ under Borel's isomorphism. We write ${\mathfrak S}_w(x)$ for the Schubert polynomial corresponding to ${\mathfrak S}_w$ on the set of variables $x: = \{x_1, \ldots, x_n\}$.

Every Schur polynomial $s_\lambda(x_1, \ldots, x_k)$ is a Schubert polynomial. Let $w\in S_n$ be a permutation with a unique descent at position $k$. Then the sequence $(w(k){-}k,\dotsc, w(2){-}2,w(1){-}1)$ is a partition contained in the of $k(n{-}k)$ into $k$ parts with each part of size $n{-}k$. This is a bijection and for $\lambda \subseteq R_{k, n-k}$ we write ${\color{RoyalBlue}v(\lambda,k)}\in S_n$ for the corresponding permutation. Then ${\mathfrak S}_{v(\lambda, k)}(x) = s_\lambda(x_1, \ldots, x_k)$. For example, when $n=7$,

$$v((3,1,0),3)\ =\ 136\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}2457
  \qquad\mbox{and}\qquad
  v((1,0,0,0),4)\ =\ 1235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}467\ =\ (4,5)\,.$$

Observe that we may write permutations using both one-line and cycle notation. The " $\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}$ " is written after the $k$-th position in a permutation in one-line notation.

It remains an important open problem in Schubert calculus to find a combinatorial rule expressing ${\mathfrak S}_u \cdot {\mathfrak S}_v$ in terms of the basis $\{ {\mathfrak S}_w \}_{w \in S_n}$ of $H^*{\mathbb F}\ell_n$. That is, one seeks a combinatorial rule for the coefficients ${\color{RoyalBlue}c_{u,v}^{w}}\in{\mathbb Z}$ in the product

$$\label{eq:classical-coeffs}
    {\mathfrak S}_u \cdot {\mathfrak S}_v\ =\ \sum_{w} c_{u, v}^{w} {\mathfrak S}_w\,.$$

A remarkable property of Schubert polynomials is that this computation can be performed directly in the polynomial ring as the resulting coefficients $c_{u, v}^w$ are the same.

Although this problem remains open in general, several special cases are known.  [@Monk] treats the case where $v$ is the simple transposition $(k, k{+}1)$. For any $u \in S_n$,

$$\label{classical-Monk-formula}
    {\mathfrak S}_u(x) \cdot {\mathfrak S}_{(k,k+1)}(x)
       \ =\ 
    \sum_{\substack{1 \leq i \leq k < j \leq n \\ \ell(u) + 1 = \ell(u(i,j))}} {\mathfrak S}_{u (i,j)}(x)\,,$$

where ${\color{RoyalBlue}\ell(u)}\vcentcolon=\#\{i<j\mid u(i)>u(j)\}$ denotes the length of the permutation $u$. In this case, ${\mathfrak S}_{(k, k+1)}(x) = s_{(1)}(x_1, \ldots, x_k)$. Proposition [\[pieri-formulas-version-2\]](#pieri-formulas-version-2){reference-type="ref" reference="pieri-formulas-version-2"} below describes the special case of multiplying by $s_{(b, 1^{a-1})}(x_1, \ldots, x_k)$ in terms of the *$k$-Bruhat order*, which we define next. Here, $(b,1^{a-1})$ is the of $a{+}b{-}1$ into $a$ parts, the first of size $b$, and the remaining all of size $1$.

## $k$-Bruhat order

The terms appearing in Monk's Formula [\[classical-Monk-formula\]](#classical-Monk-formula){reference-type="eqref" reference="classical-Monk-formula"} define a partial order on $S_n$ graded by $\ell(u)$. Define the by the covering relation $${{\color{RoyalBlue}u\lessdot_k u (i,j)}}
    \qquad\text{if}\quad
    1 \leq i\leq k<j \leq n
    \quad\text{and}\quad
    \ell(u)+1=\ell(u(i,j))\,.$$ That is, $u\lessdot_k u (i,j)$ if and only if ${\mathfrak S}_{u(i,j)}(x)$ appears in the product ${\mathfrak S}_{u}(x) \cdot {\mathfrak S}_{(k,k+1)}(x)$. Since $\ell(u)+1=\ell(u (i,j))$ if and only if $u(i)<u(j)$ and there does not exist $l$ such that $i < l < j$ and $u(i) < u(l) < u(j)$, we obtain the following equivalence.

::: proposition
[]{#nothing-in-between-is-in-between label="nothing-in-between-is-in-between"} Let $u$ and $w$ be two permutations. Then $u \lessdot_k w$ if and only if

1.  $w = u(i, j)$ for some $i \leq k < j$ such that $u(i) < u(j)$; and

2.  there does not exist $l$ such that $i < l < j$ and $u(i) < u(l) < u(j)$.
:::

Write $[u,w]_k$ for the interval between $u$ and $w$ in the $k$-Bruhat order. We may label each cover relation $u\lessdot_k u(i,j)$ with $i\leq k<j$ by $u(i)$ and write $${\color{RoyalBlue}u \xrightarrow{u(i)} u(i,j)}
    \qquad \text{if} \qquad
    u \lessdot_k u(i,j)\ \mbox{with}\ i\leq k<j\,.$$

A saturated chain $\gamma\colon u\xrightarrow{l_1}u_1\xrightarrow{l_2}\dotsb\xrightarrow{l_r}u_r$ in this poset has and we denote its maximal element by ${\color{RoyalBlue}\mathop{\mathrm{end}}(\gamma)} = u_r$. If in addition there exists a number $a$ such that $l_1>\dotsb >l_a<l_{a+1}<\dotsb<l_{r}$, then we say that $\gamma$ is a of and .

Figure [1](#F:k-Bruhat){reference-type="ref" reference="F:k-Bruhat"} shows two labeled intervals,

<figure id="F:k-Bruhat">
<div class="picture">
<p>(135,115)(-25,-2) (-4.5,0)<span><embed src="minimal4.eps" /></span> (5.5,100)<span><span class="math inline">$68357\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}421$</span></span> (-24.5, 75)<span><span class="math inline">$68257\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}431$</span></span> (35.5, 75)<span><span class="math inline">$68347\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}521$</span></span> (5.5, 50)<span><span class="math inline">$68247\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}531$</span></span> (65.5,50)<span><span class="math inline">$68345\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}721$</span></span> (-24.5, 25)<span><span class="math inline">$68237\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}541$</span></span> (35.5,25)<span><span class="math inline">$68245\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}731$</span></span> (5.5, 0)<span><span class="math inline">$68235\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}741$</span></span> ( 3, 89)<span><span class="math inline">2</span></span> ( 45, 89)<span><span class="math inline">4</span></span> ( 4, 63)<span><span class="math inline">4</span></span> ( 45, 61)<span><span class="math inline">2</span></span> ( 75, 65)<span><span class="math inline">5</span></span> ( 4, 40)<span><span class="math inline">3</span></span> ( 45, 40)<span><span class="math inline">5</span></span> ( 75, 36)<span><span class="math inline">2</span></span> ( 4, 11)<span><span class="math inline">5</span></span> ( 46, 11)<span><span class="math inline">3</span></span></p>
</div>
<div class="picture">
<p>(144,135)(-53,-2) (-33.5,0)<span><embed src="notminimal5.eps" /></span> ( 0,125)<span><span class="math inline">$627\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}4135$</span></span> ( 0,100)<span><span class="math inline">$427\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}6135$</span></span> (50,100)<span><span class="math inline">$624\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7135$</span></span> (-50, 75)<span><span class="math inline">$327\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}6145$</span></span> ( 0, 75)<span><span class="math inline">$426\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7135$</span></span> (50, 75)<span><span class="math inline">$623\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7145$</span></span> (-50, 50)<span><span class="math inline">$326\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7145$</span></span> ( 0, 50)<span><span class="math inline">$423\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7165$</span></span> (50, 50)<span><span class="math inline">$621\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7345$</span></span> (-50, 25)<span><span class="math inline">$324\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7165$</span></span> ( 0, 25)<span><span class="math inline">$421\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7365$</span></span> ( 0, 0)<span><span class="math inline">$321\raisebox{-0.5pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{9pt}}\hspace{0.55pt}7465$</span></span></p>
<p>( 10, 114)<span><span class="math inline">4</span></span> ( 42, 117)<span><span class="math inline">4</span></span> ( -17, 92)<span><span class="math inline">3</span></span> ( 10, 89)<span><span class="math inline">6</span></span> ( 68, 89)<span><span class="math inline">3</span></span> ( 18, 64)<span><span class="math inline">3</span></span> ( 42, 60)<span><span class="math inline">4</span></span> ( 68, 64)<span><span class="math inline">1</span></span> ( -40, 64)<span><span class="math inline">6</span></span> ( -9, 59)<span><span class="math inline">3</span></span> ( -40, 39)<span><span class="math inline">4</span></span> ( 18, 39)<span><span class="math inline">1</span></span> ( 42, 35)<span><span class="math inline">4</span></span> ( -12, 9)<span><span class="math inline">1</span></span> ( 18, 14)<span><span class="math inline">3</span></span></p>
</div>
<figcaption>Two intervals in <span class="math inline"><em>k</em></span>-Bruhat orders on <span class="math inline"><em>S</em><sub><em>n</em></sub></span>.</figcaption>
</figure>

one in the $5$-Bruhat order on $S_8$ and the other in the $3$-Bruhat order on $S_7$. The interval on the left has a peakless chain (colored in blue); its 'middle' chain has labels $5,3,2,4$, so it is peakless of height 3, but the other interval has no peakless chains.

## Grassmannian--Bruhat order {#SS:GBO}

We will make use of a second partial order on $S_n$ that is defined using the $k$-Bruhat order. Define the on $S_n$ by

$${\color{RoyalBlue}\eta\preceq\zeta}
    \qquad\text{if}\quad
    \begin{array}{c}
        \text{there exists $u \in S_n$ and $1\leq k < n$ with $u\leq_k \eta u\leq_k\zeta u$.}
    \end{array}$$ This is a graded partial order on $S_n$ with minimal element the identity permutation $e$. Its rank function is ${\color{RoyalBlue}{\mathcal L}(\zeta)}\vcentcolon=\ell(\zeta u)-\ell(u)$ for any $u \in S_n$ and $k \in {\mathbb N}$ with $u\leq_k\zeta u$. The cover relations inherit a labeling from the $k$-Bruhat orders. As shown in [@BS-Bruhat Sect. 3.2], neither $\preceq$, ${\mathcal L}$, nor the labeling depend on the choice of $k$ or $u$. For a permutation $\zeta\in S_n$, its is ${\color{RoyalBlue}\mathop{\mathrm{ht}}(\zeta)} \vcentcolon= \#\{i\in[n]\mid i<\zeta(i)\}$ and its is ${\color{RoyalBlue}\mathop{\mathrm{supp}}(\zeta)} = \{i\in[n]\mid\zeta(i)\neq i\}$. Then for any $\zeta \in S_n$ and $k$ satisfying $\mathop{\mathrm{ht}}(\zeta)\leq k\leq n-\#\mathop{\mathrm{supp}}(\zeta)+\mathop{\mathrm{ht}}(\zeta)$, there is a $u\in S_n$ with $u\leq_k \zeta u$ [@BS-Bruhat Thm. 3.1.5], which among other things implies that $e \preceq \zeta$.

The order $\preceq$ enjoys another symmetry. Permutations $\zeta\in S_n$ and $\eta\in S_m$ are if we have $\mathop{\mathrm{supp}}(\zeta)\subseteq\{i_1<\dotsb<i_r\}$ and $\mathop{\mathrm{supp}}(\eta)\subseteq\{j_1<\dotsb<j_r\}$ and for all $a,b$, $\zeta(i_a)=i_b$ if and only if $\eta(j_a)=j_b$. For example, the cycles $(2,3,5,7,4)$ and $(1,2,4,5,3)$ are shape-equivalent. Shape-equivalence induces an isomorphism on intervals [@BS-Bruhat Thm. 3.2.3(*v*)]. It also preserves the relative order of labels on chains, so that a chain in one interval is peakless if and only if the corresponding chain in a shape-equivalent interval is peakless.

We illustrate this. The intervals in Figure [1](#F:k-Bruhat){reference-type="ref" reference="F:k-Bruhat"} correspond to the permutations $\zeta_1=(2,3,5,7,4)$ and $\zeta_2=(1,7,4)(3,6)$ under the map that associates the permutation $v u^{-1}$ with the interval $[u, v]$. Figure [2](#F:GBorder){reference-type="ref" reference="F:GBorder"} shows labeled intervals $[e,\zeta_i]_\preceq$ for these two permutations, as well as for $\eta=(1,2,4,5,3)$, which is shape-equivalent to $\zeta_1$. The commas are omitted in the cycles for display purposes. The peakless chains in the intervals $[e,\zeta_1]_\preceq$ and $[e,\eta]_\preceq$ are highlighted.

<figure id="F:GBorder">
<div class="picture">
<p>(96,115)(-6,-2) ( 0,-1)<span><embed src="minimal4_narrow.eps" /></span> ( 9,100)<span><span class="math inline">(23574)</span></span> (-13, 75)<span><span class="math inline">(3574)</span></span> (30, 75)<span><span class="math inline">(234)(57)</span></span> ( 7.5, 50)<span><span class="math inline">(34)(57)</span></span> (65,50)<span><span class="math inline">(234)</span></span> ( -8, 25)<span><span class="math inline">(57)</span></span> (42,25)<span><span class="math inline">(34)</span></span> ( 25, 0)<span><span class="math inline"><em>e</em></span></span> ( 4, 90)<span><span class="math inline">2</span></span> ( 44, 90)<span><span class="math inline">4</span></span> ( 4, 62)<span><span class="math inline">4</span></span> ( 44, 62)<span><span class="math inline">2</span></span> ( 70, 63)<span><span class="math inline">5</span></span> ( 5, 39)<span><span class="math inline">3</span></span> ( 44, 39)<span><span class="math inline">5</span></span> ( 70, 36)<span><span class="math inline">2</span></span> ( 5, 10)<span><span class="math inline">5</span></span> ( 44, 10)<span><span class="math inline">3</span></span></p>
</div>
<div class="picture">
<p>(130,135)(-46,-2) (-33.5,0)<span><embed src="notminimal5_narrow.eps" /></span> (-7,125)<span><span class="math inline">(174)(36)</span></span> (-5,100)<span><span class="math inline">(17634)</span></span> (42,100)<span><span class="math inline">(14)(36)</span></span> (-45.5, 75)<span><span class="math inline">(1764)</span></span> (-0.5, 75)<span><span class="math inline">(1634)</span></span> (44.5, 75)<span><span class="math inline">(1364)</span></span> (-43, 50)<span><span class="math inline">(164)</span></span> ( 2, 50)<span><span class="math inline">(134)</span></span> (47, 50)<span><span class="math inline">(364)</span></span> (-40, 25)<span><span class="math inline">(14)</span></span> ( 5, 25)<span><span class="math inline">(34)</span></span> (14, 0)<span><span class="math inline"><em>e</em></span></span></p>
<p>( 9, 114)<span><span class="math inline">4</span></span> ( 40, 117)<span><span class="math inline">4</span></span> ( -17, 92)<span><span class="math inline">3</span></span> ( 18, 89)<span><span class="math inline">6</span></span> ( 64, 89)<span><span class="math inline">3</span></span> ( 18, 64)<span><span class="math inline">3</span></span> ( 41, 60)<span><span class="math inline">4</span></span> ( 64, 64)<span><span class="math inline">1</span></span> ( -39, 64)<span><span class="math inline">6</span></span> ( -8, 59)<span><span class="math inline">3</span></span> ( -39, 39)<span><span class="math inline">4</span></span> ( 18, 39)<span><span class="math inline">1</span></span> ( 41, 35)<span><span class="math inline">4</span></span> ( -13, 9)<span><span class="math inline">1</span></span> ( 18, 13)<span><span class="math inline">3</span></span></p>
</div>
<div class="picture">
<p>(96,115)(-6,-2) ( 0, -1)<span><embed src="minimal4_narrow.eps" /></span> ( 9,100)<span><span class="math inline">(12453)</span></span> (-13, 75)<span><span class="math inline">(2453)</span></span> (30,75)<span><span class="math inline">(123)(45)</span></span> ( 7.5, 50)<span><span class="math inline">(23)(45)</span></span> (65,50)<span><span class="math inline">(123)</span></span> ( -8, 25)<span><span class="math inline">(45)</span></span> (42,25)<span><span class="math inline">(23)</span></span> ( 25, 0)<span><span class="math inline"><em>e</em></span></span></p>
<p>( 4, 90)<span><span class="math inline">1</span></span> ( 44, 90)<span><span class="math inline">3</span></span> ( 4, 62)<span><span class="math inline">3</span></span> ( 44, 61)<span><span class="math inline">1</span></span> ( 70, 63)<span><span class="math inline">4</span></span> ( 5, 39)<span><span class="math inline">2</span></span> ( 44, 39)<span><span class="math inline">4</span></span> ( 70, 36)<span><span class="math inline">1</span></span> ( 5, 10)<span><span class="math inline">4</span></span> ( 44, 10)<span><span class="math inline">2</span></span></p>
</div>
<figcaption>Intervals in the Grassmannian–Bruhat order.</figcaption>
</figure>

## Minimal permutations

A permutation $\zeta$ is if ${\mathcal L}(\zeta) = \#\mathop{\mathrm{supp}}(\zeta) - s(\zeta)$, where ${\color{RoyalBlue}s(\zeta)}$ is the number of (nontrivial) cycles in the factorization of $\zeta$ into disjoint cycles. Minimality is a central concept in this paper. This terminology (introduced in [@BS-Bruhat]) arises from the inequality ${\mathcal L}(\zeta) \geq \#\mathop{\mathrm{supp}}(\zeta) - s(\zeta)$, so that a minimal permutation has the minimal possible rank given its cycle structure. For example, $\zeta_1 = (2,3,5,7,4)$ is minimal, because $${\mathcal L}(\zeta_1) = \ell(68357421) - \ell(68235741) = 22 - 18 = 4 = \#\mathop{\mathrm{supp}}(\zeta_1) - s(\zeta_1);$$ and $\zeta_2 = (1,7,4)(3,6)$ is not minimal, because $${\mathcal L}(\zeta_2) = \ell(6274135) - \ell(3217465) = 12 - 7 = 5 > 3 = \#\mathop{\mathrm{supp}}(\zeta_2) - s(\zeta_2).$$

Related to minimality is the notion of crossing. Let $l_1<l_2$ and $m_1<m_2$ be two disjoint pairs of numbers, and suppose that $l_1<m_1$. There are three possibilities for $l_2$. Either $l_2<m_1$ or $m_1<l_2<m_2$ or $m_2<l_2$. When the second occurs, we say that the pairs are , otherwise they are . This refers to arcs connecting elements of each pair, when the numbers are marked along a number line. $$\begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{nonnesting.eps}}
    \put(6,-9){$l_1$}  \put(36,-9){$l_2$}  \put(66,-9){$m_1$}  \put(96,-9){$m_2$}
    \put(24,-24){noncrossing}
   \end{picture}
   \qquad
   \begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{crossing.eps}}
    \put(6,-9){$l_1$}  \put(36,-9){$m_1$}  \put(66,-9){$l_2$}  \put(96,-9){$m_2$}
    \put(34,-24){crossing}
   \end{picture}
   \qquad
   \begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{nesting.eps}}
    \put(6,-9){$l_2$}  \put(36,-9){$m_1$}  \put(66,-9){$m_2$}  \put(96,-9){$l_2$}
    \put(24,-24){noncrossing}
   \end{picture}$$ Let $A,B\subset[n]$ be disjoint and suppose that each has at least two elements. If there exist a pair of elements of $A$ and a pair of elements of $B$ that are crossing, then $A$ and $B$ are ; otherwise they are .

A product $\zeta\cdot\eta$ of two permutations is when $\mathop{\mathrm{supp}}(\zeta)$ and $\mathop{\mathrm{supp}}(\eta)$ are disjoint and noncrossing. A permutation $\zeta$ is if it cannot be written nontrivially as a noncrossing product. Any permutation factors uniquely as a noncrossing product of irreducible permutations. In [@BS-Bruhat], $s(\zeta)$ counted the number of irreducible factors in the noncrossing factorization of $\zeta$ for minimal permutations. By [@BS-Bruhat Lem. 3.3.1] we have that $s(\zeta)$ is the number of cycles (this is also explained in the proof below). We give a characterization of minimal permutations in terms of peakless chains in the Grassmannian--Bruhat order.

<figure id="F:product">
<div class="picture">
<p>(26,80)(-11,0) (0,0)<span><embed src="row.eps" /></span> (-12,50)<span><span class="math inline">(176)</span></span> (-10,25)<span><span class="math inline">(16)</span></span> (-1,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<div class="picture">
<p>(74,85)(-1,0) (10,0)<span><embed src="hook.eps" /></span> (21,75)<span><span class="math inline">(2354)</span></span> (-0.5,50)<span><span class="math inline">(354)</span></span> (49,50)<span><span class="math inline">(234)</span></span> (27,25)<span><span class="math inline">(34)</span></span> (34.5,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<div class="picture">
<p>(275,135)(-13,0) (-1,0)<span><embed src="product.eps" /></span> (11,125)<span><span class="math inline">(176)(2354)</span></span> (-13,100)<span><span class="math inline">(176)(354)</span></span> (47.5,100)<span><span class="math inline">(176)(234)</span></span> (19.5,75)<span><span class="math inline">(176)(34)</span></span> (29,50)<span><span class="math inline">(176)</span></span></p>
<p>(108,100)<span><span class="math inline">(16)(2354)</span></span> (80.5,75)<span><span class="math inline">(16)(354)</span></span> (141,75)<span><span class="math inline">(16)(234)</span></span> (114,50)<span><span class="math inline">(16)(34)</span></span> (124,25)<span><span class="math inline">(16)</span></span></p>
<p>(208,75)<span><span class="math inline">(2354)</span></span> (180,50)<span><span class="math inline">(354)</span></span> (240,50)<span><span class="math inline">(234)</span></span> (212,25)<span><span class="math inline">(34)</span></span> (220,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<figcaption>If <span class="math inline"><em>ζ</em> ⋅ <em>η</em></span> is a noncrossing product, then the interval <span class="math inline">[<em>e</em>,<em>ζ</em>⋅<em>η</em>]<sub>≼</sub></span> is isomorphic to the product of the intervals <span class="math inline">[<em>e</em>,<em>ζ</em>]<sub>≼</sub></span> and <span class="math inline">[<em>e</em>,<em>η</em>]<sub>≼</sub></span>, and the chains in <span class="math inline">[<em>e</em>,<em>ζ</em>⋅<em>η</em>]<sub>≼</sub></span> are shuffles of chains in each of the factors.</figcaption>
</figure>

::: lemma
[]{#L:properties-noncrossing-products label="L:properties-noncrossing-products"} Let $\zeta$ be a permutation and $\zeta=\zeta_1\dotsb \zeta_s$ its unique factorization into a noncrossing product of irreducible permutations.

1.  ${\mathcal L}(\zeta)= {\mathcal L}(\zeta_1)+\dotsb+{\mathcal L}(\zeta_s).$

2.  $[e,\zeta]_\preceq\ \simeq\  [e,\zeta_1]_\preceq\ \times\ \dotsb\ \times\  [e,\zeta_s]_\preceq.$

3.  $[e,\zeta]_\preceq$ has a peakless chain if and only if each interval $[e,\zeta_i]_\preceq$ has a peakless chain.

4.  $\zeta$ is a minimal permutation if and only if each $\zeta_i$ is a minimal permutation.

5.  If $\zeta$ is minimal and irreducible, then $\zeta$ is a cycle.
:::

::: proof
*Proof.* (1) By [@BS-Bruhat Lem. 3.3.1], ${\mathcal L}(\zeta)= {\mathcal L}(\zeta_1)+\dotsb+{\mathcal L}(\zeta_s)$ as this is a noncrossing product.

\(2\) [@BS-Bruhat Lem. 3.3.3] implies that $[e,\zeta]_\preceq\ \simeq\  [e,\zeta_1]_\preceq\ \times\ \dotsb\ \times\  [e,\zeta_s]_\preceq$.

\(3\) If each interval $[e, \zeta_i]_{\preceq}$ has a peakless chain $\gamma_i$, then shuffling these chains appropriately gives a peakless chain $\gamma$ in $[e,\zeta]_\preceq$ by (2). Conversely, if $\gamma$ is a peakless chain in $[e,\zeta]_\preceq$, restricting it to each $[e,\zeta_i]_\preceq$ gives a peakless chain $\gamma_i$. Figure [3](#F:product){reference-type="ref" reference="F:product"} illustrates this for the noncrossing product of the two minimal permutations $\zeta=(1,7,6)$ and $\eta=(2,3,5,4)$. The peakless chains are indicated, and commas in cycles are omitted for display purposes.

\(4\) follows from (1) and (2).

\(5\) Suppose that $\zeta$ is minimal and irreducible. If $\zeta$ is not a single cycle, then $\zeta=\eta\cdot \eta'$, where $\eta$ and $\eta'$ have disjoint supports that are crossing. By [@BS-Bruhat Lem. 3.3.1], ${\mathcal L}(\zeta)> {\mathcal L}(\eta) + {\mathcal L}(\eta')$, which contradicts that $\zeta$ is minimal. This inequality is illustrated by $\zeta=(1,7,4)(3,6)$. We showed that ${\mathcal L}(\zeta)=5$, but ${\mathcal L}(1,7,4) = 2$ and ${\mathcal L}(3,6)=1$. ◻
:::

::: proposition
[]{#P:peaklessChains label="P:peaklessChains"} A permutation $\zeta$ is minimal if and only if the interval $[e,\zeta]_\preceq$ has a peakless chain. The number of peakless chains of height $a$ in $[e,\zeta]_\preceq$ is the binomial coefficient $\left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)$.
:::

::: proof
*Proof.* We begin by showing that the first statement follows from the corresponding result for irreducible permutations. Let $\zeta=\zeta_1\dotsb \zeta_s$ be the unique factorization of $\zeta$ into a noncrossing product of irreducible permutations. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, $\zeta$ is minimal if and only if each $\zeta_i$ is minimal. Since $\zeta_i$ is irreducible, $\zeta$ is minimal if and only if each interval $[e, \zeta_i]_{\preceq}$ has a peakless chain. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, this holds if and only if $[e, \zeta]_{\preceq}$ has a peakless chain.

We now prove the result for irreducible permutations. Suppose that $\zeta$ is minimal and irreducible. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, $\zeta$ is a single cycle. In [@BS-iso Lem. 6.7] it is proved that if $\zeta$ is a minimal cycle, then there is a unique peakless chain in the interval $[e, \zeta]_\preceq$, which proves the forward direction. Conversely, suppose that $[e, \zeta]_\preceq$ has a peakless chain. Let $a$ be the height of that chain and set ${\color{RoyalBlue}b}\vcentcolon={\mathcal L}(\zeta){-}a{+}1$. Replacing $\zeta$ by a shape-equivalent permutation if necessary, we may assume that $\mathop{\mathrm{supp}}(\zeta)=[n]$ (so that $\zeta\in S_n$) and thus ${\mathcal L}(\zeta) \geq
\#\mathop{\mathrm{supp}}(\zeta) - s(\zeta) = n-1$.

Since $e \preceq \zeta$, there is a $k < n$ and $u \in S_n$ such that $u \leq_k \zeta u$ and $[e, \zeta]_\preceq \simeq [u, \zeta u]_k$. By [@BS-Bruhat Thm. 3.1.5], we have $$\{i \mid i < \zeta(i)\}\ \subseteq\ \{u^{-1}(1), \ldots, u^{-1}(k)\}
    \quad\text{and}\quad
    \{i \mid i > \zeta(i)\}\ \subseteq\ \{u^{-1}(k + 1), \ldots, u^{-1}(n)\}$$ so that $$\mathop{\mathrm{ht}}(\zeta)\ =\ \#\{i \mid i < \zeta(i)\} \leq k
    \quad\text{and}\quad
    n - \mathop{\mathrm{ht}}(\zeta)\ =\ \#\{i \mid i > \zeta(i)\} \leq n - k.$$ Together, these imply that $\mathop{\mathrm{ht}}(\zeta) = k$. Since there is a peakless chain in $[e,\zeta]_\preceq$ and $[e,\zeta]_\preceq\simeq[u,\zeta u]_k$, it follows from Formula [\[eq:schubert-times-hook-via-peakless-chains\]](#eq:schubert-times-hook-via-peakless-chains){reference-type="eqref" reference="eq:schubert-times-hook-via-peakless-chains"} below that the coefficient $c^{\zeta u}_{u, v((b,1^{a-1}),k)}$ is nonzero. This implies that $v((b,1^{a-1}),k)\leq_k \zeta u$. As $\zeta u\in S_n$, we have $v((b,1^{a-1}),k)\in S_n$. Thus $a\leq k<n$ and $b\leq n{-}k$, so that ${\mathcal L}(\zeta)=a{+}b{-}1\leq n{-}1$. This implies that ${\mathcal L}(\zeta)=n{-}1$, $a=k$, and $b=n{-}k$. As $n=\#\mathop{\mathrm{supp}}(\zeta)$, we conclude that $\zeta$ is a minimal cycle and that $[e, \zeta]_\preceq$ has a unique peakless chain. Note that since $s(\zeta) = 1$ and $\mathop{\mathrm{ht}}(\zeta) = a$, we have $\left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)
= \left(\begin{smallmatrix} 0 \\ 0 \end{smallmatrix}\right) = 1$.

Finally, suppose that $\zeta=\zeta_1\dotsb\zeta_s$ is the noncrossing factorization of a minimal permutation $\zeta$ into disjoint minimal cycles $\zeta_1,\dotsc,\zeta_s$. Recall from Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"} that $[e,\zeta]_\preceq \simeq  [e,\zeta_1]_\preceq \times \dotsb \times  [e,\zeta_s]_\preceq.$ We count the shuffles of peakless chains $\gamma_i$ in $[e,\zeta_i]_\preceq$ with a given height. We need only consider the sequence of labels, and note that as the cycles $\zeta_i$ have disjoint supports, the set of labels on the chains $\gamma_i$ are disjoint. Partition a peakless chain (represented by its labels)

$$\label{Eq:Peakless_Partition}
    l_1\ >\ \dotsb\ >\ l_{a-1} \ >\  l_a\ <\ l_{a+1}\ <\ \dotsb\ <\ l_{a+b-1}$$

into three subsets. Call $l_1> \dotsb>l_{a-1}$ the decreasing segment, $l_a$ the minimum, and $l_{a+1} <\dotsb<l_{a+b-1}$ the increasing segment.

In a peakless chain [\[Eq:Peakless_Partition\]](#Eq:Peakless_Partition){reference-type="eqref" reference="Eq:Peakless_Partition"} of height $a$ in $[e,\zeta]_\preceq$, its decreasing segment contains the decreasing segments of each $\gamma_i$, and the same for increasing segments. Its minimum $l_a$ is the minimum of all the minima of the $\gamma_i$. The only choices possible are distributing the remaining $s{-}1$ minima between the decreasing and increasing segments of [\[Eq:Peakless_Partition\]](#Eq:Peakless_Partition){reference-type="eqref" reference="Eq:Peakless_Partition"}, which may be done independently. Since $\mathop{\mathrm{ht}}(\zeta)=\mathop{\mathrm{ht}}(\zeta_1)+\dotsb+\mathop{\mathrm{ht}}(\zeta_s)$, we see that placing $\mathop{\mathrm{ht}}(\zeta)-a$ of these remaining minima in the increasing segment gives a peakless chain of height $a$. This completes the proof. ◻
:::

## A Murnaghan--Nakayama rule for $H^*{\mathbb F}\ell_n$

We recall the following special case of Formula [\[eq:classical-coeffs\]](#eq:classical-coeffs){reference-type="eqref" reference="eq:classical-coeffs"}, which is [@So96 Cor. 9].

::: proposition
[]{#pieri-formulas-version-2 label="pieri-formulas-version-2"} Let $u \in S_n$, $a\leq k$, and $b\leq n{-}k$. Then $$\label{eq:schubert-times-hook-via-peakless-chains}
        {\mathfrak S}_u(x)\cdot s_{(b,1^{a-1})}(x_1,\dotsc,x_k)\ =\ \sum_\gamma {\mathfrak S}_{\mathop{\mathrm{end}}(\gamma)}(x)\,,$$ the sum over all peakless chains starting at $u$ of height $a$ and length $a{+}b{-}1$ in the $k$-Bruhat order.
:::

Using Proposition [\[P:peaklessChains\]](#P:peaklessChains){reference-type="ref" reference="P:peaklessChains"}, we can explicitly describe the coefficients appearing in [\[eq:schubert-times-hook-via-peakless-chains\]](#eq:schubert-times-hook-via-peakless-chains){reference-type="eqref" reference="eq:schubert-times-hook-via-peakless-chains"}.

::: proposition
[]{#P:classical_hook label="P:classical_hook"} Let $u \in S_n$, $a\leq k$ and $b\leq n{-}k$. Then $$\label{Eq:Schubert-times-hook}
        {\mathfrak S}_u(x) \cdot s_{(b, 1^{a-1})}(x_1,\dotsc,x_k)\ =\
        \sum
        \left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)
        {\mathfrak S}_{\zeta u}(x) \,,$$ the sum over all minimal permutations $\zeta \in S_n$ such that $u\leq_k\zeta u$ and ${\mathcal L}(\zeta)=a+b-1$.
:::

We use Proposition [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"} to derive a formula for the product of a Schubert polynomial and a power sum symmetric polynomial. Let ${\color{RoyalBlue}p_r(x_1,\dotsc,x_k)}\vcentcolon=x_1^r+\dotsb+x_k^r$ denote the $r$th power sum polynomial. Expanded in terms of Schur polynomials [@Macdonald], we have $$\label{Eq:PowerSumHook}
    p_r(x_1, \ldots, x_k) =
    s_{(r)}(x_1, \ldots, x_k) - s_{(r-1,1)}(x_1, \ldots, x_k) + \cdots + (-1)^{r+1} s_{(1^r)}(x_1, \ldots, x_k).$$

::: corollary
[]{#C:classical-schubert-times-powersum label="C:classical-schubert-times-powersum"} Let $u \in S_n$. Then $${\mathfrak S}_u(x) \cdot p_r(x_1,\dotsc,x_k)\ =\ \sum (-1)^{\mathop{\mathrm{ht}}(\zeta)+1} {\mathfrak S}_{\zeta u}(x)\,,$$

the sum over all minimal cycles $\zeta \in S_n$ such that $u\leq_k\zeta u$ and ${\mathcal L}(\zeta)=r$.
:::

::: proof
*Proof.* Expanding the product ${\mathfrak S}_u(x) \cdot p_r(x_1,\dotsc,x_k)$ using Equations [\[Eq:Schubert-times-hook\]](#Eq:Schubert-times-hook){reference-type="eqref" reference="Eq:Schubert-times-hook"} and [\[Eq:PowerSumHook\]](#Eq:PowerSumHook){reference-type="eqref" reference="Eq:PowerSumHook"} shows that the coefficient of ${\mathfrak S}_{\zeta u}$ for $u\leq_k\zeta u$ is zero unless ${\mathcal L}(\zeta)=r$ and $\zeta$ is minimal. When $\zeta$ is the noncrossing product of $s(\zeta)$ minimal cycles, this coefficient is $$(-1)^{\mathop{\mathrm{ht}}(\zeta)+1} \sum_{a=1}^{r} (-1)^{a-\mathop{\mathrm{ht}}(\zeta)}\binom{s(\zeta)-1}{\mathop{\mathrm{ht}}(\zeta)-a}\ =\
        \begin{cases}
            0,  & \text{ if } s(\zeta)\neq 1,\\
            (-1)^{\mathop{\mathrm{ht}}(\zeta)+1},& \text{ if } s(\zeta)=1.
        \end{cases}
        \qedhere$$ ◻
:::

This proof differs from that given in [@Morrison; @MorrisonSottile].
