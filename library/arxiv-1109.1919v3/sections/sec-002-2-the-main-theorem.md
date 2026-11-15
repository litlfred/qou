---
doc_id: arxiv-1109.1919v3
doc_title: "COMBINATORIAL DESCENT DATA FOR GERBES"
section_id: sec-002-2-the-main-theorem
section_title: "The Main Theorem"
section_number: 2
pages: 5-10
source_pdf: 1109.1919v3.pdf
source_sha256: 2b634edddf232047
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "COMBINATORIAL DESCENT DATA FOR GERBES — We consider descent data in cosimplicial crossed groupoids. This is a combinatorial abstraction of the descent data for gerbes in algebraic geom- etry."
---
\label{sec:equiv-cosim}

Recall that for a groupoid $G$, the set of isomorphism classes of objects
is denoted by $\bsym{\bsym{\pi}}_0(G)$.

\begin{dfn} \label{dfn:equiv-cosim.101}
Let 
$G = 
( G_1, G_2, 
\opn{Ad}_{G_1 \crvar G_{2}}, \opn{D} )$
be a crossed groupoid. 
We define the homotopy set
\[ \bsym{\bsym{\pi}}_0(G) := \bsym{\bsym{\pi}}_0(G_1) , \]
and the homotopy groups
\[ \bsym{\bsym{\pi}}_1(G, x) := 
\opn{Coker} \bigl( \opn{D} : G_2(x) \to G_1(x) \bigr) \]
and
\[ \bsym{\bsym{\pi}}_2(G, x) := 
\opn{Ker} \bigl( \opn{D} : G_2(x) \to G_1(x) \bigr) \]
for $x \in \opn{Ob}(G)$.
\end{dfn}

The set $\bsym{\bsym{\pi}}_0(G)$ and the groups $\bsym{\bsym{\pi}}_i(G, x)$ are
functorial in $G$. 
The group $\bsym{\bsym{\pi}}_2(G, x)$ is central in $G_2(x)$, 
and in particular it is abelian.

\begin{dfn} \label{dfn:equiv-cosim.102}
A morphism of crossed groupoids $\Phi : G \to H$  
is called a {\em weak equivalence} if the function
\[ \bsym{\bsym{\pi}}_0(\Phi)  : \bsym{\bsym{\pi}}_0(G) \to
\bsym{\bsym{\pi}}_0(H)  \]
is bijective, and the group homomorphisms
\[ \bsym{\bsym{\pi}}_i(\Phi, x) : \bsym{\bsym{\pi}}_i(G, x) \to
\bsym{\bsym{\pi}}_i(H, \Phi(x))  \]
are bijective for all $x \in \opn{Ob}(G)$
and $i \in \{ 1, 2 \}$.
\end{dfn}

\begin{dfn} \label{dfn:equiv-cosim.103}
A morphism $\Phi : G \to H$
of cosimplicial crossed groupoids is called a {\em weak equivalence} if in
every simplicial dimension $p$ the morphism of crossed groupoids
 $\Phi^p : G^p \to H^p$ is a weak equivalence.
\end{dfn}

\begin{thm}[Equivalence] \label{thm:100} 
Let $\Phi : G \to H$ be a weak equivalence between 
cosimplicial crossed groupoids. Then the function 
\[ \ol{\opn{Desc}}(\Phi) : \ol{\opn{Desc}}(G) \to
\ol{\opn{Desc}}(H) \]
from Definition \tup{\ref{dfn:cosim.1}} is bijective.
\end{thm}

We need a couple of auxiliary results first. 
A partial descent datum in $G$ is a pair $(x, g)$ of elements
$x \in \opn{Ob}(G^0)$ and 
$g \in G^1_1(x_{(0)}, x_{(1)})$ (cf.\ Definition \ref{dfn:101}).
Let $(x, g)$ and $(x', g')$ be partial descent data. A partial gauge
transformation $(x, g) \to (x', g')$ is a pair $(f, c)$ of elements 
as in Definition \tup{\ref{dfn:100}}, that satisfies condition \tup{(i)} of that
definition.

The next lemma is a sort of ``Kan condition'' satisfied by 
$\opn{Desc}(G)$.

\begin{lem} \label{lem:104}
Let $(x, g, a)$ be a descent datum in the cosimplicial crossed groupoid
$G$, let $(x', g')$ be a partial
descent datum in $G$, and let $(f, c)$ be a partial gauge
transformation $(x, g) \to (x', g')$.  Then there is a unique element 
$a' \in G^2_2(x'_{(0)})$ such that the triple 
$(x', g', a')$ is a descent datum in $G$, and 
$(f, c)$ is a gauge transformation
$(x, g, a) \to (x', g', a')$.
\end{lem}


\begin{proof}
Define 
\[ a' := \opn{Ad}(f_{(0)}) \Bigl( 
c_{(0, 2)}^{-1} \circ a \circ \opn{Ad}(g_{(0, 1)}^{-1})(c_{(1, 2)})
\circ c_{(0, 1)}  \Bigr) \in G^2_2(x'_{(0)}) . \]
Then $a'$ satisfies condition (ii) of Definition \ref{dfn:100}, and moreover it
is unique. 

We have to show that the triple $(x', g', a')$ is a descent
datum. Let us check condition (i) of Definition \ref{dfn:101}. We have 
\[ \begin{aligned}
& (g'_{(0, 2)})^{-1} \circ g'_{(1, 2)} \circ g'_{(0, 1)}
\\
& \qquad  \overset{\vartriangle}{=} \Bigl( f_{(2)} \circ g_{(0, 2)} \circ 
\opn{D}(c_{(0, 2)}) \circ f_{(0)}^{-1} \Bigr)^{-1} 
\circ \Bigl( f_{(2)} \circ g_{(1, 2)} \circ  \opn{D}(c_{(1, 2)}) 
\circ f_{(1)}^{-1} \Bigr)
\\
& \qquad \qquad \circ \Bigl( f_{(1)} \circ g_{(0, 1)} \circ  
\opn{D}(c_{(0, 1)}) \circ f_{(0)}^{-1} \Bigr)
\\
& \qquad \overset{\lozenge}{=} f_{(0)} \circ \opn{D}(c_{(0, 2)})^{-1}
\circ  
g_{(0, 2)}^{-1} \circ g_{(1, 2)} \circ \opn{D}(c_{(1, 2)})
\circ g_{(0, 1)} \circ \opn{D}(c_{(0, 1)}) \circ f_{(0)}^{-1}
\\
& \qquad \overset{\heartsuit}{=} \opn{Ad}(f_{(0)}) \Bigl( 
\opn{D}(c_{(0, 2)}^{-1}) \circ 
\opn{D}(a) \circ g_{(0, 1)}^{-1} \circ \opn{D}(c_{(1, 2)})
\circ g_{(0, 1)} \circ \opn{D}(c_{(0, 1)}) \Bigr) 
\\
& \qquad \overset{\star}{=} \opn{Ad}(f_{(0)}) \Bigl( 
\opn{D}(c_{(0, 2)}^{-1}) \circ 
\opn{D}(a) \circ \opn{Ad}(g_{(0, 1)}^{-1})(\opn{D}(c_{(1, 2)})) 
\circ \opn{D}(c_{(0, 1)}) \Bigr) 
\\
& \qquad \overset{\square}{=} \opn{D} \Bigl( \opn{Ad}(f_{(0)}) \Bigl( 
c_{(0, 2)}^{-1} \circ a \circ \opn{Ad}(g_{(0, 1)}^{-1})(c_{(1, 2)})
\circ c_{(0, 1)} \Bigr) \Bigr) 
\overset{\triangledown}{=} \opn{D}(a') . 
\end{aligned} \]
The equality marked $\overset{\vartriangle}{=}$ is true because of  
condition (i) of Definition \ref{dfn:100}, applied to the elements 
$g'_{(i, j)}$. The equality marked $\overset{\lozenge}{=}$ is true because of
cancellation. The equality marked $\overset{\heartsuit}{=}$ is because 
condition (i) of Definition \ref{dfn:101} holds for $(x, g, a)$, and by the
definition of $\opn{Ad}(f_{(0)})$. 
The equality marked $\overset{\star}{=}$ is by the
definition of $\opn{Ad}(g_{(0,1)}^{-1})$. 
The equality marked $\overset{\square}{=}$ is because $\opn{D}$ is 
$G^2_1$-equivariant
(this is condition (i) of Definition \ref{dfn:cosim.101}).
And the equality marked $\overset{\triangledown}{=}$ holds by definition of 
$a'$.

Finally we have to check that condition (ii) of Definition \ref{dfn:101} holds
for $(x', g', a')$. Namely, letting 
\begin{equation}
u' := 
(a'_{(0, 1, 3)})^{-1} \circ a'_{(0, 2, 3)} \circ a'_{(0, 1, 2)} \circ
\opn{Ad} \bigl( (g'_{(0, 1)})^{-1} \bigr) (a'_{(1, 2, 3)})^{-1} ,
\end{equation}
we have to show that $u' = 1$.

{}From the definition of $a'$ we get
\begin{equation} \label{eqn:102}
\begin{aligned}
& \opn{Ad} \bigl( (g'_{(0, 1)})^{-1} \bigr) (a'_{(1, 2, 3)}) 
\\ 
& \qquad = \opn{Ad} \bigl( (g'_{(0, 1)})^{-1} \circ f_{(1)} \bigr)
\Bigl( c_{(1, 3)}^{-1} \circ a_{(1, 2, 3)} \circ
\opn{Ad}(g_{(1, 2)}^{-1})(c_{(2, 3)}) \circ c_{(1, 2)} \Bigr)
\\
& \qquad \overset{\heartsuit}{=} \opn{Ad} \bigl( f_{(0)} 
\circ \opn{D}(c_{(0, 1)}^{-1}) \circ (g_{(0, 1)})^{-1} \bigr)
\\
& \qquad  \qquad
\Bigl( c_{(1, 3)}^{-1} \circ a_{(1, 2, 3)} \circ
\opn{Ad}(g_{(1, 2)}^{-1})(c_{(2, 3)}) \circ c_{(1, 2)}  \Bigr)
\\
& \qquad \overset{\lozenge}{=}  
\bigl( \opn{Ad} (f_{(0)}) \circ \opn{Ad}(\opn{D}(c_{(0, 1)}^{-1})) 
\circ \opn{Ad}(g_{(0, 1)})^{-1} \bigr) 
\\
& \qquad  \qquad
\Bigl( c_{(1, 3)}^{-1} \circ a_{(1, 2, 3)} \circ
\opn{Ad}(g_{(1, 2)}^{-1})(c_{(2, 3)}) \circ c_{(1, 2)} \Bigr)
\\
& \qquad \overset{\square}{=} \opn{Ad} \bigl( f_{(0)} \bigr)
\Bigl( c_{(0, 1)}^{-1} \circ 
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(c_{(1, 3)}^{-1}) \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(a_{(1, 2, 3)}) 
\\
& \qquad \qquad \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1} \bigr)(c_{(2, 3)}) \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(c_{(1, 2)}) 
\circ c_{(0, 1)} \Bigr) .
\end{aligned}
\end{equation}
The equality marked $\overset{\heartsuit}{=}$ is true because
\[  (g'_{(0, 1)})^{-1} \circ f_{(1)} = f_{(0)} \circ \opn{D}(c_{(0, 1)}^{-1})
\circ (g_{(0, 1)})^{-1} ; \]
this is from condition (i) of Definition \ref{dfn:100}.
The equality marked $\overset{\lozenge}{=}$ is because $\opn{Ad}$ is a group
homomorphism. And $\overset{\square}{=}$ is because 
$\opn{Ad}(\opn{D}(c_{(0, 1)}^{-1})) = \opn{Ad}(c_{(0, 1)}^{-1})$, 
which is an instance of condition (ii) of Definition \ref{dfn:cosim.101}.

A consequence of condition (ii) of Definition \ref{dfn:101} and 
condition (ii) of Definition \ref{dfn:cosim.101} is that 
\[ \begin{aligned}
& a_{(0, 1, 2)}^{-1} \circ c \circ a_{(0, 1, 2)} =
\opn{Ad}(a_{(0, 1, 2)}^{-1})(c) 
\\
& \qquad = \opn{Ad}(\opn{D}(a_{(0, 1, 2)}^{-1}))(c) = 
\opn{Ad}(g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1} \circ g_{(0, 2)})(c)
\end{aligned} \]
for any $c \in G^2_2(x_{(0)})$. 
Therefore, taking 
$c := \opn{Ad}(g_{(0, 2)}^{-1})(c_{(2, 3)})$, we get
\begin{equation} \label{eqn:103}
\opn{Ad}(g_{(0, 2)}^{-1})(c_{(2, 3)}) \circ a_{(0, 1, 2)}
 = a_{(0, 1, 2)} \circ 
\opn{Ad}(g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1})(c_{(2, 3)}) .
\end{equation}

By the definition of $a'$ and by formula (\ref{eqn:102}) we have
\[ \begin{aligned}
& u' = 
\opn{Ad} ( f_{(0)} )
\Bigl(  c_{(0, 3)}^{-1} \circ a_{(0, 1, 3)}
\circ \opn{Ad}(g_{(0, 1)}^{-1})(c_{(1, 3)}) \circ c_{(0, 1)} \Bigr)^{-1}
\\
& \qquad \qquad \circ
\opn{Ad} ( f_{(0)} )
\Bigl( c_{(0, 3)}^{-1}  \circ a_{(0, 2, 3)} \circ
\opn{Ad}(g_{(0, 2)}^{-1})(c_{(2, 3)}) \circ c_{(0, 2)} \Bigr)
\\
& \qquad \qquad \circ  
\opn{Ad} ( f_{(0)} )
\Bigl(  c_{(0, 2)}^{-1} \circ a_{(0, 1, 2)} \circ
\opn{Ad}(g_{(0, 1)}^{-1})(c_{(1, 2)})  \circ c_{(0, 1)} \Bigr)
\\
& \qquad \qquad \circ \opn{Ad} \bigl( f_{(0)} \bigr)
\Bigl( c_{(0, 1)}^{-1} \circ 
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(c_{(1, 3)}^{-1}) \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(a_{(1, 2, 3)}) 
\\
& \qquad \qquad  \qquad \circ 
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1} \bigr)(c_{(2, 3)}) \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(c_{(1, 2)}) 
\circ c_{(0, 1)} \Bigr)^{-1} \ .
\end{aligned} \]
Canceling adjacent inverse terms we get
\[ \begin{aligned}
& u' = 
\opn{Ad} ( f_{(0)} ) \Bigl(  c_{(0, 1)}^{-1} \circ 
\opn{Ad}(g_{(0, 1)}^{-1})(c_{(1, 3)}^{-1}) \circ 
v' \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(c_{(1, 3)})
\circ c_{(0, 1)} \Bigr) \ , 
\end{aligned} \]
where
\[ \begin{aligned}
& v' := 
a_{(0, 1, 3)}^{-1} \circ a_{(0, 2, 3)} \circ 
\opn{Ad}(g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1})(c_{(2, 3)})
\circ a_{(0, 1, 2)} 
\\
& \qquad \qquad \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1} \bigr)(c_{(2, 3)}^{-1})
\circ \opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(a_{(1, 2, 3)}^{-1}) \ .
\end{aligned} \]
It suffices to prove that $v' = 1$. 
Using formula (\ref{eqn:103}) we have 
\[ \begin{aligned}
& v' =  a_{(0, 1, 3)}^{-1} \circ a_{(0, 2, 3)}
\circ a_{(0, 1, 2)} \circ 
\opn{Ad}(g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1})(c_{(2, 3)})
\\
& \qquad \qquad \circ
\opn{Ad} \bigl( g_{(0, 1)}^{-1} \circ g_{(1, 2)}^{-1} \bigr)(c_{(2, 3)}^{-1})
\circ \opn{Ad} \bigl( g_{(0, 1)}^{-1} \bigr)(a_{(1, 2, 3)}^{-1}) \ .
\end{aligned} \]
We now cancel two adjacent inverse terms, and use the fact that condition
(ii) of Definition \ref{dfn:101} holds for $(x, g, a)$, to conclude that 
$v' = 1$.
\end{proof}

Suppose $G$ is a crossed groupoid and $x, x' \in \opn{Ob}(G)$.
There is a right action of the group $G_2(x)$ on the set 
$G_1(x, x')$, namely 
$g \mapsto g \circ \opn{D}(a)$ for $g \in G_1(x, x')$
and $a \in G_2(x)$. The quotient set is 
\begin{equation}
\bsym{\bsym{\pi}}_1(G, x, x') := G_1(x, x') / G_2(x) . 
\end{equation}
Given $g, g' \in G_1(x, x')$ let us define 
\begin{equation}
G_2(x)(g, g') := \{ a \in G_2(x) \mid 
g' = g \circ \opn{D}(a) \} . 
\end{equation}
So $\bsym{\bsym{\pi}}_1(G, x, x) = \bsym{\bsym{\pi}}_1(G, x)$ and 
$G_2(x)(1_x, 1_x) = \bsym{\bsym{\pi}}_2(G, x)$
in the notation of Definition \ref{dfn:equiv-cosim.101}.

\begin{lem} \label{lem:cosim-equiv.100}
Let $\Phi : G \to H$ be a weak equivalence between crossed
groupoids. Then the induced functions 
\[ \bsym{\bsym{\pi}}_1(\Phi, x, x') : \bsym{\bsym{\pi}}_1(G, x, x') \to
\bsym{\bsym{\pi}}_1 \bigl( H, \Phi(x), \Phi(x') \bigr)  \]
and 
\[ \Phi : G_2(x)(g, g') \to 
H_2 \bigl( \Phi(x) \bigr) \bigl( \Phi(g), \Phi(g') \bigr) \]
are bijective for all $x, x' \in \opn{Ob}(G)$ and 
$f, f' \in G_1(x, x')$. 
\end{lem}

\begin{proof}
This is the same as the usual proof for $2$-groupoids (cf.\ 
\cite[Lemma 1.1]{MS}).
\end{proof}

\begin{proof}[Proof of Theorem \tup{\ref{thm:100}}]
The proof is a ``nonabelian diagram chasing'', made possible by
Lemma \ref{lem:104}.

We begin by proving that the function $\ol{\opn{Desc}}(\Phi)$ is
surjective. Given a descent datum $(y, h, b) \in \opn{Desc}(H)$, we
have to find a descent datum $(x, g, a) \in \opn{Desc}(G)$, and a gauge
transformation $(f, c) :  (y, h, b) \to \Phi(x, g, a)$ in $H$. 

Since the function 
$\bsym{\bsym{\pi}}_0(\Phi^0) : \bsym{\bsym{\pi}}_0(G^0) \to
\bsym{\bsym{\pi}}_0(H^0)$
is surjective, there is an object $x \in \opn{Ob}(G^0)$, and a
$1$-morphism $f \in H^0_1(y, y')$, where 
$y' := \Phi(x) \in \opn{Ob}(H^0)$. 
Define 
\[ h'' := f_{(1)} \circ h \circ f_{(0)}^{-1} \in 
H^0_1(y'_{(0)}, y'_{(1)})  \]
and 
$c'' := 1_{y_{(0)}} \in H^1_2(y_{(0)})$. 
Then $(y', h'')$ is a partial descent datum in $H$, and 
$(f, c''): (y, h) \to (y', h'')$ is a partial gauge transformation.
According to Lemma \ref{lem:104} there is a unique element 
$b'' \in H^2_2(y'_{(0)})$ such that 
$(y', h'', b'')$ is a descent datum in $H$, and 
$(f, c''): (y, h, b) \to (y', h'', b'')$ is a gauge transformation.

Now by Lemma \ref{lem:cosim-equiv.100} the function 
\[ \bsym{\bsym{\pi}}_1(\Phi^1, x_{(0)}, x_{(1)}) : 
\bsym{\bsym{\pi}}_1(G^1, x_{(0)}, x_{(1)}) \to
\bsym{\bsym{\pi}}_1 ( H^1, y'_{(0)}, y'_{(1)}) \]
is surjective. Hence there are elements
$g \in G^1_1(x_{(0)}, x_{(1)})$ and 
$c' \in H^1_2(y'_{(0)})$
such that, letting 
$h' := \Phi(g) \in H^1_1(y'_{(0)}, y'_{(1)})$, 
we have 
$h'' = h' \circ \opn{D}(c')$.
Consider the partial gauge transformation 
$(1_{y'}, c') : (y', h'') \to (y', h')$.
Lemma \ref{lem:104} there is a unique element 
$b' \in H^2_2(y'_{(0)})$ such that 
$(y', h', b')$ is a descent datum in $H$, and 
$(1_{y'}, c') : (y', h'', b'') \to (y', h', b')$
is a gauge transformation. Let 
$c := \opn{Ad}(f_{(0)}^{-1})(c')^{-1} \in H^1_2(y_{(0)})$.
Then 
\[ (f, c) :  (y, h, b) \to (y', h', b') \]
is a gauge transformation in $H$, and $(y', h') = \Phi(x, g)$. 

By Lemma \ref{lem:cosim-equiv.100} the function
\[ \begin{aligned}
& \Phi^2 : G^2_2 (x_{(0)})
\bigl( 1_{x_{(0)}}, g_{(0, 2)}^{-1} \circ g_{(1, 2)} \circ g_{(0, 1)}
\bigr) \\
& \qquad \to 
H^2_2 (y'_{(0)})
\bigl( 1_{y'_{(0)}}, (h'_{(0, 2)})^{-1} \circ h'_{(1, 2)} 
\circ h'_{(0, 1)} \bigr)
\end{aligned} \]
is bijective. Let $a \in G^2_2 (x_{(0)})$
be the unique element such that 
\[ \opn{D}(a) = g_{(0, 2)}^{-1} \circ g_{(1, 2)} \circ g_{(0, 1)} \]
and $\Phi(a) = b'$. Then the triple of elements 
$(x, g, a)$ satisfies condition (i) of Definition \ref{dfn:101}, and 
$\Phi(x, g, a) = (y', h', b')$. 
Now the element 
\[ u := a_{(0, 1, 3)}^{-1} \circ a_{(0, 2, 3)} \circ 
a_{(0, 1, 2)} \circ \opn{Ad}(g_{(0, 1)}^{-1})(a_{(1, 2, 3)})^{-1} 
\in G^3_2(x_{(0)}) \]
satisfies $\opn{D}(u) = 1$, so it belongs to the subgroup 
$\bsym{\bsym{\pi}}_2(G^3, x_{(0)}) \subset G^3_2(x_{(0)})$.
Since the group homomorphism 
\[ \bsym{\bsym{\pi}}_2(\Phi^3, x_{(0)}) : \bsym{\bsym{\pi}}_2(G^3, x_{(0)}) \to 
\bsym{\pi}_2(H^3, y'_{(0)}) \]
is injective, and since 
\[ \begin{aligned}
& \bsym{\pi}_2(\Phi^3, x_{(0)})(u) = \Phi^3(u) =
\\
& \qquad  
(b'_{(0, 1, 3)})^{-1} \circ b'_{(0, 2, 3)} \circ 
b'_{(0, 1, 2)} \circ \opn{Ad}(h'_{(0, 1)})^{-1}(b'_{(1, 2, 3)})^{-1} = 1 ,
\end{aligned} \]
we conclude that $u = 1$. Thus the triple $(x, g, a)$ satisfies 
condition (ii) of Definition \ref{dfn:101}, so it is a descent datum in 
$G$. 

Now we prove that the function $\ol{\opn{Desc}}(\Phi)$ is
injective. Given 
\[ (x, g, a), (x', g', a') \in \opn{Desc}(G) , \]
define
$(y, h, b) := \Phi(x, g, a)$ and $(y', h', b') := \Phi(x', g', a')$. Assume we
are given a gauge transformation 
\[ (f, c) :  (y, h, b) \to (y', h', b') \]
in $H$. We have to produce a gauge transformation 
\[ (e, d) :  (x, g, a) \to (x', g', a') \]
in $G$.

We know that the function 
\[ \bsym{\pi}_1(\Phi^0, x, x') : 
\bsym{\pi}_1(G^0, x, x') \to
\bsym{\pi}_1 \bigl( H^0, y, y' \bigr) \]
is surjective. Therefore there is a $1$-morphism 
$e \in G^0_1(x, x')$, and a $2$-morphism 
$v \in H^0_2(y)$, 
such that 
$\Phi(e) = f \circ \opn{D}(v)$. 
Let 
\[ \til{f} := f \circ \opn{D}(v) \in H^0_1(y, y') \]
and
\[ \til{c} := \opn{Ad}(h^{-1})(v_{(1)}^{-1}) \circ c \circ v_{(0)} \in 
H^0_2(y_{(0)}) . \]
A simple calculation shows that 
\[ (\til{f}, \til{c}) :  (y, h, b) \to (y', h', b') \]
is also a gauge transformation. 

Recall that $\Phi(e) = \til{f}$, so  
\[ \Phi(g^{-1} \circ e_{(1)}^{-1} \circ g' \circ e_{(0)}) = 
h^{-1} \circ \til{f}_{(1)}^{-1} \circ h' \circ \til{f}_{(0)} =
\opn{D}(\til{c}) . \]
This is condition (i) of Definition \ref{dfn:100} for the gauge transformation 
$(\til{f}, \til{c})$.
Because the group homomorphism 
\[  \bsym{\pi}_1(\Phi^1, x_{(0)}) : 
\bsym{\pi}_1(G^1, x_{(0)}) \to
\bsym{\pi}_1 ( H^1, y_{(0)}) \]
is injective, it follows that there is an element 
$d' \in G^1_2(x_{(0)})$ such that 
\[ g^{-1} \circ e_{(1)}^{-1} \circ g' \circ e_{(0)} = \opn{D}(d') . \]
Consider the element 
$w := \til{c} \circ \Phi(d')^{-1} \in H^1_2(y_{(0)})$. 
It satisfies $\opn{D}(w) = 1$, so it belongs to the subgroup 
$\bsym{\pi}_2(H^1, y_{(0)})$. But the homomorphism 
\[ \bsym{\pi}_2(\Phi^1, x_{(0)}) : 
\bsym{\pi}_2(G^1, x_{(0)}) \to
\bsym{\pi}_2 ( H^1, y_{(0)}) \]
is bijective, so there is a unique element 
$v \in G^1_2(x_{(0)})$ satisfying $\opn{D}(v) = 1$ and 
$\Phi(v) = w$.
Let $d := v \circ d' \in G^1_2(x_{(0)})$.
Then $\Phi(d) = \til{c}$ and
\[ \opn{D}(d) = \opn{D}(d') = g^{-1} \circ e_{(1)}^{-1} \circ g' \circ e_{(0)}
. \]
Thus the pair $(e, d)$ is a partial gauge transformation 
$(x, g) \to (x', g')$. 

The last thing to check is that condition (ii) of Definition \ref{dfn:100}
holds for $(e, d)$. Let 
\[ u := \opn{Ad}(e_{(0)}^{-1})(a')^{-1} \circ    
d_{(0, 2)}^{-1} \circ a \circ 
\opn{Ad}(g_{(0, 1)}^{-1})(d_{(1, 2)}) \circ d_{(0, 1)}
\in  G^2_2(x_{(0)}) . \]
A direct calculation shows that 
$\opn{D}(u) = 1_{x_{(0)}} \in G^2_1(x_{(0)})$, so 
$u \in \bsym{\pi}_2(G^2, x_{(0)})$. 
We know that $\Phi(u) = 1_{y_{(0)}}$, and that the homomorphism 
\[ \bsym{\pi}_2(\Phi^2 ,x_{(0)}) : \bsym{\pi}_2(G^2 ,x_{(0)}) \to
\bsym{\pi}_2(H^2 ,y_{(0)}) \] 
is injective. It follows that $u = 1_{x_{(0)}}$, which is
what we had to check.
\end{proof}
