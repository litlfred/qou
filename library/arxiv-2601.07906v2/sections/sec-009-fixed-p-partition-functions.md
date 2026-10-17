---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-009-fixed-p-partition-functions
section_title: "Fixed-P partition functions"
section_number: null
pages: 27-34
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.997
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:fixedP}
Instead of working with the `canonical' partition functions, with fixed values of the complex structure moduli at the asymptotic boundary, in Virasoro TQFT it is useful to define the corresponding `fixed-$P$' partition function $Z^{\,\mathcal{C}}_{\text{Vir}}[M;\boldsymbol{P}]$. We define it by stripping off the non-degenerate blocks and including a normalization factor:
\begin{equation}\label{eq:fixed_P}
    Z_{\text{Vir}}[M;\Omega] = \int_0^\infty \d^{3g-3} P \,\rho^{\,\mathcal{C}}_g(\boldsymbol{P}) \,Z^{\,\mathcal{C}}_{\text{Vir}}[M;\boldsymbol{P}] \,\mathcal{F}_g^{\,\mathcal{C}}(\boldsymbol{P};\Omega).
\end{equation}
This equation is analogous to the gluing of trumpets to fixed-length partition functions (i.e.~Weil-Petersson volumes) in JT-gravity \cite{Saad:2018bqo}.
Let us explain the notation used. 
First, the integral in \eqref{eq:fixed_P} is only over the heavy part of the spectrum, which we parametrized by the Liouville momenta $\boldsymbol{P}$ as before. In other words, we have expanded in a basis of non-degenerate conformal blocks in the channel $\mathcal{C}$. (This heavy channel should not be confused with the identity channel that defined the contractible cycles of the handlebodies discussed above.) 

Second, the normalization factor is defined as:
\begin{equation}
    \rho^{\,\mathcal{C}}_g(\boldsymbol{P}) = \prod_{e_a\in \Gamma_{\mathcal{C}}}\rho_0(P_a)\prod_{v_{ijk}\in\Gamma_{\mathcal{C}}}C_0(P_i,P_j,P_k).
\end{equation}
The product is over all edges and vertices of the dual graph $\Gamma_{\mathcal{C}}$, with known functions $\rho_0$ and $C_0$ that are related to the modular S-kernel and fusion kernel (see App.~\ref{app:technology}). This normalization appears in the inner product on the space of conformal blocks derived in \cite{Collier:2023fwi} and will be convenient later. Indeed, one may interpret \eqref{eq:fixed_P} as the resolution of the identity in the VTQFT Hilbert space associated to the genus-$g$ boundary, which implements the change of basis from fixed-moduli to fixed-$P$:
\begin{equation}
    \braket{\Omega|Z_\text{Vir}(M)} = \int_0^\infty \d^{3g-3}P\,  \rho^{\,\mathcal{C}}_g(\boldsymbol{P}) \braket{\mathcal{F}^{\,\mathcal{C}}_g(\boldsymbol{P})|Z_\text{Vir}(M)} \braket{\Omega|\mathcal{F}^{\,\mathcal{C}}_g(\boldsymbol{P})}\,.
\end{equation}
 
 Concretely, in the case that $M$ is a handlebody $M^\gamma$, labeled by some crossing transformation $\gamma$, the fixed-$P$ partition function can be read off from  \eqref{eq:identitykernel} to be:
\begin{equation}\label{eq:def_fixedP}
    Z_{\text{Vir}}^{\,\mathcal{C}}[M^{\gamma};\boldsymbol{P}] = \frac{1}{\rho^{\,\mathcal{C}}_g(\boldsymbol{P})} \,\mathbb{K}^\gamma_{\mathds{1}\boldsymbol{P}}\,.
\end{equation}
Plugging this into \eqref{eq:fixed_P}, we see that the corresponding identity channel is  
$
    \gamma\cdot \mathcal{C}.
$ We stress that the choice of $\mathcal{C}$ is arbitrary once we sum over all $\gamma$'s in section \ref{sec:3.3}. In practice, we will choose the basis $\mathcal{C}$ to be `simple’, in the sense that the dual graph $\Gamma_{\mathcal{C}}$ has the minimal number crossings. At genus 2 and 3, this will be one of the planar graphs in equations \eqref{eq:genus2graphs} and \eqref{eq:genus3graphs}.\footnote{However, at genus 4 and higher there are contraction patterns that cannot be made planar: an example is the contraction in equation (3.46) of \cite{Collier:2024mgv}. That is why we define $\mathcal{C}$ by requiring the minimal number of crossings of $\Gamma_{\mathcal{C}}$. These simple bases are in 1-1 correspondence with the distinct contraction patterns of OPE coefficients introduced in section \ref{sec:2}. } With respect to this simple choice of basis $\mathcal{C}$, the complexity of the handlebody $M^\gamma$ is visualized by a VTQFT diagram, which represents the \emph{embedding} of $\Gamma_{\mathcal{C}}$ in a closed 3-manifold, as we will explain below. 

Again, an example will clarify the above formalism. At genus 2, consider the crossing transformation $\gamma = \mathbb{S}\circ \mathbb{S}\circ \mathbb{F}$, where one S-kernel acts on the left dumbbell and the other on the right.  
The corresponding dual graph $\Gamma_{\mathcal{C}}$ is the sunset diagram. Using the definition \eqref{eq:def_fixedP}, its fixed-$P$ partition function evaluates to: 
\begin{align}\label{eq:theta graph ZVir}
    Z_{\rm Vir}\!\left[\!\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.7,xscale=0.7]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.15,0) {\footnotesize $P_1$};
        \node at (0.31,0) {\footnotesize $P_2$};
        \node at (1.15,0) {\footnotesize $P_3$};
    \end{tikzpicture}
    }}\!\right] &= \frac{\mathbb{S}_{\mathds{1}P_1}[\mathds{1}]\,\mathbb{S}_{\mathds{1}P_3}[\mathds{1}]\,\fker{\mathds{1}}{P_2}{P_3}{P_1}{P_1}{P_3}}{\rho_0(P_1)\rho_0(P_2)\rho_0(P_3)C_0(P_1,P_2,P_3)C_0(P_1,P_2,P_3)} \\
    &= \frac{1}{C_0(P_1,P_2,P_3)}\, .
\end{align}
In the second line, we used that $\rho_0(P) = \mathbb{S}_{\mathds{1}P}[\mathds{1}]$, as well as the relation:
\begin{equation}
    \fker{\mathds{1}}{P_2}{P_3}{P_1}{P_1}{P_3} = \rho_0(P_2)C_0(P_1,P_2,P_3).
\end{equation}
Now we can find the corresponding identity channel by acting with $\gamma$ on the sunset diagram. Doing so, we see that the identity channel $\gamma\cdot\mathcal{C}$ is the dumbbell channel:
\begin{multline}
    \int_0^\infty \d^3 P\, \sker{\mathds{1}}{P_1}{\mathds{1}}\,\sker{\mathds{1}}{P_3}{\mathds{1}} \,\fker{\mathds{1}}{P_2}{P_3}{P_1}{P_1}{P_3}\mathcal{F}^{\,\mathcal{C}}_{g=2}\!\left[\!\!\vcenter{\hbox{\begin{tikzpicture}[scale=.7]
    \draw[very thick] (0,1) to[out=180,in=180,looseness=2] (0,-1) to[out=0,in=180] (1,-0.75) to[out=0,in=180] (2,-1) to[out=0,in=0,looseness=2] (2,1) to[out=180, in =0] (1,.75) to[out=180,in=0] (0,1);
    \draw[very thick, out=180, in=180, looseness=2] (0, 1) to (0,-1);
    \draw[very thick, out=0, in = 180] (0,1) to (1,0.75) to (2, 1);
    \draw[very thick, out = 0, in=180] (0,-1) to (1,-0.75) to (2,-1);
    \draw[very thick, out=0, in=0,looseness=2] (2,1) to (2,-1);
    \draw[very thick, bend right=30] (-1/2,0+.06) to (1/2, 0+.06);
    \draw[very thick, bend right=30] (2-1/2,0+.06) to (2+1/2, 0+.06);
    \draw[very thick, bend left = 30] (-1/3,-.08+.06) to (+1/3,-.08+.06);
    \draw[very thick, bend left = 30] (2-1/3,-.08+.06) to (2+1/3,-.08+.06);
    \draw[very thick, wilsonred, out=180, in=180, looseness=6] (1,-.5) to (1,.5);
    \draw[very thick, wilsonred] (1,-.5) to node[right, black, shift={(-.1,0)}] {\footnotesize $P_2$} (1,.5);
    \draw[very thick, wilsonred, out=0, in=0, looseness=6] (1,-.5) to (1,.5);
    \node at (0,.7) {\footnotesize $P_1$};
    \node at (2,.7) {\footnotesize $P_3$};
    \end{tikzpicture}}}\!\!\right] \\[0.2em]
    = \mathcal{F}_{g=2}^{\,\gamma\cdot\mathcal{C}}\!\left[\!\!\vcenter{\hbox{\begin{tikzpicture}[scale=.7]
    \draw[very thick] (0,1) to[out=180,in=180,looseness=2] (0,-1) to[out=0,in=180] (1,-0.75) to[out=0,in=180] (2,-1) to[out=0,in=0,looseness=2] (2,1) to[out=180, in =0] (1,.75) to[out=180,in=0] (0,1);
    \draw[very thick, out=180, in=180, looseness=2] (0, 1) to (0,-1);
    \draw[very thick, out=0, in = 180] (0,1) to (1,0.75) to (2, 1);
    \draw[very thick, out = 0, in=180] (0,-1) to (1,-0.75) to (2,-1);
    \draw[very thick, out=0, in=0,looseness=2] (2,1) to (2,-1);
    \draw[very thick, bend right=30] (-1/2,0+.06) to (1/2, 0+.06);
    \draw[very thick, bend right=30] (2-1/2,0+.06) to (2+1/2, 0+.06);
    \draw[very thick, bend left = 30] (-1/3,-.08+.06) to (+1/3,-.08+.06);
    \draw[very thick, bend left = 30] (2-1/3,-.08+.06) to (2+1/3,-.08+.06);
    \draw[very thick, wilsonred] (.6,0) to node[below, black] {$\mathds{1}$} (1.4,0);
    \draw[very thick, wilsonred, bend left=40] (.6,0) to (-1.17,0);
    \draw[very thick, wilsonred, dashed, bend right=40] (0,.1) to (-1.17,0);
    \draw[very thick, wilsonred, bend right=50] (.6,0) to node[above, black] {$\mathds{1}$} (0,.1);
     \draw[very thick, wilsonred, bend left=40] (3.1,0) to (1.4,0);
    \draw[very thick, wilsonred, dashed, bend right=40] (3.1,0) to (2,0.1);
    \draw[very thick, wilsonred, bend right=50] (2,0.1) to node[above, black] {$\mathds{1}$} (1.4,0);
    \end{tikzpicture}}}\!\!\right]\,,
\end{multline}
where the `bells' (sub-tori) are in the S-dual channel. The contribution of this handlebody to the statistical moment is just the universal density studied in \cite{Chandra:2022bqq}:
\begin{equation}\label{eq:C0 contribution}
    \overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \supset |\rho_0(h_1)\rho(h_2)\rho_0(h_3)C_0(h_1,h_2,h_3)|^2.
\end{equation}
As before, we used the notation $\supset$ to indicate that the left-hand side is given by a full sum over topologies, and the right-hand side is only one term in that sum. We also used the notation $|\cdot |^2$ as a shorthand for the product of left- and right-moving contributions, as in equation \eqref{eq:grav_to_VTQFT}. Furthermore, we used the shorthand $\rho_i \equiv \rho(h_i,\bar h_i)$ and changed variables from Liouville momenta back to conformal weights $h_i$.

As a second slightly more involved example, consider 
the crossing transformation $\gamma$ that was illustrated in \eqref{eq:sequence1}. Additionally, we add two S-moves acting on the bells of the dumbbell. So the total mapping class is:
\begin{equation}\label{eq:crossingtrans}
    \gamma = \mathbb{S}\circ \mathbb{S}\circ \mathbb{F}\circ \mathbb{B}^2\circ \mathbb{F} \ ,
\end{equation}
where the two S-kernels act on the two dumbbells and $\mathbb{F} \circ \mathbb{B}^2 \circ \mathbb{F}$ only acts on the centrally embedded 4-punctured sphere.
The associated VTQFT graph is the linked dumbbell channel, where the two bells have been linked as in \eqref{eq:sequence1}. We can find the fixed-$P$ partition function associated to this handlebody by representing \eqref{eq:crossingtrans} by its genus-2 crossing kernel:
\begin{equation}
    \mathbb{K}^\gamma_{\mathds{1}P_1P_2P_3} = \sker{\mathds{1}}{P_1}{\mathds{1}}\,\sker{\mathds{1}}{P_2}{\mathds{1}}\int_0^\infty \d P \,\fker{\mathds{1}}{P}{P_2}{P_1}{P_1}{P_2}\,\left(\mathbb{B}^P_{P_1P_2}\right)^2\,\fker{P}{P_3}{P_1}{P_1}{P_2}{P_2}\,.
\end{equation}
Using the expression for the braiding phase \eqref{eq:appbraid}, we note that this kernel is precisely equal to the Dehn twist representation \eqref{eq:dehntwistkernel}, and indeed $\gamma$ defines the same mapping class as \eqref{eq:dehntwistmappingclass}. Furthermore,
we note that the $P$-integral can be expressed in terms of the one-point S-kernel by using the integral identity \eqref{eq:Shat and 6j}. Dividing by the normalization factor $\rho_{g=2}^{\mathcal{C}}$, we thus obtain:
\begin{align}
Z_{\text{Vir}}\left[
    \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.4,xscale=1.4,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) -- (255.9,122.49) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) ;  

\draw  [draw opacity=0] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) -- (278.29,122.76) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (255.9,122.49) -- (278.29,122.76) ;

\draw (235,118.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (286.4,118.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};

\draw (259.41,122.68) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};
\end{tikzpicture}\right] &= \frac{\mathbb{K}^\gamma_{\mathds{1}P_1P_2P_3}}{\rho_0(P_1)\rho_0(P_2)\rho_0(P_3)C_0(P_1,P_1,P_3)C_0(P_2,P_2,P_3)} \\ 
&= \frac{\sker{P_1}{P_2}{P_3}}{\rho_0(P_2)C_0(P_2,P_2,P_3)} = \frac{1}{\sqrt{\mathsf{C}_{113}\mathsf{C}_{223}}} \,\skerhat{P_1}{P_2}{P_3}\,.\label{eq:Z_linkedhandcuff} 
\end{align}
In the last equality we rewrote the fixed-$P$ partition function in terms of the symmetric S-kernel, cf.~\eqref{eq:Shat_def}, in the so-called Racah-Wigner normalization \cite{Post:2024itb}. The prefactors are useful shorthands for the $C_0$ function:
\begin{equation}
    \mathsf{C}_{ijk} \equiv C_0(P_i,P_j,P_k)\, .
\end{equation}
In this example, $\mathcal{C}$ is the dumbbell channel, and we have represented the non-trivial topology of the handlebody $M^\gamma$ by the VTQFT diagram where the bells are linked. To find the corresponding identity channel $\gamma\cdot\mathcal{C}$, we follow the sequence of moves in \eqref{eq:sequence1} and apply the additional S-moves. The resulting identity channel is also the linked dumbbell diagram:
\begin{equation}\label{eq:identitylinkeddumbbell}
    \int_0^\infty \d^3 P \,\mathbb{K}^\gamma_{\mathds{1}P_1P_2P_3}\,\mathcal{F}_{g=2}^{\,\mathcal{C}}\left[\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [color=wilsonred  ,draw opacity=1 ] (114.8,134.74) .. controls (114.8,126.23) and (121.72,119.34) .. (130.25,119.34) .. controls (138.78,119.34) and (145.69,126.23) .. (145.69,134.74) .. controls (145.69,143.25) and (138.78,150.14) .. (130.25,150.14) .. controls (121.72,150.14) and (114.8,143.25) .. (114.8,134.74) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ] (183.07,134.74) .. controls (183.07,126.23) and (189.99,119.34) .. (198.52,119.34) .. controls (207.05,119.34) and (213.96,126.23) .. (213.96,134.74) .. controls (213.96,143.25) and (207.05,150.14) .. (198.52,150.14) .. controls (189.99,150.14) and (183.07,143.25) .. (183.07,134.74) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ]   (145.69,134.74) -- (183.07,134.74) ;

\draw (122.1,121.99) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (190.96,121.99) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};

\draw (157.24,118.96) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};
\end{tikzpicture}\right] = \mathcal{F}^{\,\gamma\cdot\mathcal{C}}_{g=2}\!\left[\!\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) -- (255.9,122.49) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (263.34,142.94) .. controls (261.02,143.77) and (258.51,144.23) .. (255.9,144.23) .. controls (243.81,144.23) and (234,134.5) .. (234,122.49) .. controls (234,110.48) and (243.81,100.75) .. (255.9,100.75) .. controls (267.99,100.75) and (277.8,110.48) .. (277.8,122.49) .. controls (277.8,128.87) and (275.02,134.62) .. (270.61,138.59) ;  

\draw  [draw opacity=0] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) -- (278.29,122.76) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (270.78,102.33) .. controls (273.13,101.48) and (275.65,101.02) .. (278.29,101.02) .. controls (290.39,101.02) and (300.19,110.75) .. (300.19,122.76) .. controls (300.19,134.77) and (290.39,144.5) .. (278.29,144.5) .. controls (266.2,144.5) and (256.4,134.77) .. (256.4,122.76) .. controls (256.4,117.02) and (258.64,111.79) .. (262.3,107.91) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (255.9,122.49) -- (278.29,122.76) ;

\draw (235,116.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (288.4,116.06) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (261.41,123.68) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\mathds{1}$};

\draw (299.43,102.83) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (230.57,102.54) node [anchor=north west][inner sep=0.75pt]    {$'$};
\end{tikzpicture}\!\right]\,.
\end{equation}
Here we used the prime $'$ to indicate that the bells are now in the S-dual channel.

The linked dumbbell in \eqref{eq:Z_linkedhandcuff} has a counterpart where the over-under crossings of the bells are reversed \cite{Hartman:2025cyj}. Their VTQFT partition functions differ by a complex conjugation, which leads to a phase $\skerhat{P_1}{P_2}{P_3}^* = \e^{-i\pi h_3}\skerhat{P_1}{P_2}{P_3}$. The sum of these two distinct handlebodies projects onto even spin $J_3$, compatible with the permutation property \eqref{eq:OPEpermutation}, and contributes as the following non-Gaussian moment:
\begin{equation}\label{eq:cherryOPE}
\overline{\rho_1\rho_2\rho_3C_{113}C_{223}} \supset 
(1+(-1)^{J_3}) \left| \rho_0(h_1)\rho_0(h_2)\rho_0(h_3)
\sqrt{\mathsf{C}_{113}\mathsf{C}_{223}}\,
\skerhat{h_1}{h_2}{h_3}
\right|^2. 
\end{equation}
As an aside, we note that the linked dumbbell diagram is also known as the `knotted handcuff' in the literature \cite{Hartman:2025cyj,Hartman:2025ula}, and it is often depicted as such: 
\begin{equation}
\label{eq:cherry}
\vcenter{
\hbox{
\begin{tikzpicture}
\begin{scope}[rotate=-90, xscale = 0.6, yscale=0.55]
\draw[very thick, wilsonred]
(-0.25,-1.45) to[out=0, in=0,looseness = 1.5]
(-0.25,1.65) to[out=180, in = 0]
(-0.53, 1.65) to[out = 180, in =90]
(-1.9, 0.74) to[out=270, in =225]
(-0.83, 0.05);
\draw[very thick, wilsonred]
(-0.68, 0.25) to[out = 55, in = -90]
(-0.53, 1.65);
\draw[very thick, wilsonred]
(-0.53,-1.45) to[out = 90, in =35, looseness=1.5] 
(-1.55,0.2);
\draw[very thick, wilsonred]
(-1.72,0.05) to[out=235, in = 90]
(-1.9, -0. 57) to[out=270, in =180]
(-0.25,-1.45);
\end{scope}
\end{tikzpicture}
}
}.
\end{equation}

As a third and last example of a more complicated handlebody, we study a diagram that is in the mapping class group orbit of the sunset diagram. We can obtain it from the linked dumbbell by acting with a braiding and a fusion move:
\begin{equation}
    \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.5,xscale=1.5,baseline={([yshift=-0.5ex]current bounding box.center)}]

\draw [line width=1.5]    (164.17,99.87) -- (191.5,99.87) ;
\draw [shift={(195.5,99.87)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.97,-3.35) -- (0,0) -- (6.97,3.35) -- cycle    ;

\draw [line width=1.5]    (265.53,100.2) -- (292.87,100.2) ;
\draw [shift={(296.87,100.2)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.97,-3.35) -- (0,0) -- (6.97,3.35) -- cycle    ;

\draw  [draw opacity=0] (145.38,94.11) .. controls (141.98,98.87) and (136.45,101.97) .. (130.22,101.97) .. controls (119.88,101.97) and (111.51,93.47) .. (111.51,82.98) .. controls (111.51,72.49) and (119.88,63.99) .. (130.22,63.99) .. controls (140.55,63.99) and (148.92,72.49) .. (148.92,82.98) .. controls (148.92,84.43) and (148.77,85.84) .. (148.46,87.2) -- (130.22,82.98) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (145.38,94.11) .. controls (141.98,98.87) and (136.45,101.97) .. (130.22,101.97) .. controls (119.88,101.97) and (111.51,93.47) .. (111.51,82.98) .. controls (111.51,72.49) and (119.88,63.99) .. (130.22,63.99) .. controls (140.55,63.99) and (148.92,72.49) .. (148.92,82.98) .. controls (148.92,84.43) and (148.77,85.84) .. (148.46,87.2) ;  

\draw  [draw opacity=0] (115.47,88) .. controls (119.18,84.31) and (124.31,82.02) .. (129.98,82.02) .. controls (141.31,82.02) and (150.5,91.15) .. (150.5,102.4) .. controls (150.5,113.66) and (141.31,122.78) .. (129.98,122.78) .. controls (118.65,122.78) and (109.47,113.66) .. (109.47,102.4) .. controls (109.47,99.55) and (110.06,96.83) .. (111.13,94.36) -- (129.98,102.4) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (115.47,88) .. controls (119.18,84.31) and (124.31,82.02) .. (129.98,82.02) .. controls (141.31,82.02) and (150.5,91.15) .. (150.5,102.4) .. controls (150.5,113.66) and (141.31,122.78) .. (129.98,122.78) .. controls (118.65,122.78) and (109.47,113.66) .. (109.47,102.4) .. controls (109.47,99.55) and (110.06,96.83) .. (111.13,94.36) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (129.98,102.4) -- (129.92,122.58) ;

\draw  [draw opacity=0] (214.18,83.82) .. controls (214.27,73.59) and (222.34,65.33) .. (232.3,65.33) .. controls (242.3,65.33) and (250.42,73.68) .. (250.42,83.99) .. controls (250.42,85.2) and (250.3,86.39) .. (250.09,87.53) -- (232.3,83.99) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (214.18,83.82) .. controls (214.27,73.59) and (222.34,65.33) .. (232.3,65.33) .. controls (242.3,65.33) and (250.42,73.68) .. (250.42,83.99) .. controls (250.42,85.2) and (250.3,86.39) .. (250.09,87.53) ;  

\draw  [draw opacity=0] (219.57,86.72) .. controls (223.2,84.19) and (227.7,82.69) .. (232.57,82.69) .. controls (244.59,82.69) and (254.33,91.81) .. (254.33,103.07) .. controls (254.33,114.32) and (244.59,123.45) .. (232.57,123.45) .. controls (220.55,123.45) and (210.8,114.32) .. (210.8,103.07) .. controls (210.8,99.55) and (211.76,96.24) .. (213.43,93.36) -- (232.57,103.07) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (219.57,86.72) .. controls (223.2,84.19) and (227.7,82.69) .. (232.57,82.69) .. controls (244.59,82.69) and (254.33,91.81) .. (254.33,103.07) .. controls (254.33,114.32) and (244.59,123.45) .. (232.57,123.45) .. controls (220.55,123.45) and (210.8,114.32) .. (210.8,103.07) .. controls (210.8,99.55) and (211.76,96.24) .. (213.43,93.36) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (232.64,107.57) -- (232.58,123.25) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (214.18,83.47) .. controls (214.21,95.57) and (226.85,98.62) .. (230.36,99.43) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (236.54,101.69) .. controls (240.97,103.98) and (237.93,106.29) .. (232.64,107.57) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (232.64,107.57) .. controls (216.21,101.57) and (243.85,101.24) .. (247.42,92.67) ;

\draw  [draw opacity=0] (327.18,86.33) .. controls (330.15,85.5) and (333.37,85.05) .. (336.75,85.05) .. controls (351.25,85.05) and (363,93.4) .. (363,103.69) .. controls (363,113.99) and (351.25,122.33) .. (336.75,122.33) .. controls (322.25,122.33) and (310.5,113.99) .. (310.5,103.69) .. controls (310.5,97.5) and (314.75,92.01) .. (321.3,88.62) -- (336.75,103.69) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (327.18,86.33) .. controls (330.15,85.5) and (333.37,85.05) .. (336.75,85.05) .. controls (351.25,85.05) and (363,93.4) .. (363,103.69) .. controls (363,113.99) and (351.25,122.33) .. (336.75,122.33) .. controls (322.25,122.33) and (310.5,113.99) .. (310.5,103.69) .. controls (310.5,97.5) and (314.75,92.01) .. (321.3,88.62) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (313.26,111.35) .. controls (323.73,110.17) and (345.84,99.96) .. (347.88,91.72) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (332.17,99.57) .. controls (316.75,87.01) and (325.48,67) .. (335.95,67) .. controls (346.42,67) and (350.78,76.81) .. (349.62,84.27) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (339.73,105.07) .. controls (344.33,108.67) and (353.11,109.78) .. (360.38,111.35) ;
\draw (174.17,85.1) node [anchor=north west][inner sep=0.75pt]    {$\mathbb{B}^{-1}$};

\draw (273.2,85.1) node [anchor=north west][inner sep=0.75pt]    {$\mathbb{F}$};
\end{tikzpicture}\,.\vspace{1mm}
\end{equation}
The right-hand side indeed has the same graph type as the sunset in \eqref{eq:theta graph ZVir}, but one of the edges `loops' around one of the other edges. We can also view this diagram as a particular fragmentation of the trefoil knot, in the sense of \cite{Chandra:2025fef}. The associated genus-2 handlebody has a fixed-$P$ partition function that we compute as before: first, we write down the crossing kernel $\mathbb{K}^\gamma$ that represents $\gamma = \mathbb{S}\circ \mathbb{S}\circ \mathbb{F}\circ \mathbb{B}^2\circ \mathbb{F} \circ \mathbb{B}^{-1} \circ \mathbb{F}$, and then we divide by the sunset normalization factor. This gives:
\begin{equation}
    Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0] (350.19,107.95) .. controls (353.46,107.13) and (357,106.68) .. (360.69,106.68) .. controls (377.37,106.68) and (390.89,115.78) .. (390.89,127.01) .. controls (390.89,138.23) and (377.37,147.33) .. (360.69,147.33) .. controls (344.02,147.33) and (330.5,138.23) .. (330.5,127.01) .. controls (330.5,120.07) and (335.66,113.95) .. (343.54,110.28) -- (360.69,127.01) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (350.19,107.95) .. controls (353.46,107.13) and (357,106.68) .. (360.69,106.68) .. controls (377.37,106.68) and (390.89,115.78) .. (390.89,127.01) .. controls (390.89,138.23) and (377.37,147.33) .. (360.69,147.33) .. controls (344.02,147.33) and (330.5,138.23) .. (330.5,127.01) .. controls (330.5,120.07) and (335.66,113.95) .. (343.54,110.28) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (333.68,135.35) .. controls (345.72,134.07) and (371.15,122.94) .. (373.49,113.96) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (355.43,122.52) .. controls (337.69,108.82) and (347.73,87) .. (359.77,87) .. controls (371.82,87) and (376.84,97.7) .. (375.5,105.83) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (364.12,128.51) .. controls (369.42,132.43) and (379.51,133.64) .. (387.88,135.35) ;

\draw (318.89,110.07) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (354.56,134.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};

\draw (377.89,88.73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};
\end{tikzpicture}\,\,\,\right] = \frac{1}{\mathsf{C}_{123}}\int_0^\infty \d P \, \rho_0(P)\,\skerhat{P_1}{P_2}{P}\,\mathbb{B}_{P}^{P_2P_2} \sixj{P_1}{P_2}{P_3}{P_2}{P_1}{P} .
\end{equation}
Here $\mathbb{B}_P^{P_2P_2}$ is the complex conjugate of the braiding phase $\mathbb{B}^P_{P_2P_2}$, and we have expressed the fusion kernel in terms of the Virasoro $6j$ symbol using the relation \eqref{eq: relation btw fusion and modular kernels}. In this example, $\mathcal{C}$ is the sunset channel, and acting on it with $\gamma$ one can show that the corresponding identity channel $\gamma\cdot\mathcal{C}$ is again a linked dumbbell as in \eqref{eq:identitylinkeddumbbell}, with the only difference that now one bell is in the S-dual channel and one bell is acted on by $\mathbb{S}\mathbb{T}$. Multiplying by the normalization factor and taking the absolute value square as in \eqref{eq:grav_to_VTQFT}, this handlebody is also a contribution to the statistical moment $\overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*}$.

From the above examples, we see that the fixed-$P$ VTQFT partition functions are fully expressed in terms of crossing kernels only. We stress that, contrary to conformal blocks, these kernels are known analytically as integrals over known special functions \cite{Eberhardt:2023mrq}. Although the integrals may be hard to compute in general, they could in principle be evaluated numerically, for any value of $c$. What's more, since we stripped off the conformal blocks, the fixed-$P$ partition functions are what actually contribute to OPE statistics.


\paragraph{Geometric interpretation of the fixed-$P$ partition function.} There are several ways to interpret the VTQFT diagrams that appear in the fixed-$P$ partition functions calculated above. First, one can view the fixed-$P$ VTQFT graph as being embedded in the 3-sphere $\mathrm{S}^3$, and obtain a 3-manifold with boundary by taking the \emph{complement} of a regular neighborhood of the graph. Here is a pictorial example:
\begin{equation}\label{eq:loopedtheta}
    \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][line width=6]  (378.52,134.27) .. controls (382.82,133.3) and (387.44,132.78) .. (392.25,132.78) .. controls (415.07,132.78) and (433.57,144.6) .. (433.57,159.17) .. controls (433.57,173.75) and (415.07,185.57) .. (392.25,185.57) .. controls (369.43,185.57) and (350.93,173.75) .. (350.93,159.17) .. controls (350.93,150.22) and (357.91,142.3) .. (368.59,137.53) -- (392.25,159.17) -- cycle ; \draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]  (378.52,134.27) .. controls (382.82,133.3) and (387.44,132.78) .. (392.25,132.78) .. controls (415.07,132.78) and (433.57,144.6) .. (433.57,159.17) .. controls (433.57,173.75) and (415.07,185.57) .. (392.25,185.57) .. controls (369.43,185.57) and (350.93,173.75) .. (350.93,159.17) .. controls (350.93,150.22) and (357.91,142.3) .. (368.59,137.53) ;  

\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]    (354.86,170.14) .. controls (371.34,168.48) and (406.56,153.9) .. (409.76,142.22) ;

\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]    (385.04,153.34) .. controls (360.77,135.56) and (374.51,107.21) .. (390.99,107.21) .. controls (407.47,107.21) and (414.34,121.11) .. (412.51,131.67) ;

\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]    (396.91,161.17) .. controls (404.16,166.27) and (417.92,167.79) .. (429.36,170.01) ;

\draw  [draw opacity=0] (379.7,134.1) .. controls (383.56,133.34) and (387.65,132.93) .. (391.89,132.93) .. controls (414.72,132.93) and (433.22,144.75) .. (433.22,159.33) .. controls (433.22,173.91) and (414.72,185.73) .. (391.89,185.73) .. controls (369.07,185.73) and (350.57,173.91) .. (350.57,159.33) .. controls (350.57,150.28) and (357.71,142.29) .. (368.59,137.53) -- (391.89,159.33) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (379.7,134.1) .. controls (383.56,133.34) and (387.65,132.93) .. (391.89,132.93) .. controls (414.72,132.93) and (433.22,144.75) .. (433.22,159.33) .. controls (433.22,173.91) and (414.72,185.73) .. (391.89,185.73) .. controls (369.07,185.73) and (350.57,173.91) .. (350.57,159.33) .. controls (350.57,150.28) and (357.71,142.29) .. (368.59,137.53) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (354.43,169.93) .. controls (370.91,168.26) and (406.13,153.68) .. (409.33,142.01) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (385.04,153.34) .. controls (360.77,135.56) and (374.08,107) .. (390.56,107) .. controls (407.05,107) and (413.91,120.89) .. (412.08,131.45) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (396.91,161.17) .. controls (404.16,166.27) and (418,167.79) .. (429.45,170.01) ;

\draw  [draw opacity=0] (429.04,151.46) .. controls (428.68,151.34) and (428.38,151.14) .. (428.18,150.84) .. controls (427.55,149.9) and (428.19,148.37) .. (429.6,147.42) .. controls (431.02,146.48) and (432.68,146.48) .. (433.31,147.42) .. controls (433.51,147.72) and (433.58,148.07) .. (433.54,148.45) -- (430.74,149.13) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (429.04,151.46) .. controls (428.68,151.34) and (428.38,151.14) .. (428.18,150.84) .. controls (427.55,149.9) and (428.19,148.37) .. (429.6,147.42) .. controls (431.02,146.48) and (432.68,146.48) .. (433.31,147.42) .. controls (433.51,147.72) and (433.58,148.07) .. (433.54,148.45) ;  

\draw  [draw opacity=0] (393.04,109.93) .. controls (392.72,110.14) and (392.37,110.24) .. (392.02,110.2) .. controls (390.89,110.08) and (390.12,108.61) .. (390.3,106.92) .. controls (390.48,105.22) and (391.54,103.95) .. (392.67,104.07) .. controls (393.02,104.1) and (393.34,104.28) .. (393.61,104.55) -- (392.34,107.13) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (393.04,109.93) .. controls (392.72,110.14) and (392.37,110.24) .. (392.02,110.2) .. controls (390.89,110.08) and (390.12,108.61) .. (390.3,106.92) .. controls (390.48,105.22) and (391.54,103.95) .. (392.67,104.07) .. controls (393.02,104.1) and (393.34,104.28) .. (393.61,104.55) ;  

\draw  [draw opacity=0] (394.59,188.22) .. controls (394.3,188.46) and (393.97,188.61) .. (393.61,188.62) .. controls (392.47,188.64) and (391.52,187.28) .. (391.49,185.58) .. controls (391.45,183.87) and (392.34,182.47) .. (393.48,182.45) .. controls (393.84,182.44) and (394.17,182.57) .. (394.47,182.81) -- (393.54,185.53) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (394.59,188.22) .. controls (394.3,188.46) and (393.97,188.61) .. (393.61,188.62) .. controls (392.47,188.64) and (391.52,187.28) .. (391.49,185.58) .. controls (391.45,183.87) and (392.34,182.47) .. (393.48,182.45) .. controls (393.84,182.44) and (394.17,182.57) .. (394.47,182.81) ;  

\draw   (333.17,147.42) .. controls (333.17,114.6) and (359.77,88) .. (392.58,88) .. controls (425.4,88) and (452,114.6) .. (452,147.42) .. controls (452,180.23) and (425.4,206.83) .. (392.58,206.83) .. controls (359.77,206.83) and (333.17,180.23) .. (333.17,147.42) -- cycle ;

\draw (324.27,101.8) node [anchor=north west][inner sep=0.75pt]    {$S^{3}$};
\end{tikzpicture}\,.
\end{equation}
This is similar to the construction of a knot complement, but instead of embedding a link (thickened into a union of solid tori), we have embedded a trivalent graph (i.e.~a network of Wilson lines). If this graph is connected, the boundary of the graph complement is a genus-$g$ surface. The cycles in $\mathcal{C}$ are now non-contractible cycles in the ambient 3-manifold, for complicated enough $\gamma$. 

More generally, instead of $\mathrm{S}^3$ we could use any other closed 3-manifold as our embedding manifold. For example, our notation of the prime in \eqref{eq:identitylinkeddumbbell} to indicate an S-transform should really be thought of as an embedding of the dumbbell graph in $\mathrm{S}^2\times \mathrm{S}^1$ (or connected sums thereof, for multiple S-transforms). We will come back to this point when we discuss Dehn surgery in section \ref{sec:3.3}. 

Geometrically, viewing the fixed-$P$ diagrams as graph complements can be understood using the theory of \emph{pleated surfaces}. Namely, for a handlebody $M^\gamma$ the complete hyperbolic metric is always of infinite volume, and `flares out' to the conformal boundary \cite{Schlenker:2022dyo}. $M^\gamma$ does not support any smooth finite-volume hyperbolic metrics with totally geodesic boundary. However, we can put a finite-volume hyperbolic metric on $M^\gamma$ if we allow the geometry to end on a boundary surface that is pleated. This means that the boundary surface has vanishing extrinsic curvature everywhere except along a collection of geodesics, where the surface is allowed to have corners. As explained in \cite{Hartman:2025ula}, the fixed-$P$ partition function can be understood geometrically as the AdS$_3$ gravitational path integral with precisely such a boundary condition, in which the fixed Liouville momenta $P_i$ are related to the lengths $\ell_i$ of the geodesics around which the pleated surface bends by the formula
$
    \ell_i = 4\pi b P_i.
$\footnote{Here $b$ is the Liouville coupling, which parametrizes the central charge as $c = 1+ 6(b+1/b)^2$.}

We remark that such a geometric interpretation does not always exist, for a number of `simple’ handlebodies. This happens if a closed curve $C_i$ dual to an edge $P_i$ bounds a compressible disk in the graph complement. An example is given by the complement of the dumbbell graph, in which the middle cycle can be contracted in the ambient $\mathrm{S}^3$:
\begin{equation}\label{eq:contractible dumbbell}
\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.1,xscale=1.1,baseline={([yshift=-0.5ex]current bounding box.center)}]

\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]  (368.59,169.97) .. controls (368.59,162.71) and (374.06,156.83) .. (380.81,156.83) .. controls (387.56,156.83) and (393.03,162.71) .. (393.03,169.97) .. controls (393.03,177.23) and (387.56,183.11) .. (380.81,183.11) .. controls (374.06,183.11) and (368.59,177.23) .. (368.59,169.97) -- cycle ;

\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]  (422.61,169.97) .. controls (422.61,162.71) and (428.09,156.83) .. (434.84,156.83) .. controls (441.59,156.83) and (447.06,162.71) .. (447.06,169.97) .. controls (447.06,177.23) and (441.59,183.11) .. (434.84,183.11) .. controls (428.09,183.11) and (422.61,177.23) .. (422.61,169.97) -- cycle ;

\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][line width=6]    (393.03,169.97) -- (422.61,169.97) ;

\draw  [color=wilsonred  ,draw opacity=1 ] (368.4,169.97) .. controls (368.4,162.71) and (373.87,156.83) .. (380.62,156.83) .. controls (387.37,156.83) and (392.85,162.71) .. (392.85,169.97) .. controls (392.85,177.23) and (387.37,183.11) .. (380.62,183.11) .. controls (373.87,183.11) and (368.4,177.23) .. (368.4,169.97) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ] (422.43,169.97) .. controls (422.43,162.71) and (427.9,156.83) .. (434.65,156.83) .. controls (441.4,156.83) and (446.87,162.71) .. (446.87,169.97) .. controls (446.87,177.23) and (441.4,183.11) .. (434.65,183.11) .. controls (427.9,183.11) and (422.43,177.23) .. (422.43,169.97) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ]   (392.85,169.97) -- (422.43,169.97) ;

\draw  [draw opacity=0] (410.6,174.07) .. controls (410.15,174.54) and (409.63,174.8) .. (409.09,174.76) .. controls (407.59,174.68) and (406.49,172.45) .. (406.62,169.79) .. controls (406.75,167.12) and (408.06,165.03) .. (409.56,165.12) .. controls (410.1,165.15) and (410.6,165.46) .. (411,165.98) -- (409.32,169.94) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (410.6,174.07) .. controls (410.15,174.54) and (409.63,174.8) .. (409.09,174.76) .. controls (407.59,174.68) and (406.49,172.45) .. (406.62,169.79) .. controls (406.75,167.12) and (408.06,165.03) .. (409.56,165.12) .. controls (410.1,165.15) and (410.6,165.46) .. (411,165.98) ;  

\draw  [draw opacity=0] (381.54,160.45) .. controls (381.14,160.76) and (380.69,160.91) .. (380.23,160.86) .. controls (378.85,160.7) and (377.9,158.77) .. (378.12,156.54) .. controls (378.34,154.32) and (379.64,152.64) .. (381.02,152.8) .. controls (381.48,152.85) and (381.89,153.1) .. (382.23,153.49) -- (380.62,156.83) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (381.54,160.45) .. controls (381.14,160.76) and (380.69,160.91) .. (380.23,160.86) .. controls (378.85,160.7) and (377.9,158.77) .. (378.12,156.54) .. controls (378.34,154.32) and (379.64,152.64) .. (381.02,152.8) .. controls (381.48,152.85) and (381.89,153.1) .. (382.23,153.49) ;  

\draw  [draw opacity=0] (435.57,160.45) .. controls (435.16,160.76) and (434.71,160.91) .. (434.25,160.86) .. controls (432.87,160.7) and (431.93,158.77) .. (432.15,156.54) .. controls (432.37,154.32) and (433.67,152.64) .. (435.05,152.8) .. controls (435.51,152.85) and (435.92,153.1) .. (436.26,153.49) -- (434.65,156.83) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (435.57,160.45) .. controls (435.16,160.76) and (434.71,160.91) .. (434.25,160.86) .. controls (432.87,160.7) and (431.93,158.77) .. (432.15,156.54) .. controls (432.37,154.32) and (433.67,152.64) .. (435.05,152.8) .. controls (435.51,152.85) and (435.92,153.1) .. (436.26,153.49) ;  

\draw    (410.11,159.91) .. controls (423.58,135.17) and (448.53,139.21) .. (459.66,159.43) ;
\draw [shift={(460.97,162.04)}, rotate = 245.26] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (457.59,170.93) .. controls (457.59,167.69) and (459.27,165.07) .. (461.35,165.07) .. controls (463.43,165.07) and (465.11,167.69) .. (465.11,170.93) .. controls (465.11,174.17) and (463.43,176.8) .. (461.35,176.8) .. controls (459.27,176.8) and (457.59,174.17) .. (457.59,170.93) -- cycle ;

\draw   (352.6,170.13) .. controls (352.6,137.32) and (379.2,110.71) .. (412.01,110.71) .. controls (444.83,110.71) and (471.43,137.32) .. (471.43,170.13) .. controls (471.43,202.95) and (444.83,229.55) .. (412.01,229.55) .. controls (379.2,229.55) and (352.6,202.95) .. (352.6,170.13) -- cycle ;

\draw (359.14,179.83) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize]  {$P_{1}$};

\draw (443.14,179.54) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize]  {$P_{2}$};

\draw (402.86,179.26) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize]  {$P_{3}$};

\draw (343.7,124.51) node [anchor=north west][inner sep=0.75pt]    {$S^{3}$};
\end{tikzpicture}\,.
\end{equation}
This is reflected by the fact that the VTQFT partition function has support only on the identity for the weight $P_3$:\footnote{Here $\mathds{1}$ means $P_3 = \frac{iQ}{2}$, which is equivalent to the real delta function setting $h_3 = 0$.} 
\begin{equation}
Z_{\text{Vir}}\!\left[\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [color=wilsonred  ,draw opacity=1 ] (114.8,134.74) .. controls (114.8,126.23) and (121.72,119.34) .. (130.25,119.34) .. controls (138.78,119.34) and (145.69,126.23) .. (145.69,134.74) .. controls (145.69,143.25) and (138.78,150.14) .. (130.25,150.14) .. controls (121.72,150.14) and (114.8,143.25) .. (114.8,134.74) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ] (183.07,134.74) .. controls (183.07,126.23) and (189.99,119.34) .. (198.52,119.34) .. controls (207.05,119.34) and (213.96,126.23) .. (213.96,134.74) .. controls (213.96,143.25) and (207.05,150.14) .. (198.52,150.14) .. controls (189.99,150.14) and (183.07,143.25) .. (183.07,134.74) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ]   (145.69,134.74) -- (183.07,134.74) ;

\draw (122.1,121.99) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{1}$};

\draw (190.96,121.99) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{2}$};

\draw (157.24,118.96) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{3}$};
\end{tikzpicture}\right] = \frac{\delta(P_3 - \mathds{1})}{\rho_0(P_3)C_0(P_1,P_1,P_3)C_0(P_2,P_2,P_3)}\,.
\end{equation}
Since this is a distribution, it clearly does not have an interpretation as a classical saddlepoint to a fixed-length path integral. For a more complicated handlebody, like the \emph{linked} dumbbell \eqref{eq:Z_linkedhandcuff}, the $P_3$ cycle is non-contractible, and indeed in that case the fixed-length path integral exists and was analyzed directly in gravity in \cite{Hartman:2025ula}. More generally, if the mapping class $\gamma$ that defines the handlebody is complicated enough (technically, a sufficient condition is that $\gamma$ is ``pseudo-Anosov'' \cite{Thurston:1988}), then the fixed-length path integral exists, and the above geometric understanding of the fixed-$P$ partition function makes sense.

\paragraph{Fixed-$P$ partition functions, wormholes, and OPE statistics.}
The fixed-$P$ partition functions that have been the subject of this subsection straightforwardly encode the moments of structure constants in the dual statistical ensemble of CFT data.
The precise relation is made transparent by noting that there is a second geometric interpretation of the VTQFT Wilson line diagrams: as Euclidean wormhole geometries with boundaries that are thrice-punctured spheres. That is, instead of excising a regular neighborhood of the full graph embedded in $\mathrm{S}^3$, we only excise a spherical neighborhood around each vertex. In replacing trivalent vertices by 3-punctured spheres, we normalize each boundary component with a factor of $C_0$:
\begin{equation}\label{eq:vertex replacement rule}
    \vcenter{\hbox{
        \begin{tikzpicture}[scale=0.75]
            \draw[very thick,wilsonred] (0,0) to (0,1);
            \draw[very thick,wilsonred] (0,0) to (-.866,-.5);
            \draw[very thick,wilsonred] (0,0) to (.866,-0.5);
            \node[above] at (0,1) {$P_1$};
            \node[left] at (-.866,-.7) {$P_2$};
            \node[right] at (.866,-0.7) {$P_3$};
        \end{tikzpicture}
    }}
    = \,\,\frac{1}{\mathsf{C}_{123}}
    \vcenter{\hbox{
    \begin{tikzpicture}[scale=0.75]
        \draw[very thick] (0,0) circle (3/4);
        \draw[very thick] (-3/4,0) to[out=-90,in=-90,looseness=.8] (3/4,0);
        \draw[thick,densely dashed] (-3/4,0) to[out=90,in=90,looseness=.8] (3/4,0);
        \draw[very thick,wilsonred] (0,1/2) to (0,1);
        \draw[very thick, wilsonred] (-.433,-.25) to (-.866,-.5); 
        \draw[very thick, wilsonred] (.433,-.25) to (.866,-.5); 
        \node[above] at (0,1) {$P_1$};
        \node[left] at (-.866,-.7) {$P_2$};
        \node[right] at (.866,-0.7) {$P_3$};
    \end{tikzpicture}
    }}\, .
\end{equation} 
This turns our trivalent graph into a Euclidean wormhole with 3-punctured
sphere boundaries and a (possibly knotted) network of Wilson lines in the bulk, where the bulk Wilson lines have fixed holonomies parametrized by $P_i$. 

When the conformal weight $h_i$ is in the conical defect regime (defined e.g. in \cite{Benjamin:2020mfz}), the Wilson line has a semiclassical interpretation as creating a conical defect in the bulk geometry. As an example, we see that the sunset graph is equivalent to the Maldacena-Maoz wormhole:
\begin{equation}\label{eq:theta graph MM wormhole}
    \vcenter{\hbox{
    \begin{tikzpicture}[scale=0.9]
        \draw[very thick, wilsonred] (0,0) circle (1);
        \draw[very thick, wilsonred] (-1,0) to (1,0);
        \node[above] at (0,1) {$1$};
        \node[above] at (0,0) {$2$};
        \node[above] at (0,-1) {$3$};
        \node[below,white] at (0,-1) {$0$};
    \end{tikzpicture}
    }}
    \,\,\Leftrightarrow\,\,
    \vcenter{\hbox{
    \begin{tikzpicture}[scale=0.9]
        \draw[thick, densely dashed] (-3,0) to[out=90,in=90,looseness=.8] (-1,0); 
        \draw[thick, densely dashed] (1,0) to[out=90,in=90,looseness=.8] (3,0);
        \draw[very thick] (-2,0) ellipse (1 and 1);
        \draw[very thick] (-3,0) to[out=-90,in=-90,looseness=.8] (-1,0);
        \draw[very thick] (2,0) ellipse (1 and 1);
        \draw[very thick] (1,0) to[out=-90,in=-90,looseness=.8] (3,0);
        \draw[very thick, out = 330, in = 210] ({-2+cos(60)},{sin(60)}) to ({{2+cos(120)}},{sin(120)});
        \draw[very thick, out = 30, in = 150] ({-2+cos(-60)},{sin(-60)}) to ({{2+cos(240)}},{sin(240)});
        \draw[very thick, wilsonred, out = 330, in = 210] ({-2+4/5*cos(60)},{4/5*sin(60)}) to ({{2+4/5*cos(120)}},{4/5*sin(120)});
        \draw[very thick, wilsonred, out = 30, in = 150] ({-2+4/5*cos(-60)},{4/5*sin(-60)}) to ({{2+4/5*cos(240)}},{4/5*sin(240)});
        \draw[very thick, wilsonred] (-2+4/5,0) to (2-4/5,0);
        \draw[fill=gray,opacity=.5] ({-2+cos(60)},{sin(60)}) to[out = 330, in = 210] ({{2+cos(120)}},{sin(120)}) to[out=210, in = 150,looseness=1.2] ({{2+cos(240)}},{sin(240)}) to[out=150, in =30] ({{-2+cos(-60)}},{sin(-60)}) to[out=30,in=330,looseness=1.2] ({{-2+cos(60)}},{sin(60)});
        \node[left] at ({-2+4/5*cos(60)},{4/5*sin(60)}) {$1$};
        \node[left] at ({-2+4/5},{0}) {$2$};
        \node[left] at ({-2+4/5*cos(-60)},{4/5*sin(-60)}) {$3$};
        \node[right] at ({2+4/5*cos(120)},{4/5*sin(120)}) {$1$};
        \node[right] at ({2-4/5},{0}) {$2$};
        \node[right] at ({2+4/5*cos(240)},{4/5*sin(240)}) {$3$};
    \end{tikzpicture}
    }}\, .
\end{equation}
This was also the perspective taken in section 3.3 of \cite{Collier:2024mgv}. The two perspectives on the fixed-$P$  partition functions are both useful to keep in mind. They interpolate between each other by taking the conformal weights of the Wilson lines above the black hole threshold, in which case the boundary of the graph complement becomes a connected Riemann surface \cite{Chandra:2022bqq}. We then effectively `trade’ the Wilson lines for tunnels.\footnote{See also \cite{Abajian:2023bqv} for a geometric description of the Euclidean wormholes in the heavy regime.} Likewise, the geometric interpretation of the conformal blocks that we integrate against is that of `trumpets’, or flares, which trade the fixed momentum labels $\boldsymbol{P}$ for complex structure moduli $\Omega$ at the conformal boundary.

Thus in order to extract the statistics of the structure constants in the boundary ensemble it is sufficient to consider trivalent networks of Wilson lines in VTQFT. While these are most naturally associated with contributions to the gravitational path integral with a single genus-$g$ boundary, they are also straightforwardly related to multi-boundary sphere 3-point wormholes which more directly encode the OPE statistics without the additional baggage of conformal blocks. 
To extract the contributions to the OPE statistics from the VTQFT Wilson line configurations we simply replace the trivalent vertices with 3-punctured spheres via the replacement rule (\ref{eq:vertex replacement rule}) and square the associated VTQFT partition function. This gives:
\begin{equation}\label{eq:ZVirOPE}
    \overline{\prod_{e_i\in \Gamma_{\mathcal{C}}}\!\!\rho(P_i,\bar P_i)\!\!\!\prod_{v_{ijk}\in \Gamma_{\mathcal{C}}}\!\!\!C_{ijk}} \,\,\,\supset \,\,\,\Big|\,\rho_g^{\mathcal{C}}(\boldsymbol{P})\, Z^{\,\mathcal{C}}_{\rm Vir}[M^{\gamma};\boldsymbol{P}]\,\Big|^2\, .
\end{equation}
 Crucially, the RHS of \eqref{eq:ZVirOPE} is generically a non-Gaussian contribution to the statistical moment on the LHS, which does not factorize into a product of variances.

\paragraph{How to tell a handlebody from a non-handlebody.}

 The fixed-$P$ formulation of Virasoro TQFT is useful for computations, because we have all of the tools of 3d topological quantum field theory at our disposal to evaluate the partition function. A list of useful calculation rules is collected in appendix \ref{app:technology}. However, one drawback of this formalism is that, given some random knotted trivalent graph,  it is in general hard to distinguish a handlebody from a non-handlebody. This problem comes down to finding a Moore-Seiberg move $\gamma$ such that the diagram can be untangled to a simple  diagram.\footnote{Another equivalent way of saying this is that in order to show that $M$ is a handlebody, one has to show that the VTQFT graph and its complement form a Heegaard splitting of $\mathrm{S}^3$.} This $\gamma$ could be a very long word in the generators $\mathbb{S}, \mathbb{F}$ and $\mathbb{B}$. For instance, in the example below, the left diagram corresponds to a handlebody and the right to a non-handlebody: 
\begin{equation}
\vcenter{\hbox{
\begin{tikzpicture}
    \begin{scope}[scale=1]
    \draw[very thick, wilsonred]
        (-0.67, -0.2) to[out=-85, in=140]
        (-0.15, -0.84);
        \draw[very thick, wilsonred]
        (0.1, -1.1) to[out=-45, in=-90]
        (1.7, -0.1) to[out = 90, in = 10]
        (-0.6,0.81);
        \draw[very thick, wilsonred]
        (-0.8,0.75) to[out = {180+10}, in = 90]
        (-1.70, -0.1) to[out= 270, in = 135]
        (-1.37, -1) to[out=-45, in = 215]
        (-0.1, -1.1);
        \draw[very thick, wilsonred]
        (-0.1,-1.1) to[out=45, in = -85]
        (0.62,0.62);
        \draw[very thick, wilsonred]
        (0.6,0.93) to[out = 100, in=0]
        (0, 1.7) to[out = 180, in = 95]
        (-0.71, 0);
        \draw[very thick, wilsonred]
        (-1.7, -0.1) -- (0.47, -0.1);
        \draw[very thick, wilsonred]
        (0.7, -0.1) --
        (1.7, -0.1);
        \node[left] at (-1.4,0.7) {$1$};
        \node[left] at (-1.1,-0.35) {$3$};
        \node[left] at (-1.4,-1.1) {$2$};
    \end{scope}
    \end{tikzpicture}
}} \qquad
\vcenter{\hbox{  
\begin{tikzpicture}
    \begin{scope}[scale=1]
        \draw[very thick, wilsonred]
        (-0.67, -0.2) to[out = -80, in =180]
        (0.76,-1.2) to[out=0, in=-90]
        (1.7, -0.1) to[out = 90, in = 10]
        (-0.6,0.81);
        \draw[very thick, wilsonred]
        (-0.8,0.75) to[out = {180+10}, in = 90]
        (-1.70, -0.1) to[out= 270, in = 135]
        (-1.37, -1) to[out=-45, in = 215]
        (-0.1, -1.1);
        \draw[very thick, wilsonred]
        (0.1,-0.9) to[out=35, in = -85]
        (0.62,0.62);
        \draw[very thick, wilsonred]
        (0.6,0.93) to[out = 100, in=0]
        (0, 1.7) to[out = 180, in = 95]
        (-0.71, 0);
        \draw[very thick, wilsonred]
        (-1.7, -0.1) -- (0.47, -0.1);
        \draw[very thick, wilsonred]
        (0.7, -0.1) --
        (1.7, -0.1);
        \node[left] at (-1.4,0.7) {$1$};
        \node[left] at (-1.1,-0.35) {$3$};
        \node[left] at (-1.4,-1.1) {$2$};
    \end{scope}
    \end{tikzpicture}
}}.
\end{equation}
The left is just the looped version of the sunset diagram \eqref{eq:loopedtheta} that we studied above. The right, on the other hand, corresponds to a known non-handlebody that we will study in section \ref{sec:5}, called $\mathbf{5}_2$ in our table \ref{table:handlebodyknots}. The two diagrams only differ by one under-over crossing. Moreover, 
both diagrams result from a fragmentation of the trefoil knot \cite{Chandra:2025fef}: on the left, the edge $3$ fragments the trefoil, and on the right the edge $1$ fragments the (mirror of the) trefoil. 

This example illustrates that the fragmentation procedure of \cite{Chandra:2025fef} obscures the handlebodiness of a given 3-manifold in VTQFT. This is not a problem if one’s perspective is to sum over \emph{all} 3-manifolds; but from the perspective of crossing symmetry, we want to be able to distinguish contributions from the sum over identity blocks from those that cannot be written as a mapping class group image of an identity block. 
Fortunately, for trivalent graphs embedded in $\mathrm{S}^3$, there is a simple test for handlebodiness, which we explain in appendix \ref{subapp:tricolorability}. A second method of determining handlebodiness is to study the fundamental group using Wirtinger's presentation, and running Whitehead's algorithm as explained in appendix \ref{subapp:fundamental group}.
