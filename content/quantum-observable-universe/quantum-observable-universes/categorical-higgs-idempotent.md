**Conjecture (categorical Higgs idempotent).**
*Let $A$ be a Frobenius–Hopf substrate
([substrate axioms](#def:frobenius-hopf-substrate)) carrying a
$G$-action with $G = \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$, and
let $\Phi \in V_{1/2, 1/2}$ be a Higgs doublet (spin-$1/2$ of
$\mathrm{SU}(2)_L$ with hypercharge $Y = 1/2$). The vacuum value
$\langle\Phi\rangle = (0, v/\sqrt{2})^\top$ defines a **categorical
Higgs idempotent**:*

$$
  e_H \;\colon\; A \;\longrightarrow\; A,
  \qquad
  e_H \;=\; \mathrm{ev}_A \circ \bigl(\mathrm{id}_{A^\vee} \otimes
  P_{T_3 + Y}\bigr) \circ \mathrm{coev}_A,
$$

*where $P_{T_3 + Y}$ is the projector onto the unbroken
$\mathrm{U}(1)_{em}$ generator $Q = T_3 + Y$. Equivalently:
$e_H = \mathrm{tr}_{\mathbf{C}}(P_{T_3 + Y})$ in the categorical
trace sense
([categorical action](#def:categorical-action)).*

### Statement

The pre-EWSB action of $G$ on $A$ decomposes the substrate
endomorphism algebra into 4 generator blocks:

$$
  \mathrm{End}(A)|_{G}
  \;=\;
  \mathrm{End}(A)|_{T^1} \oplus
  \mathrm{End}(A)|_{T^2} \oplus
  \mathrm{End}(A)|_{T^3} \oplus
  \mathrm{End}(A)|_{Y}.
$$

After EWSB, $G$ breaks to $H = \mathrm{U}(1)_{em}$ (1-dim) along
the direction $T_3 + Y$. The **categorical Higgs idempotent** $e_H$
is the projector onto this unbroken direction:

- $e_H \cdot \mathrm{End}(A)|_{T^3 + Y} = \mathrm{End}(A)|_{T^3 + Y}$
  (eigenvalue $1$);
- $e_H \cdot \mathrm{End}(A)|_{T^a} = 0$ for $a \in \{1, 2,
  T^3 - Y\}$ (eigenvalue $0$).

Hence $1 - e_H$ projects onto the **3-dimensional broken-direction
subspace**, where the 3 Goldstones live before they are eaten by
$W^\pm, Z$ longitudinal modes
(electroweak mass eigenstate count [planned, not yet authored]).

### What this conjecture closes

This single artifact unlocks **four** downstream open problems:

1. **NV-1 closed form via candidate (b)**:
   $\mathcal{N}_{\rm sym}(q)$
   (N_sym [planned, not yet authored]) is
   computed as the Frobenius trace of the symmetric-channel
   projector
   $$
     \mathcal{N}_{\rm sym}(q) \;=\;
     \mathrm{tr}_F\bigl( e_{\rm sym}^{\rm EW} \cdot e_H \bigr),
   $$
   where $e_{\rm sym}^{\rm EW} = \bigotimes_{k=2,3,4} e_{\rm sym}^{(T(2,2k))}$
   is the EW symmetric-channel projector
   (weak spectral completeness [planned, not yet authored]).
   The closed form falls out of the categorical Higgs idempotent
   composition without ansatz-fitting.

2. **U2 (force-carrier knot/link dichotomy)**: the broken-direction
   subspace $(1 - e_H) \cdot \mathrm{End}(A) \cdot (1 - e_H)$ is
   3-dimensional, matching the 3 broken gauge generators that
   couple to 2-component links. The 1-dimensional unbroken
   direction $e_H \cdot \mathrm{End}(A) \cdot e_H$ couples to the
   1-component knot (the photon in the EM sector)
   (force-carrier knot/link dichotomy [planned, not yet authored]).

3. **U4 (electroweak mass-eigenstate count)**: the 3 distinct
   masses $\{m_W, m_Z, m_H\}$ are the 3 distinct eigenvalues of
   the mass operator on $(1 - e_H) \cdot \mathrm{End}(A) \cdot
   (1 - e_H)$
   (EW mass eigenstate count [planned, not yet authored]).

4. **HIGGS-SLOT** (PR #513/#514): the Higgs scalar lives on the
   single residual direction in $(1 - e_H) \cdot \mathrm{End}(A) \cdot
   (1 - e_H)$ orthogonal to the 3 broken-gauge directions — a
   **scalar slot** distinct from the W±, Z vector slots. This
   resolves the −11.4% deficit found by PR #513 testing
   $m_H \propto \mathrm{tr}_M(T(2,8))$: the Higgs scalar is NOT
   a torus link in the same family as W±, Z; its categorical
   slot is the residual scalar of the symmetry-broken doublet.

### Construction sketch

Working in $\mathbf{Rep}(G) = \mathbf{Rep}(\mathrm{SU}(2)_L \times
\mathrm{U}(1)_Y)$, the Higgs doublet decomposes as

$$
  V_{1/2, 1/2} \;=\; V_{T_3 + Y = +1} \oplus V_{T_3 + Y = 0}
$$

where the first summand has $Q = +1$ (charged Higgs) and the
second has $Q = 0$ (neutral Higgs). The vacuum value
$\langle\Phi\rangle$ singles out the neutral $Q = 0$ direction.
The unbroken $\mathrm{U}(1)_{em}$ acts trivially on
$\langle\Phi\rangle$, so the projector

$$
  e_H \;=\; |\langle\Phi\rangle\rangle\langle\langle\Phi\rangle|
  \;=\;
  \frac{1}{|\langle\Phi\rangle|^2}\,
  \langle\Phi\rangle \otimes \langle\Phi\rangle^*
$$

is the categorical analog of the $|0\rangle\langle 0|$ vacuum
projector of standard QFT. Lifted to the substrate $A$ via the
$G$-equivariant action, $e_H$ becomes an endomorphism $A \to A$
satisfying $e_H^2 = e_H$ (idempotent) with $\mathrm{tr}(e_H) = 1$
(unbroken-direction count).

### Status

🟡 **Open**. The construction sketch above is a categorical
*translation* of standard QFT Higgs mechanics; converting it to
a derivation rigorous enough to *compute*
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ at $q_0$ requires:

1. Explicit construction of $G$-action on the
   [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) at
   the categorical level (currently axiomatic).
2. Concrete identification of $\langle\Phi\rangle$ as a specific
   morphism $\mathbf{1} \to A$ (vortex morphism per
   [mass identity](#def:mass-identity)).
3. Composition with the EW symmetric-channel projector
   $e_{\rm sym}^{\rm EW}$ + Frobenius trace evaluation.

**Empirical anchor for verification**: when the derivation is
complete, $\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$
evaluated at $q_0 = 1.10998\ldots$ MUST equal
$\mathcal{N}_{\rm sym}(q_0) = 213.111807\ldots$ (the value pinned
by CODATA $G_F$ via the
conjectured product structure [planned, not yet authored]).
The closeness of empirical zero-free-parameter forms
(e.g. $[3]_q \cdot [4]_q^3$ at 0.87%) provides anchor structure
but is *not* a substitute for derivation.

### Impact if discharged

| audit flag | current status | post-discharge status |
|------------|----------------|----------------------|
| NV-1 | 🔴 inconclusive | 🟢 closed via Higgs trace |
| HIGGS-SLOT (PR #513) | 🔴 retraction recommended | 🟢 scalar slot identified |
| U2 (force-carrier dichotomy) | 🟡 structural premise | 🟢 derived |
| U4 (EW mass eigenstate count) | 🟡 structural premise | 🟢 derived |
| §3·A v4 calibration scale | 🟡 wrong direction | 🟢 calibrated to N_sym |
| SHELL-7 reweighting | 🔴 falsified | 🟡 reformulation possible with κ=0 stratum + Higgs-eaten weights |

**Six audit flags affected by a single derivation.** This is the
highest-leverage open problem in the post-PR #515 audit landscape.
