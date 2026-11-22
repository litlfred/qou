---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-003-4-quatrisson-structures-on-bf-hp1
section_title: "Quatrisson structures on ${\bf HP}^1$."
section_number: 4
pages: 5-7
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.944
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
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
