---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-016-42-traces-of-correspondences
section_title: "Traces of correspondences"
section_number: 4.2
pages: 25-27
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.944
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
Given a map $Z\to X$, it is convenient to introduce the symmetric presentation of the based loop space $$\cL_Z X
= Z\times_{Z\times X} Z$$ Note the two natural identification with the traditional based loop space $$\xymatrix{
  \cL X \times_X Z \simeq X \times_{X \times X} Z & \ar[l]_-\sim  Z\times_{Z\times X} Z  \ar[r]^-\sim & Z \times_{X \times X} X \simeq Z \times_X \cL X
}$$ There is a natural rotational equivalence $\cL X \times_X Z \simeq Z \times_X \cL X$ that makes the above two identifications coincide. (It does not preserve base points and is not given by swapping the factors). Thus we can unambiguously identify all of the above versions of the based loop space.

::: prop
[]{#basic stack dimensions label="basic stack dimensions"}

\(1\) Any derived stack $X$ is dualizable as an object of $Corr_k$, with dual $X^\vee$ identified with $X$ itself, and dimension $\dim(X)$ identified with the loop space $$\cL X= X^{S^1}\simeq X\times_{X\times X} X$$ regarded as a self-correspondence of $pt=\Spec k$.

\(2\) The transpose of any correspondence $X\leftarrow Z\to  Y$ is identified with the reverse correspondence $Y \leftarrow Z \to  X$. The trace of a self-correspondence $X\leftarrow Z\to X$ is identified with the based loop space $$\xymatrix{ 
\Tr(Z)\simeq Z|_{\Delta_X} = Z\times_{X\times X} X \simeq \cL_Z X
 }$$ regarded as a self-correspondence of $pt=\Spec k$.

In particular, the trace of the graph $\Gamma_f \to X\times X$ of a self-map $f:X\to X$ is identified with the fixed point locus $$\xymatrix{
\Tr(f) \simeq  \Gamma_f|_{\Delta_X} = \Gamma_f \times_{X\times X} X \simeq X^f  
}$$
:::

::: proof
*Proof.* The evaluation and coevaluation presenting the self-duality of $X$ are both given by $X$ itself as a correspondence between $pt=\Spec k$ and $X\times X$ via the diagonal map. The standard identities follow from the calculation of the fiber product of the two diagonal maps $$X{}_{\Delta_{12}}\times_{X\times X\times X}{}_{\Delta_{23}} X\simeq X$$ Thus the dimension of $X$ is the loop space $$\xymatrix{&&\cL X \ar[ld]\ar[rd]&&\\
&X\ar[ld]\ar[rd]&&X\ar[ld]\ar[rd]& \\
pt&&X \times X&&pt}$$

By definition, the transpose of a correspondence $X\leftarrow Z\to  Y$ is identified with $Y\leftarrow Z\to  X$ by checking the definition $$\xymatrix{&&& Z \ar[ld]\ar[rd] &&&\\
&& Y \times Z \ar[ld]\ar[rd]   && Z  \ar[ld]\ar[rd] \times X && \\
&Y \times X\ar[ld]\ar[rd]&& Y \times Z \times X \ar[ld]\ar[rd] && Y \times X\ar[ld]\ar[rd]& \\
Y&&Y \times X \times X&&Y \times Y \times X && X}$$ The trace of a self-correspondence $X\leftarrow Z\to  X$ is then calculated by the composition $$\xymatrix{&&& Z\times_{Z\times X} Z \ar[ld]\ar[rd] &&&\\
&&  Z\ar[ld]\ar[rd]   &&   \ar[ld]\ar[rd] Z  && \\
&X \ar[ld]\ar[rd]&&Z \times X \ar[ld]\ar[rd] &&  X\ar[ld]\ar[rd]& \\
pt&&X \times X &&X \times X && pt}$$

Finally, the case of the graph $Z=\Gamma_f$ of a self-map gives the fixed point locus by definition. ◻
:::

::: remark
[]{#rem: cyclic label="rem: cyclic"} The identification $\dim(X)\simeq \cL X$ above is naturally $S^1$-equivariant for the standard loop rotation on $\cL X$ and the cyclic symmetry of $\dim(X)$ provided by the cobordism hypothesis. To see this it is useful to consider $X$ as an $E_\infty$-algebra object in $Stacks_k^{op}$ via the diagonal map (or as an $E_n$-object for any $n$). In other words, for $n=1$ we identify stacks and correspondences with objects and morphisms in the Morita category $Alg(Stacks_k^{op})$. It follows from the properties of topological chiral homology [@HA Theorem 5.3.3.8] that for a (constant) commutative algebra $A$ its topological chiral homology over a manifold is given by the tensoring of commutative algebras over simplicial sets $\int_M A= M\ot A$. In particular (passing back from the opposite category to stacks) we have $\int_{S^1} X = X^{S^1}=\cL X$. Moreover this identification holds not just for a fixed circle but over the moduli space of circles $BDiff(S^1)\sim BS^1$, i.e. equivariantly for rotation. We also know from [@HA Example 5.3.3.14] or [@TFT Example 4.2.2] that the $S^1$-action on the dimension of an associative algebra $A$ (given classically by the cyclic structure on the Hochschild chain complex) is given by the rotation $S^1$-action on the topological chiral homology $\int_{S^1} A$, i.e., the family of topological chiral homologies over the moduli space of circles. In our case this recovers the rotation action on the loop space.
:::
