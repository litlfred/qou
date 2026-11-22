---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-035-33-path-updating-strategy
section_title: "Path Updating Strategy"
section_number: 3.3
pages: 87-88
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.99
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secUpdateStrat label="secUpdateStrat"}

In each type of sampling, after we judge whether to accept the new $l$ and $r$ order in the trial wave function or not, we mark the order after judgement as $l$ and $r$. In order to make the computation fast, as illustrated in Fig. [1](#PIMCpathstore){reference-type="ref" reference="PIMCpathstore"} by the blue and yellow bands with texture, we store all the states from $| \psi^r_0 (\mathcal{R}) \rangle$ to $| \psi^r_N (\mathcal{R}) \rangle$ and $| \psi^l_0 (\mathcal{R}) \rangle$ to $| \psi^l_N (\mathcal{R}) \rangle$, by storing all the coefficients from $\phi^r_{0}(\mathcal{R},S)$ to $\phi^r_{N}(\mathcal{R},S)$ and from $\phi^l_{0}(\mathcal{R},S)$ to $\phi^l_{N}(\mathcal{R},S) | S \rangle$ in the arrays. We also store $f^V_{lr}(\mathcal{R})$ which is calculated by Eq.([\[fVRlrN2LOdef2\]](#fVRlrN2LOdef2){reference-type="ref" reference="fVRlrN2LOdef2"}).

<figure id="PIMCpathstore">
<embed src="Figures/PIMCpathstore.eps" />
<figcaption>Illustration of the path updating.</figcaption>
</figure>

Then, we propose new moves as $\mathcal{R}'$. In order to judge if the new spatial configuration $\mathcal{R}'$ is accepted or not, we need to calculate ${ f^V_{lr}(\mathcal{R}')}/{ f^V_{lr}(\mathcal{R})}$. For the $\mathcal{R}'$, it is usually the same as $\mathcal{R}$ except for several contiguous beads. For example in the multi-level sampling with level $n$, for a chosen integer $I$, we only propose new configurations from bead $I+1$ to bead $I+2^n-1$ in $\mathcal{R}'$, and the rest of the beads remain the same as those in $\mathcal{R}$. When we propose new moves from bead $I+1$ to bead $I+2^n-1$, we only need to calculate from right to left, from $\phi^r_{I+2^n-1}(\mathcal{R}',S)$ until $\phi^r_{I+1}(\mathcal{R}',S)$, by using the recursion relations Eq.([\[phirMRrecur\]](#phirMRrecur){reference-type="ref" reference="phirMRrecur"}) starting from $\phi^r_{I+2^n}(\mathcal{R},S)$ which is already stored. Then we calculate $f^V_{lr}(\mathcal{R}')= \left\langle \psi^{l'}_I (\mathcal{R}) \left| \bm{\mathcal{G}}\right| \psi^{r'}_{I+1} (\mathcal{R}') \right\rangle$, and since $f^V_{lr}(\mathcal{R})$ is also already stored, we can readily calculate ${ f^V_{l'r'}(\mathcal{R}')}/{ f^V_{lr}(\mathcal{R})}$. If the proposed new moves are accepted, we update all the rest beads. From right to left we update from $\phi^r_{I}(\mathcal{R}',S)$ until $\phi^r_{0}(\mathcal{R}',S)$, and from left to right we update from $\phi^r_{I+1}(\mathcal{R}',S)$ until $\phi^r_{N}(\mathcal{R}',S)$. In Fig. [1](#PIMCpathstore){reference-type="ref" reference="PIMCpathstore"}, the corresponding updated parts of the path from left to right are marked as green band, and those updated from right to left are marked as the red band.

The path updating process is the most time-consuming part, especially if the number of beads $N$ is large. So we find a proper $n$ in multi-level sampling to make sure $n$ is big enough to ensure the acceptance rate is relatively low, in order to optimize the decorrelation of the path within the computer time.
