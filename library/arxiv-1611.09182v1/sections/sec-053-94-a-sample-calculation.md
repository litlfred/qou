---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-053-94-a-sample-calculation
section_title: "A sample calculation"
section_number: 9.4
pages: 84-89
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.96
---
We introduce to the reader how calculations are carried out in $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$  by working through an example.  Let us find the action of the first $SU(3)$ generator of the form $\Lambda \nu$, which we will define as $\Lambda_1\nu\equiv\frac{i}{2}\left(e_{15}-e_{34}\right)\nu$, in accordance with equation~(\ref{liealg}).  Let $\Lambda_1\nu$ act on $q^R_{1}$, as defined in equations~(\ref{triplet}):
\begin{equation}\begin{array}{ll}\label{calc} & \Big[ \Lambda_1\nu \hspace{1mm},\hspace{1mm} q^R_{1} \Big]\vspace{\spacer}   \\
=& \Big[\frac{i}{2}\left(e_{15}-e_{34}\right)\nu\hspace{0.5mm} ,\hspace{1mm}\left(-ie_{12}-e_{16}+e_{23}+ie_{36}\right)\nu \Big]\vspace{\spacer} \\
=&\frac{i}{2}\Big( \left(e_{15}-e_{34}\right)\left(-ie_{12}-e_{16}+e_{23}+ie_{36}\right)\vspace{\spacer} \\
 &- \left(-ie_{12}-e_{16}+e_{23}+ie_{36}\right)\left(e_{15}-e_{34}\right) \Big)\hspace{0.2mm}\nu\vspace{\spacer} \\


=&\frac{i}{2}\big(-ie_{1512}-e_{1516}+e_{1523}+ie_{1536}\vspace{\spacer} \\
&\hspace{0.85cm}+ie_{3412}+e_{3416}-e_{3423}-ie_{3436}\vspace{\spacer} \\
&\hspace{0.85cm}+ie_{1215}+e_{1615}-e_{2315}-ie_{3615}\vspace{\spacer} \\
&\hspace{0.85cm}-ie_{1234}-e_{1634}+e_{2334}+ie_{3634}\big)\hspace{0.2mm}\nu\vspace{\spacer} \\




=&\frac{i}{2}\big(-ie_{52}-e_{56}+e_{1235}-ie_{1356}\vspace{\spacer} \\
&\hspace{0.85cm}+ie_{1234}+e_{1346}+e_{42}-ie_{46}\vspace{\spacer} \\
&\hspace{0.85cm}+ie_{25}+e_{65}-e_{1235}+ie_{1356}\vspace{\spacer} \\
&\hspace{0.85cm}-ie_{1234}-e_{1346}-e_{24}+ie_{64}\big)\hspace{0.2mm}\nu\vspace{\spacer} \\
=&i\big(ie_{25}-e_{56}-e_{24}-ie_{46}\big)\hspace{0.2mm}\nu=q^G_{1}.\vspace{\spacer} \\
\end{array}\end{equation}


\noindent This is the result we would expect for the first of the $su(3)$ Gell-Mann matrices, $\Lambda^{GM}_1$, from the standard model, acting to convert a red basis vector, $\underline{R}\equiv (1,0,0)^\top$, into a green basis vector, $\underline{G}\equiv (0,1,0)^\top$.
\begin{equation} \Lambda^{GM}_1\underline{R} = \left(
\begin{array}{ccc}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0
\end{array} \right)\left(
\begin{array}{c}
1  \\
0  \\
0
\end{array} \right) = \left(
\begin{array}{c}
0  \\
1  \\
0
\end{array} \right) = \underline{G}.
\end{equation}





\section{Summary for $SU(3)_c$ }

Finally, we conclude by summarizing the main result of this chapter in Figure~\ref{64}: the breakdown of the 64-dimensional $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ into irreducible representations of $SU(3)$.

\begin{figure}[h!]\begin{center}
\includegraphics[width=10cm]{moon_corners2-eps-converted-to.pdf}
\caption{\label{64} The 64-dimensional octonionic chain algebra splits into two sets of $SU(3)$ generators of the form $i\Lambda\nu$ and $-i\Lambda^*\nu^*$, six $SU(3)$ singlets $\ell_j$, six triplets $q_k$, and their complex conjugates.  These objects are sectioned off above into four quadrants according to their forms: $\nu a \nu$, $\nu^* a \nu$, $\nu a \nu^*$ and $\nu^* a \nu^*$ for $a$ in the chain algebra. Transforming particles into anti-particles, and \it vice versa, \rm requires only the complex conjugate $*$: $i\mapsto-i$ in our formalism.}
\end{center}\end{figure}

Using only the eight-dimensional complex octonions, $\mathbb{C}\otimes\mathbb{O}$, we have explained how to build up a 64-complex-dimensional associative algebra.  The $SU(3)$ generators identified within this algebra then break down the remaining space into six singlets, six triplets, and their antiparticles, with no extra particles beyond these.  

These representations are a curious finding.  They effortlessly suggest the existence of exactly three generations, they relate particles to antiparticles by using only the complex conjugate $i\mapsto -i$, and finally, they fill these tall orders while working from but a modest eight-complex-dimensional algebra.


















\vspace{1cm}


\section{Three generations under $SU(3)_c$ and $U(1)_{em}$  \label{ass}}








Since the time that these irreducible representations of $SU(3)_c$ were identified within $\COOO$, more standard model structure has been uncovered in the algebra.  It turns out that we can extend our three-generation results for $SU(3)_c$ to include $U(1)_{em}$ as well (presented for the first time here).  

That is, our $SU(3)_c$ action on $\COOO$ given by 

\begin{equation}\begin{array}{lll}\label{simpleaction}\large[\hspace{1mm}\Lambda_j \nu,\hspace{1mm} a \nu \hspace{1mm}\large], & \hspace{1cm}&\large[\hspace{1mm}-\Lambda_j^* \nu^*, \hspace{1mm}a \nu^* \hspace{1mm}\large] 
\end{array}\end{equation}

\noindent can be generalized, so as to include electric charges.  Furthermore, we will be able to incorporate $U(1)_{em}$ by making use of the $Q$ we had already introduced in our one-generation model of Section~\ref{ladders}, 
\begin{equation}Q=\frac{N}{3} = \sum_{i=1}^3 \alpha^{\dagger}_i\alpha_i.
\end{equation}

Consider the following action for the $SU(3)_c$ generators,

\begin{equation}\begin{array}{lll} \label{newaction} \left[\hspace{1mm}\Lambda_j \nu,\hspace{1mm} S^*a \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}-\Lambda_j^* \nu^*, \hspace{1mm}Sa \nu^* \hspace{1mm}\right],  \vspace{4mm}\\

\left[\hspace{1mm}\Lambda_j \nu,\hspace{1mm} Sa \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}-\Lambda_j^* \nu^*, \hspace{1mm}S^*a \nu^* \hspace{1mm}\right],
\end{array}\end{equation}

\noindent where $S$ is the projector given by
\begin{equation} S\equiv \frac{1}{2}-\frac{ie_7}{4}+\frac{i}{4}\left(e_{13}+e_{26}+e_{45}\right).
\end{equation}

 \noindent Clearly, $S+S^* = 1$, so that we see that this new action~(\ref{newaction}) is no different from the original action~(\ref{simpleaction}).  Although it has not been mentioned before, $S$ is a projector which has come up frequently in complex-octonionic work;  it is nothing more than the right-multiplication analogue of $\nu = \frac{1}{2}\left(1+ie_7\right)$.  Or in other words, 
 
 \begin{equation}
 f \hspace{1mm}\frac{1}{2}\left(1+ie_7\right) = Sf \hspace{1cm} \forall f\in \CO.
 \end{equation}
 
 
 
 
 
 It so happens that $-\Lambda_j^* = \Lambda_j$ $\forall j = 1 \dots 8$, so that the action~(\ref{newaction}) may be rewritten as 
 
 \begin{equation}\begin{array}{lll} \label{newnewaction} \left[\hspace{1mm}\Lambda_j \nu,\hspace{1mm} S^*a \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}-\Lambda_j^* \nu^*, \hspace{1mm}Sa \nu^* \hspace{1mm}\right],  \vspace{4mm}\\

\left[\hspace{1mm}-\Lambda_j^* \nu,\hspace{1mm} Sa \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}\Lambda_j \nu^*, \hspace{1mm}S^*a \nu^* \hspace{1mm}\right].
\end{array}\end{equation}
 
Now, an action for electric charge may be found, which matches the $SU(3)_c$ action of (\ref{newnewaction}).  Namely, 

\begin{equation}\begin{array}{lll} \label{elecaction} \left[\hspace{1mm}Q \nu,\hspace{1mm} S^*a \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}-Q^* \nu^*, \hspace{1mm}Sa \nu^* \hspace{1mm}\right],  \vspace{4mm}\\

\left[\hspace{1mm}-Q^* \nu,\hspace{1mm} Sa \nu \hspace{1mm}\right], & \hspace{1cm}&\left[\hspace{1mm}Q \nu^*, \hspace{1mm}S^*a \nu^* \hspace{1mm}\right].
\end{array}\end{equation}

\noindent Under these actions (\ref{newnewaction}) and (\ref{elecaction}), we find $SU(3)_c$ and $U(1)_{em}$ charge assignments, which are consistent with three generations of standard model particles.  Below, we relabel the states given earlier in equations~(\ref{lept})-(\ref{antitriplet2}), so as to now specify their electric charges.  

At this level, we are not specifying which generation each state belongs to, so for $i=1,2,3$, the three states with electric charge of -1 will be labelled $e^-_i$;  the three states with electric charge of +1 will be labelled $e^+_i$; the three states with electric charge of $2/3$ will be labelled $u_i$;  the three states with electric charge of $-2/3$ will be labelled $\bar{u}_i$;  the three states with electric charge $-1/3$ will be labelled $d_i$, and  the three states with electric charge $1/3$ will be labelled $\bar{d}_i$.  Since $SU(3)_c$ and $U(1)_{em}$ do not distinguish between neutrinos, $\nu_i$ and anti-neutrinos, $\bar{\nu}_i$, we will then label the six states with electric charge of zero as $n _i$ and $\bar{n} _i$, where the symbol $n_i$ could represent either a neutrino or anti-neutrino.

 
\begin{equation}\begin{array}{l}\label{newlept}
n_1\longleftarrow\ell_{a}\equiv\left(1+ie_{13}+ie_{26}+ie_{45}\right)\nu = S\hspace{1mm}\ell_{a}\hspace{1mm}\nu,   \vspace{\spacer}\\
n_2\longleftarrow\ell_{b}\equiv\left(3-ie_{13}-ie_{26}-ie_{45}\right)\nu = S^*\hspace{1mm}\ell_{b}\hspace{1mm}\nu, \vspace{\spacer}\\
n_3\longleftarrow\ell_{c}\equiv \left(-ie_{124}-e_{125}+e_{146}-ie_{156}\right)\nu = S^*\hspace{1mm}\ell_{c}\hspace{1mm}\nu, \vspace{\spacer} \\
e^+_1\longleftarrow\ell_{d}\equiv \left(-ie_{1}-e_{3}+e_{126}+e_{145}\right)\nu = S\hspace{1mm}\ell_{d}\hspace{1mm}\nu, \vspace{\spacer} \\
e^+_2\longleftarrow\ell_{e}\equiv \left(ie_{2}+e_{6}+e_{123}+ie_{136}\right)\nu = S\hspace{1mm}\ell_{e}\hspace{1mm}\nu, \vspace{\spacer} \\
e^+_3\longleftarrow\ell_{f}\equiv \left(ie_{4}+e_{5}-e_{134}+ie_{135}\right)\nu = S\hspace{1mm}\ell_{f}\hspace{1mm}\nu, \vspace{\spacer} \\
\end{array}\end{equation}

\begin{equation}\begin{array}{l}\label{newtriplet}
u_1^R\longleftarrow q^R_{1}\equiv\left(-ie_{12}-e_{16}+e_{23}+ie_{36}\right)\nu  = S^*\hspace{1mm} q^R_{1}\hspace{1mm}\nu  \vspace{\spacer} \\
u_1^G\longleftarrow q^G_{1}\equiv\left(-ie_{24}-e_{25}+e_{46}-ie_{56}\right)\nu = S^*\hspace{1mm} q^G_{1}\hspace{1mm}\nu\vspace{\spacer} \\
u_1^B\longleftarrow q^B_{1}\equiv\left(ie_{14}+e_{15}+e_{34}-ie_{35}\right)\nu = S^*\hspace{1mm} q^B_{1}\hspace{1mm}\nu\vspace{\spacer} \\
\end{array}\end{equation}

\begin{equation}\begin{array}{l}\label{newtriplet2}
\bar{u}_2^R\longleftarrow \bar{q}^R_{2}\equiv\left(ie_{12}-e_{16}+e_{23}-ie_{36}\right)\nu  =  S \hspace{1mm} \bar{q}^R_{2} \hspace{1mm}\nu  \vspace{\spacer} \\
\bar{u}_2^G\longleftarrow \bar{q}^G_{2}\equiv\left(ie_{24}-e_{25}+e_{46}+ie_{56}\right)\nu =  S \hspace{1mm} \bar{q}^G_{2} \hspace{1mm}\nu \vspace{\spacer} \\
\bar{u}_2^B\longleftarrow \bar{q}^B_{2}\equiv\left(-ie_{14}+e_{15}+e_{34}+ie_{35}\right)\nu=  S \hspace{1mm} \bar{q}^B_{2} \hspace{1mm}\nu, \vspace{\spacer} \\
\end{array}\end{equation}
\begin{equation}\begin{array}{l}\label{newtriplet3}
\bar{u}_3^R\longleftarrow \bar{q}^R_{3}\equiv\left(ie_{4}+e_{5}+e_{134}-ie_{135}\right)\nu  = S^*\hspace{1mm}\bar{q}^R_{3}\hspace{1mm}\nu  \vspace{\spacer} \\
\bar{u}_3^G\longleftarrow \bar{q}^G_{3}\equiv\left(ie_{1}+e_{3}+e_{126}+e_{145}\right)\nu= S^*\hspace{1mm}\bar{q}^G_{3}\hspace{1mm}\nu   \vspace{\spacer} \\
\bar{u}_3^B\longleftarrow \bar{q}^B_{3}\equiv\left(ie_{2}+e_{6}-e_{123}-ie_{136}\right)\nu= S^*\hspace{1mm}\bar{q}^B_{3}\hspace{1mm}\nu,   \vspace{\spacer} \\
\end{array}\end{equation}
\begin{equation}\begin{array}{l}\label{newtriplet4}
\bar{d}_1^R\longleftarrow \bar{q}^R_{4}\equiv\left(ie_{1}-e_{3}+e_{126}-e_{145}\right)\nu  = S\hspace{1mm}\bar{q}^R_{4}\hspace{1mm}\nu \vspace{\spacer} \\
\bar{d}_1^G\longleftarrow \bar{q}^G_{4}\equiv\left(-ie_{4}+e_{5}+e_{134}+ie_{135}\right)\nu = S\hspace{1mm}\bar{q}^G_{4}\hspace{1mm}\nu   \vspace{\spacer} \\
\bar{d}_1^B\longleftarrow \bar{q}^B_{4}\equiv\left(ie_{124}-e_{125}-e_{146}-ie_{156}\right)\nu = S\hspace{1mm}\bar{q}^B_{4}\hspace{1mm}\nu,   \vspace{\spacer} \\
\end{array}\end{equation}
\begin{equation}\begin{array}{l}\label{newtriplet5}
\bar{d}_2^R\longleftarrow \bar{q}^R_{5}\equiv\left(-ie_{2}+e_{6}+e_{123}-ie_{136}\right)\nu =S\hspace{1mm}\bar{q}^R_{5}\hspace{1mm}\nu  \vspace{\spacer} \\
\bar{d}_2^G\longleftarrow \bar{q}^G_{5}\equiv\left(ie_{124}-e_{125}+e_{146}+ie_{156}\right)\nu =S\hspace{1mm}\bar{q}^G_{5}\hspace{1mm}\nu   \vspace{\spacer} \\
\bar{d}_2^B\longleftarrow \bar{q}^B_{5}\equiv\left(ie_{4}-e_{5}+e_{134}+ie_{135}\right)\nu=S\hspace{1mm}\bar{q}^B_{5}\hspace{1mm}\nu ,   \vspace{\spacer} \\
\end{array}\end{equation}
\begin{equation}\begin{array}{l}\label{newtriplet6}
\bar{d}_3^R\longleftarrow \bar{q}^R_{6}\equiv\left(ie_{124}+e_{125}+e_{146}-ie_{156}\right)\nu =S\hspace{1mm}\bar{q}^R_{6}\hspace{1mm}\nu  \vspace{\spacer} \\
\bar{d}_3^G\longleftarrow \bar{q}^G_{6}\equiv\left(ie_{2}-e_{6}+e_{123}-ie_{136}\right)\nu=S\hspace{1mm}\bar{q}^G_{6}\hspace{1mm}\nu    \vspace{\spacer} \\
\bar{d}_3^B\longleftarrow \bar{q}^B_{6}\equiv\left(-ie_{1}+e_{3}+e_{126}-e_{145}\right)\nu=S\hspace{1mm}\bar{q}^B_{6}\hspace{1mm}\nu .   \vspace{\spacer} \\
\end{array}\end{equation}

Taking the complex conjugate, $*$: $i\mapsto-i$, of these 32 basis vectors gives 32 new linearly independent basis vectors:

\begin{equation}\begin{array}{l}\label{newantilept}
\bar{n}_1\longleftarrow\ell_{a}^*=\left(1-ie_{13}-ie_{26}-ie_{45}\right)\nu^* = S^*\hspace{1mm}\ell_{a}^*\hspace{1mm}\nu^*,  \vspace{\spacer}\\
 \bar{n}_2\longleftarrow \ell_{b}^*=\left(3+ie_{13}+ie_{26}+ie_{45}\right)\nu^*= S\hspace{1mm}\ell_{b}^*\hspace{1mm}\nu^*, \vspace{\spacer}\\
\bar{n}_3\longleftarrow\ell_{c}^*= \left(ie_{124}-e_{125}+e_{146}+ie_{156}\right)\nu^*= S\hspace{1mm}\ell_{c}^*\hspace{1mm}\nu^*, \vspace{\spacer} \\
e^-_1\longleftarrow\ell_{d}^*= \left(ie_{1}-e_{3}+e_{126}+e_{145}\right)\nu^*= S^*\hspace{1mm}\ell_{d}^*\hspace{1mm}\nu^*, \vspace{\spacer} \\
e^-_2\longleftarrow\ell_{e}^*= \left(-ie_{2}+e_{6}+e_{123}-ie_{136}\right)\nu^*= S^*\hspace{1mm}\ell_{e}^*\hspace{1mm}\nu^*, \vspace{\spacer} \\
e^-_3\longleftarrow\ell_{f}^*= \left(-ie_{4}+e_{5}-e_{134}-ie_{135}\right)\nu^*= S^*\hspace{1mm}\ell_{f}^*\hspace{1mm}\nu^*, \vspace{\spacer} \\
\end{array}\end{equation}

\begin{equation}\begin{array}{l}\label{newantitriplet}
\bar{u}_1^R\longleftarrow q^{R*}_{1}=\left(ie_{12}-e_{16}+e_{23}-ie_{36}\right)\nu^* \equiv\bar{q}^R_1= S\hspace{1mm}\bar{q}^R_1\hspace{1mm}\nu^*   \vspace{\spacer} \\
\bar{u}_1^G\longleftarrow q^{G*}_{1}=\left(ie_{24}-e_{25}+e_{46}+ie_{56}\right)\nu^* \equiv\bar{q}^G_1= S\hspace{1mm}\bar{q}^G_1\hspace{1mm}\nu^* \vspace{\spacer} \\
\bar{u}_1^B\longleftarrow q^{B*}_{1}=\left(-ie_{14}+e_{15}+e_{34}+ie_{35}\right)\nu^* \equiv\bar{q}^B_1= S\hspace{1mm}\bar{q}^B_1\hspace{1mm}\nu^* \vspace{\spacer} \\
\end{array}\end{equation}

\begin{equation}\begin{array}{l}\label{newantitriplet2}
u_2^R\longleftarrow \bar{q}^{R^*}_{2}=\left(-ie_{12}-e_{16}+e_{23}+ie_{36}\right)\nu^*\equiv q_2^R  = S^*\hspace{1mm}q_2^R\hspace{1mm}\nu^*  \vspace{\spacer} \\
u_2^G\longleftarrow \bar{q}^{G^*}_{2}=\left(-ie_{24}-e_{25}+e_{46}-ie_{56}\right)\nu^*\equiv q_2^G= S^*\hspace{1mm}q_2^G\hspace{1mm}\nu^* \vspace{\spacer} \\
u_2^B\longleftarrow \bar{q}^{B^*}_{2}=\left(ie_{14}+e_{15}+e_{34}-ie_{35}\right)\nu^*\equiv q_2^B= S^*\hspace{1mm}q_2^B\hspace{1mm}\nu^* \vspace{\spacer} \\
\end{array}\end{equation}
\noindent and so on.
