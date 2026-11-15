---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-018-23-model-space
section_title: "Model Space"
section_number: 2.3
pages: 33-35
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.98
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secModSpace label="secModSpace"}

The interaction used in this work will not change the total number of $Z$ protons and $A-Z$ neutrons[^1], so the number of possible isospin states is $\binom {A}{Z}$. However the tensor part $S_{ij}$ can flip spin, so the possible number of spin states is $2^A$. Therefore, as stated before, the total number of spin-isospin basis states is, $$N_{\rm{tot}}= \binom {A}{Z} \times 2^A = \frac{A!}{Z!(Z-A)!} \times 2^A.
\label{Nbasistotal}$$

Take $^4$He as an example, it has $N_{\rm{tot}}=6 \times 16=96$ spin-isospin basis states. In other words, our Hilbert space is constructed by the 96 basis states and therefore a general state is the linear combination of these basis states. We mark these basis states as $| S \rangle$ and $S$ can be labeled from 1 to 96, $$| S \rangle \equiv  | s_1\rangle \otimes | s_2 \rangle \otimes | s_3 \rangle \otimes | s_4 \rangle \equiv | s_1 s_2 s_3 s_4 \rangle, \label{basisS}$$ where $s_i$ means the spin isospin state of particle i, it can be any state from neutron spin up $|n \uparrow \rangle$, neutron spin down $|n \downarrow\rangle$, proton spin up $|p \uparrow\rangle$, proton spin down $|p \downarrow\rangle$. In Eq.([\[basisS\]](#basisS){reference-type="ref" reference="basisS"}), we implicitly mean particle 1 is at $s_1$ state, particle 2 is at $s_2$ state, particle 3 is at $s_3$ state and particle 4 is at $s_4$ state. To be clear, it is really, $$| S \rangle \equiv  | s^1_1\rangle \otimes | s^2_2 \rangle \otimes | s^3_3 \rangle \otimes | s^4_4 \rangle
\equiv | s^1_1 s^2_2 s^3_3 s^4_4 \rangle, \label{basisSmoreclear}$$ where the subscript (the state label) 1 to 4 represents state 1 to state 4, and the superscript (particle label) from 1 to 4 represents particle 1 to particle 4.

We denote the spatial configuration of a system with $A$ particles as $R$, $$R \equiv ( \bm{r}_1, \bm{r}_2, ..., \bm{r}_A  ) , \label{Rdef}$$ where $\bm{r}_i=(x_i,y_i,z_i)$ is the coordinates of particle i. The coordinate space configuration $R$ of $^4$He can also be written as a state $| R \rangle$, $$| R \rangle \equiv  | \bm{r}_1\rangle \otimes | \bm{r}_2 \rangle \otimes | \bm{r}_3 \rangle \otimes | \bm{r}_4 \rangle \equiv | \bm{r}_1 \bm{r}_2 \bm{r}_3 \bm{r}_4 \rangle. \label{basisR}$$ Similar with Eq.([\[basisSmoreclear\]](#basisSmoreclear){reference-type="ref" reference="basisSmoreclear"}), Eq.([\[basisR\]](#basisR){reference-type="ref" reference="basisR"}) really means, $$| R \rangle \equiv  | \bm{r}^1_1\rangle \otimes | \bm{r}^2_2 \rangle \otimes | \bm{r}^3_3 \rangle \otimes | \bm{r}^4_4 \rangle
\equiv | \bm{r}^1_1 \bm{r}^2_2 \bm{r}^3_3 \bm{r}^4_4 \rangle. \label{basisRmoreclear}$$

Taking $R$ and the spin isospin state $S$ in to account, our basis state $| RS \rangle$ can finally be written as, $$| RS \rangle = | R \rangle \otimes | S \rangle
\equiv | \bm{r}_1 \bm{r}_2 \bm{r}_3 \bm{r}_4 \rangle \otimes | s_1 s_2 s_3 s_4 \rangle , \label{basisRS}$$

The correspondingly identity operators for our basis are,

::: flalign
dR \| R R \| &= 1 , []{#identityR label="identityR"}\
\_S \| S S \| &= 1 , []{#identityS label="identityS"}\
\_S dR \| RS RS \| & = dR \| R R \| \_S \| S S \| = 1 . []{#identityRS label="identityRS"}
:::

In fact, without the Coulomb interaction, for $^4$He it is possible to use two $|T=0\rangle$ states (T is the total isospin quantum number) to couple with 16 spin states to form 32 basis. And due to the fact that the Hamiltonian has time-reversal symmetry, only 16 of the 32 basis states are independent, therefore we can use 16 states to form the Hilbert space instead of 96. However the Coulomb interaction does not commute with the total isospin operator, it does not conserve total isospin and can generate $T\neq 0$ states, therefore the 16 spin/isospin states with $T=0$ cannot be used when the Coulomb interaction was present. And this is why we use the 96 states in this work.

[^1]: The AV6' and local chiral N$^2$LO we use in this work conserve the number of isospin states. For example, for $^4$He we begin with $\binom {4}{2}=6$ different isospin states, the interaction we use always generate isospin states within these 6 states, they do not generate isospin states other than these 6 states.
