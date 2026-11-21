---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-011-32-transposes
section_title: "Transposes"
section_number: 3.2
pages: 22-24
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.972
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
A semi-rigid monoidal category $A\in Alg(St_\mathbb C)$, being compactly generated, is dualizable with dual $A'$. The coevaluation functor, $$\xymatrix{
\eta:\operatorname{Vect}_\mathbb C\ar[r] & A'\otimes A
}$$ sends the unit $\mathbb C$ to the Hom bimodule $[\mathop{\mathrm{Hom}}]\in A'\otimes A$ which is determined by $$\mathop{\mathrm{Hom}}_{A'\otimes A}(m\otimes n, [\mathop{\mathrm{Hom}}])=\mathop{\mathrm{Hom}}_A(m,n)$$ on compact objects $m\in A_c^{\diamondsuit}, n\in \otimes A_c$.

The dual $A'$ inherits a canonical coalgebra structure from the algebra structure on $A$ by taking transposes of all multiplication maps. An $A$-module $M$, with action map $a_M:A\otimes M\to M$, inherits a comodule structure over $A'$, with coaction map given by the transpose $$\xymatrix{a_M^t: M\ar[r]^-{\eta\otimes{\rm id}} & A'\otimes A\otimes M \ar[r]^-{{\rm id}\otimes a_M} & A'\otimes M}$$ It is evident from this construction that the comodule structure is functorial for all $A$-linear functors $M\to N$. In other words, we have an equivalence $$\mathop{\mathrm{Mod}}_A(St_\mathbb C) \simeq \mathop{\mathrm{Comod}}_{A'}(St_\mathbb C)$$ commuting with the natural forgetful functors to $St_\mathbb C$.

The left and right dualities on compact objects $$\xymatrix{
L(a) = {}^\vee a,&  R(a) =  a^\vee, &
\mbox{for $a\in A$ compact},
}$$ canonically extend by continuity to equivalences $$\xymatrix{
L, R: A\ar[r]^-\sim & A'
}$$ Let $LL,RR:A\to A$ denote the inverse monoidal automorphisms of $A$ given by taking double duals. Moreover, the identities $$\mathop{\mathrm{Hom}}_A({}^\vee(x\star m \star y), n)\simeq \mathop{\mathrm{Hom}}_A({}^\vee m, {}^{\vee\vee}y \star n\star x),$$ $$\mathop{\mathrm{Hom}}_A((x\star m \star y)^\vee, n)\simeq \mathop{\mathrm{Hom}}_A(m^\vee, y \star n\star x^{\vee\vee})$$ show that $L$ is a naturally a morphism of right $A$-modules and $R$ of left $A$-modules, while $L$ intertwines the left action of $A$ with the action twisted by the monoidal automorphism $LL:A\to A$, and likewise $R$ intertwines the right action of $A$ with the action twisted by the monoidal automorphism $RR:A\to A$. In other words, we have isomorphisms of $A$-bimodules $$\xymatrix{{}_{RR}A\ar[r]^-{L} & A'&\ar[l]_-{R}  A_{LL}}$$ where we twist the bimodule $A$ on one side or the other by the inverse monoidal automorphisms $LL,RR$.

::: definition
A *pivotal structure* on a semi-rigid monoidal category $A \in  Alg(St_\mathbb C)$ is a monoidal identification of the automorphism $LL$ (or equivalently, of its inverse $RR$) with the identity of $A$.
:::

It follows that a pivotal structure is equivalent to a lift of either of the functors $L,R:A\to A'$ to a morphism of $A$-bimodules (or to a monoidal identification of left and right duals in $A$).

::: example
For any semi-rigid monoidal category $A\in  Alg(St_\mathbb C)$, the semi-rigid monoidal category $A^e=A\otimes A^{op}$ has a canonical pivotal structure, deduced from its symmetric structure $\xymatrix{A^e\ar[r]^-{\sim} & (A^e)^{op}}$ exchanging left and right duals.
:::

::: remark
It is enlightening (though not necessary for the rest of this paper) to understand the notion of a pivotal structure in terms of traces.

Suppose $A\in  Alg(St_\mathbb C)$ is a semi-rigid monoidal category. Consider the unit morphism $u:\operatorname{Vect}_\mathbb C\to A$ and its transpose $$\xymatrix{ 
\tau:=u^{tr}:A\ar[r]^-{R} & A' \ar[r]^-{u'} & \operatorname{Vect}_\mathbb C' \ar[r]^-{R^{-1}} & \operatorname{Vect}_\mathbb C
    }$$

If $a\in A$ is compact, then we have $$\tau(a) \simeq \mathop{\mathrm{Hom}}_A(1_A, a)$$ and in general $\tau$ is the continuous extension of this assignment (which will agree with the Hom functional if and only if $A$ is rigid).

Given compact objects $a, b \in A$, we have canonical identifications $$\tau(a \star b)=
 \mathop{\mathrm{Hom}}_A(1_A, a\star b)
\simeq    \mathop{\mathrm{Hom}}_A((b^\vee)^\vee, a)
 = \tau((b^\vee)^\vee \star a)$$

It follows that a pivotal structure on $A$, i.e., a monoidal identification $RR\simeq {\rm id}$, gives rise to a trace structure on the functional $\tau$, i.e., a functorial identification $\tau(a\star b)\simeq \tau(b\star a)$ plus higher compatibilities. More precisely, a pivotal structure gives rise to a factorization $$\xymatrix{A\ar[r]^-{\mathfrak{tr}} \ar[dr]_-{\tau} & \operatorname{Tr}(A) \ar[d]\\ & \mathcal S}$$ and is in fact equivalent to such a factorization.
:::

### Adjoints are transposes

We may now identify the two coalgebras $(A,\mu^r)$ and $(A',\mu^t)$ obtained from a semi-rigid monoidal category:

::: prop
Let $A \in  Alg(St_\mathbb C)$ be a semi-rigid monoidal category.

There is a canonical equivalence of comonoidal categories $(A,\mu^r)\simeq (A',\mu^t)$ given on the level of objects by taking right duals, i.e., by the equivalence $R:A\to A'$.

In particular, for an $A$-module $M$ with action map $a_M:A\otimes M\to M$, the right adjoint $a_M^r:M\to A\otimes M$ and the transpose $a_M^t: M\to A'\otimes M$ are related by the duality $R$ in the sense that the following diagram canonically commutes: $$\xymatrix{ M \ar[dr]_-{a_M^r} \ar[r]^-{a_M^t} & A' \otimes M \ar[d]^-{R\otimes{\rm id}}\\
& A\otimes M}$$
:::

::: proof
*Proof.* The first assertion follows from the identifications $$\mathop{\mathrm{Comod}}_{A^r}(St_\mathbb C)\simeq \mathop{\mathrm{Mod}}_A(St_\mathbb C) \simeq \mathop{\mathrm{Comod}}_{A'}(St_\mathbb C)$$ of categories comonadic over $St_\mathbb C$, whence the coalgebras $A^r$ and $A'$ representing the corresponding comonads are naturally identified.

To verify that the identification is given by right duals, let us check by hand the second part of the proposition. Note that the action $a_M$ is quasi-proper by Lemma [\[quasiproper action\]](#quasiproper action){reference-type="ref" reference="quasiproper action"}. Since $A$ generates the category of $A$-modules by colimits, it suffices to establish the claim in the universal case $M=A$, where $a=a_A$ is the left action of $A$ on itself. Thus we have to identify the map $$\xymatrix{\mu^r:A\ar[r] &A\otimes A
}$$ with the map $$\xymatrix{A\ar[r]^-{a^t} & A'\otimes A \ar[r]^{R\otimes{\rm id}} & A\otimes A.}$$ Both are maps of right $A$-modules, hence it suffices to identify the images of the unit $$\xymatrix{
\eta_A:\operatorname{Vect}_\mathbb C\ar[r] & A\ar[r] & A\otimes A
}$$ under the two maps. For the first, it is characterized on compact objects by $$\begin{aligned}
\mathop{\mathrm{Hom}}_A(m\otimes n, \mu^r(1_A))&\simeq& \mathop{\mathrm{Hom}}_A(m\star n, 1_A)\\
&\simeq& \mathop{\mathrm{Hom}}_A(m, n^\vee)
\end{aligned}$$ For the second, the composition $$\xymatrix{\operatorname{Vect}_\mathbb C\ar[r]& A\ar[r]& A'\otimes A\ar[r] & A\otimes A}$$ sends the unit to $(R\otimes{\rm id})([\mathop{\mathrm{Hom}}])\in A\otimes A$, which is characterized on compact objects by $$\begin{aligned}
\mathop{\mathrm{Hom}}_{A\otimes A}(m\otimes n, (R\otimes{\rm id})([\mathop{\mathrm{Hom}}])) &\simeq& \mathop{\mathrm{Hom}}_A({}^\vee m, n)\\
 &\simeq & \mathop{\mathrm{Hom}}_A(m, n^\vee)
\end{aligned}$$ ◻
:::
