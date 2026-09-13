---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-041-45-parallel-scalability-of-the-code
section_title: "Parallel Scalability of the Code"
section_number: 4.5
pages: 116-118
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
/s48 /s53/s48 /s49/s48/s48 /s49/s53/s48 /s50/s48/s48 /s50/s53/s48 /s51/s48/s48 /s51/s53/s48 /s52/s48/s48 /s52/s53/s48 /s53/s48/s48
/s48/s46/s48/s48
/s48/s46/s48/s50
/s48/s46/s48/s52
/s48/s46/s48/s54
/s48/s46/s48/s56
/s48/s46/s49/s48
/s48/s46/s49/s50
/s48/s46/s49/s52
/s48/s46/s49/s54
/s48/s46/s49/s56
/s78/s117/s109/s98/s101/s114/s32/s111/s102/s32/s67/s80/s85/s32/s99/s111/s114/s101/s115
/s49/s47/s84/s105/s109/s101/s32/s40/s104/s111/s117/s114
/s45/s49
/s41
/s48
/s53/s48
/s49/s48/s48
/s49/s53/s48
/s50/s48/s48
/s50/s53/s48
/s51/s48/s48
/s51/s53/s48
/s52/s48/s48
/s52/s53/s48
/s53/s48/s48
/s83/s112/s101/s101/s100/s117/s112
Figure 4.14: The scaling eﬃciency of our PIMC code. It is based on sampling 4× 105
samples of 4He for τ = 0.3 MeV−1 with ∆τ = 2× 10−4 MeV−1.
Our code is parallel and uses the Message Passing Interface (MPI). Each CPU
core is assigned the same amount of blocks of steps. At every about 125 steps, all the
cores collect the values of the samples and send them to the rank 0 core. They also
send the information about the current state s to rank 0 for it to write them to a ﬁle
106
which includes all the information of all these independent paths 9 . The information
of a state (path) as shown in Eq.(3.8), includes the spatial conﬁguration of all the
beadsR and l and r order of the trial wave functions. The calculations are stopped
when we have enough samples to make the error bar of each quantity smaller than the
desired values.
Since the code is parallel, we checked the scaling of our PIMC code 10 which is
shown in Fig. 4.14. We plot the inverse of the total time it takes vs. the number of
CPU cores involved. We expect that based on doing the same amount of work, the
inverse of the total time it takes should be proportional to the number of the CPU
cores. The labels on the right y-axis is the corresponding speedup, i.e., ideally the
speedup for n CPU cores should be n. The dotted line is the prediction based on the
time 50 CPU cores takes. We can conclude from Fig. 4.14 that our scaling is in the
linear range so our MPI code is eﬃcient.
9Depending on the number of CPU cores, the number of beads in the PIMC calculation and the
total computation time involved, a complete path ﬁle can take from tens of GB to several TB storage
space. In the future we may use MPI/IO which can further improve the parallel scaling.
10All the calculations in this work are performed at the Agave cluster at Research Computing at
Arizona State University during 2019 and 2020. The Cluster is mostly conﬁgured with Intel Xeon
E5-2680v4 CPUs (CPU Architecture Broadwell) running at 2.40GHz at each node. Each node has 28
cores. Each core is conﬁgured with about 4.5GB of RAM. There are 297 nodes so there are 8316
cores (≈ 320 FP64 TFLOPS) and 4.5PB storage space. Sometimes we also use some Intel Xeon Gold
6230 and Intel Xeon Gold 6252 (CPU Architectures are both CascadeLake). Occasionally, we use
several AMD EPYC 7551 (CPU Architecture is Naples) too. Our code currently does not run on
coprocessors such as Intel Xeon Phi 7210 (CPU Architecture Knights Landing), because although
each Xeon Phi CPU has hundreds of cores, each core is slow and does not have enough RAM. We
checked the scaling only up to 500 cores simply because it is diﬃcult to request much more than that
number of cores to actually run the code on the Agave cluster.
107
Chapter 5
