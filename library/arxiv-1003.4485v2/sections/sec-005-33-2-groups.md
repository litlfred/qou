---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-005-33-2-groups
section_title: "2-Groups"
section_number: 3.3
pages: 15-21
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.982
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
Just as a group was a groupoid with one object, we define a
\define{2-group} to be a 2-groupoid with one object.  This definition
is so elegant that it may be hard to understand at first!  So, it will
be useful to take a 2-group $\G$ and chop it into four bite-sized
pieces of data, giving a `crossed module' $(G,H,t,\alpha)$.  Indeed,
2-groups were originally introduced in the guise of crossed modules by
the famous topologist J.\ H.\ C.\ Whitehead \cite{Whitehead}.  In
1950, with help from Mac Lane \cite{MW}, he used crossed modules to
generalize the fundamental group of a space to what we might now call
the `fundamental 2-group'.  But only later did it become clear that a
crossed module was another way of talking about a 2-groupoid with just
one object!  For more of this history, and much more on 2-groups, see
\cite{BaezLauda:2groups}.

Let us start by seeing what it means to say a 2-group is a
2-groupoid with one object.  It means that a 2-group $\G$ has:
\begin{itemize}
\item one object: 
\[ \bullet \]
\item morphisms: 
\[
\xymatrix{
 \bullet 
& \bullet \ar@/_0.5pc/[l]_{g}
}
\]
\item and 2-morphisms:
\[
\xy 
(-10,0)*+{\bullet}="4"; 
(10,0)*+{\bullet}="6";
{\ar@/_1.65pc/_{g} "6";"4"}; 
{\ar@/^1.65pc/^{g'} "6";"4"};
{\ar@{=>}^<<<{\alpha} (0,3)*{};(0,-3)*{}} ;
\endxy 
\]
\end{itemize}
The morphisms form a group under composition:
\[ \xymatrix{ \bullet &
\ar@/_/[l]_g  
\bullet 
& 
\bullet 
\ar@/_/[l]_{g'} 
} = 
\xymatrix{ \bullet & \bullet \ar@/_/[l]_{gg'} } \]
The 2-morphisms form a group under horizontal composition:
\[
  \xymatrix{
   \bullet
&& \bullet
  \ar@/_2.5ex/[ll]_{g_1}="g1"\ar@/^2.5ex/[ll]^{g'_1}="g2"
  \ar@{=>}^{\alpha_1} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&& 
  \ar@/_2.5ex/[ll]_{g_2}="g1"\ar@/^2.5ex/[ll]^{g'_2}="g2"
  \ar@{=>}^{\alpha_2} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\quad =\quad
\xymatrix{
  \bullet
&& \bullet 
\ar@/_3ex/[ll]_{g_1 g_2}="g1"
\ar@/^3ex/[ll]^{g'_1 g_2'}="g3"
\ar@{=>}^{\alpha_1\circ\alpha_2} "g1"+<-1ex,-2ex>;"g3"+<-1ex,2ex>
}
\]
In addition, the 2-morphisms can be composed vertically:
\[
\xymatrix{
    \bullet && \bullet 
  \ar@/_5ex/[ll]_{g}="g1"
  \ar[ll]_(0.65){g'}
  \ar@{}[ll]|{}="g2"
  \ar@/^5ex/[ll]^{g''}="g3"
  \ar@{=>}^{\alpha} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha'} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>
}
\quad =\quad
\xymatrix{
\bullet
&&\bullet 
\ar@/_3ex/[ll]_{g}="g1"
\ar@/^3ex/[ll]^{g''}="g3"
\ar@{=>}^{\alpha'\cdot\alpha} "g1"+<-1ex,-2ex>;"g3"+<-1ex,2ex>
}
\]
Vertical composition is also associative with identity and
inverses.  But the 2-morphisms do not form a group under this operation,
because a given pair may not be composable: their source
and target may not match up.  Finally, vertical and horizontal 
composition are tied together by the interchange law, which says
the two ways one can read this diagram are consistent.
\[
\xymatrix{
   \bullet 
&&  \bullet
  \ar@/_4ex/[ll]_{g_1}="g1"
  \ar[ll]_(0.65){g'_1}
  \ar@{}[ll]|{}="g2"
  \ar@/^4ex/[ll]^{g''_1}="g3"
  \ar@{=>}^{\alpha} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha'} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>

&&  \bullet 
  \ar@/_4ex/[ll]_{g_2}="h1"
  \ar[ll]_(0.65){g'_2}
  \ar@{}[ll]|{}="h2"
  \ar@/^4ex/[ll]^{g''_2}="h3"
  \ar@{=>}^{\beta} "h1"+<0ex,-2ex>;"h2"+<0ex,0.5ex>
  \ar@{=>}^{\beta'} "h2"+<0ex,-0.5ex>;"h3"+<0ex,2ex>
}
\]

Now let us create a crossed module $(G,H,t,\alpha)$ from a 2-group $\G$.  
To do this, first note that the morphisms of the 2-group form a group by 
themselves, with composition as the group operation.  So:
\begin{itemize}
\item Let $G$ be the set of morphisms in $\G$, made into a
group with composition as the group operation:
\[ \xymatrix{ \bullet &
\ar@/_/[l]_g  
\bullet 
& 
\bullet 
\ar@/_/[l]_{g'} 
} = 
\xymatrix{ \bullet & \bullet \ar@/_/[l]_{gg'} } \]
\end{itemize}
How about the 2-morphisms?  These also form a group, with horizontal 
composition as the group operation.  But it turns out to be 
efficient to focus on a subgroup of this:
\begin{itemize}
\item Let $H$ be the set of all 2-morphisms 
whose source is the identity:
\[
\xymatrix{\bullet
&& \bullet
\ar@/_3ex/[ll]_{1_\bullet}="g1"
\ar@/^3ex/[ll]^{t(h)}="g3"
\ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g3"+<0ex,2.5ex>
}
\]
We make $H$ 
into a group with horizontal composition as the group 
operation:
\[
  \xymatrix{
  \bullet
&&\bullet
  \ar@/_2.5ex/[ll]_{1_\bullet}="g1"\ar@/^2.5ex/[ll]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_2.5ex/[ll]_{1_\bullet}="g1"\ar@/^2.5ex/[ll]^{t(h')}="g2"
  \ar@{=>}^{h'} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\quad =\quad
\xymatrix{
\bullet
&& \bullet
\ar@/_3ex/[ll]_{1_\bullet}="g1"
\ar@/^3ex/[ll]^{t(hh')}="g3"
\ar@{=>}^{hh'} "g1"+<-1ex,-2.5ex>;"g3"+<-1ex,2.5ex>
}
\]
\end{itemize}
Above we use $hh'$ as an abbreviation for the horizontal composite $h
\circ h'$ of two elements of $H$.  We will use $h^{-1}$ to denote the
horizontal inverse of an element of $H$.  We use $t(h)$ to denote the
target of an element $h \in H$.  The definition of a 2-category
implies that $t \maps H \to G$ is a group homomorphism:
\[            t(hh') = t(h) t(h')  .\]
This homomorphism is our third piece of data:
\begin{itemize}
\item
A group homomorphism $t \maps H \to G$ sending each 2-morphism in
$H$ to its target:
\[
\xymatrix{\bullet
&& \bullet
\ar@/_3ex/[ll]_{1_\bullet}="g1"
\ar@/^3ex/[ll]^{t(h)}="g3"
\ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g3"+<0ex,2.5ex>
}
\]
\end{itemize}
The fourth piece of data is the subtlest.  There is a way
to `horizontally conjugate' any element $h \in H$ by an element 
$g \in G$, or more precisely by its identity 2-morphism $1_g$:
\[
  \xymatrix{
  \bullet
&&\bullet
  \ar@/_2.5ex/[ll]_{g}="g1"\ar@/^2.5ex/[ll]^{g}="g2"
  \ar@{=>}^{1_g} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_2.5ex/[ll]_{1_\bullet}="g1"\ar@/^2.5ex/[ll]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_2.5ex/[ll]_{g^{-1}}="g1"\ar@/^2.5ex/[ll]^{g^{-1}}="g2"
  \ar@{=>}^{1_{g^{-1}}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\]
The result is a 2-morphism in $H$ which we call $\alpha(g)(h)$.  In
fact, $\alpha(g)$ is an {\bf automorphism} of
$H$, meaning a one-to-one and onto function with
\[             \alpha(g)(hh') = \alpha(g)(h) \; \alpha(g)(h')  .\]
Composing two automorphisms gives another automorphism, and this
makes the automorphisms of $H$ into a group, say $\Aut(H)$.  Even
better, $\alpha$ gives a group homomorphism
\[        \alpha \maps G \to \Aut(H) . \]
Concretely, this means that in addition to the above equation, we have
\[        \alpha(g g') = \alpha(g)\alpha(g'). \]
Checking these two equations is a nice way to test your
understanding of 2-categories.  A group homomorphism $\alpha
\maps G \to \Aut(H)$ is also called an \define{action} of the group
$G$ on the group $H$.  So, the fourth and final piece of data in our
crossed module is:
\begin{itemize}
\item
An action $\alpha$ of $G$ on $H$ given by:
\[
  \xymatrix{
  \bullet
&&\bullet
  \ar@/_2.5ex/[ll]_{g}="g1"\ar@/^2.5ex/[ll]^{g}="g2"
  \ar@{=>}^{1_g} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_2.5ex/[ll]_{1_\bullet}="g1"\ar@/^2.5ex/[ll]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_2.5ex/[ll]_{g^{-1}}="g1"\ar@/^2.5ex/[ll]^{g^{-1}}="g2"
  \ar@{=>}^{1_g^{-1}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\quad = \quad
  \xymatrix{
  \bullet
&&\bullet
  \ar@/_2.5ex/[ll]_{1}="g1"\ar@/^2.5ex/[ll]^{t(\alpha(g)(h))}="g2"
  \ar@{=>}^{\alpha(g)(h)} "g1"+<-1ex,-2.5ex>;"g2"+<-1ex,2.5ex>
}
\]
\end{itemize}
A crossed module $(G,H,t,\alpha)$ must also satisfy two more
equations which follow from the definition of a 2-group.
First, examining the above diagram, we see that $t$ is
\define{\boldmath$G$-equivariant}, by which we mean:
\begin{itemize}
\item $t(\alpha(g)h) = g ( t(h) ) g^{-1}$ for all $g \in G$
and $h \in H$.
\end{itemize}
Second, the \define{Peiffer identity} holds:
\begin{itemize}
\item $ \alpha(t(h))h' = hh'h^{-1}$ for all $h,h' \in H$.
\end{itemize}

The Peiffer identity is the least obvious thing about a crossed
module.  It follows from the interchange law, and it is worth
seeing how.  First, we have:
\[
hh'h^{-1} \quad = \quad
  \xymatrix{
  \bullet
&&\bullet
  \ar@/_3ex/[ll]_{1_\bullet}="g1"\ar@/^3ex/[ll]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_3ex/[ll]_{1_\bullet}="g1"\ar@/^3ex/[ll]^{t(h')}="g2"
  \ar@{=>}^{h'} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&\bullet
  \ar@/_3ex/[ll]_{1_\bullet}="g1"\ar@/^3ex/[ll]^{t(h^{-1})}="g2"
  \ar@{=>}^{h^{-1}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\]
where---beware!---we are now using $h^{-1}$ to mean the
\emph{horizontal} inverse of $h$, since this is its inverse in the
group $H$.  We can pad out this equation by vertically composing with
some identity morphisms:
\[
hh'h^{-1} \quad = \quad
\xymatrix{
   \bullet 
&&&  \bullet
  \ar@/_6ex/[lll]_{1_\bullet}="g1"
  \ar[lll]_(0.7){t(h)}
  \ar@{}[lll]|{}="g2"
  \ar@/^6ex/[lll]^{t(h)}="g3"
  \ar@{=>}^{h} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{1_{t(h)}} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>

&&&  \bullet 
  \ar@/_6ex/[lll]_{1_\bullet}="h1"
  \ar[lll]_(0.7){1_\bullet}
  \ar@{}[lll]|{}="h2"
  \ar@/^6ex/[lll]^{t(h)}="h3"
  \ar@{=>}^{1_{1_\bullet}} "h1"+<0ex,-2ex>;"h2"+<0ex,0.5ex>
  \ar@{=>}^{h} "h2"+<0ex,-0.5ex>;"h3"+<0ex,2ex>

&&&  \bullet
  \ar@/_6ex/[lll]_{1_\bullet}="g1"
  \ar[lll]_(0.70){t(h^{-1})}
  \ar@{}[lll]|{}="g2"
  \ar@/^6ex/[lll]^{t(h^{-1})}="g3"
  \ar@{=>}^{h^{-1}} "g1"+<-0.5ex,-2ex>;"g2"+<-0.5ex,0.5ex>
  \ar@{=>}^{1_{t(h^{-1})}} "g2"+<-0.5ex,-0.5ex>;"g3"+<-0.5ex,2ex>
}
\]
This diagram describes an unambiguous 2-morphism,
thanks to the interchange law.  So, we can do the horizontal
compositions first and get:
\[
hh'h^{-1} \quad = \quad
\xymatrix{
   \bullet 
&&&&&  \bullet
  \ar@/_7ex/[lllll]_{1_\bullet}="g1"
  \ar[lllll]_(0.65){1_\bullet}
  \ar@{}[lllll]|{}="g2"
  \ar@/^7ex/[lllll]^{t(hh'h^{-1})}="g3"
  \ar@{=>}^{1_{1_\bullet}} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha(t(h))(h')} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>
}
\]
But vertically composing with an identity 2-morphism has no
effect.  So, we obtain the Peiffer identity:
\[  hh'h^{-1} = \alpha(t(h))(h')  . \]

All this leads us to define a \define{crossed module} $(G,H,t,\alpha)$ 
to consist of:
\begin{itemize}
\item a group $G$,
\item a group $H$, 
\item a homomorphism $t \maps H \to G$, and
\item an action $\alpha \maps G \to \Aut(H)$ 
\end{itemize}
such that:
\begin{itemize} 
\item $t$ is $G$-equivariant: 
\[  t(\alpha(g)h) = g ( t(h) ) g^{-1}  \]
for all $g \in G$ and $h \in H$, and
\item
the Peiffer identity holds for all $h, h'\in H$:
\[  \alpha(t(h))h' = hh'h^{-1} .\]
\end{itemize}

In fact, we can recover a 2-group $\G$ from its crossed module
$(G,H,t,\alpha)$, so crossed modules are just another way of thinking
about 2-groups.  The trick to seeing this is to notice that 
2-morphisms in $\G$ are the same as pairs $(g,h) \in G \times H$.
Such a pair gives this 2-morphism:
\[          
  \xymatrix{
   \bullet
&& \bullet
  \ar@/_2.5ex/[ll]_{1_\bullet}="g1"\ar@/^2.5ex/[ll]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&& \bullet
  \ar@/_2.5ex/[ll]_{g}="g1"\ar@/^2.5ex/[ll]^{g}="g2"
  \ar@{=>}^{1_g} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\]
We leave it to the reader to check that every 2-morphism in $\G$ is of
this form.  Note that this 2-morphism goes from $g$ to $t(h)g$.  So,
when we construct a 2-group from a crossed module, we get a
2-morphism 
\[             (g,h) \maps g \to t(h) g  \]
from any pair $(g,h) \in G \times H$.  Horizontal composition of
2-morphisms then makes $G \times H$ into a group, as follows:
\[ (g,h) \circ (g',h') = \]
\[
  \xymatrix{
   \bullet
& \bullet
  \ar@/_2.5ex/[l]_{1_\bullet}="g1"\ar@/^2.5ex/[l]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g}="g1"\ar@/^2.5ex/[l]^{g}="g2"
  \ar@{=>}^{1_g} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{1_\bullet}="g1"\ar@/^2.5ex/[l]^{t(h')}="g2"
  \ar@{=>}^{h'} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g'}="g1"\ar@/^2.5ex/[l]^{g'}="g2"
  \ar@{=>}^{1_{g'}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
= \]
\[
  \xymatrix{
   \bullet
& \bullet
  \ar@/_2.5ex/[l]_{1_\bullet}="g1"\ar@/^2.5ex/[l]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g}="g1"\ar@/^2.5ex/[l]^{g}="g2"
  \ar@{=>}^{1_g} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{1_\bullet}="g1"\ar@/^2.5ex/[l]^{t(h')}="g2"
  \ar@{=>}^{h'} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g^{-1}}="g1"\ar@/^2.5ex/[l]^{g^{-1}}="g2"
  \ar@{=>}^{1_{g^{-1}}} "g1"+<-1ex,-2.5ex>;"g2"+<-1ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g}="g1"\ar@/^2.5ex/[l]^{g}="g2"
  \ar@{=>}^{1_{g}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
& \bullet
  \ar@/_2.5ex/[l]_{g'}="g1"\ar@/^2.5ex/[l]^{g'}="g2"
  \ar@{=>}^{1_{g'}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
= 
\]
\[
   \xymatrix{
   \bullet
& \bullet
  \ar@/_2.5ex/[l]_{1_\bullet}="g1"\ar@/^2.5ex/[l]^{t(h)}="g2"
  \ar@{=>}^{h} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&&& \bullet
  \ar@/_2.5ex/[lll]_{1_\bullet}="g1"\ar@/^2.5ex/[lll]^{t(\alpha(g)(h'))}="g2"
  \ar@{=>}^{\alpha(g)(h')} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&& \bullet
  \ar@/_2.5ex/[ll]_{gg'}="g1"\ar@/^2.5ex/[ll]^{gg'}="g2"
  \ar@{=>}^{1_{gg'}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
= \]
\[
  \xymatrix{
   \bullet
&&&& \bullet
  \ar@/_4ex/[llll]_{1_\bullet}="g1"\ar@/^4ex/[llll]^{t(h\alpha(g)(h'))}="g2"
  \ar@{=>}^{h\alpha(g)(h')} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&& \bullet
  \ar@/_2.5ex/[ll]_{gg'}="g1"\ar@/^2.5ex/[ll]^{gg'}="g2"
  \ar@{=>}^{1_{gg'}} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
} 
= 
(gg', h\alpha(g)(h')) .\]
So, the group of 2-morphisms of $\G$ is the semidirect product 
$G \ltimes H$, defined using the action $\alpha$.

Following this line of thought, the reader can check the following:

\begin{thm}
\label{crossed_module}
Given a crossed module $(G,H,t,\alpha)$, there is a unique 2-group
$\G$ where:
\begin{itemize}
\item
the group of morphisms is $G$,
\item
a 2-morphism $\alpha \maps g \To g'$ is the same
as a pair $(g,h) \in G \times H$ with $g' = t(h)g$,
\item
the vertical composite of $(g,h)$ and $(g',h')$, when they
are composable, is given by
\[   (g,h) \cdot (g',h') = (g',hh') , \]
\item 
the horizontal composite of $(g,h)$ and $(g',h')$ is given by
\[   (g,h) \circ (g',h') = (gg', h \alpha(g)(h')) .\]
\end{itemize}
Conversely, given a 2-group $\G$, there is a unique crossed module
$(G,H,t,\alpha)$ where:
\begin{itemize}
\item $G$ is the group of morphisms of $\G$, 
\item $H$ is the group of 2-morphisms with source equal to $1_\bullet$,
\item $t \maps H \to G$ assigns to each 2-morphism in $H$ its target,
\item the action $\alpha$ of $G$ on $H$ is given by
\[           \alpha(g) h = 1_g \circ h \circ 1_{g^{-1}}\;  .\]
\end{itemize}
\end{thm}

Indeed, these two processes set up an equivalence between 2-groups and
crossed modules, as described more formally elsewhere
\cite{BaezLauda:2groups,ForresterBarker}.  It thus makes sense to
define a \define{Lie 2-group} to be a 2-group for which the groups $G$
and $H$ in its crossed module are Lie groups, with the maps $t \maps H
\to G$ and $\alpha \maps G \to \Aut(H)$ being smooth.  It is worth
emphasizing that in this context we use $\Aut(H)$ to mean the group of
\emph{smooth} automorphisms of $H$.  This is a Lie group in its own
right.

In Section \ref{examples} we will use Theorem \ref{crossed_module} to
construct many examples of Lie 2-groups.  But first we should finish
explaining 2-connections.
