---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-022-9-quantum-minors-and-t-systems
section_title: "Quantum minors and T-systems"
section_number: 9
pages: 66-70
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.917
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\label{sec:Quantum minors and T-systems}



\subsection{Quantum minors}
Using the isomorphism $\Phi$ in \eqref{eq: Phi}, for each
$\lambda \in \wl^+$ and $\mu, \zeta \in W \lambda$, we define the elements
$$ \Delta(\mu,\zeta)\seteq \Phi(u_\mu\tens u_\zeta^\ri) \in A_q(\g)$$
and
$$\D(\mu,\zeta)\seteq p_\n(\Delta(\mu,\zeta)) \in A_q(\n).$$
The element $\Delta(\mu,\zeta)$ is called a {\em {\rm (}generalized{\rm )}  quantum minor}
and $\D(\mu,\zeta)$ is called {\em a unipotent quantum minor}.


\begin{lemma} \label{lem: global element}
$\Delta(\mu,\zeta)$ is a member of the upper global basis of $A_q(\g)$. Moreover,
$\D(\mu,\zeta)$
is either a member of the upper global basis of $ A_q(\n)$ or zero.
\end{lemma}
\begin{proof}   Our assertions follow from Proposition~\ref{prop:Agglobal} and
Proposition~\ref{prop: nonzero elt}.
\end{proof}
\Lemma[{\cite[{(9.13)}]{BZ05}}]
 For $u,v \in W$ and $\lambda,\mu \in \wl^+$, we have
$$ \Delta(u\lambda,v\lambda)\Delta(u\mu,v\mu) =
\Delta\bl u (\lambda+\mu),v(\lambda+\mu)\br.$$
\enlemma


By Proposition \ref{prop: p_n}, we have the
following corollary:

\begin{corollary}\label{cor:Duv}
For $u,v \in W$ and $\lambda,\mu \in \wl^+$, we have
$$ \D(u\lambda,v\lambda)\D(u\mu,v\mu) =
q^{-(v\lambda,v\mu-u\mu)}\D\bl u (\lambda+\mu),v(\lambda+\mu)\br.$$
\end{corollary}

Note that
$$ \D(\mu,\mu)=1 \quad \text{ for $\mu \in W\lambda$ }.$$

Then $\D(\mu,\zeta) \ne 0$ if and only if $\mu \preceq \zeta$. Recall
that for $\mu,\zeta$ in the same $W$-orbit, we say that $\mu \preceq
\zeta$ if there exists a sequence $\{ \beta_k \}_{1 \le k \le l}$ of positive real roots such that, defining $\lambda_0=\zeta$,
$\lambda_k=s_{\beta_k}\lambda_{k-1}$ $(1 \le k \le l)$, we have
$(\beta_k,\lambda_{k-1}) \ge 0$ and $\lambda_l=\mu$.

More precisely, we have

\begin{lemma} \label{lem: D-property}
Let $\lambda \in \wl^+$ and $\mu,\zeta \in W \lambda$. Then the
following conditions are equivalent:
\begin{enumerate}[(i)]
\item $\D(\mu,\zeta)$ is an element of upper global basis of $A_q(\n)$,
\item $\D(\mu,\zeta) \ne 0$,
\item $u_\mu \in U_q^-(\g)u_\zeta$,
\item $u_\zeta \in U_q^+(\g)u_\mu$,
\item $\mu \preceq \zeta$,
\item for any $w \in W$ such that $\mu = w \lambda$, there exists $u \le w$ \ro in the Bruhat order\rf\ such that $\zeta=u \lambda$,
\item there exist $u,v \in W$ such that $\mu = w \lambda$, $\zeta=u\lambda$ and $ u \le w$.
\end{enumerate}
\end{lemma}
\Proof
(i) and (ii) are equivalent by  Lemma \ref{lem: global element}.
The equivalence of (ii), (iii) and  (iv) is obvious.
The equivalence of (v), (vi), (vii) is well-known.
The equivalence of (iv) and (vi) is proved in \cite{Kas93a}.
\QED


For any $u\in\An\setminus\{0\}$ and $i\in I$,
we set
\begin{align*}
\eps_i(u)&\seteq\max\set{n\in\Z_{\ge0}}{e_i^nu\not=0},\\
\eps^*_i(u)&\seteq\max\set{n\in\Z_{\ge0}}{e_i^{*\,n}u\not=0}.
\end{align*}
Then for any $b\in B(\An)$, we have
$$\text{$\eps_i(G^\up(b))=\eps_i(b)$ and $\eps^*_i(G^\up(b))=\eps^*_i(b)$.}$$

\Lemma\label{lem: weyl left right}
Let $\lambda \in \wl^+$, $\mu,\zeta \in W \lambda$
such that $\mu \preceq \zeta$ and $i \in I$.
\bnum
\item If $n \seteq \lan h_i,\mu \ra \ge 0$, then
$$ \ve_i(\D(\mu,\zeta))=0 \ \ \text{ and } \ \ e_i^{(n)}\D(s_i\mu,\zeta)=\D(\mu,\zeta).$$
\item If $\lan h_i,\mu \ra \le 0$ and $s_i\mu \preceq \zeta$, then $\ve_i(\D(\mu,\zeta))=-\lan h_i,\mu \ra$.
\item If $m \seteq -\lan h_i,\zeta \ra  \ge  0$, then
$$ \ve^*_i(\D(\mu,\zeta))=0 \ \ \text{ and } \ \ {e_i^*}^{(m)} \D(\mu,s_i\zeta)=
\D(\mu,\zeta).$$
\item If $\lan h_i,\zeta \ra \ge 0$ and $\mu \preceq s_i\zeta$, then $\ve^*_i(\D(\mu,\zeta))=\lan h_i,\zeta \ra$.
\end{enumerate}
\enlemma
\Proof
We have
$\eps_i\bl\Delta(\mu,\zeta)\br=\max(-\lan h_i,\mu\ran, 0)$
and $\eps_i^*\bl\Delta(\mu,\zeta)\br=\max(\lan h_i,\zeta\ran, 0)$.
Moreover, $\pn$ commutes with $e_i^{(n)}$ and ${e_i^*}^{(n)}$.

Let us show (ii). Set $\ell=-\lan h_i,\mu \ra$.
Then we have
$e_i^{\ell+1}\Delta(\mu,\zeta)=0$, which implies
$e_i^{\ell+1}\D(\mu,\zeta)=0$. Hence $\eps_i(\D(\mu,\zeta))\le \ell$.
We have
$$e_i^{(\ell)}\Delta(\mu,\zeta)=\Delta(s_i\mu,\zeta).$$
Hence we have $e_i^{(\ell)}\D(\mu,\zeta)=\D(s_i\mu,\zeta)$.
By the assumption  $s_i\mu \preceq \zeta$, $\D(s_i\mu,\zeta)$ does not vanish.
Hence we have $\eps_i(\D(\mu,\zeta))\ge \ell$.

\smallskip
The other statements can be proved similarly.
\QED

\begin{prop}[{\cite[(10.2)]{BZ05}}] \label{prop: BZ form} Let $\lambda,\mu \in \wl^+$ and $s,t,s',t' \in W$ such that $\ell(s's)=\ell(s')+\ell(s)$ and
$\ell(t't)=\ell(t')+\ell(t)$. Then we have
\bnum
\item
$ \Delta(s's\lambda,t'\lambda)\Delta(s'\mu,t't\mu)=q^{(s\lambda,\mu)-(\lambda,t\mu)}\Delta(s'\mu,t't\mu)\Delta(s's\lambda,t'\lambda)$.
\item
If we assume further that $s's\lambda \preceq t'\lambda$ and
$s'\mu \preceq t't\mu$, then we have
\begin{align}
& \D(s's\lambda,t'\lambda)\D(s'\mu,t't\mu) = q^{(s's\lambda+t'\lambda,\;s'\mu-t't\mu)} \D(s'\mu,t't\mu)\D(s's\lambda,t'\lambda),
\label{eq: quantum commuting factor} \end{align}
or equivalently
\begin{align}
& q^{(t'\lambda,\;t't\mu-s'\mu)}\D(s's\lambda,t'\lambda)\D(s'\mu,t't\mu)
=q^{(s'\mu-t't\mu,\;s's\lambda)}\D(s'\mu,t't\mu)\D(s's\lambda,t'\lambda)
\label{eq: quantum commuting factor 2}
\end{align}
\ee
\end{prop}
Note that (ii) follows from by Proposition \ref{prop: p_n} and (i).
Note also that the both sides of \eqref{eq: quantum commuting factor 2}
are bar-invariant, and hence they are members of the upper global basis
as seen by Corollary \ref{cor:qcomm}.




\Prop\label{prop:Deprod}
For $\la,\mu\in\Pd$ and $s,t\in W$,
set
$\bg\bl u_{s\la}\tens (u_\la)^\rt\br=b_-\tens t_\la\tens b_{-\infty}$
and $\bg\bl u_{\mu}\tens (u_{t\mu})^\rt\br=b_{\infty}\tens t_{t\mu}\tens b_+$
with $b_{\mp}\in B(\pm\infty)$.
Then we have
$$\De{s\la,\la}\De{\mu,t\mu}=G^\up\bl\bg^{-1} (b_-\tens t_{\la+t\mu}\tens b_+)\br.$$
\enprop
\Proof

Recall that there is a
  pairing $(\scbul,\scbul):
\bl V(\la)\tensm V(\mu)\br\times \bl V(\la)\tensp V(\mu)\br\to \Q(q)$
 defined by
$(u\tensm  v,u'\tensp v')=(u,u')(v,v')$.
It satisfies
$$\bl P(u\tensm v), u'\tensp v'\br=\bl u\tensm v, \vphi(P)(u'\tensp v')\br
 \quad \text{for any} \ P \in \Uqg.
$$
For $u,u'\in V(\la)$ and $v,v'\in V(\mu)$,
we have
\begin{align*}
\lan \Phi(u\tens u'^\rt)\Phi(v\tens v'^\rt), P\ran&=
\bl u'\tensm v', P(u\tensp v)\br\\
&=\bl\vphi(P)(u'\tensm v'),u\tensp v\br.
\end{align*}
Hence for $P\in\U$, we have
\begin{align*}\lan \De{s\la,\la}\De{\mu,t\mu}, Pa_{\zeta}\ran
&=\delta(\zeta=s\la+\mu)
\bl\vphi(P)(u_{\la}\tensm u_{t\mu}),u_{s\la}\tensp u_{\mu}\br.
\end{align*}
If $Pa_\zeta=G^\low(\vphi(b))$ for $b\in B(\tU)$,
then
we have
$$\lan \De{s\la,\la}\De{\mu,t\mu},\vphi(G^\low(b))\ran
=\delta(\zeta=s\la+\mu)
\bl G^\low(b)(u_{\la}\tensm u_{t\mu}),u_{s\la}\tensp u_{\mu}\br.$$
The element
$G^\low(b)(u_{\la}\tensm u_{t\mu})$
vanishes or is a global basis of $V(\la)\tensm V(\mu)$
by Proposition~\ref{pro:gltens}.
Since $u_{s\la}\tensp u_{\mu}$ is a member of the upper global basis of
$V(\la)\tensp V(\mu)$,
 we have
$$\lan \De{s\la,\la}\De{\mu,t\mu},\vphi(G^\low(b))\ran
=\delta(\zeta=s\la+\mu)
\delta\bl \pi_{\la,t\mu}(b)=u_{s\la}\tens u_{\mu}\br.$$
Here $\pi_{\la,t\mu}\cl B(\tU a_{\la+t\mu})\to B(\la)\tens B(\mu)$
is the crystal morphism given in \eqref{eq: pi la wmu}.

Hence we obtain
$$\De{s\la,\la}\De{\mu,t\mu}=G^\up( \bg^{-1}( b)),$$
where $b\in B(\tU)$ is a unique element such that
$\bl G^\low(b)(u_{\la}\tensm u_{s\mu}), u_{s\la}\tensp u_{\mu}\br=1$.

On the other hand, we have
$G^\low(b_+)u_{t\mu}=u_{\mu}$ and
$G^{\low}(b_-)u_\la=u_{s\la}$.
The last equality implies $\vphi(G^{\low}(b_-))u_{s\la}=u_\la$ because
$(\vphi(G^{\low}(b_-))u_{s\la},u_\la)=(u_{s\la},G^{\low}(b_-)u_\la)=(u_{s\la},u_{s\la})=1$.
As seen in \eqref{eq:tUc}, we have
$$G^{\low}(b_-)G^\low(b_+)a_{\la+t\mu}-G^\low(b_-\tens t_{\la+t\mu}\tens b_+)
\in \Um_{>s\la-\la}\Up_{<\mu-t\mu}a_{\la+t\mu}.$$
Hence we obtain
\eqn
&&\bl G^\low(b_-\tens t_{\la+t\mu}\tens b_+)(u_{\la}\tensm u_{t\mu}),\;
u_{s\la}\tensp u_{\mu}\br\allowdisplaybreaks[1]\\
&&\hs{10ex}
=\bl G^{\low}(b_-)G^\low(b_+)(u_{\la}\tensm u_{t\mu}),\;
u_{s\la}\tensp u_{\mu}\br\allowdisplaybreaks[1]\\
&&\hs{20ex}
=\bl G^\low(b_+)(u_{\la}\tensm u_{t\mu}),\;
\vphi(G^\low(b_-))(u_{s\la}\tensp u_{\mu})\br
=1.
\eneqn
In the last equality, we used
$G^\low(b_+)(u_{\la}\tensm u_{t\mu})
=u_{\la}\tensm (G^\low(b_+)u_{t\mu})=u_{\la}\tensm u_\mu$
and
$\vphi(G^\low(b_-))(u_{s\la}\tensp u_{\mu})
=\bl\vphi(G^\low(b_-))u_{s\la})\tensp u_{\mu}=u_{\la}\tensp u_\mu$.

Hence we conclude that $b=b_-\tens t_{\la+t\mu}\tens b_+$.
\QED


Let
\eqn
&&\iota_{\la,\mu}\cl V(\la+\mu)\monoto V(\la)\tens V(\mu)\eneqn
be the canonical embedding and
\eqn
&&\oi_{\la,\mu}\cl B(\la+\mu)\monoto B(\la)\tens B(\mu)\eneqn
the induced crystal embedding.

\begin{lemma} \label{lem:oi la mu}
For $\lambda,\mu \in \wl^+$ and $x,y \in W$ such that $x \ge y$, we have
$$ u_{x\lambda} \otimes u_{y \mu} \in \overline{\iota}_{\lambda,\mu} (B(\lambda+\mu)) \subset B(\lambda) \otimes B(\mu).$$
\end{lemma}

\begin{proof}
Let us show by induction on $\ell(x)$, the length of $x$ in $W$. We may assume that $x \ne 1$. Then there exists $i \in I$ such that
$s_i x < x$. If $s_iy<y$, then $s_ix \ge s_iy$ and $\tilde{e}_i^{\max}(u_{x\lambda} \otimes u_{y\mu})= u_{s_ix\lambda} \otimes u_{s_iy\mu}$.
If $s_iy>y$, then $s_ix\ge y$ and
$\tilde{e}_i^{\max}(u_{x\lambda} \otimes u_{y\mu})= u_{s_ix\lambda} \otimes u_{y\mu}$. In
both cases,
$u_{x\lambda} \otimes u_{y \mu}$  is connected with an element of $\overline{\iota}_{\lambda,\mu}(B(\lambda+\mu))$.
\end{proof}


\Lemma \label{lem:Deprod}
For $\la, \mu\in\Pd$ and $w\in W$, we have
$$\De{w\la,\la}\De{\mu,\mu}=
G^\up\bl\oi_{\la,\mu}^{-1}(u_{w\la}\tens u_\mu)\tens u_{\la+\mu}{}^\rt\br.$$
\enlemma
\Proof We have
\eqn
&&\bg(u_{w\la}\tens u_\la^\rt\br=b_{w\la}\tens t_{\la}\tens b_{-\infty},\\
&&\bg(u_{\mu}\tens u_\mu^\rt\br=b_{\infty}\tens t_{\mu}\tens b_{-\infty},
\eneqn
where $b_{w\la}\seteq\oi_\la(u_{w\la})$.
Hence Proposition~\ref{prop:Deprod}
implies that
$$\De{w\la,\la}\De{\mu,\mu}=G^\up\bl\bg^{-1}(b_{w\la}\tens t_{\la+\mu}\tens b_{-\infty})\br.$$
Then, $\bg\bl\oi_{\la,\mu}^{-1}(u_{w\la}\tens u_\mu)\tens u_{\la+\mu}{}^\rt\br
=b_{w\la}\tens t_{\la+\mu}\tens b_{-\infty}$
 gives the desired result.
\QED
