---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-012-handlebodies-are-not-sufficient
section_title: "Handlebodies are not sufficient"
section_number: null
pages: 41-46
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.994
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{subsec:gravitational machine 1}
Before introducing the gravitational machine in its full generality, we will just point out two examples of conditions imposed in section \ref{sec:2} that fail to be satisfied by the handlebody sum alone, showing that the handlebody sum is indeed insufficient.


\paragraph{Consistency between higher and lower genus.}
In section \ref{sec:3.3} we have seen that the handlebody sum at genus $g$ contains information about the handlebody sum at lower genus. For example, at genus 2 the sum over handlebodies (in the sunset channel) contains as a subsum the elements of the form $\gamma_{p_1,q_1}\circ \gamma_{p_2,q_2}\circ \mathbb{F}$, recall \eqref{eq:genus 2 to genus0,4 reduction}. Here $\gamma_{p,q}$ is a modular transformation at genus 1, labeled by a pair of co-prime integers that uniquely specify the $\mathrm{PSL}(2,\mathbb{Z})/\mathbb{Z}$ element. The sum over this subclass of crossing transformations contributes as:
\begin{equation}\label{eq:partialMWKs}
    \overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \,\supset \,\rho_{\text{MWK}}(h_1,\bar h_1)\rho_{\text{MWK}}(h_2,\bar h_2) \,\big|\rho_0(h_3)C_0(h_1,h_2,h_3)\big|^2\,.
\end{equation}
Here $\rho_{\text{MWK}}$ is the genus-1 handlebody sum \eqref{eq:MWKdensity}, which is the full sum over on-shell topologies contributing to the mean spectral density $\bar \rho$. As discussed in section \ref{sec:spectral_statistics}, if we ignore spectral correlations (associated to off-shell topologies in the bulk), the above statistical moment should factorize as:
\begin{equation}\label{eq:factorizegenus2}
    \overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} = \overline{\rho_1}\,\overline{\rho_2}\,\overline{\rho_3}\,\overline{C_{123}C_{123}^*}\,.
\end{equation}
Comparing to eq.~\eqref{eq:partialMWKs}, we see that the handlebody (sub-)sum correctly reproduces the means $\bar\rho_1 = \rho_{\text{MWK}}(h_1,\bar h_1)$ and $\bar\rho_2 = \rho_{\text{MWK}}(h_2,\bar h_2)$, but fails to reproduce the third mean spectral density $\bar\rho_3$, giving only the leading Cardy density $\rho_0(h_3)\rho_0(\bar h_3)$. Intuitively, the reason is that the genus-2 mapping class group is too small to accommodate three commuting copies of $\text{PSL}(2,\mathbb{Z})$. 

The set of topologies that \emph{does} factorize into lower moments as in \eqref{eq:factorizegenus2} is rather easy to describe, and it necessarily includes non-handlebodies. We describe this set using Dehn surgery: given a VTQFT diagram $\Gamma$ (i.e.~a network of Wilson lines), and a regular neighborhood $N(\Gamma)$ embedded in a closed 3-manifold $M_E$, take an edge dual to a non-contractible cycle in $M_E\setminus N(\Gamma)$. Then carve out a solid torus enclosing this edge and re-glue the solid torus after a modular transformation $\gamma_{p,q}$. Pictorially:
\begin{equation}\label{eq:dehn surgery picture}
\vcenter{\hbox{
\begin{tikzpicture}
    \draw[very thick, wilsonred] (-1,0) to node[above, black] {$P$} node[below, black] {$\phantom{P}$} (1,0);
\end{tikzpicture}
}}\  \longrightarrow\
\vcenter{\hbox{
\begin{tikzpicture}
    \draw[line width=13, black] (0,0) ellipse (0.6 and 1);
    \draw[line width=11, white] (0,0) ellipse (0.6 and 1);
    \draw[thick] (0,0.79) arc (-90:90:0.12 and 0.21);
    \draw[thick, dashed] (0,0.79) arc (270:90:0.12 and 0.21);
    \draw[thick] (0,-0.79) arc (90:-90:0.12 and 0.21);
    \draw[thick, dashed] (0,-0.79) arc (90:270:0.12 and 0.21);
    \draw[thick, blue] (-0.8,0.15) to[out = 80, in = -100] (-0.33,0.4);
    \draw[thick, blue] (-0.38,-0.15) to[out = -100, in = 80] (-0.77,-0.35);
    \draw[thick, blue] (-0.26,-0.55) to[out = -110, in =180] (0,-1);
    \draw[thick, blue] (0,-1) arc (-90:90:0.6 and 1);
    \draw[thick, blue] (-0.69,0.65) to[out = 40, in = -135] (-0.3,0.8) to[out=45, in=180] (0,1);
    \draw[thick, blue,dashed] (-0.33,0.4) to[out = 100, in = -80] (-0.7,0.6);
    \draw[thick, blue,dashed] (-0.8,0.15) to[out = -80, in = 100] (-0.38,-0.15);
    \draw[thick, blue,dashed] (-0.77,-0.35) to[out = -80, in = 100] (-0.25,-0.55);
    \draw[line width=4, white] (-0.3,0) to (1.2,0);
    \draw[very thick, wilsonred] (-0.3,0) to node[above, black] {$P\quad\;\;\;$} (1.2,0);
    \draw[very thick, wilsonred] (-1.2,0) to (-0.9,0);
\end{tikzpicture}
}} \cup
\vcenter{\hbox{
\begin{tikzpicture}[rotate = -90]
\draw[line width=13, black] (0,0) ellipse (0.6 and 1);
    \draw[line width=11, white] (0,0) ellipse (0.6 and 1);
    \draw[thick] (0,0.79) arc (-90:90:0.12 and 0.21);
    \draw[thick, dashed] (0,0.79) arc (270:90:0.12 and 0.21);
    \draw[thick] (0,-0.79) arc (90:-90:0.12 and 0.21);
    \draw[thick, dashed] (0,-0.79) arc (90:270:0.12 and 0.21);
    \fill[blue!15] (0.6,0) ellipse (0.21 and 0.12);
    \draw[thick,blue] (0.39,0) arc (180:0:0.21 and 0.12);
    \draw[thick, dashed,blue] (0.39,0) arc (180:360:0.21 and 0.12);
\end{tikzpicture}
}}.
\end{equation}
The element $\gamma_{p,q}$ maps the blue meridian on the right torus to a curve on the left which winds around the meridian $p$ times and around the longitude $q$ times (in the picture $p=3$ and $q=1$). For a curve with no self-intersections $p$ and $q$ are coprime integers, and the ordered pair written as $p/q$ is in one-to-one correspondence with the elements of $\mathrm{PSL}(2,\ZZ)/\ZZ$.

In Virasoro TQFT, the above Dehn surgery procedure is described by the Verlinde loop operator \cite{Collier:2024mgv, deBoer:2025rct}, as follows:
\begin{align}
    Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (271.75,122.6) -- (306.23,122.7) ;
\draw [shift={(271.75,122.6)}, rotate = 45.17] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [draw opacity=0] (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) -- (300.82,122.6) -- cycle ; \draw[line width=1.2pt]   (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (309.44,122.6) -- (332.43,122.54) ;
\draw [shift={(332.43,122.54)}, rotate = 44.84] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (259.53,122.6) .. controls (259.53,106.66) and (278.02,93.74) .. (300.82,93.74) .. controls (323.62,93.74) and (342.1,106.66) .. (342.1,122.6) .. controls (342.1,138.54) and (323.62,151.46) .. (300.82,151.46) .. controls (278.02,151.46) and (259.53,138.54) .. (259.53,122.6) -- cycle ;

\draw (316.3,124.28) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};

\draw (307.5,97.81) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$p/q$};
\end{tikzpicture}
\right] &\equiv \int_0^\infty \d P \, \mathbb{K}^{(p,q)}_{\id P} \,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (271.75,122.6) -- (306.23,122.7) ;
\draw [shift={(271.75,122.6)}, rotate = 45.17] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [draw opacity=0] (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) -- (300.82,122.6) -- cycle ; \draw [line width=1.2pt]  (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (309.44,122.6) -- (332.43,122.54) ;
\draw [shift={(332.43,122.54)}, rotate = 44.84] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (259.53,122.6) .. controls (259.53,106.66) and (278.02,93.74) .. (300.82,93.74) .. controls (323.62,93.74) and (342.1,106.66) .. (342.1,122.6) .. controls (342.1,138.54) and (323.62,151.46) .. (300.82,151.46) .. controls (278.02,151.46) and (259.53,138.54) .. (259.53,122.6) -- cycle ;

\draw (316.3,124.28) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};

\draw (307.5,97.81) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P$};
\end{tikzpicture}
\right]\\[1em]
   &= \int_0^\infty \d P \,\mathbb{K}_{\id P}^{(p,q)} \,\frac{\sker{P}{P_i}{\id}}{\sker{\id}{P_i}{\id}}\,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (286.33,129.17) .. controls (292.67,120.17) and (309.67,130.5) .. (322.33,128.83) .. controls (335,127.17) and (351,124.83) .. (355.33,127.83) .. controls (359.67,130.83) and (361.84,131.28) .. (361.67,141.83) .. controls (361.5,152.39) and (360.67,153.5) .. (353,157.83) .. controls (345.33,162.17) and (334.33,152.5) .. (320.67,153.17) .. controls (307,153.83) and (298.33,161.17) .. (290.67,156.83) .. controls (283,152.5) and (282.33,149.17) .. (283.67,141.5) .. controls (285,133.83) and (280.36,136.95) .. (286.33,129.17) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (291.75,142.6) -- (351.33,142.5) ;
\draw [shift={(351.33,142.5)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(291.75,142.6)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (331.44,128.33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};
\end{tikzpicture}
\right]  \\[1em]
    &= \frac{1}{\rho_0(P_i)
    }\,\mathbb{K}_{\id P_i}^{(-q,p)}\,Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (286.33,129.17) .. controls (292.67,120.17) and (309.67,130.5) .. (322.33,128.83) .. controls (335,127.17) and (351,124.83) .. (355.33,127.83) .. controls (359.67,130.83) and (361.84,131.28) .. (361.67,141.83) .. controls (361.5,152.39) and (360.67,153.5) .. (353,157.83) .. controls (345.33,162.17) and (334.33,152.5) .. (320.67,153.17) .. controls (307,153.83) and (298.33,161.17) .. (290.67,156.83) .. controls (283,152.5) and (282.33,149.17) .. (283.67,141.5) .. controls (285,133.83) and (280.36,136.95) .. (286.33,129.17) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (291.75,142.6) -- (351.33,142.5) ;
\draw [shift={(351.33,142.5)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(291.75,142.6)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (331.44,128.33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};
\end{tikzpicture}
\right]\,.\label{eq:dehnsurg}
\end{align}
Here $\mathbb{K}^{(p,q)}_{\id P}$ is the modular kernel for $\gamma_{p,q}$, implementing the Dehn surgery with surgery coefficient $p/q$. In the second line we used the formula \eqref{eq:verlindeloop} for removing the Verlinde loop, and in the third line we used the fact that $\gamma_{p,q}\circ \mathbb{S} = \gamma_{-q,p}$ under the modular S-transform. The above manipulations can be done locally on any edge of $\Gamma$, indicated as before by the dotted line.

To obtain the gravitational partition function from the above VTQFT computation, we multiply the fixed-$P$ partition function \eqref{eq:dehnsurg} by the normalization factor $\rho^{\,\mathcal{C}}_g(\boldsymbol{P})$---which in particular contains a factor $\rho_0(P_i)$ for the $i^{\text{th}}$ edge---and then we multiply by the right-moving counterpart. Finally, we sum over the co-primes $p,q$. The net effect of this sum over Dehn surgeries is that the Cardy density $\rho_0$ gets modular completed to the MWK spectral density:
\be\label{eq:complete to MWK}
    \rho_0(P_i)\rho_0(\bar P_i)\,\left |\tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (271.75,122.6) -- (306.23,122.7) ;
\draw [shift={(271.75,122.6)}, rotate = 45.17] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [draw opacity=0] (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) -- (300.82,122.6) -- cycle ; \draw[line width=1.2pt]   (294.15,119.26) .. controls (294.64,108.78) and (297.44,100.75) .. (300.82,100.75) .. controls (304.55,100.75) and (307.57,110.53) .. (307.57,122.6) .. controls (307.57,134.66) and (304.55,144.44) .. (300.82,144.44) .. controls (297.45,144.44) and (294.67,136.48) .. (294.15,126.06) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (309.44,122.6) -- (332.43,122.54) ;
\draw [shift={(332.43,122.54)}, rotate = 44.84] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (259.53,122.6) .. controls (259.53,106.66) and (278.02,93.74) .. (300.82,93.74) .. controls (323.62,93.74) and (342.1,106.66) .. (342.1,122.6) .. controls (342.1,138.54) and (323.62,151.46) .. (300.82,151.46) .. controls (278.02,151.46) and (259.53,138.54) .. (259.53,122.6) -- cycle ;

\draw (316.3,124.28) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};

\draw (307.5,97.81) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$p/q$};
\end{tikzpicture}
\right |^2  \,\,\xrightarrow[\text{co-primes}\,p,q]{\text{sum over}}  \,\, \rho_{\text{MWK}}'(P_i,\bar P_i) \left| \tikzset{every picture/.style={line width=0.8pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.2,xscale=1.2,baseline={([yshift=-0.5ex]current bounding box.center)}] 

\draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (286.33,129.17) .. controls (292.67,120.17) and (309.67,130.5) .. (322.33,128.83) .. controls (335,127.17) and (351,124.83) .. (355.33,127.83) .. controls (359.67,130.83) and (361.84,131.28) .. (361.67,141.83) .. controls (361.5,152.39) and (360.67,153.5) .. (353,157.83) .. controls (345.33,162.17) and (334.33,152.5) .. (320.67,153.17) .. controls (307,153.83) and (298.33,161.17) .. (290.67,156.83) .. controls (283,152.5) and (282.33,149.17) .. (283.67,141.5) .. controls (285,133.83) and (280.36,136.95) .. (286.33,129.17) -- cycle ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (291.75,142.6) -- (351.33,142.5) ;
\draw [shift={(351.33,142.5)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;
\draw [shift={(291.75,142.6)}, rotate = 44.9] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.91,0) -- (2.91,0)(0,2.91) -- (0,-2.91)   ;

\draw (331.44,128.33) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_{i}$};
\end{tikzpicture}
\right |^2.
\ee
Here $\rho'_{\text{MWK}}$ is the MWK handlebody sum \eqref{eq:MWKdensity} without the vacuum contribution, i.e.~$\rho_{\text{MWK}} = \delta(h)\delta(\bar h) + \rho'_{\text{MWK}}$. In other words, we excluded the Dehn surgery with $(p,q) = (0,1)$, which projects $P_i$ to the identity $\id$. This corresponds to the case that the surgery implements the action of the $\Omega$-loop. In this way, the sum over Dehn surgeries upgrades the heavy Cardy density to the heavy part of the MWK density, leaving the identity contributions that are already part of the genus-$g$ handlebody sum. Importantly, for complicated enough Dehn surgery coefficients, the manifolds constructed by our procedure \eqref{eq:dehnsurg} can be non-handlebodies. 

Let us see how this works in the genus-2 example discussed above. Dehn surgery on the three internal lines of the sunset channel gives:\footnote{Here we used the sunset normalization factor $\rho^{\,\mathcal{C}}_{g=2}(\boldsymbol{P}) = \rho_0(P_1)\rho_0(P_2)\rho_0(P_3)C_0(P_1,P_2,P_3)^2$, as well as \eqref{eq:theta graph ZVir} for evaluating the sunset diagram in VTQFT.}
\begin{equation}
    \rho^{\,\mathcal{C}}_{g=2}(\boldsymbol{P})\, Z_{\text{Vir}}\!\left[
\vcenter{\hbox{
\begin{tikzpicture}[yscale=1,xscale=0.75]
\draw[very thick, wilsonred] (0,1) -- (0,-1);
\draw[very thick, wilsonred] (0,0) ellipse (2 and 1);
\draw[very thick] (-0.07,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\frac{p_2}{q_2}$}};
\draw[very thick] (-2,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\frac{p_1}{q_1}$}};
\draw[very thick] (1.9,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\frac{p_3}{q_3}$}};
\draw (0,-0.5) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_2$};
\draw (-1.4,-0.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_1$};
\draw (1,-0.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$P_3$};
\end{tikzpicture}
}}
\right] = \mathbb{K}_{\id P_1}^{(-q_1,p_1)} \mathbb{K}_{\id P_2}^{(-q_2,p_2)} \mathbb{K}_{\id P_3}^{(-q_3,p_3)} C_0(P_1,P_2,P_3).
\end{equation}
In section \ref{sec:5}, we will identify the topology of the filling $(\frac{p_1}{q_1},\frac{p_2}{q_2},\frac{p_3}{q_3}) = (2,2,2)$ with a non-handlebody known as the twisted $I$-bundle \cite{Yin:2007at}, and  $(\frac{p_1}{q_1},\frac{p_2}{q_2},\frac{p_3}{q_3}) = (2,2,3)$ with another non-handlebody called the $\mathbf{5}_2$ handlebody-knot. In total, the sum over all the surgery coefficients $(p_i,q_i)$ contributes as:
\begin{equation}\label{eq: sunset surgery}
    \overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \,\supset\, \rho_{\text{MWK}}(h_1,\bar h_1)\rho_{\text{MWK}}(h_2,\bar h_2) \rho_{\text{MWK}}(h_3,\bar h_3)\,\big|C_0(h_1,h_2,h_3)\big|^2\,,
\end{equation}
which is indeed of the factorized form
\eqref{eq:factorizegenus2}. Although compatible with genus-1 modular invariance, the sum over Dehn surgeries itself still has to be completed by a sum over the genus-2 mapping class group, which acts via crossing transformations on the sunset diagram. The non-trivial interplay between crossing and the factorization \eqref{eq:factorizegenus2} into lower moments will be explained in more depth in section \ref{subsec:general gravitational machine}.


\paragraph{Typicality.}
As a second constraint that is not satisfied by the handlebody sum, we give an example of a violation of the typicality condition discussed in section \ref{sec:typicality}. As explained there, typicality predicts extra terms contributing to statistical moments with repeated pairs of indices, such as $\overline{C_{113}C_{113}}$. On the level of distributions, this means there are delta-function contributions such as:
\begin{multline}\label{eq:typicality again}
    \overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \, \supset \\ \delta^2(h_1-h_2)\, \overline{\rho_1}\,\overline{\rho_3} \,\left[(1+(-1)^{J_3})\,\mathcal{G}_S\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.5,xscale=0.5]
        \draw[very thick, wilsonred] (0,0) ellipse (1.5 and 1);
        \draw[very thick, wilsonred] (0,1) -- (0,-1);
        \node at (-1.2,0) {\footnotesize $1$};
        \node at (0.29,0) {\footnotesize $1$};
        \node at (1.2,0) {\footnotesize $3$};
    \end{tikzpicture}
    }}\right] + \mathcal{G}_D\!\left[\vcenter{\hbox{
    \begin{tikzpicture}[yscale=-0.85,xscale=0.85]
        \draw[very thick, wilsonred] (-1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (1,0) circle (0.5 and 0.5);
        \draw[very thick, wilsonred] (-0.5,0) -- (0.5,0);
        \node at (-1,-0.15) {\footnotesize $1$};
        \node at (0,0.3)  {\footnotesize $3$};
        \node at (1,-0.15)  {\footnotesize $1$};
    \end{tikzpicture}
    }}\right] \right].
\end{multline}
This is an example of a term for the index contraction $\delta_{12}$, which, since we are integrating over densities, has been represented by the Dirac delta $\delta^2(h_1-h_2) \equiv \delta(h_1-h_2)\delta(\bar h_1-\bar h_2)$. 
In some cases, these delta-function contributions may be accounted for in the bulk by handlebodies, but in general we require non-handlebodies to account for all index contractions. 

For example, \eqref{eq:typicality again} receives a contribution from the following handlebody:
\begin{equation}\label{eq:handlebody contribution}
\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (554.04,180.8) .. controls (516.15,156.6) and (555.94,124.36) .. (567.43,142.71) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (569.79,98.29) .. controls (594.8,146.19) and (556.2,158.34) .. (547.95,144.75) ;

\draw  [draw opacity=0][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) -- (578.03,141.96) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (543.4,136.77) .. controls (536.46,121.62) and (540.36,111.88) .. (554.11,103.07) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (566.4,185.12) .. controls (574.48,177.55) and (576.45,155.43) .. (571.79,149.78) ;

\draw (546.67,108.7) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $1$};

\draw (548.47,160.29) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $2$};

\draw (611.3,133.09) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $3$};

\draw (579.4,108.8) node [anchor=north west][inner sep=0.75pt]    {$'$};
\end{tikzpicture}.
\end{equation}
 Here we drew the linked dumbbell from the previous section (with the opposite over-under crossing), where one of the bells is in the S-dual channel as indicated by the prime. We can check that this indeed produces the desired delta function by using the $\Omega$-loop defined in \eqref{eq:omegaloop} to implement the S-transform:
\begin{equation}
    Z_\text{Vir}\!\left[\!\!\!\!\!\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (554.04,180.8) .. controls (516.15,156.6) and (555.94,124.36) .. (567.43,142.71) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (569.79,98.29) .. controls (594.8,146.19) and (556.2,158.34) .. (547.95,144.75) ;

\draw  [draw opacity=0][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) -- (578.03,141.96) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (543.4,136.77) .. controls (536.46,121.62) and (540.36,111.88) .. (554.11,103.07) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (566.4,185.12) .. controls (574.48,177.55) and (576.45,155.43) .. (571.79,149.78) ;

\draw (546.67,108.7) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $1$};

\draw (548.47,160.29) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $2$};

\draw (611.3,133.09) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $3$};

\draw (579.4,108.8) node [anchor=north west][inner sep=0.75pt]    {$'$};
\end{tikzpicture}\right] = Z_\text{Vir}\!\left[ \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ]   (200,105) .. controls (226.86,112.71) and (224,158.43) .. (200,165) ;

\draw  [draw opacity=0] (174.89,116.08) .. controls (171.88,113.34) and (170,109.39) .. (170,105) .. controls (170,96.72) and (176.72,90) .. (185,90) .. controls (193.28,90) and (200,96.72) .. (200,105) .. controls (200,113.28) and (193.28,120) .. (185,120) .. controls (183.15,120) and (181.37,119.66) .. (179.73,119.05) -- (185,105) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (174.89,116.08) .. controls (171.88,113.34) and (170,109.39) .. (170,105) .. controls (170,96.72) and (176.72,90) .. (185,90) .. controls (193.28,90) and (200,96.72) .. (200,105) .. controls (200,113.28) and (193.28,120) .. (185,120) .. controls (183.15,120) and (181.37,119.66) .. (179.73,119.05) ;  

\draw  [draw opacity=0] (179.93,150.88) .. controls (181.52,150.31) and (183.22,150) .. (185,150) .. controls (193.28,150) and (200,156.72) .. (200,165) .. controls (200,173.28) and (193.28,180) .. (185,180) .. controls (176.72,180) and (170,173.28) .. (170,165) .. controls (170,160.6) and (171.89,156.65) .. (174.9,153.91) -- (185,165) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (179.93,150.88) .. controls (181.52,150.31) and (183.22,150) .. (185,150) .. controls (193.28,150) and (200,156.72) .. (200,165) .. controls (200,173.28) and (193.28,180) .. (185,180) .. controls (176.72,180) and (170,173.28) .. (170,165) .. controls (170,160.6) and (171.89,156.65) .. (174.9,153.91) ;  

\draw  [draw opacity=0] (187.52,153.01) .. controls (186.29,158.95) and (184.47,162.71) .. (182.43,162.71) .. controls (178.72,162.71) and (175.71,150.24) .. (175.71,134.86) .. controls (175.71,119.47) and (178.72,107) .. (182.43,107) .. controls (184.5,107) and (186.36,110.91) .. (187.59,117.05) -- (182.43,134.86) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (187.52,153.01) .. controls (186.29,158.95) and (184.47,162.71) .. (182.43,162.71) .. controls (178.72,162.71) and (175.71,150.24) .. (175.71,134.86) .. controls (175.71,119.47) and (178.72,107) .. (182.43,107) .. controls (184.5,107) and (186.36,110.91) .. (187.59,117.05) ;  

\draw  [draw opacity=0] (188.6,123.85) .. controls (188.95,127.23) and (189.14,130.95) .. (189.14,134.86) .. controls (189.14,139.25) and (188.9,143.41) .. (188.46,147.11) -- (182.43,134.86) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (188.6,123.85) .. controls (188.95,127.23) and (189.14,130.95) .. (189.14,134.86) .. controls (189.14,139.25) and (188.9,143.41) .. (188.46,147.11) ;  

\draw (161,96.54) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (160.14,160.97) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (209.57,127.97) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (157.57,126.83) node [anchor=north west][inner sep=0.75pt]    {$\Omega $};
\end{tikzpicture}\right] = \frac{\delta(P_1-P_2)}{\rho_0(P_2)}\, Z_\text{Vir}\!\left[ \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (170.25,150) -- (170.25,216) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (126.34,183) .. controls (126.34,164.77) and (146,150) .. (170.25,150) .. controls (194.51,150) and (214.17,164.77) .. (214.17,183) .. controls (214.17,201.23) and (194.51,216) .. (170.25,216) .. controls (146,216) and (126.34,201.23) .. (126.34,183) -- cycle ;

\draw (130.14,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (157.97,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (200.01,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}
\right].
\end{equation}
Here we used the VTQFT identity \eqref{eq:omega loop on pair of lines} for the $\Omega$-loop encircling two Wilson lines. We can also directly use the VTQFT partition function for the linked dumbbell computed in \eqref{eq:Z_linkedhandcuff}, together with the fact that $\mathbb{S}$ is unitary:
\begin{align}
    \int_0^\infty \d P\, \sker{P_1}{P}{P_3} Z_\text{Vir}\!\left[\!\!\!\!\!\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (554.04,180.8) .. controls (516.15,156.6) and (555.94,124.36) .. (567.43,142.71) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (569.79,98.29) .. controls (594.8,146.19) and (556.2,158.34) .. (547.95,144.75) ;

\draw  [draw opacity=0][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) -- (578.03,141.96) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (554.11,103.07) .. controls (558.8,100.75) and (563.99,99.07) .. (569.57,98.2) .. controls (596.47,94) and (622.07,110.19) .. (626.74,134.36) .. controls (631.41,158.52) and (613.39,181.52) .. (586.48,185.71) .. controls (574.9,187.52) and (563.57,185.55) .. (554.04,180.8) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (543.4,136.77) .. controls (536.46,121.62) and (540.36,111.88) .. (554.11,103.07) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (566.4,185.12) .. controls (574.48,177.55) and (576.45,155.43) .. (571.79,149.78) ;

\draw (546.67,108.7) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $P$};

\draw (548.47,160.29) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $2$};

\draw (611.3,133.09) node [anchor=north west][inner sep=0.75pt]    {\footnotesize $3$};

\end{tikzpicture}\right] &= \int_0^\infty \d P\, \sker{P_1}{P}{P_3} \frac{\sker{P}{P_2}{P_3}^*}{\rho_0(P_2)C_0(P_2,P_2,P_3)} \\&=  \frac{\delta(P_1-P_2)}{\rho_0(P_2)C_0(P_2,P_2,P_3)}. 
\end{align}
Multiplying by the normalization factor $\rho_{g=2}(\boldsymbol{P})$ and the anti-holomorphic counterpart, we see that this handlebody contributes in the following way:
\begin{equation}
\overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \, \supset \delta^2(h_1-h_2)\, |\rho_0(h_1)\rho_0(h_3)C_0(h_1,h_1,h_3)|^2\,.
\end{equation}
There is also the handlebody with the opposite over-under crossing of the linked handles, which gives an extra phase factor $\e^{-\pi i h_3}$, as already remarked in \eqref{eq:cherryOPE}. This accounts for the $(-1)^{J_3}$ contribution to the moment \eqref{eq:typicality again}. 

Even though handlebodies account for some of the contractions predicted by typicality, not all of the contractions can be explained by the handlebody sum alone. For example, the enhancement in \eqref{eq:typicality again} by the dumbbell terms $\mathcal{G}_D$ consists of non-handlebody contributions, as we will see in section \ref{sec:5}. A simpler example is given by the double contraction $\delta_{12}\delta_{23}$, recall \eqref{eq:repeated indices b}, which contributes to the second moment when all indices coincide, $\overline{C_{iii}C_{iii}}$. When $h_i\neq \id$, the only contributions to this moment come from non-handlebodies. In fact, the simplest contribution comes from a so-called \emph{handlebody-knot}, whose VTQFT diagram can be drawn as:
 \begin{equation}\label{eq:41prime}
\tikzset{every picture/.style={line width=0.75pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][line width=1.2]  (407.84,152.91) .. controls (409.49,153.13) and (411.21,153.12) .. (412.95,152.86) .. controls (422.27,151.43) and (428.72,143.14) .. (427.37,134.35) .. controls (426.03,125.55) and (417.38,119.58) .. (408.07,121.01) .. controls (398.76,122.44) and (392.3,130.73) .. (393.65,139.52) .. controls (394.17,142.89) and (395.76,145.85) .. (398.05,148.14) -- (410.51,136.93) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (407.84,152.91) .. controls (409.49,153.13) and (411.21,153.12) .. (412.95,152.86) .. controls (422.27,151.43) and (428.72,143.14) .. (427.37,134.35) .. controls (426.03,125.55) and (417.38,119.58) .. (408.07,121.01) .. controls (398.76,122.44) and (392.3,130.73) .. (393.65,139.52) .. controls (394.17,142.89) and (395.76,145.85) .. (398.05,148.14) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (407.59,121.89) .. controls (402.76,110.15) and (384,103.75) .. (365.38,103.92) .. controls (346.75,104.08) and (337.89,109.67) .. (336.91,116.21) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (390.56,134.78) .. controls (380.42,130.26) and (343.89,140.78) .. (335.89,126.11) ;

\draw  [draw opacity=0][line width=1.2]  (351.27,127.43) .. controls (347.6,122.8) and (341.57,120.21) .. (335.25,121.18) .. controls (325.94,122.61) and (319.54,131.22) .. (320.95,140.41) .. controls (322.35,149.6) and (331.05,155.89) .. (340.36,154.46) .. controls (348.38,153.23) and (354.25,146.67) .. (354.82,138.99) -- (337.81,137.82) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (351.27,127.43) .. controls (347.6,122.8) and (341.57,120.21) .. (335.25,121.18) .. controls (325.94,122.61) and (319.54,131.22) .. (320.95,140.41) .. controls (322.35,149.6) and (331.05,155.89) .. (340.36,154.46) .. controls (348.38,153.23) and (354.25,146.67) .. (354.82,138.99) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (341.13,154.68) .. controls (353,167.29) and (377.42,166.86) .. (391.29,162.71) .. controls (405.15,158.56) and (407.74,145.42) .. (399,139) ;

\draw (315,123.4) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (427.5,122.4) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (367.38,107.32) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (414,135.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (325.5,134.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};
\end{tikzpicture} \,.
\end{equation}
If we take this knotted graph and embed it in $\mathrm{S}^3$, its complement is a non-handlebody with genus-2 boundary. It is the handlebody-knot with the least number of over-under crossings, called the $\mathbf{4}_1$ handlebody-knot in the classification of  \cite{ISHII:2012}. The primes indicate that we additionally perform an S-transform on the two bells. Let us check that this manifold produces the desired delta functions for the double contraction: 
\begin{align}
    Z_\text{Vir}\!\left[\tikzset{every picture/.style={line width=0.75pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][line width=1.2]  (407.84,152.91) .. controls (409.49,153.13) and (411.21,153.12) .. (412.95,152.86) .. controls (422.27,151.43) and (428.72,143.14) .. (427.37,134.35) .. controls (426.03,125.55) and (417.38,119.58) .. (408.07,121.01) .. controls (398.76,122.44) and (392.3,130.73) .. (393.65,139.52) .. controls (394.17,142.89) and (395.76,145.85) .. (398.05,148.14) -- (410.51,136.93) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (407.84,152.91) .. controls (409.49,153.13) and (411.21,153.12) .. (412.95,152.86) .. controls (422.27,151.43) and (428.72,143.14) .. (427.37,134.35) .. controls (426.03,125.55) and (417.38,119.58) .. (408.07,121.01) .. controls (398.76,122.44) and (392.3,130.73) .. (393.65,139.52) .. controls (394.17,142.89) and (395.76,145.85) .. (398.05,148.14) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (407.59,121.89) .. controls (402.76,110.15) and (384,103.75) .. (365.38,103.92) .. controls (346.75,104.08) and (337.89,109.67) .. (336.91,116.21) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (390.56,134.78) .. controls (380.42,130.26) and (343.89,140.78) .. (335.89,126.11) ;

\draw  [draw opacity=0][line width=1.2]  (351.27,127.43) .. controls (347.6,122.8) and (341.57,120.21) .. (335.25,121.18) .. controls (325.94,122.61) and (319.54,131.22) .. (320.95,140.41) .. controls (322.35,149.6) and (331.05,155.89) .. (340.36,154.46) .. controls (348.38,153.23) and (354.25,146.67) .. (354.82,138.99) -- (337.81,137.82) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (351.27,127.43) .. controls (347.6,122.8) and (341.57,120.21) .. (335.25,121.18) .. controls (325.94,122.61) and (319.54,131.22) .. (320.95,140.41) .. controls (322.35,149.6) and (331.05,155.89) .. (340.36,154.46) .. controls (348.38,153.23) and (354.25,146.67) .. (354.82,138.99) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (341.13,154.68) .. controls (353,167.29) and (377.42,166.86) .. (391.29,162.71) .. controls (405.15,158.56) and (407.74,145.42) .. (399,139) ;

\draw (315,123.4) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (427.5,122.4) node [anchor=north west][inner sep=0.75pt]    {$'$};

\draw (367.38,107.32) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (414,135.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (325.5,134.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};
\end{tikzpicture}\right] &= Z_\text{Vir}\!\left[ \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][line width=1.2]  (411.38,146.2) .. controls (411.9,146.91) and (412.48,147.58) .. (413.14,148.2) .. controls (419.57,154.35) and (430.06,153.81) .. (436.57,147.01) .. controls (443.08,140.2) and (443.15,129.69) .. (436.72,123.54) .. controls (430.29,117.39) and (419.8,117.93) .. (413.29,124.74) .. controls (409.31,128.9) and (407.73,134.44) .. (408.58,139.52) -- (424.93,135.87) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (411.38,146.2) .. controls (411.9,146.91) and (412.48,147.58) .. (413.14,148.2) .. controls (419.57,154.35) and (430.06,153.81) .. (436.57,147.01) .. controls (443.08,140.2) and (443.15,129.69) .. (436.72,123.54) .. controls (430.29,117.39) and (419.8,117.93) .. (413.29,124.74) .. controls (409.31,128.9) and (407.73,134.44) .. (408.58,139.52) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (412.87,125.73) .. controls (401.88,119.37) and (375.86,120.71) .. (367.29,126.43) .. controls (358.71,132.14) and (358.92,142.54) .. (364.25,145.88) ;

\draw  [draw opacity=0][line width=1.2]  (356.54,168.42) .. controls (356.24,168.69) and (355.95,168.97) .. (355.67,169.26) .. controls (349.16,176.07) and (349.32,186.8) .. (356.04,193.23) .. controls (362.76,199.65) and (373.49,199.34) .. (380,192.53) .. controls (386.51,185.72) and (386.34,174.99) .. (379.62,168.57) .. controls (375.18,164.32) and (368.99,163.02) .. (363.42,164.59) -- (367.83,180.9) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (356.54,168.42) .. controls (356.24,168.69) and (355.95,168.97) .. (355.67,169.26) .. controls (349.16,176.07) and (349.32,186.8) .. (356.04,193.23) .. controls (362.76,199.65) and (373.49,199.34) .. (380,192.53) .. controls (386.51,185.72) and (386.34,174.99) .. (379.62,168.57) .. controls (375.18,164.32) and (368.99,163.02) .. (363.42,164.59) ;  

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (380.74,192.52) .. controls (397.84,195.28) and (415.29,198.43) .. (422.14,189.86) .. controls (429,181.29) and (414.14,168.71) .. (403.86,164.71) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (370.5,150.5) .. controls (378.64,155.36) and (390.26,159.83) .. (396.83,161.83) ;

\draw  [draw opacity=0][line width=1.2]  (375.26,169.4) .. controls (371.26,175.64) and (366.52,179.19) .. (363.23,177.85) .. controls (358.8,176.04) and (358.71,165.99) .. (363.04,155.4) .. controls (367.37,144.81) and (374.47,137.69) .. (378.9,139.51) .. controls (382.01,140.78) and (382.98,146.11) .. (381.79,152.83) -- (371.07,158.68) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.2]  (375.26,169.4) .. controls (371.26,175.64) and (366.52,179.19) .. (363.23,177.85) .. controls (358.8,176.04) and (358.71,165.99) .. (363.04,155.4) .. controls (367.37,144.81) and (374.47,137.69) .. (378.9,139.51) .. controls (382.01,140.78) and (382.98,146.11) .. (381.79,152.83) ;  

\draw  [draw opacity=0][line width=1.2]  (380.48,158.11) .. controls (380.09,159.38) and (379.62,160.66) .. (379.09,161.96) .. controls (378.87,162.5) and (378.64,163.04) .. (378.41,163.56) -- (371.07,158.68) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.2]  (380.48,158.11) .. controls (380.09,159.38) and (379.62,160.66) .. (379.09,161.96) .. controls (378.87,162.5) and (378.64,163.04) .. (378.41,163.56) ;  

\draw  [draw opacity=0][line width=1.2]  (411.63,172.75) .. controls (408.31,176.68) and (404.82,178.66) .. (402.23,177.6) .. controls (397.8,175.79) and (397.71,165.74) .. (402.04,155.15) .. controls (406.37,144.56) and (413.47,137.44) .. (417.9,139.26) .. controls (420.41,140.28) and (421.53,143.96) .. (421.24,148.89) -- (410.07,158.43) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.2]  (411.63,172.75) .. controls (408.31,176.68) and (404.82,178.66) .. (402.23,177.6) .. controls (397.8,175.79) and (397.71,165.74) .. (402.04,155.15) .. controls (406.37,144.56) and (413.47,137.44) .. (417.9,139.26) .. controls (420.41,140.28) and (421.53,143.96) .. (421.24,148.89) ;  

\draw  [draw opacity=0][line width=1.2]  (420.01,156.04) .. controls (419.52,157.88) and (418.88,159.78) .. (418.09,161.71) .. controls (417.18,163.95) and (416.14,166.03) .. (415.03,167.91) -- (410.07,158.43) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.2]  (420.01,156.04) .. controls (419.52,157.88) and (418.88,159.78) .. (418.09,161.71) .. controls (417.18,163.95) and (416.14,166.03) .. (415.03,167.91) ;  

\draw (342.92,151.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\Omega $};

\draw (421.67,156.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$\Omega $};

\draw (386,122.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (361.75,184.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (422.75,120.65) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}\right] \\[1em]
&= \frac{\delta(P_1-P_2)}{\rho_0(P_2)}\,\frac{\delta(P_2-P_3)}{\rho_0(P_3)}\, Z_\text{Vir}\!\left[ \tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (170.25,150) -- (170.25,216) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (126.34,183) .. controls (126.34,164.77) and (146,150) .. (170.25,150) .. controls (194.51,150) and (214.17,164.77) .. (214.17,183) .. controls (214.17,201.23) and (194.51,216) .. (170.25,216) .. controls (146,216) and (126.34,201.23) .. (126.34,183) -- cycle ;

\draw (130.14,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (157.97,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (200.01,176.6) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};
\end{tikzpicture}
\right].\label{eq:41prime self-gluing}
\end{align}
 Multiplying by the normalization factor and the anti-holomorphic counterpart, we confirm that this non-handlebody is the leading contribution to the double index contraction $\delta_{12}\delta_{23}$ at genus two:
 \begin{equation}\label{eq:C_111C_111}
\overline{\rho_1\rho_2\rho_3C_{123}C_{123}^*} \, \supset \delta^2(h_1-h_2)\,\delta^2(h_2-h_3) \,|\rho_0(h_1)C_0(h_1,h_1,h_1)|^2\,.
\end{equation}
This example shows that non-handlebodies like $\mathbf{4}_1$ are needed for consistency with typicality.
Since a non-handlebody always remains a non-handlebody after crossing transformations, all of the mapping class group images of \eqref{eq:41prime} (which are needed to complete \eqref{eq:C_111C_111} into a crossing symmetric density) are also non-handlebodies. Moreover, it may be further modified by Dehn surgery to upgrade $\rho_0$ to $\rho_{\text{MWK}}$. 

In the next subsection, we will take the two examples studied above as the basis for an algorithm for generating 3-manifolds, which we call the `gravitational machine'.
