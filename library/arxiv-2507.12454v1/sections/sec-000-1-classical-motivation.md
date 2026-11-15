---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-000-1-classical-motivation
section_title: "Classical motivation"
section_number: 1
pages: 1-3
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.956
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
One way character varieties naturally arise is as follows. Suppose we have a linear ODE $$\label{eq:ODE}
        \frac\partial{\partial t} \vec{\varphi}(t) = A(t) \vec{\varphi}(t)\quad(t\in \mathbb{C}).$$ Here $A(t)$ is an $n\times n$ matrix-valued meromorphic function of one complex variable $t$, and we are looking for vector-valued solutions $\vec{\varphi}(t)$. Let $t_1,\ldots, t_k$ be the poles of $A(t)$ (including $\infty$ if necessary), which we call *punctures*. Choose a basepoint $\ast$, away from the poles of $A(t)$. In a neighborhood of $\ast$, we have an $n$-dimensional vector space of solutions of the ODE [\[eq:ODE\]](#eq:ODE){reference-type="eqref" reference="eq:ODE"}. For any loop $\gamma$ based at $\ast$ avoiding the punctures, solving the ODE along $\gamma$ produces a linear transformation of the space of solutions. Choosing a basis, we obtain the *monodromy representation* of the fundamental group $$\rho:\pi_1(*, \mathbb{P}^1(\mathbb{C})\setminus\{t_1,\ldots,t_k\}) \to \mathrm{GL}_n(\mathbb{C}).$$ A different choice of basis produces an equivalent representation.

Another way to think about this is that local solutions to the ODE form a *locally constant sheaf* on $\mathbb{P}^1(\mathbb{C})\setminus\{t_1,\ldots,t_k\}$. Locally constant sheaves are also called *local systems*, and they are in a natural bijection with equivalence classes of monodromy representations.

More explicitly, the fundamental group of $\mathbb{P}^1(\mathbb{C})\setminus\{t_1,\ldots,t_k\}$ is the free group on $k-1$ generators. Drawing loops around the punctures as shown on Figure [1](#fig:gammas){reference-type="ref" reference="fig:gammas"}, one obtains the following presentation of the fundamental group: $$\label{eq:presentation pi genus 0}
        \pi_1(*, \mathbb{P}^1(\mathbb{C})\setminus\{t_1,\ldots,t_k\}) = \langle \gamma_1, \ldots, \gamma_k \;|\; \gamma_1 \cdots \gamma_k = 1 \rangle.$$ This presentation is better than the free group presentation for the following reason. Let us assume that $A(t)$ has simple poles. In this case, analyzing the ODE locally around each puncture, one can compute the *local monodromy* matrices $\rho(\gamma_i)$, up to conjugation, by a purely algebraic procedure. For instance, the characteristic polynomial of $\rho(\gamma_i)$ coincides with the characteristic polynomial of the matrix $\exp{\left(2\pi \sqrt{-1} A_i\right)}$, where $A_i$ is the residue of $A(t)$ at $t=t_i$.

<figure id="fig:gammas">

<figcaption>Fundamental group of a <span class="math inline"><em>k</em></span>-punctured sphere</figcaption>
</figure>

In view of the presentation [\[eq:presentation pi genus 0\]](#eq:presentation pi genus 0){reference-type="eqref" reference="eq:presentation pi genus 0"}, a monodromy representation is encoded by a $k$-tuple of $n\times n$ matrices $M_1, \ldots, M_k$ satisfying $$M_1 \cdots M_k = I_n,$$ where the local monodromy computation informs us about the conjugacy class of each $M_i$.

Contrary to the local monodromy computation, which is algebraic, we only know how to compute the global monodromy representation by transcendental techniques (unless in special cases). So it is probably hopeless to look for an algebraic way to compute the global monodromy exactly. On the other hand, it still makes sense to formulate the following problem:

::: problem
Given $n$, $k$, and a collection of local monodromies, list all algebraic relations between the entries of the matrices comprising the monodromy representation, satisfied by all monodromy representations with prescribed local monodromies.
:::

This is the basic idea about the character variety. Before we give a precise definition we consider an example which can be worked out explicitly.
