---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-013-4-conclusions
section_title: "Conclusions"
section_number: 4
pages: 39-41
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
text_source: latex
latex_prose_ratio: 0.849
latex_coverage_ratio: 1.0
---
\label{sec-conclude}
In this paper we have identified an infinite family of asymptotic power series arising naturally in topological string theory, 
by considering the conifold free energies and ``quantizing" the flat coordinates. We have argued that these series are the analogues of conventional perturbative expansions in the coupling constant in finite rank gauge theories. 
We have conjectured that the resurgent structure of these series are encoded in ``peacock patterns", namely, infinite towers of singularities 
in the Borel plane with {\it integer} Stokes constants. The latter can then be regarded as new integer invariants of Calabi--Yau threefolds. 
We have verified our conjecture in various non-trivial toric examples by using the TS/ST correspondence. Thanks to this correspondence, 
the asymptotic series are promoted to spectral traces, which turn out to satisfy a factorization property into (anti)holomorphic blocks. This makes it possible to calculate the Stokes data in a very efficient way, and in some cases one obtains closed expressions for the Stokes constant as coefficients of explicit $q$-series. The resulting mathematical structure is very similar to the one found in complex CS theory. 

Our results raise many questions, both technical and conceptual. Let us list some open problems and further directions to explore. 

In our construction, it is crucial to enlarge the original perturbative series to a more general 
set of trans-series, in what we have called a minimal resurgent structure. It would be important to 
have a better understanding of the trans-series obtained in this way. In particular, it would be interesting 
to clarify whether they correspond to the conifold expansion of the general trans-series constructed in \cite{cesv1,cesv2}. More generally, we would like to have a more physical understanding of these trans-series, either in geometric terms (e.g. as contributions of D-brane sectors in the CY threefold) or in terms of a dual, quantum-mechanical description. 

In this paper we have explored the conventional topological string theory side of the TS/ST correspondence, but one could also consider the semi-classical limit of the spectral traces $\hbar \rightarrow 0$. This is the dual story to what we analyzed here, since it involves an $S$-duality transformation of the string coupling constant, and it should make contact with the NS limit of the topological string. 

We have also focused on the toric case for computational reasons, but as emphasized in section \ref{sec-definition}, 
our framework is very general and in particular it applies to 
compact CY examples, like e.g. the quintic CY. One can in principle use the genus expansion of topological string theory (as obtained in \cite{hk-quintic}) to extract perturbative series around the conifold point, and then study their Borel structure and Stokes constants. Although the existing data are probably not enough to perform a precise resurgent analysis, the point of view advocated in this paper might unveil 
new integrality structures in the compact case and shed light on the all-genus structure of topological string theory. 



In our study, we have focused on the ``numerical" series appearing after setting $\lambda_i=-N_i g_s$. As we explained,  
this leads to a simpler problem in the theory of resurgence, involving Gevrey-1 series with no parametric dependence 
(besides the ``easy" one due to mass parameters). It is however natural to include the full dependence on the CY moduli. 
To do this, one could take as a starting point the full perturbative series of conifold free energies, 
$\CF_g(\blambda)$, $g=0,1, \cdots$, and study 
the minimal resurgent structure associated to it, together with its Stokes constants. Some preliminary steps in 
that direction were taken in \cite{cms}, 
where additional trans-series were obtained with the techniques of \cite{cesv1,cesv2}, and used to reconstruct the fermionic spectral trace 
$Z_{\bN}(\hbar)$ for arbitrary $\bN$. There are many indications that, for each value of $\blambda$, the following formal series in $g_s$,

\be
\label{zcon}
Z(\blambda;g_s)= \exp \left( \sum_{g \ge 0} \CF_g(\blambda) g_s^{2g-2} \right),
\ee

will lead to peacock patterns, involving infinite towers of singularities in the Borel plane of $g_s$ 
(these towers are visible in the figures of \cite{cms}, and in the simpler case of the resolved conifold they have been studied in \cite{ps09}). 
It would be very interesting to understand these patterns and the resulting Stokes constants. Many questions arise naturally: 
Do the Stokes data depend on $\blambda$? Do they satisfy integrality properties? It is also likely that the Stokes constants 
obtained in this way (or by considering the similar problem for the NS free energies) 
are related to the counting of BPS invariants in the CY threefold. This more general framework might lead to a better understanding of the 
enumerative meaning of the Stokes constants calculated in this work.  

One could also consider, instead of the conifold free energies, the more conventional large radius free energies, 
and to study the Stokes constants for this different perturbative series. In the toric case, the TS/ST correspondence asserts that this series is the asymptotic expansion of the spectral determinant (\ref{spec-det}) in an appropriate scaling limit. It is also an 
open problem to ``decode" this spectral determinant in terms of the Borel resummation of an appropriate set of trans-series at large radius. 

The similarities with complex CS theory underlined in this work also suggest many questions: what is the $q$-difference 
equation satisfied by the spectral determinant $\Xi_X$? Is it 
possible to write $\Xi_X$ in terms of moduli-dependent, holomorphic blocks, similar to what was done in \cite{bdp,ggm2}? The answers 
to these questions would shed new light on the structures appearing in the TS/ST correspondence, which are not yet fully understood. 




\section{Acknowledgements}
We would like to thank Jorgen Andersen, Tom Bridgeland, Bertrand Eynard, Rinat Kashaev, 
Maxim Kontsevich and Greg Moore for useful 
comments. We are specially grateful to Stavros Garoufalidis for many discussions on 
these topics and for collaboration 
in a related project. We also thank Claudia Rella for a detailed reading of the manuscript. 
This work has been supported in part by the Fonds National Suisse, 
subsidy 200020-175539, by the NCCR 51NF40-182902 ``The Mathematics of Physics'' (SwissMAP), 
and by the ERC-SyG project 
``Recursive and Exact New Quantum Theory" (ReNewQuantum), which 
received funding from the European Research Council (ERC) under the European 
Union's Horizon 2020 research and innovation program, 
grant agreement No. 810573.
