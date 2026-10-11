---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-047-811-introduction
section_title: "Introduction"
section_number: 8.1.1
pages: 67-70
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.979
---
The $SU(5)$ grand unified theory offers a classic example of what it means to be a grand unified theory.  It was proposed in 1974 by H. Georgi and S. Glashow, \cite{su5}, and can be seen to successfully unify the gauge groups of the standard model.  However, the $SU(5)$ model only partially unifies a generation of quarks and leptons.  

The group $SU(5)$ has rank 4, as with the standard model's gauge group, $G_{SM}$; that is, its Lie algebra has a 4-dimensional Cartan subalgebra, \cite{Lang}.  The Lie algebra of $SU(5)$ essentially doubles the gauge symmetry of the standard model by subsuming the standard model's 12 symmetry generators, and then incorporating another 12, for a total of 24. 

Irreducible representations for $SU(5)$ are listed as 

$$\underline{1}, \hspace{2mm} \underline{5}, \hspace{2mm} \underline{10}, \hspace{2mm} \underline{15}, \hspace{2mm} \underline{24}, \hspace{2mm}  \underline{35}, \hspace{2mm} \underline{40}, \hspace{2mm} \underline{45},\hspace{2mm} \underline{50},  \dots
$$

\noindent Most descriptions of the $SU(5)$ model give a generation of quarks and leptons, which stretches across the $\underline{5}^*$ and the $\underline{10}$, and optionally, the singlet, $\underline{1}$.  This singlet can be included so as to represent the right-handed neutrino.  In contrast, gauge bosons lie in the $\underline{24}$, while the Higgs fields typically are represented by the $\underline{5}$ and the $\underline{24}$.

Despite its anticipated candidacy as a suitable fit to nature, the $SU(5)$ grand unified theory has run into trouble with  experiment.  For example, the theory predicts proton decay, with a lifetime of  $10^{31\pm2}$ years, depending on the details and source of the calculation, \cite{Mann}, \cite{Lang}.    This is generally seen to be at odds with the findings of the Super-kamiokande experiment, \cite{skk1}, \cite{skk2}, which gives a proton lifetime of $\geq5.9\times10^{33}$ years at the $90\%$ confidence level.




\subsection{$G_{SM}$ inside  $SU(5)$  }






Here, we detail the embedding of the standard model's gauge group into $SU(5)$, as given in \cite{agut}.

Elements of $SU(5)$ can be written down as $5\times5$ complex matrices, wherein we may embed the standard model's gauge group, \cite{agut}, \cite{Lang}.  Starting with $SU(2)$ and $SU(3)$, we have

\begin{equation}
\left( \begin{matrix}h_2&0\\0&h_3 \end{matrix}  \right) \hspace{4mm} \in \hspace{4mm} SU(5),
\end{equation}

\noindent where $h_2$ is a $2\times2$ matrix representing elements of $SU(2)$, and $h_3$ is a $3\times3$ matrix, representing elements of $SU(3)$.   Written in this way, the $SU(2)$ and $SU(3)$ subgroups clearly commute with each other.  We might then ask, what groups remain in $SU(5)$, which commute with both of these $SU(2)$ and $SU(3)$ subgroups?  

It is straightforward to see, \cite{agut}, \cite{Robinson}, that any $5\times 5$ matrix commuting with 

$$ \left( \begin{matrix}h_2&0\\0&h_3 \end{matrix}  \right)
$$

\noindent must be of the form 

\begin{equation}\begin{array}{ccc}\label{u1}
H_1 & = &   \left( \begin{matrix}c_2\hspace{1mm} \mathbb{I}_{2\times2}&0\\0&c_3\hspace{1mm} \mathbb{I}_{3\times 3} \end{matrix}  \right),
\end{array}\end{equation}

\noindent for $c_2, c_3\in\C$.  Furthermore, for $H_1$ to be an element of $SU(5)$, it must have a determinant of one, so that

\begin{equation}\begin{array}{ccc}\label{u1}
H_1 & = &   \left( \begin{matrix}(h_1)^{3}\hspace{1mm} \mathbb{I}_{2\times2}&0\\0&(h_1)^{-2}\hspace{1mm} \mathbb{I}_{3\times 3} \end{matrix}  \right),
\end{array}\end{equation}

\noindent where $h_1\in\mathbb{C}$.  




Putting these all together, we see that it is possible to map any element of $SU(3)\times SU(2) \times U(1)$ into $SU(5)$,

\begin{equation}
   \left( \begin{matrix}(h_1)^3\hspace{1mm} h_2&0\\0&(h_1)^{-2}\hspace{1mm}h_3 \end{matrix}  \right) \hspace{4mm}\in \hspace{4mm} SU(5),
\end{equation}

\noindent where $h_1\in U(1)$, $h_2\in SU(2)$, and $h_3\in SU(3)$.

Now, it turns out that after considering the action of the $SU(2)$ and $SU(3)$ subgroups on the $\underline{5}^*$ and the $\underline{10}$, we see that this $U(1)$ of equation~(\ref{u1}) is none other than $U(1)_Y$, weak hypercharge.  That is, $SU(5)$ theory is able to elegantly explain the strikingly inelegant arrangement of hypercharges asserted by the standard model.

\medskip

A question now arises, as to whether or not every element of $SU(3)\times SU(2) \times U(1)$ is mapped to a \it unique \rm element of $SU(5)$'s subgroup.  That is, we might ask, is this mapping invertible?  It turns out that the answer is no, \cite{agut}, as it is possible to find distinct elements of $SU(3)\times SU(2) \times U(1)$, given by



\begin{equation}\left(h_3 = z_n^{2}\hspace{1mm}\mathbb{I}_{3\times3}, \hspace{2mm} h_2 = z_n^{-3}\hspace{1mm}\mathbb{I}_{2\times2}, \hspace{2mm}h_1 = z_n   \right)  \hspace{4mm}\in\hspace{4mm}SU(3)\times SU(2) \times U(1),
\end{equation}













\noindent which each map to the same identity element of our $SU(5)$ subgroup,  


\begin{equation}
\left( \begin{matrix}     
z_n^3\hspace{1mm}  z_n^{-3}\hspace{1mm}\mathbb{I}_{2\times 2}     &0\\0&z_n^{-2}\hspace{1mm} z_n^{2}\hspace{1mm}\mathbb{I}_{3\times 3}
\end{matrix}  
\right)  \hspace{2mm} 
= \hspace{2mm}  {\mathbb{I}}_{5\times 5} \hspace{4mm} \in \hspace{4mm} SU(5).
\end{equation}


The above elements, $z_n$, are restricted to be sixth roots  of unity, $z_n=e^{2\pi i n/6}$,   since $z_n^{-3}\hspace{1mm}\mathbb{I}_{2\times2}\in SU(2)$ and $z_n^{2}\hspace{1mm}\mathbb{I}_{3\times3}\in SU(3)$ must each have a determinant of one.  This generates the finite group $\mathbb{Z}_6$.

So it turns out that our subgroup of $SU(5)$ is not $SU(3)\times SU(2) \times U(1)$, but rather,  $SU(3)\times SU(2) \times U(1)/\mathbb{Z}_6$.  This could be problematic for $SU(5)$ theory, if the standard model representations were indeed able to distinguish between these six values of $z_n$.  

However, by checking explicitly one can show that the standard model representations are insensitive to these distinct values of $z_n$.  Furthermore, $\mathbb{Z}_6$ is said, \cite{agut}, to constitute the entire kernel of this representation.   This leaves us with the conclusion that the standard model's gauge group is not $SU(3)\times SU(2) \times U(1)$, but rather,  $SU(3)\times SU(2) \times U(1)/\mathbb{Z}_6$.
