---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-022-5-a-q-difference-equation-of-the-41-knot
section_title: "A q-difference equation of the 41 knot"
section_number: 5
pages: 37-40
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.828
latex_coverage_ratio: 0.911
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sec.41}

This section is devoted to the proof of Theorem~\ref{thm.41},
Theorem~\ref{thm.41b} and Theorem~\ref{thm.41c}.


\subsection{Solutions}
\label{subsec.41sols}

The $q$-difference equation~\eqref{41x1} has Newton polygon shown in Figure
~\ref{f.41x1}.

\begin{figure}[!htpb]
\begin{center}
\begin{tikzpicture}[scale=0.8,baseline=-3]
\draw[<->,thick] (-3.5,0) -- (3.5,0);
\draw[<->,thick] (0,-1.5) -- (0,3.5);
\foreach \x in {-2,2}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0,0) circle (2pt);
\filldraw (0,2) circle (2pt);
\filldraw (-2,2) circle (2pt);
\filldraw (2,2) circle (2pt);
\node at (-1,2.4) {$g^{(0,0)}$};
\node at (1,2.4) {$g^{(0,1)}$};
\node at (-1.6,0.8) {$f^{(-1)}$};
\node at (1.6,0.8) {$f^{(1)}$};
\draw (0,0) -- (2,2) -- (-2,2) -- cycle;
\fill[blue,opacity=0.2] (0,0) -- (2,2) -- (-2,2) -- cycle;
\end{tikzpicture}
\caption{The Newton polygon of Equation~\eqref{41x1}.}
\label{f.41x1}
\end{center}
\end{figure}

\noindent
The boundary of the lower Newton polygon has edges of slope $-1$ and $1$. The
edge with slope $-1$ must be divided by a $\theta$-function to get a power series
solution. The effect on the Newton polygon is as follows.
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-2,0) -- (2,0);
\draw[<->,thick] (0,-1) -- (0,2);
\foreach \x in {-1,1}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0,0) circle (2pt);
\filldraw (0,1) circle (2pt);
\filldraw (-1,1) circle (2pt);
\filldraw (1,1) circle (2pt);
\draw (0,0) -- (1,1) -- (-1,1) -- cycle;
\fill[blue,opacity=0.2] (0,0) -- (1,1) -- (-1,1) -- cycle;
\node at (-0.8,0.35) {\begin{tiny}$f^{(-1)}$\end{tiny}};
\draw[->,ultra thick] (3,0) -- (4,0);
\node at (3.5,0.4) {$\theta(t;q)^{-1}$};
\draw[<->,thick] (-2+7,0) -- (2+7,0);
\draw[<->,thick] (0+7,-1) -- (0+7,2);
\foreach \x in {-1+7,1+7}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0+7,0) circle (2pt);
\filldraw (0+7,1) circle (2pt);
\filldraw (-1+7,0) circle (2pt);
\filldraw (1+7,2) circle (2pt);
\draw (0+7,0) -- (1+7,2) -- (-1+7,0) -- cycle;
\fill[blue,opacity=0.2] (0+7,0) -- (1+7,2) -- (-1+7,0) -- cycle;
\node at (-0.5+7,-0.25) {\begin{tiny}$\hat{f}^{(-1)}$\end{tiny}};
\end{tikzpicture}
\end{center}
Therefore, the bottom edge of the Newton polygon with slope $-1$ has a solution
of the form
\be
f^{(-1)}(t,q)
=
\theta(t;q)^{-1}\hat{f}^{(-1)}(t,q)
=
\theta(t;q)^{-1}\sum_{k=0}^{\infty}\alpha_{k}^{(-1)}(q)t^{k}
\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\ee
where
\be
(1-q^{-k-1}\rind^{-1})\alpha_{k}^{(-1)}(q)-2\alpha_{k-1}^{(-1)}(q)
-q^{k}\rind\alpha_{k-2}^{(-1)}(q)=0.
\ee
Therefore, this edge has indicial polynomial
\be
(1-q^{-1}\rind^{-1})\alpha_{0}^{(-1)}(q)
\ee
and so $\rind=q^{-1}$. Now notice that if we take the $(-1)$-$q$-Borel transform we
see the effect on the Newton polygon is as follows.
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-2,0) -- (2,0);
\draw[<->,thick] (0,-1) -- (0,2);
\foreach \x in {-1,1}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0,0) circle (2pt);
\filldraw (0,1) circle (2pt);
\filldraw (-1,0) circle (2pt);
\filldraw (1,2) circle (2pt);
\draw (0,0) -- (1,2) -- (-1,0) -- cycle;
\fill[blue,opacity=0.2] (0,0) -- (1,2) -- (-1,0) -- cycle;
\node at (-0.5,-0.25) {\begin{tiny}$\hat{f}^{(-1)}$\end{tiny}};
\draw[ultra thick,->] (3,0) -- (4,0);
\node at (3.5,0.4) {$\Bor_{-1}$};
\draw[<->,thick] (-2+7,0) -- (1+7,0);
\draw[<->,thick] (0+7,-1) -- (0+7,2);
\foreach \x in {1}
\draw[thick] (-0.1+7,\x) -- (0.1+7,\x);
\filldraw (0+7,0) circle (2pt);
\filldraw (-1+7,1) circle (2pt);
\filldraw (-1+7,0) circle (2pt);
\filldraw (-1+7,2) circle (2pt);
\draw (0+7,0) -- (-1+7,2) -- (-1+7,0) -- cycle;
\fill[blue,opacity=0.2] (0+7,0) -- (-1+7,2) -- (-1+7,0) -- cycle;
\node at (-0.7+7,-0.25) {\begin{tiny}$\Bor_{-1}\hat{f}^{(-1)}$\end{tiny}};
\end{tikzpicture}
\end{center}
This means that this Borel transform will satisfy the $q$-difference equation
\be
(1-q^{-1}t)^{2}\Bor_{-1}\hat{f}^{(-1)}(q^{-1}t;q)
=
\Bor_{-1}\hat{f}^{(-1)}(t,q).
\ee
Therefore, normalising so that $\alpha_{0}(q)=-(q;q)_{\infty}^{2}$ we have
\be
\Bor_{-1}\hat{f}^{(-1)}(t,q)
=
\sum_{k=0}^{\infty}(-1)^{k}q^{-k(k+1)/2}\alpha_{k}^{(-1)}(q)t^{k}
=
\frac{-(q;q)_{\infty}^{2}}{(t;q)_{\infty}^{2}}.
\ee
Therefore, we see that
\be
\alpha^{(-1)}_{k}(q)=(q;q)_{\infty}^{2}(-1)^{k+1}q^{k(k+1)/2}
\sum_{\ell=0}^{k}\frac{1}{(q;q)_{\ell}(q;q)_{k-\ell}}.
\ee
In particular, we have
\be
\label{ex41.f-1}
f^{(-1)}(t,q)=(q;q)_{\infty}^{2}\theta(q^{-1}t;q)^{-1}\sum_{k=0}^{\infty}
\sum_{\ell=0}^{k}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{\ell}(q;q)_{k-\ell}}t^{k} \,.
\ee
Now the bottom edge of slope $1$ must be multiplied by a $\theta$-function to get
a power series solution. However, this will then be divergent so we must take
$(1/2)$-$q$-Borel resummation. The effect on the Newton polygon is as follows.
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-2-5,0) -- (2-5,0);
\draw[<->,thick] (0-5,-1) -- (0-5,3);
\foreach \x in {-1-5,1-5}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\foreach \x in {2}
\draw[thick] (-5.08,\x) -- (-4.92,\x);
\filldraw (0-5,0) circle (2pt);
\filldraw (0-5,1) circle (2pt);
\filldraw (-1-5,1) circle (2pt);
\filldraw (1-5,1) circle (2pt);
\draw (0-5,0) -- (1-5,1) -- (-1-5,1) -- cycle;
\fill[blue,opacity=0.2] (0-5,0) -- (1-5,1) -- (-1-5,1) -- cycle;
\node at (0.7-5,0.25) {\begin{tiny}$f^{(1)}$\end{tiny}};
\draw[->,ultra thick] (-2.8,0) -- (-2.2,0);
\node at (-2.5,0.4) {$\theta(t;q)$};
\draw[<->,thick] (-2,0) -- (2,0);
\draw[<->,thick] (0,-1) -- (0,3);
\foreach \x in {-1,1}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\foreach \x in {2}
\draw[thick] (-2pt,\x) -- (2pt,\x);
\filldraw (0,0) circle (2pt);
\filldraw (0,1) circle (2pt);
\filldraw (-1,2) circle (2pt);
\filldraw (1,0) circle (2pt);
\draw (0,0) -- (-1,2) -- (1,0) -- cycle;
\fill[blue,opacity=0.2] (0,0) -- (-1,2) -- (1,0) -- cycle;
\node at (0.5,-0.25) {\begin{tiny}$\hat{f}^{(1)}$\end{tiny}};
\draw[->,ultra thick] (2.2,0) -- (2.8,0);
\node at (2.5,0.4) {$\Bor_{1/2}$};
\draw[<->,thick] (-2+5,0) -- (2+5,0);
\draw[<->,thick] (0+5,-1) -- (0+5,3);
\foreach \x in {1}
\draw[thick] (4.92,\x) -- (5.08,\x);
\foreach \x in {4}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0+5,0) circle (2pt);
\filldraw (1/2+5,1) circle (2pt);
\filldraw (1+5,0) circle (2pt);
\filldraw (0+5,2) circle (2pt);
\draw (0+5,0) -- (0+5,2) -- (1+5,0) -- cycle;
\fill[blue,opacity=0.2] (0+5,0) -- (0+5,2) -- (1+5,0) -- cycle;
\node at (0.6+5,-0.28) {\begin{tiny}$\Bor_{1/2}\hat{f}^{(1)}$\end{tiny}};
\end{tikzpicture}
\end{center}
By symmetry of the $q$-difference equation, one can easily use the previous
solution to check that the formal solution to this edge is given by
$q\mapsto q^{-1}$ which gives
\be
f^{(1)}(t,q)
=
\frac{\theta(t;q)}{(q;q)_{\infty}^{2}}\hat{f}^{(1)}(t,q)
=
\frac{\theta(t;q)}{(q;q)_{\infty}^{2}}\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}
\frac{q^{\ell^2-\ell k}}{(q;q)_{\ell}(q;q)_{k-\ell}}t^{k}.
\ee
One then sees that
\be
\begin{aligned}
\Bor_{1/2}\hat{f}^{(1)}(\xi,q)
&=
\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}(-1)^{k}
\frac{q^{k(k+1)/4+\ell^2-\ell k}}{(q;q)_{\ell}(q;q)_{k-\ell}}\xi^{k}
&=
\sum_{k,\ell=0}^{\infty}(-1)^{k+\ell}
\frac{q^{k(k+1)/4-k\ell/2+\ell(\ell+1)/4}}{(q;q)_{k}(q;q)_{\ell}}\xi^{k+\ell}
\end{aligned}
\ee
is holomorphic for $|\xi|<|q^{-1/4}|$. Then, using the functional equation
\be
(1-q^{1/2}\xi^2)\Bor_{1/2}\hat{f}^{(1)}(\xi,q)+
2\xi\Bor_{1/2}\hat{f}^{(1)}(q^{1/2}\xi,q)-\Bor_{1/2}\hat{f}^{(1)}(q\xi,q)=0,
\ee
we can analytically extend away from $\xi\in\pm q^{-1/4+\frac{1}{2}\BZ_{\leq0}}$
and we see that there are poles at $\xi\in\pm q^{-1/4+\frac{1}{2}\BZ_{\leq0}}$.
Therefore, we finally define
\be
\label{ex41.f1}
\begin{aligned}
f^{(1)}(t,\lambda,q)
&=
\frac{\theta(t;q)}{(q;q)_{\infty}^{2}}\Lap_{1/2}\Bor_{1/2}
\hat{f}^{(1)}(t,\lambda,q)\\
&=
\frac{\theta(t;q)}{(q;q)_{\infty}^{2}}\sum_{n\in\BZ}\frac{\Bor_{1/2}\hat{f}^{(1)}
(q^{\frac{n}{2}}\lambda t,q)}{\theta(q^{\frac{n}{2}}\lambda;q^{\frac{1}{2}})}\\
&=
\frac{\theta(t;q)}{(q;q)_{\infty}^{2}\theta(\lambda;q^{1/2})}
\sum_{n\in\BZ}(-1)^{n}q^{n(n+1)/4}\lambda^{n}\Bor_{1/2}
\hat{f}^{(1)}(q^{\frac{n}{2}}\lambda t,q).
\end{aligned}
\ee
Now the top of the Newton polygon has one edge of slope $0$. We find the solution
satisfies
\be
g^{(0)}(t,q)
=
\sum_{k=0}^{\infty}\beta_{k}(q)t^{-k}\frac{\theta(\rind^{-1}t;q)}{\theta(t;q)}
\quad\text{where}\quad
\beta_{k}(q)-q^{-k}\rind^{-1}(1-q^{k}\rind^{-1})^{2}\beta_{k+1}(q)=0.
\ee
Therefore, as the indicial polynomial is
\be
(1-q^{-1}\rind^{-1})^{2}\beta_{0}(q)=0
\ee
we take $\rind=q^{-1}e^\ve$ and expand to order $\ve^{2}$ to find
solutions
\be
\begin{aligned}
g^{(0)}(t,\ve,q)
&=
\sum_{k=0}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}t^{-1-k}\\
&+\left(\sum_{k=0}^{\infty}
  \left(\frac{1}{2}E_{1}(q)-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}\right)
  (-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}t^{-1-k}\right)\ve+O(\ve^{2})\,,
\end{aligned}
\ee
where $E_{1}(q)=1-4\sum_{j=1}^{\infty}\frac{q^{j}}{1-q^{j}}$.
Therefore, we have solutions
\be
\label{ex41.g00}
\begin{aligned}
g^{(0,0)}(t,q)
&=
\sum_{k=0}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}t^{-1-k}\\
g^{(0,1)}(t,q)
&=
\sum_{k=0}^{\infty}\left(\frac{1}{2}E_{1}(q)-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}\right)(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}t^{-1-k}.
\end{aligned}
\ee
