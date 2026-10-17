---
doc_id: arxiv-1705.01853v2
doc_title: "Line Operators in the Standard Model"
section_id: sec-000-2-a-review-of-line-operators
section_title: "A Review of Line Operators"
section_number: 2
pages: 4-7
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
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





\subsubsection{An Example: $SU(N)$ vs $SU(N)/{\bf Z}_N$}

For $g=su(N)$, the centre of the group is $Z(SU(N)) = {\bf Z}_N$.  When the gauge group is $G=S(N)$, all electric line operators are allowed; that is $z^e=0,1,2,\ldots, N-1$. In contrast, the magnetic line operators are restricted to lie on the magnetic root lattice, meaning that $z^m=0$. The resulting set of line operators for $SU(3)$  are shown in Figure \ref{su3lines}a, plotted in the $(z^e,z^m)$ lattice. The figure shows the charges extended to $z^{e,m}\in {\bf Z}$;  the key physics can be seen in the grey box, which restricts  to $z^{e,m} =0,1,2$. The lattice is then formed by tiling this box.

\para
For $SU(N)/{\bf Z}_N$, the only purely electric line operators lie on the root lattice. They have $(z^e,z^m)=(0,0)$. The magnetic line operators are more interesting and there are several, different solutions to the quantisation condition \eqn{diracq}. The simplest such solution is to admit the purely magnetic line operators $(0,z^m)$ with $z^m=0,1,2,\ldots N-1$. No further dyonic operators are then allowed. The resulting spectrum of line operators for $G=SU(3)/{\bf Z}_3$ is shown in Figure \ref{su3lines}b.



\para
For $G=SU(N)/{\bf Z}_N$ (but not for all other gauge groups \cite{ast}), other solutions to \eqn{diracq} are generated by the theta angle. This arises through the Witten effect \cite{witteneffect} -- which holds for line operators as well as dynamical particles \cite{kapustin,henningson} -- and ensures that, in the presence of $\theta\neq 0$,  purely magnetic line operators turn into dyonic line operators. In particular, as $\theta \rightarrow \theta+2\pi$, each line operator picks up an electric charge given by

\be \lambda^e \rightarrow \lambda^e + \lambda^m\ \ \ \Rightarrow\ \ \ z^e\rightarrow z^e+z^m\nn\ee

For the $G=SU(N)$ theory, the set of line operators transforms into itself under $\theta\rightarrow \theta +2\pi$. In contrast, for $G=SU(N)/{\bf Z}_N$, the set of line operators turns into something different. This means that the theory with $\theta=0$ is not the same as the theory with $\theta=2\pi$. Instead, for $G=SU(N)/{\bf Z}_N$, the theta angle takes values in the range

\be \theta \in [0,2\pi N)\nn\ee

This extended range of $\theta$  is associated to the fact that $G=SU(N)/{\bf Z}_N$ admits instantons with fractional charge $1/N$. Starting with the set of line operators generated by $(z^e,z^m) = (0,1)$, under a shift $\theta\rightarrow \theta + 2\pi k$ we have a new theory with line operators generated by $(z^e,z^m)=(k,1)$. For $G=SU(3)/{\bf Z}_3$,  the set of line operators are shown in  Figures \ref{su3lines}c and \ref{su3lines}d for $k=1$ and $k=2$ respectively.
