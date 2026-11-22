---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-003-unified-invariants-of-rational-homology-3spheres
section_title: "Unified invariants of rational homology 3–spheres"
section_number: null
pages: 4-5
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
In \cite{BBL}, we give a full generalization of the Habiro theory to
rational homology 3--spheres. This requires  completely new
techniques coming from number theory, commutative algebra,
quantum group and knot theory.
Let us explain this in more details.


Assume $M$ is a rational homology 3--sphere with
$|H_1(M,\Z)|=b$, where for a finite group $G$ we denote
by $|G|$ the number of its elements.
 Then
our unified invariant $I_M$ belongs to a modification $\R_b$ of the Habiro ring
where $b$ is inverted. Unlike the case  $b=1$, the modified Habiro ring
is not an integral domain, but a direct product of integral domains,
where each factor is determined by its own Taylor
expansion at some root of unity. There is a decomposition
 $I_M=\prod_{c|b} I_{M,c}$, where $I_{M,c}$ dominates the set
$\{\tau_M(\xi)|(\ord(\xi),b)=c\}$. If $b=1$, then $I_M$ coincides with Habiro's $J_M$.
The invariant $I_{M,1}$ was first defined in \cite{Le}.

Our results can be summarized in the following commutative
diagram. Here we assume for simplicity
that $b=p^k$ is a power of a prime and put $e_n:=\exp(2\pi I/n) $
the primitive $n$th root of unity.


\begin{diagram}
                &                        &\BC             &                                          &                 &\\
                &\ruTo(2,4)^{\tau_M(\xi)}&\uTo_{q=\xi}    &                                 &                 &\\
                &                        &\R_b&\rInto                                    &
                                                                                                 \prod^\infty_{i=0}\BZ\left[\frac{1}{p}, e_{p^i}
\right]\left[\left[e_{p^i}-q\right]\right]&\\
                &\ruTo~{I_M(q)}          &                &    &                 &\\
\{\BQ\text{HS}\}&                        &                &                                          & \dTo_{\text{projection to}\; i=0}    &\\
                &\rdTo_{\text{LMO}}      &                &                                          &                 &\\
				&                        &\A              &\rTo^{\frak {sl}_2\text{--weight}}_{\text{system}}&\BQ[[h]]     &
\end{diagram}

By $\BQ\text{HS}$ we denote the set of
rational homology 3--spheres $M$, with $|H_1(M,\Z)|=b$.
In particular, for any $M \in \BQ\text{HS}$,
we generalize Ohtsuki series as follows.


Let us fix a divisor $c<b$  of $b$,



then the Taylor expansion of $I_M$ at $e_c$ is a power series in $(q-e_c)$ with
coefficients in $\Z[1/b][e_c]$ which dominates the WRT invariants
at roots of unity whose order has the greatest common divisor $c$ with $b$.
If $c=b=p^k$, then  $I_{M,b}$ is a priory  determined by a product of power
series $\prod_{i\geq k} \BZ\left[\frac{1}{p}, e_{p^i}
\right]\left[\left[e_{{p^i}}-q\right]\right]$,
 however, conjecturally, it is enough to consider  the series in $q-e_b$.



The commutative diagram tells us that LMO invariant determines  $I_{M,1}$, or
the set of WRT invariants at roots of unity coprime with $b$.
Since there is no direct way to obtain power series in $(q-e_c)$ from the
LMO invariant, we conjecture the existence of the refined universal
finite type invariant, dominating our power series.
On the physical level of rigor, this means that the new refined
invariant should capture
more than just the contribution of flat connections
from the Chern--Simons theory.




The methods used in the unification
of the WRT invariants  also led to the full solution of
the integrality problem for quantum $SO(3)$ and $SU(2)$ WRT invariants.
In \cite{BL,BCL}, we showed that
$\tau_M^G(\xi)$ for any 3--manifold $M$ and any root of unity
is always an algebraic integer. Here $G=SO(3)$ or $SU(2)$.
The integrality of the  spin
and cohomological refinements is work in progress.





Assume $M$ is the Poincar\'e homology 3-sphere, obtained by surgery on a left-hand trefoil
with framing -1. Then
$$ I_M=\frac{1}{1-q} \sum^\infty_{k=0} q^k (1-q^{k+1})(1-q^{k+2})
\dots (1-q^{2k+1})\, .$$
We expect that  the categorification of
the WRT invariants will lead to  a
homology theory with  Euler characteristic given by $I_M$.





The paper is organized as follows. In Section \ref{defs} we recall
the definitions of Kirby moves,
WRT invariants and of the cyclotomic expansion for the colored Jones polynomial.
In Section 2 we state our main results and outline the proofs.
 Section 3 is
devoted to the discussion of the rings, where the unified
invariants take their values.
In addition, we construct generalized
Ohtsuki series.
The Laplace transform method, the Andrews identity, Frobenius maps
and the integrality of WRT invariants are explained in the last Section.
