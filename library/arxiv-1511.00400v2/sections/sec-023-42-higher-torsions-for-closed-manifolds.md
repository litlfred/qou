---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-023-42-higher-torsions-for-closed-manifolds
section_title: "Higher torsions for closed manifolds"
section_number: 4.2
pages: 27-29
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.994
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sect:higher label="sect:higher"}

From Theorem [\[thm:rig\]](#thm:rig){reference-type="ref" reference="thm:rig"}, we can define torsions.

::: definition
Let $M^3$ be a closed oriented hyperbolic three-manifold, with spin structure $\sigma$, and let $\varrho_\sigma^{k_1,k_2}=    \operatorname{Sym}^{k_1,k_2}\circ        \varrho_\sigma$ be as in [\[eqn:varrho\]](#eqn:varrho){reference-type="eqref" reference="eqn:varrho"}.

For $k_1\neq k_2$, define $$\label{eqn:taukk}
  \tau^{k_1,k_2}(M^3,\sigma):=\operatorname{tor}(M^3,  \varrho_\sigma^{k_1,k_2} )  \in 
\mathbb{C}^*/{\pm 1}\, ,$$ and for $k\geq 1$ $$\label{eqn:tauk}
   \tau^{k}(M^3,\sigma):= \tau^{k,0}(M^3,\sigma)= \operatorname{tor}(M^3,  \varrho_\sigma^{k})   .$$
:::

When $k=1$ one obtains the torsion of Definition [\[defn:tor2closed\]](#defn:tor2closed){reference-type="ref" reference="defn:tor2closed"}: $$\tau^1(M^3,\sigma)=\tau^{1,0}(M^3,\sigma)=\tau(M^3,\sigma).$$

::: remark
1.  For $k_1$ or $k_2$ odd, there is no sign indeterminacy as it is a representation in $\mathbb{C}^{(k_1+1)(k_2+1)}$, which is even dimensional (Remark [\[rem:sign\]](#rem:sign){reference-type="ref" reference="rem:sign"}).

2.  For $k_1+k_2$ even, $\operatorname{Sym}^{k_1}\otimes \overline{\operatorname{Sym}^{k_2}}$ factors through $\operatorname{PSL}_2(\mathbb{C})$, hence it does not depend on the spin structure. In addition, the sign indeterminacy can be avoided by using Turaev's refined torsion and an orientation in homology, provided by Poincar� duality [@Turaev01; @Turaev02].

3.  By construction, $\tau^{k_1,k_2}(M^3,\sigma)=\overline{\tau^{k_2,k_1}(M^3,\sigma)}$.

4.  When $k_1=k_2$, $\varrho^{k,k}$ may be not acyclic (for instance when it contains a totally geodesic surface [@Millson85]), but sometimes it can be acyclic (e.g. almost all Dehn fillings on two bridge knots for $k=1$ by [@Kapovich94; @Scannell02; @StefanoP08] or on the figure eight knot for $k=2$ by [@Heusener-Porti2011]). When $\varrho^{k,k}$ is acyclic, then $\tau^{k,k}(M^3,\sigma)$ is also well defined.

5.  Changing the orientation. Let $M^3$ and $\overline M^3$ denote the same manifold with opposite orientations and let $\sigma$ and $\overline\sigma$ denote the corresponding spin structures as in Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}. Then $$\tau^{k_1,k_2}(\overline M^3, \overline \sigma)= (-1)^{b_1(M^3) (k_1+k_2)}\, \overline{ \tau^{k_1,k_2}(M^3,\sigma)}.$$ where $b_1(M^3)$ denotes the first Betti number. Hence if $M^3$ is amphicherical, then $\tau^{k_1,k_2}(M^3,\sigma)$ is real for $b_1(M^3) (k_1+k_2)$ even and purely imaginary for $b_1(M^3) (k_1+k_2)$ odd.
:::

In [@Muller12] W. Müller found a beautiful theorem about the asymptotic behavior when $k\to\infty$:

::: thm
[]{#thm:Muller label="thm:Muller"} Let $M$ be a compact, oriented, hyperbolic 3 manifold with a spin structure $\sigma$. Then $$\label{eqn:muller}
 \lim_{k\to\infty} \frac{ \log\vert  \tau^{k}(M^3,\sigma)\vert}{k^2} = \frac 
1{4\pi}\operatorname{vol} (M^3)\, .$$ In particular, the volume can be computed from the sequence of torsions.
:::

Again, with our convention our torsion is the inverse of the usual analytic torsion, so Equation [\[eqn:muller\]](#eqn:muller){reference-type="eqref" reference="eqn:muller"} has opposite sign to [@Muller12].

As noticed in [@Muller12], this theorem implies that there are finitely many manifolds with the same sequence of torsions.

::: question
Is there a finite collection of integers $0<k_1<\cdots<k_n$ such that there are finitely many manifolds with the same $k_1,\ldots, k_n$-torsions?
:::

The answer is yes under the extra hypothesis that the volume is bounded above. More precisely, an infinite sequence of manifolds with bounded volume accumulates (for the geometric topology) to a finite set of cusped manifolds with finite volume, this is Jørgensen-Thurston properness of the volume function [@ThurstonBullAMS; @ThurstonBook]. For such a sequence of manifolds $M_n^3$, $\tau^2(M_n^3,\sigma)\to \infty$, by Corollary [\[cor:denseh\]](#cor:denseh){reference-type="ref" reference="cor:denseh"}, see also [@Memoirs Corollaire 4.18].

A priory, for some $N\in \mathbb{N}$ there could exists an infinite sequence of hyperbolic manifolds whose volume goes to infinity and with the same $k$-torsions for $k\leq N$. By Theorem [\[thm:BV\]](#thm:BV){reference-type="ref" reference="thm:BV"} the injectivity radius of this sequence would not converge to infinity.

Müller proves Theorem [\[thm:Muller\]](#thm:Muller){reference-type="ref" reference="thm:Muller"} using analytic torsion and Ruelle zeta functions. There is first a theorem of Wotzke [@Wot08] that generalizes Fried's theorem (Theorem [\[thm:Fried\]](#thm:Fried){reference-type="ref" reference="thm:Fried"}) and from this he obtains a functional equation that relates the volume, the Ruelle zeta functions and the torsions. Theorem [\[thm:Muller\]](#thm:Muller){reference-type="ref" reference="thm:Muller"} has been generalized by Müller and Pfaff [@MullerPfaff14] by working directly on the trace of the heat kernel in [\[eqn:traceheatkernel\]](#eqn:traceheatkernel){reference-type="eqref" reference="eqn:traceheatkernel"}.

::: thm
Let $M^3$ be a compact, oriented, hyperbolic 3-manifold with a spin structure $\sigma$. Then $$\lim_{k_1\to\infty} \frac{ \log\vert \tau^{k_1,k_2}(M^3,\sigma)\vert}{k_1^2} = 
\frac 1{4\pi}(k_2+1)\operatorname{vol} (M^3)\, .$$
:::

Again, the sign convention here differs from [@MullerPfaff14].
