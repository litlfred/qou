---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-059-lower-dimension-axiom
section_title: "Lower dimension axiom"
section_number: null
pages: 143-143
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma lower-dimension-axiom:
shows∃ a∈ unit-disc.∃ b∈ unit-disc.∃ c∈ unit-disc.
¬ poincare-between a b c ∧¬ poincare-between b c a ∧¬ poincare-between c a b
proof−
let ?u = of-complex (1/2 ) and ?v = of-complex (i/2 )
have 1 : 0 h∈ unit-disc and 2 : ?u∈ unit-disc and 3 : ?v∈ unit-disc
by simp-all
have∗:¬ poincare-collinear{0 h, ?u, ?v}
proof (rule ccontr )
assume¬ ?thesis
then obtain p where is-poincare-line p{0 h, ?u, ?v}⊆ circline-set p
unfolding poincare-collinear-def
by auto
moreover
have of-complex (1 / 2 )⁄= of-complex (i / 2 )
using of-complex-inj
by fastforce
ultimately
have 0 h∈ circline-set (poincare-line ?u ?v )
using unique-poincare-line[of ?u ?v p ]
by auto
thus False
unfolding circline-set-def
by simp (transfer, transfer, simp add : vec-cnj-def )
qed
show ?thesis
apply (rule-tac x =0 h in bexI, rule-tac x =?u in bexI, rule-tac x =?v in bexI)
apply (rule ccontr, auto)
using∗
using poincare-between-poincare-collinear[OF 1 2 3 ]
using poincare-between-poincare-collinear[OF 2 3 1 ]
using poincare-between-poincare-collinear[OF 3 1 2 ]
by (metis insert-commute )+
qed
