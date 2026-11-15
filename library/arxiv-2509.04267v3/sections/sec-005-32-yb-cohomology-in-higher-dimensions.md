---
doc_id: arxiv-2509.04267v3
doc_title: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology"
section_id: sec-005-32-yb-cohomology-in-higher-dimensions
section_title: "YB cohomology in higher dimensions"
section_number: 3.2
pages: 6-8
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.936
doc_brief: "Quantum Cocycle Invariants of Knots from Yang-Baxter Cohomology — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
In this subsection we review definitions of YB cohomology theory from [@SZ-YBH], see also [@SZ-BC].

We set $\sigma_{n,i} = \mathbb 1^{\otimes (i-1)}\otimes R \otimes \mathbb 1^{\otimes(n-i-1)}$. Then, for $\phi \in {\rm Hom}(V^{\otimes n}, V^{\otimes n})$, the partial differentials for YB cohomology are defined as $$\begin{aligned}
    d_{{\rm YB},i}^n(\phi) &=& \sigma_{n+1,n+1-i}\cdots\sigma_{n+1,2}\sigma_{n+1,1}(\mathbb 1\otimes \phi)\sigma_{n+1,1}\cdots\sigma_{n+1,i-1}\sigma_{n+1,i}\\
    && - \sigma_{n+1,i+1}\cdots\sigma_{n+1,n}\sigma_{n+1,n+1}(\phi \otimes \mathbb 1)\sigma_{n+1,n+1}\cdots\sigma_{n+1,i+2}\sigma_{n+1,i+1}.
\end{aligned}$$ The partial differentials $d_{{\rm YB},i}^n$ are graphically depicted as in Figure [1](#fig:partial_YB){reference-type="ref" reference="fig:partial_YB"}.

<figure id="fig:partial_YB">
<div class="center">
<embed src="YBdiff.pdf" style="width:2.8in" />
</div>
<figcaption></figcaption>
</figure>

::: definition
[]{#def:YB_coh_def label="def:YB_coh_def"} We define the YB cohomology complex of $V$, with YBO $R$, as the cochain groups $C^n(V,V) := {\rm Hom}_{\mathbb k}(V^{\otimes n},V^{\otimes n})$ and differentials $\partial^n_{\rm YB} := \sum_{i=1}^n (-1)^id_{{\rm YB},i}^n$ as an alternating sum of partial differentials. The associated cohomology is called *Yang-Baxter cohomology* and denoted $H^n_{\rm YB}(V,R)$.
:::

::: lemma
[]{#lem:YB_complex label="lem:YB_complex"} The YB cohomology complex of Definition [\[def:YB_coh_def\]](#def:YB_coh_def){reference-type="ref" reference="def:YB_coh_def"} is indeed a cochain complex.
:::

To prove the result it is sufficient to show that whenever $i<j$ the equality $d_{{\rm YB},j}^{n+1}d_{{\rm YB},i}^n = d_{{\rm YB},i}^{n+1}d_{{\rm YB},j-1}^n$ holds. We include a diagrammatic argument in Figure [2](#fig:YBdjdi){reference-type="ref" reference="fig:YBdjdi"} to show this fact.

<figure id="fig:YBdjdi">
<div class="center">
<embed src="YBdjdi.pdf" style="width:5in" />
</div>
<figcaption></figcaption>
</figure>

A natural question to ask at this point is whether the two cohomology theories, from Definition [\[def:YB_coh_def\]](#def:YB_coh_def){reference-type="ref" reference="def:YB_coh_def"} and [@Eis], are related or not. In low degrees, it turns out that when $R$ is invertible (i.e. it is a YBO rather than being just a pre-YBO) the cohomology groups are isomorphic. In the following, we denote by $\hat H^n_{\rm YB}(V,R)$ the YB cohomology groups of [@Eis1; @Eis], and their differentials by $\hat d_{\rm YB}^n$. We recall the following definition, found in [@SZ-YBH].

::: definition
Let $R : V^{\otimes 2} \longrightarrow V^{\otimes 2}$ be a Yang-Baxter operator over the $\mathbb k$-module $V$. An operator $\tilde R: \tilde V^{\otimes 2} \longrightarrow \tilde V^{\otimes 2}$, where $\tilde V := \mathbb k[[\hbar]]/(\hbar^2)\otimes V$, is said to be a *Yang-Baxter deformation* of $R$, or YB deformation for short, if it satisfies $[R - \tilde R] (V^{\otimes 2}) \subset \hbar V^{\otimes 2}$. Two YB deformations $R_1$ and $R_2$ of $R$ are said to be equivalent if there exists a mapping $f: V \longrightarrow V$ such that $$\begin{aligned}
                        R_2 = R_1 ( f \otimes {\mathbb 1}) + R_1 ( {\mathbb 1} \otimes  f ) 
                        -  ( f \otimes {\mathbb 1}) R_1 - ( {\mathbb 1} \otimes  f )  R_1. 
                
\end{aligned}$$
:::

We observe that this definition coincides with the one found in [@Eis1], see Definition 5 therein, upon taking the ideal $\frak m = (\hbar)$. We lastly recall that in [@Eis; @Eis1] and [@SZ-YBH] it has been shown that the group of YB deformations is isomorphic to the respective second cohomology groups. See for instance Proposition 27 in [@Eis1], and Theorem 3.9 in [@SZ-YBH] where the proof is given for the more general Yang-Baxter-Hochschild cohomology.

::: proposition
Suppose that $R$ is a YBO. Then, we have $$\begin{aligned}
                H^1_{\rm YB}(V,R) &\cong& \hat H^1_{\rm YB}(V,R)\\
                H^2_{\rm YB}(V,R) &\cong& \hat H^2_{\rm YB}(V,R).
        
\end{aligned}$$
:::

::: proof
*Proof.* Applying $R$ to the differential $\hat d^1_{\rm YB}$ of [@Eis], we find the relation $\partial^1_{\rm YB}(f) = \hat d^1_{\rm YB}(f)R$, for any $1$-cochain $f$. Since $R$ is invertible, we find a 1-1 correspondence between $1$-cocycles of $\partial^1_{\rm YB}$ and $1$-cocycles of $\hat d^1_{\rm YB}$. Since $\partial^0_{\rm YB}$ and $\hat d^0_{\rm YB}$ are the same, this completes the proof of the first isomorphism. To show the second, we just use the fact that both cohomology groups are isomorphic to the group of YB infinitesimal deformations, as shown in [@Eis1] and [@SZ-YBH]. The groups of deformations of YBOs are the same between the two by taking $\frak m$ in [@Eis1] to be $(\hbar)$ in our notation. This completes the proof. ◻
:::

The relation between $H^n_{\rm YB}(V,R)$ and $\hat H^n_{\rm YB}(V,R)$ remains unclear for $n\geq 3$. This does not affect the current paper.
