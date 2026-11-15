---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-047-position-of-the-intersection-point-in-the-unit-d
section_title: "Position of the intersection point in the unit disc"
section_number: null
pages: 110-112
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Check if the intersection point of one h-line with the x-axis is located more outward the edge of the disc than
the intersection point of another h-line.

definition outward-cmat :: compler-mat = complez-mat = bool where
[simp]: outward-cmat H1 H2 = (let (Al, B1, C1, D1) = H1; (A2, B2, C2, D2) = H2
in —Re B1/Re Al < —Re B2/Re A2)
lift-definition outward-clmat :: circline-mat = circline-mat = bool is outward-cmat
done
lift-definition outward :: circline => circline = bool is outward-clmat
apply transfer
apply simp
apply (case-tac circline-mat1, case-tac circline-mat2, case-tac circline-mat3, case-tac circline-mat4 )
apply simp
apply (erule-tac exE)+
apply (erule-tac conjE)+
apply simp
done

lemma outward-mk-circline:
assumes is-real Al and is-real A2 and Al 4 0 V B1 #4 0 and A240V B24 0
shows outward (mk-circline Al B1 (cnj B1) A1) (mk-circline A2 B2 (cnj B2) A2) ++ — Re B1 / Re Al < — Re
B2 / Re A2
proof—
let ?H1 = (A1, B1, (cnj B1), A1)
let ?H2 = (A2, B2, (cnj B2), A2)
have hermitean ?H1 hermitean ?H2
using <is-real Al) <is-real A2»
unfolding hermitean-def mat-adj-def mat-cnj-def
using eq-cnj-iff-real
by auto
moreover
have ?H1 # mat-zero ?H2 # mat-zero
using assms
by auto
ultimately
show ?thesis
by (transfer, transfer, auto simp add: Let-def)
qed

lemma calc-z-axis-intersection-fun-mono:
fixes x1 x2 :: real
assumes z/ > / and 22 > «1
shows x1 — sqrt(z1? — 1) > x2 — sqrt(x2? — 1)
using assms
proof—
have #: sqrt(x1? — 1) + sgrt(z2? — 1) > 0
using assms
by (smt one-less-power pos2 real-sqrt-gt-zero)

have sqrt(x1* — 1) < al
using real-sqrt-less-iff[of 22? — 1 x17] «41 > 1»
by auto
moreover
have sqrt(x2 — 1) < «2
using real-sqrt-less-iff[of 12? — 1 127] «41 > 1) (22 > xl»
by auto
ultimately
have sqrt(z1? — 1) + sqrt(a2? — 1) < a1 + «2
by simp
hence (11 + 12) / (sqrt(x1? — 1) + sqrt(x2* — 1)) > 1
using *
using less-divide-eq-1-pos[of sqrt(x1? — 1) + sqrt(a2? — 1) «1 + 22]
by simp
hence (22? — x17) / (sqrt(a1? — 1) + sqrt(x2? — 1)) > «2 — al
using (22 > a1)

110
using mult-less-cancel-left-pos[of x2 — a1 1 («2 + a1) / (sgrt(a1? — 1) + sqrt(x2? — 1))|
by (simp add: power2-eq-square field-simps)

moreover

have (x2? — x1”) = (sqrt(x1? — 1) + sgrt(a2? — 1)) * ((sqrt(a2? — 1) — sqrt(x1? — 1)))
using (rl > 1) «2 > al»
by (simp add: field-simps)

ultimately

have sqrt(x2? — 1) — sqrt(x1? — 1) > 22 — xl
using *
by simp

thus ?thesis
by simp

qed

lemma calc-2z-axis-intersection-mono:
fixes al b1 a2 b2 :: real
assumes —b1/al > 1 and al # 0 and —b2/a2 > —b1/al and a2 4 0
shows (—b1 + sgn b1 * sqrt(b1? — al?)) / al > (—b2 + sgn b2 * sqrt(b2? — a2?)) / a2 (is ?lhs > ?rhs)
proof—
have ?lhs = —b1/a1 — sqrt((—b1/al)? — 1)
proof (cases b1 > 0)
case True
hence al < 0
using assms
by (smt divide-neg-pos)
thus ?thesis
using <(b1 > 0) «al < 0»
by (simp add: real-sqrt-divide field-simps)
next
case False
hence bi < 0
using assms
by (cases b1 = 0) auto
hence al > 0
using assms
by (smt divide-pos-neg)
thus ?thesis
using (bl < 0) ‘al > 0»
by (simp add: real-sqrt-divide field-simps)
qed

moreover

have ?rhs = —b2/a2 — sqrt((—b2/a2)? — 1)
proof (cases b2 > 0)
case True
hence a2 < 0
using assms
by (smt divide-neg-pos)
thus ?thesis
using (b2 > 0) «a2 < 0»
by (simp add: real-sqrt-divide field-simps)
next
case False
hence b2 < 0
using assms
by (cases b2 = 0) auto
hence a2 > 0
using assms
by (smt divide-pos-neg)
thus ?thesis
using <(b2 < 0) «a2 > 0»
by (simp add: real-sqrt-divide field-simps)
qed

ultimately

111
show ?thesis
using calc-x-axis-intersection-fun-mono|[of —b1/al —b2/a2]
using assms
by (cases —b1/a1=—b2/a2, auto)
qed

lemma outward:
assumes is-poincare-line H1 and is-poincare-line H2
assumes intersects-z-axis-positive H1 and intersects-x-axis-positive H2
assumes outward H1 H2
shows Re (to-complex (calc-1-axis-intersection H1)) > Re (to-complex (calc-x-axis-intersection H2))
proof—
have intersects-z-azis H1 intersects-x-axis H2
using assms
by auto
thus ?thesis
using assms
proof (transfer, transfer)
fix Hi H2
assume hh: hermitean H1 \ H1 ¢ mat-zero hermitean H2 \ H2 4 mat-zero
obtain Ail B1 C1 D1 A2 B2 C2 D2 where *: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
have is-real A1 is-real A2
using hermitean-elems * hh
by auto
assume 1: intersects-x-axis-positive-cmat H1 intersects-x-axis-positive-cmat H2
assume ntersects-x-axis-cmat H1 intersects-x-axis-cmat H2
assume 3: is-poincare-line-cmat H1 is-poincare-line-cmat H2
assume 4: outward-cmat H1 H2
have Al 4 0 A240
using * <is-real A1» <is-real A2> 1 complex.expand|[of A1 0] complex.expand[of A2 0]
by auto
hence (sgn (Re B2) * sqrt ((Re B2)? — (Re A2)?) — Re B2) / Re A2
< (sgn (Re B1) * sqrt ((Re B1)? — (Re A1)”) — Re B1) / Re Al
using calc-x-axis-intersection-mono|of Re B1 Re Al Re B2 Re A2]
using 1 4 *
by simp
moreover
have (sgn (Re B2) * sqrt ((Re B2)? — (Re A2)*) — Re B2) / Re A2 =
Re ((cor (sgn (Re B2)) * cor (sqrt ((Re B2)* — (Re A2)*)) — cor (Re B2)) / A2)
using <is-real A2) (A2 # 0»
by (simp add: Re-divide-real)
moreover
have (sgn (Re B1) * sqrt ((Re B1)? — (Re A1)?) — Re B1) / Re Al =
Re ((cor (sgn (Re B1)) * cor (sqrt ((Re B1)? — (Re A1)”)) — cor (Re B1)) / Al)
using <is-real Al) (Al # 0)
by (simp add: Re-divide-real)
ultimately
show Re (to-complez-cvec (calc-x-axis-intersection-cmat-cvec H2))
< Re (to-complex-cvec (calc-x-axis-intersection-cmat-cvec H1))
using 23 (Al # 0) (A2 F O> & <is-real Al» <is-real A2>
by (simp del: is-poincare-line-cmat-def intersects-z-axis-cmat-def)
qed
qed
