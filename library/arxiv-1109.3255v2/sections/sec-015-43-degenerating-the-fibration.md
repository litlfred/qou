---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-015-43-degenerating-the-fibration
section_title: "Degenerating the fibration"
section_number: 4.3
pages: 38-40
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.975
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:degenerated-spaces label="sec:degenerated-spaces"}

By propositions [\[prop:triangles-sections\]](#prop:triangles-sections){reference-type="ref" reference="prop:triangles-sections"} and [\[prop:extended-sections\]](#prop:extended-sections){reference-type="ref" reference="prop:extended-sections"}, in order to compute the Floer product between two morphisms $q_1 \in HF^0(L(0),L(n))$ and $q_2 \in
HF^0(L(n),L(n+m))$, it is just as good to count sections of the fibration $\hat{X}_T \to T$ with Lagrangian boundary conditions $\hat{L}(0)$, $\hat{L}(n)$, $\hat{L}(n+m)$.

In order to obtain these counts, we will consider a degeneration of the Lefschetz fibration. We consider a one-parameter family of Lefschetz fibrations $\hat{X}^r \to T^r$, which for $r = 1$ is simply the one we started with. As $r$ goes to zero, the fibration deforms so that all of the $k$ critical values contained within $T$ move toward the side of $T$ corresponding to $\ell(n)$. In the limit, a disc bubble appears around each critical value, and at $r = 0$, the base $T$ has broken into a $(k+3)$-gon, with $k$ "new" vertices along the side corresponding to $\ell(n)$, each of which joins to a disk with a single critical value. We can equip each fibration with Lagrangian boundary conditions varying continuously with $r$, and degenerating to a collection of Lagrangian boundary conditions for each of the component fibrations at $r = 0$.

The base of the Lefschetz fibration undergoes the degeneration shown in figure [1](#fig:degeneration){reference-type="ref" reference="fig:degeneration"}. This figure shows specifically the case for the product of $x \in CF^*(L(0),L(1))$ and $z \in
CF^*(L(1),L(2))$. The marked point on the upper portion is the Lefschetz critical value, while the marked points on the lower portion are the Lefschetz critical value and a node.

![Degenerating the fibration.](degeneration){#fig:degeneration width="1.5in"}

When performing this construction carefully, it is better to describe this family as a smoothing of the degenerate $r = 0$ end. Let $T^0$ be a disk with $(k+3)$ boundary punctures. We emphasize that the conformal structure of $T^0$ is fixed. Let $\hat{X}^0 \to T^0$ be a symplectically trivial Lefschetz fibration. Let $D_1,\dots,D_k$ denote the $k$ disks with one boundary puncture that are our "bubbles". For each $i$ let $E_i \to D_i$ denote a Lefschetz fibration with a single critical value, and which is trivial near the puncture. Let the symplectic monodromy around $\partial D_i$ be denoted $\tau_i$.

We will equip each of the components of this fibration with a Lagrangian boundary condition as follows.

-   The base $T^0$ has one boundary component corresponding to $\ell(0)$, one boundary component corresponding to $\ell(n+m)$, and $(k+1)$ boundary components corresponding to $\ell(n)$. Since the fibration $\hat{X}^0 \to T^0$ is trivial, it suffices to describe each boundary condition in the fiber. Over the point where $\ell(0)$ and $\ell(n+m)$ come together, we identify the fiber with that of $\hat{X}^1 \to T^1$, and take $\hat{L}(0)^0$ and $\hat{L}(n+m)^0$ to be the corresponding Lagrangians.

-   Over the $k+1$ boundary components of $T^0$ corresponding to $\ell(n)$, we construct a sequence $\hat{L}(n)^0_i$ of Lagrangians. At the puncture where $\ell(0)$ and $\ell(n)$ come together, we take $\hat{L}(n)^0_0$ to have the same position relative to $\hat{L}(0)^0$ (already constructed) that $\hat{L}(n)$ has relative to $\hat{L}(0)$ in the original fibration. As we pass each of the new punctures where the disks are attached, the monodromies $\tau_i$ must be applied. So we let $$\label{eq:Ln-twists}
        \hat{L}(n)^0_i = \tau_i(\hat{L}(n)^0_{i-1})$$ This can be done so that, over the puncture where $\ell(n)$ and $\ell(n+m)$ come together, $\hat{L}(n)^0_k$ and $\hat{L}(n+m)^0$ intersect as the original $\hat{L}(n)$ and $\hat{L}(n+m)$ do.

-   Over the $k$ disks $D_i$, we take a Lagrangian boundary condition which interpolates between $\hat{L}(n)^0_{i-1}$ and $\hat{L}(n)^0_i$. This is possible because each $D_i$ contains a single Lefschetz critical value.

Note that at this stage we only care about the twists $\tau_i$ up to Hamiltonian isotopy, but we will make a particular choice in §[\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"}, as required by the technical considerations there. This gives us $\tau_i$ such that $\hat{L}(n)^0_{i-1}$ and $\hat{L}(n)^0_i$ have one intersection point over $i$-th new puncture of $T^0$.

Since the boundary conditions agree over the corresponding punctures, we can glue the components over $T^0$ and $D_1,\dots,D_k$ with large gluing length in order to obtain $\hat{X}^\epsilon \to T^\epsilon$ for small $\epsilon > 0$, which has three boundary components and $k$ critical values all near the $\ell(n)$ boundary. There is a family of Lefschetz fibrations interpolating between $\hat{X}^\epsilon
\to T^\epsilon$ back to our original $\hat{X}^1 \to T^1$, along which the critical values move back to their original points.

We equip $T^0$ and $D_1,\dots,D_k$ with complex structures, and equip $T^\epsilon$ with a family of complex structures $j^\epsilon$ converging to those in the limit. All total spaces are equipped with relatively compatible almost complex structures.

Now we appeal to the gluing theorem [@seidel-les Proposition 2.2] telling us how the curve counts behave under the degeneration.

::: proposition
[]{#prop:TQFT-gluing label="prop:TQFT-gluing"} The count of pseudo-holomorphic sections of $\hat{X}^1 \to T^1$, with Lagrangian boundary conditions $\hat{L}(d)$, $d = 0 ,n ,n+m$ is obtained from the counts of sections of $\hat{X}^0 \to T^0$ and $E_i
  \to D_i$ by gluing together sections whose values over the punctures match.
:::

::: proof
*Proof.* Considering pseudo-holomorphic sections of the fibrations $\hat{X}^\epsilon \to T^\epsilon$, as long as the gluing length is large, the sections for $r = \epsilon$ will be obtained from sections over $T^0$ and $D_1,\dots,D_k$ by gluing sections with matching values at the punctures [@seidel-les Proposition 2.2]. During the deformation from $r = \epsilon$ to $r =
1$, no Floer strip breaking can occur because our Lagrangians $\hat{L}(d)$, $d = 0, n, n+m$ do not bound any strips, even topologically, so the count remains the same at $r = 1$. ◻
:::
