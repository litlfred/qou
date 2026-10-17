---
doc_id: arxiv-0904.1556v2
doc_title: "The Algebra of Grand Uniﬁed Theories"
section_id: sec-006-222-leptons
section_title: "Leptons"
section_number: 2.2.2
pages: 17-19
source_pdf: 0904.1556v2.pdf
source_sha256: a1a43786d817f085
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "The Algebra of Grand Uniﬁed Theories — The Standard Model is the best tested and most widely accepted theory of elementary particles we have today."
---
[]{#sec:leptons label="sec:leptons"}

With the quarks and electron, we have met all the fundamental fermions required to make atoms, and almost all of the particles we need to discuss the Standard Model. Only one player remains to be introduced: the **neutrino**, $\nu$. This particle completes the **first generation** of fundamental fermions: 1em

::: center
  **The First Generation of Fermions --- Charge**                 
  ------------------------------------------------- ------------- ----------------
  Name                                                 Symbol          Charge
                                                                  
  Neutrino                                           $\nu \quad$         0
                                                                  
  Electron                                              $e^-$           $-1$
                                                                  
  Up quark                                            $u \quad$    $+\frac{2}{3}$
                                                                  
  Down quark                                          $d \quad$    $-\frac{1}{3}$
                                                                  
:::

1em

Neutrinos are particles which show up in certain interactions, like the decay of a neutron into a proton, an electron, and an antineutrino $$n \to p + e^- + \overline{\nu}.$$ Indeed, neutrinos $\nu$ have antiparticles $\overline{\nu}$, just like quarks and all other particles. The electron's antiparticle, denoted $e^+$, was the first discovered, so it wound up subject to an inconsistent naming convention: the 'antielectron' is called a **positron**.

Neutrinos carry no charge and no color. They interact very weakly with other particles, so weakly that they were not observed until the 1950s, over 20 years after they were hypothesized by Pauli. Collectively, neutrinos and electrons, the fundamental fermions that do not feel the strong force, are called **leptons**.

In fact, the neutrino only interacts via the **weak force**. Like the electromagnetic force and the strong force, the weak force is a fundamental force, hypothesized to explain the decay of the neutron, and eventually required to explain other phenomena.

The weak force cares about the 'handedness' of particles. It seems that every particle that we have discussed comes in left- and right-handed varieties, which (quite roughly speaking) spin in opposite ways. There are are left-handed leptons, which we denote as $$\nu_L \quad e^-_L$$ and left-handed quarks, which we denote as $$u_L \quad d_L$$ and similarly for right-handed fermions, which we will denote with a subscript $R$. As the terminology suggests, looking in a mirror interchanges left and right---in a mirror, the left-handed electron $e^-_L$ looks like a right-handed electron, $e^-_R$, and vice versa. More precisely, applying any of the reflections in the Poincaré group to the (infinite-dimensional) representation we use to describe these fermions interchanges left and right.

Remarkably, the weak force interacts only with left-handed particles and right-handed antiparticles. For example, when the neutron decays, we always have $$n_L \to p_L + e^-_L + \overline{\nu}_R$$ and never $$n_R \to p_R + e^-_R + \overline{\nu}_L.$$ This fact about the weak force, first noticed in the 1950s, left a deep impression on physicists. No other physical law is asymmetric in left and right. That is, no other physics, classical or quantum, looks different when viewed in a mirror. Why the weak force, and only the weak force, exhibits this behavior is a mystery.

Since neutrinos only feel the weak force, and the weak force only involves left-handed particles, the right-handed neutrino $\nu_R$ has never been observed directly. For a long time, physicists believed this particle did not even exist, but recent observations of neutrino oscillations suggest otherwise. In this paper, we will assume there are right-handed neutrinos, but the reader should be aware that this is still open to some debate. In particular, even if they do exist, we know very little about them.

Note that isospin is not conserved in weak interactions. After all, we saw in the last section that $I_3$ is all about counting the number of $u$ quarks over the number of $d$ quarks. In a weak process such as neutron decay $$udd \to uud + e^- + \overline{\nu},$$ the right-hand side has $I_3 = -\frac{1}{2}$, while the left has $I_3 = \frac{1}{2}$.

Yet maybe we are not being sophisticated enough. Perhaps isospin can be extended beyond quarks, and leptons can also carry $I_3$. Indeed, if we define $I_3( \nu_L ) = \frac{1}{2}$ and $I_3( e^- ) = -\frac{1}{2}$, we get

::: center
  -------- ---------------- ------- --------------- ----- --------------- ----- --------------------
                $n_L$        $\to$       $p_L$       $+$      $e_L^-$      $+$   $\overline{\nu}_R$
                                                                                
  $I_3:$    $-\frac{1}{2}$    $=$    $\frac{1}{2}$   $-$   $\frac{1}{2}$   $-$     $\frac{1}{2}$
  -------- ---------------- ------- --------------- ----- --------------- ----- --------------------
:::

where we have used the rule that isospin reverses sign for antiparticles.

This extension of isospin is called **weak isospin** since it extends the concept to weak interactions. Indeed, it turns out to be fundamental to the theory of weak interactions. Unlike regular isospin symmetry, which is only approximate, weak isospin symmetry turns out to be exact.

So from now on we shall discuss only weak isospin, and call it simply **isospin**. Weak isospin is zero for right-handed particles, and $\pm \frac{1}{2}$ for left-handed particles: 1em

::: center
  **The First Generation of Fermions --- Charge and Isospin**                              
  ------------------------------------------------------------- --------- ---------------- ----------------
                                                                                           
  Name                                                           Symbol        Charge          Isospin
                                                                                $Q$             $I_3$
  Left-handed neutrino                                           $\nu_L$        $0$         $\frac{1}{2}$
                                                                                           
  Left-handed electron                                           $e^-_L$        $-1$        $-\frac{1}{2}$
                                                                                           
  Left-handed up quark                                            $u_L$    $+\frac{2}{3}$   $\frac{1}{2}$
                                                                                           
  Left-handed down quark                                          $d_L$    $-\frac{1}{3}$   $-\frac{1}{2}$
                                                                                           
  Right-handed neutrino                                          $\nu_R$        $0$              $0$
                                                                                           
  Right-handed electron                                          $e^-_R$        $-1$             $0$
                                                                                           
  Right-handed up quark                                           $u_R$    $+\frac{2}{3}$        $0$
                                                                                           
  Right-handed down quark                                         $d_R$    $-\frac{1}{3}$        $0$
                                                                                           
:::

1em The antiparticle of a left-handed particle is right-handed, and the antiparticle of a right-handed particle is left-handed. The isospins also change sign. For example, $I_3( e^+_R ) = +\frac{1}{2}$, while $I_3( e^+_L ) = 0$.

In Section [\[sec:hypercharge\]](#sec:hypercharge){reference-type="ref" reference="sec:hypercharge"}, we will see that the Gell-Mann--Nishijima formula, when applied to weak isospin, defines a fundamental quantity, the 'weak hypercharge', that is vital to the Standard Model. But first, in Section [\[sec:redux\]](#sec:redux){reference-type="ref" reference="sec:redux"}, we discuss how to generalize the ${\rm SU}(2)$ symmetries from isospin to weak isospin.
