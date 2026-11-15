---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-002-3-quatrisson-and-tetraplectic-structures
section_title: "Quatrisson and tetraplectic structures"
section_number: 3
pages: 4-5
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.986
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
Recall that a symplectic manifold is a manifold equipped with a closed 
non-degenerate 2-form. We also recall 
that a Poisson manifold is a 
manifold equipped with a  bi-vector field that induces a Lie algebra structure 
on the space of smooth functions,  compatible with the commutative
product of functions via the Leibniz rule.
In the case of quaternionic flags, 
we make use of the following structures which reflect the  underlying geometry:

\begin{definition} \cite{F1}
	Let $X$ be a real orientable manifold of dimension $4m$.  
	A {\emph tetraplectic} structure on X is a  four-form, $\psi$ satisfying: 

	\begin{tabular}{c l } 
		$1)$ & $\psi$ is closed ($d\psi=0$)\\ 
		$2)$ & $\psi^{m}$ is a volume form \\ 
	\end{tabular} 
	
	\noindent We call the pair
	 $(X, \psi)$  a \emph{tetraplectic manifold}. A map
	$\phi: (X, \psi)\to (X', \psi')$ is called \emph{tetraplectic} if 
	$\phi^*\psi'=\psi$. If, in addition, $\phi$ is a diffeomorphism, then
	we call $\phi$ a \emph{tetraplectomorphism}. 
\end{definition} 
 


\example 
	Let $\psi$ be an $\Sp[2]$-invariant volume form on $S^{4}$.
	Then ($\HP[1]$,$\psi$)  is 
	a teraplectic manifold.
	In fact, in \cite{F1} the construction of invariant tetraplectic structures
	on all quaternionic flag manifolds was given. 
\qex 

\
 
\noindent One can define a standard Poisson structure 
on a manifold by giving a bi-vector field whose
the Schouten bracket with itself is zero. 
However, in order to reflect the geometry 
of our situation we will make use of 4-vector fields, for
which we recall the following \cite{Vais}:  

\begin{prop} 
	Denoting $\Wedge^i\Chi(M)$ 
	the space of $i$-vector fields on $M$,	
	there exists a unique  bracket, called the \emph{Schouten bracket}:
	\begin{displaymath}
		[\cdot,\cdot]:\Wedge^{p}\Chi(M)\times\Wedge^{q}\Chi(M) 
		\rightarrow\Wedge^{p+q-1}\Chi(M)
	\end{displaymath} 
	which extends the usual Lie bracket of vector fields and is an 
	$\R$-linear operation satisfying the following identities:  

	\begin{tabular}{l c r} 
		$1)$ 
			& 
			$[P,Q] = (-1)^{pq}[Q,P]$ 
				& 
				(Anti-Symmetry) 
		\\
		$2)$ 
			& 
			$[P,Q\wedge R] = [P,Q]\wedge R  + (-1)^{pq+q}Q\wedge[P,R]$ 
				& 
				(Leibniz)
		\\
       	 	$3)$ 
			& 
			$(-1)^{p(r-1)}[P,[Q,R]] + (-1)^{q(p-1)}[Q,[R,P]]$  
				& 
				{} 
		\\ 
	  	{}   
			& 
			$+ (-1)^{r(q-1)}[R,[P,Q]] = 0$  
				& 	
				(Jacobi)
	\end{tabular}  
\end{prop} 



\noindent We recall that in \cite{Perelomov} the authors  
use the  vanishing of the Schouten bracket  
of a $p$-vector field $\xi$ with itself, $[\xi,\xi]=0$,
to define the Generalized Poisson Structures (GPS).
For etymologic-semantic reasons, we give 
the following definition:

\begin{definition} 
	Let $M$ be a manifold, and let $\xi$ be a 4-vector field 
	on $M$ satisfying $[\xi, \xi]=0$. We call $\xi$ a \emph{quatrisson} 
	structure on $M$ and the pair $(M, \xi)$ a \emph{quatrisson manifold}. 
\end{definition}

\begin{definition} 
	For two quatrisson manifolds ($X$, $\xi$) and ($X'$,$\xi'$) 
	a map $\phi:X\rightarrow X'$ is called a \emph{quatrisson map} if 
	for any quadruple of functions $f_i\in C^{\infty}(X')$, 
	$1\le i\le 4$
	the following identity holds: 
	\begin{displaymath}
		\xi( d\phi^*f_1\wedge d\phi^* f_2\wedge d\phi^* f_3\wedge d\phi^* f_4)=
		\phi^* \xi'(df_1\wedge df_2\wedge df_3\wedge df_4).
	\end{displaymath}
	i.e. $\phi_*(\xi)=\xi'$. 
\end{definition} 
 

 
\begin{definition} 
	Let $\xi$ be a  4-vector field  on
	a $4m$-dimensional manifold, $M$.
	Then we call $\xi$  
	\emph{non-degenerate} if 
			$\xi^{\wedge m}$ is a nowhere vanishing 
$4m$-vector field. 
\end{definition} 

If $\xi$ is a non-degenerate vector field on $M$, then 
$\xi$ induces a surjection $\Wedge^3\CTn[x]{M}\rightarrow\Tn[x]{M}$ 
for all $x\in M$,  obtained by contraction with $\xi$.  
If $(M,\xi)$ is quatrisson, we define the \emph{rank} of $\xi$ at $x\in M$ 
as the dimension of the image of this map.
One can see that a quatrisson structure $\xi$ on $M$ is 
non-degenerate if the rank of $\xi$ at any point of $M$ is equal to the
dimension of $M$. 
 

\begin{lem} 
	Letting $(M, \xi)$ be as above, the 
	rank of $\xi$ at any $x\in M$ is divisible by 4. 
\end{lem} 

\proof This is an easy exercise in multi-linear algebra 
for the reader.   
\qed


\begin{definition} 
	Let $M$ be a manifold equipped with a 4-vector field
	$\xi$. We say that a smooth $4l$-dimensional 
	submanifold, $L$, is a \emph{tetraplectic leaf} in $M$ if:
	\begin{tabular}{c l}
		$1)$ 	
			&
		 	$\xi$ comes from  
			$\Wedge^{4}\Chi(L)$ at all points of $L$
		\\
		$2)$
			&
			$\xi$ is non-degenerate on $L$
		\\
		$3)$
			&
			$L$ is not properly included in any other such submanifold of $M$
		\\
		$4)$
			&
			the four-form, $\psi$,  given by $i_{\psi}\xi^{m}=\xi^{m-1}$, defines a 
		\\
		{}	
			&
			tetraplectic structure on $M$. 
	\end{tabular}
\end{definition} 


\noindent To each triple of functions ${\bf f}$=($f_1$, $f_2$, $f_3$), 
we can associate a ``hamiltonian'' vector field 
$X_{\bf f}$ given by $\iota(df_1\wedge df_2\wedge df_3)\xi$.
Then we get the \emph{characteristic distribution} of $M$. 
Unlike in the Poisson case, we cannot
expect in general that $(M, \xi)$ is stratified as a union of 
smooth tetraplectic leaves, even if $\xi$ is quatrisson,
see Example 8 in \cite{Ibanez2}. 
However, the particular case of this result 
for quaternionic flag manifolds will follow later.

\

\example Let $F_n$ be a quaternionic flag manifold considered as a 
tetraplectic manifold with an $\Sp[n]$-invariant $4$-form $\psi$ \cite{F1}. 
The corresponding  4-vector field, $\chi$, defined by
 $i_\chi(\psi^m)=\psi^{m-1}$,
 is quatrisson and $\Sp$-invariant. We refer to $\chi$
as the invariant quatrisson structure of $F_n$.
\qex
