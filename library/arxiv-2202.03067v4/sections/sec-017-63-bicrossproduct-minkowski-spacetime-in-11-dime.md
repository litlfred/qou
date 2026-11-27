---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-017-63-bicrossproduct-minkowski-spacetime-in-11-dime
section_title: "Bicrossproduct Minkowski spacetime in 1+1 dimensions with its 2D calculus"
section_number: 6.3
pages: 34-37
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
Another example of interest [3, 4] is the 1+1 bicrossproduct model quantum spacetime [r,t]=λr
with its 2D calculus
[r,t]=λr, [r,dt]=λdr, [t, dt]=λdt, [r,dr]= [t, dr]= 0,
(dr)2 = 0, dr∧v+v∧dr = 0, v 2 =λv∧dr,
QUANTUM JET BUNDLES 35
where dr and v = rdt−tdr form a central basis. Here d t, dr obey the usual exterior algebra
relations, resulting in the relations stated in terms of the central basis. The calculus is inner
withθ =−1
λr(v+tdr) and one can check that the proposed form of bimodule connection in [3, 4]
∇dr = 1
r (αv⊗v+βv⊗dr+γdr⊗v+δdr⊗dr),
∇v = 1
r (α′v⊗v+β′v⊗dr+γ′dr⊗v+δ′dr⊗dr),
σ(dr⊗dr) = dr⊗dr, σ (v⊗dr) = dr⊗v,
σ(dr⊗v) =λαv⊗v+(1+λβ)v⊗dr+λγdr⊗v+λδdr⊗dr,
σ(v⊗v) = (1+λα′)v⊗v+λβ′v⊗dr+λγ′dr⊗v+λδ′dr⊗dr
with C-number coeﬃcients is indeed inner. Hence ∇is Leibniz-compatible by Proposition 6.1.
This ansatz is motivated from geometry and suﬃcient to includes a QLC (which is then unique
if we ask for a classical limit)[3], but here we look more broadly within the same ansatz.
Lemma 6.3. σ of the general form of the stated ansatz has four cases where it obeys the braid
relations and where the parameters have a classical limit:
(i)∶α=γ = 0, α ′= βγ′
δ , β ′= βδ′
δ , γ ′=δ+βδ′
δ ; δ ≠0,β,δ ′∈C
(ii)∶α=δ =α′=δ′= 0, β =−γ, γ ′=−β′; γ,β ′∈C
(iii)∶α=β =γ =δ = 0, α ′= β′2
δ′, γ ′=β′; δ′≠0,β′∈C
(iv)∶α=γ =δ =β′=γ′=δ′= 0; β,α′∈C
Proof. This is a matter of writing out the YBE for σ on the basis dr,v . One of the equations
is α2(1+λ(α′+β)) = 0 which requires α = 0 or α′+β =−1/slash.leftλ and we exclude the latter case as
having no limit as λ→0. We then set α= 0 and analyse the simpliﬁed equations that result. □
Torsion-freeness and ﬂatness/extendability (these turn out to be the same for this form of
connection) have already been analysed in [6, 4], so all that remains is to intersect these with
the braid relations and check for ∧-compatibility.
Proposition 6.4. For the bicrossproduct Minkowski spacetime with its 2D calculus and within
the stated ansatz, bimodule connections with a classical limit which are torsion free and obey the
braid relations are given by:
(i) α=β =γ =α′=β′= 0, δ =γ′= 2, i.e.
σ(dr⊗v) =v⊗dr+ 2λdr⊗dr, σ (v⊗v) =v⊗v+ 2λdr⊗(v+δ′dr), δ ′∈C
(ii) α=β =γ =δ =α′=δ′= 0, −β′=γ′= 1, i.e.
σ(dr⊗v) =v⊗dr, σ (v⊗v) =v⊗(v−λdr)+λdr⊗v.
These are all extendable, ∧-compatible and Leibniz-compatible, so all the conditions of Theo-
rem 4.8 apply.
Proof. The moduli of torsion free connections of the general form of our ansatz is given [4] by
λα+β =γ, λα ′+β′+ 2=γ′.
The intersection of this with the braid relations in Lemma 6.3 leads to the cases (i) and (ii)
stated. We will show that the extendability and ∧-compatibility hold for both, so they both
meet all the conditions of Theorem 4.8.
36 SHAHN MAJID AND FRANCISCO SIM ˜AO
First, it was shown in [6] that the ﬂat/extendable ones within our ansatz are given by four
equations which, under the assumption of a classical limit, results in 3 cases
(a)∶α=β =α′=β′= 0, γ,γ ′,δ,δ ′∈C
(b)∶α=β =γ =α′= 0, γ ′= 1+δ, β ′≠0,δ,δ ′∈C
(c)∶α′=−β, β ′=−β2
α , γ ′=δ−1−2βγ
α , δ ′=−β(α+βγ)
α2 , α ≠0,β,γ,δ ∈C
(where the analysis in [6] missed case (b) here). From this, we see that both our solutions are
extendable without further restriction.
For∧-compatibility, in all cases, from the general form of our ansatz, the ﬂip form ofσ(( )⊗dr)
on the basis means that if we deﬁne σΩ2,Ω1 as required then
σΩ2,Ω1(dr∧dr⊗dr) =∧2(σ(dr⊗( ))⊗id)(dr⊗dr) = dr⊗dr∧dr = 0,
σΩ2,Ω1(v∧(v−λdr)⊗dr) =∧2(σ(v⊗( ))⊗id)(dr⊗(v−λdr)) = dr⊗v∧(v−λdr) = 0,
σΩ2,Ω1((v∧dr+ dr∧v)⊗dr) =∧2(σ(v⊗( ))⊗id)(dr⊗dr)+∧2(σ(dr⊗( ))⊗id)(dr⊗v)
= dr⊗(v∧dr+ dr∧v) = 0
so this part is automatic and we only have to check σΩ2,Ω1(( )⊗v).
Next, both our solutions are such that σ(dr⊗X) has the form X′⊗dr for any linear combi-
nation X and some linear combination X′of our generators. Hence in both cases
σΩ2,Ω1(dr∧dr⊗v) =∧2σ(dr⊗( ))⊗id)(X⊗dr) =σ(dr⊗X′)∧dr = 0
as dr∧dr = 0. So both our solutions are compatible with this relation.
Next, for the ﬁrst solution (i), we have
σ((v−λdr)⊗v) =v⊗(v−λdr)+ 2λdr⊗(v+(δ′−λ)dr),
σΩ2,Ω1(v∧(v−λdr)⊗v) =∧2(σ(v⊗( ))⊗id)(v⊗(v−λdr)+ 2λdr⊗(v+(δ′−λ)dr))
=σ(v⊗v)∧(v−λdr)+ 2λdr⊗v∧(v+(δ′−λ)dr)
= (v⊗v+ 2λdr⊗(v+δ′dr))∧(v−λdr)+ 2λδ′dr⊗v∧dr
= 2λδ′dr⊗(dr∧v+v∧dr) = 0
using the relations in the exterior algebra. Similarly
σΩ2,Ω1((v∧dr+ dr∧v)⊗v) =∧2(σ(v⊗( ))⊗id)(v⊗dr+ 2λdr⊗dr)
+∧2(σ(dr⊗( ))⊗id)(v⊗v+ 2λdr⊗(v+δ′dr))
= (v⊗v+ 2λdr⊗(v+δ′dr))∧dr+ 2λdr⊗v∧dr
+(v+ 2λdr)⊗dr∧v+ 2λdr⊗dr∧(v+δ′dr)
= (v+ 4λdr)⊗(v∧dr+ dr∧v) = 0
so this solution is ∧-compatible. For the solution (ii), we have more simply
σ((v−λdr)⊗v) =v⊗(v−2λdr)+λdr⊗v,
σΩ2,Ω1(v∧(v−λdr)⊗v) =∧2(σ(v⊗( ))⊗id)(v⊗(v−2λdr)+λdr⊗v)
=σ(v⊗v)∧(v−2λdr)+λdr⊗v∧v
=v⊗(v−λdr)∧(v−2λdr)+λdr⊗v∧(v−2λdr)+λdr⊗v2
=−v⊗(v∧dr+ dr∧v)+ 2λdr⊗v∧(v−λdr) = 0
using the relations in the exterior algebra. Similarly
σΩ2,Ω1((v∧dr+ dr∧v)⊗v) =∧2(σ(v⊗( ))⊗id)(v⊗dr)+∧2(σ(dr⊗( ))⊗id)(v⊗(v−λdr)+λdr⊗v)
QUANTUM JET BUNDLES 37
=σ(v⊗v)∧dr+v⊗dr∧(v−λdr)+λdr⊗dr∧v
=v⊗v∧dr+λdr⊗v∧dr+v⊗dr∧v+λdr⊗dr∧v = 0
so this solution is also ∧-compatible. □
The solution (ii) is involutive, σ2 = id, hence not strictly braided, while the 1-parameter
solution (i) is not involutive and hence is strictly braided whenλ≠0. In both cases the eigenvalues
are±1. More typical solutions in Lemma 6.3 are strictly braided with eigenvalue that depend on
some of the parameters. These could be of interest in other contexts.
For the jet bimodule, we focus on the 1-parameter solution (i). We have
J∞
A = spanA/uni27E81, dr,v, dr⊗dr,v ⊗(v−λdr),v ⊗dr+ dr⊗v,/uni22EF/uni27E9
where the dots denote higher order, and
j∞(a) =a+(∂ra)dr+(∂va)v+∇da+/uni22EF,
∇da= /parenleft.alt4∂2
ra+(∂ra) 2
r +(∂va)δ′
r /parenright.alt4dr⊗dr+(∂2
va)v⊗(v−λdr)+(∂v∂ra+λ∂2
va)(v⊗dr+ dr⊗v)
where provided a(r,t) is normal ordered with t to the right,
∂ra= ∂a
∂r +(∂λa)r−1t, ∂ va= (∂λa)r−1; ∂λa(r,t) = a(r,t)−a(r,t −λ)
λ
and ∂/slash.left∂r is the usual partial derivative leaving t constant. This is obtained by standard formu-
lae [4] for da in the dr,dt basis and re-expressing dt in terms of dr,v . One can check that
∂r∂va+(∂va) 2
r =∂v∂ra+λ∂2
va
as needed for the formula for j∞ to collect as shown. The ●k actions are then determined by the
latter.
In terms of Sσ(Ω1), one can compute in degree 2 and for generic λ,δ′that
ker(id+σ) = spanA/uni27E8v⊗dr−dr⊗v+λdr⊗dr/uni27E9
from which it follows that the braided symmetric algebra Sσ(Ω1) is spanned over A by the
algebra Sσ(C2) generated by dr,v with at least the quadratic relations [dr,v]=λ(dr)2. (These
are expected to be all the relations). The image in degree 2 is 3-dimensional over the algebra
in agreement with JA in degree 2. Thus, this is another example where, for generic parameter
values, the braided symmetric algebra and the jet bimodule essentially coincide and one could
build the jet bundle theory directly on the former for each degree k, but with ●k.
