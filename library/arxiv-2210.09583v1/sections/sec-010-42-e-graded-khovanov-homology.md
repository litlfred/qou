---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-010-42-e-graded-khovanov-homology
section_title: "e-graded Khovanov Homology"
section_number: 4.2
pages: 13-14
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.981
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
\label{section: e-Khov}
We construct the e-graded version of Khovanov homology in a nearly identical manner.
We can define an e-grading on $\cat{2Cob}$ by adding formal objects $\Sigma\{(a,b)\}$ for every $1$-manifold $\Sigma$ and $(a,b)\in \Z \times \Z_4$, and defining the degree $deg(W)$ of a cobordism $W:\Sigma_0\{(m,m')\}\to \Sigma_{1}\{(n,n')\}$ by
\[
deg(W)=(\chi(W)+n-m, -\chi(W)+n'-m')
\]
Pants cobordisms have degree $(-1,1)$ and caps and cups have degree $(1,-1)$.


Given an oriented link diagram $L$, construct a chain complex $[L]$ of cobordisms as follows.
Replace each crossing of $L$ with the chain complex
\begin{align}\label{crossing-complexes}
\left[
  \hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0) to (1,1);
\draw[thick,   blue] (1,0) to (.6,.4);
\draw[thick,   blue] (0,1) to (.4,.6);
\end{tikzpicture}}\right]
&=
\underline{
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0) to (0,1);
\draw[thick,   blue] (1,0) to (1,1);
\end{tikzpicture}}} \{(0,1)\}
\to
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}}
\{(1,0)\}
 \\
 \left[
 \hackcenter{ \begin{tikzpicture} [xscale=-1, scale=.75]
\draw[thick,   blue] (0,0) to (1,1);
\draw[thick,   blue] (1,0) to (.6,.4);
\draw[thick,   blue] (0,1) to (.4,.6);
\end{tikzpicture}}\right]
&=
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0).. controls ++(.25,.5) and ++(-.25,.5).. (1,0);
\draw[thick,   blue] (0,1).. controls ++(.25,-.5) and ++(-.25,-.5).. (1,1);
\end{tikzpicture}}
\{(-1,0)\}
\to
\underline{
\hackcenter{ \begin{tikzpicture} [scale=.75]
\draw[thick,   blue] (0,0) to (0,1);
\draw[thick,   blue] (1,0) to (1,1);
\end{tikzpicture}}} \{(0,-1)\}
\end{align}
where the underlined term in each complex lives in cohomological degree $0$.
The maps between the $0$ and $1$-resolution in each complex are given by a saddle cobordism just like before.

Then the complex $[L]$ is defined by
\begin{align}\label{pre-e-Khov}
  [L]^{r-n_-} &= \bigoplus_{\sum z_i=r} L_z' \{(-n_-+r, n_+-r)\} \\
  d|_{L_z'} &= \sum\limits_{\alpha: z \to w}\epsilon(\alpha)D_{\alpha}
\end{align}
where $D_\alpha=D_{X_j}$ is one of the two maps shown above.
We then get the e-graded version of the Khovanov complex by shifting the degree of each term.
\begin{definition}
The chain complex $eKh(L)$ is obtained by shifting the degree of each chain group by $\{wr(L), 2wr(L)\}$
  \begin{align}\label{e-Khov-1}
  eKh(L)&=[L]\{(wr(L), 2wr(L)\}
\end{align}
\end{definition}

Let $A=R[X]/(X^2)$ be the free e-graded $R$-module of rank $2$ spanned by $\1$ and $X$ in degrees $deg(\1)=(1,-1)$ and $deg(X)=(-1,1)$.
We equip $A$ with the following maps to make it a Frobenius algebra.
\begin{align}\label{Frob-str-1}
  \varepsilon: A\to R & \left\{\begin{matrix}
                                \1 \to 0 \\
                                X\to 1
                              \end{matrix} \right.\\
  \eta: R \to A & \left\{ 1\to \1 \right. \\
  m:A\otimes A \to A & \left\{  \begin{matrix}
                                  \1 \otimes \1 \to \1 & \1\otimes X \to X \\
                                  X\otimes \1 \to X & X\otimes X \to 0
                                \end{matrix}  \right. \\
  \Delta: A\to A\otimes A & \left\{ \begin{matrix}
                                      \1 \to \1\otimes X + X \otimes \1 \\
                                      X \to X \otimes X
                                    \end{matrix}\right.
\end{align}
We have $deg(m)=deg(\Delta)=(-1,1)$ and $deg(\varepsilon)=deg(\eta)=(1,-1)$.

\begin{definition}
  Let $\mathcal{F}:\cat{2Cob} \to \cat{R-emod}$ be the TQFT corresponding to the Frobenius algebra $A$. Denote $M_n$ as the object in $\cat{2Cob}$ consisting of $n$-disjoint circles. $\mathcal{F}$ sends a collection of $k$ circles to $A^{\otimes k}$ and
  \begin{itemize}
    \item The two pair-of-pants cobordisms $M_2\to M_1$ and $M_1\to M_2$ to $m$ and $\Delta$ respectively.
    \item The birth $M_0 \to M_1$ and death $M_1 \to M_0$ to $\eta$ and $\varepsilon$ respectively.
  \end{itemize}
\end{definition}
It is easy to see that $\mathcal{F}$ is well defined and degree preserving.
Apply the TQFT $\mathcal{F}:\cat{2Cob} \to \cat{R-emod}$ to turn the chain complex $eKh[L]$ into a chain complex $C(L):=\mathcal{F}(eKh[L])$ of e-graded $R$-modules.

\begin{theorem}\label{homology-link-invariant}
  The homology $H(C(L))$ of the chain complex $C(L)$ is an invariant of oriented links.
\end{theorem}

To show this, we need to show that the Reidemeister moves hold.
Since forgetting the $\Z_4$-grading recovers Khovanov homology exactly, the arguments from \cite{BN1} for why Khovanov homology is a link invariant can be used to prove this theorem.
To demonstrate, we prove that this homology satisfies R1 as a testament to how the arguments for Khovanov homology work verbatim for this homology theory.
