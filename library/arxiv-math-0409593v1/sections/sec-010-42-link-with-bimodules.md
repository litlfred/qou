---
doc_id: arxiv-math-0409593v1
doc_title: "Categorification of sl_2 and braid groups"
section_id: sec-010-42-link-with-bimodules
section_title: "Link with bimodules"
section_number: 4.2
pages: 12-13
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.974
doc_brief: "Categorification of sl_2 and braid groups — 20 sections: Front matter; Introduction; Self-equivalences"
---
[]{#appli label="appli"}

### 

We start by recalling results of Soergel [@Soe1; @Soe2; @Soe3] relating the category ${\mathcal{O}}$ to modules over the coinvariant algebra.

Let $\Lambda\in{\mathfrak{h}}^*/P$. We denote by $C_\Lambda=A/(A\cdot A_+^{W_\Lambda})$ the coinvariant algebra of $(W_\Lambda,S_\Lambda)$ and $p_\Lambda:A\to C_\Lambda$ the canonical surjection. Let $\lambda\in \Lambda^+$. We denote by $t_\lambda:A\to A$ the translation by $\lambda$, given by $f\mapsto (z\mapsto f(z+\lambda))$ We have Soergel's Endomorphismensatz [@Soe1 Endomorphismensatz 7] :

::: thm
The image of the composite morphism $Z\buildrel h\over \longrightarrow A^{\dot{W}}\hookrightarrow
A\buildrel t_\lambda\over \longrightarrow A\xrightarrow{p_\Lambda} C_\Lambda$ is $C^{W_\lambda}_\Lambda$ and the canonical morphism $Z\to \operatorname{End}\nolimits(P(w_0\cdot\lambda))$ factors through this morphism $Z\to C^{W_\lambda}_\Lambda$. The induced morphism $\sigma_\lambda:C^{W_\lambda}_\Lambda\buildrel \sim\over\to\operatorname{End}\nolimits(P(w_0\cdot\lambda))$ is an isomorphism.
:::

Let us now recall Soergel's Struktursatz [@Soe1 Struktursatz 9] :

::: thm
[]{#struktursatz label="struktursatz"} The functor $\operatorname{Hom}\nolimits(P(w_0\cdot\lambda),-):{\mathcal{O}}_\lambda\operatorname{\!-proj}\nolimits\to C^{W_\lambda}_\Lambda\operatorname{\!-mod}\nolimits$ is fully faithful.
:::

Let $\mu\in\Lambda$ be regular (*i.e.*, with trivial stabilizer in $W_\Lambda$).

There is an isomorphism $\phi:T_\lambda^\mu P(w_0\cdot\lambda)\buildrel \sim\over\to
P(w_0\cdot\mu)$. Any such isomorphism $\phi$ induces a commutative diagram [@Soe1 Bemerkung p.431] $$\xymatrix{
C^{W_\lambda}_\Lambda\ar[d]_{\sigma_\lambda}\ar[r]^{\text{inclusion}} &
 C_\Lambda\ar[d]^{\sigma_\mu}  \\
\operatorname{End}\nolimits(P(w_0\cdot\lambda))\ar[r]^{\phi_*T_\lambda^0} & \operatorname{End}\nolimits(P(w_0\cdot\mu))
}$$

This gives us an isomorphism, via the adjunction $(T_\lambda^\mu,T^\lambda_\mu)$ : $$\operatorname{Res}\nolimits_{C^{W_\lambda}_\Lambda}^{C_\Lambda} \operatorname{Hom}\nolimits(P(w_0\cdot\mu),?)\buildrel \sim\over\to
\operatorname{Hom}\nolimits(T_\lambda^\mu P(w_0\cdot\lambda),?)\buildrel \sim\over\to
\operatorname{Hom}\nolimits(P(w_0\cdot\lambda),T^\lambda_\mu(?))$$ between functors ${\mathcal{O}}_\mu\to C^{W_\lambda}_\Lambda\operatorname{\!-mod}\nolimits$. So, we have a commutative diagram, with fully faithful horizontal functors $$\xymatrix{
{\mathcal{O}}_\mu\operatorname{\!-proj}\nolimits\ar[d]_{T^\lambda_\mu} \ar[rrr]^-{\operatorname{Hom}\nolimits(P(w_0\cdot\mu),?)} &&&
 C_\Lambda\operatorname{\!-mod}\nolimits\ar[d]^{\operatorname{Res}\nolimits} \\
{\mathcal{O}}_\lambda\operatorname{\!-proj}\nolimits\ar[rrr]^-{\operatorname{Hom}\nolimits(P(w_0\cdot\lambda),?)} &&& C^{W_\lambda}_\Lambda\operatorname{\!-mod}\nolimits
}$$

### 

From the last commutative diagram, we deduce

::: prop
There is a commutative diagram with fully faithful horizontal arrows $$\xymatrix{
K^b({\mathcal{O}}_0\operatorname{\!-proj}\nolimits) \ar[rrr]^-{\operatorname{Hom}\nolimits(P(w_0),-)} \ar[d]_{F_s} &&&
  K^b(C\operatorname{\!-mod}\nolimits) \ar[d]^{F_s} \\
K^b({\mathcal{O}}_0\operatorname{\!-proj}\nolimits) \ar[rrr]^-{\operatorname{Hom}\nolimits(P(w_0),-)} &&& K^b(C\operatorname{\!-mod}\nolimits)
}$$
:::

So, we deduce from Theorem [\[actionbimod\]](#actionbimod){reference-type="ref" reference="actionbimod"} the following : given $v\in B_W$ and $v=t_1\cdots t_m=u_1\cdots u_n$ two decompositions in elements of ${\mathbf{S}}\cup{\mathbf{S}}^{-1}$, there is an isomorphism $F_{t_1}\cdots F_{t_m}\buildrel \sim\over\to F_{u_1}\cdots F_{u_n}$ between functors on $D^b({\mathcal{O}}_0)$ coming by restriction from the isomorphism between functors on $K^b(A\operatorname{\!-modgr}\nolimits)$. These form a transitive system of isomorphisms, *i.e.*

::: thm
The functors $F_s$ induce an action of $B_W$ on $D^b({\mathcal{O}}_0)$.
:::

More precisely,

::: thm
There is a monoidal functor from ${\mathcal{B}}_W$ to the category of self-equivalences of $D^b({\mathcal{O}}_0)$ sending $G_s$ to $F_s$.
:::

::: rem
One has a similar statement for the deformed category ${\mathcal{O}}$.

Note that we deduce from §[\[coinvariant\]](#coinvariant){reference-type="ref" reference="coinvariant"} that there is also a right action of $B_W$ on $D^b({\mathcal{O}}_0)$. We leave it to the reader to check that this corresponds to the actions using Zuckerman functors, or equivalently, Arkhipov functors.

In the graded setting (mixed perverse sheaves for example), the left and right actions of $B_W$ should be swapped by the self-Koszul duality equivalence, cf [@BerFreKhov] (and [@BeiGi Conjecture 5.18] for an analog in the equivariant case).

Various constructions have been given of weak actions of braid groups on $D^b({\mathcal{O}}_0)$, cf [@AnStr; @Ar; @KhomMaz; @MazStr; @Str].
:::
