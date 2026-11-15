---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-002-3-a-motivic-version-of-the-conjecture
section_title: "A motivic version of the conjecture"
section_number: 3
pages: 9-17
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.969
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
[]{#motivicsection label="motivicsection"}

If $E$ is any extension of $\Q$, and $k/\Q$ is finite and Galois with Galois group $G$, then we let $M^E = E \tensor_\Q k$ and $\KnE k = E \tensor_\Q \Kn k$, which are $E[G]$-modules. The goal of this section is to refine Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} to a conjecture for Artin motives with coefficients in $E$, or equivalently, idempotents in the group ring $E[G]$, when $E$ is a number field.

::: definition
For an idempotent $\pi$ in $E[G]$ we let $M_\pi^E = \pi M^E$ and $K_{2n-1} (M_\pi^E) = \pi \KnE k$.
:::

Now fix an embedding $\phi_\infty : k \to \C$. The pairing $G \times k \to \C$ mapping $(\s,a)$ to $\phi_\infty(\s(a))$ leads to an $E$-bilinear pairing $$\begin{aligned}\label{discpairing}
E[G] \times M^E & \to E \tensor_\Q \C
\cr
(e \s, e' \tensor a ) & \mapsto e e' \tensor \phi_\infty(\s(a))
\,.
\end{aligned}$$ and we consider its restriction $$(\,\cdot\,,\,\cdot\,)_\infty : E[G]\pi \times M_\pi^E \to E \tensor_\Q \C
\,.$$ Similarly, replacing $\phi_\infty$ with a fixed embedding $\phi_p : k \to \Qpbar$ we obtain $$(\,\cdot\,,\,\cdot\,)_p : E[G]\pi \times M_\pi^E \to E \tensor_\Q F
\,.$$ where $F \subset \Qpbar$ is the topological closure of $\phi_p(k)$, which is independent of $\phi_p$ since $k/\Q$ is Galois.

::: lemma
[]{#dimlemma label="dimlemma"} Let $\pi$ in $E[G]$ be an idempotent. Then $\dim_E(M_\pi^E) = \dim_E(E[G]\pi)$.
:::

::: proof
*Proof.* Since $\pi^2 = \pi$, [\[discpairing\]](#discpairing){reference-type="eqref" reference="discpairing"} is identically 0 on $E[G]\pi \times  M_{1-\pi}^E$ and $E[G](1-\pi) \times  M_\pi^E$. But the determinant of this pairing is, up to multiplication by $E^*$, equal to $D_k^{1/2,\infty}$, hence non-zero. This implies the lemma. ◻
:::

We now introduce pairings similar to $(\cdot,\cdot)_\infty$ and $(\cdot,\cdot)_p$ but replacing $M_\pi^E$ with $\KMn M_\pi^E$. If we denote the map $\Kn k \to \Kn {\C}$ induced by $\phi_\infty$ by $\phi_{\infty*}$ and let $\Phi_\infty$ be the composition with the Beilinson regulator map $\reg_\infty$ for $\C$, $$\Phi_\infty = \reg_\infty \circ \phi_{\infty*} : \Kn k \to \Kn {\C} \to \R(n-1) \subset \C
\,,$$ then the pairing $G \times \Kn k \to \C$ given by mapping $(\s,\a)$ to $\Phi_\infty(\s(\a))$ gives rise to an $E$-bilinear pairing $$\label{EKpairing}
\begin{aligned}
E[G] \times \KMn M^E & \to E \otimes_\Q \C
\\
(e\s, e' \tensor \a ) & \mapsto  e e' \tensor \Phi_\infty(\s(\a))
\end{aligned}$$ and we consider its restriction $$_\infty : E[G]\pi \times \KMn M_\pi^E \to E \tensor_\Q \C
\,.$$

By Lemma [\[synlemma\]](#synlemma){reference-type="ref" reference="synlemma"} and the definition of $F$ the syntomic regulator gives us $$\reg_\syn : \Kn {\OO_F} \to F
\,.$$ If we write $\phi_{p*}$ for the composition $\Kn k \iso \Kn {\O} \to \Kn {\OO_F}$, with the second map induced by $\phi_p : k \to F$, and let $\Phi_p$ be the composition $$\reg_\syn \circ \phi_{p*} : \Kn k \to \Kn {F} \to F
\,,$$ then we can similarly obtain a pairing $$_p : E[G]\pi \times \KMn M_\pi^E \to E \tensor_\Q F
\,.$$

We now fix ordered $E$-bases of $E[G]\pi$, $M_\pi^E$, and $\KMn M_\pi^E$.

::: definition
[]{#discdef label="discdef"} For $*=\infty$ or $p$ we let $D(M_\pi^E)^{1/2,*}$ be the determinant of the pairing $(\cdot,\cdot)_*$, computed with respect to our fixed bases of $E[G]\pi$ and $M_\pi^E$.
:::

Note that $D(M_\pi^E)^{1/2,\infty}$ is non-zero by the proof of Lemma [\[dimlemma\]](#dimlemma){reference-type="ref" reference="dimlemma"}, and the same argument works for $D(M_\pi^E)^{1/2,p}$.

::: definition
[]{#regdef label="regdef"} If $\dim_E(E[G]\pi)$ equals $\dim(\KMn M_\pi^E )$ then for $*=\infty$ or $p$ we let $R_{n,\infty}(M_\pi^E)$ be the determinant of the pairing $[\cdot,\cdot]_*$, computed with respect to our fixed bases of $E[G]\pi$ and $\KMn M_\pi^E$.
:::

For future use we prove the following.

::: lemma
[]{#Qpquot label="Qpquot"} If $\dim_E(E[G]\pi) = \dim(\KMn M_\pi^E )$ then

1.  $R_{n,\infty}(M_\pi^E) / D(M_\pi^E)^{1/2,\infty}$ is independent of the basis of $E[G]\pi$, of $\phi_\infty$, and lies in $E \tensor \R$;

2.  $R_{n,p}(M_\pi^E) / D(M_\pi^E)^{1/2,p}$ is independent of the basis of $E[G]\pi$, of $\phi_p$, and lies in $E \tensor \Qp$.
:::

::: proof
*Proof.* We prove the second statement, the proof of the first being entirely similar. Choosing a different $E$-basis of $E[G]\pi$ corresponds to letting an $E$-linear transformation act on $E[G]\pi$, and in the given quotient the resulting determinant cancels. Since $k/\Q$ is Galois we get all possible embeddings of $k$ into $\Qpbar$ by replacing $\phi_p$ with $\phi_p \circ \s$ for $\s$ in $G$. For both $R_{n,p}(M^E)$ and $D^{1/2,p}(M^E)$ this corresponds to letting $\s$ act on $E[G]\pi$, and the resulting determinant cancels as before. That the quotient lies in $E \tensor \Qp$ follows because it lies in $E \tensor F$ and we have just proved that it is invariant under $\Gal(F/\Qp)$ by Lemma [\[synlemma\]](#synlemma){reference-type="ref" reference="synlemma"}. ◻
:::

We now investigate when the two dimensions in Definition [\[regdef\]](#regdef){reference-type="ref" reference="regdef"} are equal. The answer is given by Proposition [\[whenconj\]](#whenconj){reference-type="ref" reference="whenconj"} below, but we need some preliminary results.

::: proposition
[]{#kerisreal label="kerisreal"} If $k/\Q$ is a finite Galois extension with Galois group $G$ and $\pi$ is an idempotent in $E[G]$ then $\dim_E (\KMn M_\pi^E ) \le \dim_E (E[G] \pi)$. Equality holds precisely when any $($hence every$)$ $\t$ in the image in $G$ of the conjugacy class of complex conjugation in $\Gal(\Qbar/\Q)$ acts by $(-1)^{n-1}$ on $E[G]\pi$.
:::

::: proof
*Proof.* For the statement we can first replace $E$ by a finitely generated subfield since $\pi$ contains only finitely many elements of $E$, next embed $E$ into $\C$ and use this embedding to enlarge $E$ to $\C$. So we may assume that $E=\C$.

According to Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} the pairing [\[EKpairing\]](#EKpairing){reference-type="eqref" reference="EKpairing"} gives an injection $$\label{Rinjection}
\begin{aligned}
\R \tensor_\Q \Kn k  & \to \R[G]^\vee = \Hom_\R(\R[G], \R)
\cr
\a & \mapsto f_\a \text{ with } f_\a(\s) = \frac{1}{(2 \pi i)^{n-1}} \Phi_\infty(\s(\a))
\end{aligned}$$ and by extending the coefficients we get an injection $\C \tensor_\Q \Kn k  \to \C[G]^\vee$. The image of $\pi (\Kn k \tensor_\Q \C)$ under the last map vanishes on $\C[G](1-\pi)$ since $(1-\pi) \pi = 0$ so that $\pi \Kn k \tensor_\Q \C$ injects into $(\C[G]/\C[G](1-\pi))^\vee \iso (\C[G]\pi)^\vee$, which proves our first inequality.

As for equality, we know by Theorem [\[boreltheorem\]](#boreltheorem){reference-type="ref" reference="boreltheorem"} that [\[Rinjection\]](#Rinjection){reference-type="eqref" reference="Rinjection"} has as its image the subspace of $\R[G]^\vee$ where, under the action of $\Gal(\Qbar/\Q)$ on $\R[G]^\vee$ via $(\tilde \s f)(\s) = f(\tilde \s^{-1}\s)$, the conjucagy class of complex conjugation in $\Gal(\Qbar/\Q)$ acts as multiplication by $(-1)^{n-1}$. The same will therefore hold with complex coefficients. Since any element $\t$ in the conjugacy class of complex conjugation has order 1 or 2, $\C[G] \pi$ decomposes into eigenspaces for the eigenvalues $\pm 1$ and the desired equality can only hold if $\t$ acts as multiplication by $(-1)^{n-1}$ on all of $\C[G] \pi$. ◻
:::

We now determine precisely when the equality of dimensions as in Proposition [\[kerisreal\]](#kerisreal){reference-type="ref" reference="kerisreal"} can occur, and for this we need a preliminary result.

::: prop
[]{#CMprop label="CMprop"} Let $\psi$ be a representation of $\Gal(\Qbar/\Q)$ over $\Qbar$ that factorizes through the Galois group of a finite Galois extension of $\Q$ and for which $\psi(\t)$ acts as multiplication by $(-1)^{n-1}$ for any $\t$ in the conjugacy class of complex conjugation in $\Gal(\Qbar/\Q)$. Then the fixed field of $\Ker(\psi)$ is a finite Galois extension of $\Q$ that is totally real if $n$ is odd, and CM if $n$ is even.
:::

::: proof
*Proof.* That the fixed field $k$ of $\Ker(\psi)$ is a finite Galois extension of $\Q$ is clear. When $n$ is odd $\psi(\t)=1$ for any $\t$ in the conjugacy class of complex conjugation so that $k$ is totally real. For even $n$ we let $\omega$ be the composition $\Gal(\Qbar/\Q) \to \Gal(\Q(\mu_4)/\Q) \rightiso \{\pm1\} \subset \Qbar^*$. Then $\Ker(\psi\omega)$ contains $\t$ and $\Ker(\psi) \cap \Ker(\omega)$, hence its fixed field is a totally real Galois extension $k^+$ of $\Q$, contained in $k(\mu_4)$. Similarly $k$ is contained in the CM field $k^+(\mu_4)$ so, since $k$ is not totally real, it must be CM. ◻
:::

::: remark
[]{#CM label="CM"} For a CM field $k$ with $k/\Q$ Galois, its maximal totally real subfield is Galois over $\Q$ and is the fixed field of an element of order two in the centre of $\Gal(k/\Q)$, which we shall refer to as the complex conjugation of $k$.
:::

::: proposition
[]{#whenconj label="whenconj"} Let $k/\Q$ be a finite Galois extension with Galois group $G$, $E$ any extension of $\Q$, and $\pi$ an idempotent of $E[G]$. Let $k'$ be the fixed field of the kernel of the representation of $G$ on $E[G] \pi$. Then for $n \ge 2$ the equality $\dim_E(E[G]\pi) = \dim_E(\KMn M_\pi^E )$ holds precisely in the following cases:

1.  $k'$ is totally real and $n$ is odd;

2.  $k'$ is a CM field, $n$ is even, and the complex conjugation of $k'$ acts on $E[G] \pi$ as multiplication by $-1$.
:::

::: proof
*Proof.* From Propositions [\[kerisreal\]](#kerisreal){reference-type="ref" reference="kerisreal"} and [\[CMprop\]](#CMprop){reference-type="ref" reference="CMprop"} we see that there cannot be any other cases. Conversely, by Proposition [\[kerisreal\]](#kerisreal){reference-type="ref" reference="kerisreal"} equality holds in both. ◻
:::

We now recall and introduce some terminology for later use.

::: definition
[]{#mindef label="mindef"} Let $G$ be a finite group and $E$ any extension of $\Q$.

1.  If $\pi$ is a central idempotent of $E[G]$ such that $E[G] \pi$ is a minimal (non-zero) 2-sided ideal of $E[G]$ then $\pi$ is a primitive central idempotent.

2.  If $\pi$ is a primitive central idempotent of $E[G]$ such that $E[G] \pi \iso M_m(E)$ as $E$-algebras for some $m$ then we call a primitive idempotent corresponding to $\pi$ any element in $E[G] \pi \subseteq E[G]$ that maps to a matrix in $M_m(E)$ that is conjugate to a matrix with 1 in the upper left corner and 0's elsewhere. (Since all automorphisms of $M_m(E)$ as $E$-algebra are inner this is independent of the isomorphism $E[G] \pi \iso M_m(E)$.)
:::

::: remark
[]{#minrem label="minrem"} (1) If $E[G] \pi \iso M_m(E)$ then any idempotent in $E[G] \pi$ can be written as a sum of orthogonal primitive idempotents corresponding to $\pi$ as one sees immediately by diagonalizing the matrix $A$ that $\pi$ maps to, which satisfies $A^2=A$.

\(2\) If $G = \Gal(k/\Q)$ and $\pi$ is a primitive central idempotent of $E[G]$ then the dimensions of $E[G] \tilde \pi$ and $\tilde \pi \KnE k$ are equal for some non-zero idempotent $\tilde \pi$ in $E[G] \pi$ if and only if the same holds for one (hence any) primitive idempotent corresponding to $\pi$. Indeed, the dimensions for $\pi$ do not change if we replace it with a conjugate in $E[G]$, and they add up for sums of orthogonal idempotents.
:::

We now introduce , both classical and , in the following context. Let $E$ be a finite extension of $\Q$, $k$ a number field, and consider a character $\psi$ of a representation of $G = \Gal(\kbar/k)$ on a finite dimensional $E$-vector space $V$ that factorizes through $\Gal(\kbar/k')$ for some finite extension $k'$ of $k$. Then for every embedding $\s : k \to \C$ we have the Artin $\L s \s(\psi) k$, with for every prime $\P$ of $k$ the reciprocal $\Eul_\P(s, \s(\psi) ,k)$ of the Euler factor corresponding to $\P$. Under the natural isomorphism $E \tensor_\Q \C \rightiso \oplus_\s \C_\s$ the $\L s \s(\psi) k$ correspond to a canonical $E\tensor_\Q \C$-valued that we denote by $\L s {\psi\tensor\id} k$. Similarly, for every prime $\P$ of $k$ we have an $E\tensor_\Q\C$-valued $\Eul_\P( s, \psi\tensor\id, k)$ corresponding to the $\Eul_\P(s,\s(\psi),k)$.

We now move on to the , and assume that $k$ is totally real, $p$ a prime number, $a$ any integer and $\omega_p$ the Teichmüller character $\Gal(\Qbar/k) \to \Q_p^*$ [\[TM\]](#TM){reference-type="eqref" reference="TM"}. If $\t : E \to \Qpbar$ is an embedding and $k_{\t(\psi)\omega_p^a}$ is totally real then from Section [\[conjecturesection\]](#conjecturesection){reference-type="ref" reference="conjecturesection"} we have the $\Lp p s \t(\psi)\omega_p^a k$, which is not identically zero. In this case, using the natural isomorphism $E\tensor_\Q\Qpbar \rightiso \oplus_\t \overline{\Q}_{p,\t}$, they give us an $E\tensor_\Q \Qpbar$-valued on $\Zp$ or $\Zp\setminus\{1\}$ that we denote by $\Lp p s \psi\tensor\omega_p^a k$.

::: lemma
[]{#pLvalueslemma label="pLvalueslemma"} The values of $\Lp p s \psi\tensor\omega_p^a k$ are in $E\tensor_\Q \Qp$.
:::

::: proof
*Proof.* Using Brauer induction for $\psi$ (cf. [\[brauerinduction\]](#brauerinduction){reference-type="eqref" reference="brauerinduction"}) it suffices to do prove this when $\psi$ is 1-dimensional. But then for each $\t : E \to \Qpbar$ the function $\Lp p s \t(\psi)\omega_p^a k$ can be described as in [\[merpL\]](#merpL){reference-type="eqref" reference="merpL"} with $l=-1$, from which the result is clear. ◻
:::

::: remark
It follows from Remark [\[interpolrem\]](#interpolrem){reference-type="ref" reference="interpolrem"} that $\Lp p s \psi\tensor\omega_p^a k$ satisfies $$\Lp p m \psi\tensor\omega_p^a k = \Eul_p(m, \psi\tensor\id, k) \L m {\psi\tensor\id} k$$ for integers $m\le0$ congruent to $1-a$ modulo $\phi(q)$, where both sides lie in $E = E\tensor_\Q \Q$ inside $E\tensor_\Q \Qp$ and $E\tensor_\Q\C$ respectively, and $$\Eul_p(s, \psi\tensor\id, k) = \prod_{\P|p} \Eul_\P(s, \psi\tensor\id, k)$$ the product being over all primes of $k$ dividing $p$.
:::

::: remark
[]{#idenrem label="idenrem"} If $E=\Q$ we shall identify $E\tensor_\Q \C$ with $\C$, and write $\L s {\psi} k$, etc., instead of $\L s {\psi\tensor\id} k$, etc. Similarly we identify $E\tensor_\Q\Qp$ with $\Qp$ and write $\Lp p s {\psi}\omega_p^a k$ instead of $\Lp p s {\psi}\tensor\omega_p^a k$.
:::

We now have all the ingredients for the generalization and refinement of Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"}. Starting with a finite Galois extension $k/\Q$ with Galois group $G$, $E$ a finite extension of $\Q$, and $\pi$ an idempotent in $E[G]$, we let $\psi_\pi$ be the natural representation of $\Gal(\Qbar/\Q)$ on $E[G]\pi$ and $\chi_\pi$ its associated character. If $\dim_E(E[G]\pi) = \dim_E(\pi \KnE k )$ for some $n \ge 2$ then, for any prime $p$ and any embedding $\t : E \to \Qpbar$, $\t(\psi_\pi) \omega_p^{1-n}$ is trivial on the conjugacy class of complex conjugation in $\Gal(\Qbar/\Q)$ by Proposition [\[kerisreal\]](#kerisreal){reference-type="ref" reference="kerisreal"}. In particular, $\Q_{\t(\psi_\pi)\omega_p^{1-n}}$ is totally real and therefore $\Lp p n {\chi_\pi\tensor\id} {\Q}$ is not identically zero. With $F \subset \Qpbar$ the topological closure of $\phi_p(k)$ as before, using ordered bases for $E[G]\pi$, $M_\pi^E$ and $\KMn M_\pi^E$, we have $D(M_\pi^E)^{1/2,\infty}$ and the regulator $R_{n,\infty}(M_\pi^E)$ in $E \tensor \C$ as well as $D(M_\pi^E)^{1/2,p}$ and $R_{n,p}(M_\pi^E)$ in $E \tensor F$.

::: conjecture
[]{#motiveconjecture label="motiveconjecture"} With notation as above, if $\dim_E(E[G]\pi) = \dim_E(\pi \KnE k )$ for some $n \ge 2$, then

1.  in $E \tensor_\Q \C$ we have $$\qquad\qquad
    \L n {\chi_\pi\tensor\id} {\Q}  D(M_\pi^E)^{1/2,\infty} = e(n, M_\pi^E) R_{n,\infty}(M_\pi^E)$$ for some $e(n, M_\pi^E)$ in $(E\tensor_\Q \Q)^*$;

2.  in $E \tensor_\Q F$ we have $$\qquad\qquad
    \Lp p n {\chi_\pi}\tensor\,\omega_p^{1-n} {\Q} D(M_\pi^E)^{1/2,p}  = e_p(n,M_\pi^E) \, \Eul_p(n, \chi_\pi\tensor\,\id,\Q) R_{n,p}(M_\pi^E)$$ for some $e_p(n,M_\pi^E)$ in $(E\tensor_\Q \Q)^*$;

3.  in fact, $e_p(n, M_\pi^E) = e(n, M_\pi^E)$;

4.  $\Lp p n {\chi_\pi}\tensor\omega_p^{1-n} {\Q}$ and $R_{n,p}(M_\pi^E)$ are units in $E \tensor_\Q \Qp$ and $E \tensor_\Q F$ respectively.
:::

::: remark
[]{#newremark label="newremark"} (1) One sees as in the proof of Lemma [\[Qpquot\]](#Qpquot){reference-type="ref" reference="Qpquot"} that the validity of each part of the conjecture is independent of the chosen bases of $E[G]\pi$, $M_\pi^E$ and $\KMn M_\pi^E$.

\(2\) Since $E\tensor_\Q \C \rightiso \oplus_\s E_\s$, where the sum is over all embeddings $\s : E \to \C$, an identity in $E \tensor_\Q \C$ is equivalent to the corresponding identities for all such embeddings. The same holds if we replace $\C$ with $\Qpbar$.
:::

In Remark [\[BBmotiverem\]](#BBmotiverem){reference-type="ref" reference="BBmotiverem"} we shall make explicit how part (1) of this conjecture is equivalent with Beilinson's conjecture [@bei85 Conjecture 3.4] for an Artin motive associated with $\pi$. First, we make various remarks about its dependence on $E$, etc., and on its relation with Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"}.

::: remark
[]{#newrem label="newrem"} (1) An equivalent for Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1) can be formulated for any idempotent $\pi$ if $k/\Q$ is any finite Galois extension (see the end of Section [\[practical\]](#practical){reference-type="ref" reference="practical"}), in which case it is a conjecture by Gross (see [@Neu88 p. 210]). In that case it was proved by Beilinson if the action of $G=\Gal(k/\Q)$ on $E[G]\pi$ is Abelian (see loc. cit.). One can deduce that it holds for any $\pi$ in $E[G]$ if this action factors through $S_3$ or $D_8$ (see Proposition [\[grossprop\]](#grossprop){reference-type="ref" reference="grossprop"}).

\(2\) If the action of $G$ on $E[G]$ is Abelian then parts (1)-(3) of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} also hold for any $\pi$ to which the conjecture applies (see Remark [\[abelrem\]](#abelrem){reference-type="ref" reference="abelrem"}).

\(3\) Extending and simplifying earlier work by F. Calegari [@Cal05], F. Beukers in [@Beu06] proved that $\z_p(2)$ is irrational when $p=2$ or 3. This value equals $\Lp p 2 \chi\omega_p^{-1} {\Q}$ with $\chi$ the primitive character on $(\Z/4\Z)^*$ for $p=2$, and the primitive character on $(\Z/3\Z)^*$ for $p=3$. Moreover, if $\chi$ is the odd primitive character on $(\Z/8\Z)^*$ then he also shows that $\Lp 2 2 \chi\omega_2^{-1} {\Q}$ is irrational. It follows that the conjecture holds in full for $\pi$ corresponding to the non-trivial representation of $\Gal(k/\Q)$ and $n=2$ when $(k,p)$ is one of $(\Q(\sqrt{-1}),2)$, $(\Q(\sqrt{-2}),2)$ and $(\Q(\sqrt{-3}),3)$.

\(4\) We have verified numerically that part (4) of the conjecture holds in certain cases; see Remark [\[dirichletcalculations\]](#dirichletcalculations){reference-type="ref" reference="dirichletcalculations"} as well as Section [\[examplesection\]](#examplesection){reference-type="ref" reference="examplesection"}.
:::

::: remark
[]{#consequencesremark label="consequencesremark"} (1) If $\pi = \pi_1 + \cdots + \pi_m$ with $\pi_i^2 = \pi_i$ and $\pi_i \pi_j = 0$ when $i \neq j$, then the conjecture for $\pi$ is implied by the conjecture for all $\pi_i$ because $D(\oplus_i M_i^E)^{1,2/\infty} = \prod_i D(M_i^E)^{1/2,\infty}$, etc., as one easily sees by using bases.

\(2\) If $\pi$ is in $E[G]$ and $E'$ is an extension of $E$, then we may view $\pi$ as an element of $E'[G]$ as well, and the conjectures for $M_i^E$ and $M_i^{E'}$ are equivalent: we can use the same bases over $E'$ as over $E$, so that $D(M_i^E)^{1/2,\infty} =  D(M_i^{E'})^{1/2,\infty}$ in $E \tensor \C \subseteq E' \tensor \C$, and the same holds for all the other ingredients (including the $L$-functions).

\(3\) By comparing bases one sees immediately that if $\pi$ and $\pi'$ are conjugate under the action of $E[G]^*$ then the conjectures for $\pi$ and for $\pi'$ are equivalent.

\(4\) If, for a primitive central idempotent $\pi_i$ of $E[G]$, $E[G] \pi_i \iso M_m(E)$ for some $m$, and $\pi$ is a primitive idempotent corresponding to $\pi_i$, then the conjecture for $\pi_i$ is implied by the conjecture for $\pi$. Indeed, we can decompose $\pi_i$ into a sum of orthogonal primitive idempotents as in Remark [\[minrem\]](#minrem){reference-type="ref" reference="minrem"}(1), and the truth of the conjecture for $\pi_i$ is implied by its truth for each such primitive idempotent. But all such primitive idempotents are conjugate to $\pi$ hence part (3) above applies.
:::

::: remark
[]{#galoisdescent label="galoisdescent"} If $k/\Q$ is a Galois extension with Galois group $G$ and $H$ a subgroup of $G$ with fixed field $k^H$, then $K_m(k)_\Q^H = K_m(k^H)_\Q$, a result known as Galois descent. With $\pi_H = |H|^{-1} \sum_{h \in H} h$, an idempotent in $E[G]$, this implies that $\pi_H K_m(k) = K_m(k^H)$.
:::

::: remark
[]{#sameconj label="sameconj"} (1) Let $k/\Q$ be a Galois extension with Galois group $G$. If $N$ is a normal subgroup of $G$ corresponding to $k' = k^N$ and $\pi_N = |N|^{-1} \sum_{h \in N} h$, then $\pi_N^2 = \pi_N$ and the natural map $\phi : E[G] \to E[G/N]$ has kernel $E[G] (1-\pi_N)$ and induces an isomorphism $E[G] \pi_N \to E[G/N]$. Indeed, it is clear that $\pi_N$ is central in $E[G]$ since $N$ is normal in $G$ and that $1-\pi_N$ is in the kernel of $\phi$. Also, since $N$ acts trivially on $E[G] \pi_N$ this is an $E[G/N]$-module generated by one element, so its dimension over $E$ cannot be bigger than $|G/N|$. Since $\phi$ is obviously surjective our claims follow. Therefore in this situation for any idempotent $\pi$ in $E[G/N]$ there is a canonical idempotent $\tilde \pi$ lifting $\pi$ to $E[G] \pi_N$, and the natural map $E[G] \tilde \pi \to E[G/N] \pi$ is an isomorphism of $E[G]$- and $E[G/N]$-modules.

Then the statements of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} for $\pi$ in $E[G/N]$ or for $\tilde \pi$ in $E[G]$ are equivalent. Namely, $$\tilde \pi \KnE k = \tilde \pi \pi_N \KnE k =  \tilde \pi \KnE k' = \pi \KnE k'$$ inside $\KnE k$ so that we can use the same bases for either side. The same holds for $\tilde \pi (E\tensor k)$ and $\pi (E \tensor k')$ inside $E \tensor k$. Moreover, $E[G]\tilde\pi$ is the pullback to $G$ of the $G/N$-representation $E[G/N] \pi$, so that $\L s  {E[G]\tilde\pi} {\Q} = \L s {E[G/N]\pi} {\Q}$ and similarly for the .

\(2\) If $k$ is a totally real number field $k$ let $\tilde k$ be its (totally real) Galois closure over $\Q$. Then $k = \tilde k ^H$ for some subgroup $H$ of $G = \Gal(\tilde k/\Q)$, $\pi = |H|^{-1} \sum_{h \in H} h$ is an idempotent in $\Q[G]$, and for $n \ge 2$ odd Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} for $\pi$ is equivalent to Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} for $k$. Namely, $\Kn k = \pi \Kn \tilde k \subseteq \Kn \tilde k$ by Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} and $\pi \tilde k = k$ so that we can use the same $\Q$-bases in each case. Moreover, $\Q[G] \pi \iso \Ind H G (1_H) = \Q[G] \tensor_{\Q[H]} 1_H$ with $1_H$ the trivial 1-dimensional representation of $H$, as one easily sees by mapping $\b$ in $\Q[G] \pi$ to $\b \tensor v$ and $\sum_\s a_\s \s \tensor(\lambda v)$ to $\lambda \sum_\s a_\s \s \pi$, $\{v\}$ being a basis of $1_H$. By well-known properties of Artin [@Neu99 Prop. 10.4(iv)] this implies that $\z_k(s) = \L n {\Q[G]\pi} {\Q}$ and similarly for the .
:::

::: remark
[]{#BBmotiverem label="BBmotiverem"} We make the relation between Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1) and Beilinson's conjecture [@bei85 Conjecture 3.4] for (Artin) motives explicit since the relation between the two elements of $E^*$ involved also shows up very explicitly in our computer calculations, suggesting that the element for the formulation at $s=1-n$ is simpler than for our formulation at $s=n$ (see Remark [\[constantremark\]](#constantremark){reference-type="ref" reference="constantremark"}). We provide some details since we could not find a detailed enough reference in the literature.

With notation as in Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} and [\[oldfuneq\]](#oldfuneq){reference-type="eqref" reference="oldfuneq"} we have $$\label{newfuneq}
\begin{aligned}
\L 1-s {\chi_\pi^\vee\tensor\id} {\Q} 
& =
W(\chi_\pi^\vee\tensor\id) C(\chi_\pi^\vee\tensor\id)^{s-\frac12} (2 (2\pi)^{-s}\Gamma(s))^{\chi^\vee(1)}
\\
& \qquad\times
 (\cos(\pi s/2))^{n^+}  (\sin(\pi s/2))^{n^-} \L s {\chi_\pi\tensor\id} {\Q} 
\,,
\end{aligned}$$ with $\chi_\pi^\vee$ the dual character of $\chi_\pi$, $W(\chi_\pi^\vee\tensor\id)$ in $E\tensor\C$, and $C(\chi_\pi^\vee\tensor\id) = C(\chi_\pi\tensor\id)$ in $\Q^*$. If $m=\dim_E(E[G]\pi)$, then $n^+ = m$ and $n^-=0$ for $n$ odd, and $n^-=m$ and $n^+=0$ for $n$ even. In either case $\L s {\chi_\pi^\vee\tensor\id} {\Q}$ has a zero of order $m$ at $s=1-n$. Moreover $$\label{edef}
W(\chi_\pi^\vee\tensor\id) C(\chi_\pi^\vee\tensor\id)^{1/2} = e_n i^{m(n-1)} D(M_\pi^E)^{1/2,\infty}$$ for some $e_n$ in $E^* = (E\tensor_\Q \Q)^*$ by [@Del77 Propositions 5.5 and 6.5] since $D^{1/2,\infty}$ can be taken to be the same for $M_\pi^E$ and the associated determinant representation (cf. [@Jan88b p.360]). Hence the first non-vanishing coefficient in its Taylor expansion around $s=1-n$, $\Lsharp {1-n} {\chi_\pi^\vee\tensor\id} {\Q}$, equals $$\delta_n e_n (2\pi i)^{m(1-n)} ((n-1)!/2)^m C(\chi_\pi^\vee\tensor\id)^{n-1} D(M_\pi^E)^{1/2,\infty} \L n {\chi_\pi\tensor\id} {\Q}$$ with $\delta_n = (-1)^{m(n-1)/2}$ when $n$ is odd, and $\delta_n = (-1)^{m(n+2)/2}$ when $n$ is even. In particular, Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1) is equivalent with $$\label{newe}
\Lsharp {1-n} {\chi_\pi^\vee\tensor\id} {\Q} 
=
\delta_n e_n ((n-1)!/2)^m C(\chi_\pi^\vee\tensor\id)^{n-1} e(n,M_\pi^E) \widetilde R_{n,\infty}(M_\pi^E)$$ with the renormalized regulator $\widetilde R_{n,\infty}(M_\pi^E) = (2\pi i)^{m(1-n)}R_{n,\infty}(M_\pi^E)$.

Let us compare this with Beilinson's conjecture for a motive associated with $\pi$. We associate motives covariantly to smooth projective varieties over $\Q$ as in [@bei85 § 2.4]. The Galois group $G$ acts on the left on $k$, hence on the right on $\spec(k)$, and we let $\art$ be the motive corresponding to $\pi$ under this action. Then $G$ acts on the left on the cohomology theories on $\spec(k)$ as well as its $K$-theory, and after tensoring with $E$ the corresponding groups for $\art$ are the images under $\pi$. Thus, the relevant motivic cohomology of $\art$ is $\hm^1(\mathcal{M}_{\pi/\Z},\Q(n))= K_{2n-1} (M_\pi^E)$.

We shall need the non-degenerate $E$-bilinear pairing $$\begin{aligned}
E[G] \times \bigoplus_{\t: k \to \C} E & \to E
\\
(\smallsum_\s a_\s \s,  (b_\t)_\t ) & \mapsto \smallsum_\s a_\s b_{\phi_\infty\circ\s^{-1}}
\,.
\end{aligned}$$ It factors through the left $E[G]$-action on $\oplus_\t E$ (given by $\s((b_\t)_\t) = (b_{\t\circ\s^{-1}})_\t$), hence is trivial on $E[G](1-\pi)\times \pi(\oplus_\t E)$ and $E[G]\pi\times (1-\pi)(\oplus_\t E)$. We therefore obtain a non-degenerate $E$-bilinear pairing $$\label{<>}
\langle \,\cdot\, , \,\cdot\, \rangle : E[G]\pi \times \pi(\oplus_\t E) \to E$$ that identifies $E[G]\pi$ and $\pi(\oplus_\t E)$ as dual $E[G]$-modules.

Tensoring [\[HDid\]](#HDid){reference-type="eqref" reference="HDid"} with $E$ and applying $\pi$ we get $$\hd^1(\artR,\R(n)) \isom  \pi \bigl( \bigoplus_{\tau: k\to \C} E\otimes \R(n-1) \bigr)
\,.$$ Note that the left hand side is a subspace of the right hand side by [\[HDid\]](#HDid){reference-type="eqref" reference="HDid"}, but because the regulator map [\[Bregulator\]](#Bregulator){reference-type="eqref" reference="Bregulator"} tensored with $\R$ is injective, and $\dim_E(K_{2n-1}(M_\pi^E)) = \dim_E(E[G]\pi) = \dim_E(\pi(\oplus_\t E))$ by our assumption on $\pi$ and since $D(M_\pi^E)^{1/2,\infty} \ne 0$ (as was noticed right after Definition [\[discdef\]](#discdef){reference-type="ref" reference="discdef"}), equality must hold. For the Beilinson regulator we therefore have to compare the two $E$-structures on $\det\hd^1(\artR,\R(n))$ coming from Betti cohomology, $$\hb^0(\artR,\Q(n-1)) \isom  \pi (\bigoplus_{\tau: k\to \C} E\otimes \Q(n-1)) 
\subseteq     \pi \bigl(\bigoplus_{\tau: k\to \C} E\otimes \R(n-1) \bigr) 
\,,$$ and that induced by the Beilinson regulator map [\[Bregulator\]](#Bregulator){reference-type="eqref" reference="Bregulator"}, $$\hm^1(\artR,\Q(n)) \to \hd^1(\artR,\R(n)) 
= \pi \bigl(\bigoplus_{\tau: k\to \C} E\otimes \R(n-1)\bigr) 
\,.$$ Choosing an $E$-basis of $\pi(\oplus_\t E)$, and multiplying it by $(2\pi i)^{n-1}$ to obtain an $E$-basis of $\pi (\oplus_\t E\tensor \Q(n-1))$, it is easy to see that Beilinson's regulator $R_\Bei$ for $\art$ satisfies $$R_\Bei = (2\pi i)^{m(1-n)} \det [\,\cdot\,,\,\cdot\,]_\infty / \det \langle\,\cdot\,,\,\cdot\,\rangle 
= \widetilde  R_{n,\infty}(M_\pi^E) / \det \langle\,\cdot\,,\,\cdot\,\rangle$$ where all determinants are computed using the chosen $E$-bases.

Finally, we compare . We have $$H_{\textup{et}}^0(\spec(k) \otimes \Qbar,\Q_l) \iso \bigoplus_{\t:k\to\Qbar} \Q_l
\iso \Q_l \tensor_\Q \biggl( \bigoplus_{\t:k\to\Qbar} \Q \biggr)$$ so that $H_{\textup{et}}^0(\art,\Q_l) \iso \Q_l \tensor \pi (\oplus_\t E)$ as $\Q_l\tensor E[G]$-modules. The $\Q_l$ plays no role, and as in [\[\<\>\]](#<>){reference-type="eqref" reference="<>"} we see that $\pi(\oplus_{\t:k\to\Qbar} E )$ is dual to $E[G] \pi$ as $E[G]$-module. As the motivic uses the geometric rather than the arithmetic Frobenius (cf. [@Kat94 p.26]), we obtain that $L(s,\art)$ of [@bei85 § 3] is equal to $\L s {\chi_\pi\tensor\id} {\Q}$. If $\theta : E[G] \to E[G]$ is the $E$-linear involution obtained by replacing each $\s$ in $G$ with $\s^{-1}$, then we need to consider $\mathcal{M}_{\pi}^0 = \mathcal{M}_{\theta(\pi)}$ instead of $\art$. But the map $E[G]\pi \times E[G]\theta(\pi) \to E$ mapping $(\a,\b)$ to the coefficient of the neutral element of $G$ in $\theta(\b)\a$ is easily seen to identify $E[G]\theta(\pi)$ and $E[G]\pi$ as dual $E[G]$-modules, so that $L(s,\art^0) = \L s {\chi_\pi^\vee\tensor\id} {\Q}$.
:::
