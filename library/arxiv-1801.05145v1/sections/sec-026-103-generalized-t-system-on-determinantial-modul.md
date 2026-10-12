---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-026-103-generalized-t-system-on-determinantial-modul
section_title: "Generalized T-system on determinantial module"
section_number: 10.3
pages: 81-91
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.584
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




\section{Monoidal categorification of $A_q(\n(w))$}



\subsection{Quantum cluster algebra structure on $A_q(\n(w))$} \label{subsubsec: Q cluster Anw}
In this subsection, we shall consider the Kac-Moody algebra
$\g$ associated with a symmetric Cartan matrix $\cmA=(a_{i,j})_{i,j\in I}$.
We shall recall briefly the definition of the subalgebra $A_q(\n(w))$ of $A_q(\g)$ and its quantum cluster algebra structure by using
the results of \cite{GLS} and \cite{Kimu12}.
Remark that we bring the results in \cite{GLS}
through the  isomorphism \eqref{eq:isoAqn}.
\medskip

For a given $w \in W$, fix a reduced expression $\widetilde{w}=s_{i_r}\cdots s_{i_1}$.


For $s \in \{ 1,\ldots,r \}$ and $j \in I$, we set
\begin{equation*} \label{eq: s+ s-}
\begin{aligned}
s_+&\seteq\min( \{k \ | \ s<k\le r,\; i_k=i_s \}\cup\{r+1\}),\\
s_-&\seteq\max(\{k \ | \  1\le k<s, \; i_k=i_s \}\cup\{0\}),\\
s^-(j)&\seteq\max(\{k \ | \ 1\le k<s,\; i_k=j \}\cup\{0\}).
\end{aligned}
\end{equation*}


We set
\eq \text{$u_k:=s_{i_1}\cdots s_{i_k}$ for $0\le k \le r$}, \label{eq:lau}
\eneq
and
\eqn
\text{$\la_k\seteq u_k\varpi_{i_k}$ for $1\le k \le r$}.
\eneqn

Note that $\la_{k_- }=u_{k-1}\varpi_{i_k}$,  if $k_- >0$ .
For $0\le t\le s\le r$, we set
\begin{align*} 
\D(s,t)&=
\bc
\D(\lambda_s,\lambda_t) & \text{if $0<t$,}\\
\D(\lambda_s,\varpi_{i_s})& \text{if $0=t<s\le r$,}\\
\one&\text{if $t=s=0$.}
\ec
\end{align*}


 The $\Q(q)$-subalgebra of  $A_q(\n)$ generated by
$\D(i,i_-)$ ($1\le i\le r$) is independent of the choice of a reduced expression of $w$. We denote it by $A_q(\n(w))$.
Then every $\D(s,t)$ ($0\le t\le s\le r$) is contained in $A_q(\n(w))$
(\cite[Corollary 12.4]{GLS}).
The set $\B^\up\bl A_q(\n(w))\br\seteq\B^\up\bl A_q(\g)\br\cap A_q(\n(w))$
is a basis of $A_q(\n(w))$ as a $\Q(q)$-vector space
(\cite[Theorem 4.2.5]{Kimu12}).
We call it the \emph{upper global basis} of $A_q(\n(w))$.
 We denote by $A_q(\n(w))_\A$ the $\A$-module generated by $\B^\up\bl A_q(\n(w))$.
Then it is a $\A$-subalgebra of $A_q(\n(w))$ (\cite[\S 4.7.2]{Kimu12}).
We set $A_{q^{1/2}}(\n(w)) \seteq \Q(q^{1/2})  \otimes_{\Q(q)}  A_{q}(\n(w))$.

\medskip
 Let $\K=\{1,\ldots,r\}$,
$\Kfr\seteq\set{k\in\K}{k_+=r+1}$ and $\Kex\seteq\K\setminus\Kfr$.
\begin{definition} We define the quiver $Q$
with the set of vertices $Q_0$ and the set of
arrows $Q_1$ as follows:
\begin{enumerate}
\item[$(Q_0)$]
$Q_0=\K=\{1,\ldots,r\}$,
\item[$(Q_1)$] There are two types of arrows:
\eqn
&&\ba{lccl}\text{{\em ordinary arrows}}&:&\text{$s\To[\ |a_{i_s,i_t}|\ ] t$}
&\text{if $1\le s<t<s_+<t_+\le r+1$,}\\[1ex]
\text{{\em horizontal arrows}}&:&
\text{$s\longrightarrow s_-$}&
\text{if $1\le s_-<s\le r$.}
\ea
\eneqn
\end{enumerate}
Let $\widetilde B = (b_{i,j})$ be the integer-valued $\K\times\Kex$-matrix associated to the quiver $Q$ by \eqref{eq: bij}.
\end{definition}

\begin{lemma}
Assume that $0 \le d\le b\le a\le c \le r$ and
\begin{itemize}
\item $i_b=i_a$  when   $b \ne 0$,
\item $i_d=i_c$  when  $d \ne 0$.
\end{itemize}
Then $\D(a,b)$ and $\D(c,d)$ $q$-commute; that is, there exists $\lambda \in \Z$ such that
$$ \D(a,b)\D(c,d)= q^{\lambda}\D(c,d)\D(a,b).$$
\end{lemma}

\begin{proof}
We may assume $a>0$.
Let $u_k$ be as in \eqref{eq:lau}.
Take $s'=u_a$, $s=u_a^{-1}u_c$, $t'=u_d$ and $t=u_d^{-1}u_b$. Then we have
$$ \D(s'\varpi_{i_a},t't\varpi_{i_a})=\D(a,b)\quad \text{and}\quad
  \D(s's\varpi_{i_c},t'\varpi_{i_c})=\D(c,d).$$
From Proposition \ref{prop: BZ form}, our assertion follows.
\end{proof}

Hence we have an integer-valued skew-symmetric matrix $L=(\lambda_{i,j})_{1 \le i,j \le r}$ such that
$$ \D(i,0)\D(j,0)=q^{\lambda_{i,j}}\D(j,0)\D(i,0).$$

\begin{prop} [{\cite[Proposition 10.1]{GLS}}] The pair $(L,\wB)$ is compatible with $d=2$ in \eqref{eq:compatible}.
\end{prop}

\begin{theorem}[{\cite[Theorem 12.3]{GLS}}] Let
$\mathscr{A}_{q^{1/2}}([\mathscr{S}])$ be the quantum cluster algebra associated to the initial quantum seed
$[\mathscr{S}]\seteq( \{ q^{-(d_s,d_s)/4}\D(s,0) \}_{1 \le s \le r}, L, \wB )$.
Then we have an  isomorphism of  $\Q(q^{1/2})$-algebras
$$ \Q(q^{1/2})  \otimes_{\Z[q^{\pm 1/2}]} \mathscr{A}_{q^{1/2}}([\mathscr{S}]) \simeq   A_{q^{1/2}}(\n(w)),$$
where $d_s \seteq \lambda_s-\varpi_{i_s}=\wt(D(s,0))$ and
$A_{q^{1/2}}(\n(w)) \seteq \Q(q^{1/2})  \otimes_{\Q(q)}  A_{q}(\n(w))$.
\end{theorem}


\subsection{Admissible seeds in the monoidal category $\shc_w$}

 For $0\le t\le s\le r$, we set
$\M(s,t)=\M(\la_s,\la_t)$.
It is a real simple module with $\ch(\M(s,t))=D(s,t)$.

\begin{definition} \label{def:cw}
For $w \in W$, let $\shc_w$ be the smallest monoidal abelian full subcategory of $R \gmod$ satisfying the following properties:
\begin{enumerate}
\item[{\rm (i)}] $\shc_w$ is stable under the subquotients, extensions and grading shifts,
\item[{\rm (ii)}] $\shc_w$ contains $\M(s,s_-)$ for all $1 \le s \le \ell(w)$.
\end{enumerate}
\end{definition}

Then by \cite{GLS}, $M\in R\gmod$ belongs to $\shc_w$ if and only if $\ch(M)$
belongs to $A_q(\n(w))$. Hence we have  a $\A$-algebra isomorphism
$$K(\shc_w)\simeq A_q(\n(w))_\A.$$

We set
$$\Lambda \seteq (\La(\M(i,0),\M(j,0)))_{1 \le i,j\le r} \quad \text{ and }
\quad D= (d_i)_{1 \le i \le r} \seteq (\wt(\M(i,0)))_{1 \le i \le r}.$$

Then, by Proposition~\ref{prop: commute 1},
$\Seed \seteq ( \{ \M(k,0) \}_{1 \le k \le r}, -\Lambda, \wB, D )$
is a quantum monoidal seed in $\shc_w$.
We are now ready to state the main theorem in this section:

\begin{theorem} \label{thm: main}
The pair
$\bl \{ \M(k,0) \}_{1 \le k \le r}, \wB\br$ is admissible.
\end{theorem}
As we already explained,  combined with Theorem  \ref{th:main} and Corollary \ref{cor:main}, this theorem implies
the following  theorem.
\begin{theorem}
The category $\shc_w$ is a monoidal categorification of the quantum cluster algebra $A_{q^{1/2}}(\n(w))$.
\end{theorem}


In the course of  proving Theorem~\ref{thm: main},
{\em we omit grading shifts} if there is no  danger of confusion.

We shall start the proof of Theorem~\ref{thm: main}
by proving that, for each $s\in\Kex$,  there exists a simple module $X$ such that
\begin{eqnarray}&&\left\{
\parbox{70ex}{ \bnam
\item there exists a surjective homomorphism (up to a grading shift)
$$  X \conv \M(s,0) \twoheadrightarrow \conv_{t;\; b_{t,s}> 0 } \M(t,0)^{\circ b_{t,s} },$$
\item there exists a surjective homomorphism (up to a grading shift)
$$ \M(s,0) \conv X \twoheadrightarrow \conv_{t;\;\ b_{t,s}<0} \M(t,0)^{\circ -b_{t,s}},$$
\item $\de(X,\M(s,0))=1$.
\ee }\right. \label{eq: conditions}
\end{eqnarray}

We set
\eqn
&&x\seteq i_s\in I,\\
&&I_s\seteq\set{i_k}{s<k<s_+}\subset I\setminus\{x\},\\
&&A\seteq
  \displaystyle \mathop{\conv}\limits_{t<s < t_+ < s_+ }
\M(t,0)^{\circ |a_{i_s,i_t}| }
= \displaystyle\mathop{\conv} \limits_{y\in I_s}
\M(s^-(y),0)^{\circ |a_{x,y}| }.
\eneqn
Then $A$ is a real simple module.

Now we claim that the following simple module $X$ satisfies
the conditions in \eqref{eq: conditions}:
$$X \seteq \M(s_+,s) \hconv  A.$$

Let us show \eqref{eq: conditions} (a).
The incoming arrows to $s$ are
\begin{itemize}
\item $t \To[{|a_{x,i_t}|}]s $ for $1\le t<s<t_+<s_+$,
\item $s_+ \To s$.
\end{itemize}
Hence we have
$$\conv_{t;\;  b_{t,s} > 0 } \M(t,0)^{\circ b_{t,s}}
\simeq A\conv M(s_+,0).$$

\medskip

Then the morphism in (a)
is obtained  as the composition:
\begin{align} \label{eq: surjection 1}
X \conv \M(s,0)  \rightarrowtail A \conv \M(s_+,s) \conv \M(s,0) \twoheadrightarrow A \conv \M(s_+,0).
\end{align}
Here the second epimorphism
is given in Theorem \ref{thm: canonical surjection},  and
Lemma \ref{lem:composition} asserts that the composition
\eqref{eq: surjection 1} is non-zero
and hence an epimorphism.

\medskip

Let us show \eqref{eq: conditions} (b).
The outgoing arrows from $s$ are
\begin{itemize}
\item $s \To[{\;|a_{x,i_t}|\;}]t$\quad for $s<t<s_+<t_+\le r+1$.
\item $s \longrightarrow s_-$\quad if $s_- > 0$.
\end{itemize}
Hence we have
\eq
&&\mathop{\conv}_{t; b_{t,s}<0 } \M(t,0)^{\circ -b_{t,s}}
\simeq\M(s_-,0)\conv \left(\mathop{\conv}_{y\in I_s} \M((s_+)^-(y),0)^{\circ -a_{x,y}}\right).
\eneq

\begin{lemma} \label{lem: step1}
There exists an epimorphism  \ro up to a grading\rf
\begin{align*} 
\Omega: \M(s,0) \conv \M(s_+,s) \conv A \twoheadrightarrow \conv_{t;b_{t,s}<0} \M(t,0)^{\circ -b_{t,s}}.
\end{align*}
\end{lemma}

\begin{proof}
By the dual of Theorem \ref{thm: canonical surjection} and the $T$-system
\eqref{eq: deteminatial seq2}
with $i=i_s$, $u=u_{s_+-1}$ and $v=u_{s-1}$, we have morphisms
\eqn
&& \M(s,0) \rightarrowtail \M(s_-,0) \conv \M(s,s_-), \label{eq: 1} \\
&&\M(s,s_-)\conv \M(s_+,s) \twoheadrightarrow
\displaystyle \conv_{y \in I\setminus\{x\}} \M((s_+)^-(y),s^-(y))^{\circ -a_{x,y}}\\\label{eq: 2}
&&\hs{35ex}\simeq \displaystyle \conv_{y \in I_s}
\M((s_+)^-(y),s^-(y))^{\circ -a_{x,y }}.  \nn
\eneqn
Here the last isomorphism follows from the fact that
$(s_+)^-(y)=s^-(y)$ for any $y\not\in \{x\}\cup I_s=\set{i_k}{s\le k<s_+}$.


Thus we have a sequence of morphisms
\eqn
&&\M(s,0) \conv \M(s_+,s) \conv A\; \xymatrix{\ar@{>->}[r]^-{\varphi_1}&}
 \M(s_-,0) \conv \M(s,s_-) \conv \M(s_+,s) \conv A  \\
&&\hs{25ex}\xymatrix@C=6ex{\ar@{->>}[r]^-{\varphi_2} &}\M(s_-,0) \conv
\left(\conv_{y \in I_s} \M((s_+)^-(y),s^-(y))^{\circ -a_{x,y}}\right) \conv A.
\eneqn
By Lemma \ref{lem:composition} (i), the composition
$\varphi \seteq \varphi_2 \circ \varphi_1$ is non-zero.

Since
$A=  \displaystyle\conv_{ \substack{y\in I_s} }  \M(s^-(y),0)^{\circ -a_{x,y} }$,
Theorem \ref{thm: canonical surjection} gives the  morphisms
\begin{align*}
 \M(s,0) \conv \M(s_+,s) \conv A   & \xymatrix@C=4ex{\ar[r]^-{\varphi}&}
   \M(s_-,0) \conv
\left(\conv_{y\in I_s} \M((s_+)^-(y),s^-(y))^{\circ -a_{x,y}}\right) \conv A  \\
&\xymatrix@C=4ex{\ar@{->>}[r]^-{\phi} &}\M(s_-,0)\conv \left(\conv_{y\in I_s} \M((s_+)^-(y),0)^{\circ -a_{x,y}}\right)\simeq \conv_{t; b_{t,s}<0} \M(t,0)^{\circ -b_{t,s}}.
\end{align*}
Here we have used Lemma~\ref{lem:MN} to obtain the morphism $\phi$.
Note that  the module $\conv_{y \in I_s} \M((s_+)^-(y),s^-(y))^{\circ -a_{x,y}}$
is  simple.
By applying Lemma \ref{lem:composition}
 once again, $\phi \circ \varphi$ is non-zero, and hence it is an epimorphism.
\end{proof}

\Lemma\label{lem: simply linked}
We have $\de(X,\M(s,0))=1$.
\enlemma

\begin{proof}
Since $A$ and $\M(s,0)$ commute and
$\de\big(\M(s_+,s),\M(s,0)\big)=1$ by Proposition~\ref{prop:deMM}, we have
$$\de\big( X,\M(s,0) \big) \le\de\big(\M(s_+,s),\M(s,0)\big)+
\de\big(A,\M(s,0)\big)\le1$$
by Proposition \ref{pro:subquotient}
and Lemma \ref{lem:commute_equiv}.
If $X$ and $\M(s,0)$ commute, then \eqref{eq: conditions} (a)
 would imply
that ${\rm ch} \left(\conv_{t;\ b_{t,s}>0}  M(t,0)^{\circ b_{t,s}} \right)$
belongs to $K(R \gmod)\,{\rm ch}(\M(s,0))$.
It contradicts the result in \cite{GLS13} that all the ${\rm ch}(\M(k,0))$'s are
prime at $q=1$.
\end{proof}


\begin{prop} \label{prop: step2}
The map  $\Omega$
factors through $\M(s,0) \conv X$; that is,
\begin{align*} \label{eq: surjection 2}
\xymatrix{
 \M(s,0) \conv \M(s_+,s) \conv A  \ar@{->>}[drr]^{\tau}\ar@{->>}[rrrr]^{\Omega} &&&&  \displaystyle \conv_{t; b_{t,s}<0} \M(t,0)^{\circ  -b_{t,s}}. \\
 && \M(s,0) \conv X \ar@{->>}[urr]^{\overline{\Omega}}
}
\end{align*}
Here $\tau$ is the canonical surjection.
\end{prop}

\begin{proof}
We have $1=\de\big(\M(s,0), \M(s_+,s)\hconv A\big)$
by Lemma~\ref{lem: simply linked}, and
$$\de\big(\M(s,0),\M(s_+,s)\big)+
\de\big(\M(s,0),A\big)=1$$
by Proposition~\ref{prop:deMM} with $x=u_{s_+ -1}, \ i = i_s$.
Hence $ \M(s,0) \conv \M(s_+,s) \conv A
$ has a simple head by Proposition~\ref{prop:3simple} (iii).
\end{proof}


\begin{proof}[End of the proof of Theorem \ref{thm: main}]
By the   above arguments, we have proved the existence of $X$ which satisfies
\eqref{eq: conditions}.
By Proposition \ref{Prop: l2} and \eqref{eq: conditions} (c),
$\M(s,0) \conv X$ has composition
length $2$. Moreover, it has a simple socle and simple head.
On the other hand, taking the dual of \eqref{eq: conditions} (a),
we obtain a monomorphism
$$\sodot_{t; b_{t,s}>0} \M(t,0)^{\snconv  b_{t,s}} \monoto \M(s,0)\conv X$$
in $R\smod$.
Together with \eqref{eq: conditions} (b),
there exists a short exact sequence in $R\gmod$:
$$ 0 \to q^c\sodot_{t;b_{t,s}>0} \M(t,0)^{\snconv b_{t,s}} \to q^{\tLa(\M(s,0), X)}  \M(s,0) \conv X \to \sodot_{t;b_{t,s}<0} \M(t,0)^{\snconv(-b_{t,s})} \to 0$$
for some $c\in \Z$. By Lemma \ref{lem:crde}
$c$
must be equal to $1$.

It remains to prove that $X$ commutes with $\M(k,0)$ ($k\not=s$).
For any $k\in\K$, we have
\begin{align*}
\La(\M(k,0),X)&=\La(\M(k,0),\M(s,0)\hconv X)-\La(\M(k,0), \M(s,0))\\
&=\sum_{t;\;b_{t,s}<0}\La(\M(k,0),\M(t,0))(-b_{t,s})-\La(\M(k,0), \M(s,0))
\end{align*}
and
\begin{align*}
\La(X,\M(k,0))&=\La(X\hconv\M(s,0),\M(k,0))-\La(\M(s,0), \M(k,0))\\
&=\sum_{t;\;b_{t,s}>0}\La(\M(t,0),\M(k,0))b_{t,s}-\La(\M(s,0), \M(k,0)).
\end{align*}
Hence we have
\begin{align*}
2\de(\M(k,0),X)&  =-2\de(\M(k,0),\M(s,0)) -
\sum_{t;\;b_{t,s}<0}\La(\M(k,0),\M(t,0))b_{t,s} \\
& \hspace{23.5ex}-\sum_{t;\;b_{t,s}>0}\La(\M(k,0),\M( t  ,0))b_{t,s} \\
& =- \sum_{1 \le t \le r}\La(\M(k,0),\M(t,0))b_{t,s} \\ & = 2\delta_{k,s},
\end{align*}
We conclude that $X$  commutes with $M(k,0)$ if $k\not=s$.
Thus we complete the proof of Theorem~\ref{thm: main}.
\end{proof}

As a corollary, we  prove the following conjecture

on the cluster monomials.
\Th  {\rm(}{\cite[Conjecture 12.9]{GLS}, \cite[Conjecture 1.1(2)]{Kimu12}} {\rm )}

 Every cluster variable in  $A_{q}(\n(w))$ is a member of the upper global basis  up to a power of $q^{1/2}$.
\enth
Theorem \ref{thm: main} also implies \cite[Conjecture 12.7]{GLS} in the refined form as follows:

\begin{corollary}
$\Z[q^{\pm1/2}]\tens_{\Z[q^{\pm1}]} A_{q}(\n(w))_{\Z[q^{\pm1}]}$ has a quantum cluster algebra structure associated with the initial quantum seed
$[\mathscr{S}]=( \{ q^{-(d_i,d_i)/4}\D(i,0) \}_{1 \le i \le r}, L, \wB )$; i.e.,
$$\Z[q^{\pm1/2}]\tens_{\Z[q^{\pm1}]} A_{q}(\n(w))_{\Z[q^{\pm1}]} \simeq \mathscr{A}_{q^{1/2}}([\Seed]).$$
\end{corollary}
