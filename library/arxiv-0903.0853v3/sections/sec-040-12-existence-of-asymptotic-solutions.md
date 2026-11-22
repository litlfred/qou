---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-040-12-existence-of-asymptotic-solutions
section_title: "Existence of asymptotic solutions"
section_number: 12
pages: 58-62
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.972
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:existasymptsols label="section:existasymptsols"}

We call *adequate* an open subset ${\mathbf C}^{*}$ of the form $q^{-{\mathbf N}} U_{0}$, where the $q^{-k} U_{0}, k \geq 0$ are pairwise disjoint. Clearly, ${\mathscr{A}}_{0}(U_{\infty})$ is a ${{\mathbf C}(\{z\})}$-vector space stable under $\sigma_q$. In particular, any $q$-difference operator $P := \sigma_q^{n} + a_{1} \sigma_q^{n-1} + \cdots + a_{n} \in {{\mathcal{D}}_{q}}$ defines a ${\mathbf C}$-linear endomorphism $P: f \mapsto P f = \sigma_q^{n}(f) + a_{1} \sigma_q^{n-1} + \cdots + a_{n} f$ of ${\mathscr{A}}_{0}(U_{\infty})$. Likewise, any matrix $A \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$, defines a ${\mathbf C}$-linear endomorphism $\sigma_q- A: X \mapsto \sigma_qX - A X$ of ${\mathscr{A}}_{0}(U_{\infty})^{n}$.

::: theo
[]{#theo:TFESA label="theo:TFESA"} Let $A \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$ and let $\hat{X} \in {{\mathbf C}[[z]]}^{n}$ be a formal solution of the system $\sigma_qX = A X$. For any adequate open subset $U$, there exists a solution $X \in {\mathscr{A}}(U_{\infty})^{n}$ of that system which is asymptotic to $\hat{X}$.
:::

::: proof
*Proof.* From theorem [\[theo:BorelRittfaible\]](#theo:BorelRittfaible){reference-type="ref" reference="theo:BorelRittfaible"}, there exists $Y \in {\mathscr{A}}(U_{\infty})^{n}$ which is asymptotic to $\hat{X}$ (without however being a solution of the system). Set: $$W := \sigma_qY - A Y = \sigma_q(Y - \hat{X}) - A (Y - \hat{X})
\in {\mathscr{A}}_{0}(U_{\infty})^{n}.$$ From proposition [\[prop:surjplats\]](#prop:surjplats){reference-type="ref" reference="prop:surjplats"} below, there exists $Z \in {\mathscr{A}}_{0}(U_{\infty})^{n}$ such that $\sigma_qZ - A Z = W$. Then $X := Y - Z \in {\mathscr{A}}(U_{\infty})^{n}$ is asymptotic to $\hat{X}$ and solution of the system. ◻
:::

::: prop
[]{#prop:surjplats label="prop:surjplats"} Let $A \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$ and let $U$ be an adequate open subset. Then, the endomorphism $\sigma_q- A$ of ${\mathscr{A}}_{0}(U_{\infty})^{n}$ is onto.
:::

::: proof
*Proof.* Let $F \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$ and $B := F[A]$. From the commutative diagram: $$\begin{CD}
{\mathscr{A}}_{0}(U_{\infty})^{n}   @>{\sigma_q- A}>>  {\mathscr{A}}_{0}(U_{\infty})^{n}        \\
@VV{F}V         @VV{\sigma_qF}V        \\
{\mathscr{A}}_{0}(U_{\infty})^{n}   @>{\sigma_q- B}>>  {\mathscr{A}}_{0}(U_{\infty})^{n}
\end{CD}$$ in which the vertical arrows are isomorphisms, we just have to prove that $\sigma_q- B$ is onto. After the cyclic vector lemma (lemma [\[lemm:cyclicvector\]](#lemm:cyclicvector){reference-type="ref" reference="lemm:cyclicvector"}), we can take $B := A_{P}$, the companion matrix of $P := \sigma_q^{n} + a_{1} \sigma_q^{n-1} + \cdots + a_{n}$ described in [\[subsubsection:functorofsolutions\]](#subsubsection:functorofsolutions){reference-type="ref" reference="subsubsection:functorofsolutions"}. We then apply lemma [\[lemm:surjsystouequa\]](#lemm:surjsystouequa){reference-type="ref" reference="lemm:surjsystouequa"} (herebelow) and theorem [\[theo:surjplats\]](#theo:surjplats){reference-type="ref" reference="theo:surjplats"} (further below). ◻
:::

::: lemm
[]{#lemm:surjsystouequa label="lemm:surjsystouequa"} Let $R$ be a ${{\mathbf C}(\{z\})}$-vector space on which $\sigma_q$ operates. With the notations of the previous proposition, $P: R \rightarrow R$ is onto if, and only if, $\sigma_q- A_{P}: R^{n} \rightarrow R^{n}$ is onto.
:::

::: proof
*Proof.* (i) Assume $P$ is onto. To solve $(\sigma_q- A_{P}) \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = 
\begin{pmatrix} y_{1} \\ \vdots \\ y_{n} \end{pmatrix}$, put $x_{i+1} := \sigma_qx_{i} - y_{i}$; one sees that $x_{1}$ just has to be solution of an equation $P x_{1} = z$, where $z$ is some explicit expression of the $y_{i}$.\
(ii) Assume $\sigma_q- A_{P}$ is onto. To solve $P f = g$, it is enough to solve $\sigma_qX - A_{P} X = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ g \end{pmatrix}$ and to set $f$ to the first component of $X$. ◻
:::

::: rema
This computation is directly related to the homotopy of complexes discussed in [\[subsection:complexhomotopy\]](#subsection:complexhomotopy){reference-type="ref" reference="subsection:complexhomotopy"}.
:::

::: theo
[]{#theo:surjplats label="theo:surjplats"} The endomorphism $P$ of ${\mathscr{A}}_{0}(U_{\infty})$ is onto.
:::

::: proof
*Proof.* We give the proof under the assumption that the slopes are integral, which is the only case we need in this paper; the reader will easily deduce the general case by ramification. The counterpart of the slope filtration on the side of $q$-difference operators is the existence of a factorisation [@MarotteZhang; @JSFIL; @zh1] of $P$ as a product of non commuting factors: elements of ${{\mathbf C}\{z\}}^{*}$ (which induce automorphisms of ${\mathscr{A}}_{0}(U_{\infty})$) and first order operators $z^{\mu} \sigma_q- a$, $\mu \in {\mathbf Z}$, $a \in {\mathbf C}^{*}$. We are therefore reduced to the following lemma. (This is where some analysis comes in !) ◻
:::

::: lemm
[]{#lemm:surjrang1 label="lemm:surjrang1"} The endomorphism $f \mapsto z^{\mu} \sigma_qf - a f$ of ${\mathscr{A}}_{0}(U_{\infty})$ is onto.
:::

::: proof
*Proof.* Write $L$ this endomorphism. Let $h \in {\mathscr{A}}_0(U_\infty)$; for all $n \in {\mathbf N}$ and each strict stable subset $V$ of $U$, there exists $C_{n,V}>0$ such that $\left |h(z)\right |< C_{n,V} \left |z \right |^n$ over $V$. We distinguish two cases: (i) $\mu \leq 0$; (ii) $\mu > 0$.

Case (i): $\mu \leq 0$ (easy case). Let $\Phi$ be the automorphism of ${\mathscr{A}}_0(U_\infty)$ defined by $\Phi(f) := a q^\mu z^{-\mu} \sigma_{q^{-1}} f$; one has $\Phi^m f = a^m q^{\mu m(m+1)/2} z^{-m\mu}\sigma_{q^{-m}} f$ for all $m \geq 0$. Since $\left |h(z)\right |\leq  C_{n,V} \left |z\right |^n$ on each stable strict subset $V$ of $U$ and all integers $n \geq 0$, one finds: $$\forall z \in V \;,\; \sum_{m \geq 0} \left |\Phi^m h(z) \right |\leq 
C_{n,V} \,\sum_{m\ge 0} \left |a \right |^m \left |q \right |^{\mu m(m+1)/2} \, 
\left |q\right |^{-nm}\, \left |z \right |^n.$$ One deduces that the series $\sum_{m \geq 0} \Phi^m h$ defines a flat function over $U$, write it $H \in {\mathscr{A}}_0(U_\infty)$. Observing that $L H = z^\mu \sigma_q(H-\Phi H) = z^\mu \sigma_qh$, we see that $L$ is onto over ${\mathscr{A}}_0(U_\infty)$.

Case (ii): $\mu > 0$ (hard case). For all $j \in {\mathbf N}$, set $U_j := q^{-j} U_0 = \{z \in {\mathbf C}^* ~ | ~q^j z \in U_0\}$; these are pairwise disjoint since $U$ was assumed to be adequate. We are going to build successively $f_0,f_1,f_2, \ldots$ over $U_0,U_1,U_2,\ldots$, which will give rise to a function $f$ defined over $U = q^{-{\mathbf N}} U_0$, with $f_j = f_{|U_j}$ and $L f = h$.

For all $j \in {\mathbf N}$, let $h_j := h_{|{U_j}} : U_j \rightarrow {\mathbf C}$. Since $(\sigma_qf)_{|U_j}=\sigma_qf_{j-1}$, equation $L f = h$ is equivalent to system: $$\forall j \in {\mathbf N}^{*} \;,\; z^\mu \sigma_q f_{j-1} - a f_j = h_j,$$ also written: $$\label{equa:Lfh}
\forall j \in {\mathbf N}^{*} \;,\; f_j = (z^\mu \sigma_q f_{j-1}-h_j)/a.$$

We agree that $f_{-1} \equiv 0$ and $f_0 = h_0/a$. Iterating the last relation [\[equa:Lfh\]](#equa:Lfh){reference-type="eqref" reference="equa:Lfh"} above, we find: $$\label{equa:Lfhj}
\forall j \in {\mathbf N}^{*} \;,\; f_j = 
-\sum_{\ell=0}^j q^{\mu\ell(\ell-1)/2} z^{\ell\mu} \sigma_q^\ell h_{j-\ell}\,a^{-\ell-1}.$$ Write $f$ the function defined on $U$ by the relations $f_{|U_j} = f_j$, $j \in {\mathbf N}$; Clearly, $Lf = h$ on $U$. We are left to show that $f\in {\mathscr{A}}_0(U_\infty)$.

Let $n \in {\mathbf N}$ and $V$ a strict stable subset of $U$; let $V_j := U_j \cap V$ and choose a $K > 0$ such that $\left |z \right |\leq K \left |q \right |^{-j}$ for all $z \in U_j$; one has $|z|\le K|q|^{-j}$ on each $V_j$. Bounding by above the right hand side of [\[equa:Lfhj\]](#equa:Lfhj){reference-type="eqref" reference="equa:Lfhj"}, one gets: $$\label{equa:Lfhj||}
\forall z \in V_j \;,\;
\left |f_j(z) \right |\leq 
\dfrac{C_{n,V}}{a} \, P_j(\left |q \right |^n\alpha)\,\left |z \right |^n,$$ where $\alpha := K^\mu/a$ and where $P_j$ denotes the polynomial with positive coefficients: $$P_j(X) := \sum_{\ell=0}^j \left |q \right |^{\mu\ell(\ell-1)/2-j\ell\mu}\,X^\ell.$$ Taking in account the relation $$P_{j+1}(X) = 
P_j(\left |q \right |^{-\mu}X)+ \left |q \right |^{-\mu(j+1)(j+2)/2}\,X^{j+1}\,,$$ one finds that $P_j(X) \leq P(X;\mu,q)$ for all $X > 0$, where we write $P(z;\mu,q)$ the entire function defined by: $$P(z;\mu,q) := \sum_{j=0}^\infty \left |q \right |^{-\mu j(j+1)/2}\,z^{j}.$$ Said otherwise, [\[equa:Lfhj\|\|\]](#equa:Lfhj||){reference-type="eqref" reference="equa:Lfhj||"} can be written in the form: $$\forall z \in V_j \;,\;
\left |f_j(z) \right |\leq 
\frac{C_{n,V}}a\,P(\left |q \right |^n\alpha;\mu,q)\,\left |z \right |^n,$$ which allows us to conclude that $f$ is flat. ◻
:::

We now apply theorem [\[theo:TFESA\]](#theo:TFESA){reference-type="ref" reference="theo:TFESA"} to a situation that we shall meet when we prove theorem [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"}.\
Let $A_{0} \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$ be the matrix of a pure module and let $A \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$ a matrix formally equivalent to $A_{0}$. Let $\hat{F} \in {\text{GL}}_{n}({{\mathbf C}((z))})$ be a gauge transformation proving this equivalence, *i.e.* $\hat{F}[A_{0}] = A$. (Note that we do not assume $\hat{F} \in {\mathfrak{G}}({{\mathbf C}((z))})$.) The conjugation relation is equivalent to $\sigma_q\hat{F} = A \hat{F} A_{0}^{-1}$, which we regard as a $q$-difference system of rank $n^{2}$ in the space ${\text{Mat}}_{n}({{\mathbf C}(\{z\})}) \simeq {{\mathbf C}(\{z\})}^{n^{2}}$. After theorem [\[theo:TFESA\]](#theo:TFESA){reference-type="ref" reference="theo:TFESA"}, there exists over each adequate open set $U$ a solution $F_{U} \in {\text{Mat}}_{n}({{\mathbf C}(\{z\})})$ of the system $\sigma_qF = A F A_{0}^{-1}$ that is asymptotic to $\hat{F}$. Since the latter is invertible, and since $\det F_{U}$ is obviously asymptotic to $\det \hat{F}$, whence non zero, $F_{U}$ is invertible.\
Now let $U'$ another adequate open set which meets $U$. Then $U'' := U \cap U'$ is adequate and the matrix $G := F_{U}^{-1} F_{U'}$ satisfies the two following properties:

1.  It is an automorphism of $A_{0}, \emph{i.e.}\ G[A_{0}] = A_{0}$.

2.  It is asymptotic to $\hat{F}^{-1} \hat{F} = I_{n}$, *i.e.* the coefficients of $G - I_{n}$ belong to ${\mathscr{A}}_0(U''_\infty)$.

::: lemm
[]{#lemm:cocyclasympt label="lemm:cocyclasympt"} The matrix $G$ belongs to ${\mathfrak{G}}({\mathscr{A}}_0(U''_\infty))$.
:::

::: proof
*Proof.* With the usual notations for $A_{0}$, each block of $G$ satisfies: $$\sigma_qG_{i,j} = 
\left(z^{\mu_{j}} A_{j}\right)^{-1} G_{i,j} \left(z^{\mu_{i}} A_{i}\right) = 
z^{\mu_{i} - \mu_{j}} A_{j}^{-1} G_{i,j} A_{i}.$$ The order of growth or decay of $G_{i,j}$ near $0$ is therefore the same as ${\theta_{q}}^{\mu_{i} - \mu_{j}}$. Since $G_{i,j}$ is flat for $i \neq j$, this implies $G_{i,j} = 0$ for $i > j$. For $i = j$, we apply the same argument to $G_{i,i} - I_{r_{i}}$, which therefore vanishes. ◻
:::
