---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-002-bimodule-categories-functors-and-natural-transfo
section_title: "(Bi)module categories, functors and natural transformations"
section_number: null
pages: 5-9
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.935
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
In this section, we summarise background on (bi)module categories, (bi)module functors and (bi)module natural transformations from \cite[Ch.~7]{EGNO}.

\begin{definition}\label{def:modulecat}
Let $\mac, \mad$ be multitensor categories with associators  $a:\oo(\oo\times\id)\Rightarrow\oo(\id\times\oo)$ 
and left and right unit constraints  $l: e\oo \id\Rightarrow \id$,  $r:\id \oo e\Rightarrow \id $.
\begin{compactenum}
\item  A {\bf $\mac$-(left) module category} is a locally finite $\C$-linear abelian category $\mam$ together with
\begin{compactitem}
\item a functor $\rhd:\mac\times\mam\to\mam$ that is $\C$-bilinear on the morphisms and exact in the first variable, 
\item  natural isomorphisms 
$c: \rhd(\oo\times\id_\mam)\Rightarrow \rhd(\id_\mac\times\rhd)$ and $\gamma: e\rhd -\Rightarrow \id_\mam$
\end{compactitem}
such that  the following diagrams commute for all  $x,y,z\in\Ob \mac$ and $m\in\Ob \mam$:
\begin{align}\label{eq:pentagoncdef}
&\xymatrix{
((x\oo y)\oo z)\rhd m \ar[r]^{c_{x\oo y, z,m}} \ar[d]_{a_{x,y,z}\rhd 1_m}& (x\oo y)\rhd (z\rhd m) \ar[r]^{c_{x,y,z\rhd m}} & x\rhd(y\rhd(z\rhd m))\\
(x\oo(y\oo z)) \rhd m \ar[r]_{c_{x,y\oo z, m}}& x\rhd ((y\oo z)\rhd m)\ar[ru]_{\quad1_x\rhd c_{y,z,m}}
}\\
&\xymatrix{ (x\oo e)\rhd m \ar[rr]^{c_{x,e,m}} \ar[rd]_{r_X\rhd 1_m}  & & x\rhd (e\rhd m) \ar[ld]^{1_x\rhd \gamma_m}\\
&x\rhd m.
}\label{eq:trianglec}
\end{align}

\item A {\bf $\mad$-right module category} is  a  locally finite $\C$-linear abelian category $\mam$ together with 
\begin{compactitem}
\item a functor $\lhd:\mam\times \mad\to\mam$ that is $\C$-bilinear on the morphisms and exact in the second variable, 
\item  natural isomorphisms 
$d: \lhd(\lhd \times\id_\mad)\Rightarrow \lhd(\id_\mam\times\oo)$ and $\delta: -\lhd e\Rightarrow \id_\mam$
\end{compactitem}
that make the following diagrams commute for all  $x,y,z\in\Ob \mad$ and $m\in\Ob \mam$
\begin{align}\label{eq:pentagonddef}
&\xymatrix{
((m\lhd x)\lhd y)\lhd z \ar[r]^{d_{m\lhd x, y,z}} \ar[d]_{d_{m,x,y}\lhd 1_z}& (m\lhd x)\lhd (y\oo z) \ar[r]^{d_{m,x,y\oo z}} & m\lhd(x\oo(y\oo z))\\
(m\lhd(x\oo y)) \lhd z \ar[r]_{d_{m,x\oo y,z}}& m\lhd ((x\oo y)\oo z)\ar[ru]_{\quad 1_m\lhd a_{x,y,z}}
}\\
&\xymatrix{ m\lhd (e\oo x) \ar[rr]^{d_{m,e,x}} \ar[rd]_{1_m\lhd l_X}  & & (m\lhd e)\lhd x \ar[ld]^{\delta_m\lhd 1_x}\\
&m\lhd x.
}\label{eq:triangled}
\end{align}


\item A  {\bf $(\mac,\mad)$-bimodule category}  is a   locally finite $\C$-linear abelian  category $\mam$  with
\begin{compactitem}
\item a $\mac$-left module category structure $(\rhd,c,\gamma)$, 
\item a $\mad$-right module category structure $(\lhd, d,\delta)$, 
\item a natural isomorphism
 $b: \lhd(\rhd\times\id_\mad)\Rightarrow \rhd(\id_\mac\times\lhd)$
 \end{compactitem}
such that  the following diagrams commute for all  $x,y\in\Ob \mac$, $u,v\in\Ob \mad$ and $m\in\Ob \mam$
\begin{align}\label{eq:pentagonbdef}
&\xymatrix{
((x\oo y)\rhd m)\lhd u \ar[r]^{b_{x\oo y, m,u}} \ar[d]_{c_{x,y,m}\lhd 1_u}& (x\oo y)\rhd (m\lhd u) \ar[r]^{c_{x,y,m\lhd u}} & x\rhd(y\rhd(m\lhd u))\\
 (x\rhd(y\rhd m))\lhd u \ar[r]_{b_{x, y\rhd m, u}}& x\rhd ((y\rhd m)\lhd u)\ar[ru]_{\quad 1_x\rhd b_{y,m,u}}
}\\
&\xymatrix{
((x\rhd m)\lhd u)\lhd v \ar[r]^{d_{x\rhd m,u,v}} \ar[d]_{b_{x,m,u}\lhd 1_v}& (x\rhd m)\lhd (u\oo v) \ar[r]^{b_{x,m,u\oo v}} & x\rhd(m\lhd(u\oo v))\\
 (x\rhd(m\lhd u))\lhd v \ar[r]_{b_{x, m\lhd u, v}}& x\rhd ((m\lhd u)\lhd v).\ar[ru]_{\quad 1_x\rhd d_{y,m,u}}
}
\end{align}
\end{compactenum}
\end{definition}

A $\mad$-right module category can be defined more succinctly as a $\mad^{rev}$-module category and a $(\mac,\mad)$-bimodule category as a $\mac\boxtimes \mad^{rev}$-module category, where $\boxtimes$ is the Deligne product.  We expanded the definitions to set up  notation and  introduce the relevant diagrams. 


\begin{remark}\label{rem:macmodule} \cite[Prop.~7.1.3]{EGNO}\\
 $\mac$-module category structures on $\mam$ correspond bijectively to 
monoidal functors $F:\mac\to \End(\mam)$. The monoidal functor defined by a $\mac$-module structure assigns to an object $x$ in $\mac$ the endofunctor $x\rhd -:\mam\to\mam$ and to a morphism $\alpha:x\to y$ in $\mac$ the natural transformation $\alpha\rhd-:x\rhd-\Rightarrow y\rhd -$.  The monoidal structure of $F$ is given by the natural isomorphisms $\gamma: e\rhd-\Rightarrow\id_\mam$ and $c_{x,y,-}: (x\oo y)\rhd -\Rightarrow x\rhd (y\rhd -)$. 
 \end{remark}





\begin{example}\label{ex:bimodulecategory} 
 Every  fusion category $\mac$ is a $(\mac,\mac)$-bimodule category with $\rhd=\lhd=\oo:\mac\times\mac\to\mac$ and  coherence isomorphisms $c_{x,y,z}=d_{x,y,z}=b_{x,y,z}=a_{x,y,z}: (x\oo y)\oo z\to x\oo (y\oo z)$, $\gamma_x=l_x: e\oo x\to x$ and $\delta_x=r_x: x\oo e\to x$.
 \end{example}

\begin{example}\label{ex:vecmodule}
 Any locally finite $\C$-linear abelian category $\mam$ is a bimodule category over the fusion category $\mathrm{Vect}_\C$ of finite-dimensional complex vector spaces.  This  $\mathrm{Vect}_\C$-module category structure is unique up to bimodule equivalence (cf.~Definition \ref{def:modulefunc}).
\end{example}

\begin{example}\label{ex:dualcat}
For  any $(\mac,\mad)$-bimodule category $\mam$ over pivotal fusion categories $\mac,\mad$ the category $\mam^{op}$ is a $(\mad,\mac)$-bimodule category with 
\begin{align}\label{eq:opcat}
&\lhd^{op}=\rhd (*\times  \id_\mam)\tau: \mam\times\mac\to\mam & &\rhd^{op}=\lhd (\id_\mam\times *)\tau: \mad\times \mam\to\mam,
\end{align}
where $*: \mac\to\mac^{op,rev}$ is the duality functor  and  $\tau$ the flip functor that exchanges the two factors in a cartesian product. 
The coherence isomorphisms are given by $c^{op}_{x,y,m}=d_{m,y^*,x^*}$, $d^{op}_{x,y,m}=c_{y^*,x^*, m}$, $b^{op}_{x,m,y}=b_{y^*,m,x^*}$.
We call it the {\bf opposite bimodule category}  $\mam^\#$.
\end{example}




\begin{example} \label{ex:modvectgomega} \cite[Ex.~7.4.10]{EGNO}\\ Indecomposable semisimple module categories $\mam$  over  the fusion category $\mathrm{Vec}_G:=\mathrm{Vec}_G^{\omega\equiv 1}$, 
up to equivalence, correspond to pairs $(X, \psi)$ of a  finite transitive $G$-set $X\cong G/L$ and an element $\psi\in H^2(L, \C^{\times})$.
\begin{compactitem}
\item The objects of $\mam$ are $X$-graded vector spaces.
\item The simple objects of $\mam$ are of the form $\delta^x$ for $x\in X$ . 

\item The action functor $\rhd: \mathrm{Vec}_G\times\mam\to\mam$ is given by $\delta^g\rhd \delta^x=\delta^{g\rhd x}$ on the simple objects. 

\item The natural isomorphism $c:\rhd(\oo\times \id)\Rightarrow \rhd(\id\times\rhd)$ is given by $\psi\in H^2(L,\C^\times)$.
\end{compactitem}
\end{example}





\begin{definition}\label{def:modulefunc}
Let $\mac,\mad$ be multitensor categories.  
\begin{compactenum}
\item  A {\bf $\mac$-module functor} $F:\mam\to\man$ between $\mac$-module categories $\mam,\man$ is a $\C$-linear right exact functor $F:\mam\to\man$ together with a natural isomorphism
$s: F\rhd \Rightarrow \rhd(\id_\mac\times F)$ that satisfies the pentagon and the triangle axiom: for all $x,y\in\Ob\mac$ and $m\in\Ob\mam$ the following diagrams commute
\begin{align}\label{eq:pentagoncfunc}
&\xymatrix{ F((x\oo y)\rhd m) \ar[d]_{F(c_{x,y,m})}\ar[r]^{s_{x\oo y, m}} & (x\oo y)\rhd F(m) \ar[r]^{c_{x,y, F(m)}} & x\rhd (y\rhd F(m))\\
F(x\rhd(y\rhd m)) \ar[r]_{s_{x. y\rhd m}} & x\rhd F(y\rhd m)\ar[ru]_{\;\; 1_x\rhd s_{y,m}}
}\\
&\xymatrix{ F(e\rhd m)\ar[rd]_{F(\gamma_m)} \ar[rr]^{s_{e,m}} & & e\rhd F(m)\ar[ld]^{\gamma_{F(m)}}\\
& F(m).
}\label{eq:trianglecfunc}
\end{align}

\item A {\bf $\mad$-right module functor} $F:\mam\to\man$ between $\mad$-right module categories $\mam,\man$ is a $\C$-linear right exact functor $F:\mam\to\man$ together with a natural isomorphism
$t: \lhd(F\times\id_\mad)\Rightarrow F\lhd$ that satisfies the pentagon and the triangle axiom: for all $x,y\in\Ob\mad$ and $m\in\Ob\mam$ the following diagrams commute
\begin{align}\label{eq:pentagondfunc}
&\xymatrix{ (F(m)\lhd x)\lhd y \ar[d]_{t_{m,x}\lhd 1_y}\ar[r]^{d_{F(m),x, y}} &  F(m)\lhd(x\oo y) \ar[r]^{t_{m, x\oo y}} & F(m\lhd (x\oo y))\\
F(m\lhd x)\lhd y \ar[r]_{t_{m\lhd x, y}} & F((m\lhd x)\lhd y) \ar[ru]_{\;\; F(d_{m,x,y})}
}\\
&\xymatrix{ F(m)\lhd e \ar[rd]_{\delta_{F(m)}} \ar[rr]^{t_{m,e}} & & F(m\lhd e)\ar[ld]^{F(\delta_m)}\\
& F(m).
}\label{eq:triangledfunc}
\end{align}


\item A  {\bf $(\mac,\mad)$-bimodule functor}  between $(\mac,\mad)$-bimodule categories $\mam,\man$ is a $\C$-linear right exact functor $F:\mam\to\man$ with a $\mac$-module functor structure $s$ and a $\mad$-right module functor structure $t$ that satisfy the hexagon axiom: for all $x\in\Ob\mac$, $y\in\Ob\mad$ and $m\in\Ob\mam$ the following diagram commutes
\begin{align}
\label{eq:hexa}
\xymatrix{
F(x\rhd m)\lhd y\ar[d]_{s_{x,m}\lhd 1_y} \ar[r]^{t_{x\rhd m, y}} & F((x\rhd m)\lhd y) \ar[r]^{F(b_{x,m,y})}& F(x\rhd (m\lhd y))\ar[d]^{s_{x, m\lhd y}}\\
(x\rhd F(m))\lhd y \ar[r]_{\;b_{x, F(m),y}} & x\rhd (F(m)\lhd y)  \ar[r]_{1_x\rhd t_{m,y}} & x\rhd F(m\lhd y).
}
\end{align}
\end{compactenum}
An {\bf equivalence of (bi)module categories} is a (bi)module functor that is an equivalence of categories.
\end{definition}


\begin{definition}\label{def:modnat} Let $\mac,\mad$ be multitensor categories.
\begin{compactenum}
\item A $\mac$-module natural transformation $\nu: F\Rightarrow G$ for $\mac$-module functors $F,G: \mam\to\man$ is a natural transformation  such that the
following diagram commutes for all $x\in\Ob\mac$ and $m\in\Ob\mam$
\begin{align}
\label{eq:cnat}
\xymatrix{ F(x\rhd m)\ar[d]_{s^F_{x,m}} \ar[r]^{\nu_{x\rhd m}} & G(x\rhd m)\ar[d]^{s^G_{x,m}}\\
x\rhd F(m) \ar[r]_{1_x\rhd \nu_m} & x\rhd G(m).
}
\end{align}
\item A $\mad$-right module natural transformation $\nu: F\Rightarrow G$ for $\mad$-right module functors $F,G: \mam\to\man$ is a natural transformation  such that the
following diagram commutes for all $x\in\Ob\mad$ and $m\in\Ob\mam$
\begin{align}
\label{eq:dnat}
\xymatrix{ F(m)\lhd x \ar[d]_{t^F_{m,x}} \ar[r]^{\nu_{m}\lhd 1_x} & G( m)\lhd x\ar[d]^{t^G_{m,x}}\\
F(m\lhd x) \ar[r]_{\nu_{m\lhd x}} & G(m\lhd x).
}
\end{align}
\item A $(\mac,\mad)$-bimodule natural transformation $\nu: F\rightarrow G$ between $(\mac,\mad)$-bimodule functors $F,G: \mam\to\man$ is a natural transformation $\nu: F\Rightarrow G$  that is a $\mac$-module and a $\mad$-right module natural transformation.
\end{compactenum}
\end{definition}

For $\mac$-module categories $\mam,\man$ we denote by $\Fun_\mac(\mam,\man)$ the category of $\mac$-module functors $F:\mam\to\man$ and $\mac$-module natural transformations between them and write $\End_\mac(\mam)=\Fun_\mac(\mam,\mam)$. Analogously, for $(\mac,\mad)$-bimodule categories $\mam,\man$, we write
$\Fun_{(\mac,\mad)}(\mam,\man)$ for the category of $(\mac,\mad)$-bimodule functors $F:\mam\to\man$ and bimodule natural transformations between them and $\End_{(\mac,\mad)}(\mam)=\Fun_{(\mac,\mad)}(\mam,\mam)$.

Composites of (bi)module functors inherit a  (bi)module functor  structure.  If $G:\mam\to\man$ and $F:\man\to\map$ are $(\mac,\mad)$-bimodule functors, then the  $(\mac,\mad)$-bimodule functor structure for $FG:\mam\to\map$ is given by 
\begin{align}\label{eq:bimodcomp}
&s^{FG}=s^F (\id_\mac\times G)\circ Fs^G: FG\rhd \Rightarrow \rhd(\id_\mac\times FG)\\
& t^{FG}=Ft^G\circ t^F (G\times\id_\mad): \lhd(FG\times\id_\mad)\Rightarrow FG\lhd.\nonumber
\end{align}
For all  bimodule functors  $F,F':\man\to\map$, $G,G':\mam\to\man$   and bimodule natural transformations $\nu: F\Rightarrow F'$ and $\mu: G\Rightarrow G'$  the natural transformations $\nu G: FG\Rightarrow F'G$ and $F\mu: FG\Rightarrow FG'$ are bimodule natural transformations with respect to this bimodule functor structure. As composites of bimodule natural transformations are  also bimodule natural transformations, it follows that  $(\mac,\mad)$-bimodule categories, $(\mac,\mad)$-bimodule functors and $(\mac,\mad)$-bimodule natural transformations form a 2-category. 




The following examples show how the data of a (bi)module category can be recovered as coherence data of  (bi)module functors.
They are the categorical counterparts of standard constructions for modules over rings.



\begin{example}\label{ex:modulefuncs} Let $\mac,\mad$ be  multitensor categories with (right) centres $\mathcal Z(\mac)$, $\mathcal Z(\mad)$ and $\mam,\man$ $(\mac,\mad)$-bimodule categories. 
\begin{enumerate}
\item  For any $x\in\Ob \mad$ the functor
$F=-\lhd x: \mam\to\mam$  is a $\mac$-module functor with coherence isomorphisms $s_{c,m}=b_{c,m,x}: (c\rhd m)\lhd x\to c\rhd (m\lhd x)$. Any morphism  $\alpha\in \Hom_\mad(x,y)$ defines a $\mac$-module natural transformation $\nu=-\lhd \alpha: -\lhd x\Rightarrow -\lhd y$. This defines a functor $\mad\to \End_\mac(\mam)$.

\item If $x\in \Ob \mathcal Z(\mad)$ with half-braidings $\sigma_{d,x}: d\oo x\to x\oo d$,  the functor $F$ from 1.~becomes  a $(\mac,\mad)$-bimodule functor with $t_{m,d}= d_{m,d,x}^\inv\circ (1_m\lhd \sigma_{x,d}^\inv)\circ d_{m,x,d}: (m\lhd x)\lhd d\to (m\lhd d)\lhd x$.
For $\alpha\in \Hom_{\mathcal Z(\mad)}(x,y)$ the morphisms $\nu_m=1\lhd \alpha: m\lhd x\to m\lhd y$ define a $(\mac,\mad)$-bimodule natural transformation $\nu: -\lhd x\Rightarrow -\lhd y$. 
This defines a functor $\mathcal Z(\mad)\to \End_{(\mac,\mad)}(\mam)$.

\item Analogously, for  $x\in \Ob\mac$  $F=x\rhd -: \mam\to\mam$    with $t_{m,d}=b_{x,m,d}: (x\rhd m)\lhd d\to x\rhd (m\lhd d)$ is a $\mad$-right module functor. Any morphism  $\alpha\in \Hom_\mac(x,y)$  defines a $\mad$-right module natural transformation $\nu=\alpha\rhd -: x\rhd -\Rightarrow y\rhd -$. This defines a functor $\mac\to \End_{\mad^{rev}}(\mam)$.  
 
 
\item If  $x\in\Ob \mathcal Z(\mac)$ with half-braidings $\sigma_{c,x}: c\oo x\to x\oo c$, the functor $F$ from 3.~becomes a  $(\mac,\mad)$-bimodule functor with $s_{c,m}=c_{c,x,m}\circ (\sigma^\inv_{c,x}\rhd 1_m)\circ c_{x,c,m}^\inv: x\rhd (c\rhd m)\to c\rhd (x\rhd m)$. 
For any morphism $\alpha\in \Hom_{\mathcal Z(\mac)}(x,y)$ the morphisms $\nu_m=\alpha\rhd 1_m: x\rhd m\to y\rhd m$ define a $\mac$-module natural transformation $\nu: x\rhd-\Rightarrow y\rhd -$. This defines a functor $\mathcal Z(\mac)\to \mathrm{End}_{(\mac,\mad)}(\mam)$. 

\item For any $\mac$-module category $\mam$ and $m\in\Ob \mam$, the functor $F=-\rhd m:\mac\to\mam$ is a $\mac$-module functor with $s_{x,y}=c_{x,y,m}: (x\oo y)\rhd m\to x\rhd (y\rhd m)$. Any morphism $\alpha\in \Hom_\mam(m,m')$ defines a $\mac$-module natural transformation $\nu=-\rhd \alpha: -\rhd m\Rightarrow -\rhd m'$. 

If $\mam$ is a $(\mac,\mad)$-bimodule category, this defines a $(\mac,\mad)$-bimodule equivalence $\mam\to \Fun_\mac(\mac,\mam)$ with respect to the $(\mac,\mad)$-bimodule structure on $\Fun_\mac(\mac,\mam)$  given by $(c\rhd F)(x)=F(x\oo c)$ and $(F\lhd d)(x)=F(x)\lhd d$ for $c,x\in\Ob\mac$, $d\in\Ob\mad$.


\item For any $\mad$-right module category $\mam$ and $m\in\Ob \mam$, the functor $F=m\lhd -:\mad\to\mam$ is a $\mad$-right module functor with $t_{x,y}=d_{x,y,m}: (m\lhd x)\lhd y\to m\lhd (x\oo y)$. Any morphism $\alpha\in \Hom_\mam(m,m')$ defines a $\mac$-module natural transformation $\nu= \alpha\lhd -:  m\lhd - \Rightarrow  m'\lhd -$. 

If $\mam$ is a $(\mac,\mad)$-bimodule category, this defines a $(\mac,\mad)$-bimodule equivalence $\mam\to \Fun_{\mad^{rev}}(\mad,\mam)$ with respect to the $(\mac,\mad)$-bimodule structure on $\Fun_{\mad^{rev}}(\mad,\mam)$  given by $(c\rhd F)(x)=c\rhd F(x)$ and $(F\lhd d)(x)=F(d\oo x)$ for $c\in\Ob\mac$, $d,x\in\Ob\mad$.


\item If $\mathcal C,\mathcal D$ are pivotal fusion categories,  any $(\mac,\mad)$-bimodule functor $F: \mam\to\man$ defines a $(\mad,\mac)$-bimodule functor $F^\#:\mam^\#\to\man^\#$ with coherence isomorphisms  $s^{F^\#}_{d,m}=t^F_{m,d^*}$ and $t^{F^\#}_{m,c}=s^F_{c^*,m}$. 
 Any $(\mac,\mad)$-bimodule natural transformation $\nu: F\Rightarrow G$ induces a $(\mad,\mac)$-bimodule natural transformation $\nu^\#: G^\#\Rightarrow F^\#$ with  $\nu^\#_m=\nu_m$.

\item For any $(\mac,\mad)$-bimodule functor $F:\mam\to\man$, the morphisms $s_{c,m}: F(c\rhd m)\to c\rhd F(m)$ define a $\mad$-right module natural isomorphism $s_c: F(c\rhd -)\Rightarrow c\rhd F(-)$. Analogously, the morphisms $t_{m,d}: F(m)\lhd d\to F(m\lhd d)$ define a $\mac$-module natural transformation $t_d: F(-)\lhd d\Rightarrow F(-\lhd d)$. This follows  from the  hexagon identity \eqref{eq:hexa} for a bimodule functor and the  module functor structure  \eqref{eq:bimodcomp} for a composite functor.

\end{enumerate}
\end{example}

If $\mac$ is a finite multitensor category as a bimodule category over itself, then  all bimodule endofunctors of $\mac$ are naturally isomorphic to functors of the  form $F=c\oo -:\mac\to\mac$ with an object $c\in \mathcal Z(\mac)$, as in Example \ref{ex:modulefuncs}, 4.~and all bimodule natural transformations between them are of the form $\nu=f\oo -: c\oo -\Rightarrow c'\oo -$ with a morphism $f: c\to c'$ in $\mathcal Z(\mac)$. This identifies $\End_\mac(\mac)$ with the  centre $\mathcal Z(\mac)$. 


\begin{example}\label{ex:center} \cite[Prop.~7.13.8.]{EGNO} Let $\mac$ be a finite multitensor category, viewed as a $(\mac,\mac)$-bimodule category. 
Then  the monoidal category $\End_\mac(\mac)$ is canonically monoidally isomorphic to the centre $\mathcal Z(\mac)$.
\end{example}
