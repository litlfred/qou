---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-007-34-on-parabolic-representations-of-twist-knot-gr
section_title: "On parabolic representations of twist knot groups"
section_number: 3.4
pages: 6-8
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{ParRep}

In this subsection, we are interested in the \emph{parabolic representations} of (hyperbolic) two--bridge knot groups and especially twist knot groups. The holonomy representation is one of them. Lemma~\ref{L8} characterizes the holonomy representation algebraically and says that it corresponds to a root of Riley's equation $\phi_K(1,u) = 0$. A natural and interesting question is the following: which roots of Riley's equation $\phi_K(1,u) = 0$ correspond to the holonomy representation? Here we will give a geometric characterization of such roots {in the case of two--bridge knots}.


\subsubsection{Remarks}

We begin this section by some elementary but important remarks on the roots of Riley's equation $\phi_K(1,u) = 0$ corresponding to holonomy  representations.
\begin{enumerate}
  \item One can first notice that such roots are necessarily \emph{complex numbers which are not real}, because the discrete and faithful representation is irreducible and \emph{not} conjugate to a real representation (i.e. a representation such that the image of each element is a matrix with real entries).
  \item One can also observe that holonomy representations correspond to \emph{a pair of complex conjugate roots} of  Riley's equation $\phi_K(1,u) = 0$ as it is easy to see.
\end{enumerate}



\subsubsection{Generalities: the case of two--bridge knots}
Let $K$ be a hyperbolic two--bridge knot.
Suppose that a presentation of the knot group $\Pi(K)$ is given as in Eq.~(\ref{P:G2B}) by
\[
\Pi(K) = \langle {x, y \, |\, \Omega x = y\Omega} \rangle, \text{ where } \Omega \text{ is a word in } x,y. 
\]
The longitude of $K$ is of the form: $\lambda = \stackrel{\gets}{\Omega}\Omega \, x^n$. Here $n$ is an integer such that 
the sum of the exponents in the word $\lambda$ is $0$ and we repeat that $\stackrel{\gets}{\Omega}$ denotes the word obtained from $\Omega$ by reversing the order of the letters.

Let $\rho \colon \Pi(K) \to \SL$ be a representation such that: 
\[
x \mapsto 
\pm \left(
\begin{array}{cc}
1 &  1 \\
  0          &  1 
\end{array}
\right)
, \quad
y \mapsto 
\pm \left(
\begin{array}{cc}
 1 & 0 \\
  - u &  1 
\end{array}
\right)
\]

where $u$ is necessarily a root of Riley's equation $\phi_K(1,u)=0$. 
Suppose that 
\[
\rho(\Omega) = \left(\begin{array}{cc}w_{1,1} & w_{1,2} \\w_{2,1} & w_{2,2}\end{array}\right)
\]
where $w_{i,j}$ is a polynomial in $u$ for all $i, j \in \{1,2\}$.



Riley's method gives us the following identities (see Section~\ref{ReviewCharK}):
\[
w_{1,1} = 0 \text{ and } u w_{1,2} + w_{2,1} = 0. 
\]
Thus
\[
\rho(\Omega) = \left(\begin{array}{cc}0 & w_{1,2} \\ -u w_{1,2} & w_{2,2}\end{array}\right).
\]
The fact that $\rho(w) \in \SL$ further gives the following equation:
\begin{equation}\label{UW}
u w_{1,2}^2 = 1.
\end{equation}

The crucial point for computing $\rho(\lambda)$ is to express $\rho(\stackrel{\gets}{\Omega})$ with the help of $\rho(\Omega)$.  
Consider the diagonal matrix:
\[
\mathbf{i} = \left(\begin{array}{cc}i & 0 \\0 & -i\end{array}\right) \in \SL,
\]
where $i$ stands for a square root of $-1$. Let $Ad$ denote the adjoint representation of the Lie group $\SL$. Then the following identities hold:
\[
\rho(x^{-1}) = Ad_{\mathbf{i}} (\rho(x)), \; 
\rho(y^{-1}) = Ad_{\mathbf{i}} (\rho(y))  
\text{ and } 
\rho(\Omega^{-1}) =  Ad_{\mathbf{i}} (\rho(\stackrel{\gets}{\Omega})).
\]
Thus, we have
\[
 \rho(\stackrel{\gets}{\Omega}) 
= Ad_{\mathbf{i}} (\rho({\Omega}^{-1})) 
= \left(
  \begin{array}{cc}
    w_{2,2} & w_{1,2} \\
    w_{2,1} & w_{1,1}
  \end{array}
  \right).
\]
Next, a direct computation gives:
\begin{equation}\label{long}
\rho(\lambda) = \rho(\stackrel{\gets}{\Omega}) \rho(\Omega) \rho(x)^n =\left(\begin{array}{cc}-u w^2_{1,2} & -n u w^2_{1,2} + 2w_{1,2}w_{2,2} \\0 & -u w^2_{1,2}\end{array}\right).
\end{equation}
Combining Eqs.~(\ref{UW}) and~(\ref{long}), we obtain
\begin{equation}\label{long2}
\rho(\lambda) = \left(\begin{array}{cc}-1 & -n + 2w_{1,2}w_{2,2} \\0 & -1\end{array}\right).
\end{equation}
And we conclude that the \emph{cusp shape of $K$} is 
\begin{equation}\label{cuspshape_bridge}
\cusp = n -  2w_{1,2}w_{2,2}.
\end{equation}

\begin{remark}
In particular, Eq.~(\ref{long2}) gives us, by an elementary and direct computation, Calegari's result~\cite{Calegari}: $\mathrm{tr}\, \rho_0(\lambda) = - 2$ for the discrete faithful representation $\rho_0$ associated to the complete hyperbolic structure of the exterior of a (hyperbolic) two--bridge knot.
\end{remark}



\subsubsection{The special case of twist knots}
In the case of hyperbolic twist knots, we can further estimate $w_{i,j}$ in Eq.~(\ref{cuspshape_bridge}). In fact, we only consider the case where $K = J(2, 2m)$ in what follows. 
The group $\Pi(K)$ of such a knot has the following presentation:
\[
\Pi(K) = \langle {x, y \, |\, w^m x = y w^m} \rangle,
\]
where $w$ is the commutator $[y,x^{-1}]$ (see Fact~\ref{Fact1}, Section~\ref{TwistKnots}). A direct computation of the commutator $\rho(w) = [\rho(y),\rho(x)^{-1}]$ gives:
\[
W= \rho(w) = \left(
\begin{array}{cc}
  1-u  & -u \\
  u^2  & u^2+u+1
\end{array}
\right) \quad (\text{where } u \text{ is such that } \phi_K(1,u) = 0).
\]

Using the Cayley--Hamilton identity, it is easy to obtain the following recursive formula for the powers of the matrix $W$:
\begin{equation}\label{CH}
W^k - (u^2+2) W^{k-1} + W^{k-2} = 0, \; k \geqslant 2.
\end{equation}
Eq.~(\ref{CH}) implies, by induction on $k$,
\[
w_{2,2} = - (u+2) w_{1,2}.
\]
Since $n = 0$ and $u w_{1,2}^2 = 1$, the \emph{cusp shape of the twist knot $K$} is:
\[
\cusp = n + (2u+4)w_{1,2}^2 = \frac{2u+4}{u}.
\]


    In other words, the root $u_0$ of Riley's equation $\phi_K(1,u) = 0$ corresponding to the holonomy representation satisfies the following equation:
\begin{equation}\label{cuspshape}
u_0 = \frac{4}{\cusp - 2},
\end{equation}
where $\cusp$ is the cusp shape of the knot exterior.

\begin{remark}
Eq.~(\ref{cuspshape}) gives a geometric characterization of the (pair of complex conjugate) roots of Riley's equation $\phi_K(1,u) = 0$ associated to the holonomy representation in terms of the cusp shape, a geometric quantity associated to each cusped hyperbolic $3$-dimensional manifold.
\end{remark}
