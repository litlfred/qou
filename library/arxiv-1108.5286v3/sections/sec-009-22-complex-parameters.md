---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-009-22-complex-parameters
section_title: "Complex parameters"
section_number: 2.2
pages: 21-24
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.993
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
\label{sec:complex}

Everything we discussed in the previous subsection has a natural analogue for graded 
Hecke algebras. The condition $q$ positive translates to $k$ real valued, but with the 
scaling isomorphisms \eqref{eq:1.3} we can also reach complex parameters.

In the graded setting we have to replace $T^P$ und $T^P_{un}$ by the vector spaces 
$\mf t^P$ and $i \mf a^P$. In the groupoid $\mc G$ we have to omit the parts $K_P$, 
so we get a groupoid $\mc W'$ with
\[
\mc W'_{PQ} = \{ g \in \Gamma \ltimes W \mid g(P) = Q \} \qquad P,Q \subset \Delta .
\]

\begin{thm}\label{thm:6.4}
Suppose that $k_\alpha \in \R$ for all $\alpha \in R$. 
There exists a natural $\Q$-linear bijection
\[
\zeta^\vee : G_\Q (\mh H \rtimes \Gamma) \to G_\Q (S (\mf t^*) \rtimes W')
\]
such that:
\begin{enumerate}[\textup{(}1\textup{)}]
\item $\zeta^\vee (\pi)$ is a tempered virtual $S (\mf t^*) \rtimes W'$-representation 
if and only if $\pi$ is a tempered virtual $\mh H \rtimes \Gamma$-representation.
\item $\zeta^\vee$ commutes with parabolic induction, in the sense that for a subgroup 
$\Gamma'_P \subset \Gamma_P$, a tempered $\mh H^P \rtimes \Gamma'_P$-representation 
$\pi$ and $\lambda \in \mf t^{W(R_P) \rtimes \Gamma'_P}$ we have
\[
\zeta^\vee \big( \mr{Ind}_{\mh H^P \rtimes \Gamma'_P}^{\mh H \rtimes \Gamma} 
(\pi \circ \phi_\lambda) \big) = 
\mr{Ind}_{S (\mf t^*) \rtimes (W (R_P) \rtimes \Gamma'_P)}^{S (\mf t^*) 
\rtimes (W \rtimes \Gamma)} (\zeta^\vee (\pi) \circ \phi_\lambda) ;
\]
\item if $\lambda \in i \mf a$ and $\pi$ is a virtual representation with central character in 
$W' \lambda + \mf a$, then so is $\zeta^\vee (\pi)$;
\item if $\pi$ is tempered and admits a real central character, then 
$\zeta^\vee (\pi) = \pi \circ m_0$ with $m_0$ as in \eqref{eq:1.3}.
\end{enumerate}
\end{thm}
\emph{Proof.}
For $\mh H \rtimes \Gamma$-representations which admit a central character whose component
in $i \mf a$ is small, this follows from Theorems \ref{thm:6.2} and \ref{thm:2.2}. The extra
condition (4) is actually the starting point for the construction of $\zeta^\vee$, see 
\cite[Section 2.3]{Sol-Irr}. We can generalize this to all $\mh H \rtimes \Gamma$-representations
via the scaling isomorphisms
\[
m_\ep : \mh H (\tilde{\mc R},\ep k) \rtimes \Gamma \to \mh H (\tilde{\mc R},k) \rtimes \Gamma
\]
for $\ep > 0 . \qquad \Box$
\\[2mm]

An induction datum for $\mh H$ is a triple $(P,\delta,\lambda)$ such that 
$P \subset \Delta, \delta$ is a discrete series representation of $\mh H_P$ and 
$\lambda \in \mf t^P$. Suppose that $\mu \in i \mf a^P$ and that $\rho$ is an 
irreducible direct summand of the representation 
$\mr{Ind}_{\mh H^P}^{\mh H^P \rtimes \Gamma_{(P,\delta,\mu)}}(\delta \circ \phi_\mu)$ (which
is completely reducible). We abbreviate $\Gamma_\rho = \Gamma_{(P,\delta,\mu)}$
and $\mf t^\rho = (\mf t^P)^{\Gamma_\rho}$. We say that 
\begin{equation} \label{eq:6.13}
\big\{ \pi_\rho (\lambda) := \mr{Ind}_{\mh H^P \rtimes \Gamma_\rho}^{\mh H \rtimes \Gamma}
(\rho \circ \phi_\lambda) \mid \lambda \in \mf t^\rho \big\}
\end{equation}
is an analytic family of $\mh H \rtimes \Gamma$-representations. Notice that 
\begin{equation}\label{eq:6.6}
\pm \mu \in \mf t^\rho 
\end{equation}
and that the central character of $\pi_\rho (-\mu)$ equals the central character of 
$\pi^\Gamma (P,\delta,0) = \mr{Ind}_{\mh H^P}^{\mh H \rtimes \Gamma} \delta$. Moreover the
weights satisfy an integrality property with respect to 
\[
\Z k := \Z \{ k_\alpha \mid \alpha \in R \} . 
\]
By \cite[Theorem A.7]{Opd-Sp} every $S (\mf t_P^*)$-weight $\nu$ of $\delta$ is a residual 
point for $(\tilde{\mc R}_P, k_P)$. The classification of such distinguished points 
in \cite[Section 4]{HeOp} shows that $\alpha (\nu) \in \Z k_P$ for all $\alpha \in R_P$.
By \cite[Theorem 6.4]{BaMo2} this property is preserved under induction, that is, 
$\alpha (\nu) \in \Z k$ for every $\alpha \in R$ and every $S (\mf t^*)$-weight $\nu$ of 
$\mr{Ind}_{\mh H^P}^{\mh H \rtimes \Gamma} \delta$. We conclude that all 
$S (\mf t^*)$-weights of $\pi_\rho (\lambda)$ lie in
\begin{equation}\label{eq:6.4}
W' (\lambda + \mu) + \mr{Hom}(\Z R, \Z k) ,
\end{equation}
where we consider $\mr{Hom}(\Z R, \Z k)$ as a lattice in $\mf a_R \subset \mf t$.
 
To the analytic family $\pi_\rho$ we associate the group
\[
\mc W'_\rho = \big\{ g \in \mc W' \mid g(P) = P , \delta \circ \psi_g^{-1} \cong \delta , 
g \text{ stabilizes } \{ \pi_\rho (\lambda) \mid \lambda \in i \mf a^\rho \} \big\}. 
\]
\texttt{Correction (2022):} The new comments on pages \pageref{eq:smoothFamily}, 
\pageref{eq:6.2} and \pageref{eq:6.12} 
also apply to the below construction and to Corollary \ref{cor:6.5}. If we can instead use one 
of the good cases listed on page \pageref{eq:6.12}, the remainder of the paper holds for those
families of $\mh H \rtimes \Gamma$-representations. Otherwise, there is still a satisfactory 
substitute for Corollary \ref{cor:6.5} in terms of families of virtual $\mh H \rtimes 
\Gamma$-representations, worked out in \cite{SolHHtwisted}.\\[2mm]

\noindent
Our discussion of $\C [X] \rtimes W' = \mc O (T) \rtimes W'$ before Theorem \ref{thm:6.2} 
applies just as well to $\mh H(\tilde{\mc R},0) \rtimes \Gamma = S (\mf t^*) \rtimes W'$.
The considerations that lead to Lemma \ref{lem:6.3} also show:

\begin{cor}\label{cor:6.5}
There exist analytic families of $\mh H \rtimes \Gamma$-representations $\pi_{\rho_w}$ for
$w \in \langle W' \rangle$, such that:
\enuma{
\item The parameter space $\mf t^{\rho_w} / \mc W'_{\rho_w}$ is isomorphic to
$\mf t^w / Z_{W'}(w)$, as orbifolds.
\item $\pi_{\rho_w} (\lambda)$ and $\pi_{\rho_w}(\lambda')$ have the same trace if and only
if $\lambda$ and $\lambda'$ lie in the same $\mc W'_{\rho_w}$-orbit.
\item The family of representations 
\[
\{ \pi_{\rho_w}(\lambda ) \mid w \in \langle W' \rangle, 
\lambda \in \mf t^{\rho_w} / \mc W'_{\rho_w} \}
\]
contains no repetitions and forms a basis of $G_\Q (\mh H \rtimes \Gamma)$.
}
\end{cor}

The scaling isomorphisms $m_\ep$ for $\ep \in \C^\times$ from \eqref{eq:1.3} provide an
immediate generalization of Theorem \ref{thm:6.4} and Corollary \ref{cor:6.5} to graded
Hecke algebras $\mh H (\tilde R,\ep k) \rtimes \Gamma$ such that $k$ is real valued and
$\ep \in \C$. To retain the formulation of Theorem \ref{thm:6.4} one must modify the 
notions tempered and discrete series, in the sense that everywhere in Section \ref{sec:temp}
one must use $\ep \mf a^-$ instead of $\mf a^-$. Let us call this $\ep$-tempered and
$\ep$-discrete series. We can also consider the family of algebras 
\[
\big\{ \mh H (\tilde{\mc R} , \ep k) \rtimes \Gamma \mid \ep \in \C \big\} .
\]
For every $\ep \in \C$ the analytic families of 
$\mh H (\tilde{\mc R} , \ep k) \rtimes \Gamma$-representations 
\[
\{ \pi_{m_\ep^* (\rho_w )} (\lambda) \mid w \in \langle W' \rangle, 
\lambda \in \mf t^{\rho_w} / \mc W'_{\rho_w} \}
\]
fulfill Corollary \ref{cor:6.5}. We note that the matrix coefficients of
$\pi_{m_\ep^* (\rho_w )} (\lambda)$ depend algebraically on $\ep$ and $\lambda$. More 
specifically, by \eqref{eq:6.4} the $S(\mf t^*)$-weights of $\pi_{m_\ep^* (\rho_w)} (-\ep \mu)$ 
lie in $\mr{Hom} (\Z R, \Z k \ep) \subset \mf t_R$ and depend linearly on $\ep$.

Next we generalize Section \ref{sec:positive} to certain
complex parameter functions $q$. As the analogue of a line $\ep \R$ we use a one-parameter
subgroup of $\C^\times$. We consider $q^\ep$ for a positive parameter function $q$ and 
$\ep \in \C$. Then \eqref{eq:2.3} becomes
\[
k_{u,\ep,\alpha} = \big( \log q_{\alpha^\vee / 2} + (1 + \alpha (u)) \log q_{\alpha^\vee} \big)
\ep / 2 \qquad \alpha \in R_u .
\]
Notice that $\ep = 0$ corresponds to the algebra $\mc H (\mc R ,q^0) \rtimes \Gamma = 
\C [X] \rtimes W'$, which we understand very well. On the other hand, for $\ep \in i \R 
\setminus \{0\}$ the parameter $q_{\alpha^\vee}$ can be a root of unity (unequal to 1), 
in which case the affine Hecke algebra $\mc H (\mc R ,q)$ can differ substiantially from 
those with positive parameters. Therefore we assume that $\Re (\ep) \neq 0$.

\begin{thm}\label{thm:6.6}
Theorem \ref{thm:6.2} and Lemma \ref{lem:6.3} also hold for parameter functions $q^\ep$ with
$q$ positive and $\ep \in \C \setminus i \R$.
For the interpretation of Theorem \ref{thm:6.2} we have to replace $\mf a^-$ by $\ep \mf a^-$,
$T_{rs}$ by $\exp (\ep \mf a)$ and tempered by $\ep$-tempered. 

Moreover we can choose the required analytic families of $\mc H (\mc R,q^\ep) \rtimes 
\Gamma$-representations such that the matrix coefficients of the representations depend 
analytically on $\ep$ and all $\mc A$-weights depend polynomially on the variables
$\big\{ q_{\alpha^\vee}^{\pm \ep/2} \mid \alpha^\vee \in R_{nr}^\vee \big\}$.
\end{thm}
\emph{Proof.}
Every $t \in T$ can be written uniquely as $t = u c$ with $u \in T_{un}$ and 
$c \in \exp (\ep \mf a)$, since $\Re (\ep) \neq 0$. In this setting Theorem \ref{thm:2.1} 
remains valid. Moreover $k_{u,\ep,,\alpha} \in \ep \R$ and 
$\langle \alpha, \lambda \rangle \in \ep \R$ for all $\alpha \in R$ and $\lambda \in \ep \mf a$, 
so $\langle \alpha, \ep \mf a \rangle$ and $\langle \alpha, \ep \mf a \rangle + k_{u,\ep,\alpha}$ 
have positive distance to $\pi i \Z \setminus \{0\}$. This ensures that Theorem \ref{thm:2.2} 
applies to all $\lambda$ in a suitable tubular neighborhood of $\ep \mf a$ in $\mf t$. 
Its part (b) tells us that
$\widehat{\mc H (\mc R,q^\ep)}_{W'u \exp (\lambda)} \rtimes \Gamma$ is Morita equivalent to 
$\widehat{\mh H (\tilde{\mc R}^{P(u)}, \ep k^{P(u)})}_{W'_{\Z P(u)} \lambda} \rtimes W'_{P(u)}$,
while $\mh H (\tilde{\mc R}^{P(u)}, \ep k^{P(u)})$ is isomorphic to a graded Hecke algebra
with real parameter function $k^{P(u)}$ by means of $m_{\ep}$. To 
$\mh H (\tilde{\mc R}^{P(u)}, k^{P(u)})$ we can apply Theorem \ref{thm:6.4}, which gives us
Theorem \ref{thm:6.2} for $\mc H \rtimes \Gamma$-representations with central character
in $W' u \exp (\ep \mf a)$. Combining these results for all $u \in T_{un}$ yields the map
\[
\zeta^\vee : G (\mc H (\mc R ,q^\ep ) \rtimes \Gamma) \to G (X \rtimes W') .
\]
It makes Theorem \ref{thm:6.2} true for $q^\ep$, because it does so on all sets 
$u \exp (\ep \mf a)$.

Let us construct the required analytic families of $\mc H (\mc R,q^\ep ) \rtimes 
\Gamma$-representations. We start with \eqref{eq:6.3} and let $\sigma$ be any of the
$\sigma_{w,i}$. With Theorem \ref{thm:2.2} we transfer the $\mc H^P \rtimes \Gamma_\sigma
$-representation to a tempered representation $\tilde \sigma$ of $\mh H^{P(u)} \rtimes 
\tilde{\Gamma}$, for a suitable subgroup $\tilde \Gamma \subset W'$. Taking for $u$ the 
unitary part of an $\mc A$-weight of $\sigma$, we can achieve that $\tilde \sigma$ has 
real central character. Then $m_\ep^* (\tilde \sigma)$ is an $\ep$-tempered representation of 
$\mh H (\tilde{\mc R}^P(u), \ep k^{P(u)}) \rtimes \tilde{\Gamma}$. Now Theorem \ref{thm:2.2}
in the opposite direction yields an $\ep$-tempered representation of 
$\mc H (\mc R^P , (q^P)^\ep ) \rtimes \Gamma_\sigma$, which we call $m_\ep^* (\sigma)$.
We claim that the analytic families of $\mc H (\mc R ,q^\ep) \rtimes \Gamma$-representations
\[
\{ \pi_{m_\ep^* (\sigma_{w,i})}(t) \mid w \in \langle W' \rangle , 1 \leq i \leq c(w) ,
t \in T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}} \} 
\]
fulfill Lemma \ref{lem:6.3}. By construction $\zeta^\vee (\pi_{m_\ep^* (\sigma_{w,i})}(t))$ 
equals $\zeta^\vee (\sigma_{w,i})(t)$. In view of Lemma \ref{lem:6.3} and
since Theorem \ref{thm:6.2} holds for $q$ and $q^\ep$, this implies the claim.

In view of \cite[(4.6)]{Sol-Irr}, $m_\ep^* (\sigma)$ is also the composition of $\sigma$ 
with the algebra homomorphism $\rho_\ep$ from \cite[Proposition 4.1.2]{Sol-Irr}. Although 
in \cite{Sol-Irr} the author assumed that $\ep \in [-1,1]$, the relevant calculations 
remain valid for $\ep \in \C \setminus i \R$. This shows that the matrix coefficients of 
$m_\ep^* (\sigma)$ depend analytically on $\ep$. More precisely, for every $v \in W^e$ the 
operator $\pi_{m_\ep^* (\sigma_{w,i})}(t,N_v)$ depends in a complex analytic way on 
$\ep$ and $t$.

By \eqref{eq:monomial} all $\mc A$-weights of $\pi_{\sigma_{w,i}}(t)$ are of the form
$\gamma (t u c)$ where $\gamma \in W'$ and $uc$ is a weight of $\sigma_{w,i}$ with unitary 
part $u \in T_{un}$ and absolute value $c \in Y \otimes_\Z q^{\Z / 2}$. This in turn 
implies that all $\mc A$-weights of $\pi_{m_\ep^* (\sigma_{w,i})}(t)$ are of the form
\begin{equation} \label{eq:6.weights}
\gamma (t u c^\ep )  \qquad c^\ep \in q^{\ep \Z / 2},
\end{equation}
and in particular that (for fixed $t$) they depend polynomially on
$\big\{ q_{\alpha^\vee}^{\pm \ep/2} \mid \alpha^\vee \in R_{nr}^\vee \big\}. \qquad \Box$ 
\\[2mm]
Since the whole situation depends in complex analytic fashion on $\ep$, it is natural to
expect that Theorem \ref{thm:6.6} extends to all but finitely many $\ep \in \C$. 
Indeed this is known when $q$ is an equal parameter function \cite{KaLu}, but the methods 
of this paper are insufficient to prove it.
\vspace{3mm}
