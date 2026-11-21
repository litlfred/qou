---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-029-103-generalized-t-system-on-determinantial-modul
section_title: "Generalized T-system on determinantial module"
section_number: 10.3
pages: 81-84
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.857
latex_coverage_ratio: 0.885
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\begin{theorem} \label{thm: canonical surjection}
Let $\lambda \in \wl^+$ and $\mu_1,\mu_2,\mu_3 \in W \lambda$ such that $\mu_1 \preceq \mu_2 \preceq \mu_3$. Then there exists a canonical epimorphism
$$ \M(\mu_1,\mu_2) \conv \M(\mu_2,\mu_3) \twoheadrightarrow \M(\mu_1,\mu_3),$$
which is equivalent to saying that $\M(\mu_1,\mu_2) \hconv \M(\mu_2,\mu_3) \simeq \M(\mu_1,\mu_3)$.

In particular, we have
$$\tLa(\M(\mu_1,\mu_2),\M(\mu_2,\mu_3))=0\quad\text{and}\quad
\La(\M(\mu_1,\mu_2),\M(\mu_2,\mu_3)) = -(\mu_1-\mu_2,\mu_2-\mu_3). $$
\end{theorem}

\begin{proof}
(a)\ Our assertion follows from Theorem \ref{thm: DDD} and Theorem \ref{th:head}

 when $\mu_3=\lambda$.

\medskip\noi
(b) We shall prove the general case by induction on $|\la-\mu_3|$.
By (a), we may assume that $\mu_3 \ne \lambda$. Then there exists $i$ such that $\lan h_i,\mu_3\ra <0$. The induction hypothesis  yields that
$$\M(\mu_1,\mu_2) \hconv \M(\mu_2,s_i \mu_3) \simeq \M(\mu_1,s_i \mu_3).$$
Since $\mu_1\preceq\mu_2\preceq\mu_3\preceq s_i\mu_3$,
Proposition~\ref{prop: weyl left right} (iv)  gives
$$\eps_i^*\bl\M(\mu_2,s_i\mu_3)\br=\eps_i^*\bl\M(\mu_1,s_i\mu_3)\br
=-\lan h_i,\mu_3\ran.$$

Then Proposition~\ref{prop: acted on left only} implies that
$$\tEs_i{}^\max\bl \M(\mu_1,\mu_2)\hconv \M(\mu_2,s_i\mu_3)\br
\simeq
\M(\mu_1,\mu_2)\hconv\bl \tEs_i{}^\max \M(\mu_2,s_i\mu_3)\br,$$
from which we obtain
$$\M(\mu_1,\mu_3)\simeq \M(\mu_1,\mu_2)\hconv  \M(\mu_2,\mu_3)$$

\medskip\noi
By  Lemma \ref{lem:selfdual},  we have
$\tLa\bl\M(\mu_1,\mu_2),\M(\mu_2,\mu_3)\br=0$. Hence we  obtain
\begin{align*}
&\La\bl\M(\mu_1,\mu_2),\M(\mu_2,\mu_3)\br
=-\bl\wt(\M(\mu_1,\mu_2),\wt(\M(\mu_2,\mu_3))\br.
\qedhere
\end{align*}
\end{proof}


\begin{prop}\label{prop:dMM}
Let $i \in I$ and $x,y,z \in W$.
\begin{enumerate}
\item[{\rm (i)}] If $\ell(xy)=\ell(x)+\ell(y)$, $zs_i>z$,
$xy\ge zs_i$
and $x \ge z$, then we have
$$ \de(\M(xy\varpi_i,zs_i\varpi_i),\M(x\varpi_i,z\varpi_i)) \le 1.$$
\item[{\rm (ii)}] If $\ell(zy)=\ell(z)+\ell(y)$, $xs_i >  x$, $xs_i\ge zy$ and $x \ge z$, then we have
$$ \de(\M(xs_i\varpi_i,zy\varpi_i),\M(x\varpi_i,z\varpi_i)) \le 1.$$
\end{enumerate}
\end{prop}

\begin{proof}
In the course of proof, we omit $\oi_{\vpi,\vpi}^{-1}$ for the sake of simplicity.
If $y\vpi = \vpi$, then the assertion follows from Proposition \ref{prop: commute 1} (i). Hence we may assume that
 $y' \seteq ys_i < y$.

\medskip

Let us show {\rm (i)}. By Proposition \ref{prop: g T-system D}, we have
\begin{equation} \label{eq: ac le 1}
\begin{aligned}
\Delta(y\vpi,s_i\vpi)\Delta(\vpi,\vpi) & =q^{-1}G^\up\left( (u_{y\vpi} \otimes u_{\vpi}) \otimes (u_{s_i\vpi} \otimes u_{\vpi})^\ri \right) \\
& \hspace{10ex} +G^\up(\oi_\lambda^{-1}(\te_i^*b) \otimes u_\lambda^\ri),
\end{aligned}
\end{equation}
where $\lambda=\vpi+s_i\vpi$ and $b=\oi_\vpi(u_{y\vpi}) \in B(\infty)$.
Let  $S_{z,\la}^* $  be the operator on $\Ag$ given by
the application of $e_{j_1}^{(a_1)}\cdots e_{j_t}^{(a_t)}$ from the right,
where $z=s_{j_t}\cdots s_{j_1}$ is a reduced expression of $z$ and
$a_k=\lan h_{j_k},s_{j_{k-1}}\cdots s_{j_1}\la\ran$.
Then applying  $S_{z,\la}^*$   to \eqref{eq: ac le 1}, we obtain
\begin{align*}
\Delta(y\vpi,zs_i\vpi)\Delta(\vpi,z\vpi) &  =q^{-1}G^\up\left( (u_{y\vpi} \otimes u_{\vpi} ) \otimes (u_{zs_i\vpi} \otimes u_{z\vpi})^\ri \right) \\
& \hspace{10ex} +G^\up(\oi_\lambda^{-1}(\te_i^*b) \otimes u_{z\lambda}^\ri).
\end{align*}


Recall that $\mu\in\Po$ is called {\em $x$-dominant}
if $c_k\ge0$.
Here $x=s_{i_r} \cdots s_{i_1}$ is a reduced expression of $x$ and
 $c_k\seteq \lan h_{i_k}, s_{i_{k-1}} \cdots s_{i_1} \mu \ra$ ($1\le k\le r$).
Recall that an element $v\in\Ag$ with $\wtl(v)=\mu$ is called
{\em $x$-highest}
if $\mu$ is $x$-dominant and
$$\text{$f_{i_k}^{1+c_k}f_{i_{k-1}}^{(c_{k-1})}\cdots f_{i_1}^{(c_{1})}v=0$ for any $k$
($1\le k\le r$).}$$
If $v$ is $x$-highest, then
$v$ is a linear combination of
$x$-highest $G^\up(b)$'s.
Moreover, $S_{x,\mu}G^\up(b)\seteq f^{(c_r)}_{i_r}\cdots f^{(c_1)}_{i_1} G^\up(b)$ is either a member of the upper global basis or zero.
Since $\Delta(y\vpi,zs_i\vpi)\Delta(\vpi,z\vpi)$ is $x$-highest
of weight $\mu\seteq  y\vpi+\vpi$,
we obtain
\begin{align*}
\Delta(xy\vpi,zs_i\vpi)\Delta(x\vpi,z\vpi) & =q^{-1}G^\up\left( (u_{xy\vpi} \otimes u_{x\vpi} ) \otimes (u_{zs_i\vpi} \otimes u_{z\vpi})^\ri \right) \\
& \hspace{10ex} +S_{x,\mu}G^\up(\oi_\lambda^{-1}(\te_i^*b) \otimes u_{z\lambda}^\ri).
\end{align*}

Applying $p_\n$, we obtain
\begin{align*}
q^c \D(xy\vpi,zs_i\vpi)\D(x\vpi,z\vpi) & =q^{-1}p_\n G^\up\left( (u_{xy\vpi} \otimes u_{x\vpi} ) \otimes (u_{zs_i\vpi} \otimes u_{z\vpi})^\ri \right) \\
& \hspace{10ex} +p_\n S_{x,\mu}G^\up(\oi_\lambda^{-1}(\te_i^*b) \otimes u_{z\lambda}^\ri)
\end{align*}
for some integer $c$. Hence we obtain {\rm (i)} by
Lemma~\ref{lem:short} (i).

\medskip\noi
{\rm (ii)} is proved similarly. By applying $\varphi^*$  to \eqref{eq: ac le 1}, we obtain
\begin{align*}
q^{(s_i\vpi_i,\vpi_i)-(y\vpi_i,\vpi_i)}\Delta(s_i\vpi,y\vpi)\Delta(\vpi,\vpi) & =q^{-1}G^\up\left( (u_{s_i\vpi} \otimes u_{\vpi}) \otimes (u_{y\vpi} \otimes u_{\vpi})^\ri \right) \\
& \hspace{10ex} +G^\up(u_\lambda  \otimes (\oi_\lambda^{-1}\te_i^*b)^\ri).
\end{align*}
 Here we used Proposition~\ref{prop:phimul}.
Then the similar arguments as above show {\rm (ii)}.
\end{proof}

\begin{prop}\label{prop:deMM}
Let $x \in W$ such that $xs_i > x$ and $x \vpi \ne \vpi$. Then we have
$$\de(\M(xs_i\vpi,x\vpi),\M(x\vpi,\vpi)) =1.$$
\end{prop}

\begin{proof}
 By Proposition~\ref{prop:dMM} (ii),
 we have $\de(\M(xs_i\vpi,x\vpi),\M(x\vpi,\vpi)) \le1$.
Assuming $\de(\M(xs_i\vpi,x\vpi),\M(x\vpi,\vpi))=0$, let us derive a contradiction.

By Theorem~\ref{thm: canonical surjection} and the assumption, we have
$$\M(xs_i\vpi,x\vpi) \conv \M(x\vpi,\vpi) \simeq \M(xs_i\vpi,\vpi).$$
Hence we have
$$ \ve_j^*(\M(xs_i\vpi,\vpi))= \ve_j^*(\M(xs_i\vpi,x\vpi))+\ve_j^*(\M(x\vpi,\vpi))$$
for any $j \in I$. Since $xs_i\vpi \preceq x\vpi \preceq s_i\vpi$, Proposition \ref{prop: weyl left right} implies that
$$ \ve_j^*(\M(xs_i\vpi,\vpi))=\ve_j^*(\M(x\vpi,\vpi))=\lan h_j,\vpi \ra.$$
It implies that
$$\ve_j^*(\M(xs_i\vpi,x\vpi))=0 \quad \text{ for any } j \in I.$$
It is a contradiction  since $\wt\bl\M(xs_i\vpi,x\vpi)\br=xs_i\vpi-x\vpi$ does not vanish.
\end{proof}
