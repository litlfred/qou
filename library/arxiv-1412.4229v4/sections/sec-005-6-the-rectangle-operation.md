---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-005-6-the-rectangle-operation
section_title: "The Rectangle Operation"
section_number: 6
pages: 32-37
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
text_source: latex
latex_prose_ratio: 0.736
latex_coverage_ratio: 0.86
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
\label{sec:rect-oper}

In this section we continue with the material of Section 
\ref{sec:pairs-DG-modules}, but with slightly different notation.
Recall that $\cat{PDGR}$ is the category of central pairs of DG rings, and 
$\cat{PDGR}^{\leq 0}$ is the full subcategory of nonpositive central pairs. 
See Definitions \ref{dfn:910} and \ref{dfn:911}.

The main result here is Theorem \ref{thm:840}. 
Throughout this section we work in the following setup.

\begin{setup} \label{set:930}
We are given:
\begin{enumerate}
\item A central morphism 
$w / v : B' / A' \to B / A$ in $\cat{PDGR}^{\leq 0}$
(namely a morphism in $\cat{PDGR}^{\leq 0}_{\vec{\mrm{ce}}}$, 
see Definition \ref{dfn:911}(3)).

\item K-flat resolutions 
$s / r : \til{B} / \til{A} \to B / A$
and 
$s' / r' : \til{B}' / \til{A}' \to B' / A'$
in $\cat{PDGR}^{\leq 0}$, and morphisms 
\[ \til{w}_0 / \til{v}_0 , \, \til{w}_1 / \til{v}_1 : 
\til{B}' / \til{A}' \to \til{B} / \til{A} \]
in $\cat{PDGR}^{\leq 0}$ above $w / v$. 
See Definitions \ref{dfn:912}, \ref{dfn:913} and \ref{dfn:52}.

\item An object 
$(M^{\mrm{l}}, M^{\mrm{r}})$ in 
$\cat{D}(B) \times \cat{D}(B^{\mrm{op}})$,
an  object 
$(M'^{\, \mrm{l}}, M'^{\, \mrm{r}})$ in 
$\cat{D}(B') \times \cat{D}(B'^{\mrm{\, op}})$,
and a morphism 
\[ (\th^{\mrm{l}},  \th^{\mrm{r}}) : (M^{\mrm{l}}, M^{\mrm{r}}) \to 
(M'^{\, \mrm{l}}, M'^{\, \mrm{r}}) \]
in 
$\cat{D}(B') \times \cat{D}(B'^{\mrm{\, op}})$.
\end{enumerate}
\end{setup}

The DG ring input is depicted in the following commutative diagram in the 
category $\cat{PDGR}^{\leq 0}$, for $i = 0, 1$. 

\[ \UseTips \xymatrix @C=8ex @R=6ex {
\til{B}' / \til{A}'
\ar[r]^{ \til{w}_i / \til{v}_i }
\ar[d]_{ s' / r' }
&
\til{B} / \til{A}
\ar[d]^{ s / r }
\\
B' / A'
\ar[r]^{ w / v }
&
B / A
} \]

The four central homomorphisms, belonging to the four central pairs above, are
$u : A \to B$, $u' : A' \to B'$,
$\til{u} : \til{A} \to \til{B}$ and 
$\til{u}' : \til{A}' \to \til{B}'$.

From here until Lemma \ref{lem:827} (inclusive), we also assume the next 
condition. 

\begin{cond} \label{cond:930} \mbox{}
\begin{enumerate}
\rmitem{i} The homomorphism $\til{u}' : \til{A}' \to \til{B}'$ is 
noncommutative semi-free (Definition \ref{dfn:60}(2)). 
\rmitem{ii} The homomorphisms 
$\til{v}_0, \til{v}_1 : \til{A}' \to \til{A}$ are equal. 
\end{enumerate}
\end{cond}

In view of item (ii) in Condition \ref{cond:930}, we may write 
$\til{v} := \til{v}_0 = \til{v}_1$; this is a homomorphism 
$\til{v} : \til{A}' \to \til{A}$
in $\cat{DGR}^{\leq 0}_{\mrm{sc}}$,
lying above $v : A' \to A$. 
The DG ring input of Setup \ref{set:930} and Condition \ref{cond:930} can be 
summarized as the following commutative diagrams in the category 
$\cat{DGR}^{\leq 0}\centover \til{A}'$,
for $i = 0, 1$:

\[ \UseTips \xymatrix @C=5ex @R=5ex {
& 
\til{B}'
\ar[dr]^{w \circ s'}
\\
\til{A}'
\ar[rr]
\ar[ur]^{\til{u}'} 
\ar[dr]_{\til{u} \circ \til{v}}
& 
&
B
\\
&
\til{B}
\ar[ur]_{s} 
}
\qquad  \qquad 
\xymatrix @C=5ex @R=5ex {
& 
\til{B}' 
\ar[dr]^{w \circ s'}
\ar[dd]_{\til{w}_i} 
\\
\til{A}'
\ar[ur]^{\til{u}'}
\ar[dr]_{\til{u} \circ \til{v}}
& 
&
B
\\
&
\til{B}
\ar[ur]_{s}
} \]

Recall the cylinder DG ring from Definition \ref{dfn:700}. 

\begin{lem} \label{lem:640}
Under Condition \tup{\ref{cond:930}}, there is a homomorphism 
\[ \til{w}_{\mrm{cyl}} : \til{B}' \to \opn{Cyl}(\til{B}) \] 
in $\cat{DGR} \centover \til{A}'$, such that diagram \tup{(\ref{eqn:359})}
is commutative for $i = 0, 1$.
\end{lem}

\begin{equation} \label{eqn:359}
\UseTips \xymatrix @C=8ex @R=6ex {
\til{B}'
\ar[r]^(0.4){ \til{w}_{\mrm{cyl}} }
\ar[d]_{s'}
\ar@(u,u)[rr]^{ \til{w}_i }
&
\opn{Cyl}(\til{B})
\ar[r]^(0.6){ \eta_i }
\ar[d]_{ \opn{Cyl}(s) }
&
\til{B}
\ar[d]_{s}
\\
B'
\ar[r]^(0.4){\ep \circ w}
&
\opn{Cyl}(B)
\ar[r]^(0.6){\eta_i}
&
B
}
\end{equation}
 
\begin{proof}
We know that $\til{u}' : \til{A}' \to \til{B}'$ is noncommutative semi-free, 
and $s$ is a surjective quasi-iso\-morphism. So Theorem \ref{thm:300} applies.
We obtain an $\til{A}'$-linear DG ring homotopy 
$\ga : \til{w}_0 \twoto \til{w}_1$ such that $s \circ \ga = 0$.
By Proposition \ref{prop:300} we deduce the 
existence of a DG ring homomorphism 
$\til{w}_{\mrm{cyl}} : \til{B}' \to \opn{Cyl}(\til{B})$. 
The formula, for $b \in \til{B}'$, is 
\[ \til{w}_{\mrm{cyl}}(b) = 
\bmat{\til{w}_0(b) & \ \xi \cd \ga(b) \\[0.3em] 0 & \til{w}_1(b)} 
. \]
This shows the commutativity of the half-moon in the diagram. 
Next, because the element $\xi$ commutes with the homomorphism $s$, and 
because $s \circ \ga = 0$, we have  
\[ \opn{Cyl}(s) (\til{w}_{\mrm{cyl}}(b)) = 
\bmat{ s(\til{w}_0(b)) & \ s(\xi \cd \ga(b)) 
\\[0.3em] 0 & s(\til{w}_1(b))} =  
\bmat{ w(s'(b)) & 0 \\ 0 & w(s'(b)) } . \]
We deduce the commutativity of the first square in the diagram. 
The second square is trivially commutative.
\end{proof}

There are central homomorphisms 
$\ep \circ u : A \to \opn{Cyl}(B)$
and 
$\ep \circ \til{u} : \til{A} \to \opn{Cyl}(\til{B})$, 
and thus two more central pairs
$\opn{Cyl}(B) / A$ and $\opn{Cyl}(\til{B}) / \til{A}$. 
These central pairs fit into a commutative diagram 

\begin{equation} \label{eqn:942}
\UseTips \xymatrix @C=10ex @R=8ex {
\til{B}' / \til{A}'
\ar[r]^(0.45){ \til{w}_{\mrm{cyl}} / \til{v} }
\ar[d]_{ s' / r' }
\ar@(u,u)[rr]^{ \til{w}_i / \til{v} }
&
\opn{Cyl}(\til{B}) / \til{A}
\ar[r]^(0.55){ \eta_i / \opn{id} }
\ar[d]_{ \opn{Cyl}(s) / r }
&
\til{B} / \til{A}
\ar[d]_{ s / r }
\\
B' / A'
\ar[r]^(0.45){ (\ep \circ w) / v }
\ar@(d,d)[rr]_{ w / v }
&
\opn{Cyl}(B) / A
\ar[r]^(0.55){ \eta_i / \opn{id} }
&
B / A
} 
\end{equation}

\medskip \noindent
in the category $\cat{PDGR}$, for $i = 0, 1$. Moreover, the morphisms between 
the pairs in the lower row are central, namely they are in 
$\cat{PDGR}_{\vec{\mrm{ce}}}$. 
The pairs in the upper row are K-flat, and the vertical morphisms are 
quasi-isomorphisms. 

Consider the DG module 
$\opn{Cyl}(M^{\mrm{l}}) \in \cat{M}(\opn{Cyl}(B))$. 
Define homomorphisms
\[ \eta_0^{\vee} : M^{\mrm{l}} \to \opn{Cyl}(M^{\mrm{l}}) , \quad
\eta_0^{\vee}(m) := \bmat{ m & 0 \\ 0 & 0 } \]
and 
\[ \eta_1^{\vee} : M^{\mrm{l}} \to \opn{Cyl}(M^{\mrm{l}}) , \quad
\eta_1^{\vee}(m) := \bmat{ 0 & 0 \\ 0 & m } . \]
Then 
$\eta_i^{\vee} : \opn{For}_{\eta_i}(M^{\mrm{l}}) \to \opn{Cyl}(M^{\mrm{l}})$
is a homomorphism in $\cat{M}(\opn{Cyl}(B))$. 
Next, define a homomorphism
\[ \ep^{\vee} : \opn{Cyl}(M^{\mrm{l}}) \to M^{\mrm{l}} , \quad
\ep^{\vee}(\bmat{ m_0 & n \\ 0 & m_1 }) :=  m_0 + m_1 . \]
Then 
$\ep^{\vee} : \opn{For}_{\ep}(\opn{Cyl}(M^{\mrm{l}})) \to M^{\mrm{l}}$
is a homomorphism in $\cat{M}(B)$. 
And 
$\ep^{\vee} \circ \eta_i^{\vee} = \opn{id}$. 
All this can be done for 
$M^{\mrm{r}}$ too. 

Consider the next commutative diagram, for $i = 0, 1$, 
in the category 
$\cat{D}(B') \times \cat{D}(B'^{\mrm{\, op}})$.

\begin{equation} \label{eqn:943}
 \UseTips \xymatrix @C=14ex @R=6ex {
(M'^{\, \mrm{l}}, M'^{\, \mrm{r}})
&
\bigl( \opn{Cyl}(M^{\mrm{l}}), \opn{Cyl}(M^{\mrm{r}}) \bigr)
\ar[l]_(0.55){ ( \th^{\mrm{l}} \circ \ep^{\vee}, 
\th^{\mrm{r}} \circ \ep^{\vee}) } 
&
(M^{\mrm{l}}, M^{\mrm{r}})
\ar[l]_(0.4){ (\eta_i^{\vee}, \eta_i^{\vee}) } 
\ar@(d,d)[ll]^{ (\th^{\mrm{l}},  \th^{\mrm{r}}) }
} 
\end{equation}

\begin{lem} \label{lem:827}
Under Condition \tup{\ref{cond:930}}, there is equality 
\begin{equation} \label{eqn:944}
\opn{Rect}_{w / v}^{\til{w}_0 / \til{v}}(\th^{\mrm{l}},  \th^{\mrm{r}}) 
= 
\opn{Rect}_{w / v}^{\til{w}_1 / \til{v}}(\th^{\mrm{l}},  \th^{\mrm{r}})
\end{equation}
of morphisms 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) \to
\opn{Rect}_{B' / A'}^{\til{B}' / \til{A}'}(M'^{\, \mrm{l}}, M'^{\, \mrm{r}}) \]
in $\cat{D}(B'^{\mrm{\, ce}})$.
\end{lem}

\begin{proof}
Step 1. Here we assume that
$B' / A' = B / A$, 
$\til{B}' / \til{A}' = \til{B} / \til{A}$, 
the morphisms $w / v$,  $\til{w}_0 / \til{v}$ and $\til{w}_1 / \til{v}$
are the identity automorphisms,
and there is equality $s' / r' = s / r$.  
Also we assume that 
$(M'^{\, \mrm{l}}, M'^{\, \mrm{r}}) = (M^{\mrm{l}}, M^{\mrm{r}})$, 
and the morphism 
$(\th^{\mrm{l}},  \th^{\mrm{r}})$ is the identity automorphism. 
We may also assume that 
$\til{w}_{\mrm{cyl}} = \ep \circ \til{w}$,
but that is not important. 
By functoriality (Proposition \ref{prop:940}), we have
\begin{equation} \label{eqn:940}
\opn{Rect}_{\ep \circ w / v}^{\til{w}_{\mrm{cyl}} / \til{v}}
(\th^{\mrm{l}} \circ \ep^{\vee},  \th^{\mrm{r}} \circ \ep^{\vee})
\circ 
\opn{Rect}_{\eta_i / \opn{id}}^{\eta_i / \opn{id}}
(\eta_i^{\vee}, \eta_i^{\vee})
= \opn{Rect}_{w / v}^{\til{w}_i / \til{v}}(\th^{\mrm{l}},  \th^{\mrm{r}}) ,
\end{equation}
in $\cat{D}(B^{\mrm{ce}})$, for $i = 0, 1$. 
Compare to diagrams (\ref{eqn:942}) and (\ref{eqn:943}). 
By Lemma \ref{lem:917}, all three morphisms above are isomorphisms.
Some caution is needed here: the morphism 
$\opn{Rect}_{\eta_i / \opn{id}}^{\eta_i / \opn{id}}
(\eta_i^{\vee}, \eta_i^{\vee})$
is actually in the category 
$\cat{D}(\opn{Cyl}(B)^{\mrm{ce}})$, and the forgetful functor 
\[ \opn{For}_{\ep^{\mrm{ce}}} : \cat{D}(\opn{Cyl}(B)^{\mrm{ce}}) \to 
\cat{D}(B^{\mrm{ce}}) \]
has been hidden. But but we know (see Proposition \ref{prop:700}) that the DG 
ring homomorphism 
$\ep : B \to \opn{Cyl}(B)$ induces an isomorphism 
$\ep^{\mrm{ce}} :  B^{\mrm{ce}} \to \opn{Cyl}(B)^{\mrm{ce}}$.
Therefore the functor 
$\opn{For}_{\ep^{\mrm{ce}}}$ is an equivalence. 

Since $\til{w}_1 = \til{w}_0$ here, formula (\ref{eqn:940}) for $i = 0, 1$
leads us to conclude that 
\begin{equation} \label{eqn:930}
\opn{Rect}_{\eta_1 / \opn{id}}^{\eta_1 / \opn{id}}
(\eta_1^{\vee}, \eta_1^{\vee}) = 
\opn{Rect}_{\eta_0 / \opn{id}}^{\eta_0 / \opn{id}} 
(\eta_0^{\vee}, \eta_0^{\vee}), 
\end{equation}
as isomorphisms 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) \to
\opn{Rect}_{\opn{Cyl}(B) / A}^{\opn{Cyl}(\til{B}) / \til{A}}
\bigl( \opn{Cyl}(M^{\mrm{l}}), \opn{Cyl}(M^{\mrm{r}}) \bigr) \]
in $\cat{D}(\opn{Cyl}(B)^{\mrm{ce}})$.
 
\medskip \noindent 
Step 2. Now there are no special assumptions. We choose a homomorphism 
$\til{w}_{\mrm{cyl}}$ as in Lemma \ref{lem:640}.
By functoriality, we again have the equalities (\ref{eqn:940}), for 
$i = 0, 1$. Formula (\ref{eqn:930}) from part (1) applies here, because it does 
not depend on $B' / A'$. We deduce that (\ref{eqn:944}) holds. 
\end{proof}

Here is the key technical result of the paper (the noncommutative version). 

\begin{thm}[Homotopy Invariance] \label{thm:840}
In the situation of Setup \tup{\ref{set:930}}, there is equality 
\[ \opn{Rect}_{w / v}^{\til{w}_0 / \til{v}_0}(\th^{\mrm{l}},  \th^{\mrm{r}}) 
= 
\opn{Rect}_{w / v}^{\til{w}_1 / \til{v}_1}(\th^{\mrm{l}},  \th^{\mrm{r}}) \]
of morphisms 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) \to
\opn{Rect}_{B' / A'}^{\til{B}' / \til{A}'}(M'^{\, \mrm{l}}, M'^{\, \mrm{r}}) \]
in $\cat{D}(B'^{\mrm{\, ce}})$.
\end{thm}

\begin{proof}
Choose the following resolutions in $\cat{PDGR}^{\leq 0}$: 
a strict K-flat resolution \lb
$s^{\diamondsuit} / \mrm{id} : \til{B}^{\diamondsuit} / A \to B / A$, 
a strict noncommutative semi-free resolution 
$s^{\heartsuit} / \mrm{id} : \til{B}^{\heartsuit} / \til{A} \to 
\til{B} / \til{A}$, 
and a strict noncommutative semi-free resolution
$s'^{\, \diamondsuit} / \mrm{id} : 
\til{B}'^{\, \diamondsuit} / \til{A}' \lb \to \til{B}' / \til{A}'$. 
These exist by Theorem \ref{thm:305}. 

There is a homomorphism 
$s^{\dag} : \til{B}^{\heartsuit} \to \til{B}^{\diamondsuit}$
in $\cat{DGR}^{\leq 0} \centover \til{A}$
such that 
$s^{\diamondsuit} \circ s^{\dag} = s \circ s^{\heartsuit}$.
For $i = 0, 1$ there is a homomorphism 
$\til{w}_i^{\diamondsuit} : \til{B}'^{\, \diamondsuit} \to 
\til{B}^{\heartsuit}$
in $\cat{DGR}^{\leq 0} \centover \til{A}'$, such that 
$s^{\heartsuit} \circ \til{w}_i^{\diamondsuit} = \til{w}_i 
\circ s'^{\, \diamondsuit}$.
These homomorphisms exist by Theorem \ref{thm:306}. 

The resolutions and the homomorphisms between them, from the two paragraphs 
above, fit into the following commutative diagram in $\cat{PDGR}^{\leq 0}$, for 
$i = 0, 1$. 
The central pairs
$\til{B}'^{\, \diamondsuit} / \til{A}'$ and 
$\til{B}' / \til{A}'$ are K-flat resolutions of $B' / A'$, and 
the central pairs
$\til{B}^{\heartsuit} / \til{A}$, 
$\til{B}^{\diamondsuit} / A$ and $\til{B} / \til{A}$
are K-flat resolutions of $B / A$.

\begin{equation} \label{eqn:946}
\UseTips \xymatrix @C=10ex @R=8ex {
&
&
\til{B}^{\heartsuit} / \til{A}
\ar[d]_{ s^{\heartsuit} / \mrm{id} }
\ar[dr]^{ s^{\dag} / r }
\\
\til{B}'^{\, \diamondsuit} / \til{A}'
\ar @/^1.5em/ [urr]^{ \til{w}_i^{\diamondsuit} / \til{v}_i }
\ar[r]^{ s'^{\, \diamondsuit} / \mrm{id} }
\ar[dr]_{ (s' \circ s'^{\, \diamondsuit}) / r' }
&
\til{B}' / \til{A}'
\ar[r]^{ \til{w}_i / \til{v}_i }
\ar[d]^{ s' / r' }
&
\til{B} / \til{A}
\ar[d]^{ s / r }
&
\til{B}^{\diamondsuit} / A
\ar[dl]^{ s^{\diamondsuit} / \mrm{id} }
\\
&
B' / A'
\ar[r]^{ w / v }
&
B / A
}
\end{equation}

\medskip
Let us introduce the temporary abbreviations 
\[ \opn{R}(\til{B} / \til{A}) := 
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) , \quad
\opn{R}(\til{B}' / \til{A}') := 
\opn{Rect}_{B' / A'}^{\til{B}' / \til{A}'}(M'^{\, \mrm{l}}, M'^{\, \mrm{r}}) , 
\]
\[ \opn{R}(\til{w}_i / \til{v}_i) :=
\opn{Rect}_{w / v}^{\til{w}_i / \til{v}_i}(\th^{\mrm{l}},  \th^{\mrm{r}}) , 
\quad
\opn{R}(s^{\dag} / r) :=
\opn{Rect}_{\mrm{id} / \mrm{id}}^{s^{\dag} / r}(\mrm{id} , \mrm{id}) , \]
etc. Applying functoriality (Proposition \ref{prop:940}) to the commutative 
diagram (\ref{eqn:946}), we obtain a commutative diagram 

\begin{equation} \label{eqn:947}
\UseTips \xymatrix @C=10ex @R=8ex {
&
&
\opn{R}(\til{B}^{\heartsuit} / \til{A})
\ar @/_1.5em/ [dll]_{ \opn{R}(\til{w}_i^{\diamondsuit} / \til{v}_i) }
\\
\opn{R}(\til{B}'^{\, \diamondsuit} / \til{A}')
&
\opn{R}(\til{B}' / \til{A}')
\ar[l]_(0.45){ \opn{R}(s'^{\, \diamondsuit} / \mrm{id}) }
&
\opn{R}(\til{B} / \til{A})
\ar[u]^{ \opn{R}(s^{\heartsuit} / \mrm{id}) }
\ar[l]_{ \opn{R}(\til{w}_i / \til{v}_i) }
&
\opn{R}(\til{B}^{\diamondsuit} / A)
\ar[ul]_{ \opn{R}(s^{\dag} / r) }
}
\end{equation}

\noindent
in $\cat{D}(B'^{\, \mrm{ce}})$, for $i = 0, 1$. All the morphisms whose names 
contain the letter ``s'' are isomorphisms. 

Note that 
$r \circ \til{v}_i = v \circ r'$. We get a commutative diagram 

\begin{equation} \label{eqn:948}
\UseTips \xymatrix @C=10ex @R=8ex {
&
&
\opn{R}(\til{B}^{\heartsuit} / \til{A})
\ar @/_1.5em/ [dll]_{ \opn{R}(\til{w}_i^{\diamondsuit} / \til{v}_i) }
\\
\opn{R}(\til{B}'^{\, \diamondsuit} / \til{A}')
&
&
&
\opn{R}(\til{B}^{\diamondsuit} / A)
\ar[ul]_{ \opn{R}(s^{\dag} / r) }
\ar[lll]_{ \opn{R}( (s^{\dag} \circ \til{w}_i^{\diamondsuit}) / (v \circ r')) } 
}
\end{equation}

\noindent
in $\cat{D}(B'^{\, \mrm{ce}})$, for $i = 0, 1$.
Because Condition \ref{cond:930} is satisfied for the morphisms of resolutions 
\[ (s^{\dag} \circ \til{w}_i^{\diamondsuit}) / (v \circ r') : 
\til{B}'^{\, \diamondsuit} / \til{A}' \to 
\til{B}^{\diamondsuit} / A , \]
Lemma \ref{lem:827} tells us that 
\[ \opn{R}( (s^{\dag} \circ \til{w}_0^{\diamondsuit}) / (v \circ r')) =
\opn{R}( (s^{\dag} \circ \til{w}_1^{\diamondsuit}) / (v \circ r')) . \]
Since $\opn{R}(y^{\dag} / r)$ is an isomorphism, we conclude that 
\[ \opn{R}(\til{w}_0^{\diamondsuit} / \til{v}_0) = 
\opn{R}(\til{w}_1^{\diamondsuit} / \til{v}_1) . \]
Going back to diagram (\ref{eqn:947}), and using the fact that both 
$\opn{R}(s^{\heartsuit} / \mrm{id})$ and 
$\opn{R}(s'^{\, \diamondsuit} / \mrm{id})$
are isomorphisms, we see that 
\[ \opn{R}(\til{w}_0^{} / \til{v}_0) = \opn{R}(\til{w}_1^{} / \til{v}_1) . \]
\end{proof}

\begin{thm}[Existence of Rectangles] \label{thm:985}
Let $A$ be a commutative DG ring, and let $A \to B$ be a central homomorphism 
of nonpositive DG rings. Given a pair 
\[ (M^{\mrm{l}}, M^{\mrm{r}}) \in \cat{D}(B) \times \cat{D}(B^{\mrm{op}}) , \]
there is a DG module 
\[ \opn{Rect}_{B / A}(M^{\mrm{l}}, M^{\mrm{r}}) \in \cat{D}(B^{\mrm{ce}}) , \]
unique up to a unique isomorphism, 
together with an isomorphism
\[ \opn{rect}^{\til{B} / \til{A}} : 
\opn{Rect}_{B / A}(M^{\mrm{l}}, M^{\mrm{r}}) \iso 
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})  \]
for every K-flat resolution 
$\til{B} / \til{A}$ of $B / A$ in  $\cat{PDGR}^{\leq 0}$,
such that the following condition holds. 

\begin{enumerate}
\item[($*$)] Let 
$\til{w} / \til{v} : \til{B}' / \til{A}' \to  \til{B} / \til{A}$
be a morphism of K-flat resolutions of $B / A$ in  $\cat{PDGR}^{\leq 0}$. Then  
the diagram 
\[ \UseTips \xymatrix @C=20ex @R=8ex {
\opn{Rect}_{B / A}(M^{\mrm{l}}, M^{\mrm{r}})
\ar[d]_{ \opn{rect}^{\til{B} / \til{A}} }
\ar[dr]^{ \quad \opn{rect}^{\til{B}' / \til{A}'} }
\\
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})
\ar[r]_{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}
(\opn{id}_{M^{\mrm{l}}}, \opn{id}_{M^{\mrm{r}}}) }
&
\opn{Rect}_{B / A}^{\til{B}' / \til{A}'}(M^{\mrm{l}}, M^{\mrm{r}}) 
} \]
of isomorphisms in $\cat{D}(B^{\mrm{ce}})$ is commutative. 
\end{enumerate}
\end{thm}

\begin{proof}
Choose a commutative semi-free resolution $\til{A}_{\mrm{un}} / \Z$ 
of $A / \Z$, 
and then choose a noncommutative semi-free resolution
$\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}$
of $B / \til{A}_{\mrm{un}}$, both in $\cat{PDGR}^{\leq 0}$.
This is possible by Theorem \ref{thm:305}. (The subscript ``un'' stands for 
``universal''.) Note that 
$\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}$
is a K-flat resolution of $B / A$. Define 
\[ \opn{Rect}_{B / A}(M^{\mrm{l}}, M^{\mrm{r}}) :=
\opn{Rect}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}
(M^{\mrm{l}}, M^{\mrm{r}}) . \]

Consider any K-flat resolution $\til{B} / \til{A}$ of $B / A$. According to 
Theorem \ref{thm:306} there is a morphism 
\[ \til{w}_{\mrm{un}} / \til{v}_{\mrm{un}} :
\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}} \to \til{B} / \til{A}  \]
of resolutions of $B / A$. We define
\[ \opn{rect}^{\til{B} / \til{A}} : 
\opn{Rect}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}
(M^{\mrm{l}}, M^{\mrm{r}}) \iso 
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) \]
to be 
\[ \opn{rect}^{\til{B} / \til{A}} := 
\opn{Rect}_{\mrm{id} / \mrm{id}}
^{\til{w}_{\mrm{un}} / \til{v}_{\mrm{un}}}
(\opn{id}_{M^{\mrm{l}}}, \opn{id}_{M^{\mrm{r}}})^{-1} . \]
Theorem \ref{thm:840} tells us that the isomorphism
$\opn{rect}^{\til{B} / \til{A}}$
does not depend on the choice of 
$\til{w}_{\mrm{un}} / \til{v}_{\mrm{un}}$. 

It remains to verify condition ($*$). Suppose 
$\til{B}' / \til{A}'$ is another K-flat resolution of $B / A$, and 
$\til{w} / \til{v} : \til{B}' / \til{A}' \to  \til{B} / \til{A}$
is a morphism of resolutions of $B / A$. Choose a morphism of resolutions 
\[ \til{w}'_{\mrm{un}} / \til{v}'_{\mrm{un}} :
\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}} \to \til{B}' / \til{A}'  . \]
We have a diagram 
\[ \UseTips \xymatrix @C=20ex @R=8ex {
\opn{Rect}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}
(M^{\mrm{l}}, M^{\mrm{r}}) 
\\
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})
\ar[u]^{ \opn{Rect}_{\mrm{id} / \mrm{id}}
^{\til{w}_{\mrm{un}} / \til{v}_{\mrm{un}}}(\opn{id}, \opn{id}) }
\ar[r]_{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\opn{id}, \opn{id}) }
&
\opn{Rect}_{B / A}^{\til{B}' / \til{A}'}(M^{\mrm{l}}, M^{\mrm{r}}) 
\ar[ul]_{ \quad \opn{Rect}_{\mrm{id} / \mrm{id}}
^{\til{w}'_{\mrm{un}} / \til{v}'_{\mrm{un}}}(\opn{id}, \opn{id}) }
} \]
of isomorphisms in $\cat{D}(B^{\mrm{ce}})$.
Proposition \ref{prop:940} says that 
\[ \opn{Rect}_{\mrm{id} / \mrm{id}}
^{\til{w}'_{\mrm{un}} / \til{v}'_{\mrm{un}}}(\opn{id}, \opn{id})
\circ 
\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\opn{id}, \opn{id}) = 
\opn{Rect}_{\mrm{id} / \mrm{id}}
^{ (\til{w} \circ \til{w}'_{\mrm{un}}) / 
(\til{v} \circ \til{v}'_{\mrm{un}})}(\opn{id}, \opn{id}) . \]
Finally, Theorem \ref{thm:840} says that 
\[ \opn{Rect}_{\mrm{id} / \mrm{id}}
^{ (\til{w} \circ \til{w}'_{\mrm{un}}) / 
(\til{v} \circ \til{v}'_{\mrm{un}})}(\opn{id}, \opn{id}) = 
\opn{Rect}_{\mrm{id} / \mrm{id}}
^{\til{w}_{\mrm{un}} / \til{v}_{\mrm{un}}}(\opn{id}, \opn{id}) . \]
We that the diagram in condition ($*$) is indeed commutative.
\end{proof}

\begin{rem} \label{rem:720}
Let $\K$ be a regular finite dimensional noetherian commutative ring, and let 
$A$ be a cohomologically pseudo-noetherian commutative DG ring 
(see \cite[Section 3]{Ye2}). Suppose $\K \to A$ is a DG ring homomorphism, 
such that $\K \to \opn{H}^0(A)$ is essentially finite type.
Let $\cat{D}^+_{\mrm{f}}(A)$ be the full subcategory of $\cat{D}(A)$
consisting of DG modules whose cohomology is bounded below, 
and whose cohomology modules are finite  over $\opn{H}^0(A)$.

For $M, N \in \cat{D}^+_{\mrm{f}}(A)$ let us write 
\[ M \ot_{A / \K}^! N := \opn{Rect}_{A / \K}(M, N) \in \cat{D}(A) . \]
In \cite{Ga}, D. Gaitsgory states that when $\K$ is a field of 
characteristic $0$, this is operation makes $\cat{D}^+_{\mrm{f}}(A)$ into a 
{\em monoidal category}. No proof of this statement is given in \cite{Ga}.

Now assume $A$ is a ring (so it is just a noetherian commutative ring, 
essentially finite type over $\K$). According to \cite{YZ3} and its corrections 
in \cite{Ye5}, there is a {\em rigid dualizing complex} $R_{A / \K}$ over $A$ 
relative to $\K$. The functor $D := \opn{RHom}_A(-, R_{A / \K})$ is a duality 
of the category 
$\cat{D}_{\mrm{f}}(A)$, and it exchanges $\cat{D}^+_{\mrm{f}}(A)$
with $\cat{D}^-_{\mrm{f}}(A)$.
Recently L. Shaul \cite{Sh1} showed that there is a bifunctorial isomorphism 
\begin{equation} \label{eqn:390}
 M \ot_{A / \K}^! N \cong D \bigl( D(M) \ot^{\mrm{L}}_A D(N) \bigr)
\end{equation}
for $M, N \in \cat{D}^{\mrm{b}}_{\mrm{f}}(A)$. The proof relies on the 
reduction formula for Hochschild cohomology \cite[Theorem 1]{AILN}, \cite{Sh2}. 
The isomorphism (\ref{eqn:390}) implies that the operation 
$- \ot_{A / \K}^! -$ is a monoidal structure on the subcategory
$\cat{D}^{\mrm{b}}_{\mrm{f}}(A)_{\mrm{fid}}$
of $\cat{D}^{\mrm{b}}_{\mrm{f}}(A)$
consisting of complexes with finite injective dimension. The monoidal 
unit is $R_{A / \K}$. 

Work in progress by Shaul indicates that the result above 
should hold in greater generality: $A$ can be as in the first paragraph of 
the remark, and $M, N$ can be any objects in  $\cat{D}^+_{\mrm{f}}(A)$.
\end{rem}
