---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-000-11-irreducible-representations-of-large-symmetri
section_title: "Irreducible representations of large symmetric groups"
section_number: 1.1
pages: 1-2
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
representations of symmetric groups are in the one-to-one c orrespondence
with Young diagrams and due to algorithms such as Murnaghan–Nakayama
rule or Robinson–Littlewood rule the essential questions concerning repre-
sentations and characters of symmetric groups can be answer ed by a com-
binatorial study of the corresponding Young diagrams [Ful9 7]. However,
when one studies the asymptotic properties of large symmetr ic groups, the
work with Young tableaux becomes cumbersome and one is in the need to
ﬁnd another object which would encode the same information i n a more
convenient way. Alternatively, one can state the above problem as follows:
a typical partition of a large number q (or equivalently, a Young diagram
with q boxes) is a collection of at least √q numbers, hence it contains a
lot of information. Nevertheless, we can expect that one doe s not need to
know all this information to extract (with a reasonable accu racy) the prop-
erties of characters and representations. Therefore the qu estion arises how
1
2 PIOTR ´SNIADY
to compress the information about the Young diagrams in the most efﬁcient
way.
It turns out that the right tool for development of the above program is the
notion of the transition measure of a Young diagram which was introduced
by Kerov [Ker93, Ker99]. The transition measure of a Young di agram is a
probability measure on the real line—therefore it has a much more analytic
nature than a combinatorial notion of a Young diagram and for this reason
it is very appealing for our purposes. Yet another advantage of this object
is that it is possible to characterize it in many ways [Bia98, Oko00].
Of course, a question arises how to relate the transition mea sure of a
Young diagram with the values of the corresponding characte rs. In this
article we ﬁnd the appropriate formula in a form of an asymptotic series the
terms of which correspond to two-dimensional surfaces with a prescribed
genus.
The ﬁrst result in this direction was obtained by Biane [Bia9 8]: he
showed that if the sequence of Young diagrams (after appropr iate scaling)
converges to some limit shape then the leading term corresponds to surfaces
with genus zero and therefore this leading term can be comput ed by the
means of V oiculescu’s free probability theory [VDN92, HP00]. Okounkov
[Oko00] was studying the distribution of the length of the ﬁr st rows of a
large random Young diagram sampled according to the Plancherel measure;
he showed that the limit distribution coincides with the limit distribution of
the biggest eigenvalues of a random matrix in the Gaussian Unitary Ensem-
ble (GUE). The main idea of his proof was the observation that the both
the formula for the moments of a GUE random matrix and the form ula for
the moments of the transition measure of a random Young diagr am can be
viewed as series the terms of which correspond to two-dimensional surfaces
with prescribed genus. One can view results of this article a s an attempt to
simplify some of the arguments of Biane [Bia98] and simultaneously to pro-
vide better asymptotic expansion. Our results are closely related to those of
Okounkov [Oko00] with the difference that we do not study theconnection
with random matrices but on the bright side we do not restrict ourselves to
the case of the Plancherel measure.
