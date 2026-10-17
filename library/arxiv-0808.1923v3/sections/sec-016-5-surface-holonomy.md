---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-016-5-surface-holonomy
section_title: "Surface Holonomy"
section_number: 5
pages: 46-46
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
Surface Holonomy
From the viewpoint of a transport 2-functor, parallel transport and holonomy are basically evaluation
on paths or bigons. Let tra : P2(M)
/ T be a transport 2-functor with BG-structure on M. Its
ﬁbres over points x, y ∈M are objects tra(x) and tra(y) in T , and we say that its parallel transport
along a path γ : x
/ y is given by the 1-morphism
tra(γ) : tra(x)
/ tra(y)
in T , and its parallel transport along a bigon Σ : γ
+3 γ′ is given by the 2-morphism
tra(Σ) : tra(γ)
+3 tra(γ′)
in T . The rules how parallel transport behaves under the composition of paths and bigons are precisely
the axioms of the 2-functor tra; see [SW, Deﬁnition A.5]. We give some examples. If γ1 : x
/ y and
γ2 : y
/ z are composable paths, the separate parallel transports along the two paths are related to
the one along their composition by the compositor
cγ1,γ2 : tra(γ2) ◦tra(γ1)
+3 tra(γ2 ◦γ1)
of the 2-functor tra. If idx is the constant path at x, the parallel transport along idx is related to the
identity at the ﬁbre tra(x) by the unitor
ux : tra(idx)
+3 idtra(x).
The parallel transports along vertically composable bigons Σ : γ1
+3 γ2 and Σ′ : γ2
+3 γ3 obey
tra(Σ′ • Σ) = tra(Σ′) • tra(Σ).
In the following we focus on certain bigons that parameterize surfaces; the parallel transport along
these bigons will be called the holonomy of the transport 2-functor tra.
