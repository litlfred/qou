---
doc_id: 1172-4
doc_title: "Notes on Construction of the Knot Invariant from Quantum Dilogarithm Function"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-9
source_pdf: 1172-4.pdf
source_sha256: ffc47732ce0138e9
toc_source: inferred
doc_brief: "Hikami, Notes on construction of the knot invariant from the quantum dilogarithm function (RIMS Kôkyûroku) — knot invariants built from Faddeev's quantum dilogarithm."
---
Introduction
Since the discovery of the Jones polynomial [15], the quantum
$\mathrm{g}\mathrm{r}o$up has
$\dot{\mathrm{b}}\mathrm{e}\mathrm{e}\mathrm{n}$ used to
construct the invariants of knots and links, and many knot invariants such as HOM-
FLY polynomial [9], colored Jones polynomial [4], Kauﬀman
$\mathrm{p}o$lynomial [22], have been
$\mathrm{p}\mathrm{r}o$posed. Recently Kashaev constructed a knot invariant by use of the cyclic quantum
dilogarithm function [17, 19, 21].
It was shown in Ref. 28 that Kashaev’s invariant
exactly coincides with the colored Jones polynomial at N-th root of unity, but what is
remarkable is that he claimed that the asymptotic value of his knot invariant (or, the
colored Jones polynomial) in a limit $Narrow\infty$ coincides with the hyperbolic
$\mathrm{v}o$lume of the
knot complement. Due to the fact that the hyperbolic knot complement is decomposed
into the ideal tetrahedra (see, e.g., Ref. 36), and that the
$\mathrm{v}o$lume of each tetrahedron
is given by use of the Lobachevsky function (see, e.g. Ref. 27), it might be natural to
Kashaev’s invariant is connected with the hyperbolic
$\mathrm{v}o$lume. While Kashaev deﬁned the
knot invariant using the quantum dilogarithm function with
$q$ being N-th root of unity
(cyclic dilogarithm function) and studied the asymptotic behavior $Narrow\infty$ , our purpose
here is rather to use the inﬁnite dimensional representation of the quantum dilogarithm
function in a case of $|q|=1$ and then take a limit $qarrow 1$ .
$\uparrow \mathrm{E}$-mail:
$\mathrm{h}\mathrm{i}\mathrm{k}\mathrm{a}\mathrm{m}\mathrm{i}\emptyset \mathrm{p}\mathrm{h}\mathrm{y}\mathrm{s}.\mathrm{s}.\mathrm{u}$ -tokyo.
$\mathrm{a}\mathrm{c}$ . jp
Address: Departmen
$\zeta$ ofPhysics, Gradua
$\mathrm{t}e$ School of Science, University of Tokyo, Hongo 7-3-1, Bunkyo,
$To\varphi o$ I 13-0033,
$\int \mathrm{a}p\partial n$.
数理解析研究所講究録
1172 巻2000 年44-69
This Note is organized as follows. We ﬁrst review several relations for the diloga-
rithm function. See Ref. 25 and references therein for topics of the dilogarithm function.
We then deﬁne the quantum dilogarithm function as a
$q$-deformation of the dilogarithm
function. Depending on a deformation parameter
$q$ , we have two deftnitions of the quan-
tum dilogarithm function; one of them is for
$q$ generic, and it is essentially given by the
$q$-exponential function. In the case of $|q|=1$ , we have
$\mathrm{a}\mathrm{n}o$ther deﬁnition in an integral
form [5]. We show that the quantum dilogarithm function satisﬁes interesting properties
with non-commutative variables. See Ref. 26 for a survey on the special functions and
$q$-commuting variables. At last stage we show that the
$R$-operator as a solution of the
constant Yang-Baxter equation can be given from the quantum dilogarithm function.
We compute the matrix elements on the inftnite dimensional space, and based on this
$R$-operator we construct the knot invariant.
2
Dilogarithm Function
The Euler dilogarithm function $Li_{2}(x)$ is deftned by
$Li_{2}(x)=n1 \sum_{=}\frac{x^{n}}{n^{2}}\infty$
(2.1a)
$=- \int_{0}^{x}\frac{\log(1-s)}{s}\mathrm{d}s$,
(2.1b)
which gives
$Li_{2}(0)=0$ ,
$Li_{2}(1)= \frac{\pi^{2}}{6}$ .
By the integral representation (2.1b), the Euler dilogarithm $Li_{2}(x)$ is analytically contin-
ued to the complex plane with a cut
$\mathrm{a}1\mathit{0}$ng the real axis
$[1, +\infty]$ . We also use the
$\mathrm{R}o$gers
dilogarithm function $L(x)$ , which is given by
$L(x)=Li_{2}(x)+ \frac{1}{2}\log x\cdot\log(1-X)$
$=- \frac{1}{2}\int_{0}^{x}(\frac{\log(1-S)}{s}+\frac{\log s}{1-s})\mathrm{d}s$ .
(2.2)
This function satisﬁes following relations;
$L(x)+L(1-x)= \frac{\pi^{2}}{6}$ ,
(2.3)
$L(x)+L(y)=L(xy)+L( \frac{x(1-y)}{1-xy})+L(\frac{y(1-x)}{1-xy})$ .
(2.4)
The second identity is called the pentago
$\mathrm{n}$ identity. Note that the dilogarithm function
often appears in various studies of mathematical physics, such as the computation of
the central charge of the conformal ﬁeld theory $[23, 24]$ , where a technique in Ref. 31
has been extensively applied.
The hyperbolic
$\mathrm{v}o$lume of the ideal tetrahedron with face angle
$\alpha,$
$\beta$, and
$\gamma$ (we have
$\alpha+\beta+\gamma=2\pi)$ is given by
$J\mathrm{I}(\alpha)+\ulcorner 1(\beta)+r1(\gamma)[27]$, where the Lobachevsky function
$J\mathrm{I}(\theta)$ is deﬁned as
$\Gamma 1(\theta)=-\int_{0}^{\theta}\log|2\sin u|\mathrm{d}u$.
(2.5)
The function
$.\ulcorner 1(\theta)$ can be written in terms of the dilogarithm function as
$\uparrow$
$Li_{2}( \mathrm{e}^{2\mathrm{i}\theta})=\frac{\pi^{2}}{6}-\theta(\pi-\theta)+2\mathrm{i}r\downarrow(\theta)$ .
(2.6)
Further when we parameterize an ideal tetrahedron by a
$\mathrm{c}o$mplex parameter
$Z$ with Imz
$>$
$0$ , the hyperbolic
$\mathrm{v}o$lume is given by the
$\mathrm{B}\mathrm{l}o\mathrm{c}\mathrm{h}-\mathrm{w}\mathrm{i}\mathrm{g}\mathrm{n}\mathrm{e}\mathrm{r}$ function $D(z)$ ,
$D(z)=\arg(1-Z)\cdot\log|\mathcal{Z}|+{\rm Im} Li2(z)$ .
(2.7)
3
$\mathrm{O}\mathrm{u}\mathrm{a}\mathrm{n}\mathrm{t}\mathrm{u}\sim \mathrm{m}$ Dilogarithm Function 1
We deﬁne the quantum dilogarithm function $S_{q}(w)$ for $|q|<1$ ;
$S_{q}(w)= \prod_{n=0}^{\infty}(1+q^{2}w)n+1$
(3.1a)
$=1+ \sum_{k=1}^{\infty}\frac{(-1)^{k}q^{\frac{k.(k-1)}{2}}w^{k}}{(q-q^{-1})\cdot\cdot(q^{k}-q-k)}$
(3.1b)
$= \exp(\sum_{k=1}^{\infty}\frac{(-1)^{k}w^{k}}{k(q^{kk}-q^{-})})$ .
(3.1C)
$\uparrow \mathrm{i}\equiv\sqrt{-1}$
These identities can be proved by the fact that each expression satisﬁes following diﬀer-
ence equation and an initial condition;
$\frac{S_{q}(qw)}{S_{q}(q^{-1}w)}=\frac{1}{1+w}$
(3.2)
$S_{q}(0)=1$ .
This deﬁnition shows that the function
$S_{q}(w)$ is merely a q-exponential function.
To
see that this function is a one-parameter deformation of the dilogarithm, we take an
$\mathrm{a}\mathrm{S}\mathrm{y}\mathrm{m}\mathrm{P}\mathrm{t}\mathrm{O}$tic behavior $qarrow 1$ in eq. (3.1a). Using the
$\mathrm{E}\mathrm{u}\mathrm{l}\mathrm{e}\mathrm{r}-\mathrm{M}\mathrm{c}\mathrm{L}\mathrm{a}\mathrm{u}\mathrm{g}\mathrm{h}\mathrm{l}\mathrm{i}\mathrm{n}$ formula, we get
$S_{q}(w)=\sqrt{1+w}\cdot \mathrm{e}^{-\frac{1}{\epsilon}Li}(-w)2(1+O(\epsilon^{3}))$ ,
(3.3)
where we have set
$q=\mathrm{e}^{-\frac{\epsilon}{2}}$ .
The reason why we call $S_{q}(w)$ as the quantum dilogarithm function is due to the fact
that it also satisﬁes the pentagon identity [7]. When we use the Weyl operato
$\mathrm{r}\mathrm{s}$ \^a and
$\hat{b}$
$\mathrm{s}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{s}\mathfrak{h}^{\gamma}\mathrm{i}\mathrm{n}\mathrm{g}$
\^a
$\hat{b}=q^{2}\hat{b}$ \^a,
we have
$S_{q}(\hat{a})S_{q}(\hat{b})=S(q\hat{b}\hat{a}+)$.
(3.4)
This identity ﬁrst appeared in Ref. 33, and can be proved from eq. (3.1b) with a help of
the
$q$-binomial formula;
$( \hat{a}+\hat{b})^{n}=\sum_{k=0}\frac{(q^{2},q^{2})_{n}}{(q^{2}1q^{2})_{k}(q^{2},q^{2})_{n-k}}n.\cdot.\hat{b}^{n-}k\hat{a}^{k}$ .
The function
$S_{q}(w)$ further satisﬁes following identities;
$S_{q}(\hat{b})s_{q}(\hat{a})=S_{q}(\hat{a}+q^{-1}\hat{a}\hat{b})S_{q}(\hat{b})$
(3.5a)
$=S_{q}(\hat{a}+\hat{b}+q^{-}\hat{a}\hat{b}1)$
(3.5b)
$=S_{q}(\hat{a})s_{q}(q-1\hat{a}\hat{b}+\hat{b})$
(3.5C)
$=S_{q}$ (\^a)
$s_{q}(q^{-}\hat{a}\hat{b}1)S_{q}(\hat{b})$ .
(3.5d)
Proof is as follows. As we have
$S_{q}(\hat{b})\cdot$ \^a $\cdot(S_{q}(\hat{b}))-1=\hat{a}\cdot s_{q}(q-2\hat{b})\cdot(S_{q}(\hat{b}))-1(=\hat{a}\cdot 1+q-1\hat{b})$ ,
we obtain the ﬁrst equality;
$S_{q}(\hat{b})\cdot S_{q}(\hat{a})\cdot(S_{q}(\hat{b}))-1=S_{q}(S_{q}(\hat{b})\cdot$ \^a
$\cdot(S_{q}(\hat{b}))^{-1})=S_{q}(\hat{a}\cdot(1+q^{-1}\hat{b}))$ .
All other equalities can be derived by repeated use of eq. (3.4). The last equation is the
quantum pentagon identity [7].
It was shown in Refs. 2, 7 that it gives the classical
pentagon identity (2.4) in
$qarrow 1\mathrm{l}\mathrm{i}\mathrm{m}\mathrm{i}\mathrm{t}$.
We can obtain a braid relation from the quantum dilogarithm function [25]. We deﬁne
the function
$\Theta(w)$ as
$\Theta(w)=S_{q}(qw)s_{q}(q-1-w1)$
(3.6)
$= \frac{1}{(q^{2},q^{2})_{\infty}}.\sum_{n\in \mathbb{Z}}q^{n^{2}}w^{n}$ .
The second equality is the Jacobi triple product identity. When the operators
\^a and
$\hat{b}$
$\mathrm{S}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{S}\mathfrak{h}$’ the
$q$-commutation relation,
\^a $\hat{b}=q^{2}\hat{b}$ \^a, we obtain that the
$\Theta$-function satisﬁes
the braid relation
$\Theta(\hat{a})\Theta(\hat{b})\Theta(\hat{a})=\Theta(\hat{b})\Theta(\hat{a})\Theta(\hat{b})$ .
(3.7)
Proof is straightforward by applying
$\mathrm{e}\mathrm{q}\mathrm{s}$.
$(3.4)$ and (3.5) $[10, 25]$ , and it can be extend
to the
$\mathrm{s}1(N)$ case [14]. We can give the knot invariant as a
$q$-series by use of this braid
relation [11], although this does not seem to be related with Kashaev’s invariant. We
rather give another solution of the braid relation in terms of the quantum dilogarithm
function in the following section.
To close this section, we note that we can solve a non-constant solution of the Yang-
Baxter equation in terms of $S_{q}(w)[8,10, 12,38]$ , and it was shown [1] that the universal
$R$-matrix with a
$q$-oscillator representation reduces to this solution.
4
Quantum Dilogarithm Function II
In the case of the $|q|=1$ we should modify the deﬁnition (3.1a) of the quantum diloga-
rithm function. Hereafter we set
$q=\mathrm{e}^{\mathrm{i}\gamma}$ ,
(4.1)
where
$\gamma$ is real,and it corresponds to the Planck constant
$\gamma=\hslash/2$ . We deﬁne
$\Phi_{\gamma}(\varphi)$ by
an integral form,
$\Phi_{\gamma}(\varphi)=\exp(\int_{\mathbb{R}+\mathrm{i}0}\frac{\mathrm{e}^{-\mathrm{i}\varphi x}}{4\mathrm{s}\mathrm{h}(\gamma X)\mathrm{s}\mathrm{h}(\pi X)}\frac{\mathrm{d}x}{x}\mathrm{I}\cdot$
(4.2)
This integral was ﬁrst introduced by Faddeev $[5, 6]$ . See also Ref. 32 where a similar
integral was
$s$tudied in a cont
$e\mathrm{x}\mathrm{t}$ of the hyperbolic gamma function.
The similarity
between this integral and the scattering matrix of the Liouville theory is claimed in
Ref. 5, and it follows from that the integral (4.2) plays a role of intertwining operator.
$\mathrm{F}o\mathrm{r}$ our later
$\mathrm{c}o$nvention to study th $e$ ‘Volume
$\mathrm{c}o$njecture”, we have interests in the
asymptotic behavior in a limit $qarrow 1$ , i.e.,
$\gammaarrow 0$ . Like eq. (3.3), the function
$\Phi_{\gamma}(\varphi)$
behaves in this limit as
$\Phi_{\gamma}(\varphi)\sim\exp(\frac{1}{2\mathrm{i}\gamma}Li_{2}(-\mathrm{e}^{\varphi})\mathrm{I}$ ,
for
$\gammaarrow 0$ .
(4.3)
This behavior indicates that the integral
$\Phi_{\gamma}$ is indeed a deformation of the Euler diloga-
rithm function. We remark that we have an inversion relation,
$\Phi_{\gamma}(\varphi)\cdot\Phi_{\gamma}(-\varphi)=\exp(-\frac{1}{2\mathrm{i}\gamma}(\frac{\varphi^{2}}{2}+\frac{\pi^{2}+\gamma^{2}}{6}))$ ,
(4.4)
which follows from a residue at the origin. From an asymptotic behavior of eq. (4.4) in
a limit
$\gammaarrow 0$ , we have a nontrivial identity for the Euler dilogarithm function;
$Li_{2}(- \mathrm{e}^{\varphi})+Li_{2}(-\mathrm{e}^{-\varphi})+\frac{\varphi^{2}}{2}+\frac{\pi^{2}}{6}=0$ .
(4.5)
We can check that the integral (4.2) satisﬁes the diﬀerence equations. We ﬁnd by
direct computation that
$\frac{\Phi_{\gamma}(\varphi+\mathrm{i}\gamma)}{\Phi_{\gamma}(\varphi-\mathrm{i}\gamma)}=\frac{1}{1+\mathrm{e}^{\varphi}}$
(4.6a)
$\frac{\Phi_{\gamma}(\varphi+\mathrm{i}\pi)}{\Phi_{\gamma}(\varphi-\mathrm{i}\pi)}=\frac{1}{1+\mathrm{e}^{\frac{\pi}{\gamma}\varphi}}$.
(4.6b)
The ﬁrst equality corresponds to eq. (3.2), and thus the Faddeev integral (4.2) can be
regarded as a function $S_{q}(w)(3.1)$ in a case of $|q|=1$ . Remarkable is that the integral
has a kind of “duality”;
$\gammarightarrow\frac{\pi^{2}}{\gamma}$ . In fact by collecting a residue of the integral (4.2) and
recalling a deﬁnition (3.1c), the integral
$\Phi_{\gamma}$ is represented by
$\Phi_{\gamma}(\varphi)=S_{q}(\mathrm{e}^{\varphi})\cdot sQ(\mathrm{e}^{\varphi\frac{\pi}{\gamma}})$ ,
where
$Q=\mathrm{e}^{\mathrm{i}\frac{\pi^{2}}{\gamma}}$ . We therefore have a “factorization” property for the integral.
This factorization can be realized by use of the quantum canonical operators [6]. We
consider the algebra generated by the Heisenberg pair
$\hat{p}$ and
$\hat{q}$ ;
$[\hat{p},\hat{q}]=-2\mathrm{i}\gamma$.
(4.7)
By use of these operators we can realize the Weyl pairs as follows;
\^u
$\hat{v}=q^{2}\hat{v}$ \^u,
$\hat{U}\hat{V}=Q^{2}\hat{V}\hat{U}$,
where
$\hat{u}=\mathrm{e}^{\hat{q}}$,
$\hat{v}=\mathrm{e}^{\hat{p}}$ ,
$\hat{U}=\mathrm{e}^{\frac{\pi}{\gamma}\hat{q}}$ ,
$\hat{V}=\mathrm{e}^{\frac{\pi}{\gamma}\hat{p}}$.
See the commutativity,
$\hat{U}$
$\text{\^{u}}=\hat{u}\hat{U}$ ,
$\hat{V}\hat{v}=\hat{v}\hat{V}$,
$\hat{U}\hat{v}=\hat{v}\hat{U}$ ,
\^u
$\hat{V}=\hat{V}$ \^u.
We can ﬁnd that the Weyl algebra generated above by
$\hat{p}$ and
$\hat{q}$ is factored into two alge-
bra $s$
$($\^u ,
$\hat{v})$ and
$(\hat{U} , \hat{V})$ . As a result, from the pentagon relation (3.5d) for $S_{q}(w)$ and a
commutativity of two algebras, we also have the pentagon relation for the integral
$\Phi_{\gamma}$ ,
$\Phi_{\gamma}(\hat{p})\Phi_{\gamma}(\hat{q})=\Phi_{\gamma}(\hat{q})\Phi\gamma(\hat{p}+\hat{q})\Phi_{\gamma}(\hat{p})$,
(4.8)
where we have used
$\mathrm{e}^{\hat{q}}\mathrm{e}^{\hat{p}}=\mathrm{e}^{\hat{p}\hat{q}+\mathrm{i}\gamma}+$.
We rewrite the pentagon relation (4.8) in a simple form. We introduce the S-operator
as an operator acting on a Hilbert space
$\mathrm{V}\otimes \mathrm{V}$ ,
$S_{1,2}=\mathrm{e}^{\frac{1}{2\mathrm{i}\gamma}}\Phi\hat{q}_{1\hat{p}}2\gamma(\hat{p}1+\hat{q}_{2}-\hat{p}_{2})$ ,
(4.9)
where
$\hat{p}_{1}=\hat{p}\otimes 1,\hat{p}_{2}=1\otimes\hat{p}$ and $so$ on. It is easy to see that the
$S$-operato
$\mathrm{r}$ satisﬁes an
identity;
$S_{2,3}S_{1,2}=S1,2S1,3S2,3$ .
(4.10)
Here we have only applied the commutation relation (4.7) to
$\mathrm{e}\mathrm{q}\mathrm{s}$.
$(4.8)$ .
This simple
form of the pentagon identity was used to deﬁne the $6j$ symbol [16] and to quantize the
Teichm\"uller space $[3, 20]$ .
We have the braid generato
$\mathrm{r}$ as in a case $o\mathrm{f}|q|<1$ , and furthermore in the case $|q|=1$
we can construct
$\mathrm{a}\mathrm{n}o$ther
$\mathrm{t}\mathrm{y}\mathrm{p}e$ of solution of the braid relation by use of a solution of the
pentagon identity (4.10). We deﬁne the
$R$-operator on a space
$\mathrm{V}^{\otimes 4}$ as [18]
$R_{12,34}=(S_{1,4}^{\mathrm{t}}4)-1S_{1,3}s_{2,4}\mathrm{t}_{2}\mathrm{t}_{4}(S_{2,3}^{\mathrm{t}_{2}})^{-1}$ ,
(4.11)
where
$\mathrm{t}_{a}$ means a transposition operation on the a-th Hilbert space V. We can see that
the
$R$-operator (4.11) satisﬁes the constant Yang-Baxter relation,
$R_{11’,221}\prime R1^{J},33^{\prime R_{22}}J,33^{l}=R_{22’,33}\prime R11’,33\prime R_{11^{l}},22’$.
(4.12)
Proof follows from recursive use of the pentagon identity (4.10) and its
$\mathrm{c}o\mathrm{r}o$llary such as
$S_{1,2}(s_{1_{1}\mathrm{s}}^{t}3)^{-1}(s_{2}^{t_{3}},3)^{-}1=(S_{2}t_{3},3)-1S_{1},2$,
$(S_{1,2}^{t_{1}})^{-}1(S_{1}t_{1},3)^{-}1s2,3=s2,3(S_{1,2}t_{1})-1$ .
When we deﬁne the operator
$\mathrm{R}:\mathrm{V}^{\otimes 2}\otimes \mathrm{V}^{@2}arrow \mathrm{V}^{\otimes 2}\otimes \mathrm{V}^{\copyright 2}$ by
$\mathrm{R}=P_{1},{}_{2}P_{1’},2^{\prime R_{11’},\prime}22$,
(4.13)
$.\mathrm{w}$here
$P$ is a permutation operator, we ﬁnd that the operator R. is a solution of the braid
relation,
$(\mathrm{R}\otimes 1)(1\otimes \mathrm{R})(\mathrm{R}\otimes 1)=(1\otimes \mathrm{R})(\mathrm{R}\otimes 1)(1\otimes \mathrm{R})$ .
(4.14)
For our later convention, we deﬁne other operato
$\mathrm{r}\mathrm{s}Y$ and
$Z$ ;
$Y= \exp(\frac{C}{2\gamma \mathrm{i}}\hat{p})$ ,
(4.15)
$Z= \exp(\frac{C}{2\gamma \mathrm{i}}\hat{q})$ ,
(4.16)
where
$C$ is an arbitrary parameter. We ﬁnd simply that these operators
$\mathrm{s}\mathrm{a}\mathrm{t}\mathrm{i}\mathrm{S}6$’
$Y_{1}Y_{2}S1,2=S_{1},2Y1$ ,
(4.17a)
$Z_{2}S_{1,2}=S_{1,2}Z_{12}z$ ,
(4.17b)
$Z_{1}Y_{21,2}S=S_{1,2}Z_{1}Y_{2}$ ,
(4.17c)
where
$S_{1,2}$ is deﬁned in eq. (4.9). With the operators
$Y$ and
$Z$, we deﬁne operators
$\mathrm{D}$
and
$\tilde{\mathrm{D}}$ on
$\mathrm{V}^{@2}$ as
$\mathrm{D}\equiv D_{1,1’}=Y_{1}(Y_{1}^{\mathrm{t}_{1’}},)^{-1}$ ,
(4.18)
$\tilde{\mathrm{D}}\equiv\tilde{D}_{1,1^{l=Z}}1(Z_{1}^{\mathrm{t}_{1’}},)^{-1}$
(4.19)
Using
$\mathrm{e}\mathrm{q}s$. $(4.11)$ and (4.17), we get
$\mathrm{D}\otimes \mathrm{D}\cdot \mathrm{R}=\mathrm{R}\cdot \mathrm{D}\otimes \mathrm{D}$ ,
(4.20)
$\tilde{\mathrm{D}}\otimes\tilde{\mathrm{D}}\cdot \mathrm{R}=\mathrm{R}\cdot\tilde{\mathrm{D}}\otimes\tilde{\mathrm{D}}$.
(4.21)
