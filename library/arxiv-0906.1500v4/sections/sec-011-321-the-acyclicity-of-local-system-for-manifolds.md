---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-011-321-the-acyclicity-of-local-system-for-manifolds
section_title: "The acyclicity of local system for manifolds with tori--boundary"
section_number: 3.2.1
pages: 10-12
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:acyclicity_boundary}

In this section we suppose that the representations $\rho\colon
\pi_1(M) \to \SL$ under consideration satisfy Assumption~$(A_\rho)$.

We prove that the twisted chain complex $C_*(M; \sllmt_\rho)$ is
acyclic in that case.


\begin{proposition}\label{prop:acyclic}
  We have $H_*(M; \sllmt_\rho) = 0$.
\end{proposition}

The proof of Proposition~\ref{prop:acyclic} is based on Milnor's
construction~\cite{Milnor:1968}, but the techniques are rather different,
actually we use the restriction map induces by the inclusion $\partial M \hookrightarrow M$.

Let $\infcover{M}$ denote the infinite cyclic covering of $M$.
We have $\ker (\mathrm{pr}_n \circ \varphi) = \pi_1(\infcover{M})$ where
$\mathrm{pr}_n \colon \ZZ^n \to \ZZ$ denotes the projection by substituting $t_1 = \cdots = t_{n-1} = 1$.
We use the symbol $F$ for the fraction field $\CC(t_1, \ldots, t_{n-1})$.
The action of
$\otAd{\varphi}{\rho^{-1}}$ of $\CC[t_n, t_n^{-1}] \otimes_{\CC} \msll{F}_\rho$
is given by the tensor product of $\mathrm{pr}_n \circ \varphi$ and
$\otAd{(\mathrm{pr}_{1, \ldots, n-1}) \circ \varphi}{\rho^{-1}}$
where $\mathrm{pr}_{1, \ldots, n-1}$ denotes the projection by substituting $t_n = 1$.
Moreover, one can observe that under the inclusion $\ZZ[t_n, t_n^{-1}] \to \CC[t_n, t_n^{-1}]$,
$$
C_*(\infcover{M}; \msll{F}_\rho) \simeq 
C_*(M; \CC[t_n, t_n^{-1}] \otimes_\CC \msll{F}_\rho).
$$ 
The Milnor sequence:
\begin{equation}\label{eqn:MilnorSq}
    0 \to
    C_*(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n - 1} 
    C_*(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n = 1} 
    C_*(M; \msll{F}) \to
    0
\end{equation}
 induces the
long exact sequence in twisted homology:
\begin{align}\label{eqn:MilnorSq2}
    0 &\to 
    H_2(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n - 1} 
    H_2(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n = 1} 
    H_2(M; \msll{F}_\rho)  \\
    & \xrightarrow{\delta} 
    H_1(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n - 1}  
    H_1(\infcover{M}; \msll{F}_\rho) \xrightarrow{t_n = 1} 
    H_1(M; \msll{F}_\rho)  \to
    0. \nonumber
\end{align}

Proposition~\ref{prop:acyclic} is a consequence of the following lemma.
\begin{lemma}\label{lemma:free_bound}
  Let $F$ be the fraction field $\CC(t_1, \ldots, t_{n-1})$.  The
  homology group $$H_*(M; \CC[t_n, t_n^{-1}] \otimes_\CC \msll{F}_\rho)$$ has
  no free part.
\end{lemma}
\begin{proof}[Proof]
  The proof is by induction on the number $n$ of variables $t_1, \ldots, t_n$. 
  The first step is to prove the lemma in the case of a
  single variable $t$.

\medskip

\noindent \textbf{(i)}. 
We prove that \emph{$H_*(M; \CC[t, t^{-1}] \otimes_\CC \sllrho)$ has no free part.}
  
Let $A_\ell$ be the annulus in $\infcover{M}$ over $T_\ell^2$ and $b$ the
number of the components of $\bord M$. The Milnor sequence for the
boundary $\partial M$ induces the first line of the following
commutative diagram, the second one is the exact
sequence of Equation~(\ref{eqn:MilnorSq2}), and the diagram is commutative because
all the constructions are natural:
$$
\xymatrix@-.7pc{ 
  0 \ar[r] & 
  \displaystyle{\mathop{\oplus}_{\ell=1}^{b} H_2(T_\ell^2; \sllrho)} \ar[r]^-{\delta_\bord} \ar[d]^-\simeq & 
  \displaystyle{\mathop{\oplus}_{\ell=1}^{b} H_1(A_\ell; \sllrho)}  \ar[r]^{t - 1} \ar[d] & 
  \displaystyle{\mathop{\oplus}_{\ell=1}^{b} H_1(A_\ell; \sllrho)} \ar[r]^-{t = 1} \ar[d] & 
  \cdots \\
  \cdots \ar[r]^-{t=1} & 
  H_2(M; \sllrho) \ar[r]^-{\delta} &
  H_1(\infcover{M}; \sllrho) \ar[r]^{t - 1} & 
  H_1(\infcover{M}; \sllrho) \ar[r]^-{t = 1} & 
  \cdots }
$$


The proof is by contradiction, so we make the following hypothesis: 
 
 
\begin{center} 
{\noindent ($\mathcal{H}$) \quad
    \emph{
      $H_1(\infcover{M}; \sllrho) \simeq H_1(M; \CC[t, t^{-1}] \otimes_\CC \sllrho)$ 
       has a free part of rank $r>0$}. 
     }
\end{center}

\noindent First observe that (because $\chi(M) = 0$ and $H_0(\infcover{M}; \sllrho) = 0$): 
\begin{equation}\label{eqn:rank}
  \mathrm{rk} \, H_2(\infcover{M}; \sllrho) = 
  \mathrm{rk} \, H_1(\infcover{M}; \sllrho) = r.
\end{equation}
 
Our proof is as follows and based on the following technical claim.
\begin{claim}\label{claim:map_Delta}
  The map 
  $$\delta_{\bord} : 
    \bigoplus_{\ell=1}^{b} H_2(T_\ell^2; \sllrho) \to
    \bigoplus_{\ell=1}^{b} H_1(A_\ell; \sllrho)$$
  in the previous diagram is
  non--trivial, and moreover for all $\ell$, 
  $\delta_{\bord}\left( \bbrack{P_\ell^\rho \otimes T^2_\ell} \right)$  
  is non zero.
\end{claim}
\begin{proof}[Proof of the Claim]
  Let $P_\ell^\rho$ $(1 \myleq \ell \myleq b)$ be the chosen invariant
  vector in $\sll$.  Since $\bord M = \cup_{\ell=1}^b T^2_\ell$, we
  have $H_0(\partial M; \sllrho) = \bigoplus_{\ell=1}^{b}
  H_0(T^2_\ell; \sllrho).$ It follows from our assumptions that
  $H_2(M; \sllrho)$ is generated by the vectors $\bbrack{P_\ell^\rho
    \otimes T^2_\ell}$ $(1 \myleq \ell \myleq b)$ and $H_1(M;
  \sllrho)$ is also generated by the vectors $\bbrack{P^\rho_\ell
    \otimes \lambda_\ell}$ $(1 \myleq \ell \myleq b)$.  The space
  $H_2(T_\ell^2; \sllrho)$ is generated by $\bbrack{P_\ell^\rho
    \otimes T^2_\ell}$ and we have:
  \begin{equation}\label{eqn:partial}
    \delta_{\partial}\left( 
      \bbrack{P_\ell^\rho \otimes T^2_\ell} 
     \right) = 
       (1 + t + \cdots + t^{a_\ell - 1})
       \bbrack{P^\rho_\ell \otimes \lambda_\ell},
  \end{equation}
  where $\varphi(\mu_\ell) = t^{a_\ell}$, $a_\ell>0$.  Next it is easy to observe
  that each $(\sum_{k=0}^{a_\ell - 1} t^k) \bbrack{P^\rho_\ell \otimes \lambda_\ell}$ 
  is a non zero element in $H_1(\infcover{M}; \sllrho)$,
  because its image by the map $(t=1)$ is 
  $a_\ell \bbrack{P^\rho_\ell \otimes \lambda_\ell}$, 
  which is non zero in $H_1(M; \sllrho)$. 
  This proves that $\delta_{\bord M} \ne 0$.
\end{proof}

Using the exactness of the Milnor sequence~(\ref{eqn:MilnorSq2}) and
 Equation~(\ref{eqn:rank}), we know that
$$
\im (t=1) \simeq 
  H_2(\infcover{M}; \sllrho)/{\left( {(t-1)H_2(\infcover{M}; \sllrho} \right)} \ne 0.
$$ 
Since $\im (t=1) = \ker \delta$, we deduce that $\ker \delta \ne 0$. 
Let $\xi$ be a non zero element in $\ker \delta$ and write it in
$H_2(M; \sllrho)$ as follows:
\[
\xi = \sum_{\ell=1}^{b} b_\ell \bbrack{P^\rho_\ell \otimes T^2_\ell}.
\]
One has (see Equation~(\ref{eqn:partial})):
\[
\delta_{\partial}(\xi) = 
\sum_{\ell=1}^{b} b_\ell
(1 + t + \cdots + t^{a_\ell - 1})
\bbrack{P^\rho_\ell \otimes \lambda_\ell}
\]
and thus,
\[
(t=1) \circ \delta_{\partial} (\xi) = 
  \sum_{\ell=1}^{b} a_\ell b_\ell \bbrack{P^\rho_\ell \otimes \lambda_\ell}.
\]
Now we prove by contradiction that $\delta_{\partial}(\xi)$ is non
zero. If $\delta_{\partial}(\xi) = 0$, then its image by $(t=1)$ is
also zero, so $a_\ell = 0$ or $b_\ell = 0$, for all $i$. Since $a_\ell > 0$,
for all $i$, we deduce that $b_\ell = 0$, for all $i$. So that, $\xi =
0$, which is a contradiction and thus $\delta_{\partial}(\xi) \ne 0$.

With our assumption we have 
$(t=1)\circ \delta_\partial(\xi) = 
  \sum_{\ell=1}^{b} a_\ell b_\ell \bbrack{P^\rho_\ell \otimes \lambda_\ell}$, 
and this element is non zero in $H_1(\infcover{M}; \sllrho)$ as we seen. 
But this is in contradiction with the fact that $\xi$ is chosen in $\ker \delta_\partial$, 
so that the
hypothesis ($\mathcal{H}$) on the free part of 
$H_1(M; \CC[t, t^{-1}] \otimes_\CC \sllrho)$ is absurd and 
proves Lemma~\ref{lemma:free_bound} in the case of a single variable.

\medskip 

\noindent \textbf{(ii)}. 
Now we 
\emph{finish the proof by induction on  the number of variables}, 
and suppose that
$$H_*(M; \CC[t_{n-1}, t_{n-1}^{-1}] \otimes_\CC \msllrho{t_1, \ldots, t_{n-2}})$$ 
has no free part. 
Thus, $H_*(M; \msllrho{F})$ vanishes and 
the long exact sequence~(\ref{eqn:MilnorSq2}) induces
the isomorphism:
\[
  0 \to 
  H_*(\infcover{M}; \msllrho{F}) \xrightarrow[\simeq]{t_n - 1}  
  H_*(\infcover{M}; \msllrho{F}) \to
  0.
\]
As a conclusion, $C_*(M; \msllrho{F})$ is acyclic which proves Lemma~\ref{lemma:free_bound}.

\end{proof}

Thus, the twisted complex $C_*(M; \sllmt_\rho)$ is acyclic and the torsion is
well--defined (even its sign if we provide $M$ with its natural
homology orientation, see e.g.~\cite{Turaev:2002}):
\begin{equation}\label{def:polytorsion}
  \PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, \ldots, t_n)
  =
  \tau_0 \cdot 
  \Tor{C_*(M;\sllmt_\rho)}{\cbasis{*}}{\emptyset} 
    \in \CC(t_1, \ldots, t_n).
\end{equation}
Here $ \tau_0 = \mathrm{sgn} (\Tor{C_*(M; \IR)}{\cbasis{*}_\IR}{\hbasis{*}_\IR})$.
