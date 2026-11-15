---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-020-51-dimensions-and-traces-of-sheaf-categories-1-c
section_title: "Dimensions and traces of sheaf categories: 1-categorical consequences"
section_number: 5.1
pages: 30-31
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.941
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
The graph of a map of derived stacks $f:X\to Y$ provides a correspondence from $X$ to $Y$ and a correspondence from $Y$ to $X$. We denote the respective induced maps by $f_{*}:\cS(X)\to \cS(Y)$ and $f^!:\cS(Y)\to \cS(X)$. The functoriality of $\cS$ concisely encodes base change for $f_{*}$ and $f^!$. For $\pi:X\to pt = \Spec k$, we denote by $\omega_{X}=\pi^! k\in \cS(X)$ the $\cS$-analogue of the dualizing sheaf, and by $\omega(X)=\pi_{*}\omega_{X} \in \cS(pt) = dgVect_k$ the $\cS$-analogue of "global volume forms\".

Next we will record formal consequences of our prior calculations deduced from the fact that a sheaf theory is symmetric monoidal.

::: prop
[]{#basic integral transforms label="basic integral transforms"} Fix a sheaf theory $\cS:Corr_k\to dgCat_k$, and $X, Y\in Corr_k$.

\(1\) $\cS(X) \in dgCat_k$ is canonically self-dual, and for any $f:X\to Y$, $f^!:\cS(Y) \to \cS(X)$ and $f_{*}:\cS(X)\to \cS(Y)$ are canonically transposes of each other.

\(2\) $\cS(X)$ is canonically symmetric monoidal with tensor product $$\xymatrix{
\cF\ot^!\cG=\Delta^!(\pi_1^! \cF\ot \pi_2^! \cG) & \cF, \cG\in \cS(X)
}$$

\(3\) For any $f:X\to Y$, the projection formula holds: $$\xymatrix{
f_*\cF\ot^! \cG \simeq f_*(\cF\ot^! f^!\cG) & \cF\in \cS(X), \cG\in \cS(Y)
}$$

\(4\) There is a canonical equivalence of functors and integral kernels $$\Hom_{dgCat_k}(\cS(X),\cS(Y))\simeq \cS(X\times Y)$$

\(5\) The functor $q_*p^!:\cS(X) \to \cS(Y)$ associated to a correspondence $$\xymatrix{X&\ar[l]_-{p} Z \ar[r]^-{q} &Y}$$ is represented by the integral kernel $(p\times q)_*\omega_Z \in \cS(X\times Y)$.
:::

::: proof
*Proof.* (1) Follows immediately from Proposition [\[basic stack dimensions\]](#basic stack dimensions){reference-type="ref" reference="basic stack dimensions"}.

\(2\) Follows immediately from the commutative algebra structure on $X\in Corr_k$ (in fact commutative coalgebra structure on $X\in Stacks_k$) provided by the diagonal map.

\(3\) Follows from base change for the diagram $$\xymatrix{
X\ar[d]_-{id\times f} \ar[r]^-{f} & Y\ar[d]^-{\Delta}\\
X\times Y\ar[r]^-{f\times \id} & Y\times Y
}$$

\(4\) Since $\cS$ is monoidal, we have $$\cS(X)\ot \cS(Y)\simeq \cS(X \times Y)$$ The self-duality of $\cS(X)$ provides $$\Hom_{dgCat_k}(\cS(X),\cS(Y))\simeq \cS(X)^\vee\ot \cS(Y) \simeq \cS(X)\ot \cS(Y)$$ By construction, the composite identification assigns the functor $$\xymatrix{
F_K(\cF)=\pi_{2_*}(\pi_1^!\cF\ot^! K)
&
K\in \cS(X\times Y)
}$$

\(5\) Follows from the projection formula: consider the diagram $$\xymatrix{
& Z \ar[dl]_-{p} \ar[dr]^-{q} \ar[d]_-{\Pi}& \\
X & \ar[l]_-{\pi_1} X\times Y \ar[r]^-{\pi_2} & Y
}$$ where $\Pi=p\times q$. Then we have $$\xymatrix{
q_*p^!(-)\simeq \pi_{2*} \Pi_* \Pi^! \pi_1^!(-) \simeq
\pi_{2*} \Pi_* (\omega_Z \otimes^! \Pi^! \pi_1^!(-)) \simeq
\pi_{2*} (\Pi_* \omega_Z \otimes^! \pi_1^!(-))
}$$ ◻
:::

::: prop
[]{#trace of integral transform label="trace of integral transform"} Fix a sheaf theory $\cS:Corr_k\to dgCat_k$.

\(1\) The $\cS$-dimension $\dim(\cS(X)) =HH_*(\cS(X))$ of any $X\in Corr_k$ is $S^1$-equivariantly equivalent with $\cS$-global volume forms on the loop space $$\dim(\cS(X))\simeq \omega(\cL X).$$

In particular, for $G$ an affine algebraic group, characters of $\cS$-valued $G$-representations are adjoint-equivariant $\cS$-global volume forms $$\dim(\cS(BG))\simeq \omega(G/G)$$

\(2\) The $\cS$-trace of any endomorphism $Z\in Corr_k(X,X)$ is equivalent to $\cS$-global volume forms on the restriction to the diagonal $$\Tr(\cS(Z)) \simeq \omega(Z|_{\Delta})$$

In particular, the $\cS$-trace of a self-map $f:X\to X$ is equivalent to $\cS$-global volume forms on the $f$-fixed point locus $$\Tr(f_{*})\simeq \omega(X^f)$$
:::

::: proof
*Proof.* (1) Follows immediately from Proposition [\[basic stack dimensions\]](#basic stack dimensions){reference-type="ref" reference="basic stack dimensions"}(1). To spell this out, using the previous proposition and base change, $\dim (\cS(X))$ results from applying the composition $$\xymatrix{
\pi_*\Delta^!\Delta_*\pi^! \simeq \pi_*p_{2*}p_1^!\pi^! \simeq \cL \pi_* \cL \pi^!:dgVect_k \ar[r] & dgVect_k
}$$ to the unit $1_{dgVect_k} = k$. Here $\pi:X\to pt$ and $\cL \pi:\cL x\to pt$ are the maps to the point, and $p_1, p_2:\cL X \simeq X\times_{X\times X} X\to X$ are the two natural projections. Thus we find $\dim (\cS(X)) \simeq \cL \pi_* \cL \pi^!(k) \simeq \omega(\cL X)$. Furthermore, the $S^1$-equivariance results from the one-dimensional cobordism hypothesis: the one-dimensional topological field theory defined by the dualizable object $\cS(X)\in dgCat_k$ factors through that defined by the dualizable object $X\in Corr_k$. Moreover, we identified the $S^1$-action on the dimension $\cL X$ with loop rotation.[^1]

\(2\) Similarly follows immediately from Proposition [\[basic stack dimensions\]](#basic stack dimensions){reference-type="ref" reference="basic stack dimensions"}(2). ◻
:::

[^1]: One can also check directly that the cyclic structure on the cyclic bar construction of the dg category $\cS(X)$ is induced by the cyclic structure of the loop space $\cL X$ under the identification $\omega(\cL X)\simeq \dim(\cS(X))$.
