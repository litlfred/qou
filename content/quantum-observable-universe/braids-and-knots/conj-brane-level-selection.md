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

## Proof obligations

1. Show that $n_\star = \ell \cdot n_0 + k$ reproduces the empirical
   binding energies of $\{D, T, {}^3\mathrm{He}\}$ to within $5\%$
   **without per-atom retuning** when substituted into the $z$-Habiro
   cyclotomic projection $\pi_{n_\star}^{(z)}$.

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

