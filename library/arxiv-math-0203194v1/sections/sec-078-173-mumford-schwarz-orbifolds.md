---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-078-173-mumford-schwarz-orbifolds
section_title: "Mumford-Schwarz orbifolds."
section_number: 17.3
pages: 183-186
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.992
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::5.3}

\begin{para}\label{para::5.3.1} Our aim is to give a more geometric
 description of $p$-adic triangle groups, independent of the theory of
 monodromy of $p$-adic differential equations. This involves the notion
 of Mumford-Schwarz orbifold.
\end{para}

\begin{dfn}\label{def::5.3.2} A Mumford-Schwarz orbifold is a $p$-adic
 Schwarz orbifold such that there exists a finite 
Galois global orbifold chart $\ovl{S}' \to \P^1$, $\ovl{S}'$ being a
 Mumford curve.  
\hfill\break In other
words, it is the orbifold quotient of a Mumford curve $\ovl{S}'$ by a
 finite group of automorphisms $G$ such that $\ovl{S}'/G= \P^1$ and the
Galois covering $\ovl{S}' \to \P^1$ is ramified exactly above $0,
1,\infty$ with ramification index $e_0,e_1,e_\infty$ respectively.
\end{dfn}

\medskip\noindent According to \ref{pro::4.5.7}, one has an exact sequence
\begin{equation*}
1\to \pi_1^{\mathrm{temp}}(\ovl{S}',\ovl{s}')\to
 \pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty),\ovl{s}) \to G \to 1. 
\end{equation*}

\noindent On the other hand, because $\ovl{S}'$ is a Mumford curve,
$\pi_1(\ovl{S}',\ovl{s}')$ is a Schottky group embedded in 
$PGL_2(K) $, and the universal topological covering
$\widetilde{\ovl{S}'}$ can be 
identified with the set $\Omega\subset \P^1_{\C_p}$ of ordinary points
for $\pi_1(\ovl{S}',\ovl{s}')$. The subgroup  
$\Gamma$ of all liftings of the elements of $G \subset \Aut (\ovl{S}')$
in $PGL_2(K)$ is a subgroup of finite index inside 
the normalizer of
$\pi_1(\ovl{S}',\ovl{s}')$ in $PGL_2(K)$; it sits in an extension 

\begin{equation*}
 1\to \pi_1^{\mathrm{top}}(\ovl{S}',\ovl{s}')\to \Gamma \to G \to 1.
\end{equation*}
{\it Remark.} A Mumford-Schwarz orbifold is hyperbolic if and only if some (\resp every) curve $\ovl{S}'$
as above has genus $\geq 2$. 

\begin{pro}\label{pro::5.3.3} Let $ \mathcal{S}=(\P^1; (0,
 e_0), (1,e_1), (\infty, e_{\infty})) $ be a Mumford-Schwarz orbifold. Then the
 $p$-adic triangle group $\Delta_p(e_0,e_1,e_\infty)$ exists, and
 coincides with the discrete group $\Gamma\;$ (in particular, $\Gamma$
 does not depend on the choice of $\ovl{S}'/ \P^1$). Moreover, one has a
 commutative diagram
 
 \begin{equation*}
  \begin{CD}
   1 @>>> \pi_1^{\mathrm{temp}}(\ovl{S}',\ovl{s}') @>>>
  \pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty),\ovl{s}) @>>> G @>>> 1\\
  @. @VVV @VVV @VVV @.\\
  1 @>>>\pi_1^{\mathrm{top}}(\ovl{S}',\ovl{s}')@>>>
  \Delta_p(e_0,e_1,e_\infty)@>>> G @>>> 1
  \end{CD}
 \end{equation*}
 with surjective vertical maps and exact arrows.
\end{pro}

\begin{proof}
  Let us consider the $p$-adic uniformizing differential equation
 attached to the orbifold-covering $\widetilde{\ovl{S}'}\to
 \mathcal{S}(e_0,e_1,e_\infty)$ (3.6). It is fuchsian with singularities
 at $0,1,\infty$, and Riemann scheme
 \begin{equation*}
 \begin{pmatrix}
 0 &  1 & \infty \\
 &&&\\
 \frac{1}{2}(1+\frac{1}{e_0})&  \frac{1}{2}(1+\frac{1}{e_{1}})&
 \frac{-1}{2}(1+\frac{1}{e_{\infty}}) \\
 &&& \\
 \frac{1}{2}(1-\frac{1}{e_0})&  \frac{1}{2}(1-\frac{1}{e_{1}})&
 \frac{-1}{2}(1-\frac{1}{e_{\infty}})     
 \end{pmatrix} .
 \end{equation*}

 \medskip Multiplying solutions of this equation by  
 \begin{equation*}
 z^{\frac{1}{2}(-1+\frac{1}{e_0})}(z-1)^{\frac{1}{2}(-1+\frac{1}{e_1})}
 \end{equation*}
 transforms the equation into a (projectively equivalent) $p$-adic
 differential equation of hypergeometric type $ HGDE(a,b,c) $ with
 $1-c=\frac{1}{e_0},\;c-a-b=\frac{1}{e_1},\;
 \pm(a-b)=\frac{1}{e_\infty}$.  By \ref{pro::4.6.4}, the projective connection
 attached to $ HGDE(a,b,c) $ is the projective connection attached to to
 the projective representation given by the composed homomorphism
 $\pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty),\ovl{s})\to \Gamma \to
 PGL_2(K)$, which has discrete image. By \ref{pro::5.2.4}. (b), we
 conclude that 
 $\Delta_p(e_0,e_1,e_\infty)$ exists and coincides with $\Gamma$. The
 commutative diagram in the statement comes from \ref{pro::4.5.7}.
\end{proof}

\begin{para}\label{para::5.3.4} F. Kato calls the $p$-adic triangle groups
 which arise in this way ``$p$-adic triangle groups of Mumford type''
\cite{kato:_schwar_mumfor}. Inspired by F. Herrlich's study of automorphisms of
Mumford curves (using graphs of groups), he has developed
geometrico-combinatorial techniques to construct Mumford-Schwarz
orbifolds, and even a complete classification scheme, including a
description of $p$-adic triangle groups ``of Mumford type'' as explicit
amalgamated sums. As a by-product, he has proved the following
\end{para}

\begin{thm}[F. Kato]\label{thm::5.3.5} For $p= 2, 3$ and $5$, there are
 infinitely many hyperbolic Mumford-Schwarz orbifolds.  For $p>5$, there
 is none.
\end{thm}

\begin{para}\label{para::5.3.6} The following theorem explains how to obtains
 all $p$-adic triangle groups from $p$-adic triangle groups ``of Mumford
 type''.
\end{para}

\begin{thm}\label{thm::5.3.7} $\Delta_p(e_0,e_1,e_\infty)$ exists if and
 only if $\mathcal{S}(e_0,e_1,e_\infty)$ is a finite orbifold-covering
 of some Mumford-Schwarz orbifold
 $\mathcal{S}(e'_0,e'_1,e'_\infty)$. Moreover, the latter can be chosen
 in such a way that
 $\Delta_p(e_0,e_1,e_\infty)=\Delta_p(e'_0,e'_1,e'_\infty)$ as a subgroup
 of $PGL_2(\C_p)$.
\end{thm}

\begin{proof}
 (a) Assume that we have a finite orbifold-covering $h:
 \mathcal{S}\to \mathcal{S}'$ of a Mumford-Schwarz orbifold by a 
 Schwarz orbifold. The pull-back by $h$ of the hypergeometric projective
 connection $ HGPC(a',b',c') $ related to 
 $e'_0,e'_1,e'_\infty$ as above is the hypergeometric projective
 connection $HGPC(a,b,c) $ related to $e_0,e_1,e_\infty$. 
 Because $\mathcal{S}'$ is a Mumford-Schwarz orbifold, its uniformizing
 differential equation, hence $ HGPC(a',b',c') $, comes 
 from a representation of the temperate fundamental group, and it follows
 that so does $ HGPC(a,b,c) $. Moreover, the monodromy group of
 $HGPC(a,b,c) $ is a subgroup of finite index of the monodromy group of
 $HGPC(a',b',c') $, which is the discrete finitely generated group
 $\Delta_p(e'_0,e'_1,e'_\infty)$. Therefore the monodromy 
 group of $HGPC(a,b,c) $ is itself discrete finitely generated, and is
 $\Delta_p(e_0,e_1,e_\infty)$.  

 (b) Conversely, assume that $\Delta_p(e_0,e_1,e_\infty)$ exists. Let 
 $\Sigma \to \P^1$ be the ramified covering corresponding to the quotient 
 $\Delta_p(e_0,e_1,e_\infty)$ of
 $\pi_1^{\mathrm{orb}}(\mathcal{S},\ovl{s}) $. By 
 definition of $\Delta_p(e_0,e_1,e_\infty)$ as projective monodromy
 group, any quotient of two non-proportional solutions of 
 $HGDE(a,b,c)$ defines an \'etale map
 \begin{equation*}
 \tau: \;\Sigma \to \P^1_{\C_p}
 \end{equation*} which is equivariant under
 $\Delta_p(e_0,e_1,e_\infty)$.

 On the other hand, $\Delta_p(e_0,e_1,e_\infty)$ being
 a finitely generated discontinuous subgroup of $PGL_2(K)$ for some
 finite extension $K/\Q_p$, it admits a normal 
 subgroup of finite index which is a Schottky group $\Gamma$. Let
 $\Omega\subset \P^1_{\C_p}$ denote the set of ordinary 
 points for $\Gamma$. Since $\Delta_p(e_0,e_1,e_\infty)$ normalizes
 $\Gamma$, it preserves $\Omega$ and the quotient 
 $H=\Delta_p(e_0,e_1,e_\infty)/\Gamma$ is a group of automorphisms of the
 Mumford curve $\Omega/\Gamma$. We denote by $T$ 
 the quotient of this Mumford curve by $H$ (a smooth projective curve).

 We claim that
 \begin{equation*}
  \tau(\Sigma) \subset \Omega.
 \end{equation*}
 Indeed, otherwise $\tau$ would have a value $\tau(s)$ which is a limit
 point for $\Gamma$, \ie an accumulation point of an infinite sequence
 of points $\gamma_n(x)$, $x\in \P^1$. Since $\tau$ is \'etale, hence
 open, we may assume that $x\in \Im\,\tau$, say $x=\tau(t)$. By
 $\Gamma$-equivariance of $\tau$, we see that $\tau(s)$ is an
 accumulation point of the infinite sequence $\tau(\gamma_n(t))$. This
 contradicts the fact that the set $\{\gamma_n(t)\}$ is discrete in
 $\Sigma$ and that $\tau$ is \'etale (hence locally invertible around
 $s$).

 Next, being $\Delta_p(e_0,e_1,e_\infty)$-equivariant, $\tau$ induces an
 analytic map
 \begin{equation*}
  \ovl{\tau}: \, \Sigma/\Delta_p(e_0,e_1,e_\infty)=\P^1
   \to \Omega/\Delta_p(e_0,e_1,e_\infty)=T.
 \end{equation*}
 This map is necessarily algebraic and finite, and $T\cong \P^1$ (we
 normalize the latter isomorphism by imposing that
 $\ovl{\tau}(\{0,1,\infty\}\subset \{0,1,\infty\}$). Notice that because
 $\tau$ is $\Delta_p(e_0,e_1,e_\infty)$-equivariant, 
 it follows that
 \begin{equation*}
  \tau(\Sigma)= \Omega 
 \end{equation*} 
 and that $\tau$ is a finite \'etale covering (not a topological
 covering, unless $\Sigma=\Omega$). We have a cartesian 
 square 
 \begin{equation*}
 \begin{CD}
  \Sigma @>>> \Omega \\
  @VVV @VVV\\
  \P^1 @>>> \P^1
 \end{CD}
 \end{equation*}
 in which the vertical maps are Galois
 orbifold-coverings with group $\Delta_p(e_0,e_1,e_\infty)$, and define
 orbifold quotients $\mathcal{S}$ and $\mathcal{S}'$ of $\Sigma$ and
 $\Omega$ respectively. Since $\tau$ is \'etale, we see that
 $\mathcal{S}$ is actually a finite orbifold-covering of
 $\mathcal{S}'$. This forces $\mathcal{S}'$ to be a Schwarz orbifold
 (like $\mathcal{S}$), hence a Mumford-Schwarz orbifold by construction.
\end{proof}

\begin{cor}\label{cor::5.3.7}
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}  
  \item Assume that $\Delta_p(e'_0,e'_1,e'_\infty)$ is a $p$-adic
	triangle group ``of Mumford type''. Assume that
	$\Delta(e_0,e_1,e_\infty)$ is a subgroup of finite index of the
	corresponding ``complex'' triangle group
	$\Delta(e'_0,e'_1,e'_\infty)$. Then $\Delta_p(e_0,e_1,e_\infty)$ 
	exists, and can be realized as a subgroup of finite index of
	$\Delta_p(e'_0,e'_1,e'_\infty)$.
  \item If $\Delta_p(e_0,e_1,e_\infty)$ exists, and if the
	corresponding ``complex'' triangle group $\Delta(e_0,e_1,e_\infty)$ is
	maximal in its commensurability class of triangle groups, then
	$\Delta_p(e_0,e_1,e_\infty)$ is ``of Mumford type''.
 \end{enumerate}
\end{cor}
\begin{proof}
 (a) If $\Delta(e_0,e_1,e_\infty)$ is a subgroup of finite index of
 $\Delta(e'_0,e'_1,e'_\infty)$, there is a finite morphism
 $\P^1\to \P^1$, defined over a number field, which underlies a
 finite orbifold-covering $\mathcal{S}(e_0,e_1,e_\infty)\to
 \mathcal{S}(e'_0,e'_1,e'_\infty)$ in the complex sense, but also
 in the $p$-adic sense (for every embedding of the number field
 in $\C_p$). The assertion comes from the ``if'' part of the
 theorem.

 (b) If $\Delta_p(e_0,e_1,e_\infty)$ exists, then, similarly, by the
 ``only if'' part of \ref{para::5.3.6}, there is a finite
 morphism $\P^1\to 
 \P^1$ defined over a number field, which underlies a finite
 orbifold-covering $\mathcal{S}(e_0,e_1,e_\infty)\to
 \mathcal{S}(e'_0,e'_1,e'_\infty)$ in the $p$-adic sense, and
 also in the complex sense. Hence
 $\Delta(e_0,e_1,e_\infty)\subset \Delta(e'_0,e'_1,e'_\infty)$
 with equality if and only if
 $\mathcal{S}(e_0,e_1,e_\infty)=\mathcal{S}(e'_0,e'_1,e'_\infty)$.
\end{proof}

\begin{cor}\label{cor::5.3.8} There is no infinite $p$-adic triangle
 group for $p>5$.
\end{cor}
\begin{proof}
 This follows from \ref{thm::5.3.5} and \ref{para::5.3.6}.  
\end{proof}
