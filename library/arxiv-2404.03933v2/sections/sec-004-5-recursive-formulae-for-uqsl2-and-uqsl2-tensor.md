---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-004-5-recursive-formulae-for-uqsl2-and-uqsl2-tensor
section_title: "Recursive formulae for Uq(sl2) and uq(sl2) tensor products."
section_number: 5
pages: 13-14
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.789
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#recursion label="recursion"} Denote by $T(lk_1 + k_0)$ the indecomposable tilting module over $U_q ({\mathfrak{s}l}_2)$ of type 1 with the highest weight $lk_1 + k_0$, with $0 \leq k_0 \leq l-1$, $k_1 \geq 0$. Note that modules $T(k)=L(k)=W(k)$ are irreducible when $0\leq k\leq l-1$ or $k=lk_1-1$.

Then we have: $$\begin{aligned}
\label{A}
T(k_0) \otimes T(1) &=& T(k_0+1) \oplus T(k_0 -1),  \quad 0 \leq  k_0 \leq l-2,  \\ 
T(lk_1 + k_0) \otimes T(1) &=& T(lk_1 + k_0 +1) \oplus T(lk_1 + k_0 -1) ,  \quad 1 \leq k_0 \leq l-3,\, k_1\geq 1 , \nonumber \\ 
T(lk_1 + l-2) \otimes T(1) &=& T(l(k_1 +1) -3) \oplus T((k_1+1)l-1) \oplus T((k_1-1)l-1) ,  \quad  k_1\geq 2, \nonumber \\ 
T(2l-2) \otimes T(1) &=& T(2l-1) \oplus T(2l-3) ,\nonumber \\
T(l k_1 -1) \otimes T(1) &=& T(lk_1) , \quad  k_1 \geq 1,\nonumber \\
T(lk_1) \otimes T(1) &=& T(lk_1 +1) \oplus 2 T(lk_1 -1) , \quad k_1\geq 1.\nonumber
\end{aligned}$$ We assume everywhere that $T(m) =0$ if $m <0$.

Similarly, we can derive recursive tensor product decomposition over the small quantum group $u_q$. Over $u_q(\mathfrak{sl}_2)$ we have the following indecomposable modules that can appear in the powers of $T(1)=L(1)$ of type $1$: $$W(k_0)=L(k_0)=T(k_0),\quad\text{for $0 \leq k_0 \leq l-2$},$$ $$T_+ (l-1)=T(l-1),$$ $$T_+(l+ k_0)=T(l+k_0),\quad\text{for $0 \leq k_0 \leq l-2$},$$ $$T_-(l-1)=T(l-1)\otimes 1_-,$$ $$T_-(l+k_0)=T(l+k_0) \otimes 1_-,\quad\text{for $0 \leq k_0 \leq l-2$}.$$ Then we have: $$\begin{aligned}
\label{B}
T(k_0) \otimes T(1)  &=& T(k_0-1) \oplus T(k_0 +1) , \quad  1 \leq k_0 \leq l-2,  \\ 
T_{\pm}(l-1) \otimes T(1)  &=& T_{\pm}(l),\nonumber \\ 
T_{\pm}(l) \otimes T(1)  &=& T_{\pm}(l+1) \oplus 2 T_{\pm}(l-1),\nonumber \\ 
T_{\pm}(l+ k_0) \otimes T(1) &=& T(l +k_0 -1)_{\pm} \oplus  T_{\pm}(l+k_0 +1) ,\quad 1 \leq k_0 \leq l-3,\nonumber \\ 
T_{\pm}(2l-2) \otimes T(1) &=& T_{\pm}(2l-3) \oplus 2 T_{\mp} (l-1).\nonumber
\end{aligned}$$
