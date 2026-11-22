---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-000-1-introductory-remarks-on-knots-braids-and-trace
section_title: "Introductory remarks on knots, braids and trace functions"
section_number: 1
pages: 1-4
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.979
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 6 sections: Front matter; Introductory remarks on knots, bra; Computations in the braid group of"
---
In  classical knot theory we  study knots inside the $3$-sphere modulo
isotopy.   Using the Alexander and Markov  theorem,  we can translate
this into a purely  algebraic setting in terms  of Artin  braid groups
modulo an equivalence  relation generated  by  `Markov moves'  (one of
which   is usual  conjugation  inside  the   braid
group).    V.F.R.\  Jones \cite{Jones} used  this    fact  in 1984 for
constructing   a new knot   invariant  through trace functions  on the
associated Iwahori-Hecke  algebras of type  $A$  with suitable 
properties that reflect  the  above  Markov moves.  

Jones's work led to  questions of developing knot theory corresponding
to other types of Coxeter groups. It is proved
in \cite{L1}  that there exist braid   structures related to arbitrary
3-manifolds, which   in  addition  satisfy  appropriate Markov-isotopy
equivalence; also that, if the 3-manifold is a solid torus,
then  the sets of  related braids form groups, which   are in fact the
Artin-Tits braid groups related  to the $B$-type Coxeter groups. These
results together with a linear  trace that we  found in 1991 are
used  in  \cite{L2} for constructing    a  4-variable analogue of  the
homfly-pt (2-variable Jones)   polynomial for oriented knots  inside a
solid torus.  We proved the existence of this trace (see \cite{L2}) by
following and adapting   to the $B$-type  case  Jones's proof of   the
existence of Ocneanu's trace in \cite{Jones}, Theorem~5.1.

\bigbreak
The aim of this  paper is to give a  full classification of  {\it all}
linear traces on Iwahori-Hecke algebras  of type $B$ which support the
{\it Markov property}, see  Definition~4.1 and Theorem~4.3.  This uses
in an essential way the results in  \cite{GP} about trace functions on
arbitrary  Iwahori-Hecke  algebras associated  with   finite   Coxeter
groups.  This method yields an  alternative proof of  the above
special trace (cf.\ also  \cite{GP}, (4.2), where an alternative proof
for Ocneanu's original trace is given.) 

In Section~5 we  discuss  the knot  theory of a   solid torus  and  we
explain why the related braid groups are in fact the Artin-Tits groups
of $B$-type.  We also give the  Markov equivalence of these braids, so
that the equivalence classes correspond bijectively to isotopy classes
of knots  in  the solid torus (detailed  account  and proofs of  these
results     can be  found  in   \cite{L1}  or  \cite{L2}). The  Markov
equivalence is in   terms of two   isotopy moves  which are  reflected
precisely in  the definition of the  Markov  property for  our traces.
Then we normalize  properly the constructed traces  in order to obtain
{\it all} homfly-pt analogues   related to the  $B$-type Iwahori-Hecke
algebras,    for    oriented    knots  inside  the   solid
torus.  Finally, we give the  skein rules  and initial conditions that
characterize these invariants diagramatically.

In \cite{G} the first author uses the results of this paper to provide a full
classification of Markov traces for  Iwahori-Hecke algebras of  type $D$ (see 4.7
for precise statement of the main result).  Moreover, in a  further  `vertical' 
development  (cf. \cite{L3}) the second author considered {\it all} Hecke-type
quotients of  the Artin-Tits  braid   group of $B$-type  and  constructed Markov
traces and knot  invariants on all levels, the  basic  level being the Iwahori-Hecke
algebras of $B$-type and the results in \cite{L2}.

\bigbreak We shall now explain  in more detail  our results.  Let us
consider the following Dynkin diagram.

\begin{picture}(300,50)
\put(  0, 20){$(B_{n})$}
\put( 40, 20){\circle*{5}}
\put( 40, 18){\line(1,0){20}}
\put( 40, 22){\line(1,0){20}}
\put( 60, 20){\circle*{5}}
\put( 60, 20){\line(1,0){30}}
\put( 90, 20){\circle*{5}}
\put( 90, 20){\line(1,0){20}}
\put(120, 20){\circle*{1}}
\put(130, 20){\circle*{1}}
\put(140, 20){\circle*{1}}
\put(150, 20){\line(1,0){20}}
\put(170, 20){\circle*{5}}
\put( 37, 30){$t$}
\put( 57, 30){$s_1$}
\put( 87, 30){$s_2$}
\put(167, 30){$s_{n-1}$}
\put(250, 20){$n \geq 1$}
\end{picture}

\noindent The symbols $t,s_1,\ldots,s_{n-1}$ labelling the nodes form
generators for  the corresponding Artin-Tits braid group $\tilde{W}_n$
and the finite Coxeter group $W_n$ of type $B_n$. The braid group 
$\tilde{W}_n$ has the defining relations 
\[\begin{array}{rclll}
s_1ts_1t & = & ts_1ts_1  & & \\
ts_i & = & s_it & \mbox{ if } & i>1 \\
s_is_j & = & s_js_i & \mbox{ if } & |i-j|>1 \\
s_is_{i+1}s_i & = & s_{i+1}s_is_{i+1} & \mbox{ if } & 1 \leq i \leq n-2
\end{array}\]
Relations of these  types will  be called {\it  braid relations}.   As
proved in \cite{L1} the elements  of $\tilde{W}_n$ can be  represented
geometrically by braids in  $S^3$ on $n+1$ strands  in which the first
strand remains  pointwise  fixed.  When  we  refer to  this  geometric
interpretation of $\tilde{W}_n$ we shall denote it by $B_{1,n}$. Below
we illustrate the generators $s_i, t$ and the element $t_i'=s_i \cdots
s_1ts_1^{-1} \cdots s_i^{-1}$ in $B_{1,n}$, and  also an example of an
element in $B_{1,5}$.

 $\vbox{\picill8inby1.75in(mein1)  }$

\noindent If in addition to the braid relations we impose the quadratic
relations that  each generator has order~$2$, then  we obtain the finite factor
group  $W_n$. 
\bigbreak
The corresponding Iwahori-Hecke
algebra $H_n$ is obtained as a   quotient of the group  algebra   of $\tilde{W}_n$
by factoring out the quadratic  relations  
\[ t^2=(Q-1)t+Q \cdot 1  \quad \mbox{ and } \quad g_i^2=(q-1)g_i+q \cdot 1 
\mbox{ for all $i$},\]  
where we denote the image of $s_i$ in  $H_n$ simply by $g_i$, and where $q, Q$ are
fixed parameters from the ground ring. The  algebra $H_n$ is finite-dimensional,
with a basis $\{g_w\}$ labelled by the elements of $W_n$. Now the idea  is to
construct invariants  of knots in the solid torus using trace    functions on
$\tilde{W}_n$  which  factor through $H_n$ and which   respect  the braid
equivalence on  $\tilde{W}_n$. The latter is generated by the following two moves 
(cf.\ Theorem~5.2).  \begin{itemize}
\item[(i)] Conjugation: if $\alpha,\beta \in \tilde{W}_n$
then $\alpha \sim \beta ^{-1}\alpha\beta$.
\item[(ii)] Markov moves: if $\alpha \in \tilde{W}_n$ then $\alpha \sim
\alpha{s_n}^{\pm 1}\in \tilde{W}_{n+1}$. 
\end{itemize} 
\noindent Thus, the problem is  reduced to studying trace
functions $\tau$ on $H:= \bigcup_{n=1}^{\infty} H_n$ which  satisfy the rule 
$\tau(hg_n)=z\tau(h)$, where $z$ is a fixed parameter  in the ground  ring over
which the algebra $H$ is defined, and $h \in H_n$. (Note that such an $h$ is  a
linear combination of basis elements $g_w$ which do  not involve the  generator
$g_n$.) This rule is what  we call `the Markov property' for trace functions on
$H$.
\bigbreak
A general  scheme for constructing  trace functions on $H_n$ (in fact,
for  Iwahori-Hecke algebras of any given  type)  has been developed in
\cite{GP}. Firstly, it is known that any trace is determined by its values on basis
elements corresponding to a set of representatives of the conjugacy classes of
$W_n$. However, it is not true in general that basis elements
 corresponding to conjugate group elements are also conjugate in the algebra, and so,
to compute the trace of an arbitrary element is no more a trivial task.  In
\cite{GP}, there is an explicit algorithm  for computing the value of a given trace
on an arbitrary basis element $g_w$ from the values on basis elements corresponding
to elements  of {\it minimal length} in the various conjugacy classes. 
\bigbreak
\noindent In $W_n$, let
$t_i:=s_i \cdots s_1t s_1 \cdots s_i$ and let a
positive, respectively  negative,  block be an element of the form
\[s_{i+1}s_{i+2}\cdots s_{i+m} \quad \mbox{ respectively } \quad
t_i s_{i+1} \cdots s_{i+m}, \quad \mbox{ where } m,i\geq 0.\]
Then an element of minimal length in a conjugacy class is a  product of negative
blocks ordered by increasing length, followed by various positive blocks also in 
increasing  length (for example, $t t_1s_2 t_3s_4 s_6 s_8s_9s_{10} \in W_{11}$). The
main idea of this paper is that, in order to determine the  
 Markov traces on  $H$, we lift the elements $t_i$ in $W_n$ to  the elements
$t'_i:=g_i \cdots g_1t g_1^{-1} \cdots g_i^{-1}$ in $H_n$ (instead of the obvious
lifting to $g_i \cdots g_1t g_1 \cdots g_i$). This will enable us to
parametrize in Section 4 all possible Markov traces with parameter~$z$  by the
initial conditions  \[ \tau(t_0't_1't_2' \cdots t_{k-1}')=y_k \quad \mbox{ for all
$k \geq 1$,}\] where $y_1,y_2 \ldots$ are arbitrary elements from the ground ring. In
particular, if $h=d_1 \cdots d_n \in H$ with $d_i \in \{1, g_{i-1}, t_{i-1}'
\}$, a lifting of a minimal length representative, we define a  trace function
$\tau$ on $H$ by the rule $ \tau(h)=z^{a(h)} y_{b(h)},$ where $a(h)$  is the 
 number of $d_i$ which are  in  the set $\{g_1,\ldots,g_{n-1}\}$ and $b(h)$ is the
number  of $d_i$ which are of the form $t_i'$ (cf. Theorem 4.3). From our definition 
it is clear that $\tau$ satisfies  the Markov property for  these
elements,  and the  problem is then to show that this  property holds on
all elements of $H$. This will require some technical preliminaries which  
are provided in Sections~2 and~3. The final proof will then be given in Section~4.
