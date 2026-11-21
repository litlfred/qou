---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-002-12-generalizations
section_title: "Generalizations"
section_number: 1.2
pages: 3-4
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#ss:gen label="ss:gen"}

Our aim is to generalize [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"} or its Poissonian version [\[eq:pois\]](#eq:pois){reference-type="eqref" reference="eq:pois"} in two ways. Instead of $S_n$ we consider arbitrary Lipschitz functions of $X_1 , \ldots , X_n$, and instead of independent Bernoullis we consider a more general negatively dependent collection of binary random variables. We will give a number of applications, but before this, we briefly discuss what is known about each of the two generalizations separately.

For the first generalization, let ${\mathcal B}_n$ denote the rank-$n$ Boolean lattice $\{ 0 , 1 \}^n$ and let $f : {\mathcal B}_n \to \mathbb{R}$ be Lipschitz with respect to the Hamming distance. Replacing $f$ by $f/c$ if necessary, we will lose no generality in assuming our Lipschitz functions to have Lipschitz constant 1, and we do so hereafter; thus $|f(x) - f(x')| \leq 1$ whenever $x$ and $x'$ are two strings differing in only one position. When ${\mathbb P}$ is a product measure, a well known generalization of [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"} [@mcdiarmid89] is $$\label{eq:gen 1}
{\mathbb P}(f - {\mathbb E}f \geq a) \leq e^{-2 a^2 / n} \, .$$

For the second generalization, we say that a collection of random variables $\{ X_j \}$ in $\{ 0 , 1 \}$ is **negative cylinder dependent** if $$\label{eq:cyl 1}
{\mathbb P}(X_j = 1 \mbox{ for all } j \in S) \leq \prod_{j \in S} p_j$$ and $$\label{eq:cyl 2}
{\mathbb P}(X_j = 0 \mbox{ for all } j \in S) \leq \prod_{j \in S} (1 - p_j) \, .$$

Negative cylinder dependence implies the inequalities [\[eq:chernoff\]](#eq:chernoff){reference-type="eqref" reference="eq:chernoff"}--[\[eq:two-sided\]](#eq:two-sided){reference-type="eqref" reference="eq:two-sided"} (see, e.g., [@panconesi-srinivasan Theorem 3.4] with $\lambda = 1$). Lyons [@lyons03 Section 6] lists extensions and applications including one to balls in bins [@dubhashi-ranjan] and one to determinantal measures [@soshnikov00].

It is not known whether these two generalizations can be combined. The random variables $\{ X_j \, : \, 1 \leq j \leq n \}$ are said to be **negatively associated** if ${\mathbb E}fg \leq ({\mathbb E}f) ({\mathbb E}g)$ for every pair $f,g$ of increasing functions on $\{ 0 , 1 \}^n$ such that $f (X_1 , \ldots , X_n)$ depends only on the values $\{ X_i : i \in S \}$ and $g (X_1 , \ldots , X_n)$ depends only on the values $\{ X_i : i \notin S \}$, for some subset $S \subseteq \{ 1 ,
\ldots , n \}$. By induction, this implies the weaker property of negative cylinder dependence. E. Mossel (personal communication, 2009) asked us whether the following holds.

::: conj
[]{#conj:both label="conj:both"} Let $X_1 , \ldots, X_n$ be negatively associated binary-valued random variables. Let $f : \{ 0,1 \}^n \to \mathbb{R}$ be Lipschitz-1 and denote $f_n := f(X_1 , \ldots , X_n)$. Then [\[eq:gen 1\]](#eq:gen 1){reference-type="eqref" reference="eq:gen 1"} holds with the bound $\exp (- 2 a^2 / n)$ replaced by $c_0 \exp (- c \, a^2 / n)$ for some positive constants $c_0$ and $c$.
:::

To see why the exponent must be weakened consider the example of Bernoulli random variables $X_1 , \ldots , X_n$ with $n$ even, $\{ X_1 , \ldots , X_{n/2} \}$ independent with mean $1/2$, and $X_{n/2 + j} = 1 - X_j$ for $1 \leq j \leq n/2$. These are negatively associated and yet the Lipschitz-1 function $f := \sum_{j=1}^{n/2} X_j - \sum_{j=n/2+1}^n X_j$ has tail probabilities on the order of $e^{- a^2 / n}$. It is possible that this is the worst example and that the conjecture holds with $c=1$, but a resolution of the conjecture would be interesting even without the optimal value of $c$. A recent paper [@farc08] appears to settle this conjecture and more, but the relevant result in that paper, Theorem 2, is not correct, the proof therein failing at equation (6).

Recent investigations of negative dependence properties indicate that negative association may not be sufficiently robust to use as a hypothesis in this context. The problem was posed in [@pemantle-NA] to find a more useful negative dependence property; this was answered in [@borcea-branden-liggett], who showed that the **strong Rayleigh property** implies negative association and many other desirable consequences, and is stable under probabilistic operations such as conditioning, symmetrizing and reweighting.

Our main result implies that Conjecture [\[conj:both\]](#conj:both){reference-type="ref" reference="conj:both"} holds with $c = 1/8$ if one assumes the strong Rayleigh property rather than just negative association. The strong Rayleigh property is known to hold for most standard examples in which negative association is known to hold, so this gives up little generality, and moreover the strong Rayleigh property is usually easier to check than is negative association. Indeed for some of the measures described below, the only way we know they are negatively associated is by establishing the strong Rayleigh property. Several classes of measures satisfying the strong Rayleigh property are:

-   Determinantal measures and point processes;

-   Bernoullis conditioned on the sum;

-   Measures obtained by running exclusion dynamics from a deterministic starting state (or more generally, exclusion with birth and death).

An overview of the rest of the paper is as follows. In the next section we introduce the strong Rayleigh property and discuss its consequences. One important consequence for us will be the **stochastic covering property**, which is all we use to derive our basic concentration inequality. In Section [\[sec:results\]](#sec:results){reference-type="ref" reference="sec:results"} we state our results, and these are proved in Section [\[sec:proofs\]](#sec:proofs){reference-type="ref" reference="sec:proofs"}. Section [\[sec:examples\]](#sec:examples){reference-type="ref" reference="sec:examples"} contains a number of applications.
