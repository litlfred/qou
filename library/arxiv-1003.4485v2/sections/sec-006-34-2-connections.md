---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-006-34-2-connections
section_title: "2-Connections"
section_number: 3.4
pages: 21-27
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 1.0
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
A 2-connection is a recipe for parallel transporting both
0-dimensional and 1-dimensional objects---say, particles and
strings.  Just as we can describe a connection on a trivial bundle
using a Lie-algebra valued differential form, we can describe a
2-connection using a \emph{pair} of differential forms.  But there is
a deeper way of understanding 2-connections.  Just as a connection was
revealed to be a smooth functor
\[           \hol \maps \P_1(M) \to G  \]
for some Lie group $G$, a 2-connection will turn out to be a 
smooth 2-functor 
\[   \hol \maps \P_2(M) \to \G \]
for some Lie 2-group $\G$.  Of course, to make sense of this we need
to define a `2-functor', and say what it means for such a thing to be
smooth.

The definition of 2-functor is utterly straightforward: it is 
a map between 2-categories that preserves everything in sight.
So, given 2-categories $C$ and $D$, a \define{2-functor} 
$F \maps C \to D$ consists of:
\begin{itemize} 
\item a map $F$ sending objects in $C$ to objects in $D$, 
\item another map called $F$ sending morphisms in $C$ to 
morphisms in $D$,
\item a third map called $F$ sending 2-morphisms in $C$ to 
2-morphisms in $D$,
\end{itemize}
such that:
\begin{itemize}
\item given a morphism $f \maps x \to y$ in $C$, we have
$F(f) \maps F(x) \to F(y)$, 
\item $F$ preserves composition for morphisms, and identity morphisms:
\[ F(fg) = F(f)F(g) \]
\[ F(1_x) = 1_{F(x)} ,\]
\item given a 2-morphism $\alpha \maps f \To g$ in $C$, we have
$F(\alpha) \maps F(f) \To F(g)$, 
\item $F$ preserves vertical and horizontal
composition for 2-morphisms, and identity 2-morphisms:
\[ F(\alpha \cdot \beta ) = F(\alpha) \cdot F(\beta) \]
\[ F(\alpha \circ \beta ) = F(\alpha) \circ F(\beta) \]
\[ F(1_f) = 1_{F(f)}. \]
\end{itemize}

There is a general theory of smooth 2-groupoids and smooth 2-functors
\cite{BaezSchreiber, SchreiberWaldorf:gerbes}.  But here we prefer to take a more
elementary approach.  We already know that for any Lie 2-group $\G$, the morphisms
and 2-morphisms each form Lie groups. Given this, we can say that for any smooth
manifold $M$, a 2-functor
\[   \hol \maps \P_2(M) \to \G \]
is \define{smooth} if:
\begin{itemize}
\item For any smoothly parametrized family of lazy paths $\gamma_s$
($s \in [0,1]^n$) the morphism $\hol(\gamma_s)$ depends smoothly
on $s$, and
\item For any smoothly parametrized family of lazy surfaces $\Sigma_s$
($s \in [0,1]^n$) the 2-morphism $\hol(\Sigma_s)$ depends smoothly
on $s$.
\end{itemize}

With these definitions in hand, we are finally ready to understand
the basic result about 2-connections.  It is completely analogous to
Theorem~\ref{thm:connections}:

\begin{thm}
\label{thm:2-connections}
For any Lie 2-group $\G$ and any smooth manifold $M$,
there is a one-to-one correspondence between:
\begin{enumerate}
\item 2-connections on the trivial principal $\G$-2-bundle over $M$,
\item pairs consisting of 
a smooth $\g$-valued 1-form $A$ and a smooth $\h$-valued 
2-form $B$ on $M$, such that
\[           \dt(B) = dA + A \wedge A \]
where we use $\dt \maps \h \to \g$, the differential of the map $t \maps
H \to G$, to convert $B$ into a $\g$-valued 2-form, and
\item smooth 2-functors
\[ \hol \maps \P_2(M) \to \G \]
where $\P_2(M)$ is the path 2-groupoid of $M$.
\end{enumerate}
\end{thm}

This result was announced by Baez and Schreiber \cite{BaezSchreiber},
and a proof can be be found in the work of Schreiber and Waldorf
\cite{SchreiberWaldorf:gerbes}.  This work was deeply inspired by
the ideas of Breen and Messing \cite{Breen:2008, BreenMessing}, who
considered a special class of 2-groups, and omitted the equation
$\dt(B) = dA + A \wedge A$, since their sort of connection did not assign
holonomies to surfaces.  One should also compare the closely 
related work of Mackaay, Martins, and Picken \cite{MackaayPicken, 
MartinsPicken:2007}, and the work of Pfeiffer and Girelli 
\cite{Pfeiffer:2003, GirelliPfeiffer:2004}.

In the above theorem, the first item mentions `2-connections' and
`2-bundles'---concepts that we have not defined.  But since we are
only talking about 2-connections on \emph{trivial} 2-bundles, we do
not need these general concepts yet.  For now, we can take the third
item as the definition of the first.  Then the content of the theorem
lies in the differential form description of smooth 2-functors $\hol
\maps \P_2(M) \to \G$.  This is what we need to understand.

A 2-functor of this sort must assign holonomies both to paths and
surfaces.  As you might expect, the 1-form $A$ is primarily
responsible for defining holonomies along paths, while the 2-form $B$
is responsible for defining holonomies for surfaces.  But this is a
bit of an oversimplification.  When computing the holonomy of a surface,
we need to use $A$ as well as $B$! 

Another surprising thing is that $A$ and $B$ need to be related by an
\textit{equation} for the holonomy to be a 2-functor.  If we ponder
how the holonomy of a surface is actually computed, we can see why
this is so.  We shall not be at all rigorous here.  We just want
to give a rough intuitive idea of how to compute a holonomy for a
surface, and where the equation $\dt(B) = dA + A \wedge A $ comes from.
Of course
\[             dA + A \wedge A = F  \]
is just the \emph{curvature} of the connection $A$.  This is a big clue.

Suppose we are trying to compute the holonomy for a surface starting
from a $\g$-valued 1-form $A$ and an $\h$-valued 2-form $B$.  Then
following the ideas of calculus, we can try to chop the surface into
many small pieces, compute a holonomy for each one, and multiply these
together somehow.  It is easy to chop a surface into small squares.
Unfortunately, the definition of 2-category doesn't seem to know
anything about squares!  But this is not a serious problem.  For
example, we can interpret this square:
\[
  \xymatrix{
\bullet & \bullet \ar[l]_{f}="g1"  \\  
\bullet \ar[u]^{h} & \bullet \ar[l]^{k}="g2"  \ar[u]_{g}
\ar@{=>}^{\alpha} "g2"+<1.5ex,7ex>;"g2"+<-1.5ex,4ex>
}
\]
as a 2-morphism $\alpha \maps f g \To h k$.  We can then compose
a bunch of such 2-morphisms:
\[
\xymatrix{
\bullet & \bullet \ar[l]_{}
& \bullet \ar[l]_{}
& \bullet \ar[l]_{}
 \\  
\bullet \ar[u]^{} 
& \bullet \ar[l]^{}="g1"  \ar[u]_{}
& \bullet \ar[l]^{}="g2"  \ar[u]_{}
& \bullet \ar[l]^{}="g3"  \ar[u]_{}
\ar@{=>}^{} "g1"+<1.5ex,5.5ex>;"g1"+<-1.5ex,2.5ex>
\ar@{=>}^{} "g2"+<1.5ex,5.5ex>;"g2"+<-1.5ex,2.5ex>
\ar@{=>}^{} "g3"+<1.5ex,5.5ex>;"g3"+<-1.5ex,2.5ex>
 \\  
\bullet \ar[u]^{} 
& \bullet \ar[l]^{}="h1"  \ar[u]_{}
& \bullet \ar[l]^{}="h2"  \ar[u]_{}
& \bullet \ar[l]^{}="h3"  \ar[u]_{}
\ar@{=>}^{} "h1"+<1.5ex,5.5ex>;"h1"+<-1.5ex,2.5ex>
\ar@{=>}^{} "h2"+<1.5ex,5.5ex>;"h2"+<-1.5ex,2.5ex>
\ar@{=>}^{} "h3"+<1.5ex,5.5ex>;"h3"+<-1.5ex,2.5ex>
}
\]
with the help of a trick called `whiskering'.

Whiskering is a way to compose a 1-morphism and a 2-morphism.  Suppose we
want to compose a 2-morphism $\alpha$ and a morphism $f$ that sticks
out like a whisker on the left:
\[
\xymatrix{
  z \bullet 
& y \bullet
  \ar[l]_{f}
&&  \bullet x
  \ar@/_2.5ex/[ll]_{g}="h1"
  \ar@/^2.5ex/[ll]^{g'}="h3"
  \ar@{=>}^{\alpha} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
}
\]
We can do this by taking the horizontal composite $1_f \circ \alpha$:
\[
\xymatrix{
 z \bullet &&
y \bullet \ar@/_2.5ex/[ll]_{f}="h1"
  \ar@/^2.5ex/[ll]^{f}="h3"
  \ar@{=>}^{1_f} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
&& \bullet x
  \ar@/_2.5ex/[ll]_{g}="h1"
  \ar@/^2.5ex/[ll]^{g'}="h3"
  \ar@{=>}^{\alpha} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
}
\]
We call the result $f \circ \alpha$, or $\alpha$ \define{left whiskered}
by $f$.  Similarly, if we have a whisker sticking out on the right:
\[
\xymatrix{
z \bullet &&
y \bullet 
  \ar@/_2.5ex/[ll]_{g}="h1"
  \ar@/^2.5ex/[ll]^{g'}="h3"
  \ar@{=>}^{\alpha} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
& x \bullet
  \ar[l]_{f}
}
\]
we can take the horizontal composite $\alpha \circ 1_f$:
\[
\xymatrix{
z \bullet &&
y \bullet \ar@/_2.5ex/[ll]_{g}="h1"
  \ar@/^2.5ex/[ll]^{g'}="h3"
  \ar@{=>}^{\alpha} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
&& \bullet x
  \ar@/_2.5ex/[ll]_{f}="h1"
  \ar@/^2.5ex/[ll]^{f}="h3"
  \ar@{=>}^{1_f} "h1"+<0ex,-2ex>;"h3"+<0ex,2ex>
}
\]
and call the result $\alpha \circ f$, or $\alpha$ 
\define{right whiskered} by $f$.  

With the help of whiskering, we can compose 2-morphisms shaped like
arbitrary polygons.  For example, suppose we want to horizontally
compose two squares: 
\[
\xymatrix{
\bullet 
& \bullet \ar[l]_{f}="g1"  
& \bullet \ar[l]_{f'}="h1"  
\\  
\bullet \ar[u]^{h} 
& \bullet \ar[l]^{k}="g2"  \ar[u]_{\ell}
& \bullet \ar[l]^{k'}="g3"  \ar[u]_{g}
\ar@{=>}^{\alpha} "g2"+<1.5ex,7ex>;"g2"+<-1.5ex,4ex>
\ar@{=>}^{\beta} "g3"+<1.5ex,7ex>;"g3"+<-1.5ex,4ex>
}
\]
To do this, we can left whisker $\beta$ by $f$, obtaining
this 2-morphism:
\[    f \circ \beta \maps \; f f' g \; \To \; f \ell k' \]
\[
  \xymatrix{
\bullet 
& \bullet \ar[l]_{f}="g1"  
& \bullet \ar[l]_{f'}="h1"  
\\  
& \bullet \ar[u]_{\ell}
& \bullet \ar[l]^{k'}="g3"  \ar[u]_{g}
\ar@{=>}^{\beta} "g3"+<1.5ex,7ex>;"g3"+<-1.5ex,4ex>
}
\]
Then we can right whisker $\alpha$ by $k'$, obtaining 
\[         \alpha \circ k' \maps \; f \ell k' \; \To \; h k k' \]
\[
\xymatrix{
\bullet 
& \bullet \ar[l]_{f}="g1"  
& 
\\  
\bullet \ar[u]^{h} 
& \bullet \ar[l]^{k}="g2"  \ar[u]_{\ell}
& \bullet \ar[l]^{k'}="g3"  
\ar@{=>}^{\alpha} "g2"+<1.5ex,7ex>;"g2"+<-1.5ex,4ex>
}
\]
Then we can vertically compose these to get the desired 2-morphism:
\[   (\alpha \circ k') \cdot (g \circ \beta) 
\maps \; f f' g \; \To \; h k k' \]
\[
\xymatrix{
\bullet 
& \bullet \ar[l]_{f}="g1"  
& \bullet \ar[l]_{f'}="h1"  
\\  
\bullet \ar[u]^{h} 
& \bullet \ar[l]^{k}="g2"  \ar[u]_{\ell}
& \bullet \ar[l]^{k'}="g3"  \ar[u]_{g}
\ar@{=>}^{\alpha} "g2"+<1.5ex,7ex>;"g2"+<-1.5ex,4ex>
\ar@{=>}^{\beta} "g3"+<1.5ex,7ex>;"g3"+<-1.5ex,4ex>
}
\]

The same sort of trick lets us vertically compose squares.
By iterating these procedures we can define more complicated
composites, like this:
\[
\xymatrix{
\bullet & \bullet \ar[l]_{}
& \bullet \ar[l]_{}
& \bullet \ar[l]_{}
& \bullet \ar[l]_{}
 \\  
\bullet \ar[u]^{} 
& \bullet \ar[l]^{}="g1"  \ar[u]_{}
& \bullet \ar[l]^{}="g2"  \ar[u]_{}
& \bullet \ar[l]^{}="g3"  \ar[u]_{}
& \bullet \ar[l]^{}="g4"  \ar[u]_{}
\ar@{=>}^{} "g1"+<1.5ex,5.5ex>;"g1"+<-1.5ex,2.5ex>
\ar@{=>}^{} "g2"+<1.5ex,5.5ex>;"g2"+<-1.5ex,2.5ex>
\ar@{=>}^{} "g3"+<1.5ex,5.5ex>;"g3"+<-1.5ex,2.5ex>
\ar@{=>}^{} "g4"+<1.5ex,5.5ex>;"g4"+<-1.5ex,2.5ex>
 \\  
\bullet \ar[u]^{} 
& \bullet \ar[l]^{}="h1"  \ar[u]_{}
& \bullet \ar[l]^{}="h2"  \ar[u]_{}
& \bullet \ar[l]^{}="h3"  \ar[u]_{}
& \bullet \ar[l]^{}="h4"  \ar[u]_{}
\ar@{=>}^{} "h1"+<1.5ex,5.5ex>;"h1"+<-1.5ex,2.5ex>
\ar@{=>}^{} "h2"+<1.5ex,5.5ex>;"h2"+<-1.5ex,2.5ex>
\ar@{=>}^{} "h3"+<1.5ex,5.5ex>;"h3"+<-1.5ex,2.5ex>
\ar@{=>}^{} "h4"+<1.5ex,5.5ex>;"h4"+<-1.5ex,2.5ex>
}
\]
Of course, one may wonder if these more complicated composites are
unambiguously defined!  Luckily they are, thanks to associativity and
the interchange law.  This is a nontrivial result, called the `pasting
theorem' \cite{Power}.

By this method, we can reduce the task of computing $\hol(\Sigma)$ for
a large surface $\Sigma$ to the task of computing it for lots of small
squares.   Ultimately, of course, we should take a limit as the squares
become smaller and smaller.  But for our nonrigorous discussion, it is
enough to consider a very small square like this:
\[
\xy
(-8,8)*+{\bullet}="A";
(8,8)*{}="B";
(-8,-8)*{}="C";
(8,-8)*+{\bullet}="D";
(2,2)*{}="E";
(-2,-2)*{}="F";
"C";"D" **\dir{-};
"B";"D" **\dir{-};
{\ar@{=>}^{\scriptstyle \Sigma} "F";"E";};
{\ar@{->} "B";"A"};
{\ar@{->} "C";"A"};
(-10,-10)*{\scriptstyle \gamma_2};
(10,10)*{\scriptstyle \gamma_1};
\endxy
\]
We can think of this square as a 2-morphism 
\[   \Sigma \maps \gamma_1 \To \gamma_2 \]
where $\gamma_1$ is the path that goes up and then across,
while $\gamma_2$ goes across and then up.  We wish to compute
\[   \hol(\Sigma) \maps \hol(\gamma_1) \To \hol(\gamma_2) . \]
On the one hand, $\hol(\Sigma)$ involves the 2-form $B$.  On the
other hand, its source and target depend only on the 1-form $A$:
\[      \hol(\gamma_1) =  \poexp \left( \int_{\gamma_i} A \right) , 
\qquad 
        \hol(\gamma_2) =  \poexp \left( \int_{\gamma_2} A \right) .\]
So, $\hol(\Sigma)$ cannot have the right source and target unless $A$
and $B$ are related by an equation!

Let us try to guess this equation.  Recall from Theorem \ref{crossed_module}
that a 2-morphism $\alpha \maps g_1 \To g_2$ in $\G$ is determined by 
an element $h \in H$ with $g_2 = t(h) g_1$.
Using this, we may think of $\hol(\Sigma) \maps \hol(\gamma_1) \to 
\hol(\gamma_2)$ as determined by an element $h \in H$ with
\[        \poexp \left( \int_{\gamma_2} A \right) = 
         t(h) \; \poexp \left( \int_{\gamma_1} A \right) , \]
or in other words
\begin{equation}
\label{constraint}
       t(h) = \poexp \left( \int_{\partial \Sigma} A \right) 
\end{equation}
where the loop $\partial \Sigma = \gamma_2 \gamma_1^{-1}$ goes around
the square $\Sigma$.  For a very small square, we can approximately
compute the right hand side using Stokes' theorem:
\[       \poexp \left( \int_{\partial \Sigma} A \right) \approx
                 \exp\left( \int_\Sigma F \right) . \] 
On the other hand, there
is an obvious guess for the approximate value of $h$, which is
supposed to be built using the 2-form $B$:
\[          h \approx \exp\left( \int_\Sigma B\right) . \]
For this guess to yield Equation (\ref{constraint}), 
at least to first order in the size of our square, we need
\[    t(\exp\left( \int_\Sigma B\right)) 
\approx \exp\left( \int_\Sigma F \right) . \]
But this will be true if
\[          \dt(B) = F  .\]
And this is the equation that relates $A$ and $B$!

What have we learned here?  First, for any surface $\Sigma \maps \gamma_1
\To \gamma_2$, the holonomy $\hol(\Sigma)$ is determined by an element
$h \in H$ with 
\[        \poexp \left( \int_{\gamma_2} A \right) = 
         t(h) \; \poexp \left( \int_{\gamma_1} A \right)   \]
In the limit where $\Sigma$ is very small, this element $h$ depends 
only on $B$:
\[         h \approx \exp\left( \int_\Sigma B \right)  .\]
But for a finite-sized surface, this formula is no good, since it 
involves adding up $B$ at different points, which is not a smart
thing to do.  For a finite-sized surface, $h$ depends on $A$ as well as
$B$, since we can approximately compute $h$ by chopping this surface 
into small squares, whiskering them with paths, and composing them---and 
the holonomies along these paths are computed using $A$.  

To get the \emph{exact} holonomy over a finite-sized surface by
this method, we need to take a limit where we subdivide the surface
into ever smaller squares.   This is the Lie 2-group analogue
of a Riemann sum.  But for actual calculations, this process 
is not very convenient. More practical formulas for computing 
holonomies over surfaces can be found in the work of Schreiber and Waldorf 
\cite{SchreiberWaldorf:gerbes}, Martins and Picken \cite{MartinsPicken:2007}.
