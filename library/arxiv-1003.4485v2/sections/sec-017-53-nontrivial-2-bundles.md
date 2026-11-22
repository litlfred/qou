---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-017-53-nontrivial-2-bundles
section_title: "Nontrivial 2-Bundles"
section_number: 5.3
pages: 47-60
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.538
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{nontrivial}

So far we have implicitly been looking at 2-connections on trivial
2-bundles.  This is fine locally.  But there are also interesting
issues involving nontrivial 2-bundles, which become crucial when we
work globally.   

A careful treatment of 2-bundles would require some work, and the
reader interested in this topic would do well to start with Moerdijk's
introductory paper on `stacks' and `gerbes' \cite{Moerdijk}.  Here we
take a less sophisticated approach: we simply describe how to build a
principal 2-bundle and put a 2-connection on it.  Since we do not say
when two principal 2-bundles built this way are the `same', our treatment
is incomplete.  The reader can find more details elsewhere
\cite{BaezStevenson, BJ, Bartels:2004, Breen:2006, Breen:2008,
BreenMessing, SchreiberWaldorf:gerbes}.  We warn the reader that
almost every paper in the literature uses different notation, sign
conventions, and so forth.  
 
First recall ordinary gauge theory: suppose $G$ is a Lie group and $M$
a manifold.  In this case we can build a principal $G$-bundle over $M$
using transition functions.  First, write $M$ as the union of open
sets or \define{patches} $U_i \subseteq M$:
\[ M = \bigcup_i U_i. \]
Then, choose a smooth \define{transition
function} on each double intersection of patches:
\[ g_{ij} \maps U_i \cap U_j \to G .\]
These transition functions give gauge transformations.  We can build a
principal $G$-bundle over all of $M$ by gluing together trivial bundles
over the patches with the help of these gauge transformations.
However, this procedure will only succeed if the transition functions
satisfy a consistency condition on each triple intersection:
\[ g_{ij}(x) g_{jk}(x) = g_{ik}(x) \]
for all $x \in U_i \cap U_j \cap U_k$.  This equation is called a
\define{cocycle condition}.  We can visualize it as a triangle:
\[
\xy 
(0,0)*+{\bullet}="1"; 
(-12,-20.78)*+{\bullet}="2"; 
(12,-20.78)*+{\bullet}="3"; 
{\ar^-{g_{ik}} "3";"2"}; 
{\ar_-{g_{jk}} "3";"1"}; 
{\ar_-{g_{ij}} "1";"2"}; 
\endxy
\]
where we suppress the variable $x$ for the sake of readability.
The idea is that this triangle should `commute': the direct way
of identifying points in the trivial bundle in the $i$th patch 
to points in the trivial bundle over the $k$th patch should match 
the indirect way which proceeds via the $j$th patch.

A similar but more elaborate recipe works for higher gauge theory.
Now let $\G$ be a Lie 2-group with crossed module
$(G, H, t, \alpha)$.  To build a $\G$-2-bundle, we start by
choosing transition functions on double intersections of patches:
\[ g_{ij} \maps U_i \cap U_j \to G \]
However, now it makes sense to replace the equation in
the cocycle condition by a 2-morphism!  So, for each triple 
intersection we choose 2-morphisms
in $\G$:
\[ \gamma_{ijk}(x) \maps g_{ij}(x) \, g_{jk}(x) \Rightarrow g_{ik}(x) \]
depending smoothly on $x \in U_i \cap U_j \cap U_k$.   We can again
visualize these as triangles:
\[
\xy 
(0,0)*+{\bullet}="1"; 
(-12,-20.78)*+{\bullet}="2"; 
(12,-20.78)*+{\bullet}="3"; 
{\ar^-{g_{ik}} "3";"2"}; 
{\ar_-{g_{jk}} "3";"1"}; 
{\ar_-{g_{ij}} "1";"2"}; 
{\ar@2{->}^-{\gamma_{ijk}} (0,-7)*{};(0,-18)*{}};
\endxy
\]
But now we demand that these 2-morphisms themselves obey
a cocycle condition on quadruple intersections of patches.  
As we ascend the ladder of higher gauge theory, triangles become
tetrahedra and then higher-dimensional simplexes.  In this case, the
cocycle condition says that this tetrahedron commutes:
\[
{\xy 
(15,-15)*+{\bullet}="1"; 
(15,15)*+{\bullet}="2"; 
(-15,15)*+{\bullet}="3"; 
(-15,-15)*+{\bullet}="4"; 
(0,0)*+{}="0"; 
{\ar_-{g_{kl}} "1";"2"}; 
{\ar_-{g_{jk}} "2";"3"}; 
{\ar_-{g_{ij}} "3";"4"};
{\ar^-{g_{il}} "1";"4"};
{\ar@{.}_(0.5){\tiny{g_{ik}}} "2";"0"};
{\ar@{.>} "0";"4"};
{\ar_(0.75){g_{jl}} "1";"3"};
{\ar@2{->}^-{\gamma_{ijl}} (-9.5,-3)*{};(-5.5,-13.5)*{}};
{\ar@2{->}^-{\gamma_{jkl}} (10.5,7.5)*{};(3,0)*{}};
{\ar@2{.>}_-{\tiny{\gamma_{ijk}}} (-10.5,7.5)*{};(-3,0)*{}};
{\ar@2{.>}_-{\tiny{\gamma_{ikl}}} (9.5,-3)*{};(5.5,-13.5)*{}};
\endxy}
\]

\noindent
By saying that this tetrahedron `commutes', we mean that the composite
of the front two sides equals the composite of the back two sides:
\[
{\xy 
(10,-10)*+{\bullet}="1"; 
(10,10)*+{\bullet}="2"; 
(-10,10)*+{\bullet}="3"; 
(-10,-10)*+{\bullet}="4"; 
{\ar_-{g_{kl}} "1";"2"}; 
{\ar_-{g_{jk}} "2";"3"}; 
{\ar_-{g_{ij}} "3";"4"};
{\ar^-{g_{il}} "1";"4"};
{\ar_(0.3){g_{jl}} "1";"3"};
{\ar@2{->}^-{\gamma_{ijl}} (-5,-2)*{};(-3,-9)*{}};
{\ar@2{->}_-{\gamma_{jkl}} (7,7)*{};(2,2)*{}};
\endxy}
\quad = \quad
{\xy 
(10,-10)*+{\bullet}="1"; 
(10,10)*+{\bullet}="2"; 
(-10,10)*+{\bullet}="3"; 
(-10,-10)*+{\bullet}="4"; 
{\ar_-{g_{kl}} "1";"2"}; 
{\ar_-{g_{jk}} "2";"3"}; 
{\ar_-{g_{ij}} "3";"4"};
{\ar^-{g_{il}} "1";"4"};
{\ar_{} "2";"4"}; 
(3.5,6)*+{\scriptstyle{g_{ik}}};
{\ar@2{->}_(0.8){\gamma_{ijk}} (-7,7)*{};(-2,2)*{}};
{\ar@2{->}_-{\gamma_{ikl}} (5,-2)*{};(3,-9)*{}};
\endxy}
\]
We need whiskering to compose the 2-morphisms in this diagram, as explained
near the end of Section \ref{2-connections}.  So in equations,
the tetrahedral cocycle condition says that:
\[
\gamma_{ijl} \cdot (g_{ij} \circ \gamma_{jkl}) = 
 \gamma_{ikl} \cdot (\gamma_{ijk} \circ g_{kl}) 
\]
where $\cdot$ stands for vertical composition and $\circ$ stands
for whiskering.

We can describe this cocycle condition in a more down-to-earth
manner if we use Theorem \ref{crossed_module}, which says that a
2-morphism
\[ \gamma_{ijk} \maps g_{ij} \, g_{jk} \Rightarrow g_{ik} \]
is the same as an element $h_{ijk} \in H$ such that
\[   
t(h_{ijk}) \, g_{ij} \, g_{jk} = g_{ik} .
\]
This theorem also gives formulas for vertical and horizontal 
composition in terms of the groups $G$ and $H$.  Since whiskering by 
a morphism is horizontal composition with its identity 2-morphism, 
we can also express whiskering in these terms.  So,
a little calculation---a wonderful exercise for the 
would-be higher gauge theorist---shows that:
\[
h_{ijl} \; \, \alpha(g_{ij})(h_{jkl}) = h_{ikl} \; h_{ijk} 
\]
where $\alpha$ is the action of $G$ on $H$.  

There is no need to have $g_{ii} = 1$ in this formalism; we should
really choose a 2-morphism from $g_{ii}$ to $1$.  However, without loss 
of generality, we can assume that $g_{ii} = 1$ and set this 2-morphism 
equal to the identity.  We can also assume that $h_{ijk} = 1$ whenever 
two or more of the indices $i,j,k$ are equal.  The reason is that
Bartels \cite{Bartels:2004} has shown that any principal 2-bundle is
equivalent to one for which these simplifying assumptions hold.  
We will make these assumptions in what follows.  For the full story 
without these assumptions, see Schreiber and Waldorf 
\cite{SchreiberWaldorf:gerbes}.

Now consider connections.  Again, it helps to begin by reviewing
the story for ordinary gauge theory.  Suppose we have a manifold $M$
written as a union of patches $U_i$, and suppose we have principal
$G$-bundle over $M$ built using transition functions $g_{ij}$.  To put
a connection on this bundle, we first put a connection on the trivial
bundle over each patch: that is, for each $i$, we choose a $\g$-valued
1-form $A_i$ on $U_i$.  But then we must check to see if these fit
together to give a well-defined connection on all of $M$.  For this,
we need the gauge transform of the connection on the $j$th patch to
equal the connection on the $i$th patch:
\[         A_i = g_{ij} A_j g_{ij}^{-1} + g_{ij} dg_{ij}^{-1}  \]
on each double intersection $U_i \cap U_j$.   

The story is similar for 2-connections.  Suppose we have a principal
$\G$-2-bundle over $M$ built using transition functions $g_{ij}$ and
$h_{ijk}$ as described above.  To equip this 2-bundle with a
2-connection, we first put a 2-connection on the trivial 2-bundle over
each patch.  So, on each open set $U_i$ we choose a $\g$-valued 1-form
$A_i$ and an $\h$-valued 2-form $B_i$ with $\dt(B_i) = F_i$.  But then
we must fit these together to get a 2-connection on all of $M$.

For this, we should follow the ideas from Section \ref{gauge} on how
gauge transformations work in higher gauge theory.  So, we choose
an $\h$-valued 1-form $a_{ij}$ on each double intersection $U_i \cap
U_j$, and require that
\[       
\begin{array}{ccl}
A_i &=& g_{ij} A_j g_{ij}^{-1} \, + \, g_{ij}\, dg_{ij}^{-1} \, + 
\, \dt(a_{ij})  \\  \\
B_i &=& \alpha(g_{ij})(B_j) \, + \, \dalpha(A_i) \wedge a_{ij} \, + \, 
da_{ij} \, - \, a_{ij} \wedge a_{ij} .
\end{array}
\]
These equations say that the 2-connection $(A_i,B_i)$ is a
gauge-transformed version of $(A_j,B_j)$.  The appearance of $A_i$ on
the right-hand side of the second equation is not a typo!  Finally,
the 1-forms $a_{ij}$ must obey a consistency condition on triple
intersections:
\begin{equation}
\label{compatibility}
  h_{ijk}^{-1} \, \dalpha(A_i)(h_{ijk}) \, + \,
   h_{ijk}^{-1} \, dh_{ijk}    \, + \, 
   \alpha(g_{ij})(a_{jk}) \, + \, a_{ij} = 
   h_{ijk}^{-1}\, a_{ik}\, h_{ijk}  
\end{equation}
Where does this consistency condition come from?  Indeed, what does
it even mean?  We have not yet defined `$h^{-1} \dalpha(A)(h)$' when 
$A \in \g$ and $h$ is an element of the group $H$.  

We could systematically derive this condition from a more conceptual
approach to 2-connections \cite{BaezSchreiber,
SchreiberWaldorf:gerbes}, but it will be marginally less stressful to
motivate it as follows.  For every triple intersection $U_i \cap U_j
\cap U_k$ we have three equations relating $A_i, A_j$ and $A_k$:
\[       
\begin{array}{ccl}
A_i &=& g_{ij} A_j g_{ij}^{-1} \, + \, g_{ij}\, dg_{ij}^{-1} \, + 
\, \dt(a_{ij}) \\   \\
A_j &=& g_{jk} A_k g_{jk}^{-1} \, + \, g_{jk}\, dg_{jk}^{-1} \, + 
\, \dt(a_{jk}) \\   \\
A_k &=& g_{ki} A_i g_{ki}^{-1} \, + \, g_{ki}\, dg_{ki}^{-1} \, + 
\, \dt(a_{ki}) 
\end{array}
\]
The first equation expresses $A_i$ in terms of $A_j$.
We can substitute the second equation in the first to get a formula for 
$A_i$ in terms of $A_k$.  Then we can use the third equation
to get a formula for $A_i$ in terms of itself!  We would like to
be able to simplify this formula to get simply $A_i = A_i$.  
The consistency condition, Equation (\ref{compatibility}), ensures that
we can do this.

This calculation is a bit of a workout; let us see how it goes.
We begin by doing the substitutions:
\[
\begin{array}{ccl}
A_i &=& g_{ij} A_j g_{ij}^{-1} \, + \, g_{ij}\, dg_{ij}^{-1} \, + 
\, \dt(a_{ij}) \\   \\
    &=& g_{ij} \left(g_{jk} A_k g_{jk}^{-1} \, + \, g_{jk}\, dg_{jk}^{-1} \, + 
\, \dt(a_{jk}) \right) g_{ij}^{-1} \, + \, g_{ij}\, dg_{ij}^{-1} \, + 
\, \dt(a_{ij}) \\   \\
    &=& g_{ij} \left(g_{jk} \left( g_{ki} A_i g_{ki}^{-1} + 
g_{ki} dg_{ki}^{-1}  + \dt(a_{ki})  \right) g_{jk}^{-1} + 
g_{jk}\, dg_{jk}^{-1} + \dt(a_{jk}) \right) g_{ij}^{-1}  + \\  
&& g_{ij}\, dg_{ij}^{-1} \, + \, \dt(a_{ij}) .
\end{array}
\]
Then we do a bit of simplification:
\[  
\begin{array}{ccl}
A_i &=& g_{ij} g_{jk} g_{ki} A_i (g_{ij} g_{jk} g_{ki})^{-1} \, + \,
g_{ij} g_{jk} g_{ki} d(g_{ij} g_{jk} g_{ki})^{-1} \, +  \\
&& g_{ij} g_{jk}  \dt(a_{ki})  (g_{ij} g_{jk})^{-1} \, + \,
g_{ij} \dt(a_{jk}) g_{ij}^{-1} \, + \, \dt(a_{ij}) .
\end{array}
\]
Since $t(h_{ijk}) \, g_{ij} \, g_{jk} = g_{ik}$ and by our assumptions
 $g_{ik}^{-1} = g_{ki}$, we have
\[   g_{ij} g_{jk} g_{ki} = t(h_{ijk})^{-1}   \]
so
\begin{equation}
\label{step1}
\begin{array}{ccl}
0 &=& t(h_{ijk})^{-1} \, A_i \, t(h_{ijk}) - \, A_i \, + \,  
         t(h_{ijk})^{-1} \, dt(h_{ijk})    \, +  \\  
&& t(h_{ijk})^{-1} g_{ik} \dt(a_{ki}) g_{ik}^{-1} t(h_{ijk})  \, + \,
g_{ij} \dt(a_{jk}) g_{ij}^{-1} \, + \, \dt(a_{ij}) .
\end{array}
\end{equation}

Now, if $G$ is a matrix group, we can freely multiply group elements
and Lie algebra elements.  Then for any $h \in H$ and $A \in \g$ we
have
\begin{equation}
\label{step2}
   t(h)^{-1} A t(h) \, - \, A =  t(h)^{-1} [A, t(h) ] .
\end{equation}
This will allow us to simplify the first two terms in Equation (\ref{step1}).
Moreover, for any $g \in G$, $h \in H$ we have
\[    t(h^{-1} \alpha(g) h) = t(h)^{-1} t(\alpha(g)(h)) = 
      t(h)^{-1} g t(h) g^{-1}  .\]
Taking $g = \exp(s A)$ for $A \in \g$ and differentiating 
this equation with respect to $s$ at $s = 0$, we get
\begin{equation}
\label{step3}
\dt(h^{-1} \dalpha(A)(h)) =  t(h)^{-1} A t(h) \, - \, A 
\end{equation}
where on the left side $\dalpha$ means the derivative of the map
$\alpha \maps G \times H \to H$ with respect to its first argument,
while $\dt$ is the derivative of $t$.  Here are we extending our
previous definitions of $\dalpha$ and $\dt$.  
Combining Equations (\ref{step2}) and (\ref{step3}) we see that
\[       t(h)^{-1} [A, t(h)] =  \dt\left(h^{-1} \dalpha(A)(h)\right)  .\]
In fact this result holds even when $G$ is a non-matrix Lie group, 
as long as we carefully make sense of both sides.

Using this result, we can rewrite Equation (\ref{step1}) as follows:
\[  
\begin{array}{ccl}
0 &=&    \dt(h_{ijk}^{-1} \, \dalpha(A_i)(h_{ijk})) \, + \,
   t(h_{ijk})^{-1} \, dt(h_{ijk})    \, +  \\  
&& t(h_{ijk})^{-1} g_{ik} \, \dt(a_{ki})
   \, g_{ik}^{-1} t(h_{ijk}) \, + \, g_{ij} \, \dt(a_{jk}) \, g_{ij}^{-1} \,
   + \, \dt(a_{ij})
\end{array}
\]
Each term in the above equation is $\dt$ applied to an $\h$-valued 1-form. 
Writing down all these $\h$-valued 1-forms, we see that the above equation 
will be true if this condition holds:
\[  
0 =  h_{ijk}^{-1} \dalpha(A_i) (h_{ijk}) \, + \,
   h_{ijk}^{-1} dh_{ijk}    \, + \,   \\  \\
  h_{ijk}^{-1} \alpha(g_{ik})(a_{ki}) h_{ijk}  \, + \,  
   \alpha(g_{ij})(a_{jk}) \, + \, a_{ij} 
\]
This is our consistency condition in disguise!  To remove the
disguise, let us simplify it a bit further.  When $i = j$ this 
condition reduces to 
\[  
 a_{ik}  \, + \, \alpha(g_{ik})(a_{ki}) = 0.
\]
Reinserting this result we obtain
\[  
\begin{array}{ccl}
0 &=&  h_{ijk}^{-1} \, \dalpha(A_i) (h_{ijk}) \, + \,
   h_{ijk}^{-1} \, dh_{ijk}    \, - \,  
   h_{ijk}^{-1} \, a_{ik} \, h_{ijk}  \, + \, 
   \alpha(g_{ij})(a_{jk}) \, + \, a_{ij}
\end{array}
\]
\emph{Voil\`a!}  This is clearly equivalent to the consistency condition
we stated in the first place, Equation (\ref{compatibility}):
\[  
  h_{ijk}^{-1} \, \dalpha(A_i) (h_{ijk}) \, + \,
   h_{ijk}^{-1} \, dh_{ijk}    \, + \, 
   \alpha(g_{ij})(a_{jk}) \, + \, a_{ij} = 
   h_{ijk}^{-1} \, a_{ik} \, h_{ijk}  
\]

Now let us consider some examples.  Recall from Section \ref{abelian} that
$\mathrm{b}\U(1)$ is 2-group with one morphism and $\U(1)$ as its
group of 2-morphisms.  A \define{\boldmath $\U(1)$ gerbe} is principal
$\mathrm{b}\U(1)$-2-bundle.  Let's look at principal $\U(1)$-bundles
and then $\U(1)$ gerbes, to get a feel for how they are similar and
how they differ.

To build a principal $\U(1)$-bundle with a connection on it, we
choose transition functions
\[         g_{ij} \maps U_i \cap U_j \to \U(1) \]
such that 
\[ g_{ij} g_{jk} = g_{ik} \]
on each triple intersection.  
To put a connection on this bundle, we then choose a 1-form $A_i$ on 
each patch such that
\[ A_i = A_j + g_{ij} dg^{-1}_{ij} \]
on each double intersection $U_i \cap U_j$.  The curvature of 
this connection is then 
\[ F_i = dA_i \]
on the $i$th patch.  Note that $F_i = F_j$ on $U_i \cap U_j$, 
so we get a well-defined curvature 2-form $F$ on all of $M$.

To build a $\U(1)$ gerbe, we choose transition functions 
$h_{ijk} \maps U_i \cap U_j \cap U_k \to \U(1)$ such that
\[  h_{jkl} h_{ijl} = h_{ikl} h_{ijk} \]
on each quadruple intersection.  Remember, the 2-group
$\mathrm{b}\U(1)$ has only one morphism, the identity, so the
transition functions $g_{ij}$ are trivial and can be ignored.  To put
a 2-connection on this gerbe, we must first choose a 2-form $B_i$ on
each patch.  Then we must choose a 1-forms $a_{ij}$ on each double
intersection.  We require that
\[ B_i = B_j + da_{ij}  \]
on each double intersection, and 
\[ a_{ij} + a_{jk} = a_{ik} + h_{ijk} \, dh^{-1}_{ijk} \]
on each triple intersection.   The \define{2-curvature} of this 
2-connection is then
\[ Z_i = dB_i \]
on the $i$th patch.  Note that $Z_i = Z_j$ on $U_i \cap U_j$, so we
get a well-defined 2-curvature 3-form $Z$ on all of $M$. 

There is a nice link between $\U(1)$ gerbes and cohomology, which
in fact is the reason they were invented in the first place.  
For any principal $\U(1)$-bundle with connection, the curvature $F$ is 
\define{integral}:
\[ \int_\Sigma F \in 2\pi \Z \]
for any closed surface $\Sigma$ mapped into $M$. In addition, 
$F$ is closed: 
\[ dF = 0. \] 
Conversely, any closed, integral 2-form $F$ on $M$ is the curvature of
some connection on a principal $\U(1)$-bundle over $M$.  Two different
connections on the same bundle have curvature 2-forms that differ by
an exact 2-form, so we get a well-defined element of the de Rham
cohomology $H^2(M,\R)$ from a principal $\U(1)$-bundle.  This idea can
be refined further, and the upshot is that principal $\U(1)$-bundles
over $M$ are classified by the cohomology group $H^2(M,\Z)$.

Similarly, for any $\U(1)$ gerbe, the curvature 3-form $Z$ is closed 
and integral, where the latter term now means that 
\[ \int_Y Z \in 2\pi \Z \]
for any closed 3-manifold $Y$ mapped into $M$.  Conversely, any such
3-form is the 2-curvature of some 2-connection on a $\U(1)$ gerbe over
$M$---and in fact, $\U(1)$ gerbes over $M$ are classified by
$H^3(M,\Z)$.  

This is just the beginning of a longer tale: namely, the story of
characteristic classes in higher gauge theory \cite{BaezStevenson,SSS}.
Indeed, though higher gauge theory is only in its infancy, there is
much more to say.   But our story ends here.  We invite the reader to 
go further.


\subsection{Acknowledgements}

This paper is based on JH's notes of lectures given by JB 
at the 2nd School and Workshop on Quantum Gravity and Quantum
Geometry, held as part of the 2010 Corfu Summer Institute.  We thank
George Zoupanos, Harald Grosse, and everyone else involved with the
Corfu Summer Institute for making our stay a pleasant and productive
one.  We thank Urs Schreiber for many discussions of higher gauge
theory, and thank Tim van Beek, David Roberts and Elliot Schneider for catching 
some errors.  This research was partially supported by an FQXi grant.
