---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-023-52-monodromy
section_title: "Monodromy"
section_number: 5.2
pages: 40-42
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.862
latex_coverage_ratio: 0.942
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
Consider the fundamental matrices $U$ and $V$ given by Equations~\eqref{UVex41}
and the associated monodromy. Using the modular transformation properties of
the Jacobi $\theta$-function Equation~\eqref{thetaS} and the Dedekind $\eta$-function,
it is easy to see that Equation~\eqref{M412} implies~\eqref{M41c}.

Note that each of the functions $\vM_{2,1},\vM_{2,1}|_{-1}T,\vM_{2,1}|_{-1}S$ has
$\SL_2(\BZ)$-stabiliser $\langle T^2,TST\rangle$, $\langle T^2,S\rangle$ and
$\langle ST^2S,T\rangle$, respectively, and that the second group is the
$\theta$-subgroup and the last group is $\Gamma_{0}(2)$. The appearance of
$\Gamma_{0}(2)$ is a consequence of the $(1/2)$-$q$-Borel transform below. 

The rest of this section is devoted to the proof that the monodromy is given
by Equation~\eqref{M412}. To achieve this, we need to write $f^{(-1)}$ and $f^{(1)}$
as linear combinations of $g^{(0,0)}$ and $g^{(0,1)}$, the coefficients in these
expressions give the entries of the monodromy matrix. 

Firstly we determine the second column of the monodromy, using an adaption of an
argument in~\cite{Morita:conn-mon}. Using the $(-1)$-$q$-Laplace transform or the
Meinardus trick (see for example~\cite{Meinardus} and~\cite[p.54]{Zagier:dilog})
and shifting the contour of $\oint:=\int_{|t|=\ve}$ we obtain that
\be
\begin{tiny}
\begin{aligned}
  \label{f1=g01}
&\hat{f}^{(-1)}(t,q)
=
(q;q)_{\infty}^{2}\oint_{0}\frac{\theta(t/\xi;q)}{(\xi;q)_{\infty}^{2}}
\frac{d\xi}{2\pi i \xi}
=
-(q;q)_{\infty}^{2}\sum_{k=0}^{\infty}\left(\Res_{\xi=q^{-k}}\right)
\frac{\theta(t/\xi;q)}{(\xi;q)_{\infty}^{2}}\frac{d\xi}{2\pi i \xi}\\
&=
-(q;q)_{\infty}^{2}\sum_{k=0}^{\infty}\left(\Res_{\ve=0}\right)
\frac{\theta(tq^{k}e^{\ve};q)}{(q^{-1}e^{-\ve};q^{-1})_{k}^2
  (e^{-\ve};q)_{\infty}^{2}}\frac{-d\ve}{2\pi i }\\
&=
-(q;q)^{4}\sum_{k=0}^{\infty}\left(\Res_{\ve=0}\right)
\frac{(-1)^{k}q^{-k(k+1)/2}t^{-k}e^{-k\ve}
  \theta(te^{\ve};q)}{\theta(e^{\ve};q)^{2}}
\frac{(qe^{\ve};q)_{\infty}^{2}}{q^{-k(k+1)}
  e^{-2k\ve}(qe^{\ve};q)_{k}^2}\frac{-d\ve}{2\pi i }\\
&=
(q;q)_{\infty}^{6}\Res_{\ve=0}
\frac{\theta(te^{\ve};q)}{\theta(e^{\ve};q)^{2}}
\frac{(qe^{\ve};q)_{\infty}^{2}}{(q;q)_{\infty}^{2}}
\sum_{k=0}^{\infty}
\frac{(-1)^{k}q^{k(k+1)/2}t^{-k}e^{k\ve}}{(qe^{\ve};q)_{k}^2}
\frac{d\ve}{2\pi i }\\
&=
-\theta(t^{-1};q)\sum_{k=0}^{\infty}\left(\frac{1}{2}E_{1}(q)-\frac{1}{2}+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}\right)
\frac{(-1)^{k}q^{k(k+1)/2}t^{-k-1}}{(q;q)_{k}^2}+\theta'(t^{-1};q)
\sum_{k=0}^{\infty}\frac{(-1)^{k}q^{k(k+1)/2}t^{-k-1}}{(q;q)_{k}^2}.
\end{aligned}
\end{tiny}
\ee
Therefore, we see that
\be\label{fg}
f^{(-1)}(t,q)
=
g^{(0,1)}(t,q) \,, 
\ee
which implies that $\vM_{1,2}=0$ and $\vM_{2,2}=1$. Lemma~\ref{lem.41det} below
implies that $\det(M)=-1$, therefore 
\be
\label{41:paritalmono}
\vM(t,\lambda,q) =
\begin{pmatrix}
-1 & 0\\
* & 1
\end{pmatrix} \,.
\ee
To finish the proof we will show that the function
\be
\label{41mono:intfunc}
\calE_2:=f^{(1)}+g^{(0,0)}-m_{2,1}g^{(0,1)}
\ee
vanishes identically, where $m_{2,1}$ denotes the function given in
Equation~\eqref{M412}. The function $\calE_2$ is meromorphic of
$t \in \BC^{\times}$ and has potential simple poles located at
$t\in\pm q^{-1/4-\frac{1}{2}\BZ}\lambda^{-1}$ (coming from $f^{(1)}$ and $\vM_{2,1}$)
and potential simple poles at $q^\BZ$ (coming from $g^{(0,1)}$).
Lemma~\ref{lem.resf1} below gives
\be
\label{41res}
\begin{aligned}
&\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}f^{(1)}(t,\lambda,q)\frac{dt}{2\pi it}\\
&=
\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)
  \theta(\pm q^{-3/4}\lambda;q)}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}
f^{(-1)}(\pm q^{-1/4-n} \lambda^{-1},q) \,.
\end{aligned}
\ee
On the other hand,
\be
\begin{aligned}
  &\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}m_{2,1}(t,\lambda,q)
  \frac{dt}{2\pi it}\\
&=
\frac{\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}\theta(qt;q)\theta(t\lambda;q)
  \theta(t\lambda q^{-1/2};q)
  \theta(t\lambda^{2}q^{-1/2};q)}{\theta(t\lambda q^{1/4};q)
  \theta(-t\lambda q^{1/4};q)\theta(t\lambda q^{-1/4};q)
  \theta(-t\lambda q^{-1/4};q)\theta(q^{-1}\lambda;q)\theta(q^{-3/2}
  \lambda;q)}\frac{dt}{2\pi it}\\
&=
\frac{(-1)^{n}q^{n(n-1)/2}}{(q;q)_{\infty}^{3}}\frac{\theta(\pm q^{3/4-n}
  \lambda^{-1};q)\theta(\pm q^{-1/4-n};q)\theta(\pm q^{-3/4-n};q)
  \theta(\pm q^{-3/4-n}\lambda;q)}{
  \theta(-q^{-n};q)\theta(q^{-1/2-n};q)
  \theta(-q^{-1/2-n};q)\theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}\\
&=
\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)
  \theta(\pm q^{-3/4}\lambda;q)}{(q;q)_{\infty}^{3}
  \theta(-1;q)\theta(q^{-1/2};q)
  \theta(-q^{-1/2};q)\theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}\\
&=
\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)
  \theta(\pm q^{-3/4}\lambda;q)}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)} \,.
\end{aligned}
\ee
Therefore,
\be
\Res_{t=\pm q^{-1/4-n}\lambda^{-1}} \calE_2(t,\lambda,q) \frac{dt}{2\pi it}=0 \,.
\ee
A similar computation or the fact everything is elliptic in
$\lambda\mapsto q^{1/2}\lambda$ also shows that
\be
\Res_{t=\pm q^{-3/4-n}\lambda^{-1}} \calE_2(t,\lambda,q) \frac{dt}{2\pi it}=0 \,.
\ee
Now notice that $m_{2,1}(q^{\BZ},\lambda,q)=0$ which implies $m_{2,1}g^{(0,1)}$
is holomorphic at $t\in q^{\BZ}$. We then see that $\calE_2(t,\lambda,q)$ extends
to a holomorphic function of $t \in \BC^{\times}$. Therefore, from
Corollary~\ref{cor:41holsol} we see that $\calE_2(t,\lambda,q)=C(q)g^{(0,0)}(t,q)$.
Finally, we note that 
\be
\frac{-C(q)}{(q;q)_{\infty}^{2}}
=
\lim_{r\rightarrow\infty}\frac{\calE_{2}(q^{r}t,\lambda,q)}{\theta(q^{r}t;q)}
=
0
\ee
which follows from Lemma~\ref{lem.fglimits}.
Thus, Equation~\eqref{M412} follows from the residue equation~\eqref{41res}
and from a computation of the determinants of $U$ and $V$. We discuss these
in the next sections.

\begin{lemma}
\label{lem.fglimits}
  For $t$ in some compact set where the functions are holomorphic, we have
\be
\begin{aligned}
\lim_{r\rightarrow\infty}\frac{g^{(0,0)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
\frac{-1}{(q;q)_{\infty}^{2}}\qquad
&
\lim_{r\rightarrow\infty}\frac{f^{(-1)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
0
\\
\lim_{r\rightarrow\infty}\frac{g^{(0,1)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
0\qquad
&
\lim_{r\rightarrow\infty}\frac{f^{(1)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
\frac{1}{(q;q)_{\infty}^{2}}\,.
  \end{aligned}
\ee
\end{lemma}

\begin{proof}
We have
\be
\begin{aligned}
g^{(0,0)}(q^{r}t,q)
&=
\sum_{k=0}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2-rk-r}}{(q;q)_{k}^{2}}t^{-k-1}\\
&=
q^{-r(r+1)/2}\sum_{k=0}^{\infty}(-1)^{k}
\frac{q^{(k-r)(k-r+1)/2}}{(q;q)_{k}^{2}}t^{-k-1}\\
&=
(-1)^{r}q^{-r(r+1)/2}t^{-r-1}\sum_{k=-r}^{\infty}(-1)^{k}
\frac{q^{k(k+1)/2}}{(q;q)_{k+r}^{2}}t^{-k}\,.
\end{aligned}
\ee
The first equality then follows from
\begin{align*}
\lim_{r\rightarrow\infty}\frac{g^{(0,0)}(q^{r}t,q)}{\theta(q^{r}t;q)}
&=
\lim_{r\rightarrow\infty}\frac{-1}{\theta(t^{-1};q)}
\sum_{k=-r}^{\infty}(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k+r}^{2}}t^{-k}
\\
&=
\frac{-1}{\theta(t^{-1};q)}\sum_{k\in\BZ}(-1)^{k}
\frac{q^{k(k+1)/2}}{(q;q)_{\infty}^{2}}t^{-k}
=\frac{-1}{(q;q)_{\infty}^{2}} \,.
\end{align*}
We can show similarly that
\be
\begin{tiny}
\begin{aligned}
g^{(0,1)}(q^{r}t,q)
&=
(-1)^{r}q^{-r(r+1)/2}t^{-r-1}\sum_{k=-r}^{\infty}\left(\frac{1}{2}E_{1}(q)-r-\frac{1}{2}-\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}+\sum_{j=1}^{k+r}\frac{1+q^{j}}{1-q^{j}}\right)
(-1)^{k}\frac{q^{k(k+1)/2}}{(q;q)_{k+r}^{2}}t^{-k} \,.
\end{aligned}
\end{tiny}
\ee
Noting that $E_{1}(q)/2-1/2+\sum_{j=1}^{k}\frac{1+q^{j}}{1-q^{j}}=k+O(q^{k})$ completes the proof of the limits of
$g^{(0,0)},g^{(0,1)}$. The limits of $f^{(\pm1)}$ follow from Watson's lemma for
$q$-Borel resummation and keeping track of the $\theta$ prefactors.
\end{proof}
