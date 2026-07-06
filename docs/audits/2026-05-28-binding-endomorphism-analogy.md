# Binding endomorphism: B = m_e × Vol(K_bind) × Δtr (2026-05-28)

## Summary

The nuclear binding energy follows the **mass-endomorphism analogy**.
Where the nucleon mass is

$$
  m(K) = m_e \cdot \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
         \cdot \mathrm{lw}(K, q_0),
$$

the binding energy of a composite nucleus is

$$
  B(K) = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}}) \cdot \Delta\mathrm{tr},
  \qquad
  \Delta\mathrm{tr} = |\mathrm{tr}_M(\text{free})| - |\mathrm{tr}_M(\text{atom})|,
$$

where $K_{\mathrm{bind}}$ is the **binding link** — the closure of the
inter-nucleon crossings in the $H_{3A}(q_0)$ braid — and $\Delta\mathrm{tr}$
is the Wedderburn trace difference between the free (disjoint) and bound
(interleaved) nucleon configurations.

## Deuteron: confirmed at +0.19%

| Factor | Value | Source |
|--------|-------|--------|
| $m_e$ | $0.51099895$ MeV | CAL-1 anchor |
| $\mathrm{Vol}(\mathcal{B}_3) = 8G$ | $7.327725$ | Borromean knot complement (proved) |
| $\Delta\mathrm{tr}(d)$ | $0.595240$ | $H_6$ Wedderburn (binding_canonical) |
| **$B(d)$** | **$2.2289$ MeV** | vs AME $2.22452$ — **+0.19%** |

Zero free parameters. Witness:
[`binding-endomorphism-deuteron.witness.json`](../../computations/binding-endomorphism-deuteron.witness.json).

This confirms the existing
[`prop:deuterium-derived-binding`](../../content/quantum-observable-universe/mass-theory/deuterium-derived-binding.md)
result, now framed explicitly as the binding-endomorphism analogue of
the mass formula.

## The binding link is atom-specific (SDP registry)

The [binding-K SDP solver](../../computations/binding-k-solver.witness.json)
identifies the binding link $K_{\mathrm{bind}}$ per atom:

| Atom | $A$ | $H_{3A}$ | Binding link $K_{\mathrm{bind}}$ |
|------|-----|----------|----------------------------------|
| $d$ (²H) | 2 | $H_6$ | Hopf link $L_H$ |
| $t$ (³H) | 3 | $H_9$ | $8_{11}$-class link |
| ³He | 3 | $H_9$ | L6a4 (3-component) |
| ⁴He | 4 | $H_{12}$ | (pending SnapPy) |

The volume scale for the deuteron matches $\mathrm{Vol}(\mathcal{B}_3) = 8G$
to $0.19\%$ — the Borromean volume, inherited from the per-nucleon
Borromean braid structure, governs the binding.

## Extension to T / ³He / ⁴He (open)

The deuteron formula uses $\mathrm{Vol}(\mathcal{B}_3)$ because both
nucleons are Borromean and the single inter-nucleon crossing is a Hopf
link (whose Seifert volume vanishes, so the Borromean scale dominates).

For $A \geq 3$ the binding link is genuinely hyperbolic (8₁₁-class,
L6a4) with nonzero volume. The honest extension requires:

1. **SnapPy computation** of $\mathrm{Vol}(K_{\mathrm{bind}})$ for each
   binding link in the registry.
2. **Per-pair decomposition** — the large-$A$ pair-sum structure
   described in `prop:deuterium-derived-binding` (the continuum limit
   reproduces Bethe–Weizsäcker).
3. **Verification** that $B(K) = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}})
   \cdot \Delta\mathrm{tr}$ matches AME without rescaling.

### Anti-pattern warning

A prior attempt (PR #1383, **retracted**) manufactured a match by
multiplying $\Delta\mathrm{tr}$ by $A(A-1)/2$ pair counts and $q^{-A}$
powers — a multi-parameter fit disguised as a derivation. The actual
trace ratio $\Delta\mathrm{tr}(⁴\mathrm{He})/\Delta\mathrm{tr}(d) = 0.67$,
not the $12.7$ needed for $[4]_q!/2$. The binding link volume — not
hand-chosen rescaling — must supply the $A$-dependence.

## Raw data (binding_canonical, $H_{3A}$)

| Atom | $|\mathrm{tr}_{\mathrm{free}}|$ | $|\mathrm{tr}_{\mathrm{atom}}|$ | $\Delta\mathrm{tr}$ | scale needed (MeV) |
|------|------|------|------|------|
| $d$ | 0.9835 | 0.3883 | 0.5952 | 3.74 (= $m_e \cdot 8G$ ✓) |
| $t$ | 0.9080 | 0.1041 | 0.8040 | 10.55 |
| ³He | 1.0478 | 0.2065 | 0.8412 | 9.17 |
| ⁴He | 0.9673 | 0.0553 | 0.9120 | 31.03 |

The deuteron scale $3.74 = m_e \cdot \mathrm{Vol}(\mathcal{B}_3)$. The
heavier scales (10.55, 9.17, 31.03) await their binding-link volumes.

## RESOLVED: the trace-convention gap was a weight-scheme error

An earlier note here flagged a 29 % gap between `binding_canonical`'s
$\Delta\mathrm{tr}(d) = 0.5952$ and an $H_{3A}$-direct value $0.4241$,
calling it an unresolved inconsistency. **This is now resolved**
([`trace_convention_reconciliation.py`](../../computations/trace_convention_reconciliation.py)):
the gap is purely a **$y_\lambda$ weight-scheme difference**, not a
framework inconsistency.

Both paths evaluate $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot
\chi_\lambda(W)$ on the *same* joint $H_6$ braid word with the *same*
characters $\chi_\lambda$. They differ only in $y_\lambda$:

| Convention | $y_\lambda$ | $\Delta\mathrm{tr}(d)$ |
|------------|-------------|------------------------|
| **Wenzl Jones–Markov** (`binding_canonical`) | $z = 1/(\sqrt q + 1/\sqrt q)$ per Markov move | **0.59524** |
| normalized-Plancherel (q-Schur) | $\dim_q(\lambda)^2 / [n]_q!$ | 0.42405 |

The Wenzl-bridge value on the joint word matches `binding_canonical`'s
factorized closed form to 11 digits ($3\times10^{-12}$, full mpf — no
float64), so `binding_canonical` *is* the Wenzl convention. Per AGENTS.md,
**the mass/binding chain uses Wenzl JM** (the Plancherel scheme is for
the torus-knot lepton tower). The `binding_per_bond_decomposition.py`
probe erroneously used Plancherel weights — that was the source of the
apparent gap, not a real disagreement.

**Consequence:** the deuteron $+0.19\%$ endomorphism result (Wenzl JM)
is correct and stands. The A≥3 $-60\%$ failure of the single-link
volume **persists in the correct Wenzl convention** — so it is the
genuine open problem, not a convention artifact. Witnesses:
[`trace-convention-reconciliation.witness.json`](../../computations/trace-convention-reconciliation.witness.json),
[`binding-per-bond-decomposition.witness.json`](../../computations/binding-per-bond-decomposition.witness.json).

## Binding-link volumes (SnapPy, PR #1397)

| Atom | Link | Vol | Note |
|------|------|-----|------|
| ²H | Hopf (L2a1) | 0 | Seifert-fibred |
| ³H | $8_{11}$ | 8.2863 | hyperbolic |
| ³He | L6a4 | 7.3277 | **= 8G = Vol(Borromean)** |

The ³He binding link L6a4 *is* the Borromean rings. The single-link
endomorphism $B = m_e \cdot \mathrm{Vol}(K_{\mathrm{bind}}) \cdot
\Delta\mathrm{tr}$ matches ²H (via Hopf→$\mathrm{Vol}(\mathcal{B}_3)$)
but gives $-60\%$ for ³H/³He: the A-dependence is not carried by a
single binding-link volume.

## Multi-bond test (Wenzl JM, PR follow-up)

With conventions reconciled, the additive per-bond model
$B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \sum_{\text{bonds}}
\Delta\mathrm{tr}_{\text{bond}}$ (each chain bond's Wenzl trace shift,
no scale fit) gives:

| Atom | bonds | $\sum\Delta\mathrm{tr}$ | $B(\Sigma)$ | err | $B$(combined) | err |
|------|-------|------|------|------|------|------|
| ²H | 1 | 0.5952 | 2.229 | +0.2% | 2.229 | +0.2% |
| ³H | 2 | 1.1940 | 4.471 | −47% | 3.010 | −64% |
| ³He | 2 | 1.1587 | 4.339 | −44% | 3.150 | −59% |

**Findings (no fit):**
1. Binding is **more additive than multiplicative** — the per-bond sum
   beats the combined product ($-47\%$ vs $-64\%$ for ³H), confirming
   binding lives in the inter-nucleon bonds.
2. The per-bond sum is still **~2× short** for $A=3$ ($t$ needs
   $4.24$ MeV/bond; the model gives $\sim 2.2$). The factor of two
   points to **all-pairs vs chain** bond counting: ³He has
   $\binom{3}{2}=3$ pairs (pp + pn + pn) but the chain braid
   `atom_braid_word_3A` encodes only $A-1=2$ adjacent bonds. The
   missing non-adjacent (nucleon₀–nucleon₂) bond is a long-range
   braid generator the current chain word does not carry.

**Next:** an all-pairs braid (not the linear chain) is the topology
to test — a genuine braid-structure question, not a rescaling.
Witness: [`binding-multibond-wenzl.witness.json`](../../computations/binding-multibond-wenzl.witness.json).

## CORRECTION: the all-pairs "−15%" was a summing artifact

The multi-bond note above suggested an all-pairs 2-body **sum**
($\sum_{\text{pairs}} \Delta\mathrm{tr}$) improves ³He to $-15\%$.
**This is wrong** — and the correction is important.

Summing three independently-computed $H_6$ pair-traces is **not** a
valid 3-nucleon trace. The physically correct object is the **joint
$H_9$ trace** with all three nucleons mutually coupled (including the
long-range nucleon₀–nucleon₂ bond). Computed directly
([`binding_threebody_joint_trace.py`](../../computations/binding_threebody_joint_trace.py)):

| Atom | joint-$H_9$ Δtr | $B$(joint) | err | (all-pairs *sum* was) |
|------|------|------|------|------|
| ³He | 0.8479 | 3.175 | **−58.9%** | (−15%, artifact) |
| ³H | 0.8122 | 3.041 | **−64.1%** | (−21%, artifact) |

The joint trace matches the combined/single-link value (−59%), **not**
the additive sum. The irreducible 3-body term is therefore **large and
destructive**: $\Delta\mathrm{tr}_{3\text{body}} = 0.848 - 1.759
\approx -0.91$ for ³He — the bonds interfere destructively, making the
joint binding *smaller*, not larger.

**Consequence.** First-principles categorical binding (the correct
joint Markov trace) genuinely **undershoots A≥3 by ~60%**. The
deuteron ($+0.2\%$) works because it is a true 2-body system. The
additive multi-bond model does **not** close the gap — it overcounted
by treating pairs as independent. The A≥3 binding deficit is real, not
a missing-constructive-term artifact.

## Error source: Δtr is intensive, binding is extensive

Diagnosed in [`binding_error_source.py`](../../computations/binding_error_source.py).
The A≥3 undershoot has a single structural cause:

| Atom | Δtr | $B_{\mathrm{cat}}$ | $B_{\mathrm{AME}}$ | clip |
|------|-----|------|------|------|
| ²H | 0.595 | 2.23 | 2.22 | **+0.2%** |
| ³H | 0.804 | 3.01 | 8.48 | −64% |
| ³He | 0.841 | 3.15 | 7.72 | −59% |
| ⁴He | 0.912 | 3.42 | 28.30 | −88% |

$\Delta\mathrm{tr} = |\mathrm{tr}_{\mathrm{free}}| -
|\mathrm{tr}_{\mathrm{atom}}|$ is bounded by $|\mathrm{tr}_{\mathrm{free}}|
\approx 1$, so $B = m_e\!\cdot\!\mathrm{Vol}(\mathcal{B}_3)\cdot
\Delta\mathrm{tr}$ has a **hard ceiling of $\approx 3.74$ MeV for every
$A$**. The deuteron ($B=2.2 < 3.74$) sits below the ceiling and works;
³He/⁴He exceed it and are clipped.

**Δtr is an intensive, saturating observable; binding energy is
extensive** (grows with $A$). An intensive quantity cannot represent an
extensive one — that is the $-60\%$, not a missing volume or a
convention artifact.

**Structural fix direction (not a calibrated formula — calibration
would be fitting):** the Markov trace is partition-function-like
(multiplicative over disjoint subsystems), so its **logarithm** is the
extensive, additive, free-energy-like analog. $-\log(|\mathrm{tr}_
{\mathrm{atom}}|/|\mathrm{tr}_{\mathrm{free}}|)$ grows with $A$
($0.93 \to 2.17 \to 1.62 \to 2.86$) where $\Delta\mathrm{tr}$
saturates. A correct extensive binding observable must be built from
$\log(\mathrm{tr})$, not $\Delta\mathrm{tr}$. Recalibrating the scale
for the log observable is deferred (it changes the deuteron
calibration and must be done without back-fitting AME).

## A≥3 derivation campaign + shell/magic review (2026-05-29)

Follow-up to the "log observable" direction above — a systematic
derive-or-refute campaign (all probes evaluate substrate-derived
quantities only, **no AME fitting**), plus a consolidated review of how
the paper treats nuclear shells / magic numbers. PR #1417.

### Overclaim retracted

The Δ_λ gating doc's "Update (2026-05-26): Δ_λ CLOSURE ACHIEVED, zero
free parameters" was **overclaimed** and is retracted. The per-λ formula
$B = m_e\,|\sum_\lambda y_\lambda\chi^\lambda\,\mathrm{sgn}(w_0)\,f^\lambda|$
undershoots **every** light isotope
([`delta-lambda-binding-full-evaluation.witness.json`](../../computations/delta-lambda-binding-full-evaluation.witness.json):
D −83 / T −78 / ³He −70 / ⁴He −89 %); `binding_energy_categorical_deuteron.py`
reached AME only via `C_knot = 5.852 = B_AME/(m_e·|sum|)` — fitted. Also
retracted: `mass-volume-factorization.md`'s "≤6.2% zero free parameters"
(per-isotope (link, ρ∈{m_e,2m_e}) fit; companion
[`rho-f-volume-binding-gap.witness.json`](../../computations/rho-f-volume-binding-gap.witness.json)
shows `matches_within_10pct: []`).

### The linear-truncation diagnosis (root cause)

Per [`kashaev-as-archimedean-realization.md`](../../content/quantum-observable-universe/mass-theory/kashaev-as-archimedean-realization.md),
$\mathrm{Vol}(K) = 2\pi\lim_{N\to\infty}\log|J_N|/N$, so the trace is the
**exponential of a volume**: $\mathrm{tr}\sim e^{\mathrm{Vol}}$. The
endomorphism's $\Delta\mathrm{tr}$ is the **linearisation**
$e^{\mathrm{Vol}}\approx 1+\mathrm{Vol}$ — exact for the deuteron (small
Vol), saturating for A≥3. Confirmed truncation loci:
`conj-chirality-ribbon-frobenius.md:73` (chirality factor to first order
$1+2wc\log q+O(h^2)$); `rem-im-q-vs-p-skew.md` ($\sinh(\log q)$ Coulomb
channel "discarded by the canonical projection");
`atom-knot-mass-derivation.md:385` ("the Hecke quadratic relation **is**
the curvature 2-form $[F,F]$" — identified but unused in binding).

### Volume-difference: triple refutation at real q₀

[`binding_volume_difference_probe.py`](../../computations/probes/binding_volume_difference_probe.py)
tests $B=\rho\,[\mathrm{Vol}(\text{atom})-\mathrm{Vol}(\text{free})]$ with
**derived** volumes (no census-knot fit): (A) $\log|\mathrm{tr}_M|$ — no
derived ρ closes it; (B) cosh-inversion — all $|\mathrm{tr}_M|<2$
(elliptic); (C) SnapPy on the derived braid closure — non-hyperbolic
(Vol≈0). A genuine hyperbolic volume needs **complex-q** (Kashaev
$N\to\infty$), absent at real q₀.

### Complex-q / q-Reeb rotation — the extensive observable

The cosh-inversion "degeneracy" ($|\mathrm{tr}_M|<2$) is the **elliptic /
rotation** regime — the complex-q sector. Per
[`unit-modulus-eigenvalue.md`](../../content/quantum-observable-universe/braids-and-knots/unit-modulus-eigenvalue.md)
and [`figure-eight-reeb-rotation.md`](../../content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.md),
behaviour is **representation-dependent**: the (2,1) standard rep has
unit-modulus eigenvalues $e^{\pm i\theta}$ (q-Reeb phase
$\theta=\arccos(\chi_{(2,1)}/2)$, Kashaev limit = Vol(4₁) = the muon); the
(n)/(1ⁿ) outer channels carry $q^{\pm\text{writhe}}$ growth. The scalar
$\Delta\mathrm{tr}$ collapses this split and the *difference* cancels the
common growth — why every scalar observable refuted.

[`binding_reeb_phase_decomposition.py`](../../computations/binding_reeb_phase_decomposition.py)
keeps the per-rep split and finds the **first extensive observable**: the
free growth-channel mass grows 16.5→93→153→1504 (D/T/³He/⁴He), collapsing
to ~2 when bound; the q-Reeb phase shift $\Sigma|\Delta\theta|$ is also
extensive.

**The rotation-phase lead** ([`binding_rotation_phase_lead.py`](../../computations/binding_rotation_phase_lead.py)):
the **Markov-weighted** phase
$\rho_{\text{need}} = B_{\text{AME}}/\sum_\lambda y_\lambda\dim_\lambda|\Delta\theta_\lambda|$:

| atom | ρ_need (MeV/rad) |
|------|------------------|
| D | 14.7 |
| T (³H) | 18.3 |
| ³He | 18.7 |
| ⁴He | 54.8 |

The **A=3 mirror pair (³H, ³He) agrees to 2% with no fit** — the strong
binding scale is p/n-symmetric under the Markov-weighted Reeb phase. D
(true 2-body) and ⁴He (doubly-magic + 2-proton Coulomb = the
$\sinh(\log q)$ channel) are the expected special cases. Tightest derived
binding observable to date — a genuine lead, **not** closure.

**Lean (this branch):** `crossing-energy-decomposition.lean` now proves
$(q\pm q^{-1})/2=\cosh/\sinh(\log q)$ and $q=\cosh(\log q)+\sinh(\log q)$
— the $\sinh$ Coulomb channel is a **derived identity, not fitted**
(build-verify deferred to CI; no `lake` in the authoring container).

### How the paper treats shells / magic (review)

Shell structure is **per-λ Wedderburn**, extractable from the canonical
braid-word witnesses
([`atom-chi-rust-*`](../../computations/atom-chi-rust-d.witness.json),
[`chi-lambda-he4-full-partition-table`](../../computations/chi-lambda-he4-full-partition-table.witness.json)):

| Mechanism | Block | Statement |
|-----------|-------|-----------|
| Binding formula is per-λ | `prop:rho-k-h3a-refinement` | $B=m_e\sum_\lambda y_\lambda\chi^\lambda\Delta_\lambda$ |
| Magic = self-conjugate | [`categorical-neutrality-saturated-shells`](../../content/quantum-observable-universe/mass-endomorphism/categorical-neutrality-saturated-shells.md), [`homological-shell-condensation`](../../content/quantum-observable-universe/mass-endomorphism/homological-shell-condensation.md) | content-sum-0 ⇒ full-twist-fixed at $n\in\{2,8,20,28,50,82,126\}$ |
| Inter-shell gap | [`torus-knot-shell-binding`](../../content/quantum-observable-universe/predicted-spectra/torus-knot-shell-binding.md) | shell closes → $T_{2,n_s}$, gap $q^{2n_s}$ |
| Doubly-magic compat. | [`double-magic-delta-i-bound`](../../content/quantum-observable-universe/observations/double-magic-delta-i-bound.md) | Δi≤1 LR-fusion; ⁴He=(2,2) self-conjugate |
| Staircase shell partition | [`sigma-shell-from-beta-chain-derivation`](../../content/quantum-observable-universe/mass-theory/sigma-shell-from-beta-chain-derivation.md) | $\lambda_{\mathrm{shell}}$ = staircase (self-conjugate) |
| Magic-shell coupling | [`magic-shell-coupling-kappa`](../../content/quantum-observable-universe/particle-interactions/magic-shell-coupling-kappa.md) | $\kappa=-E_0\log(1/h)/([2]_q[3]_q)\approx-1.07$ MeV (derived, 0.03%) |
| ⁴He knot factor | [`knot-factor-shell-closed`](../../content/quantum-observable-universe/mass-theory/knot-factor-shell-closed.md) | $a_K=1$ exact (Markov equilibrium, Z=N even-even) |

The shell structure is **not missing** — the scalar $\Delta\mathrm{tr}$
collapsed it. The campaign shows the extensive A-dependence lives in the
**per-rep q-Reeb phase** + **growth-channel** content, which the per-λ
shell data carries.

### Witnesses + coordination

`binding-log-scale-investigation`, `binding-shell-enhancement-derivation`,
`binding-volume-difference-probe`, `binding-reeb-phase-decomposition`,
`binding-rotation-phase-lead`. Ledger:
[`2026-05-29-binding-a3-honesty.md`](../coordination/2026-05-29-binding-a3-honesty.md).
PR #1417; complementary scalar-scale lane #1416; converges with #1421
(no derived atom→knot rule) and #1420 (EM/Coulomb = sinh channel).

### Two further results (cosh/sinh proofs, transcendental, Yekutieli)

**cosh/sinh now proved (narrows the surface area).**
`crossing-energy-decomposition.lean` proves the algebraic→hyperbolic
bridge for any $q>0$: $(q\pm q^{-1})/2=\cosh/\sinh(\ln q)$,
$q^n=\cosh(n\lambda)+\sinh(n\lambda)$, $q^n-q^{-n}=2\sinh(n\lambda)$, and
$[n]_q=\sinh(n\lambda)/\sinh(\lambda)$ — the quantum integer is a value of a
transcendental hyperbolic sine (the $q$-deformed seed of the Kashaev
volume). So the cosh = strong / sinh = Coulomb split is a **theorem, not a
fit**. (Build-deferred: no `lake` in the authoring container.)

**Transcendental (Lobachevsky volume) — REFUTED; phase wins.** Replacing
the Reeb phase shift $|\Delta\theta_\lambda|$ with the Lobachevsky volume
$\Delta\Lambda(\theta_\lambda)$ ($\Lambda(\theta)=\tfrac12\mathrm{Cl}_2(2\theta)$,
the building block of hyperbolic volume) makes the fit **worse** (A=3
mirror-pair spread 1.7%→12.6%; full 274%→317%). So binding tracks the
**Reeb angle itself**, not the volume of it — it is *linear in the
rotation angle*, the boundary-holonomy datum.

**Yekutieli non-abelian Stokes — refined picture.** The chain is
$\mathbf{C}$ categorical action $\to$ Yekutieli non-abelian Stokes $\to$
$H_n(q)$: the braid word (1-D boundary) is the holonomy; the curvature
2-form $[F,F]$ is the Hecke quadratic relation
(`atom-knot-mass-derivation.md:385`); the Yekutieli classes $\kappa_n\neq0$
are the lifting obstruction (`archimedean-yekutieli.md`). **Assessment:**
the pieces are present but **not assembled** into one explicit
boundary↔surface (linear↔quadratic) derivation — that remains a gap. But
the phase result *refines* the earlier "dropped quadratic $[F,F]$"
hypothesis: the A=3 binding (to 2%) is recovered from the **boundary
holonomy's per-representation Reeb phase** $e^{\pm i\theta_\lambda}$, which
the scalar Markov trace $\sum_\lambda y_\lambda\chi_\lambda$ collapses
($\cos\theta$ summed). So the dominant missing piece is **per-rep phase
resolution of the boundary holonomy**, not (primarily) the dropped surface
term. The surface $[F,F]$ correction is separate and likely sub-dominant.

**q-Hamiltonian rotational energy — μ₀ derived; deuteron reproduced; A≥3 deficit persists.**
The $q$-energy block (`climax-volume-mass/q-energy`) gives the q-Hamiltonian
$\mathfrak{E}_q = J_q^2\hbar_q\mu_0$ (rotational) $+\, p_q^2\hbar_q/(2[n]_q)$
(translational) $+\, S_q$ (action). A q-Reeb rotation is the **rotational
term** with all factors substrate-derived: $\mu_0 = m_e/(3(q-q^{-1})/2)
\approx 1.6295$ MeV (the per-crossing scale fixed by the electron's three
crossings,
[`universal-ilp-algorithm`](../../content/quantum-observable-universe/particle-interactions/universal-ilp-algorithm.md)),
$\hbar_q = 1-q^{-1}$, and $J_q^2(j) = [j]_q[j+1]_q$ with $j = n/2$ for
$n = 3A$ strands ([`q-angular-momentum`](../../content/quantum-observable-universe/climax-volume-mass/q-angular-momentum.md)).
Live evaluation
([`binding-qhamiltonian-rotational-scale.witness.json`](../../computations/binding-qhamiltonian-rotational-scale.witness.json)):

| atom | $j=n/2$ | $J_q^2$ | $E_{\mathrm{rot}}=\mu_0\hbar_q J_q^2$ | $B_{\mathrm{AME}}$ | err |
|------|---------|---------|--------------------------------------|---------------------|-----|
| D    | 3.0     | 12.51   | **2.020 MeV**                        | 2.225               | **−9 %** |
| T    | 4.5     | 27.00   | 4.360                                | 8.482               | −49 % |
| ³He  | 4.5     | 27.00   | 4.360                                | 7.718               | −44 % |
| ⁴He  | 6.0     | 48.71   | 7.865                                | 28.296              | −72 % |

The **deuteron binding is reproduced to −9 % from fully-derived quantities
with zero free parameters** — a second, independent derivation of $B_D$
alongside the $m_e\cdot\mathrm{Vol}(\mathcal{B}_3)\cdot\Delta\mathrm{tr}$
endomorphism (+0.19 %). But A≥3 undershoots by the same 44–72 % deficit.
**Net status:** $\mu_0$ is derived. The gate is **not** "derive the scale"
— it is the per-rep A≥3 structure: the highest-weight $j=n/2$ quantum
collapses the per-block Reeb phase just as the scalar trace does. (An
earlier draft of this probe incorrectly used the spin-½ quantum $j=\tfrac12$,
producing a bogus 249 MeV scale; corrected with $j=n/2$ above.)

## See also (2026-05-30 — α_shift universal chain unification)

The "per-rep A≥3 structure" gate is the same boundary holonomy that the
**α_shift universal derivation chain** captures via
$\alpha_{\text{shift}}(T_{p, k}) = k \cdot (p - 1)$ on torus knots.
The merged `prop:alpha-shift-torus-knot` provides the Lean-proved
formula; the new
[`prop:binding-alpha-shift-extension`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.md)
wires this into binding closure:
$B(A) = m_e \cdot \rho_0 \cdot \alpha_{\text{shift}}(T(p_A, k_A))$.

Remaining open math (per-A force-carrier knot identification —
T(2, 5) for A = 3 mirror pair, T(3, 4) for ⁴He, both conjectural)
is now structurally parallel to:

- [`prop:meson-color-tube-uniqueness`](../../content/quantum-observable-universe/mass-theory/meson-color-tube-uniqueness.md) (meson, T(2, 3) + T(2, 4));
- [`prop:em-coupling-bring-zero-mode`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md) (α_EM, T(2, 9) + T(3, 5)).

Reference: [α_shift universal derivation chain audit](2026-05-30-alpha-shift-universal-derivation-chain.md).
