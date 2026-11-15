---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-009-points-on-h-line
section_title: "Points on h-line"
section_number: null
pages: 8-11
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Each h-line in the Poincaré model contains at least two different points within the unit disc.

First we prove an auxiliary lemma.

lemma ex-is-poincare-line-points’:
assumes 112: il € circline-set H  unit-circle-set
i2 € circline-set H M unit-circle-set
il # i2
assumes a: a € circline-set H a ¢ unit-circle-set
shows 3 b.b 4 i1 ADA i2 Ab fad bF inversion a A b € circline-set H
proof—
have inversion a ¢ unit-circle-set
using <a ¢ unit-circle-set»
unfolding unit-circle-set-def circline-set-def
by (metis inversion-id-iff-on-unit-circle inversion-involution mem-Collect-eq)

have a # inversion a
using <a ¢ unit-circle-sety inversion-id-iff-on-unit-circle[ of a]
unfolding unit-circle-set-def circline-set-def
by auto

have a F il a F i2 inversion a F il inversion a F i2
using assms <inversion a ¢ unit-circle-sety
by auto

then obtain 6 where cr2: cross-ratio b i1 a i2 = of-complex 2
using <i1 4 i2>
using ex-cross-ratio[of il a i2]
by blast

have distinct-b: b A i1b #i2b#a
using <i1 4 i2) «a FZ il) (a F 12)
using ex1-cross-ratio|of il a i2]
using cross-ratio-O|of i1 a i2] cross-ratio-1[of i1 a i2] cross-ratio-inf|of i1 i2 a]
using cr2
by auto

hence 6 € circline-set H
using assms four-points-on-circline-iff-cross-ratio-reallof b i1 a i2| cr2
using unique-circline-set{of i1 i2 a]
by auto
moreover

have b inversion a
proof (rule ccontr)
assume *: — ?thesis
have inversion il = il inversion i2 = i2
using i112
unfolding unit-circle-set-def
by auto
hence cross-ratio (inversion a) il a i2 = cross-ratio a il (inversion a) i2
using * cross-ratio-inversion|of il a i2 b] <a 4 ily (a # 12> cil F 12) «b F il
using four-points-on-circline-iff-cross-ratio-reallof b i1 a i2]
using i12 distinct-b conjugate-id-iff [of cross-ratio b i1 a i2]
using 712 a <b € circline-set H»
by auto
hence cross-ratio (inversion a) i1 a i2 # of-complex 2
using cross-ratio-commute-13|of inversion a il a i2]
using reciprocal-id-iff
using of-complez-inj
by force
thus False
using * cr2
by simp
qed

ultimately
show ?thesis
using assms <b # il) (b # i2) (b # ay
by auto
qed

Now we can prove the statement.

lemma ex-is-poincare-line-points:
assumes is-poincare-line H
shows 3 uv. u € unit-disc A v € unit-disc Au 4 v A {u, v} C circline-set H
proof—
obtain uv w where *:uZAvv4wuF w {u, v, w} C circline-set H
using assms is-poincare-line-iff [of H]
using circline-type-neg-card-gt3|of H|
by auto

have — {u, v, w} C unit-circle-set
using unique-circline-set{of uv w] *
by (metis assms insert-subset not-is-poincare-line-unit-circle unit-circle-set-def )

hence H # unit-circle
unfolding unit-circle-set-def
using *
by auto

show ?thesis
proof (cases (u € unit-disc A v € unit-disc) V
(u € unit-disc A w € unit-disc) V
(v € unit-disc \ w € unit-disc))
case True
thus ?thesis
using *
by auto
next
case False

have 5 ab. a #6 A a F inversion b A a € circline-set H A b € circline-set H \ a € unit-circle-set A b ¢
unit-circle-set
proof (cases (u € unit-circle-set \ v € unit-circle-set) V
(u € unit-circle-set \ w € unit-circle-set) V
(uv € unit-circle-set \ w € unit-circle-set))
case True
then obtain i/ i2 a where +:
il € unit-circle-set M circline-set H i2 € unit-circle-set \ circline-set H
a € circline-set H a ¢ unit-circle-set
i Ail 4ai2F#a
using * (7 {u, v, w} C unit-circle-set»
by auto
then obtain b where 6 € circline-set H b £ i1 b 4 i2b 4. ab F inversion a
using ex-is-poincare-line-points'|of i1 H i2 a]
by blast

hence b ¢ unit-circle-set
using « (H # unit-circley unique-circline-set|of il i2 b]
unfolding unit-circle-set-def
by auto

thus ?thesis
using * <b € circline-set Hy <b # a» <b # inversion ay
by auto
next
case False
then obtain f g h where
x: f #4 gf € circline-set H f ¢ unit-circle-set
g € circline-set H g €¢ unit-circle-set
h € circline-set Hh A fhAg
using *
by auto
show ?thesis
proof (cases f = inversion g)
case False
thus ?thesis
using *
by auto
next
case True
show ?thesis
proof (cases h € unit-circle-set)
case False
thus ?thesis
using * <f = inversion g>
by auto
next
case True
obtain m where cr2: cross-ratio m h f g = of-complex 2
using ex-cross-ratiolof h fg) * (f Ag hA fr h# gr
by auto
hencem4#4hmz7fm4qg
using hA¢Af hAg if #q
using ex1-cross-ratio|of h f g]
using cross-ratio-O[of h f g| cross-ratio-1[of h f g| cross-ratio-inf lof h g f]
using cr2
by auto
hence m € circline-set H
using four-points-on-circline-iff-cross-ratio-reallof m h f g| cr2
using (h #4 f> (h #g> (f #g) *
using unique-circline-set[of h f g]
by auto

show ?thesis
proof (cases m € unit-circle-set)
case False
thus ?thesis
using (m # f> «m # g> <f = inversion g> * «m € circline-set Hy
by auto
next
case True

10
then obtain n where n 4 hn #4 mn ¥F fn F inversion fn € circline-set H
using ez-is-poincare-line-points'[of h H m f] * «m € circline-set H» «h € unit-circle-sety «m # hy
by auto
hence n ¢ unit-circle-set
using « (H # unit-circle> unique-circline-set|of m n h]
using «m # h> «m © unit-circle-set> <h € unit-circle-set> «m € circline-set H»
unfolding unit-circle-set-def
by auto

thus ?thesis
using * <n € circline-set Hy in # f> «n & inversion f»
by auto
qed
qed
qed
qed
then obtain a b where ab: a # b a F inversion b a € circline-set H b € circline-set H a ¢ unit-circle-set b ¢
unit-circle-set
by blast
have V x. x € circline-set H A x ¢ unit-circle-set —> (J 2’. x’ € circline-set H M unit-disc A (e' = 2 V x! =
inversion 2))
proof safe
fix x
assume z: x € circline-set H x ¢ unit-circle-set
show J 2’. x’ € circline-set H M unit-disc A (’ = « V x’ = inversion x)
proof (cases x € unit-disc)
case True
thus ?thesis
using x
by auto
next
case False
hence x € unit-disc-compl
using x in-on-out-univ[of ounit-circle]
unfolding unit-circle-set-def unit-disc-def unit-disc-compl-def
by auto
hence inversion x € unit-disc
using inversion-unit-disc-compl
by blast
thus ?thesis
using is-poincare-line-inverse-point|OF assms, of t] «
by auto
qed
qed
then obtain a’ b’ where
«x: a’ € circline-set H a’ € unit-disc b' € circline-set H b' € unit-disc and
xe: a’ = a V a’ = inversion a b' = b V b! = inversion b
using ab
by blast
have a’ 4 b’
using (a 4 by (a # inversion by *x *
by (metis inversion-involution)
thus ?thesis
using *
by auto
qed
qed
