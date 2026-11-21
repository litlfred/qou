---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-002-3-trace-functions-on-the-iwahori-hecke-algebra-o
section_title: "Trace functions on the Iwahori-Hecke algebra of type $B$"
section_number: 3
pages: 9-12
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.95
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 6 sections: Front matter; Introductory remarks on knots, bra; Computations in the braid group of"
---
In this section, we introduce the  Iwahori-Hecke algebra $H_n$ of type
$B_n$ as a quotient of  the braid group algebra  of $\tilde{W}_n$.  We
also   show how the  main  results  of \cite{GP}  on determining trace
functions on  $H_n$ can be   adapted to  our  present situation  where
reduced expressions  for representatives   of minimal length    in the
conjugacy classes involve some inverses.

\medskip
3.1. Let $A$ be a commutative ring with~$1$ and $Q,q \in A$ two
fixed invertible elements.  Then $H_n$  is an associative algebra over $A$. 
It can be described as a quotient of the
group algebra of the braid  group $\tilde{W}_n$ (over $A$) obtained by
factoring by the ideal generated  by all elements  of the form $t^2 
-(Q-1)t-Q \cdot 1$, $s_i^2-(q-1)s_i- q \cdot 1$ for $i=1,\ldots,n-1$.  We
denote the    image  of $t$  under the   canonical   map $A\tilde{W}_n
\rightarrow H_n$ again by  $t$, and the image of  $s_i$ by  $g_i$, for
all $i$. Then the generators  $t,g_1,\ldots,g_{n-1}$ of $H_n$  satisfy
braid  relations completely analogous to  the braid  relations for the
generators  $t,s_1,\ldots,s_{n-1}$ of   $\tilde{W}_n$.  In
addition, we have the following quadratic relations.
\[ t^2=(Q-1)t+Q \cdot 1  \quad \mbox{ and } \quad g_i^2=(q-1)g_i+q \cdot 1 
\mbox{ for all $i$}.\]
Let $w \in W_n$ and assume that we  are given a reduced expression for
$w$ as a  product    of generators $t,s_1,\ldots,s_{n-1}$.  Then   the
corresponding element      of $H_n$  in  terms     of  the  generators
$t,g_1,\ldots,g_{n-1}$ is independent of the chosen reduced expression
for $w$.  We may therefore  denote this element in $H_n$ unambiguously
by   $g_w$. It is  known that  the set  of elements $\{g_w  \mid w \in
W_n\}$  forms   an $A$-basis of   $H_n$.  (For   all these  facts see
\cite{Bour},  Chap.\  IV,  \S 2, Ex.\   23.)   We then also   have the
following relations.
\[ g_w g_{w'}=g_{ww'} \quad \mbox{ if $l(ww')=l(w)+l(w')$}.\]
The embeddings $W_0 \subset W_1 \subset W_2 \subset \ldots$ of (2.1)
induce corresponding embeddings of algebras $H_0 \subset H_1 \subset H_2 
\subset \ldots$ and we shall denote
\[ H:=\bigcup_{n \geq 0} H_n.\]

\medskip
3.2.  The fact that $q$ is invertible in $A$ implies that the generators
$g_i$ are also invertible in $H$. In fact, we have that
\[ g_i^{-1}=q^{-1}g_i+(q^{-1}-1) \cdot 1 \in H_n.\]
Thus, the images of the elements $t_i',t_{i,j}' \in \tilde{W}_n$ under
the map  $A\tilde{W}_n  \rightarrow H_n$ are  well-defined elements in
$H_n$, and we shall denote them by the same symbols. We also write
\[{\cal D}_n' = \{ 1,g_{n-1}, t_{n-1}' \}\]
and,   similarly, for  ${\cal   R}_n'$, ${\cal  D}_{n,i}'$ and  ${\cal
R}_{n,i}'$ (cf.\ (2.2)). With   these conventions, all results   about
commutation and conjugation of the various special elements considered
in the previous section carry over without change to $H_n$.

Let $w \in W_n$ and write $w=r_1 \cdots r_n$ with $r_i \in {\cal R}_i$
for  all $i$. Since this expression is reduced we also have $g_w=
g_{r_1} \cdots g_{r_n}$. For  each $r_i$ let   $r_i' \in {\cal  R}_i'$  be 
the corresponding element in $H_n$ (where the $s_j$ are replaced by $g_j$,
and $t_j$  by   $t_j'$).  Let $n_w  \geq  0$  be the   total number of
inverses in the   terms $r_1',\ldots,r_n'$. Using  the above inversion
formula it then follows that
\[ g_w=q^{n_w}r_1' \cdots r_n'+ \mbox{$A$-linear combination of elements
$g_v$ with $l(v) < l(w)$}.\] One consequence of this  is the fact that
the elements $\{r_1' \cdots r_n' \mid r_i' \in  {\cal R}_i'\}$ form an
$A$-basis of   $H_n$,  and if   we order  the   elements of  $W_n$  by
increasing  length then the matrix  performing the base  change to the
old  basis $\{ g_{r_1    \cdots r_n} \mid   r_i  \in {\cal  R}_i\}$ is
triangular with powers of $q$ along the diagonal.

\medskip 
3.3. Let $\{C\}$ be the set of conjugacy classes of $W_n$ and let $w_C$ be 
an element of minimal length in $C$ which admits a decomposition as a 
product of negative blocks (ordered by increasing length) followed
by various positive blocks (see (2.4)). We can even fix a unique choice
of $w_C$ if we also require that the positive blocks  have increasing 
length. We then define an element $g_C \in  H_n$ by taking an
expression $w_C=d_1 \cdots d_n$ (with $d_i \in {\cal D}_i$) and replacing 
each  $s_i$ by  $g_i$ and each $t_i$ by $t_i'$.  As in (3.2) we have (with 
$n_C:=n_{w_C}$) that
\[ g_{w_C} =q^{n_C}g_{C}+   \mbox{$A$-linear combination of elements $g_w$ 
with $l(w)<l(w_C)$}.\] 
A  trace  function   on $H_n$   is  an  $A$-linear  map   $\varphi:H_n
\rightarrow  A$ such that  $\varphi(h h')=\varphi(h' h)$ for all $h,h'
\in   H_n$.  By \cite{GP}, each trace   function  on $H_n$ is uniquely
determined  by  its   values   on  the  elements   $g_{w_C}$,  for all
$C$. Conversely, given  a set  of elements  $a_C \in A$,  one for each
conjugacy class $C$, there exists a unique trace function $\varphi$ on
$H_n$ such that $\varphi(g_{w_C})=a_C$ for all~$C$.  Using the above 
relations, we deduce that these results on the determination of trace 
functions  remain valid when we replace each $g_{w_C}$ by $g_C$, for all~$C$.

The following result will show how to reduce the computation of the value
of a  trace function  on any element to the values on elements in signed
block form.


\addtocounter{thm}{3}
\begin{prop}
For each $h \in  H_n$ there exists a  finite (non-empty) subset  $I(h)
\subseteq   A  \times  {\cal  D}_{1,0}'  \times   \ldots \times  {\cal
D}_{n,0}'$ such that \[\varphi(h) =   \sum_{(r,d_1^{*},\ldots,d_n^{*})
\in I(h)} r \varphi(d_1^{*} \cdots d_n^{*}),\] for all trace functions
$\varphi$ on $H_n$.
\end{prop}

\begin{pf}
The result clearly holds  if $n=1$. Now  let  $1<j \leq n$ and  assume
that we have already found  a finite (non-empty) subset $I_j \subseteq
H_j \times D_{j+1,j-1}' \times  \ldots \times {\cal D}_{n,j-1}'$  such
that \[ \varphi(h)= \sum_{(h_j,d_{j+1}',\ldots,d_n') \in I_j} 
\varphi(h_jd_{j+1}' \cdots d_{n}'),\]
for  all trace  functions $\varphi$  on    $H_n$. We will  proceed  by
downward induction on $j$. For $j=n$ there is nothing to prove. We now
show  how to   obtain an  analogous   statement with  $j$ replaced  by
$j-1$. This is done as follows.

Consider one element  $(h_j,d_{j+1}',  \ldots,d_n') \in  I_j$. The
element $h_j$ is an $A$-linear combination of basis elements $g_w$
with $w \in W_j$. By (3.2), this can be rewritten as an $A$-linear
combination of products $r_1' \cdots r_j'$ with $r_i' \in {\cal R}_i'$.
Collecting terms with a fixed value of $r_j'$, we obtain a finite 
(non-empty) subset   $R(h_j) \subseteq H_{j-1}  \times {\cal  R}_j'$   
such  that \[h_j=\sum_{(h_{j-1},r_j')  \in R(h_j)} h_{j-1}r_j'.\] 
We  can write $r_j'=d_j'r_{j-1}''$   with  $d_j' \in  {\cal D}_j'$  
and $r_{j-1}'' \in {\cal R}_{j-1}'$ (cf.\  (2.1)). Now  the element 
$r_{j-1}''$ either is a product of various generators $g_1,\ldots,g_{j-2}$
or is like the element considered in Lemma~2.3(c). In any case,  it 
commutes with $d_{j+1}'$ up to (possibly) changing some inverses at 
indices bigger than $j-2$, and similarly for $d_{j+2}',\ldots,d_{n}'$. 
Thus, we conclude that 
\[ h_jd_{j+1}'\cdots d_n' = \sum_{(h_{j-1},r_j') \in R(h_j)} 
h_{j-1}d_j'd_{j+1}'' \cdots d_n''r_{j-1}'',\] where $d_{j+1}'' \in   
{\cal D}_{j+1,j-2}',\ldots,d_n'' \in {\cal D}_{n,j-2}'$. 
So we have that \[\varphi(h)=\sum_{(h_j,d_{j+1}',\ldots,d_n') \in I_j}
\sum_{(h_{j-1},r_j') \in R(h_j)} \varphi(r_{j-1}''h_{j-1}d_j'd_{j+1}''
\cdots d_n'').\]  We  can combine the index   sets to a  new  set  
$I_{j-1}  \subseteq H_{j-1}  \times {\cal D}_{j,j-2}' \times \ldots 
\times  {\cal D}_{n,j-2}'$ and arrive  at a new  expression  as above  
with  $j$ replaced  $j-1$.  We  repeat this process until  we  arrive 
at  $j=1$.  Then $H_1=\langle 1,  t \rangle= \langle {\cal D}_1' 
\rangle$, and we are done.  \end{pf}

In fact, the above proof also yields the following extension.

\begin{cor}
Let $h \in H_n$ and $d_{n+1} \in {\cal D}_{n+1}', \ldots, d_{n+m} \in 
{\cal D}_{n+m}'$ (for some $m \geq 0$). Then, for all trace functions
$\varphi$ on $H_n$, we have that
\[\varphi(hd_{n+1} \cdots d_{n+m})=\sum_{(r,d_1^{*},\ldots,d_n^{*}) \in I(h)} 
r\varphi(d_1^{*} \cdots d_n^{*}d_{n+1}^{*} \cdots d_{n+m}^{*}),\]
for some elements $d_{n+1}^{*} \in {\cal D}_{n+1,0}',\ldots,
d_{n+m}^{*} \in {\cal D}_{n+m,0}'$ (depending on the various elements in 
$I(h)$).
\end{cor}
