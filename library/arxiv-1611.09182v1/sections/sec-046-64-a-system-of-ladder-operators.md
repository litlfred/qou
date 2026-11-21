---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-046-64-a-system-of-ladder-operators
section_title: "A system of ladder operators"
section_number: 6.4
pages: 53-54
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
With the algebra $\COOO$ in hand, we can now set out to find a system of ladder operators within the octonionic chain algebra.  Consider $\alpha_1 \equiv \frac{1}{2}\left(-e_5+ie_4\right)$,  $\alpha_2 \equiv \frac{1}{2}\left(-e_3+ie_1\right),$ and $\alpha_3 \equiv \frac{1}{2}\left(-e_6+ie_2\right)$, similar to that defined in~\cite{GGquarks}.  For all $f$ in $\mathbb{C}\otimes\mathbb{O}$, and assuming right-to-left multiplication, these three lowering operators obey the anticommutation relations

\begin{equation}\label{alpha}
\{\alpha_i, \alpha_j\}f =\alpha_i(\alpha_jf)+\alpha_j (\alpha_if) = 0 
\end{equation}

\noindent for all $i,j = 1,2,3.$  The above can be seen as a generalization of the system in~\cite{GGstats}.  That is, \cite{GGstats} is recovered by restricting the general $f$ in $\mathbb{C}\otimes\mathbb{O}$ to $f=1$.  

In another slight deviation from \cite{GGstats}, we define raising operators as $\alpha_1^{\dagger} = \frac{1}{2}\left(e_5+ie_4\right)$,  $\alpha_2^{\dagger} = \frac{1}{2}\left(e_3+ie_1\right),$ and $\alpha_3^{\dagger} = \frac{1}{2}\left(e_6+ie_2\right)$, which obey

\begin{equation}\label{alphad}
\{\alpha_i^{\dagger}, \alpha_j^{\dagger}\}f = 0 \hspace{0.7cm}\textup{for all} \hspace{0.2cm} i,j = 1,2,3.
\end{equation}

\noindent We finally also have 

\begin{equation}\label{alphaalphad}
\{\alpha_i,\alpha_j^{\dagger}\}f=\delta_{ij}f \hspace{0.7cm} \textup{for all} \hspace{0.2cm}i,j = 1,2,3.
\end{equation}

With the purpose simplifying notation, we will now implicitly assume all multiplication to be carried out starting at the right, and moving to the left, as was shown in equation~(\ref{alpha}).  That is, we will now not write these brackets in explicitly, nor will we include an arrow going from right to left, specifying the direction of multiplication.   

Furthermore,  we will now be concerned only with operators, such as the $\alpha_i$, as opposed to the object $f$.  This being the case, it will now be understood that all equations will hold over all $f$ in $\CO$, even though $f$ will not be mentioned explicitly.    For example, we will now write equation~(\ref{alpha}) simply as

\begin{equation}
\{\alpha_i, \alpha_j\} =\alpha_i\alpha_j+\alpha_j \alpha_i = 0 \hspace{1cm}\textup{for all}\hspace{0.2cm} i,j = 1,2,3.
\end{equation}

As mentioned earlier, these operators acting on $f$ may be viewed as $8\times8$ complex matrices acting on $f,$ an eight-complex-dimensional column vector.  Taking into account the above paragraph, our equations from here on in can be considered as relations only between the matrices.

Another way of restating the above is to say that the operators are simply elements of $\COOO$, and we will be considering only the elements of $\COOO$ from here on in.
