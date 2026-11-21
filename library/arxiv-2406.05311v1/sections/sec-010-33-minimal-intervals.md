---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-010-33-minimal-intervals
section_title: "Minimal intervals"
section_number: 3.3
pages: 10-10
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 1.0
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
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
