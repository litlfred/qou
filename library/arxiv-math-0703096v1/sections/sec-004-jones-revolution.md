---
doc_id: arxiv-math-0703096v1
doc_title: "KNOTS From combinatorics of knot diagrams to combinatorial topology based on knots"
section_id: sec-004-jones-revolution
section_title: "Jones revolution"
section_number: null
pages: 28-53
source_pdf: arxiv-math-0703096v1.pdf
source_sha256: 337c26b7164ff942
toc_source: outline
doc_brief: "History of knot theory (Przytycki, arXiv:math/0703096, chapter of KNOTS) — from Gauss and Listing through Kelvin, Tait, Kirkman and Little to the twentieth century"
---
Jones revolution
In the spring of 1984, Vaughan Jones discovered his invariant of links, VL(t)
[Jo-0, Jo-1, Jo-2]37, and still in May of 1984 he was trying various substi-
tutions to the variable t, in particular t = −1. He observed that VL(−1)
is equal to the classical knot invariant – determinant of a knot; however,
initially he was unable to prove it. Soon he realized that his polynomial
satisﬁes the local relation analogous to that discovered by Alexander and
Conway and established the meaning of t = −1.38 Thus the Jones polyno-
mial is deﬁned recursively as follows:
(i) Vo = 1,
(ii)
1
t VL+(t) −tVL−(t) = (
√
t −
1
√
t)VL0(t).
In the summer and the fall of 1984, the Alexander and the Jones polyno-
mials were generalized to the skein (named also Conway-Jones, Flypmoth,
Homﬂy, Homﬂypt39, generalized Jones, 2-variable Jones, Jones-Conway,
Thomﬂyp, twisted Alexander) polynomial, PL ∈Z[a±1, z±1], of oriented
links [FYHLMO, P-T-1]. This polynomial is deﬁned recursively as follows
[FYHLMO, P-T-1]:
(i) Po = 1;
(ii) aPL+ + a−1PL−= zPL0.
In particular ∆L(t) = PL(i, i(
√
t −
1
√
t)), VL(t) = PL(it−1, i(
√
t −
1
√
t)).
In August 1985 L. Kauﬀman found another approach to the Jones polyno-
mial40. It starts from an invariant, < D >∈Z[µ, A, B], of an unoriented
37Jones wrote in [Jo-6]: “It was a warm spring morning in May, 1984, when I took
the uptown subway to Columbia University to meet with Joan S. Birman, a specialist in
the theory of “braids”... In my work on von Neumann algebras, I had been astonished
to discover expressions that bore a strong resemblance to the algebraic expression of
certain topological relations among braids. I was hoping that the techniques I had been
using would prove valuable in knot theory. Maybe I could even deduce some new facts
about the Alexander polynomial.
I went home somewhat depressed after a long day
of discussions with Birman. It did not seem that my ideas were at all relevant to the
Alexander polynomial or to anything else in knot theory. But one night the following
week I found myself sitting up in bed and running oﬀto do a few calculations. Success
came with a much simpler approach than the one that I had been trying. I realized I had
generated a polynomial invariant of knots.”
38The relation was also discovered independently in July 1984 by Lickorish and Millett.
39Homﬂy or Homﬂypt is the acronym after the initials of the inventors: Hoste, Ocneanu,
Millett, Freyd, Lickorish, Yetter, Przytycki and Traczyk.
40First he thought that he produced a new knot polynomial and only analyzing the
polynomial he realized that he found a variant of the Jones polynomial.
II.4. JONES REVOLUTION
29
link diagram D called the Kauﬀman bracket [K-6]. The Kauﬀman bracket
is deﬁned recursively by:
(i)
< o . . . o
| {z }
i
>= µi−1
(ii)
< L+ >= A < L0 > +B < L∞>
(iii)
< L−>= B < L0 > +A < L∞>
where L+, L−, L0 and L∞denote four diagrams that are identical except
near one crossing as shown in Figure 14, and < o . . . o
| {z }
i
> denotes a diagram
of i trivial components (i simple circles).
If we assign B = A−1 and µ = −(A2 + A−2) then the Kauﬀman bracket
gives a variant of the Jones polynomial for oriented links. Namely, for A =
t−1
4 and D being an oriented diagram of L we have
VL(t) = (−A3)−w(D) < D >
(II.1)
where w(D) is the planar writhe (twist or Tait number) of D equal to the
algebraic sum of signs of crossings.
It should be noted, as ﬁrst observed by Kauﬀman, that bracket < >µ,A,B
is an isotopy invariant of alternating links (and their connected sums) under
the assumption that the third Tait conjecture (soon after proven by Menasco
and Thistlethwaite [M-T-1, M-T-2]) holds.
In the summer of 1985 (two weeks before discovering the “bracket”),
L. Kauﬀman invented another invariant of links [K-5], FL(a, z) ∈Z[a±1, z±1],
generalizing the polynomial discovered at the beginning of 1985 by Brandt,
Lickorish, Millett and Ho [B-L-M, Ho]. To deﬁne the Kauﬀman polynomial
we ﬁrst introduce the polynomial invariant of link diagrams ΛD(a, z). It is
deﬁned recursively by:
(i) Λo(a, z) = 1,
(ii) Λ
(a, z) = aΛ|(a, z); Λ
(a, z) = a−1Λ|(a, z),
(iii) ΛD+(a, z) + ΛD−(a, z) = z(Λ0(a, z) + ΛD∞(a, z)).
30
CHAPTER II. HISTORY OF KNOT THEORY
The Kauﬀman polynomial of oriented links is deﬁned by
FL(a, z) = a−w(D)ΛD(a, z)
where D is any diagram of an oriented link L.
+
L
-
L
L 0
L
8
Figure 5.1
Jones type invariants lead to invariants of three-dimensional manifolds
[At, Wit, P-5, Tu-2, R-T-2, Tu-Vi, Tu-We, P-19]. We already mentioned
that Jones type invariants of knots have been used to solve Tait conjectures.
The Jones discovery, however, not only introduced a delicate method of
analyzing knots in 3-manifolds but related knot theory to other disciplines
of mathematics and theoretical physics, for example statistical mechanics,
quantum ﬁeld theory, operator algebra, graph theory and computational
complexity. On the other hand the Jones polynomial gives a simple tool to
recognize knots and as such is of great use for biologists (e.g. for analysis of
DNA) and chemists (see for example [SCKSSWW]).
Biographical Notes
We give below a chronological list of selected people mentioned in the article
(compare [B-L-W]):
Gottfried Wilhelm Leibniz (1646-1716)
Heinrich Kuhn (1690-1769)
Leonhard Euler (1707-1783)
Alexandre-Theophile Vandermonde (1735-1796)
Carl Friedrich Gauss (1777-1855)
Thomas Penyngton Kirkman (1806-1895)
Johann Benedict Listing (1808-1882)
Hermann Von Helmholtz (1821-1894)
Gustav Robert Kirchhoﬀ(1824-1887)
William Thomson (Lord Kelvin) (1824-1907)
Peter Guthrie Tait (1831-1901)
James Clerk Maxwell (1831-1879)
Oscar Simony (1852-1915)
Jules Henri Poincar´e (1854-1912)
II.4. JONES REVOLUTION
31
Charles Newton Little (1858-1923)
Hermann Karl Brunn (1862- 1939)
Wilhelm Wirtinger (1865-1945)
Poul Heegaard (1871-1948)
Max Dehn (1878-1952)
Heinrich Tietze (1880-1964)
George David Birkhoﬀ(1884-1944)
James Waddell Alexander (1888-1971)
Mary Gertrude Haseman (1889-1979)
Kurt W. F. Reidemeister (1893-1971)
Ronald M. Foster (1896-1998)
Hidetaka Terasaka (1904-1996)
Herbert Seifert (1907-1996)
Ralph Hartzler Fox (1913-1973).
Bibliography
[A-V]
J. W. Alexander, Letter to Oswald Veblen, 1919, Papers of Oswald
Veblen, 1881-1960 (bulk 1920-1960), Archival Manuscript Material
(Collection), Library of Congress. (I would like to thank Jim Hoste
for providing me with a copy of the letter).
To have a taste of Alexander letter, here is the quotation from the
beginning of the interesting part: “When looking over Tait on knots
among other things, He really doesn’t get very far. He merely writes
down all the plane projections of knots with a limited number of
crossings, tries out a few transformations that he happen to think of
and assumes without proof that if he is unable to reduce one knot to
another with a reasonable number of tries, the two are distinct. His
invariant, the generalization of the Gaussian invariant ... for links
is an invariant merely of the particular projection of the knot that
you are dealing with, - the very thing I kept running up against in
trying to get an integral that would apply. The same is true of his
“Beknottednes”.
Here is a genuine and rather jolly invariant: take a plane projection
of the knot and color alternate regions light blue (or if you prefer,
baby pink). Walk all the way around the knot and ...”
[Al-3]
J. W. Alexander, Topological invariants of knots and links,
Trans. Amer. Math. Soc. 30, 1928, 275-306.
[Amer]
American Men of Science, 1921, 3’rd edition, Edited by Catell,
J.McKeen Brimhall, Dean R. Garrison, NY, The Science
Press.
[Arch]
T. Archibald, Connectivity and Smoke-Rings: Green’s Second
Identity in Its First Fifty Years, Math.Magazine, 62(2) 1989,
219-232.
[Arr]
L. F. Arrian, Anabasis Alexandri, Book II, c.150 AD (English
translation P.A. Brunt, Harvard University Press, 1976).
32
BIBLIOGRAPHY
33
[At]
M. Atiyah, The geometry and physics of knots, Cambridge
Univ. Press, 1990, 75 pp.
[Ba-Wh]
Bambach [Cappel], Carmen, and Lucy Whitaker. ”The Lost
Knots.” Achademia Leonardi Vinci:
Journal of Leonardo
Studies and Bibliography of Vinciana 4 (1991), pp. 107+10,
and unpaginated ﬁgures.
[Ban]
C. Bankwitz,
¨Uber die Torsionszahlen der alternierenden
Knoten, Math. Ann., 103, 1930, 145-161.
[B-L-W]
N. L. Biggs, E. K. Lloyd, R. J. Wilson, Graph theory 1736-
1936, Clarendon Press, Oxford, 1986.
[Birk-1]
G. D. Birkhoﬀ, A determinant formula for the number of ways
of coloring a map, Ann. of Math. (2)14, 1912, 42-46.
[Birk-2]
G. D. Birkhoﬀ, On the polynomial expressions for the number
of ways of coloring a map, Annali, Pisa, Scoula Normali Su-
periore, s.2, v.3 (1934), 85-104. Also in George David Birkhoﬀ
Collected Mathematical Papers, Vol.3, AMS (1950), 29-47.
[Birk-3]
G. D. Birkhoﬀ, Fifty years of American Mathematics, Amer.
Math. Soc., Semicentennial Addresses, v. 2, 1938, 270-315.
Also in George David BirkhoﬀCollected Mathematical Pa-
pers, Vol.3, AMS (1950), 606-651.
[Bi-1]
J. S. Birman, Braids, links and mapping class group, Ann.
Math. Studies 82, Princeton N.J.:
Princeton Univ. Press,
1974.
[Bl]
W. Blaschke, Obituary:
Hermann Brunn. (German) Jber.
Deutsch. Math. Verein. 50, (1940). 163–166.
[Boe-1]
O. Boeddicker, Beitrag zur Theorien des Winkels, Dissertation
G¨ottingen 1876.
[Boe-2]
O. Boeddicker, Erweiterung der Gausschen Theorie der Ver-
schlingungen, Stuttgart, 1876.
[Bog]
M. Bogn´ar, Fundations of linking theory, Akad´emiai Kiad´o,
Budapest 1992.
[B-L-M]
R. D. Brandt, W. B. R.Lickorish, K. C. Millett, A polynomial
invariant for unoriented knots and links, Invent. Math.
84,
1986, 563-573.
34
BIBLIOGRAPHY
[Bre-1]
E. Breitenberger, Gauss und Listing: Topologie und Freund-
schaft. (German) [Gauss and Listing: topology and friendship]
Gauss-Ges. Gvttingen Mitt. No. 30 (1993), 3–56.
[Bre-2]
E. Breitenberger, Johann Benedikt Listing, History of topol-
ogy, 909–924, North-Holland, Amsterdam, 1999.
[Brill]
A. Brill, Math. Ann. 18, 1881.
[Br]
H. Brunn, Topologische Betrachtungen, Zeitschrift f¨ur Math-
ematik und Physik, 37, 1892, 106-116.
[B-Z]
G. Burde, H. Zieschang, Knots, De Gruyter (1985).
[Ch-M]
B. Chandler, W. Magnus, The history of Combinatorial group
theory: A case study in the history of ideas, Studies in the
History of Mathematics and Physical Sciences 9, Springer-
Verlag, 1982.
[Col]
D. Collon, Ancient Near Eastern Art, University of California
Press, Berkeley, Los Angeles, 1995.
[Coom]
Ananda Kentish Coomaraswamy, The iconography of D¨urer’s
”Knots” and Leonardo’s ”Concatenation”, Detroit Institute
of Arts, 1944.
[Com]
Comprehensive Dissertation Index, 1861-1972, Volume 5:
Mathematics and Statistics, Xerox University Microﬁlms,
Ann Arbor, Michigan, 1973.
[Co-1]
J. H. Conway, An enumeration of knots and links, Compu-
tational problems in abstract algebra (ed. J.Leech), Pergamon
Press (1969) 329 - 358.
[Cro]
W. Cr¨onert, Sprachliches zu griechischen ¨Arzten, Archiv f¨ur
Papyrus-forschungen und Vervandte Gebiete, II (1902-1903),
474-482.
[Crowe]
M. J. Crowe, A history of vector analysis: The evolution of
the idea of a vectorial system, Dover Publications, 1994 (ﬁrst
publ. 1967).
[Da]
C. L. Day, Quipus and Witches’ Knots, With a Translation
and Analysis of “Oribasius De Laqueis”, The University of
Kansas Press, Lawrence 1967.
BIBLIOGRAPHY
35
[D-W]
R. Dedekind, H. Weber, Theorie der algebraischen Funktionen
einer Ver¨anderlichen, J. de Crelle, XCII (1882), 181-290. (Also
in R.Dedekind, Ges.Math.Werke,t. I, p. 248-349).
[De-0]
M.
Dehn,
Jahresbericht
der
deutschen
Mathematiker–
Vereinigung, Vol.16, 1907, p.573.
[De-1]
M. Dehn, ¨Uber die Topologie des dreidimensionalen Raumes,
Math. Annalen. 69 (1910), 137-168.
[De-2]
M. Dehn, Die beiden Kleeblattschlingen, Math.Annalen. 75,
1914, 1-12.
[De-3]
M. Dehn, The mentality of the mathematician. A characteri-
zation, Math. Intelligencer, 5(2), 1983, 18–26.
[De-4]
M. Dehn, Papers on group theory and topology. (English)
Translated from the German and with introductions and
an appendix by John Stillwell. With an appendix by Otto
Schreier. Springer-Verlag, New York-Berlin, 1987. viii+396 pp
[D-H]
M. Dehn, P. Heegaard, Analysis situs, Encykl. Math. Wiss.,
vol. III AB3 Leipzig, 1907, 153-220.
[Die]
J. A. Dieudonn´e, A history of algebraic and diﬀerential topol-
ogy 1900-1960, Birkh¨auser, Boston, Basel, 1989.
[Dil]
Dilgendey, Topologische Studien, Leipzig, 1890.
[D-T]
C. H. Dowker, M. B. Thistlethwaite, Classiﬁcation of knot
projections, Topology and its applications 16, 1983, 19-31.
[Dun]
G. W. Dunnington, Carl Friedrich Gauss, Titan of Science,
Hafner Publishing Co., New York, 1955.
[Dur-1]
Albrecht Durer Master Printmaker, Department of Prints and
Drawings, Boston Museum of Fine Arts, Hacker Art Books,
New York, 1988.
[Dur-2]
Albrecht Durer, Diary of his Journey to the Netherlands,
1520-1521, translated by P.Trou, edited by J.A.Goris and
G.Marlier, London, Lund Humphries, 1971.
[EIS]
Encyclopedia of Integer Sequences (on-line),
http://www.research.att.com/∼njas/sequences/A002864
[Ep]
M. Epple, Geometric aspects in the development of knot the-
ory, History of topology (ed. I.M.James) , 301–357, North-
Holland, Amsterdam, 1999.
36
BIBLIOGRAPHY
[Ep-1]
M. Epple, Die Entstehung der Knotentheorie (Braunschweig,
1999).
[Eu]
L. Euler, Solutio problematis ad geometriam situs pertinentis,
Commentarii Academiae Scientiarum Imperialis Petropoli-
tanae 8, 1736, 128-140.
[Falc]
W. Falconer, A universal dictionary of the marine, London
1769.
[F-1]
R. H. Fox, A quick trip through knot theory, In: Top. 3-
manifolds, Proc. 1961 Top.Inst.Univ. Georgia (ed. M.K.Fort,
jr), 120-167. Englewood Cliﬀs. N.J.: Princeton-Hall, 1962.
[FYHLMO]
P. Freyd, D. Yetter, J. Hoste, W. B. R. Lickorish, K. Millett,
A. Ocneanu, A new polynomial invariant of knots and links,
Bull. Amer. Math. Soc., 12, 1985, 239-249.
[Ga-1]
C. F. Gauss, Notebooks, Old library in G¨ottingen.
[Ga-2]
K. F. Gauss, Zur mathematischen Theorie der electrody-
namischen Wirkungen, 1833, Werke, K¨oniglichen Gesellschaft
der Wissinchaften zu Gottingen, 5, 1877, 602-629.
[Gor]
C. McA. Gordon, Some aspects of classical knot theory, In:
Knot theory, L.N.M. 685, 1978, 1-60.
[Gor-1]
C. McA. Gordon, 3-dimensional topology up to 1960. History
of topology (ed. I.M.James), 449–489, North-Holland, Ams-
terdam, 1999.
[G-Lu]
C. McA. Gordon, J. Luecke, Knots are Determined by their
Complements, Bulletin of the A.M.S, 20, 1989, 83-87.
[Grg]
E. Grgeta, Simony knots, and continued fractions, Senior The-
sis, George Washington University, 1988.
[Gr-1]
P. van de Griend, The history of knot theory, preprint 18,
Aarhus University, April 1992.
[Gr-2]
P. van de Griend, Notes on Knots, ˚Arhus, March 1993.
[Gr-3]
P. van de Griend, A history of topological knot theory; History
and science of knots, 205–260, Ser. Knots Everything, Vol. 11,
World Sci. Publishing, River Edge, NJ, 1996.
[T-G]
J. C. Turner, P. van de Griend, Ser.Knots Everything, Vol.
11, World Sci. Publishing, River Edge, NJ, 1996.
BIBLIOGRAPHY
37
[G-S]
B. Gr¨unbaum, G. C. Shephard, Interlace patterns in Islamic
and Moorish art, ”The Visual Mind - Art and Mathematics”.
Edited by Michele Emmer, MIT Press (1993); Chapter 22,
147-155. (Articles from “Leonardo”).
[Ha]
F. Harary, The knots and links of Albrecht D¨urer, Atti Accad.
Pontaniana (N.S.) 34, 1985, 97-106.
[H-K-W]
P. de la Harpe, M. Kervaire, C. Weber, On the Jones polyno-
mial, L’enseignement Math´ematique, 32 (1986), 271-335.
[Has-1]
M. G. Haseman, On knots, with a census of the amphicheirals
with twelve crossings, Trans. Roy. Soc. Edinburgh, 52 (1917),
235-255 (also Ph.D thesis, Bryn Mawr College, 1918 [Com]).
[Has-2]
M. G. Haseman, Amphicheiral knots, Trans. Roy. Soc. Edin-
burgh 52, 1918 597-602.
[Has-3]
M. G. Haseman, Obituary, Linton Daily Citizen Newspaper,
April 10, 1979.
[Hea]
M. C. Heath, ”Early Helladic Clay Sealings from the House
of the Tiles at Lerna,” Hesperia 27, 1958, 81-120.
[Heeg]
P. Heegaard, Forstudier til en Topologisk Teori for de alge-
braiske Fladers Sammenhæng, København, 1898, Filosoﬁske
Doktorgrad; French translation:
Sur l’Analysis situs, Soc.
Math. France Bull., 44 (1916), 161-242.
[Helm]
H. Helmholtz, ¨Uber Integrale der hydrodynamischen Gle-
ichungen,
Welche
den
Wirbelbewegungen
entsprechen,
Crelle’s Journal f¨ur Mathematik, 55, 1858, 25-55; English
translation by P.G.Tait: Philosophical Magazine, June 1867,
485-511.
[Hemion]
G. Hemion, The classiﬁcation of knots and 3-dimensional
spaces, Oxford University Press, 1992.
[He]
Heraklas, ﬁrst century A.D., included in Oribasius ”Medical
collections”, fourth century A.D.
[Hig]
R. Higgins, Minoan and Mycean art, Thames and Hudson,
1997 (Revised edition).
[Hind]
A. M. Hind, Two Unpublished Plates of the Series of Six
“Knots” Engraved after designs by Leonardo Da Vinci, The
Burlington Magazine for Connoisseurs, Vol. 12, No. 55, Oc-
tober 1907, 41-43.
38
BIBLIOGRAPHY
[Ho]
C. F. Ho, A new polynomial for knots and links; preliminary
report, Abstracts AMS 6(4), 1985, p. 300.
[H-W]
B. Hopkins, R. J. Wilson, The Truth about Konigsberg, ⁀The
College Mathematics Journal, May 2004, 198-207.
[Hos-2]
J. Hoste, e-mails, 2 and 7 Sept. 1993, and 9 June 1994.
[Hos-20]
J. Hoste, The enumeration and classiﬁcation of knots and
links, in W. Menasco and M. Thistlethwaite (eds.) Handbook
of Knot Theory; Amsterdam: Elsevier, 2005, 209-232.
[H-T]
J. Hoste, M. Thistlethwaite, J. Weeks, The First 1701936
Knots, Math. Intell., 20(4), 1998, 33-48
[Hur]
A. Hurwitz,
¨Uber Riemannsche Fl¨achen mit gegebenen
Verzweigung spunkten, Math. Annalen, 39, 1891, 1-61.
[Jan]
A. Januszajtis, Scientists in Old Gdansk: 17th and 18th Cen-
turies (From the history of science in ancient Gdansk), Task
Quarterly 5(3), 2001, 389-399.
http://www.pg.gda.pl/archiwalne/januszajtis/2000/III.PDF
[Jo-0]
V. F. R. Jones. Letter to J.Birman, May 31, 1984.
[Jo-1]
V. F. R. Jones. A polynomial invariant for knots via Von
Neuman algebras, Bull. Amer. Math. Soc 12 (1985) 103-111.
[Jo-2]
V. F. R. Jones. Hecke algebra representations of braid groups
and link polynomials, Ann. of Math. 126(2), 1987, 335-388.
[Jo-6]
V. F. R. Jones, Knot theory and statistical mechanics, Scien-
tiﬁc American, 263, November, 1990, no. 5, 4, 98–103.
[K-3]
L. H. Kauﬀman, On Knots, Princeton University Press, 1987.
[K-5]
L. H. Kauﬀman, An invariant of regular isotopy, Trans. Amer.
Math. Soc., 318(2), 1990, 417–471.
[K-6]
L. H. Kauﬀman, State models and the Jones polynomial,
Topology 26, 1987, 395-407.
[K-8]
L. H.Kauﬀman, Formal knot theory, Mathematical Notes 30,
Princeton University Press, 1983.
[Ken]
A. E. Kennelly, The equivalence of triangles and three-pointed
stars in conducting networks, Electrical World and Engineer,
34, 1899, 413-414.
BIBLIOGRAPHY
39
[Kir]
G. R. Kirchhoﬀ, ¨Uber die Auﬂosung der Gleichungen, auf
welche man bei der Untersuchung der linearen Vertheilung
galvanischer strome gef¨uhrt wird, Annalen d. Physik und
Chemie 72, 1847, 497-508.
[Kirk-1]
T. P. Kirkman, The enumeration description and construc-
tion of knots with fewer than 10 crossing, Trans. R. Soc. Ed-
inburgh, 32, 1885, 281-309.
[Klein]
F. Klein, Mathematische Annalen, IX, 478.
[Kli]
M. Kline, Mathematical Thought from Ancient to Modern
Times, Oxford University Press, 1972.
[Kno]
C. G. Knott, Life and Scientiﬁc work of Peter Guthrie Tait,
Supplementing the two volumes of scientiﬁc papers published
in 1898 and 1900, Cambridge University Press, 1911.
[Kur]
The complete woodcuts of Albrecht D¨urer, Edited by Dr. Willi
Kurth, Dover publications, Inc. New York, 1983 (translated
from 1927 German edition).
[Leh]
D. M. Lehmer, Obiturary of Charles Newton Little, Science,
Vol. LVIII, No. 1508, October 1923, N.Y. City, the Science
Press.
[Lei]
G. W. Leibniz, Math. Schriften, 1 Abt., Vol 2, 1850, 19-20.
[Lis]
J. B. Listing, Vorstudien zur Topologie, G¨ottinger Studien
(Abtheilung 1) 1, 1847, 811-875.
[Lit-0]
C. N. Little, On knots, with a census for order 10, Trans.
Connecticut Acad. Sci., 18, 1885, 374-378 (also Ph.D. thesis,
1885, Yale University [Com]).
[Lit-1]
C.
N.
Little,
Non-Alternate
±
Knots,
Trans.
Royal.
Soc.Edinburgh, XXXIX (part III(No.30) - for sessions 1898-
99), 1900, 771-778. (Communicated by Professor Tait. (With
three plates). (Read July 3, 1899).
[Lit-2]
C. N. Little, Non-Alternate knots of order eight and nine,
(1889), Trans. Royal. Soc.Edinburgh, XXXV 1890,
[Lit-3]
C. N. Little, Alternate ± Knots of order eleven, (read 21st
July; revised December 1890), Trans. Royal. Soc.Edinburgh,
XXXVI 1892, 235-255.
40
BIBLIOGRAPHY
[Lom]
S. L. Lomonaco, The modern legacies of Thomson’s atomic
vortex theory in classical electrodynamics, Proceedings of
Symposia in Applied Mathematics, Vol. 51, 1996, 145-166.
[Mac]
E. MacCurdy, The Notebooks of Leonardo, New York: Reynal
and Hitchcook, 1938, vol.2, p.588.
[Mag]
W. Magnus, Max Dehn. Math. Intelligencer 1 (1978), 132–
143. (Also in: Wilhelm Magnus Collected Paper, Edited by
G.Baumslag and B.Chandler, Springer-Verlag, 1984).
[Max]
J. C. Maxwell, A treatise on electricity and magnetism, Oxford
2 (1873).
[M-T-1]
W. M. Menasco, M.B.Thistlethwaite, The Tait Flyping Con-
jecture, Bull. Amer. Math. Soc. 25 (2), 1991 403-412.
[M-T-2]
W. M. Menasco, M.B.Thistlethwaite, The classiﬁcation of al-
ternating links, Annals of Math., 138, 1993, 113-171.
[Mey]
Fr. Meyer, Dissertation, M¨unchen 1878. Also Edinb. Proc., 13,
1886.
[Mi]
L. G. Miller, The earliest(?) description of a string ﬁgure, The
American Anthropologist, XLVII (1945), 461-462.
[M-M]
E. S. Munkholm, H. J. Munkholm, Poul Heegaard (ed.
I.M.James), History of topology, 925–946, North-Holland,
Amsterdam, 1999.
[M-4]
K. Murasugi, Jones polynomial and classical conjectures in
knot theory, Topology, 26(2), 1987, 187-194.
[Ol]
L. Olesko (ed.), Science in Germany, Osiris (2nd series) 5
(1989).
[Per-0]
Perko, Kenneth A., Jr. On the classiﬁcation of knots, Proc.
Amer. Math. Soc., 45 (1974), 262–266.
[Per-1]
K. A. Perko, NAMS 25(6), 1978.
[Per-2]
K. A. Perko, Primality of certain knots, Topology Proceedings,
vol. 7, 1982, 109-118.
[Per-3]
K. A. Perko, Invariants of 11-crossing knots, Publications
Math. d’Orsay, 1980.
[Plu]
Plutarch of Chareonera, The age of Alexander, translated by
I. Scott-Kilvert, Penguin Books, 1982.
BIBLIOGRAPHY
41
[Pogg]
Poggendorﬀ’s Biographisch Literarisches Handw¨orterbuch,
Vol. 3, 1858-83 (A-Z), 1898.
[Po-1]
H. Poincar´e, Analysis Situs (&12), Journal d’Ecole Polytech-
nique Normale, 1 (1895), 1-121.
[Po-2]
H. Poincar´e, First Compl´ement `a l’analysis situs, 1899; in
Œuvres, vol VI, Gauthier-Villars, Paris, 1953.
[P-1]
J. H. Przytycki, Survey on recent invariants in classical knot
theory, Uniwersytet Warszawski, Preprinty 6,8,9; 1986. (the
third chapter of this book is based on [P-1]).
[P-5]
J. H. Przytycki, Skein modules of 3-manifolds, Bull. Ac. Pol.:
Math.; 39(1-2), 1991, 91-100.
[P-13]
J. H. Przytycki, History of the knot theory from Vander-
monde to Jones, Aportaciones Matem´aticas Comunicaciones,
11, 1992, 173-185.
[P-18]
J. H. Przytycki, Teoria w¸ez l´ow: podej´scie kombinatoryczne,
(Knots: combinatorial approach to the knot theory), Script,
Warsaw, August 1995, 240+XLVIIIpp.
[P-19]
J. H. Przytycki, Algebraic topology based on knots: an in-
troduction, Knots 96, Proceedings of the Fifth International
Research Institute of MSJ, edited by Shin’ichi Suzuki, World
Scientiﬁc Publishing Co., 1997, 279-297.
[P-21]
J. H. Przytycki, Classical roots of Knot Theory, Chaos, Soli-
tons and Fractals, Vol. 9 (No. 4-5), 1998, 531-545.
[P-22]
J. H. Przytycki, Knot theory from Vandermonde to Jones,
with the translation of the topological part of Poul Heegaard
Dissertation: Forstudier til en topologisk teori for de alge-
braiske ﬂaders sammenh[ae]ng, København 1898, Filosoﬁsk
Doktorgrad (Preliminary studies towards the topological the-
ory of connectivity of algebraic surfaces), by A. H. Przy-
byszewska, Preprint 43, Odense University 1993.
[P-29]
J. H. Przytycki, From 3-moves to Lagrangian tangles and
cubic skein modules, Advances in Topological Quantum Field
Theory, Proceedings of the NATO ARW on New Techniques
in Topological Quantum Field Theory, Kananaskis Village,
Canada from 22to 26 August 2001; Ed. John M. Bryden,
42
BIBLIOGRAPHY
October 2004,
e-print: http://front.math.ucdavis.edu/math.GT/0405248
[P-35]
J. H. Przytycki, The interrelation of the Development of
Mathematical Topology in Japan, Poland and USA: Notes to
the early history of the Knot theory in Japan, Annals of the
Institute for Comparative Studies of Culture, TWCU, Vol.
63, 2002, 61-86;
e-print: http://front.math.ucdavis.edu/math.HO/0108072
[P-T-1]
J. H. Przytycki, P. Traczyk, Invariants of links of Conway
type, Kobe J. Math. 4 (1987) 115-139.
[Ra]
J. Raeder, Oribassi Collectionum Medicarum Reliquiae, 4 vol-
umes, Leipzig and Berlin, 1928-1933.
[Re-2]
K. Reidemeister, Knotentheorie. Ergebn. Math. Grenzgeb.,
Bd.1; Berlin:
Springer-Verlag (1932) (English translation:
Knot theory, BSC Associates, Moscow, Idaho, USA, 1983).
[R-T-2]
N. Y. Reshetikhin, V.Turaev, Invariants of three manifolds
via link polynomials and quantum groups. Invent. Math. 103
(1991) 547-597.
[Ro-1]
D. Rolfsen, Knots and links, Publish or Perish, 1976 (second
edition, 1990).
[SSW]
H. Sachs, M. Stiebitz, R. J. Wilson, An Historical Note - Euler
Konigsberg Letters, Journal of Graph Theory, 12 (1), 1988,
133-139.
[Sar]
G. Sarton, Ancient Science through the Golden Age of Greece,
Dover Pub., 1993 (ﬁrst edition: Harvard Univ. Press, 1952).
[Sar-2]
G. Sarton, Introduction to the history of science, Baltimore:
Williams and Wilkins, 1927-1948; (quotation from Vol. 1
p.216).
[Sha]
H. I. Sharlin, T.Sharlin, Lord Kelvin, the dynamic Victorian,
Penn. State University Press, 1979.
[She]
R. B. Sher, Max Dehn and Black Mountain College, Math.
Intelligencer 16(1), 1994, 54–55.
[Sil]
R.
H.
Silliman,
William
Thomson:
smoke
rings
and
nineteenth-century atomism, Isis, 54, December 1963, 472-.
BIBLIOGRAPHY
43
[Sim]
O. Simony, ¨Uber eine Reihe neuer Thatsachen aus dem Gebi-
ete der Topologie, Math. Annalen, 19 (1882), 110-120, and 24
(1884), 253-280.
[Stac]
P. St¨ackel, Gyuss als Geometer, in the X’th Volume of Gauss’
Collected Works..D.
[Stil]
J. Stillwell, Classical Topology and Combinatorial Group The-
ory, Grad. Texts in Math. 72, Springer-Verlag 1980.
[Str]
D. J. Struik, A concise history of mathematics, Dover Publi-
cations, Inc. New York, 1967.
[SCKSSWW] D. W. Sumners (Editor), N. R. Cozzarelli, L. H. Kauﬀman,
J. Simon, D. W. Sumners, J. H. White, S. G. Whittington,
New Scientiﬁc Applications of Geometry and Topology, Pro-
ceedings of Symposia in Applied Mathematics, Vol. 45, AMS
1992.
[Ta-0]
P. G. Tait, Some elementary properties of closed plane curves,
Messenger of Mathematics, New Series, No.69, 1877, (com-
municated at the 1876 Meeting of the British Association).
Reprinted in Scientiﬁc Papers of P. G. Tait, 270-272.
[Ta]
P. G. Tait, On knots I, II, III, Scientiﬁc Papers, Cambridge
University Press, 1898-1900. Including: Trans. R. Soc. Edin.,
28, 1877, 35-79. Reprinted by Amphion Press, Washington
D.C., 1993.
[Ta-1]
P. G. Tait, Johann Benedict Listing, Nature, February 1, 1883.
Reprinted in Scientiﬁc Papers of P.G.Tait.
[Ta-2]
P. G. Tait, Listing’s Topologie (Introductory address to the
Edinbutgh Mathematical Society, November 9, 1883), Philo-
sophical Magazine, January, 1884. Reprinted in Scientiﬁc Pa-
pers of P.G.Tait.
[This-1]
M. B. Thistlethwaite, Knot tabulations and related topics,
Aspects of topology, LMS Lecture Notes Series, 93 (1985), 1-
76.
[This-3]
M. B. Thistlethwaite, A spanning tree expansion of the Jones
polynomial, Topology, 26 (1987), 297-309.
[Thomp]
S. P. Thompson, The life of William Thomson: Baron Kelvin
of Largs, 2 vols., London: Macmillan, 1910.
44
BIBLIOGRAPHY
[Thomps]
D’A. W. Thompson, On Growth and Form, Dover Publica-
tions, 1992 (republication of “A New Edition” by Cambridge
University Press, 1942; “I wrote this book in wartime, and its
revision has employed me during another war”.)
[Thom]
J. J. Thomson, A treatise on the motion of vortex rings, The
Adams prize in 1882, (published in 1883).
[Thoms]
W. H. Thomson (Kelvin), On vortex motion, Trans. R. Soc.
Edin., 25 (1867), 217-260. See also Proceedings of the Royal
Society of Edinburgh, February 1867.
[Ti-1]
H. Tietze, ¨Uber die topologischen Invarianten mehrdimen-
sionaler Mannigfaltigkeiten, Monatshefte f¨ur Mathematik and
Physik 19, 1908, 1-118.
[Ti-2]
H. Tietze,
¨Uber Simony-Knoten und Simony-Ketten mit
vorgeschriebenen singul¨aren Primzahlen f¨ur die Figur und f¨ur
ihr Spiegelbild, Math. Zeitschrift, 49, 1943, 351-369.
[Tu-2]
V. G. Turaev, The Conway and Kauﬀman modules of the solid
torus, Zap. Nauchn. Sem. Lomi 167 (1988), 79-89. English
translation: J. Soviet Math. 52, 1990, 2799-2805.
[Tu-Vi]
V. G. Turaev, O.Y.Viro, State sum invariants of 3-manifolds
and quantum 6j-symbols, Topology, 31 (1992), 865-902.
[Tu-We]
V. G. Turaev, H.Wenzl, Quantum invariants of 3-manifolds as-
sociated with classical simple Lie algebras, Internat. J. Math.,
4(2), 1993,323-358.
[Tut-1]
W. T. Tutte, A ring in graph theory, Proc. Cambridge Phil.
Soc., 43, 1947, 26-40.
[Va]
A. T. Vandermonde, Remarques sur les probl`emes de situ-
ation, M´emoires de l’Acad´emie Royale des Sciences (Paris)
(1771), 566-574.
[Weil]
A. Weil, Riemann, Betti and the birth of topology, Arch. for
Hist. Exact Sci., 16, 1979, 91-96.
[Web]
C. Weber, A stroll through knot theory, New. J. Chem., 17
(1993), 627-644.
[Weith]
H.
Weith,
Topologische
Untersuchung
der
Kurven-
Verschlingung, Inaugural Dissertation, Z¨urich 1876.
BIBLIOGRAPHY
45
[Whit-1]
H. Whitney, The coloring of graphs, Ann. of Math., 33, 1932,
688-718.
[Wh]
W. Whitten, Knot complements and groups, Topology, 26,
1987, 41-44.
[Wie]
M. H. Wiencke, “Further Seals and Sealings from Lerna,” Hes-
peria 38, 1969, 500-521.
[Wir]
W. Wirtinger,
¨Uber die Verzweigungen bei Funktionen
von zwei Ver¨anderlichen, Jahresbericht d. Deutschen Math-
ematiker Vereinigung, 14 (1905), 517. (The title of the talk
supposedly given at September 26 1905 at the annual meet-
ing of the German Mathematical Society in Meran).
[Wit]
E. Witten, Quantum ﬁeld theory and the Jones polynomial,
Comm. Math. Phys., 121, 1989, 351-399.
[Wo-Kr]
D. Wolkstein, S. N. Kramer, Inanna: Queen of heaven and
earth, Harper Collins Publisher, 1983.
[Yale]
Yale University, Obituary Record of graduates deceased dur-
ing the year ending July 1, 1924, New Haven (Published by
the University), 1924, p.1211.
Dept. of Mathematics, Old Main Bldg., 1922 F St. NW
The George Washington University, Washington, DC 20052
e-mail: przytyck@gwu.edu
46
BIBLIOGRAPHY
Appendix: Preface to P. Heegaard thesis of 1898
Poul Heegaard (1871-1948) is well known to topologists because of his theorem
about decomposition of any 3-manifold into two handlebodies. His achievements
in knot theory are much less known.41 One of the reasons for this was the fact
that his 1898 Doctoral Dissertation [Heeg] was written in Danish. It was translated
into French only 18 years later. I learned of the Heegaard work on knots only from
the book by J. C. Stillwell [Stil]. When visiting Odense University (1992-1994), I
had a privilege to have every day access to a copy of Heegaard dissertation and
I was lucky to know very gifted high school student, Agata Przybyszewska, who
kindly agreed to translate parts of the dissertation. We present here the Przy-
byszewska’s translation (from Danish) of the Preface, and the section 6 and 7 of
Heegaard’s Dissertation. The second, topological part of the dissertation is trans-
lated by Przybyszewska in [P-22] (references in the main part of the chapter). One
can hope that the whole Dissertation will be translated soon. As to importance of
Heegaard results we can best quote from the Stillwell book [Stil]:
“Heegaard’s results lay dormant (although noted by Tietze 1908) until the publi-
cation of the French translation of his thesis in 1916. The translation was checked
for mathematical soundness by J.W.Alexander, fresh from his work on homology
groups, and we may surmise that the collision of these ideas led to the fruitful
discoveries which were to follow. Alexander must also have read Tietze 1908 at
this time, because in short order he disposed of two of the most important of Ti-
etze’s conjectures: Alexander 1919a42 shows that there are nonhomeomorphic lens
spaces with the same group, while Alexander 1919b43 proves that any orientable
3-manifold is a branched cover of S3. Later in 1920 he ﬁnally took the cue from
Heegaard’s example and looked for torsion in cyclic covers of S3 branched over
various knots.”
41The only, known to me, research papers on topology by Heegaard are [D-H, Heeg].
For other Heegaard’s work see his bibliography (Brjan Toft found the box donated to
Odense Math. Dept. by Niels Erik Nørlund (1885-1981) with Heegaard papers (as in the
Heegaard’s bibliography except [D-H] and only French version of [Heeg]).
42Note on two three-dimensional manifolds with the same group, Trans. Amer. Math.
Soc., 20 (1919), 339-342.
43Note on Riemann spaces, Bull. Amer. Math. Soc., 26 (1919), 370-372.
BIBLIOGRAPHY
47
Preliminary studies towards the topological theory of
connectivity of algebraic surfaces.
Poul Heegaard
Copenhagen, 1898
1. Preface
It is commonly known, which development took the theory of functions of one
independent variable, when the imaginary values of the independent variable were
considered and the theory became linked with a geometrical presentation of the
imaginary numbers.
When we shall construct a theory of functions with two independent variables,
it will therefore be natural to look for a similar presentation. The fact that such
a long time has lapsed before the work on this quite natural generalization was
started can, among other reasons, be explained by the fact that the examinations
with two independent variables are a lot more diﬃcult than with one. The variety
of possibilities produces conditions, for which there is no analogy in the theory of
one independent variable. Picard observes thus:
“ On voit, par ce qui pr´ec`ede, les diﬀ´erences profondes qui separent la th´eorie
des fonctions alg´ebrique d’une variable de la th´eorie de fonctions alg´ebriques de
deux variables ind´ependantes. L’analogie qui souvent est un guide excellent, peut
devenir ici bien trompeuse.”44
Another diﬃculty on the way towards a lucid presentation is of course the fact
that the geometrical structures that should play the part of the Riemann surfaces
are 4-dimensional.
Even if the analogy can be misleading in our examination of the details, then a
survey of the methods employed in the theory of one independent variable will give
us a good working program for such a study. Let us then present such a survey.
The theory of functions with one independent variable is very closely connected
with the theory of the algebraic curves. The geometry of such a curve becomes
therefore of fundamental importance.
The examinations are set up from quite a diﬀerent points of view. The most
important made use of:
1. the elementary algebraic theorems. Among these we can mention
(a) Examination of the adjoint polynomials, created by Brill and N¨other in the
paper: Ueber die algebraischen Functionen (M.A. vol. 7, 1873).
(b) The examinations of the linear groups of points made by Italians.
They
have tried to liberate the former theory from its projective form, so they
44We see from the proceeding the important diﬀerences that separate the theory of al-
gebraic functions of one variable from the theory of algebraic functions of two independent
variables. The analogy that often is an excellent guide, can just as well be faulty.
48
BIBLIOGRAPHY
could develop it independently of such concepts as degree, class e.t.c., cf. a
summary by Castelnuovo and Euriques (Sur quelques recent resultantas dans
la th’eorie des surfaces alg´ebriques. M.A. vol. 48, p.242, 1897)
(c) Number-geometrical examinations, especially a number of papers by Zeuthen
(e.g. M.A. vol.3 and vol. 9)
2. the examinations of the algebraic curves which belong to the transcendental
functions. These examinations originate from Riemann’s pioneer work (1857) are
well known, so there is no reason to mention them any further.
3. the topological examinations of the Riemann surfaces that represent the algebraic
curve. Here once again two diﬀerent approaches were chosen:
(a) We can either determine the connectivity number of surfaces using a theorem
which we can regard as a generalization of Euler’s theorem about polyhedra
(Riemann, Neumann).
(b) Or we can puncture the Riemann surface and next bring it by continuous
deformation into a normal form. As far as we can tell this approach was only
implemented by Jul. Petersen (Foreleasninger over Funktionsteori, chapter
IV). Listing uses indeed such a procedure in shaping the “diagram” of a
spatial ﬁgure in hereby arriving to a generalization of Euler’s theorem (Census
r¨aumlicher Complexe, 1862), and Betti (1871) uses such a consideration in
his examinations of the connectivity number of a n-dimensional space in
generality, but both of these papers seem to have been unnoticed for a long
time. This method gives us a remarkably lucid presentation of the discussed
situation.
The transformations of algebraic surfaces play an analogous part to the theory of
functions of two variables. There already exist an amount of works - especially from
recent times - in which the problem is treated from points of view that correspond
to these enumerated here.
1. Elementary algebraic examinations.
(a) Adjoint polynomials. This theory originates from Clebsch (C.R. Dec. 1868)
an N¨other (Zur aindeutigen Entsprechen... I & II, M.A. vol.2, 1869 and vol.8,
19874)
(b) Linear systems of curves. The Italians have created a theory of linear systems
of curves on surfaces that is analogous with the before mentioned theory of
groups of points on curves. By means of this the invariants of surfaces can
be determined (cf. the mentioned summery by Castelnuevo and Enriques).
(c) Surface transformations have also been examined by Zeuthen from the num-
ber geometrical point of view (´Etudes g´eom’etriques..., M.A. vol.4).
2. Examinations by transcendent functions. Already in his paper in M.A. vol. 2
N¨other considers the integrals of the form:
Z Z Q(xyz)dxdy
f ′x
BIBLIOGRAPHY
49
Picard introduces the integrals of the form:
Z xyz
x0y0z0
Pdx + Qdy
Where P and Q satisfy the condition of integrability (Liouville Journ. 1885&1886).
Finally, Picard has in his prized paper (Memoire sur la the´orie des fonctions alg´ebriques
de deux variables (Liouv. Journ. series 4. vol. 5, 1889) and in the recently printed
book on the same subject (Picard at Simart: Th´eorie des fonctions alg´ebriques de
deux variables ind´ependantes, 1987)) given a coherent presentation of the whole
theory.
Poincar´e’s paper ”Sur les residus...” (Acta mathematica, vol. 9, 1887) should also
be mentioned here.
3.
Topological examinations.
This direction it is almost empty.
In the works
of Picard there is a lot, but none of it is carried through, as he whenever possible
prefers the analytical presentation. The whole trouble is that the Riemann-Betti
theory of connectivity numbers is very insuﬃcient and diﬃcult to use when we
speak of manifolds of more than 2 dimensions. Poincar´e has tried to complete it
(Analysis Situs, Journ, de l’´ecole polit´echnique, series 2. Cah. 1. 1895) without
succeeding, according to our opinion. Later Picard has given his share: W. Dyck
has already before worked on the problem (Beitri¨age sur Analysis situs, M.A. vol.
32 and 37), but a quite satisfying theory can not be found anywhere.
Previous to the examination in this direction, we therefore need to have a theory
of topological correspondence of manifolds of dimension greater than 2.
What
already does exist in this direction, can be compared to that what is mentioned in
3(b).
The following pages contain no uniﬁed totality, only a study of the problem; its
diﬃculty can be used as an excuse therefore. To let the examinations be considered
as they should be, it will perhaps be a good idea to advance a line of thought that
have been the guide of my examinations.
By accident I have noticed that the Zeuthen-Halphen generalization of the
genus theorem could be proved by a pure topological argument; namely, for any
two Riemann surfaces, for which we assume a µ −ν value-correspondence between
their points, we can construct new Riemann surfaces, which correspond bijectively
to each other. The equation, which says that two constructed surfaces have equal
connectivity number, states exactly the mentioned theorem. The fact, which is
so important to the enumerative geometry, that the generalized genus theorem
can be used without inﬁnitesimal examinations of the coincident points (or their
substitutes), while these examinations are necessary when using the other formulas
of correspondence (cf. Acta mathem., vol. 1, p. 171) let us see these circumstances
in a new light. As I have found later the proof in a paper written by Hurwitz (M.A.
vol. 39), I shall not go into details of the proof here.
50
BIBLIOGRAPHY
My thought was that it could be possible to construct a theorem similar to that
for the algebraic surfaces, but before that a lot of work ought to be done: there
should be created something for algebraic surfaces that could correspond to the
Riemann surfaces of algebraic curves; next topological criteria for their unique cor-
respondence should be advanced. And, as it is already mentioned, the material for
such an examination that already existed was either insuﬃcient or full of mistakes.
It was in trying to correct these mistakes, and to ﬁll up the gaps, that the contents
of the following pages originated.
Second part
On topological connectivity numbers
6 Topology.
Descartes’ analytical method was presumably a universal method for solving geo-
metrical problems, but as a rule it gives constructions that are far behind the Greeks
in simplicity and elegance. During his attempts of penetrating the principles of the
curious geometrical analysis, Leibniz formulated a number of observations, which he
called Analysis situs or Geometria situs. Analysis situs or Geometria situs. (Leib-
nizens gesammelte Werke herausg. von G. H. Pertz,1858, mathematische Schriften
vol. 1, p. 178: De analysi situs). Sometimes in connection with this, Leibniz has
been named the father of the modern topology: i.e. the branch of mathematics,
which aims at the qualitative properties of the objects analyzed without occupying
itself with the quantities and the metrics. Leibniz notices somewhere on the occa-
sion of his theory:45
“Figura in universum praeter quantitatem continet qualitatem seu formam,”
but in reality his theory has no points of similarity with what we today understand
as topology. In the recent times the mathematicians became interested in a lot of
topological problems. It should be enough to remind oneself of
• the studies of topological knots, nets, and the like by Tait or Simony;
• the graphs;
• the appearance of the graphical curves; the problem of colorings, and hereby
separating, the countries on a map by means of 4 diﬀerent colors;
• the problem of folding a stamp
• and “last but not least” of the extensive attempts to make a theory of the
connectivity numbers of the n-dimensional manifolds, and of generalizing
Euler’s theorem of polyhedra – 2 attempts that are closely connected.
(A good survey of the literature can be found in (W.Dyck: Beitr¨age zur Analysis
45A ﬁgure generally contains besides an extent (quantitas) a nature (qualitas) or form.
BIBLIOGRAPHY
51
situs, M.A. vol. 32)). The usage is somewhat staggering, but it is most fair to
reserve the name ‘analysis situs’ for the last mentioned kind of studies, and against
it, to use the name ‘topology’ about all research of qualitative nature, as Listing
has proposed it (Vorstudien zur Topologie).
7 Analysis situs.
Presumably, it will be very diﬃcult to formulate basic theorems about the con-
nectivity in n-dimensional manifolds; anyhow it will probably be a good idea, if we
did study the concrete cases in more details, than it has been done so far, instead
of going at the whole matter in its abstract generality. In theory, the logic should
be enough to ensure the development of mathematics, but practice shows us, what
a mighty lever is the sense of tact that develops when a theory is applied to a large
class of the concrete cases; even if a theory appears to be very logical and plausible,
it can very easily contain mistakes that will only be revealed when it is additionally
controlled by the understanding.
Riemann and Betti are the ﬁrst who have tried to generalize the theory of
connectivity of surfaces, which Riemann himself with great luck has applied to the
theory of Abelian integrals. After Riemann’s death Betti put forward a paper on
the mentioned subject (Sugli spazi di un numero qualanque di dimensioni, Ann. di
matem. series 2, vol. 4, 1871). He does not speak of any collaboration between
himself and Riemann; but we judge from the fragments of the theory, which Weber
has collected together from notes that Riemann wrote down (Riemann: Gesammelte
mathematische Werke, 2. Auﬂ. fragment XXIX), that Riemann has contributed
essentially during his stay in Italy (Ges. Werke, p.555) to the thoughts that are
found in Betti’s paper. It is where the deﬁnition can be found of the connectivity
numbers of the manifolds of dimensions greater than 2. Later, diﬀerent people have
tried to improve and complete the theory:
• Dyck in ”Beitr”age zur Analysis situs”(M.A. vol. 32 and vol.37),
• Poincar´e in the paper “Analysis Situs”, and
• Picard in his studies of functions of two variables (see p.5)
Even before I knew the last mentioned works, I have decided to try another
way than the one of Riemann-Betti that is to say, an attempt to generalize Jul.
Petersen’s puncture method which I recalled from lectures. (I became acquainted
with Listing’s “Diagram” and “Trema” a long time after, and the same goes for
the studies by Betti, which are related to this subject, and which I until lately only
have known from the short summary in “Fortshritteder Mathematik”).
Among
other things it seemed awkward to me that the n connectivity numbers were not
adequate for a topological characterization of a manifold when n > 2. When I
became acquainted with the papers that I’ll mention later, especially that one of
Poincar´e, I started to doubt about the rightness of my choice, as I compared the
elegant methods that I met there, with the somewhat clumsy and awkward theory
52
BIBLIOGRAPHY
that I myself was working on; but then I thought to have discovered that the patch,
which I have chosen, would illuminate some circumstances that would not appear
clearly by means of the other method, and because I held a method in my hands to
ﬁnd suﬃcient criteria for the equivalence of n-dimensional manifolds, so I decided
to continue despite of the great diﬃculties, which I encountered. The fact that two
manifolds are equivalent does mean that they correspond to each other, point to
point, in such a way that two arbitrary points in one of them are close to coincide
when the two corresponding points in the other manifold are. (We will later return
to the connection between Poincar´e’s concept of hom´emorphisme, Analysis Situs
&2, and the concept of equivalence that has been deﬁned here). The question that
arises is, how we shall cut a closed manifold (vari´ete ferm´ee; Poincar´e 1.c. &1) to
make it simply connected. To solve this problem we use the following procedure:
the manifold is punctured: i.e.
the elementary manifold, which constitutes the
neighborhood of a point, is removed. From the puncture arises a boundary, and it
is extended by the means of continuous deformation in such a way that we remove
more and more of the given manifold. We continue like this, until a part of the
boundary encounters other parts of itself; in such places we stop the deformation,
when the distance between the parts that are encountering has become inﬁnitely
small. If we continue in this way, then we end up with a diagram, which is made
from a system of manifolds of lower dimensions than the original one46 – or rather:
it is made from the closest neighborhood of this system, that is, a manifold that is
inﬁnitely small in the nth dimension. We call the system of manifolds of a lower
dimension, which is the boundary of the diagram, its nucleus. This diagram has
two meanings. First, it presents the manifold which is equivalent with the given one
after the puncture. If we succeed in proposing normal forms into which the diagrams
could be reduced, then the fact that the normal forms of the diagrams are identical
will be the necessary and suﬃcient condition for two diagrams to be equivalent.
– But the nucleus of the diagram indicates the cuts that shall be done to make
the given manifold simply connected; if we make the discussed extending in reverse
order, then the manifold, which remains after performing the cuts determined by
the diagram, will contract into that elementary manifold, which is removed by the
puncture.
We will later return to this comparison of results that are found along this path,
and the Riemann-Betti theory of connectivity numbers.
The whole Second part is translated in [P-22].
Poul Heegaard’s bibliography:
[Heeg] P. Heegaard, Forstudier til en Topologisk Teori for de algebraiske Fladers
Sammenhæng, København, 1898, Filosoﬁske Doktorgrad; French translation: Sur
l’Analysis situs, Soc. Math. France Bull., 44 (1916), 161-242.
[D-H] M. Dehn, P. Heegaard, Analysid situs, Encykl. Math. Wiss., vol. III
AB3 Leipzig, 1907, 153-220.
46It is called a spine of the manifold in the modern terminology [translator’s remark]
BIBLIOGRAPHY
53
[H-1] P. Heegaard, Der Mathematikunterricht in D¨anemark, Internationale
Matchematische Unterrichtskommission I.M.U.K, København 1912. (Teaching of
Mathematics in Denmark).
[H-2] P. Heegaard, Bidrag til Grafernes Theori, Tredie Skandinaviske Matem-
atikerkomgres i Kristiania, 1913, 1-6.
[H-3] P. Heegaard, Omriss av kronologiens historie i Europa (med sœrlig hen-
blikk p´a den norske almanakk av 1644, ????? 51-96.
[H-4] P. Heegaard, Hamiltons Dodekaederspil, Nyt Tidsskrift Matematik, 29(4),
1919, 81-88.
[H-5] P. Heegaard, Mindetale, oer prof..dr.H.G.Zeuthen, Særtrykk av Viden-
skapsselskapets Forhandlinger 1920, 1-3.
[H-6] P. Heegaard, Hovedlinjer i H.G.Zeuthens videnskabelige production, Fore-
drag i Norsk Matematisk Forening, Særtrykk av Norsk Matematisk Tidsskrift, 1920,
1-5.
[H-7] P. Heegaard, Eudoksos’ Hippopede. Et foredrag holdt i Norsk Matematisk
Forening, Særtrykk av Norsk Matematisk Tidsskrift, 1921, 1-10.
[H-8] P. Heegaard, Felix Klein, Et foredrag holdt i Norsk Matematisk Forening
25. mars 1926, Særtrykk av Norsk Matematisk Tidsskrift, 1926, 1-7.
[H-9] P. Heegaard, Om en generalisasjon til rummet av Sophus Lies fremstilling
av imaginære elementer i planet, Den syvende Skandinaviske Matematikerkongress,
I Oslo 19-22 August 1929, Oslo 1930, 92-95.
[H-10] P. Heegaard, Scandinavie. Les modiﬁcations essentielles de l’enseignement
math´ematique dans les principaux pays depuis 1910, L’Enseignement math´ematique,
XXIX(4-6), 1930, 307-314.
[H-11] P. Heegaard, Appendix P.Osl 6. The date of the Horoscope of Philoe
(in “Papyri Osloenses” by S.Eitrem, L.Amundsen), Oslo, on commission by Jacob
Dybwad, 1931, 146-151.
[H-12] P. Heegaard, ¨Uber die Heawoodschen Kongruenzen, Særtrykk av Norsk
Matematisk, Forenings Skrifter,Serie II, Nr. 1-12, 1933, 47-54.
[H-13] P. Heegaard, Norv`ege. La pr´eparation th´eorique et pratique des pro-
fesseurs de Math´ematiques de l’enseignement secondaire, De L’Enseignement math´ematique,
5-6, 1933, 360-364.
[E-H] F. Engel, P. Heegaard, Sophus Lies Samlede Avhandlinger.
Blind I,
Særtrykk av Norsk Matematisk Tidsskrift, 1934, 1-9.
[H-14] P. Heegaard, Et brev fra Abel til Degen, Særtrykk av Norsk Matematisk
Tidsskrift, 2. hefte 1935, 1-6.
[H-15] P. Heegaard, Bemerkungen zum Vierfarbenproblem, Mat.
Sb.
(New
Ser.), 1(43):5, (1936), 685-693.
[H-16] P. Heegaard, La repr´esentation des points imaginaires de Sophus Lie at
sa valeur didactique, Atti del Congresso Internazionale dei Matematici, Bologna,
3-10 settembre 1938 - VI, 421-423.
[H-17] P. Heegaard, Die Topologie unddie Theorie der algebraischen Funktionen
mit zwei komplexen Variabeln, Congr`es des Math´ematiques `a Helsingfors 1938, 1-8.
