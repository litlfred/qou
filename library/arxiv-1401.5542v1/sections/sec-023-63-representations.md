---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-023-63-representations
section_title: "Representations"
section_number: 6.3
pages: 17-20
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.803
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
\begin{definition}\label{def:BoundaryNonDeg}
Let $\rho$ be an $(\SL(n,\C),N)$-representation, and let $I_i$ denote the image of the peripheral subgroup corresponding to cusp $i$. We say that $\rho$ is \emph{boundary-non-degenerate} if each $I_i$ has an element whose Jordan canonical form has a single (maximal) Jordan block.
\end{definition}
\begin{proposition}
The map 
\begin{equation}
\mathcal R\colon P_n(\T)_\rd\to \big\{(\SL(n,\C),N)\text{-representations}\big\}
\big/\Conj.
\end{equation}
maps onto the generic representations, and the preimage of a generic boundary-non-degenerate representation consists of a single point.
\end{proposition}
\begin{proof}
The proof is identical to the proof in Section~\ref{sec:PtolemyToRepProof} for $n=2$.
\end{proof}
\begin{conjecture}
The Ptolemy field of a generic, boundary-non-degenerate representation is equal to its trace field.
\end{conjecture}

\begin{remark}Much of the theory also works for $\PSL(n,\C)$-representations by means of obstruction classes in $H^2(\widehat M;\Z/n\Z)$. When $n$ is even, obstruction classes in $H^2(\widehat M;\Z/2\Z)$ were defined in~\cite{GaroufalidisThurstonZickert} for representations in $p\SL(n,\C)=\SL(n,\C)/\pm I$. 
For $\PSL(n,\C)$-representations, both the Ptolemy field and the trace field are only defined up to $n$th roots of unity.
The generalized obstruction classes are used on the website~\cite{Unhyperbolic} and will be explained in a forthcoming publication. 

\end{remark}


\subsection{Proof that $\alpha^*$ is basic}\label{sec:AlphaStarBasicGeneral}
By Lemma~\ref{lemma:CokernelN} we need to prove the existence of integral points such that the corresponding columns of $\alpha^*$ form a matrix of determinant $\pm n$. As in Section~\ref{sec:AlphaStarBasic} we split the proof into three cases.


\subsubsection{Basic matrix algebra}
Let $I_k$ be the identity matrix, $R_{k}$ the sparse matrix whose first row contains entirely of $1$'s, $S_{k}$ the sparse matrix whose lower diagonal consists of $1$'s ($S_1=0$), and $T_k$ the sparse matrix whose lower right entry is $1$. The index $k$ denotes that the matrices are $k\times k$.
\begin{equation}
R_3=\begin{pmatrix}1&1&1\\&&\\&&\end{pmatrix},\quad S_3=\begin{pmatrix}&&\\1&\\&1\end{pmatrix},\quad T_3=\begin{pmatrix}&&\\&&\\&&1\end{pmatrix}
\end{equation}

\begin{lemma}\label{lemma:DeterminantIdentity} We have
\begin{equation}
\det(I_k+R_k-S_k)=k+1,\qquad \det(I_k+R_k+T_k-S_k)=2k+1.
\end{equation}
\end{lemma}
\begin{proof}
This follows e.g.~by expanding the determinant using the last column. The matrices $I_k+R_k-S_k$ are shown below for $k=1,2,3$ and $4$.
\begin{equation}
\begin{pmatrix}2\end{pmatrix},\qquad \begin{pmatrix}2&1\\-1&1\end{pmatrix},\qquad \begin{pmatrix}2&1&1\\-1&1&\\&-1&1\end{pmatrix},\qquad\begin{pmatrix}2&1&1&1\\-1&1&&\\&-1&1&\\&&-1&1\end{pmatrix}
\end{equation}
For $I_k+R_k+T_k-S_k$, the only difference is that the lower right entry is now $2$.
\end{proof}
\begin{lemma}\label{lemma:BlockDeterminant}
Let $A$, $B$, $C$, $D$ be $k\times k$, $k\times l$, $l\times k$, and $l\times l$ matrices, respectively, and let $M=\left(\begin{smallmatrix}A &B\\C&D\end{smallmatrix}\right)$. If $D$ is invertible, we have
\begin{equation}
\pushQED{\qed}
\det(M)=\det(D)\det(A-BD^{-1}C).\qedhere\popQED
\end{equation}
\end{lemma}
\begin{proof}
This follows from the identity $\left(\begin{smallmatrix}A &B\\C&D\end{smallmatrix}\right)=\left(\begin{smallmatrix}I &B\\0&D\end{smallmatrix}\right)\left(\begin{smallmatrix}A-BD^{-1}C &0\\D^{-1}C&I\end{smallmatrix}\right)$.
\end{proof}
  

\subsubsection{One cusp}

Pick any face of $\T$ and consider the integral points shown in Figures~\ref{fig:OneCuspBasicOdd} and \ref{fig:OneCuspBasicEven}. Let $A_n$ be the $(n-1)\times(n-1)$ matrix formed by the corresponding columns of $\alpha^*$. The columns are ordered as shown in the figures, and the rows, i.e. the generators $x\otimes e_i$ of $C^n_0$, are ordered in the natural way (increasing in $i$). The following is an immediate consequence of the definition of $\alpha^*$.
\begin{lemma}
The matrix $A_n$ is given by
\begin{equation}
A_{2k+1}=\begin{pmatrix}I_k+R_k+T_k&I_k\\S_k&I_k\end{pmatrix},\qquad A_{2k}=\begin{pmatrix}2&0\cdots01&0\\0&I_{k-1}+R_{k-1}&I_{k-1}\\0&S_{k-1}&I_{k-1}\end{pmatrix}
\end{equation}
\end{lemma}
\begin{corollary}
The determinant of $A_n$ is $\pm n$.
\end{corollary}
\begin{proof}
This follows from Lemma~\ref{lemma:BlockDeterminant} and Lemma~\ref{lemma:DeterminantIdentity}.
\end{proof}

\begin{figure}[htpb]
\centering
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(268.6568,184.63654)
 \put(0,0){\includegraphics{figures_gen/OneCuspBasicOdd_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-5.561203,15.525296){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(93.695257,184.072556){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(154.044197,96.256546){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2k$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(189.822007,16.244256){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(183.001667,44.856476){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k\!+\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(173.498027,60.573316){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k\!+\!2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(113.036297,79.637116){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(93.121647,117.219426){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(85.782287,132.176086){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$1$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Basic generators, $n=2k+1$.}\label{fig:OneCuspBasicOdd}
\end{minipage}		
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(268.6568,184.63655)
 \put(0,0){\includegraphics{figures_gen/OneCuspBasicEven_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(99.549357,135.585706){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(106.395467,120.847476){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(196.460937,45.072976){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(162.618107,102.997396){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2k\!-\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(116.851437,88.046496){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k\!-\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(186.474887,62.523116){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$k\!+\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(206.908497,17.034216){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(8.515647,15.962786){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(107.265647,184.059786){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Basic generators, $n=2k$.}\label{fig:OneCuspBasicEven}
\end{minipage}				
\end{figure}



\subsubsection{Multiple cusps, self edges}
Pick a face with a self edge, and extend to a maximal tree with $1$-cycle $G$ as in~Figure~\ref{fig:TreeWithCycle}. Let $T=G\setminus\varepsilon_1$, and let   
$B_n$ denote the matrix formed by the columns of $\alpha^*$ corresponding to the face points shown in Figure~\ref{fig:OneCycleBasic} together with the edge points on $T$.
We order the generators $x_i\otimes e_j$ of $C_0^n$ as follows
\begin{equation}
x_1\otimes e_1,\dots, x_1\otimes e_{n-1},\quad x_2\otimes e_{n-1},\dots ,x_2\otimes e_1
\end{equation}
with a similar scheme for the other vertices. The following is an immediate consequence of the definition of $\alpha^*$.



\begin{lemma}
The matrix $B_n$ is given by
\begin{equation}
B_n=\left(\begin{array}{c|c}
I_{n-1}+R_{n-1}& \\
S_{n-1}&I_T\otimes\Z^{n-1}\\\cline{1-1}
 0 &
\end{array}\right),
\end{equation}
where $I_T\otimes\Z^{n-1}$ is the matrix obtained from $I_T$ by replacing each non-zero entry by $I_{n-1}$.\qed
\end{lemma}
\begin{corollary}
The determinant of $B_n$ is $\pm n$.
\end{corollary}
\begin{proof}
This follows from
\begin{equation}
\det(B_n)=\pm\det(\begin{pmatrix}I_{n-1}+R_{n-1}&I_{n-1}\\S_{n-1}&I_{n-1}\end{pmatrix}=\pm n,
\end{equation}
where the second equality follows from Lemmas~\ref{lemma:BlockDeterminant} and \ref{lemma:DeterminantIdentity}.
\end{proof}
\begin{figure}[htpb]
\centering
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(419.827,187.53966)
 \put(0,0){\includegraphics{figures_gen/OneCycleBasic_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.205343,21.642686){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(95.658267,193.225666){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(191.849327,20.175936){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(78.019267,168.399576){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(89.694227,141.095706){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(102.925917,64.756666){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!-\!2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(113.590717,47.850206){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!-\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(186.771677,46.744906){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(177.396207,65.247636){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!+\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(131.490297,141.366736){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n\!-\!3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(119.579697,168.019386){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n\!-\!2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(34.705867,112.924186){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\varepsilon_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(152.388637,113.934326){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\varepsilon_2$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Basic generators, tree with $1$-cycle.}\label{fig:OneCycleBasic}
\end{minipage}	
\begin{minipage}[c]{0.48\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(366.29214,190.0125)
 \put(0,0){\includegraphics{figures_gen/ThreeCycleBasic_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.205344,21.929366){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(98.017767,195.698506){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(194.689837,29.589416){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$x_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(129.354927,160.917186){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!-\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(95.508487,124.573426){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!-\!2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.875607,80.353336){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(69.458617,60.335406){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(150.430547,17.243666){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n\!-\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(126.090987,17.348266){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(75.528997,17.348276){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$3n\!-\!2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(22.713907,17.113666){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$3n\!-\!3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(15.932547,64.220646){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(6.024096,85.938926){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$n\!+\!1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(29.048917,143.770146){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n\!-\!3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(153.676427,113.876286){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\varepsilon_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(35.488577,113.876286){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\varepsilon_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(96.855347,43.670686){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\Large{$\varepsilon_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(41.746477,167.219866){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$2n\!-\!2$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\captionsetup{width=10cm}
\caption{Basic generators, tree with $3$-cycle.}\label{fig:ThreeCycleBasic}
\end{minipage}					
\end{figure}


\subsubsection{Multiple cusps, no self edge}
Pick a maximal tree with $3$-cycle $G$, and let $C_n$ be the matrix formed by the columns of $\alpha^*$ corresponding to the face points in Figure~\ref{fig:ThreeCycleBasic} together with the edge points on $T=G\setminus\varepsilon_1$.
\begin{lemma}
The matrix $C_n$ is given by
\begin{equation}
C_n=\left(\begin{array}{c|c}
I_{n-1}& \\
S_{n-1}&I_T\otimes\Z^{n-1}\\
R_{n-1}&\\\cline{1-1}
 0 &
\end{array}\right),
\end{equation}
\end{lemma}
\begin{corollary}
The determinant of $C_n$ is $\pm n$.
\end{corollary}
\begin{proof}
We have
\begin{equation}
\det(C_n)=\pm\det(M),\qquad M=\begin{pmatrix}I_{n-1}&I_{n-1}&\\S_{n-1}&I_{n-1}&I_{n-1}\\R_{n-1}&&I_{n-1}\end{pmatrix}.
\end{equation}
Using Lemma~\ref{lemma:BlockDeterminant} with $A=\left(\begin{smallmatrix}I_{n-1}&I_{n-1}\\S_{n-1}&I_{n-1}\end{smallmatrix}\right)$, $B=\left(\begin{smallmatrix}0\\I_{n-1}\end{smallmatrix}\right)$, $C=\left(\begin{smallmatrix}R_{n-1}&0\end{smallmatrix}\right)$, $D=I_{n-1}$, we have
\begin{equation}
\det(M)=\det\begin{pmatrix}I_{n-1}&I_{n-1}\\S_{n-1}-R_{n-1}&I_{n-1}\end{pmatrix}=\det(I_{n-1}+R_{n-1}-S_{n-1})=n,
\end{equation}
where the second equation follows from Lemma~\ref{lemma:BlockDeterminant}, and the third from Lemma~\ref{lemma:DeterminantIdentity}.
\end{proof}
This concludes the proof that $\alpha^*$ is basic.

































































































































































































































\bibliographystyle{plain}
