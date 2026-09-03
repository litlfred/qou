---
doc_id: arxiv-0802.1072v2
doc_title: "A note on closed 3-braids ∗"
section_id: sec-005-using-theorems-12-and-3
section_title: "Using Theorems 1,2, and 3"
section_number: null
pages: 6-9
source_pdf: 0802.1072v2 (1).pdf
source_sha256: 6f4d93f0b7ba5cd7
doc_brief: "A note on closed 3-braids ∗ — This is a review article about knots and links of braid index 3."
---
Theorems 1 and 2 . We need two more results before we can make Theorems 1 and 2 in to
results that can be used computationally. First, we need to b e able to recognize when the closure
of a 3-braid has braid index less than 3. Table I gives the Xu sy mbols Σ ⋆(W ) in the cases when
6
the closed braid associated to W has braid index less than 3. Using it, we can decide when a
closed 3-braid is a link of braid index 3, by computing its Xu- invariant and verifying whether it
is or is not the symbol for a 3-braid of braid index less than 3. In the table the symbol 1 u means
u syllables of length 1. For example, Table I tells us that a 3-b raid X whose Xu-invariant is
(−5; (14, 2)) = (−5; (1, 1, 1, 1, 2)) is conjugate to the 3-braid a−5
1 a2, which closes to the type (2,5)
torus knot. Therefore the closure of X has braid index 2.
W Σ ⋆(W )
ak
1a2, k = 1 and 2 (1; ( k− 1))
ak
1a2, k≥ 3 (−1; ( k + 1))
ak
1a−1
2 , k≥ 2 (−1; (1 , k))
ak
1a2, k≤− 2 (k; (1−k−1, 2))
ak
1a−1
2 , k≤− 1, (k; (1 −k−1))
a−1
1 a2 and a1a−1
2 (−1; (2))
a2 (0; (1))
a−1
2 (−1; (1))
T able I: Conjugacy classes of links of braid index less than 3
Next, if we are given two 3-braids W, W ′ and ﬁnd that they have distinct Xu-invariants, we cannot
be sure that they determine distinct links until we determin e whether they are ﬂype-admissible.
To answer this question, we need the following Lemma, which i s due to K.H.Ko and S.J.Lee:
Lemma 1. K.H.Ko and S.J.Lee, [21] (i) The ﬂype in (2) is non-degenerate if and only if |v|≥ 2,
also u, v + ǫ, w are pairwise distinct, also u, w⁄= 0 , ǫ, 2ǫ. (ii) The conjugacy class of a negative
ﬂype-admissible braid L contains a braid that admits a positive ﬂype if and only if u = 1 or w = 1,
or v = 2.
In Table II we give the Xu symbols for all non-degenerate ﬂype -admissible braids, up to cyclic
permutation of the tail symbol. There are 16 cases, because t he exponents u, v, w, ǫ can either be
positive or negative. To keep track of the signs, replace u, v, w by±p,±q,±r, where p, q, r > 0. Now
observe that only 8 of the 16 cases are needed, because a given braid K admits a non-degenerate
ﬂype if and only if the Xu-symbol for K or for K −1 coincides with one of the 8 symbols that are
given in Table II.
ǫ W Σ ⋆(W ), up to cyclic permutation of tail symbol
pos ap
1aq
2ar
1a2 (3 ; ( p− 2, q − 1, r − 2))
a−p
1 aq
2ar
1a2 (1− p ; ( q, r − 1, 1p))
ap
1a−q
2 ar
1a2 (2− q ; ( p− 1, 1q−1, r − 1))
ap
1aq
2a−r
1 a2 (1− r ; ( p− 1, q, 1r))
neg ap
1aq
2ar
1a−1
2 (0 ; ( p, q − 1, r ))
a−p
1 aq
2ar
1a−1
2 (−p ; ( q, r + 1, 1p−2))
ap
1a−q
2 ar
1a−1
2 (−q− 1 ; ( r + 1, p + 1, 1q−1))
ap
1aq
2a−r
1 a−1
2 (−r ; ( p + 1, q, 1r−2))
T able II: Conjugacy classes admitting non-degenerate ﬂypes
We remark that the data in Table II is only given up to cyclic pe rmutation of the tail symbol,
because the lexicographically smallest choice depends upo n the relative numerical values of p, q, r.
7
We now have essentially all the data needed to implement Theo rems 1,2 and 3, however an addi-
tional issue arises if one wishes to use any of our three theor ems on low crossing examples which
admit non-degenerate ﬂypes. For example, one might wish to t est a potential invariant which was
diﬃcult to compute on knots which had large crossing number. We give, in Table III, a list of all
of the knots of braid index 3 which admit non-degenerate nega tive ﬂypes, and do not also admit
positive ﬂypes, and have braid crossing number cb =|u| +|v| +|w| + 1≤ 12. Note that cb is not the
same as minimum crossing number for all possible projection s of the knot associated to our closed
braid (although for all but one of the examples in Table 1 the t wo are actually the same), rather it
is crossing number for closed 3-braid representatives whic h are in ﬂype position.
The knots are identiﬁed, in Table III, using both classical n otation (e.g as in [32]) and the newer
notation of Dowker-Thistlethwaite (used in all the newer ta bles). The former only exist through
10 crossings.
K(classical) K(Dowker-Thistlethwaite) β cb (u, v, w) (w, v, u)
810 8a3 -1 8 (3,-2,2) (2,-2,3)
1047 10a15 +1 10 (5,-2,2) (2,-2,5)
1062 10a41 +1 10 (3,-2,4) (4,-2,3)
1048 10a79 -3 10 (3,-4,2) (2,-4,3)
10127 10n16 -9 10 (-5,-2,2) (2,-2,-5)
10143 10n26 -7 10 (3,-2,-4) (-4,-2,3)
∗∗∗ 11a240 +7 12 (5,3,3) (3.3.5)
∗∗∗ 12a146 +3 12 (7,-2,2) (2,-2,7)
∗∗∗ 12a369 +3 12 (5,-2,4) (4,-2,5)
∗∗∗ 12a576 +3 12 (3,-2,6) (6,-2,3)
∗∗∗ 12a835 -5 12 (3,-6,2) (2,-6,3)
∗∗∗ 12a878 -1 12 (5,-4,2) (2,-4,5)
∗∗∗ 12a1027 -1 12 (3,-4,4) (4,-4,3)
∗∗∗ 12a1233 +1 12 (5,-3,3) (3,-3,5)
∗∗∗ 12n234 -11 12 (-7,-2,2) (2,-2,-7)
∗∗∗ 12n466 -9 12 (-5,-3,3) (3,-3,-5)
∗∗∗ 12n467 -7 12 (-3,-4,4) (4,-4,-3)
∗∗∗ 12n468 -5 12 (-3,-3,5) (5,-3,-3)
∗∗∗ 12n472 -15 12 (-3,-4,-4) (-4,-4,-3)
∗∗∗ 12n570 -9 12 (-3,-5,3) (3,-5,-3)
T able III: A list of all examples of non-transversally simple
closed 3-braids with braid crossing number cb≤ 12
To assemble the data in Table III we began by listing all possi ble numbers (±|u|,±|v|,±|w|) with
cb =|u|+|v|+|w|+ 1, deleting those that do not satisfy the constraints of the two lemmas. Next we
used Knotscape [15] to sort the survivors into classes which had the same topological knot type. For
each topological knot type, some of the examples had non-min imal braid crossing number, so we
deleted those. For example, (−3, 4, 2) appeared as an example with cb = 10, but its conjugacy class
also has an 8-crossing example, (3 ,−2, 2), so we deleted ( −3, 4, 2). After that, for each topological
knot type we divided the representing closed braids into con jugacy classes belonging to the braids
before and after the ﬂype. In every case it turned out that the re were two distinct conjugacy classes
8
in B3, as must be the case, by Theorem 1. Finally, we chose exactly o ne representative from each
conjugacy class, whenever it happened that the list of survi vors had more than one representative.
In this regard we note that, for example, σ−5
1 σ3
2σ−3
1 σ−1
2 ≈ σ2
1σ−2
2 σ−5
1 σ−1
2 ≈ σ−3
1 σ−4
2 σ2
1σ−1
2 . This
shows that conjugate braids which admit ﬂypes need not have t he same braid crossing number cb.
In this case the ﬁrst has braid crossing number 12 and the othe r two have crossing number 10.
There are examples where all three have the same crossing num ber, and examples where one has
minimal crossing number and the other two have higher crossi ng number. This issue arises when
we enumerate the low-crossing number examples.
The examples in Table III are given by specifying, for each pa ir of transversal knot types, the topo-
logical knot typeK in the standard tables, the Bennequin number β = u + v + w− 4, the minimum
closed braid crossing number cb =|u| +|v| +|w| + 1, and the two closed 3-braid representatives
TK 1,TK 2. The closed braids are determined by the triplets ( u, v, w) and ( w, v, u), i.e. as negative
ﬂype-related braids σu
1 σv
2σw
1 σ−1
2 and σw
1 σv
2 σu
1 σ−1
2 .
