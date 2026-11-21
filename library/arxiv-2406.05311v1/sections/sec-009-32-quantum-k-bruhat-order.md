---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-009-32-quantum-k-bruhat-order
section_title: "Quantum k-Bruhat order"
section_number: 3.2
pages: 9-10
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.833
latex_coverage_ratio: 0.964
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#quantum-k-bruhat-order label="quantum-k-bruhat-order"}

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
