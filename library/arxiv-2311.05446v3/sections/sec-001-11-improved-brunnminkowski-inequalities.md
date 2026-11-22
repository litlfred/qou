---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-001-11-improved-brunnminkowski-inequalities
section_title: "Improved Brunn–Minkowski inequalities"
section_number: 1.1
pages: 1-3
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.975
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
Let $\nu$ be a Borel measure on $\mathbb{R}^{n}$. We say that $\nu$ satisfies a Brunn--Minkowski inequality with exponent $a$ if for all Borel sets $K_{0}, K_{1} \subseteq\mathbb{R}^{n}$ satisfying $\nu(K_{0}),\nu(K_{1})>0$ and every $0\le t \le1$ we have $$\label{eq:BM}
\nu\left((1-t)K_{0}+ t K_{1}\right)\ge\left((1-t)\nu(K_{0})^{a}+ t \nu(K_{1})^{a}\right)^{1/a}.$$ Here $(1-t)K_{0} +t K_{1}=\left\{ (1-t) x+ t  y:\ x\in K_{0},\ y\in K_{1}\right\}$ is the $t$-*Minkowski average* of the sets $K_{0}$ and $K_{1}$. Note that the inequality becomes stronger as $a$ increases. The prototypical example is the classical BrunnMinkowski inequality, which states that the Lebesgue measure satisfies ([\[eq:BM\]](#eq:BM){reference-type="eqref" reference="eq:BM"}) with exponent $a=\frac{1}{n}$ (see e.g. [@Gardner02] for a survey on the BrunnMinkowski inequality and its importance). When $\nu$ is not the Lebesgue measure, inequalities such as [\[eq:BM\]](#eq:BM){reference-type="eqref" reference="eq:BM"} are sometimes called weighted Brunn--Minkowski inequalities.

More generally, from the works of Borell ([@Borell74], [@Borell75]) and Brascamp--Lieb ([@BrascampLieb76BBL]), a characterization of all measures $\nu$ which satisfy ([\[eq:BM\]](#eq:BM){reference-type="eqref" reference="eq:BM"}) for some exponent $a$ is known:

::: thm
[]{#thm: Borell label="thm: Borell"} Let $\nu$ be a Borel measure on $\mathbb{R}^{n}$ with density $\phi$ with respect to the Lebesgue measure on $\mathbb{R}^n$, and fix $a\in[-\infty,\frac{1}{n}]$. Then the following are equivalent:

1.  $\nu$ satisfies a BrunnMinkowski inequality with exponent $a$ (we also say that $\nu$ is $a$-concave).

2.  For all $x,y\in\mathbb{R}^{n}$ with $\phi(x),\phi(y)>0$ and every $0\le t \le1$ we have $$\phi\left(\left(1-t\right)x+t y\right)\ge\left((1-t)\phi(x)^{b}+t\phi(y)^{b}\right)^{1/b},$$ where $\frac{1}{a}=\frac{1}{b}+n$ (we also say that $\phi$ is $b$-concave).
:::

For simplicity we assumed that $\nu$ has a density, though Borell's original result is slightly more general. Note that the cases where $a$ or $b$ belong to $\left\{ -\infty,0,+\infty\right\}$ are interpreted in the limiting sense: We define $\left((1-\lambda)x^{a}+\lambda y^{a}\right)^{1/a}$ to be $\max(x,y)$ if $a=\infty$, $x^{1-\lambda}y^{\lambda}$ if $a=0$, and $\min(x,y)$ if $a=-\infty$.

Of special interest to us will be the case $a=b=0$, when Borell's theorem essentially reduces to the PrékopaLeindler inequality ([@Prekopa71; @Leindler72]): A measure $\nu$ is *log-concave*, i.e. it satisfies $$\nu\left((1-t)K_{0}+t K_{1}\right)\ge\nu(K_{0})^{1-t}\nu(K_{1})^{t},$$ if and only if its density $\phi$ is of the form $\phi=e^{-V}$ where $V:\mathbb{R}^{n}\to[0,\infty)$ is a convex function.

Borell's theorem gives us the best possible BrunnMinkowski inequality satisfied by a measure $\nu$ for *all* Borel sets $K_{0}$ and $K_{1}$. However, a better inequality may hold for specific choices of $K_{0}$ and $K_{1}$. For example, let $\gamma$ denote the standard Gaussian measure on $\mathbb{R}^{n}$, i.e. the measure with density $\frac{\mathrm{d}\gamma}{\mathrm{d}x}=\frac{1}{\left(2\pi\right)^{n/2}}e^{-\left|x\right|^{2}/2}$. This is a log-concave measure, but in general it doesn't satisfy the BrunnMinkowski inequality with any exponent $a>0$. However, KolesnikovLivshyts ([@KolesnikovLivshyts21]) proved that if $K_{0},K_{1}\subseteq\mathbb{R}^{n}$ are convex sets such that $0\in K_{0}\cap K_{1}$, then we have $$\gamma\left((1-t)K_{0} + t K_{1}\right)^{\frac{1}{2n}}\ge(1-t)\gamma(K_{0})^{\frac{1}{2n}}+t \gamma(K_{1})^{\frac{1}{2n}}.\label{eq:gassian-BM-2n}$$

Eskenazis and Moschidis ([@EskenazisMoschidis21]) further proved that if $K_{0},K_{1}\subseteq\mathbb{R}^{n}$ are convex and *origin-symmetric* (i.e. $K_{0}=-K_{0}$ and $K_{1}=-K_{1}$), the exponent $\frac{1}{2n}$ improves to $\frac{1}{n}$, which is the best possible. This settled a conjecture of Gardner and Zvavitch ([@GardnerZvavitch10]). In fact, the original conjecture was that perhaps the condition $0\in K_{0}\cap K_{1}$ is sufficient to have ([\[eq:gassian-BM-2n\]](#eq:gassian-BM-2n){reference-type="eqref" reference="eq:gassian-BM-2n"}) with exponent $\frac{1}{n}$, but Nayar and Tkocz ([@NayarTkocz13]) proved that this is not the case and suggested that central symmetry may be the correct condition.

More generally, the following conjecture is widely believed:

::: con
[]{#conj:DBM label="conj:DBM"}Let $\nu$ be an even log-concave measure on $\mathbb{R}^{n}$. Then for every $K_{0},K_{1} \subseteq\mathbb{R}^{n}$ which are convex and origin-symmetric we have $$\nu\left((1-t)K_{0}+t K_{1}\right)^{\frac{1}{n}}\ge(1-t)\nu(K_{0})^{\frac{1}{n}}+ t\nu(K_{1})^{\frac{1}{n}}.$$
:::

One reason to believe this conjecture is the paper [@LivshytsMarsigliettiNayarZvavitch17], which shows that it would follow from another important conjecture, the log-BrunnMinkowski conjecture. In particular, the results of BöröczkyLutwakYangZhang ([@BoroczkyLutwakYangZhang12]) show that Conjecture [\[conj:DBM\]](#conj:DBM){reference-type="ref" reference="conj:DBM"} holds in dimension $n=2$.

In dimensions $n>2$, not much is known. It is immediate from Borell's theorem that uniform measures on convex bodies satisfy the BrunnMinkowski inequality with exponent $\frac{1}{n}$ without any symmetry assumptions. The results of [@Cordero-ErasquinRotem23] show that the conjecture holds in particular for rotation-invariant log-concave measures (as well as some rotation-invariant measures that are not log-concave). Livshyts ([@Livshyts23]) proved that the conjecture holds for all even log-concave measures, but with the optimal exponent $\frac{1}{n}$ replaced by $\frac{1}{n^{4+o(1)}}$.

The proofs of all the results mentioned so far followed the same general strategy. The idea was developed by Kolesnikov and Milman ([@KolesnikovMilman18], [@KolesnikovMilman22]) to study various BrunnMinkowski type inequalities, both on $\mathbb{R}^{n}$ and in the setting of Riemannian manifolds. The details will not be very important for us, but roughly speaking one tries to prove that $\frac{\mathrm{d}^{2}}{\mathrm{d}t^{2}}\left(\nu\left((1-t)K_{0}+t K_{1}\right)^{a}\right)\le0$ by directly computing this second derivative. Without loss of generality it is enough to check this at $t=0$, which gives a functional inequality for functions $f:\partial K_{0} \to\mathbb{R}$. Then the crucial step is to transform this inequality to an inequality for functions $u:K_{0} \to\mathbb{R}$ by taking $u$ to be the solution of a certain elliptic PDE with $f$ as its Neumann boundary condition. As far as we can tell this strategy strongly depends on the convexity of $K_{0}$ and $K_{1}$, and without this assumption no results are possible.
