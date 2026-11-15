---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-004-23-discrete-and-compact-case
section_title: "Discrete and Compact Case"
section_number: 2.3
pages: 9-11
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.952
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
The following proposition is well known and easy to prove.

::: prop
[]{#Berkeley label="Berkeley"} Let $I$ be a set and $H_i, i\in I$ finite dimensional Hilbert spaces. Consider the algebraic direct sum $$A=\bigoplus_{i\in I} \ B(H_i)$$

1.  $A$ is a $*$-algebra with the usual $*$-operation on $B(H_i)$.

2.  $A$ is unital iff $I$ is finite.

3.  The canonical embedding maps $\iota_i: B(H_i)\hookrightarrow A$ and projections $p_i: A\rightarrow B(H_i)$ are $*$-homomorphisms.

4.  Let $M(A)$ be the multiplier algebra and $L: A\rightarrow M(A)$ the canonical embedding map. There exists a unique isomorphism $$P: \ M(A)\rightarrow\prod_{i\in I} \ B(H_i)$$ such that $PL=\mathrm{id}$, where we use the obvious identification of the direct sum with a subalgebra of the direct product.

5.  If $\pi$ is an irreducible ($*$)-representation of $A$ there is $i\in I$ and an invertible (unitary) $U\in B(H,H_i)$ unique up to a scalar such that $$\pi(\cdot)=\pi\iota_i p_i(\cdot)=U p_i(\cdot) U^{-1}.$$

6.  Any ($*$-)representation of $A$ is a direct sum of irreducible ($*$-)representations.
:::

From now on the isomorphism $P$ will be used to make an identification $M(A)\equiv\prod_{i\in I} \ B(H_i)$ and therefore suppressed.

::: defin
[]{#def-comp-disc label="def-comp-disc"} A multiplier Hopf $*$-algebra $(A, \Delta)$ is called discrete if $A=\oplus_i B(H_i)$. An aqg is called discrete if it is discrete as a multiplier Hopf $*$-algebra.
:::

The proof of the following result is included, since it is instructive for our purposes.

::: thm
[]{#t-disc2 label="t-disc2"} Let $(A,\Delta)$ be a discrete multiplier Hopf $*$-algebra. Then there is a unique $f\in M(A)$ satisfying

1.  $f$ is positive and invertible,

2.  $\displaystyle S^2(a)=faf^{-1}\ \forall a\in A$,

3.  $\displaystyle Tr_i\, p_i(f)=Tr_i\, p_i(f^{-1})$, where $Tr_i$ is the usual trace on $B(H_i)$.

It also satisfies $\displaystyle S(f)=f^{-1}$ (where the unique extension of $S$ to $M(A)$ is understood).
:::

*Proof. *To simplify the formulae we introduce the antilinear map $\chi(a)=S(a^*)$ which satisfies $\chi^2=\mathrm{id}_A$. For every $i\in I$ we pick an antiunitary $J_i: H_i\rightarrow H_i$. Now, $J_i p_i(\cdot)J_i^{-1}$ is a (linear) irreducible representation of $A$ on $H_i$ for any $i\in I$. By Prop. [\[Berkeley\]](#Berkeley){reference-type="ref" reference="Berkeley"} there is a unique $c(i)\in I$ and an invertible $V_i: H_i\rightarrow H_{c(i)}$ such that $$\label{equ}
V_iJ_i \, p_i\chi(\cdot)J_i^{-1}V_i^{-1}= p_{c(i)}.$$ Now $U_i\equiv V_iJ_i$ is unique up to a scalar. We calculate $$U_ip_i(a)U_i^{-1}=U_ip_i(\chi\chi(a))U_i^{-1}=p_{c(i)}(\chi(a))=
   U_{c(i)}^{-1}p_{c(c(i))} U_{c(i)}.$$ In the first step we have used $\chi^2=\mathrm{id}$ and then we have used ([\[equ\]](#equ){reference-type="ref" reference="equ"}) twice. This shows that the irreducible representations $p_i$ and $p_{c(c(i))}$ are equivalent and therefore $c$ is involutive: $c(c(i))=i$. From now on we write $\overline{\imath}=c(i)$. We have $$U_{\overline{\imath}}U_ip_i(\cdot)U_i^{-1}U_{\overline{\imath}}=p_i(\cdot),$$ and by irreducibility $U_{\overline{\imath}}U_i=k_i 1\in B(H_i)$. Using the freedom (up to a scalar) in the choice of the $U_i$ we can assume that $k_i=1\ \forall i\in I$. (If $i=\overline{\imath}$ we can absorb $k_i$ in $U_i$. If $i\ne \overline{\imath}$, we can achieve $U_{\overline{\imath}}U_i=1$, and since the $U_i$ are invertible this implies that automatically $k_{\overline{\imath}}=1$.)

From ([\[equ\]](#equ){reference-type="ref" reference="equ"}) we obtain $p_iS(a)=U_i^{-1}p_{\overline{\imath}}(a^*)U_i$ and applying this twice yields $$p_i S^2(a) = U_i^{-1}p_{\overline{\imath}}S(a)^* U_i 
   = U_i^{-1}[U_{\overline{\imath}}^{-1}p_{\overline{{\overline{\imath}}}}(a^*)U_{\overline{\imath}}]^*U_i
   =  U_i^{-1}U_{\overline{\imath}}^* p_i(a)U_{\overline{\imath}}^{-1 *}U_i.$$ Thus $p_i S^2(a)=G_i p_i(a) G_i^{-1}$ with $G_i=U_i^{-1}U_{\overline{\imath}}^*=k_i^{-1}U_{\overline{\imath}}U_{\overline{\imath}}^*$ positive and invertible for all $i\in I$. Defining $$F_i=\sqrt{\frac{Tr_i\,G_i^{-1}}{Tr_i\,G_i}}\,G_i,$$ we have $$Tr_i\, F_i=\sqrt{Tr_i\,G_i^{-1}\,Tr_i\,G_i}=Tr_i\,F_i^{-1}$$ as required. Obviously, also the $F_i$ are positive and invertible and $p_iS^2(a)=F_ip_i(a)F_i^{-1}$. The uniqueness is obvious in view of the normalizations. It remains to prove $S(f)=f^{-1}$, which is clearly equivalent to $p_iS(f)=p_i(f^{-1})\ \forall i$. As above, with ([\[equ\]](#equ){reference-type="ref" reference="equ"}) we have $p_iS(f)=U_i^{-1}p_{\overline{\imath}}(f^*)U_i=U_i^{-1}F_{\overline{\imath}}^*U_i$. On the other hand, $p_i(f^{-1})=F_i^{-1}$. Thus we have to show $$U_i^{-1}F_{\overline{\imath}}^*U_i = F_i^{-1}\quad\forall i\in I.$$ Inserting the definition of the $F_i$ this is equivalent to $$U_i^{-1}\sqrt{\frac{Tr_{\overline{\imath}}\,G_{\overline{\imath}}^{-1}}{Tr_{\overline{\imath}}\,G_{\overline{\imath}}}}U_iU_{\overline{\imath}}^{-1*}U_i=
   \sqrt{\frac{Tr_i\,G_i}{Tr_i\,G_i^{-1}}} U_{\overline{\imath}}^{*-1}U_i\quad\forall i\in I.$$ This is clearly equivalent to $$Tr_{\overline{\imath}}\,G_{\overline{\imath}}^{-1}\ Tr_i\,G_i^{-1}=Tr_i\,G_i\ Tr_{\overline{\imath}}\, G_{\overline{\imath}}\quad\forall i\in I.$$ Plugging in $G_i=U_i^{-1}U_{\overline{\imath}}^*$ this is an easy computation which we omit. (One uses $U_{\overline{\imath}}=U_i^{-1}$ and cyclicity of the traces.)

::: thm
[]{#thm-haar label="thm-haar"} A discrete multiplier Hopf $*$-algebra $(A,\Delta)$ admits a non-zero left-invariant positive linear functional $\varphi$, thus is an aqg.
:::

::: prop
[]{#p-disc label="p-disc"} An aqg $(A,\Delta)$ is discrete iff there exists $h\in A$ such that $ah=\varepsilon(a) h$, for all $a\in A$.
:::

::: defin
An aqg $(A,\Delta)$ is called compact if $A$ is unital.
:::

Note that an aqg $(A,\Delta)$ is compact iff it is a Hopf $*$-algebra. Hence the analytical extension of a compact aqg is a compact quantum group in the sense of S.L. Woronowicz. A multiplier Hopf $*$-algebra $(A,\Delta)$ with $A$ unital is not necessarily an aqg, but this is the case whenever $A$ has a C\*-algebra envelope. It is easily seen that $(A,\Delta)$ is compact and discrete iff $A$ is finite dimensional.

::: thm
Let $(A,\Delta)$ be an aqg. Then $(A,\Delta)$ is compact iff $(\hat{A},\hat{\Delta})$ is discrete.
:::
