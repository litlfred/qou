---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-011-8-l-modular-categories-from-small-quantum-sl2
section_title: "L-modular categories from small quantum sl(2)"
section_number: 8
pages: 18-20
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.922
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogy that the notion of modular category was an appropriate structure for build"
---
\label{S:sl_2_non-sem-sim}

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
