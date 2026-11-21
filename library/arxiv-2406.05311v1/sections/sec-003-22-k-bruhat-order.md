---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-003-22-k-bruhat-order
section_title: "k-Bruhat order"
section_number: 2.2
pages: 3-4
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.857
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
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
