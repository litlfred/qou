---
doc_id: arxiv-1007.2335v1
doc_title: "Hopf solitons in the Nicole model"
section_id: sec-003-4-numerical-results
section_title: "Numerical results"
section_number: 4
pages: 7-10
source_pdf: 1007.2335v1.pdf
source_sha256: a55d544d1740523f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 1.0
doc_brief: "Hopf solitons in the Nicole model — The Nicole model is a conformal ﬁeld theory in three-dimensional space."
---
[]{#sec-num label="sec-num"} In this section we present the results of numerical computations of Hopf solitons using the volume-preserving flow algorithm, with initial conditions constructed as in the previous section. The simulation region $\Omega$ consists of the cube $|x_i|\le 75$ with spatial derivatives approximated by fourth-order accurate finite differences using a lattice spacing $\Delta x=1.$ The flow is evolved using an explicit method with timestep $\Delta t=0.1$ and is terminated once the energy has stabilized at a constant value.

In the continuum theory in Euclidean space the energy of a given solution is invariant under a spatial rescaling. The simulation lattice and finite region $\Omega$ mean that the energy is not independent of the volume $V,$ but for a reasonable range of $V$ we find that there is only a weak variation of the energy. The results of varying $V$ suggest that our quoted energies should be accurate to around one percent. In situations where there are two different solutions with the same value of $Q,$ then comparisons of energies are made using similar volumes. Generally the profile function $g(r)$ is taken to have a simple linear form, with a cutoff to ensure that the boundary condition is satisfied. Varying the cutoff allows different values of $V$ to be investigated, and the results are found to be consistent within the errors mentioned above, of around one percent.

As a first test the ${\cal A}_{1,1}$ solution with $Q=1$ is computed using initial conditions ([\[Qnm11\]](#Qnm11){reference-type="ref" reference="Qnm11"}) with a simple linear profile function. The energy is calculated to be $E=1.000,$ which agrees with the exact solution to three decimal places. This accuracy is beyond that expected in general. Figure 1.1 displays the position curve for this $Q=1$ soliton. For clarity, a tube around the position is displayed by plotting an isosurface where $\phi_3$ is slightly greater than $-1$. The stability of this solution has been confirmed by applying perturbations and also by using initial conditions in which a squashing perturbation is applied to break the axial symmetry of the ${\cal A}_{1,1}$ rational map constructed field. Under the volume-preserving flow the axial symmetry is restored and the same solution is recovered.

The situation is similar for the $Q=2$ solution of type ${\cal A}_{2,1},$ which is shown in Figure 1.2 and has been constructed using initial conditions ([\[Qnm\]](#Qnm){reference-type="ref" reference="Qnm"}) with $(n,m)=(2,1).$ This solution is found to be stable under perturbations that break the axial symmetry and its energy is computed to be $E=1.794.$ This is expected to be the same solution as found using toroidal coordinates, though our energy is $3\%$ lower than that reported in [@ASVW]. This difference is slightly more than that expected from studying variations of the volume $V.$ A comparison of our results for axially symmetric solutions with larger values of $Q$ reveals a better agreement with the toroidal computations in [@ASVW], so the origin of the unusually large disagreement in the case of $Q=2$ remains unclear. We have also computed a solution of the type ${\cal A}_{1,2}$ and confirmed the results of [@ASVW], that this solution has an energy greater than that of the type ${\cal A}_{2,1}.$ This result agrees with the similar situation in the Skyrme-Faddeev model.

In the Skyrme-Faddeev model the axially symmetric $Q=3$ solution of type ${\cal A}_{3,1}$ is unstable to a perturbation that breaks the axial symmetry [@BS5] to form a twisted ring. The notation $\widetilde {\cal A}_{3,1}$ is used to denote the type of this solution, to indicate that it has the same topological type as ${\cal A}_{3,1}$ but that the axial symmetry is broken. We have confirmed that a similar situation occurs in the Nicole model by first constructing the ${\cal A}_{3,1}$ solution, using initial conditions ([\[Qnm\]](#Qnm){reference-type="ref" reference="Qnm"}) with $(n,m)=(3,1),$ and then applying a non-axial perturbation. The resulting twisted ring solution is displayed in Figure 1.3 and its energy is listed in Table [1](#tab-energy){reference-type="ref" reference="tab-energy"}, together with the energies of all the minimal energy solutions found for $1\le Q\le 8.$

<figure id="fig-all8s">
<div class="center">
<embed src="all8s.eps" style="width:16cm" />
</div>
<figcaption>Position curves for the known lowest energy solitons with Hopf charges <span class="math inline">1 ≤ <em>Q</em> ≤ 8.</span></figcaption>
</figure>

::: {#tab-energy}
   $Q$              Type                $E$    $E/Q^{3/4}$
  ----- ----------------------------- ------- -------------
    1         ${\cal A}_{1,1}$         1.000      1.000
    2         ${\cal A}_{2,1}$         1.794      1.067
    3    $\widetilde {\cal A}_{3,1}$   2.535      1.112
    4      ${\cal L}_{1,1}^{1,1}$      3.156      1.116
    5      ${\cal L}_{1,2}^{1,1}$      3.739      1.118
    6      ${\cal L}_{2,2}^{1,1}$      4.339      1.132
    7         ${\cal K}_{3,2}$         4.843      1.125
    8      ${\cal L}_{2,2}^{2,2}$      5.297      1.114

  : Energies and types of the known minimal energy solitons with $1\le Q\le 8.$
:::

<figure id="fig-en">
<div class="center">
<embed src="en.eps" style="width:10cm" />
</div>
<figcaption>The ratio of the energy <span class="math inline"><em>E</em></span> to the conjectured bound <span class="math inline"><em>Q</em><sup>3/4</sup></span> for the known minimal energy solitons with <span class="math inline">1 ≤ <em>Q</em> ≤ 8.</span> </figcaption>
</figure>

In the Skyrme-Faddeev model the minimal energy soliton with $Q=4$ is axially symmetric and is of the type ${\cal A}_{2,2}$ [@HS]. A solution of this type has been constructed in the Nicole model using toroidal coordinates [@ASVW]. We have computed this solution, using initial conditions ([\[Qnm\]](#Qnm){reference-type="ref" reference="Qnm"}) with $(n,m)=(2,2),$ but found that, in constrast to the Skyrme-Faddeev model, this solution is unstable to perturbations that break the axial symmetry. Such a perturbation leads to the linked solution displayed in Figure 1.4, which is of the type ${\cal L}_{1,1}^{1,1}.$ We have also confirmed that the same solution is obtained by starting with the initial conditions ([\[Qlink\]](#Qlink){reference-type="ref" reference="Qlink"}) with $n=1.$ The energy of this solution can be found in Table [1](#tab-energy){reference-type="ref" reference="tab-energy"}.

Solitons with $Q=5,6,7,8$ have been constructed using a variety of initial conditions for each $Q$, including perturbed axial fields, links and knots. The resulting minimal energy solitons for each $Q$ are displayed in Figure 1 and their energies and types are listed in Table [1](#tab-energy){reference-type="ref" reference="tab-energy"}. For $Q=5,6$ the solitons are links and have the same type as in the Skyrme-Faddeev model. For $Q=7$ the soliton is a trefoil knot and again this agrees with the result of the Skyrme-Faddeev model. For $Q=8$ the soliton is a link of type ${\cal L}_{2,2}^{2,2}.$ In the Skyrme-Faddeev model the minimal energy soliton with $Q=8$ is also a link, but it has the different type ${\cal L}_{3,3}^{1,1}.$ In the Skyrme-Faddeev model initial conditions of the type ${\cal L}_{2,2}^{2,2}$ develop reconnections during the energy minimization process and this produces the minimal energy link ${\cal L}_{3,3}^{1,1}$ [@Su].

In the Skyrme-Faddeev model it has been shown [@VK] that a lower bound on the energy exists of the form $E\ge k\, Q^\frac{3}{4},$ where $k$ is a known constant. To date, a similar lower bound has not been proved for the Nicole model: see [@ASVW] for a discussion of the technical difficulties in adapting the proof in [@VK] to the Nicole model. A conjectured lower bound for the Nicole model is $E\ge Q^\frac{3}{4},$ where the constant has been set to unity, as this is the largest possible value consistent with the energy of the explicit $Q=1$ solution. In the final column of Table [1](#tab-energy){reference-type="ref" reference="tab-energy"} we list the ratio of the energy to this conjectured bound and plot this ratio in Figure [2](#fig-en){reference-type="ref" reference="fig-en"}. It is clear that our numerical results are consistent with the conjectured bound. Furthermore, for $Q>2$ the excess above the bound appears to settle down to a value around $12\%,$ which suggests that the solutions we have found are good candidates for the global energy minima for these values of $Q.$
