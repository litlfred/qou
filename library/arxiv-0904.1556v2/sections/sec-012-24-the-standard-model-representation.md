---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-012-24-the-standard-model-representation
section_title: "The Standard Model Representation"
section_number: 2.4
pages: 28-30
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:smrep label="sec:smrep"}

We are now in a position to put the entire Standard Model together in a single picture, much as we combined the isospin ${\rm SU}(2)$ and hypercharge ${\rm U}(1)$ into the electroweak gauge group, ${\rm U}(1) \times {\rm SU}(2)$, in Section [\[sec:electroweak\]](#sec:electroweak){reference-type="ref" reference="sec:electroweak"}. We then tensored the hypercharge ${\rm U}(1)$ representations with the isospin ${\rm SU}(2)$ representations to get the electroweak representations.

Now let us take this process one step further, by bringing in a factor of ${\rm SU}(3)$, for the color symmetry, and tensoring the representations of ${\rm U}(1)
\times {\rm SU}(2)$ with the representations of ${\rm SU}(3)$. Doing this, we get the Standard Model. The Standard Model has this gauge group: $$G_{\mbox{SM}} = {\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3).$$ The fundamental fermions described by the Standard Model combine to form representations of this group. We know what these are, and describe all of them in Table [1](#tab:smrep){reference-type="ref" reference="tab:smrep"}.

::: center
::: {#tab:smrep}
  **The Standard Model Representation**                                                                                                                                                  
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------
  Name                                                                                                        Symbol                                                                              ${\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3)$ rep
                                                                                                                                                                                         
  Left-handed leptons                                                           $\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)$                                             ${\mathbb C}_{-1} \otimes {\mathbb C}^2 \otimes {\mathbb C}$
                                                                                                                                                                                         
  Left-handed quarks                       $\renewcommand{0.8}{1.2} \left( \! \begin{array}{c} u^r_L, u^g_L, u^b_L \\ d^r_L, d^g_L, d^b_L \end{array} \! \right) \renewcommand{0.8}{1}$   ${\mathbb C}_{\frac{1}{3}} \otimes {\mathbb C}^2 \otimes {\mathbb C}^3$
                                                                                                                                                                                         
  Right-handed neutrino                                                                                      $\nu_R$                                                                             ${\mathbb C}_{0} \otimes {\mathbb C}\otimes {\mathbb C}$
                                                                                                                                                                                         
  Right-handed electron                                                                                      $e^-_R$                                                                             ${\mathbb C}_{-2} \otimes {\mathbb C}\otimes {\mathbb C}$
                                                                                                                                                                                         
  Right-handed up quarks                                                                             $(u^r_R, u^g_R, u^b_R)$                                                               ${\mathbb C}_{\frac{4}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3$
                                                                                                                                                                                         
  Right-handed down quarks                                                                           $(d^r_R, d^g_R, d^b_R)$                                                               ${\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3$
                                                                                                                                                                                         

  : Fundamental fermions as representations of ${G_{\mbox{\rm SM}}}= {\rm U}(1) \times {\rm SU}(2) \times {\rm SU}(3)$
:::
:::

All of the representations of ${G_{\mbox{\rm SM}}}$ in the left-hand column are irreducible, since they are made by tensoring irreps of this group's three factors, ${\rm U}(1)$, ${\rm SU}(2)$ and ${\rm SU}(3)$. This is a general fact: if $V$ is an irrep of $G$, and $W$ is an irrep of $H$, then $V \otimes W$ is an irrep of $G \times H$. Moreover, all irreps of $G \times H$ arise in this way.

On the other hand, if we take the direct sum of all these irreps, $$F = ({\mathbb C}_{-1} \otimes {\mathbb C}^2 \otimes {\mathbb C}) \quad \oplus \quad \cdots \quad 
\oplus \quad ({\mathbb C}_{-\frac{2}{3}} \otimes {\mathbb C}\otimes {\mathbb C}^3),$$ we get a reducible representation containing all the first-generation fermions in the Standard Model. We call $F$ the **fermion representation**. If we take the dual of $F$, we get a representation describing all the antifermions in the first generation. And taking the direct sum of these spaces: $$F \oplus F^*$$ we get a representation of ${G_{\mbox{\rm SM}}}$ that we will call the **Standard Model representation**. It contains all the first-generation elementary particles in the Standard Model. It does not contain the gauge bosons or the mysterious Higgs.

The fermions living in the Standard Model representation interact by exchanging gauge bosons that live in the complexified adjoint representation of ${G_{\mbox{\rm SM}}}$. We have already met all of these, and we collect them in Table [2](#tab:gaugebosons){reference-type="ref" reference="tab:gaugebosons"}.

::: center
::: {#tab:gaugebosons}
  **Gauge Bosons**                        
  ------------------ -------------------- ----------------------
  Force              Gauge Boson                  Symbol
                                          
  Electromagnetism   Photon                      $\gamma$
                                          
  Weak force         $W$ and $Z$ bosons    $W^+$, $W^-$ and $Z$
                                          
  Strong force       Gluons                        $g$
                                          

  : Gauge bosons
:::
:::

Of all the particles and antiparticles in $F \oplus F^*$, exactly two of them are fixed by the action of ${G_{\mbox{\rm SM}}}$. These are the right-handed neutrino $$\nu_R \in {\mathbb C}_0 \otimes {\mathbb C}\otimes {\mathbb C}$$ and its antiparticle $$\overline{\nu}_L \in ({\mathbb C}_0 \otimes {\mathbb C}\otimes {\mathbb C})^*,$$ both of which are trivial representations of ${G_{\mbox{\rm SM}}}$; they thus do not participate in any forces mediated by the gauge bosons of the Standard Model. They might interact with the Higgs boson, but very little about right-handed neutrinos is known with certainty at this time.
