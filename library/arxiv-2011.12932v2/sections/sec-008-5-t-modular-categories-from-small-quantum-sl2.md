---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-008-5-t-modular-categories-from-small-quantum-sl2
section_title: "T-modular categories from small quantum sl(2)"
section_number: 5
pages: 9-12
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.958
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:sl_2_sem-sim}

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
