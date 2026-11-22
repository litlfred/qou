---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-021-33-proof-of-the-main-theorems
section_title: "Proof of the main theorems"
section_number: 3.3
pages: 43-45
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.957
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.proofmain}

We are now ready to give proofs of our main theorems.

\begin{proof}[Proof of Theorem~\ref{thm.HR} of Section~\ref{sub.habmod}]
Firstly, we see that $\calH_{R}\subseteq\calH_{R,0}$ as $f(q)=1$ is a global invertible
$L(0)$-section. For all $p$ prime to $\Delta$, the constant collection
$1$ is an invertible $L_p(0)$-section. Therefore, from Corollary~\ref{cor:unique.loc}
of Section~\ref{sub.habp} and the gluing condition~\eqref{eq:gluing} of
Definition~\ref{def.HRmod}, if $f\in\calH_{R,0}$, then $f\in\calH_{R_p^\wedge}$.






Varying
over all primes shows that $f\in\calH_{R}$.
This completes the proof that $\calH_{R,0}=\calH_{R}$.
The second statement follows from the fact that $\ve_m$ is
multiplicative while $D_{p}$ is additive and that the conditions
equation~\eqref{eq:gluing} and equation~\eqref{fxidef} are multiplicative as a
consequence. The final statement follows from the combination of the previous two.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm.2} of Section~\ref{sub.results}]
Firstly, we show that the constant term of $\Phitof_{A,z,m}(x)$
is $\ve_m(\xi)^{1/m}$ times an element of $\BK[\z_m]$.
For $m$ prime to $\Delta$ (where $\Delta$ includes the primes $2$ and $3$ and
finitely many other primes that depend only on the number field $\BK$),
this follows from Theorem 1.6 and equation (14) of~\cite[Thm.1.6]{CGZ} combined
with Hutchinson~\cite{Hutchinson}.

Secondly, we will prove that for a system of $q$-difference equations
associated to the combination in equation~\eqref{eq:gluing}
there is a unique solution in formal power series in $t$. 
We will explicitly describe the case when $N=1$.
(We again omit the case when $N>1$, since it completely analogous but notationally
heavier.) To do this, we will use standard methods in the study of $q$-holonomic
modules. Recall the $q$-difference equation~\eqref{PhiAshift} and define
\be
\psi_{A,\mu}(t,q) \= F_{A}(q^\mu t,q)\,.
\ee
Fix $\gamma\in\BZ_{>0}$ and consider the function
\be
(\mu,\nu,t) \mapsto
\psi^{(\gamma)}_{A,\mu,\nu}(t,q) \=
\psi_{A,\mu_1}(t,q^\gamma)\cdots \psi_{A,\mu_\gamma}(t,q^{\gamma})
\psi_{A,\nu}(t,q^{-1})\,,
\ee
where $\mu \= (\mu_1,\dots,\mu_\gamma) \in \BZ^\gamma$ and $\nu \in \BZ$.
It satisfies $\gamma+2$ equations, corresponding to the number of variables:
\be
\label{eq:qdiff.proofs}
\begin{aligned}
\psi^{(\gamma)}_{A,\mu,\nu}(t,q)
-
\psi^{(\gamma)}_{A,\mu+\delta_i,\nu}(t,q)
&\=
(-1)^Aq^{A\gamma}t\psi^{(\gamma)}_{A,\mu+A\delta_i,\nu}(t,q)\qquad
(i=1,\cdots,\gamma)\,,\\
\psi^{(\gamma)}_{A,\mu,\nu}(t,q)
-
\psi^{(\gamma)}_{A,\mu,\nu+1}(t,q)
&\=
(-1)^Aq^{-A}t\psi^{(\gamma)}_{A,\mu,\nu+A}(t,q)\,,\\
\psi^{(\gamma)}_{A,\mu}(qt,q)
&\=
\psi^{(\gamma)}_{A,\mu+1,\nu-1}(t,q)\,.
\end{aligned}
\ee
These equations have a unique solution for power series in $t$
of the form $1+\mathrm{O}(t)$. This follows from the fact
that the first two equations imply that the coefficient of $t^k$
in $\psi^{(\gamma)}$ is constant in $\mu,
\nu$ modulo coefficients
of smaller powers of $t$. Assuming this, the last equation
implies that this coefficient multiplied by $q^k-1$ is given entirely
by combinations of lower order terms. Therefore,
everything is determined by the coefficient of $t^0$.

From the explicit formulas of equation~\eqref{PhiFGIdef} and
equation~\eqref{Ikdef}, Theorem~\ref{thm.fgi.is.admis} of Section~\ref{sub.synthesis},
Theorem~\ref{thm.FGI2} of Section~\ref{sub.results}, and Galois invariance under
$z^{1/m}\mapsto \z_mz^{1/m}$; we see that
$\psi^{(\gamma)}_{A,\mu,\nu}(t^{1/m},\z_m+x)\in S_p^{(m)}[\![x]\!]$,
for all primes $p$ prime to $\Delta$ and $m$ prime to $\gamma$. Therefore,
$\psi^{(\gamma)}_{A,\mu,\nu}(t^{1/m},\z_m+x)\in S^{(m)}[\![x]\!]$.
Moreover, since there is a unique solution to the equations~\eqref{eq:qdiff.proofs},
if we $p$-complete and re-expand by $x\mapsto x+\z_{pm}-\z_m$
then we must find an equality after applying a Frobenius, which maps $t\mapsto t^p$.
Therefore, these equalities persist when we specialise $t=1$.
This proves that $\Phitof_{A,z}$ satisfies equation~\eqref{eq:gluing}.

For the rest of the proof, we fix a positive integer $m$, a prime $p$ with
$(m,p)=1$ and a congruence class $k \in (\BZ/m\BZ)^N$. Theorems~\ref{thm.FGI2} of
Section~\ref{sub.results} and~\ref{thm.fgi.is.admis} of Section~\ref{sub.synthesis}
imply that each term $\CS_{A,m,k}(t,x)$ of
equation~\eqref{FGIcong}, specialised to $t=1$, satisfies equation~\eqref{dphiA},
which is an essentially equation~\eqref{fxidef} restricted to a disc. 







Summing up using~\eqref{PhiFGIdef} and~\eqref{FGIcong}, we obtain that 
\be
\Phitof_{A,m}^\FGI(1,x) \=\!\!\!\!
\sum_{k \in (\BZ/m\BZ)^N}
\frac{(-1)^{\mathrm{diag}(A)\cdot k}q^{\frac{1}{2}(k^t A k + \mathrm{diag}(A)\cdot k)}}
{(q;q)_{k_1}\cdots(q;q)_{k_N}}\CS_{A,m,k}(1,q)\,,\quad q\=\z_{m}+x \,.
\ee
It follows that $\Phitof_{A}^\FGI(1,q)$ gives an element of the
module $\calH_{R[\delta^{-1/2}]^\wedge_p[\z_m,z^{1/m}],\xi}$ for $q$-restricted
to the disc around $\z_m$.
Finally, from the invariance under $z^{1/m}\mapsto\z_m z^{1/m}$ from
Lemma~\ref{lem.PhiA} of Section~\ref{sub.FGI}, we see that $\Phitof_{A,z}(q)$
descends to an element of $\calH_{R[\delta^{-1/2}]^\wedge_p,\xi}$ restricted to
the disc around $\z_m$.

Varying over all $m$ prime to $\Delta$ and combining this with the previous
result that equation~\eqref{eq:gluing} is satisfied, we conclude that
$\Phitof_{A,z}(q)\in\calH_{R[\delta^{-1/2}],\xi}|_\Delta$.
\end{proof}

\begin{proof}[Proof of Corollary~\ref{cor.3} of Section~\ref{sub.results}]
This would immediately follow from Theorem~\ref{thm.2} of Section~\ref{sub.results},
Theorem~\ref{thm.HR} of Section~\ref{sub.habmod}, and Proposition~\ref{prop.HRxi}
of Section~\ref{sub.habmod}; if we did not have the technical
assumption on the order of roots of unity being prime to $\Delta$.

However, equation~\eqref{symhab} does immediately follow from the proof of
Theorem~\ref{thm.2} of Section~\ref{sub.results} that showed $\Phitof_{A,z}$ satisfies
equation~\eqref{eq:gluing}, which in particular holds when $\gamma=1$.

For part (b), a weaker statement asserting that
$\Phitof_{A,z}(q)^{r} \in \calH_{R[1/\sqrt{\delta}]}|_\Delta$ follows from
Theorem~\ref{thm.2} of Section~\ref{sub.results} and Theorem~\ref{thm.HR} of
Section~\ref{sub.habmod}. To replace $\calH_{R[1/\sqrt{\delta}]}|_\Delta$
by $\calH_{R[1/\sqrt{\delta}]}$, note the surjective map $K_3(\BK) \to B(\BK)$
of Suslin (see e.g.,~\cite[Eqn.(1.1)]{Zickert:bloch}). Hence, if $r\xi=0$, then
the image of $\xi$ in the Bloch group can be written as a sum of $5$-term relations
in the Bloch group. Then the identity of~\cite{KMS} that was used in~\cite{CGZ}
shows that the constant term at $\z_m$ is in $S^{(m)}$.
\end{proof}

\begin{remark}
\label{rem.desc}
In fact, the specialisation $t=q^\nu$ for $\nu \in \BZ^N$ (i.e., $t_j=q^{\nu_j}$
for integers $\nu_j$) defines an element $\Phitof_{A,z,\nu}(q) \in
\calH_{R[1/\sqrt{\delta}],\xi}|_\Delta$.
The proof is identical to the proof of Theorem~\ref{thm.2} of
Section~\ref{sub.results} and is omitted.
\end{remark}

\begin{proof}[Proof of Proposition~\ref{prop.HRxi} of Section~\ref{sub.habmod}]
The proofs of the proposition are all elementary and outlined as follows:
\begin{itemize}
\item
  Property (a) and (d) follow from the $\chi^{-1}$ equivariance of $\ve$.
\item
  Property (b) follows from Theorem~\ref{thm.HR} of Section~\ref{sub.habmod}.
\item
  Property (c) is trivial and follows from the definition of $\gamma^{*}$ just prior
  to the proposition.
\item
  Property (e) this property follows from the fact that, varying over $\gamma,\gamma'$,
  the collections $f(q^{\gamma_1})\cdots f(q^{\gamma_n})f(q^{-\gamma_1'})
  \cdots f(q^{-\gamma_{n'}'})$,
  where $\sum_{k}\gamma_k^{-1}-\sum_k\gamma_{k}'^{-1}=0$ determine
  $f(q)$. Alternatively, one could use the remark
  
  of Section~\ref{sub.habp} to connect
  various roots of unity.
  \item Property (f) follows from the fact that the constants
  $f_m(0) \in R^\wedge_p[\z_m,\ve_m^{1/m}]$ for all $m$ and
  $p$ with $(mp,\Delta)=1$.  
\end{itemize}
\end{proof}

An immediate corollary of part (f) is the following result, which even in very simple
instances like the $4_1$-knot
seems very difficult to prove directly.

\begin{corollary}
For $m$ prime to $\Delta$, the constants $U_{m}^\FGI(1)$ from equation
~\eqref{Umtdef} are $\Delta$-integral.
\end{corollary}
