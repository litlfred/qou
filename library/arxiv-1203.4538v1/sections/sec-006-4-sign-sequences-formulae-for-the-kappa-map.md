---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-006-4-sign-sequences-formulae-for-the-kappa-map
section_title: "Sign sequences formulae for the kappa map."
section_number: 4
pages: 9-13
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.958
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 9 sections: Front matter; Introduction.; Preliminaries on surreal numbers."
---
[]{#sect:kappa-sign label="sect:kappa-sign"} For any $a\in\textbf{No}$ and $n\in\mathbb{N}$, we denote by $\kappa_{a,n}:=\log^n(\kappa_a)$ and $\kappa_{a,-n}=\exp^n(\kappa_a)$, where $\log^0$ and $\exp^0$ are equal to the identity map on $\textbf{No}$. The aim of this section is to show that $\kappa_{a,n}$ and $\kappa_{a,-n}$ for any $n$ are elements of $\omega^{\omega^{No}}$, and to give their sign sequence. In order to do so, we introduce the following auxiliary map $\iota$ and give its sign sequence.

::: nota
[]{#nota:gamma label="nota:gamma"}

-   Consider a surreal number $a=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand \alpha_1\oplus\binampersand \beta_1\ominus\binampersand\cdots$. For any ordinal $\mu\in\textbf{On}$ intervening in the writing of $a$, we set:

    ::: center
    $\gamma_\mu:=\displaystyle\sum_{\lambda\leq\mu}\alpha_\lambda\ \  \textrm{ (ordinal sum).}$
    :::

-   We set $\Omega^0$ to be the constant map equal to 1 in $\textbf{No}$ and $\epsilon_{\flat 0}:=0$.
:::

::: lem
[]{#lemme:iota label="lemme:iota"} The recursive formula:

::: center
$\forall a\in\textbf{No},\ \iota(a)=\iota_a:=\langle \iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus\ |\ \iota_{a^R}\binampersand n\ominus\rangle$.
:::

(where it is understood that $n\in\mathbb{N}$) defines a map

::: center
$\begin{array}{llcl}
\iota: &\textbf{No}&\rightarrow&\textbf{No}\\
a&\mapsto&\iota(a):=\iota_a
\end{array}$
:::

such that for any $a=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand \alpha_1\oplus\binampersand \beta_1\ominus\binampersand\cdots$, the sign sequence of $\iota_a$ is given by:

::: center
$\iota_a=\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\epsilon_{\flat\gamma_1}\oplus\binampersand\omega\beta_1\ominus \binampersand\cdots$.
:::

A uniformity property holds for this map.
:::

::: demo
We proceed by transfinite induction on $l(a)\in\textbf{On}$. We have $\iota_0=\langle\emptyset\ |\ \emptyset\rangle=0$.\
Given a surreal number $a\in\textbf{No}$ with $l(a)>0$, we suppose that for any $b$ with $l(b)<l(a)$, $\iota_b$ is well defined, with the corresponding sign sequence. Consider a canonical representation $a=\langle a^L\ |\ a^R\rangle$ of $a$. For instance, in the case where $l(a)$ is a successor ordinal and $a=a^L\binampersand\oplus$. So $a^R<_sa^L$ et $a^R>a^L$. More precisely, either $a^L$ is only made of $\oplus$'s in which case $a^R=\emptyset$ (case (i)), or $a^R$ is a truncation of $a^L$, ending with a group of $\ominus$'s of $a^L$ of smaller number than the corresponding one in $a^L$ (case (ii)). In the case (i), the sign sequence formula of $\iota_a$ is:

::: center
$\begin{array}{lcl}
\iota_a&=&\langle \iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\ |\ \emptyset\rangle\\
&=&\langle \epsilon_{\flat(a^L)^+}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\ |\ \emptyset\rangle\\
&=&\epsilon_{\flat(a^L)^++1}\\
&=&\epsilon_{\flat a^+}
\end{array}$
:::

In the case (ii), denote by $a^L=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand\cdots\binampersand \alpha_\mu\oplus\binampersand \beta_\mu\ominus\binampersand\cdots$. So $a^R=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand\cdots\binampersand \alpha_\mu\oplus\binampersand \tilde{\beta}_\mu\ominus$ with $\tilde{\beta}_\mu<\beta_\mu$ (in $\textbf{On}$) for some $\mu\in\textbf{On}$. By the induction hypothesis, $\iota_{a^L}=\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\beta_\mu\ominus\binampersand\cdots<\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\tilde{\beta}_\mu\ominus=\iota_{a^R}$. So we obtain as desired $\iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)<\iota_{a^R}\binampersand n\ominus$ for any $n\in\mathbb{N}$. Moreover,

::: center
$\begin{array}{lcl}
\iota_a&=&\langle \iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\ |\ \iota_{a^R}\binampersand n\ominus\rangle\\
&=&\langle (\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\beta_\mu\ominus\binampersand\cdots) \binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\ |\ \\
&&\ \ \ \ \ (\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\tilde{\beta}_\mu\ominus)\binampersand n\ominus\rangle\\
&=&\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\beta_\mu\ominus\binampersand\cdots) \binampersand\epsilon_{\flat(a^L)^++1}\\
&=&\epsilon_{\flat\gamma_{0}}\oplus\binampersand\omega\beta_0\ominus \binampersand\cdots\binampersand\epsilon_{\flat\gamma_\mu}\oplus \binampersand\omega\beta_\mu\ominus\binampersand\cdots) \binampersand\epsilon_{\flat(a)^+}.
\end{array}$
:::

The other cases for $l(a)$ and $a$ are analogous. They are left to the reader as an exercise.\
Concerning the uniformity property, by the sign sequence formula for $\iota$, we note that for any surreal numbers $a,b\in\textbf{No}$, $a<b\Rightarrow\iota_a<\iota_b$. So the uniformity property follows from Theorem [\[theo:cofin\]](#theo:cofin){reference-type="ref" reference="theo:cofin"} in the same way as in [@gonshor_surreal Theorem 3.2, 3.5, Corollary au Theorem 5.2] and in Theorem [\[theo:kappa-defi\]](#theo:kappa-defi){reference-type="ref" reference="theo:kappa-defi"}.
:::

The main result of this section is:

::: thm
[]{#theo:kappa-signe label="theo:kappa-signe"}

1.  For any $a\in\textbf{No}$, $n\in\mathbb{N}$, we have $\kappa_{a,n},\ \kappa_{a,-n}\in\omega^{\omega^{\textbf{No}}}$. More precisely:

    ::: center
    $\begin{array}
    {lcl}
    \kappa_{a,n}&=&\omega^{\omega^{b}}\ \textrm{ with }\ b=\iota_a\binampersand n\ominus;\\
    \kappa_{a,-n-1}&=&\omega^{\omega^{b}}\ \textrm{ with }\ b=\iota_a\binampersand \Omega^n(\epsilon_{\flat a^+}+1)\oplus.
    \end{array}$
    :::

    In particular, $\kappa_a=\omega^{\omega^{\iota_a}}$.

2.  With the Notation [\[nota:gamma\]](#nota:gamma){reference-type="ref" reference="nota:gamma"}, for any $a\in\textbf{No}$, $n\in\mathbb{N}$, we have:

    ::: center
    $\begin{array}
    {lcl}
    \kappa_a&=&\omega^{\omega^{\epsilon_{\flat\gamma_{0}}}}\oplus\binampersand [(\omega^{\omega^{\epsilon_{\flat\gamma_{0}}}}\omega)^2\beta_0]\ominus \binampersand\epsilon_{\flat\gamma_1}\oplus\binampersand [(\epsilon_{\flat\gamma_{1}}\omega)^2\beta_1]\ominus\binampersand\cdots\ ;\\
    \kappa_{a,n}&=&\kappa_a\binampersand (\epsilon_{\flat a^+}\omega n)\ominus\ ;\\
    \kappa_{a,-n-1}&=&\kappa_a\binampersand (\Omega^{n+2}(\epsilon_{\flat a^+}+1)\oplus.
    \end{array}$
    :::
:::

The second point of the theorem follows directly from the first one and the sign sequences for the maps $\Omega$ (Theorem [\[theo:signe-omega\]](#theo:signe-omega){reference-type="ref" reference="theo:signe-omega"}) and $\iota$ (Lemma [\[lemme:iota\]](#lemme:iota){reference-type="ref" reference="lemme:iota"}). The first point will be deduced from the following lemma.

::: lem
[]{#lemme:h-iota label="lemme:h-iota"} For any $a\in\textbf{No}$ and any $\lambda\in\textbf{On}$, if we set $\lambda =\epsilon_\nu +\mu$ where $\epsilon_\nu$ is the unique epsilon number (possibly 0) such that $\epsilon_\nu<\lambda\leq \epsilon_{\nu+1}$, we have:

::: center
$\begin{array}
{lcl}
h(\iota_a\binampersand \lambda\ominus)&=&\omega^{\iota_a\binampersand(\lambda+1)\ominus} ;\\
h(\iota_a\binampersand \lambda\oplus)&=&\omega^{\iota_a}\binampersand \epsilon\oplus\binampersand\flat\mu\oplus\textrm{ avec }\lambda>0.
\end{array}$
:::
:::

::: demo
We proceed by transfinite induction on $(l(a),\lambda)\in \overrightarrow{\textbf{On}\times\textbf{On}}$ (the lexicographical product of $\textbf{On}$ with itself).\
Suppose that $l(a)=0$ i.e. $a=0$. By the definition of the map $h$ (see Theorem [\[theo:exp\]](#theo:exp){reference-type="ref" reference="theo:exp"} (2.)), we have $h(0)=\langle 0\ |\ 1/2^n\rangle=\omega^{-1}$.\
Moreover, $1=\oplus=\langle 0\ |\ \emptyset\rangle$. So:

::: center
$\begin{array}
{lcl}
h(\oplus)&=&\langle 0,h(0)\ |\ \omega/2^n\rangle\\
&=& \langle \omega^{-1}\ |\ \omega/2^n\rangle\\
&=&\langle \oplus\binampersand\omega \ominus\ |\ \omega\oplus\binampersand\par\noindent\ominus\rangle\textrm{ by the Theorem \ref{theo:signe-omega}}\\
&=& \oplus = \omega^0.
\end{array}$
:::

Consider now $(a,\lambda)\in\textbf{No}\times\textbf{On}$ with $\lambda>0$ in $\textbf{On}$. Suppose that the lemma holds for any $(b,\mu)\in\textbf{No}\times\textbf{On}$ with $(l(b),\mu)<_{lex}(l(a),\lambda)$ in $\overrightarrow{\textbf{On}\times\textbf{On}}$. We have $\iota_a\binampersand\lambda\ominus=\langle (\iota_a)^L\ |\ \iota_a\binampersand\mu\ominus\rangle$ with $\mu<\lambda$ in $\textbf{On}$. So, by the definition of $h$ and by the induction hypothesis:

::: center
$\begin{array}{lcl}
h(\iota_a\binampersand\lambda\ominus)&=&\langle 0,\ h((\iota_a)^L)\ |\ h(\iota_a\binampersand\mu\ominus),\ \omega^{\iota_a\binampersand\lambda\ominus}/2^n\rangle\\
&=& \langle 0,\ h(\iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus)\ |\ \omega^{\iota_a\binampersand(\mu+1)\ominus},\ \omega^{\iota_a\binampersand\lambda\ominus}/2^n\rangle\textrm{ (Lemma \ref{lemme:iota})}\\
&=& \langle 0,\ \omega^{\iota_{a^L}}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus\ |\ \omega^{\iota_a\binampersand\lambda\ominus}\binampersand(\epsilon_{\flat a+}n)\ominus\rangle\textrm{ by cofinality }\\
&=& \omega^{\iota_a\binampersand\lambda\ominus} \binampersand(\epsilon_{\flat a+}\omega)\ominus\\
&=& \omega^{\iota_a\binampersand(\lambda+1)\ominus}\textrm{ by Theorem \ref{theo:signe-omega}}.
\end{array}$
:::

We set $\lambda=\epsilon_\nu+\mu$ where $\epsilon_\nu<\lambda\leq \epsilon_{\nu+1}$. We have $\iota_a\binampersand\lambda\oplus=\iota_a\binampersand\epsilon_\nu\oplus\binampersand\mu\oplus= \langle\iota_a\binampersand\epsilon_\nu\oplus\binampersand\rho\oplus\ |\  (\iota_a)^R\rangle$ with $\rho<\mu$ in $\textbf{On}$. So, by the definition of $h$ and by the induction hypothesis:

::: center
$\begin{array}{lcl}
h(\iota_a\binampersand\lambda\oplus)&=&\langle 0,\ h(\iota_a\binampersand\epsilon_\nu\oplus\binampersand\rho\oplus)\ |\ h((\iota_a)^R),\ \omega^{\iota_a\binampersand\lambda\oplus}/2^n\rangle\\
&=& \langle 0,\ \omega^{\iota_a}\binampersand \epsilon_\nu\oplus\binampersand\flat\rho\oplus\ |\ h(\iota_{a^R}\binampersand n\ominus),\ \omega^{\iota_a\binampersand\lambda\oplus}/2^n\rangle\\
&=& \langle 0,\ \omega^{\iota_a}\binampersand \epsilon_\nu\oplus\binampersand\flat\rho\oplus\ |\ \omega^{\iota_{a^R}\binampersand(n+1)\ominus},\ \omega^{\iota_a\binampersand\lambda\oplus}/2^n\rangle\\
&&\ \ \textrm{ (note that }\iota_{a^R}\binampersand(n+1)\ominus>\iota_a\binampersand\lambda\oplus)\\
&=& \langle 0,\ \omega^{\iota_a}\binampersand \epsilon_\nu\oplus\binampersand\flat\rho\oplus\ |\ \omega^{\iota_{a^R}\binampersand(n+1)\ominus},\ \omega^{\iota_a}\binampersand(\epsilon_{\flat a^+}\omega^{\lambda})\oplus\binampersand (\epsilon_{\flat a^+}\omega^{\lambda}n)\ominus\rangle\\
&&\ \ \textrm{ (Theorem \ref{theo:signe-omega} and cofinality) }\\
&=& \omega^{\iota_a}\binampersand\epsilon\oplus\binampersand \flat\mu\oplus.
\end{array}$
:::

Consider now $a\in\textbf{No}$ with $l(a)>0$, and suppose that the lemma holds for any $(b,\mu)\in\textbf{No}\times\textbf{On}$ with $l(b)<l(a)$ in $\textbf{On}$. We have $\iota_a=\langle \iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus\ |\ \iota_{a^R}\binampersand n\ominus\rangle$ by Lemma [\[lemme:iota\]](#lemme:iota){reference-type="ref" reference="lemme:iota"}. So, by the definition of $h$ and the induction hypothesis, we have:

::: center
$\begin{array}{lcl}
h(\iota_a)&=&\langle 0,\ h((\iota_a)^L)\ |\ h((\iota_a)^R),\ \omega^{\iota_a}/2^n\rangle\\
&=& \langle 0,\ h(\iota_{a^L}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus)\ |\ h(\iota_{a^R}\binampersand n\ominus),\ \omega^{\iota_a}/2^n\rangle\textrm{ (Lemma \ref{lemme:iota})}\\
&=& \langle 0,\ \omega^{\iota_{a^L}}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus\ |\ \omega^{\iota_{a^R}\binampersand (n+1)\ominus},\ \omega^{\iota_a}\binampersand(\epsilon_{\flat a+}n)\ominus\rangle\textrm{ (Theorem \ref{theo:signe-omega})}\\
&=& \langle 0,\ \omega^{\iota_{a^L}}\binampersand\Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus\ |\ \omega^{\iota_a}\binampersand(\epsilon_{\flat a+}n)\ominus\rangle\textrm{ by cofinality }\\
&=& \omega^{\iota_a} \binampersand(\epsilon_{\flat a+}\omega)\ominus\\
&=& \omega^{\iota_a\binampersand\ominus}\textrm{ (Theorem \ref{theo:signe-omega})}.
\end{array}$
:::
:::

***Proof of Theorem [\[theo:kappa-signe\]](#theo:kappa-signe){reference-type="ref" reference="theo:kappa-signe"} (1.).*** $\ \ $ We proceed by tranfinite induction on $(l(a),n)\in\overrightarrow{\textbf{On}\times\mathbb{N}}$.

Suppose that $l(a)=0$, i.e. $a =0$. In the proof of the Theorem [\[theo:kappa-defi\]](#theo:kappa-defi){reference-type="ref" reference="theo:kappa-defi"}, we proved that $\kappa_0=\omega$. So $\kappa_0=\omega^{\omega^0}$ as desired.

Let $n\in\mathbb{N}^*$. We suppose that the property holds for any $(b,m)\in\textbf{No}\times\mathbb{N}$ with $(l(b),m)<(l(a),n)$. We have:

::: center
$\begin{array}{lcl}
\kappa_{a,n}&=&\log^n(\kappa_a)\\
&=&\log(\kappa_{a,n-1})\\
&=&\log(\omega^{\omega^{b}})\ \textrm{ with }\ b=\iota_{a}\binampersand(n-1)\ominus\\
&=& \omega^{h(\iota_{a}\binampersand(n-1)\ominus)}\textrm{ (Theorem \ref{theo:exp})}\\
&=& \omega^{\omega^{b}}\ \textrm{ with }\ b=\iota_{a}\binampersand n\ominus\textrm{ (Lemma \ref{lemme:h-iota})}\\
\end{array}$
:::

We also have:

::: center
$\begin{array}{lcl}
\kappa_{a,-1}&=&\exp(\kappa_a)\\
&=&\exp(\omega^{\omega^{\iota_{a}}})\\
&=& \omega^{\omega^{b}}\ \textrm{ with }\ b=g(\omega^{\iota_{a}})\textrm{ (Theorem \ref{theo:exp})}\\
&=& \omega^{\omega^{b}}\ \textrm{ with }\ b=\iota_{a}\binampersand\oplus\\
&&\ \ \textrm{ (Lemma \ref{lemme:h-iota} : }g(\omega^{\iota_{a}})=\iota_{a}\binampersand\oplus\Leftrightarrow \omega^{\iota_{a}}=h(\iota_{a})
\end{array}$
:::

and

::: center
$\begin{array}{lcl}
\kappa_{a,-n-1}&=&\exp^{n+1}(\kappa_a)\\
&=&\exp(\kappa_{a,-n})\\
&=&\exp(\omega^{\omega^{b}})\ \textrm{ with }\ b=\iota_{a}\binampersand\Omega^{n-1}(\epsilon_{\flat a^+}+1)\oplus\\
&=& \omega^{\omega^{b}}\ \textrm{ with }\ b=g(\omega^{\iota_{a}\binampersand\Omega^{n-1}(\epsilon_{\flat a^+}+1)\oplus}) \textrm{ (Theorem \ref{theo:exp})}\\
&=& \omega^{\omega^{b}}\ \textrm{ with }\ b=\iota_{a}\binampersand\Omega^{n}(\epsilon_{\flat a^+}+1)\oplus \textrm{ (Lemma \ref{lemme:h-iota})}\\
\end{array}$
:::

Consider $a\in\textbf{No}$ with $l(a)>0$, and suppose that the property holds for any $(b,m)\in\textbf{No}\times\mathbb{N}$ with $l(b)<l(a)$ and any $m\in\mathbb{N}$. By the definition of $\kappa$ (Theorem [\[theo:kappa-defi\]](#theo:kappa-defi){reference-type="ref" reference="theo:kappa-defi"}) and by the induction hypothesis, we have:

::: center
$\begin{array}{lcl}
\kappa_a&=&\langle \exp^n(0),\ \exp^n (\kappa_{a^L})\ |\ \log^n (\kappa_{a^R})\rangle\\
&=& \langle n,\ \omega^{\omega^{b}}\ |\ \omega^{\omega^{c}},\ \omega^{\iota_a}/2^n\rangle\ \textrm{ with }\ b=\iota_{a^L}\binampersand \Omega^n(\epsilon_{\flat(a^L)^+}+1)\oplus)\textrm{ and }c=\iota_{a^R}\binampersand n\ominus \\
&=&\omega^{\omega^{\iota_{a}}} \textrm{ (by cofinality and definition of }\iota\textrm{, Lemma \ref{lemme:iota})}\\
\end{array}$
:::

This finishes the proof of Theorem [\[theo:kappa-signe\]](#theo:kappa-signe){reference-type="ref" reference="theo:kappa-signe"}.$\Box$

::: rem
[]{#rem:gonshor label="rem:gonshor"}

1.  One can find in [@gonshor_surreal] partial results about these sign sequences. Indeed, for any $n\in\mathbb{N}$, any ordinal $\lambda\in\textbf{On}$, any epsilon-number $\epsilon_\mu$ with $\mu\in\textbf{On}$, we have:

    ::: center
    $\begin{array}{lcl}
    \log^n(\omega^{\omega^{\lambda\ominus}})&=&\omega^{\omega^{(\lambda+n)\ominus}}\textrm{ by \cite[Theorem 10.15]{gonshor_surreal}}\\
    \exp^n(\omega)&=&\Omega^{n+1}(1)\textrm{ by \cite[Theorem 10.14]{gonshor_surreal}}\\
    \exp^n(\epsilon_\mu)&=&\Omega^{n+1}(\epsilon_\mu+1)\textrm{ by \cite[Theorem 10.14]{gonshor_surreal}}\\
    \end{array}$.
    :::

2.  By the Theorems [\[theo:signe-omega\]](#theo:signe-omega){reference-type="ref" reference="theo:signe-omega"}, [\[theo:sign-seq-epsilon\]](#theo:sign-seq-epsilon){reference-type="ref" reference="theo:sign-seq-epsilon"} and [\[theo:kappa-signe\]](#theo:kappa-signe){reference-type="ref" reference="theo:kappa-signe"}, we have:

    ::: center
    $\epsilon_{\textbf{No}}\subsetneq \kappa_{\textbf{No}}\subsetneq\omega^{\omega^{\textbf{No}}} \subsetneq\omega^{\textbf{No}}\subsetneq\textbf{No}$.
    :::
:::
