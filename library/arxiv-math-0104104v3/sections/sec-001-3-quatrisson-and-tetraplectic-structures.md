---
doc_id: arxiv-math-0104104v3
doc_title: "arXiv:math/0104104v3 [math.DG] 29 Mar 2002"
section_id: sec-001-3-quatrisson-and-tetraplectic-structures
section_title: "Quatrisson and tetraplectic structures"
section_number: 3
pages: 4-10
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
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



 

\section{Quatrisson structures on ${\bf HP}^1$.} 
 
For our flag manifolds, we construct a Bruhat quatrisson structure explicitly by 
analogy to the  Poisson case as in \cite{LW} or \cite{Soibel}. 
We begin by defining a quatrisson 4-vector field, $\sham$, on $\Sp[2]$, which  
we show descends to the quotient $\Sph\backslash\Sp[2]$.   
 
We begin by defining an element $\Lambda$ of $\wedge^4\sp[2]$ 
in terms of the following basis for $\sp[2]$: 
\begin{eqnarray*} 
	E = \mat{0}{1}{-1}{0}	  
			&   	
			S_x = \mat{0}{x}{x}{0}  
	\\ 
	H_x = \mat{x}{0}{0}{-x}	  
			&  	
			M_x = \mat{x}{0}{0}{x}	  
\end{eqnarray*} 
where $x$ is one of $\{ \i, \j, \k\}$.  For convenience we denote
$S_{-x}:=-S_x$, $H_{-x} := -H_x$, and $M_{-x} := - M_x$.  We now can note the
following commutator relations: 
\begin{eqnarray*}
	{[M_x,E]}=0
		&
	{[H_x,E]}=2\cdot S_x
			&
			{[ S_x , E ]}=	2 \cdot H_x
\end{eqnarray*} 
\begin{eqnarray*}
	{[ M_x , M_y ] } = {[ H_x , H_y ]} =  {[ S_x , S_y ] }
		&
		= 
			&
			\Bigg\{ 
			\begin{tabular}{c l}
				$2\cdot M_{x\cdot y} $
					&
					$x\ne y$
				\\
				$0$
					&
					$x=y$
			\end{tabular} 
	\\
	{[S_x,H_y] }
		&
		=
			&
			\Bigg\{ 
			\begin{tabular}{c l}
				$0$
					&
					$x\ne y$
				\\
				$-2\cdot E$
					&
					$x=y$
			\end{tabular}
	\\
	{[S_x,M_y]}
		&
		=
			&
			\Bigg\{ 
			\begin{tabular}{c l}
				$0$
					&
					$x =  y$
				\\
				$2\cdot S_{x\cdot y}$
					&
					$x \ne y$
			\end{tabular}
	\\
		{[H_x,M_y]}
		&
		=
			&
			\Bigg\{ 
			\begin{tabular}{c l}
				$0$
					&
					$x =  y$
				\\
				$2\cdot H_{x\cdot y}$
					&
					$x \ne y$
			\end{tabular}
\end{eqnarray*}

\noindent We may now define: 
\begin{displaymath} 
	\Lambda :=E \wedge S_{\i} \wedge S_{\j}\wedge S_{\k}. 
\end{displaymath} 

\noindent and denoting by $\Lambda^{L}$ and $\Lambda^{R}$  the left 
and right 
invariant $4$-vector fields on $\Sp[2]$ with  value $\Lambda$ 
at the identity element, we let:
\begin{displaymath}	
	\sham=\Lambda^{L}-\Lambda^{R}.
\end{displaymath}
 
\begin{prop} 
	The 4-vector field $\sham$ is a quatrisson structure
	on $\Sp[2]$.  Moreover, $\sham$ 
	descends to  a vector field, $\Sham$,
	on 	$\HP[1]\simeq\Sph\backslash\Sp[2]$  inducing a $\Sph$-invariant quatrisson 
	structure on $\HP[1]$ called the 
	\emph{Bruhat quatrisson structure} \label{prop444} 
\end{prop} 

\proof 
	The fact that $\sham$ is a quatrisson structure on $\Sp[2]$ is
	nothing more than the fact that $[\sham,\sham]\in\Wedge^{7}\Chi(\Sp[2]) = 0$.
	To show that $\Sham$ is $\Sph$-invariant, and hence descends, we may apply
	the same formalism of the Poisson case
	and show that for any $X\in \sph$ we have $\ad{X}{\Lambda} = [X,\Lambda]=0$.
	This follows readily from the above commutator relations and 
	the Leibniz rule of the Schouten bracket.  It is clear that 
	$[\Sham,\Sham]=0$.
\qed

\ 



\noindent We can make use of the Bruhat decomposition to describe the vector 
field explicitly.  As above, we denote by $\CC_\id$ and $\CC_{(12)}$ 
the cells of $F_n$ corresponding to the 
North pole and the $\H$ components.
It is clear, that at the North pole $\sham$ is the zero vector.  
For $x\in \CC_{(12)}$ we
choose a convenient coset representative in $\Sp[2]$, 
namely:
\begin{displaymath}
	k_x = \frac{1}{\sqrt{1+\rho^2}} \cdot \mat{-\bar{v}}{1}{1}{v},  
\end{displaymath}
where $\rho = |v| = \sqrt{v\bar{v}}$. In fact, the identification of 
$S^4$ as a natural $SO(5)\simeq \Sp[2]/(\Z/2)$ -invariant submanifold of 
$\R^5$ with $\H$ plus the point at infinity using stereographic 
projection sends $v\in \H$ to a point in $S^4$ at the height
$\displaystyle{1-{1\over 1+|v|^2}}$ and the 
same $\Sp[1]$-angular coordinate. 

To compute $\Sham$ at $x$, we identify $\Tn[x]{\Sp[2]}$ with 
$\Tn{\Sp[2]}$ by right translations so that  we have
$\Lambda^{R} = \Lambda$ and  $\Lambda^{L}$ is simply 
conjugation of  $\Lambda$ by $k_x$.  We have thus expressed 
$\Sham=f(v)\partial_{v_1}\wedge\partial_{v_2}\wedge\partial_{v_3}\wedge\partial_{v_4}$
 in terms
of the coordinates $v=v_1+v_2\cdot \i+v_3 \cdot \j + v_4 \cdot \k$.  We would
like more natural coordinates for $\H$, namely if
$v=\rho\cdot\exp{\theta_1\cdot \i}\exp{\theta_2 \cdot \j}\exp{\theta_3 \cdot \k}\in \H$,
then we have $\Sham=$
$\displaystyle{\frac{g(\rho)}{\rho^3}\partial_\rho\wedge\Theta}$, for
 $\Theta=\partial_{\theta_1}\wedge\partial_{\theta_2}\wedge\partial_{\theta_3}$ -
the $\Sp[1]$-invariant $3$-vector field on $\Sp[1]\simeq S^3$. 
To find $g(\rho)$, we divide $\Sham$ by its value at $v=0$, the South pole. 
After a  computer assisted 
computation\footnote{We thank Klaus Lux and Stephane Lafortune for help with this.} 
we see that  
$\displaystyle{g(\rho)=\frac{(1+3\rho^4)}{(1+\rho^2)^3}}$. Thus we have proved that:

\begin{prop} 
	The invariant quatrisson structure on $S^4\simeq \HP[1]$
	is given by: 
	\begin{displaymath}
		\chi := {(1+\rho^2)^4\over \rho^3}\partial_\rho\wedge\Theta
	\end{displaymath}
	and the Bruhat quatrisson structure is given by:
	\begin{displaymath}
		\Sham = {(1+\rho^2)(1+3\rho^4)\over \rho^3}\partial_\rho\wedge\Theta.
	\end{displaymath}
	In particular we have that:
	\begin{displaymath}
	 	\Sham={1+3\rho^4\over (1+\rho^2)^3}\chi.
	\end{displaymath}
\end{prop} 

One can easily see that $\Sham$ has rank four everywhere except for
at the North pole, where it vanishes. Thus the two cells are characterized by 
the rank of $\Sham$.
 







\section{Quatrisson structures on  flag manifolds} 
 
Following \cite{Lu2} 
we will produce the quatrisson structure on the full flag of 
$\H^{n}$ by way of the so-called multiplication formula.  By analogy to the $\Sp[2]$
 case, for $1\le p<q \le n$ 
 we denote by $E^{p,q}$ the quaternionic matrix whose entries are $0$'s
 everywhere except in the 
($p$,$q$)-th position which is $1$, and the ($q$,$p$)-th position which is $-1$. We also let  
$S_x^{p,q}$ denote the matrix with $0$'s  everywhere except in the 
($p$,$q$)-th and ($q$,$p$)-th positions where the entries are $x$ where $x$ is again
chosen from $\{\i, \j, \k\}$.  Similarly,
these matrices are clearly in the Lie algebra, $\sp$, of $\Sp$, 
and correspond to ``positive roots''
(i.e. pairs of integers $1\le p< q\le n$) as in \cite{Lu2}.   We  define
 $\Lambda\in\Wedge^4\Tn{\Sp}$ by:
\begin{displaymath} 
	\Lambda=\sum_{p<q} E^{p,q}\wedge S_{\i}^{p,q}\wedge S_{\j}^{p,q}\wedge S_{\k}^{p,q}.
\end{displaymath} 
Then if $\Lambda^{L}$ and $\Lambda^{R}$ are the right and left invariant 
$4$-vector fields on $\Sp$ with the values  $\Lambda$ at the identity element
on $\Sp$, we let:
\begin{displaymath}
	 \sham=\Lambda^{L}-\Lambda^{R}.
\end{displaymath}


Unlike the $\Sp[2]$ case, when $n> 2$, one can readily check that $\sham$ will
not be a quatrisson structure on $\Sp$ by making use of the Leibniz rule and commutator
relations similar to those as above and noting that there will be some terms that will not cancel.
However, we still have:

\begin{prop} 
	The 4-vector field $\sham$ descends to $\Sph\backslash\Sp$, inducing a
	\Sph -invariant quatrisson structure, $\Sham$, 
	called the \emph{Bruhat quatrisson structure}.
\end{prop} 

\proof 
	For $\sham$ to descend and be invariant we need to show that both
	the left and right translations by elements of the Spheroid 
	leave $\sham$ invariant, meaning that the 
	adjoint action by the Spheroid on $\Lambda$ is trivial.
	This can be checked similarly to the $n=2$ case  of Proposition
	\ref{prop444}. One can also directly check that $[\Sham, \Sham]=0$ on
	$\Sph\backslash\Sp$, which will also follow from Proposition
\ref{prop:p247}.
\qed

\

\noindent We recall:

\begin{definition}\label{def:mult-act}
	Let $H$ be a Lie group equipped with a 
	multiplicative 4-vector field $\mu$, 
	which acts on a quatrisson manifold $(P, \xi)$:
	\begin{displaymath}
		\beta:H\times P\to P.
	\end{displaymath}
	We say that $H$ acts \emph{multiplicatively} if,
	denoting the corresponding translation maps:
	\begin{eqnarray*}
	 	\beta_h:P\to P
			&
				&
				\beta_y:H\to P
		\\
		y\mapsto h\cdot y
			&
				&
				h \mapsto h\cdot y
	\end{eqnarray*}
	we have:
	\begin{displaymath}
		\xi(h\cdot x) = \beta_{h_{\ast}}\xi(x) + \beta_{x_{\ast}}\mu(h).
	\end{displaymath}
	We sometimes say that the actions is multiplicative with respect to the
	direct sum $4$-vector field $\mu\oplus\xi$ on $H\times P$.
\end{definition}
 
\noindent and notice the following fact (cf. \cite{LW}, \cite{KS}):

\begin{lemma}
	The $4$-vector field $\sham$ on $\Sp$ is 
	multiplicative.
\end{lemma}


\begin{prop} 
	Let $\Sham$ be the Bruhat quatrisson structure on $\Sph\backslash\Sp$.  
	The action map: 
	\begin{displaymath} 
		\Sp \times \Sph\backslash\Sp \rightarrow \Sph\backslash\Sp 
		: (g,h)\mapsto g\cdot h 
	\end{displaymath} 
	is multiplicative with respect to the four-vector field $\sham\oplus\Sham$ 
	on $\Sp\times(\Sph\backslash\Sp)$. 
\end{prop} 
\proof Straightforward.
\qed

\

\noindent We will also make use of the following embeddings:
\begin{eqnarray*}
	f_{r,r+1}:  \Sp[2]  
		&
		\hookrightarrow  
			&
			\Sp 
	\\
	A
		&
		\mapsto 
			&
			A_{r,r+1}
\end{eqnarray*}
where $1\le r <n$ and for  
$A=\mat{a}{b}{c}{d}$  the matrix $A_{r,r+1}$ is given by: 
\begin{displaymath} 
	  \left( \begin{tabular}{c c c c}
		$Id$	 
			&
				&
					&
					$0$
		\\
			&
			$a$
				&
				$b$
					&
		\\
			&
			$c$
				&
				$d$
					&
		\\
		$0$ &
				&
					&
					$Id$
	\end{tabular}\right)
	\begin{tabular}{c}
		$\leftarrow r^{th}$ row 
		\\ 
		\\ 
		\\
	\end{tabular} 
\end{displaymath} 
 
\

\begin{lemma}
	The embeddings $f_{r,r+1}: \Sp[2] \hookrightarrow \Sp$ respect the
	multiplicative 4-vector fields $\sham$. 
\end{lemma}
\proof
	Straightforward. 
\qed


\begin{prop}
	Every tetraplectic leaf $L$ of $\Sp$ lies entirely in some $\ZZ_w$. 
	If $L_w$ is a tetraplectic leaf containing the permutation matrix $P_w$ 
	corresponding to some $w\in S_n$, and we  write
	$w=\prod_{i=1}^{m}\tau_i$ as a minimal product
	of adjacent transpositions, we have a tetraplectomorphism:

	\begin{tabular}{c c l c}
		$F_w:$
			& 
			$L_{\tau_1}\times\dots\times L_{\tau_m}$ 
				& 
				$\rightarrow$ 
					& $L_w$ 
		\\
	           	& 
			$(l_1,\dots,l_m)$ 
				& 
				$\mapsto$     
					& 
					$l_1 l_2 \dots l_m$ 
	\end{tabular}

	\noindent Moreover,  for $\sigma\in\Sph$, 
	the tetraplectic leaf through $\sigma P_w$ equals  $\sigma L_w$.   
\label{prop:p247} \end{prop}

\proof (cf. \cite{Lu2}, \cite{Soibel}.) 
	Immediately follows from the discussion above.
\qed

\

\noindent More explicitly, one can follow \cite{Lu2} to identify $L_w$ with the
$\VV_w$ - orbit of $P_w$, and 
in the next section, we will define and exploit the analogues of the 
dressing action \cite{STS} to get clearer picture of the tetraplectic leaves. 
In any case,  we have the following:
 
\begin{Th} 
	The tetraplectic leaf decomposition of the quaternionic 
	flag manifold $F_n\simeq \BB\backslash\GL{\H}$ arising from the Bruhat
	quatrisson structure coincides with the Bruhat cell decomposition.  
\end{Th} 
\proof 
	The important point is that any tetraplectic leaf in $\Sp$ under 
	the quotient map $\Sp\to \Sph\backslash \Sp$ maps tetraplectomorphically 
	onto a Bruhat cell as follows from the results in this section. 
\qed
