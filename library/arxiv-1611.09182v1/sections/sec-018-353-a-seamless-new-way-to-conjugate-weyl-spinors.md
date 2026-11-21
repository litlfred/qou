---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-018-353-a-seamless-new-way-to-conjugate-weyl-spinors
section_title: "A seamless new way to conjugate Weyl spinors"
section_number: 3.5.3
pages: 21-22
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.992
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
In quantum field theory textbooks, it is typically explained that a left handed Weyl spinor, $\Psi_{\textup{L}}$, can be conjugated so as to give a right-handed Weyl spinor.  The procedure necessary to do so, in the usual matrix-and-column-vector formalism, entails (1) complex conjugating the left-handed spinor's two components, and (2) multiplying this column vector by the matrix $\epsilon = -i\sigma_y=\left( \begin{smallmatrix}0&-1\\1&0 \end{smallmatrix}  \right)$, 

\begin{equation}\label{old} \begin{array}{lllll}\left[\hspace{1mm}\psi^{\uparrow}_{\textup{L}} , \hspace{1mm} \psi^{\downarrow}_{\textup{L}}\hspace{1mm}\right]^{\top} &  \rightarrow (1) \rightarrow  & \left[\hspace{1mm}{\psi^{\uparrow}_{\textup{L}}}^* , \hspace{1mm} {\psi^{\downarrow}_{\textup{L}}}^*\hspace{1mm}\right]^{\top} & \rightarrow (2) \rightarrow & \left[\hspace{1mm}-{\psi^{\downarrow}_{\textup{L}}}^* , \hspace{1mm} {\psi^{\uparrow}_{\textup{L}}}^*\hspace{1mm}\right]^{\top}.
\end{array}\end{equation}

Notice what happens, though, if we write these Weyl spinors instead in terms of the $\CH$ algebra:

\begin{equation}\label{new}\Psi_{\textup{L}}^* = {\psi^{\uparrow}_{\textup{L}}}^* \hspace{1mm} {\epsilon_{\uparrow \uparrow}}^* +  {\psi^{\downarrow}_{\textup{L}}}^* \hspace{1mm} {\epsilon_{\downarrow \uparrow}}^* = -{\psi^{\downarrow}_{\textup{L}}}^* \hspace{1mm} {\epsilon_{\uparrow \downarrow}} + {\psi^{\uparrow}_{\textup{L}}}^* \hspace{1mm}{\epsilon_{\downarrow \downarrow}}.
\end{equation}

\noindent That is, we arrive at the exact same result using nothing more than the complex conjugate:  $i\mapsto-i$.

\vspace{1cm}

Now, in order to return back to the original left-handed Weyl spinor, in the usual matrix-and-column-vector formalism, we must again $(1)$ complex conjugate the spinor's components, but this time, $(2)'$ multiply by the new matrix $-\epsilon$,

\begin{equation} \begin{array}{lllll}
 \left[\hspace{1mm}-{\psi^{\downarrow}_{\textup{L}}}^* , \hspace{1mm} {\psi^{\uparrow}_{\textup{L}}}^*\hspace{1mm}\right]^{\top} & \rightarrow (1) \rightarrow & \left[\hspace{1mm}-{\psi^{\downarrow}_{\textup{L}}} , \hspace{1mm} {\psi^{\uparrow}_{\textup{L}}}\hspace{1mm}\right]^{\top} & \rightarrow (2)' \rightarrow& 
\left[\hspace{1mm}\psi^{\uparrow}_{\textup{L}} , \hspace{1mm} \psi^{\downarrow}_{\textup{L}}\hspace{1mm}\right]^{\top}. 
\end{array}\end{equation}

\noindent In comparison, the same result is achieved in $\CH$ more simply by taking the complex conjugate twice,
\begin{equation}\label{psicc}{\Psi_{\textup{L}}}^{**} = \Psi_{\textup{L}}.
\end{equation}

Readers should note that $*: \Psi_{\textup{L}}\mapsto \Psi_{\textup{R}}$ is a basis-independent statement in our formalism.  It holds, regardless of whether $\Psi_\textup{L}$ is written in the Weyl, Dirac, or Majorana basis of the Dirac algebra.   To the best of this author's knowledge, \cite{UTI} was the first instance where this more streamlined method of conjugating spinors has been proposed.   






\vspace{.3cm}


In considering these two formalisms, one comes to notice that no $\epsilon$-type object was needed in the $\CH$ case.  Somehow, the complex conjugate $i\mapsto -i$ automatically encoded the information given by $\epsilon$.  It is natural to ask, then, why $\epsilon$ is necessary in the matrix-and-column-vector formalism.

After comparing equations (\ref{old}) and (\ref{new}), one sees that $\epsilon$ was what was needed so as to account for the complex conjugation of basis vectors.  In the $\CH$ formalism, we naturally take the complex conjugate of \it both \rm the coefficients, and the basis vectors.  On the other hand, there is no notion of complex conjugating basis vectors in the matrix-and-column-vector formalism.  The matrix $\epsilon$ needs to be introduced so as to account for this.  The conjugation of Weyl spinors, as explained here, then exposes a naturalness to the purely algebraic formalism.
