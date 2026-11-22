---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-014-33-compactly-supported-cohomology
section_title: "Compactly supported cohomology"
section_number: 3.3
pages: 38-40
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.961
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
Let $\cE$ be a spectrum object of $\Psh_\ast(\cB)$, a model for which is as a functor $\cB^{\op} \to \spectra$.  
Now, Corollary~1.4.4.5 of~\cite{HA} grants that a finite limit preserving functor from a stable $\infty$-category to $\spaces$ canonically factors through $\spectra \xra{\Omega^\infty} \spaces$.  
In particular, for $\cS$ a stable $\infty$-category, the Yoneda functor $\cS^{\op}\times \cS \to \spaces$ canonically factors through $\spectra \xra{\Omega^\infty}\spaces$. 
In particular, there is a factorization of the Yoneda functor
\[
\Map_{\Psh_\ast(\cB)}(-,\Omega^\infty\cE)\colon \Psh_\ast(\cB)^{\op} \xra{\cE^-} \spectra \xra{\Omega^\infty} \spaces_\ast~,
\]
the first of which is symmetric monoidal with respect to coproduct on the source and on the target, and the second of which is symmetric monoidal with respect to coproduct on the source and product on the target.  
We will denote the composite symmetric monoidal functor
\begin{equation}\label{E-c}
\cE_{\sf c}\colon \mfld(\cB)^{\sf fin} \xra{\tau^+}\Psh^{\sf fin}_\ast(\cB)^{\op}\xra{\cE^-} \spectra
\end{equation}
where here the target is equipped with the symmetric monoidal structure given by wedge sum.
We will use the notation
\[
A_\cE ~:=~ (\cE_{\sf c})_{|\disk(\cB)} \in \Alg_{\disk(\cB)}(\spectra)
\]
for the restriction.  
We give notation for the relative version:
\[
\cE_{X^+}\colon \mfld(\cB)_{/X^+} \xra{\tau^{X^+}}\Psh_\ast(\cB)\xra{\cE^-} \spectra~.  
\]

\begin{prop}[Compactly supported cohomology]\label{sections-excision}
Let $\cE$ be a spectrum object of $\Psh_\ast(\cB)$.  
Then the symmetric monoidal functor $\cE_{\sf c}\colon \mfld(\cB) \to \spectra$ satisfies $\ot$-excision.
In particular, the canonical map
\[
\int_- A_\cE\xra{~\simeq~} \cE_{\sf c}(-)
\]
is an equivalence of symmetric monoidal functors $\mfld(\cB)^{\sf fin}\to \spectra$.  

\end{prop}

\begin{proof}
Let $X\cong X_-\underset{\RR\times X_0}\bigcup X_+$ be a collar-gluing among $\cB$-manifolds.  
After Lemma~\ref{pre-excision}, there is the pullback diagram among spectra
\[
\xymatrix{
\cE_{\sf c}(X^+)  \ar[r]  \ar[d]
&
\cE_{X^+}(X_+)  \ar[d]
\\
\cE_{X^+}(X_-)  \ar[r]
&
\cE_{X^+}(\RR\times X_0)~.
}
\]
Thereafter, using the canonical identification $\Omega \cE_{X^+}(\RR\times X_0) \simeq \cE_{\sf c}(\RR\times X_0)$ and Lemma~\ref{pre-excision} again, there is the pushout diagram of spectra
\[
\xymatrix{
\cE_{\sf c}(X_0) \ar[r]  \ar[d]
&
\cE_{\sf c}(X_+)  \ar[d]
\\
\cE_{\sf c}(X_-)\ar[r]
&
\cE_{\sf c}(X^+)~.
}
\]

Because we are equipping spectra with wedge sum, which is its categorical coproduct, the forgetful functor $\Alg_{\Ass^{\sf RL}}(\spectra) \xra{\simeq} \Fun\bigl((-\la 0 \to +), \spectra\bigr)$ is an equivalence; and, for $(P\la A \to Q)$ an object of this functor category, regarded as an $\Ass^{\sf RL}$-algebra in $\spectra$, then the canonical map from the pushout $P\underset{A} \coprod Q \xra{\simeq} P\underset{A}\bigotimes Q$ is an equivalence of spectra.  
And so, we have verified that $\cE_{\sf c}$ satisfies $\ot$-excision.  

\end{proof}

Specializing Proposition~\ref{sections-excision} to the case that $\cE = \SS \colon \cB^{\op} \to \spectra$ is the constant functor at the sphere spectrum, we have the following classical consequence.
For this case, we will use the special notation 
\[
\DD\bigl((-)^+\bigr)~:=~\SS_{\sf c}(-) ~,\qquad \text{ and }\qquad \omega ~:=~ A_{\SS}~.
\]
This notation is invoked because, for each $\cB$-manifold $X$, the spectrum $\DD(X^+)$ is the Spanier-Whitehead dual of the 1-point compactification of the underlying space of $X$; and the value of $\omega$ on a basic $U$ is $\DD(U^+)$, the stalk of the dualizing sheaf for the site $\mfldd(\cB)$ at $U$.  

Immediate from the present definitions is the following result. 
\begin{prop}
Let $\cB = \BO(n)$, so that a $\cB$-manifold is an ordinary smooth $n$-manifold.  
Let $X$ be smooth $n$-manifold that is the interior of a compact manifold with boundary.
Then there is a canonical identification 
\[
X^{-\tau_X} \simeq \int_X\omega
\] 
from the Thom spectrum of the virtual negative of the tangent bundle of $X$.  

\end{prop}

  
\begin{cor}[Atiyah duality]\label{atiyah}
Let $X$ be a finitary $\cB$-manifold.
Then there is a canonical identification
\[
\int_X \omega  ~\simeq~ \DD(X^+)~.
\]
More generally, for each functor $\cE\colon \cB^{\op} \to \spectra$, there is a canonical identification
\[
\int_X \cE\wedge \omega~\simeq~ \cE_{\sf c}(X)~.
\]

\end{cor}

\begin{example}[Classical Poincar\'e duality]
Let us consider the case $\cB = \sD_n^{\sf or}$ so that a $\cB$-manifold is an oriented smooth $n$-manifold; and an oriented $n$-manifold $X$ that is the interior of a compact manifold with boundary; and $\cE = \sH\ZZ\colon (\sD_n^{\sf or})^{\op} \to \spectra$ is the constant functor at the Eilenberg-MacLane spectrum for $\ZZ$.
Identify $\sH\ZZ_{\sf c}(X)\simeq \sH\ZZ^{X^+}$ as the mapping spectrum from the 1-point compactification.  
For each object $U\in \sD_n^{\sf or}$ there is a canonical identification $\sH\ZZ\wedge \omega(U)\simeq \sH\ZZ\wedge \SS^{-n}\simeq \Omega^n \sH\ZZ$.    
And so, there is a canonical equivalence of spectra $\int_X \sH\ZZ\wedge \omega~\simeq \Omega^n\sH\ZZ\wedge X_+$.
Putting these identification into Corollary~\ref{atiyah} arrives at a canonical equivalence of spectra:
$
\Omega^n \sH\ZZ\wedge X_+~\simeq~ \sH\ZZ^{X^+}.  
$
Upon taking homotopy groups, indexed appropriately, we arrive at classical Poincar\'e duality: 
\[
\sH_\ast(X;\ZZ)\cong \sH^{n-\ast}_{\sf c}(X;\ZZ)~.
\]

\end{example}
