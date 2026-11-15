---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-003-22-disks
section_title: "Disks"
section_number: 2.2
pages: 9-11
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.948
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We now consider $B$-framed $n$-disks. In terms of configuration spaces, we identify the maximal $\infty$-subgroupoid of $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$, $B$-framed $n$-disks embedding into a $B$-framed $n$-manifold.

::: definition
The symmetric monoidal $\mathop{\mathrm{\infty}}$-category $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_n$ is the full $\mathop{\mathrm{\infty}}$-subcategory of $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_n$ whose objects are disjoint unions of $B$-framed $n$-dimensional Euclidean spaces.
:::

::: remark
Consider $\ast\rightarrow\mathop{\mathrm{\sf BTop}}(n)$, the basepoint of $\mathop{\mathrm{\sf BTop}}(n)$. A $\ast$-structure on an $n$-manifold $M$ is then equivalent to a topological framing of the tangent microbundle $\tau_M$ of $M$,[^1] and we denote the associated $\mathop{\mathrm{\infty}}$-category of framed $n$-disks as $\mathop{\mathrm{{\mathcal D}\sf isk}}^{\mathop{\mathrm{\sf fr}}}_n$. This symmetric monoidal $\infty$-category $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\mathop{\mathrm{\sf fr}}}$ is homotopy equivalent to the PROP associated to the $\mathcal E_n$ operad of Boardman-Vogt [@bv]. This follows because the inclusion of rectilinear embeddings as framed embeddings determines a homotopy equivalence $\mathcal E_n(I) \xrightarrow\sim \mathop{\mathrm{\mathsf{Emb}}}^{\sf fr}(\bigsqcup_I \mathbb R^n, \mathbb R^n)$ from the $I$-ary space of the $\mathcal E_n$ operad.
:::

::: example
For $B=\mathop{\mathrm{{\mathsf BO}}}(n)$, with the usual map $\mathop{\mathrm{{\mathsf BO}}}(n)\rightarrow\mathop{\mathrm{\sf BTop}}(n)$, the $\mathop{\mathrm{\infty}}$-category of topological $n$-disks with $\mathop{\mathrm{{\mathsf BO}}}(n)$-framings is equivalent to the $\mathop{\mathrm{\infty}}$-category of smooth $n$-disks and smooth embeddings, $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\mathop{\mathrm{\mathsf{sm}}}}\simeq\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{{\sf BO}(n)}$. These are both equivalent to the PROP associated to the unoriented version of the ribbon, or "framed,\" $\mathcal E_n$ operad; see [@sw] for a treatment of this operad.[^2] To see these equivalences it is enough to explain why each of the natural maps $\mathsf O(n) \rightarrow\mathop{\mathrm{\mathsf{Emb}}}^{\mathop{\mathrm{\mathsf{sm}}}}(\mathbb R^n,\mathbb R^n) \rightarrow\mathop{\mathrm{\mathsf{Emb}}}^{{\sf BO}(n)}(\mathbb R^n,\mathbb R^n)$ is an equivalence. Smoothing theory ([@kirbysieb]) gives the equivalence of the second map. Via Gram--Schmidt, the inclusion $\mathsf O(n) \xrightarrow{\simeq} {\sf GL}(\mathbb R^n)$ is a deformation retraction. Conjugation by scaling and translation, $(f,t)\mapsto \bigl(x\mapsto  \frac{f(tx)-f(0)}{t}+f(0)\bigr)$, demonstrates the inclusion ${\sf GL}(\mathbb R^n) \xrightarrow{\simeq} \mathop{\mathrm{\mathsf{Emb}}}^{\sf sm}(\mathbb R^n,\mathbb R^n)$ as a deformation retraction.
:::

Given a topological space $X$ and a finite cardinality $i$, we let $\mathop{\mathrm{\mathsf{Conf}}}_i(X)\subset X^i$ denote the subspace of those maps $\{1,\dots,i\}\to X$ which are *injective*. This configuration space has an evident free action of the symmetric group $\Sigma_i$.

In the next result, for $M$ a $B$-framed $n$-manifold, we consider the over $\infty$-category $$\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}^B~:=~ \mathop{\mathrm{{\mathcal D}\sf isk}}^B_n \underset{\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^B}\times \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}^B_{n/M}~.$$ Informally, an object is an embedding $\underset{i}\sqcup \mathbb R^n \hookrightarrow M$ for some $i$.

::: lemma
[]{#EE-equivs label="EE-equivs"} The maximal $\infty$-subgroupoid of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B$ is canonically identified as the space $$\underset{i\geq 0} \coprod {B}^i_{\Sigma_i}~\simeq~\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}_n^B\bigr)^\sim$$ where the coproduct is indexed by finite cardinalities and each cofactor is the $\Sigma_i$-homotopy coinvariants of the $i$-fold product of the space $B$. In particular, the symmetric monoidal functor $[-]\colon \mathop{\mathrm{{\mathcal D}\sf isk}}_n^B \to \mathop{\mathrm{\sf Fin}}$, given by taking sets of connected components of underlying manifolds, is conservative.

For $M$ a $B$-framed $n$-manifold, the maximal $\infty$-subgroupoid of $\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}$ is canonically identified as the space $$\underset{i\geq 0}\coprod \mathop{\mathrm{\mathsf{Conf}}}_i(M)_{\Sigma_i}~\simeq~\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}^B_{n/M}\bigr)^\sim$$ where the coproduct is indexed by finite cardinalities, and each cofactor is an unordered configuration space.
:::

::: proof
*Proof.* Lemma [\[slice-slice\]](#slice-slice){reference-type="ref" reference="slice-slice"} gives an equivalence $\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}^B\simeq \mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}$. So it suffices to assume the case of an equality $B= \mathop{\mathrm{\sf BTop}}(n)$.

The maximal $\infty$-subgroupoid of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n$ necessarily lies over the maximal $\infty$-subgroupoid of $\mathop{\mathrm{\sf Fin}}$, which is $\underset{i\geq 0}\coprod \mathsf B\Sigma_i$. The first assertion will be implied upon verifying, for each $i\geq 0$, that the map $${\Sigma_i\wr {\sf Top}(n)}  \longrightarrow \mathop{\mathrm{\mathsf{Emb}}}(\underset{i} \sqcup \mathbb R^n,\underset{i}\sqcup \mathbb R^n)$$ is weakly homotopy equivalent to an inclusion of connected components. This is an immediate consequence of the Kister--Mazur Theorem [\[kister\]](#kister){reference-type="ref" reference="kister"}. Via translation, the inclusion of the subgroup of origin preserving homeomorphisms $\mathop{\mathrm{\mathsf{Top}}}_0(n) \xrightarrow{\simeq}\mathop{\mathrm{\mathsf{Top}}}(n)$ is a homotopy equivalence, and so we recognize further the identification $$\underset{i\geq 0}\coprod \mathsf B(\Sigma_i\wr \mathop{\mathrm{\mathsf{Top}}}_0(n))\xrightarrow{~\simeq~} (\mathop{\mathrm{{\mathcal D}\sf isk}}_n)^\sim~.$$

Because the projection $\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}\to \mathop{\mathrm{{\mathcal D}\sf isk}}_n$ is a right fibration, we recognize the maximal $\infty$-subgroupoid of $\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M}$ as $$\underset{i\geq 0} \coprod \mathop{\mathrm{\mathsf{Emb}}}\bigl(\underset{i}\sqcup \mathbb R^n,M\bigr)_{\Sigma_i\wr \mathop{\mathrm{\mathsf{Top}}}_0(n)}\xrightarrow{~\simeq~}(\mathop{\mathrm{{\mathcal D}\sf isk}}_{n/M})^\sim~.$$ Therefore, the second assertion follows upon showing that the $\Sigma_i$-equivariant continuous map $${\sf ev}_0\colon \mathop{\mathrm{\mathsf{Emb}}}\bigl(\underset{i}\sqcup \mathbb R^n,M\bigr)_{\mathop{\mathrm{\mathsf{Top}}}_0(n)^i} \longrightarrow \mathop{\mathrm{\mathsf{Conf}}}_i(M)$$ is a weak homotopy equivalence. This is implied upon showing the homotopy fiber of the continuous map $${\sf ev}_0\colon \mathop{\mathrm{\mathsf{Emb}}}(\underset{i}\sqcup \mathbb R^n,M) \longrightarrow \mathop{\mathrm{\mathsf{Conf}}}_i(M)$$ is weakly homotopy equivalent to $\mathop{\mathrm{\mathsf{Top}}}_0(n)^i$. In a standard manner, this map is a Serre fibration, and the fiber over $c\colon \{1,\dots,i\}\hookrightarrow M$ is the space $\mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M)$ of embeddings under $c$. Fix such a based embedding $e_0\colon \underset{i}\sqcup \mathbb R^n \hookrightarrow M$. So we must show that the composite inclusion $$\mathop{\mathrm{\mathsf{Top}}}_0(n)^i \hookrightarrow \mathop{\mathrm{\mathsf{Emb}}}((0\in \mathbb R^n),(0\in \mathbb R^n))^i\cong \mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,\underset{i}\sqcup \mathbb R^n)\xrightarrow{-\circ e_0} \mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M)$$ is a weak homotopy equivalence.

The Kister--Mazur Theorem gives that the first of these maps is a homotopy equivalence. The problem is thus reduced to showing that the second of these maps is a weak homotopy equivalence. This is the problem of showing that each solid diagram among topological spaces $$\xymatrix{
S^{k-1} \ar[rr]^-{f_0}  \ar[d]
&&
\mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,\underset{i}\sqcup \mathbb R^n)  \ar[d]
\\
\mathbb D^k  \ar[rr]_-{f}  \ar@{-->}[urr]^-{\widetilde{f}}  
&&
\mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M)
}$$ admits a filler with respect to which the diagram commutes up to homotopy. Choose a continuous map $\phi\colon (0,1]\times \mathbb R^n \to \mathbb R^n$ such that $\phi_t$ is an origin preserving open embedding for each $t$, $\phi_1 = {\sf id}_{\mathbb R^n}$, the closure $\overline{\phi_s(\mathbb R^n)}\subset \phi_t(\mathbb R^n)$ whenever $s<t$, and the collection of images $\{\phi_t(\mathbb R^n)\mid 0<t\leq 1\}$ is a basis for the topology about $0\in \mathbb R^n$. Choose a continuous map $\mathbb D^k \xrightarrow{\epsilon} (0,1]$ for which the restriction $\epsilon_{|S^{k-1}} \equiv 1$ is identically one, and the composition $$\mathbb D^k\xrightarrow{~f~}\mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M) \xrightarrow{~(\underset{i} \sqcup \phi_\epsilon)^\ast~} \mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M)$$ factors through $\mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,\underset{i}\sqcup \mathbb R^n)$. Define $\widetilde{f}$ to be this factorization. By construction, the restriction $\widetilde{f}_{|S^{k-1}} = f_0$. The map $[0,1]\times\mathbb D^k \to \mathop{\mathrm{\mathsf{Emb}}}_0(\underset{i}\sqcup \mathbb R^n,M)$ given by $(t,p)\mapsto f\circ (\underset{i}\sqcup \phi_{t\epsilon +(1-t)})^\ast(p)$ demonstrates a homotopy making the lower triangle commute. ◻
:::

We conclude this section by justifying the term *tangent classifier* for the functor $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n \xrightarrow{\tau} \mathop{\mathrm{\mathsf{Spaces}}}_{/\mathop{\mathrm{\sf BTop}}(n)}$ of (1).

::: cor
[]{#tang-class label="tang-class"} The value of the tangent classifier ([\[tau\]](#tau){reference-type="ref" reference="tau"}) on a topological $n$-manifold $M$ is the map of spaces $M \xrightarrow{\tau_M} \mathop{\mathrm{\sf BTop}}(n)$ classifying the tangent microbundle.
:::

::: proof
*Proof.* Recognize $\mathcal E{\sf uc}_n\subset \mathop{\mathrm{{\mathcal D}\sf isk}}_n$ as the full $\infty$-subcategory consisting of the connected $n$-manifolds. Specialize the second statement of Lemma [\[EE-equivs\]](#EE-equivs){reference-type="ref" reference="EE-equivs"} to $i=1$ to obtain an identification $$M~\simeq~ \mathcal E{\sf uc}_{n/M}~\simeq~ \mathop{\mathrm{\mathsf{Emb}}}(\mathbb R^n,M)_{{\sf Top}(n)} \longrightarrow \mathop{\mathrm{\sf BTop}}(n)$$ involving the homotopy ${\sf Top}(n)$-coinvariants. Manifestly, this map of spaces agrees with the tangent classifier in the case $M=\mathbb R^n$. By construction, this map is functorial in the argument $M \in \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n$. The general case follows. ◻
:::

[^1]: By smoothing theory, framed topological manifolds are essentially equivalent to framed smooth manifolds except in dimension 4.

[^2]: The historical use of "framed\" here is potentially misleading, since in the "framed\" $\mathcal E_n$ operad the embeddings do not preserve the framing, while in the usual $\mathcal E_n$ operad the embeddings do preserve the framing (up to scale). It might lead to less confusion to replace the term "framed $\mathcal E_n$ operad\" with "unoriented $\mathcal E_n$ operad.\"
