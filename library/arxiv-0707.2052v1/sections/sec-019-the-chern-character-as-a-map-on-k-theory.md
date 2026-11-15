---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-019-the-chern-character-as-a-map-on-k-theory
section_title: "The Chern character as a map on K-theory."
section_number: null
pages: 22-24
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#subsec:iotae label="subsec:iotae"} To show that the Chern character descends to a map on K-theory we give a characterization of the Chern character similar to that of Markarian [@Mar].

For any object ${\mathscr E}\in \mathbf{D}(X)$, which is to be considered an object of $\mathbf{D}( {\mathsf{pt}}\times X)$, there are the following two maps: $$\iota_{\mathscr E}\colon \mathop{\mathrm{HH}}_\bullet(X)\to \mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^\bullet({\mathscr E},\Sigma_X\circ {\mathscr E});
\qquad\raisebox{-.45\height}{}\,\mapsto \,\raisebox{-.45\height}{}$$ and $$\iota^{\mathscr E}\colon \mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^\bullet({\mathscr E},{\mathscr E})\to\mathop{\mathrm{HH}}_\bullet(X);
\qquad\raisebox{-.45\height}{}\mapsto \,\raisebox{-.45\height}{}.$$

Recall that the Mukai pairing is a non-degenerate pairing on $\mathop{\mathrm{HH}}_\bullet(X)$ and that the Serre pairing is a perfect pairing between $\mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^\bullet({\mathscr E},\Sigma_X\circ {\mathscr E})$ and $\mathop{\mathrm{Hom}}_{\mathbf{D}(X\times X)}^\bullet({\mathscr E},{\mathscr E})$.

With respect to these pairings the two maps $\iota^{\mathscr E}$ and $\iota_{\mathscr E}$ are adjoint in the following sense.

::: Proposition
[]{#prop:iotasadjoint label="prop:iotasadjoint"} For $\varphi\in \mathop{\mathrm{Hom}}^\bullet({\mathscr E},{\mathscr E})$ and $v\in \mathop{\mathrm{HH}}_\bullet(X)$ the following equality holds: $$\langle v,\, \iota^{\mathscr E}\varphi\rangle_{\rm M} ={\ensuremath{\left\langle \iota_{\mathscr E}v,\, \varphi\right\rangle_{\rm S}}}$$
:::

::: Proof
Here in the third equality we use the invariance of the Serre trace under the partial trace map. $$\begin{aligned}
    {\ensuremath{\left\langle v,\, \iota^{\mathscr E}\varphi\right\rangle_{\rm M}}}&=
    {\ensuremath{\Biggl\langle \raisebox{-.45\height}{},\, \raisebox{-.45\height}{}\Biggr\rangle_{\rm M}}}
    :=\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)\\&=
    \mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)
    =\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)\\
    &=: {\ensuremath{\Biggl\langle \raisebox{-.45\height}{}\quad,\, \quad\raisebox{-.45\height}{}\Biggr\rangle_{\rm S}}} =:{\ensuremath{\left\langle \iota_{\mathscr E}
      v,\, \varphi\right\rangle_{\rm S}}}.\qedhere
  
\end{aligned}$$
:::

Note that, using this, the Chern character could have been defined as $$\mathop{\mathrm{ch}}({\mathscr E}):=\iota^{\mathscr E}(\mathsf {Id}_{\mathscr E}).$$ Then from the above proposition the following is immediate.

::: Lemma
For $v\in \mathop{\mathrm{HH}}_0(X)$ and ${\mathscr E}\in \mathbf{D}(X)$ there is the equality $${\ensuremath{\left\langle v,\, \mathop{\mathrm{ch}}({\mathscr E})\right\rangle_{\rm M}}}=\mathop{\mathrm{Tr}}(\iota_{\mathscr E}(v)),$$ and this defines $\mathop{\mathrm{ch}}({\mathscr E})$ uniquely.
:::

The fact that the Chern character descends to a function on the K-group can now be demonstrated.

::: Proposition
For ${\mathscr E}\in \mathbf{D}(X)$ the Chern character $\mathop{\mathrm{ch}}({\mathscr E})$ depends only on the class of ${\mathscr E}$ in $\mathop{\mathrm{K}}_0(X)$. Thus the Chern character can be considered as a map $$\mathop{\mathrm{ch}}\colon \mathop{\mathrm{K}}_0(X) \rightarrow\mathop{\mathrm{HH}}_0(X).$$
:::

::: Proof
It suffices to show that if ${\mathscr F}\rightarrow{\mathscr G}\rightarrow{\mathscr H}\rightarrow{\mathscr F}[1]$ is an exact triangle in $\mathbf{D}(X)$, then $$\mathop{\mathrm{ch}}({\mathscr F}) - \mathop{\mathrm{ch}}({\mathscr G}) + \mathop{\mathrm{ch}}({\mathscr H}) = 0$$ in $\mathop{\mathrm{HH}}_0(X)$.

For ${\mathscr G},{\mathscr H}\in \mathbf{D}(X)$, $\alpha \colon {\mathscr G}\to {\mathscr H}$ and $v\in
  \mathop{\mathrm{HH}}_\bullet(X)$ the diagram on the left commutes as it expresses the equality on the right: $$\begin{diagram}[height=2em,width=2em]
    {\mathscr G}& \rTo^{\alpha} & {\mathscr H}\\
    \dTo^{\iota_{\mathscr G}( v)} & &
    \dTo_{\iota_{\mathscr H}( v)}  \\
    \Sigma_X \circ{\mathscr G}& \rTo^{\mathsf {Id}_{\Sigma_X}\circ \alpha} & \Sigma_X
    \circ{\mathscr H}.
  \end{diagram}\qquad;\qquad\raisebox{-.45\height}{}\ =\ \raisebox{-.45\height}{}\ .$$ In other words, from an element $v\in \mathop{\mathrm{HH}}_\bullet(X)$ we get $\tau_R(v)\in \mathop{\mathrm{Hom}}(\mathsf {Id}_X,\Sigma_X)$, which in turn gives rise to a natural transformation between the functors $\mathsf {Id}_{\mathbf{D}(X)}\colon \mathbf{D}(X)\to
  \mathbf{D}(X)$ and $\Sigma_X\circ{-}\colon \mathbf{D}(X)\to \mathbf{D}(X)$. This leads to a map of triangles $$\begin{diagram}[height=2em,width=2em]
    {\mathscr F}& \rTo & {\mathscr G}& \rTo & {\mathscr H}& \rTo & {\mathscr F}[1] \\
    \dTo_{\iota_{\mathscr F}( v)} & & \dTo_{\iota_{\mathscr G}( v)} & &
    \dTo_{\iota_{\mathscr H}( v)} & & \dTo_{\iota_{\mathscr F}( v)[1]} \\
    S_X {\mathscr F}& \rTo & S_X {\mathscr G}& \rTo & S_X {\mathscr H}& \rTo & S_X {\mathscr F}[1].
  \end{diagram}$$ Observe that if we represent the morphism $v$ by an actual map of complexes of injectives, and the objects ${\mathscr F}$, ${\mathscr G}$ and ${\mathscr H}$ by complexes of locally free sheaves, then the resulting maps in the above diagram commute on the nose (no further injective or locally free resolutions are needed), so we can apply [@May Theorem 1.9] to get $$\mathop{\mathrm{Tr}}_X(\iota_{\mathscr F}( v)) - \mathop{\mathrm{Tr}}_X(\iota_{\mathscr G}( v)) + \mathop{\mathrm{Tr}}_X(\iota_{\mathscr H}(
  v)) = 0.$$ Therefore, by the lemma above, for any $v\in
  \mathop{\mathrm{HH}}_\bullet(X)$, $${\ensuremath{\left\langle v,\, \mathop{\mathrm{ch}}({\mathscr F})-\mathop{\mathrm{ch}}({\mathscr G})+\mathop{\mathrm{ch}}({\mathscr H})\right\rangle_{\rm M}}}= 0 .$$ Since the Mukai pairing on $\mathop{\mathrm{HH}}_0(X)$ is non-degenerate, we conclude that $$\mathop{\mathrm{ch}}({\mathscr F}) - \mathop{\mathrm{ch}}({\mathscr G}) + \mathop{\mathrm{ch}}({\mathscr H}) = 0. \qedhere$$
:::
