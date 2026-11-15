---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-061-121-nested-hilbert-scheme-definitions-and-notati
section_title: "Nested Hilbert scheme: definitions and notations"
section_number: 12.1
pages: 67-67
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.978
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: NHilb defs label="ssec: NHilb defs"} Direct definition of the scheme $\Hilb_{1,n}$ is the moduli space of the sequences of the ideals $I_1\subset\dots\subset I_n\subset \CC[x,y]$ such that $\dim \CC[x,y]/I_k=k$. We are also interested in the subvariety $\Hilb_{1,n}^L$ which consists of the sequence like above with extra condition $\supp(I_{k-1}/I_k)$ is a point on the line $L=\{ y=0\}$.

We can also think of a point on $\Hilb_{1,n}$ as quotient sequence $$\CC[x,y]/I_n\to\CC[x,y]/I_{n-1}\to\dots\to \CC[x,y]/I_1.$$ Let us use notation $V_k=\CC[x,y]/I_k$. If we choose a basis $\{v_i\}_{i=1,\dots,n}$ of $V_n$ such that $\langle v_1,\dots,v_k\rangle=V_k$ then the operators of multiplication by $x$ and $y$ become upper triangular in this basis. Let us denote these operators by $X$, $Y$. Let us also notice that the fact that $V_k$ are obtained as a quotient of $\CC[x,y]$ implies that there is a special vector in $u\in V_n$ which is the image of $1\in \CC[x,y]$. Thus on the level of points we obtained identification of $\Hilb_{1,n}$ with the quotient of the variety $$\SymbolPrint{ \mathcal{CV}^{st}}_{\frb\times\frb}=\{(X,Y)\in \frb| [X,Y]=0 \mbox{ and exists } u \mbox{ such that } \CC[X,Y] u=V\}$$ by the group $B$. Respectively, to obtain a model for $\Hilb_{1,n}^L$ one need to impose the condition $Y\in \frn$

The tricky part of the previous description is the fact that we take quotient by the group $B$ which is not a reductive group. Thus to reveal the scheme theoretic structure of the quotient $\mathcal{CV}^{st}_{\frb\times \frb}/B$ one could consider slightly different model for $\Hilb_{1,n}$ which we describe below. Let us define $\tilde{C}\subset \Fl\times \gl_n\times \gl_n$ which consists of the triples $(V_{\bullet},X,Y)$ satisfying the following conditions: $$X V_i\subset V_i,\quad YV_i\subset V_i, \quad [X,Y]=0.$$

There is a natural action of $GL(n)$ on $\tilde{C}$ and analogously to the argument in [@Nak] one can show that the semi-stable locus $\tilde{C}^{ss}$ of the action is exactly the locus where there is a vector $u$ such that $\CC[X,Y]u=V_n$. Thus on the set theoretic level we established the isomorphism between $\mathcal{CV}^{st}_{\frb\times\frb}/B$ and $\tilde{C}^{ss}/GL_n$. Lastly, let us notice that the quotient $\tilde{C}^{ss}/GL_n$ has a natural scheme structure due to GIT theory [@N].
