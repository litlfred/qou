---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-008-31-theta-functions
section_title: "Theta Functions"
section_number: 3.1
pages: 14-16
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.919
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:thetafunctions label="subsection:thetafunctions"}

Jacobi theta functions pervade the theory of $q$-difference equations. We shall mostly have use for two slightly different forms of them.\
In chapter [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"}, we shall use: []{#not6 label="not6"} $$\label{eqn:tripleproduit}
\theta(z;q) := \sum_{n\in{\mathbf Z}} q^{-n(n-1)/2} z^n =
\prod_{n\in{\mathbf N}}(1 - q^{-n-1})(1 + q^{-n} z)(1 + q^{-n-1}/z).$$ The second equality is Jacobi's celebrated triple product formula. When obvious, the dependency in $q$ will be omitted and we shall write $\theta(z)$ instead of $\theta(z;q)$. One has: $$\theta(qz) = q~z~\theta(z) \text{~and~} \theta(z) = \theta(1/q z).$$

In chapter [\[chapter:geometryofF(M)\]](#chapter:geometryofF(M)){reference-type="ref" reference="chapter:geometryofF(M)"}, we shall rather use: []{#not7 label="not7"} $$\label{eqn:thq}
{\theta_{q}}(z) := \sum_{n \in {\mathbf Z}} q^{-n(n+1)/2} z^{n} 
        = \prod_{n\in{\mathbf N}}(1 - q^{-n-1})(1 + q^{-n-1} z)(1 + q^{-n}/z).$$ One has of course ${\theta_{q}}(z) = \theta(q^{-1}z;q)$ and: $${\theta_{q}}(q z) = z {\theta_{q}}(z) = {\theta_{q}}(1/z).$$ Both functions are analytic over the whole of ${\mathbf C}^*$ and vanish on the discrete $q$-spiral $- q^{{\mathbf Z}}$ with simple zeroes.\
In chapter [\[chapter:examplesStokes\]](#chapter:examplesStokes){reference-type="ref" reference="chapter:examplesStokes"}, we shall use in alternance both forms, according to which fits better the needs of the computation. Indeed, in section [\[section:QuadForms\]](#section:QuadForms){reference-type="ref" reference="section:QuadForms"}, we shall even use the "classical" forms $\theta_{i,j}$, $i,j \in \{0,1\}$ to be found in the standard theory of special functions.

## $q$-Gevrey levels {#subsection:qGevreylevels}

As in [@Bezivin],[@RamisGrowth], we introduce the space of formal series of *$q$-Gevrey order $s$*: $${{{\mathbf C}[[z]]}_{q;s}}:= \left\{\sum a_{n} z^{n} \in {{\mathbf C}[[z]]}~ | ~
\exists A > 0 ~:~ a_{n} = O\left(A^{n} q^{s n^{2}/2}\right)\right\}.$$ We also say that $f \in {{{\mathbf C}[[z]]}_{q;s}}$[]{#not8 label="not8"} is of *$q$-Gevrey level $1/s$*. It understood that ${{\mathbf C}[[z]]}_{q;0} = {{\mathbf C}\{z\}}$ and ${{\mathbf C}[[z]]}_{q;\infty} = {{\mathbf C}[[z]]}$. Note however that it is *not* true that $\bigcap\limits_{s > 0} {{\mathbf C}[[z]]}_{q;s} = {{\mathbf C}\{z\}}$, as shows the example of the classical Euler series $\sum n! z^n$, which belongs to the former but not to the later (and the same is true for any divergent series having a finite Gevrey level in the sense of the classical theory of ordinary differential equations); nor that $\bigcup\limits_{s > 0} {{\mathbf C}[[z]]}_{q;s} = {{\mathbf C}[[z]]}$, as shows the example of $\sum n^n z^n$, which belongs to the latter but not to the former.\
Similar considerations apply to spaces of Laurent formal series: $${{{\mathbf C}((z))}_{q;s}}:= {{{\mathbf C}[[z]]}_{q;s}}[1/z].$$ More generally, one can speak of $q$-Gevrey sequences of complex numbers. Let $k \in {\mathbf R}^* \cup \{\infty\}$ and $s := \dfrac{1}{k}$. A sequence $(a_n) \in {\mathbf C}^{{\mathbf N}}$ is *$q$-Gevrey of order $s$* if it is dominated by a sequence of the form $\left(C A^n \left |q \right |^{n^2/(2k)}\right)$, for some constants $C,A > 0$.\
Note that this terminology is all about sequences, or coefficients of series. Extension to $q$-Gevrey asymptotics is explained in definition [\[defi:ALambda\]](#defi:ALambda){reference-type="ref" reference="defi:ALambda"}, while the $q$-Gevrey interpolation by growth of decay of functions is dealt with in definitions [\[defi:LambdaF\]](#defi:LambdaF){reference-type="ref" reference="defi:LambdaF"} and [\[defi:diviseurrelatif\]](#defi:diviseurrelatif){reference-type="ref" reference="defi:diviseurrelatif"}.
