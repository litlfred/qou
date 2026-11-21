---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-011-sufficiency-of-external-relations
section_title: "Sufficiency of External Relations"
section_number: null
pages: 54-60
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.981
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:external sufficient}
Equipped with prime commutativity, legs and waist relations, co-legs and co-waist relations, we are ready to state a sufficiency theorem among $G_2 $ generators.


\begin{thm} \label{mainthmG2}
$\operatorname{Cob}( 3)_{S^2} $ has a presentation with $G_2$ generators under commutative Frobenius relations, prime commutativity, legs and waist relations, and co-legs and co-waist relations.
\end{thm}

\begin{proof}
Proposition \ref{generate} shows that $G_2 $ is generating. We need to show that the relations listed above are sufficient. Let $[M]$ be a bordism, and $f_0, f_1:M\to \mathbb{R}$ admissible excellent Morse functions inducing two generating compositions. We claim that there is a path from $f_0$ to $f_1$ which exhibits finitely many prime-commutativity relations, co/legs and co/waist relations, or fails to be excellent Morse at finitely many times due to commutative Frobenius relations. Thus the two compositions of $[M]$ are related by a sequence of prime relations and commutative Frobenius relations.

First, either $M$ is closed and $[M] \in \operatorname{End}(\emptyset)$, or $[M]$ has a non-empty boundary. We treat the two cases slightly differently.

If $[M]$ has at least one boundary component $S$, say outgoing, then for the Morse decomposition induced by $f_0 $, 
\begin{enumerate}
\item take a path $\gamma $ from a point on a particular prime endomorphism $p^{\times \times} $ to a point 
$x\in S$.

\item since $M$ is compact, it is finitely generated. Therefore the path $\gamma $ intersects finitely many generating bordisms. In particular it may intersect the boundary of an individual bordism multiple times.

\item The idea is to ``carry'' $p^{\times \times} $ along this path until we reach the outgoing boundary. Take a chronological ordering of the bordism pieces intersected by $\gamma $ as $p\setminus \operatorname{int}(D^3\sqcup D^3), M_1, M_2, \dots M_I$ . For each $M_i$ take a chronological ordering of the boundary components intersected by $\gamma $ as $b_1^i, b_2^i, \dots b_{J_i}^i $. Since the path originates from $p^{\times \times} $, $b_1^1$ is the boundary along which $p^{\times \times}  $ is composed with $[M_1]$. Since the path terminates on $S$, we have $b_{J_I}^I = S$.

If $b_1^i, b_{J_i}^i$ are different boundary components, apply the appropriate relation. After the relation is applied, $[p]$ is composed with $[M_i]$ along boundary component $b_{J_i}^i$ and, since $[M_i]$ and $[M_{i+1}]$ were glued along $b_{J_i}^i=b_1^{i+1}$, $p^{\times \times} $ is also composed with $[M_{i+1}]$ along boundary component $b_1^{i+1}$.

If $b_1^i = b_{J_i}^i$ are the same boundary component, namely $\gamma $ enters and exists $[M_i]$ through the same boundary component, then $[M_{i+1}] = [M_{i-1}]$. We take the identity relation (aka do nothing). Then $p^{\times \times} $ is still composed with $[M_i]$ along $b_1^i = b_{J_i}^i$ and with  $[M_{i+1}]$ along $b_1^{i+1}$.

\item The fact that $\gamma $ ends on $S=b_{J_I}^I$ guarantees that this process terminates with $p^{\times \times} $ ending up composed with $[M_I]$ along $S$.

\item We will then repeat this finite process for the remaining finitely many prime factors, each time choosing the target $S$ as the outgoing boundary of the previously chosen prime factor.

\item Now that all the prime bordisms are composed in a sequence, we use naturality to bring the composition to the form \[
\left( (p^{\times \times}_1 \circ p^{\times \times}_2 \circ \dots \circ p^{\times \times}_n) \otimes id  \right) \circ s_0
.\]
where $s_0$ is a composition of CF bordisms which equals $[\#^g \left( S^2 \times S^1 \right)  \setminus \operatorname{int}(\sqcup^{n_{inc}+n_{out}}D^3) ]$. Let $f_0 ': M\to  \mathbb{R}$ be a corresponding admissible Morse function. 

\item Repeat this process for $f_1 $, choosing the same outgoing boundary component $S$ at the beginning, bringing its corresponding composition to the form \[
\left( (p^{\times \times}_1 \circ p^{\times \times}_2 \circ \dots \circ p^{\times \times}_n) \otimes id  \right) \circ s_1
.\]
where $s_1$ is again a (possibly different) composition of CF bordisms which equals $[\#^g \left( S^2 \times S^1 \right)  \setminus \operatorname{int}(\sqcup^{n_{inc}+n_{out}}D^3) ]$. Let $f_1 ':M\to \mathbb{R}$ be a corresponding admissible Morse function.

\item By proposition \ref{prop:keypropCF}, there exists a path \[
\widehat{f}_t':I \times \left( \#^g \left( S^2\times S^1 \right) \setminus \operatorname{int}(\sqcup^{n_{inc}+n_{out}}D^3) \right) \to \mathbb{R}
\]
from $f_0' |_{\#^g \left( S^2\times S^1 \right)  \setminus \operatorname{int}(\sqcup^{n_{inc}+n_{out}}D^3)}$ to $f_1' |_{\#^g \left( S^2\times S^1 \right) \setminus \operatorname{int}(\sqcup^{n_{inc}+n_{out}}D^3)}$ which is admissible excellent spherical Morse at all but finitely many times where the failures are of CF type.

\item Hence there is a sequence of commutative Frobenius relations which sends $s_0 $ to $s_1 $. Taking the reverse process from $f_1 '$ to $f_1 $, we have obtained a sequence of relations which sends one composition to the other. Cerf-theoretically, there is a path $f_0$ to $f_0'$ exhibiting all the prime relations used in turning the composition into the standard form. We glue the path $\widehat{f}_t'$ and the constant path $f_0'|_{p_1 \# p_2 \dots \# p_n \setminus \operatorname{int}(D^3 \sqcup D^3)}$ together, forming a path $f_t'$ from $f_0'$ to $f_1 '$. Taking the path from $f_1 $ to $f_1 '$ in reverse, we have constructed a path from $f_0 $ to $f_1 $ with the desired property.
\end{enumerate}

If $[M]$ has empty boundary component, we must deal with the fact that there is no preferred boundary component to stack the prime factors. At first glance the situation is further complicated by the fact that $f_0 $ and $f_1 $ may achieve minima and maxima at different points on $M$, so there is no preferred point towards which to send the prime factors. However, we may treat $f_0 $, $f_1 $ independently. One can still choose regular values $r_0, r_1 $ close to say the maxima, such that the regular surfaces $S_0 = f_0 ^{-1}(r_0 ) ,S_1 = f_1 ^{-1}(r_1 ) $ are still diffeomorphic to $S^2$. We may repeat the same process, bringing all the prime factors towards the respective maxima using only prime commutativity and legs and waist relations, such that the composition induced by $f_0 $ is brought to the form \[
tr \circ p^{\times \times}_1 \circ p^{\times \times}_2 \circ \dots \circ p^{\times \times}_n \circ s_0 
.\]
and the composition induced by $f_1 $ brought to the form \[
tr \circ p^{\times \times}_1 \circ p^{\times \times}_2 \circ \dots \circ p^{\times \times}_n \circ s_1
.\]
where $s_0 ,s_1 $ are two composition sequences of CF bordisms which equals $[\#^g \left( S^2 \times S^1 \right)  \setminus \operatorname{int}( D^3)]$. Then proposition \ref{prop:keyprop} provides a sequence of commutative Frobenius moves turning $s_0 $ into $s_1 $.
\end{proof}

\begin{thm} \label{mainthmG1}
$\operatorname{Cob}( 3)_{S^2} $ has a presentation with $G_1$ generators and commutative Frobenius relations.
\end{thm}

It is very tempting to treat this as a corollary of theorem \ref{mainthmG2} by exploiting the fact that every $p^\times \in L$ can be written as $p^{\times \times}  \circ 1$ and then ``carry'' the prime factors to some extrema or boundary component like we did in the proof of \ref{mainthmG2}. However this is not a correct proof of the sufficiency of commutative Frobenius relations, at least not on the nose-- we would have to use the legs and waist relations of $G_2$, as well as prime commutativity of $G_2$.

What we need is instead a sequence of relations which preserves the prime $L$ morphisms of $G_1$. 

One way to fix this approach is by noting that even though $p^\times = p^{\times \times} \circ 1$ inevitably uses $p^{\times \times} $, we can rewrite $p^{\times \times} $ in terms of $p^\times$ to get \[
p^\times = p^{\times \times} \circ 1 = \Big(m\circ (p^\times \otimes id_{S^2})\circ \lambda^{-1}_{S^2}\Big) \circ 1
.\]
Notice that the right most term is entirely in terms of $G_1 $ generators. Then one only needs to show that prime commutativity, legs and waist relations of $P$ have analogous versions in terms of $m\circ (p^\times \otimes id_{S^2} \circ \lambda^{-1}_{S^2})$ as a whole, instead of $p^{\times \times} $, using only commutative Frobenius relations. Therefore each use of prime commutativity or legs and waist relations of $P$ does in fact result in a composition in terms of $G_1$ generators.

Below we present a cleaner proof without breaking up the $L$ generators. The proof requires the repeated use of the following lemma, see notations \ref{coherencenotations}:

\begin{lemma}\label{lemma:pullaside}
Let  $(\mathcal{C}, 1_{\otimes }, \alpha , \beta , \lambda, \rho )$ be a symmetric monoidal category, and let $f: A \to A'$, $g: B \to B'$, $h: C \to A \otimes B$, $p: 1_ \otimes \to S$ be morphisms. Then the following is true as morphisms $C \to A' \otimes B'$ \[
\left( f \otimes \left( p \otimes g \right)  \right) \circ \left( id_A \otimes \lambda ^{-1}_B \right) \circ h = \left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ \alpha _{A,B,S} \circ \left( h \otimes p \right) \circ \rho ^{-1}_C
\]
\end{lemma}

\begin{rmk}
Notice that one can use bifunctoriality and write the right hand side as \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ \alpha _{A,B,S} \circ \left( h \otimes id_S \right) \circ (id_C \otimes p) \circ \rho ^{-1}_C
.\]
\end{rmk}

\begin{mycom}
The take home lesson is this: given any morphism $M : C \to C'$ which is equal to a composition containing a factor of $p: 1_ \otimes \to S$, $M$ is necessarily of the form \[
M = H \circ \left( f \otimes \left(p \otimes g\right) \right) \circ (id_A \otimes \lambda^{-1}_B) \circ h
.\]
for some $H: A' \otimes \left( S \otimes B' \right) \to C'$. We have shown that $M$ has an alternative composition as \[
M = H \circ \left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ \alpha _{A,B,S} \circ \left( h \otimes p \right) \circ \rho ^{-1}_C
.\]
We can clean up the mess by packaging all but the last two terms together, into the form \[
M = \overline{H} \circ \left( h \otimes p \right) \circ \rho ^{-1}_C
.\]
This means that we can always extract/isolate the morphism $p$ by ``pulling it aside/passing through the right.''

The alternative form in the remark enables us to write \[
M = \overline{H'} \circ (id_C \otimes p) \circ \rho ^{-1}_C
.\]
which gives an extraction/isolation of $p$ by ``pulling aside and pushing down.'' These are best summarized intuitively in the following figure \ref{fig:pullaside}.

\begin{figure}[ht]
    \centering
    \incfig{pullaside}
    \caption[Pulling aside a map out of $1_\otimes$]{Pulling aside a map out of $1_ \otimes $.}
    \label{fig:pullaside}
\end{figure}




\end{mycom}

\begin{proof}[Proof of Lemma \ref{lemma:pullaside}]
Starting with the left hand side $\left( f \otimes \left( p \otimes g \right)  \right) \circ \left( id_A \otimes \lambda ^{-1}_B \right) \circ h$, first rewrite it using bifunctoriality as \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \left( \left( p \otimes id_B \right) \circ \lambda^{-1}_B \right)  \right) \circ h
.\]
Using the braiding relation $\left( p \otimes id_B \right) \circ \lambda^{-1}_B = \beta _{B,S}\circ \left( id_B \otimes p \right) \circ \rho ^{-1}_B$, the above is equivalent to \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \left( \beta _{B,S}\circ \left( id_B \otimes p \right) \circ \rho ^{-1}_B \right)  \right) \circ h
.\]
Rewrite this expression using bifunctoriality as \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta _{B,S} \right) \circ \left( id_A \otimes \left( id_B \otimes p \right)  \right) \circ \left( id_A \otimes \rho ^{-1}_B \right) \circ h
.\]
Using a coherence condition [Kelly 64] of unitors and aassociators, the following diagram commutes for all objects $X,Y$,

\[\begin{tikzcd}
{(X \otimes Y) \otimes 1_\otimes} && {X\otimes Y} \\
{X \otimes (Y \otimes 1_\otimes)}
\arrow["{\rho_{X \otimes Y}}", from=1-1, to=1-3]
\arrow["{\alpha_{X,Y,1_\otimes}}"', from=1-1, to=2-1]
\arrow["{id_X \otimes \rho_Y}"', from=2-1, to=1-3]
\end{tikzcd}\]
In particular for $X=A, Y=B$, we have $id_A \otimes \rho^{-1}_B= \alpha _{A,B, 1_ \otimes } \circ \rho ^{-1}_{A \otimes B} $, so the left hand side is equal to  \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta _{B,S} \right) \circ \left( id_A \otimes  \left( id_B \otimes p \right)  \right)  \circ \alpha _{A,B, 1_ \otimes } \circ \rho ^{-1}_{A \otimes B} \circ h
.\]
We may pass the associator to the left using naturality and get \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ  \alpha _{A,B,S} \circ \left( id_{A \otimes B}  \otimes p   \right) \circ \rho ^{-1}_{A \otimes B} \circ h
.\]
Shifting our attention to the last two terms, note that the naturality of the right unitor makes the following diagram commute

\[\begin{tikzcd}
C & {C\otimes 1_\otimes} \\
{A\otimes B} & {(A\otimes B) \otimes 1_\otimes}
\arrow["{\rho^{-1}_C}", from=1-1, to=1-2]
\arrow["h"', from=1-1, to=2-1]
\arrow["{h \otimes id_{1_\otimes}}", from=1-2, to=2-2]
\arrow["{\rho^{-1}_{A\otimes B}}"', from=2-1, to=2-2]
\end{tikzcd}\]
Hence $\rho ^{-1}_{A \otimes B} \circ h = \left( h \otimes id_{1_ \otimes } \right) \circ \rho ^{-1}_C$, and we get \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ  \alpha _{A,B,S} \circ \left( id_{A \otimes B}  \otimes p   \right) \circ \left( h \otimes id_{1_ \otimes } \right) \circ \rho ^{-1}_C
.\]
Combining the third and second to last terms, we get the desired right hand side \[
\left( f \otimes \left( id_S \otimes g \right)  \right) \circ \left( id_A \otimes \beta_{B,S} \right) \circ  \alpha _{A,B,S} \circ (h \otimes p) \circ \rho ^{-1}_C
.\]
\end{proof}




\begin{proof}[Proof of Theorem \ref{mainthmG1}]
Proposition \ref{generate} shows that $G_1 $ generates morphisms. So we need to show that commutative Frobenius relations are sufficient and necessary.

The idea of the proof for sufficiency is simple: use lemma \ref{lemma:pullaside} repeatedly by induction over finitely many prime units, isolating and grouping them into a manageable composite, such that whatever remains is generated by non-prime morphisms.  We then invoke proposition \ref{prop:keyprop}, freely changing the remaining morphisms using only commutative Frobenius relations. 

Precisely, let $[M]$ be a morphism in $\operatorname{Cob}(3)_{S^2}$ from $n_{inc}$-many $S^2$ to $n_{out}$-many $S^2$. Pick any representative and let its unique (non-$S^2 \times S^1$) prime factors be $p_1 , p_2 , \dots p_m$. Hence $[M]$ is $G_1 $-generated by commutative Frobenius generators as well as prime units $p^\times_1, \dots , p^\times_m: \emptyset \to S^2$. We want to show that any two such compositions are related by, and only by, commutative Frobenius relations.

Without loss of generality, consider the prime unit $p^\times_1$ in either compositions. As a morphism whose domain is $\emptyset $, the compositions necessarily take the form 
\begin{align*}
[M] &= H_1 \circ \left( f_1 \otimes (p^\times_1 \otimes g_1 ) \right) \circ (id_{A_1 } \otimes \lambda^{-1}_{B_1 }) \circ h_1 \\
[M] &= H_2 \circ \left( f_2 \otimes (p^\times_1 \otimes g_2 ) \right) \circ (id_{A_2 } \otimes \lambda^{-1}_{B_2 }) \circ h_2 
\end{align*}
for some morphisms $f_{1,2} : A_{1,2} \to A_{1,2}' $, $g_{1,2}: B_{1,2} \to B_{1,2}'$, $h_{1,2}: \otimes ^{n_{inc}} S^2 \to A_{1,2} \otimes B_{1,2}$, $H_{1,2}: A_{1,2}' \otimes (S^2 \otimes B_{1,2}') \to \otimes ^{n_{out}} S^2$. These morphisms themselves are generated by commutative Frobenius generators and the remaining prime units $p^\times_2 ,\dots , [p_m\setminus D^3]$.

Focusing our attention to the first composition, lemma \ref{lemma:pullaside} allows us to use only coherences to set the first composition as \[
[M] = \left( f_1  \otimes \left( id_{S^2} \otimes g_1  \right)  \right) \circ \left( id_{A_1 } \otimes \beta_{B_1 ,S^2} \right) \circ \alpha _{A_1 ,B_1 ,S^2} \circ \left( h_1 \otimes id_{S^2} \right) \circ (id_{\otimes ^{n_{inc}} S^2} \otimes p^\times_1) \circ \rho ^{-1}_{\otimes ^{n_{inc}} S^2}
.\]

Keeping the last two terms untouched, rewrite this composition in a shorten form as \[
[M] = \overline{H}_1^1 \circ (id_{\otimes ^{n_{inc}} S^2} \otimes p^\times_1)\circ \rho ^{-1}_{\otimes ^{n_{inc}}S^2}
.\]
where $\overline{H}_1^1 = \left( f_1  \otimes \left( id_{S^2} \otimes g_1  \right)  \right) \circ \left( id_{A_1 } \otimes \beta_{B_1 ,S^2} \right) \circ \alpha _{A_1 ,B_1 ,S^2} \circ \left( h_1 \otimes id_{S^2} \right): \otimes ^{n_{inc}+1} S^2 \to \otimes ^{n_{out}}S^2 $. Note that since $\overline{H}_1 ^1$ no longer has the $p^\times_1$ factor, it contains only the remaining prime factors $p^\times_2, \dots p^\times_m$. The $1$ in the superscript of $\overline{H}_1^1$ records this fact.

We may inductively repeat this process for each of the remaining prime factors, giving a sequence of equalities \[
\overline{H}_1^i = \overline{H}_1^{i+1} \circ (id_{\otimes ^{inc+i} S^2} \otimes p^\times_{i+1})\circ \rho ^{-1}_{\otimes ^{inc + i}S^2}
.\]
where $\overline{H}_1^j$ is generated by commutative Frobenius generators and prime factors $p^\times_{j+1}, \dots p^\times_m$. In particular, at the termination of this process, $\overline{H}_1^m $ is generated by commutative Frobenius generators alone.

Therefore using purely coherence relations, the first composition can be rewritten as\footnote{We are essentially casting the underlying 3 manifold into a normal form.} \[
[M] = \overline{H}_1^m \circ (id_{\otimes ^{inc + m} S^2} \otimes p^\times_m) \circ \rho ^{-1}_{\otimes ^{n_{inc}+m} S^2} \circ \dots \circ (id_{\otimes^{n_{inc}} S^2} \otimes p^\times_1) \circ \rho ^{-1}_{\otimes ^{n_{inc}} S^2}
.\]

Similarly, using purely coherence relations, the second composition can be rewritten as \[
[M] = \overline{H}_2^m \circ (id_{\otimes ^{inc + m} S^2} \otimes p^\times_m) \circ \rho ^{-1}_{\otimes ^{n_{inc}+m} S^2} \circ \dots \circ (id_{\otimes^{n_{inc}} S^2} \otimes p^\times_1) \circ \rho ^{-1}_{\otimes ^{n_{inc}} S^2}
.\]

Since both $\overline{H}_{1,2}^m$ are generated entirely by commutative Frobenius generators, proposition \ref{prop:keyprop} shows that they are related by commutative Frobenius relations. Recalling that we have not used any non-coherence relations, we have shown that any two $G_1$ compositions of $[M]$ can be turned into each other using commutative Frobenius relations alone.

That the commutative Frobenius relations are necessary follows from theorem \ref{thm:Cob2Cob3CFIso}. 










\end{proof}
