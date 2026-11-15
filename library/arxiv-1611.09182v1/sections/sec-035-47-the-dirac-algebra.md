---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-035-47-the-dirac-algebra
section_title: "The Dirac algebra"
section_number: 4.7
pages: 34-36
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 1.0
doc_brief: "Standard model physics from an algebra? — 77 sections: Front matter; Abstract; Acknowledgements"
---
It is not enough for us here to consider minimal left ideals for just $\Psi_{\textup{L}}$ or for just $\Psi_{\textup{R}}$, separately.  We would like also to combine these two objects together into a single four-complex-dimensional Dirac spinor, as shown in Section~\ref{WD}.

It had been mentioned earlier that chirality, L and R, is the analogue of spin, $\uparrow$ and $\downarrow$, in this formalism.  One can confirm that left multiplying $\Psi_{\textup{L}}$ and $\Psi_{\textup{R}}$ by $\CH$ causes rotation between their spin states, $\uparrow$ and $\downarrow$, whereas right multiplying $\Psi_{\textup{L}}$ and $\Psi_{\textup{R}}$ by $\CH$ causes rotation between L and R.  



The left action and right action of $\CH$ on itself each give a representation of $\CLtwo$.  Furthermore, taking $\ell,$ $a$, $r$ $\in\CH$, one can easily show that $\ell a = ar$ $\forall a$ $\Rightarrow$ $\ell, r$ $\in\mathbb{C} \subset \CH$.  That is, the left action of $\CH$ on itself cannot be re-expressed as the right action of $\CH$ on itself, and vice versa.  It is a property of $\CH$ that these two actions are distinct, a feature which does not appear in the case of $\CO$.  Furthermore, the associativity of $\CH$ ensures that the left and right action commute with each other.  Hence, the underlying Clifford algebraic structure when considering both left and right multiplication of $\CH$ on itself is $\CLtwo\otimes_{\mathbb{C}}\CLtwo$, where the tensor product is over $\mathbb{C}$. 

As $\mathbb{C}l(n) \otimes_{\mathbb{C}} \CLtwo \simeq \mathbb{C}l(n+2)$ for $n\in\mathbb{Z}\geq 0,$ we then find that $\CLtwo\otimes_{\mathbb{C}}\CLtwo\simeq \CLfour$.  Furthermore, as the complexification of a real Clifford algebra, $Cl(p,q)$ acts to erase its signature, $\mathbb{C}\otimes Cl(p,q) \simeq \mathbb{C}l(p+q)$, we then find that $\CLfour\simeq \mathbb{C}\otimes Cl(1,3)$.  

In other words, the left and right action of $\CH$ on itself gives a representation of the Dirac algebra.





It is straightforward for readers to confirm this fact.  Explicitly, the gamma matrices $\gamma^0$, $\gamma^1$, $\gamma^2$, and $\gamma^3$, written in the Weyl basis, have the following correspondences in $\CH$:

\begin{equation}\begin{array}{ccc}
\gamma^0 = \left(   \begin{array}{cc} 0 & I \\ I & 0 
\end{array}\right) \hspace{2mm} \mapsto \hspace{2mm} 1\hspace{1mm} | \hspace{1mm} i{\epsilon_x}    &  \hspace{1cm} &
\gamma^1 = \left(   \begin{array}{cc} 0 & \sigma_x \\ -\sigma_x & 0 
\end{array}\right)  \hspace{2mm}\mapsto \hspace{2mm} i{\epsilon_x}\hspace{1mm} | \hspace{1mm} {\epsilon_y}   \vspace{5mm}\\

\gamma^2 = \left(   \begin{array}{cc} 0 & \sigma_y \\ -\sigma_y & 0 
\end{array}\right) \hspace{2mm} \mapsto \hspace{2mm} i{\epsilon_y}\hspace{1mm} | \hspace{1mm} {\epsilon_y}    &  \hspace{1cm} &
\gamma^3 = \left(   \begin{array}{cc} 0 & \sigma_z \\ -\sigma_z & 0 
\end{array}\right)  \hspace{2mm}\mapsto \hspace{2mm} i{\epsilon_z}\hspace{1mm} | \hspace{1mm} {\epsilon_y}. 

\end{array}\end{equation}

\noindent These findings are likely to appear in future joint work with G. Fiore from INFN.  

Here, we make use of the bar notation from earlier authors, \cite{deleoGUT}.  By definition, the operator $a\hspace{1mm} | \hspace{1mm} b$ acting on some element $c$, for $a,b,c\in\CH$, is given simply by $acb$.  As an example, consider the object corresponding to $\gamma^0$  acting on $\Psi_{\textup{D}}\in\CH$,

\begin{equation} \begin{array}{l}    1\hspace{1mm}  \Psi_{\textup{D}} \hspace{1mm} i{\epsilon_x}  =  1\hspace{1mm} \left( \Psi_{\textup{L}}+ \Psi_{\textup{R}}\right) \hspace{1mm} i{\epsilon_x}\vspace{3mm}\\ =  \left( \psi^{\uparrow}_{\textup{L}} \hspace{1mm} \epsilon_{\uparrow \uparrow} +  \psi^{\downarrow}_{\textup{L}} \hspace{1mm} \epsilon_{\downarrow \uparrow}  + \psi^{\uparrow}_{\textup{R}} \hspace{1mm} \epsilon_{\uparrow \downarrow} +  \psi^{\downarrow}_{\textup{R}} \hspace{1mm} \epsilon_{\downarrow \downarrow}  \right)  \hspace{1mm} i{\epsilon_x}\vspace{3mm}\\   = \left( \psi^{\uparrow}_{\textup{R}} \hspace{1mm} \epsilon_{\uparrow \uparrow} +  \psi^{\downarrow}_{\textup{R}} \hspace{1mm} \epsilon_{\downarrow \uparrow}  + \psi^{\uparrow}_{\textup{L}} \hspace{1mm} \epsilon_{\uparrow \downarrow} +  \psi^{\downarrow}_{\textup{L}} \hspace{1mm} \epsilon_{\downarrow \downarrow}  \right).
\end{array}\end{equation}  

\noindent This flips chirality, as one would expect.  

From these operators, an object corresponding to $\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3$ can be found to be 

\begin{equation} \gamma^5 = \left(   \begin{array}{cc} -I & 0 \\ 0 & I 
\end{array}\right)  \hspace{2mm} \mapsto \hspace{2mm} -1\hspace{1mm} | \hspace{1mm} i{\epsilon_z}.
\end{equation}

\noindent This thereby confirms the role of $P$ and $P^*$ as $\frac{1}{2}\left(1\mp\gamma^5\right)$, introduced early on in equation~(\ref{cma}).


More generally, it can now be seen that $  \Psi_{\textup{D}} =   \Psi_{\textup{L}}+  \Psi_{\textup{R}}$ introduced previously, does in fact behave as a Dirac spinor, acted upon by a complex quaternionic representation of the Dirac algebra, $\mathbb{C}\otimes Cl(1,3)$.
