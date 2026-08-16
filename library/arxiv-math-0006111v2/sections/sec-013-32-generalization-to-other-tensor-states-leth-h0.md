---
doc_id: arxiv-math-0006111v2
doc_title: "APPROXIMA TE F ACTORIZA TION AND CONCENTRA TION FOR CHARACTERS OF SYMMETRIC GROUPS Philippe Biane"
section_id: sec-013-32-generalization-to-other-tensor-states-leth-h0
section_title: "Generalization to other tensor states. LetH =H0 ⊕H1, be a Z/ 2-graded"
section_number: 3.2
pages: 10-11
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "APPROXIMATE FACTORIZATION AND CONCENTRATION FOR CHARACTERS OF SYMMETRIC GROUPS Philippe Biane — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
Hilbert space with grading operator ∆. Endow B(H ⊗q) = B(H)⊗q with a tensor
stateτ⊗q whereτ is a state on B(H), of the form τ(X) = Tr (TX ), withT a positive
trace class operator, with trace 1, commuting with the gradi ng. Denote by t1, 0 ≥
t2, 0 ≥... ≥tk, 0 ≥... ≥ 0 and t1, 1 ≥t2, 1 ≥... ≥tk, 1 ≥... ≥ 0 the eigenvalues of
T onH0 andH1 respectively, and let pn =Tr (∆(∆ T )n) =∑ ∞
j=1tn
j, 0 − (−tj, 1)n for
n ≥ 1.
APPROXIMATE F ACTORIZATION AND CONCENTRATION 11
In this last section we shall consider the representation of Sq on H ⊗q, given by
(ii + 1)(v1 ⊗...v i ⊗vi+1... ⊗vq) = ( −1)ε(vi)ε(vi+1)v1 ⊗...v i+1 ⊗vi... ⊗vq
where vk are graded vectors, with graduation ε(vk) ∈ { 0, 1}. The positive deﬁnite
function on Sq determined by this representation and the state τ⊗q is given by
(3.2.1) τ⊗q(ρ) =
∏
c|ρ
p|c|+1
where the product is over the non trivial cycles c of ρ. Recall that for a cycle c
one has |c| + 1 = s(c). This is of course a direct generalization of Section 3.1 wh ere
we had t1, 0 =t2, 0 =... =tN, 0 = 1
N , the other eigenvalues being 0. We shall now
investigate the asymptotic decomposition of the associate d probability measure on
Young diagrams, under the hypothesis that τ := τq depends on q as q → ∞ , and
that the moments Tr (Tn
q ) satisfy
q(n−1)/ 2Tr (Tn
q ) →q→∞wn+1 n ≥ 1
for some sequence of real numbers wn, with |wn| ≤ Cn for some constant C > 0.
This last condition insures that the positive deﬁnite funct ions (3.2.1) belong to the
sets Fn
c, 0 as in Section 3.1. Using the same arguments as in the precedin g section,
we see that the measure on rescaled diagrams converges towar ds the Dirac mass
at the diagram with cumulants ( wn)n≥1, with w1 = 0, w2 = 1. These cumulants
have the form wn =
∫
R |t|tn−2µ (dt); n ≥ 2 for some positive measure µ on [ −C,C ],
satisfying
∫
R |t|µ (dt) = 1. The R-transform of the measure with cumulants wn is
thus
R(z) =
∞∑
n=1
wnzn−1 =
∫
R
z
1 −zt |t|µ (dt)
Comparing with the free L´ evy-Khintchine formula of [BV], we see that the measure
corresponding to the limit diagram is freely indeﬁnitely di visible, with correspond-
ing L´ evy measureν(dt) = 1
|t|µ (dt)
Remark. One can give an explicit expression for the weight of a given d iagram
λ ∈ Yq, under the measure associated with the function (3.2.1), in terms of the
Schur functions (see also [M] formula (7.8)). It would be interesting to rederive the
results of Sections 3.1 and 3.2 directly from this explicit e xpression.
