---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-001-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 6-9
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.983
---
[]{#sec:preliminaries label="sec:preliminaries"}

Before we present a mathematically-friendly summary of our proposal and the physics behind it, we need to introduce some notations, especially those relevant to abelian flat connections that will be central in our discussion.

Consider a closed and connected 3-manifold $M_3$, with $\partial M_3=\emptyset$. In order to present the results in full generality, it will be useful to consider the linking pairing on the torsion part of $H_1(M_3,{\mathbb Z})$: $$\begin{array}{cccc}
        {\ell k}: & {\mathrm{Tor}\,}H_1(M_3)\otimes {\mathrm{Tor}\,}H_1(M_3) & \longrightarrow & {\mathbb Q}/{\mathbb Z}\\
        & [a]\otimes [b] & \longmapsto & {\#(a\cap b')}/{n} \\
    \end{array}$$ where $b'$ is a 2-chain such that $\partial b'=nb$ for an integer $n$. Such $b'$ and $n$ exist because $[b]$ is torsion. As usual, $\#(a\cap b')$ denotes the number of intersection points counted with signs determined by the orientation. Note that the linking form provides an isomorphism between ${\mathrm{Tor}\,}H_1(M_3)$ and its Pontryagin dual $({\mathrm{Tor}\,}H_1(M_3))^*\equiv\mathrm{Hom}({\mathrm{Tor}\,}H_1(M_3),U(1))$ via the pairing $e^{2\pi i{\ell k}(\cdot,\cdot)}$.

The ${\mathbb Z}_2$ Weyl group acts on the elements $a\in{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ via $a\mapsto -a$. The set of orbits is the set of connected components of abelian flat $SU(2)$ connections on $M_3$ (*i.e.*, connections in the image of $\rho: {\mathcal M}_\text{flat}\left(M_3,U(1)\right)\rightarrow {\mathcal M}_\text{flat}\left(M_3,SU(2)\right)$ from the embedding $U(1)\subset SU(2)$),[^1] $${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2 \; \cong \; \pi_0{\mathcal M}_\text{flat}^\text{ab}(M_3,SU(2)) \,.$$ It is also useful to introduce a shorthand notation for the stabilizer subgroup: $${\mathcal W}_a \; \equiv \; \text{Stab}_{{\mathbb Z}_2}(a) \; = \; \left\{
    \begin{array}{cl}
        {\mathbb Z}_2, & a=-a \,, \\
        1, & \text{otherwise\,.}
    \end{array}
    \right.$$

## ${D^2\times S^1}$ partition function of ${T[M_3]}$ and WRT invariant {#sec:summaryConj}

Now we are ready to present a slightly generalized and improved version of the results from [@Gukov:2016gkn sec. 6].

### Categorification of WRT invaraiant

Let $Z_{SU(2)_k}[M_3]$ be the partition function of $SU(2)$ Chern-Simons theory with "bare" level $(k-2)$ on $M_3$, also known as the WRT invariant. We use the standard "physics" normalization where $$Z_{SU(2)_k}\left[S^2\times S^1\right]=1,$$ and $$Z_{SU(2)_k}\left[S^3\right]=\sqrt{\frac2k}\sin\left(\frac\pi k\right).$$ The following conjecture was proposed in [@Gukov:2016gkn].[^2]

::: conj
The WRT invariant can be decomposed into the following form: $$Z_{SU(2)_k}[M_3]=(i\sqrt{2k})^{b_1(M_3)-1}\sum_{a,b\;\in \;\atop{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}e^{2\pi ik{\ell k}(a,a)}\,S_{ab}
    \, \widehat{Z}_b(q)|_{q\rightarrow e^{\frac{2\pi i }{k}}}
    \label{WRT-decomposition}$$ with [^3][^4] $$\widehat{Z}_b(q) \in \, 2^{-c} q^{\Delta_b} {\mathbb Z}[[q]]\qquad \Delta_b\in {\mathbb Q},\qquad c\in{\mathbb Z}_+
    \label{Block-qSeries}$$ convergent in $|q|<1$ and $$S_{ab}=\frac{e^{4\pi i{\ell k}(a,b)}+e^{-4\pi i{\ell k}(a,b)}}{|{\mathcal W}_a|\sqrt{|{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})|}}.$$ []{#Conjecture1 label="Conjecture1"}
:::

In other words, we claim the existence of new 3-manifold invariants $\widehat{Z}_a$, which admit $q$-series expansion with integer powers and integer coefficients (hence, more suitable for categorification) and from which the WRT invariant can be reconstructed via [\[WRT-decomposition\]](#WRT-decomposition){reference-type="eqref" reference="WRT-decomposition"}. While the formal mathematical definition of the invariants $\widehat{Z}_a$ is waiting to be discovered, they admit a physics definition that will be reviewed below and can be independently computed via techniques of resurgent analysis. In particular, each term $$\sum_{b\in{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})}\left.e^{2\pi ik{\ell k}(a,a)}\,S_{ab}
        \, \widehat{Z}_b(q)\right|_{q\rightarrow e^{\frac{2\pi i }{k}}}
        \equiv
            e^{2\pi ik{\ell k}(a,a)}\,Z_a(q)
\label{WRT-ab-contrib}$$ in the sum ([\[WRT-decomposition\]](#WRT-decomposition){reference-type="ref" reference="WRT-decomposition"}) is a certain resummation of the perturbative (in $\frac{2\pi i}k$ or, equivalently, in $(1-q)$) expansions of the WRT invariant around the corresponding abelian flat connection $a$ [@Gukov:2016njj].

In order to avoid unnecessary technical complications, in the rest of this paper we assume that ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ has no ${\mathbb Z}_2$ factors.[^5] Under this assumption, the $S$-matrix satisfies $$\sum_{b}S_{ab}S_{bc}=\delta_{ac}.
\label{S-squared}$$

Moreover, as will be discussed in detail below, physics predicts the existence of a ${\mathbb Z}\times {\mathbb Z}\times {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2$ graded homological invariant of $M_3$: $${\mathcal H}_{D^2}[M_3] \; =\bigoplus_{a\in {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}{\mathcal H}_a[M_3],\qquad {\mathcal H}_a[M_3] \; =\bigoplus_{i\in {\mathbb Z}+\Delta_a,\atop j\in{\mathbb Z}}{\mathcal H}^{i,j}_a$$ which categorifies the $q$-series $\widehat{Z}_a(q)$. Namely[^6], $$\widehat{Z}_a(q)=\sum_{i\in {\mathbb Z}+\Delta_a,\atop j\in{\mathbb Z}}q^{i}(-1)^j\dim{\mathcal H}^{i,j}_a.
    \label{BlockEuler}$$ Because of their close relation to homological invariants, we usually refer to $\widehat{Z}_a(q)$ as *homological blocks*. The vector space ${\mathcal H}_{D^2}[M_3]$ can be interpreted as the closed 3-manifold analog of Khovanov-Rozansky knot homology. From this point of view, $e^{4\pi i{\ell k}(a,\cdot)}$ can be understood as the variable associated with ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2$ grading and enters into the decomposition [\[WRT-decomposition\]](#WRT-decomposition){reference-type="eqref" reference="WRT-decomposition"} much like $q$, the variable for one of the ${\mathbb Z}$-gradings (the "$q$-grading"). Note that the label $a$ in ${\mathcal H}^{i,j}_a$ is reminiscent of the Spin$^c$ structure in Heegaard/monopole Floer homologies of 3-manifolds. This fact, of course, is not an accident and plays an important role in the relation between Heegaard/monopole Floer homologies of 3-manifolds and the categorification of WRT invariants [@Gukov:2016gkn].

Next, we describe the physics behind the Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"}. (A mathematically inclined reader may skip directly to Conjecture [\[Conjecture2\]](#Conjecture2){reference-type="ref" reference="Conjecture2"}.)

![Another representation of the background in Figure 1.](cigar1){#fig:cigar1 width="3.5in"}

[^1]: It is in fact $\left({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})\right)^*/{\mathbb Z}_2$ that is canonically identified with components of abelian flat connections. However, as the distinction between ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ and its dual is only important in section [0.1](#sec:summaryConj){reference-type="ref" reference="sec:summaryConj"}, we will use the same set of labels $\{a, b, \ldots\}$ for elements in both groups.

[^2]: A related conjecture was made in [@hikami2011decomposition]. However it did not include the $S$-transform, which is crucial for restoring integrality and categorification.

[^3]: The constant positive integer $c$ depends only on $M_3$ and in a certain sense measures its "complexity". In many simple examples $c=0$, and the reader is welcome to ignore $2^{-c}$ factor which arises from some technical subtleties. Its physical origin will be explained later in the paper.

[^4]: Later in the text we will sometimes use slightly redefined quantities, $\widehat{Z}_a(q)\rightarrow q^{\Delta}\widehat{Z}_a(q)$, where $\Delta$ is a common, $a$ independent rational number.

[^5]: Recall that ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$, as a finitely generated abelian group, can be decomposed into ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})= \prod_{i}{\mathbb Z}_{p_i}$. We ask for a fairly weak condition that ${\mathbb Z}_2$ doesn't appear in this decomposition. In other words, $M_3$ is a ${\mathbb Z}_2$-homology sphere. Equivalently, there is a unique Spin structure on $M_3$, so that there is no ambiguity in specifying Nahm-pole boundary condition for ${\mathcal N}=4$ $SU(2)$ SYM on $M_3\times{\mathbb R}_+$ [@Witten:2011zz]. The general case, in principle, could also be worked out. We leave it as an exercise to an interested reader.

[^6]: The presence of $1/2$ factors that produce $2^{-c}$ overall factor in ([\[Block-qSeries\]](#Block-qSeries){reference-type="ref" reference="Block-qSeries"}) can be interpreted as presence of factors $\cong {\mathbb C}[x]$ with $\text{deg}_qx=0$ in ${\mathcal H}_a[M_3]$. The $q$-graded Euler charecteristic of ${\mathbb C}[x]$ is naively divergent: $1+1+1+\ldots$, but its zeta-regularization gives $1/2$.
