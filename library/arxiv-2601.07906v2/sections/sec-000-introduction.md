---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 4-10
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.998
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:intro}


The gravitational path integral continues to be an enigmatic yet essential tool in understanding aspects of holography. Low-dimensional models have served as valuable laboratories for uncovering some of its more intricate features. From these models, much evidence has been gathered in favour of the idea that the path integral for pure Einstein gravity can be understood as performing a \emph{statistical} average over the data that define the dual conformal field theory. Developing this idea in three-dimensional gravity has become an active direction of current research, but our understanding of the statistical holographic dictionary is still incomplete. 

Thanks to the absence of local bulk degrees of freedom \cite{Witten:1988hc}, pure AdS$_3$ quantum gravity is a particularly suitable playground to explore the statistical nature of the gravitational path integral, and significant progress has been made over the past few years \cite{Belin:2020hea,Chandra:2022bqq,Cotler:2020ugk,Mertens:2022ujr,DiUbaldo:2023qli,Belin:2023efa,Jafferis:2025vyp,Schlenker:2022dyo,deBoer:2023vsm,Collier:2023fwi, Collier:2024mgv,deBoer:2024mqg,deBoer:2025rct,Hartman:2025ula,Hartman:2025cyj,Chandra:2025fef,Yan:2023rjh,Chandra:2024vhm}. As a starting point, the main entry in the dictionary between pure 3-dimensional gravity and the statistical ensemble of CFT$_2$ data  posits that averaged boundary quantities are computed as a sum over topologies in the bulk:  
\begin{equation}\label{eq:sumovertopologies}
    \overline{Z[\Sigma]} = \sum_{\partial M = \Sigma} Z_\text{grav}[M]\,.
\end{equation}
On the right-hand side, $Z_\text{grav}$ denotes the gravitational path integral for pure Einstein gravity with a negative cosmological constant, on a fixed bulk topology $M$.\footnote{For notational clarity, we suppress the dependence on the moduli of the boundary Riemann surface and use $\Sigma$ as a placeholder for all the boundary data.} The sum runs over all distinct bulk 3-manifolds whose asymptotic boundary is $\Sigma$. If $\Sigma$ is a connected Riemann surface of genus $g$, the left-hand side computes the average genus $g$ partition function, in some yet to be specified statistical model of CFT$_2$ data. If $\Sigma$  consists of multiple disconnected components, then the right-hand side includes Euclidean wormhole topologies and the left-hand side computes a higher statistical moment of CFT$_2$ partition functions. In recent years, powerful new tools have been developed to compute $Z_\text{grav}[M]$ exactly, i.e.~to all orders in $G_N$, for a large class of 3-manifolds \cite{Collier:2023fwi,Collier:2024mgv}. Nevertheless, 3-manifold topology is a rich and complex subject, which means that understanding the full sum over topologies in \eqref{eq:sumovertopologies} is a difficult (and unresolved) problem.

In this paper, our principal aim is to systematize the correspondence between universal statistics of 2d conformal field theory and pure 3d quantum gravity. In particular, we want to understand what role the sum over topologies plays in the pure gravity/ensemble duality, and explain how the bulk sum over topologies arises from the \emph{boundary} perspective. We will explore how, and to what extent, the 3-manifolds contributing to \eqref{eq:sumovertopologies} are organized to furnish a consistent statistical ensemble of CFT$_2$ data, compatible with kinematic constraints, crossing symmetry, modular invariance and typicality at high energies.


\paragraph{Handlebodies and crossing symmetry.} To illustrate the question that we want to ask, suppose that the asymptotic boundary $\Sigma$ is a Riemann surface of genus $g\geq 1$, and fix the boundary moduli $\Omega_i,\bar\Omega_i$. 
Then a natural class of 3-manifolds contributing to the sum over topologies consists of the genus-$g$ \emph{handlebodies}:\footnote{Here and in the rest of the paper, we use the symbol $\supset$ to denote that the right-hand side is a \emph{sub-sum} of the full sum over topologies.}
\begin{equation}\label{eq:handlebodysum}
        \overline{Z[\Sigma_{g}]} \quad \supset \sum_{\gamma \in \text{MCG}(\Sigma_{g})/\mathcal{H}_g} \!Z_\text{grav}[M^\gamma]\,.
    \end{equation}
Topologically, a genus-$g$ handlebody is homeomorphic to a `filled-in' genus-$g$ surface. Geometrically, it admits an infinite-volume hyperbolic metric after choosing a collection of $3g-3$ disjoint cycles on the boundary $\Sigma_g$ that become contractible in the bulk (a choice of identity channel, in CFT parlance). Different choices of cycles are related to each other by crossing transformations $\gamma$, which are elements of the mapping class group of $\Sigma_g$.\footnote{For an introduction to crossing transformations, see \cite{Eberhardt:2023mrq}.} An example of such a mapping class group transformation is shown in figure \ref{fig:crossing}.
The sum over handlebodies can hence be written as a sum over crossing transformations, modulo the bulk mapping class group of the handlebody $\mathcal{H}_g$ (the so-called handlebody group).

\begin{figure}
    \centering
    \tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (460.19,220.08) .. controls (468.13,222.25) and (520.13,177.25) .. (537.08,173.25) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (434.88,259) .. controls (449.13,257) and (504.13,212) .. (514.38,210.25) ;

\draw  [draw opacity=0][line width=1.5]  (226.28,190.5) .. controls (230.28,192.05) and (233.38,202.8) .. (233.38,215.83) .. controls (233.38,227.79) and (230.77,237.83) .. (227.24,240.6) -- (225.28,215.83) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (226.28,190.5) .. controls (230.28,192.05) and (233.38,202.8) .. (233.38,215.83) .. controls (233.38,227.79) and (230.77,237.83) .. (227.24,240.6) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (225.88,241.28) .. controls (225.68,241.33) and (225.48,241.35) .. (225.28,241.35) .. controls (220.8,241.35) and (217.18,229.92) .. (217.18,215.83) .. controls (217.18,202.26) and (220.54,191.17) .. (224.78,190.36) -- (225.28,215.83) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (225.88,241.28) .. controls (225.68,241.33) and (225.48,241.35) .. (225.28,241.35) .. controls (220.8,241.35) and (217.18,229.92) .. (217.18,215.83) .. controls (217.18,202.26) and (220.54,191.17) .. (224.78,190.36) ;  


\draw [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.3 ]   (132.53,216.22) .. controls (132.71,182.04) and (157.87,172.55) .. (174.5,173) .. controls (195.87,173.45) and (208.15,190.48) .. (224.78,190.36) .. controls (241.69,190.52) and (254.56,173.23) .. (275.1,173.11) .. controls (292.01,173.27) and (317.15,181.95) .. (316.98,216.42) .. controls (317.08,251.46) and (291.92,260.09) .. (275.01,259.63) .. controls (254.75,259.76) and (241.64,242.15) .. (224.73,242.27) .. controls (208.1,242.4) and (195.51,259.69) .. (174.41,259.53) .. controls (158.06,259.94) and (132.92,251.26) .. (132.53,216.22) -- cycle ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (157.85,216.71) .. controls (164.29,201.6) and (190.16,199.81) .. (201.07,215.87) ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (157.85,216.71) .. controls (165.6,231.87) and (194.38,231.62) .. (201.07,215.87) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (99,151) -- (615,151) -- (615,281.67) -- (99,281.67) -- cycle ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (248.08,216.67) .. controls (255.33,201.6) and (282.14,200.71) .. (291.3,215.82) ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (248.08,216.67) .. controls (260.23,231.31) and (284.54,229.15) .. (291.3,215.82) ;

\draw    (248.08,216.67) .. controls (247.41,215.71) and (247.18,215.59) .. (246.71,214.29) ;


\draw [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.33 ]   (393,215.69) .. controls (393.17,181.51) and (418.34,172.02) .. (434.96,172.47) .. controls (456.34,172.93) and (468.62,189.96) .. (485.25,189.83) .. controls (502.16,190) and (515.03,172.7) .. (535.57,172.58) .. controls (552.48,172.74) and (577.62,181.42) .. (577.44,215.89) .. controls (577.55,250.93) and (552.39,259.56) .. (535.48,259.11) .. controls (515.22,259.23) and (502.1,241.62) .. (485.2,241.75) .. controls (468.57,241.88) and (455.97,259.17) .. (434.88,259) .. controls (418.53,259.41) and (393.38,250.74) .. (393,215.69) -- cycle ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (418.84,214.8) .. controls (426.53,231.11) and (456.13,231.65) .. (464.1,213.73) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]    (437.81,204.86) .. controls (467.88,176) and (512.63,258.75) .. (543.51,223.89) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (437.81,204.86) .. controls (424.43,199.91) and (423.4,176.01) .. (441.9,173.07) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]    (441.9,173.07) .. controls (446.65,177.69) and (469.13,198.75) .. (491.42,194.73) .. controls (513.72,190.72) and (540.71,182.63) .. (532.72,204.7) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (449.62,226.43) .. controls (469.27,244.58) and (508.72,184.12) .. (532.72,204.7) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]    (449.62,226.43) .. controls (444.54,242.49) and (456.49,237.22) .. (484.31,234.86) .. controls (512.13,232.5) and (520.46,259.47) .. (541.24,259.2) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (541.24,259.2) .. controls (553.48,253.31) and (553.48,232.99) .. (543.51,223.89) ;

\draw [line width=1.5]    (332.13,215.36) -- (375.18,215.36) ;
\draw [shift={(379.18,215.36)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.13,-3.9) -- (0,0) -- (8.13,3.9) -- cycle    ;

\draw  [draw opacity=0][line width=1.5]  (132.9,215.37) .. controls (133.29,211.09) and (138.74,207.7) .. (145.4,207.7) .. controls (151.8,207.7) and (157.09,210.83) .. (157.83,214.88) -- (145.4,215.87) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (132.9,215.37) .. controls (133.29,211.09) and (138.74,207.7) .. (145.4,207.7) .. controls (151.8,207.7) and (157.09,210.83) .. (157.83,214.88) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (157.91,215.57) .. controls (157.92,215.67) and (157.92,215.77) .. (157.92,215.87) .. controls (157.92,220.38) and (152.32,224.03) .. (145.4,224.03) .. controls (138.61,224.03) and (133.08,220.51) .. (132.88,216.11) -- (145.4,215.87) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (157.91,215.57) .. controls (157.92,215.67) and (157.92,215.77) .. (157.92,215.87) .. controls (157.92,220.38) and (152.32,224.03) .. (145.4,224.03) .. controls (138.61,224.03) and (133.08,220.51) .. (132.88,216.11) ;  


\draw  [draw opacity=0][line width=1.5]  (290.89,215.18) .. controls (291.3,210.9) and (296.9,207.52) .. (303.74,207.52) .. controls (310.31,207.52) and (315.72,210.64) .. (316.51,214.67) -- (303.74,215.69) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (290.89,215.18) .. controls (291.3,210.9) and (296.9,207.52) .. (303.74,207.52) .. controls (310.31,207.52) and (315.72,210.64) .. (316.51,214.67) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (316.6,215.39) .. controls (316.6,215.49) and (316.61,215.59) .. (316.61,215.69) .. controls (316.61,220.2) and (310.84,223.86) .. (303.74,223.86) .. controls (296.76,223.86) and (291.08,220.33) .. (290.87,215.94) -- (303.74,215.69) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (316.6,215.39) .. controls (316.6,215.49) and (316.61,215.59) .. (316.61,215.69) .. controls (316.61,220.2) and (310.84,223.86) .. (303.74,223.86) .. controls (296.76,223.86) and (291.08,220.33) .. (290.87,215.94) ;  


\draw    (201.07,215.87) .. controls (201.68,214.68) and (201.89,213.53) .. (202.1,212.8) ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (509.33,216.92) .. controls (516.58,201.85) and (543.39,200.96) .. (552.55,216.07) ;

\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (509.33,216.92) .. controls (521.48,231.56) and (545.79,229.4) .. (552.55,216.07) ;

\draw    (509.33,216.92) .. controls (508.66,215.96) and (508.43,215.84) .. (507.96,214.54) ;


\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (419.73,216.71) .. controls (428.55,199.5) and (455.33,201.97) .. (462.96,215.87) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.5]    (434.88,259) .. controls (422.38,254) and (406.13,238.5) .. (405.88,214) .. controls (405.63,189.5) and (442.38,184) .. (468.13,196.5) .. controls (493.88,209) and (506.38,203.75) .. (514.38,210.25) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.5]    (537.08,173.25) .. controls (549.17,178.05) and (564.88,192.94) .. (565.12,216.48) .. controls (565.37,240.01) and (529.82,245.29) .. (504.92,233.29) .. controls (480.02,221.28) and (467.93,226.32) .. (460.19,220.08) ;

\draw (351.73,191.56) node [anchor=north west][inner sep=0.75pt]    {\large $\gamma $};
\end{tikzpicture}
    \caption{Example of a crossing transformation $\gamma$ on a genus-$2$ Riemann surface. The two sets of contractible cycles (the thick closed curves) lead to two distinct genus-$2$ handlebodies upon filling in the bulk. 
    }
    \label{fig:crossing}
\end{figure}


Note that in the $g=1$ case, the handlebody sum \eqref{eq:handlebodysum} was studied by Maloney and Witten \cite{Maloney:2007ud} and subsequently by Keller and Maloney  \cite{Keller:2014xba}. The resulting sum over solid tori takes the form of a Poincar\'e series, with $\text{MCG}(\Sigma_{1}) = \PSL(2,\mathbb{Z})$ and $\mathcal{H}_1 = \mathbb{Z}$. Each $Z_\text{grav}[M^\gamma]$ evaluates to a product of left- and right moving Virasoro vacuum characters, $|\chi_{\mathds{1}}(\gamma\cdot\tau)|^2$, and hence the role of the sum over topologies is quite clear: it renders the average partition function modular invariant. Restricting the sum to a smaller set of bulk saddles would violate modular invariance of the average.\footnote{A \emph{larger} set of bulk manifolds may be included, as long as it does not spoil modular invariance. In the genus-1 case, such additional contributions are conjectured to be necessary in order to cure the negativity in the spectral density in the near-extremal limit \cite{Benjamin:2019stq,Ghosh:2019rcj, Maxfield:2020ale,Benjamin:2020mfz,DiUbaldo:2023hkc}.}


In the higher-genus case, $g>1$, the gravitational path integral on a handlebody evaluates to the product of left- and right-moving vacuum Virasoro conformal blocks in the channel specified by $\gamma$ \cite{Collier:2023fwi}. Each vacuum block resums all contributions from descendant states, which are interpreted in 3d gravity as boundary gravitons \cite{Giombi:2008vd}. Similar to the genus-1 case, the sum over handlebodies renders the average genus-$g$ CFT partition function crossing symmetric (invariant under the action of the mapping class group). 

The sum over handlebodies has an interesting implication for the statistics of OPE coefficients in our model. In the original statistical model of \cite{Belin:2020hea, Chandra:2022bqq}, a Gaussian ansatz was used to describe the statistics of heavy OPE coefficients. This simplified description captures many important features of gravity, but it generates only a finite subset of handlebodies (for the genus-$2$ computation, see section 8.3 of \cite{Chandra:2022bqq}). Hence, the average is only invariant under a finite subset of all crossing transformations. Instead, insisting on a fully crossing symmetric average $\overline{Z[\Sigma_g]}$ implies the existence of \emph{non-Gaussianities} in the statistical description of the CFT$_2$ data \cite{Belin:2023efa, Belin:2021ryy,Anous:2021caj,Collier:2023fwi,Collier:2024mgv,deBoer:2024mqg, deBoer:2025rct, Hartman:2025ula,Hartman:2025cyj,deBoer:2023vsm,Chandra:2025fef}.
 In section \ref{sec:3}, we will show how to systematically include non-Gaussian OPE statistics in order to reproduce the full (infinite) sum over handlebodies, for all genera $g\geq 1$. One useful consequence of this systematic approach is that the spins $J_i = h_i-\bar h_i$ of all propagating heavy operators are appropriately quantized.

    \paragraph{Why include non-handlebodies?} Now we come to the central question of this paper. In three dimensions, there are many single-boundary topologies that are not handlebodies: the classic example of such a non-handlebody (in the 3d gravity literature) is the twisted $I$-bundle of \cite{Yin:2007at}. However, since the handlebody sum in equation \eqref{eq:handlebodysum} already furnishes a crossing symmetric average (for any choice of connected genus-$g$ boundary), one could ask why non-handlebodies are needed at all, from the perspective of the boundary CFT. Said differently, is there a redundancy in the possible consistent statistical ensembles dual to pure 3d gravity? 
    
    This question is especially compelling for a connected boundary of genus $g\geq 2$. In the $g=1$ case, all non-handlebodies are off-shell \cite{Maloney:2007ud}, so there is no semiclassical saddlepoint approximation for $Z_\text{grav}$ on such topologies. These include single-boundary Seifert manifolds \cite{Maxfield:2020ale,deBoer:2025rct}, for which it is currently not known how to  compute the gravitational path integral from first principles. By contrast, for $g\geq 2$ there are many non-handlebodies that support well-defined \emph{on-shell} solutions of pure Einstein gravity with the correct asymptotic boundary behaviour, so there is no a priori reason to discard their contributions. Moreover, they can be added in a manifestly crossing symmetric way, by summing over mapping class group images of a given `seed' non-handlebody, as will be shown in section \ref{sec:minimal completion}. The question is: does the statistical theory of CFT$_2$ data require these saddles for internal consistency, or are they optional? We view this question as a statistical version of the conformal bootstrap, applied to 3d gravity.

    Let us emphasize that the above question is distinct from previous work on Euclidean wormholes and the factorization puzzle \cite{Belin:2020hea,Chandra:2022bqq,Maldacena:2004rf,Marolf:2021kjc,Saad:2019lba,Marolf:2020xie,Stanford:2020wkf}. When the boundary $\Sigma$ has multiple disconnected components, there are well-known wormhole topologies connecting them (the simplest example being the Maldacena-Maoz solution \cite{Maldacena:2004rf}), and these are always non-handlebodies. Moreover, it is by now well understood that these Euclidean wormholes probe higher statistical moments (such as the variance) in the ensemble of OPE coefficients \cite{Belin:2020hea,Chandra:2022bqq, Collier:2024mgv, deBoer:2024mqg}. So, in the multi-boundary case, non-handlebodies are clearly needed for the ensemble to have non-zero fluctuations around the average. 
    On the other hand, the \emph{single}-boundary non-handlebodies that we address in this paper have so far remained elusive. 

   

\begin{figure}
    \centering
    \tikzset{every picture/.style={line width=0.8pt}} 
    \tikzset{
pattern size/.store in=\mcSize, 
pattern size = 5pt,
pattern thickness/.store in=\mcThickness, 
pattern thickness = 0.3pt,
pattern radius/.store in=\mcRadius, 
pattern radius = 1pt}
\makeatletter
\pgfutil@ifundefined{pgf@pattern@name@_7jrft2iun}{
\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_7jrft2iun}
{\pgfqpoint{0pt}{0pt}}
{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
{\pgfpoint{\mcSize}{\mcSize}}
{
\pgfsetcolor{\tikz@pattern@color}
\pgfsetlinewidth{\mcThickness}
\pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
\pgfpathlineto{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
\pgfusepath{stroke}
}}
\makeatother


 
\tikzset{
pattern size/.store in=\mcSize, 
pattern size = 5pt,
pattern thickness/.store in=\mcThickness, 
pattern thickness = 0.3pt,
pattern radius/.store in=\mcRadius, 
pattern radius = 1pt}
\makeatletter
\pgfutil@ifundefined{pgf@pattern@name@_expa5zgm6}{
\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_expa5zgm6}
{\pgfqpoint{0pt}{0pt}}
{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
{\pgfpoint{\mcSize}{\mcSize}}
{
\pgfsetcolor{\tikz@pattern@color}
\pgfsetlinewidth{\mcThickness}
\pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
\pgfpathlineto{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
\pgfusepath{stroke}
}}
\makeatother


 
\tikzset{
pattern size/.store in=\mcSize, 
pattern size = 5pt,
pattern thickness/.store in=\mcThickness, 
pattern thickness = 0.3pt,
pattern radius/.store in=\mcRadius, 
pattern radius = 1pt}
\makeatletter
\pgfutil@ifundefined{pgf@pattern@name@_g54laaovo}{
\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_g54laaovo}
{\pgfqpoint{0pt}{0pt}}
{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
{\pgfpoint{\mcSize}{\mcSize}}
{
\pgfsetcolor{\tikz@pattern@color}
\pgfsetlinewidth{\mcThickness}
\pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
\pgfpathlineto{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
\pgfusepath{stroke}
}}
\makeatother


 
\tikzset{
pattern size/.store in=\mcSize, 
pattern size = 5pt,
pattern thickness/.store in=\mcThickness, 
pattern thickness = 0.3pt,
pattern radius/.store in=\mcRadius, 
pattern radius = 1pt}
\makeatletter
\pgfutil@ifundefined{pgf@pattern@name@_cc1njbb37}{
\pgfdeclarepatternformonly[\mcThickness,\mcSize]{_cc1njbb37}
{\pgfqpoint{0pt}{0pt}}
{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
{\pgfpoint{\mcSize}{\mcSize}}
{
\pgfsetcolor{\tikz@pattern@color}
\pgfsetlinewidth{\mcThickness}
\pgfpathmoveto{\pgfqpoint{0pt}{0pt}}
\pgfpathlineto{\pgfpoint{\mcSize+\mcThickness}{\mcSize+\mcThickness}}
\pgfusepath{stroke}
}}
\makeatother
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2]



\draw  [draw opacity=0][pattern=_7jrft2iun,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 155; green, 155; blue, 155}] (372.31,90.05) -- (412.48,90.05) -- (412.48,220.34) -- (372.31,220.34) -- cycle ;

\draw [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (370.26,89.76) .. controls (390.78,105.09) and (383.75,127.4) .. (396.06,137.19) .. controls (408.37,146.98) and (406.03,167.26) .. (395.18,175.77) .. controls (384.33,184.29) and (394.59,194.22) .. (372.31,220.34) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (193.34,175.39) -- (211.89,175.39) -- (211.89,164.11) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (202.43,175.39) -- (184.25,175.39) -- (184.25,164.11) ;


\draw   (139.17,175.01) -- (175.19,175.01) -- (175.19,163.99) ;

\draw   (126.19,170.25) -- (162.2,170.25) -- (162.2,164.24) ;

\draw   (256.86,175.26) -- (221.74,175.26) -- (221.74,164.24) ;

\draw   (270.34,170.5) -- (235.22,170.5) -- (235.22,164.49) ;


\draw  [draw opacity=0][line width=0.75]  (387.24,133.5) .. controls (396.22,137.39) and (402.47,146.09) .. (402.47,156.21) .. controls (402.47,166.5) and (395.99,175.34) .. (386.75,179.12) -- (376.69,156.21) -- cycle ; \draw  [line width=0.75]  (387.24,133.5) .. controls (396.22,137.39) and (402.47,146.09) .. (402.47,156.21) .. controls (402.47,166.5) and (395.99,175.34) .. (386.75,179.12) ;  

\draw  [draw opacity=0][line width=0.75]  (402.4,156.81) .. controls (401.43,161.02) and (390.29,164.33) .. (376.69,164.33) .. controls (362.45,164.33) and (350.91,160.7) .. (350.91,156.21) .. controls (350.91,156.18) and (350.91,156.15) .. (350.91,156.12) -- (376.69,156.21) -- cycle ; \draw  [line width=0.75]  (402.4,156.81) .. controls (401.43,161.02) and (390.29,164.33) .. (376.69,164.33) .. controls (362.45,164.33) and (350.91,160.7) .. (350.91,156.21) .. controls (350.91,156.18) and (350.91,156.15) .. (350.91,156.12) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=0.75]  (350.92,156.08) .. controls (351.27,151.69) and (362.68,148.17) .. (376.69,148.17) .. controls (390.73,148.17) and (402.15,151.7) .. (402.47,156.1) -- (376.69,156.29) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=0.75]  (350.92,156.08) .. controls (351.27,151.69) and (362.68,148.17) .. (376.69,148.17) .. controls (390.73,148.17) and (402.15,151.7) .. (402.47,156.1) ;  

\draw  [draw opacity=0][line width=1.5]  (387.45,134.88) .. controls (387.53,135.1) and (387.57,135.32) .. (387.57,135.55) .. controls (387.57,138) and (382.63,139.98) .. (376.54,139.98) .. controls (370.45,139.98) and (365.51,138) .. (365.51,135.55) .. controls (365.51,135.16) and (365.63,134.79) .. (365.86,134.43) -- (376.54,135.55) -- cycle ; \draw  [line width=1.5]  (387.45,134.88) .. controls (387.53,135.1) and (387.57,135.32) .. (387.57,135.55) .. controls (387.57,138) and (382.63,139.98) .. (376.54,139.98) .. controls (370.45,139.98) and (365.51,138) .. (365.51,135.55) .. controls (365.51,135.16) and (365.63,134.79) .. (365.86,134.43) ;  

\draw [line width=1.5]    (339.85,95.61) .. controls (362.43,107.11) and (365.25,123.61) .. (365.51,135.55) ;

\draw [line width=1.5]    (363.71,89.61) .. controls (379.36,99.36) and (386.03,116.86) .. (387.57,135.55) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (363.77,101.8) .. controls (376.77,115.13) and (374.49,125.61) .. (376.54,135.55) ;
\draw [shift={(376.54,135.55)}, rotate = 123.33] [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (365.52,135.32) .. controls (365.82,132.97) and (370.64,131.11) .. (376.54,131.11) .. controls (382.28,131.11) and (387,132.88) .. (387.52,135.13) -- (376.54,135.55) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (365.52,135.32) .. controls (365.82,132.97) and (370.64,131.11) .. (376.54,131.11) .. controls (382.28,131.11) and (387,132.88) .. (387.52,135.13) ;  

\draw  [draw opacity=0][line width=0.75]  (365.34,178.55) .. controls (356.79,174.5) and (350.91,166.02) .. (350.91,156.21) .. controls (350.91,146.12) and (357.13,137.44) .. (366.07,133.54) -- (376.69,156.21) -- cycle ; \draw  [line width=0.75]  (365.34,178.55) .. controls (356.79,174.5) and (350.91,166.02) .. (350.91,156.21) .. controls (350.91,146.12) and (357.13,137.44) .. (366.07,133.54) ;  

\draw  [draw opacity=0][line width=1.5]  (387.17,177.68) .. controls (387.25,177.46) and (387.3,177.24) .. (387.3,177.01) .. controls (387.3,174.57) and (382.36,172.58) .. (376.26,172.58) .. controls (370.17,172.58) and (365.23,174.57) .. (365.23,177.01) .. controls (365.23,177.31) and (365.31,177.6) .. (365.45,177.88) -- (376.26,177.01) -- cycle ; \draw  [line width=1.5]  (387.17,177.68) .. controls (387.25,177.46) and (387.3,177.24) .. (387.3,177.01) .. controls (387.3,174.57) and (382.36,172.58) .. (376.26,172.58) .. controls (370.17,172.58) and (365.23,174.57) .. (365.23,177.01) .. controls (365.23,177.31) and (365.31,177.6) .. (365.45,177.88) ;  

\draw [line width=1.5]    (339.58,216.85) .. controls (362.15,205.38) and (364.98,188.92) .. (365.23,177.01) ;

\draw [line width=1.5]    (363.44,222.83) .. controls (379.09,213.11) and (385.76,195.65) .. (387.3,177.01) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (366.95,206.33) .. controls (376.47,194.33) and (374.21,186.92) .. (376.26,177.01) ;
\draw [shift={(376.26,177.01)}, rotate = 326.7] [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (365.25,177.24) .. controls (365.54,179.58) and (370.36,181.44) .. (376.26,181.44) .. controls (382.01,181.44) and (386.73,179.67) .. (387.25,177.42) -- (376.26,177.01) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (365.25,177.24) .. controls (365.54,179.58) and (370.36,181.44) .. (376.26,181.44) .. controls (382.01,181.44) and (386.73,179.67) .. (387.25,177.42) ;  

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (355.29,93.93) .. controls (358.3,96.2) and (360.9,98.73) .. (363.77,101.8) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (366.95,206.33) .. controls (364.34,209.79) and (357.07,217.4) .. (353.37,219.4) ;

\draw [draw opacity=0][pattern=_expa5zgm6,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 155; green, 155; blue, 155}]   (337.72,98.9) .. controls (346.39,99) and (371.43,122.9) .. (357.95,135.19) .. controls (344.46,147.48) and (348.09,168.58) .. (358.86,176.58) .. controls (369.64,184.58) and (355.83,206.6) .. (335.08,215.76) ;

\draw  [draw opacity=0][pattern=_g54laaovo,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 155; green, 155; blue, 155}] (481.72,89.65) -- (440.39,89.65) -- (440.39,219.94) -- (481.72,219.94) -- cycle ;

\draw [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (483.83,89.36) .. controls (462.71,104.69) and (469.35,126.86) .. (457.28,136.79) .. controls (445.22,146.73) and (447.03,166.86) .. (458.19,175.37) .. controls (469.35,183.89) and (458.79,193.82) .. (481.72,219.94) ;

\draw  [draw opacity=0][line width=0.75]  (466.62,133) .. controls (457.24,136.83) and (450.68,145.6) .. (450.68,155.81) .. controls (450.68,166.19) and (457.47,175.09) .. (467.11,178.81) -- (477.21,155.81) -- cycle ; \draw  [line width=0.75]  (466.62,133) .. controls (457.24,136.83) and (450.68,145.6) .. (450.68,155.81) .. controls (450.68,166.19) and (457.47,175.09) .. (467.11,178.81) ;  

\draw  [draw opacity=0][line width=0.75]  (450.76,156.43) .. controls (451.79,160.63) and (463.24,163.93) .. (477.21,163.93) .. controls (491.86,163.93) and (503.73,160.3) .. (503.73,155.81) .. controls (503.73,155.78) and (503.73,155.75) .. (503.73,155.72) -- (477.21,155.81) -- cycle ; \draw  [line width=0.75]  (450.76,156.43) .. controls (451.79,160.63) and (463.24,163.93) .. (477.21,163.93) .. controls (491.86,163.93) and (503.73,160.3) .. (503.73,155.81) .. controls (503.73,155.78) and (503.73,155.75) .. (503.73,155.72) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=0.75]  (503.73,155.67) .. controls (503.35,151.29) and (491.62,147.77) .. (477.21,147.77) .. controls (462.77,147.77) and (451.03,151.3) .. (450.69,155.7) -- (477.21,155.89) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=0.75]  (503.73,155.67) .. controls (503.35,151.29) and (491.62,147.77) .. (477.21,147.77) .. controls (462.77,147.77) and (451.03,151.3) .. (450.69,155.7) ;  

\draw  [draw opacity=0][line width=1.5]  (466.15,134.46) .. controls (466.06,134.68) and (466.02,134.91) .. (466.02,135.15) .. controls (466.02,137.6) and (471.1,139.58) .. (477.37,139.58) .. controls (483.64,139.58) and (488.72,137.6) .. (488.72,135.15) .. controls (488.72,134.75) and (488.58,134.37) .. (488.34,134) -- (477.37,135.15) -- cycle ; \draw  [line width=1.5]  (466.15,134.46) .. controls (466.06,134.68) and (466.02,134.91) .. (466.02,135.15) .. controls (466.02,137.6) and (471.1,139.58) .. (477.37,139.58) .. controls (483.64,139.58) and (488.72,137.6) .. (488.72,135.15) .. controls (488.72,134.75) and (488.58,134.37) .. (488.34,134) ;  

\draw [line width=1.5]    (515.11,95.21) .. controls (491.88,106.71) and (488.98,123.21) .. (488.72,135.15) ;

\draw [line width=1.5]    (490.56,89.21) .. controls (474.46,98.96) and (467.6,116.46) .. (466.02,135.15) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (490.5,101.4) .. controls (477.13,114.73) and (479.48,125.21) .. (477.37,135.15) ;
\draw [shift={(477.37,135.15)}, rotate = 147] [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (488.7,134.91) .. controls (488.39,132.57) and (483.43,130.71) .. (477.37,130.71) .. controls (471.47,130.71) and (466.62,132.47) .. (466.07,134.72) -- (477.37,135.15) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (488.7,134.91) .. controls (488.39,132.57) and (483.43,130.71) .. (477.37,130.71) .. controls (471.47,130.71) and (466.62,132.47) .. (466.07,134.72) ;  

\draw  [draw opacity=0][line width=0.75]  (488.62,178.27) .. controls (497.56,174.27) and (503.73,165.72) .. (503.73,155.81) .. controls (503.73,145.63) and (497.22,136.88) .. (487.88,133.03) -- (477.21,155.81) -- cycle ; \draw  [line width=0.75]  (488.62,178.27) .. controls (497.56,174.27) and (503.73,165.72) .. (503.73,155.81) .. controls (503.73,145.63) and (497.22,136.88) .. (487.88,133.03) ;  

\draw  [draw opacity=0][line width=1.5]  (466.44,177.3) .. controls (466.35,177.07) and (466.3,176.84) .. (466.3,176.61) .. controls (466.3,174.17) and (471.38,172.18) .. (477.65,172.18) .. controls (483.92,172.18) and (489,174.17) .. (489,176.61) .. controls (489,176.92) and (488.92,177.22) .. (488.77,177.5) -- (477.65,176.61) -- cycle ; \draw  [line width=1.5]  (466.44,177.3) .. controls (466.35,177.07) and (466.3,176.84) .. (466.3,176.61) .. controls (466.3,174.17) and (471.38,172.18) .. (477.65,172.18) .. controls (483.92,172.18) and (489,174.17) .. (489,176.61) .. controls (489,176.92) and (488.92,177.22) .. (488.77,177.5) ;  

\draw [line width=1.5]    (515.39,216.45) .. controls (492.17,204.98) and (489.26,188.52) .. (489,176.61) ;

\draw [line width=1.5]    (490.85,222.43) .. controls (474.75,212.71) and (467.88,195.25) .. (466.3,176.61) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (487.23,205.93) .. controls (477.44,193.93) and (479.76,186.52) .. (477.65,176.61) ;
\draw [shift={(477.65,176.61)}, rotate = 302.98] [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (488.98,176.85) .. controls (488.67,179.18) and (483.71,181.04) .. (477.65,181.04) .. controls (471.75,181.04) and (466.9,179.28) .. (466.35,177.04) -- (477.65,176.61) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (488.98,176.85) .. controls (488.67,179.18) and (483.71,181.04) .. (477.65,181.04) .. controls (471.75,181.04) and (466.9,179.28) .. (466.35,177.04) ;  

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (499.23,93.53) .. controls (496.13,95.8) and (493.46,98.33) .. (490.5,101.4) ;

\draw [color={rgb, 255:red, 0; green, 14; blue, 255 }  ,draw opacity=1 ][line width=0.75]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (487.23,205.93) .. controls (489.91,209.39) and (497.04,217.8) .. (502.78,220.6) ;

\draw [draw opacity=0][pattern=_cc1njbb37,pattern size=6pt,pattern thickness=0.75pt,pattern radius=0pt, pattern color={rgb, 255:red, 155; green, 155; blue, 155}]   (517.31,98.5) .. controls (511.88,97.93) and (481.52,123.11) .. (495.39,135.4) .. controls (509.27,147.69) and (506.64,168.18) .. (495.55,176.18) .. controls (484.47,184.18) and (500.73,208.2) .. (520.02,215.36) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=2.25]    (387.14,151.24) .. controls (410.46,135.03) and (440.38,134.57) .. (465.59,151.74) ;
\draw [shift={(469.53,154.6)}, rotate = 217.63] [fill=wilsonred  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (11.43,-5.49) -- (0,0) -- (11.43,5.49) -- cycle    ;
\draw [shift={(382.93,154.4)}, rotate = 321.11] [fill=wilsonred  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (11.43,-5.49) -- (0,0) -- (11.43,5.49) -- cycle    ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (83.33,70) -- (550.5,70) -- (550.5,240) -- (83.33,240) -- cycle ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (303.7,70) -- (303.7,240) ;

\draw (338.36,78.33) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$P_{3}$};

\draw (497.73,79.23) node [anchor=north west][inner sep=0.75pt]  [font=\small]  {$P_{4}$};

\draw (119.88,137.9) node [anchor=north west][inner sep=0.75pt]  [font=\Large]  {$\cdots C_{i_{1}}{}_{i_{2}}{}_{i_{3}} C_{i_{4}}{}_{i_{5}}{}_{i_{6}} \cdots $};

\draw (90.02,219.5) node [anchor=north west][inner sep=0.75pt]   [align=left] {OPE index contractions (typicality)};

\draw (414.13,121.67) node [anchor=north west][inner sep=0.75pt]   [align=left] {\small glue};

\draw (380.71,222.5) node [anchor=north west][inner sep=0.75pt]   [align=left] {cylinder surgery};
\end{tikzpicture}
    \caption{In section \ref{sec:minimal completion}, we show that index contractions, in a statistical ensemble of heavy OPE coefficients, correspond to 3-manifold surgery where the gluing surface is a cylinder. Combining this surgery with crossing transformations generates many non-handlebodies.}
    \label{fig:machine1}
\end{figure}
\paragraph{Non-handlebodies from statistics.} In section \ref{sec:minimal completion}, we demonstrate that including non-handlebodies in the sum over topologies becomes necessary when, in addition to crossing symmetry, we require the ensemble of CFT$_2$ data to satisfy \emph{typicality}. This concept is familiar from the Eigenstate Thermalization Hypothesis \cite{Deutsch1991,Srednicki1994,Foini:2018sdb,Pappalardi:2022aaz,Jafferis:2022uhu} and can be generalized to chaotic 2d CFTs \cite{Belin:2021ryy, Belin:2021ibv, deBoer:2024mqg}, where it amounts to approximate local rotational invariance in microcanonical windows around primary states of high conformal dimension. Importantly, typicality predicts the structure of index contractions of random OPE coefficients, which in the bulk translates to precise \emph{surgery} operations on 3-manifolds, as illustrated in figure \ref{fig:machine1}. We show that iteratively applying these surgery moves and combining them with crossing transformations generates a large class of non-handlebody topologies. 

We will refer to this inductive procedure for generating topologies from properties of the statistical ensemble of CFT$_2$ data as the ``gravitational machine''. This machine takes as input any handlebody (or multiple handlebodies) and repeatedly acts on it with three basic surgery operations, which will be specified in section \ref{subsec:general gravitational machine}. The resulting set of 3-manifold topologies should be seen as the \emph{minimal} completion of the handlebody sum that is compatible with typicality, crossing symmetry and consistency between higher and lower statistical moments.\footnote{However, this is not the end of the story: in this paper, we focus on OPE statistics and ignore spectral correlations. The latter are expected to arise from off-shell topologies \cite{Cotler:2020ugk,Maxfield:2020ale, DiUbaldo:2023qli, Haehl:2023tkr,deBoer:2025rct,Boruch:2025ilr} that further correct the dictionary \eqref{eq:sumovertopologies}. We will have more to say on this in the \hyperref[sec:discussion]{discussion}.}

\begin{figure}
    \centering
    \tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1]


\draw  [draw opacity=0][line width=1.5]  (522.15,195.41) .. controls (518.36,200.1) and (512.45,203.11) .. (505.8,203.11) .. controls (499.36,203.11) and (493.59,200.27) .. (489.79,195.81) -- (505.8,183.11) -- cycle ; \draw  [line width=1.5]  (522.15,195.41) .. controls (518.36,200.1) and (512.45,203.11) .. (505.8,203.11) .. controls (499.36,203.11) and (493.59,200.27) .. (489.79,195.81) ;  

\draw    (363.36,138.32) .. controls (377.81,138.4) and (381.82,150.12) .. (381.63,157.87) .. controls (381.43,167.83) and (374.23,173.55) .. (374.29,181.3) .. controls (374.22,189.18) and (381.53,195.17) .. (381.58,204.74) .. controls (381.51,212.62) and (377.84,224.34) .. (363.27,224.26) .. controls (348.46,224.3) and (344.81,212.58) .. (345,204.7) .. controls (344.95,195.26) and (352.39,189.15) .. (352.34,181.27) .. controls (352.29,173.53) and (344.98,167.66) .. (345.05,157.83) .. controls (344.87,150.21) and (348.54,138.5) .. (363.36,138.32) -- cycle ;

\draw    (364.25,150.79) .. controls (360.44,154.02) and (359.81,164.07) .. (364.72,166.97) ;

\draw    (363.05,152.24) .. controls (366.6,157.82) and (365.98,161.17) .. (363.47,165.85) ;

\draw    (364.27,194.69) .. controls (360.46,197.93) and (359.83,207.97) .. (364.74,210.88) ;

\draw    (363.07,196.14) .. controls (366.62,201.72) and (366,205.07) .. (363.49,209.76) ;

\draw    (297.36,138.42) .. controls (311.81,138.5) and (315.82,150.22) .. (315.63,157.97) .. controls (315.44,167.93) and (308.24,173.65) .. (308.29,181.4) .. controls (308.23,189.28) and (315.54,195.28) .. (315.59,204.85) .. controls (315.52,212.72) and (311.85,224.44) .. (297.28,224.36) .. controls (282.46,224.4) and (278.82,212.68) .. (279.01,204.8) .. controls (278.96,195.36) and (286.4,189.25) .. (286.35,181.38) .. controls (286.29,173.63) and (278.98,167.76) .. (279.05,157.93) .. controls (278.88,150.31) and (282.55,138.6) .. (297.36,138.42) -- cycle ;

\draw    (298.26,150.89) .. controls (294.44,154.12) and (293.82,164.17) .. (298.73,167.07) ;

\draw    (297.06,152.34) .. controls (300.61,157.92) and (299.98,161.27) .. (297.47,165.95) ;

\draw    (298.28,194.79) .. controls (294.46,198.03) and (293.84,208.07) .. (298.75,210.98) ;

\draw    (297.08,196.24) .. controls (300.63,201.82) and (300,205.17) .. (297.5,209.86) ;

\draw    (304.43,139.57) .. controls (323.53,147.02) and (336.26,146.62) .. (354.51,140.18) ;

\draw    (303.39,223.55) .. controls (322.15,216.91) and (338.74,217.08) .. (353.74,222.11) ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (330.75,129) -- (329.69,235) ;

\draw [line width=1.5]    (174.48,217.23) .. controls (157.9,217.29) and (143.61,209.3) .. (141.12,184.15) .. controls (138.62,159) and (156.7,131.78) .. (177.12,147.23) ;

\draw [line width=1.5]    (174.08,177.19) .. controls (158.01,146.78) and (195.09,129.6) .. (212.69,153.74) .. controls (230.3,177.89) and (214.58,197.56) .. (213.75,203.76) .. controls (212.92,209.96) and (206.3,230.38) .. (189.33,228.31) .. controls (172.36,226.25) and (161.74,196.56) .. (180.11,187.38) ;

\draw [line width=1.5]    (188.56,184.93) .. controls (200.88,186.47) and (203.31,192.14) .. (210.36,182.13) .. controls (217.42,172.11) and (207.19,154.45) .. (195.41,152.04) .. controls (183.64,149.62) and (174.69,158.8) .. (179.94,172.77) ;

\draw [line width=1.5]    (185.28,153.54) .. controls (214.8,187.95) and (139.73,183.92) .. (157.92,201.21) ;

\draw [line width=1.5]    (179.52,160.18) .. controls (194.22,175.14) and (149.87,190.45) .. (150.22,179.51) .. controls (150.57,168.57) and (158.53,145.52) .. (172.03,155.14) ;

\draw [line width=1.5]    (183.79,179.5) .. controls (186.74,184.44) and (211.26,203.93) .. (185.68,214.66) ;

\draw [line width=1.5]    (177.05,183.4) .. controls (185.82,193.96) and (193.66,203.44) .. (181.54,205.62) ;

\draw [line width=1.5]    (157.92,201.21) .. controls (160.34,203.29) and (166.81,207.27) .. (170.98,207.11) ;

\draw [line width=1.5]    (185.56,194.69) .. controls (174.8,199.31) and (183.84,222.66) .. (194.73,216.99) ;

\draw [line width=1.5]    (195.22,194.4) .. controls (207.49,198.96) and (204.4,211.5) .. (194.73,216.99) ;

\draw    (461.37,182.88) .. controls (461.46,171.97) and (473.94,168.95) .. (482.2,169.09) .. controls (492.81,169.23) and (498.9,174.67) .. (507.15,174.63) .. controls (515.54,174.68) and (521.93,169.16) .. (532.13,169.12) .. controls (540.52,169.18) and (552.99,171.95) .. (552.91,182.94) .. controls (552.96,194.12) and (540.47,196.87) .. (532.08,196.73) .. controls (522.03,196.77) and (515.52,191.15) .. (507.13,191.19) .. controls (498.87,191.23) and (492.62,196.75) .. (482.15,196.7) .. controls (474.04,196.83) and (461.56,194.06) .. (461.37,182.88) -- cycle ;

\draw    (471.21,183.22) .. controls (473.63,178.56) and (484.52,175.89) .. (492.39,183) ;

\draw    (520.43,183) .. controls (522.85,178.33) and (536.18,175.65) .. (541.61,182.78) ;

\draw  [draw opacity=0][line width=1.5]  (485.3,186.08) .. controls (485.15,185.11) and (485.08,184.12) .. (485.08,183.11) .. controls (485.08,172.07) and (494.36,163.11) .. (505.8,163.11) .. controls (517.25,163.11) and (526.53,172.07) .. (526.53,183.11) .. controls (526.53,183.9) and (526.48,184.69) .. (526.39,185.46) -- (505.8,183.11) -- cycle ; \draw  [line width=1.5]  (485.3,186.08) .. controls (485.15,185.11) and (485.08,184.12) .. (485.08,183.11) .. controls (485.08,172.07) and (494.36,163.11) .. (505.8,163.11) .. controls (517.25,163.11) and (526.53,172.07) .. (526.53,183.11) .. controls (526.53,183.9) and (526.48,184.69) .. (526.39,185.46) ;  

\draw    (469.39,181.89) .. controls (472.62,187.67) and (490.37,189) .. (493.6,181.67) ;

\draw    (518.61,181.67) .. controls (521.84,187.44) and (539.59,188.78) .. (542.82,181.44) ;

\draw  [draw opacity=0][line width=1.5]  (501.1,173.48) .. controls (502.47,170.62) and (504.43,168.83) .. (506.61,168.83) .. controls (510.73,168.83) and (514.07,175.22) .. (514.07,183.11) .. controls (514.07,191) and (510.73,197.4) .. (506.61,197.4) .. controls (504.4,197.4) and (502.41,195.55) .. (501.05,192.62) -- (506.61,183.11) -- cycle ; \draw  [line width=1.5]  (501.1,173.48) .. controls (502.47,170.62) and (504.43,168.83) .. (506.61,168.83) .. controls (510.73,168.83) and (514.07,175.22) .. (514.07,183.11) .. controls (514.07,191) and (510.73,197.4) .. (506.61,197.4) .. controls (504.4,197.4) and (502.41,195.55) .. (501.05,192.62) ;  
\draw  [draw opacity=0][line width=1.5]  (469.04,194.74) .. controls (467.83,195.18) and (466.53,195.42) .. (465.18,195.42) .. controls (458.45,195.42) and (453,189.52) .. (453,182.25) .. controls (453,174.98) and (458.45,169.08) .. (465.18,169.08) .. controls (471.91,169.08) and (477.36,174.98) .. (477.36,182.25) .. controls (477.36,183.41) and (477.22,184.54) .. (476.96,185.62) -- (465.18,182.25) -- cycle ; \draw  [line width=1.5]  (469.04,194.74) .. controls (467.83,195.18) and (466.53,195.42) .. (465.18,195.42) .. controls (458.45,195.42) and (453,189.52) .. (453,182.25) .. controls (453,174.98) and (458.45,169.08) .. (465.18,169.08) .. controls (471.91,169.08) and (477.36,174.98) .. (477.36,182.25) .. controls (477.36,183.41) and (477.22,184.54) .. (476.96,185.62) ;  

\draw  [draw opacity=0][line width=1.5]  (535.54,185.18) .. controls (535.39,184.34) and (535.31,183.47) .. (535.31,182.58) .. controls (535.31,175.31) and (540.76,169.42) .. (547.49,169.42) .. controls (554.21,169.42) and (559.67,175.31) .. (559.67,182.58) .. controls (559.67,189.86) and (554.21,195.75) .. (547.49,195.75) .. controls (546.41,195.75) and (545.37,195.6) .. (544.37,195.32) -- (547.49,182.58) -- cycle ; \draw  [line width=1.5]  (535.54,185.18) .. controls (535.39,184.34) and (535.31,183.47) .. (535.31,182.58) .. controls (535.31,175.31) and (540.76,169.42) .. (547.49,169.42) .. controls (554.21,169.42) and (559.67,175.31) .. (559.67,182.58) .. controls (559.67,189.86) and (554.21,195.75) .. (547.49,195.75) .. controls (546.41,195.75) and (545.37,195.6) .. (544.37,195.32) ;  

\draw   (445.05,182.44) .. controls (445.05,148.51) and (472.56,121) .. (506.5,121) .. controls (540.44,121) and (567.95,148.51) .. (567.95,182.44) .. controls (567.95,216.38) and (540.44,243.89) .. (506.5,243.89) .. controls (472.56,243.89) and (445.05,216.38) .. (445.05,182.44) -- cycle ;

\draw   (119.28,182.3) .. controls (119.28,148.37) and (146.79,120.86) .. (180.72,120.86) .. controls (214.66,120.86) and (242.17,148.37) .. (242.17,182.3) .. controls (242.17,216.24) and (214.66,243.75) .. (180.72,243.75) .. controls (146.79,243.75) and (119.28,216.24) .. (119.28,182.3) -- cycle ;

\draw (386.32,169.05) node [anchor=north west][inner sep=0.75pt]  [font=\Large]  {$/\ \Phi $};

\draw (100.37,224) node [anchor=north west][inner sep=0.75pt]    {$a)$};

\draw (250.8,224) node [anchor=north west][inner sep=0.75pt]    {$b)$};

\draw (428.27,224) node [anchor=north west][inner sep=0.75pt]    {$c)$};

\draw (456.31,156.84) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$n_1$};

\draw (537.42,156.84) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$n_3$};

\draw (498.24,206.89) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$n_4$};

\draw (496.78,177.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$n_2$};

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (80.33,96.67) -- (596.33,96.67) -- (596.33,267.67) -- (80.33,267.67) -- cycle ;
\end{tikzpicture}
    \caption{Examples of non-handlebodies with genus-2 boundary. These non-handlebodies are all necessary in the sum over topologies, in order for the statistical description of the CFT to be consistent. $a)$ Complement of a handlebody-knot in $\mathrm{S}^3$. $b)$ Twisted $I$-bundle. $c)$ Dehn surgery on the complement of a handlebody embedded in $\mathrm{S}^3$. }
    \label{fig:nonhandlebodies}
\end{figure}
The main results of this paper are to study and rigorously prove certain appealing properties of the gravitational machine, which we summarize here:
\begin{itemize}
    \item \textbf{The machine generates non-handlebodies.} We will explicitly show that the examples illustrated in figure \ref{fig:nonhandlebodies} are generated by the machine. Moreover, we show that they are indeed non-handlebodies by analyzing their fundamental groups. As a simple class of examples of non-handlebodies, we similarly analyze all genus-2 handlebody-knots with fewer than 6 crossings (see table \ref{table:handlebodyknots}). More generally, the machine applies for arbitrary genus $g\geq 2$ of the boundary manifold and also works for disconnected boundaries. 
    \item \textbf{The machine is hyperbolic.} In section \ref{subsec:machine is hyperbolic}, we prove that starting from any hyperbolic 3-manifold, the action of the gravitational machine only produces 3-manifolds that are also hyperbolic. The proof follows from studying how the fundamental group changes under the operations of the machine, making use of Thurston's hyperbolization theorem \cite{Thurston:1982} and geometric group theory. This key result makes precise the intuition that OPE statistics in the boundary description only requires on-shell saddles in the bulk. 
    \item \textbf{But not all hyperbolic non-handlebodies are generated.} This is perhaps the most interesting outcome of our analysis: in section \ref{subsec:what 3-manifolds are generated}, we show that all manifolds generated by the machine are so-called \emph{cylindrical} 3-manifolds, which contain embedded essential cylinders. However, there are many topologies that are not cylindrical; as an example of a hyperbolic, acylindrical manifold with genus-2 boundary, we study Thurston's so-called `tripus' manifold \cite{thurston_book}. We will discuss the implications of this fact for the sum over topologies below.
\end{itemize}

Throughout the paper, we demonstrate that the above results, which are mostly about topology rather than gravity, can be implemented directly on the level of the gravitational path integral by using Virasoro TQFT \cite{Collier:2023fwi}. This formalism gives the exact quantum gravity partition (i.e.~at finite $c$), topology by topology, so we do not rely on semiclassical arguments. Virasoro TQFT also allows us to straightforwardly extend our results to 3-manifolds with conical defects: for example, when $\Sigma = \Sigma_{0,4}$ is the 4-punctured sphere, the analogue of the handlebody sum is the `conformal block Farey tale' of \cite{Maloney:2016kee} and the analogue of a non-handlebody is a non-rational tangle. 


\paragraph{Is 3d gravity non-minimal?}
Let us end this introduction by contemplating what the above results imply for 3d gravity and the sum over topologies. Although we have managed to find a boundary interpretation for a large class of non-handlebodies, there are still infinitely many on-shell manifolds not generated by our gravitational machine. The main source of such counterexamples are the \emph{acylindrical} 3-manifolds described in the third point above, which can be characterized by admitting a finite-volume hyperbolic metric with totally geodesic boundary \cite{Thurston1986HyperbolicI}. Apparently, these topologies are not strictly necessary in order for the statistical ensemble to obey crossing and typicality, leaving the intriguing possibility that the full sum over topologies in 3d gravity is not a minimal solution of the statistical bootstrap. 

In fact, it seems perfectly consistent to take any on-shell and acylindrical `seed', consider its orbit under the action of the machine, and decide to add this orbit to the sum over topologies or not. This gives an infinite number of choices, signaling a large redundancy in the possible consistent statistical descriptions for 3d gravity. This seems contrary to our expectation that pure 3d gravity would, in some sense, be the simplest theory satisfying the statistical bootstrap.

We could turn this question around and instead ask: What are the minimal properties imposed on a statistical ensemble of CFT$_2$ data that uniquely select 3d gravity, including the full sum over topologies? It is logically possible that adding conditions \emph{beyond} those we have imposed (such as a version of the moment problem \cite{Janssen:2021stl}, the existence of a matrix-tensor model \cite{Belin:2023efa, Jafferis:2025vyp}, or the presence of random matrix universality in the CFT spectrum \cite{Perlmutter:2025ngj}) requires more topologies for these additional conditions to be satisfied. We come back to this important open question in the discussion.


\paragraph{Plan of the paper.}
In section \ref{sec:2}, we will define the conditions that any statistical theory of CFT$_2$ data dual to pure 3d gravity must satisfy. Then, in section \ref{sec:3} we show that the condition of crossing symmetry (at all genera) is solved by summing over handlebodies, explaining in particular the relation to non-Gaussianities in the statistics of OPE coefficients. Although this is mainly a review, it sets up a lot of the formalism that will be needed in the following sections. In section \ref{sec:minimal completion}, we show how the condition of typicality, combined with crossing and consistency conditions between higher and lower moments, leads to non-handlebodies in the bulk. The gravitational machine is introduced as a way to systematize these non-handlebody contributions, and its main properties are proven. In section \ref{sec:5}, we apply the machine to produce a variety of examples of non-handlebodies, and compute their partition functions. We end with a discussion and an outlook for future work. Finally, in the appendices we have collected many technical results about 3-manifolds, their fundamental groups, and Virasoro TQFT that are needed in the main text.
