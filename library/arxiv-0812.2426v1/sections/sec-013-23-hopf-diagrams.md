---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-013-23-hopf-diagrams
section_title: "Hopf diagrams"
section_number: 2.3
pages: 8-11
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 0.933
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-Hdiag label="sect-Hdiag"} For a precise treatment of the theory of Hopf diagrams, we refer to [@BV1]. Note that Habiro, shortly after us, had similar results in [@Hab1].

Briefly speaking, a *Hopf diagram* is a planar diagram, with inputs but no output, obtained by stacking the generators of Figure [1](#gensHdiag){reference-type="ref" reference="gensHdiag"} (diagrams are read from bottom to top). Examples of Hopf diagrams with 1 and 2 inputs are depicted in Figure [2](#exsHdiag){reference-type="ref" reference="exsHdiag"}. Hopf diagrams are submitted to the relations of Figure [3](#relsHdiag){reference-type="ref" reference="relsHdiag"} (plus relations expressing that $\tau$ is an invertible QYBE solution which is natural with respect to the other generators). In particular, the relations of Figure [3](#relsHdiag){reference-type="ref" reference="relsHdiag"} say that $\Delta$ behaves as a coproduct with counit $\varepsilon$, $S$ behaves as an antipode, $\omega_\pm$ behaves as a Hopf pairing, and $\theta_\pm$ behaves as a twist form. The last two relations of Figure [3](#relsHdiag){reference-type="ref" reference="relsHdiag"} are nothing but the Markov relations for pure braids.

<figure id="gensHdiag">
<div class="center">
<p><span class="math inline"><em>Δ</em>= </span> , <span class="math inline"><em>ε</em>= </span> , <span class="math inline"><em>ω</em><sub>+</sub>= </span> , <span class="math inline"><em>ω</em><sub>−</sub>= </span> ,<br />
<span class="math inline"><em>θ</em><sub>+</sub>= </span> , <span class="math inline"><em>θ</em><sub>−</sub>= </span> , <span class="math inline"><em>S</em>= </span> , <span class="math inline"><em>S</em><sup>−1</sup>= </span> ,<br />
<span class="math inline"><em>τ</em>= </span> , <span class="math inline"><em>τ</em><sup>−1</sup>= </span> .</p>
</div>
<figcaption>Generators of Hopf diagrams</figcaption>
</figure>

<figure id="exsHdiag">
<div class="center">

</div>
<figcaption>Examples of Hopf diagrams</figcaption>
</figure>

<figure id="relsHdiag">
<div class="center">
<p>  , ,<br />
, , , ,<br />
, ,<br />
[Bl][Bl]<span>,</span> [Bl][Bl]<span>.</span> <embed src="relsuptheta1.eps" /><br />
<embed src="relsupRII.eps" /><br />
<embed src="relsup3T.eps" /><br />
<embed src="relsup4T.eps" /></p>
</div>
<figcaption>Relations on Hopf diagrams</figcaption>
</figure>

Hopf diagrams with the same number of inputs can be composed using the *convolution product* $\star$ defined in Figure [4](#convoprod){reference-type="ref" reference="convoprod"}. This leads to the category $\mathcal{D}iag$ of Hopf diagrams. Objects of $\mathcal{D}iag$ are the non-negative integers. For two non-negative integers $m$ and $n$, the set $\mathrm{Hom}_{\mathcal{D}iag}(m,n)$ of morphisms from $m$ to $n$ is the empty set if $m \neq n$ and is the set of Hopf diagrams with $m$ inputs (up to their relations) if $m=n$. The composition is the convolution product and the identity of $n$ is the Hopf diagram obtained by juxtaposing $n$ copies of $\varepsilon$.

The category $\mathcal{D}iag$ is a monoidal category: $m \otimes n=m+n$ on objects and the monoidal product $D \otimes D'$ of two Hopf diagrams $D$ and $D'$ is the Hopf diagram obtained by juxtaposing $D$ on the left of $D'$.

<figure id="convoprod">
<div class="center">
<p>[cc][cc]<span><span class="math inline"><em>D</em> ⋆ <em>D</em>′</span></span> [cc][cc]<span><span class="math inline"><em>D</em></span></span> [cc][cc]<span><span class="math inline"><em>D</em>′</span></span> [cc][cc]<span><span class="math inline">∘</span></span> <embed src="convoprod.eps" /></p>
</div>
<figcaption>Composition of Hopf diagrams</figcaption>
</figure>

Let us denote by $\mathrm{RSL}$ the category of ribbon string links. The objects of $\mathrm{RSL}$ are the non-negative integers. For two non-negative integers $m$ and $n$, the set of morphisms from $m$ to $n$ is $$\mathrm{Hom}_{\mathrm{RSL}}(m,n)=\begin{cases} \emptyset & \text{if $m\neq n$,}\\ \mathrm{RSL}_n & \text{if $m=n$,} \end{cases}$$ where $\mathrm{RSL}_n$ denotes the set of (isotopy classes) of ribbon $n$-string links. The composition $T' \circ T$ of two ribbon $n$-string links is given by stacking $T'$ on the top of $T$ (i.e., with ascending convention). Identities are the trivial string links. Note that the category $\mathrm{RSL}$ is a monoidal category: $m \otimes n=m+n$ on objects and the monoidal product $T \otimes T'$ of two ribbon string links $T$ and $T'$ is the ribbon string link obtained by juxtaposing $T$ on the left of $T'$.

Hopf diagrams give a 'Hopf algebraic' description of ribbon string links. Indeed, any Hopf diagram $D$ with $n$ inputs gives rise to a ribbon $n$-string link $\Phi(D)$ in the following way: using the rules of Figure [5](#Hopf2Hand){reference-type="ref" reference="Hopf2Hand"}, we obtain a ribbon $n$-handle[^1] $h_D$, that is, a ribbon $(2n,0)$-tangle consisting of $n$ arc components, without any closed component, such that the $k$-th arc joins the $(2k-1)$-to the $2k$-th bottom endpoints. Then, by rotating $h_D$, we get a ribbon $n$-string link $\Phi(D)$: $$\text{$D$ Hopf diagram} \;\; \rightsquigarrow  \; \;   \psfrag{a}[cc][cc]{$h_D$} \raisebox{-.403\height}{\includegraphics[scale=.8]{defphi2a.eps}} \;\;
\rightsquigarrow \;\; \Phi(D)=\, \raisebox{-.403\height}{\includegraphics[scale=.8]{defphi2b.eps}} \; .$$ An example of this procedure is depicted in Figure [6](#exHopf2Hand){reference-type="ref" reference="exHopf2Hand"}.

This leads to a functor $\Phi\colon\mathcal{D}iag\to \mathrm{RSL}$ defined on objects by $n \mapsto \Phi(n)=n$ and on morphisms by $D \mapsto
\Phi(D)$.

::: thm
$\Phi\colon\mathcal{D}iag\to \mathrm{RSL}$ is a well-defined monoidal functor and there exists (constructive proof) a monoidal functor $\Psi\colon\mathrm{RSL}\to \mathcal{D}iag$ which satisfies $\Phi\circ\Psi=1_{\mathrm{RSL}}$.
:::

Note that by 'constructing proof' we mean there is an explicit algorithm that associates to a ribbon string $T$ a Hopf diagram $\Psi(T)$ such that $\Phi\bigl(\Psi(T) \bigr)=T$ (see [@BV1]). The key point is that such a functor $\Psi$ exists thanks to the relations we put on Hopf diagrams.\

<figure id="Hopf2Hand">
<div class="center">
<p>[Bl][Bl]<span>,</span> [Bl][Bl]<span>.</span> <embed src="defphi.eps" /></p>
</div>
<figcaption>Rules for transforming Hopf diagrams to tangles</figcaption>
</figure>

<figure id="exHopf2Hand">
<div class="center">
<p><span class="math inline"><em>D</em>=</span> <span class="math inline">⇝</span> <span class="math inline"><em>h</em><sub><em>D</em></sub>=</span> <span class="math inline">⇝</span> <span class="math inline"><em>Φ</em>(<em>D</em>)=</span>  <span class="math inline">∼</span>  </p>
</div>
<figcaption>From Hopf diagrams to ribbon string links</figcaption>
</figure>

Let now $\mathcal{B}$ be a ribbon autonomous category which admits a coend $C$. Let us answer to the second question of Section [\[sect-construct\]](#sect-construct){reference-type="ref" reference="sect-construct"}: given a ribbon $n$-string link $T$, how to compute the morphism $\phi_T\colon C^{\otimes n}\to
\mathbb{1}$ which is defined by universal property? Recall $C$ is a Hopf algebra in $\mathcal{B}$ and denote its coproduct, counit, and antipode by $\Delta_C$, $\varepsilon_C$, and $S_C$ respectively. The twist (and its inverse) of $\mathcal{B}$ is encoded by morphisms $\theta^\pm_C \to C \to \mathbb{1}$ (see Section [\[sect-kirby\]](#sect-kirby){reference-type="ref" reference="sect-kirby"}). Furthermore, we can defined a Hopf pairing $\omega_C
\colon C \otimes C \to \mathbb{1}$ via: $$\begin{aligned}
&\omega_C (i_X \otimes i_Y)=(\mathrm{ev}_X \otimes \mathrm{ev}_Y)(\mathrm{id}_{\leftidx{^\vee}{\!X}{}} \otimes \tau_{\leftidx{^\vee}{\!Y}{},X}\tau_{X,\leftidx{^\vee}{\!Y}{}} \otimes
\mathrm{id}_{\leftidx{^\vee}{\!Y}{}}),
\end{aligned}$$ where $\tau$ is the braiding of $\mathcal{B}$ and $i_Y \colon\leftidx{^\vee}{\!Y}{} \otimes Y \to C$ is the universal dinatural transformation of the coend $C$. Finally, we set $\omega_C^+=\omega_C(S_C^{-1} \otimes \mathrm{id}_C)$ and $\omega_C^-=\omega_C$.

::: thm
Let $T$ be ribbon $n$-string link. Let $D$ be any Hopf diagram (with $n$ entries) which encodes $T$, that is, such that $\Phi(D)=T$ (recall there is an algorithm producing such a Hopf diagram). Then the morphism $\phi_T\colon C^{\otimes n} \to
\mathbb{1}$ defined by $T$ is given by replacing in $D$ the generators $\Delta$, $\varepsilon$, $\omega_\pm$, $\theta_\pm$, $S^{\pm
1}$, and $\tau^{\pm 1}$ (see Figure [1](#gensHdiag){reference-type="ref" reference="gensHdiag"}) by the morphisms $\Delta_C$, $\varepsilon_C$, $\omega^\pm_C$, $\theta^\pm_C$, $S^{\pm 1}_C$, and $\tau^{\pm 1}_{C,C}$ respectively.
:::

Remark that the product and unit of the coend $C$ are not needed to represent Hopf diagrams.\
Let us summarize the above universal construction of quantum invariants, starting from a ribbon category $\mathcal{B}$ which admits a coend $C$. Pick a normalizable Kirby element $\alpha$ of $\mathcal{B}$ (for example as in Theorem [\[thmkirbel\]](#thmkirbel){reference-type="ref" reference="thmkirbel"}). Recall it gives rise to the invariant $\tau_\mathcal{B}(M,\alpha)$ of 3- manifolds. Let $M$ be a 3- manifold. Present $M$ by surgery along a framed link $L$, which can be viewed as the closure of a ribbon $n$-string link $T$ where $n$ is the number of components of $L$. Encode the string link $T$ by a Hopf diagram $D$: $$M\simeq S^3_L, \quad L\, \sim \psfrag{T}[c][c]{\scalebox{.72}{$T$}}\raisebox{-.38\height}{\scalebox{1}{\includegraphics{Tcirclittle.eps}}} \quad \text{with} \quad
T=\,\raisebox{-.38\height}{\scalebox{1}{\includegraphics{TLittle.eps}}} \; \scalebox{-1.1}[1.1]{$\mapsto$ \,}\quad D=\raisebox{-.38\height}{\scalebox{1}{\includegraphics{petit-InvPoinc1.eps}}}$$ The morphism $\phi_T\colon C^{\otimes n} \to \mathbb{1}$ associated to $T$ can be computed by replacing the generators of $D$ by the corresponding structural morphisms of the coend $C$. Then evaluate $\phi_T$ with the Kirby element $\alpha$ and normalize to get the invariant: $$\tau_\mathcal{B}(M;\alpha)=\;\psfrag{w}[c][c]{\scalebox{.8}{$\omega^-_C$}} \psfrag{m}[c][c]{\scalebox{.8}{$\omega^+_C$}}
\psfrag{o}[c][c]{\scalebox{.8}{$S_C$}} \psfrag{c}[c][c]{\scalebox{.8}{$\tau_{C,C}$}}
\psfrag{D}[c][c]{\scalebox{.8}{$\Delta_C$}} \psfrag{a}[c][c]{\scalebox{.9}{$\alpha$}}
\psfrag{t}[c][c]{\scalebox{.8}{$\theta^+_C$}} \psfrag{r}[c][c]{\scalebox{.8}{$\theta^-_C$}}
\psfrag{x}[Bl][Bl]{\scalebox{.8}{$b_-(L)-n$}} \psfrag{u}[Bl][Bl]{\scalebox{.8}{$-b_-(L)$}}\raisebox{-.403\height}{\includegraphics[scale=.8]{InvPoinct+.eps}}
\qquad \quad\;\;\raisebox{-.403\height}{\includegraphics[scale=.8]{InvPoinct-.eps}} \quad \qquad\raisebox{-.403\height}{\includegraphics[scale=.8]{InvPoinc.eps}}$$

In particular, to compute such quantum invariants defined from the center $\mathcal{Z}(\mathcal{C})$ of a autonomous category $\mathcal{C}$, one needs to give an explicit description of the structural morphism of the coend of $\mathcal{Z}(\mathcal{C})$ in terms of the category $\mathcal{C}$. In the next section, we give such a description by using Hopf monads (this was our original motivation for introducing Hopf monad).

[^1]: Ribbon handles are called bottom tangles in [@Hab1].
