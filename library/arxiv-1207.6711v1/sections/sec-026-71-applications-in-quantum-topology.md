---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-026-71-applications-in-quantum-topology
section_title: "Applications in quantum topology"
section_number: 7.1
pages: 23-25
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.965
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sub.applicationsQT}

Recently, ideal triangulations $\CT$ of 3-manifolds $M$ with torus boundary 
components
and their gluing equations have found several applications
in quantum topology, and this has been a main motivation for our work. We
will list three applications here, and refer to the literature for more
details:

\begin{itemize}
\item[(a)] The {\em Quantum Riemann surfaces} of \cite{Di1}
\item[(b)] The {\em loop invariants} of \cite{DG}
\item[(c)] The {\em 3D index} of \cite{DGG1,DGG2,Ga-3Dindex}
\end{itemize}

The input of a quantum Riemann surface of \cite{Di1} is an ideal triangulation 
$\CT$ of a 3-manifold with torus boundary components, and the output is
a polynomial in $q$-commuting variables (one per meridian and longitude
of each torus boundary component). The operators generate a $q$-holonomic
ideal which depends on $\CT$ and ought to map to the gluing
equation variety $V_2(\CT)$ when $q=1$. 

The input of the loop invariants of \cite{DG} is a Neumann-Zagier datum
which consists of an ideal triangulation together with a solution of
the gluing equations whose image under the map \eqref{eq.dev2} is
the discrete faithful representation of $M$. The output is
a formal power series in a variable $\hbar$ with
coefficients rational functions on the image of the map  
\eqref{eq.dev2}. The coefficient of $\hbar$ in the above series ought to agree
with the non-abelian torsion of \cite{Porti} and the evaluation of the
series at the discrete faithful representation when $\hbar=2\pi i/N$, ought
to agree to all orders in $1/N$ with the asymptotics of the Kashaev invariant
\cite{Kashaev} of a hyperbolic knot complement.
 
The input of the 3D index of \cite{DGG1,DGG2} (see also the survey
article \cite{Ga-3Dindex}) is an ideal triangulation $\CT$ which supports
a strict angle structure. The output is a $q$-holonomic function $
I_{\CT}: \BZ^{2r} \longto \BZ((q^{1/2}))$ where $r$ is the number of torus
boundary components of $M$ and $\BZ((q^{1/2}))$ is the ring of Laurent 
series in $q$ with integer coefficients.

Using our Theorems \ref{thm:soft} and \ref{thm:ShortMainThm}, one can extend 
the above invariants to the case of representations in $\PGL(n,\BC)$.
For example, fix an ideal triangulation $\CT$ with $t$ tetrahedra
of a 3-manifold $M$ with torus boundary. Following \cite[Sec.1.2]{DG},
choose a pair of opposite edges of each subsimplex, remove $n-1$ gluing
equations which are dependent on the others, and replace them with the
$n-1$ cusp equations of the meridian to obtain matrices $r \times r$
$A_n$ and $B_n$ where $r=t\binom{n+1}{3}$. Let $z$ denote the $r$ vector
of shapes of solutions to the gluing equations. Following 
\cite[Defn.1.1]{DG} consider the Neumann-Zagier datum 
$\b_{\CT,n}=((A_n|B_n),z)$ and its enhanced version 
$\hat\b_{\CT,n}=((A_n|B_n),z,f)$ where $f$ is a choice of flattening of each
subsimplex. Following \cite[Defn.1.2]{DG} we define the 1-loop invariant
of $\hat\b_{\CT,n}$ by

\be 
\qquad\tau_{\CT,n} = 
\pm \frac12\det\big( A_n\Delta_{z''}
+B_n\Delta_z^{-1}\big)z^{f''}z''^{-f}
\ee

where $\Delta_z:=\diag(z_1,...,z_r)$ and 
$\Delta_{z''}:=\diag(z_1'',...,z_r'')$ are diagonal matrices, and  
$z^{f''}z''^{-f} := \prod_i z_i{}^{f''_i}z''_i{}^{-f_i}$. When $z$ is the
solution that comes from the discrete faithful representation of $M$,
then $\tau_{\CT,n}$ lies in the invariant trace field of $M$.
An exact computation is possibe using the SnapPy tools \cite{SnapPy}. 
We thank N. Dunfield for providing an automated code for exact computation. 
Let us give some examples.

\begin{example}
\label{ex:411loop}
The $4_1$ knot has invariant trace field $\BQ(x)$ where 
$$
x^2 - x + 1=0, \qquad x=\frac{1+i \sqrt{3}}{2}
$$
If $\tau_n=\tau_{4_1,n}$, the quotient $\tau_{n+2}/\tau_n$
appears to have lower complexity than $\tau_n$ and is given by
\begin{align*}
\tau_2 &= 1/2 - x &
\tau_3 &= 21/2
\\
\frac{\tau_4}{\tau_2} &= 6720 &
\frac{\tau_5}{\tau_3} &= 52147200
\\
\frac{\tau_6}{\tau_4} &= -5381278156800 &
\frac{\tau_7}{\tau_5} &= -7383730314510950400
\\
\frac{\tau_8}{\tau_6} &= -138731589652863387775795200 &
\end{align*}
\end{example}

\begin{example}
\label{ex:52.1loop}
Consider the knot $5_2$ with invariant trace field $\BQ(x)$ where
$$
x^3-x^2+1=0, \qquad x=0.877439 \dots -i \, 0.744862 \dots \,.
$$
The {\em mirror} $-(-2,3,7)$ of the $(-2,3,7)$ pretzel knot has the same volume
and the same invariant trace field as $5_2$.  
If $\tau_n=\tau_{5_2,n}$ and $\tau'_n=\tau_{-(-2,3,7),n}$ 
then we have

{\small
\begin{align*}
\tau_2 &= 1-3/2 x &
\tau'_2 &= -2 + 5  x -3  x^2
\\
\frac{\tau_3}{\tau_2} &= -63+ 57 x^2 &
\frac{\tau'_3}{\tau'_2} &= -120 -48  x + 144  x^2
\\
\frac{\tau_4}{\tau_3} &= 1536 -3072 x -9792 x^2 &
\frac{\tau'_4}{\tau'_3} &= 21984 + 5712  x -31008  x^2
\\
\frac{\tau_5}{\tau_4} &= -12831360 -10393200 x +  8023440 x^2 &
\frac{\tau'_5}{\tau'_4} &= -3196800 + 14346000  x +  24614400  x^2
\\
\frac{\tau_6}{\tau_5} &= -95788707840 -84869406720 x  &
\frac{\tau'_6}{\tau'_5} &= 158834390400 + 213765955200 x 
\\
 & \quad + 55161630720 x^2 & & \quad + 4444675200 x^2
\end{align*}
}
\end{example}
