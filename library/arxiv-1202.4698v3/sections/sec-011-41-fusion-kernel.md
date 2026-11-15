---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-011-41-fusion-kernel
section_title: "Fusion kernel"
section_number: 4.1
pages: 10-11
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
Recall that the fusion kernel is usually defined in terms 
of the conformal blocks appearing in the holomorphically 
factorized form of the four-point functions,
\begin{align}\notag
& \left\langle\, V_{\al_4}(z_4,\bz_4) V_{\al_3}(z_3,\bz_3)
V_{\al_2}(z_2,\bz_2)V_{\al_1}(z_1,\bz_1)\,\right\rangle
=\\ \label{s-channel}
&\qquad
=\int_{{Q}/{2}+\textup{i}\BR}d\al_s\;C(\al_4,\al_3,\al_s)C(Q-\al_s,\al_2,\al_1)
\CF_{\al_s}^{(s)}(A|Z)\CF_{\al_s}^{(s)}(A|\bar{Z})\,\\
&\qquad \label{t-channel}
=\int_{{Q}/{2}+\textup{i}\BR}d\al_t\;C(\al_4,\al_t,\al_1)C(Q-\al_t,\al_3,\al_2)
\CF_{\al_t}^{(t)}(A|Z)\CF_{\al_t}^{(t)}(A|\bar{Z})\,
\end{align}
where $A=(\al_1,\al_2,\al_3,\al_4)$, $Z=(z_1,z_2,z_3,z_4)$, and
\begin{align}\label{DOZZ}
C(\al_1 &,\al_2,\al_3)  =
(\pi \mu\ga(b^2)b^{2-2b^2})^{\frac{1}{b}(Q-\al_1-\al_2-\al_3)}\times \\
&\times\frac{\up_0\up(2\al_1)\up(2\al_2)\up(2\al_3)}
{\up(\al_1+\al_2+\al_3-Q)\up(\al_1+\al_3-\al_2)
\up(\al_1+\al_2-\al_3)\up(\al_2+\al_3-\al_1)
}
\,,
\notag\end{align}
here $\mu$ is the so-called cosmological constant in Liouville field 
theory and $\gamma(x)=\Ga(x)/\Ga(1-x)$. We also used $\up(x) = 
(\Ga_b(x)\Ga_b(Q-x))^{-1}$, $\up_0 = \frac{d \up(x)}{dx}|_{x=0}$ where 
the function $\Ga_b(x)$ is the Barnes double Gamma function.
Appendix A lists the definition and the relevant properties of $\Ga_b(x)$.

The first expression \rf{s-channel} for the four-point functions 
represents the operator product expansion of the fields 
$V_{\al_2}(z_2,\bz_2)$ and $V_{\al_1}(z_1,\bz_1)$, while the 
second expression \rf{t-channel} 
represents the operator product expansion of the fields 
$V_{\al_3}(z_3,\bz_3)$ and $V_{\al_2}(z_2,\bz_2)$. The equality of 
the two expressions \rf{s-channel} and \rf{t-channel} follows from the
validity of the relations 
\begin{equation}\label{fusion}
\CF_{\al_s}^{(s)}(A|Z)\,=\,\int_{{Q/2}+\textup{i}\BR} d\al_t\;F_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,
\CF_{\al_t}^{(t)}(A|Z)\,,
\end{equation}
which were established in \cite{Teschner:2001rv}. The following formula was
found in \cite{PT1,Teschner:2001rv},
\begin{equation}\label{FvsRW}
F_{\al_s\al_t}
\big[\,{}^{\al_3}_{\al_4}\,{}^{\al_2}_{\al_1}\,\big]\,=\,
\frac{N(\alpha_s,\alpha_2,\alpha_1)N(\alpha_4,\alpha_3,\alpha_s)}
{N(\alpha_t,\alpha_3,\alpha_2) N(\alpha_4,\alpha_t,\alpha_1)} 
\,M(\al_t)\,\big\{\,{}^{\al_1}_{\al_3}\;{}^{\al_2}_{{\al}_4}\,|\,
{}^{\al_s}_{\al_t}\big\}^{\rm an}\,,
\end{equation}
where
\begin{align} \label{normcoefN}
& N(\alpha_3,\alpha_2,\alpha_1)= \\ \nonumber & = 
\frac{\Ga_b(2Q-2\al_3)\Ga_b(2\al_2)\Ga_b(2\al_1)}
{\Ga_b(2Q-\alpha_1-\alpha_2-\alpha_3) \Ga_b(Q-\alpha_1-\alpha_2+\alpha_3) 
\Ga_b(\alpha_1+\alpha_3-\alpha_2) \Ga_b(\alpha_2+\alpha_3-\alpha_1)}.
\end{align}
