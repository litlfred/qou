---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-025-94-generalized-t-system
section_title: "Generalized T-system"
section_number: 9.4
pages: 74-75
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.939
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
The $T$-system in \S \ref{subsubsec: T-system} can be interpreted as  a system of equations among the three products of elements
in $\B^\up(A_q(\g))$ or $\B^\up(A_q(\n))$.
In this subsection, we introduce  another among the three products
of elements in $\B^\up(A_q(\g))$, called {\em a generalized $T$-system}.

\begin{prop} \label{prop: g T-system D}
Let $\mu \in W \varpi_i$ and set $b = \oi_{\varpi_i}(u_\mu) \in B(\infty)$. Then we have
\begin{equation}\label{eq: G t-sys}
\begin{aligned}
\Delta(\mu,s_i\varpi_i)\Delta(\varpi_i,\varpi_i) & = q_i^{-1}
G^\up\left( \oi^{-1}_{\varpi_i,\varpi_i}(u_\mu \otimes u_{\varpi_i})
\otimes \big( \oi^{-1}_{\varpi_i,\varpi_i}(u_{s_i\varpi_i} \otimes u_{\varpi_i}) \big)^\ri \right) \\
& \hspace{10ex} +G^\up \left( \oi_{\varpi_i+s_i\varpi_i}^{-1}(\widetilde{e^*_i}b) \otimes u^\ri_{\varpi_i+s_i\varpi_i} \right).
\end{aligned}
\end{equation}
\end{prop}

Note that if $\mu = \varpi_i$, then $b=1$ and the last term in \eqref{eq: G t-sys} vanishes. If $\mu \ne \varpi_i$, then
$\ve_i^*(b)=1$ \ and $\oi_{\varpi_i+s_i\varpi_i}^{-1}(\te_i^* b) \in B(\varpi_i+s_i\varpi_i)$,  $u_\mu \otimes u_{\varpi_i} \in
\oi_{\varpi_i,\varpi_i}B(2\varpi_i)$.

\begin{proof}
In the sequel, we omit $\oi^{-1}_{\varpi_i,\varpi_i}$ for the sake of simplicity. Set
$$  u = \Delta(\mu,s_i\varpi_i)\Delta(\varpi_i,\varpi_i)- q_i^{-1}
G^\up\left( (u_\mu \otimes u_{\varpi_i}) \otimes
(u_{s_i\varpi_i} \otimes u_{\varpi_i})^\ri  \right).$$
 Then $\wt_\ri(u)=\lambda\seteq\varpi_i+s_i\varpi_i$.

It is obvious that we have $uf_j=0$ for $j \ne i$. Since $\te_i(u_{s_i\varpi_i} \otimes u_{\varpi_i})= u_{\varpi_i} \otimes u_{\varpi_i}$,
we have
\begin{align*}
G^\up\left( (u_\mu \otimes u_{\varpi_i}) \otimes (u_{s_i\varpi_i} \otimes u_{\varpi_i})^\ri  \right)f_i  & =
G^\up\left( (u_\mu \otimes u_{\varpi_i}) \otimes (u_{\varpi_i} \otimes u_{\varpi_i})^\ri  \right) \\
& = \Delta(\mu,\varpi_i)\Delta(\varpi_i,\varpi_i) \\
& = G^\up(u_\mu \otimes u^\ri_{\varpi_i})G^\up(u_{\varpi_i} \otimes u^\ri_{\varpi_i}).
\end{align*}
Here the second equality follows from Lemma~\ref{lem:Deprod} and the third follows from Proposition \ref{prop:Agglobal}.
On the other hand, we have
\begin{align*}
\left( \Delta(\mu,s_i\varpi_i)\Delta(\varpi_i,\varpi_i)   \right) f_i & =  \left( \Delta(\mu,s_i\varpi_i)f_i \right)
\left(\Delta(\varpi_i,\varpi_i)t_i^{-1}\right) \\ & = q_i^{-1}\Delta(\mu,\varpi_i)\Delta(\varpi_i,\varpi_i).
\end{align*}
Hence we have $uf_i=0$. Thus, $u$ is a lowest weight vector of wight $\lambda$ with respect to the right action of
$U_q(\g)$. Therefore there exists some $v \in V(\lambda)$ such that
$$u=\Phi(v \otimes u_\lambda^\ri).$$
Hence we have $p_\n(u)=\iota_\lambda(v) \in A_q(\n)$. On the other hand, we have
\begin{align*}
p_\n\left( \Delta(\mu,s_i\varpi_i)\Delta(\varpi_i,\varpi_i) \right) & =
p_\n\left(\Delta(\mu,s_i\varpi_i) \right) p_\n\left(\Delta(\varpi_i,\varpi_i)\right) \\
& = \D(\mu,s_i\varpi_i)=G^{\up}(\te_i^*b) \\
& = \iota_\lambda\left(G_\lambda^\up \big(\oi_\lambda^{-1}(\te_i^* b) \big) \right)
\end{align*}
Note that since $\ve_i^*(\te_i^*b) =0$ and $\ve_j^*(\te_i^*b) \le -\lan h_j,\alpha_i \ra$ for $j \ne i$, we have
$\te_i^*b \in \oi_\lambda(B(\lambda))$.

Hence in order to prove our assertion, it is enough to show that
$$
p_\n\left( G^\up\big( (u_\mu \otimes u_{\varpi_i}) \otimes (u_{s_i\varpi_i} \otimes u_{\varpi_i})^\ri  \big) \right) =0.
$$
This follows from Proposition \ref{prop: nonzero elt} and
\begin{align} \label{eq: kernel}
\oi_\g\left( (u_\mu \otimes u_{\varpi_i}) \otimes (u_{s_i\varpi_i} \otimes u_{\varpi_i})^\ri \right) = b \otimes t_\lambda \otimes \te_ib_{-\infty}.
\end{align}

Let us prove \eqref{eq: kernel}. Since
$$
(u_\mu \otimes u_{\varpi_i}) \otimes (u_{s_i\varpi_i} \otimes u_{\varpi_i})^\ri
= \te_i^*
\bl(u_\mu \otimes u_{\varpi_i}) \otimes (u_{\varpi_i} \otimes u_{\varpi_i})^\ri\br,
$$
the left-hand side of \eqref{eq: kernel} is equal to
$$
\te_i^*\left(\oi_\g\big( (u_\mu \otimes u_{\varpi_i}) \otimes (u_{\varpi_i} \otimes u_{\varpi_i})^\ri \big)\right)
= \te_i^*(b \otimes t_{2\varpi_i}\otimes b_{-\infty}).
$$

Since $\ve_i^*(b)=1 < \lan h_i,2\varpi_i \ra=2$, we obtain
\begin{align*}
&\te_i^*\left(b \otimes t_{2\varpi_i}\otimes b_{-\infty}\right)
= b \otimes t_{2\varpi_i-\al_i}\otimes \te_i^* b_{-\infty}
=b \otimes t_\lambda \otimes \te_ib_{-\infty}.  \qedhere
\end{align*}
\end{proof}
