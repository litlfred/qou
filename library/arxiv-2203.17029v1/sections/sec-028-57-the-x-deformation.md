---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-028-57-the-x-deformation
section_title: "The x-deformation"
section_number: 5.7
pages: 52-62
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.966
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
We will first discuss the two variable holonomic system given by
the homogeneous equations
\begin{subequations}
\be
\label{41x}
\begin{aligned}
tq^{-1}f(q^{-1}t,x,q)+(1-(x^{-1}+x)t)f(t,x,q)+tqf(qt,x,q)
=
0\,,
\end{aligned}
\ee
\be
\label{41x2}
\begin{aligned}
(1-qx)(1-q^{-1}x^{2})f(t,qx,q)&\\
-(x-1)^2(x+1)&(x^2t-x-(q^{-1}+q)t-x^{-1}+x^{-2}t)f(t,x,q)\\
+&(1-qx^2)(1-q^{-1}x)f(t,q^{-1}x,q)
=
0 \,,
  \end{aligned}
  \ee
\be
\label{41x3}
(1-xq)(f(t,qx,q)-x^{-1}f(qt,qx,q))=(1-x^{-1})(f(t,x,q)-qxf(qt,x,q)) \,.
\ee
\end{subequations}
This is not a random system of equations, instead they are the defining equations
of the $t$-deformation of the homogeneous $\hat{A}$-polynomial of the $4_{1}$
knot. This system appeared in~\cite[Eqn.(10)]{GK:desc} and
~\cite[Eqn.(134)]{GGM:peacock}, and it is $q$-holonomic of rank 2 in the variables
$(t,x)$. The system is symmetric under the involution $x \leftrightarrow x^{-1}$
(which corresponds to the Weyl symmetry in the color of the Jones polynomial of
the knot) and our solutions will also be invariant under this involution. As a
result the monodromy connecting $x=0$ to $x=\infty$ is the identity. 

To construct solutions, we will apply the Frobenius method to the
Equation~\eqref{41x}. This has Newton polygon depicted in Figure~\ref{f.41x1}.
Notice that the indicial polynomial $(\rind-1)^2$ for the top edge of
Equation~\eqref{41x1} now becomes $(\rind-x)(\rind-x^{-1})$ for Equation~\eqref{41x}.
We can then normalise so that the solutions satisfy the full system of equations
~\eqref{41x},~\eqref{41x2},~\eqref{41x3}. The solutions to this homogeneous
system are then given by
\be
\label{sols.41.x}
\begin{aligned}
f^{(-1)}(t,x,q)
&=
\frac{\theta(q^{-1}x;q)}{(1-x)\theta(q^{-1}t;q)(q;q)_{\infty}}\sum_{k=0}^{\infty}
\sum_{\ell=0}^{k}(-1)^{k}\frac{q^{k(k+1)/2}x^{2\ell-k}}{(q;q)_{\ell}
  (q;q)_{k-\ell}}t^{k}\\
f^{(1)}(t,x,\lambda_{1},q)
&=
\frac{\theta(t;q)(q;q)_{\infty}}{(1-x)\theta(x;q)}
\Lap_{1/2}\Bor_{1/2}\hat{f}^{(1)}(t,x,\lambda_{1},q)\\
g^{(0,x^{-1})}(t,x,q)
&=
\frac{\theta(q^{-1}x;q)\theta(tx;q)(qx^{2};q)_{\infty}}{\theta(t;q)
  \theta(x^{2};q)(1-x)(q;q)_{\infty}}\sum_{k=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}x^{k}}{(q;q)_{k}(qx^{2};q)_{k}}t^{-k-1}\\
g^{(0,x)}(t,x,q)
&=
\frac{\theta(q^{-1}x^{-1};q)\theta(tx^{-1};q)(qx^{-2};q)_{\infty}}{\theta(t;q)
  \theta(x^{-2};q)(1-x^{-1})(q;q)_{\infty}}\sum_{k=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}x^{-k}}{(q;q)_{k}(qx^{-2};q)_{k}}t^{-k-1}
\end{aligned}
\ee
where
\be
\hat{f}^{(1)}(t,x,q)
=
\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}\frac{q^{\ell^{2}-k\ell}
  x^{2\ell-k}}{(q;q)_{\ell}(q;q)_{k-\ell}}t^{k}.
\ee
Notice that we have
\be
\Bor_{1/2}\hat{f}^{(1)}(t,x,q)
=
\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}(-1)^{k}
\frac{q^{k(k+1)/4+\ell^{2}-k\ell}x^{2\ell-k}}{(q;q)_{\ell}(q;q)_{k-\ell}}t^{k}
\ee
which satisfies
\be
(1-q^{1/2}\xi^2)\Bor_{1/2}\hat{f}^{(1)}(\xi,q)+
(x+x^{-1})\xi\Bor_{1/2}\hat{f}^{(1)}(q^{1/2}\xi,q)-\Bor_{1/2}
\hat{f}^{(1)}(q\xi,q)=0.
\ee
We can complete this to include the inhomogeneous solutions to the system of
Equations~\eqref{41x.inhom}, \eqref{41x2.inhom}, \eqref{41x3.inhom}.
Equations~\eqref{41x.inhom} can be made third order homogenous which has
Newton polygon depicted in Figure~\ref{f.413}. The indicial polynomial of
the top edge now factors as $(\rind-x)(\rind-x^{-1})(\rind-1)$.
This gives two additional solutions as in Section~\ref{sec.4.inhom.x1}.
Firstly we have
\be
\hat{f}^{(0)}(t,x,q)=\sum_{k=0}^{\infty}(-1)^{k}q^{-k(k+1)/2}
(qx;q)_{k}(qx^{-1};q)_{k}t^{k} \,,
\ee
a divergent formal power series solution at $t=0$. Then
\be
  \Bor_{1}f^{(0)}(\xi,x,q)=\sum_{k=0}^{\infty}(qx;q)_{k}(qx^{-1};q)_{k}t^{k} \,,
\ee
which can be analytically continued away from $\xi\in q^{\BZ_{\leq0}}$ using the
relation
\be
(1-\xi)\Bor_{1}\hat{f}^{(0)}(\xi,q)+(x+x^{-1})q\xi \Bor_{1}\hat{f}^{(0)}(q\xi,q)
-q^2\xi \Bor_{1}\hat{f}^{(0)}(q^{2}\xi,q) = 1.
\ee
So we define
\be
\label{f0x}
f^{(0)}(t,x,\lambda_{2},q)
=
(\Lap_{1}\Bor_{1}\hat{f}^{(0)})(t,x,\lambda_{2},q)
=
\frac{1}{\theta(\lambda_{2};q)}\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)}
\lambda_{2}^{k}\Bor_{1}\hat{f}^{(0)}(q^{k}\lambda_{2}t,x,q).
\ee
The second solution is then given by
\be
\label{gGM}
g^{(0)}(t,x,q)
=
\sum_{k=0}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(x;q)_{k+1}(x^{-1};q)_{k+1}}t^{-k-1}.
\ee
We then take
\be
\label{UVex41x}
\begin{aligned}
  U(t,x,\lambda_{1},\lambda_{2},q) &=
  W(f^{(1)}(t,x,\lambda_{1},q), f^{(-1)}(t,x,q), f^{(0)}(t,x,\lambda_{2},q))\:,\\
V(t,q) &= W(g^{(0,x^{-1})}(t,x,q), g^{(0,x)}(t,x,q), g^{(0,1)}(t,x,q)) \,.
\end{aligned}
\ee
Before we give the proof note the immediate symmetries
\be
\begin{aligned}
g^{(0,x^{-1})}(t,x^{-1},q)
&=
g^{(0,x)}(t,x,q),\qquad
&
f^{(-1)}(t,x^{-1},q)
&=
f^{(-1)}(t,x,q),
\\
g^{(0,x)}(t,x^{-1},q)
&=
g^{(0,x^{-1})}(t,x,q),\qquad
&
f^{(-1)}(t,x^{-1},q)
&=
f^{(-1)}(t,x,q),
\\
g^{(0,1)}(t,x^{-1},q)
&=
g^{(0,1)}(t,x,q),\qquad
&
f^{(0)}(t,x^{-1},q)
&=
f^{(0)}(t,x,q)\,.
  \end{aligned}
\ee
\begin{proof}[Proof of Theorem~\ref{thm.41c}]
  First we prove the existence of the elliptic function $m_{2,1}$
  with the properties listed in Theorem~\ref{thm.41c}. 
  Note that the only restriction to an existence of an elliptic function
  with prescribed poles and residues is the vanishing of
  the sum of the residues on a fundamental domain. Here, there are six
  residues, and their sum vanishing is equivalent to
\be
\begin{small}
\begin{aligned}
  1
  &=\frac{\theta(q^{3/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}\\
  &+\frac{\theta(-q^{3/4}\lambda_{1}^{-1};q)\theta(-q^{-1/4}x;q)\theta(-q^{-3/4}x;q)
  \theta(-q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}\\
  &+\frac{\theta(q^{1/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}\\
  &+\frac{\theta(-q^{1/4}\lambda_{1}^{-1};q)\theta(-q^{-1/4}x;q)\theta(-q^{-3/4}x;q)
  \theta(-q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}\\
  &=\left(\frac{\theta(q^{3/4}\lambda_{1}^{-1};q)
  \theta(q^{-3/4}\lambda_{1};q)}{2
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
  +\frac{\theta(q^{1/4}\lambda_{1}^{-1};q)
  \theta(q^{-1/4}\lambda_{1};q)}{2
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}\right)
  \frac{\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)}{\theta(x;q)\theta(x^{-1};q)}\\
  &+\left(\frac{\theta(-q^{3/4}\lambda_{1}^{-1};q)
  \theta(-q^{-3/4}\lambda_{1};q)}{2
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
  +\frac{\theta(-q^{1/4}\lambda_{1}^{-1};q)
  \theta(-q^{-1/4}\lambda_{1};q)}{2
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}\right)
  \frac{\theta(-q^{-1/4}x;q)\theta(-q^{-3/4}x;q)}{\theta(x;q)\theta(x^{-1};q)}\,.
\end{aligned}
\end{small}
\ee
To prove this identity, notice that the right hand side is elliptic in
$\lambda_{1}\mapsto q^{1/2}\lambda_{1}$ and $x\mapsto qx$. Moreover, $\lambda_{1}$
has only one potential simple pole in its fundamental domain and therefore this
is constant in $\lambda_{1}$. Then $x$ has a potential double pole which cancels.
Then specialising the RHS to $\lambda_{1}=q^{1/4}$ and $x=-q^{1/4}$ gives
\be
\frac{\theta(q^{1/2};q)
  \theta(q^{-1/2};q)}{2
  \theta(q^{-3/4};q)\theta(q^{-5/4};q)}
\frac{\theta(-1;q)\theta(-q^{-1/2};q)}{\theta(-q^{1/4};q)\theta(-q^{-1/4};q)}.
\ee
This can be proven to equal one by elementary means using the Jacobi triple
product identity. Therefore, such an $m_{2,1}(t,x,\lambda_{1},q)$ exists.
Explicitly, we have











































\be
\label{m21explicit}
\begin{tiny}
\begin{aligned}
  &m_{2,1}(t,x,\lambda_{1},q)
  =
  \frac{-1}{2}\frac{\theta'(tx;q)}{\theta(tx;q)}
  +\frac{-1}{2}\frac{\theta'(tx^{-1};q)}{\theta(tx^{-1};q)}\\
  +&\frac{\theta(q^{3/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
\frac{\theta'(t\lambda_{1} q^{1/4})}{\theta(t\lambda_{1} q^{1/4})}
  +\frac{\theta(- q^{3/4}\lambda_{1}^{-1};q)\theta(- q^{-1/4}x;q)\theta(- q^{-3/4}x;q)
  \theta(- q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
\frac{\theta'(-t\lambda_{1} q^{1/4})}{\theta(-t\lambda_{1} q^{1/4})}\\
  +&\frac{\theta(q^{1/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}
\frac{\theta'(t\lambda_{1} q^{3/4})}{\theta(t\lambda_{1} q^{3/4})}
  +\frac{\theta(- q^{1/4}\lambda_{1}^{-1};q)\theta(- q^{-1/4}x;q)\theta(- q^{-3/4}x;q)
  \theta(- q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}
\frac{\theta'(-t\lambda_{1} q^{3/4})}{\theta(-t\lambda_{1} q^{3/4})}\\
  &\qquad\qquad\qquad\quad-\frac{-1}{2}\frac{\theta'(x;q)}{\theta(x;q)}
  -\frac{-1}{2}\frac{\theta'(x^{-1};q)}{\theta(x^{-1};q)}
  -\frac{\theta(q^{3/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
\frac{\theta'(\lambda_{1} q^{1/4})}{\theta(\lambda_{1} q^{1/4})}\\
-&\frac{\theta(- q^{3/4}\lambda_{1}^{-1};q)\theta(- q^{-1/4}x;q)
  \theta(- q^{-3/4}x;q)\theta(- q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
\frac{\theta'(-\lambda_{1} q^{1/4})}{\theta(-\lambda_{1} q^{1/4})}
  -\frac{\theta(q^{1/4}\lambda_{1}^{-1};q)\theta(q^{-1/4}x;q)\theta(q^{-3/4}x;q)
  \theta(q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}
\frac{\theta'(\lambda_{1} q^{3/4})}{\theta(\lambda_{1} q^{3/4})}\\
&\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad
-\frac{\theta(- q^{1/4}\lambda_{1}^{-1};q)\theta(- q^{-1/4}x;q)\theta(- q^{-3/4}x;q)
  \theta(- q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}
\frac{\theta'(-\lambda_{1} q^{3/4})}{\theta(-\lambda_{1} q^{3/4})} \,.
\end{aligned}
\end{tiny}
\ee


Next we calculate the second column of the monodromy matrix using the same
argument as Equation~\eqref{f1=g01} from \cite{Morita:conn-mon}.
\be
\begin{small}
\begin{aligned}
&\hat{f}^{(-1)}(t,x;q)
=
\oint_{0}\Bor_{-1}(g)(\xi,x;q)\theta(t/\xi;q)\frac{d\xi}{2\pi i \xi}
=
\oint_{0}\frac{\theta(t/\xi;q)}{(x\xi;q)_{\infty}
  (x^{-1}\xi;q)_{\infty}}\frac{d\xi}{2\pi i \xi}\\
&=
-\sum_{k=0}^{\infty}\left(\Res_{\xi=x^{\pm}q^{-k}}\right)
\frac{\theta(t/\xi;q)}{(x\xi;q)_{\infty}(x^{-1}\xi;q)_{\infty}}
\frac{d\xi}{2\pi i \xi}\\










&=
-\sum_{k=0}^{\infty}\left(\Res_{\ve=0}\right)
\frac{\theta(txq^{k}e^{\ve};q)}{
  (q^{-1}e^{-\ve};q^{-1})_{k}
  (e^{-\ve};q)_{\infty}(x^{-2}q^{-1}
  e^{-\ve};q^{-1})_{k}(x^{-2}e^{-\ve};q)_{\infty}}
\frac{-d\ve}{2\pi i}\\
&\quad\quad-\sum_{k=0}^{\infty}\left(\Res_{\ve=0}\right)
\frac{\theta(tx^{-1}q^{k}e^{\ve};q)}{
  (x^{2}q^{-1}e^{-\ve};q^{-1})_{k}(x^{2}
  e^{-\ve};q)_{\infty}(q^{-1}e^{-\ve};q^{-1})_{k}(
  e^{-\ve};q)_{\infty}}\frac{-d\ve}{2\pi i}\\





&=
\sum_{k=0}^{\infty}\frac{\theta(txq^{k};q)(qx^{2};q)_{\infty}}{
  (q^{-1};q^{-1})_{k}(x^{-2}q^{-1};q^{-1})_{k}\theta(x^{2};q)}
+\sum_{k=0}^{\infty}\frac{\theta(tx^{-1}q^{k};q)(qx^{-2};q)_{\infty}}{
  (x^{2}q^{-1};q^{-1})_{k}\theta(x^{-2};q)(q^{-1};q^{-1})_{k}}\\
&=
\frac{\theta(tx;q)(qx^{2};q)_{\infty}}{\theta(x^{2};q)}
\sum_{k=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}x^{k}t^{-k}}{(q;q)_{k}(x^{2}q;q)_{k}}
+\frac{\theta(tx^{-1};q)(qx^{-2};q)_{\infty}}{\theta(x^{-2};q)}
\sum_{k=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}x^{-k}t^{-k}}{(q;q)_{k}(qx^{-2};q)_{k}}
\\
&=
-\frac{\theta(q^{-1}t;q)(1-x)(q;q)_{\infty}}{
  \theta(q^{-1}x;q)}g^{(0,x^{-1})}(t,x,q)
-\frac{\theta(q^{-1}t;q)(1-x^{-1})(q;q)_{\infty}}{
  \theta(q^{-1}x^{-1};q)}g^{(0,x)}(t,x,q) \,.
\end{aligned}
\end{small}
\ee
Therefore, we see that
\be\label{fm1ingx}
\begin{aligned}
f^{(-1)}(t,x,q)
&=
-g^{(0,x^{-1})}(t,x,q)
-
g^{(0,x)}(t,x,q).
\end{aligned}
\ee
Now note that the bottom row of $\vM$ is given by $(0,0,1)$ simply from the fact
the inhomogeneous module contains the homogeneous as a sub-module and then the
inhomogeneity normalises the last entry. Therefore, from Lemma~\ref{lem.det41x},
we see that
\be
\begin{pmatrix}
1 & -1 & 0\\
-1 & -1 & 0\\
0 & 0 & 1
\end{pmatrix}^{-1}
\vM(t,x,\lambda,q)
=
\begin{pmatrix}
  \frac{\theta(x^{-2};q)
    \theta(t;q)^2
    (q;q)_{\infty}^3}{2\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)} & 0 & *\\
* & 1 & *\\
0 & 0 & 1
\end{pmatrix}\,.
\ee
Consider the function
\be
\begin{aligned}
  \calE_{4}&:=f^{(1)}(t,x,\lambda_{1},q)-\frac{\theta(x^{-2};q)
  \theta(t;q)^2(q;q)_{\infty}^3}{2\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)}
  \left(g^{(0,x^{-1})}(t,x,q)-g^{(0,x)}(t,x,q)\right)\\
  &\quad-m_{2,1}(t,x,\lambda_{1},q)\left(-g^{(0,x^{-1})}(t,x,q)-g^{(0,x)}(t,x,q)
  \right)\\
  &=
  f^{(1)}(t,x,\lambda_{1},q)-\frac{\theta(x^{-2};q)
  \theta(t;q)^2(q;q)_{\infty}^3}{2\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)}
  \left(g^{(0,x^{-1})}(t,x,q)+g^{(0,x)}(t,x,q)\right)\\
  &\quad-m_{2,1}(t,x,\lambda_{1},q)f^{(-1)}(t,x,q)
\end{aligned}
\ee
where is $m_{2,1}$ has the properties stated in Theorem~\ref{thm.41c}.
Then by the definition of $m_{2,1}$ along with Lemma~\ref{lem.41.gx} and
Lemma~\ref{lem.resf1.x} we see that $\calE_{4}$ is holomorphic and satisfies
Equation~\eqref{41x} and therefore must be zero from Lemma~\ref{lem.41.x.holsol}.
This proves the first column. Now for the last column consider the function 
\be
\begin{aligned}
  \calE_{5}
  &:=
  f^{(0)}(t,\lambda_{2},x,q)
  -
  g^{(0,1)}(t,x,q)\\
  &-
  \frac{\theta(x^{-2};q)
    \theta(t;q)^2(q;q)_{\infty}^{3}}{2\theta(q^{-1}x;q)^2\theta(tx;q)
    \theta(tx^{-1};q)}\left(g^{(0,x^{-1})}(t,x,q)-g^{(0,x)}(t,x,q)\right)\\
  &-
  \left(\frac{\theta'(t\lambda_{2})}{\theta(t\lambda_{2})}
-\frac{\theta'(tx)}{2\theta(tx)}-\frac{\theta'(tx^{-1})}{2\theta(tx^{-1})}
-\frac{\theta'(\lambda_{2})}{\theta(\lambda_{2})}-\frac{1}{2}\right)
  \\ & \times 
  \left(-g^{(0,x^{-1})}(t,x,q)-g^{(0,x)}(t,x,q)\right).
\end{aligned}
\ee
This is holomorphic from Lemma~\ref{lem.41.gx}, Lemma~\ref{lem.resf1.x} and
Lemma~\ref{lem.resf0.x}. Moreover, $\calE_{5}$ satisfies Equation~\eqref{41x}
and therefore vanishes from Lemma~\ref{lem.41.x.holsol}.

The entries of the RHS
of Equation~\eqref{m3x3x} have the following transformation properties under
the $S$ matrix
\be
\begin{small}
\begin{aligned}
  \frac{\theta(x^{-2};\tq)
    \theta(t;\tq)^2(\tq;\tq)_{\infty}^{3}}{2\theta(\tq^{-1}x;\tq)^2
    \theta(tx;\tq)\theta(tx^{-1};\tq)}
  &=\tau\frac{\theta(x^{-2};q)
    \theta(t;q)^2(q;q)_{\infty}^3}{2\theta(q^{-1}x;q)^2\theta(tx;q)
    \theta(tx^{-1};q)}\\
  \left(\frac{\theta'(\ti t\ti \lambda_{2})}{\theta(\ti t\ti \lambda_{2})}
    -\frac{\theta'(\ti t\ti x)}{2\theta(\ti t\ti x)}
    -\frac{\theta'(\ti t\ti x^{-1})}{2\theta(\ti t\ti x^{-1})}
  -\frac{\theta'(\ti \lambda_{2})}{\theta(\ti \lambda_{2})}-\frac{1}{2}\right)
  &=\tau\left(\frac{\theta'(t\lambda_{2})}{\theta(t\lambda_{2})}
  -\frac{\theta'(tx)}{2\theta(tx)}-\frac{\theta'(tx^{-1})}{2\theta(tx^{-1})}
  -\frac{\theta'(\lambda_{2})}{\theta(\lambda_{2})}-\frac{1}{2}\right)\\
\end{aligned}
\end{small}
\ee
while $m_{2,1}$ has three elements in it's $\SL_{2}(\BZ)$ orbit
$m_{2,1},m_{2,1}|_{1}S,m_{2,1}|_{1}T$. To see this notice that $m_{2,1}|_{1}T^2$
simply permutes the terms in RHS of Equation~\eqref{m21explicit}. Then using
Equations~\eqref{thetaS}~\eqref{S.mod.thd} we can explicitly compute
$m_{2,1}|_{1}S$ and $m_{2,1}|_{1}TS$ which can be used to show that
$m_{2,1}|_{1}ST=m_{2,1}|_{1}S$ and $m_{2,1}|_{1}TS=m_{2,1}|_{1}T$.
Altogether, this shows the monodromy satisfies Equation~\eqref{M41x}.

\begin{lemma}
  \label{lem.41.x.holsol}
  If $h(t,x,q)$ is holomorphic for $t\in\BC^{\times}$ and satisfies
  Equation~\eqref{41x} then it vanishes.
\end{lemma}

\begin{proof}
  If $h(t,x,q)$ is holomorphic for $t\in\BC^{\times}$ then is has an Laurent
  series expansion
\be
h(t,x,q)=\sum_{k\in\BZ}\a_{k}(x,q)t^{k}.
\ee
Therefore Equation~\eqref{41x} determines the coefficients $\a_{k}(x,q)$ from
two initial conditions say $\a_{0}$ and $\a_{-1}$. However for any non-zero choice
of $(\a_{0},\a_{-1})$ we find that $\a_{k}\sim O(q^{-k^{2}/2})$ for $k\sim-\infty$
and therefore it is divergent unless $\a_{0}=\a_{-1}=0$. Notice the difference here
with that of Corollary~\ref{cor:41holsol} comes from the fact that $\a_{-1}=0$ does
not imply that $\a_{k}=0$ for $k<0$.
\end{proof}
  
\begin{lemma}
  \label{lem.41.gx}
We have
\be
\begin{aligned}
  \Res_{t=q^{m}x}\frac{\theta(t;q)^{2}}{\theta(tx;q)
\theta(tx^{-1};q)}g^{(0,x^{-1})}(t,x,q)\frac{dt}{2\pi i t}
  &=
  \frac{-\theta(x;q)^2f^{(-1)}(q^{m}x,x,q)}{\theta(x^{2};q)(q;q)_{\infty}^{3}}\\
  \Res_{t=q^{m}x^{-1}}\frac{\theta(t;q)^{2}}{\theta(tx;q)
\theta(tx^{-1};q)}g^{(0,x)}(t,x,q)\frac{dt}{2\pi i t} 
  &=
  \frac{-\theta(x^{-1};q)^2f^{(-1)}(q^{m}x^{-1},x,q)}{
    \theta(x^{-2};q)(q;q)_{\infty}^{3}}\\
\end{aligned}
\ee
while $g^{(0,1)}(t,x,q)$ is holomorphic for $t\in\BC^{\times}\cup\{\infty\}$.
\end{lemma}

\begin{proof}
This follows from Equation~\eqref{fm1ingx} and the fact that
\be
\Res_{t=q^{m}x^{\pm}}\frac{\theta(t;q)^{2}}{\theta(tx;q)
\theta(tx^{-1};q)}\frac{dt}{2\pi i t}
=
\frac{\theta(x^{\pm};q)^2}{\theta(x^{\pm2};q)(q;q)_{\infty}^3}\,.
\ee
\end{proof}

\begin{lemma}
  \label{lem.resf1.x}
  \rm{(a)} The function $\Bor_{1/2}\hat{f}^{(1)}(\xi,x,q)$ has simple poles at
$\xi=\pm q^{-1/4-\BZ_{\geq0}/2}$ with residue
\be
\begin{aligned}
\Res_{\xi=\pm q^{-1/4-n/2}}\Bor_{1/2}\hat{f}^{(1)}(\xi,x,q)\frac{d\xi}{2\pi i\xi}
&=
\frac{-\theta(\pm q^{-1/4}x;q^{1/2})}{2(q;q)_{\infty}^{2}}
\sum_{\ell=0}^{n}(\pm1)^{n}
\frac{q^{\frac{n(n+2)}{4}}x^{2\ell-n}}{(q;q)_{\ell}(q;q)_{n-\ell}}.
\end{aligned}
\ee
  \rm{(b)}
  The function $f^{(1)}(t,x,\lambda_{1},q)$ has simple poles at
  $t=\pm q^{-1/4+\BZ}\lambda_{1}^{-1}$
  with residue
  \be
\begin{aligned}
  &\Res_{t=\pm q^{-1/4-n}\lambda_{1}^{-1}}f^{(1)}(t,x,\lambda_{1},q)
  \frac{dt}{2\pi it}\\
&=
\frac{\theta(\pm q^{3/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)
  \theta(\pm q^{-3/4}\lambda_{1};q)}{2\theta(x;q)
  \theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
f^{(-1)}(\pm q^{-1/4-n} \lambda_{1}^{-1},x,q) \,.
\end{aligned}
\ee
\end{lemma}
\begin{proof}
Firstly note that the singularities are determined by the functional equation
for $\Bor_{1/2}\hat{f}^{(1)}(\xi,x,q)$. For part (a), recall the auxiliary
function $H_{r}(\xi,q)$ defined in Equation~\eqref{aux.fun.H}. Note that
from the power series at $\xi=0$, we see that
\be
\Bor_{1/2}\hat{f}^{(1)}(q^{-1/4}\xi,x,q)
=
\sum_{r\in\BZ}(-1)^{r}q^{r^{2}/4}x^{r}\xi^{r}H_{r}(\xi,q).
\ee
Let
\be
R_{\pm}(n,x,q)=\Res_{\xi=\pm q^{-1/4-n/2}}
\Bor_{1/2}\hat{f}^{(1)}(\xi,x,q)\frac{d\xi}{2\pi i\xi}.
\ee
Then, from Equation~\eqref{res.aux.fun.H},
\be
\begin{aligned}
R_{\pm}(0,x,q)
&=
\Res_{\xi=\pm 1}\sum_{r\in\BZ}(-1)^{r}q^{r^{2}/4}\xi^{r}x^{r}H_{r}(\xi,q)
\frac{d\xi}{2\pi i\xi}
&=
\frac{-\theta(\pm q^{-1/4}x;q^{1/2})}{2(q;q)_{\infty}^{2}}.
\end{aligned}
\ee
Now from the functional equation of $\Bor_{1/2}\hat{f}^{(1)}(\xi,x,q)$, we can
deduce that
\be
\begin{aligned}
&\Res_{\xi=\pm q^{-1/4-n/2}}(1-q^{1/2}\xi^2)\Bor_{1/2}\hat{f}^{(1)}(\xi,q)+
(x+x^{-1})\xi\Bor_{1/2}\hat{f}^{(1)}(q^{1/2}\xi,q)-\Bor_{1/2}\hat{f}^{(1)}(q\xi,q)
\frac{d\xi}{2\pi i\xi}\\
&=
(1-q^{-n})R_{\pm}(n,x,q)\pm(x+x^{-1})q^{-1/4-(n-1)/2}R_{\pm}(n-1,x,q)
-R_{\pm}(n-2,x,q)=0.
\end{aligned}
\ee
Note that $R_{\pm}(n,x,q)=0$ for $n<0$ and that when $R_{\pm}(-1,x,q)$ is zero we
have a unique solution determined by $R_{\pm}(0,x,q)$. One can then check that
\be
R_{\pm}(n,x,q)
=
\frac{-\theta(\pm q^{-1/4}x;q^{1/2})}{2(q;q)_{\infty}^{2}}
\sum_{\ell=0}^{n}(\pm1)^{n}\frac{q^{\frac{n(n+2)}{4}}
  x^{2\ell-n}}{(q;q)_{\ell}(q;q)_{n-\ell}} \,.
\ee
For part (b), we compute
{\small
\be
\begin{aligned}
  &\Res_{t=\pm q^{-1/4-n}\lambda_{1}^{-1}}f^{(1)}(t,x,\lambda_{1},q)
  \frac{dt}{2\pi it}\\
&=
\Res_{t=\pm q^{-1/4-n}\lambda_{1}^{-1}}
\frac{\theta(t;q)(q;q)_{\infty}}{(1-x)\theta(x;q)}
\Lap_{1/2}\Bor_{1/2}\hat{f}^{(1)}(t,x,\lambda_{1},q)\frac{dt}{2\pi it}\\
&=
\frac{\theta(\pm q^{-1/4-n}\lambda_{1}^{-1};q)(q;q)_{\infty}}{(1-x)\theta(x;q)
  \theta(\lambda_{1};q^{1/2})}
\sum_{k\in\BZ}(-1)^{k}q^{(k-2n)(k-2n-1)/4}\lambda_{1}^{-k+2n}R_{\pm}(k,x,q)\\
&=
\frac{\theta(\pm q^{-1/4-n}\lambda_{1}^{-1};q)(q;q)_{\infty}}{(1-x)\theta(x;q)
  \theta(\lambda_{1};q^{1/2})}
\frac{-\theta(\pm q^{-1/4}x;q^{1/2})}{2(q;q)_{\infty}^{2}q^{-n(2n+1)/2}\lambda_{1}^{-2n}}
\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}(-1)^{k}\frac{
  q^{\frac{k(k+1)}{2}}x^{2\ell-k}}{(q;q)_{\ell}(q;q)_{k-\ell}}
(\pm q^{-1/4-n}\lambda_{1}^{-1})^{k}\\
&=
-\frac{\theta(\pm q^{-1/4-n}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q^{1/2})}{
  2(q;q)_{\infty}(1-x)\theta(x;q)\theta(\lambda_{1};q^{1/2})}q^{n(2n+1)/2}
\lambda_{1}^{2n}
  \frac{(1-x)}{\theta(q^{-1}x;q)}
\hat{f}^{(-1)}(\pm q^{-1/4-n/2}\lambda_{1}^{-1},x,q)\\
&=
\frac{\theta(\pm q^{-1/4-n}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)\theta(\pm q^{-5/4-n}
  \lambda_{1}^{-1};q)}{2x\theta(x;q)^2
  \theta(\lambda_{1};q)\theta(q^{-1/2}\lambda_{1};q)q^{-n(2n+1)/2}\lambda_{1}^{-2n}}
f^{(-1)}(\pm q^{-1/4-n}\lambda_{1}^{-1},x,q)\\
&=
\frac{\theta(\pm q^{-1/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)\theta(\pm q^{-5/4}
  \lambda_{1}^{-1};q)}{2x\theta(x;q)^2
  \theta(\lambda_{1};q)\theta(q^{-1/2}\lambda_{1};q)}
f^{(-1)}(\pm q^{-1/4-n}\lambda_{1}^{-1},x,q)\\
&=
\frac{\theta(\pm q^{3/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)
  \theta(\pm q^{-3/4}\lambda_{1};q)}{2\theta(x;q)
  \theta(x^{-1};q)\theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}
f^{(-1)}(\pm q^{-1/4-n} \lambda_{1}^{-1},x,q) \,.
\end{aligned}
\ee
}
\end{proof}
\begin{lemma}
\label{lem.resf0.x}
\rm{(a)}
The function $\Bor_{1}\hat{f}^{(0)}(\xi,x,q)$ has simple poles at $\xi \in q^\BZ$
with residue
\be
\label{resBf0.x}
R(m,x,q)
:=
\Res_{\xi=q^{-m}}\Bor_{1}\hat{f}^{(0)}(\xi,x,q)\frac{d\xi}{2\pi i\xi}
= -(qx;q)_{\infty}(qx^{-1};q)_{\infty}\sum_{\ell=0}^{m}
\frac{q^{m}x^{2\ell-m}}{(q;q)_{\ell}(q;q)_{m-\ell}} \,.
\ee
\rm{(b)}
The function $f^{(0)}(t,x,\lambda_{2},q)$ has simple poles at
$t\in \lambda_{2}^{-1}q^{\BZ}$ with residue
\be
\label{resf0.x}
\Res_{t=q^{-m}\lambda_{2}^{-1}}f^{(0)}(t,x,\lambda_{2},q)\frac{dt}{2\pi it} =
f^{(-1)}(q^{-m}\lambda_{2}^{-1},x,q) \,.
\ee
\end{lemma}
\begin{proof}
For part (a), notice that
{\small
\be
\begin{aligned}
\Bor_{1}\hat{f}^{(0)}(\xi,x,q)
&=
\sum_{k=0}^{\infty}(qx;q)_{k}(qx^{-1};q)_{k}\xi^{k}  
=
(qx;q)_{\infty}(qx^{-1};q)_{\infty}\sum_{k=0}^{\infty}
\frac{1}{(q^{k+1}x;q)_{\infty}(q^{k+1}x^{-1};q)_{\infty}}\xi^{k}\\
&=
(qx;q)_{\infty}(qx^{-1};q)_{\infty}\sum_{k=0}^{\infty}
\sum_{n,\ell=0}^{\infty}\frac{q^{kn+k\ell+n+\ell}
  x^{\ell-n}}{(q;q)_{n}(q;q)_{\ell}}\xi^{k}\\
&=
(qx;q)_{\infty}(qx^{-1};q)_{\infty}\sum_{n,\ell=0}^{\infty}
\frac{q^{n+\ell}x^{\ell-n}}{(q;q)_{n}(q;q)_{\ell}(1-q^{n+\ell}\xi)}\\
&=
(qx;q)_{\infty}(qx^{-1};q)_{\infty}\sum_{n=0}^{\infty}\sum_{\ell=0}^{n}
\frac{q^{n}x^{2\ell-n}}{(q;q)_{\ell}(q;q)_{n-\ell}(1-q^{n}\xi)}.
\end{aligned}
\ee
}
The residue then follows.
For part (b), the pole structure is clear noting that Equation~\eqref{f0x}
is convergent if all the terms are and that
$\Bor_{1}\hat{f}^{(0)}(q^{k}t\lambda_{2},x,q)$ has poles at
$t\in\lambda_{2}^{-1}q^{\BZ_{\leq -k}}$. We compute the residues
$\rho_m:=\Res_{t=q^{-m}\lambda_{2}^{-1}}f^{(0)}(t,x,\lambda_{2},q)\frac{dt}{2\pi it}$
as follows:
\be
\begin{aligned}

  \rho_m
  &=
\Res_{t=q^{-m}\lambda_{2}^{-1}}(\Lap_{1}\Bor_{1}\hat{f}^{(0)})(t,x,\lambda_{2},q)
\frac{dt}{2\pi it}\\
&=
\Res_{t=q^{-m}\lambda_{2}^{-1}}\frac{1}{\theta(\lambda_{2},q)}
\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)/2}\lambda_{2}^{k}\Bor_{1}\hat{f}^{(0)}(q^{k}
\lambda_{2}t,x,q)\frac{dt}{2\pi it}\\
&=
\frac{1}{\theta(\lambda_{2},q)}\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)/2}
\lambda_{2}^{k}R(m-k,x,q)\\



&=
\frac{1}{\theta(\lambda_{2},q)}(-1)^{m}q^{m(m+1)/2}\lambda_{2}^{m}
\sum_{k=0}^{\infty}(-1)^{k}q^{k(k-1)/2}(q^{-m}\lambda_{2}^{-1})^{k}R(k,x,q)\\





&=
\frac{-(qx;q)_{\infty}(qx^{-1};q)_{\infty}}{
  \theta(\lambda_{2},q)}(-1)^{m}q^{m(m+1)/2}
\lambda_{2}^{m}\sum_{k,\ell=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}x^{2\ell-k}}{
  (q;q)_{\ell}(q;q)_{k-\ell}}(q^{-m}\lambda_{2}^{-1})^{k}\\


&=
f^{(-1)}(q^{-m}\lambda_{2}^{-1},x,q) \,.
\end{aligned}
\ee
\end{proof}

The functional equation \eqref{41x} for $U,V$ defined in~\eqref{UVex41x}
can be written in the form
\be
U(qt,x,\lambda_{1},\lambda_{2},q)
=
A(t,x,q)U(t,x,\lambda_{1},\lambda_{2},q)
\quad\text{and}\quad
V(qt,x,q)
=
A(t,x,q)V(t,x,q)
\ee
where
\be
A(t,x,q)
=
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-3} & q^{-3}t^{-1}-(1+x+x^{-1})q^{-2} & (1+x+x^{-1})q^{-1}-q^{-3}t^{-1}
\end{pmatrix}.
\ee
Therefore, we see that
\begin{equation*}
\det(U(qt,x,\lambda_{1},\lambda_{2},q))=\det(U(t,x,\lambda_{1},\lambda_{2},q))q^{-3},
\qquad \det(V(qt,x,q))=\det(V(t,x,q))q^{-3} \,.
\end{equation*}

\begin{lemma}
  \label{lem.det41x} 
  We have:
\be
\begin{aligned}
\det(U(t,x,\lambda_{1},\lambda_{2},q))
&=
-\frac{q^{-3}x}{(1-x)^2}t^{-3}\\
\det(V(t,x,q))
&=
\frac{\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)}{\theta(x^{-2};q)
  \theta(t;q)^2(q;q)_{\infty}^3}\frac{q^{-3}x}{(1-x)^2}t^{-3}\,.
\end{aligned}
\ee
\end{lemma}

\begin{proof}
Firstly notice that
\be
\begin{tiny}
\begin{aligned}
&U(t,x,\lambda_{1},\lambda_{2},q)\\
&=
W(f^{(1)}(t,x,\lambda_{1},q),f^{(-1)}(t,x,q),f^{(0)}(t,x,\lambda_{2},q))\\
&=
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-2}t^{-1} & -q^{-2} & q^{-2}t^{-1}-(x+x^{-1})q^{-1}
\end{pmatrix}
\begin{pmatrix}
0 & 0 & 1\\
f^{(1)}(t,x,\lambda_{1},q) & f^{(-1)}(t,x,q) & f^{(0)}(t,x,\lambda_{2},q)\\
f^{(1)}(qt,x,\lambda_{1},q) & f^{(-1)}(qt,x,\lambda_{1},q) &
f^{(0)}(qt,x,\lambda_{2},q)
\end{pmatrix}
\end{aligned}
\end{tiny}
\ee

\noindent
with a similar expression for $V$. Therefore,
\be
\label{det.3x3.in.2x2}
\begin{aligned}
  \det(U(t,x,\lambda_{1},\lambda_{2},q))
  &=
  q^{-2}t^{-1}(f^{(1)}(t,x,\lambda_{1},q)f^{(-1)}(qt,x,q)-f^{(1)}(qt,x,
\lambda_{1},q)f^{(-1)}(t,x,q))\\
  \det(V(t,x,q))
  &=
  q^{-2}t^{-1}(g^{(0,x^{-1})}(t,x,q)g^{(0,x)}(qt,x,q)
-g^{(0,x^{-1})}(qt,x,q)g^{(0,x)}(t,x,q))\,.
\end{aligned}
\ee
Now notice that both $\det(U(t,x,\lambda_{1},\lambda_{2},q))t^3$ and
$\det(V(t,x,q))t^3$ are elliptic functions in $t$. Furthermore,
$\det(U(t,x,\lambda_{1},q))$ has potentially simple poles in $t$ at
$t\in\pm q^{-1/4-\BZ/2}\lambda^{-1}$ and $t\in q^{\BZ}$. However, note that
the poles of $f^{(-1)}$ at $t\in q^{\BZ}$ cancel with zeros of $f^{(1)}$.
Lemma~\ref{lem.resf1.x} implies that
  \be
\begin{aligned}
& \Res_{t=\pm q^{-1/4-n}\lambda^{-1}}\det(U(t,x,\lambda_{1},\lambda_{2},q)q^{2}t)=\\
&\frac{\theta(\pm q^{3/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)\theta(\pm q^{-3/4}\lambda_{1};q)
  
  
}{2(q;q)_{\infty}^{2}\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}\\
   & \times f^{(-1)}(\pm q^{-1/4-n}
  \lambda_{1}^{-1},x,q)f^{(-1)}(\pm q^{3/4-n}
  \lambda_{1}^{-1},x,q) \\
&\quad-\frac{\theta(\pm q^{3/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)
  \theta(\pm q^{-3/4}\lambda_{1};q)}{2(q;q)_{\infty}^{2}\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)}\\
& \times f^{(-1)}(\pm q^{3/4-n}
  \lambda_{1}^{-1},x,q)f^{(-1)}(\pm q^{-1/4-n}
  \lambda_{1}^{-1},x,q) = 0 \,.
\end{aligned}
\ee
A similar calculation shows that
\be
\Res_{t=\pm q^{-3/4-n}\lambda_{1}^{-1}}\det(U(t,x,\lambda_{1},\lambda_{2},q))=0 \,.
\ee
Therefore, we see that $U(t,x,\lambda_{1},q)t^2$ is elliptic and holomorphic in
$t\in\BC^{\times}$. Therefore, it is constant in $t$. Now considering the limit as
$t\rightarrow0$, using the definition of $f^{(\pm1)}$ and their asymptotic expansions
(given by their formal power series expansions, by a version of Watson's lemma),
it follows that
\be
\begin{aligned}
\det(U(t,x,\lambda_{1},\lambda_{2},q))q^2t^3
&=
\lim_{t\rightarrow 0}\det(U(t,x,\lambda_{1},\lambda_{2},q))q^2t^3\\
&=
\lim_{t\rightarrow 0}\frac{\theta(t;q)\theta(q^{-1}x;q)}{\theta(t;q)
  \theta(x;q)(1-x)^2}t^2
-\lim_{t\rightarrow 0}\frac{\theta(qt;q)\theta(q^{-1}x;q)}{\theta(q^{-1}t;q)
  \theta(x;q)(1-x)^2}t^2\\
&=
-\lim_{t\rightarrow 0}q^{-1}\frac{\theta(t;q)\theta(x;q)}{\theta(t;q)
  \theta(x;q)(1-x)^2}
=
-\frac{q^{-1}x}{(1-x)^2} \,.
\end{aligned}
\ee
Now noting that $\theta(t;q)^2/\theta(tx;q)\theta(tx^{-1};q)$
is elliptic we see that 
\be
\det(V(t,x,q))t^{3}\frac{\theta(t;q)^2}{\theta(tx;q)\theta(tx^{-1};q)}
\ee
is elliptic and holomorphic in $t$ and therefore constant in $t$. Then we see that
\be
\begin{aligned}
  &\lim_{t\rightarrow\infty}\det(V(t,x,q))q^{2}t^{3}
  \frac{\theta(t;q)^2}{\theta(tx;q)\theta(tx^{-1};q)}\\
&=
\lim_{t\rightarrow\infty}(g^{(0,x^{-1})}(t,x,q)g^{(0,x)}(qt,x,q)
-g^{(0,x^{-1})}(qt,x,q)g^{(0,x)}(t,x,q))t^{2}\frac{\theta(t;q)^2}{\theta(tx;q)
  \theta(tx^{-1};q)}\\
&=
q^{-1}\frac{(qx^2;q)_{\infty}(qx^{-2};q)_{\infty}(1-x^2)
\theta(q^{-1}x;q)
\theta(q^{-1}x^{-1};q)}{
  (1-x)^2\theta(x^{2};q)\theta(x^{-2};q)(q;q)_{\infty}^2}\\
&=
-q^{-1}x^{2}\frac{\theta(x^2;q)\theta(q^{-1}x;q)
\theta(q^{-1}x^{-1};q)}{\theta(x^{2};q)\theta(x^{-2};q)(1-x)^2(q;q)_{\infty}^3}\,.
\end{aligned}
\ee
\end{proof}
To finish the proof of
Theorem~\ref{thm.41c} we will use the state integrals introduced in
~\cite[Equ.(139)]{GGMW:trivial} for $w$ in a neighbourhood of zero.








\be\label{41x.sint}
\int_{\BR+i\ve}
\Phi_{\sfb}(x+i\sfb^{-1}u)\Phi_{\sfb}(x-i\sfb^{-1}u)
\frac{\exp\left(-\pi i x^{2}-2\pi\frac{zx}{\sfb}\right)}{1
  +\tq^{1/2}\exp\left(-\frac{2\pi x}{\sfb}\right)}dx\,.
\ee
The factorisation of this integral was done in \cite[Equ.(149)]{GGMW:trivial}.
This module is again not self dual (see Proposition~\ref{41inhom.not.sd}) and
means that additional functions arise in the factorisation. It was shown, using
Equation~\eqref{thetaS}, that Equation~\eqref{41x.sint} factors as combinations
of elementary functions holomorphic in $\BC'$ times
\be
\calI(z,w,\tau)
=
g^{(0,1)}(\tilde{t},\ti x,\tq)+\tau g^{(0,x)}(\tilde{t},\ti x,\tq)
L^{(x^{-1})}(t,x,q)-\tau g^{(0,x^{-1})}(\tilde{t},\ti x,\tq)L^{(x)}(t,x,q)
\ee
where
\be
  L^{(x^{\mp})}(t,x,q)
  =
  \frac{
    \theta(t;q)(1-x^{\mp})(q;q)_{\infty}^2}{\theta(q^{-1}x^{\pm};q)
    \theta(tx^{\mp};q)}(qx^{\pm2};q)_{\infty}\sum_{k=0}^{\infty}(-1)^{k}
  \frac{q^{k(k+1)/2}x^{\pm k}}{(q;q)_{k}(qx^{\pm2};q)_{k}(1-q^{k}x^{\pm})}t^{-k}.
\ee
These functions $L^{(x^\mp)}$ can then be shown to satisfy
\be
\begin{aligned}
  L^{(x^{\mp})}(t,x,q)-L^{(x^{\mp})}(qt,x,q)&=\frac{\theta(x^{-2};q)
    \theta(t;q)^2(q;q)_{\infty}^3}{\theta(q^{-1}x;q)^2\theta(tx;q)
    \theta(tx^{-1};q)}\frac{(1-x)^2}{x}qtg^{(0,x^{\pm})}(qt,x,q).
\end{aligned}
\ee
Again this determines $L^{(x^{\mp})}$ up to the addition of an elliptic function
so checking the principal parts
\be
{\small
V(t,x,q)^{-1}
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-2}t^{-1} & -q^{-2} & q^{-2}t^{-1}-(x+x^{-1})q^{-1}
\end{pmatrix}
=
\begin{pmatrix}
  -L^{(x)}(t,x,q) & * & *\\
  L^{(x^{-1})}(t,x,q)& * & *\\
  1 & 0 & 0
\end{pmatrix}.
}
\ee
where the $*$ are given by $\pm\det(V(t,x,q))^{-1}g^{(0,x^{\pm})}(q^{m}t,x,q)$
where $m=0,1$. Finally, one can use the functional equations to take $w$ away
from $0$ which gives the analytic continuation or can alter the contour
depending on $w$. Noting that the entries of $\Omega_{V,S}$ are combinations of
elementary functions times $\calI(z+n+m\tau,w,\tau)$, we see that $\Omega_{V,S}$
extends for $\tau\in\BC'$ and using the modularity of the monodromy and part (c)
of Theorem~\ref{thm.ST} completes the proof.
\end{proof}
