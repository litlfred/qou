---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-011-234-color-and-su3
section_title: "Color and SU(3)"
section_number: 2.3.4
pages: 27-28
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:color label="sec:color"}

There is one more fundamental force in the Standard Model: the **strong force**. We have already met this force, as the force that keeps the nucleus together, but we discussed it before we knew that protons and neutrons are made of quarks. Now we need a force to keep quarks together inside the nucleons, and quark confinement tells us it must be a very strong force indeed. It is this force that, in modern parlance, is called the strong force and is considered fundamental. The force between nucleons is a side effect of these more fundamental interactions among quarks.

Like all three forces in the Standard Model, the strong force is explained by a gauge theory, this time with gauge group ${\rm SU}(3)$, the color symmetry group of the quarks. The picture is simpler than that of electromagnetism and the weak force, however, because this symmetry is 'unbroken'.

By now you can guess how this goes. Every kind of quark spans the fundamental representation ${\mathbb C}^3$ of ${\rm SU}(3)$. For example, the left-handed up quark, with its three colors, lives in $$u^r_L, u^g_L, u^b_L \in {\mathbb C}^3$$ and the left-handed down quark, with its three colors, spans another copy of ${\mathbb C}^3$, $$d^r_L, d^g_L, d^b_L \in {\mathbb C}^3$$ Together, these span the ${\rm SU}(3)$ representation $${\mathbb C}^2 \otimes {\mathbb C}^3$$ where ${\mathbb C}^2$ is trivial under ${\rm SU}(3)$.

The quarks interact by the exchange of **gluons**, the gauge bosons of the strong force. These gauge bosons live in ${\mathbb C}\otimes {\mathfrak{su}}(3)
\cong\mathfrak{sl}(3, {\mathbb C})$, the complexified adjoint representation of ${\rm SU}(3)$. The interactions are drawn as Feynman diagrams, which now depict intertwining operators between representations of ${\rm SU}(3)$:

::: center
![image](gluon_exchange)
:::

The gluons are fundamental particles, gauge bosons of the strong force, and they complete our table of gauge bosons: 1em

::: center
  **Gauge Bosons**                        
  ------------------ -------------------- ----------------------
  Force              Gauge Boson                  Symbol
  Electromagnetism   Photon                      $\gamma$
                                          
  Weak force         $W$ and $Z$ bosons    $W^+$, $W^-$ and $Z$
                                          
  Strong force       Gluons                        $g$
                                          
:::

1em

On the other hand, the leptons are 'white': they transform trivially under ${\rm SU}(3)$. So, they do not exchange gluons. In other words, they are not affected by the strong force. We can capture all of this information in a table, where we give the ${\rm SU}(3)$ representations in which all our fermions live.

1em

::: center
  **The First Generation of Fermions --- ${\rm SU}(3)$ Representations**                                       
  ------------------------------------------------------------------------ ----------------------- ----------- -------------------
                                                                                                               
  Name                                                                             Symbol            Colors     ${\rm SU}(3)$ rep
  Left-handed neutrino                                                             $\nu_L$            white       ${\mathbb C}$
                                                                                                               
  Left-handed electron                                                             $e^-_L$            white       ${\mathbb C}$
                                                                                                               
  Left-handed up quarks                                                     $u^r_L, u^g_L, u^b_L$   $r, g, b$    ${\mathbb C}^3$
                                                                                                               
  Left-handed down quarks                                                   $d^r_L, d^g_L, d^b_L$   $r, g, b$    ${\mathbb C}^3$
                                                                                                               
  Right-handed electron                                                            $e^-_R$            white       ${\mathbb C}$
                                                                                                               
  Right-handed neutrino                                                            $\nu_R$            white       ${\mathbb C}$
                                                                                                               
  Right-handed up quarks                                                    $u^r_R, u^g_R, u^b_R$   $r, g, b$    ${\mathbb C}^3$
                                                                                                               
  Right-handed down quarks                                                  $d^r_R, d^g_R, d^b_R$   $r, g, b$    ${\mathbb C}^3$
                                                                                                               
:::

1em
