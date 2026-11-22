---
doc_id: arxiv-1712.03058v3
doc_title: "Iterated ﬁltering methods for Markov process epidemic models"
section_id: sec-017-17-rotavirus-example
section_title: "Rotavirus example"
section_number: 1.7
pages: 21-24
source_pdf: 1712.03058v3.pdf
source_sha256: ba48c5bbb2467374
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.98
doc_brief: "Iterated ﬁltering methods for Markov process epidemic models — Dynamic epidemic models have proven valuable for public health decision makers as they provide useful insights into the understanding"
---
[]{#rota_example label="rota_example"} After presenting a simple toy example as a proof of concept, we now give a short illustration of a real-world problem which accommodates some of the complications presented in the previous section and was analyzed with iterated filtering. A detailed description of the model and inference results can be found in [@Stocks2017].\
The data which were analyzed in that paper are the weekly reported number of new laboratory-confirmed rotavirus cases among children, adults and elderly from 2001 until 2008 in Germany, scaled up by an underreporting rate (cf. Section [\[complications\]](#complications){reference-type="ref" reference="complications"}) as inferred and described in more detail in [@wei1]. Surveillance of rotavirus infection is relevant to public health authorities because it is the primary cause for severe gastroenteritis in infants and young children and causes significant morbidity, mortality and financial burdens worldwide [@wales]. Individuals can get the disease more than once but the highest reported incidence is observed in children under the age of 5 and rises again later in life. Parameter estimation from surveillance data is crucial if one wants to e.g. assess the effect of vaccination campaigns or other public health control measures.\
In [@Stocks2017] the disease transmission was modeled as an age-stratified SIRS Markov process with overdispersion in the observation (cf. Equation ([\[nbin\]](#nbin){reference-type="ref" reference="nbin"})) as well as in the transmission model (cf. Equation ([\[gammawnoise\]](#gammawnoise){reference-type="ref" reference="gammawnoise"})). As rotavirus in Germany varies seasonally peaking around March, a forcing function (cf. Equation ([\[forcing\]](#forcing){reference-type="ref" reference="forcing"})) was used.\
Here, we will present a simplified version of the model which ignores age-structure and perform inference for one realization of this model; the simulated case report data (black line) is shown in Figure [1](#rota){reference-type="ref" reference="rota"}. The initial values were fixed at the stationary distribution of the system and the waning of immunity rate, $\omega>0$, was also assumed to be fixed and known. With the notation as in Section [\[examplesir\]](#examplesir){reference-type="ref" reference="examplesir"}, this translates mathematically into $$\begin{aligned}
\mathbb{P}[\Delta N_{\centerdot S}(t)=1 |\bm{X}(t)]&=  \mu \mathcal{N} \tau +o(\tau)  \nonumber \\
\mathbb{P}[\Delta N_{SI}(t)=1 |\bm{X}(t)]&=  \beta(t) I(t) S(t)\mathcal{N}^{-1}\tau +o(\tau) \quad \nonumber \\
\mathbb{P}[\Delta N_{IR}(t)=1 |\bm{X}(t)]&= \gamma I(t)\tau  +o(\tau) \quad\label{jump_rota}\\
\mathbb{P}[\Delta N_{RS}(t)=1 |\bm{X}(t)]&= \omega R(t)\tau +o(\tau)  \nonumber\\
\mathbb{P}[\Delta N_{A \centerdot}(t)=1 |\bm{X}(t)]&= \mu A(t)\tau  +o(\tau) \quad \text{with $A\in \{S,I, R\}$} \nonumber 
\end{aligned}$$ where $\mu>0$ denotes the birth and death rate which was assumed to be constant and known. Moreover, $N_{\centerdot A}(t)$ counts the number of births and $N_{A \centerdot}(t)$ counts the number of deaths with $A \in \mathcal{X}$ in the respective compartment up until time $t$. The seasonal-forced transmission rate was defined as $$\beta(t)= \beta \left(1+\rho\cos\left(\frac{2\pi}{w} t +\phi\right)\right) \xi(t), 
\label{forcing}$$ where $\xi(t)$ is defined as in Equation ($\ref{gammawnoise}$). The transition probabilities from ([\[jump_rota\]](#jump_rota){reference-type="ref" reference="jump_rota"}) are related to the state variables in the following way: $$\begin{aligned}
\Delta S(t)&= \Delta N_{ \centerdot S}(t)-\Delta N_{ SI}(t) +  \Delta N_{RS}(t)-\Delta N_{S \centerdot}(t) \nonumber\\
\Delta I(t)&= \Delta N_{ SI}(t)-\Delta N_{ IR}(t)-\Delta N_{I \centerdot}(t) \nonumber\\
\Delta R(t)&= \Delta N_{IR}(t)-\Delta N_{RS}(t)-\Delta N_{R \centerdot}(t). \nonumber
\end{aligned}$$ With this notation the true number of newly infected individuals accumulated in each observation time period $(t_{n-1},t_{n}]$, $n \in \{1,2,\dots,N\}$ is given as $$H(t_n)=N_{SI}(t_{n})-N_{SI}(t_{n-1}).\label{obs_stoc}$$ The number of recorded cases $Y_n$ within this time period was modeled as $$\begin{aligned}
Y_n &\sim \text{NegBin}\left( H(t_n), \frac{1}{\psi}\right),
\end{aligned}$$ compare Equation ([\[nbin\]](#nbin){reference-type="ref" reference="nbin"}). In this example we inferred the susceptibility parameter $\beta$, the seasonal forcing parameters $\rho$ and $\phi$ and the overdispersion parameters $\sigma$ and $\psi$, hence $\bm{ \theta}=(\beta, \rho,\phi,\sigma, \psi)'$. A diagnostic plot similar to the one in Figure [\[mif\]](#mif){reference-type="ref" reference="mif"} (available online) shows that the iterated filtering algorithm performs well as the parameter estimates converge towards the parameters used for simulation. Figure [1](#rota){reference-type="ref" reference="rota"} shows the model evaluated at the MLE obtained from the iterated filtering. Further implementational details for this example are available at [@theresa_git].\
The aim of the analysis in [@Stocks2017] was to compare the impact of different kinds of variabilities in the transmission as well as the observation model. The paper concluded that a model which accounts for overdispersion in both model components (dark and light shading in Figure [1](#rota){reference-type="ref" reference="rota"}) is best suited to explain the analyzed data. The strength of using iterated filtering in this context was that the method allowed for efficient maximum likelihood estimation for a POMP where the underlying transmission model was stochastic. Hence, it facilitated model comparison with respect to different choices of variability in both model components.

<figure id="rota">
<div class="center">
<embed src="child_study.pdf" style="width:11.5cm" />
</div>
<figcaption>The 95% prediction interval (light shading) for 1000 realizations of the model for rotavirus evaluated at the maximum likelihood estimate for the simulated case report data (solid back line) and the median (solid white line). Furthermore, the 95 % prediction interval of these 1000 realizations for only the transmission model is shown (darker shading). </figcaption>
</figure>
