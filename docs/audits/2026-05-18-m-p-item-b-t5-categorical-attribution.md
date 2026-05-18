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

[`prop:bw-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/bw-coefficient-shadow-price.md)
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
  [`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py))
  — already MPFR-50dps capable, already emits the required
  dual fields per CLAUDE.md §LP / SDP duals — and read off the
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
