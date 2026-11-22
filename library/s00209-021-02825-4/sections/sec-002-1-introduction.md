---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
In 1914, Pólya and Schur [14] characterized the set of diagonal linear operators on polyno-
mials which preserve real-rootedness. Since this seminal paper, much work has been done in
extending this characterization to other classes of linear operators. This program in essence
came to a close in 2009 with a paper of Borcea and Brändén [1], which gave a complete
characterization of linear operators on polynomials which preserve real-rootedness.
Their real-rootedness preservation characterization is derived from a more general
result pertaining to stable polynomials. Given  ⊂Cm, we say that a polynomial f ∈
C[x1, . . . , xm] is -stable if f does not vanish in . Further, f is real stable if it has
real coefﬁcients and is Hm
+-stable, where H+ ⊂C is the open upper half-plane. (We also
denote the open lower half-plane by H−⊂C.) We additionally use the terms weakly -
stable and weakly real stable if we allow f ≡0. Finally, we write f ∈Cλ[x1, . . . , xm] for
λ ≡(λ1, . . . , λm) if f is of degree at most λk in xk. We are then led to the following problems
for K ∈{C, R}, generalized from the Pólya-Schur characterization:
Problem 1 Characterize linear operators T : Kλ[x1, . . . , xm] →K[x1, . . . , xm] preserving
weak -stability.
Problem 2 Characterize linear operators T : K[x1, . . . , xm] →K[x1, . . . , xm] preserving
weak -stability.
B Jonathan Leake
jonathan@jleake.com
1
Technische Universität Berlin, Berlin, Germany
1360
J. Leake
In [1], Borcea and Brändén were able to solve these problems in many cases. In particular,
they solved both problems for K = R and  = Hm
+, where m = 1 corresponds to the case
of preservation of real-rooted polynomials. For K = C, they were able to solve Problem 1
for  that is any product of open circular regions in C.
In this paper we will only be concerned with Problem 1, for which we now state the solution
from [1]. Given a linear operator T : Kλ[x1, . . . , xm] →K[x1, . . . , xm], a polynomial
SymbBB(T ) called the (Borcea–Brändén) symbol is associated to T . Speciﬁcally, the symbol
is a polynomial in Kλ⊔λ[x1, . . . , xm, z1, . . . , zm] (i.e., of 2m variables), where λ ⊔λ :=
(λ1, . . . , λm, λ1, . . . , λm). The crucial feature of the symbol is that it shares certain stability
properties with its associated linear operator, which yields the characterizations stated in the
following results. (We will express these results in more detail in Sects. 6 and 7.)
Theorem 1.1 (Borcea–Brändén)Fixalinearoperator T : Cλ[x1, . . . , xm] →C[x1, . . . , xm]
which has image of dimension greater than one. Then, T maps Hm
+-stable polynomials to
weakly Hm
+-stable polynomials if and only if SymbBB(T ) is H2m
+ -stable.
Theorem 1.2 (Borcea–Brändén)Fixalinearoperator T : Rλ[x1, . . . , xm] →R[x1, . . . , xm]
which has image of dimension greater than two. Then, T maps real stable polynomials to
weakly real stable polynomials if and only if either SymbBB(T ) or SymbBB(T −) is real
stable, where T −(p) := T (p(−x1, . . . , −xm)).
To deal with other products of circular regions, one then conjugates T by certain Möbius
transformations and applies Theorem 1.1 to the conjugated operator. Unfortunately though,
this is a tedious process which has to be done each time a new stability region is to be
considered. Additionally, the image dimension restrictions give rise to degeneracy cases
which have to be dealt with separately. Both of these issues obscure the connection between
an operator and its symbol.
In this paper, we present a new conceptual approach to the Borcea–Brändén characteriza-
tion via the representation theory of SL2(C). In particular, we derive a new symbol (denoted
Symb) in a natural way, and our deﬁnition eliminates the issues discussed above. This is seen
in the following results, which are our simpliﬁed and generalized versions of the Borcea–
Brändén characterizations. Note that for the sake of simplicity, we have omitted a few details
here regarding non-convex circular regions. Speciﬁcally, circular regions of C should be
thought of as lying in the Riemann sphere, so that complements of discs contain the point at
∞.
Theorem 6.2 Fix a linear operator T : Cλ[x1, . . . , xm] →Cα[x1, . . . , xl], a product of
all open or all closed circular regions 0 = C1 × · · · × Cm, and a product of sets 1 :=
S1 × · · · × Sm. Further, denote 0 := (C\C1) × · · · × (C\Cm). Up to certain degree
and convexity (of Ck) restrictions, we have that T maps 0-stable polynomials to nonzero
1-stable polynomials if and only if Symb(T ) is (0 × 1)-stable.
Theorem 7.2 Fix a linear operator T : Rλ[x1, . . . , xm] →Rα[x1, . . . , xl]. Up to certain
degree restrictions, T maps real stable polynomials to nonzero real stable polynomials if and
only if Symb(T ) is either (H−
m × Hl
+)-stable or (H−
m × Hl
−)-stable.
We summarize the speciﬁc improvements that this and our other related results give over
the Borcea–Brändén characterization as follows.
1. Different stability regions can be considered using the same symbol. The symbol we
deﬁne in this paper is universal: for example, it gives stability-preservation information
for any product of open circular regions. The Borcea–Brändén symbol, on the other hand,
required the application of Möbius transformations. In addition, our symbol also allows
A representation theoretic explanation...
1361
for the output stability region to be chosen independently of the input stability region.
While this does not literally improve the result, it does allow for quicker computations.
In particular, see Examples 6.3 and 6.4 where classical polynomial convolution results
are easily derived from our framework.
2. Our characterization does not require any degeneracy condition. Our results characterize
operators which preserve (strong) stability rather than weak stability. As seen above,
this slightly stronger notion of stability enables us to eliminate any image dimension
degeneracy condition, as required in the Borcea–Brändén characterizations (Theorems
1.1 and 1.2). This demonstrates a cleaner link between an operator and its symbol.
3. Closed circular regions and projectively convex regions can be considered. The symbol
we deﬁne in this paper handles products of open circular regions, as well as products of
closed circular regions. (In [12], Melamud proves a result similar to the Borcea–Brändén
characterization for closed circular regions.) Further, we are also able to consider more
general projectively convex regions (circular regions with portions of their boundary; also
called generalized circular regions, see [18] and [17]) in Proposition 6.5. This allows
us to determine stability-preservation information about real intervals and half-lines. It
also turns out, somewhat surprisingly, that our symbol can handle products of any sets
as possible output space stability regions (as seen in Theorem 6.2 above).
In the process of generalizing the Borcea–Brändén characterization we develop a general
algebraic framework which also encompasses many of the classical polynomial tools. This
framework aims to motivate classical results and provide intuition for the connection between
a stability preserving operator and its symbol.
