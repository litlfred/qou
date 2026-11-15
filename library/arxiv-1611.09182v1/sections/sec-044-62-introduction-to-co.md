---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-044-62-introduction-to-co
section_title: "Introduction to CO"
section_number: 6.2
pages: 48-50
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.975
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
The complex octonions are not a tool commonly used in physics, so we introduce them here.

The generic element of $\mathbb{C} \otimes \mathbb{O}$ is written $ \sum_{n=0}^7 A_n e_n $, where the $A_n$ are complex coefficients.  The $e_n$ are octonionic imaginary units $\left(e_n^2=-1\right)$, apart from $e_0=1$, which multiply according to Figure~\ref{fano}.  The complex imaginary unit $i$ commutes with the octonionic $e_n$.

\begin{figure}[h!] \begin{center}
\includegraphics[width=7cm]{doubling_fano-eps-converted-to.pdf}
\caption{\label{fano}
Multiplication of octonionic imaginary units}
\end{center}\end{figure}

Any three imaginary units on a directed line segment in Figure~\ref{fano} act as if they were a triplet of Pauli matrices, $\sigma_m$.  (More precisely, they behave as $-i\sigma_m$.)  For example, $e_6e_1 =-e_1e_6= e_5,$ $e_1e_5=-e_5e_1=e_6,$ $e_5e_6=-e_6e_5=e_1,$ $e_4e_1=-e_1e_4=e_2$, etc.  

The multiplication rules for these imaginary units can be defined by setting $e_1e_2 = e_4$, and then applying the following rules,  as shown in \cite{baez}.  

\begin{equation}\begin{array}{l} 
e_ie_j = -e_je_i \hspace{1cm} i\neq j, \vspace{2mm}\\
e_ie_j = e_k \hspace{2mm} \Rightarrow  \hspace{2mm}e_{i+1}e_{j+1} = e_{k+1},\vspace{2mm}\\
e_ie_j = e_k \hspace{2mm}\Rightarrow \hspace{2mm} e_{2i}e_{2j} = e_{2k}. 
\end{array}\end{equation}


It is indeed true that the octonions form a non-associative algebra, meaning that the relation $(ab)c =a(bc)$ does not always hold.   The reader can check this by finding three imaginary units, which are not all on the same line segment, and substituting them as in $a$, $b$, and $c$.  

The octonionic automorphism group is $G_2$, which is a 14-dimensional exceptional Lie group.  Its Lie algebra may be represented by the generators 

\begin{equation}\begin{array}{lll}\label{g2}

\Lambda_1 = \frac{i}{2}\big(e_1\left(e_5\hspace{2mm} \cdot\hspace{1mm}\right)-e_3\left(e_4 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  &\hspace{1mm}&    \Lambda_8 = \frac{i}{2\sqrt{3}}\big(e_1\left(e_3\hspace{2mm} \cdot\hspace{1mm}\right)+e_4\left(e_5 \hspace{2mm}\cdot\hspace{1mm}\right)   -    2e_2\left(e_6 \hspace{2mm}\cdot\hspace{1mm}\right) \big) , \vspace{3mm} \\



\Lambda_2 = -\frac{i}{2}\big(e_1\left(e_4\hspace{2mm} \cdot\hspace{1mm}\right)+e_3\left(e_5 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  &\hspace{1mm}& g_9 =   -\frac{i}{2\sqrt{3}}\big(e_1\left(e_5\hspace{2mm} \cdot\hspace{1mm}\right)+e_3\left(e_4 \hspace{2mm}\cdot\hspace{1mm}\right)   +    2e_2\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big),\vspace{3mm} \\





\Lambda_3 = \frac{i}{2}\big(e_4\left(e_5\hspace{2mm} \cdot\hspace{1mm}\right)-e_1\left(e_3 \hspace{2mm}\cdot\hspace{1mm}\right) \big) , &\hspace{1mm}& g_{10} = \frac{i}{2\sqrt{3}}\big(e_1\left(e_4\hspace{2mm} \cdot\hspace{1mm}\right)-e_3\left(e_5 \hspace{2mm}\cdot\hspace{1mm}\right)   +    2e_6\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big), \vspace{3mm} \\






 \Lambda_4 = \frac{i}{2}\big(e_2\left(e_5\hspace{2mm} \cdot\hspace{1mm}\right)+e_4\left(e_6 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  
 &\hspace{1mm}&  g_{11} =   -\frac{i}{2\sqrt{3}}\big(e_4\left(e_6\hspace{2mm} \cdot\hspace{1mm}\right)-e_2\left(e_5 \hspace{2mm}\cdot\hspace{1mm}\right)   +    2e_1\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big),\vspace{3mm} \\


  
\Lambda_5 = \frac{i}{2}\big(e_5\left(e_6\hspace{2mm} \cdot\hspace{1mm}\right)-e_2\left(e_4 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  &\hspace{1mm}&  g_{12} = -\frac{i}{2\sqrt{3}}\big(e_2\left(e_4\hspace{2mm} \cdot\hspace{1mm}\right)+e_5\left(e_6 \hspace{2mm}\cdot\hspace{1mm}\right)   -    2e_3\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big), \vspace{3mm} \\


\Lambda_6 = \frac{i}{2}\big(e_1\left(e_6\hspace{2mm} \cdot\hspace{1mm}\right)+e_2\left(e_3 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  &\hspace{1mm}& g_{13} =   -\frac{i}{2\sqrt{3}}\big(-e_1\left(e_6\hspace{2mm} \cdot\hspace{1mm}\right)+e_2\left(e_3 \hspace{2mm}\cdot\hspace{1mm}\right)   +   2e_4\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big),\vspace{3mm} \\



\Lambda_7 = \frac{i}{2}\big(e_1\left(e_2\hspace{2mm} \cdot\hspace{1mm}\right)+e_3\left(e_6 \hspace{2mm}\cdot\hspace{1mm}\right) \big),  
&\hspace{1mm}&  g_{14} = \frac{i}{2\sqrt{3}}\big(-e_1\left(e_2\hspace{2mm} \cdot\hspace{1mm}\right)+e_3\left(e_6 \hspace{2mm}\cdot\hspace{1mm}\right)   +   2e_5\left(e_7 \hspace{2mm}\cdot\hspace{1mm}\right) \big) ,

\end{array}\end{equation}

\noindent acting on the octonions.  Here, the nested brackets indicate that the generators are constructed from chains of octonions, multiplying from right to left.  

The eight objects, $\Lambda_i$, generate $SU(3)\subset G_2$.    This $SU(3)$ may be defined as the subgroup of $G_2$ which leaves the octonionic unit $e_7$ invariant.  Of course,  alternate $SU(3)$ subgroups of $G_2$ may be found, which correspond to other imaginary units. For a more thorough introduction of $\mathbb{O}$ see~\cite{baez}, \cite{conway}, \cite{okubo}.

Finally, we define three notions of conjugation on an element $a$ in $\mathbb{C}\otimes\mathbb{O}$.  The \it complex conjugate \rm of $a$, denoted $a^*$, maps the complex $i\mapsto -i$, as would be expected.  The \it octonionic conjugate \rm of $a$, denoted $\tilde{a}$, takes each of the octonionic imaginary units $e_n\mapsto -e_n$ for $n=1,\dots 7$.  That which we will call the \it hermitian conjugate \rm of $a$, denoted $a^{\dagger}$, performs both of these maps simultaneously, $i \mapsto -i$ and $e_n \mapsto -e_n$ for $n=1,\dots 7$.  The conjugate and the hermitian conjugate each reverse the order of multiplication, as is familiar from the hermitian conjugate of a product of matrices.
