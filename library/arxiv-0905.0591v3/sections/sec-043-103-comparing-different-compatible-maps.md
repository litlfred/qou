---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-043-103-comparing-different-compatible-maps
section_title: "Comparing different –compatible maps"
section_number: 10.3
pages: 33-34
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.959
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:comparison}


\noindent We now recall a definition from \cite{Ha06}.

\begin{definition}
Let $N$ be a 3--manifold with empty or toroidal boundary.
We write $\pi=\pi_1(N)$. Let $\phi:\pi\to \mathbb{Z}$ an epimorphism. Furthermore let $\varphi_1:\pi \to
\gamma_1$ and $\varphi_2:\pi \to \gamma_2$ be epimorphisms to torsion--free solvable groups $\gamma_1$
and $\gamma_2$. We call $(\varphi_1,\varphi_2,\phi)$ an {\em admissible triple} for $\pi$ if there
exist epimorphisms $\varphi_{2}^1:\gamma_1\to \gamma_2$  and $\phi_2:\gamma_2\to
\mathbb{Z}$ such that $\varphi_2=\varphi_{2}^1\circ \varphi_1$, and $\phi=\phi_2\circ \varphi_2$.
\end{definition}



\noindent The situation can be summarized in the following diagram
 \[   \xymatrix { &\gamma_1\ar[d]^{\varphi_2^1}\\ \pi \ar[dr]_{\phi} \ar[ur]^{\varphi_1} \ar[r]^{\varphi_2}
&\gamma_2 \ar[d]^{\phi_2}\\& \mathbb{Z}. }
     \]
Note that in particular $(\varphi_i,\phi), i=1,2$ are admissible pairs for $\pi$.








The following theorem is perhaps the most striking feature of higher order Alexander polynomials.
In light of Theorem \ref{thm:lowerboundho} the statement can be summarized as saying that higher order Alexander polynomials corresponding to larger groups
give better bounds on the Thurston norm.

 \begin{theorem}
Let $N$ be a 3--manifold whose boundary is a (possibly empty) collection of tori. Let
$(\varphi_1,\varphi_2,\phi)$ be an admissible triple for $\pi_1(N)$.
Suppose that $\Delta_{N,\phi}^{\varphi_2}\ne 0$, then it follows that $\Delta_{N,\phi}^{\varphi_1}\ne 0$.
We write
\[ d_i\mathrel{\mathop:}=\deg(\Delta_{N,\phi}^{\varphi_i})- \deg(\Delta_{N,\phi,0}^{\varphi_i})-\deg(\Delta_{N,\phi,2}^{\varphi_i}), i=1,2 \]
Then the following holds:
\[ d_1 \geq d_2.\]
Furthermore, if the ordinary Alexander polynomial $\Delta_N^\phi\in \mathbb{Z}[t^{\pm 1}]$ is non--trivial, then
 $d_1-d_2$ is an even integer.
\end{theorem}

\begin{proof}
The fact that $\Delta_{N,\phi}^{\varphi_2}\ne 0$ implies that $\Delta_{N,\phi}^{\varphi_1}\ne 0$
and the  inequality $d_2\geq d_1$  were first proved for knots by Cochran \cite{Co04}.
 Cochran's result were  then extended to the case of 3--manifolds by Harvey \cite{Ha06} (cf. also \cite{Fr07}).
Finally the fact that $d_2-d_1$ is an even integer when $\Delta_N^\phi\ne 0$ is proved in \cite{FK08a}.
\end{proof}

The strong relationship between the Thurston norm and higher order Alexander polynomials
is also confirmed by the following result (cf. \cite{FH07}).

\begin{theorem}
Let $N$ be a 3--manifold with empty or toroidal boundary, let $\varphi:\pi_1(N) \to \gamma$ be an epimorphism to a torsion--free solvable group such that the abelianization $\pi_1(N)\to F\mathrel{\mathop:}=H_1(N;\mathbb{Z})/\mbox{torsion}$ factors through $\varphi$.
Then  the map
\[ \begin{array}{rcl} H^1(N;\mathbb{Z})=\mbox{Hom}(F,\mathbb{Z})&\to & \mathbb{Z}_{\geq 0} \\
\phi &\mapsto &\max\{0,\deg(\Delta_{N,\phi}^{\varphi})- \deg(\Delta_{N,\phi,0}^{\varphi})-\deg(\Delta_{N,\phi,2}^{\varphi})\}\end{array} \]
defines a seminorm on $H^1(N;\mathbb{Z})$ which gives a lower bound on the Thurston norm.
\end{theorem}
