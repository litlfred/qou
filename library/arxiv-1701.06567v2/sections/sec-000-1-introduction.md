---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-6
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.995
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Can we hear the shape of a drum? Much like harmonics of a musical instrument, spectra of quantum systems contain wealth of useful information. Of particular interest are supersymmetric or the so-called BPS states which, depending on the problem at hand, can manifest themselves either as minimal surfaces, or solutions to partial differential equations, or other "extremal" objects. Thus, a spectrum of BPS states in Calabi-Yau compactifications can be used to reconstruct the geometry of the Calabi-Yau space itself and, as we explain in this paper, spectra of BPS states play a similar role in low-dimensional topology.

The old approach to constructing numerical invariants of 3- and 4-manifolds, as well as the corresponding homological invariants of 3-manifolds, is based on gauge theory. The famous examples are Donaldson-Witten and Seiberg-Witten (SW) invariants of 4- and 3-manifolds, and corresponding instanton and monopole [@kronheimer2007monopoles] Floer homologies of 3-manifolds. All of them were extensively studied in mathematical literature and have appropriate rigorous definitions that go back to the previous century. The numerical invariants are realized in terms of counting solutions to certain partial differential equations, while the homological invariants build on the ideas of Andreas Floer [@MR956166]. In particular, Seiberg-Witten invariants of 4-manifolds had great success distinguishing some homeomorphic but non-diffeomorphic 4-manifolds. And, in the world of 3-manifolds, the so-called Heegaard Floer homology constructed by Ozsvath and Szabo [@ozsvath2004holomorphic] gives a much simpler and non-gauge theoretic definition of a homological invariant, which is believed to be equivalent to the monopole Floer homology.

A seemingly different class of 3-manifold invariants, the so-called Witten-Reshetikhin-Turaev (WRT) invariants [@Witten:1988hf; @MR1091619], comes from a different type of TQFT, which sometimes is called "of Schwarz type" to distinguish it from the TQFTs "of cohomological type" mentioned in the previous paragraph [@Birmingham:1991ty]. At the turn of the century, however, the distinction between the two types started to blur and the ideas of the present paper suggest it may even go away completely in the future. In fact, the first hints for this go back to the early work [@Rozansky:1992td; @Chang:1991df; @Rozansky:1992zt; @meng1996sw] that relates Seiberg-Witten theory in three dimensions to Chern-Simons theory with $U(1|1)$ super gauge group. The latter provides a much simpler invariant compared to the usual Chern-Simons theory, say, with $SU(2)$ gauge group, due to cancelations between bosonic and fermionic contributions. Therefore, if one can find a 4d TQFT that categorifies $SU(2)$ Chern-Simons theory in 3d, similar to how 4d SW theory categorifies 3d SW theory, it would help a great deal with the classification problem of smooth 4-manifolds. The first step in constructing such categorification is, of course, to find a homological invariant of 3-manifolds whose (equivariant) Euler characteristic gives the WRT invariant.

The existence of such 4d TQFT was envisioned by Crane and Frenkel [@MR1295461] more than 20 years ago, and the first evidence came with the advent of knot homology [@khovanov1999categorification; @khovanov2008matrix; @MR2901970] which categorifies WRT invariants of knots and links (realized by Wilson lines in CS theory) in $S^3$, also known as the colored Jones polynomial. The physical understanding of a homological approach to HOMFLY polynomials was independently initiated in the physics literature in [@Ooguri:1999bv], which later led to the physical interpretation of Khovanov-Rozansky homology as certain BPS Hilbert spaces [@Gukov:2004hz; @Gukov:2007ck; @Witten:2011zz; @Aganagic:2011sg] (see *e.g.* [@Chun:2015gda; @Nawata:2015wya] for an overview and an extensive list of references).

The physical construction suggests that there should be a homological invariant that categorifies (in a certain sense) the WRT invariant of general 3-manifolds with knots inside. Namely, such homological invariant can be understood as the BPS sector of the Hilbert space of the 6d ${\mathcal N}=(2,0)$ theory (that is a theory describing dynamics of coincident M5-branes in M-theory) on $M_3\times D^2\times {\mathbb R}$ with a certain supersymmetry preserving background along $M_3\times D^2$. Equivalently, if one first reduces the 6d theory on $M_3$, it can be understood as the BPS Hilbert space of the effective 3d ${\mathcal N}=2$ theory $T[M_3]$ on $D^2\times {\mathbb R}$. On the other hand, if one first compactifies on $D^2$, one does not get an ordinary 4d gauge theory on $M_3\times {\mathbb R}$ like 4d SW gauge theory[^1]: $$\begin{aligned}
\begin{array}{ccccc}
\; & \;\text{6d $(2,0)$ theory} &\text{on}  &\text{${\mathbb R}\times D^2\times M_3$}  \; & \; \\
\; & \swarrow \qquad\qquad\qquad& \; &\qquad\qquad\qquad \searrow & \; \\
\text{space of BPS states ${\mathcal H}_{\text{BPS}}$  } & \; & \; & \; & \text{Hilbert space ${\mathcal H}_{M_3}$ of } \\
\text{of 3d ${\mathcal N}=2$ theory $T[M_3]$} & \; & \; & \; & \text{4d ``Crane-Frenkel TQFT''}\\
\text{on $D^2$} & \; & \; & \; & \text{on $M_3$}
\end{array}
\label{CatGeom0}
\end{aligned}$$

There is another natural SUSY-preserving background on which one can quantize $T[M_3]$. Since the IR physics of $T[M_3]$ is governed by a non-trivial 3d ${\mathcal N}=2$ SCFT, one can consider its radial quantization and study its Hilbert space on $S^2\times {\mathbb R}$. This should provide us with another non-trivial homological invariant of $M_3$ which should have roughly the same level of complexity as the BPS Hilbert space on $D^2\times {\mathbb R}$ which categorifies the WRT invariant, but with several advantages due to the presence of operator-state correspondence and no need to specify a boundary condition at $\partial D^2=S^1$.

The set of boundary conditions that one can put at $\partial D^2\cong S^1$ in the path integral can be understood as follows. Let us represent $D^2$ as an elongated cigar, which asymptoically looks like $S^1\times {\mathbb R}$. After compactification of the stack of fivebranes on $S^1$ we obtain 5d maximally supersymmetric gauge theory. The supersymmetric vacua of such theory on $M_3\times {\mathbb R}$ (where ${\mathbb R}$ is the original time direction) are given by flat connections[^2] on $M_3$. The number of such supersymetric vacua is the same as the number of boundary conditions (*cf.* [@Cecotti:1991me; @Witten:2011zz; @Pasquetti:2011fj; @Beem:2012mb; @Cecotti:2013mba]). As we will see later, the subset of such boundary conditions that corresponds to abelian flat connections plays an important role; for convenience, here we summarize various clues that all point to a special role of abelian flat connections:

-   charges of BPS states in the target space theory [@Ooguri:1999bv];

-   relation between homological invariants of different rank [@Gukov:2016gkn];

-   resurgent analysis of complex Chern-Simons theory [@Gukov:2016njj];

-   similar analysis of 3d ${\mathcal N}=2$ theories (section [\[sec:summary\]](#sec:summary){reference-type="ref" reference="sec:summary"} below);

-   Langlands duality for flat connections on 3-manifolds (section [\[sec:Langlands\]](#sec:Langlands){reference-type="ref" reference="sec:Langlands"}).

Moreover, in this paper we give many examples of $q$-series invariants for various 3-manifolds which exhibit integrality, and in many cases we also write the corresponding homological invariants. All of these invariants are labeled by (connected components of) abelian flat connections; we do not have any such example associated with a non-abelian flat connection.

In this paper we study the relation between such homological invariants and their decategorified counterparts --- superconformal indices. The structure described above, of course, will also manifest itself at the level of partition functions, *i.e.* indices, once we compactify the time on $S^1$. For some of the examples in this paper for there are no cancellations among states in computing the refined index. In those cases, the homological invariants are faithfully captured by the refined index computation.

The organization of the paper is as follows. In Section 2 we review some results of [@Gukov:2016gkn] and summarize general conjectures about homological invariants of closed 3-manifolds mentioned here and their decategorified versions. In Section 3 we consider various examples for which we explicitly verify these conjectures. In Section 4 we extend it to the case of 3-manifolds with knots. Note, the main part of Section 4 is written in jargonish shorthand, using the concepts and notations introduced earlier. Various details and generalizations of this work can be found in the appendices. Thus, Appendix [\[app:Zq-from-WRT\]](#app:Zq-from-WRT){reference-type="ref" reference="app:Zq-from-WRT"} explains how the WRT invariants of general negative definite plumbed 3-manifolds can be analytically continued away from roots of unity to produce power series in $q$ with integer powers and integer coefficients, required for categorification. In Appendix [\[app:cabling\]](#app:cabling){reference-type="ref" reference="app:cabling"}, we compare the ordinary Khovanov homology of the $n$-th cabling of the unknot in a 3-sphere to the refined partition function of 3d ${\mathcal N}=2$ theory $T[S^3]$ in the presence of line operators, *cf.* Figure [1](#fig:impurity){reference-type="ref" reference="fig:impurity"}. Finally, in Appendix [\[sec:TV\]](#sec:TV){reference-type="ref" reference="sec:TV"} we explain how categorification of the index of $T[M_3]$ relates to categorification of the Turaev-Viro invariants.

![The space of BPS states in 3d ${\mathcal N}=2$ theory on ${\mathbb R}\times D^2$ with an impurity, relevant to the physical realization of Heegaard Floer homology $HF(M_3)$, monopole Floer homology $HM(M_3)$, as well as categorification of WRT invariants of 3-manifolds with knots.](impurity){#fig:impurity width="4.0in"}

[^1]: Roughly speaking, the effective 4d theory is an infinite KK-like tower on 4d gauge theories. However one needs to appropriately sum it up. The decategorified counterpart of such summation was studied in [@Gukov:2016njj].

[^2]: The choice of such flat connections should not be confused with the choice of flat connections in CS theory on $M_3$. As will be explained later in detail they are related by S-transform.
