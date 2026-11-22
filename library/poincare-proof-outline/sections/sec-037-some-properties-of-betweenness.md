---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-037-some-properties-of-betweenness
section_title: "Some properties of betweenness"
section_number: null
pages: 87-89
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-between-transitivity:
assumes a € unit-disc and z € unit-disc and b € unit-disc and y € unit-disc and
poincare-between a x b and poincare-between a b y
shows poincare-between x b y
proof (cases a = b)
case True
thus ?thesis
using assms
using poincare-between-sandwich by blast
next
case False

87
have V z. V y. poincare-between a x b \ poincare-between a b y \ x € unit-disc
A y € unit-dise —+ poincare-between x b y (is ?P a b)
proof (rule wlog-positive-x-azis[;where P=?P])
show a € unit-disc
using assms by simp
next
show b € unit-disc
using assms by simp
next
show a + b
using False by simp
next
fix Muv
assume *: unit-disc-fix M u € unit-disc v € unit-disc u # v
Va y. poincare-between (moebius-pt M u) x (moebius-pt M v) A
poincare-between (moebius-pt M u) (moebius-pt M v) y A
a € unit-disc \ y € unit-disc —>
poincare-between x (moebius-pt M v) y
show Vz y. poincare-between u x v A poincare-between uv y A « € unit-disc \ y € unit-disc
—> poincare-between xv y
proof safe
fix ry
assume poincare-between u x v poincare-between uv y x € unit-disc y € unit-disc

have poincare-between (moebius-pt M u) (moebius-pt M x) (moebius-pt M v)
using <poincare-between u x v> <unit-disc-fix My «x € unit-discy (u € unit-disc> <v € unit-disc)
by simp

moreover

have poincare-between (moebius-pt M u) (moebius-pt M v) (moebius-pt M y)
using <poincare-between u v y> <unit-disc-fix M> <y € unit-disc) (wu € unit-discy «v € unit-disc»
by simp

moreover

have (moebius-pt M x) € unit-disc
using <unit-disc-fix M> «x € unit-discy by simp

moreover

have (moebius-pt M y) € unit-disc
using <unit-disc-fix M> <y € unit-discy by simp

ultimately

have poincare-between (moebius-pt M x) (moebius-pt M v) (moebius-pt M y)
using * by blast

thus poincare-between xv y
using <y € unit-disc) * (x € unit-disc) by simp

qed
next
fix x
assume zz: is-realaz 0 < Rex Rex < 1
hence of-complez « € unit-disc
using cmod-eq-Re by auto
hence of-complex « # on
by simp
have of-compler x # On
using «tz by auto
have of-complex x € circline-set x-axis
using zx by simp
show Vm n. poincare-between 0, m (of-complex x) A poincare-between 0), (of-complex x) n A
m € unit-disc A n € unit-disc —>+ poincare-between m (of-complex x) n
proof safe
fix mn
assume **: poincare-between 0; m (of-complez x) poincare-between 0), (of-complex x) n
m € unit-disc n € unit-disc

show poincare-between m (of-complex x) n

proof (cases m = 0p)
case True
thus ?thesis

using ** by auto
next

88
case False
hence m € circline-set x-axis
using poincare-between-poincare-line-uzvlof On of-complex x m]
using poincare-line-0-real-is-x-axis|of of-complex x]
using <of-complex x € unit-disc) <of-complex x # con? <of-compler x # On>
using <of-complex x € circline-set z-axis» «m € unit-discy **(1)
by simp
then obtain m’ where m = of-complex m’ is-real m’
using inf-or-of-complez[of m] «m € unit-disc»
unfolding circline-set-x-axis
by auto
hence Re m’ < Re x
using <poincare-between 0, m (of-complex x)» xx <of-complex x # On>
using False *« <of-complex x € unit-disc»
using cmod-Re-le-iff poincare-between-Ouv by auto

have n # 0n
using **(2, 4) <of-compler « # 0,» <of-complez x € unit-disc»
using poincare-between-sandwich by fastforce
have n € circline-set x-axis
using poincare-between-poincare-line-uvz|of On of-complex x n]
using poincare-line-0-real-is-x-axis|of of-complex x]
using <of-complex x € unit-disc) <of-complex x # con? <of-compler x # On>
using <of-complex x € circline-set z-axis» «n € unit-disc) **(2)
by simp
then obtain n’ where n = of-complez n’ is-real n’
using inf-or-of-complez{of n] «n € unit-disc»
unfolding circline-set-x-axis
by auto
hence Re x < Ren’
using <poincare-between 0), (of-compler x) n> xx <of-compler x # 01,»
using False ** <of-complex x € unit-discy «n # On?
using cmod-Re-le-iff poincare-between-Ouv
by (metis Re-complez-of-real arg-0-iff rcis-cmod-Arg rcis-zero-arg to-complex-of-complex)

have poincare-between (of-complex m'‘) (of-complex x) (of-complex n’)
using (Re x < Ren’ «Re m' < Re x
using poincare-between-z-azis-uvwlof Re m' Re x Re n’|
using <is-real n’) <is-real m') «n € unit-discy «n = of-complex n'y
using xz <m = of-complez m'> «m € unit-disc»
by (smt complex-of-real-Re norm-of-real poincare-between-def unit-disc-

thus ?thesis
using <n = of-complex n’> «m = of-complex m'y
by auto
qed
qed
qed
thus ?thesis
using assms
by blast
qed
