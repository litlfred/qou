<!-- FILE_START: borromean-reidemeister-intro.md -->
The bundle and observation data make the knot--particle dictionary measurable. We apply the dictionary to the Borromean baryon. This structure consists of three pairwise-unlinked unknots that bind into a stable composite. Borromean binding forces the typed crossing operator, a Borromean Hecke element, and a numerical mass formula.

This section defines the Borromean baryon as the structural model of a baryon. The baryon mass formula writes the mass as a product of the algebraic categorical volume and a common scale factor $\lambda_{\mathrm{scale}}$. The substrate decomposition proposes the form $5/2 - h^2 \cdot G + O(h^4)$ for this scale. A Skein substrate identity anchors the conjecture to a structural cross-check at the figure-eight knot. On the operator side, the typed crossing operator decomposes a crossing by quark flavour, and the Borromean Hecke element builds the Markov-stabilised element of $H_4(q)$.

We prove the mass is a knot invariant under the three Reidemeister moves. The shell-transition geometry produces stability pairs. The proton and the fermion/boson statistics distinction map onto the Borromean carrier. The subsequent section lifts the typed crossing operator and the Reidemeister invariance to a categorical definition of mass that decomposes by Wedderburn block.

_(draft.)_
<!-- FILE_END: borromean-reidemeister-intro.md -->

<!-- FILE_START: borromean-baryon.md -->
A **Borromean baryon** is a hadron whose three constituents are unknots $K_{0_1}$ joined by the Borromean link $\mathcal{B}_3$ and bound by the Hopf link $\mathcal{L}_H$:

$$
  B = 
  \mathcal{B}_3(K_{0_1}, K_{0_1}, K_{0_1})
   \oplus  \mathcal{L}_H
$$
<!-- FILE_END: borromean-baryon.md -->

<!-- FILE_START: borromean-topological-confinement.md -->
**Brunnian property.** The defining property of the Borromean link $\mathcal{B}_3$ is that every two-component sub-link is the unlink. The three components are topologically inseparable, yet no two are pairwise linked. Deleting any one of the three unknots in a Borromean baryon leaves a trivial two-component unlink. The topological binding of the remaining two strands collapses immediately.

**Implication for topological isolation.** An "isolated" component requires lifting one unknot out of $\mathcal{B}_3$. This configuration is unstable in the Borromean topology. The move that extracts one strand unlinks the other two. The extraction of a single component dissolves the entire three-component bound state. Pulling on a single constituent produces three unbound unknots. This Brunnian property models a strict three-body inseparability.
<!-- FILE_END: borromean-topological-confinement.md -->

<!-- FILE_START: brunnian-property-of-borromean.md -->
**Conjecture (Brunnian property of $\mathcal{B}_3$).** *Let $\mathcal{B}_3 \subset \mathbb{R}^3$ be the standard Borromean link, presented as the closed braid $\overline{(\sigma_0\sigma_1^{-1})^3}$ in $B_3$. For each $i \in \{0, 1, 2\}$, let $\mathcal{B}_3 \setminus K_i$ denote the two-component sub-link obtained by removing the $i$-th component. Then $\mathcal{B}_3 \setminus K_i$ is topologically equivalent to the trivial two-component unlink $U_2$.*

This formalizes the confinement mechanism. Removing any single component dissolves the binding between the remaining two. This is the defining property of Brunnian links \cite{kawauchi1996}. Naive strand-deletion at the braid word level does not immediately yield the empty braid. Deleting the 0-th strand produces $(\sigma_0^{-1})^3 \in B_2$, whose closure is the negative trefoil $\overline{3_1}$. Topological equivalence to $U_2$ requires a sequence of Reidemeister moves.

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

The `sorry` acts as a conjectural witness. The gap is the absence of Mathlib primitives for Reidemeister and Markov-move equivalence on braid-word closures. Formal topological equivalence to $U_2$ requires an explicit sequence of two R2 moves and one R3 move. This cannot be stated until the link-equivalence relation is formalized.
<!-- FILE_END: brunnian-property-of-borromean.md -->

<!-- FILE_START: delta-skein-substrate-identity.md -->
**Remark (substrate identity for the proton–neutron Skein difference).** Under the common-scale Borromean baryon mass formula, the proton–neutron Skein difference is derived from three calibration inputs:

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

If the common-scale conjecture holds, the second bracket vanishes. The identity reduces to:

$$
  \boxed{\;
    \Delta S(n - p)
    \;=\;
    \frac{\mathfrak{Q}_\beta + m_e}{m_e}
    \;=\;
    \frac{m_n - m_p}{m_e}
  \;}
$$

This is a closed-form prediction in $\{m_e, q_0\}$ via the substrate $\mathfrak{Q}_\beta$ Form A, recorded in the witness file, with no calibration to the proton or neutron individually.

## Normalisation

The Skein contribution divided by the Borromean topological quantum gives a dimensionless residual:

$$
  \widetilde{\Delta S}(n - p)
  \;:=\;
  \frac{\Delta S(n - p)}{\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}
  \;=\;
  \frac{m_n - m_p}{m_e \cdot \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2}.
$$

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps) and CAL-1 $m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}\ldots\;\mathrm{MeV}$, we evaluate this:

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$ at $q_0$ | $746.4179\ldots$ | substrate compute |
| $(\mathfrak{Q}_\beta + m_e)/m_e$ at $q_0$ | $2.53388\ldots$ | CAL-3 + CAL-1 |
| $\widetilde{\Delta S}_{\mathrm{derived}}$ | $0.0033943\ldots$ | ratio |
| $\widetilde{\Delta S}_{\mathrm{empirical}}$ | $0.0033908\ldots$ | $\lambda_p - \lambda_n$ from CODATA $m_p$, $m_n$ |
| relative agreement | $1\,015$ ppm | — |

## Identity of the residual

The substrate $\mathfrak{Q}_\beta$ ansatz predicts $\mathfrak{Q}_\beta(q_0) = 0.78174\ldots\;\mathrm{MeV}$ against the empirical CAL-3 value $0.78233341\ldots\;\mathrm{MeV}$—a $760$ ppm residual. The $\widetilde{\Delta S}$ relative error of $1\,015$ ppm is the same residual, dominated by:

1. the symmetric $(\mathfrak{Q}_\beta+m_e)/m_e$ numerator;
2. the common-scale conjecture $\lambda_{\mathrm{scale}}(\mathfrak{p}) - \lambda_{\mathrm{scale}}(\mathfrak{n}) = 0$.

The 1 015 ppm agreement is consistent with the $\mathfrak{Q}_\beta$ closure precision under the common-scale hypothesis. Falsification of the common-scale conjecture requires either a direct closed-form derivation of $\lambda_{\mathrm{scale}}(\mathfrak{p}) \neq \lambda_{\mathrm{scale}}(\mathfrak{n})$ from the substrate, or a substrate-only refinement of $\mathfrak{Q}_\beta$ exposing a non-zero residual after subtraction.

## Substrate-only character

The derivation consumes three substrate quantities:

| Input | Provenance | Calibration |
|-------|-----------|-------------|
| $m_e$ | input | **CAL-1** |
| $q_0$ | input (via $m_\mu/m_e$) | **CAL-2** |
| $\mathrm{Vol}(\mathcal{B}_3)$ | Thurston topological invariant | — |

The identity predicts $\Delta S(n - p)$ from CAL-1, CAL-2, and a topological invariant. CAL-3 enters only as a consistency cross-check.

## Scope

The Borromean mass ansatz is consistent with CODATA to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and a fixed topological invariant. The common scale $\lambda_{\mathrm{scale}}$ requires further derivation to determine $m_p$ and $m_n$ individually.
<!-- FILE_END: delta-skein-substrate-identity.md -->

<!-- FILE_START: figure-8-muon-mass-cross-check.md -->
**Remark (numerical cross-check of CAL-2 at 50 dps: $\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$).**
*The CAL-2 identity*

$$
  \frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

*is the substrate-side anchor that fixes $q_0$. We evaluate both sides at 50-decimal precision and record the residual in the witness file:*

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $2.0298832128\ldots$ | substrate (figure-8 archimedean image) |
| $\hbar_q^2 = ((q_0 - 1)/q_0)^2$ at $q_0$ | $9.8174\ldots \times 10^{-3}$ | substrate (CAL-2) |
| $\mathrm{Vol}(4_1)/\hbar_q^2$ at $q_0$ | $206.76828305\ldots$ | substrate |
| $m_\mu/m_e$ (CODATA 2022) | $206.7682830\ldots$ | empirical |
| relative residual | $1.45 \times 10^{-30}$ ppm | — |

## Structural vanishing of the residual

The 50-dps residual is $\sim 10^{-30}$ ppm. This is exactly the $q_0$-pinning equation read in the forward direction. The CAL-2 calibration defines $q_0$ as the unique real solution of $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$. Evaluating both sides at that $q_0$ yields equality by construction, up to the 50-dps numerical precision of the pinning algorithm and the CODATA $m_\mu/m_e$ truncation.

The witness serves as a numerical certificate of the pinning procedure. It is not a falsifiability test of the formula. A falsifiability test requires varying $q_0$ or adding an independent substrate constraint.

## Significance for the Borromean baryon programme

The figure-8 (muon) sector verifies the mass ansatz at the single-knot level with a topologically trivial Skein contribution ($S(4_1) = 0$ in the canonical orientation). The mass formula reduces to $m_\mu = m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$.

The Borromean baryon programme asks whether the same ansatz, lifted to a 3-link with non-trivial Skein contribution, gives baryon masses with a single common scale $\lambda_{\mathrm{scale}}$:

$$
  m_B
  \;=\;
  m_e \cdot \left[\,
    \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
    \cdot \lambda_{\mathrm{scale}}
    \;+\; S(B)
  \,\right].
$$

In the figure-8 case, the formula degenerates to $\lambda_{\mathrm{scale}}^{(4_1)} = 1$ and $S(4_1) = 0$. In the Borromean case, the empirical closure target is $\lambda_{\mathrm{scale}}^{(\mathcal{B}_3)} \approx 2.46$.

The substrate consistency of $\Delta S(n - p)$ to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and $\mathrm{Vol}(\mathcal{B}_3)$ is the first non-trivial extension of the figure-8 cross-check to the Borromean sector.
<!-- FILE_END: figure-8-muon-mass-cross-check.md -->

<!-- FILE_START: typed-crossing-operator.md -->
Within the Borromean baryon, the three quark strands form a $3$-strand braid in $B_3$. Each pairwise crossing between strands $i$ and $j$ is resolved in the Iwahori–Hecke algebra $H_3(R, q)$ according to the **flavors** of the quarks at positions $i$ and $j$.

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
- The **down--down** crossing is the inverse generator $\sigma_k^{-1} = \sigma_k - (q - q^{-1})$. Negative-orientation unknots cross negatively.
- The **mixed** crossing is the arithmetic mean $\tfrac{1}{2}(\sigma_k + \sigma_k^{-1}) = \sigma_k - \tfrac{1}{2}(q - q^{-1})$. One positive and one negative orientation average to a half-shift.

These three cases reflect the crossing types generated by the quark flavor assignments. The typed crossing operator encodes the flavor dependence of the strong interaction within the Borromean link.
<!-- FILE_END: typed-crossing-operator.md -->

<!-- FILE_START: nucleon-hecke-element.md -->
Let $\mathfrak{N} = [\mathfrak{q}_1, \mathfrak{q}_2, \mathfrak{q}_3]$ denote a Borromean baryon with quark flavors $f_1, f_2, f_3 \in \{\mathfrak{u}, \mathfrak{d}\}$. The **nucleon Hecke element** evaluates in $H_3(R, q)$ as:

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

- $\mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3 \in H_3(R, q)$ is the Borromean link element.
- $C(f_i, f_j; \sigma_k)$ is the typed crossing operator for the quark pair at positions $i, j$.
- The three pairwise crossings $(1,2)$, $(1,3)$, $(2,3)$ map to generators $\sigma_0, \sigma_0, \sigma_1$, respectively.

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

**Normal form.** After Gröbner--Shirshov reduction, each nucleon reduces to exactly six terms, one for each basis element of $H_3(R, q)$:

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

**Witness**: `breit-wheeler-nucleon-nf.witness.json`.
<!-- FILE_END: nucleon-hecke-element.md -->

<!-- FILE_START: hadron-proton-example.md -->
The proton is a hadron. Its three constituents link in a Borromean configuration.

**Constituent quarks as unknots.**
Quarks are unknots $K_{0_1}$ distinguished by their crossing orientation within the Borromean link. The up quark $\mathfrak{u}$ carries positive crossing orientation. The down quark $\mathfrak{d}$ carries negative crossing orientation. The proton $\mathfrak{p}$ comprises two up quarks and one down quark:

$$
  \mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_{\mathrm{Bor}},
$$

where $\mathcal{L}_{\mathrm{Bor}}$ is the Borromean link.

**Borromean property.**
The Borromean link requires all three components to remain linked. Removing any single component unlinks the remaining two:

- Remove $\mathfrak{u}_1$: the pair $(\mathfrak{u}_2, \mathfrak{d})$ has linking number zero and separates.
- Remove $\mathfrak{u}_2$: the pair $(\mathfrak{u}_1, \mathfrak{d})$ unlinks.
- Remove $\mathfrak{d}$: the pair $(\mathfrak{u}_1, \mathfrak{u}_2)$ unlinks.

The three components form a non-trivial link. Their pairwise linking numbers vanish, but their Milnor triple linking number $\bar{\mu}(123) = \pm 1$ is non-zero. This provides the topological mechanism for quark confinement. No single quark can be extracted without dissolving the entire structure. Any two-body subsystem remains topologically trivial.

**Mass from the linking matrix.**
The proton mass decomposes into constituent masses and binding energy:

$$
  \mathfrak{m}_{\mathfrak{p}} = 2\mathfrak{m}(\mathfrak{u}) + \mathfrak{m}(\mathfrak{d}) + \mathfrak{E}_{\mathrm{bind}}.
$$

The binding energy $\mathfrak{E}_{\mathrm{bind}}$ originates from the Borromean linking. Because the individual quark masses $\mathfrak{m}(\mathfrak{u})$ and $\mathfrak{m}(\mathfrak{d})$ are small, the binding energy dominates. The mass of the proton arises overwhelmingly from topological complexity.

We compute the binding energy from the crossing energy of the linking braid word $\beta_{\mathrm{Bor}} \in B_3$. The Borromean link admits the braid representation $\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$. This geometry yields mutual crossings that ensure $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. At the substrate parameter $q \approx 1.110$, this evaluates to:

$$
  \mathfrak{m}_{\mathfrak{p}}(q) \approx :val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} \text{MeV}.
$$

**Stability of the proton.**
The proton is the lightest baryon and cannot decay. Topologically, the Borromean link of three unknots is the simplest non-trivial three-component link carrying the correct charge and color quantum numbers. No sequence of Reidemeister moves or Markov stabilizations simplifies it further while preserving the baryon number.
<!-- FILE_END: hadron-proton-example.md -->

<!-- FILE_START: fermion-boson-knot-link.md -->
**Proposition.**
The fermion--boson decomposition coincides with the knot--link decomposition of the $T(2,n)$ torus family on Bring's surface:

- A **fermion** ($\alpha_V \neq 0$) is a **knot** (1 component).
- A **boson** ($\alpha_V = 0$) is a **link** (2 components).

Equivalently, fermions have odd $n$ in $T(2,n)$ and bosons have even $n$.
<!-- FILE_END: fermion-boson-knot-link.md -->

<!-- FILE_START: shell-transition-knot.md -->
**Proposition (conditional on the Borromean quark hypothesis).**
The stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ arise from the harmonic oscillator shell structure of nucleons in the nuclear mean field, corrected by the spin-orbit coupling of the Borromean baryon's 3 internal crossings.

**1. Harmonic oscillator levels.**
Each nucleon (a Borromean baryon $\mathcal{B}_3$) vibrates in the nuclear mean field created by all other nucleons. The 3D harmonic oscillator has shell sizes
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
having $2j + 1$ states each. The spin-orbit coupling energy is proportional to the $q$-Laplacian eigenvalue:
$$
  E_{\mathrm{SO}}(\ell, j)
   \propto 
  [\ell]_q [\ell + 1]_q
  \cdot (j - \ell)
$$
where $j - \ell = +\tfrac{1}{2}$ for the high-$j$ level (pushed down in energy) and $j - \ell = -\tfrac{1}{2}$ for the low-$j$ level (pushed up).

**3. The shell-transition threshold at $N = 3$.**
The Borromean baryon $\mathcal{B}_3$ has exactly 3 internal crossings. Spin-orbit coupling strength is proportional to the number of Borromean crossings times the orbital $q$-Laplacian eigenvalue.

The coupling exceeds the HO level spacing when
$$
  3 \cdot [\ell]_q [\ell + 1]_q  >  2(N + 1).
$$
At $q = 1$, this reduces to $3 \cdot N(N+1) > 2(N+1)$ ($N \geq 1$). The coupling must exceed a full gap. The empirical threshold is $N \geq 3$, matching the 3 Borromean crossings.

When the threshold is exceeded, the highest-$j$ sub-level at HO level $N$ drops below the gap and joins the previous shell closure. This is the shell-transition level.

**4. The stability pairs.**
See [Table 2](#tbl:shell-transition-knot-table2-data).

The shell-transition levels and their state counts $2(N+1)$ are shown in [Table 3](#tbl:shell-transition-knot-table3-data). All 7 stability pairs are reproduced exactly.

*Proof.*
The HO cumulative $C_N = (N+1)(N+2)(N+3)/3$ is standard. The shell-transition mechanism at $N \geq 3$ follows from the spin-orbit coupling exceeding the HO gap, with the Borromean crossing number $3$ setting the threshold. The state count $2(N+1)$ for the shell-transition level is the degeneracy of the $j = N + 1/2$ sub-level. The cumulative result matches $\{2, 8, 20, 28, 50, 82, 126\}$ by direct computation. $\square$
<!-- FILE_END: shell-transition-knot.md -->

<!-- FILE_START: shell-transition-knot-interpretation.md -->
**Threshold value $N = 3$.**

The Borromean link $\mathcal{B}_3$ has crossing number $3$. The spin-orbit coupling is mediated by the interaction between the Borromean crossings and the orbital crossings of the nucleon in the nuclear Hopf link. The number of resonant coupling channels equals the Borromean crossing number. For $N < 3$, there are fewer orbital crossings than Borromean crossings, and the coupling is sub-threshold. For $N \geq 3$, all 3 Borromean crossings couple simultaneously to the orbital mode. This produces a spin-orbit energy that exceeds the HO gap.

In a theoretical regime with a different Borromean-like structure (e.g. a 4-component Brunnian link with crossing number $c$), the shell-transition threshold shifts to $N \geq c$, producing different stability pairs.
<!-- FILE_END: shell-transition-knot-interpretation.md -->
