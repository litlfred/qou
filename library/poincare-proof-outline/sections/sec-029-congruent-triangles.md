---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-029-congruent-triangles
section_title: "Congruent triangles"
section_number: null
pages: 74-77
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
For every pair of triangles such that its three pairs of sides are pairwise equal there is an h-isometry (a unit disc
preserving Mobius transform, eventually composed with a conjugation) that maps one triangle onto the other.

lemma unit-disc-fiz-f-congruent-triangles:
assumes
in-disc: u € unit-disc v € unit-disc w € unit-disc and
in-disc’: u' € unit-disc v' € unit-disc w’ € unit-disc and
d: poincare-distance uv = poincare-distance u’ v!
poincare-distance v w = poincare-distance v' w’
poincare-distance uw = poincare-distance u' w’
shows
3M. unit-disc-fic-fM \ Mu=u'AMv=v'AMw=w’'
proof (casesu=vVu=wVv=w)
case True
thus ?thesis
using assms
using poincare-distance-eq-0-iff [of u' v'|
using poincare-distance-eq-0-iff [of v' w'|
using poincare-distance-eq-0-iff [of u’ w']
using poincare-distance-eq-ex-mocbius|of v wv’ w']
using poincare-distance-eq-ex-moebius|of u wu’ w’|
using poincare-distance-eq-ex-moebius|of uv u’ v'|
by (metis wnit-disc-fix-f-def )
next
case False

have V wu! vu’ w’. w € unit-dise A u' € unit-disc A v' € unit-disc A w' € unit-disc \wAuANwAVA

poincare-distance uv = poincare-distance u' v' A
poincare-distance v w = poincare-distance v' w’ A

74
poincare-distance u w = poincare-distance u' w' —>
(A M. unit-disc-fic-f MA Mu=u' A Mv=0'A Mw=vw’) (is ?P uv)
proof (rule wlog-positive-x-azis[;where P=?P])
show v € unit-disc u € unit-disc
by fact+
next
show u #v
using False
by simp
next
fix x
assume 2: is-real tr 0 < Rex Rex < 1

hence of-compler « # On
using of-complez-zero-iff [of 2]
by (auto simp add: complex.expand)

show ?P 0), (of-complex x)
proof safe
fix wu’ vw’
assume in-disc: w € unit-disc u’ € unit-disc v' € unit-disc w' € unit-disc
assume poincare-distance 0}, (of-complex x) = poincare-distance u' v’
then obtain M’ where M’: unit-disc-fix M' moebius-pt M’ u' = 0n moebius-pt M' v’ = (of-complex x)
using poincare-distance-eq-ex-moebius|of u' v' 0), of-complex x] in-disc x
by (auto simp add: cmod-eq-Re)
let ?w = moebius-pt M’ w’
have ?w € unit-disc
using <unit-disc-fir M'> «w' € unit-disc»
by simp

assume w # 0n w ¥ of-complex &
hence dist-gt-0: poincare-distance 0;, w > 0 poincare-distance (of-complex x) w > 0
using poincare-distance-eq-0-iff|of On w] in-disc poincare-distance-ge0 [of On w)
using poincare-distance-eq-0-iff [of of-complex x w| in-disc poincare-distance-ge0|of of-complex x w]
using x
by (simp-all add: cmod-eq-Re)

assume poincare-distance (of-complex x) w = poincare-distance v' w’
poincare-distance 0, w = poincare-distance u' w’
hence poincare-distance 0, ?w = poincare-distance 0, w
poincare-distance (of-complex x) ?w = poincare-distance (of-complex x) w
using M'(1) M'(2)[symmetric] M'(3)|[symmetric] in-disc
using unit-disc-fir-preserve-poincare-distance|of M' u’ w’|
using unit-disc-fir-preserve-poincare-distance|of M' v' w']
by simp-all
hence ?w € poincare-circle 0, (poincare-distance 0; w) M poincare-circle (of-complex x) (poincare-distance
(of-complex x) w)
w € poincare-circle 0, (poincare-distance 0, w)  poincare-circle (of-complex x) (poincare-distance (of-complex
x) w)
using <?w € unit-discy (w € unit-discy
unfolding poincare-circle-def
by simp-all
hence ?w = w V ?w = conjugate w
using intersect-poincare-circles-x-axis|of 0 x poincare-distance 0, w poincare-distance (of-complex x) w ?w w] x
using <of-compler x # 0;,) dist-gt-0
using poincare-distance-eq-0-iff
by auto
thus 4M. unit-disc-fir-f M \ M 0; = u' A M (of-complex z) = v' A Mw = w'
proof
assume moebius-pt M' w! = w
thus ?thesis
using M’
using mocbius-pt-invert[of M’ u’ 0;)
using moebius-pt-invert|of M' v' of-complez x]
using mocbius-pt-invert[of M’ w’ wl
apply (rule-tac c=moebius-pt (—M’) in eal)
apply (simp add: unit-disc-fix-f-def)
apply (rule-tac z=—M' in ezl, simp)

done
next
let ?M = moebius-pt (—M') © conjugate
assume mocbius-pt M' w' = conjugate w

hence ?M w= w’
using mocbius-pt-invert[of M’' w' conjugate w|
by simp
moreover
have ?M 0; = u' ?M (of-complex x) = v'
using moebius-pt-invert[of M’ u’ 0]
using mocbius-pt-invert|of M‘ v’ of-complex |
using M’ ¢is-real x» eq-cnj-iff-real|of 2]
by simp-all
moreover
have unit-disc-fix-f ?M
using <unit-disc-fix M'y
unfolding unit-disc-fix-f-def
by (rule-tac z=—M' in exI, simp)
ultimately
show ?thesis
by blast
qed
qed
next
fix Muv
assume 1: unit-disc-fiz M u € unit-disc v € unit-disc
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt M v
assume 2: ?P ?Mu ?Mv
show ?P uv
proof safe
fix wu’ v' w’
let ?Mw = moebius-pt Mw and ?Mu' = moebius-pt M u' and ?Mv' = moebius-pt M v' and ?Mw' = moebius-pt
Mw’
assume w € unit-disc u' € unit-disc v' € unit-disc w' € unit-disc wAuwHAv
poincare-distance uv = poincare-distance u’ v'
poincare-distance v w = poincare-distance v' w’
poincare-distance uw = poincare-distance u' w’
then obtain M’ where M’: unit-disc-fir-f M’ M’ ?Mu = ?Mu' M' ?Mv = ?Mv' M’ ?Mw = ?Mw’
using J 2[rule-format, of ?7Mw ?Mu’ ?Mv' ?Mw’|
by auto

let ?M = moebius-pt (-M) o M'o moebius-pt M
show 4M. unit-disc-fiz-f MA Mu=u'A\Mv=0'AMw=vw'
proof (rule-tac z=?M in exl, safe)
show unit-disc-fit-f ?M
using M'(1) <unit-disc-fix M>
by (subst unit-disc-fix-f-comp, subst unit-disc-fix-f-comp, simp-all)
next
show ?Mu=u' ?Mv=0' *(Mw=w’'
using M’
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
