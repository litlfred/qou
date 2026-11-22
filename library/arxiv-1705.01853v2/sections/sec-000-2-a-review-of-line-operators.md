---
doc_id: arxiv-1705.01853v2
doc_title: "Line Operators in the Standard Model"
section_id: sec-000-2-a-review-of-line-operators
section_title: "A Review of Line Operators"
section_number: 2
pages: 4-6
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Line Operators in the Standard Model — There is an ambiguity in the gauge group of the Standard Model."
---
\label{reviewsec}

We start by reviewing the properties of line operators, described in \cite{ast},  that we will later need. 


\para
Wilson lines are operators which describe the insertion of an infinitely massive, electrically charged particle sitting at the origin of space \cite{wilson}. They are labelled by representations $R$ of  the gauge group $G$, and given by

\be W_R = {\rm Tr}_R \,{\cal P}\exp\left(i\int dt\  A_0\right)\nn\ee

Wilson lines exist for all representations $R$, regardless of the dynamical matter content of the theory. This means, in particular, that different gauge groups $G$ will have a different spectrum of Wilson lines, even if they share a common Lie algebra ${\bf g}$. We denote the weight lattice of ${\bf g}$ as $\Lambda_w$. Then the representations of the universal cover of $G$ --- which we denote as $\tilde{G}$ ---  are labelled by points in the lattice $\Lambda_w/W$ where $W$ is the Weyl group. Representations of $G = \tilde{G}/\Gamma$ are labelled by an appropriate sublattice $\Lambda_w/W$.

\para
't Hooft lines are operators which describe the insertion of an infinitely massive, magnetically charged particle sitting at the origin of space \cite{thooft}.  They are best thought of as defect operators, in which the gauge fields have suitable boundary conditions imposed on the worldline of the magnetic source \cite{kapustin}.  For a gauge group $G$, 't Hooft lines are labelled by some sublattice of $\Lambda_{mw}/W$ where $\Lambda_{mw}$ is the magnetic weight lattice \cite{gno}; it is the weight lattice of the dual Lie algebra ${\bf g}^\star$, or the dual of the root lattice of ${\bf g}$.

\para
More generally, we may probe the theory with a dyonic Wilson-'t Hooft line. These are labelled by some sublattice of $(\Lambda_w\times \Lambda_{mw})/W$ \cite{kapustin}. We will denote the weights as $(\lambda^e,\lambda^m)\in \Lambda_w\times \Lambda_{mw}$, with the identification $(\lambda^e,\lambda^m)\sim (w\lambda^e,w\lambda^m)$, where $w\in W$.

\para
Given a choice of gauge group $G= \tilde{G}/\Gamma$, we would like to determine the allowed spectrum of  line operators. This  problem was solved in \cite{ast} for connected  groups. (Here we consider only line operators which enjoy an independent existence, as opposed to  those which survive only on the boundary of a surface operator.) Certain line operators exist regardless of the choice of the discrete quotient  $\Gamma$. For the Wilson lines, these correspond to the root lattice $\Lambda_r\subset \Lambda_w$. They include, for example, the Wilson line in the adjoint representation.  Different choices of $\Gamma$ then determine which of the remaining Wilson lines are allowed. These can be characterised by their transformation under $\Lambda_w/\Lambda_r = Z(\tilde{G})$, the centre of $\tilde{G}$. 

\para
A similar story plays out for the 't Hooft lines: for every choice of $G = \tilde{G}/\Gamma$ there is a 't Hooft line corresponding to the  co-root lattice $\Lambda_{cr}\subset \Lambda_{mw}$ or, equivalently the root lattice of ${\bf g}^\star$. The remaining 't Hooft lines are characterised by  $\Lambda_{mw}/\Lambda_{cr} = Z(\tilde{G})$ and their admissibility depends on the choice of $\Gamma$.  





\para
The upshot of this is that line operators  decompose into classes, labelled by the 

\be
(z^e,z^m) \in Z(\tilde{G}) \times Z(\tilde{G})\nn\ee

Furthermore, the line operators form a group; the operator product gives rise to an addition law while the reversal of orientation provides an inverse. These properties are enough to ensure that if one member of the class labelled by $(z^e,z^m)$ is present in the theory the the entire class is present. 

\begin{figure}[htb]
\begin{center}
\epsfxsize=6.2in\leavevmode\epsfbox{sumore.eps}
\end{center}
\caption{The spectrum of line operators for: a) $SU(3)$;  b) $SU(3)/{\bf Z}_3$ at $\theta=0$;  c) $SU(3)/{\bf Z}_3$ at $\theta=2\pi$;  d) $SU(3)/{\bf Z}_3$ at $\theta=4\pi$.}
\label{su3lines}
\end{figure}


\para
The admissible electric line operators $(z^e,0)$ are determined by the choice of gauge group $G=\tilde{G}/\Gamma$, with only those $z^e$ which are invariant under $\Gamma$ present. The magnetic and dyonic line operators are then restricted by Dirac quantisation. To be specific, consider gauge groups with centre $Z(\tilde{G}) = {\bf Z}_N$. In this case both $z^e$ and $z^m$ are integers mod $N$. Two lines $(z^e,z^m)$ and $(z^{\prime\,e},z^{\prime\,m})$ can both exist as operators only if

\be z^ez^{\prime\,m} - z^mz^{\prime\,e} = 0\ \ {\rm mod}\ \ N\label{diracq}\ee

This is the Dirac quantisation condition for non-Abelian lines. The important role played by the centre of the gauge group in Dirac quantisation was first pointed out by Corrigan and Olive \cite{corrigan}.
