---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-009-5-analytic-r-groups-for-non-tempered-representat
section_title: "Analytic R-groups for non-tempered representations"
section_number: 5
pages: 20-21
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.944
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
In this section we extend the definitions and results from Section \ref{sec:RgroupTemp}
(which stem from \cite{DeOp2}) to non-tempered induction data $\xi \in \Xi \setminus \Xi_{un}$.
One approach would be to define the R-group of $\xi = (P,\delta,t)$ to be that of
$\xi_{un} = (P,\delta ,t \,|t|^{-1})$. This works out well in most cases, but it is unsatisfactory
if the isotropy group $\mc W_{\xi_{un}}$ is strictly larger than $\mc W_\xi$.

The problem is that $t \, |t|^{-1}$ is not always a generic point of $(T^P)^{\mc W_\xi}$.
To overcome this, we define $\mc M_\xi$ to be the collection of mirrors $M \in \mc M^{P,\delta}$
that contain not only $t \, |t|^{-1}$, but the entire connected component of $t |t|^{-1}$ in
$(T^P_{un})^{\mc W_\xi}$. Notice that all components of $(T^P)^{\mc W_\xi}$ are cosets of a
complex subtorus of $T^P$. Since $t \, |t|^r \in (T^P)^{\mc W_\xi}$ for all $r \in \R ,\; \mc M_\xi$
is precisely the collection of mirrors whose complexification contains $t$.

Now we define $R_{\xi} ,R^+_{\xi}$ and $\mf R_\xi$ as in \eqref{eq:24} and \eqref{eq:3}.
We note that $\mf R_\xi$ may differ from $\mf R_{\xi_{un}}$, but that $R_\xi = R_{P,\delta,t'}$
for almost all $t' \in (T^P_{un})^{\mc W_\xi}$. For positive induction data there is an analogue
of Theorem \ref{thm:KnappStein}:

\begin{thm} \label{thm:KnappSteinNontemp}
Let $\xi = (P,\delta,t) \in \Xi^+$.
\enuma{
\item For $w \in \mc W_\xi$ the intertwiner $\pi (w,\xi)$ is scalar if and only if $w \in W(R_{\xi})$.
\item There exists a 2-cocycle $\kappa_\xi$ of $\mf R_\xi$ such that
$\mr{End}_{\mc H} (\pi (\xi))$ is isomorphic to the twisted group algebra $\C [\mf R_\xi ,\kappa_\xi]$.
\item There exists a unique bijection
\[
\mr{Irr}(\C [\mf R_\xi ,\kappa_\xi]) \to \mr{Irr}_{\mc W \xi} ( \mc H ) :
\rho \mapsto \pi_\rho ,
\]
and there exist indecomposable direct summands $\widetilde{\pi_\rho}$ of $\pi (\xi)$,
such that $\pi_\rho$ is a quotient of $\widetilde{\pi_\rho}$ and
$\pi (\xi) \cong \bigoplus_\rho \widetilde{\pi_\rho} \otimes \rho$ as
$\mc H \otimes \C [\mf R_\xi ,\kappa_\xi]$-modules.
}
\end{thm}
\begin{rem} Part (a) also holds for general $\xi \in \Xi$. Part (d) of Theorem
\ref{thm:KnappStein} does not admit a nice generalization to $\xi \in \Xi^+$.
One problem is that the category $\mr{Mod}_f (\C [\mf R_\xi ,\kappa_\xi])$ is semisimple,
while $\pi (\xi)$ is not always completely reducible. One can try to consider the category of
$\mc H$-representations all whose irreducible subquotients lie in $\mr{Irr}_\xi (\mc H)$,
but then one does not get a nice formula for the functor $E_\xi$.
\end{rem}
\emph{Proof.}
(a) and (b) Since $\xi$ is positive, the operators $\pi (w,\xi)$ with $w \in \mc W_\xi$ span
$\mr{End}_{\mc H} (\pi (\xi))$ \cite[Theorem 3.3.1]{Sol-Irr}.
Let $v \in W(R_{\xi})$. The intertwiner $\pi (v,P,\delta ,t')$ is rational in $t'$ and
by Theorem \ref{thm:KnappStein}.a it is scalar for all $t'$ in a Zariski-dense subset of
$(T^P_{un})^{\mc W_\xi}$. Hence $\pi (v,P,\delta ,t')$ is scalar for all
$t' \in (T^P)^{\mc W_\xi}$, which together with \eqref{eq:3} and \eqref{eq:multIntOp} implies that
\[
\mr{End}_{\mc H} (\pi (\xi)) = \mr{span} \{ \pi (w,\xi) : w \in \mf R_\xi \} .
\]
All the intertwiners $\pi (w,P,\delta,t')$ depend continuously on $t'$, so the type of
$\pi (P,\delta,t')$ as a projective $\mf R_\xi$-representation is constant on connected
components of $(T^P)^{\mc W_\xi}$. Again by Theorem \ref{thm:KnappStein}.a
$\{ \pi (w,\xi) : w \in \mf R_\xi \}$ is linearly independent for generic
$t' \in (T^P_{un})^{\mc W_\xi}$, so it is in fact linearly independent for all $t' \in (T^P)^{\mc W_\xi}$.
Now the multiplication rules for intertwining operators \eqref{eq:multIntOp} show that
$\mr{End}_{\mc H} (\pi (\xi))$ is isomorphic to a twisted group algebra of $\mf R_\xi$.

(c) Let $A = \mr{End}_{\C [\mf R_\xi,\kappa_\xi]}$ be the bicommutant of $\pi (\xi, \mc H)$ in
$\mr{End}_\C (\mc H)$. There is a canonical bijection
\[
\mr{Irr}(\C [\mf R_\xi ,\kappa_\xi]) \to \mr{Irr} (A) : \rho \mapsto \widetilde{\pi_\rho}
\]
such that $\pi (\xi) \cong \bigoplus_\rho \widetilde{\pi_\rho} \otimes \rho$ as
$A \otimes \C [\mf R_\xi ,\kappa_\xi]$-modules. By construction the irreducible $A$-subrepresentations
of $\pi (\xi)$ are precisely the indecomposable $\mc H$-subrepresentations of $\pi (\xi)$.
By \cite[Proposition 3.1.4]{Sol-Irr} every $\widetilde{\pi_\rho}$ has a unique irreducible quotient
$\mc H$-representation, say $\pi_\rho$, and $\pi_\rho \cong \pi_{\rho'}$ if and only if
$\widetilde{\pi_\rho} \cong \widetilde{\pi_{\rho'}}$ as $\mc H$-representations. Thus
$\rho \mapsto \pi_\rho$ sets up a bijection between Irr$(\C [\mf R_\xi ,\kappa_\xi])$ and the
equivalence classes of irreducible quotients of $\pi (\xi)$. By Theorem \ref{thm:parametrizationOfDual}
the latter collection is none other than $\mr{Irr}_{\mc W \xi} (\mc H). \qquad \Box$
\vspace{4mm}
