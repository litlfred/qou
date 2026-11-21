---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-007-the-mapping-class-group
section_title: "The mapping class group"
section_number: null
pages: 22-24
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.864
latex_coverage_ratio: 1.0
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
In general, a 3-dimensional handlebody $M$ of genus $g$ is defined by gluing $g$ 1-handles to a 3-ball. Its boundary is a genus-$g$ Riemann surface $\Sigma_g$, with a collection of $3g-3$ non-intersecting closed curves that bound disks in $M$. These essential curves are also called contractible cycles, or meridians. An example at genus 2 is shown below:
\begin{equation}\label{eq:genus2handlebody}
\tikzset{every picture/.style={line width=0.8pt}}
\begin{tikzpicture}
[x=0.75pt,y=0.75pt,yscale=-1.4,xscale=1.4,baseline={([yshift=-0.5ex]current bounding box.center)}]


\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (230.73,206.33) .. controls (230.8,206.32) and (230.88,206.32) .. (230.96,206.32) .. controls (234.74,206.32) and (237.81,215.11) .. (237.81,225.95) .. controls (237.81,236.79) and (234.74,245.59) .. (230.96,245.59) .. controls (230.76,245.59) and (230.56,245.56) .. (230.37,245.51) -- (230.96,225.95) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (230.73,206.33) .. controls (230.8,206.32) and (230.88,206.32) .. (230.96,206.32) .. controls (234.74,206.32) and (237.81,215.11) .. (237.81,225.95) .. controls (237.81,236.79) and (234.74,245.59) .. (230.96,245.59) .. controls (230.76,245.59) and (230.56,245.56) .. (230.37,245.51) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (232.06,245.33) .. controls (231.7,245.5) and (231.34,245.59) .. (230.96,245.59) .. controls (227.18,245.59) and (224.11,236.79) .. (224.11,225.95) .. controls (224.11,215.11) and (227.18,206.32) .. (230.96,206.32) .. controls (231.34,206.32) and (231.71,206.4) .. (232.07,206.57) -- (230.96,225.95) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (232.06,245.33) .. controls (231.7,245.5) and (231.34,245.59) .. (230.96,245.59) .. controls (227.18,245.59) and (224.11,236.79) .. (224.11,225.95) .. controls (224.11,215.11) and (227.18,206.32) .. (230.96,206.32) .. controls (231.34,206.32) and (231.71,206.4) .. (232.07,206.57) ;  

\draw    (152.53,226.25) .. controls (152.68,199.95) and (173.96,192.65) .. (188.02,193) .. controls (206.09,193.35) and (216.48,206.45) .. (230.54,206.35) .. controls (244.84,206.48) and (255.72,193.17) .. (273.09,193.08) .. controls (287.39,193.2) and (308.65,199.88) .. (308.5,226.4) .. controls (308.59,253.36) and (287.31,260) .. (273.02,259.65) .. controls (255.88,259.75) and (244.79,246.2) .. (230.49,246.3) .. controls (216.43,246.39) and (205.78,259.7) .. (187.94,259.57) .. controls (174.12,259.89) and (152.86,253.21) .. (152.53,226.25) -- cycle ;

\draw    (173.94,226.63) .. controls (179.38,215) and (201.27,213.63) .. (210.49,225.98) ;

\draw    (173.94,226.63) .. controls (180.49,238.29) and (204.83,238.1) .. (210.49,225.98) ;

\draw    (250.24,226.59) .. controls (256.37,215) and (279.04,214.32) .. (286.79,225.94) ;

\draw    (250.24,226.59) .. controls (260.51,237.86) and (281.07,236.2) .. (286.79,225.94) ;

\draw    (250.24,226.59) .. controls (249.67,225.85) and (249.48,225.76) .. (249.08,224.77) ;

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (152.84,226.36) .. controls (152.83,226.23) and (152.82,226.11) .. (152.82,225.98) .. controls (152.82,222.51) and (157.56,219.69) .. (163.41,219.69) .. controls (169.26,219.69) and (174,222.51) .. (174,225.98) .. controls (174,226.51) and (173.89,227.02) .. (173.68,227.52) -- (163.41,225.98) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (152.84,226.36) .. controls (152.83,226.23) and (152.82,226.11) .. (152.82,225.98) .. controls (152.82,222.51) and (157.56,219.69) .. (163.41,219.69) .. controls (169.26,219.69) and (174,222.51) .. (174,225.98) .. controls (174,226.51) and (173.89,227.02) .. (173.68,227.52) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (173.78,224.69) .. controls (173.93,225.11) and (174,225.54) .. (174,225.98) .. controls (174,229.45) and (169.26,232.26) .. (163.41,232.26) .. controls (157.56,232.26) and (152.82,229.45) .. (152.82,225.98) .. controls (152.82,225.6) and (152.88,225.23) .. (152.99,224.87) -- (163.41,225.98) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (173.78,224.69) .. controls (173.93,225.11) and (174,225.54) .. (174,225.98) .. controls (174,229.45) and (169.26,232.26) .. (163.41,232.26) .. controls (157.56,232.26) and (152.82,229.45) .. (152.82,225.98) .. controls (152.82,225.6) and (152.88,225.23) .. (152.99,224.87) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1.5]  (286.47,225.27) .. controls (286.97,222.06) and (291.63,219.55) .. (297.3,219.55) .. controls (303.1,219.55) and (307.83,222.17) .. (308.17,225.47) -- (297.3,225.84) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (286.47,225.27) .. controls (286.97,222.06) and (291.63,219.55) .. (297.3,219.55) .. controls (303.1,219.55) and (307.83,222.17) .. (308.17,225.47) ;  

\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (308.04,224.83) .. controls (308.14,225.16) and (308.19,225.49) .. (308.19,225.84) .. controls (308.19,229.31) and (303.31,232.13) .. (297.3,232.13) .. controls (291.29,232.13) and (286.42,229.31) .. (286.42,225.84) .. controls (286.42,225.5) and (286.47,225.16) .. (286.56,224.83) -- (297.3,225.84) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}][line width=1.5]  (308.04,224.83) .. controls (308.14,225.16) and (308.19,225.49) .. (308.19,225.84) .. controls (308.19,229.31) and (303.31,232.13) .. (297.3,232.13) .. controls (291.29,232.13) and (286.42,229.31) .. (286.42,225.84) .. controls (286.42,225.5) and (286.47,225.16) .. (286.56,224.83) ;  

\draw    (210.49,225.98) .. controls (211.01,225.07) and (211.19,224.18) .. (211.36,223.62) ;
\end{tikzpicture}
\end{equation}
where the compressible disks chosen in this example have been shaded gray. 
The contractible cycles are associated to the Teichm\"uller parameters that specify the conformal structure moduli at the boundary. If we fix the values of these moduli, the handlebody carries a hyperbolic metric (i.e.~of constant negative curvature) with infinite volume, which is unique up to isometry \cite{Sullivan1981ErgodicInfinity}.  

There are three important groups associated to a handlebody. The first is the fundamental group $\pi_1(M)$, which for a handlebody is isomorphic to the free group on $g$ generators. The second is the mapping class group of the boundary surface:
\begin{equation}
    \text{MCG}(\Sigma_g) = \frac{\text{Diff}^+(\Sigma_g)}{\text{Diff}_0(\Sigma_g)}
\end{equation}
where the numerator is the group of orientation preserving diffeomorphisms of $\Sigma_g$ and the denominator is the subgroup of diffeomorphisms that are continuously connected to the identity. A famous theorem by Lickorish states that the mapping class group is generated by a finite collection of Dehn twists \cite{Lickorish_1964}. A Dehn twist $T$ is a local operation on a cylinder neighborhood of a closed curve $C$, where the cylinder is cut along $C$ and reglued after a rotation by $2\pi$:\vspace{2mm}
\begin{equation}\label{eq:Dehntwist}
T:\quad\tikzset{every picture/.style={line width=0.8pt}}
    \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (200.15,160) .. controls (200.1,160) and (200.05,160) .. (200,160) .. controls (194.48,160) and (190,142.09) .. (190,120) .. controls (190,97.91) and (194.48,80) .. (200,80) .. controls (200.05,80) and (200.09,80) .. (200.14,80) -- (200,120) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (200.15,160) .. controls (200.1,160) and (200.05,160) .. (200,160) .. controls (194.48,160) and (190,142.09) .. (190,120) .. controls (190,97.91) and (194.48,80) .. (200,80) .. controls (200.05,80) and (200.09,80) .. (200.14,80) ; 

\draw   (90,120) .. controls (90,97.91) and (94.48,80) .. (100,80) .. controls (105.52,80) and (110,97.91) .. (110,120) .. controls (110,142.09) and (105.52,160) .. (100,160) .. controls (94.48,160) and (90,142.09) .. (90,120) -- cycle ;

\draw    (100,80) -- (200,80) ;

\draw    (100,160) -- (200,160) ;

\draw  [draw opacity=0] (200.15,80) .. controls (205.6,80.32) and (210,98.1) .. (210,120) .. controls (210,140.75) and (206.05,157.81) .. (200.99,159.81) -- (200,120) -- cycle ; \draw   (200.15,80) .. controls (205.6,80.32) and (210,98.1) .. (210,120) .. controls (210,140.75) and (206.05,157.81) .. (200.99,159.81) ;  

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (110,120) -- (210,120) ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (149.31,159.91) .. controls (144.11,158.49) and (140,141.16) .. (140,120) .. controls (140,98.81) and (144.12,81.46) .. (149.33,80.09) -- (150,120) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (149.31,159.91) .. controls (144.11,158.49) and (140,141.16) .. (140,120) .. controls (140,98.81) and (144.12,81.46) .. (149.33,80.09) ;  

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (110,120) -- (127,120) ;
\draw [shift={(130,120)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (160,120) -- (177,120) ;
\draw [shift={(180,120)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw    (220,120) -- (237,120) ;
\draw [shift={(240,120)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.25,-3) -- (0,0) -- (6.25,3) -- cycle    ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (390.15,160) .. controls (390.1,160) and (390.05,160) .. (390,160) .. controls (384.48,160) and (380,142.09) .. (380,120) .. controls (380,97.91) and (384.48,80) .. (390,80) .. controls (390.05,80) and (390.09,80) .. (390.14,80) -- (390,120) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (390.15,160) .. controls (390.1,160) and (390.05,160) .. (390,160) .. controls (384.48,160) and (380,142.09) .. (380,120) .. controls (380,97.91) and (384.48,80) .. (390,80) .. controls (390.05,80) and (390.09,80) .. (390.14,80) ; 

\draw   (250,120) .. controls (250,97.91) and (254.48,80) .. (260,80) .. controls (265.52,80) and (270,97.91) .. (270,120) .. controls (270,142.09) and (265.52,160) .. (260,160) .. controls (254.48,160) and (250,142.09) .. (250,120) -- cycle ;

\draw    (260,80) -- (310.14,80) ;

\draw    (260,160) -- (310.41,159.97) ;

\draw  [draw opacity=0] (390.15,80) .. controls (395.6,80.32) and (400,98.1) .. (400,120) .. controls (400,140.75) and (396.05,157.81) .. (390.99,159.81) -- (390,120) -- cycle ; \draw   (390.15,80) .. controls (395.6,80.32) and (400,98.1) .. (400,120) .. controls (400,140.75) and (396.05,157.81) .. (390.99,159.81) ;  

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (270,120) -- (320,120) ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (309.31,159.91) .. controls (304.11,158.49) and (300,141.16) .. (300,120) .. controls (300,98.81) and (304.12,81.46) .. (309.33,80.09) -- (310,120) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (309.31,159.91) .. controls (304.11,158.49) and (300,141.16) .. (300,120) .. controls (300,98.81) and (304.12,81.46) .. (309.33,80.09) ;  

\draw  [draw opacity=0][line width=1.5]  (310.14,80) .. controls (315.6,80.3) and (320,98.1) .. (320,120) .. controls (320,141.54) and (315.74,159.1) .. (310.41,159.97) -- (310,120) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (310.14,80) .. controls (315.6,80.3) and (320,98.1) .. (320,120) .. controls (320,141.54) and (315.74,159.1) .. (310.41,159.97) ;  

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (286.71,120.14) -- (287,120.13) ;
\draw [shift={(290,120)}, rotate = 177.51] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (350,120) -- (367,120) ;
\draw [shift={(370,120)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (349.59,120) -- (399.59,120) ;

\draw   (329.59,120) .. controls (329.59,97.91) and (334.07,80) .. (339.59,80) .. controls (345.11,80) and (349.59,97.91) .. (349.59,120) .. controls (349.59,142.09) and (345.11,160) .. (339.59,160) .. controls (334.07,160) and (329.59,142.09) .. (329.59,120) -- cycle ;

\draw    (339.59,80) -- (389.73,80) ;

\draw    (339.59,160) -- (390,159.97) ;

\draw    (323.84,147.32) .. controls (324.85,163.15) and (314.02,175.31) .. (306.5,164.5) ;
\draw [shift={(323.5,144.25)}, rotate = 80.94] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- cycle    ;

\draw    (410,120) -- (427,120) ;
\draw [shift={(430,120)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.25,-3) -- (0,0) -- (6.25,3) -- cycle    ;

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (550.15,160) .. controls (550.1,160) and (550.05,160) .. (550,160) .. controls (544.48,160) and (540,142.09) .. (540,120) .. controls (540,97.91) and (544.48,80) .. (550,80) .. controls (550.05,80) and (550.09,80) .. (550.14,80) -- (550,120) -- cycle ; \draw  [dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (550.15,160) .. controls (550.1,160) and (550.05,160) .. (550,160) .. controls (544.48,160) and (540,142.09) .. (540,120) .. controls (540,97.91) and (544.48,80) .. (550,80) .. controls (550.05,80) and (550.09,80) .. (550.14,80) ; 

\draw   (440,120) .. controls (440,97.91) and (444.48,80) .. (450,80) .. controls (455.52,80) and (460,97.91) .. (460,120) .. controls (460,142.09) and (455.52,160) .. (450,160) .. controls (444.48,160) and (440,142.09) .. (440,120) -- cycle ;

\draw    (450,80) -- (550,80) ;

\draw    (450,160) -- (550,160) ;

\draw  [draw opacity=0] (550.15,80) .. controls (555.6,80.32) and (560,98.1) .. (560,120) .. controls (560,140.75) and (556.05,157.81) .. (550.99,159.81) -- (550,120) -- cycle ; \draw   (550.15,80) .. controls (555.6,80.32) and (560,98.1) .. (560,120) .. controls (560,140.75) and (556.05,157.81) .. (550.99,159.81) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (499.31,159.91) .. controls (494.11,158.49) and (490,141.16) .. (490,120) .. controls (490,98.81) and (494.12,81.46) .. (499.33,80.09) -- (500,120) -- cycle ; \draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (499.31,159.91) .. controls (494.11,158.49) and (490,141.16) .. (490,120) .. controls (490,98.81) and (494.12,81.46) .. (499.33,80.09) ;  

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (460,120) .. controls (490,120.4) and (501.6,120.4) .. (499.33,80.09) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (500,160) .. controls (514.8,126.8) and (482.4,117.2) .. (560.38,119.5) ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (471.58,120) -- (471.64,120) ;
\draw [shift={(474.63,119.83)}, rotate = 176.87] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ]   (526.67,119.5) -- (527.42,119.47) ;
\draw [shift={(530.42,119.33)}, rotate = 177.46] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (3.57,-1.72) -- (0,0) -- (3.57,1.72) -- cycle    ;

\draw  [draw opacity=0][line width=1.5]  (150.14,80) .. controls (155.6,80.3) and (160,98.1) .. (160,120) .. controls (160,141.54) and (155.74,159.1) .. (150.41,159.97) -- (150,120) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][line width=1.5]  (150.14,80) .. controls (155.6,80.3) and (160,98.1) .. (160,120) .. controls (160,141.54) and (155.74,159.1) .. (150.41,159.97) ;  
\end{tikzpicture} \,.
\end{equation}
The minimal number of Dehn twist generators for $\text{MCG}(\Sigma_{g})$ with $g\geq 2$ is $2g+1$ \cite{Humphries} (while for $g=1$ the minimum number is 2). A canonical choice of cycles, whose corresponding Dehn twists generate the mapping class group, is shown in figure \ref{fig:humphries}. Although finitely generated, it is not a free group: there are relations among the Dehn twist generators. These relations can be used to reduce the number of generators to 2 elements \cite{Wajnryb1996}, which consist of products of Dehn twists. 

\begin{figure}
    \centering
    \tikzset{every picture/.style={line width=1pt}}
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.4,xscale=1.4,baseline={([yshift=-0.5ex]current bounding box.center)}
]


\draw  [draw opacity=0] (139.88,130.5) .. controls (139.34,133.12) and (134.85,135.17) .. (129.4,135.17) .. controls (123.58,135.17) and (118.87,132.84) .. (118.87,129.97) .. controls (118.87,129.96) and (118.87,129.96) .. (118.87,129.96) -- (129.4,129.97) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (139.88,130.5) .. controls (139.34,133.12) and (134.85,135.17) .. (129.4,135.17) .. controls (123.58,135.17) and (118.87,132.84) .. (118.87,129.97) .. controls (118.87,129.96) and (118.87,129.96) .. (118.87,129.96) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (118.93,129.41) .. controls (119.49,126.8) and (123.97,124.77) .. (129.4,124.77) .. controls (135.14,124.77) and (139.8,127.03) .. (139.94,129.84) -- (129.4,129.97) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (118.93,129.41) .. controls (119.49,126.8) and (123.97,124.77) .. (129.4,124.77) .. controls (135.14,124.77) and (139.8,127.03) .. (139.94,129.84) ;  

\draw  [draw opacity=0] (101.22,130.34) .. controls (100.67,132.96) and (96.19,135) .. (90.74,135) .. controls (84.92,135) and (80.2,132.67) .. (80.2,129.8) .. controls (80.2,129.8) and (80.2,129.79) .. (80.2,129.79) -- (90.74,129.8) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (101.22,130.34) .. controls (100.67,132.96) and (96.19,135) .. (90.74,135) .. controls (84.92,135) and (80.2,132.67) .. (80.2,129.8) .. controls (80.2,129.8) and (80.2,129.79) .. (80.2,129.79) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (80.26,129.24) .. controls (80.83,126.63) and (85.3,124.6) .. (90.74,124.6) .. controls (96.47,124.6) and (101.14,126.86) .. (101.27,129.67) -- (90.74,129.8) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (80.26,129.24) .. controls (80.83,126.63) and (85.3,124.6) .. (90.74,124.6) .. controls (96.47,124.6) and (101.14,126.86) .. (101.27,129.67) ;  

\draw    (110,160) .. controls (69.8,159.8) and (69.8,100.2) .. (110,100) ;

\draw    (110,100) .. controls (130.6,99.8) and (150.51,105.85) .. (169.91,106.45) ;

\draw    (110,160) .. controls (129.8,160.2) and (150.55,154.8) .. (169.55,155) ;

\draw    (100.18,128.36) .. controls (103.18,136.56) and (119.18,134.16) .. (120.18,128.36) ;

\draw    (101.27,130) .. controls (103.91,127.36) and (112.64,124.45) .. (119.18,130.27) ;

\draw    (138.88,127.98) .. controls (141.88,136.18) and (157.88,133.78) .. (158.88,127.98) ;

\draw    (139.97,129.62) .. controls (142.61,126.98) and (151.33,124.08) .. (157.88,129.89) ;

\draw  [draw opacity=0] (169.81,134.8) .. controls (169.41,134.82) and (168.99,134.83) .. (168.57,134.83) .. controls (162.75,134.83) and (158.03,132.51) .. (158.03,129.63) .. controls (158.03,129.63) and (158.03,129.63) .. (158.03,129.62) -- (168.57,129.63) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (169.81,134.8) .. controls (169.41,134.82) and (168.99,134.83) .. (168.57,134.83) .. controls (162.75,134.83) and (158.03,132.51) .. (158.03,129.63) .. controls (158.03,129.63) and (158.03,129.63) .. (158.03,129.62) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (158.09,129.07) .. controls (158.66,126.46) and (163.13,124.43) .. (168.57,124.43) .. controls (168.97,124.43) and (169.37,124.44) .. (169.76,124.47) -- (168.57,129.63) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (158.09,129.07) .. controls (158.66,126.46) and (163.13,124.43) .. (168.57,124.43) .. controls (168.97,124.43) and (169.37,124.44) .. (169.76,124.47) ;  

\draw  [color=wilsonred  ,draw opacity=1 ] (93.73,130.05) .. controls (93.73,121.94) and (100.99,115.36) .. (109.95,115.36) .. controls (118.92,115.36) and (126.18,121.94) .. (126.18,130.05) .. controls (126.18,138.15) and (118.92,144.73) .. (109.95,144.73) .. controls (100.99,144.73) and (93.73,138.15) .. (93.73,130.05) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ] (132.82,130.05) .. controls (132.82,121.94) and (140.08,115.36) .. (149.05,115.36) .. controls (158.01,115.36) and (165.27,121.94) .. (165.27,130.05) .. controls (165.27,138.15) and (158.01,144.73) .. (149.05,144.73) .. controls (140.08,144.73) and (132.82,138.15) .. (132.82,130.05) -- cycle ;

\draw  [draw opacity=0] (229.07,130.52) .. controls (229.63,133.13) and (234.18,135.17) .. (239.7,135.17) .. controls (245.61,135.17) and (250.4,132.84) .. (250.4,129.97) .. controls (250.4,129.97) and (250.4,129.96) .. (250.4,129.96) -- (239.7,129.97) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (229.07,130.52) .. controls (229.63,133.13) and (234.18,135.17) .. (239.7,135.17) .. controls (245.61,135.17) and (250.4,132.84) .. (250.4,129.97) .. controls (250.4,129.97) and (250.4,129.96) .. (250.4,129.96) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (250.34,129.4) .. controls (249.75,126.8) and (245.22,124.77) .. (239.7,124.77) .. controls (233.89,124.77) and (229.15,127.03) .. (229.01,129.84) -- (239.7,129.97) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (250.34,129.4) .. controls (249.75,126.8) and (245.22,124.77) .. (239.7,124.77) .. controls (233.89,124.77) and (229.15,127.03) .. (229.01,129.84) ;  

\draw  [draw opacity=0] (268.31,130.35) .. controls (268.88,132.97) and (273.42,135) .. (278.95,135) .. controls (284.86,135) and (289.64,132.68) .. (289.64,129.8) .. controls (289.64,129.8) and (289.64,129.8) .. (289.64,129.79) -- (278.95,129.8) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (268.31,130.35) .. controls (268.88,132.97) and (273.42,135) .. (278.95,135) .. controls (284.86,135) and (289.64,132.68) .. (289.64,129.8) .. controls (289.64,129.8) and (289.64,129.8) .. (289.64,129.79) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (289.58,129.24) .. controls (289,126.63) and (284.46,124.6) .. (278.95,124.6) .. controls (273.13,124.6) and (268.4,126.86) .. (268.26,129.68) -- (278.95,129.8) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (289.58,129.24) .. controls (289,126.63) and (284.46,124.6) .. (278.95,124.6) .. controls (273.13,124.6) and (268.4,126.86) .. (268.26,129.68) ;  

\draw    (259.4,160) .. controls (300.2,159.8) and (300.2,100.2) .. (259.4,100) ;

\draw    (259.4,100) .. controls (238.49,99.8) and (218.28,105.86) .. (198.59,106.46) ;

\draw    (259.4,160) .. controls (239.3,160.2) and (218.24,154.8) .. (198.96,155) ;

\draw    (269.36,128.37) .. controls (266.32,136.57) and (250.08,134.17) .. (249.06,128.37) ;

\draw    (268.26,130) .. controls (265.58,127.37) and (256.72,124.46) .. (250.08,130.28) ;

\draw    (230.09,127.99) .. controls (227.04,136.19) and (210.8,133.79) .. (209.79,127.99) ;

\draw    (228.98,129.63) .. controls (226.3,126.99) and (217.45,124.08) .. (210.8,129.9) ;

\draw  [draw opacity=0] (198.71,134.8) .. controls (199.11,134.83) and (199.53,134.84) .. (199.95,134.84) .. controls (205.86,134.84) and (210.64,132.51) .. (210.64,129.64) .. controls (210.64,129.63) and (210.64,129.63) .. (210.64,129.63) -- (199.95,129.64) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ] (198.71,134.8) .. controls (199.11,134.83) and (199.53,134.84) .. (199.95,134.84) .. controls (205.86,134.84) and (210.64,132.51) .. (210.64,129.64) .. controls (210.64,129.63) and (210.64,129.63) .. (210.64,129.63) ;  

\draw  [draw opacity=0][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (210.58,129.07) .. controls (210,126.47) and (205.46,124.44) .. (199.95,124.44) .. controls (199.55,124.44) and (199.15,124.45) .. (198.76,124.47) -- (199.95,129.64) -- cycle ; \draw  [color=wilsonred  ,draw opacity=1 ][dash pattern={on 1.5pt off 1.5pt on 1.5pt off 1.5pt}] (210.58,129.07) .. controls (210,126.47) and (205.46,124.44) .. (199.95,124.44) .. controls (199.55,124.44) and (199.15,124.45) .. (198.76,124.47) ;  

\draw  [color=wilsonred  ,draw opacity=1 ] (275.91,130.05) .. controls (275.91,121.94) and (268.54,115.37) .. (259.44,115.37) .. controls (250.35,115.37) and (242.97,121.94) .. (242.97,130.05) .. controls (242.97,138.16) and (250.35,144.73) .. (259.44,144.73) .. controls (268.54,144.73) and (275.91,138.16) .. (275.91,130.05) -- cycle ;

\draw  [color=wilsonred  ,draw opacity=1 ] (236.24,130.05) .. controls (236.24,121.94) and (228.86,115.37) .. (219.77,115.37) .. controls (210.67,115.37) and (203.3,121.94) .. (203.3,130.05) .. controls (203.3,138.16) and (210.67,144.73) .. (219.77,144.73) .. controls (228.86,144.73) and (236.24,138.16) .. (236.24,130.05) -- cycle ;

\draw (177.33,128.4) node [anchor=north west][inner sep=0.75pt]    {$\dotsc $};
\end{tikzpicture}
    \caption{For a closed Riemann surface of genus $g\geq 2$, the mapping class group $\text{MCG}(\Sigma_g)$ is generated by Dehn twists along the $2g+1$ cycles drawn in red.}
    \label{fig:humphries}
\end{figure}


The third important group associated to a handlebody is the so-called \emph{handlebody group} $\mathcal{H}_g$ of $M$. To describe it, consider the \emph{bulk} mapping class group $\text{MCG}(M)$, which consists of all large diffeomorphisms of $M$. Then we have the injection 
\begin{equation}
    \text{MCG}(M) \hookrightarrow \text{MCG}(\Sigma_g)
\end{equation}
by restricting the diffeomorphisms of $M$ to its boundary.
The image of this map is precisely the handlebody group. It is an infinite index (and non-normal) subgroup of the boundary MCG, which is rather complicated to describe explicitly \cite{Wajnryb1998}. An equivalent criterion for a mapping class $\gamma$ to be an element of $\mathcal{H}_g$ is that for every contractible cycle $C$, the image $\gamma(C)$ is also a contractible cycle \cite{Hensel2018APO}. Hence, the set of inequivalent handlebodies is parametrized by the coset 
\begin{equation}\label{eq:coset}
    \text{MCG}(\Sigma_g)/\mathcal{H}_g\,.
\end{equation} 

For genus 1, the above groups are easy to describe. The genus-1 handlebodies are the solid tori described by Maloney and Witten \cite{Maloney:2007ud} (consisting of thermal AdS$_3$ and an infinite family of Euclidean BTZ black holes), with fundamental group $\pi_1(M)=\mathbb{Z}$. The mapping class group of the boundary torus is $\text{MCG}(\Sigma_1) \cong \mathrm{PSL}(2,\mathbb{Z})$ and the handlebody group is
$
    \mathcal{H}_1 \cong \mathbb{Z}.
$
This follows from the fact that, at genus 1, there is only one contractible cycle $C$, hence any $\gamma \in \mathcal{H}_1$ that maps $C$ to itself is a power of a Dehn twist $T$ along $C$, i.e.~$\gamma = T^n$ for some $n\in \mathbb{Z}$. 

For genus $g\geq 2$, the handlebody group also contains powers of Dehn twists along contractible cycles, but the group is strictly larger than the subgroup generated by these simple twists. As an example of a distinct type of element in $\mathcal{H}_g$, consider any triple of closed curves $(\alpha,\beta,\delta)$ that bound a pair of pants. Then, if $\delta$ is a contractible cycle, the product of Dehn twists  $T_\alpha T_\beta^{-1}$ is in $\mathcal{H}_g$ \cite{Hensel2018APO}.
