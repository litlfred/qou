---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-011-42-twisted-nets-and-background-potentials
section_title: "Twisted nets and background potentials."
section_number: 4.2
pages: 23-25
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.98
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
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
