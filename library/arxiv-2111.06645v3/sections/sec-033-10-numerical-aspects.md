---
doc_id: arxiv-2111.06645v3
doc_title: ""
section_id: sec-033-10-numerical-aspects
section_title: "Numerical aspects"
section_number: 10
pages: 71-74
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α7→ Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.828
---
[]{#sec.compKash label="sec.compKash"}

In this section, we describe how the power series whose existence is predicted by the modularity conjecture can be computed effectively via a numerical computation of the Kashaev invariant, extrapolation, and recognition of algebraic numbers in a known number field. We also describe other methods that are applicable to the power series for $\sigma$ different from $\sigma_1$, as well as the smooth truncation methods of "evaluating" factorially divergent power series at non-zero arguments that were discussed in Section [\[sub.4.3\]](#sub.4.3){reference-type="ref" reference="sub.4.3"}. The actual numerical data for several knots will then be presented in the appendix.

## Computing the power series $\boldsymbol{\Phi_\alpha^{(K,\sigma)}(h)}$ {#sub.comp2}

In this subsection, we explain the various methods that can be used to compute the coefficients of the power series for all $\alpha\in\mathbb Q$ and $\sigma\in\mathcal P_K$ numerically and then exactly as algebraic numbers.

**Step 1: Computing the colored Jones polynomials.** To compute the Kashaev invariant $\langle K \rangle_N$ of a knot $K$, we use the Murakami--Murakami formula $\langle K \rangle_N=J_N\big({\rm e}^{2 \pi {\rm i}/N}\big)$, where ${J_n(q)\!=\!J_{K,n}(q)}$ is the $n$-th colored Jones polynomial, together with a theorem of T.T.Q. Lê and the first author [@GL] that asserts the existence of a recursion relation for the polynomials $J_n(q)$. This reduces the problem to that of computing/guessing this recursion relation concretely for a given knot. This in turn has been solved for several knots in joint work of the first author, X. Sun and C. Koutschan [@GK; @GK2; @GS]. The solution required a modulo $p$ computation of the $N$-th colored Jones polynomial (for several primes $p$ and several thousand values of $N$), together with a careful guess of the supporting coefficients of such a recursion. In particular, the recursion was computed in [@GS] for the twist knots $K_p$ with $|p|\le15$, was guessed in [@GK] for the $(-2,3,3+2p)$ pretzel knots with $|p|\le5$, and was computed (when $p=2$) or guessed (when ${p=3,4,5}$) in [@GK2] for the double twist knots $K_{p,p}$ with $2\le p\le5$.

**Step 2: Computing the Kashaev invariant for large $\boldsymbol{N}$.** In order to get numerical information about the asymptotics of the Kashaev invariant $\langle K \rangle_N$, we need to be able to compute it numerically to high precision for large values of $N$, say of the order of $N=5000$. Although both the Kashaev invariant and the colored Jones polynomial are given by finite-dimensional terminating $q$-hypergeometric sums, and the latter have been programmed in `Mathematica` [@B-N], these programs can only give the value of the colored Jones polynomial and of the Kashaev invariant for modest values of $N$, say, up to $N=20$, which is far less than we need for the numerical extrapolation. By using the recursion, we can compute $J_n(\zeta_N)$ numerically to high precision for $N$ large and $0<n<N$. (This is far faster than computing the colored Jones polynomials $J_n(q)$ for these values of $n$ and substituting $q=\zeta_N$ at the end.) However, this does not give the Kashaev invariant $\langle K \rangle_N=J_{K,N}(\zeta_N)$ because the recursion gives $P(q,q^n)J_n(q)$ as a linear combination of a bounded number of previous values $J_{n-i}(q)$, where $P(q,x)$ is a fixed polynomial that is always divisible by $1-x$. To overcome this, we use the recursion relation and its first $r$ derivatives, where $(1-x)^r\|P(q,x)$, to get a recursion for the length-$r$ vector . We can the use the recursion to compute the whole vector numerically for $q=\zeta_N$ and $0<n<N$, and the single value $J_n(q)$ for $n=N$. It follows that

::: Proposition
[]{#prop.ckashaev label="prop.ckashaev"} The Kashaev invariant $\langle K \rangle_N$ of a knot $K$ can be computed in $O(N)$ steps.
:::

This linear-time algorithm, which seems to be new even for the Kashaev invariant, can be used equally well to compute $J(\gamma N)$ for $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)\in\mathrm{SL}_2(\mathbb Z)$ fixed and $N$ tending to infinity, or even $J(\gamma X)$ with $\gamma=\bigl(\smallmatrix a&b\\c&d\endsmallmatrix\bigr)$ fixed and $X$ tending to infinity with fixed fractional part, since this simply the value of $J_n(\gamma X)$ with $n$ equal to the denominator of $\gamma X$ and can be calculated by the same trick. Note that the computation takes time $O(N)$ numerically and $O\big(N^3\big)$ if we work over $\mathbb Q[\zeta_N]$.

**Step 3: Computing $\boldsymbol{\Phi_\alpha^{(K,\sigma_1)}(h)}$.** Once we know how to compute $J(\gamma N)$ for large integers $N$ (or even $J(\gamma X)$ for large $X$ with bounded denominator), we can we can obtain the first few coefficients of the power series numerically for a fixed rational number $\alpha=\gamma(\infty)$ by combining the quantum modularity conjecture [\[QMCa\]](#QMCa){reference-type="eqref" reference="QMCa"} (or [\[QMCb\]](#QMCb){reference-type="eqref" reference="QMCb"}) together with the extrapolation method of the second author (as described in detail in [@GrMor] or the appendix of [@GV]) or the closely related Richardson transform [@Bender Chapter 8]. This is quite effective and gives, for instance, the first hundred coefficients of the series [\[as41\]](#as41){reference-type="eqref" reference="as41"} or forty coefficients of the series [\[as52\]](#as52){reference-type="eqref" reference="as52"} in only a few minutes of computing time. We should mention, however, that this extrapolation method requires either exact numbers or else very high precision (often several hundred or even thousand decimal digits in the calculations we did.)

**Step 4: Recognizing the coefficients exactly.** Given that the coefficients of are conjecturally algebraic numbers in a specific number field, we can then test numerically by using the standard LLL (Lenstra--Lenstra--Lovasz) algorithm to approximate the numerically computed coefficients by rational linear combinations of a basis of this field. If this works to high precision with coefficients that are not too large and have only small primes in the denominator, then we have considerable confidence that the approximate equality is an exact one. The method is self-verifying in the sense that the success at each stage requires the correctness of the answer guessed at the previous stage.

**Step 5: Computing $\boldsymbol{\Phi_\alpha^{(K,\sigma_0)}(h)}$.** In this step, we explain how to compute the expansion of the element of the Habiro ring at a root of unity, in linear time. More precisely, we have:

::: Proposition
[]{#prop.hab label="prop.hab"} The series is computable in $O(N)$ steps.
:::

This follows from the fact that the expansion of the Habiro element at $q=\zeta_\alpha{\rm e}^h$ up to $O(h)^{N+1}$ requires $cN$ terms of the cyclotomic polynomial of $K$, which is a linear combination of the first $cN$ colored Jones polynomials of $K$. An alternative formula, inspired by Mahler's ideas on $p$-adic interpolation, gives the following expansion of the Habiro element: $$\label{hab-mahler}
\Phi^{(K,\sigma_0)}_\alpha(h) = \sum_{k=1}^{cn} \widehat{J}^K_n\big(\zeta_\alpha{\rm e}^h\big) + O\big(h^{n+1}\big),$$ where $c$ is the denominator of $\alpha$, $\zeta_\alpha=\mathbf{e}(\alpha)$ and $$\widehat{J}^K_n(q) = \sum_{k=1}^n (-1)^{n-k} \binom{n}{k}_q
q^{\frac{k(k-1)}{2}} J^K_{n-k+1}(q)  q^{-\frac{n(n+1)}{2}}$$ and is the $q$-binomial symbol and $(q;q)_n=(1-q)\big(1-q^2\big)\cdots\allowbreak (1-q^n)$ is the $q$-Pochhammer symbol. The right-hand side of [\[hab-mahler\]](#hab-mahler){reference-type="eqref" reference="hab-mahler"} gives a well-defined formal power series since $\widehat{J}^K_{cn}\big(\zeta_\alpha{\rm e}^h\big)$ lies in $h^n \mathbb Q[[h]]$.

**Step 6: Computing the remaining power series.** Once we have the leading term in the original QMC, we can obtain the numerical terms by successively subtracting the corrections coming from the values of $\sigma$ different from $\sigma_1$ as explained in Sections [\[sub.4.1\]](#sub.4.1){reference-type="ref" reference="sub.4.1"} (using "optimal truncation") and [\[sub.4.3\]](#sub.4.3){reference-type="ref" reference="sub.4.3"} (using the more precise "smooth truncation" described in Section [\[sub.optimal\]](#sub.optimal){reference-type="ref" reference="sub.optimal"} and in more detail in [@GZ:optimal]), where numerical examples were also given.

**Step 7: Alternative methods.** In Steps 2 and 3, we discussed how to obtain the coefficients of from the original QMC together with the high-speed high-precision computation of Jones polynomials at roots of unity and numerical extrapolation; in Steps 4 and 5 we explained how to get the series for $\sigma$ Galois conjugate to $\sigma_1$ and for $\sigma=\sigma_0$, respectively; and in Step 6 we described how to obtain the remaining series by using the *refined* quantum modularity conjecture together with optimal truncation. However, there are at least two other ways to get these other series that are of interest and are sometimes more efficient.

The first way is to use the formal Gaussian integration of Section [\[sec.perturbation\]](#sec.perturbation){reference-type="ref" reference="sec.perturbation"} and [@DG; @DG2]. This method uses exact arithmetic and allows the computation of few terms (in practice $k \leq 5$) as exact algebraic numbers for many knots (such as those with ideal triangulations with up to 15 ideal tetrahedra). See also [@Ga:exact].

The other, which is completely different, is based on the asymptotics near roots of unity of the holomorphic functions in the upper half plane (generalized Nahm sums) that we study in [@GZ:qseries]. Since Nahm sums converge quadratically, the values of those functions at $\tau=\alpha+{\rm i}/N$ can be computed in $O\big(\sqrt{N}\big)$ steps and after extrapolation give a numerical computation of the algebraic numbers . This method, when applicable, is not only much faster (time $O\big(\sqrt N\big)$ rather than $O(N)$), but also has the major advantage of allowing the simultaneous numerical computation of for all $\alpha$ of a fixed denominator and for all $\sigma$ in a Galois orbit which (after multiplication by $D_k$ and by a suitable $S$-unit) reduces the problem of recognizing the list of coefficients as algebraic numbers to the problem of recognizing numerically computed *integers*, albeit of growth $k!^2 C^k$. This allowed us to compute, for instance, 100 coefficients of the series for the $5_2$ knot for $\alpha=0$ and $a=1/2$ and for all three representations $\sigma$ in the Galois orbit of the geometric representation, and it allowed us to compute 37 terms of the series of the $(-2,3,7)$ pretzel knot for $\alpha=0$ and for both Galois orbits (each of size 3) of nontrivial representations $\sigma$. It is remarkable that this method allows the computation of series for representations not Galois conjugate to the geometric one, though not for the trivial representation $\sigma_0$.

**Orientation conventions.** Finally, we have to discuss an annoying technical point, namely, the choice of a consistent set of conventions for the two classical invariants (namely the trace field and the complex volume of a knot) and the two quantum invariants (namely the colored Jones polynomial and the Kashaev invariant of a knot). These conventions are especially important since the tables of knots rarely distinguish a knot from its mirror, and (for instance) the name $5_2$ of the unique hyperbolic 5-crossing knot does not convey this distinction.

On the other hand, replacing a knot $K$ by its mirror $K^*$ reverses the orientation of the knot complement $M_K = S^3 \smallsetminus K$, which implies that

-   $F_{K^*} = \overline{F_K}$ and $v(K^*) =\overline v(K)$.

-   $J_{K^*,N}(q)=J_K\big(q^{-1}\big)$ and $\langle K^* \rangle_N=\overline{\langle K \rangle_N}$ and $J^{K^*}(x)=J^K(-x)=\overline{J^K(x)}$.

Thus, a random orientation convention for $K$ might not match the asymptotics whose coefficients are in a fixed subfield of the complex numbers, and not on its complex conjugate subfield.

The Jones (hence, also the colored Jones) polynomial $J_{K}(q) \in \mathbb Z\big[q^{\pm 1}\big]$ of a knot (or a link) $K$ is uniquely determined by the following skein-relation [@Jones] $$\label{jones}
q  J_{\left(\includegraphics[height=0.1in]{figures/Rp.pdf} \right)}(q)
-q^{-1} J_{\left(\includegraphics[height=0.1in]{figures/Rn.pdf} \right)}(q) =
\big(q^{1/2}-q^{-1/2}\big)
J_{\left(\includegraphics[height=0.1in]{figures/Rs.pdf} \right)}(q),
\qquad J_{\text{unknot}}(q)=1 .$$ In particular, for the left-hand trefoil $3_1$, we have: $J_{3_1}(q)= -q^{4} + q^{3} + q^{1}$. Moreover, the colored Jones polynomial $J_{K,N}(q) \in \mathbb Z\big[q^{\pm 1}\big]$ is normalized to be $1$ at the unknot, and to equal to the Jones polynomial when $N=2$.

Note that the `SnapPy` program [@snappy] for computing the Jones polynomial agrees with [\[jones\]](#jones){reference-type="eqref" reference="jones"}, whereas the `Mathematica` program `KnotAtlas` [@B-N] polynomial differs by replacing $q$ by $1/q$:

::: center
  -------------------------------------- ---------------------------------
  `L = Link(braid_closure=[-1,-1,-1])`   `Jones[BR[2, {-1, -1, -1}]][q]`
  `L.jones_polynomial()`                 `-q^-4 + q^-3 + q^-1`
  `-q^4 + q^3 + q^1`                     
  -------------------------------------- ---------------------------------
:::

We will be using the consistent orientation convention for $M_K$ of the `SnapPy` program (when $K$ is given as the closure of a braid, or via a planar projection, or via an augmented DTcode or Gauss code), which has the added advantage that it also gives shapes of tetrahedra corresponding to the hyperbolic structure (exactly or numerically), as well as the trace field (exactly) and the complex volume $v(K)$ (exactly or numerically).
