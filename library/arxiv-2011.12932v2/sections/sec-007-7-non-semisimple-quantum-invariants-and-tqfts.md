---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-007-7-non-semisimple-quantum-invariants-and-tqfts
section_title: "Non-semisimple quantum invariants and TQFTs"
section_number: 7
pages: 16-20
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.97
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:TQFT_non-sem-sim}

Using the coend $\calL$ and the integral $\Lambda$, it is possible to develop a diagrammatic calculus which steps outside of the framework provided by the Reshetikhin--Turaev functor. This time, the topological gadgets underlying this graphical notation are called \textit{bichrome graphs}. Very roughly speaking, bichrome graphs are ribbon graphs whose edges can be of two kinds, either \textit{red} (and unlabeled) or \textit{blue} (and labeled as usual by objects of $\calC$). Similarly, coupons (which, for standard ribbon graphs, correspond to boxes like the one represented in \eqref{E:coupon}) are partitioned in two groups, according to the edges they meet, and can thus be either \textit{bichrome} (and unlabeled) or \textit{blue} (and labeled as usual by morphisms of $\calC$). These ribbon graphs are subject to certain restrictions, see \cite[Sec.~3.1]{DGGPR19} for details. An example of a bichrome graph, with red components represented as dashed-dotted lines, is given by
\[
 \pic{bichrome_graph}
\]
This can be understood as representing a morphism of $\calC$ with source $V^* \otimes U$ and target $\calL \otimes W^*$. Indeed, just like standard ribbon graphs, bichrome graphs can be arranged as morphisms of a category\footnote{Our notation for the category of bichrome graphs $\calR_\Lambda$ features the integral $\Lambda$ in order to highlight the relevant functor this category supports, but remark that the definition of $\calR_\Lambda$ itself is actually independent of the choice of $\Lambda$.} $\calR_\Lambda$, and we can interpret $\calR_\calC$ as the subcategory whose morphisms are exclusively blue bichrome graphs. Then, the idea behind bichrome graphs is essentially the following: on the one hand, the red part of the graph should be interpreted as prescribing surgery instructions, and it has to be processed through Lyubashenko's algorithm, that is, invoking the universal property \eqref{E:univ_prop_coend} of the coend $\calL$, in order to extract a morphism of $\calC$ (red minima of diagrams translate to the integral $\Lambda$ under this correspondence); on the other hand, the blue part supports the standard graphical calculus implemented by the Reshetikhin--Turaev functor. There exists a coherent way of harmonizing the two approaches, which is realized by a functor
\[
 F_\Lambda : \calR_\Lambda \to \calC
\]
restricting to $F_\calC$ on $\calR_\calC$, and called the \textit{Lyubashenko--Reshetikhin--Turaev functor}, see \cite[Sec.~3.1]{DGGPR19}.

Starting from an L-modular category $\calC$, Lyubashenko's construction can be reformulated as producing a topological invariant $\rmL_\calC$ of closed oriented 3-manifolds decorated with closed bichrome graphs. As explained in Section \ref{SS:renormalized_non-semisimple}, this invariant cannot be extended to a TQFT unless $\calC$ is semisimple, in which case everything boils down to Turaev's theory. However, in the non-semisimple case, one can construct a renormalized invariant $\rmL'_\calC$ of closed oriented 3-manifolds decorated with so-called admissible closed bichrome graphs. We say a bichrome graph is \textit{admissible} if it features at least a projective object $P \in \Proj(\calC)$ among the labels of its blue edges. In particular, just like in the semisimple case, the theory can be understood as producing a family $\{ \rmL'_P \}_{P \in \Proj(\calC)}$ of topological invariants of framed oriented links inside 3-manifolds. However, this time it is crucial not to allow empty links, and to restrict to projective objects for the parametrization.

The first step for the construction of $\rmL'_\calC$ is the definition of a renormalized invariant of admissible closed bichrome graphs. A \textit{cutting presentation} of an admissible closed bichrome graph $T$ is a bichrome graph $T_P$ satisfying
\[
 \pic{cutting_presentation} = T
\]
for some $P  \in \Proj(\calC)$. Remark that every admissible bichrome graph admits a cutting presentation, which is simply obtained by cutting open one of its blue edges carrying projective label. However, cutting presentations are by no means unique. For instance, we might have several blue edges with projective labels to choose from, and these could all determine inequivalent presentations. Nonetheless, if $T$ is an admissible closed bichrome graph, and if $T_P$ is a cutting presentation of $T$, then 
\[
 F'_\calC(T) := \rmt_P \left( F_\Lambda(T_P) \right)
\]
is a topological invariant of $T$. The proof of this result essentially follows from the defining properties of the trace $\rmt$, which were designed explicitly to obtain these kinds of \textit{renormalized} topological invariants. Now, in order to extend this construction to 3-manifolds, we need again a normalization coefficient, just like in the semisimple theory. This is defined in terms of the so-called \textit{stabilization coefficients}
\[
 \Delta_+ := F_\Lambda \left( \pic{stabilization_coeff_+_red} \right) \in \Bbbk, \qquad
 \Delta_- := F_\Lambda \left( \pic{stabilization_coeff_-_red} \right) \in \Bbbk.
\]
Just like in the fusion case, it is a consequence of L-modularity that the product $\Delta_+ \Delta_-$ is invertible, and so we can choose two parameters $\calD,\delta \in \Bbbk^\times$ satisfying
\[
 \calD^2 = \Delta_+ \Delta_-, \qquad 
 \delta = \frac{\Delta_+}{\calD} = \frac{\calD}{\Delta_-}.
\]
The definition of the topological invariant $\rmL'_\calC$ depends again on the choice of $\calD$, which uniquely determines $\delta$. If $M$ is a closed oriented 3-manifold, if $T \subset M$ is an admissible closed bichrome graph, and if $L \subset S^3$ is a surgery presentation of $M$, which we assume having $\ell$ components and signature $\sigma$, and to which we assign an arbitrary orientation and the color red, then
\[
 \rmL'_\calC(M,T) := \calD^{-1-\ell} \delta^{-\sigma} F'_\Lambda(L \cup T)
\]
is a topological invariant of the pair $(M,T)$.

Just like in Section \ref{S:TQFT_sem-sim}, the universal construction of \cite{BHMV95} extends the invariant $\rmL'_\calC$ to a dual pair of TQFTs given by a covariant functor $\rmV_\calC$ and a contravariant one $\rmV'_\calC$.  Again, this means that, for every closed oriented surface $\Sigma$, we obtain dual vector spaces $\rmV_\calC(\Sigma)$ and $\rmV'_\calC(\Sigma)$ supporting respectively left and right actions of decorated cobordisms. This time, if $\bar{\Sigma}$ is obtained from $\Sigma$ by reversing its orientation, the isomorphism $\rmV'_\calC(\Sigma) \cong \rmV_\calC(\bar{\Sigma})$ is no longer natural, as a consequence of the admissibility condition. Indeed, if $\Sigma_g$ is a closed oriented surface of genus $g$, then the contravariant state space $\rmV'_\calC(\Sigma_g)$ can be naturally identified with
\begin{equation}\label{E:st_sp_non-sem-sim_prime}
 \rmV_\calC'(\Sigma_g) \cong \calC(\calL^{\otimes g},\one).
\end{equation}
On the other hand, the covariant state space $\rmV_\calC(\Sigma_g)$, which is isomorphic to the linear dual of $\rmV'_\calC(\Sigma_g)$, can be naturally identified with 
\begin{equation}\label{E:st_sp_non-sem-sim}
 \rmV_\calC(\Sigma_g) \cong \calC(P_{\one},\calE^{\otimes g}) / \rad_R \langle \_,\_ \rangle_g,
\end{equation}
where $P_{\one}$ is the projective cover of the tensor unit $\one$, and where the bilinear pairing $\langle \_,\_ \rangle_g : \calC(\calL^{\otimes g},\one) \times \calC(P_{\one},\calE^{\otimes g}) \to \Bbbk$ is determined by 
\[
 \langle f',f \rangle_g = \rmt_{P_{\one}} \left( \eta_{\one} \circ f' \circ (D^{-1})^{\otimes g} \circ f \right)
\]
for the Drinfeld map $D : \calL \to \calE$ and the injective envelope\footnote{Projective covers coincide with injective envelopes in modular categories.} monomorphism $\eta_{\one} : \one \to P_{\one}$. When $\calC$ is semisimple, then $P_{\one} = \one$, $\eta_{\one} = \id_{\one}$, and $\langle \_,\_ \rangle_g$ is non-degenerate, so that we recover the description of \eqref{E:st_sp_sem-sim}.


\section{L-modular categories from small quantum \texorpdfstring{$\mathfrak{sl}_2$}{sl(2)}}\label{S:sl_2_non-sem-sim}

The small quantum group $\bar{U}_q \fsl_2$ introduced in Section \ref{S:sl_2_sem-sim} is factorizable. This is proved in \cite[Ex.~3.4.3]{M95} by looking directly at the M-matrix $M \in \bar{U}_q \fsl_2 \otimes \bar{U}_q \fsl_2$, which is given by
\[
 M := \frac{1}{r} \sum_{a,b,c,d=0}^{r-1} \frac{\{ 1 \}^{a+b}}{[a]![b]!} q^{\frac{a(a-1)+b(b-1)}{2} - 2 cd - (b+c)(b-d)} F^b K^c E^a \otimes E^b K^d F^a.
\]
This means the category $\calC = \mods{\bar{U}_q \fsl_2}$ of finite-dimensional left $\bar{U}_q \fsl_2$-modules is L-modular, see \cite[Rem.~3.6.1]{L95}.

An \textit{integral} $\Lambda : \C \to \coad$ is determined by the linear form $\lambda = \Lambda(1) \in (\bar{U}_q \fsl_2)^*$ defined as
\[
 \lambda \left( E^a F^b K^c \right) := \frac{r^3}{\{ 1 \}^{2r-2}} \delta_{a,r-1} \delta_{b,r-1} \delta_{c,1},
\]
see \cite[Prop.~A.5.1]{L94}. Remark that Lyubashenko uses Lusztig's coproduct, which explains why the formula written here defines a right integral, instead of a left one. A direct computation gives the \textit{stabilization parameters}
\begin{align*}
 \Delta_- &= \lambda(v) = i^{\frac{r-1}{2}} r^{\frac 32} q^{\frac{r+3}{2}}, &
 \Delta_+ &= \lambda(v^{-1}) = i^{-\frac{r-1}{2}} r^{\frac 32} q^{\frac{r-3}{2}},
\end{align*}
and we fix the square root
\[
 \calD = r^{\frac 32}
\]
of the product $\Delta_+ \Delta_-$, which uniquely determines the coefficient
\[
 \delta = i^{-\frac{r-1}{2}} q^{\frac{r-3}{2}},
\]
as well as the corresponding normalization of $\rmL'_\calC$. 

In order to illustrate the difference between the L-modular category $\calC$ and its T-modular subquotient $\bar{\calC}$ defined in Section \ref{S:sl_2_sem-sim}, let us describe projective covers of simple objects of $\calC$. For every integer $0 \leqs n \leqs r-2$ we denote with $P_n$ the $\bar{U}_q \fsl_2$-module with basis 
\[
 \{ a_i^n, x_j^n, y_j^n, b_i^n \in P_n \mid 0 \leqs i \leqs n, 0 \leqs j \leqs r-n-2 \}
\] 
and action given, for all integers $0 \leqs i \leqs n$ and $0 \leqs j \leqs r-n-2$, by
\begin{equation*}
 \begin{split}
  K \cdot a_i^n &= q^{n-2i} a_i^n, \\
  E \cdot a_i^n &= [i][n-i+1] a_{i-1}^n, \\
  F \cdot a_i^n &= a_{i+1}^n, \\
  K \cdot x_j^n &= q^{-n-2j-2} x_j^n, \\
  E \cdot x_j^n &= -[j][n+j+1] x_{j-1}^n, \\ 
  F \cdot x_j^n &= 
  \begin{cases}
   x_{j+1}^n & 0 \leqs j < r-n-2, \\
   a_0^n & j = r-n-2,
  \end{cases} \\
  K \cdot y_j^n &= q^{-n-2j-2} y_j^n, \\
  E \cdot y_j^n &= 
  \begin{cases}
   a_n^n & j = 0, \\
   -[j][n+j+1] y_{j-1}^n & 0 < j \leqs r-n-2,
  \end{cases} \\
  F \cdot y_j^n &= y_{j+1}^n, \\
  K \cdot b_i^n &= q^{n-2i} b_i^n, \\
  E \cdot b_i^n &= 
  \begin{cases}
   x_{r-n-2}^n & i = 0, \\
   a_{i-1}^n + [i][n-i+1] b_{i-1}^n & 0 < i \leqs n, 
  \end{cases} \\
  F \cdot b_i^n &= 
  \begin{cases}
   b_{i+1}^n & 0 \leqs i < n, \\
   y_0^n & i = n,
  \end{cases}
 \end{split}
\end{equation*}
where $a_{-1}^n := a_{n+1}^n := x_{-1}^n := y_{r-n-1}^n := 0$. These modules are all projective, indecomposable, and self-dual, and every indecomposable projective object of $\calC$ is isomorphic to either $P_{r-1} = V_{r-1}$ or $P_n$ for some $0 \leqs n \leqs r-2$. Their categorical dimension is
\[
 \dim_\calC(P_n) = \tr_\calC(\id_{P_n}) = 0.
\]
However, the normalization $\rmt_{V_{r-1}}(\id_{V_{r-1}}) = 1$ uniquely determines a trace $\rmt$ on $\Proj(\calC)$ which satisfies
\[
 \rmt_{P_n}(\id_{P_n}) = \{ n+1 \}',
\]
as follows from a computation that can be adapted from \cite[Lem.~6.9]{CGP14} (remark the difference between the pivotal element $g = K$ and the one used by Costantino, Geer, and Patureau for their right duality morphisms, which accounts for the sign appearing in their formula).

Thanks to equations \eqref{E:st_sp_non-sem-sim_prime} and \eqref{E:st_sp_non-sem-sim}, state spaces of closed oriented surfaces for the TQFTs $\rmV_{\calC}$ and $\rmV'_{\calC}$ extending $\rmL'_{\calC}$ can be written in terms of morphism spaces in $\calC$ involving tensor powers of the end $\calE \cong \ad$ and of the coend $\calL \cong \coad$. We point out that, although $\ad$ and $\coad$ can be described very explicitly, their description is rather complicated. For instance, they are not projective objects of $\calC$, as follows from an explicit decomposition into indecomposable summands computed by Ostrik \cite{Os95}. If $\Sigma_g$ is a closed oriented surface of genus $g$, then equation \eqref{E:st_sp_non-sem-sim_prime} identifies $\rmV'_{\calC}(\Sigma_g)$ with $ \calC(\coad^{\otimes g},\one)$. On the other hand, equation \eqref{E:st_sp_non-sem-sim} describes the dual vector space $\rmV_{\calC}(\Sigma_g)$ as a quotient of $\calC(P_0,\ad^{\otimes g})$. In the example of the torus $\Sigma_1 = S^1 \times S^1$, since $\calC(\coad,\one)$ can be naturally identified with the center $Z(\bar{U}_q \fsl_2)$ of $\bar{U}_q \fsl_2$, then
\[
 \rmV'_{\calC}(\Sigma_1) \cong Z(\bar{U}_q \fsl_2).
\]
On the other hand, the quotient of $\calC(P_0,\ad^{\otimes g})$ can be naturally identified with the Hochschild homology $\HH_0(\bar{U}_q \fsl_2) = \bar{U}_q \fsl_2/[\bar{U}_q \fsl_2,\bar{U}_q \fsl_2]$ of $\bar{U}_q \fsl_2$, so that
\[
 \rmV_{\calC}(\Sigma_1) \cong \HH_0(\bar{U}_q \fsl_2).
\]
The dimension of both spaces is
\[
 \dim_\C \rmV_\calC(\Sigma_1) = \dim_\C Z(\bar{U}_q \fsl_2) = \frac{3r-1}{2},
\]
as computed by Kerler in \cite[Lem.~14]{K94}. In the same paper, Kerler independently redefines and computes Lyubashenko's projective representation of the genus one mapping class group $\MCG(\Sigma_1)$ in $\PGL_\C(Z(\bar{U}_q \fsl_2))$, see \cite[Thm.~2]{K94}. He conjectures an explicit decomposition of this representation, and he verifies his conjecture for $r=3$ and $r=5$ in \cite[Sec.~3.6]{K94}. Remark that in both cases the resulting representation of $\MCG(\Sigma_1)$ is faithful modulo the center $Z(\MCG(\Sigma_1)) \cong \Z/2\Z$. Up to isomorphism, Kerler--Lyubashenko's representations are precisely those induced by the contravairant TQFT $\rmV'_\calC$ for $\calC = \mods{\bar{U}_q \fsl_2}$, see \cite[Thm.~1.2]{DGGPR20}.
