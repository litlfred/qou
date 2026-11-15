---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.743
latex_coverage_ratio: 0.993
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
The Reshetikhin-Turaev invariants are a family of link-invariants constructed from the representation theory of quantum groups \cite{RT90}.
Examples of such invariants include the HOMFLY-PT polynomial and the colored Jones polynomial.
Following Khovanov's pioneering work categorifying the Jones polynomial \cite{K00}, and the subsequent work of many others\cite{Kh03, Sus07, KR08a, KR08b, MS09}, Webster categorified these invariants \cite{Web} using the theory of categorified quantum groups developed by Khovanov, Lauda, and Rouquier \cite{Rou2,KL10}.

The study of these link homology theories has produced a myriad of results in many different fields.

A major development in the study of categorified link invariants was an alternative categorification of the Jones polynomial called odd Khovanov homology introduced by Ozsv\'ath, Rasmussen  and Szab\'o \cite{ORS}.
Odd Khovanov homology coincides with Khovanov homology when taken with $\Z_2$-coefficients, but is distinct from Khovanov homology in general \cite{Shum}.
In order to obtain a representation theoretic undestanding of this odd Khovanov homology, Ellis, Khovanov, and Lauda started a program studying odd analogues of structures related to $U_q(\mf{sl}_2)$ and its categorification \cite{EKL, EK,Lau-odd}.

These investigations into odd categorification turned out to be closely connected with independent parallel investigations into  Kac-Moody superalgebra categorifications~\cite{KKT, KKO, KKO2}, with the odd categorification of $\mf{sl}_2$ lifting the rank one Kac-Moody superalgebra.
These odd categorifications give categorifications of the theory of covering Kac-Moody algebras~\cite{HillWang,ClarkWang, CHW,CHW2}.
Covering algebras $U_{q,\pi}(\mf{g})$ generalize quantum enveloping algebras, depending on an additional parameter $\pi$ with $\pi^2 = 1$.  When $\pi=1$, it reduces to the usual quantum enveloping algebra $U_{q}(\mf{g})$, while the $\pi = -1$ specialization recovers the quantum group of a super Kac-Moody algebra.
The quantum algebra and quantum superalgebra can be identified by an automorphism of (an extension of) the covering quantum group called a twistor, which sends $\pi \to -\pi$ and $q\to t^{-1}q$ where $t^2=-1$ \cite{CFLW}.

In the rank one case, the $\pi=1$ specialization is $U_{q}(\mf{sl}_2)$, while for $\pi=-1$ it gives the quantum supergroup $U_{q}(\mf{osp}(1|2))$ associated with the lie superalgebra $\mf{osp}(1|2)$.
Ellis and Lauda defined a $2$-supercategory $\mf{U}$ that categorifies the rank one covering algebra $U_{q,\pi}(\mf{sl}_2)$ \cite{Lau-odd}.
This categorification was later greatly simplified and generalized by Brundan and Ellis~\cite{BE2}, where the 2-supercategory formalism was better developed, building off of their work~\cite{BE1}. 
However, a understanding of odd Khovanov homology in terms of higher representation theory of $\mf{U}$ still eludes us.

There is heurisitic evidence for the existence of odd link homology theories associated to $\mf{so}_{2n+1}$ from Mikhaylov and Witten \cite{Witten}.
If we are somehow able to develop an odd version of Webster's results in the future, then we can get odd link homology theories categorifying invariants obtained through the RT process on quantum supergroups.

The $U_{q}(\mf{osp}(1|2n))$ link invariant has been defined using Markov traces on the Birman-Wenzl-Murakami algebra\cite{Blu09}.
Clark \cite{C} produced the colored $U_q(\mf{osp}(1|2n))$ invariant from the representation theory of the quantum covering group $U_{q,\pi}(\mf{osp}(1|2n))$ a la Turaev \cite{Tu}.
A notable result from Clark's paper is that the $\mf{osp}(1|2n)$ invariant and the $\mf{so}(2n+1)$ invariant are basically the same using the theory of twistors.
If we represent a tangle as a composition $S$ of $U_{q,\pi}$-module homomorphisms, then Clark showed that twistors commute with $S$ up to an integral power of $\tau$.
\begin{theorem}{\cite[Theorem 4.24]{C}}
Let $K$ be any oriented knot, and let ${}_{\mf{osp}}J_K^\lambda(q), {}_{\mf{so}}J_K^\lambda(q)\in \Q(q,t)^\tau$ be the $\lambda$-colored $\mf{osp}$ and $\mf{so}$ knot invariants.
Then
  \[
  {}_{\mf{osp}}J_K^\lambda(q)=t^{\star(K,\lambda)}{}_{\mf{so}}J_K^\lambda(t^{-1}q)
  \]
  for some $\star(K,\lambda)\in \Z$.
\end{theorem}
In particular, the $U_q(\mf{osp}(1|2))$-invariant in the variable $q$ is just the Jones polynomial in the variable $\tau^{-1}q$.

If $T_+, T_-, T_0$ are unframed oriented links that differ as shown below
\begin{align*}
  \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue, ->] (0,0) to (1,1);
\draw[thick,   blue  ] (1,0) to (.6,.4);
\draw[thick,   blue, <-] (0,1) to (.4,.6);
 \node at (.5,-1) {$T_+$};
\end{tikzpicture}}
\qquad
  \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]
\draw[thick,   blue, ->] (0,0) to (1,1);
\draw[thick,   blue  ] (1,0) to (.6,.4);
\draw[thick,   blue, <-] (0,1) to (.4,.6);
 \node at (.5,-1) {$T_-$};
\end{tikzpicture}}
\qquad
  \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]
\draw[thick,   blue, ->] (0,0) to (0,1);
\draw[thick,   blue, ->] (1,0) to (1,1);
 \node at (.5,-1) {$T_0$};
\end{tikzpicture}},
\end{align*}
then
\begin{align}\label{osp-Skein}
  (\tau^{-1}q)^{-2} J_{T_+}^1-(\tau^{-1} q)^2 J_{T_-}^1=(\tau q^{-1}-\tau^{-1}q)J_{T_0}^1.
\end{align}
However, a categorification of this invariant has not been discovered as of yet.
