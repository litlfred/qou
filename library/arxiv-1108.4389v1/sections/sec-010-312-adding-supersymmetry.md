---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-010-312-adding-supersymmetry
section_title: "Adding supersymmetry"
section_number: 3.1.2
pages: 23-24
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.993
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:susySp label="sec:susySp"}

The $Sp(2N,{\mathbb Z})$ action can be supersymmetrized to give an $Sp(2N,{\mathbb Z})$ action on supersymmetric 3d theories equipped with a supersymmetric coupling to a background abelian gauge supermultiplet. This can be done for any amount of supersymmetry, but it is important to make a specific choice, as different choices give different group actions.

In the reference [@GW-Sduality] this was applied to theories with $\mathcal{N}=4$ supersymmetry. As a useful example of the $S$ action in the context of $\mathcal{N}=4$ theories, we can consider a single hypermultiplet of unit flavor charge canonically coupled to an $\mathcal{N}=4$ background gauge field. If we make the $\mathcal{N}=4$ background gauge field dynamical --- performing an $S$ operation --- we have a familiar 3d theory: $\mathcal{N}=4$ SQED with one flavor. This is the canonical setup for 3d mirror symmetry [@IS; @dBHOY], which provides an alternative description of the theory in terms of a free twisted hypermultiplet that arises as a monopole operator in the original description. In particular, it carries unit flavor charge under the new $\mathcal{N}=4$ background gauge field. So the transformation $S$ acts rather trivially on this simple 3d theory: it sends it back to itself [@KS-mirror]. On the other hand, $T$ acts non-trivially.

Any $\mathcal{N}=4$ statement can be reinterpreted as an $\mathcal{N}=2$ statement, but a little care is needed: the $\mathcal{N}=4$ 3d gauge multiplet consists of an $\mathcal{N}=2$ 3d gauge multiplet plus a chiral multiplet. The $\mathcal{N}=4$ $Sp(2N,{\mathbb Z})$ action is the combination of an $\mathcal{N}=2$ $Sp(2N,{\mathbb Z})$ action plus additional operations involving 3d chiral multiplets and superpotential couplings. This anticipates a central theme of this paper: the interplay between the "gauge" $Sp(2N,{\mathbb Z})$ action and a "matter" action which involves adding new chiral multiplets with appropriate superpotential couplings. Indeed, the 3d $\mathcal{N}=2$ theories $T_M$ associated to 3-manifolds $M$ with boundary will be coupled both to background gauge fields and background chiral multiplets.

As a first step towards understanding this statement, let us describe the "gauge" $Sp(2N,{\mathbb Z})$ action for $\mathcal{N}=2$ theories. Suppose we have a theory with $U(1)^N$ flavor symmetry, coupled to $N$ background vector multiplets $V_i$. Each $V_i$, containing a real scalar field $\sigma_i$ and two Majorana fermions $\lambda^\alpha_i$ in addition to the gauge field $A_i$, can also be dualized to a linear multiplet [@AHISS; @NishinoGates]

$$V_i\quad\leftrightarrow\quad \Sigma_i = \overline{D}^\alpha D_\alpha V\,,$$

where the lowest component of $\Sigma_i$ is $\sigma_i$. Now, in order to supersymmetrize the $Sp(2N,{\mathbb Z})$ action [\[SpT\]](#SpT){reference-type="eqref" reference="SpT"}--[\[SpGL\]](#SpGL){reference-type="eqref" reference="SpGL"}, one simply has to substitute $AdA'\to V\Sigma'$ for all relevant Chern-Simons or FI terms:

$$\begin{aligned}
 \text{``$T$-type''}\quad g=\begin{pmatrix} I & 0 \\ B & I \end{pmatrix} \;\;&:\qquad \mathcal{L}[\vec{V}]\to\mathcal{L}[\vec{V}_{\rm new}]+\frac{1}{4\pi}\int d^4\theta\,\vec\Sigma_{\rm new} \cdot B\,\vec V_{\rm new}\,; \label{Sp2T} \\

\text{``$S$-type''}\quad g= \begin{pmatrix}I-J & -J \\ J & I-J \end{pmatrix}\;\;&:\qquad \mathcal{L}[\vec V]\to\mathcal{L}[\vec V]+\frac{1}{2\pi}\int d^4\theta\, \vec{\Sigma}_{\rm new}\cdot J\,\vec V\, \label{Sp2S} \\

\text{``$GL$-type''}\quad g = \begin{pmatrix} U & 0 \\ 0 & U^{-1\,t}\end{pmatrix}\;\;&:\qquad \mathcal{L}[\vec V]\to \mathcal{L}[U^{-1}\vec V_{\rm new}]\,. \label{Sp2GL}
\end{aligned}$$ Note that a $GL(N,{\mathbb Z})$ linear transformation $U^{-1}$ can be applied both to a collection of vector multiplets $\vec V$ and linear multiplets $\vec \Sigma$, wherever they occur in the Lagrangian.
