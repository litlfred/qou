---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-049-82-a-fermionic-binary-code
section_title: "A fermionic binary code"
section_number: 8.2
pages: 71-76
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
text_source: latex
latex_prose_ratio: 0.609
latex_coverage_ratio: 1.0
---
It turns out that there is a very efficient way of describing the standard model's fermions, which is helpful in understanding $SU(5)$, $Spin(10)$, Pati-Salam theories, and incidentally, also upcoming $\RCHO$ models based on $\C l(12)$.   This is in terms of a binary code, \cite{agut}, \cite{Robinson}.  For a thorough explanation of this topic, the reader is encouraged to consult \cite{agut}.  

This fermionic binary code can be thought of as a sequence of answers to five different yes or no questions:


\newpage

\hspace{1cm} Is the fermion red?

\hspace{1cm} Is the fermion green?

\hspace{1cm} Is the fermion blue?

\hspace{1cm}  Does the fermion have isospin up?

\hspace{1cm}  Does the fermion have isospin down?

\vspace{ 0.7cm}




The set of answers to these five questions can be represented by an exterior algebra, $\Lambda \C^5$, which is $2^5=32$-complex dimensional.  For example, a fermion which is  red, $r$, and has isospin up, $u$, would be represented by $r\wedge u$.  A fermion which is said to be both red, $r$, and blue, $b$, and has both isospin up, $u$, and isospin down, $d$, would be represented by $r\wedge b \wedge u \wedge d$, and so on.  (It may seem odd for a particle to be both red and blue, or to have both isospin up and isospin down, but this should become clear shortly.)  Please see Figure~\ref{c5}.






\begin{figure}[h!]\begin{center}
\includegraphics[width=15cm]{extalg2-eps-converted-to.pdf}
\caption{\label{c5} The exterior algebra $\Lambda \C^5$, representing a fermionic binary code. }
\end{center}\end{figure}

Now, complex linear combinations of the basis vectors, $r, \hspace{1mm}g,  \hspace{1mm}b,  \hspace{1mm}u,  \hspace{1mm}d,$ may be acted upon by $SU(5)$, where they form the irreducible representation, $\underline{5}$.  By extension, the bivectors of $\Lambda \C^5$ form the $\underline{10}$, the three-vectors form the $\underline{10}^*$, the four-vectors form the $\underline{5}^*$, whereas both the unit, 1, and the five-vector form singlets.  We then see that we have exactly the right $SU(5)$ representations to describe one generation of standard model particles, together with the right-handed neutrino, including all corresponding antiparticles.  Please see Figure~\ref{c5su5}.   

\begin{figure}[h!]\begin{center}
\includegraphics[width=16.5cm]{extalgsu5_3-eps-converted-to.pdf}
\caption{\label{c5su5} The exterior algebra $\Lambda \C^5$, representing a fermionic binary code, broken down into irreps of $SU(5)$.  Here, basis elements which are part of the same irreducible representations are connected by red lines.}
\end{center}\end{figure}


Upon spontaneous symmetry breaking, the $\underline{5}$ breaks into  $\left(\hspace{1mm} \underline{3}, \hspace{1mm}\underline{1}, \hspace{1mm}-\frac{1}{3} \hspace{1mm}\right)$  and   $\left(\hspace{1mm} \underline{1}, \hspace{1mm}\underline{2}, \hspace{1mm}\frac{1}{2} \hspace{1mm}\right)$, and the rest of $\Lambda \C^5$ can then be seen to follow suit.  This then allows us to identify each element of $\Lambda \C^5$ with one of the standard model's fermions, as shown in Figure~\ref{c5sm}.

\begin{figure}[h!]\begin{center}
\includegraphics[width=16cm]{extalgsm3-eps-converted-to.pdf}
\caption{\label{c5sm} The exterior algebra $\Lambda \C^5$, representing a fermionic binary code, with the corresponding standard model particles written underneath.  Here, basis elements which are part of the same irreps under $G_{SM}$ are connected by blue lines.}
\end{center}\end{figure}

Readers may notice that $SU(5)$ respects the grading of $\Lambda \C^5$, and that all left-handed particles reside in the even grades, while all right-handed particles reside in the odd grades.


\section{$Spin(10)$ unification  }


Although the $SU(5)$ model was able to draw together the three gauge groups of the standard model into a single group, it only partially unified the standard model's fermions into the $\underline{5}^*$ and the $\underline{10}$.  One might wonder if an alternate Lie group might exist, which could fully unify not only the standard model's gauge bosons, but also its fermions. 










One Lie group which does hit the mark is $Spin(10)$.  The $Spin(10)$ grand unified theory is more commonly known in the literature as the ``$SO(10)$" model, and was proposed by H. Georgi in 1974/1975, \cite{georgi10}, and independently by H. Fritzsch  and P. Minkowski in 1975, \cite{mink}.  

$Spin(10)$ is the double cover of the group $SO(10)$, and is of rank 5, \cite{Lang}.  It unifies the standard model's gauge group, and extends it from 12 dimensions to 45.  A generation of quarks and leptons in this model is unified into a 16-dimensional spinor, with a conjugate spinor accounting for the required anti-particles.  This spinor representation can be seen to naturally account for a right-handed neutrino, \cite{agut}.






The group, $Spin(10)$, is associated with the Clifford algebra $\C l (10)$, which has an irreducible representation given by a 32-dimensional Dirac spinor.  Under $Spin(10)$, this Dirac spinor breaks down into two irreducible representations, known as Weyl spinors, which are each 16-dimensional. Now, it can be shown, \cite{agut}, that Dirac spinors of the group $Spin(2n)$ can be represented by the exterior algebra, $\Lambda \C ^n$.  Hence, we see that the exterior algebra, $\Lambda \C^5$, which we just described in the previous section, is capable of acting not only as a representation of $SU(5)$, but also as a representation of $Spin(10)$.  Please see Figure~\ref{c5sp10}.

Readers may recognize that this same pattern has appeared more than once in this thesis.  That is, minimal left ideals, such as $\Psi _L$ and $S^u$, have been built using raising operators of the Clifford algebras $\CLtwo$ and $\CLsix$, respectively.  These raising operators may be viewed as generating exterior algebras.  For example, by looking at equation~(\ref{su}) of Section~\ref{syst}, it is easy to see how the Dirac spinor, $S^u$, is built from the exterior algebra, $\Lambda \C^3$, generated by $\alpha_1^{\dagger}$, $\alpha_2^{\dagger}$, and $\alpha_3^{\dagger}$. 

\begin{figure}[h!]\begin{center}
\includegraphics[width=16.5cm]{extalgs10-eps-converted-to.pdf}
\caption{\label{c5sp10} The exterior algebra $\Lambda \C^5$, representing a fermionic binary code, with the corresponding standard model particles written underneath.  Here, basis elements connected by lines in the even part of the algebra form one irreducible representation under $Spin(10)$, with left-handed chirality.  Similarly, those basis elements in the odd part of the algebra form another irreducible representation under $Spin(10)$, with right-handed chirality.}
\end{center}\end{figure}

Now, it can be shown that our representation of $SU(5)$ resides inside that of $Spin(10)$, \cite{agut}.  As with $SU(5)$, the group $Spin(10)$ can be seen to respect the chirality of particles;  it does not mix left- and right-handed species.  However, it does not respect the grading of $\Lambda \C^5$, as do $SU(5)$ and $G_{SM}$.
