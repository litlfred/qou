---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-010-41-twisted-field-nets
section_title: "Twisted field nets."
section_number: 4.1
pages: 20-23
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.982
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
Let $\EuFrak{F}= (F,\jmath)_\Delta$ be a net of $C^*$-algebras. We say that $\EuFrak{F}$ is ${\mathbb Z}_2$-*graded* whenever there is a period $2$ automorphism

$$\beta_a : F_a \to F_a
\ \ : \ \
\beta_{a'} \circ \jmath_{a'a} = \jmath_{a'a} \circ \beta_a
\ \ , \ \
\beta_a^2 = id_{F_a}
\ \ , \ \
\forall a \subseteq a' \in \Delta \ .$$

In this case we set

$$F^\pm_a \ := \ \{ t \in F_a : \beta_a(t) = \pm t  \}
\ \ , \ \
\forall a \in \Delta
\ ,$$

so we have the usual projections

$$F_a \to F^\pm_a
\ , \
t \mapsto t^\pm := 1/2 (t \pm \beta_a(t))
\ \ , \ \
\forall a \in \Delta \ .$$

The following definition of normal commutation relations is a variant of [@BR08 Eq.3.6] taking account, differently from the above-cited reference, of the net structure of the involved representation. At any rate, it is trivially verified that the following results remain valid with the older definition.

We say that a representation $(\pi,U)$ of $\EuFrak{F}$ is *normal* whenever for any $a,o \in \Delta$ with $a \perp o$, $t_1 \in F_a$, $t_2 \in F_o$, it turns out

$$\label{def.norm}
\left\{
\begin{array}{ll}
[ \pi_a(t_1^+) \, , \, \pi_o(t_2^+) ]^{net} =  
[ \pi_a(t_1^+) \, , \, \pi_o(t_2^-) ]^{net} = 
[ \pi_a(t_1^-) \, , \, \pi_o(t_2^+) ]^{net} = 0 \ ,

\\

\left[ \pi_a(t_1^-) \, , \, \pi_o(t_2^-) \right]^{net}_+ = 0 \ ,
\end{array}
\right.$$

where the (anti)commutators are in the sense of ([\[eq.nets1\]](#eq.nets1){reference-type="ref" reference="eq.nets1"}) (with the convention $[ \cdot , \cdot ]^{net}_- \equiv [ \cdot , \cdot ]^{net}$).

Let now $H_*$ denote a Hilbert space. A *${\mathbb Z}_2$-graded group on $H_*$* is given by a group $G_*$ of unitary operators on $H_*$, metrizable and compact under the strong topology, and a central element

$\gamma \in ZG_*$, $\gamma^2 = 1$,

where $1 \in G_*$ is the identity.

A *$(G_*,\gamma)$-net of von Neumann algebras* is a net

$$\EuFrak{F}_* = (F_*,\jmath_*)_\Delta \ \subset BH_*$$

represented on the Hilbert space $H_*$ (that is, $\jmath_*$ is given by inclusion maps), such that

$$\label{eq.gauge1}
\alpha^g_a(t) := g t g^* \in F_{*,a}
\ \ , \ \
\forall g \in G_* \ , \ t \in F_{*,a} \ , \ a \in \Delta \ .$$

We denote the fixed-point net by $\EuFrak{R}_* = (R_*,\jmath_*)_\Delta$, where

$$R_{*,a} := F_{*,a} \cap G_*' \ \ , \ \ \forall a \in \Delta \ .$$

Note that $\gamma$ induces a ${\mathbb Z}_2$-grading on $\EuFrak{F}_*$. We say that $\EuFrak{F}_*$ is *normal* whenever the defining Hilbert space representation $(id_{F_*},1)$ is normal in the sense of the previous lines. By ([\[eq.nets1\]](#eq.nets1){reference-type="ref" reference="eq.nets1"}), this agrees with the classical definition used, for example, in [@DR90]. Finally, we define the normalizer group

$$\label{def.NG}
N_\gamma G_* \subset UH_* \ : \ V \in N_\gamma G_* \stackrel{\cdot}{\Leftrightarrow} 

\left\{  
\begin{array}{ll}
V F_{*,a} V^* = F_{*,a} \ , \ \forall a \in \Delta \ , \\

VgV^* \in G_* \ , \ \forall g \in G_* \ , \\

V \gamma = \gamma V \ .
\end{array}
\right.$$

::: lem
[]{#lem.gauge1 label="lem.gauge1"} Let $(G_*,\gamma)$ be a ${\mathbb Z}_2$-graded group on the Hilbert space $H_*$ and $\EuFrak{F}_*$ a normal $(G_*,\gamma)$-net of von Neumann algebras on $H_*$. Then for any morphism

$$\chi : \pi_1(M) \to N_\gamma G_* \subset UH_*$$

there are:

1.  A group net bundle $\EuFrak{G}= (G,\hat \imath)_\Delta$ with fibre $G_*$;

2.  A ${\mathbb Z}_2$-graded net of *C\**-algebras $\EuFrak{F}= (F,\jmath)_\Delta$;

3.  A gauge action $\EuFrak{G}\times_\Delta \EuFrak{F}\to \EuFrak{F}$ with fixed point net $\EuFrak{R}= (R,\jmath)_\Delta$;

4.  A Hilbert net bundle $\EuFrak{H}= (H,U)_\Delta$ with holonomy $\chi$ and a normal representation $\pi : \EuFrak{F}\to \EuFrak{B}\EuFrak{H}$;

5.  A causal

    [^1]

    representation $(\pi|_R ,U|_R)$ of $\EuFrak{R}$.
:::

::: proof
*Proof.* *Point 1.* Given $\omega \in \Delta$ and a path frame $P_\omega$ as in ([\[def.pf\]](#def.pf){reference-type="ref" reference="def.pf"}) we define

$$\imath_{a'a} := \chi( p_{\omega a'}*(a',a;a') * p_{a \omega})
\ \ , \ \qquad
\forall a \subseteq a' \ .$$

By homotopy invariance the family $\imath$ fulfils

$\imath_{a''a'} \imath_{a'a} = \imath_{a''a}$, $\forall a \subseteq a' \subseteq a''$

(see [@Ruz05 §2.2]). We define

$$G_a \equiv G_*
\ \ , \ \
\hat \imath_{a'a}(g) := \imath_{a'a} g \, \imath_{a'a}^*
\ \ , \ \qquad
\forall g \in G_* \ , \ a \subseteq a' \in \Delta \ .$$

*Point 2.* We define $F_a := F_{*,a}$, $\forall a \in \Delta$, and

$$\jmath_{a'a} : F_a \to F_{a'}
\ \ , \ \
\jmath_{a'a}(t) := i_{a'a} t \, i_{a'a}^*
\ \ , \ \qquad
\forall a \subseteq a'
\ , \
t \in F_a
\ .$$

Since $\imath_{a''a'} \imath_{a'a} = \imath_{a''a}$, $\forall a \subseteq a' \subseteq a''$, we conclude that $\EuFrak{F}= (F,\jmath)_\Delta$ is a net. Moreover, since

$$\imath_{a'a} \gamma   \ = \ \gamma \, \imath_{a'a}
\ \ , \ \ 
\forall a \subseteq a' \ ,$$

we have a ${\mathbb Z}_2$-grading on $\EuFrak{F}$ given by the adjoint action of $\gamma$.

*Point 3.* Taking into account that $G_a \equiv G_*$ and $F_a = F_{*,a}$ for any $a \in \Delta$ we define $\alpha^g_a \in {\bf aut}F_a$ as in ([\[eq.gauge1\]](#eq.gauge1){reference-type="ref" reference="eq.gauge1"}). To check that $\alpha$ is a gauge action ([\[eq.GA00\]](#eq.GA00){reference-type="ref" reference="eq.GA00"}) must be fulfilled, so we compute, for any $a \in \Delta$, $g \in G_a$, $t \in F_a$,

$$\alpha^{\hat i_{a'a}(g)}_{a'} \circ \jmath_{a'a}(t) \ = \
\imath_{a'a} g \, \imath_{a'a}^* \cdot \imath_{a'a} t \, \imath_{a'a}^* \cdot \imath_{a'a} g^* \, \imath_{a'a}^* \ = \
\imath_{a'a} g t g^* \imath_{a'a}^* \ = \
\jmath_{a'a} \circ \alpha^g_a(t) \ ,$$

and this yields the desired equalities. Note that $R_a = R_{*,a}$ for any $a \in \Delta$, because $G_* \equiv G_a$.

*Point 4.* We set $H_a := H_*$, $\pi_a(t) := t$, and $U_{a'a} := \imath_{a'a}$ for any $a \subseteq a' \in \Delta$, $t \in F_a$. The pair $(\pi,U)$ is clearly a representation, that is normal since, for any $o \perp a$, $t \in F_a$, $t' \in F_o$,

$$\pi_a(t) \cdot U_p \pi_o(t') U_p \ = \ t \cdot \imath_p t' \imath_p^*
\ \ , \ \
\forall p : o \to a
\ ,$$

and by construction $\imath_p t' \imath_p^* \in F_{*,o}$. Finally, by construction $(H,U)_\Delta$ has holonomy $\chi$.

*Point 5.* Since $\EuFrak{F}$ is graded by $\gamma \in G_*$ we have $R_a \subseteq F^+_a$, $\forall a \in \Delta$, so $\pi|_R$ is causal by applying ([\[def.norm\]](#def.norm){reference-type="ref" reference="def.norm"}). ◻
:::

The following notion is a natural generalization of [@DR90 Def.3.4]. Let

$\EuFrak{F}= (F,\jmath)_\Delta$

be a ${\mathbb Z}_2$-graded net with a faithful normal representation

$(\pi,U)$

on the Hilbert net bundle $\EuFrak{H}=(H,U)_\Delta$, $H = \{ H_a \}$. We assume that there is a net bundle of ${\mathbb Z}_2$-graded compact groups acting on

$\EuFrak{H}$,

that is, we have a family

$G = \{ G_a \subset UH_a \}$,

and central, period 2 elements $\gamma_a \in G_a$, $a \in \Delta$,

such that

${\mathrm{ad}}U_{a'a}(G_a) = G_{a'}$, ${\mathrm{ad}}U_{a'a}(\gamma_a) = \gamma_{a'}$, $a \subseteq a' \in \Delta$,

in such a way that the group net bundle

$\EuFrak{G}= (G, {\mathrm{ad}}U)_\Delta$

is defined. We assume that $\EuFrak{G}$ defines, by adjoint action, a gauge action on $\pi(\EuFrak{F})$. In this case, we call the quadruple

$(\EuFrak{F},\pi,U,\EuFrak{G})$

a *field system*.

::: defn
We say that field systems $(\EuFrak{F}_1,\pi_1,U_1,\EuFrak{G}_1)$, $(\EuFrak{F}_2,\pi_2,U_2,\EuFrak{G}_2)$ are **equivalent** whenever there is a unitary family

$\nu = \{ \nu_a : H_{1,a} \to H_{2,a} \}$

such that

$$\label{eq.gauge2}
\nu_{a'} U_{1,a'a} = U_{2,a'a} \nu_a
\ \ , \ \
{\mathrm{ad}}\nu_{a'} \circ \jmath_{1,a'a} = \jmath_{2,a'a} \circ {\mathrm{ad}}\nu_a
\ \ , \ \
\nu_a g \nu_a^* \in G_{2,a} 
\ \ , \ \
\nu_a \gamma_{1,a} = \gamma_{2,a} \nu_a
\ ,$$

for any $a \subseteq a'$, $g \in G_a$.
:::

Note that if $\chi_k$, $k=1,2$, are the holonomies of $(H_k,U_k)_\Delta$, then the first of ([\[eq.gauge2\]](#eq.gauge2){reference-type="ref" reference="eq.gauge2"}) implies

$$\label{eq.gauge3}
\chi_2(p) = \nu_a \cdot \chi_1(p) \cdot \nu_a^* \ \ , \ \ \forall p : a \to a \ .$$

::: cor
[]{#cor.gauge1 label="cor.gauge1"} If the morphism $\chi$ of the previous Lemma takes values in

$G_* \subseteq N_\gamma G_*$

then $\EuFrak{R}$ is isomorphic to $\EuFrak{R}_*$. Moreover, when $\chi$ is non-trivial $\EuFrak{R}_*$ is the fixed-point net of inequivalent field systems, namely

$(\EuFrak{F}_*,id_{F_*},1,G_*)$ and $(\EuFrak{F},\pi,U,\EuFrak{G})$.
:::

::: proof
*Proof.* Since $\chi$ takes values in $G_*$ we have $\imath_{a'a}(t) = t$ for any $a \subseteq a'$ and $t \in R_a$, so $\EuFrak{R}= \EuFrak{R}_*$. To prove that the above field systems are inequivalent it suffices to show that $U$ has a nontrivial holonomy, in fact the immersion $id_{F_*} : \EuFrak{F}_* \to BH$ has trivial holonomy and ([\[eq.gauge3\]](#eq.gauge3){reference-type="ref" reference="eq.gauge3"}) implies that the holonomy of $U$ should be trivial too. But this is not the case, as the holonomy of $U$, by construction, coincides with $\chi$ (see the proof of Point 4 of the previous Lemma). ◻
:::

One could argue that the only field net having a physical meaning is $\EuFrak{F}_*$. But, as a matter of fact, the twisted field net $\EuFrak{F}$ has the same local algebras and causal properties as $\EuFrak{F}_*$, and it can be constructed in such a way to support the Klein-Gordon and Dirac equations (see §[\[app.sym\]](#app.sym){reference-type="ref" reference="app.sym"}).

Note that $\EuFrak{F}$ lives in a representation, $\pi$, having a nontrivial holonomy in the sense of [@BR08], whose restriction to $\EuFrak{R}$ is equivalent to the (topologically trivial) representation of $\EuFrak{R}_*$ in the initial Hilbert space $H_*$; thus the difference between $\EuFrak{F}$ and $\EuFrak{F}_*$ can be detected only in charged states which, in $\pi$, carry topological effects given by the action of the fundamental group.

As a further remark, we observe that the technical ingredient underlying the construction of twisted field nets is that we allow

$\jmath_{a'a}$, $a \subseteq a'$,

to be actual \*-monomorphisms and not simply inclusion maps. This is justified by the fact that the same happens for images

$\pi^z(\EuFrak{R}_*)$

of the observable net under the action of sectors $\pi^z$, $z \in {\bf obj \ }Z^1(\EuFrak{R}_*)$, see ([\[eq.C00\]](#eq.C00){reference-type="ref" reference="eq.C00"}).

At the conceptual level, the question in which we are interested in is whether $\EuFrak{R}_*$ and the superselection structure $Z^1(\EuFrak{R}_*)$ encode enough informations to select a unique field system. On the grounds of [@Vas12] and the previous corollary we conclude that, to this end, further informations must be extracted from $Z^1(\EuFrak{R}_*)$. A complete discussion on twisted field nets is beyond the purposes of the present paper, and we postpone it to a future work (see §[\[sec.concl\]](#sec.concl){reference-type="ref" reference="sec.concl"}).

[^1]: That is $[ \pi_a(R_a) , \pi_o(R_o) ]^{net} = 0$ for any $o \perp a$, in the sense of ([\[eq.nets1\]](#eq.nets1){reference-type="ref" reference="eq.nets1"}).
