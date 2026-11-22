---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-020-36-hermitian-invariant-action-mh
section_title: "Hermitian invariant-action, mh"
section_number: 3.6
pages: 23-24
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
We will now find that the hermitian invariant-action, $m_h$, leads to new generalized ideals, which behave like four-vectors, 

\begin{equation}
\underline{b} ' = a\hspace{1mm} \underline{b}\hspace{1mm} a ^{\dagger}.
\end{equation}

Any element of $\mathbb{C}\otimes\mathbb{H}$ can be written as a sum of hermitian $p\equiv p_0 + p_1i{\epsilon_x} +p_2i{\epsilon_y} + p_3i{\epsilon_z}$ and anti-hermitian $\hat{p}\equiv i\hat{p}_0 + \hat{p}_1{\epsilon_x} +\hat{p}_2{\epsilon_y} + \hat{p}_3{\epsilon_z}$ parts, where the $p_n$ and $\hat{p}_n$ $\in \mathbb{R}$.  
 As $a p a ^{\dagger}$ is hermitian and $a \hat{p} a ^{\dagger}$ is antihermitian for any $a \in \mathbb{C}\otimes\mathbb{H}$, it is clear that these two subspaces form generalized ideals under the multiplication $m_h( a,\underline{b} ) = a \underline{b} a ^{\dagger}$.

Just as was done in the case for spinors, we may now set $a=L$, where $L$ represents elements of $SL(2, \mathbb{C})$.  The hermitian element, $p$, transforms as $p'= LpL^{\dagger}$.  Matching components, one finds that under this transformation law, $p$ transforms as a contravariant four-vector under the Lorentz group, \cite{gs}.  Taking the complex conjugate of $p$ describes the transformation a covariant four-vector,  ${p^*}'= L^*p^*\widetilde{L}$.  It can be seen that the antihermitian case for $\hat{p}$ follows analogously.

As an example, let us consider the momentum $p = p_0 + p_1i{\epsilon_x} +p_2i{\epsilon_y} + p_3i{\epsilon_z}$ under a rotation about the $z$ axis by an angle $\theta$.  This rotated momentum is given by

\begin{equation} \begin{array}{c}
p' =  \exp{\left(-\frac{\theta{\epsilon_z}}{2}\right)}\hspace{1mm}p\hspace{1mm} \exp{\left(\frac{\theta{\epsilon_z}}{2}\right)} = \left(  \cos{\frac{\theta}{2}} - {\epsilon_z}\sin{\frac{\theta}{2}}    \right) p \left(    \cos{ \frac{ \theta }{2} } + {\epsilon_z}\sin{\frac{\theta}{2}}   \right)=
\\ \\
p_0 + \left( p_1 \cos{\theta} + p_2 \sin{\theta}  \right) i{\epsilon_x} + \left(  p_2 \cos{\theta} - p_1 \sin{\theta} \right)i{\epsilon_y} + p_3i{\epsilon_z},
\end{array}\end{equation}

\noindent as expected. 

From this example, readers may note that even though the object $p = p_0 + p_1i{\epsilon_x} +p_2i{\epsilon_y} + p_3i{\epsilon_z}$ looks to have indices which are all tied off, it does not represent a Lorentz scalar.  It transforms as a four-vector.  Furthermore, even though the coefficients $p_{\mu}$ have space-time indices, they do not transform directly on their own.   This is in contrast to objects in the formalism of standard QFT, which would have real numbers, $p_{\mu}$, transforming under the Lorentz group.  Here, we have only the complete  $p = p_0 + p_1i{\epsilon_x} +p_2i{\epsilon_y} + p_3i{\epsilon_z}$ transforming under the Lorentz group.



 As shown in~\cite{gs}, scalars can be constructed  between a covariant vector $p$ and contravariant vector $q$, as $\frac{1}{2}\left( pq + \widetilde{pq} \right)$, which is simply the real part of $pq$.  Indeed, when $q=p^*$, this gives $p_0^2 -p_1^2-p_2^2-p_3^2$.

\vspace{1cm}


In brief, we have just seen that four-vectors can be represented simply by generalized ideals under the hermitian multiplicative action, $m_h$.  For the hermitian case, contravariant four vectors transform as $p'= LpL^{\dagger}$, and covariant four-vectors transform as ${p^*}'= L^*p^*\widetilde{L}$, where $L$ represents and element of $SL(2, \mathbb{C})$.
