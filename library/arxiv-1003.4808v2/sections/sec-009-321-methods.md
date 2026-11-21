---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-009-321-methods
section_title: "Methods"
section_number: 3.2.1
pages: 18-21
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.971
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
The problem of quantization can be approached in many different ways. Each approach has its advantages and disadvantages, but in the end all methods are expected to yield the same result. The classic approach of *geometric quantization* (*cf.* [@woodhouse-1992]) starts by defining a prequantum line bundle $L \to {\cal M}$ with a unitary connection of curvature $\frac{1}{\hbar}\omega$. Note that such a line bundle only exists for

$$\frac{1}{2\pi\hbar}\omega\in H^2({\cal M};{\mathbb{Z}})\,, \label{wquant}$$

which can lead to a quantization of $\hbar^{-1}$ (*i.e.* a restriction of $\hbar$ to a discrete set of values in ${\mathbb{C}}^*$). The local choice of "position" versus "momentum" coordinates is encoded in the choice of a set of $\frac12\dim_{\mathbb{R}}{\cal M}$ vector fields ${\cal P}_j$, called a polarization, and the Hilbert space ${\cal H}$ is then defined as the set of square-integrable, ${\cal P}_j$-invariant sections of ${\cal L}$. This gives a very concrete definition of ${\cal H}$, although it can be very hard to show that the construction is independent of the choice of polarization. (The problem becomes more manageable if ${\cal M}$ is Kähler.) Moreover, it is often difficult in geometric quantization to find the full quantum expressions for operators ${\cal O}_{f_i}$.\
An alternative, *deformation quantization* [@bayen-def] partially solves this latter problem. It describes a formal $\hbar$-deformation of the ring of functions on ${\cal M}$, using a noncommutative product of the type $$\begin{aligned}
f \star_\hbar g & = & f g + \hbar \sum_{i,j} \alpha^{ij} \partial_i (f) \partial_j (g)
+ \frac{\hbar^2}{2} \sum_{i,j,k,l} \alpha^{ij} \alpha^{kl} \partial_i \partial_k (f) \partial_j \partial_l (g) \nonumber\\
& & + \frac{\hbar^2}{3} \left(\sum_{i,j,k,l} \alpha^{ij} \partial_j (\alpha^{kl}) (\partial_i \partial_k (f) \partial_l (g) - \partial_k (f)
\partial_i \partial_l (g)) \right) + \ldots,
\label{starproduct}
\end{aligned}$$

where $\alpha = \omega^{-1}$ is the Poisson structure corresponding to the symplectic form $\omega$. In local coordinates $\{ f,g \} = \alpha^{ij} \partial_i (f) \partial_j (g)$.

One important advantage of deformation quantization is that it is completely canonical and does not require any auxiliary choices. In particular, there is an explicit formula for the $\star_\hbar$-product [\[starproduct\]](#starproduct){reference-type="eqref" reference="starproduct"} due to Kontsevich [@kont-poisson], that allows one to express it as a sum over *admissible graphs*,

$$f \star_\hbar g := \sum_{n=0}^\infty \hbar^n \sum_{{{\rm graphs}\;\Gamma \atop {\rm of~order}\; n}}
w(\Gamma) B_\Gamma(f,g)\,,
\label{kproduct}$$

where $w(\Gamma)$ is a weight (number) assigned to $\Gamma$, and $B_\Gamma (f,g)$ are bilinear differential operators whose coefficients are differential polynomials, homogeneous of degree $n$ in the components of the bivector field $\alpha$ on ${\cal M}$. By definition, an admissible graph of order $n$ is an ordered pair of maps $i,j : \{ 1, \ldots , n \} \to \{1, \ldots , n, L, R \}$ where neither map has fixed points and both maps are distinct at every point. There are $n^n (n+1)^n$ such graphs.

For example, the graph of order 2 corresponding to the first term in the second line of eq. [\[starproduct\]](#starproduct){reference-type="eqref" reference="starproduct"} has 4 vertices and 4 edges:

$$\Gamma ~=~
\raisebox{-1.2cm}{\includegraphics[width=3.0cm]{Pgraph1}}
\qquad\qquad
\begin{array}{c}
i_1 = (1,2) \\
j_1 = (1,L) \\
i_2 = (2,L) \\
j_2 = (2,R)
\end{array}$$

An example of a more complicated admissible graph (of order 4) is shown on Figure [1](#fig:Pgraph){reference-type="ref" reference="fig:Pgraph"}. The corresponding bidifferential operator is $$B_\Gamma (f,g) = \sum \alpha^{i_4 j_4} (\partial_{i_3} \alpha^{i_1 j_1}) (\partial_{j_1} \partial_{j_4} \alpha^{i_2 j_2})
(\partial_{i_2} \partial_{i_4} \alpha^{i_3 j_3}) (\partial_{i_1} \partial_{j_3} f) (\partial_{j_2} g)\,.$$

When the Poisson structure is flat, a graph with an edge ending in a vertex other than $L$ or $R$ will have zero contribution to the sum [\[kproduct\]](#kproduct){reference-type="eqref" reference="kproduct"}, since it will involve derivatives of $\alpha$. In this case the $\star_{\hbar}$-product [\[kproduct\]](#kproduct){reference-type="eqref" reference="kproduct"} becomes the usual Moyal product $$f \star_{\hbar} g (x) = \exp \left( \hbar \alpha^{ij} \frac{\partial}{\partial x^i} \frac{\partial}{\partial y^j} \right) f(x) g(y) \vert_{y=x}
\label{moyal}$$

![An example of an admissible graph of order 4.](Pgraph2){#fig:Pgraph width="1.5in"}

Deformation quantization is a powerful method for finding the operators ${\cal O}_{f_i}$. It is important to stress, however, that, by itself, it does *not* explain how to construct the space ${\cal H}$ (it is not an honest quantization), and can not capture the fact that $\hbar^{-1}$ should ever be discretized.\
A third option, *brane quantization* [@gukov-2008], is a marriage of geometric and deformation quantizations in a physical context. It approaches the problem of quantization by complexifying ${\cal M}$ and $\omega$, and constructing a certain (secondary) topological quantum field theory on the resulting space ${\cal M}_{\mathbb{C}}$. It has the advantage of easily characterizing the various choices that one must make in quantization, and provides simple geometric criteria that describe quantizable $({\cal M},\omega;\hbar)$. In this approach, the Hilbert space ${\cal H}$ is constructed as the space of morphisms (space of open strings), $${\cal H}= {\rm Hom} ({\cal B}_{cc},{\cal B}') \,,$$ where ${\cal B}_{cc}$ and ${\cal B}'$ are objects (branes) of a certain category associated to the symplectic manifold ${\cal M}_{\mathbb{C}}$. Moreover, in this approach, independence of ${\cal H}$ on various choices can be reformulated as a problem of constructing a flat connection on the space of such choices, which identifies the space of ground states in the secondary TQFT. In a closely related context, this problem has been studied in the mathematical physics literature [@CecottiV; @Dubrovin], and leads to a beautiful story that involves integrable systems and $tt^*$ equations.
