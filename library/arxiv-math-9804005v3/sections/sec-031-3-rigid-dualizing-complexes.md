---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-031-3-rigid-dualizing-complexes
section_title: "Rigid Dualizing Complexes"
section_number: 3
pages: 16-18
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
text_source: latex
latex_prose_ratio: 0.633
latex_coverage_ratio: 0.926
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
In this section we consider dualizing complexes which satisfy a special condition discovered by Van den Bergh [@VdB]. Rigid dualizing complexes are unique and even functorial. Furthermore if $R$ is an Auslander rigid dualizing complex then the canonical dimension $\operatorname{Cdim}_{R}$ is particularly well behaved (as examples indicate; see Question [\[a4.15\]](#a4.15){reference-type="ref" reference="a4.15"}). By default $A$ and $B$ denote noetherian $k$-algebras.

First we shall need some more notation for bimodules. Suppose $A$ and $B$ are $k$-algebras. For an element $a \in A$ we denote by $a^{\circ} \in A^{\circ}$ the same element. Thus for $a_{1}, a_{2} \in A$, $a_{1}^{\circ} \cdot a_{2}^{\circ} =
(a_{2} \cdot a_{1})^{\circ} \in A^{\circ}$. With this notation if $M$ is a right $A$-module then the left $A^{\circ}$ action is $a^{\circ} \cdot m = m \cdot a$, $m \in M$. The algebra $A^{\mathrm{e}}$ has an involution $A^{\mathrm{e}} \rightarrow(A^{\mathrm{e}})^{\circ}$, $a_{1} \otimes a_{2}^{\circ} \mapsto a_{2} \otimes a_{1}^{\circ}$ which allows us to regard every left $A^{\mathrm{e}}$-module $M$ as a right $A^{\mathrm{e}}$-module in a consistent way: $$(a_{1} \otimes a_{2}^{\circ}) \cdot m =
(a_{2} \otimes a_{1}^{\circ})^{\circ} \cdot m =
m \cdot (a_{2} \otimes a_{1}^{\circ}) = a_{1} \cdot m \cdot a_{2} .$$

Given an $(A \otimes B)$-module $M$ and a $(B \otimes A)$-module $N$ we define a mixed action of $A^{\mathrm{e}} \otimes B^{\mathrm{e}}$ on the tensor product $M \otimes N$ as follows. $A^{\mathrm{e}}$ acts on $M \otimes N$ by the outside action $$(a_{1} \otimes a_{2}^{\circ}) \cdot (m \otimes n) :=
(a_{1} \cdot m) \otimes (n \cdot a_{2}) ,$$ whereas $B^{\mathrm{e}}$ acts on $M \otimes N$ by the inside action $$(b_{1} \otimes b_{2}^{\circ}) \cdot (m \otimes n) :=
(m \cdot b_{2}) \otimes (b_{1} \cdot n) .$$ By default we regard the outside action as a left action and the inside action as a right action. If $A = B$ and $M = N$ then the two actions by $A^{\mathrm{e}}$ on $M \otimes M$ are interchanged the involution $m_{1} \otimes m_{2} \mapsto m_{2} \otimes m_{1}$. However for the sake of definiteness in this case, given an $A^{\mathrm{e}}$-module $L$, $\operatorname{Hom}_{A^{\mathrm{e}}}(L, M \otimes M)$ shall refer to homomorphisms $L \rightarrow M \otimes M$ which are $A^{\mathrm{e}}$-linear with respect to the outside action.

::: dfn
[]{#a4.1 label="a4.1"} Suppose $R$ is a dualizing complex over $A$. If there is an isomorphism $$\phi : R \stackrel{\simeq}{\rightarrow}\mathrm{R} \operatorname{Hom}_{A^{\mathrm{e}}}(A, R \otimes R)$$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$, we call $(R, \phi)$ a *rigid dualizing complex*.
:::

It is obvious that if $R$ is rigid, then any shift $R[n]$, for $n \neq 0$, is no longer rigid. Van den Bergh proved that a rigid dualizing complex $(R, \phi)$ over $A$ is unique, up to an isomorphism in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$ (see [@VdB] Proposition 8.2). Below we extend this result by proving that rigid dualizing complexes are functorial, in a suitable sense.

Let $A \rightarrow B$ be a $k$-algebra homomorphism. Given $M \in \mathsf{D}^{+}(\operatorname{\mathsf{Mod}} B)$, $N \in \mathsf{D}^{+}(\operatorname{\mathsf{Mod}} A)$ and a morphism $\psi : M \rightarrow N$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A)$, $\psi$ factors naturally through $\mathrm{R} \operatorname{Hom}_{A}(B, N)$. This can be seen by replacing $N$ with an injective resolution $I$ in $\mathsf{D}^{+}(\operatorname{\mathsf{Mod}} A)$, and then we can take $\psi$ to be a homomorphism of complexes. The image of $\psi$ will then land inside $\operatorname{Hom}_{A}(B, I)$. The same fact is true for bimodules.

We say a $k$-algebra homomorphism $A \rightarrow B$ if *finite* if $B$ is finitely generated as a left and as a right $A$-module.

::: thm
[]{#a4.2 label="a4.2"} Let $A \rightarrow B$ be a finite $k$-algebra homomorphism. Suppose $A$ and $B$ have rigid dualizing complexes $(R_{A}, \phi_{A})$ and $(R_{B}, \phi_{B})$ respectively. Then there is *at most one* morphism $\psi : R_{B} \rightarrow R_{A}$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$ satisfying conditions [(i)]{.upright} and [(ii)]{.upright} below:

1.  $\psi$ induces an isomorphism $$R_{B} \cong \mathrm{R} \operatorname{Hom}_{A}(B, R_{A}) \cong
    \mathrm{R} \operatorname{Hom}_{A^{\circ}}(B, R_{A})$$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$.

2.  The diagram $$\begin{CD}
    R_{B} @> \phi_{B} >>
    \mathrm{R} \operatorname{Hom}_{B^{\mathrm{e}}}
    (B, R_{B} \otimes R_{B}) \\
    @V \psi VV @V \psi \otimes \psi VV \\
    R_{A} @> \phi_{A} >>
    \mathrm{R} \operatorname{Hom}_{A^{\mathrm{e}}}
    (A, R_{A} \otimes R_{A})
    \end{CD}$$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$ is commutative.
:::

The theorem is proved after this lemma. Given a $k$-algebra homomorphism $A \rightarrow B$, denote by $\mathrm{Z}_{B}(A) \subset B$ the centralizer of $A$.

::: lem
[]{#a4.3 label="a4.3"} Let $A \rightarrow B$ be a finite $k$-algebra homomorphism. Suppose $A$ and $B$ have dualizing complexes $R_{A}$ and $R_{B}$ respectively, and $\psi : R_{A} \rightarrow R_{B}$ is a morphism in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$ satisfying condition [(i)]{.upright} of the theorem. Then $\operatorname{Hom}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(R_{B}, R_{A})$ is a free left and right $\mathrm{Z}_{B}(A)$-module with basis $\psi$.
:::

::: proof
*Proof.* Denote by $D := \mathrm{R} \operatorname{Hom}_{A}(-, R_{A})$ and $D^{\circ} := \mathrm{R} \operatorname{Hom}_{A^{\circ}}(-, R_{A})$ the dualizing functors. By assumption $R_{B} \cong D^{\circ} B$. Applying the functor $D$ we get isomorphisms of left $\mathrm{Z}_{B}(A)$-modules $$\begin{aligned}
\operatorname{Hom}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(R_{B}, R_{A}) & \cong
\operatorname{Hom}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(D^{\circ} B, D^{\circ} A)
\\ & \cong
\operatorname{Hom}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(A, B) \\
& \cong \operatorname{Hom}_{A^{\mathrm{e}}}(A, B) \cong \mathrm{Z}_{B}(A) .
\end{aligned}$$ Likewise for the right action. ◻
:::

::: proof
*Proof of the theorem.* Assume $\psi'$ is another such isomorphism. According to the lemma above, $$\psi' = (b_{1} \otimes 1) \psi = (1 \otimes b_{2}^{\circ}) \psi$$ for suitable $b_{i} \in \mathrm{Z}_{B}(A)^{\times}$. So $$\psi' \otimes \psi' = (b_{1} \otimes b_{2}^{\circ})
(\psi \otimes \psi) .$$ Now the diagram in condition (ii) consists of morphisms in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$. Since multiplications by $b_{1}$ and $b_{2}^{\circ}$ are $A^{\mathrm{e}}$-linear, we see that $$(b_{1} \otimes 1) \psi = (b_{1} \otimes b_{2}^{\circ}) \psi
\in \operatorname{Hom}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(R_{B}, R_{A}) .$$ Hence dividing by the unit $b_{1} \otimes 1$, we see that $b_{2} = 1$. ◻
:::

::: cor
[]{#a4.6 label="a4.6"} A rigid dualizing complex $(R, \phi)$ over $A$ is unique up to a unique isomorphism.
:::

::: proof
*Proof.* Suppose $(R', \phi')$ is another rigid dualizing complex. We claim that there is an isomorphism $\psi : R \stackrel{\simeq}{\rightarrow}R'$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})$ which satisfies condition (ii) of the theorem. By Theorem [\[a4.2\]](#a4.2){reference-type="ref" reference="a4.2"} such $\psi$ is unique.

To produce $\psi$, choose any isomorphism $\psi' : R \stackrel{\simeq}{\rightarrow}R'$, which we know exists by [@VdB] Proposition 8.2. Then by Lemma [\[a4.3\]](#a4.3){reference-type="ref" reference="a4.3"} there are $a_{i} \in \mathrm{Z}(A)^{\times}$ such that $$(a_{1} \otimes 1)^{-1} \psi' =
(1 \otimes a_{2}^{\circ})^{-1} \psi' =
{\phi'}^{-1} (\psi' \otimes \psi') \phi .$$ The isomorphism $$\psi := (a_{1} \otimes 1) \psi' =
(1 \otimes a_{2}^{\circ}) \psi'$$ will satisfy condition (ii). ◻
:::

Thus we may speak of *the* rigid dualizing complex of $A$ (if it exists).

Lemma [\[a4.3\]](#a4.3){reference-type="ref" reference="a4.3"} can be sharpened when $A = B$.

::: prop
[]{#a4.4 label="a4.4"} Let $(R, \phi)$ be a rigid dualizing complex over $A$. Then the two $k$-algebra homomorphisms $$\lambda, \rho : \mathrm{Z}(A) \rightarrow
\operatorname{End}_{\mathsf{D}(\operatorname{\mathsf{Mod}} A^{\mathrm{e}})}(R)$$ from the center of $A$, namely left and right multiplication, are both isomorphisms, and are equal.
:::

::: proof
*Proof.* By Lemma [\[a4.3\]](#a4.3){reference-type="ref" reference="a4.3"} with $A = B$ and $\psi = 1$, we see that $\lambda$ and $\rho$ are isomorphisms. Take $a \in \mathrm{Z}(A)$, and let $a' := \rho^{-1} \lambda(a) \in \mathrm{Z}(A)$. Using the definition of the mixed action on $R \otimes R$ and the rigidification isomorphism $\phi$, the commutation (or conjugation) of $a$ across $R$ is transferred to commutation of $a'$ across $A$. Since $a'$ does commute with $A$ it follows that $\lambda(a) = \rho(a)$ (and so in fact $a' = a$). ◻
:::

We will often omit reference to the rigidifying isomorphism $\phi$.

::: cor
[]{#a4.5 label="a4.5"} If $R$ is a rigid dualizing complex over $A$ then for any $q$ the cohomology bimodule $\mathrm{H}^{q} R$ is central over $\mathrm{Z}(A)$.
:::

::: dfn
[]{#a4.7 label="a4.7"} Let $A \rightarrow B$ be a finite homomorphism of $k$-algebras. Assume the rigid dualizing complexes $(R_{A}, \phi_{A})$ and $(R_{B}, \phi_{B})$ exist. If there is a morphism $\psi$ satisfying the conditions of Theorem [\[a4.2\]](#a4.2){reference-type="ref" reference="a4.2"} then we call it the *trace morphism* and denote it by $\operatorname{Tr}_{B / A}$.
:::

The next corollary is obvious.

::: cor
[]{#a4.8 label="a4.8"} Let $A \rightarrow B$ and $B \rightarrow C$ be finite $k$-algebra homomorphisms. Assume the rigid dualizing complexes $(R_{A}, \phi_{A})$, $(R_{B}, \phi_{B})$ and $(R_{C}, \phi_{C})$ and the trace morphisms $\operatorname{Tr}_{B / A}$ and $\operatorname{Tr}_{C / B}$ exist. Then $\operatorname{Tr}_{C / A}$ exists too, and $$\operatorname{Tr}_{C / A} = \operatorname{Tr}_{B / A} \operatorname{Tr}_{C / B} .$$
:::

The existence of the trace morphism allows to transfer good properties of $R_{A}$ to $R_{B}$.

::: prop
[]{#a4.9 label="a4.9"} Let $A \rightarrow B$ be a finite homomorphism of $k$-algebras, and assume the rigid dualizing complexes $R_{A}$ and $R_{B}$ and the trace morphism $\operatorname{Tr}_{B / A}$ exist.

1.  Let $C$ be any $k$-algebra. Then for $M \in \mathsf{D}(\operatorname{\mathsf{Mod}} (B \otimes C^{\circ}))$ there is a functorial isomorphism $$\mathrm{R} \operatorname{Hom}_{B}(M, R_{B}) \cong
    \mathrm{R} \operatorname{Hom}_{A}(M, R_{A})$$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} (C \otimes A^{\circ}))$.

2.  If $R_{A}$ is Auslander then so is $R_{B}$.

3.  For any $B$-module $M$, $\operatorname{Cdim}_{R_{A}; A} M = \operatorname{Cdim}_{R_{B}; B} M$.

4.  If $R_{A}$ is $\operatorname{GKdim}$-Macaulay, then so is $R_{B}$.

5.  Suppose $A \rightarrow B$ is surjective. If $R_{A}$ is $\operatorname{Kdim}$-Macaulay then so is $R_{B}$.
:::

::: proof
*Proof.* 1. We can assume $R_{A}$ and $R_{B}$ are complexes of injectives over $A^{\mathrm{e}}$ and $B^{\mathrm{e}}$ respectively, and $\operatorname{Tr}_{B / A}$ is a homomorphism of complexes. Then we get a functorial morphism $\mathrm{R} \operatorname{Hom}_{B}(M, R_{B}) \rightarrow\mathrm{R} \operatorname{Hom}_{A}(M, R_{A})$ in $\mathsf{D}(\operatorname{\mathsf{Mod}} (C \otimes A^{\circ}))$. To prove it's an isomorphism we can forget the $C$-module structure. Because the two functors are way-out in both directions (see [@RD] Section I.7), and they send direct sums to direct products, it suffices to check for an isomorphism when $M = B$. But that's given.\
2, 3. Let $M$ be a finitely generated $B$-module and $N \subset \operatorname{Ext}^{q}_{B}(M, R_{B})$ a $B^{\circ}$-submodule. Then by part 1, $N \subset \operatorname{Ext}^{q}_{A}(M, R_{A})$ as $A^{\circ}$-modules, and for every $p$, $\operatorname{Ext}^{p}_{B^{\circ}}(N, R_{B}) \cong
\operatorname{Ext}^{p}_{A^{\circ}}(N, R_{A})$ as $A$-modules. This proves the Auslander condition for $B$ and the dimension equality for finitely generated $B$-modules.\
4. Follows from part 3 and the fact $\operatorname{GKdim}_{A} M = \operatorname{GKdim}_{B} M$.\
5. Similar to 4. ◻
:::

::: dfn
[]{#a4.11 label="a4.11"} Suppose $A$ has an Auslander rigid dualizing complex $R$. Then we denote the canonical dimension $\operatorname{Cdim}_{R}$ by $\operatorname{Cdim}$.
:::

::: exa
[]{#a4.10 label="a4.10"} Suppose $A$ is an affine $k$-algebra and finite over its center. Then we can find a smooth integral commutative $k$-algebra $C$ (e.g. a polynomial algebra), and a finite homomorphism $C \rightarrow\mathrm{Z}(A)$. Say $\operatorname{Kdim} C = n$. Since $\Omega^{n}_{C / k}[n]$ is a rigid dualizing complex over $C$, it follows from [@Ye3] Proposition 5.9 that $$R := \mathrm{R} \operatorname{Hom}_{C}(A, \Omega^{n}_{C / k}[n])$$ is a rigid dualizing complex over $A$.
:::

::: exa
Let $A$ be the algebra $\left( \begin{smallmatrix} k & V \\ 0 & k \end{smallmatrix}
\right)$ where $V$ is a finite rank $k$-module. The rigid dualizing complex is $A^{*} := \operatorname{Hom}_{k}(A, k)$. Now $A$ is hereditary, hence Gorenstein, so the bimodule $A$ is a dualizing complex. When $V \neq 0$ the dualizing complexes $A$ and $A^{*}$ are not isomorphic, so $A$ is not rigid then.
:::

::: exa
Let $t_{1}, t_{2}, \ldots$ be a countable sequence of commuting indeterminates and let $C := k(t_{1}, t_{2}, \ldots)$ be the field of rational functions. We claim that as $k$-algebra, $C$ has no rigid dualizing complex. Since any dualizing complex over $C$ has to be of the form $R = C^{\sigma}[n]$ for an automorphism $\sigma$ and an integer $n$ (by [@Ye3] Corollary 4.6 and Propositions 3.4 and 3.5), it suffices to prove that $\operatorname{Ext}^{i}_{C^{\mathrm{e}}}(C, C^{\mathrm{e}}) = 0$ for all $i$. This follows from the next lemma with $n = 0$.
:::

::: lem
[]{#a5.8 label="a5.8"} Let $D_{n} := C^{\mathrm{e}} / I$ where $I$ is the ideal generated by the elements $f_{j} := x_{j} \otimes 1 - 1 \otimes x_{j}$ for $j = 1, \ldots, n$. Then $\operatorname{Ext}^{i}_{C^{\mathrm{e}}}(C, D_{n}) = 0$ for all $i, n \geq 0$.
:::

::: proof
*Proof.* Assume on the contrary that $\operatorname{Ext}^{i}_{C^{\mathrm{e}}}(C, D_{n}) \neq 0$ for some $i$ and $n$. Let $i_0$ be the smallest such $i$. Since $f_{n + 1}$ is nonzero in the domain $D_{n}$ there is a short exact sequence $$0 \rightarrow D_{n} \xrightarrow{f_{n + 1}} D_{n} \rightarrow D_{n+1} \rightarrow 0$$ of $C^{\mathrm{e}}$-modules. That induces an exact sequence $$0 = \operatorname{Ext}^{i_{0} - 1}_{C^{\mathrm{e}}}(C, D_{n+1}) \rightarrow
\operatorname{Ext}^{i_{0}}_{C^{\mathrm{e}}}(C, D_{n})
\xrightarrow{f_{n + 1}}
\operatorname{Ext}^{i_{0}}_{C^{\mathrm{e}}}(C, D_{n}) .$$ But $f_{n + 1}$ annihilates the $C^{\mathrm{e}}$-module $C$, which implies $\operatorname{Ext}^{i_{0}}_{C^{\mathrm{e}}}(C, D_{n}) = 0$, contradicting the choice of $i_{0}$. ◻
:::

We end the section with a basic question.

::: que
[]{#a4.15 label="a4.15"} Let $R$ be a rigid dualizing complex and $M$ an $A$-bimodule finitely generated on both sides. Is there a functorial isomorphism $\mathrm{R} \operatorname{Hom}_{A}(M, R) \cong
\mathrm{R} \operatorname{Hom}_{A^{\circ}}(M, R)$? Or, at least, is $\operatorname{Cdim}_{R; A} M = \operatorname{Cdim}_{R; A^{\circ}} M$?
:::

For a partial answer turn to Section 6, where the presence of auxiliary filtrations allows us to take advantage of results in Sections 4-5 on graded algebras.
