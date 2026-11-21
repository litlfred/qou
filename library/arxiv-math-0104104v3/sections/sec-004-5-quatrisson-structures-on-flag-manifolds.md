---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds"
section_id: sec-004-5-quatrisson-structures-on-flag-manifolds
section_title: "Quatrisson structures on flag manifolds"
section_number: 5
pages: 7-10
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.929
doc_brief: "Geometry of Four-Vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-vector ﬁelds on quaternionic ﬂag manifolds, which geometrically determine"
---
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
