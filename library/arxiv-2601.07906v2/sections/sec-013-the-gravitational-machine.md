---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-013-the-gravitational-machine
section_title: "The gravitational machine"
section_number: null
pages: 46-52
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.996
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{subsec:general gravitational machine}

The examples discussed above suggest a general procedure that systematically constructs a minimal set of 3-manifolds that should be summed over in the bulk, in order to satisfy the constraints imposed in section \ref{sec:2} on the moments of the CFT data. In this section, we will introduce this algorithm---the gravitational machine---in full generality. It will generalize both the Dehn surgery and the $\Omega$-loop computations of the previous section and works for manifolds with arbitrary number of boundary components of any genus $g\geq 1$. We will formulate the rules on the level of the fixed-$P$ partition functions, i.e.~for networks of Wilson lines in VTQFT. It is simple to change the formulation into the canonical ensemble by thickening the Wilson lines and considering the drilled out manifold with the asymptotic conformal boundary. 

\paragraph{Cylinder surgery.}
The main topological operation in the gravitational machine is what we will call \emph{cylinder surgery}. This procedure can be described as follows. Given a (possibly disconnected) network of Wilson lines in VTQFT, surround one of the edges by a 2-punctured sphere, and carve out its interior to obtain a new manifold with a 2-punctured sphere boundary. Do the same with another edge, and glue the two 2-punctured spheres to each other with the opposite orientation:
\begin{equation}\label{eq:cylinder surgery}
    \tikzset{every picture/.style={line width=0.75pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ]   (439.57,167.78) .. controls (438.95,163.52) and (439.24,156.67) .. (439.28,152.06) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (393.93,167.93) .. controls (394.38,163.52) and (394.38,156.67) .. (394.2,152.21) ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (383.46,160.17) .. controls (383.46,154.21) and (388.63,149.39) .. (395.01,149.39) .. controls (401.38,149.39) and (406.55,154.21) .. (406.55,160.17) .. controls (406.55,166.12) and (401.38,170.95) .. (395.01,170.95) .. controls (388.63,170.95) and (383.46,166.12) .. (383.46,160.17) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (427.38,160.17) .. controls (427.38,154.21) and (432.55,149.39) .. (438.92,149.39) .. controls (445.3,149.39) and (450.46,154.21) .. (450.46,160.17) .. controls (450.46,166.12) and (445.3,170.95) .. (438.92,170.95) .. controls (432.55,170.95) and (427.38,166.12) .. (427.38,160.17) -- cycle ;

\draw [line width=1.2]    (403.71,165) .. controls (410.54,168.36) and (424.57,168.55) .. (432.16,165.25) ;
\draw [shift={(435.5,163.17)}, rotate = 148.89] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;
\draw [shift={(400.5,162.5)}, rotate = 36.76] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (381.44,124.17) .. controls (392.52,135.6) and (393.38,143.32) .. (394.2,152.21) ;
\draw [shift={(394.2,152.21)}, rotate = 129.71] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (372.95,116.15) .. controls (375.96,118.46) and (378.56,121.04) .. (381.44,124.17) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (384.62,194.02) .. controls (392.52,184.67) and (393.1,177.24) .. (393.93,167.91) ;
\draw [shift={(393.93,167.91)}, rotate = 320.12] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (384.62,194.01) .. controls (382.01,196.7) and (374.73,202.64) .. (371.04,204.2) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (452.42,124.05) .. controls (439.95,136.14) and (440.24,145.45) .. (439.28,152.09) ;
\draw [shift={(439.28,152.09)}, rotate = 143.18] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (449.14,193.89) .. controls (440.24,182.67) and (440.24,176.67) .. (439.57,167.78) ;
\draw [shift={(439.57,167.78)}, rotate = 310.68] [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (-2.24,0) -- (2.24,0)(0,2.24) -- (0,-2.24)   ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (461.15,116) .. controls (458.05,118.31) and (455.38,120.89) .. (452.42,124.02) ;

\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}]  (449.14,193.89) .. controls (451.83,196.59) and (458.95,203.15) .. (464.7,205.33) ;

\draw (374.99,131.56) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize]  {$P_{1}$};

\draw (447.86,130.59) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize]  {$P_{2}$};

\draw (405.24,170.37) node [anchor=north west][inner sep=0.75pt]  [font=\normalsize] [align=left] {glue};
\end{tikzpicture}\,.
\end{equation}
We call this `cylinder surgery', because the 3-manifolds in VTQFT are the complement of a regular neighborhood of the Wilson line network embedded in $M_E$, so that the 2-punctured sphere along which we glue becomes a cylinder. This was illustrated in the introduction in figure \ref{fig:machine1}.

When $P_1$ and $P_2$ belong to two disconnected networks of Wilson lines, corresponding to disjoint manifolds $M_1$ and $M_2$, 
the above construction is similar to a connected sum of 3-manifolds, in which one removes two empty balls and identifies the resulting $\mathrm{S}^2$ boundaries. In this case, cylinder surgery is a generalization of the connected sum of $M_1$ and $M_2$, now including Wilson lines. We will denote it by
\be 
M_1 \#_{P_1 \sim P_2} M_2\ , \label{eq:generalized connected sum}
\ee
with $P_1$ and $P_2$ the Wilson line labels that get identified. 

When the $P_1$ and $P_2$ Wilson lines are part of the same connected VTQFT diagram, with corresponding graph complement $M$, we denote cylinder surgery by
\be
M \#_{P_1 \sim P_2}\,.
\ee 
We will also refer to this as `self-gluing' throughout the rest of the paper.


\paragraph{Reformulating Dehn surgery.} Let us see how the above procedure generalizes the Dehn surgery that we described in section~\ref{subsec:gravitational machine 1}. We can think of the modified manifold in \eqref{eq:dehn surgery picture} as being obtained by applying cylinder surgery to the original manifold $M_1$ (with Wilson line $P_1$), and a genus-1 handlebody $M_2$ (i.e.~one of the $\mathrm{PSL}(2,\mathbb{Z})$-family of solid tori). The fixed-$P$ version of the genus-1 handlebody can be represented in VTQFT as:
\be 
\vcenter{\hbox{
\begin{tikzpicture}[scale=0.8]
    \draw[very thick] (0,-.9) arc (-90:90:.5 and 1) node[black, shift={(.72,-.2)}] {$p/q$};
    \fill[white] (.35,0) rectangle (.65,.12);
    \draw[very thick, wilsonred] (0,1) circle (1.4 and 1);
    \node at (0,1.7) {$P$};
    \fill[white] (-.45,0) rectangle (-.55,.12);
    \draw[very thick] (0,1.1) arc (90:270:.5 and 1);
\end{tikzpicture}
}}
\ee
embedded in $\mathrm{S}^3$.
Thus, we can view the Dehn surgery operation \eqref{eq:dehn surgery picture} on $M_1$ as the result of gluing a genus-1 handlebody to $M_1$ by removing a ball neighborhood around a pair of Wilson lines and identifying the boundaries, that is, $M_1\#_{P_1\sim P_2} M_2$. For example, when $M_1$ is a genus-2 handlebody, we have:
\begin{equation}\label{eq:gluing solid torus}
\vcenter{\hbox{
\begin{tikzpicture}
\draw[very thick, wilsonred] (0,1) -- (0,-1);
\draw[very thick, wilsonred] (0,0) ellipse (2 and 1);
\draw[very thick] (1.9,0.2) arc (100:440:0.35 and 0.25);
\node at (2.3,-0.6) {$p/q$};
\end{tikzpicture}
}}\cong\vcenter{\hbox{
\begin{tikzpicture}
\draw[very thick, wilsonred] (-2,1) -- (-2,-1);
\draw[very thick, wilsonred] (-2,0) ellipse (2 and 1);
\draw[very thick, wilsonred] (2,0) circle (.5);
\draw[very thick] (2.4,0.2) arc (100:440:0.35 and 0.25);
\node at (2.8,-0.6) {$p/q$};
\draw[red, fill=gray, opacity=.75] (0,0) circle (.25);
\draw[red, fill=gray, opacity=.75] (1.5,0) circle (.25);
\draw[very thick,<->,bend left=20] (.2,.2) to node[above] {glue} (1.3,.2);
\end{tikzpicture}
}}\ .
\end{equation}
This requires of course to identify the Wilson line labels of the two Wilson lines that get glued together. On the RHS, before gluing, the genus-1 and genus-2 Wilson line networks are embedded in two disjoint copies of $\mathrm{S}^3$.

\paragraph{Reformulating self-contractions.} Let us also see how cylinder surgery generates the bulk manifolds discussed in section \ref{subsec:gravitational machine 1} that contribute to the index contractions predicted by typicality. In the examples given in \eqref{eq:handlebody contribution} and \eqref{eq:41prime}, we used the $\Omega$-loop encircling a pair of Wilson lines to produce the delta function $\delta(P_1-P_2)$. Topologically, this is equivalent to doing the cylinder surgery described above, see also~\eqref{eq:omega loop on pair of lines}.

For example, the non-handlebody manifold \eqref{eq:41prime} that contributes to the double self-contraction $\overline{C_{111}C_{111}}$ can also be constructed from the following self-gluing: 
\begin{equation}\label{eq:4_1 from surgery}
\tikzset{every picture/.style={line width=1.2pt}} 
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
\end{tikzpicture} \quad \cong \quad
\tikzset{every picture/.style={line width=0.75pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw [color=wilsonred  ,draw opacity=1 ][line width=1.2]    (170.25,150) -- (170.25,229.63) ;

\draw  [color=wilsonred  ,draw opacity=1 ][line width=1.2]  (126.34,189.81) .. controls (126.34,167.82) and (146,150) .. (170.25,150) .. controls (194.51,150) and (214.17,167.82) .. (214.17,189.81) .. controls (214.17,211.8) and (194.51,229.63) .. (170.25,229.63) .. controls (146,229.63) and (126.34,211.8) .. (126.34,189.81) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (117.55,177.25) .. controls (117.55,171.3) and (122.72,166.47) .. (129.09,166.47) .. controls (135.47,166.47) and (140.63,171.3) .. (140.63,177.25) .. controls (140.63,183.2) and (135.47,188.03) .. (129.09,188.03) .. controls (122.72,188.03) and (117.55,183.2) .. (117.55,177.25) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (158.71,177.25) .. controls (158.71,171.3) and (163.88,166.47) .. (170.25,166.47) .. controls (176.63,166.47) and (181.8,171.3) .. (181.8,177.25) .. controls (181.8,183.2) and (176.63,188.03) .. (170.25,188.03) .. controls (163.88,188.03) and (158.71,183.2) .. (158.71,177.25) -- cycle ;

\draw [line width=1.2]    (135.04,182.08) .. controls (141.88,185.44) and (155.9,185.64) .. (163.49,182.33) ;
\draw [shift={(166.83,180.25)}, rotate = 148.89] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;
\draw [shift={(131.83,179.58)}, rotate = 36.76] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (159.3,205.75) .. controls (159.3,199.8) and (164.47,194.97) .. (170.84,194.97) .. controls (177.22,194.97) and (182.38,199.8) .. (182.38,205.75) .. controls (182.38,211.7) and (177.22,216.53) .. (170.84,216.53) .. controls (164.47,216.53) and (159.3,211.7) .. (159.3,205.75) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.72 ] (200.71,205.75) .. controls (200.71,199.8) and (205.88,194.97) .. (212.25,194.97) .. controls (218.63,194.97) and (223.8,199.8) .. (223.8,205.75) .. controls (223.8,211.7) and (218.63,216.53) .. (212.25,216.53) .. controls (205.88,216.53) and (200.71,211.7) .. (200.71,205.75) -- cycle ;

\draw [line width=1.5]    (179.54,210.58) .. controls (186.38,213.94) and (200.4,214.14) .. (207.99,210.83) ;
\draw [shift={(211.33,208.75)}, rotate = 148.89] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;
\draw [shift={(176.33,208.08)}, rotate = 36.76] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (4.64,-2.23) -- (0,0) -- (4.64,2.23) -- cycle    ;

\draw (141.89,158.92) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (172.25,153.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};

\draw (195.76,163.34) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}\,.
\end{equation}

This can be seen from the figure \eqref{eq:cylinder surgery} by slicing it horizontally through the middle. In the top half of the figure, take the hemispheres punctured by $P_1$ and $P_2$ and puff up the Wilson lines so that the punctured hemispheres becomes annuli. When we glue, these become a torus. Doing the same with the bottom half of the figure, we get two tori that are glued to each other with the identity map, thus making the background manifold $\mathrm{S}^2\times \mathrm{S}^1$. This is precisely what the $\Omega$-loop implements. 


\paragraph{Cylinder surgery in VTQFT.}  
In cylinder surgery, we glue along a 2-punctured 2-sphere. The corresponding Hilbert space in VTQFT is one-dimensional  (provided that the labels of the Wilson lines agree). Thus the gravitational path integral in $M_1$ and $M_2$ has to produce the unique state up to proportionality and we obtain:
\be\label{eq:VTQFT generalized connected sum}
Z_\text{Vir}[M_1 \#_{P_1 \sim P_2} M_2]=\frac{\delta(P_1-P_2)}{\rho_0(P_1)}\, Z_\text{Vir}[M_1]Z_\text{Vir}[M_2].
\ee 
The proportionality constant $\rho_0(P_1)^{-1}$ can be understood in two ways. First, after surgery we have one edge less in the VTQFT diagram, so the normalization factor $\rho^{\mathcal{C}}_g(\boldsymbol{P})$ should get one fewer factor of $\rho_0$. Second, 
we note that for $M_1$ and $M_2$ both unknots in $\mathrm{S}^3$, the connected sum is also an unknot in $\mathrm{S}^3$. Using that $Z_\text{Vir}(\text{unknot})=\rho_0(P)$ explains the proportionality factor.\footnote{We may regard (\ref{eq:VTQFT generalized connected sum}) as the VTQFT analog of the identity for the partition function on manifolds constructed as connected sums in ordinary TQFTs (e.g.~based on a modular tensor category). In particular, for $M = M_1 \# M_2$, we have $Z_{\text{TQFT}}(M) = \tfrac{Z_{\text{TQFT}}(M_1)Z_{\text{TQFT}}(M_2)}{Z_{\text{TQFT}}(\mathrm{S}^3)}$. This equation is derived by carving out a three-ball from each of $M_1$ and $M_2$ and gluing them along the resulting $\mathrm{S}^2$ boundaries. This operation is not allowed in VTQFT: the Hilbert space on the naked $\mathrm{S}^2$ is ill-defined, the total quantum dimension badly diverges, and indeed hyperbolic manifolds are prime and so cannot be written as connected sums anyway. However the generalization with Wilson lines \eqref{eq:generalized connected sum} as implemented by (\ref{eq:VTQFT generalized connected sum}) does (under certain conditions) lead to hyperbolic manifolds, as we shall see below.}

For self-gluing, the same reasoning gives:
\be\label{eq:VTQFT self gluing}
Z_\text{Vir}[M \#_{P_1 \sim P_2} ;P_1,P_2,\dots]=\frac{\delta(P_1-P_2)}{\rho_0(P_1)}\, Z_\text{Vir}[M;P_1,P_1,\dots].
\ee 
In the special case that $M = M_1\sqcup M_2$ is a disjoint union, we recover \eqref{eq:VTQFT generalized connected sum}.


\paragraph{Statistical interpretation.} Cylinder surgery has a clear interpretation from the boundary ensemble point of view. Namely, 
consider some moment $\overline{XY}$, where $X$ and $Y$ are products of OPE coefficients and densities of states. $\overline{XY}$ necessarily includes the disconnected moment $\overline{X}\, \overline{Y}$, which is described gravitationally by considering the disconnected union of the set of manifolds computing the lower moments $\overline{X}$ and $\overline{Y}$. Now, the typicality assumption also forces us to include connected contractions of the indices in $X$ and $Y$, which are constructed in the bulk via cylinder surgery. That is, let $M_1$ be a manifold contributing to $\overline{X}$ and $M_2$ a manifold contributing to $\overline{Y}$. Then we should add to $\overline{XY}$ the manifold corresponding to the diagonal contraction by excising a ball around two Wilson lines and identifying their boundaries, i.e.~applying the cylinder surgery $M_1 \#_{P_1 \sim P_2} M_2$ as above.



\paragraph{Adding crossing transformations.} Once we have added a new topology $M$ that was obtained using cylinder surgery, such as the $\mathbf{4}_1$ handlebody-knot in \eqref{eq:4_1 from surgery}, we must also include its sum over mapping class group images in order to preserve crossing symmetry. More precisely, we sum over the boundary mapping class group modulo the bulk diffeomorphisms of $M$, i.e.~the coset \cite{Collier:2023fwi}:
\begin{equation}\label{eq:MCG coset}
\text{MCG}(\partial M) / \text{MCG}(M, \partial M).
\end{equation}
Here $\text{MCG}(M, \partial M)$ is the bulk mapping class group of $M$, containing the large diffeomorphisms of $M$ that preserve the boundary setwise. On the level of the VTQFT diagrams, this means we can act with any of the crossing transformations $\mathbb{B}$, $\mathbb{F}$ and $\mathbb{S}$, as in equations \eqref{eq:Z_vir braiding}, \eqref{eq:RHScrossing} and \eqref{eq:omegaloop}, up to the relations of the Moore-Seiberg groupoid and the identifications by the bulk mapping class group. 

Crucially, these crossing transformations map VTQFT partition functions with delta functions $\delta(P_i-P_j)$ to partition functions without delta functions. For example, recall the $\mathbf{4}_1$ handlebody-knot \eqref{eq:41prime}, which is a contribution to the double contraction $\overline{C_{111}C_{111}}$. If we act with S-transforms on its bells, we get a smooth function of $P_{1,2,3}$ that is a product of two S-kernels, written in \eqref{eq:vir41-2} and further analyzed there. Hence, crossing symmetry combined with typicality predicts a non-handlebody contribution to $\overline{C_{112}C_{233}}$, even when $P_{1,2,3}$ are all different.

Similarly, recall the Dehn surgery \eqref{eq:dehn surgery picture}, which was needed in order to reproduce the correct factors of $\rho_{\text{MWK}}$ as in \eqref{eq: sunset surgery}. Acting with crossing transformations on the VTQFT diagram gives an amplitude that is no longer of the factorized form \eqref{eq:factorizegenus2}; hence a new $\text{PSL}(2,\mathbb{Z})$-family of Dehn surgeries must be added for consistency with modular invariance of the lower moments $\overline{\rho_i}$. To illustrate this, consider the sunset diagram (with Dehn surgery) and act with an $\mathbb{F}$ move:
\begin{equation}
    \vcenter{\hbox{
\begin{tikzpicture}[yscale=1,xscale=0.75]
\draw[very thick, wilsonred] (0,1) -- (0,-1);
\draw[very thick, wilsonred] (0,0) ellipse (2 and 1);
\draw[very thick] (-0.07,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\gamma_2$}};
\draw[very thick] (-2,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\gamma_1$}};
\draw[very thick] (1.9,0.2) arc (100:440:0.35 and 0.25)
node[right, black]{{\,$\gamma_3$}};
\draw (0.1,-0.5) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$2$};
\draw (-1.4,-0.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};
\draw (1,-0.9) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};
\end{tikzpicture}
}} \,\,\xrightarrow[]{\quad\mathbb{F}_{24}\quad} \,\,\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.4,xscale=1.4,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw [color=wilsonred  ,draw opacity=1 ]   (178.67,144.07) .. controls (186.39,117.21) and (232.1,120.07) .. (238.67,144.07) ;

\draw  [draw opacity=0] (189.75,169.18) .. controls (187.01,172.19) and (183.06,174.07) .. (178.67,174.07) .. controls (170.39,174.07) and (163.67,167.36) .. (163.67,159.07) .. controls (163.67,150.79) and (170.39,144.07) .. (178.67,144.07) .. controls (186.96,144.07) and (193.67,150.79) .. (193.67,159.07) .. controls (193.67,160.93) and (193.33,162.7) .. (192.72,164.34) -- (178.67,159.07) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (189.75,169.18) .. controls (187.01,172.19) and (183.06,174.07) .. (178.67,174.07) .. controls (170.39,174.07) and (163.67,167.36) .. (163.67,159.07) .. controls (163.67,150.79) and (170.39,144.07) .. (178.67,144.07) .. controls (186.96,144.07) and (193.67,150.79) .. (193.67,159.07) .. controls (193.67,160.93) and (193.33,162.7) .. (192.72,164.34) ;  

\draw  [draw opacity=0] (224.55,164.14) .. controls (223.98,162.55) and (223.67,160.85) .. (223.67,159.07) .. controls (223.67,150.79) and (230.39,144.07) .. (238.67,144.07) .. controls (246.96,144.07) and (253.67,150.79) .. (253.67,159.07) .. controls (253.67,167.36) and (246.96,174.07) .. (238.67,174.07) .. controls (234.28,174.07) and (230.32,172.18) .. (227.58,169.17) -- (238.67,159.07) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (224.55,164.14) .. controls (223.98,162.55) and (223.67,160.85) .. (223.67,159.07) .. controls (223.67,150.79) and (230.39,144.07) .. (238.67,144.07) .. controls (246.96,144.07) and (253.67,150.79) .. (253.67,159.07) .. controls (253.67,167.36) and (246.96,174.07) .. (238.67,174.07) .. controls (234.28,174.07) and (230.32,172.18) .. (227.58,169.17) ;  

\draw  [draw opacity=0] (226.68,156.55) .. controls (232.62,157.78) and (236.39,159.61) .. (236.39,161.64) .. controls (236.39,165.35) and (223.91,168.36) .. (208.53,168.36) .. controls (193.14,168.36) and (180.67,165.35) .. (180.67,161.64) .. controls (180.67,159.57) and (184.58,157.71) .. (190.72,156.48) -- (208.53,161.64) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (226.68,156.55) .. controls (232.62,157.78) and (236.39,159.61) .. (236.39,161.64) .. controls (236.39,165.35) and (223.91,168.36) .. (208.53,168.36) .. controls (193.14,168.36) and (180.67,165.35) .. (180.67,161.64) .. controls (180.67,159.57) and (184.58,157.71) .. (190.72,156.48) ;  

\draw  [draw opacity=0] (197.52,155.47) .. controls (200.9,155.12) and (204.62,154.93) .. (208.53,154.93) .. controls (212.92,154.93) and (217.08,155.17) .. (220.78,155.61) -- (208.53,161.64) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ] (197.52,155.47) .. controls (200.9,155.12) and (204.62,154.93) .. (208.53,154.93) .. controls (212.92,154.93) and (217.08,155.17) .. (220.78,155.61) ;  

\draw  [draw opacity=0] (168.59,155.1) .. controls (169.41,156.2) and (169.9,157.57) .. (169.9,159.06) .. controls (169.9,162.63) and (167.08,165.53) .. (163.6,165.53) .. controls (160.12,165.53) and (157.3,162.63) .. (157.3,159.06) .. controls (157.3,155.71) and (159.78,152.95) .. (162.95,152.62) -- (163.6,159.06) -- cycle ; \draw   (168.59,155.1) .. controls (169.41,156.2) and (169.9,157.57) .. (169.9,159.06) .. controls (169.9,162.63) and (167.08,165.53) .. (163.6,165.53) .. controls (160.12,165.53) and (157.3,162.63) .. (157.3,159.06) .. controls (157.3,155.71) and (159.78,152.95) .. (162.95,152.62) ;  

\draw  [draw opacity=0] (254.09,152.39) .. controls (254.15,152.38) and (254.21,152.38) .. (254.27,152.38) .. controls (257.75,152.38) and (260.57,155.28) .. (260.57,158.86) .. controls (260.57,162.43) and (257.75,165.33) .. (254.27,165.33) .. controls (250.79,165.33) and (247.97,162.43) .. (247.97,158.86) .. controls (247.97,156.66) and (249.03,154.72) .. (250.67,153.54) -- (254.27,158.86) -- cycle ; \draw   (254.09,152.39) .. controls (254.15,152.38) and (254.21,152.38) .. (254.27,152.38) .. controls (257.75,152.38) and (260.57,155.28) .. (260.57,158.86) .. controls (260.57,162.43) and (257.75,165.33) .. (254.27,165.33) .. controls (250.79,165.33) and (247.97,162.43) .. (247.97,158.86) .. controls (247.97,156.66) and (249.03,154.72) .. (250.67,153.54) ;  

\draw (160.67,136.4) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$1$};

\draw (204.6,126.8) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$4$};

\draw (250.07,137) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize]  {$3$};

\draw (202.6,170) node [anchor=north west][inner sep=0.75pt]    {$\gamma _{2}$};

\draw (144.27,157.57) node [anchor=north west][inner sep=0.75pt]    {$\gamma _{1}$};

\draw (261.43,157.4) node [anchor=north west][inner sep=0.75pt]    {$\gamma_{3}$};
\end{tikzpicture}\,.
\end{equation}
Here $\gamma_i$ specify the Dehn surgery parameters, which we assume to be non-trivial. On the RHS, the VQTFT amplitude is not of the factorized form $\bar \rho_1 \,\bar \rho_3\, \bar \rho_4 \,\overline{C_{114}C_{334}}$. At the same time, the  Dehn filling $\gamma_2$ has resulted in a new non-contractible cycle, namely the loop surrounding the $P_4$ edge. We can restore the factorized form by adding a fourth Dehn surgery around this loop and summing over $\gamma_4\in \PSL(2,\ZZ)/\ZZ$. Iterating this procedure generates more and more complicated contributions to the sum over geometries, e.g.:\vspace{-0.3cm}
\begin{equation}\label{eq:adding crossing}
\vcenter{\hbox{
\begin{tikzpicture}[yscale=1,xscale=0.7]
\draw[very thick, wilsonred] (0,1) -- (0,-1);
\draw[very thick, wilsonred] (0,0) ellipse (2 and 1);
\draw[very thick] (-0.07,0.2) arc (100:440:0.35 and 0.25) node[right,black] {$\gamma_2$};
\end{tikzpicture}
}} \,\,\rightarrow\,\,
\vcenter{\hbox{
\begin{tikzpicture}
    \draw[very thick] (0,0) ellipse (0.8 and 0.3) node[black] {$\gamma_2$};
    \draw[line width=4, white] ({-1+0.5*cos{-15}},{0.5*sin{-15}})  arc (-15:300:0.5);
    \draw[very thick, wilsonred] ({-1+0.5*cos{-15}},{0.5*sin{-15}})  arc (-15:320:0.5);
    \draw[line width=4, white] ({1+0.5*cos{-145}},{0.5*sin{-145}})  arc (-145:190:0.5);
    \draw[very thick, wilsonred] ({1+0.5*cos{-145}},{0.5*sin{-145}})  arc (-145:190:0.5);
    \draw[very thick,red] (-1,0.5) to[out = 90,in=90,looseness=1.5] (1,0.5);
    \draw[very thick] (0.15,1.45) arc (15:345:0.2 and 0.3) node[above right, black] {$\gamma_4$};
\end{tikzpicture}
}}
\,\,\rightarrow\,\,
\vcenter{\hbox{
\begin{tikzpicture}[yscale=1,xscale=0.75,baseline={([yshift=10ex]current bounding box.south)}
]
\draw[very thick, wilsonred] (0,1) -- (0,-1);
\draw[very thick, wilsonred] (0,0) ellipse (2 and 1);
\draw[very thick] (-0.07,0.2) arc (100:440:0.35 and 0.25) node[right,black] {$\gamma_5$};
\draw[very thick] (0,-1.75) arc (-90:90:0.2 and 0.3);
\draw[line width=4, white] (-0.5,-1.01) arc (180:360:0.5 and 0.3);
\draw[line width=4, white] (-0.9,-1) arc (180:360:0.9 and 0.6);
\draw[very thick] (-0.5,-1.01) arc (180:360:0.5 and 0.3);
\draw[very thick] (-0.9,-1) arc (180:360:0.9 and 0.6);
\draw[very thick] (-0.9,-1) arc (180:25:0.2);
\draw[very thick] (0.9,-1) arc (0:155:0.2);
\draw[line width=4, white] (0,-1.75) arc (270:90:0.2 and 0.3);
\draw[very thick] (0,-1.75) arc (270:90:0.2 and 0.3);
\node at (-1.2,-1.1) {$\gamma_2$};
\node at (0,-2) {$\gamma_4$};
\end{tikzpicture}
}} \rightarrow \;\; \cdots
\end{equation}
This mechanism applies to any VTQFT diagram and will be an essential ingredient in the formulation of the gravitational machine, to which we turn next.

\paragraph{The general gravitational machine.} Having introduced all the necessary ingredients, we come to formulate the general gravitational machine, which produces a set of manifolds $\mathcal{M}$ consistent with all properties of the boundary statistical ensemble that we imposed in section~\ref{sec:2}. The idea is to give a finite set of `moves' which inductively define a set of orientable 3-manifolds\footnote{$\mathcal{M}$ can in principle also contain manifolds with conical defects described by light Wilson lines. However, here we will restrict ourselves to the `pure' gravity case without defects.}
\be 
M \in \mathcal{M}\,.
\ee
As an initial condition, we assume that $\mathcal{M}$ contains all handlebodies of genus $g$, which is the minimal set needed for consistency with crossing. From this initial set, we define a finite number of operations that produce new manifolds, which we also have to include in the sum over topologies for consistency with the other conditions imposed in section \ref{sec:2} (including the ones discussed above). We will again think of the resulting manifolds at the level of networks of Wilson lines (i.e.~in the fixed-$P$ formalism), but they can as always be thickened to pass to the canonical ensemble.

The three moves of the gravitational machine are as follows:
\begin{enumerate}
    \item For $M_1$ and $M_2$ in $\mathcal{M}$, the disconnected manifold $M_1 \sqcup M_2$ is also allowed. \label{move:disconnected sum}
    \item For any $M \in \mathcal{M}$, we are allowed to perform crossing transformations on the Wilson line network representing the boundary data.\label{move:crossing}
    \item For $M\in \mathcal{M}$, we can apply the cylinder surgery $M \#_{P_1 \sim P_2}$ on any pair of Wilson lines, where $P_1$ and $P_2$ are identified. This surgery can either glue different connected components of $M$ or it can glue the same component to itself. \label{move:gluing}
\end{enumerate}
For the third move, we have to make some additional technical assumptions that we discuss below. Next,
for each application of one of these moves, one should check\footnote{Hyperbolic manifolds are completely specified topologically by their fundamental group $\pi_1(M)$. Since the machine generates only hyperbolic manifolds (as we will show), checking homeomorphism comes down to testing for isomorphism of the fundamental group. This can be highly non-trivial in practice, see for example the computation in appendix \ref{subapp:fundamental group}.} whether the resulting topology is already part of the set $\mathcal{M}$, and if not, add it to $\mathcal{M}$. This algorithm generates an infinite set of bulk manifolds. Then, when we compute the average of any CFT quantity $\overline{Z[\Sigma]}$ (where $\Sigma$ may be disconnected), we use the dictionary \eqref{eq:sumovertopologies} to sum over all $M\in \mathcal{M}$ with $\partial M = \Sigma$. 

This defines a minimal sum over topologies that is consistent with the statistical bootstrap defined in section \ref{sec:2}. From the point of view of the statistical description of the boundary CFT$_2$, move~\ref{move:disconnected sum} ensures that any statistical moment $\overline{XY}$ contains at least the disconnected contribution $ \overline{X}\,\overline{Y}$, which always exists. Move \ref{move:crossing} ensures crossing symmetry of each moment, as defined in \eqref{eq:crossingOPE}. Lastly, move \ref{move:gluing} ensures that all index contractions exist as demanded by typicality \eqref{eq:generaltypicality}. 

There are three more technical conditions that we have to impose on the cylinder surgery operation $M \#_{P_1 \sim P_2}$ in move \ref{move:gluing}. Namely, consider the Wilson lines $P_1$ and $P_2$ in the manifold $M$ before gluing, and let $m_1$ and $m_2$ be loops around these Wilson lines. These loops define elements of the fundamental group $\pi_1(M)$.\footnote{For $M$ disconnected, say $M=M_1 \sqcup M_2$ with $m_1$ a loop in $M_1$ and $m_2$ a loop in $M_2$, they define elements in $\pi_1(M_1)$ and $\pi_1(M_2)$ respectively.} We assume that these group elements satisfy the following conditions:
\begin{enumerate}[label=\alph*)]
        \item \label{cond:no Omega loops 2} $m_1$ and $m_2$ are not contractible. In other words, the elements they define in $\pi_1(M)$ are non-trivial. 
        \item \label{cond:no parallel rings 2} $m_1$ \emph{or} $m_2$ is primitive, i.e.~not a power of another element in $\pi_1(M)$.
        \item \label{cond:no Wilson line self gluing} For self-gluings, i.e.~where $m_1$ and $m_2$ are in the same connected component, $\langle m_1 \rangle$ does not have a non-trivial intersection with a conjugate of $\langle m_2 \rangle$ in $\pi_1(M)$. 
\end{enumerate}
The first condition \ref{cond:no Omega loops 2} means that neither $m_1$ nor $m_2$ are $\Omega$-loops, since they are not contractible in the bulk. If either $m_1$ or $m_2$ would be contractible, i.e.~bound a disk, then the Wilson line label is projected to the identity Wilson line.\footnote{For example, this happens for the middle edge of the dumbbell diagram as illustrated in \eqref{eq:contractible dumbbell}.}
However, the identity does not behave in a statistical way since it is constant throughout the ensemble. In particular, for the typicality ansatz \eqref{eq:genus2typicality} it was assumed that all operators are different from the identity, because for OPE coefficients with an identity $C_{\id 23}$ the right hand side is simply dictated by conformal symmetry. So condition \ref{cond:no Omega loops 2} is natural from the ensemble point of view. 

The second condition \ref{cond:no parallel rings 2}  appears from requiring that we do not include disconnected moments more than once. To see why this is necessary, consider a Wilson line that has already been Dehn filled, and apply a second Dehn surgery:
\be \label{cond:no parallel rings}
\tikzset{every picture/.style={line width=1.2pt}} 
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.4,xscale=1.4,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (171.69,142.23) .. controls (171.12,147.23) and (168.52,151) .. (165.4,151) .. controls (161.87,151) and (159,146.16) .. (159,140.2) .. controls (159,134.24) and (161.87,129.4) .. (165.4,129.4) .. controls (168.3,129.4) and (170.75,132.66) .. (171.54,137.13) -- (165.4,140.2) -- cycle ; \draw   (171.69,142.23) .. controls (171.12,147.23) and (168.52,151) .. (165.4,151) .. controls (161.87,151) and (159,146.16) .. (159,140.2) .. controls (159,134.24) and (161.87,129.4) .. (165.4,129.4) .. controls (168.3,129.4) and (170.75,132.66) .. (171.54,137.13) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (140,140) -- (156.6,140) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (162.4,140) -- (185.4,140) ;

\draw  [draw opacity=0] (270.09,142.63) .. controls (269.52,147.63) and (266.92,151.4) .. (263.8,151.4) .. controls (260.27,151.4) and (257.4,146.56) .. (257.4,140.6) .. controls (257.4,134.64) and (260.27,129.8) .. (263.8,129.8) .. controls (266.7,129.8) and (269.15,133.06) .. (269.94,137.53) -- (263.8,140.6) -- cycle ; \draw   (270.09,142.63) .. controls (269.52,147.63) and (266.92,151.4) .. (263.8,151.4) .. controls (260.27,151.4) and (257.4,146.56) .. (257.4,140.6) .. controls (257.4,134.64) and (260.27,129.8) .. (263.8,129.8) .. controls (266.7,129.8) and (269.15,133.06) .. (269.94,137.53) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (245.4,140) -- (255,140) ;

\draw [color=wilsonred  ,draw opacity=1 ]   (260.8,140) -- (273.8,140) ;

\draw  [draw opacity=0] (289.29,142.63) .. controls (288.72,147.63) and (286.12,151.4) .. (283,151.4) .. controls (279.47,151.4) and (276.6,146.56) .. (276.6,140.6) .. controls (276.6,134.64) and (279.47,129.8) .. (283,129.8) .. controls (285.9,129.8) and (288.35,133.06) .. (289.14,137.53) -- (283,140.6) -- cycle ; \draw   (289.29,142.63) .. controls (288.72,147.63) and (286.12,151.4) .. (283,151.4) .. controls (279.47,151.4) and (276.6,146.56) .. (276.6,140.6) .. controls (276.6,134.64) and (279.47,129.8) .. (283,129.8) .. controls (285.9,129.8) and (288.35,133.06) .. (289.14,137.53) ;  

\draw [color=wilsonred  ,draw opacity=1 ]   (279.6,140) -- (303.8,140) ;

\draw (162.37,117) node [anchor=north west][inner sep=0.75pt]    {$\gamma _{1}$};

\draw (190.8,129) node [anchor=north west][inner sep=0.75pt]    {$\xrightarrow{\text{not allowed}} $};

\draw (252.77,117) node [anchor=north west][inner sep=0.75pt]    {$\gamma _{1}$};

\draw (281.57,117) node [anchor=north west][inner sep=0.75pt]    {$\gamma _{2}$};
\end{tikzpicture}\,
\ee
Using \eqref{eq:complete to MWK}, this Dehn surgery along parallel loops would lead to the enhancement of $\rho_0(P)\rho_0(\bar P)$ to the \emph{square} of $\rho_{\text{MWK}}(P,\bar P)$, which does not make sense from the CFT point of view. To see why the condition \ref{cond:no parallel rings 2} forbids the move in \eqref{cond:no parallel rings}, we note that 
on the LHS, after a single Dehn filling $p/q$, the loop around the Wilson line admits a $p$-th root and is no longer primitive as an element of $\pi_1$. The converse also holds: if a loop around a Wilson line is not primitive, then we can write the geometry as a Dehn filling of a simpler geometry where the loop is primitive. Thus primitivity of the loop around the Wilson line formalizes the notion of a Dehn filling already being present, which explains condition \ref{cond:no parallel rings 2}.\footnote{We remark that it can be non-trivial to ascertain whether a parallel Dehn-filled arc already exists, since this is in principle a complicated topological condition and the parallel arc might be knotted in non-trivial ways. The cleanest way to formulate this condition is in terms of the fundamental group, which is what we have done in condition \ref{cond:no parallel rings 2}.}

The third condition \ref{cond:no Wilson line self gluing} simply says that we are not allowed to glue the same Wilson line to itself, since that would clearly not make sense from a boundary statistical viewpoint. The phrasing in \ref{cond:no Wilson line self gluing} of this simple statement is a bit technical, due to the fact that $m_1$ and $m_2$ are only defined up to conjugation and thus we have to demand that $m_1$ is not conjugate to $m_2$. In fact, we required the slightly stronger condition that powers of $m_1$ are also not conjugate to powers of $m_2$. This says that we are also not allowed to glue a Wilson line to a power of itself, i.e.~to a loop that winds several times around the same Wilson line.
