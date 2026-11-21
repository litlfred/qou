---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-052-b4-compositions-of-bps-automorphisms
section_title: "B.4. Compositions of BPS automorphisms"
section_number: null
pages: 47-48
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
Let $(\Gamma,Z,\Omega)$ be a convergent BPS structure and fix  a  convex sector $\Delta\subset \bC^*$.  Fix $\epsilon>0$ and take $R>0$ as in Lemma \ref{sven}. Recall the  notion of the height of  a ray from Section \ref{raydiagram}. For each ray $\ell\subset \Delta$ define $M(\ell)>0$ as in the proof of Proposition \ref{prop} so that \eqref{thatwas} and \eqref{flfl} hold. Note that if a ray has height $> H$ then by the second inequality in \eqref{ein} we have  $\|\gamma\|>H/k_2$ for all nonzero terms in the sum \eqref{thatwas}. It follows that by increasing $R$ we can assume that for all $H>0$
\begin{equation}
\label{wa}\sum_{\height(\ell)> H} M(\ell)<\epsilon\cdot e^{-H}.\end{equation}

The proof of Proposition \ref{prop} shows that for each $S>R$ and each ray $\ell\subset \Delta$ the map $\bS(\ell)$ gives a well-defined embedding $U_\Delta(S+M(\ell))\to U_\Delta(S)$. 
For each $H>0$, the composition in anti-clockwise order of the $\Delta$-map  germs $\bS(\ell)$ corresponding to the finitely many rays $\ell\subset \Delta$ of height $\leq H$ therefore gives a well-defined map $U_\Delta(R+\epsilon)\to U_\Delta(R)$, and hence a  bounded $\Delta$-map germ
\[\bS(\Delta)_{\leq H}=\prod_{\height(\ell)\leq H} \bS(\ell)\in \Aut_\Delta(\bT).\]
The remaining task is to make sense of the limit of this map germ as $H\to \infty$. 
 
Suppose that a $\Delta$-map germ $f$ is well-defined on the open subset $U_\Delta(R)\subset \bT$. We define the $R$-norm of $f$ to be the infimum of the real numbers $K>0$ such that for all $\beta\in \Gamma$ and all $\xi\in U_\Delta(R)$
 \[e^{-K\cdot  \|\beta\|} \,|x_\beta(\xi)|\leq |x_\beta(f(\xi))|\leq e^{K\cdot \|\beta\|}\, |x_\beta(\xi)|.\]
 The proof of Proposition \ref{prop} shows that the $\Delta$-bounded map germ $\bS(\ell)$ is well-defined on $U_\Delta(R+\epsilon)$ and has norm $<M(\ell)$ there.


\begin{lemma}
\label{popo}
Suppose given a sequence  of invertible $\Delta$-bounded map germs $f_n\in G_\Delta(\bT)$, all defined on a fixed 
 $U_\Delta(R)$,  and such that the $R$-norm $d(m,n)$ of the composite $f_n^{-1}\circ f_m$ goes to zero as $\min(m,n)\to \infty$. Then the holomorphic maps $f_n$ have a uniform limit, which is itself an invertible $\Delta$-bounded map germ, and hence defines a limiting element $f_\infty\in G_\Delta(\bT)$.
\end{lemma}

\begin{proof}
By definition, for any $\xi\in U_\Delta(R)$ we have
\[e^{-d\cdot  \|\beta\|} \,|x_\beta(f_m(\xi))|\leq |x_\beta(f_n(\xi))|\leq e^{d\cdot \|\beta\|}\, |x_\beta(f_m(\xi))|,\]
where $d=d(m,n)$. Thus the $x_\beta(f_n(\xi))$ converge uniformly on compact subsets.
\end{proof}

\begin{prop}
\label{prop2}
The $\Delta$-map germs $\bS(\Delta)_{\leq H}$ have a well-defined   limit  \[\bS(\Delta)=\lim_{H\to \infty} \bS(\Delta)_{\leq H} \in \Aut_\Delta(\bT).\]
\end{prop}

\begin{proof}
Let us consider two finite compositions $P_1$ and $P_2$ of the maps $\bS(\ell)$ with $\ell\subset \Delta$ as above, which  differ by the insertion of one extra term. Thus the two products can be written in the form
$P_1=AC$ and $P_2=ABC$ with \[ A=\prod_i \bS(\ell_i), \quad B=\bS(\ell_j), \quad C=\prod_k \bS(\ell_k).\]
The  composite map germ
 $X=P_2 P_1^{-1}$ is well-defined on $U_\Delta(R+2\epsilon)$. We claim that it  has norm $<2M(\ell_j)$ there.
 Given  heights $H_2>H_1>0$ we can apply the claim repeatedly and use \eqref{wa} to deduce that
\[\bS(\Delta)_{\leq H_2} = \bS(\Delta)_{\leq H_1}\circ X(H_1,H_2),\]
where $X(H_1,H_2)$ has norm at most  $2\epsilon\cdot e^{-H_1}$. The result then follows from  Lemma \ref{popo}.

To prove the claim, note first that $X=ABA^{-1}$ is also the time 1 flow of a vector field on $\bT$, namely the  Hamiltonian vector field of the function $\DT(\ell_j)\circ A^{-1}$ pushed forward by the map $A$. We can therefore apply the same argument as in Proposition \ref{prop} provided we can bound the norm of this vector field as in  \eqref{co2}. To do this it is enough to bound the norm of the difference between the derivative of the map $A$ and the identity at points of $U_\Delta(R)$. This in turn is achieved by the same argument as Proposition \ref{prop} using the $p=2$ case of inequality \eqref{thatwas}. We leave the details to the reader.\end{proof}
