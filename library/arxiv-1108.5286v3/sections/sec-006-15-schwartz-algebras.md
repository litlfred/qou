---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-006-15-schwartz-algebras
section_title: "Schwartz algebras"
section_number: 1.5
pages: 12-16
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.983
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
\label{sec:temp}

An important tool to study $\mc H$-representations is restriction to the commutative 
subalgebra $\mc A \cong \mc O (T)$. We say that $t \in T$ is a weight of $(\pi,V)$ if there
exists a $v \in V \setminus \{ 0 \}$ such that $\pi (a) v = a(t) v$ for all $a \in \mc A$.
Temperedness of $\mc H$-representations, which is defined via $\mc A$-weights, is analogous to 
temperedness of representations of reductive groups. Via the Langlands classification for 
affine Hecke algebras \cite[Section 2.2]{Sol-Irr} these representations are essential 
in the classification of irreducible representations.

The antidual of $\mf a^{*+} :=  \{ x \in \mf a^* \mid  \inp{x}{\alpha^\vee} \geq 0 
\: \forall \alpha \in \Delta \}$ is
\begin{equation} 
\mf a^- = \{ \lambda \in \mf a \mid \inp{x}{\lambda} \leq 0 \: \forall x \in \mf a^{*+} \} = 
\big\{ \sum\nolimits_{\alpha \in \Delta} 
\lambda_\alpha \alpha^\vee \mid \lambda_\alpha \leq 0 \big\} .
\end{equation}
The interior $\mf a^{--}$ of $\mf a^-$ equals $\big\{ {\ts \sum_{\alpha \in \Delta}} 
\lambda_\alpha \alpha^\vee \mid \lambda_\alpha < 0 \big\}$
if $\Delta$ spans $\mf a^*$, and is empty otherwise. We write $T^- = \exp (\mf a^-)$ and
$T^{--} = \exp (\mf a^{--})$. 

Let $t = |t| \cdot t |t|^{-1} \in T_{rs} \times T_{un}$ be the polar decomposition of $t$.
A finite dimensional $\mc H$-representation is called tempered if $|t| \in T^-$ for all its 
$\mc A$-weights $t$, and anti-tempered if $|t|^{-1} \in T^-$ for all such $t$. 

We say that an irreducible  $\mc H$-representation belongs to the discrete 
series (or simply: is discrete series) if all its $\mc A$-weights lie in $T^{--} T_{un}$. 
In particular the discrete series is empty if $\Delta$ does not span $\mf a^*$.
The discrete series is a starting point for the construction of irreducible representations:
they can all be realized as a subrepresentation of the induction of a discrete series 
representation of a parabolic subalgebra of $\mc H$.
The notions tempered and discrete series apply equally well to $\mc H \rtimes \Gamma$,
since that algebra contains $\mc A$ and the action of $\Gamma$ on $T$ preserves $T^-$.

This terminology also extends naturally to graded Hecke algebras, via the $S (\mf t^*)$-weights
of a representation. Thus we say that a finite dimensional $\mh H \rtimes \Gamma$-representation
is tempered if all its $S (\mf t^*)$-weights lie in $\mf a^- + i \mf a$ and we say that it
is discrete series if it is irreducible and all its $S (\mf t^*)$-weights lie in 
$\mf a^{--} + i \mf a$. By construction Lusztig's two reduction theorems from Section 
\ref{sec:redthm} preserve the properties temperedness and discrete series.

\begin{prop}\label{prop:5.1}
Let $P \subset \Delta$.
\enuma{
\item Let $\sigma$ be a finite dimensional $\mc H_P \rtimes \Gamma_P$-representation. 
For $t \in T^P$ the $\mc H \rtimes \Gamma$-representation
$\mr{Ind}_{\mc H_P \rtimes \Gamma_P}^{\mc H \rtimes \Gamma} (\sigma \circ \phi_t)$
is tempered if and only if $t \in T^P_{un}$ and $\sigma$ is tempered.
\item Let $\rho$ be a finite dimensional $\mh H_P \rtimes \Gamma_P$-representation. 
For $\lambda \in \mf t^P$ the $\mh H \rtimes \Gamma$-representation
$\mr{Ind}_{\mh H_P \rtimes \Gamma_P}^{\mh H \rtimes \Gamma} (\rho \circ \phi_\lambda)$
is tempered if and only if $\lambda \in i \mf a^P$ and $\rho$ is tempered.
}
\end{prop}
\emph{Proof.}
For (a) see \cite[Lemma 3.1.1.b]{Sol-Irr} and for (b) see \cite[Lemma 2.2]{SolGHA}. 
$\qquad \Box$ \\[2mm]

Now we will recall the construction of the Schwartz algebra $\mc S$ of an affine Hecke 
algebra \cite{DeOp1}, which we will use in Section \ref{sec:homS}.
For this we assume that the parameter function $q$ is positive, because otherwise
there would not be a good link with $C^*$-algebras. As a topological vector space $\mc S$ 
will consist of rapidly decreasing functions on $W^e$, with respect to a suitable length 
function $\mc N$. For example we can take a $W$-invariant norm on $X \otimes_\Z \R$ and put
$\mc N (w t_x) = \norm{x}$ for $w \in W$ and $x \in X$. Then we can define, for $n \in \N$, 
the following norm on $\mc H$:
\[
p_n \big( \sum_{w \in W^e} h_w N_w \big) = \sup_{w \in W^e} |h_w| (\mc N (w) + 1)^n .
\]
The completion of $\mc H$ with respect to these norms is the Schwartz algebra 
$\mc S = \mc S (\mc R,q)$. It is known from \cite[Section 6.2]{Opd-Sp} that it is a 
Fr\'echet algebra. Diagram automorphisms of $\mc R$ induce automorphisms of $\mc S$, so the
crossed product algebra $\mc S \rtimes \Gamma$ is well-defined. By \cite[Lemma 2.20]{Opd-Sp} 
a finite dimensional $\mc H \rtimes \Gamma$-representation is 
tempered if and only if it extends continuously to an $\mc S \rtimes \Gamma$-representation. 

Next we describe the Fourier transform for $\mc H$ and $\mc S$.
An induction datum for $\mc H$ is a triple $(P,\delta,t)$, with $P \subset \Delta , t \in T^P$ 
and $\delta$ a discrete series representation of $\mc H_P$. A large part of the representation 
theory of $\mc H$ is built on the parabolically induced representations
\[
\pi (P,\delta,t) = \mr{Ind}_{\mc H^P}^{\mc H} (\delta \circ \phi_t)  \quad \text{and} \quad 
\pi^\Gamma (P,\delta,t) = \mr{Ind}_{\mc H^P}^{\mc H \rtimes \Gamma} (\delta \circ \phi_t) .
\]
Let $\Xi$ be the space of all such induction data $(P,\delta,t)$, with $\delta$ up to
equivalence of $\mc H_P$-representations. It carries a natural structure of a complex affine 
variety with finitely many components of different dimensions. Furthermore $\Xi$ has 
a compact submanifold
\[
\Xi_{un} := \big\{ (P,\delta,t) \in \Xi \mid t \in T^P_{un} \big\} ,
\]
which is a disjoint union of finitely many compact tori.

Given a discrete series representation $(\delta ,V_\delta)$ of a parabolic subalgebra 
$\mc H_P$ of $\mc H$, the $\mc H \rtimes \Gamma$-representation $\pi^\Gamma (P,\delta,t)$
can be realized on the vector space $V_\delta^\Gamma := \C [\Gamma W^P] \otimes V_\delta$,
which does not depend on $t \in T^P$. Here $W^P$ is a specified set of representatives for
$W / W(R_P)$. Let $\mc V_\Xi^\Gamma$ be the vector bundle over $\Xi$ whose fiber at 
$\xi = (P,\delta,t)$ is $V_\delta^\Gamma$, and let 
\[
\mc O (\Xi; \mr{End}(\mc V_\Xi^\Gamma)) := \bigoplus\nolimits_{P,\delta} \mc O (T^P) \otimes
\mr{End}_\C (V_\delta^\Gamma)
\]
be the algebra of polynomials sections of the endomorphism bundle $\mr{End} (\mc V_\Xi^\Gamma)$.
The Fourier transform for $\mc H \rtimes \Gamma$ is
\begin{align*}
& \mc F : \mc H \rtimes \Gamma \to \mc O (\Xi; \mr{End}(\mc V_\Xi^\Gamma)), \\
& \mc F (h) (\xi) = \pi^\Gamma (\xi) (h) .
\end{align*}
It extends to an algebra homomorphism
\begin{equation}
\mc F : \mc S \rtimes \Gamma \to C^\infty (\Xi_{un}; \mr{End}(\mc V_\Xi^\Gamma )) :=
\bigoplus\nolimits_{P,\delta} C^\infty (T^P_{un}) \otimes \mr{End}_\C (V_\delta^\Gamma) ,
\end{equation}
defined by the same formula. 

We will need a groupoid $\mc G$ over the power set of $\Delta$, defined as follows. 
For $P,Q \subset \Delta$ the collection of arrows from $P$ to $Q$ is
\[
\mc G_{PQ} = \{ (g,u) \in \Gamma \ltimes W \times K_P \mid g(P) = Q \} .
\]
Whenever it is defined, the multiplication in $\mc G$ is 
\[
(g',u') \cdot (g,u) = (g' g, g^{-1}(u) u') .
\]
This groupoid acts from the left on $\Xi$ by
\begin{equation}\label{eq:GactsXi}
(g,u) (P,\delta,t) = \big( g(P),\delta \circ \psi^{-1}_u \circ \psi^{-1}_g, g(ut) \big) .
\end{equation} 
This is the projection of an action of $\mc G$ on parabolically induced representations via
intertwining operators. These operators provide an action of $\mc G$ on $C^\infty (\Xi_{un}; 
\mr{End}(\mc V_\Xi^\Gamma ))$, see \cite[Theorem 4.33]{Opd-Sp} and \cite[(3.16)]{Sol-Irr}. 
The Plancherel isomorphism for (extended) affine Hecke algebras with positive parameters reads:

\begin{thm} \label{thm:5.2}
The Fourier transform $\mc F$ induces an isomorphism of Fr\'echet algebras
\[
\mc S \rtimes \Gamma \to C^\infty (\Xi_{un}; \mr{End}(\mc V_\Xi^\Gamma ))^{\mc G} .
\]
\end{thm}
\emph{Proof.}
See \cite[Theorem 5.3]{DeOp1} and \cite[Theorem 3.2.2]{Sol-Irr}. $\qquad \Box$
\vspace{2mm}

From this isomorphism we see in particular that there are unique central idempotents
$e_{P,\delta} \in \mc S \rtimes \Gamma$ such that 
\begin{equation} \label{eq:5.1}
\begin{aligned}
& e_{P,\delta} \mc S \rtimes \Gamma \cong 
\big( C^\infty (T^P_{un}) \otimes \mr{End}_\C (V_\delta^\Gamma) \big)^{\mc G_{P,\delta}} ,\\
& \mc G_{P,\delta} := \big\{ g \in \mc G \mid g (P,\delta,T^P_{un}) = (P,\delta,T^P_{un}) \big\} .
\end{aligned}
\end{equation}
For a suitable collection $\mc P$ of pairs $(P,\delta)$ we obtain decompositions
\begin{equation} \label{eq:5.2}
\begin{aligned}
& \mc S \rtimes \Gamma && = && 
\bigoplus\nolimits_{(P,\delta) \in \mc P} e_{P,\delta} \mc S \rtimes \Gamma ,\\
& Z (\mc S \rtimes \Gamma) && = && 
\bigoplus\nolimits_{(P,\delta) \in \mc P}  C^\infty (T^P_{un})^{\mc G_{P,\delta}} .
\end{aligned}
\end{equation}
Via \eqref{eq:5.1} the subalgebra $e_{P,\delta} \mc H \rtimes \Gamma$ of 
$\mc S \rtimes \Gamma$ is isomorphic to a subalgebra of
$\big( \mc O (T^P) \otimes \mr{End}_\C (V_\delta^\Gamma) \big)^{\mc G_{P,\delta}}$.
We note that $e_{P,\delta} Z (\mc H \rtimes \Gamma )$ is isomorphic to the restriction of
$Z (\mc H \rtimes \Gamma) \cong \mc O (T)^{W'}$ to the image of $(P,\delta,T^P_{un})$
in $T / W'$. We will see from Lemma \ref{lem:6.3} that it is just $\mc O (T^P)^{\mc G_{P,\delta}}$.

Clearly $e_{P,\delta} \mc H \rtimes \Gamma$ is dense in $e_{P,\delta} \mc S \rtimes \Gamma$,
so for any closed ideal $I \subset e_{P,\delta} \mc S \rtimes \Gamma$ of finite codimension
the canonical maps
\begin{equation} \label{eq:5.3}
e_{P,\delta} \mc H \rtimes \Gamma / \big( I \cap e_{P,\delta} \mc H \rtimes \Gamma \big) \to
\big( e_{P,\delta} \mc H \rtimes \Gamma + I \big) / I \to
e_{P,\delta} \mc S \rtimes \Gamma / I 
\end{equation}
are isomorphisms of $e_{P,\delta} \mc H \rtimes \Gamma$-modules. 

\begin{lem}\label{lem:5.3}
The multiplication map
\[
\mu_{P,\delta} : e_{P,\delta} Z (\mc S \rtimes \Gamma ) \otimes_{e_{P,\delta} Z (\mc H 
\rtimes \Gamma )} e_{P,\delta} \mc H \rtimes \Gamma \to e_{P,\delta} \mc S \rtimes \Gamma 
\]
is an isomorphism of $e_{P,\delta} Z (\mc S \rtimes \Gamma )$-modules.
\end{lem}
\emph{Proof.}
Clearly $\mu_{P,\delta}$ is $e_{P,\delta} Z (\mc S \rtimes \Gamma )$-linear. By Theorem
\ref{thm:5.2} $e_{P,\delta} \mc S \rtimes \Gamma$ is of finite rank over 
$e_{P,\delta} Z (\mc S \rtimes \Gamma )$ and we know that $e_{P,\delta} \mc H \rtimes \Gamma$ 
is dense in $e_{P,\delta} \mc S \rtimes \Gamma$. Thus the image of $\mu_{P,\delta}$ is
closed and dense in $e_{P,\delta} \mc S \rtimes \Gamma$, which means that $\mu_{P,\delta}$ 
is surjective. 

Let $I_\xi$ be the maximal ideal of $e_{P,\delta} Z (\mc S \rtimes \Gamma ) \cong
C^\infty (T^P_{un})^{\mc G_{P,\delta}}$ corresponding to $\xi = (P,\delta,t)$. Applying 
\eqref{eq:5.3} to $I_\xi^n e_{P,\delta} \mc S \rtimes \Gamma$ we see that
$\mu_{P,\delta}$ induces isomorphisms
\begin{equation}\label{eq:5.4}
e_{P,\delta} Z (\mc S \rtimes \Gamma ) / I_\xi^n \otimes_{e_{P,\delta} Z (\mc H 
\rtimes \Gamma )} e_{P,\delta} \mc H \rtimes \Gamma \to 
e_{P,\delta} \mc S \rtimes \Gamma / I_\xi^n (e_{P,\delta} \mc S \rtimes \Gamma ) ,
\end{equation}
for all $n \in \Z_{>0}$. Consider any $x \in \ker \mu_{P,\delta}$. Its annihilator Ann$(x)$
is a closed ideal of $e_{P,\delta} Z (\mc S \rtimes \Gamma )$ and $e_{P,\delta} Z(\mc S \rtimes
\Gamma) x \cong e_{P,\delta} Z(\mc S \rtimes \Gamma) / \mr{Ann}(x)$. By \eqref{eq:5.4}
$I_\xi^n / I_\xi^n \mr{Ann}(x) = 0$ for all $\xi \in (P,\delta,T^P_{un})$. Therefore
Ann$(x)$ is not contained in any of the closed maximal ideals $I_\xi$. Consequently
Ann$(x) = e_{P,\delta} Z (\mc S \rtimes \Gamma )$ and $x = 0. \qquad \Box$
\vspace{3mm}
