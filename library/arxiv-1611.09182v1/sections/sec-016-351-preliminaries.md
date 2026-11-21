---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-016-351-preliminaries
section_title: "Preliminaries"
section_number: 3.5.1
pages: 19-20
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.981
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
We will now find that left- and right-handed Weyl spinors, Majorana spinors, and Dirac spinors are all generalized ideals under the same complex invariant-action, 
\begin{equation}\label{cma}
\underline{b}' =  a\hspace{1mm}\underline{b}\hspace{1mm} P + a^*\hspace{1mm}\underline{b}\hspace{1mm} P^*.  
\end{equation}
\noindent For concreteness, we define $P$ to be the projector $\frac{1}{2}\left(1+i{\epsilon_z}\right)$, although it is  clear that a continuum of other possibilities exist.  $P$ and its complex conjugate, $P^*$, exhibit the properties 
\begin{equation}\begin{array}{lllllll}
PP=P,  & \hspace{1cm} & P^*P^* = P^*, & \hspace{1cm} & PP^* = P^*P = 0,  & \hspace{1cm} & P + P^* = 1.
\end{array}\end{equation}


Before we begin, though, it will be useful to carry out a change of basis from $\{1, \hspace{1mm}i{\epsilon_x}, \hspace{1mm}i{\epsilon_y}, \hspace{1mm}i{\epsilon_z}\}$ to a new, suggestively named basis, $\{\epsilon_{\uparrow \uparrow},  \hspace{1mm} \epsilon_{\downarrow \uparrow},\hspace{1mm} \epsilon_{\uparrow \downarrow},\hspace{1mm} \epsilon_{\downarrow \downarrow} \}$.  This new basis will be linked to the operator, $i{\epsilon_z}\sim \sigma_z$, in that these basis elements will be defined so as to have the properties:
\begin{equation}
\begin{array}{lll}
i{\epsilon_z}\hspace{1mm}\epsilon_{\uparrow \uparrow} = +\hspace{1mm} \epsilon_{\uparrow \uparrow} & \hspace{1cm} &\epsilon_{\uparrow \uparrow}\hspace{1mm}i{\epsilon_z} = +\hspace{1mm} \epsilon_{\uparrow \uparrow}\vspace{3mm} \\

i{\epsilon_z}\hspace{1mm}\epsilon_{\downarrow \uparrow} = -\hspace{1mm}\epsilon_{\downarrow \uparrow} & \hspace{1cm} &\epsilon_{\downarrow \uparrow}\hspace{1mm}i{\epsilon_z} = +\hspace{1mm}\epsilon_{\downarrow \uparrow}\vspace{3mm} \\

i{\epsilon_z}\hspace{1mm}\epsilon_{\uparrow \downarrow} = +\hspace{1mm}\epsilon_{\uparrow \downarrow} & \hspace{1cm} &\epsilon_{\uparrow \downarrow}\hspace{1mm}i{\epsilon_z} = -\hspace{1mm}\epsilon_{\uparrow \downarrow}\vspace{3mm} \\

i{\epsilon_z}\hspace{1mm}\epsilon_{\downarrow \downarrow} = -\hspace{1mm}\epsilon_{\downarrow \downarrow} & \hspace{1cm} &\epsilon_{\downarrow \downarrow}\hspace{1mm}i{\epsilon_z} = -\hspace{1mm}\epsilon_{\downarrow \downarrow}.\vspace{3mm} \\
\end{array}
\end{equation}


\noindent In terms of the old basis, we define these new basis vectors to be
\begin{equation}
\begin{array}{lll} 
\epsilon_{\uparrow \uparrow} \equiv \frac{1}{2}\left(1+i{\epsilon_z}\right) & \hspace{1cm} & \epsilon_{\downarrow \uparrow} \equiv \frac{1}{2}\left({\epsilon_y}+i{\epsilon_x}\right) \vspace{3mm} \\

\epsilon_{\uparrow \downarrow} \equiv \frac{1}{2}\left(-{\epsilon_y}+i{\epsilon_x}\right)  & \hspace{1cm} & \epsilon_{\downarrow \downarrow} \equiv \frac{1}{2}\left(1-i{\epsilon_z}\right).

\end{array}
\end{equation}

\noindent For convenience, we also include here the old basis in terms of the new one,

\begin{equation}
\begin{array}{lll} 
1 = \epsilon_{\uparrow \uparrow}+\epsilon_{\downarrow \downarrow} & \hspace{1cm} & \epsilon_x = -i\left(\epsilon_{\downarrow\uparrow}+\epsilon_{\uparrow\downarrow}\right) \vspace{3mm} \\

\epsilon_y = \epsilon_{\downarrow\uparrow}-\epsilon_{\uparrow\downarrow}  & \hspace{1cm} & \epsilon_z = -i\left(\epsilon_{\uparrow \uparrow}-\epsilon_{\downarrow \downarrow}   \right).

\end{array}
\end{equation}
