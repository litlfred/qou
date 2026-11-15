---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-053-126-application-of-the-theory-of-p-adic-betti-la
section_title: "Application of the theory of $p$-adic Betti lattices."
section_number: 12.6
pages: 110-113
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.826
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub:7.6}

\begin{para}\label{para:7.6.1}
 We consider more closely the Gauss-Manin connection
 $(\mathcal{H},\nabla_{\mathrm{GM}})$ in the case of Shimura curves.


 We begin with the case $E=\Q$ as in \ref{sub:7.4}.  Then $\mathcal{H}$
 is a vector bundle of rank $4$, and the $B$-action on $\mathcal{H}$
 obtained by functoriality of De Rham cohomology commutes with
 $\nabla_{\mathrm{GM}}$.

 Let us choose an imaginary quadratic field $F=\Q(\sqrt{-d})$ inside
 $B$. Then $(\mathcal{H},\nabla_{\mathrm{GM}})\otimes F$ splits into two parts:
 $(\mathcal{H},\nabla_{\mathrm{GM}})_+\oplus
 (\mathcal{H},\nabla_{\mathrm{GM}})_{-}$ (on 
 which $F\subset B$ acts through identity and complex conjugation
 respectively).


 On the other hand, let us fix embeddings $F\subset \ovl{\Q} \subset \C$,
 and let us fix a base point $s\in \mathcal{X}_{\Gamma}(\ovl{\Q})$ of our
 Shimura curve.  This is the moduli point of a decorated fake elliptic
 curve $A/\ovl{\Q}$. We have $V^\C=\mathrm{H}^1_B(A_\C,\C)\cong
 (\mathcal{H}_\C^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$, and this again splits
 into $\pm$ parts. The Betti cohomology $F$-space
 $\mathrm{H}^1_B(A_\C,F)$ already splits into two parts:
 $\mathrm{H}^1_B(A_\C,F)_+\oplus \mathrm{H}^1_B(A_\C,F)_{-}$, both of
 rank two and stable under the action of $B\otimes F \cong M_2(F)$.

 The flag space $\mathcal{D}^\vee$ is actually defined over the reflex
 field $\Q$. Over $F$, it becomes isomorphic to $\P^1$, or more
 precisely, to $\P(\mathrm{H}^1_B(A_\C,F)_+)$. The period mapping describes the
 ``slope'' of the Hodge line $F^1\cap V^\C_+$ with respect to a basis of
 $\mathrm{H}^1_B(A_\C,F)_+\subset
 ((\mathcal{H}_+)_\C^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$, and is 
 thus given by a quotient of solutions of the (partial) Gauss-Manin
 connection $\nabla_{\mathrm{GM}+}$.


 Assume for simplicity that $\Gamma\subset B^\times/\Q^\times$ is
 torsion-free. Then $\Gamma$ may be identified with the projective
 monodromy group, \ie with the quotient by the homotheties of the image
 of the monodromy representation
 \begin{equation*}
  \pi_1((\mathcal{X}_{\Gamma })_\C,s)\rightarrow GL(\mathrm{H}^1_B(A_\C,F)_+).
 \end{equation*}


\end{para}

\begin{para}\label{para:7.6.2} Let us now turn to the $p$-adic side. We fix an
embedding $\ovl{\Q} 
\subset \C_p$. We shall limit ourselves to the case of a prime $p$ of
 {\it supersingular reduction} for $A$. Note that this includes the case
 of critical primes (\ref{lem:7.4.6}).


 Let $D$ be the definite quaternion algebra over $\Q$ which is ramified
 only at $p$, and let $\ovl{B}$ be the definite quaternion algebra over
 $\Q$ which is ramified at the same primes as $B$ except $p$. Then,
 whether $p$ is critical or not, the group $J$ (of self-quasi-isogenies
 of $\ovl{A}[p^\infty]$ commuting with $B$) is $\ovl{B}_p^\times$.
 

 By the local criterion for splitting fields \cite[III.3.5]{adadq}, $F$
 is also a splitting field for the quaternion algebra $D$ (and $\ovl{B}$
 as well). We can therefore apply the theory of
 I.\ref{sub-p-adic-betti-lattice-supersing}, and get an 
 $F$-structure $\mathrm{H}^1_B(A_{\C_p},F)$ inside
 $\mathrm{H}^1_{\mathrm{cris}}(\ovl{A},/\C_p)\cong
 V^{\C_p}=\D(\ovl{\Lambda})\otimes \C_p.$ By construction, it is stable
 under the action of $M_2(D)\otimes F\cong M_4(F)\cong B\otimes \ovl{B}
 \otimes F$.


 Using the embedding $F\otimes 1\otimes F\subset B\otimes \ovl{B} \otimes
 F$, one splits this $F$-structure $\mathrm{H}^1_B(A_{\C_p},F)$ into two parts
 $\mathrm{H}^1_B(A_{\C_p},F)_+\oplus \mathrm{H}^1_B(A_{\C_p},F)_{-}$ (on
 which $F\otimes 
 1\otimes 1\subset B\otimes \ovl{B} \otimes F$ acts through identity and
 complex conjugation respectively), both of rank two and stable under
 the action of $\ovl{B}\otimes F \subset M_4(F)$, hence under $J$.  \par
 The $p$-adic flag space $\mathcal{D}^\vee$ is again defined over the
 reflex field $\Q$. Over $F$, it becomes isomorphic to
 $\P(\mathrm{H}^1_B(A_{\C_p},F)_+)$ (note that the scaling ambiguity of
 $\mathrm{H}^1_B(A_{\C_p},F)_+$ by a factor in $\sqrt{F^\times}$ disappears
 here). The $J$-equivariant period mapping $\mathcal{P}$ describes the
 ``slope'' of the Hodge line $F^1\cap V^{\C_p}_+$ with respect to a
 fixed basis $(e_0,\,e_1)$ of $\mathrm{H}^1_B(A_{\C_p},F)_+\subset
 ((\mathcal{H}_+)_{\C_p}^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$, and is
 thus given by a quotient of solutions of $\nabla_{\mathrm{GM}+}$.


 Note that if $B$ is split at $p$, then $\mathcal{P}$ is of
 Gross-Hopkins type, and one has only a local $p$-adic uniformization of
 $\mathcal{X}_{\Gamma}$ around $s$ (in a supersingular disk).


 If instead $p$ is critical, then $\mathcal{P}$ is of Drinfeld type, and
 the group $\Gamma_p \subset J^1$ appearing in the global $p$-adic
 uniformization of $\mathcal{X}_{\Gamma}$ may be identified with the
 quotient by the homotheties of the image of the monodromy representation
 (in the sense of \ref{cor:7.2.6})
 \begin{equation*}
  \pi_1^{\mathrm{top}}((\mathcal{X}_{\Gamma })_{\C_p},s)\rightarrow
   GL(\mathrm{H}^1_B(A_{\C_p},F)_+).
 \end{equation*}

 A slight refinement provides a rank two
 $\mathcal{O}_F[\frac{1}{p}]$-lattice
 $\mathrm{H}^1_B(A_{\C_p},\mathcal{O}_F[\frac{1}{p}])_+$ in
 $((\mathcal{H}_+)_{\C_p}^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$ stable
 under $p$-adic monodromy.
\end{para}

\begin{para}\label{para:7.6.3}
 One can go one step further and see that the phenomenon encountered in
 \ref{para:6.3.3} shows up here again: ``the'' quotient $\tau$ of solutions of
 solutions of ${\nabla_{\mathrm{GM}}}$ which expresses locally the
 period mapping 
 $\mathcal{P}$ is essentially given by the same formula in the complex
 and the $p$-adic cases.


More precisely, assume that $A$ has complex multiplication by an order
in $M_2(F)$ (so that $A$ is isogenous to the square of an elliptic curve
with complex multiplication by $\mathcal{O}_{\Q(\sqrt{-d})}$ with
[fundamental] discriminant $-d$ ), and identify $\End_B(A)$ with $F$. We
denote by $\epsilon$ the Dirichlet character, $w$ the number of roots of
unity, $h$ the class number attached to $\mathcal{O}_{\Q(\sqrt{-d})}$.


\noindent We may choose our symplectic basis $e_0,e_1$ of
$\mathrm{H}^1_B(A_{\C},F)_+$ (\resp $\mathrm{H}^1_B(A_{\C_p},F)_+$) in
 such a way that 
$[\sqrt{-d}]^\ast e_0=-\sqrt{-d} \; e_0,\,$ $[\sqrt{-d}]^\ast
e_1=\sqrt{-d} \;e_1$ (here $[\sqrt{-d}]$ is viewed as an element of
$\End_B(A)=F$).

\noindent Let $\omega$ be a section of $\mathcal{H}_+$ in a Zariski
neighborhood $U$ of $s$, which corresponds to a relative differential of
the first kind (no pole) on the universal abelian scheme. Then $\omega$
is a cyclic vector for $\mathcal{H}_+$ over $U$ with respect to
$\nabla_{\mathrm{GM}}$, so that $\nabla_{\mathrm{GM}}$ amounts to a
 concrete linear 
differential equation of order two over $U$.

\noindent We calculate $\tau$ with respect the basis $e_0, e_1$
 of $\mathrm{H}^1_B(A_{\C},F)_+$ (\resp $\mathrm{H}^1_B(A_{\C_p},F)_+$)
 in a small 
 neighborhood of the base point $s$. Denoting by $z$ an algebraic local
 parameter at $s$ in $U$, and extending $e_0,\, e_1$ by horizontality, we
 then have the proportionality
\begin{equation*}
 \omega \sim \tau(z) e_0 + e_1
\end{equation*}
\end{para}

\begin{thm}\label{thm:7.6.4}
 There is a quotient $y=y_1/y_2$ of solutions of $\nabla_{\mathrm{GM}}$ in
 $\ovl{\Q}[[z]]$ such that $\tau$ takes the form
 $\;\tau(z)=\kappa^{-1}\;y(z)\;$ for a suitable constant $\kappa$.

\noindent In the complex case, $\;\kappa\sim\displaystyle
 \prod_{u\in (\Z/d)^\times}
 \Bigl(\Gamma\Bigl\langle\frac{u}{d}\Bigr\rangle\Bigr)^{\epsilon(u)w/2h}\;\in
 \C^\times/\ovl{\Q}^\times$.

\noindent In the $p$-adic case, assuming moreover that $p\nmid d $, 
\begin{equation*}
 \kappa\sim \prod_{u\in (\Z/d)^\times}
  \Bigl(\Gamma_p\Bigl\langle\frac{pu}{d}\Bigr\rangle\Bigr)^{-\epsilon(u)w/4h}
  \in \C_p^\times/\ovl{\Q}^{\times}.
\end{equation*}
\end{thm}
\begin{proof}
 Let us write $\omega_{| z=0}=\omega_{11}e_1$. Then
 $\tau(z)=\kappa^{-1} y(z)$, with $\kappa = \omega_{11}^2/2\pi i$ in
 the complex case, $\kappa = \omega_{11}^2$ in the $p$-adic case (the
 factor $2\pi i$ which arises in the complex case is the factor of
 proportionality of the symplectic forms in De Rham and in Betti
 cohomology respectively). The evaluation of $\omega_{11}$ in the
 complex case is given by the Lerch-Chowla-Selberg formula (\cf
 I.\ref{thm-ogus-formula}). In the $p$-adic case, it is given by
 I.\ref{thm-cm-period}.
\end{proof}

\begin{para}\label{para:7.6.5}
 This discussion generalizes without much complication to the case of
 Shimura curves attached to a quaternion algebra $D$ over a totally real
 number field $E$ of degree $>1$. We concentrate on the case of a
 critical place $v$ and assume, for simplicity, that $E$ is Galois over
 $\Q$ and that $v$ is the unique place of $E$ with the same residue
 characteristic $p$ (\ie $m=0$ in the notation of \ref{para:7.5.2}).


 Let $F$ be a totally imaginary quadratic extension of $E$ contained in
 $B$. Then $F$ is a splitting field for $B,\ovl{B}$, and $D$. Let us fix
 a double embedding $\C \hookleftarrow \ovl{\Q} \hookrightarrow \C_p$ as
 in \ref{para:7.5.2}, and an extension $FK\hookrightarrow \ovl{\Q}$ of $\infty_0$.
 For $C$ small enough, $\Sh^\bullet$ carries a universal abelian scheme
 of relative dimension $g=[FK:\Q]$. After tensoring $\otimes_K
 \ovl{\Q}$, its Gauss-Manin connection splits into pieces of rank two,
 indexed by the embeddings of $FK$ into $\ovl{\Q}$. We select the piece
 $(\mathcal{H},\nabla_{\mathrm{GM}})_+$ corresponding to $\infty_0$.


 Let us fix a base point $s\in \Sh(\ovl{\Q})\subset \Sh^\bullet(\ovl{\Q})
 $ of our Shimura curve.  This is the moduli point of a decorated
 abelian variety $A^\bullet/\ovl{\Q}$ (of dimension $g=[FK:\Q]$ and
 multiplication by $\mathcal{B}^\bullet$). We have $V^\bullet=V\otimes_E
 K \cong \mathrm{H}^1_B(A^\bullet_\C,\Q)$.  Note that
 $\mathrm{H}^1_B(A_\C,F)\cong 
 V\otimes_\Q FK$ splits into pieces of $FK$-rank two, indexed by the
 embeddings of $F$ into $\ovl{\Q}$. We select the piece
 $\mathrm{H}^1_B(A^\bullet_\C,F)_+$ corresponding to $\infty_0$.  We
 then have a 
 natural embedding $\mathrm{H}^1_B(A^\bullet_\C,F)_+\subset
 ((\mathcal{H}_+)_{\C}^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$, and
 $\mathrm{H}^1_B(A^\bullet_\C,F)_+$ is stable under monodromy.


 On the other hand, it follows from \ref{lem:7.4.6}, that $A^\bullet$ has
 supersingular reduction $\ovl{A}^\bullet$ at $v$. We can construct the
 $F$-structure $\mathrm{H}^1_B(A^\bullet_{\C_p},F)$ inside
 $\mathrm{H}^1_{\mathrm{cris}}(\ovl{A}^\bullet,/\C_p)\cong
 V^{\C_p}=\D(\ovl{\Lambda}^\bullet)\otimes \C_p.$ 
 By construction, it is stable under the action of $M_g(D)\otimes F\cong
 M_{2g}(F)$, which contains naturally $B\otimes_\Q \ovl{B}\otimes_\Q F$.


 Using the embedding $F\otimes 1\otimes F\subset B\otimes \ovl{B} \otimes
 F$, one splits this $F$-structure $\mathrm{H}^1_B(A_{\C_p},F)$ into parts of
 $FK$-rank two, indexed by the embeddings of $F$ into $\ovl{\Q}$. We
 select the piece $\mathrm{H}^1_B(A^\bullet_{\C_p},F)_+$ corresponding to
 $\infty_0$.  We then have a natural embedding
 $\mathrm{H}^1_B(A^\bullet_{\C_p},F)_+\subset
 ((\mathcal{H}_+)_{\C_p}^{\mathrm{an}})^{\nabla_{\mathrm{GM}}}$, and
 $\mathrm{H}^1_B(A^\bullet_{\C_p},F)_+$ is stable under $p$-adic monodromy.
\end{para}
