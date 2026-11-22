---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-004-32-second-moment-of-the-unfolded-level-spacing-d
section_title: "Second moment of the unfolded level spacing distribution"
section_number: 3.2
pages: 4-5
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 1.0
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
---
[]{#ssec:smulsd label="ssec:smulsd"}

As can be seen in Fig. [\[fig:ulsd\]](#fig:ulsd){reference-type="ref" reference="fig:ulsd"} the unfolded level spacing distribution changes in the spectrum from the exponential to the Wigner surmise in a continuous fashion. There does not appear to be a sharp mobility edge, $\lambda_c$, separating localized and delocalized states. Even in the case of Anderson transitions, however, a sharp transition is expected only in the thermodynamic limit when the spatial size of the system, $N_s$, goes to infinity. This is completely analogous to second order phase transitions where a truly divergent correlation length and a sharp phase transition can only be observed in infinite systems. In principle any physical quantity that changes in a well defined way from the localized to the delocalized regime can be used to define a transition point in the spectrum. If there is a sharp transition in the thermodynamic limit then non-analytic behavior should appear in all these quantities at a given point, $\lambda_c$, in the spectrum. In what follows we will look for a quantity that can be used to define the transition point.

<figure id="fig:ulsdvar">
<div class="center">
<embed src="ulsdvar.eps" />
</div>
<figcaption><span id="fig:ulsdvar" label="fig:ulsdvar"></span> Variance of the unfolded level spacing distribution across the transition in the spectrum for ensembles C1, C2 and C3 that differ only in their spatial volume. The dashed horizontal lines at 1 and 0.178 indicate the expected limits in the localized (Poisson) and delocalized (RMT) regime.</figcaption>
</figure>

Since the first moment of the unfolded level spacing distribution is unity by construction, the simplest quantity to consider is its second moment or variance. In the localized case the level spacings are exponentially distributed and the variance is

$$\sigma\ensuremath _{\mbox{\scriptsize s}}^2 = \langle s^2 \rangle - \langle s \rangle^2=1,$$

while in the delocalized regime the second moment of the distribution of Eq. ([\[eq:wigner_chu\]](#eq:wigner_chu){reference-type="ref" reference="eq:wigner_chu"}) can be analytically determined to be $\sigma\ensuremath _{\mbox{\scriptsize s}}^2=\frac{3\pi}{8}-1$. In Fig. [1](#fig:ulsdvar){reference-type="ref" reference="fig:ulsdvar"} we plot how the variance changes in the spectrum throughout the transition region. The three data sets correspond to ensembles C1-C3 with three different spatial volumes but otherwise identical parameters. It is apparent that with increasing volume the transition becomes sharper. To define a finite volume pseudocritical point in the spectrum we locate the inflection point of the curve $\sigma^2(\lambda)$. To this end we use the three-parameter fitting Ansatz

$$\sigma^2(\lambda) = A\left\{ 1 - \tanh(B(\lambda-C)) \right\} + 
          \frac{3\pi}{8}-1.
    \label{eq:tanh}$$

This form ensures the correct limit for large $\lambda$ and yields good fits starting already from $\lambda a = 0.2, 0.25$ i.e. already from below the transition point. Using this Ansatz the inflection point can be easily seen to be at $\lambda\ensuremath _{\mbox{\scriptsize c}} a=C$ and the slope of the curve there is $AB$. These two parameters are largely independent of the starting point of the fit as long as it starts at smaller values of $\lambda$ than where the inflection point occurs. The location of the inflection point turns out to be also independent of the volume yielding pseudocritical points $C=\lambda_ca =
0.321(4), 0.322(1), 0.324(2)$ for the spatial sizes $N_s=16, 24, 32$. The slope at the inflection point is $AB=7.6(5), 10.96(36), 13.8(5)$ for the three different spatial sizes and it scales roughly proportionally to the linear spatial size of the box. This indicates that there might be a genuine sharp transition in the thermodynamic limit. The sharpening of the transition with the volume can be better seen in Fig. [2](#fig:ulsdvar_zoom){reference-type="ref" reference="fig:ulsdvar_zoom"} where we plot again the variance of the unfolded level spacing distribution but zoom in on the transition region and also show the fitted curves with the above described parameters.

<figure id="fig:ulsdvar_zoom">
<div class="center">
<embed src="ulsdvar_zoom.eps" />
</div>
<figcaption><span id="fig:ulsdvar_zoom" label="fig:ulsdvar_zoom"></span> The same as Fig. <a href="#fig:ulsd" data-reference-type="ref" data-reference="fig:ulsd">[fig:ulsd]</a> but zooming in on the transitions region. The dotted, dashed and the continuous curve indicate the fits of the form Eq. (<a href="#eq:tanh" data-reference-type="ref" data-reference="eq:tanh">[eq:tanh]</a>) to the <span class="math inline"><em>N</em><sub><em>s</em></sub> = 16, 24</span> and <span class="math inline">32</span> data respectively.</figcaption>
</figure>
