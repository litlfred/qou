---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-005-5-pairs-of-dg-modules-compound-resolutions-and-r
section_title: "Pairs of DG Modules, Compound Resolutions, and Rectangles"
section_number: 5
pages: 26-32
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.961
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
---
\label{sec:pairs-DG-modules}

Recall that $\cat{PDGR}$ is the category of central pairs DG rings.
See Definition \ref{dfn:910}. 
Resolutions in $\cat{PDGR}$ were defined in Definition \ref{dfn:912} and 
\ref{dfn:52}. The category of central DG $A$-rings  
$\cat{DGR} \centover A$
was defined in Definition \ref{dfn:750}(4). 

\begin{dfn} \label{dfn:914}
Let $\til{B} / \til{A}$ be an object of $\cat{PDGR}$. 
The {\em enveloping DG ring} of $\til{B}$ over $\til{A}$ is the DG ring 
\[ \til{B}^{\mrm{en}} := 
\til{B}^{} \ot_{\til{A}^{}} \til{B}^{\mrm{op}}
\in \cat{DGR} \centover \til{A} . \]

Let 
$\til{w} / \til{v} : \til{B}_1 / \til{A}_1 \to \til{B}_0 / \til{A}_0$
be a morphism in $\cat{PDGR}$. There is an induced DG ring homomorphism 
\[ \til{w}^{\mrm{en}} := \til{w} \ot_{\til{v}} \til{w}^{\mrm{op}} : 
\til{B}^{\mrm{en}}_1 \to \til{B}^{\mrm{en}}_0  \]
in $\cat{DGR} \centover \til{A}_1$. 
\end{dfn}

In this way we obtain a functor 
$\cat{PDGR} \to \cat{DGR}$.

\begin{lem} \label{lem:911}
Let $w / v : B_1 / A_1 \to B_0 / A_0$ be a quasi-isomorphism in $\cat{PDGR}$,
and let 
$\til{w} / \til{v} : \til{B}_1 / \til{A}_1 \to \til{B}_0 / \til{A}_0$
be a K-flat resolution of $w / v$. Then 
$\til{w}^{\mrm{en}} : \til{B}^{\mrm{en}}_1 \to \til{B}^{\mrm{en}}_0$
is a quasi-isomorphism.
\end{lem}

\begin{proof}
The homomorphisms 
$\til{v} : \til{A}_1 \to \til{A}_0$
and 
$\til{w} : \til{B}_1 \to \til{B}_0$
are also quasi-iso\-morphisms. 
We can forget the DG rings structures of $\til{B}_0$ and $\til{B}_1$, and just 
view them as K-flat DG modules over $\til{A}_0$ and $\til{A}_1$ respectively. 
Then Proposition \ref{prop:462}(1) applies. 
\end{proof}
 
\begin{dfn} \label{dfn:915}
Let $\til{B} / \til{A}$ be an object of $\cat{PDGR}$, and let 
$(\til{M}^{\mrm{l}}, \til{M}^{\mrm{r}})$
be an object of 
$\cat{M}(\til{B}) \times \cat{M}(\til{B}^{\mrm{op}})$;
namely $\til{M}^{\mrm{l}}$ is a left DG $\til{B}$-module, and 
$\til{M}^{\mrm{r}}$ is a right DG $\til{B}$-module.
We define the DG module
\[ \til{M}^{\mrm{en}} := \til{M}^{\mrm{l}} \ot_{\til{A}} 
\til{M}^{\mrm{r}} \in \cat{M}(\til{B}^{\mrm{en}}) . \]

Let 
$\til{w} / \til{v} : \til{B}_1 / \til{A}_1 \to \til{B}_0 / \til{A}_0$
be a morphism in $\cat{PDGR}$, let 
\[ (\til{M}^{\mrm{l}}_k, \til{M}^{\mrm{r}}_k) \in 
\cat{M}(\til{B}_k) \times \cat{M}(\til{B}^{\mrm{op}}_k) \]
for $k = 0, 1$, and let 
\[ (\til{\th}^{\mrm{l}}, \til{\th}^{\mrm{r}}) : 
(\til{M}^{\mrm{l}}_0, \til{M}^{\mrm{r}}_0) \to
(\til{M}^{\mrm{l}}_1, \til{M}^{\mrm{r}}_1) \]
be a morphism in 
$\cat{M}(\til{B}_1) \times \cat{M}(\til{B}^{\mrm{op}}_1)$.
We define the morphism 
\[ \til{\th}^{\mrm{en}} := 
\til{\th}^{\mrm{l}} \ot_{\til{v}} \til{\th}^{\mrm{r}} : 
\til{M}^{\mrm{en}}_0 \to \til{M}^{\mrm{en}}_1  \]
in $\cat{M}(\til{B}^{\mrm{en}}_1)$.
\end{dfn}

\begin{rem}
We have omitted reference to the forgetful functors in the definition 
above. Thus, the homomorphism 
$\til{\th}^{\mrm{l}}$ in $\cat{M}(\til{B}_1)$ 
is actually a homomorphism 
$\til{\th}^{\mrm{l}} : \opn{For}_{w}(\til{M}^{\mrm{l}}_0) \to M^{\mrm{l}}_1$;
and the homomorphism 
$\til{\th}^{\mrm{r}}$ in $\cat{M}(\til{B}^{\mrm{op}}_1)$ 
is actually a homomorphism 
$\til{\th}^{\mrm{r}} : \opn{For}_{w^{\mrm{op}}}(\til{M}^{\mrm{r}}_0) \to 
M^{\mrm{r}}_1$.

We shall continue with these omissions, for the sake of clarity. 
The forgetful functors will only be made explicit when there is more than one 
given homomorphism between two DG rings. We hope this shortcut will not be a 
cause for confusion. 
\end{rem}

\begin{dfn} \label{dfn:917}
Let $B/ A$ be an object of $\cat{PDGR}$, let 
$(M^{\mrm{l}}, M^{\mrm{r}})$ be an object of 
$\cat{D}(B) \times \cat{D}(B^{\mrm{op}})$, 
and let $\til{B} / \til{A}$ be a K-flat resolution of $B / A$. 
A {\em compound resolution of $(M^{\mrm{l}}, M^{\mrm{r}})$ over 
$\til{B} / \til{A}$} is the following data:
\begin{itemize}
\item A K-flat resolution 
$\al^{\mrm{l}} : \til{P}^{\mrm{l}} \to M^{\mrm{l}}$
in $\cat{M}(\til{B})$. 

\item A K-flat resolution 
$\al^{\mrm{r}} : \til{P}^{\mrm{r}} \to M^{\mrm{r}}$
in $\cat{M}(\til{B}^{\mrm{op}})$. 

\item A K-injective resolution 
$\be : \til{P}^{\mrm{en}} \to \til{I}$
in $\cat{M}(\til{B}^{\mrm{en}})$.
\end{itemize}
We denote this compound resolution by 
\[ \bsym{P} := (\til{P}^{\mrm{l}}, \til{P}^{\mrm{r}}, \til{I}; 
\al^{\mrm{l}}, \al^{\mrm{r}}, \be ) . \]
\end{dfn}

It is easy to see that compound resolutions exist. 

Consider a K-flat resolution
$s / r : \til{B} / \til{A} \to B / A$ in $\cat{PDGR}$.
The left and right actions of $\til{B}$ on $B$ commute with each other, and 
they commute with the action of $B^{\mrm{ce}}$ on $B$ (all in the graded 
sense). Thus $B$ is a DG module over
$\til{B}^{\mrm{en}} \ot_{\til{A}} B^{\mrm{ce}}$. Hence we can make the next 
definition, in the spirit of Proposition \ref{prop:461}. 

\begin{dfn} \label{dfn:918}
In the situation of Definition \ref{dfn:917}, we define the DG module
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(\bsym{P}) :=
\opn{Hom}_{B^{\mrm{en}}}(B, \til{I}) \in \cat{M}(B^{\mrm{ce}}) . \]
\end{dfn}

The next setup shall be used in the rest of this section. 

\begin{setup} \label{set:940}
For $k = 0, 1, 2$ we are given a central pair
$B_k / A_k \in \cat{PDGR}$, 
a K-flat resolution
$\til{B}_k / \til{A}_k \to B_k / A_k$ in $\cat{PDGR}$, 
and a pair of DG modules 
\[ (M^{\mrm{l}}_k, M^{\mrm{r}}_k) \in
\cat{D}(B_k) \times \cat{D}(B^{\mrm{op}}_k) . \]

For $k = 1, 2$ we are given a central morphism
\[ w_k / v_k : B_k / A_k \to B_{k - 1} / A_{k - 1}  \] 
in $\cat{PDGR}$ (i.e.\ a morphism in $\cat{PDGR}_{\vec{\mrm{ce}}}$, see 
Definition \ref{dfn:911}(3)), a morphism 
\[ (\th_{k}^{\mrm{l}},  \th_{k}^{\mrm{r}}) : 
(M_{k - 1}^{\mrm{l}},  M_{k - 1}^{\mrm{r}}) \to 
(M_{k}^{\mrm{l}},  M_{k}^{\mrm{r}}) \]
in $\cat{D}(B_k) \times \cat{D}(B_k^{\mrm{op}})$,
and a morphism 
\[ \til{w}_k / \til{v}_k : \til{B}_k / \til{A}_k \to 
\til{B}_{k - 1} / \til{A}_{k - 1} \]
above $w_k / v_k$. 

When we only consider $k = 0, 1$, the index $1$ on the morphisms 
$w_1$, $v_1$, $\th_{1}^{\mrm{l}}$, $\th_{1}^{\mrm{r}}$,  
$\til{w}_1$ and $\til{v}_1$ is redundant, and hence we will suppress it. 
\end{setup}

\begin{dfn} \label{dfn:919}
Consider Setup \ref{set:940}, with $k = 0, 1$ only. 
Let $\bsym{P}_k$ be a compound resolution of 
$(M^{\mrm{l}}_k, M^{\mrm{r}}_k)$
over $\til{B}_k / \til{A}_k$. 
A {\em compound morphism}
$\bsym{\eta} : \bsym{P}_0 \to \bsym{P}_1$
above $(\th_{}^{\mrm{l}},  \th_{}^{\mrm{r}})$
and $\til{w} / \til{v}$
is the following data:
\begin{itemize}
\item K-projective resolutions 
$\ga_{0}^{\mrm{l}} : \til{Q}_{0}^{\mrm{l}} \to \til{P}_{0}^{\mrm{l}}$
and 
$\ga_{0}^{\mrm{r}} : \til{Q}_{0}^{\mrm{r}} \to \til{P}_{0}^{\mrm{r}}$
in $\cat{M}(\til{B}_1)$ and $\cat{M}(\til{B}_1^{\mrm{op}})$
respectively. 

\item  Homomorphisms 
$\til{\th}^{\mrm{l}} : \til{Q}_{0}^{\mrm{l}} \to \til{P}_1^{\mrm{l}}$
and 
$\til{\th}^{\mrm{r}} : \til{Q}_{0}^{\mrm{r}} \to \til{P}_1^{\mrm{r}}$
in $\cat{M}(\til{B}_1)$ and
$\cat{M}(\til{B}_1^{\mrm{op}})$ respectively,
such that 
\[ \th_{}^{\mrm{l}} \circ \opn{Q}(\al_{0}^{\mrm{l}})
\circ \opn{Q}(\ga_{0}^{\mrm{l}}) =
\opn{Q}(\al_{1}^{\mrm{l}}) \circ \opn{Q}(\til{\th}_{}^{\mrm{l}}) \]
and
\[ \th_{}^{\mrm{r}} \circ \opn{Q}(\al_{0}^{\mrm{r}})
\circ \opn{Q}(\ga_{0}^{\mrm{r}}) =
\opn{Q}(\al_{1}^{\mrm{r}}) \circ \opn{Q}(\til{\th}_{}^{\mrm{r}}) \]
in $\cat{D}(\til{B}_1)$ and $\cat{D}(\til{B}_1^{\mrm{op}})$ respectively.

\item A homomorphism $\eta : \til{I}_{0} \to \til{I}_1$
in $\cat{M}(\til{B}_1^{\mrm{en}})$, such that 
\[ \opn{Q}(\eta) \circ \opn{Q}(\be_{0}) 
\circ \opn{Q}( \ga_{0}^{\mrm{l}} \ot_{\til{v}} \ga_{0}^{\mrm{r}} ) = 
\opn{Q}(\be_{1}) \circ \opn{Q}(\til{\th}_{}^{\mrm{en}}) , \]
as morphisms 
$\til{Q}_{0}^{\mrm{l}} \ot_{\til{A}_1} \til{Q}_{0}^{\mrm{r}}
\to \til{I}_1$
in $\cat{D}(\til{B}_1^{\mrm{en}})$.
\end{itemize}
We denote this compound morphism by 
\[ \bsym{\eta} = (\til{Q}_{0}^{\mrm{l}}, \til{Q}_{0}^{\mrm{r}};
\ga_{0}^{\mrm{l}}, \ga_{0}^{\mrm{r}},
\til{\th}^{\mrm{l}}, \til{\th}^{\mrm{r}}, \eta ) . \]
We also say that $\bsym{\eta}$ is a {\em compound resolution of 
$(\th_{}^{\mrm{l}},  \th_{}^{\mrm{r}})$}.
\end{dfn}

This definition is illustrated in the next diagrams, that are commutative
diagrams in the categories $\cat{D}(\til{B}_1)$,
$\cat{D}(\til{B}_1^{\mrm{op}})$
and $\cat{D}(\til{B}_1^{\mrm{en}})$ respectively.
The vertical arrows in these diagrams (namely those whose names do not contain 
the letters ``$\th$'' or ``$\eta$'') are isomorphisms. 
(Note that the letter $\opn{Q}$ denotes the localization functor, 
not to be confused with the DG modules $\til{Q}_0^{\mrm{l}}$ etc.)

\[ \UseTips \xymatrix @C=7ex @R=6ex {
\til{Q}_0^{\mrm{l}}
\ar[d]_{ \opn{Q}(\ga_0^{\mrm{l}}) }
\ar[dr]^{ \opn{Q}(\til{\th}^{\mrm{l}}) }
\\
\til{P}_0^{\mrm{l}}
\ar[d]_{ \opn{Q}(\al_0^{\mrm{l}}) }
&
\til{P}_1^{\mrm{l}}
\ar[d]_{ \opn{Q}(\al_1^{\mrm{l}}) }
\\
M_0^{\mrm{l}}
\ar[r]_{ \th^{\mrm{l}} }
&
M_1^{\mrm{r}}
} 
\qquad 

\xymatrix @C=6ex @R=7ex {
\til{Q}_0^{\mrm{r}}
\ar[d]_{ \opn{Q}(\ga_0^{\mrm{r}}) }
\ar[dr]^{ \opn{Q}(\til{\th}^{\mrm{r}}) }
\\
\til{P}_0^{\mrm{r}}
\ar[d]_{ \opn{Q}(\al_0^{\mrm{r}}) }
&
\til{P}_1^{\mrm{r}}
\ar[d]_{ \opn{Q}(\al_1^{\mrm{r}}) }
\\
M_0^{\mrm{r}}
\ar[r]_{ \th^{\mrm{r}} }
&
M_1^{\mrm{r}}
} 

\qquad 
\UseTips \xymatrix @C=6ex @R=6ex {

\til{Q}_{0}^{\mrm{l}} \ot_{\til{A}_1} \til{Q}_{0}^{\mrm{r}}
\ar[d]_{ \opn{Q}(\ga_{0}^{\mrm{l}} \ot_{\til{v}} \ga_{0}^{\mrm{r}}) }
\ar[dr]^{ \opn{Q}(\til{\th}^{\mrm{en}}) }
\\
\til{P}_0^{\mrm{en}}
\ar[d]_{ \opn{Q}(\be_0) }
&
\til{P}_1^{\mrm{en}}
\ar[d]_{ \opn{Q}(\be_1) }
\\
\til{I}_0^{}
\ar[r]_{ \opn{Q}(\eta) }
&
\til{I}_1^{}
} 
\]

There is no composition rule for the compound morphisms $\bsym{\eta}$; 
but this is taken care of by the following lemmas. 

\begin{lem} \label{lem:915}
In the situation of Definition \tup{\ref{dfn:919}}, compound
resolutions $\bsym{\eta}$ of the morphism 
$(\th_{}^{\mrm{l}},  \th_{}^{\mrm{r}})$ exist.
\end{lem}

\begin{proof}
The homomorphisms $\til{\th}^{\mrm{l}}$ and $\til{\th}^{\mrm{r}}$ exist because 
$\til{Q}_0^{\mrm{l}}$ and $\til{Q}_0^{\mrm{r}}$ are K-projective in the 
respective categories. The homomorphism $\eta$ exists because 
$\til{I}_1$ is K-injective. See Proposition \ref{prop:460}. 
\end{proof}

In the next definition, it is crucial that the homomorphism 
$w : B_1 \to B_0$ is central; this is guaranteed by Setup \ref{set:940}, in 
which we demand that $w / v$ is a morphism in $\cat{PDGR}_{\vec{\mrm{ce}}}$.
Since $w$ is central, we get an induced DG ring homomorphism 
$w^{\mrm{ce}} : B^{\mrm{ce}}_1 \to B^{\mrm{ce}}_0$. 
So Proposition \ref{prop:461}(2) applies.

\begin{dfn} \label{dfn:920}
In the situation of Definition \tup{\ref{dfn:919}}, we let 
\[ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}) : 
\opn{Rect}_{B_0 / A_0}^{\til{B}_{0} / \til{A}_{0}}(\bsym{P}_{0}) \to
\opn{Rect}_{B_1 / A_1}^{\til{B}_{1} / \til{A}_{1}}(\bsym{P}_{1}) \]
be the morphism 
\[ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta})  :=
\opn{Q} \bigl( \opn{Hom}_{w^{\mrm{en}}}(w, \eta) \bigr) \]
in $\cat{D}(B_1^{\mrm{ce}})$.  
\end{dfn}

\begin{lem} \label{lem:916}
The morphism 
$\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta})$
is independent of the compound resolution $\bsym{\eta}$. Namely, if 
$\bsym{\eta}'$ is another compound resolution of 
$(\th^{\mrm{l}},  \th^{\mrm{r}})$, 
then there is equality
\[ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}) = 
\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}') \]
of morphisms 
\[ \opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_{0}}(\bsym{P}_{0}) \to
\opn{Rect}_{B_1 / A_1}^{\til{B}_{1} / \til{A}_{1}}(\bsym{P}_{1}) \]
in $\cat{D}(B_1^{\mrm{ce}})$.
\end{lem}

\begin{proof}
Say 
\[ \bsym{\eta}' = (\til{Q}_{0}'^{\, \mrm{l}}, \til{Q}_{0}'^{\, \mrm{r}};
\ga_{0}'^{\, \mrm{l}}, \ga_{0}'^{\, \mrm{r}},
\til{\th}'^{\, \mrm{l}}, \til{\th}'^{\, \mrm{r}}, \eta' ) . \]
The DG modules $\til{Q}_{0}'^{\, \mrm{l}}$ and $\til{Q}_{0}^{\mrm{l}}$
are homotopy equivalent in $\cat{M}(\til{B}_1)$, 
and under this equivalence the homomorphisms 
$\til{\th}'^{\, \mrm{l}} : \til{Q}_{0}'^{\, \mrm{l}} \to
\til{P}_{1}^{\mrm{l}}$
and 
$\til{\th}^{\mrm{l}} : \til{Q}_{0}^{\mrm{l}} \to \til{P}_{1}^{\mrm{l}}$
are homotopic. Likewise for ``r''. Therefore the DG modules 
$\til{Q}_{0}'^{\, \mrm{en}}$ and $\til{Q}_{0}^{\mrm{en}}$
are homotopy equivalent in $\cat{M}(\til{B}_1^{\mrm{en}})$, 
and under this equivalence the homomorphisms 
$\til{\th}'^{\, \mrm{en}} : \til{Q}_{0}'^{\, \mrm{en}} \to
\til{P}_{1}^{\mrm{en}}$
and 
$\til{\th}^{\mrm{en}} : \til{Q}_{0}^{\mrm{en}} \to \til{P}_{1}^{\mrm{en}}$
are homotopic.
This implies that the homomorphisms $\eta'$ and $\eta$ are homotopic.
\end{proof}

\begin{lem} \label{lem:925}
Assume that $B_1 / A_1 = B_0 / A_0$, 
$\til{B}_1 / \til{A}_1 = \til{B}_0 / \til{A}_0$,
$(M^{\mrm{l}}_1, M^{\mrm{r}}_1) = (M^{\mrm{l}}_0, M^{\mrm{r}}_0)$, 
and all the morphisms between them are the identities. 
Also assume that $\bsym{P}_1 = \bsym{P}_0$. Then for any compound morphism
$\bsym{\eta} : \bsym{P}_{0} \to \bsym{P}_{0}$
above 
$(\opn{id}_{M^{\mrm{l}}_0}, \opn{id}_{M^{\mrm{r}}_0})$,
the morphism 
$\opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta})$
is the identity automorphism of
$\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_{0}}(\bsym{P}_{0})$.
\end{lem}

\begin{proof}
Clear. 
\end{proof}

\begin{lem} \label{lem:919}
Consider Setup \tup{\ref{set:940}}, with $k = 0, 1, 2$. 
We are given a compound resolution
$\bsym{P}_k$ of $(M^{\mrm{l}}_k, M^{\mrm{r}}_k)$
over $\til{B} / \til{A}$. 
For $k = 1, 2$ we are given a compound morphism  
$\bsym{\eta}_k : \bsym{P}_{k - 1} \to \bsym{P}_{k}$
above $(\th_{k}^{\mrm{l}},  \th_{k}^{\mrm{r}})$ 
and $\til{w}_k / \til{v}_k$.
Also, we are given a compound morphism 
$\bsym{\eta}_{0, 2} : \bsym{P}_{0} \to \bsym{P}_{2}$
above 
$(\th_{2}^{\mrm{l}}, \th_{2}^{\mrm{r}}) \circ 
(\th_{1}^{\mrm{l}}, \th_{1}^{\mrm{r}})$
and 
$(\til{w}_1 / \til{v}_1) \circ  (\til{w}_2 / \til{v}_2)$.
Then there is equality
\[ \opn{Rect}_{(w_1 / v_1) \circ (w_2 / v_2)}
^{(\til{w}_1 / \til{v}_1) \circ (\til{w}_2 / \til{v}_2)}(\bsym{\eta}_{0, 2}) 
= \opn{Rect}_{w_2 / v_2}^{\til{w}_2 / \til{v}_2}(\bsym{\eta}_2) 
\circ 
\opn{Rect}_{w_1 / v_1}^{\til{w}_1 / \til{v}_1}(\bsym{\eta}_1) \]
of morphisms 
\[ \opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_{0}}(\bsym{P}_{0}) \to
\opn{Rect}_{B_2 / A_2}^{\til{B}_{2} / \til{A}_{2}}(\bsym{P}_{2})  \]
in $\cat{D}(B_2^{\mrm{ce}})$.
\end{lem}

\begin{proof}
By choosing homomorphisms 
$\til{Q}_{0}^{\mrm{l}} \to \til{Q}_{1}^{\mrm{l}}$
and 
$\til{Q}_{0}^{\mrm{r}} \to \til{Q}_{1}^{\mrm{r}}$
that lift $\th_1^{\mrm{l}}$ and $\th_1^{\mrm{r}}$
respectively, we can concoct a ``composed'' morphism 
$\bsym{\eta}_2 \circ \bsym{\eta}_1$,
well-defined up to homotopy, whose component 
$\til{I}_0 \to \til{I}_2$ is  $\eta_2 \circ \eta_1$. 
Thus 
\[ \opn{Rect}_{(w_1 / v_1) \circ (w_2 / v_2)}
^{(\til{w}_1 / \til{v}_1) \circ (\til{w}_2 / \til{v}_2)}
(\bsym{\eta}_2 \circ \bsym{\eta}_1) = 
\opn{Rect}_{w_2 / v_2}^{\til{w}_2 / \til{v}_2}(\bsym{\eta}_2) 
\circ 
\opn{Rect}_{w_1 / v_1}^{\til{w}_1 / \til{v}_1}(\bsym{\eta}_1) . \]
On the other hand, by Lemma \ref{lem:916} we know that 
\[ \opn{Rect}_{(w_1 / v_1) \circ (w_2 / v_2)}
^{(\til{w}_1 / \til{v}_1) \circ (\til{w}_2 / \til{v}_2)}
(\bsym{\eta}_2 \circ \bsym{\eta}_1) = 
\opn{Rect}_{(w_1 / v_1) \circ (w_2 / v_2)}
^{(\til{w}_1 / \til{v}_1) \circ (\til{w}_2 / \til{v}_2)}
(\bsym{\eta}_{0, 2}) . \] 
\end{proof}

\begin{lem} \label{lem:917}
If 
$w / v : B_1 / A_1 \to B_0 / A_0$ is a quasi-isomorphism in $\cat{PDGR}$,
and if 
\[ (\th_{}^{\mrm{l}},  \th_{}^{\mrm{r}}) : 
(M_{0}^{\mrm{l}},  M_{0}^{\mrm{r}}) \to 
(M_{1}^{\mrm{l}},  M_{1}^{\mrm{r}}) \]
is an isomorphism in $\cat{D}(B_1) \times \cat{D}(B_1^{\mrm{op}})$,
then 
$\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta})$
is an isomorphism in $\cat{D}(B_1^{\mrm{ce}})$.
\end{lem}

\begin{proof}
Here 
$w : B_1 \to B_0$,
$\til{w}^{\mrm{en}} : B_1^{\mrm{en}} \to B_0^{\mrm{en}}$,
$\til{\th}^{\mrm{l}}$, $\til{\th}^{\mrm{r}}$,
$\til{\th}^{\mrm{en}}$ and
$\eta : \til{I}_0 \to \til{I}_1$ are quasi-iso\-morphism.
According to Proposition \ref{prop:462}(2), 
$\opn{Hom}_{w^{\mrm{en}}}(w, \eta)$
is a quasi-isomorphism.
\end{proof}

\begin{prop} \label{prop:915}
Let $B / A$ be a pair in $\cat{PDGR}$, with K-flat resolution
$\til{B} / \til{A}$. 
Let $(M^{\mrm{l}}, M^{\mrm{r}})$ be a pair in  
$\cat{D}(B) \times \cat{D}(B^{\mrm{op}})$. 
There is an object 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})
\in \cat{D}(B^{\mrm{ce}}) , \]
unique up to a unique isomorphism, together with an isomorphism 
\[ \opn{rect}(\bsym{P}) : 
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})
\iso \opn{Rect}_{B / A}^{\til{B} / \til{A}}(\bsym{P}) \]
in $\cat{D}(B^{\mrm{ce}})$ 
for every compound resolution $\bsym{P}$ of the pair 
$(M^{\mrm{l}}, M^{\mrm{r}})$ over $\til{B} / \til{A}$,
satisfying this condition\tup{:}
\begin{enumerate}
\item[($\dag$)] Let $\bsym{P}_0$ and $\bsym{P}_1$ be compound resolutions of 
the pair $(M^{\mrm{l}}, M^{\mrm{r}})$ over $\til{B} / \til{A}$,
and let 
$\bsym{\eta} : \bsym{P}_0 \to \bsym{P}_1$ 
be a compound morphism above 
$(\opn{id}_{M^{\mrm{l}}}, \opn{id}_{M^{\mrm{r}}})$

and
$\opn{id}_{\til{B}} / \opn{id}_{\til{A}}$. 
Then  the diagram 
\[ \UseTips \xymatrix @C=12ex @R=6ex {
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}})
\ar[d]_{ \opn{rect}(\bsym{P}_0) }
\ar[dr]^{ \opn{rect}(\bsym{P}_1) }
\\
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(\bsym{P}_0) 
\ar[r]_{ \opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}) }
&
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(\bsym{P}_1) 
} \]
of isomorphisms in $\cat{D}(B^{\mrm{ce}})$ is commutative. 
\end{enumerate}
\end{prop}

\begin{proof}
The uniqueness is clear. As for existence, let us fix some 
resolution $\bsym{P}$ of $(M^{\mrm{l}}, M^{\mrm{r}})$, 
and define 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}}, M^{\mrm{r}}) :=
\opn{Rect}_{B / A}^{\til{B} / \til{A}}(\bsym{P}) . \]
The isomorphism $\opn{rect}(\bsym{P})$ is the identity. 

Given any resolution $\bsym{P}_{0}$ of $(M^{\mrm{l}}, M^{\mrm{r}})$, 
let $\bsym{\eta}_0 : \bsym{P} \to \bsym{P}_0$ 
be any morphism above the identity. Define the isomorphism
\[ \opn{rect}(\bsym{P}_0) :=
\opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}_0) . \]
By Lemma \ref{lem:916} this does not depend on the choice of 
$\bsym{\eta}_0$.

To verify condition ($\dag$), let 
$\bsym{\eta}_1 : \bsym{P} \to \bsym{P}_1$
be any morphism above the identity. Then, according to Lemma \ref{lem:919},
we have
\[ \opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}_1) =
\opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}) \circ
\opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}_0) . \]
\end{proof}

\begin{prop} \label{prop:916}
In the situation of Setup \tup{\ref{set:940}}, with $k = 0, 1$ only, there is a 
unique morphism 
\[  \opn{Rect}_{w / v}^{\til{w} / \til{v}}
(\th^{\mrm{l}}, \th^{\mrm{r}}) :
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(M_0^{\mrm{l}}, M_0^{\mrm{r}}) \to
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(M_1^{\mrm{l}}, M_1^{\mrm{r}}) \]
in $\cat{D}(B_1^{\mrm{ce}})$
satisfying this condition\tup{:}
\begin{enumerate}
\item[($\dag \dag$)]
For $k = 0, 1$ let $\bsym{P}_k$ be a compound resolution of 
$(M_k^{\mrm{l}},  M_k^{\mrm{r}})$ over $\til{B}_k / \til{A}_k$, 
and let  
$\bsym{\eta} : \bsym{P}_0 \to \bsym{P}_1$ 
be a compound morphism above 
$(\th^{\mrm{l}},  \th^{\mrm{r}})$ and $\til{w} / \til{v}$. 
Then the diagram 
\[ \UseTips \xymatrix @C=16ex @R=6ex {
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(M_0^{\mrm{l}}, M_0^{\mrm{r}})
\ar[d]_{ \opn{rect}(\bsym{P}_0) }
\ar[r]^{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}
(\th^{\mrm{l}}, \th^{\mrm{r}}) }
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(M_1^{\mrm{l}}, M_1^{\mrm{r}})
\ar[d]^{ \opn{rect}(\bsym{P}_1) }
\\
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(\bsym{P}_0) 
\ar[r]^{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}) }
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(\bsym{P}_1) 
} \]
of morphisms in $\cat{D}(B_1^{\mrm{ce}})$ is commutative.
\end{enumerate} 
\end{prop}

\begin{proof}
Choose a compound resolution $\bsym{P}_k^{\mrm{bs}}$ of  
$(M_k^{\mrm{l}},  M_k^{\mrm{r}})$ over $\til{B}_k / \til{A}_k$, 
for $k = 0, 1$. Then choose a compound morphism 
$\bsym{\eta}^{\mrm{bs}} : \bsym{P}^{\mrm{bs}}_0 \to \bsym{P}^{\mrm{bs}}_1$.
(The superscript ``bs'' stands for ``basic''.)
This can be done by Lemma \ref{lem:915}. 
Let 
$\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\th^{\mrm{l}}, \th^{\mrm{r}})$
be the the unique morphism for which condition ($\dag \dag$) holds, 
with respect to these choices.

We have to prove that condition ($\dag \dag$) holds for an arbitrary choice of 
compound resolutions $\bsym{P}_k$ and a compound morphism 
$\bsym{\eta}$. Let us choose compound morphisms
$\bsym{\eta}_k :  \bsym{P}^{\mrm{bs}}_k \to \bsym{P}_k$
above $(\opn{id}_{M^{\mrm{l}}}, \opn{id}_{M^{\mrm{r}}})$
and
$\opn{id}_{\til{B}_k} / \opn{id}_{\til{A}_k}$. 
Consider the following diagram in $\cat{D}(B_1^{\mrm{ce}})$.

\[ \UseTips \xymatrix @C=16ex @R=8ex {
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(M_0^{\mrm{l}}, M_0^{\mrm{r}})
\ar[d]^{ \opn{rect}(\bsym{P}^{\mrm{bs}}_0) }
\ar[r]^{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}
(\th^{\mrm{l}}, \th^{\mrm{r}}) }
\ar @/_4.5em/ [dd]_(0.7){ \opn{rect}(\bsym{P}_0) }
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(M_1^{\mrm{l}}, M_1^{\mrm{r}})
\ar[d]_{ \opn{rect}(\bsym{P}^{\mrm{bs}}_1) }
\ar @/^4.5em/ [dd]^(0.7){ \opn{rect}(\bsym{P}_1) }
\\
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(\bsym{P}^{\mrm{bs}}_0) 
\ar[r]^{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}^{\mrm{bs}}) }
\ar[d]^{ \opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}} (\bsym{\eta}_0) 
}
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(\bsym{P}^{\mrm{bs}}_1)
\ar[d]_{ \opn{Rect}_{\mrm{id} / \mrm{id}}^{\mrm{id} / \mrm{id}}(\bsym{\eta}_1)}
\\
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(\bsym{P}_0) 
\ar[r]^{ \opn{Rect}_{w / v}^{\til{w} / \til{v}}(\bsym{\eta}) }
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(\bsym{P}_1)
} \]

\noindent 
The top square is commutative by definition. The bottom square is commutative 
by Lemmas \ref{lem:915} and \ref{lem:919}. The half-moons are commutative by 
condition ($\dag$) of Proposition \ref{prop:915}. Therefore the outer paths are 
equal; and this is what we had to prove. 
\end{proof}

\begin{prop} \label{prop:940}
In the situation of Setup \tup{\ref{set:940}}, with $k = 0, 1, 2$,
the diagram 
\[ \UseTips \xymatrix @C=18ex @R=8ex {
\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(M_0^{\mrm{l}}, M_0^{\mrm{r}})
\ar[dr]_{ \opn{Rect}_{(w_1 / v_1) \circ (w_2 / v_2)}
^{(\til{w}_1 / \til{v}_1) \circ (\til{w}_2 / \til{v}_2)}
(\th_2^{\mrm{l}} \circ \th_1^{\mrm{l}}, \th_2^{\mrm{r}}  \circ 
\th_1^{\mrm{r}}) \quad \quad \quad \quad }

\ar[r]^{ \opn{Rect}_{w_1 / v_1}^{\til{w}_1 / \til{v}_1}
(\th_1^{\mrm{l}}, \th_1^{\mrm{r}}) }
&
\opn{Rect}_{B_1 / A_1}^{\til{B}_1 / \til{A}_1}(M_1^{\mrm{l}}, M_1^{\mrm{r}})
\ar[d]^{ \opn{Rect}_{w_2 / v_2}^{\til{w}_2 / \til{v}_2}
(\th_2^{\mrm{l}}, \th_2^{\mrm{r}}) }
\\
&
\opn{Rect}_{B_2 / A_2}^{\til{B}_2 / \til{A}_2}(M_2^{\mrm{l}}, M_2^{\mrm{r}})
} \]
of morphisms in $\cat{D}(B_2^{\mrm{ce}})$ is commutative.

If $B_1 / A_1 = B_0 / A_0$, 
$\til{B}_1 / \til{A}_1 = \til{B}_0 / \til{A}_0$,
$(M^{\mrm{l}}_1, M^{\mrm{r}}_1) = (M^{\mrm{l}}_0, M^{\mrm{r}}_0)$, 
and the morphisms 
$w_1 / v_1$, 
$\til{w}_1 / \til{v}_1$ and 
$(\th_1^{\mrm{l}}, \th_1^{\mrm{r}})$
are the identity automorphisms, then 
$\opn{Rect}_{w_1 / v_1}^{\til{w}_1 / \til{v}_1}
(\th_1^{\mrm{l}}, \th_1^{\mrm{r}})$
is the identity automorphism of
$\opn{Rect}_{B_0 / A_0}^{\til{B}_0 / \til{A}_0}(M_0^{\mrm{l}}, M_0^{\mrm{r}})$. 
\end{prop}

\begin{proof}
The triangular diagram is commutative by Lemmas \ref{lem:915} and \ref{lem:919},
with condition ($\dag \dag$) of Proposition \ref{prop:916}.
The assertion about the identity automorphisms is true by Lemma \ref{lem:925}.
\end{proof}

\begin{rem} \label{rem:950}
We could have defined the rectangle object directly as 
\[ \opn{Rect}_{B / A}^{\til{B} / \til{A}}(M^{\mrm{l}},  M^{\mrm{r}}) := 
\opn{RHom}_{\til{B}^{\mrm{en}}}(B, M^{\mrm{l}} \ot_{\til{A}}^{\mrm{L}}  
M^{\mrm{r}}) \in \cat{D}(B^{\mrm{ce}}) , \]
i.e.\ as the composition of these three functors: 
\[ \opn{For}_{} \times \opn{For} :
\cat{D}(B) \times \cat{D}(B^{\mrm{op}}) \to 
\cat{D}(\til{B}) \times \cat{D}(\til{B}^{\mrm{op}}) , \]
\[ - \ot_{\til{A}}^{\mrm{L}} - : 
\cat{D}(\til{B}) \times \cat{D}(\til{B}^{\mrm{op}}) \to 
\cat{D}(\til{B}^{\mrm{en}}) \]
and 
\[ \opn{RHom}_{\til{B}^{\mrm{en}}}(B, -) : \cat{D}(\til{B}^{\mrm{en}})
\to \cat{D}(B^{\mrm{ce}}) . \]
In other words, Proposition \ref{prop:915} would have become a definition. 

However, this approach would have made it hard to make precise sense of the 
morphism 
$\opn{Rect}_{w / v}^{\til{w} / \til{v}}(\th^{\mrm{l}}, \th^{\mrm{r}})$,
and to prove the functoriality result (Proposition \ref{prop:940}).
\end{rem}
