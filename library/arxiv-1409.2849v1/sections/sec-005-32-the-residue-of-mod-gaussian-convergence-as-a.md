---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-005-32-the-residue-of-mod-gaussian-convergence-as-a
section_title: "The residue of mod-Gaussian convergence as a limiting law"
section_number: 3.2
pages: 13-15
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
and prove the main result of this Section. We assume the hypotheses (A) and (B), and
keep the same notation as before.
Theorem 6. The following assertions are equivalent:
(i) The sequence ( Yn
tn )n∈N is tight.
(ii) The sequence ( Yn
tn )n∈N converges in law to a variable with density ψ(x)/
∫
R ψ(x) dx.
(iii) The convergence ψn→ ψ, which is supposed locally uniform on R, also occurs in L1(R).
We shall then say that (Xn)n∈N converges in the L1-mod-Gaussian sense with parameters t n
and limiting function ψ. In this setting, the residue ψ can be interpreted as the limiting law of
(Xn)n∈N after an appropriate change of measure.
Proof. Since the Gaussian variable Gn of variance 1
tn converges in probability to 0,
( Yn
tn )n∈N converges to a law µ if and only if (Wn)n∈N converges to the law µ. If (iii)
is satisﬁed, then by Proposition 5,
lim
n→∞
P[Wn≤ w] =
∫ w
−∞ ψ(x) dx∫ ∞
−∞ ψ(x) dx ,
so the cumulative distribution functions of the variablesWn converge to the cumulative
distribution function of the law ψ(x)/
∫
R ψ(x) dx, and (ii) is established. Obviously,
one also has (ii)⇒ (i). Finally, if (iii) is not satisﬁed, then by Scheffe’s lemma one also
has ∫
R
ψn(x) dx⁄→
∫
R
ψ(x) dx.
However, by Fatou’s lemma,
∫
R ψ(x) dx≤ lim infn→∞
∫
R ψn(x) dx. Therefore, the non-
convergence in L1 is only possible if
∫
R ψ(x) dx < lim supn→∞
∫
R ψn(x) dx. Thus, there
is an ε > 0 and a subsequence (nk)k∈N such that
∀k∈ N,
∫
R
ψnk (x) dx≥ ε +
∫
R
ψ(x) dx.
Then, for all a, b∈ R,
lim sup
k→∞
P[a≤ Wnk≤ b] = lim sup
k→∞
(∫ b
a ψnk (x) dx∫
R ψnk (x) dx
)
=
∫ b
a ψ(x) dx
lim infk→∞
∫
R ψnk (x) dx
≤
∫
R ψ(x) dx
ε +∫
R ψ(x) dx < 1
which amounts to saying that (Wn)n∈N (and therefore ( Yn
tn )n∈N) is not tight; hence, (i)
implies (iii). □
To complete this result, it is important to compare the two notions of complex mod-
Gaussian convergence and of integral L1-mod-Gaussian convergence. Though there
14 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
are no direct implication between these two assumptions, the following Proposition
shows that the latter notion is a stronger type of convergence:
Proposition 7. Let (Xn)n∈N be a sequence that converges in theL1-mod-Gaussian sense with
parameters tn→ ∞ and limiting function ψ∈ L1(R). The estimate of precise large deviations
(2) is then satisﬁed.
Proof. Recall than Zn = E[e(Xn)2/2tn] =
√
tn
2π
∫
R ψn(x) dx. We want to compute
P[Xn≥ tnx] =
∫ ∞
tnx
Pn[dy] = Zn
∫ ∞
tnx
e− y2
2tn Qn[dy] = Zn
∫ ∞
x
e− tn u2
2 P Yn
tn
[du].
Suppose for a moment that we can replace the law of Yn
tn by the one of Wn = Gn + Yn
tn in
the previous computation. Then, one obtains from Proposition 5
Zn
∫ ∞
x
e− tn u2
2 PWn[du] =
√
tn
2π
∫ ∞
x
e− tnu2
2 ψn(u) du.
Fix ε > 0. Since ψn converges locally uniformly to the continuous function ψ, there is
an interval [x, x + η] such that for n large enough and u∈ [x, x + η],
ψ(x)− ε < ψn(u) < ψ(x) + ε.
Therefore, for n large enough,
(ψ(x)− ε)
∫ x+η
x
e− tnu2
2 du≤
∫ x+η
x
e− tnu2
2 ψn(u) du≤ (ψ(x) + ε)
∫ x+η
x
e− tnu2
2 du
↓ ↓
(ψ(x)− ε) e− tnx2
2
tnx (ψ(x) + ε) e− tnx2
2
tnx .
Indeed, by integration by parts,
∫ x+η
x e− tn u2
2 du is asymptotic to e− tn x2
2
tn x . On the other
hand, since ψn→L1 ψ, for the remaining part of the integral,
∫ ∞
x+η
e− tnu2
2 ψn(u) du≤ e− tn(x+η)2
2
(∫ ∞
x+η
ψn(u) du
)
≃ e− tn(x+η)2
2
(∫ ∞
x+η
ψ(u) du
)
which is much smaller than the previous quantities. Therefore, assuming that one can
replace Yn
tn by Wn, we obtain the asymptotics
P[Xn≥ tnx] = e− tn x2
2
√2πtn x ψ(x) (1 + o(1))
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS15
for all x > 0; this is what we wanted to prove. Finally, the replacement Yn
tn ↔ Wn is
indeed valid, because
∫ ∞
x
e− tn u2
2 PWn[du] =
[
e− tn u2
2 P[Wn≤ u]
]∞
x
+
∫ ∞
x
tnu e− tn u2
2 P[Wn≤ u] du
≃
[
e− tn u2
2 P[Yn/tn≤ u]
]∞
x
+
∫ ∞
x
tnu e− tn u2
2 P[Yn/tn≤ u] du
≃
∫ ∞
x
e− tn u2
2 P Yn
tn
[du]
by using on the second line the fact that both Yn
tn and Wn converge in law to the same
limit, and therefore have equivalent cumulative distribution function on R+. □
In the same setting of L1-mod-Gaussian convergence, one has similarly the estimates
on the negative part of the real line, and around 0, as described on page 4 in the setting
of complex mod-Gaussian convergence.
