---
doc_id: arxiv-2402.08782v1
doc_title: "Hecke–Farey coordinates for Bring’s surface"
section_id: sec-001-2-brings-surface
section_title: "Bring's surface"
section_number: 2
pages: 1-3
source_pdf: 2402.08782v1.pdf
source_sha256: 30311f0bd815f93f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.935
doc_brief: "Hecke–Farey coordinates for Bring’s surface — The modular group Γ (which is the Hecke group H3) can be used to study triangular maps, Here we use the Hecke group H4 to study the reg- ular map that"
---
We start with the following result which comes from Conder and Dobcsanyi's classifications of regular maps of small genus~\cite{CD01}.
 
  \begin{theorem} \label{th1}There is a unique regular map of type $\{5,4\}$ of genus 4 with 120 automorphisms.  The automorphism group of this map here is the symmetric group $S_5$.
    \end{theorem}

  Underlying this map is a unique Riemann surface of genus 4 with automorphism group $S_5$.  This surface is called {\it Bring's Surface}.  (Type $\{5, 4\}$ means that all faces are quadrilaterrals and all vertices have valency 5.)

 
We let $\Gamma(2, 5, 4)$ denote the triangle group with periods 2, 5, 4.  This triangle group acts as a group of conformal  automorphisms of the upper-half complex plane $\mathbb{H}$ and it has a presentation  
 
$$\Gamma(2,5,4)=\langle X,Y,Z\,|\,X^{2}=Y^{5}=Z^{4}=XYZ=1\rangle.$$
  \vspace{0.2cm}

  There is an epimorphism $\theta:\Gamma(2,5,4)\mapsto S_5$ given by $X\mapsto x=(1, 5),   Y\mapsto y=(5,4,3,2, 1)$,  and $Z\mapsto z=(2, 3, 4, 5).$
  
  The kernel $K$ of this epimorphism is a surface group of index 120 in $\Gamma$ and so by the Riemann-Hurwitz formula $\mathbb{H}/K$ is a Riemann surface of genus 4 with $S_5$ as automorphism group and so by Theorem \ref{th1}, this surface is Bring's Surface.
  
  As $K$ is a normal subgroup of the triangle group $\Gamma(2, 5, 4)$, it follows from~\cite{JS78} that underlying  Bring's surface  there is a regular map of type $\{5, 4\}$ which we consider in more detail later.

  \vspace{0.2cm}

  All compact Riemann surfaces arise from compact algebraic curves.  Bring's surface is the underlying Riemann surface of  {\it Bring's Curve} which is the complete intersection of of the three hyper-surfaces
\begin{equation}
\sum_{i=1}^{5} x_i = 0\;\;\;\; \sum_{i=1}^{5} x_i^{2} = 0\;\;\;\;\sum_{i=1}^{5} x_i^{3} = 0.
\end{equation} 
  \vspace{0.2cm}

Another way of considering Bring's Surface is  in terms of the Hecke group $H_4$.

Consider a group with the two generators $T: z\mapsto z+\lambda$ and $S: z\mapsto \frac{-1}{z}$.

Hecke showed that this group is discrete, i.e., a Fuchsian group, if and only if 


(i) $\lambda=\lambda_q=2\cos \frac{\pi}{q}$ or 

(ii) $\lambda\ge 2$.
  \vspace{0.2cm}

We are interested in case (i).\\

We then find that $$R(z)=TS(z)=\frac{\lambda_q z-1}{z}.$$

This transformation is represented by the matrix 
$$\begin{pmatrix}\lambda_q&-1\\1&0\\\end{pmatrix}.$$

The eigenvalues of this matrix are $e^{\pm \pi i/q}$ and so $R$ has period $q$.  It is known that as a group  $H_q\cong C_2*C_q$.
  \vspace{0.2cm}

In this paper we are interested in the case  $q=4$ and then $\lambda_4=\sqrt 2$.
  The group $H_4$ has two generators 
  
 $$T:z\mapsto z+\sqrt 2 \;\;\;\;and\;\;\;\;  S: z\mapsto \frac{-1}{z}.$$
 
  Writing the M\"obius transformations as matrices we find that the transformations of $H_4$ are of two types\\
 (i) $$\begin{pmatrix}a&b\sqrt 2\\c\sqrt 2& d\\ \end{pmatrix}  \;  a,b,c,d \in \mathbb{Z} \;,\; ad-2bc=1$$ \\ and\\(ii) $$\begin{pmatrix}a\sqrt 2&b\\c&d\sqrt 2\\ \end{pmatrix}\;  a,b,c,d \in \mathbb{Z} \;,\; 2ad-bc=1.$$
 
 The matrices of type (i) form a subgroup of index 2 in $H_4$ and are called {\it even} matrices.  We denote this subgroup by $H_{4}^{e}$.
 The matrices of type (ii) are called {\it odd} matrices and they form a coset.
