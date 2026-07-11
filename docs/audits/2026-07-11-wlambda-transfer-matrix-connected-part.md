# Binding as a `W_λ` transfer matrix — the connected part is the extensive channel

**Date:** 2026-07-11 · **Axis:** Δ_λ / per-isotope binding (GAP-A-4, extensive channel) ·
**Type:** design note + mechanism probe (fit-free) · **No fit; nothing wired; NOT a closure.**
**Discipline:** every negative is (a) scope-limited unless a proved invariant licenses (b);
the single-trace refutations cited are (a)-scoped re-statements, not new claims.

## The reformulation (owner lead: "transfer matrix in terms of `W_n`")

The scalar per-partition form

$$B(K) \;=\; m_e \sum_{\lambda} y_\lambda\,\chi^\lambda\,\Delta_\lambda$$

is a **single Markov trace** — hence **intensive** (it saturates at ~3–4 MeV;
gate-status 2026-07-05 §0). No scalar per-block reweighting can turn an intensive
quantity extensive — the *proved reason* the six Δ_λ ansätze failed. The proposal
is to lift the scalar weights to a **transfer matrix built from the q-Plancherel
measure** `W_λ = d_q(λ)²/[n]_q!`:

$$T \;=\; \bigoplus_{\lambda \vdash n} W_\lambda\, P_\lambda, \qquad P_\lambda = \text{Jones–Wenzl block projector},$$

and read binding off the **connected part** of a multi-bond product over the
inter-nucleon bond graph `⋈_K`:

$$B(K) \;\sim\; \operatorname{tr}\!\Big(\prod_{b\in\bowtie_K} T_b\Big) \;-\; (\text{factorized}).$$

`tr(∏T)` is genuinely many-body (cross-terms) → **extensive** (∝A), realising the
"additive many-body series over bonds `B = Σ_b B_b + Σ_{b,b'} B_{bb'} + …`" that the
gate-status demands.

## Two walls you must route around (proved / logged)

1. **`W_λ ≠ y_λ`.** `W_λ = d_q²/[n]_q!` is the **q-Plancherel (symmetric-pairing)
   measure**; the production trace weight `y_λ` is the **Wenzl principal
   specialisation** (colour-multiplicity side). Conflating them is a logged recurring
   error (`s5-so3-keystone` §Refutations).
2. **The single-trace `W_λ` surface is EXHAUSTED** (#2584): every object of the form
   `tr(T) = Σ_λ W_λ`, `Σ_λ W_λ χ^λ`, projected / home-block-weighted Markov trace has
   been probed and refuted for the μ/e mechanism (cross-checked to 1e-50), and the
   direct single-bond `W_λ` **brackets but misses** the deuteron (#2528). So a
   transfer matrix that is **traced per bond** buys nothing new.

The un-exhausted move is therefore **product-across-bonds, un-traced** — the
connected part — which the single-trace refutations never touched.

## What the probe shows (fit-free; [`…connected_probe.py`](../../computations/deltalambda/wlambda_transfer_matrix_connected_probe.py) → witness, 3/3)

**Check 1 — the transfer-matrix trace carries the Lean-proved defect cubic.**
`tr(T) = Z(n) = Σ_λ W_λ`, and `1 − Z(n) = C(n)h² + O(h⁴)` with
`144·C(n) = −n(n−1)(2n−13)` ([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean),
sorry-free). Direct evaluation at `q₀` reproduces the **n = 7 sign change exactly**:

| n | 2 | 3 | 4 | 5 | 6 | **7** | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| `Z(n)` | 0.9946 | 0.9874 | 0.9822 | 0.9822 | 0.9911 | **1.0124** | 1.0506 | 1.1109 |
| `1−Z` | + | + | + | + | + | **−** | − | − |

`Z` crosses 1 at `n = 7` — the transfer-matrix trace **super-normalises** for the
heavier blocks, exactly as the cubic predicts. This is a genuine falsifiable gate any
`W_λ`-transfer-matrix must satisfy, and it does.

**Check 2 — the single bond under-binds (the gap is the connected term).** For the
deuteron pn standard channel `λ=(2,1)`, `n=3`: `W_{(2,1)} = 0.6607`, so
`0.395 < f_pn = 0.588 < 0.6607` (#2528). The single bond **brackets `f_pn` from
above**; the `0.193` shortfall from the bare channel is precisely what a connected
higher-body term must supply — i.e. the bracket miss is *evidence for* the connected
channel, not a refutation of `W_λ`.

**Check 3 — the mechanism: connected part is 0 for diagonal/disjoint, ≠0 for braided.**
The **diagonal** transfer matrix `T = ⊕_λ W_λ P_λ` factorises in the `λ`-basis: two
disjoint/commuting bonds give `tr(2 bonds) − tr(bond)² = 0` (exactly). So the diagonal
`W_λ` weights **alone cannot be extensive** — the connected part vanishes identically.
Extensivity must come from the **non-commuting braid** structure: a repeated/braided
crossing (`σ² =` Hopf) gives `tr_M(σ²) − tr_M(σ)² = 0.855 ≠ 0`. The topological binding
lives in the off-diagonal (braid) part, with `W_λ` injected **per block**.

## Verdict + the honest next step

**Mechanism pinned, no closure.** The correct object is the **non-commuting braid
transfer matrix with `W_λ` injected per Wedderburn block**, read via its **connected
multi-bond part** — not the scalar weighted trace (intensive) and not the diagonal
`W_λ` transfer matrix (connected ≡ 0) and not the single-trace `W_λ`-projected Markov
trace (#2584-exhausted). The falsifiable gates it must hit are already in place: the
defect cubic (n=7 crossing, Check 1 ✓) and the deuteron bracket `f_pn ∈ (0.395, 0.661)`
(Check 2 ✓).

## Follow-on: the ³He/⁴He nuclear-braid probe (PROBE 2 direction)

[`wlambda_nuclear_braid_connected_probe.py`](../../computations/deltalambda/wlambda_nuclear_braid_connected_probe.py)
→ witness (fit-free) runs the connected part on the **actual multi-bond nuclear
braid** (the corpus `internuc_characters` chain of `A(A−1)/2` crossings) for
²H/³He/³H/⁴He/⁶Li/¹²C. It exposes a clean, rigorous structure:

- The **1-dim reps** (`(3)` sym, `(1,1,1)` alt) evaluate the braid as a literal
  **product over bonds** — they **factorise** → disconnected → intensive.
- The **standard `(2,1)` rep** evaluates via a **2×2 transfer-matrix product** over
  the chain — it does **not** factorise. The connected part
  `C_std(K) = V_std_full − ∏_bonds(z·c_b + d_b)` is the genuine many-body term, and
  `(2,1)` is exactly the deuteron `f_pn` channel (#2528).

Results: `C_std = 0` for A=2 (one bond, ✓ sanity); `C_std ≠ 0` for **all** A≥3
(the extensive channel is **non-empty**, and lives entirely in the non-abelian
`(2,1)` rep — `W_{(2,1)}·C_std(⁴He) = 0.673` vs the 1-dim factorised parts `0.334`).

**Honest caveat (the useful negative).** `C_std` is **non-monotone** in bond count
(`3He 0.43, 4He 1.02, 6Li 0.41, 12C 1.22`) and its **per-bond** value **shrinks** for
heavy nuclei (`0.142 → 0.170 → 0.027 → 0.018`). So the **fixed-H₃** braid localizes
the extensive channel but does **not by itself sustain extensivity** past the light
nuclei — consistent (a-scope) with the known r18k det-direction non-monotonicity and
the light-nuclei method breakdown. This says the H₃-level connected part is the right
*channel* but the *A-scaling* needs the jet-tower / higher-Hₙ content (the `W_λ`
geometric realization), not a fixed-n braid.

## Jet-tower lift: the extensive content IS in the tower (positive redirect)

[`wlambda_jet_tower_connected_probe.py`](../../computations/deltalambda/wlambda_jet_tower_connected_probe.py)
→ witness (exact branching, no fit) lifts the connected standard channel over the
**jet tower** `H_k → H_3` (`k = 3..9`), using the universal weight
`w_std(k) = Σ_{λ⊢k} W_λ · mult_{(2,1)}(λ↓H_3)`. The naive expectation (bounded/
convergent tower) was **overturned by the data**:

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| `w_std(k)` | 0.66 | 0.90 | 1.68 | 3.84 | 8.95 | 22.4 | 62.2 |
| std share | 0.67 | 0.53 | 0.52 | 0.53 | 0.51 | 0.51 | 0.51 |

`w_std(k)` **grows geometrically (~2.5×/level, unbounded)** — even though the
*normalised* per-level invariant `a_k` **converges** (the ratio cancels the growth;
`jet_knot_invariants.py`). The connected `(2,1)` channel holds a **stable ~51% share**
at every level. So the jet tower **does** supply the unbounded, extensive-capable
growth the fixed-H₃ braid lacked — it lives in the raw (un-normalised) connected
weight, hidden by the `a_k` normalisation.

**This sharpens the open problem to a single named object:** the **level-selection
rule `k(A)`** — which jet level a nucleus of mass `A` occupies. If `k(A)` grows with
`A` / bond-count, then `w_std(k(A))` supplies the extensive binding. `k(A)` is exactly
**GAP-A-3 "categorical brane-tower level selection"** (gate-status productive
direction). The probe does **not** set `k(A)` or land magnitudes — it establishes that
the extensivity is *available* and pins where the remaining derivation must happen.

**Next (compute):** derive/constrain `k(A)` from the drivers (the categorical
brane-tower level selection, GAP-A-3) — e.g. test whether `k ∝ A` or `k ∝` bond-count
reproduces the AME `B(A)` scaling, gated by the defect cubic + `f_pn` bracket, no fit.
The A-operator `A^λ_{μν}(I)` (`wenzl-A-operator.md`) is the operator-valued bond datum;
its universal (unfitted) form remains the open piece (Track-A, `s5-so3-keystone`).
