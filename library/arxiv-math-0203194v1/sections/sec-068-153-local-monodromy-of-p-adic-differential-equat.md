---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-068-153-local-monodromy-of-p-adic-differential-equat
section_title: "Local monodromy of $p$-adic differential equations and Galois representations."
section_number: 15.3
pages: 150-152
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.888
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::3.3}

\begin{para}\label{para::3.3.1} The differential sub-$K$-algebra 
 \begin{equation*}
  \mathcal{E}^{\dag} = \{\text{bounded $K$-analytic functions on some }
   \mathcal{C}(]1,r[)\}
 \end{equation*} 
 of bounded functions in $\mathcal{R}$ is actually a field. With the
 $p$-adic sup-norm, it is even a henselian field, with residue field
 $k((\frac{1}{z}))$ (where $k$ stands for the residue field of $K$).
 Hence any Galois extension $k((\frac{1}{z'}))/k((\frac{1}{z}))$ gives
 rise to an unramified Galois extension
 $\mathcal{E}^\dagger_{z',K'}/\mathcal{E}^\dagger_{z,K}$ (and, further,
 to a finite integral extension
 $\mathcal{R}_{z',K'}/\mathcal{R}_{z,K}$).
\end{para}

\begin{para}\label{para::3.3.2} In I.\ref{para-unit-root}, we have
 reviewed Katz' functor 
 from representations of fundamental groups of algebraic curves in
 characteristic $p$ to unit-root $F$-(iso)crystals. This construction has
 a local analogue, and one has the following theorem of N. Tsuzuki 
 \cite{tsuzuki98:_finit_f}:
\end{para}

\begin{thm}\label{thm::3.3.3} There is a natural equivalence of
 categories between the category of continuous $Q(W(k))$-linear 
 representations of
 $\Gal(k((\frac{1}{z}))^{\mathrm{sep}}/k((\frac{1}{z})))$ with 
 {\rm finite inertia} and the category of overconvergent unit-root
 $F$-isocrystals on $\Spec\;k((\frac{1}{z}))$.
\end{thm}

\par\noindent In particular, disregarding the precise Frobenius
structure, one gets a functor
\begin{equation*}
 \left\{\begin{matrix}
    \text{$p$-adic representations of $k((\frac{1}{z}))$}\\
    \text{with finite inertia}
   \end{matrix}
   \right\}
   \to
   \left\{\begin{matrix}
      \text{differential modules over $\mathcal{E}^\dagger$}\\
      \text{with Frobenius structure}
     \end{matrix}
     \right\}
\end{equation*}
hence, loosing even more structure, a functor

\begin{align*}
 &\bigl\{\begin{matrix}
	 \text{finite $p$-adic representations of $k((\frac{1}{z}))$}
	\end{matrix}\bigr\}\\
 &\qquad\qquad\qquad \to
 \left\{
 \begin{matrix}
  \text{differential modules over $ \mathcal{R}_{z,K}$ with Frobenius
  }\\
  \text{structure, which become trivial over some 
  }\\
  \text{finite extension $\mathcal{R}_{z',K'}$ of $\mathcal{R}_{z,K}$ as above}
 \end{matrix}
 \right\}
\end{align*}

\begin{dfn}\label{def::3.3.4} (R. Crew) A differential module $M$ over
$\mathcal{R}$ is {\rm quasi-unipotent} if there is a Galois extension
$k((\frac{1}{z'}))/k((\frac{1}{z}))$ such that after tensoring with the
corresponding finite extension $\mathcal{R}_{z',K'}$ of
$\mathcal{R}_{z,K} $, $M$ becomes an iterated extension of trivial
differential modules over $\mathcal{R}_{z',K'}$.

 There is an
 extensive work by Crew, S. Matsuda and Tsuzuki relating Galois
 representation theory and ramification theory of $k((\frac{1}{z})))$ and
 Christol-Mebkhout theory in the case of quasi-unipotent differential
 modules, \cf \cite{ceiatsc}.  In particular, they 
 establish a dictionary between Swan conductor and $p$-adic irregularity
 (in the above sense), break decomposition (in the sense of Katz) and
 $p$-adic slope decomposition... 
\end{dfn}

 \medskip\noindent {\it Examples.} (i) A {\it tame} module $M$
 with Frobenius structure is quasi-unipotent by \ref{thm::3.2.8}; indeed, it
 suffices to take a Kummer extension
 $k((\frac{1}{z^{1/n}}))/k((\frac{1}{z}))$. 

 (ii) $\mathcal{R}/\mathcal{R}(\partial-\pi z)$ is
 quasi-unipotent: take an Artin-Schreier extension defined by
 $z'-z^{\prime p}=z$.

 (iii) $p$-adic Bessel $M_{\nu,\pi}$ for odd $p$: a cyclic
 extension of $k((\frac{1}{z}))$ of degree $2p$ of 
 suffices. Indeed, it suffices to deal with the case $\nu = 1/2$ (\cf
\ref{para::3.2.3}). Then $(\frac{1}{z})^{\pm 1/2}.e^{\pm 2\pi z}$ is a
basis of solutions, and one reduces to the previous two examples.

\begin{coj}[Crew's $p$-adic local monodromy conjecture]\label{coj::3.3.5}
 Any differential module $M$ over $\mathcal{R}$, with Frobenius structure, is
 quasi-unipotent.
\end{coj}

This conjecture, which can be seen as a $p$-adic analogue of
Grothendieck's $\ell$-adic local monodromy theorem for wild $\ell$-adic
coefficients, and as a {\it non-abelian} extension of
\ref{thm::3.2.8} to the wild case, has now been solved
\cite{andre01:_filtr_hasse_arf}.
The proof relies heavily 
on theorems \ref{thm::3.2.5}, \ref{thm::3.2.6}, \ref{thm::3.2.8}.

\medskip\noindent A crucial test \cite{andre:_repres_bessel}, which is
at the origin 
of the solution, is the case of the {\it diadic} normalized Bessel
module $M_{\nu,2}$ (this test was suggested by Mebkhout as a potential
counterexample). This example provides a typical non-abelian instance of
\ref{coj::3.3.5}:

\begin{thm}\label{thm::3.3.6} For $K=\Q_4$, the normalized Bessel
 differential $\mathcal{E}^\dagger_{x,K}$-module $M$ is 
 quasi-unipotent.
\end{thm}

\medskip More precisely, let $E$ be the supersingular elliptic curve
 over $\F_4$ with affine equation 
  $Y^2+Y=X^3+\omega,\;$ ($\omega^3=1, \omega\neq 1$); then the covering
 $E\to E/\Aut(E)\cong \P^1\;$ is wildly totally ramified at the origin
 of $E$, and defines an unramified Galois extension of
 $\mathcal{E}^\dagger_{x,K}$ of degree $24$, with group $\Aut(E)\cong
 SL_2(\Z/3\Z)$, which contains all solutions of $M$. The underlying
 Galois representation of $G_{\F_4((1/z))}$ corresponds to the action of
 $\Aut(E)$ on $\mathrm{H}^1_{\mathrm{cris}}(E)$.
