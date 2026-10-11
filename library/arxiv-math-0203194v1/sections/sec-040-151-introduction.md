---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-040-151-introduction
section_title: "Introduction."
section_number: 15.1
pages: 145-152
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.988
---
\label{sub::3.1}

\begin{para}\label{para::3.1.1} Let us briefly review some well-known facts
 about singularities of ordinary linear differential equations. For
 concreteness, we consider a differential equation   

 \begin{equation}
  \alpha_\mu(z) \partial^\mu y + \cdots + \alpha_0 (z)
   y =0,\;\; \partial=z\frac{d}{dz}, \tag{$\ast$}
 \end{equation}
 with polynomial coefficients $\alpha_i(z)$, and concentrate on
 phenomena at infinity.
\end{para}

\begin{para}\label{para::3.1.2}  We begin the discussion with the formal
 setting. One defines the formal Newton polygon at $\infty$,
 $\widehat{NP}_\infty$ to be the convex hull of $\{(X\leq i,Y\geq \deg_z
 \alpha_0 -\deg_z \alpha_i )\}$ in the real 
 plane. Its `height'\footnote{the 
 height is the difference between the $Y$-coordinate of the highest 
 vertex and the $Y$-coordinate of the lowest vertex.}
 is called the (formal) irregularity of $(\ast)$ at
 $\infty$. The equation is called regular at $\infty$ if the
 irregularity is $0$, \ie if the only finite slope is $0$.

\medskip It is known that $(\ast)$ has a basis of `formal' solutions of
 the form 

\begin{equation*}
 \hat y=\sum {\hat u_i}\Bigl(\frac{1}{z}\Bigr) z^{-{\hat e}_i}(\log^{k_i}
  z) e^{P_i(z^{1/\mu !})},
\end{equation*}
 where the $P_i$'s are polynomials, and the ${\hat u_i}$ are just formal
 power series in $\frac{1}{z}$. The degree of the `ramified polynomials'
 $P_i(z^{1/\mu !}) $ actually corresponds to the slopes of $\widehat 
{NP}_\infty$. The ${\hat e}_i$'s are called the formal or Turrittin
 exponents; they can be computed algebraically.

 \medskip
 \noindent {\it Example.} Let us illustrate these notions with the {\it
 Bessel equation}
 \begin{equation*}
  (B)_{\nu}:\;\;\;\;(\partial^2  + (z^2  - \nu^2))y=0 
 \end{equation*}
 A basis of `formal solutions' at $\infty$ is given by
 \begin{equation*}
  \hat y_\pm= z^{-1/2}e^{\pm\sqrt{-1}z}.
   {}_2F_0\Bigl(\frac{\nu +1}{2},\frac{-\nu +1}{2}; \frac{\mp
   \sqrt{-1}}{2z}\Bigr), \quad {\hat e}_i=1/2,
 \end{equation*}
 and $\widehat{NP}_\infty$ is
 

 \begin{figure}[h]
  \begin{picture}(100,100)(0,0)
   \put(0,0){\line(1,0){40}}
   \put(40,0){\line(1,1){40}}
   \put(40,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(60,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,0){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,20){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,40){\makebox(0,0)[c]{{\small $\bullet$}}}
   \put(80,40){\line(0,1){40}}
  \end{picture}
  \caption{}
 \end{figure}
\end{para}

\begin{para}\label{para::3.1.3} {\it Complex-analytic setting}.  Solutions at
 any non-singular point $s$ (\ie a point in $\C^\times$ which is not a
 root of $\alpha_\mu$) converge up to the next singularity.

 Let ${\mathcal{C}}= \mathcal{C}(]r',r[) =\{z, \;r'<|z| < r\}$ be an
 annulus which contains no singularity. Using the fact the
 $\pi_1(\mathcal{C},s)\cong \Z$, it is classical to deduce that $(\ast)$
 has a basis of `analytic' solutions of the form

 \begin{equation*}
  y=\sum {u_i}\Bigl(\frac{1}{z}\Bigr) z^{-{e}_i} (\log^{k_i} z),
 \end{equation*}
 where the ${u_i}$ are Laurent series in $\frac{1}{z}$
 which converge in $\mathcal{C}$.
 The ${ e}_i$'s are called the analytic exponents.\footnote{in terms of
 differential systems, this amounts to the fact that a system
 $\partial Y = A Y$ on $\mathcal{C}$ has a fundamental solution matrix
 $Y$ of the form 
 $U.z^{-E}$, where $U$ is analytic in $\mathcal{C}$ and $E$ is constant (Fuchs
 normal form).}

 \medskip
 The relation between the $y$'s (analytic) and
 the $\hat y$'s (formal) is not straightforward. If $r=\infty$, the $\hat
 y$'s occur as asymptotic expansions of the $y$'s on suitable sectors,
 and the theory of multisummability/acceleration provides a kind of
 canonical inverse process (again on suitable sectors). If $\infty$ is a
 regular singularity, the $\hat u_i$ converge so that with $u_i=\hat u_i,
 e_i=\hat e_i$, the solutions $y$ and $\hat y$ coincide.

 \medskip
 \noindent {\it Example.} For the Bessel equation (say with non-integral
 parameter $\nu$ to simplify), one has a basis of solutions on
 $\mathcal{C}=\C^\times$ given by
  
\begin{equation*}
 y_\pm= z^{\pm\nu}\sum_0^\infty \;\frac{\;(-1)^n z^{2n }}{4^n n! (\pm\nu
  +1)_n}. 
\end{equation*}
 Moreover $e_i = \pm \nu$ (analytic exponents at $\infty = -$ analytic
 exponents at $0$); here we are `lucky', there are just two
 singularities, one of them is regular. In general, the computation of
 analytic exponents involves infinite determinants. Even in the
 so-called fuchsian case where there are only regular singularities, the
 computation of analytic exponents on an annulus which encloses several
 regular singularities is transcendental; e.g. the exponents of the
 differential equation of order two with solution
 ${}_2F_{1}(\frac{1}{2},\frac{1}{2},1;z^2)$, on an 
 annulus enclosing $0$ and $1$ but not $-1$ and
 $\infty$, are transcendental numbers:
 $\frac{\log(3\pm 2\sqrt 2)}{2\pi i}$\footnote{An independent
 solution is given by $i. \,{}_2F_{1}(\frac{1}{2}, \frac{1}{2}, 1;
 1-z^2)$, and in this basis, the local monodromy matrix 
 around $1$ (\resp $0$) is
 $\bigl(\begin{smallmatrix}1&0\\ -2&1\end{smallmatrix}\bigr)$
 (\resp $\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)$); the
 eigenvalues of the 
 monodromy around $\mathcal{C}$ are the eigenvalues of 
 $\bigl(\begin{smallmatrix}1&0\\-2&1\end{smallmatrix}\bigr)
  \bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)
  =\bigl(\begin{smallmatrix}-7&4\\-2&1\end{smallmatrix}\bigr)$, 
 \ie $3\pm 2\sqrt 2$.}.
\end{para}

\begin{para}\label{para::3.1.4}  {\it $p$-adic-analytic setting}.  The first
 problem one encounters when dealing with $p$-adic differential
 equations (\cf I.\ref{sub-r-and-unit-root}) is that the solutions at
 non-singular points have small radii of convergence in general, and do
 not converge up to the next singularity.
 
 \medskip
 \noindent {\it Example.}
 $\frac{d}{dz}y=y,\;  e^z=\sum \frac{z^n}{n!} $ converges only in
 $\matheur{D}(0,|\pi|^-)$, $\pi^{p-1}=-p$. 

 \medskip
 This problem leads one to normalize somehow the situation by postulating 

 \medskip\noindent {\it Dwork's condition: the radius of convergence of
 solutions of $(\ast)$ at a generic point\footnote{a generic point of
 modulus $\rho$ in the sense of Dwork is a point $t_\rho$ in a complete
 extension $\Omega$ of $K$ with $| t_\rho|=\rho$ and such that the disk
 $\matheur{D}_\Omega(t_\rho,\rho^-)$ does not contain any element of $K$.}
 $\;t_1$ of modulus $1$ is $\geq 1$}.

 \medskip
 \noindent {\it Example.} One `normalizes' Bessel's equation by the
 change of variable $ z\mapsto 2\pi\sqrt{-1} z$. The normalized 
 Bessel differential operator is then   
 \begin{equation*}
  B_{\nu,\pi} = \partial^2  - (4\pi^2 z^2 +\nu^2)  
 \end{equation*}
 which is solvable in the $p$-adic generic disk whenever $\nu \in \Z_p$.
\end{para}

\begin{para}\label{para::3.1.5} Let us now discuss problems at $p$-adic
 singularities, concentrating again on phenomena at infinity.

 \medskip\noindent $\bullet$ The first one is the problem of `small
 divisors': if some formal exponent $\hat e_i\in \Z_p$ (or rather some
 difference $\hat e_i -\hat e_j$) is a Liouville number, \ie very
 closely approximated by infinitely many rational integers, the formal
 power series $\hat u_i$ occuring in the formal solutions $\hat y$ may
 diverge, even in the regular case. Otherwise, the $\hat u_i$ 
 converge, even in the irregular case \cite{baldassarri82:_differ}.

 \medskip
 \noindent {\it Example.} if $\nu \in \Z_p$ is well-approximable by
 negative integers, $\sum_0^\infty \frac{(-1)^n z^{2n}}{4^n n! (\nu
 +1)_n}$ may diverge, although $0$ is a regular singularity of the
 Bessel equation.

\medskip\noindent 
 $\bullet$ Even if Liouville numbers do not show up (\eg if everything
 is defined over $\ovl{\Q}$) so that the $\hat u_i$'s converge, these
 series may not converge as far as one might expect (\eg in a unit disk
 under the Dwork condition). This subtle phenomenon occurs in the
 normalized Bessel case $B_{\nu,\pi}$ for $p=2$ (${}_2F_0(\frac{\nu
 +1}{2},\frac{-\nu +1}{2}; \frac{\pm 1}{4\pi z})$ do not converge up
 to the unit circle): there is an annulus $\mathcal{C}(]1,r[)$ such that
 neither $y_\pm$ nor $\hat y_\pm$ provide any information about the
 solutions of $B_{\nu,\pi}$ in $\mathcal{C}(]1,r[)$.

 In particular, the question arises whether there is a basis of solutions 

 \begin{equation*}
  \sum{u_i}\Bigl(\frac{1}{z}\Bigr) z^{-{e}_i}(\log^{k_i} z),
 \end{equation*}
 where the ${u_i}$ are Laurent series in $\frac{1}{z}$ which converge in
 such an annulus $\mathcal{C}(]1,r[)$. More generally, concerning the
 existence of a `$p$-adic Fuchs normal form': 

 \medskip\noindent 
 $\bullet$ Does there exist a basis of solutions of $(\ast)$ of the form 
 \begin{equation*}
  y=\sum {u_i}\Bigl(\frac{1}{z}\Bigr) z^{-{e}_i} (\log^{k_i} z),
 \end{equation*}
 where the ${u_i}$ are Laurent series which converge in
 a given annulus $\mathcal{C}(]r',r[)$?

 \medskip\noindent A necessary condition has been put forward by
 P. Robba: {\it for any $\rho\in ]r',r[$, the radius of convergence of
 the solutions at the generic point $t_\rho$ of modulus $\rho$ is $\geq
 \rho$} (in the variable $z$, not $1/z$).

 The problems are: to which extent is the converse true? What can be
 said if Robba's condition is not fulfilled?

 \medskip\noindent These questions have recently become almost complete
 answers thanks to the Christol-Mebkhout theory of $p$-adic slopes of
 differential modules over annuli.  
\end{para}


\subsection{Local monodromy of $p$-adic differential equations. Outline
 of Christol-Mebkhout theory.}\label{sub::3.2}

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


\subsection{Local monodromy of $p$-adic differential equations and
  Galois representations.}\label{sub::3.3}

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
