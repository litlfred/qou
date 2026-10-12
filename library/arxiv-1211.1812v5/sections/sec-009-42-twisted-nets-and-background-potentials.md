---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-009-42-twisted-nets-and-background-potentials
section_title: "Twisted nets and background potentials."
section_number: 4.2
pages: 23-28
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.993
---
[]{#rem.qed label="rem.qed"}

We show how a class of twists arises when a quantum field interacts with a *classical* background potential. We start by assuming that $M$ is a globally hyperbolic spin manifold and consider the free Dirac field $\psi_*$ interacting with a (classical) closed 1--form $A \in Z^1_{deRham}(M)$.

To this end we extract some informations from $A$. A first point is that, since $A$ is closed, for any loop $\ell : [0,1] \to M$ the integral

$\int_\ell A$

is independent of the choice of $\ell$ in its homotopy class, thus we obtain the character

$$\label{eq,A0}
\zeta_A : \pi_1(M) \to {\mathbb T}\ \ , \ \ \zeta_A([\ell]) \, := \, \exp 2\pi i \int_\ell A \ .$$

Moreover, since any diamond $o \in \Delta$ is simply connected there is a local primitive $\phi_o \in C^\infty(o,{\mathbb R})$ such that $A|_o = d\phi_o$, and we have

$$\phi_{o'} |_o - \phi_o \, = \, \Lambda_{o'o} \in {\mathbb R}
\ \ \Rightarrow \ \ 
\Lambda_{o''o'} + \Lambda_{o'o} \, = \, \Lambda_{o''o}
\ , \ 
\forall o \subseteq o' \subseteq o'' \in \Delta
\ .$$

Let now $b \in \Sigma_1(\Delta)$ and $\beta : [0,1] \to |b| \subset M$ such that $\beta(0) \in \partial_1b$, $\beta(1) \in \partial_0b$. Then

$$\int_\beta A \, = \, 
\int_\beta d\phi_{|b|} \, = \, 
\phi_{|b|}(\beta(1)) - \phi_{|b|}(\beta(0)) \, = \, 
\phi_{\partial_0b}(\beta(1)) - \phi_{\partial_1b}(\beta(0)) + \Lambda_b \ ,$$

where

$\Lambda_b \, := \, \Lambda_{|b|\partial_0b} - \Lambda_{|b|\partial_1b}$.

Note that the family $\Lambda = \{ \Lambda_b \}$ is a cocycle and it can be verified that it encodes the cohomology class of $A$ (see [@RRV08 §3]). In particular the holonomy of $A$ can be reconstructed as follows. Let $a \in \Delta$ and

$p : a \to a$, $p = b_n * \ldots * b_1$;

then using the isomorphism ([\[eq.back1\]](#eq.back1){reference-type="ref" reference="eq.back1"}) we have a homotopy class $[p] \in \pi_1(M)$ containing a loop

$\ell : [0,1] \to M$, $\ell = \beta_n * \ldots * \beta_1$,

where each curve $\beta_k$, $k=1,\ldots,n$, fulfils the above properties with respect to $b_k \in \Sigma_1(\Delta)$ (see [@Ruz05 §2.5.1]). Thus, iterating the previous equality, we obtain

$$\label{eq.A}
\int_\ell A \, = \, 
\sum_k \int_{\beta_k} A \, = \, 
\sum_k \Lambda_{b_k} 
\ .$$

We now define a net by means of the family $\phi$ and the free Dirac field. To this end we consider the spinor bundle $DM \to M$, the space $S^\infty_c(M,DM)$ of compactly supported, $C^\infty$-sections of $DM$ (spinors), and, for any $o \in \Delta$, the space $\mathcal S^\infty_o(M,DM)$ of spinors supported within $o \in \Delta$. We note that we can define the product

$$e^{2\pi i\phi_o} s \, \in S^\infty_o(M,DM)
\ \ , \ \ 
\forall o \in \Delta \ , \ s \in \mathcal S^\infty_o(M,DM) \ .$$

Let us consider the free Dirac field

$\psi_* : \mathcal S^\infty_c(M,DM) \to BH_*$

in the sense of [@Dim82]. For any $o \in \Delta$ we define the operator-valued distribution

$$\psi_o : \mathcal S^\infty_o(M,DM) \to BH_*
\ \ , \ \ 
\psi_o(s) \, := \, \psi_*( e^{2\pi i\phi_o} s )
\ .$$

Clearly, defining the field $\psi_o$ corresponds to considering the local gauge transformation

$$\psi_*(x) \, \to \, e^{2\pi i\phi_o(x)}\psi_*(x) \ \ , \ \ x \in o \ ,$$

which yields in $o$ a solution for the Dirac equation with interaction given by $A$. The net of von Neumann algebras $\EuFrak{F}_* = (F,\jmath_*) \subset BH_*$,

$$F_o \, := \, \{ \psi_o(s) \, : \, s \in \mathcal S^\infty_o(M,DM) \}'' \subset BH_* \ \ , \ \ o \in \Delta \ ,$$

coincides with the one defined by $\psi_*$, thus at a first stage $\EuFrak{F}_*$ does not seem to preserve informations on the potential $A$; but, in the following lines, we shall show that this is not the case.

We consider global gauge transformations

$\alpha_z(\psi_o(s))  :=  z \psi_o(s)$, $s \in \mathcal S^\infty_o(M,DM)$, $z \in {\mathbb T}$,

that are unitarily implemented in the fermionic Fock space $H_*$ by universality of the CARs,

$$\label{eq.gdirac}
\alpha_z(\psi_o(s)) \, = \, V_z \psi_o(s) V_z^* \ \ , \ \ \forall z \in {\mathbb T}\ ,$$

and set $G_* := \{ V_z , z \in {\mathbb T}\} \subset UH_*$ with grading element $\gamma = V_{-1}$. This yields the observable subnet

$\EuFrak{R}_* = (R,\jmath_*)_\Delta$, $R_o = F_o \cap G_*'$, $o \in \Delta$.

Now, for any $o \subseteq o'$ we consider the map

$$\jmath_{o'o}(\psi_o(s)) \, := \, 
\psi_{o'}(s) \, = \, 
\psi_*( e^{2\pi i (\phi_o + \Lambda_{o'o}) }s ) \, = \, 
e^{2\pi i \Lambda_{o'o}} \psi_o(s)
\ \ , \ \
s \in \mathcal S^\infty_o(M,DM)
\ .$$

By universality, any $\jmath_{o'o}$ extends to a \*-monomorphism $\jmath_{o'o} : F_o \to F_{o'}$ and we obtain a net $\EuFrak{F}= (F,\jmath)_\Delta$. A natural representation of $\EuFrak{F}$ can be constructed as follows: we define the Hilbert net bundle $\EuFrak{H}= (H,U)_\Delta$,

$$H_o \equiv H_* \ \ , \ \ U_{o'o} \, := \, V_{ \exp 2\pi i \Lambda _{o'o} } \ \ , \ \ \forall o \subseteq o' \ ,$$

and then note that, by ([\[eq.gdirac\]](#eq.gdirac){reference-type="ref" reference="eq.gdirac"}),

$$\jmath_{o'o}(t) \, = \, 
\alpha_{ \exp 2\pi i \Lambda _{o'o} }(t) \, = \,
U_{o'o} \, t \, U_{o'o}^* 
\ \ , \ \ 
\forall o \subseteq o' \ , \ t \in F_o \ .$$

The holonomy of $\EuFrak{H}$ is easily computed using ([\[eq,A0\]](#eq,A0){reference-type="ref" reference="eq,A0"}) and ([\[eq.A\]](#eq.A){reference-type="ref" reference="eq.A"}):

$$U_p \, = \, \prod_k V_{\exp 2\pi i \Lambda _{b_k}} \, = \, V_{\zeta_A([\ell])} \in G_*
\ \ , \ \ 
\ell \in [p] \in \pi_1(M)
\ .$$

Thus $\EuFrak{F}$ is a twisted net faithfully represented in the Hilbert net bundle $\EuFrak{H}= (H,U)_\Delta$. Performing a parallel displacement around the loop $p : a \to a$ yields a phase factor affecting the charged field operators,

$$\label{eq.AB2}
{\mathrm{ad}}U_p(\psi_a(s)) \, = \, \zeta_A([\ell]) \, \psi_a(s) \, = \, \exp 2\pi i \int_\ell A \, \cdot \, \psi_a(s)
\ \ , \ \
\ell \in [p] \in \pi_1(M)
\ .$$

Thus, if $v_0 \in H_*$ is the vacuum, then the relative phase $\exp 2\pi i \int_\ell A$ appears between the states $\psi_a(s)v_0$, $U_p \psi_a(s) v_0 \in H_*$ (we use the notation in which $\psi_a(s)$ is defined by the creation operator).

To give an example we parametrize ${\mathbb R}^4$ by the coordinates $x_0 , x_1 , x_2 , x_3$ and define $M = {\mathbb R}^4 - S_\delta$, where $S_\delta$ is the closed tube centered around the axis $x_3$ and having ray $\delta > 0$. The base $\Delta$ is given by the one of double cones contained in $M$, which generates a nontrivial topology in the sense that

$\pi_1(\Delta) \simeq \pi_1(M) \simeq {\mathbb Z}$

(note that $M$ is homotopic to $S^1$).

We consider a vector potential $A' \in \Omega^1({\mathbb R}^4)$ such that $F := dA' \in \Omega^2({\mathbb R}^4)$ is supported within $S_\delta$.

Note that this scenario is modeled in such a way to obtain a situation analogous to the one of the Aharonov-Bohm effect, see [@Fey §15.5]. We can always find such 1--forms $A'$ by starting from $F \in \Omega^2({\mathbb R}^4)$ fulfilling the above property and defining $A'$ as a primitive of $F$.

As a final step we define $A \in \Omega^1(M)$, $A := A'|_M$. In this way, the previous hypothesis say that $A$ is closed and we can apply the previous construction, that gives rise to the phase factor ([\[eq.AB2\]](#eq.AB2){reference-type="ref" reference="eq.AB2"}). This last coincides with the phase affecting the wavefunctions of electrically charged particles in the Aharonov-Bohm effect (see [@Fey Eq.15.33]).

## Current algebras on $S^1$. {#sec.BMT}

We now apply Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"} to current algebras on $S^1$ defined as in the approach of Buchholz-Mach-Todorov ([@BMT1; @BMT2]); here, at a first stage, fields fulfilling braided commutation relations appear, anyway after a \"bosonization\" procedure a causal field net is constructed. For a complete discussion of the model we refer the reader to the above-cited references; here we limit ourselves to give the basic definitions, needed to see how Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"} applies.

The base $\Delta$ of $S^1$ is the one of intervals with proper closure, and we write $o \perp w \Leftrightarrow o \cap e = \emptyset$.

We take a fixed $n \in {\mathbb N}$ (with no squares in the factor decomposition, see the above-cited references), parametrize $S^1$ with complex numbers of modulus $1$, and for every $o \in \Delta$ consider the space

$$\label{eq.BMT0}
\mathcal V^n_o \, := \, 
\{ \, q \in C^\infty(S^1,{\mathbb C}) \, : \, {\mathrm{supp}}(q) \subseteq o \, , \, 
                                   zq(z) \in {\mathbb R}, \forall z \in S^1 \, , \, 
                                   
                                   \oint \frac{1}{2\pi i} \, q(z) \, dz \, = \sqrt{2n} \, \}
\, .$$

Here every $q \in \mathcal V^n_o$ is interpreted as a charge distribution supported within $o \in \Delta$, see [@BMT1 Eq.2.24]. A field net $\EuFrak{F}^n_* = (F^n,\jmath)_\Delta \subset BH_*$ is defined, with local von Neumann algebras

$$F^n_o \, = \, \{  \phi_q \in UH_* \, : \, q  \in \mathcal V^n_o \}'' \ \ , \ \ o \in \Delta \ ,$$

see [@BMT1 Eq.4.93] and the following remarks. The net $\EuFrak{F}^n_*$ is bosonic in the sense that $[ \phi_q , \phi_{q'} ] = 0$ whenever $\phi_q \in F_o$, $\phi_{q'} \in F_e$ with $o \perp e$, see the discussion after [@BMT1 Eq.4.82]. There is a gauge group $G_* \simeq {\mathbb Z}_{2n}$ generated by a unitary

$$V \, = \, e^{2\pi i (2n)^{-1/2} Q} \in UH_* \ \ : \ \ V^{2n} = 1 \ ,$$

on which we define the grading element $\gamma = 1$; in the previous expression $Q$ denotes an unbounded operator on $H_*$ affiliated with the von Neumann algebra generated by $F^n$, see [@BMT1 Eq.4.40], which is interpreted as the charge. We have

$$\label{eq.BMT1}
V \phi_q V^* \, = \, e^{i\pi / n} \phi_q
\ \ , \ \ 
\forall o \in \Delta \ , \ q \in \mathcal V^n_o
\ ,$$

see [@BMT1 Eq.4.94]. We can apply Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"} with morphisms of the form

$$\chi : {\mathbb Z}\simeq \pi_1(S^1) \to G_* \ ,$$

that are determined by the choice of $\chi(1)$ that must be of the type $\chi(1) = V^\kappa$, $\kappa \in \{ 1 , \ldots , 2n-1 \}$. As a consequence of Cor.[\[cor.gauge1\]](#cor.gauge1){reference-type="ref" reference="cor.gauge1"}, the twisted net $\EuFrak{F}$ defined by $\chi$ has observable net isomorphic to the untwisted net $\EuFrak{R}^n_* = (R^n,\jmath)_\Delta$ generated by operators in $\EuFrak{F}^n_*$ commuting with $V$. We note that $V$ is, indeed, a central element of the von Neumann algebra $\vec{R}^n \subset BH_*$ generated by the family $R^n$, see [@BMT1 Eq.4.90]. Any $\phi_q$ defines a localized automorphism of $\vec{R}^n$,

$$\gamma_q \, := \, {\mathrm{ad}}\phi_q 
\ \ , \ \
\gamma_q(t) = t \, , \, \forall t \in R_e \, , \, e \perp {\mathrm{supp}}(q) \ .$$

Passing to the twisted net $\EuFrak{F}^n$ we have a representation $\pi : \EuFrak{F}^n \to \EuFrak{B}\EuFrak{H}$, where $\EuFrak{H}= (H,U)_\Delta$ is the Hilbert net bundle with fibres $H_o \equiv H_*$, $o \in \Delta$, defined as in Lemma [\[lem.gauge1\]](#lem.gauge1){reference-type="ref" reference="lem.gauge1"},

$$\pi_o : F^n_o \to BH_* \ \ , \ \ {\mathrm{ad}}U_{o'o} \circ \pi_o \,= \, \pi_{o'}|_{F^n_o} \ \ , \ \ \forall o \subseteq o' \ ;$$

here any $\pi_o$ is the inclusion map $F^n_o \to BH_*$, thus in the sequel it will be dropped from the notation. It is instructive to exhibit the effect of the parallel displacement along a loop on the charged fields. To this end, to fix the ideas we take $\kappa = 1$, that means $\chi(1) = V$. Given $a \in \Delta$, the homotopy class of any loop $p : a \to a$ is labelled by an integer $[p] \in {\mathbb Z}$, thus

$${\mathrm{ad}}U_p(\phi_q) \, = \, V^{[p]} \phi_q V^{[p],*} \, = \, e^{i\pi [p] / n} \phi_q 
\ \ , \ \ 
\forall \phi_q \in F^n_a
\ ,$$

and a relative phase appears between the charged field and its parallel displacement. We note that the interpretation of ${\mathrm{ad}}U_p(\phi_q)$ as the displacement of the field operator $\phi_q$ inducing the DHR automorphism $\gamma_q$ is in accord with the standard formulation of charge transporters, see [@Rob0 §3.4.5].

## Existence of field nets with a given gauge symmetry. {#sec.free}

The following construction is on the line [@DP02], where similar results are proven for the Minkowski spacetime. We prove that for every suitable compact group $G_0$, globally hyperbolic spacetime $M$ and flat bundle $\mathcal G\to M$ with suitable structure group, there is a twisted field net over which $\mathcal G$ acts as a group of internal symmetries. The \"untwisted\" net from which we start is defined by means of generalized free fields and yields a large class of toy models where the analysis of topologically trivial superselection sectors of [@GLRV01; @Ruz05] can be checked, as happens for [@DP02] in the Minkowski spacetime.

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
