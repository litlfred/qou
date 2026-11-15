---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-019-54-twisted-invariants-and-slice-links
section_title: "Twisted invariants and slice links"
section_number: 5.4
pages: 17-18
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.967
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:slicelinks} \label{section:linkslice}


Kawauchi \cite[Theorems~A~and~B]{Ka78} showed that if $L$ is a slice link with more than one component, then the ordinary Alexander module  is necessarily non--torsion,
in particular the corresponding Reidemeister torsion is zero.
We will follow an idea of Turaev \cite[Section~5.1]{Tu86} to define a (twisted) invariant for links even if the (twisted) Alexander module is non--torsion.
This invariant will then give rise to a sliceness obstruction for links. We refer throughout this section to \cite{CF10} and \cite{Tu86} for details.

Let $L\subset S^3$ be an oriented $m$--component link.
Let $R\subset \mathbb{C}$ be a subring and let $\alpha:\pi(S^3\setminus \nu L)\to \mbox{GL}(k,R)$ be a unitary representation. Suppose that
$\psi:\pi_1(S^3\setminus \nu L)\to F$ is a homomorphism to a free abelian group which is non--trivial on each meridian of $L$.
Under these assumptions      we can endow $H_1(S^3\setminus \nu L;Q(R[F])^k)$ and $H_2(S^3\setminus \nu L;Q(R[F])^k)$
with dual bases and using these bases we can define
 the
Reidemeister torsion
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)\in Q(F)^*/N(Q(F)^*),\]
here  $N(Q(F)^*)$ denotes the subgroup of norms of the multiplicative group $Q(F)^*$, i.e.
 $N(Q(F)^*)=\{ q\overline{q} \, |\, q\in Q(F)^*\}$. Reidemeister torsion
$\tilde{\tau}^{\alpha\otimes \psi}(L)$ viewed as an element in $Q(F)^*/N(Q(F)^*)$ is well--defined up to multiplication
by an element of the form $\pm df$ where $d\in \det(\alpha(\pi_1(S^3\setminus \nu L))), f\in F$.
The invariant $\tau^{\alpha\otimes \psi}(L)$ is the twisted version of an invariant first introduced by Turaev \cite[Section~5.1]{Tu86}.


For example, if $L$ is the $m$--component unlink in $S^3$ with meridians $\mu_1,\dots,\mu_m$,
then given $\alpha$ and $\psi$ as above we have
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)=\pm df \cdot \prod\limits_{i=1}^m \det\big(\mbox{id}-\psi(\mu_i)\alpha(\mu_i)\big)^{-1} \, \in Q(F)^*/N(Q(F)^*)\]
with $d\in \det(\alpha(\pi_1(S^3\setminus \nu L))), f\in F$.





In \cite{CF10} the first author and Jae Choon Cha prove the following result.

\begin{proposition}\label{prop:slicelink}
Let $L$ be an $m$--component oriented slice link with meridians $\mu_1,\dots,\mu_m$.
 Let $R\subset \mathbb{C}$ be a subring closed under complex conjugation and let $\alpha:\pi_1(S^3\setminus \nu L)\to \mbox{GL}(k,R)$ be a representation which factors through a finite group of prime power order. Let
$\psi:H_1(S^3\setminus \nu L)\to F$ be an epimorphism onto a free abelian group which is non--trivial on each meridian of $L$.  Then
\[ \tilde{\tau}^{\alpha\otimes \psi}(L)=\pm
 df\cdot \prod\limits_{i=1}^m \det\big(\mbox{id}-\psi(\mu_i)\alpha(\mu_i)\big)^{-1} \, \in Q(F)^*/ N(Q(F))^* \]
 for some $d\in \det(\alpha(\pi_1(S^3\setminus \nu L)))$ and $f\in F$.
\end{proposition}



If $\alpha$ is the trivial representation over $\mathbb{Z}$, then it is shown in \cite[Theorem~5.1.1]{Tu86} that the torsion
is represented by the untwisted Alexander polynomial of $L$ corresponding to $\psi$.
Using this observation we see that Proposition \ref{prop:slicelink} generalizes earlier
results of Murasugi \cite{Mu67}, Kawauchi \cite{Ka77,Ka78} and Nakagawa \cite{Na78}. The approach taken in \cite{CF10}
is partly inspired by  Turaev's proof of the untwisted case (cf. \cite[Theorem~5.4.2]{Tu86}).

In \cite{CF10} we will in particular use the obstruction of Proposition \ref{prop:slicelink} to reprove that the Bing double of the Figure 8 knot is not slice.
This had first been shown by Cha \cite{Ch09}.
