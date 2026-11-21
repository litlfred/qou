---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-045-63-octonionic-chain-algebra
section_title: "Octonionic chain algebra"
section_number: 6.3
pages: 50-53
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.971
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
As a non-associative algebra, the octonions can at times seem temperamental.  Equations involving this algebra can quickly become unwieldy, due to the need to repeatedly specify the order of multiplication, by use of brackets.  The assumptions we are accustomed to making in associative algebras now do not always apply, and one might be led to wonder how (associative) groups can be described with the (non-associative) octonions.  

In this section, however,  we explain how this is not the conundrum that it might seem to be.  Every multiplication between two octonions can be considered as a linear map of one octonion on the other.  As maps are associative by definition, this gives a way of re-describing the action of octonions as an associative algebra.

\vspace{.5cm}

It is plain to see that left-multiplying one complex octonion, $m$, onto another, $f$, provides a map from $f\in\mathbb{C}\otimes\mathbb{O}$ to $f'\equiv mf \in\mathbb{C}\otimes\mathbb{O}$.  Subsequently left-multiplying by another complex octonion, $n$, provides another map: $f\mapsto  f'' \equiv n(mf)$.  We will call this map $\overleftarrow{nm}$, where the arrow is in place so as to indicate the order in which multiplication occurs.  We may extend the chain further by left-multiplying by $p\in\mathbb{C}\otimes\mathbb{O}$, giving  $\hspace{1mm}\overleftarrow{pnm}:f\mapsto p(n(mf))$, and so on.

In an associative algebra, $A$, the exercise of building up chains in order to make new maps would be futile.  That is, for $m_1, m_2, f$ in an associative algebra, $m_2(m_1f)$ can always be summarized as $(m_2m_1)f=m'f$, where $m'\equiv m_2m_1 \in A$.  However, as the complex octonions form a non-associative algebra, building chains does in fact lead to new maps.  For example, consider the map $\overleftarrow{e_3e_4}$ acting on $f=\left(e_6+ie_2 \right)$. 

\begin{equation}\overleftarrow{e_{3}e_{4}}\left(e_6+ie_2 \right) =  e_3 \left( e_4 \left( e_6+ie_2  \right) \right) =  -1 +ie_7.
\end{equation}

\noindent This is not the same as 

\begin{equation}
\left( e_3  e_4 \right) \left( e_6+ie_2  \right)= \left( e_6 \right) \left(e_6+ie_2  \right)=  -1 -ie_7 , 
\end{equation}

\noindent and in fact there exists no $a \in \mathbb{C}\otimes\mathbb{O}$ such that $\overleftarrow{e_{3}e_{4}}\left( e_6+ie_2 \right) = a \left( e_6+ie_2 \right)$.

Addition and multiplication are easy to define on this set of chains; we will refer to the resulting algebra as the \it complex octonionic chain algebra, \rm $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$, or simply the \it chain algebra \rm for short.  Addition of two maps $N =\overleftarrow{\cdots n_3 n_2 n_1}$ and $P=\overleftarrow{\cdots p_3 p_2 p_1}$ $\in \mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ on $f$ is given by $\left[N+P\right]f = Nf+Pf,$ where the $n_i$ and $p_j$ $\in \mathbb{C}\otimes\mathbb{O}$.  Multiplication, $\circ$, is given simply by the composition of maps,

\begin{equation}\left[P\circ N\right]f =P(N(f))= \overleftarrow{\cdots p_3 p_2 p_1\cdots n_3 n_2 n_1}f.
\end{equation}

As the composition of maps is always associative, $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ is an associative algebra. Unconvinced readers are encouraged to check explicitly that $ \left[\left[A \circ B\right] \circ C \right]f = \left[A \circ \left[B \circ C \right]\right]f$ $\forall$ $A,B,C\in \mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ and $\forall$ $f\in\mathbb{C}\otimes\mathbb{O}$.

In analogy with the $\CO$ case, three notions of conjugation can be defined on $\COOO$.  Here, the complex conjugate is the same as before: $i\mapsto -i$.  For the octonionic and hermitian conjugates, the definition is also the same as for the $\CO$ case, bearing in mind that these conjugates now reverse the order of the chain algebra's multiplication, $\circ$.


Looking more closely at the chains, we notice quickly that

\begin{equation}\label{flip}
\overleftarrow{\cdots e_ae_b\cdots} f = -\hspace{1.5mm}\overleftarrow{\cdots e_be_a\cdots} f \hspace{0.5cm} \forall f \in \mathbb{C}\otimes\mathbb{O},
\end{equation}

\noindent for $a,b = 1,2,\dots 7$, when $a\neq b$.  Furthermore,

\begin{equation}\label{snip}
\overleftarrow{\cdots e_ie_je_je_k\cdots} f = -\hspace{1.5mm}\overleftarrow{\cdots e_ie_k\cdots} f \hspace{0.5cm} \forall f \in \mathbb{C}\otimes\mathbb{O},
\end{equation}

\noindent when $i, k = 0, 1, 2, \dots 7$ and $j=1,2, \dots 7$.  With these properties, the chains acting on $\CO$ provide a representation of the Clifford algebra $\CLseven$, where $\{i\overleftarrow{e_1}, i\overleftarrow{e_2}, \dots i\overleftarrow{e_7}\}$, acting on $f$, forms the generating set of vectors, \cite{baez}.  

It turns out, though, that $\COOO$ does not give a faithful representation of $\CLseven$.  There exists an additional symmetry, which identifies  two monomial chains with the same map.  For example, $\overleftarrow{e_1e_2e_3}f =-\overleftarrow{e_4e_5e_6e_7}f,$ $\overleftarrow{e_5e_7}f =-\overleftarrow{e_1e_2e_3e_4e_6}f,$ $\overleftarrow{e_7}f =\overleftarrow{e_1e_2e_3e_4e_5e_6}f$, etc.  These 64 equations (duality relations) are readily found by making use of equations (\ref{flip}) and (\ref{snip}), and also the following form of the identity: $\overleftarrow{e_0}f=-\overleftarrow{e_1e_2e_3e_4e_5e_6e_7}f$.  We then see that any element of $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ may be represented as a complex linear combination of chains, of no more than three $e_j$s in length.

The reader is encouraged to check that $\mathbb{C}\otimes\overleftarrow{\mathbb{O}}$ faithfully represents the 64-complex-dimensional Clifford algebra $\CLsix$, generated by the set $\{i\overleftarrow{e_1}, i\overleftarrow{e_2}, \dots i\overleftarrow{e_6}\}$, acting on $f$.  Figure~(\ref{cliff6}) depicts the complex octonionic chain algebra, organized so as to demonstrate its $\CLsix$ structure.  Starting from the bottom, we have the zero-vector, $1$ acting on $f$, the generating vectors, $\{i\overleftarrow{e_1}, i\overleftarrow{e_2}, \dots i\overleftarrow{e_6}\}$ acting on $f$, the bivectors, $\{\overleftarrow{e_1e_2},\dots  \overleftarrow{e_5e_6}\}$ acting on $f$, and so on.  Note that we make regular use the identity $\overleftarrow{e_7}f=\overleftarrow{e_1e_2e_3e_4e_5e_6}f$ so as to avoid writing long chains of multivectors involving only the generators $i\overleftarrow{e_1}, \hspace{.7mm}i\overleftarrow{e_2}, \dots i\overleftarrow{e_6}$.  

For readers more comfortable with matrices and column vectors, one may loosely think of $\COOO$ as a space of $8\times8$ complex matrices, whereas the elements, $f$, would be represented by 8-complex-dimensional column vectors.



\begin{figure}[h!]
\begin{center}
\includegraphics[width=10cm]{cl6_blackblue-eps-converted-to.pdf}
\caption{\label{cliff6}
The 64-complex-dimensional octonionic chain algebra gives a representation of $\CLsix$.  This octonionic chain algebra is a space of maps acting through left multiplication onto any element $f\in\mathbb{C}\otimes\mathbb{O}$.}
\end{center}
\end{figure}


\newpage

Now that we have described octonionic left multiplication, by making use of an associative algebra, one might wonder if we have lost something by neglecting right multiplication.  It turns out, though, that unlike in the $\CH$ case, every complex octonion multiplied from the right may be re-expressed as a sum of chains of octonions, multiplying from the left,

\begin{equation}\label{COOOgen}

fm = c_0f  + \sum_{i=1}^7 c_i \overleftarrow{e_i}f + \sum_{j=2}^7\sum_{i=1}^{j-1}c_{ij} \overleftarrow{e_{i}e_{j}}f + \sum_{k=3}^7\sum_{j=2}^{k-1}\sum_{i=1}^{j-1}c_{ijk} \overleftarrow{e_{i}e_{j}e_{k}}f,

\end{equation}

\noindent for $f$, $m$ $\in\CO$, and  for some $c_0, c_i,  c_{ij}, c_{ijk} \in \mathbb{C}$.  In other words,  these right-multiplication maps are already accounted for by $\COOO$.






Finally, one might ask, if we are moving to a Clifford algebraic description of octonionic multiplication via $\CLsix$ anyway, why not just start with $\CLsix$ in the first place?  The answer to this question is two-fold.  First of all, in starting only from Clifford algebras, one would be hard-pressed to know which Clifford algebras to choose.  That is, an infinite number of Clifford algebras exist, and there appears to be no reason to choose one over any other.  Secondly, with an octonionic description of $\CLsix$, we will be able to map particles into ant-particles, and vice versa, using only the complex conjugate, $i\mapsto -i$.  This is typically not the case when Clifford algebras are expressed as matrices with complex components, as was already shown in the $\CH \simeq \CLtwo$ case of Section~\ref{lr} for left- and right- handed Weyl spinors.
