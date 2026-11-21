---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-020-42-the-appell-lerch-sums
section_title: "The Appell-Lerch sums"
section_number: 4.2
pages: 32-37
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.959
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.ex2}

This section is devoted to the proof of Theorem~\ref{thm.ex2}.
The $q$-difference equation~\eqref{ex2} has Newton polygon shown in
Figure~\ref{f.ex2}.

\begin{figure}[!htpb]
\begin{center}
\begin{tikzpicture}[scale=0.8,baseline=-3]
\draw[<->,thick] (-1.5,0) -- (5.5,0);
\draw[<->,thick] (0,-1.5) -- (0,3.5);
\filldraw (2,0) circle (2pt);
\filldraw (2,2) circle (2pt);
\filldraw (0,2) circle (2pt);
\filldraw (4,0) circle (2pt);
\draw (0,2) -- (2,0) -- (4,0) -- (2,2) -- cycle;
\fill[blue,opacity=0.2] (0,2) -- (2,0) -- (4,0) -- (2,2) -- cycle;
\node at (3,-0.3) {$f^{(0)}$};
\node at (0.7,0.6) {$f^{(-1)}$};
\node at (1,2.3) {$g^{(0)}$};
\node at (3.3,1.5) {$g^{(-1)}$};
\end{tikzpicture}
\caption{The Newton polygon of Equation~\eqref{ex2}.}
\label{f.ex2}
\end{center}
\end{figure}

\noindent
To begin with, the boundary of the lower Newton polygon consists of one edge of
slope zero and one edge of slope $1$. The edge of slope zero has a solution of
the form
\be
f^{(0)}(t,q)=
\sum_{k=0}^{\infty}\alpha_{k}(q)t^{k}\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\;\text{where}\;
\alpha_{k}(q)q^{2k}\rind^{2}+q^{k}
\rind\alpha_{k-1}(q)-q^{k}\rind\alpha_{k}(q)-\alpha_{k-1}(q)
=0.
\ee
Therefore, as $\alpha_{k}(q)=0$ for $k<0$, we get the indicial polynomial
\be
\alpha_{0}(q)(\rind^{2}-\rind) = 0
\ee
and so $\rind=1$. Then we have
\be
(q^{2k}-q^{k})\alpha_{k}(q)-(1-q^k)\alpha_{k-1}(q)=0
\quad\text{so}\quad
-q^{k}a_{k}=a_{k-1}.
\ee
Therefore, normalising so that $\alpha_{0}(q)=1$,
\be
\hat{f}^{(0)}(t,q)=\sum_{k=0}^{\infty}(-1)^{k}q^{-k(k+1)/2}t^{k}.
\ee
This is of course divergent for $|q|<1$ so we must $q$-Borel resum. The affect on
the Newton polygon is as follows
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-1,0) -- (3,0);
\draw[<->,thick] (0,-1) -- (0,2);
\filldraw (1,0) circle (2pt);
\filldraw (1,1) circle (2pt);
\filldraw (0,1) circle (2pt);
\filldraw (2,0) circle (2pt);
\draw (0,1) -- (1,0) -- (2,0) -- (1,1) -- cycle;
\fill[blue,opacity=0.2] (0,1) -- (1,0) -- (2,0) -- (1,1) -- cycle;
\node at (1.5,-0.35) {\begin{tiny}$f^{(0)}$\end{tiny}};
\node at (4,0.4) {$\Bor_{1}$};
\draw[->,ultra thick] (3.5,0) -- (4.5,0);
\draw[<->,thick] (-1+6,0) -- (3+6,0);
\draw[<->,thick] (0+6,-1) -- (0+6,2);
\draw (-0.1+6,1) -- (0.1+6,1);
\filldraw (1+6,0) circle (2pt);
\filldraw (1+6,1) circle (2pt);
\filldraw (2+6,1) circle (2pt);
\filldraw (2+6,0) circle (2pt);
\draw (1+6,1) -- (1+6,0) -- (2+6,0) -- (2+6,1) -- cycle;
\fill[blue,opacity=0.2] (1+6,1) -- (1+6,0) -- (2+6,0) -- (2+6,1) -- cycle;
\node at (1.5+6,-0.35) {\begin{tiny}$\Bor_{1}f^{(0)}$\end{tiny}};
\end{tikzpicture}
\end{center}
Now notice that
\be
\Bor_{1}{\hat{f}^{(0)}}(\xi,q) = \sum_{k=0}^{\infty}\xi^{k}
= \frac{1}{1-\xi}
\ee
and so we find
\be
\label{ex2.f0}
f^{(0)}(t,\lambda ,q)
=
\mathcal{L}_{1}\mathcal{B}_{1}(\hat{f}^{(0)})(t,\lambda ,q)
=
\frac{1}{\theta(\lambda ;q)}\sum_{\ell}(-1)^{\ell}
\frac{q^{\ell(\ell+1)/2}\lambda ^{\ell}}{1-\lambda tq^{\ell}}.
\ee
This is the Appell-Lerch sum whose modular properties were studied in Zwegers
thesis~\cite{Zwegersthesis}. Now the bottom edge of slope $-1$ must be divided by
a $\theta$-function to get a zero slope. The effect on the Newton polygon is as
follows.
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-1,0) -- (3,0);
\draw[<->,thick] (0,-1) -- (0,2);
\filldraw (1,0) circle (2pt);
\filldraw (1,1) circle (2pt);
\filldraw (0,1) circle (2pt);
\filldraw (2,0) circle (2pt);
\draw (0,1) -- (1,0) -- (2,0) -- (1,1) -- cycle;
\fill[blue,opacity=0.2] (0,1) -- (1,0) -- (2,0) -- (1,1) -- cycle;
\node at (0.37,0.19) {\begin{tiny}$f^{(-1)}$\end{tiny}};
\node at (4,0.4) {$\theta(q^{-1}t;q)^{-1}$};
\draw[->,ultra thick] (3.5,0) -- (4.5,0);
\draw[<->,thick] (-1+6,0) -- (3+6,0);
\draw[<->,thick] (0+6,-1) -- (0+6,2);
\draw (-0.1+6,1) -- (0.1+6,1);
\draw (2+6,-0.1) -- (2+6,0.1);
\filldraw (1+6,0) circle (2pt);
\filldraw (1+6,1) circle (2pt);
\filldraw (0+6,0) circle (2pt);
\filldraw (2+6,1) circle (2pt);
\draw (0+6,0) -- (1+6,0) -- (2+6,1) -- (1+6,1) -- cycle;
\fill[blue,opacity=0.2] (0+6,0) -- (1+6,0) -- (2+6,1) -- (1+6,1) -- cycle;
\node at (0.5+6,-0.25) {\begin{tiny}$\hat{f}^{(-1)}$\end{tiny}};
\end{tikzpicture}
\end{center}
Therefore, the bottom edge of slope minus one has a solution of the form
\be
f^{(-1)}(t,q)
=
\theta(q^{-1}t;q)^{-1}\hat{f}^{(-1)}(t,q)
=
\theta(q^{-1}t;q)^{-1}\sum_{k=0}^{\infty}\alpha_{k}(q)t^{k}
\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\ee
where
\be
(1-q^{k}\rind)\alpha_{k}(q)+q^{k}\rind(1-q^{k-1}\rind)\alpha_{k-1}(q)=0.
\ee
Therefore, the indicial polynomial is given by
\be
(1-\rind)\alpha_{0}(q)=0
\ee
and so $\rind=1$. Then we see that
\be
(1-q)\alpha_{1}(q)=0
\ee
and so $\alpha_{k}=0$ for $k\neq 0$. Therefore,
\be
\label{ex2.f-1}
f^{(-1)}(t,q)=\theta(q^{-1}t;q)^{-1}\,.
\ee
Now following similar calculations we find that
\be
\Bor_{1}\hat{g}^{(0)}(\xi,q)
=
-\sum_{k=-\infty}^{-1}\xi^{k}
=
-\frac{\xi^{-1}}{1-\xi^{-1}}
=
\frac{1}{1-\xi}
\ee
and so
\be
\label{ex2.g0}
g^{(0)}(t,\mu ,q)
=
\frac{1}{\theta(\mu ;q)}\sum_{\ell}(-1)^{\ell}
\frac{q^{\ell(\ell+1)/2}\mu ^{\ell}}{1-\mu tq^{\ell}} \,.
\ee
Then finally, we have
\be
\label{ex2.g1}
g^{(-1)}(t,q)=\theta(q^{-1}t;q)^{-1} \,.
\ee
Consider the inhomogeneous gauge transformation (see Section~\ref{sub.cat})
\be
U(t,\lambda,q)
=
\begin{pmatrix}
  0 & 1\\
  1 & -t
\end{pmatrix}
\begin{pmatrix}
  1 & 0\\
  f^{(0)}(t,\lambda,q) & f^{(-1)}(t,q)
\end{pmatrix}
\ee
and the similar one for $V$. With the definition of the fundamental matrices
given in Equations~\eqref{UVex2} and associated monodromy, we then have that

\be
\begin{aligned}
\vM(t,\lambda,q)
&=
\begin{pmatrix}
  1 & 0\\
  g^{(0)}(t,\mu,q) & g^{(-1)}(t,q)
\end{pmatrix}^{-1}
\begin{pmatrix}
  1 & 0\\
  f^{(0)}(t,\lambda,q) & f^{(-1)}(t,q)
\end{pmatrix}\\
&=
\theta(q^{-1}t,q)
\begin{pmatrix}
  \theta(q^{-1}t,q)^{-1} & 0\\
  -g^{(0)}(t,\mu,q) & 1
\end{pmatrix}
\begin{pmatrix}
  1 & 0\\
  f^{(0)}(t,\lambda,q) & \theta(q^{-1}t,q)^{-1}
\end{pmatrix}\\
&=
\begin{pmatrix}
  1 & 0\\
  \vM_{2,1}(t,\lambda ,\mu ,q) & 1
\end{pmatrix}
\end{aligned}
\ee

where

\be
\begin{aligned}
\vM_{2,1}(t,\lambda ,\mu ,q)
&=
\theta(q^{-1}t;q)f^{(0)}(t,\lambda ,q)-\theta(q^{-1}t;q)g^{(0)}(t,\mu ,q)\\
&=
\frac{\theta(q^{-1}t;q)}{\theta(\lambda ;q)}\sum_{\ell}(-1)^{\ell}
\frac{q^{\ell(\ell+1)/2}\lambda ^{\ell}}{1-\lambda tq^{\ell}}
-\frac{\theta(q^{-1}t;q)}{\theta(\mu ;q)}\sum_{\ell}(-1)^{\ell}
\frac{q^{\ell(\ell+1)/2}\mu ^{\ell}}{1-\mu tq^{\ell}} \,.
\end{aligned}
\ee
Using Equation~(7) of Proposition~1.4 of \cite{Zwegersthesis}, we can deduce that
\be
\label{M21sander}
\vM_{2,1}(t,\lambda ,\mu ,q)
=
-\frac{(q;q)_{\infty}^{3}\theta(q^{-1}t;q)\theta(\lambda ^{-1}\mu ;q)
  \theta(\lambda ^{-1}\mu ^{-1}t^{-1};q)}{\theta(\lambda ^{-1};q)\theta(\mu ;q)
  \theta(\lambda ^{-1}t^{-1};q)\theta(\mu ^{-1}t^{-1};q)}.
\ee
We now give a second proof of the above equation using elliptic functions and
residues, which is more general and applicable to our third example. Let $m_{2,1}$
denote the function defined by the right-hand side of~\eqref{M21sander}.
We need to prove that the function $\calE_1$, defined by
\be
\calE_1(t,\lambda,\mu,q)
:=
f^{(0)}(t,\lambda,q)
-g^{(0)}(t,\mu,q)
-\frac{m_{2,1}(t,\lambda,\mu,q)}{\theta(q^{-1}t;q)}
\ee
is identically zero. This will follow from the facts, that
$\calE_1$ is holomorphic at $\BC^\times$ (see Lemma~\ref{lem.resAL} below),
and a solution of a first order equation~\eqref{AL.hom.equ}
(see Lemma~\ref{lem.vanish}). 

\begin{lemma}
\label{lem.vanish}
  If $h(t,q)$ is a solution to the equation
\be
\label{AL.hom.equ}
h(qt,q)+th(t,q)=0
\ee
that is holomorphic for $t\in\BC^{\times}$ then $h(t,q)=0$.
\end{lemma}

\begin{proof}
  Every solution is of the form $C(t,q)/\theta(q^{-1}t;q)$ for some elliptic
  function $C(t,q)$. Therefore, $C(t,q)=h(t,q)\theta(q^{-1}t;q)$ is a
  holomorphic elliptic function and therefore constant. However, this implies
  that $h$ has simple poles unless $C=0$.
\end{proof}

\begin{lemma}
  \label{lem.resAL}
  \rm{(a)} The function $f^{(0)}(t,\lambda,q)$ has simple poles at
$t\in \lambda^{-1}q^{\BZ}$ with residue
\be
\begin{aligned}
\Res_{t=q^{-m}\lambda^{-1}}f^{(0)}(t,\lambda,q)\frac{dt}{2\pi it}
&=
\frac{-1}{\theta(q^{m}\lambda;q)}\\
\Res_{t=q^{-m}\mu^{-1}}g^{(0)}(t,\mu,q)\frac{dt}{2\pi it}
&=
\frac{-1}{\theta(q^{m}\mu;q)} \,.
\end{aligned}
\ee
  \rm{(b)}
  The function $\theta(q^{-1}t;q)^{-1}m_{2,1}(t,\lambda,\mu,q)$ has simple
  poles at $t\in q^{\BZ}\lambda^{-1},q^{\BZ}\mu^{-1}$ with residues
  \be
\begin{aligned}
  \Res_{t=q^{-m}\lambda^{-1}}\theta(q^{-1}t;q)^{-1}
  m_{2,1}(t,\lambda,\mu,q)\frac{dt}{2\pi it}
&=
\frac{-1}{\theta(q^{m}\lambda;q)}\\
\Res_{t=q^{-m}\mu^{-1}}\theta(q^{-1}t;q)^{-1}
m_{2,1}(t,\lambda,\mu,q)\frac{dt}{2\pi it}
&=
\frac{1}{\theta(q^{m}\mu;q)}\,.
\end{aligned}
\ee
\end{lemma}
\begin{proof}
  Part (a) follows from a calculation of the residue of the only term in the
  sum that contributes to the residue in Equations~\eqref{ex2.f0}~\eqref{ex2.g0}
  and Equation~\eqref{theta.fun2}. Now for part (b) we note that
\be
\Res_{t=1}\frac{1}{\theta(t;q)}\frac{dt}{2\pi it}=\frac{1}{(q;q)_{\infty}^{3}}
\ee
which follows easily from the Jacobi triple product~\eqref{theta} for example.
Therefore, we see
\be
\begin{aligned}
  &\Res_{t=q^{-m}\lambda^{-1}}
  \frac{m_{2,1}(t,\lambda,\mu,q)}{\theta(q^{-1}t;q)}\frac{dt}{2\pi it}\\
&=
(-1)^{m}q^{m(m+1)/2}\Res_{t=1}
-\frac{(q;q)_{\infty}^{3}\theta(\lambda ^{-1}\mu ;q)
\theta(\mu ^{-1}t^{-1};q)}{\theta(\lambda ^{-1};q)\theta(\mu ;q)
\theta(t^{-1};q)\theta(\lambda\mu ^{-1}t^{-1};q)}\frac{dt}{2\pi it}\\
&=
(-1)^{m}q^{m(m+1)/2}
\frac{\theta(\lambda ^{-1}\mu ;q)
\theta(\mu ^{-1};q)}{\theta(\lambda ^{-1};q)\theta(\mu ;q)
\theta(\lambda\mu ^{-1};q)}\\
&=
\frac{-1}{\theta(q^{m}\lambda;q)}
\end{aligned}
\ee
where we have repeatedly used Equations~\eqref{theta.fun}
and~\eqref{theta.fun2}. A similar computation calculates the other residues
or using Equation~\eqref{theta.fun} we can show that
\be
m_{2,1}(t,\lambda,\mu,q)=-m_{2,1}(t,\mu,\lambda,q) \,.
\ee
\end{proof}

Noting that $\calE_{1}(t,\lambda,\mu,q)$ satisfies Equation~\eqref{AL.hom.equ}
these lemmata show that the potential simple poles of $\calE_{1}(t,\lambda,\mu,q)$
cancel and therefore it is holomorphic on $t\in\BC^{\times}$ and therefore
vanishes.

For completeness, we give a third proof of~\eqref{M21sander} using  
Lemma~\ref{lem.fund}.
\be
\begin{aligned}
\vM_{2,1}(t,\lambda ,\mu ,q)
&=
\theta(q^{-1}t;q)\Lap_{1}\left(\frac{1}{1-\xi}\right)(t,\lambda ;q)
-\theta(q^{-1}t;q)\Lap_{1}\left(\frac{1}{1-\xi}\right)(t,\mu ;q)\\
&=
\frac{\theta(q^{-1}t;q)\theta(\lambda ^{-1}\mu ;q)(q;q)_{\infty}^{3}}{
  \theta(\lambda ^{-1};q)\theta(\mu ;q)}\Res_{\xi=1}\frac{\theta(\lambda ^{-1}
  \mu ^{-1}t^{-1}\xi;q)}{\theta(\xi\lambda ^{-1}t^{-1};q)
  \theta(\xi\mu ^{-1}t^{-1};q)(1-\xi)}\\
&=
-\frac{(q;q)_{\infty}^{3}\theta(q^{-1}t;q)\theta(\lambda ^{-1}\mu ;q)
  \theta(\lambda ^{-1}\mu ^{-1}t^{-1};q)}{\theta(\lambda ^{-1};q)\theta(\mu ;q)
  \theta(\lambda ^{-1}t^{-1};q)\theta(\mu ^{-1}t^{-1};q)} 
\end{aligned}
\ee
concluding the proof of Equation~\eqref{Mex2b}.
From the explicit expression for $\vM_{2,1}$ from Equation~\eqref{M12ex2} and the
modularity of the Dedekind $\eta$-function and the Jacobi $\theta$-function it
follows that $M$ satisfies Equation~\eqref{Mmod} with weight $\kappa=(0,1)$. It
follows that the two cocycles of Equation~\eqref{UVex2} agree.
This implies that neither cocycle depends on $\lambda$ or $\mu$. This
is equivalent to observations in \cite{Zwegersthesis} that the slash operator
acting on the Appell-Lerch sums depends only on the difference of two Jacobi
variables. Then using~\cite[Proposition~1.5]{Zwegersthesis} we can give an
explicit formula for the cocycle in terms of the Mordell integral~\eqref{mordell}
and elementary functions. In particular, we have
\be
\begin{aligned}
f^{(0)}(qt,\lambda ,q)+tf^{(0)}(t,\lambda ,q)
&=1\\
f^{(-1)}(qt,q)+tf^{(-1)}(t,q)
&=0\\
\ti f^{(0)}(t,\lambda ,q)\;\e
\left(\frac{(z+1/2-\tau/2)^{2}}{2\tau}-\frac{1}{8}\right)\sqrt{\tau}
&=
\tau f^{(0)}(t,\lambda ,q)-\tau t^{-\frac{1}{2}}q^{\frac{1}{8}}h(t,q)\\
f^{(-1)}(\ti t,\ti q)\;\e\left(\frac{(z+1/2-\tau/2)^{2}}{2\tau}
  -\frac{1}{8}\right)
\sqrt{\tau}
&=
f^{(-1)}(t,q) \,.
\end{aligned}
\ee
This means that
\be
\begin{aligned}
\det U(t,\lambda ,q)
&=
f^{(-1)}(qt,q)f^{(0)}(t,q)-f^{(-1)}(t,q)f^{(0)}(qt,q)\\
&=
f^{(-1)}(t,q)\left(-tf^{(0)}(t,q)-f^{(0)}(qt,q)\right)\\
&=
-f^{(-1)}(t,q).
\end{aligned}
\ee
Therefore, we see that
\be
\Om_{S}(z,\tau)
=
\begin{pmatrix}
0 & 1\\
1 & -\tilde{t}
\end{pmatrix}
\begin{pmatrix}
\tau^{-1} & 0\\
\frac{\e\left(\frac{1}{8}\right)}{\sqrt{\tau}}\tilde{t}^{-\frac{1}{2}}
\tq^{\frac{1}{8}}\e\left(\frac{z^2}{2\tau}\right)h(z,\tau) &
\frac{\e\left(\frac{1}{8}\right)}{\sqrt{\tau}}\e
\left(-\frac{(z+1/2-\tau/2)^{2}}{2\tau}\right)
\end{pmatrix}
\begin{pmatrix}
0 & 1\\
1 & -t
\end{pmatrix}^{-1}.
\ee
We can vary the contour in Equation~\eqref{mordell} to get the integral
\be
\int_{\zeta\BR}\frac{e^{\pi i (\tau x^{2} + 2 i z x)}}{2\cosh(\pi x)}dx
\ee
for $|\zeta|=1$ and $\zeta\neq\pm i$. This is a convergent integral to a
holomorphic function in $(z,\tau)$ when $\Im(\tau\zeta^2)>0$. Therefore, we
see that from the uniqueness properties of the solutions to the functional
equations of $h$ the Mordell integral~\cite[Proposition~1.2]{Zwegersthesis}
these functions give an analytic extension of $h$ the Mordell integral to
the cut plane $\BC'$. Therefore, the cocycle $\Om_{U,S}(t,q)$ extends to a
holomorphic function for $z\in\BC$ and $\tau\in\BC'$. Since $\Om_{U,T}=I$,
part (c) of Theorem~\ref{thm.ST} concludes that the cocycle $\Om_U$ is modular.
