---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.697
latex_coverage_ratio: 0.976
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
The Beilinson conjectures about special values of  [@bei85] are a far reaching generalization of the class number formula for the Dedekind zeta function. For every algebraic variety $X$ over the rationals it predicts the leading term of the Taylor expansions of $L(H^i(X),s)$ at certain points, up to a rational multiple, in terms of arithmetic information associated with $X$, namely, its algebraic K-groups $K_j(X)$ [@qui73b]. More generally, these conjectures can also be formulated for motives.

There have been several important steps taken towards verification of these conjectures in various cases, although, strictly speaking they have only been verified completely in the case where $X$ is the spectrum of a number field, where they follow from famous theorems of Borel [@Borel74; @Borel77].

To motivate what follows, let us briefly recall the conjecture that interests us the most (for an introduction see [@DenSch91; @schn88]). One associates with $X$ two cohomology groups. The first one is the Deligne cohomology $\hd^i(X_{/\R},\R(n))$, which is an $\R$-vector space. The second is ''integral'' motivic cohomology $\hm^i(X_{/\Z},\Q(n))$, which may be defined as a certain subspace of $K_{2n-i}(X)\tensor_\Z \Q$. There is a regulator map defined by Beilinson, $$\label{regmap}
 \hm^i(X_{/\Z},\Q(n)) \to \hd^i(X_{/\R},\R(n))
\,.$$ If $2n > i+1$ then $\det\hd^i(X_{/\R},\R(n))$ has a rational structure coming from the relations between $\hd^i(X_\R,\R(n))$ and the de Rham and singular cohomology groups of $X$ [@schn88 p.30].

The first part of the conjecture is that the map in [\[regmap\]](#regmap){reference-type="eqref" reference="regmap"} induces an isomorphism between the lefthand side tensored with $\R$ and the righthand side, and consequently provides a second rational structure on $\det\hd^i(X_{/\R},\R(n))$. The second part of the conjecture states that, assuming a suitable functional equation for $L(H^{i-1}(X),s)$, these two rational structures differ from each other by the leading term in the Taylor expansion of $L(H^{i-1}(X),s)$ at $s=i-n$. Because of the expected functional equation one can reformulate the conjecture in terms of $L(H^{i-1}(X),n)$ (see [@bei85 Corollary 3.6.2] or [@Jan88b 4.12]).

As mentioned before, this conjecture has only been verified in the case of number fields, due to difficulties in the computation of motivic cohomology. What has been verified in several other cases is a form of the conjecture in which one assumes the first part. For this one finds $\dim_{\R} \hd^i(X_{/\R},\R(n))$ elements of $\hm^i(X_{/\Z},\Q(n))$, checks that their images under [\[regmap\]](#regmap){reference-type="eqref" reference="regmap"} are independent, hence should form a basis of $\hm^i(X_{/\Z},\Q(n))$ according to the first part of the conjecture, and verifies the second part using these elements.

The idea that there should be a $p$-adic analogue of Beilinson's conjectures has been around since the late 80's. Such a conjecture was formulated and proved by Gros in [@Gro90; @Gro94] in the case of Artin motives associated with Dirichlet characters. In the weak sense mentioned before, it was proved for certain CM elliptic curves in [@Col-Gro89] (where the relation with the syntomic regulator is proved in [@Bes98b] and further elucidated in [@Bes-Den99]), and for elliptic modular forms it follows from Kato's work (see [@Scho98]).

The book [@Peri96] contains a very general conjecture about the existence and properties of , from which one can derive a Beilinson conjecture. Rather than explain this in full detail we shall give a sketch of this conjecture similar to the sketch above of the Beilinson conjecture.

For the Beilinson conjectures one has to replace Deligne cohomology with syntomic cohomology [@Gro94; @Niz97; @Bes98a], the Beilinson regulator with the syntomic regulator, and with .

Syntomic cohomology $\hsyn^i(Y,n)$ is defined for a smooth scheme $Y$ of finite type over a complete discrete valuation ring of mixed characteristic $(0,p)$ with perfect residue field. For the $\Q$-variety $X$ we obtain, for all but finitely many primes, a map $$\label{regpmap}
 \hm^i(X_{/\Z},\Q(n)) \to \hsyn^i(Y,n)$$ where $Y$ is a smooth model for $X$ over $\Z_p$. This cohomology group is a $\Qp$-vector space.

The theory of starts with Kubota and Leopoldt's $\z$-function [@Kub-Leo], $\z_p(s)$, which is defined by interpolating special values of complex valued Dirichlet . This principle has been extended to $\z$- and in various situations, resulting in corresponding functions for totally real number fields [@Bar78; @Cas-Nog79; @Del-Rib], CM fields [@Kat76; @Kat78] and modular forms [@MTT86]. (Given the occasion, let us note that the approach of Deligne and Ribet using modular forms was initiated by Serre [@Ser73].)

The $p$-adic Beilinson conjecture therefore has many similarities with its complex counterpart. However, there is a very important difference. In general, when $2n>i+1$, there is no hope that [\[regpmap\]](#regpmap){reference-type="eqref" reference="regpmap"} induces an isomorphism after tensoring the lefthand side with $\Q_p$. To see this, consider a number field $k$ with ring of algebraic integers $\O$. By Borel's theorem (see Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"}) we have, in accordance with Beilinson's conjectures, $$\dim_\Q \hm^1(\spec(k)_{/\Z},\Q(n))=
\left\{ 
\begin{aligned}
      r_2 & \text{ when $ n \ge 2 $ is even }
\\
r_1 + r_2 & \text{ when $ n \ge 2 $ is odd }
\end{aligned}
 \right.$$ with $r_1$ (resp. $2 r_2$) the number of real (resp. complex) embeddings of $k$. Thus, motivic cohomology "knows" about the number of real and complex embeddings of $k$, as does, by its definition, Deligne cohomology, which in this case becomes $\hd^1(\spec(k)_{/\R},\R(n)) \iso \{ (x_\s)_{\s: k \to \C} \text{ in } \R(n-1)^{r_1+2r_2} \text{ such that } \overline{x_\s} = x_{\overline \s}\}$. But syntomic cohomology, which depends only on the completion of $k$ at $p$, does not. In this case, we obtain $\hsyn^1(\spec(\O\tensor_\Z\Zp),n) \iso \Q_p^{r_1+2r_2}$.

The solution to this problem suggested in [@Peri96] is to make the depend on a subspace of syntomic cohomology which is complementary to the image of the regulator. While this might seem artificial, there are other reasons for choosing this solution. In most cases one chooses a particular subspace and obtains a special case of the conjecture.

In the important special case of a totally real number field, or more generally an Artin motive over $\Q$, associated with a Galois representation whose kernel is totally real (let us call these totally real Artin motives), no such subspace is required when $n\ge2$ is odd (see Proposition [\[whenconj\]](#whenconj){reference-type="ref" reference="whenconj"}). The same holds for Artin motives where the conjugacy class of complex conjugation acts as multiplication by $-1$ and $n \ge2$ is even (we may think of those as the "negative part\" of CM Artin motives).

If $\chi$ denotes the character associated with either representation, then the Beilinson conjecture relates the regulator of $K_{2n-1}$ with the Artin of $\chi$ at $n$. For the one has to consider $\chi \tensor \omega_p^{1-n}$ with $\omega_p$ the Teichmüller character for the prime number $p$. Then the fixed field of the kernel of the representation underlying $\chi \tensor \omega_p^{1-n}$ is totally real, and it is perhaps no coincidence that in precisely this case the existence of a that is not identicaly zero has been established, by [@Bar78; @Cas-Nog79; @Del-Rib] for the case of fields and by [@greenberg83] for Artin motives.

The goal of the present work is to describe in detail the conjectures for the cases of totally real fields, totally real Artin motives, as well as the "negative part\" of CM Artin motives, and describe the (conjectural) relation between the classical and conjectures. We test everything numerically in several cases, and also deduce most of the conjectures for Abelian Artin motives from work by Coleman [@Col82].

There have been several developments that allow us to carry out this numerical verification. In [@dJ95] de Jeu proved part of Zagier's conjecture concerning a more explicit description of the $K$-theory (tensored with $\Q$) of number fields (see Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"}). While this conjecture is not known to give the K-theory of such fields in all cases, it does in practice. Thus it provides a way of computing them, and Paul Buckingham wrote a computer implementation for this. In [@BdJ03] Besser and de Jeu computed the syntomic regulator for (essentially) the part of the $K$-theory of a number field described by Zagier's conjecture and showed that it is given by applying the polylogarithm. Those polylogarithms were invented by Coleman [@Col82] using his theory of integration but are not so easy to compute. In [@BdJ06] Besser and de Jeu devised an algorithm for this computation. Taken together, these developments allow us to compute [\[regmap\]](#regmap){reference-type="eqref" reference="regmap"} and  [\[regpmap\]](#regpmap){reference-type="eqref" reference="regpmap"} for number fields. Finally, building on earlier work in [@Sol-Rob], Roblot has dealt with the computational aspects of computing for Abelian characters over $\Q$ or a real quadratic field [@Rob06].

This paper is organized as follows. In Section [1](#conjecturesection){reference-type="ref" reference="conjecturesection"} we recall Borel's theorem as well as various facts about and , and formulate a conjectural analogue of Borel's theorem. In Section [\[motivicsection\]](#motivicsection){reference-type="ref" reference="motivicsection"} we introduce Artin motives with coefficients in a number field $E$ in terms of representations of the Galois group, determine when the $\Q$-dimension of the left-hand side of [\[regpmap\]](#regpmap){reference-type="eqref" reference="regpmap"} equals the $\Qp$-dimension of the right-hand side (corresponding to equality in Proposition [\[whenconj\]](#whenconj){reference-type="ref" reference="whenconj"}), define both classical and with coefficients in $E$, and formulate the motivic Beilinson conjecture with coefficients in $E$, Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}, a small part of which is the same as a conjecture by Gross. In Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"} we describe the set-up for finding elements in the $K$-groups of number fields using Zagier's conjecture, and the classical and regulators on them. We also prove most of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} for Abelian Artin motives over $\Q$ (Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"} and Remark [\[abelrem\]](#abelrem){reference-type="ref" reference="abelrem"}). In Section [\[practical\]](#practical){reference-type="ref" reference="practical"} we discuss a few computational aspects of implementing Zagier's conjecture and describe the Artin motives that we consider later for the numerical examples, and in the process prove Gross's conjecture for Artin motives obtained from $S_3$ and $D_8$-extensions of $\Q$. Then in Section [\[pLsection\]](#pLsection){reference-type="ref" reference="pLsection"} we sketch how the can be computed in certain cases, and make the required Brauer induction explicit for the Artin motives we want to consider. Finally, the last section is devoted to the results of the numerical calculations for examples.

Amnon Besser, Paul Buckingham and Rob de Jeu would like to thank the EC network Arithmetic Algebraic Geometry for travel support. Rob de Jeu would like to thank the Tata Institute of Fundamental Research for a productive stay during which this paper was worked on, and the Nuffield Foundation for a grant under the Undergraduate Research Bursary programme (NUF-URB03) that enabled Paul Buckingham to develop a computer program for finding the necessary elements in $K$-theory. Amnon Besser would like to thank the Institute for Advanced Study in Princeton for a stay during which part of the paper was worked on, and the Bell companies Fellowship and the James D. Wolfensohn fund for financial support while at the institute. Finally, the authors would like to thank Alfred Weiss for very useful explanations about , and, in particular, for bringing to their attention the paper [@greenberg83].

**Notation** Throughout the paper, for an Abelian group $A$ we let $A_\Q$ denote $A \tensor_\Z \Q$. If $B$ is a subgroup of $\C$ and $n$ an integer then we let $B(n) = (2 \pi i)^n B \subseteq \C$ We normalize the absolute value $|\cdot|_p$ on the field of $p$-adic numbers $\Qp$ in such a way that $|p|_p= p^{-1}$, and use the same notation for its extensions to an algebraic closure $\Qpbar$ and $\Cp = \hat{\overline\Q}_p$.

# The Beilinson conjecture for totally real fields {#conjecturesection}

Let $k$ be a number field with $r_1$ real embeddings, $2r_2$ complex embeddings, ring of algebraic integers $\O$, and discriminant $D_k$. As is well-known, $\O^*$ is a finitely generated Abelian group of rank $r = r_1 + r_2 - 1$, and its regulator $R$ satisfies $w \sqrt{  |D_k| } \, \text{Res}_{s=1}\zeta_k(s) =  2^{ r_1 } (2\pi)^{ r_2 } \, |\text{Cl}(\O )| \, R$, with $\text{Cl}(\O)$ the class group of $\O$, and $w$ the number of roots of unity in $k$. Because $K_0(\O) \iso \text{Cl}(\O) \oplus \Z$ and $K_1(\O) \iso \O^*$, so $|\text{Cl}(\O)| = |K_0(\O)_{\text{tor}}|$ and $w = | K_1(\O)_{\text{tor}} |$, this can be interpreted as a statement about the $K$-theory of $\O$, and it is from this point of view that it can be generalized to $\zeta_k(n)$ for $n \geq 2$. Namely, in [@qui73b], Quillen proved that $K_m(\O)$ is a finitely generated Abelian group for all $m$. Borel in [@Borel74] computed its rank when $m \ge 2$. For $m$ even this rank is zero, but for odd $m$ it is $r_1+r_2$ or $r_2$, and in [@Borel77] he showed that a suitably defined regulator of $K_{2n-1}(\O)$ is related to $\zeta_k(n)$. Since $K_{2n-1}(\O) \rightiso K_{2n-1}(k)$ when $n \ge 2$ we can rephrase his results for $K_{2n-1}(\O)$ in terms of $K_{2n-1}(k)$. Also, we replace Borel's regulator map $\reg_B : K_{2n-1}(\C) \to \R(n-1)$ ($n \ge 2$) with Beilinson's regulator map $\reg_\infty$ (see [@schn88 § 4]), which is half the Borel map regulator by [@Bur02 Theorem 10.9]. Because $k\tensor_\Q\C \iso \oplus_{\s: k \to \C} \C$, and $n > \dim \spec(k\otimes \C)$, we obtain by [@schn88 p.9] $$\label{HDid}
\begin{aligned}
   \hd^1(\spec(k\otimes \C)_{/\R},\R(n))
& \iso
   H^0(\spec(k\otimes \C)_{/\R},\R(n-1))
\cr
& \iso
   \Bigl(\bigoplus_{\s: k\to \C} \R(n-1)\Bigr)^+
\,,
\end{aligned}$$ which consists of those $(x_\s)_\s$ with $x_{\overline\s} = \overline{x_\s}$. Finally, for any embedding $\s : k \to \C$ we let $\s_* : K_{2n-1}(k) \to K_{2n-1}(\C)$ be the induced map.

::: theorem
[]{#boreltheorem label="boreltheorem"}**(Borel)** Let $k$ be a number field of degree $d$, with $r_1$ real embeddings and $2 r_2$ complex embeddings, and let $n \ge 2$. Then the rank $m_n$ of $K_{2n-1}(k)$ equals $r_2$ if $n$ is even and $r_1+r_2$ if $n$ is odd. Moreover, the map $$\label{Bregulator}
\begin{aligned}
 K_{2n-1}(k) & \to \bigoplus_{\s : k \to \C } \R(n-1)
\\
\a & \mapsto (\reg_\infty\circ\s_*(\a))_\s
\end{aligned}$$ embeds $K_{2n-1}(k)/\tor$ as a lattice in $(\oplus_\s \R(n-1))^+ \iso \R^{m_n}$, and the volume $V_n(k)$ of a fundamental domain of this lattice satisfies $$\label{borelq}
 \zeta_k(n)  \sqrt{|D_k|} = q \pi^{n(d-m_n)} V_n(k)$$ for some $q$ in $\Q^*$.
:::

::: remark
[]{#klingensiegelremark label="klingensiegelremark"} In Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} $m_n = 0$ precisely when $k$ is totally real and $n \ge 2$ is odd. In this case the given relation holds (with $V_n(k) = 1$) by the Siegel-Klingen theorem [@Neu99 Chapter VII, Corollary 9.9].
:::

This theorem is equivalent with Beilinson's conjecture for $k$. In order to deal with this in detail (see Remarks [\[BBeq\]](#BBeq){reference-type="ref" reference="BBeq"} and [\[BBmotiverem\]](#BBmotiverem){reference-type="ref" reference="BBmotiverem"}) and in order to introduce we recall some facts about Artin [@Neu99 Chapter VII, § 10-12]. Let $k$ be a number field, $d = [k:\Q]$, and let $\chi$ be a $\C$-valued Artin character of $\Gal(\kbar/k)$. For a prime number $\ell$ we define $$\Eul_\ell(s, \chi, k) =  \prod_{\mathfrak{l} \mid \ell} \Eul_{\mathfrak l}(s,\chi,k)$$ where $\Eul_{\mathfrak l}(s,\chi,k)$ is the reciprocal of the Euler factor for $\mathfrak l$ and the product is over primes $\mathfrak l$ of $k$ lying above $\ell$. Then for $s \in \C$ with $\Re(s)>1$ we can write the Artin of $\chi$ as $$\L s {\chi} k = \prod_\ell \Eul_\ell(s,\chi,k)^{-1} 
\,.$$ For an infinite place $v$ of $k$ we let $$L_v(s, \chi, k) = \left\{
\begin{aligned}
& \hbox to 1.5 in {$ L_\C(s)^{\chi(1)} $\hfill}\hbox to 1.5 in{when $ v $ is complex,\hfill}
\\
& \hbox to 1.5 in {$ L_\R(s)^{n^+} L_\R(s+1)^{n^-} $\hfill}\hbox to 1.5 in{when $ v $ is real,\hfill}
\end{aligned}
\right.$$ where $L_\R(s) = \pi^{-s/2} \Gamma(s/2)$, $L_\C(s) = 2 (2\pi)^{-s}  \Gamma(s)$ and $n^\pm = \frac d2 \overline\chi(1) \pm \sum_v  \frac 12 \overline\chi(\Fr_w)$, with the sum taken over the real places $v$ of $k$ and $\Fr_w$ the generator of the image of $\Gal(\C/\R)$ in $\Gal(\kbar/k)$ corresponding to any extension $w : \kbar \to \C$ of $v$. Then $$\Lambda(s, \chi, k) =  \L s {\chi} k \prod_{v|\infty} L_v(s, \chi, k)$$ extends to a meromorphic function, satisfying the functional equation (cf. [@Neu99 p. 541]) $$\Lambda(s, \chi, k) = W(\chi) C(\chi,k)^{1/2}  C(\chi,k)^{-s} \Lambda(1-s, \overline\chi, k)$$ with $W(\chi)$ a constant of absolute value 1 and $C(\chi,k) = |D_k|^{\chi(1)} \Nm_{k/\Q}(\f(\chi,k))$ for $\f(\chi,k)$ the Artin conductor of $\chi$. Therefore $$\label{oldfuneq}
\begin{aligned}
\L 1-s {\overline\chi} k 
& =
W(\overline\chi) C(\overline\chi,k)^{s-\frac12} (2 (2\pi)^{-s}\Gamma(s))^{d\overline\chi(1)}
\\
& \qquad\times
 (\cos(\pi s/2))^{n^+}  (\sin(\pi s/2))^{n^-} \L s {\chi} k 
\,.
\end{aligned}$$

Following [@greenberg83 pp. 80--81] we shall now describe a $\Lp p s {\chi} k$ when $k$ is a totally real number field, $p$ a prime and $\chi : \Gal(\kbar/k) \to \Qpbar$ a suitable Artin character. We begin with the case of 1-dimensional Artin characters.

If $\sigma:\Qpbar \to \C$ is any isomorphism then $\sigma \circ \chi$ is a complex Artin character, so we have the Artin $\L s {\sigma\circ\chi} k$. We may also view $\chi$ as a character of a suitable ray class group, so by [@Neu99 Corollary 9.9 and page 509] all $\L m {\sigma\circ\chi} k$ for $m \in \Z_{\leq 0}$ are in $\Q(\s\circ\chi)$ and the values $$\label{sigmaindependence}
  \Ls m {\chi} k = \sigma^{-1}(\L m {\sigma\circ\chi} k )$$ are independent of the choice of $\sigma$.

In the same way, we define $$\label{sigmaeuler}
\Eul^\ast_\ell(m, \chi, k) = \sigma^{-1} (\Eul_\ell(m,\sigma\circ\chi, k)) \,,$$ which is clearly independent of the choice of $\s$. To construct the one finds a analytic or meromorphic function on an open ball around 0 that interpolates the values $\Ls m {\chi} k$. For 1-dimensional $\chi$ with the fixed field $k_\chi$ of its kernel totally real this was achieved independently by Deligne and Ribet [@Del-Rib], Barsky [@Bar78], and Cassou-Noguès [@Cas-Nog78; @Cas-Nog79]. We shall sketch a proof of the following theorem and Remark [\[interpolrem\]](#interpolrem){reference-type="ref" reference="interpolrem"} below in Section [\[pLsection\]](#pLsection){reference-type="ref" reference="pLsection"}. (When $k_\chi$ is not totally real the is identically zero since the values interpolated are all zero by the functional equation of the .)

::: theorem
[]{#padicLfunction label="padicLfunction"} For $p$ prime, let $\mathcal{B}$ in $\Cp$ be the open ball with centre $0$ and radius $qp^{-1/(p-1)}$ where $q = p$ if $p>2$ and $q=4$ if $p=2$. If $k$ is a totally real number field and $\chi : \Gal(\kbar/k) \to \Qpbar$ a $1$-dimensional Artin character, then there exists a unique $\Cp$-valued function $\Lp p s {\chi} k$ on $\mathcal{B}$ satisfying the following properties:

1.  $\Lp p s {\chi} k$ is analytic if $\chi$ is non-trivial and meromorphic with at most a simple pole at $s = 1$ if $\chi$ is trival;

2.  if $m$ is a negative integer such that $m \equiv 1$ modulo $\varphi(q)$ then $$\Lp p m {\chi} k = \Eul^\ast_p(m,\chi,k) \Ls m {\chi} k 
          \,.$$
:::

If $\chi : \Gal(\kbar/k) \to \Qpbar$ is any Artin character then by Brauer's induction theorem [@Neu99 (10.3)] there exist 1-dimensional Artin characters $\chi_1, \dots,\chi_t$ on subgroups $G_1,\dots,G_t$ of $\Gal(\kbar/k)$ of finite index, and integers $a_1, \dots, a_t$, such that $$\label{brauerinduction}
  \chi = \sum_{i=1}^t a_i \Ind {G_i} {\Gal(\kbar/k)} (\chi_i)
\,.$$ If $k_\chi$ is totally real then we can assume that the same holds for the fixed fields $k_i$ of the $G_i$, and we define the of $\chi$ by $$\label{artinLp}
  \Lp p s {\chi} k = \prod_{i=1}^t \Lp p s {\chi_i} k_i  ^{a_i}
\,,$$ which is a meromorphic function on $\mathcal{B}$ (see Section [\[pLsection\]](#pLsection){reference-type="ref" reference="pLsection"}). For any negative integer $m \equiv 1$ modulo ${\varphi(q)}$ the value $\Lp p m {\chi} k$ is defined and equals $\Eul^\ast_p(m,\chi,k) \Ls m {\chi} k$ by well-known properties of Artin  (see [@Neu99 Prop. 10.4(iv)]), showing the function is independent of how we express $\chi$ as a sum of induced 1-dimensional characters.

::: remark
In [@greenberg83], Greenberg proves that the Main Conjecture of Iwasawa theory implies the $p$-adic Artin conjecture, that is, that the of an Artin character $\chi$ is analytic on the open ball $\mathcal{B}$ if it does not contain the trivial character, and has at most a simple pole at $s=1$ otherwise. It therefore follows from the proof of the Main Conjecture by Mazur and Wiles [@MW84] for $p$ odd that $\Lp p n {\chi} k$ for $p\ne2$ is defined for all integers $n\ne1$. In particular, the values of the in Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} below exist by Theorem [\[padicLfunction\]](#padicLfunction){reference-type="ref" reference="padicLfunction"}, and those in Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} exist when $p\ne2$ but have to be assumed to exist when $p = 2$.
:::

::: remark
[]{#interpolrem label="interpolrem"} Let $W_p \subset \Z_p^*$ be the subgroup of $(p-1)$-th roots of unity if $p$ is odd and let $W_2 = \{\pm 1\}$. The Teichmüller character on $\Gal(\kbar/k)$ is defined as the composition $$\label{TM}
\omega_p: \Gal(\kbar/k) \to \Gal(\Qbar/\Q) \to \Gal(\Q(\mu_q)/\Q) \rightiso (\Z/q\Z)^* \rightiso W_p
\,,$$ where the last map sends an element of $(\Z/q\Z)^*$ to the unique element of $W_p$ to which it is congruent modulo $q$. For an Artin character $\chi : \Gal(\kbar/k) \to \Qpbar$ and an integer $l$, $\chi\omega_p^l$ is also an Artin character. If $m \le 0$ satisfies $l+ m \equiv 1$ modulo ${\varphi(q)}$ and either $\chi$ is 1-dimensional or $k_\chi$ is totally real then $\Lp p m {\chi\omega_p^l} k = \Eul_p^*(m, \chi, k) \Ls m {\chi} k$.
:::

The Beilinson conjecture is going to predict the special values of in terms of a regulator. The required regulator is the syntomic regulator [@Bes98a Theorem 7.5]. Let $F$ be a complete discretely valued field of characteristic $0$ with perfect residue field of characteristic $p$ and let $X$ be a scheme that is smooth and of finite type over the valuation ring ${\OO}_F$. Then the above mentioned paper associates to $X$ its rigid syntomic cohomologies $\hsyn^i(X,n)$, as well as syntomic regulators (i.e., Chern characters) $\reg_p: K_{2n-i}(X) \to
\hsyn^i(X,n)$. In this work, unlike in [@Bes98a], we shall need to change the base field $F$. We therefore prefer to denote the syntomic cohomology by $\hsyn^i(X/\OO_F,n)$. For the formulation of the conjecture the following basic fact is required.

::: lemma
[]{#synlemma label="synlemma"} We have $\hsyn^1(\spec(\OO_F)/\OO_F,n) \isom F$, for all $n>0$ and consequently we have a syntomic regulator $\reg_p: K_{2n-1}(\OO_F)\to F$. Furthermore, the map $\reg_p$ commutes in the obvious way with finite extensions of fields and with automorphisms of such fields, provided that their residue fields are algebraic over the prime field.
:::

::: proof
*Proof.* The first claim follows from part 3 of [@Bes98a Proposition 8.6]. For the second claim we note that by part 4 of the same proposition we have in this case an isomorphism between syntomic and modified syntomic cohomology (the latter only exists under the additional assumption on the residue field). The compatibility with finite base changes now follows from the same result for modified syntomic cohomology in [@Bes98a Proposition 8.8]. The same holds for automorphisms, although not explicitly stated in the above reference, since the relevant base change results, e.g., Proposition 8.6.4, hold for this type of base change as well. ◻
:::

As a consequence of the lemma we can also, by abuse of notation, define for any complete discretely valued subfield $F\subset \Qpbar$ the regulator $\reg_p: K_{2n-1}(\OO_F)\to F$. In [@BdJ03], two of the authors of the present work showed how one can sometimes compute the map $\reg_p$ by using polylogarithms.

We now restrict our attention to a totally real number field $k$ with $[k:\Q] = d$. Our goal will be to formulate a conjecture that is the analogue of Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} for $K_{2n-1}(k)$ with $n \ge 2$. Since this $K$-group is torsion when $n$ is even but has rank $d$ when $n$ is odd, we only consider odd $n\ge 2$.

In preparation for the more general construction that will follow in Section [\[motivicsection\]](#motivicsection){reference-type="ref" reference="motivicsection"} let us first reformulate Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} in this special case. Let $a_1,\dots,a_d$ form a $\Z$-basis of $\O$ and let $\s_1^\infty,\dots,\s_d^\infty$ be the embeddings of $k$ into $\C$. Then we define $\Drt = \det(\s_i^\infty(a_j))$, a real root of the discriminant of $k$. Similarly, if $\a_1,\dots,\a_d$ form a $\Z$-basis of $K_{2n-1}(k)/\tor$ then we let $R_{n,\infty}(k) = \det(\reg_\infty\circ\s_{i*}^\infty(\a_j))$. Then $\Drt$ and $R_{n,\infty}(k)$ are well-defined up to sign, and the relation in Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} in this case is equivalent with $$\label{rat}
\zeta_k(n)  D_k^{1/2,\infty} = q(n,k) R_{n,\infty}(k)$$ with $q(n,k)$ in $\Q^*$.

Now let $F \subset \Qpbar$ be the topological closure of the Galois closure of $k$ embedded in $\Qpbar$ in any way. If $\s_1^p,\dots,\s_d^p$ are the embeddings of $k$ into $F$ then $\Drtp = \det(\s_i^p(a_j))$ is a root in $F$ of the discriminant of $k$. For $\s : k \to F$ an embedding we denote the induced map $K_{2n-1}(k) \to K_{2n-1}(F)$ by $\s_*$. Then we define a regulator in $F$ by $R_{n,p}(k) = \det(\reg_p\circ\s_{i*}^p(\a_j))$. Both $\Drtp$ and $R_{n,p}(k)$ are well-defined up to sign.

Remark [\[interpolrem\]](#interpolrem){reference-type="ref" reference="interpolrem"} suggests that the role of $\zeta_k(n)$ in a analogue of Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} should be played by $\Lp p n \omega_p^{1-n} k / \Eul_p(n,k)$ where $\z_k(s) = \prod_l \Eul_l(s,k)^{-1}$ for $\Re(s) > 1$, so we can hope that $$\Lp p  n \omega_p^{1-n} k  \Drtp  = q_p(n,k) \, \Eul_p(n,k) R_{n,p}(k)$$ for some $q_p(n,k)$ in $\Q^*$.

More precisely, because $R_{n,\infty}(k) / \Drt$ and $R_{n,p}(k) / \Drtp$ are invariant under reordering the $\s_i^\infty$ or $\s_i^p$, and transform in the same way if we change the bases of $\O$ and $K_{2n-1}(k)/\tor$, we can make the following conjecture.

::: conjecture
[]{#pborel label="pborel"} For $k$ a totally real number field, $p$ prime, and $n \ge 2$ odd, we have, with notation as above:

1.  in $F$ the equality $$\Lp p  n \omega_p^{1-n} k   D_k^{1/2,p}  =   q_p(n,k) \, \Eul_p(n,k) R_{n,p}(k)$$ holds for some $q_p(n,k)$ in $\Q^*$;

2.  in fact, $q_p(n,k) = q(n,k)$;

3.  $\Lp p n \omega_p^{1-n} k$ and $R_{n,p}(k)$ are non-zero.
:::

As mentioned in the introduction, this, and the corresponding parts of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} below, can be deduced (with some effort) from a much more general conjecture of Perrin-Riou [@Peri96 4.2.2].

::: remark
The conjecture is similar to the result that the residue of $\z_p(s,k)$ at $s=1$ is related to the Leopoldt regulator of $\O^*$ through exactly the same formula as for the residue of $\z(s,k)$ and the Dirichlet regulator [@Colm88], with part(4) corresponding to the Leopoldt conjecture. However, we have not tried to determine if Colmez's normalization of the sign for the regulator is the same as here, especially given the sign error in the proof of Lemma 4.3 in loc. cit. (see Section [\[pLsection\]](#pLsection){reference-type="ref" reference="pLsection"}).
:::

::: remark
[]{#basisremark label="basisremark"} We can use a basis of a subgroup of finite index of $K_{2n-1}(k)/\tor$ in the definition of $R_{n,\infty}(k)$ and $R_{n,p}(k)$, or even a $\Q$-basis of $\Kn k$, without affecting the rationality of $q(n,k)$, $q_p(n,k)$ or their equality. Similarly we can replace the $\Z$-basis of $\O$ with a $\Q$-basis of $k$ in the definitions of $\Drt$ and $\Drtp$.
:::

::: remark
[]{#BBeq label="BBeq"} As is well-known, for $k$ and $n$ as in Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"}, by [\[oldfuneq\]](#oldfuneq){reference-type="eqref" reference="oldfuneq"} $\z_k(s)$ at $s=1-n$ has a zero of order $d$ and the first non-zero coefficient in its Taylor expansion, $\z_k^\sharp(1-n)$, equals $(2 \pi i )^{d(1-n)} ((n-1)!/2)^d  D_k^{n-1/2} \z_k(n)$. If we take $\Drt = D_k^{1/2}$ in [\[rat\]](#rat){reference-type="eqref" reference="rat"} then we obtain $$\z_k^\sharp(1-n) =  ((n-1)!/2)^d q(n,k) D_k^{n-1} \widetilde R_{n,\infty}(k)$$ for Beilinson's renormalized regulator $\widetilde R_{n,\infty}(k) = (2\pi i)^{d(1-n)} R_{n,\infty}(k)$. In computer calculations $((n-1)!/2)^d q(n,k) D_k^{n-1}$ often has only relatively small prime factors, so the larger prime factors in $q(n,k)$ correspond to $D_k^{1-n}$. This phenomenon also occurs in the calculations for Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} below (see Remark [\[constantremark\]](#constantremark){reference-type="ref" reference="constantremark"}).
:::

::: remark
\(1\) The thought that $\Lp p n \omega_p^{1-n} k$ is non-zero for $n \ge 2$ and odd when $k$ is a totally real Abelian extension of $\Q$ is mentioned by C. Soulé in [@sou81 3.4].

\(2\) F. Calegari [@Cal05] (see also [@Beu06]) proved that, for $p=2$ and 3, $\z_p(3)$, which in those cases equals $\Lp p 3 \omega_p^{-2} {\Q}$, is irrational. (More results along these lines are described in Remark [\[newrem\]](#newrem){reference-type="ref" reference="newrem"}(3).)

\(3\) Parts (1) and (2) of Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} hold when $k$ is a totally real Abelian number field, and in fact the corresponding parts of a much stronger conjecture that we shall describe in Section [\[motivicsection\]](#motivicsection){reference-type="ref" reference="motivicsection"} hold for cyclotomic fields (see Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"}).

\(4\) We numerically verified part (3) of Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"}, and its more refined version Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(4) below, in certain cases; see Remark [\[dirichletcalculations\]](#dirichletcalculations){reference-type="ref" reference="dirichletcalculations"} and Section [\[examplesection\]](#examplesection){reference-type="ref" reference="examplesection"}.
:::
