---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-008-handlebodies-as-conformal-blocks
section_title: "Handlebodies as conformal blocks"
section_number: null
pages: 24-27
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.992
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Let us now discuss how handlebodies contribute to the path integral of 3d gravity. As explained in \cite{Collier:2023fwi}, 3d gravity with a negative cosmological constant on a hyperbolic 3-manifold is related to two copies of Virasoro TQFT (VTQFT). The gravitational partition function is just the product 
\begin{equation}\label{eq:grav_to_VTQFT}
    Z_\text{grav}[M;\Omega,\bar\Omega] = Z_{\text{Vir}}[M;\Omega]Z^*_{\text{Vir}}[M;\bar\Omega].
\end{equation}
Here $\Omega,\bar\Omega$ are complex structure moduli fixed at the conformal boundary. For a genus-$g$ handlebody $M^{\mathcal{C}}$ with conformal boundary $\Sigma_g$, the VTQFT amplitude is given by the vacuum Virasoro conformal block:
\begin{equation}\label{eq:vir_block}
    Z_{\text{Vir}}[M^{\mathcal{C}};\Omega] = \mathcal{F}_g^{\,\mathcal{C}}(\mathds{1};\Omega).
\end{equation}
Here $\mathcal{C}$ denotes a choice of contractible cycles (i.e.~an identity channel) that is part of the data specifying the handlebody $M^{\mathcal{C}}$. In general, the genus-$g$ Virasoro conformal blocks are defined as solutions of the conformal Ward identities \cite{Belavin:1984vu} but for $g>1$ and $c>1$ they are not known analytically (although recursive representations exist in special cases \cite{Zamolodchikov:1985ie,Hadasz:2009db,Cho:2017oxl}, using the plumbing construction). In \cite{Collier:2024mgv}, the relation between the gravitational path integral on a handlebody and the square of the identity block was verified, for $g=2$, in the semiclassical ($c\to \infty$) limit, including the one-loop determinant (in a perturbative expansion around a degenerating locus of moduli space). See also \cite{Yin:2007gv,Headrick:2015gba}. In this match, one uses the Brown-Hennaux relation \cite{Brown:1986nw}
\begin{equation}
    c \sim \frac{3\ell_{\text{AdS}}}{2G_N}
\end{equation}
between the gravitational coupling and the central charge. However, we stress that the identification between the gravitational path integral and the identity block \eqref{eq:vir_block} is exact in $c$ and does not rely on a semiclassical approximation. This is striking, because it shows that the gravitational answer is fully determined by the representation theory of the Virasoro algebra, which is universal to every 2d CFT. 

\paragraph{Action of the mapping class group.}
The fact that 3d gravity partition functions are given by representation-theoretic objects holds more generally: in VTQFT, the partition function on any  3-manifold with boundary $\Sigma_g$ can be expressed as a state in the Hilbert space of Virasoro conformal blocks. This Hilbert space is spanned by non-degenerate blocks, which have internal conformal weights $h_i \geq \frac{c-1}{24}$. The identity module is a degenerate representation of the Virasoro algebra with $c>1$, but the identity block can be expressed in the basis of non-degenerate blocks in a dual channel through the crossing kernels introduced in section \ref{sec:2}:
\begin{equation}\label{eq:identitykernel}
    \mathcal{F}_g^{\,\gamma\cdot\mathcal{C}}(\mathds{1};\Omega) =\int_{0}^\infty \d^{3g-3} P \,\,\mathbb{K}^\gamma_{\mathds{1}\boldsymbol{P}}\, \mathcal{F}_g^{\,\mathcal{C}}(\boldsymbol{P};\Omega).
\end{equation}
Here we introduced the convenient Liouville parametrization $
    h_i= \frac{c-1}{24} + P_i^2,
$ where the Jacobian factor is implicit in $\mathbb{K}^\gamma_{\id \boldsymbol{P}}$, and used the notation
$\boldsymbol{P} = (P_1,\dots, P_{3g-3})$. This corresponds to a non-normalizable state in the VTQFT Hilbert space. So the handlebody partition functions, labeled by the mapping classes $\gamma$, are particular (non-normalizable) states in the Hilbert space of Virasoro conformal blocks whose expansion coefficients are the crossing kernels $\mathbb{K}^\gamma$. Here the relevant kernels are the \emph{identity} kernels $\mathbb{K}^\gamma_{\mathds{1}\boldsymbol{P}}$, whose definition requires the subtraction of null states by hand to account for the fact that the vacuum module is a degenerate representation \cite{Eberhardt:2023mrq}. 

Through equation \eqref{eq:identitykernel}, these identity kernels implement the action of the mapping class group on the set of handlebodies \eqref{eq:coset}. We can find the action of a Dehn twist generator, twisting along some non-contractible cycle $C$, by crossing to the channel where $T_C$ is diagonalized (acting on the conformal block as multiplication by a phase), and then cross back to the original channel. For example, consider the genus-2 block, with $\mathcal{C}$ the dumbbell channel: 
\begin{equation}
    \mathcal{F}_{g=2}^{\,\mathcal{C}}(\boldsymbol{P},\Omega) =  \mathcal{F}_{g=2}^{\,\mathcal{C}}\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]    (255.38,240.72) -- (285.63,240.58) ;

\draw  [draw opacity=0][line width=1.5]  (270.27,221.07) .. controls (270.35,221.06) and (270.43,221.06) .. (270.5,221.06) .. controls (274.04,221.06) and (276.9,229.85) .. (276.9,240.69) .. controls (276.9,251.54) and (274.04,260.33) .. (270.5,260.33) .. controls (270.3,260.33) and (270.11,260.3) .. (269.91,260.25) -- (270.5,240.69) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (270.27,221.07) .. controls (270.35,221.06) and (270.43,221.06) .. (270.5,221.06) .. controls (274.04,221.06) and (276.9,229.85) .. (276.9,240.69) .. controls (276.9,251.54) and (274.04,260.33) .. (270.5,260.33) .. controls (270.3,260.33) and (270.11,260.3) .. (269.91,260.25) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (271.61,260.04) .. controls (271.25,260.23) and (270.88,260.33) .. (270.5,260.33) .. controls (266.97,260.33) and (264.11,251.54) .. (264.11,240.69) .. controls (264.11,229.85) and (266.97,221.06) .. (270.5,221.06) .. controls (270.88,221.06) and (271.25,221.16) .. (271.61,221.35) -- (270.5,240.69) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (271.61,260.04) .. controls (271.25,260.23) and (270.88,260.33) .. (270.5,260.33) .. controls (266.97,260.33) and (264.11,251.54) .. (264.11,240.69) .. controls (264.11,229.85) and (266.97,221.06) .. (270.5,221.06) .. controls (270.88,221.06) and (271.25,221.16) .. (271.61,221.35) ;  

\draw    (192.53,240.99) .. controls (192.68,214.69) and (213.96,207.39) .. (228.02,207.74) .. controls (246.09,208.09) and (256.48,221.19) .. (270.54,221.1) .. controls (284.84,221.22) and (295.72,207.92) .. (313.09,207.82) .. controls (327.39,207.95) and (348.65,214.63) .. (348.5,241.14) .. controls (348.59,268.11) and (327.31,274.74) .. (313.02,274.4) .. controls (295.88,274.49) and (284.79,260.94) .. (270.49,261.04) .. controls (256.43,261.14) and (245.78,274.44) .. (227.94,274.31) .. controls (214.12,274.63) and (192.86,267.95) .. (192.53,240.99) -- cycle ;

\draw    (213.94,241.37) .. controls (219.38,229.75) and (241.27,228.37) .. (250.49,240.72) ;

\draw    (213.94,241.37) .. controls (220.49,253.03) and (244.83,252.84) .. (250.49,240.72) ;

\draw    (290.24,241.34) .. controls (296.37,229.75) and (319.04,229.06) .. (326.79,240.69) ;

\draw    (290.24,241.34) .. controls (300.51,252.6) and (321.07,250.94) .. (326.79,240.69) ;

\draw    (290.24,241.34) .. controls (289.67,240.6) and (289.48,240.51) .. (289.08,239.51) ;

\draw  [draw opacity=0][line width=1.5]  (192.84,241.1) .. controls (192.83,240.98) and (192.82,240.85) .. (192.82,240.72) .. controls (192.82,237.25) and (197.56,234.43) .. (203.41,234.43) .. controls (209.26,234.43) and (214,237.25) .. (214,240.72) .. controls (214,241.25) and (213.89,241.77) .. (213.68,242.26) -- (203.41,240.72) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (192.84,241.1) .. controls (192.83,240.98) and (192.82,240.85) .. (192.82,240.72) .. controls (192.82,237.25) and (197.56,234.43) .. (203.41,234.43) .. controls (209.26,234.43) and (214,237.25) .. (214,240.72) .. controls (214,241.25) and (213.89,241.77) .. (213.68,242.26) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (213.78,239.43) .. controls (213.93,239.85) and (214,240.28) .. (214,240.72) .. controls (214,244.19) and (209.26,247.01) .. (203.41,247.01) .. controls (197.56,247.01) and (192.82,244.19) .. (192.82,240.72) .. controls (192.82,240.34) and (192.88,239.97) .. (192.99,239.61) -- (203.41,240.72) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (213.78,239.43) .. controls (213.93,239.85) and (214,240.28) .. (214,240.72) .. controls (214,244.19) and (209.26,247.01) .. (203.41,247.01) .. controls (197.56,247.01) and (192.82,244.19) .. (192.82,240.72) .. controls (192.82,240.34) and (192.88,239.97) .. (192.99,239.61) ;  

\draw  [draw opacity=0][line width=1.5]  (326.47,240.01) .. controls (326.97,236.81) and (331.63,234.3) .. (337.3,234.3) .. controls (343.1,234.3) and (347.83,236.91) .. (348.17,240.21) -- (337.3,240.58) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (326.47,240.01) .. controls (326.97,236.81) and (331.63,234.3) .. (337.3,234.3) .. controls (343.1,234.3) and (347.83,236.91) .. (348.17,240.21) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (348.04,239.57) .. controls (348.14,239.9) and (348.19,240.24) .. (348.19,240.58) .. controls (348.19,244.05) and (343.31,246.87) .. (337.3,246.87) .. controls (331.29,246.87) and (326.42,244.05) .. (326.42,240.58) .. controls (326.42,240.24) and (326.47,239.9) .. (326.56,239.58) -- (337.3,240.58) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (348.04,239.57) .. controls (348.14,239.9) and (348.19,240.24) .. (348.19,240.58) .. controls (348.19,244.05) and (343.31,246.87) .. (337.3,246.87) .. controls (331.29,246.87) and (326.42,244.05) .. (326.42,240.58) .. controls (326.42,240.24) and (326.47,239.9) .. (326.56,239.58) ;  

\draw    (250.49,240.72) .. controls (251.01,239.81) and (251.19,238.92) .. (251.36,238.36) ;

\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]  (203.41,240.72) .. controls (203.41,228.9) and (215.04,219.32) .. (229.39,219.32) .. controls (243.74,219.32) and (255.38,228.9) .. (255.38,240.72) .. controls (255.38,252.54) and (243.74,262.12) .. (229.39,262.12) .. controls (215.04,262.12) and (203.41,252.54) .. (203.41,240.72) -- cycle ;

\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=1.5]  (285.63,240.58) .. controls (285.63,228.76) and (297.19,219.18) .. (311.46,219.18) .. controls (325.73,219.18) and (337.3,228.76) .. (337.3,240.58) .. controls (337.3,252.4) and (325.73,261.98) .. (311.46,261.98) .. controls (297.19,261.98) and (285.63,252.4) .. (285.63,240.58) -- cycle ;

\draw    (264.38,269.13) .. controls (254.31,258.39) and (262.06,251.65) .. (267.74,245.34) ;
\draw [shift={(269.63,243.13)}, rotate = 128.16] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;


\draw (203.75,212.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (321.75,214.15) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};

\draw (263.25,264.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};
\end{tikzpicture}\right]\,.
\end{equation}
We have drawn the dual graph $\Gamma_\mathcal{C}$ in gray and labelled the edges by Liouville momenta $P_1,P_2,P_3$. Now choose $\gamma$ to be following product of Dehn twists, where we twist along the non-contractible cycles $(B_1,B_2,A)$ highlighted in red:
\begin{equation}\label{eq:dehntwistmappingclass}
    \gamma = T_{B_1}T_{B_2}T_{A} :\quad \tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (230.7,246.93) .. controls (230.51,246.57) and (230.41,246.2) .. (230.41,245.83) .. controls (230.41,242.29) and (239.2,239.43) .. (250.04,239.43) .. controls (260.89,239.43) and (269.68,242.29) .. (269.68,245.83) .. controls (269.68,246.2) and (269.58,246.57) .. (269.39,246.93) -- (250.04,245.83) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (230.7,246.93) .. controls (230.51,246.57) and (230.41,246.2) .. (230.41,245.83) .. controls (230.41,242.29) and (239.2,239.43) .. (250.04,239.43) .. controls (260.89,239.43) and (269.68,242.29) .. (269.68,245.83) .. controls (269.68,246.2) and (269.58,246.57) .. (269.39,246.93) ;  

\draw  [draw opacity=0][line width=1.5]  (250.27,226.33) .. controls (250.35,226.32) and (250.43,226.32) .. (250.5,226.32) .. controls (254.04,226.32) and (256.9,235.11) .. (256.9,245.95) .. controls (256.9,256.79) and (254.04,265.59) .. (250.5,265.59) .. controls (250.3,265.59) and (250.11,265.56) .. (249.91,265.5) -- (250.5,245.95) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (250.27,226.33) .. controls (250.35,226.32) and (250.43,226.32) .. (250.5,226.32) .. controls (254.04,226.32) and (256.9,235.11) .. (256.9,245.95) .. controls (256.9,256.79) and (254.04,265.59) .. (250.5,265.59) .. controls (250.3,265.59) and (250.11,265.56) .. (249.91,265.5) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (251.61,265.29) .. controls (251.25,265.49) and (250.88,265.59) .. (250.5,265.59) .. controls (246.97,265.59) and (244.11,256.79) .. (244.11,245.95) .. controls (244.11,235.11) and (246.97,226.32) .. (250.5,226.32) .. controls (250.88,226.32) and (251.25,226.42) .. (251.61,226.61) -- (250.5,245.95) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (251.61,265.29) .. controls (251.25,265.49) and (250.88,265.59) .. (250.5,265.59) .. controls (246.97,265.59) and (244.11,256.79) .. (244.11,245.95) .. controls (244.11,235.11) and (246.97,226.32) .. (250.5,226.32) .. controls (250.88,226.32) and (251.25,226.42) .. (251.61,226.61) ;  

\draw    (172.53,246.25) .. controls (172.68,219.95) and (193.96,212.65) .. (208.02,213) .. controls (226.09,213.35) and (236.48,226.45) .. (250.54,226.35) .. controls (264.84,226.48) and (275.72,213.17) .. (293.09,213.08) .. controls (307.39,213.2) and (328.65,219.88) .. (328.5,246.4) .. controls (328.59,273.36) and (307.31,280) .. (293.02,279.65) .. controls (275.88,279.75) and (264.79,266.2) .. (250.49,266.3) .. controls (236.43,266.39) and (225.78,279.7) .. (207.94,279.57) .. controls (194.12,279.89) and (172.86,273.21) .. (172.53,246.25) -- cycle ;

\draw    (193.94,246.63) .. controls (199.38,235) and (221.27,233.63) .. (230.49,245.98) ;

\draw    (193.94,246.63) .. controls (200.49,258.29) and (224.83,258.1) .. (230.49,245.98) ;

\draw    (270.24,246.59) .. controls (276.37,235) and (299.04,234.32) .. (306.79,245.94) ;

\draw    (270.24,246.59) .. controls (280.51,257.86) and (301.07,256.2) .. (306.79,245.94) ;

\draw    (270.24,246.59) .. controls (269.67,245.85) and (269.48,245.76) .. (269.08,244.77) ;

\draw  [draw opacity=0][line width=1.5]  (172.84,246.36) .. controls (172.83,246.23) and (172.82,246.11) .. (172.82,245.98) .. controls (172.82,242.51) and (177.56,239.69) .. (183.41,239.69) .. controls (189.26,239.69) and (194,242.51) .. (194,245.98) .. controls (194,246.51) and (193.89,247.02) .. (193.68,247.52) -- (183.41,245.98) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (172.84,246.36) .. controls (172.83,246.23) and (172.82,246.11) .. (172.82,245.98) .. controls (172.82,242.51) and (177.56,239.69) .. (183.41,239.69) .. controls (189.26,239.69) and (194,242.51) .. (194,245.98) .. controls (194,246.51) and (193.89,247.02) .. (193.68,247.52) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (193.78,244.69) .. controls (193.93,245.11) and (194,245.54) .. (194,245.98) .. controls (194,249.45) and (189.26,252.26) .. (183.41,252.26) .. controls (177.56,252.26) and (172.82,249.45) .. (172.82,245.98) .. controls (172.82,245.6) and (172.88,245.23) .. (172.99,244.87) -- (183.41,245.98) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (193.78,244.69) .. controls (193.93,245.11) and (194,245.54) .. (194,245.98) .. controls (194,249.45) and (189.26,252.26) .. (183.41,252.26) .. controls (177.56,252.26) and (172.82,249.45) .. (172.82,245.98) .. controls (172.82,245.6) and (172.88,245.23) .. (172.99,244.87) ;  

\draw  [draw opacity=0][line width=1.5]  (306.47,245.27) .. controls (306.97,242.06) and (311.63,239.55) .. (317.3,239.55) .. controls (323.1,239.55) and (327.83,242.17) .. (328.17,245.47) -- (317.3,245.84) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (306.47,245.27) .. controls (306.97,242.06) and (311.63,239.55) .. (317.3,239.55) .. controls (323.1,239.55) and (327.83,242.17) .. (328.17,245.47) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (328.04,244.83) .. controls (328.14,245.16) and (328.19,245.49) .. (328.19,245.84) .. controls (328.19,249.31) and (323.31,252.13) .. (317.3,252.13) .. controls (311.29,252.13) and (306.42,249.31) .. (306.42,245.84) .. controls (306.42,245.5) and (306.47,245.16) .. (306.56,244.83) -- (317.3,245.84) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (328.04,244.83) .. controls (328.14,245.16) and (328.19,245.49) .. (328.19,245.84) .. controls (328.19,249.31) and (323.31,252.13) .. (317.3,252.13) .. controls (311.29,252.13) and (306.42,249.31) .. (306.42,245.84) .. controls (306.42,245.5) and (306.47,245.16) .. (306.56,244.83) ;  

\draw    (230.49,245.98) .. controls (231.01,245.07) and (231.19,244.18) .. (231.36,243.62) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (183.41,245.98) .. controls (183.41,234.16) and (195.79,224.58) .. (211.06,224.58) .. controls (226.32,224.58) and (238.7,234.16) .. (238.7,245.98) .. controls (238.7,257.8) and (226.32,267.38) .. (211.06,267.38) .. controls (195.79,267.38) and (183.41,257.8) .. (183.41,245.98) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (262.02,245.84) .. controls (262.02,234.02) and (274.39,224.44) .. (289.66,224.44) .. controls (304.93,224.44) and (317.3,234.02) .. (317.3,245.84) .. controls (317.3,257.66) and (304.93,267.24) .. (289.66,267.24) .. controls (274.39,267.24) and (262.02,257.66) .. (262.02,245.84) -- cycle ;

\draw  [draw opacity=0][line width=1.5]  (269.66,245.59) .. controls (269.67,245.67) and (269.68,245.75) .. (269.68,245.83) .. controls (269.68,249.36) and (260.89,252.22) .. (250.04,252.22) .. controls (239.2,252.22) and (230.41,249.36) .. (230.41,245.83) .. controls (230.41,245.63) and (230.44,245.43) .. (230.49,245.24) -- (250.04,245.83) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (269.66,245.59) .. controls (269.67,245.67) and (269.68,245.75) .. (269.68,245.83) .. controls (269.68,249.36) and (260.89,252.22) .. (250.04,252.22) .. controls (239.2,252.22) and (230.41,249.36) .. (230.41,245.83) .. controls (230.41,245.63) and (230.44,245.43) .. (230.49,245.24) ;  

\draw    (243.2,275.6) .. controls (234.87,266.08) and (238.31,258.07) .. (240.88,254.24) ;
\draw [shift={(242.7,251.9)}, rotate = 128.66] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;
\draw  [color=wilsonred  ,draw opacity=1 ] (209,222.5) -- (216.1,224.6) -- (209,226.7) ;
\draw  [color=wilsonred  ,draw opacity=1 ] (287.8,222.5) -- (294.9,224.6) -- (287.8,226.7) ;
\draw  [color=wilsonred  ,draw opacity=1 ] (247,250.1) -- (254.1,252.2) -- (247,254.3) ;

\draw (188.27,215.58) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$B_{1}$};

\draw (298.98,215.62) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$B_{2}$};

\draw (241.43,268.66) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$A$};
\end{tikzpicture}\,.
\end{equation}
 One can convince oneself that $\gamma$ acts on the contractible cycles as shown in figure \ref{fig:crossing}. The corresponding kernel $\mathbb{K}^\gamma_{\mathds{1}\boldsymbol{P}}$ can be found by using $\mathbb{F}$ and $\mathbb{S}$ kernels to cross to the dual channels, where $T$ acts by a phase $\mathbb{T}_P = \e^{-2\pi i h_P}$, giving:
\begin{equation}\label{eq:dehntwistkernel}
    \mathbb{K}^\gamma_{\mathds{1}P_1P_2P_3} = (\mathbb{S}\mathbb{T}\mathbb{S})_{\mathds{1}P_1}(\mathbb{S}\mathbb{T}\mathbb{S})_{\mathds{1}P_2} (\mathbb{F}\mathbb{T}\mathbb{F})_{\mathds{1}P_3}\,.
\end{equation}
More explicitly, we have:
\begin{align}
    (\mathbb{F}\mathbb{T}\mathbb{F})_{\mathds{1}P_3} &= \int_0^\infty \d P \,\fker{\mathds{1}}{P}{P_2}{P_1}{P_1}{P_2}\,\mathbb{T}_P\,\fker{P}{P_3}{P_1}{P_1}{P_2}{P_2}, \\
    (\mathbb{S}\mathbb{T}\mathbb{S})_{\mathds{1}P_1} &= \int_0^\infty \d P\,\sker{\mathds{1}}{P}{\mathds{1}}\,\mathbb{T}_{P}\,\sker{P}{P_1}{\mathds{1}} = \sker{\mathds{1}}{P_1}{\mathds{1}}\,\mathbb{T}_{P_1}^*\,,
\end{align}
where in the second line we used the $\text{PSL}(2,\mathbb{Z})$ identity $ \mathbb{S}\mathbb{T}\mathbb{S} = \mathbb{T}^*\mathbb{S}\mathbb{T}^*$ and $\mathbb{T}_{\mathds{1}} = 1$.
This example shows how Dehn twists are represented by crossing kernels acting on identity blocks. The expressions in terms of Dehn twists can always be re-expressed in terms of the Moore-Seiberg generators $\mathbb{B},\mathbb{F},\mathbb{S}$, as we will see below. 

\paragraph{Action of the handlebody group.} 
We can ask when a mapping class, represented by $\mathbb{K}^\gamma$, is in the handlebody group $\mathcal{H}_g$.  On the level of conformal blocks, a handlebody group element leaves the vacuum block invariant up to a phase:
\begin{equation}\label{eq:H_group_invariance}
\mathcal{F}^{\,\gamma\cdot\mathcal{C}}_g(\mathds{1};\Omega) = \e^{i\theta_\gamma}\mathcal{F}^{\,\mathcal{C}}_g(\mathds{1};\Omega), \quad \gamma \in \mathcal{H}_g.
\end{equation}
The overall phase is a manifestation of the framing anomaly familiar from Chern Simons theory.
Since the gravitational partition function on the handlebody is the absolute value squared of the identity block (recall \eqref{eq:grav_to_VTQFT}), this phase factor drops out. Hence, any two  handlebodies that are diffeomorphic have the same gravitational partition function, as they should. 

On the level of the crossing kernels, the condition in equation \eqref{eq:H_group_invariance} can be translated using the block decomposition \eqref{eq:identitykernel} to the statement that for $\gamma \in \mathcal{H}_g$, the associated crossing kernel is the Dirac delta up to an overall $\bm{h}$-independent phase:
\begin{equation}
    \mathbb{K}^\gamma_{\mathds{1}\bm{h}} = \e^{i\theta_\gamma} \delta(\bm{h})\,, \quad \gamma \in \mathcal{H}_g.
\end{equation}
We can be more explicit in the genus-$1$ case. There, the vacuum block is simply the Virasoro vacuum character $\chi_{\mathds{1}}(\tau) = q^{-\frac{c-1}{24}}\frac{1}{\eta(\tau)}(1-q)$, and the handlebody group consists of the Dehn twists around the contractible cycle $\tau \to \tau+n$, where $n\in \mathbb{Z}$. These act on the vacuum character as 
multiplication by a phase:  
\begin{equation}
    \chi_{\mathds{1}}(\tau+1) = \e^{-2\pi i \frac{c}{24}}\chi_{\mathds{1}}(\tau),
\end{equation}
where the phase is just the conformal anomaly determined by the central charge $c$.
