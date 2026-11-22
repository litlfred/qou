# Pre-registration: single-level binding sum on γγ candidate words (²H, ³H, ³He, ⁴He)

Written and committed **before** any number in this directory is computed. Issue #8983.
Nothing here is fitted, and no word, layout, power or site is chosen by its result. AME2020
enters only as a final comparison column.

## 0. What the corpus fixes, and what it does not

- **Formula.** The corpus binding form is the single-level sum
  `Binding(K) = m_e Σ_{λ ⊢ 3A} y_λ(q) χ^λ(β_K) Δ_λ`
  (`mass-endomorphism/recomputed-low-isotope-mass-table.md` §"Direct binding formulation";
  `mass-theory/two-row-stratum.md:22`; `appendix-mass-binding-algorithms/mba-chain-map.md` row 9b).
  There `𝔪(K) = (Z m_p + N m_n) + Binding(K)`, so `Binding` is a **mass shift**: a bound
  nucleus has `Binding < 0`. The comparison quantity is therefore `B_pred := −Binding`.
- **Δ_λ** `= (−1)^{n(λ)} f^λ`, `n(λ) = Σ_i (i−1) λ_i`, `f^λ` the number of standard tableaux
  (`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, sorry-free). For a two-row
  `λ = (n−k, k)`, `n(λ) = k`.
- **y_λ.** The convention-D Markov (Ocneanu/Wenzl, SU(2) Schur–Weyl) weight,
  `y_λ = s_λ(1, q) / Σ_μ f^μ s_μ(1, q)` by hook-content with N = 2
  (`computations/y_lambda_su_n.py::y_lambda_su_n(n, q, 2)`), normalised `Σ y_λ f^λ = 1`. For a
  two-row shape it equals `[λ₁ − λ₂ + 1]_q / [2]_q^n` (balanced q-integers), and it implies
  `z_D = q³/(q²+1)` (`z_from_weights`). For `ℓ(λ) ≥ 3` it is exactly 0
  (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`).
- **q₀**: proton pin, `qou_substrate.constants.q_at(70)`. `m_e`: `qou_substrate.constants.M_E_MEV_STR`.
- **Letters.** Hecke generator `σ_g` with eigenvalues `q`, `−q⁻¹`; `σ_g⁻¹ = σ_g − h`,
  `h = q − q⁻¹`. Vertex `V(s) = σ_s σ_{s+1}⁻¹` on strands `s, s+1, s+2` (0-based generators).
- **Not fixed by any ruling:** a γγ word per multi-nucleon nucleus. Everything below is the
  PR #7741 candidate family (`computations/probes/h2_gg_atom/results.md`), not a ruled word.
  Not fixed either: whether `Binding` of the nucleus should be read against the bond-free word.
  Both readings are reported (§3); neither is chosen.

## 1. Candidate words (the whole enumeration space)

Strands `3A`. Nucleon `j` occupies strands `3j, 3j+1, 3j+2`.

- **Nucleon block** `N_j = V(3j)^m`, `m ∈ {3, 6}`. These are the only powers that pass reading 3 on
  H₃ in #7741 (`m = 3` is `β_Bor = V³`, the 2026-11-21 working conjecture; `m = 6` is the core
  twice). Proton and neutron are the **same word**, so **³H and ³He are the same word** and get the
  same number. There is no flavour and no Coulomb term. This is a consequence of the grammar, stated now.
- **Bond letter** at interface `j` (between nucleon `j` and `j+1`, cut between strands `3j+2` and
  `3j+3`): `K_j = V(s_j)^k` with `s_j = 3j + o_j`, `o_j ∈ {1, 2}` (the two vertices that straddle
  the cut; for A = 2 these are sites 1, 2, mirroring #7741's sites 4, 5), and `k ∈ {1, 2, 3}`.
  `k = 3` (V³) is the power that passed in #7741 H₂; `k = 1, 2` are evaluated too. The power `k`
  is the same at every interface; the offsets `o_j` run over **all** `2^{A−1}` patterns.
- **Free word** (`k = 0`): `N_0 ⋯ N_{A−1}` with no bond letter.
- **Layout.** Chain only: a vertex couples adjacent strands, and `StrandLayoutForcesChain.lean`
  (PR #8969) records that the strand layout admits only adjacent-block bonds. Two bond orders
  are computed: ascending `N_0⋯N_{A−1} K_0 K_1 ⋯` and descending `N_0⋯N_{A−1} ⋯ K_1 K_0`.
- **Formation routes.** Sequential (`N_0N_1K_0N_2K_1N_3K_2`, the p+³H route) and D+D
  (`N_0N_1K_0 N_2N_3K_2 K_1`) for ⁴He, and sequential for ³H. **Prediction made now**: every
  formation route equals the assembled ascending word as a Hecke element, because each
  reordering only moves letters past letters on disjoint strands (`|g − g'| ≥ 2`). This is checked
  two ways: a commutation normal form of the letter strings, and a numerical character match on
  one ⁴He row per route. The two bond orders differ only when two bonds share a strand, which
  happens for offset pattern `(…, 2, 1, …)` at consecutive interfaces.
- **Nucleon alone** (A = 1, n = 3): `V^m`, `m ∈ {3, 6}`.

Row count (before dedup by commutation normal form): ²H `2 × (1 + 3·2·1)` = 14,
³H/³He `2 × (1 + 3·4·2)` = 50, ⁴He `2 × (1 + 3·8·2)` = 98, nucleon 2.

## 1a. p–n difference at q = 1 (owner working assumption 2026-11-22, not a ruling)

Owner working assumption (recorded on PR #8804): `m_p = m_n` at `q = 1`, and
`FlipSymmetryAtOne.lean` proves `n − p = 0` at `q = 1` for every braid word. In this family the
proton and neutron are the same word `V^m`, so every p–n difference (³H − ³He, and the
nucleon itself) is **identically 0 at every q**, in particular at `q = 1`. No candidate carries a
static charge or p–n term, so none conflicts with the assumption. The flip side is that this
family cannot produce any ³H/³He splitting; that is reported, not repaired. The q = 1 p–n
difference is still checked numerically for every A = 3 row (the ³H and ³He words are built
separately with their own p/n labels and compared at q = 1 and at q₀).

Prior work read (beans mount): `qou-46ys` (convention D keeps 7 of 77 blocks at ⁴He;
`Σ y_λ f^λ = 1` under D at n = 3…12), `qou-ales`, `qou-99qc`, `qou-a1hh`.

## 2. Computation

- `χ^λ(W)` for every **two-row** `λ ⊢ 3A`: Rust MPFR kernel
  `pyhecke_native.lp_accumulator_step_traces_mpfr` (one chain = the whole word, 70 dps, q as a
  70-digit string; true trace = `t·e^{ℓ}`). Cross-checked against an mpmath (70 dps) seminormal
  representation built here, which is also used for reading 3.
- **Three-row blocks** (`y_λ = 0`): their `χ^λ` is computed with the same kernel for every row at
  n = 6 and n = 9, and at n = 12 for the m = 3, k ∈ {0, 3}, uniform-offset rows only (the large
  three-row blocks at n = 12 cost seconds each). Their contribution to the sum is reported as
  `y_λ · χ^λ · Δ_λ`, which must be exactly 0; `y_λ` is checked to be exactly 0 from
  `y_lambda_su_n`.
- **Reading 3, every level** (as in #7741): close strands from the top with the convention-D
  Markov conditional expectation, and require `χ_μ(E_{n→m} W) ≥ 0` (tolerance `−1e-40`) for every
  two-row `μ ⊢ m`, `m = 1…n`. Computed from the diagonal of `W` in the seminormal basis.
- **Sum.** `Binding = m_e Σ_{λ two-row} y_λ χ^λ Δ_λ` (the three-row terms are zero), with each
  block's term reported.
- No float arithmetic anywhere; floats only inside display strings.

## 3. What is reported, per nucleus and per row

1. `Binding` (MeV), its sign, and `B_pred = −Binding`.
2. Per two-row block: `y_λ`, `χ^λ`, `Δ_λ`, and `m_e y_λ χ^λ Δ_λ`.
3. Reading 3: pass/fail, failing levels, the negative characters.
4. Bond-relative reading: `B_bond := −(Binding(word) − Binding(free word, same m))`. Also
   `A · Binding(nucleon alone)` beside `Binding(free word)`, as a diagnostic only.
5. The trace ratio `tr_M(word)/tr_M(free)` (reported, not used, ruling B of 2026-11-15).
6. Comparison columns, last: AME2020 `B` (`computations/substrate/codata_constants.py`), and the
   old `unified_iterative_correction(Z, N)` at the production cutoff `K_PARTITION_MAX = 11`
   (run here, recorded as that producer returns it).

No row is ranked, preferred or adopted. If several rows pass reading 3 they are all reported.

## 4. Calibration (must pass before results are read)

- C1: kernel and mpmath seminormal agree on every two-row `χ^λ` of every row to 1e-50.
- C2: `χ_(2,1)(V³) = −(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/q⁶` (#7741 closed form) to 1e-50.
- C3: `tr_M(σ_0) = z_D = q³/(q²+1)` from the two-row `y_λ` at n = 2, 3, 6.
- C4: Markov property of the conditional expectation: `χ_μ(E_{n→n−1}(x σ_{n−2}))`
  `= z_D · χ_μ(x)` for a test `x ∈ H_{n−1}` (n = 6).
- C5: `y_λ = 0` exactly for every three-row `λ ⊢ 6, 9, 12` from `y_lambda_su_n`, and the two-row
  `y_λ` from that function equal `[λ₁−λ₂+1]/[2]^n`.
- C6: every formation route and every commutation-equal pair gives the same characters (§1).

## 5. Outcomes (stated before computing)

For each nucleus, the result is one of:
- **(a)** some rows pass reading 3 with `B_pred > 0`;
- **(b)** rows pass reading 3 but every passing row has `B_pred ≤ 0`;
- **(c)** no row passes reading 3.
Reported for both the direct reading (item 1) and the bond-relative reading (item 4). Any
agreement or disagreement with AME is reported as a comparison only.

## 6. Scope

Scope (a): this candidate family (nucleon `V^m`, `m ∈ {3,6}`; bonds `V^k`, `k ≤ 3`, at
straddling vertices; chain), convention D, proton pin. A negative result here excludes nothing
outside this family.
