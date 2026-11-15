---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-007-324-cyclotomic-expansion
section_title: "Cyclotomic expansion"
section_number: 3.2.4
pages: 39-47
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.991
---
[]{#sec:cyclotomic label="sec:cyclotomic"}

In this secition we show how to obtain expression for $\widehat{Z}_a(1/q,t)$ with $|q|<1$ using what is usually called the *cyclotomic expansion*.

Let us first consider the general construction. Let $F(q,t)$ be some function of $q$ and $t$, and suppose we know its restrictions at $t=q^\beta$, with $\beta\in{\mathbb Z}$, $$F^{(\beta)}(q)\equiv F(q,q^\beta).$$ Then, one can write the following formal cyclotomic-like expansion for $F(q,t)$: $$F(q,t)=\sum_{m=0}^\infty\widetilde{F}^{(m)}(q)\cdot\frac{t^m(1/t;q)_m}{(q;q)_m}.
    \label{cyclotomic}$$ The coefficient of the cyclotomic expansion, $\widetilde{F}^{(m)}(q)$, are related to ${F}^{(m)}(q)$ by a "triangular" linear transform: $$\begin{array}{rcl}
        \widetilde{F}^{(0)}(q) & = & F^{(0)}(q)\\
        \widetilde{F}^{(1)}(q) & = & F^{(0)}(q)-F^{(1)}(q)\\
        \widetilde{F}^{(2)}(q) & = & F^{(0)}(q)-(1+q^{-1})F^{(1)}(q)+q^{-1}F^{(2)}(q)\\
        \widetilde{F}^{(3)}(q) & = & F^{(0)}(q)-(1+q^{-1}+q^{-2})F^{(1)}(q)
        +(q^{-1}+q^{-2}+q^{-3})F^{(2)}(q)-q^{-4}F^{(3)}(q)\\
        \ldots
    \end{array}
    \label{Cyc-transform}$$ Note, that the denominators $(q;q)_m$ in ([\[cyclotomic\]](#cyclotomic){reference-type="ref" reference="cyclotomic"}) are introduced for convenience, so that $$F^{(\beta)}(q)\;\in{\mathbb Z}[q,q^{-1}]\qquad\Longleftrightarrow \qquad\widetilde{F}^{(m)}(q) \in{\mathbb Z}[q,q^{-1}]$$ but in principle they can be absorbed into the definition of cyclotomic coefficients $\widetilde{F}^{(m)}(q)$.

If the minimal degree of $q$ in $\widetilde{F}^{(m)}(q)$ grows with $m$, one can produce a $q$-expansion from the cyclotomic expansion ([\[cyclotomic\]](#cyclotomic){reference-type="ref" reference="cyclotomic"}). However, such procedure is quite formal and in general might not actually give the actual $q$-expansion that converges to $F(q,t)$ when $|q|<1$. But it can be done for homological blocks. In particular, from ([\[BlockBeta\]](#BlockBeta){reference-type="ref" reference="BlockBeta"}) one obtains the following cyclotomic-like expansion: $$\widehat{Z}_a(q,t)=\frac{1}{(qt;q)_\infty}\sum_{m=0}^\infty\widetilde{\widehat{Z}}_a^{(m)}(q)\cdot\frac{t^m(1/t;q)_m}{(q;q)_m}
    \label{Zcyclotomic}$$ where the coefficients $$\widetilde{\widehat{Z}}_a^{(m)}(q)\;\;\in{\mathbb Z}[q]$$ turn out to be polynomials in $q$ (non-Laurent) with minimal power growing linearly in $m$. Expanding each term in $q$ then gives us a $q$-series of the following form: $$\widehat{Z}_a(q,t)=\sum_{n= 0}^\infty P_n(t)q^n,\qquad P_n(t)\in {\mathbb Z}[t],
    \label{Block-qexp}$$ which coincides with the $q$-series that can be produced directly from ([\[TM3mod\]](#TM3mod){reference-type="ref" reference="TM3mod"}). On the other hand, since $P_m(t)$ contain only positive powers of $t$, one can produce $\widehat{Z}^{(\beta)}(q)$ --- or, equivalently, the coefficients of the cyclotomic expansion $\widetilde{\widehat{Z}}^{(\beta)}(q)$ --- from ([\[TM3mod\]](#TM3mod){reference-type="ref" reference="TM3mod"}) just by making the substitution $t=q^\beta$ and observing that the resulting $q$-series truncates.

Therefore, we assume that for anti-blocks one can write similarly: $$\widehat{Z}_a(1/q,t)=(1/t;q)_\infty\sum_{m=0}^\infty\widetilde{\widehat{Z}}_a^{(-m)}(1/q)\cdot\frac{t^m(1/t;q)_m}{(q;q)_m}
    \label{AZcyclotomic}$$ where $\widetilde{\widehat{Z}}_a^{(-m)}(1/q)$ are related to ${\widehat{Z}}_a^{(-\beta)}(1/q)\equiv (q^{-1}t;q^{-1})_\infty\widehat{Z}_a(q^{-1},t)|_{t=q^\beta}$ in the same way as $\widetilde{F}^{(m)}(q)$ are related to $F^{(\beta)}(q)$ in ([\[Cyc-transform\]](#Cyc-transform){reference-type="ref" reference="Cyc-transform"}).

For example, in the case $p=5$, using expressions for $\widehat{Z}_a^{(-\beta)}(q)$ calculated in Section [\[sec:beta-reduction\]](#sec:beta-reduction){reference-type="ref" reference="sec:beta-reduction"} we have $$\begin{array}{rl}
        2\widehat{Z}_0(1/q,t)=&\left(-t^3+t^2-t+1\right)+\left(t^4-3 t^3+5 t^2-3 t\right)
   q+\left(-t^5+6 t^4-11 t^3+11 t^2-6 t+1\right) q^2\\ &\qquad+\left(t^6-6
   t^5+17 t^4-28 t^3+26 t^2-12 t+2\right)
   q^3+O\left(q^4\right),\vspace{1ex}
   \\
        \widehat{Z}_1(1/q,t)=&q^{-1/5}\Big(\left(t^2-t\right)+\left(t^4-3 t^3+3
   t^2-2 t+1\right) q+\left(-t^5+4 t^4-9 t^3+10 t^2-5 t+1\right)
   q^2 \\& \qquad+\left(-4 t^5+15 t^4-24 t^3+21 t^2-10 t+2\right)
   q^3+O\left(q^{4}\right)\Big),\vspace{1ex}
   \\
        \widehat{Z}_2(1/q,t)=&q^{1/5}\Big(\left(-t^3+2 t^2-t\right)+\left(2
   t^4-5 t^3+5 t^2-3 t+1\right) q+ \\& \qquad+\left(-2 t^5+7 t^4-13 t^3+14
   t^2-7 t+1\right) q^2+O\left(q^3\right)\Big).
    \end{array}$$ Now we can check ([\[Index-factorization\]](#Index-factorization){reference-type="ref" reference="Index-factorization"}) and ([\[Itop-factorization\]](#Itop-factorization){reference-type="ref" reference="Itop-factorization"}) directly. From ([\[I-Lp1-SU2\]](#I-Lp1-SU2){reference-type="ref" reference="I-Lp1-SU2"}), or equivalently from ([\[Zcyclotomic\]](#Zcyclotomic){reference-type="ref" reference="Zcyclotomic"}), we have $$\begin{array}{rl}
        \widehat{Z}_0(q,t)&=1+q+(2-t+t^2)q^2+(3-2t+2t^2)q^3+O(q^4),\vspace{1ex}\\
        \widehat{Z}_1(q,t)&=q^{1/5}\left(-1+(-2+t)q+(-3+2t-2t^2)q^2+(-5+4t-3t^2+t^3)q^3+O(q^4)\right),\vspace{1ex}\\
        \widehat{Z}_2(q,t)&=q^{4/5}\left((1-t)q+(1-2t+t^2)q^2+O(q^3)\right).
    \end{array}$$ And from ([\[I-Lp1-SU2\]](#I-Lp1-SU2){reference-type="ref" reference="I-Lp1-SU2"}) we have: $$\begin{gathered}
    {\mathcal I}(q,t)=\left(1-\frac{1}{t^3}\right)+\left(-1+\frac{1}{t}+\frac{1}{t^2}-\frac{1}{t^3}\right)
   q+\left(t^2-2+\frac{1}{t}-\frac{1}{t^3}+\frac{1}{t^4}\right)
   q^2+\\+\left(\frac{1}{t}-\frac{1}{t^2}-\frac{1}{t^5}+\frac{1}{t^6}
   \right) q^3+O\left(q^4\right).
\end{gathered}$$ Then, one can check explicitly that indeed $${\mathcal I}(q,t) \; = \; \widehat{Z}_0(q,t)\cdot 2\widehat{Z}_0(1/q,1/t)+
    \widehat{Z}_1(q,t)\widehat{Z}_1(1/q,1/t)+
    \widehat{Z}_2(q,t)\widehat{Z}_2(1/q,1/t) \,.$$ Similarly, the topologically twisted index, $${\mathcal I}_\text{top}(q,t) \; = \; 1-t^3 \,,$$ can indeed be decomposed as $${\mathcal I}_\text{top}(q,t) \; = \; \widehat{Z}_0(q,t)\cdot 2\widehat{Z}_0(1/q,t)+
    \widehat{Z}_1(q,t)\widehat{Z}_1(1/q,t)+
    \widehat{Z}_2(q,t)\widehat{Z}_2(1/q,t) \,.$$

### Positivity of coefficients

In [@Gukov:2016gkn], it was shown that, up to an overall $\pm$ sign, the refined homological blocks (with or without contribution from the Cartan component of the adjoint chiral) have the following positivity property: $$\begin{aligned}\label{block-pos}
\pm \widehat{Z}_a(q,-t) \quad & \in \quad q^{\Delta_a} {\mathbb Z}_+[t][[q]] \\
\pm (-qt;q)_\infty\widehat{Z}_a(q,-t) \quad & \in \quad q^{\Delta_a} {\mathbb Z}_+[t][[q]]
\end{aligned}$$

so that it is naturally to conjecture that $\pm \widehat{Z}_a(q,-t)$ actually coincides with the Poincaré polynomial of the underlying doubly graded homology (after a shift in overall degrees), $${\mathcal H}_a[M_3] \; = \; \bigoplus_{i\in {\mathbb Z}+\Delta_a\atop j\in {\mathbb Z}} {\mathcal H}_a^{i,j}.$$ This is equivalent to the statement that the triply graded homology (refined by the flavor charge) is supported only on the "diagonal" $${\mathcal H}_a^{i,j;\ell}=\delta_{j,\ell}{\mathcal H}_a^{i,j}.$$ Since we have advertised that the superconformal/twisted index and their categorifications are "better-behaved," one may ask whether they have a similar positivity property. The answer is affirmative.

#### Superconformal index.

In contrast to the homological blocks, the coefficients of ${\mathcal I}(q,t)$ are not all positive/negative and there does not seem to be an easy change of variables which achieves that (contrary to what happend for $\widehat{Z}_a(q,t)$, see [@Gukov:2016gkn]). However, there seem to be an easy factor which makes them positive. In particular, in the case of $G=SU(2)$ and $p>1$, one observes that $${\mathcal I}_{T[L(p,1),SU(2)]}(q,t) \; = \; P(q,t) \cdot (t^{-1};q)_\infty\,\cdot (1-qt)$$ where $$P(q,t) \; \in \; {\mathbb Z}_+[t][[q]] \,$$ is a positive power series. So, naively one can expect that the spectrum of BPS operators of $T[L(p,1),SU(2)]$ is given by cohomology $$\label{PositiveFactor}
    {\mathcal H}_\text{BPS} \; = \; H^*( {\mathcal H}_{P} \otimes {\mathcal H}_\text{Fermi} , d)$$ for some differential $d$, where ${\mathcal H}_P$ categorifies $P(q,t)$ and ${\mathcal H}_\text{Fermi}$ is the space generated by a tower of fermions with the index $(t^{-1};q)_\infty$ and one single fermions with index $(1-tq)$. And one would expect the tower is related to $\overline{\psi}^3_+$, the Cartan component of $\overline{\psi}_+$ in the (anti-)chiral multiplet, and its derivatives.

#### Twisted index.

The twisted index also shares this positivity property, which can be understood in greater depth. For $T[L(p,1);G]$ with large $p$, we know from the discussion in section [\[sec:TopInd\]](#sec:TopInd){reference-type="ref" reference="sec:TopInd"} that $${\mathcal H}_\text{tw-BPS}^\bullet=H^\bullet(G)=(\Lambda^\bullet \mathfrak{g})^G.$$ Then the equivariant Euler characteristics will factorizes into a positive part times a simple factor, $$\label{TopIndPos}
{\mathcal I}_{\text{top}}=\prod_i^{\mathrm{rk}\,G}(1-t^{2m_i+1})=(1-t)^{\mathrm{rk}\,G}\cdot \prod_i^{\mathrm{rk}\,G}(1+t+\ldots +t^{2m_i}),$$ where $m_i$ are exponents of the group $G$. At the level of homological invariants, one may be tempted to factor out the exterior algebra of the Cartan subalgebra $\mathfrak{t}\subset\mathfrak{g}$ $$(\Lambda \mathfrak{g})^G\sim\Lambda \mathfrak{t} \cdot (\Lambda \mathfrak{g})^G/\Lambda \mathfrak{t}.$$ However, the last quotient doesn't make sense as $\Lambda \mathfrak{t}$ is not a submodule of $(\Lambda \mathfrak{g})^G$ --- this parallels the discussion for the superconformal index where the gauge-non-invariant operator $\overline{\psi}^3_+$ plays the role of $\mathfrak{t}$ here. Instead, one has to consider the Leray spectral sequence $$E_2^{\bullet,\bullet}=H^{\bullet}(G/T,H^\bullet(T)) \Rightarrow H^\bullet(G)$$ associated with the fibration $$T\rightarrow G\rightarrow G/T.$$ The $E_2$ page factorizes as $$H^\bullet(T)\otimes H^{\bullet}(G/T)$$ where $H^\bullet(T)$ is fermionic (generated by elements in $H^1(T)$) while $H^{\bullet}(G/T)$ is bosonic (with only even-degree cohomology groups). But the differentials in the spectral sequence are no longer trivial. And this is the reason that we expect [\[PositiveFactor\]](#PositiveFactor){reference-type="eqref" reference="PositiveFactor"} as opposed to a direct factorization of ${\mathcal H}_{\text{BPS}}$.

#### A summary.

Up to now, we have encountered several positivity-related phenomena, similar but each with its own flavor, and it may be worthwhile to summarize and compare.

1.  Positivity of homological blocks $\widehat{Z}_a$. Besides overall signs, all homological blocks are positive in variables $q$ and $-t$. This is likely due to "homological-flavor locking" --- the homological degree is not independent from the flavor degree and one completely determines the other, *cf.* [@Gukov:2016gkn sec.3.4]. We have already illustrated how this happens for $T[S^3]$ in section [\[sec:S3\]](#sec:S3){reference-type="ref" reference="sec:S3"}, and expect this to be a general phenomena. In fact, such behavior was already observed for homological invariants of knot [@Aganagic:2011sg; @Gorsky:2013jxa; @Cherednik:2011nr].

2.  Positivity of the superconformal index ${\mathcal I}$ and twisted index ${\mathcal I}_{\text{top}}$. After factorizing out a "fermionic factor," all coefficients appearing in the two indices will be positive. This may seems to be qualitatively different from 1, where we have positivity in $(q,-t)$-variable as opposed to $(q,t)$. However, the example of ${\mathcal I}_\text{top}(T[L(p,1)])$ with large $p$ suggests that 1 and 2 are intimately related. Namely, from [\[TopIndPos\]](#TopIndPos){reference-type="eqref" reference="TopIndPos"}, the twisted index in this case is $${\mathcal I}_{\text{top}}=P_{-t}(G)=\prod_i^{\mathrm{rk}\,G}(1-t^{2m_i+1})=(1-t)^{\mathrm{rk}\,G}\cdot (\text{positive polynomial}),$$ where one sees that the third quantity is positive in $-t$ via "homological-flavor locking", while removal of a factor will achieve strict positivity in the fourth quantity.

3.  Positivity of "$\beta$-reduced" homological blocks $\widehat{Z}^{(\beta)}_a$ and indices ${\mathcal I}^{(\beta)}$, ${\mathcal I}^{(\beta)}_{\text{top}}$. For ${\mathcal I}^{(\beta)}$ and ${\mathcal I}^{(\beta)}_{\text{top}}$, their positivity directly follows from 2 by setting $t=q^\beta$. On the other hand, positivity for $\widehat{Z}^{(\beta)}_a$ is not *a priori* obvious and require non-trivial cancellations that also involve the $q$-degree. This hints at the non-trivial role played by the $q$-grading in the "homological-flavor locking."

### Comparison with refined CS {#sec:refCS}

Let $R_n$ denote by a representation of $SU(2)$ of dimension $n$. The Hilbert space of the refined Chern-Simons theory [@Aganagic:2011sg] on $T^2$ is the same as in the unrefined case. Namely, it is generated by integral representations of the affine Kac-Moody algebra at "bare" level $k-2$, which in our notations[^1] have $n = 1,\ldots,k-1$: $${\mathcal H}_{T^2}=\bigoplus_{n=1}^{k-1} {\mathbb C}|R_n\rangle.$$ Let $$q=e^{\frac{2\pi i}{k+2\beta}},\quad\text{and} \quad t=q^\beta.$$ The $T$ and $S$ matrices read (up to simple $q,t$-independent phase factors) $$T_{nm}\equiv \langle R_n |T|R_m\rangle=
    \delta_{nm}\cdot q^{\frac{n^2}{4}}t^{\frac{n}{2}+\frac{\beta}{4}}$$ $$S_{nm}\equiv \langle R_n |S|R_m\rangle=d_{R_n}(t)M_{R_m}(tq^n)$$ where the refined quantum dimension $d_{R_n}$ is given by $$d_{R_n}(tq)=\frac{1}{(2k+4\beta)^{1/2}}
        \prod_{m=0}^{\beta} (q^{-(m+1)/2}t^{-1/2}-q^{(m+1)/2}t^{1/2})M_{R_n}(tq)$$ and the $SU(2)$ Macdonald polynomials are given by[^2] $$M_{R_n}(x)=\sum_{j=0}^{n-1}x^{j-n/2+1/2}
    \prod_{i=1}^j\frac{[n-i]_q[i+\beta]_q}{[n-i+\beta]_q[i]_q},$$ which at the special value of the argument simplifies to $$M_{R_n}(tq)=\prod_{m=0}^\beta
    \frac{q^{-(m+n)/2}t^{-1/2}-q^{(m+n)/2}t^{1/2}}{q^{-(m+1)/2}t^{-1/2}-q^{(m+1)/2}t^{1/2}}.$$ The scalar product on ${\mathcal H}_{T^2}$ is given by $$\langle R_n|R_m\rangle = g_n \delta_{nm},$$ $$g_n=\prod_{m=0}^\beta\frac{q^{-(n+m)/2}t^{-1/2}-q^{(n+m)/2}t^{1/2}}{q^{-(n-m)/2}t^{-1/2}-q^{(n-m)/2}t^{1/2}}.$$ The refined CS partition function on $M_3=L(p,1)$ is then given by $$\begin{gathered}
    Z_{SU(2)}^\text{ref. CS}[L(p,1)]=\sum_{n=1}^{k-1} g^{-1}_n\,(S_{1n})^2(T_{nn})^{-p}\\
    =(2k+4\beta)^{-1}
    \sum_{n=1}^{k-1}q^{-\frac{pn^2}{4}-\frac{pn\beta}{2}-\frac{p\beta^2}{4}}
    \prod_{j=0}^\beta (q^{-\frac{n+j+\beta}{2}}-q^{\frac{n+j+\beta}{2}})
    (q^{-\frac{n-j+\beta}{2}}-q^{\frac{n-j+\beta}{2}}).
\end{gathered}$$ Changing the summation variable from $n$ to $m=n+\beta$ gives $$\begin{gathered}
    (2k+4\beta)\,Z_{SU(2)}^\text{ref. CS}[L(p,1)]=
    \sum_{m=\beta+1}^{k+\beta-1}q^{-\frac{pm^2}{4}}
    \prod_{j=0}^\beta (q^{-\frac{m+j}{2}}-q^{\frac{m+j}{2}})
    (q^{-\frac{m-j}{2}}-q^{\frac{m-j}{2}})\\
    =\frac{(-1)^\beta q^{-\frac{\beta(\beta+1)}{2}} }{2}
    \sum_{m\in {\mathbb Z}_{2(k+2\beta)}}q^{-\frac{pm^2}{4}}\prod_{j=0}^\beta (1-q^{j+m})(1-q^{j-m}),
    \label{ref-Lp1-1}
\end{gathered}$$ where we have extended the range of summation using the parity and vanishing properties of the summand. Using the Gauss sum reciprocity formula (which is a particular case of ([\[reciprocity\]](#reciprocity){reference-type="ref" reference="reciprocity"})) $$\sum_{m\in {\mathbb Z}_{2(k+2\beta)}}q^{-\frac{pm^2}{4}}\cdot q^{\frac{n\ell}{2}}=
    \frac{e^{-\frac{\pi i}{4}}(2k+4\beta)^{1/2}}{|p|^{1/2}}
    \sum_{a\in {\mathbb Z}_p} e^{2\pi i (k+2\beta)\frac{a^2}{p}}\cdot
    e^{2\pi i \frac{a\ell}{p}}\cdot
    q^{\frac{\ell^2}{4p}},$$ we can rewrite ([\[ref-Lp1-1\]](#ref-Lp1-1){reference-type="ref" reference="ref-Lp1-1"}) as follows: $$\begin{gathered}
    (2k+4\beta)^{1/2}\,Z_{SU(2)}^\text{ref. CS}[L(p,1)]=\\
    =t^{-\frac{\beta+1}{2}}\sum_{a,b\in {\mathbb Z}_p /{\mathbb Z}_2} e^{2\pi i (k+2\beta)\text{CS}(a)}\cdot
    S_{ab}\cdot \frac{1}{|{\mathcal W}_b|}\,{\mathcal L}_{b}^{(p)}\left[\prod_{j=0}^\beta (1-q^{j}z^2)(1-q^{j}z^{-2})\right],
\end{gathered}$$ where, again, we drop the overall phase factor and $\text{CS}(a)$ is the CS invariant of a flat connection $a$. As before, the $S$-transform is given by[^3] $$S_{ab}=\frac{e^{2\pi i\frac{ab}{p}}+e^{-2\pi i\frac{ab}{p}}}{|{\mathcal W}_a|}
    \label{SZp}$$ and ${\mathcal L}_{b}^{(p)}$ is the "Laplace transform": $$\begin{array}{cccc}
    {\mathcal L}_{b}^{(p)}:& {\mathbb Z}[q]\otimes {\mathbb Z}[z^2,z^{-2}]&\longrightarrow & q^{\frac{b^2}{p}}{\mathbb Z}[q],
    \vspace{2ex}
    \\
    & z^{2\ell}&\longmapsto &
    \left\{\begin{array}{cl} q^{\ell^2/p}, & \ell=b \mod p, \\ 0, & \text{otherwise.}  \end{array}\right.
    \end{array}
    \label{LaplaceZp}$$ Equivalently, it can be realized as follows: $${\mathcal L}_{b}^{(p)}:\qquad f(z) \longmapsto
    \int\frac{dz}{2\pi i z}\,
    f(z^{-1})\,\sum_{n\in p{\mathbb Z}+b}q^{n^2/p}\,z^{2n}.$$ Therefore we have $$(2k+4\beta)^{1/2}\,Z_{SU(2)}^\text{ref. CS}[L(p,1)]
    =t^{-\frac{\beta+1}{2}}\sum_{a,b\in {\mathbb Z}_p /{\mathbb Z}_2} e^{2\pi i (k+2\beta)\text{CS}(a)}\cdot
    S_{ab}\cdot \widehat{Z}_b^{(\beta)}(q)
    \label{ref-WRT-decomp}$$ where $\widehat{Z}^{(\beta)}_b(q)$ are the same as homological blocks ([\[BlockBeta1\]](#BlockBeta1){reference-type="ref" reference="BlockBeta1"}) obtained as the $D^2\times_q S^1$ partition function of $T[L(p,1),SU(2)]$, $$\widehat{Z}^{(\beta)}_b(q)=
    \frac{1}{|{\mathcal W}_b|}\left.\int\frac{dz}{2\pi i z}\,
    \frac{(z^2;q)_\infty(z^{-2};q)_\infty}{(z^2tq;q)_\infty(z^{-2}tq;q)_\infty}\,\sum_{n\in p{\mathbb Z}+b}q^{n^2/p}\,z^{2n}\right|_{t=q^\beta}.$$ Therefore, we just showed that ([\[ref-WRT-decomp\]](#ref-WRT-decomp){reference-type="ref" reference="ref-WRT-decomp"}) can be understood as a refined version of the decomposition ([\[WRT-decomposition\]](#WRT-decomposition){reference-type="ref" reference="WRT-decomposition"}) of the WRT invariant into homological blocks $\widehat{Z}_a(q)$.

## ${M_3=O(-p)\rightarrow \Sigma_g}$

Now, we consider a class of three-manifolds $M_3$ that could be viewed as a natural generalization of $L(p,1)$ --- the total space of a degree-$(-p)$ circle bundle over a genus-$g$ Riemann surface. We expect the 3d ${\mathcal N}=2$ theory $T[M_3,SU(2)]$ to have the following Lagrangian description: $$T[M_3] \quad = \quad
    \boxed{\begin{array}{c}
    {\mathcal N}=2 \text{ level-$p$ Chern-Simons term }\\
    +~\text{adjoint chiral $\Sigma$ with R-charge 2 }\\
    +~\text{$2g$ adjoint chirals $(\Phi_i,\widetilde{\Phi}_i)_{i=1}^g$ with R-charge 0}.
    \end{array}}
    \label{TCircFib}$$ When $p=0$, the theory has ${\mathcal N}=4$ supersymmetry and coincides with the mirror description of the 3d reduction of $T[\Sigma_g]$ [@Benini:2010uu]. Having $p\neq 0$ results in $p$ units of RR 2-form flux after reducing the M5-branes first on the circle fiber, which then give rise to a level-$p$ Chern-Simons term via D4-brane world-volume couplings to RR fields. The assignment of R-symmetry charges is consistent with the cubic superpotential coupling ${\rm Tr}\,\widetilde{\Phi_i}\Sigma\Phi_i$ and reproduces the the correct R-charge assignment for the Lens space theory $T[L(p,1)]$ when $g=0$.

When $p=0$, the theory $T[M_3]$, considered as an ${\mathcal N}=2$ theory has $U(1)_{\beta}\times USp(2g)$ symmetry [@Benini:2010uu], where $USp(2g)$ rotates $2g$ adjoint chirals and $U(1)_{\beta}$ is the anti-diagonal of $SU(2)\times SU(2)$ R-symmetry, with respect to which the fields $\Phi_i$, $\widetilde{\Phi}_i$ and $\Sigma$ have charges $-1$, 0 and 1 respectively.[^4] When $p\neq 0$, the CS interaction does not break these symmetries, but the $U(1)_{t'}$ R-symmetry of the ${\mathcal N}=4$ theory with $p=0$ will become the flavor symmetry $U(1)_\beta$ of the ${\mathcal N}=2$ theory with $p\neq 0$. For our purposes, it is more convenient to consider instead $U(1)_{\beta}\times U(g)$ maximal rank subgroup with the following charge assignments: $$\begin{array}{c|cc}
         & U(1)_{\beta} & U(g) \\
        \hline
        \Sigma & 1 & \mathbf{1} \\
        \Phi_i & -1 & \mathbf{\overline g} \\
        \widetilde\Phi_i & 0 & \mathbf{g}
    \end{array}\,$$

[^1]: Our notations slightly differ from those in [@Aganagic:2011sg]: $$\begin{array}{c}
            k_\text{here} \; = \; k_\text{AS}+2, \\
            \beta_\text{here} \; = \; \beta_\text{AS}-1, \\
            t_\text{here} \; = \; t_\text{AS}/q.
        \end{array}$$

[^2]: As usual, $q$-numbers are defined as $$_q \equiv \frac{q^{n/2}-q^{-n/2}}{q^{1/2}-q^{-1/2}}.$$

[^3]: Notice, that this $S$-transform matrix is different from the $S$-matrix in refined Chern-Simons theory!

[^4]: This is because $\Phi_i$ and $\widetilde{\Phi}_i$ are combined into an ${\mathcal N}=4$ *twisted* hypermultiplet [@Benini:2010uu] and transform under the $SU(2)\times SU(2)$ in the same way as a vector multiplet. As a consequence, $U(1)_{\beta}$ only acts on $\Phi_i$, not $\widetilde{\Phi}_i$.
