---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-020-024-existence-of-the-haar-integral
section_title: "Existence of the Haar integral"
section_number: 0.24
pages: 28-31
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.964
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
Given a dual bases $\{f_i\}$ and $\{\xi^i\}$ of $H$ and $\widehat H$, respectively, let us consider the following canonical element $$\chi =\sum_i(\xi^i\leftharpoonup S^{-2}(f_i)).$$ One can show that $\chi$ is a left integral in $\widehat H$ such that $\chi(xy)=\chi(yS^2(x))$ for all $x,y\in H$ and $l\rightharpoonup\chi={\widehat S}^2(\widehat 1\leftharpoonup l)$ for any left integral $l$ in $H$ (see [@BNSz], 3.25).

::: lemma
[]{#Haar label="Haar"}

1.  The Haar integral $h\in H$ exists iff the above mentioned $\chi$ is non-degenerate, in which case $(h,\chi)$ is a dual pair of left integrals.

2.  A left integral $l$ is a Haar integral iff $\varepsilon_s(l)=1$.
:::

::: proof
*Proof.* (ii) If $\varepsilon_s(l)=1$, then by $l\rightharpoonup\chi={\widehat S}^2(\widehat 1\leftharpoonup l)$ one has $l\rightharpoonup\chi=\widehat 1$. Therefore, $(h,\chi)$ is a dual pair of non-degenerate left integrals. The property $\chi(xy)=\chi(yS^2(x))$ is equivalent to that the quasi-basis of $\chi$ satisfies $$l_{(2)}\otimes S^{-1}(l_{(1)})=S(l_{(1)})\otimes l_{(2)},$$ from where $\Delta(l)=\Delta(S(l))$ and $l=S(l)$. Furthermore, $\varepsilon_t(l)=
\varepsilon_t(S(l))=S\cdot \varepsilon_s(l)=1$. Thus, $l$ is a Haar integral. The inverse statement is obvious. (i) The \"only if\" part follows from the proof of (ii). If $\chi$ is non-degenerate and $h$ is its dual left integral, then, as above, $S(h)=h$; so $h$ is a two-sided integral and since $l\rightharpoonup\chi={\widehat S}^2(\widehat 1\leftharpoonup l)$, it is normalized. ◻
:::

::: theorem
[]{#Haar theorem label="Haar theorem"} Let $H$ be a finite quantum groupoid over an algebraically closed field $k$. Then the following conditions are equivalent:

1.  There exists a Haar integral,

2.  $H$ is semisimple and there exists an invertible element $g\in H$ such that $gxg^{-1}=S^2(x)$ for all $x\in H$ and $Tr(\pi_\alpha(g^{-1}))\neq 0$ for all irreducible representations $\pi_\alpha$ of $H$ (here $Tr$ is the usual trace on a matrix algebra).
:::

::: proof
*Proof.* The assumption on $k$ is used only to ensure that $H=\oplus_\alpha M_{n_\alpha}(k)$, once knowing that it is semisimple, so that there is a $k$-basis of matrix units $\{e^{\alpha}_{ij}\}$ in $H$.

(ii)$\implies$(i): Recall that any trace $\tau$ on $H$ is completely determined by its *trace vector* $\tau_\alpha =\tau(1_\alpha)$. Now let $\tau:H\to k$ be the trace with trace vector $\tau_\alpha=
\mbox{tr}\pi_\alpha(g^{-1})$. Then $\tau$ is non-degenerate and has a quasi-basis $$\sum_i x_i\otimes y_i=\sum_\alpha{\frac{1}{\tau_\alpha}}\sum^{n_\alpha}_{i,j=1}
e^{\alpha}_{ij}\otimes e^{\alpha}_{ji}.$$ Notice that $\sum_i x_ig^{-1}y_i=1$. It is straightforward to verify that $\chi'=g\rightharpoonup\tau$ coincides with $\chi$, so $\chi$ is non-degenerate and therefore its dual left integral $l$ has $\varepsilon_s(l)=1$ by $l\rightharpoonup\chi={\widehat S}^2(\widehat 1\leftharpoonup l)$. Thus, $l$ is a Haar integral.

(i)$\implies$(ii): If $h$ is a Haar integral, then $H$ is semisimple by Theorem [\[maschke\]](#maschke){reference-type="ref" reference="maschke"}. Let $\tau$ be a non-degenerate trace on $H$, then there exists a unique $i\in H$ such that $i\rightharpoonup\tau=\widehat 1=\tau\leftharpoonup i$. One can verify that $i$ is a two-sided non-degenerate integral in $H$ and that $S(i)=i$ (see [@BNSz], I.3.21). To prove that $S^2$ is inner, it is enough to construct a non-degenerate functional $\chi$ on $H$ such that $\chi(xy)=\chi(yS^2(x))$ for all $x,y\in H$. But the proof of Lemma [\[Haar\]](#Haar){reference-type="ref" reference="Haar"} shows that this is the case for the dual left integral to $i$. ◻
:::

::: remark
[]{#C*-semisimple label="C*-semisimple"}

1.  There is a unique normalization of $g$ from Theorem [\[Haar theorem\]](#Haar theorem){reference-type="ref" reference="Haar theorem"}(ii) such that the following conditions hold ([@BNSz], 4.4) :

    1.  $\mbox{tr}(\pi_\alpha(g^{-1}))=\mbox{tr}(\pi_\alpha(g))$ for all irreducible representations $\pi_\alpha$ of $H$ (here $\mbox{tr}$ is a usual trace on a matrix algebra);

    2.  $S(g)=g^{-1}$.

    One can show that such a $g$ is *group-like*, i.e., $$\Delta(g) =(g\otimes g)\Delta(1) = \Delta(1) (g\otimes g).$$ The element $g$ implementing $S^2$ and satisfying normalization conditions (i) and (ii) is called the *canonical group-like element* of $H$.

2.  Since $\chi = g\rightharpoonup\tau$ is the dual left integral to $h$, its quasi-basis $\sum_i x_ig^{-1}\otimes y_i$ equals to $h_{(2)}\otimes S^{-1}(h_{(1)})$, which implies the formula $$(S\otimes id)\Delta(h)=\sum_i x_i\otimes g^{-1}y_i=\sum_\alpha 1/\tau_\alpha
    \sum_{ij}e^\alpha_{ij}g^{-1/2}\otimes g^{-1/2}e^\alpha_{ji}.$$
:::

A dual notion to that of the Haar integral is the Haar measure. Namely, a functional $\phi \in \widehat H$ is said to be a *Haar measure* on $H$ if it is a normalized left and right invariant measure and $\phi\circ S=\phi$. Any of the equivalent conditions of Theorem [\[Haar\]](#Haar){reference-type="ref" reference="Haar"} is also equivalent to existence (and uniqueness) of the Haar measure.

## $C^*$-quantum groupoids

Definition [\[semisimple and C\*\]](#semisimple and C*){reference-type="ref" reference="semisimple and C*"} and the uniqueness of the unit, counit and the antipode (see Proposition [\[properties of S\]](#properties of S){reference-type="ref" reference="properties of S"}) imply that $$1^*=1,\quad \varepsilon(x^*)= \overline{\varepsilon(x)},\quad (S\circ *)^2 =\mbox{id}$$ for all $x$ in any $*$-quantum groupoid. It is also easy to check the relations $$\varepsilon_t(x)^*=\varepsilon_t(S(x)^*),\qquad \varepsilon_t(x)^*=\varepsilon_t(S(x)^*),$$ therefore, $H_t$ and $H_s$ are $*$-subalgebras, and to show that the dual, $\widehat H$, is also a $*$-quantum groupoid with respect to the $*$-operation $$\langle\,\phi^*,x\,\rangle=\overline{\langle\,\phi,S(x)^*\,\rangle}\qquad \mbox{ for all } 
\phi\in \widehat H,\ x\in H.$$

The $*$-operation allows to simplify the axioms of a quantum groupoid (cf. the axioms used in [@NV1], [@N1]). The second parts of equalities ([\[eps m\]](#eps m){reference-type="ref" reference="eps m"}) and ([\[Delta 1\]](#Delta 1){reference-type="ref" reference="Delta 1"}) of Definition [\[finite quantum groupoid\]](#finite quantum groupoid){reference-type="ref" reference="finite quantum groupoid"} follow from the rest of the axioms, also $S*\mbox{id}= \varepsilon_s$ is equivalent to $\mbox{id}* S=\varepsilon_t$. Alternatively, under the condition that the antipode is both algebra and coalgebra anti-homomorphism, the axioms ([\[eps m\]](#eps m){reference-type="ref" reference="eps m"}) and ([\[Delta 1\]](#Delta 1){reference-type="ref" reference="Delta 1"}) can be replaced by the identities of Proposition [\[counital properties\]](#counital properties){reference-type="ref" reference="counital properties"} (ii) and (v) involving the target counital map.

::: theorem
([@BNSz], 4.5) []{#C*-Haar label="C*-Haar"} In a $C^*$-quantum groupoid the Haar integral $h$ exists, $h=h^*$ and $$(\phi,\psi)=\langle\,\phi^*\psi,h\,\rangle,\qquad \phi,\psi\in \widehat H$$ is a scalar product making $\widehat H$ a Hilbert space where the left regular representation of $\widehat H$ is faithful. Thus, $\widehat H$ is a $C^*$-quantum groupoid, too.
:::

::: proof
*Proof.* Clearly, $H$ and $g$ verify all the conditions of Theorem [\[Haar theorem\]](#Haar theorem){reference-type="ref" reference="Haar theorem"}, from where the existence of Haar integral follows. Since $h$ is non-degenerate, the scalar product $(\cdot,\cdot)$ is also non-degenerate. By the equality $$(\phi,\phi)=\langle\,\phi^*\phi,h\,\rangle=\overline{\langle\,\phi,S(h_{(1)})^*\,\rangle}\langle\,\phi,h_{(2)}\,\rangle,$$ positivity of $(\cdot,\cdot)$ follows from Remark [\[C\*-semisimple\]](#C*-semisimple){reference-type="ref" reference="C*-semisimple"}(b). ◻
:::

We will denote by $\widehat h$ the Haar measure of $\widehat H$.

::: remark
[]{#eps is positive label="eps is positive"} $\varepsilon$ is a positive functional, i.e., $\varepsilon(x^*x) \geq 0$ for all $x\in H$. Indeed, for all $x\in H$ we have $$\varepsilon(x^*x)
= \varepsilon(x^*1_{(1)})\varepsilon(1_{(2)} 1'_{(2)})\varepsilon(1'_{(1)} x)=\varepsilon(\varepsilon_t(x)^* \varepsilon_t(x))
= \langle\,\widehat h,\varepsilon_t(x)^*\varepsilon_t(x)\,\rangle\geq 0,$$ where $\widehat h\vert_{H_t}=\varepsilon\vert_{H_t}$, since $\langle\,\widehat h,z\,\rangle=\langle\,\widehat\varepsilon_t(\widehat h),z\,\rangle=\langle\,\widehat 1,z\,\rangle$ for all $z\in H_t$.
:::

The Haar measure provides target and source *Haar conditional expectations* (all properties are easy to verify): $$\begin{aligned}
E_t &:& H\to H_t :  E_t(x)=(id\otimes\widehat h)\Delta(x), \\
E_s &:& H\to H_s :  E_s(x)=(\widehat h\otimes id)\Delta(x).
\end{aligned}$$ Let us introduce an element $g_t=E_t(h)^{1/2}\in H_t$.

::: remark
[]{#group-like label="group-like"}([@BNSz], 4.12). $g_t$ is positive and invertible, and the canonical group-like element of $H$ can be written as $g=g_tS(g_t^{-1})$.
:::

One can check that for a quasitriangular $*$-quantum groupoid ${\bar {\mathcal R}}={\mathcal R}^*$.

::: proposition
[]{#*-double label="*-double"} If $H$ is a $C^*$-quantum groupoid, then $D(H)$ is a quasitriangular $C^*$-quantum groupoid.
:::

::: proof
*Proof.* The result follows from the fact that $\widehat{D(H)}$ is a $C^*$-quantum groupoid, which is easy to verify using the explicit formulas from Remark [\[dual double\]](#dual double){reference-type="ref" reference="dual double"}. ◻
:::

::: proposition
[]{#*-Ribbon WHA label="*-Ribbon WHA"} A quasitriangular $C^*$-quantum groupoid $H$ is automatically ribbon with the ribbon element $\nu=u^{-1}g=gu^{-1}$, where $u$ is the Drinfeld element from Definition [\[Drinfeld element\]](#Drinfeld element){reference-type="ref" reference="Drinfeld element"} and $g$ is the canonical group-like element.
:::

::: proof
*Proof.* Since $u$ also implements $S^2$ (Proposition [\[elements u and v\]](#elements u and v){reference-type="ref" reference="elements u and v"}), $\nu=u^{-1}g$ is central, therefore $S(\nu)$ is also central. Clearly, $u$ must commute with $g$. The same Proposition gives $\Delta(u^{-1}) = {\mathcal R}_{21}{\mathcal R}(u^{-1}\otimes u^{-1})$, which allows us to compute $$\Delta(\nu) = \Delta(u^{-1})(g\otimes g) = 
{\mathcal R}_{21}{\mathcal R}(u^{-1}g\otimes u^{-1}g) = {\mathcal R}_{21}{\mathcal R}(\nu \otimes \nu).$$ Propositions [\[properties of R\]](#properties of R){reference-type="ref" reference="properties of R"} and [\[elements u and v\]](#elements u and v){reference-type="ref" reference="elements u and v"} and the trace property imply that $$\begin{aligned}
\mbox{tr}(\pi_\alpha(u^{-1})) 
&=& \mbox{tr}(\pi_\alpha( {\mathcal R}^{(2)}S^2({\mathcal R}^{(1)}) )) \\ 
&=& \mbox{tr}(\pi_\alpha(S^3({\mathcal R}^{(1)}) S({\mathcal R}^{(2)}) ) = \mbox{tr}(\pi_\alpha(S(u^{-1}))).
\end{aligned}$$ Since $u^{-1} = \nu g^{-1}$ and $\nu$ is central, the above relation means that $$\mbox{tr}(\pi_\alpha(\nu))\mbox{tr}(\pi_\alpha(g^{-1})) =
\mbox{tr}(\pi_\alpha(S(\nu)))\mbox{tr}(\pi_\alpha(g)),$$ and, therefore, $\mbox{tr}(\pi_\alpha(\nu)) = \mbox{tr}(\pi_\alpha(S(\nu)))$ for any irreducible representation $\pi_\alpha$, which shows that that $\nu = S(\nu)$ (cf. [@EG]). ◻
:::

::: remark
[]{#C*-q-trace label="C*-q-trace"} For a connected ribbon $C^*$-quantum groupoid we have: $$\mbox{tr}_q(f) = (\dim H_t)^{-1} \mbox{Tr}\,_V(g\circ f),\ \dim_q(V) = 
(\dim H_t)^{-1} \mbox{Tr}\,_V(g).$$ for any $f\in \mbox{End}(V)$, $V$ is an $H$-module.
:::
