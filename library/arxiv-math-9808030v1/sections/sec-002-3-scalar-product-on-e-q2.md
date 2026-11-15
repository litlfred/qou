---
doc_id: arxiv-math-9808030v1
doc_title: "Planscherel Measure on Eq(2)"
section_id: sec-002-3-scalar-product-on-e-q2
section_title: "Scalar Product on $E_q(2)$"
section_number: 3
pages: 6-8
source_pdf: 9808030v1.pdf
source_sha256: 7889d6481b876b12
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.973
doc_brief: "Planscherel Measure on Eq(2) — Following the construction of the invariant integral and the scalar product for the quantum Euclidean group Eq(2), we obtained the full matrix elements of its unitary"
---
Let $\Phi (E_q(2))$ be the set of analytic functions on $E_q(2)$ such that 
\begin{equation}
\label{plan1}\psi (f f^*)<\infty , 
\end{equation}
where $\psi$ is the invariant integral (\ref{invine}) on $E_q(2)$.

Recall that the homomorphism 
\begin{equation}
\phi (z)=0, \ \ \ \phi (z^*)=0, \ \ \ \phi (\delta)=t 
\end{equation}
defines the quantum subgroup $U(1)\subset E_q(2)$. We have then the
decomposition 
\begin{equation}
\label{plan2}\Phi(E_q(2))=\sum_{ij\in Z}\oplus \Phi[i,j] 
\end{equation}
where 
\begin{equation}
\Phi[i,j]=\{ f\in \Phi(E_q(2)) : L (f) = t^i\otimes f ; \ \ R (f) = f\otimes
t^j \} 
\end{equation}
and 
\begin{equation}
L = (\phi \otimes id)\circ \Delta ,\ \ \ \ R = (id\otimes \phi )\circ\Delta
. 
\end{equation}
The subspace $\Phi[i,j]\subset\Phi(E_q(2))$ consists of the elements of the
following form 
\begin{equation}
\label{plan3}f_{ij} (g) = \delta^jz^{i-j} f_{ij}(\rho^2), \ \ \ \ \ for \ \
i\geq j 
\end{equation}
and 
\begin{equation}
\label{plan4}f_{ij} (g) = \delta^j(z^*)^{j-i} f_{ij}(\rho^2), \ \ \ \ \ for
\ \ i\leq j, 
\end{equation}
where $\rho^2 =zz^*$.

By means of the invariant integral we introduce in $\Phi (E_q(2))$ the
bilinear forms 
\begin{equation}
\label{plan6}(f , f^\prime )_L =\psi (f^* f^\prime ) 
\end{equation}
and 
\begin{equation}
\label{plan7}(f^\prime , f )_R =\psi (f^\prime f^*) 
\end{equation}
related to each other as 
\begin{equation}
\label{plan8}( f , f^\prime )_L=(\tau(f^\prime ), f)_R, 
\end{equation}
where $\tau $ is the automorphism in $E_q(2)$ defined as 
\begin{equation}
\tau (z)=qz, \ \ \tau (z^*)=q^{-2}z^*, \ \ \tau (\delta )=q^{-4}\delta 
\end{equation}
By the virtue of (\ref{plan3}) and (\ref{plan4}) we get 
\begin{equation}
\label{top4}\tau (f)=q^{-2(i+j)}f 
\end{equation}
for $f\in \Phi[i,j]$. To prove the identity (\ref{plan8}) we use the
following representation for the invariant integral 
\begin{equation}
\label{plan10}\psi (f)=(1-q^2)Tr (f\rho^2), 
\end{equation}
which is the result of (\ref{invine}). In this representation the equality (
\ref{plan8}) reads 
\begin{equation}
Tr( f^* f^\prime \rho^2)=Tr(\tau(f^\prime )f^*\rho^2). 
\end{equation}
Due to the decomposition (\ref{plan2}) it is enough to verify that (\ref
{plan10}) is valid for $f\in \Phi [i,j]$ and $f^\prime\in\Phi [i^\prime,
j^\prime]$. The latter can easily be verified by using (\ref{plan3}), (\ref
{plan4}), (\ref{top4}) and (B.7).

The representation ({\ref{plan10}) of the invariant integral allows us to
prove that the bilinear forms (\ref{plan6}) and (\ref{plan7}) are scalar
products in $\Phi (E_q(2))$. For that purpose we put $F=f\rho $ and $
F^{\prime }=f^{\prime }\rho $ in (\ref{plan6}) and using (\ref{plan10}) we
get 
\begin{equation}
(f,f^{\prime })_L=(1-q^2)Tr(F^{*}F^{\prime }).
\end{equation}
The left hand side of the above equality defines the scalar product in the
space of Hilbert--Schmidt type operators. Thus the bilinear form (\ref{plan6}
) defines the scalar product in $\Phi (E_q(2))$. In a similar fashion one
can show that bilinear form (\ref{plan7}) is also scalar product. }

From (\ref{plan3}), (\ref{plan4}), (\ref{repe1}) and (\ref{invine}) we have 
\begin{equation}
(f_1 , f_2 )_{L, R} =0, 
\end{equation}
for $f_1\in \Phi [i,j]$, $f_1\in \Phi [i^{\prime},j^{\prime}]$ such that $
(i,j)\neq (i^{\prime},j^{\prime})$. Thus the decomposition (III.3) is
orthogonal with respect to the scalar products (\ref{plan6}) and (\ref{plan7}
).

\vspace{1cm}

\renewcommand{\theequation}{IV.\arabic{equation}} \setcounter{equation}{0}
