---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-018-53-near-extremal-ads-throat
section_title: "Near Extremal AdS Throat"
section_number: 5.3
pages: 44-46
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.979
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
Recall the $AdS_d$ Schwarzschild geometry $$\label{AdSsch}
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega_{d-2}^2,$$ with $$f(r)=1+\left(\frac{r}{R}\right)^2-\frac{\alpha}{r^{d-3}}.$$ A scalar field on this background feels an effective potential. In particular if we look for solutions of the Klein-Gordon equation of the form $$\phi\equiv r^{-\frac{d-2}{2}}e^{-i\omega t}Y_{\ell}(\Omega_{d-2})\Psi_{\omega \ell}(r),$$ it is not hard to see that $\Psi_{\omega \ell}$ must obey a Schrodinger-type equation $$-\frac{d}{dr_*^2}\Psi_{\omega \ell}+V_{eff}(r)\Psi_{\omega\ell}=\omega^2 \Psi_{\omega \ell}.$$ Here $r_*$ is a "tortoise" type coordinate obeying $$r_*'(r)=f^{-1},$$ and the effective potential is $$\begin{aligned}
\nonumber
V_{eff}(r)=R^{-2}\bigg(1+\left(\frac{R}{r}\right)^2&-\frac{\alpha R^2}{r^{d-1}}\bigg)\bigg[\left(m^2+\frac{d(d-2)}{4R^2}\right)r^2\\
&+\left(\ell(\ell+d-3)+\frac{(d-2)(d-4)}{4}\right)+\frac{(d-2)^2}{4}\cdot \frac{\alpha}{r^{d-3}}\bigg].\label{AdSPot}
\end{aligned}$$ The details of this potential do not matter, but we see that it vanishes linearly at the only real positive root of $f(r)$, that is at the horizon, and that it grows quadratically with $r$ at large $r$. Near the horizon the solution then behaves as $\Psi_{\omega\ell}\sim e^{i\omega(\pm r_*-t)}$, while at large $r$ we have $\phi\sim r^{-\Delta_{\pm}}$ with the usual AdS/CFT formula $$\Delta_{\pm}=\frac{d-1}{2}\pm\frac{1}{2}\sqrt{(d-1)^2+4R^2m^2}.$$

The idea of this section is to cut off this geometry at some large value of $r$ and sew it onto Minkowski space, after which the effective potential [\[AdSPot\]](#AdSPot){reference-type="eqref" reference="AdSPot"} would go back to zero provided we set the scalar field mass $m^2$ to zero. The black hole would then be able to decay via massless quanta tunneling out of this potential into the Minkowski region, and by choosing the crossover value of $r$ to be large we could adjust the decay time independently of the entropy of the black hole. We can also "outsource" the computation by putting the computer out in the Minkowski region, which allows us to buy a large redshift factor enhancement in the time it takes to do the computation from the point of view of Alice living down by the black hole.

There is a new problem with this construction however, which is that any attempt to send the result of the computation from the Minkowski region back down the throat to the vicinity of the black hole has to get back through the potential barrier. The signal the computer sends down the throat will need to be very low energy, so its absorption probability will be exponentially small. Nonetheless one could imagine trying to send the signal repeatedly, hoping that eventually one of the times it will get through. This approach gets much harder as the size of the signal we wish to send increases, but unlike the previous examples it is not obvious that it cannot be done and we need to analyze it more carefully.
