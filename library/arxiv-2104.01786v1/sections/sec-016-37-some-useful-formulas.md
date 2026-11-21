---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-016-37-some-useful-formulas
section_title: "Some useful formulas"
section_number: 3.7
pages: 15-16
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 1.0
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
Here we list some useful pairings that can be computed using the particle-friendly parametrisation developed in the previous subsection. We will give them in their version analogous to ([\[y12\]](#y12){reference-type="ref" reference="y12"}), with two different spinors.

First, we have $$\begin{aligned}
\label{Ot-formulas-1}
- \langle y_1, \tilde{E}^1\tilde{E}^2 \tilde{E}^3 y_2 \rangle = \langle y_1, \tilde{J} y_2 \rangle=
-{\rm i\,}\left( \begin{array}{cc} u & d \end{array}\right)_1
\left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right)  \left( \begin{array}{c} u \\ d \end{array}\right)_2 + {\rm c.c.}
\end{aligned}$$ This result follows from the fact that $\tilde{J}$ acts as the operator of multiplication by $-{\rm i\,}$ on $(1,0)$ eigenspace where $y_{1,2}^+$ take values.

We will also need $$\begin{aligned}
\label{Ot-formulas-2}
\langle y_1, (\phi^i \tilde{E}^i) y_2\rangle = \left( \begin{array}{cc} u & d \end{array}\right)_1 
\left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right) \left( \begin{array}{cc} \phi^3 & \phi^1 -{\rm i\,}\phi^2 \\ \phi^1+{\rm i\,}\phi^2 & -\phi^3 \end{array}\right) \left( \begin{array}{c} u \\ d \end{array}\right)_2 + {\rm c.c.}
\\ \nonumber
\langle y_1, \frac{1}{2}(\epsilon^{ijk} \phi^i \tilde{E}^j \tilde{E}^k) y_2\rangle = {\rm i\,}\left( \begin{array}{cc} u & d \end{array}\right)_1 
\left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right) \left( \begin{array}{cc} \phi^3 & \phi^1 -{\rm i\,}\phi^2 \\ \phi^1+{\rm i\,}\phi^2 & -\phi^3 \end{array}\right) \left( \begin{array}{c} u \\ d \end{array}\right)_2 + {\rm c.c.}
\end{aligned}$$

## The split $\tilde{G}_2$

The group of automorphisms of the split octonions $\tilde{G}_2$ can be defined as the subgroup of ${\rm SO}(4,3)$ that preserves the 3-form ([\[C-split\]](#C-split){reference-type="ref" reference="C-split"}). Equivalently, it is the subgroup of ${\rm Spin}(4,3)$ that preserves the spinor ${\mathbb I}$.

It can be checked that the intersection of the Lie algebras $\tilde{{\mathfrak g}}(2)$ and ${\mathfrak so}(3)\times{\mathfrak so}(1,3)$ is the diagonal ${\mathfrak so}(3)$ that describes simultaneous rotations in the $\tilde{e}^{1,2,3}$ and $\tilde{e}^{5,6,7}$ planes. In particular, there are no boosts in this intersection.

While this may sound as bad news for physics, we remind the reader that the analogous intersection in the ${\mathbb O}$ case is that between ${\mathfrak g}(2)$ and ${\mathfrak so}(6)$. And as we discussed in the previous section, this intersection is ${\mathfrak su}(3)$, but not ${\mathfrak su}(3)\times {\mathfrak u}(1)_{B-L}$ that would be desirable for physics. So, the ${\rm U}(1)_{B-L}$ does not survive the intersection with $G_2$ in the case of ${\rm Spin}(7)$. What we see in the present case of ${\rm Spin}(4,3)$ is that this group naturally contains the weak ${\rm SU}(2)$ together with the Lorentz group, but neither of this survives the intersection with $\tilde{G}_2$. Only the diagonal ${\rm SU}(2)$ consisting of the simultaneous weak ${\rm SU}(2)$ transformations and spatial rotations does survive as a subgroup of $\tilde{G}_2$. So, this situation is analogous to what happens for ${\rm Spin}(7)$. This just means that the to-be-found mechanism that will select the \"physical\" unbroken subgroups from ${\rm Spin}(11,3)$ is not the one where intersections with $G_2, \tilde{G}_2$ will play role. But there is clearly something important to be understood here.

# The octonionic model for ${\rm Spin}(11,3)$ {#sec:spin11-3}

We now put the ${\mathbb O}, \tilde{{\mathbb O}}$ building blocks together, and construct an octonionic model for the group ${\rm Spin}(11,3)$. The construction we are to describe applies to a more general set of pseudo-orthogonal groups, and so we give it in full generality.
