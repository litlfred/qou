---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-010-32-dualizability
section_title: "Dualizability"
section_number: 3.2
pages: 17-19
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.94
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
::: defn
An object $A$ of the symmetric monoidal $(\oo, 2)$-category $\cA$ is said to be *dualizable* (equivalently, $A$ is dualizable in the $(\oo,1)$-category $f(\cA)$) if it admits a monoidal dual: there is a dual object $A^\vee \in \cA$ and evaluation and coevaluation morphisms $$\xymatrix{
\epsilon_A:A^\vee \otimes A\ar[r] & 1_\cA
&
\eta_A:1_\cA \ar[r] & A \otimes A^\vee
}$$

such that the usual compositions are naturally equivalent to the identity morphism $$\xymatrix{
A \ar[rr]^-{\eta_A \otimes \id_A} && A \otimes A^\vee \otimes A
\ar[rr]^-{ \id_A\otimes \epsilon_A} && A 
&
A^\vee \ar[rr]^-{ \id_{A^\vee} \otimes \eta_A} && A^\vee \otimes A \otimes A^\vee 
\ar[rr]^-{ \epsilon_A\otimes  \id_{A^\vee}} && A^\vee 
}$$
:::

::: example
Any algebra object $A\in \Alg(\cC)$ is dualizable with dual the opposite algebra $A^{op}\in \Alg(\cC)$. The evaluation morphism $$\xymatrix{
\epsilon_A: A^{op} \otimes A \ar[r] & 1_\cC
}$$ is given by $A$ itself regarded as an $A$-bimodule. The coevaluation morphism $$\xymatrix{
\eta_A:  1_\cC \ar[r] &A \otimes A^{op} 
}$$ is also given by $A$ itself regarded as an $A$-bimodule.
:::

### Dualizable morphisms {#dualizable morphisms}

Consider two objects $A, B\in \cA$, and a morphism $$\xymatrix{
\Phi:A \ar[r] & B.
}$$

::: example
If $\cA = \Alg(\cC)$, then $\Phi$ is simply an $A^{op}\otimes B$-module.
:::

If $B$ is dualizable with dual $B^{\vee}$, we can package $\Phi$ in the equivalent form of the morphism $$\xymatrix{
e_{\Phi}:B^{\vee} \otimes A \to 1_\cA}$$ defined by

$$\xymatrix{  
 B^\vee\ot A  \ar[d]_-{\id_{B^\vee} \ot \Phi} \ar[r]^-{e_\Phi} & 1_{\cA}\\
 B\ot B^\vee \ar[ur]^-{\epsilon_B} & }$$

If $A$ is dualizable with dual $A^{\vee}$, we can package $\Phi$ in the equivalent form of the morphism $$\xymatrix{
u_\Phi:1_\cA\to B\ot A^\vee}$$ defined by $$\xymatrix{ & A\ot A^\vee\ar[d]^-{\Phi\otimes \id_{A^\vee}}\\
1_\cA\ar[ur]^-{\eta_A} \ar[r]^-{u_\Phi} & B\ot A^\vee}$$

If both $A$ and $B$ are dualizable, we can also encode $\Phi$ by its dual morphism $$\xymatrix{
\Phi^\vee:B^\vee\ar[r] & A^\vee
}$$ defined by $$\xymatrix{ B^\vee  \ar@/_2pc/^-{\Phi^\vee}[rrrrrr]  \ar[rr]^-{\id_{B^\vee}\otimes \eta_A} && B^\vee \ot A\ot A^\vee 
\ar[rr]^-{\id_{B^\vee} \otimes \Phi\otimes \id_{A^\vee}}
&& B^\vee \ot B\ot A^\vee \ar[rr]^-{\epsilon_{B^\vee}\ot\id_{A^\vee}} && A^\vee}$$ There is a natural composition identity $$(\Phi\Psi)^\vee\simeq \Psi^\vee \Phi^\vee$$ Note that for fixed $A, B$, the construction $\Phi\mapsto \Phi^\vee$ naturally defines a covariant map $$\xymatrix{
(-)^\vee:\Hom(A,B)\ar[r]& \Hom(B^\vee,A^\vee)
}$$ and in particular a morphism $\Phi_1\to \Phi_2$ induces a natural morphism $\Phi_1^\vee\to \Phi_2^\vee$.

Let us record the canonical equivalences encoded by the following commutative diagrams

$$\label{standard identities}
\xymatrix{ & A\ot A^\vee\ar[d]^-{\Phi\otimes \id_{A^\vee}}                 &&&  
A^\vee\ot A \ar[dr]^-{\epsilon_{A^\vee}} &\\
1_\cA\ar[ur]^-{\eta_A} \ar[dr]_-{\eta_B} \ar[r]^-{u_\Phi} & B\ot A^\vee &&& 
B^\vee\ot A \ar[u]^-{\Phi^\vee\ot \id_A} \ar[r]^-{e_\Phi}\ar[d]_-{\id_{B^\vee} \ot \Phi} & 1_{\cA}\\
& B\ot B^\vee \ar[u]_-{\id_B\ot \Phi^\vee}                                                &&&
B\ot B^\vee  \ar[ur]_-{\epsilon_B} & }$$

::: example
In the setting of algebras, bimodules and intertwiners, the morphisms $\Phi$, $u_\Phi$, $e_\Phi$ and $\Phi^\vee$ are all different manifestations of the same bimodule $\Phi$, making their various compatibilities particularly evident.
:::

::: defn
\(1\) A morphism $\Phi: A\to B$ is said to be *left dualizable* if it admits a left adjoint: there is a morphism $\Phi^\ell: B\to A$ and unit and counit morphisms $$\xymatrix{
\eta_ \Phi: \id_B \ar[r] & \Phi \circ \Phi ^\ell
&
\eps_\Phi : \Phi ^\ell \circ \Phi\ar[r] & \id_A
}$$ satisfying the usual identities.

\(2\) A morphism $\Phi: A\to B$ is said to be *right dualizable* if it admits a right adjoint: there is a morphism $\Phi^r: B\to A$ and unit and counit morphisms $$\xymatrix{
\eta_ \Phi: \id_A \ar[r] & \Phi^r \circ \Phi 
&
\eps_\Phi : \Phi  \circ \Phi^r\ar[r] & \id_B
}$$ satisfying the usual identities.
:::

::: remark
If $A$ and $B$ are dualizable, and $\Phi: A\to B$ is left (resp. right) dualizable, then $\Phi^\vee: B^{\vee}\to A^{\vee}$ is right (resp. left) dualizable with right adjoint $(\Phi^\ell)^{\vee}:A^{\vee}\to B^{\vee}$ (resp. left adjoint $(\Phi^r)^{\vee}:A^{\vee}\to B^{\vee}$).
:::
