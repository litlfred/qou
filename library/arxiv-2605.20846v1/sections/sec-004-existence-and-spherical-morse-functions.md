---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-004-existence-and-spherical-morse-functions
section_title: "Existence and Spherical Morse Functions"
section_number: null
pages: 26-32
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.995
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:existenceandsphericalMorse}
\begin{defn} \label{defn:good}
Let $M$ be a compact oriented manifold possibly with boundary $\partial M$ and $f:M\to \mathbb{R}$ a Morse function. We say that $f$ is 
\begin{itemize}
\item ``admissible'' if $f : M \to \left[ a,b \right]  $ such that $a$ and $b$ are regular values and $\partial M = f^{-1}(a) \cup f^{-1}(b)$;
\item ``excellent'' if all critical values are distinct;
\item ``spherical'' if all regular level sets are disjoint unions of spheres.

\end{itemize}
\end{defn}

Standard Cerf theory, introduced in \cite{cerf_stratification_1970}, shows that two such admissible Morse functions $f_0 ,f_1 \in C^\infty(M)$ are connected by a path $f_t$ which fails to be ``excellent'' Morse only at finitely many points. For a short working exposition in the context of topological field theories, see the notes by \cite{FreedLecture23}. Passing through these bad points, the Morse function goes through either a birth-death singularity or a critical values exchange. We are interested in classifying those singularities whose regular level sets are disjoint unions of $S^2$, the defining feature of CF generators.

\begin{prop} \label{prop:CFcommFrob}
$C$ and $F$ generators satisfy commutative Frobenius relations.
\end{prop}

\begin{proof}
We handle the proof in two parts. The first part handles relations due to birth-death singularities, and the second part handles exchanges.

\begin{enumerate}
\item A birth-death singularity is the creation/annihilation of a pair of critical points whose indices are adjacent $(i,i+1)$, $i=0,1, \dots , \dim(M)$. In 3 dimensions, the possible birth-death singularities are between $(0,1)$, $(1,2)$, and $(2,3)$. Near the birth of these singularities, the path $f_t$ has the local form (up to a constant) \[
  f_t(x, y , z) = x^3 - t x \pm y^2 \pm z^2 ,\quad t\in \left[ -1, 1 \right] 		
.\]
More specifically, for $(0,1)$ birth\footnote{For the death version, take $f_{-t}$}, the local form is \[
  f_t(x,y,z) = x^3 - tx + y^2 + z^2
.\]
where the two critical points are $(\pm \sqrt{\frac{t}{3}} ,0,0)$ of index $0,1$ respectively. Geometrically, consider filling one of the missing 3-balls in $S^3 \setminus \operatorname{int}(D^3 \sqcup D^3 \sqcup D^3)$, resulting in $S^3 \setminus \operatorname{int}(D^3 \sqcup D^3)$.

\begin{figure}[ht]
    \centering
    \incfig{01death}
    \caption[Birth and Death of $(0,1)$ and $(2,3)$ critical points]{The birth and death of a pair of critical points of index $(0,1)$ and $(2,3)$. The first equality, when read from left to right, shows the death of critical points of indices $0$ and $1$. One can imagine pushing the left cone up until the bottom tip is level with the crouch of the pair of pants, then smoothly deform the result into a straight cylinder. When read from right to left, it depicts the birth of critical points of indices $0$ and $1$. The second equality when read from left to right depicts the birth of $2$ and $3$. }
    \label{fig:01death}
\end{figure}





The former is a representative of the pair of pants bordism $m$, while the latter is diffeomorphic to $S^2\times I$ which is a representative for the identity morphism $id_{S^2}$. The filling 3-ball is a representative of the unit bordism $1$. The first equality in figure \ref{fig:01death} provides a familiar geometric intuition. The local form of the birth of $(0,1)$ critical points encodes the geometric fact that $1$ is the unit with respect to the multiplication: \[
  m \circ (1 \otimes id_{S^2}) \cong id_{S^2}
.\]

The local form for the birth of $(2,3)$ critical points is \[
  f_t(x,y,z) = x^3 - tx -y^2 -z^2
.\]
which corresponds to the same picture but turned upside down as illustrated in figure \ref{fig:01death} as the second equality, encoding the geometric fact that $tr$ is the counit with respect to co multiplication\footnote{Strictly speaking, the left side needs to be pre-composed with a unitor. We shall ignore the unitors and associators for this part of the proof for clarity. However much of the rest of the paper work with them more carefully and explicitly.}: \[
  (tr \otimes id_{S^2})\circ m^\vee \cong id_{S^2}
.\]






\item This part of the proof is inspired by \cite{FreedLecture23}. By a classic theorem in Morse theory \cite{hirsch_differential_1976} Thm 3.4 and 3.5, if $f:\widehat{M}\to \left[ a,b \right] $ is a Morse function on a closed manifold $\widehat{M}$, and $v_k$ is the number of critical points of $f$ of index $k$, then \[
  \chi (\widehat{M}) = \sum_{k=0}^{\dim(M)}  (-1)^k v_k
.\]

We want to classify all possible connected bordisms before and after exchanges of two critical values. We demand such a bordism has two critical points at all times along the Cerf path $f_t$. Let $(i,j)$ denote the indices of the critical points whose critical values are exchanged. We know that neither $i$ nor $j$ can be $0$ -- indeed, at the singular time when the critical values coincide, the critical level set must be connected. Otherwise it takes a handle attachment to connect the index $0$ critical point to the other critical point, which is only possible if $M$ has at least 3 critical points. 

A similar argument shows that neither $i$ nor $j$ can be $3$.

So there are only three possible exchanges we need to classify:  indices $(1,1)$, $(1,2)$, and $(2,2)$ exchanges. The $(2,1)$ exchange is the reversal of the $(1,2)$ exchange by taking $f_{-t}$. 

Since $m$ and $m^\vee$ are the generators of index $1$ and $2$ in CF, we need only consider relations involving these two generators. They respectively decreases/increases the number of boundary components by $1$. By using only two of them, the only possible changes in incoming to outgoing boundary components is $1\to 1$, $2\to 2$, $3\to 1$, and $1\to 3$.

Let $M$ be such a bordism, and let $\widehat{M}$ be the closed manifold one obtains by filling in the boundary components. Then \[
  0= \chi(\widehat{M}) = v_0 -v_1 +v_2 -v_3 
.\]
where $v_0 $ is the number of incoming components and $v_3 $ is the number of outgoing components. \footnote{Secretely using the fact that one can glue two Morse functions together}

For the case of $3\to 1$, we learn that $-v_1 +v_2=-2$, and since we only have two critical points on $M$ at all times, the critical points being exchanged must have indices $(1,1)$. Therefore we are looking for two combinations of two $m$ 's which are both bordisms with three incoming and one outgoing boundary components. There are only two, illustrated in figure \ref{fig:assocandcoassoc}-(a), which are the three dimensional analogue of the associativity condition in two dimensions: \[
  m \circ (m \otimes id_{S^2}) \cong m \circ (id_{S^2} \otimes m)
.\]

\begin{figure}[ht]
    \centering
    \incfig{assocandcoassoc}
    \caption[Associativity and Co-associativity]{(a) Associativity of multiplication. (b) Coassociativity of comultiplication.}
    \label{fig:assocandcoassoc}
\end{figure}



For the case of $1\to 3$, we learn that $-v_1 +v_2 =2$, meaning the exchange is of type $(2,2)$, so we are looking for ways to compose two $m^\vee$ which results in one incoming and two outgoing boundary components. The only two possible compositions illustrated in figure \ref{fig:assocandcoassoc}-(b) are the three dimensional analogue of coassociativity in two dimensions: \[
  (m^\vee \otimes id_{S^2}) \circ m^\vee \cong (id_{S^2} \otimes m^\vee) \circ m^\vee
.\]





For the case of $2\to 2$, we learn that $-v_1 +v_2 =0$, so the exchange is of type $(1,2)$. The only two possible compositions of one  $m$ and one $m^\vee$ which result in a bordism from two incoming to two outgoing boundary components are the analogue of the Frobenius relation: \[
  m^\vee \circ m \cong (m \otimes id_{S^2})\circ  (id_{S^2} \otimes m^\vee)
.\]

This is depicted in figure \ref{fig:12frob}.
\begin{figure}[ht]
    \centering
    \incfig{12frob}
    \caption[Frobenius relation]{Frobenius relation}
    \label{fig:12frob}
\end{figure}





\end{enumerate}

So far we have demonstrated that CF has units, counits, associativity, coassociativity, and the Frobenius relation. By \cite{kock_frobenius_2003} these are equivalent to the relations which define a Frobenius algebra, namely these bordisms form the Frobenius PROP.  We have co/commutativity as well, upgrading to a commutative Frobenius relation. All together we see that CF generators satisfy commutative Frobenius relations.
\end{proof}

\begin{rmk} \label{rmk:12Bnotspherical}
It is worth drawing attention to the fact that even though type $(1,2)$ birth-death singularities are allowed by generic Cerf theory along path $f_t$ connecting two Morse functions $f_{0,1}:M\to \mathbb{R}$, it does not constitute a relation among the CF generators-- these generators, along with their pre-equipped Morse functions, have spherical regular surfaces. However the local form of type $(1,2)$ birth singularity is given by \[
f_t(x,y,z) = x^3 - tx -y^2 + z^2 ,\quad t\in \left[ -1,1 \right] 
.\]
For $t<0$ there are no critical points. $t=0$ has a degenerate critical point at the origin. For $t>0$ there are two critical points $(\pm \sqrt{\frac{t}{3}} ,0,0)$, of index $1$ and $2$ respectively. Let $r \in f_{t}(\pm \sqrt{\frac{t}{3}} ,0,0)$ be a regular value, one can show that the regular level surface $f_t ^{-1}(r) $ has genus at least 1 (see figure \ref{fig:12b}). Therefore there is no type $(1,2)$ birth-death relations between CF generators.

\begin{figure}[ht]
    \centering
    \incfig{12b}
    \caption[The local picture of the birth of a pair of critical points of index $1$ and $2$]{The local picture of the regular surface $f^{-1}(r)$ after the birth of a pair of critical points $c_{1,2}$ of index $1$ and $2$, where $f(c_1) < r < f(c_2)$. Notice that this surface has genus at least 1, hence is not spherical.}
    \label{fig:12b}
\end{figure}




Cerf-theoretically, this means the type $(1,2)$ birth-death singularities cannot occur if we demand the path $f_t$ between two ``good'' Morse functions $f_0 ,f_1 $ remains ``good'' Morse. By ``good'' Morse here we mean spherical admissible Morse functions-- whose regular level sets are all disjoint unions of two-spheres. 
\end{rmk}

\begin{rmk} \label{S2xS1PantsvsHeegaard}
It is also worth noting that we did not treat the type $1 \to 1$ exchanges, which has $-v_1 +v_2 =0$, meaning the critical values being exchanged are of indices $(1,2)$. There is only one such bordism which is a composition of CF generators, analogous to the pants decomposition of the torus in two dimensions in figure \ref{fig:s2s2pantsvsheegaard}-(a) : \[
\Big[ (S^2 \times S^1 )\setminus \operatorname{int}(D^3 \sqcup D^3) \Big]  = m \circ m^\vee
.\]
\begin{figure}[ht]
    \centering
    \incfig{s2s2pantsvsheegaard}
    \caption[Pants and Heegaard decomposition of $S^2 \times S^1$]{Two different decompositions of $S^2 \times S^1$. Figure (a) is the usual ``pants'' decomposition which resembles the pants decomposition of a torus in 2-dimensions. A regular surface $f^{-1}(r)$, for any $r$ between the index $2$ and $1$ critical values, is the disjoint union $S^2 \sqcup S^2$. In contrast, figure (b) is the (minimal) Heegaard decomposition, where a regular surface $f^{-1}(r)$, for any $r$ between the index $1$ and $2$ critical values, is a torus. }
    \label{fig:s2s2pantsvsheegaard}
\end{figure}




To understand what happens if one insists on a $(1,2)$ exchange to occur, consider the following Morse function introduced earlier in remark \ref{rmk:S2xS1redundant}\[
S^2 \times S^1 \overset{\text{proj}}{\longrightarrow } S^1 \overset{\text{Height}}{\longrightarrow} \mathbb{R}
.\]

The standard decomposition of this Morse function induces the composition \[
[S^2 \times S^1] = tr \circ m \circ m^\vee \circ 1
\]
where the elementary bordisms are of index $3, 1, 2, 0$ respectively, in descending critical value . If we exchange the critical values of the critical points whose indices are $(1,2)$, the indices would read $3,2,1,0$ in descending critical value. But the only way to attach a 1-handle to a ball would increase the bounding surface genus by 1. So the regular surface between index 2 and 1 is a torus, and this Morse function gives the (minimal) Heegaard splitting \ref{thm:HeegaardSplitting} of $S^2\times S^1$, illustrated in figure \ref{fig:s2s2pantsvsheegaard}-(b).





While this type of exchange is perfectly normal in generic Cerf theory, it does not give us a relation between CF generators, which requires that the Morse functions before and after have no regular level set which has a non-zero genus component.

We will say more about this in example \ref{eg:S2xS1pantstoHeegaardtopants} after introducing an important lemma.
\end{rmk}







\begin{lemma}
Let $\left[ M \right] $ be a morphism in $\operatorname{Cob}(3)_{S^2,CF}$. Then there exists an admissible excellent spherical Morse function on a representative $M$.
\end{lemma}

\begin{proof}
Each CF generator comes with a standard Morse function which is spherical. Since $ M $ comes with a decomposition in terms of glueing CF generators, we can glue their Morse functions together in a collared neighbourhood of the glueing boundaries after appropriate shifts. The resulting Morse function is by definition spherical and admissible on $M$. If two critical values coincide, take a small perturbation of the Morse function, rendering the values distinct and the function excellent.
\end{proof}

\begin{rmk}
The lemma addresses the existence of an admissible excellent spherical Morse function. It is always possible that there is a different composition, giving rise to a different admissible excellent spherical Morse function on $M$. Given that these compositions are the Morse data of two Morse functions, we know the full theory of Cerf can be employed. Therefore these two compositions must be related by a sequence of Cerf moves. However, the example below shows that we cannot maintain the ``spherical-ness'' of the Cerf path in 3 dimensions. Therefore it raises the question whether CF relations are sufficient. The next two sections ensure that they are indeed sufficient.
\end{rmk}

\begin{eg} \label{eg:S2xS1pantstoHeegaardtopants}
($S^2\times S^1$ Pants to Heegaard to Pants) Take any pants decomposition of $S^2 \times S^1$, induced by a Morse function we call $f_{\text{pants}}$. There is a path from $f_{\text{pants}}$ to itself, which first exchanges the order of the 1-handle and 2-handle attachments, then exchanges the order again, undoing the first switch. As we explained in remark \ref{S2xS1PantsvsHeegaard}, a Morse function along the path after the first exchange has a toric regular level set between the index $1$ and $2$ critical values, hence the interval between the two exchanges are aspherical, corresponding to the minimal Heegaard splitting of $S^2\times S^1$. Figure \ref{fig:kirby} presents the Kirby graphics of this Cerf path.

\begin{figure}[ht]
    \centering
    \incfig{kirby}
\caption[The Kirby graphics for a path $f_t$ which fails to remain spherical]{The Kirby graphics for a path at $f_{\text{pants}}: S^2 \times S^1$ which fails to remain spherical as it exchanges the index $1$ and $2$ critical points. After the exchange the Morse function along the path segment now gives the genus 1 Heegaard splitting of $S^2\times S^1$.}
    \label{fig:kirby}
\end{figure}



\end{eg}
