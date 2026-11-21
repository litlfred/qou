---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-006-cancellation-of-singularities
section_title: "Cancellation of singularities"
section_number: null
pages: 12-14
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.897
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: cancellation label="sec: cancellation"} Again, we hide the explicit dependence on the classical solution $\alpha$ to simplify the notation. Here and in the rest of this work, we will only re-introduce it when necessary.

Recall that the exact wave function $\chi(u;\hbar)$ is well-defined for $\hbar>0$. In particular, it is well-defined for

$$\label{rathbar}
\hbar = 2 \pi {P \over Q} \, ,$$

where $P, Q$ are coprime positive integers. We will refer to values of $\hbar$ of the form in Eq. [\[rathbar\]](#rathbar){reference-type="eqref" reference="rathbar"} as *rational values*. On the other hand, due to the conjectured integrality structure in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"}, $\phi^{\rm WKB} (X; q)$ is singular for these values of $\hbar$ precisely, thus implying that the singularities have to cancel in the sum

$$\label{phi-sum}
\phi^{\rm WKB} (X; q) +\phi^{\rm WKB} (X_D; q_D) \, ,$$

which appears in the formula for $\chi(u;\hbar)$ in Eq. [\[exactconj\]](#exactconj){reference-type="eqref" reference="exactconj"}. This leads to non-trivial constraints on the coefficients $\hat a_{\pm n}(q)$ in Eq. [\[ahatf-def\]](#ahatf-def){reference-type="eqref" reference="ahatf-def"}. This type of cancellation of singularities played a major role in the understanding of the ABJM matrix model [@hmo2] and the TS/ST correspondence [@km; @ghm; @wzh].

We will now study how this cancellation occurs in the exact wave function $\chi(u;\hbar)$ as given in Eq. [\[exactconj\]](#exactconj){reference-type="eqref" reference="exactconj"}, and, in Section [\[sec: rational1\]](#sec: rational1){reference-type="ref" reference="sec: rational1"}, we will compute the finite, well-defined piece which is left from the cancellation and constitutes the sum in Eq. [\[phi-sum\]](#phi-sum){reference-type="eqref" reference="phi-sum"}. Moreover, as we will see following [@szabolcs] in Section [\[sec: rational3\]](#sec: rational3){reference-type="ref" reference="sec: rational3"}, it is possible to compute this finite part by using only the information contained in the quantum operator $\hat{A}(\hat{P}, \hat{X},q)$. We take $$q={\rm e}^{{\rm i}\hbar}={\rm e}^{2 \pi {\rm i}{P \over Q}} \, , \quad  P,Q \in {\mathbb Z}_{>0} \; \; \text{coprime} \, ,$$ and, substituting into Eq. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"}, we find that the possible singularities of $\phi^{\rm WKB} (X; q)$ occur in $a_{\pm n}(q)$ when $n=s Q$ and $s \in {\mathbb Z}_{>0}$. For these values of $n$, the coefficient functions $a_{\pm n}(q)$ in Eq. [\[ahatf-def\]](#ahatf-def){reference-type="eqref" reference="ahatf-def"} become $$\label{ahatsQ}
a_{\pm s Q}\left(q \right) = \frac{\hat{a}_{ \pm sQ}\left( q \right)}{sQ (q^{sQ}-1) q^{ \sigma_{\pm sQ}}} \, .$$ Similarly, considering the dual variable $$q_D={\rm e}^{{4 \pi^2 \over \hbar}}={\rm e}^{2 \pi {\rm i}{Q \over P}} \, ,$$ the possible singularities of the dual function $\phi_{\rm WKB} (X_D; q_D)$ occur in $a_{\pm n} (q_D)$ when $n=s P$ and $s \in {\mathbb Z}_{>0}$. Indeed, the coefficient functions $a_{\pm n}(q_D)$ in Eq. [\[ahatf-def\]](#ahatf-def){reference-type="eqref" reference="ahatf-def"} become $$\label{ahatsP}
a_{\pm s P}\left( q_D\right) = \frac{\hat{a}_{\pm sP}\left( q_D \right)}{sP (q_D^{sP}-1) q_D^{ \sigma_{\pm sP}}}  \, .$$

Let us now introduce $$\label{hbareps}
q_{\epsilon}= {\rm e}^{{\rm i}\hbar_{\epsilon}} \, , \quad q_{\epsilon, D}= {\rm e}^{{ 4 \pi^2 {\rm i}\over  \hbar_{\epsilon}}} \, , \quad \hbar_{\epsilon}=  2 \pi {P \over Q}+ \epsilon \, , \quad 0 < \epsilon\ll 1 \, ,$$ and consider the limit $\epsilon\rightarrow 0$. As detailed in Appendix [\[app: eps\]](#app: eps){reference-type="ref" reference="app: eps"}, Eqs. [\[ahatsQ\]](#ahatsQ){reference-type="eqref" reference="ahatsQ"}, [\[ahatsP\]](#ahatsP){reference-type="eqref" reference="ahatsP"} produce the NLO $\epsilon$-expansions $$\begin{align}
a_{\pm s Q}\left( q_{\epsilon} \right) &= \left(- \frac{{\rm i}}{(sQ)^2 \epsilon} -\frac{1}{2sQ} + \frac{1}{(sQ)^2} q \frac{\partial}{\partial q} \right) \frac{ \hat{a}_{\pm sQ}(q) }{q^{\sigma_{\pm sQ}}} + {\cal O}(\epsilon) \, , \label{pole} \\
a_{\pm s P}\left( q_{\epsilon, D} \right) &= \left( \frac{{\rm i}}{(sQ)^2 \epsilon} +\frac{1}{sP}\left(\frac{{\rm i}}{2 \pi sQ}- {1 \over 2} \right) + \frac{1}{(sP)^2} q_D \frac{\partial}{\partial q_D} \right) \frac{ \hat{a}_{\pm sP}(q_D)}{q_D^{\sigma_{\pm sP}}}  + {\cal O}(\epsilon) \, . \label{poleD}
\end{align}$$ We then require the cancellation of the $\epsilon$-poles in Eqs. [\[pole\]](#pole){reference-type="eqref" reference="pole"}, [\[poleD\]](#poleD){reference-type="eqref" reference="poleD"}, which yields the relation

$$\label{aas}
\hat a_{\pm sQ}\left({\rm e}^{2 \pi {\rm i}{P \over Q}} \right) {\rm e}^{- 2 \pi {\rm i}{P \over Q} \sigma_{\pm sQ}} =  \hat a_{\pm sP} \left({\rm e}^{2 \pi {\rm i}{Q \over P}} \right) {\rm e}^{- 2 \pi {\rm i}{Q \over P} \sigma_{\pm sP}} \, ,$$

for all $s, P, Q \in {\mathbb Z}_{>0}$ with $P,Q$ coprime. We remark that, for the geometric branch, the formula in Eq. [\[aas\]](#aas){reference-type="eqref" reference="aas"} assumes the simplified form[^1]

$$\label{aas-geom}
\hat a^{(\rm{geom})}_{sQ}\left({\rm e}^{2 \pi {\rm i}{P \over Q}} \right)  =  \hat a^{(\rm{geom})}_{sP} \left({\rm e}^{2 \pi {\rm i}{Q \over P}} \right)  \, ,$$

where again $s, P, Q \in {\mathbb Z}_{>0}$ with $P,Q$ coprime.

Let us now prove that the cancellation formula in Eq. [\[aas\]](#aas){reference-type="eqref" reference="aas"} is indeed a consequence of the integrality structure presented in Eq. [\[multi-conj\]](#multi-conj){reference-type="eqref" reference="multi-conj"}. More precisely, Eqs. [\[ahatf-def\]](#ahatf-def){reference-type="eqref" reference="ahatf-def"}, [\[struc-an\]](#struc-an){reference-type="eqref" reference="struc-an"} imply that $$\label{an-dec}
 \hat{a}_n(q) q^{-\sigma_n}= \sum_{k|n} k D_k \left( q^{n \over k} \right) q^{-{n \over k} \sigma_k} \sum_{j=0}^{k-1} q^{{n \over k}j} \, ,$$ and, after substituting $n=sQ$ and $q = {\rm e}^{2 \pi {\rm i}{P \over Q}}$ with $s, P, Q$ as above, we obtain $$\label{asQtemp}
 \hat{a}_{sQ}\left({\rm e}^{2 \pi {\rm i}{P \over Q}}\right) {\rm e}^{- 2 \pi {\rm i}{P \over Q} \sigma_{sQ}}= \sum_{k| sQ} k D_k \left( {\rm e}^{2 \pi {\rm i}\frac{sP}{k}} \right) {\rm e}^{- 2 \pi {\rm i}\frac{sP}{k} \sigma_{k}} \sum_{j=0}^{k-1} {\rm e}^{2 \pi {\rm i}\frac{sP}{k} j} \, .$$ Since the sum over $j$ on the RHS is non-zero if and only if $k | s$, Eq. [\[asQtemp\]](#asQtemp){reference-type="eqref" reference="asQtemp"} gives $$\label{cs-sequenceP}
 \hat{a}_{sQ}\left({\rm e}^{2 \pi {\rm i}{P \over Q}}\right) {\rm e}^{- 2 \pi {\rm i}{P \over Q} \sigma_{sQ}}= \sum_{k| s} k^2 D_k (1) = c_s \in {\mathbb Z}\, , \quad s \in {\mathbb Z}_{>0} \, ,$$ which is independent of the choice of $P,Q \in {\mathbb Z}_{>0}$ coprime, thus proving the cancellation identity in Eq. [\[aas\]](#aas){reference-type="eqref" reference="aas"}. We note that the case of $\hat{a}_{-n}(q)$ is handled analogously, yielding the same result. In particular, recalling that $\sigma_{-n}=0$, $n \in {\mathbb Z}_{>0}$, it defines the sequence of integers $$\label{cs-sequenceM}
 \hat{a}_{-sQ}\left({\rm e}^{2 \pi {\rm i}{P \over Q}}\right) = \sum_{k| s} k^2 D_{-k} (1) = c_{-s} \in {\mathbb Z}\, , \quad s \in {\mathbb Z}_{>0} \, .$$ Finally, applying the Möbius inversion formula for arithmetic functions, we deduce that

$$D_{\pm s}(1)= {1\over s^2} \sum_{k|s} \mu(k) c_{\pm{ s \over k}} \, , \quad s \in {\mathbb Z}_{>0} \, ,$$

where $\mu(k)$ is the Möbius function. As we will see, the construction presented here is experimentally verified for the knots ${\bf 4}_1$ and ${\bf 5}_2$ in Section [\[sec: examples\]](#sec: examples){reference-type="ref" reference="sec: examples"}.

[^1]: A similar cancellation requirement was obtained in [@szabolcs] in the study of the wave function for quantum mirror curves.
