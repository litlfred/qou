---
doc_id: arxiv-2211.08164v2
doc_title: "INFINITELY MANY RIEMANN SURF ACES WITH A TRANSITIVE ACTION ON THE WEIERSTRASS POINTS"
section_id: sec-002-3-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: 3
pages: 3-6
source_pdf: 2211.08164v2.pdf
source_sha256: aff9ff3ef5ac28be
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.975
doc_brief: "INFINITELY MANY RIEMANN SURFACES WITH A TRANSITIVE ACTION ON THE WEIERSTRASS POINTS — In this short note, we prove the existence of inﬁnitely many pairwise non-isomorphic, non-hyperelliptic Riemann"
---
The proof of the main theorem will be a consequence of the following four facts.

\s

\begin{customfact}{1} Let $\cX$ be a non-hyperelliptic compact Riemann surface of genus $g=3$. If the  automorphism group of $\cX$ acts transitively on the Weierstrass points then $\cX \in \mathscr{K}_3.$
\end{customfact}

\begin{proof}
Assume that the automorphism group $G$ of $X$ acts transitively on the Weierstrass points. By \cite[Theorem 1]{kato}, the weight of each of these points is either equal to 1 or 2. Since the sum of the weights of all the points of $X$ is equal to 24, the Riemann surface $X$ has either 12 or 24 \we points. In particular, the order of $G$ must satisfy $$|G|=12|G_P| \,\, \mbox{ or } \,\, |G|=24|G_P|$$ where $G_P$ stands for the stabiliser subgroup of a \we point $P$ of $X.$ It follows that the order of $G$ must be divisible by 12 and consequently, by \cite[Theorem 16]{bars}, the Riemann surface either belongs to $\mathscr{K}_3$ or is isomorphic to the Picard curve $$\mathscr{Q} : x^4 +y^4 +z^3x= 0.$$

This latter curve is the unique non-hyperelliptic Riemann surface of genus $g=3$ with exactly 48 automorphisms (see, for instance, \cite{CP} and \cite{Shaska}).

\s
 To prove the fact it suffices to verify that $X$ is not isomorphic to $\mathscr{Q}.$ Let  $$Q = [0:0:1] \in \mathscr{Q}$$ and denote by $\mathbb{C}(\bf{x},\bf{y})$  the function field of $\mathscr{Q}$. A straightforward  computation shows that $1/{\bf x}$ has a pole of order $4$ at $Q$ while it is regular elsewhere, and that ${\bf y}/{\bf x}$ has a pole of order $3$ at $Q$ while it is regular elsewhere. In other words,  $Q$ is a \we point of $\mathscr{Q}$, its gap sequence is $\{1,2,5\}$ and its weight is 2.  Now, the transitivity implies that all the \we points of $\mathscr{Q}$ have weight equal to $2$, which is the maximal possible weight in genus three. However, following \cite[Theorem 1.2]{keem}, there are exactly two Riemann surfaces of genus three on which all \we points are of maximal weight; these surfaces being $\mathscr{C}_0$ and $\mathscr{C}_3.$ Clearly, none of them is isomorphic to $\mathscr{Q}$ and the proof of the fact is done. 
\end{proof}
 
Although the following fact is known (see, for instance, \cite{FS}), we include a proof for the sake of completeness. 
 
  \begin{customfact}{2} \label{f2}
  Assume that $X$ is isomorphic to $\mathscr{C}_t$ with $t \neq 0, -1, \pm 2, t_0$ 
and let $G$ denote its automorphism group. Then the signature of the action of  $G$ on $X$ is $(0;2,2,2,3)$. In other words, the quotient $X/G$ is rational, the associated regular covering map $$X \to X/G \cong \mathbb{P}^1$$ramifies over exactly four values, and the corresponding fibers consist of ramification points with stabilisers of orders $2,2,2$ and $3$ respectively.
 \end{customfact}

\begin{proof} 
We recall that the signature of the action of a group isomorphic to $\mathbf{S}_4$ on a compact Riemann surface of genus $g=3$ is either $(0;2,2,2,3)$ or $(0; 3,4,4)$. 
Consider the automorphism of $\mathbb{P}^2$ given by
$$
\Phi([x:y:z]) = [-y:x:z]
$$and observe that $\Phi$ has only two fixed points$$P_1=[-i:1:0] \,\,\, \mbox{ and } \,\,\, P_2=[1:-i:0].$$
Note that $\Phi$ restricts to an automorphism of order 4 of $\mathscr{C}_t$ for each $t$. A straightforward computation shows that $P_1, P_2$ belong to $\mathscr{C}_t$ if and only if $t=2$, and therefore $$G \geqslant \langle \Phi \rangle \cong C_4$$is a group of automorphisms of $X$ acting without fixed points. This, coupled with the fact that ${\bf S}_4$ possesses a single conjugacy class of cyclic subgroups of order $4$, shows that there is no point of $X$ with $G$-stabiliser of order divisible by $4$. Hence, the signature cannot be $(0;3,4,4)$ and the claim follows.
\end{proof}



\begin{customfact}{3} \label{f3}
If $X$ is isomorphic to $\mathscr{C}_t$ with $t \neq 0, -1, \pm 2, t_0$ 
and there is a \we point of $X$ fixed by an involution of $X$ then the action of the automorphism group $G$ of $X$ is transitive on the \we points. \end{customfact}

\begin{proof}
 We recall that the group $\mathbf{S}_4$ has two conjugacy classes of cyclic subgroups of order two (a standard reference for permutation groups is \cite{Cameron}; a nice and concise list of properties of $\mathbf{S}_4$, including presentations, can be also found at \cite{database}). In terms of the presentation$$G \cong \mathbf{S}_4= \langle a,b,c,d : a^2, b^2,(ab)^2, c^3, cac^{-1}ab, cbc^{-1}a, d^2, dadab, [d,b], (dc)^2 \rangle,$$ these conjugacy classes are represented by $\langle d \rangle$ (of length 6) and by $\langle b \rangle$  (of length 3).  A computation shows that the action of $G$ on $X$ is topologically equivalent to the one represented by the generating vector $$(b,db,dc,c^{-1})$$(see \cite{Brou} for a precise definition of generating vector) and consequently, each involution $\iota$ of $G$ acts with fixed points. More precisely,  if $\iota$ is conjugate to $d$ then $\iota$ has 4  fixed points, and such points belong to two distinct orbits. By contrast,  if $\iota$ is conjugate to $b$ then $\iota$ has 4  fixed points, and such points belong to the same orbit (see Macbeath's formula \cite{mcB}).

\s

Now, assume that there exists a \we point $P$ fixed by an involution. The weight of points fixed by involutions was investigated by Towse. In fact, following his main results in \cite{towse}, the expected weight of a point fixed by an involution fixing $4$ points is equal to $0$, that is, these points are not \we points unless the image points in the quotient curve are \we points, either for the canonical or another linear series. In addition,  the parity of the actual weight  of such a point must agree with the parity of the expected weight. It follows that  the weight of $P$ is even; hence it is equal to $2$. If $P$ is fixed by an involution conjugate to $d$ then $X$ has  24 \we points of weight $2$; a contradiction. Thus, one sees that $P$ must be fixed by an involution conjugate to $b$. Thereby, the orbit of $P$ consists of 12 \we points of weight $2$, and the action is transitive, as claimed.
\end{proof}



 \begin{customfact}{4} \label{f4}
If $X \in \mathscr{K}_3$  then the automorphism group $G$ of $X$ acts transitively on the Weierstrass points.
\end{customfact}

\begin{proof} Since Klein's quartic and Fermat's quartic are known to have a transitive action on the \we points \cite{laings}, we only need to consider the remaining cases, namely, when $X$ is isomorphic to $\mathscr{C}_t$ where $t \neq 0, -1, \pm2, t_0.$ As proved in Fact \ref{f2}, in such a case the $G$-stabiliser subgroup of each point of $X$ is trivial, of order two or of order three.
\s

 Assume that there exists a \we point $P$ with trivial stabiliser. Then each point in the $G$-orbit of $P$ is a \we point. In particular, we have $24$ \we points of weight $1$, and the action is transitive. 
 
 \s
 
Now, suppose  that there exists a \we point $P$ fixed by an automorphism of order three. In such a case, $X$ has 8 \we points. It follows from the fact that $X$ is non-hyperelliptic that there exists a \we point $R$ which does not belong to the $G$-orbit of $P$. If the stabiliser of $R$ were trivial, then $X$ would have 32 \we points; a contradiction. It then follows from the preceding discussion that $R$ must be fixed by an involution conjugate to $b$ and therefore  the surface possesses, in addition to $P$ and its whole $G$-orbit, 12 \we points of weight 2. This is impossible and therefore there is no \we point among the fixed points of automorphisms of order three. 

\s

Finally, in the remaining case (namely, if there is a \we point fixed by an involution) the transitivity has been already proved. The proof of the fact then follows.
 \end{proof}


The previous four facts can be summarised in the following theorem.

\begin{customthm}{1}
 A non-hyperelliptic compact Riemann surface $X$ of genus three has automorphism group acting transitively on the \we points if and only if $X$ belongs to the family $\mathscr{K}_3.$
\end{customthm}


The proof of the main theorem follows directly from the result above.
