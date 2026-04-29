**Proposition (SW-period $\equiv$ thimble integral; archimedean realisation
of the categorical Markov–Frobenius pairing).**

*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q_0$
([quantum observable universe](#def:quantum-observable-universe)).
Fix a vertical degree $k \in \{0, 1, 2, 3\}$ and a categorical mass
class $T_w \in H_n(R, q)$ with Hecke normal form
([Hecke normal form](#def:hecke-normal-form)).  Define the two
presentations of the degree-$k$ mass functional:*

- *(Algebraic / categorical, over $R$.)*

$$
  \mathfrak{m}^{(k)}_{\text{alg}}(T_w)
  \;:=\;
  \bigl|\bigl\langle \mathrm{tr}_M,\ E_\infty^{k, *}(T_w) \bigr\rangle\bigr|
  \;\in\; R,
$$

  *the pairing of the Markov trace against the level-$k$ page of the
  Gröbner–Shirshov spectral sequence
  ([GB spectral sequence](#prop:gb-spectral-sequence),
   [$E_\infty$ page identifications](#prop:e-infinity-page-identifications)).*

- *(Analytic / archimedean, over $\mathbb{C}$.)*

$$
  \mathfrak{m}^{(k)}_{\text{an}}(T_w; q_0)
  \;:=\;
  \tau\bigl|\Pi^{(k)}(T_w; q_0)\bigr|,
  \qquad
  \Pi^{(k)}(T_w; q_0)
  \;:=\;
  \sum_{\sigma} n_\sigma^{(k)} \oint_{\mathcal{J}_\sigma}
    \lambda_{\mathrm{SW}}^{(k)}(z; T_w)\, dz,
$$

  *where $\lambda_{\mathrm{SW}}^{(k)}$ is the $k$-th jet prolongation of
  the Seiberg–Witten differential on $\mathcal{E}_q$
  ([lepton mass integrals](#rem:lepton-mass-integrals)),
  $\mathcal{J}_\sigma$ are the Picard–Lefschetz thimbles attached to the
  discriminant locus of the color-tube cubic
  ([Picard–Lefschetz thimble](#def:picard-lefschetz-thimble)),
  $n_\sigma^{(k)} \in \mathbb{Z}$ are the intersection numbers
  $\langle \mathcal{K}_\sigma, \gamma \rangle$, and $\tau \colon R
  \hookrightarrow \mathbb{C}$ is the archimedean fibre functor.*

**Conditional equivalence.**
*Subject to the five hypotheses (A2.1–A2.5) below, both presentations
agree after applying $\tau$:*

$$
  \boxed{\;
    \tau\bigl(\mathfrak{m}^{(k)}_{\text{alg}}(T_w)\bigr)
    \;=\;
    \mathfrak{m}^{(k)}_{\text{an}}(T_w; q_0)
    \quad\text{for all } k \in \{0,1,2,3\}.
  \;}
$$

**Hypotheses (each isolates one derivation step).**

1. **(A2.1 — Critical-point completeness, over $R$.)**
   *The set of critical points of the SW action $S(z) = \int^z
   \lambda_{\mathrm{SW}}^{(1)}\, dz'$ equals the discriminant locus
   $\Delta(z) = 0$ of the color-tube cubic with multiplicity.
   This is an $R$-side identity: it follows from implicit
   differentiation of $F(z, c) = 0$ at $\partial F/\partial c = 0$,
   which is purely algebraic
   ([color-tube cubic](#rem:color-tube-cubic)).*

2. **(A2.2 — Hessian non-degeneracy, archimedean.)**
   *At each critical point $z_c \in \mathbb{C}$, the Hessian
   $H(z_c) = \partial^2 S/\partial z^2|_{z_c} \neq 0$ (Morse
   condition).  The discriminant of $\Delta(z)$ as a polynomial in
   $z$ is squarefree (degree $6$ with three distinct conjugate
   pairs), so the resultant $\mathrm{Res}(F, \partial F/\partial c)$
   has only simple zeros.  This statement is technically
   archimedean (it speaks of $\mathbb{C}$-roots), but the
   underlying squarefreeness is an $R[z]$-algebraic fact.*

3. **(A2.3 — Lefschetz decomposition with intersection numbers.)**
   *In the relative homology $H_1(\mathcal{E}_q, \mathrm{Re}\,S
   \to -\infty)$, the original real-axis contour $\gamma \subset
   \mathbb{R}$ decomposes as*

   $$
     \gamma \;=\; \sum_{\sigma \in \{1, \ldots, 6\}}
       n_\sigma\, \mathcal{J}_\sigma,
     \qquad n_\sigma \in \mathbb{Z}.
   $$

   *This is classical for Morse $S$ (Picard 1897; Lefschetz 1924);
   the work for our $\mathcal{E}_q$ is the **explicit computation of
   $n_\sigma$** at the six conjugate-paired thimbles.  This step is
   inherently archimedean.*

4. **(A2.4 — Real-axis $=$ thimble-sum identity, archimedean.)**
   *For each $k$ and each $T_w$,*

   $$
     \int_{-a(q_0)}^{\,a(q_0)} \lambda^{(k)}(z; T_w)\, dz
     \;=\;
     \sum_\sigma n_\sigma^{(k)}\,
       \oint_{\mathcal{J}_\sigma} \lambda^{(k)}(z; T_w)\, dz,
   $$

   *with $a(q_0) = (4-q_0)/(4q_0 + 3)$ derived in
   ([Möbius limit from thimble](#prop:mobius-limit-from-thimble)).
   Two sub-cases:*

   - *If all $n_\sigma = 0$ (the script's current finding,
     ([picard-lefschetz-thimble.witness.json](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/picard-lefschetz-thimble.witness.json))),
     both sides equal the residue contributions only, and the
     identity follows from Cauchy's theorem applied to a contour
     closed at $\pm \infty$ on $\mathbb{R}$ versus a half-plane
     contour through the discriminant residues.*
   - *If some $n_\sigma \neq 0$ (the intersection-number
     computation is currently uncertain per the script's
     caveats), the identity is the genuine Lefschetz formula.*

   *This is the **single most important derivation** for the
   "PL is correct" claim and is the open question #2 of
   ([baryon integration limit](#rem:baryon-integration-limit)).*

5. **(A2.5 — Product prescription = $\mathrm{Alt}^3$ isotype, $R$-side.)**
   *The baryon integrand $\lambda_{\mathrm{baryon}}(z) = \prod_{k=1}^3
   dc_k/dz$ equals the projection of the rank-$3$ colour-velocity
   tensor onto the sign isotype of $R[\mathrm{S}_3]$.  Derived in
   ([baryon product from Alt](#prop:baryon-product-from-alt)) — this
   hypothesis is **purely algebraic** and lives entirely on the
   $R$-side of $\tau$.*

**Strict archimedean split.**

*The proposition's statement spans both rings, but each piece is
sharply tagged:*

| ingredient | side of $\tau$ | object class |
|---|---|---|
| $\langle \mathrm{tr}_M, E_\infty^{k,*}(T_w)\rangle$ | $R$ | spectral-sequence pairing in $\mathrm{End}_{\mathbf{C}}$ |
| $T_w$, $H_n(R,q)$, $J^\bullet(q)$ | $R$ | filtered Hecke algebra |
| $F(z, c)$, $\Delta(z)$, $\pi_{\mathrm{Alt}}$ | $R$ | algebraic over $R[z, c]$ |
| $a(q) = (4-q)/(4q+3)$ as a Möbius transformation | $R$ | rational in $q$ |
| $z_c \in \mathbb{C}$, $|H(z_c)|$, $\arg H(z_c)$ | archimedean | requires $R \hookrightarrow \mathbb{C}$ |
| $\mathcal{J}_\sigma$, $n_\sigma$, $\Pi^{(k)}$ | archimedean | complex contours |
| $a(q_0)$ as a real number | archimedean | image of Möbius under $\tau$ |

*The equivalence asserts that $\tau$ commutes with the two natural
"mass" operations:*

$$
  \begin{tikzcd}[column sep=large]
    \mathfrak{m}^{(k)}_{\text{alg}}(T_w)
    \arrow[r, "\tau"] \arrow[d, "\text{cat. pairing}"', dashed]
    & \mathfrak{m}^{(k)}_{\text{an}}(T_w; q_0)
    \arrow[d, "\text{PL evaluation}", dashed] \\
    R \arrow[r, "\tau"]
    & \mathbb{C}
  \end{tikzcd}
$$

*The right-hand vertical (PL evaluation) is **only available** after
$\tau$ — Picard–Lefschetz thimbles are objects in $\mathbb{C}$, not
$R$.  The left-hand vertical (categorical pairing) is **only
available** before $\tau$ — the Markov–Frobenius pairing is an
$R$-bilinear form on $H_n(R, q)$, and its values land in $R$, not
$\mathbb{C}$.  The diagram's commutation is the content of the
proposition.*

**Status of derivation.**

| hypothesis | status | block |
|---|---|---|
| A2.1 (crit. pts $\subset$ discriminant) | **derived**, $R$-side | implicit differentiation, see proof below |
| A2.2 (Hessian Morse) | derived, $R$-side via squarefreeness | discriminant of $\Delta(z)$ is squarefree |
| A2.3 (Lefschetz decomposition exists) | classical, archimedean | Picard–Lefschetz, [witten2011] |
| A2.4 (real-axis = thimble sum) | **partial / open** | depends on $n_\sigma$ computation |
| A2.5 ($\mathrm{Alt}^3$ projector) | **derived**, $R$-side | [baryon-product-from-alt](#prop:baryon-product-from-alt) |

*Hypotheses A2.1, A2.2, A2.5 are derived; A2.3 is classical (cited);
A2.4 is the single open analytic step.  Once A2.4 is checked for our
specific $\mathcal{E}_q$, the equivalence is a theorem.*

**Proof (assuming A2.1–A2.5).**

**Step 1 (Yekutieli license: PL is the categorical surface integral.)**
*By the non-abelian Stokes theorem
([Yekutieli–Stokes remark](#rem:yekutieli-stokes)), the
categorical pairing $\langle \mathrm{tr}_M, T_w\rangle$ on
$H_n(R, q)$ admits a surface-integral representation*

$$
  \langle \mathrm{tr}_M, T_w\rangle
  \;=\;
  \mathrm{MI}\!\!\int_{\Sigma} \alpha_{T_w}
$$

*with $\partial \Sigma = \varrho$ a categorical loop and
$\alpha_{T_w}$ the connection $1$-form determined by $T_w$.  When
$\Sigma$ deforms to a thimble cap (A2.3), the surface integral
collapses to a sum of point residues — exactly the right-hand side of
the equivalence.  This step does not require $\tau$; it is the
$R$-side license.*

**Step 2 (Spectral-sequence reduction to $E_\infty$ pages, $R$-side.)**
*By
([GB spectral sequence](#prop:gb-spectral-sequence)) and
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications)),
$\langle \mathrm{tr}_M, T_w\rangle$ decomposes as $\sum_p \langle
\mathrm{tr}_M, E_\infty^{p,*}(T_w)\rangle$.  Each summand is an
$R$-rational quantity supported on the level-$p$ stratum
$J^p(q)/J^{p+1}(q)$.*

**Step 3 (Apply $\tau$; $E_0$ page becomes $\mathbb{C}$-realisation.)**
*Applying $\tau$ promotes each $J^p/J^{p+1}$ to its $\mathbb{C}$-vector-
space realisation $\tau(J^p/J^{p+1})$.  Under the geometric / jet
correspondence
([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)), the
level-$p$ stratum maps to the $p$-th jet bundle $J^p\mathcal{S}$ on
$\mathcal{E}_q$, with $\lambda^{(p)}_{\mathrm{SW}}$ as its tautological
section.  The pairing becomes a fibre integral.*

**Step 4 (Identify $E_0$ residues with thimble residues, archimedean.)**
*By A2.1 + A2.2, the residues of $\lambda^{(p)}_{\mathrm{SW}}$ at the
discriminant locus are non-degenerate Gaussian saddle-point integrals.
By A2.3 + A2.4 (Lefschetz decomposition + real-axis equality), these
residues evaluate to the thimble integrals $\oint_{\mathcal{J}_\sigma}
\lambda^{(p)}\,dz$, weighted by intersection numbers.*

**Step 5 (Channel-selection by $\mathrm{Alt}$, $R$-side.)**
*For the baryon channel ($k = 3$), A2.5 selects the integrand
$\prod_k dc_k/dz$ — an $R$-rational quantity that descends from the
sign isotype of $R[\mathrm{S}_3]$.  After $\tau$, this is the
integrand of $\Pi^{(3)}$.  Combining with Steps 3–4 yields
$\tau(\mathfrak{m}^{(3)}_{\text{alg}}) = \mathfrak{m}^{(3)}_{\text{an}}$.
Analogous specialisations of A2.5 to the trivial isotype (electron,
$k=0$) and standard isotype (muon, $k=1$) yield the remaining
equivalences. $\square$*

**Promotion of `conj:baryon-period-ratio`.**

*Under this proposition, the
([baryon period ratio](#conj:baryon-period-ratio)) conjecture is
the $k = 3$ case applied to $T_w = $ the proton's atomic braid.
Once A2.4 is checked numerically for the proton word (or proven
algebraically), the conjecture upgrades to a corollary.  The
conjectural-propagation rule
(CLAUDE.md §3b) is respected: this proposition keeps `conjecture`
status at the downstream level until A2.4 is closed.*

**Relation to other blocks.**

- *([GB spectral sequence](#prop:gb-spectral-sequence)) — algebraic side.*
- *([GB residue spectral sum](#prop:gb-residue-spectral-sum)) — symbolic
  shadow of this equivalence; the proposition gives its convergent
  archimedean realisation.*
- *([categorical mass as Markov trace](#prop:categorical-mass-markov)) —
  fixes the scalar weight $w_\lambda$; this proposition fixes the
  channel and the contour.*
- *([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence)) — the
  geometric image of the GB filtration under $\tau$, used in Step 3.*
- *([Yekutieli–Stokes remark](#rem:yekutieli-stokes)) — supplies
  the non-abelian Stokes license used in Step 1.*
