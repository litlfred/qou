---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-001-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 5-7
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.971
---
\subsection{Affine Hecke algebras}
\label{sec:defAHA}

Let $\mf a$ be a finite dimensional real vector space and let $\mf a^*$ be its dual. 
Let $Y \subset \mf a$ be a lattice and $X = \mr{Hom}_\Z (Y,\Z) \subset \mf a^*$ the dual lattice. Let
\[
\mc R = (X, R, Y ,R^\vee ,\Delta) .
\]
be a based root datum. Thus $R$ is a reduced root system in $X ,\, R^\vee \subset Y$ 
is the dual root system and $\Delta$ is a basis of $R$.
Furthermore we are given a bijection $R \to R^\vee ,\: \alpha \mapsto \alpha^\vee$ such 
that $\inp{\alpha}{\alpha^\vee} = 2$ and such that the corresponding reflections
$s_\alpha : X \to X$ (resp. $s^\vee_\alpha : Y \to Y$) stabilize $R$ (resp. $R^\vee$).
We do not assume that $R$ spans $\mf a^*$. 

The reflections $s_\alpha$ generate the Weyl group $W = W (R)$ of $R$, and 
$S_\Delta := \{ s_\alpha \mid \alpha \in \Delta \}$ is the collection of simple reflections. 
We have the affine Weyl group $W^\af = \mh Z R \rtimes W$ 
and the extended (affine) Weyl group $W^e = X \rtimes W$. Both can be considered as groups
of affine transformations of $\mf a^*$. We denote the translation corresponding to $x \in X$ by $t_x$.
As is well known, $W^\af$ is a Coxeter group, and the basis of $R$ gives rise to a set $S^\af$ 
of simple (affine) reflections. More explicitly, let $\Delta_M^\vee$ be the set of maximal elements of
$R^\vee$, with respect to the dominance ordering coming from $\Delta$. Then
\[
S^\af = S_\Delta \cup \{ t_\alpha s_\alpha \mid \alpha^\vee \in \Delta_M^\vee \} .
\]
We write
\begin{align*}
&X^+ := \{ x \in X \mid \inp{x}{\alpha^\vee} \geq 0
\; \forall \alpha \in \Delta \} , \\
&X^- := \{ x \in X \mid \inp{x}{\alpha^\vee} \leq 0
\; \forall \alpha \in \Delta \} = -X^+ .
\end{align*}
It is easily seen that the centre of $W^e$ is the lattice
\[
Z(W^e) = X^+ \cap X^- .
\]
The length function $\ell$ of the Coxeter system $(W^\af ,S^\af )$ extends naturally to $W^e$.
The elements of length zero form a subgroup $\Omega \subset W^e$ and $W^e = W^\af \rtimes \Omega$.
With $\mc R$ we also associate some other root systems. There is the non-reduced root system
\[
R_{nr} := R \cup \{ 2 \alpha \mid \alpha^\vee \in 2 Y \} .
\]
Obviously we put $(2 \alpha )^\vee = \alpha^\vee / 2$. Let $R_l$
be the reduced root system of long roots in $R_{nr}$:
\[
R_l := \{ \alpha \in R_{nr} \mid \alpha^\vee \not\in 2 Y \} .
\]
We introduce a complex parameter function for $\mc R$ in two equivalent ways.
Firstly, it is a map $q : S^\af \to \mh C^\times$ such that $q(s) = q(s')$ if $s$ and $s'$ 
are conjugate in $W^e$. This extends naturally to a map $q : W^e \to \C^\times$ which is
1 on $\Omega$ and satisfies $q(w w') = q(w) q(w')$ if $\ell (w w') = \ell (w) + \ell (w')$.
Secondly, a parameter function is a $W$-invariant map $q : R_{nr}^\vee \to \C^\times$.
The relation between the two definitions is given by
\begin{equation}\label{eq:parameterEquivalence}
\begin{array}{lll}
q_{\alpha^\vee} = q(s_\alpha) = q (t_\alpha s_\alpha) & \text{if} & \alpha \in R \cap R_l, \\
q_{\alpha^\vee} = q(t_\alpha s_\alpha) & \text{if} & \alpha \in R \setminus R_l, \\
q_{\alpha^\vee / 2} = q(s_\alpha) q(t_\alpha s_\alpha)^{-1} & \text{if} & \alpha \in R \setminus R_l. 
\end{array}
\end{equation}
We speak of equal parameters if $q(s) = q(s') \; \forall s,s' \in S^\af$ and of positive parameters if 
$q(s) \in \R_{>0} \; \forall s \in S^\af$. 

We fix a square root $q^{1/2} : S^\af \to \mh C^\times$.
The affine Hecke algebra $\mc H = \mc H (\mc R ,q)$ is the unique associative
complex algebra with basis $\{ N_w \mid w \in W \}$ and multiplication rules
\begin{equation}\label{eq:multrules}
\begin{array}{lll}
N_w \, N_v = N_{w v} & \mr{if} & \ell (w v) = \ell (w) + \ell (v) \,, \\
\big( N_s - q(s)^{1/2} \big) \big( N_s + q(s)^{-1/2} \big) = 0 & \mr{if} & s \in S^\af .
\end{array}
\end{equation}
In the literature one also finds this algebra defined in terms of the
elements $q(s)^{1/2} N_s$, in which case the multiplication can be described without
square roots. This explains why $q^{1/2}$ does not appear in the notation $\mc H (\mc R ,q)$.

Notice that $N_w \mapsto N_{w^{-1}}$ extends to a $\C$-linear anti-automorphism of $\mc H$,
so $\mc H$ is isomorphic to its opposite algebra.
The span of the $N_w$ with $w \in W$ is a finite dimensional Iwahori--Hecke algebra,
which we denote by $\mc H (W,q)$.

Now we describe the Bernstein presentation of $\mc H$. For $x \in X^+$ we put
$\theta_x := N_{t_x}$. The corresponding semigroup morphism 
$X^+ \to \mc H (\mc R ,q)^\times$ extends to a group homomorphism
\[
X \to \mc H (\mc R ,q)^\times : x \mapsto \theta_x .
\]

\begin{thm}\label{thm:1.1}
\textup{(Bernstein presentation)}
\enuma{
\item The sets $\{ N_w \theta_x \mid w \in W , x \in X \}$ and
$\{ \theta_x N_w \mid w \in W , x \in X \}$ are bases of $\mc H$.
\item The subalgebra $\mc A := \mr{span} \{ \theta_x \mid x \in X \}$
is isomorphic to $\mh C [X]$.
\item The centre of $Z(\mc H (\mc R ,q))$ of $\mc H (\mc R ,q)$ is 
$\mc A^{W}$, where we define the action of $W$ on $\mc A$ by 
$w (\theta_x ) = \theta_{wx}$.
\item For $f \in \mc A$ and $\alpha \in \Delta$
\[
f N_{s_\alpha} - N_{s_\alpha} s_\alpha (f) = 
q(s_\alpha)^{-1/2} \big( f - s_\alpha (f) \big)  (q(s_\alpha) c_\alpha - 1) . 
\]
Here the c-functions are defined as
}
\begin{equation*}
c_\alpha = \left\{
\begin{array}{ll}
{\ds \frac{\theta_\alpha + q(s_\alpha )^{-1/2} q (t_\alpha s_\alpha )^{1/2}}{\theta_\alpha + 1} 
\, \frac{\theta_\alpha - q(s_\alpha )^{-1/2} q (t_\alpha s_\alpha )^{-1/2}}{\theta_\alpha - 1} }
 & \alpha \in R \setminus R_l \\
(\theta_\alpha - q(s_\alpha )^{-1}) (\theta_\alpha - 1)^{-1}
& \alpha \in R \cap R_l .
\end{array}
\right.
\end{equation*}
\end{thm}
\emph{Proof.}
These results are due to Bernstein, see \cite[\S 3]{Lus-Gr}. $\qquad \Box$
\\[2mm]

Consider the complex algebraic torus 
\[
T = \mr{Hom}_{\mh Z} (X, \mh C^\times ) \cong Y \otimes_\Z \C^\times ,
\]
so $\mc A \cong \mc O (T)$ and $Z (\mc H ) = \mc A^{W} \cong \mc O (T / W )$. From Theorem 
\ref{thm:1.1} we see that $\mc H$ is of finite rank over its centre. Let $\mf t = \mr{Lie}(T)$ 
and $\mf t^*$ be the complexifications of $\mf a$ and $\mf a^*$. The direct sum
$\mf t = \mf a \oplus i \mf a$ corresponds to the polar decomposition 
\[
T = T_{rs} \times T_{un} = \mr{Hom}_\Z (X, \R_{>0}) \times \mr{Hom}_\Z (X, S^1)
\]
of $T$ into a real split (or positive) part and a unitary part. The exponential map 
$\exp : \mf t \to T$
is bijective on the real parts, and we denote its inverse by $\log : T_{rs} \to \mf a$.

An automorphism of the Dynkin diagram of the based root system $(R,\Delta )$ is a 
bijection $\gamma : \Delta \to \Delta$ such that
\begin{equation}
\inp{\gamma (\alpha )}{\gamma (\beta )^\vee} = \inp{\alpha}{\beta^\vee} 
\qquad \forall \alpha ,\beta \in \Delta \,.
\end{equation}
Such a $\gamma$ naturally induces automorphisms of $R, R^\vee, W$ and 
$W^\af$. It is easy to classify all diagram automorphisms of $(R ,\Delta)$: they permute the
irreducible components of $R$ of a given type, and the diagram automorphisms of a
connected Dynkin diagram can be seen immediately.

We will assume that the action of $\gamma$ on $W^{\af}$ has been extended in
some way to $W^e$, and then we call it a diagram automorphism of $\mc R$. For example, this 
is the case if $\gamma$ belongs to the Weyl 
group of some larger root system contained in $X$. We regard two diagram automorphisms 
as the same if and only if their actions on $W^e$ coincide.

Let $\Gamma$ be a finite group of diagram automorphisms of $\mc R$ and assume that
$q_{\alpha^\vee} = q_{\gamma (\alpha^\vee)}$ for all $\alpha \in R_{nr}$. Then $\Gamma$
acts on $\mc H$ by algebra automorphisms $\psi_\gamma$ that satisfy
\begin{equation}\label{eq:1.2}
\begin{array}{lll@{\quad}l}
\psi_\gamma (N_w) & = & N_{\gamma (w)} & w \in W , \\
\psi_\gamma (\theta_x) & = & \theta_{\gamma (x)} & x \in X .
\end{array}
\end{equation}
Hence one can form the crossed product algebra $\Gamma \ltimes \mc H = \mc H \rtimes \Gamma$, 
whose natural basis is indexed by the group $(X \rtimes W) \rtimes \Gamma = 
X \rtimes (W \rtimes \Gamma)$. It follows easily from \eqref{eq:1.2} and Theorem 
\ref{thm:1.1}.c that $Z(\mc H \rtimes \Gamma) = {\mc A}^{W \rtimes \Gamma}$. We say that 
the central character of an (irreducible) $\mc H \rtimes \Gamma$-representation is positive 
if it lies in $T^{rs} / (W \rtimes \Gamma)$.
\vspace{2mm}
