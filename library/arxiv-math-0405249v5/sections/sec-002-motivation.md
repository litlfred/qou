---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-002-motivation
section_title: "motivation"
section_number: null
pages: 4-4
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
Twisted cyclic (co)homology arose from the study of covariant differential calculi over quantum groups [@kmt].

Let $\mathcal{A}$ be an algebra over $\mathbb{C}$. Given a differential calculus $(\Omega, d)$ over $\mathcal{A}$, with $\Omega = \oplus_{n=0}^N \; \Omega_n$, Connes [@connes1] considered linear functionals $\int : \Omega_N \rightarrow\mathbb{C}$, which are closed and graded traces on $\Omega$, meaning $$\int \; d \omega = 0 \quad \forall \; \omega \in \Omega_{N-1}$$ $$\label{closed}
\label{graded_trace}
\int \; \omega_m \omega_n = (-1)^{mn} \int \; \omega_n \omega_m \quad \forall \; \omega_m \in \Omega_m, \; \omega_n \in \Omega_n$$ Connes found that such linear functionals are in one to one correspondence with cyclic $N$-cocycles $\tau$ on the algebra, via $$\label{cyclic_cocycle}
    \tau( a_0, a_1, \ldots , a_N) = \int \; a_0 \; d a_1 \; d a_2 \ldots d a_N$$ which led directly to his simplest formulation of cyclic cohomology [@connes1].

If $\mathcal{A}$ is the coordinate algebra of a quantum group, then Woronowicz proposed to study covariant differential calculi, for which the left coaction of $\mathcal{A}$ on $\mathcal{A}$ given by the coproduct $\Delta : \mathcal{A}\rightarrow \mathcal{A}\otimes \mathcal{A}$ extends to a coaction $\Delta_L : \Omega \rightarrow\mathcal{A}\otimes \Omega$ compatible with the differential $d$ [@wo_suq2], [@wo_cmpg]. For such calculi the natural linear functionals $\int : \Omega_N \rightarrow\mathbb{C}$ are no longer graded traces, but twisted graded traces, meaning that $$\label{twisted_graded_trace}
\int \; \omega_m \omega_n = (-1)^{mn} \int \; \sigma(\omega_n) \omega_m \quad \forall \; \omega_m \in \Omega_m, \; \omega_n \in \Omega_n$$ for some degree zero automorphism $\sigma$ of $\Omega$. In particular, $\sigma$ restricts to an automorphism of $\mathcal{A}$, and, for any $a \in \mathcal{A}$, $\omega_N \in \Omega_N$ we have $$\label{int_aut}
\int \; \omega_N a = \int \; \sigma(a) \omega_N$$ Hence for each covariant calculus there is a natural automorphism of $\mathcal{A}$. Motivated by this observation, Kustermans, Murphy and Tuset defined "twisted" Hochschild and cyclic cohomology for any pair of an algebra $\mathcal{A}$ and automorphism $\sigma$, and showed that the one-to-one correspondence between graded traces and cyclic cocycles generalizes to this setting. The next section recalls their definitions, transposed to homology.
