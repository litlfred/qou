---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-008-33-the-main-result
section_title: "The main result."
section_number: 3.3
pages: 17-20
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.968
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
We now define a presheaf structure on the family

$Z^1_c(\EuFrak{R})_< := \{ Z^1_c(\EuFrak{R})_{<a} \}_{a \in \Delta}$,

by means of the restriction functors

$$r_{aa'} : Z^1_c(\EuFrak{R})_{<a'} \to Z^1_c(\EuFrak{R})_{<a}
\ \ , \ \
( \ r_{aa'}z := z|_{\Sigma_1(\Delta^a)}
\ , \
r_{aa'}\rho := \{ \rho_e \}_{e \in \Delta^a} \ )
\ \ , \ \
r_{aa'}t := \{ t_e \}_{e \in \Delta^a}
\ ,$$

which obviously fulfill the presheaf relations

$r_{aa''} = r_{aa'} \circ r_{a'a''}$, $\forall a \subseteq a' \leq a''$.

::: lem
[]{#lem.br1 label="lem.br1"} The pair $\EuFrak{Z}_\otimes := (Z^1_c(\EuFrak{R})_<,r)^\Delta$ defines a simple tensor presheaf. Moreover we have

$$\label{eq.lem.br1}
\epsilon(z_\rho,w_\sigma)_e \ = \ \epsilon( \ r_{aa'}z_\rho , r_{aa'}w_\sigma \ )_e
\ \ , \ \
\forall e < a \subseteq a'
\ ,$$

where $z_\rho , w_\sigma \in {\bf obj \ }Z^1_c(\EuFrak{R})_{<a'}$.
:::

::: proof
*Proof.* We assume $a \subset a'$, otherwise there is nothing to prove. Let $z_\rho,w_\sigma \in {\bf obj \ }Z^1_c(\EuFrak{R})_{<a'}$ and $t \in (z_\rho,w_\sigma)$. Then for any path $p : e' \to e$ such that $e < a$, ${e'} < a'$, $|p| \subseteq \Delta^{a'}$, we have

$$\| t_e \|^2 = 
\| z(p) t_{e'} w(p)^* \|^2 = 
\| w(p) t_{e'}^* t_{e'} w(p)^* \| = 
\| t_{e'}^* t_{e'} \| =
\| t_{e'} \|^2
\ ,$$

so $r_{aa'}$ is isometric and $\EuFrak{Z}$ is a presheaf.

In the following lines we prove that any $r_{aa'}$, $a \subseteq a'$, preserves tensor product and the families $\epsilon(\cdot,\cdot)$. The fact that the tensor product is preserved is evident by ([\[eq.tens.z1\]](#eq.tens.z1){reference-type="ref" reference="eq.tens.z1"}).

Passing to the \"symmetry\", we consider $a \subseteq a'$, $z_\rho , w_\sigma \in Z^1_c(\EuFrak{R})_{<a'}$ and note that the operators

$$\epsilon( \ r_{aa'}z_\rho , r_{aa'}w_\sigma \ )_e
\ \ , \ \
e \in \Delta^a
\ ,$$

should be defined, according to ([\[eq.sym.z1\]](#eq.sym.z1){reference-type="ref" reference="eq.sym.z1"}), using paths

$p_{oe}$, $p_{o'e}$ in $\Delta^a$ with $o \perp o'$;

but since $\Delta^a \subseteq \Delta^{a'}$ and $\Sigma_1(\Delta^a) \subseteq \Sigma_1(\Delta^{a'})$ we have that $p_{oe}$, $p_{o'e}$ are paths also in $\Delta^{a'}$, so, since any

$\epsilon(z_\rho,w_\sigma)_e$, $e \in \Delta^{a'}$,

is independent on the choice of $p_{oe}$, $p_{o'e}$, we obtain ([\[eq.lem.br1\]](#eq.lem.br1){reference-type="ref" reference="eq.lem.br1"}) as desired. ◻
:::

::: lem
[]{#lem.br2 label="lem.br2"} $Z^1(\EuFrak{R})$ is the category of sections of $\EuFrak{Z}_\otimes$.
:::

::: proof
*Proof.* If $z \in {\bf obj \ }Z^1(\EuFrak{R})$ then we define the family

$z^a := z|_{\Sigma_1(\Delta^a)}$, $\forall a \in \Delta$;

to add a family of charges, for any $e<a$ we set

$$\left\{
\begin{array}{ll}
\Delta(\perp a,e) \ := \ \{ p \ : \ \partial_1p \perp a , \partial_0p = e \} \ ,
\\
\varrho^a_e(t) \ := \ \{ {\mathrm{ad}}z(p) \}(t) \ , \  \forall t \in R_a \ ,
\ \ {\mathrm{where}} \ \ p \in \Delta(\perp a,e) \ .
\end{array}
\right.$$

By [@BR08 Eq.4.5], $\varrho^a_e$ does not depend on the choice of $p \in \Delta(\perp a,e)$, and [@BR08 Lemma 5.1(i,iv)]

[^1]

imply that $\varrho^a_e \in {\bf loc}R_a$. Using [@BR08 Lemma 5.1(ii)] we find

$$\label{eq.C1.0}
z(b) \cdot \varrho^a_{\partial_1b}(t) = \varrho^a_{\partial_0b}(t) \cdot z(b)
\ \ , \ \
\forall a \in \Delta \ , \ t \in R_a \ , \ b \in \Sigma_1(\Delta^a)
\ ,$$

so

$$z_\varrho^a \ := \ ( \ z^a \ , \ \varrho^a := \{ \varrho^a_e \}_{e<a} \ ) \ \in \ {\bf obj \ }Z^1_c(\EuFrak{R})_{<a} \ .$$

Let now $a \subseteq a'$; then $\Delta(\perp a',e) \subseteq \Delta(\perp a,e)$ so, by path-invariance of $\varrho^{a'}_e$,

$$\varrho^{a'}_e |_{R_a} 
\ := \ 
{\mathrm{ad}}z(p')|_{R_a}
\ = \
\varrho^a_e
\ \ \ , \ \ \qquad
\forall p \in \Delta(\perp a',e) \subseteq \Delta(\perp a,e)
\ ,$$

and we conclude that $\{ z_\varrho^a \}_a$ is a section of $\EuFrak{Z}$. If $t \in (z,w)$ then defining

$t^a_e := t_e$, $\forall e<a$,

yields an arrow $t^a$ of $Z^1_c(\EuFrak{R})_{<a}$ and a section $\widetilde t := \{ t^a \}$, so $Z^1(\EuFrak{R})$ is a subcategory of $\widetilde\EuFrak{Z}$.

On the other side, let us consider a section

$$(\widetilde z,\widetilde\varrho) \in {\bf obj \ }\widetilde\EuFrak{Z}
\ \ , \ \
(\widetilde z,\widetilde\varrho) \ = \ \{ (\widetilde z^a,\widetilde\varrho^a) \in {\bf obj \ }Z^1_c(\EuFrak{R})_{<a} \}_{a \in \Delta} \ .$$

Since any $a \in \Delta$ has proper closure in $M$, for any $b \in \Sigma_1(\Delta)$ there is $a \in \Delta$ such that

$|b| \in \Sigma_1(\Delta^a)$ and we define

$z(b) := \widetilde z^a(b)$.

Since $\widetilde z$ is a section, the previous definition does not depend on the choice of $a > |b|$; moreover given $c \in \Sigma_2(\Delta)$ we have $dz(c) = d \widetilde z^a(c) = 1$ for any $a > |c|$ so $z \in {\bf obj \ }Z^1(\EuFrak{R})$.

If $\widetilde t := \{ \widetilde t^a \}$ is an arrow of $\widetilde\EuFrak{Z}$ then for any $e \in \Delta$ there must be some $a \in \Delta$ with $e<a$ and we set

$t_e := \widetilde t^a_e$,

so reasoning as above we have that $t := \{ t_e \}$ is an arrow of $Z^1(\EuFrak{R})$. We conclude that $Z^1(\EuFrak{R}) = \widetilde\EuFrak{Z}$ as desired. ◻
:::

::: lem
[]{#lem.br3 label="lem.br3"} The subpresheaf $\EuFrak{S}:= \EuFrak{Z}^\downarrow$, defined as in Rem.[\[rem.back1\]](#rem.back1){reference-type="ref" reference="rem.back1"}, is a simple, symmetric tensor presheaf and $\widetilde\EuFrak{S}= Z^1(\EuFrak{R})$.
:::

::: proof
*Proof.* By definition we have $\EuFrak{S}= (S,r)^\Delta$, where each $S_a$, $a \in \Delta$, is the full subcategory of $Z^1_c(\EuFrak{R})_{<a}$ with objects

$${\bf obj \ }S_a \ := \ \{  z_\varrho^a \ , \ z \in {\bf obj \ }Z^1(\EuFrak{R}) \} \ .$$

By Rem.[\[rem.back1\]](#rem.back1){reference-type="ref" reference="rem.back1"} we already know that $\widetilde\EuFrak{S}= Z^1(\EuFrak{R})$. Moreover $\EuFrak{S}$ is clearly simple and tensorial, so we only have to check the symmetry property.

To this end we note that we already know from §[\[sec.sym\]](#sec.sym){reference-type="ref" reference="sec.sym"} that, given $o,o' < a$, $o \perp o'$,

$$\epsilon(z_\varrho^a , w_\varsigma^a)_e 
\ := \
w_\varsigma(p_{oe})^* \varsigma^a_o(z_\varrho(p_{o'e}))^* \cdot
z_\varrho(p_{o'e}) \varrho^a_e(w_\varsigma(p_{oe}))
\ \ , \ \
e < a
\ ,$$

fulfils the symmetry relations, so we only have to prove that

$\epsilon(z_\varrho^a , w_\varsigma^a)_e \in R_e$ for any $e \in \Delta^a$.

Now, the point is that $\epsilon(z_\varrho^a , w_\varsigma^a)$ is defined exactly as in [@BR08 Eq.5.10] and this time, due to the fact that $z,w$ *are globally defined*, the charges $\varrho^a_e , \varsigma^a_e$ extend to endomorphisms

$\varrho^x_e , \varsigma^x_e \in {\bf end}R^\perp_x$,

where $R^\perp_x := \cup_{ \overline\omega \perp \{ x \} } R_\omega$ for any $x \in M$ such that $\{ x \} \perp \overline e$ (see [@BR08 §5.1]). The property ([\[eq.int\]](#eq.int){reference-type="ref" reference="eq.int"}) now holds in the form

$$\epsilon(z_\varrho^a , w_\varsigma^a)_e \cdot \{ \varrho^x_e \circ \varsigma^x_e \}(t)
\ = \
\{ \varsigma^x_e \circ \varrho^x_e \}(t) \cdot \epsilon(z_\varrho^a , w_\varsigma^a)_e
\ \ , \ \
\forall t \in R^\perp_x 
\ ,$$

at varying of $x \in M$ with $\{ x \} \perp \overline e$ (see [@BR08 Lemma 5.1(iii)]). So, as remarked in §[\[sec.sym\]](#sec.sym){reference-type="ref" reference="sec.sym"},

$$\epsilon(z_\varrho^a , w_\varsigma^a)_e \cdot t' \ = \ 
t' \cdot \epsilon(z_\varrho^a , w_\varsigma^a)_e 
\ \ , \ \
\forall t' \in R_\omega \subseteq R^\perp_x 
\ , \ 
\overline\omega \perp \{ x \} \ , \ \omega \perp e
\ ,$$

and we conclude, by punctured Haag duality, that $\epsilon(z_\varrho^a , w_\varsigma^a)_e \in R_e$ as desired. ◻
:::

Before to state our main result we select the sectors having a conjugate. For any $a \in \Delta$, we denote the full subcategory of $S_a$ with objects $z_\varrho^a$, $z \in Z^{1,\bullet}(\EuFrak{R})$, by $S^\bullet_a$, and define

$$\EuFrak{S}^\bullet \ := \ (S^\bullet,r)^\Delta \ .$$

By the previous Lemmata, and since by [@BR08 §5.3] we have that $Z^{1,\bullet}(\EuFrak{R})$ is a DR-category, we obtain:

::: thm
[]{#thm.br label="thm.br"} Let $\EuFrak{R}= (R,j)_\Delta \subseteq BH$ be a Haag-Kastler net where $\Delta$ is the base of diamonds of a globally hyperbolic spacetime $M$ with spacetime dimension $\geq 3$. Then $\EuFrak{S}:= (S,r)^\Delta$ is a simple, symmetric tensor presheaf such that $Z^1(\EuFrak{R})$ is the category of sections of $\EuFrak{S}$. In particular, $\EuFrak{S}^\bullet$ is a DR-presheaf with category of sections $Z^{1,\bullet}(\EuFrak{R})$.
:::

In the following points we list some consequences of the previous theorem.

#### Holonomy of sectors.

Let $z \in {\bf obj \ }Z^1(\EuFrak{R})$ and ${}_\beta \widehat z$ the presheaf bundle of tensor powers of $z$ defined in ([\[eq.beta\]](#eq.beta){reference-type="ref" reference="eq.beta"}). By definition, the fibre ${}_\beta \widehat z_a$, $a \in \Delta$, has objects the tensor powers

$z^n_a := z \otimes \ldots \otimes z$, $n \in {\mathbb N}$

(note that $a \in \Delta$ plays no role at the level of objects), and arrows

$${}_\beta(z^n_a , z^m_a) 
\ = \ 
\{  t = ( t_e \in R_e \, , \, e \in \cup_{a' \supseteq a} \Delta^{a'} ) 
    \, : \, 
    z^m(b) t_{\partial_1 b}= t_{\partial_0 b}z^n(b) \, , \, \forall b \in \Sigma_1(\cup_{a' \supseteq a} \Delta^{a'}) \}
\ .$$

A simpler way to describe ${}_\beta(z^n_a , z^m_a)$ is the following: since any $a$ has compact closure, we can find $a' \in \Delta$ such that $a \in \Delta^{a'}$; thus for any $t \in {}_\beta(z^n_a , z^m_a)$ we can pick $t_a \in R_a$, and this suffices to determine $t$ because of the relation

$$t_e \ = \ z^m(p) \, t_a \, z^n(p)^* \ \ , \ \ \forall e \in \cup_{a' \supseteq a} \Delta^{a'} \ ,$$

where $p : a \to e$ is a path made of 1-simplices in $\Sigma_1(\cup_{a' \supseteq a} \Delta^{a'})$. In this way, on the arrows, the restriction functors take the form

$r^z_{aa'}(t_{a'}) =  t_a$, $a \subseteq a'$,

and have inverse

$$r^z_{a'a}(t_a) \ = \ t_{a'} \ = \  z^m(b_{a'a}) \, t_a \, z^n(b_{a'a})^*
\ \ , \ \
b_{a'a} := (a',a;a') \in \Sigma_1(\Delta) \ .$$

Thus, reasoning as in ([\[eq.back3a\]](#eq.back3a){reference-type="ref" reference="eq.back3a"}), we compute the holonomy of ${}_\beta \widehat z$,

$$\label{eq.holz}
\chi'_z : \pi_1(\Delta) \to {\bf aut}{}_\beta \widehat z_a
\ \ , \ \
\{ \chi'_z(p) \}(t_a) \ = \ z^m(p) \, t_a \, z^n(p)^*
\ \ , \ \qquad
p : a \to a 
\ , \
t_a \in {}_\beta(z^n_a , z^m_a) \ .$$

Let now in particular $z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$. By Theorem [\[lem_CCS00\]](#lem_CCS00){reference-type="ref" reference="lem_CCS00"}, the sector $z$ defines a compact Lie group $G_z \subseteq {{\mathbb U}(d)}$ and a holonomy representation

$\chi_z : \pi_1(\Delta) \to QG_z := NG_z / G_z$,

which is a complete invariant of the presheaf bundle ${}_\beta \widehat z$. In accord with the proof of [@Vas12 Theorem 5.3], the group $G_z$ is such that there is a symmetric tensor isomorphism

$F : {}_\beta \widehat z_a \to \widehat\pi_{G_z}$.

Regarding $QG_z$ as an automorphism group of $\widehat\pi_{G_z}$ (see Ex.[\[ex.back1\]](#ex.back1){reference-type="ref" reference="ex.back1"}), by the argument used to prove [@Vas12 Eq.5.5] we have

$\chi_z \circ F = F \circ \chi'_z$.

It can be easily verified that $d$ is the statistical dimension of $z$ (see [@BR08 §5.3]), but we prefer to not discuss here the details.

#### Dual objects and topologically trivial sectors.

By Theorem [\[thm_DUAL\]](#thm_DUAL){reference-type="ref" reference="thm_DUAL"}, any embedding

$I : \EuFrak{S}^\bullet \to \EuFrak{C}$

yields a full embedding of symmetric tensor *C\**-categories

$Z^{1,\bullet}(\EuFrak{R}) \hookrightarrow{\bf Hilb}_\EuFrak{G}(\Delta)$,

where $\EuFrak{G}$ is a compact group net bundle, and induces lifts

$\widehat\chi_z : \pi_1(\Delta) \to NG_z$, $\chi_z = \widehat\chi_z \, {\mathrm{mod}} G_z$,

of the holonomies defined by sectors $z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$.

Let now $Z^1_t(\EuFrak{R})$ denote the subcategory of topologically trivial sectors, that is, of those $z \in {\bf obj \ }Z^1(\EuFrak{R})$ such that there is a family $\psi = \{ \psi_a \in UH \}$ with $z(b) = \psi_{\partial_0b}^* \psi_{\partial_1b}$, $b \in \Sigma_1(\Delta)$.

Then

$z^n(p) = 1$ for any $p : a \to a$ and $n \in {\mathbb N}$,

and by ([\[eq.holz\]](#eq.holz){reference-type="ref" reference="eq.holz"}) we have that $\chi'_z(p)$ is the identity functor for any $z \in {\bf obj \ }Z^1_t(\EuFrak{R})$. Thus when $z \in {\bf obj \ }Z^{1,\bullet}_t(\EuFrak{R})$ we have that $\chi'_z$ and $\chi_z$ are trivial, and there is at least one lift $\widehat\chi_z$, the trivial one. We have a full embedding

$Z^{1,\bullet}_t(\EuFrak{R}) \hookrightarrow{\bf Hilb}_{\EuFrak{G}_t}(\Delta)$,

where $\EuFrak{G}_t$ is the trivial net bundle with fibre the Doplicher-Roberts dual $G_t$ of $Z^{1,\bullet}_t(\EuFrak{R})$. But, by the results in [@Vas12], we may also have

$Z^{1,\bullet}_t(\EuFrak{R}) \hookrightarrow{\bf Hilb}_\EuFrak{G}(\Delta)$

for some nontrivial group net bundle $\EuFrak{G}$.

#### Cochains.

By Theorem [\[thm.gerbe\]](#thm.gerbe){reference-type="ref" reference="thm.gerbe"}, any sector $z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$ defines the 1--cochain

$u_z : \Sigma_1(\Delta) \to NG_z$

that classifies lifts $\widehat\chi_z : \pi_1(\Delta) \to NG_z$, $q \circ \widehat\chi_z = \chi_z$. The cochain $u_z$ defines a gerbe in the sense of §[\[sec.concl\]](#sec.concl){reference-type="ref" reference="sec.concl"}, see ([\[eq.CON1a\]](#eq.CON1a){reference-type="ref" reference="eq.CON1a"}).

#### Characteristic classes.

Let $P_z \to M$ denote the locally constant, principal $QG_z$-bundle defined by $\chi_z$. By ([\[eq.ccs0\]](#eq.ccs0){reference-type="ref" reference="eq.ccs0"}), we have characteristic classes

$\zeta^\uparrow(z) := [\zeta^\uparrow(P_z)] \in H^{2k-1}(M,{\mathbb R}/ {\mathbb K})$

that vanish when $\chi_z$ is the trivial morphism, that is, when $z$ is a topologically trivial sector. Thus we can measure the obstruction of $z$ being a topologically trivial sector in terms of the odd cohomology of the given spacetime.

#### Chern classes of fields with \"trivial gauge group\".

Let $\EuFrak{R}$ be a Haag-Kastler net such that $G_z$ is trivial for any $z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$. Then $NG_z = QG_z = {{\mathbb U}(d)}$ and $\chi_z$ takes values in ${{\mathbb U}(d)}$. By ([\[eq.ccs\]](#eq.ccs){reference-type="ref" reference="eq.ccs"}) we have Chern classes

$$\label{eq.ccsz}
\left\{
\begin{array}{ll}
c_k(z) := c_k^\uparrow(\chi_z) \in H^{2k-1}(M,{\mathbb{R/Z}})
\ , \
\forall k=1,\ldots \ , d \ ,
\\
ccs(z) := d + \sum_{k=1}^d \frac{ (-1)^{k-1}  }{ (k-1)! } \ c_k(z)_{ {\mathrm{mod}}{\mathbb Q}}
\ \in {\mathbb Z}\oplus H^{odd}(M,{\mathbb{R/Q}}) \ .
\end{array}
\right.$$

This is the situation that we expect to hold for quantum fields with trivial superselection structure in the Minkowski spacetime, as, for example, the free electromagnetic field.

The classes ([\[eq.ccsz\]](#eq.ccsz){reference-type="ref" reference="eq.ccsz"}) are an interesting clue supporting the idea that Brunetti-Ruzzi sectors describe Aharonov-Bohm-type situations ([@BR08 §7]): in fact, in the same way the monodromy phase of the quantum electromagnetic potential is described by a class in $H^1(M,{\mathbb{R/Z}})$, the holonomy of $z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$ is measured by the first Chern class $c_1(z) \in H^1(M,{\mathbb{R/Z}})$.

In this regard, we conjecture that the free electromagnetic field yields a net such that that $G_z$ is trivial for any

$z \in {\bf obj \ }Z^{1,\bullet}(\EuFrak{R})$.

[^1]: In this reference an $x \in M$ is chosen with $a \perp \{ x \}$, and we have the notation $\varrho^a_e \equiv y^z_x(e) |_{R_a}$, $\forall e \in \Delta^a$. Moreover, it is proved that $\varrho^a_e$ is independent of $x$.
