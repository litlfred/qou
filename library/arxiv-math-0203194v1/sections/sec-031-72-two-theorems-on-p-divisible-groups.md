---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-031-72-two-theorems-on-p-divisible-groups
section_title: "Two theorems on $p$-divisible groups."
section_number: 7.2
pages: 76-79
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.946
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:2.2} 

\begin{para}\label{para:2.2.1}
 A considerable amount of work has been
 devoted to $p$-divisible groups and their 
 applications to the $p$-adic study of abelian varieties and their local
 moduli. Among the pioneers, let us mention: Barsotti, Tate, Serre,
 Grothendieck, Lubin, Messing...


 In the sequel, we shall outline the main concepts and results of the
 Rapoport-Zink theory of period mappings for $p$-divisible groups,
 emphasizing the analogy with the complex case. We refer to their book
 \cite{psfpg} for details and proofs. We shall also emphasize the
 relation to differential equations, which does not appear in
 \cite{psfpg}.

 The whole theory relies upon three basic theorems on $p$-divisible
 groups and their Dieudonn\'e modules, which we shall recall below:


 \begin{enumerate}
  \item the rigidity theorem for $p$-divisible groups up to isogeny,
  \item the Serre-Tate theorem, and
  \item the Grothendieck-Messing theorem,
 \end{enumerate}

 \noindent
 which deal with infinitesimal deformations of $p$-divisible groups.
\end{para}

\begin{para}\label{para:2.2.2} Let $\mathfrak{v}$ be a complete discrete
valued ring $\mathfrak{v}$ of mixed characteristic $(0,p)$. Let 
$\Nil_\mathfrak{v}$ denote the category of locally noetherian 
$\mathfrak{v}$-schemes $S$ on which $p$ is locally nilpotent.  For any
$S$ in $\Nil_\mathfrak{v}$, the ideal of definition 
$\mathcal{J}=\mathcal{J}_{S_{\mathrm{red}}}$ of the closed subscheme $S_{\mathrm{red}}$ 
(of characteristic $p$) is locally nilpotent.
\end{para}

\begin{thm}[Rigidity theorem for $p$-divisible groups up to isogeny]
 \label{thm:2.2.3}
 
 Every homomorphism
 $\;\ovl{\rho}:\;\Lambda\times_S S_{\mathrm{red}} \rightarrow \Lambda'\times_S
 S_{\mathrm{red}}$ of $p$-divisible groups up to isogeny admits a unique lifting
 $\rho: \Lambda \rightarrow \Lambda'$. Moreover, $\rho$ is a
 quasi-isogeny if $\ovl{\rho}$ is.
\end{thm}

\begin{proof}
 (following an argument of V. Drinfeld). We may assume that $S$ is
 affine, and that $\mathcal{J}$ is nilpotent. Then the connected part
 ${\hat\Lambda'}$ is a formal Lie group, hence there is a power $p^n$ of
 $p$ such that for any affine $S$-scheme $S'$, ${\hat\Lambda}'(S')$ is
 killed by $[p^n]$ (in fact if $\mathcal{J}^{r+1}=0$ on $S$, one can take
 $n=r^2$).

 We observe that $\Ker(\Lambda'(S')\rightarrow
 \Lambda'(S'_{\mathrm{red}}))= {\hat\Lambda}'(S')$. We have
 \begin{align*}
 &\Ker(\Hom(\Lambda(S') ,
 \Lambda'(S'))\rightarrow \Hom(\Lambda(
 S'_{\mathrm{red}}) , \Lambda'(S'_{\mathrm{red}}) )\\
 =&
 \Hom (\Lambda(S') ,\Ker(\Lambda'(S')
 \rightarrow \Lambda'(S'_{\mathrm{red}}))) 
 \end{align*}
 which is zero because $\Ker(\Lambda'(S')\rightarrow
 \Lambda'(S'_{\mathrm{red}})$ is killed by $[p^n]$ while $\Lambda$ is
 $p$-divisible.

 \noindent This implies the injectivity of
 $\qisog_S(\Lambda , \Lambda') \rightarrow 
 \qisog_{S_{\mathrm{red}}}(\Lambda\times_S S_{\mathrm{red}} ,
 \Lambda'\times_S S_{\mathrm{red}}) $ (taking into account the fact that 
 $\Hom(\Lambda( S'_{\mathrm{red}}), \Lambda'(S'_{\mathrm{red}}) )$ is
 torsion-free).

 \noindent For the surjectivity, let us first show that for any
 ${\ovl{f}}\in \Hom(\Lambda(S'_{\mathrm{red}}),
 \Lambda'(S'_{\mathrm{red}}))$, there is 
 a lifting $g\in \Hom(\Lambda(S'), \Lambda'(S'))$ of $p^n {\ovl{f}}$. For
 any $x\in \Lambda( S')$, let $\ovl{x}$ denote its image in $\Lambda(
 S'_{\mathrm{red}})$. Since $\Lambda'$ is formally smooth,
 ${\ovl{f}}({\ovl{x}})$ 
 admits a lifting $y\in \Lambda'(S')$.  Since
 $\Ker(\Lambda'(S')\rightarrow \Lambda'(S'_{\mathrm{red}}))) $ is killed
 by $p^n$, 
 $g(x):=[p^n] y$ is well-defined. This construction provides the desired
 lifting $g$.

 It remains to show that $g$ is an isogeny if
 $\ovl{f}$ is. Let $\ovl{f}'$ be a quasi-inverse of $\ovl{f}$
 ($\ovl{f}'\ovl{f}=[p^m]$), and $g'$ be a lifting of $p^n\ovl{f}'$. Then
 $g'g=[p^{2n+m}]$ by unicity of liftings. Thus $g$ is an epimorphism, and
 the subscheme $\Ker g$ of $\Ker [p^{2n+m}]$ is finite over $S$. On the
 other hand, $\Lambda$ is flat over $S$ and the fibers of $g'$ are flat
 (being isogenies). The criterium of flatness fiber by fiber
 \cite[11.3.10]{ega44} implies that $g'$ is flat, and we conclude that
 it is an isogeny.
\end{proof}

Let us observe that there is variant of both the statement and the
proof of \ref{thm:2.2.3} for abelian schemes, instead of $p$-divisible groups. 

 The next theorem asserts that deforming an abelian scheme of
 characteristic 
 $p$ is equivalent to deforming its $p$-divisible group. For any $S $ in
 $\Nil_\mathfrak{v}$, let $\Def_{p\text{-div}}(S)$ be the category of
 triples $(\ovl{A},\Lambda, \epsilon)$ consisting of an abelian scheme
 over $S_{\mathrm{red}}$, a $p$-divisible group $\Lambda$ over $S$ and an
 isomorphism $\epsilon: \ovl{A}[p^\infty]\cong \Lambda\times_S S_{\mathrm{red}}$.

\begin{thm}[The Serre-Tate theorem]\label{thm:2.2.4}
 The functor
 \begin{equation*}
  A\;\mapsto \;(A_{\mathrm{red}},\;\Lambda=A[p^\infty],
   \;\epsilon: A_{\mathrm{red}}[p^\infty]\cong \Lambda\times_S S_{\mathrm{red}})
 \end{equation*}
 induces an equivalence of categories between the
 category of abelian schemes over $S$ and the category
 $\Def_{p\text{-div}}(S)$.
\end{thm}


We again follow Drinfeld's argument \cite{copsr}, \cf also \cite{slm}.
We may assume that $S$ is affine and that
$\mathcal{J}^{n+1}=0$. We begin with the full faithfulness: given a
homomorphism $f^\infty: A[p^\infty]\rightarrow B[p^\infty]$ such that
$f^\infty$ $\pmod{\mathcal{J}}$ comes from a homomorphism $\ovl{f} :
A_{\mathrm{red}}\rightarrow B_{\mathrm{red}}$ of abelian schemes over $S_{\mathrm{red}}$, we have
to show that there exists a unique homomorphism $f: A\rightarrow B$
compatible with $f^\infty$ and $\ovl{f}$. The unicity follows from the
injectivity of $\Hom(A,B)\rightarrow \Hom(A_{\mathrm{red}},B_{\mathrm{red}})\;$
(\ref{thm:2.2.3}). Furthermore, \ref{thm:2.2.3} shows the existence of a
homomorphism $g$ 
compatible with $\;p^nf^\infty$ and $p^n\ovl{f}$. To show the existence
of an $f$ such that $g=p^nf=f\circ [p^n]$, the point is to show that $g$
kills $A[p^n]$, which can be seen on $g^\infty$.


For the essential surjectivity, we have to construct an abelian scheme
$A$ over $S$ compatible with a given datum $(\ovl{A},\Lambda, \epsilon)$
in $\Def_{p\text{-div}}(S)$.  By unicity of liftings, it suffices to do so
locally on $S$.  hence we may assume that $S$ is affine, and choose an
abelian scheme $A'$ over $S$ and an isogeny $A'_{\mathrm{red}}\rightarrow
\ovl{A}$. By the above argument, $p^n$ times the given isogeny
$A'_{\mathrm{red}}\rightarrow \ovl{A}$ lifts to a (unique) isogeny
$e:\;A'[p^\infty ]\rightarrow \Lambda$ of $p$-divisible groups over
$S$. Its kernel is a finite locally free subgroup scheme of $A'$, and we
can form the abelian scheme $A'':=A'/\Ker e$. The isogeny $A''[p^\infty
]\rightarrow \Lambda$ induced by $e$ is an isomorphism
$\pmod{\mathcal{J}}$, hence is an isomorphism.

\begin{para}\label{para:2.2.5} In the sequel, we shall have to deal
 occasionally with $p$-divisible groups over formal schemes rather 
than over schemes. Our formal schemes $\mathfrak{X}$ will be adic,
locally noetherian; hence there is a largest ideal of definition
$\mathcal{J}\subset \mathcal{O}_{\mathfrak{X}}$, and
$\mathfrak{X}=\liminj \;{\mathfrak{X}}_n\;,\;{\mathfrak{X}}_n =
\Spec(\mathcal{O}_{\mathfrak{X}}/\mathcal{J}^{n+1})\;\;
({\mathfrak{X}}_{\mathrm{red}}={\mathfrak{X}}_0)\;$.

A $p$-divisible group $\Lambda$ over $\mathfrak{X}$ will be an inductive
system of $p$-divisible groups $\Lambda_n$ over $\mathfrak{X}_n$ such
that $\Lambda_{n+1}\times_{{\mathfrak{X}}_{n+1}}{\mathfrak{X}}_n\cong
\Lambda_n$.

\newpage
