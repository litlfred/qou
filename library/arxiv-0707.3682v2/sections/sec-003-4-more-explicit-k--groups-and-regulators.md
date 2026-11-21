---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-003-4-more-explicit-k--groups-and-regulators
section_title: "More explicit K -groups and regulators"
section_number: 4
pages: 17-23
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.955
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
[]{#ksection label="ksection"}

In this section we first describe an inductive procedure that conjecturally gives $\Kn k$ ($n \ge 2$) for any number field $k$. It is originally due to Zagier [@Zag91], but we essentially give a reformulation by Deligne [@del:imd]. We also describe results concerning Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} when the action of $G$ on $E[G]\pi$ is Abelian.

In order to describe Zagier's conjecture we need the functions $$\label{Lindef}
\Li_n(z) = \sum_{k \geq 1} \frac{z^k}{k^n}
\qquad (n \geq 0)$$ for $z$ in $\C$ with $|z| < 1$ if $n = 0$ or 1, and $|z|\le1$ if $n \ge 2$. In particular, $\Li_1(z)$ is the main branch of $-\log(1-z)$. Using that $\dd \, \Li_{n+1}(z) = \Li_n(z) \, \dd \log(z)$ they extend to multi-valued analytic functions on $\C\setminus\{0,1\}$. By simultaneously continuing all $\Li_n$ along the same path one obtains single-valued functions on $\C\setminus\{0,1\}$ (see [@Zag91 § 7] or [@dJ95 Remark 5.2]) by putting $$\label{Pndef}
\Pn_n(z)  = \pi_{n-1}\biggl( \sum_{j=0}^{n-1} \frac{b_j}{j!} (2\log|z|)^j \Li_{n-j}(z) \biggr)
\quad\quad (n \ge 1) \,,$$ with $b_j$ the $j$-th Bernoulli number and $\pi_{n-1}$ the projection of $\C=\R(n-1)\oplus\R(n)$ onto $\R(n-1)$. These functions satisfy $\Pn_n(\bar z) = \overline{\Pn_n(z)}$ as well as $$\label{poleq}
\Pn_n(z) + (-1)^n \Pn_n (1/z) = 0$$ and $$\label{distrieq}
\Pn_n(z^m) = m^{n-1} \sum_{\z^m=1} \Pn_n(\z z)$$ when $m \ge 1$ and $z^m \ne 1$.

We can now describe the conjecture. Let $d=[k:\Q]$, and for $n \ge 2$ let $\tB_n(k)$ be a free Abelian group on generators $[x]_n^\sim$ with $x\ne 0,1$ in $k$. Define $$\begin{aligned}
{1}
\widetilde P_n : \tB_n(k) & \to \left(\R(n-1)^d\right)^+
\\
[x]_n^\sim & \mapsto (P_n(\s(x)))_{\s: k \to \C}
\,,
\end{aligned}$$ with $\left(\R(n-1)^d\right)^+ = \{ (a_\s)_\s \text{ in } \R(n-1)^d \text{ such that } a_{\bar\s} = \overline{a_\s} \}$. Then we define inductively, for $n \ge 2$, $$\begin{aligned}
{1}
\dd_n : \tB_n(k) & \to
 \left\{\begin{aligned}\bigwedge^2\lower 4pt\hbox{$ {}_\Z $} k^* \hbox to 30 pt{} & \text{ if $ n =2 $} \\ B_{n-1}(k) \tensor_\Z k^* & \text{ if $n>2$}\end{aligned} \right.
\\
\intertext{by}
[x]_n^\sim & \mapsto
   \left\{\begin{aligned}(1-x)\wedge x & \text{ if $ n =2 $} \\ [x]_{n-1} \tensor x & \text{ if $  n > 2 $\,,}\end{aligned} \right.
\end{aligned}$$ where $[x]_{n-1}$ denotes the class of $[x]_{n-1}^\sim$ in $B_{n-1}(k)$, which is defined as $$B_n(k) = \tB_n(k)/ \Ker(\dd_n) \cap \Ker(\widetilde P_n)
\,.$$ There are some universal relations, one of which is that $[x]_n + (-1)^n [1/x]_n = 0$, a consequence of [\[poleq\]](#poleq){reference-type="eqref" reference="poleq"}.

::: conjecture
[]{#zagierconjecture label="zagierconjecture"} If $n \ge 2$ then

1.  there is an injection $$\dfrac{\Ker(\dd_n)}{\Ker(\dd_n) \hskip-.5pt \cap \Ker(\widetilde P_n)} \to K_{2n-1}(k)_\Q$$ with image a finitely generated group of rank equal to $\dim_\Q (\Kn k )$;

2.  Beilinson's regulator map is given by $\widetilde P_n$: $$\xymatrix{
    \dfrac{\Ker(\dd_n)}{\Ker(\dd_n) \hskip-.5pt \cap \Ker(\widetilde P_n)} \ar[r]\ar[rd]_-{(n-1)!\widetilde P_n} & \Kn
    k \ar[d]^-{\prod_{\s: k \to \C} \reg_\infty\circ\s_*} \cr
      & \left(\R(n-1)^d\right)^+
    }$$ commutes.
:::

::: remark
For $n=2$ the corresponding results were already known before Zagier made his conjecture ([@bl00; @susXkof]; see also [@gon:goc § 2]).
:::

From the results in [@dJ95 § 5] one obtains the following.

::: theorem
[]{#zagierthm label="zagierthm"} Let $k$ be a number field and let $n \geq 2$ be an integer. Then there is an injection $$\Psi_n : \dfrac{\Ker(\dd_n)}{\Ker(\dd_n) \cap \Ker(\widetilde P_n)} \to \Kn k$$ with finitely generated image, such that the diagram in Conjecture [\[zagierconjecture\]](#zagierconjecture){reference-type="ref" reference="zagierconjecture"}(2) commutes.
:::

::: remark
The part of Zagier's conjecture that remains open is the question if the rank of the image of $\Psi_n$ equals $\dim_\Q(\Kn k )$. For a cyclotomic field $k$ this holds for any $n \geq 2$ as we shall recall in Example [\[cyclo\]](#cyclo){reference-type="ref" reference="cyclo"} below, but it is also known for arbitrary number fields for $n=2$, as mentioned above, or $n=3$ (see [@gonXpam § 3] and [@G3 Appendix]).
:::

::: remark
[]{#equivariance label="equivariance"} Although not stated explicitly in [@dJ95], it is clear from the construction there that the map $\Psi_n$ in Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} is natural in $k$. In particular, if $k/\Q$ is Galois then $\Gal(k/\Q)$ acts on $\Ker(\dd_n) /\Ker(\dd_n) \cap \Ker(\widetilde P_n)$ (through the obvious action on the generators $[x]_n^\sim$) as well as on $\Kn k$, and $\Psi_n$ is $\Gal(k/\Q)$-equivariant.
:::

::: example
[]{#cyclo label="cyclo"} If $k$ is a cyclotomic field then Zagier's conjecture is known in full. By Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} it suffices to see that the rank of the image of $\Psi_n$ equals $\dim_\Q \Kn k$. For an $N$-th root of unity $\z\neq1$, $N[\zeta]_n$ is in $\Ker(\dd_n) / \Ker(\dd_n) \cap \Ker(\widetilde P_n)$. If $k = \Q(\z)$ for a primitive $N$-th root of unity $\z$ with $N > 2$ then $\dim_\Q \Kn k = [k:\Q]/2$ for $n \geq 2$, and the $N [\z^j]_n$ with $1 < j < N/2$ and $\gcd(j,N)=1$ have $\R$-independent images under $\widetilde P_n$ [@Zag91 pp.420--422] so that they are $\Z$-independent in $\Ker(\dd_n) / \Ker(\dd_n) \cap \Ker(\widetilde P_n)$, and the same holds for their images under the injective map $\Psi_n$. For $k=\Q$ one can easily check directly from Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} and [\[Pndef\]](#Pndef){reference-type="eqref" reference="Pndef"} that for odd $n \geq 2$ the element $2 \Psi([-1]_n)$ is non-zero.
:::

For the regulator we need to describe the polylogarithms introduced in [@Col82]. We first make a choice of a branch of the logarithm. Recall that a homomorphism $\log_p: \OO_{\Cp}^*
\to \Cp$ is uniquely determined by the requirement that for $|x|_p<1$ it is given by the usual power series for $\log(1+x)$. To extend it to a homomorphism $\log_p: \Cp^* \to \Cp$ it suffices to make an arbitrary choice of $\log_p(p)$. Any such extension will be called a branch of the $p$-adic polylogarithm. In what follows we fix one such choice.

Coleman first produced the $p$-adic polylogarithm out of a more extensive theory of what is now called Coleman integration. For the $p$-adic polylogarithm it is, however, possible to give a more elementary and explicit theory. To do this, consider the class of functions $f: \Cp\setminus\{1\} \to \Cp$ that satisfy the following properties:

1.  for any $a\in \Cp$ with $|a-1|_p=1$ we have a power series expansion for $f(z)$ in $z-a$ that converges for $|z-a|_p<1$;

2.  for $0<|z-1|_p<1$ (resp. $|z|_p>1$) $f(z)$ is given by a polynomial in $\log_p(z-1)$ (resp. $\log_p(1/z)$) with coefficients that are Laurent series in $z-1$ (resp. $1/z$), convergent for $0<|z-1|_p<1$ (resp. $|z|_p>1$).

It is easy to see that differentiation sends this class surjectively onto itself. The $p$-adic polylogarithms are functions $\Li_{n,p}(z)$ ($n \ge 0$) in this class with the following properties:

1.  $\Li_{0,p}(z) = \frac{z}{1-z}$;

2.  $\Li_{n,p}(0) = 0$ for $n\ge 0$;

3.  $\dd \Li_{n+1,p}(z) = \Li_{n,p}(z) \frac{\dd  z}{z}$ for $n\ge 0$;

4.  for every $n \ge 0$ there is a power series $g_n(v)$, convergent for $|v|_p < p^{1/(p-1)}$, such that $g_n(1/(1-z)) = \Li_{n,p}(z)  - \frac{1}{p^n} \Li_{n,p}(z^p)$ when $|z-1|_p>  p^{-1/(p-1)}$.

Note that $1/z$ has a singularity at $0$ but $\Li_{n,p}(z) /z$ does not, because of the assumption that $\Li_{n,p}(0) = 0$. In fact, it is easy to see that $\Li_{n,p}(z)$ is given by the $p$-adically convergent power series [\[Lindef\]](#Lindef){reference-type="eqref" reference="Lindef"} for $|z|_p<1$.

In [@BdJ06] two of the authors of the present work described an efficient algorithm for the computation of $p$-adic polylogarithms up to a prescribed precision. This will be used in Section [\[examplesection\]](#examplesection){reference-type="ref" reference="examplesection"} to compute the regulator for $n \ge 2$ that we now proceed to describe in terms of suitable combinations of $\log_p^{n-m}(z) \Li_{m}(z)$.

By Proposition 6.4 and the correct version of Proposition 6.1 of [@Col82] the $\Li_{n,p}(z)$ for $n \ge 0$ and $z$ in $\Cp\setminus\{1\}$ satisfy $$\Li_{n,p}(z) + (-1)^n \Li_{n,p}(1/z) = -\frac{1}{n!} \log_p^n(z)$$ when $z \ne 0$, and $$\label{distrieqp}
\Li_{n,p}(z^m) = m^{n-1} \sum_{\z^m=1} \Li_{n,p}(\z z)$$ when $m \ge 1$ and $z^m \ne 1$.

For $z$ in $\Cp\setminus\{0,1\}$ and fixed $n \ge 2$, we define $$\label{Pnpdef}
\Lmod n (z) = \sum_{j=0}^{n-1} c_j \log_p^j(z) \Li_{n-j}(z)
\qquad (n \ge 2)$$ for any $c_j$ in $\Cp$ satisfying $c_0=1$ and $\sum_{j=0}^{n-1} c_j/(n-j)! =0$, so that $\Lmod n (z) + (-1)^n \Lmod n (1/z) = 0$. This is the case for $c_j=b_j$ with $b_j$ the $j$-th Bernoulli numbers as before, although the resulting formula is different from [\[Pndef\]](#Pndef){reference-type="eqref" reference="Pndef"}. Another possible natural candidate for the function $\Lmod n (z)$ is $L_n(z) + L_{n-1}(z) \log_p(z)/n$, where $$L_n(z) = \sum_{m=0}^{n-1} \frac{(-1)^m}{m!} \log_p^m(z) \Li_{n-m}(z)$$ (see [@BdJ03 (1.3) and Remark 1.5]).

The relations corresponding to [\[poleq\]](#poleq){reference-type="eqref" reference="poleq"} and  [\[distrieqp\]](#distrieqp){reference-type="eqref" reference="distrieqp"} for $\Lmod n (z)$ ($n\ge2$) are then $$\Lmod n (z) + (-1)^n \Lmod n (1/z) = 0$$ when $z\ne 0,1$, and $$\label{distrieqpLmod}
\Lmod n (z^m) = m^{n-1} \sum_{\z^m=1} \Lmod n (\z z)$$ when $m \ge 1$ and $z^m \ne 0,1$.

For any branch of the logarithm one then has the following result for the regulator map (see [@BdJ03 Theorem 1.10 or page 909]). Since its formulation depends on the embedding of $k$ we deal with one such embedding at a time.

::: theorem
[]{#synreg label="synreg"} Let $k$ be a number field, and let $F \subset \Qpbar$ be the topological closure of the Galois closure of any embedding $k \to \Qpbar$. For $\s : k \to F$ let $$B_n^\s(k) = \langle  [x]_n\,\, |\text{ $ \s(x) $, $ 1-\s(x) $ are in $ \OO_\Cp^* $}\rangle
\subseteq B_n(k) = \dfrac{\tB_n(k)}{\Ker(\dd_n) \hskip-.5pt \cap \Ker(\widetilde P_n)}
\,.$$ Then $$\begin{aligned}
{1}
\tB_n(k) & \to F \cr
[x]_n & \mapsto \Lmod n (\s(x))
\end{aligned}$$ induces a map $$\Lmod n ^\s : B_n^\s(k) \to F$$ and the solid arrows in $$\xymatrix{
B_n^\s(k) \cap {\Ker(\dd_n)} \,\, \ar@{^{(}->}[r]\ar[rrd]_-{(n-1)!\Lmod n ^\s}
&
\dfrac{\Ker(\dd_n)}{\Ker(\dd_n) \hskip-.5pt \cap \Ker(\widetilde P_n)} \ar[r]^-{\Psi_n}\ar@{.>}[rd]^-{\,\,(n-1)!\Lmod n ^\s}
&
\Kn k \ar[d]^-{\reg_p\circ\s_*}
\\
&
&
\,F
}$$ form a commutative diagram.
:::

::: remark
[]{#synregremark label="synregremark"} It was conjectured in [@BdJ03 Conjecture 1.14] that the dotted arrow exists and that the full diagram commutes. This is known to hold for $N [\z]_n$ if $\z$ is any $N$-th root of unity other than 1 (see Theorem 1.12 of loc. cit.).
:::

::: remark
The formulae for the complex and regulators involved in Theorems [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} and [\[synreg\]](#synreg){reference-type="ref" reference="synreg"} are stated up to sign in [@dJ95 Proposition 4.1] (with a normalizing factor) and [@BdJ03 Theorem 1.10(2) or Proposition 7.14] respectively, since they depend on the choice of $\Psi_n$, which is natural only up to sign. In the case it is clear from [@BdJ03 Proposition 7.10] that the sign is $(-1)^n$ if the ''relativity isomorphism'' in the case is normalized as in Proposition 5.7 of loc. cit. and the $K$-theoretic relativity isomorphism as in (3.1) of loc. cit. corresponds to this under the naturality of the regulator map. In order to see that the sign for the complex regulator is the same with the same choice of $\Psi_n$, we observe that one can use the techniques of [@BdJ03 Appendix A and Section 5] to describe the target for the complex regulator of $[z]_n$ with $z$ in $\C\setminus\{0,1\}$ in [@dJ95] by means of a complex with the same formal structure as in [@BdJ03 Definition 5.2], but using $\R(n-1)$-valued $C^\infty$-forms $\psi$ with logarithmic poles on copies of $(\mathbb{P}_\C^1\!\setminus\!\{1,z\})^j$ indexed by increasing functions $f : [1,\dots,j] \to [1,\dots,n-1]$. Using the maps $\psi \mapsto \int_{ (\mathbb{P}_\C^1)^j} \dd \arg(t_{f(1)}) \wedge \cdots \wedge \dd \arg(t_{f(j)}) \wedge \psi$ for a $j$-form $\psi$ with index $f : [1,\dots,j] \to [1,\dots,n-1]$, and suitable normalizing factors, one writes down an $\R$-linear map $\Pi_\infty$ on such forms, with values in $\R(n-1)$, that vanishes on exact forms and satisfies the analogous normalization condition as $\Pi=\Pi_p$ in [@BdJ03 Proposition 5.7]. Moreover, as in [@dJ95 Section 2.5] one sees that the subcomplex of forms on the component where $j=n-1$ that vanish if some $t_l = 0$ or $\infty$ gives a quasi-isomorphism under inclusion, and that the image of the regulator of $[z]_n$ is given by $\varepsilon_n(z)$ as in Section 4 of loc. cit. (up to sign since one has to use the correct formula for $\omega_n$, which can be obtained as in [@BdJ03 Section 6]). Using the computations on pages 236 and 237\] of [@dJ95] one then sees that $\Pi_\infty$ maps $\varepsilon_n(z)$ to $(-1)^n (n-1)! P_n^\flat (z)$, where $P_n^\flat(z) =  \pi_{n-1}\left( \sum_{l=0}^{n-1} \frac{1}{l!} (-\log|z|)^l \Li_{n-l}(z) \right)$, which induces the same map on $\Ker(\dd_n)/\Ker(\dd_n) \cap \Ker(\widetilde P_n)$ as $(-1)^n (n-1)! \, P_n(z)$. Since the relativity isomorphism in $K$-theory only depends on a choice of $t_l =0$ or $\infty$ for $l=1,\dots,n-1$ this shows that the signs in the formulae for the complex and regulators of $[z]_n$ match for the same choice of $\Psi_n$, and we adjust $\Psi_n$ so that those signs disappear.
:::

We conclude this section by considering Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} when the action of $G$ on $E[G]\pi$ is Abelian.

::: prop
[]{#abelprop label="abelprop"} Let $N \ge 2$, $k = \Q(\mu_N)$, $G = \Gal(k/\Q) = (\Z/N\Z)^*$ where $a$ in $(\Z/N\Z)^*$ corresponds to $\psi_a$ in $G$ satisfying $\psi_a(\z) = \z^a$ for all roots of unity $\z$ in $k$. Assume that $E$ contains a root of unity of order equal to the exponent of $G$ and let $\pi$ in $E[G]$ be the idempotent corresponding to an irreducible character $\chi$ of $G$. Then parts (1), (2) and (3) of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} hold for $\pi$ and $n \ge 2$ if $\chi(-1) = (-1)^{n-1}$.
:::

::: proof
*Proof.* That Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1) holds in this case is well-known (cf. [@Neu88]) but we make it explicit here for part (3) of the conjecture (cf. [@Gro94 Proposition 3.1]).

We deal with the case $N=2$ later so by Remark [\[sameconj\]](#sameconj){reference-type="ref" reference="sameconj"}(1) we may assume $N > 2$ and $\chi$ primitive. The idempotent $\pi$ corresponding to $\chi$ is $|G|^{-1} \sum_{a=1}^{\prime N} \chi^{-1}(a) \tensor \psi_a$, where the prime indicates that we sum over $a$ that are relatively prime to $N$.

Note that by our assumption on $\chi(-1)$ and Proposition [\[kerisreal\]](#kerisreal){reference-type="ref" reference="kerisreal"} the dimension of $K_{2n-1}(M_\pi^E)$ equals 1. Fixing a generator $\z$ of $\mu_N \subset k^*$ we use $\pi$, $\pi(1\tensor\z)$ and $\pi(1\tensor [\z]_n)$ as basis vectors of $E[G]\pi$, $M_\pi^E$ and $K_{2n-1}(M_\pi^E)$ respectively, where we simplify notation by writing $[\z]_n$ instead of $\Psi_n([\z]_n)$ as in Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"}.

In order to verify (1) in $E\tensor_\Q\C$ it suffices by Remark [\[newremark\]](#newremark){reference-type="ref" reference="newremark"}(2) to consider all embeddings $\s: E \to \C$. If $\eta=\phi_\infty(\z)$ with $\phi_\infty$ as in Section [\[motivicsection\]](#motivicsection){reference-type="ref" reference="motivicsection"} then the $\s$-component of $D(M_\pi^E)^{1/2,\infty}$ becomes $$D(M_\pi^E)^{1/2,\infty}_\s
=
|G|^{-1} \sum_{a=1}^N \raise7pt\hbox{$\prime$} \chi_\s^{-1}(a) \eta^a
=
N |G|^{-1} \left(\sum_{a=1}^N \raise7pt\hbox{$\prime$} \chi_\s(a) \eta^{-a} \right) ^{-1}$$ by [@Lan70 (3) on p.84]. Similarly, by Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"} the $\s$-component of $R_{n,\infty}(M_\pi^E)$ is $$R_{n,\infty}(M_\pi^E)_\s
=
(n-1)!\, |G|^{-1} \sum_{a=1}^N  \raise7pt\hbox{$\prime$} \chi_\s^{-1}(a) \Pn_n(\eta^a)
=
(n-1)! \, |G|^{-1} \sum_{a=1}^N  \raise7pt\hbox{$\prime$} \chi_\s^{-1}(a) \Li_n(\eta^a)$$ because $\Pn_n(\eta^a) = (\Li_n(\eta^a)+\chi_\s^{-1}(-1)\Li_n(\eta^{-a}))/2$ by our assumption on $\chi(-1)$, where $\Li_n$ is computed using the power series in [\[Lindef\]](#Lindef){reference-type="eqref" reference="Lindef"}. They relate to the $\s$-component of $\L n {\chi} {\Q}$ via $\L n {\chi_\s} {\Q} = (n-1)!^{-1} R_{n,\infty}(M_\pi^E)_\s / D(M_\pi^E)^{1/2,\infty}_\s$ according to (2) on page 172 of [@Col82] with the correct sign in the exponent of the Gauss sum as used here (cf. [@Zag91 p. 421]). Since $\L n {\chi_\s} {\Q} \ne 0$ this also shows that $\pi(1\tensor [\z]_n)$ gives a basis of $K_{2n-1}(M_\pi^E)$ as claimed.

Similarly, for (2) and (3) we consider all embeddings $\t : E \to  \Qpbar$. If $\phi_p(\z)=\eta_p$ then the $\t$-component of $D(M_\pi^E)^{1/2,p}$ is $N |G|^{-1} ( \sum_{a=1}^{\prime N} \chi_\t(a) \eta_p^{-a} )^{-1}$ and the $\t$-component of $R_{n,p}(M_\pi^E)$ equals $(n-1)! \, |G|^{-1} \sum_{a=1}^{\prime N} \chi_\t^{-1}(a) \Lmod n (\eta_p^a)$ by Remark [\[synregremark\]](#synregremark){reference-type="ref" reference="synregremark"}, independent of our assumption on $\chi(-1)$. By (3) on page 172 of [@Col82] we have $$\Lp p n {\chi_\t\omega_p^{1-n}} {\Q} =  (n-1)!^{-1} \Eul_p(k,\chi_\t,\Q) R_{n,p}(M_\pi^E)_\t / D(M_\pi^E)_\t^{1/2,p}
\,.$$ Therefore Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1)-(3) hold with $e(n,M_\pi^E) = e_p(n,M_\pi^E)$ in $\Q^* \subseteq E^*$.

Now assume that $N=2$ so that $\chi$ is the trivial character 1, $\pi = 1$ and $n \ge2$ is odd. Taking $1$, $1\tensor 1$ and $1 \tensor [-1]_n$ as bases of $E[G] = E$, $M_\pi^E = E \tensor \Q$ and $K_{2n-1}(\Q)_E$ we find from Theorem [\[zagierthm\]](#zagierthm){reference-type="ref" reference="zagierthm"}, [\[Lindef\]](#Lindef){reference-type="eqref" reference="Lindef"}, [\[Pndef\]](#Pndef){reference-type="eqref" reference="Pndef"} and [\[distrieq\]](#distrieq){reference-type="eqref" reference="distrieq"} that $$\L n 1 {\Q} = \z(n) = \frac{2^{n-1}}{1-2^{n-1}} P_n(-1) = \frac{2^{n-1}}{(n-1)!(1-2^{n-1})} R_{n,\infty}(M_1^E)
\,,$$ again proving that $[-1]_n$ gives a basis for $\Kn {\Q}$. Coleman proves that $$\Lp p n \omega_p^{1-n} {\Q} = (1-p^{-n}) \lim_{x \to 1}{}'\, \Li_{n,p}(x)$$ where the limit is taken in any subfield of $\Cp$ that is of finite ramification degree over $\Qp$. But by [\[Pnpdef\]](#Pnpdef){reference-type="eqref" reference="Pnpdef"} and [\[distrieqpLmod\]](#distrieqpLmod){reference-type="eqref" reference="distrieqpLmod"} we can rewrite this as $$\Lp p n \omega_p^{1-n} {\Q}
= \frac{ (1-p^{-n}) 2^{n-1}}{1-2^{n-1}} \Lmod n (-1)
= \frac{(1-p^{-n}) 2^{n-1}}{(n-1)! (1-2^{n-1})} R_{n,\infty}^p(M_1)
\,.$$ ◻
:::

::: remark
[]{#abelrem label="abelrem"} The $\pi$ in the proof of Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"} are primitive in the sense of Definition [\[mindef\]](#mindef){reference-type="ref" reference="mindef"}. So, by Remarks [\[consequencesremark\]](#consequencesremark){reference-type="ref" reference="consequencesremark"}(4) and [\[sameconj\]](#sameconj){reference-type="ref" reference="sameconj"}(1), if Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} applies to $\pi$ in $E[G]$, then parts (1), (2) and (3) of it hold for $\pi$ for any $E$ if the action on $E[G]\pi$ is Abelian. In particular, parts (1) and (2) of Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} hold for any totally real Abelian number field by Remark [\[consequencesremark\]](#consequencesremark){reference-type="ref" reference="consequencesremark"}.
:::

::: remark
[]{#dirichletcalculations label="dirichletcalculations"} Computer calculations show that $\Lp p n {\omega_p^{1-n}} {\Q}$ is in $\Q_p^*$ when $p=2,\dots,19$ and $n=2,\dots,20$ is odd, verifying Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"}(3) in those cases. Similarly, with notation and assumptions as in Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"}, for the 470 primitive characters $\chi$ of $\Gal(\Q(\m_N)/\Q) = (\Z/N\Z)^*$ with $2\le N \le 50$, $\Lp p n {\chi \tensor \omega_p^{1-n}} {\Q}$ lies in $(E\tensor \Qp)^*$ for those values of $p$ and $n=2,\dots,20$ whenever $\chi(-1) = (-1)^{n-1}$. Thus Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(4) also holds in those cases.
:::
