---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-014-hochschild-homology
section_title: "Hochschild homology."
section_number: null
pages: 18-18
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
Now we define $\mathop{\mathrm{HH}}_\bullet(X)$ the Hochschild *homology* of a space $X$ as follows: $$\mathop{\mathrm{HH}}_\bullet(X):=\mathop{\mathrm{{2\mbox{-}Hom}}}_{\mathscr{V}\textsf{ar}}^\bullet(\Sigma_X^{-1},\mathsf {Id}_X)$$ or, in more concrete terms, $$\mathop{\mathrm{HH}}_\bullet(X) = \mathop{\mathrm{Ext}}_{X\times X}^{-\bullet}(\Sigma^{-1}_X,{\mathscr O}_\Delta).$$ Thus an element $w\in \mathop{\mathrm{HH}}_\bullet(X)$ will be denoted $$\raisebox{-.45\height}{},$$ where again the shifts are understood.

It is worth taking a moment to compare this with other definitions of Hochschild homology, such as that of Weibel [@Weibel]. He defines the Hochschild homology of a space $X$ as $\mathsf H^\bullet(X,\Delta^*{\mathscr O}_\Delta)$, where as usual by $\Delta^*$ we mean the left-derived functor. This cohomology group is naturally identified with the hom-set $\mathop{\mathrm{Hom}}^\bullet_{X}({\mathscr O}_X,\Delta^*{\mathscr O}_\Delta)$ which is isomorphic to $\mathop{\mathrm{Hom}}^\bullet_{X\times
  X}(\Delta_!{\mathscr O}_X,{\mathscr O}_\Delta)$ where $\Delta_!$ is the left-adjoint of $\Delta^*$. Direct calculation shows that $\Delta_!{\mathscr O}_X\cong
\Sigma_X^{-1}$ and so our definition is recovered. Another feasible definition of Hochschild homology is $\mathsf H^\bullet(X\times
X,{\mathscr O}_\Delta\otimes {\mathscr O}_\Delta)$, and this again is equivalent to our definition as there is the isomorphism $\Sigma_X^{-1}\cong
{\mathscr O}_\Delta^{\scriptscriptstyle\vee}$.
