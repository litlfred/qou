**Proposition (transport sketch).**
*Let $\rho_{\infty} : \widehat{\mathbb{Z}[q]} \to \mathbb{R}$
denote the archimedean realization functor
([archimedean realization](#def:archimedean-realization-functor)).
On molecular-binding $\Phi_{1}$ outputs, $\rho_{\infty}$ acts as*

$$
  \boxed{\;\;
    \rho_{\infty}\bigl(\Phi_{1}(\mathcal{M})\bigr)
    \;=\;
    \Phi_{1}(\mathcal{M})
    \cdot
    \underbrace{m_e c^{2}\,\alpha_{EM}^{2}}_{E_{\mathrm{Hartree}}}
    \cdot
    \underbrace{(q + q^{-1})^{-2}}_{\text{molecular factor}}
  \;\;}
$$

*with the leading factor $E_{\mathrm{Hartree}} = m_e c^{2}\,\alpha_{EM}^{2}$
the Hartree energy.*

> ### Caveat — derivation status
>
> This proposition **is not derived from QOU/Hecke structure
> alone**. The two factors of $\alpha_{EM}$ are argued by
> chaining through
> [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical),
> which itself transports the standard QED virial-balance
> argument. The asserted "uniqueness" of the archimedean energy
> unit reduces to "matches QED in $q \to 1$ limit" — empirical
> consistency with standard physics, *not* a fully internal QOU
> derivation.
>
> The numerical match $0.687 \times 6.750 = 4.638$ eV with the
> H_2 binding witness ([`computations/h2-molecular-binding.witness.json`](computations/h2-molecular-binding.witness.json))
> is **internal-consistency arithmetic**, not a verification: the
> LP outputs the dimensionless 0.687, the Python multiplies by a
> hardcoded conversion factor involving $\alpha^2$
> ([`hecke_core.py:198`](computations/hecke_core.py)),
> and the arithmetic produces 4.638 eV. *Any* framework using
> $E_h \sim m_e c^{2}\,\alpha^{2}$ as the unit would match
> within $\sim 10\%$ of the experimental 4.476 eV — that's just
> standard physics.
>
> The proposition is recorded with this caveat to preserve the
> structural mapping while being honest that closure remains open.
> Companion to
> [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical),
> which carries the same caveat.

### Numerical breakdown (informational)

At $q_{0} \approx 1.1097$:

| Quantity | Symbolic | Numerical |
|---|---|---:|
| $\alpha_{EM}$ | $1/(q\,[9]_q\,[10]_q)$ | $0.007309$ |
| $\alpha_{EM}^{2}$ | — | $5.34 \times 10^{-5}$ |
| $m_{e}c^{2}$ | (input) | $511\,000$ eV |
| $E_{\mathrm{Hartree}}$ | $m_{e}c^{2}\,\alpha_{EM}^{2}$ | $27.296\,\mathrm{eV}$ |
| $TWO\_Q^{2}$ | $(q+q^{-1})^{2}$ | $4.044$ |
| $E_{\mathrm{MOL}}$ | $E_{\mathrm{Hartree}}/TWO\_Q^{2}$ | $6.750\,\mathrm{eV}$ |
| $\Phi_{1}^{H_{2}}$ binding diff | LP dual output | $0.687$ |
| $E_{\mathrm{bind}}^{H_{2}}$ | $\rho_{\infty}(\Phi_{1})$ | $4.638\,\mathrm{eV}$ |
| Experiment $D_{0}(H_{2})$ | — | $4.476\,\mathrm{eV}$ (3.6% off) |

These numbers are *internally consistent* with the proposition,
not independent verification of it.

### What is rigorous (and what is not)

**Rigorous:**
- $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$ from the EM
  force-carrier's operator-selection LP weight
  ([`prop:em-coupling-projection`](#prop:em-coupling-projection)).
- The molecular Markov-trace dimensionless output 0.687 from the
  H_2 LP/SDP optimum
  ([`prop:h2-lp-dual-binding`](#prop:h2-lp-dual-binding)).
- The molecular per-strand factor $(q + q^{-1})^{-2}$ for
  4-strand diatomic braids.

**Transported / postulated (not derived):**
- The choice $E_{\mathrm{nat}} = m_e c^{2}\,\alpha_{EM}^{2}$
  rather than $m_e c^{2}\,\alpha_{EM}$ or $m_e c^{2}$ as the
  natural energy unit per $\Phi_{1}$. The α-power is fixed by
  appealing to the Bohr-virial picture (transported via
  [`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical)).
- The "uniqueness" of $\rho_{\infty}$ — argued at the level of
  matching the standard QED limit at $q \to 1$.
- The hardcoded `E_HARTREE_EV = 511000 * alpha_em**2` in
  [`hecke_core.py:198`](computations/hecke_core.py)
  as the implementation of $\rho_{\infty}$.

### Five candidate routes for genuine categorical closure

Closing this proposition rigorously requires deriving the
$\alpha_{EM}^{2}$ factor of $E_{\mathrm{Hartree}}$ from QOU
algebraic structure alone, without appealing to standard QED.
Five candidates (mirrored from the companion proposition's
[Option 4a-4e](#prop:bohr-radius-categorical) discussion, with
additional functorial-uniqueness considerations for the
archimedean side):

#### Option 4a — Symbolic-$q$ recompute of $\Phi_{1}^{H_2}(\pi^{*})$

Track the dressed-vs-bare crossing contributions through the
multiplicative transfer-matrix chain symbolically, identify which
monomials in the resulting $V_i(q)$ originate from each crossing
type, and check whether the natural prefactor of the bound-state
Markov trace is $\alpha_{EM}^{2}$ as a polynomial fact in $R$
(not just at $q_0$ numerically). If yes: the $\alpha^{2}$ factor
emerges from algebraic structure, closing the conjecture.

#### Option 4b — Spectral-gap balance from Hecke eigenvalues

Use the categorical spectral gaps
$\Delta_{\mathrm{kin}}(k) = (4k+2)\log q$,
$\Delta_{\mathrm{Coul}} = 2\log q$
as Hecke-algebraic quantities, and derive the natural energy
scale per $\Phi_{1}$ from their ratio at the bound state. The
$\alpha_{EM}^{2}$ would appear as a specific function of these
gaps and the operator-selection LP weights.

#### Option 4c — Length-graded Hecke functor

Introduce length grading on $H_n(q)$ axiomatically; the
archimedean functor $\rho_{\infty}$ becomes a length-graded map.
Force the natural energy per $\Phi_{1}$ at a given length to
match the LP-optimum length, derive the result.

#### Option 4d — GB spectral-sequence stratification

Apply the GB spectral sequence
([`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse))
to the molecular Markov trace; identify the curvature-rank-2
contribution (corresponding to two interacting force-carriers as
in a covalent bond) as the source of $\alpha_{EM}^{2}$. The
factor of 2 in the exponent comes from the rank-2 stratum.

#### Option 4e — Functorial uniqueness from $q \to 1$ smoothness

Prove a uniqueness lemma: any $q$-smooth functor
$\rho : \widehat{\mathbb{Z}[q]} \to \mathbb{R}$ satisfying
$\rho|_{q=1}$ = standard QED Hartree formula must be the unique
$\rho_{\infty}$ multiplying $\Phi_{1}$ by
$m_e c^{2}\,\alpha_{EM}^{2}$. Still appeals to standard QED at
$q = 1$, but reduces the empirical input from "match Hartree
formula globally" to "match Hartree formula at one point".

### Recommendation

**Option 4a is the most concrete next step.** A symbolic-$q$
recompute is computationally tractable and would either yield a
clean prefactor identification (closing the proposition) or
reveal a more complex polynomial structure (sharpening the gap).
Option 4d is the most QOU-native and would generalize beyond
H_2 to arbitrary covalent diatomics if successful.

Until either succeeds, this proposition remains a **transport
sketch**. The structural mapping it asserts is correct (consistent
with standard physics) and useful (defines the target for
categorical derivation), but it is not a closed theorem.

### Round-8 findings (cross-reference)

Direct attempts at options 4a, 4b, 4d on this proposition's
sibling
[`prop:bohr-radius-categorical`](#prop:bohr-radius-categorical)
yielded the following:

- **4a (yes) — partial.** $V_i$ for the H_2 optimal ordering
  decomposes additively into bare ($h_b$) and dressed ($h_d$)
  components: $V_H = z + h_b - h_d$, $V[1] = 1 + 2zh_b - zh_d$,
  $V[2] = z - h_b$. Cross-terms $h_b \cdot h_d$ cancel in the
  optimal-ordering chain.
- **4b (yes) — relative spacing recovered.** Categorical shell
  ratios $(2k+1)^{-2}$ match Bohr $1/n^2$ exactly with
  $n = 2k+1$. Pure Hecke, no transport.
- **4d partial.** Covalent rank-2 $\to$ $\alpha^2$ works for
  covalent binding but doesn't explain atomic $\alpha^2$ (single
  electron systems also at $\alpha^2$ but only one EM coupling).

**Implication for this proposition:** the $\alpha^2$ factor in
$\rho_\infty(\Phi_1) = \Phi_1 \cdot E_{\mathrm{Hartree}} \cdot (q+q^{-1})^{-2}$
is partially supported (covalent case via 4d, shell-spacing via
4b) but the **absolute scale** — the appearance of $m_e c^2$ as
the universal mass-energy unit — is not derived from Hecke
algebra in this round. Round-8 brings the conjecture closer to
closure but the universal-scale step still requires either:

1. **Option 4e (functorial uniqueness)** — prove a uniqueness
   lemma for $\rho_\infty$ via $q \to 1$ smoothness; reduces
   empirical input to "match standard QED at one point".
2. **Sharpening 4d** — extend curvature-rank $\to$ $\alpha$-power
   to atomic single-electron case; would require identifying the
   "second electron" categorical structure that gives the
   second factor of $\alpha$ in atomic binding (perhaps the
   Frobenius-pairing partner of the bound electron, or the
   virtual-pair vacuum polarization).

Net status after round 8: structural mapping is **partially
derived** from Hecke (relative shell spacing, additive
$h_b/h_d$ decomposition, covalent-bond rank-2 scaling) and
**partially transported** (universal $m_e c^2$ unit, atomic
$\alpha^2$ scaling).

### Round 9 — sharpened 4d: bound state ⟺ Hopf link ⟺ 2 crossings (WITHDRAWN in round 10)

> ### Caveat — Round 9 (withdrawn)
>
> The Hopf-link $\to$ 2-crossings $\to$ $\alpha^2$ argument presented
> below was **refuted in Round 10** (see
> [`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation)
> "Round 10 — LP-cost factorization REFUTED"). Direct computation
> gives $\mathrm{tr}_M(\sigma_1^2) = h\,z + 1 \approx 1.10$ at
> $q_0$ — i.e. $O(1)$, not $O(\alpha^2)$. The Hopf-link Hecke
> generators carry Markov weight $z$, not $\alpha_{EM}$, so the
> "each crossing $\to$ 1 $\alpha$ factor" mapping fails.
>
> The Round-9 argument is preserved here as an **investigation
> record**, not as an active closure route. Skip to Round 10
> (in the conjecture .md) for the refutation and to Round 11 for
> the q-dimension layer insight that supersedes it.

A unifying mechanism for *both* atomic and covalent
$\alpha^2$ scaling: **every bound state in QOU is a Hopf-linked
$(p, e)$ pair**, and the Hopf link's minimum crossing number is
**2** (classical knot theory: $\mathrm{cr}(\mathrm{Hopf}) = 2$).

| System | Hopf links | Min crossings | Predicted scaling |
|---|---|---:|---|
| Free $e^-$ + free $p$ | 0 | 0 | $\alpha^0$ (no binding) |
| Single H atom | 1 | 2 | $\alpha^2$ ✓ |
| H$_{2}$ molecule | 2 (one per atom) | 4 (per pair) | $\alpha^2$ $\times$ shell-factor ✓ |
| He atom | 1 (proton + 2 e) | $\geq 2$ | $\alpha^2$ $\times$ shell-factor ✓ |

**Categorical statement (sharpened 4d):**

> *Any bound state in QOU is realised as a Hopf-linked
> proton-electron pair (or aggregate). The Hopf link has minimum
> crossing number 2. Each crossing in the operator-selection LP
> contributes one factor of $\alpha_{EM}$ (the EM force-carrier
> weight). Therefore the binding energy of any bound state scales
> as $\alpha_{EM}^{2} \cdot m_e c^{2} \cdot (\text{shell factor})$.*

This explains atomic AND covalent $\alpha^2$ from a single
Hecke-algebraic structure: the Hopf link.

**What is now rigorous:**
- Hopf link minimum crossing number = 2 (classical knot theory).
- Single hydrogen atom = Hopf-linked $(p, e)$ pair (definitional
  in QOU; see [`def:atomic-braid`](#def:atomic-braid)).

**What remains the gap (round-9 sharpened):**
- The precise mechanism for "each LP-active Hecke crossing
  contributes exactly one $\alpha_{EM}$ factor". Looking at the
  operator-selection LP: $\alpha_{EM}$ is the LP weight of the
  *whole EM force-carrier knot* (the Bring complex), not a
  per-crossing factor. The translation from "per-knot weight" to
  "per-crossing factor" requires a multiplicative-decomposition
  lemma:
  $$
    \alpha_{\mathrm{Bring}}(\text{n-crossing braid})
    \;=\;
    \prod_{i=1}^{n} \alpha_{\mathrm{Bring,per-crossing}}.
  $$
  This is plausible (LP cost factorizes over independent
  crossings) but not yet proved.

**If this gap closes**, the conjecture is fully closed: every
bound-state binding energy scales as $\alpha^2 \cdot m_e c^2$
from the rank-2 Hopf-link structure, with the absolute $m_e c^2$
scale fixed by the trefoil-electron Markov-trace identification
(QOU's bare mass formula).

The round-9 sharpening reduces the conjecture's open question to:

> *Does the operator-selection LP cost of an n-crossing knot
> factorise multiplicatively as
> $\prod_i \alpha_{EM, i}$ over its $n$ crossings?*

This is a **concrete LP-structure question**, more tractable than
the original "$J^1$-vanishing" framing.

### Status

**Proposition with explicit caveat.** The archimedean functor
formula
$\rho_{\infty}(\Phi_{1}) = \Phi_{1} \cdot m_e c^{2}\,\alpha_{EM}^{2} \cdot (q+q^{-1})^{-2}$
is asserted as the structural mapping between QOU LP outputs and
physical eV values, with the explicit acknowledgement that the
$\alpha_{EM}^{2}$ factor is *not* derived from Hecke algebra
alone. Closure requires one of options 4a-4e.
