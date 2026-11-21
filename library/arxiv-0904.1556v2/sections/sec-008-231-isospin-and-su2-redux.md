---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-008-231-isospin-and-su2-redux
section_title: "Isospin and SU(2), Redux"
section_number: 2.3.1
pages: 19-22
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:redux label="sec:redux"}

The tale we told of isospin in Section [\[sec:isospin\]](#sec:isospin){reference-type="ref" reference="sec:isospin"} only concerned the strong force, which binds nucleons together into nuclei. We learned about an approximation in which nucleons live in the fundamental rep ${\mathbb C}^2$ of the isospin symmetry group ${\rm SU}(2)$, and that they interact by exchanging pions, which live in the complexified adjoint rep of this group, namely $\mathfrak{sl}(2, {\mathbb C})$.

But this tale is mere prelude to the modern story, where *weak* isospin, defined in Section [\[sec:leptons\]](#sec:leptons){reference-type="ref" reference="sec:leptons"}, is the star of the show. This story is not about the strong force, but rather the weak force. This story parallels the old one, but it involves left-handed fermions instead of nucleons. The left-handed fermions, with $I_3 = \pm \frac{1}{2}$, are paired up into fundamental representations of ${\rm SU}(2)$, the **weak isospin symmetry group**. There is one spanned by left-handed leptons: $$\nu_L, e^-_L \in {\mathbb C}^2,$$ and one spanned by each color of left-handed quarks: $$u^r_L, d^r_L \in {\mathbb C}^2, \quad u^g_L, d^g_L \in {\mathbb C}^2, \quad 
u^b_L, d^b_L \in {\mathbb C}^2.$$ The antiparticles of the left-handed fermions, the right-handed antifermions, span the dual representation ${\mathbb C}^{2*}$.

Because these particles are paired up in the same ${\rm SU}(2)$ representation, physicists often write them as **doublets**: $$\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)\qquad \left( \! \begin{array}{c} u_L \\ d_L \end{array} \! \right)$$ with the particle of higher $I_3$ written on top. Note that we have suppressed color on the quarks. This is conventional, and is done because ${\rm SU}(2)$ acts the same way on all colors.

The particles in these doublets then interact via the exchange of $W$ bosons, which are the weak isospin analogues of the pions. Like the pions, there are three $W$ bosons: $$W^+ = \left(\begin{array}{cc} 0 & 1 \\ 0 & 0 \end{array} \right), \quad  
W^0 = \left(\begin{array}{cc} 1 & 0 \\ 0 & -1 \end{array} \right), \quad
W^- = \left(\begin{array}{cc} 0 & 0 \\ 1 & 0 \end{array} \right).$$ They span the complexified adjoint rep of ${\rm SU}(2)$, $\mathfrak{sl}(2, {\mathbb C})$, and they act on each of the doublets like the pions act on the nucleons, via the action of $\mathfrak{sl}(2,{\mathbb C})$ on ${\mathbb C}^2$. For example,

::: center
![image](W+d_vertex)
:::

Again, Feynman diagrams are the physicists' way of drawing intertwining operators. Since all the ${\mathbb C}^2$'s are acted on by the same ${\rm SU}(2)$, they can interact with each other via $W$ boson exchange. For example, quarks and leptons can interact via $W$'s:

::: center
![image](qlW_exchange)
:::

This is in sharp contrast to the old isospin theory. In the new theory, it is processes like these that are responsible for the decay of the neutron:

::: center
![image](betadecay)
:::

The fact that only left-handed particles are combined into doublets reflects the fact that only they take part in weak interactions. Every right-handed fermion, on the other hand, is trivial under ${\rm SU}(2)$. Each one spans the trivial rep, ${\mathbb C}$. An example is the right-handed electron $$e^-_R \in {\mathbb C}.$$ Physicists call these particles **singlets**, meaning they are trivial under ${\rm SU}(2)$. This is just the representation theoretic way of saying the right-handed electron, $e^-_R$, does not participate in weak interactions.

In summary, left-handed fermions are grouped into doublets (nontrivial representations of ${\rm SU}(2)$ on ${\mathbb C}^2$), while right-handed fermions are singlets (trivial representations on ${\mathbb C}$). So, the left-handed ones interact via the exchange of $W$ bosons, while the right-handed ones do not. 1em

::: center
  **The First Generation of Fermions --- ${\rm SU}(2)$ Representations**                                                                                           
  ------------------------------------------------------------------------ -------------------------------------------------------------------- ------------------ -------------------
                                                                                                                                                                   
  Name                                                                                                    Symbol                                     Isospin        ${\rm SU}(2)$ rep
  Left-handed leptons                                                       $\left( \! \begin{array}{c} \nu_L \\ e^-_L \end{array} \! \right)$   $\pm\frac{1}{2}$    ${\mathbb C}^2$
                                                                                                                                                                   
  Left-handed quarks                                                          $\left( \! \begin{array}{c} u_L \\ d_L \end{array} \! \right)$     $\pm\frac{1}{2}$    ${\mathbb C}^2$
                                                                                                                                                                   
  Right-handed neutrino                                                                                  $\nu_R$                                       $0$            ${\mathbb C}$
                                                                                                                                                                   
  Right-handed electron                                                                                  $e^-_R$                                       $0$            ${\mathbb C}$
                                                                                                                                                                   
  Right-handed up quark                                                                                   $u_R$                                        $0$            ${\mathbb C}$
                                                                                                                                                                   
  Right-handed down quark                                                                                 $d_R$                                        $0$            ${\mathbb C}$
                                                                                                                                                                   
:::
