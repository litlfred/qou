---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-061-continuity-axiom
section_title: "Continuity axiom"
section_number: null
pages: 150-157
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The set φ is on the left of the set ψ
abbreviation set-order where
set-order A ϕ ψ≡∀ x∈ unit-disc.∀ y∈ unit-disc. ϕ x∧ ψ y−→ poincare-between A x y
The point B is between the sets φ and ψ
abbreviation point-between-sets where
point-between-setsϕ B ψ≡∀ x∈ unit-disc.∀ y∈ unit-disc. ϕ x∧ ψ y−→ poincare-between x B y
lemma continuity:
assumes∃ A∈ unit-disc. set-order A ϕ ψ
150
shows ∃ B∈ unit-disc. point-between-setsϕ B ψ
proof (cases (∃ x0∈ unit-disc. ϕx0 )∧ (∃ y0∈ unit-disc. ψ y0 ))
case False
thus ?thesis
using assms by blast
next
case True
then obtain Y0 where ψ Y0 Y0 ∈ unit-disc
by auto
obtain A where∗: A∈ unit-disc set-order A ϕ ψ
using assms
by auto
show ?thesis
proof (cases∀ x∈ unit-disc. ϕx−→ x = A)
case True
thus ?thesis
using ‹A∈ unit-disc›
using poincare-between-nonstrict(1 ) by blast
next
case False
then obtain X0 where ϕ X0 X0 ⁄= A X0 ∈ unit-disc
by auto
have Y0⁄= A
proof (rule ccontr )
assume¬ Y0⁄= A
hence∀ x∈ unit-disc. ϕx−→ poincare-between A x A
using∗ ‹ψ Y0 ›
by (cases A ) force
hence∀ x∈ unit-disc. ϕx−→ x = A
using∗ poincare-between-sandwich by blast
thus False
using False by auto
qed
show ?thesis
proof (cases∃ B∈ unit-disc. ϕB∧ ψ B)
case True
then obtain B where B∈ unit-disc ϕ B ψ B
by auto
hence∀ x∈ unit-disc. ϕx−→ poincare-between A x B
using∗ by auto
have∀ y∈ unit-disc. ψ y−→ poincare-between A B y
using∗ ‹B∈ unit-disc› ‹ϕ B›
by auto
show ?thesis
proof (rule+)
show B∈ unit-disc
by fact
next
ﬁx x y
assume x∈ unit-disc y ∈ unit-disc ϕ x∧ ψ y
hence poincare-between A x B poincare-between A B y
using ‹∀ x∈ unit-disc. ϕx−→ poincare-between A x B ›
using ‹∀ y∈ unit-disc. ψ y−→ poincare-between A B y ›
by simp+
thus poincare-between x B y
using ‹x∈ unit-disc› ‹y∈ unit-disc› ‹B∈ unit-disc› ‹A∈ unit-disc›
using poincare-between-transitivity[of A x B y ]
by simp
qed
next
case False
have poincare-between A X0 Y0
using ‹ϕ X0 › ‹ψ Y0 ›∗ ‹Y0∈ unit-disc› ‹X0∈ unit-disc›
by auto
151
have∀ ϕ.∀ ψ. set-order A ϕ ψ∧¬ (∃ B∈ unit-disc. ϕB∧ ψ B)∧ ϕ X0∧
(∃ y∈ unit-disc. ψ y)∧ (∃ x∈ unit-disc. ϕx)
−→ (∃ B∈ unit-disc. point-between-setsϕ B ψ)
(is ?P A X0 )
proof (rule wlog-positive-x-axis [where P=?P])
show A∈ unit-disc
by fact
next
show X0∈ unit-disc
by fact
next
show A⁄= X0
using ‹X0⁄= A› by simp
next
ﬁx M u v
let ?M = λ x. moebius-pt M x
let ?Mu = ?M u and ?Mv = ?M v
assume hip: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
?P ?Mu ?Mv
show ?P u v
proof safe
ﬁx ϕ ψ x y
assume set-order u ϕ ψ¬ (∃ B∈unit-disc. ϕB∧ ψ B) ϕ v
y∈ unit-disc ψ y x ∈ unit-disc ϕ x
let ?Mϕ = λ X ′.∃ X. ϕX∧ ?M X = X ′
let ?Mψ = λ X ′.∃ X. ψ X∧ ?M X = X ′
obtain Mϕ where Mϕ = ?Mϕ by simp
obtain Mψ where Mψ = ?Mψ by simp
have Mϕ ?Mv
using ‹ϕ v› using ‹Mϕ = ?Mϕ›
by blast
moreover
have¬ (∃ B∈unit-disc. Mϕ B∧ Mψ B)
using ‹¬ (∃ B∈unit-disc. ϕB∧ ψ B)›
using ‹Mϕ = ?Mϕ› ‹Mψ = ?Mψ›
by (metis hip (1 ) moebius-pt-invert unit-disc-ﬁx-discI unit-disc-ﬁx-moebius-inv )
moreover
have∃ y∈ unit-disc. Mψ y
using ‹y∈ unit-disc› ‹ψ y› ‹ Mψ = ?Mψ› ‹unit-disc-ﬁx M ›
by auto
moreover
have set-order ?Mu ?M ϕ ?Mψ
proof ((rule ballI )+, rule impI )
ﬁx Mx My
assume Mx∈ unit-disc My ∈ unit-disc ?Mϕ Mx∧ ?Mψ My
then obtain x y where ϕ x∧ ?M x = Mx ψ y∧ ?M y = My
by blast
hence x∈ unit-disc y ∈ unit-disc
using ‹Mx∈ unit-disc› ‹My∈ unit-disc› ‹unit-disc-ﬁx M ›
by (metis moebius-pt-comp-inv-left unit-disc-ﬁx-discI unit-disc-ﬁx-moebius-inv )+
hence poincare-between u x y
using ‹set-order u ϕ ψ›
using ‹Mx∈ unit-disc› ‹My∈ unit-disc› ‹ϕ x∧ ?M x = Mx› ‹ψ y∧ ?M y = My›
by blast
then show poincare-between ?Mu Mx My
using ‹ϕ x∧ ?M x = Mx› ‹ψ y∧ ?M y = My›
using ‹x∈ unit-disc› ‹y∈ unit-disc› ‹u∈ unit-disc› ‹unit-disc-ﬁx M ›
using unit-disc-ﬁx-moebius-preserve-poincare-betweenby blast
qed
hence set-order ?Mu M ϕ Mψ
152
using ‹Mϕ = ?Mϕ› ‹Mψ = ?Mψ›
by simp
ultimately
have∃ Mb∈ unit-disc. point-between-sets Mϕ Mb Mψ
using hip(5 )
by blast
then obtain Mb where bbb:
Mb∈ unit-disc point-between-sets ?Mϕ Mb ?Mψ
using ‹Mϕ = ?Mϕ› ‹Mψ = ?Mψ›
by auto
let ?b = moebius-pt (moebius-inv M ) Mb
show∃ b∈ unit-disc. point-between-setsϕ b ψ
proof (rule-tac x =?b in bexI, (rule ballI )+, rule impI )
ﬁx x y
assume x∈ unit-disc y ∈ unit-disc ϕ x∧ ψ y
hence poincare-between u x y
using ‹set-order u ϕ ψ›
by blast
let ?Mx = ?M x and ?My = ?M y
have ?Mϕ ?Mx ?Mψ ?My
using ‹ϕ x∧ ψ y›
by blast+
have ?Mx∈ unit-disc ?My ∈ unit-disc
using ‹x∈ unit-disc› ‹unit-disc-ﬁx M › ‹y∈ unit-disc›
by auto
hence poincare-between ?Mx Mb ?My
using ‹?Mϕ ?Mx› ‹?Mψ ?My› ‹?Mx∈ unit-disc› ‹?My∈ unit-disc› bbb
by auto
then show poincare-between x ?b y
using ‹unit-disc-ﬁx M ›
using ‹x∈ unit-disc› ‹y∈ unit-disc› ‹Mb∈ unit-disc› ‹?Mx∈ unit-disc› ‹?My∈ unit-disc›
using unit-disc-ﬁx-moebius-preserve-poincare-between[of M x ?b y ]
by auto
next
show ?b∈ unit-disc
using bbb ‹unit-disc-ﬁx M ›
by auto
qed
qed
next
ﬁx X
assume xx: is-real X 0 < Re X Re X < 1
let ?X = of-complex X
show ?P 0 h ?X
proof ((rule allI )+, rule impI, (erule conjE )+)
ﬁx ϕ ψ
assume set-order 0 h ϕ ψ¬ (∃ B∈unit-disc. ϕB∧ ψ B) ϕ ?X
∃ y∈unit-disc. ψ y∃ x∈unit-disc. ϕx
have ?X∈ unit-disc
using xx
by (simp add : cmod-eq-Re)
haveψpos:∀ y∈ unit-disc. ψ y−→ (is-real (to-complex y )∧ Re (to-complex y ) > 0 )
proof (rule ballI, rule impI )
ﬁx y
let ?y = to-complex y
assume y∈ unit-disc ψ y
hence poincare-between 0h ?X y
using ‹set-order 0 h ϕ ψ›
using ‹?X∈ unit-disc› ‹ϕ ?X ›
153
by auto
thus is-real ?y∧ 0 < Re ?y
using xx ‹?X∈ unit-disc› ‹y∈ unit-disc›
by (metis (mono-tags, opaque-lifting) arg-0-iﬀ of-complex-zero-iﬀ poincare-between-0uv poincare-between-sandwich
to-complex-of-complex unit-disc-to-complex-inj zero-in-unit-disc )
qed
haveϕnoneg:∀ x∈ unit-disc. ϕx−→ (is-real (to-complex x )∧ Re (to-complex x )≥ 0 )
proof (rule ballI, rule impI )
ﬁx x
assume x∈ unit-disc ϕ x
obtain y where y∈ unit-disc ψ y
using ‹∃ y∈ unit-disc. ψ y› by blast
let ?x = to-complex x and ?y = to-complex y
have is-real ?y Re ?y > 0
using ψpos ‹ψ y› ‹y∈ unit-disc›
by auto
have poincare-between 0h x y
using ‹set-order 0 h ϕ ψ›
using ‹x∈ unit-disc› ‹ϕ x› ‹y∈unit-disc› ‹ψ y›
by auto
thus is-real ?x ∧ 0≤ Re ?x
using ‹x∈ unit-disc› ‹y∈ unit-disc› ‹is-real (to-complex y )› ‹ψ y›
using ‹set-order 0 h ϕ ψ›
using ‹ϕ ?X › ‹?X∈ unit-disc› ‹Re ?y > 0 ›
by (metis arg-0-iﬀ le-less of-complex-zero poincare-between-0uv to-complex-of-complex zero-complex .simps(1 )
zero-complex.simps(2 ))
qed
haveϕlessψ:∀ x∈unit-disc.∀ y∈unit-disc. ϕx∧ ψ y−→ Re (to-complex x ) < Re (to-complex y )
proof ((rule ballI )+, rule impI )
ﬁx x y
let ?x = to-complex x and ?y = to-complex y
assume x∈ unit-disc y ∈ unit-disc ϕ x∧ ψ y
hence poincare-between 0h x y
using ‹set-order 0 h ϕ ψ›
by auto
moreover
have is-real ?x Re ?x ≥ 0
using ϕnoneg
using ‹x∈ unit-disc› ‹ϕ x∧ ψ y› by auto
moreover
have is-real ?y Re ?y > 0
using ψpos
using ‹y∈ unit-disc› ‹ϕ x∧ ψ y› by auto
ultimately
have Re ?x ≤ Re ?y
using ‹x∈ unit-disc› ‹y∈ unit-disc›
by (metis Re-complex-of-real arg-0-iﬀ le-less of-complex-zero poincare-between-0uv rcis-cmod-Arg rcis-zero-arg
to-complex-of-complex)
have Re ?x ⁄= Re ?y
using ‹ϕ x∧ ψ y› ‹is-real ?x › ‹is-real ?y ›
using ‹¬ (∃ B∈unit-disc. ϕB∧ ψ B)› ‹x∈ unit-disc› ‹y∈ unit-disc›
by (metis complex.expand unit-disc-to-complex-inj )
thus Re ?x < Re ?y
using ‹Re ?x ≤ Re ?y › by auto
qed
154
have∃ b∈ unit-disc.∀ x∈ unit-disc.∀ y∈ unit-disc.
is-real (to-complex b )∧
(ϕ x∧ ψ y−→ (Re (to-complex x )≤ Re (to-complex b )∧ Re (to-complex b )≤ Re (to-complex y )))
proof−
let ?Phi ={x. (of-complex (cor x ))∈ unit-disc∧ ϕ (of-complex (cor x ))}
have∀ x∈ unit-disc. ϕx−→ Re (to-complex x )≤ Sup ?Phi
proof (safe)
ﬁx x
let ?x = to-complex x
assume x∈ unit-disc ϕ x
hence is-real ?x Re ?x ≥ 0
using ϕnoneg
by auto
hence cor (Re ?x ) = ?x
using complex-of-real-Re by blast
hence of-complex (cor (Re ?x ))∈ unit-disc
using ‹x∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
moreover
haveϕ (of-complex (cor (Re ?x )))
using ‹cor (Re ?x ) = ?x› ‹ϕ x› ‹x∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
ultimately
have Re ?x ∈ ?Phi
by auto
have∃ M.∀ x∈ ?Phi. x≤ M
using ϕlessψ
using ‹∃ y∈ unit-disc. ψ y›
by (metis (mono-tags, lifting) Re-complex-of-real le-less mem-Collect-eq to-complex-of-complex )
thus Re ?x ≤ Sup ?Phi
using cSup-upper[of Re ?x ?Phi ]
unfolding bdd-above-def
using ‹Re ?x ∈ ?Phi›
by auto
qed
have∀ y∈ unit-disc. ψ y−→ Sup ?Phi ≤ Re (to-complex y )
proof (safe)
ﬁx y
let ?y = to-complex y
assume ψ y y ∈ unit-disc
show Sup ?Phi ≤ Re ?y
proof (rule ccontr )
assume¬ ?thesis
hence Re ?y < Sup ?Phi
by auto
have∃ x. ϕ(of-complex (cor x ))∧ (of-complex (cor x ))∈ unit-disc
proof −
obtain x ′ where x ′∈ unit-disc ϕ x ′
using ‹∃ x∈ unit-disc. ϕx› by blast
let ?x ′ = to-complex x ′
have is-real ?x ′
using ‹x ′∈ unit-disc› ‹ϕ x ′›
using ϕnoneg
by auto
hence cor (Re ?x ′) = ?x ′
using complex-of-real-Re by blast
hence x ′ = of-complex (cor (Re ?x ′))
using ‹x ′∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
show ?thesis
155
apply (rule-tac x =Re ?x ′ in exI )
using ‹x ′∈ unit-disc›
apply (subst (asm) ‹x ′ = of-complex (cor (Re ?x ′))›, simp)
using ‹ϕ x ′›
by (subst (asm) ( 2 ) ‹x ′ = of-complex (cor (Re ?x ′))›, simp)
qed
hence ?Phi⁄={}
by auto
then obtain x where ϕ (of-complex (cor x )) Re ?y < x
(of-complex (cor x ))∈ unit-disc
using ‹Re ?y < Sup ?Phi ›
using less-cSupE[of Re ?y ?Phi ]
by auto
moreover
have Re ?y < Re (to-complex (of-complex (cor x )))
using ‹Re ?y < x›
by simp
ultimately
show False
using ϕlessψ
using ‹ψ y› ‹y∈ unit-disc›
by (metis less-not-sym )
qed
qed
thus ?thesis
using ‹∀ x∈ unit-disc. ϕx−→ Re (to-complex x )≤ Sup ?Phi ›
apply (rule-tac x =(of-complex (cor (Sup ?Phi ))) in bexI, simp)
using ‹∃ y∈unit-disc. ψ y› ‹ϕ ?X › ‹?X∈ unit-disc›
using ‹∀ y∈unit-disc. ψ y−→ is-real (to-complex y )∧ 0 < Re (to-complex y )›
by (smt complex-of-real-Re inf-notin-unit-disc norm-of-real of-complex-to-complex to-complex-of-complex
unit-disc-iﬀ-cmod-lt-1 xx (2 ))
qed
then obtain B where B∈ unit-disc is-real (to-complex B )
∀ x∈unit-disc.∀ y∈unit-disc. ϕx∧ ψ y−→ Re (to-complex x )≤ Re (to-complex B )∧
Re (to-complex B )≤ Re (to-complex y )
by blast
show∃ b∈ unit-disc. point-between-setsϕ b ψ
proof (rule-tac x =B in bexI)
show B∈ unit-disc
by fact
next
show point-between-setsϕ B ψ
proof ((rule ballI )+, rule impI )
ﬁx x y
let ?x = to-complex x and ?y = to-complex y and ?B = to-complex B
assume x∈ unit-disc y ∈ unit-disc ϕ x∧ ψ y
hence Re ?x ≤ Re ?B ∧ Re ?B ≤ Re ?y
using ‹∀ x∈unit-disc.∀ y∈unit-disc. ϕx∧ ψ y−→ Re (to-complex x )≤ Re ?B ∧
Re (to-complex B )≤ Re (to-complex y )›
by auto
moreover
have is-real ?x Re ?x ≥ 0
using ϕnoneg
using ‹x∈ unit-disc› ‹ϕ x∧ ψ y›
by auto
moreover
have is-real ?y Re ?y > 0
using ψpos
using ‹y∈ unit-disc› ‹ϕ x∧ ψ y›
by auto
156
moreover
have cor (Re ?x ) = ?x
using complex-of-real-Re ‹is-real ?x › by blast
hence x = of-complex (cor (Re ?x ))
using ‹x∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
moreover
have cor (Re ?y ) = ?y
using complex-of-real-Re ‹is-real ?y › by blast
hence y = of-complex (cor (Re ?y ))
using ‹y∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
moreover
have cor (Re ?B ) = ?B
using complex-of-real-Re ‹is-real (to-complex B )› by blast
hence B = of-complex (cor (Re ?B ))
using ‹B∈ unit-disc›
by (metis inf-notin-unit-disc of-complex-to-complex )
ultimately
show poincare-between x B y
using ‹is-real (to-complex B )› ‹x∈ unit-disc› ‹y∈ unit-disc› ‹B∈ unit-disc›
using poincare-between-x-axis-uvw[of Re (to-complex x ) Re (to-complex B ) Re (to-complex y )]
by (smt Re-complex-of-real arg-0-iﬀ poincare-between-nonstrict(1 ) rcis-cmod-Arg rcis-zero-arg unit-disc-iﬀ-cmod-lt-1)
qed
qed
qed
qed
thus ?thesis
using False ‹ϕ X0 › ‹ψ Y0 ›∗ ‹Y0∈ unit-disc› ‹X0∈ unit-disc›
by auto
qed
qed
qed
