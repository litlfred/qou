---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-013-152-formulation-of-a-pomp-model
section_title: "Formulation of a POMP model"
section_number: 1.5.2
pages: 12-14
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.946
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
We will first formulate a Markov transmission model and in a second step relate the data to the transmission model via some observation model which then gives us $f_{\bm{Y}_n|\bm{X}_{n}}$.\
**Transmission model** As transmission model we choose a stochastic SIR model among a closed population of $\mathcal{N}$ individuals where $\bm{X}(t)=(S(t), I(t), R(t))$ denotes the number of susceptible, infectious and recovered individuals at time $t$. Individuals are mixing homogeneously and $\beta$ is the average number of infectious contacts an infectious individual has per time unit. Furthermore, we assume that the time an individual is infectious is exponentially distributed with mean $\gamma ^{-1}$. We will now fromulate this in a way which makes understanding of the code in [@theresa_git] easier. So let $\{N_{AB}(t): t \geq 0\}$ denote a stochastic process which counts the number of individuals which have transitioned from compartment $A$ to compartment $B$ during the time interval $[0,t)$ with $A, B \in \mathcal{X}$, where $\mathcal{X}=\{S, I, R\}$ contains all model compartments. The infinitesimal increment probabilities of a jump between compartments fully specify the continuous-time Markov process describing the transmission dynamics. With the notation above, $\Delta N_{AB}(t)=N_{AB}(t+\tau)-N_{AB}(t)$ counts the number of individuals changing compartment in an infinitesimal time interval $\tau>0$. Thus, $$\begin{aligned}
\mathbb{P}[\Delta N_{SI}(t)=1 |\bm{X}(t)]&=  \beta I(t) S(t)\mathcal{N}^{-1}\tau +o(\tau) \quad \nonumber \\
\mathbb{P}[\Delta N_{IR}(t)=1 |\bm{X}(t)]&= \gamma I(t)\tau  +o(\tau). \quad\label{jump}
\end{aligned}$$

Moreover, the state variables and the transition probabilities ([\[jump\]](#jump){reference-type="ref" reference="jump"}) are related in the following way: $$\begin{aligned}
\Delta S(t)&= -\Delta N_{ SI}(t)  \nonumber\\
\Delta I(t)&= \Delta N_{ SI}(t)-\Delta N_{ IR}(t) \label{states}\\
\Delta R(t)&= \Delta N_{IR}(t). \nonumber
\end{aligned}$$ **Observation model** We now relate the transmission model to our observations of the weekly number of newly reported cases. With the notation above the true number of newly infected individuals accumulated in each observation time period $(t_{n-1},t_{n}], n \in \{1,2,\dots,N\}$ is given as $$H(t_n)=N_{SI}(t_{n})-N_{SI}(t_{n-1}).\label{obs_stoc}$$ To incorporate the count nature of the observations a natural assumption is to model the actual reported cases as realizations of a Poisson-distributed random variable with a given time-dependent mean. The number of recorded cases $Y_n$ within a given reporting interval $(t_{n-1},t_{n}],$ is then $$\begin{aligned}
Y_n &\sim \text{Pois}\left(  H(t_n)\right).
\label{poisson}
\end{aligned}$$ This distribution then corresponds to $f_{\bm{Y_n|\bm{X}_n}}$ which is easy to evaluate. One interpretation of this choice of observation noise is to account for uncertainty in classification of cases, including false positives.
