---
doc_id: pjm-v161-n1-p02-p
doc_title: "Paciﬁc Journal of Mathematics STUDYING LINKS VIA CLOSED BRAIDS. III. CLASSIFYING LINKS WHICH ARE CLOSED 3-BRAIDS"
section_id: sec-001-1-introduction-this-manuscript-is-the-third-in-a
section_title: "Introduction. This manuscript is the third in a series of six papers"
section_number: 1
pages: 2-5
source_pdf: pjm-v161-n1-p02-p.pdf
source_sha256: a93e922eab1ee67c
doc_brief: "Paciﬁc Journal of Mathematics STUDYING LINKS VIA CLOSED BRAIDS. III. CLASSIFYING LINKS WHICH ARE CLOSED 3-BRAIDS — 24 sections: JOAN S. BIRMAN AND WILLIAM W. MENA; Introduction. This manuscript is t"
---
in which the authors have been studying the closed braid representa-
tives of links. The other five are referenced here as [B-M I, II, IV-VI]
In [B-M, I] the authors prove that, with an appropriate definition of
the complexity of a closed braid representative of a link, there are
finitely many conjugacy classes of braids of minimum complexity. In
this paper we work out in detail the first non-trivial example of this
"finiteness theorem": we prove that for links of braid index n < 3
there are at most two conjugacy classes of minimum complexity. We
then use this result to give a complete numerical invariant of link type,
and an algorithm to find it, starting with an arbitrary closed 3-braid.
The complexity function which was used in [B-M, I] relates to in-
compressible surfaces which are bounded by the link. These surfaces
have maximum Euler characteristic, among all oriented surfaces with
25
26 JOAN S. BIRMAN AND WILLIAM W. MENASCO
boundary the given oriented link. It was shown in [Be] and in [B-M,
II] that when the link has braid index < 3 these surfaces are especially
simple. As a result, the combinatorial data which was introduced in
[B-M, I] to describe the surfaces reduces to a cyclic word in a special
set of generators for the braid group B^. The algorithm which we
give then not only solves the link problem for links of braid index 3,
it also (with the help of results in [X]) provides a surface of maximal
Euler characteristic with boundary the given link. The long range goal
of the series of manuscripts [B-M, I-VI] is to generalize these results
to arbitrary braid index n .
Let JSP be an oriented link type in oriented S3, let L be a rep-
resentative of S*, and let A be an oriented circle in S3 — L. We
say that L is a closed n-braid with braid axis A if there is a choice
H = {H# θ e [0, 2π]} oΐafibration H of the open solid torus S3-A
by meridian discs H# such that L intersects each H# transversally.
The number n is the number of points in LnH^. In 1923 James
Alexander proved in [Al] that every link could be so-represented,
in many ways and for many different values of n. The connection
between braids and links was further developed by Emil Artin. In
his 1925 manuscript [Ar] he introduced the n-string braid group Bn
(n = 1, 2, 3, ...) and uncovered its structure. In 1935 A. A. Markov
studied the disjoint union B^ of all the Bn 's, describing in [Ma] the
equivalence relation in B^ which relates all of the open braids whose
closures have the same oriented link type. Two elementary equiva-
lences are needed: conjugacy in Bn and a stabilization move which
changes n. In 1968 Garside [Ga] solved the conjugacy problem in
Bn . This was a highly non-trivial step in the translation of Markov's
equivalence relation into an algorithmic solution to the link problem.
The role of "stabilization" in Markov's equivalence relation (and
indeed in many other areas of low dimensional topology such as Hee-
gaard theory, bridge representations of links, Kirby's Calculus, and
Waldhausen's study of the Heegaard splittings of S3) has been some-
what mysterious. The present investigation began with an attempt to
understand what is accomplished when one stabilizes, in the situation
of Markov's theorem. In the papers [B-M, I-VI] and subsequent ones
we hope to establish a version of Markov's theorem which does not
involve stabilization, i.e. in which one studies the braid representa-
tives of a link in Bn , for fixed n, rather than in the disjoint union
Boo of all of the braid groups. In this manuscript we do exactly that
for the first non-trivial case, n = 3. The classification of links which
STUDYING LINKS VIA CLOSED BRAIDS III 27
are closed 3-braids follows immediately, as there are several known
algorithmic solutions to the conjugacy problem in £3 ([SC], [G], [X]),
each yielding unique normal forms for conjugacy classes.
By the work of Yamada [Y] links which are defined by closed n-
braids have an alternative interpretation as links which are defined by
diagrams with n Seifert circles. A computer program is now available
[F] which begins with an arbitrary link diagram with n Seifert circles
and produces from it a closed n-braid representative (in fact, for n =
3 the program gives a 3-braid which is defined by the special generators
&\, &2> #3 which are introduced in this paper). We also have a second
program which yields normal forms for conjugacy classes in B$. Thus
our results are very concrete.
Two other special cases of Markov's theorem without stabilization
are proved in [B-M, IV] (which is a study of the n-braid representa-
tives of split links and composite links) and [B-M, V] (where the n-
braid representatives of the r-component unlink are studied for fixed
n>r). The pathologies which are investigated in the three papers [B-
M, III], [B-M, IV] and [B-M, V], all come into play if one attempts
to generalize the results of this paper to higher braid index.
To state our result, let σ\ and σ-i be the standard elementary braids
which generate the 3-string braid group #3. The central result in this
paper may be stated in the following way:
THE CLASSIFICATION THEOREM (Version I). A link & which is rep-
resented by a closed 3-braid admits a unique conjugacy class of 3-braid
representatives, with the following exceptions:
(i) £? is the unknot, which has three conjugacy classes of 3-braid
representatives, namely the classes of σ\σ2, ^f1^1 and σiσ^1 •
(ii) & is a type (2, k) torus link, k Φ ±\, which has two conju-
gacy classes of 3-braid representatives, namely the classes of o\θ2 and
kσ-\
σ2
(iii) J2? is one of a special class of links of braid index 3 which have
3-braid representatives which admit "braid-preserving flypes". These
links have at most two conjugacy classes of 3-braid representatives,
namely the classes of σfσ|σ[σ| and σfσ|σ[σ|, where p, q, r are
distinct integers having absolute value at least 2 and where δ = ±1.
The exceptional cases (i) and (ii) are the expected ones, but (iii)
was not previously recognized except in special cases (see [Mu]). It is
σΐσ2
