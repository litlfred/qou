The brane-tower regularization of the Habiro series
([conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro)) requires a
canonical level-selection rule $n_\star : \{\text{confined particles}\} \to \mathbb{N}$
derivable from the QOU substrate data alone.  Currently $n_\star$ is
chosen empirically for each particle class.  This conjecture proposes
a structural formula for $n_\star$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom
([confined particle](#def:confined-particle)) with confinement level
$\ell$ and strand count $n_0$.  Let $T_w \in H_{n_0}(q_0)$ be the
canonical Hecke element in GB normal form
([GB spectral sequence](#prop:gb-spectral-sequence)), and let
$k = \ell(w)$ be its Coxeter length (GB filtration grade).  Then the
canonical brane-tower truncation level is*

$$
  n_\star(\mathfrak{H}) \;=\; \ell \cdot n_0 + k,
$$

*where $\ell$ is the confinement level and $k$ is the GB filtration
grade of $T_w$.  Equivalently, $n_\star$ equals the total number of
elementary crossing insertions in the finite-slice Yekutieli picture.*

## Evidence from the uniform-$k$ sweep (2026-04-29)

The `brane-tower-z-habiro` conjecture documents a
**uniform-$k$ probe** over $\{D, T, {}^3\mathrm{He}\}$ at depths
$k \in \{1,2,3,4,5,6,8,10\}$.  Key observations:

1. **Sign-flip at $k = 2$.**  For all three atoms, the subtractive tower
   $\Delta\mathrm{tower}^{(k)}$ changes sign between $k = 1$
   (negative) and $k \geq 2$ (positive).  The depth $k = 2$ is the
   first depth that includes the **Hecke quadratic slice**
   ($\sigma_i^2 = (q-q^{-1})\sigma_i + 1$).  Under the proposed
   formula this corresponds to:

   | Particle | $\ell$ | $n_0 = 3A$ | $k_{\mathrm{Hecke}}$ | $n_\star = \ell n_0 + k$ |
   |----------|--------|------------|-----------------------|--------------------------|
   | Proton/neutron | $1$ | $3$ | $2$ | $5$ |
   | Electron | $0$ | $2$ | $2$ | $2$ |
   | Deuterium $^2$H | $2$ | $6$ | $2$ | $14$ |
   | Tritium $^3$H | $2$ | $9$ | $9$ | $27$ |
   | Helium-3 $^3$He | $2$ | $9$ | $2$ | $20$ |

   The $n_0 = 3A$ rule (atomic-braid strand count, three strands per
   nucleon) is the canonical definition per
   [`def:confined-particle`](#def:confined-particle) lines 26–28 and
   [`atomic-braid`](#def:atomic-braid) lines 2–4; the per-atom
   $k_{\mathrm{Hecke}}$ values come from
   `joint-tower-sdp-h6-h9.witness.json`.

2. **Structural motivation.**  The formula $n_\star = \ell \cdot n_0 + k$
   counts the total GB filtration depth across all confinement levels:
   at each of $\ell$ wrapping levels there are $n_0$ strand-insertions,
   and within the innermost Hecke algebra there are $k$ additional
   generators.  This is precisely the depth of the Yekutieli
   multiplicative integral on a $\ell$-level composition of branes.

3. **Non-uniform failure.**  Uniform $k$ (independent of $\mathfrak{H}$)
   never closes the residual for all three atoms simultaneously —
   confirming that $n_\star$ must depend on $\mathfrak{H}$ in a
   structural way.

## Empirical falsification (2026-05-09, proof obligation 1)

**The specific formula $n_\star = \ell \cdot n_0 + k$ is empirically
falsified at the predicted values $(n_\star^D, n_\star^T, n_\star^{{}^3\mathrm{He}}) = (14, 27, 20)$.**
The probe
[`probe_phiq_n_star_rule.py`](../../../computations/probe_phiq_n_star_rule.py)
(witness
[`probe-phiq-n-star-rule.witness.json`](../../../computations/probe-phiq-n-star-rule.witness.json))
substitutes these depths into the truncated quantum dilogarithm
$\Phi_q^{[\leq n_\star]}$ and finds that the brane-tower contribution
diverges by $\sim 10^5$–$10^7$%:

| Atom | $n_\star$ | $\mathrm{tower}^{({n_\star})}$ | $B^{\mathrm{abs}}$ (MeV) | $B^{\mathrm{AME}}$ (MeV) | err |
|------|-----------|--------------------------------|--------------------------|--------------------------|-----|
| $^2\mathrm{H}$ | $14$ | $1.92 \times 10^5$ | $9.8 \times 10^4$ | $2.225$ | $+4.4 \times 10^6$ % |
| $^3\mathrm{H}$ | $27$ | $1.29 \times 10^6$ | $1.32 \times 10^6$ | $8.482$ | $+1.6 \times 10^7$ % |
| $^3\mathrm{He}$ | $20$ | $9.23 \times 10^5$ | $9.43 \times 10^5$ | $7.718$ | $+1.2 \times 10^7$ % |

**Diagnosis.** The per-generator atomic-braid volumes
$|\hat{V}_i^{\mathrm{full}}|$ at $q_0$ sit at $\sim 0.99$, near the
$\Phi_q$ pole at $q^{-k} z = 1$.  Each additional truncation level
multiplies the result by $(1 - q^{-k}z)^{-1} \sim 10^{0.5}$ to
$10^1$; truncation depths $\geq 10$ blow up the tower beyond
physical scale.

**Compatible with the uniform-$k$ probe** in
[`brane-tower-z-habiro`](#conj:brane-tower-z-habiro), which already
reported $+775\%$ error at $k=1$ and $+1.27 \times 10^6\%$ at $k=10$
under uniform $k$.  The per-atom rule with $n_\star = (14, 27, 20)$
is even deeper, so the divergence is structurally consistent.

**Implications.**

- The specific formula $n_\star = \ell \cdot n_0 + k$ does not
  produce a regularized brane-tower contribution at the empirically
  required scale.  **Proof obligation 1 of this conjecture is now
  refuted at the proposed values.**
- The right $n_\star$ rule must give values of order $\leq 2$
  (since the sign-flip observation at $k=2$ in
  `brane-tower-z-habiro` is the *only* uniform-$k$ regime that comes
  close to the right magnitude).  A revised conjecture should
  consider:

  1. $n_\star$ depending only on the *Hecke* depth $k$ (not the
     atomic strand count $n_0$), or
  2. $n_\star = \ell \cdot k$ (drop $n_0$ entirely), giving
     $(n_\star^D, n_\star^T, n_\star^{{}^3\mathrm{He}}) = (4, 18, 4)$, or
  3. a fundamentally different regularization (Borel resummation,
     Habiro–Kontsevich integral) where the truncation depth is not
     the controlling parameter.

The conjecture's structural motivation (counting elementary
crossings in the Yekutieli multiplicative integral) survives, but
its quantitative content needs revision.

## Proof obligations

1. **(Refuted at $n_\star = \ell n_0 + k$, 2026-05-09.)** Show that
   *some* $n_\star$ rule derivable from substrate data reproduces
   the empirical binding energies of $\{D, T, {}^3\mathrm{He}\}$ to
   within $5\%$ **without per-atom retuning** when substituted into
   the $z$-Habiro cyclotomic projection $\pi_{n_\star}^{(z)}$.  The
   formula $\ell \cdot n_0 + k$ has been refuted; the obligation is
   now to find a correct alternate.

2. Derive $n_\star$ from the structure of the Yekutieli non-abelian
   Stokes theorem at $\ell$ nested slicing levels —  the formula
   should follow from counting elementary curvature insertions at all
   levels.

3. Explain the ${}^3$He overshoot: the doubled near-pole entry in
   ${}^3$He's generator volume list must either be absorbed by the
   formula or require a multiplicity correction.

## Relationship to GAP-A-3

This conjecture directly addresses GAP-A-3 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the empirical per-particle level-selection with
a structural formula derivable from the categorical data of
$(\mathbf{C}, \varTheta, G, \mathcal{S})$.

