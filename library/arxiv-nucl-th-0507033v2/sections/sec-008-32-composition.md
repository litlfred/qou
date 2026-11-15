---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter"
section_id: sec-008-32-composition
section_title: "Composition"
section_number: 3.2
pages: 7-10
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.932
doc_brief: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter — 15 sections: Front matter; Introduction; Formalism"
---
We now discuss the $\alpha$ particle concentration.  The $\alpha$ mass 
fraction is given by $x_\alpha=4n_\alpha/n_b$.  In Fig.~\ref{Fig4}, we 
show $x_\alpha$ for a temperature $T = 4 \mev$ and proton fraction 
$Y_p=1/2$ with various values of the virial coefficients.  
The largest $\alpha$ particle concentration results for 
a free $n$, $p$, $\alpha$ gas, where all $b_i = 0$. Including nucleonic
interactions $b_n, b_{pn}, b_{\text{nuc}} \neq 0$, but still keeping 
$b_\alpha, b_{\alpha n}=0$ reduces $x_\alpha$ significantly.  This is 
because the attractive nuclear interactions reduce the nucleon chemical 
potential, and this leads to a reduction of $x_\alpha$.  Including 
also $b_{\alpha n}\neq 0$ increases the $\alpha$ mass fraction,
but $x_\alpha$ is still smaller than its free value. The
latter effect is dominated by the low-energy N$\alpha$ resonance.
Finally, including $b_\alpha \neq 0$ only increases $x_\alpha$ by a very 
small amount. Therefore, in general, NN virial coefficients are expected 
to be most important, while the N$\alpha$ virial coefficient leads to
small changes, and $b_\alpha$ is least important.  This hierarchy is 
because typically $n_p+n_n > n_\alpha$.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{xalpha_T4_Yp0.5_b2s.eps}
\caption{(Color online) The $\alpha$ mass fraction $x_\alpha$ versus 
baryon density $n_b$ for $T = 4 \mev$, $Y_p = 1/2$ and various values 
of the virial coefficients, as explained in the text. The fugacities 
are small over this density range $z_n = z_p < 0.05$ and $z_\alpha < 0.004$.}
\label{Fig4}
\end{center}
\end{figure}


The LS model excludes nucleons from the volume occupied by alpha particles. 
Although this is a prescription, it leads to an $\alpha$ mass fraction that
vanishes in the high-density limit~\cite{LPRL}. The effects of the excluded
volume are small at low densities. However, the excluded volume corresponds 
to a repulsive N$\alpha$ interaction that reduces the $\alpha$ particle 
concentration. In contrast, the neutron-alpha resonance and the attractive
total phase shift leads to an attractive N$\alpha$ intraction in the virial 
expansion. As a result, the $\alpha$ mass fraction increases, as shown in 
Fig.~\ref{Fig4}. Therefore, the excluded volume alone gives the wrong sign 
for N$\alpha$ interactions in the low-density limit, but we caution that 
the effects of the excluded volume and the N$\alpha$ virial coefficient may be 
small at very low densities.

The third virial coefficient $b_{\text{nuc}}^{(3)}$ can be used to
make a simple error estimate of neglected terms in the virial expansion. 
From the above conclusion, we expect $b_{\text{nuc}}^{(3)}$ to be 
the most important of the third virial coefficients, and we therefore
take into account only $b_{\text{nuc}}^{(3)}$ in this estimate.  
For simplicity, we consider symmetric nuclear matter with $z_p=z_n=z$,
for which the virial equation of state, Eqs.~(\ref{p},\ref{nn}-\ref{nalpha}),
including $b_{\text{nuc}}^{(3)}$ reads
\begin{align}
\frac{P}{T} &= \frac{4}{\lambda^3}(z+z^2b_{\text{nuc}}
+z^3b_{\text{nuc}}^{(3)}) \nonumber \\[1mm]
&+\frac{1}{\lambda_\alpha^3}(z_\alpha
+z_\alpha^2 b_\alpha +4z_\alpha z\,b_{\alpha n}) \,, \\[1mm]
n &= n_p+n_n =\frac{4}{\lambda^3}(z+2z^2 b_{\text{nuc}}
+3z^3b_{\text{nuc}}^{(3)}+8z_\alpha z\,b_{\alpha n}) \,, \\[1mm]
n_\alpha &= \frac{1}{\lambda_\alpha^3}(z_\alpha + 2z_\alpha^2 b_\alpha 
+ 4 z_\alpha z\,b_{\alpha n}) \,.
\end{align}
In Fig.~\ref{Fig5}, we again plot the $\alpha$ mass fraction.  The solid 
line is our previous result with $b_{\text{nuc}}^{(3)}=0$.  We also 
give approximate error bands by considering $b_{\text{nuc}}^{(3)}=10$ 
(which gives a lower $x_\alpha$) and $b_{\text{nuc}}^{(3)}=-10$.  
This estimates the error only from the effect of a 
typical neglected term in the virial expansion.  Our estimate 
$|b_{\text{nuc}}^{(3)}|<10$ is somewhat arbitrary, as it is based 
on the observation that all second virial coefficients are comfortably 
less then 10 for $T=4 \mev$.  We see from Fig.~\ref{Fig5} that the 
resulting error band is small.  {\it Therefore, our virial 
expansion makes a model-independent prediction for the $\alpha$ particle 
concentration.}  We also contrast our results in Fig.~\ref{Fig5} to
the $x_\alpha$ predicted by two phenomenological equations of state.  
The Lattimer-Swesty (LS) equation of state~\cite{LS} is based on an 
extended liquid drop model and is almost universally used in modern 
supernova simulations.  The LS model predicts too few alpha particles 
over the densities where the virial equation of state is applicable.  
Alternatively, the Shen-Toki-Oyamatsu-Sumiyoshi (Shen) equation of
state~\cite{Shen} is based on an approximate Thomas Fermi calculation
using a relativistic mean-field interaction. The Shen equation of state
predicts slightly too high values for $x_\alpha$ at this temperature.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{xalpha_T4_Yp0.5.eps}
\caption{(Color online) The $\alpha$ mass fraction $x_\alpha$ 
versus baryon density $n_b$ for $T=4 \mev$ and $Y_p=1/2$.  The 
dotted error band for the virial equation of state is based on 
an estimate of a neglected third virial coefficient 
$b_{\text{nuc}}^{(3)} = \pm 10$. Also shown are results for 
the LS~\cite{LS} and Shen~\cite{Shen} equations of state.}
\label{Fig5}
\end{center}
\end{figure}



\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{xalpha_T4_Yps.eps}
\caption{(Color online) The $\alpha$ mass fraction $x_\alpha$ versus 
baryon density $n_b$ for $T=4 \mev$ and proton fractions $Y_p=0.1$, 
$0.2$, $0.3$, $0.4$ and $0.5$. For the lowest proton fraction $Y_p=0.1$,
the fugacities are $z_n < 0.2$, $z_p < 0.005$ and $z_\alpha < 0.001$ 
over this density range.}
\vspace*{-8mm}
\label{Fig6}
\end{center}
\end{figure}


It is a simple matter to apply the virial equation of state to 
different proton fractions and temperatures. In Fig.~\ref{Fig6}, 
we show how the $\alpha$ particle concentration decreases with 
decreasing proton fraction $Y_p$ for $T=4 \mev$. In addition,
we give $x_\alpha$ for $Y_p=1/2$ and a range of 
temperatures $T=2$, $4$ and $8 \mev$ in Fig.~\ref{Fig7}.
At the lowest temperature $T=2 \mev$, $x_\alpha$ rises rapidly at 
low densities where the virial coefficients make only small 
contributions.  Therefore the error band is very small.  The error 
band becomes more important for $T=8 \mev$.  The LS equation of 
state is seen to significantly underestimate $x_\alpha$ 
at all three temperatures.  This may be due to a simple oversight 
in the published version~\cite{LS} of the LS equation of state.  Lattimer
and Swesty include the neutron-proton mass difference in the 
proton chemical potential, but do not appear to include twice 
this difference in the alpha chemical potential.  In contrast,
the Shen equation of state is close to our virial 
results at low densities. However, both LS and Shen equations
of state predict too few $\alpha$ particles at high temperatures 
$T > 10 \mev$. This can be clearly seen from 
the $\alpha$ mass fraction shown in Fig.~\ref{Fig8} for $T= 20 \mev$.
The differences of the LS and Shen equations of state at the higher
densities shown for $T= 20 \mev$ in Fig.~\ref{Fig8} are due to the
differences in the symmetry energy~\cite{Jim}.


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{xalpha_Ts_Yp0.5.eps}
\caption{(Color online) The $\alpha$ mass fraction $x_\alpha$ versus 
baryon density $n_b$ for $T=2$, $4$ and $8 \mev$ and $Y_p=1/2$.  
The dotted error bands for the virial equation of state are based on 
an estimate of a neglected third virial coefficient 
$b_{\text{nuc}}^{(3)} = \pm 10$. Note that for $T=2 \mev$ 
the error band is very small. Also shown are results for the 
LS~\cite{LS} and Shen~\cite{Shen} equations of state. Over this
density range, the fugacities are 
$z_n = z_p < 0.03$, $0.10$, $0.16$ and
$z_\alpha  < 0.27$, $0.09$, $0.03$ for $T=2$, $4$, $8 \mev$.}
\vspace*{-5mm}
\label{Fig7}
\end{center}
\end{figure}



\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{xalpha_T20_Yp0.5.eps}
\caption{(Color online) The $\alpha$ mass fraction $x_\alpha$ versus 
baryon density $n_b$ for $T=20 \mev$ and $Y_p=1/2$.  
The dotted error bands for the virial equation of state are based on 
an estimate of a neglected third virial coefficient 
$b_{\text{nuc}}^{(3)} = \pm 10$. Also shown are results for the 
LS~\cite{LS} and Shen~\cite{Shen} equations of state. Over this
density range, the fugacities are $z_n = z_p < 0.21$ and
$z_\alpha  < 0.07$.}
\vspace*{-7mm}
\label{Fig8}
\end{center}
\end{figure}


Both phenomenological equations of state shown in Fig.~\ref{Fig7} 
give $\alpha$ particle concentrations that first increase with density and 
then rapidly decrease.  This decrease is due to the formation of 
heavy nuclei. Heavy nuclei are not included in our first studies.
We will extend the virial formalism to include heavy nuclei in
future work. Therefore, our virial results are currently limited 
to lower densities, where one does not expect large contributions 
from heavy nuclei. In Fig.~\ref{Fig9}, we plot the density above 
which the Shen equation of state has a heavy nuclei mass fraction
larger than 10\%.  This provides an estimate for the range of validity 
of the virial $n$, $p$, $\alpha$ equation of state. For this 
estimate we have considered the Shen instead of the LS model due
to the LS error in $x_\alpha$.    


\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{Shen_threshold.eps}
\caption{(Color online) The threshold baryon density $n_b$ above 
which the Shen equation of state~\cite{Shen} predicts a heavy
nuclei mass fraction larger than 10\%. This figure is for $Y_p=1/2$.}
\label{Fig9}
\end{center}
\end{figure}



\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{pressure_T10_Yp0.5_v2.eps}
\caption{(Color online) The pressure $P$ of symmetric nuclear 
matter versus baryon density $n_b$ for $T=10 \mev$. The dotted 
error band for the virial equation of state is based on an 
estimate of a neglected third virial coefficient 
$b_{\text{nuc}}^{(3)} = \pm 10$. Also shown are virial results 
without $\alpha$ particles ($z_\alpha=0$) and the microscopic 
FHNC results of Friedman and Pandharipande (FP)~\cite{FP}. 
The effects of interactions are illustrated by comparing to the
pressure of a free gas of nucleons and alpha particles.
Over this density range, the fugacities are $z_n = z_p < 0.21$ 
($< 0.51$ without alphas, $< 0.32$ for the free gas) and 
$z_\alpha  < 0.04$ ($< 0.17$ free gas).}
\label{Fig10}
\end{center}
\end{figure}
