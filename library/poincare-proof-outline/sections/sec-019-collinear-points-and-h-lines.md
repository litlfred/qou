---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-019-collinear-points-and-h-lines
section_title: "Collinear points and h-lines"
section_number: null
pages: 32-34
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-collinear3-poincare-line-general:
assumes poincare-collinear {a, a1, a2} al # a2 al F inversion a2
shows a € circline-set (poincare-line al a2)
using assms
using poincare-collinear-def unique-poincare-line-general
by auto

lemma poincare-line-poincare-collinear3-general:
assumes a € circline-set (poincare-line al a2) al # a2
shows poincare-collinear {a, a1, a2}
using assms
unfolding poincare-collinear-def
by (rule-tac «=poincare-line a1 a2 in eal, simp)

lemma poincare-collinear3-poincare-lines-equal-general:
assumes poincare-collinear {a, al, a2} a 4 al a ¥ a2 a F inversion al a F inversion a2
shows poincare-line a al = poincare-line a a2
using assms
using unique-poincare-line-generallof a a2 poincare-line a al]
by (simp add: insert-commute poincare-collinear3-poincare-line-general)

4.2.7 Points collinear with 0),

lemma poincare-collinear-zero-iff:
assumes of-complex y’ € unit-disc and of-complez z’ € unit-disc and
y' #z' and y’ 4 0 and z' 4 0
shows poincare-collinear {0;, of-complex y’, of-complex z"} +
y'*cnj z' = cnj y'*z' (is ?lhs +> ?rhs)
proof—
have of-complex y' 4 of-complex z’
using assms
using of-complez-inj
by blast
show ?thesis
proof
assume ?/hs
hence 0), € circline-set (poincare-line (of-complex y') (of-complex z'))
using wnique-poincare-line|of of-complex y’ of-complex z’|
using assms <of-complex y' 4 of-complex z'>
unfolding poincare-collinear-def
by auto
moreover
let ?mix = y’ * cnj z' — cnj y’ * 2’
have is-real (i * ?mix)
using eq-cnj-iff-reallof ?miz]
by auto
hence y! « enj z’ = cnj y’ * z' ++ Re (i * ?miz) = 0
using complez.expand|of i * ?mizx 0]
by (metis complex-i-not-zero eq-iff-diff-eq-0 mult-eq-0-iff zero-complex.simps(1) zero-complex.simps(2))
ultimately
show ?rhs
using (y’ Az «y' 40> «z' A O>
unfolding circline-set-def
by simp (transfer, transfer, auto simp add: vec-cnj-def split: if-split-asm, metis Re-complez-of-real Re-mult-real
Im-complex-of-real)
next
assume ?rhs
thus ?hs
using assms <of-complex y' 4 of-complex z'»
unfolding poincare-collinear-def
unfolding circline-set-def
apply (rule-tac t=poincare-line (of-complex y’) (of-complex z’) in ez!)
apply auto
apply (transfer, transfer, simp add: vec-cnj-def)
done
qed
qed

lemma poincare-collinear-zero-polar-form:
assumes poincare-collinear {0n, of-complex x, of-complex y} and
a # 0 and y ¥ 0 and of-complex x € unit-disc and of-complex y € wnit-disc
shows 3 y rrzry. z= corrz * cise Ay =corry*cisp AN rr £0 AN ry #0
proof—
from «x 4 0» (y 4 0» obtain y vy’ rz ry where
polar: x = cor rz * cis p y = cor ry * cis y'and y= Argz yp’ = Argy
by (metis cmod-cis)
hence rz 4 0 ry 4 0
using (x # 0) cy # 0»
by auto
have of-complex y € circline-set (poincare-line 0; (of-complex x))
using assms
using unique-poincare-line|of 0), of-complex 2]
unfolding poincare-collinear-def
unfolding circline-set-def
using of-complex-zero-iff
by fastforce
hence cnj x * y= u * cnjy
using (x # 0) cy # 0»
unfolding circline-set-def
by simp (transfer, transfer, simp add: vec-cnj-def field-simps)
hence cis(yp’ — y) = cis(p — ’)
using polar (rz # 0» «ry # 0»
by (simp add: cis-mult)
hence sin (y’ — y) = 0
using cis-diff-cis-opposite[of yp’ — y]
by simp
then obtain k :: int where y’ — y = k x pi
using sin-zero-iff-int2[of yp’ — ¢]
by auto
hence «: y’ = y + k * pi
by simp
show ?thesis
proof (cases even k)
case True
then obtain k’ where k = 2xk’
using evenE by blast
hence cis y = cis y!
using * cos-periodic-int sin-periodic-int
by (simp add: cis.ctr field-simps)
thus ?thesis
using polar «rx # 0» «ry # 0»
by (rule-tac c= in eal, rule-tac z=rz in ez, rule-tac r=ry in exl) simp
next
case False
then obtain k’ where k = 2xk’ + 1
using oddE by blast
hence cis y = — cis yp’
using * cos-periodic-int sin-periodic-int
by (simp add: cis.ctr complez-minus field-simps)
thus ?thesis
using polar «rx # 0» «ry # 0»
by (rule-tac c= in eal, rule-tac c=rz in ezl, rule-tac z=—ry in exI) simp
qed
qed

end

theory Poincare-Lines-Ideal-Points
imports Poincare-Lines

begin
