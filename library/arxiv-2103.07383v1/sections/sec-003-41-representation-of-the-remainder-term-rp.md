---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-003-41-representation-of-the-remainder-term-rp
section_title: "Representation of the remainder term R(p)"
section_number: 4.1
pages: 9-10
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
---
In this subsection we are concerned with an alternative representation of the remainder term
R(p) and its derivatives. Let us ﬁrst recall the following result.
Lemma 4.1 (Regularity of the remainder integrand, [BR15, Lemma 4.4]).
Letγ∈W (3p−4)/2+σ,2(R/Z, Rn) be a simple curve parametrized by arc-length.
• If σ= 0, thengp∈L1(R/Z×D, Rn) and
• if σ >0, then ((v,w )↦→gp(·,v,w ;...))∈L1(D,W ˜σ,1(R/Z, Rn)) for any ˜σ <σ.
The respective norms are bounded independently ofs1,...,sK.
We then derive a representation of the remainder termR(p) corresponding to theL2-repre-
sentation of the main termQ(p) in the ﬁrst variation ofintM(p,2). Recall that⊗denotes any kind
of bilinear product structure, such as cross product, dot product, scalar or matrix multiplication.
Lemma 4.2. Letγ∈C∞(R/Z, Rn) be parametrized by arc-length and leth∈W
3
2p−2,2(R/Z, Rn).
Then,
R(p)(γ,h) =

R/Z
⟨
⟨R(p)(γ)(u),h (u)
⟩
du
with
⟨R(p)(γ)o(u) :=
kmax∑
k=1

D

···

[0,1]K
d
dugp
k(u−sK−1v−sKw,v,w ;s1,...,sK−2) dθ1···dθK dv dw⊗eo.
Here,eo∈Rn is theo-th canonical unit vector, eachgp
k is of the same form asgp in Lemma 2.1
and neitherK nor kmax depend onγ. Furthermore,u↦→gp
k(u,v,w ;s1,...,sK)∈C∞(R/Z, Rn)
for allk∈{1,...,k max}.
Proof. Sinceγ∈C∞(R/Z, Rn), Lemma 4.1 yields that the integrand is in fact integrable on the
integration domain, allowing us to substituteu by ˜u :=u +sK−1v +sKw. We also obtain that
u↦→gp(u,v,w ;s1,...,sK)∈C∞(R/Z, Rn) and note that⊗is a bilinear operation. Thus we
may use integration by parts component-wise to obtain that (5) is equal to

R/Z×D

···

[0,1]K
( d
d˜ugp(˜u−sK−1v−sKw,v,w ;s1,...,sK−2))⊗h(˜u) dθ1···dθK dv dw d˜u.
Note that we have no boundary terms because bothh andgp are periodic. Using the bilinearity
of⊗, we may write⟨R(p) as 
R/Z
R
(p)
(γ)(u)⊗h(u) du
9
with
R
(p)
(γ)(u) :=
kmax∑
k=1

D

···

[0,1]K
d
dugp
k(u−sK−1v−sKw,v,w ;s1,...,sK−2) dθ1···dθK dv dw.
Seeing asx↦→R
(p)
(γ)(u)⊗x∈R is linear, we may set
⟨R(p)(γ)o(u) :=R
(p)
(γ)(u)⊗eo
and obtain forx =∑n
o=1xoeo∈Rn:
R
(p)
(γ)(u)⊗x =
n∑
o=1
xo·R
(p)
(γ)(u)⊗eo =
n∑
o=1
xo·⟨R(p)(γ)o(u) =
⟨
⟨R(p)(γ)(u),x
⟩
.
The l-th derivative of the remainder representation⟨R(p) can be computed as follows.
Lemma 4.3. Letγ∈C∞(R/Z, Rn) be parametrized by arc-length. Then,
dl
dul
⟨R(p)(γ)o(u)
=
kmax∑
k=1

D

···

[0,1]K
dl+1
dul+1gp
k(u−sK−1v−sKw,v,w ;s1,...,sK−2) dθ1···dθK dv dw⊗eo
for alll∈N.
Note that we do not need the assumption of arc-length parametrization here, as⟨R(p) is well-
deﬁned without it. However, for other parametrizations, we do not expect⟨R(p)(γ) to be related
to R(p)(γ,·).
Proof. Since X ↦→X⊗eo is a ﬁxed linear map, dl
dul (X(u)⊗eo) = ( dl
dul∂lX(u))⊗eo, so
we only need to worry about the integral term. By Lemma 4.1,((v,w )↦→gp
k(·,v,w ;...))∈
L1(D,W ˜σ,1(R/Z, Rn)) for all ˜σ >0 and its norm is independent ofs1,...,sK. This means that
gp
k is diﬀerentiable with respect tou arbitrarily many times and the derivatives are all integrable
with the majorant
‖∂l+1
1 gp
k(·,v,w ;s1,...,sK)‖L∞.
By the Morrey- (see e.g. [AF03, Paragraph 4.16]) and Sobolev-embedding theorems, we can
bound this above by
C‖∂l+1
1 gp
k(·,v,w ;s1,...,sK)‖W 1,2≤⟨C‖gp
k(·,v,w ;s1,...,sK)‖W l+ 5
2 ,1.
As we have a uniformL1-bound on the latter, we may exchange integration and diﬀerentiation.
