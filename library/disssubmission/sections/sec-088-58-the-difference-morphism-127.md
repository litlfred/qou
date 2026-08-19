---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-088-58-the-difference-morphism-127
section_title: "The difference morphism 127"
section_number: 5.8
pages: 135-137
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
whereτ∈ Perv(X,C) is some negligible perverse sheaf. In factτ = δX by
part (a) of the proposition. Furthermorepδ6 = δ0 is a skyscraper sheaf,
hence forU⊂ X sufﬁciently small we have
V+∼= H−4(δ−)|U∼= H−4(pδ4,2⊕δX)|U∼= d2∗(CC2×C2)
where the ﬁrst isomorphism is due to lemma 5.21 and where the last one
comes from the proof of lemma 5.25 forn = 2. □
5.8. The difference morphism
Motivated by the previous section, letC be a smooth complex projective
curve of genusg = 2n withn∈ N, and put
Cn = (C×···× C)/Sn.
We want to study the difference morphismdn : Cn×Cn−→X = JC from
above. To begin with, we claim that this morphism is generically ﬁnite and
has generic degree
N = deg(dn) = (2n
n
).
Indeed, by birationality of the Abel-Jacobi mapCn→Wn it sufﬁces to check
that the difference morphismgn : Wn×Wn→ X is generically ﬁnite of the
given degree. Note that the ﬁbre ofgn over a pointx∈ X(C) is isomorphic
to the intersectionZ =Wn∩(Wn +x). Now a Bertini-type argument and the
Poincar´e formula [13, sect. 11.2.1] for the fundamental classes
[Wn] = [ Wn +x] = 1
n!· [Θ]n∈ Hn(X,Z)
show that for a sufﬁciently general pointx∈X(C) the intersectionZ is ﬁnite
of cardinality
|Z| = degX
([Wn]∪[Wn +x]) = g!
n!·n! = N.
So over some Zariski-open dense subsetU⊂ X the morphismsgn and dn
restrict to a ﬁnite´etale cover of degreeN as claimed.
Now pickx∈ U(C), and consider the monodromy action ofπ1(U,x)
on the N distinct points of the ﬁbred−1n (x). Labelling these points in any
chosen order, we get a homomorphism
π1(U,x)−→ SN
to the symmetric group, and we deﬁne the monodromy groupG(dn) to
be the image of this homomorphism. A different choice of the labelling
only changes this subgroup by an inner automorphism ofSn. Our goal is
to determine the monodromy groupG(dn) for a general curveC of even
genus g = 2n. For this we will study a degeneration into a hyperelliptic
curve, where we have the following situation.
128 Chapter 5 – A family of surfaces
LEMMA 5.26. If C is a hyperelliptic curve of genus g= 2n, then the
above monodromy group G(dn) is isomorphic to the symmetric groupS2n,
and its action on the N points of a general ﬁbre of dn can be identiﬁed with
the action ofS2n on the set of all n-element subsets of{1,2, . . . ,2n}.
Proof. If g1
2 denotes the hyperelliptic linear series onC, then for every
effective divisorD∈ Cn the linear seriesn· g1
2−D contains an effective
divisor. Hence Wn is a translate of its negative−Wn, and it follows that
up to a translation the difference morphismdn coincides with the addition
morphismCn×Cn→ X. The latter factors asCn×Cn→C2n→ X where
the Abel-Jacobi morphismC2n→ X is birational. So we must determine
the monodromy groupH of the ﬁnite branched coverCn×Cn→C2n. This
cover is not Galois, but it is dominated by the Galois cover with groupS2n
in the following diagram.
C2n
S2n
%%
Cn×Cn
Sn×Sn

Cn×Cn

C2n
Take a pointp1 +··· + p2n∈ C2n with the pi∈ C all distinct. Via the ﬁrst
projectionCn×Cn→Cn, the ﬁbreF of the coverCn×Cn→C2n over this
point is identiﬁed with the set of alln-element subsets of{p1, . . . ,p2n}, and
the monodromy groupH is the image of the homomorphism
ϕ : S2n−→Aut(F)
which is given by the action of the Galois groupS2n of C2n→ C2n on
the ﬁbre F via permutation ofp1, . . . ,p2n. Note that ϕ is injective: The
identity is the only permutation inS2n that ﬁxes alln-element subsets of
the set{p1, . . . ,p2n}. Hence the claim of the lemma follows. □
We can now also deal with a general curve, proving theorem 5.2 from
the introduction. Here the monodromy groupG(dn) turns out to be almost
as large as possible — with the only drawback that we do not know whether
it contains an odd permutation.
THEOREM 5.2. If C is a general curve of genus g= 2n, then G(dn) is
either the alternating groupAN or the full symmetric groupSN.
Proof. By lemma 5.26 we can assume thatg > 2. In particular then a
general curveC of genusg is non-hyperelliptic. Hence lemma 5.25 shows
that the monodromy representation ofG(dn) splits into a direct sum of the
