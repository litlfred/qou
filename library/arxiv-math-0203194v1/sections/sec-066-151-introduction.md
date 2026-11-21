---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-066-151-introduction
section_title: "Introduction."
section_number: 15.1
pages: 145-148
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.984
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
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
