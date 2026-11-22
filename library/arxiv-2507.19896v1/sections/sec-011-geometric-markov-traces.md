---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-011-geometric-markov-traces
section_title: "Geometric Markov traces."
section_number: null
pages: 9-12
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.532
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
\label{sec:geom-mark-trac}
Markov traces $\tr_n^B:\He_{v,v}(B_n) \to \mathcal{A}(a), \tr_n^D:\He(D_n) \to \mathcal{A}(a)$ studied in \cite{gomi2006markov}, \cite{websterGeometryMarkovTraces2009} are specializations of traces $\tr_{n,y}^X$ satisfying the extension of the properties \ref{item:5}, \ref{item:6} for the embeddings $B_0 \to B_1$ and $D_1 \to D_2, D_0 \to D_1$. In particular, these traces satisfy
\[
  \tr_1^B(t_0) = v-v^{-1}, \tr_1^D(t_1) = \tr_1^D(t_{1'}) = v-v^{-1}, \tr^D_2(t_1t_{1'}) = (v-v^{-1})^2.
\]
The condition on $\tr_1^B$ forces $y = v - v^{-1}$ and $\overline{y}-\alpha_0 = 0$. Thus we get that $\tr_n^B = \tr_{\zeta_n}$, the trace from Theorem \ref{sec:markov-traces-via}.

The conditions on $\tr_1^D, \tr_2^D$ imply that
\[
  y^2 = \tr_2^D(U_1U_2) = \tr_2^D(t_1t_{1'}^{-1}) = \tr_2^D(t_1t_{1'}) - \alpha \tr_2^D(t_1) = \alpha^2 - \alpha^2(1+a) = -\alpha^2a.
\]

It is easy to see that geometric Markov traces $\tr_n^B, \tr_n^D$ take values in $\mathcal{A}[a]$. Let $\tr_n^{X,k}:\He(X_n) \to \mathcal{A}$ be the coefficient of $\tr_n^X$ at $a^k$. We summarize the above discussion in the following
\begin{theorem}
  \label{sec:geom-mark-trac-1}
  The functional $\tr_n^{B,k}$ is represented by the $k$th elementary symmetric polynomial in Jucys-Murphy elements:
  \[
    \tr_n^{B,k}(h) = \langle e_k(J_1^B, \dots, J_n^B), h\rangle.
  \]

  Let $e_k'(x_1, \dots, x_n;\alpha)$ be the symmetric polynomial in $(x_i)$ appearing as a degree $2k$ homogeneous part in
  \[
    \prod_{i=1}^n(1 + \alpha x_i - x_i^2) = \prod_{i=1}^n(v-x_i)(v^{-1}+x_i).
  \]
  where $\alpha = v - v^{-1}$.
  Then
   \[
    \tr_n^{D,k}(h) = (-1)^k\langle e'_k(j_1^D, \dots, j_n^D; \alpha),h \rangle.
  \]
\end{theorem}
The symmetric polynomial $e_k'$ can be written explicitly as
\[
  e_k' = \sum_{\substack{i+j = 2k,\\ i,j\geq 0}}(-1)^{i}v^{j-i}e_ie_j.
\]
Note that the highest $a$-coefficient is always represented by the ``full twist'' element $\Se^{-1} = e_n(J_1^X, \dots, J_n^X), \tr_n^{X,n} = \tr_{\Se^{-1}}.$ This  recovers the symmetry of the HOMFLY-PT polynomial observed by K\'{a}lm\'{a}n \cite{kalmanMeridianTwistingClosed2009}, that was categorified in \cite{gorskySerreDualityKhovanov2019} in type $A$ and in \cite{bezrukavnikovMonodromicModelKhovanov2022} in general type.
\begin{remark}
  The statement analogous to Theorem \ref{sec:geom-mark-trac-1} was lifted to the level of Khavanov-Rozansky homology in \cite{bezrukavnikovMonodromicModelKhovanov2022}. Namely, there it is shown that the object representing the $k$th degree of the invariant has a filtration by the objects representing products of Jucys-Murphy elements. For an arbitrary Weyl group, the object representing the $k$th degree was constructed in \cite{bezrukavnikovMonodromicModelKhovanov2022} in terms of some explicit character sheaves on a reductive group $G$ with the Weyl group $W$. It was also explained how these character sheaves correspond to exterior powers of the reflection representation of $W$. We expect that, if the analogous filtration categorifying expressions in Theorem \ref{sec:geom-mark-trac-1} can be constructed in types $B$ and $D$, the arguments in this paper can be lifted to the level of Khovanov-Rozansky homology: the pairing $\langle, \rangle$ is categorified to the $\mathrm{Hom}$-pairing on the Hecke category; the ``Serre property'' of Proposition \ref{sec:full-twist-jucys-1} has a categorical analogue in the description of the Serre functor of the Hecke category \cite{beilinsonTiltingExercises2004}, \cite{gorskySerreDualityKhovanov2019}; elements $j_n^X$ can be expressed using the braid group action on the Hecke category. Such an extension would, for example, give a geometric interpretation to the special properties of Markov traces in types $B_n$ and $D_n$ involving the elements $T_n, U_n$. We hope to address this in a future work.

  We would also like to  remark that, in type $A$, the fact that Jucys-Murphy elements and their symmetric polynomials come from the extended affine Hecke algebra has an interpretation in terms of geometric representation theory, see \cite{gnr}, \cite{oblomkovAFFINEBRAIDGROUP2019} and \cite{tolmachovkostiantynLinearStructureFinite}. We do not know if this interpretation can be extended to other types. 
\end{remark}
