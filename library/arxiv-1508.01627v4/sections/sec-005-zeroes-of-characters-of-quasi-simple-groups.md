---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-005-zeroes-of-characters-of-quasi-simple-groups
section_title: "Zeroes of characters of quasi-simple groups"
section_number: 6
pages: 17-18
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
Together with our previous work [10, 11] with C. Lassueur and E. Schulte our results allow us to
guarantee the existence of zeroes of characters of quasi-simple groups on ℓ-singular elements once the
ℓ-rank is at least 3, as claimed in Theorem 1 which we restate:
Theorem 6.1. Let ℓ > 2 be a prime and G a finite quasi-simple group of ℓ-rank at least 3. Then for any
non-trivial character χ ∈ Irr(G) there exists an ℓ-singular element g ∈ G with χ(g) = 0, unless one of:


18

FRANK LÜBECK AND GUNTER MALLE

(1) G is of Lie type in characteristic ℓ;
(2) ℓ = 5, G = L5 (q) with 5||(q − 1) and χ is unipotent of degree χ(1) = q 2 Φ5 ;
(3) ℓ = 5, G = U5 (q) with 5||(q + 1) and χ is unipotent of degree χ(1) = q 2 Φ10 ; or
(4) ℓ = 5, G = Ly and χ(1) ∈ {48174, 11834746}; or
(5) G = E8 (q) with q odd, dℓ (q) = 4 and χ is the semisimple character with label ((0), (8)) in the
unique Lusztig-series of type D8 .
Proof. For G a covering group of a sporadic simple group, an easy check of the known character tables
shows that only case (4) arises. For alternating groups and their covering groups the claim is contained
in the proof of [11, Prop. 4.2 and Thm. 4.5]. If G is a covering group of a special linear or unitary group
then [10, Thm. 1.3] shows that only the cases in (1), (2) and (3) can arise.
For the remaining groups of Lie type first note that the Steinberg character vanishes on the product
of any ℓ-element with a unipotent element in its centraliser, so can be discarded from our discussion. We
now first consider groups G of exceptional Lie type. Since the ℓ-rank of G is at least 3, it must be of
type F4 , E6 , 2E6 , E7 or E8 . For these it is shown in the proof of [11, Thm. 6.11] that their irreducible
characters χ vanish on some ℓ-singular element unless either χ is unipotent or ℓ|(q 2 + 1) in G = E8 (q)
and χ lies in the Lusztig series of an isolated element with centraliser D8 (q). We deal with these cases in
turn.
We begin with G = E8 (q). Since G has ℓ-rank at least 3 we must have d = dℓ (q) ∈ {1, 2, 3, 4, 6}.
First assume that d = 1. There exist maximal tori of orders divisible by Φ1 Φ7 , Φ1 Φ9 and Φ1 Φ14 , hence
G contains semisimple ℓ-singular elements of order divisible by a Zsigmondy prime divisor r of Φ7 , Φ9
and Φ14 . All non-trivial unipotent characters apart from φ8,1 , φ8,91 and the Steinberg character are of
defect zero for one of these three primes, hence vanish on any r-singular element. For the remaining two
characters, direct calculation with the character formula shows that they vanish on elements of order
Φ1 Φ4 . Very similar considerations apply to the remaining cases d ∈ {2, 3, 4, 6}. If d = 4 and χ lies in the
Lusztig series of an isolated element with centraliser D8 (q), the same argument using Zsigmondy
 prime
divisors of Φ5 , Φ8 , Φ10 and Φ12 only leaves the four characters in that series, those with label 08 and 01
18
and their duals. Three of them are zero on suitable products of an ℓ element with a unipotent element.
The arguments for the unipotent characters of the remaining exceptional groups are similar and easier.
Finally, let us suppose that G is of classical Lie type. By Theorem 4.1 the claim holds if χ is not
unipotent. For unipotent characters χ, the claim follows from Theorem 4.2, since all exceptions listed
there have ℓ-rank two, including those in cases (4) and (5) with n = 3e respectively n = 3d.

Remark 6.2. (a) Let p be a prime and f ≥ 1. Then G = SL2 (pf ) has p-rank f , but its irreducible
characters of degree q ± 1 do not vanish on any p-singular elements of G. Similarly, there exist such
characters for SL3 (pf ), SU3 (pf ) and 2 G3 (32f +1 ). This shows that Case (1) in Theorem 6.1 is a true
exception. Also, Ly has characters of degrees 48174 and 11834746 which do not vanish on 5-singular
elements. (It is well-known that the Lyons group behaves like a characteristic 5 group in many respects,
see e.g. [14].) It can be checked that the unipotent characters of L5 (q) and U5 (q) listed in Cases (2)
and (3) are also true exceptions.
(b) We expect the exceptions in Case (1) to only occur for groups of Lie type in characteristic ℓ of
small Lie rank.
(c) The results of [11], [10] and of the present paper show that even for ℓ-rank 2 there exist only
relatively few irreducible characters of quasi-simple groups not vanishing on some ℓ-singular element.
Nevertheless we refrain from attempting to give an explicit list in that case.
