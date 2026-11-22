---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-019-27-the-dg-scheme
section_title: "The dg scheme"
section_number: 2.7
pages: 18-19
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.926
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:dg scheme label="sub:dg scheme"}

We will now give an alternative definition of the dg scheme [\[eqn:def dg zero\]](#eqn:def dg zero){reference-type="eqref" reference="eqn:def dg zero"}, and we leave it as an exercise to the interested reader to show that the two descriptions are equivalent (we will only use the definition in this Subsection for the remainder of this paper). The idea is to note that the map $\Psi$ of the complex [\[eqn:two step\]](#eqn:two step){reference-type="eqref" reference="eqn:two step"} fails to be injective on many fibers, and this will lead to the flag Hilbert scheme misbehaving. To remedy this issue, we replace the middle cohomology sheaf $H^0 (\mathcal{E}_n)$ in [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} by the entire complex $\mathcal{E}_n$ (we tacitly suppress the symbol $* \in \{\mathbb{C}^2,\mathbb{C},\mathrm{point}\}$ since the construction applies equally well to all three choices).

::: proposition
[]{#prop:dg scheme label="prop:dg scheme"}

There exist dg schemes $\mathrm{FHilb}_n^\emph{dg}$ endowed with flags of objects: $$\mathcal{T}_n \rightarrow \mathcal{T}_{n-1} \rightarrow ... \rightarrow \mathcal{T}_1 \quad \in D^b(\mathrm{Coh}(\mathrm{FHilb}_n^\emph{dg}))$$ together with maps $q\mathcal{T}_n \stackrel{X}\rightarrow \mathcal{T}_n$, $t\mathcal{T}_n \stackrel{Y}\rightarrow \mathcal{T}_n$ that respect the above flag, and $\mathcal{O}\stackrel{v}\rightarrow \mathcal{T}_n$ such that: $$\label{eqn:def dg}
\mathrm{FHilb}_{n+1}^\emph{dg}= \mathbb{P}_{\mathrm{FHilb}^\emph{dg}_{n}} \left( \mathcal{E}_n^\vee  \right) := \mathrm{Proj}_{\mathrm{FHilb}^\emph{dg}_{n}} \left(S^\bullet\mathcal{E}_n\right)$$ where the complex $\mathcal{E}_n$ is defined by formula [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"}. See Subsection [\[sub:proj dg\]](#sub:proj dg){reference-type="ref" reference="sub:proj dg"} for the definition of the Proj construction of a two-step complex of vector bundles (according to [\[eqn:two step\]](#eqn:two step){reference-type="eqref" reference="eqn:two step"}).
:::

::: proof
*Proof.* Let us write $\mathcal{L}_{n+1} = \mathcal{O}(1)$ for the tautological line bundle on the projectivization [\[eqn:def dg\]](#eqn:def dg){reference-type="eqref" reference="eqn:def dg"}, and $\pi:\mathrm{FHilb}_{n+1} \rightarrow \mathrm{FHilb}_n$ for the natural map. Take the defining map of projective bundles: $$\text{Taut} \in \mathop{\mathrm{Hom}}(\pi^*\mathcal{E}_n, \mathcal{O}(1))$$ and compose it with the natural map $\mathcal{T}_n[-1] \stackrel{i}\rightarrow \mathcal{E}_n$. We obtain an object: $$i_*(\text{Taut}) \ =: \ \mathcal{T}_{n+1} \in \mathop{\mathrm{Hom}}\left(\pi^*\mathcal{T}_n[-1],\mathcal{L}_{n+1} \right)$$ Composing the map $i$ with $q\mathcal{T}_n \oplus t\mathcal{T}_n \oplus \mathcal{O}\xrightarrow{(X,Y,v)} \mathcal{T}_n$ yields 0, hence: $$(X,Y,v)_* \left( \mathcal{T}_{n+1} \right) \in \mathop{\mathrm{Hom}}\left(\pi^*( q\mathcal{T}_n \oplus t\mathcal{T}_n \oplus \mathcal{O})[-1], \mathcal{L}_{n+1} \right)$$ equals 0 as well. This precisely gives rise to a splitting: $$\includegraphics{before_2_37.png}$$ and the dotted map is the desired extension of the arrows $X,Y,v$ from $\mathcal{T}_n$ to $\mathcal{T}_{n+1}$. Note that we may write the above diagram as an equality in the derived category of $\mathrm{FHilb}_{n+1}^\text{dg}$: $$\label{eqn:ind}
\left[ qt \mathcal{L}_{n+1} \xrightarrow{(-y,x)} \underline{q \mathcal{L}_{n+1} \oplus t \mathcal{L}_{n+1}} \xrightarrow{(x,y)} \mathcal{L}_{n+1} \right] \cong \left[ \underline{\mathcal{E}_{n+1}} \longrightarrow \widetilde{\pi^*(\mathcal{E}_n)} \right]$$ where we have underlined the $0$--th terms of both complexes. In the above equation, we write $x$ and $y$ for the operators of multiplication by $x_n-x_{n+1}$ and $y_n-y_{n+1}$, respectively, and: $$\label{eqn:switch}
\widetilde{\pi^*(\mathcal{E}_n)} \ \text{ denotes } \ \pi^*(\mathcal{E}_n) \text{ with the variables }(x_n,x_{n+1}) \text{ and }(y_n,y_{n+1}) \text{ switched}$$ ◻
:::

One can run the proof of Proposition [\[prop:dg scheme\]](#prop:dg scheme){reference-type="ref" reference="prop:dg scheme"} with $\mathcal{E}_n$ replaced by $H^0\mathcal{E}_n$. We leave it as an exercise to the interested reader to show that one would obtain the schemes $\mathrm{FHilb}_n$ of Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"}.
