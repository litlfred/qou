---
doc_id: arxiv-2402.08782v1
doc_title: "Hecke–Farey coordinates for Bring’s surface"
section_id: sec-002-3-the-congruence-subgroups-of-the-hecke-groups
section_title: "The congruence subgroups of the Hecke groups"
section_number: 3
pages: 3-4
source_pdf: 2402.08782v1.pdf
source_sha256: 30311f0bd815f93f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.946
doc_brief: "Hecke–Farey coordinates for Bring’s surface — The modular group Γ (which is the Hecke group H3) can be used to study triangular maps, Here we use the Hecke group H4 to study the reg- ular map that"
---
Let $I$ be an ideal of  $\mathbb Z[\lambda_{q}]$.\\We define
 \begin{equation*}
  PSL(2,\mathbb Z[\lambda_{q}],I) = \left\{ \left(
  \begin{matrix}
    a & b \\ c & d 
  \end{matrix}
  \right) \in PSL(2,\mathbb Z[\lambda_{q}]) \; |\;  a-1,b,c,d-1\;\in I
  \right\}.
\end{equation*}

Now for any ideal $I$ of  $\mathbb Z[\lambda_{q}]$ we define the $\mathit{ principal\; congruence \;subgroup}$ of the Hecke group $H_{q}$ as, $$H_{q}(I)=PSL(2,\mathbb Z[\lambda_{q}],I) \cap H_{q},$$ that is, the subgroup of $H_{q}$ consisting of elements in $PSL(2,\mathbb Z[\lambda_{q}])$.  For our interest we take the special case when $I=(n)$ where $2\leq n\in \mathbb{Z}^+$, i.e. $(n)$ is a principal ideal of $\mathbb{Z}[\sqrt{m}]$ where $m=2,3$ for $q=4,6$. The even principal congruence subgroup is now    \begin{equation}
  H_q^e(n) = \left\{ \left(
   \begin{matrix}
    a    & b \sqrt{m} \\
   c \sqrt{m}     & d \\
  \end{matrix}
  \right) \in H_q^e \; |\; a\equiv d \equiv \pm 1 \;  \text{mod}\; n, \; b\equiv c \equiv  0 \;   \text{mod}\; n
  \right\}.
  \label{h:1}
\end{equation}  
As  $a\sqrt{m}$ and $d\sqrt{m}$  are not congruent to $ \pm 1$ mod $n$ we can not have odd elements in $H_q(n).$

\vspace{1cm}




For $q=$4 or 6 and for $n>2$, the index of $H_q(n)$ in $H_q$ was found by Parson~\cite[Theorem 2.3]{Par76}.
\vspace{1cm}

\begin{theorem}\label{p} 
 \begin{equation}
\label{dk1c}
\mu_q(n)=|H_q:(H_q)(n)|= \begin{cases}
                           n^3   \prod_{p|n} (1-\frac{1}{p^2})             &if \; (n,m)=1\\
               n^3 (1-\frac{1}{m})   \prod_{p|n,p\neq m} (1-\frac{1}{p^2})               &if \; (n,m)=m.
           \end{cases}
\end{equation}
 
\end{theorem}   
\vspace{1cm}


Now we are interested in the quotient spaces $\mathbb{H}/ H_{4}(n)$. \\  
The fundamental region $F_{\lambda_4}$ for $ H_{4}$ is the region of the upper-half plane bounded by the unit circle and the lines $Re(z)=\pm{\sqrt 2/2}.$



\begin{figure}[H]
  \caption{The fundamental region $F_{\lambda_4}$ for $H_{4}$ }
    \includegraphics[width=0.6\textwidth]{FRQR}
    \centering
    \label{f9}
\end{figure} 


This fundamental domain is not compact  and in fact the quotient space $\mathbb{H}/H_4$ has one puncture corresponding to the point at infinity in the fundamental domain. Thus  $\mathbb{H}/H_4(5)$ is a punctured surface.   However its compactification  $\overline {\mathbb{H}/H_4(5)}$ (found by adding the punctures) is a compact Riemann surface. Now by Theorem \ref{p},   $H_4(5)$ is a normal subgroup of index 120 in $H_4$ and so $\overline {\mathbb{H}/H_4(5)}$  is a compact Riemann surface with 120  automorphisms.
  
   
   
   \vspace{1cm}

   We now show its genus is equal to 4.  $H_4$ is the $\Gamma(2, \infty, 4)$ triangle group so that by \cite{JS78}  $\mathbb{H}/H_4(5)$ has the structure of a topological map. In fact, as $H_4(5)$ is a normal subgroup of $H_4$ (of index 120  by Theorem \ref{p}) it is a regular map with 120/2 =60 edges, 120/4=30 vertices and 120/5=24 faces. Thus if $g$ is the genus then $2-2g=30-60+24= -6,$ giving $g=4.$
      \vspace{1cm}

   
As $\mathbb{H}/H_4(5)$ has 120 automorphisms then by Theorem \ref{p} we deduce
\vspace{1cm}

 \begin{theorem}  
 $\overline {\mathbb{H}/H_4(5)}$ is Bring's surface.
   \end{theorem}
