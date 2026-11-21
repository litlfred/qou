---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-019-55-proof-of-result-on-blocks
section_title: "Proof of result on blocks"
section_number: 5.5
pages: 34-37
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.93
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
[]{#secblocks label="secblocks"} In this section we give a proof of Theorem [\[blocksinSt\]](#blocksinSt){reference-type="ref" reference="blocksinSt"}. To start, given a Young diagram $\lambda$ we will describe how $\operatorname{Lift}_t(L(\lambda))$ decomposes as a sum of indecomposable objects in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ (see Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"}). This description, along with Lemma [\[equalxi\]](#equalxi){reference-type="ref" reference="equalxi"} will be used to prove Theorem [\[blocksinSt\]](#blocksinSt){reference-type="ref" reference="blocksinSt"}. We begin with the following proposition.

::: proposition
[]{#liftsim label="liftsim"} Suppose $\lambda, \lambda^{(1)},\ldots, \lambda^{(m)}$ are Young diagrams with the property that $\operatorname{Lift}_t(L(\lambda))=L(\lambda^{(1)})\oplus\cdots\oplus L(\lambda^{(m)})$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$. Then $\lambda^{(i)}\stackrel{t}{\sim}\lambda$ for all $i=1,\ldots, m$.
:::

::: proof
*Proof.* Fix a positive integer $k$ such that $\lambda^{(i)}_k=\lambda_k=0$ for all $i=1,\ldots, m$. By Lemma [\[equalxi\]](#equalxi){reference-type="ref" reference="equalxi"}(2), it suffices to show $\xi^{\lambda^{(i)}(t)}_{r, k}=\xi^{\lambda(t)}_{r, k}$ for all $r>0$ and $i=1,\ldots, m$. Fix a positive integer $r$, set $n=|\lambda|$, $e=e_\lambda$ and let $\varepsilon\in KP_n(T)$ be a lift of $e$. Let $A(x)\in K[x]$ be the minimal monic polynomial with $A(\omega_n^r(T))\varepsilon=0$. If $\varepsilon=\varepsilon_1+\cdots+\varepsilon_{m'}$ is an orthogonal decomposition of $\varepsilon$ into primitive idempotents, then $m'=m$ and (after reordering) $L(\lambda^{(i)})=([n], \varepsilon_i)$ for all $i=1,\ldots, m$. Hence $A(x)$ is the product of linear terms of the form $x-\xi^{\lambda^{(i)}(T)}_{r, k}$ (see Proposition [\[minpoly\]](#minpoly){reference-type="ref" reference="minpoly"}). Let $B(x), C(x)\in K[x]$ be the unique monic polynomials with $A=BC$ such that $B(x)$ (resp. $C(x)$) is the product of linear terms of the form $x-\xi^{\lambda^{(i)}(T)}_{r, k}$ with $\xi^{\lambda^{(i)}(t)}_{r, k}$ equal to (resp. not equal to) $\xi^{\lambda(t)}_{r, k}$. Suppose for a contradiction that $C(x)\not=1$. Since $B(x)$ and $C(x)$ are relatively prime polynomials of positive degree, there exist nonzero polynomials $G(x), H(x)\in K[x]$ with $\deg G(x)<\deg C(x)$, $\deg H(x)<\deg B(x)$ and $$\label{gbhc}G(x)B(x)+H(x)C(x)=1.$$ Let $N$ be the minimal integer so that all coefficients of both $G'(x):=(T-t)^NG(x)$ and $H'(x):=(T-t)^NH(x)$ lie in $F[[T-t]]$. Then from equation ([\[gbhc\]](#gbhc){reference-type="ref" reference="gbhc"}) we have $$\label{gbhcprime}G'(x)B(x)+H'(x)C(x)=(T-t)^N.$$ Let $b(x), c(x), g(x), h(x)\in F[x]$ be the polynomials obtained by evaluating $T=t$ in the polynomials $B(x), C(x), G'(x), H'(x)$ respectively. If $N>0$, then equation ([\[gbhcprime\]](#gbhcprime){reference-type="ref" reference="gbhcprime"}) implies $b(x)$ (resp. $c(x)$) divides $h(x)$ (resp. $g(x)$). On the other hand, $\deg b(x)=\deg B(x)>\deg H(x)\geq\deg h(x)$. Similarly $\deg c(x)>\deg g(x)$. Thus $h(x)=g(x)=0$ which contradicts the minimality of $N$. Hence $N=0$ which implies the coefficients of $H(x)=H'(x)$ and $G(x)=G'(x)$ are in $F[[T-t]]$. Thus evaluating $T=t$, $x=\omega_n^r(t)$ in equation ([\[gbhc\]](#gbhc){reference-type="ref" reference="gbhc"}) and multiplying by $e$ gives $$\label{gbhcomega}g(\omega_n^r(t))b(\omega_n^r(t))e+h(\omega_n^r(t))c(\omega_n^r(t))e=e.$$ Since $\omega_n^r(t)$ is in the center of $FP_n(t)$ (Proposition [\[centralomega\]](#centralomega){reference-type="ref" reference="centralomega"}(2)) and $b(\omega_n^r(t))c(\omega_n^r(t))e=0$, the two summands on the left side of equation ([\[gbhcomega\]](#gbhcomega){reference-type="ref" reference="gbhcomega"}) are idempotents. As $e$ is assumed to be primitive, either $g(\omega_n^r(t))b(\omega_n^r(t))e=0$ or $h(\omega_n^r(t))c(\omega_n^r(t))e=0$. Since $G(\omega_n^r(T))B(\omega_n^r(T))\varepsilon$ and $H(\omega_n^r(T))C(\omega_n^r(T))\varepsilon$ are lifts of $g(\omega_n^r(t))b(\omega_n^r(t))e$ and $h(\omega_n^r(t))c(\omega_n^r(t))e$ respectively, it follows that either $G(\omega_n^r(T))B(\omega_n^r(T))\varepsilon=0$ or $H(\omega_n^r(T))C(\omega_n^r(T))\varepsilon=0$ (see Theorem [\[appenlift\]](#appenlift){reference-type="ref" reference="appenlift"}) which contradicts the minimality of $A(x)$. This completes the proof. ◻
:::

Among other things, Proposition [\[liftsim\]](#liftsim){reference-type="ref" reference="liftsim"} implies that $\operatorname{Lift}_t(L(\lambda))=L(\lambda)$ whenever $\lambda$ is in a trivial $\stackrel{t}{\sim}$-equivalence class. The following lemma describes $\operatorname{Lift}_t(L(\lambda))$ for arbitrary $\lambda$.

::: lemma
[]{#liftdec label="liftdec"} (1) Suppose $t\in F$ and $\lambda$ is a Young diagram which is either in a trivial $\stackrel{t}{\sim}$-equivalence class or the minimal element of a nontrivial $\stackrel{t}{\sim}$-equivalence class. Then $\operatorname{Lift}_t(L(\lambda))=L(\lambda)$.

\(2\) Suppose $d$ is a nonnegative integer and $B=\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ is a nontrivial $\stackrel{d}{\sim}$-equivalence class. Then $\operatorname{Lift}_d(L(\lambda^{(i)}))=L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})$ for all $i>0$.
:::

::: proof
*Proof.* Part (1) follows from Propositions [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3) and [\[liftsim\]](#liftsim){reference-type="ref" reference="liftsim"}. To prove part (2), assume $\operatorname{Lift}_d(L(\lambda^{(i)}))$ is indecomposable. Then it follows from Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3) that $\operatorname{Lift}_d(L(\lambda^{(i)}))=L(\lambda^{(i)})$. Hence, by Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(2) and Proposition [\[gendimen\]](#gendimen){reference-type="ref" reference="gendimen"}, $\dim_{\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)}L(\lambda^{(i)})=P_{\lambda^{(i)}}(d)$, which is nonzero by Proposition [\[zero\]](#zero){reference-type="ref" reference="zero"}. Therefore $\mathcal{F}(L(\lambda^{(i)}))$ is nonzero in $\operatorname{Rep}(S_d; F)$, which is only possible if $i=0$ (see Propositions [\[Findy\]](#Findy){reference-type="ref" reference="Findy"} and [\[mindiag\]](#mindiag){reference-type="ref" reference="mindiag"}). Hence $\operatorname{Lift}_d(L(\lambda^{(i)}))$ is decomposable whenever $i>0$. We now proceed by induction on $\prec$.

For our base case, assume that $B$ is the minimal $\stackrel{d}{\sim}$-equivalence class. Fix $i>0$ and let $\rho$ be as in as in Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(1). Since $\rho$ is in a trivial $\stackrel{d}{\sim}$-equivalence class $\operatorname{Lift}_d(L(\rho))=L(\rho)$ (by part (1)). Hence, by Example [\[lift1\]](#lift1){reference-type="ref" reference="lift1"}(1), Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(1), and Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(1), $$\operatorname{Lift}_d(L(\rho)\otimes([1], \text{id}_1))=L(\rho)\otimes(L(\Box)\oplus L(\varnothing))=L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})\oplus A$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $A$ is an object with no indecomposable summands of the form $L(\lambda^{(j)})$. By Propositions [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3) and [\[liftsim\]](#liftsim){reference-type="ref" reference="liftsim"}, $L(\rho)\otimes([1], \text{id}_1)$ must have $L(\lambda^{(i)})$ as an indecomposable summand in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. Moreover, since $\operatorname{Lift}_d(L(\lambda^{(i)}))$ is decomposable, it must be the case that $\operatorname{Lift}_d(L(\lambda^{(i)}))=L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})$.

Now assume $B$ is not minimal and let $B'=\{\rho^{(0)}\subset\rho^{(1)}\subset\cdots\}$ be as in Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2). Since $B'\precneqq B$, by induction we have $\operatorname{Lift}_d(L(\rho^{(i)}))=L(\rho^{(i)})\oplus L(\rho^{(i-1)})$ whenever $i>0$. Hence, by Example [\[lift1\]](#lift1){reference-type="ref" reference="lift1"}(1), Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(1) and Lemma [\[oneboxlemma\]](#oneboxlemma){reference-type="ref" reference="oneboxlemma"}(2), $$\begin{array}{rcl}\operatorname{Lift}_d(L(\rho^{(i)})\otimes([1], \text{id}_1)) & = &(L(\rho^{(i)})\oplus L(\rho^{(i-1)}))\otimes(L(\Box)\oplus L(\varnothing))\\
& = & L(\lambda^{(i)})\oplus L(\lambda^{(i-1)})\oplus A\end{array}$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $A$ is an object with no indecomposable summands of the form $L(\lambda^{(i)})$. As in the base case, this implies the desired result. ◻
:::

::: remark
Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"}(2) implies that $P_{\lambda^{(i)}}(d)=-P_{\lambda^ 
{(i-1)}}(d)$ for $i>0$ whence $P_{\lambda^{(i)}}(d)=(-1)^i P_{\lambda^{(0)}}(d)$. This identity was observed by Deligne, see [@Del07 §7.5].
:::

We are ready to prove the main result section [\[blocks\]](#blocks){reference-type="ref" reference="blocks"}, which we restate now.

*$L(\lambda)$ and $L(\lambda')$ are in the same block of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ if and only if $\lambda\stackrel{t}{\sim}\lambda'$.*

::: proof
*Proof.* If $L(\lambda)$ and $L(\lambda')$ are in the same block of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$, then Lemma [\[equalxi\]](#equalxi){reference-type="ref" reference="equalxi"} implies $\lambda\stackrel{t}{\sim}\lambda'$. To prove the converse, by Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}(1) we may assume $t=d$ is a nonnegative integer. Suppose $\{\lambda^{(0)}\subset \lambda^{(1)}\subset\cdots\}$ is a nontrivial $\stackrel{d}{\sim}$-equivalence class and fix $i> 0$. By Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(5) $\dim_F\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)}(L(\lambda^{(i-1)}), L(\lambda^{(i)}))$ is equal to $\dim_K\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}(\operatorname{Lift}_d(L(\lambda^{(i-1)})), \operatorname{Lift}_d(L(\lambda^{(i)})))$, which is nonzero by Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"}. The result follows. ◻
:::

We close this section by examining the dimensions of the Hom spaces between indecomposable objects in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$.

::: proposition
[]{#dimstuff label="dimstuff"} (1) $\dim_F\operatorname{End}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)}(L(\lambda))=1$ whenever $\lambda$ is in a trivial $\stackrel{t}{\sim}$-equivalence class. In particular, the block corresponding to a trivial $\stackrel{t}{\sim}$-equivalence class is trivial.

\(2\) Given a nontrivial block $\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$, $$\dim_F\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)}(L(\lambda^{(i)}), L(\lambda^{(j)}))=\left\{\begin{array}{ll}
2& \text{if $i=j>0$,}\\
0& \text{if $|i-j|>2$,}\\
1& \text{otherwise.}
\end{array}\right.$$
:::

::: proof
*Proof.* By Lemma [\[liftdec\]](#liftdec){reference-type="ref" reference="liftdec"} and Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(5), it suffices to prove $$\dim_K\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)}(L(\lambda), L(\lambda'))=\left\{\begin{array}{ll}
1& \text{if $\lambda=\lambda'$,}\\
0& \text{if $\lambda\not=\lambda'$.}
\end{array}\right.$$ By Proposition [\[fieldex\]](#fieldex){reference-type="ref" reference="fieldex"} it suffices to consider the case when $K$ is algebraically closed. As $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ is semisimple (Corollary [\[ssT\]](#ssT){reference-type="ref" reference="ssT"}), the result follows from Schur's lemma. ◻
:::

::: corollary
[]{#ss label="ss"} $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ is semisimple if and only if $t$ is not a nonnegative integer.
:::

::: proof
*Proof.* This follows from Proposition [\[dimstuff\]](#dimstuff){reference-type="ref" reference="dimstuff"}(1) along with corollaries [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}(1) and [\[mindiag\]](#mindiag){reference-type="ref" reference="mindiag"}. ◻
:::
