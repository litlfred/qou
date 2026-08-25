---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-026-14-it-follows-from-the-axioms-1-and-2-that-a-com
section_title: "It follows from the axioms (1) and (2) that a compact oriented 3-manifold M with ∂M ="
section_number: 14
pages: 34-37
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting"
---
(−Σ 1) ⊔ Σ 2 determines a linear map Z(M ) ∈ HomC(HΣ 1 , HΣ 2 ). Such a manifold M is called a
cobordism between Σ 1 and Σ 2.
33
whereM is a representation space of π1(Σ) into the compact part of the gauge group,
G. Therefore, the corresponding Hilbert space HΣ is not ﬁnite dimensional. To be more
speciﬁc, by analogy with the SL(2,C) case studied in this paper, one might deﬁne the
quantum Hilbert space HΣ of a Chern-Simons theory with gauge group GC as a space of
half-densities onP. Since this space is inﬁnite-dimensional, one needs a reﬁne ment of the
above deﬁnition in order to prove that we deal with a topologi cal quantum ﬁeld theory in a
mathematical sense. Physical considerations suggest, how ever, that there exists a rigorous
mathematical deﬁnition of the topological invariant Z(M ;γi,R i), which we postpone to
future work.
Implications for Representation Varieties and the A-polyn omial
Apart from deﬁning a topological invariant of three-manifo lds with links colored by
inﬁnite-dimensional representations, Chern-Simons theo ry can also shed some light on
the properties of representation varieties (2.3), in parti cular, on the properties of the A-
polynomial. Thus, a lot of interesting information about L = Hom
(
π1(M );G
C
)
/GC and
about the 3-manifold M itself can be obtained by treating L as a Lagrangian submanifold
inP. In particular, as we saw earlier, the Lagrangian inclusion֒Pis a natural
starting point for quantization, and can lead to new connect ions between three-dimensional
topology, symplectic geometry, and perhaps even Langlands ’ program [73].
For instance, it directly follows from this new perspective that the “volume formula”
(3.30) and the “Chern-Simons formula” (3.31) can be general ized to hyperbolic 3-manifolds
with arbitrary boundary Σ, not necessarily connected. Ther e is a nice class of examples
of such manifolds called convex cores, which have ﬁnite volu me [74] and may be useful in
this context. Even though the explicit description of the re presentation variety
L = Hom (π1(M );SL(2,C))/SL(2,C) (4 .3)
may be very complicated for a generic 3-manifold M with boundary Σ, the ambient space
P is always a symplectic space of the form (4.2). Speciﬁcally, in the case we are considering,
the space P is the total space of the cotangent bundle over the moduli spa ce,M, of ﬂat
SU (2) connections on Σ. Let ωσ denote the natural symplectic structure on P = T ∗M,
and let θσ be the corresponding canonical 1-form, such that ωσ =dθσ . Then, the physical
considerations suggest that
θσ|L = 1
2dVol(M ) (4 .4)
34
should hold for arbitrary M (along with a similar expression for the Chern-Simons invar iant
of M ). Furthermore, the 1-form θσ should be exact, when restricted to the Lagrangian
submanifold֒P , ∮
C
θσ = 0 , ∀C∈π1(L)
There is a similar set of constraints that follows from the ra tionality of the periods of θk,
cf. (3.29). Altogether, these conditions assert that L is a quantizable submanifold and
impose severe restrictions on its geometry, especially whe n π1(L) is large.
For example, these constraints lead to some non-trivial obs tructions to a polynomial
arising as the A-polynomial of a knot. Namely, if Σ = T 2 and L is described by the zero
locus of the A-polynomial, from (3.29) we ﬁnd that the integr al of the 1-form θσ around
any closed loop C on the curve L must vanish,∮
C
log|l|d(argm)− log|m|d(argl) = 0 (4 .5)
and, furthermore, that the integral of the 1-form θk must be a rational number,
1
π2
∮
C
log|m|d log|l| + (argl)d(argm)∈ Q (4 .6)
In particular, this gives the answer to a question posed by Co oper and Long in [53,54]:
“Which aﬃne curves L in C∗× C∗ satisfy the condition that θσ is exact on L?” Namely,
the 1-form θσ should be interpreted as an “imaginary part” of the Lioville form (3.26),
and then the condition (4.5) is simply the condition for L to be a quantizable Lagrangian
submanifold in C∗× C∗. This suggests a further relationship to symplectic geomet ry. The
ﬁrst of the above conditions can be understood as a consequen ce of the Sch¨ aﬂi-like formula
(3.30), and has a number of applications, see e.g. [53]. To the best of our knowledge, the
second condition has not been discussed in the mathematical literature.
Example.
Following [53], let us demonstrate how the condition (4.5) c an be used to constrain
the form of the A-polynomial. For example, in Table 2 one ﬁnds the A-polynomial of
the ﬁgure-eight knot:
A(l, m) = −2 + m4 + m−4 − m2 − m−2 − l − l−1
A slight modiﬁcation of this polynomial gives
f (l, m) = −2 + m6 + m−6 − m2 − m−2 − l − l−1
which is not the A-polynomial of any knot since the 1-form θσ has non-vanishing periods
on f (l, m) = 0, therefore, violating (4.5). However, f (l, m) does exhibit every other
property of the A-polynomial. It would be interesting to inv ent similar examples which
satisfy the ﬁrst condition (4.5), but fail (4.6).
35
Notice, that the genus of the curve A(l,m ) = 0 grows very rapidly with the complexity
of the knot. (One can get a general impression, say, by lookin g at the examples listed in
Table 2.) Therefore, the number of non-trivial constraints in (4.5) and (4.6) also becomes
very large, especially for polynomials of large degree. In f act, one might wonder if these
constraints, together with the ones mentioned in section 2. 3, give a complete list:
Question: Is every integral, reciprocal, and tempered polynomial f (l,m ) that satisﬁes
both conditions (4.5) and (4.6) is the A-polynomial of some k not?
