---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-022-62-twisted-alexander-polynomials-and-the-thursto
section_title: "Twisted Alexander polynomials and the Thurston norm"
section_number: 6.2
pages: 21-23
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.945
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:genus}

It is a classical result of Alexander that given a knot $K\subset S^3$ the following inequality holds:
 \[ 2\mbox{genus}(K) \geq \deg(\Delta_K).  \]
This result was first generalized to general 3--manifolds by McMullen \cite{McM02}
and then to twisted Alexander polynomials in \cite{FK06}.
The following theorem is \cite[Theorem~1.1]{FK06}.
The proof builds partly on ideas of Turaev's in \cite{Tu02b}.


\begin{theorem} \label{thm:lowerboundphi} Let $N$ be a 3--manifold whose boundary is empty or consists of tori.
Let $\phi \in H^1(N;\mathbb{Z})$ be non--trivial and let $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ be a representation such that
$\Delta_{N}^{\gamma \otimes \phi}\ne 0$.
 Then
\[  ||\phi||_T \geq  \frac{1}{k} \deg(\tau(N,\gamma\otimes \phi)).\]
Equivalently,
\[ ||\phi||_T \geq \frac{1}{k}\big(\deg(\Delta_{N}^{\gamma\otimes \phi})- \deg(\Delta_{N,0}^{\gamma\otimes \phi}) -\deg(\Delta_{N,2}^{\gamma\otimes \phi})\big).\]
\end{theorem}

\begin{remark}
\begin{enumerate} In \cite{FK06} it was furthermore shown using `KnotTwister' (cf. \cite{Fr09}) that
twisted Alexander polynomials  detect the genus of all knots with up to twelve crossings.
\item
It seems reasonable to conjecture that given an irreducible 3--manifold $N$
twisted Alexander polynomials detect the Thurston norm for any $\phi \in H^1(N;\mathbb{Z})$.
A positive answer would have interesting consequences for 4--manifold topology as pointed out in
\cite{FV09}.
\item If $\Delta_{N}^{\gamma \otimes \phi}=0$, then we define the \emph{torsion twisted Alexander polynomial} $\tilde{\Delta}_N^{\gamma\otimes \phi}$ to be
the order of the $R[t^{\pm 1}]$--module
\begin{eqnarray*}

 &&\mbox{Tor}_{R[t^{\pm1}]}(H_1(N;R[t^{\pm1}]^k))=\\
&&=\{ v\in H_1(N;R[t^{\pm1}]^k)\, |\, \lambda v=0 \mbox{ for some }\lambda \in R[t^{\pm1}] \setminus \{0\}\,\}.
\end{eqnarray*}
It is then  shown in  \cite[Section~4]{FK06} that
the $\tilde{\Delta}^{\gamma\otimes \phi}_N$ also gives rise to give lower bounds on the Thurston norm.
We point out that  by \cite[Theorem~3.12~(3)]{Hi02} and  \cite[Lemma~4.9]{Tu01} the torsion twisted Alexander polynomial can be computed directly from a presentation
of $H_1(N;R[t^{\pm1}]^k)$.
\end{enumerate}
\end{remark}

Note that Theorem \ref{thm:lowerboundphi} gives lower bounds on the Thurston norm for a given $\phi\in H^1(N;\mathbb{Z})$.
In order to give bounds for the whole Thurston norm ball at once, we will introduce
 twisted Alexander norms, generalizing McMullen's Alexander norm \cite{McM02} and Turaev's torsion norm \cite{Tu02a}.
In the following let $N$ be a 3--manifold with empty or toroidal boundary such that $b_1(N)>1$.
Let  $\psi:\pi_1(N)\to F\mathrel{\mathop:}=H_1(N;\mathbb{Z})/\mbox{torsion}$ be the canonical projection map.
Let $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ be a  representation. If $\Delta_{N}^{\gamma\otimes \psi}=0$ then we set
$||\phi||_{A}^{\gamma}=0$ for all $\phi\in H^1(N;\mathbb{R} )$. Otherwise we write $\Delta_{N}^{\gamma\otimes \psi}=\sum a_if_i$
for $a_i\in R$ and $f_i \in F$. Given $\phi \in H^1(N;\mathbb{R} )$ we then define
\[ ||\phi||_{A}^{\gamma} \mathrel{\mathop:}=\max\{  \phi(f_i-f_j)\, |\, (f_i, f_j) \mbox{ such that }a_ia_j\ne 0\}.\]
Note that this norm is independent of the choice of representative of $\Delta_{N}^{\gamma\otimes \psi}$.
Clearly this defines a seminorm on $H^1(N;\mathbb{R} )$ which we call the
\emph{twisted Alexander norm of $(N,\gamma)$}. Note that if $\gamma :
\pi_1(N) \to \mbox{GL} (1,\mathbb{Z})$ is the trivial representation, then we just obtain McMullen's Alexander norm.

The following is proved in \cite[Theorem~3.1]{FK08a},
but we also refer to the work of McMullen \cite{McM02}, Turaev \cite{Tu02a}, \cite[Section~6]{Tu02b}, Harvey \cite{Ha05} and Vidussi \cite{Vi99,Vi03}.
The main idea of the proof is to combine  Theorem \ref{thm:lowerboundphi} with Corollary \ref{cor:changevardelta}.

\begin{theorem}
Let $N$ be a 3--manifold with empty or toroidal boundary such that $b_1(N)>1$. Let $\psi:\pi_1(N)\to F\mathrel{\mathop:}=H_1(N;\mathbb{Z})/\mbox{torsion}$ be the canonical projection map
and let $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ be a representation with $R$ a Noetherian UFD.
Then for any $\phi\in H^1(N;\mathbb{R} )$ we have
\[ ||\phi||_T \geq \frac{1}{k}||\phi||_A^\gamma\]
and equality holds for any $\phi$ in a fibered cone of the Thurston norm ball.
\end{theorem}

We refer to \cite{McM02} and \cite{FK08a} for some calculations, and we refer to \cite{Du01} for more information on the relationship
between the Alexander norm and the Thurston norm.
