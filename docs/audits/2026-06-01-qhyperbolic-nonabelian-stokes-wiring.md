# q-Hyperbolic geometry as the implementation of the Yekutieli non-abelian Stokes step

**Branch:** `claude/qhyperbolic-stokes-wiring-2026-06-01`
**PR:** #1611
**Date:** 2026-06-01
**Status:** read-only trace + design. No fit, no fabrication.

> Companion to the VolDensity derivation trace
> (`docs/audits/2026-06-01-vol-density-derivation-trace.md`, this session,
> PR #1608), which found the `C-action → Yekutieli non-abelian Stokes →
> Hecke` chain link is ASSERTED (`conj:geom-yekutieli-alignment`,
> trivial `:= True` stubs), not derived. Overlaps PR #1610 (VolDensity
> compute-vs-paper). A sibling agent runs the Reeb/Bring geometric escape
> test on `claude/reeb-bring-geometric-escape-2026-06-01`; this branch
> uses distinct `-qhyp`-themed filenames and does not touch it.

---

## TL;DR

**The paper STATES** a clean geometric implementation of the Yekutieli
step: the categorical connection over the q-hyperbolic knot complement
`S³∖K` has a surface-ordered exponential whose boundary holonomy is the
Markov trace in `H_n(q)`, and the q-hyperbolic VOLUME (via the
Kashaev/Volume-Conjecture limit of the q-Reeb rotation angle) is the
MeV scale `Geom(K) = Vol(K)/ℏ_q²`. This is the intended per-knot,
geometric bridge.

**But it is NOT DERIVED.** Every step that would do real work is an
asserted hypothesis field or a `:= True` / `(1 = 1)` Lean stub:

- The non-abelian Stokes theorem itself is `axiom
  yekutieli_finite_slice_substrate` + a `punitInstance` discharging
  `stokes_holds := True` (`NonAbelianStokes.lean:107-121`).
- The surface-Stokes → boundary-holonomy → Markov-trace map is modelled
  as `braidSurfaceMultTrace z n := z ^ n` — a SCALAR group power, with
  no knot complement, no connection, no Hecke representation
  (`NonAbelianStokes.lean:191-192`).
- The CS/volume correspondence `baselineHolonomy = knotVolume` is a
  `structure` hypothesis field, asserted not proved
  (`topological-mass-formula.lean:83`).
- `Vol(𝓑₃) = 8·Catalan` is a hardcoded SnapPy table-lookup constant
  (`_li_2_q_util.py:243`), NOT a holonomy evaluation, and explicitly
  "NOT Lean-formalized".

**Per-operator vs per-partition — the key question.** The q-hyperbolic
construction *as stated in the paper* IS genuinely per-knot-operator: a
hyperbolic volume `Vol(S³∖K)` is a knot-complement invariant that
differs for genuinely different knots, and the q-Reeb rotation angle θ
on `V_(2,1)` is an operator (knot-word) invariant, not a partition
character. So *in principle* it escapes the Markov-degeneracy
impossibility (per-partition functions cannot distinguish p from n).

**BUT in production it COLLAPSES — and not even to a per-partition
character; to a single global scalar.** Production uses ONE knot (the
Borromean link `𝓑₃`) and ONE volume `Vol(𝓑₃)/ℏ_q²` for BOTH proton and
neutron (`mass_table_comprehensive.py:206`, `_li_2_q_util.py:210-254`).
The proton/neutron split does NOT come from geometry at all — it comes
from a separate substrate-identity witness flavour-split plus a Habiro
ratio (`mass_table_comprehensive.py:194-213`) and from
`closed_form_tau_M.py`'s per-partition character traces `tr_M³(𝓑_p)`
vs `tr_M³(𝓑_n)` (`closed_form_tau_M.py:291-298`). The geometric
per-knot Vol is degenerate `Vol(proton) = Vol(neutron) = Vol(𝓑₃)` in
production. So the production pipeline does NOT realise the per-operator
escape; the geometry is short-circuited to a constant and the actual
distinction is injected from outside it.

The escape is therefore **available in principle from the paper's
stated construction, but un-wired**: closing it requires giving the
proton and neutron DISTINCT knots/operators with DISTINCT q-hyperbolic
holonomies, and deriving (not asserting) the surface-Stokes →
Markov-trace map.

---

## 1. The q-hyperbolic geometry in the paper — inventory

| Object | File:line | Status | Role |
|--------|-----------|--------|------|
| Hyperbolic mass formula `m(K) = Vol(K)/ℏ_q²` | `quantum-universes/topological-mass-formula.lean:52-107` | DERIVED *modulo 2 asserted hypotheses* | Closed form from `TopologicalMassDecomposition` + (CS/vol) + (dilog) |
| CS/volume correspondence `baselineHolonomy = knotVolume` | `topological-mass-formula.lean:83` | ASSERTED (structure field) | The non-abelian-Stokes "boundary holonomy = volume" step |
| Dilog evaluation `Σ exceptional = Vol·(1/ℏ²−1)` | `topological-mass-formula.lean:88-89` | ASSERTED (structure field) | Briggs–Klein blow-up sum |
| `knotVolume : R_q` (per-knot) | `topological-mass-formula.lean:77` | per-knot variable; numeric value = SnapPy table | The per-operator geometric input |
| SnapPy-verified volumes (11 knots) | `observations/knot-volumes-verification.md:1-18` | DERIVED (independent SnapPea kernel) | Numeric `Vol(K)` table; Lean uses `axiom -- Ref:[computation]` |
| q-Reeb rotation angle θ on `V_(2,1)` | `braids-and-knots/figure-eight-reeb-rotation.md:38-80` | PAPER-STATES (proof *sketch*) | θ = accumulated Reeb phase of the alternating braid; → Vol(4₁) in Kashaev limit |
| Volume-Conjecture link θ(q₀) ↔ Vol(4₁) | `figure-eight-reeb-rotation.md:70-74` | PAPER-STATES (cited as Volume Conjecture) | The finite-q phase → asymptotic volume bridge |
| `conj:hyperbolic-volume-transcendence` | `predicted-spectra/hyperbolic-volume-transcendence.lean:18-23` | CONJECTURE (`class … holds : Prop`) | Algebraic independence of QOU volumes |
| `conj:geom-yekutieli-alignment` | `mass-theory/geom-yekutieli-alignment.{md,lean}` | CONJECTURE; Lean = §3b-cond stub | The "Geom = Yekutieli rigid-dualizing evaluation" claim |
| Yekutieli non-abelian Stokes (axiomatised) | `lean/QOU/Mathlib/NonAbelianStokes.lean` | AXIOM + `:= True` stub | The non-abelian Stokes theorem itself |

---

## 2. The intended derivation — how Yekutieli SHOULD produce VolDensity

Reading the paper's stated chain (`geom-yekutieli-alignment.md:3-152`,
`figure-eight-reeb-rotation.md`, `NonAbelianStokes.lean` docstrings):

### (a) The connection / categorical action
The Frobenius–Hopf algebra `A` at substrate parameter `q` carries a
Lie-algebra-valued 1-form `α ∈ Ω¹(M; 𝔤)` (the categorical/gauge
connection). Abstractly modelled as `LieAlgebraOneForm`
(`NonAbelianStokes.lean:287-289`); the gauge-covariant derivative
`d_α β = dβ + [α, β]` is `gaugeCovariantDerivative`
(`NonAbelianStokes.lean:300-305`). **Status: structure present,
content `:= 0` (`LieValuedStokes_canonical`, lines 333-344, sets
`alpha := 0`, `beta := 0`).** The actual QOU categorical connection is
never instantiated.

### (b) The surface
The paper takes the surface-ordered exponential over the
**Young-diagram braid surface** (the piecewise-affine 2-complex of the
braid β whose closure is `K = β̂`), NOT directly over the Seifert
surface or the Bring curve. See `NonAbelianStokes.lean:21-27,97-101`
("finite-slice … on a piecewise-affine surface … literal finite
product of generator-actions"). The geometric reading on `S³∖K` is the
**τ-image** of the algebraic evaluation
(`geom-yekutieli-alignment.md:13-16,67-75`), classified by Thurston
geometrization at the τ-side. So: algebra over the braid surface;
geometry over the knot complement; the two linked by τ (the fibre
functor / Markov trace).

### (c) Does the boundary holonomy land in `H_n(q)` (giving tr_M)?
**Intended: yes.** Yekutieli-Stokes turns `MI₁(α; ∂σ) = MI₂(d_α β; σ)`;
the boundary `∂σ` of the closed braid surface is the braid closure, and
its multiplicative line integral is the ordered product of
generator-actions `σ_{i_1}···σ_{i_ℓ}` — i.e. the image of β in `H_n(q)`,
whose Markov trace is `tr_M = J_K(q)`. **Status: ASSERTED.** The Lean
realises this only as `braidSurfaceMultTrace z n := z^n`
(`NonAbelianStokes.lean:191-192`) — a single group element `z` raised
to the braid length, with NO Hecke representation, NO Wedderburn
blocks, NO `χ_λ`. The genuine "holonomy ∈ H_n(q)" content is the
~3000-5000 LoC of Mathlib Lie-valued-forms infrastructure the file
flags as the upstream target (`NonAbelianStokes.lean:29-32`).

### (d) Where does the q-hyperbolic VOLUME enter as the MeV scale?
Two routes, both PAPER-STATES / ASSERTED:

1. **CS/volume correspondence** (`topological-mass-formula.lean:80-83`):
   the baseline holonomy of the QOU connection *equals* `Vol(K)`. This
   is exactly the "non-abelian Stokes boundary holonomy = hyperbolic
   volume" identity — and it is a `structure` hypothesis field, not a
   theorem. The `1/ℏ_q²` normalisation is the Frobenius pairing
   normalisation (dilog hypothesis, lines 84-89).

2. **q-Reeb rotation → volume** (`figure-eight-reeb-rotation.md:38-74`):
   the q-Reeb flow advances the color angular coordinate by `q·t` per
   crossing; the alternating figure-eight braid accumulates net Reeb
   phase `2hπ`, manifest as the `V_(2,1)` eigenvalue phase θ; θ in the
   Kashaev `N→∞` limit yields `Vol(4₁)` via the Volume Conjecture. This
   is the cleanest *geometric* statement of the dimensional bridge — and
   it is a proof *sketch* (PAPER-STATES), citing the Volume Conjecture
   (open in general) for the θ(q₀) ↔ Vol(4₁) link.

So the MeV scale enters as `m(K) = m_e · Vol(K)/ℏ_q²`, with `Vol(K)`
the q-hyperbolic volume reached either by the asserted CS/volume
holonomy identity or by the q-Reeb-phase/Volume-Conjecture route.

---

## 3. The KEY QUESTION — per-operator-geometric vs per-partition

### What the Markov-degeneracy impossibility says
(Proven this session, parent trace PR #1608.) A function of the
**partition data alone** — `tr_M = Σ_λ y_λ χ_λ` with the same partitions
λ ⊢ n and the same `H_n(q)` characters for p and n — cannot distinguish
proton from neutron, because they share the same Wedderburn block
structure. The distinction must come from data sensitive to the actual
operator/knot, not just its partition spectrum.

### Is the q-hyperbolic route per-operator?
**In principle YES — this is the genuine appeal of the steer.**

- `Vol(S³∖K)` is a **knot-complement invariant**: distinct knots have
  distinct hyperbolic volumes (e.g. `Vol(4₁) ≈ 2.0299`,
  `Vol(𝓑₃) = 8G ≈ 7.328`). It is NOT a function of the partition
  spectrum of the braid's Hecke image — it depends on the actual
  geometry of the complement. Two braids with the SAME Markov trace can
  have DIFFERENT complement volumes. So a `Vol(K)`-valued Geom is
  strictly finer than `tr_M`, and CAN distinguish operators that the
  character cannot.
- The q-Reeb rotation angle θ on `V_(2,1)`
  (`figure-eight-reeb-rotation.md:50-52`) is likewise an **operator
  invariant** — the accumulated phase of the *specific braid word*
  `(σ₁σ₂⁻¹)²` — not a partition character. Different knot operators
  accumulate different Reeb phases.

Therefore the q-hyperbolic Stokes route, *as the paper states it*, is a
per-knot-OPERATOR geometric quantity that escapes the per-partition
character degeneracy. This is the affirmative finding connecting to the
sibling Reeb test.

### Does production realise the escape? NO.
Production **collapses the per-operator geometry to a single global
scalar** and injects the p/n distinction from elsewhere:

1. Both proton and neutron use the SAME knot `𝓑₃` and the SAME
   `vol_density_borromean(q) = Vol(𝓑₃)/ℏ_q² · linking_weight`
   (`mass_table_comprehensive.py:206`, `_li_2_q_util.py:210-254`).
   `Vol(𝓑₃) = 8·Catalan` is a hardcoded constant
   (`_li_2_q_util.py:243`).
2. `linking_weight = 5/2 + (3/4)h²` is a per-PARTITION character sum:
   `(1/4)·Σ_{λ⊢4} dim_q V_λ` (`_li_2_q_util.py:172-197`) — exactly the
   degenerate kind of object.
3. The p/n split is `(1 ∓ Δm/(2M_N))` from a separate substrate-identity
   witness + Habiro ratio (`mass_table_comprehensive.py:194-213`), and
   the constituent factor `tr_M³(𝓑_p)` vs `tr_M³(𝓑_n)`
   (`closed_form_tau_M.py:291-298`) — character traces, again
   per-partition-style.

So in production the geometric Vol is **degenerate p=n**, the available
per-operator escape is **not used**, and the actual p/n split rides on
non-geometric data. The geometry has been short-circuited to a constant.

---

## 4. Concrete wiring needed to replace the `:= True` stub

To make the q-hyperbolic Stokes route an actual derivation AND realise
the per-operator escape:

### Provable from existing repo defs (+ Yekutieli's theorem cited)
1. **Boundary-holonomy = braid Hecke image.** Replace
   `braidSurfaceMultTrace z n := z^n` (`NonAbelianStokes.lean:192`) with
   the genuine ordered product in `H_n(q)` of the braid's Hoefsmit
   matrices (the repo already has Hoefsmit seminormal `σ_i` on
   `V_(2,1)`, `figure-eight-reeb-rotation.md:15-31`, and a Hecke/Markov
   layer in `jones-markov-trace.lean`). The finite-slice claim
   (`stokes_holds`) then becomes: `MI₁(α; ∂σ̂)` = ordered product of
   Hoefsmit `σ_i` = `ρ(β)`, and `tr_M(ρ(β)) = J_K(q)`. This is a
   **finite-dimensional matrix computation**, no analysis — provable
   from existing Hoefsmit + Markov defs, citing Yekutieli (2015) §3
   only for the surface→boundary reduction on piecewise-affine surfaces.

2. **q-Reeb phase = eigenvalue phase on `V_(2,1)`.** The
   `figure-eight-reeb-rotation.md` proof *sketch* (unitarity of `M_{4₁}`,
   det = 1, real trace ⇒ eigenvalues `e^{±iθ}`) is a 2×2 Hoefsmit-block
   computation — fully provable in Lean from the existing Hoefsmit data.
   This grounds the operator-invariant θ rigorously.

### Needs new categorical / analytic input (NOT provable from existing defs)
3. **CS/volume correspondence** `baselineHolonomy = knotVolume`
   (`topological-mass-formula.lean:83`). This is the genuine
   non-abelian-Stokes content: that the categorical baseline holonomy of
   the QOU connection on `S³∖K` evaluates to the hyperbolic volume. It is
   a deep geometric theorem (Chern–Simons/volume; cf. the Volume
   Conjecture for the q-Reeb route). **Not provable from current defs** —
   needs either the Volume Conjecture (open) for the Reeb route, or a
   direct categorical Stokes evaluation that the repo does not have. This
   is the load-bearing assertion.

4. **`Vol(𝓑₃) = 8·G` and per-knot Vol as holonomy.** Currently a SnapPy
   table constant (`_li_2_q_util.py:235,243`). To be a *derivation* it
   must be the output of the categorical holonomy of step 3, not a
   literature lookup. New input.

5. **Per-operator p/n knots.** To USE the escape, proton and neutron
   need DISTINCT operators with DISTINCT q-hyperbolic holonomies (e.g.
   `𝓑_p` vs `𝓑_n` as genuinely different braids whose complements have
   different volumes), feeding `geomInvariant(K_p) ≠ geomInvariant(K_n)`.
   Production currently uses one knot for both. This is a
   modelling/categorical decision, not yet made — and is exactly where
   the Markov-degeneracy escape would be cashed in.

### Mapping to the `:= True` stubs
| Stub | File:line | Replace with |
|------|-----------|--------------|
| `stokes_holds := True` | `NonAbelianStokes.lean:110` | `MI₁(α;∂σ̂) = ρ(β)` (Hoefsmit ordered product) — step 1 |
| `braidSurfaceMultTrace z n := z^n` | `NonAbelianStokes.lean:192` | Hecke ordered product + `tr_M` — step 1 |
| `GeomYekutieli … holds : True` | `geom-yekutieli-alignment.lean:86` | CS/volume correspondence — step 3 (NEW INPUT) |
| `baseline_eq_volume` (hyp field) | `topological-mass-formula.lean:83` | derive, not assert — step 3 (NEW INPUT) |
| `vol_b3 = 8*mp.catalan` (const) | `_li_2_q_util.py:243` | holonomy output — step 4 (NEW INPUT) |

---

## 5. Verdict

- **Per-operator-geometric escape EXISTS in the paper's stated
  construction** (q-hyperbolic volume / q-Reeb phase are knot-operator
  invariants, strictly finer than `tr_M = Σ_λ y_λ χ_λ`). This is the
  affirmative result for the sibling Reeb/Bring test.
- **It is un-wired in production**: both nucleons share one knot, one
  volume, one global scalar; the p/n split is injected from non-geometric
  witnesses. The escape is *not currently realised*.
- **Steps 1–2 are provable from existing Hoefsmit/Markov defs** (finite
  matrix computations + Yekutieli §3 citation for the finite-slice
  reduction).
- **Steps 3–5 need new input**: the CS/volume correspondence (or the
  Volume Conjecture for the Reeb route), a categorical-holonomy
  derivation of `Vol(K)`, and a per-operator p/n knot model. These are
  the load-bearing assertions the `:= True` stub currently hides.

No fit was performed; no derivation was fabricated. Every status label
above is sourced to file:line.
