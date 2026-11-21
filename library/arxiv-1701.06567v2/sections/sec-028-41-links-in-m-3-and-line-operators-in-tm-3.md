---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-028-41-links-in-m-3-and-line-operators-in-tm-3
section_title: "Links in $M_3$ and line operators in $T[M_3]$"
section_number: 4.1
pages: 56-60
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.997
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:knots label="sec:knots"}

Consider a knot $K$ in $M_3$ colored by a representation ${\mathcal R}$ of $G$. As described above, it corresponds to a certain half-BPS line operator $\Gamma_{K,{\mathcal R}}$ in $T[M_3;G]$: $$(K,{\mathcal R})\;\longmapsto \; \Gamma_{K,{\mathcal R}}\;\in\;{\mathcal C}.
    \label{Knots-LineOps}$$ where ${\mathcal C}$ is the category of BPS line operators in ${\mathcal N}=2$ SCFT $T[M_3,G]$. The homological invariant for a combined system of a knot and a 3-manifold is then given by the BPS Hilbert space of $T[M_3]$ on the disk $D^2$ with $\Gamma_{K,{\mathcal R}}$ inserted at $O$, the center of the disk (see Figure [\[fig:impurity\]](#fig:impurity){reference-type="ref" reference="fig:impurity"}): $${\mathcal H}_a[M_3;K,{\mathcal R}]\equiv {\mathcal H}_{T[M_3]}(D^2,\Gamma_{K,{\mathcal R}};a),\qquad a\in (\text{Tor}\,H_1(M_3,{\mathbb Z}))^N/S_N$$ where $a$ denotes the choice of boundary condition, the same as in the case without a knot. It has the same gradings as before, namely the $q$-grading $i$ and the homological (R-charge) grading $j$: $${\mathcal H}_a[M_3;K,{\mathcal R}]=\bigoplus_{i\in \Delta_a+{\mathbb Z},\,j\in{\mathbb Z}}{\mathcal H}_a^{i,j}[M_3;K,{\mathcal R}]$$ And, as before, the graded Euler characteristic gives the partition function on $D^2\times S^1$: $$\widehat{Z}_a(q;\Gamma_{K,{\mathcal R}})\equiv Z_{T[M_3]}(D^2\times S^1,\Gamma_{K,{\mathcal R}};a)=
    \sum_{i,j}(-1)^jq^i{\mathcal H}_a^{i,j}[M_3;K,{\mathcal R}]$$ now, in 3d ${\mathcal N}=2$ theory $T[M_3]$ with an extra 1d "impurity" $\Gamma_{K,{\mathcal R}}$ supported on $O\times S^1$. The analogue of the Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} is then the following:

::: conj
The WRT invariant of $M_3$ with a knot $K$ colored by representation ${\mathcal R}$ can be decomposed into the following form: $$Z_{SU(2)_k}[M_3;K,{\mathcal R}]=(i\sqrt{2k})^{b_1(M_3)-1}\sum_{a,b\;\in \;\atop{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}e^{2\pi ik{\ell k}(a,a)}\,S_{ab}
    \, \widehat{Z}_b(q;\Gamma_{K,{\mathcal R}})|_{q\rightarrow e^{\frac{2\pi i }{k}}}
    \label{WRT-knot-decomposition}$$ where $$\widehat{Z}_b(q;\Gamma_{K,{\mathcal R}}) \in \, 2^{-c} q^{\Delta_b} {\mathbb Z}[[q]]\qquad \Delta_b\in {\mathbb Q},\qquad c\in{\mathbb Z}_+
    \label{Block-knot-qSeries}$$ convergent in $|q|<1$ and $S_{ab}$ is the same as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} []{#Conjecture3 label="Conjecture3"}
:::

For certain 3-manifolds with an extra symmetry, preserved by the knot $K$, we have an extra grading whose value we denote by $\ell$: $${\mathcal H}_a[M_3;K,{\mathcal R}]=\bigoplus_{i\in \Delta_a+{\mathbb Z},\,j,\ell\in{\mathbb Z}}{\mathcal H}_a^{i,j;\ell}[M_3;K,{\mathcal R}]$$ In practice, to compute these homological invariants, one needs a convenient ultra-violet (UV) description of the fivebrane setup [\[CatGeom2\]](#CatGeom2){reference-type="eqref" reference="CatGeom2"} or, better yet, of the IR superconformal theory $T[M_3]$. In general, the brane system [\[CatGeom2\]](#CatGeom2){reference-type="eqref" reference="CatGeom2"} and the 3d theory $T[M_3]$ may admit many such UV descriptions, in various duality frames, all of which flow to the same IR physics and produce the same homological invariants (space of BPS states).

In a given UV gauge theory description of $T[M_3]$, the objects in the tensor category ${\mathcal C}$ of BPS line operators can be understood as vector spaces --- the "Hilbert spaces of ${\mathcal N}=2$ quantum mechanics on the line, coupled to the bulk gauge theory". The most familiar line operators are Wilson operators $W_\lambda$, labeled by a representation $\lambda$ of the UV gauge group[^1] ${\mathcal G}$ (which, in general, has little to do with $G$). The corresponding object of the category ${\mathcal C}$ is, tautologically, the representation $\lambda$. The Wilson lines are expected to form a complete basis of line operators in the IR theory, in the sense that any line operator (not necessarily associate to a knot) should have the following decomposition: $$\begin{aligned}

\overbrace{\rule{1.0cm}{0pt}}^{\text{IR}} &  & ~~~\overbrace{\rule{2.5cm}{0pt}}^{\text{UV}} \label{Line-UV} \\
\Gamma_{K,{\mathcal R}} & ~=~ & \bigoplus_{\lambda,i,j,\ell} W_\lambda\otimes {\mathcal H}_{K,{\mathcal R}}^{\lambda;i,j;\ell} \,. \nonumber
\end{aligned}$$ The reason is very simple --- one can always decompose the "defect Hilbert space" into representations of ${\mathcal G}$, with the multiplicity space ${\mathcal H}_{\Gamma}^{\lambda}$ associated with the representation $\lambda$. The symmetry ${\mathcal G}$ plays the role of the flavor symmetry in QM on the line, which couples to 3d theory $T[M_3]$ by gauging ${\mathcal G}$ in the bulk. If $\Gamma$ is a generic physical line operator (*cf.* superposition of physical line operators), the corresponding multiplicity spaces ${\mathcal H}_{\Gamma}^{\lambda}$ are honest vector space that are at least doubly-graded, with the $(i,j)$-grading coming from $U(1)_q\times U(1)_R$ symmetry of the brane system [\[CatGeom2\]](#CatGeom2){reference-type="eqref" reference="CatGeom2"}. When the flavor symmetry $U(1)_{\beta}$ is a symmetry of both $T[M_3]$ and $\Gamma$, the third $\ell$-grading is also present.

As a trivial example, consider a line defect given by a quantum mechanics that is completely decoupled from the bulk. Then, $$\Gamma_{\text{QM}} \; = \; W_0\otimes {\mathcal H}_{\text{QM}} \,,
\label{babyexmpl}$$ where ${\mathcal H}_{\text{QM}}$ is the Hilbert space of the quantum mechanics and $W_0$ is the trivial Wilson loop. So, we see that [\[Line-UV\]](#Line-UV){reference-type="eqref" reference="Line-UV"} has a chance of being correct, even if there are infinitely many possibilities of engineering defects via 1d-3d coupled systems. In this sense, $\lambda$ is analogous to the label "$a$" of the homological blocks, which reduces infinitely many possible boundary conditions to a finite set. In fact, this isn't just an analogy --- it comes from the equivalence of two categories $$\label{C=CB}
{\mathcal C}\cong {\mathcal C}_B.$$ Namely, a line operator can be viewed as the interface between two boundary conditions, and picking a "reference boundary condition" (*e.g.* the one giving $\widehat{Z}_0$ with zero brane charge) will identify the two categories. This equivalence is a special feature of 3d quantum field theories, which associate categories to $S^1$, with the objects that can be interpreted either as line operators or as boundary conditions at spatial infinity.

At this point, $\lambda$ can still be an arbitrary representation of the UV gauge group ${\mathcal G}$, and one might naively think that ${\mathcal C}$ is $$\label{CUV}
{\mathcal C}_{\text{UV}}=\mathrm{Rep}({\mathcal G}),$$ given by the representation category of ${\mathcal G}$. But in light of the equivalence [\[C=CB\]](#C=CB){reference-type="eqref" reference="C=CB"}, we expect ${\mathcal C}$ to be much smaller, since ${\mathcal C}_B$ is generated by finitely many simple objects (boundary conditions that give homological blocks), as we have seen in all our examples.

Indeed, [\[CUV\]](#CUV){reference-type="eqref" reference="CUV"} is often redundant, due to presence of Chern-Simons couplings in $T[M_3]$. There is a set $\Lambda_{M_3}$ of "integrable representations" of ${\mathcal G}$ giving a complete basis of $W_\lambda$ in $T[M_3;G]$, and every Wilson loop labeled by a non-integrable representation can be decomposed as $$\label{WilsonDec}
W_{\nu}=\bigoplus_{\lambda\in \Lambda_{M_3}\atop i,j,\ell\in{\mathbb Z}}W_{\lambda}\otimes {\mathcal H}_{\nu}^{\lambda;i,j;\ell}.$$ All such relations generate an ideal (in the categorical sense) of ${\mathcal C}_{\text{UV}}$, and ${\mathcal C}$ is given by the quotient $${\mathcal C}={\mathcal C}_{UV}/{\mathcal I}.$$ As a vector space, ${\mathcal C}$ is the same as $\Lambda_{M_3}\otimes{\mathbb C}$, but the algebra structure depends on ${\mathcal I}$ and is determined by the theory $T[M_3]$ in a non-trivial way. Both ${\mathcal C}_{\text{UV}}$ and ${\mathcal I}$ depend on the duality frame (presentation of $M_3$), but it is expected that the quotient category ${\mathcal C}$ is a topological invariant of $M_3$. It describes line operators / boundary conditions in the IR theory, which is what usually meant by $T[M_3]$.

We expect, for arbitrary $M_3$, the independent Wilson loops in the theory $T[M_3;G]$ are labeled by elements in[^2] $$\label{WilsonCharge}
\Lambda_{M_3}=\mathrm{Tor}\,H_1(M_3,\Lambda_{\text{rt}})/W_G,$$ where $\Lambda_{\text{rt}}$ is the root lattice of $\mathfrak{g}$ and $W_G$ is the Weyl group (not to be confused with Wilson line $W_{\lambda}$ in UV description of $T[M_3]$). The argument for this statement parallels our discussion of boundary conditions given by M2-brane charges "$a$", which take values in exactly the same set. And the fundamental Wilson loops are expected to come from knots $K$ wrapping torsion 1-cycles, colored by a representation ${\mathcal R}$ of $G$ (*i.e.* ${\mathcal R}\in \Lambda_{\text{char}}(G)/W_G$).

If $G$ is abelian, then $\Lambda_{M_3}$ is a group and one can introduce an action of line operators on boundary conditions, which we call the *shift* action in what follows. This action is expected because Wilson line operators $W_\lambda,\;\lambda\in \Lambda_{M_3}$, can be engineered using M2-branes[^3] as in [\[CatGeom2\]](#CatGeom2){reference-type="eqref" reference="CatGeom2"}, and the label "$a$" for homological blocks also measures M2-brane charges. In other words, a Wilson loop $W_\lambda$ relates two Hilbert spaces $${\mathcal H}_{T[M_3]}(D^2,W_\lambda;a) \; \sim \; {\mathcal H}_{T[M_3]}(D^2,W_\lambda;a-\lambda).$$ One does not *a priori* know whether this is an isomorphism or not, or how the gradings on the two sides are related. However, in various examples below we observe that, at the level of homological blocks $\widehat{Z}_a(q)$, Wilson loop acts as a simple shift operator, even for $G=SU(2)$ if the Weyl group action is properly taken into account.

As before, our main tools for probing the new homological invariants are SUSY-protected quantities. In particular, using a UV descriptions of $T[M_3]$ and a half-BPS impurity $\Gamma_{K,{\mathcal R}}$, one can compute the partition function of $T[M_3]$ on $D^2\times S^1$ with $\Gamma_{K,{\mathcal R}}$ inserted along $O\times S^1$ as follows: $$\begin{gathered}
\label{BlockKnot}
    \widehat{Z}_a(q,t;\Gamma_{K,{\mathcal R}})\equiv Z_{T[M_3]}(D^2\times S^1,\Gamma_{K,{\mathcal R}};a)=\\ =\int \frac{dz}{2\pi i z}
    \,[\text{same as without $\Gamma_{K,{\mathcal R}}$}] \sum_{\lambda\in \Lambda_{M_3}\atop i,j,\ell \in{\mathbb Z}}\chi_\lambda(z)q^it^\ell(-1)^{j}
    \dim{\mathcal H}_{K,{\mathcal R}}^{\lambda;i,j;\ell}
\end{gathered}$$ where $z$ stands for the gauge fugacities of the UV gauge group ${\mathcal G}$ and $\chi_\lambda$ is the character of the ${\mathcal G}$-representation $\lambda$.

Similarly, we can consider the $S^2 \times S^1$ superconformal index with half-BPS impurities inserted at one (or both) poles of $S^2$. The UV localization formula for the index is modified as follows (when the impurity is at the north pole): $$\begin{gathered}
\label{IndexKnot}
    {\mathcal I}(q,t;\Gamma_{K,{\mathcal R}})\equiv Z_{T[M_3]}(S^2\times S^1;\Gamma_{K,{\mathcal R}})= \\ =\sum_{m}\int \frac{dz}{2\pi i z}
    \,[\text{same as without $\Gamma$}] \sum_{\lambda\in\Lambda_{M_3} \atop i,j,\ell \in {\mathbb Z}}\chi_\lambda(zq^{m/2})q^i t^\ell (-1)^{j}
    \dim{\mathcal H}_{K,{\mathcal R}}^{\lambda;i,j;\ell}.
\end{gathered}$$ As we demonstrate in a variety of examples, it obeys the modified factorization formula $${\mathcal I}(q,t;\Gamma_{K,{\mathcal R}}) \; = \; \sum_a|{\mathcal W}_a| \widehat{Z}_a(q,t;\Gamma_{K,{\mathcal R}})\widehat{Z}_a(q^{-1},t^{-1}) \,.$$ Note, all of the above relations depend only on the IR data, namely on $K$ and its color ${\mathcal R}$, not on the UV description of $\Gamma_{K,{\mathcal R}}$. In particular, note that $\lambda$ is always summed over in these relations, which goes back to the basic relation between IR line operators $\Gamma_{K,{\mathcal R}}$ ("impurities") and their description [\[Line-UV\]](#Line-UV){reference-type="eqref" reference="Line-UV"} in the UV theory via $W_{\lambda}$.

The reader should keep in mind that there are two non-trivial maps (dualities) involved in the study of knots.[^4] First, there is a rather non-trivial map [\[Line-UV\]](#Line-UV){reference-type="eqref" reference="Line-UV"} between line operators in the IR theory $T[M_3]$ and its UV description (or, rather, one of many UV descriptions). This UV/IR map has nothing to do with applications to low-dimensional topology and is a standard phenomenon in quantum field theory. In addition, there is a map between knots and links colored by ${\mathcal R}$ in a TQFT on $M_3$ and half-BPS line operators ("impurities") in the 3d ${\mathcal N}=2$ theory $T[M_3]$. This map is a chapter in the so-called 3d/3d correspondence. The reason one should pay attention to both of these maps is that it is their composition which relates homological invariants of $K \subset M_3$ to concrete calculations in $T[M_3;G]$, $$\boxed{{\text{UV line} \atop \text{operators}~W_{\lambda}}}
\quad \xleftrightarrow[~]{\text{UV/IR map}} \quad
\boxed{{\frac12\text{-BPS impurity} \atop \Gamma_{K,{\mathcal R}} }}
\quad \xleftrightarrow[\text{~}]{\text{3d/3d correspondence}} \quad
\boxed{{\text{link}~K \subset M_3 \atop \text{colored by}~{\mathcal R}}}$$ Because each of these maps can be rather non-trivial, one should not confuse the representation $\lambda$ that labels half-BPS line operators in the UV description with the "color" of $K$. The latter is denoted by ${\mathcal R}$ and, whenever non-trivial, leads to the ${\mathcal R}$-colored link homology [@Gukov:2011ry; @Fuji:2012pm] in our setup [\[CatGeom2\]](#CatGeom2){reference-type="eqref" reference="CatGeom2"}.

So far, the discussion in this section is very general and, as such, may be somewhat abstract. We will now give some very concrete examples for $G=SU(2)$.

[^1]: In general, ${\mathcal G}$ is different from $G$. For a quiver theory, it may be given by a product $\times_i G_i$ over the vertices.

[^2]: So far, we have ignored the difference between $G$ and the Langlands dual group $G^\vee$ because the quantities considered so far are not sensitive to the global structure of the group. However, the spectrum of Wilson loops is sensitive to this difference, and [\[WilsonCharge\]](#WilsonCharge){reference-type="eqref" reference="WilsonCharge"} is stated for the adjoint form $G=G_{\text{ad}}$. If $G$ has a center, one needs to add the representations of $G$ where the center acts non-trivially. Reader interested in this subject may consult [@EVFCBI] where this issue was extensively discussed in a similar brane system.[]{#ft:Global label="ft:Global"}

[^3]: *i.e.* $W_\lambda=\Gamma_{K,{\mathcal R}}$ when torsion homology class of ${\mathcal R}$-cable of $K$ is given by $\lambda\in  \Lambda_{M_3}$

[^4]: This aspect is a surprising exception to the rule that knot homology is easier than 3-manifold homology.
