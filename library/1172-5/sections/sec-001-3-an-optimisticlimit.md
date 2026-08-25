---
doc_id: 1172-5
doc_title: "Optimistic calculations about the Witten-Reshetikhin-Turaev invariants of closed three-manifolds obtained from the figure-eight knot by integral Dehn surgeries"
section_id: sec-001-3-an-optimisticlimit
section_title: "AN OPTIMISTICLIMIT"
section_number: 3
pages: 3-4
source_pdf: 1172-5.pdf
source_sha256: 21b7a0e13bd208fc
doc_brief: "Optimistic calculations about the Witten-Reshetikhin-Turaev invariants of closed three-manifolds obtained from the figure-eight knot by integral Dehn surgeries — I calculate"
---
Suppose that we are given a function $S(N)$of $N$by the following summation.
(3.1) $S(N)=P(N)n2\sum_{n_{1},,..,n_{k}}.q^{Q+}L\prod_{a=1}(q\alpha)_{l_{a}}\epsilon_{a}$,
where $P(N)$is a function of $N$with polynomial growth, $\epsilon_{a}=\pm 1,$$l_{a}$and $L$are linear
functions of $n_{1},$$n_{2},$$\ldots,$$n_{k}$(they do not depend on $N$but may have constant terms),
$Q=\sum_{1\leq i\leq j\leq k}\gamma_{i}jn_{i}nj$, and the summation runs over some range in $\{(n_{1}, n_{2}, \ldots, n_{k})|$
$0\leq n_{i}\leq N-1(i=1,2, \ldots, k)\}$. Note that $q=\exp(\frac{2\pi\sqrt{-1}}{N})$and we regard $S$
as a function of $N$rather than $q$.
Then an optimistic limit of $\frac{2\pi\sqrt{-1}\log S(N)}{N}$) denoted by $N arrow\infty(\succ\lim\frac{2\pi\sqrt{-1}\log S(N)}{N}$
is deﬁned as follows.
First we replace $S(N)/P(N)$ with the following iterated integral $I(N)$along
some contours.
(3.2) $I(N):=\int\cdots\int\exp[\frac{N}{2\pi\sqrt{-1}}V(Z_{1}, z_{2}, \ldots, Z_{k})]dZ_{1}dZ2\ldots dz_{k}$.
Here $V(z_{1}, Z_{2}, \ldots, Z_{k})$is deﬁned as follows. Put
(3.3) $\tilde{V}(z_{1}, z_{2}, \ldots, Zk):=-\sum_{a=1}^{\alpha}\epsilon_{a}\{\mathrm{L}\mathrm{i}_{2}(x_{a})-\frac{\pi^{2}}{6}\}+\sum_{1\leq i\leq j\leq k}rij\log_{Z_{i}}\log Z_{j}$,
where $z_{i}=q^{n:}$and $x_{a}=q^{l_{a}}$’
with $l_{a}$’ the degree one term in $l_{a}$, and $\mathrm{L}\mathrm{i}_{2}(z)$is
Euler’s dilogarithm deﬁned by
$\mathrm{L}\mathrm{i}_{2}(z):=-\int_{0}^{z}\frac{\log(1-u)}{u}du$.
Next we consider the following system of partial diﬀerential equations:
(3.4) $\frac{\partial\tilde{V}(Z_{1},z_{2},\ldots Z_{k})}{\partial z_{i}},=0$$(i=1,2, . .. , k)$ .
Since
$\frac{\partial\tilde{V}(Z_{1},z_{2\cdots k}z)}{\partial z_{i}},,=\sum_{1a=}^{\alpha}\epsilon ali\frac{\log(1-X_{a})}{z_{i}}+\sum_{j1}^{k}ar=ij\frac{\log z_{j}}{z_{i}}+\gamma_{ii^{\frac{\log z_{i}}{z_{i}}}}$
with $\iota_{a}’=\sum_{i=1}^{k}\iota_{ai}Z_{i},$$(3.4)$implies the following algebraic equations.
(3.5) $z_{i^{r.:}} \prod_{1j=}z_{j}\prod_{a}kr_{i\mathrm{j}}=1\alpha(1-X_{a})\zeta a\iota a\iota=1$$(i=1,2,\ldots, k)$.
Let $(\zeta_{1}, \zeta_{2}, \ldots, \zeta_{k})$be a solution to (3.5).
72
Deﬁnition 3.1 (optimistic limit). We put
(3.6) $V(\zeta_{1}, \zeta_{2}, \ldots, \zeta_{k}):=\tilde{V}(\zeta_{1}, \zeta_{\sim}’),$$\ldots,$$\zeta_{k})+2\pi\sqrt{-1}(_{j=1}\sum^{k}cj\log\zeta j)$
and call it an optimistic limit of $\frac{2\pi\sqrt{-1}\log S(N)}{N}$as $N$goes to the inﬁnity. It is
denoted by $N arrow\infty 0-\lim\frac{2\pi\sqrt{-1}\log S(N)}{N}$. Here $c_{i}$is chosen so that $\frac{\partial\tilde{V}(\zeta 1\zeta_{2},\ldots,\zeta_{k})}{\partial z_{i}},+$
$2\pi\sqrt{-1}\sum_{j=1}^{k}\frac{c_{j}}{\zeta_{j}}=0$for every $i$.
Remark 3.2. The term $-\frac{\pi^{2}}{6}$in (3.3) appears so that $V(1,1,\ldots, 1)=0$since
$\mathrm{L}\mathrm{i}_{2}(1)=\frac{\pi^{2}}{6}$(see for example [6, (1.5)]). (I learned this from [11, \S 5].)
Remark 3.3. Note that $V$and $\tilde{V}$satisfy the same algebraic equations (3.5) but
diﬀerent partial diﬀerential equations (3.4) and that the extra terms in (3.6) are
necessary to choose an appropriate branch since $\mathrm{L}\mathrm{i}_{2}$and $\log$are multivalued func-
tions. (I learned this from T. Takata.)
Remark 3.4. An optimistic limit is not well deﬁned. There are many ambiguities
both in choosing $I(N)$(I did not say anything about the range of the summation
in $S(N)$and the contours in $I(N))$and in choosing $(\zeta_{1}, \zeta_{2}, \ldots, \zeta_{k})$.
Remark 3.5. Following Kashaev [2], the behavior of $S(N)$for large $N$may be
approximated by $P(N)I(N)$ with suitably chosen contours. Moreover by using
the saddle point method (see for example [7, \S 7.2])we see that $I(N)$(and $S(N)$)
behaves like $\exp(\frac{N}{2\pi\sqrt{-1}}\mathrm{o}-\lim\frac{2\pi\sqrt{-1}\log S(N)}{N}Narrow\infty)$for large $N$if we choose a solu-
tion $(\zeta_{1}, \zeta_{2}, \ldots, \zeta_{k})$suitably. Even if this is not true I expect that there is a relation
between an optimistic limit and the asymptotic behavior of $S(N)$.
