---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-036-h-betweenness-and-h-collinearity
section_title: "H-betweenness and h-collinearity"
section_number: null
pages: 86-87
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
For three h-collinear points at least one of the three possible h-betweeness relations must hold.

lemma poincare-collinear3-between:
assumes u € unit-disc and v € unit-disc and w € unit-disc
assumes poincare-collinear {u, v, w}
shows poincare-between uv w V poincare-between u wv V poincare-between v uw (is ?P’ uv w)
proof (cases u=v)
case True
thus ?thesis
using assms
by auto
next
case False
have V w. w € unit-dise A poincare-collinear {u, v, w} —+ ?P' wv w (is ?P uv)
proof (rule wlog-positive-x-azis[;where P=?P])
fix x
assume 2: is-real tr 0 < Rex Rex < 1
hence z 4 0
using complez.expand[of x 0]
by auto
hence *: poincare-line 0; (of-complex x) = x-axis
using 2 poincare-line-0-real-is-x-axis|of of-complex «|
unfolding circline-set-x-axis
by auto
have of-complex x € unit-disc
using x
by (auto simp add: cmod-eq-Re)
have of-complex x # On

using <x # 0>

by auto
show ?P 0), (of-complex x)
proof safe

fix w

assume w € unit-disc
assume poincare-collinear {0;,, of-complex x, w}
hence w € circline-set x-axis
using * wnique-poincare-line[of 0), of-complex x] <of-complex x € unit-discy «x # 0» <of-complex x # On>
unfolding poincare-collinear-def
by auto
then obtain w’ where w’: w = of-complez w’ is-real w!'
using (w € unit-disc»
using inf-or-of-complez|of w]
unfolding circline-set-x-azxis
by auto
hence —1 < Rew’ Rew' < 1
using (w € unit-disc»
by (auto simp add: cmod-eq-Re)
assume 1: — poincare-between (of-complex x) On w
hence w 4 0, w' # 0
using w’

86
unfolding poincare-between-def
by auto

hence Re w’ 4 0
using w’ complex.expand[of w' 0]
by auto

have Re w' > 0
using 1 poincare-between-z-axis-u0v[of x w'| «Re x > 0» <is-real x» «x A 0» cw! £ Ov w'
using mult-pos-neg
by force

moreover

assume — poincare-between 0, (of-complex x) w
hence Re w’ < Rez
using poincare-between-z-axis-Ouvlof Re x Re w'|
using w’ x (-1 < Rew’ ‘Rew’ < 1) ‘Rew’ F O>
by auto

ultimately
show poincare-between 0}, w (of-complex x)
using poincare-between-z-axis-Ouvlof Re w' Re x]
using w’ x (-1 < Rew’ ‘Rew’ < 1) ‘Rew’ # 0»
by auto
qed
next
show u € unit-disc v € unit-disc u A v
by fact+
next
fix Muv
assume 1: unit-disc-fiz M u € unit-disc v € unit-disc u # v
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt M v
assume 2: ?P ?Mu ?Mv
show ?P uv
proof safe
fix w
assume w € unit-disc poincare-collinear {u, v, w} 7 poincare-between u v w > poincare-between v uw
thus poincare-between u wv
using 1{ 2[rule-format, of moebius-pt M w]
by simp
qed
qed
thus ?thesis
using assms
by simp
qed

lemma poincare-collinear3-iff :
assumes u € unit-disc v € unit-disc w € unit-disc
shows poincare-collinear {u, v, w} <—> poincare-between uv w V poincare-between v uw V poincare-between v wu
using assms
by (metis poincare-collinear3-between insert-commute poincare-between-poincare-collinear poincare-between-rev)
