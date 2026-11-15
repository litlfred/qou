---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-027-56-the-inhomogeneous-equation
section_title: "The inhomogeneous equation"
section_number: 5.6
pages: 47-52
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.954
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sec.4.inhom.x1}

We now consider Equation~\eqref{41x1inhom}.
We can convert this into a homogeneous equation of one degree higher
\be
tf(t;q)+(1-3qt)f(qt;q)+(3tq^2-1)f(q^2t;q)-tq^3f(q^3t;q)=0
\ee
with Newton polygon shown in Figure~\ref{f.413}.

\begin{figure}[!htpb]
\begin{center}
\begin{tikzpicture}[scale=0.8,baseline=-3]
\draw[<->,thick] (-1.5,0) -- (7.5,0);
\draw[<->,thick] (0,-1.5) -- (0,3.5);
\foreach \x in {2,4,6}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0,2) circle (2pt);
\filldraw (2,0) circle (2pt);
\filldraw (2,2) circle (2pt);
\filldraw (4,0) circle (2pt);
\filldraw (4,2) circle (2pt);
\filldraw (6,2) circle (2pt);
\node at (1,2.3) {$g^{(0,0)}$};
\node at (3,2.3) {$g^{(0,1)}$};
\node at (5,2.3) {$g^{(0,2)}$};
\node at (0.5,0.8) {$f^{(-1)}$};
\node at (5.5,0.8) {$f^{(1)}$};
\node at (3,-0.3) {$f^{(0)}$};
\draw (0,2) -- (2,0) -- (4,0) -- (6,2) -- cycle;
\fill[blue,opacity=0.2] (0,2) -- (2,0) -- (4,0) -- (6,2) -- cycle;
\end{tikzpicture}
\caption{The Newton polygon of Equation~\eqref{41x1inhom}.}
\label{f.413}
\end{center}
\end{figure}

\noindent
Now from the general theory the solutions $f^{(\pm1)}$ and $g^{(0,0)}$ and
$g^{(0,1)}$ are the same as the solutions in Section~\ref{subsec.41sols}. We do
find two additional
solutions which are in fact solutions to the inhomogeneous equation, namely
\be
\hat{f}^{(0)}(t,q)=\sum_{k=0}^{\infty}(-1)^{k}q^{-k(k+1)/2}(q;q)_{k}^{2}t^{k} \,,
\ee
a divergent formal power series solution at $t=0$ and
\be
\label{g2}
{\small
\begin{aligned}
g^{(0,2)}(t;q)
&=
\sum_{k=0}^{\infty}\left(\frac{1}{2}\Bigg(\frac{1}{2}E_{1}(q)-\frac{1}{2}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}\right)^{2}
  -\left(\frac{1}{2}E_{1}(q)-\frac{1}{2}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}\right)\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}\\
  &\qquad\qquad+\frac{1}{2}\frac{\theta''(t^{-1};q)}{\theta(t^{-1};q)}
  +\sum_{j=1}^{k}\frac{q^{j}}{(1-q^{j})^2}-\frac{1}{24}-\frac{1}{24}E_{2}(q)\Bigg)
(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}t^{-1-k}\,,
\end{aligned}
}
\ee
where $E_{2}(q)=1-24\sum_{k=0}^{\infty}q^{k}/(1-q^{k})^2$,
a convergent solution at $t=\infty$. So, we must resum $\hat{f}^{(0)}(t,q)$. For $|\xi|<1$, we have
\be
\Bor_{1}\hat{f}^{(0)}(\xi,q)
=
\sum_{k=0}^{\infty}(q;q)_{k}^{2}\xi^{k}
\ee
which can be analytically continued away from $\xi\in q^{\BZ_{\leq0}}$ using the
relation
\be
(1-\xi)\Bor_{1}\hat{f}^{(0)}(\xi,q)+2q\xi \Bor_{1}\hat{f}^{(0)}(q\xi,q)
-q^2\xi \Bor_{1}\hat{f}^{(0)}(q^{2}\xi,q) = 1.
\ee
\begin{center}
\begin{tikzpicture}
\draw[<->,thick] (-1,0) -- (4,0);
\draw[<->,thick] (0,-1) -- (0,2);
\foreach \x in {1,2,3}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0,1) circle (2pt);
\filldraw (1,0) circle (2pt);
\filldraw (1,1) circle (2pt);
\filldraw (2,0) circle (2pt);
\filldraw (2,1) circle (2pt);
\filldraw (3,1) circle (2pt);
\draw (0,1) -- (1,0) -- (2,0) -- (3,1) -- cycle;
\fill[blue,opacity=0.2] (0,1) -- (1,0) -- (2,0) -- (3,1) -- cycle;
\node at (1.5,-0.25) {\begin{tiny}$f^{(0)}$\end{tiny}};
\draw[->,ultra thick] (3+2,0) -- (4+2,0);
\node at (3.5+2,0.4) {$\Bor_{1}$};
\draw[<->,thick] (-1+8,0) -- (4+8,0);
\draw[<->,thick] (0+8,-1) -- (0+8,2);
\foreach \x in {1+8,2+8,3+8}
\draw[thick] (\x,-2pt) -- (\x,2pt);
\filldraw (0+8,1) circle (2pt);
\filldraw (0+8,0) circle (2pt);
\filldraw (1+8,1) circle (2pt);
\filldraw (1+8,0) circle (2pt);
\filldraw (2+8,1) circle (2pt);
\filldraw (3+8,1) circle (2pt);
\draw (0+8,1) -- (0+8,0) -- (1+8,0) -- (3+8,1) -- cycle;
\fill[blue,opacity=0.2] (0+8,1) -- (0+8,0) -- (1+8,0) -- (3+8,1) -- cycle;
\node at (1.5+8,-0.25) {\begin{tiny}$\Bor_{1}f^{(0)}$\end{tiny}};;
\end{tikzpicture}
\end{center}
Therefore, we define
\be\label{f0x1}
f^{(0)}(t,\lambda_{2},q)
=
(\Lap_{1}\Bor_{1}\hat{f}^{(0)})(t,\lambda_{2},q)
=
\frac{1}{\theta(\lambda_{2};q)}\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)}
\lambda_{2}^{k}\Bor_{1}\hat{f}^{(0)}(q^{k}\lambda_{2}t,q).
\ee
Now we consider the matrices
\be
\label{U413}
\begin{aligned}
&U(t,\lambda_{1},\lambda_{2},q)
=
W(f^{(1)}(t,\lambda_{1},q),f^{(-1)}(t,q),f^{(0)}(t,\lambda_{2},q))\\
&=
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-2}t^{-1} & -q^{-2} & q^{-2}t^{-1}-2q^{-1}
\end{pmatrix}
\begin{pmatrix}
0 & 0 & 1\\
f^{(1)}(t,\lambda_{1},q) & f^{(-1)}(t,q) & f^{(0)}(t,\lambda_{2},q)\\
f^{(1)}(qt,\lambda_{1},q) & f^{(-1)}(qt,\lambda_{1},q) & f^{(0)}(qt,\lambda_{2},q)
\end{pmatrix}
\end{aligned}
\ee
and
\be
\label{V413}
\begin{aligned}
V(t,q)
&=
W(g^{(0,0)}(t,q),g^{(0,1)}(t,q),g^{(0,2)}(t,q))\\
&=
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-2}t^{-1} & -q^{-2} & q^{-2}t^{-1}-2q^{-1}
\end{pmatrix}
\begin{pmatrix}
0 & 0 & 1\\
g^{(0,0)}(t,q) & g^{(0,1)}(t,q) & g^{(0,2)}(t,q)\\
g^{(0,0)}(qt,q) & g^{(0,1)}(qt,q) & g^{(0,2)}(qt,q)\\
\end{pmatrix}.
\end{aligned}
\ee
With these formulae we will now go on to prove Theorem~\ref{thm.41b}.

\begin{proof}[Proof of Theorem~\ref{thm.41b}]
  The identification of the first two columns of $\vM(t,\lambda_{1},\lambda_{2},q)$
  with those in Equation~\eqref{M413} follows from Theorem~\ref{thm.41}.
  Equations~\eqref{U413} and~\eqref{V413}, together with Lemma~\ref{lem.41det}
  imply that 
\be
-\det(U(t,\lambda_{1},\lambda_{2},q))
=
\det(V(t,q))
=
q^{-3}t^{-3} \,.
\ee
Hence, $\det(\vM(t,\lambda_{1},\lambda_{2},q))=-1$ which in turn
implies that $\vM_{3,3}(t,\lambda_{2},q)=1$.

Now, Equation~\eqref{M413}, written in the form $U(t,\lambda_{1},\lambda_{2},q)=
V(t,q) \vM(t,\lambda_{1},\lambda_{2},q)$, together with Equations~\eqref{U413}
and~\eqref{V413} and the fact that $\vM_{3,3}=1$ imply that
\be
\label{fgs0}
f^{(0)} = \vM_{1,3} g^{(0,0)} + \vM_{2,3} g^{(0,1)} + g^{(0,2)} \,.
\ee
Thus, to determine the two remaining entries of the monodromy matrix, we need to
show that the function
\be
\label{fgs}
\calE_3 :=f^{(0)} -(m_{1,3} g^{(0,0)} + m_{2,3} g^{(0,1)} + g^{(0,2)}) 
\ee
vanishes identically, where 
\be
\label{m1323}
m_{1,3}(t,q) = \wp(t,q), \qquad
m_{2,3}(t,\lambda_{2},q)
= \frac{1}{2}\frac{\wp'(t,q)-\wp'(\lambda_{2},q)}{\wp(t,q)-\wp(\lambda_{2},q)}
\ee
denote the two entries of the matrix on the right hand-side of Equation~\eqref{M413}.
Note that $\calE_3(t,\lambda_{2},q)$ is a meromorphic function of $t$
with potential simple poles at $\lambda_2^{-1} q^\BZ$ (coming from $f^{(0)}$ and
$m_{2,3}$) and potential double poles at $q^\BZ$ (coming from
$g^{(0,1)}$, $g^{(0,2)}$, $m_{1,3}$ and $m_{2,3}$). 
Since
$\Res_{t=q^{-m}\lambda_{2}^{-1}} m_{2,3}(t,\lambda_{2},q) \frac{dt}{2\pi it} = 1 \,,
$
combined with equation~\eqref{fg} gives
\be
\Res_{t=q^{-m}\lambda_{2}^{-1}}m_{2,3}(t,\lambda_{2},q)
g^{(0,1)}(t,q) \frac{dt}{2\pi it} =  f^{(-1)}(q^{-m}\lambda_{2}^{-1},q) \,,
\ee
we see from Lemma~\ref{lem.resf0} that $\calE_3$ has no poles at
$\lambda_{2}^{-1} q^\BZ$. Now noting that
\be
m_{2,3}(t,\lambda_{2},q)
=
\frac{\theta'(t^{-1};q)}{\theta'(t^{-1};q)}
+\frac{\theta'(\lambda^{-1};q)}{\theta'(\lambda^{-1};q)}
-\frac{\theta'(\lambda^{-1}t^{-1};q)}{\theta'(\lambda^{-1}t^{-1};q)}+\frac{1}{2}\,,
\ee
the only terms that contribute to the polar part of
\be
\label{gsoff0}
  g^{(0,2)}(t,q)+m_{2,3}(t, \lambda_{2},q)
  g^{(0,1)}(t,q)+m_{1,3}(t,q) g^{(0,0)}(t,q)
\ee
at $t=q^{m}\ve$ for $\ve\sim 1$ are
\be
\begin{aligned}
&\sum_{k=0}^{\infty}\bigg(
-\left(k-2E^{(k)}_{1}(q)\right)\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}
+\frac{1}{2}\frac{\theta''(q^{-m}\ve^{-1};q)}{\theta(q^{-m}\ve^{-1};q)}\\
&\qquad+\left(k-m-\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}-2E^{(k)}_{1}(q)
\right)\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}
-\frac{1}{2}\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}\\
&\qquad+\frac{\theta'(\ve^{-1};q)^2}{\theta(\ve^{-1};q)^2}
-\frac{\theta''(\ve^{-1};q)}{\theta(\ve^{-1};q)}\bigg)(-1)^{k}
\frac{q^{k(k+1)/2-m-mk}}{(q;q)_{k}^{2}}\ve^{-1-k}\\
&=\sum_{k=0}^{\infty}\bigg(
\frac{1}{2}\frac{\theta''(q^{-m}\ve^{-1};q)}{\theta(q^{-m}\ve^{-1};q)}
-\left(m+\frac{1}{2}\right)\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}
-\frac{\theta''(\ve^{-1};q)}{\theta(\ve^{-1};q)}\bigg)
(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}}\ve^{-1-k}.
\end{aligned}
\ee
This has a potentially simple pole at $\ve=1$ however noting that
\be
\begin{aligned}
  \Res_{\ve=1}\frac{\theta''(q^{-m}\ve^{-1};q)}{\theta(q^{-m}\ve^{-1};q)}
  \frac{d\ve}{2\pi i\ve}
&=
-2m+1\\
\Res_{\ve=1}\frac{\theta'(\ve^{-1};q)}{\theta(\ve^{-1};q)}\frac{d\ve}{2\pi i\ve}
&=
-1
\end{aligned}
\ee
we see that the residue vanishes and therefore \eqref{gsoff0} has a removable
singularity at all points $t\in q^{\BZ}$. Therefore, we see that $\calE_3$ is
a holomorphic (for $t \in \BC^\times$) solution of Equation~\eqref{41x1} and
therefore from Corollary~\ref{cor:41holsol} we see that
$\calE_3(t,\lambda_{2},q) = C(q)g^{(0,0)}(t,q)$. 
To finish the proof we note that for $t$ on some compact set where the functions
are holomorphic, Lemma~\ref{lem.fglimits} and Lemma~\ref{lem.fglimits.inhom}
implies that
\begin{align*}
-\frac{C(q)}{(q;q)_{\infty}^{2}} &=
\lim_{r\rightarrow\infty}\frac{C(q) g^{(0,0)}(t^r,q)}{\theta(q^{r}t;q)} \\  
&=\lim_{r\rightarrow\infty}\frac{
f^{(0)}(t,\lambda_{2},q)-(g^{(0,2)}(t,q) + m_{2,3}(t,\lambda_{2},q)
g^{(0,1)}(t,q) + m_{1,3}(t,q)  g^{(0,0)}(t,q))}{\theta(q^{r}t;q)} \\ &=
\frac{1}{(q;q)_{\infty}^{2}}(m_{1,3}(t^{-1},q)-m_{1,3}(t,q))= 0 \,,
\end{align*}
where we note that $m_{1,3}(t,q)$ is the Weierstrass $\wp$-function plus a
constant which is even in $z$ where $t=\e(z)$.

Our next task is to compute the residues of $f^{(0)}$. 

\begin{lemma}
\label{lem.resf0}
\rm{(a)}
The function $\Bor_{1}\hat{f}^{(0)}(\xi,q)$ has simple poles at $\xi \in q^\BZ$
with residue
\be
\label{resBf0}
R(m,q) :=
\Res_{\xi=q^{-m}}\Bor_{1}\hat{f}^{(0)}(\xi,q)\frac{d\xi}{2\pi i\xi}
= -(q;q)_{\infty}^{2}\sum_{\ell=0}^{m}\frac{q^{m}}{(q;q)_{\ell}(q;q)_{m-\ell}} \,.
\ee
\rm{(b)}
The function $f^{(0)}(t,q)$ has simple poles at $t\in \lambda_{2}^{-1}q^{\BZ}$
with residue
\be
\label{resf0}
\Res_{t=q^{-m}\lambda_{2}^{-1}}f^{(0)}(t,\lambda_{2},q)\frac{dt}{2\pi it} =
f^{(-1)}(q^{-m}\lambda_{2}^{-1},q) \,.
\ee
\end{lemma}

\begin{proof}
For part (a), notice that
\be
\begin{aligned}
\Bor_{1}\hat{f}^{(0)}(\xi,q)
&=
\sum_{k=0}^{\infty}(q;q)_{k}^{2}\xi^{k}
=
(q;q)_{\infty}^{2}\sum_{k=0}^{\infty}\frac{1}{(q^{k+1};q)_{\infty}}\xi^{k}\\
&=
(q;q)_{\infty}^{2}\sum_{k,\ell,n=0}^{\infty}
\frac{q^{kn+k\ell+n+\ell}}{(q;q)_{\ell}(q;q)_{n}}\xi^{k}
=
(q;q)_{\infty}^{2}\sum_{\ell,n=0}^{\infty}\frac{q^{n+\ell}}{
  (q;q)_{\ell}(q;q)_{n}(1-q^{n+\ell}\xi)}
\end{aligned}
\ee
is the analytic continuation of $\Bor_{1}\hat{f}^{(0)}$. From this, it clearly
follows that the only poles are simple, located at $\xi=q^\BZ$. (Alternatively,
one can also use the linear $q$-difference equation satisfied by this function,
though this is not needed here). We compute the residue as follows:
\be
\begin{aligned}
R(m,q)
&=
\Res_{\xi=q^{-m}}(q;q)_{\infty}^{2}\sum_{\ell,n=0}^{\infty}
\frac{q^{n+\ell}}{(q;q)_{\ell}(q;q)_{n}(1-q^{n+\ell}\xi)}\frac{d\xi}{2\pi i\xi}\\
&=
-(q;q)_{\infty}^{2}\sum_{\ell=0}^{m}\frac{q^{m}}{(q;q)_{\ell}(q;q)_{m-\ell}}.
\end{aligned}
\ee

For part (b), the pole structure is clear noting that Equation~\eqref{f0x1}
is convergent if all the terms are and that
$\Bor_{1}\hat{f}^{(0)}(q^{k}t\lambda_{2},q)$ has poles at
$t\in\lambda_{2}^{-1}q^{\BZ_{\leq -k}}$. We compute the residues as follows:
\be
\begin{aligned}
\Res_{t=q^{-m}\lambda_{2}^{-1}}&\,f^{(0)}(t,\lambda_{2},q)\frac{dt}{2\pi it}
=
\Res_{t=q^{-m}\lambda_{2}^{-1}}(\Lap_{1}\Bor_{1}\hat{f}^{(0)})(t,\lambda_{2},q)
\frac{dt}{2\pi it}\\
&=
\Res_{t=q^{-m}\lambda_{2}^{-1}}\frac{1}{\theta(\lambda_{2},q)}
\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)/2}\lambda_{2}^{k}\Bor_{1}\hat{f}^{(0)}(q^{k}
\lambda_{2}t,q)\frac{dt}{2\pi it}\\
&=
\frac{1}{\theta(\lambda_{2},q)}\sum_{k\in\BZ}(-1)^{k}q^{k(k+1)/2}
\lambda_{2}^{k}R(m-k,q)\\



&=
\frac{1}{\theta(\lambda_{2},q)}(-1)^{m}q^{m(m+1)/2}\lambda_{2}^{m}
\sum_{k=0}^{\infty}(-1)^{k}q^{k(k-1)/2}(q^{-m}\lambda_{2}^{-1})^{k}R(k,q)\\





&=
\frac{-(q;q)_{\infty}^{2}}{\theta(\lambda_{2},q)}(-1)^{m}q^{m(m+1)/2}
\lambda_{2}^{m}\sum_{k,\ell=0}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}}{(q;q)_{\ell}(q;q)_{k-\ell}}(q^{-m}\lambda_{2}^{-1})^{k}\\


&=
f^{(-1)}(q^{-m}\lambda_{2}^{-1},q) \,.
\end{aligned}
\ee
\end{proof}
\begin{lemma}
\label{lem.fglimits.inhom}
  For $t$ in some compact set where the functions are holomorphic, we have
\be
\begin{aligned}
\lim_{r\rightarrow\infty}\frac{g^{(0,2)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
\frac{1}{(q;q)_{\infty}^2} m_{1,3}(t^{-1},q)
&\qquad
\lim_{r\rightarrow\infty}\frac{f^{(0)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
0 \,.
  \end{aligned}
\ee
\end{lemma}

\begin{proof}
We have
\be
\begin{aligned}
&(-1)^{r}q^{r(r+1)/2}t^{r+1}g^{(0,2)}(q^{r}t,q)\\
&=
\sum_{k=-r}^{\infty}
\Bigg(\frac{1}{2}\left(\frac{1}{2}E_{1}(q)-r-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k+r}\frac{1+q^{j}}{1-q^{j}}\right)^{2}\\
&\qquad\qquad-\left(\frac{1}{2}E_{1}(q)-r-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k+r}\frac{1+q^{j}}{1-q^{j}}\right)
  \frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}\\
  &\qquad\qquad+\frac{1}{2}
  \frac{\theta''(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k+r}\frac{q^{j}}{(1-q^{j})^2}-\frac{1}{24}-\frac{1}{24}E_{2}(q)\Bigg)(-1)^{k}
\frac{q^{k(k+1)/2}}{(q;q)_{k+r}^{2}}t^{-k} \,.
\end{aligned}
\ee
Then noting that $1/24-E_2(q)/24-\sum_{j=1}^{k}q^j/(1-q^j)^2)=O(q^{k+1})$ the proof then proceeds as in Lemma~\ref{lem.fglimits}.
\end{proof}

To finish the proof of
Theorem~\ref{thm.41b} we will use the state integrals introduced in
~\cite[Eqn.(73)]{GGMW:trivial}.








\be\label{41inhom.sint}
\int_{\BR+i\ve}
\Phi_{\sfb}(x)^2
\frac{\exp\left(-\pi i x^{2}-2\pi\frac{zx}{\sfb}\right)}{1+\tq^{1/2}
  \exp\left(-\frac{2\pi x}{\sfb}\right)}dx\,.
\ee
The factorisation of this integral was done in \cite[Thm.7]{GGMW:trivial}. The
fact this module is not self dual (see Proposition~\ref{41inhom.not.sd}) means
that additional functions arise in the factorisation. It was shown, using
Equation~\eqref{S.mod.thd}, that Equation~\eqref{41inhom.sint} factors as an
elementary function holomorphic in $\BC'$ times
\be
\begin{aligned}
\calI(z,\tau)
=&
\tau^{2}g^{(0,2)}(\tilde{t},\tq)
+\tau g^{(0,1)}(\tilde{t},\tq)L_{0}(t,q)-g^{(0,0)}(\tilde{t},\tq)L_{1}(t,q)
\end{aligned}
\ee
where
\be
\label{41.stateint.fac.inhom}
\begin{aligned}
L_{0}(t,q)
&=
1-\frac{1}{2}E_{1}(q)+\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}
+\sum_{k=1}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}(1-q^{k})}t^{-k}\\
L_{1}(t,q)
&=
-\frac{5}{12}+\frac{1}{2}E_{1}-E_{1}(q)^{2}-\frac{1}{24}E_{2}(q)
-\left(\frac{1}{8}-\frac{1}{8}E_{1}(q)\right)\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}
-\frac{\theta''(t^{-1};q)}{2\theta(t^{-1};q)}\\
&\quad+\sum_{k=1}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}}{(q;q)_{k}^{2}(1-q^{k})}t^{-k}
\left(\frac{1}{2}E_{1}(q)-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}
  +\frac{q^{k}}{1-q^{k}}\right)\,.
\end{aligned}
\ee
These functions $L_{i}$ where then shown to satisfy
\be
\begin{aligned}
  L_{0}(t,q)-L_{0}(qt,q)&=-qtg^{(0,0)}(qt,q)\\
  L_{1}(t;q)-L_{1}(qt,q)&=-qtg^{(0,1)}(qt,q).
\end{aligned}
\ee
Notice that functions satisfying these equations are unique up to the
addition of an elliptic function. Therefore, with exactly the same argument in
~\cite[Thm.4]{GGMW:trivial} with the addition of checking the principal parts
of the LHS and RHS we can then show that
\be
{\small
V(t,q)^{-1}
\begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
q^{-2}t^{-1} & -q^{-2} & q^{-2}t^{-1}-2q^{-1}
\end{pmatrix}
=
\begin{pmatrix}
  -L_{1}(t,q) & -qt^2g^{(0,1)}(qt,q) & qt^2g^{(0,1)}(t,q)\\
  L_{0}(t,q)& qt^2g^{(0,0)}(qt,q) & -qt^2g^{(0,0)}(qt,q)\\
  1 & 0 & 0
\end{pmatrix}.
}
\ee

\noindent
Therefore, we see that the entries of $\Om_{V,S}$ are combinations of elementary
functions times $\calI(z+n+m\tau,\tau)$ for $m,n\in\{-2,-1,0,1,2\}$. Using the
explicit expressions for the monodromy one can prove it satisfies Equation
~\eqref{M41c} with equal weights $(2,1,0)$ and again using part (c) of Theorem
~\ref{thm.ST} complete the proof.
\end{proof}
