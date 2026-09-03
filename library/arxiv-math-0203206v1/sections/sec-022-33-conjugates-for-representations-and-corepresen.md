---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-022-33-conjugates-for-representations-and-corepresen
section_title: "Conjugates for Representations and Corepresentations"
section_number: 3.3
pages: 17-19
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
Suppose that (A, ∆) is a discrete aqg with counit ε and coinverse S. We now show that the semisimple tensor
∗-categories Repf (A, ∆) and Corep f ( ˆA, ˆ∆) have conjugates, and provide a conjugate object for every n on-zero
object.
Suppose π is a non-zero non-degenerate ∗-representation on the ﬁnite dimensional Hilbert space K. Let
f ∈ M (A) be as in Theorem 2.12 and consider the positive operator π(f −1) ∈ B(K). Pick any Hilbert space
K and any invertible antilinear operator J :K →K such that J ∗J =π(f −1). This can clearly be done. Now
pick an orthonormal basis ( ei) for K and deﬁne linear maps r : C →K ⊗K and r : C →K ⊗K by
r(1) =
∑
i
Jei ⊗ei and r(1) =
∑
i
ei ⊗J ∗−1ei,
respectively. Next deﬁne
π : A →B(K), a ↦→JπS (a∗)J −1.
As J and J −1 both are antilinear, π(a) is linear and thus π(a) ∈ B(K) for all a ∈ A. By the following
proposition, π is indeed a conjugate to π andr and r are normalized solutions of the conjugate equations for π
and π.
Proposition 3.21 Let (A, ∆) be a discrete aqg and π a non-zero object of Repf (A, ∆) . Then π is a non-zero
object of Repf (A, ∆) . Moreover, the following hold:
1. r ∈ Hom(ε,π ×π),
17
2. r ∈ Hom(ε,π ×π),
3. r∗ ⊗ idπ ◦ idπ ⊗r = idπ,
4. r∗ ⊗ idπ ◦ idπ ⊗r = idπ,
5. r∗ ◦ r =r∗ ◦ r.
Proof. Claims 3 and 4 hold for any invertible antilinear map J, as is easily veriﬁed. Claim 5 is simply a
restatement of the fact Trπ(f ) = Trπ(f −1) stated in Theorem 2.12. To show that π ∈ Repf (A, ∆), we ﬁrst note
that π is linear (as AdJ and ∗ are both antilinear), multiplicative and non-degenerate, thus non- zero. To see
that π is ∗-preserving, ﬁrst notice that S(a∗)∗ =S−1(a) and S2(a) = faf −1 for all a ∈A, and then calculate
π(a)∗ =J ∗−1πS −1(a)J ∗ =Jπ (f )πS −1(a)π(f −1)J −1 =JπS (a)J −1 =π(a∗),
for all a ∈A.
It remains to show relations 1 and 2. We prove only the ﬁrst, the sec ond being proved similarly. Now
r ∈ Hom(ε,π ×π) simply means that ε(a)r(1) = (π ×π)(a)r(1), for all a ∈A. By the non-degeneracy of π it
thus suﬃces to show that
(ε(a)r(1),J ∗−1ej ⊗π(b∗)el) = ((π ×π)(a)r(1),J ∗−1ej ⊗π(b∗)el)
for all a,b ∈A and all j,l . On the l.h.s. we have
(ε(a)r(1),J ∗−1ej ⊗π(b∗)el) = ε(a)
∑
i
(Jei,J ∗−1ej)(ei,π (b∗)el)
=ε(a)
∑
i
δij(ei,π (b∗)el) = ε(a)(ej,π (b∗)el) = (π(ε(a)b)ej,el).
To see that the r.h.s. coincides with this expression, ﬁrst write (1 ⊗b)∆( a) =∑
kak ⊗bk and notice that
∑
k
bkS(a∗
k)∗ =
∑
k
bkS−1(ak) = m(ι ⊗S−1)(
∑
k
bk ⊗ak) = m(ι ⊗S−1)((b ⊗ 1)∆ op(a)) = ε(a)b.
Hence
((
π ×π)(a)r(1),J ∗−1ej ⊗π(b∗)el) =
∑
i
((π ⊗π)∆( a)(Jei ⊗ei),J ∗−1ej ⊗π(b∗)el)
=
∑
i
((π ⊗π)(1 ⊗b)(π ⊗π)∆( a)(Jei ⊗ei),J ∗−1ej ⊗el)
=
∑
i
((π ⊗π)((1 ⊗b)∆( a))(Jei ⊗ei),J ∗−1ej ⊗el)
=
∑
ik
(π(ak)Jei ⊗π(bk)ei,J ∗−1ej ⊗el) =
∑
ik
(JπS (a∗
k)ei ⊗π(bk)ei,J ∗−1ej ⊗el)
=
∑
ik
(JπS (a∗
k)ei,J ∗−1ej)(π(bk)ei,el) =
∑
ik
(ej,πS (a∗
k)ei)(π(bk)ei,el)
=
∑
ik
(πS(a∗
k)∗ej,ei)(π(bk)ei,el) =
∑
k
(π(bk)
∑
i
(πS(a∗
k)∗ej,ei)ei,el)
=
∑
k
(π(bk)πS(a∗
k)∗ej,el) = (π(
∑
k
bkS(a∗
k)∗)ej,el) = (π(ε(a)b)ej,el),
as desired. ■
18
Note that for a discrete aqg ( A, ∆), the intrinsic dimension d(π) of an irreducible object π ∈ Repf (A, ∆) is
then given by
d(π) = r∗ ◦ r =r∗ ◦ r = Trπ(f ) = Trπ(f −1).
In fact, the latter two expressions can be thought of as the quan tum dimension of π [30] and gives the intrinsic
dimension for any π ∈ Repf (A, ∆). By the Schwarz inequality for the inner product given by Tr it follo ws that
if d(π) equals the dimension of the Hilbert space on which π acts, then π(f ) = 1. Thus the von Neumann
extension of (A, ∆) is a Kac algebra iﬀ the intrinsic dimension of any ﬁnite dimensional rep resentation coincides
with the dimension of the Hilbert space on which it acts.
Suppose now that (A, ∆) is a compact agq with counit ε and coinverseS. We would like to ﬁnd an expression
for the conjugate unitary corepresentation V of a non-zero object V ∈ Corepf (A, ∆). To this end, we will use
the correspondence between Rep f ( ˆA, ˆ∆) and Corep f (A, ∆) established in Theorem 3.14. Recall that the dual
( ˆA, ˆ∆) of ( A, ∆) is a discrete aqg. Let ˆ ε denote its counit, ˆS its coinverse, and let ˆf ∈M ( ˆA) be as in Theorem
2.12.
LetV ∈A ⊗B(K) be a non-zero unitary corepresentation of ( A, ∆) on a ﬁnite dimensional Hilbert space K.
Pick a ﬁnite dimensional Hilbert space K and a antilinear map J :K →K such that J ∗J =πV ( ˆf −1) ∈B(K).
Given any invertible antilinear map J we deﬁne a linear map j : B(K) → B(K) by j(x) = Jx ∗J −1, for all
x ∈B(K).
Proposition 3.22 Suppose (A, ∆) is a compact aqg. Let V be a unitary corepresentation of (A, ∆) on a ﬁnite
dimensional Hilbert space K with J ∗J =πV ( ˆf −1) ∈B(K). Deﬁne V ∈A ⊗B(K) by V = (S−1 ⊗j)V . Then
the following hold:
