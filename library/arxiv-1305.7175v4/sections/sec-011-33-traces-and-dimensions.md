---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-011-33-traces-and-dimensions
section_title: "Traces and dimensions"
section_number: 3.3
pages: 19-21
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.969
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
(We continue to refer to [@TV; @HSS] for thorough treatments of the theory of traces in higher category theory.)

Let $A\in \cA$ be a dualizable object with dual $A^{\vee}$. Consider an endomorphism $$\xymatrix{
\Phi:A \ar[r] & A
}$$ Since $A$ is dualizable, $\Phi$ has a trace defined as follows.

::: defn
[]{#trace1 label="trace1"}

\(1\) The *trace* of $\Phi: A\to A$ is the object $\Tr(\Phi)\in
\Omega\cA$ defined by $$\xymatrix{1_{\cA}\ar[r]^-{\eta_A}\ar@/_2pc/@{-}^-{\Tr(\Phi)}[rrrr]& A\ot A^\vee \ar[rr]^-{\Phi\ot\id_A}& &  A\ot A^\vee
\ar[r]^-{\epsilon_A}& 1_\cA}.$$

Given a natural transformation $\varphi:\Phi\to \Psi$, we define the induced morphism $$\xymatrix{
\Tr(\varphi):\Tr(\Phi)\ar[r] & \Tr(\Phi')
}$$ by applying $\varphi\ot\id_{A^{\vee}}$ to the middle arrow above.

\(2\) The *dimension* (or *Hochschild homology) of $A$ is the trace of the identity $$\dim(A)=\Tr(\id_A)\in \Omega\cA$$ or in other words, the object defined by $$\xymatrix{ 1_\cA\ar[rr]^-{\eta_A}\ar@/_2pc/@{-}^-{\dim(A)}[rrrr] &&
  A\ot A^\vee \ar[rr]^-{\epsilon_A}&& 1_\cA}$$*
:::

::: remark
Equivalently, we can describe the trace as the composition $$\xymatrix{1_{\cA}\ar[r]^-{\Phi}& \End(A)\ar[r]^-{\sim} &  A\ot A^{\vee}
\ar[r]^-{\epsilon_A}& 1_\cA}$$ where the middle arrow is the identification deduced from the dualizability of $A$.
:::

::: remark
Observe that for fixed dualizable $A\in \cA$, taking traces gives a functor $$\xymatrix{
\Tr:\End(A) \ar[r] & \Omega\cA
}$$
:::

::: remark
Observe that for any dualizable endomorphism $\Phi$, the standard identities encoded by Diagrams [\[standard identities\]](#standard identities){reference-type="ref" reference="standard identities"} give rise to an identification $$\Tr(\Phi)\simeq \Tr(\Phi^\vee)$$
:::

::: example
When $A = 1_\cA$ is the monoidal unit, and $\Phi:1_\cA \to 1_\cA$ is an endomorphism, we have an evident equivalence of endomorphisms $$\Tr(\Phi) \simeq \Phi$$
:::

::: thm
[]{#thm lurie S1-action label="thm lurie S1-action"} There is a canonical $S^1$-action on the dimension $\dim(A)$ of any dualizable object $A$ of a symmetric monoidal $\oo$-category $\cA$.
:::

### Cyclic symmetry

::: prop
[]{#cyclic trace label="cyclic trace"} Given two morphisms $$\xymatrix{A  \ar@<+.5ex>[r]^\Phi &
  \ar@<+.5ex>[l]^{\Psi}B}$$ between dualizable objects $A, B\in \cA$, there is a canonical equivalence $$\xymatrix{
m(\Phi, \Psi):\Tr(\Phi\circ \Psi) \ar[r]^-\sim & \Tr(\Psi \circ \Phi)
}$$ functorial in morphisms of both $\Phi$ and $\Psi$.
:::

::: proof
*Proof.* We construct $m(\Phi,\Psi)$ following the commutative diagram below:

$$\xymatrix{ & A\ot A^\vee\ar[r]^-{\Phi\otimes \id_{A^\vee}}     \ar[ddr]^-{\id_{A} \ot \Psi^\vee}       & B\ot A^\vee
 \ar[r]^-{\Psi\ot \id_{A^\vee}} \ar[ddr]^-{\id_{B} \ot \Psi^\vee}  &  A\ot A^\vee 
\ar[dr]^-{\epsilon_{A}} &\\
1_\cA\ar[ur]^-{\eta_A} \ar[dr]_-{\eta_B} & &  && 1_{\cA}\\
& B\ot B^\vee   \ar[r]_-{\Psi\ot \id_{B^\vee}}    & A\ot B^\vee \ar[r]_-{\Phi\ot \id_{B^\vee}} &
B\ot B^\vee  \ar[ur]_-{\epsilon_B} & }$$

Following the top edge, we find the definition of $\Tr(\Psi\circ\Phi)$. Following the bottom edge, we find the definition of $\Tr(\Phi\circ \Psi)$. The identifications filling the left and right diamonds arise from the standard identities encoded by Diagrams [\[standard identities\]](#standard identities){reference-type="ref" reference="standard identities"}. The identification filling the central square results from the symmetric monoidal structure.

The construction is evidently functorial for morphisms $\Phi\to \Phi'$. The functoriality for morphisms $\Psi\to \Psi'$ is similar, once one recalls that the construction $\Psi\mapsto \Psi^\vee$ is covariantly functorial in morphisms of $\Psi$. ◻
:::

::: example
Taking $\Phi= \id_A$ yields a canonical equivalence $$\xymatrix{
\gamma': \id_{\Tr(\Phi')} \ar[r]^-\sim & m( \id_A, \Phi'_A) 
}$$ and likewise, taking $\Phi'= \id_A$ yields a canonical equivalence $$\xymatrix{
\gamma: \id_{\Tr(\Phi)} \ar[r]^-\sim & m( \Phi_A, \id_A) 
}$$ Thus taking $\Phi= \Phi' =\id_A$ yields an automorphism of the identity of the Hochschild homology $$\xymatrix{
 (\gamma')^{-1}\circ \gamma:\id_{\Tr(\id_A)} \ar[r]^-\sim & \id_{\Tr(\id_A)}
}$$ called the *BV homotopy*.
:::

::: remark
The proposition is only the initial part of the full cyclic symmetry of trace (see Remark [\[full trace\]](#full trace){reference-type="ref" reference="full trace"}), and the example is the lowest level structure of the $S^1$-action on Hochschild homology (see Theorem [\[thm lurie S1-action\]](#thm lurie S1-action){reference-type="ref" reference="thm lurie S1-action"}) defining cyclic homology.
:::

::: lemma
[]{#cyclic composition label="cyclic composition"} Given morphisms $$\xymatrix{A\ar[r]^-{\Phi}& B\ar[r]^-{\Psi} & C\ar[r]^-{\Upsilon}& A}$$ between dualizable objects $A, B, C\in \cA$, there is a canonical commutative diagram $$\xymatrix{\Tr(\Psi\Phi\Ups) \ar[rr]^-{m(\Psi,\Phi\Ups)} \ar[drr]_-{m(\Psi\Phi,\Ups)}&& \Tr(\Phi\Ups\Psi)\ar[d]^-{m(\Phi,\Ups\Psi)} \\ 
&& \Tr(\Ups\Psi\Phi)}$$
:::

::: proof
*Proof.* We construct the desired equivalence from the following diagram:

$$\xymatrix{ & C\ot C^\vee\ar[r]^-{\Ups}           \ar[dr]^-{\Psi^\vee}
& A\ot C^\vee  \ar[r]^-{\Phi} \ar[dr]^-{ \Psi^\vee}  
& B\ot C^\vee \ar[r]^-{\Psi}\ar[dr]^-{ \Psi^\vee} 
&  C\ot C^\vee 
\ar[dr]^-{\epsilon_{C}} &
\\
1_\cA\ar[ur] \ar[r] \ar[dr]
& B\ot B^\vee   \ar[r]^-{\Psi}  \ar[dr]^-{\Phi^\vee}  & C\ot B^\vee \ar[r]^-{\Ups} \ar[dr]^-{\Phi^\vee}&
A\ot B^\vee\ar[r]^-{\Phi} \ar[dr]^-{\Phi^\vee} & B\ot B^\vee \ar[r] & 1_{\cA}\\
& A\ot A^\vee\ar[r]^-{\Phi}          
& B\ot A^\vee  \ar[r]^-{\Psi}   
& C\ot A^\vee \ar[r]^-{\Ups}
&  A\ot A^\vee 
\ar[ur]^-{\epsilon_{A}} &
}$$

The natural transformations $m(\Psi,\Phi\Ups)$ and $m(\Phi,\Ups\Psi)$ describe passage from the top row to the middle row and from the middle to the bottom, respectively. The transformation $m(\Psi\Phi,\Ups)$ can then be identified with the transformation from the top row to the bottom given by inserting the diagonal morphisms $\id\ot \Phi^\vee\circ\Psi^\vee$ and using standard composition identities. ◻
:::
