---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-006-25-connection-to-the-standard-model
section_title: "Connection to the Standard Model"
section_number: 2.5
pages: 8-10
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.903
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
[]{#sec:octsm label="sec:octsm"} In order to highlight the connection of the octonions to the standard mode, we now provide an explicit example of how the associative left multiplication algebra $\mathbb{C}\ell(6)$ generated from the adjoint actions of $\mathbb{C}\otimes\mathbb{O}$ can be used to represent one generation of standard model fermions with ${\rm{SU}}(3)\times {\rm{U}}(1)$ unbroken gauge symmetries.

### One Generation of Electrocolor States from $\mathbb{C}\otimes\mathbb{O}$ {#Furey}

Let $L_{e_1},...,L_{e_6}$ be a generating basis (over $\mathbb{C}$) for $\mathbb{C}\ell(6)$ associated with the left associative multiplication algebra of $\mathbb{C}\otimes\mathbb{O}$, satisfying the relations $L_{e_i}^2=-1$ and $L_{e_i}L_{e_j}=-L_{e_j}L_{e_i}$. Define a Witt basis for $\mathbb{C}\ell(6)$ as follows, $$\begin{aligned}
\alpha_1^\dagger &:= \frac{1}{2}(L_{e_1}+iL_{e_5}),& \alpha_2^\dagger &:= \frac{1}{2}(L_{e_2}+iL_{e_6}),& \alpha_3^\dagger &:= \frac{1}{2}(L_{e_3}+iL_{e_7}) \\
\alpha_1 &:= \frac{1}{2}(-L_{e_1}+iL_{e_5}), & \alpha_2 &:= \frac{1}{2}(-L_{e_2}+iL_{e_6}),& \alpha_3 &:= \frac{1}{2}(-L_{e_3}+iL_{e_7}) \:.
\end{aligned}$$ Here ${}^{\dagger}$ corresponds to the composition of complex conjugation and octonion conjugation. This new basis satisfies the anti-commutation relations $$\{\alpha_i,\alpha_j\}\, x = \{\alpha_i^{\dagger},\alpha_j^{\dagger}\}\, x=0,
\quad\{\alpha_i,\alpha_j^{\dagger}\}\, x=\delta_{ij}x,\qquad \text{for all~$x\in\mathbb{C}\otimes\mathbb{O}$} \:.$$ Both $\{\alpha_i\}$ and $\{\alpha_i^{\dagger}\}$ correspond to bases for the maximally isotropic subspaces $\chi$ and $\chi^{\dagger}$ respectively, because $$\{\alpha_i,\alpha_j\}=0 \quad \forall \alpha_i,\alpha_j\in \chi
\qquad \text{and} \qquad \{\alpha_i^{\dagger},\alpha_j^{\dagger}\}=0 \quad \forall \alpha_i^{\dagger},\alpha_j^{\dagger}\in\chi^{\dagger} \:.$$ Moreover, they generate the exterior algebras $\bigwedge \chi$ and $\bigwedge\chi^{\dagger}$ via the product of the Clifford algebra.

From this Witt basis it is possible to construct two minimal left ideals of the algebra $\mathbb{C}\ell(6)$, following the procedure in [@ablamowicz1995construction] (see [@furey2016standard] for a detailed construction): $$\mathbb{C}\ell(6)\,\omega\omega^{\dagger}=\bigwedge\chi^{\dagger}\omega\omega^{\dagger},\qquad \mathbb{C}\ell(6)\,\omega^{\dagger}\omega=\bigwedge\chi\omega^{\dagger}\omega \:,$$ where $\omega = \alpha_1\alpha_2\alpha_3$ and $\omega^\dagger = \alpha_3^\dagger\alpha_2^\dagger\alpha_1^\dagger$ are nilpotents, but $\omega\omega^{\dagger}$ and $\omega^{\dagger}\omega$ are primitive idempotents. Each minimal ideal has complex dimension eight. Explicitly, $$\notag
 \begin{split}
     S^u=&{\nu}\omega\omega^\dagger + \\  \overline{d^r}{\alpha_1^\dagger}\omega\omega^\dagger + &\overline{d^g}{\alpha_2^\dagger}\omega\omega^\dagger + \overline{d^b}{\alpha_3^\dagger}\omega\omega^\dagger + \\ u^r{\alpha_3^\dagger}{\alpha_2^\dagger}\omega\omega^\dagger + &u^g{\alpha_1^\dagger}{\alpha_3^\dagger}\omega\omega^\dagger + u^b{\alpha_2^\dagger}{\alpha_1^\dagger}\omega\omega^\dagger + \\ &e^+{\alpha_3^\dagger}{\alpha_2^\dagger}{\alpha_1^\dagger}\omega\omega^\dagger
\end{split}
\qquad 
\begin{split}
     S^d=&{\overline{\nu}}\omega^\dagger\omega + \\ {d}^r{\alpha_1}\omega^\dagger\omega + &{d}^g{\alpha_2}\omega^\dagger\omega +  {d}^b{\alpha_3}\omega^\dagger\omega + \\ \overline{u^r}{\alpha_3}{\alpha_2}\omega^\dagger\omega + &\overline{u^g}{\alpha_1}{\alpha_3}\omega^\dagger\omega + \overline{u^b}{\alpha_2}{\alpha_1}\omega^\dagger\omega + \\ &e^-{\alpha_3}{\alpha_2}{\alpha_1}\omega^\dagger\omega
\end{split}$$ where the suggestively labeled coefficients are elements of $\mathbb{C}$.

The subgroup of $\mathop{\mathrm{Spin}}(6)$ generated from the grade two elements of $\mathbb{C}\ell(6)$ that preserves the Witt basis, and hence the minimal left ideals, is the unitary symmetry ${\rm{U}}(3)={\rm{SU}}(3)\times {\rm{U}}(1)$. The generators of this symmetry, written in terms of the Witt basis elements, are: $$\begin{aligned}
 \notag
     \Lambda_1 &= -\alpha_2^\dagger\alpha_1 - \alpha_1^\dagger\alpha_2 \notag \hspace{2em}
     \Lambda_2 = i\alpha_2^\dagger\alpha_1 -i\alpha_1^\dagger\alpha_2 \notag \hspace{2em}
     \Lambda_3 = \alpha_2^\dagger\alpha_2 - \alpha_1^\dagger\alpha_1 \notag\\ 
     \Lambda_4 &= -\alpha_1^\dagger\alpha_3 - \alpha_3^\dagger\alpha_1 \notag \hspace{2em}
     \Lambda_5 = -i\alpha_1^\dagger\alpha_3 + i\alpha_3^\dagger\alpha_1 \notag \hspace{2em}
     \Lambda_6 = -\alpha_3^\dagger\alpha_2 - \alpha_2^\dagger\alpha_3 \notag\\
     \Lambda_7 &= i\alpha_3^\dagger\alpha_2 - i\alpha_2^\dagger\alpha_3 \notag \hspace{1em}
     \Lambda_8 = -\frac{1}{\sqrt{3}}(\alpha_1^\dagger\alpha_1 + \alpha_2^\dagger\alpha_2 - 2\alpha_3^\dagger\alpha_3), \notag
 
\end{aligned}$$ $$\notag
     Q = \frac{1}{3}(\alpha_1^\dagger\alpha_1 + \alpha_2^\dagger\alpha_2 + \alpha_3^\dagger\alpha_3).$$ The basis states of minimal ideals are then found to transform as $1\oplus 3\oplus\overline{3}\oplus1$ under ${\rm{SU}}(3)$, which can therefore be associated with the color symmetry ${\rm{SU}}(3)_C$, justifying the choice of coefficients. The ${\rm{U}}(1)$ generator $Q$ (together with $-Q^*$), related to the number operator $Q=N/3$, on the other hand, gives the correct electric charge for each state. The ideal $S^u$ contains the isospin up states, whereas the $S^d$ contains the isospin down states.

Two minimal ideal of  $\mathbb{C}\ell(6)$ arising as the associative left multiplication algebra of  $\mathbb{C}\otimes\mathbb{O}$ therefore provides an elegant representation of one generation of standard model electrocolor states. In this construction, the dimension of the minimal ideals (eight) corresponds to the number of distinct particle states, whereas the gauge symmetries are obtained as the subgroup of $\mathop{\mathrm{Spin}}(6)$ that preserves the Witt basis (and subsequently the minimal left ideals).
