---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-009-23-the-q-borel-and-the-q-laplace-transforms
section_title: "The q-Borel and the q-Laplace transforms"
section_number: 2.3
pages: 14-17
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.955
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.qborel}

We now recall the $q$-Borel transform $\Bor_\kappa$ (for a rational number $\kappa$)
defined by
\be
\label{qborel}
\Bor_{\kappa}\left(\sum_{\ell=0}^{\infty}a_{\ell}t^{\ell}\right)(\xi,q)
=
\sum_{\ell=0}^{\infty}(-1)^{\ell}q^{\kappa \ell(\ell+1)/2}a_{\ell}\xi^{\ell}\,.
\ee
Its role is to convert divergent series, e.g., of the form
$\sum_{\ell=0}^\infty q^{-\kappa \ell(\ell+1)/2}a_{\ell}t^{\ell}$ (where $a_\ell$
is bounded and $\kappa>0$) to convergent ones at $\xi=0$. 


An inverse of the $q$-Borel transform is the $q$-Laplace transform, whose role
is to construct analytic solutions to the linear $q$-difference equation
with prescribed asymptotics. It is defined for $\kappa>0$ by
\be
\label{qlap}
\Lap_{\kappa}(f)(t,\lambda,q)
=
\frac{1}{\theta(\lambda;q^\kappa)}\sum_{\ell\in\BZ}(-1)^{\ell}
q^{\kappa\ell(\ell+1)/2}\lambda^{\ell}f(q^{\kappa\ell}\lambda t,q)
=
\sum_{\ell\in\BZ}
\frac{f(q^{\kappa\ell}\lambda t,q)}{\theta(q^{\kappa\ell}\lambda;q^\kappa)}\, ,
\ee
and for $\kappa<0$, by
\be
\Lap_{\kappa}(f)(t,q)=\oint f(\xi,q)\theta(t/\xi;q^{-\kappa})
\frac{d\xi}{2\pi i\xi} \,.
\ee
The $q$-Laplace transform for positive $\kappa$ is more common, however, in
the computation of the monodromy of the $4_1$ knot, we will use $\kappa <0$,
following analogous computations of Morita \cite{Morita:conn-mon}.

In some sense, the two tranformations are inverse to each other. More precisely,
for all $\kappa$ and all natural numbers $n$, we have
\be
\label{qlapbort}
\Lap_{\kappa}\Bor_{\kappa}(t^{n})(t,\lambda,q) = t^n \,.
\ee
(Interestingly, the right hand side is independent of $\lambda$.) Indeed,
for $\kappa >0$, we have 
\be
\begin{aligned}
\Lap_{\kappa}\Bor_{\kappa}(t^{n})
&=
\frac{1}{\theta(\lambda;q^\kappa)}\sum_{\ell\in\BZ}(-1)^{\ell}q^{\kappa\ell(\ell+1)/2}
\lambda^{\ell}(-1)^{n}q^{\kappa n(n+1)/2}q^{\kappa\ell n}\lambda^{n}t^{n}\\
&=
\frac{1}{\theta(\lambda;q^\kappa)}\sum_{\ell\in\BZ}(-1)^{\ell+n}
q^{\kappa(\ell+n)(\ell+n+1)/2}\lambda^{\ell+n}t^{n}\\
&=
\frac{1}{\theta(\lambda;q^\kappa)}\sum_{\ell\in\BZ}(-1)^{\ell}
q^{\kappa\ell(\ell+1)/2}\lambda^{\ell}t^{n} = t^n \,.
\end{aligned}
\ee
A similar calculation using the residue theorem shows~\eqref{qlapbort}
for $\kappa <0$.
More generally, the fact solutions constructed by Borel transforms followed
by iterated Laplace transforms are asymptotic to the original formal power series is
known in the literature as Watson's lemma, 
a modern proof of which may be found for instance in
Miller~\cite[p.~53, Prop.~2.1]{Miller:applied}. An analogous lemma holds for
the $q$-case, see~\cite[Prop.2.9]{Dreyfus:building}.

By its very definition, $\Lap_\kappa$ for $\kappa>0$ depends on the
variable $\lambda$ in an elliptic way
\be
\label{lapelliptic}
\Lap_\kappa(f)(t,q^{\kappa}\lambda,q)=\Lap_\kappa(f)(t,\lambda,q) 
\ee
whereas $\Lap_\kappa$ for $\kappa <0$ does not involve a variable $\lambda$. 
The next lemma, whose proof follows from an elementary application of the
residue theorem, concerns the dependence of the $q$-Laplace transform on the
auxiliary variable $\lambda$, and may be of independent interest.

\begin{lemma}
\label{lem.fund}
Assuming that
\be
\lim_{\ve\rightarrow 0}\oint_{|\xi|=\ve^{\pm}}
\frac{f(\xi t,q)\theta(\mu^{-1}\lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)
  \theta(\xi\lambda^{-1};q)}\frac{d\xi}{2\pi i\xi}=0
\ee
where $\ve$ avoids the poles of the integrand we have  
\be
\begin{aligned}
\Lap_{1}(f)(t,\lambda &,q)-\Lap_{1}(f)(t,\mu,q)\\
&=
\frac{\theta(\lambda ^{-1}\mu ;q)(q;q)_{\infty}^{3}}{\theta(\lambda ^{-1};q)
  \theta(\mu ;q)}\sum_{x\in\mathrm{poles\;of}\;f}\Res_{\xi=x}\frac{f(\xi,q)
  \theta(\lambda ^{-1}\mu ^{-1}t^{-1}\xi;q)}{\theta(\xi\lambda ^{-1}t^{-1};q)
  \theta(\xi\mu ^{-1}t^{-1};q)} \,.
\end{aligned}
\ee
\end{lemma}

Note that the assumption on $f$ is mild since as $t$ approaches $0$ or $\infty$
bounded away from the poles, the quotient of $\theta$'s approaches $0$. Note
also that the lemma can be extended to the case of $\mathcal{L}_{\kappa}$ for
$\kappa >0$ by substituting $q\mapsto q^{\kappa}$ except in the argument of $f$. 

\begin{proof}
We compute  
\be
\begin{aligned}
0&=
\sum_{\xi\in \mathrm{poles}}\Res_{\xi}\frac{f(\xi t,q)\theta(\mu^{-1}
  \lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)\theta(\xi\lambda^{-1};q)}
\frac{d\xi}{2\pi i\xi}\\
&=
\sum_{k}\Res_{\xi=q^{k}\lambda}\frac{f(\xi t,q)
  \theta(\mu^{-1}\lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)
  \theta(\xi\lambda^{-1};q)}\frac{d\xi}{2\pi i\xi}
+\sum_{k}\Res_{\xi=q^{k}\mu}\frac{f(\xi t,q)
  \theta(\mu^{-1}\lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)
  \theta(\xi\lambda^{-1};q)}\frac{d\xi}{2\pi i\xi}\\
&\qquad\qquad+\sum_{x\in \mathrm{poles\;of}\;f}\Res_{\xi=t^{-1}x}
\frac{f(\xi t,q)\theta(\mu^{-1}\lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)
  \theta(\xi\lambda^{-1};q)}\frac{d\xi}{2\pi i\xi}\\









&=
\sum_{k}(-1)^{k}q^{k(k+1)/2}\lambda^{k}
\frac{f(q^{k}\lambda t,q)
  \theta(\mu^{-1};q)}{\theta(\mu^{-1}\lambda;q)(q;q)_{\infty}^{3}}
+\sum_{k}(-1)^{k}q^{k(k+1)/2}\mu^{k}
\frac{f(q^{k}\mu t,q)\theta(\lambda^{-1};q)}{\theta(\mu\lambda^{-1};q)
  (q;q)_{\infty}^{3}}\\
&\qquad\qquad+\sum_{x\in \mathrm{poles\;of}\;f}\Res_{\xi=t^{-1}x}
\frac{f(\xi t,q)\theta(\mu^{-1}\lambda^{-1}\xi;q)}{\theta(\xi\mu^{-1};q)
  \theta(\xi\lambda^{-1};q)}\frac{d\xi}{2\pi i\xi}\\
&=
\frac{\theta(\mu^{-1};q)\theta(\lambda;q)}{\theta(\mu^{-1}\lambda;q)
  (q;q)_{\infty}^{3}}\Lap_{1}(f)(t,\lambda,q)
+\frac{\theta(\mu;q)\theta(\lambda^{-1};q)}{\theta(\mu\lambda^{-1};q)
  (q;q)_{\infty}^{3}}\Lap_{1}(f)(t,\mu,q)\\
&\qquad\qquad+\sum_{x\in \mathrm{poles\,of}\,f}\Res_{\xi=x}
\frac{f(\xi,q)\theta(\mu^{-1}\lambda^{-1}t^{-1}\xi;q)}{\theta(\xi\mu^{-1}t^{-1};q)
  \theta(\xi\lambda^{-1}t^{-1};q)}\frac{d\xi}{2\pi i\xi} \,.
\end{aligned}
\ee
\end{proof}

This type of residue formula for the Laplace transform is similar to the definition
of the Laplace transform for $\kappa<0$. We can find a similar expression for a single
Laplace transform using a special function. The Appell-Lerch sum will be studied later
in Section~\ref{sub.ex2} but we will define it here.
\be
L(t,\lambda,q)
=
\frac{1}{\theta(\lambda;q)}\sum_{k\in\BZ}(-1)^{k}
\frac{q^{k(k+1)/2}\lambda^{k}}{1-q^{k}\lambda t}.
\ee
Using this we have the following integral expression for the Laplace transform for
$\kappa>0$.

\begin{lemma}
For $\kappa>0$, we have  
\be
(\Lap_{\kappa}f)(t,\lambda,q) =
\sum_{k\in\BZ}\Res_{\xi=q^{\kappa k}}L(\xi^{-1}\lambda^{-1},\lambda,q^{\kappa})
f(\xi\lambda t,q)\frac{d\xi}{2\pi i\xi} \,.
\ee
\end{lemma}

Deforming the contour and the residue theorem give the following lemma.

\begin{lemma}
  Assuming that
  \be
\lim_{\ve\rightarrow 0}
\oint_{|\xi|=\ve^{\pm}}
L(\xi^{-1}\lambda^{-1},\lambda,q^{\kappa})
f(\xi\lambda t,q)\frac{d\xi}{2\pi i\xi}
=0
  \ee
  where $\ve$ avoids the poles of the integrand we have
  \be
(\Lap_{\kappa}f)(t,\lambda,q)
=
-\sum_{x\in\mathrm{poles\,of}\,f}
L(x^{-1}t,\lambda,q)
\Res_{\xi=x}f(\xi,q)\frac{d\xi}{2\pi i\xi}
  \ee
\end{lemma}
Notice that all the dependence on $t$ and $\lambda$ is now in the arguments of
the Appell-Lerch sums. This illustrates the important role the residues of the
Borel transform play in the resummation. An application of this lemma leads to
the following remarkable formula.

\begin{corollary}
  \be
f^{(1)}(t,\lambda,q)
=
-\theta(t;q)\sum_{k=0}^{\infty}
\left(L(q^{1/4+k/2}t,\lambda,q^{1/2})R_{+}(k,q)
  +L(-q^{1/4+k/2}t,\lambda,q^{1/2})R_{-}(k,q)\right)
  \ee
  where $f^{(1)}$ is given in Equation~\eqref{ex41.f1} and $R_{\pm}$ is given
  in Equation~\eqref{Rpm}.
\end{corollary}
