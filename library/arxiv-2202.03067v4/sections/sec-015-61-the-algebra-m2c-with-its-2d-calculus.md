---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-015-61-the-algebra-m2c-with-its-2d-calculus
section_title: "The algebra M2(C) with its 2D calculus."
section_number: 6.1
pages: 31-33
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
connections since there is an obvious connection that turns out to meet all our criteria, namely
the standard QLC for the quantum metric g = s⊗t−t⊗s [4]. One could also analyse the full
moduli of allowed ∇by similar methods.
The standard 2-dimensional Ω 1 for this algebra has a central basis s,t while the exterior
algebra is unusual as it obey s∧t=t∧s (it is commutative!) along with s2 =t2 = 0 and
ds= 2θ∧s, dt= 2θ∧t, θ =E12s+E21t, θ 2 =s∧t, dθ = 2s∧t.
Here Eij is the elementary matrix with 1 at place (i,j) and zero elsewhere and θ makes the
calculus inner. Then
∇s= 2θ⊗s, ∇t= 2θ⊗t, R ∇=T∇= 0
is the standard connection. It corresponds to α = 0 and σ =−ﬂip on the generators and is part
of a larger moduli of QLCs for this metric in [4, Ex 8.13].
For our extra conditions, since the basis is central, it is enough to check everything on the
generators. In this case, as σ is just the −ﬂip map it is obvious that σΩ2 is just the ﬂip map, so
any relations among the basic 1-forms are respected and hence the connection is ∧-compatible.
Likewise for extendability on the other side. It is also obvious that σ obeys the braid relations
and hence the Leibniz-compatibility necessarily holds by Proposition 6.1 but is also easy to check
(eg on s⊗t, both side of Fig. 1(e) are −2θ⊗t⊗s.) So all conditions for Theorem 4.8 are met.
For the jet bimodule, we ﬁnd after some computation that
J∞
A = spanM2(C)/uni27E81,s,t,s ⊗s,t⊗t,g, /uni22EF/uni27E9,
where g = s⊗t−t⊗s was the metric we began with (this is quantum symmetric in the sense
∧(g) = 0, so lives in Ω 2
S) and the dots denote higher degrees. The map j∞ can be computed as
j∞(a) =a+(∂sa)s+(∂ta)t−{E21,∂sa}g
32 SHAHN MAJID AND FRANCISCO SIM ˜AO
for alla∈M2(C), from which we see that there is nothing in higher degrees. Here ∂sa= [E12,a],
∂ta = [E21,a] are commutators while the curly brackets denote anticommutator. The last term
is ∇da and can also be written as +{E12,∂ta}g. Moreover, ∇2∇da = 0 in part because the
connection is a QLC so ∇2g = 0. The bullet bimodule actions on lower degree for J∞
A (or any
k > 4) come out explicitly as
a●b=j∞(a)b, b ●a=bj∞(a),
a●s=as−(∂ta)g, s ●a=sa+(∂ta)g,
a●t=at+(∂sa)g, t ●a=ta−(∂sa)g,
a●(s⊗s) = (s⊗s)●a=a(s⊗s)+(∂sa)s⊗s⊗s+(∂ta)(s⊗s⊗t−g⊗s)−{E21,∂sa}g,
a●(t⊗t) = (t⊗t)●a=a(t⊗t)+(∂ta)t⊗t⊗t+(∂sa)(t⊗t⊗s−t⊗g)−{E21,∂sa}g,
a●g =g●a=ag.
For the algebra of quantum symmetric forms Ω S itself, the lower degree products are
s⊙s=t⊙t= 0, s ⊙t=−t⊙s=g,
s⊙(s⊗s) = (s⊗s)⊙s=s⊗s⊗s, t ⊙(t⊗t) = (t⊗t)⊙t=t⊗t⊗t,
t⊙(s⊗s) = (s⊗s)⊙t=s⊗g+t⊗s⊗s=s⊗s⊗t−g⊗s,
s⊙(t⊗t) = (t⊗t)⊙s=g⊗t+t⊗t⊗s=s⊗t⊗t−t⊗g,
s⊙g =g⊙s=t⊙g =g⊙s= 0,
(s⊗s)⊙(s⊗s) = 2s⊗s⊗s⊗s, (t⊗t)⊙(t⊗t) = 2t⊗t⊗t⊗t,
(s⊗s)⊙(t⊗t) = (t⊗t)⊙(s⊗s) =s⊗s⊗t⊗t+t⊗t⊗s⊗s−g⊗g,
g⊙(s⊗s) = (s⊗s)⊙g =s⊗s⊗g+g⊗s⊗s,
g⊙(t⊗t) =g⊙(t⊗t) =t⊗t⊗g+g⊗t⊗t,
g⊙g = 0.
Finally, the braided-symmetric algebra Sσ(Ω1) in Section 4.3 is much smaller and can be
identiﬁed as generated overM2(C) by the Grassmann algebra ins,t (i.e. these now anti-commute
with each other, and commute with elements of M2(C)). Here [2,σ](s⊗t) =g so that the image
ofjk lies in the corresponding subalgebra of ΩS for all k. Hence we have a reduced jet bimodule
Jk
σ for each k, albeit zero for degree 3 and above, and hence
J∞
σ = spanM2(C)/uni27E81,s,t,g /uni27E9/uni228AJ∞
A, j ∞
σ =
2
/summation.disp
i=0
di,
d0(a) =a, d 1(a) = (∂sa)s+(∂ta)t, d 2(a) =−{E21,∂sa}st
with the bullet bimodule structure
a●b=j∞
σ (a)b, b ●a=bj∞
σ (a),
a●s=as−(∂ta)st, s ●a=sa+(∂ta)st,
a●t=at+(∂sa)st, t ●a=ta−(∂sa)st,
a●(st) = (st)●a=ast.
This is much as before but on our subalgebra.
QUANTUM JET BUNDLES 33
