---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-028-43-examples-of-clifford-algebras-from-ch
section_title: "Examples of Clifford algebras from CH"
section_number: 4.3
pages: 29-30
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
Given the multiplication properties from equation~(\ref{CHmult}), it is straightforward to see that $\CH$ gives a representation of the real Clifford algebra, $Cl(3,0)$.  Please see Figure~(\ref{cl3}).

\begin{figure}[h!]
\begin{center}
\includegraphics[width=7cm]{cl3_eps-eps-converted-to.pdf}
\caption{\label{cl3}
The algebra $\CH$ written so as to show its $Cl(3,0)$ structure.  Here, the Clifford algebra's zero-vector is 1, its generating vectors are $i{\epsilon_x}$, $i{\epsilon_y}$, $i{\epsilon_z}$, its bivectors are ${i\epsilon_y}{i\epsilon_z} = -{\epsilon_x}$, \hspace{1mm} ${i\epsilon_z}{i\epsilon_x} = -{\epsilon_y}$, \hspace{1mm}${i\epsilon_x}{i\epsilon_y} = -{\epsilon_z}$, and its 3-vector is ${i\epsilon_x}{i\epsilon_y}{i\epsilon_z} = i$.  These multi-vectors are understood to be taken over $\R$.}
\end{center}\end{figure}

\noindent Alternately, $\CH$ also gives a representation of $\CLtwo$, as shown in Figure~(\ref{cl2}).
\begin{figure}[h!]\label{cl2}\begin{center}
\includegraphics[width=5cm]{cl2_eps-eps-converted-to.pdf}
\caption{\label{cl2}
The algebra $\CH$ written so as to show its $\CLtwo$ structure.  Here, the Clifford algebra's zero-vector is 1, its generating vectors are $i{\epsilon_x}$ and $i{\epsilon_y}$, its bivector is ${i\epsilon_x}{i\epsilon_y} = -{\epsilon_z}$.  These multi-vectors are understood to be taken over $\C$.}
\end{center}\end{figure}




\newpage

It was mentioned above that complex Clifford algebras, $\mathbb{C}l(n)$, each have just a single irreducible representation when $n$ is even, and have two inequivalent irreducible representations when $n$ is odd.  In the even case, that irreducible representation is $2^{n/2}$-complex-dimensional, whereas, in the odd case, each of the two irreducible representations are $2^{(n-1)/2}$-complex-dimensional.  These irreducible representations are commonly known as  spinors. 


Consider the example of the complex quaternions acting on themselves from the left.  This action gives a representation of $\CLtwo$, so that $n=2$ in this case.  We would then expect a single $2^{n/2}$-complex-dimensional irreducible representation for that Clifford algebra.  This irreducible representation is none other than the familiar 2-complex-dimensional Weyl spinor.
