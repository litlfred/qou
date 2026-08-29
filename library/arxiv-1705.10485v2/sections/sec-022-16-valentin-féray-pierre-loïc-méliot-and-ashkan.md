---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-022-16-valentin-féray-pierre-loïc-méliot-and-ashkan
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 16
pages: 16-17
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
dKol(X,Y )≤ 3
2(B + 7m)ε,
which is easy to remember and manipulate.
Proof. For the convenience of the reader, we reproduce here the proof given in [MN15]. Fix a positive
constant K, and denote∆ = supa∈R|FX(a)−FY (a)| the Kolmogorov distance betweenX and Y. One
has
FX(a) = E[1X≤a]≤ E[fa+Kε,ε(X)] + E[(1−fa+Kε,ε(X)) 1X≤a]
≤ E[fa+Kε,ε(Y )] + E[(1−fa+Kε,ε(X)) 1X≤a] +Bε. (2)
The second expectation writes as
E[(1−fa+Kε,ε(X)) 1X≤a] =
∫
R
(1−fa+Kε,ε(x)) 1(−∞,a](x) PX(dx)
=−
∫
R
((1−fa+Kε,ε(x)) 1(−∞,a](x))′FX(x)dx =A1 +A2,
where A1 = (1 −fa+Kε,ε(a))FX(a), A2 =
∫
Rf′
a+Kε,ε(x) 1(−∞,a](x)FX(x)dx. Indeed, in the space of
tempered distributions,((1−fa+Kε,ε(x)) 1(−∞,a](x))′ =−(1−fa+Kε,ε(x))δa(x)−f′
a+Kε,ε(x) 1(−∞,a](x).
We evaluate the two termsA1 and A2 as follows:
• Since FX(a)≤FY (a) +∆,
A1≤ (1−fa+Kε,ε(a))FY (a) + (1−fa+Kε,ε(a))∆
≤
∫
R
(1−fa+Kε,ε(x))δa(x)FY (x)dx+ (1−f1(−K))∆.
• For A2, since FX(x)≥ FY (x)−∆ and the derivative offa+Kε,ε is negative, an upper bound is
obtained as follows:
A2≤
∫
R
f′
a+Kε,ε(x) 1(−∞,a](x)FY (x)dx−∆
∫
R
f′
a+Kε,ε(x) 1(−∞,a](x)dx
=
∫
R
f′
a+Kε,ε(x) 1(−∞,a](x)FY (x)dx+ (1−fa+Kε,ε(a))∆
=
∫
R
f′
a+Kε,ε(x) 1(−∞,a](x)FY (x)dx+ (1−f1(−K))∆.
Therefore, by gathering the bounds onA1 and A2, we get
E[(1−fa+Kε,ε(X)) 1X≤a]≤ E[(1−fa+Kε,ε(Y )) 1Y≤a] + 2(1−f1(−K))∆. (3)
On the other hand, ifm is a bound on the densityfY of Y, then
E[fa+Kε,ε(Y ) 1Y≥a] =
∫ ∞
a
fa+Kε,ε(y)fY (y)dy
≤m
∫ ∞
a
fε(y−a−Kε)dy =m
∫ ∞
0
fε(y−Kε)dy
≤mε
∫ ∞
0
f1(u−K)du≤mε
(
K + 3
3
√
3
π
)
;
and
E[fa+Kε,ε(Y )]≤ E[fa+Kε,ε(Y ) 1Y≤a] +m
(
K + 3
3
√
3
π
)
ε. (4)
Mod-φ convergence, II: Estimates on the speed of convergence 17
Putting together Eqs. (2), (3) and (4), we get
FX(a)≤FY (a) +
(
B +m
(
K + 3
3
√
3
π
))
ε + 64
πK 3 ∆.
Similarly,FX(a)≥FY (a)−
(
B +m(K + 3 3
√
3
π )
)
ε− 64
πK 3 ∆, so in the end
∆ = sup
a∈R
|FX(a)−FY (a)|≤
(
B +m
(
K + 3
3
√
3
π
))
ε + 64
πK 3 ∆.
As this is true for everyK, settingK = 4 3
√
1+λ
πλ with λ> 0, one obtains
∆≤ (1 +λ)
(
B + m
3√π
(
4
3
√
1 + 1
λ + 3
3√
3
))
ε. ⊓ ⊔
In the next Section 2.5, we shall combine Theorem 19 and the estimates on smooth test distributions
given by Proposition 16 to get a Berry–Esseen type bound on the Kolmogorov distances in the setting of
mod-φ convergence.
