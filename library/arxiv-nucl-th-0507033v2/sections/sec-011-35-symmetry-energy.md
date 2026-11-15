---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter"
section_id: sec-011-35-symmetry-energy
section_title: "Symmetry Energy"
section_number: 3.5
pages: 12-13
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter — 15 sections: Front matter; Introduction; Formalism"
---
The symmetry energy $S_E$ characterizes how the energy rises as one 
moves away from equal numbers of neutrons and protons,
\begin{equation}
S_E = \frac{1}{8} \frac{\partial^2}{{\partial Y_p}^2} 
\frac{E}{A} \: \biggr|_{Y_p=1/2} \,.
\label{se}
\end{equation}
We evaluate the second derivative of the energy per baryon with
respect to the proton fraction numerically. Fig.~\ref{Fig16}
shows the symmetry energy for $T=4 \mev$.  At very low density, 
$S_E$ rises slowly with density. To lowest order in the density
and neglecting $\alpha$ particles, the symmetry energy is given by
\begin{equation}
S_E \approx \frac{3}{8} \, T \lambda^3 n_b (b_{pn} - 2 T b_{pn}^\prime/3
- b_n + 2 T b_n^\prime/3) \,.
\end{equation}
Then, as $\alpha$ particles form, $S_E$ rises much faster with 
density.  As a result of clustering, the symmetry energy 
is large even at a very small fraction of saturation density. 
This is analogous to the observed behavior for the energy.

We also show in Fig.~\ref{Fig16} the symmetry free energy $S_F$ defined as
\begin{equation}
S_F = \frac{1}{8} \frac{\partial^2}{{\partial Y_p}^2} 
\frac{F}{A} \: \biggr|_{Y_p=1/2} \,.
\label{sf}
\end{equation}
To lowest order in 
the density and neglecting $\alpha$ particles, the symmetry free energy 
is given by
\begin{equation}
S_F \approx \frac{T}{2}+\frac{1}{4} \, T \lambda^3 n_b (b_{pn}-b_n) \,,
\end{equation}
where the $T/2$ term is from the entropy of mixing in the free 
energy density.  Again, as $\alpha$ particles form, we find in 
Fig.~\ref{Fig16} that $S_F$ increases rapidly with density.

Finally, the temperature dependence of the symmetry energy is shown 
in Fig.~\ref{Fig17} for $T=2$, $4$ and $8 \mev$.  The lower the 
temperature, the more rapidly $S_E$ rises with density. We conclude 
that, in the thermodynamic limit, the symmetry energy is large at
low densities due to cluster formation.

Isospin observables in asymmetric heavy-ion collisions, such as
the $N/Z$ ration of emitted fragments, are often analyzed with
semiclassical simulations, where nucleons move in isospin-dependent
mean fields and undergo two-nucleon collisions. The isospin-dependent
mean-field implies a certain symmetry energy. The density dependence
of this symmetry energy can be adjusted to improve agreement with
the data, e.g., see~\cite{tsang}. This phenomenological symmetry
energy at low densities is in general much smaller than our
virial $S_E$. This is because the symmetry energy in the virial 
expansion includes the contributions of clusters with high central
densities even at low baryon density. The relation between $S_E$
and the symmetry energy of mean-field models for single nuclei
should therefore be investigated in future work.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{symenergy_T4.eps}
\caption{(Color online) The symmetry energy $S_E$ and the symmetry 
free energy $S_F$ versus baryon density $n_b$ for $T=4 \mev$. 
Also shown are virial results without $\alpha$ particles 
($z_\alpha=0$). Over this density range, the fugacities are 
$z_n = z_p < 0.09$ ($< 0.37$ without alphas) and $z_\alpha  < 0.06$.}
\label{Fig16}
\end{center}
\end{figure}



\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{symenergy_Ts.eps}
\caption{(Color online) The symmetry energy $S_E$ versus baryon 
density $n_b$ for $T=2$, $4$ and $8 \mev$. Over this
density range, the fugacities are 
$z_n = z_p < 0.02$, $0.09$, $0.13$ and
$z_\alpha  < 0.18$, $0.06$, $0.01$ for $T=2$, $4$, $8 \mev$.}
\label{Fig17}
\end{center}
\end{figure}
