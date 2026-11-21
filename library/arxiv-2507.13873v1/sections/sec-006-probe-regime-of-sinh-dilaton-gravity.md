---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-006-probe-regime-of-sinh-dilaton-gravity
section_title: "Probe regime of sinh dilaton gravity"
section_number: null
pages: 15-21
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.975
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence of q-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
[]{#s:probe label="s:probe"}

We now turn to a different regime, the probe regime. To study it, it is beneficial to change coordinates from the momentum labels $s_1,s_2$ to the mass of the background black hole $E$ and the energy of the probe $\omega$ in terms of $$\begin{aligned}
\label{eq:transformation}
          E \equiv \frac{1}{4\pi^2b^4}\cosh(2\pi bs_2), \qquad E+\omega/b^2 \equiv \frac{1}{4\pi^2b^4} \cosh(2\pi bs_1).
\end{aligned}$$ Such types of approximations were extensively studied in JT gravity in [@Lam:2018pvp]. The Jacobian of this transformation is given by $$\mathrm{d}M \mathrm{d}\omega\simeq \sinh(2\pi bs_1)\sinh(2\pi bs_2)\mathrm{d}s_1 \mathrm{d}s_2,$$ such that the boundary two-point function is equivalent to $$\begin{aligned}
    \begin{tikzpicture}[baseline={([yshift=-.5ex]current bounding box.center)}, scale=0.5]
\draw[fill=blue!40!white,opacity=0.3] (0,0) ellipse (1.5 and 1.5);
\draw[fill] (-1.5,0) circle (0.06);
\draw[fill] (1.5,0) circle (0.06); 
\node at (-2.6,0) {\small $\mathcal{O}_{\beta_M}$};
\node at (2.6,0) {\small $\mathcal{O}_{\beta_M}$};
\node at (0,-1.8) {\small $\tau$};
\node at (0,1.8) {\small $\beta-\tau$};
\end{tikzpicture}
    =\int_\kappa^\infty \mathrm{d}E\int_{(\kappa-E)b^2}^\infty \mathrm{d}\omega \ \mathcal{A}(E,\omega),
\end{aligned}$$ where the spectral decomposition of the amplitude $\mathcal{A}(E,\omega)$ is given by $$\begin{aligned}
\label{eq:start}
\mathcal{A}(E,\omega)=\sinh\left(\frac{2\pi}{b}s_1 (E,\omega)\right)\sinh\left(\frac{2\pi}{b}s_2 (E,\omega)\right)e^{-\beta E-\frac{\tau}{b^2}\omega}\frac{S_b\left(\beta_M\pm i s_1 (E,\omega)\pm i s_2 (E,\omega)\right)}{S_b(2\beta_M)},
\end{aligned}$$ with the variables $s_1 (E,\omega)$ and $s_2 (E,\omega)$ given by the inverses of [\[eq:transformation\]](#eq:transformation){reference-type="eqref" reference="eq:transformation"}. The energy cutoff is defined as $\kappa\equiv \frac{1}{4\pi^2b^4}$.

In the probe approximation, we imagine a large background energy $E$ which remains unchanged by the injection of the probe, which is assumed not to alter the underlying semiclassical geometry. This is indeed the region of the Hilbert space, corresponding to large energies $E_1,E_2 \gg1$ and a small energy difference, i.e. $E_1\simeq E_2$, where the features of $q$-holography are expected to emerge, as we are approaching the holographic screen of sinh dilaton gravity. We now focus on this regime of the Hilbert space directly at the level of $\mathcal{A}(E,\omega)$ to check whether the structure of the integrand on the left-hand side of [\[eq:ramanexplicit\]](#eq:ramanexplicit){reference-type="eqref" reference="eq:ramanexplicit"} is recovered. In the limit of large energies, we can approximate $\mathcal{A}(E,\omega)$ to first order in the probe energy $\omega$, leading to $$\begin{aligned}
        s_1&=\frac{1}{2\pi b}\text{arccosh}(4\pi^2 b^4E), \\
        s_2&=\frac{1}{2\pi b}\text{arccosh}\left(4\pi^2b^4 (E+\omega/b^2)\right) \approx \frac{1}{2\pi b}\text{arccosh}(4\pi^2b^4 E)+\frac{2\pi b\omega}{\sqrt{(4\pi^2b^4E)^2-1}}+\dots \nonumber
\end{aligned}$$ By using the asymptotics of the double-sine functions $$S_b(x) \to e^{\pm i \frac{\pi}{2}x(Q-x)}e^{\pm i \delta(b)}, \qquad \text{Im}(x) \to \pm \infty,$$ with $\delta(b)$ an $x$-independent phase, the product of the two $S_b$ functions involving the total momentum can be approximated as $$\begin{aligned}
    S_b(\beta_M\pm i(s_1+s_2)) \,\, \rightarrow \,\,e^{2\pi \beta_M(s_1+s_2)-\pi Q (s_1+s_2)}.
\end{aligned}$$ Implementing these approximations in [\[eq:start\]](#eq:start){reference-type="eqref" reference="eq:start"}, we get $$\begin{aligned}
\mathcal{A}(E,\omega) \,\,&\simeq \,\, e^{\frac{1}{b^2} \text{arccosh}\left(4\pi^2b^4 E\right)- \beta E+{\color{darkblue}\frac{2\beta_M}{b}\text{arccosh}\left(4\pi^2b^4E\right)-\text{arccosh}\left(4\pi^2b^4E\right)}} \label{eq:Eintegral}\\
&\times \,e^{\frac{2\pi^2\omega}{\sqrt{(4\pi^2b^4E)^2-1}}-\frac{\tau}{b^2}\omega{\color{darkblue}+\frac{4\pi^2\beta_M b\omega}{\sqrt{(4\pi^2b^4E)^2-1}}-\frac{2\pi^2b^2\omega}{\sqrt{(4\pi^2b^4E)^2-1}}}}\frac{S_b\left(\beta_M\pm i \frac{2\pi b\omega}{\sqrt{(4\pi^2b^4E)^2-1}}\right)}{S_b(2\beta_M)} ,\label{eq:omegaintegral}
\end{aligned}$$ where we suggestively bundled the factors together in the two lines. We recognize in the first two terms in the exponent of [\[eq:Eintegral\]](#eq:Eintegral){reference-type="eqref" reference="eq:Eintegral"} the same terms that would appear in the saddle approximation of the disk partition function [\[partfuncs\]](#partfuncs){reference-type="eqref" reference="partfuncs"}. For the probe approximation to be successful, the matter operator should be light enough not to disturb the saddle of the background geometry [\[firstlaw\]](#firstlaw){reference-type="eqref" reference="firstlaw"}. Implementing the *light probe* approximation $$\frac{2\beta_M}{b} -1 \ll 1/b^2\quad \Leftrightarrow \quad 
\beta_M\ll \frac{Q}{2},$$ on [\[eq:Eintegral\]](#eq:Eintegral){reference-type="eqref" reference="eq:Eintegral"}, the two last terms (in darkblue) in the exponent of [\[eq:Eintegral\]](#eq:Eintegral){reference-type="eqref" reference="eq:Eintegral"} can be discarded. In this way the $E$-saddle is still given by $$\begin{aligned}
\label{saddle2}
    \sqrt{(4\pi^2b^4E)^2-1} = \frac{4\pi^2b^2}{\beta},
\end{aligned}$$ and the first law of thermodynamics of the sinh dilaton gravity black hole is preserved. It is important to note that although the probe approximation does not alter the saddle, the saddle is not necessarily dominating the correlator. In other words, we do not consider a semiclassical $b\rightarrow 0$ regime for which the integrand peaks sharply around the saddle point value. Instead, we are probing a quantum mechanical regime with finite $b$ in which the saddle point experiences large quantum fluctuations. We can then transition to the microcanonical two-point function of the full quantum correlation function by an inverse Laplace transform to remove the integral over background energies and finally set the energy of the microcanonical correlator to be equal to the large saddle point value $E(\beta)$ given by [\[saddle2\]](#saddle2){reference-type="eqref" reference="saddle2"}.

Within the probe regime, the two darkblue terms in [\[eq:omegaintegral\]](#eq:omegaintegral){reference-type="eqref" reference="eq:omegaintegral"} are also subdominant. We end up with the final microcanonical answer (for which we strip off the contributions on the first line [\[eq:Eintegral\]](#eq:Eintegral){reference-type="eqref" reference="eq:Eintegral"}) $$\begin{aligned}
  \boxed{  \mathcal{A}(E,\omega) \approx  e^{\frac{\omega \beta(E)}{2b^2}-\frac{\tau\omega}{b^2}}\frac{S_b\left(\beta_M\pm i \frac{\omega\beta(E)}{2\pi b}\right)}{S_b(2\beta_M)}},
\end{aligned}$$ where we encoded the energy dependence within the saddle temperature equation.

The main result of this paper is that this is just the spectral decomposition of the two-point correlator [\[eq:ramanexplicit\]](#eq:ramanexplicit){reference-type="eqref" reference="eq:ramanexplicit"} we derived by studying $q$-Ward identities, but now emerging within this specific kinematic regime of the sinh dilaton gravity two-point function. Hence we explicitly find the quantum hyperbolic disk in the probe region of frequency space (see Fig. [1](#Figkinematic){reference-type="ref" reference="Figkinematic"}).

![Kinematic regime in frequency space where the probe approximation holds, and where the quantum disk geometry and its isometries govern the correlation functions.](Figkinematic.pdf){#Figkinematic width="0.3\\linewidth"}

While the probe integral transform [\[eq:ramanexplicit\]](#eq:ramanexplicit){reference-type="eqref" reference="eq:ramanexplicit"} runs over energies $\omega$ from $-\infty$ to $+\infty$, for the probe approximation to be valid on the bulk side, we require $\omega \ll E$. Even when $E$ is taken to be very large, as in our case, for any fixed $E$ there will inevitably be a region in the Hilbert space where $\omega \sim \mathcal{O}(E)$, at which point the probe approximation breaks down. We may thus conclude that the quantum disk accurately captures the sector of the sinh dilaton gravity Hilbert space corresponding to the probe regime at large energies. However, a complete identification in coordinate space would require extrapolating the probe regime beyond its domain of validity. Under this extrapolation, we would obtain[^1] $$\label{eq:final}
\boxed{\left\langle \mathcal{O}(\tau) \mathcal{O}(0)\right\rangle_{\beta(E)} \quad\overset{\text{probe}}{\to} \quad \frac{S_b(-\beta_M+\frac{b}{2}+\frac{\tau}{b\beta(E)})}{S_b(\beta_M+\frac{b}{2}+\frac{\tau}{b\beta(E)})}}.$$ We have considered very large background energies with light probes that do not influence the thermodynamical saddle. Due to the UV-IR relation in this model (as discussed above in subsection [\[s:classical\]](#s:classical){reference-type="ref" reference="s:classical"}), this kinematic regime probes the geometric region close to the boundary of the dilaton gravity model.

If we interpret this result as a saddle evaluation of a canonical correlation function $\text{Tr}( \mathcal{O}(\tau) \mathcal{O}(0)e^{-\beta H})$, using $S_b(Q-x)=1/S_b(x)$, then our expression [\[eq:final\]](#eq:final){reference-type="eqref" reference="eq:final"} manifestly preserves the KMS condition $\tau\rightarrow \beta-\tau$ of the original Liouville correlator, as required for any thermal correlation function. This means physically that there is no defect in the interior of the thermal disk (see Fig. [2](#FigKMS){reference-type="ref" reference="FigKMS"}).

![The KMS condition requires that there is no defect in the geometrical bulk. The blue endpoint is moved around the boundary to a distance $\beta-\tau$, but it would pick up any defect in the interior, as illustrated by the dashed line now encircling the red defect (if it would be there).](FigKMS.pdf){#FigKMS width="0.45\\linewidth"}

Assuming $\beta_M\equiv b\Delta$ with $\Delta$ integer, we can use the recursive property of the $S_b(.)$ functions $S_b(x+b)=2\sin(\pi bx)S_b(x)$ to rewrite the correlation function in terms of elementary functions as ($\beta_M = b\Delta$): $$\begin{aligned}
 \label{eq:sine}
    \frac{S_b(-\beta_M+\frac{b}{2}+\frac{\tau}{b\beta})}{S_b(\beta_M+\frac{b}{2}+\frac{\tau}{b\beta})}=\frac{1}{\prod_{n=-\Delta}^{\Delta-1}2\sin\left(\frac{\pi\tau}{\beta}+\frac{\pi b^2}{2}+\pi b^2n\right) },
\end{aligned}$$ Again taking the JT limit $b\to 0$ readily leads to the usual thermal CFT$_1$ answer: $$\label{eq:classicalcorrelator}
\left\langle \mathcal{O}(\tau) \mathcal{O}(0)\right\rangle_{\beta}\,\,\overset{\text{probe, } b\to 0}{\longrightarrow} \,\, \frac{1}{\left(\sin \frac{\pi}{\beta}\tau\right)^{2\Delta}}.$$ The full probe answer [\[eq:sine\]](#eq:sine){reference-type="eqref" reference="eq:sine"} has $2\Delta$ simple poles at locations $$\label{poles}
\tau_{\text{pole}} =\beta b^2\Delta, \, \beta b^2(\Delta-1), \, \hdots  , \, 0, \,  \hdots , \, -\beta b^2(\Delta-1).$$ and their shifts by multiples of $\beta$. The fact that the composite pole is disentangled into simple poles is intuitively associated to the fuzzyness of non-commutative geometry. However, Fig. [\[fig:numerical\]](#fig:numerical){reference-type="ref" reference="fig:numerical"} shows that the exact sinh dilaton gravity two-point function does not exhibit these extra poles [\[poles\]](#poles){reference-type="eqref" reference="poles"} in $\tau$. These poles arise as a result of the probe extrapolation. Heuristically, this can be explained by noting that the other poles would correspond to bulk trajectories that extend too deep into the bulk, where the quantum disk approximation is no longer valid.

The fact that the semi-classical answer ($\hbar \to 0$) and the probe answer (UV or near-boundary region) disagree with each other can be physically interpreted in that the near-boundary region is not a classical geometry; it is instead the quantum hyperbolic disk. Where is this quantum hyperbolic disk geometry hidden? This emergent quantum hyperbolic disk geometry should be viewed as a $q$-deformation of the effective AdS$_2$ geometry that governed semi-classical physics [\[eq:weylliou\]](#eq:weylliou){reference-type="eqref" reference="eq:weylliou"}. To see this, it is useful to rewrite the sinh dilaton gravity model in terms of $q$-Liouville quantum mechanics, as explained in detail in Appendix [\[a:quant\]](#a:quant){reference-type="ref" reference="a:quant"}. One of the phase space variables is the length $L$ of the Einstein-Rosen bridge in the effective AdS$_2$ spacetime [\[eq:weylliou\]](#eq:weylliou){reference-type="eqref" reference="eq:weylliou"}: $$\label{LL}
L = \int_\mathcal{\text{geodesic}}\mathrm{d} s_{\text{eff}} = \int_\mathcal{\text{geodesic}} \mathrm{d} s_{\text{flat}} \,e^{b\varphi}.$$ where $\varphi$ is the Liouville field in the original Liouville gravity formulation. In this language, the boundary two-point function (which encoded the quantum disk isometries) is an insertion of the operator $e^{- \Delta L}$ in the $q$-Liouville path integral [@Blommaert:2023wad]. Therefore, it is this Liouville metric that encodes the non-commutative features of the quantum disk in the probe regime. We can then suggestively interpret the situation as follows. Since the physical dilaton gravity geometry is given by the geometry in the Liouville frame $\varphi$ up to a Weyl rescaling, this suggests also the dilaton gravity geometry is becoming fuzzy. Hence the classical singularity at the boundary [\[R\]](#R){reference-type="eqref" reference="R"} is fuzzy, and it then seems resolved quantum mechanically by the non-commutative geometry of the quantum hyperbolic disk. In the past, non-commutative geometry has been indeed proposed as one of the main mechanisms to resolve curvature singularities.

We summarize the final bulk structure of the *quantum* model in Fig. [3](#Figfinal){reference-type="ref" reference="Figfinal"}.

![Geometry of the quantum sinh dilaton gravity bulk, with a full quantum gravity region deep in the interior, and a UV region closer to the holographic screen where we have an emergent quantum hyperbolic disk and SL$_q(2,\mathbb{R})$ symmetry. One way to phrase this is that close to the boundary the gravitational quantum fluctuations are reduced from full quantum gravity to just those describing the non-commutativity of the quantum hyperbolic disk spacetime.](Figfinalstruct.pdf){#Figfinal width="0.55\\linewidth"}

[^1]: As a technical aside, the particular ratio of $S_b$-functions in [\[eq:final\]](#eq:final){reference-type="eqref" reference="eq:final"} has appeared before in the literature and has nice structural properties. In [@Teschner:2012em], it would be denoted as $D_{-i\beta_M}(i\frac{\tau}{b\beta}+i\frac{1}{2b})$, and was identified as the kernel of the intertwiner $R_\alpha: \mathcal{P}_\alpha \to \mathcal{P}_{Q-\alpha}$, mapping Virasoro representations $\alpha$ into their conjugate $Q-\alpha$. This same function was then identified as the building block of the $3j$-symbols of the modular double [@Teschner:2012em].
