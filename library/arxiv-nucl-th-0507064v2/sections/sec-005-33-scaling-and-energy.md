---
doc_id: arxiv-nucl-th-0507064v2
doc_title: "The Virial Equation of State of Low-Density Neutron Matter"
section_id: sec-005-33-scaling-and-energy
section_title: "Scaling and Energy"
section_number: 3.3
pages: 5-6
source_pdf: 0507064v2.pdf
source_sha256: dcfad7240ba81bf5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.959
doc_brief: "The Virial Equation of State of Low-Density Neutron Matter — 10 sections: Front matter; Introduction; Virial Equation of State"
---
\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{pressure_neut_scaling.eps}
\caption{(Color online) The pressure $P$ versus density $n$
calculated for $T=1$, $4$, $8$ and $20 \mev$ and scaled to a 
temperature of $T'=4 \mev$ (for details see text). The lower
curves are results for the scaled pressures obtained with a 
virial coefficient calculated only from the S-wave scattering length
$a_{np}$. The latter curves have been shifted for better readability.
The circles indicate where the fugacity is $z =0.5$, and for this
density range, the fugacity is $z<0.87$.}
\label{Fig3}
\end{center}
\end{figure}



\begin{figure}[t]
\begin{center}
\includegraphics[scale=0.36,clip=]{energy_neut.eps}
\caption{(Color online) The energy per particle $E/N$ versus
density $n$ for $T=4$, $8$ and $20 \mev$. In order to clearly 
show the interaction effects we have subtracted the free kinetic 
energy $3T/2$ from all curves. The energy per particle
obtained using the universal relation $\epsilon = 3P/2$ with
the corresponding virial pressures are indistinguishable from
these curves. The circles indicate where the fugacity is $z =0.5$,
and for this density range, the fugacities are $z<1.60$, 
$0.77$ and $0.25$ for $T=4$, $8$ and $20 \mev$.}
\label{Fig4}
\end{center}
\end{figure}


If the virial coefficients are temperature independent, then the power series 
in the fugacity for the pressure and the density will have no explicit 
temperature dependence. Consequently, the dependence of the pressure on
density and temperature will be given by
\be
P(n,T) = T^{5/2} \, f(n/T^{3/2}) \,,
\ee
where $f(x)$ is a scaling function of $n/T^{3/2}$. If this scaling relation 
holds, one can predict the pressure $P(n',T')$ at a new temperature $T'$ 
from $P(n,T)$ through
\be
P(n',T')=\biggl(\frac{T'}{T}\biggr)^{5/2} P(n,T) \,,
\label{pscale}
\ee
with $n'=(T'/T)^{3/2} \, n$. In Fig.~\ref{Fig3}, we demonstrate that 
low-density neutron matter scales according to Eq.~(\ref{pscale}).
The predicted pressures for $T'=4 \mev$ obtained from virial pressures 
calculated for $T=1$, $8$ and $20 \mev$ are in excellent agreement with 
the unscaled $T=4 \mev$ virial pressure. Fig.~\ref{Fig3} also gives
results for the scaled pressures ($T=1$, $8$ and $20 \mev$ scaled to 
$T'=4 \mev$ and unscaled $T=4 \mev$) obtained from the virial equation of 
state with $b_n$ calculated only from the S-wave scattering length $a_{np}$.
Although Table~\ref{Table1} shows that $b_n$ increases by $35 \%$ from
$T=1$ to $20 \mev$ in this case, the scaling symmetry continues 
to hold to a good approximation.

In the scaling regime, $b_n^\prime = 0$ and therefore the energy
density, Eq.~(\ref{epsilon}), is given by
\be
\epsilon = 3 P/2 \,.
\label{uniepsilon}
\ee
This is a general thermodynamic relation in the universal 
regime~\cite{Ho}. In Fig.~\ref{Fig4}, we show the energy per 
particle for $T=4$, $8$ and $20 \mev$. In order to separate
the interaction effects we have subtracted the free kinetic 
energy $3T/2$ from all curves. We have also calculated the
energy per particle from the virial pressures using the
universal relation Eq.~(\ref{uniepsilon}). The resulting
curves for the energy per particle are indistinguishable from
those shown in Fig.~\ref{Fig4}. This
demonstrates that the $b_n^\prime$ term is indeed negligible.
While neutron matter scales as in the unitary limit, the
thermodynamic properties depend on the value of the virial
coefficient, and the latter depends on the physics of NN 
scattering.

Finally, we emphasize that the universal relation for the energy
density, Eq.~(\ref{uniepsilon}), holds independent of the value
of the universal interaction coefficient given by $\xi$ for $T=0$
and $b_n$ for higher temperatures. In fact, Eq.~(\ref{uniepsilon})
is valid for $T=0$, where the energy per particle only scales with
density, $E/N \sim \xi \, n^{2/3}$ according to Eq.~(\ref{unieos}), and
for the virial regime, where the energy per particle scales with
density and temperature $E/N \sim \xi(T/n^{2/3}) \, n^{2/3}
\sim \widetilde{\xi}(T/n^{2/3}) \, T$, with Fermi temperature
$T_{\rm F} \sim n^{2/3}$. The latter scaling is very
explicit to lowest order in the 
density, where the energy per particle is given by
\be
\frac{E}{N} \approx \frac{3}{2} \, T \, ( 1 - b_n \lambda^3 n/2 ) \,.
\ee
