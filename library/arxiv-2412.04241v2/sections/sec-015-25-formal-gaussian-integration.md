---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-015-25-formal-gaussian-integration
section_title: "Formal Gaussian integration"
section_number: 2.5
pages: 28-33
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 0.907
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.FGI}

In this section we review a collection of formal power series at roots of unity
that were defined by formal Gaussian integration in~\cite{DG} for $\z=1$ and in
~\cite{DG2} for arbitrary complex roots of unity $\z$. The input to define these
power series was a Neumann--Zagier datum, which, in the case of perturbative complex
Chern--Simons theory, comes from an ideal triangulation of a 3-manifold and a solution
of its gluing equations.
For the simpler case of a single matrix $A$ and the Nahm equations, and for
$\zeta=1$, the same series were found in~\cite{Zagier:dilog}.
We will tailor the definition of
these series for the purpose of our paper and match them with the associated series
$\Phitof_A(t,q)$ of the admissible series $F_A(t,q)$ of~\eqref{FAdef}. The most
important point here is that formal Gaussian integration gives series with
coefficients that are manifestly algebraic functions.

We now recall the definition of $\Phitof_{A,m}$. Fix a symmetric $N \times N$ matrix
$\Lambda$ with integer entries. For a $\BQ$-algebra $R$, formal Gaussian integration
is a map $\langle \cdot \rangle: R[\![w,w^3h^{-1},h]\!] \to R[\![ h]\!]$, where
$w=(w_1,\dots,w_N)$, defined by
\be
\label{eq:bracket}
\left\langle
f(w,h)
\right\rangle_{\Lambda}
\;:=\; \exp\left(
{\frac{h}{2}\sum_{i,j=1}^N (\Lambda^{-1})_{i,j}
\frac{\partial}{\partial w_i}
\frac{\partial}{\partial w_j}}\right)
f(w,h) \Big|_{w=0}
\inn R[\![h]\!]\,.
\ee
This formally recovers the integral
\be
\frac{\int e^{-\frac{1}{2h}w^t \Lambda \,w}f(w,h) \, dw}{
\int e^{-\frac{1}{2h}w^t \Lambda \,w} \, dw}
\inn R[\![h]\!]\,.
\ee
Starting with the admissible series $F_{A}(t,q)$ of equation~\eqref{FAdef} and taking
$q=\z_me^{h}$, summing over congruences modulo $m$, and applying Poisson
summation assuming that one term dominates, leads formally to the integral
\be
\label{eq:inform.int}
\begin{aligned}
&\frac{1}{(q;q)_{\infty}^{N}}\sum_{k\in(\BZ/m\BZ)^N}
(-1)^{\mathrm{diag}(A)\cdot k}q^{\frac{1}{2}(k^t A k
+ \mathrm{diag}(A)\cdot k)}t_1^{k_1} \cdots t_{N}^{k_N}
\int \prod_{j=1}^{N}(q^{k_j+1}e^{w_j};q)_{\infty}\\
&\quad\times \exp\Big(\frac{1}{h}\Big(
\frac{\diag(A)\cdot w\pi i}{m}+\frac{1}{2}w^tAw+w\cdot\log(t)\Big)
+(\frac{\diag(A)}{2}+k^{t}A)\cdot w\Big)
\frac{dw}{(mh)^{N}}\,.
\end{aligned}
\ee
To define the integral in equation~\eqref{eq:inform.int} precisely, we use the
same coordinates as we did previously for the Habiro ring 
\be
q\=\z_me^{h}\=\z_m+x\,,\qquad
h\=\log(1+x/\z_m)\,.
\ee
together with the expansion of the infinite Pochhammer symbol (see~\eqref{logpocm}) 
from which we remove four terms
\be
\label{Psikdef}
\begin{small}
\begin{aligned}
&\psi_{k,z,\z_m}(w,x) \= 
((\z_m+x)^{k+1}ze^w;\z_m+x)_{\infty} \cdot 
\exp\Big(-\frac{\Li_{2}(z^{m})}{m^2\log(1+x/\z_m)}\\
&-\frac{\Li_{1}(z^{m})}{m^2\log(1+x/\z_m)} w 
 -\frac{\Li_{0}(z^{m})}{m^2\log(1+x/\z_m)}w^2
+ \sum_{\ell=0}^{m-1}
\big(\frac{1}{2}-\frac{k+\ell+1}{m}\big)\log(1-\z_m^{k+\ell+1}z) \Big)\,,
\end{aligned}
\end{small}
\ee
where $\psi_{k,z,\z_m}(w,x)\in1+x\BQ(z,\z_m)[\![w,w^3x^{-1},x]\!]$.
The integral~\eqref{eq:inform.int} is dominated by the leading term given by
the exponential of $h^{-1}$ times the function
\be
\label{eq:Vgen}
\frac{1}{2}w^tAw +\sum_{j=1}^{N} -\frac{\Li_{2}(1-e^{mw_j})}{m^2}
+\frac{w_j}{m}\log\Big(\frac{(-1)^{A}t_j^m}{1-e^{mw_j}}\Big) \,,
\ee
whose critical points are exactly $1/m$ times the logarithm of $z$, where
$z=z(t)\in (\BZ[\![t]\!])^N$ is the unique solution to the equations~\eqref{zjt}.
The critical values of equation~\eqref{eq:Vgen} are given by
\be 
\label{Vt}
V^\FGI(t) 
\= -\sum_{j=1}^N \Li_2(1-z_j(t))
- \frac{1}{2} \sum_{i,j=1}^N A_{ij} \log(z_i(t))\log(z_j(t)) \inn \BQ[\![t]\!],
\qquad V^\FGI(0)\=0 \,.
\ee
The above discussion leads to the following definition.

\begin{definition}
\label{def.FGI}
We let:
\be
\label{PhiFGIdef}
\Phitof_{A,m}^\FGI(t,x) \= \sum_{k \in (\BZ/m\BZ)^N}  I_{A,m,k}(t^{1/m},x)\,,
\ee
where $I_{A,m,k}(t,x)$ is given by a formal Gaussian integral
\be
\label{Ikdef}
\begin{small}
\begin{aligned}
&I_{A,m,k}(t,x)
\=\frac{(-1)^{\mathrm{diag}(A)\cdot k}
  q^{\frac{1}{2}(k^t A k + \mathrm{diag}(A)\cdot k)}t_1^{k_1}
\cdots t_{N}^{k_N}
\exp\Big(\frac{V(t^{m})}{m^2\log(1+x/\z_m)}\Big)}{\sqrt{m^N
  \det(-\Lambda(t^m))\prod_{j=1}^{N}(1-z_{j}(t^{m})^{\frac{1}{m}})}}\\
&\times\prod_{j=1}^{N}\Big(
\prod_{\ell=1}^{m-1-k_j}
\Big(\frac{1-\z_m^{k_{j}+\ell}z_{j}(t^{m})^{\frac{1}{m}}}{1-\z_m^{\ell+k_j}}
\Big)^{\frac{1}{2}-\frac{k_{j}+\ell}{m}}\!\!\!\!
\prod_{\ell=m+1-k_j}^{m}
\Big(\frac{1-\z_m^{k_{j}+\ell}z_{j}(t^{m})^{\frac{1}{m}}}{1-\z_m^{\ell+k_j}}
\Big)^{\frac{1}{2}-\frac{k_{j}+\ell}{m}}
(1-\z_m^{\ell+k_j})\Big)\\
&\qquad\times\Big\langle
\exp\Big(\Big(k^{t}A+\frac{1}{2}\mathrm{diag}(A)\Big)
\Big(w+\frac{1}{m}\log z(t^{m})\Big)\Big)
\prod_{j=1}^{N}
\psi_{k_j,z_{j}(t^{m})^{\frac{1}{m}},\z_m}(w_j,x)
\Big\rangle_{\Lambda(t^{m})}
\end{aligned}
\end{small}
\ee
with
\be
\label{lt}
\Lambda(t)\=-A-\mathrm{diag}\Big(\frac{z(t)}{1-z(t)}\Big) \,.
\ee
\end{definition}
An important and non-trivial property is that $I_{A,m,k}(t,x)$ is $m$-periodic
in $k$, so that equation~\eqref{PhiFGIdef} makes sense. This follows from the
definition of $I_{A,m,k}(t,x)$ and a simple change of coordinates in the Gaussian
integration as done in~\cite{AarhusII} or~\cite{GSW}.

Note that the exponential prefactor of all $I_{A,m,k}(t,x)$ is independent of $k$.
Said differently, these formal Gaussian integrals are equi-peaked Gaussians.
Consider
\be
\label{dt}
\delta^\FGI(t)\= \prod_{j=1}^Nz_j(t)^{-A_{jj}}(1-z_j(t)) \det(-\Lambda(t))\,,\qquad
\delta^\FGI(0)\=1 \,.
\ee
and 
\be
\begin{aligned}
\label{Umtdef}
U_m^\FGI(t) &\= \frac{1}{m^N}
\prod_{j=1}^{N}\frac{(1-z_{j})D_{\z_m}(1)}{(1-z_{j}^{\frac{1}{m}})
D_{\z_m}(z_{j}^{\frac{1}{m}})}
\sum_{k \in (\BZ/m\BZ)^N}
\frac{
\z_m^{\frac{1}{2}\mathrm{diag}(A)\cdot k}
t^{\frac{k}{m}}z^{\frac{Ak}{m}+\diag(A)(\frac{1}{2m}-\frac{1}{2})}}
{(-\z_m)^{-\frac{1}{2}k^{t}Ak}\prod_{j=1}^{N}(\z_mz_{j}^{\frac{1}{m}};\z_m)_{k_j}}\,,
\end{aligned}
\ee
where $z_j=z_j(t)$ and 
\be\label{cycdl}
D_{\z_m}(z)
\=
\prod_{\ell=1}^{m-1}
(1-\z_m^{\ell}z)^{\frac{\ell}{m}}\,.
\ee
Note that~\eqref{Umtdef} is a well-defined power series in $t$ and $U_m^\FGI(0) \=1$.
Recall the ring $S^{(m)}$ defined in~\eqref{RA} and let
$S^{(m)}_\BQ=S^{(m)} \otimes \BQ$. 

\begin{lemma}
\label{lem.PhiA}
For every positive integer $m$ we have: 
\be
\label{eq.PhiA}
\log \Phitof^\FGI_{A,m}(t,x) \inn \frac{V^\FGI(t)}{m^2\log(1+x/\z_m)}
-\frac{1}{2} \log \delta^\FGI(t) + \log U_m^\FGI(t) + x S^{(m)}_\BQ[\![x]\!] 
\ee
and $\delta^\FGI(t) \in S$ and $m^{N m} U_m^\FGI(t)^{2m} \in S^{(m)}$. 
\end{lemma}

\begin{proof}
A priori, the coefficients of $x^k$ for $k>1$ in the LHS of equation~\eqref{eq.PhiA}
are in the bigger ring $\BZ[\z_m,t^{\pm 1/m}, z^{\pm 1/m}, \tfrac{1}{\delta}]/(1-z-(-1)^A
t z^A)$. The endomorphism $\gamma_j$ that sends $z_j(t)^{1/m}$ to $\z_m z_j(t)^{1/m}$
and fixes $S^{(m)}$ satisfies
\be
\gamma_j I_{A,m,k}(t,x) \= I_{A,m,k+\delta_j}(t,x) \,.
\ee
This follows from applying $\gamma_j$ and also a change of variables to sending
$w \mapsto w + h$. Therefore, the coefficients in the LHS of equation
~\eqref{eq.PhiA} is invariant under $\gamma_j$ and hence an element of~$S^{(m)}$.
For $U_{m}^\FGI(t)^{2m}$, we see that it is in $m^{-2N}S^{(m)}$. To see
that a factor of $m$ cancels we use
\be
D_{\z_m}(1)^{24m} \= m^{12m}\,,
\ee
which follows from properties of the multiplier system of the Dedekind
$\eta$-function~\cite{Rademacher}.
\end{proof}

We will now improve on the sets where the coefficients of the $x$-series expansions
lie. For
$m,m'\in\BZ_{>0}$ with $m'$ prime to $m$ and $k\in(\BZ/m\BZ)^{N}$ we define
\be
\label{FGIcong}
\CS_{A,m,k}(t,q) \;=\!\!\!\!
\sum_{\underset{\ell\equiv_m k}{\ell\in(\BZ/mm'\BZ)^{N}}}
\frac{(q;q)_{k_1}\cdots(q;q)_{k_N}I_{A,mm',\ell}(t^{1/m},x)}
{(-1)^{\mathrm{diag}(A)\cdot k}q^{\frac{1}{2}(k^t A k + \mathrm{diag}(A)\cdot k)}
t_1^{k_1/m} \cdots t_{N}^{k_N/m}} \,,\quad q\=\z_{mm'}+x\,.
\ee
Notice that when $m=1$ we have
\be
\CS_{A,1,0}(t,\z_{m'}+x) \= \Phitof_{A}^{\FGI}(t^{m'},\z_{m'}+x)\,.
\ee
The sets that the coefficients of the expansions of $\log(\CS_{A,m,k})$ live in
is improved by Dwork-like quotients. In particular the pole and the constant
term in the expansion~\eqref{Ikdef} becomes better.

\begin{lemma}
\label{lem:dwork.diff.VU} 
For all primes $p$ and positive integers $m$ with $(m,p)=1$, we have 
\be
\label{dphiA2}
\log(\CS_{A,m,k}(t^p,q^p)) -p\log(\CS_{A,m,k}(t,q))
\inn x^{-1}S^{(m)}_p[\tfrac{1}{p},z^{1/m}] [\![x]\!]\,,\quad
  q\=\z_{m}+x\,.
\ee
\end{lemma}

\begin{proof}
To prove the result we need to check two conditions. For $V(t)$ of equation
~\eqref{Vt} and a single term in the sum $U_{m}(t)$ of equation~\eqref{Umtdef}
\be
U_{m,k}(t) \=
z^{\frac{Ak}{m}+\diag(A)(\frac{1}{2m}-\frac{1}{2})}
\prod_{j=1}^{N}\frac{(1-z_{j})D_{\z_{m}}(1)}{m(1-z_{j}^{\frac{1}{m}})
D_{\z_{m}}(z_{j}^{\frac{1}{m}})} \frac{(\z_{m};\z_{m})_{k_j}}
{(\z_{m}z_{j}^{\frac{1}{m}};\z_{m})_{k_j}}\,,
\ee
we need to show that
\be
\label{eq:V.dwork}
\frac{V(t^p)}{p}-pV(t)
 
 
 
\inn pS^{(1)}_{p}\,
\ee
and
\be
\log(\delta(t^p)^{-1}U_{m,k}(t^p)^2) -p
\log(\delta(t)^{-1}U_{m,k}(t)^2) \in pS^{(m)}_{p}[z^{1/m}] \,.
\ee
Equation~\eqref{Vt} implies that
\be
\label{pe0}
\frac{V(t^p)}{p}-pV(t)
\=
\frac{1}{p}\fr\Li_{2}(tz^A)-p\Li_{2}(tz^A)
-\frac{1}{2p}\fr\log(z)^tA\log(z)+\frac{p}{2}\log(z)^tA\log(z) \,.
\ee
Since $z$ is a unit, there exists $\eta=\eta(z)\in S^{(1)}_p$ such that
$\fr(z)\=z^p e^{p \eta}$. We have
\be
\label{pe1}
\begin{aligned}
\fr\Li_{2}(tz^A)-p^2\Li_{2}(tz^A)
&\=
\Li_{2}(t^pz^{pA}e^{p\eta})-p^2\Li_{2}(tz^A)\\
&\inn
\Li_{2}^{(p)}(t^pz^{pA})
+\Li_{1}(t^pz^pz^{pA})^tpA\eta
+S^{(1)}_p\,,
\end{aligned}
\ee
which follows from $
\Li_{n}(ze^x)\=\sum_{k=0}^{\infty}\frac{x^k}{k!}\Li_{n-k}(z)\,,
$
and $\Li_{n}(z)\in\BZ[z,(1-z)^{-1}]$ for $n\leq0$. Moreover, we have
\begin{align}
\label{pe2}
\fr\log(z)^tA\log(z)-p^2\log(z)^tA\log(z)
& \=
2p\log(z^p)^tA\eta
+p^2\eta^tA\eta \\
\label{pe3}
A \Li_{1}(t^pz^pz^{pA})+ A \log(z^p)
& \=
\Li_1((1-z)^p)-p\Li_{1}(1-z)A
\=
pA \Li_{1}^{(p)}(1-z)\,.
\end{align}
Combining~\eqref{pe1}, ~\eqref{pe2} and ~\eqref{pe3} with
$\Li_{n}^{(p)}(1-z)\in S^{(1)}_{p}$, we deduce that the right hand side of
equation~\eqref{pe0} is also an element of $S^{(1)}_{p}$. Finally, as
$\delta(t)^{-m}U_{m,k}(t)^{2m}$ is a $p$-unit there is a $\beta\in S^{(1)}_p$ such that
$\fr(\delta(t)^{-m}U_{m,k}(t)^{2m})\=\delta(t)^{-mp}U_{m,k}(t)^{2mp} e^{p \beta}$, and a
similar argument can be used to deduce the remaining statements. 
\end{proof}

\begin{remark}
If $U_{m}^{\FGI}(t)$ is a $p$-unit then we can lift the statement of
equation~\eqref{dphiA2} to
\be
\log(\Phitof^{\FGI}_{A}(t^p,q^p)) -p\log(\Phitof^{\FGI}_{A}(t,q))
\inn x^{-1}S^{(m)}_p[\tfrac{1}{p}] [\![x]\!]\,,\quad
q\=\z_{m}+x\,.
\ee
\end{remark}

The final property we will need is that $\CS_{A,m,k}$ satisfies a system
of $q$-difference equations.

\begin{lemma}
\label{lem.cs.qdiff}
For a positive integer $m$ and residue class $k\in\{0,\cdots,m-1\}^N$, the
function $t^{k}\CS_{A,m,k}(t,q)$ defined in equation~\eqref{FGIcong} satisfies
the $q$-difference equations
\be
\label{PhiFGIAshift}
\begin{aligned}
  &\sum_{\ell=0}^{m}(-1)^{\ell}q^{-\ell(\ell-1)/2}
  \binom{m}{\ell}_{\!\!q^{-1}}\s_j^{\ell}\Big(t^{k}\CS_{A,m,k}(t^{m},q)\Big)\\
  &\=
  (-1)^{A_{j,j}m(m+1)/2}q^{A_{j,j}m(m+1)/2}t_i^{m}
  \prod_{i=1}^N \s_i^{mA_{i,j}}\Big(
  t^{k}\CS_{A,m,k}(t^{m},q)\Big)\,,
\end{aligned}
\ee
where $\s_jt:=(t_1,\dots,qt_j,\dots, t_N)$.
\end{lemma}

\begin{proof}
From the definition of $I_{A,m,k}(t,x)$ and a simple change of coordinates in the
Gaussian integration as done in~\cite{AarhusII} or~\cite{GSW}, it is easy to see for
$\ell\in(\BZ/mm'\BZ)^{N}$ that $I_{A,\ell}(t,x)$ satisfies
\be
\label{SAshift}
I_{A,mm',\ell}(t,x) - I_{A,mm',\ell}(\s_j t,x) \= (-1)^{A_{j,j}} t_{j} q^{A_{j,j}}
I_{A,mm',\ell-\delta_j}\bigg(\prod_{i=1}^N \s_i^{A_{i,j}}t,x\bigg),
\qquad j\=1,\dots,N\,,
\ee
where $\delta_j$ is the vector whose only non-zero entry is $1$ in the $j$-th
position. Therefore, from the basic properties of Gaussian polynomials we see that
\be
\begin{aligned}
&\sum_{i=0}^{m}(-1)^{i}q^{-i(i-1)/2}\binom{m}{i}_{\!\!q^{-1}}I_{A,mm',\ell}(\s_j^{i}t,x)
\\
&\= (-1)^{A_{j,j}m(m+1)/2}q^{A_{j,j}m(m+1)/2}t_i^{m}
I_{A,mm',\ell-m\delta_i}\bigg(\prod_{i=1}^N \s_i^{mA_{i,j}}t,q\bigg)\,.
\end{aligned}
\ee
The rest of the proof follows from the definition of $\CS_{A,m,k}$.
\end{proof}
