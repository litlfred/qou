---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-032-56-unbalanced-realizations
section_title: "Unbalanced realizations"
section_number: 5.6
pages: 55-57
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.98
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{nonbalanced}


Now we discuss the diagrammatic alterations which must be made to accommodate the case of non-balanced realizations. This was discussed for dihedral groups in the appendix to
\cite{EDihedral}, where two separate diagrammatic conventions are proposed to deal with the new bookkeeping required. We follow the second suggested convention from that appendix.

Fix a dihedral parabolic subgroup with $m=m_{st} < \infty$. Relation \eqref{dot2m} implies that there is a close connection between $2m$-valent vertices and two-colored Jones-Wenzl
projectors. However, this begs the question: which Jones-Wenzl projector? After all, the left-blue-aligned Jones-Wenzl projector is not equal to the rotation of the left-red-aligned one. A
careful examination of \eqref{dot2m} and \eqref{twocoloridemp} shows that different choices of Jones-Wenzl projector must be made, depending on the location of the dot and the orientation
of the $2m$-valent vertex.

If some rescaling of \eqref{dot2m} is to hold, for any positioning of the dot and the $2m$-valent vertex, then the Jones-Wenzl projector must satisfy the death by pitchfork property
\eqref{JWpitch}. In particular, $JW_{m-1}$ must be negligible, and must have some rotational eigenvalue. This is not possible when the realization is even-unbalanced (see \cite{EDihedral}
for more details). While one may be able to design a diagrammatic calculus for even-unbalanced realizations, we will not attempt to do so. When $m$ is even and $[m-1]=1$, all the two-color
relations above hold as stated.

The $2m$-valent vertex is supposed to correspond, under the functor $\FC$, to some non-zero morphism between bimodules, living in a one-dimensional space of morphisms. Let $\un{w}_{(s)}$
denote the reduced expression $\ldots tsts$ of length $m$ ending in $s$, and let $\un{w}_{(t)}$ denote the reduced expression $\ldots stst$ of length $m$ ending in $t$. There is a unique
bimodule map $f_{(s)} \co BS(\un{w}_{(t)}) \to BS(\un{w}_{(s)})$ which sends the 1-tensor to the 1-tensor, and a unique map $f_{(t)} \co BS(\un{w}_{(s)}) \to BS(\un{w}_{(t)})$ which does
the same. However, when the realization is not balanced, these maps are not rotations of each other (by one strand), and this is the underlying issue. However, these maps are individually
invariant under color-preserving rotations (just like $JW_{m-1}$, even in the odd-unbalanced case), so we may draw each unambiguously as some kind of $2m$-valent vertex. We label the
vertices $(s)$ or $(t)$ to distinguish the two. (We only draw the case when $m$ is odd, but nothing prevents drawing the even case too.)

\igc{1}{funky2m}

The purple strand is meant to encode the appropriate sequence of alternating red and blue strands. To reiterate, when the blue-centered $2m$-valent vertex is oriented such that its
upper-right strand is blue (as in the picture above), then it corresponds under $\FC$ to a morphism which preserves the 1-tensor. When the blue-centered $2m$-valent vertex is oriented such
that its upper-right strand is red, one differs from this map by an invertible scalar $\l$. In \cite{EDihedral}, this scalar $\l = [m-1]_y$ is discussed at additional length. Therefore,
one has the rotational relation: \begin{equation} {
\labellist
\small\hair 2pt
 \pinlabel {$\l$} [ ] at 65 24
 \pinlabel {$\l^{-1}$} [ ] at 194 23
\endlabellist
\centering
\ig{1}{funky2mrotate}
} \end{equation}

When we place a dot on a $2m$-valent vertex, we obtain a relation similar to \eqref{dot2m}. \begin{equation} {
\labellist
\small\hair 2pt
 \pinlabel {$JW_{m-1}$} [ ] at 92 93
 \pinlabel {$JW_{m-1}$} [ ] at 236 93
 \pinlabel {$JW_{m-1}$} [ ] at 92 20
 \pinlabel {$JW_{m-1}$} [ ] at 236 20
\endlabellist
\centering
\ig{1}{dot2malternate}
} \end{equation} In each case, the version of the
Jones-Wenzl projector used is the one whose coefficient of the identity is $1$, when color-aligned as above. By rotating these pictures, one knows how to place a dot on any strand in
either $2m$-valent vertex. To check that these relations make sense, observe that both sides send the 1-tensor to the 1-tensor.

To give the correct versions of \eqref{assoc2} and \eqref{twocoloridemp}, one should label the $2m$-valent vertices in such a way that both sides preserve the 1-tensor. \begin{equation}
\ig{1}{twocolorassocalternate} \end{equation} \begin{equation} \ig{1}{twocoloridempalternate} \end{equation} There are additional, color-switched versions of each of these relations.

Finally, to give the correct version of the three-color relations, one should again ensure that both sides preserve the 1-tensor. Here is the $A_3$ relation. \begin{equation}
\ig{1}{A3altalt} \end{equation}

Note that, when working with these diagrams, there is a scalar ambiguity that appears when defining a rex move, determined by the choice of central color on each $2m$-valent vertex. Our
convention is that one will always choose a coloring so that the 1-tensor is preserved by the rex move.

For the remainder of this paper, we will work solely with the balanced case, and thus will not need the extra confusion of labeled $2m$-valent vertices. In the rest of the paper, it is
roughly the case that diagrams are only important ``up to scalar." That is, we will be asking whether certain morphisms span or are linearly independent, and these concepts are not
affected by rescaling. It should not be hard to convince oneself that the remainder of this paper applies equally well to the odd-unbalanced case. 

 


































\part{Light leaves morphisms and proofs}

\label{pt:proofs}
