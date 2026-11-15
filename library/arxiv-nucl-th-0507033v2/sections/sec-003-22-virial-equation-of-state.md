---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter"
section_id: sec-003-22-virial-equation-of-state
section_title: "Virial Equation of State"
section_number: 2.2
pages: 3-4
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.723
latex_coverage_ratio: 0.939
doc_brief: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter — 15 sections: Front matter; Introduction; Formalism"
---
We expand the grand-canonical partition function $\mathcal{Q}$ for a system of $n$, $p$ and $\alpha$ particles confined to a volume $V$ as $$\begin{aligned}
\mathcal{Q}(z_n,z_p,z_\alpha,V,T) &= 1 + z_n Q_n + z_p Q_p 
+ z_\alpha Q_\alpha
\nonumber \\[1mm]
&+ z_n^2 Q_{nn} + z_p^2 Q_{pp} + z_\alpha^2 Q_{\alpha\alpha}
\nonumber \\[1mm]
&+ 2z_pz_n Q_{np}+ 2z_nz_\alpha Q_{\alpha n} \nonumber \\[1mm]
&+ 2z_pz_\alpha Q_{\alpha p} + \mathcal{O}(z_i^3) \,.
\end{aligned}$$ Here, $Q_i=Q_i(V,T)$ and $Q_n$, $Q_p$ and $Q_\alpha$ are the partition functions for single particle $n$, $p$ or $\alpha$ systems $$\frac{Q_n}{V} = \frac{Q_p}{V} = \frac{2}{\lambda^3} \quad
\text{and} \quad \frac{Q_\alpha}{V} = \frac{1}{\lambda_\alpha^3} \,,$$ where $\lambda$ ($\lambda_\alpha$) denotes the nucleon ($\alpha$ particle) thermal wavelength, $$\lambda = (2\pi/mT)^{1/2} \quad \text{and} \quad \lambda_\alpha = 
(2\pi/m_\alpha T)^{1/2} \,.$$ We use $m_n=m_p$ for the nucleon mass $m$ and $m_\alpha=4m$ for the alpha particle mass, thus $\lambda_\alpha = \lambda/2$. Below, we will relate the two-particle partition functions $Q_{ij}=Q_{ij}(V,T)$ with $i,j=n,p,
\alpha$ to the second virial coefficients.

Next, we expand $\log \mathcal{Q}$ to second order in the fugacities $$\begin{aligned}
\frac{\log \mathcal{Q}}{V} &= 2 \, \frac{z_n}{\lambda^3} + 2 \, 
\frac{z_p}{\lambda^3} + \frac{z_\alpha}{\lambda_\alpha^3} +
z_n^2 \, \frac{Q_{nn}-\frac{1}{2}Q_n^2}{V} \nonumber \\[1mm]
&+ z_p^2 \, \frac{Q_{pp}-\frac{1}{2}Q_p^2}{V} 
+ z_\alpha^2 \, \frac{Q_{\alpha\alpha}-\frac{1}{2}Q_\alpha^2}{V} 
\nonumber \\[1mm]
&+ 2 z_p z_n \frac{Q_{np}-\frac{1}{2}Q_nQ_p}{V} 
+ 2 z_p z_\alpha \frac{Q_{\alpha p}-\frac{1}{2}Q_\alpha Q_p}{V} 
\nonumber \\[1mm]
&+ 2 z_n z_\alpha \frac{Q_{\alpha n}-\frac{1}{2}Q_\alpha Q_n}{V} 
+ \mathcal{O}(z_i^3) \,.
\end{aligned}$$ We define the second neutron virial coefficient $b_n$ as $$b_n = \frac{\lambda^3}{2V}(Q_{nn}-\frac{1}{2}Q_n^2) \approx 
\frac{\lambda^3}{2V}(Q_{pp}-\frac{1}{2}Q_p^2) \,,$$ where the second approximation is due to neglecting the Coulomb interaction between protons and assumes charge-independent nuclear interactions. Likewise, the second alpha virial coefficient $b_\alpha$ is given by $$b_\alpha=\frac{\lambda_\alpha^3}{V}(Q_{\alpha\alpha}-\frac{1}{2}Q_\alpha^2) \,,$$ and the virial coefficients describing strong interactions between $pn$ and N$\alpha$ particles are $$\begin{aligned}
b_{pn}&=\frac{\lambda^3}{2V}(Q_{np}-\frac{1}{2}Q_nQ_p) \,, \\[1mm]
b_{\alpha n}&=\frac{\lambda_\alpha^3}{V}(Q_{\alpha n}-\frac{1}{2}Q_\alpha Q_n)
\approx \frac{\lambda_\alpha^3}{V}(Q_{\alpha p}-\frac{1}{2}Q_\alpha Q_p) \,,
\end{aligned}$$ where again the second approximation neglects the Coulomb interaction and strong-interaction charge dependences. Coulomb effects typically depend on the ratio of the Coulomb energy to the thermal energy $\Gamma_i = Z_i^2 \alpha/a_i T$ [@Ichimaru], where $Z_i$ is the ion charge, $\alpha$ the fine structure constant, and $a_i = (3/4 \pi n_i)^{1/3}$ with $n_i$ the ion density. For example, for symmetric nuclear matter (assumed composed only of nucleons) at a density $n=10^{12} \, \text{g}/\text{cm}^{3}$ and $T=4 \, \text{MeV}$ one has $\Gamma_p = 0.05$, and thus we expect Coulomb effects to be small. However, this should be checked explicitly in future work and Coulomb interactions may be more important when we extend the virial approach to densities where heavy nuclei are present. Note that the choice of $\lambda_\alpha^3$ in the last equation (instead of $\lambda^3$) is our convention. Below, we will calculate these second virial coefficients from microscopic NN, N$\alpha$ and $\alpha\alpha$ elastic scattering phase shifts.

The pressure $P$ is given by the logarithm of the partition function, which we truncate after second order in the fugacities. In terms of the second virial coefficients, the pressure can be written as $$\begin{aligned}
\frac{P}{T}=\frac{\log \mathcal{Q}}{V}&=\frac{2}{\lambda^3}(z_n+z_p +
(z_n^2+z_p^2) b_n + 2 z_p z_n b_{pn}) \nonumber \\[1mm]
&+\frac{1}{\lambda_\alpha^3}(z_\alpha + z_\alpha^2 b_\alpha + 2 
z_\alpha (z_n+z_p) b_{\alpha n}) \,.
\label{p}
\end{aligned}$$ The $n$, $p$ and $\alpha$ densities follow from derivatives of $\log 
\mathcal{Q}$ with respect to the chemical potential or the fugacity, $$n_i = z_i \biggl(\frac{\partial}{\partial z_i} \frac{\log \mathcal{Q}}{V}
\biggr)_{V,T} \,.$$ The resulting $n$, $p$ and $\alpha$ particle densities are given by $$\begin{aligned}
n_n &= \frac{2}{\lambda^3}(z_n+2z_n^2b_n+2z_pz_nb_{pn}+8z_\alpha z_n 
b_{\alpha n}) \,, \label{nn} \\[1mm]
n_p &= \frac{2}{\lambda^3}(z_p+2z_p^2b_n+2z_pz_nb_{pn}+8z_\alpha z_p 
b_{\alpha n}) \,, \label{np} \\[1mm]
n_\alpha &= \frac{1}{\lambda_\alpha^3}(z_\alpha+2z_\alpha^2b_\alpha+
2z_\alpha(z_n+z_p)b_{\alpha n}) \,, \label{nalpha}
\end{aligned}$$ where we have used $\lambda^3/\lambda_\alpha^3=8$.

These equations provide a parametric form for the virial equation of state that is thermodynamically consistent. For values of $z_n$ and $z_p$, the alpha fugacity $z_\alpha$ follows from chemical equilibrium $z_\alpha = z_p^2 \, z_n^2 \, e^{E_\alpha/T}$ and one can then calculate the pressure $P$ and composition, $n_n$, $n_p$ and $n_\alpha$, from Eqs. ([\[p\]](#p){reference-type="ref" reference="p"},[\[nn\]](#nn){reference-type="ref" reference="nn"}-[\[nalpha\]](#nalpha){reference-type="ref" reference="nalpha"}). The total baryon density $n_b$ is given by $$n_b=n_n+n_p+4n_\alpha \,,
\label{nb}$$ and the proton fraction $Y_p$, the number of protons per baryon, by $$Y_p=(n_p+2n_\alpha)/n_b \,.
\label{yp}$$ The dependence of the baryon density and the proton fraction on $z_n$ and $z_p$ can be inverted to yield the virial equation of state in terms of $$P = P\bigl(z_n(n_b,Y_p,T),z_p(n_b,Y_p,T),z_\alpha(z_n,z_p,T),T\bigr) \,.$$ Note that these dependences are nonlinear and strongly temperature dependent, mainly due to the $e^{E_\alpha/T}$ term in the chemical equilibrium condition for $z_\alpha$. In practice, for a given proton fraction, we use Eq. ([\[yp\]](#yp){reference-type="ref" reference="yp"}) to determine the proton fugacity as a function of the neutron one $z_n(z_p,Y_p,T)$, and generate the virial equation of state in tabular form for a range of $z_n$. This maintains the thermodynamic consistency of the virial equation of state.
