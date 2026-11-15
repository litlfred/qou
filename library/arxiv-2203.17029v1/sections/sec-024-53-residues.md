---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-024-53-residues
section_title: "Residues"
section_number: 5.3
pages: 42-44
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.84
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
Note that $g^{(0,0)}$ is holomorphic on $\BC^{\times}\cup\{\infty\}$. In this
subsection we compute the residues of the meromorphic functions $f^{(-1)}=g^{(0,1)}$
and $f^{(1)}$.

\begin{lemma}
  \label{lem.resg01}
  The functions $f^{(-1)}(t,q)=g^{(0,1)}(t,q)$ have simple poles at $t = q^\BZ$ with
  residues
\be
\Res_{t=q^{n}}f^{(-1)}(t,q)\frac{dt}{2\pi i t}
=
\Res_{t=q^{n}}g^{(0,1)}(t,q)\frac{dt}{2\pi i t}
=
g^{(0,0)}(q^{n},q)\,.
\ee
\end{lemma}

\begin{proof}
We have
\be
\Res_{t=q^{k}}\frac{\theta'(t^{-1};q)}{\theta(t^{-1};q)}\frac{dt}{2\pi it}
=
-1 \,.
\ee
To finish we note that the proof of the equality $f^{(-1)}=g^{(0,1)}$ is
independent of this Lemma and follows from Equation~\eqref{f1=g01}.
\end{proof}

\begin{lemma}
  \label{lem.resf1}
  \rm{(a)} The function $\Bor_{1/2}\hat{f}^{(1)}(\xi,q)$ has simple poles at
$\xi=\pm q^{-1/4-\BZ/2}$ with residue
\be
\begin{aligned}
\Res_{\xi=\pm q^{-1/4-n/2}}\Bor_{1/2}\hat{f}^{(1)}(\xi,q)\frac{d\xi}{2\pi i\xi}
&=
\frac{-\theta(\pm q^{-1/4};q^{1/2})}{2(q;q)_{\infty}^{2}}
\sum_{\ell=0}^{k}(\pm1)^{k}\frac{q^{\frac{k(k+2)}{4}}}{(q;q)_{\ell}(q;q)_{k-\ell}}.
\end{aligned}
\ee
  \rm{(b)}
  The function $f^{(1)}(t,\lambda,q)$ has simple poles at
  $t=\pm q^{-1/4+\BZ}\lambda^{-1}$ with residue
  \be
\begin{aligned}
&\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}f^{(1)}(t,\lambda,q)\frac{dt}{2\pi it}\\
&=
\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q) \theta(\pm q^{-3/4}\lambda;q)}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}
f^{(-1)}(\pm q^{-1/4-n} \lambda^{-1},q) \,.
\end{aligned}
\ee
\end{lemma}

\begin{proof}
For part (a), consider the following auxiliary function,
\be
\label{aux.fun.H}
H_{r}(\xi,q)=\sum_{k}\frac{\xi^{2k}}{(q;q)_{k}(q;q)_{k+r}},
\ee
which we analytically continue to $\xi\notin\pm q^{\frac{1}{2}\BZ_{\leq0}}$.
From the power series at $\xi=0$, we see that
\be
\Bor_{1/2}\hat{f}^{(1)}(q^{-1/4}\xi,q)
=
\sum_{r\in\BZ}(-1)^{r}q^{r^{2}/4}\xi^{r}H_{r}(\xi,q).
\ee
We have the relation
\be
H_{r-1}(\xi,q)-\xi H_{r}(\xi,q)
=
-q^{1-r}\left(H_{r-2}(\xi,q)-H_{r-1}(\xi,q)\right)
\ee
and from this we can see that
\be
\Res_{\xi=1}\left(H_{r-1}(\xi,q)-H_{r}(\xi,q)\right)\frac{d\xi}{2\pi i\xi}
=
(-1)^{r}q^{-r(r-1)/2}\Res_{\xi=1}\left(H_{-1}(\xi,q)-H_{0}(\xi,q)\right)
\frac{d\xi}{2\pi i\xi}.
\ee
Since
\be
\lim_{r\rightarrow\infty}H_{r}(\xi,q)
=
\frac{1}{(q;q)_{\infty}(\xi^{2};q)_{\infty}},
\ee
it follows that 
\be
\label{res.aux.fun.H}
\Res_{\xi=1}H_{r}(\xi,q)\frac{d\xi}{2\pi i\xi}
=
\Res_{\xi=1}H_{0}(\xi,q)\frac{d\xi}{2\pi i\xi}
=
\Res_{\xi=1}H_{\infty}(\xi,q)\frac{d\xi}{2\pi i\xi}
=
\frac{-1}{2(q;q)_{\infty}^{2}}.
\ee
Let
\be
R_{\pm}(n,q)=\Res_{\xi=\pm q^{-1/4-n/2}}
\Bor_{1/2}\hat{f}^{(1)}(\xi,q)\frac{d\xi}{2\pi i\xi} \,.
\ee
Then,
\be
\begin{aligned}
R(0,q)
&=
\Res_{\xi=\pm 1}\sum_{r\in\BZ}(-1)^{r}q^{r^{2}/4}\xi^{r}H_{r}(\xi,q)
\frac{d\xi}{2\pi i\xi}
&=
\frac{-\theta(\pm q^{-1/4};q^{1/2})}{2(q;q)_{\infty}^{2}} \,.
\end{aligned}
\ee
Now from the functional equation of $\Bor_{1/2}\hat{f}^{(1)}(\xi,q)$,
we deduce that
\be
\begin{aligned}
0
&=
\Res_{\xi=\pm q^{-1/4-n/2}}(1-q^{1/2}\xi^2)\Bor_{1/2}\hat{f}^{(1)}(\xi,q)+
2\xi\Bor_{1/2}\hat{f}^{(1)}(q^{1/2}\xi,q)-\Bor_{1/2}\hat{f}^{(1)}(q\xi,q)
\frac{d\xi}{2\pi i\xi}\\
&=
(1-q^{-n})R_{\pm}(n,q)\pm2q^{-1/4-(n-1)/2}R_{\pm}(n-1,q)-R_{\pm}(n-2,q).
\end{aligned}
\ee
Note that $R_{\pm}(n,q)=0$ for $n<0$ and that when $R_{\pm}(-1,q)$ is zero we have
a unique solution determined by $R_{\pm}(0,q)$. One can then check that
\be\label{Rpm}
R_{\pm}(n,q)
=
\frac{-\theta(\pm q^{-1/4};q^{1/2})}{2(q;q)_{\infty}^{2}}
\sum_{\ell=0}^{n}(\pm1)^{n}\frac{q^{\frac{n(n+2)}{4}}}{(q;q)_{\ell}(q;q)_{n-\ell}} \,.
\ee
For part (b), we compute  
\be
\begin{small}
\begin{aligned}
&\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}f^{(1)}(t,\lambda,q)\frac{dt}{2\pi it}\\
&=
\Res_{t=\pm q^{-1/4-n}\lambda^{-1}}\frac{\theta(t;q)}{(q;q)_{\infty}^{2}}
\Lap_{1/2}\Bor_{1/2}\hat{f}^{(1)}(t,q)\frac{dt}{2\pi it}\\
&=
\frac{\theta(\pm q^{-1/4-n}\lambda^{-1};q)}{(q;q)_{\infty}^{2}
  \theta(\lambda;q^{1/2})}
\sum_{k\in\BZ}(-1)^{k}q^{(k-2n)(k-2n-1)/4}\lambda^{-k+2n}R_{\pm}(k,q)\\
&=
\frac{\theta(\pm q^{-1/4-n}\lambda^{-1};q)}{(q;q)_{\infty}^{2}
  \theta(\lambda;q^{1/2})}\frac{-\theta(\pm q^{-1/4};q^{1/2})}{2(q;q)_{\infty}^{2}}
q^{n(2n+1)/2}\lambda^{2n}
\sum_{k=0}^{\infty}\sum_{\ell=0}^{k}(-1)^{k}\frac{
  q^{\frac{k(k+1)}{2}}}{(q;q)_{\ell}(q;q)_{k-\ell}}(\pm q^{-1/4-n}
\lambda^{-1})^{k}\\
&=
-\frac{\theta(\pm q^{-1/4-n}\lambda^{-1};q)\theta(\pm q^{-1/4};q^{1/2})}{
  2(q;q)_{\infty}^{4}\theta(\lambda;q^{1/2})}q^{n(2n+1)/2}\lambda^{2n}
\hat{f}^{(-1)}(\pm q^{-1/4-n/2}\lambda^{-1},q)\\
&=
-\frac{\theta(\pm q^{-1/4-n}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)\theta(\pm q^{-5/4-n}\lambda^{-1};q)}{2(q;q)_{\infty}^{6}
  \theta(\lambda;q)\theta(q^{-1/2}\lambda;q)q^{-n(2n+1)/2}\lambda^{-2n}}
f^{(-1)}(\pm q^{-1/4-n}\lambda^{-1},q)\\
&=
-\frac{\theta(\pm q^{-1/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)
  \theta(\pm q^{-3/4};q)\theta(\pm q^{-5/4}\lambda^{-1};q)}{2(q;q)_{\infty}^{6}
  \theta(\lambda;q)\theta(q^{-1/2}\lambda;q)}
f^{(-1)}(\pm q^{-1/4-n}\lambda^{-1},q)\\
&=
\frac{\theta(\pm q^{3/4}\lambda^{-1};q)\theta(\pm q^{-1/4};q)\theta(\pm q^{-3/4};q)
  \theta(\pm q^{-3/4}\lambda;q)}{2(q;q)_{\infty}^{6}
  \theta(q^{-1}\lambda;q)\theta(q^{-3/2}\lambda;q)}
f^{(-1)}(\pm q^{-1/4-n} \lambda^{-1},q) \,.
\end{aligned}
\end{small}
\ee
\end{proof}
