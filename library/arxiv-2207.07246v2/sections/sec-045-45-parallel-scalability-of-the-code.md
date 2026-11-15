---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-045-45-parallel-scalability-of-the-code
section_title: "Parallel Scalability of the Code"
section_number: 4.5
pages: 116-118
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.987
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
<figure id="figscaling">
<embed src="Figures/scaling.eps" />
<figcaption>The scaling efficiency of our PIMC code. It is based on sampling <span class="math inline">4 × 10<sup>5</sup></span> samples of <span class="math inline"><sup>4</sup></span>He for <span class="math inline"><em>τ</em> = 0.3 MeV<sup>−1</sup></span> with <span class="math inline"><em>Δ</em><em>τ</em> = 2 × 10<sup>−4</sup> MeV<sup>−1</sup></span>.</figcaption>
</figure>

Our code is parallel and uses the Message Passing Interface (MPI). Each CPU core is assigned the same amount of blocks of steps. At every about 125 steps, all the cores collect the values of the samples and send them to the rank 0 core. They also send the information about the current state $s$ to rank 0 for it to write them to a file which includes all the information of all these independent paths[^1]. The information of a state (path) as shown in Eq.([\[state_s\]](#state_s){reference-type="ref" reference="state_s"}), includes the spatial configuration of all the beads $\mathcal{R}$ and $l$ and $r$ order of the trial wave functions. The calculations are stopped when we have enough samples to make the error bar of each quantity smaller than the desired values.

Since the code is parallel, we checked the scaling of our PIMC code[^2] which is shown in Fig. [1](#figscaling){reference-type="ref" reference="figscaling"}. We plot the inverse of the total time it takes vs. the number of CPU cores involved. We expect that based on doing the same amount of work, the inverse of the total time it takes should be proportional to the number of the CPU cores. The labels on the right y-axis is the corresponding speedup, i.e., ideally the speedup for $n$ CPU cores should be $n$. The dotted line is the prediction based on the time 50 CPU cores takes. We can conclude from Fig. [1](#figscaling){reference-type="ref" reference="figscaling"} that our scaling is in the linear range so our MPI code is efficient.

# Conclusion {#secSumOutlook}

[^1]: Depending on the number of CPU cores, the number of beads in the PIMC calculation and the total computation time involved, a complete path file can take from tens of GB to several TB storage space. In the future we may use MPI/IO which can further improve the parallel scaling.

[^2]: All the calculations in this work are performed at the Agave cluster at Research Computing at Arizona State University during 2019 and 2020. The Cluster is mostly configured with Intel Xeon E5-2680v4 CPUs (CPU Architecture Broadwell) running at 2.40GHz at each node. Each node has 28 cores. Each core is configured with about 4.5GB of RAM. There are 297 nodes so there are 8316 cores ($\approx 320$ FP64 TFLOPS) and 4.5PB storage space. Sometimes we also use some Intel Xeon Gold 6230 and Intel Xeon Gold 6252 (CPU Architectures are both CascadeLake). Occasionally, we use several AMD EPYC 7551 (CPU Architecture is Naples) too. Our code currently does not run on coprocessors such as Intel Xeon Phi 7210 (CPU Architecture Knights Landing), because although each Xeon Phi CPU has hundreds of cores, each core is slow and does not have enough RAM. We checked the scaling only up to 500 cores simply because it is difficult to request much more than that number of cores to actually run the code on the Agave cluster.
