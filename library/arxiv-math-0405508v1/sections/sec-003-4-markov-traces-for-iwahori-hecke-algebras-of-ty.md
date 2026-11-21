---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-003-4-markov-traces-for-iwahori-hecke-algebras-of-ty
section_title: "Markov traces for Iwahori-Hecke algebras of type $B$"
section_number: 4
pages: 12-20
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.957
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 6 sections: Front matter; Introductory remarks on knots, bra; Computations in the braid group of"
---
Jones writes in \cite{Jones}, p.346, that there should be analogues of
Ocneanu's trace for  Iwahori-Hecke  algebras other than those  of type
$A$. The  trace given  in \cite{L2} was  the  first such  analogue for
$B$-type  Iwahori-Hecke   algebras.  The  aim of  this   section is to
classify  {\it all} such  `Markov' traces on Iwahori-Hecke algebras of
type $B$, based on the results in the previous sections.


\begin{defn} 
Let $z \in A$ and $\tau:H \rightarrow A$ be an $A$-linear map. Then $\tau$
is called a Markov trace (with parameter $z$) if the following conditions 
are satisfied.
\begin{itemize}
\item[(1)] $\tau$ is a trace function on $H$.
\item[(2)] $\tau(1)=1$ (normalization).
\item[(3)] $\tau(hg_n)=z\tau(h)$ for all $n \geq 1$ and $h \in H_n$.
\end{itemize}
\end{defn}

\noindent We note that all generators $g_i$ (for $i=1,2,\ldots$) are 
conjugate in $H$. In particular, any trace function on $H$ must have the 
same value on these elements. This explains why the parameter $z$ is 
independent of $n$ in rule (3) of this definition. 

Let   us  consider    the  subalgebra   $H'$ of    $H$  generated   by
$g_1,g_2,\ldots$.   Then  $H'$ is  the algebra  considered by Jones in
\cite{Jones}, \S 5 (infinite  union over all Iwahori-Hecke algebras of
type  $A_n$ with parameter  $q$).   Moreover, the restriction of  any
Markov trace $\tau$ on $H$ to $H'$  yields Ocneanu's original trace as
in  \cite{Jones},  Theorem~5.1,  which is uniquely   determined by the
parameter~$z$.

The next result describes a set of elements in $H$ which is sufficient
to determine a  Markov trace $\tau$. We shall see that this set
is in fact as small as possible.

\begin{lem}
Let $\tau:H \rightarrow A$ be a Markov trace (with parameter~$z \in A$).
\begin{itemize}
\item[(a)] If $n \geq 1$, $m \geq 0$ and $h \in H_n$, then 
\begin{eqnarray*}
 \tau(hg_nt_{n+1}' \cdots t_{n+m}') & = & z \tau(ht_n' \cdots 
t_{n+m-1}') \quad \mbox{ and }\\
 \tau(ht_{n+1}' \cdots t_{n+m}') & = &  \tau(ht_n' \cdots 
t_{n+m-1}') \end{eqnarray*}
\item[(b)] If $h=d_1 \cdots d_n \in H$ where $d_i \in {\cal D}_i'$ for all
$i$ then  \[ \tau(h)=z^{a(h)} \tau(t_0't_1' \cdots  t_{b(h)-1}')\] where
$a(h)$  is    the   number  of    $d_i$    which   are  in  the    set
$\{g_1,\ldots,g_{n-1}\}$  and $b(h)$ is the number  of $d_i$ which are
conjugate to $t$.
\item[(c)] $\tau$ is uniquely determined by its values on the elements 
in the set \[ \{ t_0' t_1' \cdots t_{k-1}' \mid k=1,2,\ldots \}.\]
\end{itemize}
\end{lem}

\begin{pf} To prove the first relation in (a) we will proceed by induction 
on $m$.    If $m=0$   then we    can   apply directly    rule (3)   in
Definition~4.1.  Now let  us assume that  $m>0$.  We  have to evaluate
the expression
\[\tau(hg_nt_{n+1}' \cdots t_{n+m}').\]
We write $t_{n+1}'=g_{n+1}t_n'g_{n+1}^{-1}$ and observe that $g_{n+1}^{-1}$
commutes with $t_{n+2}',\ldots,t_{n+m}'$ by Lemma~2.3(a). Since $\tau$ is
a trace our expression is equal to
\[\tau(g_{n+1}^{-1}hg_ng_{n+1}t_n't_{n+2}' \cdots t_{n+m}').\]
Now $h$   lies in $H_n$,  that is,  $h$ only   involves the generators
$t,g_1,\ldots,g_{n-1}$.     It follows    that    $h$   commutes  with
$g_{n+1}^{-1}$.    Using      moreover        the   braid     relation
$g_{n+1}^{-1}g_ng_{n+1}=g_ng_{n+1}g_n^{-1}$, the above  expression can
be rewritten as
\[\tau(hg_ng_{n+1}g_n^{-1}t_n't_{n+2}' \cdots t_{n+m}').\] 
If we write $t_n'=g_nt_{n-1}'g_n^{-1}$,  the left hand term $g_n$ will
cancel and then $g_{n+1}$ commutes with $t_{n-1}'$. Now our expression
reads
\[\tau(hg_nt_{n-1}'g_{n+1}g_n^{-1}t_{n+2}' \cdots t_{n+m}').\] 
The element $g_n^{-1}$ commutes with all terms to the right of it. Hence our
expression is equal to
\[\tau(g_n^{-1}hg_nt_{n-1}'g_{n+1}t_{n+2}' \cdots t_{n+m}').\]
We write $h':=g_n^{-1}hg_nt_{n-1}'$ and observe that this element lies
in $H_{n+1}$. So we can apply the induction and obtain that
\[\tau(hg_nt_{n+1}' \cdots t_{n+m}')=\tau(h'g_{n+1}t_{n+2}' \cdots t_{n+m}')=
z \tau(h't_{n+1}' \cdots t_{n+m-1}').\]
We insert the expression for $h'$ again, note that $g_n^{-1}$ commutes
with $t_{n+1}' \cdots t_{n+m-1}'$, and conclude that
\[\tau(h't_{n+1}' \cdots t_{n+m}')= 
\tau(hg_nt_{n-1}'g_n^{-1} t_{n+1}' \cdots t_{n+m-1}')=
\tau(ht_n't_{n+1}' \cdots t_{n+m-1}').\]
Putting  things together we see that  this completes  the proof of the
first relation. The proof  of the second is  achieved by  an analogous
computation  (with $g_n$ replaced by~$1$).  In  order  to prove (b) we
consider an element
\[ h=d_1 \cdots d_n \in H_n \quad \mbox{ where $d_i \in {\cal D}_i'$ for all
$i$.} \] Using (a) and induction on $n$ we deduce that 
\[ \tau(h)=z^{a(h)} \tau(t_0't_1' \cdots t_{b(h)-1}')\]
where $a(h),b(h)$ are defined as above. Using (3.3) we 
conclude that these equations determine $\tau$ uniquely, proving (c).  
\end{pf}

\begin{thm}
Let $z,y_1,y_2 \ldots \in A$. Then there exists a unique Markov trace 
$\tau$ on $H$ with parameter $z$ such that 
\[ \tau(t_0't_1't_2' \cdots t_{k-1}')=y_k \quad \mbox{ for all $k \geq 1$.}\]
\end{thm}

\begin{pf} Uniqueness was already proved in Lemma~4.2. Using the facts 
summarized  in  (3.3) we can  define  a  trace function  $\tau$ on $H$
satisfying $\tau(1)=1$ and \[ \tau(g_C)=z^ay_b\] where $g_C=d_1 \cdots
d_n$   with   $d_i  \in  {\cal D}_i'$   and   the elements $a=a(g_C)$,
$b=b(g_C)$ are defined as in Lemma~4.2. Thus, the existence of a trace
function  $\tau$    on   $H$   satisfying   conditions~(1),  (2)    in
Definition~4.1 is already established. The problem is to show that (3)
holds.

This will  be done by an  induction, as follows.   For $N \geq  0$ let
$H(\leq N)$ be the $A$-subspace of $H$ generated by all elements $g_w$
with $w \in W$ and $l(w) \leq N$. We  shall prove the following claim,
for all $N \geq 0$.
\begin{itemize}
\item[(*)] {\em Let $h \in H_n$ and $d_{n+i}^{*} \in  
{\cal D}_{n+i,0}'$ (for some $n,m \geq 1$ and $i=1,\ldots,m$) such that 
$hd_{n+1}^{*}\cdots d_{n+m}^{*} \in H(\leq N)$.
Then} 
\begin{eqnarray*}
\tau(hd_{n+1}^{*} \cdots d_{n+m}^{*}) & = & \tau(hd_{n+1} \cdots 
d_{n+m}) \quad \mbox{ and} \\
\tau(hg_nd_{n+2}^{*}d_{n+3}^{*} \cdots d_{n+m}^{*}) & = & z\tau(hd_{n+2}^{*} 
\cdots d_{n+m}^{*}). \end{eqnarray*} 
\end{itemize}
(Here, we used  the following convention. For each  $i$, we  denote by
$d_i$ the analogous element as $d_i^{*}$ with the inverses (if any) on
the right hand side of $t$.) If this is proved for all $N$ then $\tau$
will   satisfy condition  (3)    in    Definition~4.1 as a     special
case. Clearly, (*) is true  for $N=0$. Now  let $N>0$. We proceed in a
number of steps.

\medskip
{\em Step~1.} At first we show that $\tau(hd_{n+1}^{*} \cdots d_{n+m}^{*})
=\tau(hd_{n+1} \cdots d_{n+m})$. By induction on $m$ we may assume
that $d_{n+2}^{*}=d_{n+2},\ldots, d_{n+m}^{*}=d_{n+m}$. We can also assume
that
\[d_{n+1}^{*}=T_{n+1,i}:=g_{n} \cdots g_{i+1}g_i^{\mp 1}t_{i-1,0}'
g_i^{\pm 1}g_{i+1}^{-1} \cdots g_{n}^{-1} \quad \mbox{ for some  $i \leq n$}.
\]
(That is, the inverses are already fixed at  indices   bigger than $i$.)    
Then $T_{n+1,i-1}$ is  the analogous element where  the inverse at index  
$i$ is also  correct.  Now assume that the sign in $g_i^{\mp 1}$ is $-1$.
We will show that $\tau(hT_{n+1,i}d_{n+2} \cdots d_{n+m})=\tau(hT_{n+1,i-1}
d_{n+2} \cdots d_{n+m})$.  This is done as follows.  In $T_{n+1,i}$  and 
$T_{n+1,i-1}$ we  replace $g_i^{-1}$ by $(q^{-1}-1)g_i+q^{-1} \cdot 1$. 
Then $hT_{n+1,i}d_{n+2} \cdots d_{n+m}=(q^{-1}-1)S_1+ q^{-1}S_2$ and 
$hT_{n+1,i-1}d_{n+2} \cdots d_{n+m}=(q^{-1}-1)S_1+q^{-1}S_3$ where
\begin{eqnarray*}
S_1 & = & h (g_n \cdots g_{i+1}g_i t_{i-1,0}'g_ig_{i+1}^{-1} \cdots g_n^{-1})
                    d_{n+2} \cdots d_{n+m},\\
S_2 & = & h (g_n \cdots g_{i+1}t_{i-1,0}'g_ig_{i+1}^{-1} \cdots g_n^{-1}) 
                    d_{n+2} \cdots d_{n+m},\\
S_3 & = & h (g_n \cdots g_{i+1}g_it_{i-1,0}'g_{i+1}^{-1} \cdots g_n^{-1})
                    d_{n+2} \cdots d_{n+m}.
\end{eqnarray*}
Note that $S_2,S_3 \in H(\leq N-1)$ so that we can use our inductive
hypotheses in the evaluation of $\tau$ on these elements.
Let us first consider $S_2$. At first, we note that $g_n \cdots g_{i+1}$
commutes with $t_{i-1,0}'$. So we obtain that
\begin{eqnarray*}
\tau(S_2) & = & \tau(ht_{i-1,0}'(g_n \cdots g_{i+1}g_ig_{i+1}^{-1} 
               \cdots g_n^{-1})d_{n+2} \cdots d_{n+m}) \\
    & = & \tau(ht_{i-1,0}' (g_i^{-1} \cdots g_{n-1}^{-1}g_ng_{n-1} 
                    \cdots g_i)d_{n+2} \cdots d_{n+m}).\end{eqnarray*}
Now $g_{n-1} \cdots g_{i}$ commutes with all terms to the right of it,
by Lemma~2.3(a). Hence we conclude that
\[ \tau(S_2)= \tau((g_{n-1} \cdots g_i)ht_{i-1,0}' (g_i^{-1} 
         \cdots g_{n-1}^{-1})g_nd_{n+2} \cdots d_{n+m}). \]
We write the argument of $\tau$ as $h'g_nd_{n+2} \cdots 
d_{n+m}$ with $h' \in H_n$. Since this element lies in $H(\leq N-1)$
we can use induction to deduce that 
\[\tau(S_2)=\tau(h'g_nd_{n+2} \cdots d_{n+m})= 
z\tau(h'd_{n+2} \cdots d_{n+m}).\]
Now we observe that $h'$ is a conjugate of $ht_{i-1,0}'$ and the conjugating
element $g_{n-1} \cdots g_i$ commutes with $d_{n+2} \cdots d_{n+m}$, again
using Lemma~2.3(a). Thus, we finally compute that
\[\tau(S_2) = z \tau(ht_{i-1,0}'d_{n+2} \cdots d_{n+m}).\]
Now we follow the same procedure with $S_3$ and find that
\begin{eqnarray*}
\tau(S_3) & = & \tau(h (g_n \cdots g_{i+1}g_ig_{i+1}^{-1} \cdots g_n^{-1})
                                    t_{i-1,0}'d_{n+2} \cdots d_{n+m}) \\
    & = & \tau(h (g_i^{-1}  \cdots g_{n-1}^{-1}g_ng_{n-1} 
                            \cdots g_i)t_{i-1,0}'d_{n+2} \cdots d_{n+m}).
\end{eqnarray*}
Now we  would like  to  interchange $t_{i-1,0}'$  and $d_{n+2}  \cdots
d_{n+m}$ but  this   is   not  necessarily possible   on   the algebra
level.  However, it still works  modulo the kernel  of  $\tau$, as the
following   argument shows.   We  write  $t_{i-1,0}'=x^{-1}tx$   where
$x=g_1^{\pm 1} \cdots g_{i-1}^{\pm  1}$.  By Lemma~2.3(a), the element
$x$ will commute with $d_{n+2} \cdots d_{n+m}$.  The next factor, $t$,
only commutes with $d_{n+2}  \cdots d_{n+m}$ up to (possibly) changing
some  inverses. Thus, the  term  on the right   hand side of the above
equality is equal to
\[ \tau(tx h (g_i^{-1} \cdots g_{n-1}^{-1}g_ng_{n-1} 
                         \cdots g_i)x^{-1}d_{n+2}' \cdots d_{n+m}'),\]
for some $d_{n+2}' \in {\cal D}_{n+2,0}',\ldots, d_{n+m}' 
\in {\cal D}_{n+m,0}'$. Now we can apply our inductive hypothesis to 
conclude that this equals
\[ \tau(tx h (g_i^{-1} \cdots g_{n-1}^{-1}g_ng_{n-1} 
                         \cdots g_i)x^{-1}d_{n+2} \cdots d_{n+m}).\]
Now, again by Lemma~2.3(a), the element $x^{-1}$ will commute with the
terms to the right of it. So, finally, we obtain that
\[ \tau(S_3) = \tau(t_{i-1,0}'h (g_i^{-1} \cdots g_{n-1}^{-1}g_ng_{n-1} 
                         \cdots g_i)d_{n+2} \cdots d_{n+m}).\]
Once more, we use Lemma~2.3(a) to conclude that $g_{n-1} \cdots g_i$ 
commutes with all terms to the right of it. So we arrive at the equality
\[ \tau(S_3)=\tau((g_{n-1} \cdots g_i)t_{i-1,0}'h 
(g_i^{-1} \cdots g_{n-1}^{-1}) g_nd_{n+2} \cdots d_{n+m}).\]
In this situation, we can argue similarly as in the evaluation
of $\tau(S_2)$. This evaluation will result in  an analogous expression as 
before, but with the terms $h$ and $t_{i-1,0}'$ interchanged. Thus, we
conclude that
\[\tau(S_3)=z\tau(t_{i-1,0}'hd_{n+2} \cdots d_{n+m}).\] Arguing as above,
we see that $t_{i-1,0}'$ and $d_{n+2} \cdots d_{n+m}$ can be 
interchanged modulo the kernel of $\tau$.  So, eventually, we find that
$\tau(S_2)=\tau(S_3)$ and, hence, that $\tau(hT_{n+1,i}d_{n+2} \cdots
d_{n+m})=\tau(hT_{n+1,i-1}d_{n+2} \cdots d_{n+m})$, as required. The proof 
of the assertion of Step~1 is now completed by repeating the whole process 
with $T_{n+1,i-1}$ and so on, until all inverses are fixed.

\medskip
{\em  Step~2.} Now  we  consider  the   case where $h=d_1^{*}   \ldots
d_n^{*}$, for some $d_i^{*} \in {\cal D}_{i,0}'$. As before, let $d_i$
be the  element of ${\cal  D}_i'$ corresponding to $d_i^{*}$ where all
inverses  (if any) are  in the right position.  Using Step~1, we first
see   that   $\tau(d_1^{*}    \cdots  d_{n+m}^{*})=   \tau(d_1  \cdots
d_{n+m})$. Now, we will prove that
\[\tau(d_1^{*}\cdots d_{n+m}^{*})=z^a y_{b},\] where 
$a=a(d_1 \cdots d_{n+m})$  and $b=b(d_1 \cdots d_{n+m})$. (Note  that,
in the  definition  of $a,b$ in Lemma~4.2(b),   it does not   matter  
whether we  take $d_i^{*}$ or $d_i$.)  As explained in (2.4),  (3.3), the  
element $d_1 \cdots d_{n+m}$ can be regarded as a  product of positive and 
negative blocks. If this element is equal to $g_C$ for some conjugacy class 
$C$ then we are done by the  defining equation for $\tau$.  If this is not
the case, then some positive block is followed by a negative block or
some  negative    block is followed  by   a  strictly shorter negative
block. We   can  then  use Lemma~2.5 to     conjugate our  element  to
${d_1'} \cdots {d_{n+m}'}  \in H_n(\leq N-1)$ with ${d_i'}
\in  {\cal D}_{i,0}'$ and  with   the same  signed block structure  as
before, that is,  the values of  $a$ and $b$ haven't changed after this
conjugation. Thus, we conclude that
\[ \tau(d_1^{*} \cdots d_{n+m}^{*}) = \tau(d_1 \cdots d_{n+m}) 
  = \tau({d_1'} \cdots  {d_{n+m}'}) = z^ay_b,\] where the last
equality is by induction on $N$.  Our claim is proved.

\medskip
{\em Step 3.} Finally, let $h \in H_n$ and
$d_{n+i}^{*} \in {\cal D}_{n+i,0}'$ for $2 \leq i \leq m$. Now, we show
that \[ \tau(hg_nd_{n+2}^{*}d_{n+3}^{*} \cdots d_{n+m}^{*}) = 
z\tau(hd_{n+2}^{*} \cdots d_{n+m}^{*}). \]
Using Step~1, we have that $\tau(hg_nd_{n+2}^{*} \cdots d_{n+m}^{*})=
\tau(hg_nd_{n+2} \cdots d_{n+m})$ where $d_{n+i} \in {\cal D}_{n+i}'$ 
corresponds to $d_{n+i}^{*}$ as above. Using Corollary~3.5, the latter 
trace is equal to
\[\sum_{(r,d_1^{*},\ldots,d_{n}^{*}) \in I(h)} r\tau(d_1^{*}\cdots d_n^{*}
g_nd_{n+2}^{*}  \cdots  d_{n+m}^{*}),\]  for  some $d_{n+2}^{*} \in {\cal
D}_{n+2,0}',\ldots,d_{n+m}^{*} \in  {\cal D}_{n+m,0}'$ (depending   on
the various elements in $I(h)$).   Let  us consider  one term in  this
sum,  corresponding to   $(r,d_1^{*},  \ldots,d_n^{*}) \in   I(h)$. 
We shall write $d_1^{*} \cdots   d_n^{*}  
g_nd_{n+2}^{*}  \cdots  d_{n+m}^{*}$  in   the  form
$h_1g_nh_2$. Let $a=a(h_1g_nh_2)$, $b=b(h_1g_nh_2)$  and
$a'=a(h_1h_2)$, $b'=b(h_1h_2)$.  Then, clearly,  $a'=a-1$  and $b=b'$.
Using this and Step~2, the value of $\tau$ on our element is given by
\[ rz^ay_{b}=rz^{a'}y_{b'}z.\]
Thus, for each term in the above sum, we obtain a factor $z$ as the
expense of cancelling the factor $g_n$ in that term. We conclude that
\[ \tau(hg_nd_{n+2}^{*} \cdots d_{n+m}^{*})=
z\tau(hd_{n+2}^{*} \cdots d_{n+m}^{*}).\]
The proof is complete.  \end{pf}

\medskip
4.4. In the course of the above proof, we have shown the following remarkable
property of a Markov trace $\tau$.

\medskip
\noindent {\em  Let $h \in H_n$  and $d_{n+1}^{*}  \in {\cal D}_{n+1,0}',
\ldots, d_{n+m}^{*} \in {\cal D}_{n+m,0}'$ for some $m \geq 1$. Then
\[ \tau(hd_{n+1}^{*} \cdots d_{n+m}^{*})=\tau(hd_{n+1} \cdots d_{n+m}),\] 
where, as before, $d_i$ is the element in ${\cal D}_i'$ corresponding 
to $d_i^{*}$.}
\medskip

For $h \in H_n$ let $I(h)$ be the corresponding set given by
Proposition~3.4. For each $i=(r,d_1^{*},\ldots,d_n^{*}) \in I(h)$ we
write $r(i)=r$, $a(i)=a(d_1 \cdots d_n)$ and $b(i)=b(d_1 \cdots d_n)$. Then
the above property in combination with Proposition~3.4 and Lemma~4.2 yields 
the following rule for computing $\tau(h)$.
\[ \tau(h)=\sum_{i \in I(h)} r(i) z^{a(i)}y_{b(i)}.\]
Note that an algorithm for computing $I(h)$ is given by the inductive
proof of Proposition~3.4.

\addtocounter{thm}{1}
\begin{prop}
Let $z,y \in A$ and $\tau:H \rightarrow A$ be a Markov trace with
parameter $z$ and such that $\tau(t_0't_1' \cdots t_{k-1}')=y^{k}$ 
for all $k \geq 1$. Then \[ \tau(ht_{n,0}')=y\tau(h) \quad 
\mbox{ for all $n \geq 0$ and $h \in H_n$}.\]
\end{prop}

\begin{pf} Following the steps in the proof of Theorem~4.3 we see that
it is sufficient to consider the case where $h=d_1^{*} \cdots d_n^{*}$
with $d_i^{*} \in {\cal D}_{i,0}'$ for all~$i$. The result in this
case follows from Lemma~4.2. \end{pf}

\begin{rems}{\rm  (a) Given elements $z,y  \in  A$, the  existence of a  Markov 
trace
$\tau= \tau_{z,y}$ as in the previous Proposition can also be proved
along the lines of the approach followed by  Jones \cite{Jones}, \S 5,
in the proof of Ocneanu's  Theorem for Iwahori-Hecke algebras of  type
$A_n$. Such a  proof is sketched in \cite{L2}  (see also \cite{L1}, \S
3.3). It is based on the observation that, for all $n \geq 0$, the map
\[ C_n: H_n \oplus H_n \oplus H_n \otimes_{H_{n-1}} H_n \longrightarrow 
H_{n+1}, \quad  a+b+c \otimes  d  \mapsto a+bt_n'+cg_nd \] defines  an
isomorphism  of $(H_n,H_n)$-bimodules.   Analogously to  the  proof of
\cite{Jones}, (5.1),  we  can now   define  an $A$-linear  map  $\tau$
inductively   on  $H=\bigcup_{n}   H_n$   by  the rules:  $\tau(1)=1$,
$\tau(bt_n')=y\tau(b)$  and $\tau(cg_nd)=z\tau(cd)$  where  $b,c,d \in
H_n$  and $n \geq  0$.  It   follows easily  that  this map  satisfies
conditions (2) and  (3) of Definition 4.1, and  the problem then is to 
show that (1) holds, that is, to show that $\tau$ is a trace function. 
This verification is a lengthy and tedious calculation  that we do not 
want to reproduce here. We do not see, however,  how this method could 
be modified so as to give an alternative  proof  of  our more  general
Theorem~4.3, too. Yet another construction of the trace in \cite{L2} was given by 
T.~tom
Dieck in \cite{tD} using Turaev's $R$--matrix approach (see \cite{T2}). It would be
interesting to find such an $R$--matrix interpretation of our more general traces in
Theorem 4.3, too.

\medskip
\noindent (b) For the definition of Markov traces it doesn't matter
whether we use the elements $t_i$ or $t_i'$ in the signed block form
of elements. From Theorem~4.3 we see that this only plays a role
in the formulation of the {\em initial conditions} determining the trace,
and it would not be clear how to do this in terms of the elements $t_i$.
This gives an explanation for using $t_i'$ rather than $t_i$.}
\end{rems}

4.7. We can use the results of this section to obtain a classification
of Markov traces for Iwahori--Hecke algebras of type~$D$, in the following
way. First note that if we define $u:=ts_1t$ then the elements $u,s_1,
\ldots,s_{n-1}$ generate a subgroup $W_n' \subset W_n$ which is the
finite Coxeter group of type~$D_n$ with relations given by the following diagram.

\begin{picture}(300,50)
\put(  0, 20){$(D_{n})$}
\put( 52, 38){\circle*{5}}
\put( 52,  2){\circle*{5}}
\put( 52, 38){\line(1,-1){16}}
\put( 52,  2){\line(1,1){16}}
\put( 70, 20){\circle*{5}}
\put( 70, 20){\line(1,0){30}}
\put( 100, 20){\circle*{5}}
\put( 100, 20){\line(1,0){20}}
\put(130, 20){\circle*{1}}
\put(140, 20){\circle*{1}}
\put(150, 20){\circle*{1}}
\put(160, 20){\line(1,0){20}}
\put(180, 20){\circle*{5}}
\put( 38, 37){$u$}
\put( 36,  1){$s_1$}
\put( 67, 30){$s_2$}
\put( 97, 30){$s_3$}
\put(177, 30){$s_{n-1}$}
\put(250, 20){$n \geq 2$}
\end{picture}

\noindent We shall use the convention that $W_1'=\{1\}$.

The above embedding also works on the level of the Iwahori--Hecke algebras if
we let $Q=1$. Indeed, denoting $u:=tg_1t \in H_n$ in this case, we compute
that $u^2=(q-1)u+q \cdot 1$. Thus, the elements $u,g_1,\ldots,g_{n-1}$
generate a subalgebra $H_n' \subset H_n$ which is the Iwahori--Hecke algebra
of type~$D_n$. As in the $B$-type case, we have embeddings $W_1' \subset W_2'
\subset \ldots$ and $H_1' \subset H_2' \subset \ldots$, and we denote $H':=
\bigcup_{n \geq 1} H_n'$. In analogy to Definition~4.1 we say that a trace 
function $\tau:H' \rightarrow A$ is a Markov trace with parameter $z \in A$ if
$\tau(1)=1$ and $\tau(hg_n)=z\tau(h)$ for all $n \geq 1$ and $h \in H_n'$. Now 
we can state (for the proof see \cite{G}, Section~6):
\begin{itemize}
\item[(a)] {\em Every Markov trace on $H'$ is the restriction of a Markov
trace on~$H$ (with the same parameter~$z \in A$).}
\item[(b)] {\em A Markov trace $\tau$ on $H'$ (with parameter~$z \in A$) is
uniquely determined by its values on the elements in the set 
\[ \{u_1' \cdots u_{2k-1}' \mid k=1,2,\ldots \}\]
where $u_i':=g_i \cdots g_2ug_1^{-1}g_2^{-1} \cdots g_i^{-1}$ for all~$i \geq 1$.}
\end{itemize}
The elements $u_i'$ play an analogous role as the elements $t_i'$ in the 
$B$-type case. Note that under the above embedding $H' \subset H$ we have
$u_i'=tt_i'$ for all $i \geq 1$.
