---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-013-332-synthesis
section_title: "Synthesis"
section_number: 3.3.2
pages: 27-32
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.677
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
[]{#sec:path label="sec:path"}

It is fairly clear from the above discussion of quantization that there should be a relation between the partition function for Chern-Simons theory with compact gauge group $G$ and the partition function for Chern-Simons theory with complex gauge group $G_{\mathbb{C}}$. Essentially the same equations [\[Acpt\]](#Acpt){reference-type="eqref" reference="Acpt"} and [\[Acx\]](#Acx){reference-type="eqref" reference="Acx"} define the two partition functions --- though in one case they are difference equations and in the other they are differential equations. This relation was developed in [@gukov-2003; @DGLZ], and was recently explained very concretely in [@Wit-anal] in terms of analytic continuation.

Algebraically, there may be several solutions to the difference equations [\[Acpt\]](#Acpt){reference-type="eqref" reference="Acpt"} of the compact theory. Let us label them as $Z^{\alpha}_G(M;u)$. The exact partition function of the compact theory (*i.e.* the colored Jones polynomial for $G=SU(2)$) is given as a linear combination

$$Z^G(M;u;\hbar) = \sum_\alpha n_\alpha Z^\alpha_G(M;u;\hbar)\,. \label{sumG}$$

The $\hbar\to 0$ asymptotics of each component in this sum are then governed by the corresponding solution $Z^\alpha_{\rm pert}(M;u)$ to the differential equation [\[Acx\]](#Acx){reference-type="eqref" reference="Acx"}, written in the form [\[Zcxpert\]](#Zcxpert){reference-type="eqref" reference="Zcxpert"}. These are holomorphic pieces of the $G_{\mathbb{C}}$ partition function. The physical statement of the volume conjecture for $SU(2)$ is that the component of the sum [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} with the *dominant* leading asymptotics corresponds to the $SL(2,{\mathbb{C}})$ partition function $Z^{\alpha=\rm hyp}_{\rm pert}(M;u)$ around the hyperbolic $SL(2,{\mathbb{C}})$ flat connection. Of all the flat $SL(2,{\mathbb{C}})$ connections, this has the largest volume in a neigborhood of the complete hyperbolic point $u=i\pi$. Therefore, *if* the solution $Z^{\rm hyp}_G(M;u)$ of the difference equations contributes to the colored Jones polynomial in [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"}, it will have the dominant asymptotic. One must simply assure that

$$\text{Physical volume conjecture\,:}\qquad  n_{\rm hyp}\neq 0\,.\hspace{1in}$$

For higher-rank groups, it is again clear that the overall asymptotics of $Z^G(M;u)$ will be controlled by the flat $G_{\mathbb{C}}$ connection with the largest volume that makes a corresponding contribution to [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"}. One may expect by comparison to $SU(2)$ theory that the connection with the largest overall volume (the analog of the hyperbolic flat connection) in fact contributes and dominates. This has yet to be explored.\
The expansions [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} and [\[sumGc\]](#sumGc){reference-type="eqref" reference="sumGc"} for compact and complex Chern-Simons theory, and the relation between them, were explained in [@Wit-anal] using analytic continuation of the Chern-Simons path integral. The path integral provides yet another method for quantizing a topological quantum field theory, with its own inherent advantages. Let us finish by saying a few words about this.

The path integral for compact Chern-Simons theory takes the form

$$\begin{aligned}
 Z^G(M;u;\hbar)  &= \int {\cal D}{\cal A}_{(u)} \exp\left(\frac{ik}{4\pi}I_{CS}({\cal A})\right) \label{Pcpt} \\
&= \int {\cal D}{\cal A}_{(u)} \exp\left(-\frac{1}{4\hbar}I_{CS}({\cal A})\right)\,, \nonumber
\end{aligned}$$

where $I_{CS}({\cal A}) = \int_M {\rm Tr}\big({\cal A}d{\cal A}+\frac23{\cal A}^3\big)$ is the Chern-Simons action as in [\[ICS\]](#ICS){reference-type="eqref" reference="ICS"} and $k\in{\mathbb{Z}}$. The integral is over all $G$-connections on $M=\widetilde{M}\backslash K$, modulo gauge equivalence, with fixed holonomy eigenvalues $e^u$ at the meridian of $K$. (In order to obtain a nonzero answer, $u/\hbar\sim \lambda^*+\rho^*$ must be integral.) For ${\frak{g}}$-values connections ${\cal A}$, the action $I_{CS}({\cal A})$ is real. Therefore, for $k\in{\mathbb{Z}}$, the integral [\[Pcpt\]](#Pcpt){reference-type="eqref" reference="Pcpt"} is oscillatory and can be calculated by appropriately regulating the oscillations as ${\cal A}\to\infty$. In [@Wit-anal], however, the problem was posed of analytically continuing to $k\in {\mathbb{C}}$. Roughly speaking, to accomplish this one must also complexify the gauge connection ${\cal A}$ so that it is ${\frak{g}}_{\mathbb{C}}$-valued. When $k\in{\mathbb{R}}$, the integral [\[Pcpt\]](#Pcpt){reference-type="eqref" reference="Pcpt"} is then interpreted as a holomorphic contour integral along the real subspace in the space of complex connections. As $k$ is pushed away from the real line, this integration contour must also move. In general, the appropriate integration contour for $k\in{\mathbb{C}}$ is a sum of contours going through the various saddle points of the complexified action $I_{CS}({\cal A})$. Each saddle point is a flat $G_{\mathbb{C}}$ connection, and an expression of the form [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} results.

For complex Chern-Simons theory, the procedure is quite similar. The path integral is

$$\begin{aligned}
 Z^{G_{\mathbb{C}}}(M;u;\hbar,\tilde{\hbar}) &=
 \int {\cal D}{\cal A}_{(u)}{\cal D}\overline{{\cal A}}_{(\bar{u})}
   \exp\left( \frac{i\tau}{8\pi} I_{CS}({\cal A})+ \frac{i\tilde{\tau}}{8\pi} I_{CS}(\overline{{\cal A}}) \right)  \label{Pcx} \\
 &= \int {\cal D}{\cal A}_{(u)}{\cal D}\overline{{\cal A}}_{(\bar{u})}
   \exp\left( -\frac{1}{4\hbar} I_{CS}({\cal A})- \frac{1}{4\tilde{\hbar}} I_{CS}(\overline{{\cal A}}) \right)\,, \nonumber
\end{aligned}$$

for a ${\frak{g}}_{\mathbb{C}}$-valued $G_{\mathbb{C}}$-connection ${\cal A}$. The integrand is initially well-defined when $\tau+\tilde{\tau}\in{\mathbb{Z}}$, and leads to a convergent oscillatory integral when the exponent is imaginary --- *i.e.* for $\tilde{\tau}=\bar{\tau}$. In order to analytically continue to independent $\tau,\tilde{\tau}\in{\mathbb{C}}$, one must treat ${\cal A}$ and $\overline{{\cal A}}$ as independent connections and again complexify *each* of them. One then deforms the contour of integration away from the "real" subspace when $\tilde{\tau}\neq\bar{\tau}$, and writes the resulting contour as a sum over *pairs* of saddle points for ${\cal A}$ and $\overline{{\cal A}}$. Since $({\frak{g}}_{\mathbb{C}})_{\mathbb{C}}\simeq {\frak{g}}_{\mathbb{C}}\times {\frak{g}}_{\mathbb{C}}$, however, these are just pairs of saddle points of flat $G_{\mathbb{C}}$-connections. An expression of the form [\[sumGc\]](#sumGc){reference-type="eqref" reference="sumGc"} results:

$$\label{sumGG}
Z^{G_{\mathbb{C}}}(M;u;\hbar,\tilde{\hbar}) = \sum_{\alpha,\bar{\alpha}}n_{\alpha,\bar{\alpha}} Z^{\alpha}_{G_{\mathbb{C}}}(M;u;\hbar) \overline{Z^{\alpha}_{G_{\mathbb{C}}}}(M;\bar{u};\tilde{\hbar})\,.$$

The functions $Z^{\alpha}_{G_{\mathbb{C}}}(M;u;\hbar)$ and $Z^{\alpha}_{G}(M;u;\hbar)$ here and in [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} should be *identical*, since they both correspond to $G_{\mathbb{C}}$ connections.

In [@Wit-anal], it is explained how the coefficients $n_\alpha$ and $n_{\alpha,\bar{\alpha}}$ may be calculated for specific examples, like the trefoil and figure-eight knot complements. As expected, the coefficient of the hyperbolic component "$\alpha={\rm hyp}$" of the $SU(2)$ partition function is nonzero, leading to another demonstration of the volume conjecture.

The careful reader may still be wondering why it is only the growth of the colored Jones polynomial at *non*rational $N/k$ that shows exponential behavior. The answer comes from a final subtlety in the analytic continuation of the path integral: for $k\notin{\mathbb{Z}}$, the sum [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} can have *multiple* contributions from the same flat connection, differing by a multiplicative factor $e^{2\pi i k}$. (If analytically continuing in $N$ as well, factors of $e^{\frac{2\pi i u}{\hbar}}$ may also arise.) This behavior originates from the fact that $\exp\big(\frac{ik}{4\pi}I_{CS})$ is not completely gauge-invariant when $k\notin{\mathbb{Z}}$. For example, in the case of the figure-eight knot, the actual hyperbolic contribution to [\[sumG\]](#sumG){reference-type="eqref" reference="sumG"} goes like

$$\big(e^{i\pi k}-e^{-i\pi k})Z^{\rm hyp}_{G_{\mathbb{C}}}(M;u;\hbar)\,,$$

which vanishes at $k\in{\mathbb{Z}}$, leading to polynomial rather than exponential growth of $J_N(K;q)$ for $u/i\pi \sim N/k\in {\mathbb{Q}}$. It is expected that this feature is fairly generic for hyperbolic knots.

**Acknowledgements**\
We would like to thank Edward Witten, Don Zagier, and Jonatan Lenells for enlightening discussions on subjects considered in these notes. We would also like to thank the organizers of the workshops *Interactions Between Hyperbolic Geometry, Quantum Topology, and Knot Theory*; *Chern-Simons Gauge Theory: 20 years after*; and *Low Dimensional Topology and Number Theory II*; and Columbia University, the Hausdorff Center for Mathematics, and the University of Tokyo, respectively, for their generous support, accommodations, and collaborative working environment. The work of SG is supported in part by DOE Grant DE-FG03-92-ER40701, in part by NSF Grant PHY-0757647, and in part by the Alfred P. Sloan Foundation. Opinions and conclusions expressed here are those of the authors and do not necessarily reflect the views of funding agencies.
