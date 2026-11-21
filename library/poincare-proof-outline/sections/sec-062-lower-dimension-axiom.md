---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-062-lower-dimension-axiom
section_title: "Lower dimension axiom"
section_number: null
pages: 143-143
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma lower-dimension-axiom:
shows J a € unit-disc. 4 b € unit-disc. J c € unit-disc.
7 poincare-between a b c A 7 poincare-between b c a A — poincare-between c a b
proof—
let ?u = of-compler (1/2) and ?v = of-complex (i/2)
have 1: 0; € unit-disc and 2: ?u € unit-disc and 3: ?v € unit-disc
by simp-all
have *: — poincare-collinear {On, ?u, ?v}
proof (rule ccontr)
assume — ?thesis
then obtain p where is-poincare-line p {0;, ?u, ?v} C circline-set p
unfolding poincare-collinear-def
by auto
moreover
have of-complex (1 / 2) 4 of-complex (i / 2)
using of-complez-inj
by fastforce
ultimately
have 0», € circline-set (poincare-line ?u ?v)
using unique-poincare-line[of ?u ?v p|
by auto
thus False
unfolding circline-set-def
by simp (transfer, transfer, simp add: vec-cnj-def)
qed
show ?thesis
apply (rule-tac c=0», in bel, rule-tac r= ?u in bezl, rule-tac x=?v in bez!)
apply (rule ccontr, auto)
using *
using poincare-between-poincare-collinear[OF 1 2 3}
using poincare-between-poincare-collinear[OF 2 8 1}
using poincare-between-poincare-collinear[OF 3 1 2}
by (metis insert-commute)+
qed
