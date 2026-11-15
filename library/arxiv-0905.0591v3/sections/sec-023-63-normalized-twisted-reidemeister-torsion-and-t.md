---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-023-63-normalized-twisted-reidemeister-torsion-and-t
section_title: "Normalized twisted Reidemeister torsion and the free genus of a knot"
section_number: 6.3
pages: 23-24
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.943
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:normalized}

Let $K\subset S^3$ a knot and let $\gamma:\pi_1(S^3\sm \nu K)\to \mbox{GL}(k,R)$ be a representation with $R$ a Noetherian UFD.
Let $\epsilon=\det(\gamma(\mu))$ where $\mu$ denotes a meridian of $K$.
Kitayama \cite{Kiy08a} introduced an invariant $\tilde{\Delta}_{K,\gamma}\in Q(R(\epsilon^{\frac{1}{2}})[t^{\pm \frac{1}{2}}])$ which is a normalized version of the twisted Reidemeister torsion $\tau(K,\gamma)$, i.e.  $\tau(K,\gamma)$ has no indeterminacy and up to multiplication by an element of the form $\epsilon^r t^{\frac{s}{2}}$ it is a representative of the twisted Reidemeister torsion. (The invariant $\tilde{\Delta}_{K,\gamma}$ should not be confused with the torsion polynomial introduced in Section \ref{section:linkslice}.)

Kitayama \cite[Theorem~6.3]{Kiy08a} studies the invariant $\tilde{\Delta}_{K,\gamma}$ for fibered knots, obtaining a refined version of the fibering obstruction which we stated in Theorem \ref{thm:fibob}. Furthermore \cite[Theorem~5.8]{Kiy08a} proves a duality theorem for $\tilde{\Delta}_{K,\gamma}$, refining  Proposition \ref{prop:dualitytau}.

In the following we say that $S$ is a \emph{free Seifert surface} for $K$ if $\pi_1(S^3\setminus S)$ is a free group.
Note that Seifert's algorithm produces free Seifert surfaces, in particular any knot has a free Seifert surface.
Given $K$ the \emph{free genus} is now defined as
\[ \mbox{free-genus}(K)=\mbox{min}\{ \mbox{genus}(S) \, |\, \mbox{$S$ free Seifert surface for $K$}\}.\]
Clearly we have $\mbox{free-genus}(K)\geq \mbox{genus}(K)$.
In order to state the lower bound on the free genus coming from $\tilde{\Delta}_{K,\gamma}$ we have to make a few more definitions.
Given a Laurent polynomial $p=\sum_{i=k}^l a_it^i\in R[t^{\pm \frac{1}{2}}]$ with $a_k\ne 0, a_l\ne 0$
we write $\mbox{l-deg}(p)=k$ (`lowest degree') and $\mbox{h-deg}(p)=l$ (`highest degree').
Furthermore given $f\in Q(R[t^{\pm \frac{1}{2}}])$ we  define
\[ \mbox{h-deg}(f)=\mbox{h-deg}(p)-\mbox{h-deg}(q)\]
where we pick $p,q\in R[t^{\pm \frac{1}{2}}]$ with $f=\frac{p}{q}$.
Kitayama \cite[Proposition~6.6]{Kiy08a} proved the following theorem:

\begin{theorem}
Given a knot $K\subset S^3$ and a representation $\gamma:\pi_1(S^3\sm \nu K)\to \mbox{GL}(k,R)$  with $R$ a Noetherian UFD
we have
\[ 2k  \mbox{free-genus}(K) \geq 2\,\mbox{h-deg}(\tilde{\Delta}_{K,\gamma})+k.\]


\end{theorem}

Note that if $\mbox{h-deg}(\tilde{\Delta}_{K,\gamma})=-\, \mbox{l-deg}(\tilde{\Delta}_{K,\gamma})$ (which is the case for unitary representations)
then the bound in the theorem is implied by the bound given in Theorem \ref{thm:lowerboundphi}.
It is a very interesting question whether Kitayama's bound can detect the difference between the genus and the free genus.

Recall that Lin's original definition of the twisted Alexander polynomial is in terms of regular Seifert surfaces,
it might be worthwhile to explore the possibility that an appropriate version of Lin's twisted Alexander polynomial gives lower bounds on the `regular genus' of a knot
which can tell the regular genus apart from the free genus.
