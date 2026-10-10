---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-049-82-a-fermionic-binary-code
section_title: "A fermionic binary code"
section_number: 8.2
pages: 71-76
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.604
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
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
