---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-017-52-reissner-nordstrom
section_title: "Reissner-Nordstrom"
section_number: 5.2
pages: 43-44
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
Another way Alice could try to extend the lifetime of her black hole is by giving it some charge. The Reissner-Nordstrom black hole of mass $M$ and charge $Q$ has metric $$ds^2=-dt^2f(r)+\frac{dr^2}{f(r)}+r^2 d\Omega_2^2,$$ where $$f(r)=1-\frac{2GM}{r}+\frac{GQ^2}{r^2}\equiv \frac{(r-r_+)(r-r_-)}{r^2}$$ and $$r_\pm=GM\pm\sqrt{G(GM^2-Q^2)}.$$ Its entropy is $$S=\frac{\pi r_+^2}{G}\equiv \frac{\pi r_+^2}{\ell_p^2}$$ and its temperature is $$T=\frac{r_+-r_-}{4\pi r_+^2}.$$ We see when $M\ell_P=Q$, the black hole is extremal and the temperature is zero. If we start the black hole with mass above extremality, it will radiate and gradually approach extremality. The relevant point here is that as it does this, the temperature decreases and semiclassically it appears that the decay takes an infinite amount of time. More precisely if we define the energy above extremality to be $$E=M-Q\ell_p^{-1},$$ the energy-temperature relation is $$\label{exttemp}
E=2\pi^2 Q^3 T^2 \ell_p$$ and a simple calculation tells us that, for a black hole which starts with energy $E_0\leq Q\ell_p^{-1}$, we have $$E(t)=\frac{E_0}{1+\alpha tE_0Q^{-4}}.$$ Here $\alpha$ is some order one numerical constant. Thus it appears that the black hole takes an infinite amount of time to reach extremality. There is a well-known problem with this argument however [@Preskill:1991tb; @maldstrom], which is that from [\[exttemp\]](#exttemp){reference-type="eqref" reference="exttemp"} we see that when the temperature reaches $$T\sim \frac{1}{Q^3 \ell_p}$$ the remaining energy $E$ above extremality is no longer bigger than the temperature $T$. At this point the semiclassical description of the evaporation process breaks down, and quantum gravity is necessary to understand what happens next. This is related to an instability of $AdS_2$ called fragmentation [@maldstrom], and in the cases where it can be understood in string theory it is always true that the geometry breaks apart into something that has little resemblance to the original Reissner-Nordstrom geometry.

It is easy to see that no matter whether we start with $E$ near extremality or much larger, this instability always sets in well before the exponential of the initial entropy. For example, say that we start with $E_0\leq Q$ (setting $\ell_p=1$). The initial entropy is of order $Q^2$, while the time to reach the instability is of order $Q^7$. Alternatively if we start with $E_0\gg Q$ then we are back to the Schwarzschild situation where evaporating back down to $E\approx Q \ell_P^{-1}$ takes a time of order $E_0^3\approx S_0^{3/2}$, and the additional time to get down to the instability is $Q^7\ll S_0^{7/2}$. The total evaporation time is always bounded by a polynomial in $S_0$. Thus charged black holes, near extremal or otherwise, are of no use to Alice.
