---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-002-21-some-definitions-and-notations
section_title: "Some definitions and notations"
section_number: 2.1
pages: 5-6
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.938
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
We refer to \cite[Section 2]{mue09} for our general conventions and recall only a few less
standard notations. A retract $Y\prec X$ is also called a subobject. A category has
subobjects if all idempotents split, and every category $\2A$ has a canonical completion 
$\ol{\2A}^p$ for which this is the case. A $\7F$-linear category is semisimple if it has
direct sums and subobjects and every object is a finite direct sum of simple objects, $X$
being simple iff $\End(X)\cong\7F$. For monoidal categories we require in addition that
$\11$ is simple. A subcategory of a semisimple category is called semisimple if it is
closed w.r.t.\ direct sums and retractions, thus in particular replete (stable under
isomorphisms).

Since all categories in question are $\7F$-linear we understand the product 
$\2K\otimes_\7F\2L$ of (tensor) categories in the sense of enriched category theory. Thus 
\[ \obj\,\2K\otimes_\7F\2L = \{ K\boxtimes L,\ K\in \obj\,\2K, L\in \obj\,\2L\}, \]
where $X\boxtimes Y$ stands for the pair $(X,Y)$, and
\[ \Hom_{\2K\otimes_\7F\2L}(K_1\boxtimes L_1, K_2\boxtimes L_2))= 
   \Hom_\2K(K_1,K_2)\otimes_\7F\Hom_\2L(L_1,L_2) \]
with the obvious composition laws. 
We denote by $\2K\boxtimes\2L=\ol{\2K\otimes_\7F\2L}^\oplus$ the completion w.r.t.\
finite direct sums. If $\2X, \2Y$ are monoidal categories the same holds for
$\2X\boxtimes\2Y$. In order to save brackets we declare $\boxtimes$ to bind stronger than 
$\otimes$ but weaker than juxtaposition $XY$ of objects (which abbreviates $X\otimes
Y$). Note that $\otimes$ and $\boxtimes$ commute: 
\[ X_1\boxtimes Y_1 \,\otimes\, X_2\boxtimes Y_2=
  (X_1\otimes X_2) \,\boxtimes\, (Y_1\otimes Y_2)=
   X_1X_2 \,\boxtimes\, Y_1 Y_2. \]
