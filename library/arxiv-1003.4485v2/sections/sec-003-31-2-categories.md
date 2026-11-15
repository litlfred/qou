---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-003-31-2-categories
section_title: "2-Categories"
section_number: 3.1
pages: 12-14
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.989
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
Sets have elements.  Categories have elements, usually
called `objects', but also morphisms between these.  
In an `$n$-category', we go further and include 2-morphisms 
between morphisms, 3-morphisms between 2-morphisms,... and so 
on up to the $n$th level.  We are beginning to see $n$-categories 
provide an algebraic language for $n$-dimensional structures 
in physics \cite{BaezLauda:prehistory}.  Higher gauge theory is just 
one place where this is happening. 

Anyone learning $n$-categories needs to start with 
2-categories \cite{Lack}.  A \define{2-category} consists of:
\begin{itemize}
\item a collection of objects,
\item for any pair of objects $x$ and $y$, a set of morphisms
$f \maps x \to y$:
\[
\xymatrix{
   y \bullet 
& \bullet x \ar@/_0.5pc/[l]_{f}
}
\]
\item for any pair of morphisms $f,g \maps x \to y$,
a set of 2-morphisms $\alpha \maps f \To g$:
\[
  \xymatrix{
y \bullet 
&& \bullet x
\ar@/^2.5ex/[ll]^{g}="g1"\ar@/_2.5ex/[ll]_{f}="g2"
\ar@{=>}^{\alpha} "g2"+<0ex,-2.5ex>;"g1"+<0ex,2.5ex>
}
\]
We call $f$ the \define{source} of $\alpha$ and $g$ the 
\define{target} of $\alpha$.  
\end{itemize}
Morphisms can be composed just as in a category:
\[
\xymatrix{
   z \bullet 
&& \bullet y \ar@/_1pc/[ll]_{f}
    && \bullet x \ar@/_1pc/[ll]_{g}
}
\quad = \quad
\xymatrix{
   z \bullet 
&& \bullet x \ar@/_1pc/[ll]_{fg}
}
\]
while 2-morphisms can be composed in two distinct ways, vertically:
\[
\xymatrix{
   y \bullet && \bullet x
  \ar@/_5ex/[ll]_{f}="g1"
  \ar[ll]_(0.65){f'}
  \ar@{}[ll]|{}="g2"
  \ar@/^5ex/[ll]^{f''}="g3"
  \ar@{=>}^{\alpha} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha'} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>
}
\quad =\quad
\xymatrix{
y \bullet
&&\bullet x
\ar@/_3ex/[ll]_{f}="g1"
\ar@/^3ex/[ll]^{f''}="g3"
\ar@{=>}^{\alpha'\cdot\alpha} "g1"+<-1ex,-2ex>;"g3"+<-1ex,2ex>
}
\]
and horizontally:
\[
  \xymatrix{
  z \bullet
&&y \bullet
  \ar@/_2.5ex/[ll]_{f_1}="g1"\ar@/^2.5ex/[ll]^{f'_1}="g2"
  \ar@{=>}^{\alpha_1} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
&& \bullet x
  \ar@/_2.5ex/[ll]_{f_2}="g1"\ar@/^2.5ex/[ll]^{f'_2}="g2"
  \ar@{=>}^{\alpha_2} "g1"+<0ex,-2.5ex>;"g2"+<0ex,2.5ex>
}
\quad =\quad
\xymatrix{
 z \bullet
&& \bullet x
\ar@/_3ex/[ll]_{f_1 f_2}="g1"
\ar@/^3ex/[ll]^{f'_1 f_2'}="g3"
\ar@{=>}^{\alpha_1\circ\alpha_2} "g1"+<-1ex,-2ex>;"g3"+<-1ex,2ex>
}
\]
Finally, these laws must hold:
\begin{itemize}
\item Composition of morphisms is associative, and every
object $x$ has a morphism
\[
\xymatrix{x \bullet &
\bullet x \ar@/_0.5pc/[l]_{1_x}
}
\]
serving as an identity for composition, just as in an ordinary
category.
\item
Vertical composition is associative, and every morphism $f$ 
has a 2-morphism
\[
  \xymatrix{
y \bullet 
&& \bullet x
\ar@/^2.5ex/[ll]^{f}="g1"\ar@/_2.5ex/[ll]_{f}="g2"
\ar@{=>}^{1_f} "g2"+<0ex,-2.5ex>;"g1"+<0ex,2.5ex>
}
\]
serving as an identity for vertical composition.
\item
Horizontal composition is associative, and the 2-morphism
\[
  \xymatrix{
x \bullet 
&& \bullet x
\ar@/^2.5ex/[ll]^{1_x}="g1"\ar@/_2.5ex/[ll]_{1_x}="g2"
\ar@{=>}^{1_{1_x}} "g2"+<0ex,-2.5ex>;"g1"+<0ex,2.5ex>
}
\]
serves as an identity for horizontal composition.
\item
Vertical and horizontal composition of 2-morphisms obey
the \define{interchange law}:
\[
(\alpha'_1 \cdot \alpha_1) \circ (\alpha'_2 \cdot \alpha_2) 
= (\alpha'_1 \circ \alpha'_2) \cdot (\alpha_1 \circ \alpha_2)
\]
so that diagrams of the form
\[
\xymatrix{
  x \bullet 
&& y \bullet
  \ar@/_4ex/[ll]_{f_1}="g1"
  \ar[ll]_(0.65){f'_1}
  \ar@{}[ll]|{}="g2"
  \ar@/^4ex/[ll]^{f''_1}="g3"
  \ar@{=>}^{\alpha_1} "g1"+<0ex,-2ex>;"g2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha'_1} "g2"+<0ex,-0.5ex>;"g3"+<0ex,2ex>

&&  \bullet z
  \ar@/_4ex/[ll]_{f_2}="h1"
  \ar[ll]_(0.65){f'_2}
  \ar@{}[ll]|{}="h2"
  \ar@/^4ex/[ll]^{f''_2}="h3"
  \ar@{=>}^{\alpha_2} "h1"+<0ex,-2ex>;"h2"+<0ex,0.5ex>
  \ar@{=>}^{\alpha'_2} "h2"+<0ex,-0.5ex>;"h3"+<0ex,2ex>
}
\]
define unambiguous 2-morphisms.
\end{itemize}

The interchange law is the truly new thing here.  A category is
all about attaching 1-dimensional arrows end to end, and we need the
associative law to do that unambiguously.  In a 2-category, we
visualize the 2-morphisms as little pieces of 2-dimensional surface:
\[
  \xymatrix{
 \bullet 
&& \bullet 
\ar@/^2.5ex/[ll]^{\;}="g1"\ar@/_2.5ex/[ll]_{\;}="g2"
\ar@{=>}^{\;} "g2"+<0ex,-1.5ex>;"g1"+<0ex,1.5ex>
}
\]
We can attach these together in two ways: vertically and
horizontally.  For the result to be unambiguous, we need not only
associative laws but also the interchange law.  In what follows we
will see this law turning up all over the place.
