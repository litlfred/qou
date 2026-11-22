# Higher Atiyah classes of the holomorphic jet tower on Bring's surface

**Date:** 2026-10-12. **Follows:** [`2026-10-12-jet-tower-band-construction.md`](2026-10-12-jet-tower-band-construction.md) §2.4. That section
left open whether the higher jet extension classes on $\Sigma_4$ vanish.
**Scope:** read-only audit. No content block, `.lean` file or bean was edited.
**Discipline:** no reading is chosen because it gives persistence. Every line bundle is evaluated, and
the verdict for $T\Sigma_4$ is the one the formula gives. Claim tags:
**[D]** derived here; **[S]** standard and cited; **[O]** open.

## 0. Answer

For a line bundle $L$ of degree $d$ on a compact Riemann surface of genus $g\ge2$, the $n$-th jet
extension class lives in a group that is **always one-dimensional**:
$\mathrm{Ext}^1(J^{n-1}L,K^nL)\cong\mathbb C$. Under that isomorphism it equals

$$
e_n(L)\;=\;c\cdot n\,\bigl(d+(n-1)(g-1)\bigr),\qquad c\neq0\ \text{universal.}
$$

| $L$ on $\Sigma_4$ ($g=4$) | $d$ | $e_n \propto$ | zero at |
|---|---|---|---|
| $T\Sigma_4$ (frame bundle, holomorphic) | $-6$ | $3\,n(n-3)$ | **$n=3$ only** |
| $K_{\Sigma_4}$ | $6$ | $3\,n(n+1)$ | never |
| $K^{-1/2}$ (spin; Bring is spin) | $-3$ | $3\,n(n-2)$ | $n=2$ only (projective structures) |
| general $d$ | $d$ | $n(d+3(n-1))$ | $n=1-d/3$, if that is a positive integer |
| any $L$, $C^\infty$ category | — | $0$ | every $n$ |

So for $T\Sigma_4$ the obstruction is **not** perpetual. It vanishes at exactly one level, $n=3$, by the
invariant $d+(n-1)(g-1)=0$. The level is not chosen here. It is the classical fact that Bol's
third-order operator $K^{-1}\to K^2$ exists once a projective structure is fixed. For $K$ the class is
non-zero at every level. But all levels give the same number up to the factor $n(n+1)$, so this
"persistence" is $\deg K\neq0$ restated, not a new obstruction at each level (§4).

## 1. Setup [S]

$X$ is a compact Riemann surface of genus $g$, $K=\Omega^1_X$, and $L$ is a holomorphic line bundle of
degree $d$. $J^nL$ has rank $n+1$, with the exact sequences

$$
0\to K^n\otimes L\to J^nL\xrightarrow{\ \pi_n\ }J^{n-1}L\to0,\qquad J^0L=L.
$$

So $J^nL$ carries a filtration $0\subset F^n\subset\cdots\subset F^0=J^nL$ with
$F^i/F^{i+1}\cong K^iL$. $F^n=K^nL$ is the deepest piece and $L$ is the top quotient. The class
$e_n\in\mathrm{Ext}^1(J^{n-1}L,K^nL)=H^1\bigl(X,\mathcal H_n\bigr)$, with
$\mathcal H_n:=(J^{n-1}L)^\vee\otimes K^nL$, vanishes iff $\pi_n$ has a holomorphic splitting.

- $n=1$: $e_1$ is the Atiyah class $a(L)\in H^1(X,K)$. A holomorphic connection on $L$ exists iff
  $a(L)=0$, iff $d=0$ on a curve (Atiyah, *Complex analytic connections in fibre bundles*, Trans. AMS 85
  (1957) 181–207; Weil). **Not held** in `library/`.
- A connection is an $\mathcal O$-linear section $M\to\mathcal P^1(M)$ of the first-jet projection.
  **Held:** André, *Period mappings and differential equations*
  (`library/arxiv-math-0203194v1/sections/sec-041-154-a-non-archimedean-riemann-hilbert-equivalenc.md:132–139`,
  para 3.4.5).

## 2. The Ext group is $\mathbb C$ at every level [D]

**Graded pieces of $\mathcal H_n$.** Dualising $J^{n-1}L$ reverses the filtration. Its pieces are
$K^{-i}L^{-1}$ for $i=0,\dots,n-1$, and $L^{-1}$ is now the *sub*. Tensoring with $K^nL$ gives pieces
$K^{n-i}$, i.e. $K^m$ for $m=1,\dots,n$. The sub is $K^n$ and the top quotient is $K^1$. The quotient
map $\rho\colon\mathcal H_n\to K$ is restriction of a homomorphism to the deepest piece
$K^{n-1}L\subset J^{n-1}L$.

**Vanishing.** For $m\ge2$ and $g\ge2$, Serre duality gives $H^1(X,K^m)\cong H^0(X,K^{1-m})^\vee$.
This is $0$ because $\deg K^{1-m}=(1-m)(2g-2)<0$. Also $H^1(X,K)\cong H^0(X,\mathcal O)^\vee=\mathbb C$
and $H^2=0$ for any coherent sheaf on a curve.

**Induction.** Let $\mathcal H_n'=\ker\rho$. It is filtered by $K^m$, $m\ge2$. Each short exact
sequence $0\to A\to B\to C\to0$ gives $H^1(A)\to H^1(B)\to H^1(C)\to H^2(A)=0$. So $H^1(\mathcal H_n')=0$.
Then the sequence for $0\to\mathcal H_n'\to\mathcal H_n\to K\to0$ gives

$$
\rho_*\colon\ \mathrm{Ext}^1(J^{n-1}L,K^nL)\xrightarrow{\ \sim\ }H^1(X,K)\cong\mathbb C\qquad(n\ge1,\ g\ge2).
$$

This is the subtle point. The graded pieces $K^m$ with $m\ge2$ contribute nothing. But the **Ext group
does not vanish at any level**, because $K^1$ is always the top quotient of $\mathcal H_n$. So a
"$H^1(K^m)=0$, hence $e_n=0$ for $n\ge2$" argument is **wrong**. The correct conclusion is that $e_n$ is
detected by the single scalar $\rho_*e_n$.

**What $\rho_*e_n$ is.** It is the class of the pulled-back two-step extension

$$
0\to K^nL\to N_n\to K^{n-1}L\to0,\qquad N_n:=\ker\bigl(J^nL\to J^{n-2}L\bigr).
$$

So $e_n=0$ iff $N_n$ splits holomorphically.

## 3. Computing $[N_n]$ [D]

Take charts with coordinates $z$ and $w$, $z=\varphi(w)$, and frames with $e_\beta=h\,e_\alpha$, so
$f=hF$. Elements of $N_n$ at $p$ are jets of sections $f=u\frac{(z-p)^{n-1}}{(n-1)!}+v\frac{(z-p)^n}{n!}+\cdots$.
Write $a=\varphi'$, $b=\varphi''/2$ and $\ell=h'/h$ at $p$. Expanding $F=f/h$ in $w$ gives

$$
U=\frac{a^{n-1}}{h}\,u,\qquad V=\frac{a^n}{h}\Bigl(v+\bigl(\tfrac{n(n-1)b}{a^2}-n\ell\bigr)u\Bigr).
$$

This was checked symbolically with exact rational arithmetic for $n=1,\dots,5$, including a cubic term
in $\varphi$ and a quadratic term in $h$ (sympy, scratch script; no witness emitted). The off-diagonal
entry, read in $\mathrm{Hom}(K^{n-1}L,K^nL)=K$, is the Čech 1-cocycle

$$
\omega_{\alpha\beta}=\tfrac{n(n-1)}{2}\,d\log\varphi'_{\alpha\beta}\;-\;n\,d\log h_{\alpha\beta}.
$$

Here $[d\log h]=a(L)$ and $[d\log\varphi']=a(T_X)=-a(K)$, both in the same frame convention. Atiyah's
class is additive, and $a(M)=c'\deg M$ under $H^1(K)\cong\mathbb C$. So

$$
[N_n]=-n\Bigl(a(L)+\tfrac{n-1}{2}\,a(K)\Bigr)=c\cdot n\bigl(d+(n-1)(g-1)\bigr).
$$

**Cross-checks against classical results** [S]. Each result below is cited by author and title only.
Gunning and Bol appear in `library/` only as bibliography entries:
`alvarez-gaume-moore-vafa-1986-…/sections/sec-031-12-gunning-r-introduction-to-riemann-surfaces-pr.md`,
and `arxiv-math-0203194v1/sections/sec-059-i-examples.md:783` (Gunning, *Special coordinate coverings*).

- **$n=1$:** $[N_1]=-a(L)$. This is Atiyah's theorem.
- **$L=K^{-1/2}$:** $e_1\propto 1-g\neq0$. $J^1(K^{-1/2})$ is the non-split Gunning extension of $K^{-1/2}$
  by $K^{1/2}$, the uniformizing oper bundle. At $n=2$, $e_2\propto2(1-g+g-1)=0$. So
  $J^2(K^{-1/2})\to J^1$ splits. These splittings are the second-order operators $K^{-1/2}\to K^{3/2}$,
  i.e. projective structures. Their existence on every Riemann surface is Gunning's theorem (*Lectures on
  Riemann Surfaces*, Princeton 1966; *On uniformization of complex manifolds: the role of connections*,
  1978).
- **General zero locus** $d=-(n-1)(g-1)$, i.e. $L=K^{(1-n)/2}$. This matches the Bol operators
  $K^{(1-n)/2}\to K^{(1+n)/2}$ of order $n$, which exist given a projective structure. For $L=T=K^{-1}$
  that is $n=3$.

The library also holds André's discussion of projective connections
(`arxiv-math-0203194v1/sections/sec-042-155-examples-and-applications.md:393–438`) and the jet
description of connections cited in §1. **Atiyah 1957 is not held.** "Atiyah class" occurs in the
library only in reference lists: `arxiv-0707.2052v1`, `arxiv-0801.3233v4`, `arxiv-1305.7175v4`, and
`m4-24/…/sec-092…:824` (Kapranov, *Rozansky–Witten invariants via Atiyah classes*). The general
formula above is **[D]**, not quoted from a held source.

## 4. Per-level verdicts on $\Sigma_4$

**$L=T\Sigma_4$.** $e_n\propto3n(n-3)$.
- Non-zero for $n=1,2$ and every $n\ge4$; zero at $n=3$.
- "Non-zero at every level" is **excluded** in this reading.
- Invariant: the closed form $n(d+(n-1)(g-1))$ at $d=2-2g$, i.e. $n(n-3)(g-1)$.
- Scope: (b)-type, *for this reading*. The proof is a hand derivation with a symbolic check, consistent
  with Bol/Gunning. It is **not** Lean-checked.
- It does not exclude other readings of item 3.

**Holomorphic frame bundle of $T\Sigma_4$.** This is the $\mathbb C^\times$-bundle of $T$, so it has the
same answer.

**Reeb / unit tangent circle bundle.** This is a smooth $\mathrm U(1)$-bundle with no holomorphic
structure, so only the $C^\infty$ answer applies.

**$C^\infty$, any bundle, every $n$.** $e_n=0$ [S]. The relevant Ext group is $H^1$ of a fine sheaf of
smooth sections (partitions of unity), so every smooth jet sequence splits. This is the regime
`archimedean-lifting-intro.md:1` declares.

**$L=K$.** $e_n\propto3n(n+1)\neq0$ for all $n\ge1$. This is the **one reading in which a non-zero class
persists at every level.** It is recorded, not adopted, for four reasons:
1. All $e_n$ sit in the same line $H^1(K)\cong\mathbb C$ and are fixed multiples of one number, $g-1$.
   No level carries information the first level lacks.
2. They obstruct **splitting**, not **existence**. $J^nL$ exists for every $n$ and the tower never stops.
   This is an "obstruction to a canonical unit section" (tension T2 of the parent audit), not an
   obstruction to lifting.
3. They have degree 1, in a $\mathbb C$-vector space. They are not $\kappa_n\in H^2(\mathcal S,\mathcal B)$.
4. $K$ is not the bundle `thm:qu-to-qou` names. Its $-6$ is $\deg T$, and $T$ fails at $n=3$.

**General $d$ (on $\Sigma_4$).** Every level is non-zero iff $d\notin\{0,-3,-6,-9,\dots\}$. $T$, with
$d=-6$, falls in the excluded set.

## 5. What this implies for "perpetual obstruction"

- **No reading built on $T\Sigma_4$ gives persistence.**
  - Holomorphic jet extension classes of $T$ vanish at $n=3$.
  - $C^\infty$ classes vanish at every level.
  - The degree-2 bands are settled in the parent audit: zero, torsion, or ill-posed.
- **A persistent reading exists only by changing both the bundle and the degree.**
  - Use $K$, or any $d\notin-3\mathbb Z_{\ge0}$.
  - Recast item 3 as "the holomorphic jet tower never splits at any level".
  - The resulting statement is equivalent to $d+(n-1)(g-1)\neq0$ for all $n$, a congruence on $d$. It is
    not a perpetual cohomological phenomenon.
  - Adopting it is a restatement of the theorem and an owner decision. It is not a repair.
- **Complementary-subgroup argument.** It has no analogue here, because every $e_n$ lies in one
  1-dimensional space. Corrections cannot be "complementary" to $e_1$. The parent audit's §3 count 3
  (indecomposability) applies even more strongly.

## 6. Formalizability (no Lean written)

- **The arithmetic:** $n(d+(n-1)(g-1))\big|_{d=2-2g}=n(n-3)(g-1)$. This is a one-line `ring` identity
  over any `CommRing`.
- **Vanishing $H^1(X,K^m)=0$ for $m\ge2$:** this needs Serre duality and degree theory on curves.
  Whether Mathlib has these at v4.24 has **not been checked here** [O].
- **Ext group and cocycle:** the identification $\mathrm{Ext}^1\cong H^1(K)$ and the cocycle computation
  would need jet sheaves in Mathlib. These are presumed absent and were not searched [O].
- **The algebraic core:** $e_n$ factors as $n\cdot(\text{linear in }d)$ with a root at $n=1-d/(g-1)$.
  This core is formalizable today as a statement about the cocycle coefficients.

## 7. Status summary

| claim | tag |
|---|---|
| Jet filtration, Atiyah's theorem, smooth splitting | [S] |
| $\mathrm{Ext}^1(J^{n-1}L,K^nL)\cong\mathbb C$ for all $n\ge1$, $g\ge2$ | [D] |
| $e_n=c\,n(d+(n-1)(g-1))$ | [D], symbolically checked $n\le5$; consistent with Gunning/Bol [S] |
| $T\Sigma_4$: $e_3=0$, others $\neq0$; no persistence | [D] |
| $K$: persistent but degenerate (one scalar) | [D] |
| Value of the universal constant $c$ ($\pm2\pi i$-type) | not needed; only $c\neq0$ is used [S] |
| Mathlib coverage of Serre duality on curves | [O] |
