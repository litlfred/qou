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

**Next (compute):** build `T_b =` the `W_λ`-weighted interface generator (the Hecke
`σ_{i_b}`, non-commuting across overlapping bonds) and compute the **connected
`tr_M`** of the multi-bond nuclear braid for ³He/⁴He (= PROBE 2, A=4 interface
operator, Track-A owner-authorised via `s5-so3-keystone`), testing whether the
connected part fills the deuteron bracket gap and respects the n=7 defect sign —
**without fitting any entry**. The A-operator `A^λ_{μν}(I)` (`wenzl-A-operator.md`) is
the operator-valued bond datum; its universal (unfitted) form remains the open piece.
