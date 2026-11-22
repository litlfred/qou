---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-005-the-serre-functor-on-dx
section_title: "The Serre functor on D(X)."
section_number: null
pages: 10-11
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.978
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#subsec:Serretrace label="subsec:Serretrace"} If $X$ is a space then we consider the functor $$\mathsf{S}\colon\mathbf{D}(X)\to \mathbf{D}(X);\qquad {\mathscr E}\mapsto \omega_X[\dim
X]\otimes {\mathscr E},$$ where $\omega_X$ is the canonical line bundle of $X$. Serre duality then gives natural, bifunctorial isomorphisms $$\eta_{{\mathscr E},{\mathscr F}}\colon\mathop{\mathrm{Hom}}_{\mathbf{D}(X)}({\mathscr E}, {\mathscr F}) \stackrel{\sim}{\longrightarrow}
\mathop{\mathrm{Hom}}_{\mathbf{D}(X)}({\mathscr F}, \mathsf{S}{\mathscr E})^{\scriptscriptstyle\vee}$$ for any objects ${\mathscr E},{\mathscr F}\in \mathbf{D}(X)$, where ${-}^{\scriptscriptstyle\vee}$ denotes the dual vector space.

A functor such as $\mathsf{S}$, together with isomorphisms as above, was called a *Serre functor* by Bondal and Kapranov [@BonKapSerre] (see also [@ReiVan]). From this data, for any object ${\mathscr E}\in\mathbf{D}(X)$, define the *Serre trace* as follows: $$\mathop{\mathrm{Tr}}\colon\mathop{\mathrm{Hom}}({\mathscr E}, \mathsf{S}{\mathscr E}) \rightarrow\textsf{k};\qquad \mathop{\mathrm{Tr}}(\alpha) := \eta_{{\mathscr E},{\mathscr E}}(\mathsf {Id}_{\mathscr E})(\alpha).$$ Note that from this trace we can recover $\eta_{{\mathscr E},{\mathscr F}}$ because $$\eta_{{\mathscr E},{\mathscr F}}(\alpha)(\beta)=\mathop{\mathrm{Tr}}(\beta\circ\alpha).$$ We also have the commutativity identity $$\mathop{\mathrm{Tr}}(\beta\circ \alpha) = \mathop{\mathrm{Tr}}(\mathsf{S}\alpha \circ \beta).$$ Yet another way to encode this data is as a perfect pairing, the *Serre pairing*: $${\ensuremath{\left\langle {-},\, {-}\right\rangle_{\rm S}}}\colon \mathop{\mathrm{Hom}}({\mathscr E},{\mathscr F})\otimes \mathop{\mathrm{Hom}}({\mathscr F},\mathsf{S}{\mathscr E})\to
\textsf{k}; \qquad {\ensuremath{\left\langle \alpha,\, \beta\right\rangle_{\rm S}}}:=\mathop{\mathrm{Tr}}(\beta\circ \alpha).$$
