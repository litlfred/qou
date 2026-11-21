---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-008-21-positive-parameters
section_title: "Positive parameters"
section_number: 2.1
pages: 16-21
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.985
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
\label{sec:positive}

In this subsection we assume that $q$ is positive. We will define analytic families of 
representations and show that they can be used to construct the dual space of $\mc H (\mc R,q)$.

\begin{thm} \label{thm:6.1}
Let $\xi, \xi' \in \Xi$.
\enuma{
\item The $\mc H \rtimes \Gamma$-representations $\pi^\Gamma (\xi)$ and $\pi^\Gamma (\xi')$
have the same trace if and only if there exists a $g \in \mc G$ such that $g \xi = \xi'$.
\item Suppose that $\xi, \xi' \in \Xi_{un}$. Then $\pi^\Gamma (\xi)$ and $\pi^\Gamma (\xi')$ are 
completely reducible, and they have a common irreducible subquotient if only if there exists a 
$g \in \mc G$ such that $g \xi = \xi'$. Moreover $\pi^\Gamma (\xi) \cong \pi^\Gamma (\xi')$ 
in this situation.
}
\end{thm}
\emph{Proof.}
(a) \cite[Lemma 3.1.7]{Sol-Irr} provides the "if"-part. 
By \cite[page 44]{Sol-Irr} the "only if"-part can be reduced to certain positive induction data, 
to which \cite[Theorem 3.3.1]{Sol-Irr} applies.\\
(b) See Corollary 3.1.3 and Theorem 3.3.1 of \cite{Sol-Irr}. We note that this is essentially a 
consequence of Theorem \ref{thm:5.2}. $\qquad \Box$ 
\\[2mm]

Since $\gamma (P) \subset \Delta$ for all $\gamma \in \Gamma$ and $P \subset \Delta$,
\eqref{eq:GactsXi} describes an action of $\Gamma$ on $\Xi$. 
Given an induction datum $\xi = (P,\delta,t) \in \Xi$ we put
\[
\Gamma_\xi = \{ \gamma \in \Gamma_P \mid \delta \circ \phi_t \cong \delta \circ \phi_t
\circ \psi_\gamma^{-1} \text{ as } \mc H^P \text{-representations }\} .
\]
Now we fix $(P,\delta ,u) \in \Xi_{un}$ and we let $\sigma$ be an irreducible direct summand of
$\mr{Ind}_{\mc H^P}^{\mc H^P \rtimes \Gamma_{(P,\delta,u)}} (\delta \circ \phi_u)$.
In this case we abbreviate $\Gamma_{(P,\delta,u)} = \Gamma_\sigma$. By Clifford theory
the representations 
$\mr{Ind}_{\mc H^P}^{\mc H^P \rtimes \Gamma_\sigma} (\delta \circ \phi_u)$ and 
$\mr{Ind}_{\mc H^P \rtimes \Gamma_\sigma}^{\mc H^P \rtimes \Gamma_P} (\sigma)$
are completely reducible.

Let $T^\sigma$ be the connected component of $T^{W (R_P) \rtimes \Gamma_\sigma}$
that contains $1 \in T$. Notice that $T^\sigma \subset T^P$ because $T_P^{W(R_P)}$ is finite.
We call
\begin{equation}\label{eq:smoothFamily}
\big\{ \pi_\sigma (t) = \mr{Ind}_{\mc H^P \rtimes \Gamma_\sigma}^{\mc H \rtimes \Gamma}
(\sigma \circ \phi_t) \mid t \in T^\sigma \big\} 
\end{equation}
an analytic $d$-dimensional family of $\mc H \rtimes \Gamma$-representations, where $d$ is the 
dimension of the complex algebraic variety $T^\sigma$. By Proposition \ref{prop:5.1} the 
representations $\pi_\sigma (t)$ are tempered if and only if 
$t \in T^\sigma_{un} := T^\sigma \cap T_{un}$. We refer to 
$\{ \pi_\sigma (t) \mid t \in T^\sigma_{un} \}$ as a tempered analytic family
or an analytic family of $\mc S$-representations. \\[1mm]

\texttt{Correction (2021):} To guarantee that the union of analytic families of representations 
spans $G_\Q (\mc H \times \Gamma)$, we need to allow more general $\sigma$. Namely, we need all 
irreducible tempered elliptic representations of a parabolic subalgebra $\mc H^P \rtimes \Gamma'_P$, 
where $\Gamma'_P$ is an arbitrary subgroup of $\Gamma_P$. Here elliptic means that the image in 
$G_\Q (\mc H^P \rtimes \Gamma'_P)$ does not belong to the span of the representations induced from 
proper parabolic subalgebras of $\mc H^P \rtimes \Gamma'_P$.
Such a $\sigma$ is a direct summand of the $\mc H^P \rtimes \Gamma'_P$-representation associated to a
triple $(P,\delta,u) \in \Xi_{un}$. With that, the below arguments hold in the necessary generality.\\

Since there are only finitely many pairs $(P,\delta)$ and since two $u$'s in the same 
$T^\sigma$-coset give rise to the same analytic family, there exist only finitely many analytic 
families of $\mc H \rtimes \Gamma$-representations. Recall from \cite[Theorem 2.58]{OpSo2}
that the absolute value of any $\mc A_P$-weight of $\delta$ is a monomial in the variables 
$q (s_\alpha)^{\pm 1/2}$. That is, it lies in 
\begin{equation}
W (R_P) u_\delta Y_P \otimes_\Z q^{\Z / 2}
\end{equation}
where $u_\delta \in T_{P,un}$ is the unitary part of such a weight.
Hence all $\mc A$-weights of $\pi_\sigma (t)$ lie in
\begin{equation}\label{eq:monomial}
W' t u  u_\delta Y \otimes_\Z q^{\Z / 2} . 
\end{equation}
We note that the $\mc H^P \rtimes \Gamma_\sigma$-representation $\pi_\sigma (t)$ is only
defined for $t \in T^{W(R_P) \rtimes \Gamma_\sigma}$, so it is impossible to extend 
\eqref{eq:smoothFamily} to a larger connected subset of $T^P$. As discussed in \cite{Sol-Irr} after
(3.30), the representations $\pi_\sigma (t)$ are irreducible for $t$ in a Zariski-open dense
subset of $T^\sigma$. Like in \eqref{eq:5.1} the group
\begin{equation} \label{eq:Gsigma}
\mc G_\sigma := \big\{ g \in \mc G \mid g(P) = P, \delta \circ \psi_g^{-1} \cong \delta, 
g \text{ stabilizes } \{ \pi_\sigma (t) \mid t \in T^\sigma_{un} \} \big\}
\end{equation}
acts on $T^\sigma$. (Here the advantage of considering only $T^\sigma_{un}$ is that Theorem 
\ref{thm:6.1}.b applies.) By Theorem \ref{thm:6.1}.a $\pi_\sigma (t)$ and $\pi_\sigma (g t)$ 
have the same trace for all $t \in T^{\sigma}$ and $g \in \mc G_\sigma$. We will see later 
that every representation $\pi_{\sigma}(t')$ with $t'$ in a different $\mc G_\sigma$-orbit 
has a different trace.

Let $G (A)$ denote the Grothendieck group of finite dimensional $A$-representations, for suitable
algebras or groups $A$. As explained in \cite[Section 3.4]{Sol-Irr}, 
\begin{equation*}
G_\Q (\mc H \rtimes \Gamma) := \Q \otimes_\Z G (\mc H \rtimes \Gamma) 
\end{equation*}
can be built from analytic families of representations (called smooth families in that paper). 
By this we mean that we can choose a collection of analytic families 
$\{ \pi_{\sigma_i} (t) \mid t \in T^{\sigma_i} \}$ such that the set
\begin{equation}\label{eq:6.1}
\bigcup\nolimits_i  \{ \pi_{\sigma_i} (t) \mid t \in T^{\sigma_i}  / \mc G_{\sigma_i} \}
\end{equation}
spans $G_\Q (\mc H \rtimes \Gamma)$. In \cite[Section 3.4]{Sol-Irr} this is actually done with
"Langlands constituents" of $\pi_{\sigma_i} (t)$. But by \cite[Lemma 2.2.6]{Sol-Irr} the
Langlands formalism is such that the other constituents of $\pi_{\sigma_i}(t)$ are smaller in
a certain sense. Hence the non-Langlands constituents are already accounted for by families of 
smaller dimension.

All this can be made much more concrete for the algebra 
\[
\mc H (\mc R ,1) \rtimes \Gamma = \C [X \rtimes (W \rtimes \Gamma)] = \mc O (T) \rtimes W' .
\] 
By classical results which go back to Frobenius and Clifford, its irreducible representations 
with $\mc O (T)^{W'}$-character $W' t$ are in bijection with the irreducible representations 
$\sigma$ of the isotropy group $W'_t$, via
\begin{equation}\label{eq:6.9}
\sigma \mapsto \mr{Ind}_{X \rtimes W'_t}^{X \rtimes W'} (\C_t \otimes \sigma) .
\end{equation}
With this one can easily determine the dual space of $X \rtimes W'$. Let
\[
\tilde T = \{ (w,t) \in T \times W' \mid w(t) = t \} .
\]
Then $W'$ acts on $\tilde T$ by $w \cdot (w',t) = (w w' w^{-1}, w(t))$ and $\tilde T / W'$ 
is called the extended quotient of $T$ by $W'$. Let $\langle W' \rangle$ be a set of 
representatives for the conjugacy classes in $W'$. Then
\begin{equation}\label{eq:6.10}
\tilde T / W' \cong \bigsqcup_{w \in \langle W' \rangle} T^w / Z_{W'}(w) ,
\end{equation}
where $Z_{W'}(w)$ denotes the centralizer of $w$ in $W'$. Let $T_i^w / Z_{W'}(w) ,
i=1 ,\ldots, c(w)$ be the connected components of $T^w / Z_{W'}(w)$, so that
\begin{equation}\label{eq:6.11}
\tilde T / W' \cong \bigsqcup_{w \in \langle W' \rangle} 
\bigsqcup_{1 \leq i \leq c(w)} T_i^w / Z_{W'}(w) .
\end{equation}
By the above there exists a continuous bijection from $\tilde T / W'$ to the space of irreducible 
complex representations of $X \rtimes W'$. We vary a little and take the 
Grothendieck group of $X \rtimes W'$ instead. Let $C_w \subset W'$ be the cyclic group generated 
by $w$ and let $\rho_w$ be a $C_w$-representation.
This yields an analytic family of $X \rtimes W'$-representations 
\[
\big\{ \pi_{w,i} (t) := \mr{Ind}_{X \rtimes C_w}^{X \rtimes W'} 
(\C_t \otimes \rho_w) \mid t \in T_i^w \big\} .
\]
For generic $t$, $\pi_{w,i}(t)$ is irreducible if $W'_t = C_w$. Moreover $\pi_{w,i}(t)$ arise
by induction from an elliptic representation of $X \rtimes (W(R_P) \rtimes \Gamma'_P)$, where
$W(R_P) \rtimes \Gamma'_P$ is a parabolic subgroup of $W \rtimes \Gamma$ minimally containing $w$.

By Artin's Theorem \cite[Theorem 17]{Ser} it is possible to choose the $\rho_w$ such that $G_\Q (W'_t)$ 
is spanned by $\{ \mr{Ind}_{C_w}^{W'_t}(\rho_w) \mid w \in W'_t \}$, \\[1mm]

\texttt{Correction (2021): The next claim is false, it can fail for\\
instance if $W' = \Z / 4 \Z$.} \\

and a basis is obtained by 
taking only one $w$ from every conjugacy class in $W'_t$. It follows that the representations
\begin{equation} \label{eq:6.2}
\big\{ \pi_{w,i} (t) \mid w \in \langle W' \rangle, 
1 \leq i \leq c(w), t \in T_i^w / Z_{W'}(w) \big\}
\end{equation}
form a basis of $G_\Q (X \rtimes W')$. Notice that the space underlying \eqref{eq:6.2} is exactly
the extended quotient $\tilde T / W'$, since all the involved representations are different. 
Having described this Grothendieck group conveniently, we recall how it can be compared with the 
Grothendieck groups of associated affine Hecke algebras.

\begin{thm} \label{thm:6.2}
\textup{\cite[Section 2.3]{Sol-Irr}} \\
Let $q$ be positive. There exists a natural $\Q$-linear bijection 
\[
\zeta^\vee : G_\Q (\mc H \rtimes \Gamma) \to G_\Q (X \rtimes W')
\]
such that:
\begin{enumerate}[\textup{(}1\textup{)}]
\item $\zeta^\vee$ restricts to a bijection between the corresponding Grothendieck groups of 
tempered representations;
\item $\zeta^\vee$ commutes with parabolic induction, in the sense that for a subgroup 
$\Gamma'_P \subset \Gamma_P$, a tempered $\mc H^P \rtimes \Gamma'_P$-representation 
$\pi$ and $t \in T^{W(R_P) \rtimes \Gamma'_P}$ we have
\[
\zeta^\vee \big( \mr{Ind}_{\mc H^P \rtimes \Gamma'_P}^{\mc H \rtimes \Gamma} 
(\pi \circ \phi_t) \big) = \mr{Ind}_{X \rtimes (W (R_P) \rtimes \Gamma'_P 
)}^{X \rtimes (W \rtimes \Gamma)} (\zeta^\vee (\pi) \circ \phi_t) ;
\]
\item if $u \in T_{un}$ and $\pi$ is a virtual representation with central character in 
$W' u T_{rs}$, then so is $\zeta^\vee (\pi)$.
\end{enumerate}
\end{thm}

Let $d \in \N$. By property (2) $\zeta^\vee$ sends analytic $d$-dimensional families of 
$\mc H \rtimes \Gamma$-representations to analytic $d$-dimensional families of 
$X \rtimes W'$-representations - except that the latter need not be generically irreducible. 
The image can not be part of a higher
dimensional analytic family, for that would violate the bijectivity of $\zeta^\vee$. 
Since no $d$-dimensional variety is a finite union of varieties of dimension strictly smaller 
than $d$, and since there are only finitely many analytic families, $\zeta^\vee$ restricts to 
a bijection between the subspaces (of the Grothendieck groups) spanned by analytic families of 
dimension at least $d$. Let us call these subspaces $G_\Q^d (\mc H \rtimes \Gamma)$ and 
$G_\Q^d (X \rtimes W')$. Then $\zeta^\vee$ induces a bijection 
\begin{equation}\label{eq:6.12}
G_\Q^d (\mc H \rtimes \Gamma) / G_\Q^{d+1} (\mc H \rtimes \Gamma) \to
G_\Q^d (X \rtimes W') / G_\Q^{d+1} (X \rtimes W') .
\end{equation}
By \eqref{eq:6.2} the right-hand side has a basis which is parametrized by the $d$-dimensional 
part of $\widetilde T / W'$. \\[1mm]

\texttt{Correction (2022):} Unfortunately the below construction of families of representations
does not work in general, because of the problems with \eqref{eq:6.2} and because an application
of Theorem \ref{thm:6.2} could result in virtual $\mc H \rtimes \Gamma$-representations.
Nevertheless a collection of families of representations satisfying Lemma \ref{lem:6.3} below
can be found in most cases:
\begin{itemize}
\item When the parameters $q$ are of ``geometric type", one can use families of standard 
representations from \cite[Paragraph 3.3]{AMS3}.
\item For most positive-valued $q$ one can use the technique with parameter deformations from
\cite[proof of Lemma 6.4]{SolHecke}, to reduce to the previous case.
\item We are not aware of any examples of graded Hecke algebras for which it is clear that they 
do not possess families of representations satisfying Lemma \ref{lem:6.3}.
\end{itemize}
In all these cases, the remainder of the paper is valid without further changes.\\[2mm]

We can use this to pick a suitable collection of analytic families of 
$\mc H \rtimes \Gamma$-representations. Fix a $d$-dimensional component of $\widetilde T / W'$
and let $C$ be its image in $T / W'$. In the notation of \eqref{eq:6.11} let $\tilde C$ 
be the collection of $(w,i)$ such that $w \in \langle W' \rangle ,\; 1 \leq i \leq c(w)$ and 
$T^w_i / W' = C$. By Theorem \ref{thm:6.2} and \eqref{eq:6.12} there exist analytic families of
$\mc H \rtimes \Gamma$-representations $\{ \pi_{\sigma_{w,i}}(t) \mid (w,i) \in \tilde C , 
t \in T^{\sigma_{w,i}} \}$ such that
\[
\zeta^\vee \big( G_\Q^{d+1} (\mc H \rtimes \Gamma) \big) + \zeta^\vee \big( \{ \pi_{\sigma_{w,i}}(t) 
\mid (w,i) \in \tilde C , t \in T^{\sigma_{w,i}} \} \big)
\]
contains a basis of 
\[
\text{span} \{ \pi \in \text{Irr}(X \rtimes W') \mid c \text{ is the central character of } \pi \} 
\subset G_\Q (X \rtimes W') ,
\]
for all generic points $c \in C$. This procedure yields analytic $d$-dimensional families whose 
span in $G_\Q (\mc H \rtimes \Gamma)$ is mapped bijectively to $G_\Q^d (X \rtimes W') \big/ 
G_\Q^{d+1} (X \rtimes W')$ by $\zeta^\vee$. By \eqref{eq:Gsigma} we may take the parameters for 
$\pi_{\sigma_{w,i}}$ in $T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}}$, when we consider these 
representations in $G (\mc H \rtimes \Gamma)$. Let us list some properties of
\begin{equation} \label{eq:6.3}
\{ \pi_{\sigma_{w,i}}(t) \mid w \in \langle W' \rangle , 1 \leq i \leq c(w) ,
t \in T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}} \} .
\end{equation}

\begin{lem}\label{lem:6.3}
\enuma{
\item The parameter space $T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}}$ is isomorphic to 
$T^w_i / Z_{W'}(w)$, as orbifolds.
\item $\pi_{\sigma_{w,i}}(t)$ and $\pi_{\sigma_{w,i}}(t')$ have the same trace if and only if
$t$ and $t'$ lie in the same $\mc G_{\sigma_{w,i}}$-orbit.
\item The family of representations \eqref{eq:6.3} contains no repetitions 
and forms a basis of $G_\Q (\mc H \rtimes \Gamma)$.
}
\end{lem}
\noindent \emph{Proof.}
By the above construction and since different $w \in W'$ act differently on $T$,
\begin{align*}
& \zeta^\vee \big( G_\Q^{d+1} (\mc H \rtimes \Gamma) \big) + 
\zeta^\vee \big( \text{span} \{ \pi_{\sigma_{w,i}}(t) \mid t \in T^{\sigma_{w,i}} \} \big) = \\
& \zeta^\vee \big( G_\Q^{d+1} (X \rtimes W') \big) + 
\zeta^\vee \big( \text{span} \{ \pi_w (t) \mid t \in T^w_i / Z_{W'}(w) \} \big) .
\end{align*}
Hence the parameter space $T^w_i / Z_{W'}(w)$ is diffeomorphic to $T^{\sigma_{w,i}}$
modulo the equivalence relation 
\[
t \sim t' \Longleftrightarrow \pi_{\sigma_{w,i}}(t) = 
\pi_{\sigma_{w,i}}(t') \text{ in } G_\Q (\mc H \rtimes \Gamma) .
\]
By Theorem \ref{thm:6.1}.b $t \sim t'$ if and only if there exists a $g \in \mc G$ with 
$g (P,\delta,ut) = (P,\delta,ut')$, where $\pi_{\sigma_{w,i}}$ is a direct summand of 
$\pi (P,\delta,u)$. By definition any $g \in \mc G_{\sigma_{w,i}}$ yields such equivalences 
for all $t \in T^{\sigma_{w,i}}$, so $T^{\sigma_{w,i}} / \sim$ is a quotient of 
$T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}}$. On the other hand, elements 
$h \in \mc G_{(P,\delta)} \setminus \mc G_{\sigma_{w,i}}$ can only produce such
equivalences on lower dimensional subsets of $T^{\sigma_{w,i}}$. But any such relation which 
does not already come from $\mc G_{\sigma_{w,i}}$ would destroy the orbifold structure of 
$T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}}$, so 
\[
T^w_i / Z_{W'}(w) \cong T^{\sigma_{w,i}} / \sim \, \cong T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}} .
\]
This proves (a) and since we work in $G_\Q (\mc H \rtimes \Gamma)$, it also implies (b).

We noted that \eqref{eq:6.2} contains no repetitions and is a basis of $G_\Q (X \rtimes W')$. 
Since the collection of analytic families 
\[
\{ \zeta^\vee (\pi_{\sigma_{w,i}}(t)) \mid t \in w \in \langle W' \rangle , 
1 \leq i \leq c(w) , t \in T^{\sigma_{w,i}} / \mc G_{\sigma_{w,i}} \}
\]
is parametrized by the same space $\tilde T / W'$, it also enjoys these properties. 
As $\zeta^\vee$ is bijective, these two properties already hold for \eqref{eq:6.3} in 
$G_\Q (\mc H \rtimes \Gamma) . \qquad \Box$
\vspace{2mm}
