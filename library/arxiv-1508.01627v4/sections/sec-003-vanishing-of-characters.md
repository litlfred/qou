---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-003-vanishing-of-characters
section_title: "Vanishing of characters"
section_number: 4
pages: 9-14
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
In this section we prove Theorem 1 for quasi-simple groups of classical type. So let G be a simplyconnected simple algebraic group of type Bn with n ≥ 3, Cn with n ≥ 2 or Dn with n ≥ 4, and let
F be a Steinberg morphism of G (we exclude the 3D4 case) with G = G(q) := GF . We consider
the corresponding finite groups G = Spin2n+1 (q) only for odd q, and Sp2n (q) and Spin±
2n (q) for any q,
respectively.
We consider primes ℓ such that the Sylow ℓ-subgroups of G are not cyclic. We will show that for such
ℓ with only very few exceptions all ordinary irreducible characters of G vanish on some ℓ-singular regular
semisimple element.
If we write d := dℓ (q) for the order of q modulo ℓ as in Section 2.2 and then n = ad + r, 0 ≤ r < d,
for odd d respectively n = ae + r, 0 ≤ r < e, for even d = 2e, then our assumption on ℓ implies a ≥ 2
because the cyclotomic polynomial Φd (q) must divide the order of G(q) at least twice. If G is of type
2
Dn we have n > 2d for odd d and n > 2e for even d = 2e (see the order formula in [13, Tab. 24.1]).
4.1. Non-unipotent characters. We first deal with non-unipotent characters, and afterwards examine
in more detail the unipotent characters.
Theorem 4.1. Let G be one of the groups Spin2n+1 (q) for odd q and n ≥ 3, Sp2n (q) for any q and
n ≥ 2, or Spin±
2n (q) for any q and n ≥ 4. Let 2 6= ℓ6 |q be a prime such that the Sylow ℓ-subgroups of G
are non-cyclic. Then any non-unipotent irreducible complex character of G vanishes on some ℓ-singular
regular semisimple element, except for the two cases G = C2 (2) = Sp4 (2) and G = C4 (2) = Sp8 (2).
The group Sp4 (2) ∼
= S6 contains no 3-singular regular semisimple elements. It has three non-trivial

irreducible characters which do not vanish on any 3-singular class, the unipotent character 012
and the
−
two characters of degree 10 (belonging to Lusztig series of type A1 (q) × (q + 1)).
The group Sp8 (2) has only one 5-singular regular semisimple class and there are 15 irreducible characters which do not vanish on this class. There is only
one non-trivial character which does not vanish

on any 5-singular class, the unipotent character 01
.
4

Proof. We use the following facts from Deligne–Lusztig theory. The irreducible characters of G are
partitioned into Lusztig series which are parameterised by semisimple conjugacy classes of the dual group
G∗ . If s ∈ G∗ is semisimple then the values of characters in the Lusztig series of s on semisimple
elements t ∈ G are linear combinations of values of Deligne–Lusztig characters on t which belong to types
of tori which occur in the connected centraliser of s in G∗ . In particular Deligne–Lusztig characters
corresponding to a maximal torus T of G vanish on regular semisimple classes which do not intersect T ,
see e.g. [11, Prop. 6.4].
Since G is simply-connected the dual group G∗ has trivial center so that non-unipotent characters are
in Lusztig series of non-central elements.
We show the theorem by listing in each case a set of types of maximal tori which contain regular ℓsingular elements by Lemma 2.1 and which cannot all occur in any proper centraliser. We have described
these subgroups together with the types of tori they contain in Lemma 2.3. Note that for G of type Bn
the dual group is of type Cn (we need to apply Lemma 2.3 for type Cn and consider tori with regular
elements in type Bn ); the same remark holds with Bn and Cn interchanged.
Let d = dℓ (q) and write n = ad + r with 0 ≤ r < d for odd d and n = ae + r with 0 ≤ r < e for even
d = 2e, a ≥ 2, as explained above.
Recall that for odd d a torus of type (λ, µ) contains ℓ-singular elements if and only if some part of λ
is a positive multiple of d. For even d = 2e a torus of type (λ, µ) contains ℓ-singular elements if and only
if µ contains an odd multiple of e or λ contains an even multiple of e.
We collect the tori we consider in Table 4.1.
A few additional remarks are in order. In the two cases marked with (∗ ) in the table we need to rule out
the possibility that the given tori all lie in a subgroup of type Dd +Dn−d or De +Dn−e , respectively. Such


10

FRANK LÜBECK AND GUNTER MALLE

Table 1. Tori needed in the proof of Theorem 4.1
type
Cn ,Bn
Cn ,Bn
Dn
Dn

d
odd
odd
odd
odd

2

Dn (∗ )
Dn
Cn ,Bn
Cn ,Bn
Cn ,Bn
Cn ,Bn
Dn

odd any
0
odd any > 0
= 2e even
0
= 2e even > 0
= 2e odd
0
= 2e odd > 0
= 2e even
0

Dn
Dn (∗ )

= 2e even > 0
= 2e odd
0

Dn
2
Dn
2
Dn
2
Dn
2
Dn

= 2e odd > 0
= 2e even
0
= 2e even > 0
= 2e odd
0
= 2e odd > 0

2

a
any
any
any
any

r
0
>0
0
>0

tori
((n), −), ((n − d), (d)), and ((n − d), (1, d − 1)) if d > 1
((n − r), (r)), ((n − r − d), (d + r)), ((n − r − d), (d + r − 1, 1))
((n), −), ((n − 1, 1), −) if d = 1, or ((n − d), (d − 1, 1)) if d > 1
((n − d − r, d + r), −), ((n − r, r), −) if r 6= 2, or ((n − 2), (1, 1)) if
r=2
((n − d), (d)), ((d), (n − d)), ((n − d − 1, d), (1)) if d > 1
((n − r), (r)), ((n − d − r), (d + r)), ((n − d − r, 1), (d + r − 1))
((n), −), ((n − e), (e)), (−, (n − e − 1, e, 1)) if e > 1
((n − r), (r)), (−, (n − e, e)), (−, (n − e − 1, e, 1)) if r 6= 1
(−, (n)), (−, (n − e, e)), ((n − e − 1), (e, 1)) if e > 1
(−, (n − r, r)), ((n − r − e), (r + e)), ((n − r − e), (r + e − 1, 1))
((n), −), ((n − e − 1), (e, 1)) if (n, e) ∈
/ {(4, 1), (6, 3)}, or ((n − e −
2), (e, 2)) otherwise
(−, (n − e, e)), ((n − 1, 1), −) if r = 1, ((n − r), (r − 1, 1)) if r > 1
(−, (n − e, e)), (−, (n − 2e, 2e)), ((1), (n − 2e, 2e − 1)) if e > 1,
((2e), (e − 1, 1) if n = 3e
(−, (n − r, r)), (−, (n − e, e)), ((1), (n − r, r − 1)) if r > 1
((n − e), (e)), ((n − 2e), (2e)), ((n − 2e, 2e − 1), (1)) if e > 1
((n − r), (r)), ((n − e), (e)), ((n − r, 1), (r − 1)) if r > 1
(−, (n)), ((n − e), (e)), ((n − e, 1), (e − 1)) if e > 1
((n − e − r), (e + r)), (−, (n − r, r − 1, 1)) if r > 1, ((1), (n − 1)) if
r=1

a subgroup stabilises a decomposition of the orthogonal space on which G acts into two non-degenerate
subspaces. In the first case one of these subspaces must be of minus- and the other of plus-type. So the
corresponding finite subgroups are of type 2Dd + D2d or Dd + 2D2d , each of these only contains one of
the types of tori, ((d), (n − d)) or ((n − d), (d)). The argument for the second case is similar, there both
subspaces must be of minus-type or both of plus-type.
It remains to check for which groups one of the tori given in Table 4.1 does not contain regular elements.
Note that for q = 3 we have d > 2 because ℓ 6= 2, and for q = 2 we have d > 1. Furthermore, when
r > 0, we have d ≥ 3 or e ≥ 2, respectively. This implies that only the following cases need an extra
consideration:
C2 (2) with e = 1: this is the first exception mentioned in the statement.
B4 (q) with q = 3 and e = 2: We compute that for q = 3 the torus of type ((1), (1, 2)) contains regular
element. So, we can argue with tori of types ((4), −) and ((1), (1, 2)).
C4 (q) with q = 3 and e = 2: In this case the torus of type ((2), (2)) in C4 (3) contains regular elements.
Here we can argue with tori of types ((4), −) and ((2), (2)) by checking that the dual group (adjoint of
type B4 (3)) does not contain a semisimple element whose centraliser contains tori of both types.
For C4 (2) and e = 2 (and so ℓ = 5) only tori of type ((4), −) contain ℓ-singular regular elements. This
leads to the second exception mentioned in the statement.
2
D4 (2) with e = 1: Here, the maximal tori containing ℓ-elements all have conjugates inside a subgroup
of type D1 + D3 . We can apply the argument from above: the tori of types ((1), (3)) and ((3), (1)) cannot
both occur in the same rational form of such a subgroup.

4.2. Unipotent characters. In the following theorem we use symbols to describe unipotent characters
and refer to Section 3.2 for the notation.


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

11

Theorem 4.2. Let G be one of the groups Spin2n+1 (q) for odd q and n ≥ 3, Sp2n (q) for any q and
n ≥ 2, or Spin±
2n (q) for any q and n ≥ 4. Let 2 6= ℓ6 |q be a prime such that the Sylow ℓ-subgroups of G
are non-cyclic.
Let ρS be a unipotent character of G for some symbol S and assume that ρS does not vanish on any
regular semisimple ℓ-singular class. Then either ρS is the trivial character, or the Steinberg character, or
up to Alvis-Curtis duality we are in one of the following cases (as before we set d = dℓ (q), and interpret
−1 as the empty set):
(1) G = Sp2n (q) or Spin2n+1 (q), d is odd, n = 2d + r with 0 ≤ r < d and


d − r − 1 \ 0 ∪ d ∪ 2d
S=
;
d−r−1
(2) G = Sp2n (q) or Spin2n+1 (q), d = 2e is even, n = 2e + r with 0 ≤ r < e and


e−r−1∪e
S=
;
e − r − 1 \ 0 ∪ 2e
(3) G = Spin+
2n (q), d is odd, n = 2d + r with 0 ≤ r < d and


d − r − 1 \ 0 ∪ d ∪ 2d
;
S=
d−r
(4) G = Spin+
2n (q), d = 2e is even, n = 2e + r with 0 ≤ r ≤ e and


e−r−1∪e
;
S=
e − r \ 0 ∪ 2e
(5) G = Spin−
2n (q), d is odd, n = 2d + r with 0 < r ≤ d and


d − r \ 0 ∪ d ∪ 2d
;
S=
d−r−1
(6) G = Spin−
2n (q), d = 2e is even, n = 2e + r with 0 < r < e and


e−r∪e
;
S=
e − r − 1 \ 0 ∪ 2e


1 2
(7) G = Sp4 (2), d = 2 and S = 0 −
or 012 (there is no regular semisimple ℓ-singular element);

1 3
(8) G = Sp6 (2), d = 2 and S = 0 −
;


(9) G = Sp8 (2), d = 4 and S = 041 or 104 ; or

1 3
(10) G = Spin−
8 (2), d = 2, 4 and S = − .
Conversely, all characters listed above take non-zero valueson all regular semisimple ℓ-singular classes.
1 3
More precisely, in cases G = Spin−
the character ρS has value 2 on classes of
8 (2), d = 2, 4, S =
−
type (−, (2, 1, 1)). In all other cases the character values are ±1.
Proof. (a) Our strategy is to use Corollary 3.4 of the Murnaghan–Nakayama formula. We consider
maximal tori with ℓ-singular regular elements which are parameterised by pairs of partitions with very
few parts. For example, if for a symbol S the character ρS has non-zero value on regular elements in a
torus of type ((λ1 ), (µ1 )) then the Murnaghan-Nakayama formula implies that we can remove a λ1 -hook
from S and that the resulting symbol has a µ1 -cohook which after removing leaves a symbol of rank 0.
(b) For groups of type Bn and Cn we need to consider symbols of rank n with odd defect. First note
that there is only one symbol of rank 0 with odd defect, namely the defect 1 symbol

  
0
n
=
n−1
−


12

FRANK LÜBECK AND GUNTER MALLE

(apply the shift operation n times). We will write all symbols with 2n + 1 entries, because this way we
can construct all symbols of rank n by adding hooks or cohooks starting from the rank 0 symbol without
the need of further shift operations. Also, we will write all symbols of non-zero defect such that the larger
number of entries is in the first row.

for n + 1 − t ≤ k ≤ n and their dual
The symbols of rank t ≤ n which have a t-hook are n\k∪k+t
n−1

n
symbols n−1\k∪k+t for n − t ≤ k ≤ n − 1.
To find up to duality all symbols S of rank n which have an (n − t)-cohook c such that S \ c has a
t-hook, it is sufficient to take the first set of symbols of rank t with a t-hook and to add an (n − t)-cohook
in all possible ways (filling the gap k, creating new entries in the first or the second row or moving the
k + t entry). We get:


n∪l+n
(1 ≤ l ≤ t),
n−1\l


n\k∪k+t∪l+n−t
(n − t < k ≤ n, t < l < n, k − l 6= n − 2t),
n−1\l


n−1∪l+n−t
(n − t < k ≤ n, t ≤ l ≤ n, k 6= l),
n\k\l∪k+t


n−1∪k+n
(n − t < k ≤ n).
n\k
(c) We now prove the theorem for the case Bn , Cn for n ≥ 3 and odd d. Write n = ad + r with
0 ≤ r < d. Note that for q = 2 or 3 we have d > 1 (since ℓ 6= 2). In our argument we will use maximal
tori which by Lemma 2.1 contain regular ℓ-singular elements.
First assume r = 0 and let S be a symbol of rank n such that ρS is non-zero on all regular semisimple
ℓ-singular classes. Then as a torus of type ((n), −) contains ℓ-singular elements, S has an n-hook, that is
(up to duality) one of


n\k∪k+n
S=
(1 ≤ k ≤ n).
n−1
Tori of type ((d), (n − d)) also contain ℓ-singular regular elements. Therefore S must have a d-hook h
and an (n − d)-cohook such that S \ h still has an (n
 − d)-cohook. This is only the case for k = n and
k = n − d. For k = n we obtain the symbol n−1∪2n
of the trivial character. For k = n − d we get the
n−1
symbol


n \ n − d ∪ 2n − d
S=
.
n−1
If a > 2 then this symbol has no (a − 1)d = (n − d)-hook, hence ρS is zero on regular elements in tori
of type ((n − d), (d)). For a = 2 we get one of the symbols shown in part (1) of the statement (after
applying the inverse shift operation n − d times).
Now let r > 0 (and so d ≥ 3). We consider tori of types ((ad), (r)) = ((n − r), (r)) and ((d, n − d), −).
Here we check for every symbol S listed in (b) (for t = n − r) if it has an (n − r)-hook and if we can
get the rank 0 symbol by removing a d-hook and an (n − d)-hook in both possible orders. Note that the
last condition implies that S has defect one because removing hooks does not change the defect. These
conditions yield in all cases relations between the parameters k and l and then determine k. The only
possible symbols which remain are those of the trivial character and


n
S=
.
n\d\n−r∪n+d−r


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

13

If a > 2 this has no (a − 1)d-hook and so ρS is zero on regular elements in tori of type (((a − 1)d), (d + r)).

and applying the inverse
For a = 2 the dual of S is given in statement (1), that is n−1\n−d+r∪n+r∪n+d+r
n−1
shift operation n − d + r times.
(d) The argument for type Bn , Cn , n ≥ 7, and even d = 2e, n = ae + r, is very similar. Pairs of
partitions corresponding to tori with ℓ-singular regular elements must now have an odd multiple of e in
the second part or an even multiple of e in the first part. Therefore we distinguish the cases of even and
odd a and of r = 0 and r > 0. We just list the types of tori which we consider in the given order such
that the arguments from (c) work with slight modifications.
a even, r = 0: ((n), −) and ((n − e), (e)), and for a > 2 also ((n − 2e), (2e)).
a even, r > 0: ((n − r), (r)), (−, (n − e, e)) and ((n − e), (e)), and for a > 2 also (−, ((a − 1)e, e + r)).
a odd, r = 0: ((n − e), (e)), (−, (n)) and (−, (n − e, e)), and finally to rule out a symbol of defect 3
also ((n − e, e), −) (if a ≤ 3) or ((n − 3e), (3e)) (if a > 3).
a odd, r > 0: ((n − r − e), (e + r)), (−, (n − r, r)) and ((n − e), (e)).
(e) The cases of type Dn and 2Dn can also be discussed
with very similar arguments. The only symbol
n−1
and
so all the symbols of rank n with an n-hook
of rank 0 and even defect has defect 0 and is −
=
−
n−1
are


n−1\k∪k+n
S=
(0 ≤ k ≤ n).
n−1
Here it is sufficient to consider the cases with k ≥ (n−1)/2 in the further arguments because the remaining
ones are the duals of these.
(f) Type Dn , n ≥ 7. We list again which tori we consider in the various cases.
d odd, r = 0: ((n), −) and in case d = 1 we use ((n − 1, 1), −) and for d ≥ 3 we use ((n − d), (d − 1, 1)).
For a > 2 we also need ((n − 2d), (2d − 1, 1)) to rule out one possibility.
d odd, r > 0: ((n − d, d), −) and ((n − r, r), −) if r 6= 2 or ((n − 2), (1, 1)) if r = 2, ((d), (n − d − 1, 1)).
d = 2e even, n = ae, a even: ((n), −) and (−, (n − 1, 1)) if e = 1 or ((n − e − 1), (e, 1)) if e > 1. For
a > 2 we also use ((n − 2e), (2e − 1, 1)).
d = 2e even, n = ae + r, a even, r > 0: (−, (n − e, e)), ((n − e − 1), (e, 1)) and ((n − r, r), −) if r 6= 2
or ((n − 2), (1, 1)) if r = 2. For a > 2 we also need ((2e), (n − 2e − 1, 1)).
d = 2e even, n = ae, a odd: (−, (n − e, e)) and ((n − e, e), −) if e 6= 2 or ((n − 2), (1, 1)) if e = 2.
Finally, use ((n − 3e, 3e), −) if a > 3. For a = 3 we get the exception listed in (4) for the parameter r = e
(that is n = 2e + r = 3e).
d = 2e even, n = ae + r, a odd, r > 0: (−, (n − e, e)), (−, (n − r, r)), ((n − e − 1), (e, 1)) and
((2e), (n − 2e − 1, 1)).
(g) Type 2Dn , n ≥ 7. We list again which tori we consider in the various cases.
d odd, n = ad: Recall that in this case we have a ≥ 3. We use ((n − d), (d)) and ((n − 2d), (2d)).
For a > 3 we also use ((n − 3d), (d)) and for a = 3 we get the exception listed in (5) for r = d (that is
n = 2d + r = 3r).
d odd, n = ad + r, r > 0 (and so d ≥ 3): ((n − r), (r)), ((d), (n − d)) and ((d, 1), (n − d − 1)). And for
a > 2 also ((2d), (n − 2d)). For a = 2 this leads to the other exceptions listed in (5).
d = 2e even, n = ae, a even: Recall that in this case we have a ≥ 4. We use ((n−e), (e)), ((n−2e), (2e))
and one of ((3), (n − 3)) (if e = 1) or ((n − 3e), (3e)) (if e > 1) or (−, (6, 1, 1)) (if n = 8).
d = 2e even, n = ae + r, a even, r > 0 (so e > 1): ((n − e), (e)) and ((n − r), (r)). For a > 2 we also
use ((2e), (n − 2e)). For a = 2 this leads to the exceptions listed in (6).
d = 2e even, n = ae, a odd: (−, (n)), ((n − e), (e)) and ((n − e − 1, 1), (e)).
d = 2e even, n = ae + r, a odd, r > 0: ((n − e), (e)), ((n − e − r), (e + r)) and ((2e), (n − 2e)). Finally
also ((r), (n − r)) if r 6= 2 or (−, (n − 2, 1, 1)) for r = 2.


14

FRANK LÜBECK AND GUNTER MALLE

(h) For small rank n ≤ 6 we compute the number of regular elements in all tori, and determine the
values of unipotent characters on all ℓ-singular regular semisimple classes via the Murnaghan-Nakayama
formula in Theorem 3.3. This yields the extra cases in statements (7) to (10).
(i) The symbols given in statements (1) to (6) each contain a unique d-hook and a unique 2d-hook (or
a unique e-cohook and unique 2e-hook, respectively). Removing these we always get the symbol of the
trivial representation of the appropriate rank (and the Steinberg representation for the dual symbols).
Therefore, the Murnaghan-Nakayama formula shows that the values on all regular semisimple ℓ-singular
elements are ±1.

