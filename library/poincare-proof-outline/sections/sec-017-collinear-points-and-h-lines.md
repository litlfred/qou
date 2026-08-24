---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-017-collinear-points-and-h-lines
section_title: "Collinear points and h-lines"
section_number: null
pages: 32-34
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-collinear3-poincare-line-general:
assumes poincare-collinear{a, a1, a2} a1⁄= a2 a1 ⁄= inversion a2
shows a∈ circline-set (poincare-line a1 a2 )
using assms
using poincare-collinear-def unique-poincare-line-general
by auto
lemma poincare-line-poincare-collinear3-general:
assumes a∈ circline-set (poincare-line a1 a2 ) a1⁄= a2
shows poincare-collinear{a, a1, a2}
using assms
unfolding poincare-collinear-def
by (rule-tac x =poincare-line a1 a2 in exI, simp)
lemma poincare-collinear3-poincare-lines-equal-general:
assumes poincare-collinear{a, a1, a2} a⁄= a1 a ⁄= a2 a ⁄= inversion a1 a ⁄= inversion a2
shows poincare-line a a1 = poincare-line a a2
using assms
using unique-poincare-line-general[of a a2 poincare-line a a1 ]
by (simp add : insert-commute poincare-collinear3-poincare-line-general)
4.2.7 Points collinear with 0 h
lemma poincare-collinear-zero-iﬀ:
assumes of-complex y ′∈ unit-disc and of-complex z ′∈ unit-disc and
y ′⁄= z ′ and y ′⁄= 0 and z ′⁄= 0
shows poincare-collinear{0 h, of-complex y ′, of-complex z ′}←→
y ′∗cnj z ′ = cnj y ′∗z ′ (is ?lhs←→ ?rhs)
proof−
have of-complex y ′⁄= of-complex z ′
using assms
using of-complex-inj
by blast
show ?thesis
proof
assume ?lhs
hence 0 h∈ circline-set (poincare-line (of-complex y ′) ( of-complex z ′))
using unique-poincare-line[of of-complex y ′ of-complex z ′]
using assms ‹of-complex y ′⁄= of-complex z ′›
unfolding poincare-collinear-def
by auto
moreover
let ?mix = y ′∗ cnj z ′− cnj y ′∗ z ′
have is-real (i∗ ?mix)
using eq-cnj-iﬀ-real[of ?mix ]
by auto
hence y ′∗ cnj z ′ = cnj y ′∗ z ′←→ Re (i∗ ?mix) = 0
using complex.expand[of i∗ ?mix 0 ]
by (metis complex-i-not-zero eq-iﬀ-diﬀ-eq-0 mult-eq-0-iﬀ zero-complex .simps(1 ) zero-complex.simps(2 ))
ultimately
show ?rhs
using ‹y ′⁄= z ′› ‹y ′⁄= 0 › ‹z ′⁄= 0 ›
unfolding circline-set-def
by simp (transfer, transfer, auto simp add : vec-cnj-def split : if-split-asm, metis Re-complex-of-real Re-mult-real
Im-complex-of-real)
next
assume ?rhs
thus ?lhs
using assms ‹of-complex y ′⁄= of-complex z ′›
unfolding poincare-collinear-def
unfolding circline-set-def
apply (rule-tac x =poincare-line (of-complex y ′) ( of-complex z ′) in exI )
apply auto
apply (transfer, transfer, simp add : vec-cnj-def )
32
done
qed
qed
lemma poincare-collinear-zero-polar-form:
assumes poincare-collinear{0 h, of-complex x, of-complex y} and
x⁄= 0 and y⁄= 0 and of-complex x ∈ unit-disc and of-complex y ∈ unit-disc
shows∃ ϕ rx ry. x = cor rx ∗ cis ϕ∧ y = cor ry ∗ cis ϕ∧ rx⁄= 0∧ ry⁄= 0
proof−
from ‹x⁄= 0 › ‹y⁄= 0 › obtain ϕ ϕ′ rx ry where
polar: x = cor rx ∗ cis ϕ y = cor ry ∗ cis ϕ ′ and ϕ = Arg x ϕ ′ = Arg y
by (metis cmod-cis )
hence rx⁄= 0 ry ⁄= 0
using ‹x⁄= 0 › ‹y⁄= 0 ›
by auto
have of-complex y ∈ circline-set (poincare-line 0 h (of-complex x ))
using assms
using unique-poincare-line[of 0 h of-complex x ]
unfolding poincare-collinear-def
unfolding circline-set-def
using of-complex-zero-iﬀ
by fastforce
hence cnj x ∗ y = x∗ cnj y
using ‹x⁄= 0 › ‹y⁄= 0 ›
unfolding circline-set-def
by simp (transfer, transfer, simp add : vec-cnj-def ﬁeld-simps )
hence cis(ϕ ′− ϕ) = cis(ϕ− ϕ ′)
using polar ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (simp add : cis-mult)
hence sin (ϕ ′− ϕ) = 0
using cis-diﬀ-cis-opposite[of ϕ ′− ϕ]
by simp
then obtain k :: int where ϕ ′− ϕ = k∗ pi
using sin-zero-iﬀ-int2 [of ϕ ′− ϕ]
by auto
hence∗: ϕ ′ = ϕ + k∗ pi
by simp
show ?thesis
proof (cases even k )
case True
then obtain k ′ where k = 2∗k ′
using evenE by blast
hence cis ϕ = cis ϕ ′
using∗ cos-periodic-int sin-periodic-int
by (simp add : cis.ctr ﬁeld-simps )
thus ?thesis
using polar ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (rule-tac x =ϕ in exI, rule-tac x =rx in exI, rule-tac x =ry in exI ) simp
next
case False
then obtain k ′ where k = 2∗k ′ + 1
using oddE by blast
hence cis ϕ =− cis ϕ ′
using∗ cos-periodic-int sin-periodic-int
by (simp add : cis.ctr complex-minus ﬁeld-simps )
thus ?thesis
using polar ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (rule-tac x =ϕ in exI, rule-tac x =rx in exI, rule-tac x =−ry in exI ) simp
qed
qed
end
theory Poincare-Lines-Ideal-Points
imports Poincare-Lines
begin
33
