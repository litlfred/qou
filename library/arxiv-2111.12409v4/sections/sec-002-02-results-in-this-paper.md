---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-002-02-results-in-this-paper
section_title: "Results in this paper"
section_number: 0.2
pages: 2-4
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 1.0
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
The goal of this paper is to generalise Roth's theorem  in a wider framework which includes Corvaja's and Vojta's settings.

The theory of  adelic curves introduced by Chen and Moriwaki in \cite{Ch-Mo} provides such natural framework:  an adelic curve $\mathbb X$ consists of a field $\mathbb K$ of characteristic $0$ and a measure space $(\Omega,\mathcal A, \mu)$ endowed with a function  $\phi:\omega\mapsto \vert\cdot \vert_{\omega}$ that maps $\Omega$ into the set of places of $\mathbb K$ and such that $\omega\mapsto\log|a|_\omega$ is  in $L^1(\Omega,\mu)$ for any $a\in\mathbb K^\times$. On $\mathbb X$ we have a well defined notion of height $h_{\mathbb X}$, and moreover a ``product formula'' which is expressed as an integral over $\Omega$. The adelic curves satisfying this product formula are called \emph{proper}. The fields with a product formula of $\cite{C}$ are trivially proper adelic curves when the set of places is endowed with the counting measure. Moreover in \cite[Section 3]{vo} it is shown that arithmetic function fields can be endowed with  a structure of proper adelic curve.

In this paper we prove two generalisations of Roth's theorem for proper adelic curves. The main results will be stated in terms of some inequalities involving the integral of the measurable functions $\omega\mapsto \log^-|\beta-\alpha_i|_\omega$  where $\alpha_1,\ldots, \alpha_n\in\mathbb K$ are the elements we want to approximate by an approximant $\beta\in\mathbb K$. Unfortunately, the bare definition of proper adelic curves is too general to give any meaningful result in the direction of Roth's approximation theorem, since  the functions $\log^-|\beta-\alpha_i|$ can be in principle very ``wild''. Therefore, we have to impose some analytic conditions on such functions in order to get the desired Roth's theorems. We will see that these assumptions are not too artificial, in fact we recover Theorems \ref{CorCorv} and \ref{vojta} as special cases. 



The first condition we impose  on our adelic curves is the \emph{strong $\mu$-equicontinuity} (see definition \ref{st_muequi}): roughly speaking it  means that for any set of finite measure $S\subset\Omega$ one requires for the functions $\omega\mapsto \log|\beta|_{\omega}$, to be ``equicontinuous'' almost everywhere  on $S$. Under such hypothesis we prove the following theorem:

\begin{namedtheorem}[\hypertarget{thm:(A)}{Theorem (A)}]
Let $\mathbb X=(\mathbb K,\Omega, \phi)$ be a proper adelic curve satisfying the strong $\mu$-equicontinuity condition. Let $S=S_1\sqcup S_2\sqcup\ldots\sqcup S_n\subseteq\Omega $ be the disjoint union of subsets of finite measure. Fix some distinct elements $\alpha_1,\dots ,\alpha_n\in\mathbb K$, then for any $\varepsilon>0$ there exists a real constant $C>0$ (depending on the fixed data) such that for any $\beta\in \mathbb K$ with $h_{\mathbb X}(\beta)>C$ 
it holds that:
\begin{equation}\label{our_roth}
\sum^n_{i=1}\int_{S_i}\log^-\vert \beta-\alpha_i\vert_\omega d\mu(\omega)>-(2+\varepsilon)h_\mathbb X(\beta)\,.
\end{equation}
\end{namedtheorem}
We will show that Theorem \ref{CorCorv} is a consequence of Theorem \bref{thm:main}{(A)}, but on the other hand Vojta's inequality is stronger and moreover it doesn't depend on the fixed partition of $S$. Nevertheless, we get a generalisation of Theorem \ref{vojta}  under the following hypotheses:
\begin{itemize}
\item We slightly relax the  strong $\mu$-equicontinuity condition and we allow the existence of arbitrary small sets where the equicontinuity fails (see Definition \ref{muequi}).
\item   We assume that  the functions $\omega\to \log^-|\beta|_\omega$ are \emph{uniformly integrable} while $\beta$ varies (see definition \ref{un_int})
\end{itemize}

Our second main theorem is then the following:

\begin{namedtheorem}[\hypertarget{thm:(B)}{Theorem (B)}]
Let $\mathbb X=(\mathbb K,\Omega, \phi)$ be a proper adelic curve satisfying the $\mu$-equicontinuity condition and the uniform integrability condition. Fix some distinct elements $\alpha_1,\dots ,\alpha_n\in\mathbb K$. Let $S$ be a measurable  subset of $\Omega$ of finite measure. Then for any $\varepsilon>0$ and any $c\in\mathbb R$ there exists a real constant $C>0$ (depending on the fixed data) such that for any $\beta\in \mathbb K$  with  $h_{\mathbb X}(\beta)>C$   
it holds that:
\begin{equation}\label{our_roth_encore}
\int_{S}\,\min_{1\le i\le n}\left(\log^-\vert \beta-\alpha_i\vert_\omega\right) d\mu(\omega)>-(2+\varepsilon)h_\mathbb X(\beta)+c
\end{equation}
\end{namedtheorem}
Finally, in  Example \ref{Qbar} we show that  the $\mu$-equicontinuity condition doesn't hold for all proper adelic curves; in our example we consider $\overline{\mathbb Q}$ endowed with a natural structure of adelic curve naturally inherited from $\mathbb Q$.


Our strategy consists  in weaving together the ideas of Corvaja and Vojta to get  rather elementary proofs which are independent from Arakelov geometry. On the other hand we don't have, at the moment, any examples of interesting proper adelic curve different from the ones already known. It is a much harder problem to find new concrete cases in which Roth's theorem holds. After all, a highly nontrivial  achievement of Vojta's work consists in showing that the $\mu$-equicontinuity   and the uniform integrability hold  for arithmetic function fields. He does this by using the geometry  of complex fibres at infinity  appearing in Arakelov geometry.


 The very coarse overview of the proofs is the following: Roth's theorem is about the simultaneous approximation of some distinct elements $\alpha_1,\ldots, \alpha_n$ that by simplicity (in fact it will be enough to consider this case) can be fixed in $\mathbb K$, with an element $\beta\in\mathbb K$. The existence of a very special ``interpolating polynomial'' $\delta$ for such elements (section \ref{aux}) allows us to write some  integral estimates  for  measurable functions  on $\Omega$  satisfying some technical properties related to the heights of the $\alpha_i$'s and $\beta$ (section \ref{estimates}). Then, assuming  that Roth's theorem is false  leads to the construction  of a measurable function $\theta:S\to\mathbb R_{\ge 0}$ that gives the desired contradiction on the integral estimates previously found. The crucial point of the proof consists in the construction of $\theta$, and this is exactly where we need the additional technical conditions on the adelic curve. 


We finally mention that section \ref{introad} is a brief review of the theory of adelic curves introduced  in \cite{Ch-Mo}, and moreover that Appendix \ref{ap} sketches the construction of the interpolating polynomial employed in \cite{C}.



\paragraph{Acknowledgements.} Both the authors want to express their gratitude to \emph{Pietro Corvaja} for introducing them to the subject and for his enlightening explanations. They also want to thank \emph{Lorenzo Freddi} and \emph{Huyai Chen} for replying to several questions.

A special mention goes to the anonymous referee for their incredible peer-reviewing work with this article. Their deep understanding of the topic and their compelling comments  were extremely useful to fix some mistakes.

The first author was partially supported by the EPSRC grant EP/M024830/1 ``Symmetries and correspondences: intra-disciplinary developments and applications'', partially by the research grant ``Higher Arakelov geometry, Cryptography and Isogenies of Elliptic Curves'' conferred by the University of Udine, and partially by the Ben-Gurion university of the Negev.

The second author wants to thank his wife \emph{Elena}.
