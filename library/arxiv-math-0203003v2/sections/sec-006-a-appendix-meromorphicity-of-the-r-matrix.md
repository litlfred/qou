---
doc_id: arxiv-math-0203003v2
doc_title: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002"
section_id: sec-006-a-appendix-meromorphicity-of-the-r-matrix
section_title: "Appendix : Meromorphicity of the R-matrix"
section_number: A
pages: 11-13
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
toc_source: inferred
doc_brief: "arXiv:math/0203003v2 [math.QA] 24 Apr 2002 — 8 sections: Front matter; Introduction; Representations of Quantum Dynamic"
---
Appendix : Meromorphicity of the R-matrix
In this appendix we give a new proof of Theorem 2.1.
Let U be a neighborhood of zero in Cn, and G : U →Cn be an analytic mapping, such that
G(0) = 0. Let p ∈C, |p| > 1.
Lemma A.1. Let f ∈zCn[[z]] be a formal solution to the diﬀerence equation
f(pz) = G(f(z))
Then f converges to an analytic function in some neighborhood of zero.
Proof. Let f(z) = P
n≥1 fnzn, and G(y) = P
n≥1 gnyn, where gn are multilinear operators. Since
G is analytic at zero, there exists A > 0 such that the norms of the coeﬃcients are estimated by
|gn| < An for all n.
Let k0 be so big that for k ≥k0 one has|(pk −g1)−1| < 2|p|−k, and 2A < |p|k/2. Let C be such
that |fk| < C for k < k0, and let B > max(1,
AC
|p|1/2−1).
Let us prove by induction in k that |fk| < CBk−1. The statement is clear for k < k0 (as B > 1).
Assume that the statement is known for all n < k, for some k ≥k0, and prove it for k. We have
fk = (pk −g1)−1 X
1<r≤k
X
i1,...,ir:P ij=k
gr(fi1, ..., fir)
Now, |gr(fi1, ..., fir)| ≤|gr| Qr
l=1 |fil| < (AC)rBk−r, and the number of terms with gr is dominated
by the binomial coeﬃcient
k −1
r −1

(as ij ≥1, r > 1). Thus, we have
|fk| < 2(AC/B)(1 + AC/B)k−1|p|−kBk < CBk−1,
since 2A < |p|k/2 and 1 + AC/B < |p|1/2. The inductive step is proved.
This implies that f(z) converges for small z. We are done.
Now we proceed with the proof of Theorem 2.1. Recall the crossing symmetry condition (equa-
tion (9.19) of [EFK98])
(((RV,W (z)−1)t1)−1)t1) = (q2ρ ⊗1)RV,W (zq2mh∨)(q−2ρ ⊗1)
(A.1)
where t1 is transposition in the ﬁrst component and ρ is the half-sum of positive roots of g. It is
valid for any ﬁnite dimensional representations. If |q|̸ = 1, it can be regarded as an equation of the
type f(pz) = G(f(z)) considered above. Namely, f takes values in the space of endomorphisms
of V ⊗W, p = q±2mh∨, G(X) = (((X−1)t1)−1)t1, and the origin in End(V ⊗W) is at the point
X = RV,W(0), which is a ﬁxed point of G. Thus, by Lemma A.1, the function RV,W (z) is analytic
near zero. Then the meromorphicity in the whole complex plane follows immediately from the
diﬀerence equation (A.1) and the fact that in our case G is a birational isomorphism.
□
Remark: It is clear that the same result and proof applies to V, W being in category O as Uq(g)
modules (since the R-matrix has zero weight, and the weight spaces of V ⊗W are ﬁnite dimensional).
References
[ABRR98] Arnaudon, D.-Buﬀenoir, E.-Ragoucy, E.-Roche, Ph. Universal solutions of quantum
dynamical Yang-Baxter equations. Lett. Math. Phys., 44:201–214, 1998. q-alg/9712037.
[BBB95] Babelon, O.; Bernard, D.; Billey, E. A quasi-Hopf algebra interpretation of quantum 3-j
and 6-j symbols and diﬀerence equations. Phys. Lett. B 375 (1996), 89–97, q-alg/9511019.
[Ca01] A.Cavalli, Ph.D. thesis, ETH, Zurich, 2001.
[EFK98] Etingof, P.-Frenkel, I.-Kirillov Jr., A. Lectures on representation theory and Knizhnik-
Zamolodchikov equations, volume 58 of Mathematical Surveys and Monographs. AMS, 1998.
[ES98] Etingof, P.-Schiﬀmann, O.
On highest weight modules over elliptic quantum groups.
preprint. QA/9809161.
[ES99] Etingof, P.-Schiﬀmann, O. Lectures on the dynamical Yang-Baxter equations. preprint,
1999. QA/9908064.
[EV98] Etingof, P.-Varchenko, A. Solutions of the quantum dynamical Yang-Baxter equation and
dynamical quantum groups. Comm. Math. Phys, 196:591–640, 1998.
[EV99] Etingof, P.-Varchenko, A.
Exchange dynamical quantum groups.
Comm. Math. Phys,
205:19–52, 1999.
[EV00] Etingof, P.-Varchenko, A. Traces of intertwiners for quantum groups and diﬀerence equa-
tions, I. Duke Math. J., 104 (3):391–432, 2000.
[Fe94a] Felder, G. Conformal ﬁeld theory and integrable systems associated to elliptic curves. Proc.
of the ICM, Z urich, 1994. hep-th 9407154.
[Fe94b] Felder, G. Elliptic quantum groups. Proc. of the ICMP, Paris, 1994. hep-th 9412207.
[FeV96] Felder, G.-Varchenko, A.
On representations of the elliptic quantum group eτ,γ(sl2).
preprint. q-alg/9601003.
[Fra02] Frappat, L. Quantum elliptic algebras and double Yangians. preprint. QA/0201245.
[FR92] Frenkel, I.-Reshetikhin, N. Quantum aﬃne algebras and holonomic diﬀerence equations.
Comm. Math. Phys., 146:1–60, 1992.
[JKOS99] Jimbo, M.A.-Konno, H.-Odake, S.-Shiraishi, J. Quasi-Hopf twistors for elliptic quantum
groups. Transformation Groups, 4:303–327, 1999. q-alg/9712029.
[KL93a] Kazhdan, D.-Lusztig, G. Tensor structures arising from aﬃne Lie algebras I. J. Amer.
Math. Soc., 6:905–947, 1993.
[KL93b] Kazhdan, D.-Lusztig, G. Tensor structures arising from aﬃne Lie algebras II. J. Amer.
Math. Soc., 6:949–1011, 1993.
[KL94a] Kazhdan, D.-Lusztig, G. Tensor structures arising from aﬃne Lie algebras III. J. Amer.
Math. Soc., 7:335–381, 1994.
[KL94b] Kazhdan, D.-Lusztig, G. Tensor structures arising from aﬃne Lie algebras IV. J. Amer.
Math. Soc., 7:383–453, 1993.
[KS95] Kazhdan, D. Soibelman, Y. Representations of quantum aﬃne algebras. Selecta Math.
(N.S.), 1 (3):537–595, 1995.
[M01] Moura, A.
Elliptic dynamical R-matrices from the monodromy of the q-Knizhnik-
Zamolodchikov equations for the standard representation of Uq(˜sln+1). preprint. rt/0112145.
[TV97] Tarasov, V.-Varchenko, A. Geometry of q-hypergeometric functions, quantum aﬃne alge-
bras and elliptic quantum groups. Ast´erisque, 246, 1997. q-alg/9703044.
[TV01] Tarasov, V.-Varchenko, A. Small elliptic quantum group eτ,γ(sln). Moscow Math. J., 1 (2),
2001. QA/0011145.
