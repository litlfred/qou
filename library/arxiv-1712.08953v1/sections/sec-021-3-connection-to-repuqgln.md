---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-021-3-connection-to-repuqgln
section_title: "Connection to RepUq(gln)"
section_number: 3
pages: 16-18
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
---
In this section, we assume until the ﬁnal proof that k is a ﬁeld of characteristic
0, q ∈ k × is not a root of unity, and z = q− q−1. Fix n ∈ N and let Uq(gln)
be the usual quantized enveloping algebra over k ; we include the possibility that
n = 0 by interpreting Uq(gl0) as k . We denote the standard generators of Uq(gln)
by
{
ei,fi,d±
j | 1≤i<n, 1≤j≤n
}
. This is a well-known object, so the reader should
have no trouble surmising the relations on being told that the usual d iagonal gen-
erator ki of Uq(sln) is did−1
i+1. We have the natural Uq(gln)-module V + on basis{
v+
i | 1≤i≤n
}
and the dual natural module V− on basis
{
v−
i | 1≤i≤n
}
. The
actions of the generators on these bases are given by the following formulae:
fiv+
j =δi,jv+
i+1, e iv+
j =δi+1,jv+
i , d iv+
j =qδi,jv+
j ,
fiv−
j =δi+1,jv−
i , e iv−
j =δi,jv−
i+1, d iv−
j =q−δi,jv−
j .
We use the comultiplication ∆ : Uq(gln)→Uq(gln)⊗Uq(gln) deﬁned from
∆( fi) = 1⊗fi +fi⊗did−1
i+1, ∆( ei) = d−1
i di+1⊗ei +ei⊗ 1, ∆( di) = di⊗di.
The corresponding antipode is given by S( ei) = −did−1
i+1ei, S(fi) = −fid−1
i di+1 and
S(di) = d−1
i ; for the user of [L] we note that Lusztig’s v and Ki are our q−1 and
k−1
i =d−1
i di+1.
Let RepUq(gln) be the category of ﬁnite-dimensional Uq(gln)-modules that are iso-
morphic to ﬁnite direct sums of summands of the modules obtained by taking tensor
products of V + and V−; in the trivial case n = 0, we mean the category of ﬁnite-
dimensional vector spaces. In general, Rep Uq(gln) is the usual category of ﬁnite-
dimensional representations of Uq(gln) that are semisimple of type 1 over its diagonal
subalgebra. It is well known that Rep Uq(gln) is a ribbon category, but we do not
want to ﬁx a ribbon structure yet. Instead, we are going to use Th eorem 1.1 classify
monoidal functors Φ : OS (z,t )→ RepUq(gln) that take ↑ to V + and↓ to V−.
There is a unique (up to scalars) non-degenerate bilinear pairing
⟨·,·⟩ :V +×V−→ k
satisfying⟨uv+,v−⟩ =⟨v+, S(u)v−⟩. Since there is freedom to rescale the basis vectors
v−
j by a global scalar, we may assume this is given explicitly by the formula ⟨v+
i ,v−
j⟩ :=
(−1)iq−iδi,j. The associated evaluation and coevaluation maps will be denoted
ev : V +⊗V−→ k , v +
i ⊗v−
j ↦→(−1)iq−iδi,j, (3.1)
coev : k →V−⊗V +, 1↦→
n∑
j=1
(−1)jqjv−
j ⊗v+
j . (3.2)
Then if we deﬁne Φ( C) := coev and Φ( D) := ev, where C = and D = , the
relation (3) from Theorem 1.1 is satisﬁed.
Next we choose a candidate for the image of S = . This should be an isomorphism
V +⊗V + ∼
→ V +⊗V + satisfying the relations (1) and (2) from Theorem 1.1. One
possible choice is to take Ψ( S) := R where
R(v+
i ⊗v+
j ) :=



v+
j ⊗v+
i if i<j,
qv+
j ⊗v+
i if i =j,
v+
j ⊗v−
i + (q−q−1)v+
i ⊗v+
j if i>j.
(3.3)
This formula is the R-matrix from [L, §32.1.4]. The only other possibility for us
would be to take Ψ( S) := −R−1, but there is no loss in generality in choosing the
former, since one can twist with the isomorphism # : OS (z,t )
∼
→OS (z,t−1) from
ORIENTED SKEIN CATEGORY 17
(2.12) which switches S and−S−1. To see that −R−1 is indeed the only other option,
recall that endomorphism algebra of V +⊗V + is two-dimensional, so any isomorphism
V +⊗V + → V +⊗V + takes the form aR +b for scalars a and b. Then a simple
computation shows there are only two choices for these scalars wh ich satisfy the relation
(1): a = 1,b = 0 or a =−1,b =q−q−1.
Using the relation (4), we can determine the image of T = , as follows. We want
to have Ψ( T−1) = (1V −⊗ 1V +⊗ ev)◦ (1V −⊗R⊗ 1V − )◦ (coev⊗1V +⊗ 1V −). Computing
the right hand side explicitly gives that
Ψ(T−1)(v+
i ⊗v−
j ) =



v−
j ⊗v+
i if i⁄=j,
qv−
i ⊗v+
i + (q−q−1)
n∑
k=j+1
(−q)k−iv−
k ⊗v+
k if i =j;
Inverting this map then gives us Ψ( T ):
Ψ(T )(v−
i ⊗v+
j ) =



v+
j ⊗v−
i if i⁄=j,
q−1v+
i ⊗v−
i − (q−q−1)
n∑
k=i+1
(−q)i−kv+
k ⊗v−
k if i =j.
Now the relation (4) holds.
The images under Ψ of C′ = and D′ = must come from another non-
degenerate pairing
⟨·,·⟩′ :V−×V +→ k
such that ⟨uv−,v +⟩′ =⟨v−, S(u)v+⟩′. There is a unique (up to scalars) such pair-
ing, namely, ⟨v−
i ,v +
j⟩′ := ε(−1)iqi−n−1δi,j for ε∈ k ×. We denote the corresponding
evaluation and coevaluation maps by
ev′ :V−⊗V +→ k , v −
i ⊗v+
j ↦→ε(−1)iqi−n−1δi,j, (3.4)
coev′ : k →V +⊗V−, 1↦→ε−1
n∑
j=1
(−1)jqn+1−jv+
j ⊗v−
j . (3.5)
Then, for some choice of ε, we have that Φ( C′) = coev ′ and Φ( D′) = ev ′. To de-
termine the possibilities for ε, from the ﬁrst equation in (2.5), we know that ev ′ =
t ev◦Ψ(T ). Applying this equation to the vector v−
n⊗v+
n quickly produces the equa-
tion ε(−1)nq−1 = tq−1(−1)nq−n, hence, t = εqn. From the second equation in (2.5),
we know that coev ′ = tΨ(T )◦ coev. Looking at the v+
1 ⊗v−
1 -coeﬃcient of the im-
age of 1 under the two sides of this equation gives −ε−1qn =−t, hence, t = ε−1qn.
We deduce that ε = ε−1, i.e., ε =±1. Since we can twist with the isomorphism
π :OS (z,t )
∼
→OS (z,−t) from (2.11) which takes C′ to−C′ and D′ to−D′, we are
reduced without loss of generality to the case that ε = +1 and t =qn. It can then be
checked that (2.5) holds fully.
Finally, we have that coev ◦ ev′ = [n]q, so that relation (5) from Theorem 1.1 holds
too, and the theorem implies that the functor Ψ is well deﬁned. We ha ve proved the
following lemma, a version of which was used already in [T2].
Lemma 3.1. Assume k is of characteristic zero, z =q−q−1 for generic q∈ k ×, and
t = qn for n∈ N. There is a k -linear monoidal functor Ψ : OS (z,t )→ RepUq(gln)
sending↑↦→V +,↓↦→V−, the positive upward crossing to the R-matrix from (3.3),
the rightward cap and rightward cup to the maps ev and coev from (3.1)–(3.2), and
the leftward cap and leftward cup to the maps ev′ and coev′ from (3.4)–(3.5) taking
ε = +1.
