# q-Bessel joint J⊕I binding probe — does the rotation/growth *joint* combination help A≥3? (2026-06-14)

**Status:** exploratory probe (no production wiring). Tests whether the
one named-but-untested closure lever from the 2026-06-02 full-θ verdict —
combining the rotation (arccos / `J_ν`) and growth (arccosh / `I_ν`)
channels *jointly* per the q-Bessel structure, rather than summing
`|Δθ_λ|` magnitudes — moves the data-complete A≥3 cases (³He, T) toward
closure. **This is a refutation/characterization probe, not a 7th fit
ansatz** (cf. AGENTS.md "Δ_λ gate (Track A blocker)").

## Why this probe exists (wire-check synthesis, 2026-06-14)

A wire-check asked: *could the per-λ θ_λ rotation/growth split (the object
PR #2279's Hahn–Exton q-Bessel identification describes) close A≥3
binding?* The corpus already answers most of it:

1. **It is already wired and tested.** The full-order assembly
   `binding_a3plus_full_theta_assembly.py`
   ([verdict](2026-06-02-binding-A3plus-full-theta-verdict.md), zero fits)
   is the **closest non-fit A≥3 derivation to date** — but does **not**
   close:

   | atom | result (zero fits) | note |
   |------|--------------------|------|
   | **³He** | **+17.4 %** | closest valid non-fit derivation to date |
   | T    | +39.1 % | mirror-pair sign agrees |
   | D    | +287 % | *special* — scalar path closes D at +0.19 %; full-order double-counts at A=2 |
   | ⁴He  | gated out | χ witness `partial` (24/77 partitions) |

2. **No structural obstruction on the canonical route.** The
   [quadratic-obstruction finding](2026-06-09-delta-lambda-gate-quadratic-obstruction.md)
   (required Δ spans ~459 orders of magnitude → no constant `Δ_λ` closes)
   is **route-specific** to the non-canonical H₃-local `build_atom_nf`
   projection. Owner-confirmed correction: the **canonical** binding
   `tr_M` (H₃ₐ matrix-M) is **O(1)** (deuteron 1.332, tritium 1.086) — no
   blow-up. The gate is genuinely open, not provably shut.

3. **PR #2279's q-Bessel structure *is* the one named, untested lever.**
   The verdict's remaining lever (its own §"Remaining gap analysis", row
   "Growth-channel arccosh"): rotation and growth are *"NOT separately
   combined with rotation contributions"* — the assembly summed `|Δθ_λ|`
   **magnitudes**, collapsing the J/I distinction. PR #2279 identifies the
   tower as a Hahn–Exton q-Bessel = `E_q(2)` matrix coefficient, i.e. a
   **joint `J_ν ⊕ I_ν`** object. That joint structure maps exactly onto
   this lever.

**Honest caveat.** The q-Bessel identification fails at n=3
(resid 0.128) at the trace level, so the joint structure is only
approximate; the lever it targets is also most relevant for ⁴He (data-
blocked), and the verdict attributes the T/³He gap partly to differing
binding *links* (8₁₁ vs L6a4), not the J/I split. So this is *informed*
speculation aligned with a named lever — not a guaranteed payoff. The
probe is cheap and decisive, which is why we run it before the
multi-session `SU_q(2) → E_q(2)` formalization (formalize-first
discipline: cheap decisive probe before expensive proof).

## The combiner (no fit — reads the documented eigenvalue)

`binding_reeb_phase_decomposition.py` documents the per-block eigenvalue
structure directly (its docstring §WHY, lines 8–16):

- **rotation** reps: unit-modulus eigenvalues `e^{±iθ}`, `r_λ = χ_λ/dim_λ = cos θ_λ ∈ [−1,1]`;
- **growth** reps: eigenvalue `q^{±writhe}`, `|r_λ| = cosh θ_λ > 1`.

The scalar Markov trace keeps only the **real part**
`χ_λ = dim_λ · r_λ = dim_λ · cos θ_λ` (rotation) / `cosh θ_λ` (growth).
The **un-collapsed** (pre-observation) per-block object is the full
eigenvalue

$$ z_\lambda = \begin{cases} e^{i\theta_\lambda} & \text{rotation } (|r_\lambda|\le 1) \\ e^{\theta_\lambda} & \text{growth } (|r_\lambda|>1) \end{cases} $$

The **joint binding combiner** is the modulus of the Markov-weighted
*difference* of full eigenvalues (free → bound) — the "operator-valued
combiner" the decomposition docstring anticipates (line 176):

$$ S_{\text{joint}}(K) = \Bigl| \sum_\lambda y_\lambda\, \dim_\lambda \,(z^{\text{atom}}_\lambda - z^{\text{free}}_\lambda) \Bigr|. $$

Rotation channels add as **phasors** (can interfere/cancel — Jacobi–Anger);
growth channels add as **positive reals** (extensive accumulation). The
channel-flip blocks (rotation when free, growth when bound) are exactly
the `J → I` analytic continuation `I_ν(z) = i^{-ν} J_ν(iz)` made concrete.

Compare `B_pred = ρ · Vol(K_bind) · S_joint` to AME `B(K)` for the
data-complete D/T/³He, against the `Σ y·dim·|Δθ|` baseline (³He +17.4 %).

Every factor is substrate-derived (ρ ∈ {m_e, μ₀, ×ℏ_q}, Vol from
`substrate/knot_volumes`, y_λ from `chi-*-at-q0-50dps`, θ_λ/r_λ from the
Reeb decomposition). **No tuned parameters.**

## Result — NO-GO (the joint combiner hurts the trustworthy cases)

Probe run 2026-06-14 (`binding-a3plus-joint-ji-combiner.witness.json`,
2 assertions passed — the ³He baseline **reproduces the full-θ 0.7587**,
confirming the y_λ / θ_λ read is correct). Volume-scaled rel_err at ρ=μ₀:

| atom | baseline `Σ y·dim·\|Δθ\|` | joint `\|Σ y·dim·(z_a−z_f)\|` | closer? |
|------|---------------------------|--------------------------------|---------|
| D    | +286.7 % | +442.0 % | no |
| T    | +39.1 %  | +87.6 %  | no |
| **³He** | **+17.4 %** | **+117.9 %** | **no** |
| ⁴He  | +25.9 %  | +13.5 %  | YES — but on the **provisional/wrong** 2·Vol(𝓑₃) |

**Verdict: NO-GO.** The joint J⊕I combiner makes all three data-complete,
correct-volume cases (D / T / ³He) **substantially worse** — ³He degrades
6.8× (+17.4 % → +117.9 %). The lone ⁴He "improvement" sits on the
provisional `2·Vol(𝓑₃)` volume the full-θ verdict already flagged as
wrong (⁴He needs a JSJ decomposition, not a single doubled link) — exactly
the provisional-input mirage that produced the **retracted** +2.7 % ⁴He
claim. (chi-helium-4 is now complete 77/77 — regenerated since 2026-06-02
— but the *volume* is still provisional, so ⁴He stays untrustworthy here.)

### Why — structural read

Per-block partial moduli: the **growth** channel contributes ~nothing to
the joint differencing (`grow` mod ≈ 0.001–0.003 across all atoms); the
joint sum is entirely **rotation phasors adding as vectors**, and they add
*constructively*, so the joint modulus exceeds the `Σ|Δθ|` baseline (³He
1.41 vs 0.76) → overshoot. "Joint J⊕I" reduces, in this free→bound
differencing form, to "rotation phasors, un-collapsed", and the
phase-preservation **hurts**: the `|Δθ|` magnitude collapse (baseline) is
strictly better for binding.

This refutes the operator-valued-combiner motivation
(`binding_reeb_phase_decomposition.py` docstring line 176: "carry the
per-λ phase to the operator-valued combiner") **for absolute binding in
the free→bound differencing scheme** — the data prefers the collapsed
magnitude, consistent with the "observation collapses the phase" theme of
the [quadratic-obstruction finding](2026-06-09-delta-lambda-gate-quadratic-obstruction.md).

### Bearing on PR #2279

PR #2279's Hahn–Exton q-Bessel identification is sound **as mathematics /
exposition**, but its joint `J_ν⊕I_ν` structure, applied as the binding
operator-valued combiner, does **not** rescue absolute A≥3 binding. So
#2279 is **not load-bearing** for the binding frontier — it stands on its
own mathematical merit. The one named open lever from the full-θ verdict
("rotation/growth NOT separately combined") is now **tested and retired**
in this differencing form; the productive binding directions remain
GAP-A-3 / GAP-A-4 (Option-E) and the ⁴He JSJ volume, not the J/I phase
split.

## Reproducibility

```bash
cd computations
python3 binding_a3plus_joint_ji_combiner.py
# Emits: binding-a3plus-joint-ji-combiner.witness.json
```

## Cross-refs

- [`2026-06-02-binding-A3plus-full-theta-verdict.md`](2026-06-02-binding-A3plus-full-theta-verdict.md) — the baseline this probe extends
- [`2026-06-09-delta-lambda-gate-quadratic-obstruction.md`](2026-06-09-delta-lambda-gate-quadratic-obstruction.md) — why the gate is open on the canonical route
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the six failed ansätze + GAP-A-3/A-4
- PR #2279 (`claude/inspiring-shannon-7ioifb`) — the q-Bessel identification this lever derives from
