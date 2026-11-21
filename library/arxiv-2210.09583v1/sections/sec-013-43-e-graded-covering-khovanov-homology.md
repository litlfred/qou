---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-013-43-e-graded-covering-khovanov-homology
section_title: "e-graded Covering Khovanov Homology"
section_number: 4.3
pages: 15-16
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.962
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
Let $R=\Z^\pi$ for the remainder of the paper.
This section assumes prior knowledge of Putyra's work on Covering Khovanov homology \cite{P}.
For the sake of brevity we omit most of the technical details and definitions involving "chronology".
Covering Khovanov homology constructs a chain complex of modules over the ring $\mathbf{k}:=\Z[X,Y,Z]/(X^2=Y^2=1)$ such that the homology of the chain complex if we specialize $X,Y,Z$ to be 1 is regular Khovanov homology and the homology of the chain complex where we take $X, Z$ to be $1$ but $Y$ to be $-1$ is Odd Khovanov homology.
For our purposes, we can describe this as a chain complex of $R=\Z^\pi$ modules with $\pi$ playing the role of $Y$.


We first construct an e-graded version of the generalized Khovanov bracket $eKh_{cov}(L)$ from \cite[Definition 5.9]{P} by following the exact same procedure as Putyra except we handle the gradings and shifts exactly as in Section \ref{section: e-Khov}.
This is a chain complex in the additive closure of the $R$-linear category of chronological cobordisms $\cat{RChCob}$.

Then one can show that this complex is an invariant of oriented links if we consider it as a chain complex of chronological cobordisms modulo the S, T, and 4Tu relations \cite[Section 7]{P}.
The quotient of $\cat{RChCob}$ by these relations is denoted $\cat{RChCob}_{/\ell}$.
The proof of invariance is exactly the same as the proof presented in \cite[Section 7]{P}.


\begin{definition}{\cite[Definition 10.1]{P}}
  Set $G=\Z\times \Z_4 \times \Z_2$, and $U(R)$ to be the group of invertible elements in $R$. Then define a group homomorphism $\lambda: G \times G \to U(R)$ by
  \[
  \lambda((a,b,c)(d,e,f))=\pi^{cf}
  \]
  We also define a e-graded super tensor product of $G$-graded modules as usual, but for homogeneous homomorphisms $f,g$ we define $f\otimes g$ by the formula:
  \[
  (f\otimes g)(m\otimes n) = \lambda(deg(g), deg(m))f(m)\otimes g(n)
  \]
  This defines a symmetric monoidal structure on the category of $G$-graded $R$-modules, which we call $\cat{R-egSmod}$.
\end{definition}

We refer to $\cat{R-egSmod}$ as the category of e-graded $R$-supermodules.

\begin{definition}
  Let $A=R[X]/(X^2)$ be the free e-graded $R$-supermodule of rank 2 spanned by $\1$ and $X$ in degrees $deg(\1)=(1,-1,0)$ and $deg(X)=(-1,1,1)$.
  Equip it with the following operations
  \begin{align}\label{Frob-str-1}
  \varepsilon: A\to R & \left\{\begin{matrix}
                                \1 \to 0 \\
                                X\to 1
                              \end{matrix} \right.\\
  \eta: R\to A & \left\{ 1\to \1 \right. \\
  m:A\otimes A \to A & \left\{  \begin{matrix}
                                  \1 \otimes \1 \to \1 & \1\otimes X \to X \\
                                  X\otimes \1 \to X & X\otimes X \to 0
                                \end{matrix}  \right. \\
  \Delta: A\to A\otimes A & \left\{ \begin{matrix}
                                      \1 \to \pi \1\otimes X + X \otimes \1 \\
                                      X \to X \otimes X
                                    \end{matrix}\right.
\end{align}
These maps have degrees
\[deg(\Delta)=(-1,1,1), \; deg(m)=(-1,1,0), \;deg(\varepsilon)=(1,-1,1), \; deg(\eta)=(1,-1,0).\]
\end{definition}

The pair $(R,A)$ with these operations defines a Chronological Frobenius system as in \cite[Definition 10.5]{P}
Then we obtain a well defined, degree preserving chronological TQFT functor $\mathcal{F}:\cat{RChCob}\to \cat{R-egSmod}$ as in \cite[Proposition 10.6]{P}.
This functor preserves the S, T, and 4Tu relations, so we get a well-defined functor $\mathcal{F}_{cov}:\cat{RChCob}_{/\ell} \to \cat{R-egSmod}$.

Let $C_{cov}(L)$ be the chain complex of e-graded $R$-supermodules given by $C_{cov}(L):=\mathcal{F}_{cov}(eKh_{cov}(L))$.
When $\pi=1$, $C_{cov}(L)=C(L)$ by construction, which is the chain complex for e-graded Khovanov homology.
We call the homology $H(C_{cov}(L))$ of this complex the \emph{e-graded version of covering Khovanov homology}.
If we forget the $\Z_4$-grading of each module in the complex, then we obtain the covering Khovanov homology $\mathcal{H}_{cov}(L)$ defined in \cite[Example 10.7]{P}.



\bibliographystyle{plain}
