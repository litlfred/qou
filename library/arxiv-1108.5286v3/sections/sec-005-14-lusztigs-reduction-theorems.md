---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-005-14-lusztigs-reduction-theorems
section_title: "Lusztig's reduction theorems"
section_number: 1.4
pages: 10-12
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.986
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
\label{sec:redthm}

The study of irreducible representations of $\mc H \rtimes \Gamma$  is simplified by 
two reduction theorems, which are essentially due to Lusztig \cite{Lus-Gr}.
The first one reduces to the case of modules whose central character is positive on
the lattice $\Z R_l$. The second one relates these to modules of an associated graded
Hecke algebra. 

Given $t \in T$ and $\alpha \in R$, \cite[Lemma 3.15]{Lus-Gr} tells us that
\begin{equation}\label{eq:sAlphaFixt}
s_\alpha (t) = t \text{ if and only if } \alpha (t) = 
\begin{cases} 1 & \text{if } \alpha^\vee \notin 2 Y \\
\pm 1 & \text{if } \alpha^\vee \in 2 Y .
\end{cases}
\end{equation}
We define $R_t := \{ \alpha \in R \mid s_\alpha (t) = t \}$. The collection of long
roots in $R_{t,nr}$ is $\{ \beta \in R_l \mid \beta (t) = 1\}$. Let $F_t$ be the unique
basis of $R_t$ consisting of roots that are positive with respect to $\Delta$.
We can define a parameter function $q_t$ for the based root datum
\[
\mc R_t := (X,R_t,Y,R_t^\vee,F_t)
\]
via restriction from $R_{nr}^\vee$ to $R_{t,nr}^\vee$. Furthermore we write
\[
P(t) := \Delta \cap \Q R_t .
\]
Then $R_{P(t)}$ is a parabolic root subsystem of $R$ that contains $R_t$ 
as a subsystem of full rank. Let $t = u c \in T_{un} T_{rs}$ be the polar
decomposition of $t \in T$. We note that $R_{uc} \subset R_u$, that 
$W'_{uc} \subset W'_u$ and that the lattice
\[
\Z P(t) = \Z R \cap \Q R_u 
\]
can be strictly larger than $\Z R_t$. We will phrase the first reduction theorem such that 
it depends mainly on the unitary part $u$ of $t$, it will decompose a representation in parts
corresponding to the point of the orbit $W' u$.

For a finite set $U \subset T / W$, let $Z_U (\mc H) \subset Z (\mc H)$ be the ideal of functions 
vanishing at $U$. Let $\widehat{Z (\mc H )_U}$ be the formal completion of $Z (\mc H)$ with
respect to the powers of the ideal $Z_U (\mc H)$ and define
\begin{equation}\label{eq:ZHt}
\widehat{\mc H_U} = \widehat{Z (\mc H )_U} \otimes_{Z (\mc H)} \mc H .
\end{equation}
Similarly, for $t \in T$ let $\widehat{\mc A_t}$ denote the formal completion of $\mc A \cong 
\mc O (T)$ with respect to the powers of the ideal $\{ f \in \mc O (T) \mid f(t) = 0 \}$.
Inside $\widehat{\mc H_U}$ we have the formal completion of $\mc A$ at $U$, which 
by the Chinese remainder theorem is isomorphic to
\begin{equation}
\widehat{\mc A_U} := \widehat{Z (\mc H )_U} \otimes_{\mc A^W} \mc A \cong
\bigoplus_{t \in U} \widehat{\mc A_t} .
\end{equation}
In this notation we can rewrite
\[
\widehat{Z (\mc H )_{W t}} \cong \widehat{\mc A_{W t}}^{W} \cong \widehat{\mc A_t}^{W_t} .
\]
Analogous statements hold for $\mc H \rtimes \Gamma$.
Given a subset $\varpi \subset W' t$ we let $1_\varpi \in \widehat{\mc A_{W' t}}$
be the idempotent corresponding to $\bigoplus_{s \in \varpi} \widehat{\mc A_s}$.

\begin{thm}\label{thm:2.1}
\textup{(First reduction theorem)} \\
There is a natural isomorphism of $\widehat{Z (\mc H \rtimes \Gamma)_{W' uc}}$-algebras
\[
\widehat{\mc H (\mc R^{P(u)}, q^{P(u)})_{W'_{\Z P (u)} uc}} \rtimes W'_{P(u)} \cong 
1_{W'_{\Z P(u)} uc} \big( \widehat{\mc H_{W' uc}} \rtimes \Gamma \big) 1_{W'_{\Z P(u)} uc}
\]
It can be extended (not naturally) to isomorphism of 
$\widehat{Z (\mc H \rtimes \Gamma)_{W' uc}}$-algebras
\[
\widehat{\mc H_{W' uc}} \rtimes \Gamma  \cong  
M_{[W' : W'_{\Z P(u)}]} \Big( 1_{W'_{\Z P(u)} uc} \big( \widehat{\mc H_{W' uc}} \rtimes \Gamma \big)  
1_{W'_{\Z P(u)} uc} \Big) ,
\]
where $M_n (A)$ denotes the algebra of $n \times n$-matrices with coefficients in an algebra~$A$. 
In particular the algebras
\[
\widehat{\mc H (\mc R^{P(u)}, q^{P(u)})_{W'_{\Z P(u)} uc}} \rtimes W'_{P(u)} \quad \text{and} \quad
\widehat{\mc H_{W' uc}} \rtimes \Gamma 
\]
are Morita equivalent.
\end{thm}
\emph{Proof.}
This is a variation on \cite[Theorem 8.6]{Lus-Gr}. Compared to Lusztig we substituted his $R_{uc}$ 
by a larger root system, we replaced the subgroup $Y \otimes \langle v_0 \rangle \subset T$ by
$T_{rs} = Y \otimes \R_{>0}$ and we included the automorphism group~$\Gamma$. These changes are 
justified in the proof of \cite[Theorem 2.1.2]{Sol-Irr}. $\quad \Box$
\\[2mm]

By \eqref{eq:sAlphaFixt} we have $\alpha (u) = 1$ for all $\alpha \in R_l \cap \Q R_u$, so
$\alpha (t) = \alpha (u) \alpha (c) > 0$ for such roots. Hence Theorem \ref{thm:2.1} allows us 
to restrict our attention to $\mc H \rtimes \Gamma$-modules whose central character is positive
on the sublattice $\Z R_l \subseteq X$.

By definition $u$ is fixed by $W'_u \supset W (R_{P(u)})$, so the map
\begin{equation}\label{eq:expMap}
\exp_u : \mf t \to T ,\;  \lambda \mapsto u \exp (\lambda)
\end{equation}
is $W'_u$-equivariant. 

Analogous to \eqref{eq:ZHt}, let $Z_{W \lambda} (\mh H) \subset Z (\mh H)$ be the maximal ideal
of functions vanishing at $W \lambda \in \mf t / W$. Let $\widehat{Z (\mh H )_{W \lambda}}$ 
be the formal completion of $Z (\mh H)$ with respect to $Z_{W \lambda} (\mh H)$ and define 
\begin{equation}
\widehat{\mh H_{W \lambda}} := \widehat{Z (\mh H )_{W' \lambda}} \otimes_{Z (\mh H)} \mh H .
\end{equation}
The corresponding formal completion of $S (\mf t^*) \cong \mc O (\mf t)$ is
\[
\widehat{S (\mf t^*)_{W \lambda}} := \widehat{Z (\mh H )_{W \lambda}} 
\otimes_{S (\mf t^*)^W} S (\mf t^*) \cong \bigoplus_{\mu \in W \lambda} \widehat{S (\mf t^*)_\mu} .
\]
The map \eqref{eq:expMap} induces a $W'_u$-equivariant isomorphism
\[
\widehat{\mc A_{u \exp \lambda}} \to \widehat{S (\mf t^*)_{\lambda}} : f \mapsto f \circ \exp_u ,
\]
which restricts to an isomorphism
\begin{equation}\label{eq:Phiu}
\Phi_{u,W' \lambda} : \widehat{Z (\mc H \rtimes \Gamma)_{W' u \exp (\lambda)}} 
\to \widehat{Z (\mh H \rtimes \Gamma)_{W' \lambda}} .
\end{equation}
We define a parameter function $k_u$ for the degenerate root datum $\tilde{\mc R}_u$ by
\begin{equation}\label{eq:2.3}
2 k_{u,\alpha} = \log q_{\alpha^\vee / 2} + (1 + \alpha (u)) \log q_{\alpha^\vee}
\qquad \alpha \in R_u .
\end{equation}
Let $q^{\Z / 2}$ be the subgroup of $\mh C^\times$ generated by
$\{ q_{\alpha^\vee}^{\pm 1/2} \mid \alpha^\vee \in R_{nr}^\vee \}$. 

\begin{thm}\label{thm:2.2}
\textup{(Second reduction theorem)} \\
Suppose that 1 is the only root of unity in $q^{\Z / 2}$.
Let $u \in T_{un}^{W'}$ and let $\lambda \in \mf t$ be such that
\begin{equation}\label{eq:2.2}
\inp{\alpha}{\lambda}, \inp{\alpha}{\lambda} + k_{u,\alpha} 
\notin \pi i \mh Z \setminus \{0\} \qquad \forall \alpha \in R \,.
\end{equation} 
\enuma{
\item The map \eqref{eq:Phiu} extends to an algebra isomorphism 
\[
\Phi_{u,W' \lambda} : \widehat{\mc H_{W' u \exp (\lambda)}} \rtimes \Gamma \to 
\widehat{\mh H (\tilde{\mc R},k_u)_{W' \lambda}} \rtimes \Gamma.
\]
\item The algebras $\widehat{\mc H_{W' u \exp (\lambda)}} \rtimes \Gamma$ and
$\widehat{\mh H (\tilde{\mc R}^{P(u)}, k^{P(u)})_{W'_{\Z P(u)} \lambda}} \rtimes W'_{P(u)}$
are Morita equivalent.
}
\end{thm}
\emph{Proof.}
For part (a) see \cite[Theorem 9.3]{Lus-Gr}. Our conditions on $q$ replace the 
assumption \cite[9.1]{Lus-Gr}. Part (b) follows from part (a) and Theorem \ref{thm:2.1}. 
$\qquad \Box$ \vspace{2mm}
