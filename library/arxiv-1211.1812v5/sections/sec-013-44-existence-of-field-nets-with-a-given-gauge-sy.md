---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-013-44-existence-of-field-nets-with-a-given-gauge-sy
section_title: "Existence of field nets with a given gauge symmetry."
section_number: 4.4
pages: 26-28
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.995
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.free label="sec.free"} The following construction is on the line [@DP02], where similar results are proven for the Minkowski spacetime. We prove that for every suitable compact group $G_0$, globally hyperbolic spacetime $M$ and flat bundle $\mathcal G\to M$ with suitable structure group, there is a twisted field net over which $\mathcal G$ acts as a group of internal symmetries. The \"untwisted\" net from which we start is defined by means of generalized free fields and yields a large class of toy models where the analysis of topologically trivial superselection sectors of [@GLRV01; @Ruz05] can be checked, as happens for [@DP02] in the Minkowski spacetime.

In the sequel we shall consider a ${\mathbb Z}_2$-graded group $(G_0,\gamma)$, not necessarily realized on a Hilbert space, where $G_0$ is compact and metrizable.

Let $\lambda$ be a symmetric and separating set

[^1]

of irreducible subrepresentations of the regular representation of $G_0$. We consider the corresponding Hilbert space

$$L_\lambda := \oplus_{\varrho \in \lambda} L_\varrho \ \subset L^2(G_0)$$

on which $G_0$ acts by means of the faithful unitary representation

$$\label{def.rep}
G_0 \to UL_\lambda
\ \ , \ \
g \mapsto g_\lambda := \oplus_\varrho g_\varrho
\ ,$$

where any $g_\varrho$ is a unitary acting on the irreducible, finite dimensional $G_0$-Hilbert space $L_\varrho$. The grading element $\gamma$ induces the spectral decomposition

$$L_\lambda = L_\lambda^+ \oplus L_\lambda^- \ ,$$

which decomposes ([\[def.rep\]](#def.rep){reference-type="ref" reference="def.rep"}) into

$$\label{def.rep.pm}
G_0 \to UL_\lambda^\pm
\ \ , \ \
g \mapsto g_\lambda^\pm := \oplus_{\varrho(\gamma) = \pm 1} g_\varrho \ .$$

Finally, we consider a real structure (that is, an antilinear, isometric map)

$J : L_\lambda^+ \to L_\lambda^+$, $J^2 = 1$,

commuting with ([\[def.rep\]](#def.rep){reference-type="ref" reference="def.rep"}) and stabilizing the subspaces $L_\varrho$ for any $\varrho \in \lambda$ with $\varrho(\gamma) = 1$, so that we have real structures

$J_\varrho : L_\varrho \to L_\varrho$.

We denote the *real* subspace of $J$-invariant vectors in $L_\lambda^+$ by $L_\lambda^{+,J}$, which is a real Hilbert space with the scalar product induced by $L_\lambda^+$.

Now, we say that a compactly supported $f : M \to L_\lambda^{+,J}$ is $C^\infty$ whenever the function

$f_v(x) := ( f(x),v ) \in {\mathbb R}$, $x \in M$,

is $C^\infty$ for any $v \in L_\lambda^{+,J}$, and denote the corresponding real vector space by $C^\infty_c(M,L_\lambda^{+,J})$.

Given the decomposition

$f(x) = \{ f_\varrho(x) \in L_\varrho \}$, $x \in M$,

we define the real vector space

$$\mathcal D^+ \ := \ 
\{ f \in C^\infty_c(M,L_\lambda^{+,J}) \ : \
   f_\varrho \neq 0 \ {\mathrm{for \ finite \ }} \varrho \in \lambda  \} \ .$$

The representation ([\[def.rep\]](#def.rep){reference-type="ref" reference="def.rep"}) induces an action by invertible linear maps,

$$\label{eq.CON0a}
G_0 \to GL \mathcal D^+
\ \ : \ \
f_g(x) := g_\lambda^+ f(x)
\ \ , \ \qquad
\forall f \in \mathcal D^+ \ , \ g \in G_0 \ , \ x \in M \ .$$

Now, let us suppose that $M$ has a spin structure (this is guaranteed for 4-dimensional globally hyperbolic spacetimes, see [@Ish78] and related references). We consider the spinor bundle $DM \to M$ (with fibre ${\mathbb C}^4$), whose tensor product by $L_\lambda^-$ yields the bundle of Hilbert spaces

$D_\lambda^- M \to M$, $D_\lambda^- M := L_\lambda^- \otimes DM$.

We have the direct sum decomposition

$$D_\lambda^- M \ \simeq \ \oplus_{\varrho(\gamma)=-1} D_\varrho M 
\ ,$$

where any $D_\varrho M := L_\varrho \otimes DM \to M$ is a *smooth* vector bundle. Any section $s : M \to D_\lambda^- M$ decomposes as

$s = \{ s_\varrho : M \to D_\varrho M \}$,

and we say that $s$ is $C^\infty$ whenever every $s_\varrho$ is a $C^\infty$ section. We denote the set of compactly supported, $C^\infty$ sections of $D_\lambda^-M$ by $\mathcal S^\infty_c(M,D_\lambda^-M)$ and define

$$\mathcal D^- \ := \ 
\{ s \in \mathcal S^\infty_c(M,D_\lambda^-M) \ : \
   s_\varrho \neq 0 \ {\mathrm{for \ finite \ }} \varrho \in \lambda \} \ ,$$

that is a complex vector space with action

$$\label{eq.CON0b}
G_0 \to GL \mathcal D^-
\ \ : \ \
s_g(x) := \{ g_\lambda^- \otimes 1 \} s(x)
\ \ , \ \
\forall s \in \mathcal D^- \ , \ g \in G_0 \ , \ x \in M \ .$$

::: lem
[]{#lem.gauge2 label="lem.gauge2"} For any globally hyperbolic (spin) manifold $M$ and ${\mathbb Z}_2$-graded group $(G_0,\gamma)$, there are a Hilbert space $H_*$ with a faithful, strongly continuous representation

$\tau : G_0 \to UH_*$,

and a normal $( \tau(G_0),\tau(\gamma) )$-net of von Neumann algebras $\EuFrak{F}_*$ on $H_*$.
:::

The proof of the previous Lemma is postponed to §[\[app.sym\]](#app.sym){reference-type="ref" reference="app.sym"} and is based on the construction of a symplectic form on $\mathcal D^+$ and a scalar product on $\mathcal D^-$, that allow us to define, respectively,

-   a selfadjoint Klein-Gordon field $\phi(f)$, $f \in \mathcal D^+$, on the Hilbert space $H_*^\phi$,

-   a Dirac field $\psi(s)$, $s \in \mathcal D^-$, on the Hilbert space $H_*^\psi$,

and then define $H_* := H_*^\phi \otimes H_*^\psi$ and $F_{*,a}$, $a \in \Delta$, as the von Neumann algebra generated by

$$\{ e^{i \phi(f)} \otimes 1_\psi \ , \ 1_\phi \otimes \psi(s) \ : \ 
   f \in \mathcal D^+ \ , \ s \in \mathcal D^- \ , \ {\mathrm{supp}} \, (f) \, , \, {\mathrm{supp}} \, (s) \subseteq a \} \ .$$

We now define the (compact) normalizer group

$$N^\lambda G_0 \ := \ \{ V = \oplus_\varrho V_\varrho \in UL_\lambda \ : \ 
                        V_\varrho g_\varrho V_\varrho^* \in \varrho(G_0) \ , \ \forall g \in G_0  \} \ .$$

Note that $N^\lambda G_0$ acts by adjoint action on $G_0$ and, since $\gamma_\varrho = \pm 1$ for any $\varrho \in \lambda$, we have

$$V \gamma_\lambda V^* = \gamma_\lambda \ \ , \ \ \forall V \in N^\lambda G_0 \ .$$

Moreover, any $V \in N^\lambda G_0$ splits as $V = V^+ \oplus V^-$, $V^\pm \in UL_\lambda^\pm$.

::: thm
[]{#thm.gauge1 label="thm.gauge1"} Let $M$ denote a globally hyperbolic (spin) manifold and $(G_0,\gamma)$ a ${\mathbb Z}_2$-graded group. Given a symmetric, separating set $\lambda$ for $G_0$ and a morphism

$$\chi : \pi_1(M) \to N^\lambda G_0 \ ,$$

there is a ${\mathbb Z}_2$-graded net of *C\**-algebras $\EuFrak{F}= (F,\jmath)_\Delta$ endowed with:

1.  A Hilbert net bundle $(H,U)_\Delta$ carrying a normal representation $(\pi,U)$ of $\EuFrak{F}$;

2.  A gauge action $\EuFrak{G}\times_\Delta \pi(\EuFrak{F}) \to \pi(\EuFrak{F})$ with fixed-point net $\EuFrak{R}$ causally represented on $(H,U)_\Delta$, where $\EuFrak{G}= (G, \hat \imath)_\Delta$ is the group net bundle with fibre $G_0$ and holonomy ${\mathrm{ad}}\chi$.
:::

::: proof
*Proof.* With the notation of the previous Lemma we define $G_* := \tau(G_0) \subset UH_*$. So $(G_*,\tau(\gamma))$ is a ${\mathbb Z}_2$-group on $H_*$, and by the previous Lemma we have a normal $(G_*,\tau(\gamma))$-net of von Neumann algebras $\EuFrak{F}_*$ on $H_*$. Now, by Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"}, to prove the Theorem it suffices to show that the unitary representation $\tau$ of the previous Lemma extends to a unitary representation $\tau$ of $N^\lambda G_0$ taking values in $N_{\tau(\gamma)} G_*$, in fact in such a case we would have the morphism

$\tau \circ \chi : \pi_1(M) \to N_{\tau(\gamma)} G_*$.

But the construction of the desired representation is easy, in fact it suffices to define the actions

$$\left\{
\begin{array}{ll}
f_V(x) := V^+ f(x)
\ , \
\forall x \in M
\ , \
f \in \mathcal D^+

\\

s_V(x) := \{ V^- \otimes 1 \} s(x)
\ , \
\forall x \in M
\ , \
s \in \mathcal D^-
\end{array}
\right.
\ \ , \ \
V \in N^\lambda G_0 \ ,$$

that yield, by universality of the CCRs and CARs, the desired extension $\tau$ fulfilling

$$\tau_V \{ e^{i \phi(f)} \otimes 1_\psi \} \tau_V^* \ = \ e^{i \phi(f_V)} \otimes 1_\psi 
\ \ , \ \
\tau_V \{ 1_\phi \otimes \psi(s) \} \tau_V^* \ = \  1_\phi \otimes \psi(s_V)
\ .$$

The verifications that $\tau(N^\lambda G_0) \subseteq N_{\tau(\gamma)} G_*$ now are trivial (see ([\[def.NG\]](#def.NG){reference-type="ref" reference="def.NG"})) and the Theorem is proved. ◻
:::

[^1]: With *symmetric* we mean that if $\varrho \in \lambda$ then the same is true for the conjugate representation $\overline\varrho$, whilst the term *separating* indicates that for any $g \neq g' \in G_0$ there is $\varrho \in \lambda$ such that $\varrho(g) \neq \varrho(g')$.
