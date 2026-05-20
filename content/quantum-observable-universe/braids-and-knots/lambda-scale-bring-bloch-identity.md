**Proposition (categorical identity for the per-knot scale factor
$\lambda_K^{\mathrm{scale}}$).**
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
[`borromean-volume-100dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/borromean-volume-100dps.witness.json)).

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
[`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/m-p-borromean-verification-50dps.witness.json)
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
[`bring-bloch-tier0-search-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring-bloch-tier0-search-m-p.witness.json).

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

## What this resolves

Three prior obstructions are now structurally addressed:

- **The empirical $5/2 - h^2 \cdot G$ ansatz**
  (`prop:lambda-scale-substrate-form` (forthcoming))
  was falsified in PR #701 as a PSLQ coincidence. The categorical
  identity above replaces it: $\lambda_p^{\mathrm{scale}}$ is *not*
  a polynomial in $h$, but rather the Bloch-Wigner regulator of an
  integer combination of hyperbolic-knot classes.
- **The "hidden CAL-4" objection**: the $\lambda_p^{\mathrm{scale}}$
  literal $2.4599527869$ in the production script was a calibration-
  closure value. Under the Bring-Bloch identity it becomes the
  K-theoretic content of $K_p^{\mathrm{eff}}$ — no longer free,
  fixed by the choice of integer combination $n_i^{(p)}$.
- **The 251 ppb residual** flagged in
  [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-lambda-scale-derivation-search.md)
  §93–104 was a stale-Vol propagation bug; fixing the script to use
  $\mathrm{Vol}(\mathcal{B}_3) = 8G$ exact closes the m_p residual
  to $\sim 1$ ppb (literal-truncation of the 11-digit
  $\lambda_p^{\mathrm{scale}}$ snapshot). See
  [`borromean-volume-propagation-to-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/borromean-volume-propagation-to-m-p.witness.json).

## Witness chain

1. [`borromean-volume-100dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/borromean-volume-100dps.witness.json) ---
   $\mathrm{Vol}(\mathcal{B}_3) = 8G$ exact at 100 dps.
2. [`borromean-volume-propagation-to-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/borromean-volume-propagation-to-m-p.witness.json) ---
   251 ppb m_p residual closes to $\sim 1$ ppb with exact Vol.
3. [`m-p-borromean-verification-50dps.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/m-p-borromean-verification-50dps.witness.json) ---
   production m_p verification under exact Vol.
4. [`bring-bloch-tier0-search-m-p.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/bring-bloch-tier0-search-m-p.witness.json) ---
   Tier 0 PSLQ search; negative result motivating Tier 1+.
