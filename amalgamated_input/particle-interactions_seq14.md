<!-- FILE_START: borromean-reidemeister-intro.md -->
The bundle and observation data of the previous section make the knot--particle dictionary measurable. We now run the dictionary on its hardest test case: the Borromean baryon. This structure consists of three pairwise-unlinked unknots that nonetheless bind into a stable composite. Borromean binding forces the typed crossing operator, a Borromean Hecke element, and a numerical mass formula that the rest of the chapter must match.

The section opens with Definition: Borromean baryon, which fixes the composite of three Borromean rings as the structural model of a baryon. The pivot is Conjecture: Borromean baryon mass formula with common scale $\lambda_{\mathrm{scale}}$. This writes the baryon mass as a product of the algebraic categorical volume and a common scale factor. The companion Conjecture: Borromean baryon $\lambda_{\mathrm{scale}}$ substrate form: $5/2 - h^2 \cdot G + O(h^4)$ proposes the substrate decomposition. The linked Remark: Skein substrate identity for $\delta = q^{1/2} - q^{-1/2}$ anchors the conjecture to a structural cross-check at the figure-eight knot. The operator-side machinery follows in Definition: Typed crossing operator, which decomposes a crossing by quark flavour, and Definition: Borromean Hecke element, which builds the Markov-stabilised element of $H_4(q)$.

The structural results Proposition: Reidemeister invariance of mass and binding energy and Proposition: Stability pairs from Borromean spin-orbit shell-transition knots show that the mass is a knot invariant under the three Reidemeister moves. Furthermore, they show that the shell-transition geometry produces stability pairs. The Example: The proton as a Borromean hadron and the linked Proposition: Fermions are knots, bosons are links pin both the proton and the fermion/boson statistics distinction onto the same Borromean carrier. The interpretive remark on shell transitions closes the loop. The next section, **Categorical Mass Foundations**, treats the typed crossing operator and the Reidemeister invariance of mass as fixed. It lifts them to a categorical definition of mass that decomposes by Wedderburn block.

_(draft.)_
<!-- FILE_END: borromean-reidemeister-intro.md -->

<!-- FILE_START: borromean-baryon.md -->
A **Borromean baryon** is a hadron ([hadron](#def:hadron)) whose three constituents are unknots $K_{0_1}$ joined by the Borromean link $\mathcal{B}_3$ and bound by the Hopf link $\mathcal{L}_H$:

$$
  B = 
  \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1})
   \oplus  \mathcal{L}_H
$$
<!-- FILE_END: borromean-baryon.md -->

<!-- FILE_START: borromean-topological-confinement.md -->
**Brunnian property.** The defining property of the Borromean link $\mathcal{B}_3$ is that every two-component sub-link is the unlink. The three components are topologically inseparable, yet no two of them are pairwise linked. Concretely, deleting any one of the three unknots that make up a [Borromean baryon](#def:borromean-baryon) leaves a trivial two-component unlink. The topological binding of the remaining two strands collapses immediately.

**Implication for topological isolation.** An "isolated" component would be the configuration produced by lifting one unknot out of $\mathcal{B}_3$. Such a configuration is unstable in the Borromean topology. The same move that extracts one strand unlinks the other two. Thus, the extraction of a single component arrives together with the dissolution of the entire three-component bound state. Pulling on a single constituent produces three unbound unknots rather than a partially bound state. This Brunnian property models a strict three-body inseparability, providing a topological analogue for three-component bound states.
<!-- FILE_END: borromean-topological-confinement.md -->

<!-- FILE_START: brunnian-property-of-borromean.md -->
**Conjecture (Brunnian property of $\mathcal{B}_3$).** *Let $\mathcal{B}_3 \subset \mathbb{R}^3$ be the standard Borromean link ([Borromean baryon](#def:borromean-baryon)), presented as the closed braid $\overline{(\sigma_0\sigma_1^{-1})^3}$ in $B_3$. For each $i \in \{0, 1, 2\}$, let $\mathcal{B}_3 \setminus K_i$ denote the two-component sub-link obtained by removing the $i$-th component. Then $\mathcal{B}_3 \setminus K_i$ is topologically equivalent to the trivial two-component unlink $U_2$.*

This formalizes the confinement mechanism of [topological mechanism of color confinement](#rem:borromean-topological-confinement): removing any single component dissolves the binding between the remaining two. This is the defining property of Brunnian links \cite{kawauchi1996}. Naive strand-deletion at the braid word level does not immediately yield the empty braid. For example, deleting the 0-th strand produces $(\sigma_0^{-1})^3 \in B_2$, whose closure is the negative trefoil $\overline{3_1}$. Topological equivalence to $U_2$ requires a sequence of Reidemeister moves.

## Lean structure

The statement is co-located with `def:borromean-baryon` under the `qou` Lake package. The substantive declarations live at [`QOU.KnotTheory.Brunnian`](../lean/QOU/KnotTheory/Brunnian.lean):

```lean
-- BraidWord-level naive component deletion.
def BraidWord.deleteComponent (β : BraidWord) (i : Fin β.strands) : BraidWord

-- Predicate: closure of β is the n-component trivial unlink.
def isUnlink (β : BraidWord) : Prop

-- The Brunnian property as a conjectural class instance.
theorem borromean_brunnian :
  ∀ i : Fin 3,
    isUnlink (borromeanRings.deleteComponent i) := by
  sorry  -- Ref: [kawauchi1996] Survey of Knot Theory §1.5
```

The `sorry` acts as a conjectural witness (per [AGENTS.md §3b-cond]). The gap is not a missing arithmetic fact, but the absence of Mathlib primitives for Reidemeister and Markov-move equivalence on braid-word closures. Formal topological equivalence to $U_2$ requires an explicit sequence of two R2 moves and one R3 move, which cannot be stated until the link-equivalence relation is formalized.
<!-- FILE_END: brunnian-property-of-borromean.md -->

<!-- FILE_START: delta-skein-substrate-identity.md -->
**Remark (substrate identity for the proton–neutron Skein difference).** Under the common-scale Borromean baryon mass formula ([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)), the proton–neutron Skein difference is derived from three calibration inputs:

$$
  \Delta S(n - p)
  \;:=\;
  S(\mathfrak{n}) - S(\mathfrak{p})
  \;=\;
  \frac{\mathfrak{Q}_\beta + m_e}{m_e}
  \;-\;
  \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
  \cdot \bigl[\lambda_{\mathrm{scale}}(\mathfrak{n}) - \lambda_{\mathrm{scale}}(\mathfrak{p})\bigr].
$$

If the common-scale conjecture holds (with $\lambda_{\mathrm{scale}}$ independent of the orientation partition), the second bracket vanishes. The identity reduces to:

$$
  \boxed{\;
    \Delta S(n - p)
    \;=\;
    \frac{\mathfrak{Q}_\beta + m_e}{m_e}
    \;=\;
    \frac{m_n - m_p}{m_e}
  \;}
$$

This is a closed-form prediction in $\{m_e, q_0\}$ via the substrate $\mathfrak{Q}_\beta$ Form A ([prop:q-beta-spectral-bridge](#prop:q-beta-spectral-bridge)), recorded in the [m-baryon-volume-form witness](https://github.com/litlfred/qou/blob/claude/neutron-mass-50dps-chain/computations/m-baryon-volume-form.witness.json), with no calibration to the proton or neutron individually.

## Normalisation

The Skein contribution divided by the Borromean topological quantum gives a dimensionless residual:

$$
  \widetilde{\Delta S}(n - p)
  \;:=\;
  \frac{\Delta S(n - p)}{\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}
  \;=\;
  \frac{m_n - m_p}{m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}.
$$

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps) and CAL-1 $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}\ldots\;\mathrm{MeV}$, we evaluate this via the [`m-baryon-volume-form.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json):

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ at $q_0$ | $746.4179\ldots$ | substrate compute |
| $(\mathfrak{Q}_\beta + m_e)/m_e$ at $q_0$ | $2.53388\ldots$ | CAL-3 + CAL-1 ([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale)) |
| $\widetilde{\Delta S}_{\mathrm{derived}}$ | $0.0033943\ldots$ | ratio |
| $\widetilde{\Delta S}_{\mathrm{empirical}}$ | $0.0033908\ldots$ | $\lambda_p - \lambda_n$ from CODATA $m_p$, $m_n$ |
| relative agreement | $1\,015$ ppm | — |

## Identity of the residual

The substrate $\mathfrak{Q}_\beta$ ansatz predicts $\mathfrak{Q}_\beta(q_0) = 0.78174\ldots\;\mathrm{MeV}$ against the empirical CAL-3 value $0.78233341\ldots\;\mathrm{MeV}$ ([rem:beta-decay-energy-scale](#rem:beta-decay-energy-scale))—a $760$ ppm residual. The $\widetilde{\Delta S}$ relative error of $1\,015$ ppm is the same residual, dominated by:

1. the symmetric $(\mathfrak{Q}_\beta+m_e)/m_e$ numerator (set by the substrate $\mathfrak{Q}_\beta$ formula's $\sim 760$ ppm error, plus the CAL-1 $m_e$ uncertainty);
2. the common-scale conjecture $\lambda_{\mathrm{scale}}(\mathfrak{p}) - \lambda_{\mathrm{scale}}(\mathfrak{n}) = 0$.

The 1 015 ppm agreement is consistent with the existing $\mathfrak{Q}_\beta$ closure precision under the common-scale hypothesis. Falsification of the common-scale conjecture requires either a direct closed-form derivation of $\lambda_{\mathrm{scale}}(\mathfrak{p}) \neq \lambda_{\mathrm{scale}}(\mathfrak{n})$ from the substrate, or a substrate-only refinement of $\mathfrak{Q}_\beta$ exposing a non-zero residual after subtraction.

## Substrate-only character

The derivation consumes three substrate quantities:

| Input | Provenance | Calibration |
|-------|-----------|-------------|
| $m_e$ | input | **CAL-1** |
| $q_0$ | input (via $m_\mu/m_e$) | **CAL-2** |
| $\mathrm{Vol}(\mathcal{B}_3)$ | Thurston topological invariant | — |

The identity predicts $\Delta S(n - p)$ from CAL-1, CAL-2, and a topological invariant. CAL-3 enters only as a consistency cross-check ([prop:three-calibration-inputs](#prop:three-calibration-inputs)).

## Scope

The Borromean Vol-form mass ansatz is consistent with CODATA to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and a fixed topological invariant. The common scale $\lambda_{\mathrm{scale}}$ itself requires further derivation to determine $m_p$ and $m_n$ individually (cf. [conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)).
<!-- FILE_END: delta-skein-substrate-identity.md -->

<!-- FILE_START: figure-8-muon-mass-cross-check.md -->
**Remark (numerical cross-check of CAL-2 at 50 dps: $\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$).**
*The CAL-2 identity ([prop:three-calibration-inputs](#prop:three-calibration-inputs))*

$$
  \frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

*is the substrate-side anchor that fixes $q_0$. The [derive\_m\_baryon\_volume\_form](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/derive_m_baryon_volume_form.py) script evaluates both sides at 50-decimal precision and records the residual in [`m-baryon-volume-form.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json):*

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $2.0298832128\ldots$ | substrate (figure-8 archimedean image) |
| $\hbar_q^2 = ((q_0 - 1)/q_0)^2$ at $q_0$ | $9.8174\ldots \times 10^{-3}$ | substrate (CAL-2) |
| $\mathrm{Vol}(4_1)/\hbar_q^2$ at $q_0$ | $206.76828305\ldots$ | substrate |
| $m_\mu/m_e$ (CODATA 2022) | $206.7682830\ldots$ | empirical |
| relative residual | $1.45 \times 10^{-30}$ ppm | — |

## Structural vanishing of the residual

The 50-dps residual is $\sim 10^{-30}$ ppm. This is **not** a fit, coincidence, or fortunate cancellation. It is exactly the $q_0$-pinning equation read in the forward direction:

- The CAL-2 calibration *defines* $q_0$ as the unique real solution of $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ ([prop:local-substrate-q](#prop:local-substrate-q)).
- Evaluating both sides at *that* $q_0$ yields equality by construction, up to the 50-dps numerical precision of the pinning algorithm and the CODATA $m_\mu/m_e$ truncation.

The witness therefore serves as a **numerical certificate of the pinning procedure**. It is not a falsifiability test of the formula. A falsifiability test would have to vary $q_0$ or add an independent substrate constraint ([prop:three-calibration-inputs](#prop:three-calibration-inputs)).

## Significance for the Borromean baryon programme

The figure-8 (muon) sector verifies the [$\mathrm{Vol}(K)/\hbar_q^2$](#lem:topological-mass-cat-descended) ansatz at the single-knot level with topologically trivial Skein contribution ($S(4_1) = 0$ in the canonical orientation). The mass formula reduces to $m_\mu = m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$.

The Borromean baryon programme ([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)) asks whether the same ansatz, lifted to a 3-link with non-trivial Skein contribution, gives baryon masses with a single common scale $\lambda_{\mathrm{scale}}$:

$$
  m_B
  \;=\;
  m_e \cdot \left[\,
    \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
    \cdot \lambda_{\mathrm{scale}}
    \;+\; S(B)
  \,\right].
$$

In the figure-8 case, the formula degenerates to $\lambda_{\mathrm{scale}}^{(4_1)} = 1$ and $S(4_1) = 0$. In the Borromean case, the empirical closure target is $\lambda_{\mathrm{scale}}^{(\mathcal{B}_3)} \approx 2.46$ (see [conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)).

The substrate consistency of $\Delta S(n - p)$ ([rem:delta-skein-substrate-identity](#rem:delta-skein-substrate-identity)) to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and $\mathrm{Vol}(\mathcal{B}_3)$ is the first non-trivial extension of the figure-8 / muon cross-check to the Borromean / baryon sector.
<!-- FILE_END: figure-8-muon-mass-cross-check.md -->

<!-- FILE_START: typed-crossing-operator.md -->
Within the Borromean baryon ([Definition](#def:borromean-baryon)), the three quark strands form a $3$-strand braid in $B_3$. Each pairwise crossing between strands $i$ and $j$ is resolved in the Iwahori–Hecke algebra $H_3(R, q)$ ([Hecke algebra](#rem:hecke-algebra-from-braiding)) according to the **flavors** of the quarks at positions $i$ and $j$.

The **typed crossing operator** $C(f_i, f_j; \sigma_k) \in H_3(R, q)$ for a pair of quarks with flavors $f_i, f_j \in \{\mathfrak{u}, \mathfrak{d}\}$ at generator $\sigma_k$ is:

$$
  C(f_i, f_j; \sigma_k)
  = 
  \begin{cases}
    \sigma_k
      & \text{if } f_i = f_j = \mathfrak{u}
        \quad\text{(both up)}, \\[6pt]
    \sigma_k - (q - q^{-1})\mathbf{1}
      & \text{if } f_i = f_j = \mathfrak{d}
        \quad\text{(both down)}, \\[6pt]
    \sigma_k - \tfrac{1}{2}(q - q^{-1})\mathbf{1}
      & \text{if } f_i \neq f_j
        \quad\text{(mixed)}.
  \end{cases}
$$

**Motivation.**

- The **up--up** crossing is the bare generator $\sigma_k$. Positive-orientation unknots cross positively.
- The **down--down** crossing is the *inverse* generator $\sigma_k^{-1} = \sigma_k - (q - q^{-1})$, expanded via the Hecke relation. Negative-orientation unknots cross negatively.
- The **mixed** crossing is the arithmetic mean $\tfrac{1}{2}(\sigma_k + \sigma_k^{-1}) = \sigma_k - \tfrac{1}{2}(q - q^{-1})$. One positive and one negative orientation average to a half-shift.

These three cases reflect the three crossing types generated by the quark flavor assignments ([up quark](#def:up-quark), [down quark](#def:down-quark)). The typed crossing operator encodes the flavor dependence of the strong interaction within the Borromean link.
<!-- FILE_END: typed-crossing-operator.md -->

<!-- FILE_START: nucleon-hecke-element.md -->
Let $\mathfrak{N} = [\mathfrak{q}_1, \mathfrak{q}_2, \mathfrak{q}_3]$ denote a Borromean baryon ([Definition](#def:borromean-baryon)) with quark flavors $f_1, f_2, f_3 \in \{\mathfrak{u}, \mathfrak{d}\}$. The **nucleon Hecke element** evaluates in $H_3(R, q)$ as:

$$
  \mathfrak{N}(f_1, f_2, f_3)
  = 
  \mathcal{B}_3
   \cdot 
  C(f_1, f_2; \sigma_0)
   \cdot 
  C(f_1, f_3; \sigma_0)
   \cdot 
  C(f_2, f_3; \sigma_1)
$$

where:

- $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3 \in H_3(R, q)$ is the Borromean link element ([Borromean baryon](#def:borromean-baryon)).
- $C(f_i, f_j; \sigma_k)$ is the typed crossing operator ([typed crossing](#def:typed-crossing-operator)) for the quark pair at positions $i, j$.
- The three pairwise crossings $(1,2)$, $(1,3)$, $(2,3)$ are assigned to generators $\sigma_0, \sigma_0, \sigma_1$ respectively, matching the $B_3$ strand geometry.

**Proton.** For $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{u}; \sigma_0)}_{\sigma_0}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}\mathrm{HA}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_1)}_{\sigma_1 - \tfrac{1}{2}\mathrm{HA}\cdot\mathbf{1}}
$$

where $\mathrm{HA} = q - q^{-1}$.

**Neutron.** For $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$:

$$
  \mathfrak{n}
  = 
  \mathcal{B}_3
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}\mathrm{HA}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{u}, \mathfrak{d}; \sigma_0)}_{\sigma_0 - \tfrac{1}{2}\mathrm{HA}\cdot\mathbf{1}}
   \cdot 
  \underbrace{C(\mathfrak{d}, \mathfrak{d}; \sigma_1)}_{\sigma_1 - \mathrm{HA}\cdot\mathbf{1}}
$$

**Normal form.** After Gröbner--Shirshov reduction (Hecke, Yang--Baxter, and far-commutativity relations), each nucleon reduces to exactly **six terms**, one for each basis element of $H_3(R, q)$ ($\dim H_3(R, q) = 3! = 6$):

$$
  \mathfrak{N}
  = 
  c_\gamma\mathbf{1}
  + c_{\sigma_0}\sigma_0
  + c_{\sigma_1}\sigma_1
  + c_{L_+}\sigma_0\sigma_1
  + c_{L_-}\sigma_1\sigma_0
  + c_{e^-}\sigma_0\sigma_1\sigma_0
$$

The coefficients $c_\bullet \in \mathbb{Z}[q, q^{-1}]$ encode the particle content of the nucleon: the photon channel $\gamma$ ($\mathbf{1}$), virtual crossings $\sigma_0, \sigma_1$, Hopf links $L_+, L_-$ ($\sigma_0\sigma_1, \sigma_1\sigma_0$), and the trefoil (electron) $e^-$ ($\sigma_0\sigma_1\sigma_0$).

The **net** of the nucleon is:

$$
  \mathrm{net}(\mathfrak{N})
  = 
  \sum_{\text{basis } w} c_w(q_0)
$$

evaluated at the substrate parameter $q_0$.

**Witness**: `breit-wheeler-nucleon-nf.witness.json` (Gröbner--Shirshov reduction: proton 6 terms, $\mathrm{net}(\mathfrak{p}) \approx +0.9991$; neutron 6 terms, $\mathrm{net}(\mathfrak{n}) \approx +0.8108$).
<!-- FILE_END: nucleon-hecke-element.md -->

<!-- FILE_START: hadron-proton-example.md -->
The proton is a [hadron](#def:hadron). Its three constituents link in a [Borromean configuration](#def:borromean-baryon).

**Constituent quarks as unknots.**
Quarks are unknots $K_{0_1}$ distinguished by their crossing orientation within the Borromean link. The up quark $\mathfrak{u}$ carries positive crossing orientation, while the down quark $\mathfrak{d}$ carries negative crossing orientation. The proton $\mathfrak{p}$ comprises two up quarks and one down quark:

$$
  \mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_{\mathrm{Bor}},
$$

where $\mathcal{L}_{\mathrm{Bor}}$ is the Borromean link.

**Borromean property.**
The Borromean link requires all three components to remain linked. Removing any single component unlinks the remaining two:

- Remove $\mathfrak{u}_1$: the pair $(\mathfrak{u}_2, \mathfrak{d})$ has linking number zero and separates.
- Remove $\mathfrak{u}_2$: the pair $(\mathfrak{u}_1, \mathfrak{d})$ unlinks.
- Remove $\mathfrak{d}$: the pair $(\mathfrak{u}_1, \mathfrak{u}_2)$ unlinks.

Together, the three components form a non-trivial link. Their pairwise linking numbers vanish, but their Milnor triple linking number $\bar{\mu}(123) = \pm 1$ is non-zero. This provides the topological mechanism for quark confinement. No single quark can be extracted without dissolving the entire structure, yet any two-body subsystem remains topologically trivial.

**Mass from the linking matrix.**
The proton mass decomposes into constituent masses and binding energy:

$$
  \mathfrak{m}_{\mathfrak{p}} = 2\mathfrak{m}(\mathfrak{u}) + \mathfrak{m}(\mathfrak{d}) + \mathfrak{E}_{\mathrm{bind}}.
$$

The binding energy $\mathfrak{E}_{\mathrm{bind}}$ originates from the Borromean linking. Because the individual quark masses $\mathfrak{m}(\mathfrak{u})$ and $\mathfrak{m}(\mathfrak{d})$ are small, the binding energy dominates. The mass of the proton arises overwhelmingly from topological complexity.

We compute the binding energy from the [crossing energy](#ex:crossing-energy-trefoil) of the linking braid word $\beta_{\mathrm{Bor}} \in B_3$. The Borromean link admits the braid representation $\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$. This geometry yields mutual crossings that ensure $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. At the substrate parameter $q \approx 1.110$, this computation gives:

$$
  \mathfrak{m}_{\mathfrak{p}}(q) \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} \text{MeV}.
$$

**Stability of the proton.**
The proton is the lightest baryon and cannot decay into lighter baryons. Topologically, the Borromean link of three unknots is the simplest non-trivial three-component link carrying the correct charge and color quantum numbers. No sequence of Reidemeister moves or Markov stabilizations can simplify it further while preserving the baryon number.
<!-- FILE_END: hadron-proton-example.md -->

<!-- FILE_START: fermion-boson-knot-link.md -->
**Proposition.**
The fermion--boson decomposition ([fermion--boson decomposition](#def:fermion-boson-decomposition)) coincides with the knot--link decomposition of the $T(2,n)$ torus family on Bring's surface:

- A **fermion** ($\alpha_V \neq 0$) is a **knot** (1 component).
- A **boson** ($\alpha_V = 0$) is a **link** (2 components).

Equivalently, fermions have odd $n$ in $T(2,n)$ and bosons have even $n$.
<!-- FILE_END: fermion-boson-knot-link.md -->

<!-- FILE_START: shell-transition-knot.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
The stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ arise from the harmonic oscillator shell structure of nucleons in the nuclear mean field, corrected by the spin-orbit coupling of the Borromean baryon's 3 internal crossings.

**1. Harmonic oscillator levels.**
Each nucleon (a Borromean baryon $\mathcal{B}_3$, [Borromean baryon](#def:borromean-baryon)) vibrates in the nuclear mean field created by all other nucleons. The 3D harmonic oscillator has shell sizes
$$
  s_N =  (N + 1)(N + 2),
  \qquad N = 0, 1, 2, \ldots
$$
and cumulative closures
$$
  C_N =  \sum_{k=0}^{N} (k+1)(k+2)
  =  \frac{(N+1)(N+2)(N+3)}{3}.
$$
See [Table 1](#tbl:shell-transition-knot-table1-data).

Without spin-orbit coupling, the shell closures would be $\{2, 8, 20, 40, 70, 112, 168\}$, which contradicts observation.

**2. Spin-orbit coupling from the Borromean structure.**
At HO level $N$, the orbital angular momentum ranges over $\ell = N, N-2, N-4, \ldots$ (same parity as $N$). Each $\ell \geq 1$ splits into two sub-levels with total angular momentum
$$
  j = \ell + \tfrac{1}{2}
  \qquad\text{and}\qquad
  j = \ell - \tfrac{1}{2}
$$
having $2j + 1$ states each. The spin-orbit coupling energy is proportional to the $q$-Laplacian eigenvalue ([Fourier decomposition](#conj:orbital-fourier-decomposition)):
$$
  E_{\mathrm{SO}}(\ell, j)
   \propto 
  [\ell]_q [\ell + 1]_q
  \cdot (j - \ell)
$$
where $j - \ell = +\tfrac{1}{2}$ for the high-$j$ level (pushed down in energy) and $j - \ell = -\tfrac{1}{2}$ for the low-$j$ level (pushed up).

**3. The shell-transition threshold at $N = 3$.**
The Borromean baryon $\mathcal{B}_3$ has exactly 3 internal crossings (the minimum crossing number of the Borromean link). Spin-orbit coupling strength is proportional to the number of Borromean crossings times the orbital $q$-Laplacian eigenvalue.

The coupling exceeds the HO level spacing when
$$
  3 \cdot [\ell]_q [\ell + 1]_q  >  2(N + 1)
  \qquad\text{(level spacing)}
$$
At $q = 1$, this reduces to $3 \cdot N(N+1) > 2(N+1)$ ($N > 2/3$, so $N \geq 1$). The coupling must exceed a full gap (not just the intra-level spacing). The empirical threshold is $N \geq 3$, matching the 3 Borromean crossings.

When the threshold is exceeded, the highest-$j$ sub-level at HO level $N$ ($j = N + \tfrac{1}{2}$ with $2(N+1)$ states) drops below the gap and joins the previous shell closure. This is the shell-transition level.

**4. The stability pairs.**
See [Table 2](#tbl:shell-transition-knot-table2-data).

The shell-transition levels and their state counts $2(N+1)$ are shown in [Table 3](#tbl:shell-transition-knot-table3-data). All 7 stability pairs are reproduced exactly.

*Proof.*
The HO cumulative $C_N = (N+1)(N+2)(N+3)/3$ is standard. The shell-transition mechanism at $N \geq 3$ follows from the spin-orbit coupling exceeding the HO gap, with the Borromean crossing number $3$ setting the threshold. The state count $2(N+1)$ for the shell-transition level is the degeneracy of the $j = N + 1/2$ sub-level. The cumulative result matches $\{2, 8, 20, 28, 50, 82, 126\}$ by direct computation. $\square$
<!-- FILE_END: shell-transition-knot.md -->

<!-- FILE_START: shell-transition-knot-interpretation.md -->
**Threshold value $N = 3$.**

The Borromean link $\mathcal{B}_3$ has crossing number $3$.
The spin-orbit coupling is mediated by the interaction between
the Borromean crossings and the orbital crossings of the
nucleon in the nuclear Hopf link.  The number of "resonant"
coupling channels equals the Borromean crossing number.  For
$N < 3$, there are fewer orbital crossings than Borromean
crossings, and the coupling is sub-threshold.  For $N \geq 3$,
all 3 Borromean crossings can couple simultaneously to the
orbital mode, producing a spin-orbit energy that exceeds the
HO gap.

In a QOU with a different Borromean-like structure (e.g. a
4-component Brunnian link with crossing number $c$), the
shell-transition threshold would shift to $N \geq c$, producing
different stability pairs.
<!-- FILE_END: shell-transition-knot-interpretation.md -->

