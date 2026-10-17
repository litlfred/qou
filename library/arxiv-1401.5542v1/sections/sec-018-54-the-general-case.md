---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-018-54-the-general-case
section_title: "The general case"
section_number: 5.4
pages: 13-15
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.633
latex_coverage_ratio: 0.891
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
\label{sec:ProofOfMainThm}The general case follows the same strategy, but is more complicated since it involves edge paths between multiple cusps. 


\begin{lemma}\label{lemma:BootStrapEdge}
If $\varepsilon$ is a self edge from cusp $i$ to itself, $m_ic_\varepsilon\in k_\rho$
\end{lemma}
\begin{proof}
The proof is identical to that of Lemma~\ref{lemma:BootStrapEdgeOneCusp}.
\end{proof}

\begin{lemma}\label{lemma:connectTwoCusp}
If two (distinct) cusps $i$ and $j$ are joined by an edge $\varepsilon$ in $G$, we have
\begin{equation}m_i m_j\in k_\rho.
\end{equation} 
\end{lemma}

\begin{proof}
Consider the loop $\varepsilon_j\bar{M}_j\bar{\varepsilon_j}M_i$ shown in Figure~\ref{fig:TwoCuspCase}. A simple computation shows that
\begin{equation}
\Tr(\alpha(c_\varepsilon)\beta(-m_{j})\alpha(-c_{\varepsilon})\beta(m_i))=2+m_i m_{j} c_{\varepsilon}^2.
\end{equation}
Since $\varepsilon\in T$, $c_\varepsilon=1$, and the result follows.
\end{proof}
More generally, the following holds.
\begin{lemma}\label{lemma:AllMiInKRho}
We have $m_i\in k_\rho$ for all cusps $i$.
\end{lemma}

\begin{proof}
If $G$ is a tree with 1-cycle, then $c_1=1$, so Lemma~\ref{lemma:BootStrapEdge} implies that $m_1\in k_\rho$. Inductively applying Lemma~\ref{lemma:connectTwoCusp} for the edge $\varepsilon_j$ connecting cusp $i=j-1$ and $j$ implies the result. If $G$ is a tree with $3$-cycle, the Ptolemy coordinates $c_1,c_2$ and $c_3$ are $1$, so the edges of the face are labeled by $\alpha(1)$ and $\beta(-1)$ only (see Figure~\ref{fig:PtolemyToCocycle}). Inserting the peripheral loops $M_i$ as in Figure~\ref{fig:TreeWithThreeCycleCase}, we obtain
\begin{equation}
\Tr\big(\beta(-1)\beta(m_1)\alpha(1)\beta(-1)\beta(m_2)\alpha(1)\beta(-1)\beta(m_3)\alpha(1)\big)\in k_\rho
\end{equation}
By an elementary computation, the trace equals
\begin{equation}
m_1m_2m_3-m_1m_2-m_2m_3-m_3m_1+2\in k_\rho.
\end{equation}
By Lemma~\ref{lemma:connectTwoCusp}, $m_im_j\in k_\rho$, so $m_1\in k_\rho$. The result now follows as above by inductively applying Lemma~\ref{lemma:connectTwoCusp}.
\end{proof}

Let $\varepsilon$ be an arbitrary $1$-cell. If $\varepsilon$ is a self edge, Lemmas~\ref{lemma:BootStrapEdge} and \ref{lemma:AllMiInKRho} imply that $c_\varepsilon\in k_\rho$. Otherwise, there exists an edge path $p$ in the maximal tree $G\setminus\varepsilon_1$, such that $p*\varepsilon$ is a loop in $\widehat M$. By relabeling the cusps and edges if necessary, we may assume that $p=\varepsilon_{i+1}\!*\!\varepsilon_{i+2}\!*\cdots\!*\!\varepsilon_{j}$, where $\varepsilon_{k}$ goes from cusp $k-1$ to cusp $k$. Pick peripheral paths $X_{k}$ on cusp $k$ connecting the ends (in $M$, not $\widehat M$) of edges $\varepsilon_{k}$ and $\varepsilon_{k+1}$ (see Figure~\ref{fig:ArbitraryEdgeCase}). We obtain a loop that can be composed with arbitrary powers of the peripheral loops $M_{i}, \dots, M_{j}$. We thus obtain the following traces (where $b_k\in\Z$)
\begin{equation}
\Tr(\beta(x_{i}+b_{i}m_{i})\alpha(c_{i+1})\beta(x_{i+1}+b_{i+1}m_{i+1})\alpha(c_{i+2})\cdots \beta(x_{j}+b_jm_j)\alpha(c_\varepsilon))\in k_\rho.
\end{equation}

\begin{figure}[htb]
\begin{center}
\hspace{-10mm}
\begin{minipage}[c]{0.4\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(340.52692,277.40344)
 \put(0,0){\includegraphics{figures_gen/ThreeCuspCycle_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(182.5451029,184.4897843){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(178.759021,57.27859){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(44.74235,127.858837){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(64.56978,217.033079){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(-1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(247.718131,123.025426){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(-1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(70.71563,22.56969){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(-1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(173.530509,267.189497){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_1)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(279.517293,29.66383){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_2)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(16.27348,89.252617){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_3)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(99.697986,48.33525){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(99.372859,188.800326){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(215.163868,122.470312){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(92.135175,125.210053){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(168.905141,160.137307){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_2$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(162.520277,74.00083){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(23.21089,59.00358){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_3$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(138.154585,247.301417){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(250.314966,60.01249){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_2$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\begin{minipage}[c]{0.6\textwidth}
\scalebox{0.8}{\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(467.052,214.4512)
 \put(0,0){\includegraphics{figures_gen/ManyCuspCase_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(82.821724,84.7552665){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(c_{i+1})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(13.5915,138.34793){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(x_i)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(80.164288,185.658862){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_i)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(39.987221,109.856966){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_i$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.759839,106.586428){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_{i+1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(52.483056,161.747852){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_i$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(175.90683,53.904203){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(c_\varepsilon)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(183.6829,28.394938){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(181.757894,84.7552665){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(c_{i+2})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(99.761713,138.34793){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(x_{i+1})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(179.100458,185.658862){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_{i+1})$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(132.5404125,109.856966){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_{i+1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(185.278645,106.586428){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_{i+2}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(153.546886,161.747852){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_{i+1}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(300.82554,138.34793){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(x_j)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(367.39833,185.658862){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\beta(m_j)$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(325.0936,109.856966){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$X_j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(341.31284,161.747852){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$M_j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(362.85956,70.495264){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{Cusp $j$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(277.1942,110.459941){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\varepsilon_{j}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(269.09307,84.5765278){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{365.37732pt}
\textcolor{inkcol1}{\large{$\alpha(c_{j})$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\\
\begin{minipage}[t]{0.35\textwidth}
\captionsetup{width=1\textwidth}
\caption{3-cycle case.}\label{fig:TreeWithThreeCycleCase}
\end{minipage}
\hspace{2mm}
\begin{minipage}[t]{0.5\textwidth}
\captionsetup{width=\textwidth}
\caption[Bla]{Arbitrary edge $\varepsilon$.}\label{fig:ArbitraryEdgeCase}
\end{minipage}
\end{center}
\end{figure}

It will be convenient to regard $\Tr(\beta(x_i)\alpha(c_{i+1})\beta(x_{i+1})\alpha(c_{i+2})\cdots \beta(x_j)\alpha(c_\varepsilon))$ as a function of variables $x_i$ (disregarding that the $x_i$'s are fixed expressions of the Ptolemy coordinates).
\begin{definition}
Given a function $f(x_1,\dots,x_r)$, let $\Delta_{i}f$ be the function given by
\begin{equation}
\Delta_{i}f(h)=f(x_1,\dots,x_i+h,\dots,x_r)-f(x_1,\dots,x_i,\dots,x_r).
\end{equation}
\end{definition}
The following is elementary.
\begin{lemma}\label{lemma:Deltas} If $f(x_1,\dots,x_r)$ is a polynomial where the exponents of all variables $x_i$ are $0$ or $1$, and where the highest degree term is $ax_1x_2\cdots x_r$, we have
\begin{equation}\label{eq:Deltas}
\Delta_r\big(\cdots\Delta_2\big(\Delta_1f(h_1)\big)(h_2)\cdots\big)=ah_1h_2\dots h_r,
\end{equation}
and is thus independent of the $x_i$'s.\qed
\end{lemma}
If, e.g.,~$f(x_1,x_2)=x_1x_2$, we have
\begin{equation}\label{eq:DeltaExample}
\Delta_1f(h_1)=(x_1+h_1)x_2-x_1x_2=h_1x_2,\quad \Delta_2\big(\Delta_1f(h_1)\big)(h_2)=h_1(x_2+h_2)-h_1x_2=h_1h_2.
\end{equation}


\begin{lemma}\label{lemma:TraceFormula} Let $x_1,\dots,x_r$ be variables and $y_1,\dots,y_r$ be constants.
The expression
\begin{equation}
\Tr\big(\beta(x_1)\alpha(y_1)\cdots\beta(x_r)\alpha(y_r)\big)
\end{equation}
is a polynomial in the $x_i$'s whose unique highest degree term is $\prod_{i=1}^ry_i\prod_{i=1}^rx_i$. Moreover, for each monomial term, the exponent of each variable is either $1$ or $0$.
\end{lemma}
\begin{proof}
This follows by induction on $r$.
\end{proof}

Applying Lemmas \ref{lemma:TraceFormula} and \ref{lemma:Deltas} to the function
\begin{equation}
f(x_i,\dots,x_j)=\Tr\big(\beta(x_i)\alpha(c_{i+1})\beta(x_{i+1})\alpha(c_{i+2})\cdots \beta(x_j)\alpha(c_\varepsilon)\big),
\end{equation} 
we obtain 
\begin{equation}
(m_im_{i+1}\cdots m_jc_ic_{i+1}\cdots c_j)c_\varepsilon\in k_\rho.
\end{equation}
Since all $m_i$'s are in $k_\rho$ by Lemma~\ref{lemma:AllMiInKRho}, and all $c_i$'s are $1$ (since $\varepsilon_i\in T$), it follows that $c_\varepsilon$ is in $k_\rho$. This concludes the proof. 



\subsection{Proof of Proposition~\ref{prop:GenericBoundaryNonTrivial}}\label{sec:PtolemyToRepProof}

The fact that $\mathcal R$ factors, follows from the fact that the diagonal action only changes the decoration (by diagonal elements, c.f.~Remark~\ref{rm:IntrinsicDiagonalAction}), not the representation.
Since the preimage of the right map in~\eqref{eq:1to1Obstruction} is parametrized by choices of lifts, i.e.~elements in $Z^1(\widehat M;\Z/2\Z)$, all that remains is to show that the only freedom in the choice of decoration of a boundary-non-trivial representation is the diagonal action. 
This follows from results in ~\cite{GaroufalidisThurstonZickert}: A decoration is an equivariant map
\begin{equation}
D\colon \widehat{\widetilde{M}}^{(0)}\to \PSL(2,\C)\big/P,
\end{equation}
and is thus determined by its image of lifts $\widetilde e_1,\dots,\widetilde e_v$ of the cusps of $M$. The freedom in the choice of $D(\widetilde e_i)$ is the choice of a coset $gP$ satisfying that $g\rho(\Stab(\widetilde e_i))g^{-1}\subset P$, where $\Stab(\widetilde e_i)\subset\pi_1(M)$ is the stabilizer of $\widetilde e_i$, i.e.~a peripheral subgroup corresponding to cusp $i$. Hence, if $\rho(\Stab(\widetilde e_i))$ is non-trivial, the freedom is right multiplication by a diagonal matrix (if it is trivial, any coset works). Hence, if $\rho$ is boundary-non-trivial, the only freedom in choosing a decoration is the diagonal action.
