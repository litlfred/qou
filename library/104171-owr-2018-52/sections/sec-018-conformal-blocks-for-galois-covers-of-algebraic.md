---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-018-conformal-blocks-for-galois-covers-of-algebraic
section_title: "Conformal blocks for Galois covers of algebraic groups"
section_number: null
pages: 58-66
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Shrawan Kumar
(joint work with Jiuzu Hong)
1. Introduction
Wess-Zumino-Witten model is a type of two dimensional conformal ﬁeld theory,
which associates to an algebraic curve with marked points and integrable highest
weight modules of an aﬃne Kac-Moody Lie algebra associated to the points, a
ﬁnite dimensional vector space consisting of conformal blocks. The space of con-
formal blocks has many important properties including Propogation of Vacua and
Factorization. Deforming the pointed algebraic curves in a family, we get a sheaf of
conformal blocks. This sheaf admits a projectively ﬂat connection when the fam-
ily of pointed curves is a smooth family. The mathematical theory of conformal
blocks was ﬁrst established by Tsuchiya-Ueno-Yamada. All the above properties
are important ingredients in the proof of the celebrated Verlinde formula for the
dimension of the space of conformal blocks.This theory has a geometric counter-
part in the theory of moduli spaces of principal bundles over algebraic curves and
also the moduli of curves and its stable compactiﬁcation.
In this paper we study a twisted theory of conformal blocks on Galois covers of
algebraic curves. More precisely, we consider an algebraic curve Σ with an action
of a ﬁnite group Γ. Moreover, we take a group homomorphism φ : Γ →Aut(g)
of Γ acting on a simple Lie algebra g. Given any smooth point q ∈Σ, we attach
an aﬃne Lie algebra ˆL(g, Γq) (in general a twisted aﬃne Lie algebra), where Γq
is the stabilizer group of Γ at q. The integrable highest weight representations of
ˆL(g, Γq) of level c (where c is a positive integer) are parametrized by certain ﬁnite
set Dc,q of dominant weights of the reductive Lie algebra gΓq, i.e., for any λ ∈Dc,q
we attach an integrable highest weight representation H (λ) of ˆL(g, Γq) of level c
and conversely. Given a collection⃗q := (q1, · · · , qs) of smooth points in Σ such
that their Γ-orbits are disjoint and a collection of weights⃗λ = (λ1, . . . , λs) with
λi ∈Dc,qi, we consider the representation H (⃗λ) := H (λ1) ⊗· · · ⊗H (λs). Now,
deﬁne the associated space of twisted covacua (or twisted dual conformal blocks)
as follows:
VΣ,Γ,φ(⃗q,⃗λ) :=
H (⃗λ)
g[Σ\Γ ·⃗q]Γ · H (⃗λ)
,
where g[Σ\Γ ·⃗q]Γ is the Lie algebra of Γ-equivariant regular functions from Σ\Γ ·⃗q
to g acting on the i-th factor H (λi) of H (⃗λ) via its Laurent series expansion at
qi.
The following Propogation of Vacua is the ﬁrst main result of our work.
Theorem 1. Assume that Γ stabilizes a Borel subalgebra of g. Let q be a smooth
point of Σ such that q is not Γ-conjugate to any point⃗q.
Then, we have the
Enveloping Algebras and Geometric Representation Theory
3139
following isomorphism of spaces of twisted covacua:
VΣ,Γ,φ(⃗q,⃗λ) ≃VΣ,Γ,φ

(⃗q, q), (⃗λ, 0)

.
In fact, a stronger version of Propogation Theorem is proved. In our equivariant
setting we need to generalize some important ingredients. Further, the fact that
“ The endormorphism X−θ ⊗f of H is locally nilpotent for all f ∈O(U) ”
can not easily be generalized to the twisted case. To prove an analogous result,
we need to assume that Γ stabilizes a Borel subalgebra of g. It will be interesting
to see if this assumption can be removed.
Let q be a nodal point in Σ. Assume that the action of Γ at q is stable and the
stabilizer group Γq does not exchange the two formal branches around q. Let Σ′ be
the normalization of Σ at the points Γ · q, and let q′, q′′ be the two smooth points
in Σ′ over q. The following Factorization Theorem is our second main result.
Theorem 2. Assume that Γ stabilizes a Borel subalgebra of g. Then, there exists
a natural isomorphism:
VΣ,Γ,φ(⃗q,⃗λ) ≃
M
µ∈Dc,q′′
VΣ′,Γ,φ

(⃗q, q′, q′′), (⃗λ, µ∗, µ)

,
where µ∗is the dominant weight of gΓq′ such that V (µ∗) is the dual representation
V (µ)∗of gΓq = gΓq′ = gΓq′′ .
The formulation of the Factorization Theorem in the twisted case is a bit more
delicate, since the parameter sets Dc,q′ and Dc,q′′ attached to the points q′, q′′ are
diﬀerent in general; nevertheless they are related by the dual of representations
under the assumption that the action of Γ at the node q is stable and the stabilizer
group Γq does not exchange the branches. Its proof requires additional care (from
that of the untwisted case) at several places. The assumption that Γ stabilizes
a Borel subalgebra of g also appears in this theorem as we use the Propogation
Theorem in its proof.
Given a family (ΣT ,⃗q) of s-pointed Γ-curves over a connected scheme T and
weights⃗λ = (λ1, . . . , λs) with λi ∈Dc,qi as above, one can attach a functorial
coherent sheaf VΣT ,Γ,φ(⃗q,⃗λ) of twisted covacua over the base T . We prove the
following theorem.
Theorem 3. Assume that the family ΣT →T is a smooth family over a smooth
base T . Then, the sheaf VΣT ,Γ,φ(⃗q,⃗λ) of twisted covacua is locally free of ﬁnite
rank over T . In fact, there exists a projectively ﬂat connection on VΣT ,Γ,φ(⃗q,⃗λ).
This theorem relies mainly on the Sugawara construction for the twisted aﬃne
Kac-Moody algebras. In the untwisted case, this construction is quite well-known.
In the twisted case, the formulae are written in terms of the abstract Kac-Moody
presentation of ˆL(g, σ), where σ is a ﬁnite order automorphism of g.
For our
application, we require the formulae in terms of the aﬃne realization of ˆL(g, σ) as
3140
Oberwolfach Report 52/2018
a central extension of the twisted loop algebra g((t))σ. We present such a formula
in our work, which might be new (to our knowledge).
Let H M g,Γ,η be the Hurwitz stack of Γ-stable s-pointed Γ-curves of genus g
with marking data η at the marked points such that the set of Γ-orbits of the
marked points contains the full ramiﬁcation divisor.
It was proved by Bertin-
Romagny that H M g,Γ,η is a smooth and proper Deligne-Mumford stack. We can
attach a collection⃗λ of dominant weights to the marking data η, and associate a
coherent sheaf Vg,Γ,φ(η,⃗λ) of twisted covacua over the Hurwitz stack H Mg,Γ,η.
We prove the following theorem.
Theorem 4. Assume that Γ stabilizes a Borel subalgebra of g. Then, the sheaf
Vg,Γ,φ(η,⃗λ) is locally free over the stack H Mg,Γ,η .
Our proof of this theorem follows closely the work of Looijenga in the non-
equivariant setting; in particular, we use the canonical smoothing deformation of
nodal curves and gluing tensor elements. The Factorization Theorem also plays a
crucial role in the proof. In the case Γ is cyclic, this theorem together with the
Factorization Theorem allows us to reduce the computation of the dimension of
the space of twisted covacua to the case of Galois covers of projective line with
three marked points.
In the usual (untwisted) theory of conformal blocks, the space of covacua has a
beautiful geometric interpretation in that it can be identiﬁed with the space of
generalized theta functions on the moduli space of parabolic G-bundles over the
algebraic curve, where G is the simply-connected simple algebraic group associ-
ated to g. This identiﬁcation was proved by Beauville-Laszlo, Faltings, Kumar-
Narasimhan-Ramanathan, Laszlo-Sorger and Pauly. In the setting of Γ-curves Σ
as well, it is expected that the space of twisted covacua can be identiﬁed with the
generalized theta functions on the moduli space of parabolic G-bundles on ¯Σ, where
¯Σ is the quotient of Σ by Γ, and G is the parahoric Bruhat-Tits group scheme over
¯Σ obtained via the construction of Γ-invariants of the Weil restriction from Σ to ¯Σ.
In fact, this natural question has been formulated earlier by Pappas-Rapoport in
a more general setting. Along this direction, there has been some results recently
by Hacen when Γ is of order 2 acting on g = sln by certain involutions.
There were some earlier works related to the twisted theory of conformal blocks.
For example Frenkel-Szczesny studied the twisted modules over Vertex algebras on
algebraic curves, and Kuroki-Takebe studied a twisted Wess-Zumino-Witten model
on elliptic curves. When Γ is of prime order and the marked points are unramiﬁed,
the space VΣ,Γ,φ(⃗q,⃗λ) has been studied recently by Damiolini, where she proved
similar results as ours. Our work is a vast generalization of her work, since we do
not need to put any restrictions on the Γ-orbits, and the only restriction on Γ is
that Γ stabilizes a Borel subalgebra of g (when Γ is a cyclic group it automatically
holds). In particular, when Γ has nontrivial stabilizers at the marked points⃗q,
twisted aﬃne Kac-Moody Lie algebras and their representations occur naturally in
this ramiﬁcation theory of conformal blocks. We also learnt from S. Mukhopadhyay
that he has obtained some results (unpublished) in this direction.
Enveloping Algebras and Geometric Representation Theory
3141
Our
work
is
motivated
by
a
conjectural
connection
predicted
by
Fuchs-Schweigert between the trace of diagram automorphism on the space of
conformal blocks and certain conformal ﬁeld theory related to twisted aﬃne Lie
algebras. A Verlinde type formula for the trace of diagram automorphism on the
space of conformal block has been proved recently by J. Hong, where the formula
involves the twisted aﬃne Kac-Moody algebras mysteriously. We hope that it can
shed some light on the dimension of twisted conformal blocks; in particular, when
Γ acts on g by diagram automorphisms.
Reporter: Leonardo Patimo
3142
Oberwolfach Report 52/2018
Participants
Prof. Dr. Pramod N. Achar
Department of Mathematics
Louisiana State University
Baton Rouge LA 70803-4918
UNITED STATES
Prof. Dr. Henning Haahr
Andersen
TGMRC
China Three Gorges University
No. 8, Daxue Road, Xiling
Yichang City, Hubei Province 443 002
CHINA
Prof. Dr. Alexander Braverman
Perimeter Institute for Theoretical
Physics
31 Caroline St. N.
Waterloo ON N2L 2Y5
CANADA
Dr. Adrien Brochier
Department Mathematik
Universit¨at Hamburg
Bundesstrasse 55
20146 Hamburg
GERMANY
Prof. Dr. Vyjayanthi Chari
Department of Mathematics
University of California, Riverside
900, West Big Springs Road
Riverside CA 92521-0135
UNITED STATES
Dr. Stephanie Cupit-Foutou
Fakult¨at f¨ur Mathematik
Ruhr-Universit¨at Bochum
Geb¨aude NA 4/67
44780 Bochum
GERMANY
Dr. Olivier Dudas
UFR de Math´ematiques
Universit´e Paris Diderot
5, rue Thomas Mann
75205 Paris Cedex 13
FRANCE
Dr. Claude Eicher
Department of Mathematics
Massachusetts Institute of Technology
77 Massachusetts Avenue
Cambridge, MA 02139-4307
UNITED STATES
Prof. Dr. Mikhail Finkelberg
Department of Mathematics
National Research University
Higher School of Economics
6 Usacheva St.
Moscow 119 048
RUSSIAN FEDERATION
Dr. Iordan Ganev
Institute of Science and
Technology Austria (IST Austria)
Am Campus 1
3400 Klosterneuburg
AUSTRIA
Prof. Dr. Sachin Gautam
Department of Mathematics
The Ohio State University
100 Mathematics Building
231 West 18th Avenue
Columbus, OH 43210-1174
UNITED STATES
Enveloping Algebras and Geometric Representation Theory
3143
Prof. Dr. Christof Geiss
Instituto de Matem´aticas
UNAM
Ciudad Universitaria
04510 Ciudad de M´exico Ciudad de
M´exico
MEXICO
Prof. Dr. Victor Ginzburg
Department of Mathematics
The University of Chicago
5734 South University Avenue
Chicago, IL 60637-1514
UNITED STATES
Dr. Simon Goodwin
School of Mathematics
The University of Birmingham
Edgbaston
Birmingham B15 2TT
UNITED KINGDOM
Prof. Dr. Iain Gordon
School of Mathematics
University of Edinburgh
James Clerk Maxwell Building
King’s Buildings
Mayﬁeld Road
Edinburgh EH9 3FD
UNITED KINGDOM
Prof. Dr. Maria Gorelik
Department of Mathematics
The Weizmann Institute of Science
P.O. Box 26
Rehovot 76100
ISRAEL
Prof. Dr. Jacob Greenstein
Department of Mathematics
University of California, Riverside
900, West Big Springs Road
Riverside, CA 92521-0135
UNITED STATES
Dr. Sam Gunningham
School of Mathematics
The University of Edinburgh
James Clerk Maxwell Building
The King’s Buildings
Peter Guthrie Tait Road
Edinburgh EH9 3FD
UNITED KINGDOM
Dr. Thorsten Heidersdorf
Max-Planck-Institut f¨ur Mathematik
Vivatsgasse 7
53111 Bonn
GERMANY
Prof. Dr. Anthony Henderson
School of Mathematics and Statistics
The University of Sydney
Sydney NSW 2006
AUSTRALIA
Prof. Dr. David Hernandez
IMJ - PRG
Universit´e Paris VII - Paris Diderot
Bat. S. Germain
CP 7012
75205 Paris Cedex 13
FRANCE
Prof. Dr. Jens Carsten Jantzen
Matematisk Institut
Aarhus Universitet
Ny Munkegade 118
8000 Aarhus C
DENMARK
Dr. Thorge Jensen
D´epartement de Math´ematiques
LMBP UMR 6620
Universit´e Clermont Auvergne
24, Avenue des Landais
63177 Aubi`ere Cedex
FRANCE
3144
Oberwolfach Report 52/2018
Dr. David Jordan
School of Mathematics
University of Edinburgh
James Clerk Maxwell Bldg.
King’s Buildings, Mayﬁeld Road
Edinburgh EH9 3JZ
UNITED KINGDOM
Dr. Daniel Juteau
IMJ - PRG
Universit´e Paris Diderot (Paris VII)
CNRS UMR 7586
Bˆatiment Sophie Germain
Case Postale 7012
75205 Paris Cedex 13
FRANCE
Prof. Dr. Shrawan Kumar
Department of Mathematics
University of North Carolina at Chapel
Hill
Phillips Hall
Chapel Hill, NC 27599-3250
UNITED STATES
Dr. Martina Lanini
Dipartimento di Matematica
Universita degli Studi di Roma II
Tor Vergata
Via della Ricerca Scientiﬁca
00133 Roma
ITALY
Prof. Dr. Bernard Leclerc
D´epartement de Math´ematiques
Universit´e de Caen
14032 Caen Cedex
FRANCE
Prof. Dr. Ivan Loseu
Department of Mathematics
University of Toronto
40 St. George Street
Toronto ON M5S 2E4
CANADA
Dr. Carl Mautner
Department of Mathematics
University of California, Riverside
900 University Avenue
Riverside, CA 92521
UNITED STATES
Prof. Dr. Kevin R. McGerty
Mathematical Institute
Oxford University
Woodstock Road
Oxford OX2 6GG
UNITED KINGDOM
Peter J. McNamara
School of Mathematics and Statistics
The University of Melbourne
Parkville, VIC 3010
AUSTRALIA
Prof. Dr. Anne Moreau
Laboratoire Paul Painleve, UMR 8524
Universit´e des Sciences et
Technologie de Lille 1
Cite Scientiﬁque, Bat. M2
59655 Villeneuve d’Ascq Cedex
FRANCE
Dr. Emily Norton
Max-Planck-Institut f¨ur Mathematik
Vivatsgasse 7
53111 Bonn
GERMANY
Dr. Leonardo Patimo
Mathematisches Institut
Universit¨at Freiburg
Ernst-Zermelo-Strasse 1
79104 Freiburg i. Br.
GERMANY
Enveloping Algebras and Geometric Representation Theory
3145
Tomasz Przezdziecki
School of Mathematics and Statistics
University of Glasgow
University Gardens
Glasgow G12 8QW
UNITED KINGDOM
Dr. Fan Qin
School of Mathematical Sciences
Shanghai Jiao Tong University
800 Dongchuan Road
Shanghai Shi 200 240
CHINA
Prof. Dr. Markus Reineke
Fakult¨at f¨ur Mathematik
Ruhr-Universit¨at Bochum
Universit¨atsstrasse 150
44801 Bochum
GERMANY
Prof. Dr. Jan Schr¨oer
Mathematisches Institut
Universit¨at Bonn
Endenicher Allee 60
53115 Bonn
GERMANY
Dr. Beatrix Schumann
Mathematisches Institut
Universit¨at zu K¨oln
Weyertal 86 - 90
50931 K¨oln
GERMANY
Prof. Dr. Vera V. Serganova
Department of Mathematics
University of California
Berkeley CA 94720-3840
UNITED STATES
Dr. Peng Shan
Yau Mathematical Sciences Center
Tsinghua University
Beijing 100 084
CHINA
Prof. Dr. Wolfgang Soergel
Mathematisches Institut
Universit¨at Freiburg
Ernst-Zermelo-Strasse 1
79104 Freiburg i. Br.
GERMANY
Prof. Dr. Catharina Stroppel
Mathematisches Institut
Universit¨at Bonn
Endenicher Allee 60
53115 Bonn
GERMANY
Prof. Dr. Peter Tingley
Department of Mathematics and
Statistics
Loyola University of Chicago
Chicago, IL 60626-5385
UNITED STATES
Prof. Dr. Valerio Toledano Laredo
Department of Mathematics
Northeastern University
567 Lake Hall
360 Huntington Avenue
Boston MA 02115-5000
UNITED STATES
Dr. Jacinta Torres
Fakult¨at f¨ur Mathematik
Karlsruher Institut f¨ur Technologie
(KIT)
Englerstrasse 2
76131 Karlsruhe
GERMANY
Prof. Dr. Michela Varagnolo
D´epartement de Math´ematiques
Universit´e de Cergy-Pontoise
Site Saint-Martin, BP 222
2, Avenue Adolphe Chauvin
95302 Cergy-Pontoise Cedex
FRANCE
3146
Oberwolfach Report 52/2018
Prof. Dr. Eric Vasserot
Equipe de Theorie de Groupes
Universit´e Paris VII
175, rue de Chevaleret
75013 Paris Cedex
FRANCE
Prof. Dr. Ben Webster
Perimeter Institute for Theoretical
Physics
31 Caroline St. N.
Waterloo ON N2L 2Y5
CANADA
Dr. Harold Williams
Department of Mathematics
University of Texas
2515 Speedway Stop
Austin, TX 78712-1202
UNITED STATES
Prof. Dr. Geordie Williamson
School of Mathematics and Statistics
The University of Sydney
Sydney NSW 2006
AUSTRALIA
Prof. Dr. Oksana Yakimova
Mathematisches Institut
Friedrich-Schiller-Universit¨at Jena
07737 Jena
GERMANY
