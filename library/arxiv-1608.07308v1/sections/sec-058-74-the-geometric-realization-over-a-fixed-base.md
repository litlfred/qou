---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-058-74-the-geometric-realization-over-a-fixed-base
section_title: "The geometric realization over a fixed base"
section_number: 7.4
pages: 54-57
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.871
latex_coverage_ratio: 0.959
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:geometric diagonalization label="sub:geometric diagonalization"}

As we saw in Lemma [\[lem:universal\]](#lem:universal){reference-type="ref" reference="lem:universal"}, any categorical diagonalization in a category $\mathcal{C}$ comes from a $T$--equivariant map: $$\mathcal{C}\rightarrow \mathbb{P}^n_A \qquad \text{i.e.} \qquad K^b(\mathcal{C}) \xtofrom[\iota^*]{\iota_*} \mathcal{D}$$ where $\mathcal{D}= D^b(\mathrm{Coh}_T(\mathbb{P}^n_A))$, and the action $T \curvearrowright \mathbb{P}^n_A$ is given in [\[eqn:action\]](#eqn:action){reference-type="eqref" reference="eqn:action"}. The above functors extend to functors on the homological completions: $$K(\mathcal{C}^{\uparrow}) \xtofrom[\iota^*]{\iota_*} \mathcal{D}^{\uparrow}$$ which are given by the same formulas, but allow infinite direct sums of objects in decreasing homological degree. Therefore, we have: $$P_i = \iota^*(\mathcal{P}_i)$$ where $\mathcal{P}_i \in \mathcal{D}^{\uparrow}$ are given by formula [\[eqn:idempotent\]](#eqn:idempotent){reference-type="eqref" reference="eqn:idempotent"} with $F$ replaced by $\mathcal{O}(1)$ and $\alpha_i$ replaced by multiplication with the homogeneous coordinate $z_i$: $$\label{eqn:idempotent geometry}
\includegraphics{7_9.png}$$ The rows in the above diagram make up for the expansion of the geometric series $(\lambda_j - \lambda_i)^{-1}$. Meanwhile, observe that the top row is precisely; $$\label{eqn:quasi}
\text{top row of }\mathcal{P}_i = \bigotimes_{j<i} \left[\mathcal{O}\stackrel{z_j}\longrightarrow  \mathcal{O}(1) \lambda_j^{-1}\right] \bigotimes_{j>i} \left[\lambda_j \lambda_i^{-1} \stackrel{z_j}\longrightarrow \mathcal{O}(1)\lambda_i^{-1} \right] \stackrel{\mathrm{q.i.s.}}\cong \mathcal{O}_{p_i} \prod_{j<i} \frac {\lambda_i}{\lambda_j}$$ Here, $\mathcal{O}_{p_i}$ is the structure sheaf of the torus invariant subscheme $p_i = [0:...:0:1:0:...:0] \in \mathbb{P}^n_A$, which is a closed point if and only if $A$ is a field. The quasi-isomorphism in [\[eqn:quasi\]](#eqn:quasi){reference-type="eqref" reference="eqn:quasi"} is the standard one between the structure sheaf of $p_i$ and its Koszul complex. We conclude that the full idempotent [\[eqn:idempotent geometry\]](#eqn:idempotent geometry){reference-type="eqref" reference="eqn:idempotent geometry"} is a way to make sense of the denominators in the object: $$\label{pi as a fraction}
\mathcal{P}_i = \frac {\mathcal{O}_{p_i}}{\prod_{0 \leq j \neq i \leq n} \left(1-\frac {\lambda_j}{\lambda_i} \right)} \in \overline{\mathcal{D}}$$ Recall from [\[eqn:semi orthogonal\]](#eqn:semi orthogonal){reference-type="eqref" reference="eqn:semi orthogonal"} that $\mathcal{P}_0,...,\mathcal{P}_n$ give a decomposition of the unit object in $\overline{\mathcal{D}}$. This statement categorifies the fact that: $$[\mathcal{O}] = \sum_{i=0}^n [\mathcal{P}_i] = \sum_{i=0}^n \frac {[\mathcal{O}_{p_i}]}{\prod_{0\leq j \neq i \leq n} \left(1 - \frac {\lambda_j}{\lambda_i} \right)}$$ in the algebraic $K$--theory ring of $\mathbb{P}^n_A$. The above is nothing but the Thomason equivariant localization formula, which is a very interesting result even in $K$--theory. At the categorical level, it is made even more interesting by the presence of the various differentials that appear in [\[eqn:semi orthogonal\]](#eqn:semi orthogonal){reference-type="eqref" reference="eqn:semi orthogonal"}, which give rise to a semi-orthogonal decomposition of the category $\overline{\mathcal{D}}$.

The denominator of [\[pi as a fraction\]](#pi as a fraction){reference-type="eqref" reference="pi as a fraction"} equals the Poincaré series for the equivariant local ring of $\mathbb{P}^n_A$ at $p_i$. This is not a coincidence, and the relation between the two objects can be made more precise.

::: proposition
[]{#open vs proj label="open vs proj"} Consider a locally closed subset $S_i=\{z_0=\ldots=z_{i-1}=0,z_i\neq 0\}\subset \mathbb{P}^n_{A}$. Then $\mathcal{P}_i$ is quasi-isomorphic to the pushforward of $S^{\bullet}(\nu^{\vee}_{S_i})$, where $\nu_{S_i}$ is the normal bundle to $S_i$.
:::

::: remark
The ordering of coordinates in the definition of $S_i$ agrees with the ordering of eigenvalues of $\mathcal{O}(1)$ (that is, the weights of the torus action) on $\mathbb{P}^n$. It is easy to see that the strata $S_i$ agree with the cells in the Białynicki-Birula decomposition [@BB1; @BB2] of $\mathbb{P}^n$ with respect to this torus action. Similar decompositions of equivariant derived categories with respect to Białynicki-Birula strata were studied in [@DanHL], and we plan to study the relation between the categorical diagonalization framework and [@DanHL] in the future work.
:::

::: proof
*Proof.* To simplify the notations, we will consider the case $n=1$ and omit all the grading shifts (which can be easily reconstructed since all maps are homogeneous). The construction [\[eqn:idempotent geometry\]](#eqn:idempotent geometry){reference-type="eqref" reference="eqn:idempotent geometry"} yields two different infinite complexes built from the sections $z_0,z_1:\mathcal{O}\to \mathcal{O}(1)$. The first has a form: $$\includegraphics{pf_7_11a.png}$$ Here $y$ is a formal variable corresponding to the shift of the complex down by one unit. It can be made less formal by considering the projection $\pi:\mathbb{P}^n\times \mathbb{A}^1\to \mathbb{P}^n$, so that $$\mathcal{P}_0=p_*\left[\mathcal{O}\xrightarrow{z_1+yz_0}\mathcal{O}(1)\right]=p_*\mathcal{O}_{\{z_1+yz_0=0\}}.$$ The projection $p$ identifies the closed subset $\{z_1+yz_0=0\}\subset \mathbb{P}^n\times \mathbb{A}^1$ with the open subset $S_0=\{z_0\neq 0\}\subset \mathbb{P}^n$, so $\mathcal{P}_0=\mathcal{O}_{S_0}$. The second complex is more interesting. It has the form: $$\includegraphics{pf_7_11b.png}$$ It is supported on $S_1=\mathbb{P}^1\setminus S_0=\{z_0=0\}$ where the stalk of $\mathcal{O}$ is isomorphic to $\mathbb{C}[\frac{z_0}{z_1}]$ and the stalk of $\mathcal{O}_{S_0}$ is isomorphic to $\mathbb{C}[\frac{z_0}{z_1},\frac{z_1}{z_0}]$, so the quotient is isomorphic to $\frac{z_1}{z_0}\cdot \mathbb{C}[\frac{z_1}{z_0}].$ ◻
:::

::: remark
Note that $$\includegraphics{rmk_7_13.png}$$ One can use similar arguments to formally match this complex with $\mathcal{O}_{\{z_1\neq 0\}}\otimes \mathcal{O}(-1)=\mathcal{O}_{\{z_1\neq 0\}}$. However, $\mathcal{P}_1^{\vee}$ does not belong to the category $\mathcal{D}^{\uparrow}$ since the gradings of its summands are unbounded.
:::

::: corollary
The endomorphism ring of $\mathcal{P}_i$ is isomorphic to the local ring of $\mathbb{P}^n_{A}$ at a fixed point $p_i$.
:::

::: proof
*Proof.* We follow the proof of Proposition [\[open vs proj\]](#open vs proj){reference-type="ref" reference="open vs proj"}. Indeed, $\mathrm{End}(\mathcal{P}_0)=H^0(S_0,\mathcal{O}_{S_0})=\mathbb{C}[\frac{z_1}{z_0}]$. On the other hand, $$\mathrm{End}(\mathcal{P}_1)=\mathrm{End}\left[\mathbb{C}\left[\frac{z_0}{z_1}\right]\rightarrow \mathbb{C}\left[\frac{z_1}{z_0},\frac{z_0}{z_1}\right]\right]=\mathbb{C}\left[\frac{z_0}{z_1}\right].$$ One could also argue that $$\mathrm{End}(\mathcal{P}_1)=\mathrm{End}(\mathcal{P}_1^{\vee})=\mathrm{End}(\mathcal{O}_{\{z_1\neq 0\}})=\mathbb{C}\left[\frac{z_0}{z_1}\right].$$ The proof for general $n$ is analogous. ◻
:::

::: remark
Proposition [\[open vs proj\]](#open vs proj){reference-type="ref" reference="open vs proj"} shows that the endomorphism rings of the projectors can be interpreted as the rings of functions on certain open charts. This point of view will be important in the next section where we define some open charts on the flag Hilbert scheme and compute the rings of functions on them (up to a certain completion). By Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} and the preceding discussion these rings match the homology of the categorified Jones-Wenzl projectors.
:::

::: remark
[]{#rem:what if label="rem:what if"} The equivariant localization formula makes sense when $\mathcal{D}= D^b(\mathrm{Coh}_T(X))$ for any local complete intersection $X$ acted on by a torus $T$: $$\label{eqn:equivloc}
[\mathcal{O}_X] = \sum_{p \in X^T} \frac {[\mathcal{O}_p]}{\wedge^\bullet \left( \text{Tan}_p^\vee X \right)}$$ As we have seen, when $X = \mathbb{P}^n$ the above setup encodes categorical diagonalization as in Definition [\[def:EH2\]](#def:EH2){reference-type="ref" reference="def:EH2"} and [\[def:EH3\]](#def:EH3){reference-type="ref" reference="def:EH3"}. It would be very interesting to determine which problems in "categorical linear algebra\" are encoded by formula [\[eqn:equivloc\]](#eqn:equivloc){reference-type="eqref" reference="eqn:equivloc"} for more general schemes $X$.
:::

## The relative case

For the remainder of this Section, we will generalize the objects [\[eqn:idempotent geometry\]](#eqn:idempotent geometry){reference-type="eqref" reference="eqn:idempotent geometry"} from $\mathbb{P}^n_A$ to projective bundles $\mathbb{P}\mathcal{V}^\vee$ on an arbitrary base scheme $X$, as in Example [\[ex:equivrelative\]](#ex:equivrelative){reference-type="ref" reference="ex:equivrelative"}. We assume that both $X$ and $\mathcal{V}$ are acted on by a torus $T$, and that we have a decomposition: $$\label{eqn:bill}
\mathcal{O}_X \cong \left[ \bigoplus_{x\in X^T} \mathcal{P}_x, \text{ a certain differential}\right] \in \overline{D^b(\mathrm{Coh}_T(X))}$$ where the indexing set goes over the fixed points of $X$. We assume that the above is semi-orthogonal, in the sense that $\mathop{\mathrm{Hom}}(\mathcal{P}_x, \mathcal{P}_y) = 0$ whenever $x>y$ with respect to some total order. We wish to upgrade the decomposition [\[eqn:bill\]](#eqn:bill){reference-type="eqref" reference="eqn:bill"} to the projective bundle $\mathbb{P}\mathcal{V}^{\vee}$.

::: proposition
[]{#prop:decomposition projective label="prop:decomposition projective"}

Let $n + 1 = \emph{rank }\mathcal{V}$. There exist objects $\mathcal{P}_i^x$ for all $i \in \{0,...,n\}$ and $x\in X^T$, such that we have a semi-orthogonal decomposition: $$\label{eqn:decomposition}
\mathcal{O}_{\mathbb{P}\mathcal{V}^{\vee}} \cong \left[ \bigoplus^{0\leq i \leq n}_{x\in X^T} \mathcal{P}^i_x, \text{ a certain differential}\right] \in \overline{D^b(\mathrm{Coh}_T(\mathbb{P}\mathcal{V}^\vee))}$$ whenever the homological subtorus $\mathbb{C}^* \subset T$ acts with distinct weights in the fibers $\mathcal{V}|_x$ for all $x \in X^T$. We have $\mathop{\mathrm{Hom}}(\mathcal{P}_x^i, \mathcal{P}_y^j) = 0$ if $x>y$ or if $x=y$ and $i<j$.
:::

The object $\mathcal{P}_x^i$ is precisely of the form [\[eqn:idempotent geometry\]](#eqn:idempotent geometry){reference-type="eqref" reference="eqn:idempotent geometry"} if one replaces $\mathcal{O}$ with $\mathcal{P}_x$, and $\lambda_0,...,\lambda_n$ are precisely the weights of the torus $T$ in the fiber $\mathcal{V}|_x$.
