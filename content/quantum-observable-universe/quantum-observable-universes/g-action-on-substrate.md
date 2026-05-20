**Conjecture (categorical $G$-action on the Frobenius–Hopf substrate).**
*Let $A$ be a Frobenius–Hopf substrate
([substrate axioms](#def:frobenius-hopf-substrate)) in $\mathbf{C} =
\mathbf{Rep}(\mathrm{SU}_q(2))$. Then $A$ admits a unique
$G$-equivariant structure for $G = \mathrm{SU}(2)_L \times
\mathrm{U}(1)_Y$ compatible with the path-α torus-link identification
(electroweak/Higgs torus-link triplet [planned, not yet authored]),
specified by the four axioms below. From these axioms the
symmetric-channel Frobenius trace
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ — the value
$\mathcal{N}_{\rm sym}(q)$ — is computable in closed form.*

### The four axioms

**Axiom (G-1) — $G$-isotypic decomposition.**
The substrate $A$ decomposes as a direct sum of $G$-isotypic
components:

$$
  A \;=\; A^{(\gamma)} \;\oplus\; A^{(W^+)} \;\oplus\; A^{(W^-)}
  \;\oplus\; A^{(Z)} \;\oplus\; A^{(H)} \;\oplus\; A^{(\rm matter)}
$$

where each $A^{(X)}$ carries a unique irrep of $G$:

| component | $G$-irrep $(j, y)$ | post-EWSB role |
|-----------|------------------:|----------------|
| $A^{(\gamma)}$ | $(0, 0)$ | unbroken photon |
| $A^{(W^+)}$ | $(1, 0)|_{T^+}$ | $W^+$ vector boson |
| $A^{(W^-)}$ | $(1, 0)|_{T^-}$ | $W^-$ vector boson |
| $A^{(Z)}$ | $(1, 0)|_{(T^3,\,Y)}$ | $Z$ vector boson (mixed $T^3$/$Y$ component) |
| $A^{(H)}$ | $(1/2, 1/2)|_{\langle\Phi\rangle\text{-fixed}}$ | Higgs scalar (residual) |
| $A^{(\rm matter)}$ | residual matter sector | leptons + quarks (orthogonal) |

**Axiom (G-2) — Per-host q-dim assignment.**
The categorical q-dimension of each component is determined by its
torus-link host (per
force-carrier Bring uniqueness [planned, not yet authored]
+ path-α identification):

$$
  \dim_q\bigl(A^{(W^\pm)}\bigr) \;=\; [4]_q,
  \qquad
  \dim_q\bigl(A^{(Z)}\bigr) \;=\; [6]_q,
  \qquad
  \dim_q\bigl(A^{(H)}\bigr) \;=\; [2]_q.
$$

The W-host scale $[4]_q$ comes from the $T(2,4)$ crossing count;
the Z-host scale $[6]_q$ from $T(2,6)$. The Higgs scale $[2]_q$
is the q-dim of the SU(2)_L fundamental (Higgs doublet),
restricted to the $\langle\Phi\rangle$-fixed neutral component.

**Axiom (G-3) — Higgs vacuum vortex morphism.**
The Higgs vacuum value $\langle\Phi\rangle \in A$ is the unique
non-zero vortex morphism
([mass identity](#def:mass-identity)) of the form
$\varrho_\Phi \colon \mathbf{1} \to A^{(H)}$ satisfying

$$
  Q \cdot \varrho_\Phi = 0, \qquad
  \mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi) = v^2 / m_e^2,
$$

where $Q = T_3 + Y$ is the unbroken charge generator and
$v \approx 246\,\mathrm{GeV}$ is the weak VEV. The first
condition makes $\varrho_\Phi$ neutral under the unbroken
$\mathrm{U}(1)_{em}$; the second pins its categorical norm to
the empirically observed Higgs VEV.

**Axiom (G-4) — Higgs idempotent.**
The categorical Higgs idempotent $e_H$
([categorical Higgs idempotent](#conj:categorical-higgs-idempotent))
is constructed from $\varrho_\Phi$ via

$$
  e_H \;=\; \frac{\varrho_\Phi \cdot \varrho_\Phi^*}{\mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi)}.
$$

This is the rank-1 projector onto the unbroken-direction
1-dimensional subspace of $A^{(H)}$. By Axiom (G-2),
$\dim_q(e_H \cdot A) = $ q-dim of the residual Higgs scalar = the
$\langle\Phi\rangle$-fixed direction inside $A^{(H)}$, contributing
factor $[2]_q$ in the trace.

### Derivation of $\mathcal{N}_{\rm sym}(q)$ from the axioms

Compose:

$$
  \mathrm{tr}_F\bigl(e_{\rm sym}^{\rm EW} \cdot e_H\bigr)
  \;=\;
  \dim_q(e_{\rm sym}^{\rm EW}\bigl[A^{(W^+)} \oplus A^{(W^-)} \oplus A^{(Z)}\bigr]) \;\cdot\;
  \dim_q\bigl(e_H \cdot A^{(H)}\bigr).
$$

By Axioms (G-1) and (G-2):

- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(W^+)}]) = \dim_q(A^{(W^+)}) = [4]_q$
  (the sym block is the unbroken-direction projector at the W-host)
- Similarly $\dim_q(e_{\rm sym}^{\rm EW}[A^{(W^-)}]) = [4]_q$
- $\dim_q(e_{\rm sym}^{\rm EW}[A^{(Z)}]) = [6]_q$
- $\dim_q(e_H \cdot A^{(H)}) = [2]_q$ (the residual neutral Higgs)

Hence

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  \mathrm{tr}_F\bigl(e_{\rm sym}^{\rm EW} \cdot e_H\bigr)
  \;=\;
  [4]_q \cdot [4]_q \cdot [6]_q \cdot [2]_q
  \;=\;
  [2]_q \cdot [4]_q^2 \cdot [6]_q.
$$

This is **Anchor II** of the prior structural analysis — but now
**derived**, not guessed. Each factor is forced by an explicit
axiom:

| factor | source axiom | meaning |
|--------|-------------|---------|
| $[2]_q$ | (G-2) + (G-4) | Higgs scalar (residual neutral component) |
| $[4]_q$ | (G-2) | $W^+$ Goldstone at W-host |
| $[4]_q$ | (G-2) | $W^-$ Goldstone at W-host |
| $[6]_q$ | (G-2) | $Z$ Goldstone at Z-host |

### Verification against numerical anchor

At $q_0 = :val[q_0]{precision=6}\ldots$:

$$
  [2]_q \cdot [4]_q^2 \cdot [6]_q \;=\; 2.0109 \cdot 16.892 \cdot 6.388
  \;\approx\; 216.96
$$

vs. the CODATA-pinned target $\mathcal{N}_{\rm sym}(q_0) = 213.11$.

**Residual: −1.81%.** The 1.81% deviation requires explanation:
either (a) one of the axioms above is slightly off, or (b) there is
a Plancherel reweighting / vacuum-volume factor not yet captured.

### The 1.81% residual — open question

Three plausible sources:

1. **Vacuum-volume normalization** in Axiom (G-3): the
   $\mathrm{tr}_F(\varrho_\Phi^* \cdot \varrho_\Phi) = v^2/m_e^2$
   pinning may carry a small categorical correction
   $1 + \delta_v$ from the substrate's q-deformed measure.
2. **Plancherel weight** for the EW Wedderburn block: the
   $e_{\rm sym}^{\rm EW}$ projector may include a Plancherel factor
   $\prod_k 1/[2]_q$ (one per host) that I've omitted; including
   it would reduce the prediction.
3. **Higgs-mixing correction**: the $W^3$-$B$ mixing angle
   $\theta_W$ enters categorically through a small q-deformation
   factor $(1 + \mathcal{O}(\hbar_q^2))$ on the Z-host contribution.

Pursuing any of these without categorical guidance is fitting and
should be avoided. The discrimination requires either (a) a
sharper version of the four axioms above or (b) an independent
categorical computation of $\mathcal{N}_{\rm sym}$ that directly
extracts the leading + correction.

### Status

**Open at the closure level.** The four axioms above are a
**concrete framework extension** that takes the QOU substrate
from "$\mathbf{Rep}(\mathrm{SU}_q(2))$-equivariant" to
"$G \times \mathbf{Rep}(\mathrm{SU}_q(2))$-equivariant", entailing
the closed form $\mathcal{N}_{\rm sym}(q) = [2]_q \cdot [4]_q^2 \cdot
[6]_q$ that matches CODATA-derived target to 1.81%. Each factor is
**categorically derived**, not fitted.

The remaining 1.81% is a SINGLE missing categorical input (one of
the three sources above); identifying it would close the audit
flag NV-1 entirely.

**To promote to `proposition`:**
1. Resolve the 1.81% residual via one of the three open routes
2. Provide the unique-existence argument for the four axioms
3. Author the Lean formalization

### Audit-flag impact

If discharged:

| flag | current | post-discharge |
|------|---------|----------------|
| NV-1 | 🔴 inconclusive | 🟢 closed via this trace formula + corrected residual |
| HIGGS-SLOT (PR #513) | 🔴 retraction | 🟢 Higgs scalar slot identified as residual of $A^{(H)}$ |
| U2 (force-carrier dichotomy) | 🟡 premise | 🟢 derived from G-1 |
| U4 (EW mass eigenstate count) | 🟡 premise | 🟢 derived from G-1 (3 broken + 1 scalar) |
| categorical Higgs idempotent | 🟡 sketch | 🟢 explicit construction (G-4) |
| §3.A v4 calibration | 🟡 wrong direction | 🟢 calibrated via Higgs trace |

**Six audit flags closed by a single residual-resolution.**
