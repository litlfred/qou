---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-003-complex-chernsimons-theory
section_title: "Complex Chern–Simons theory"
section_number: null
pages: 9-11
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.995
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
\label{sec-cs}

Complex Chern--Simons (CS) theory is an ideal arena to study trans-series, 
since as a QFT it is essentially solvable, and at the same time 
it leads to highly non-trivial perturbative series. The mathematical program of applying resurgence in 
complex CS theory was pioneered in \cite{garoufalidis}, and applied in e.g. \cite{garo-costin,gmp}. 

In this section we will illustrate our considerations with the resurgent 
results for partition functions on the complements of knots, presented in \cite{ggm1, ggm2}. This 
observable admits a non-perturbative definition through the so-called state integral invariant \cite{hikami, DGLZ, ak}, 
which can be calculated by a finite-dimensional integral. The coupling constant will be denoted by $\tau$ and is a 
complex variable. The partition function depends on an additional complex variable, the holonomy 
around the knot, but we will set it to zero for simplicity. In this case, the 
partition function is known to be an analytic function of $\tau$ on $\IC \backslash (-\infty, 0]$.  

For concreteness, we will consider the complement of the famous figure-eight knot. Its state-integral 
invariant is explicitly known, and we would like to express it as a trans-series. The building blocks of the 
trans-series are the perturbative expansions around non-trivial saddle points or instantons in 
complex CS theory. In this case, there are two of them, corresponding to the so-called 
geometric connection and its complex conjugate. We will denote the perturbative series 
attached to these saddle-points by $\varphi_{g,c}(\tau)$, where $g (c)$ refers to the geometric 
(respectively, conjugate) connection. They can be computed explicitly up to the very high order, and their very first terms read as 

\be
\varphi_g(\tau)=  \sum_{k \ge 0} a_k \tau^k= 3^{-1/4} \left( 1+  {11 \pi \over {\sqrt{3}}\cdot  36} \tau+ {697 \pi^2 \over 7776} \tau^2+ \cdots \right), \qquad 
\varphi_c(\tau)= \varphi_g(-\tau). 
\ee

The partition function (or Andersen--Kashaev invariant) will be denoted by $\CI (\tau)$. As shown in \cite{ggm1}, it 
can be expressed as the lateral Borel resummation of a trans-series involving the above perturbative series. 
Not surprisingly, this expression depends on the region of the $\tau$ plane which we consider. When $\tau$ is slightly above the positive real axis, one simply finds

\be
\label{I1}
\CI(\tau) = -2 \ri \, \re^{-{V \over 2 \pi \tau}} s(\varphi_c)(\tau), 
\ee

where $V=2.029883...$ is the volume of the figure-eight knot, and it is the classical action of the conjugate connection in complex 
CS theory. In (\ref{I1}), the resummation is along the direction set by the argument of $\tau$. However, as 
we move to the region slightly above the negative real axis, we find the expression 

\be
\label{I2}
\CI(\tau)=-2 \ri \, \re^{-{V \over 2 \pi \tau}} s\left(\varphi_c\right)(\tau) M_1 (\tilde q) 
+ 2 \, \re^{{V \over 2 \pi \tau}} s\left(\varphi_g\right)(\tau) M_2(\tilde q).  
 \ee
 
Here, 

\be
\tilde q= \re^{-{2 \pi \ri \over \tau}}, 
\ee

and the resummation is also along the direction set by the argument of $\tau$. 
$M_{1,2}(\tilde q)$ are power series in $\tilde q$. Their very first terms read

\be
\ba
M_1 (q)&= 1 - 8 q -9 q^2 + 18 q^3+ 46 q^4+\CO(q^5),\\
M_2 (q)&=-9 q - 3 q^2 + 39 q^3 + 69 q^4 + \CO(q^5), 
\ea
\ee

and their exact expressions were conjectured in \cite{ggm1}. We will not need them 
here, but we note that they are convergent power series with radius of convergence $R=1$. 


The result (\ref{I2}) has a very clear physical interpretation. The terms 
$\tilde q^n \exp(\pm V/(2 \pi \tau))$ correspond to contributions of 
complex instantons, whose actions are of the form 

\be
\mp {V \over 2 \pi}+ 2 \pi \ri n, \qquad n \in \IZ_{>0}. 
\ee

The additional term $2 \pi \ri n$ is due to the multivaluedness of the CS action. Therefore, the expression (\ref{I2}) can be 
regarded as a multi-instanton expansion in which we sum over an infinite 
number of exponentially small corrections (which in fact arise as Borel 
singularities of the series $\varphi_{g,c}(\tau)$, see \cite{ggm1} for a detailed explanation). In terms of the formalism we 
set in section \ref{tss-sec}, we have a slightly more general trans-series than (\ref{phits}). Let us denote 

\be
\label{q-series}
M_1( q)= \sum_{n \ge 0} \mu_{1, n}  q^n, \qquad M_2( q)= \sum_{n \ge 0} \mu_{2, n}  q^n. 
\ee

Then, we can write the underlying trans-series as 

\be
\Phi(\tau)=  -2 \ri \, \re^{-{V \over 2 \pi \tau}} \sum_{\ell \ge 0} \tilde q^\ell  \varphi_{c, \ell} (\tau) + 2 \, \re^{{V \over 2 \pi \tau}}\sum_{\ell \ge 1} \tilde q^\ell  \varphi_{g, \ell}(\tau), 
\ee

where 

\be
\varphi_{c, \ell} (\tau)= \mu_{1, \ell} \varphi_{c} (\tau), \qquad \varphi_{g, \ell} (\tau)=\mu_{2, \ell} \varphi_{g} (\tau). 
\ee

Due to the presence of two different actions, we have two different functions $\CG_n(y)$ to consider, and they are given by 

\be
\label{csGs}
\CG_n^1(y)= (-1)^n a_n \sum_{\ell \ge 0} \mu_{1, \ell} y^\ell= (-1)^n a_n M_1(y), \qquad \CG_n^2 (y)=  a_n \sum_{\ell \ge 0} \mu_{2, \ell} y^\ell=a_n M_2(y),  
\ee

where in this case $y= \tilde q$. 
Therefore, it is clear that the convergence of the series $M_{1,2}(q)$ defined in (\ref{q-series}) 
guarantees the convergence of the partial series, and 
it is obvious from (\ref{csGs}) that the radius of convergence of $\CG^i_n(y)$, $i=1,2$ are the same, for all $n$. 

Although we have focused on a particular example, the resulting structure seems to be typical of many trans-series in complex CS theory:
the partial series are given by convergent $\tilde q$ series. As we have pointed out, this makes it possible to have a simple resurgent structure without further resummations.
