---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-003-22-su3-algebra-version-of-octonion-algebra
section_title: "SU(3)-algebra version of octonion algebra"
section_number: 2.2
pages: 7-9
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
One can combine the 3-linear form $v$ on $E$ with the Hilbertian scalar product to define an antibilinear antisymmetric product $(Z_1,Z_2)\mapsto Z_1\vartimes Z_2$ on $E$ by $$v(Z_1,Z_2,Z_3)=\langle Z_1\vartimes  Z_2,Z_3\rangle
\label{vectp}$$ for any $Z_1,Z_2,Z_3\in E$. In the $SU(3)$-basis $(e_1,e_2,e_3)$ and the corresponding identification of $E$ with $\mathbb C^3$ this product reads $$(Z_1\vartimes  Z_2)^k=\varepsilon_{k\ell m} \bar Z^\ell_1 \bar Z^m_2
\label{prv}$$ for $k\in \{1,2,3\}$. Notice that this product on $E$ is nonassociative and is invariant by the action of $SU(3)$. Thus one has a product $$\vartimes:E\times E\rightarrow E, \ \ (Z,Z')\mapsto Z\vartimes  Z'$$ and the scalar product $$\langle, \rangle:E\times E \rightarrow \mathbb C,(Z,Z')\mapsto \langle Z,Z'\rangle$$ which are invariant by the action of $SU(3)$ on $E$. This representation of $SU(3)$ is the fundamental representation and $SU(3)$ is exactly the subgroup of the complex linear group of $E$ which preserves these two products; $\mathbb C$ being equipped with the trivial representation of $SU(3)$ $$(g,z)\mapsto gz=z$$ for $g\in SU(3)$, $z\in \mathbb C$. It is therefore natural to combine these products into an $SU(3)$-invariant product $$((z,Z),(z',Z'))\mapsto (z,Z)(z',Z')$$ on $\mathbb C\oplus E$ in such a way that $$(0,Z)(0,Z')=(\alpha\langle Z,Z'\rangle,\beta Z\vartimes Z')
\label{p0}$$ for some $\alpha,\beta\in \mathbb C$ and that $\mbox{\rm 1\hspace {-.6em} l}=(1,0)$ is a unit, i.e. that one has in particular $$(1,0)(0,Z)=(0,Z)(1,0)=(0,Z)$$ for any $Z\in E$ with of course $(1,0)(1,0)=(1,0)$ and more generally $$(z,0)(z',0)=(zz',0)$$ for $z,z'\in \mathbb C$.\
If $\mathbb C\oplus E$ is endowed with its natural structure of 4-dimensional Hilbert space (Hilbertian direct sum), one has $$\parallel (0,Z)(0,Z')\parallel^2=(\vert\alpha\vert^2-\vert\beta\vert^2)\vert\langle Z,Z'\rangle\vert^2 + \vert \beta\vert^2\parallel Z\parallel^2\parallel Z'\parallel^2$$ so that one has $$\parallel (0,Z)(0,Z')\parallel^2=\parallel (0,Z)\parallel^2 \parallel(0,Z')\parallel^2$$ by chosing $$\vert \alpha\vert^2=\vert \beta\vert^2=1
\label{nor}$$ as normalization. One has also of course $$\parallel (z,0)(z',0)\parallel^2=\parallel (z,0)\parallel^2\parallel(z',0)\parallel^2$$ so it is natural to require $$\parallel (z,Z)(z',Z')\parallel^2=\parallel(z,Z)\parallel^2\parallel (z',Z')\parallel^2$$ with $\parallel(z,Z)\parallel^2=\vert z\vert^2+\parallel Z\parallel^2$ and the real bilinearity of the product.\
A solution is given by $$(z,Z)(z',Z')=(zz'-\langle Z,Z'\rangle,\bar zZ'+z'Z+iZ\vartimes Z')
\label{proc}$$ This product is probably essentially unique up to irrelevant normalizations. Setting $$\overline{(z,Z)}=(\bar z, -Z) 
\label{cjc}$$ one obtains in particular $$\overline{(z,Z)} (z,Z)=(z,Z)\overline{(z,Z)}=(\vert z\vert^2+\parallel Z\parallel^2)(1,0)$$ i.e. $$\overline{(z,Z)}(z,Z)=(z,Z)\overline{(z,Z)}=\parallel (z,Z)\parallel^2 \mbox{\rm 1\hspace {-.6em} l}
\label{nj}$$ which implies that as a real 8-dimensional algebra for the product ([\[proc\]](#proc){reference-type="ref" reference="proc"}),$A=\mathbb C\mbox{\rm 1\hspace {-.6em} l}\oplus E$ is a normed division algebra which is (necessarily) isomorphic to the algebra $\mathbb O$ of octonions. The group $SU(3)$ is the group of automorphisms of this algebra which preserves the structure of 4-dimensional complex vector space of $\mathbb C\oplus E$ or, equivalently, the group of all complex automorphisms of $\mathbb C\oplus E$ which preserve the product given by ([\[proc\]](#proc){reference-type="ref" reference="proc"}).
