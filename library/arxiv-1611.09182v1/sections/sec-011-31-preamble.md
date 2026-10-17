---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-011-31-preamble
section_title: "Preamble"
section_number: 3.1
pages: 16-17
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.774
latex_coverage_ratio: 0.99
doc_brief: "Standard model physics from an algebra? — 69 sections: Front matter; Abstract; Acknowledgements"
---
A significant challenge within  causal set programs has been to explain the existence of 3+1 dimensions.
That is, any causal set chosen at random is highly unlikely to have this particular dimension of our choosing.  

It is for this reason that we propose here causal sets originating from an algebra, $A$.  The idea then is that a careful choice of algebra will impart on the causal set the desired 3+1 Lorentzian structure.  In this section, we will consider $A = \CH,$ the complex quaternions.  Between the left and right action of $\CH$ on itself, we will now introduce an unusually compact way of describing all of the (3+1) Lorentz representations of the standard model of particle physics.


\section{Introduction to $\CH$\label{introCH}  }


Any element of the complex quaternions can be described as the complex linear combination, 
\begin{equation}
c_0 + c_1 \hspace{1mm}i\epsilon_x + c_2 \hspace{1mm}i\epsilon_y+ c_3\hspace{1mm} i{\epsilon_z},
\end{equation}

\noindent where the $c_n \in \mathbb{C}$.  The element $i$ is the usual complex imaginary unit, with $i^2 = -1$, that commutes with all of the elements in the algebra.  The quaternionic imaginary units, ${\epsilon_x}$, ${\epsilon_y}$, and ${\epsilon_z}$ follow the multiplication rules 

\begin{equation}\label{CHmult}

{\epsilon_x}^2={\epsilon_y}^2={\epsilon_z}^2={\epsilon_x}\hspace{1mm}{\epsilon_y}\hspace{1mm}{\epsilon_z}=-1,

\end{equation}

\noindent which lead to the identities ${\epsilon_x} {\epsilon_y} = -{\epsilon_y}{\epsilon_x} =  {\epsilon_z}, \hspace{0.1cm}  {\epsilon_y} {\epsilon_z} = -{\epsilon_z}{\epsilon_y} =  {\epsilon_x}, \hspace{0.1cm}  {\epsilon_z}{\epsilon_x} = - {\epsilon_x}{\epsilon_z} = {\epsilon_y}.$  The complex quaternions form an associative algebra, meaning that $\left(ab\right)c=a\left(bc\right)$ $\forall$ $a$, $b,$ $c$ $\in\CH$.  (Note that all tensor products will be assumed to be over $\mathbb{R}$ in this text, unless otherwise stated.)

From their behaviour under multiplication, one may associate $i{\epsilon_x}$ with the more familiar Pauli matrix $\sigma_x = \left( \begin{smallmatrix}0&1\\1&0 \end{smallmatrix}  \right)$, $i{\epsilon_y}$ with $\sigma_y = \left( \begin{smallmatrix}0&-i\\i&0 \end{smallmatrix}  \right)$, and $i{\epsilon_z}$ with $\sigma_z = \left( \begin{smallmatrix}1&0\\0&-1 \end{smallmatrix}  \right)$.  Note, however, that the set $\{ i{\epsilon_x}, i{\epsilon_y}, i{\epsilon_z}\}$ transforms more symmetrically under complex conjugation than does $\{\sigma_x, \sigma_y, \sigma_z\}$,

\begin{equation}\begin{array}{lll} \sigma_x^* = \sigma_x, \hspace{13mm}&   \sigma_y^* = -\sigma_y,  \hspace{13mm}&\sigma_z^* = \sigma_z,  \vspace{5mm}  \\
 & \textup{versus} & \vspace{5mm}  \\
  \left(i{\epsilon_x}\right)^* = -i{\epsilon_x}, &   \left(i{\epsilon_y}\right)^* = -i{\epsilon_y},  & \left(i{\epsilon_z}\right)^* = -i{\epsilon_z}. \vspace{2mm}
 
\end{array}\end{equation}


Elements of the form $s\equiv r_1 {\epsilon_x} + r_2 i{\epsilon_x} + r_3 {\epsilon_y} + r_4  i{\epsilon_y} + r_5 {\epsilon_z} + r_6 i{\epsilon_z} $  for $r_n\in \mathbb{R}$ can easily be seen to give a representation of the Lie algebra $sl(2,\mathbb{C})$, using the usual commutator, $\left[ s, s' \right] \equiv ss' - s's$.  

Later in Section~\ref{mc}, we will find that $L\equiv e^{is}\in \CH$ represents an element of $SL(2,\mathbb{C})$, which acts on left-handed Weyl spinors.  These Weyl spinors also reside in $\CH$, and in fact, all of the results obtained throughout this thesis will follow simply from having an algebra $A$ act on itself.
