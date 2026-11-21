---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-010-141-algorithm
section_title: "Algorithm"
section_number: 1.4.1
pages: 10-12
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.876
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
[]{#mif_algorithm label="mif_algorithm"} In the following we present the pseudocode for iterated filtering as implemented in the `mif2` function in the `R` package `pomp` and explain how to draw samples from $f_{\bm{X}_n|\bm{X}_{n-1}}$.\
**Pseudocode iterated filtering (`mif2`)** cf. [@Ionides2015]\
**Input:** Simulators for $f_{\bm{X}_0}(\bm{x}_0;\boldsymbol{\theta})$ and $f_{\bm{X}_n|\bm{X}_{n-1}}(\bm{x}_n| \bm{x}_{n-1}; \boldsymbol{\theta})$; evaluator for $f_{\bm{Y}_n|\bm{X}_n}(\bm{y}_n|\bm{x}_n;\boldsymbol{\theta})$; data $\bm{y}^*_{1:N}$\
**Algorithmic parameters:** \# of iterations $M$; \# of particles $J$; initial parameter swarm $\{\boldsymbol{\theta}^0_j, j=1,\dots,J\}$; perturbation density $h_n(\boldsymbol{\theta}|\varphi;\sigma)$; perturbation scale $\sigma_{1{:}M}$\
**Procedure:**\
1. $\quad$ For $m$ in $1{:} M$\
2. $\quad\quad\quad$ $\boldsymbol{\theta}^{F,m}_{0,j}\sim h_0(\ \cdot \ |\bm{\theta}^{m-1}_{j}; \sigma_m)$ for $j$ in $1{:} J$\
3. $\quad\quad\quad$ $\bm{X}_{0,j}^{F,m}\sim f_{\bm{X}_0}(\ \cdot \ ; \bm{\theta}^{F,m}_{0,j})$ for $j$ in $1{:} J$\
4. $\quad\quad\quad$ For $n$ in $1{:} N$\
5. $\quad\quad\quad\quad\quad$ $\bm{\theta}^{P,m}_{n,j}\sim h_n(\ \cdot \ |\bm{\theta}^{F,m}_{n-1,j},\sigma_m)$ for $j$ in $1{:} J$\
6. $\quad\quad\quad\quad\quad$ $\bm{X}_{n,j}^{P,m}\sim f_{\bm{X}_n|\bm{X}_{n-1}}(\ \cdot \  |\bm{X}^{F,m}_{n-1,j}; \bm{\theta}^{P,m}_{n,j})$ for $j$ in $1{:} J$\
7. $\quad\quad\quad\quad\quad$ $w_{n,j}^m = f_{\bm{Y}_n|\bm{X}_n}(\bm{y}^*_n| \bm{X}_{n,j}^{P,m} ; \bm{\theta}^{P,m}_{n,j})$ for $j$ in $1{:} J$\
8. $\quad\quad\quad\quad\quad$ Draw $k_{1{:}J}$ with $P(k_j=i)=  w_{n,i}^m\Big/\sum_{u=1}^J w_{n,u}^m$\
9. $\quad\quad\quad\quad\quad$ $\bm{\theta}^{F,m}_{n,j}=\bm{\theta}^{P,m}_{n,k_j}$ and $\bm{X}^{F,m}_{n,j}=\bm{X}^{P,m}_{n,k_j}$ for $j$ in $1{:} J$\
10. $\quad\quad\quad$ End For\
11. $\quad\quad\quad$ Set $\bm{\theta}^{m}_{j}=\bm{\theta}^{F,m}_{N,j}$ for $j$ in $1{:} J$\
12. $\quad$ End For\
**Output:** Final parameter swarm, $\{\bm{\theta}^M_j, j=1,\dots,J\}$ \
In the algorithm the initial parameter values are perturbed (line 2) by a perturbation density where its standard deviation $\sigma_m$ is a decreasing function of $m$. The Markov process is initialized (line 3) as a draw from the initial density dependent on the proposed parameter vector. What follows in lines 4 - 10 is a particle filter as described in the section above with the only difference being that the parameter vector is stochastically perturbed in every iteration through the data. The $M$ loop repeats the particle filter with decreasing perturbations and throughout the algorithm the superscripts $F$ and $P$ denote filtering and prediction distribution, respectively. The algorithm returns the best guess of the parameter swarm after $M$ iterations. In the `R` package `pomp` the point estimate that the function `mif2` returns is the mean of the parameter swarm. To generate realizations from $f_{\bm{X}_n|\bm{X}_{n-1}}$ we can use the Gillespie algorithm [@gila]. Given the current state of the system, the algorithm simulates the waiting time of the next event and updates the number of individuals in each compartment and the overall time is incremented accordingly. The whole procedure is repeated until a pre-defined stopping time is reached. In the case of constant per capita transition rates, the simulation of every individual event gives us a complete and detailed history of the process, however, it is usually a very time-consuming task for systems with large population and state space, because of the enormous number of events that can take place. As a way to speed up such simulations an approximate simulation method can be used, the so called *$\tau$-leap algorithm* which is based on the Gillespie algorithm [@gil]. The $\tau$-leap algorithm holds all rates constant in a small time interval $\tau$ and simulates the numbers of events that will occur in this interval, then updates all state variables, computes the transition rates again and the procedure is repeated until the stopping time is reached [@taul; @into]. Given the total number of jumps, the number of individuals leaving any of the states by any available route during a time interval $\tau$ is then multinomially distributed. Note that the simulation time step is not identical with the time scale the observation process evolves on. Both simulation algorithms are conveniently implemented in the `pomp` package as the functions `gillespie.sim` and `euler.sim`.
