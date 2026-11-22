---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-005-15-modular-q-holonomic-modules-in-chernsimons-th
section_title: "Modular q-holonomic modules in Chern–Simons theory"
section_number: 1.5
pages: 7-12
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.983
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
In this section we present three $q$-holonomic modules whose cocycles play a key
role in complex Chern--Simons theory and prove their modularity. We will not need
a detailed knowledge of Chern--Simons theory, but focus on the fact that it is a
gauge theory with gauge group a complex Lie group, whose partition function
can be identified by a finite dimensional integrals of products of the Faddeev
quantum dilogarithm. A detailed exposition of Chern--Simons theory is given in the
work of Andersen--Kashaev and Beem, Dimofte and Pasquetti~\cite{AK,Dimofte:complex,
  Beem,Pasquetti}. The quasi-periodicity of the Faddeev quantum dilogarithm implies
that the partition function of complex Chern--Simons theory satisfies a
$q$-holonomic module of linear $q$-difference equations.

In the modular $q$-holonomic modules discussed below, we prove their modularity
\emph{and} at the same time define and compute fundamental matrices $U$ and $V$
of solutions algorithmically, and give explicit formula for their monodromy.
This is possible because of two key features, namely:
\begin{itemize}
\item[(a)]
  The fundamental matrices $U$ and $V$ are meromorphic functions with explicit
  poles and with residues expressed linearly in terms of $U$ and $V$.
  This is some kind of resurgence property and it is ultimately responsible for
  determining the monodromy.
\item[(b)]
  The monodromy is uniquely determined by its elliptic property, the explicit
  poles and principle parts, and its limiting values at $t=0$ or $t=\infty$. 
\end{itemize}

Our first module, the linear $q$-difference equation for the infinite
Pochhammer symbol
\be
\label{ex1}

(1-qt)f(qt,q)-f(t,q)=0 \,,
\ee
has trivial monodromy but its cocycle is a very interesting function, the Faddeev
quantum dilogarithm function which is the building block of the partition function
of complex Chern--Simons theory. With the definition of $f^{(0)}$ and $g^{(1)}$ given
in Equations~\eqref{ex1.f0} and~\eqref{ex1.g1} below, we define the fundamental
matrices $U(t,q)$ and $V(t,q)$ of solutions at $t=0$ and $t=\infty$ by 
\be
\label{UVex1}
U(t,q) = W(f^{(0)}(t,q)), \qquad
V(t,q) = W(g^{(1)}(t,q)) \,,
\ee
with equal weights $\kappa = 0$. In our theorems below,
we will use the terms ``a $q$-holonomic module is modular'' and ``its cocycle
in modular'' interchangeably. 

\begin{theorem}
\label{thm.ex1}
The monodromy matrix is $\vM(t,q)=(1)$. The two cocycles~\eqref{Om} $\Om_U$
and $\Om_V$ are equal, modular and when $\gamma=S$, they are given explicitly by
\be
\Om_{S}(z,\tau) = 
\Phi_{\sfb}\left(\frac{iz}{\sfb}
  +\frac{i\sfb}{2}+\frac{1}{2i\sfb}\right)^{-1}
\ee
where $\Phi$ is the Faddeev quantum dilogarithm function~\cite{Faddeev, FK-QDL}.
\end{theorem}
  
In forthcoming work~\cite{GKZ:cocycle}, the cocycle $\Om_\gamma$ will be
identified with an $\SL_2(\BZ)$-extension of the Faddeev quantum dilogarithm,
and its modularity will be deduced independently, using properties of the
odd Eisenstein series. 

Our second module is the $q$-difference equation of the Appell-Lerch sums
\be
\label{ex2}

f(q^2t,q)+(qt-1)f(qt,q)-tf(t,q)=0 \,.
\ee
The cocycle of~\eqref{ex2} is the Appell-Lerch sum, which is the building block
for the extension of the partition function of complex Chern--Simons theory
that detects the trivial flat connection, see~\cite{GGMW:trivial}.
In the above equation, some formal power series solutions are divergent, and their 
$q$-Laplace resummation is expressed in terms of an Appell-Lerch sum that depends
on an additional elliptic variable. The monodromy of this equation is an explicit
product of theta functions that depends on two elliptic variables, but the cocycle
is independent of them, and is expressed explicitly in terms of the Mordell
integral. Our results give a new interpretation of the Mordell integral and
Appell-Lerch sums emphasising the role of the linear $q$-difference equations
as opposed to the aspects of modular forms advocated by Zwegers in his
thesis~\cite{Zwegersthesis} and by Dabholkar--Murthy--Zagier~\cite{DMZ:blackholes}
in the study of mock modular forms and their incarnations in the mathematical
physics of black holes.

With the definition of $f^{(-1)}$, $f^{(0)}$, $g^{(0)}$ and $g^{(1)}$ given in
Equations~\eqref{ex2.f-1}, \eqref{ex2.f0}, \eqref{ex2.g0} and~\eqref{ex2.g1}
below, we define the fundamental matrices $U(t,\lambda,q)$ and $V(t,\mu,q)$
of solutions at $t=0$ and $t=\infty$ by 
\be
\label{UVex2}
U(t,\lambda,q) = W(f^{(0)}(t,\lambda,q), f^{(-1)}(t,q)), \qquad
V(t,\mu,q) = W(g^{(0)}(t,\mu,q), g^{(-1)}(t,q)) \,,
\ee







with equal weights $\kappa=(0,1)$.

\begin{theorem}
\label{thm.ex2}
{\rm (a)}
The monodromy matrix $\vM(t,\lambda,\mu,q)=V(t,\mu,q)^{-1}U(t,\lambda,q)$ is
given by
\be
\label{Mex2b}
\vM(t,\lambda,\mu,q) =
\begin{pmatrix}
1 & 0\\
* & 1\\
\end{pmatrix}
\ee
where 
\be
\label{M12ex2}
\vM_{2,1}(t,\lambda,\mu,q) =
-\frac{(q;q)_{\infty}^{3}\theta(q^{-1}t;q)\theta(\lambda ^{-1}\mu ;q)
  \theta(\lambda ^{-1}\mu ^{-1}t^{-1};q)}{\theta(\lambda ^{-1};q)\theta(\mu ;q)
  \theta(\lambda ^{-1}t^{-1};q)\theta(\mu ^{-1}t^{-1};q)} \,.
\ee
The matrix $\vM$ satisfies the modular transformation~\eqref{Mmod}.
\newline
{\rm (b)}
The two cocycles~\eqref{Om} $\Om_U$ and $\Om_V$ are equal, modular, 
independent of $\lambda$ and $\mu$ and when $\gamma=S$, are given explicitly
by
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
\end{pmatrix}^{-1}
\ee
where
\be
\label{mordell}
h(z,\tau)=\int_{\BR}\frac{e^{\pi i (\tau x^{2} + 2 i z x)}}{2\cosh(\pi x)}dx.
\ee
is the Mordell integral. 
\end{theorem}




















































  














































Our third module is a linear $q$-difference equation associated to quantum
invariants of the simplest hyperbolic  knot $4_1$,
\be
\label{41x1}
tqf(qt;q) +(1-2t)f(t;q)+ tq^{-1}f(q^{-1}t;q) = 0 \,.
\ee
This equation, which is also related to the $q$-Hahn Bessel function, appeared
in homogeneous form in~\cite[Eqn.(11)]{GGM}. 
With the definition of $f^{(-1)}$, $f^{(1)}$ and $g^{(0,0)}$ and $g^{(0,1)}$ given in
Equations~\eqref{ex41.f-1}, \eqref{ex41.f1} and \eqref{ex41.g00}
below, we define the fundamental matrices $U(t,\lambda,q)$ and $V(t,q)$
of solutions at $t=0$ and $t=\infty$ by 
\be
\label{UVex41}
U(t,\lambda,q) = W(f^{(1)}(t,\lambda,q), f^{(-1)}(t,q)), \qquad
V(t,q) = W(g^{(0,0)}(t,q), g^{(0,1)}(t,q)) \,,
\ee







and equal weights $\kappa=(1,0)$.
\begin{theorem}
  \label{thm.41}
{\rm (a)}
The monodromy matrix $\vM(t,\lambda,q)=V^{-1}(t,q)U(t,\lambda,q)$ is given by
\be
\label{M41b}
\vM(t,\lambda,q) =
\begin{pmatrix}
- 1 & 0\\
\vM_{2,1}(t,\lambda,q) & 1\\
\end{pmatrix}
\ee
where 
\be
\label{M412}
\vM_{2,1}(t,\lambda,q) =
\frac{\theta(qt;q)\theta(t\lambda;q)\theta(t\lambda q^{-1/2};q)
\theta(t\lambda^{2}q^{-1/2};q)}{\theta(t\lambda q^{1/4};q)
\theta(-t\lambda q^{1/4};q)\theta(t\lambda q^{-1/4};q)
\theta(-t\lambda q^{-1/4};q)\theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)} \,.
\ee
The matrix $M$ satisfies the modular transformations
\be
\label{M41c}
\Delta_{T^{2},\kappa}\vM|_{\kappa}T^2=\vM,\quad
\Delta_{STS,\kappa}\vM|_{\kappa}STS=\vM,\quad
\Delta_{TST,\kappa}\vM|_{\kappa}TST=\vM\,.
\ee
It follows that the $\SL_2(\BZ)$-orbit of $M$ consists
of three functions $M,\Delta_{T,\kappa}\vM|_{\kappa}T,\Delta_{S,\kappa}\vM|_{\kappa}S$.
\newline
{\rm (b)}
The two cocycles~\eqref{Om} $\Om_{\Av(U)}$ and $\Om_{V}$, defined by the averaging 
\be
\Av(U)=V\Av(\vM), \qquad \Av(\vM)=
\frac{1}{3}\left(\vM+\Delta_{T,\kappa}\vM|_{\kappa}T
  +\Delta_{S,\kappa}\vM|_{\kappa}S\right) \,,
\ee
are equal, modular, independent of $\lambda$ and when $\gamma=S$, they
are given by elementary functions times the state integrals







\be
\int_{\BR+i\ve}
\Phi_{\sfb}(x)^2
\exp\left(-\pi i x^{2}-2\pi\sfb^{-1}zx\right)dx.
\ee
\end{theorem}

The above can be phrased by saying that $M$ is modular on an index three subgroup
$\Gamma'$ of $\SL_2(\BZ)$ (conjugate to the $\theta$ subgroup and to the congruence
subgroup $\Gamma_0(2)$ of $\SL_2(\BZ)$) 



and if $\gamma \in \Gamma'$ then $\Om_{U,\gamma}=\Om_{V,\gamma}$ is independent of
$\lambda$ and modular. The corresponding state integrals are defined in forthcoming
work~\cite{GKZ:cocycle}. However, the modularity of the module follows from
Theorem~\ref{thm.ST}. 

The equation~\eqref{41x1} has two important extensions, each containing important
information about the knot. The first extension is an inhomogeneous version, which
for the $4_1$ knot, takes the form (see~\cite[Eqn.(98)]{GZ:kashaev}
and~\cite[Sec.2.2]{GGMW:trivial})
\be
\label{41x1inhom}
tqf(qt;q) +(1-2t)f(t;q)+ tq^{-1}f(q^{-1}t;q) = 1 \,.
\ee
The solution $f^{(0)}$ at $t=0$ given in Equation~\eqref{g2} below is a resummation
of the Kashaev invariant of the $4_1$ knot, whereas the solution $g^{(0,2)}$ 
given in Equation~\eqref{f0x1} below is a $q$-series that appeared recently
in~\cite{GGMW:trivial} in relation to the asymptotic expansion of the Kashaev
invariant at the trivial representation. With those two solutions, we define
the fundamental matrices
\be
\label{UVex41b}
\begin{aligned}
  U(t,\lambda_{1},\lambda_{2},q)
  &=W(f^{(1)}(t,\lambda_{1},q),f^{(-1)}(t,q),f^{(0)}(t,\lambda_{2},q)) \\
V(t,q) &= W(g^{(0,0)}(t,q), g^{(0,1)}(t,q), g^{(0,2)}(t,q)) \,,
\end{aligned}
\ee
with equal weights $\kappa=(2,1,0)$. The monodromy matrix involves the Weierstrass
elliptic function $\wp$, a well-known function discussed in detail for example
in~\cite{Akhiezer}.

\begin{theorem}
\label{thm.41b} 
{\rm (a)} The monodromy matrix $\vM(t,\lambda_{1},\lambda_{2},q)
= V(t,q)^{-1}U(t,\lambda_{1},\lambda_{2},q)$ is given by
\be
\label{M413}
\vM(t,\lambda_{1},\lambda_{2},q) =
\begin{pmatrix}
- 1 & 0 & \wp(t,q)\\
\vM_{2,1}(t,\lambda_{1},q) & 1 &
\frac{1}{2}\frac{\wp'(t,q)-\wp'(\lambda_{2},q)}{\wp(t,q)-\wp(\lambda_{2},q)}\\
0 & 0 & 1
\end{pmatrix}
\ee
where $\vM_{2,1}$ is given by~\eqref{M412}. The matrix $M$ satisfies the
modular transformations~\eqref{M41c} with weight $\kappa=(2,1,0)$. 
\newline
{\rm (b)}
The two cocycles~\eqref{Om} $\Om_{\Av(U)}$ and $\Om_{V}$ are equal,
modular, independent of $\lambda_{1},\lambda_{2}$ and when $\gamma=S$,
they are given by combinations of elementary functions times the state integrals







\be
\int_{\BR+i\ve}
\Phi_{\sfb}(x)^2
\frac{\exp\left(-\pi i x^{2}-2\pi\sfb^{-1}zx\right)}{1+\tq^{1/2}
  \exp\left(-2\pi\sfb^{-1}x\right)}dx\,.
\ee
\end{theorem}



The second and last extension of equation~\eqref{41x1inhom} is the addition of
an $x$-variable in $\BC^\times$, which topologically measures the holonomy of the
meridian of the knot, or the color of the colored Jones polynomial, and behaves
like a Jacobi variable. The new equations are now a two variable holonomic
system and take the form 
{\small
\begin{subequations}
\be
\label{41x.inhom}
\begin{aligned}
tqf(qt,x,q)+(1-(x^{-1}+x)t)f(t,x,q) + tq^{-1}f(q^{-1}t,x,q)
=
1 
\end{aligned}
\ee
\be
\label{41x2.inhom}
\begin{aligned}
(1-qx)(1-q^{-1}x^{2})&f(t,qx,q)\\
-(x-1)^2&(x+1)(x^2t-x-(q^{-1}+q)t-x^{-1}+x^{-2}t)f(t,x,q)\\
+&(1-qx^2)(1-q^{-1}x)f(t,q^{-1}x,q)
=
(1+x^{-1})(1-qx^2)(1-q^{-1}x^{2}) \,,
\end{aligned}
\ee
\be
\label{41x3.inhom}
(1-xq)(f(t,qx,q)-x^{-1}f(qt,qx,q))=(1-x^{-1})(f(t,x,q)-qxf(qt,x,q)) \,.
\ee
\end{subequations}
}
This is not a random system of equations, instead they are the defining equations
of the descendant colored Jones polynomial of the $4_1$ knot, and appeared
explicitly in~\cite[Eqn.(97)]{GGMW:trivial}. This is a $q$-holonomic module of
rank 3, with fundamental solutions $f^{(j)}(t,x,q)$ for $j=-1,0,1$ at $t=0$
and $g^{(0,x^{j})}(t,x,q)$ for $j=-1,0,1$ at $t=\infty$ defined
in Equations~\eqref{sols.41.x}, \eqref{f0x} and~\eqref{gGM}. 
With these solutions we can define the fundamental matrices with respect
to the shift in $t$ as
\be
\label{UVex41.x}
\begin{aligned}
  U(t,x,\lambda_{1},\lambda_{2},q)
  &=W(f^{(1)}(t,x,\lambda_{1},q),f^{(-1)}(t,x,q),f^{(0)}(t,x,\lambda_{2},q))\,, \\
V(t,x,q) &= W(g^{(0,x^{-1})}(t,x,q), g^{(0,x)}(t,x,q), g^{(0,1)}(t,x,q)) \,,
\end{aligned}
\ee
with weights $\kappa_{U}=(0,1,0)$ and $\kappa_{V}=(1,1,0)$.
The next theorem gives the properties of this monodromy.

\begin{theorem}
\label{thm.41c}
{\rm (a)} The monodromy matrix is given by
  \be
  {\small
\begin{aligned}
  \label{m3x3x}
&\vM(t,x,\lambda_{1},\lambda_{2},q)
=
\begin{pmatrix}
1 & -1 & 0\\
-1 & -1 & 0\\
0 & 0 & 1
\end{pmatrix} \times \\ 
&\begin{pmatrix}
  \frac{\theta(x^{-2};q)
    \theta(t;q)^2(q;q)_{\infty}^3}{2\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)}
  & 0 & \frac{\theta(x^{-2};q)
  \theta(t;q)^2(q;q)_{\infty}^{3}}{2\theta(q^{-1}x;q)^2\theta(tx;q)\theta(tx^{-1};q)}\\
  m_{2,1}(t,x,\lambda_{1},q) & 1 &
  \left(\frac{\theta'(t\lambda_{2})}{\theta(t\lambda_{2})}
-\frac{\theta'(tx)}{2\theta(tx)}-\frac{\theta'(tx^{-1})}{2\theta(tx^{-1})}
-\frac{\theta'(\lambda_{2})}{\theta(\lambda_{2})}-\frac{1}{2}\right)\\
  0 & 0 & 1
\end{pmatrix}
\end{aligned}
  }
  \ee
  where $m_{2,1}(t,x,\lambda_{1},q)$ is the unique elliptic function in $t$
  satisfying $m_{2,1}(1,x,\lambda_{1},q)=0$ with simple poles at $t_0\in
\{x^{\pm}q^{\BZ},\pm\lambda^{-1}q^{\frac{1}{2}\BZ}\}$ and residues
$\rho_{t_0}:=\Res_{t=t_0}m_{2,1}(t,x,\lambda_{1},q)\frac{dt}{2\pi i t}$ given by
  \be
  \label{m21resx}
\begin{aligned}
  \rho_{x^{\pm}q^{\BZ}} &=
  \frac{-1}{2} \\
  \rho_{\pm\lambda_{1}^{-1}q^{-1/4-\BZ}} &=
  \frac{\theta(\pm q^{3/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
\theta(\pm q^{-3/4}x;q)
\theta(\pm q^{-3/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
\theta(q^{-1}\lambda_{1};q)\theta(q^{-3/2}\lambda_{1};q)} \\
  \rho_{\pm\lambda_{1}^{-1}q^{-3/4-\BZ}} &=
  \frac{\theta(\pm q^{1/4}\lambda_{1}^{-1};q)\theta(\pm q^{-1/4}x;q)
  \theta(\pm q^{-3/4}x;q)
  \theta(\pm q^{-1/4}\lambda_{1};q)}{2\theta(x;q)\theta(x^{-1};q)
  \theta(q^{-1/2}\lambda_{1};q)\theta(q^{-1}\lambda_{1};q)}\,.
  \end{aligned}
  \ee
The monodromy satisfies the following modular transformations
\be
\label{M41x}
\Delta_{T^{2},\kappa_{V}}\vM|_{\kappa_{U}}T^2=\vM,\quad
\Delta_{STS,\kappa_{V}}\vM|_{\kappa_{U}}STS=\vM,\quad
\Delta_{TST,\kappa_{V}}\vM|_{\kappa_{U}}TST=\vM\,.
\ee
{\rm (b)}
The two cocycles~\eqref{Om} $\Om_{\Av(U)}$ and $\Om_{V}$ are equal,
modular, independent of $\lambda_{1},\lambda_{2}$ and when $\gamma=S$, they
are given by combinations of elementary functions times the state integrals








\be
\int_{\calC}
\Phi_{\sfb}(x+i\sfb u)\Phi_{\sfb}(x-i\sfb u)
\frac{\exp\left(-\pi i x^{2}-2\pi\sfb^{-1} zx\right)}{1+\tq^{1/2}
  \exp\left(-2\pi\sfb^{-1}x\right)}dx\,.
\ee
\end{theorem}

An explicit formula for the function $m_{2,1}$ is given in Equation
~\eqref{m21explicit} below.

The next theorem identifies the function 
$f^{(0)}(t,x,\lambda_{1},q)$ with the $q$-Borel resummation of the descendant of
the colored Jones polynomial, and provides a lift of the colored Jones polynomial
(as a function of $N$ and $q$) to an analytic function of $x$ and $q$.  
Its extension to all knots will be discussed in forthcoming work. 

\begin{theorem}
  \label{thm.CJ41lift}
  The $N$-th colored Jones polynomial $J_{N}(q)$ of $4_{1}$ for $|q|<1$ is given by
  \be
  \label{J41f0}
J_{N}(q)=f^{(0)}(1,q^{N},\lambda_{2},q) \,.
  \ee
\end{theorem}
Note that there is no $\lambda_{2}$ dependence on the left hand side of
~\eqref{J41f0} and that $\lambda_{2}$ parametrises a family of analytic
continuations of the colored Jones polynomial as we vary $x$ away from $q^{N}$.

The cocycles given in the previous theorems reveal the relation of the
following three special functions (all being entries of a matrix-valued
$S$-cocycle of a modular $q$-difference equation)
  \begin{itemize}
\item[(a)] the Fadeev quantum dilogarithm
\item[(b)] the Mordell integral
\item[(c)] the Andersen-Kashaev state integral. 
\end{itemize}

We end this section with some comments regarding modular $q$-holonomic modules.
It is not obvious that $q$-holonomic modules exist or occur naturally. Yet,
they are abundant, for instance all proper $q$-hypergeometric multidimensional
sums are $q$-holonomic; see  Zeilberger--Wilf~\cite{WZ}. A detailed introduction
of $q$-holonomic modules and their functional and closure properties can be found
in~\cite{GL:survey,Koutschan:HF,PWZ}. 

Regarding the occurence of $q$-holonomic modules, they are often given in the form
$M_f=\calW f$ where $f: \BZ^r \to \BQ(q)$ is a quantum invariant. For instance,
if $f$ denotes the colored Jones polynomial of a link (colored with an arbitrary
representation of a fixed simple Lie group), or the colored HOMFLY-PT polynomial
of a link (colored by arbitrary partitions with a fixed number of rows or columns),
the corresponding modules $M_f$ are $q$-holonomic; see~\cite{GL} and~\cite{GLL}.
In addition, the special $q$-hypergeometric sums (so-called Nahm sums) studied
in~\cite[Sec.4.7]{GZ:kashaev} that depend on the upper-half of a symplectic matrix,
are $q$-holonomic. Moreover, the linear $q$-difference equations in quantum cohomology
or in quantum $K$-theory are often (and perhaps always?) specialisations of
$q$-hypergeometric series; see~\cite{OP,GS:quintic,Iritani:rec,Wen}.
Finally, the $q$-GKZ modules of Gelfand--Kapranov--Zelevinsky~\cite{Gelfand3,Gelfand2,
  Gelfand1} which are constructed by combinatorial data (a matrix of integers) together
with some ``charge vectors'' are $q$-holonomic.

The above discussion leads naturally to the following conjecture.

\begin{conjecture}
\label{conj.2}
Every $q$-holonomic module associated to a proper $q$-hypergeometric multi-dimensional
sum is modular.
\end{conjecture}
