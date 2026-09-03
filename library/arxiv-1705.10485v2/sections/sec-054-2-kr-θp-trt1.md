---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-054-2-kr-θp-trt1
section_title: "Kr (θP )tr−t1,"
section_number: 2
pages: 44-46
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
whereM =|X|.
The proof of this bound relies on arguments due to Diaconis, Stroock and Fill, see [DS91, Fil91]. We also
refer to [SS91, Section 4.1] for an alternate approach. Given an ergodic transition matrixP on X with
invariant measureπ, we denote~P the time reversal ofP, which is the stochastic matrix deﬁned by the
equation
~P (x,y ) = π(y)P (y,x )
π(x) .
This new transition matrix is again ergodic, with stationary measureπ. The multiplicative reversiblization
ofP is the matrixM(P ) =P~P. It is a stochastic matrix, which is ergodic with stationary measureπ, and
with all its eigenvalues that are real and belong to[0, 1]. Indeed, ifD is the diagonal matrixD = diag(π),
then ~P =D−1PtD, and
Mod-φ convergence, II: Estimates on the speed of convergence 45
Spec(M(P )) = Spec
(
D1/2P~PD−1/2
)
= Spec
(
(D1/2PD−1/2)(D−1/2PtD1/2)
)
= Spec
(
(D1/2PD−1/2)(D1/2PD−1/2)t
)
.
Thus, M(P ) has the spectrum of a symmetric positive matrix, so it belongs toR+, and in fact to[0, 1]
since M(P ) is also stochastic. We denote
(θP )2 = max{|z|| z eigenvalue ofM(P ), z⁄= 1}. (9)
Notice that ifP is reversible, then~P =P and M(P ) =P 2, so in this case
θP = max{|z|| z eigenvalue ofP, z⁄= 1}.
Ingeneral,onecanthinkof θP astheanalogueofthesecondlargesteigenvaluefornon-reversibletransition
matrices. The following result estimates the rate of convergence of the Markov chain associated toP in
terms ofθ:
Theorem 53 (Fill, 1991).For anyx∈ X,
∑
y∈X
|Pt(x,y )−π(y)|≤ (θP )t
√
π(x)
;
∑
y∈X
|Pt(x,y )−π(y)|√
π(y)
≤
√
M (θP )t
√
π(x)
whereM =|X|.
Proof. For completeness, we reproduce here the discussion of [Fil91, Section 2], which relies on the
following identity due to Mihail. Iff is a function onX, we denoteVar(f) its variance under the stationary
probability measureπ. We also introduce the Dirichlet form
E (f,g ) = 1
2
∑
x,y∈X
(f(x)−f(y))(g(x)−g(y))π(x)M(P )(x,y ).
Then, for any functionf,
Var(f) = Var(~Pf ) + E (f,f ).
Indeed, one can assume w.l.o.g. thatπ(f) =∑
x∈Xπ(x)f(x) = 0. If⟨f|g⟩π =∑
x∈Xπ(x)f(x)g(x), then
E (f,f ) =⟨f| (id−M(P ))f⟩π =⟨f|f⟩π−
⟨
f
⏐⏐⏐P~Pf
⟩
π
=⟨f|f⟩π−
⟨
~Pf
⏐⏐⏐ ~Pf
⟩
π
= Var(f)− Var(~Pf )
since ~P is the adjoint ofP for the action on the left of functions and with respect to the scalar product
⟨·|·⟩ π. Consider now a Markov chain(Xt)t∈N on X with arbitrary initial distributionπ0, and denote
πt =π0Pt the distribution at timet. We introduce the quantity
(χt)2 =
∑
y∈X
(πt(y)−π(y))2
π(y) .
This is the variance offt = πt
π with respect to the probability measureπ. By Mihail’s identity,
(χt+1)2 = Var(ft+1) = Var(~Pft) = Var(ft)− E (ft,ft) = (χt)2− E (ft,ft).
By the minimax characterization of eigenvalues of symmetric positive matrices,
46 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
(θP )2 = 1− inf
{ E (f,f )
Var(f), fnon-constant
}
.
Therefore, (χt+1)2≤ (θP )2 (χt)2, and (χt)2≤ (θP )2t (χ0)2 by induction ont. On the other hand, the
Cauchy-Schwarz inequality yields
∑
y∈X
|πt(y)−π(y)|≤
√∑
y∈X
π(y)
vuu√
∑
y∈X
(πt(y)−π(y))2
π(y) =χt.
If we chooseπ0 =δx, we ﬁnally obtain:
∑
y∈X
|Pt(x,y )−π(y)|≤ (θP )tχ0 = (θP )t
√
1
π(x)− 1≤ (θP )t
√
π(x)
.
Similarly,
∑
y∈X
|Pt(x,y )−π(y)|√
π(y)
≤
√
Mχ t≤
√
M (θP )tχ0≤
√
M (θP )t
√
π(x)
. ⊓ ⊔
Proof (Proposition 52).If f : X→ R, denoteDf = diag(f(x),x∈ X). Then, the Boolean cumulant has
the following matrix expression:
B(r)(Yt1,...,Y tr) =πDft1 (Pt2−t1−1π)··· Dftr−1
(Ptr−tr−1−1π)Dftr 1,
where 1 is the column vector with all its entries equal to1; see [Fér16, Lemma 10.1]. If we expand this
expression as a sum, and denoteQt =Pt−1π and δi =ti+1−ti, then
B(r)(Yt1,...,Y tr)
=
∑
x1,...,xr
π(x1)ft1(x1)Qt2−t1(x1,x 2)ft2(x2)··· Qtr−tr−1(xr−1,xr)ftr(xr)
and we obtain
|B(r)(Yt1,...,Y tr)|≤ Kr ∑
x1,...,xr
π(x1)|Qδ1(x1,x 2)|···| Qδr−1(xr−1,xr)|
≤Kr (θP )δr−1
∑
x1,...,xr−1
π(x1)|Qδ1(x1,x 2)|··· |Qδr−2(xr−2,xr−1)|√
π(xr−1)
...
≤KrM
r−2
