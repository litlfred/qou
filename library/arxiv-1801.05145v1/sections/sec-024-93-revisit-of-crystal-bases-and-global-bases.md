---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-024-93-revisit-of-crystal-bases-and-global-bases
section_title: "Revisit of crystal bases and global bases"
section_number: 9.3
pages: 70-74
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.915
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
In order to prove Theorem~\ref{thm: DDD} below, we first investigate
the upper crystal lattice of
$\Dv V$ induced by an upper  crystal lattice of $V\in\Oint(\g)$.

Let $V$ be a $U_q(\g)$-module in $\Oint (\g)$. Let $L^\up$ be an upper crystal lattice of $V$. Then we have (see Lemma~\ref{lem:lowup})
$$ \soplus_{\xi \in \wl} q^{(\xi,\xi)/2}(L^\up)_\xi \text{ is a lower crystal lattice of $V$.}$$

Recall that, for $\lambda\in \wl^+$, the upper crystal lattice $L^\up(\lambda)$ and the lower crystal lattice $L^\low(\lambda)$ of $V(\lambda)$ are related by
\begin{align}
L^\up(\lambda) = \soplus_{\xi \in \wl} q^{((\lambda,\lambda)-(\xi,\xi))/2}L^\low(\lambda)_\xi \subset L^\low(\lambda).
\end{align}

Write
$$V \simeq \soplus_{\lambda \in \wl^+} E_\lambda \otimes V(\lambda)$$
with finite-dimensional $\Q(q)$-vector spaces $E_\lambda$ .
Accordingly, we have a canonical decomposition
$$L^\up \simeq \soplus_{\lambda\in \wl^+} C_\lambda \otimes_{\QA_0} L^\up(\lambda),$$
where $C_\lambda \subset E_\lambda$ is an $\QA_0$-lattice of $E_\lambda$.

On the other hand, we have
$$\Dv V \simeq\soplus_{\lambda\in \wl^+}  E^*_\lambda \otimes V(\lambda).$$

Note that we have
$$ \Phi_V \left( (a \otimes u) \otimes (b \otimes v)^\ri \right) = \lan a,b \ra \Phi_\lambda(u \otimes v^\ri)
\quad \text{for $u,v \in V(\lambda)$ and $a \in E_\lambda$, $b \in E^*_\lambda$.}$$


We define the induced upper crystal lattice $\Dv L^\up$ of $\Dv V$ by
$$\Dv L^\up \seteq \soplus_{\lambda \in \wl^+} C_\lambda^\vee \otimes_{\QA_0} L^\up(\lambda)
\subset \Dv V, $$
where $C_\lambda^\vee \seteq  \set{ u \in E_\lambda^*}{\lan u,C_\lambda \ra \subset \QA_0 }$. Then we have
$$ \Phi_V \left(L^\up \otimes (\Dv L^\up)^\ri \right) \subset L^\up(A_q(\g)).$$
Indeed, we have
$$ \Dv L^\up =\set{ u \in \Dv V }{\Phi_V(L^\up \otimes u^\ri) \subset L^\up(A_q(\g)) }. $$

Since $(L^\up(\lambda))^\vee = L^\low(\lambda)$, we have
$$ (L^\up)^\vee = \soplus_{\lambda \in \wl^+} C_\lambda^\vee \otimes_{\QA_0} L^\low(\lambda).$$

The properties $L^\up(\lambda) \subset L^\low(\lambda)$ and $L^\up(\lambda)_\lambda = L^\low(\lambda)_\lambda$ imply the following lemma.

\begin{lemma} \label{lem: largest upper crystal}
$\Dv L^\up$ is the largest upper crystal lattice of $\Dv V$ contained in the lower crystal lattice $(L^\up)^\vee$.
\end{lemma}


Let $\la, \mu\in\Pd$.
Then
$\bl L^\up(\la)\tensp L^\up(\mu)\br^\vee
=L^\low(\la)\tensm L^\low(\mu)$ is a lower crystal lattice of
$\Dv\bl V(\la)\tensp V(\mu)\br\simeq V(\la)\tensm V(\mu)$.
Let
$\Xi_{\la,\mu}\cl V(\la)\tensp V(\mu)\isoto V(\la)\tensm V(\mu)
\simeq \Dv\bl V(\la)\tensp V(\mu)\br$
be the $\U$-module isomorphism defined by
$$\Xi_{\la,\mu}(u\tensp v)=q^{(\la,\mu)-(\xi,\eta)}\bl u\tensm v\br
\quad\text{for $u\in V(\la)_\xi$ and $v\in V(\mu)_\eta$.}
$$

Then
\eqn
\tLt&\seteq&\Xi_{\la,\mu}\bl L^\up(\la)\tensp L^\up(\mu)\br\\
&\;=&\soplus_{\xi,\eta\in\Po}
q^{(\la,\mu)-(\xi,\eta)}L^\up(\la)_\xi\tensm L^\up(\mu)_\eta
\eneqn
is an upper crystal lattice of $V(\la)\tensm V(\mu)$.
Since we have $(\la,\mu)-(\xi,\eta)\ge0$
for any $\xi\in\wt\bl V(\la)\br$ and $\eta\in\wt\bl V(\mu)\br$,
Lemma~\ref{lem: largest upper crystal} implies that
\eq \label{eq:tildeL}
\tLt\subset \Dv\bl L^\up(\la)\tensp L^\up(\mu)\br.
\eneq

\begin{lemma}
Let $\lambda, \mu \in \wl^+$ and $x_1,x_2,y_1,y_2 \in W$ such that $x_k \ge y_k$
 $(k=1,2)$. Then we have
\begin{equation} \label{eq: multi}
\begin{aligned}
& q^{(\lambda,\mu)-(x_2\lambda,y_2\mu)} \Delta(x_1\lambda,x_2\lambda)\Delta(y_1\mu,y_2\mu) \\
& \hspace{10ex} \equiv G^\up( \oi^{-1}_{\lambda,\mu}(u_{x_1\lambda} \otimes u_{y_1 \mu}) \otimes  \oi^{-1}_{\lambda,\mu}(u_{x_2\lambda} \otimes u_{y_2 \mu})^\ri )
\quad {\rm mod} \ q L^\up(A_q(\g)).
\end{aligned}
\end{equation}
\end{lemma}
\Proof
By the definition, we have
$$\De{x_1\la,x_2\la}\De{y_1\mu,y_2\mu}
=\Phi_{V(\la)\tensp V(\mu)}\bl
(u_{x_1\la}\tensp u_{y_1\mu})\tens (u_{x_2\la}\tensm u_{y_2\mu})^\rt\br.$$
Hence we have
\eqn
&&q^{(\la,\mu)-(x_2\la,y_2\mu)}
\De{x_1\la,x_2\la}\De{y_1\mu,y_2\mu}\\
&&\hs{3ex}=\Phi_{V(\la)\tensp V(\mu)}\bl
(u_{x_1\la}\tensp u_{y_1\mu})\tens q^{(\la,\mu)-(x_2\la,y_2\mu)}(u_{x_2\la}\tensm u_{y_2\mu})^\rt\br\\
&&\hs{6ex}=\Phi_{V(\la)\tensp V(\mu)}\bl
(u_{x_1\la}\tensp u_{y_1\mu})\tens
\bl\Xi_{\la,\mu}(u_{x_2\la}\tensp u_{y_2\mu})\br^\rt\br.
\eneqn
The right-hand side of \eqref{eq: multi} can be calculated as follows.
Let us take $v_k\in L^\up(\la+\mu)$ such that $\iota_{\la,\mu}(v_k)-u_{x_k\la}\tensp u_{y_k\mu}
\in qL^\up(\la)\tensp L^\up(\mu) $  for $k=1,2$.
Here $\iota_{\la,\mu}\cl V(\la+\mu)\to V(\la)\tensp V(\mu)$
denotes the canonical $\U$-module homomorphism and such a $v_k$ exists by Lemma \ref{lem:oi la mu}.

Then we have
\eqn
&&G^\up\Bigl(\oi_{\la,\mu}^{\ -1}(u_{x_1\la}\tens u_{y_1\mu})
\tens\bl  \oi_{\la,\mu}^{\ -1}(u_{x_2\la}\tens u_{y_2\mu})\br^\rt\Bigl)\\
&&\hs{5ex}\equiv \Phi_{\la+\mu}(v_1\tens v_2^\rt)\mod qL^\up(\Ag)\\
&&\hs{6ex}=\Phi_{V(\la)\tensp V(\mu)}\bl \iota_{\la,\mu}(v_1)\tens
\bl\Xi_{\la,\mu}\iota_{\la,\mu}(v_2))^\rt \br.
\eneqn
 The last equality follows from $(v_2, u) = (\Xi_{\la,\mu}\iota_{\la,\mu}(v_2), \iota_{\la,\mu} (u))$ for all $u \in V(\la+\mu)$.

On the other hand, we have
$$\iota_{\la,\mu}(v_1)\equiv
u_{x_1\la}\tensp u_{y_1\mu}\mod qL^\up(\la)\tensp L^\up(\mu)$$
and
$$\Xi_{\la,\mu}\bl\iota_{\la,\mu}(v_2)\br
\equiv \Xi_{\la,\mu}(u_{x_2\la}\tensp u_{y_2\mu})\mod q\tLt.
$$
Hence
\eqn
&&\Phi_{V(\la)\tensp V(\mu)}\bl
(u_{x_1\la}\tensp u_{y_1\mu})\tens \Xi_{\la,\mu}(u_{x_2\la}\tensp u_{y_2\mu})^\rt\br\\
&&\hs{10ex}\equiv
\Phi_{V(\la)\tensp V(\mu)}\bl (\iota_{\la,\mu}(v_1)\tens
(\Xi_{\la,\mu}\iota_{\la,\mu}(v_2))^\rt\br
\mod qL^\up(\Ag)
\eneqn
by \eqref{eq:tildeL}, as desired.
\QED

\begin{theorem} \label{thm: DDD}
Let $\lambda \in \wl^+$ and $x,y \in W$ such that $x \ge y$. Then we have
$$ \D(x\lambda,y\lambda)\D(y\lambda,\lambda) \equiv \D(x\lambda,\lambda) \quad {\rm mod} \ qL^\up(A_q(\n)).$$
\end{theorem}

\begin{proof}
Applying $p_\n$ to \eqref{eq: multi}, we have
\begin{equation*}  \label{eq: DDD}
\begin{aligned}
& \D(x\lambda,y\lambda)\D(y\lambda,\lambda) \\
& \hspace{10ex} \equiv p_\n
\left( G^\up( \oi^{-1}_{\lambda,\lambda}(u_{x\lambda} \otimes u_{y \lambda})  \otimes \oi^{-1}_{\lambda,\lambda}(u_{y\lambda} \otimes u_{\lambda})^\ri ) \right)
\quad {\rm mod} \ q L^\up(A_q(\n)).
\end{aligned}
\end{equation*}
Hence the desired result follows from
Proposition~\ref{prop: nonzero elt}, Proposition \ref{prop: p_n} and  Lemma \ref{lem: iotas} below.
\end{proof}


\Lemma\label{lem: iotas}
Let $\la\in \Pd$ and $x,y\in W$ such that $x\ge y$.
Then we have
$$
\bg\Bigl(
\oi_{\la,\la}^{\ -1}(u_{x\la}\tens u_{y\la})
\tens\bl  \oi_{\la,\la}^{\ -1}(u_{y\la}\tens u_{\la})\br^\rt\Bigr)
=\oi_\la(u_{x\la})\tens t_{y\la+\la}\tens b_{-\infty}.$$
\enlemma

\Proof
We shall argue by induction on $\ell(x)$.
We set $b_{x\la}=\oi_\la(u_{x\la})$.
Since the case $x=1$ is obvious, assume that $x\not=1$.
Take $i\in I$ such that $x'\seteq s_ix<x$

\medskip
\noi
(a) First assume that $s_iy>y$. Then we have
$y\le  x'$.
Hence by the induction hypothesis,
\eq
&&\oi_\g\Bigl(
\oi_{\la,\la}^{\ -1}(u_{x'\la}\tens u_{y\la})
\tens\bl  \oi_{\la,\la}^{\ -1}(u_{y\la}\tens u_{\la})\br^\rt\Bigr)
=b_{x'\la}\tens t_{y\la+\la}\tens b_{-\infty}.\label{eq:agtu}
\eneq
We have $\vphi_i(u_{x'\la})=\lan h_i,x'\la\ran$ and
$\vphi_i(b_{x'\la}\tens t_{y\la+\la}\tens b_{-\infty}) =\vphi_i(b_{x'\la}\tens t_{y\la+\la})=\lan h_i,x'\la\ran
+\lan h_i,y\la\ran\ge\lan h_i,x'\la\ran$.
Hence, applying $\tf_i^{\lan h_i,x'\la\ran}$ to \eqref{eq:agtu}, we obtain
\eqn
&&\oi_\g\Bigl(
\oi_{\la,\la}^{\ -1}(u_{x\la}\tens u_{y\la})
\tens\bl  \oi_{\la,\la}^{\ -1}(u_{y\la}\tens u_{\la})\br^\rt\Bigr)
=b_{x\la}\tens t_{y\la+\la}\tens b_{-\infty}.
\eneqn


\medskip
\noi
(b) Assume that $y'\seteq s_iy<y$. Then we have
$y'\le x'$, and the induction hypothesis implies that
$$
\oi_\g\Bigl(
\oi_{\la,\la}^{\ -1}(u_{x'\la}\tens u_{y'\la})
\tens\bl  \oi_{\la,\la}^{\ -1}(u_{y'\la}\tens u_{\la})\br^\rt\Bigr)
=b_{x'\la}\tens t_{y'\la+\la}\tens b_{-\infty}.$$
 Apply $\te_i^{*\;\lan h_iy'\la\ran}\tf_i^{\lan h_i,x'\la+y'\la\ran}$
to the both sides.
Then the left-hand side yields
$$\oi_\g\Bigl(
\oi_{\la,\la}^{\ -1}(u_{x\la}\tens u_{y\la})
\tens\bl  \oi_{\la,\la}^{\ -1}(u_{y\la}\tens u_{\la})\br^\rt\Bigr).$$
Since $\vphi_i(b_{x'\la}\tens t_{y'\la+\la})=\lan h_i,x'\la\ran
+\lan h_i,y'\la+\la\ran\ge\lan h_i,x'\la+y'\la\ran$,
the right-hand side yields
\begin{align*}
\te_i^{*\;\lan h_i,y'\la\ran}\tf_i^{\lan h_i,x'\la+y'\la\ran}
\bl b_{x'\la}\tens t_{y'\la+\la}\tens b_{-\infty}\br
&=\te_i^{*\;\lan h_i,y'\la\ran}\bl(\tf_i^{\lan h_i,x'\la+y'\la\ran}
 b_{x'\la})\tens t_{y'\la+\la}\tens b_{-\infty}\br\\
&=\te_i^{*\;\lan h_i,y'\la\ran}\bl(\tf_i^{\lan h_i,y'\la\ran}
 b_{x\la})\tens t_{y'\la+\la}\tens b_{-\infty}\br.
\end{align*}

Since
$\eps_i^*(b_{x\la})=-\vphi_i(b_{x\la}) = \lan h_i, \la\ran$
and
$\tf_i^{\lan h_i,y'\la\ran}b_{x\la}=\tf_i^{*\;\lan h_i,y'\la\ran}b_{x\la}$,
we have
\begin{align*}\te_i^{*\;\lan h_i,y'\la\ran}\bl(\tf_i^{\lan h_i,y'\la\ran}
 b_{x\la})\tens t_{y'\la+\la}\tens b_{-\infty}\br
&=b_{x\la}\tens t_{y\la+\la}\tens b_{-\infty}.
 \qedhere
\end{align*}
\QED
