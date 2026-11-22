---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-007-the-wave-function-in-the-rational-case-i
section_title: "The wave function in the rational case, I"
section_number: null
pages: 14-17
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.994
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
[]{#sec: rational1 label="sec: rational1"} We will now apply the results obtained in Section [\[sec: cancellation\]](#sec: cancellation){reference-type="ref" reference="sec: cancellation"} to derive explicitly the exact wave function $\chi(u;\hbar)$ in Eq. [\[exactconj\]](#exactconj){reference-type="eqref" reference="exactconj"} as a power series in $X, X^{-1}$ for rational values of $\hbar$. Let us start from the holomorphic components $\phi^{(\alpha), {\rm WKB}} (X; q)$ and fix $\hbar$ as in Eq. [\[rathbar\]](#rathbar){reference-type="eqref" reference="rathbar"}, that is, $$q={\rm e}^{{\rm i}\hbar}={\rm e}^{2 \pi {\rm i}{P \over Q}} \, , \quad  P,Q \in {\mathbb Z}_{>0} \; \; \text{coprime} \, .$$ As before, we drop the label $\alpha$ for simplicity and we intend the following discussion to hold for each choice of the classical branch independently. The singular terms come from the values $n = sQ$ for $s \in {\mathbb Z}_{>0}$, while choosing $n= sQ+k$ with $1 \le k \le Q-1$ produces only regular terms. Specifically, the terms involving singularities are obtained by substituting Eq. [\[pole\]](#pole){reference-type="eqref" reference="pole"} into Eq. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"} and contain the non-singular contributions

$$\label{finitep1}
\sum_{s \ge 1} \left( -{1\over 2} +{1\over  sQ} q {\partial \over \partial q} \right) \frac{\hat a_{\pm s Q} (q)}{s Q q^{\sigma_{\pm sQ}}}  X^{\pm sQ} \, .$$

The regular terms associated with $n \ne sQ$ are instead

$$\label{finitep2}
\sum_{k=1}^{Q-1} \frac{1}{q^k-1} \sum_{s \ge 0} {\hat a_{\pm (s Q +k)} (q) \over (sQ+k) q^{\sigma_{\pm (sQ+k)}}} X^{\pm (sQ+k)} \, ,$$

where we have used that $q^{sQ+k}= q^k$. Thus, the sum of the quantities in Eqs. [\[finitep1\]](#finitep1){reference-type="eqref" reference="finitep1"}, [\[finitep2\]](#finitep2){reference-type="eqref" reference="finitep2"} is the finite part of $\phi^{\rm WKB}(X;q)$ evaluated at the rational point in Eq. [\[rathbar\]](#rathbar){reference-type="eqref" reference="rathbar"}. It is convenient to introduce the functions

$$\label{phifunct-parts}
\begin{align}
\varphi^{(+)}_Q(X)&= \sum_{s \ge 1} {\hat a_{s Q} (q) \over sQ q^{\sigma_{sQ}}} X^{sQ}    \, , \\
\varphi^{(-)}_Q(X)&= \sum_{s \ge 1}  {\hat a_{-s Q} (q) \over (-sQ) q^{sQ + \sigma_{-sQ}}} X^{-sQ}   \, , \\
\varphi^{(+)}_k(X)&=  \sum_{s \ge 0} {\hat a_{s Q +k} (q) \over (sQ+k) q^{\sigma_{sQ+k}}} X^{sQ+k}\, , \quad k=1, \dots, Q-1 \, , \\
\varphi^{(-)}_k(X)&=  \sum_{s \ge 0} {\hat a_{-(s Q +k)} (q) \over -(sQ+k) q^{sQ+k + \sigma_{-(sQ+k)}}} X^{-(sQ+k)}\, , \quad k=1, \dots, Q-1 \, ,
\end{align}$$

where we hide the dependence on $q$ to simplify the notation. Moreover, we define

$$\label{phifunct}
\begin{align}
\varphi_Q(X)&=  \varphi^{(+)}_Q(X) + \varphi^{(-)}_Q(X)  \, , \\
\varphi_k(X)&=  \varphi^{(+)}_k(X) - q^k \varphi^{(-)}_k(X) \, , \quad k=1, \dots, Q-1 \, .
\end{align}$$

Putting Eqs. [\[finitep1\]](#finitep1){reference-type="eqref" reference="finitep1"}, [\[finitep2\]](#finitep2){reference-type="eqref" reference="finitep2"} together and suitably identifying the functions just introduced in Eq. [\[phifunct\]](#phifunct){reference-type="eqref" reference="phifunct"}, we can write the holomorphic block as

$$\label{phirat}
\phi^{\rm WKB}(X;q)= -{1\over 2} \varphi_Q(X) + q{\partial \over \partial q} \int_0^X \varphi_Q(X') {{\rm d}X '\over X'} + 
\sum_{k=1}^{Q-1} { \varphi_k(X) \over q^k-1} \, .$$

Let us now consider the antiholomorphic component $\phi^{\rm WKB} (X_D; q_D)$ and fix $\hbar$ as above. The derivation in this case is very similar to the previous one, but the novelty is the appearance of $\log X$ terms, which originate from the $\epsilon$-expansion of the dual variable $$X_D=X^{2 \pi \over \hbar}=X^{Q \over P} \, .$$ Let us add a small positive term $\epsilon$ to the rational value of $\hbar$ as in Eq. [\[hbareps\]](#hbareps){reference-type="eqref" reference="hbareps"}. Then, we consider the limit $\epsilon\rightarrow 0$ and find that

$$\label{XDeps}
X_{\epsilon,D}=X^{2 \pi \over \hbar_{\epsilon}}=X^{{Q \over P} {1 \over 1+ {\epsilon \over 2 \pi} {Q \over P}}}= X^{Q\over P} \left( 1 -{Q^2  \over 2 \pi P^2} \epsilon\log X +  {\cal O}(\epsilon^2) \right) \, .$$

As described before, the singular terms come from the values $n = sP$ for $s \in {\mathbb Z}_{>0}$, while choosing $n= sP+k$ with $1 \le k \le P-1$ produces only regular terms. Specifically, the terms involving singularities are obtained by substituting Eqs. [\[poleD\]](#poleD){reference-type="eqref" reference="poleD"}, [\[XDeps\]](#XDeps){reference-type="eqref" reference="XDeps"} into the Eq. [\[phi-struc\]](#phi-struc){reference-type="eqref" reference="phi-struc"} and contain the non-singular contributions

$$\label{finitep1D}
\sum_{s \ge 1} \left( \frac{{\rm i}}{2 \pi sQ}-{1\over 2} +{1\over  sP} q_D {\partial \over \partial q_D} \mp \frac{{\rm i}}{2 \pi} \log X \right) \frac{ \hat a_{\pm s P} (q_D) }{s P q_D^{\sigma_{\pm sP}}} X^{\pm sQ} \, .$$

The regular terms associated with $n \ne sP$ are instead

$$\label{finitep2D}
\sum_{k=1}^{P-1} \frac{1}{q_D^k-1} \sum_{s \ge 0} {\hat a_{\pm (s P +k)} (q_D) \over (sP+k) q_D^{\sigma_{\pm (sP+k)}}} X^{\pm (sP+k){Q \over P}} \, ,$$

where we have used that $q_D={\rm e}^{2 \pi {Q \over P}}$ and thus $q_D^{sP+k}= q_D^k$. Therefore, the sum of the quantities in Eqs. [\[finitep1D\]](#finitep1D){reference-type="eqref" reference="finitep1D"}, [\[finitep2D\]](#finitep2D){reference-type="eqref" reference="finitep2D"} is the finite part of the function $\phi^{\rm WKB}(X_D;q_D)$ evaluated at the rational point in Eq. [\[rathbar\]](#rathbar){reference-type="eqref" reference="rathbar"}. As for the holomorphic block, we introduce the functions

$$\label{phitildefunct-parts}
\begin{align}
\widetilde \varphi^{(+)}_P(X_D)&= \sum_{s \ge 1} {\hat a_{s P} (q_D) \over sP q_D^{\sigma_{sP}}} X_D^{sP}  \, ,\\
\widetilde \varphi^{(-)}_P(X_D)&= \sum_{s \ge 1} {\hat a_{-s P} (q_D) \over -(sP) q_D^{sP+\sigma_{-sP}}} X_D^{-sP}  \, ,\\
\widetilde \varphi^{(+)}_k(X_D)&=  \sum_{s \ge 0} {\hat a_{s P +k} (q_D) \over (sP+k) q_D^{\sigma_{sP+k}}} X_D^{sP+k}  \, , \quad k=1, \dots, P-1 \, , \\
\widetilde \varphi^{(-)}_k(X_D)&=  \sum_{s \ge 0} {\hat a_{-(s P +k)} (q_D) \over -(sP+k) q_D^{sP+k+\sigma_{-(sP+k)}}} X_D^{-(sP+k)}  \, , \quad k=1, \dots, P-1 \, , 
\end{align}$$

where we hide the dependence on $q_D$ to simplify the notation. Moreover, we define

$$\label{phitildefunct}
\begin{align}
\widetilde  \varphi_P(X_D)&=  \widetilde \varphi^{(+)}_P(X_D) + \widetilde \varphi^{(-)}_P(X_D)  \, , \\
\widetilde  \varphi_k(X_D)&=  \widetilde \varphi^{(+)}_k(X_D) - q_D^k \widetilde \varphi^{(-)}_k(X_D) \, , \quad k=1, \dots, Q-1 \, .
\end{align}$$

Putting Eqs. [\[finitep1D\]](#finitep1D){reference-type="eqref" reference="finitep1D"}, [\[finitep2D\]](#finitep2D){reference-type="eqref" reference="finitep2D"} together and suitably identifying the functions just introduced in Eq. [\[phitildefunct\]](#phitildefunct){reference-type="eqref" reference="phitildefunct"}, we can now write the antiholomorphic block as

$$\label{phiratD}
\begin{aligned}
\phi^{\rm WKB}(X_D;q_D)=& -\left( {1\over 2} + {{\rm i}\over 2 \pi} \log X \right) \widetilde \varphi_P(X_D) \\
&+ \left({{\rm i}P \over 2 \pi Q} + q_D{\partial \over \partial q_D} \right) \int_0^{X_D} \widetilde \varphi_P(X_D') {{\rm d}X_D' \over X_D'} + \sum_{k=1}^{P-1} { \widetilde \varphi_k(X_D)\over q_D^k-1} \, .
\end{aligned}$$

Finally, we observe that $$\label{rel-phi}
\widetilde \varphi^{(+)}_P(X_D)={Q \over P} \varphi^{(+)}_Q(X) \, , \quad  \widetilde \varphi^{(-)}_P(X_D)={Q \over P} q^{s Q \left( 1- \frac{Q}{P} \right)} \varphi^{(-)}_Q(X) \, ,$$ as a direct consequence of the cancellation symmetry in Eq. [\[aas\]](#aas){reference-type="eqref" reference="aas"}. Therefore, after summing Eqs. [\[phirat\]](#phirat){reference-type="eqref" reference="phirat"}, [\[phiratD\]](#phiratD){reference-type="eqref" reference="phiratD"} and using the relations in Eq. [\[rel-phi\]](#rel-phi){reference-type="eqref" reference="rel-phi"}, we obtain the expression $$\label{phirat-final}
\begin{aligned}
\phi^{\rm WKB}(X;q)+ \phi^{\rm WKB}(X_D;q_D)= & \left( -{1 \over 2} - {Q \over 2 P} - {{\rm i}Q \over 2 \pi P} \log X \right) \varphi_Q(X) \\
&+ \left( {{\rm i}Q \over 2 \pi P} + 2 q {\partial \over \partial q} \right)\int_0^X \varphi_Q(X') {{\rm d}X '\over X'} \\
&+ s Q \left( 1- \frac{Q}{P} \right) \int_0^X \varphi^{(-)}_Q(X') {{\rm d}X '\over X'} \\
&+ \sum_{k=1}^{Q-1} { \varphi_k(X)\over q^k-1} + \sum_{k=1}^{P-1} { \widetilde \varphi_k(X^{Q \over P})\over q^{k{Q^2 \over P^2}}-1} \, .
\end{aligned}$$

Moreover, the power series defined in Eqs. [\[phifunct\]](#phifunct){reference-type="eqref" reference="phifunct"}, [\[phitildefunct\]](#phitildefunct){reference-type="eqref" reference="phitildefunct"}, which dictate the formula for the exact wave function at rational points following Eq. [\[phirat-final\]](#phirat-final){reference-type="eqref" reference="phirat-final"}, are determined by the function $$\label{upsilon}
\Upsilon (X)=\Upsilon^{(+)} (X)+\Upsilon^{(-)} (X)=\sum_{n \ge 1} {\hat{a}_n (q) \over n q^{\sigma_n}} X^n + \sum_{n \ge 1} {\hat{a}_{-n} (q) \over (-n) q^{n+\sigma_{-n}}} X^{-n} \, ,$$ where, again, we hide the dependence on $q$ to simplify the notation. Indeed, we can write

$$\begin{align}
\varphi_Q(X)&={1\over Q} \sum_{m=0}^{Q-1}  \Upsilon (q^m X)  \, , \label{varphiQ-U} \\
\varphi^{(\pm)}_k(X)&={1\over Q} \sum_{m=0}^{Q-1} q^{\mp m k} \, \Upsilon^{(\pm)} (q^m X,q) \, , \quad k=1, \dots, Q-1 \, , 
\end{align}$$

and similarly $$\begin{align}
\widetilde \varphi_P(X_D)&={1\over P} \sum_{m=0}^{P-1}  \Upsilon (q_D^m X_D)  \, , \\
\widetilde \varphi^{(\pm)}_k(X_D)&={1\over P} \sum_{m=0}^{P-1} q_D^{\mp m k} \, \Upsilon^{(\pm)} (q_D^m X_D) \, , \quad k=1, \dots, P-1 \, .
\end{align}$$ Let us stress that the derivation we have presented here implies a fixed choice of the classical branch. Indeed, the functions $\Upsilon (X), \varphi_Q(X), \varphi_k(X), \widetilde \varphi_P(X_D), \widetilde \varphi_k(X_D)$ are implicitly dependent on the label $\alpha$. We note that, applying Eqs. [\[cs-sequenceP\]](#cs-sequenceP){reference-type="eqref" reference="cs-sequenceP"}, [\[cs-sequenceM\]](#cs-sequenceM){reference-type="eqref" reference="cs-sequenceM"}, we can simply read off the integer coefficients $c_{\pm s}$, $s \in {\mathbb Z}_{>0}$, from the function $\varphi_Q(X)$. Namely, we have that

$$\label{varphiQ-cs}
\varphi_Q(X)=\sum_{s \ge 1} {c_s \over sQ} X^{sQ} - {c_{-s} \over sQ} X^{-sQ} \, ,$$ after substituting $q^{sQ}=1$. In Appendix [\[app: rational2\]](#app: rational2){reference-type="ref" reference="app: rational2"}, we describe an alternative way of computing the integer sequences $\{ c_{\pm s} \}$, $s \in {\mathbb Z}_{>0}$ using Eq. [\[phirat-final\]](#phirat-final){reference-type="eqref" reference="phirat-final"}. We will show in Section [\[sec: examples\]](#sec: examples){reference-type="ref" reference="sec: examples"} that, starting from the known closed expression for the holomorphic and antiholomorphic blocks, we can successfully compute the integer coefficients for both series in $X, X^{-1}$ and all choices of the saddle connection $\alpha$ in the examples of the figure-eight and the three-twist knots.
