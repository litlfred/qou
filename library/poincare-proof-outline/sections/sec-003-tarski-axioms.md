---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-003-tarski-axioms
section_title: "Tarski axioms"
section_number: null
pages: 4-5
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
In this section we introduce axioms of Tarski [7] trough a series of locales.

theory Tarski
imports Main
begin

The first locale assumes all Tarski axioms except for the Euclid’s axiom and the continuity axiom and corresponds
to absolute geometry.

locale TarskiAbsolute =
fixes cong :: 'p => 'p => 'p = 'p => bool

fixes betw :: '‘p => 'p => ‘p => bool

assumes cong-reflexive: cong © y y &

assumes cong-transitive: cong « y zu A cong zy vw —> congzuuvw

assumes cong-identity: conguyzz—>@r=y

assumes segment-construction: 4 z. betw xyz A congyzab

assumes five-segment: «A#y A betwxryz A betwr' yz’ A congzryxz'y’ A congyzy’z' A congzusz’u’ A cong
yuyu’ — congzuz'u’

assumes betw-identity: betwxyr—->r=y

assumes Pasch: betwauz A betwy vz — (J a. betwuay A betw ra v)

assumes lower-dimension: J a. 4 b. 4d c. = betwabe A 7 betwbcaA- betwcab

assumes upper-dimension: congxuxv A congyuyuA congzuzvAu¢v — betwaxyz V betwy za V betw z
ry
begin

The following definitions are used to specify axioms in the following locales.

Point p is on line ab.
definition on-line where
on-line pa b <—+ betwpabyv betwapbv betwabp
Point p is on ray ab.
definition on-ray where
on-ray p a b <—> betwapbv betwabp
Point p is inside angle abc.
definition in-angle where
in-anglepabc+<>+bfAahbAcApFbdbA (Au. betwarcNr#aNhu Fc on-ray p bx)
Ray rary meets the line Ialy.
definition ray-meets-line where

ray-meets-line ra rb la lb <— (A «&. on-ray x ra rb A on-line «x la Ib)

end

The second locales adds the negation of Euclid’s axiom and limiting parallels and corresponds to hyperbolic
geometry.
locale TarskiHyperbolic = TarskiAbsolute +
assumes euclid-negation: J abcdt. betwadt A bettwhdcvhNa#dA(V xy. betwaba A betwacy — 7 betw
rty)
assumes limiting-parallels: = on-line a x1 «2 =>
(A al a2. - on-line a al a2 A
— ray-meets-line a al x1 72 \
— ray-meets-line a a2 x1 22 \
(V a’. in-angle a’ al a a2 —+ ray-meets-line a a’ x1 22))

The third locale adds the continuity axiom and corresponds to elementary hyperbolic geometry.

locale ElementaryTarskiHyperbolic = TarskiHyperbolic +
assumes continuity: [J a.V c.V y. prAwy — btwaryl = 3d.VaeVyprApy— betwxrby

end
