---
doc_id: 1172-4
doc_title: "Notes on Construction of the Knot Invariant from Quantum Dilogarithm Function"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1172-4.pdf
source_sha256: ffc47732ce0138e9
doc_brief: "Hikami, Notes on construction of the knot invariant from the quantum dilogarithm function (RIMS Kôkyûroku) — knot invariants built from Faddeev's quantum dilogarithm."
---
Since the discovery of the Jones polynomial [15], the quantum $\mathrm{g}\mathrm{r}o$up has $\dot{\mathrm{b}}\mathrm{e}\mathrm{e}\mathrm{n}$used to
construct the invariants of knots and links, and many knot invariants such as HOM-
FLY polynomial [9], colored Jones polynomial [4], Kauﬀman $\mathrm{p}o$lynomial [22], have been
$\mathrm{p}\mathrm{r}o$posed. Recently Kashaev constructed a knot invariant by use of the cyclic quantum
dilogarithm function [17, 19, 21]. It was shown in Ref. 28 that Kashaev’s invariant
exactly coincides with the colored Jones polynomial at N-th root of unity, but what is
remarkable is that he claimed that the asymptotic value of his knot invariant (or, the
colored Jones polynomial) in a limit $Narrow\infty$coincides with the hyperbolic $\mathrm{v}o$lume of the
knot complement. Due to the fact that the hyperbolic knot complement is decomposed
into the ideal tetrahedra (see, e.g., Ref. 36), and that the $\mathrm{v}o$lume of each tetrahedron
is given by use of the Lobachevsky function (see, e.g. Ref. 27), it might be natural to
Kashaev’s invariant is connected with the hyperbolic $\mathrm{v}o$lume. While Kashaev deﬁned the
knot invariant using the quantum dilogarithm function with $q$being N-th root of unity
(cyclic dilogarithm function) and studied the asymptotic behavior $Narrow\infty$, our purpose
here is rather to use the inﬁnite dimensional representation of the quantum dilogarithm
function in a case of $|q|=1$ and then take a limit $qarrow 1$.
$\uparrow \mathrm{E}$-mail: $\mathrm{h}\mathrm{i}\mathrm{k}\mathrm{a}\mathrm{m}\mathrm{i}\emptyset \mathrm{p}\mathrm{h}\mathrm{y}\mathrm{s}.\mathrm{s}.\mathrm{u}$-tokyo. $\mathrm{a}\mathrm{c}$.jp
Address: Departmen$\zeta$of Physics, Gradua$\mathrm{t}e$School of Science, University of Tokyo,Hongo 7-3-1, Bunkyo,
$To\varphi o$I 13-0033, $\int \mathrm{a}p\partial n$.
?tM}2r@O8&5f=j9V5fO?
1172 4,2000 G/44-69 44
This Note is organized as follows. We ﬁrst review several relations for the diloga-
rithm function. See Ref. 25 and references therein for topics of the dilogarithm function.
We then deﬁne the quantum dilogarithm function as a $q$-deformation of the dilogarithm
function. Depending on a deformation parameter $q$, we have two deftnitions of the quan-
tum dilogarithm function; one of them is for $q$generic, and it is essentially given by the
$q$-exponential function. In the case of $|q|=1$, we have $\mathrm{a}\mathrm{n}o$ther deﬁnition in an integral
form [5]. We show that the quantum dilogarithm function satisﬁes interesting properties
with non-commutative variables. See Ref. 26 for a survey on the special functions and
$q$-commuting variables. At last stage we show that the $R$-operator as a solution of the
constant Yang-Baxter equation can be given from the quantum dilogarithm function.
We compute the matrix elements on the inftnite dimensional space, and based on this
$R$-operator we construct the knot invariant.
2 Dilogarithm Function
The Euler dilogarithm function $Li_{2}(x)$is deftned by
$Li_{2}(x)=n1 \sum_{=}\frac{x^{n}}{n^{2}}\infty$ (2.1a)
$=-\int_{0}^{x}\frac{\log(1-s)}{s}\mathrm{d}s$, (2.1b)
which gives
$Li_{2}(0)=0$, $Li_{2}(1)= \frac{\pi^{2}}{6}$.
By the integral representation (2.1b), the Euler dilogarithm $Li_{2}(x)$is analytically contin-
ued to the complex plane with a cut $\mathrm{a}1\mathit{0}$ng the real axis $[1, +\infty]$. We also use the $\mathrm{R}o$gers
dilogarithm function $L(x)$, which is given by
$L(x)=Li_{2}(x)+ \frac{1}{2}\log x\cdot\log(1-X)$
$=-\frac{1}{2}\int_{0}^{x}(\frac{\log(1-S)}{s}+\frac{\log s}{1-s})\mathrm{d}s$. (2.2)
45
This function satisﬁes following relations;
$L(x)+L(1-x)=\frac{\pi^{2}}{6}$, (2.3)
$L(x)+L(y)=L(xy)+L(\frac{x(1-y)}{1-xy})+L(\frac{y(1-x)}{1-xy})$. (2.4)
The second identity is called the pentago $\mathrm{n}$identity. Note that the dilogarithm function
often appears in various studies of mathematical physics, such as the computation of
the central charge of the conformal ﬁeld theory $[23, 24]$, where a technique in Ref. 31
has been extensively applied.
The hyperbolic $\mathrm{v}o$lume of the ideal tetrahedron with face angle $\alpha,$$\beta$, and $\gamma$(we have
$\alpha+\beta+\gamma=2\pi)$is given by $J\mathrm{I}(\alpha)+\ulcorner 1(\beta)+r1(\gamma)[27]$, where the Lobachevsky function
$J\mathrm{I}(\theta)$is deﬁned as
$\Gamma 1(\theta)=-\int_{0}^{\theta}\log|2\sin u|\mathrm{d}u$. (2.5)
The function $.\ulcorner 1(\theta)$can be written in terms of the dilogarithm function as $\uparrow$
$Li_{2}( \mathrm{e}^{2\mathrm{i}\theta})=\frac{\pi^{2}}{6}-\theta(\pi-\theta)+2\mathrm{i}r\downarrow(\theta)$. (2.6)
Further when we parameterize an ideal tetrahedron by a $\mathrm{c}o$mplex parameter $Z$with Imz $>$
$0$, the hyperbolic $\mathrm{v}o$lume is given by the $\mathrm{B}\mathrm{l}o\mathrm{c}\mathrm{h}-\mathrm{w}\mathrm{i}\mathrm{g}\mathrm{n}\mathrm{e}\mathrm{r}$function $D(z)$,
$D(z)=\arg(1-Z)\cdot\log|\mathcal{Z}|+{\rm Im} Li2(z)$. (2.7)
3 $\mathrm{O}\mathrm{u}\mathrm{a}\mathrm{n}\mathrm{t}\mathrm{u}\sim \mathrm{m}$Dilogarithm Function 1
We deﬁne the quantum dilogarithm function $S_{q}(w)$for $|q|<1$;
$S_{q}(w)= \prod_{n=0}^{\infty}(1+q^{2}w)n+1$ (3.1a)
$=1+\sum_{k=1}^{\infty}\frac{(-1)^{k}q^{\frac{k.(k-1)}{2}}w^{k}}{(q-q^{-1})\cdot\cdot(q^{k}-q-k)}$(3.1b)
$=\exp(\sum_{k=1}^{\infty}\frac{(-1)^{k}w^{k}}{k(q^{kk}-q^{-})})$. (3.1C)
$\uparrow \mathrm{i}\equiv\sqrt{-1}$
46
These identities can be proved by the fact that each expression satisﬁes following diﬀer-
ence equation and an initial condition;
$\frac{S_{q}(qw)}{S_{q}(q^{-1}w)}=\frac{1}{1+w}$ (3.2)
$S_{q}(0)=1$.
This deﬁnition shows that the function $S_{q}(w)$is merely a q-exponential function. To
see that this function is a one-parameter deformation of the dilogarithm, we take an
$\mathrm{a}\mathrm{S}\mathrm{y}\mathrm{m}\mathrm{P}\mathrm{t}\mathrm{O}$tic behavior $qarrow 1$in eq. (3.1a). Using the $\mathrm{E}\mathrm{u}\mathrm{l}\mathrm{e}\mathrm{r}-\mathrm{M}\mathrm{c}\mathrm{L}\mathrm{a}\mathrm{u}\mathrm{g}\mathrm{h}\mathrm{l}\mathrm{i}\mathrm{n}$formula, we get
$S_{q}(w)=\sqrt{1+w}\cdot \mathrm{e}^{-\frac{1}{\epsilon}Li}(-w)2(1+O(\epsilon^{3}))$, (3.3)
where we have set $q=\mathrm{e}^{-\frac{\epsilon}{2}}$.
The reason why we call $S_{q}(w)$as the quantum dilogarithm function is due to the fact
that it also satisﬁes the pentagon identity [7]. When we use the Weyl operato $\mathrm{r}\mathrm{s}$\^aand $\hat{b}$
$\mathrm{s}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathfrak{h}^{\gamma}\mathrm{i}\mathrm{n}\mathrm{g}$
\^a$\hat{b}=q^{2}\hat{b}$\^a,
we have
$S_{q}(\hat{a})S_{q}(\hat{b})=S(q\hat{b}\hat{a}+)$. (3.4)
This identity ﬁrst appeared in Ref. 33, and can be proved from eq. (3.1b) with a help of
the $q$-binomial formula;
$(\hat{a}+\hat{b})^{n}=\sum_{k=0}\frac{(q^{2},q^{2})_{n}}{(q^{2}1q^{2})_{k}(q^{2},q^{2})_{n-k}}n.\cdot.\hat{b}^{n-}k\hat{a}^{k}$.
The function $S_{q}(w)$further satisﬁes following identities;
$S_{q}(\hat{b})s_{q}(\hat{a})=S_{q}(\hat{a}+q^{-1}\hat{a}\hat{b})S_{q}(\hat{b})$(3.5a)
$=S_{q}(\hat{a}+\hat{b}+q^{-}\hat{a}\hat{b}1)$ (3.5b)
$=S_{q}(\hat{a})s_{q}(q-1\hat{a}\hat{b}+\hat{b})$(3.5C)
$=S_{q}$(\^a)$s_{q}(q^{-}\hat{a}\hat{b}1)S_{q}(\hat{b})$. (3.5d)
47
Proof is as follows. As we have
$S_{q}(\hat{b})\cdot$\^a$\cdot(S_{q}(\hat{b}))-1=\hat{a}\cdot s_{q}(q-2\hat{b})\cdot(S_{q}(\hat{b}))-1(=\hat{a}\cdot 1+q-1\hat{b})$,
we obtain the ﬁrst equality;
$S_{q}(\hat{b})\cdot S_{q}(\hat{a})\cdot(S_{q}(\hat{b}))-1=S_{q}(S_{q}(\hat{b})\cdot$\^a$\cdot(S_{q}(\hat{b}))^{-1})=S_{q}(\hat{a}\cdot(1+q^{-1}\hat{b}))$.
All other equalities can be derived by repeated use of eq. (3.4). The last equation is the
quantum pentagon identity [7]. It was shown in Refs. 2, 7 that it gives the classical
pentagon identity (2.4) in $qarrow 1\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{t}$.
We can obtain a braid relation from the quantum dilogarithm function [25]. We deﬁne
the function $\Theta(w)$as
$\Theta(w)=S_{q}(qw)s_{q}(q-1-w1)$ (3.6)
$=\frac{1}{(q^{2},q^{2})_{\infty}}.\sum_{n\in \mathbb{Z}}q^{n^{2}}w^{n}$.
The second equality is the Jacobi triple product identity. When the operators \^aand $\hat{b}$
$\mathrm{S}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{S}\mathfrak{h}$’the $q$-commutation relation, \^a$\hat{b}=q^{2}\hat{b}$\^a,we obtain that the $\Theta$-function satisﬁes
the braid relation
$\Theta(\hat{a})\Theta(\hat{b})\Theta(\hat{a})=\Theta(\hat{b})\Theta(\hat{a})\Theta(\hat{b})$. (3.7)
Proof is straightforward by applying $\mathrm{e}\mathrm{q}\mathrm{s}$. $(3.4)$and (3.5) $[10, 25]$, and it can be extend
to the $\mathrm{s}1(N)$case [14]. We can give the knot invariant as a $q$-series by use of this braid
relation [11], although this does not seem to be related with Kashaev’s invariant. We
rather give another solution of the braid relation in terms of the quantum dilogarithm
function in the following section.
To close this section, we note that we can so lve a non-constant solution of the Yang-
Baxter equation in terms of $S_{q}(w)[8,10, 12,38]$, and it was shown [1] that the universal
$R$-matrix with a $q$-oscillator representation reduces to this solution.
48
