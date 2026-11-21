---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-024-272-path-diagrams
section_title: "Path Diagrams"
section_number: 2.7.2
pages: 50-53
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.994
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secPathDiagrams label="secPathDiagrams"}

Function $f(\mathcal{R})_{lr}$ corresponds to the denominator of Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}) and it does not depend on where the operator $\hat{O}$ is placed,

::: flalign
f()\_lr &= \_S_0,S_N \^l_T\| R_0 S_0 R_0 S_0 \| \[U()\]\^N \| R_N S_N R\_N S\_N \| \^r_T \
& = f\^V\_lr() g\^F() . []{#fRlr label="fRlr"}
:::

Function $g(\mathcal{R})_{lr}$ corresponds to the numerator of Eq.([\[Oraw\]](#Oraw){reference-type="ref" reference="Oraw"}), and it depends on $\hat{O}_M$ defined in Eq.([\[Orawreduce\]](#Orawreduce){reference-type="ref" reference="Orawreduce"}) which means the operator $\hat{O}$ is placed at bead $M$ (its spatial configuration is $R_M$),

::: flalign
g()\_lr &= \_S_0,S_N \^l_T\| R_0 S_0 R_0 S_0 \| \[U()\]\^N_1 \_M \[U()\]\^N_2\| R\_N S\_N R\_N S\_N \| \^r_T\
&= g\^V\_lr,M() g\^F(). []{#gRlr label="gRlr"}
:::

Function $g^F(\mathcal{R})$ in Eqs.([\[fRlr\]](#fRlr){reference-type="ref" reference="fRlr"},[\[gRlr\]](#gRlr){reference-type="ref" reference="gRlr"}) is the total free particle propagator, $$g^F(\mathcal{R}) = \prod_{I=0}^{N-1} G^f_{I, I+1} ,
\label{gF}$$ where the free particle propagator $G^f_{I, I+1}$ in Eq.([\[gF\]](#gF){reference-type="ref" reference="gF"}) is defined as[^1], $$G^f_{I, I+1} \equiv \langle R_I | e^{-T \Delta \tau}  | R_{I+1} \rangle
= \left( \frac{m}{2\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}   e^{  -\frac{ (R_I-R_{I+1})^2 }{2 \Delta \tau \frac{\hbar^2}{m}}  },
\label{Gfii1}$$ and each of these free particle propagator is represented by the black curved line from below in Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}, it carries $\Delta \tau$ and it connects configuration $R_I$ and $R_{I+1}$ (or we can say it connects beads $I$ and $I+1$). Actually, We can see that the $\prod_{I=0}^{N-1}  G^f_{I, I+1}$ in functions $A_{lr} (\mathcal{R})$ and $B_{lr} (\mathcal{R})$ actually canceled out because they exist in both the denominators and the numerators.

Note that in $A_{lr} (\mathcal{R})$ and $B_{lr} (\mathcal{R})$ in Eqs.([\[Alrform\]](#Alrform){reference-type="ref" reference="Alrform"},[\[Blrform\]](#Blrform){reference-type="ref" reference="Blrform"}), both $f(\mathcal{R})_{lr}$ and $g(\mathcal{R})_{lr}$ contain $g^F(\mathcal{R})$, therefore $A_{lr} (\mathcal{R})$ and $B_{lr} (\mathcal{R})$ can be simplified as, $$\begin{aligned}

A_{lr} (\mathcal{R}) &= \frac{Re[ g^V_{lr,M}(\mathcal{R})]}{|Re[ f^V_{lr}(\mathcal{R})]|  } ,
\label{Alrsimpform} \\
B_{lr} (\mathcal{R}) &= \frac{Re[ f^V_{lr}(\mathcal{R})]}{|Re[ f^V_{lr}(\mathcal{R})]|  } .
\label{Blrsimpform}
\end{aligned}$$ The superscript $V$ in $g^V_{lr,M}(\mathcal{R})$ and $f^V_{lr}(\mathcal{R})$ means the potential propagators are involved.

<figure id="PIMCbeads">
<embed src="Figures/PIMCBeads.eps" />
<figcaption>Path diagrams which illustrate the PIMC beads, <span class="math inline"><em>f</em>(ℛ)<sub><em>l</em><em>r</em></sub></span>, and <span class="math inline"><em>g</em>(ℛ)<sub><em>l</em><em>r</em></sub></span>. </figcaption>
</figure>

Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"} is a visualization of $f(\mathcal{R})_{lr}$ in Eq.([\[fRlr\]](#fRlr){reference-type="ref" reference="fRlr"}) and $g(\mathcal{R})_{lr}$ in Eq.([\[gRlr\]](#gRlr){reference-type="ref" reference="gRlr"}). The calculations of functions $g^V_{lr,M}(\mathcal{R})$ in Eq.([\[Alrsimpform\]](#Alrsimpform){reference-type="ref" reference="Alrsimpform"}) and $f^V_{lr}(\mathcal{R})$ in Eq.([\[Blrsimpform\]](#Blrsimpform){reference-type="ref" reference="Blrsimpform"}) can be more clear with the help of Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"} which contains diagrams that visualize the path. By inserting $N+1$ complete basis marked by the black dots and labeling them from 0 to $N$, the total time $\tau$ is split into $N$ small time step $\Delta \tau$ so $\tau=N \Delta \tau$. We call each black dot a bead. For a given whole spatial configuration $\mathcal{R}$ defined by Eq.([\[defmathcalR\]](#defmathcalR){reference-type="ref" reference="defmathcalR"}), each of the beads carries its own spatial configuration. For example, the $I^{\text{th}}$ bead has spatial configuration $R_I$. The long black horizontal line represents the total imaginary time of the path $\tau$ and we can call it time line, and it has been split into $N$ pieces and occupied by $N+1$ beads. Each of the black curved lines from the bottom represents the corresponding free particle propagator, e.g., if the black curved line connects beads $I$ and $I+1$, the black curved line just represents the free particle propagator $G^f_{I, I+1}$ in Eq.([\[gF\]](#gF){reference-type="ref" reference="gF"}). The red curved line from the upper, on the other hand, represents the accordingly potential part of the propagator, e.g., we use $P_I$ to denote the red curved line as the corresponding $e^{\frac{- \mathcal{V}_I \Delta \tau }{2}}$ where $\mathcal{V}_I$ is defined in Eq.([\[PER\]](#PER){reference-type="ref" reference="PER"}) and it has spatial configuration $R_I$ while $P^\dagger_I$ is the Hermitian conjugate of $P_I$ which gives the reverse order of Eq.([\[propagatorv6half\]](#propagatorv6half){reference-type="ref" reference="propagatorv6half"}). The symbol $\downarrow$ means the additional propagator inserted when needed. For the AV6' interaction, $\downarrow$ means 1, for the local chiral N$^2$LO interaction it means the effective $\bm{\mathcal{G}}$ which is Eq.([\[defdownarroweff\]](#defdownarroweff){reference-type="ref" reference="defdownarroweff"}).

For a given $l$ and $r$ order in the trial wave function $\Psi_T$, and a given $\mathcal{R}$ of all the beads, the calculations of $f^V_{lr}(\mathcal{R})$ and $g^V_{lr,M}(\mathcal{R})$ are straightforward. Here we describe the computation rule which is basically a two-step process.

Step one

:   First of all, we just need to follow the order of beads in Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"} and replace all the red curves and $\downarrow$ symbols above the black time line with corresponding $e^{\frac{- \mathcal{V}_I \Delta \tau }{2}}$ or $e^{\frac{- \mathcal{V}^\dagger_I \Delta \tau }{2}}$ and the effective $\bm{\mathcal{G}}$. We next replace all of the black curve under the black time line with corresponding $g^F_{IJ}$ which are gaussian functions.

Step two

:   Then, for $f^V_{lr}(\mathcal{R})$ in the upper part in Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}, we just need to sandwich all the ordered operators above the black time line between $\langle \psi_T^l |$ and $| \psi_T^r \rangle$ to give a (complex) number. This number is the corresponding $f^V_{lr}(\mathcal{R})$. We multiply $f^V_{lr}(\mathcal{R})$ by $g^F(\mathcal{R})$ which is the product of all the black curved lines under the time line to find $f(\mathcal{R})_{lr}$.

The calculations of $g^V_{lr,M}(\mathcal{R})$ and $g(\mathcal{R})_{lr}$ are similar. The difference is that when calculating $g^V_{lr,M}(\mathcal{R})$, the additional operator $\hat{O}$ needs to be placed at the appropriate imaginary time as illustrated in the lower panel in Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"}.

[^1]: For any $R_I$ and $R_J$ on the time line which is represented by the long horizontal lines in Fig. [1](#PIMCbeads){reference-type="ref" reference="PIMCbeads"} on which there are black points (beads), the general form of the free particle propagator can be written as, $$G^f_{I, J} \equiv \langle R_I | e^{-T \Delta \tau |J-I| }  | R_{J} \rangle
    = \left( \frac{m}{2\pi |J-I| \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
    e^{  -\frac{ (R_I-R_{J})^2 }{2 |J-I| \Delta \tau \frac{\hbar^2}{m}}  },
    \label{Gfij}$$
