---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-002-21-coloured-decompositions-for-the-simplest-sate
section_title: "Coloured decompositions for the simplest satellites"
section_number: 2.1
pages: 4-5
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.632
latex_coverage_ratio: 0.976
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Many colored knot polynomials (the symmetric and adjoint HOMFLY are among them) can be computed (or even defined) as linear combinations of plain polynomials for the knot cables [@AMcab] and, more generally, for the knot satellites [@KnotBook]. The simplest family, the torus satellites $\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}$, looks like multiply twisted ribbons tied in the (companion) knot $\mathcal{K}$ (fig.[\[fig:sat\]](#fig:sat){reference-type="ref" reference="fig:sat"}.I). The closure of the ribbon is then a two-strand torus knot (fig.[\[fig:tortw\]](#fig:tortw){reference-type="ref" reference="fig:tortw"}.I). The *unreduced* plain HOMFLY polynomials of these satellites are linear combinations of the unreduced coloured (namely, antisymmetric and symmetric) polynomials of the knot $\mathcal{K}$ [@AMcab], $$\begin{aligned}
H^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=-(Aq)^{-k}H^{\mathcal{K}}_{\mathtt{asm}}+(A/q)^{-k}H^{\mathcal{K}}_{\mathtt{sym}}.\label{tor-cab-top_u}
\end{aligned}$$ The power $k$ is related to the number of half-twist of the ribbon as we specify below.

If the border of the ribbon is linked with itself to form a twist knot (fig.[\[fig:tortw\]](#fig:tortw){reference-type="ref" reference="fig:tortw"}.II), one obtains the next to simplest family, the twisted satellites $\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}$ (Whitehead doubles) of the knot $\mathcal{K}$ (fig.[\[fig:sat\]](#fig:sat){reference-type="ref" reference="fig:sat"}.II). The unreduced HOMFLY of these satellites are expressed via another pair of the unreduced coloured polynomials (namely, the trivial and adjoint ones) as $$\begin{aligned}
H^{\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}}=\tau_{\mathtt{trv}}H^{\mathcal{K}}_{\mathtt{trv}}+A^{-k-1}H^{\mathcal{K}}_{\mathtt{adj}}.\label{tw-cab-top-u}
\end{aligned}$$ The rational form-factor $\tau_{\mathtt{trv}}=A^{-2}\Big(q^2+q^{-2}-A-A^{-1}\Big)$ is associated with the "lock-down" pair of crossings (adjacent to the gray area in fig.[\[fig:tortw\]](#fig:tortw){reference-type="ref" reference="fig:tortw"}.II), which is new for the twisted satellites compared to the torus family. Below we substitute $H^{\mathcal{K}}_{\mathtt{trv}}=1$, which holds for any $\mathcal{K}$.

We will mostly work with the *reduced* polynomials $\mathcal{H}$, which are ratios of the unreduced polynomials of the given knot and the unknot (in the given representation), i.e., $\mathcal{H}^{\mathcal{K}}_Q=H^{\mathcal{K}}_Q/H^{\emptyset}_Q$. The analogues of decompositions ([\[tor-cab-top_u\]](#tor-cab-top_u){reference-type="ref" reference="tor-cab-top_u"},[\[tw-cab-top-u\]](#tw-cab-top-u){reference-type="ref" reference="tw-cab-top-u"}) for the reduced polynomials are $$\begin{aligned}
\mathcal{H}^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=A^{-k}\Big(-q^{-k}\frac{\{Aq^{-1}\}}{\{q^2\}}\mathcal{H}^{\mathcal{K}}_{\mathtt{asm}}+q^{k}\frac{\{Aq\}}{\{q^2\}}\mathcal{H}^{\mathcal{K}}_{\mathtt{sym}}\Big),
\label{tor-cab-top}
\end{aligned}$$ $$\begin{aligned}
\mathcal{H}^{\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}}=A^{-2}\Big(1+\frac{A\{q\}^2}{\{A\}}+A^{-k+1}\frac{\{Aq\}\{A/q\}}{\{A\}}\mathcal{H}^{\mathcal{K}}_{\mathtt{adj}}\Big).\label{tw-cab-top}
\end{aligned}$$

## The pattern decomposition[]{#sec:unsat label="sec:unsat"}

Following [@MorTwSat], one can identically rewrite ([\[tw-cab-top\]](#tw-cab-top){reference-type="ref" reference="tw-cab-top"}) and ([\[tor-cab-top\]](#tor-cab-top){reference-type="ref" reference="tor-cab-top"}) in form of *pattern decompositions*. Namely, $$\begin{aligned}
\mathcal{H}^{\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}}=\mathcal{H}^{\mathtt{Tw}_{k+\gamma}}+A^{-k-\gamma+1}\{Aq\}\{A/q\}\mathfrak{H}^{\mathcal{K}}_{\mathtt{adj}},\label{tw-patt-v}
\end{aligned}$$ and $$\begin{aligned}
\mathcal{H}^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=\left(Aq\right)^{\delta}\mathcal{H}^{\mathtt{Tor}_{k+\delta}}-(Aq)^{k+\delta}\{Aq^{-1}\}\mathfrak{H}^{\mathcal{K}}_{\mathtt{asm}}+(A/q)^{k+\delta}\{Aq\}\mathfrak{H}^{\mathcal{K}}_{\mathtt{sym}},
\label{tor-patt-v}
\end{aligned}$$ where $$\begin{aligned}
\mathfrak{H}^{\mathcal{K}}_{\mathtt{asm}}\!=\!\frac{\left(Aq\right)^{\delta}}{\{q^2\}}\Big(\mathcal{H}^{\mathcal{K}}_{\mathtt{asm}}-1\Big),\  \mathfrak{H}^{\mathcal{K}}_{\mathtt{sym}}\!=\!\frac{(A/q)^{-\delta}}{\{q^2\}}\Big(\mathcal{H}^{\mathcal{K}}_{\mathtt{sym}}-q^{2\delta}\Big), 
\ \text{and}\ \mathfrak{H}^{\mathcal{K}}_{\mathtt{adj}}\!=\!\frac{A^{\gamma}}{\{A\}}\Big(\mathcal{H}^{\mathcal{K}}_{\mathtt{adj}}-A^{-\gamma}\Big)
\end{aligned}$$ are Lauren polynomials in $A$ and $q$ with integer coefficients. One can chose *any* integers for $\gamma$ and $\delta$, but they must be knot invariants if one wishes the $\mathfrak{H}$ to be a knot invariant too. Some values $\delta=\gamma\equiv\mathtt{Sh}_{\mathcal{K}}$ given by ([\[ShKn\]](#ShKn){reference-type="ref" reference="ShKn"}) prove to be distinguished. Namely, ([\[tor-patt-v\]](#tor-patt-v){reference-type="ref" reference="tor-patt-v"}) then can be extended to the Khovanov case so that the coefficients are naturally "deformed", and $\mathfrak{H}_{\mathtt{sym}}$ and $\mathfrak{H}_{\mathtt{adj}}$ (which coincide for $A=q^2$) are substituted with positive polynomials $\mathfrak{K}$ (while $\mathfrak{H}_{\mathtt{asm}}$ vanishes for $A=q^2$). The distinguished value $\mathtt{Sh}_{\mathcal{K}}$ depends on the companion knot and equals to the power of $q^2$, which acquires the factor of $(-t)$ at the critical point of the evolution flow (see sec.[\[sec:int\]](#sec:int){reference-type="ref" reference="sec:int"}). We redefine the satellite label $k\rightarrow k+\mathtt{Sh}_k$ in the Khovanov-related formulae to simplify them.
