---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-020-9-recovering-a-representation-from-its-ptolemy-c
section_title: "Recovering a representation from its Ptolemy coordinates"
section_number: 9
pages: 26-34
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
We now show that a Ptolemy assignment on K determines a generically decorated boundary-
unipotent representation, which is given explicitly in ter ms of the Ptolemy coordinates. The idea is
that a Ptolemy assignment canonically determines a (G, N)-cocycle on M .
Deﬁnition 9.1. An n × n matrix A is counter diagonal if the only non-zero entries of A are on the
lower left to upper right diagonal, i.e. Aij = 0 unless j = n − i + 1. If Aij = 0 for j > n − i + 1
(resp. j < n − i + 1), A is upper (resp. lower ) counter triangular.
Given subsets I, J of {1, . . . , n}, let AI,J denote the submatrix of A whose rows and columns are
indexed by I and J, respectively. If |I| = |J|, let |A|I,J denote the minor det(AI,J ). Let I c denote
{1, . . . , n} \ I.
Recall that the adjugate Adj(A) of a matrix A is the matrix whose ijth entry is (−1)i+j|A|{j}c,{i}c.
It is well known that Adj(A) = det( A)A−1. The following result by Jacobi (see e.g. [ 1, Section 42])
expresses the minors of Adj(A) in terms of the minors of A.
Lemma 9.2. Let I, J be subsets of {1, . . . , n} with |I| = |J| = r. We have
(9.1) |Adj(A)|I,J = (−1)
∑ (I,J ) det(A)r−1|A|J c,I c,
where∑ (I, J ) is the sum of the indices occurring in I and J. □
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 27
Deﬁnition 9.3. A matrix A ∈ GLn(C) is generic if |A|{k,...,n},{1,...,n−k+1} ⁄= 0 for all k ∈ {1, . . . , n}.
Note that A is generic if and only if the Ptolemy coordinates of (N, AN ) are non-zero. The
following is a generalization of Zickert [ 30, Lemma 3.5].
Proposition 9.4. Let A ∈ GLn(C) be generic. There exist unique x ∈ N and y ∈ N such that
q = x−1Ay is counter diagonal. The entries of x, y and q are given by
qn,1 = An,1, q n−j+1,j = (−1)j−1 |A|{n−j+1,...,n},{1,...,j}
|A|{n−j+2,...,n},{1,...,j−1}
for 1 < j ≤ n(9.2)
xij =
|A|{i,j+1,...,n},{1,...,n−j+1}
|A|{j,...,n},{1,...,n−j+1}
for j > i(9.3)
yij = (−1)i+j |A|{n−j+2,...,n},{1,...,ˆi,...,j}
|A|{n−j+2,...,n},{1,...,j−1}
for j > i.(9.4)
Proof. It is enough to prove existence and uniqueness of x and y in N such that Ay and x−1A are
upper and lower counter triangular, respectively. Suppose Ay is upper counter triangular. Then
the vector y{1,...,j−1},{j} consisting of the part above the counter diagonal of the jth column vector
of y must satisfy
(9.5) A{n−j+2,...,n},{1,...,j−1}y{1,...,j−1},{j} + A{n−j+2,...,n},{j} = 0.
The existence and uniqueness of y, as well as the given formula for the entries, now follow from
Cramer’s rule. Since x−1A is lower counter-triangular if and only if A−1x is upper counter-triangular,
existence and uniqueness of x follows. The explicit formula for the entries follows from J acobi’s
identity ( 9.1) and the formula for the entries of y. To obtain the formula for the entries of q, note
that qn−j+1,j = (Ay)n−j+1,j. Hence, qn,1 = An,1, and for 1 < j ≤ n,
qn−j+1,j =
j−1∑
i=1
An−j+1,iyi,j + An−j+1,j
=
∑ j
i=1(−1)i+jAn−j+1,i|A|{n−j+2,...,n},{1,...ˆi,...,j}
|A|{n−j+2,...,n},{1,...,j−1}
= (−1)j−1 |A|{n−j+1,...,n},{1,...,j}
|A|{n−j+2,...,n},{1,...,j−1}
,
where the second equality follows from ( 9.4). □
For a generic matrix A, let xA, yA and qA be the unique matrices provided by Proposition 9.4.
Given cosets giN , gjN , gkN , deﬁne
(9.6) qij = qg− 1
i gj
, α i
jk = (xg− 1
i gj
)−1xg− 1
i gk
.
Corollary 9.5. The diagonal left G-action on C gen
k (G/N) is free when k ≥ 1, and the chain complex
C gen
∗≥1(G/N) ⊗Z[G] Z computes relative homology.
Proof. By Proposition 9.4, every generic tuple (g0N, . . . , gkN ) may be uniquely written as
(9.7) g0xg− 1
0 g1(N, q01N, α0
12q02N, . . . , α0
1kq0kN ).
28 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
This proves that the G-action is free. Also note that for each generic tuple (g0N, . . . , gkN ), there
exists a coset gN such that (gN, g0N, . . . , gkN ) is generic. Hence, C gen
∗≥1(G/N) is acyclic, and is thus a
free resolution of Ker(C0(G/N) → Z). This proves the result (see e.g. Zickert [ 30, Theorem 2.1]). □
A generic tuple (g0N, . . . , gkN ) determines a (G, N)-cocycle on a truncated simplex ∆ , by labeling
the long edges by qij and the short edges by αi
jk (see Figure 5). In particular, a generically decorated
representation ρ determines a (G, N)-cocycle representing ρ.
0
1
2
3
q02
q01 q12 q23
q13
q03
α0
12
α0
13
α0
23
α1
02
α1
23α1
03
α2
01
α2
13
α2
03
α3
01
α3
02
α3
12
Figure 5. A (G, N)-cocycle on a truncated 3-simplex.
A (G, N)-cocycle τ coming from a generic tuple is called generic. Letting B
gen
∗ (G, N) be the
subcomplex of B∗(G, N) generated by generic cocycles on a standard simplex, it foll ows that we
have a canonical isomorphism
(9.8) B
gen
∗ (G, N) = C gen
∗ (G/N) ⊗Z[G] Z.
It now follows from Proposition 4.7, that the fundamental class can be represented as in ( 4.3).
We wish to prove that a generic (G, N)-cocycle is uniquely determined by the Ptolemy coordi-
nates.
Notation 9.6. Let k ∈ {1, . . . , n− 1}.
(i) For a1, . . . , an ∈ C∗, let q(a1, . . . , an) be the counter-diagonal matrix whose entries on the
counter-diagonal (from lower left to upper right) are a1, . . . , an.
(ii) For x ∈ C, let xk(x) be the elementary matrix whose (k, k + 1) entry is x.
(iii) For b1, . . . , bk ∈ C, let πk(b1, . . . , bk) = x1(b1)x2(b2) · · · xk(bk).
Proposition 9.7. The long edges of a generic (G, N)-cocycle are determined by the Ptolemy
coordinates as follows:
(9.9) qij = q(a1, . . . , an), a k = (−1)k−1 c(n−k)ei+kej
c(n−k+1)ei+(k−1)ej
.
Proof. Let (g0N, . . . , gkN ) be a generic tuple, and let A = g−1
i gj. Then qij = qA. Since
(9.10) |A|{n−j+1,...,n},{1,j} = det({gi}n−k, {gj }k) = c(n−k)ei+kej ,
the result follows from ( 9.2). □
The corresponding formula for the short edges requires cons iderable more work, and is given in
Proposition 9.12 below.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 29
Lemma 9.8. Let A be generic, and let L = x−1
A A. The entries Li,n−i+2 right below the counter
diagonal are given by
(9.11) Li,n−i+2 = (−1)n−i |A|{i,...,n},{1,..., ˆn−i+1,n−i+2}
|A|{i+1,...,n},{1,...,n−i}
.
Proof. We proceed as in the proof of Proposition 9.4. Let x = x−1
A . Since L is lower counter-
triangular, we must have
(9.12) x{i},{i+1,...,n}A{i+1,...,n},{1,...,n−i} + A{i},{1,...,n−i} = 0,
so by Cramer’s rule,
(9.13) xij = (−1)i+j |A|{i,...,ˆj,...,n},{1,...,n−i}
|A|{i+1,...,n},{1,...,n−i}
for j > i.
We thus have
|A|{i+1,...,n},{1,...,n−i}Li,n−i+2 = Ai,n−i+2|A|{i+1,...,n},{1,...,n−i}
+
n∑
k=i+i
(−1)i+k|A|{j,...,ˆk,...,n},{1,...,n−j}Ak,n−i+2
=
n∑
k=j
(−1)i+k|A|{j,...,ˆk,...,n},{1,...,n−i}Ak,n−i+2
= (−1)n−i|A|{i,...,n},{1,..., ˆn−i+1,...,n−i+2},
which proves the result. □
Deﬁnition 9.9. Let A, B ∈ GL(n, C).
(i) A and B are related by a type 0 move if all but the last column of A and B are equal.
(ii) A and B are related by a type 1 move if all but the second last column of A and B are equal.
(iii) A and B are related by a type 2 move if for some j < n − 1, B is obtained from A by switching
columns j and j + 1.
Proposition 9.10. Let A and B be generic, and let Ai and Bi denote the ith column of A, resp. B.
(i) If A and B are related by a type 0 move, xB = xA.
(ii) If A and B are related by a type 1 move, xB = xAx1(x), where
(9.14) x = − det(A1, . . . , An−1, Bn−1) det(e1, e2, A1, . . . , An−2)
det(e1, A1, . . . , An−1) det(e1, A1, . . . , An−2, Bn−1) .
(iii) If A and B are related by a type 2 move switching columns j and j + 1, xB = xAxn−j(x),
where
(9.15) x = − det(e1, . . . , en−j−1, A1, . . . , Aj+1) det(e1, . . . , en−j+1, A1, . . . , Aj−1)
det(e1, . . . , en−j, A1, . . . , Aj) det(e1, . . . , en−j, A1, . . . , Aj−1, Bj) .
Proof. The ﬁrst statement follows from the fact that xA is independent of the last column of A.
Suppose A and B are related by a type 1 move. Using ( 9.3), one sees that (xA)ij = ( xB)ij except
when i = 1 and j = 2 . It thus follows that xB = xAx1(x), where x = ( xB)12 − (xA)12. Letting C
be the matrix obtained from A by replacing the nth column by the (n − 1)th column of B, one has
|A|{1,3,...,n},{1,...,n−1} = Adj(C)n,2, |B|{1,3,...,n},{1,...,n−1} = Adj(C)n−1,2,
|A|{2,...,n},{1,...,n−1} = Adj(C)n,1, |B|{2,...,n},{1,...,n−1} = Adj(C)n−1,1,
30 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
and it follows from ( 9.3) that
(9.16) x = (xB)12 − (xA)12 = Adj(C)n−1,2
Adj(C)n−1,1
− Adj(C)n,2
Adj(C)n,1
.
We then have
x Adj(C)n,1 Adj(C)n−1,1 = Adj(C)n−1,2 Adj(C)n,1 − Adj(C)n−1,1 Adj(C)n,2
= −|Adj(C)|{n−1,n},{1,2}
= − det(C)|C|{3,...,n},{1,...,n−2}
= − det(A1, . . . , An−1, Bn−1) det(e1, e2, A1, . . . , An−2),
where the third equality follows from Jacobi’s identity ( 9.1). Since
Adj(C)n,1 Adj(C)n−1,1 = det(e1, A1, . . . , An−1) det(e1, A1, . . . , An−2, Bn−1),
this proves the second statement.
Now suppose A and B are related by a type 2 move. Let Ej,j+1 be the elementary matrix
obtained from the identity matrix by switching the jth and (j + 1)th columns. Then B = AEj,j+1.
Since L = x−1
A A is lower counter triangular, xn−j(− Ln− j,j+1
Ln− j+1,j+1
)LEj,j+1 must also be lower counter
triangular. We thus have
(9.17) xB = xAxn−j(− Ln−j,j+1
Ln−j+1,j+1
)−1 = xAxn−j( Ln−j,j+1
Ln−j+1,j+1
).
By ( 9.11) and ( 9.2), we have
(9.18)
Ln−j+1,j+1 = (−1)j−1 |A|{n−j+1,...,n},{1,...,ˆj,j +1}
|A|{n−j+2,...,n},{1,...,j−1}
Ln−j,j+1 = (−1)j |A|{n−j,...,n},{1,...,j+1}
|A|{n−j+1,...,n},{1,...,j}
.
Hence,
Ln−j,j+1
Ln−j+1,j+1
= −
|A|{n−j,...,n},{1,...,j+1}|A|{n−j+2,...,n},{1,...,j−1}
|A|{n−j+1,...,n},{1,...,j}|A|{n−j+1,...,n},{1,...,ˆj,j +1}
= − det(e1, . . . , en−j−1, A1, . . . , Aj+1) det(e1, . . . , en−j+1, A1, . . . , Aj−1)
det(e1, . . . , en−j, A1, . . . , Aj ) det(e1, . . . , en−j, A1, . . . , Aj−1, Bj) ,
proving the third statement. □
Note that any two matrices A, B ∈ GL(n, C) are related by a sequence of moves of type 1, 2 and
0 as follows:
(9.19)
A 1− →[A1, . . . , An−2, B1, An] 2− →[A1, . . . , An−3, B1, An−2, An] 2− →. . . 2− →
[B1, A1, . . . , An−2, An] 1− →[B1, A1, . . . , An−3, B2, An] 2− →. . . 2− →
[B1, B2, A1, . . . , An−3, An]
1,2
− − →. . .
1,2
− − →[B1, . . . , Bn−1, An] 0− →B.
Consider the tilings of a face ijk, i < j < k , of ∆ 2
n by diamonds shown in Figure 6. We refer to
the diamonds as being of type i, j and k, respectively.
Deﬁnition 9.11. The diamond coordinate dk
r,s of a diamond (r, s) of type k is the alternating
product of the Ptolemy coordinates assigned to its vertices , see Figure 6.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 31
i
j
k
(1, 1)
(1, n − 1)
(1, 2) (2 , 1)
(r, s)
(n − 1, 1)
b
c
d
a
i
j
k
(1, 1)
(1, n − 1)
(1, 2)
(2, 1)
(r, s)
(n − 1, 1)
b
c d
a
i
j
k
(1, 1) (1 , n − 1)(1, 2)
(2, 1)
(r, s)
(n − 1, 1)
bc
da
Figure 6. Diamonds of type i, j and k. The diamond coordinates are di
r,s = dk
r,s = −ab
cd ,
and dj
r,s = ab
cd , where a, b, c, and d are Ptolemy coordinates.
Proposition 9.12. The short edges αi
jk , j < k , of a generic (G, N)-cocycle are determined by the
Ptolemy coordinates as follows:
(9.20) αi
jk = πn−1(di
1,1, . . . , di
1,n−1)πn−2(di
2,1, . . . , di
2,n−2) · · · π1(di
n−1,1),
where the di
j,k’s are the type i diamond coordinates on the face ijk.
Proof. Let (g0N, . . . , glN ) be a generic tuple, and let A = g−1
i gj and B = g−1
i gk. We assume that
i < j < k , the other cases being similar. Note that the Ptolemy coordi nates on the ijk face are
given by
(9.21) ctiei+tj ek+tkek = det(e1, . . . , eti , A1, . . . , Atj , B1, . . . , Btk ).
Performing the sequence of moves in ( 9.19), the result follows from Proposition 9.10. □
Corollary 9.13. A generic tuple is determined up to the diagonal G-action by its Ptolemy coordi-
nates. □
This result together with Proposition 9.7 shows that there is at most one generic (G, N)-cocycle
with a given collection of Ptolemy coordinates. We now prove that the Ptolemy relations are the
only relations among the Ptolemy coordinates when k ≤ 3.
Example 9.14. Suppose Ptolemy assignments on ∆ 2
n, n ∈ { 2, 3}, are given as in Figure 7. Us-
ing ( 9.9) and ( 9.20), we obtain that the corresponding (G, N)-cocycle is given by
(9.22)
q01 = q(a, −1/a), q 12 = q(b, −1/b), q 02 = q(c, −1/c),
α0
12 = x1
( −b
ac
)
, α 1
02 = x1
( c
ab
)
, α 2
01 = x1
( −a
cb
)
when n = 2, and
(9.23)
q01 = q(c, −a/c, 1/a), q 12 − q(b, −e/b, 1/e), q 02 = q(f, −g/f, 1/g),
α1
02 = x1
( f a
cd
)
x2
( d
ab
)
x1
( gb
de
)
,
α0
12 = x1
( −bc
ad
)
x2
( −d
cf
)
x1
( −ef
dg
)
, α 2
01 = x1
( −cg
f d
)
x2
( −d
ge
)
x1
( −ae
db
)
when n = 3.
32 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
0
1
2
a b
c
0
1
2
a b
c d e
f g
0
1
2
q01 q12
q02
α0
12 α0
12
α1
02
Figure 7. Ptolemy assignments and the corresponding cocycle for n = 2 and n = 3.
Lemma 9.15. Let ai,j and bi,j be non-zero complex numbers. The equality
(9.24) πn−1(a1,1, . . . , a1,n−1) · · · π1(an−1,1) = πn−1(b1,1, . . . , b1,n−1) · · · π1(bn−1,1)
holds if and only if ai,j = bi,j for all i, j.
Proof. For any ci,j, the nth column of πn−1(c1,1, . . . , c1,n−1) · · ·π1(cn−1,1) is equal to the nth column
of πn−1(c1,1, . . . , c1,n−1), which equals
(
n−1∏
i=1
c1,i,
n−1∏
i=2
c1,i, . . . , c1,n−1).
This proves that a1,j = b1,j for all j. The result now follows by induction. □
Proposition 9.16. For any assignment c : ˙∆ 2
n(Z) → C∗, there is a unique Ptolemy assignment
c ∈ P tn
2 whose Ptolemy coordinates are ct.
Proof. We prove that the Ptolemy coordinates c′
t of (N, q01N, α0
12q02N ) equal ct, where q01, q02 and
α0
12 are given in terms of the ct’s by ( 9.9) and ( 9.20). First note that ct = c′
t if either t1 or t2 is 0,
i.e. if t is on one of the edges of ∆ 2
n containing the 0th vertex. Each of the other integral points t
is the upper right vertex of a unique diamond (r, s) of type 0. Let τk be the upper right vertex of
the kth diamond Dk in the sequence
(9.25) (1, n − 1), (1, n − 2), . . .(1, 1), (2, n − 2), . . . ,(2, 1), . . . ,(n − 1, 1).
By Lemma 9.15, d0′
r,s = d0
r,s for all diamonds (r, s) of type 0. It thus follows that if ct = c′
t for all
but one of the vertices of a diamond D, then ct = c′
t for all vertices of D. In particular c′
τ1 = cτ1 .
Suppose by induction that c′
τi = cτi for all i < k . Then c′
t = ct, for all vertices of Dk except τk.
Hence, we also have c′
τk = cτk , completing the induction. □
Proposition 9.17. For any assignment c :
dot∆ 3
n(Z) → C∗ satisfying the Ptolemy relations, there is a unique Ptolemy assignment c ∈ P tn
3
whose Ptolemy coordinates are ct.
Proof. Let c′
t be the Ptolemy coordinates of the tuple (N, q01N, α0
12q02N, α0
13q03N ) deﬁned from the
ct’s by ( 9.9) and ( 9.20). We wish to prove that c′
t = ct for all t. Note that if, for some subsimplex
∆ 3(α), c′
αij = cαij for all but one of the 6 αij’s, then c′
αij = cαij holds for all αij. This is a direct
consequence of the Ptolemy relations. By Proposition 9.16, c′
t = ct, when either t2 or t3 is zero.
Hence, for each α = (a0, a1, a2, a3) with a2 = a3 = 0, c′
αij = cαij except possibly when (i, j) = (2 , 3).
As explained above, c′
α23 = cα23 as well. Now suppose by induction that c′
αij = cαij for all α with
a2 + a3 < k . Then c′
αij = cαij holds except possibly when (i, j) = (2 , 3). Again, c′
α23 = cα23 must
also hold, completing the induction. □
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 33
A (G, N)-cocycle on M obviously determines a decorated representation (up to con jugation).
The main results of this section can thus be summarized by the diagram below.
(9.26)
{
Points in Pn(K)
}
/d111/d111 /d47/d47
{
Generic (G, N)-cocycles
on M
}
/d111/d111 /d47/d47
{
Generically decorated
(G, N)-representations
}
Remark 9.18. We stress that the Ptolemy variety parametrizes decorated r epresentations and not
decorated representations up to equivalence. In particula r, the dimension of P (K) depends on the
triangulation, and may be very large if K has many interior vertices.
9.1. Obstruction cocycles and the p SL(n, C)-Ptolemy varieties. Suppose n is even. The
projection G → pG maps N isomorphically onto its image (also denoted by N ), and by elementary
obstruction theory (see e.g. Steenrod [ 24]), the obstruction to lifting a (pG, N)-representation ρ to
a (G, N)-representation is a class in
(9.27) H 2(M, ∂M ; Z/2Z) = H 2(K; Z/2Z).
We can represent it by an explicit cocycle in Z 2(K; Z/2Z) as follows: Pick any (p SL(n, C), N)-
cocycle ¯τ on M representing ρ and a lift τ of ¯τ to a (G, N)-cochain. Each 2-cell of K corresponds
to a hexagonal 2-cell of M , and the 2-cocycle σ ∈ Z 2(K; Z/2Z) taking a 2-cell to the product of the
τ -labelings along the corresponding hexagonal 2-cell of M represents the obstruction class.
Proposition 9.19. Suppose the interior of M is a 1-cusped hyperbolic 3-manifold with ﬁnite
volume. The obstruction class in H 2(K; Z/2Z) to lifting the geometric representation is non-trivial.
Proof. By a result of Calegari [ 5, Corollary 2.4], any lift of the geometric representation t akes a
longitude to an element in SL(2, C) with trace −2. This shows that no lift is boundary-unipotent,
so the obstruction class must be non-trivial. □
Proposition 9.4 also holds in p SL(n, C), and we thus have a 1-1 correspondence between generi-
cally decorated representations and (pG, N)-cocycles on M .
Deﬁnition 9.20. Let σ ∈ Z 2(K; Z/2Z). A lifted (pG, N) cocycle on M with obstruction cocycle
σ is a generic (G, N)-assignment on M lifting a (pG, N)-cocycle on M such that the 2-cocycle on
K obtained by taking products along hexagonal faces of M equals σ.
A 1-cochain η ∈ C 1(K; Z/2Z) acts on a lifted (pG, N)-cocycle τ by multiplying a long edge
e by η(e). Note that if τ has obstruction cocycle σ, ητ has obstruction cocycle δ(η)σ, where δ
is the standard coboundary operator. Recall that there is a 1-1 correspondence between generic
(G, N)-cocycles on M and points in the Ptolemy-variety. We shall prove a similar r esult for pG.
We wish to deﬁne a coboundary action on pG-Ptolemy assignments (see Deﬁnition 5.11). Let c
be a pG-Ptolemy assignment on ∆ , and let ηij ∈ C 1(∆; Z/2Z) be the cochain taking the edge ij to
−1 and all other edges to 1. Deﬁne
(9.28) ηijc : ˙∆ 3
n(Z) → C∗, (ηijc)t = (−1)titj ct
and extend in the natural way to deﬁne ηc for a pG-Ptolemy assignment c on K and η ∈ C 1(K; Z/2Z).
A priori ηc is only an assignment of complex numbers to the integral poin ts of the simplices of K.
However, we have:
Lemma 9.21. If c is a pG-Ptolemy assignment on K with obstruction cocycle σ, ηc is a pG-Ptolemy
assignment on K with obstruction cocycle δ(η)σ.
34 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
Proof. It is enough to prove this for a simplex ∆ and for η = ηij. Let c′ = ηijc. We assume for
simplicity that ij = 01; the other cases are proved similarly. For any α = (a0, a1, a2, a3) ∈ ∆ k
n−2(Z),
we then have
(9.29) c′
α03 c′
α12 + c′
α01c′
α23 − c′
α02 c′
α13 = (−1)a0+a1(cα03 cα12 − cα01 cα23 − cα02 cα13 )
Let τ = δ(η01). Since δ(η01)2 = δ(η01)3 = −1 and δ(η01)0 = 1, ( 9.29) implies that
(9.30) τ2τ3c′
α03 c′
α12 + τ0τ3c′
α03 c′
α01 c′
α23 = c′
α02 c′
α13,
as desired. □
Deﬁnition 9.22. The diamond coordinates of a p SL(n, C)-Ptolemy assignment with obstruction
cocycle σ are deﬁned as in Deﬁnition 9.11, but multiplied by the sign (provided by σ) of the face.
Note that for η ∈ C 1(K; Z/2/Z), the diamond coordinates of c and ηc are identical.
Proposition 9.23. For any σ ∈ Z 2(K; Z/2Z), there is a 1-1 correspondence between p SL(n, C)-
Ptolemy assignments on K with obstruction cocycle σ, and lifted (p SL(n, C), N)-cocycles on M
with obstruction cocycle σ. The correspondence preserves the coboundary actions.
Proof. It is enough to prove this for a simplex ∆ . For a pG-Ptolemy assignment c on ∆ with
obstruction cocycle σ ∈ Z 2(∆; Z/2Z), deﬁne a cochain τ on ∆ by the formulas ( 9.9) and ( 9.20)
using the σ-modiﬁed diamond coordinates (Deﬁnition 9.22). Let η ∈ C 1(∆; Z/2Z) be such that
δη = σ, where δ is the standard coboundary map. By Lemma 9.21 ηc satisﬁes the SL(n, C) Ptolemy
relations (5.4), and hence corresponds to an (SL(n, C), N)-cocycle τ ′. Since the diamond coordinates
of c and ηc are the same, the short edges of τ ′ agree with those of τ and the long edges diﬀer from
those of τ by η. This proves that τ is a lifted (pG, N)-cocycle with obstruction cocycle σ. The
inductive arguments of Propositions 9.16 and 9.17 show that this is a 1-1 correspondence. The fact
that the actions by coboundaries correspond is immediate fr om the construction. □
Corollary 9.24. Let σ ∈ Z 2(K; Z/2Z). There is an algebraic variety P σ
n (K) of generically deco-
rated boundary-unipotent representations ρ : π1(M ) → p SL(n, C) whose obstruction class to lifting
to SL(n, C) is represented by σ. Up to canonical isomorphism, the variety P σ
n (K) only depends on
the cohomology class of σ.
Proof. This follows immediately from Proposition 9.23. □
Note that the canonical isomorphisms in Corollary 9.24 respect the extended Bloch group element.
This follows from the pG variant of Proposition 7.7. The analogue of ( 9.26) is
(9.31)
{
Points in P σ
n (K)
}
/d111/d111 /d47/d47
{
Lifted (pG, N)-cocycles on M
with obstruction cocycle σ
}
k:1 /d47/d47 /d47/d47



Generically decorated
(pG, N)-representations
with obstruction cocycle σ


 ,
where k is the number of lifts, i.e. k = |Z 1(K; Z/2Z)|.
