---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-004-23-grassmannianbruhat-order
section_title: "Grassmannian–Bruhat order"
section_number: 2.3
pages: 4-5
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.951
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#SS:GBO label="SS:GBO"}

We will make use of a second partial order on $S_n$ that is defined using the $k$-Bruhat order. Define the on $S_n$ by

$${\color{RoyalBlue}\eta\preceq\zeta}
    \qquad\text{if}\quad
    \begin{array}{c}
        \text{there exists $u \in S_n$ and $1\leq k < n$ with $u\leq_k \eta u\leq_k\zeta u$.}
    \end{array}$$ This is a graded partial order on $S_n$ with minimal element the identity permutation $e$. Its rank function is ${\color{RoyalBlue}{\mathcal L}(\zeta)}\vcentcolon=\ell(\zeta u)-\ell(u)$ for any $u \in S_n$ and $k \in {\mathbb N}$ with $u\leq_k\zeta u$. The cover relations inherit a labeling from the $k$-Bruhat orders. As shown in [@BS-Bruhat Sect. 3.2], neither $\preceq$, ${\mathcal L}$, nor the labeling depend on the choice of $k$ or $u$. For a permutation $\zeta\in S_n$, its is ${\color{RoyalBlue}\mathop{\mathrm{ht}}(\zeta)} \vcentcolon= \#\{i\in[n]\mid i<\zeta(i)\}$ and its is ${\color{RoyalBlue}\mathop{\mathrm{supp}}(\zeta)} = \{i\in[n]\mid\zeta(i)\neq i\}$. Then for any $\zeta \in S_n$ and $k$ satisfying $\mathop{\mathrm{ht}}(\zeta)\leq k\leq n-\#\mathop{\mathrm{supp}}(\zeta)+\mathop{\mathrm{ht}}(\zeta)$, there is a $u\in S_n$ with $u\leq_k \zeta u$ [@BS-Bruhat Thm. 3.1.5], which among other things implies that $e \preceq \zeta$.

The order $\preceq$ enjoys another symmetry. Permutations $\zeta\in S_n$ and $\eta\in S_m$ are if we have $\mathop{\mathrm{supp}}(\zeta)\subseteq\{i_1<\dotsb<i_r\}$ and $\mathop{\mathrm{supp}}(\eta)\subseteq\{j_1<\dotsb<j_r\}$ and for all $a,b$, $\zeta(i_a)=i_b$ if and only if $\eta(j_a)=j_b$. For example, the cycles $(2,3,5,7,4)$ and $(1,2,4,5,3)$ are shape-equivalent. Shape-equivalence induces an isomorphism on intervals [@BS-Bruhat Thm. 3.2.3(*v*)]. It also preserves the relative order of labels on chains, so that a chain in one interval is peakless if and only if the corresponding chain in a shape-equivalent interval is peakless.

We illustrate this. The intervals in Figure [\[F:k-Bruhat\]](#F:k-Bruhat){reference-type="ref" reference="F:k-Bruhat"} correspond to the permutations $\zeta_1=(2,3,5,7,4)$ and $\zeta_2=(1,7,4)(3,6)$ under the map that associates the permutation $v u^{-1}$ with the interval $[u, v]$. Figure [1](#F:GBorder){reference-type="ref" reference="F:GBorder"} shows labeled intervals $[e,\zeta_i]_\preceq$ for these two permutations, as well as for $\eta=(1,2,4,5,3)$, which is shape-equivalent to $\zeta_1$. The commas are omitted in the cycles for display purposes. The peakless chains in the intervals $[e,\zeta_1]_\preceq$ and $[e,\eta]_\preceq$ are highlighted.

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
