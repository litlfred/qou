---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-027-congruent-triangles
section_title: "Congruent triangles"
section_number: null
pages: 74-77
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
For every pair of triangles such that its three pairs of sides are pairwise equal there is an h-isometry (a unit disc
preserving Möbius transform, eventually composed with a conjugation) that maps one triangle onto the other.
lemma unit-disc-ﬁx-f-congruent-triangles:
assumes
in-disc: u∈ unit-disc v ∈ unit-disc w ∈ unit-disc and
in-disc ′: u ′∈ unit-disc v ′∈ unit-disc w ′∈ unit-disc and
d: poincare-distance u v = poincare-distance u ′ v ′
poincare-distance v w = poincare-distance v ′ w ′
poincare-distance u w = poincare-distance u ′ w ′
shows
∃ M. unit-disc-ﬁx-f M ∧ M u = u ′∧ M v = v ′∧ M w = w ′
proof (cases u = v∨ u = w∨ v = w)
case True
thus ?thesis
using assms
using poincare-distance-eq-0-iﬀ[of u ′ v ′]
using poincare-distance-eq-0-iﬀ[of v ′ w ′]
using poincare-distance-eq-0-iﬀ[of u ′ w ′]
using poincare-distance-eq-ex-moebius[of v w v ′ w ′]
using poincare-distance-eq-ex-moebius[of u w u ′ w ′]
using poincare-distance-eq-ex-moebius[of u v u ′ v ′]
by (metis unit-disc-ﬁx-f-def )
next
case False
have∀ w u ′ v ′ w ′. w∈ unit-disc∧ u ′∈ unit-disc∧ v ′∈ unit-disc∧ w ′∈ unit-disc∧ w⁄= u∧ w⁄= v∧
poincare-distance u v = poincare-distance u ′ v ′∧
poincare-distance v w = poincare-distance v ′ w ′∧
74
poincare-distance u w = poincare-distance u ′ w ′−→
(∃ M. unit-disc-ﬁx-f M ∧ M u = u ′∧ M v = v ′∧ M w = w ′) ( is ?P u v )
proof (rule wlog-positive-x-axis [where P=?P])
show v∈ unit-disc u ∈ unit-disc
by fact+
next
show u⁄= v
using False
by simp
next
ﬁx x
assume x: is-real x 0 < Re x Re x < 1
hence of-complex x ⁄= 0 h
using of-complex-zero-iﬀ [of x ]
by (auto simp add : complex.expand)
show ?P 0 h (of-complex x )
proof safe
ﬁx w u ′ v ′ w ′
assume in-disc: w∈ unit-disc u ′∈ unit-disc v ′∈ unit-disc w ′∈ unit-disc
assume poincare-distance 0 h (of-complex x ) = poincare-distance u ′ v ′
then obtain M ′ where M ′: unit-disc-ﬁx M ′ moebius-pt M ′ u ′ = 0 h moebius-pt M ′ v ′ = ( of-complex x )
using poincare-distance-eq-ex-moebius[of u ′ v ′ 0 h of-complex x ] in-disc x
by (auto simp add : cmod-eq-Re)
let ?w = moebius-pt M ′ w ′
have ?w∈ unit-disc
using ‹unit-disc-ﬁx M ′› ‹w ′∈ unit-disc›
by simp
assume w⁄= 0 h w⁄= of-complex x
hence dist-gt-0 : poincare-distance 0 h w > 0 poincare-distance (of-complex x ) w > 0
using poincare-distance-eq-0-iﬀ[of 0 h w] in-disc poincare-distance-ge0 [of 0 h w]
using poincare-distance-eq-0-iﬀ[of of-complex x w ] in-disc poincare-distance-ge0 [of of-complex x w ]
using x
by (simp-all add : cmod-eq-Re)
assume poincare-distance (of-complex x ) w = poincare-distance v ′ w ′
poincare-distance 0 h w = poincare-distance u ′ w ′
hence poincare-distance 0 h ?w = poincare-distance 0 h w
poincare-distance (of-complex x ) ?w = poincare-distance (of-complex x ) w
using M ′(1 ) M ′(2 )[symmetric] M ′(3 )[symmetric] in-disc
using unit-disc-ﬁx-preserve-poincare-distance[of M ′ u ′ w ′]
using unit-disc-ﬁx-preserve-poincare-distance[of M ′ v ′ w ′]
by simp-all
hence ?w ∈ poincare-circle 0 h (poincare-distance 0 h w) ∩ poincare-circle (of-complex x ) ( poincare-distance
(of-complex x ) w)
w∈ poincare-circle 0h (poincare-distance 0h w)∩ poincare-circle (of-complex x ) ( poincare-distance (of-complex
x) w)
using ‹?w∈ unit-disc› ‹w∈ unit-disc›
unfolding poincare-circle-def
by simp-all
hence ?w = w∨ ?w = conjugate w
using intersect-poincare-circles-x-axis[of 0 x poincare-distance 0 h w poincare-distance (of-complex x ) w ?w w ] x
using ‹of-complex x ⁄= 0 h› dist-gt-0
using poincare-distance-eq-0-iﬀ
by auto
thus∃ M. unit-disc-ﬁx-f M ∧ M 0 h = u ′∧ M (of-complex x ) = v ′∧ M w = w ′
proof
assume moebius-pt M ′ w ′ = w
thus ?thesis
using M ′
using moebius-pt-invert[of M ′ u ′ 0 h]
using moebius-pt-invert[of M ′ v ′ of-complex x ]
using moebius-pt-invert[of M ′ w ′ w]
75
apply (rule-tac x =moebius-pt (−M ′) in exI )
apply (simp add : unit-disc-ﬁx-f-def )
apply (rule-tac x =−M ′ in exI, simp)
done
next
let ?M = moebius-pt (−M ′)◦ conjugate
assume moebius-pt M ′ w ′ = conjugate w
hence ?M w = w ′
using moebius-pt-invert[of M ′ w ′ conjugate w ]
by simp
moreover
have ?M 0 h = u ′ ?M (of-complex x ) = v ′
using moebius-pt-invert[of M ′ u ′ 0 h]
using moebius-pt-invert[of M ′ v ′ of-complex x ]
using M ′ ‹is-real x › eq-cnj-iﬀ-real[of x ]
by simp-all
moreover
have unit-disc-ﬁx-f ?M
using ‹unit-disc-ﬁx M ′›
unfolding unit-disc-ﬁx-f-def
by (rule-tac x =−M ′ in exI, simp)
ultimately
show ?thesis
by blast
qed
qed
next
ﬁx M u v
assume 1 : unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v
assume 2 : ?P ?Mu ?Mv
show ?P u v
proof safe
ﬁx w u ′ v ′ w ′
let ?Mw = moebius-pt M w and ?Mu ′ = moebius-pt M u ′ and ?Mv ′ = moebius-pt M v ′ and ?Mw ′ = moebius-pt
M w ′
assume w∈ unit-disc u ′∈ unit-disc v ′∈ unit-disc w ′∈ unit-disc w ⁄= u w ⁄= v
poincare-distance u v = poincare-distance u ′ v ′
poincare-distance v w = poincare-distance v ′ w ′
poincare-distance u w = poincare-distance u ′ w ′
then obtain M ′ where M ′: unit-disc-ﬁx-f M ′ M ′ ?Mu = ?Mu ′ M ′ ?Mv = ?Mv ′ M ′ ?Mw = ?Mw ′
using 1 2 [rule-format, of ?Mw ?Mu ′ ?Mv ′ ?Mw ′]
by auto
let ?M = moebius-pt (−M )◦ M ′◦ moebius-pt M
show∃ M. unit-disc-ﬁx-f M ∧ M u = u ′∧ M v = v ′∧ M w = w ′
proof (rule-tac x =?M in exI, safe)
show unit-disc-ﬁx-f ?M
using M ′(1 ) ‹unit-disc-ﬁx M ›
by (subst unit-disc-ﬁx-f-comp, subst unit-disc-ﬁx-f-comp, simp-all )
next
show ?M u = u ′ ?M v = v ′ ?M w = w ′
using M ′
by auto
qed
qed
qed
thus ?thesis
using assms False
by auto
qed
end
theory Poincare-Between
imports Poincare-Distance
begin
76
