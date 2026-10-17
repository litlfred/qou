---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-006-4-semisimple-quantum-invariants-and-tqfts
section_title: "Semisimple quantum invariants and TQFTs"
section_number: 4
pages: 7-16
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.973
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:TQFT_sem-sim}

The diagrammatic interpretation for morphisms of ribbon categories which was discussed earlier highlights the fundamental interplay between algebra and topology arising in this context. In fact, it is a result of Turaev that certain topological gadgets called \textit{ribbon graphs} provide the relevant topological structure underlying Penrose graphical notation \cite[Thm.~I.2.5]{T94}. Indeed, isotopy classes of ribbon graphs can be organised as morphisms of a category $\calR_\calC$, and the graphical calculus introduced above can be implemented by a functor
\[
 F_\calC : \calR_\calC \to \calC
\]
called the \textit{Reshetikhin--Turaev functor}. This technology plays a fundamental role in every construction discussed in this survey.

Starting from a T-modular category $\calC$, Turaev showed how to construct a topological invariant $\RT_\calC$ of closed oriented 3-manifolds decorated with closed\footnote{A ribbon graph is \textit{closed} if it has no boundary vertices, and thus represents an endomorphism of the tensor unit $\one$ of $\calC$ under the Reshetikhin--Turaev functor $F_\calC$.} ribbon graphs. By their very definition, ribbon graphs have a rather hybrid nature, between topology and algebra. This of course can be seen as a strenght of the theory, which allows for great flexibility. However, for the benefit of those who are looking for a purely topological point of view, the construction can be understood as producing, in particular, a family $\{ \RT_V \}_{V \in \calC}$ of topological invariants of framed oriented links inside 3-manifolds, where each invariant $\RT_V$ is obtained by choosing the object $V \in \calC$ as a label for every component of the link. The definition of these topological invariants is based on surgery presentations, which allow us to interpret framed links in $S^3$ as closed oriented 3-manifolds. The main idea consists in choosing orientations and labels for a surgery presentation, and then using the Reshetikhin--Turaev functor $F_\calC$ in order to extract a scalar. The choice needs to be made in such a way that the resulting scalar is invariant under orientation reversals and Kirby moves. Turaev came up with such a label, which is given by a formal linear combination of objects of $\calC$ called the \textit{Kirby color}, and given by
\[
 \Omega := \sum_{i \in I} \dim_\calC(V_i) \cdot V_i,
\]
where again $\Gamma(\calC) = \left\{ V_i \mid i \in I \right\}$ is a set of representatives of isomorphism classes of simple objects of $\calC$, and where
\[
 \dim_\calC(X) = \tr_\calC(\id_X) = \rev_X \circ \lcoev_X
\]
is the \textit{categorical dimension} of an object $X \in \calC$, which coincides with the \textit{categorical trace} of its identity endomorphism. Labeling components of a framed oriented link using the Kirby color is a shortcut that has to be understood through multilinear expansions. More precisely, if $L$ is a framed oriented link featuring a component $K$ labeled by $\Omega$, and if $L_i$ is obtained from $L$ by replacing the label of $K$ with $V_i \in \Gamma(\calC)$, then we set
\[
 F_\calC(L) := \sum_{i \in I} \dim_\calC(V_i) F_\calC(L_i).
\]
This oriented framed link invariant is already preserved under Kirby II moves, as the terminology might suggest. In order to obtain invariance under Kirby I moves, we need a normalization coefficient. This is defined in terms of the so-called \textit{stabilization coefficients}
\[
 \Delta_+ := F_\calC \left( \pic{stabilization_coeff_+_black} \right) \in \Bbbk, \qquad
 \Delta_- := F_\calC \left( \pic{stabilization_coeff_-_black} \right) \in \Bbbk.
\]
As a consequence of T-modularity, their product $\Delta_+ \Delta_-$ is invertible, and so we can choose two parameters $\calD,\delta \in \Bbbk^\times$ satisfying
\[
 \calD^2 = \Delta_+ \Delta_-, \qquad 
 \delta = \frac{\Delta_+}{\calD} = \frac{\calD}{\Delta_-}.
\]
The definition of the topological invariant $\RT_\calC$ depends on the choice of $\calD$, which uniquely determines $\delta$. If $M$ is a closed oriented 3-manifold, if $T \subset M$ is a closed ribbon graph, and if $L \subset S^3$ is a surgery presentation of $M$, which we assume having $\ell$ components and signature $\sigma$, and which we equip with an arbitrary orientation and the label $\Omega$ on every component, then
\[
 \RT_\calC(M,T) := \calD^{-1-\ell} \delta^{-\sigma} F_\calC(L \cup T)
\]
is a topological invariant of the pair $(M,T)$.

The universal construction of \cite{BHMV95} extends the invariant $\RT_\calC$ to a dual pair of TQFTs given by a covariant functor $\rmV_\calC$ and a contravariant one $\rmV'_\calC$. This means that, for a closed oriented surface $\Sigma$, we obtain dual vector spaces $\rmV_\calC(\Sigma)$ and $\rmV'_\calC(\Sigma)$ supporting respectively left and right actions of decorated cobordisms. If $\bar{\Sigma}$ is obtained from $\Sigma$ by reversing its orientation, we have a natural isomorphism $\rmV'_\calC(\Sigma) \cong \rmV_\calC(\bar{\Sigma})$. This means we can simply focus on the covariant TQFT $\rmV_\calC$. If $\Sigma_g$ is a closed oriented surface of genus $g$, then
\begin{equation}\label{E:st_sp_sem-sim}
 \rmV_\calC(\Sigma_g) \cong \bigoplus_{i_1,\ldots,i_g \in I} \calC \left( \one,\bigotimes_{j=1}^g V_{i_j} \otimes V_{i_j}^* \right).
\end{equation}
Since $\calC$ is semisimple, this vector space can be rewritten, using fusion rules, in terms of labelings of trivalent graphs, with different graphs determining different decompositions. If $\calG$ is an oriented trivalent graph, whose sets of vertices and egdes are denoted $\calV$ and $\calE$ respectively, then, for every vertex $v \in \calV$, we denote with $v_-$ the set of incoming germs of edges with target $v$, and we denote with $v_+$ the set of outgoing germs of edges with source $v$. A fundamental labeling of $\calE$ is a function $i : \calE \rightarrow I$, and for every $v \in \calV$ the morphism space
\[
 \calC(i,v) := \calC \left( \bigotimes_{e \in v_-} V_{i(e)},\bigotimes_{e \in v_+} V_{i(e)} \right)
\]
is called the \textit{multiplicity module} of $i$ in $v$. Then, let us consider the embedded oriented trivalent graph
\begin{equation}\label{E:triv_graph}
 \calG_g := \pic{trivalent_graph} \subset \R^3, 
\end{equation}
and let us denote with $\calV_g$ and $\calE_g$ its sets of vertices and edges respectively. We should think of $\Sigma_g$ as being identified with the boundary of a regular neighborhood of $\calG_g$. Then, the state space $\rmV_\calC(\Sigma_g)$ decomposes as a direct sum of tensor products of multiplicity modules
\begin{equation}\label{E:E:st_sp_sem-sim_dec}
 \rmV_\calC(\Sigma_g) \cong \bigoplus_{i : \calE_g \to I} \bigotimes_{v \in \calV_g} \calC(i,v).
\end{equation}


\section{T-modular categories from small quantum \texorpdfstring{$\mathfrak{sl}_2$}{sl(2)}}\label{S:sl_2_sem-sim}

The Witten--Reshetikhin--Turaev TQFT was first constructed from the restricted quantum group of $\fsl_2$ at even roots of unity. A careful exposition can be found in \cite{T94}, while a popular alternative construction, based on Jones--Kauffman skein theory, can be found in \cite{BHMV95}. This skein construction also produces TQFTs when the quantum parameter is an odd root of unity. Referring to Witten's gauge picture, these are called $\SO(3)$-TQFTs. We choose this family as a demonstrative example, and develop in this section the construction of the underlying modular categories, corresponding to the so-called small quantum group of $\fsl_2$ at odd roots of unity.

We start by fixing an odd integer $3 \leqs r \in \Z$, and we consider the primitive $r$th root of unity $q = e^{\frac{2 \pi i}{r}}$. For every integer $k \geqs 0$ we introduce the notation 
\[
 \{ k \} := q^k - q^{-k},
 \quad \{ k \}' := q^k + q^{-k},
 \quad [k] := \frac{\{ k \}}{\{ 1 \}},
 \quad [k]! := \prod_{j=1}^k [j].
\]
The small quantum group $\bar{U}_q \fsl_2$, first defined by Lusztig in \cite{Lu90}, can be constructed as the $\C$-algebra with generators $\{ E,F,K \}$ and relations
\begin{gather*}
 E^r = F^r = 0, \qquad K^r = 1, \\*
 K E K^{-1} = q^2 E, \qquad K F K^{-1} = q^{-2} F, \qquad [E,F] = \frac{K - K^{-1}}{q-q^{-1}},
\end{gather*}
and with Hopf algebra structure obtained by setting
\begin{align*}
 \Delta(E) &= E \otimes K + 1 \otimes E, & \varepsilon(E) &= 0, & S(E) &= -E K^{-1}, \\*
 \Delta(F) &= K^{-1} \otimes F + F \otimes 1, & \varepsilon(F) &= 0, & S(F) &= - K F, \\*
 \Delta(K) &= K \otimes K, & \varepsilon(K) &= 1, & S(K) &= K^{-1}.
\end{align*}
Remark that Lusztig considers the opposite coproduct, while we are using the one of Kassel \cite[Sec.~VII.1]{K95}. A basis of $\bar{U}_q \fsl_2$ is given by
\[
 \left\{ E^a F^b K^c \mid \ 0 \leqs a,b,c \leqs r - 1 \right\},
\]
as proved in \cite[Thm.~5.6]{Lu90}. Furthermore, $\bar{U}_q \fsl_2$ supports the structure of a ribbon Hopf algebra. Indeed, an \textit{R-matrix} $R \in \bar{U}_q \fsl_2 \otimes \bar{U}_q \fsl_2$ is given by
\begin{align*}
 R &:= \frac{1}{r} \sum_{a,b,c=0}^{r-1} \frac{\{ 1 \}^a}{[a]!}
 q^{\frac{a(a-1)}{2} - 2bc} K^b E^a \otimes K^c F^a, \\*
 R^{-1} &\phantom{:}= \frac{1}{r} \sum_{a,b,c=0}^{r-1} \frac{\{ -1 \}^a}{[a]!}
 q^{-\frac{a(a-1)}{2} + 2bc} E^a K^b \otimes F^a K^c,
\end{align*}
while a \textit{ribbon element} $v \in \bar{U}_q \fsl_2$ is given by
\begin{align*}
 v &:= \frac{i^{\frac{r-1}{2}}}{\sqrt{r}} \sum_{a,b = 0}^{r - 1} \frac{\{ -1 \}^a}{[a]!} q^{-\frac{a(a-1)}{2} + \frac{(r+1)(a-b-1)^2}{2}} F^a K^b E^a, \\*
 v^{-1} &\phantom{:}= \frac{i^{-\frac{r-1}{2}}}{\sqrt{r}} \sum_{a,b = 0}^{r - 1} \frac{\{ 1 \}^a}{[a]!} q^{\frac{a(a-1)}{2} + \frac{(r-1)(a+b-1)^2}{2}} F^a K^b E^a.
\end{align*}
An explicit formula for $R$ first appeared in \cite[Sec.~3.5]{R93}, see also \cite[Sec.~4.5]{Oh02} for a different one. The expression for $v$ reported here can be obtained by adapting the proof of \cite[Thm.~4.1.1]{FGST05}. A \textit{pivotal element} $g \in \bar{U}_q \fsl_2$ is given by $g := K$. It is proved in \cite[Prop.~XIV.6.5]{K95} that this choice defines a compatible ribbon structure, in the sense that $v = ug^{-1}$ for the \textit{Drinfeld element} $u \in \bar{U}_q \fsl_2$ given by $u := S(R'')R'$, where the notation $R = R' \otimes R''$ hides a sum. Thus the category $\calC = \mods{\bar{U}_q \fsl_2}$ of finite-dimensional left $\bar{U}_q \fsl_2$-modules is a ribbon category.

For every integer $0 \leqs n \leqs r-1$ we denote with $V_n$ the $\bar{U}_q \fsl_2$-module with basis 
\[
 \{ a_i^n \in V_n \mid 0 \leqs i \leqs n \}
\]
and action given, for all integers $0 \leqs i \leqs n$, by
\begin{equation*}
 \begin{split}
  K \cdot a_i^n &= q^{n-2i} a_i^n, \\
  E \cdot a_i^n &= [i][n-i+1] a_{i-1}^n, \\
  F \cdot a_i^n &= a_{i+1}^n,
 \end{split}
\end{equation*}
where $a_{-1}^n := a_{n+1}^n := 0$. These $\bar{U}_q \fsl_2$-modules are all simple and self-dual, and every simple object of $\calC$ is isomorphic to $V_n$ for some $0 \leqs n \leqs r-1$. Their categorical dimension is
\[
 \dim_\calC(V_n) = \tr_\calC(\id_{V_n}) = [n+1].
\]
We will see later that the category $\calC$ is not semisimple. However, starting from $\calC$, we can obtain a fusion category as follows. Let us set
\[
 I = \left\{ 2n \Bigm\vert 0 \leqs n \leqs \frac{r-3}{2} \right\},
\]
let us consider the set of simple objects
\[
 \Gamma(\bar{\calC}) = \{ V_i \in \calC \mid i \in I \}, 
\] 
and let $\tilde{\calC}$ denote the full monoidal subcategory of $\calC$ generated by $\Gamma(\bar{\calC})$. A morphism $f \in \calC(V,W)$ is \textit{negligible} if
\[
 \tr_\calC(g \circ f) = 0
\]
for every morphism $g \in \calC(W,V)$. An example of a negligible morphism is the identity $\id_{V_{r-1}}$ of the so-called \textit{Steinberg module} $V_{r-1}$. Negligible morphisms of $\tilde{\calC}$ form a linear congruence\footnote{The term \textit{tensor ideal} is often used instead. Remark however that there are two concurring notions of tensor ideal, with the other one arising in the context of modified traces. In order to avoid confusion, we use Mac Lane's terminology here.} $\calN(\tilde{\calC})$ in $\tilde{\calC}$, see \cite[Sec.~II.8]{M71}. This means that we can define a quotient category $\bar{\calC} := \tilde{\calC} / \calN(\tilde{\calC})$ whose objects coincide with those of $\tilde{\calC}$, and whose morphism spaces are given by
\[
 \bar{\calC}(V,W) := \tilde{\calC}(V,W)/\calN(\tilde{\calC})(V,W).
\]

\begin{proposition}
 The category $\bar{\calC}$ is T-modular.
\end{proposition}

\begin{proof}
 It follows from \cite[Cor.~4.1]{A92} that $\bar{\calC}$ is semisimple. This means that $\bar{\calC}$ is a ribbon fusion category, and we only need to check that its S-matrix $S(\bar{\calC})$ is invertible. Thanks to \cite[Prop.~1.1]{B00}, this happens if and only if none of the columns of $S(\bar{\calC})$ is colinear to the one corresponding to the tensor unit $\one$. Then, let us consider the matrix
 \[
  S(\calC) := \left( \pic{S-matrix} \right)_{0 \leqs i,j \leqs r-1}.
 \]
 It follows from an easy computation, which mimics \cite[Lem.~3.27]{KM91}, that
 \[
  S(\calC)_{i,j} = [(i+1)(j+1)]
 \]
 for all $0 \leqs i,j \leqs r-1$. Remark that this formula explains why we need to restrict ourselves to the full subcategory $\tilde{\calC}$ of $\calC$. Indeed, the column $(S_{i,j})_{0 \leqs j \leqs r-1}$ is colinear to the column $(S_{r-i-2,j})_{0 \leqs j \leqs r-1}$ for every integer $0 \leqs i \leqs r-1$.  We claim now that the S-matrix $S(\bar{\calC})$ is given by the submatrix 
 \[
  S := \left( S(\calC)_{2i,2j} \right)_{0 \leqs i,j \leqs \frac{r-3}{2}}
 \]
 of $S(\calC)$. The fact that no column of $S$ is colinear to the first one follows from
 \begin{align*}
  &\sum_{i=0}^{\frac{r-3}{2}} [2i+1] S_{i,j} = \sum_{i=0}^{\frac{r-3}{2}} [2i+1][(2i+1)(2j+1)] \\
  &\hspace*{\parindent} = \frac 12 \left( \sum_{i=0}^{\frac{r-3}{2}} [2i+1][(2i+1)(2j+1)] + \sum_{i=0}^{\frac{r-3}{2}} [2i+1][(2i+1)(2j+1)] \right) \\
  &\hspace*{\parindent} = \frac 12 \left( \sum_{i=0}^{\frac{r-3}{2}} [2i+1][(2i+1)(2j+1)] + \sum_{i=0}^{\frac{r-3}{2}} [r-2i-1][(r-2i-1)(2j+1)] \right) \\
  &\hspace*{\parindent} = \frac 12 \left( \sum_{i=0}^{\frac{r-3}{2}} [2i+1][(2i+1)(2j+1)] + \sum_{i=1}^{\frac{r-1}{2}} [2i][2i(2j+1)] \right) \\
  &\hspace*{\parindent} = \frac 12 \sum_{i=0}^{r-1} [i][i(2j+1)] 
  = \frac 12 \sum_{i=0}^{r-1} \frac{\{ i \} \{ i(2j+1) \}}{\{ 1 \}^2} 
  = \frac 12 \sum_{i=0}^{r-1} \frac{\{ 2i(j+1) \}' - \{ 2ij \}'}{\{ 1 \}^2} \\ 
  &\hspace*{\parindent} = - \delta_{0,j} \frac{r}{\{ 1 \}^2}. \qedhere
 \end{align*}
\end{proof}

It follows then from the construction that $\Gamma(\bar{\calC})$ is a set of representatives of isomorphism classes of simple objects of $\bar{\calC}$. A direct computation gives the \textit{stabilization parameters}
\begin{align*}
 \Delta_- &= -\frac{i^{\frac{r-1}{2}} r^{\frac 12} q^{\frac{r+3}{2}}}{\{ 1 \}}, &
 \Delta_+ &= \frac{i^{-\frac{r-1}{2}} r^{\frac 12} q^{\frac{r-3}{2}}}{\{ 1 \}},
\end{align*}
and we fix the square root
\[
 \calD = \frac{i r^{\frac 32}}{\{ 1 \}}
\]
of the product $\Delta_+ \Delta_-$, which uniquely determines the coefficient
\[
 \delta = i^{-\frac{r+1}{2}} q^{\frac{r-3}{2}},
\]
as well as the corresponding normalization of $\RT_{\bar{\calC}}$. 

Thanks to equation \eqref{E:E:st_sp_sem-sim_dec}, state spaces of closed oriented surfaces for the TQFT $\rmV_{\bar{\calC}}$ extending $\RT_{\bar{\calC}}$ can be written as direct sums of tensor products of multiplicity modules. It turns out that all multiplicity modules in $\bar{\calC}$ have dimension at most one. In particular, if $\Sigma_g$ is a closed oriented surface of genus $g$, then a basis of $\rmV_{\bar{\calC}}(\Sigma_g)$ is determined by so-called $r$-triangular labelings of the set of edges $\calE_g$ of the graph $\calG_g$ represented in \eqref{E:triv_graph}. If $v \in \calV_g$ is a vertex, and $v_- \cup v_+ = \{ e,e',e'' \}$ is the set of germs of edges which are incident to $v$, then a labeling $i : \calE_g \rightarrow I$ is said to be \textit{$r$-triangular in $v$} if it satisfies the inequalities
\begin{equation*}
 \lvert i(e')-i(e'') \rvert \leqs i(e) \leqs i(e')+i(e''), \qquad i(e)+i(e')+i(e'') < 2r-2.
\end{equation*}
A labeling $i : \calE_g \rightarrow I$ is \textit{$r$-triangular}\footnote{Such a labeling is called \textit{$r$-admissible} in \cite{BHMV95}, but we change terminology here because admissibility will be a different condition, and a key one, in the non-semisimple construction.} if it is $r$-triangular in every $v \in \calV_g$. Thanks to the next statement, the dimension of $\rmV_{\bar{\calC}}(\Sigma_g)$ is obtained by counting $r$-triangular labelings of $i : \calE_g \rightarrow I$.

\begin{proposition}
 The multiplicity module
 \[
  \bar{\calC}(i,v) \cong \bar{\calC}(\one,V_{i(e)} \otimes V_{i(e')} \otimes V_{i(e'')})
 \]  
 has dimension one if $i$ is $r$-triangular in $v$, and zero otherwise.
\end{proposition}

\begin{proof}
 Since $\bar{\calC}$ is a fusion category, the dimension of $\bar{\calC}(\one,V_{i(e)} \otimes V_{i(e')} \otimes V_{i(e'')})$ is equal to the multiplicity of $V_{i(e)}^* \cong V_{i(e)}$ in the decomposition of $V_{i(e')} \otimes V_{i(e'')}$ in $\bar{\calC}$. The decomposition of $V_{i(e')} \otimes V_{i(e'')}$ into a sum of indecomposable $\bar{U}_q \fsl_2$-modules in $\calC$ is given by
 \[
  V_{i(e')} \otimes V_{i(e'')} \cong \bigoplus_{n = \frac{\lvert i(e')-i(e'') \rvert}{2}}^{\min \left\{ \frac{i(e')+i(e'')}{2},r-\frac{i(e')+i(e'')}{2}-2 \right\}} V_{2n} \oplus \bigoplus_{n = r-\frac{i(e')+i(e'')}{2}-1}^{\frac{r-1}{2}} P_{2n},
 \]
 where $P_{2n}$ is the projective cover of $V_{2n}$, see Section \ref{S:sl_2_non-sem-sim}. A similar formula for even values of $r$ is established in \cite{S92}, and the proof can be adapted. Since $P_{2n}$ is a direct summand of $V_{r-1} \otimes V_{r-1}$, its identity is negligible. In particular, the decomposition of $V_{i(e')} \otimes V_{i(e'')}$ in the category $\bar{\calC}$ reduces to
 \[
  V_{i(e')} \otimes V_{i(e'')} \cong \bigoplus_{n = \frac{\lvert i(e')-i(e'') \rvert}{2}}^{\min \left\{ \frac{i(e')+i(e'')}{2},r-\frac{i(e')+i(e'')}{2}-2 \right\}} V_{2n}.
 \]
 This proves the proposition.
\end{proof}

As an example, the state space of the torus $\Sigma_1 = S^1 \times S^1$ has dimension
\[
 \dim_\C \rmV_\calC(\Sigma_1) = \frac{r-1}{2}.
\]
Since every Dehn twist is sent to (the projective class of) a matrix of finite order, the projective representation of the genus one mapping class group $\MCG(\Sigma_1)$ in $\PGL_\C(\rmV_\calC(\Sigma_1))$ is never faithful, although it has very interesting asymptotic faithfulness properties as $r$ tends to infinity, see \cite[Thm.~1]{A02}.


\section{Lyubashenko's notion of modular category}\label{S:L-mod_cat}

An \textit{L-modular category} (L for Lyubashenko) can be defined as a finite ribbon category whose Müger center is trivial. Remark that this is not the original definition of Lyubashenko, but it is equivalent to it. This is a consequence of a result of Shimizu \cite{S16}, who compared several notions of non-degeneracy for the braiding of a finite ribbon category, proving the equivalence of four different conditions. Among these, we can find Lyubashenko's original one, as well as the short property used above. This formulation makes it clear that T-modular categories are just semisimple L-modular categories.

In order to review Lyubashenko's definition, let $\calC$ be a finite ribbon category, and let us consider the functor $\calH : \calC^\op \times \calC \to \calC$ determined by $(X,Y) \mapsto X^* \otimes Y$. We recall the classical notion of a \textit{dinatural transformation of source $\calH$}, which is given by an object $Z \in \calC$ equipped with a family $\{ d_X : X^* \otimes X \to Z \}_{X \in \calC}$ of morphisms of $\calC$ satisfying
\[
 d_X \circ (f^* \otimes \id_X) = d_Y \circ (\id_{Y*} \otimes f)
\]
for every morphism $f : X \to Y$ of $\calC$, see \cite[Sec.~IX.4]{M71}. We usually abuse notation, and simply denote dinatural transformations by their underlying objects. The \textit{coend of $\calH$} is the universal dinatural transformation of source $\calH$, which means it is an object $\calL \in \calC$ with a dinatural family of structure morphisms $i_X : X^* \otimes X \to \calL$ satisfying the following condition: for every dinatural transformation $Z$ of source $\calH$ there exists a unique morphism $\ell_Z : \calL \to Z$ such that the diagram
\begin{equation}\label{E:univ_prop_coend}
 \begin{tikzpicture}[descr/.style={fill=white},baseline=(current  bounding  box.center)]
  \node (P0) at (135:{sqrt(2)*2.5}) {$Y^* \otimes X$};
  \node (P1) at (90:2.5) {$X^* \otimes X$};
  \node (P2) at (180:2.5) {$Y^* \otimes Y$};
  \node (P3) at (0:0) {$\calL$};
  \node (P4) at (-45:{2.5/sqrt(2)}) {$Z$};
  \draw
  (P0) edge[->] node[above] {\scriptsize $f^* \otimes \id_X$} (P1)
  (P1) edge[->] node[right] {\scriptsize $i_X$} (P3)
  (P0) edge[->] node[left] {\scriptsize $\id_{Y^*} \otimes f$} (P2)
  (P2) edge[->] node[below] {\scriptsize $i_Y$} (P3)
  (P1) edge[bend left,->] node[right] {\scriptsize $d_X$} (P4)
  (P2) edge[bend right,->] node[below] {\scriptsize $d_Y$} (P4)
  (P3) edge[->] node[descr] {\scriptsize $\ell_Z$} (P4);
 \end{tikzpicture}
\end{equation}
commutes for every morphism $f : X \to Y$ of $\calC$. It has been proved by Majid \cite{M91a} and Lyubashenko \cite{L95,L99} that, since $\calC$ is a finite ribbon category, the coend of $\calH$ always exists, and furthermore it supports the structure of a braided Hopf algebra in $\calC$. This means that it admits:
\begin{enumerate}
 \item a product $\mu : \calL \otimes \calL \to \calL$ and a unit $\eta : \one \to \calL$;
 \item a coproduct $\Delta : \calL \to \calL \otimes \calL$ and a counit $\epsilon : \calL \to \one$;
 \item an antipode $S : \calL \to \calL$.
\end{enumerate}
All these structure morphisms are uniquely determined by the universal property~\eqref{E:univ_prop_coend} of $\calL$. Indeed, they can be defined as the unique morphisms of $\calC$ that satisfy
\begin{gather*}
 \pic{Hopf_algebra_structure_1} \\[5pt]
 \pic{Hopf_algebra_structure_2} \\[5pt]
 \pic{Hopf_algebra_structure_3}
\end{gather*}
for all $X,Y \in \calC$. Remark that the product $\mu$ is actually determined by a universal property satisfied by the so-called \textit{double coend} $\calL \otimes \calL$, and it requires a Fubini theorem for coends \cite[Prop.~IX.8]{M71} whose name comes from the standard notation
\[
 \calL = \int^{X \in \calC} X^* \otimes X,
\]
see also \cite[Prop.~5.1.2]{KL01}. We should point out that, dually, every finite ribbon category $\calC$ also admits an \textit{end}
\[
 \calE = \int_{X \in \calC} X \otimes X^*,
\]
which is similarly defined as a universal dinatural transformation, see Appendix \ref{A:end} for details. Equivalent constructions can be carried out exploiting the properties of $\calE$, which are completely analogous to those of $\calL$, and it is for historical reasons that we focus on $\calL$ instead of $\calE$, following Lyubashenko.

From a topological point of view, what we said so far hints at the fact that the universal property \eqref{E:univ_prop_coend} of the coend $\calL$ provides an alternative to the Reshetikhin--Turaev functor for extracting morphisms of $\calC$ from diagrams of certain framed oriented tangles. For instance, a Hopf pairing $\omega : \calL \otimes \calL \to \one$ is uniquely determined by the equality
\[
 \pic{Hopf_pairing}
\]
for all $X,Y \in \calC$. Then, following Lyubashenko's original definition, an L-modular category is a finite ribbon category for which the Hopf pairing $\omega$ is non-degenerate, meaning that it induces an isomorphism between $\calL$ and $\calL^*$. Remark how similar the defining diagram for $\omega$ is with respect to the one defining the S-matrix of Turaev. In fact, when $\calC$ is semisimple, then Prop.~\ref{P:end_fusion} and \cite[Lem.~2]{K96a} give
\[
 \calE \cong \bigoplus_{i \in I} V_i \otimes V_i^*, \qquad 
 \calL \cong \bigoplus_{i \in I} V_i^* \otimes V_i,
\]
and $\omega$ is non-degenerate if and only if the S-matrix is invertible \cite[Prop.~7.4.3]{KL01}. 


An alternative condition for the modularity of $\calC$ is that a certain morphism $D : \calL \to \calE$ called the \textit{Drinfeld map} is an isomorphism, see \cite[Prop.~4.11]{FGR17}. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional ribbon Hopf algebra $H$, then let us denote with $\ad$ the \textit{adjoint representation} of $H$, which is given by the vector space $H$ equipped with the adjoint left $H$-action defined by
\[
 \ad_x(y) = x_{(1)}yS(x_{(2)})
\]
for all $x,y \in H$, where we are using Sweedler's notation $\Delta(x) = x_{(1)} \otimes x_{(2)}$ for the coproduct. Similarly, let us denote with $\coad$ the \textit{coadjoint representation} of $H$, which is given by the vector space $H^*$ equipped with the coadjoint left $H$-action defined by
\[
 \coad_x(\phi)(y) = \phi(S(x_{(1)})yx_{(2)})
\]
for all $x,y \in H$ and $\phi \in H^*$. Then Prop.~\ref{P:end_H-mod} and \cite[Lem.~3]{K96a} give
\[
 \calE \cong \ad, \qquad \calL \cong \coad.
\]
In this setting, the Drinfeld map $D : \coad \to \ad$ was first defined in \cite[Prop.~3.3]{D90} as the $H$-module morphism determined by $D(\phi) := (\phi \otimes \id_H)(R_{21}R_{12})$, where $R_{12} = R \in H \otimes H$ is the R-matrix of $H$, and $R_{21} \in H \otimes H$ is obtained from $R$ by reversing the order of its components. The element $M = R_{21}R_{12} \in H \otimes H$ is sometimes called the \textit{M-matrix}, or \textit{monodromy matrix}, of $H$. By definition, $H$ is \textit{factorizable} if $D$ is an isomorphism.

When $\calC$ is modular, an \textit{integral} of the coend $\calL$ is a morphism\footnote{The source of $\Lambda$ might be a different invertible object in general, called the \textit{object of integrals}, but here we are supposing $\calC$ is modular.} $\Lambda : \one \to \calL$ satisfying
\[
 \mu \circ (\Lambda \otimes \id_\calL) = \Lambda \circ \epsilon = \mu \circ (\id_\calL \otimes \Lambda).
\]
In analogy with Sweedler's result for Hopf algebras in the category of finite-di\-men\-sion\-al vector spaces, the coend $\calL$ admits an integral, which is unique up to scalar \cite[Thm.~6.1]{L95}. When $\calC$ is semisimple, then, up to scalar, we have
\[
 \Lambda = \left( \dim_\calC(V_i) \cdot \rcoev_{V_i} \right)_{i \in I},
\]
which means that we can think of an integral $\Lambda$ of the coend $\calL$ as extending the Kirby color to the non-semisimple case. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional factorizable ribbon Hopf algebra $H$, then, up to scalar, we have
\[
 \Lambda(1) = \lambda \in H^*,
\]
where $\lambda \in H^*$ is a classical right integral on the Hopf algebra $H$. See \cite[Sec.~2.5]{K96a} for both claims.

The algebraic setup discussed up to here is sufficient to perform Lyubashenko's construction, but in order to obtain TQFTs, we also need the theory of modified traces. Let us present the key definitions by focusing on a relevant special case. We denote by $\Proj(\calC)$ the full subcategory of projective objects of $\calC$, which forms a \textit{tensor ideal} in $\calC$, in the sense that it is closed under retracts and absorbent under tensor products, see \cite[Def.~3.1.1]{GKP10}. A \textit{trace} on $\Proj(\calC)$ is a family of linear maps
\[
 \rmt := \{ \rmt_P : \End_\calC(P) \to \Bbbk \}_{P \in \Proj(\calC)}
\]
satisfying:
\begin{enumerate}
 \item \textit{Cyclicity}: $\rmt_P \left( \pic{m-trace_cyclicity_1} \right) = \rmt_Q \left( \pic{m-trace_cyclicity_2} \right)$ \par \bigskip
  for all $P,Q \in \Proj(\calC)$, $f \in \calC(P,Q)$, and $g \in \calC(Q,P)$; 
  \bigskip
 \item \textit{Partial trace}: $\rmt_{P \otimes X} \left( \pic{m-trace_partial_trace_1} \right) = \rmt_P \left( \pic{m-trace_partial_trace_2} \right)$ \par \bigskip
  for all $P \in \Proj(\calC)$, $X \in \calC$, and $f \in \End_{\calC}(P \otimes X)$.
\end{enumerate}
We say a trace $\rmt$ on $\Proj(\calC)$ is \textit{non-degenerate} if, for all $P \in \Proj(\calC)$ and $X \in \calC$, the bilinear pairing $\rmt_P(\_ \circ \_) : \calC(X,P) \times \calC(P,X) \to \Bbbk$ determined by $(g,f) \mapsto \rmt_P(g \circ f)$ is non-degenerate. Thanks to \cite[Cor.~5.6]{GKP18}, for a modular\footnote{The statement is a particular case of a much more general existence and uniqueness result, see \cite[Thm.~5.5]{GKP18}.} category $\calC$ there exists a trace $\rmt$ on $\Proj(\calC)$, which is unique up to scalar and furthermore non-degenerate. When $\calC$ is semisimple, then $\Proj(\calC) = \calC$, and the standard categorical trace $\tr_\calC$ is the unique trace on $\calC$ up to scalar. When $\calC$ is the category $\mods{H}$ of finite-dimensional representations of a finite-dimensional factorizable\footnote{Again, hypotheses for this result can be considerably relaxed, but we prefer to avoid introducing more terminology.} ribbon Hopf algebra $H$, there is a natural correspondence between the space of traces on $\Proj(\calC)$ and the spaces of so-called \textit{symmetrized} integrals on $H$, see \cite[Thm.~1]{BBG18}.
