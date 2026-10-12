---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-009-45-charge-conjugation
section_title: "Charge conjugation"
section_number: 4.5
pages: 23-30
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in t erms of the unimodularity of the color group SU (3) and on the existence of 3"
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
---
In the identification of the octonion algebra $\mathbb O$ as $\mathbb C\oplus \mathbb C^3$, the octonionic conjugate of $(z,Z)=z+Z$ is $\overline{(z,Z)}=(\bar z,-Z)=\bar z-Z$.\
On the other hand if one interprets $Z\in \mathbb C^3$ as an internal quark state and $z\in \mathbb C$ as an internal state of the corresponding lepton, the charge conjugation ${\cal C}$ induces the complex conjugation in $\mathbb C^3$ and in $\mathbb C$ that is $${\cal C}(z+Z)=\bar z+\bar Z$$ for $z\in \mathbb C$, $Z\in \mathbb C^3$.\
It is easy to verify by using Formula ([\[proc\]](#proc){reference-type="ref" reference="proc"}) that ${\cal C}$ is an automorphism of $\mathbb O$ $({\cal C}\in G_2)$ with ${\cal C}^2=\mbox{\rm 1\hspace {-.6em} l}$ by construction. This automorphism of $\mathbb O$ induces canonically an involutive automorphism of the Jordan algebra $J^8_3$ as well as of the $J^8_3$-modules. These automorphisms will be all denoted by ${\cal C}$.\

# Differential calculus over Jordan algebras

## First order differential calculi

Given a category $\mathbf C$ of algebras over some field $\mathbb K$ and an algebra ${\cal A}$ in $\mathbf C$, a pair $(\Omega^1,d)$ of an ${\cal A}$-bimodule $\Omega^1$ for $\mathbf C$ [@mdv:2001] and a derivation $d$ of ${\cal A}$ into $\Omega^1$, that is a $\mathbb K$-linear mapping satisfying (the Leibniz rule) $$d(xy)=d(x)y+xd(y)$$ for any $x,y\in {\cal A}$, will be refered to as a *first order differential calculus over ${\cal A}$* for $\mathbf C$ or simply a first order calculus over ${\cal A}$ when no confusion arises. There is an obvious notion of homomorphism of first order differential calculi over ${\cal A}$. This terminology as well as the one for higher order differential calculi was introduced in [@wor:1989] for the case of the category of associative algebras on a field $\mathbb K$.

In the following we shall be concerned with the category of real unital Jordan algebras so, if $J$ is such a unital Jordan algebra, a $J$-bimodule is a unital $J$-module which will be simply refered to as a $J$-module when no confusion arises.\
Let $J$ be a unital Jordan algebra and let us define *its center* $Z(J)$ by $$Z(J)=\{z\in J \vert [x,y,z]=[x,z,y]=0, \forall x,y\in J\}
  \label{center}$$ where $[x,y,z]=(xy)z-x(yz)$ denotes the associator of $x,y,z\in J$. The center $Z(J)$ is a unital associative subalgebra of $J$. The Lie algebra ${\mbox{Der}}(J)$ of all derivations of $J$ into itself is also a $Z(J)$-module and we denote by $\Omega^1_{{\mbox{\tiny Der}}}(J)$ the $J$-module of all the $Z(J)$-homomorphisms of ${\mbox{Der}}(J)$ into $J$. One defines a derivation $$d_{{\mbox{\tiny Der}}}:J\rightarrow \Omega^1_{{\mbox{\tiny Der}}}(J)$$ by setting $$d_{{\mbox{\tiny Der}}}(x)(X)=X(x)
  \label{dDer}$$ for any $x\in J$ and $X\in{\mbox{Der}}(J)$.\
This first-order differential calculus $(\Omega^1_{{\mbox{\tiny Der}}}(J),d_{{\mbox{\tiny Der}}})$ will be referred to as the *derivation-based first order differential calculus* over $J$.

## First order differential calculi over $J^8_3$

The Lie algebra ${\mbox{Der}}(J^8_3)$ of all derivations of the exceptional Jordan algebra $J^8_3$ is the exceptional compact simple Lie algebra $\mathfrak f_4$. Since $J^8_3$ is simple $Z(J^8_3)=\mathbb R$ so the unital $J^8_3$-module $\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)$ is the vector space of all linear mappings of ${\mbox{Der}}(J^8_3)$ into $J^8_3$ that is $$\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)=J^8_3\otimes {\mbox{Der}}(J^8_3)^\ast
  \label{omegad}$$ where ${\mbox{Der}}(J^8_3)^\ast=\mathfrak f_4^\ast$ denotes the dual vector space of ${\mbox{Der}}(J^8_3)$.\
One defines as before the derivation $d_{{\mbox{\tiny Der}}}:J^8_3\rightarrow \Omega_{{\mbox{\tiny Der}}}(J^8_3)$ by setting $d_{{\mbox{\tiny Der}}}(x)(X)=X(x)$ for any $x\in J^8_3$ and $X\in {\mbox{Der}}(J^8_3)$. The first order differential calculus $(\Omega_{{\mbox{\tiny Der}}}(J^8_3),d_{{\mbox{\tiny Der}}})$ over $J^8_3$ is characterized by the following universal property.

::: proposition
[]{#univ label="univ"} For any first order calculus $(\Omega^1,d)$ over $J^8_3$, there is a unique (unital) Jordan module homomorphism $i_d:\Omega^1_{{\mbox{\tiny Der}}}(J^8_3)\rightarrow \Omega^1$ such that one has $d=i_d\circ d_{{\mbox{\tiny Der}}}$.
:::

[Proof]{.underline}. From the general structure of the $J^8_3$-modules, $\Omega^1$ is of the form $\Omega^1=J^8_3\otimes E$ for some vector space $E$. Let $(e^\alpha)$ be a basis of $E$ then $d(x)=X_\alpha(x)\otimes e^\alpha$ with $X_\alpha\in {\mbox{Der}}(J^8_3)$ for any $\alpha$. Let $(\partial_k)$ be a basis of ${\mbox{Der}}(J^8_3)$ with dual basis $\theta^k$ then one has $d(x)=\partial_k(x)\otimes C^k_\alpha e^\alpha$ with the $C^k_\alpha\in \mathbb R$. Define $i_d$ by $i_d(x\otimes \theta^k)=x\otimes C^k_\alpha e^\alpha$, then $i_d$ is a $J^8_3$-module homomorphism satisfying $d=i_d\circ d_{{\mbox{\tiny Der}}}$ which is clearly unique. $\square$\
[Remark]{.underline}. Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"} is very specific to the exceptional Jordan algebra $J^8_3$ and is a direct consequence of the fact that $J^8_3$ is, as $J^8_3$-module, the only irreducible module. For instance if $J$ is a finite-dimensional simple Euclidean Jordan algebras of Theorem 2 which is distinct of $\mathbb R$ and of $J^8_3$, the first order differential calculus $(\Omega^1_{{\mbox{\tiny Der}}}(J), d_{{\mbox{\tiny Der}}})$ is not universal since then there several inequivalent irreducible $J$-modules and not only $J$ itself. In all these cases one has $\Omega^1_{{\mbox{\tiny Der}}}(J)=J\otimes {\mbox{Der}}(J)^\ast$ and ${\mbox{Der}}(J)$ is a real compact form of a classical simple Lie algebra. Furthermore all the classical simple Lie algebras are realized in this way as Lie algebras of derivations of the finite-dimensional simple special Euclidean Jordan algebras.

## Differential graded Jordan algebras

Let us define a *differential graded Jordan algebra* to be a $\mathbb N$-graded algebra $$\Omega=\oplus_{n\in \mathbb N}\Omega^n$$ which is a *Jordan superalgebra*, (see e.g. in [@kac:1977], [@mar-zel:2010]), for the induced $\mathbb Z/2\mathbb Z$ degree and which is equipped with a *differential*, that is with an antiderivation $d$ of degree 1 and of square 0.\
Thus $\Omega$ is a graded-commutative algebra, that is one has $$ab=(-1)^{\vert a\parallel b\vert} ba \in \Omega^{\vert a\vert+\vert b\vert}
\label{grcom}$$ for $a\in \Omega^{\vert a\vert}$, $b\in \Omega^{\vert b\vert}$, and one has the *graded Jordan identity* $$(-1)^{\vert a\parallel c\vert}[L_{ab},L_c]_{\mathrm{gr}}+(-1)^{\vert b\parallel a\vert}[L_{bc},L_a]_{\mathrm{gr}}+(-1)^{\vert c\parallel b\vert}[L_{ca},L_b]_\mathrm{gr}=0
\label{grJ}$$ for $a\in \Omega^{\vert a\vert},b\in\Omega^{\vert b\vert}, c\in \Omega^{\vert c\vert}$ where $L_a$ is the left-multiplication operator by $a\in \Omega$ defined by $L_a(x)=ax$ for any $x\in \Omega$ and where $[\bullet, \bullet]_{\mathrm{gr}}$ denotes the graded commutator $$[A,B]_{\mathrm{gr}}=AB-(-1)^{\vert a \parallel b\vert}BA$$ for $A$ of degree $\vert a\vert$ and $B$ of degree $\vert b\vert$. The differential $d$ satisfies $$d^2=0$$ $$d\Omega^n\subset \Omega^{n+1}$$ for any $n\in \mathbb N$, and the graded Leibniz rule $$d(ab)=d(a)b+(-1)^{\vert a\vert} ad(b)$$ for $a\in \Omega^{\vert a\vert}$, $b\in \Omega$.\
In the following the real unital differential graded Jordan algebras will be our models for the "algebras of differential forms\" on "quantum spaces\".\
Let $J$ be a Jordan algebra. A differential graded Jordan algebra $\Omega=\oplus_{n\geq 0}\Omega^n$ such that $\Omega^0=J$ will be called a *differential calculus over* $J$.\

## Higher order derivation-based differential calculi

Let $J$ be a unital Jordan algebra with center $Z(J)$ and let $\Omega^n_{{\mbox{\tiny Der}}}(J)$ be the $J$-module of all $n$-$Z(J)$-linear antisymmetric mappings of ${\mbox{Der}}(J)$ into $J$, that is $\omega\in \Omega^n_{{\mbox{\tiny Der}}}(J)$ is a $Z(J)$-linear mapping $$\omega:\wedge^n_{Z(J)} {\mbox{Der}}(J)\rightarrow J$$ of the n-th exterior power over $Z(J)$ of the $Z(J)$-module ${\mbox{Der}}(J)$ into $J$ as a $Z(J)$-module. Then $\Omega_{{\mbox{\tiny Der}}}(J)=\oplus_{n\geq 0} \ \Omega^n_{{\mbox{\tiny Der}}}(J)$ is canonically a differential graded Jordan algebra with differential given by the Chevalley-Eilenberg formula $$\begin{array}{ll}
d\omega(X_0,\cdots,X_n) & =  \sum_{0\leq k\leq n} (-1)^k X_k\  \omega(X_0,\stackrel{k\atop \vee}{\cdots},X_n) \\
&+ \sum_{0\leq r<s\leq n}(-1)^{r+s}\ \omega([X_r,X_s],X_0,\stackrel{r\atop \vee}{\cdots} \stackrel{s\atop \vee}{\cdots},X_n)
\end{array}
\label{C-E}$$ for $\omega\in \Omega^n_{{\mbox{\tiny Der}}}(J)$ and $X_p\in {\mbox{Der}}(J)$. Thus $\Omega_{{\mbox{\tiny Der}}}(J)$ is a differential calculus over $J$ which will be referred as the *derivation-based differential calculus* over $J$.\
If $J$ is a finite-dimensional simple Euclidean Jordan algebra, (i.e. one of the list of Theorem 2), one has

$$\Omega_{{\mbox{\tiny Der}}}(J)=J\otimes \wedge {\mbox{Der}}(J)^\ast
\label{omegaJ}$$ where $\wedge{\mbox{Der}}(J)^\ast$ is the exterior algebra of the dual of the finite-dimensional real Lie algebra ${\mbox{Der}}(J)$. In the case where $J$ is the exceptional Jordan algebra $J^8_3$, this differential calculus is characterized by the following universal property.

::: proposition
[]{#dex label="dex"} Any homomorphism $\varphi$ of unital Jordan algebra of $J^8_3$ into the Jordan subalgebra $\Omega^0$ of a unital differential graded Jordan algebra $\Omega=\oplus \Omega^n$ has a unique extension $\tilde\varphi:\Omega_{{\mbox{\tiny Der}}}(J^8_3)\rightarrow \Omega$ as a homomorphism of differential graded Jordan algebras.
:::

(sketch of). By using the fact that the $J^8_3$-modules are of the form $J^8_3\otimes {\cal E}$ for some vector spaces ${\cal E}$ and the definition of the $\mathbb N$-graded Jordan superalgebras, Formulae ([\[grcom\]](#grcom){reference-type="ref" reference="grcom"}) and ([\[grJ\]](#grJ){reference-type="ref" reference="grJ"}), it follows that any unital differential graded Jordan algebra $\Omega=\oplus \Omega^n$ which contains $J^8_3$ as unital Jordan subalgebra of $\Omega^0$ is as algebra of the form $$\Omega=J^8_3\otimes \Omega_{(0)}$$ where $\Omega_{(0)}=\oplus \Omega^n_{(0)}$ is an associative graded-commutative algebra (this generalizes a classical result in the non graded case). The proof follows then from Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"}, from $d^2=0$ with the graded Leibniz rule for $d$ and from the simplicity of $J^8_3$. $\square$\
A more detailed proof will appear in a forthcoming paper.\
. Notice that as Proposition [\[univ\]](#univ){reference-type="ref" reference="univ"}, Proposition [\[dex\]](#dex){reference-type="ref" reference="dex"} is very specific to the exceptional Jordan algebra $J^8_3$.\
As a consequence all differential calculus over $J^8_3$ which are generated as differential graded Jordan algebra by $J^8_3$ are quotients of $\Omega_{\mbox{\tiny Der}}(J^8_3)$, in particular among these, one has all the differential graded Jordan algebras of the form

$$\Omega=J^8_3\otimes \wedge {\mathfrak g}^\ast
 \label{diffexc}$$ where ${\mathfrak g}$ is a Lie subalgebra of ${\mbox{Der}}(J^8_3)=\frak f_4$, the differential being the Chevalley-Eilenberg differential (${\mathfrak g}$ acting by derivations on $J^8_3$).

## Differential calculi as $A_\infty$-algebras

Let ${\cal A}$ be a complex unital $\ast$-algebra and let $\Omega_u({\cal A})=\oplus_{n\geq 0}\Omega^n_u({\cal A})$ be the universal differential calculus over ${\cal A}$, [@kar:1983]. It is shown in [@wor:1989] (see also in [@mdv:2001]) that there is a unique involution on $\Omega_u({\cal A})$ which extends the involution of ${\cal A}$ for which it is a differential graded $\ast$-algebra. This means that one has $$\left\{
 \begin{array}{l}
 (\alpha\beta)^\ast=(-1)^{ab}\beta^\ast \alpha^\ast\\
 d(\gamma^\ast)=(d\gamma)^\ast
 \end{array}
 \right.
 \label{stardga}$$ for any $\alpha\in\Omega^a_u({\cal A}),\beta\in\Omega^b_u({\cal A})$ and $\gamma\in\Omega_u({\cal A})$. The cohomology of $\Omega_u({\cal A})$ is trivial, i.e. $H^n(\Omega_u({\cal A}))=0$ for $n\geq 1$ and $H^0(\Omega_u({\cal A}))=\mathbb C$, and in fact by using a linear form $\omega$ on ${\cal A}$ such that $\omega(\mbox{\rm 1\hspace {-.6em} l})=1$, one constructs a linear mapping $K$ of degree -1 on $\Omega_u({\cal A})$ such that $$dK+Kd=I
 \label{coho}$$ on $\oplus_{n\geq 1}\Omega^n_u({\cal A})$ (see in [@mdv:2001]). By replacing $K$ by $\frac{1}{2}(K+K^\ast)$ one can assume that $K(\alpha^\ast)=K(\alpha)^\ast$ for any $\alpha\in\Omega_u({\cal A})$.\
Let $J={\cal H}({\cal A})$ be the real Jordan algebra of the hermitian elements of ${\cal A}$, i.e. $J=\{h\in {\cal A}\vert h^\ast=h\}$ endowed with the product $$h\circ h'=\frac{1}{2}(hh'+h'h)$$ for $h,h'\in J$. Then the real graded subspace $\Omega(J)$ of $\Omega_u({\cal A})$ of hermitian elements is a real differential graded Jordan algebra, that is a differential calculus over $J$ for the graded Jordan product defined by $$\alpha\circ \beta=\frac{1}{2}(\alpha\beta+(-1)^{ab}\beta\alpha)
 \label{grJ}$$ for $\alpha\in\Omega^a(J),\beta\in\Omega^b(J)$.\
The contracting homotopy $K$ restricts to $\Omega(J)$. By using $K$, one constructs by induction on $n$ a sequence of product $m_n(\alpha_1,\cdots,\alpha_n)$ of respective degrees $2-n$ on $\Omega(J)$ starting with $m_1(\alpha)=d\alpha$ and $m_2(\alpha,\beta)=\alpha\circ \beta$ such that, endowed with these products, $\Omega(J)$ is an $A_\infty$-algebra [@kel:2001]. This implies in particular that the graded Jordan product $\alpha\circ \beta$ of $\Omega(J)$ is associative up to homotopy. In fact, by taking $$m_3(\alpha,\beta,\gamma)=K((\alpha\circ\beta)\circ \gamma-\alpha\circ(\beta\circ \gamma))
 \label{m3}$$ for $\alpha\in\Omega^a(J), \beta\in\Omega^b(J),\gamma\in\Omega^c(J)$ with $a+b+c\geq 1$, one gets $$(\alpha\circ\beta)\circ \gamma-\alpha\circ (\beta\circ \gamma)=d(m_3) (\alpha,\beta,\gamma)$$ i.e. the associativity up to homotopy of the graded Jordan product.\
The occurrence of $A_\infty$-structures in the present context is not accidental. For instance it will be shown in another paper that, for the simple finite dimensional Euclidean Jordan algebras of Theorem 2, the derivation-based differential calculus admits such $A_\infty$-structures with $m_1$ given by the differential and $m_2$ given by the graded Jordan product.
