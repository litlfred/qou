---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-050-h-lines
section_title: "H-lines"
section_number: null
pages: 124-125
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
typedef p-line ={H. is-poincare-line H}
by (rule-tac x =x-axis in exI, simp)
setup-lifting type-deﬁnition-p-line
lift-deﬁnition p-incident :: p-line⇒ p-point⇒ bool is on-circline
done
Set of h-points on an h-line
deﬁnition p-points :: p-line⇒ p-point set where
p-points l ={p. p-incident l p}
124
x-axis is an example of an h-line
lift-deﬁnition p-x-axis :: p-line is x-axis
by simp
Constructing the unique h-line from two h-points
lift-deﬁnition p-line :: p-point⇒ p-point⇒ p-line is poincare-line
proof−
ﬁx u v
show is-poincare-line (poincare-line u v )
proof (cases u ⁄= v)
case True
thus ?thesis
by simp
next
This branch must work only for formal reasons.
case False
thus ?thesis
by (transfer, transfer, auto simp add : hermitean-def mat-adj-def mat-cnj-def split : if-split-asm)
qed
qed
Next we show how to lift some lemmas. This could be done for all the lemmas that we have proved earlier, but
we do not do that.
If points are diﬀerent then the constructed line contains the starting points
lemma p-on-line:
assumes z⁄= w
shows p-incident (p-line z w ) z
p-incident (p-line z w ) w
using assms
by (transfer, simp)+
There is a unique h-line passing trough the two diﬀerent given h-points
lemma
assumes u⁄= v
shows∃ ! l.{u, v}⊆ p-points l
using assms
apply (rule-tac a =p-line u v in ex1I, auto simp add : p-points-def p-on-line )
apply (transfer, simp add : unique-poincare-line)
done
The unique h-line trough zero and a non-zero h-point on the x-axis is the x-axis
lemma
assumes p-zero∈ p-points l u ∈ p-points l u ⁄= p-zero u ∈ p-points p-x-axis
shows l = p-x-axis
using assms
unfolding p-points-def
apply simp
apply transfer
using is-poincare-line-0-real-is-x-axis inf-notin-unit-disc
unfolding circline-set-def
by blast
