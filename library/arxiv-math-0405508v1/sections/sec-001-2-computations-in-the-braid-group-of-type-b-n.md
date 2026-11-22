---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-001-2-computations-in-the-braid-group-of-type-b-n
section_title: "Computations in the braid group of type $B_n$"
section_number: 2
pages: 4-9
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.975
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 6 sections: Front matter; Introductory remarks on knots, bra; Computations in the braid group of"
---
It is the purpose of  this section to reformulate  some of the results
in \cite{GP}  on elements in signed block  form in  terms of the braid
group. These will then carry through to the Iwahori-Hecke algebra level and will be
used in the  existence and  uniqueness proof for the  analogues of   Ocneanu's 
trace for type $B$.
 
\medskip
2.1. Let $W_n$ and $\tilde{W}_n$ as in Section 1. For  each element $w$ in $W_n$ (or
in $\tilde{W}_n$) we  define the length, $l(w)$, to be the smallest non-negative 
integer $k$ such that $w$  can   be  written as  a    product of $k$  generators  
(or their inverses).  Such an expression of  $w$ of minimal possible length will
be called  a reduced expression for  $w$. (See \cite{Bour}, Chap.\ IV,
\S 1.1.) The  exchange  condition for Coxeter  groups implies   that, if we are
given two  reduced expressions of an element  in $W_n$ as  products in
the generators    $t,s_1,\ldots,s_{n-1}$      then the   corresponding
expressions  in the braid  group   $\tilde{W}_n$ are also  equal  (see
\cite{Bour}, Chap.\ IV, \S 1, Proposition~5).

 By convention, we let $W_0=\{1\}$. Then, for  all $n \geq 1$, the
group $W_{n-1}$ is a parabolic subgroup  of $W_n$ obtained by removing
the  node  with   label $s_{n-1}$   (cf.\ \cite{Bour}, Chap.\   IV, \S
1.8).  Hence, we have natural  embeddings $W_0 \subset W_1 \subset W_2
\subset \ldots$ and we let $W:=\bigcup_{n} W_n$.  We define
\[t_i:=s_is_{i-1} \cdots s_1ts_1 \cdots s_{i-1}s_i \in W_n \quad
\mbox{ for all $0 \leq i \leq n-1$, where $t_0:=t$}.\] Then the set of distinguished
right  coset representatives of $W_{n-1}$ in $W_n$ is given as follows.
\[ \begin{array}{lcl}
{\cal R}_n:=\{ & 1,\;\;\; t_{n-1}, & \\
         & s_{n-1}s_{n-2} \cdots s_{n-k} & (1 \leq k \leq n-1), \\
         & s_{n-1}s_{n-2} \cdots s_{n-k}t_{n-k-1} & (1 \leq k \leq n-1)\}\\
\end{array}\]
(Note that ${\cal R}_1=\{1,t\}$.) Then each element $w \in W_n$ can be
written uniquely in  the form $w=r_1 \cdots  r_n$ with  $r_i \in {\cal
R}_i$.   Such an   expression  of $w$  is  reduced, that  is,  we have
$l(w)=l(r_1)+\ldots +l(r_n)$.

Finally,  let   ${\cal  D}_n:=\{1,s_{n-1},  t_{n-1}\}  \subseteq {\cal
R}_n$.  Then ${\cal  D}_n$  is the set  of distinguished  double coset
representatives of $W_{n-1}$ in $W_n$ (see \cite{Bour}, Chap.\ IV, \S 1, 
Ex.\ 3).

Each  $r  \in {\cal R}_n$  can  now be written  uniquely   in the form
$r=dr'$ where   $d \in {\cal  D}_n$  and  $r'=1$  or $r'=s_{n-2}\cdots
s_{n-k}$ or $r'=s_{n-2} \cdots s_{n-k}t_{n-k-1}$. In particular, we
have $r' \in {\cal R}_{n-1}$.


\medskip
2.2.  We   shall  now lift these elements to the   braid  group
$\tilde{W}_n$.  First  note   that we also     have natural embeddings
$\tilde{W}_0  \subset \tilde{W}_1 \subset  \tilde{W}_2 \subset \ldots$
and we  let $\tilde{W}:=\bigcup_{n}  \tilde{W}_n$.   Geometrically the
embedding of $B_{1,n}$ into $B_{1,n+1}$  is described by the following
picture.

$$\vbox{\picill3.7inby1.04in(mein2)  }$$   

\noindent We would like to define the analogue of $t_i$ to be a conjugate  
of $t$ where the conjugating element is of the form $s_1^{\pm 1} \cdots
s_i^{\pm 1}$. In accordance with the geometric considerations in Section~1,
we choose the exponents $\pm 1$ so as to obtain the element $t_i'$ 
already encountered above:
\[ t_i':=s_is_{i-1} \cdots s_1ts_1^{-1} \cdots s_{i-1}^{-1}s_i^{-1} 
\in \tilde{W}_n \quad \mbox{ for all $0 \leq i \leq n-1$}.\] 
(All inverses on the right hand side of $t$.) Then each $t_i'$ maps to
$t_i$  under  the canonical surjection $\tilde{W}_n  \rightarrow W_n$.
We  let ${\cal D}_n' \subseteq {\cal  R}_n'  \subseteq \tilde{W}_n$ be
the analogous sets as above, where each $t_i$ is replaced by $t_i'$.

For  any $i,j$ the  elements $t_j$  and $t_i$  commute with each other
(cf.\ \cite{GP}, (2.3)). For $t_j'$ and $t_i'$, this will only be true 
up to possibly changing some inverses in the definition of these elements. 
We will not completely formalize this, but only give the following 
additional definition.  For any $j \in \{0,\ldots,i\}$ we denote 
\begin{eqnarray*}
t_{i,j}' & :=  & s_i^{\pm 1} \cdots  s_{j+1}^{\pm 1} s_js_{j-1} \cdots
s_1ts_1^{-1} \cdots    s_{j-1}^{-1}s_j^{-1}s_{j+1}^{\mp      1} \cdots
s_i^{\mp 1}\\ &     =     & s_i^{\pm  1}   \cdots    s_{j+1}^{\pm   1}
t_j's_{j+1}^{\mp 1}  \cdots  s_i^{\mp  1}.\end{eqnarray*}  (That is,  all
inverses up   to index $j$  are in  the right  position,  and for each
bigger  index, the inverse may  be put either on  the  right or on the
left hand side.)

Finally,   we  let ${\cal  D}_{n,j}'$  be  the set  consisting of $1$,
$s_{n-1}$ and  all possible elements of  the form $t_{n-1,j}'$. 
Similarly, we define ${\cal R}_{n,j}'$.  As a convention, we will 
usually denote the elements in ${\cal D}_{n,0}'$ by the symbol $d_n^{*}$. 

The next result will show  that, in particular,  a product of the form
$t_i't_j'$ with $i < j$ can be written as $t_{j,i}'t_j'$. Relations of
this kind will be used frequently in the sequel.


\addtocounter{thm}{2}
\begin{lem}
The following relations hold in $\tilde{W}_n$.

\begin{itemize}

\item[(a)] $s_it_m'=t_m's_i$ and $s_i^{-1}t_m'=t_m's_i^{-1}$ for all 
$i<m$ and $i>m+1$.

\item[(b)] $t_i't_m'=s_m \cdots s_{i+2}s_{i+1}^{-1}s_i\cdots s_1ts_1^{-1}
\cdots s_i^{-1}s_{i+1}s_{i+2}^{-1}\cdots s_{m}^{-1}t_i'$ for $i < m$.\\
(The inverse at index $i+1$ changes in $t_m'$) 
\item[(c)] $s_{m-1} \cdots s_{m-k}t_{m-k-1}'t_{m}'=
t_{m,m-1}'s_{m-1} \cdots s_{m-k}t_{m-k-1}'$ for $0 \leq k \leq m-1$.
(The inverse at index $m$ changes in $t_m'$)
\end{itemize}
\end{lem}

\begin{pf} The defining relations for $\tilde{W}_n$ imply that
\begin{eqnarray*}
ts_i^{-1}=s_i^{-1}t & \mbox{  if } &  i>1 \\ s_is_j^{-1}=s_j^{-1}s_i &
\mbox{ if  } &  |i-j|>1 \\ s_is_{i+1}s_i^{-1}=s_{i+1}^{-1}s_is_{i+1} &
\mbox{ if  } & 1 \leq  i \leq n-2  \\ s_1^{-1}ts_1t=ts_1ts_1^{-1}. & &
\end{eqnarray*} The assertions   of  the Lemma now  readily  follow by
straightforward computations.   (Notice that these relations  could be
alternatively checked easily using the geometric interpretations given
above.) \end{pf}

\medskip
2.4. Consider an element of the form  $d_1 \cdots d_n \in \tilde{W}_n$
with   $d_i \in {\cal   D}_i'$ for  all $i$.   If  we collect together
non-trivial terms with consecutive  indices we obtain a  decomposition
of  this element  as  a product of  signed blocks.   More precisely, a
positive respectively  negative  block  of length   $m+1  \geq 0$   in
$\tilde{W}_n$ is an element of the form
\[s_{i+1}s_{i+2}\cdots s_{i+m} \quad \mbox{ respectively } \quad
t_i's_{i+1} \cdots s_{i+m}\] where  $m,i\geq 0$. If  we denote such an
element     by        $b(i,m)$       then           \[d_1       \cdots
d_n=b(i_1,m_1)b(i_2,m_2)b(i_3,m_3)      \cdots,  \quad  \mbox{ where }
i_2>i_1+m_1, i_3>i_2+m_2 \mbox{ etc}.\] By \cite{GP}, \S 2, each conjugacy 
class in the Coxeter group $W_n$ contains an element in signed block 
form, and such an element is of miminal length in its class if and only 
if all negative blocks are in the beginning, ordered by increasing length. 
In order to reduce an arbitrary element in $W_n$ to such a minimal form, 
it is necessary to interchange by conjugation two consecutive blocks in 
the signed block form of an element in $W_n$. Our aim here is to show 
that similar relations also hold in the braid group.

\addtocounter{thm}{1}
\begin{lem} {\rm (cf.\ \cite{GP}, Proposition~2.4.)}\\
Let  $y=(s_{i+m+1}  \cdots s_{i+1})  (s_{i+m+2} \cdots s_{i+2}) \cdots
(s_{i+m+k+1} \cdots s_{i+k+1})$ for $i,k,m \geq 0$. Geometrically
\ $y$ \ is  a half-twist of  $m+1$ consecutive strands around the next
$k+1$ consecutive strands in the classical braid group.

(a) Let
\begin{eqnarray*} 
w & = & (s_{i+1} s_{i+2} \cdots s_{i+m}) (s_{i+m+2} 
s_{i+m+3} \cdots s_{i+m+k+1}) \quad \mbox{and}\\ 
v & = & (s_{i+1} s_{i+2} \cdots s_{i+k}) (s_{i+k+2} s_{i+k+3} \cdots 
s_{i+k+m+1}).  \end{eqnarray*}
Then $y^{-1}wy=v$  in the braid group.

(b) Let 
\begin{eqnarray*}
w & = & (s_{i+1} s_{i+2} \cdots s_{i+m}) (t_{i+m+1}'s_{i+m+2} 
s_{i+m+3} \cdots s_{i+m+k+1}) \quad \mbox{and} \\
v & = & (t_i's_{i+1} s_{i+2} \cdots s_{i+k}) (s_{i+k+2} s_{i+k+3} \cdots 
s_{i+k+m+1}).  \end{eqnarray*}
Then $y^{-1}wy=v$ in the braid group.

(c) Let \[w = (t_i's_{i+1} s_{i+2} \cdots s_{i+m}) (t_{i+m+1}'s_{i+m+2} 
s_{i+m+3} \cdots s_{i+m+k+1})\] for some $m>k$. Then $y^{-1}wy=v$ in the 
braid group where
\[ v  = (t_i's_{i+1} s_{i+2} \cdots s_{i+k})(t_{i+k+1,i}'s_{i+k+2} s_{i+k+3}
 \cdots s_{i+k+m+1})\] for some $t_{i+k+1,i}'$ (see the proof below).

In (b), (c), the length of $v$ is strictly shorter than the length of $w$.
\end{lem}

\begin{pf} Geometrically, (a), (b) and (c) follow immediately by looking 
at  the corresponding braid  pictures and comparing their closures; note that
in each case we obtain links  of two components.  For an algebraic proof,
we  use the similar relations   in \cite{GP}, Proposition~2.4, on  the
level of $W_n$.   We have to slightly  modify those arguments in order
to derive relations in $\tilde{W}_n$.

(a)  In \cite{GP}, Proposition~2.4(a), it   is shown that the equation
$wy=vy$ holds  in $W_n$ and  that the  expressions  on both sides  are
reduced.  Hence the  left hand side  can be  transformed to  the right
hand side by  a finite sequence of braid  relations.   It follows that
the equation $wy=vy$ also holds in the braid group.

(b) We write $y=(s_{i+m+1} \cdots s_{i+1})y'$. Then 
\[ y^{-1}t_{i+m+1}'y= y^{-1}s_{i+m+1} \cdots s_{i+1}t_i's_{i+1}^{-1} \cdots
s_{i+m+1}^{-1}y = {y'}^{-1}t_i'y'=t_i'.\]  For the last equality, note
that $y'$ is  a product of generators $s_j$  with $j>i+1$ and that all
of these commute with $t_i'$.

Now $(s_{i+1} \cdots s_{i+m})$  commutes with $t_{i+m+1}'$. So we  can
write $w=t_{i+m+1}'w_a$ and $v=t_i'v_a$  where $w_a$ and $v_a$  are as
in part (a) of the Lemma. Hence we deduce, using (a), that
\[ y^{-1}wy=(y^{-1}t_{i+m+1}'y)(y^{-1}w_ay)=t_i'v_a=v.\]

(c) We rearrange the given reduced expression for $y$ as 
\[ y=(s_{i+m+1} \cdots s_{i+m+k+1})  (s_{i+m} \cdots s_{i+m+k}) \cdots  
(s_{i+1} \cdots    s_{i+k+1})\]   and write   $y=y'(s_{i+1}     \cdots
s_{i+k+1})$.  Now note that $y'$ is a product of generators $s_j$ with
$j>i+1$ and  that all of these  commute  with $t_i'$. Then  we compute
that
\begin{eqnarray*}
y^{-1}t_i'y     &          =      &        (s_{i+k+1}^{-1}      \cdots
s_{i+1}^{-1}){y'}^{-1}t_i'y'(s_{i+1}  \cdots    s_{i+k+1}) \\  &   = &
s_{i+k+1}^{-1} \cdots s_{i+1}^{-1}t_i's_{i+1} \cdots s_{i+k+1} \\ & =:
& t_{i+k+1,i}''. \end{eqnarray*} We can  write $w=t_i'w_b$ where $w_b$
is as in part (b). Thus, we deduce, using (b), that
\[y^{-1}wy = (y^{-1}t_i'y)(y^{-1}w_by) = 
(t_{i+k+1,i}''t_i's_{i+1} \cdots s_{i+k})(s_{i+k+2} \cdots s_{i+k+m+1}).\]
Using Lemma~2.3(b), we compute that $t_{i+k+1,i}''t_i'=t_i't_{i+k+1,i+1}''$
where the inverses in $t_{i+k+1,i+1}''$ at all indices bigger than $i+1$ 
are on the left hand side of $t$. A final calculation then shows that 
\[t_{i+k+1,i+1}''(s_{i+1} \cdots s_{i+k})=(s_{i+1} \cdots s_{i+k})
(s_{i+k+1}s_{i+k}^{-1} \cdots s_{i+1}^{-1}t_i's_{i+1} \cdots 
s_{i+k}s_{i+k+1}^{-1}).\]
If we denote the second factor on the right hand by $t_{i+k+1,i}'$ then
$y^{-1}wy=v$ as required.  The proof is complete.  \end{pf}

\begin{rems} \rm 
(a) One can also  show that, if   the conjugation in  (b), (c)  of the
above Lemma is performed step by step (one generator of $y$ at a time)
then this sequence of conjugations can be arranged  in such a way that
the length  of the elements  does  not increase at  each step   (cf.\
\cite{GP}, Proposition~2.4(b,c)).

(b) Consider the elements
\[ w=(s_1) (s_2^{-1}s_1ts_1^{-1}s_2) \quad \mbox{ and } \quad v=ts_2 
\quad \mbox{(in $\tilde{W}_3$)}.\]
If  all the inverses in  $w$ were on the  right  hand side of $t$ then
this element would be  conjugate to $v$  in $\tilde{W}_3$, by part (b)
of the above Lemma  (with $m=1$, $k=i=0$). However,  one can show that
$w$  and $v$ are  not conjugate in $\tilde{W}_n$, and  not even in the
associated Iwahori-Hecke algebra.   This  example indicates  that  the
statements in the above Lemma  are as strong as  possible, and that we
cannot distribute the inverses in some arbitrary order around $t$ when
we want to conjugate elements in block form.

Note, however, that the oriented links obtained by closing the braids
corresponding to the above elements are isotopic (see (5.4) below). In 
particular, the knot invariants constructed in Definition~5.3 must
have the same value on them.
\end{rems}
