---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-006-22-boundary-slopes-and-homology-of-cable-spaces
section_title: "Boundary slopes and homology of cable spaces"
section_number: 2.2
pages: 6-9
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.996
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
A \emph{slope}  $s$ on  a torus $T$ is the isotopy class of a simple closed curve on $T$.
Let $\mathcal {S}(T)$ denote the set of {slopes}  of $T$.
The elements in  $\mathcal {S}(T)$  are represented by elements of
${\QQ}\cup \{ 1/0\}$.  With this in mind we will often refer to a slope by its corresponding numerical value.
A homology class in
$H_1(T,  \ZZ)$ is called \emph{primitive} if it is not a non-trivial integer multiple of another element in $H_1(T,  \ZZ)$.
There is a 2-1 correspondence between primitive  classes in $H_1(T,  \ZZ)$
and elements  in $\mathcal {S}(T)$, where $\alpha, \beta \in H_1(T,  \ZZ)$ give the same slope if and only iff $\alpha=
\pm \beta$.



Next we need the following lemma.


\begin{lemma} \label{glue} Consider  a cable knot complement $\M=\C\cup M_K$  as above.
Let $s\in \mathcal {S}(T_{-})$ be a slope on  $T_{-}$ of $\C$, corresponding to $a/b\in {\QQ}\cup \{ 1/0\}$.
Suppose that in $\C$ we have a properly embedded, connected, essential surface $F$ such that:
\begin{enumerate}
\item The boundary $\partial F$ intersects both of $T_{-}$ and $T_{+}$.

\item  Each component of $\partial F$ on $T_{-}$ has  slope $s$.

\item The total slope of $\partial F\cap T_{+}$ is a boundary slope
in $M_K$.
\end{enumerate}

Then $a/b$ is a boundary slope in $\M$.

\end{lemma}
\begin{proof}  
Suppose that the total slope of $\partial F\cap T_{+}$  corresponds to 
$c/d\in {\QQ}\cup \{ 1/0\}$.
Let $E$ be a essential surface in $M_K$ with  $\partial E$ having  total slope $c/d$.
By passing to the doubles if necessary, we may assume that $E$ and $F$ are orientable.
Let $x$ and $y$  denote the number of components of $\partial F$  and $\partial E$ on $T_{+}$, respectively.
In $\C$ consider a surface $F'$ that is  $y$ copies of  $F$ and in $M_K$ consider a surface $E'$ that is $x$ copies of
$E$. Each of $\partial E'$ and $\partial F'$ has $xy$ components on $T_{+}$.  After isotopy on $T_{+}$ we may assume that $\partial E'=\partial F'$. Now $S=E'\cup F'$ is a properly embedded surface in $\M$.
By assumption, each  component of $S \cut T_{+}$ is essential in the component of $\M \cut T_{+}$ it lies in. Thus  
by Lemma \ref{components}, $S$ is essential in $\M$.
\end{proof}



The following lemma  should be compared with
 \cite[Lemma 2.3]{KS}.

\begin{lemma} \label{bijection} Let $\C$ be a cable space with $\partial C= T_{-}\cup T_{+}$ as above. 
Let $\mathcal {S}_{-}$ and $\mathcal{S}_{+}$ denote the set of slopes on $T_{-}$ and $T_{+}$ respectively.
There is  a bijection
$$\phi: \mathcal {S}_{-}\longrightarrow \mathcal {S}_{+},$$
such that for every $s\in \mathcal {S}_{-}$
there is a connected, essential  properly embedded surface $F\subset \C$, intersecting both components of $\partial \C$,
and such that each component $\partial F\cap T_{-}$ has slope $s$ while each component of $\partial F\cap T_{+}$ has slope $\phi(s)$.

\end{lemma}
\begin{proof}To simplify our notation, throughout this proof, we will use $X:=\C$.
Identify $H_1(\partial X ; \QQ)$  with $H_1(T_{-};  \QQ)\oplus H_1(T_{+};  \QQ)$. 

We claim that the maps 
$i_{\pm}  : H_1(T_{\pm};  \QQ) \longrightarrow H_1(X; \QQ)$, induced by the inclusions of $T_{\pm}$ in $X$ are isomorphisms.
To see that $i_{-}$ is an isomorphism consider the solid torus $X\cup n(T_{p,q})$, and apply the
Mayer--Vietoris long exact sequence to this decomposition. To see that $i_{+}$ is an isomorphism decompose $X$ into a fibered solid torus and an $I$-bundle
$T_{+}\times I$ along a vertical annulus and again apply the Mayer--Vietoris long exact sequence.

The fact that $i_{\pm}$ are isomorphisms implies  the following: Given a primitive class $\alpha_{-} \in H_1(T_{-};  \ZZ) \subset H_1(T_{-}; \QQ)$
there is a unique primitive class $\alpha_{+} \in H_1(T_{+};  \ZZ) \subset H_1(T_{+}; \QQ)$
so that
\begin{equation}
\label{eq-r}
\alpha_{+} = r \ i_{+}^{-1}\circ i_{-}(\alpha_{-}), \  {\text {\rm for \ some }} \   r\in \QQ.
\end{equation}

As discussed above, a  slope $s\in \mathcal {S}_{\pm}$  determines  a primitive class $\alpha_{\pm} \in H_1(T_{\pm};  \ZZ)$ 
up to sign. 
Given  $s\in \mathcal {S}_{-}$, determining a primitive element $\alpha_{-} \in H_1(T_{-},  \ZZ)$  up to sign, 
define $\phi(s)$ to be the slope  in $S_{+}$ that describes the class $\alpha_{+} \in  H_1(T_{+},  \ZZ)$ defined in equation \eqref{eq-r}.
This clearly defines a bijection.

By above discussion, there are relatively prime integers $m,n $  such that 
$$m i_{-}(\alpha_{-})+ n i_{+}(\alpha_{+})=0.$$ Thus the element
$m\alpha_{-} + n\alpha_{+}$ is in the kernel of the map
$i_{-}\oplus i_{+}: H_1(\partial X;  \ZZ) \longrightarrow H_1( X; \ZZ) $. Looking at the homology  long exact sequence for the pair $(X, \partial X)$,
we conclude that there is a class $A \in H_1(X, \partial X; \ZZ)$ such that
$\partial (A)=m\alpha_{-} + n\alpha_{+}$ under the boundary map
$\partial: H_1(X, \partial X; \ZZ) \longrightarrow H_1(\partial X; \ZZ)$.
Now 3-manifold theory assures that there is a 2-sided, embedded, essential  surface $S$ that represents $A$ \cite[Lemma 6.6]{hempel}.
That is $[S]=A$.
By construction, each component of $\partial S\cap T_{-}$ has slope $s$ while each component of $\partial S\cap T_{+}$ has slope $\phi(s)$.

Now $S$ may not be connected. However since $S$ represents $A$, we have $\partial(A)= m\alpha_{-} + n\alpha_{+}\neq 0$. There must be a component $F\subset S$ such that $\partial([F])\neq 0$. We claim that $F$ must intersect both components of $\partial X$.
For, suppose that it doesn't intersect one component of $\partial X$; say $F\cap T_{+}=\emptyset$. Then the class
$\partial([F])\neq 0$ would be a non-zero multiple of $\alpha_{-} \in H_1(\partial X;  \ZZ)$. But this is impossible, since
$i_{-}(\alpha_{-})$ has infinite order in $H_1( X;  \ZZ)$.
Thus $F\cap T_{\pm}\neq \emptyset$. To finish the proof of the lemma, note that since $F\subset S$ and $S$ is essential, each component $\partial F\cap T_{-}$ has slope $s$ while each component of $\partial F\cap T_{+}$ has slope $\phi(s)$.
\end{proof}






\subsection{The proof of Theorem \ref{main:bs}.} We are now ready to  prove Theorem \ref{main:bs}. For part (a) let $K$ be a non-trivial knot and let  $(p, q)$ coprime  integers.
 Suppose that  $a/b$ is a boundary slope of $K$.
Let $\K$ be the cable knot
of $K$. As above we will consider the complement $\M$ obtained by gluing a cable space $\C$  to the complement $M_K$.
We must show that there is an essential surface $S$ in $\M$ such that the total slope of $S\cap \partial \M$ is $q^2a/b$.


On the boundary component $T_{-}=\partial M_{\K}$  consider a pair  $(\mu,  \lambda)$ of meridian and canonical longitude
whose homology classes generate $H_1(T_{-}; \ZZ)$. Let  
$r := \gcd(aq^2, b)$ and let
$x= a q^2 /r$ and $y=b/r$.
Consider
a simple closed curve $\gamma$ whose numerical slope is $x/y$. That is in $H_1(T_{-}; \ZZ)$ we have
$$[\gamma]= x\mu+ y\lambda.$$

 By Lemma \ref{bijection}, applied for  $s=x/y$ we have  a slope $\phi(s)$ 
on the other component  $T_{+}$ of $\C$ such that the following is true: There is an essential, connected,  properly embedded surface $F\subset \C$, with  $\partial F$ intersecting both components of $\partial \C$,
and such that each component $\partial F\cap T_{-}$ has slope $s$ while each component of $\partial F\cap T_{+}$ has slope $\phi(s)$.

Since $\C$ is a Seifert fibered space, up to isotopy,  essential surfaces are either vertical or horizontal with respect to the Seifert fibration \cite{Ha}. Since the base space of $\C$ is an annulus, the only vertical surfaces in $\C$ are annuli.
In fact, essential surfaces in cable spaces are classified by Gordon and Litherland in \cite[Lemma 3.1]{GL}. From that lemma and its proof, it follows that if $F$ is a vertical annulus in $\C$, then every component of $\partial F\cap T_{-}$  has slope $pq$, while every component of 
$\partial F\cap T_{+}$ has slope $p/q$.  In particular, we have $a/b=p/q$ and our hypothesis 
implies that for this to happen  $p/q$ must be a boundary slope of $K$. On the other hand $x/y=pq$ which, by Lemma \ref{cannulus},
is always a boundary slope of $\M$. Thus the desired conclusion holds in this case.



Now suppose that the surface $F$ is horizontal with respect to the Seifert fibration of $\C$.
On $T_{-}$ a regular fiber of the fibration can be identified with the knot $H:=\K$.
The only singular fiber of the fibration  (that has multiplicity $\abs{q}$) may be identified with the knot $K$ on $T_{+}$. If $N$ is the number of times that $F$ intersects the regular fibers of $\C$, then since the base of the fibration is an annulus we have
$$0-\chi(F)/N= 1-1/\abs{q}.$$
It follows that  $\chi(F)=n' (1-\abs{q})$, where
 $N=n'q$. 
Since the intersection number of $\mu$ and $H$ is $1$ we conclude that on $\partial T_{-}$,  the meridian curve $\mu$ is a cross section of the fibration and in $H_1(\partial \M)$ we have
$[\gamma]=nq  \mu +mH$, where  $n=n'/r, m\in \ZZ$ and we have $(nq, m)=1$.
On the other hand we must have  $H= pq \mu + \lambda$.
Hence we obtain that each component of   $$[\partial F]=r(nq +mq) \mu +rm\lambda, \ \ \  {\rm thus} \ \ \  s=x/y= (nq +mpq)/m.$$

In $\C$ we have a horizontal planar surface that intersects $T_{+}$ in a single meridian, call it $\mu'$,  and it intersects
$T_{-}$ in $q$ copies of $\mu$. This surface may be taken to be the image of a meridian disk of a neighborhood of $K$ in $\C$.
By choosing appropriate orientations of $\mu, \mu'$, and by the proof of Lemma \ref{bijection},  we may assume that $\phi(\mu)=\mu'$ and that in $H_1(\C ; \ZZ)$ we have $\mu'=q m$.


In $H_1(T_{+}; \ZZ)$,  the fiber $H$ corresponds to the slope $p/q$
and each component of  $T_{+}\cap \partial F$ has the form
$n  \mu' + mH$. Thus,  
as also stated in \cite[Lemma 3.1]{GL}, $T_{+}\cap \partial F$ 
 has total slope $(n+mp)/(mq)$. The number of components
$T_{+}\cap \partial F$ is $t= \gcd(n+mp, mq)$. Since in $\QQ$ we have that 
 $(n+mp)/(mq)=a/b$ we may take $a':=a/w=n+mp/t$ and $b':=b/w=mq/t$, where $w=\gcd(a, b)$.
Thus we may assume that  $\phi(s)=a'/b'$. 
By assumption $a/b$  is a boundary slope in $M_K$. Thus, Lemma \ref{glue} applies
to conclude that $s=q^2a/b$ is a boundary slope in $\M$. This finishes the proof of part (a) of
 Theorem \ref{main:bs}.
 
For a non-trivial knot $K$, part (b) follows at once from part (a).
To finish the proof of part (b) assume that $K$ is the trivial knot and let  $(p, q)$ coprime  integers.
Now $\K$ is the $(p, q)$ torus knot. The only boundary slope of $K$ is  $a/b=0/1$ and the boundary slopes of
$\K$ are $0$ and $pq$. Thus $q^2 bs_K \cup \{pq\} =\{0, pq \}= bs_{K_{p,q}}$. \qed
\medskip

We close the section with the following corollary that will be useful to us in subsequent sections.

\begin{corollary}\label{integers} Let $\M=\C\cup M_K$ be the complement of a cable knot, where $\abs{q}>1$.
Let $F\subset \C$ be a properly embedded essential surface, that is not an annulus, and such that each   component of 
 $\partial F\cap T_{+}$  has integral slope $a$. 
Suppose   that there is a connected essential surface
$S'\subset M_K$ such that each component of $\partial S'$ has slope $a$. Then the followings hold.
\begin{enumerate}
\item 
 $\partial F\cap T_{+}$  has $\abs{q}$ components and  $\partial F\cap T_{-}$ has a single component
 of slope $q^2a\in \ZZ$.

\item There is a connected essential surface $S\subset \M$, such that each component of $\partial S$ has slope
$q^2a$ and 
$$\chi(S)=    \abs{q} \chi(S') + \abs{ \partial S'}(1-\abs{q})\abs{p-aq},$$
\noindent where $\abs{ \partial S'}$ denotes the number of boundary components of $S'$.
Furthermore, we have $\abs{ \partial S}= \abs{ \partial S'}$.

\end{enumerate}

\end{corollary}
\begin{proof} Let $F$ be as in the statement above.
By the proof of Theorem \ref{main:bs}, since $F$ is not an annulus, $ F$ may be isotopied to be horizontal with respect to the Seifert fibration of $\C$.
Furthermore, $\partial F\cap T_{+}$
has total  slope  $(n+mp)/(mq)$, while 
$\partial F\cap T_{-}$ has total slope  $ (nq +mpq)/m$,
for some coprime  integers $m,n$.
The number of components of $\partial F\cap T_{+}$ is $t= \gcd(n+mp, mq)$,
and each has slope $b/c$ where $b=(n+mp)/t$ and $c=mq/t$.
Since  $b/c\in \ZZ$ and $\gcd(m,n)=1$, it follows that $m=\pm1$ and $t=\abs{q}$.
Hence 
 $n=m(qa-p)$, where we will have $m=1$ or $m=-1$ according to whether $qa\geq p$
or $qa\leq p$. Furthermore $n>0$, $\chi(F)=n(1-\abs{q})$. 
The rest of the claims  in part (1) follow.

Now we prove part (2): By the proof of Theorem \ref{main:bs}, an essential  surface $S$ realizing the boundary slope $q^2a$ for $\K$ 
is as in the proof of Lemma \ref{glue}. Since   $\partial F\cap T_{+}$  has $\abs{q}$ components, $S$ is constructed by 
gluing  $\abs{q}$ copies of $S'$ with $ \abs{ \partial S'}$ copies of $F$. Hence we have
$$\chi(S)=\chi(M_K\cap S)+\chi(\C \cap S)=\abs{q}  \chi(S')+\abs{\partial S'} \, \abs{aq-p} (1- \abs{q} ).$$
The last equation follows from the fact that
$\chi(\C \cap S)=\abs{\partial S'}  \chi(F)$ and the above discussion on
  $\chi(F)$.
\end{proof}
