---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-059-20-privileged-cocycles
section_title: "Privileged cocycles"
section_number: 20
pages: 105-107
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
In ”applications”, it is sometimes desirable to have explicit cocycles to
work with instead of cohomology classes. We shall now describe cocycles with
nice properties, that can be explicitly computed from a matrix in standard
form. Most of the proofs of what follows are consequences of theorem 5.5.3.
However, they can also be obtained through the more elementary approach
of [50], which we shall brieﬂy summarize here in subsection 6.1.1.
Fix A0 as in (3.1) page 36 and let M0 be the corresponding pure module.
All notations that follow are relative to this A0 and M0. Recall from section
1.3 at the end of the introduction the notations a ∈Eq for the class of a ∈C∗
and [a; q] := aqZ for the corresponding q-spiral. Also recall from paragraph
1.3.1 the function θq, holomorphic over C∗with simple zeroes on [−1; q] and
satisfying the functional equation σqθq = zθq.
6.1.1. “Algebraic summation”. — To construct cocycles encoding the
analytic class of A ∈GLn(C({z})), we use “meromorphic sums” of ˆFA. These
can be obtained either by the summation process of theorem 5.5.3, or by the
100
CHAPTER 6. GEOMETRY OF THE SPACE OF CLASSES
“algebraic summation process” of [50]. We now summarize this process. We
restrict to the case of divisors supported by a point, since it is suﬃcient for
classiﬁcation.
Let A as in (3.2) (we do not assume from start that it is in Birkhoﬀ-
Guenther normal form). We want to solve the equation σqF = AFA−1
0
with
F ∈GA0 meromorphic in some punctured neighborhood of 0 in C∗. Since
A, A0, A−1, A−1
0
are all holomorphic in some punctured neighborhood of 0 in
C∗, the singular locus (1) of F near 0 is invariant under q−N: it is therefore
a ﬁnite union of germs of half q-spirals aq−N (the ﬁniteness ﬂows from the
meromorphy of F). If we take A in Birkhoﬀ-Guenther normal form (deﬁnition
3.3.6), the functional equation σqF = AFA−1
0
actually allows us to extend F
to a meromorphic matrix on the whole of C∗and its singular locus is a ﬁnite
union of discrete logarithmic q-spirals [a; q].
To illustrate the process, we start with an example.
Example 6.1.1. — Setting Au :=
z−1
z−1u
0
1

, with u ∈C({z}), and
F =
1
f
0
1

, we saw that Au = F[A0] ⇐⇒zσqf −f = u.
This admits
a unique formal solution ˆf, which can be computed by iterating the z-adically
contracting operator f 7→−u+zσqf. If A is in Birkhoﬀ-Guenther normal form,
u ∈C and ˆf = −u Q (the Tshakaloﬀseries). We want f to be meromorphic
on some punctured neighborhood of 0 in C∗, which we write f ∈M(C∗, 0),
and to have (in germ) half q-spirals of poles. For simplicity, we shall assume
that u is holomorphic on C∗, so that f will have to be meromorphic on the
whole of C∗with complete q-spirals of poles. We set θq,c(z) := θq(z/c), which
is holomorphic on C∗, with simple zeroes on the q-spiral [−c; q] and satisﬁes
the functional equation σqθq,c = (z/c)θq,c. We look for f with simple poles
on [−c; q] by writing it f = g/θq,c and looking for g holomorphic on C∗and
satisfying the functional equation:
zσq(g/θq,c) −(g/θq,c) = u ⇐⇒cσqg −g = uθq,c
⇐⇒∀n ∈Z , (cqn −1)gn = [uθq,c]n,
1. In the context of q-diﬀerence equations, the singular locus of a matrix of functions P
is made of the poles of P as well as those of P −1. For a unipotent matrix, like F, these are
all poles of F since F −1 is a polynomial in F.
