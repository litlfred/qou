---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-003-22-dimofte-gaiotto-gukovs-construction-tdgg
section_title: "Dimofte-Gaiotto-Gukov's construction : TDGG"
section_number: 2.2
pages: 10-21
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.979
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
\label{sec:DGG}

In \cite{Dimofte:2011ju}, a combinatorial way of constructing a 3d SCFT, which we denote $T^{DGG}[N,X_A]$, for given choice of $(N,A)$ is proposed. Empirically, the theory associated to non-hyperbolic $N$ is a trivial theory only with topological degrees of freedom.  In this subsection we focus on the case when $N$ is hyperbolic. Here we give a  summary of the DGG's construction with a modification on superpotential deformation associated to  `hard' internal edges (see \eqref{DGG : final}) which play a crucial role in the symmetry enhancement of the theory. 

\paragraph{Mechanics of ideal triangualtion} The construction is based on a choice of an ideal triangulation $\cT$ of $N$.

\begin{align}
\cT \;: \; N = \bigg{(}\bigcup_{i=1}^k \Delta_i \bigg{)}/\sim\;.
\end{align}

Here $\Delta_i$ denote the $i$-th tetrahedron in the triangulation. Ideal tetrahedron can be embedded into  a hyperbolic upper half plane $\mathbb{H}^3$ in a way that all vertices are located on the boundary of $\mathbb{H}^3$ and both of edges and faces are geodesics. Hyperbolic structures on an ideal tetrahedron can be parameterized by a complex parameter $z$ (with $0<\textrm{Im}[Z]<\pi$, $Z:=\log z$), which is the cross-ratio of the positions of its vertices on $\partial \mathbb{H}^3$. We assign edge parameters $(z,z',z'')$ to each pair of edges of ideal tetrahedron as in the figure below.

\begin{figure}[h]
\begin{center}   
\includegraphics[width=.30\textwidth]{ideal-tetrahedron-in-H3.pdf}
\quad 
\includegraphics[width=.25\textwidth]{ideal-tetrahedron.pdf}
\end{center}
\caption{Edge parameters $(z,z',z'')$ of an ideal tetrahedron. Left: ideal tetrahedron in $\mathbb{H}^3=\{(y,w):y\in \mathbb{R}_+, w \in \mathbb{C}\}$ with metric $ds^2 (\mathbb{H}^3) = \frac{dy^2 +d w d \bar{w}}{y^2}$. Using the isometry of $\mathbb{H}^3$, $PSL(2,\mathbb{C})$, four asymptotic vertices can be placed at  $(y,w) = (0,0),(0,1),(0,z)$ and $(\infty, \cdot)$. Right: topologically, ideal tetrahedron is a tetrahedron with truncated vertices. } 
\label{fig:ideal-tetrahedron}
\end{figure}

\\
Geometrically, these edge parameters correspond to 

\begin{align}
&\{ Z,Z',Z''\}:=\{ \log z, \log z',\log z'' \}  \nonumber
\\
&=i(\textrm{dihedral angle between two faces meeting on the edge})+(\textrm{torsion}) \;.
\end{align}

Here ``torsion'' is a quantity which measures the twisting of hyperbolic metric around the edge. 
For an ideal tetrahedron in $\mathbb{H}^3$, these parameters satisfy

\begin{align}
\begin{split}
&Z_i+Z'_i+Z''_i=i \pi\; (\textrm{sum of angles in small boundary triangle equals to $\pi$})\;, 
\\
&e^{-Z_i}+e^{Z''_i}=1\;. \label{hyperbolic on Delta}
\end{split}
\end{align}

The second equation follows directly from the geometric definition of $(z,z',z'')$ as equivalent cross-ratios.
These constraints are compatible with the following cyclic symmetry of ideal tetrahedron:

\begin{align}
\mathbb{Z}_3 \;: \; (Z,Z',Z'')\rightarrow  (Z',Z'',Z)\rightarrow (Z'',Z,Z')\;. \label{Cyclc-in-Z-Zp-Zpp}
\end{align}


An hyperbolic structure on a knot complement $N$ can be obtained  by gluing the hyperbolic structure on each tetrahedron in a smooth way. 
For the smooth gluing, we need to impose the following conditions

\begin{align}
\begin{split}
C_I  &:= (\textrm{sum of all logarithmic edge variables associated to }
\\
& \quad \quad  \textrm{edges meeting at the $I$-th internal edge in the gluing})  
\\
& =\sum_{i=1}^{k}(G_{Ii}Z_i +G'_{Ii}Z'_i +G''_{Ii}Z''_i)\;, \quad G_{Ii},G'_{Ii},G''_{Ii}\in \{ 0,1,2\}\;.
\\
& =2\pi i \;. \label{internal edges}
\end{split}
\end{align}

There are $k$-internal edges in an ideal triangulation with $k$ ideal tetrahedra. A solution to these gluing equations  \eqref{hyperbolic on Delta} and \eqref{internal edges} with conditions $0<\textrm{Im}[Z_i]<\pi$ for all $i$ gives a  hyperbolic  (generally  incomplete) structure on $N$. 

\paragraph{$\CM(P_{SCFT})$ from ideal triangulation}  More generally, a solution to the exponentiated gluing equations  gives an irreducible flat $PSL(2,\mathbb{C})=SL(2,\mathbb{C})/\langle \pm 1\rangle$ connections on $N$. 
Consider the algebraic variety $\cD[N,\cT]$ determined by gluing equations of an ideal triangulation $\cT$,

\begin{align}
\cD[N,\cT]:=\{ z_i, z'_i, z''_i \in \mathbb{C}\backslash \{ 0,1\}: z_i z_i' z_i''=-1, z_i^{-1}+z''_i-1=0, \prod_{i=1}^k z_i^{G_{Ii}}(z'_i)^{G'_{Ii}} (z''_i)^{G''_{Ii}}=1\}\;.
\label{deformation variety}
 \end{align}
 
The variety  is called a {\it deformation variety}.  A point in $\cD[N,\cT]$ gives an irreducible flat-connection via a map $\chi_T$
 \begin{align}
 \chi_{\cT} : \; \cD[N,\cT] \rightarrow \chi (N):=\{  \rho_{\rm hol} \in \textrm{Hom}\big{[}\pi_1 (N) \rightarrow PSL(2,\mathbb{C})\big{]}/(\textrm{conj}) \}\;. 
 \end{align}

where the definition of $\chi(N)$ here is equivalent to that in \eqref{eq:chidef1}.
The map $ \chi_{\cT}$ is injective but not surjective.  
Using the map, holonomy matrix along a primitive boundary  cycle $A\in H_1 (\partial N,\mathbb{Z}) = \pi_1 (\partial N) \subset \pi_1 (N)$ can be written as linear combinations of logarithmic edge parameters

\begin{align}
\begin{split}
& \rho_{\rm hol}(A) = \left(\begin{array}{cc}e^{a/2} & 0 \\ * & e^{-a/2}\end{array}\right) \quad \textrm{where }a=\sum_{i=1}^k (\alpha_i Z_i +\alpha''_i Z''_i)+ i \pi \epsilon 
\\
&\textrm{with integer coefficients }(\alpha_i, \alpha''_i ,  \epsilon)\;. \label{Hol(A) in terms of edges}
\end{split}
\end{align}

Dependence on $\{Z'_i\}$ was eliminated using the linear relations in  \eqref{hyperbolic on Delta}.
The algebraic variety depends on the choice of an ideal triangulation $\cT$ of $N$.  
But it is known that  the Dehn surgery component $\chi_0(N)=\bigcup_m \CM(P_{SCFT},m)$ 
in \eqref{Dehn-surgery com} is always contained in $\cD[N,\cT]$ for any $\cT$  except exotic cases when  $\cD[N,\cT]$ is empty \cite{tillmann2012degenerations},

\begin{align}
\begin{split}
\chi_0(N)=\; &\textrm{the connected component of $\cD[N,\cT]$ for non-exotic $\cT$  }
\\
&\textrm{containing a  solution  of gluing eqns corresponding to $\CA^{\rm \overline{hyp}}$} \;. \label{Dehn-surgery com-2}
\end{split}
\end{align}

We currently do not have the field theoretic understanding of the exotic case and will always work with non-exotic triangulations. 

\paragraph{$SU(2)/SO(3)$-type  of boundary cycle $A$} For later use, we classify a primitive boundary cycle $A$ into two types, $SU(2)$ or $SO(3)$, depending on evenness/oddness of the linear coefficients $(\alpha_i, \alpha''_i)$. 

\begin{align}
A \textrm{ is of }
 \begin{cases}
 \textrm{$SU(2)$-type}\;,\;\textrm{if all $(\alpha_i, \alpha''_i)$ can be chosen as even-integers}
 \\
\textrm{$SO(3)$-type}\;,\;\textrm{otherwise} 
\end{cases} \label{Def : SO/SU type}
\end{align}

Note that the linear coefficients are defined modulo the following shifts due to the last gluing equations in \eqref{deformation variety}

\begin{align}
 \bigg{(}\alpha_i, \alpha''_i \bigg{)}\rightarrow \bigg{(} \alpha_i + \sum_{i=1}^k c_{Ii}(G_{Ii}-G'_{Ii}), \alpha''_i + \sum_{i=1}^k c_{Ii} (G''_{Ii} - G'_{Ii})\bigg{)}\quad \textrm{with some integers $c_{Ii}$}\;,\nonumber
\end{align}

and $A$ is $SU(2)$-type if there is a choice of $c_{Ii}$ which makes all $(\alpha_i, \alpha''_i)$ even-integers. An  alternative definition of $SO(3)/SU(2)$ type without relying an ideal triangulation is 

\begin{align}
A \textrm{ is of }
 \begin{cases}
 \textrm{$SU(2)$-type}\;,\; A \in \textrm{Ker} \big{(} i_* : H_1 (\partial N, \mathbb{Z})\rightarrow H_1 (N, \mathbb{Z}_2) \big{)}
 \\
\textrm{$SO(3)$-type}\;,\;\textrm{otherwise} 
\end{cases} \label{Def : SO/SU type 2}
\end{align}

Two definitions, \eqref{Def : SO/SU type} and  \eqref{Def : SO/SU type 2}, are equivalent \cite{neumann1992combinatorics}.
An explanation of $SU(2)/SO(3)$ types from the 6d $\CN=(2,0)$ theory point of view is discussed in Appendix~\ref{app:susotypes}.

\paragraph{$T^{DGG}[N,X_A]$ from symplectic gluing} The gluing equations are known to have the following symplectic structure \cite{neumann1985volumes,neumann1992combinatorics} which play a crucial role in the DGG's construction. Upon a skew-symmetric bilinear $\{ \;, \;\}$ \textrm{defined by } $\{Z_i, Z'_j  \} =\{Z'_i, Z''_j  \} = \{ Z''_i, Z_j \} = \delta_{ij}$, internal edge variables $\{C_I\}$ and the boundary holonomy variable $a$ around $A$ satisfy the followings:  

\begin{align}
\{ C_I, C_J\} = \{ a , C_I\} =0\;, \quad \textrm{for all $I,J=1,\ldots, k$}
\end{align}

Further we can choose a linearly independent primitive cycle $B\in H_1 (\partial N, \mathbb{Z})$ such that 

\begin{align}
\{a, b\} =- 2\;, 
\end{align}

where $b$ is related to the holonomy along $B$ as in eq.~\eqref{Hol(A) in terms of edges}. The choice of $B$ is not unique but have the following freedom of choice

\begin{align}
B\rightarrow B+ k A\;, \quad k \in \mathbb{Z}\;.
\end{align}

Using the freedom, we will always choose $B$ to have the properties that

\begin{align}
B \textrm{ is of }
 \begin{cases}
 \textrm{$SU(2)$ type}\;,\;\textrm{when $A$ is of  $SO(3)$ type\;,}
 \\
\textrm{$SO(3)$ type}\;,\;\textrm{when $A$ is of $SU(2)$ type\;,} \label{types of (A,B)}
\end{cases}
\end{align}

where the $SU(2)/SO(3)$ types of $B$-cycle is defined in the same way as $A$.

Among $k$-internal edge variables in eq.~\eqref{internal edges},  only $k-1$ of them\footnote{More generally, for an ideal triangulation of  a knot/link complement $N$  with $\sharp_T$ torus boundaries the number of linearly independent internal edge variables are $k-\sharp_T$. } are linearly independent modulo linear relations in \eqref{hyperbolic on Delta}. Let the linearly independent set as $\{C_I\}_{I=1}^{k-1}$. Then, we introduce their conjugate variables $\{\Gamma_I\}_{I=1}^{k-1}$ satisfying

\begin{align}
\{ C_I, \Gamma_J\}= \delta_{IJ}\;, \quad \{ a, \Gamma_I\} = \{ b, \Gamma_I\}=0\;, \quad I,J=1,\ldots, k-1\;.
\end{align}

From the choice of $(A,B,\{ C_I\}, \{\Gamma_I\})$, we associate a $Sp(2k,\mathbb{Z})$ matrix $g_{N}$ and integer-valued $2k$-vector $\nu$ as follows


\begin{align}
&\left(\begin{array}{c}X_A \\C_1  \\ \ldots \\ C_{k-1}\\ P_B \\ \Gamma_1 \\ \ldots \\ \Gamma_{k-1}\end{array}\right) = g_{N} \cdot  \left(\begin{array}{c}Z_1 \\ Z_2  \\ \ldots \\ Z_{k}\\ Z_1'' \\ Z_2'' \\ \ldots \\ Z_{k}'' \end{array}\right) + i \pi \nu_{N}\;, \label{g_N}
\end{align}
where
\begin{align}
&(X_A, P_B) = 
\begin{cases}
 (\frac{a} 2,b)\;,\;\textrm{when $(A,B)$ is of  $\big{(}SU(2),SO(3)\big{)}$ type}
 \\
(a,\frac{b}2 )\;,\;\textrm{when $(A,B)$ is of $\big{(}SO(3),SU(2)\big{)}$ type} \end{cases} \label{(XA,PB)}
\end{align}

Notice that $(X_A, P_B)$ are always linear combinations of $Z_i, Z''_i$ with integer coefficients because of the even-ness condition \eqref{Def : SO/SU type}.

Using the gluing data summarized in $(g_N, \nu_N)$, we can construct the corresponding $T^{DGG}$ theory. 
As a first step, we prepare $k$-copies of a free chiral theory 

\begin{align}
\begin{split}
&T_{\textrm{step I}} = T_\Delta^{\otimes k} = \overbrace{T_\Delta \otimes \ldots \otimes T_{\Delta}}^{\textrm{$k$ times}}\;,
\\
& T_{\Delta}  := (\textrm{a free theory of single chiral multiplet $\Phi$ with  CS level $-1/2$}
\\
&  \quad \quad \quad \textrm{ for non-dynamical background gauge field coupled to $U(1)$ flavor symmetry})\;,
\\
&\mathcal{L}_{T_{\rm step 1}} (V_1,\ldots , V_k) = \sum_{i=1}^k \frac{1}{4\pi}\int d^4\theta (- \frac{1}2 \Sigma_{i} V_{i})   +\int d^4\theta \Phi_{i}^\dagger e^{V_{i}} \Phi_i\;,
\label{DGG : step 1}
\end{split}
\end{align}

where $\Sigma_i$ is the field strength of the vector multiplet $V_i$.
The theory $T_{\textrm{step I}}$ has $u(1)^k$ flavor symmetry and  $\{V_i\}$ are background vector-multiplets  coupled to the flavor symmetries. 

Using the symmetry, one can consider $Sp(2k,\mathbb{Z})$ action on the theory which is a generalization of Witten's $SL(2,\mathbb{Z})$ action \cite{Witten:2003ya} which corresponds to  $k=1$ case. To be more explicit, one needs to decompose a $Sp(2k,\mathbb{Z})$ into products of ``T-type ($g^t_K$),'' ``S-type ($g^s_{J}$),'' and ``GL-type($g^{gl}_U$)'': 

\begin{align}
g^t_K:= \left(\begin{array}{cc}I & 0 \\ K & I\end{array}\right)\ \;,  \quad g^s_J:= \left(\begin{array}{cc}I-J & -J \\ J & I-J\end{array}\right)\ \;,  \quad g^{gl}_U:= \left(\begin{array}{cc}U & 0 \\ 0 & (U^{-1})^t\end{array}\right)\ \;. \label{T,S and GL type}
\end{align}

Here $J$ is a diagonal matrix whose diagonal entries are either 0 or 1.
Let $\mathcal{L}_{T} (\vec{V}:=(V_1, \ldots, V_k))$ be a Lagrangian for a theory $T$ with $U(1)^k$ flavor symmetry. Field theoretic actions of the basic types  are

\begin{align}
\begin{split}
&\mathcal{L}_{g^t_K \cdot T} (\vec{V}) :=   \mathcal{L}_{T} (\vec{V}) + \frac{1}{4\pi } \int d^4\theta \vec{\Sigma} \cdot K \vec{V}\;,
\\
&\mathcal{L}_{g^s_J \cdot T} (\vec{V}) :=   \mathcal{L}_{T} ((I-J)\vec{V}+J\vec{V}') + \frac{1}{2\pi } \int d^4\theta \vec{\Sigma}\cdot J \vec{V}'\;,
\\
&\mathcal{L}_{g^{gl}_U \cdot T} (\vec{V}) :=   \mathcal{L}_{T} (U^{-1}\cdot\vec{V})\;,
\end{split}
\end{align}

where $\vec{V}'$ only has components such that $J\vec{V}'=\vec{V}'$, and they are now dynamical fields.
As for the $SL(2,\mathbb{Z})$ case, the final theory does not depend on the decomposition and depends only on the $Sp(2k,\mathbb{Z})$ element. 

Now the second step of the construction is 

\begin{align}
T_{\textrm{step II}} = g_N \cdot T_{\textrm{step I}}\;, \label{DGG : step 2}
\end{align}

where $g_N$ is the symplectic matrix in \eqref{g_N} obtained from an ideal triangulation of $N$. The $g_N$-transformed theory still has $u(1)^k$ flavor symmetry 

\begin{align}
U(1)_{X_A} \times U(1)_{C_1} \times \ldots \times U(1)_{C_{k-1}}\;,
\end{align}

whose background gauge fields are $V_{X_A}:=V_1,\ldots, V_{C_{k-1}}:=V_{k}$ in $T_{\textrm{step II}}$.

As a final step, we break the $U(1)^k$ to its subgroup by adding chiral operators 
to the superpotential 

\begin{align}
\mathcal{L}_{T^{DGG}[N,X_A]} = \mathcal{L}_{T_{\textrm{step II}}}+\bigg{(} \sum_{\textrm{`easy' $C_I$}}\int d^2 \theta  O_{C_I}+c.c \bigg{)}\;. \label{DGG : final}
\end{align}

An internal edge $C_I = \sum_{i=1}^k (G_{Ii}Z_i +G'_{Ii}Z'_i+G''_{Ii}Z''_i)$ in  \eqref{internal edges} is called `easy' \cite{Dimofte:2011ju} 
if at most one of $G_{Ii}$, $G'_{Ii}$ and $G''_{Ii}$ is nonzero for each $i$,

\begin{align}
\sum_{i=1}^k (G_{Ii}G'_{Ii}+G'_{Ii} G''_{Ii}+G''_{Ii}G_{Ii}) = 0\;
\end{align}

and `hard' otherwise. 
This condition simply means that only one of edge parameters ($Z_i,Z'_i$ and $Z''_i$) of $i$-th tetrahedron appears in $C_I$ for all $i=1\ldots k$. Upon a proper choice of cyclic relabeling \eqref{Cyclc-in-Z-Zp-Zpp} of edge parameters, we can  make such an internal edge $C_I$ as a linear combination of only $Z_i$s: 

\begin{align}
C_I = \sum_{i=1}^k \widetilde{G}_{Ii}Z_i\;, \quad G_{Ii}\in \{ 0, 1, 2\}\;.
\end{align}

Then, the gauge-invariant chiral primary operator $O_{C_I}$ in $T_{\textrm{step II}}$ is given by

\begin{align}
O_{C_I} = \prod_{i=1}^k \Phi_i^{\widetilde{G}_{Ii}}\;.
\end{align}

As will be explained below, different cyclic labelings  give different descriptions of $T_{\textrm{step II}}$ which are related by a sequence of basic dualities in \eqref{T=ST*(T)}. Therefore for each easy internal edge $C_I$, there is a chiral primary operator  $O_{C_I}$ which can be written as the above form in a  duality frame.  The operator is  charged only under $U(1)_{C_I}$. For each hard internal edge, on the other hand, there may only be a corresponding gauge invariant dyonic 1/4 BPS operator with non-zero spin.  There is no way to write down a supersymmetric deformation using the dyonic local operators. 


\paragraph{Hard internal edges and accidental symmetries } In the original DGG's construction \cite{Dimofte:2011ju}, they proposed to use ideal triangulations with only easy internal edges. From superficial counting, we expect the resulting $T^{DGG}[N]$ has   flavor symmetry of rank $1$ whose Cartan corresponds to the $U(1)_{X_A}$.

\begin{align}
\begin{split}
&\textrm{If all $C_I$ are easy, we superficially expect that}
\\
&U(1)_{X_A} \times U(1)_{C_1}\times \ldots \times U(1)_{C_{k-1}} \; \textrm{in $T_{\textrm{step II}}$}
\\
&  \xrightarrow[]{\textrm{\quad Superpotential deformation in \eqref{DGG : final} \quad } }   U(1)_{X_A} \; \textrm{in $T^{DGG}[N,X_A]$}
\end{split}
\end{align}

The counting sounds compatible with the 6d construction since the knot gives a flavor symmetry $(su(2))$ of rank 1. But the counting  could be wrong as we will see below  for the case with an ideal triangulation of $N=(\textrm{figure-eight knot complement})$ with $6$-tetrahedra. The correct  rank is always equal or greater than the superficial counting.  
In our modified proposal \eqref{DGG : final}, we can use any ideal triangulation  and  will argue that the resulting  theory is independent of the choice of ideal triangulation regardless of existence of hard edges. One of the consequences is that  rank of the flavor symmetry could be larger than $1$ because the number of independent easy edges  could be less than $(k-1)$.  From the counting of linearly independent easy internal edges, we checked that $T^{DGG}$ theories for most of knot complements in SnapPy's census have additional symmetries. 

For example, we show  the $SU(3)$ symmetry for all hyperbolic twist knots in section  \ref{sec:SU(3)}.
The  additional symmetries are accidental and unexpected from 6d viewpoint. 
The above DGG's construction can be  generalized to higher $\mathcal{K}$ (number of M5-branes) cases \cite{Dimofte:2014zga} and  there is no such an additional symmetry when  $\mathcal{K}$ is sufficiently large. 
For higher $\CK$ one need to use a so-called $\mathcal{K}$-decomposition which replace a single tetrahedron in an ideal triangulation into  $\frac{1}6 \mathcal{K}(\mathcal{K}^2-1)$ copies of finer building blocks, octahedra. The construction of the 3d theory for higher $\mathcal{K}$ is parallel to the construction for $\mathcal{K}=2$ case reviewed above except tetrahedra in an ideal triangulation are replaced by  octahedra in a $\mathcal{K}$-decomposition. 
We  assign 3 complex parameters ($z,z',z''$) to each pair of two vertices of an octahedron and their gluing equations  in a $\CK$-decomposition also possess a symplectic structure. One  difference in higher $\mathcal{K}$ is that there are enough number of easy internal edges (better to call internal vertices for $\mathcal{K}$-decomposition case) to break all $u(1)$ symmetries except the ones expected from 6d viewpoint. 6d viewpoint expect that the 3d theory has a flavor symmetry of rank $(\mathcal{K}-1)$.  A hard internal edge  appears when two edges of a single tetrahedron are glued to the internal edges simultaneously. In  $\mathcal{K}$-decomposition, two different vertices of a single octahedron can not meet at an internal vertex possibly except when the octahedron is located nearest  to one of  vertices of tetrahedrons.  So the number of hard internal vertices will be at most order of $k$ (the number of tetrahedrons in a triangulation) while there are $k \frac{\mathcal{K}(\mathcal{K}^2-1)}6$ internal vertices among which  $(\mathcal{K}-1)$ are linearly dependent. So the number of easy internal vertices are  $k \big{(} \frac{\mathcal{K}(\mathcal{K}^2-1)}6- o(1) \big{)}$ which is large enough to span the  $\big{(} k \frac{\mathcal{K}(\mathcal{K}^2-1)}6 - (\mathcal{K}-1)  \big{)}$-linearly independent internal vertices for sufficiently large $\mathcal{K}$.

\paragraph{Topological invariance of $T^{DGG}[N,X_A]$}  At first glance, the above construction seems to depend on the various choices other than $(N,A)$. For the construction, we  choose  an ideal triangulation of $N$.   
All different ideal triangulations of a given 3-manifold are known to be related by sequence of a basic local move called 2-3 Pachner move. In the DGG's construction, the geometric move corresponds to a mirror symmetry  between a 3d $\mathcal{N}=2$ SQED with two chirals $(\Phi_A, \Phi_B)$ of charge $(+1, -1)$ and a free theory with 3 chirals $(M, T_p, T_m)$:

\begin{align}
\begin{split}
&\int d^4 \theta  \bigg{(}\Phi_A^\dagger e^{V} \Phi_A +\Phi_B^\dagger e^{-V+U} \Phi_B +\frac{1}{4\pi} (U+ 2W) (\Sigma_{V}-\frac{1}2 \Sigma_U)\bigg{)} \quad (\textrm{$ V$ : dynamical})
\\
&\simeq \int d^4 \theta \bigg{(}   M^\dagger e^{U} M + (T_p)^\dagger e^{W} T_p + (T_m)^\dagger e^{-U-W} T_m \bigg{)} +\big{(}  \int d^2 \theta M T_p T_m +c.c \big{)}
\label{3d mirror-1}
\end{split}
\end{align}

Under the duality, gauge-invariant chiral operators  are mapped as follows

\begin{align} 
\Phi_A \Phi_B  \qquad \qquad \qquad \qquad  \qquad \quad &\leftrightarrow&  \qquad \qquad M  \nonumber
\\
V_+ \; (\textrm{BPS monopole operator of magnetic flux $+1$}) \qquad &\leftrightarrow &  T_p \label{3d mirror-2}
\\
V_- \; (\textrm{BPS monopole operator of magnetic flux $-1$}) \qquad &\leftrightarrow &  T_m \nonumber
\end{align}

So the $T^{DGG}$ theory is invariant under the local 2-3 move and thus independent on the choice of $\cT$.
For a given choice of $\cT$, we still have freedoms of choosing cyclic labeling \eqref{Cyclc-in-Z-Zp-Zpp} of edge parameters for each tetrahedron. 

\begin{align}
\begin{split}
 &\left( {\begin{array}{c}
   Z  \\
   Z''  \\
  \end{array} } \right) \; \rightarrow \;  \left( {\begin{array}{c}
   Z'  \\
   Z  \\
  \end{array} } \right)  = ST\cdot  \left( {\begin{array}{c}
   Z  \\
   Z''  \\
  \end{array} } \right) +  i \pi \left( {\begin{array}{c}
   1 \\
   0  \\
  \end{array} } \right)\;,
 \\
 & S := \left( {\begin{array}{cc}
   0 & -1 \\
   1 & 0 \\
  \end{array} } \right)\;, \quad 
  T := \left( {\begin{array}{cc}
   1 & 0 \\
   1 & 1 \\
  \end{array} } \right)\;.
  \end{split}
\end{align}

The invariance $T^{DGG}$ theory under choice is guaranteed from a duality 

\begin{align}
T_\Delta \simeq (ST) \cdot T_\Delta\;. \label{3d mirror-2}
\end{align}

More explicitly, the duality is 

\begin{align}
\begin{split}
&\int d^4 \theta \big{(} \Phi^\dagger e^{U} \Phi -\frac{1}{8\pi} U \Sigma_U \big{)}
\\
&\simeq \int d^4 \theta  \big{(}\Phi^\dagger e^{V} \Phi + \frac{1}{8\pi} V \Sigma_V + \frac{1}{2\pi} U \Sigma_V \big{)} \;, \quad (\textrm{$ V$ : dynamical})\;. \label{T=ST*(T)}
\end{split}
\end{align}

In the construction of $T^{DGG}$ theory, we also need to choose conjugate variables $\{ P_B, \Gamma_I\}$. But these choices only affect the background Chern-Simons coupling coupled to flavor symmetries. So modulo the background CS couplings, the theory only depends on the topological choice $(N,A)$.  To specify the background Chern-Simons coupling of the $U(1)_{X_A}$ flavor symmetry associated to the knot, we sometimes specify the choice of boundary cycle $B$ and denote the theory by 

\begin{align}
T^{DGG}[N,X_A ;P_B]\;.
\end{align}


\paragraph{Example : $N=S^3 \backslash \mathbf{4}_1 =m004$ with an ideal triangulation with 2 tetrahedra} Here $\mathbf{4}_1$ is a simplified notation, called Alexander-Briggs notation, for  figure-eight knot which is depicted in fig \ref{fig:ideal-triangulation-41}.  The notation simply means that the figure-eight knot is the 1st (simplest) knot with 4 crossings.  The fundamental group of the knot complement is 

\begin{align}
\pi_1 (S^3\backslash \mathbf{4_1}) = & \langle \alpha, \beta,\gamma : \alpha \gamma^{-1} \beta \alpha^{-1}\gamma = \beta \gamma^{-1}\beta^{-1}\alpha= 1 \rangle\;.
\end{align}

 The group contains a  peripheral subgroup $\mathbb{Z}\times \mathbb{Z}$  which can be identified as fundamental group of boundary torus

\begin{align}
\begin{split}
&\pi_1 \big{(}\partial (S^3 \backslash \mathbf{4}_1)\big{)} = \pi_1 (\mathbb{T}^2) = \mathbb{Z} \times \mathbb{Z}=  \langle \mu , \nu \rangle \subset \pi_1 (S^3\backslash \mathbf{4}_1)
\end{split}
\end{align}

Canonical choice of the basis $(\mu, \lambda)$ is   (meridian, longitude). Upon the basis choice, the embedding $i : \pi_1 \big{(}\partial (S^3 \backslash \mathbf{4}_1)\big{)}  \rightarrow \pi_1 (S^3 \backslash \mathbf{4}_1)$ is given by 

\begin{align}
i (\mu) = \alpha \;, \quad i (\nu) = \alpha \gamma^{-1}\beta \gamma \alpha^{-1}\beta^{-1}
\end{align}

The knot complement can be  ideally triangulated by two tetrahedrons. 

\begin{align}
\begin{split}
\cT \; : \;  S^3 \backslash \mathbf{4_1} =(\Delta_1 \cup \Delta_2)/\sim\;.
\end{split}
\end{align}

See fig.~\ref{fig:ideal-triangulation-41} below for the gluing rule $\sim$.

 \begin{figure}[h]
\begin{center}   \includegraphics[width=.35\textwidth]{ideal-triangulation-41.pdf}
   \end{center}
   \caption{The simplest ideal triangulation of $m004=S^3\backslash \mathbf{4_1}$.} 
   \label{fig:ideal-triangulation-41}
\end{figure}

There are two internal edges in the triangulation which are linearly dependent modulo the linear equations in \eqref{hyperbolic on Delta}.

\begin{align}
C_1 =Z_1''+Z_2'+2Z_1'+2Z_2\;, \quad C_2 = Z_1''+Z_2'+2Z_1+2Z_2''\;. \label{internal edges of 4_1}
\end{align}

The deformation variety in this example is

\begin{align}
\begin{split}
\mathcal{D}[S^3\backslash \mathbf{4_1},\cT] = & \{ z_1,z_1', z_1'',z_2,z_2',z_2'' : z_i^{-1}+z_i''-1=0,\; z_i z_i'z_i''=-1,\; z_1'' (z_1')^2  z_2' z_2^2 =1\}_{i=1,2}\;. 
\label{deformation variety-m004}
\end{split}
\end{align}

Each point in the variety gives a $PSL(2,\mathbb{C}) = SL(2,\mathbb{C})/\langle \pm 1 \rangle$ flat connection on the knot complement. 
The holonomy matrices along the basis ($\alpha, \beta,\gamma$) of $\pi_1 (S^3\backslash \mathbf{4_1})$ for the flat connections is 

\begin{align}
\begin{split}
& \rho_{\rm hol}(\alpha)= \left(
\begin{array}{cc}
 \sqrt{\frac{z_1}{z_2}} & 0 \\
 \frac{-1+z_1}{\sqrt{z_1 z_2}} & \sqrt{\frac{z_2}{z_1}} \\
\end{array}
\right) \;,
\\
& \rho_{\rm hol}(\beta)= \left(
\begin{array}{cc}
 \sqrt{\frac{z_2'}{z_1''}} &- \sqrt{\frac{z_2'}{z_1''}} \\
 \sqrt{z_1'' z_2'} & \, -\sqrt{\frac{z_1''}{z_2'}}\left(z_2'-1\right) \\
\end{array}
\right) \;,
\\
& \rho_{\rm hol}(\gamma)= \left(
\begin{array}{cc}
 \frac{z_1'+z_2''-1}{\sqrt{z_1' z_2''}} & \frac{1-z_1'}{\sqrt{z_1' z_2''}} \\
 \frac{z_2''-1}{\sqrt{z_1' z_2''}} & \frac{1}{\sqrt{z_1' z_2''}} \\
\end{array}
\right) \;.
\end{split}
\label{Hol-m004-1}
\end{align}

Boundary (meridian, longitudinal) holonomies  are

\begin{align}
\begin{split}
& \rho_{\rm hol}(\mu)=  {\rm Hol}(\alpha) = \left(\begin{array}{cc}e^{a_\mu /2}& 0 \\ * & e^{-a_\mu /2}\end{array}\right)\;, \quad a(\mu) =  Z_1-Z_2\;,
\\
& \rho_{\rm hol} (\nu) = {\rm Hol} (\alpha \gamma^{-1 }\beta \gamma \alpha^{-1}\beta^{-1})=  \left(\begin{array}{cc}e^{b_\lambda/2}& 0 \\ * & e^{-b_\lambda/2}\end{array}\right)\;, \quad b_\lambda = 2(Z_1-Z_1')\;.
\label{Hol-m004-2}
\end{split}
\end{align}

So, $(\mu,\lambda)$ is of $(SO(3),SU(2))$ type and we choose

\begin{align}
X_{\mu} = a_\mu = Z_1-Z_2\;, \quad P_{\lambda} = b_\lambda/2 = Z_1-Z_1'\;.
\end{align}

With the choices, the $Sp(4,\mathbb{Z})$ matrix $g_{m004}$ in \eqref{g_N} is given by

\begin{align}
g_{m004} = \left(
\begin{array}{cccc}
 1 & -1 & 0 & 0  \\
 -2 & 1 & -1 & -1 \\
 2 & 0 & 1 & 0 \\
 0 & 1 & 0 & 0 \\
\end{array}
\right)\;,
\end{align}

which can be decomposed into $g_{m004} = g^s_{J_{m004}} g^t_{K_{m004}} g^{gl}_{U_{m004}}$  with \eqref{T,S and GL type}

\begin{align}
U_{m004} = \left(
\begin{array}{cc}
 1 & -1  \\
 0 & 1  \\
\end{array}
\right)\;, \quad K_{m004} = \left(
\begin{array}{cc}
 2 & 2 \\
 2 & 1  \\
\end{array}
\right)\;, \quad J_{m004} = \left(
\begin{array}{cc}
 0 & 0  \\
 0 & 1  \\
\end{array}
\right)\;.
\end{align}

Following each steps in eq.~\eqref{DGG : step 1},\eqref{DGG : step 2} and \eqref{DGG : final}, $T^{DGG}[m004,X_\mu;P_\lambda]$ is given by 

\begin{align}
\begin{split}
&\mathcal{L}_{T_{\rm step 1}} (V_1, V_2) = \mathcal{L}_{T^{\otimes 2}_\Delta}
\\
&=\frac{1}{4\pi}\int d^4\theta (- \frac{1}2 \Sigma_{1} V_{1} - \frac{1}2 \Sigma_{2} V_{2} ) +\int d^4\theta (\Phi_{1}^\dagger e^{V_{1}} \Phi_1+\Phi_{2}^\dagger e^{V_{2}} \Phi_2)\;,
\\
&\mathcal{L}_{T^{DGG}[m004, X_\mu ;P_\lambda]} (V_{X}, V_C) = \mathcal{L}_{T_{\rm step 2}} (V_{X}, V_C) 
\\
&=\frac{1}{4\pi} \int d^4 \theta \left(- \frac{1}2 \Sigma_C V_X + \Sigma (2V_C + 3 V_X) \right) + \int d^4 \theta \left( \Phi_1^\dagger e^{V+\frac{V_X}2}\Phi_1 +\Phi_2^\dagger e^{V- \frac{V_X}2}\Phi_2 \right)\;.\label{TDGG[m004]}
\end{split}
\end{align}

Here $V(\textrm{with }\Sigma:=\bar{D}D V)$ is a dynamical $U(1)$ vector multiplet while $V_X(\Sigma_X)$ and $V_C(\Sigma_C)$ are background multiplets coupled to flavor symmetries, $U(1)_{X_A}$ and say $u(1)_C$ respectively. Note that both of $C_1$ and $C_2$ are hard internal edges and we can not break the $u(1)_C$ associated to them. 

\paragraph{Example : $N=S^3 \backslash \mathbf{4}_1 =m004$ with an ideal triangulation with 6 tetrahedra}
The absence of chiral primary operators corresponding to hard edges in the above construction of $T^{DGG}[m004, X_\mu ;P_\lambda]$
using 2 tetrahedra were already noticed in \cite{Dimofte:2011ju}.  
The interpretation there was that this is due to the ``bad" choice of triangulation, which contains hard internal edges, 
and can be cured by choosing a proper ideal triangulation which does not have a hard internal edge. 
As a ``good" ideal triangulation for $m004$, they propose the one using six tetrahedra, $\Delta_{R,S,X,Y,Z,W}$ . 
The internal edges in the triangulation are \cite{Dimofte:2011ju}
\beq
\begin{array}{ll}
C_1 =X+W +2(R' +S' +Z''), \qquad & C_2 =R+Y +2(Z' +W' +S''),  \\
C_3=S+W+2(R''+X''+Y'), \qquad & C_4=R+Z+2(Y''+W''+X'),  \\
C_5=X+Y, \qquad &C_6=S+Z. 
\end{array}
\eeq
Note that there is no hard internal edges in the triangulation and 5 internal edges are linearly independent. 
Superficial counting suggests that the resulting theory have a flavor symmetry of rank $6 -5 = 1$, where five $u(1)$s are broken by superpotential operators.

Our interpretation on this problem is different from \cite{Dimofte:2011ju}. We claim that the theory realized by six tetrahedra is 
actually completely the same as the one realized by two tetrahedra in the low energy limit. Therefore, the theory constructed by six tetrahedra 
has a hidden additional $u(1)$ symmetry in the low energy limit which corresponds to the hard edge in the triangulation with two tetrahedra.

To see it, let us focus on the two tetrahedra $\Delta_X$ and $\Delta_Y$, which are glued in such a way that the system has the internal edge $C_5=X+Y$.
Then, this theory is described by two chiral fields $\Phi_X$ and $\Phi_Y$ with the Lagrangian
\beq
\int d^4\theta (\Phi_X^\dagger \Phi_X+\Phi_Y^\dagger \Phi_Y) + \int d^2\theta \Phi_X \Phi_Y + {\rm h.c.},
\eeq
where we have neglected background fields. The superpotential is due to the presence of the internal edge $C_5=X+Y$.
Then it is clear that these fields $\Phi_X$ and $\Phi_Y$ can be integrated out and the theory becomes empty in the low energy limit.
This means that two tetrahedra $\Delta_X$ and $\Delta_Y$ are eliminated. 
Mathematically this corresponds to the 0-2 move. The invariance of a topological quantity called  3d index (see appendix~\ref{sec : 3d index}) under the 0-2 move is proven in  \cite{2013arXiv1303.5278G}. The definition  of the topological quantity is based on ideal triangulation and is   equivalent to the localization expression for the  superconformal index of  $T^{DGG}$ theory. 
Intuitively, the constraints $0 < \Im[X], \Im[Y] < \pi$ and $C_5=2\pi i $ mean that $\Im[X], \Im[Y] \to \pi$,
and hence these tetrahedra are squashed to be flat. 
The same comment also applies to $\Delta_S$, $\Delta_Z$ and $C_6=S+Z$.

At the level of edge variables, the process of integrating out the massive fields may be done by 
eliminating the variables corresponding to the massive fields. More explicitly, we define
\beq
&C'_1:=C_3+C_4+2C_5-C_6 - 4\pi i=W+R+2W''+2R'' \\
&C'_2:=C_1+C_2 -C_5+2C_6 - 4\pi i=W+R+2W'+2R', 
\eeq
After renaming $W \to Z_1'',~R \to Z_2'$ and so on, these variables $C'_1$ and $C'_2$ become the same
as the ones in the triangulation with two tetrahedra.
