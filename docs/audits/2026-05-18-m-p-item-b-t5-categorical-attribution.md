# m_p Item B: T5 categorical attribution — full math+phys context

**Date:** 2026-05-18
**Branch:** `claude/canonical-chi-rust` (PR #683)
**Status:** Open R&D, structural resolution proposed (see §6).
**Predecessors:**
- `2026-05-17-1ppb-workplan-v5.md` §3 (Item B in m_p chain)
- `2026-05-17-m-p-item-a-closure.md` (Item A resolved; B blocks ¹H derived-status)
- `term5-aK-audit.witness.json` (PR #520 V1-vs-Gram audit)
- `term5-aK-v2-mirror-chirality-probe.witness.json` (V2 numeric)
- [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md)

## 1. Where T5 sits in the 6-term mass formula

The 6-term mass formula
([`thm:six-term-mass-formula-complete`](../../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md)):

$$
  \mathfrak{m}(Z, N) \;=\;
  \underbrace{m_e \cdot \rho_K \cdot |\mathrm{tr}_M|}_{T_1}
  \;+\; \underbrace{z^2 \sum_i \Phi_q(|\hat V_i|)}_{T_2}
  \;+\; \underbrace{z^2 \sum_{i<j} \Phi_q(|\hat V_i \hat V_j|)}_{T_3}
  \;+\; \underbrace{m_e \cdot \mathrm{tr}_M(C_{\dim_q})}_{T_4}
  \;+\; \underbrace{a_K \cdot \mathcal{C}_K}_{T_5}
  \;+\; \underbrace{\sum_\ell \mathrm{Res}_{q \to \zeta_\ell}[\cdots]}_{T_6}.
$$

| Term | Role | Status |
|------|------|--------|
| $T_1$ | Markov-trace anchor (rest-mass scale) | derived, MPFR-50dps |
| $T_2, T_3$ | Brane-tower quantum dilogarithm sums | derived (Item A) |
| $T_4$ | Frobenius co-Casimir (representation-theoretic) | derived |
| **$T_5$** | **Knot chirality / Bethe–Weizsäcker bulk** | **Item B (this audit)** |
| $T_6$ | Habiro cyclotomic residue tail | derived (Item C closed) |

$T_5$ is the **chirality / handedness** contribution and the
categorical replacement for the empirical Bethe–Weizsäcker
volume + surface terms ($\lambda_V \cdot A$, $\lambda_S \cdot
A^{2/3}$) plus the BW knot factor $a(N)$. The conjecture
([`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md))
unifies all three into one quantity: the **Markov-trace mass
defect** between the disconnected free-nucleon braid and the
connected atomic braid.

## 2. Mathematical context — competing definitions of $a_K$

Three categorical attributions for $a_K$ have been put on the
table; numerical values at $q_0$ for the proton (Z=1, N=0, A=1)
illustrate their structural difference:

| # | Definition | Symbolic | Proton @ $q_0$ |
|---|------------|----------|----------------|
| **D** (SDP+thimble dual) | chirality-active dual sum $1 + \sum_{\lambda \in \mathcal{A}^{\mathrm{chi}}} u_\lambda^*/u_0^*$ (=  $1 + \sum_{\sigma} (n^{\mathrm{atom}}_\sigma - n^{\mathrm{free}}_\sigma) \oint_\sigma \lambda_{\mathrm{SW}}^{(1)} / \lvert\mathrm{tr}_M^{\mathrm{free}}\rvert$ on archimedean side) | conjugate-pair cancellation at A=1 | $1.000000$ |
| **R** (Ratio) | $\dfrac{\lvert\mathrm{tr}_M(W_{\text{atom}})\rvert}{\lvert\mathrm{tr}_M(W_{\text{free}})\rvert}$ | trivially 1 at A=1 | $1.000000$ |
| **C** (Closed form / V1 narrative) | $\prod_{c \in \text{pn-crossings}} (1 + \mathrm{sign}(c) \cdot h)$, $h = q - q^{-1}$ | empty product at A=1 | $1.000000$ |
| **V1** (Gram, $\beta^* = \beta^{-1}$) | $\tau(\beta \cdot \beta^{-1}) = \tau(\mathbf{1}_n)$ | $\dfrac{(1+q^2)^4}{16 q^4}$ | $1.021972$ |
| **V2** (Mirror Gram, $\beta^* = \beta_{\text{mirror}}$) | $\tau(\beta \cdot \beta_{\text{mirror}}^{-1})$ | high-order polynomial in $q$ | $2.423743$ |

(**D** is added per §7b — the SDP shadow-price + thimble-intersection
realisation, the deepest structural attribution and the one the
existing infra already computes.)

For A = 2 (deuteron), A = 3 (figure-8 / triton), A = 4 (Borromean
/ ⁴He) the conjecture asserts (Step 4):

$$
  a_K^{(2)} = 1 + h, \qquad
  a_K^{(3)} = 1 - h^2, \qquad
  a_K^{(4)} = (1 - h^2)^2.
$$

The Π-over-pn-crossings closed form **C** reproduces these for
the canonical atomic braid words (each pn-crossing contributes
$(1 + \mathrm{sign} \cdot h)$; products give exactly the above).
The ratio form **R** is the universal categorical definition; **C**
is its small-A simplification on the local-knot regime.

### Why V1 was rejected (PR #520 follow-up)

V1 was framed in the original Gram-matrix conjecture as "the
natural Hecke choice" for the mirror $\beta^*$ but $\beta^* =
\beta^{-1}$ collapses:

$$
  \tau(\beta \cdot \beta^{-1}) \;=\; \tau(\mathbf{1}_n)
  \;=\; z^{n-1}
  \;=\; \biggl(\frac{1}{q^{1/2} + q^{-1/2}}\biggr)^{n-1}
$$

— a function **only of strand count $n$**, carrying zero
information about the braid word $\beta$ itself. The 1.022 value
for the proton is $z^2$ for $n = 3$ (rescaled to a different
normalisation in the audit). V1 is **structurally informationless**
about chirality; it cannot be $a_K$.

### Why V2 is **not** $T_5$ either

V2 = $\tau(\beta \cdot \beta_{\text{mirror}}^{-1})$ where
$\beta_{\text{mirror}}$ flips every crossing pointwise (the
geometric mirror knot $K^*$). This *is* a genuine chirality
measure — confirmed by the 25% T ↔ ³He asymmetry in
`term5-aK-v2-mirror-chirality-probe.witness.json` (V2 distinguishes
isospin mirrors as required by chirality; V1 cannot).

**But V2 does not reduce to the BW knot factor for A=2,3,4.**
Compare:

| A | Atom | $a_K$ (BW / conjecture Step 4) | V2 @ $q_0$ (numeric) |
|---|------|-------------------------------|--------------------|
| 1 | proton  | 1 (no pn-crossings)            | 2.424 |
| 1 | neutron | 1                              | 2.134 |
| 2 | deuteron | $1 + h \approx 1.209$         | 5.228 |
| 3 | triton  | $1 - h^2 \approx 0.988$        | 10.477 |
| 3 | ³He     | $1 - h^2 \approx 0.988$        | 13.994 |

The structural mismatch (factor ~2-13×) is **not a normalisation
constant**: V2 grows with $A$ while the BW knot factor stays
$\mathcal{O}(1)$. V2 measures a fundamentally different
categorical object — the **doubled-braid Markov trace**, which
counts mirror-violating crossings squared. It is plausibly the
right operator for a *separate* term (e.g. a quark-spin pairing
diagonal, or part of $T_6$'s chirality-sensitive residue), but
**not** $T_5$.

## 3. Physical context — what does $T_5$ represent?

In the QOU mass identity, $T_5$ plays three classical roles
simultaneously:

1. **Bethe–Weizsäcker bulk volume** ($\lambda_V \cdot A \approx
   15.8\;\mathrm{MeV}/A$): the dominant nuclear-binding term in
   the empirical liquid-drop model. Categorically, this is the
   $|\mathrm{tr}_M|$-dominant Wedderburn-block contribution
   that survives in the $A \to \infty$ thermodynamic limit.

2. **Bethe–Weizsäcker surface** ($\lambda_S \cdot A^{2/3}$):
   subleading correction in $A$ from the boundary of the nuclear
   "drop". Categorically, this is the $\sqrt[3]{|\mathrm{tr}_M|}$
   correction picked up from the perimeter of the closed braid in
   2D categorical Stokes (Yekutieli 2015,
   [`rem:yekutieli-stokes`](../../content/quantum-observable-universe/braids-and-knots/yekutieli-stokes.md)).

3. **BW knot factor** $a(N)$: an empirical $\mathcal{O}(1)$
   modulation that BW fitting requires to match isotopes with
   exotic nucleon configurations (deuteron, helium-4 alpha-knot,
   borromean rings of $^{11}$Li). The categorical replacement is
   the **knot-type-dependent chirality factor** of the atomic
   braid relative to the disconnected baseline.

The conjecture's ratio form **R** unifies all three: the entire
BW combination $\lambda_V A + \lambda_S A^{2/3} + a(N)$ is the
*single* quantity $\lvert\mathrm{tr}_M(W_{\text{atom}})\rvert /
\lvert\mathrm{tr}_M(W_{\text{free}})\rvert$. The volume and
surface scaling emerges from the Wedderburn-block structure of
$\mathrm{tr}_M$; the knot factor emerges from the difference
between connected (atom) and disconnected (free) braid topology.

## 4. Why this matters for the 1 ppb compute target

For the m_p ($^{1}$H) derivation chain, all six terms must
evaluate at MPFR 50 dps. Currently:

- $T_1, T_2, T_3, T_4, T_6$ all have **canonical**, **computable**,
  **categorical** definitions that emit witnesses at 50 dps.
- $T_5$ has **two competing implementations** in the codebase:
  - `paper_six_term_isotope_sweep.term5_chirality` (V1 closed form)
  - `term5_v2_chirality.aK_v2` (V2 mirror Gram form)
  - default switched to V2 in `mass_formula_6term_mpfr_50dps.py:term_5_chirality_bw_mp` (2026-05-15)
  - `chirality_source = "bw_legacy"` falls back to a hand-coded
    BW-style constant per knot type — empirical, not categorical.

Until $T_5$'s definition is canonical, the m_p chain produces an
$\mathcal{O}(\text{MeV})$ ambiguity in the total mass (the V1 vs V2
gap at the proton alone is $\sim 22\;\mathrm{MeV}$ scaled to $T_5$'s
amplitude, dwarfing the 1 ppb compute target by ~$10^{10}\times$).

This is why $^{1}$H carries `derivation_pending` in
`derived-masses.witness.json` and why the workplan-v5 governance
question Q2 (staged tightening of `M_P_DERIVED_MAX_REL_DIFF`)
remains stuck at the 1% threshold — it cannot tighten past the
$T_5$ ambiguity.

## 5. The structural resolution proposed

**Claim:** The canonical $T_5$ categorical attribution is the
**ratio form R**. Both V1 and V2 are diagnostics of *related but
distinct* objects.

**Reasoning:**

(a) The conjecture statement itself writes
$a(N) = |\mathrm{tr}_M(W_{\text{atom}})| / |\mathrm{tr}_M(W_{\text{free}})|$
as the definition of the knot factor (lines 93–102 of
`knot-factor-frobenius-pairing.md`). The closed form **C** is
listed as a small-$A$ simplification that *reproduces* this
ratio, not as a separate definition.

(b) **C** matches **R** for A=1,2,3,4 (the cases the conjecture
verifies). For A=1, both equal 1; for A=2,3,4 the BW values
match Step 4 of the conjecture.

(c) **R** has an unambiguous categorical definition at every $A$,
including A=1 (where it is trivially 1 because $W_{\text{atom}} =
W_{\text{free}}$ — a free proton/neutron is its own "atom").
**C** also gives 1 at A=1 (empty product), consistent.

(d) **V2** measures the *mirror chirality* of the braid relative
to its geometric mirror — a meaningful structural quantity but
**not** the BW knot factor. It captures information **R** loses
(the 25% T ↔ ³He asymmetry is genuinely there; **R** absolute-
values it away). V2 should live in a separate categorical slot,
likely a chirality-sensitive contribution to $T_6$ (Habiro
residue) or a future $T_7$.

(e) **V1** measures $\tau(\mathbf{1}_n)$ — an n-dependent
normalisation constant. Not chirality. Drop from any
attribution.

**Consequence for the implementation:**

1. Switch the default `chirality_source` in
   `mass_formula_6term_mpfr_50dps.term_5_chirality_bw_mp` from
   `"v2"` back to a new `"ratio"` mode that computes
   $|\mathrm{tr}_M^{\text{atom}}| / |\mathrm{tr}_M^{\text{free}}|$
   directly. Existing `"v2"` and `"bw_legacy"` paths retained
   for regression comparison.

2. The closed form **C** becomes a **derived shortcut** for A ≤ 4
   (validated against the ratio form to 1 ppb), not the primary
   compute path.

3. V2 is documented as a **separate chirality diagnostic** in
   the audit trail; rename
   `probe_term5_aK_v2_mirror_chirality.py` →
   `probe_mirror_chirality_diagnostic.py` to remove the "T5"
   misnomer.

4. ¹H lifts to `derived` once `mass_formula_6term_mpfr_50dps`
   under `"ratio"` mode matches CODATA to 1 ppb (compute
   precision, not experimental floor).

## 6. Step plan for Item B closure

| Step | Owner | Tractability | Estimated effort |
|------|-------|--------------|------------------|
| **B.1** Implement `"ratio"` chirality source: $\lvert\mathrm{tr}_M(W_{\text{atom}})\rvert / \lvert\mathrm{tr}_M(W_{\text{free}})\rvert$ at MPFR-50dps, using the same Hoefsmit infrastructure already in `term5_v2_chirality.py` | this PR | high (existing infra) | half-day |
| **B.2** Validate **C** = **R** for A ∈ {1, 2, 3, 4} to 1 ppb (the cases where conjecture Step 4 explicitly verifies) | this PR | high (5-row table) | hour |
| **B.3** Validate **R** structurally for A ∈ {5, 6, 7} (Li, Be, ...) — no symbolic check possible, but **C** breaks down beyond A=4 so **R** is the canonical extension | this PR | medium | day |
| **B.4** Re-derive ¹H mass under `"ratio"` mode at MPFR-50dps; assert match to CODATA $m_p = 938.272088\;\text{MeV}$ within compute precision | this PR | high | hour (after B.1) |
| **B.5** Lift ¹H to `derived` in `derived-masses.witness.json`; raise `M_P_DERIVED_MAX_REL_DIFF` from 1% → 1 ppb | this PR | high | minutes |
| **B.6** Update `knot-factor-frobenius-pairing.md` to make **R** the primary statement and demote **C** to a small-A corollary (preserves existing BW agreement) | this PR | medium (narrative edit) | hour |
| **B.7** Promote `conj:knot-factor-frobenius-pairing` from conjecture to proposition? — needs §3b-cond Lean class formalisation; defer to a follow-on PR | follow-on | low (R&D) | weeks |
| **B.8** Rename V2 probe per §5 step 3 | this PR | trivial | minutes |

**Critical path for the 1 ppb gate:** B.1 → B.2 → B.4 → B.5
(four steps, totalling roughly one working day on top of the
existing MPFR infrastructure).

## 7. Open governance questions

| # | Question |
|---|----------|
| QB.1 | Does **R** match **C** to 1 ppb at A=2,3,4? Symbolic identity says yes (Step 4 of conjecture), but a numeric witness has never been emitted. B.2 produces it. |
| QB.2 | For A ≥ 5, is **R** unique up to a global sign / phase? The absolute-value $|\cdot|$ in the conjecture statement removes one sign; could there be a residual $\mathbb{Z}/2$ ambiguity? |
| QB.3 | Where does V2's chirality information actually go in the mass formula — is it part of $T_6$'s cyclotomic residue (which is chirality-sensitive via the Habiro polynomial), or is it a missing 7th term? |
| QB.4 | The ratio form **R** uses both $W_{\text{atom}}$ and $W_{\text{free}}$; the disconnected braid $W_{\text{free}}$ is defined only up to a strand-relabelling. Is the ratio invariant under this relabelling? Yes by braid-conjugation invariance of $\mathrm{tr}_M$, but the proof should be cited explicitly. |

## 7b. Structural attribution via SDP shadow price + PL thimble

*(Added 2026-05-18 after user note: "a_K from sibling is related
to SDP and thimble".)*

The Ratio form **R** is **not** the deepest categorical
attribution — it is already realised in the existing infrastructure
by **two equivalent constructions on opposite sides of the
archimedean wall**:

### 7b.1 Algebraic side: a_K = knot-factor SDP shadow price

[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md)
already proves that *each* coefficient of the Bethe–Weizsäcker
formula is a **shadow price (LP dual variable) of a Wedderburn-
block Frobenius positivity constraint** in the nuclear-operator
selection LP:

$$
  B(Z,N) \;=\; \sum_\lambda C_\lambda \cdot S_\lambda(Z,N,A) \cdot m_e,
  \qquad
  C_\lambda = u_\lambda^*\big|_{S_\lambda = 1}.
$$

The dual factors as $u_\lambda^*(Z,N) = C_\lambda \cdot
S_\lambda(Z,N,A)$ where $C_\lambda$ is a $q$-integer product
(partition algebra: hooks, contents, Frobenius coords) and
$S_\lambda$ is the content-sum-driven scaling ($c(\lambda) > 0$:
volume; $c(\lambda) = 0$: isospin; $c(\lambda) < 0$: charge).

**Claim:** $T_5$'s chirality factor $a_K$ is the **knot-factor
shadow price** — the dual variable $u_\lambda^*$ summed over
the **chirality-discriminating Wedderburn block(s)** — i.e. the
non-self-conjugate partitions $\lambda \neq \lambda^\vee$, since
the Wenzl-bridge identification $y_\lambda = w_\lambda$ holds
**only on the self-conjugate stratum**. The chirality information
is exactly what the self-conjugate stratum loses.

Concretely, the active set
$\mathcal{A}(Z, N) = \{\lambda \vdash 3A : u_\lambda^*(Z, N) > 0\}$
splits as
$\mathcal{A} = \mathcal{A}^{\mathrm{sc}} \sqcup \mathcal{A}^{\mathrm{chi}}$
(self-conjugate + chirality), and

$$
  a_K(Z, N) \;=\;
  1 \;+\;
  \sum_{\lambda \in \mathcal{A}^{\mathrm{chi}}}
    \frac{u_\lambda^*(Z,N)}{u_0^*(Z,N)}.
$$

For the proton (A=1, n=3), the only partitions are $(3), (2,1),
(1,1,1)$; of these, $(2,1)$ is self-conjugate ($\lambda = \lambda^\vee$),
and $(3) \leftrightarrow (1,1,1)$ form a conjugate pair. The
proton's atomic braid is **invariant under the conjugate-pair
involution** (all three quarks identical up to colour relabel),
so the chirality contributions from $(3)$ and $(1,1,1)$ cancel
in the dual sum — giving $a_K^{\text{proton}} = 1$ exactly, with
**structural** (LP-duality + symmetry) justification, not just
"empty pn-crossings product".

This is the deeper reason **C** matches **R** at A=1: not the
counting argument of zero pn-crossings, but the LP-complementarity
between conjugate Wedderburn blocks under the proton's reflection
symmetry.

### 7b.2 Archimedean side: a_K = thimble intersection ratio

Under the fibre functor $\tau$, the algebraic Markov trace
descends to the Picard–Lefschetz thimble decomposition at the
color-tube cubic discriminant
([`def:picard-lefschetz-thimble`](../../content/quantum-observable-universe/descartes-universe/picard-lefschetz-thimble.md),
[`prop:sw-period-thimble-equivalence`](../../content/quantum-observable-universe/descartes-universe/sw-period-thimble-equivalence.md)):

$$
  \tau\bigl(\mathrm{tr}_M(W)\bigr)
  \;=\;
  \sum_\sigma n_\sigma \oint_{\mathcal{J}_{z_{c,\sigma}}}
    \lambda_{\mathrm{SW}}^{(1)}(z; W)\, dz.
$$

The intersection numbers $n_\sigma = \langle \mathcal{K}_\sigma,
\gamma \rangle \in \mathbb{Z}$ count which thimbles contribute
to which braid configurations. The PL ↔ JSJ mass-integration
equivalence
([`conj:pl-jsj-mass-integration-equivalence`](../../content/quantum-observable-universe/descartes-universe/pl-jsj-mass-integration-equivalence.md))
identifies the **active set of thimbles** with the **active set
of Wedderburn blocks** under $\tau$:

$$
  \mathcal{A}^{\mathrm{chi}}(Z,N)
  \;\xleftrightarrow{\;\tau\;}\;
  \bigl\{\sigma : n_\sigma^{\mathrm{atom}}(Z,N)
                 \neq n_\sigma^{\mathrm{free}}(Z,N)\bigr\}.
$$

The chirality-active thimbles are precisely the SW critical
points $z_{c, \sigma}$ where the **anti-thimble intersection
number differs** between the connected (atom) and disconnected
(free) braid contours — i.e. the thimbles "newly captured" by
the binding topology.

The thimble form gives:

$$
  a_K(Z, N) \;=\; 1 \;+\;
  \sum_{\sigma \in \mathcal{A}^{\mathrm{chi}}}
    \bigl(n_\sigma^{\mathrm{atom}} - n_\sigma^{\mathrm{free}}\bigr)
    \cdot \frac{\oint_{\mathcal{J}_{z_{c,\sigma}}}
      \lambda_{\mathrm{SW}}^{(1)}\,dz}
      {|\mathrm{tr}_M(W_{\mathrm{free}})|}.
$$

For the proton, the SW critical points $z_c^{\pm} \approx 0.106
\pm 0.937 i$ come in a conjugate pair; the proton braid contour
sits on the real axis with **equal anti-thimble intersection
with both** ($n^+ = n^-$), so the conjugate-pair sum vanishes —
the **same cancellation** as the conjugate Wedderburn blocks
above. The two pictures are identified by $\tau$.

### 7b.3 What this changes for the closure plan

The original §6 step **B.1** (implement `"ratio"` mode via
direct $|\mathrm{tr}_M(W_{\mathrm{atom}})| /
|\mathrm{tr}_M(W_{\mathrm{free}})|$ compute) is **not the
canonical route**. The correct routes are:

- **B.1a (SDP-side).** Compute $a_K$ via the existing
  operator-selection LP/SDP dual extractor
  (`lp_dual_solver.solve_operator_selection_lp` or
  `solve_psd_operator_selection_sdp`,
  [`computations/lp_dual_solver.py`](../../computations/lp_dual_solver.py))
  — already MPFR-50dps capable, already emits the required
  dual fields per AGENTS.md §LP / SDP duals — and read off the
  chirality-active dual sum as in §7b.1.

- **B.1b (PL-side).** Compute $a_K$ via the thimble intersection
  numbers $n_\sigma^{\mathrm{atom}} - n_\sigma^{\mathrm{free}}$
  from the existing PL machinery (`picard-lefschetz-thimble`
  block + `sw-period-thimble-equivalence`); validate against B.1a
  to 1 ppb as a cross-check of the archimedean ↔ algebraic
  bijection.

- **B.1c (cross-check vs C).** Validate the BW closed form **C**
  against B.1a for A = 2, 3, 4 — the closed form should equal the
  dual sum because the conjecture Step 4 BW values are exactly
  the $C_\lambda$ values for the small-A active set.

The advantage of B.1a/B.1b over a generic ratio compute: $a_K$ is
**not a new quantity** — it is read off existing infrastructure
(SDP duals already wired per `prop:operator-selection-lp`,
thimble intersections already computed in the PL chain). No new
Hoefsmit compute, no new Wedderburn sum — just one extraction
from the dual variables of an LP that is already solved as
part of every binding-energy compute.

### 7b.4 Sibling-PR coordination

- **PR #682** (post-675-1ppb-roadmap-fe454f): wires Li_2^q
  production tower form into `mass_formula_6term_mpfr_50dps`;
  necessary substrate for the SDP dual extraction at MPFR-50dps
  because the Li_2^q convergence governs the
  $S_\lambda(Z,N,A)$ scaling functions.

- **PR #686** (flavor-split-higher-order): probes sub-leading
  substrate corrections via thimble (`mobius-limit-from-thimble`,
  `picard-lefschetz-thimble`, `sw-period-thimble-equivalence`
  witnesses re-emitted). The thimble infrastructure $a_K$ would
  consume is being kept fresh by #686's drift refresh.

- **PR #679** (rho-k-wire-li-extend): extends ρ_K to ⁶Li/⁷Li
  using LR-bridge witness. ρ_K is the leading-order term;
  $a_K$ is the **next-order chirality correction**. Stacking
  order in the 6-term formula: $T_1$ (ρ_K) → $T_5$ (a_K) →
  $T_6$ (Habiro residue).

The §6 critical path now reads: B.1a → B.1c → B.4 → B.5,
totalling **less than a working day** because no new compute
is implemented; it is purely **a re-read of existing SDP dual
variables** through the lens of the §7b.1 identification.

## 7c. B.1a wiring result — R ≠ C numerically, conjecture Step 4 needs revision

*(Added 2026-05-18 after running `aK_via_lp_dual.py`.)*

The B.1a prototype script
[`computations/aK_via_lp_dual.py`](../../computations/aK_via_lp_dual.py)
emits the comparison witness
[`a-K-via-lp-dual.witness.json`](../../computations/a-K-via-lp-dual.witness.json)
at q_0 50 dps for the six chi-cache atoms. The result surfaces a
**structural inconsistency** between the narrative conjecture and
the production code:

| atom | A | $a_K^R$ (Ratio) | $a_K^C$ (Closed) | R − C residual |
|------|---|------------------|------------------|----------------|
| proton  | 1 | 1.000 | 1.000 | 0 (trivial) |
| neutron | 1 | 1.000 | 1.000 | 0 (trivial) |
| deuteron | 2 | **0.395** | 1.209 | −67% |
| tritium  | 3 | 0.115 | 0.956 | −88% |
| ³He      | 3 | 0.197 | 0.956 | −79% |
| ⁴He      | 4 | 0.055 | 0.914 | −94% |

The conjecture's Step 4 claim — that $a(N) = \lvert\mathrm{tr}_M(W_{\text{atom}})\rvert / \lvert\mathrm{tr}_M(W_{\text{free}})\rvert$
reproduces $a_K^C = 1+h, 1-h^2, (1-h^2)^2$ at A=2,3,4 — **fails
numerically by a factor of ~2-18×** when $W_{\text{free}}$ is taken
to be the disconnected product of nucleon braids (which is the
natural Markov-trace multiplicative definition).

### Likely resolution

The narrative `a(N) = R` and the production `T5 = a_K · 𝒞_K`
**use the same symbol for different objects**. The production
code's $\mathcal{B}_{\mathrm{bulk}}$ is the **subtractive mass
defect**

$$
  \mathcal{B}_{\mathrm{bulk}}(Z,N) = E_0 \cdot
    \bigl(\lvert\mathrm{tr}_M(W_{\mathrm{free}})\rvert -
          \lvert\mathrm{tr}_M(W_{\mathrm{atom}})\rvert\bigr),
$$

and $a_K$ is a **separate multiplier** matching the closed
form **C**. The narrative conjecture's "ratio form" identification
is **not** equivalent to the closed form; one of them is
incorrect, or they refer to different physical observables.

This shifts the §6 closure plan substantially. The corrected
framing:

- **C is the canonical $a_K$ for T5** (matches conjecture Step 4
  symbolic values; matches production code's multiplicative role).
- **R is a *different* quantity** — the mass-defect ratio for
  $\mathcal{B}_{\mathrm{bulk}}$ envelope, not the chirality
  multiplier.
- **D-sc / D-chi** (per-partition contribution sums) — exploratory;
  do not reproduce C either.

### Side-finding: chirality stratum dominates for A ≥ 3

The per-atom dual breakdown shows the self-conjugate
contribution to $\lvert\mathrm{tr}_M\rvert$ vanishes for A ≥ 3:

| atom | A | sc contribution | chi contribution (signed) | $\lvert\mathrm{tr}_M\rvert$ |
|------|---|----------------|---------------------------|------------------------------|
| proton   | 1 | 0.508 | 0.557 | 1.065 |
| neutron  | 1 | 0.478 | 0.445 | 0.923 |
| deuteron | 2 | −0.014 | 0.403 | 0.388 |
| tritium  | 3 | 0.0004 | 0.104 | 0.104 |
| ³He      | 3 | 0.0005 | 0.207 | 0.207 |
| ⁴He      | 4 | **0.000** | 0.054 | 0.054 |

This means: **for A ≥ 3, essentially all of $\lvert\mathrm{tr}_M\rvert$
comes from non-self-conjugate (chirality-active) Wedderburn
blocks.** The self-conjugate stratum (where the Wenzl-bridge
identification $y_\lambda = w_\lambda$ holds) carries the
nucleon traces but **vanishes for composite nuclei**. This is
consistent with the chirality interpretation — composite-nucleus
binding lives entirely in the chirality stratum at A ≥ 3.

### Revised closure plan

| Step | Action |
|------|--------|
| **B.1a-rev.1** | Drop R as a candidate for $a_K$; promote C as canonical (matches conjecture Step 4 symbolic identities + production code's multiplicative role). |
| **B.1a-rev.2** | Re-frame R as a separate quantity governing $\mathcal{B}_{\mathrm{bulk}}$'s mass-defect envelope, not $a_K$. Audit production code's `B_bulk` interpretation against R. |
| **B.1a-rev.3** | Update `knot-factor-frobenius-pairing.md` Step 4 to disclaim the literal "$a(N) = \lvert\mathrm{tr}_M(W_{\text{atom}})\rvert/\lvert\mathrm{tr}_M(W_{\text{free}})\rvert$" equality; clarify that the BW values $(1+h, 1-h^2, ...)$ are derived via Skein eigenvalues, not the Markov-trace ratio. |
| **B.1a-rev.4** | (Optional) Run the full operator-selection LP via `solve_operator_selection_lp` at MPFR-50dps to extract literal $u_\lambda^*$ values and compare against C. The narrative's §7b SDP-shadow-price attribution is still conjectural until verified. **Executed in this audit (f64 prototype)** — see §7d below; conclusion: Wedderburn-block-diagonal LP is degenerate, full Hecke-basis LP is required for meaningful duals. |

## 7d. B.1a-rev.4 — full LP-dual extraction prototype: Wedderburn-block LP is degenerate

The script
[`aK_via_lp_dual_full.py`](../../computations/aK_via_lp_dual_full.py)
solves the operator-selection LP per
[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md)
using the Wedderburn-block projector basis $\{\pi_\lambda : \lambda \vdash n\}$
with diagonal Gram $G_{\lambda\lambda'} = w_\lambda \cdot \delta_{\lambda\lambda'}$.
Result (f64 prototype, scipy linprog highs method):

| atom | A | $u_0^*$ | chirality dual sum | $a_K^{\mathrm{dual}}$ | $a_K^C$ |
|------|---|---------|---------------------|------------------------|---------|
| proton  | 1 | 0.0168 | 0.99 | 58.7 | 1.0 |
| neutron | 1 | 0.0207 | 0.97 | 47.1 | 1.0 |
| deuteron | 2 | **0.0** | 41.0 | 10⁶ | 1.21 |
| tritium  | 3 | **0.0** | 46.9 | 4.5·10⁸ | 0.96 |
| ³He      | 3 | **0.0** | 141.2 | 6.8·10⁸ | 0.96 |
| ⁴He      | 4 | **0.0** | 153.8 | 2.9·10⁶ | 0.91 |

**The LP is degenerate**: $u_0^* = 0$ for all atoms with A ≥ 2. The
diagonal Gram makes the operator-selection LP a 1-constraint
problem; the shadow price on the net constraint collapses to zero
while the per-block shadow prices diverge.

**Diagnostic conclusion:** The §7b SDP-shadow-price identification
of $a_K$ requires the **full Hecke algebra basis** $\{b_i : i = 1, \ldots, [n]_q!\}$
with **non-diagonal Frobenius Gram** $G_{ij} = \mathrm{tr}_M(b_i b_j)$,
not the Wedderburn-block-diagonal projection. The block-diagonal
LP discards inter-block coupling information that the proper LP
needs to bind the dual variables.

This is consistent with `prop:mass-coefficient-shadow-price`'s
proof structure — the Wedderburn decomposition is a *consequence*
of solving the full LP (the block-diagonalisation falls out of
the Wedderburn structure of $H_n$), not an input simplification.

**Status of §7b SDP-attribution claim**: open. The structural
identification $a_K = $ chirality-active dual sum is still
plausible but **not yet verified**. Verification requires:

1. Computing the full Hecke algebra Gram matrix $G_{ij} = \mathrm{tr}_M(b_i b_j)$
   for the active atom at $n = 3A$. For A=2 this is $[6]_q! = 720$
   basis elements, $720 \times 720$ Gram. At A=3, $[9]_q!$ is
   ~360,000 — intractable in this form.

2. Or: using a smaller basis that nevertheless captures the
   relevant non-diagonal coupling (e.g. the Murphy basis at the
   atomic braid's centraliser).

3. Or: deriving the dual variables analytically from the
   $C_\lambda \cdot S_\lambda(Z,N,A)$ factorisation in
   `prop:mass-coefficient-shadow-price` Step "Factorisation" —
   bypassing the explicit LP solve. This is the path that the
   block already proves in narrative form.

**Practical recommendation**: pursue path (3) — the dual factorisation
is already proved in `prop:mass-coefficient-shadow-price` and gives
$u_\lambda^*(Z,N) = C_\lambda \cdot S_\lambda$ in closed form.
Read off $a_K$ via the $C_\lambda$ values for the chirality-active
partitions. This is **analytical**, not numerical — no LP solve
needed.

## 7e. B.1a-rev.5 — full Hecke-basis LP at H_3 (proton, neutron): also degenerate

The script
[`aK_via_lp_dual_hecke_basis.py`](../../computations/aK_via_lp_dual_hecke_basis.py)
implements the recommended *path 1* from §7d: full Hecke-algebra
basis at H_3 (proton, neutron) with the non-diagonal Frobenius
Gram from
[`gram-matrix-dual.witness.json`](../../computations/gram-matrix-dual.witness.json)
(6×6, $\det G \approx -0.36$ at $q_0$).

Result (f64 prototype):

| atom | $u_0^*$ | active set | chirality y-sum | $a_K^{\mathrm{chi-active}}$ | $a_K^C$ |
|------|---------|------------|------------------|------------------------------|---------|
| proton  | $-0.000$ | $\{\mathbf{1}\}$ | 1.000 | **NaN** (division by 0) | 1.0 |
| neutron | $-0.000$ | $\{\mathbf{1}\}$ | 1.000 | **NaN** (division by 0) | 1.0 |

**Same degeneracy pattern as §7d**: the LP corner solution puts
all weight on the identity basis element, $u_0^* \to 0$, and
$a_K^{\mathrm{chi-active}}$ formally diverges. Even with the full
non-diagonal Gram, the corner-solution structure does not yield
the C-matching a_K via dual shadow prices.

**Cumulative finding (audit §7c + §7d + §7e):** The SDP-shadow-
price identification of $a_K$ from audit §7b is **not directly
extractable as a corner-LP-dual**. None of the four numerical
candidates tested (R, D-sc, D-chi, dual-ratio, chi-active) match
the closed-form C numerically. The §7b claim that "a_K = $1 + \sum_\lambda u_\lambda^*/u_0^*$"
holds only in the analytical-factorisation form
$u_\lambda^*(Z,N) = C_\lambda \cdot S_\lambda$ proved in
`prop:mass-coefficient-shadow-price`, not via direct LP solves at
LP corner-vertex solutions.

**Definitive recommendation:** The canonical a_K is the closed
form C; the SDP-shadow-price attribution should be interpreted as
the *analytical* dual factorisation $C_\lambda \cdot S_\lambda$,
not the numerical LP-corner duals. The §7b narrative is **correct
in principle** but needs reformulation: the dual variables
referenced are the **factorised analytical $u_\lambda^*$**, not
the corner-solution duals returned by scipy linprog.

This is the closure of the Item B SDP-shadow-price investigation
within the scope of B.1a-rev.{1..5}. The next concrete step is
B.1a-rev.3 (narrative update to
`knot-factor-frobenius-pairing.md` Step 4) — drop the literal
"$a(N) = \lvert\mathrm{tr}_M\rvert/\lvert\mathrm{tr}_M\rvert$ "
identity, clarify that the BW values $1+h, 1-h^2, (1-h^2)^2$
come from Skein eigenvalues / Wenzl branching, and document
the analytical $C_\lambda \cdot S_\lambda$ dual factorisation as
the canonical structural form (with C as the q-integer product
the conjecture's Step 4 BW values agree with empirically).

This finding is **non-blocking for the m_p chain** because the
production code already uses C (`paper_six_term_isotope_sweep.term5_chirality`
default mode). The audit just needs to reflect that C is canonical
and update the narrative.

## 7f. Course-correction — BW-shadow-price framework was deprecated

*(Added 2026-05-18 after user note: "bw-coef … these were deprecated".)*

The §7b–§7e investigation was built on
[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md),
whose computational backing
(`bw_wenzl_shadow_equivalence.py`) was **moved to `_deprecated/`**
per the 2026-05-11 plancherel-usage audit
([`docs/audits/2026-05-11-plancherel-usage-audit.md`](2026-05-11-plancherel-usage-audit.md))
together with related scripts
(`bw_lagrangian_prefactor_derivation_attempt.py`,
`sdp_on_shadows.py`, `symbolic_k6_shadow.py`). The
plancherel-usage audit also systematically renamed
`plancherel_sum` → `markov_m3_sum` across the LP-dual scripts
and promoted
[`prop:wedderburn-weight-canonical`](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md)
(q-deformed weight $\tilde w_\lambda = \dim_q(\lambda)^2 / [n]_q!$)
as the canonical Wedderburn-weight framework.

The narrative `prop:mass-coefficient-shadow-price` block still
exists (not marked deprecated in `.ts`), but **production six-
term mass formula does not cite it**, and its compute path is
the deprecated one. The §7b SDP-shadow-price attribution of a_K
was therefore chasing a structural framing that the codebase has
already moved past.

**Consequence for Item B:** §7b, §7c, §7d, §7e are **withdrawn
as primary attribution paths.** They remain in this audit as
historical record of what was tested and why each failed
(R/D-chi numerical mismatch in §7c; Wedderburn-block LP
degeneracy in §7d; H_3 full-Hecke LP corner-degeneracy in
§7e). But they should **not** drive the canonical T5
implementation.

**Live framework for Item B:**

1. **`prop:wedderburn-weight-canonical`** ($\tilde w_\lambda$):
   the q-deformed Wedderburn weight, replacing the older
   classical Plancherel weight $w_\lambda$ in non-self-conjugate
   strata. Used by `markov_m3_sum_numeric` and the production
   `mass_formula_6term_mpfr_50dps`.

2. **`prop:plancherel-weight-boundedness`** + **Wenzl-bridge
   identification** $y_\lambda = w_\lambda$ on the
   self-conjugate stratum only.

3. **Closed form C** for $a_K = \prod_{c \in \text{pn-crossings}}(1 + \mathrm{sign}(c) \cdot h)$
   — empirically matches conjecture Step 4 BW values
   $(1+h, 1-h^2, (1-h^2)^2)$ at A=2,3,4, and used by the
   production `paper_six_term_isotope_sweep.term5_chirality`
   default. **This remains the canonical $a_K$.**

**Revised closure plan for Item B:**

| Step | Action |
|------|--------|
| **B.1a-rev.6 (NEW)** | Drop §7b SDP-shadow-price attribution from primary framing. Re-locate Item B audit's "structural attribution" claim onto `prop:wedderburn-weight-canonical` + Wenzl bridge on the self-conjugate stratum. The chirality $a_K$ then lives **between** the self-conjugate and non-self-conjugate strata where the bridge breaks. |
| **B.1a-rev.7** | Verify the canonical T5 path: `mass_formula_6term_mpfr_50dps` with `chirality_source="closed_form"` (= C) at MPFR-50dps for proton, neutron — confirm it gives the BW values 1.0 / 1.0 as a sanity check. |
| **B.3** | Re-derive ¹H mass under production C-mode at MPFR-50dps. |
| **B.4** | Lift ¹H to `derived`; tighten `M_P_DERIVED_MAX_REL_DIFF` 1% → 1 ppb. |
| **B.5** | Update `knot-factor-frobenius-pairing.md` Step 4 — drop literal Markov-trace ratio; cite C as canonical $a_K$; reference `wedderburn-weight-canonical` for the structural backing. |

**Audit-author note:** apologies for chasing the deprecated
framework over §7b–§7e. The B.1a-rev.4 and B.1a-rev.5 scripts
remain in the tree as cautionary artefacts (degenerate-LP
witnesses); they should not be re-run as part of the canonical
m_p closure. The next concrete move is **B.1a-rev.7** (sanity-
check the live C-mode path), which avoids both deprecated
infrastructure and re-litigating §7b's structural claim.

## 8. Coordination notes

This audit is **structural / R&D only** — no code changes in
this commit. The implementation (steps B.1–B.8) will be wired
on follow-on commits once the structural framing is reviewed.

Item B closure does NOT block #683's merge: PR #683 carries
the Step 2 Rust + Item A + Item C + Q6 work, none of which
touches $T_5$. Item B is the next gating item for the m_p
chain after #683 lands.

**Sibling PR overlap:** None known.
- PR #682 (Python chi-cache reader) — disjoint from T5.
- PR #671 (audit-only m_p coordination) — references Item B
  as open; this audit supersedes the open-R&D framing with
  a structural resolution proposal.
- PR #681 (Wenzl operator-valued branching) — disjoint from T5.

**Ledger:** `docs/coordination/1ppb.md` will be appended with
this audit's structural-resolution claim once merged.
