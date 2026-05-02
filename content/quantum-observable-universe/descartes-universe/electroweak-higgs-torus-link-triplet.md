**Conjecture (electroweak/Higgs torus-link triplet).**
*The standard-model electroweak gauge bosons $W^\pm, Z$ and the
Higgs scalar $H$ are identified, in any QOU built on
([Bring's surface](#def:brings-surface)) with EM/strong sector
$\{T_{2,9}, T_{3,5}\}$
([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)),
with the **non-Bring even-twist 2-component torus-link triplet***

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

*Each link has braid presentation $\sigma_1^{2k}$ in $B_2$ for
$k = 2, 3, 4$ respectively; their Seifert-surface genera are
$1, 2, 3$ — exactly the genera **not** occupied by the Bring-
saturating force-carrier sector (which lives at genus $4$).*

**Where this conjecture comes from.**

A research-grade audit of the framework's torus-knot inventory
([NV-1 / FROB-FILTER conjectures, 2026-05-02](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-02-nv-frob-filter-conjectures.md))
established that:

1. **Bring's genus-$4$ capacity is saturated** by
   $\{T_{2,9}, T_{3,5}\}$ — the only two coprime solutions of
   $(p-1)(q-1) = 8$. No additional torus knots can embed at
   genus $\leq 4$ on Bring as saturating generators.
2. The weak-scale crossing count $N_v$ in the Fermi-constant
   decomposition $G_F = 1/(\sqrt{2}v^2)$, $v = N_v\,E_\times\,\mu_0$
   currently has no categorical derivation; closing this gap (the
   **NV-1** audit flag) requires identifying $W^\pm, Z$ as specific
   knots/links.
3. An exploratory SDP-feasibility probe
   ([`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/ew-higgs-sdp-probe.witness.json))
   on three candidate identification paths returned a **clean PSD
   discrimination**: only the non-Bring even-twist torus-link
   triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced
   positive-semidefinite Hecke certificates on every Wedderburn
   block. The two competing paths — $T_{3,5}$ as unified weak
   triplet (Bring-internal), and non-torus knots ($4_1$ for
   Higgs, $5_2$ for $Z$, $3_1$ for $W$) — all failed PSD on the
   standard $(2,1)$ representation.

**Decisive structural argument: even-twist parity.**

The $T(2, 2k)$ braid is $\sigma_1^{2k} \in B_2$. The Hecke
algebra $H_2(q)$ has Wedderburn decomposition $H_2(q) \cong
\mathbb{Q}(q) \oplus \mathbb{Q}(q)$ with the two block projectors
sym + alt, and $\sigma_1$ acts as $q$ on sym and $-q^{-1}$ on alt.
Hence $\sigma_1^{2k}$ has block eigenvalues

$$
  \mathrm{sym}\colon\; q^{2k} > 0,
  \qquad
  \mathrm{alt}\colon\; (-q^{-1})^{2k} = q^{-2k} > 0.
$$

**Both eigenvalues are strictly positive** for any $k \geq 1$ —
the even power kills the sign-flip. By contrast, $\sigma_1^{2k+1}$
(odd-twist) has alt eigenvalue $-q^{-(2k+1)} < 0$ and is **never**
PSD-feasible. So **even-twist is the unique parity** at which a
2-component torus link supports a positive-definite Frobenius
form.

This is the proposition `prop:even-twist-torus-link-psd-feasibility`
(below) that *is* a derivable proposition — it follows mechanically
from the Hecke relation. The conjecture sits at the next layer:
*which* even-twist links carry $W^\pm, Z, H$.

**Why genera 1, 2, 3 specifically.**

The genera of the 2-component torus links $T(2, 2k)$ form an
arithmetic progression $g(T(2, 2k)) = k - 1$ (Seifert genus of the
canonical Seifert surface). Bring's saturating force-carriers
occupy genus $4$ exclusively. The non-Bring **complement** thus has
genera $\{1, 2, 3\}$ available for 2-component torus-link
identifications, occupied by $T(2, 4), T(2, 6), T(2, 8)$.

The **mass ordering** of the standard model
$m_{W^\pm}\;{<}\;m_Z\;{<}\;m_H$
($80.4 \;{<}\; 91.2 \;{<}\; 125.3$ GeV in CODATA / PDG) maps
monotonically onto the crossing-number ordering $4 < 6 < 8$ — a
necessary but not sufficient consistency check.

**What the conjecture closes.**

If true, the conjecture supplies the missing categorical structure
for the **NV-1** audit flag (the weak-scale crossing count). With
$W^\pm, Z, H$ identified as $T(2,4), T(2,6), T(2,8)$, the parallel
of the $1/\alpha_{EM}$ derivation
([`prop:alpha-em-categorical-trace`](#prop:alpha-em-categorical-trace))
becomes available for $G_F$:

| Step in the parallel pipeline | EM analog | EW/Higgs analog |
|---|---|---|
| Strand count | 10 (Bring exterior square $\Lambda^2 V^{10}$) | 2 (each $T(2, 2k)$ is in $B_2$) |
| Force-carrier sector | $\{T_{2,9}, T_{3,5}\}$ | $\{T(2,4), T(2,6), T(2,8)\}$ |
| Categorical complexity | $[9]_q \cdot [10]_q$ | $[4]_q \cdot [6]_q \cdot [8]_q$ |
| Spectral completeness | `thm:em-spectral-completeness` | open: `prop:weak-spectral-completeness` |
| Plancherel weight | gram-determinant ratio | open |
| Closed form | $1/\alpha = 45[3]_q(1 + \delta_{CS} + 8q\delta_{CS}^2)$ | open: $N_v = ?$ |

Closing the open rows above is the explicit research program
unlocked by this conjecture.

**Status.** Open. The PSD-feasibility evidence is **necessary but
not sufficient** for uniqueness. PSD-feasibility holds for *every*
even-twist $T(2, 2k)$ at any $k \geq 1$ (proposition below), so the
SDP probe alone cannot select the specific triplet $\{T(2,4), T(2,6),
T(2,8)\}$ from the infinite family. **Full uniqueness factorises
into five sub-arguments**, only some of which are derivable
from the existing framework:

| # | Sub-argument | Derivability | Status |
|---|--------------|-------------:|--------|
| **U1** | Even-twist parity (forces $\sigma_1^{2k}$ over $\sigma_1^{2k+1}$) | derivable from Hecke positivity | ✓ proven below as the proposition |
| **U2** | Force-carriers are 2-component **links**, not knots | structural premise (matter = knots, force = links) | needs content support — currently a structural choice |
| **U3** | Non-Bring genus $\leq 3$ | corollary of `prop:force-carrier-bring-uniqueness` | ✓ Bring saturates genus 4 |
| **U4** | Exactly **three** force-carrier slots in the EW/Higgs sector | from representation theory of broken $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (3 mass eigenstates after Higgs eating Goldstones) | needs content block — open |
| **U5** | Mass ordering $m_W < m_Z < m_H$ matches crossing ordering $4 < 6 < 8$ | empirical / consistency | ✓ matches PDG |

The conjecture as stated **rides on U2 + U4**. Closing each:

- **U2** would be discharged by a content block characterising
  *force-carrier* objects categorically (e.g., as morphisms in
  $\mathbf{C}$ rather than objects, or as elements of $\mathrm{End}_R$
  rather than $\mathrm{Hom}(\mathbf{1}, A)$). The matter-vs-force
  distinction is implicit in the existing framework but not codified
  as a proposition.
- **U4** would be discharged by a representation-theoretic
  proposition counting the EW mass eigenstates: the broken
  $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ has $3 + 1 = 4$ gauge
  generators, the Higgs mechanism eats $3$ Goldstones via the
  longitudinal modes of $W^\pm, Z$, leaving $4 - 3 = 1$ scalar plus
  $3$ massive vectors with $W^\pm$ mass-degenerate, hence $3$
  distinct masses. This is standard EW theory, but to enter the
  QOU framework as a derivable proposition it must be cast in
  $\mathbf{C}$ as a count of irreducible Wedderburn channels
  surviving the Higgs idempotent.

**Uniqueness analysis at $q_0$ (probe table for $T(2, 2k)$,
$k = 1..7$):**

| $k$ | link | genus | crossings | sym = $q^{2k}$ | alt = $q^{-2k}$ | PSD? | role |
|----:|-----:|------:|----------:|---------------:|----------------:|:---:|-----|
| 1 | $T(2,2)$ | 0 | 2 | 1.231 | 0.812 | ✓ | **Hopf link** $L_H$ (binding link, *not* a force-carrier) |
| 2 | $T(2,4)$ | 1 | 4 | 1.516 | 0.659 | ✓ | $W^\pm$ |
| 3 | $T(2,6)$ | 2 | 6 | 1.867 | 0.535 | ✓ | $Z$ |
| 4 | $T(2,8)$ | 3 | 8 | 2.300 | 0.435 | ✓ | $H$ |
| 5 | $T(2,10)$ | 4 | 10 | 2.832 | 0.353 | ✓ | (no SM particle) |
| 6 | $T(2,12)$ | 5 | 12 | 3.487 | 0.287 | ✓ | (no SM particle) |
| 7 | $T(2,14)$ | 6 | 14 | 4.294 | 0.233 | ✓ | (no SM particle) |

*Every* row PSD-passes. The selection of rows 2–4 over rows 1, 5, 6, 7
comes from U2–U5, **not** from PSD.

**To promote to a `proposition`, one path:**

1. Author the open content blocks for U2 and U4 (currently
   structural premises).
2. Provide a PSLQ uniqueness witness at $\geq 1000$-dps confirming
   that $N_v$ has a unique short closed form in
   $\{q^k, [k]_q, \hbar_q^k\}$ when the $T(2, 4), T(2, 6), T(2, 8)$
   basis is added.

Together these would discharge the conjecture into a derivable
proposition. Until both are available, the identification is
*structurally consistent* but not *categorically unique*.

**Witness.**
[`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/ew-higgs-sdp-probe.witness.json)
— PSD-feasibility certificates for the three candidate paths
(α non-Bring even-twist; β $T_{3,5}$ double-duty; γ non-torus
knots). Path α passes every block; β and γ fail the standard
$(2,1)$ block.

---

**Proposition (even-twist 2-component torus links are
PSD-feasible).**
*For every $k \geq 1$, the braid $\sigma_1^{2k} \in B_2$ acts
on the Hecke algebra $H_2(q)$ with both Wedderburn-block
eigenvalues strictly positive at any real $q > 0$:*

$$
  \mathrm{sym\text{-}eigenvalue}(\sigma_1^{2k}) = q^{2k} > 0,
  \qquad
  \mathrm{alt\text{-}eigenvalue}(\sigma_1^{2k}) = q^{-2k} > 0.
$$

*Conversely, for every $k \geq 0$, $\sigma_1^{2k+1}$ has
$\mathrm{alt\text{-}eigenvalue} = -q^{-(2k+1)} < 0$, hence is
**never** PSD-feasible.*

*Proof.* Direct from the Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ specialised to $i = 1$ in
$B_2$: $\sigma_1 = q$ on sym, $\sigma_1 = -q^{-1}$ on alt
([Hecke-Skein convention](#prop:hecke-skein-convention) §7a of
CLAUDE.md). Composition with itself $2k$ times preserves the sign
on sym and squares the sign on alt, giving $(-q^{-1})^{2k} =
q^{-2k} > 0$. Odd powers retain the negative sign on alt.
$\square$

This proposition is the **even-twist parity selection rule**.
Together with the structural input that force-carrier links are
2-component torus links of $H_1(\Sigma_{\text{host}}, \mathbb{Z})$,
it *forces* the parity to be even.
