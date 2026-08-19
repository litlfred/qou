---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-002-2-combinatorial-and-analytic-torsions
section_title: "Combinatorial and analytic torsions"
section_number: 2
pages: 4-6
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
This section overviews the deﬁnition and main properties of combinat orial tor-
sion, as they are used later in some proofs. It also recalls brieﬂy the deﬁnition
of analytic torsion, as it is used in many relevant results.
2.1 Combinatorial torsion
For a detailed deﬁnition of combinatorial torsion see [95, 65, 59, 80 ]. This section
follows mainly [82], in particular its convention with the power (−1)i+1 instead
of (−1)i for the alternated product. (See Remark 2.2 on this convention.) T he
deﬁnition is given for chain and for cochain complexes, in a way that bo th
homology and cohomology give the same deﬁnition of the torsion of a m anifold.
2.1.1 T orsion of a chain complex
Let F be a ﬁeld and C∗ = (C∗, ∂) a chain complex of ﬁnite dimensional F -vector
spaces:
Cd
∂
/leftrightline → Cd−1
∂
/leftrightline → ⋯
∂
/leftrightline → C0.
The subspaces of boundaries and cycles are denoted by Bi = Im(Ci+1
∂
/leftrightline → Ci) and
Zi = ker(Ci
∂
/leftrightline → Ci−1) respectively, the homology is denoted by by Hi = Zi/sl⊗sh.leftBi.
Assume
ci = {ci,1, . . . , ci,ji }
is an F -basis for Ci and
hi = {hi,1, . . . , hi,ri },
is a basis for Hi, if nonzero. For the deﬁnition of torsion, a basis
bi = {bi,1, . . . , bi,ri}
for Bi is also required. Using the exact sequences:
0 → Zi → Ci
∂
/leftrightline → Bi−1 → 0 (1)
0 → Bi → Zi → Hi → 0, (2)
lift bi−1 to ˜bi−1 ⊂Ci in (1) and hi to ˜hi ⊂Zi ⊂Ci in (2) and construct a new
basis for Ci:
bi ⊔ ˜bi−1 ⊔ ˜hi, (3)
4
where ⊔ denotes the disjoint union. The bases are compared with the deter -
minant of the corresponding matrix. Given two bases α = {α1, . . . , αr} and
β = {β1, . . . , βr} for F r, if (ηij) ∈Mn(F ) is the matrix that relates the bases,
i.e. if αi = ∑j ηijβj, set
[α, β] = det(ηij) ∈F ∗. (4)
Deﬁnition 2.1. The torsion of the chain complex C∗ with bases {ci} and bases
{hi} for Hi is:
tor(C∗, {ci}, {hi}) =
d
/product.disp
i=0
[bi ⊔ ˜bi−1 ⊔ ˜
hi, ci](−1)i+1
∈F ∗/slash.l⟩ft{±1}. (5)
As it is an alternated product, it is easy to see that it does not depen d on
the choice of bi, the basis for Bi, and it is also straightforward that it does not
depend on the lifts ˜bi−1 and ˜hi.
Remark 2.2. In the alternated product deﬁning the torsion of a complex (5),
may authors use (−1)i instead of (−1)i+1. Deﬁnition 2.1 follows the convention of
[96, 97, 95, 67, 53] for instance, but opposite to [65, 21] and all pa pers on analytic
torsion [13, 71] and quantum invariants [102, 3, 24, 37, 20, 44, 76, 19, 81, 23]. I
followed this convention in [82] but not in [63]. This convention is better suited
for polynomials, also for functions on the deformation space; the o pposite one
is more useful for the interpretation of the torsion as a volume for m.
We follow a diﬀerent deﬁnition for the torsion of a cocomplex, which giv es
a nonstandard statement of Lemma 2.4 (in the standard version it is corrected
by a power (−1)n).
There is a formula of change of bases. For diﬀerent choices c′
i and h′
i of bases
for Ci and Hi we have
tor(C∗, {c′
i}, {h′
i})
tor(C∗, {ci}, {hi}) =
d
/product.disp
i=0
/par⟩nl⟩ft.alt4[c′
i, ci]
[h′
i, hi] /par⟩nright.alt4
(−1)i
. (6)
The proof is straightforward, see [65, 82, 80] for details.
Deﬁnition 2.3. Let C∗ = (C∗, δ) be a cochain complex with bases {ci}, and
cohomology bases {hi}, by constructing the bi in a similar way, its torsion is
deﬁned as
tor(C∗, {ci}, {hi}) =
d
/product.disp
i=0
[bi ⊔ ˜bi−1 ⊔ ˜hi, ci](−1)i
∈F ∗/slash.l⟩ft{±1}. (7)
The convention of powers (−1)i and (−1)i+1 has been changed in this deﬁ-
nition, for the purpose of Lemma 2.4.
Lemma 2.4. Let (Ci)⋆ = homF (Ci, F) be the dual cocomplex, with coboundary
δ ∶ C⋆
i → C⋆
i−1 deﬁned by δ(θ) = θ ○ d. If (hi)⋆ is dual to hi, then
tor(C∗, {hi}) = tor((C∗)⋆, {(hi)⋆}).
Notice that this lemma uses Deﬁnition 2.3 of a cochain complex. If inste ad of
the cocomplex one considers the dual complex, one must re-index t he dimension
i by d−i, then the torsion of the complex is replaced by its (−1)d+1-power! Then,
one may see [30, 67] for a proof with this version of Lemma 2.4.
5
