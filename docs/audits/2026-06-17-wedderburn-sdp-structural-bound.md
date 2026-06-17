# The dense Wedderburn-projector SDP is structurally bounded — a redundant-constraint, degenerate-face program that selects no unique operator, never 𝓑₃ (2026-06-17)

**Branch:** `claude/delta-lambda-open-levers-2026-06-17`
**Picks up:** the Δ_λ-route arc — specifically the one open *compute* lever
left by [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](2026-06-17-delta-lambda-two-remaining-directions-closed.md)
(#2433): *"implement the genuine dense Wedderburn-projector SDP
([`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md)),
which — if it selects the Borromean signature — unlocks #2430's
operator-cumulant scalar."*
**Discipline:** formalize-first (state the class, find the invariant, let it
narrow the probe); derive-or-refute; no fit, nothing rewired.

## Formalize-first verdict — do NOT build the heavy solver; it is provably bounded

Before implementing the full dense matrix-`Φ` primal SDP, the formalize-first
discipline asks: *is there a structural invariant the whole solution class must
satisfy that settles the question first?* There is, and it is decisive.

The SDP ([`confinement-sdp.md`](../../content/quantum-observable-universe/mass-theory/confinement-sdp.md),
implemented in dual/scalar form in `computations/sdp_cross_channel.py`) is

$$\min_\Phi\ \langle T,\Phi\rangle \quad\text{s.t.}\quad \Phi\succeq 0,\ \ \langle\pi_\lambda,\Phi\rangle\ge 0\ \forall\lambda,\ \ \text{(2×2-pair PSD)},\ \ \mathrm{tr}\,\Phi = c.$$

Three structural facts collapse it.

1. **`⟨π_λ,Φ⟩ ≥ 0` is redundant.** The `π_λ` are the central idempotents
   projecting onto the Wedderburn blocks — PSD projectors. For any `Φ ⪰ 0`,
   `⟨π_λ,Φ⟩ = tr(π_λ Φ) ≥ 0` automatically (the trace of a product of two PSD
   operators is non-negative). The per-block Frobenius-positivity constraints
   add nothing.
2. **The 2×2-pair-PSD constraints are redundant.** Every principal submatrix of
   a PSD matrix is PSD. Given the global `Φ ⪰ 0`, every adjacent-pair `2×2`
   block is already PSD.
3. **The cost operator `T` is block-constant diagonal.** In
   `sdp_cross_channel.py` the cost is `T_λλ = μ_λ` (the q-Laplacian /
   content-Casimir eigenvalue per Wedderburn block), off-diagonal `= 0`
   (`sdp_with_atom_observables` docstring, line 178). The Markov-trace-weighting
   variant is likewise a scalar weight per central block; its resolvent is
   diagonal too.

So the SDP reduces to `min ⟨T,Φ⟩ s.t. Φ⪰0, trΦ=c` with block-constant diagonal
`T`. A **linear** objective over the (compact, convex) density spectrahedron
attains its minimum on the **face** of states supported on the minimum
eigenspace of `T` — i.e. on the union of the blocks `λ` achieving `min_λ μ_λ`.

> **Structural theorem (corrected — the optimum is a *face*, not a single block).**
> *The genuine dense Wedderburn-projector SDP minimises a linear functional with
> block-constant diagonal cost over the density spectrahedron. Its optimum is the
> face of densities supported on `T`'s minimum eigenspace `⋃_{λ:\,μ_λ=μ_{\min}}`.
> The per-block and 2×2-pair constraints, being implied by the global PSD cone,
> change neither the optimal value nor the optimal face. When `min_λ μ_λ` is
> attained by more than one block the face is high-dimensional and the program
> selects **no unique operator**. The Borromean braid `𝓑₃` is a specific
> multi-block element (its normal form is ≈99.8% the identity, which carries
> weight in **every** block including the high-cost trivial `[3]`); a degenerate
> face that also excludes the `[3]` block cannot single it out. Hence no
> block-diagonal-cost SDP of this form selects `𝓑₃`.*

This is the rigorous upgrade of #2433's empirical *"run directly it concentrates
on the smallest-cost mesonic channel."* The reason is structural and basis-free:
**selection by minimising a linear functional lands on a face of the
spectrahedron**, and at `q₀` that face is degenerate — so the program does not
even produce a unique operator, let alone the specific `𝓑₃`.

## Numerical confirmation

[`computations/probes/wedderburn_sdp_extreme_point.py`](../../computations/probes/wedderburn_sdp_extreme_point.py)
solves the dense `6×6` primal SDP over `H_3(q₀)` (blocks `[3]⊕[2,1]⊕[1,1,1]`,
dims `1+4+1`) with cvxpy, **with and without** the redundant per-block / pair
constraints. The q-Laplacian costs at `q₀ = 1.10998`:

| block `λ` | `dim²` | `μ_λ` | |
|---|--:|--:|---|
| `[3]` | 1 | **8.13148** | high-cost trivial block |
| `[2,1]` | 4 | 2.01090 | ← min (tie) |
| `[1,1,1]` | 1 | 2.01090 | ← min (tie) |

Results:

1. **Redundancy.** With vs without the extra constraints: `|Δobjective| =
   8.7×10⁻⁷` and the optimal **support is identical** (`{[2,1],[1,1,1]}` in both)
   — the constraints are redundant (same value, same optimal face).
2. **Degenerate face.** `min_λ μ_λ = 2.01090` is attained by **two** blocks
   (`[2,1]` and `[1,1,1]`), so the optimal face has dimension **5 of 6**. The
   two solves return *different* `Φ*` (`‖ΔΦ‖_F = 0.111`) at the *same* objective
   — the signature of a high-dimensional optimal face: **no unique operator is
   selected.**
3. **`𝓑₃` not selected.** The face **excludes** the high-cost `[3]` block — the
   trivial component where `𝓑₃`'s ≈99.8%-identity weight partly lives — and is
   in any case a degenerate 5-dim set, so it cannot pin the specific multi-block
   `𝓑₃` element.

## Formalizability (Lean)

The two redundancy facts are standard and Mathlib-backed: for `A, B` PSD,
`0 ≤ trace (A * B)` (`Matrix.PosSemidef` + `inner_mul_le_norm…` / the trace-form
positivity lemmas), and a principal submatrix of a PSD matrix is PSD
(`Matrix.PosSemidef.submatrix`). The "linear functional minimised on a face /
extreme point of a compact convex set" is the Bauer minimum principle
(Krein–Milman corollary). A Lean lemma stating *"the feasible set is unchanged
by the redundant constraints"* is a short `Matrix.PosSemidef` exercise; the
face-degeneracy is a numerical fact about the spectrum of `T` at `q₀`. Recorded
as formalizable; not built here (the structural argument is decisive and the
Lean env is cold — per the formalize-first caveat, a rigorous symbolic argument
suffices when the probe is cheap and decisive).

## Consequence for the arc

The one open *compute* lever of #2433 is closed structurally: building the dense
SDP would only reproduce a degenerate min-cost face that excludes the trivial
block and selects no unique operator. `𝓑₃`-selection genuinely requires the
external **topological** criterion (Borromean = no separable sub-link), exactly
as the corpus's actual selection
(`particle-interactions/confinement-operator-selection.md`) already does — a
discrete ranking + a topological tiebreak, not a continuous variational program.

### Correction — the *other* "remaining lever" (GAP-A-3) was already refuted

#2433 also listed **GAP-A-3** (substrate-derived `A(K)` × an "open"
partition-projection `P_λ(K)`) as a non-refuted lever. A corpus-grep
([`docs/coordination/gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md))
shows this is **stale**:

- **GAP-A-3 is closed.** [#1868](https://github.com/litlfred/qou/pull/1868)
  scoped it (brane-tower content channels);
  [#1870](https://github.com/litlfred/qou/pull/1870) refuted the deuteron
  `P_λ` — **5/5 channels REFUTED**. The ledger records *"18 no-fit closures
  form a saturating chain — no per-partition ansatz survives (single statistic,
  brane-tower content channel, induction, stabilization, Bratteli, Kashiwara
  crystal, …)."*
- **`A(K)` is already substrate-derived** to ≤ 2.5 % (Phase-4).
- The GAP-A-4 follow-ons are also closed negative: additive `S(K)`
  ([#1886](https://github.com/litlfred/qou/pull/1886)) and the per-knot `Vol(K)`
  convention ([#1891](https://github.com/litlfred/qou/pull/1891)).

So there is **no fresh GAP-A-3 scope to open** — re-deriving it would repeat the
already-closed `P_λ(K)` route (the precise anti-pattern the STRICT corpus-grep
"before declaring open" rule guards against). The single *nominally*-open thread
on that ledger is **T3** — *derive `λ(K)` from a Path-B-specific formulation
(not a Phase-4 transplant)* — whose scope landed
([`2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md`](2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md))
with a probe follow-up open, and which is itself heavily constrained by the
18-closure saturating chain.

### Net for the Δ_λ-route arc

With this PR the arc is **fully bounded**: sign = chirality (proved);
scalar/trace functional (refuted #2417); operator-cumulant (gated on `𝓑₃`,
#2430); continuous `𝓑₃`-selection (refuted #2433 + **dense SDP closed
structurally here**); α-cluster (fit-blocked #2433); **GAP-A-3 (already refuted
#1868/#1870)**. No continuous/per-partition lever survives; `𝓑₃`-selection rests
on the external topological criterion the corpus already uses.

## Cross-links
- [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](2026-06-17-delta-lambda-two-remaining-directions-closed.md) (#2433) — the lever this closes structurally.
- `content/quantum-observable-universe/mass-theory/confinement-sdp.md` — the SDP spec (the object proved bounded here).
- `computations/sdp_cross_channel.py` — the dual/scalar implementation (diagonal cost `T = μ_λ`).
- `content/quantum-observable-universe/particle-interactions/confinement-operator-selection.md` — the corpus's actual discrete + topological selection.
