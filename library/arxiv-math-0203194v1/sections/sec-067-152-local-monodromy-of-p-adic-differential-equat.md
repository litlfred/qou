---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-067-152-local-monodromy-of-p-adic-differential-equat
section_title: "Local monodromy of $p$-adic differential equations. Outline of Christol-Mebkhout theory."
section_number: 15.2
pages: 148-150
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.988
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::3.2}

\begin{para}\label{para::3.2.1} Let $K$ be a complete subfield of
 $\C_p$. We assume for simplicity that the restriction of the $p$-adic 
valuation to $K$ is discrete. 

The Robba $K$-algebra at `infinity' is 
 \begin{equation*}
\mathcal{R}=\mathcal{R}_{z,K}= \{K\text{-analytic functions on some }
 \mathcal{C}(]1,r[)\}.
\end{equation*}
 Endowed with $\partial = zd/dz$, this is a differential (integral)
 $K$-algebra. Although it is not simple as a differential algebra (there
 are many non-trivial differential ideals), it has the following useful
 property, which often allows one to replace $\mathcal{R}$ by its
 fraction field $Q(\mathcal{R})$ (\cf \cite{andre:_repres_bessel}.): 

\begin{quote}
 {\it any $\mathcal{R}[\partial]$-module $M$ which is of finite
 presentation over $\mathcal{R}$ is free over $\mathcal{R}$.} 
\end{quote}
 In the sequel, we simply refer to such an $M$ as a
 {\it differential module} over $\mathcal{R}$.
\end{para}

\begin{para}\label{para::3.2.2} For any $\rho >1$ sufficiently close to $1$,
 let us denote by $R(M,\rho)$ the infinimum of $\rho$ and the maximal
 radius $R$ such that $M$ is solvable (= has a basis of analytic
 solutions) in $\matheur{D}(t_\rho, R^-)$.

 One says that  $M$ is  {\it solvable} (at the inner boundary), if  
 $\displaystyle\lim_{\rho \to 1^+}R(M,\rho) = 1$ 

 \noindent(this is essentially Dwork's condition, except that $R(M,1)$
 itself is not defined.)
\end{para}

\begin{para}\label{para::3.2.3} A useful criterion (which goes back the
 Dwork's early studies) for $M$ being solvable is the existence 
 of a Frobenius structure. 

 Let $\sigma$ be an automorphism of $K$ inducing $t\mapsto
 t^{p^f}$ in characteristic $p$, and let $\varphi_f$ be the
 $\sigma$-linear endomorphism of $\mathcal{R}$ defined by $z\mapsto
 z^{p^f}$.

 One says that $M$ {\it has a Frobenius structure} if $\varphi_f^\ast
 M\cong M $. In what follows, the particular choice of such an
 isomorphism is irrelevant.

 \medskip\noindent
 {\it Example.} Let
 $M_{\nu,\pi}=\mathcal{R}/\mathcal{R}B_{\nu,\pi}$ be the differential
 module over $\mathcal{R}$ attached 
 to the normalized Bessel operator. It turns out that, up to isomorphism,
 $M_{\nu,\pi}$ does not depend on $\nu\in \Z_p$ 
 \cite{andre:_repres_bessel}. Choosing $\nu=0$ for instance, the existence of a
 Frobenius structure is known by the interpretation of $M_{\nu,\pi}$ in 
 terms of Kloosterman sums \cite{bfapfota} (in fact, for any $\nu \in \Q\cap
 \Z_p$, there is a relation to twisted Kloosterman sums, and a Frobenius
 structure has a geometric interpretation, \cf \cite{berthelot84:_cohom_dwork}).
\end{para}

\begin{para}\label{para::3.2.4} We know turn to $p$-adic slopes\footnote{which
 should not be confused with the so-called slopes of Frobenius which
 measure the $p$-adic size of a fixed Frobenius structure (when it
 exists); a unit-root $F$-crystal corresponding to the case of Frobenius
 slope zero.}, as defined by G. Christol and Z. Mebkhout.

\begin{itemize}
 \item A solvable $M$ is of {\it greatest slope} $\lambda \in
       [0,\infty[$ if $R(M,\rho) = \rho^{1-\lambda}$ for $\rho $
       close to $1$.
 \item $M$ is {\it purely of slope} $\lambda$ if any non-zero 
       solution at $t_\rho$ has radius of convergence $\rho^{1-\lambda}$ for
       $\rho $ close to $1$.
\end{itemize}
\end{para}

\begin{thm}\label{thm::3.2.5} Any solvable $M$ has a decreasing
 filtration $M_{>\lambda}$ such that $Gr_\lambda\; M$ is free and 
 purely of slope $\lambda$.  
\end{thm}
\par \noindent \cf \cite{sltdldedp3}. Following Christol-Mebkhout, one
defines the {\it $p$-adic Newton polygon} 
(at infinity) $NP_\infty$: the horizontal length of the segment of slope
$\lambda$ is  $rk \;Gr_\lambda\; M $.  In particular, the greatest slope
of $M$ in the above sense is the greatest slope of $NP_\infty$ in the
usual sense. The height of $NP_\infty$ is called the $p$-adic
irregularity of $M$. 

A solvable module $M$ is called {\it tame} (or $p$-adically regular) if
the only finite slope of $NP_\infty$ is zero. 
This amounts to say that $M$ satisfies the Robba condition of
\ref{para::3.1.5}: $R(M,\rho)=\rho$ when $\rho\to 1^+$.

\medskip One of the main results in the Christol-Mebkhout theory is
(\cite{sltdldedp3}): 
 
\begin{thm}\label{thm::3.2.6}
 $NP_\infty$ has integral vertices. 
\end{thm}
 
\par \noindent  A useful complement in the computation of $NP_\infty$
is given by (\cite{andre:_repres_bessel}):

\begin{lem}\label{lem::3.2.7} Assume $M$ comes from a differential module
 over the subring of $(K\cap \ovl{\Q})((\frac{1}{x}))$ consisting of
 convergent series in  $\mathcal{C}(]1,\infty[)$. Then the $p$-adic
 greatest slope $\lambda$ is $\leq$ than the greatest formal slope
 $\lambda_\infty$.
\end{lem}

 \noindent
 {\it Example.} It can be shown (using \ref{thm::3.2.8} below) that the
 Bessel module $M_{\nu,\pi}$ is not tame; \ref{thm::3.2.6} and
 \ref{lem::3.2.7} then leave only two possibilities for 
 $NP_\infty$, and it turns out that both occur  (\cf
 \cite{andre:_repres_bessel}).


 \begin{figure}[h]
  \begin{picture}(300,125)(0,-25)
   \put(0,0){\line(1,0){40}}
   \put(40,0){\line(2,1){40}}
   \put(40,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(60,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,20){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,20){\line(0,1){60}}
   \put(55,20){\makebox(0,0)[r]{{\footnotesize $\lambda=1/2$}}}
   \put(40,-20){\makebox(0,0)[c]{$p=2$}}

   \put(200,0){\line(1,0){40}}
   \put(240,0){\line(1,1){40}}
   \put(240,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(260,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(280,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(280,20){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(280,40){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(280,40){\line(0,1){40}}
   \put(255,25){\makebox(0,0)[r]{{\footnotesize $\lambda=1$}}}
   \put(240,-20){\makebox(0,0)[c]{$p>2$}}
  \end{picture}
  \caption{}
 \end{figure}
 \newpage
 \noindent
 As for the converse of Robba's criterion (\cf \ref{para::3.1.5}), one 
 has (\cf \cite{sltdldedp2}): 
\begin{thm}[$p$-adic local monodromy theorem, tame
 case]\label{thm::3.2.8}
 Assume $M$ has a Frobenius structure\footnote{there is a more 
 general version without Frobenius structure, in which one encounters 
 some trouble with the problem of small divisors. The existence of a
 Frobenius structure simplifies the statement, if not the proof, since
 it implies a priori that if $p$-adic exponents exist, they are
 rational, hence non-Liouville.}, and is purely of slope zero. Then 
 $M$ is an iterated extension of rank one differential modules of type
 $\partial-\alpha\;$, $\alpha\in \Q\cap \Z_p$ (called the $p$-{\rm adic
 exponents} of $M$).
 
 With respect to the conclusion about the rationality of the $p$-adic
 exponents, this result may be seen as a $p$-adic analogue of
 Grothendieck's $\ell$-adic local monodromy theorem for tame $\ell$-adic
 coefficients.
\end{thm}
The result, if not its proof, is closely related to the fact that a tame
(= of degree prime to $p$) Galois \'etale finite 
covering of any annulus $\mathcal{C}$ is Kummer (the tame algebraic
fundamental group of $\mathcal{C}$ is $\widehat{\Z}'(1)$, where the 
dash means as usual that the $p$-component is omitted,
\cf \cite{ecfnas}). The relationship will appear more clearly below.

\begin{para}\label{para::3.2.9} Let us return to our original differential
 equation $(\ast)$. Let us assume that the only singularities at finite
 distance are in $\matheur{D}(0,1^+)$.  Let us 
 also assume that $(\ast)$ satisfies Dwork's condition (so that the
 associated differential module over $\mathcal{R}$ is solvable), and that
 the formal exponents at $\infty$ are rational. Then the $p$-adic
 behavior of $(\ast)$ in a small punctured disk $\matheur{D}(\infty,
 \epsilon)^\ast$ centered at $\infty$ is dictated by the formal behavior
 (\cf \ref{para::3.1.5}), while the $p$-adic behavior in a thin annulus
 $\mathcal{C}(]1,r[)$ is predicted by Christol-Mebkhout theory. However,
 in the intermediate region $\mathcal{C}([r,1/\epsilon])$, nothing seems
 to be known.

 We shall return to this problem in 3.5. 
\end{para}
