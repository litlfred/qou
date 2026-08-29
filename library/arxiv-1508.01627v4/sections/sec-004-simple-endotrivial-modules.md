---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-004-simple-endotrivial-modules
section_title: "Simple endotrivial modules"
section_number: 5
pages: 14-17
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
In this section we prove Theorem 2 on the classification of simple endotrivial modules for finite classical
groups. Note that the case of linear and unitary groups has already been treated in [10], so we only need
to consider symplectic groups and spin groups as in the previous section.
5.1. On certain unipotent characters. We first rule out some candidate characters. Let Φd ∈ Z[x]
denote the dth cyclotomic polynomial.
Proposition 5.1. Let χ be the unipotent character of G = SO6d−1 (q) or Sp6d−2 (q) (respectively of
−
SO+
2(3d−1) (q), SO6d (q)) parameterised by the symbol




 
d 2d
d 2d
d 2d
respectively
,
,
0
01
with d ≥ 3 odd, or the unipotent character of SO+
6e (q) parameterised by
 
2e
e
for d = 2e even. Then χ(1) 6≡ ±1 (mod |G|ℓ ) for any prime 2 < ℓ with dℓ (q) = d.
Proof. Since Φd (q) divides |G| at least twice it is sufficient to show that χ(1) 6≡ ±1 (mod Φd (q)2ℓ ). We
use a version of Babbage’s congruence for quantum binomial coefficients


d
hd − 1
≡ x(h−1)(2) (mod Φd (x)2 ) in Z[x]
d−1 x

for any d, h ≥ 2 (proved in [10, Lemma 3.7]). If χ belongs to d 02d , we can express its degree using a
quantum binomial coefficient evaluated at q 2 , see [4, 13.8]:


1 3d − 1
(q 2 − 1) · · · (q 6d−2 − 1)(q 2d − q d )(q 2d + 1)(q d + 1)
q d (q 2d + 1).
=
χ(1) =
2(q 2 − 1) · · · (q 4d − 1)(q 2 − 1) · · · (q 2d − 1)
2 d − 1 q2
Substituting x = q 2 in the Babbage congruence we get a congruence over the integers modulo Φd (q 2 )2 .
Since Φd (x2 ) = Φd (x)Φd (−x) we also get a congruence modulo Φd (q)2 :
1
χ(1) ≡ q 2d(d−1)+d (q 2d + 1) (mod Φd (q)2 ).
2
It suffices to show that 2χ(1) 6≡ ±2 (mod Φd (q)2ℓ ). Since Φd (q) | (q d − 1) we get
2χ(1) ≡ q 2d(d−1)+d · 2q d = 2(q 2d )d ≡ 2(q 2d − (q d − 1)2 )d = 2(2(q d − 1) + 1)d
≡ 2(2d(q d − 1) + 1) (mod Φd (q)2 ).
Since ℓ 6= 2, d < ℓ and ℓ | (q d − 1) we conclude that 2χ(1) + 2 is not divisible by ℓ and that the highest
power of ℓ dividing 2χ(1) − 2 is (q d − 1)ℓ = Φd (q)ℓ .


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

Now we turn to the unipotent character with symbol
considered χ(1) by the factor

d 2d
0 1 .



15

Its degree differs from the previously

(q 2d + q)(q d−1 + 1)
q 3d−1 + 3q d + q − 1 + (q d − 1)2
.
=
(q 3d−1 + 1)(q + 1)
q 3d−1 + 3q d + q − 1 + (q d + 2)(q d − 1)2
We argue that both degrees are equal modulo Φd (q)2ℓ .
For this, note that for integers a, b, c, m with ab/c ∈ Z, b ≡ c (mod m) and (c, m) = 1 there is an
integer c̃ with cc̃ ≡ bc̃ ≡ 1 (mod m) and so ab/c ≡ ab/c · cc̃ ≡ abc̃ ≡ a (mod m). This applies here
because (q 3d−1 + 1)(q + 1) is not divisible by ℓ (since d ≥ 3 is the order of q modulo ℓ and (q 3d−1 + 1)(q +
1)(q 3d−1 − 1)(q − 1) = (q 6d−2 − 1)(q 2 − 1) is not divisible by ℓ).

The same argument works for the degree of the unipotent character with symbol d 2d . Its degree
differs from the previous χ(1) by the factor
2q d + 2(q d − 1)2
2(q 2d − q d + 1)
=
2d
q +1
2q d + (q d − 1)2
and q 2d + 1 is not divisible by ℓ.
Finally we consider for even d = 2e the unipotent character ψ with symbol


3e − 1
ψ(1) =
(q 2e + q e + 1)q e .
e − 1 q2

2e
e . Its degree is



Evaluating Babbage’s congruence at q 2 yields a congruence modulo Φe (q 2 )2 . But note that for odd e we
have Φe (x2 ) = Φe (x)Φe (−x) and Φe (−x) = Φd (x), and for even e we have Φe (x2 ) = Φd (x). So, we also
get congruences modulo Φd (q)2 . Using now Φd (q) | (q e + 1) we find with similar arguments as before
2
that ψ(1) ≡ −q 2e (mod Φd (q)2 ) and that ψ(1) − 1 is not divisible by ℓ, and that ψ(1) + 1 is divisible by
Φd (q)ℓ but no higher power of ℓ.

In order to deal with certain unipotent characters, we recall some results of James and Mathas [8] on
reducibility of characters of Hecke algebras. Let Hn = Hn (q, Q) be the Iwahori–Hecke algebra of type Bn
with parameters q and Q over Z[q ±1 , Q±1 ]. Its irreducible characters are in natural bijection with those
of the Weyl group W (Bn ) via the specialisation q 7→ 1, Q 7→ 1, and hence labelled by pairs of partitions
(λ, µ) of n. We write χλ,µ for the character of Hn labelled by (λ, µ). We consider certain specialisations
of Hn .
Proposition 5.2. Let ℓ be a prime and q a prime power. Set d = dℓ (q).
(a) If d is odd, n = 2d + r with 0 ≤ r ≤ d − 2, and (λ, µ) = ((d + r, r + 1, 1d−r−1), −), then the
character χλ,µ of Hn (q, q) is reducible modulo ℓ.
(b) If d = 2e > 2 is even, n = 2e + r with 0 ≤ r ≤ e − 1, and (λ, µ) = ((r), (e + r + 1, 1e−r−1 )), then
the character χλ,µ of Hn (q, q) is reducible modulo ℓ.
Proof. Let ζd denote a primitive complex dth root of unity. The reduction modulo ℓ of Hn (q, q) factors
through the specialisation to Hn (ζd , ζd ), thus a character which becomes reducible under the latter
specialisation will a fortiori be reducible modulo ℓ. James and Mathas [8, Thms. 4.7(i) and 4.10] give
a sufficient criterion for χλ,µ to become reducible under the specialisation to Hn (ζd , ζd ), if (λ, µ) is a
Kleshchev bipartition. In case (a), χλ,µ is reducible modulo Φd by [8, Thm. 4.10(i)] since the character of
the Hecke algebra of Sn labelled by λ = (d + r, r + 1, 1d−r−1) is reducible modulo Φd , as the first column
hook lengths are different.
In (b), (λ, µ) is Kleshchev, and for r > 0 the last box of the Young diagram of λ can be moved to the
end of the first column of µ without changing its residue, so χλ,µ is reducible by [8, Thm. 4.10(ii)]. For
r = 0 the character χλ,µ is reducible modulo Φ2e by [8, Thm. 4.10(i)] since the character of the Hecke
algebra of Sn labelled by the second part µ = (e + 1, 1e−1 ) is.



16

FRANK LÜBECK AND GUNTER MALLE

The next reducibility result for characters of specialisations of the Hecke algebra of type Bn will be
used in the investigation of unipotent characters of Spin±
2n (q).
Proposition 5.3. Let ℓ be a prime and q a prime power. Set d = dℓ (q).
(a) If d is odd, n = 2d + r with 0 ≤ r ≤ d − 2, and (λ, µ) = ((d + r, r + 1, 1d−r−1), −), then the
character χλ,µ , of Hn (q, 1) is reducible modulo ℓ.
(b) If d = 2e > 2 is even, n = 2e + r with 0 ≤ r ≤ e − 1, and (λ, µ) = ((e + r, 1e−r ), (r)), then the
character χλ,µ of Hn (q, 1) is reducible modulo ℓ.
(c) If d is odd, n = 2d + r with 1 ≤ r ≤ d − 1, and (λ, µ) = (d + r − 1, r, 1d−r ), −, then the character
χλ,µ of Hn−1 (q, q 2 ) is reducible modulo ℓ.
(d) If d = 2e > 2 is even, n = 2e + r with 1 ≤ r ≤ e − 1, and (λ, µ) = ((r − 1), (e + r + 1, 1e−r−1 )),
then the character χλ,µ of Hn−1 (q, q 2 ) is reducible modulo ℓ unless (e, r) = (2, 1).
Proof. Parts (a) and (c) again follow from [8, Thm. 4.10(i)] as the first column hook lengths of λ are
different. The characters χλ,µ as in (b) and (d) are reducible since the first, respectively second part of λ
is a hook partition, of length d = 2e, hence belonging to a reducible character of the Hecke algebra of type
S2e , unless this hook is either (2e) or (12e ). The latter case only occurs in (d) when (e, r) = (2, 1).

5.2. Simple endotrivial modules in classical type groups. We will use the fact shown in [11,
Thm. 1.3] that any endotrivial module is liftable to a characteristic 0 representation. Therefore, we can
investigate endotrivial modules by the ordinary character of their lift. These characters have the following
properties:
• they are irreducible modulo ℓ,
• their values on ℓ-singular classes are of absolute value 1,
• their degree is congruent to ±1 modulo |G|ℓ .
Theorem 2 is now a consequence of:
Theorem 5.4. Let G = Sp2n (q) or G = Spin2n+1 (q) with n ≥ 2, (n, q) 6= (2, 2), or G = Spin±
2n (q) with
n ≥ 4, and ℓ a prime for which Sylow ℓ-subgroups of G are non-cyclic. Let ρ be the character of a nontrivial
simple endotrivial kS-module, for a central factor group S of G. Then we have G = S = Sp8 (2) ∼
= O9 (2),
ℓ = 5, and ρ = ρS , with S = 041 , is the unipotent character of degree ρS (1) = 51.

Proof. By [11, Thms. 6.7 and 5.2] there do not exist non-trivial simple endotrivial kS-modules if either
ℓ = 2 or ℓ divides q. Now let d = dℓ (q). Since Sylow ℓ-subgroups of G are non-cyclic, the cyclotomic
polynomial Φd (q) has to divide the group order at least twice. By Theorem 4.1, all non-unipotent characters of G vanish on some ℓ-singular element of G, so cannot come from simple endotrivial modules.
The only candidates for endotrivial unipotent characters are those appearing in the conclusion of Theorem 4.2. Of those, we can discard the Steinberg character of G, because G contains ℓ-singular elements
with non-trivial unipotent part, and on those classes the value of the Steinberg character is zero.
Now consider the other unipotent characters listed in Theorem 4.2. First assume that G = Sp2n (q) or
G = Spin2n+1 (q). Let ρ = ρS with S as in Theorem 4.2(1). So d is odd and n = 2d + r, 0 ≤ r ≤ d − 1.
Then ρ lies in the principal series and is parameterised by the character of the Weyl group W (Bn ) labelled
by the pair of partitions ((d + r, r + 1, 1d−r−1), −) ⊢ 2d + r. By Proposition 5.2(a), the corresponding
character of the Hecke algebra Hn of type Bn is reducible modulo ℓ for r 6= d−1. Since the decomposition
matrix of the Hecke algebra of W (Bn ) embeds into that of G (see e.g. [7, Thm. 4.1.14]), this shows that
ρS is reducible modulo ℓ, so does not give an example. The same argument applies to the Alvis–Curtis
dual characters, since Alvis–Curtis duality on the side of Hecke
algebras corresponds to tensoring with

the sign character. In the case r = d − 1 we have S = d 02d and the corresponding unipotent character
does not satisfy the necessary degree congruence by Proposition 5.1.
So now assume that d = 2e is even and write n = 2e + r with 0 ≤ r ≤ e − 1. Let ρ = ρS as in
Theorem 4.2(2). Again, ρ lies in the principal series and is labelled by the pair of partitions ((r + 1), (e +


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

17

r, 1e−r−1 )) ⊢ 2e + r. Hence
 it is reducible modulo ℓ by Proposition 5.2(b) if e > 1. For e = 1 we have
r = 0, n = 2 and S = 021 . Here ρS (1) = q(q 2 + 1)/2 ≡ 2q + 1 (mod (q + 1)2 ) is not congruent to ±1
modulo the ℓ-part of the group order.
For G = Sp2n (q) or G = Spin2n+1 (q) it remains to consider the unipotent characters listed in Theorem 4.2(8) and (9). (Note that the group Sp4 (2) was excluded.) In case (8) we have q = d = 2, so ℓ = 3.
The listed symbol parameterises a unipotent character of degree 7, its Alvis-Curtis dual has degree 56,
both incongruent ±1 (mod 33 ). Finally in case (9), ℓ|(q 2 + 1) = 5. The second symbol belongs to a
character of degree 119, its Alvis–Curtis dual has degree 30464, both incongruent to ±1 (mod 52 ), so
this gives no example. But the 51-dimensional simple unipotent module for Sp8 (2) labelled by 041 is
irreducible and endotrivial in characteristic ℓ = 5. Indeed, the restriction of the corresponding irreducible
character to the subgroup O+
8 (2) contains the trivial character once and all other constituents are of 5defect zero, hence projective modulo 5. Its Alvis–Curtis dual has degree 13056 ≡ 6 (mod 52 ), so cannot
lead to an example.
Next consider the case that G = Spin+
2n (q). Let ρ = ρS be unipotent with S as in Theorem 4.2(3). So
d is odd and n = 2d + r with 0 ≤ r ≤ d − 1. Then ρ lies in the principal series and is parameterised by the
character of the Weyl group W (Dn ) labelled by the pair of partitions (λ, µ) = ((d + r, r + 1, 1d−r−1 ), −) ⊢
2d + r. By Proposition 5.3(a), the corresponding character χλ,µ of the Hecke algebra Hn of type Bn is
reducible modulo ℓ for r 6= d − 1. Since λ 6= µ, χλ,µ restricts irreducibly to the Hecke algebra Hn′ of type
Dn (of index 2) and thus is also reducible as a character of Hn′ modulo ℓ. Using that the decomposition
matrix of the Hecke algebra of W (Dn ) embeds into that of G, this shows that ρS is reducible modulo ℓ,
so does not give an example. The same argument applies to the Alvis–Curtis dual characters. In the
remaining case r = d − 1, Proposition 5.1 shows that the corresponding unipotent character does not
satisfy the degree congruence.
Now assume that ρS is as in Theorem 4.2(4), so d = 2e is even and n = 2e + r with 0 ≤ r ≤ e. Again,
ρ lies in the principal series and is labelled by the pair of partitions ((e + r, 1e−r ), (r)) ⊢ 2e + r. By
Proposition 5.3(b) the corresponding character of the Hecke algebra of type Bn is reducible modulo ℓ if
r < e and e > 1, and so as before the same holds for the character of the Hecke subalgebra of type Dn ,
whence ρS is reducible modulo ℓ for e > 1. Note that e = 1 is excluded since then n = 2e = 2. The case
when r = e does not satisfy the degree congruence by Proposition 5.1.
2
Similarly, in the case that G = Spin−
2n (q) the characters of the principal series Hecke algebra Hn−1 (q, q )
labelled by (λ, µ) as in Theorem 4.2(5) and (6) are reducible modulo ℓ by Proposition 5.3(c) and (d),
so the same holds for the unipotent characters parameterised by these pairs, unless r = d. The latter
character again does not belong to an endotrivial module by Proposition 5.1. In the exceptional case
(e, r) = (2, 1) of Proposition 5.3(d) we have n = 2e + r = 5 and ρS (1) + 1 ≡ 4(q 2 + 1) (mod (q 2 + 1)2 ),
hence the necessary degree congruence is not satisfied for ρS .
Finally, the character listed in Theorem 4.2(10) takes value 2 on some ℓ-singular classes, by the final
statement in that result, so again cannot be endotrivial.

The endotrivial characters of Sp4 (2) ∼
= S6 and its covers have been described in [11, Thm. 4.9].
As pointed out before the simple endotrivial modules of linear and unitary groups have already been
determined in [10, Thm. 3.10 and 4.5].
