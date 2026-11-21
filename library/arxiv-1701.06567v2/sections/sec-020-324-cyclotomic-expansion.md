---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-020-324-cyclotomic-expansion
section_title: "Cyclotomic expansion"
section_number: 3.2.4
pages: 39-41
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
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
