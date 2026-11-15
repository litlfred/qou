---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-000-abstract
section_title: "ABSTRACT"
section_number: null
pages: 2-4
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
I describe the ﬁrst continuous space nuclear path integral quantum Monte Carlo
method, and calculate the ground state properties of light nuclei including Deuteron,
Triton, Helium-3 and Helium-4, using both local chiral interaction up to next-to-
next-to-leading-order and the Argonne v′
6 interaction. Compared with diﬀusion based
quantum Monte Carlo methods such as Green’s function Monte Carlo and auxiliary
ﬁeld diﬀusion Monte Carlo, path integral quantum Monte Carlo has the advantage
that it can directly calculate the expectation value of operators without tradeoﬀ,
whether they commute with the Hamiltonian or not. For operators that commute
with the Hamiltonian, e.g., the Hamiltonian itself, the path integral quantum Monte
Carlo light-nuclei results agree with Green’s function Monte Carlo and auxiliary ﬁeld
diﬀusion Monte Carlo results. For other operator expectations which are important
to understand nuclear measurements but do not commute with the Hamiltonian and
therefore cannot be accurately calculated by diﬀusion based quantum Monte Carlo
methods without tradeoﬀ, the path integral quantum Monte Carlo method gives reliable
results. I show root-mean-square radii, one-particle number density distributions, and
Euclidean response functions for single-nucleon couplings. I also systematically describe
all the sampling algorithms used in this work, the strategies to make the computation
eﬃcient, the error estimations, and the details of the implementation of the code to
perform calculations. This work can serve as a benchmark test for future calculations
of larger nuclei or ﬁnite temperature nuclear matter using path integral quantum
Monte Carlo.
i
Flowers may bloom over and over again, but people can never be young again.
花有重开日，人无再少年。
To my parents Chen Wei and Yuan Mao-Ying.
向我的老爸老妈陈伟和袁茂英致意。
ii
