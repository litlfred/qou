---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-006-31-basics-on-formal-gaussian-integration
section_title: "Basics on formal Gaussian integration"
section_number: 3.1
pages: 9-18
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.97
---
\label{sub.prelim}

In this section, we review the basic properties of formal Gaussian integration,
which is a combinatorial analogue of integration of analytic functions. This theory
was introduced and studied in detail in~\cite{AarhusII}, where it was used to
define a universal perturbative finite type invariant of rational homology 3-spheres,
and to identify it with the trivial connection contribution of Chern--Simons
perturbation theory. 

As a warm-up, the formal Gaussian integral of a monomial $x^n$ in one variable
with respect to the quadratic form $\lambda \neq 0$ is defined by
\bea
\label{formalG1}
\left\langle x^n \right\rangle_{x,\lambda}
\= \begin{cases}
  \lambda^{-n/2} (n-1)!! & n \,\, \text{even} \\
  0 & n \,\, \text{odd} \,.
\end{cases}
\eea
When $\lambda>0$, then the above bracket equals to a normalized Gaussian integral
\be
\left\langle x^n \right\rangle_{x,\lambda} \=
\frac{\int_\BR e^{-\frac{1}{2}\lambda x^2} x^n \, dx}{
  \int_\BR e^{-\frac{1}{2}\lambda x^2} \, dx} \,,
\ee
explaining the naming of formal Gaussian integration. The formal Gaussian integration
can be extended by linearity to $\langle f(x) \rangle_{x,\lambda}$ for any polynomial
$f(x)$, or even further to a power series $f(x) = \sum_{n \geq 0} a_n x^n$ whose
coefficients tend to zero in a local ring (such as the ring
$\BQ\llbracket \hroot \rrbracket$).

The formal Gaussian integral~\eqref{formalG1} has a multivariable extension given
in Equation~\eqref{FGI} where $x$ is a vector of variables and $\Lambda$ is
an invertible matrix over a field matching the size of $x$.
Throughout this paper, the entries of $\Lambda$ are elements of the field $\BQ(z)$
where $z$ is a vector of variables, the integrable functions $f_\hbar(x,z)$ that
we apply the formal Gaussian integration with respect to $x$ with be elements of
$\BQ(z)[x]\llbracket \hroot \rrbracket$, and the result of formal Gaussian integration
will be an element of the ring $\BQ(z)\llbracket \hbar \rrbracket$ or
$\BQ(z)[x]\llbracket \hbar^{\frac{1}{2}} \rrbracket$. When we specialize
to the case of a vector of algebraic numbers $z$, then $\BQ(z)$ defines the
corresponding number field.    

Just like integration of sufficiently smooth functions satisfies certain invariance
properties (such as change of variables, iterated integration, and even integration
by parts~\cite{AarhusII}), so does formal Gaussian integration. The corresponding
identities of formal Gaussian integration are combinatorial statements about
polynomials or rational functions and often follow from the corresponding statements
of integration of functions. 

We now give some elementary properties of formal Gaussian integration that we will
use in our paper.

\begin{lemma}
\label{lem.ff1}

\rm{(a)} For all invertible matrices $\Lambda$ and $P$ over $\BQ(z)$, we have
\bea
\left\langle
f_{\hbar}(Px,z)
\right\rangle_{x, P^t \Lambda P}
\= \left\langle f_{\hbar}(x,z)\right\rangle_{x,\Lambda}\,.




\eea
\rm{(b)} For all invertible matrices $\Lambda$ and vectors $G$ over $\BQ(z)$,
we have
\be
\label{fga1}
\langle\exp(-G^{t}\Lambda x \hroot) f_{\hbar}(x+G \hroot,z)
\rangle_{x,\Lambda} \= \exp\left(\frac{G^{t}\Lambda G}{2}\hbar\right)
\langle f_{\hbar}(x,z)\rangle_{x,\Lambda}
\ee
\rm{(c)} If
$\Lambda=\left(\begin{smallmatrix} A & B \\ B^t & C \end{smallmatrix}\right)$,
and $\Lambda$ and $A$ invertible, then for any $F$, we have 
\bea
\label{ff1}
\left\langle
\exp(F x' \hroot)f_{\hbar}(x'',z)
\right\rangle_{x,\Lambda}
\= \exp\left(\frac{FA^{-1}F^t}{2}\hbar \right)
\left\langle
\exp(-FA^{-1}B x''\hroot) f_{\hbar}(x'',z)
\right\rangle_{x'',C-B^t A^{-1} B} \!\!.
\eea
\end{lemma}

\begin{proof}
Part (a) follows from the fact the integration is unchanged
under a linear change of variables.


Part (b) follows from the fact the integration is unchanged
under an affine change of variables.

Part (c) follows from Fubini's theorem~\cite[Prop.2.13]{AarhusII}, combined
with Equation~\eqref{fga1}.
\end{proof}

The next lemma, which will be important in the application of $q$-holonomic
methods in Section~\ref{sub.qhol} and in the proofs of Theorems~\ref{thm.fourier}
and~\ref{thm.pentagon} below, concerns the behavior of formal Gaussian
integration when $z=(z_1,\dots,z_r)$ is shifted to
$e^{\ve \hbar}z:=(e^{\ve_1 \hbar}z_1,\dots,e^{\ve_r \hbar}z_r)$ for integers $\ve_j$.

\begin{lemma}
\label{lem.ff2}
For all invertible matrices $\Lambda(z)$ over $\BQ(z)$ and all integrable functions
$f_\hbar$, we have
\be
\label{eq.ff2}
\langle f_{\hbar}(x,z)\rangle_{x,\Lambda(z)} |_{z \mapsto e^{\ve \hbar}z}
\= \sqrt{\frac{\det\Lambda(e^{\ve\hbar}z)}{\det\Lambda(z)}} 
\Big\langle \exp\bigg(
\frac{x^{t}\big(\Lambda(z)-\Lambda(e^{\ve\hbar}z)\big)x}{2}\bigg)
f_{\hbar}(x,e^{\ve\hbar}z) \Big\rangle_{x,\Lambda(z)} \,.
\ee
\end{lemma}

\begin{proof}
The lemma follows from recentering the Gaussian after multiplying
$z$ by $e^{\ve\hbar}$.
\end{proof}


\subsection{\texorpdfstring{$q$--holonomic aspects of $\psi_\hbar$}{q-holonomic aspects of psi}}
\label{sub.qhol}
It is well-known that identities of holonomic functions can be proven 
algorithmically~\cite{WZ,PWZ}. We will use these ideas, adapted to our needs,
to prove fundamental identities between certain Gaussian integrals involving
the building block $\exp(\psi_{\hbar})$ of our series $\Phi^\Xi(\hbar)$.
Since $\psi_{\hbar}$ is related to the infinite Pochhammer symbol given in
Equation~\eqref{poch}, its functional equations will be of fundamental importance.
From its definition, it is clear that the infinite Pochhammer symbol
satisfies a simple first order linear $q$--difference equation
\be
\label{eq.poch}
(x;q)_{\infty} \= (1-x)(qx;q)_{\infty} \,.
\ee
To convert this into an identity of formal $\hbar$-series where $q=e^{\hbar}$,
we use the fact that there is an action of the quantum plane
(also known as
$q$--Weyl~\cite[Ex. 1.7]{Etingof} algebra)
on the space $\BQ(z)[x]\llbracket\hroot\rrbracket$
of integrable functions by an action on the $z$-variable given by
\be
\label{ML}
(L f_\hbar)(x,z) \= f_\hbar(x,e^{\hbar} z), \qquad
(M f_\hbar)(x,z) \= e^{\hbar} f_\hbar(x,e^{\hbar} z)
\ee
where $LM=qML$. The next lemma asserts that the completion
$\widehat{\psi}_{\hbar}(x,z)$ 
\be
\label{eq.psicomp}
\begin{aligned}
\widehat{\psi}_{\hbar}(x,z)
\;:&=\;
\exp\Big(\!
-\frac{\Li_{2}(z)}{\hbar}
-\frac{\Li_{1}(z)x}{\hbar^{\frac{1}{2}}}
+\frac{1}{2}\Li_{1}(z)
-\frac{\Li_{0}(z)x^2}{2}
\Big)
\psi_{\hbar}(x,z) \\
&=\;
\exp\Big(\!
-\sum_{k,\ell\in\BZ_{\geq0}}
\frac{B_{k}\,x^{\ell}\,\hbar^{k+\frac{\ell}{2}-1}}{\ell!\,k!}\Li_{2-k-\ell}(z)\Big)
\\
&\quad\in
\exp\Big(\!-\frac{\Li_{2}(z)}{\hbar}
-\frac{\Li_{1}(z)x}{\hbar^{\frac{1}{2}}}
+\frac{1}{2}\Li_{1}(z)
-\frac{\Li_{0}(z)x^2}{2}
\Big)(1+\hbar^{\frac{1}{2}}\BQ(z)[x]\llbracket\hbar^{\frac{1}{2}}
\rrbracket)
\end{aligned}
\ee
of $\psi_{\hbar}(x,z)$, as well as $\psi_{\hbar}(x,z)$ itself, satisfy a
corresponding first order linear $q$--difference equation, albeit with
complicated coefficients.

\begin{lemma}
\label{lem.psihdiff}
\rm{(a)} We have:
\be
\label{eq.qdiff.of.psih}
\widehat{\psi}_{\hbar}(x,e^{\hbar}z)
\=
(1-ze^{x\hbar^{1/2}})\,\widehat{\psi}_{\hbar}(x,z)\,.
\ee
\rm{(b)} We have:
\be
\label{eq.qdiff.of.psi}
\begin{aligned}
&\psi_{\hbar}(x,e^{\hbar}z)
\=
(1-ze^{x\hbar^{1/2}})
\,\psi_{\hbar}(x,z)
\sqrt{\frac{1-e^{\hbar}z}{1-z}}\\
&\times
\exp\Big(\frac{\Li_{2}(e^{\hbar}z)}{\hbar}-\frac{\Li_{2}(z)}{\hbar}
+\frac{\Li_{1}(e^{\hbar}z)x}{\hbar^{\frac{1}{2}}}
-\frac{\Li_{1}(z)x}{\hbar^{\frac{1}{2}}}
+\frac{1}{2}\Li_{0}(e^{\hbar}z)x^2
-\frac{1}{2}\Li_{0}(z)x^2\Big)\,.
\end{aligned}
\ee
\end{lemma}

Note that the identity~\eqref{eq.qdiff.of.psih} takes place in a larger ring,
which includes the symbols
$\exp(\frac{\Li_{2}(z)}{\hbar})$, $\exp(\frac{\Li_{1}(z)x}{\hroot})$,
$\exp(\frac{\Li_{0}(z)x^2}{2})$ and $\exp(\frac{\Li_{0}(z)x^2}{2})$ which one can
adjoin in the differential field $\BQ(z)((\hbar))$ as is standard in differential
Galois theory of linear differential equations~\cite{Singer:galois-differential}.
The symbols $\Li_k(z)$ for $k=0,1,2$ can be interpreted as normalized solutions
to the linear differential equations $z \frac{d}{dz} \Li_k(z) = \Li_{k-1}(z)$
with $\Li_0(z)=z/(1-z)$ and satisfy the usual properties
$\Li_k(e^\hbar z) = \sum_{r=0}^\infty \frac{1}{r!} \Li_{k-r}(z) \hbar^r$.
On the other hand, the coefficients in identity~\eqref{eq.qdiff.of.psi}
are elements of the ring $\BQ(z)[x]\llbracket \hroot \rrbracket$.

\begin{proof}
Part (a) can be proved directly using the facts that for
the Bernoulli polynomials $B_{r}(x)$ we have
$B_{r}(1)=B_{r}+\delta_{r,1}$ and
$B_{r}(x)=\sum_{k=0}^{r}\binom{r}{k}B_{n-k}x^{k}$.
Applying these identities we find that
\be
\begin{aligned}
&\exp\Big(-\sum_{k,\ell\in\BZ_{\geq0}}
\frac{B_{k}x^{\ell}\hbar^{k+\frac{\ell}{2}-1}}{\ell!k!}\Li_{2-k-\ell}(ze^{\hbar})\Big)
\\
&\=
\exp\Big(-\sum_{r,\ell\in\BZ_{\geq0}}\sum_{k=0}^{r}B_{k}\binom{r}{k}
\frac{x^{\ell}\hbar^{r+\frac{\ell}{2}-1}}{\ell!r!}\Li_{2-r-\ell}(z)\Big)\\
&\=
\exp\Big(-\sum_{r,\ell\in\BZ_{\geq0}}
\frac{B_{r}(1)x^{\ell}\hbar^{r+\frac{\ell}{2}-1}}{\ell!r!}\Li_{2-r-\ell}(z)\Big)\\
&\=
\exp\Big(-\Li_{1}(ze^{x\hbar^{1/2}})-\sum_{r,\ell\in\BZ_{\geq0}}
\frac{B_{r}x^{\ell}\hbar^{r+\frac{\ell}{2}-1}}{\ell!r!}\Li_{2-r-\ell}(z)\Big)\\
&\=
(1-ze^{x\hbar^{1/2}})\exp\Big(-\sum_{r,\ell\in\BZ_{\geq0}}
\frac{B_{r}x^{\ell}\hbar^{r+\frac{\ell}{2}-1}}{\ell!r!}\Li_{2-r-\ell}(z)\Big)\,.
\end{aligned}
\ee
Part (b) follows from (a), using Equation~\eqref{eq.psicomp} and expanding
in $\hbar$ to find that
\be
\begin{tiny}
\begin{aligned}
\sqrt{\frac{1-e^{\hbar}z}{1-z}}
\exp\Big(\frac{\Li_{2}(e^{\hbar}z)}{\hbar}-\frac{\Li_{2}(z)}{\hbar}
+\frac{\Li_{1}(e^{\hbar}z)x}{\hbar^{\frac{1}{2}}}
-\frac{\Li_{1}(z)x}{\hbar^{\frac{1}{2}}}
+\frac{1}{2}\Li_{0}(e^{\hbar}z)x^2
-\frac{1}{2}\Li_{0}(z)x^2\Big)
\in\BQ(z)[x]\llbracket\hbar^{\frac{1}{2}}\rrbracket\,.
\end{aligned}
\end{tiny}
\ee
\end{proof}

We end this section by discussing a useful relation between $\psi_\hbar(x,z)$
and its specialization at $x=0$. It is easy to see that the completion
$\widehat{\psi}_{\hbar}(x,z)$ of $\psi_\hbar(x,z)$ is regular at $x=0$ and satisfies
\be
\widehat{\psi}_{\hbar}(x,z)
\=
\widehat{\psi}_{\hbar}(0,ze^{x\hbar^{1/2}})\,.
\ee
This implies a corresponding statement
\bea
\label{eq.psid}
\psi_\hbar(x,z)
\= \psi_\hbar\big(0,ze^{x\hbar^{1/2}}\big)C_\hbar(x,z),
\eea
for $\psi_{\hbar}$ 
where
\bea
\label{Cdef}
C_\hbar(x,z) &\= \exp\Big(\!-\sum_{\ell\geq 3}
\frac{\hbar^{\frac \ell 2 -1}}{\ell!}\Li_{2-\ell}(z)x^\ell 
+\frac 1 2 \sum_{\ell\geq 1} \frac{h^{\frac \ell2}}{\ell!}\Li_{1-\ell}(z)x^\ell\Big)\\
&\=\exp\Big(\!-\frac{\Li_2(ze^{x\hroot})}\hbar+\frac{\Li_2(z)}\hbar
-\frac{\log(1-z)}\hroot x + \frac{z}{1-z}\frac {x^2}2\\
&\qquad\qquad-\frac 1 2 (\log(1-z\ezh) - \log(1-z))\Big)\,.
\eea


\subsection{\texorpdfstring{Fourier transform of $\psi_\hbar$}{Fourier transform of psi}}
\label{sub.fourier}

In this section, we prove two functional identities for $\psi_{\hbar}(\bullet,z)$,
$\psi_{\hbar}(\bullet,z')$ and $\psi_{\hbar}(\bullet,z'')$
where $z':=1/(1-z)$ and $z'':=1-1/z$ are related to the $\BZ/3\BZ$-symmetry of
the shapes of a tetrahedron, and reflect the $\BZ/3\BZ$-symmetry of the dilogarithm
function.

The next theorem is a formal Gaussian integration version of
the Fourier transform of the Faddeev quantum dilogarithm given in
Equation~\eqref{phifourier}. The proof, however, does not follow from the
distributional identity~\eqref{phifourier}, and instead uses $q$--holonomic ideas
and the basics of formal Gaussian integration. 

This theorem and its Corollary~\ref{cor.fourier} are used in Section~\ref{sec.quad}
to show that the power series $\Phi^\Xi(\hbar)$ are independent of the choice of
a nondegenerate quad.

\begin{theorem}
\label{thm.fourier}
We have:
\bea
\label{eq.fourier}
\psi_\hbar (x,z)
\=e^{-\frac{\hbar}{24}}\Big\langle
\exp\Big(
\Big(y+\frac{xz}{1-z}\Big) \frac{\hbar^{\frac 1 2}}{2}\Big)\,
\psi_\hbar\Big(y+\frac{xz}{1-z}, \frac 1 {1-z}
\Big)
\Big\rangle_{y,1-z^{-1}} 
\eea
in the ring $\BQ(z)[x]\llbracket\hroot\rrbracket$.
\end{theorem}

In fact, both sides of of Equation~\eqref{eq.fourier} lie in the subring
$\BQ[z^{\pm},(1-z)^{-1}][x]\llbracket\hroot\rrbracket$. 

\begin{proof}
It it clear from the definition that both sides of Equation~\eqref{eq.fourier}
are elements of the ring $\BQ(x)[z]\llbracket\hbar\rrbracket$. 
First, we will prove the specialization of Equation~\eqref{eq.fourier}
when $x=0$, i.e., we will show that
\bea
\label{eq.fourier0}
\psi_\hbar(0,z)
\= e^{-\frac{\hbar}{24}}
\Big\langle
\exp\Big(
\frac y2\hroot\Big)\,
\psi_\hbar\Big(y,\frac 1{1-z}\Big)
\Big\rangle_{y,1-z^{-1}} \in \BQ(z)[[\hbar]] \,.
\eea
To prove this, we will combine $q$-holonomic ideas with formal Gaussian
integration. From Equation~\eqref{eq.qdiff.of.psih}, we see that the left hand
side of Equation~\eqref{eq.fourier0} multiplied by
$\frac{\exp(-\Li_{2}(z)\hbar^{-1})}{\sqrt{1-z}}$ satisfies a simple first order
$q$--difference equation. We want to show the same for the right hand side.
To do this, consider the function
\be
\begin{aligned}
I_{m,\hbar}(w,z)
\=
w^me^{-\frac{\hbar}{24}+\frac{\pi^2}{6\hbar}}
\exp\Big(
\log(w)\Big(
\!-\frac{\log(w)}{2\hbar}
+\frac{\pi i}{\hbar}
-\frac{\log(z)}{\hbar}
+\frac{1}{2}\Big)\Big)\,
\widehat{\psi}_\hbar(0,w)
\end{aligned}
\ee
which is an element of a larger ring discussed in relation to
$\widehat{\psi}_{\hbar}$ of Equation~\eqref{eq.psicomp}. Using
Equation~\eqref{eq.psid} and the symmetry
\be
    \Li_2(z)
    \=
    \Li_2\Big(\frac 1 {1-z}\Big)
    -\frac 1 2\log({1-z})^2 +\pi i \log({1-z})-\log(z)\log({1-z})
    -\frac {\pi^2}6
\ee
of the dilogarithm~\cite{Zagier:dilog}, it is easy to see that
the right hand side of Equation~\eqref{eq.fourier0} is given by
\be
\label{eq.fourier.I.to.bracket}
\Big\langle
\sqrt{-z}
\exp\Big(\frac{\Li_{2}(z)}{\hbar}
+(1-z^{-1})\frac{w^2}{2}\Big)
I_{0,\hbar}\Big(\frac{1}{1-z}e^{w\hbar^{1/2}},z\Big)
\Big\rangle_{w,1-z^{-1}}\,.
\ee
The function $I_{m,\hbar}$ satisfies the linear $q$--difference equations
\be
\begin{aligned}
I_{m,\hbar}(e^{\hbar}w,z)
&\=
-e^{m\hbar}w^{-1}z^{-1}(1-w)I_{m,\hbar}(w,z)\,,\\
I_{m,\hbar}(w,e^{\hbar}z)
&\=
w^{-1}I_{m,\hbar}(w,z)\,,\\
I_{m,\hbar}(w,z)
&\=
wI_{m,\hbar}(w,z)\,,
\end{aligned}
\ee
which imply that
\be
\label{eq.If}
(1-e^{-m\hbar}z)I_{m,\hbar}\Big(\frac{1}{1-z}e^{w\hbar^{1/2}+\hbar},z\Big)
\=
I_{m}\Big(\frac{1}{1-z}e^{w\hbar^{1/2}},e^{\hbar}z\Big).
\ee
If we multiply both sides of~\eqref{eq.If} with the factors from
Equation~\eqref{eq.fourier.I.to.bracket} and take the bracket of both sides
and apply Lemma~\ref{lem.ff1} and Lemma~\ref{lem.ff2} to change
coordinates and the Gaussian, we find that when $m=0$ both sides of
Equation~\eqref{eq.fourier0} satisfy the same $q$--difference
equation~\eqref{eq.qdiff.of.psih}.























Moreover, it is easy to see that both sides of
Equation~\eqref{eq.fourier.I.to.bracket} are power series in $\hbar$ with
coefficients rational functions of $z$ of nonpositive degree, thus we can work
with the ring $\BQ\llbracket z^{-1}\rrbracket\llbracket \hbar\rrbracket$
instead. In this case, the Newton polygon of this first order linear
$q$-difference equation implies that it has a unique solution in
$\BQ\llbracket z^{-1}\rrbracket\llbracket \hbar\rrbracket$ determined by its
value at $z=\infty$. Therefore, the identity in Equation~\eqref{eq.fourier0}
follows from its specialization at $z=\infty$. Since
\be
\begin{aligned}
\psi_\hbar(0,\infty)
&\=
\exp\Big(\frac{\hbar}{12}\Big)\,,\\
e^{\frac{-\hbar}{24}}\left\langle
\exp\Big(
\frac w2\hroot\Big)
\psi_\hbar\left(w,0\right)
\right\rangle_{w,1}
&\=
e^{\frac{-\hbar}{24}}\left\langle
\exp\left(
\frac w2\hroot
\right)
\right\rangle_{w,1}
\=
\exp\Big(\frac{\hbar}{12}\Big)\,,
\end{aligned}
\ee
this completes the proof of Equation~\eqref{eq.fourier0}.

\medskip

Going back to the general case of $z$, Equation~\eqref{eq.fourier} follows
from Equation~\eqref{eq.psid}
together with~\eqref{eq.fourier0} using Lemma~\ref{lem.ff2}
to shift the Gaussian and Lemma~\ref{lem.ff1}
to change integration variable via the transformation
\be
w \mapsto w-\frac 1 \hroot \log\left(\frac{1-z}{1-ze^{x\hbar^{1/2}}}\right)
-\frac{x}{1-z^{-1}}
\,.
\ee
The detailed calculation is given in Appendix~\ref{app.fourier}. 
\end{proof}

Theorem~\ref{thm.fourier} implies the following identity relating
$\psi_\hbar(\bullet,z)$ and $\psi_\hbar(\bullet,z'')$.

\begin{corollary}
\label{cor.fourier}
We have:
\bea
\label{eq.fourier2}
\psi_\hbar (x,z)
\=e^{\frac{\hbar}{24}}\Big\langle
\exp\Big(\!
-\frac{x}{2}\hbar^{\frac{1}{2}}\Big)\,
\psi_\hbar\Big(y-\frac{x}{1-z}, 1-z^{-1}\Big)
\Big\rangle_{y,z-1} 
\eea
in the ring $\BQ(z)[x]\llbracket\hroot\rrbracket$.
\end{corollary}
\begin{proof}
Apply Equation~\eqref{eq.fourier} to the $\psi_{\hbar}$
that appears on the right hand side of the same Equation~\eqref{eq.fourier}.
Then apply a change of variables and Fubini's
theorem of Lemma~\ref{lem.ff1} to calculate
the bracket for the variable that doesn't appear
in the argument of the remaining $\psi_{\hbar}$.
\end{proof}


\subsection{\texorpdfstring{Pentagon identity for $\psi_\hbar$}{Pentagon identity for psi}}
\label{sub.pentagon}

In this section, we prove a pentagon identity for the functions
$\psi_\hbar(\bullet,z)$ where $z$ takes the five values
\be
\label{5z}
[z_1]+[z_2]\mapsto
[z_1 z_0^{-1}] +[z_0] +[z_2 z_0^{-1}], 
\qquad z_0\=z_1+z_2-z_1 z_2
\ee
what appear in the 5-term relation for the dilogarithm.
The next theorem is a formal Gaussian integration version of the pentagon
identity~\eqref{phipentagon} of the Faddeev quantum dilogarithm and will be
used in Section~\ref{sec.pachner} to prove that the series $\Phi^\Xi(\hbar)$
is independent of 2--3 Pachner moves. Let us denote
\be
\label{eq.delta23}
\delta
\=2+\Li_{0}(z_1z_{0}^{-1})+\Li_{0}(z_{0})+\Li_{0}(z_2z_{0}^{-1})
\=
\frac{(z_1+z_2-z_1z_2)^2}{z_1z_2(1-z_1)(1-z_2)}\,.
\ee

\begin{theorem}
\label{thm.pentagon}
We have: 
\be
\label{eq.pentagon}
\begin{aligned}
&\psi_\hbar(x,z_1)\,\psi_\hbar(y,z_2)
\=e^{- \frac \hbar {24}}
\Big\langle
\psi_\hbar\Big(-w -y
+\frac{xz_2+yz_1}{z_0},
z_1z_0^{-1}\Big)\\
&
\psi_\hbar\Big(w+x+y
-\frac{xz_2+yz_1}{z_0},
z_0\Big)
\psi_\hbar\Big(-w-x
+\frac{xz_2+yz_1}{z_0},
z_2z_0^{-1}\Big)
\Big\rangle_{w,\delta}
\end{aligned}
\ee
in the ring $\BQ(z_1,z_2)[x,y]\llbracket\hroot\rrbracket$. 
\end{theorem}






\begin{proof}
It is clear from the definition that both sides of Equation~\eqref{eq.pentagon}
are elements of the ring $\BQ(z_1,z_2)[x,y]\llbracket\hroot\rrbracket$. To prove this,
we follow the same approach we used to prove Theorem~\ref{thm.fourier}. First, we
prove the identity~\eqref{eq.pentagon} when $u=v=0$, i.e., we will show that
\be
\label{pentagon0}
\psi_\hbar(0,z_1)\,\psi_\hbar(0,z_2) 
\=e^{- \frac \hbar {24}}
\big\langle\psi_\hbar(-w,z_1z_0^{-1})
\,\psi_\hbar(w,z_0)
\,\psi_\hbar(-w,z_2z_0^{-1})
\big\rangle_{w,\delta}
\ee
in the ring $\BQ(z_1,z_2)\llbracket\hbar\rrbracket$
and to prove this we will again use $q$--holonomic methods.
To do so, consider the function
\be
\label{eq.Ip}
\begin{aligned}
&I_{m,\hbar}(z_1,z_2,z)
\=
e^{\frac{\pi^{2}}{6\hbar}-\frac{\hbar}{24}}z^{m}\,
\widehat{\psi}_{\hbar}(0,z_1z^{-1})\,
\widehat{\psi}_{\hbar}(0,z)\,
\widehat{\psi}_{\hbar}(0,z_2z^{-1})\\
&\times\exp\Big(-\frac{\log(z_1)\log(z_2)}{\hbar}
+\frac{\log(z)\log(z_1)}{\hbar}
+\frac{\log(z)\log(z_2)}{\hbar}
-\frac{\log(z)^2}{\hbar}\Big)\,,
\end{aligned}
\ee
which is again an element of a larger ring discussed in relation to
$\widehat{\psi}_{\hbar}$ of Equation~\eqref{eq.psicomp}.
Using Equation~\eqref{eq.psid} and the five term relation for the
dilogarithm~\cite{Zagier:dilog}, it is easy to see that the right hand side of
Equation~\eqref{pentagon0} is given by
\be
\label{eq.Ip1}
\Big\langle\frac{\sqrt{z_1z_2}(1-z_1)(1-z_2)}{z_1+z_2-z_1z_2}
\exp\Big(\frac{\Li_{2}(z_1)}{\hbar}
+\frac{\Li_{2}(z_2)}{\hbar}
+\frac{\delta}{2}z^2\Big)
I_{0,\hbar}(z_1,z_2,z_0e^{w\hbar^{1/2}})
\Big\rangle_{w,\delta}\,.
\ee
The function $I_{m,\hbar}$ satisfies the system of linear $q$--difference equations
\be\label{eq.Ip2}
\begin{aligned}
I_{m,\hbar}(e^{\hbar}z_1,z_2,z)
&\=z\,z_2^{-1}(1-z_1z^{-1})\,
I_{m,\hbar}(z_1,z_2,z)\,,\\
I_{m,\hbar}(z_1,e^{\hbar}z_2,z)
&\=z\,z_1^{-1}(1-z_2z^{-1})\,
I_{m,\hbar}(z_1,z_2,z)\,,\\
I_{m,\hbar}(z_1,z_2,e^{\hbar}z)
&\=(1-z)\,z_1z_2z^{-2}e^{(m-1)\hbar}
I_{m,\hbar}(z_1,z_2,z)\,,\\
I_{m+1,\hbar}(z_1,z_2,z)
&\=
z\,I_{m,\hbar}(z_1,z_2,z)\,,
\end{aligned}
\ee
which can be derived from Equation~\eqref{eq.qdiff.of.psih}. In fact, the
function $I_{m,\hbar}$ is holonomic of rank $1$, a fact that we will not use
explicitly~\cite{PWZ}. Therefore, we see that
\be\label{eq.Ip3}
\begin{tiny}
\begin{aligned}
&I_{m,\hbar}(e^{\hbar}z_1,z_2,z)
\=z_2^{-1}I_{m+1,\hbar}(z_1,z_2,z)-z_1z_2^{-1}I_{m,\hbar}(z_1,z_2,z)\,,\\
&I_{m,\hbar}(e^{\hbar}z_1,z_2,(e^{\hbar}z_1+z_2-e^{\hbar}z_1z_2)e^{w\hbar^{1/2}})\\
&\=z_2^{-1}I_{m+1,\hbar}(z_1,z_2,(e^{\hbar}z_1+z_2-e^{\hbar}z_1z_2)e^{w\hbar^{1/2}})
-z_1z_2^{-1}I_{m,\hbar}(z_1,z_2,(e^{\hbar}z_1+z_2-e^{\hbar}z_1z_2)e^{w\hbar^{1/2}})\,,\\




&I_{m,\hbar}(z_1,z_2,(z_1+z_2-z_1z_2)e^{z\hbar^{1/2}+\hbar})\\
&\=z_1z_2e^{(m-1)\hbar}I_{m-2,\hbar}(z_1,z_2,(z_1+z_2-z_1z_2)e^{z\hbar^{1/2}})
-z_1z_2e^{(m-1)\hbar}I_{m-1,\hbar}(z_1,z_2,(z_1+z_2-z_1z_2)e^{z\hbar^{1/2}})\,.\\
\end{aligned}
\end{tiny}
\ee
Let us define $\widehat{J}_{m,\hbar}$ and $J_{m,\hbar}$ by the equation
\be\label{eq.Ip4}
\begin{aligned}
\widehat{J}_{m,\hbar}(z_1,z_2)
&\=
\frac{1}{\sqrt{(1-z_1)(1-z_2)}}
\exp\Big(-\frac{\Li_{2}(z_1)}{\hbar}
-\frac{\Li_{2}(z_2)}{\hbar}\Big)
J_{m,\hbar}(z_1,z_2)\\
&\=\Big\langle\frac{\sqrt{z_1z_2(1-z_1)(1-z_2)}}{z_1+z_2-z_1z_2}
\exp\Big(
\frac{\delta}{2}z^2\Big)
I_{m,\hbar}(z_1,z_2,z_0e^{w\hbar^{1/2}})
\Big\rangle_{w,\delta}\,.
\end{aligned}
\ee
If we multiply both sides of the Equations~\eqref{eq.Ip3} with the
factors from Equation~\eqref{eq.Ip1}, take the bracket of both sides,
and apply Lemma~\ref{lem.ff2} to change
coordinates and the Gaussian, we find that $\widehat{J}_{\hbar,m}(z_1,z_2)$
satisfies the $q$--difference equations
\be
\begin{aligned}
\widehat{J}_{m,\hbar}(e^{\hbar}z_1,z_2)
&\=z_2^{-1}\widehat{J}_{m+1,\hbar}(z_1,z_2)
-z_1z_2^{-1}\widehat{J}_{m,\hbar}(z_1,z_2)\,,\\
\widehat{J}_{m,\hbar}(z_1,e^{\hbar}z_2)
&\=z_1^{-1}\widehat{J}_{m+1,\hbar}(z_1,z_2)
-z_1^{-1}z_2\widehat{J}_{m,\hbar}(z_1,z_2)\,,\\
\widehat{J}_{m,\hbar}(z_1,z_2)
&\=z_1z_2e^{(m-1)\hbar}\widehat{J}_{m-2,\hbar}(z_1,z_2)
-z_1z_2e^{(m-1)\hbar}\widehat{J}_{m-1,\hbar}(z_1,z_2)\,.
\end{aligned}
\ee
From these relations we can derive the equations
\be
\begin{aligned}
0&\=(z_1-z_1e^{(m+1)\hbar}+z_1^2e^{(m+1)\hbar}-z_1)\widehat{J}_{m,\hbar}(z_1,z_2)\\
&\qquad+(z_1z_2e^{(m+1)\hbar}-z_2+qz_1)\widehat{J}_{m,\hbar}(e^{\hbar}z_1,z_2)
+z_2\widehat{J}_{m,\hbar}(e^{2\hbar}z_1,z_2)\,,\\
0&\=(z_2-z_2e^{(m+1)\hbar}+z_2^2e^{(m+1)\hbar}-z_2)\widehat{J}_{m,\hbar}(z_1,z_2)\\
&\qquad+(z_2z_1e^{(m+1)\hbar}-z_1+qz_2)\widehat{J}_{m,\hbar}(z_1,e^{\hbar}z_2)
+z_1\widehat{J}_{m,\hbar}(z_1,e^{2\hbar}z_2)\,.\\
\end{aligned}
\ee
These $q$--difference equations give rise to equations for $J_{m,\hbar}$ given by
\be\label{eq.qJ}
\begin{aligned}
0&\=(z_1-z_1e^{\hbar}+z_1^2e^{\hbar}-z_1)J_{m,\hbar}(z_1,z_2)\\
&\qquad+(z_1z_2e^{\hbar}-z_2+qz_1)\sqrt{\frac{1-z_1}{1-e^{\hbar}z_1}}
\exp\Big(\frac{\Li_{2}(z_1)-\Li_{2}(e^{\hbar}z_1)}{\hbar}\Big)
J_{m,\hbar}(e^{\hbar}z_1,z_2)\\
&\qquad+z_2\sqrt{\frac{1-z_1}{1-e^{2\hbar}z_1}}\exp\Big(\frac{\Li_{2}(z_1)
-\Li_{2}(e^{2\hbar}z_1)}{\hbar}\Big)J_{m,\hbar}(e^{2\hbar}z_1,z_2)\,,\\
0&\=(z_2-z_2e^{\hbar}+z_2^2e^{\hbar}-z_2)J_{m,\hbar}(z_1,z_2)\\
&\qquad+(z_2z_1e^{\hbar}-z_1+qz_2)\sqrt{\frac{1-z_2}{1-e^{\hbar}z_2}}
\exp\Big(\frac{\Li_{2}(z_2)-\Li_{2}(e^{\hbar}z_2)}{\hbar}\Big)
J_{m,\hbar}(z_1,e^{\hbar}z_2)\\
&\qquad+z_1\sqrt{\frac{1-z_2}{1-e^{2\hbar}z_2}}
\exp\Big(\frac{\Li_{2}(z_2)-\Li_{2}(e^{2\hbar}z_2)}{\hbar}\Big)
J_{m,\hbar}(z_1,e^{2\hbar}z_2)\,.
\end{aligned}
\ee
These equations are also satisfied by the left hand side of
Equation~\eqref{pentagon0}, which follows from repeated application of
Equation~\eqref{eq.qdiff.of.psi}.

It is easy to see that both sides of Equation~\eqref{pentagon0} are formal power
series in $\hbar$ with coefficients rational functions of $(z_1,z_2)$ of
nonpositive degree with respect to both $z_1$ and $z_2$, thus their coefficients
embed in $\BQ\llbracket z_1^{-1}, z_2^{-1} \rrbracket$, and it suffices to prove
~\eqref{pentagon0} in the ring $\BQ\llbracket z_1^{-1}, z_2^{-1} \rrbracket
\llbracket \hbar \rrbracket$. In this case, we consider the linear $q$-difference
equations~\eqref{eq.qJ} over the ring $\BQ\llbracket z_1^{-1}, z_2^{-1} \rrbracket
\llbracket \hbar \rrbracket$. Looking at the corresponding Newton polytopes, 
the leading monomials that appear as coefficients of this $q$--difference equation
~\eqref{eq.qJ} at $\infty$ are $z_1^{2}(1+\mathrm{O}(z_1^{-1})\mathrm{O}(z_2^{0}))$
and $z_1^{2}z_2(1+\mathrm{O}(z_1^{-1})\mathrm{O}(z_2^{0}))$ for the first equation,
and $z_2^{2}(1+\mathrm{O}(z_1^{0})\mathrm{O}(z_2^{-1}))$ and
$z_1z_2^{2}(1+\mathrm{O}(z_1^{0})\mathrm{O}(z_2^{-1}))$ for the second equation,
respectively. The structure of these monomials and their Newton polytopes
shows that there is a unique solution to these equations in
$\BQ\llbracket z_1^{-1},z_2^{-1}\rrbracket\llbracket\hbar\rrbracket$ determined
by the value at $z_1=z_2=\infty$. Therefore, the identity in
Equation~\eqref{pentagon0} reduces to its specialization at $z_1=z_2=\infty$.
Since
\be
\begin{aligned}
\psi_\hbar(0,\infty)\,\psi_\hbar(0,\infty)
&\=
e^{\frac{\hbar}{6}}\quad\text{and}\\
e^{- \frac \hbar {24}}
\big\langle\psi_\hbar(-w,0)^2
\,\psi_\hbar(w,\infty)
\big\rangle_{w,\delta}
&\=
e^{- \frac \hbar {24}}
\Big\langle\exp\Big(
\frac{\hbar}{12}-\frac{z\hbar^{\frac{1}{2}}}{2}
\Big)\Big\rangle_{w,\delta}
\=
e^{\frac{\hbar}{6}}\,,
\end{aligned}
\ee
this completes the proof of Equation~\eqref{pentagon0}.

\medskip

Going back to the general case of $x,y$, Equation~\eqref{eq.pentagon} follows
from Equation~\eqref{eq.psid} together with~\eqref{pentagon0} using
Lemma~\ref{lem.ff2} to shift the Gaussian and with a change of integration
variable
\be
w \mapsto w+\frac{1}{\hroot}\log\left(\frac{z_1+z_2-z_1z_2}{
z_1e^{x_1\hbar^{1/2}}+z_2e^{x_2\hbar^{1/2}}-z_1z_2e^{(x_1+x_2)\hbar^{1/2}}}\right)
+x+y - \frac{xz_1+yz_2}{z_0}\,.
\ee
The detailed calculation is given in Appendix~\ref{app.pentagon}.
\end{proof}


\subsection{\texorpdfstring{Inversion formula for $\psi_\hbar$}{Inversion formula for psi}}
\label{sub.inversion}

In this section, we give an inversion formula for $\psi_\hbar$ analogous to the
inversion formula~\eqref{doublephi} for the Faddeev quantum dilogarithm.
Although we will not use this formula explicitly in our paper, we include it
for completeness.

\begin{lemma}
\label{lem.inversion}
We have:
\be
\label{inv1}
\psi_{\hbar}(x,z)
  \frac{1-z^{-1}e^{-x\hbar^{1/2}}}{1-z^{-1}}
  \psi_{\hbar}(-x,1/z) \= \exp\Big(-
  \frac{x\hbar^{\frac{1}{2}}}{2}+\frac{\hbar}{12}\Big),
\ee  
\be
\label{inv2}
\widehat{\psi}_{\hbar}(0,z)
\widehat{\psi}_{\hbar}(0,1/z) 
\= \frac{\sqrt{-z}}{1-z}\exp\Big(\frac{\pi^2}{6\hbar}+\frac{1}{2\hbar}
\log(-z)^2+\frac{\hbar}{12}\Big) \,.
\ee
\end{lemma}

\begin{proof}
These formulas all follow from the well-known inversion formulas
for the polylogarithms (see for example~\cite{Oesterle}):
\bea
  \Li_{2}(z)+\Li_{2}(1/z)
  &\=
  -\frac{\pi^2}{6}-\frac{1}{2}\log(-z)^2\,,\\
  \Li_{1}(z)-\Li_{1}(1/z)
  &\=
  -\log(-z)\,,\\
  \Li_{0}(z)+\Li_{0}(1/z)
  &\=
  -1\,,\\
  \Li_{-n}(z)+(-1)^n\Li_{-n}(1/z)
  &\=0 \qquad (n>0) \,.
\eea
Using these relations, we have
\bea
\widehat{\psi}_{\hbar}(0,z)
\widehat{\psi}_{\hbar}(0,1/z)
&\=
\exp\Big(\!
-\sum_{k\in\BZ_{\geq0}}
\frac{B_{k}\,\hbar^{k-1}}{k!}(\Li_{2-k}(z)+\Li_{2-k}(1/z))\Big)\\
&\=
\frac{\sqrt{-z}}{1-z}\exp\Big(\frac{\pi^2}{6\hbar}+\frac{1}{2\hbar}
\log(-z)^2+\frac{\hbar}{12}\Big)\,.
\eea
Similarly, we find that
\be
\begin{aligned}
  &\psi_{\hbar}(x,z)
  \frac{1-z^{-1}e^{-x\hbar^{1/2}}}{1-z^{-1}}
  \psi_{\hbar}(-x,1/z)\\
  &\=
  \exp\bigg(\!-\!\!\sum_{\underset{k+\frac{\ell}{2}>1}{k,\ell\in\BZ_{\geq0}}}
  \frac{B_{k}\,x^{\ell}\,\hbar^{k+\frac{\ell}{2}-1}}{\ell!\,k!}
  \big(\Li_{2-k-\ell}(z)+(-1)^{k+\ell}\Li_{2-k-\ell}(1/z)\big)\bigg)\\
  &\=
  \exp\Big(-
  \frac{x\hbar^{\frac{1}{2}}}{2}+\frac{\hbar}{12}\Big)\,.
\end{aligned}
\ee
Notice that this is exactly the factor that appeared in the remark after
Equation~\eqref{psih}, which gave the relation between the $\psi_{\hbar}$ used
in the current paper and the ones used in~\cite[Eq.~1.9]{DG}.
Indeed, $\frac{1-z^{-1}}{1-z^{-1}e^{-x\hbar^{1/2}}}\psi_{\hbar}(-x,1/z)^{-1}$ is
exactly the series used in~\cite{DG} where the factor
$\frac{1-z^{-1}}{1-z^{-1}e^{-x\hbar^{1/2}}}$ amounts to swapping the sign of $B_{1}$
as done there.
\end{proof}
