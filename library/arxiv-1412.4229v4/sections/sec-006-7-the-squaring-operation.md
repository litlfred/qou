---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-006-7-the-squaring-operation
section_title: "The Squaring Operation"
section_number: 7
pages: 37-43
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.656
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
\label{sec:squaring}

In this section all DG rings are commutative; namely, we work 
inside the category $\cat{DGR}_{\mrm{sc}}^{\leq 0}$. See Definition 
\ref{dfn:876}. 
The category $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$ of commutative pairs of DG rings 
was introduced in Definition \ref{dfn:911}(2); it is a full subcategory of the 
category $\cat{PDGR}$ of central pairs of DG rings. 

\begin{dfn} \label{dfn:955}
\begin{enumerate}
\item Let $B / A$ be an object of $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$.
A {\em K-flat resolution} of $B / A$ in 
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$
is a resolution 
$s / r : \til{B} / \til{A} \to B / A$
in the sense of Definition \ref{dfn:912}, such that the pair
$\til{B} / \til{A}$ is commutative and K-flat (Definition \ref{dfn:60}(3)). 

\item Morphisms of resolutions in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
and resolutions of morphisms in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
are as in Definition \ref{dfn:913}, but all the pairs are now commutative. 
\end{enumerate}
\end{dfn}

\begin{prop} \label{prop:1010}
Any object and any morphism in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$
admits a K-flat resolution.
\end{prop}

\begin{proof}
Like the proof of Corollary \ref{cor:980}, but using commutative semi-free 
resolutions. 
\end{proof}

For a commutative DG ring $B$ we have $B^{\mrm{ce}} = B$ of course. This is 
used in the following definitions. 

\begin{dfn} \label{dfn:950}
Let $B / A$ be a pair of commutative DG rings, and let $M$ be a DG 
$B$-module. Given a K-flat resolution $\til{B} / \til{A}$ of $B / A$ in  
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, 
we let 
\[ \opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) := 
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M, M) \in \cat{D}(B) . \]
See Proposition \ref{prop:915}. 
\end{dfn}

\begin{dfn} \label{dfn:956}
Let $w / v : B' / A' \to B / A$ be a morphism in  
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, let 
$M \in \cat{D}(B)$, let $M' \in \cat{D}(B')$, and let 
$\th : M \to M'$
be a morphism in $\cat{D}(B')$.
Given a K-flat resolution
$\til{w} / \til{v} : \til{B}' / \til{A}' \to \til{B} / \til{A}$
of $w / v$ in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
we define
\[ \opn{Sq}_{w / v}^{\til{w} / \til{v}}(\th) :
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \to 
\opn{Sq}_{B' / A'}^{\til{B}' / \til{A}'}(M') \]
to be the morphism 
\[ \opn{Sq}_{w / v}^{\til{w} / \til{v}}(\th) :=
\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\th, \th) \]
in $\cat{D}(B')$ from Proposition \ref{prop:916}.
\end{dfn}

\begin{rem} \label{rem:965}
As explained in Remark \ref{rem:950}, we can write 
\[ \opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) = 
\opn{RHom}_{\til{B}^{\mrm{en}}}(B, M \ot_{\til{A}}^{\mrm{L}} M) . \]
However, the morphism $\opn{Sq}_{w / v}^{\til{w} / \til{v}}(\th)$
in Definition \ref{dfn:956} is not standard, so we 
have to use the more explicit approach with compound resolutions, as was 
done in Section \ref{sec:pairs-DG-modules}. 

Still, here we can simplify matters by using symmetric compound resolutions.
A symmetric compound resolution of a DG $B$-module $M$ is data 
$\bsym{P} = (\til{P}, \til{I}; \al, \be)$, 
consisting of a K-flat resolution 
$\al : \til{P} \to M$ in $\cat{M}(\til{B})$, 
and a K-injective resolution 
$\be : \til{P}^{\mrm{en}} = \til{P} \ot_{\til{A}} \til{P} \to \til{I}$
in $\cat{M}(\til{B}^{\mrm{en}})$.

Likewise, a morphism $\th : M \to M'$ can be resolved by a symmetric compound
morphism $\bsym{\eta} : \bsym{P} \to \bsym{P}'$,
where 
$\bsym{\eta} = (\til{Q}; \ga, \til{\th}, \eta)$
consists of  a K-projective resolution
$\ga : \til{Q} \to \til{P}$ in $\cat{M}(\til{B}')$;
a homomorphism
$\til{\th} : \til{Q} \to \til{P}'$
in $\cat{M}(\til{B}')$ lifting $\th$; and a homomorphism
$\eta : \til{I} \to \til{I}'$ in 
$\cat{M}(\til{B}'^{\, \mrm{en}})$ lifting 
\[ \til{\th} \ot \til{\th} : \til{Q} \ot_{\til{A}'} \til{Q} \to 
\til{P}' \ot_{\til{A}'} \til{P}' . \]
\end{rem}

Here is the key technical result of our paper (Theorem \ref{thm:960} in the 
Introduction). Actually, it is just a special case of Theorem \ref{thm:840}. 

\begin{thm}[Homotopy Invariance] \label{thm:950}
Let $w / v : B' / A' \to B / A$ be a morphism in  
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, let 
$M \in \cat{D}(B)$, let $M' \in \cat{D}(B')$, and let 
$\th : M \to M'$ be a morphism in $\cat{D}(B')$.
Suppose
$\til{B} / \til{A}$ and $\til{B}' / \til{A}'$
are K-flat resolutions of 
$B / A$ and $B' / A'$ respectively in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
and  
\[ \til{w}_0 / \til{v}_0,  \, \til{w}_1 / \til{v}_1 :
\til{B}' / \til{A}' \to \til{B} / \til{A} \]
are morphisms of resolutions above $w / v$. Then the morphisms 
\[ \opn{Sq}_{w / v}^{\til{w}_0 / \til{v}_0}(\th), \,
\opn{Sq}_{w / v}^{\til{w}_1 / \til{v}_1}(\th) :
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \to 
\opn{Sq}_{B' / A'}^{\til{B}' / \til{A}'}(M') \]
in $\cat{D}(B')$ are equal. 
\end{thm}
 
\begin{proof}
Take $M^{\mrm{l}} = M^{\mrm{r}} := M$, 
$M'^{\, \mrm{l}} = M'^{\, \mrm{r}} := M'$, and
$\th^{\mrm{l}} = \th^{\mrm{r}} := \th$
in Theorem \ref{thm:840}.
\end{proof}

This brings us to the first main theorem of the paper (which is Theorem 
\ref{thm:965} in the Introduction). 

\begin{thm}[Existence of Squares] \label{thm:860} 
Let $A \to B$ be a homomorphism of commutative DG rings, and let $M$ be a DG 
$B$-module. There is a DG module 
$\opn{Sq}_{B / A}(M)$, 
unique up to a unique isomorphism in $\cat{D}(B)$, 
together with an isomorphism 
\[ \opn{sq}^{\til{B} / \til{A}} : \opn{Sq}_{B / A}(M) \iso 
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \]
in $\cat{D}(B)$ for each K-flat resolution 
$\til{B} / \til{A}$ of $B / A$ in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
satisfying the following condition. 

\begin{enumerate}
\item[($*$)] Let 
$\til{w} / \til{v} : \til{B}' / \til{A}' \to  \til{B} / \til{A}$
be a morphism of K-flat resolutions of $B / A$ in 
$\cat{PDGR}_{\mrm{sc}}^{\leq 0}$. 
Then there is equality
\[ \opn{Sq}_{\mrm{id} / \mrm{id}}^{\til{w} / \til{v}}(\opn{id}_{M}) = 
\opn{sq}_{}^{\til{B}' / \til{A}'} \circ \,
(\opn{sq}_{}^{\til{B} / \til{A}})^{-1} \]
of isomorphisms
$\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \iso 
\opn{Sq}_{B / A}^{\til{B}' / \til{A}'}(M)$
in $\cat{D}(B)$.
\end{enumerate}
\end{thm}

\begin{proof}
The proof is very similar to that of Theorem \ref{thm:985}: we fix a 
universal K-flat resolution of $B / A$; but now it has to be a commutative 
resolution. So let $\til{A}_{\mrm{un}} / \Z$ be a commutative semi-free 
resolution of $A / \Z$, and let 
$\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}$
be a commutative semi-free resolution
of $B / \til{A}_{\mrm{un}}$, both in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$.
This is possible by Theorem \ref{thm:305}. Define 
\[ \opn{Sq}_{B / A}(M) :=
\opn{Sq}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}(M) . \]

Given any K-flat resolution 
$\til{B} / \til{A}$ of $B / A$ in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$,
Theorem \ref{thm:306} says there is a morphism of resolutions 
\[ \til{w}_{\mrm{un}} / \til{v}_{\mrm{un}} :
\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}} \to \til{B} / \til{A} . \]
We define the isomorphism
\[ \opn{sq}^{\til{B} / \til{A}} : 
\opn{Sq}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}(M) \iso 
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M) \]
to be 
\[ \opn{sq}^{\til{B} / \til{A}} := 
\opn{Sq}_{\mrm{id} / \mrm{id}}
^{\til{w}_{\mrm{un}} / \til{v}_{\mrm{un}}}(\opn{id}_{M})^{-1} . \]

The verification of condition ($*$) is the same as in the proof of Theorem 
\ref{thm:985}, except that here we use Theorem \ref{thm:950} instead of 
Theorem \ref{thm:840}.
\end{proof}

\begin{dfn} \label{dfn:1000}
A {\em triple in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$} is the data of 
homomorphisms $A \xar{u} B \xar{v} C$ in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$.
We refer to this triple as $C / B / A$.  

A {\em commutative K-flat resolution of $C / B / A$} is a 
triple 
$\til{A} \xar{\til{u}} \til{B} \xar{\til{v}} \til{C}$
in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$,
together with homomorphisms 
$r : \til{A} \to A$, $s : \til{B} \to B$ and $t : \til{C} \to C$
in $\cat{DGR}_{\mrm{sc}}^{\leq 0}$, such that:
\begin{itemize}
\item $r$ is a quasi-isomorphism, and $s, t$ are surjective quasi-isomorphisms.
\item $s \circ \til{u} = u \circ r$ and $t \circ \til{v} = v \circ s$.
\item $\til{u}$ and $\til{v} \circ \til{u}$ are K-flat. 
\end{itemize}
\end{dfn}

See diagram (\ref{eqn:966}) in the Introduction. 
A commutative K-flat resolution 
$\til{A} \xar{\til{u}} \til{B} \xar{\til{v}} \til{C}$
can be viewed as follows:  K-flat resolutions
$s / r : \til{B} / \til{A} \to B / A$ and 
$t / r : \til{C} / \til{A} \to C / A$
in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$, 
and a morphism of resolutions 
$\til{v} / \mrm{id}_{\til{A}} : \til{B} / \til{A} \to \til{C} / \til{A}$
above the morphism of pairs 
$v / \mrm{id}_{A} : B / A \to C / A$. 

\begin{prop} \label{prop:1011}
Commutative K-flat resolutions of triples exist. 
\end{prop}

\begin{proof}
This follows from Theorems \ref{thm:305} and \ref{thm:306}. Compare to the 
proof of Corollary \ref{cor:980}.
\end{proof}

Here is the second main theorem of the paper (which is Theorem \ref{thm:966} in 
the Introduction). 

\begin{thm}[Trace Functoriality] \label{thm:871}
Let $A \xar{} B \xar{v} C$ 
be homomorphisms of commutative DG rings, 
let $M \in \cat{D}(B)$, let $N \in \cat{D}(C)$, and let 
$\th : N \to M$ be a morphism in $\cat{D}(B)$.
There is a unique morphism 
\[ \opn{Sq}_{v / \mrm{id}_A}(\th) :
\opn{Sq}_{C / A}(N) \to \opn{Sq}_{B / A}(M) \]
in $\cat{D}(B)$, satisfying the condition\tup{:}
\begin{enumerate}
\item[($**$)] For any commutative K-flat resolution
$\til{A} \to \til{B} \xar{\til{v}} \til{C}$
of the triple $A \to B \xar{v} C$, there is equality 
\[ \opn{Sq}_{v / \mrm{id}_A}^{\til{v} / \mrm{id}_{\til{A}}}(\th) = 
 \opn{sq}^{\til{B} / \til{A}} \circ \opn{Sq}_{v / \mrm{id}_A}(\th) 
\circ (\opn{sq}^{\til{C} / \til{A}})^{-1} \]
of morphisms 
$\opn{Sq}_{C / A}^{\til{C} / \til{A}}(N) \to 
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M)$
in $\cat{D}(B)$.
\end{enumerate}
\end{thm}

\begin{proof}
We begin by choosing a universal K-flat resolution of the triple 
$A \xar{u} B \xar{v} C$.
We choose, in this order, commutative semi-free resolutions 
$r_{\mrm{un}} / \mrm{id} : \til{A}_{\mrm{un}} / \Z \to A / \Z$, 
$s_{\mrm{un}} / r_{\mrm{un}} : \til{B}_{\mrm{un}} / \til{A}_{\mrm{un}} \to B / 
\til{A}_{\mrm{un}}$
and
$t_{\mrm{un}} / s_{\mrm{un}} : \til{C}_{\mrm{un}} / \til{B}_{\mrm{un}} \to C / 
\til{B}_{\mrm{un}}$.
In this way we obtain a K-flat resolving triple 
$\til{A}_{\mrm{un}} \xar{\til{u}_{\mrm{un}}} \til{B}_{\mrm{un}} 
\xar{\til{v}_{\mrm{un}}} \til{C}_{\mrm{un}}$
of $A \xar{u} B \xar{v} C$.
Now we define 
\[ \opn{Sq}_{v / \mrm{id}_A}(\th) := 
(\opn{sq}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}})^{-1} \circ 
\opn{Sq}_{v / \mrm{id}_A}^{\til{v}_{\mrm{un}} / 
\mrm{id}_{\til{A}_{\mrm{un}}}}(\th)
\circ \opn{sq}^{\til{C}_{\mrm{un}} / \til{A}_{\mrm{un}}} . \]

Let us verify condition ($**$). We are given an arbitrary commutative K-flat 
resolution 
$\til{A} \xar{\til{u}} \til{B} \xar{\til{v}} \til{C}$
of the triple $A \to B \xar{v} C$.
According to Theorem \ref{thm:306} we can find homomorphisms 
$\til{r} : \til{A}_{\mrm{un}} \to \til{A}$,
$\til{s} : \til{B}_{\mrm{un}} \to \til{B}$ and
$\til{t} : \til{C}_{\mrm{un}} \to \til{C}$, 
such that the diagram below in $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$
is commutative.  

\begin{equation} \label{eqn:1000}
\UseTips \xymatrix @C=10ex @R=6ex {
\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}
\ar[r]^{ \til{v}_{\mrm{un}} / \mrm{id} }
\ar[d]^{ \til{s} / \til{r} }
\ar @/_3em/ [dd]_(0.7){ s_{\mrm{un}} / r_{\mrm{un}} }
&
\til{C}_{\mrm{un}} / \til{A}_{\mrm{un}}
\ar[d]_{ \til{t} / \til{r} }
\ar @/^3em/ [dd]^(0.7){ t_{\mrm{un}} / r_{\mrm{un}} }
\\
\til{B} / \til{A}
\ar[r]^{ \til{v} / \mrm{id} }
\ar[d]^{ s / r }
&
\til{C} / \til{A}
\ar[d]_{ t / r }
\\
B / A
\ar[r]^{ v / \mrm{id} }
&
C / A
} 
\end{equation}

Now let us look at the corresponding diagram with the squaring operation. It is 
a diagram in $\cat{D}(B)$. 

\[ \UseTips \xymatrix @C=16ex @R=8ex {
\opn{Sq}_{B / A}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}}(M)
&
\opn{Sq}_{C / A}^{\til{C}_{\mrm{un}} / \til{A}_{\mrm{un}}}(N)
\ar[l]_(0.5){ \opn{Sq}_{v / \mrm{id}}^{\til{v}_{\mrm{un}} / \mrm{id}}(\th) }
\\
\opn{Sq}_{B / A}^{\til{B} / \til{A}}(M)
\ar[u]_{ \opn{Sq}_{\mrm{id} / \mrm{id}}^{\til{s} / \til{r}}(\mrm{id}) }
&
\opn{Sq}_{C / A}^{\til{C} / \til{A}}(N)
\ar[u]^{ \opn{Sq}_{\mrm{id} / \mrm{id}}^{\til{t} / \til{r}}(\mrm{id}) }
\ar[l]_(0.5){ \opn{Sq}_{v / \mrm{id}}^{\til{v} / \mrm{id}}(\th) }
\\
\opn{Sq}_{B / A}(M)
\ar @/^4em/ [uu]^(0.3){ \opn{sq}^{\til{B}_{\mrm{un}} / \til{A}_{\mrm{un}}} }
\ar[u]_{ \opn{sq}^{\til{B} / \til{A}} }
&
\opn{Sq}_{C / A}(N)
\ar[u]^{ \opn{sq}^{\til{C} / \til{A}} }
\ar[l]_{ \opn{Sq}_{v / \mrm{id}}(\th) }
\ar @/_3em/ [uu]_(0.3){ \opn{sq}^{\til{C}_{\mrm{un}} / \til{A}_{\mrm{un}}} }
} \]

The top square is commutative by Proposition \ref{prop:940} (applied twice). 
The two half-moons are commutative by condition ($*$) of Theorem \ref{thm:860}.
The outer paths are equal by definition of 
$\opn{Sq}_{v / \mrm{id}}(\th)$. Because the vertical arrows are isomorphisms, 
we conclude that the bottom square is commutative. This is what we had to 
prove. 
\end{proof}

\begin{cor} \label{cor:970}
Let $B / A$ be a pair of commutative DG rings.
The assignments 
\[ M \mapsto \opn{Sq}_{B / A}(M) \quad \tup{and} \quad 
\th \mapsto \opn{Sq}_{\mrm{id}_B / \mrm{id}_A}(\th) \]
are a functor 
\[ \opn{Sq}_{B / A} : \cat{D}(B) \to  \cat{D}(B) . \]
\end{cor}

\begin{proof}
Consider morphisms 
$M_0 \xar{\th_1} M_1 \xar{\th_2} M_2$
in $\cat{D}(B)$. A combination of Proposition \ref{prop:940} and condition 
($**$) of Theorem \ref{thm:871} shows that 
\[ \opn{Sq}_{\mrm{id} / \mrm{id}}(\th_2) \circ 
\opn{Sq}_{\mrm{id} / \mrm{id}}(\th_1) = 
\opn{Sq}_{\mrm{id} / \mrm{id}}(\th_2 \circ \th_1) . \]
And by Lemma \ref{lem:925}, 
$\opn{Sq}_{\mrm{id} / \mrm{id}}(\mrm{id}_M) = 
\mrm{id}_{\opn{Sq}_{B / A}(M)}$.
\end{proof}

\begin{dfn} \label{dfn:1001}
The object $\opn{Sq}_{B / A}(M)$ from Theorem \ref{thm:860}  is called the 
{\em square of $M$ over $B$ relative to $A$}. 
The functor $\opn{Sq}_{B / A}$ from Corollary \ref{cor:970}
is called the {\em squaring operation  over $B$ relative to $A$}. 
\end{dfn}

The following result says that the squaring operation $\opn{Sq}_{B / A}$ is 
also functorial in the DG ring $B$. 

\begin{prop} \label{prop:1000}
We are given homomorphisms of commutative DG rings 
$A \to B_2 \xar{v_2} B_1 \xar{v_1} B_0$,
DG modules $M_k \in \cat{D}(B_k)$,
and morphisms 
$\th_k : M_{k - 1} \to  M_k$ in $\cat{D}(B_k)$.
Then 
\[ \opn{Sq}_{v_2 / \mrm{id}_A}(\th_2) \circ 
\opn{Sq}_{v_1 / \mrm{id}_A}(\th_1) = 
\opn{Sq}_{(v_1 \circ v_2) / \mrm{id}_A}(\th_2 \circ \th_1) , \]
as morphisms 
$\opn{Sq}_{B_0 / A}(M_0) \to \opn{Sq}_{B_2 / A}(M_2)$ in $\cat{D}(B_2)$.  
\end{prop}

\begin{proof}
Choose a K-flat resolution 
$\til{A} \xar{} \til{B}_2 \xar{\til{v}_2} \til{B}_1 \xar{\til{v}_1} \til{B}_0$
of 
$A \to B_2 \xar{v_2} B_1 \xar{v_1} B_0$, 
in the obvious sense that generalizes 
Definition \ref{dfn:1000}. According to condition ($**$) of Theorem 
\ref{thm:871}, it suffices to prove that 
\[ \opn{Sq}_{v_2 / \mrm{id}}^{\til{v}_2 / \mrm{id}} (\th_2) \circ 
\opn{Sq}_{v_1 / \mrm{id}}^{\til{v}_1 / \mrm{id}}(\th_1) = 
\opn{Sq}_{(v_1 \circ v_2) / \mrm{id}}^{(\til{v}_1 \circ \til{v}_2) / \mrm{id}}
(\th_2 \circ \th_1) , \]
as morphisms 
$\opn{Sq}_{B_0 / A}^{\til{B}_0 / \til{A}}(M_0) \to 
\opn{Sq}_{B_2 / A}^{\til{B}_2 / \til{A}}(M_2)$ 
in $\cat{D}(B_2)$. This is true by Proposition \ref{prop:940}.
\end{proof}


\begin{prop} \label{prop:1015}
Let $A$ be a commutative DG ring.
The action from Proposition \tup{\ref{prop:461}(1)}
makes $\cat{D}(A)$ into an $\opn{H}^0(A)$-linear category. 
\end{prop}

\begin{proof}
Because $A^0$ is in the center of $A$, and $\d(A^0) = 0$, we see that 
$\cat{M}(A)$ is an $A^0$-linear category. See formula (\ref{eqn:1015}). 
Next, from formula 
(\ref{eqn:1016}) we see that $\cat{K}(A)$ is an 
$\opn{H}^0(A)$-linear category. Hence its localization $\cat{D}(A)$ is an
$\opn{H}^0(A)$-linear category.
\end{proof}

Given a homomorphism $B \to C$ of commutative DG rings, and objects 
$M \in \cat{D}(B)$ and $N \in \cat{D}(C)$, the set 
$\opn{Hom}_{\cat{D}(B)}(N, M)$
is an $\opn{H}^0(C)$-module, with action coming the action of 
$\opn{H}^0(C)$ on $N$ as an object of $\cat{D}(C)$, as in the proposition 
above. 

We end the paper with the next result.

\begin{thm} \label{thm:1010}
In the situation of Theorem \tup{\ref{thm:871}}, let $c \in \opn{H}^0(C)$. 
Then 
\[ \opn{Sq}_{v / \mrm{id}}(c \cd \th) =
c^2 \cd \opn{Sq}_{v / \mrm{id}}(\th) , \]
as morphisms 
\[ \opn{Sq}_{C / A} (N)  \to \opn{Sq}_{B / A} (M) \]
in $\cat{D}(B)$.
\end{thm}

\begin{proof}
Choose a K-flat resolution
$\til{B} / \til{A}$ of $B / A$. Then choose a strict commutative semi-free 
resolution $\til{C} / \til{B}$ of $C / \til{B}$. 
Putting them together we obtain a K-flat resolution 
$\til{A} \xar{} \til{B} \xar{\til{v}} \til{C}$
of $A \to B \xar{v} C$, where $\til{v}$ is commutative semi-free. 
Let $\bsym{P}_M = (\til{P}_M, \til{I}_M; \al_M, \be_M)$
be a symmetric compound resolution of $M$ over $\til{B} / \til{A}$, 
and let  
$\bsym{P}_N = (\til{P}_N, \til{I}_N; \al_N, \be_N)$
be a symmetric compound resolution of $N$ over $\til{C} / \til{A}$.
See Remark \ref{rem:965} and Definition \ref{dfn:919}.

Because $\til{P}_N$ is K-projective over $\til{B}$,
we can find a homomorphism 
$\til{\th} : \til{P}_N \to \til{P}_M$
in $\cat{M}(\til{B})$ that lifts $\th$. 
We obtain a symmetric compound morphism
$\bsym{\eta} : \bsym{P}_N \to \bsym{P}_M$, 
$\bsym{\eta} := (\til{P}_N; \mrm{id}_{\til{P}_N}, \til{\th}, \eta)$
above $\th$ and  $\til{v} / \mrm{id}_{\til{A}}$.
Specifically, the homomorphism 
$\eta : \til{I}_N \to \til{I}_M$
in $\cat{M}(\til{B}^{\mrm{en}})$ is a lift of 
\[ \til{\th} \ot \til{\th} : \til{P}_N \ot_{\til{A}} \til{P}_N \to 
\til{P}_M \ot_{\til{A}} \til{P}_M . \]
By Proposition \ref{prop:916},  
$\opn{Sq}_{v / \mrm{id}}(\th)$
is represented by 
\[ \opn{Hom}_{v^{\mrm{en}}}(v, \eta) : 
\opn{Hom}_{C^{\mrm{en}}}(C, \til{I}_N) \to 
\opn{Hom}_{B^{\mrm{en}}}(B, \til{I}_M) . \]
We remind that 
$\til{B}^{\mrm{en}} = \til{B} \ot_{\til{A}} \til{B}^{\mrm{op}}$
and
$\til{C}^{\mrm{en}} = \til{C} \ot_{\til{A}} \til{C}^{\mrm{op}}$.

Now choose some $\til{c} \in \til{C}^0$ that represents the cohomology class 
$c \in \opn{H}^0(C) \cong \opn{H}^0(\til{C})$. 
Then 
$\til{c} \cd \til{\th} : \til{P}_N \to \til{P}_M$ 
lifts $c \cd \th : N \to M$, and 
$(\til{c} \ot \til{c}) \cd \eta : \til{I}_N \to \til{I}_M$
lifts 
$(\til{c} \cd \til{\th}) \ot (\til{c} \cd \til{\th})$. 
We get a symmetric compound morphism 
$\bsym{\eta}_c : \bsym{P}_N \to \bsym{P}_M$, 
\[ \bsym{\eta}_c := \bigl( \til{P}_N; \mrm{id}_{\til{P}_N} , \til{c} \cd 
\til{\th}, (\til{c} \ot \til{c}) \cd \eta \bigr)  \]
resolving $c \cd \th$. But then the homomorphism 
\[ \opn{Hom}_{v^{\mrm{en}}}(v, (\til{c} \ot \til{c}) \cd \eta) = 
\opn{Hom}_{v^{\mrm{en}}}( \til{c}^2 \cd v, \eta) = 
\til{c}^2 \cd \opn{Hom}_{v^{\mrm{en}}}(v, \eta)  \]
represents 
$\opn{Sq}_{v / \mrm{id}}(c \cd \th)$.
\end{proof}

This theorem shows that the functor $\opn{Sq}_{B / A}$ is a 
{\em quadratic functor}.
