---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-018-71-admissible-pair
section_title: "Admissible pair"
section_number: 7.1
pages: 45-54
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.957
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
In this section, we assume that \emph{$R$ is a symmetric KLR algebra
over a base field $\coro$}.

From now on, we focus on the case when $\shc$ is a full subcategory of $R \gmod$
 stable under taking convolution products, subquotients, extensions
and grading shift.
In particular, we have
\eqn
\shc = \soplus_{\beta \in \rootl^-} \shc_\beta, \quad
\text{where} \ \shc_\beta \seteq\shc\cap R(-\beta) \gmod,
\eneqn
and we have the grading shift functor $q$ on $\shc$.
Hence we have
$$K(\shc_\beta)\subset\Um_\beta,$$
and $K(\shc)$ has a $\Z[q^{\pm1}]$-basis consisting of
the isomorphism classes of self-dual simple modules.


\begin{definition} \label{def:admissible}
A pair $(\{M_i\}_{i\in\K}, \widetilde B)$ is called \emph{admissible} if
\bnum
\item  $\{M_i\}_{i\in\K}$ is a family of real simple  self-dual  objects of $\shc$ which commute with each other,
\item $\widetilde B$ is an integer-valued $\K \times\Kex$-matrix with
skew-symmetric principal part,
\item
 for each $k\in\Kex$, there exists a  self-dual  simple object $M'_k$ of $\shc$
 such that
 there is an exact sequence in $\shc$
 \eq
&&0 \to q \sodot_{b_{ik} >0} M_i^{\snconv b_{ik}} \to q^{\tLa(M_k,M_k')} M_k \conv M_k' \to
 \sodot_{b_{ik} <0} M_i^{\snconv (-b_{ik})} \to 0,
\label{eq:ses graded mutation KLR}
 \eneq
and
$M_k'$ commutes with $M_i$  for any  $i \neq k$.
  \end{enumerate}
\end{definition}


Note that $M'_k$ is uniquely determined by $k$ and
$(\{M_i\}_{i\in\K}, \widetilde B)$. Indeed, it follows from
$q^{\tLa(M_k,M_k')}M_k\hconv M'_k\simeq\sodot_{b_{ik} <0} M_i^{\snconv(-b_{ik})}$ and
\cite[Corollary 3.7]{KKKO14}.
Note also that if there is an epimorphism $q^mM_k\conv M'_k\epito
\sodot_{b_{ik} <0} M_i^{\snconv(-b_{ik})}$ for some $m\in\Z$, then $m$ should coincide with $\tL(M_k,M'_k)$ by Lemma~\ref{lem:selfdual} and Lemma~\ref{lem:multipro}.

\smallskip
For an admissible pair  $(\{M_i\}_{i\in\K}, \widetilde B)$, let
$\La=(\La_{ij})_{i,j\in\K}$
be the skew-symmetric matrix
given by $\La_{ij}=\Lambda(M_i,M_j)$.
and let $D=\{d_i\}_{i\in\K}$ be the family of elements of $\rootl^-$ given by
$d_i=\wt(M_i)$.

\smallskip
Now we can simplify  the conditions in Definition \ref{def:quantum monoidal seed} and
Definition \ref{def:monoidal mutation} as follows.

\begin{prop} \label{prop:condition simplified}
Let $(\{M_i\}_{i\in\K},\widetilde B)$ be an admissible pair in $\shc$,
and let $M'_k$ $(k\in\Kex)$ be as in {\rm Definition~\ref{def:admissible}}.
    Then we have the following properties.
  \bna
      \item The quadruple $\seed\seteq(\{M_i\}_{i\in\K}, -\La,\widetilde B,D)$
    is a quantum monoidal seed in $\shc$.\label{item:1}
    \item The self-dual simple object $M_k'$ is real for every $k\in\Kex$.
\label{item:2}
    \item The quantum monoidal seed $\seed$ admits a mutation in each direction $k\in\Kex$.\label{item:3}
\item $M_k$ and $M'_k$ are simply-linked for any $k\in\Kex$
\ro i.e., $\de(M_k,M'_k)=1$\rf.\label{item:sl}
\item For any $j\in\K$ and $k\in\Kex$, we have
\eq&&
\ba{l}\La(M_j,M'_k)=-\La(M_j,M_k)-\sum_{b_{ik}<0}\La(M_j,M_i)b_{ik},\\[1ex]
\La(M'_k,M_j)=-\La(M_k,M_j)+\sum_{b_{ik}>0}\La(M_i,M_j)b_{ik}.
\ea\label{eq:Larel}
\eneq\label{item:Larel}
  \end{enumerate}
\end{prop}
\Proof
\eqref{item:sl} follows from the exact sequence
\eqref{eq:ses graded mutation KLR} and Lemma \ref{lem:crde}.

\medskip\noi
\eqref{item:2} follows from the exact sequence
\eqref{eq:ses graded mutation KLR}
by applying Corollary \ref{cor:real} to the case
$$M=M_k, \ N=M'_k, \ X= q  \sodot_{b_{ik} > 0} M_i^{\snconv b_{ik}}
\ \text{and} \  Y= \sodot_{b_{ik} < 0} M_i^{\snconv(-b_{ik})}. $$


\medskip
\noi
\eqref{item:Larel} follows from
\begin{align*}
\La(M_j,M_k)+\La(M_j,M'_k)&=\La(M_j,M_k\hconv M'_k)
=\La\bl M_j,\sodot_{b_{ik} <0} M_i^{\snconv(-b_{ik})}\br\\
&=\sum_{b_{ik}<0}\La(M_j,M_i)(-b_{ik})
\end{align*}
and
\begin{align*}
\La(M_k,M_j)+\La(M'_k,M_j)&=\La(M'_k\hconv M_k,M_j)
=\La\bl\sodot_{b_{ik} >0} M_i^{\snconv b_{ik}}, M_j\br\\
&=\sum_{b_{ik}>0}\La(M_i,M_j)b_{ik}.
\end{align*}

\medskip 
Let us show \eqref{item:1}.
 The conditions (i)--(v) in Definition \ref{def:quantum monoidal seed} are satisfied by the construction.
 The condition (vi) follows from Proposition \ref{prop:real simple}
and the fact that $M_i$ is real simple
for every $i\in\K$.
 The condition (viii) is nothing but Lemma \ref{lem:tLa even}.
 The condition (ix) follows easily from the fact that
the weights of the first and the last terms in the exact sequence \eqref{eq:ses graded mutation KLR} coincide.


Let us show  the condition (vii)  in Definition \ref{def:quantum monoidal seed}.
By \eqref{eq:Larel} and \eqref{item:sl} of this proposition, we have
\begin{align*}
2\delta_{jk}=2\de(M_j,M'_k)
&=-2\de(M_j,M_k)-\sum_{b_{ik}<0}\La(M_j,M_i)b_{ik}
+\sum_{b_{ik}>0}\La(M_i,M_j)b_{ik}\\
&=-\sum_{b_{ik}<0}\La(M_j,M_i)b_{ik}-\sum_{b_{ik}>0}\La(M_j,M_i)b_{ik}
=-\sum_{i\in\K}\La(M_j,M_i)b_{ik}
\end{align*}
for $k\in\Kex$ and $j\in\K$.
Thus we have shown that $\seed$ is a quantum monoidal seed
in $\shc$.


\medskip 
Let us show \eqref{item:3}. Let $k\in\Kex$. The exact sequence
\eqref{eq:ses graded mutation1}
follows from  \eqref{eq:ses graded mutation KLR}
and the equality
\eq
\tL(M_k,M'_k)=\dfrac{1}{2}\bl(\wt(M_k,M'_k)
-\sum_{b_{ik}<0}\La(M_k,M_i)b_{ik}\br=m_k,
\eneq
which is an immediate consequence of \eqref{eq:Larel}.

 Similarly, taking the dual of
the exact sequence \eqref{eq:ses graded mutation KLR},
we obtain an exact sequence
 \eqn
&&0 \to  \sodot_{b_{ik} <0} M_i^{\snconv (-b_{ik})}  \to q^{-\tLa(M_k,M_k')+(\wt M_k, \wt M_k')} M_k' \conv M_k  \to q^{-1}\sodot_{b_{ik} >0} M_i^{\snconv b_{ik}}
 \to 0,
 \eneqn
which gives the exact sequence \eqref{eq:ses graded mutation2}.
\smallskip

It remains to prove that $\mu_k(\seed)\seteq(\{M_i\}_{i\neq k}\cup\{M_k'\},\mu_k(-\La),
\mu_k(\widetilde B), \mu_k(D))$ is
a quantum monoidal seed in $\shc$ for any $k\in\Kex$.

We see easily that $\mu_k(\seed)$
satisfies the conditions (i)--(iv) and (vii)--(ix) in Definition~\ref{def:quantum monoidal seed}.

For  the condition (v), it is enough to show that
for $i,j\in\K$ we have
\eqn \mu_k(-\La)_{ij} = -\Lambda(\mu_k(M)_i,\mu_k(M)_j),
\eneqn
where $\mu_k(M)_i = M_i$ for $i\neq k$ and $\mu_k(M)_k=M_k'$.
In the case $i \neq k$ and $j \neq k$, we have
\eqn \mu_{k}(-\La)_{ij}=-\Lambda(M_i,M_j)=-\Lambda(\mu_k(M_i),\mu_k(M_j)).
\eneqn
The other cases follow from \eqref{eq:Larel}.

 The condition (vi) in Definition~\ref{def:quantum monoidal seed}
for $\mu_k(\seed)$ follows from Proposition \ref{prop:real simple} and the fact that $\{\mu_k(M)_i\}_{i\in\K}$ is a commuting family of real simple modules.
\QED

Now we are ready to give  one of our main theorems.
\Th\label{th:main}
Let  $(\{M_i\}_{i\in \K},\widetilde B)$ be an admissible pair in $\shc$
and set $$\seed=(\{M_i\}_{i\in\K}, -\La,\widetilde B,D)$$
as in {\rm Proposition~\ref{prop:condition simplified}}.
We set
$[\seed]\seteq(\{q^{-\frac{1}{4}(\wt(M_i), \wt(M_i))}[M_i]\}_{i\in\K}, -\La,\widetilde B,D)$.
We assume further  that
\eq
&&\hs{1ex}\parbox[t]{79ex}{
 The $\Q(q^{1/2})$-algebra $\Q(q^{1/2})\tens\limits_{\Z[q^{\pm1}]}K(\shc)$
is isomorphic to $\Q(q^{1/2})\tens\limits_{\Z[q^{\pm1}]}\mathscr A_{q^{1/2}}([\seed])$.
}\label{eq:Cluster}
\eneq
Then, for each $x\in\Kex$, the pair
$\bl\{\mu_x(M)_i\}_{i\in\K},\mu_x(\widetilde B)\br$
 is admissible in $\shc$.
\enth
\Proof In Proposition ~\ref{prop:condition simplified} (\ref{item:2}), we have already  shown that
the condition (i) in Definition~\ref{def:admissible} holds for
$(\{\mu_x(M)_i\}_{i\in\K},\mu_x(\widetilde B))$.
The condition (ii) is clear from the definition.
Let us show (iii).
Set $N_i\seteq\mu_x(M)_i$ and
$b_{ij}' \seteq\mu_x(\widetilde B)_{ij}$ for $i\in \K$ and $j\in \Kex$.
It is enough to show that, for any $y\in\Kex$,
there exists a self-dual simple module $M_y'' \in \shc$ such that
there is a short exact sequence
\eq
\xymatrix{
0 \ar[r] &  q \sodot_{b'_{iy} > 0} N_i^{\snconv b'_{iy}} \ar[r]
&q^{\tLa(N_y,M_y'')}  N_y \conv  M_y'' \ar[r]
& \sodot_{b'_{iy} <0} N_i^{\snconv (-b'_{iy})}   \ar[r] & 0
}\label{eq:seqdes}
\eneq
and
$$\de(N_i,M_y'')=0 \quad \text{for $i \neq y$.}$$


If $x=y$, then $b'_{iy}=-b_{ix}$ and hence $M''_y=M_x$ satisfies the desired condition.

Assume that $x\not=y$ and $b_{xy}=0$. Then $b'_{iy} = b_{iy}$ for any $i$
and $N_i=M_i$ for any $i\not=x$.
Hence  $M_y''=\mu_y(M)_y$ satisfies the desired condition.

\medskip
We will show the assertion in the case $b_{xy} > 0$.
We omit the proof of the case $b_{xy} <0$ because it
can be shown in a similar way.


Recall that we have
\eq \label{eq:bxy>0 mutation}
b_{iy}'=\begin{cases}
b_{iy}+b_{ix}b_{xy} & \text{if } b_{ix} >0, \\
b_{iy} & \text{if } b_{ix} \le 0
\end{cases}
\eneq
for $i  \in \K$ different from $x$ and $y$.

Set
\eqn
&&M_x'\seteq\mu_x(M)_x, \hs{3ex} M_y'\seteq\mu_y(M)_y, \\
&&C\seteq\sodot_{b_{ix} >0} M_i^{\snconv b_{ix}}, \quad  S\seteq\sodot_{b_{ix} <0, \ i\neq y} M_i^{\snconv -b_{ix}}, \\
&&P\seteq\sodot_{b_{iy} >0, i\neq x} M_i^{\snconv b_{iy}}, \quad  Q:=\sodot_{b_{iy}' <0, \ i\neq x} M_i^{\snconv-b_{iy}'}, \\
&&A\seteq\sodot_{b_{iy}' \le 0, \ b_{ix} >0} M_i^{\snconv b_{ix}b_{xy}} \nconv \sodot_{\substack{b_{iy} <0,\; b_{iy}' >0,\;b_{ix} >0}} M_i^{\snconv -b_{iy}}
 \\
&&\hs{3ex}\simeq
\sodot_{\substack{b_{iy} <0,\; b_{ix} >0}}
M_i^{\snconv \min(b_{ix}b_{xy},-b_{iy})},\\
&&B\seteq\sodot_{ b_{iy} \ge 0,  \ b_{ix} >0} M_i^{\snconv b_{ix}b_{xy}} \nconv \sodot_{\substack{b_{iy}' >0, \; b_{iy} <0,\;b_{ix} >0}} M_i^{\snconv b_{iy}'}.
 \eneqn

Then    using \eqref{eq:bxy>0 mutation} repeatedly,
we have
\begin{align*}
Q \nconv A \simeq \sodot_{b_{iy} < 0} M_i^{\snconv -b_{iy}}, \quad
A \nconv B \simeq C^{\snconv b_{xy}}, \quad \text{and}  \quad
 B\nconv P \simeq \nconv \sodot_{ b_{iy}' > 0} M_i^{\snconv b_{iy}'}.
\end{align*}
Set
 \eqn
&&L\seteq(M_x')^{\snconv b_{xy}},   \quad 
V\seteq M_x^{\snconv b_{xy}}
\eneqn
 and set
\eqn
X \seteq \sodot_{b_{iy} >0} M_i^{\snconv b_{iy}}\simeq
M_x^{\snconv b_{xy}} \nconv P =V \nconv P,
 \quad Y\seteq \sodot_{b_{iy} <0} M_i^{\snconv-b_{iy}}\simeq Q \nconv A.
\eneqn

Then \eqref{eq:seqdes}  is read as
\eq
\xymatrix{
0 \ar[r] &  q (B \nconv P)\ar[r]  &q^{\tL(M_y,M''_y)}M_y \conv M''_y \ar[r] &
L  \nconv Q\ar[r] & 0.
}\label{eq:seqdes'}
\eneq

Note that we have
\eq
&&0 \to q C  \to q^{\tLa(M_x,M_x')}M_x \conv M_x' \to  M_y^{\snconv b_{xy}} \nconv S \to 0,  \\
&&0 \to q X \to  q^{\tLa(M_y,M_y')}M_y \conv M_y' \to  Y \to 0. \label{eq:sesMy}
\eneq

Taking the convolution products of $L=(M_x')^{\snconv b_{xy}}$  and \eqref{eq:sesMy}, we obtain

\eqn
&&
\xymatrix@R=.5ex{0 \ar[r]& qL \conv X  \ar[r]&
 q^{\tLa(M_y,M_y')} L \conv (M_y \conv M_y')\ar[r]& L \conv Y \ar[r]& 0, \\
0\ar[r]& qX \conv L \ar[r]&
q^{\tLa(M_y,M_y')} (M_y \conv M_y') \conv L \ar[r]&  Y\conv L \ar[r]& 0.}
\eneqn


Since $L$ commutes with  $M_y$,
we have
\eqn
&&\Lambda(L, Y)=\Lambda(L, M_y \hconv M_y') \\
 &&=\Lambda(L, M_y) +\Lambda(L, M_y') = \Lambda(L,M_y \conv M_y' ).
\eneqn


On the other hand, we have
\eqn
&&\Lambda(M_x',X) - \Lambda(M_x',Y)  \\
&&=\Lambda(M_x', \sodot_{b_{iy} >0} M_i^{\snconv b_{iy}})-\Lambda(M_x',\sodot_{b_{iy} <0} M_i^{\snconv -b_{iy}})  \\
&&=\sum_{b_{iy} >0} \Lambda(M_x',M_i)b_{iy} -\sum_{b_{iy} <0} \Lambda(M_x',M_i)(-b_{iy})  \\
&&=\sum_{i\in\K} \Lambda(M_x', M_i)b_{iy}
=\sum_{i \neq x} \Lambda(M_x',M_i)b_{iy} + \Lambda(M_x',M_x)b_{xy} \\
&&=\sum_{i \neq x} \Lambda(M_x', M_i)(b_{iy}' -\delta(b_{ix} >0)b_{ix} b_{xy}) + \Lambda(M_x',M_x)b_{xy} \\
&&=\sum_{i \neq x} \Lambda(M_x', M_i) b_{iy}'
-\sum_{b_{ix} >0} \Lambda(M_x', M_i)b_{ix}b_{xy} + \Lambda(M_x',M_x)b_{xy} \\
&&\mathop=\limits_{\mathrm(a)}0-\Lambda(M_x', \sodot_{b_{ix} >0} M_i^{\snconv b_{ix}})b_{xy} + \Lambda(M_x',M_x)b_{xy} \\
&&=\bl-\Lambda(M_x',\sodot_{b_{ix} >0} M_i^{\snconv b_{ix}} ) + \Lambda(M_x',M_x) \br b_{xy} \\
&&=(-\Lambda(M_x', M_x' \hconv M_x) + \Lambda(M_x',M_x) )b_{xy} \\
&&=(-\Lambda(M_x', M_x')-\Lambda(M_x', M_x) + \Lambda(M_x',M_x) )b_{xy}=0.
\eneqn
Note that we used the compatibility of the pair
$\bl\bl-\Lambda(\mu_x(M_i),\mu_x(M_j))\br_{i,j\in\K}, \, \mu_x(\widetilde B)\br$
when we derive the equality (a).

Since $L=(M'_x)^{\snconv b_{xy}}$, the equality $\La(M'_x,X)=\La(M'_x,Y)$ implies
\eqn
&& \Lambda(L,X)
=\Lambda(L,Y)=\La(L, M_y \conv M_y'). \label{eq:LaLX=LaLY}
\eneqn
Hence  the following  diagram is commutative by Proposition \ref{prop:inequalities} (i):
\eqn \label{eq:commutative ses}
&&\ba{c}\xymatrix{
0 \ar[r] & q L \conv X \ar[r] \ar[d]^{\rmat{L,X}} &  q^{\tLa(M_y,M_y')} L \conv (M_y \conv M_y')
 \ar[d]^{\rmat{L,M_y \circ M_y'}} \ar[r] &  L \conv Y \ar[r] \ar[d]_{\rmat{L,Y}} ^{\bwr}&0\\
0 \ar[r] & q^{d+1} X \conv L \ar[r]  & q^{d+\tLa(M_y,M_y')} (M_y \conv M_y') \conv L \ar[r] & q^{d}\, Y \conv L \ar[r] & 0,
}\ea
\eneqn
where $d=-\Lambda(L,X)=-\Lambda(L,M_y \conv M_y')=-\Lambda(L,Y)$.
Note that  since $L=(M_x')^{\snconv b_{xy}}$ commutes with $Q$ and $A$, $\rmat{L,Y}$ is an isomorphism.  Hence
we have
$$\Im(\rmat{L,Y}) \simeq L \conv Y.$$
 Therefore we obtain  an exact sequence
\eq
\xymatrix{0\ar[r]&\Im(\rmat{L,X})\ar[r]&\Im(\rmat{L, M_y\circ M'_y})\ar[r]
&L\circ Y\ar[r]&0.}\label{eq:exIm}
\eneq

On the other hand, $\rmat{L, M_y \circ M_y'}$ decomposes
(up to a grading shift) by Lemma \ref{lem:composition} as follows:
\eqn
\xymatrix@C=6em{
L \conv M_y \conv M_y'  \ar[r]^\sim_{\rmat{L,M_y} \circ M_y'}
\ar@/^2pc/ [rr]^{\rmat{L, M_y \circ M_y'}}&
 M_y \conv L \conv M_y'  \ar[r]_{M_y \circ \rmat{L,M_y'}} &
 M_y  \conv M_y' \conv L.
 }
 \eneqn
Since $L=(M_x')^{\snconv b_{xy}}$ commutes with $M_y$,
the homomorphisms $\rmat{L,M_y} \conv M_y'$ is an isomorphism and hence we have
\eqn
\Im
 (\rmat{L, M_y \circ M_y'}) \simeq  M_y \conv (L\hconv M'_y)
\quad\text{up to a grading shift.}
 \eneqn


Similarly, $\rmat{L, X}$ decomposes
(up to a grading shift) as follows:
\eqn
\xymatrix@C=6em{
L \conv V \conv P  \ar[r]_{\rmat{L,V} \circ P}
\ar@/^1.5pc/ [rr]^{\rmat{L,X}}&
 V \conv L \conv P  \ar[r]_{ V\circ \rmat{L,P}}^\sim &
V \conv P  \conv L.
 }
 \eneqn

Since $L$ commutes with $P$,
the  homomorphism  $V \conv \rmat{L,P} $ is an isomorphism and hence we have
  \eqn
\Im
 (\rmat{L,X})
  \simeq (L \hconv V) \conv P
\simeq \bl(M_x')^{\conv b_{xy}} \hconv M_x^{\conv b_{xy}}\br \conv P
\quad\text{up to a grading shift.}
 \eneqn
On the other hand,
Lemma~\ref{lem:MN} implies that
\eqn
(M_x')^{\conv b_{xy}} \hconv M_x^{\conv b_{xy}}
\simeq (M_x' \hconv M_x)^{\conv b_{xy}}
\simeq  C^{\conv b_{xy}}
\simeq B \nconv A
\eneqn
and hence we obtain
  \eqn
\Im
 (\rmat{L,X})
\simeq (B \nconv P)  \nconv A\quad\text{up to a grading shift.}
\eneqn

Thus the exact sequence \eqref{eq:exIm} becomes the exact sequence in $\shc$:
\eq
&&\xymatrix{
0 \ar[r] &  q^m (B \nconv P) \nconv A \ar[r]  &q^nM_y \conv (L\hconv M_y') \ar[r] & (L  \nconv Q) \nconv A \ar[r] & 0
}\label{eq:exML}
\eneq
for some $m,n\in\Z$.
Since $(L  \nconv Q) \nconv A$ is self-dual, $n=\tL(M_y,L\hconv M_y')$.
On the other hand, by Proposition \ref{prop:Lambda decomp} (i) and  Proposition \ref{prop:condition simplified} (\ref{item:sl}), we have
\eqn
\de(M_y,L \hconv M_y') \le \de(M_y, L) + \de(M_y, M_y') =1.
\eneqn
By the exact sequence \eqref{eq:exML},
$M_y \conv (L\hconv M_y')$ is not simple and we conclude
$$\de(M_y,L \hconv M_y')=1.$$
Then Lemma~\ref{lem:crde} implies that $m=1$.
Thus we obtain an exact sequence in $\shc$:
\eq
&&\xymatrix@C=3ex{
0 \ar[r] &  q (B \nconv P) \nconv A \ar[r]  &q^{\tL(M_y,L\shconv M_y')}M_y \conv (L\hconv M_y') \ar[r] & (L  \nconv Q) \nconv A \ar[r] & 0.
}\label{eq:exML1}
\eneq

Now we shall rewrite \eqref{eq:exML1} by using $\scbul\conv A$ instead of
$\scbul\nconv A$.
We have \eqn
&&\tLa(B,A)+\tLa(A,A)
=b_{xy}\tLa(C,A)
=b_{xy}\tLa(M_x' \hconv M_x,A) \\
&&\hs{10ex}=b_{xy}\tLa(M_x',A)+b_{xy}\tLa(M_x,A)=\tL(L,A)+b_{xy}\tLa(M_x,A).
\eneqn
On the other hand, the exact sequence \eqref{eq:sesMy} gives
\eqn
&&b_{xy}\tLa(M_x,A)+\tLa(P,A)=\tL(X,A)=\tL(M'_y\hconv M_y,A)\\
&&\hs{5ex}=\tL(M'_y,A)+\tL(M_y,A)=\tL(M_y\hconv M'_y,A)=
\tL(Y,A)=\tL(Q,A)+\tL(A,A).
\eneqn
It follows that
\eqn
&&\tLa(B \conv P,A)=\tLa(B,A) + \tLa(P,A) \\
&&\hs{5ex}=  \bl \tL(L,A)+b_{xy}\tLa(M_x,A)-\tLa(A,A)\br
+\bl \tL(Q,A)+\tL(A,A)-b_{xy} \tLa(M_x,A)\br\\
&&\hs{5ex}=\tLa(L,A) + \tLa(Q,A)=\tLa(L \conv Q, A). \label{eq:qpower3}
\eneqn

 Hence we have
\eqn
&&\xymatrix{
0 \ar[r] &  q (B \nconv P) \conv A \ar[r]  &q^{c}  M_y \conv (L\hconv M_y') \ar[r] & (L  \nconv Q) \conv A \ar[r] & 0,
}\label{eq:LQA}
\eneqn
where $c=\tLa(M_y, L \hconv M_y')-\tLa(B \nconv P,A)$ by Lemma \ref{lem:selfdual}.

Thus we obtain the identity in $K(R \gmod)$:
\eqn
q^c  [M_y] [L \hconv M_y'] = \bl q [B \nconv P] + [L \nconv Q]\br [A].
\eneqn




On the other hand,  the hypothesis \eqref{eq:Cluster} implies that
there exists $\phi \in \Q(q^{1/2}) \otimes_{\Z[q^{\pm1}]} K(\shc)$
corresponding to $\mu_y\mu_x([M])$ so that
it satisfies
\eq
[M_y] \phi = q [B \nconv P] + [L \nconv Q]
\label{eq:Mphi}
\eneq
and
\eq
\phi [\mu_x(M)_i] = q^{\la'_{yi}} [\mu_x(M)_i] \phi
\quad
\text{for} \ i \neq y,
\label{eq:phiA}
\eneq
where $\mu_y\mu_x(-\La)=(\la'_{ij})_{i,j\in\K}$.


Hence, in $\Q(q^{1/2}) \otimes_{\Z[q^{\pm1}]} K(\shc)$, we have
\eqn
[M_y] \phi [A] = \bl q [B \nconv P] + [L \nconv Q]\br [A ]=  q^c  [M_y][L \hconv M_y'].
\eneqn
Since $\Q(q^{1/2}) \otimes_{\Z[q^{\pm1}]} K(\shc)$ is a domain, we conclude that
\eqn
\phi [A] = q^c [L \hconv M_y'].
\eneqn


On the other hand,  \eqref{eq:phiA}  implies
\eqn
\phi [A] = q^{l} [A] \phi\quad\text{for some $l\in\Z$.}
\eneqn
Hence, Theorem \ref{thm:divisible} implies that, when we write
\eqn
\phi =\sum_{b \in B(\infty)} a_b [L_b]\quad\text{for some $a_b \in \Q(q^{1/2})$,}
\eneqn
we have $$L_b\conv A \simeq q^{l} A\conv L_b \quad \text{whenever } \ a_b\not=0.$$
In particular,  each module  $L_b\conv A $ with $a_b\not=0 $ is simple because $A$ is a real simple module.
Thus we obtain
\eqn
q^c [ L \hconv M_y' ] =\phi [A] = \sum_{b \in B(\infty)} a_b [L_b \conv A].
\eneqn
 Since $L \hconv M_y'$ is simple,
 there exists $b_0$ such that $L_{b_0} \conv A$ is isomorphic to $L \hconv M_y'$ up to a grading shift, and
 $a_b=0$ for $b \neq b_0$.
Set $M_y'':=L_{b_0}$.
Then we conclude that $\phi[A] = q^m [M_y'' \conv A]  =q^m[M_y''][A] $ so that
$$ \phi=q^m[M''_y] \quad \text{for some } \ m \in\Z.$$
We emphasize that $M_y''$ is a self-dual simple module in $R \gmod$ which satisfies that $M_y'' \conv A
\simeq L \hconv M_y $ up to a grading shift.






Now \eqref{eq:Mphi}  implies
$$q^m[M_y\conv M''_y] = q [B \nconv P] + [L \nconv Q].$$
Hence there exists an exact sequence
$$0\To W\To q^m\;M_y\conv M''_y\To Z\To 0,$$
where $W=q B \nconv P$ and $Z=L \nconv Q$ or
$W=L \nconv Q$ and $Z=q B \nconv P$.
By Lemma~\ref{lem:crde}, the  second case does not occur and we have an exact sequence
$$0\To q B \nconv P\To q^m\;M_y\conv M''_y\To L \nconv Q\To 0.$$

Since $M_y$, $M_y''$ and $L \nconv Q$ are self-dual, we have
$m=\tLa(M_y,M_y'')$,
and we obtain the desired short exact sequence \eqref{eq:seqdes'}.


\vskip 1em
Since $\phi$ commutes with $[\mu_x (M)_i]$  up to a power of $q$ in
$K(\shc)$,
and
$\mu_x(M)_i$ is real simple,
$M_y''$ commutes with $\mu_x (M)_i$ for $i\neq y$, by Corollary \ref{cor:qcomm_module}.
\QED

\Cor\label{cor:main}
Let  $(\{M_i\}_{i\in\K},\widetilde B)$ be an admissible pair in $\shc$.
Under the assumption \eqref{eq:Cluster},
$\shc$ is a monoidal categorification of the quantum cluster algebra
$\mathscr A_{q^{1/2}}([\seed])$.
Furthermore,  the following statements hold{\rm:}
\bnum
  \item The quantum monoidal seed $\seed=(\{M_i\}_{i\in\K},  -\La,\widetilde B,D)$
  admits successive mutations in all directions.
  \item Any cluster monomial in $\Z[q^{\pm1/2}] \otimes_{\Z[q^\pm1]} K(\shc)$
   is the isomorphism class of a  real simple object in $\shc$ up to a power of $q^{1/2}$.
  \item Any cluster monomial in $\Z[q^{\pm1/2}]\otimes_{\Z[q^\pm1]} K(\shc)$
is a Laurent polynomial of the initial cluster variables with coefficient
in $\Z_{\ge0}[q^{\pm1/2}]$.
\end{enumerate}
\encor

\Proof
(i) and (ii) are straightforward.

Let us show (iii). Let $x$ be a cluster monomial.
By the Laurent phenomenon (\cite{BZ05}),
we can
write
$$xX^{\mathbf{c}}=\sum_{\bfa\in\Z_{\ge0}^\K}c_\bfa X^\bfa,$$
where
$X=(X_i)_{i\in \K}$ is the initial cluster,  $\mathbf{c}\in\Z_{\ge0}^\K$
and $c_\bfa\in \Q(q^{\pm1/2})$.
Since $x$ and $X^{\mathbf{c}}$ are the isomorphism classes of simple modules
up to a power of $q^{1/2}$,
their product $xX^{\mathbf{c}}$ can be written as
a linear combination of
the isomorphism classes of simple modules
with coefficients in $\Z_{\ge0}[q^{\pm1/2}]$.
Since
every $X^\bfa$ is the isomorphism class of a simple module
up to a power of $q^{1/2}$,
we have
$c_\bfa\in \Z_{\ge0}[q^{\pm1/2}]$.
\QED
