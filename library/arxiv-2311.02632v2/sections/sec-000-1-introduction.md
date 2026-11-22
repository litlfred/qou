---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.99
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In 1893, Hurwitz proved that a compact Riemann surface $X$ of genus $g \geq 2$ has at most $84(g - 1)$ conformal automorphisms [@hurwitz1893]. This upper bound is now known as the Hurwitz bound, and a Riemann surface attaining this bound is called a Hurwitz surface.

Notably, for Riemann surfaces of low genera, those meeting the Hurwitz bound are rare. One prominent example is the Klein quartic [@Klein79], described by the equation $$x_0^3x_1 + x_1^3x_2 + x_2^3x_0 = 0,$$ in complex projective space. The Klein quartic predates Hurwitz's seminal work and stands as the first of its kind to have ever been discovered. This surface possesses 168 conformal automorphisms, with its automorphism group being isomorphic to the simple group $\PSL_2(7)$. For a comprehensive exploration of the history and significance of Klein's quartic, as well as the subsequent advancements inspired by it, one can refer to [@MR1722410].

In 1899, Fricke made a significant contribution to the subject by unveiling another Hurwitz surface, particularly one of genus 7 [@MR1511059]. This surface possesses the automorphism group $\PSL_2(8)$, a simple group of order 504. Subsequently, in 1965, without being aware of Fricke's earlier work, Macbeath determined its algebraic model [@macbeath1965]. This surface is now known as the Fricke-Macbeath surface, and alongside the Klein quartic, it holds the distinction of being one of the only two instances of Hurwitz surfaces with genera less than 14. Interestingly, in the case of genus 14, there exist three distinct Hurwitz surfaces with the same automorphism group of order 1092.

The abundant symmetries inherent in Hurwitz surfaces facilitates intriguing interactions with various structures associated with a surface, making their study compelling. This interplay makes Hurwitz surfaces a fertile ground for researchers across diverse fields. Notably, in the realm of arithmetic, some of these surfaces hold significant recognition as Shimura curves, a fact highlighted by Shimura [@MR0204426]. Their connection with Galois theory is also a subject of discussion in Serre's enlightening letter to Abhyankar [@MR1272022]. For their role in the theory of dessins d'enfants, see the book by Jones and Wolfart [@MR3467692].

In this paper, we explore the interaction between symmetries and the spectral properties of such a surface. According to the uniformization theorem, $X$ is conformally equivalent to $\Gamma\backslash \uhp$, where $\uhp$ is the upper half-plane in the complex plane and $\Gamma$ is discrete, torsion-free subgroup of $\PSL_2(\R)$. Then $\Aut(X) \cong N(\Gamma) / \Gamma$, where $N$ is the normalizer of $\Gamma$ in $\PSL_{2}(\R)$. In particular, $X$ is a Hurwitz surface when $N(\Gamma)$ is the $(2,3,7)$-triangle group. Now $X$ admits a hyperbolic metric, namely, the Riemannian metric of constant Gaussian curvature -1. The elements of $\Aut(X)$ act as orientation-preserving isometries of $X=\Gamma\backslash \uhp$. The Laplacian $\Delta$ for $X$ has non-negative discrete eigenvalues $$0=\la_0< \la_1 \leq \la_2 \leq \ldots \to \infty.$$ An interesting feature of a Riemann surface with many automorphisms is that each eigenspace of the Laplacian can exhibit high multiplicities, as each of these eigenspaces of the Laplacian serves as a representation of $\Aut(X)$.

There are only a few known cases of Riemann surfaces with non-trivial automorphism groups for which we have established values for the multiplicities $m_1$ of $\la_1$. To the best of our knowledge, the Bolza surface and the Klein quartic are the only known cases. The Bolza surface, despite not meeting the Hurwitz bound, is a genus 2 Riemann surface renowned for having the highest number of conformal symmetries, totaling 48, within its genus. In a study by Jenni [@jenni1984], it was asserted that $m_1=3$ for the Bolza surface; however, Cook [@cook2018] identified a gap in its proof. Cook subsequently narrowed down the possible range to $3 \leq m_1 \leq 4$. A subsequent investigation conducted in [@FBP21] successfully confirmed that the correct value for $m_1$ is indeed 3. Concerning the Klein quartic, Cook's analysis indicated that the multiplicity of the first eigenvalue lies within the range of 6 to 8. A rigorous proof establishing $m_1=8$ is also provided in [@FBP21].

Surfaces with many automorphisms like the Bolza surface and the Klein quartic often emerge as solutions to extremal problems concerning both $m_1$ and $\la_1$. In  [@FBP21], it was shown that the Klein quartic attains the maximal $m_1$ among all hyperbolic surfaces of genus 3. In a work by Strohmaier and Uski [@MR3009726], they conjectured that the Bolza surface maximizes $\la_1$ among all hyperbolic surfaces of genus 2 based on numerical experiments. A recent study [@kravchuk2023automorphic] provides additional evidence supporting the conjecture that both the Bolza surface and the Klein quartic maximize $\la_1$ among hyperbolic surfaces of genus 2 and 3, respectively.

Our main result is as follows:

::: thmnn
The multiplicity of the first eigenvalue $\la_1$ of the Fricke-Macbeath surface is 7, and $\la_1\in [1.23, 1.26]$.
:::

Our primary tool for the proof is the Selberg trace formula. We make use of Vogeler's results [@Vogeler2003] concerning the length spectrum of the Fricke-Macbeath surface, specifically, we require information about the conjugacy classes of the two shortest lengths in the spectrum. When applying the Selberg trace formula, we utilize various types of test functions. These include the functions featured in [@MR2338122 Section 4] and [@MR4186122 Section 5], which played a crucial role in confirming the Selberg eigenvalue conjecture for numerous congruence subgroups with small conductor. We also employ the test functions introduced in the context of the sphere packing problem [@MR1973059 Section 7], which were recently employed in the investigation of spectral properties of hyperbolic surfaces in [@FBP21].

After establishing the multiplicity of an eigenvalue, the subsequent natural question is to identify the associated eigenspace as a representation. To address this, we present a numerical method for computing the character of a representation obtained from a set of eigenfunctions. This method enables us to formulate a conjecture regarding which 7-dimensional representation of $\PSL_2(8)$ corresponds to the representation associated with $\la_1$ of the Fricke-Macbeath surface; see Conjecture [\[conj:rep7\]](#conj:rep7){reference-type="ref" reference="conj:rep7"}. The application of these algorithms to compute the characters for other Riemann surfaces with many automorphisms will be discussed in a separate work.

To conduct a numerical calculation based on the finite element method, we determine a fundamental domain for the Fuchsian group that uniformizes the Fricke-Macbeath surface using Poincaré's polyhedron theorem [@maskit1971], along with its side-pairing transformations. It is a hyperbolic polygon with 42 sides, which is actually the Dirichlet domain centered at 0. We offer a visualization of this fundamental domain, updating the classic Fricke-Klein illustration [@MR0352287]; see Figures [\[fig:fricke_tess1\]](#fig:fricke_tess1){reference-type="ref" reference="fig:fricke_tess1"} and [1](#fig:fricke_tess2){reference-type="ref" reference="fig:fricke_tess2"} for a comparison. Unlike the case of the Klein quartic in Figure [\[fig:237_klein\]](#fig:237_klein){reference-type="ref" reference="fig:237_klein"}, we find that this polygon is not completely tessellated by the fundamental $(2,3,7)$-triangles. We note that the fundamental domain discussed in  [@MR1511059] differs from ours.

<figure id="fig:fricke_tess2">
<img src="fricke_tess1.jpg" />
<img src="fricke_tess2.png" />
<figcaption>Fundamental domain for the Fricke-Macbeath surface (boundary in thick lines)</figcaption>
</figure>

The paper is organized as follows. In Section 2, we delve into the background, discussing topics like the Laplacian on a Riemannian manifold, the hyperbolic plane, and the Selberg trace formula. Section 3 focuses on presenting an explicit uniformization of the Fricke-Macbeath surface and the identification of its fundamental domain. In Section 4, we prove our main result on the first eigenvalue of the Fricke-Macbeath surface. Lastly, in Section 5, we present a numerical method to determine the character of a representation obtained from a set of eigenfunctions, and propose a conjecture identifying the 7-dimensional representation of $\PSL_2(8)$ associated to the first eigenvalue of the Fricke-Macbeath surface.

The accompanying computer code for this paper is available at <https://github.com/chlee-0/fricke_macbeath>.
