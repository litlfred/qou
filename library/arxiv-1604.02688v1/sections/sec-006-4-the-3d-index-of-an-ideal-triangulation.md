---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-006-4-the-3d-index-of-an-ideal-triangulation
section_title: "The 3D-index of an ideal triangulation"
section_number: 4
pages: 6-8
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.906
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Using the notation from the previous section, we now give a definition of 
the 3D-index of an ideal triangulation $\tri$ as formulated 
in \cite[section 4.7]{GHRS}. 

Given $\kk =(k_1, \ldots, k_n)\in \Z^n$, we can assign an integer weight 
$k_i$ to the $i$th edge class. Effectively, this also gives a weight on 
each edge of each tetrahedron $\sigma_j$ in $\CT$.
Let $a_j(\kk), b_j(\kk), c_j(\kk)$ be the sums of weights assigned to 
the pair of edges in  tetrahedron $j$ opposite quads $q_j, q_j',q_j''$ 
respectively. Note that these coefficients are precisely the entries in 
the linear combination $\sum_{i=1}^n k_i E_i$ of the rows of the gluing matrix 
corresponding to the edge equations. 

Now we define a tetrahedral index associated to the tetrahedron $\sigma_j$ by
$$
J(\sigma_j;\kk)=\JD(a_j(\kk), b_j(\kk) , c_j(\kk)).
$$
and the \emph{3D-index}  $I_{\CT}({\bf 0})$ of the triangulation $\CT$ is 
defined as 
\be
I_{\CT}({\bf 0})(q)  = \sum_{\kk \in \Z^{n-r}} 
 q^{\sum_i k_i}   \prod_{j=1} ^n
J(\sigma_j;\kk),
\ee
where the summation is over a (suitable) sublattice  
$\Z^{n-r} \subset \Z^{n}$, obtained by setting $r$ of the edge weights 
$k_i$ equal to zero. For $r=1$ we can set any $k_i=0$; but  in general the 
$r$ edge weights set to zero must be chosen carefully (see 
\cite[sections 4.5, 4.6]{GHRS}).

More generally, the 3D-index gives a function 
$I_{\CT} : H_1(\bd M; \Z) \cong \Z^{2r}\to \Z((q^\frac{1}{2}))$ defined 
as follows. Let $\gamma$ be an oriented multicurve on $\bd M$ with no 
contractible components, such that $\gamma$  is in {\em normal position} 
with respect to the induced triangulation $\tri_\bd$ of $\bd M$. 
Then let $\gamma_h$ be the component of $\gamma$ in cusp $h$ and express 
$\gamma_h = p_h \mu_h + q_h \lambda_h$, where $\mu_h$ corresponds to the 
row $M_h$ in the gluing matrix and $\lambda_h$ corresponds to $L_h$.
Now put
$$
J(\sigma_j;\kk,\gamma)=\JD(a_j(\kk,\gamma), b_j(\kk,\gamma) , c_j(\kk,\gamma))
$$
where the coefficients  
$a_j(\kk,\gamma), b_j(\kk,\gamma), c_j(\kk,\gamma)$ are precisely the 
entries in the linear combination 
$\sum_{i =1}^nk_i E_i  +\sum_{h=1}^n (p_h M_h + q_h L_h)$ corresponding 
to tetrahedron $\sigma_j$.

Then the general \emph{3D-index} of the triangulation $\CT$ is defined as 
\be
I_{\CT}([\gamma])(q)  = \sum_{\kk \in \Z^{n-r}} q^{\sum_i k_i}   \prod_j 
J(\sigma_j;\kk,\gamma),
\label{JD_index_eq}
\ee
where $[\gamma] \in H_1(\bd M; \Z)$ is the homology class of $\gamma$ and
the summation is over $\Z^{n-r} \subset \Z^{n}$ as above. (It is shown 
in \cite{GHRS} that the sum only depends on the homology class of $\gamma$.)

\begin{ex}
\label{ex:fig8}
For the figure eight knot complement $M$, with the ideal triangulation 
given by Thurston \cite[\sect4]{Th}, we have the following 
induced triangulation on $\bd M$ (as viewed from the cusp).

\begin{center}
\begin{figure}[htpb]
\includegraphics[width=0.8\textwidth]{figures/figure8Cusp_new}
\caption{\label{fig:figure8cusp} A labelled triangulation of the cusp 
of the figure 8 knot complement.}
\end{figure}
\end{center}

From this we can read off the following gluing data.

\begin{table}[htpb]
\begin{tabular}{|c||c|c|c|c|c|c|}
\hline
edge/peripheral curve
& ~~$a_1$~~ & ~~$b_1$~~ & ~~$c_1$~~ & ~~$a_2$~~ & ~~$b_2$~~ & ~~$c_2$ \\
\hline
\hline
edge 1 (blue) & 2 & 1 & 0 & 2 &1 & 0 \\
\hline
edge 2 (red) & 0& 1 & 2& 0 & 1 & 2 \\ 
\hline
meridian $\mu$ & 0& 0 & 1& -1 & 0 & 0 \\ 
\hline
longitude $\lambda$ & 0& 0 & 0& 2  & 0 & -2\\ 
\hline
\end{tabular}
\end{table}

Choosing generators $\mu,\lambda$ for $H_1(\bd M, \Z) = \Z^2$ corresponding 
to the standard meridian and longitude, and integer weights $k_1=k,k_2=0$ 
on the edges gives

\begin{align*} 
I_{\CT}(x \mu + y\lambda )
&=\sum_{k \in \Z}  q^k \JD(2k,k,x)\JD(2k-x+2y,k,-2y) \\
& = \sum_{k \in \Z}  \ID(k-x,k) \ID(k+2y,k-x+2y).
\end{align*}

For example, up to terms of order $q^{10}$, we have 

\begin{align*}
I_{\CT}({\bf 0} ) &=  
1-2 q-3 q^2+2 q^3+8 q^4+18 q^5+18 q^6+14 q^7-12 q^8-52 q^9-106 q^{10} + \ldots
\\
I_{\CT}(\mu) &= 
2 q-2 q^2+2 q^3+8 q^4+16 q^5+16 q^6+10 q^7-14 q^8-52 q^9-102 q^{10}+ \ldots
\\
I_{\CT}(2\mu) &= 
-q - q^2 + 3 q^3 + 6 q^4 + 12 q^5 + 9 q^6 + 3 q^7 - 19 q^8 - 50 q^9 -  88 q^{10}
+ \ldots \\
I_{\CT}(\lambda ) &=  
q^3+2 q^4+5 q^5+2 q^6-3 q^7-16 q^8-32 q^9-52 q^{10}+ \ldots \\
I_{\CT}(4\mu+\lambda ) &= 
q-q^4-2 q^5-5 q^6-8 q^7-10 q^8-11 q^9-6 q^{10}+ \ldots
\end{align*}
In this example, it is easy to check that 
$I_{\CT}(\pm x \mu  \pm y \lambda)=I_{\CT}(x \mu + y\lambda)$,
and we can also define the index for $x \in \Z, y \in \frac{1}{2} \Z$, 
as done in \cite{DGG1}. For example,

\begin{align*}
I_{\CT}(\frac{1}{2} \lambda) &= -2 q^{3/2}+4 q^{7/2}+10 q^{9/2}
+14 q^{11/2}+10 q^{13/2}-2 q^{15/2}-32 q^{17/2}-68   q^{19/2} + \ldots \\
I_{\CT}(\mu+\frac{1}{2} \lambda) &= -q-q^2+2 q^3+7 q^4+11 q^5+11 q^6
+3 q^7-17 q^8-49 q^9-88 q^{10} + \ldots  \\
I_{\CT}(2\mu+\frac{1}{2} \lambda) &=
-q^{1/2}+q^{5/2}+4 q^{7/2}+7 q^{9/2}+7 q^{11/2}+3 q^{13/2}-12 q^{15/2}
-31 q^{17/2}-62 q^{19/2}  + \ldots 
\end{align*}
\end{ex}
