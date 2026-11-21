---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-015-32-self-duality
section_title: "Self duality"
section_number: 3.2
pages: 25-28
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 0.956
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
We will introduce a state integral in Section~\ref{subsec.heine.stateint} which
factorises as a finite sum of products of solutions of the module $M$ associated
to Equations~\eqref{heine.equs} and its dual $M^{\wedge}$ (see Section~\ref{sub.duality}
for the definitions of the two duals). To prove modularity we must factorise the state
integral as a finite sum of products of solutions of $M$ and $M^{\vee}$. To do
so, we need to give an explicit isomorphism between $M^{\vee}$ and $M^{\wedge}$.
This is the content of the following proposition, which after some change of
variables, is equivalent to Beukers--Jouhet~\cite[Thm.1.3]{Beukers:duality}.
For completeness, we will give an independent proof using the methods of our paper.

\begin{proposition}
  \label{prop.heine.selfdual}\cite[Thm.1.3]{Beukers:duality}
If $M$ is the module associated to Equations~\eqref{heine.equs} then
\be
\label{heine.selfdual.MV=MA}
  M^{\vee}\cong M^{\wedge} \,.
\ee
Explicitly, there exists $Q(t,a,b,q)\in GL_{r}(\BQ(t,a,b,q))$ such that
\be\label{heine.selfdual.Peq}
  Q(qt,a,b,q)A(qt,a,b,q^{-1})^{-1}
  =
  A(t,a,b,q)^{-T}Q(t,a,b,q)\,.
\ee
In addition, $Q$ satisfies 
\be
\label{heine.selfdual.Ueq}
  U(t,a,b,q)^{-T}
  =
  Q(t,a,b,q)
  U(t,a,b,q^{-1})
  \mathrm{diag}(1,-1,-1,\dots,-1)\,.
\ee
\end{proposition}

\begin{proof}
To prove Equation~\eqref{heine.selfdual.Peq} let
\be
\begin{tiny}
\begin{aligned}
  &(1-q^{-1}b_{1})\dots(1-q^{-1}b_{r-1})P(t,a,b,q)\\
  &=\begin{pmatrix}
    1-t & 0 & 0 & \dots & 0\\
    0 & -(e_{2}(b/q)-q^{-1}te_{2}(a)) & e_{3}(b/q)-q^{-2}te_{3}(a) & \dots
    & (-1)^{r-1}(e_{r}(b/q)-q^{-r+1}te_{r}(a))\\
    0 & (e_{3}(b/q)-q^{-1}te_{3}(a)) & -(e_{4}(b/q)-q^{-2}te_{4}(a)) & \dots & 0\\
    : & : & : & \dots & :\\
    0 & (-1)^{r-1}(e_{r}(b/q)-q^{-1}te_{r}(a)) & 0 & \dots & 0
  \end{pmatrix}\,.
\end{aligned}
\end{tiny}
\ee
Using the fact that $e_{k}(\lambda x)=\lambda^{k}e_{k}(x)$, one can then see that
\be
\begin{tiny}
\begin{aligned}
  &(1-q^{-1}b_{1})\dots(1-q^{-1}b_{r-1})P(qt,a,b,q)A(qt,q^{-1}a,q^{-2}b,q^{-1})^{-1}\\
  &=(1-q^{-1}b_{1})\dots(1-q^{-1}b_{r-1})A(t,a,b,q)^{-T}P(t,a,b,q)\\
  &=
  \begin{pmatrix}
    e_{1}(b/q)-te_{1}(a) & -(e_{2}(b/q)-q^{-1}te_{2}(a)) & \dots
    & (-1)^{r-1}(e_{r}(b/q)-q^{-r+1}te_{r}(a))\\
    -(e_{2}(b/q)-te_{2}(a)) & e_{3}(b/q)-q^{-1}te_{3}(a) & \dots & 0\\
    : & : & \dots & : \\
    (-1)^{r-1}(e_{r}(b/q)-te_{r}(a)) & 0 & \dots & 0\\
  \end{pmatrix}\,.
\end{aligned}
\end{tiny}
\ee
Now notice that the second and third Equations~\eqref{heine.equs} give gauge
equivalences between the modules in $t$ thinking of $a,b$ as constants when we
shift $a_{j}\mapsto qa_{j}$ and $b_{i}\mapsto qb_{i}$. Therefore, multiplying $P$
by these gauge equivalences gives the desired $Q$. Now to prove
Equation~\eqref{heine.selfdual.Ueq} we note that, from Equation
~\eqref{heine.selfdual.Peq}
\be
  E(t,a,b,q)
  :=
  U(t,q^{-1}a,q^{-2}b,q^{-1})^{-1}P(t,a,b,q)^{-1}U(t,a,b,q)^{-T}
\ee
is an elliptic function. However,
\be
  H(t,a,b,q)
  :=
  \mathrm{diag}\left(\frac{\theta(q^{-2}b_{i}t;q)}{\theta(q^{-1}t;q)}\right)^{-1}
  E(t,a,b,q)\,\,\,
  \mathrm{diag}\left(\frac{\theta(q^{-1}b_{i}t;q)}{\theta(t;q)}\right)
\ee
is holomorphic at $t=0$. Therefore, we see that
\be
H_{i,j}(t,a,b,q)=
-t\frac{\theta(q^{-1}b_{j-1}t;q)}{\theta(q^{-2}tb_{i-1};q)}E_{i,j}(t,a,b,q)
\ee
is holomorphic. This implies that if $i\neq j$ that $E_{i,j}(t,a,b,q)$ has at most
has simple poles at $q\in b_{j-1}^{-1}q^{\BZ}$ and must have zeros at
$t\in b_{i-1}^{-1}q^{\BZ}$ and there is no such non-zero elliptic function and
therefore $E_{i,j}(t,a,b,q)=0$. Then notice that
\be
  H_{ii}(t,a,b,q)
  =
  -t\frac{\theta(q^{-1}b_{i-1}t;q)}{\theta(q^{-2}tb_{i-1};q)}E_{i,i}(t,a,b,q)
  =
  qb_{i-1}^{-1}E_{i,i}(t,a,b,q)
\ee
is holomorphic at $t=0$ and so as $E_{i,i}(t,a,b,q)$ is also elliptic in $t$ it
is constant in $t$. Now notice that
\be
\begin{tiny}
\begin{aligned}
  &\lim_{t\rightarrow 0}U(t,q^{-1}a,q^{-2}b,q^{-1})
  \mathrm{diag}\left(\frac{\theta(q^{-2}b_{i}t;q)}{\theta(q^{-1}t;q)}\right)\\
  &=
  \begin{pmatrix}
    1 & 1 & \dots & 1\\
    1 & qb_{1}^{-1} & \dots & qb_{r-1}^{-1}\\
    : & : & \dots & :\\
    1 & (qb_{1}^{-1})^{r-1} & \dots & (qb_{r-1}^{-1})^{r-1}\\
  \end{pmatrix}
  \begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & B_{1}(q^{-1}a,q^{-2}b,q^{-1}) & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & B_{r-1}(q^{-1}a,q^{-2}b,q^{-1})\\
  \end{pmatrix}
\end{aligned}
\end{tiny}
\ee
and
\be
\begin{small}
\begin{aligned}
  &\lim_{t\rightarrow 0}\mathrm{diag}
  \left(\frac{\theta(q^{-1}b_{i}t;q)}{\theta(t;q)}\right)^{-1}U(t,a,b,q)^{T}\\
  &=
  \begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & B_{1}(a,b,q) & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & B_{r-1}(a,b,q)\\
  \end{pmatrix}
  \begin{pmatrix}
    1 & 1 & \dots & 1\\
    1 & qb_{1}^{-1} & \dots & (qb_{1}^{-1})^{r-1}\\
    : & : & \dots & :\\
    1 & qb_{r-1}^{-1} & \dots & (qb_{r-1}^{-1})^{r-1}\\
  \end{pmatrix}\,.
\end{aligned}
\end{small}
\ee
Then using the fact that
\be
  \sum_{j=0}^{r}(-1)^{j}e_{j}(b/q)\rho^{j}
  =
  (1-\rho)(1-q^{-1}b_{1}\rho)\dots(1-q^{-1}b_{r-1}\rho)
\ee
vanishes at $\rho\in\{qb_{i}^{-1}\}$ we can show the matrix
\be
\begin{aligned}
  \prod_{k=1}^{r}(1-q^{-1}b_{k})
  \begin{pmatrix}
    1 & 1 & \dots & 1\\
    1 & qb_{1}^{-1} & \dots & (qb_{1}^{-1})^{r-1}\\
    : & : & \dots & :\\
    1 & qb_{r-1}^{-1} & \dots & (qb_{r-1}^{-1})^{r-1}\\
  \end{pmatrix}
  P(t,a,b,q)
  \begin{pmatrix}
    1 & 1 & \dots & 1\\
    1 & qb_{1}^{-1} & \dots & qb_{r-1}^{-1}\\
    : & : & \dots & :\\
    1 & (qb_{1}^{-1})^{r-1} & \dots & (qb_{r-1}^{-1})^{r-1}\\
  \end{pmatrix}
\end{aligned}
\ee
has $(i+1,j+1)$-th entry
\be
\begin{aligned}
  &\sum_{k=0}^{r-1}(-1)^{j}e_{j}(b/q)(qb_{j}^{-1})^{k}
  \sum_{\ell=0}^{r-1-k}(b_{i}b_{j}^{-1})^{\ell}\\
  &=
  \delta_{i,j}(1-b_{0}/b_{j})\dots(1-b_{j-1}/b_{j})(1-b_{j+1}/b_{j})
  \dots(1-b_{r-1}/b_{j})\
\end{aligned}
\ee
where we have used the fact that
\be
\begin{small}
\begin{aligned}
    &\sum_{k=0}^{r-1}(-1)^{j}e_{j}(b/q)x^{k}\sum_{\ell=0}^{r-1-k}(xy^{-1})^{\ell}
    =
    \sum_{k=0}^{r-1}(-1)^{j}e_{j}(b/q)x^{k}\frac{1-(xy^{-1})^{r-k}}{1-xy^{-1}}\\
    &=
    \frac{1}{1-xy^{-1}}\left((1-x)(1-q^{-1}b_{1}x)
 \dots(1-q^{-1}b_{2}x)-x^{r}y^{-r}(1-y)(1-q^{-1}b_{1}y)\dots(1-q^{-1}b_{2}y)\right)\,.
\end{aligned}
\end{small}
\ee
Therefore, with the convention that $(x;q^{-1})_{\infty}=(qx;q)_{\infty}^{-1}$ and
$(q^{-1};q^{-1})_{\infty}=(q;q)_{\infty}^{-1}$ when $|q|<1$, for $j>0$
\be
\begin{aligned}
  &B_{j}(a,b,q)B_{j}(q^{-1}a,q^{-2}b,q^{-1})\\
  &=-q^{-1}b_{j}\frac{(1-q^{-1}b_{1})\dots(1-q^{-1}b_{r-1})}{(1-q/b_{j})(1-b_{1}/b_{j})
    \dots(1-b_{j-1}/b_{j})(1-b_{j+1}/b_{j})\dots(1-b_{r-1}/b_{j})}
\end{aligned}
\ee
and we see that
\be
\begin{aligned}
  &\begin{pmatrix}
    E_{1,1}(t,a,b,q) & 0 & 0 & \dots & 0\\
    0 & qb_{1}^{-1}E_{2,2}(t,a,b,q) & 0 & \dots & 0\\
    : & : & : & \dots & :\\
    0 & 0 & 0 & \dots & qb_{r-1}^{-1}E_{r,r}(t,a,b,q)
  \end{pmatrix}\\
  &=
  \lim_{t\rightarrow 0}H(t,a,b,q)
  =
  \begin{pmatrix}
    1 & 0 & 0 & \dots & 0\\
    0 & -qb_{1}^{-1} & 0 & \dots & 0\\
    : & : & : & \dots & :\\
    0 & 0 & 0 & \dots & -qb_{r-1}^{-1}
  \end{pmatrix}
\end{aligned}
\ee
Therefore, again using the gauge equivalence in the second and third Equations
~\eqref{heine.equs} complete the proof.
\end{proof}

\begin{remark}
  \label{rem.r=2}
When $r=2$, Proposition~\ref{prop.heine.selfdual} is equivalent to the identity
~\cite[Eqn.(1.4.3)]{Gasper}
\be
  {}_{2}\phi_{1}(a,b;c;q,t)
  =
  \frac{(abc^{-1}t;q)_{\infty}}{(t;q)_{\infty}}
  {}_{2}\phi_{1}(ca^{-1},cb^{-1};c^{-1};q,abc^{-1}t)
\ee
where we note that the ratio of Pochhammers is related to the determinant of $U$.
This is the $q$-analogue of Euler's transformation formula for ${}_2F_{1}$
~\cite[Eqn.(1.4.2)]{Gasper}
\be
  {}_{2}F_{1}(a,b;c;t)=(1-t)^{c-a-b}{}_{2}F_{1}(c-a,c-b;c;t)
\ee
where
\be
{}_{r}F_{r-1}(a;b;t) =
\sum_{k=0}^{\infty}
\frac{(a_{1})_{k}\dots(a_{r})_{k}}{(b_{1})_{k}\dots(b_{r-1})_{k}}\frac{t^{k}}{k!} \,.
\ee
\end{remark}

\begin{remark}
\label{rem.q=1}
The $q\rightarrow 1$ limit of Proposition~\ref{prop.heine.selfdual} is discussed
in full generality in \cite[Thm.1.1]{Beukers:duality}, where it is shown that the
dual of the module associated to ${}_{r}F_{r-1}(a;b;t)$ is the module associated to
${}_{r}F_{r-1}(1-a;2-b;t)$.
\end{remark}
