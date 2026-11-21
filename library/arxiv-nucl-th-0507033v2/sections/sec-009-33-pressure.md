---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter"
section_id: sec-009-33-pressure
section_title: "Pressure"
section_number: 3.3
pages: 10-11
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.791
latex_coverage_ratio: 0.995
doc_brief: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter — 15 sections: Front matter; Introduction; Formalism"
---
Next, we present our results for the pressure.  In Fig.~\ref{Fig10}, 
we plot the pressure of symmetric nuclear matter for $T=10 \mev$.
The formation of $\alpha$ particles reduces the 
total number of particles in the system, and 
this significantly lowers the pressure. For comparison, we also show 
in Fig.~\ref{Fig10} the microscopic Fermi hyper-netted-chain (FHNC) 
equation of state of Friedman and Pandharipande~\cite{FP}.  The
latter calculation is based on a variational wave function with only
two-nucleon correlations.  However, the model-independent virial 
equation of state shows that there are large $\alpha$ concentrations 
in this density regime.  For example, at the threshold density of 
$n_b=0.013 \fm^{-3}$ (from Fig. \ref{Fig9}) we have $x_\alpha 
= 0.40$.  Microscopic calculations may require wave functions 
with four-nucleon correlations to accurately describe these $\alpha$ 
particle contributions.  {\it This suggests that all present microscopic 
variational or Brueckner equations of state are incomplete in their
description of low-density nuclear matter.}  In Fig.~\ref{Fig10},
we also give the pressure for densities beyond the threshold density
of Fig.~\ref{Fig9} in order to compare virial and FHNC results, which
both omit the formation of heavy nuclei.

The error band in Fig.~\ref{Fig10} is again estimated from
a neglected third virial coefficient $b_{\text{nuc}}^{(3)} = \pm 10$.  
For the pressure, this involves a cancellation. Increasing 
$b_{\text{nuc}}^{(3)}$ decreases the nucleonic contribution 
to the pressure due to the additional attractive interaction 
between nucleons. However, a larger $b_{\text{nuc}}^{(3)}$ also 
reduces the formation of $\alpha$ particles (due to a lower alpha
chemical potential), and this acts to increase the total pressure.           
Therefore, a positive $b_{\text{nuc}}^{(3)}$ reduces the pressure
at very low densities, but then leads to a larger pressure with
increasing density.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{pressure_T4_Yp0.5.eps}
\caption{(Color online) The pressure $P$ of symmetric nuclear 
matter versus baryon density $n_b$ for $T=4 \mev$. As discussed 
in the text, these results include the contribution of an electron
and photon gas, and we also show the virial pressure without this
contribution. In addition, we give the results of the LS~\cite{LS} 
and Shen~\cite{Shen} equations of state. Over this density range, 
the fugacities are $z_n = z_p < 0.06$ and $z_\alpha < 0.01$.}
\label{Fig11}
\end{center}
\end{figure}


In Fig.~\ref{Fig11}, we show our results for the pressure of
symmetric nuclear matter for $T=4 \mev$ in comparison to the
phenomenological LS and Shen equations 
of state.  The pressure given in Fig.~\ref{Fig11} also includes 
the contribution of an electron and photon gas as in Appendix~C
of~\cite{LS}. We find the pressures given by the virial equation 
of state and the phenomenological models agree well.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{pressure_scaling.eps}
\caption{(Color online) The pressure $P$ of pure neutron matter 
and of symmetric nuclear matter calculated for $T=1$, $4$ and 
$8 \mev$ and scaled to a temperature of $T'=4 \mev$ (for details 
see text). The circle indicates where $z_n =0.5$ for pure neutron
matter. For symmetric nuclear matter, the fugacities are 
$z_n = z_p < 0.10$ and $z_\alpha < 0.09$ over this density range.}
\label{Fig12}
\end{center}
\end{figure}


In a separate paper~\cite{vEOSneut}, we have demonstrated that the 
equation of state of low-density neutron matter scales to a
very good approximation.  Table~\ref{Table1} shows that the
neutron virial coefficient $b_n(T)$ is practically independent 
of the temperature.  If all virial coefficients are 
temperature independent, and provided the condition for
chemical equilibrium does not introduce a strong temperature dependence
through $z_\alpha(z_n,z_p,T)$, then the power series in the 
fugacity for the pressure and the baryon density will have no 
explicit temperature dependence.  In this case, the pressure 
will scale as
\begin{equation}
P(n_b,T) = T^{5/2} \, f(n_b/T^{3/2}) \,,
\end{equation}
where $f(x)$ is some function of $n_b/T^{3/2}$.  If this scaling
relation holds, one can predict the pressure $P(n_b,T')$ at a new 
temperature $T'$ from the original $P(n_b,T)$ through
\begin{equation}
P(n_b,T')=\biggl(\frac{T'}{T}\biggr)^{5/2} P(\widetilde{n}_b,T) \,,
\label{pscale}
\end{equation}
with $n_b = (T'/T)^{3/2} \, \widetilde{n}_b$.

We study this scaling symmetry in Fig.~\ref{Fig12}, 
where we have used Eq.~(\ref{pscale}) to predict 
the pressure of neutron matter for $T'=4 \mev$ from virial pressures 
calculated for $T=1$ and $8 \mev$.  The agreement with the unscaled
$T=4 \mev$ virial pressure is excellent.  This demonstrates that 
low-density neutron matter scales, even when interactions are included.  
Fig.~\ref{Fig12} also shows scaled pressures of symmetric nuclear matter 
for $T'=4 \mev$ using $T=1$ and $8 \mev$ results as input.  
These scaled pressures 
do not agree with the $T=4 \mev$ virial pressure.  Therefore, nuclear 
matter does not scale, which is due to clustering and mainly 
comes as a result of the strong 
temperature dependence of $z_\alpha$ and $x_\alpha$. 


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{entropy_T4_Yp0.5_v2.eps}
\caption{(Color online) The entropy per baryon $S/A$ versus baryon 
density $n_b$ for $T=4 \mev$ and $Y_p=1/2$. As discussed in the text, 
these results include the contribution of an electron and photon gas. 
Also shown are results for the LS~\cite{LS}, Shen~\cite{Shen} and the 
Wolff~\cite{wolff} equations of state. 
The effects of interactions are illustrated by comparing to the
entropy of a free gas of nucleons and alpha particles.
Over this density range, 
the fugacities are $z_n = z_p < 0.11$ ($< 0.17$ for the free gas) 
and $z_\alpha < 0.17$ ($< 0.81$ free gas).}
\label{Fig13}
\end{center}
\end{figure}



\subsection{Entropy and Energy}

The entropy per baryon $S/A$ of symmetric nuclear matter is shown 
for $T=4 \mev$ in Fig.~\ref{Fig13}.  Here, our virial calculation 
again includes the entropy of an electron and photon gas as in
Appendix~C of~\cite{LS}.  The entropy is clearly seen to 
reflect the composition.  At low densities, the LS entropy is 
above the other calculations because of the low $\alpha$ mass
fraction in the LS model.  At high densities, the entropy in the
phenomenological models is below our virial result due to the 
formation of heavy nuclei.  This deviation coincides with the threshold
density of Fig.~\ref{Fig9}.  In Fig.~\ref{Fig13}, we also show 
the entropy per baryon for the Wolff equation of state~\cite{wolff},
to give a measure for the model dependence of the onset 
of heavy nuclei. The entropy per baryon for extremely 
neutron-rich matter $Y_p=0.05$ is shown in Fig.~\ref{Fig14}.  Now 
there is very little change in composition, and thus good agreement 
between the virial and phenomenological results.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{entropy_T4_Yp0.05.eps}
\caption{(Color online) The entropy per baryon $S/A$ versus baryon 
density $n_b$ for $T=4 \mev$ and $Y_p=0.05$. As discussed in the text, 
these results include the contribution of an electron and photon gas. 
Also shown 
are results for the LS~\cite{LS} and the Shen~\cite{Shen} equations 
of state. The circle indicates where $z_n =0.5$ ($z_p = 0.002$ and 
$z_\alpha = 0.001$).}
\label{Fig14}
\end{center}
\end{figure}


In addition to the entropy, we show our results for the energy
per baryon $E/A$ in Fig.~\ref{Fig15}.  In the limit of very low 
density, the energy reduces to the kinetic energy of an ideal 
classical gas $3T/2$.  Therefore, we have subtracted $3T/2$ from 
$E/A$ in Fig.~\ref{Fig15}, in order to clearly show the interaction 
effects. We find that the energy per baryon for pure neutron 
matter is somewhat below $3T/2$ due to the attractive nuclear 
interactions. Our neutron matter 
results are in excellent agreement with
the scaling law for the energy density $\epsilon = 3/2 P$,
which follows from Eq.~(\ref{epsilon}) when the virial coefficients 
are temperature independent, as is the case for neutron matter
with $b_n' \approx 0$. In contrast, $E/A$ for symmetric nuclear 
matter drops very rapidly with increasing density.  This reflects 
the large binding energy as $\alpha$ particles form. As can be seen
from Fig.~\ref{Fig15}, this drop becomes more rapid for lower 
temperatures.  We therefore expect that the inclusion of 
heavy nuclei, or many-nucleon correlations, are
necessary to obtain a constant energy per particle $E/A \approx 
-16 \mev$ for $T=0$ nuclear matter at subsaturation densities.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{energy_T4.eps}
\caption{(Color online) The energy per baryon $E/A$ versus baryon 
density $n_b$ for $T=4 \mev$ (and also $T=2 \mev$ (dotted) for 
nuclear matter). In order to clearly show the interaction 
effects we have subtracted the free kinetic energy $3T/2$ from 
all curves. The circle indicates where $z_n =0.5$ for pure neutron
matter. For symmetric nuclear matter, the fugacities are $z_n = z_p 
< 0.08$, $0.02$ and $z_\alpha < 0.03$, $0.11$ for $T=4$ and $2 \mev$ 
respectively.}
\label{Fig15}
\end{center}
\end{figure}
