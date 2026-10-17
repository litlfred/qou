---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-007-321-further-graphical-conventions
section_title: "Further graphical conventions"
section_number: 3.2.1
pages: 10-10
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.922
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Fix a root choice $\{d_i\}$, $i \in I$. We introduce the following notation. For an endomorphism of a simple object $f : X_i \rightarrow X_i$, we will write $\langle f \rangle \in \mathbb{C}$ for the scalar satisfying $f = \langle f \rangle \, \id_{X_i}$. In string diagrams, 
\begin{equation} \label{extract_scalar}
 \ba \ig{h1.pdf} \ea \, = \, \langle f \rangle \, \ba \ig{h2.pdf} \ea  \, .
\end{equation}
We can extract the scalar $\langle f \rangle$ by pre- and post-composing both sides with the cup and cap maps, using the pairing convention with respect to the root choice. This gives
\begin{equation} \label{loop_scalar}
 \langle f \rangle = \frac{1}{d_i} \, \ba \ig{h3.pdf} \ea \, .
\end{equation}
Note that since $d_{i} = d_{i^*}$, it doesn't matter in which direction one closes the loop. 

Similarly, given a morphism $f : X_i \rightarrow X_j \otimes X_k$, we can insert the identity on $X_j \otimes X_k$ in the form of \eqref{res_id}, and close the loop as above, to expand $f$ in a basis $e_\beta : X_i \rightarrow X_k \otimes X_k$ as follows:
\begin{equation} \label{expand_loop}
\ba \ig{h5.pdf} \ea \, = \frac{1}{d_i} \sum_\beta \ba \ig{h6.pdf} \ea \, \ba \ig{h7.pdf} \ea
\end{equation}
