---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-017-352-weyl-and-dirac-spinors-as-generalized-ideals
section_title: "Weyl and Dirac spinors as generalized ideals"
section_number: 3.5.2
pages: 20-21
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
Let us now identify two subspaces, which partition the algebra $\CH$.  These subspaces will be given the suggestive nomenclature $\Psi_{\textup{L}}$ and $\Psi_{\textup{R}}$, and be defined as
\begin{equation}\begin{array}{lll}
\Psi_{\textup{L}} \equiv \psi^{\uparrow}_{\textup{L}} \hspace{1mm} \epsilon_{\uparrow \uparrow} +  \psi^{\downarrow}_{\textup{L}} \hspace{1mm} \epsilon_{\downarrow \uparrow}  & \hspace{1cm} &  \Psi_{\textup{R}} \equiv \psi^{\uparrow}_{\textup{R}} \hspace{1mm} \epsilon_{\uparrow \downarrow} +  \psi^{\downarrow}_{\textup{R}} \hspace{1mm} \epsilon_{\downarrow \downarrow},
\end{array}\end{equation}
\noindent where $\psi^{\uparrow}_{\textup{L}}$, $\psi^{\downarrow}_{\textup{L}}$, $\psi^{\uparrow}_{\textup{R}}$, $\psi^{\downarrow}_{\textup{R}}$ $\in \mathbb{C}$.  Readers may notice that spin and chirality are analogues of each other in this formalism, as transitions between spin states occur via left multiplication, and transitions between $\textup{L}$ and $\textup{R}$ occur via right multiplication.

Straightforward calculation shows that  
\begin{equation} \begin{array}{lll}
\Psi_{\textup{L}}\hspace{1mm} P = \Psi_{\textup{L}} & \hspace{1cm} & \Psi_{\textup{L}}\hspace{1mm} P^* = 0,\vspace{3mm}\\
\Psi_{\textup{R}}\hspace{1mm} P = 0 & \hspace{1cm} &   \Psi_{\textup{R}}\hspace{1mm} P^* = \Psi_{\textup{R}}.
\end{array}\end{equation}




Now, the reader may confirm that $\Psi_{\textup{L}}$ and $\Psi_{\textup{R}}$ are left ideals, as defined in Chapter~\ref{m1}.  That is, no matter which $a_1$ and $a_2$  are left multiplied onto them, there exists some ${\Psi_{\textup{L}}}'  \equiv {\psi^{\uparrow}_{\textup{L}}}' \hspace{1mm} \epsilon_{\uparrow \uparrow} +  {\psi^{\downarrow}_{\textup{L}}}'\hspace{1mm} \epsilon_{\downarrow \uparrow} $ and ${\Psi_{\textup{R}}}'  \equiv {\psi^{\uparrow}_{\textup{R}}}' \hspace{1mm} \epsilon_{\uparrow \downarrow} +  {\psi^{\downarrow}_{\textup{R}}}' \hspace{1mm} \epsilon_{\downarrow \downarrow}$ such that
\begin{equation}\begin{array}{lll}
a_1\Psi_{\textup{L}} = {\Psi_{\textup{L}}}'  &  \hspace{1cm}  &   a_2\Psi_{\textup{R}} = {\Psi_{\textup{R}}}' .
\end{array}\end{equation}
\noindent In other words, the L and R subspaces are each stable under left multiplication.  

With this knowledge in hand, it is now almost trivial to see that $\Psi_{\textup{L}}$ and $\Psi_{\textup{R}}$ are each generalized ideals under the complex invariant-action, $m_c$.  That is, for any $a\in\CH$, there exists a $\Psi_{\textup{L}}'$ such that
\begin{equation}
\Psi_{\textup{L}}' =  a\Psi_{\textup{L}} =  a\Psi_{\textup{L}}P  = a\Psi_{\textup{L}}P + a^*\Psi_{\textup{L}}P^* = m_c(a,\Psi_{\textup{L}} ).
\end{equation}
\noindent Likewise, for any $a^*\in\CH$, there exists a $\Psi_{\textup{R}}'$ such that
\begin{equation}
\Psi_{\textup{R}}' =  a^*\Psi_{\textup{R}} =  a^*\Psi_{\textup{R}}P^*  = a\Psi_{\textup{R}}P + a^*\Psi_{\textup{R}}P^* = m_c(a,\Psi_{\textup{R}} ).
\end{equation}

\noindent It is furthermore easily seen that the set of elements of the form $\Psi_{\textup{D}} \equiv \Psi_{\textup{L}} + \Psi_{\textup{R}}$ spans all of $\CH$, and hence trivially qualifies as a generalized ideal under $m_c$.  



Taking now $a$ to be $L = e^{is}$ from Section~\ref{introCH} gives the transformation
\begin{equation}
{\Psi_{\textup{D}}}' = m_c(L,\Psi_{\textup{D}} ) = L\Psi_{\textup{L}} + L^* \Psi_{\textup{R}}.
\end{equation}
\noindent The reader is encouraged to confirm that indeed $\Psi_{\textup{D}}$ transforms as a Dirac spinor, $\Psi_{\textup{L}}$ transforms as a left-handed Weyl spinor, and $\Psi_{\textup{R}}$ transforms as a right-handed Weyl spinor under $SL(2,\mathbb{C})$.  In other words, the complex coefficients within $\Psi_{\textup{D}}$ transform exactly as would the complex components of a four-dimensional column vector, representing a Dirac spinor, from standard quantum field theory.    It is for this reason that the names $\Psi_{\textup{D}}$, $\Psi_{\textup{L}}$, and $\Psi_{\textup{R}}$ were given to these generalized ideals early on.
