---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-012-25-braid-representations-of-links-9
section_title: "Braid representations of links 9"
section_number: 2.5
pages: 9-10
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
2.5. Braid representations of links
By a theorem of Alexander [Al], any link is the closure ˆβ of a braid β. The braid index b(L) of a link L is the smallest
number of strands of a braid β whose closure ˆβ is L. See [Mo, FW, Mu]. Such β are also called braid representations
of L. The closure operation gives for a particular braid word β a link diagram D = ˆβ. Then we have for example
w(ˆβ) = [β], c(β) = c(ˆβ), c±(β) = c±(ˆβ), and s(ˆβ) is the number of strings of β (i.e. n for β ∈ Bn).
Many properties of braid words we will deal with relate to the corresponding properties of their link diagrams. For
example, a braid word is called positive if it contains no σ−1
i , or in other words, its closure diagram is positive. A
braid is positive if it has a positive braid word. In a similar fashion, we say that braid is ( A/B-)adequate if it has an
(A/B-)adequate word representation, and a word is adequate if the link diagram obtained by its closure is adequate.
If a braid word β is written as σ±1
1 ασ p
1 α′, where p ∈ Z and none of α and α′ contains a syllable of index 1, then the
diagram admits a ﬂype, which exchanges the syllables of index 1 in β, so that we obtain σp
1 ασ±1
1 α′. This operation
preserves the isotopy type of the closure link ˆβ, but in general changes the braid conjugacy class. The pheno menon
is explained in [BM]. In the context of general link diagrams , the ﬂype has been studied also extensively, most
prominently in [MT].
Alternatively to the standard Artin generators, one considers also a representation of the braid groups by means of an
extended set of generators (and their inverses)
σ±1
i,j = σi . . .σ j−2σ±1
j−1σ−1
j−2 . . .σ−1
i
for 1 ≤ i < j ≤ n. Note that
σi = σi,i+1 .(10)
A representation of a braid β, and its closure link L = ˆβ, as word in σ±1
i,j is called a band representation [BKL]. A
band representation of β spans naturally a Seifert surface of the link L as in ﬁgure 1: one glues disks into the strands,
and connects them by half-twisted bands along the σi,j. The resulting surface is called braided Seifert surface of L. A
minimal genus Seifert surface of L, which is a braided Seifert surface, is also called a Bennequin surface [BM2].
In this paper we will deal exclusively with band representations in B3. Then we have three band generators σi,i mod 3+1
(where i = 1,2,3, and ‘ mod ’ is taken with values between 0 and 2). With (10), we have σ1 = σ1,2 and σ2 = σ2,3, and
with the special meaning of σ3 ∈ B3 introduced above, σ3 = ¯σ1,3, where bar denotes the mirror image. (This mirroring
is used here for technical reasons related to Xu’s normal form, as explained below.)
If a band representation contains only positively half-twi sted bands (i.e. no σ−1
i,j occur), it is called band-positive
or strongly quasi-positive. A link with a strongly quasi-positive band (braid) represe ntation is called strongly quasi-
positive. Such links have an importance in connection to algebraic curves; see [Ru2].
Using the skein polynomial, deﬁne a quantity by
MW F(L) = 1
2
(
maxdeg v P − mindegv P
)
+ 1 .(11)
The Morton-Williams-Franks braid index inequality[Mo, FW] (abbreviated as MWF) states that
b(L) ≥ MWF (L)(12)
for every link L. This inequality is often exact (i.e. an equality). The stud y of links where it is exact or not has
occupied a signiﬁcant part of previous literature. Most not eworthy is the work of Murasugi [Mu] and Murasugi-
Przytycki [MP2].
The Morton-Williams-Franks results from two other inequal ities, due to Morton, namely that for a diagram D, we
have
1 − s(D) +w(D) ≤ mindeg l P(D) ≤ maxdeg l P(D) ≤ s(D) − 1 + w(D) .(13)
Williams-Franks showed these inequalities for the case of b raid representations (i.e. when D = ˆβ for some braid β).
Later it was observed from the algorithm of Yamada [Y] and V ogel [V o] that the braid version is actually equivalent to
(and not just a special case of) the diagram version.
10 2 Preliminaries, basic deﬁnitions and conventions
These inequalities were later improved in [MP2] in a way that allows to settle the braid index problem for many links
(see §6 or also [Oh]).
In the special case of 3-braids (and with the special meaning of σ3 as described above), Xu [Xu] gives a normal form
of a conjugacy class in σ1,2,3. By Xu’s algorithm, eachβ ∈ B3 can be written in one of the two forms
(A) [21]kR or L−1[21]−k (k ≥ 0), or
(B) L−1R,
where L and R are positive words in σ1,2,3 with (cyclically) non-decreasing indices (i.e. each σi is followed by σi or
σi mod 3+1, with ‘mod’ taken with values between 0 and 2). Since the form B must be cyclically reduced, we may
assume that L and R do not start or end with the same letter. This form is the short est word in σ1,2,3 of a conjugacy
class. By Bennequin’s aforementioned result, the braided surface is then a minimal genus (or Bennequin) surface.
