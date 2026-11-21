---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-036-34-sampling-strategies
section_title: "Sampling Strategies"
section_number: 3.4
pages: 88-90
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.979
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secSampStrat label="secSampStrat"}

We have tested all the algorithms described in this chapter. We have also tested the bisection method ([@Ceperley95a]), as well as the reptation Monte Carlo method ([@Baroni99a; @Baroni10a]) for our calculation. For our light nuclei PIMC calculation, as pointed out in section [\[secMultibeadSample\]](#secMultibeadSample){reference-type="ref" reference="secMultibeadSample"}, we did not find any advantage for bisection over the multi-level sampling method. The reptation method basically samples the spatial configuration of the path by adding some beads at one end of the path, and removing some beads to the other end of the path. However, since we have spin and isospin sums in the path, the removing and adding of beads, even if just one bead is involved, requires the recalculation of the whole path $f^V_{l'r'}(\mathcal{R}')$. Therefore it is not economical to perform reptation moves. After initial testing we did not pursue reptation moves further.

The multi-level sampling is efficient so we do not do regular sampling described in section [\[secregularsampling\]](#secregularsampling){reference-type="ref" reference="secregularsampling"} very often. The importance sampling also does not make much difference. Considering that the importance sampling at least needs to calculate the two possibilities $\pi(s'_1)$ and $\pi(s'_2)$ and an additional $\pi(s_2)$, we did not find it particularly increase the efficiency. Again we turned off the importance sampling in our calculations. So when performing our calculations, about $90\%$ moves are proposed by multi-level sampling described in section [\[secMultibeadSample\]](#secMultibeadSample){reference-type="ref" reference="secMultibeadSample"}, and the other $10\%$ are proposed by different kinds of regular sampling described in section [\[secregularsampling\]](#secregularsampling){reference-type="ref" reference="secregularsampling"}.

For multi-level sampling, for the total $N+1$ beads along the path, we pick two lengths, $n_1 \approx N/3$ and $n_2 \approx N/6$. And, $80\%$ of the moves are proposed for $n_1$ beads and the others are for $n_2$ beads. The acceptance rate for sampling $n_1$ beads is about $20\%$, for $n_2$ beads is about $40\%$. The reason for sampling $n_2$ beads is mainly to include the and the $N^{\text{th}}$ beads. For example, if we have a total of 400 beads, we can pick $n_1=2^7=128$ and $n_2=2^6=64$. $80\%$ moves are proposed for the $n_1=128$ beads with acceptance rate around $20\%$, and the other $20\%$ of the moves among the total multi-level samplings are for $n_2=64$ beads with an acceptance rate around $40\%$.

For the different kinds of regular sampling which make the samples more uncorrelated than applying multi-level sampling alone, we include moving beads one by one, moving all the beads at the same time, and shifting all the beads at the same time, according to section [\[secregularsampling\]](#secregularsampling){reference-type="ref" reference="secregularsampling"}. By moving beads one by one, we randomly pick a direction, either propose moves from bead $N$ to bead $0$, or propose moves from bead $0$ to bead $N$. For each bead, we move each particle in it and we choose the step parameter $\alpha$ to make the acceptance rate around $50\%$. By moving all the beads at the same time, we move all the particles in each bead, the step parameter $\alpha$ needs to be smaller than when moving beads one by one, in order to make the acceptance rate of moving all the beads at the same time around $50\%$ again. By shifting all the beads at the same time, we propose to move each of the beads by using Eq.([\[shiftmove\]](#shiftmove){reference-type="ref" reference="shiftmove"}). The step parameter in the common $\Lambda$ vector is again adjusted to make the acceptance rate of shifting all the beads around $50\%$. The overall efficiency of the algorithm is not substantially affected by these acceptance rates as long as they are in the 20% to 80% range.

# Ground state calculations of light nuclei {#RsDs}
