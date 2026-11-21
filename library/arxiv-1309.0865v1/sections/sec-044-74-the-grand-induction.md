---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-044-74-the-grand-induction
section_title: "The grand induction"
section_number: 7.4
pages: 73-83
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.773
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-hereitis}


Now comes the crux of the argument, a giant induction on maxwidth to prove Proposition \ref{LLabasismlt}. This entire section represents the proof.

Fix a rex ${\un{w}}$ for $w$. Let $X_{{\un{x}}}$ denote the set of all possible maps which are valid constructions of $\LL_{{\un{x}},\eb}$ with target ${\un{w}}$, but which also have polynomials in any
region. We omit ${\un{w}}$ from the notation $X_{\un{x}}$ because, as noted, the choice of reduced expression giving the final target does not matter, because the canonical isomorphisms between Hom spaces modulo lower terms
preserve the sets $X_{\un{x}}$.

Fix $M \ge 0$ and consider the following two statements:

\vspace{0.5cm}

($L_M$) For any ${\un{x}}$ with $\ell({\un{x}}) \le M$ and any ${\un{w}}$ with $\ell({\un{w}}) \le M$, choose a single map $\LL_{{\un{x}},\eb}$ for each appropriate sequence $\eb$ with target ${\un{w}}$. Then every map
$B_{\un{x}} \to B_{\un{w}}$ of maxwidth $\le M$ is in the left $R$-span of the $\LL_{{\un{x}},\eb}$ modulo $I_{\un{w}}$.

\vspace{0.5cm}

($X_M$) For any ${\un{x}}$ with $\ell({\un{x}}) \le M$ and any ${\un{w}}$ with $\ell({\un{w}}) \le M$, every map $B_{\un{x}} \to B_{\un{w}}$ of maxwidth $\le M$ is in the $\Bbbk$-span of $X_{\un{x}}$ modulo $I_{\un{w}}$.

\vspace{0.5cm}

Obviously $(L_M)$ is stronger than $(X_M)$. Our induction will use $(X_M)$ and $(L_{M-1})$ to prove $(L_M)$, and $(L_M)$ to prove $(X_{M+1})$. The base case is $M=0$. A map of maxwidth $0$ necessarily has $\un{w} = \emptyset$ and is just a polynomial, so both $(L_0)$ and $(X_0)$ hold. Now we fix ${\un{x}}$ and ${\un{w}}$. Any map $B_{\un{x}} \to B_{\un{w}}$ will have maxwidth $M \ge \ell({\un{w}})$ and $M \ge \ell({\un{x}})$, and if the map is in
$X_{\un{x}}$ then it has maxwidth precisely $M=\ell({\un{x}})$. Thus the statements $(L_M)$ and $(X_M)$ are vacuous for maps to ${\un{w}}$ when $M < \ell({\un{w}})$. When proving the inductive statement for maps to
${\un{w}}$, there will be two separate cases: $M=\ell({\un{w}})$, which we think of as the ``base case" for ${\un{w}}$ because it does not use induction; and $M>\ell({\un{w}})$.

Suppose that $M=\ell({\un{w}})$, and consider a graph $B_{\un{x}} \to B_{\un{w}}$. There can be no negative maps on top of the diagram, because of the maxwidth constraint, so the diagram ends with a
non-negative map. Unless the diagram is purely neutral, it ends with a strictly non-negative map which, by the upside-down version of Claim \ref{posrexhasdot}, implies that the diagram
lies within $I_{\un{w}}$. Hence we can assume that the diagram is neutral, and $\ell({\un{x}})=\ell({\un{w}})$. Any neutral map must consist only of polynomials and $2m$-valent vertices, so it is a rex move
with polynomials, and ${\un{x}}$ is also a rex for $w$. Such a map is an element of $X_{\un{x}}$ as desired, when $\eb=(1,1,\ldots,1)$. To show $(L_M)$ we need to show that any single rex move, with
polynomials only in the leftmost region, will span morphisms consisting of compositions of all rex moves with all polynomials modulo $I_{\un{w}}$. First we use the polynomial forcing relation \eqref{dotforcegeneral} to move the polynomials
to the leftmost region. This leaves behind terms where strands in the rex move are broken, but such terms are in $I_{\un{w}}$, because they have a strictly negative-positive decomposition. Now
we apply Lemma \ref{rexmovesmlt} to show that the difference between two rex moves is also in $I_{\un{w}}$.

Thus we have shown $(L_M)$ and $(X_M)$ for the case when $M=\ell({\un{w}})$. We assume henceforth that $\ell({\un{w}})<M$.

\begin{proof}[$(L_{M-1})$ and $(X_M) \implies (L_M)$] We need to show that each element of $X_{\un{x}}$ is in the span of our particular fixed choice of $\LL$ maps. Since the width of a map in
$X_{\un{x}}$ is precisely $\ell({\un{x}})$, induction already works unless $\ell({\un{x}})=M$, which we now assume.

To get from an element of $X_{\un{x}}$ associated to $\eb$ to our particular choice of $\LL_{{\un{x}},\eb}$, we need to force all polynomials to the left, and change our rex moves (possibly changing
the intermediate rexes ${\un{w}}_k$ as well). Let us refer to a rex move in the $\LL$ construction by which $\phi_k$ it appears in, and by whether it appears in the form $\a$ or $\b$ in Figure
\ref{fourmaps}. In fact, rex moves of the form $\b$ inside $\phi_k$ can be viewed instead as part of $\a$ inside $\phi_{k-1}$, so we shall assume that $\b$ is always trivial, and the
location of the rex move is specified by which $\phi_k$ it appears in. With this assumption, ${\un{w}}_k = {\un{w}}^s_k$ always.

Suppose that we are building a new light leaves map for some $({\un{x}},\eb)$ expressing $w$, using arbitrary choices, but we make a single error. While performing a rex move, we
accidentally insert some map with a strictly negative-positive decomposition. We call a graph of this form an ``$\LL$ map with error" or simply an \emph{error term}. Polynomial forcing
\eqref{dotforcegeneral} implies that the cost of sliding a polynomial across a rex move is adding an error term. By inspection, every region in an $\LL$ map is separated from the leftmost
region by the reduced expression ${\un{w}}_k$, or a subset thereof, so that we can assume that all polynomials are on the left, modulo error terms.

Lemma \ref{rexmovesmlt} implies that the difference between two rex moves is an error (that is, what would be an error if plugged in to the $\LL$ construction). Thus if two constructions
of $\LL$ differ only in the choice of rex moves, then the difference between the $\LL$ moves is spanned by error terms. Two constructions can also differ in their choice of ${\un{w}}_k =
{\un{w}}^s_k$, but this can be accounted for by changing rex moves as well. One can replace the identity of ${\un{w}}_k$ with a rex move $fg$ where $g \co {\un{w}}_k \to {\un{w}}'_k$ and $f \co {\un{w}}'_k \to
{\un{w}}_k$. Then, viewing $g$ as part of $\a$ in $\phi_k$ and $f$ as part of $\a$ in $\phi_{k+1}$, we can effectively replace ${\un{w}}_k$ with ${\un{w}}'_k$. (This still works even when dealing with
expressions having $s$ on the right, because we can split the rex move into the parts that affect $s$ and the parts that do not.) Hence, two different constructions of the same $\LL$
differ by error terms. Thus to show that a particular choice of $\LL$ maps spans them all, we need only show that that this choice of $\LL$ maps spans any error term.

This discussion of error terms is not strictly required for the proof we give next, but does say that the difference between $\LL$ maps is under control, and is useful for picturing how
one would, by hand, attempt to reduce a diagram into the desired form. We will use the notion of error terms in the later proofs.

Note that adding an error does not affect the maxwidth of a map. Let $F$ denote the partially constructed error term $\LL_{M-1}$, after the first $M-1$ steps have been applied. Now $F$ is
a map of width $\le M-1$, so we may apply induction and replace $F$ with an $\LL$ map \emph{of our choice}, or with a term having dots on top. By adjusting the rex moves in $\phi_{M-1}$
and $\phi_M$ we assume that whenever $F$ is an $\LL$ map, the top of $F$ is our desired ${\un{w}}_{M-1}$. Now we apply $\phi_M$ to finish the construction. We draw the four possibilities.
\igc{1}{proof10}

As noted previously, any error in $\phi_M$ itself yields a map contained in $I_{\un{w}}$ because some dot pulls to the top, so we can assume $\phi_M$ is error free, and that
it has our desired rex move. If $F$ is a term which has a dot on top, then this dot will pull through $\phi_M$ to become a dot on the very top except in a single case: when $\eb_M$ is D0
or D1, and the dot is on the final strand.

We have sufficient choice of $\phi_M$ such that the first diagram is actually one of our specified $\LL$ maps! The second diagram is in $I_{\un{w}}$. For the third and fourth diagrams, we can
reapply induction to $F$ without the dot on the blue strand, thus replacing the question marks with $\LL$ maps of our choice (or with more terms of the second type). Because the top of $F$
was a reduced expression ending in $s$, removing $s$ from the end still yields a reduced expression for which $s$ is \emph{not} in the right descent set. Now the overall expression is our
desired $\LL$ map, for $e_M$ being U1 or U0 respectively (again, up to the freedom we have to alter $\a$). \end{proof}


\begin{proof}[$(L_{M-1}) \implies (X_M)$] Now let us fix ${\un{w}}$ with $\ell({\un{w}})<M$, and prove that $(L_{M-1})$ implies $(X_M)$ for ${\un{w}}$. Consider a diagram of maxwidth $\le M$. If the
maxwidth $M$ is never attained then we may use induction, so let us assume that width $M$ is attained at least once. Width $M$ may be maintained for a period of time using $2m$-valent
vertices, and eventually the width may drop again to $M-1$ and rise back to $M$ for another interval.

\begin{claim} \label{goesbackdown} Assume $(L_{M-1})$. A map $B_{\un{x}} \to B_{\un{w}}$ with $\ell({\un{x}}) \le M-1$ which only reaches width $M$ for one continuous interval is in the span of $X_{\un{x}}$ modulo $I_{\un{w}}$.
\end{claim}

\begin{claim} \label{staysup} Assume $(L_{M-1})$. A map $B_{\un{x}} \to B_{\un{w}}$ with $\ell({\un{x}}) = M$ which only reaches width $M$ for one continuous interval starting at the
bottom is in the span of $X_{\un{x}}$ modulo $I_{\un{w}}$. \end{claim}

Suppose that we can show these two claims. Then we may simplify the diagram from top to bottom as follows. Consider the first interval where width $M$ appears. If that extends all the way
to the bottom of the map, we can use Claim \ref{staysup} to conclude that $X_M$ holds. If the interval ends and we return to width $M-1$, we can apply Claim \ref{goesbackdown} to replace that region with
an $\LL$ map (by $(L_{M-1})$, any $\LL$ map we choose), and thus the whole region now stays below width $M-1$. After doing this, the next interval becomes the first interval, and we repeat
the argument.

We proceed to prove Claim \ref{staysup} first. Let $\eta$ denote the map in question (having bottom ${\un{x}}$), ${\un{y}}$ the topmost sequence where width $M$ is attained, and $\un{z}$
the sequence immediately above, having $\ell(\un{z})=M-1$. The map $B_{\un{z}} \to B_{\un{w}}$ has maxwidth $M-1$ so by induction we can assume it is any construction of
$\LL_{{\un{z}},\eb}$ we choose. We can ignore polynomials on the left of the diagram. We begin by treating the case without $2m$-valent vertices on bottom, where ${\un{x}}={\un{y}}$. There
are two cases, to be treated differently.

\igc{1}{proof1}

\begin{claim} \label{addnegtri} Suppose a negative (merging) trivalent is added below a light leaves map. The result is light leaves. \end{claim}

\begin{proof} Suppose that the new trivalent vertex is attached to the $k$-th strand, with ${\un{x}}_k=s$. There are four choices for $\eb_k$: U0, U1, D0, D1. The composition will be a light
leaves with $(s\ s)$ instead of ${\un{x}}_k$ and one of four sequences instead of $\eb_k$: (U1 D1), (U1 D0), (D0 D0) or (D0 D1) respectively. This is pictured below:
\[ \ige{1}{mergingbelowLL} \qedhere \]
\end{proof}

\begin{claim} \label{addnegdot} Suppose that we add a negative (bottom) dot after the $k$-th strand of an $\LL_{\zb,\eb}$ of our choice, yielding a map from $B_{\un{y}}$. The result is in
$X_{\un{y}}$. \end{claim}

\begin{proof} Suppose that the new boundary dot is colored $s$. If $s$ is not in the right descent set of $w_k$, then the result is an $\LL$ map, with the new strand being U0. If $s$ is in
the right descent set, by choosing our $\LL_{\zb,\eb}$ appropriately, we can assume that $s$ occurs on the right of ${\un{w}}_k$. Now the statement follows from the equality below, because
both terms on the RHS are in $X_{\un{y}}$. We use the decomposition of Remark \ref{LLof111}, and relation \eqref{dotforcegeneral}. Remember that the use of $\frac{1}{2}$ is unnecessary, as any dual basis will do.
\[ \ige{1}{negdotbelowLL} \qedhere \]
\end{proof}

\begin{remark} While this is the only use in this chapter of the assumption of Demazure Surjectivity, it is significant. Without this assumption, double leaves will not form a
basis in the simplest counterexample: maps from $B_s \ot B_s \to B_s$. \end{remark}

Now we want to add more $2m$-valent vertices below this $\LL$ map. First we prove a useful inductive lemma.

\begin{claim} \label{splitintwain} Assume $(L_{M-1})$, and let $\ell({\un{x}})=M$. Suppose we have a map $B_{\un{x}} \to B_{\un{w}}$ which never returns to width $M$ after it leaves it. Suppose further that
the map splits as follows for some $0<k<M$.

\igc{1}{splitintwain}

Then the map is in the span of $X_{\un{x}}$, modulo $I_{\un{w}}$. \end{claim}

\begin{proof} Both question mark boxes have width strictly less than $M$, so by induction, we can assume that these boxes contain $\LL$ maps of our choice, or morphisms with dots on top.
The rest of the proof is exactly the same as the proof in the previous section. We induct on the width of the sequence $\vb$ with the dashed line through it. By an application of Lemma
\ref{rexesonlyplz} we can assume without loss of generality that $\vb$ is actually a reduced expression for $v \in W$. We write the lower box as $f_v + f_l$, where $f_v$ is a linear
combination of light leaves and $f_l$ is in $I_\vb$, and we write the upper box as $g_{w,1} + g_{w,0} + g_l$ where $g_l$ is in $I_{\un{w}}$, $g_{w,1}$ is a linear combination of light leaves
beginning with all U1 for $\vb$, and $g_{w,0}$ is a linear combination of light leaves which do not begin with U1's, meaning that somewhere on $\vb$ is a U0. In the product, combining
$f_v$ with $g_{w,1}$ will give valid constructions for an element of $X_{\un{x}}$. Combining anything with $g_l$ will be in $I_{\un{w}}$. For a term with either $f_l$ or $g_{w,0}$, we draw a new
dashed line to avoid the dot; this decreases the width of the dashed line by one. Induction then finishes the proof. \end{proof}

\begin{claim} \label{add2m} Assume $(L_{M-1})$, and let $\ell({\un{x}})=M$. Placing a $2m$-valent vertex below a diagram in $X_{\un{w}}$ will result in a diagram in the span of $X_{\un{x}}$ modulo $I_{\un{w}}$.
\end{claim}

\begin{proof} Any light leaves map with a neutral map below it is non-positive, so that it will never return to width $M$ after it departs. Suppose that we add the $2m$-valent vertex of
colors $s,t$ to strands ${\un{x}}_{l+1}$ through ${\un{x}}_{l+m}$ of a light leaves map $\LL_{{\un{x}},\eb}$. For any $0< k \le l$ or $l+m \le k < M$, we can split the diagram into $\LL_{\le k}$ and the
remainder as in Remark \ref{LLof111}, placing the new $2m$-valent vertex below whichever half is appropriate. Therefore, if any such $\LL_{\le k}$ maps to a shorter sequence, we can simply
use Claim \ref{splitintwain} to finish the proof. This allows us to reduce to the following special case: ${\un{x}}_{\le l}$ is a reduced expression and $\eb_{\le l}$ is all U1 (this includes
the possibility $l=0$); unless $l+m=M$, ${\un{x}}_{\le M-1}$ is a reduced expression and $\eb_{\le M-1}$ is all U1. Any time where $\eb_{l+1}$ through $\eb_{l+m}$ are all U1, the $2m$-valent
vertex can be viewed as part of the rex move in $\LL_{{\un{x}},\eb}$, so the result is clearly in $X_{\un{x}}$. Hence, we assume that $M=l+m$, and $({\un{x}},\eb)_{\le l}$ is a reduced expression for
$w_l \in W$.

Furthermore, we can alter any rex moves in $\LL_{{\un{x}},\eb}$ at will. The difference term will have an error. If this error occurs in $\phi_k$ for $k<M$ then we can use induction on the
error version of $\LL_{\le k}$, which has width $\le M-1$, to rewrite it in terms of $\LL$ maps and graphs with dots on top. These can be dealt with in the familiar manner. If the error occurs in $\phi_M$, it produces a dot on top, and is thus in $I_{\un{w}}$.

Hence, we can choose any desired reduced expression ${\un{w}}_l$ for $w_l$. Now $w_l = uv$ for $v \in W_{s,t}$ the dihedral group, and $u$ a minimal right coset representative of $W_{s,t}$. We
can choose a rex for $w_l$ of the form $\ub \vb$. Now the remaining terms of ${\un{x}}$ are all $s$ or $t$, and given any sequence of 1's and 0's, the assignment of U and D only depends on $v$
and not on $u$. Moreover, the rex moves required to send $s$ or $t$ to the right when a D appears (i.e. the rex moves of type $\b$ in Figure \ref{fourmaps}) can all be performed within
$\vb {\un{x}}_{>l}$, preserving $\ub$. Suppose that they are so in $\LL_{{\un{x}},\eb}$. Then the reduction to light leaves form does not depend on $\ub$ at all. We could assume without loss of
generality that $w_l=v \in W_{s,t}$, and the entire diagram only contains $2$ colors! Morphism spaces in $\DC$ for dihedral groups are already proven in \cite{EDihedral} to be the right
size, which implies the result; alternatively, one could do a case by case analysis. \end{proof}

\begin{remark} The case by case analysis can be quite interesting, although tedious. The following is a worthwhile exercise. Let $m=3$, and $\vb=sts$. Let ${\un{x}}=ststst$ and
$\eb=(U1,U1,U1,D0,D0,D0)$. First draw $\LL_{{\un{x}},\eb}$, and then place a $2m$-valent vertex below the D0's, and transform the diagram into light leaves format for $stssts$. This involves
repeated applications of \eqref{assoc2}. The exact same calculation works for general $m$. \end{remark}

We have now proven Claim \ref{staysup}. In order to prove Claim \ref{goesbackdown}, we need only put a positive generator below a map in $X_{\un{y}}$ for $\ell({\un{y}})=M$.

\begin{claim} \label{addpostri} Assume $(L_{M-1})$. Suppose that $\ell({\un{y}})=M$ and we add a positive (splitting) trivalent below a map in $X_{\un{y}}$ to obtain a map $B_{\un{x}} \to
B_{\un{w}}$. Then the result is in the span of $X_{\un{x}}$, modulo $I_{\un{w}}$. \end{claim}

\begin{proof} Suppose that the trivalent vertex is added to ${\un{y}}_k$ and ${\un{y}}_{k+1}$. There are 8 consistent possibilities for $\eb_k$ and $\eb_{k+1}$: $\eb_k$ can be any of U0, U1, D0, D1,
and it determines whether $\eb_{k+1}$ is U or D. In fact, if $\eb_k$ is U0 or D1, the result is manifestly in light leaves format.

\igc{1}{splittingbelowLLU0D1}

On the other hand, if $\eb_k$ is U1 or D0, the result locally looks like the following.

\igc{1}{splittingbelowLLU1D0}

By ``D0 or D1" we mean that the topmost trivalent in these graphs is as pictured when $\eb_{k+1}$ is D0, and has a further dot on top when $\eb_{k+1}$ is D1; this extra dot will not affect
our discussion. The dashed line indicates where width $M$ is reached. The asterisk box in these graphs is some rex move between two rexes which both have $s$ on the far right.

In fact, we believe both these diagrams to be zero. Let us pause to state a computational conjecture.

\begin{conj} \label{conj:rextri} For any rex move $\b \co \un{w} \to \un{w'}$, where both $\un{w}$ and $\un{w'}$ have $s$ on the far right, one has \begin{equation} \label{eq:slidetrithrurex} 
	{
	\vspace*{.4 cm}
	\labellist
	\small\hair 2pt
	 \pinlabel {$\b$} [ ] at 20 20
	 \pinlabel {$\b$} [ ] at 100 44
	 \pinlabel {$\un{w'}$} [ ] at 20 75
	 \pinlabel {$\un{w'}$} [ ] at 100 75
	 \pinlabel {$\un{w}$} [ ] at 20 -10
	 \pinlabel {$\un{w}$} [ ] at 100 -10
	 \pinlabel {$s$} [ ] at 47 53
	 \pinlabel {$s$} [ ] at 128 29
	\endlabellist
	\centering
	\ig{1}{lemma0}
	}.
	\vspace*{.4 cm} \end{equation} 

This would imply, using \eqref{assoc1} and \eqref{needle}, that the following is zero. \begin{equation} \label{rexmovestriis0} \ig{1}{rexmovestriis0} \end{equation} \end{conj}

Let us continue the proof without assuming this conjecture.

Which rex move appears in the asterisk box? If the rex move does not involve the rightmost $s$-colored strand, then clearly the result is zero by \eqref{assoc1} and \eqref{needle}. Since
two rex moves are equal modulo lower terms, we may assume that the asterisk box actually contains a strictly negative map followed by a strictly positive map. Moreover, Lemma
\ref{rexmovesmlt} guarantees that both the top and bottom of the asterisk box has a boundary dot.

We will now use these boundary dots to reduce the maxwidth of the diagram below $M$. The bottom dot (resp. top dot) appears either in one of the initial $k-1$ strands, or on the final
$s$-colored strand. If the dot appears on the final $s$-colored strand, then it will pull into the nearby trivalent vertex by \eqref{unit}. Otherwise, using rectilinear isotopy, the dot
can be pulled past this trivalent vertex. After performing these operations to the top and bottom dots, the resulting diagram never factors through a sequence of width $M$, and therefore
$(L_{M-1})$ implies that it can be expressed in the span of light leaves. \end{proof}

\begin{claim} \label{addposdot} Assume $(L_{M-1})$. Suppose that $\ell({\un{y}})=M$ and we add a positive (top) dot below a map in $X_{\un{y}}$ to obtain a map $B_{\un{x}} \to B_{\un{w}}$. Then the result is in
the span of $X_{\un{x}}$, modulo $I_{\un{w}}$. \end{claim}

\begin{proof} Suppose that the dot is attached to ${\un{y}}_l$ in $\LL_{{\un{y}},\eb}$. Let us draw a number of possibilities for what can happen to the dot.

\igc{1}{dotbelowLL}

In the first row, $\eb_l$ is U0 or D0 and is quickly taken care of. When $\eb_l$ is U1, what happens to the dot next can be a number of things. If the dot hits a rex move we end up on the
third row, which we will discuss shortly. Otherwise, we consult the second row. The dot either makes it all the way to the top (ending up in $I_{\un{w}}$) or it runs into a D0 or D1 and is
taken care of. Finally, if $\eb_l$ is D1, we end up in the first picture on the third row. The diagram on the right hand side clearly has width $\le M-1$, so it can be taken care of with
$(L_{M-1})$.

We have now proven this result except when the dot meets a rex move. We can induct on the number of $2m$-valent vertices in the rex move; the base case has just been done. Each term in the
Jones-Wenzl projector will have a dot on top. We can resolve that dot by induction to get an $\LL$ map with width $\le M-1$. After doing so, the remainder of the diagram has width $\le
M-1$, and we can apply $(L_{M-1})$ to finish the proof. \end{proof}

\begin{remark} There is an alternative proof. We can use Claim \ref{splitintwain} and the same style of argument as in Claim \ref{add2m} to reduce to the case where $({\un{y}},\eb)_{<
M-1}$ is a reduced expression with all U1's, and $\eb_M$ is D. Moreover, we can choose whatever rex moves we desire. Now the case by case analysis is easy, using some of the cases above.
\end{remark}

This concludes the proof of Claim \ref{goesbackdown}, and consequently of the fact that $(L_{M-1}) \implies (X_M)$. \end{proof}
