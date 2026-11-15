---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-010-6-quantum-cocycle-invariants-via-maximaminima
section_title: "Quantum cocycle invariants via maxima/minima"
section_number: 6
pages: 19-21
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.953
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
[]{#sec:cupcap label="sec:cupcap"}

In this section we describe a construction of quantum cocycle invariants by deforming maxima and minima for knot diagrams with a height function specified. Throughout this section, a height function is fixed on the plane where knot diagrams lie, and diagrams are in general position, so that they have isolated maxima, minima, and double crossings. Diagrams are unoriented.

Let $R$ be a YBO on $V$. Let $\tilde R = \phi_0 + \hbar \phi_1$, where $\phi_0 := R$ and $\phi_1 := \phi$, be a deformed YBO. Denote by $\tilde R^{-1} = \hat \phi_0 + \hbar \hat \phi_1$ as before. Let $\tilde \cup = \cup_0 + \hbar \cup_1$, where $\cup_0 := \cup$ and $\cup_1: V \otimes V \rightarrow V$ is a pairing. Similarly let $\tilde \cap = \cap_0 + \hbar \cap_1$, where $\cup_0 := \cap$ and $\cap_1:  V  \rightarrow V \otimes V$ is a copairing. Suppose that $\cup$ and $\cap$ satisfy the switchback, passcup, and passcap properties. Below we use the notation $\Gamma=\Gamma_1^2$ from Definition [\[def:gamma\]](#def:gamma){reference-type="ref" reference="def:gamma"}.

::: theorem
[]{#thm:cupcap label="thm:cupcap"} The deformed YBO $\tilde R$, pairing $\tilde \cup$ and copairing $\tilde \cap$ on $\tilde V =  \mathbb k[[\hbar]]/(\hbar^2) \otimes V$ satisfy the switchback, passcup, and passcap properties if and only if the following equations hold. $$\begin{aligned}
\sum_{(i,j) \in \Gamma} (\cup_i \otimes {\mathbb 1}) ( {\mathbb 1} \otimes \cap_j) 
&=&  {\mathbb 1} \label{switch1} \\
\sum_{(i,j) \in \Gamma} ( {\mathbb 1} \otimes \cup_i)  (\cap_j \otimes {\mathbb 1}) 
&=&  {\mathbb 1} \label{switch2} \\
\sum_{(i,j) \in \Gamma} ( {\mathbb 1} \otimes \cup_i) (\phi_j \otimes  {\mathbb 1} )
&=& \sum_{(i,j) \in \Gamma} (\cup_i \otimes {\mathbb 1}) ( {\mathbb 1} \otimes \hat \phi_j ) \label{passcup1} \\
\sum_{(i,j) \in \Gamma} ( {\mathbb 1} \otimes \cup_i) ( \hat \phi_j \otimes  {\mathbb 1} )
&=& \sum_{(i,j) \in \Gamma} (\cup_i \otimes {\mathbb 1}) ( {\mathbb 1} \otimes  \phi_j ) \label{passcup2} \\
\sum_{(i,j) \in \Gamma} (\phi_i \otimes {\mathbb 1} ) ( {\mathbb 1} \otimes \cap_j) 
&=& \sum_{(i,j) \in \Gamma}( {\mathbb 1} \otimes \hat \phi_i) (\cap_j \otimes {\mathbb 1} )  \label{passcap1} \\
\sum_{(i,j) \in \Gamma} (\hat \phi_i \otimes {\mathbb 1} ) ( {\mathbb 1} \otimes \cap_j) 
&=& \sum_{(i,j) \in \Gamma}( {\mathbb 1} \otimes  \phi_i) (\cap_j \otimes {\mathbb 1} )  \label{passcap2}
\end{aligned}$$

Moreover, if $\tilde \phi$, $\tilde \cup$ and $\tilde \cap$ satisfy the switchback, passcup and passcap identities, then they define a knot invariant $$\Phi^{\rm M}_{(\tilde R, \tilde \cup, \tilde \cap)}(K) = \Phi^{{\rm M} 0}_{(\tilde R, \tilde \cup, \tilde \cap)}(K) + \Phi^{{\rm M} 1}_{(\tilde R, \tilde \cup, \tilde \cap)}(K)$$ up to regular isotopy (equivalence without type I Reidemeister moves).

If in addition $$\sum_{(i,j) \in \Gamma}\cup_j  \phi_i =  \cup_1, \quad  \sum_{(i,j) \in \Gamma} \phi_j \cap_i =  \cap_1$$ are satisfied, it provides a knot invariant up to isotopy.
:::

::: proof
*Proof.* The YBO $\hat \phi$ on $\tilde V \otimes \tilde V$, where $\tilde V = V\otimes \mathbb k[[\hbar]]//(\hbar^2)$, together with $\tilde \cup$ and $\tilde \cap$ satisfy the switchback, passcup, and passcap properties if they satisfy the corresponding conditions on infinitesimal part (degree one part with respect top $\hbar$), which are computed in Equations ([\[switch1\]](#switch1){reference-type="ref" reference="switch1"}) through ([\[passcap2\]](#passcap2){reference-type="ref" reference="passcap2"}). Then the composition corresponding to a given knot diagram with a height function defines a knot invariant up to regular isotopy with these operators. For isotopy, the condition for type I move translates to the stated condition on the degree one term of $\hbar$. ◻
:::

<figure id="swd1">
<div class="center">
<img src="swd1" style="width:3.5in" />
</div>
<figcaption></figcaption>
</figure>

For the rest of the section, we show that the cobounded cocycles give trivial infinitesimal part, in parallel to Lemma [\[lem:cob_EYBO\]](#lem:cob_EYBO){reference-type="ref" reference="lem:cob_EYBO"} and Proposition [\[prop:cob\]](#prop:cob){reference-type="ref" reference="prop:cob"}.

::: lemma
[]{#lem:cupcapcob label="lem:cupcapcob"} Let $\phi=\delta^1(f)$ be a cobounded YB 2-cocycle and $\tilde R=R + \hat \phi$ be the deformed YBO on $\tilde V$.

Let $\tilde \cup = \cup + \hbar \bar \cup$ and $\tilde \cap = \cap  + \hbar \bar \cap$ be a deformed pairing and copairing on $\tilde V$, respectively, where $$\bar \cup := \cup (f \otimes \mathbb 1 + \mathbb 1 \otimes f ) \quad 
{\rm and } \quad \bar \cap :=  (- f \otimes \mathbb 1 - \mathbb 1 \otimes f) \cap$$ as represented by diagrams in Figure [1](#swd1){reference-type="ref" reference="swd1"} left and right. Then $(\tilde R, \tilde \cup, \tilde \cap)$ satisfy the conditions in Theorem [\[thm:cupcap\]](#thm:cupcap){reference-type="ref" reference="thm:cupcap"}.
:::

::: proof
*Proof.* The switchback property Equation [\[switch2\]](#switch2){reference-type="eqref" reference="switch2"} is checked directly as diagrammatically represented in Figure [2](#swd2){reference-type="ref" reference="swd2"}. Equation [\[switch1\]](#switch1){reference-type="eqref" reference="switch1"} is similarly checked by their mirror diagrams.

A direct computation as in the proof of Lemma [\[lem:cob_EYBO\]](#lem:cob_EYBO){reference-type="ref" reference="lem:cob_EYBO"} shows that $\tilde R^{-1} = R^{-1} + \hbar \hat \phi$, where $\hat \phi = \delta^1_{R^{-1}}(f)$ is the image of the first YB coboundary of the inverse YBO $R^{-1}$. A direct computation for the terms of degree $1$ in $\hbar$ for the passcap and passcup moves using $\tilde R$ and $\tilde R^{-1}$ shows that the equations hold. A part of a passcap move is depicted in Figure [3](#cancelcap){reference-type="ref" reference="cancelcap"}. In the figure, one of the terms $R(\mathbb 1 \otimes f)$ of the coboundary from $\phi$ is depicted as a circle in the middle edge of the right-hand side, and another term $-(f \otimes \mathbb 1 )\cap$ from $\bar \cap$ is depicted as another circle on the same edge, and seen to cancel. The other terms involving $f$ are assigned on the end edges. The passcap equality of $R$ and $\cap$ imply the corresponding equality for $\tilde R$ and $\tilde \cap$. ◻
:::

<figure id="swd2">
<div class="center">
<img src="swd2" style="width:3.5in" />
</div>
<figcaption></figcaption>
</figure>

By Theorem [\[thm:cupcap\]](#thm:cupcap){reference-type="ref" reference="thm:cupcap"}, the deformed YBO and (co)pairings $(\tilde R, \tilde \cup, \tilde \cap)$ of Lemma [\[lem:cupcapcob\]](#lem:cupcapcob){reference-type="ref" reference="lem:cupcapcob"} defines a regular isotopy invariant $\Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M} =\Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M 0} + \hbar \Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M1}$.

<figure id="cancelcap">
<div class="center">
<img src="cancelcap" style="width:3.5in" />
</div>
<figcaption></figcaption>
</figure>

::: proposition
[]{#prop:cupcapcob label="prop:cupcapcob"} The infinitesimal part of the invariant $\Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M1}$ is trivial for a cobounded YB 2-cocycle $\phi=\delta^1(f)$. In other words, it holds that $\Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M} =\Phi_{(\tilde R, \tilde \cup, \tilde \cap)}^{\rm M 0}$.
:::

::: proof
*Proof.* This is proved in a manner similar to Proposition [\[prop:cob\]](#prop:cob){reference-type="ref" reference="prop:cob"}. There are three types of arcs in a given diagram in this case: (1) internal edge bounded by crossings, (2) edges with one end point on a crossing, other on an extremum, and (3) both ends on extrema. For the internal edge (1), cancelation happens as in Figure [\[cancel\]](#cancel){reference-type="ref" reference="cancel"}. Edges of case (2) happens where diagrams are as in passcup or passcap moves, and cancelation happens as in Figure [3](#cancelcap){reference-type="ref" reference="cancelcap"}. Case (3) happens as in figures of the switchback move, and cancelations happen as in Figure [2](#swd2){reference-type="ref" reference="swd2"}. Hence the same argument as in Proposition [\[prop:cob\]](#prop:cob){reference-type="ref" reference="prop:cob"} applies. ◻
:::
