---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-006-13-asymptotics-in-the-bulk-of-the-spectrum-given
section_title: "Asymptotics in the bulk of the spectrum. Given a sequence"
section_number: 1.3
pages: 6-8
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
of subsets
X(n) = {x1(n) < · · · < x s(n)} ⊂ Z ,
where s = |X(n)| is some ﬁxed integer, we call this sequence regular if
the following limits
ai = lim
n→∞
xi(n)
√n ,(1.10)
dij = lim
n→∞
(xi(n) − xj(n)) ,(1.11)
exist, ﬁnite or inﬁnite. Here i, j = 1, . . . , s. Observe that if dij is ﬁnite
then dij = xi(n) − xj(n) for n ≫ 0.
In the case when X(n) can be represented as X(n) = X ′(n) ∪ X ′′(n)
and the distance between X ′(n) and X ′′(n) goes to ∞ as n → ∞
we shall say that the sequence splits; otherwise, we call it nonsplit.
Obviously, X(n) is nonsplit if and only if all xi(n) stay at a ﬁnite
distance from each other.
Deﬁne the correlation functions ̺(n, · ) of the measures Mn by the
same rule as in (1.4)
̺(n, X) = Mn ({λ | X ⊂ D(λ)}) .
We are interested in the limit of ̺(n, X(n)) as n → ∞. This limit will
be computed in Theorem 3 below. As we shall see, if X(n) splits, then
the limit correlations factor accordingly.
Introduce the following discrete sine kernel which is a translation
invariant kernel on the lattice Z
S(k, l; a) = S(k − l, a) , k, l ∈ Z ,
depending on a real parameter a:
S(k, a) = sin(arccos(a/2) k)
πk
=
√
4 − a2
2π
Uk−1(a/2)
k , k ∈ Z .
ASYMPTOTICS OF PLANCHEREL MEASURES 7
Here Uk is the Tchebyshev polynomials of the second kind. We agree
that
S(0, a) = arccos(a/2)
π , S(∞, a) = 0
and also that
S(k, a) =
{
0 , a ≥ 2 or a ≤ 2 and k ⁄= 0 ,
1 , a ≤ 2 and k = 0 .
The following result describes the local structure of a Plan cherel
typical partition.
Theorem 3. Let X(n) ⊂ Z be a regular sequence and let the numbers
ai, dij be deﬁned by (1.10), (1.11). If X(n) splits, that is, if X(n) =
X ′(n) ∪ X ′′(n) and the distance between X ′(n) and X ′′(n) goes to ∞
as n → ∞ then
lim
n→∞
̺(n, X(n)) = lim
n→∞
̺(n, X′(n)) · lim
n→∞
̺(n, X′′(n)) .(1.12)
If X(n) is nonsplit then
lim
n→∞
̺ (n, X(n)) = det
[
S(dij, a)
]
1≤i,j ≤s
,(1.13)
where S is the discrete sine kernel and a = a1 = a2 = . . ..
We prove this theorem in Section 3.
Remark 1.4. Notice that, in particular, Theorem 3 implies that, as
n → ∞ , the shape of a typical partition λ near any point of the limit
curve Ω is described by a stationary random process. For dist inct
points on the curve Ω these random processes are independent .
Remark 1.5. By complementation, see Section A.3 and 3.2, one ob-
tains from Theorem 3 an equivalent statement about the asymp totics
of the following correlation functions
ρ(n, X) = Mn ({λ | X ⊂ Fr(λ)}) .
Remark 1.6. The discrete sine kernel was studied before, see [40, 41],
mainly as a model case for the continuous sine kernel. In part icular, the
asymptotics of Toeplitz determinants built from the discre te sign kernel
was obtained by H. Widom in [41] answering a question of F. Dys on. As
pointed out by S. Kerov, this asymptotics has interesting co nsequences
for the Plancherel measures.
