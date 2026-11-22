---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-005-the-left-multiplication-algebra-of-cs
section_title: "The left multiplication algebra of CS"
section_number: null
pages: 7-8
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.81
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
---
Despite the algebra $\mathbb{S}$ being non-associative and non-alternative, just as for $\mathbb{O}$, we can consider the left actions of $\mathbb{S}$ on itself as linear operators generating an associative algebra.

The generalisation from $(\mathbb{C}\otimes\mathbb{O})_L$ to $(\mathbb{C}\otimes\mathbb{S})_L$ is not immediately obvious because the identities which held for $(\mathbb{C}\otimes\mathbb{O})_L$, namely $$\begin{aligned}
    L_{i_1}L_{i_2}L_{i_3}L_{i_4}L_{i_5}L_{i_6}x&=&L_{i_7}x,\\
    ...L_{i_b}L_{i_a}L_{i_a}L_{i_c}....x&=&-...L_{i_b}L_{i_c}....x,\label{octidentity1}\\
    ...L_{i_a}L_{i_b}...x&=&-...L_{i_b}L_{i_a}...,\label{octidentity2}
\end{aligned}$$ where $a,b,c=1,...,7$ are no longer satisfied by general composition of sedenion left multiplications. Although one finds a new identify $$\begin{aligned}
\label{sedenionidentity}
L_{s_1}L_{s_2}...L_{s_{14}}w=L_{s_{15}}w,
\end{aligned}$$ the two identities ([\[octidentity1\]](#octidentity1){reference-type="ref" reference="octidentity1"}) and ([\[octidentity2\]](#octidentity2){reference-type="ref" reference="octidentity2"}), crucial for generating a Clifford algebra, no longer hold in general. For example, $s_3(s_{14}(s_1)) = -s_{14}(s_3(s_1))$, but $s_3(s_{14}(s_2)) = +s_{14}(s_3(s_2)$. Consequently, the left multiplications of the (complex) sedenions do not generate $\mathbb{C}\ell(14)$, as one might initially expect.

However, since the linear operators corresponding to each complex sedenion left multiplication can be written as a $16\times 16$ matrix with complex entries acting on $\mathbb{C}\otimes\mathbb{S}$ written as a column vector, one would expect to be able to generate $Mat(16,\mathbb{C})\cong \mathbb{C}\ell(8)$. It then remains to find a suitable set of sedenion elements that generate $\mathbb{C}\ell(8)$ via their left multiplication. Closer inspection reveals that all the left multiplications of the original octonion elements $e_0=i_0=s_0,...,e_7=i_7=s_7$ do satisfy the identities ([\[octidentity1\]](#octidentity1){reference-type="ref" reference="octidentity1"}) and ([\[octidentity2\]](#octidentity2){reference-type="ref" reference="octidentity2"}) (where now the action is on $\mathbb{C}\otimes\mathbb{S}$ instead of $\mathbb{C}\otimes\mathbb{O}$), as do all new sedenion basis elements $e_9=s_7,...,e_{15}=s_{15}$: $$\begin{aligned}
    e_i(e_jw)&=&-e_j(e_iw),\qquad e_{i+8}(e_{j+8}w)= -e_{j+8}(e_{i+8}w),\\
    e_i(e_iw)&=&-w,\qquad e_{i+8}(e_{i+8}w)= -w\quad i,j=1,...,7,\quad \forall w\in\mathbb{C}\otimes\mathbb{S}
\end{aligned}$$ However, $e_i$ and $e_{i+8}$ fail to anti-commute (or commute) with each other as left actions $$\begin{aligned}
   e_i(e_{j+8}w)\neq -e_{j+8}(e_iw). 
\end{aligned}$$ The left action of $e_8$ however anti-commutes with the left action of every other basis element. One possible generating basis for $\mathbb{C}\ell(8)$ is therefore given by the left multiplications of $\{e_1,...,e_8\}$. Another possible generating basis is $\{e_8,...,e_{15}\}$.

Accepting some abuse of notation, we now simple write $L_{e_i}=e_i$ and take ${e_0,e_1,...,e_8}$ as our generating basis for $\mathbb{C}\ell(8)$. The left action of the remaining sedenion basis elements $e_9,...,e_{15}$ then need to be expressed as the left action of some element of $\mathbb{C}\ell(8)$. After some trial and error, one finds that $$\begin{aligned}
    e_9w&=&\frac{1}{2}(-e_{123458}+e_{123678}+e_{145678}-e_{18})w,\\
    e_{10}w&=&\frac{1}{2}(-e_{123468}-e_{123578}+e_{245678}-e_{28})w,\\
    e_{11}w&=&\frac{1}{2}(-e_{123478}+e_{123568}+e_{345678}-e_{38})w\\
    e_{12}w&=&\frac{1}{2}(e_{124568}+e_{134578}+e_{234678}-e_{48})w\\
    e_{13}w&=&\frac{1}{2}(e_{124578}-e_{134568}+e_{235678}-e_{58})w\\
    e_{14}w&=&\frac{1}{2}(e_{124678}-e_{135678}-e_{234568}-e_{68})w\\
    e_{15}w&=&\frac{1}{2}(e_{125678}+e_{134678}-e_{234578}-e_{78})w,
\end{aligned}$$ where $e_{123458}=e_1e_2e_3e_4e_5e_8=L_{e_1}L_{e_2}L_{e_3}L_{e_4}L_{e_5}L_{e_8}$, $e_{18}=e_1e_8=L_{e_1}L_{e_8}$ etc are elements of $\mathbb{C}\ell(8)$.
