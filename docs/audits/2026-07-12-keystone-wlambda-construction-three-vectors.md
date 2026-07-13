# Geometric W_λ construction — three-vector tranche (gate open)

**Date:** 2026-07-12 · **Axis:** s5-so3-keystone geometric `W_λ` (owner gate open) ·
**Branch:** `claude/keystone-wlambda-construction-2026-07-12` · **No fit; no physics claim.**

The owner opened the geometric `W_λ` gate. Target: exhibit the object whose measure is
`W_λ = d_q(λ)²/D²`, on the **full-Hecke** side (the Step-1 gate having refuted the
SU(2)/WRT route on coverage, [2026-06-24 audit](2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md)).
Three attack vectors were run in parallel, each **no-fit / zero-free-parameter**, each
reporting honestly. Two are clean negatives (valid pruning per the no-negative-result
discipline); one is a proved formalize-first extension. They **interlock**.

## Vector 1 — E_q(2) q-Bessel `latticePt` : REFUTED, scope-(a)

[`keystone_qbessel_latticept_search.py`](../../computations/probes/keystone_qbessel_latticept_search.py).
Tests whether a zero-parameter *structural* `latticePt` index into the 2nd-kind Jackson
q-Bessel contiguity **weight orbit** realizes the seven n=5 `d_q(λ)` (the open field of
`QBesselRadialPartRealization`). Six transpose-invariant index maps (|content|, content²,
Durfee, n(λ)+n(λ′), max-hook, hook-sum): **4 excluded a priori** (index collisions — same
index, different `d_q`); the **2 injective** ones miss numerically (~100%; the alternating
`q^{2k}`-scaled orbit does not track the near-linear `d_q` vector). **Scope-(a)** — these
maps *alone*; not a structural exclusion (the geometric owner-gated `latticePt` untouched).
Genuinely new vs the prior s013 probes (weight-orbit index, not roots / closed forms).

## Vector 2 — colored-WRT per-block vs `d_q(λ)` : PARTIAL/FAIL, scope-(b) on the narrow hypothesis

[`keystone_colored_wrt_perblock_vs_dq.py`](../../computations/probes/keystone_colored_wrt_perblock_vs_dq.py).
In any ribbon MTC the λ-colored WRT weight factorizes its colour dependence as
`W^{WRT}_λ = (global)·S_{0λ}·θ_λ^{f}`, with `S_{0λ}/S_{00}=d_q(λ)` (full-Hecke, all rows),
`θ_λ=q^{2c(λ)}` the ribbon twist, and `f` the fibre framing **forced** by Σ(2,3,5)
(orbifold `e=−1/30`, ≠ 0). So `W^{WRT}_λ ∝ d_q(λ) ⟺ θ_λ^{f}` const `⟺ f=0`.

Result (q₀, 55 dps, n=3,4,5): the ratio `W/d_q = θ_λ^{f}` is **not constant** (spread
3.50 → 12.23 → **64.95** at n=3,4,5). Decisively, since `d_q(λ)=d_q(λ′)` (hook-multiset
symmetric) but `θ_{λ′}=θ_λ^{−1}` (content-sum antisymmetric), the framed weight obeys
`W_λ/W_{λ′}=θ_λ^{2f}≠1` — it **breaks a conjugation symmetry `d_q` has**, normalization-
independently, on every non-self-conjugate pair. The only proportional case `f=0` is the
content-free reduction valid for *any* manifold (carries **zero** Σ(2,3,5) data — the
forbidden tautology). **Scope-(b)** exclusion of the *narrow* hypothesis "fibre-colored
WRT(Σ(2,3,5)) weight `= d_q` as-is", justified by two proved invariants (hook-multiset
symmetry of `d_q`; content-sum antisymmetry of the twist) + the nonzero orbifold framing.
The **broad** programme (an S¹-equivariant index on the corrected full-Hecke arena that
cancels the framing) stays **(a)-open**. This extends the Step-1 gate: SU(2) failed on
*coverage* (≥3-row blocks); the full-Hecke coloring restores coverage but is then killed by
the **ribbon twist**.

## Vector 3 — modular T-matrix `θ_λ = q^{c(λ)}` (Lean) : PROVED, sorry-free

[`KeystoneModularTwist.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneModularTwist.lean).
Adds the **second** piece of modular data to the keystone MTC (which carried only the
S-matrix vacuum row `S_{0λ}`): the ribbon twist / modular T-matrix `θ_λ = q^{c(λ)}`. Proves
sorry-free (axioms `[propext, Classical.choice, Quot.sound]`; generic `[GroupWithZero R]`,
§7c — no `ℝ`): the **signed content flip** `contentSum_conjugate : c(λ′) = −c(λ)` (the
corpus had only the *squared* invariance `sumSqContents_conj` + a single `[2]↔[1,1]`
instance), hence the twist's chirality law `theta_conjugate : θ_{λ′} = θ_λ⁻¹`; the vacuum
triviality `θ_∅ = 1`; the one-row framing `2·c([n]) = n(n−1)` (`θ_{[n]} = q^{\binom n2}`);
and the `ModularTwistData` structure + `heckeTwistData` instance (needs **no** `1<q` — the
twist is the purely-algebraic half of the modular data).

## The interlock (why the three cohere)

Vector 3 **proves the exact invariant that vector 2 shows is fatal**: the T-matrix chirality
law `θ_{λ′}=θ_λ⁻¹` (Lean-proved) is *precisely* why the framed colored-WRT weight
`S_{0λ}·θ_λ^{f}` cannot equal the conjugation-symmetric `d_q(λ)` for `f≠0` (vector 2). So the
tranche's net structural content is sharp and proved:

> Any geometric carrier of `W_λ` must produce a **twist-free / conjugation-symmetric**
> amplitude. A colour-charged Wilson line on the nontrivially-framed Σ(2,3,5) fibre
> structurally cannot (the ribbon twist `θ_λ`, now a Lean object with a proved chirality
> law, is the obstruction). The q-Bessel radial *weight-orbit index* (vector 1) also fails
> as-is. The owner-gated open object (`bwS0_eq_hecke`) is untouched; these results **narrow**
> what it must be — a framing-cancelling full-Hecke index.

## Follow-up (#3662) — the gate `bwS0_eq_hecke` de-opaqued

[`BWVacuumRowConcrete.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BWVacuumRowConcrete.lean)
(sorry-free, axioms `[propext, Classical.choice, Quot.sound]`). The gate's field `bwS0` was an
**opaque free field** — fiat-dischargeable by `bwS0 := d_q/D`, capturing no content. This file
**replaces it with the concrete RT/Seifert vacuum row** `bwS0Concrete = S0·θ^f` (the compact modular
datum × the ribbon twist `θ_λ=q^{c(λ)}` from vector 3, raised to the forced Seifert framing `f`),
converting an un-provable physics-fiat into a genuine, refutable math claim, and proves:

- `bwS0Concrete_f_zero` — `f=0` (zero Σ(2,3,5) data) collapses to `S0` (the tautology).
- `bwS0Concrete_eq_S0_iff` — the de-opaqued gate holds **iff `θ^f=1`** (symbolic-exact).
- `bwS0Concrete_conj_mul` / `bwS0Concrete_breaks_symmetry` — the concrete row **breaks the conjugation
  symmetry `d_q` has** (`S0` transpose-invariant via `qDim_conj`, `θ` transpose-inverting via
  `theta_conjugate`) — a scope-(b) invariant, not a magnitude probe.
- `bwS0Concrete_eq_hecke_forces_trivial_twist` (capstone) — if the concrete Hecke row equals
  `d_q/√Σd_q²` on all of `P`, then `∀ l∈P, (θ_λ)^f=1`.

**Honest disposition:** at the observable real `q₀>1`, `θ_λ=q₀^{c(λ)}` is no root of unity for
`c(λ)≠0`, so for the forced framing `f≠0` the gate is **REFUTED** off self-conjugate blocks — a
scope-(a) negative for *this construction at real q₀*, sharpened by the scope-(b) transpose-symmetry
invariant. The surviving residue is the **fibre root-of-unity form** (`|q|=1`, `|θ|=1`) archimedean-
continued to `q₀` (AGENTS.md fibre-vs-observable-`q`). De-opaquing **exposes and sharpens** the gate;
it does not close it. No fit; no fabricated `BWVacuumRowIsHecke` instance is presented as a closure.

## Scope (STRICT)

No fit, no free constants, no production wiring, no physics claim. Vectors 1–2 are
falsifiable probes (negatives = pruning); vector 3 is a formalize-first modular-data
extension; the #3662 follow-up de-opaques the gate into a refutable-at-`q₀` claim. The
geometric `W_λ` index itself remains owner-gated (the fibre/archimedean-continuation residue).
