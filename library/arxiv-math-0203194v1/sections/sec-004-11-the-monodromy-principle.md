---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-004-11-the-monodromy-principle
section_title: "The Monodromy principle."
section_number: 1.1
pages: 14-16
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.946
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
Let $S$ be a topological space, and $\mathcal{F}$ an abelian sheaf on $S$.
For an open set $U\subseteq S$ and a section $f\in\Gamma(U,\mathcal{F})$, the 
support of $f$ is the subset $\Supp(f)=\{u\in U\ |\ f_u\neq 0\}$, 
which is easily seen to be closed in $U$.

\begin{dfn}\label{dfn-unique-cont}
We say that the sheaf $\mathcal{F}$ satisfies the {\it principle of unique
continuation} if for any open set $U\subseteq S$ and any section 
$f\in\Gamma(U,\mathcal{F})$ the support $\Supp(f)$ is open in $U$.
\end{dfn}

Note that the principle of unique continuation is a local property.

\begin{lem}\label{lem-unique-cont}
If $\mathcal{F}$ satisfies the principle of unique continuation, then
any two sections $f,g\in\Gamma(U,\mathcal{F})$
on a connected open subset $U\subseteq S$ coincide if (and only if)
their germs $f_s$, $g_s$ at some point $s\in U$ coincide.
The converse also holds if $S$ is locally connected.
\end{lem} 

\begin{proof}
 The first assertion is clear. For the converse, let $u$ be a point adherent to the complement 
 of $\Supp(f)$. There exists a sufficiently small connected open
 neighborhood $V$ of $u$ contained in $U$. Since $f_s=0$ at some
 point $s\in V$, $f\equiv 0$ on $V$. Hence $u\not\in\Supp(f)$. This shows that $\Supp(f)$ is open.
\end{proof}

\begin{lem}\label{lem-separated}
 Let $p: F\rightarrow S$
 be the local homeomorphism canonically attached to
 $\mathcal{F} $: $\mathcal{F}(U)$ is the set of (continuous) sections of $p$ over $U$. 
 If $F$ is separated (\ie Hausdorff), then $\mathcal{F}$ satisfies the
 principle of unique continuation. The converse also holds if $S$ is
 separated.
\end{lem}

\begin{proof} If $F$ is separated, then for any two sections $f, g$ of
 $p$ over an open subset $U\subset S$, the set of $s\in U$ such that
 $f(s)=g(s)$ is closed.  Applying this to the zero-section $g=0$, we see
 that the support of $f$ is open.

 Conversely, let $x,y $ be two points of $F$. If $p(x)\neq p(y)$, there
 are disjoint open neighborhoods $V_x, V_y$ of $p(x)$ and $p(y)$
 respectively in the separated space $S$; then $p^{-1}V_x$ and
 $p^{-1}V_y$ are disjoint open neighborhoods of $x$ and $y$
 respectively. If $p(x)= p(y)$, there are open neighborhoods $U_x, U_y$
 of $x$ and $y$ respectively, an open subset $V\subset S$, and sections
 $f,g$ of $p$ over $V$, such that $f(V)=U_x,\;g(V)=U_y$. By the
 principle of unique continuation, $f\neq g$ defines an open subset
 $W\subset V$ containing $p(x)=p(y)$; then $f(W)$ and $g(W)$ are
 disjoint open neighborhoods of $x$ and $y$ respectively.
\end{proof}

\begin{dfn}
 We say that the sheaf $\mathcal{F}$ 
 satisfies the {\it monodromy principle} if it has the following property:

 let $\Gamma: [a,b]\times [0,1] \rightarrow S$ be any 
 continuous map with
 $\Gamma(\{a\}\times [0,1])=\{x_a\}, \Gamma(\{b\}\times
 [0,1])=\{x_b\}$. Let $f_{x_a}$ be an element of the stalk
 $\mathcal{F}_{x_a}$. Assume that for any
 $t\in [0,1]$, $f_{x_a}$ extends to a global section $f^{\Gamma_t}$ of
 $\Gamma_t^{\ast} \mathcal{F}$ on
 $[a,b]$. Then this extension is unique and
 $f^{\Gamma_t}(b)\in \mathcal{F}_{x_b}$ is independent of $t$.

 In this situation, the section $f^{\Gamma_t}$ of 
 $\Gamma_t^{\ast} \mathcal{F}$ is called the
 {\it continuation of $f_{x_a}$ along the path $\Gamma_t$}, and 
 $f^{\Gamma_t}(b)\in \mathcal{F}_{x_b}$ its {\it value at $x_b$}.
\end{dfn}

\begin{pro}
 If $\mathcal{F}$ satisfies the principle of
 unique continuation, then it satisfies the principle of monodromy. 
 The converse also holds if
 $S$ is locally arcwise connected.
\end{pro}

\begin{proof}
 Assume that $\mathcal{F}$ satisfies the principle of
 unique continuation. This guarantees the uniqueness of the 
 continuation $f^{\Gamma_t}$ of
 $f_{x_a}$ along the path $\Gamma_t$ for any $t$. Moreover, by a 
 special case of the proper base change theorem
 (applied to the first projection $[a,b]\times [0,1]\rightarrow 
 [a,b]$, \cf \cite[IV, 1.4]{cos}) $f^{\Gamma_t}$
 extends to a section of
 $\Gamma^{\ast}
 \mathcal{F}$ on a suitable subset of the form $[a,b]\times 
 (t-\epsilon,t+\epsilon)$. By unicity, these sections glue
 together to a global section of $\Gamma^{\ast} \mathcal{F}$. The restriction 
 of this sheaf to
 $\{b\}\times [0,1]$ is the constant sheaf with stalk
 $\mathcal{F}_{x_b}$. Therefore the value 
 $f^{\Gamma_t}(b)\in \mathcal{F}_{x_b}$ is independent of $t$.

 Conversely, let $U$ be an arcwise connected open subset of $S$, let
 $x_a, x_b$ be two points of
 $U$, and let $f$ be a section of
 $\mathcal{F}$ over $U$. Let $\gamma: [a,b]\rightarrow S$ be any path from 
 $x_a$ to $ x_b$. It
 follows from the unicity of continuation of $f_{x_a}$ along $\gamma$ 
 (requested in the monodromy
 principle) that if $f_{x_a}$ is
 $0$, so is
 $f_{x_b}$.
\end{proof}

\begin{exa}\label{lem-homotopy}
  (1) Any locally constant abelian sheaf $\mathcal{F}$ on a
 topological space $S$ satisfies the principle of unique 
 continuation, hence the principle of monodromy.
 
 In fact, for any $\Gamma: [a,b]\times [0,1]\rightarrow S$ as in
 \lemref{lem-separated}, the inverse image
 $\Gamma^{\ast}\mathcal{F}$ is locally constant, hence constant and 
 canonically isomorphic to the
 constant sheaf attached to
 $\mathcal{F}_{x_a}$. Therefore the extension $f^\gamma$ of any 
 $f_{x_a}\in \mathcal{F}_{x_a}$ along any
 path $\gamma$ exists, and the value at the other extremity 
 $x_b=\gamma(b)$ depends only on the
 \emph{homotopy class} of $\gamma$.

  (2) When $S$ is a complex manifold, the structure sheaf
 $\mathcal{O}_S$ satisfies the principle of unique continuation, hence
 the principle of monodromy.
\end{exa}


\begin{para}
 Let $S$ be a topological space, connected and locally arcwise 
 (or simply) connected,
 and $\mathscr{F}$ a locally constant abelian sheaf on $S$.
 We fix a point $s\in S$, and denote by $\pi_1(S,s)$ the fundamental
 group based at $s$.\footnote{to remove any ambiguity, let us say that we
 adopt Deligne's convention: the composition in $\pi_1(S,s)$
 is induced by the juxtaposition of loops in the reverse order. As 
 such, $\pi_1(S,s)$ acts \emph{on the right} on the
 pointed universal covering.}
 To any loop $\gamma\colon [0,1]\rightarrow S$ based at $s$, let us associate
 the so-called {\it monodromy} along $\gamma$, defined by the composite
 \begin{equation*}
  \mathscr{F}_s\stackrel{\sim}{\longrightarrow}(\gamma^{\ast}\mathscr{F})_0
   \stackrel{\sim}{\longrightarrow}\Gamma([0,1],\gamma^{\ast}\mathscr{F})
   \stackrel{\sim}{\longrightarrow}(\gamma^{\ast}\mathscr{F})_1
   \stackrel{\sim}{\longrightarrow}\mathscr{F}_s.
 \end{equation*}
 By \examref{lem-homotopy} (1), the monodromy
 
 $\mathscr{F}_s\xrightarrow{\sim}\mathscr{F}_s$
 depends only on the class of $\gamma$ in
 $\pi_1(S,s)$,
 hence gives rise to a left $\Z[\pi_1(S,s)]$-module structure on 
 $\mathscr{F}_s$.
 This construction yields an equivalence of the categories
 \begin{equation*}
  \left\{\textrm{locally constant sheaves on} \; S\right\}
   \stackrel{\sim}{\longrightarrow}
   \left\{\textrm{left\ }\Z[\pi_1(S,s)]\textrm{-modules}\right\}\;:
 \end{equation*}
  giving a locally constant sheaf amounts to giving its value at $s$
 together with the monodromy action.
\end{para}
