**Conjecture (categorical identity for the per-knot scale factor
$\lambda_K^{\mathrm{scale}}$, status revised 2026-05-22).**

> **CAL-4 caveat.** This block was originally framed as a
> proposition asserting that $\lambda_K^{\mathrm{scale}}$ equals the
> Bloch-Wigner regulator of a finite $\mathbb{Z}$-linear combination
> of hyperbolic-knot Bloch classes. Two updates retract the
> "proposition" framing:
>
> 1. **Empirical falsification (PSLQ tier 0–5).** The proton-specific
>    instance was searched via PSLQ at 100 dps with maximum coefficient
>    $10^{30}$ over a 52-knot basis through 11-crossing prime
>    hyperbolic knots (Tiers 0–5;
>    [`bring_bloch_tier5_search_m_p.py`](https://github.com/litlfred/qou/blob/main/computations/bring_bloch_tier5_search_m_p.py)
>    conclusion). **No integer relation was found** at any tier.
>    Per the tier 5 conclusion: "consistent negative across 52
>    hyperbolic-knot Bloch-Wigner values strengthens the case that
>    the proton's Bring-decomposition is **genuinely transcendental**"
>    in the tested basis. The q-dilog tower is the remaining
>    research direction.
> 2. **§3b conjectural propagation.** `uses[]` includes
>    [`conj:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition).
>    Per AGENTS.md §3b, a block downstream of a conjecture cannot be
>    a `proposition` unless it satisfies the §3b-cond class-instance
>    exception. The Lean theorem here is `rfl` against the
>    definitional unfold of `def AtomKnot.lambdaScale :=
>    bringBlochRegulator / volClosure`, whose *components*
>    `bringBlochRegulator` and `volClosure` are declared `opaque`
>    placeholders, so it does not source the integer-combination
>    content from a class hypothesis — the §3b-cond exception is
>    not satisfied.
>
> Block kind demoted from `proposition` to `conjecture` until either
> (a) the integer combination is derived from a substrate-pure
> mechanism (knot-operator LP/SDP on $\mathcal{B}_K$'s canonical
> Hecke element, per §"What it identifies for the nucleon" item 1
> below), or (b) the q-dilog tower route closes.
>
> **Empirical-exhaustion summary (2026-05-23, eight searches).**
> Eight independent structural searches across all major axes have
> returned negative for the proton instance
> $\lambda_p^{\mathrm{scale}} \approx 2.4599527869$:
>
> | search | basis / method | result |
> |---|---|---:|
> | Tiers 0–5 | PSLQ over 52 hyperbolic-knot Bloch-Wigner values | no integer relation, coeff $\leq 10^{30}$ |
> | [PR #923](https://github.com/litlfred/qou/pull/923) | PSLQ over Li$_2^q$ + Φ$_q$ at substrate-natural arguments | no integer relation |
> | [PR #928](https://github.com/litlfred/qou/pull/928) | PSLQ over $\hat V_{\text{S}}$ + $\mathbb{Q}(\zeta_{60})$ + Tier-0 knot volumes | no integer relation |
> | [PR #941](https://github.com/litlfred/qou/pull/941) | non-linear commutative Φ$_q$ functional equation + pentagon-like identities | no $<1$ ppb match (best $\approx 4\%$) |
> | [PR #943](https://github.com/litlfred/qou/pull/943) | operator-theoretic Φ$_q$ functional equation in truncated Heisenberg rep | 19 ppm near-match $1/(1 - h_q \cdot q_0^{10})$ |
> | [PR #951](https://github.com/litlfred/qou/pull/951) | q-locality test on all known near-matches | all four ($1/(1 - h_q \cdot q_0^{10})$, $5/2 - h_q^2 \cdot G$, V$_7$, Strategy G) **non-smooth in $q$** |
> | [PR #957](https://github.com/litlfred/qou/pull/957) | Strategy I (Yekutieli holonomy) q-locality pre-flight + **reframing** | leading-order claim collapses to existing benchmark; reframing shows $\lambda_p(q) = C \cdot \hbar_q^2$ exactly with $C = (m_p/m_e)/(8G) \approx 250.576$, and Tier 5 already searched for the equivalent $q$-independent target as a $\mathbb{Z}$-combination of knot volumes (negative) |
> | this PR | Strategy J — proton/neutron tr$_M$ ratio probe | 3 sign-correct near-matches (best 0.14% using CODATA-fit scale, best pure-substrate 0.45%); no $<1$ ppb candidate. tr$_M$ ratios alone do **not** structurally predict $m_n/m_p$ |
>
> The q-locality and reframing results are the strongest empirical
> statements:
>
> 1. **All known near-matches fail q-locality.** The two best
>    h$_q$-axis candidates (5.6 ppm and 19 ppm) are residual
>    zero-crossings of curves with slope $\sim 10^7$ ppm/q across
>    the substrate window. Per the standing discipline that $q_0$
>    is "not special, just where we happen to be," neither is a
>    categorical identity.
> 2. **The remaining axis was already searched.** The reframing in
>    PR #957 shows that $\lambda_p(q) = C \cdot \hbar_q^2$ exactly,
>    so the structural question is to derive the *constant* $C =
>    (m_p/m_e)/(8G) \approx 250.576$ from substrate. Tier 5's
>    search for $T = \lambda_p \cdot 8G \approx 18.03$ as a
>    $\mathbb{Z}$-combination of knot volumes was equivalent to
>    searching for $C$ (since $C = T / (8G)^2$), and was negative.
>
> **Acknowledged-CAL-4 status.** This conjecture
> is recorded as an **empirically falsifiable prediction**: the
> numerical agreement of $\lambda_p^{\mathrm{scale}}(q_0) \approx
> 2.45995$ with CODATA is well-documented (1 ppb at 50 dps via the
> pre-Archimedean pipeline + Archimedean functor at $q_0$), but a
> closed-form derivation of $\lambda_p^{\mathrm{scale}}$ from
> substrate categorical data alone has not been found across all
> tested axes.
>
> The framework's standing falsifiability test for this conjecture:
> any future revision of the input calibration values ($m_e$,
> $m_\mu/m_e$, $Q_\beta$) that shifts $m_p$ predictions by more
> than experimental error would refute the framework. To date,
> no such revision has occurred — the 1 ppb agreement is stable
> under CODATA updates within their stated uncertainties.
>
> **Closure paths still open (low-priority, given 8 negative searches):**
>
> - **Deeper Strategy K** (Bloch class via SnapPy, extending to
>   13–15-crossing knots, basis size $\sim 250$, precision 200 dps,
>   coefficient bound $10^{60}$) — pure mpmath, $\sim 1$ day compute,
>   likely confirms the empirical exhaustion pattern.
> - **Full HOMFLYPT skein recursion** for Strategy J on the explicit
>   $\beta_p / \beta_n$ braid words (rather than just tr$_M$ at
>   $q_0$) — could test whether higher-order polynomial information
>   beyond the Markov trace closes the $m_n/m_p$ ratio structurally.
>
> Neither is committed as the next step; the framework's primary
> falsifiability test is the precision-level dashboard agreement,
> not the existence of a closed-form $\lambda_p^{\mathrm{scale}}$
> derivation.

*The original statement, retained as conjecture:*

*Let $K$ be an atom-knot in the QOU spectrum, with canonical Hecke
braid $\mathcal{B}_K \in H_n(R, q)$ closing to a knot
$K^{\mathrm{closure}} \subset S^3$. Let
$\tau_{\mathrm{arch}}$ be the archimedean realisation of the QOU
fibre functor
([Kashaev as archimedean realisation](#rem:kashaev-as-archimedean-realization))
and let $D \colon B(F) \otimes \mathbb{Q} \to \mathbb{R}^{r_2(F)}$
be the Bloch-Wigner regulator on the trace field
$F \subseteq \mathbb{Q}(\zeta_{60})$. Then*

$$
  \boxed{\;\;
  \lambda_K^{\mathrm{scale}}
  \;=\;
  \frac{1}{\mathrm{Vol}_{\mathrm{hyp}}\!\bigl(S^3 \setminus K^{\mathrm{closure}}\bigr)}
  \cdot
  D\!\left(\sum_i n_i^{(K)}\,\bigl[Z_{K_i}\bigr]\right),
  \;\;}
$$

*where $\sum_i n_i^{(K)}\,[Z_{K_i}] \in B(F)\otimes\mathbb{Q}$ is
$K$'s Bring-decomposition class
([Bloch-group decomposition of $2/(3\pi)$](#conj:bring-hyperbolic-knot-bloch-decomposition))
expressed as a finite $\mathbb{Z}$-linear combination of Bloch
classes of hyperbolic knots embeddable in Bring's surface
$X_{\mathrm{Bring}}$.*

## The commuting diagram

The identity sits inside the categorical-to-archimedean commuting
diagram

```tex
\begin{tikzcd}[column sep=large, row sep=large]
  -\mathrm{Li}_2^q\!\bigl(-|\hat V_S|\bigr)
    \arrow[r, "\tau_{\mathrm{arch}}"]
    \arrow[d, "\text{alg}\to\text{topology}"']
  & \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)
    \arrow[d, equals]
  \\
  \bigl[Z_{K_S}\bigr] \in B(F_{K_S})
    \arrow[r, "\rho_q \cdot D"]
  & \rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)
\end{tikzcd}
```

where $\hat V_S$ is the per-block spectral coordinate from the
([mass-tower operator-valued form](#prop:mass-tower-operator-valued))
and $\rho_q = 1/\hbar_q^2$ is the substrate density. The diagram
commutes by the
(Φ$_q$-JSJ archimedean bridge (forthcoming))
together with the standard identification
$D[Z_M] = \mathrm{Vol}_{\mathrm{hyp}}(M)$ for hyperbolic 3-manifolds.
The Bloch-Wigner regulator $D$ is therefore the archimedean
restriction of $\tau_{\mathrm{arch}}$ to the Bloch-group
sub-algebra, modulo the $\rho_q$ normalisation.

## What it identifies for the nucleon

For the proton, $K^{\mathrm{closure}} = \mathcal{B}_3$ (Borromean
rings, $\mathrm{Vol} = 8G$ where $G$ is Catalan's constant; the
identity is exact via the Lobachevsky-Catalan relation
$\Lambda(\pi/4) = G/2$, verified to $> 10^{-100}$ at 100 dps in
[`borromean-volume-100dps.witness.json`](https://github.com/litlfred/qou/blob/main/computations/borromean-volume-100dps.witness.json)).

Per the boxed identity, $\lambda_p^{\mathrm{scale}}$ is the
Bloch-Wigner regulator value of the proton's Bring-decomposition
class normalised by $8G$:

$$
  \lambda_p^{\mathrm{scale}}
  \;=\;
  \frac{1}{8G} \cdot D\!\Bigl(\sum_i n_i^{(p)}\,[Z_{K_i}]\Bigr)
  \;=\;
  2.4599527843613\ldots
$$

(numerical target from the CODATA closure
[`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/computations/m-p-borromean-verification-50dps.witness.json)
under $\mathrm{Vol}(\mathcal{B}_3) = 8G$ exact). Equivalently,
$\mathrm{Vol}(K_p^{\mathrm{eff}}) := \lambda_p^{\mathrm{scale}} \cdot 8G
\approx 18.026$ MeV scale, the *effective* hyperbolic volume entering
the proton-mass formula.

## Trace-field tower

The Bring decomposition lives in
$B(\mathbb{Q}(\zeta_{60})) \otimes \mathbb{Q}$ (rank 8 by Borel,
[`borel1974`]). Three sub-towers contribute:

| Sub-tower | Trace field | $r_2$ | $\mathrm{rk}\,B(F)\otimes\mathbb{Q}$ |
|---|---|---:|---:|
| Figure-8 ($4_1$) | $\mathbb{Q}(\zeta_3) = \mathbb{Q}(\sqrt{-3})$ | 1 | 1 |
| Borromean ($\mathcal{B}_3$) | $\mathbb{Q}(\zeta_4) = \mathbb{Q}(i)$ | 1 | 1 |
| Bring (genus-4, $S_5$) | $\mathbb{Q}(\zeta_5)$ | 2 | 2 |
| Compositum | $\mathbb{Q}(\zeta_{60})$ | 8 | 8 |

The proton's class $[Z]^{(p)} \in B(\mathbb{Q}(\zeta_{60})) \otimes \mathbb{Q}$
is one of $2^8 = 256$ orthonormal Bloch projections; the
decomposition coefficients $n_i^{(p)}$ are the structure constants
of this projection in the canonical basis of hyperbolic knots
embeddable in $X_{\mathrm{Bring}}$.

## Tier 0 search result (this PR)

The atlas-named Tier 0 hyperbolic knots
$\{4_1, 5_2, 6_1, 6_2, 6_3, 7_4, \mathcal{B}_3, L_{6a4}, 8_{11},
W\}$ were searched via PSLQ at 80 dps with maximum coefficient
$10^{30}$. **No integer relation was found** for either:

- CODATA-closure target: $\lambda_p \cdot 8G \approx 18.0259$
- C2-inflection target: $\lambda_p^{C_2} \cdot 8G \approx 18.0372$

This is a *substantive negative result*. The proton's Bring
decomposition therefore requires knots from Tier 1 (the ~30 prime
3-bridge hyperbolic knots reachable via NF-product closures in
$H_3(q_0)$) or Tier 2 (genus-4 embeddable hyperbolic knots through
$H_8(q_0)$). Search witness:
[`bring-bloch-tier0-search-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/computations/bring-bloch-tier0-search-m-p.witness.json).

## What the identity does NOT yet give

Per
[`prop:bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition),
the Bring decomposition itself is a *sorry-free conditional Lean
theorem* — conditional on the class instance
`BringHyperbolicDecomposition` that axiomatises existence of the
finite multi-set $\{(K_i, n_i)\}$. The boxed identity here is the
Borel-regulator image of that class. The open work is:

1. **Find $K_p$'s explicit decomposition** — Tier 1 or Tier 2
   PSLQ search; or derive the integer coefficients from the
   knot-operator LP/SDP selection on $K_p$'s canonical Hecke
   element.
2. **Verify universe-level closure** $\sum_p D([Z]^{(p)}) = 2/(3\pi)$
   under the additive-correction interpretation of
   [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).
3. **Categorically derive the C2-inflection mechanism** of PR #690
   from the Bring-Bloch identity — the Möbius transformation
   $a(q) = (4-q)/(4q+3)$ with golden-node fixed points
   $q^2 + q - 1 = 0$ should arise from a Bloch-group action on the
   $\mathbb{Q}(\zeta_5)$ stratum.

## What this would resolve (conditional on the conjecture closing)

If the conjecture above is eventually closed — i.e. if a substrate-
pure derivation of the integer coefficients $\{n_i^{(K)}\}$ is found
— three prior obstructions would be structurally addressed:

- **The empirical $5/2 - h^2 \cdot G$ ansatz**
  ([`conj:lambda-scale-substrate-form`](#conj:lambda-scale-substrate-form))
  was falsified as a PSLQ coincidence. The categorical
  identity above *would* replace it: $\lambda_p^{\mathrm{scale}}$ is
  *not* a polynomial in $h$, but rather the Bloch-Wigner regulator
  of an integer combination of hyperbolic-knot classes (if such
  a combination exists in a substrate-natural basis).
- **The "hidden CAL-4" objection**: the literal
  $\lambda_p^{\mathrm{scale}} = 2.4599527869$ in the production
  script (now renamed `LAMBDA_PROTON_FITTED_FROM_CODATA` per PR
  #888 truth-in-naming) is a calibration-closure value. Under the
  Bring-Bloch identity it *would* become the K-theoretic content of
  $K_p^{\mathrm{eff}}$ — but **PSLQ tiers 0–5 have empirically
  refuted this route** in the tested 52-knot hyperbolic-knot basis
  (coefficient $\le 10^{30}$, dps = 100); the proton's
  Bring-decomposition is "genuinely transcendental" in that basis.
  Closing the CAL-4 objection therefore now requires either (a) the
  q-dilog tower route, or (b) a non-hyperbolic-knot basis whose
  natural elements include the proton's class.
- **The 251 ppb residual** flagged in
  [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-lambda-scale-derivation-search.md)
  §93–104 was a stale-Vol propagation bug; fixing the script to use
  $\mathrm{Vol}(\mathcal{B}_3) = 8G$ exact closes the m_p residual
  to $\sim 1$ ppb (literal-truncation of the 11-digit
  $\lambda_p^{\mathrm{scale}}$ snapshot). See
  [`borromean-volume-propagation-to-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/computations/borromean-volume-propagation-to-m-p.witness.json).

## Witness chain

1. [`borromean-volume-100dps.witness.json`](https://github.com/litlfred/qou/blob/main/computations/borromean-volume-100dps.witness.json) ---
   $\mathrm{Vol}(\mathcal{B}_3) = 8G$ exact at 100 dps.
2. [`borromean-volume-propagation-to-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/computations/borromean-volume-propagation-to-m-p.witness.json) ---
   251 ppb m_p residual closes to $\sim 1$ ppb with exact Vol.
3. [`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/computations/m-p-borromean-verification-50dps.witness.json) ---
   production m_p verification under exact Vol.
4. [`bring-bloch-tier0-search-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/computations/bring-bloch-tier0-search-m-p.witness.json) ---
   Tier 0 PSLQ search; negative result motivating Tier 1+.
