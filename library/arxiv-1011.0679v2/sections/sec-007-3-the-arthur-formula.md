---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-007-3-the-arthur-formula
section_title: "The Arthur formula"
section_number: 3
pages: 14-17
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.968
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
\label{sec:Arthur}

In this section we prove the Arthur formula for the Euler--Poincar\'e pairing \eqref{eq:4}
of representations of affine Hecke algebras. In view of Lemma \ref{lem:Elltemp} little is lost
if we restrict $EP_{\mc H}$ to tempered representations, so we do that until further notice.
One of the main results of \cite{OpSo1} says that
\begin{equation}\label{eq:ExtHS}
\mr{Ext}^n_{\mc S} (\pi,\pi') \cong \mr{Ext}^n_{\mc H} (\pi,\pi') \qquad n \in \Z_{\geq 0}
\end{equation}
for all $\pi,\pi' \in \mr{Mod}_f (\mc S)$, and hence
\begin{equation} \label{eq:5}
EP_{\mc S} (\pi,\pi') := \sum_{n \geq 0} (-1)^n \dim_\C \mr{Ext}_{\mc S}^n (\pi,\pi')
\quad \text{equals} \quad EP_{\mc H}(\pi,\pi') .
\end{equation}
We remark that corresponding statement for reductive $p$-adic groups
is a deep theorem of Meyer \cite{Mey}.

It is clear from the definition \eqref{eq:4} that $EP_{\mc H}(\pi,\pi') = 0$ if $\pi$ and $\pi'$
admit different $Z(\mc H)$-characters. With \eqref{eq:5} we can strengthen this to
$EP_{\mc H}(\pi,\pi') = 0$ whenever $\pi$ and $\pi'$ admit different $Z(\mc S)$-characters.
This is really stronger, because $Z(\mc S)$ is larger than the closure of $Z(\mc H)$ in $\mc S$.

We fix $\xi = (P,\delta,t) \in \Xi_{un}$. As $\Xi_{un}$ has the structure of a smooth
manifold (with components of different dimensions) we can consider its tangent space
$T_\xi (\Xi_{un})$ at $\xi$. The isotropy group $\mc W_\xi$ acts linearly on $T_\xi (\Xi_{un})$
and for $w \in \mc W_\xi$ we denote the determinant of the corresponding linear map by
$\det (w )_{T_\xi (\Xi_{un})} $. Since the connected component of $\xi$ in $\Xi_{un}$ is
diffeomorphic to $T^P_{un}$, we have
\[
T_\xi (\Xi_{un}) \cong \text{Lie}(T^P_{un}) \cong i \mf a^P \cong i (\mf a / \mf a_P) .
\]
The expression $\det (1-w )_{T_\xi (\Xi_{un})} = \det (1-w )_{\mf a^P}$
is analogous to the Weyl denominator and to $d(r)$ in Theorem \ref{thm:1}. Notice that
\[
\det (1-w )_{T_\xi (\Xi_{un})} \geq 0
\]
because $T_\xi (\Xi_{un})$ is a real representation of the finite group $\mc W_\xi$. Clearly
$\det (1-w )_{T_\xi (\Xi_{un})} \neq 0$ if and only if $w$ acts without fixed points on
$T_\xi (\Xi_{un}) \setminus \{0\}$, in which case we say that $w$ is elliptic in $\mc W_\xi$.

Given $\pi \in \mr{Mod}_{f,un,\mc W \xi} (\mc S)$, Theorem \ref{thm:KnappStein}.d
produces a representation $E_\xi^{-1} (\pi) = \mr{Hom}_{\mc H}(\pi ,\pi (\xi))$ of
$\C [\mf R_\xi, \kappa_\xi]$. Explicitly, this means
\begin{equation}\label{eq:1}
E_\xi^{-1} (\pi) (w_1) E_\xi^{-1} (\pi) (w_2) E_\xi^{-1} (\pi) (w_1 w_2 )^{-1} =
\kappa_\xi (w_1,w_2) \quad \text{for all } w_1,w_2 \in \mc W_\xi ,
\end{equation}
A variation on \eqref{eq:1} shows that the dual space $E_\xi^{-1} (\pi)^*$ is a representation
of $\C [\mf R_\xi, \kappa_\xi^{-1}]$. If $\pi' \in \mr{Mod}_{f, un, \mc W \xi} (\mc S)$, then
$E_\xi^{-1} (\pi)^* \otimes E_\xi^{-1} (\pi')$ is a representation of $\C [\mf R_\xi,1]$, that is,
of the group $\mf R_\xi$. Its trace is
\begin{equation}\label{eq:23}
\mr{tr}_{E_\xi^{-1} (\pi)^* \otimes E_\xi^{-1} (\pi')} (r) =
\overline{\mr{tr}_{E_\xi^{-1} (\pi)} (r)} \, \mr{tr}_{E_\xi^{-1} (\pi')} (r) .
\end{equation}
It is an elementary result in homological algebra that, for the purpose of computing
Euler--Poincar\'e-pairings, one may replace any module by its semisimplification.
Hence in the next theorem it suffices to compute $EP_\mc{H}(\pi,\pi')$ for
$\pi,\pi'\in \mr{Mod}_{f,\mc W \xi}(\mc S)$ irreducible. Recall that irreducible
tempered modules are unitarizable \cite[Corollary 3.23]{DeOp1}. In particular Theorem
\ref{thm:KnappStein}.d applies to $\pi$ and $\pi'$.
\begin{thm}\label{thm:ArthurFormula}
Let $\pi, \pi' \in \mr{Mod}_{f,\mc W \xi} (\mc S) $ be irreducible tempered $\mc{H}$-modules.
Denote by $\rho:=E_\xi^{-1}(\pi)$ and $\rho':=E_\xi^{-1}(\pi')$
the irreducible modules of $\mathbb{C}[\mf{R}_\xi,\kappa_\xi]$ corresponding to
$\pi$ and $\pi'$ respectively (according to Theorem \ref{thm:KnappStein}).
Then we have:
\[
EP_{\mc H} (\pi,\pi') = | \mf R_\xi |^{-1} \sum_{r \in \mf R_\xi} \det (1-r )_{T_\xi
(\Xi_{un})}\overline{\mr{tr}_{\rho} (r)} \, \mr{tr}_{\rho'} (r) .
\]
\end{thm}
\noindent \emph{Proof.}
Our strategy is to consider $\pi$ and $\pi'$ as modules over various algebras $A$, such that
the extension groups $\mr{Ext}_A^n (\pi, \pi')$ for different $A$'s are all isomorphic.

Write $\xi = (P,\delta,t)$. By \eqref{eq:5}, \eqref{eq:FourierIso} and \eqref{eq:25} we may
replace $\mc H$ first by $\mc S$ and then by
\begin{equation}\label{eq:2}
\big( C^\infty (T^P_{un}) \otimes \mr{End}_\C (\C [W^P] \otimes V_\delta ) \big)^{\mc W_{P,\delta}} .
\end{equation}
Let $U_\xi \subset T^P_{un}$ be a nonempty open ball around $t$ such that
\[
\overline{U_\xi} \cap w \overline{U_\xi} = \left\{ \begin{array}{lll}
\overline{U_\xi} & \text{if} & w \in \mc W_\xi \\
\emptyset & \text{if} & w \in \mc W_{P,\delta} \setminus \mc W_\xi .
\end{array} \right.
\]
The localization of \eqref{eq:2} at $U_\xi$ is
\begin{equation}
\begin{split}\label{eq:6}
C^\infty (U_\xi)^{\mc W_\xi} \otimes_{C^\infty (T^P_{un})^{\mc W_{P,\delta}}}
\big( C^\infty (T^P_{un}) \otimes \mr{End}_\C (\C [W^P] \otimes V_\delta ) \big)^{\mc W_{P,\delta}} \\
\cong \big( C^\infty (U_\xi) \otimes \mr{End}_\C (\C [W^P] \otimes V_\delta ) \big)^{\mc W_\xi} .
\end{split}
\end{equation}
As localization is an exact functor, this preserves the Ext-groups, up to a natural isomorphism.
The action of $\mc W_\xi$ on $C^\infty (U_\xi) \otimes \mr{End}_\C (\C [W^P] \otimes V_\delta )$
is still defined by \eqref{eq:actSections}, so for $w \in \mc W_\xi$ and $t' \in U_\xi$
\begin{equation}\label{eq:7}
(w \cdot f)(t') = \pi (w,P,\delta, w^{-1}t') f (w^{-1} t') \pi (w,P,\delta, w^{-1}t')^{-1} .
\end{equation}
Let $V_\xi$ be the vector space $\C [W^P] \otimes V_\delta$ endowed with the
$\mc H$-representation $\pi (\xi)$. It is also a projective $\mc W_\xi$-representation, so we can
define a $\mc W_\xi$-action on $C^\infty (U_\xi) \otimes \mr{End}_\C (V_\xi)$ by
\begin{equation}\label{eq:8}
(w \cdot f)(t') = \pi (w,\xi) f (w^{-1} t') \pi (w,\xi)^{-1} .
\end{equation}
The difference between \eqref{eq:7} and \eqref{eq:8} is that $\pi (w,P,\delta, w^{-1}t')$
depends on $t'$, while $\pi (w,\xi)$ does not. Since $U_\xi$ is $\mc W_\xi$-equivariantly
contractible to $t$, we are in the right position to apply \cite[Lemma 7]{Sol-Chern}. Its proof, and
in particular \cite[(20)]{Sol-Chern} shows that the algebra \eqref{eq:6}, with the $\mc W_\xi$-action
\eqref{eq:7}, is isomorphic to
\begin{equation}\label{eq:9}
\big( C^\infty (U_\xi) \otimes \mr{End}_\C (V_\xi ) \big)^{\mc W_\xi},
\end{equation}
with respect to the $W_\xi$-action \eqref{eq:8}.
By Theorem \ref{thm:KnappStein}.a the elements of $W (R_{\xi})$ do not really act on
$\mr{End}_\C (V_\xi)$, only on $C^\infty (U_\xi)$. Moreover by \eqref{eq:3} $W (R_{\xi})$ is
normal in $\mc W_\xi$ and $W_\xi / W (R_{\xi}) \cong \mf R_\xi$, so we can rewrite \eqref{eq:9} as
\begin{equation}\label{eq:10}
\big( C^\infty (U_\xi )^{W (R_{\xi})} \otimes \mr{End}_\C (V_\xi ) \big)^{\mf R_\xi} .
\end{equation}
Using suitable coordinates on $U_\xi$, we can identify it as a $\mc W_\xi$-representation with
$T_\xi (\Xi_{un})$. By Chevalley's Theorem \cite{Che,Hum} the algebra
$\mc O (T_\xi (\Xi_{un}))^{W (R_{\xi})}$ is a free polynomial algebra on $\dim T^P_{un}$
generators. With \cite[Theorem 3]{Bie} or \cite{Schw}
one can extend Chevalley's Theorem to smooth functions. Explicitly, this means that
$U_\xi / W(R_{\xi})$ is a manifold with corners such that
\begin{equation}\label{eq:11}
C^\infty (U_\xi )^{W (R_{\xi})} \cong C^\infty \big( U_\xi / W(R_{\xi}) \big)
\cong C^\infty \big( \R^{\dim T^P_{un}} \big) .
\end{equation}
We insert \eqref{eq:11} in \eqref{eq:10} to obtain
\begin{equation}\label{eq:12}
\big( C^\infty \big( U_\xi / W(R_{\xi}) \big) \otimes \mr{End}_\C (V_\xi ) \big)^{\mf R_\xi} .
\end{equation}
Let $\kappa_\xi : \mf R_\xi \times \mf R_\xi \to \C^\times$ be the cocycle from Theorem
\ref{thm:KnappStein}.b and let $\mf R_\xi^*$ be a Schur extension of $\mf R_\xi$
(also known as a representation group, see \cite[Section 53]{CuRe}).
There is a central idempotent $p \in \C [\mf R_\xi^*]$ such that
\[
\C [\mf R_\xi ,\kappa_\xi] \cong p \C [\mf R_\xi^*]
\]
as algebras and as $\C [\mf R_\xi]$-bimodules. By Theorem \ref{thm:KnappStein}.c every
irreducible representation of $\C [\mf R_\xi,\kappa_\xi]$ appears at least
once in $V_\xi$, so by Theorem \ref{thm:Moritaeq}.a \eqref{eq:12} is Morita equivalent to
\begin{equation}\label{eq:16}
\big( C^\infty \big( U_\xi / W(R_{\xi}) \big) \otimes
\mr{End}_\C (p \C [\mf R^*_\xi] ) \big)^{\mf R^*_\xi} .
\end{equation}
Under this Morita equivalence $\pi$ corresponds to a representation
$\pi_1$ of \eqref{eq:16} such that
\begin{equation}\label{eq:17}
\begin{split}
\rho := \mr{Hom}_{\mc H} (\pi, \pi (\xi)) \cong \mr{Hom}_{\big( C^\infty \big( U_\xi /
W(R_{\xi}) \big) \otimes \mr{End}_\C (V_\xi ) \big)^{\mf R_\xi}} (\pi, \pi (\xi)) \\
\cong \mr{Hom}_{\big( C^\infty \big( U_\xi / W(R_{\xi}) \big) \otimes
\mr{End}_\C (p \C [\mf R^*_\xi] ) \big)^{\mf R^*_\xi}} (\pi_1, p \C [\mf R^*_\xi]) ,
\end{split}
\end{equation}
as $\mf R^*_\xi$-representations. Since $p$ is central and by Theorem \ref{thm:Moritaeq}.b,
\eqref{eq:16} is isomorphic to
\begin{equation}\label{eq:18}
p \big( C^\infty \big( U_\xi / W(R_{\xi}) \big) \otimes \mr{End}_\C (\C [\mf R^*_\xi] )
\big)^{\mf R^*_\xi} \cong p \big( C^\infty (U_\xi / W(R_{\xi})) \rtimes \mf R^*_\xi \big) .
\end{equation}
This is a direct summand of $C^\infty (U_\xi / W(R_{\xi})) \rtimes \mf R^*_\xi$, so we can
consider the Ext-groups of $\pi_1$ and $\pi'_1$ just as well with respect to
$C^\infty (U_\xi / W(R_{\xi})) \rtimes \mf R^*_\xi$.
More precisely, by Theorem \ref{thm:Moritaeq}.c and \eqref{eq:17} we get
\begin{equation}\label{eq:21}
\mr{Ext}_{\mc H}^n (\pi,\pi') \cong \mr{Ext}^n_{C^\infty (U_\xi / W(R_{\xi}))
\rtimes \mf R^*_\xi} (\pi_2,\pi'_2) ,
\end{equation}
where $\pi_2$ admits the $C^\infty (U_\xi / W(R_{\xi}))$-character $\mf R^*_\xi t$
and $\pi_2 \big|_{\mf R^*_\xi} \cong \rho^*$, and similarly for $\pi'_2$ and $\rho'$.

Now that we took enough reduction steps, we can resort to more direct calculations. The simple
structure of $C^\infty (U_\xi / W(R_{\xi})) \rtimes \mf R^*_\xi$ allows one to construct an
analogue of the Koszul resolution, which was used in \cite[Theorem 3.2.c]{OpSo1} to show that
\begin{equation}\label{eq:19}
EP_{C^\infty (U_\xi / W(R_{\xi})) \rtimes \mf R^*_\xi} (\pi_2,\pi'_2) =
e_{\mf R^*_\xi} (\pi_2, \pi'_2) = e_{\mf R^*_\xi} (\rho^*, \rho'^*) .
\end{equation}
Following \cite{Ree}, $e_{\mf R^*_\xi}$ denotes the elliptic pairing of
$\mf R^*_\xi$-representations, with respect to the representation of $\mf R^*_\xi$ on the
tangent space $T_t (U_\xi / W(R_{\xi}))$ of $U_\xi / W(R_{\xi})$ at $t$. Of course this is imprecise,
as the orbifold $U_\xi / W(R_{\xi})$ has a corner at $t$. To make more sense of it, one uses
\eqref{eq:11} and reinterprets $T_t (U_\xi / W(R_{\xi}))$ as the tangent space of
$\R^{\dim T^P_{un}}$ at 0. These identifications can be made $\mf R_\xi$-equivariantly,
so $T_0 \big( \R^{\dim T^P_{un}} \big)$ becomes a $\mf R_\xi$-representation.

According to \cite[Section 2]{Ree}, the right hand side of \eqref{eq:19} equals
\begin{equation}\label{eq:20}
\begin{split}
| \mf R^*_\xi |^{-1} \sum\nolimits_{r \in \mf R^*_\xi} \det (1-r )_{T_t (U_\xi / W(R_{\xi}))}
\overline{\mr{tr}_{\pi_2}(r)} \mr{tr}_{\pi'_2}(r) \; = \\
| \mf R^*_\xi |^{-1} \sum\nolimits_{r \in \mf R^*_\xi} \det (1-r )_{T_t (U_\xi / W(R_{\xi}))}
\mr{tr}_{\rho}(r) \overline{\mr{tr}_{\rho'}(r)} .
\end{split}
\end{equation}
Notice that this formula does not use the entire action of $\mf R^*_\xi$ on
$T_t (U_\xi / W(R_{\xi}))$, only $\det (1-r )_{T_t (U_\xi / W(R_{\xi}))}$. This determinant is zero
whenever $r \in \mf R^*_\xi$ fixes a nonzero vector in $T_t (U_\xi / W(R_{\xi}))$. Suppose that
$R_{\xi}$ is nonempty. Then $R_{\xi}^\vee$ is a nonempty root system in $\mf a^P$ and
$\R R_{\xi}^\vee$ can be identified with a subspace of $T_t (U_\xi)$. Every $r \in \mf R^*_\xi$
fixes $\sum_{\alpha \in R^+_{\xi}} \alpha^\vee \in \mf a^P \setminus \{0\}$, so $r$ fixes
nonzero vectors of $T_t (U_\xi)$ and $T_t (U_\xi / W(R_{\xi}))$. We conclude that
\[
\det (1-r )_{T_t (U_\xi / W(R_{\xi}))} = 0 = \det (1-r )_{T_t (U_\xi)}
\]
whenever $R_{\xi}$ is nonempty. Therefore we may always replace
$T_t (U_\xi / W(R_{\xi}))$ by $T_t (U_\xi) = T_\xi (\Xi_{un})$ in \eqref{eq:20}.
So by \eqref{eq:21}, \eqref{eq:19} and \eqref{eq:20}
\begin{equation}\label{eq:22}
EP_{\mc H} (\pi, \pi') = | \mf R^*_\xi |^{-1} \sum_{r \in \mf R^*_\xi}
\det (1-r )_{T_\xi (\Xi_{un})} \mr{tr}_{\rho}(r) \overline{\mr{tr}_{\rho'}(r)} .
\end{equation}
Finally we want to reduce from $\mf R^*_\xi$ to $\mf R_\xi$. The action of $\mf R^*_\xi$ on
$T_\xi (\Xi_{un})$ is defined via the quotient map $\mf R^*_\xi \to \mf R_\xi$, so that is no problem.
We noted in \eqref{eq:23} that $\rho\otimes\rho'^*$ is a $\mf R_\xi$-representation with trace
\[
\mr{tr}_{\rho\otimes\rho'^*} (r) =
\mr{tr}_\rho (r) \overline{\mr{tr}_{\rho'}(r)} .
\]
Hence any two elements of $\mf R^*_\xi$ with the same image in $\mf R_\xi$ give the same
contribution to \eqref{eq:22}. Furthermore $EP_{\mc H}$ is symmetric by Theorem \ref{thm:EP}.b, so
\begin{equation*}
EP_{\mc H} (\pi, \pi') = EP_{\mc H} (\pi' ,\pi) = | \mf R_\xi |^{-1} \sum_{r \in \mf R_\xi}
\det (1-r )_{T_\xi (\Xi_{un})} \mr{tr}_{\rho'}(r) \overline{\mr{tr}_\rho (r)} .
\quad \Box
\end{equation*}

\begin{rem}\label{rem:ArthurPadic}
The proof of Theorem \ref{thm:ArthurFormula} relies on three deep results: the Knapp--Stein
linear independence theorem (Theorem \ref{thm:KnappStein}), the isomorphism
$\mr{Ext}^*_{\mc H} \cong \mr{Ext}^*_{\mc S}$ for tempered representations \eqref{eq:ExtHS}
and the Plancherel isomorphism for $\mc S$ \eqref{eq:FourierIso}. Since these three theorems are
also known for all reductive $p$-adic groups (as we indicated in some remarks) the proof of Theorem
\ref{thm:ArthurFormula} applies equally well to the Euler--Poincar\'e pairing for admissible
tempered representations of reductive $p$-adic groups. This proves Theorem \ref{thm:2}.
\end{rem}
\vspace{4mm}
