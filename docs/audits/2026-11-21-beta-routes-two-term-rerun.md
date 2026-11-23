# The β-decay routes re-run under the covariant two-term trace

Bean `qou-99qc`. Owner, 2026-11-21 04:57: update "the routes that you were trying" to use the
two-term Lagrangian trace. P1/P4 (#8681), P2 (#8680), P3 (#8682), route L (#8693, held) and N2
(#8636) all used only the one-term trace: the convention-D Markov trace at `z_D = q³/(q²+1)`,
which is the quantum trace `Tr(K^{⊗N} ρ(X))/[2]_q^N`.

Pre-registration: `computations/probes/beta_routes_two_term/PREREGISTRATION.md` (committed first,
`d38166d1cb`). Lean: `QOU/QBeta/BetaRoutesTwoTerm.lean` (19 theorems, generic `[CommRing]` /
`[Field]`, no `sorry`, axioms `propext, Classical.choice, Quot.sound`; lean-direct exit 0). Probe and
witness: `computations/probes/beta_routes_two_term/` (14/14). Everything is exact in ℚ(q). Exact
zero tests use q = 2 and q = 3/2. Values are at the proton q₀ to 70 dps. The q → 1 orders are
estimated from exact evaluations at `1 + 10⁻³` and `1 + 10⁻⁴`. Nothing is wired. CODATA appears in
comparison rows only.

## 0. What "two-term" means once a lepton strand is present

The scored object (`two_term_covariant_all_pairs_qtrace`) is built from four pieces:
- the charge insertion `Q_pair = Σ_{i<j} Q_i Q_j`;
- its projection `E` onto the braid commutant (#8552 T5/T6);
- its connected part, i.e. `E(Q_pair)` minus its scalar part on the weight space;
- the derived quantum-trace weighting.

It has only ever been evaluated on three quark strands, and there its connected part is 0.

**Pieces I used that are derived:**
- the trace weighting `K^{⊗N}/[2]^N`;
- the quark charges;
- `E` as the #8552 expectation onto the commutant.

**Pieces that are assumptions or selections:**
- **Lepton strand charges.** I use `ν = u ↦ 0` and `e⁻ = d ↦ −1`. This is the P4/N2 "C-lep"
  convention (the lepton strand is a second doublet in the same `V`). It is not derived.
- **Photon-pair strand charges.** The P1/P4 photon-pair strands have no derived charge. I report
  two colourings: **A** (lepton) and **B** (neutral).
- **The coefficient `c_em`.** It is not derived; its scale is a selection (#8524). So every row
  reports `t₂`, which is `d t/d c_em`, or `t₂/t₁`, which is `d log t/d c_em`.
- **The covariance group** (new here, see below).

**The covariance group is a new choice.** With strands of two charge types, two different
"braid-covariant" projections exist. On the nucleon they coincide.
- **H_N-covariant (pre-registered).** Project onto the commutant of the full `H_N(q)` on each
  total-weight space. That commutant is spanned by the central idempotents `P_λ`, and `P_λ` are
  polynomials in the full twist `Δ²_N`. So `E(Q)` is a function of `Δ²_N`: it braids every strand
  around every other strand, whatever the word does.
- **Colour-block-covariant.** Project only onto the commutant of the colour-preserving algebra.
  `Q_pair` is then constant on each joint block-weight sector (Lean below), so the connected part
  is **identically 0 for every word**, and two-term = one-term on every route.

## 1. Structural results (Lean, `QOU.QBeta.BetaRoutesTwoTerm`)

| theorem | content |
|---|---|
| `offDiag_sum_eq` | `Σ_{offDiag} f_i f_j = (Σ f)² − Σ f²` |
| `pairSum_eq_of_total_eq` | one charge type (common offset, `t_i² = c`): `Q_pair` depends only on the total weight. So it is a scalar on every weight space, and its connected part vanishes against **every word, every N**. This is the general-N form of `deltaT_allPairs_connected_eq_zero`. |
| `pairSum_sub_of_total_eq` | per-strand offsets `y_i`: two configurations with the same total differ by `−2 Σ y_i (t_i − t'_i)`. So with a lepton strand, `Q_pair` is not a scalar on the weight space. |
| `pairSum_union` | for disjoint blocks: the block pair sums plus `2(Σ_s)(Σ_{s'})`. With one charge type per block, `Q_pair` is constant on every joint block sector, so the colour-block-covariant connected term is 0. |
| `covariant_coeff_s/_a`, `trace_conn_one`, `trace_conn_crossing`, `trace_conn_crossing_sq`, `quarkquark_scalar` | one quark strand and one lepton strand under the H_N projection: `E(Q)^conn = κ(P_s − P_a)` with `κ = (q²−1)/(3(q²+1))`. Its trace against `1` is 0, against the crossing `h/3`, and against the wrap `σ²` `h²/3`. Two quark strands give 0. |

The probe reproduces the N = 2 closed form exactly. For N = 3, 4 the commutant coefficients
`c_λ − c̄` are all `∝ (q²−1)`, so they vanish at q = 1, as pre-registered.

## 2. Per-route tables (H_N-covariant two-term against one-term)

Notation:
- `R = t(W)/(t(β)t(Γ)t(bridge))` and `C = t(W) − t(β)t(Γ)t(bridge)` are the #8681 cross term.
- `δlogR = t₂/t₁(W) − Σ_pieces t₂/t₁` is the first-order two-term change of `log R` per unit `c_em`.
- `D` is the K-weighted, dimension-normalised sector difference `(τ_{n⊗ν} − τ_{p⊗e⁻})/12` of P4.

### P1 / P4

| word (Γ = 1) | one-term R | one-term C | δlogR two-term, A | δlogR, B | t₂/t₁ A | P4 D one-term | P4 D two-term cov A | P4 D two-term cov B |
|---|---|---|---|---|---|---|---|---|
| W0_split | 1.0 | 0 (exact) | 2.9513e-5 ·O((q−1)^5) | 5.9e-6 ·O((q−1)^5) | 2.9513e-5 ·O((q−1)^5) | 0 (exact) | 0.0086887 ·O((q−1)^2) | 0.001668 ·O((q−1)^2) |
| W1_one_bridge | 1.0 | 0 (exact) | 0.00012345 ·O((q−1)^4) | 3.2322e-5 ·O((q−1)^4) | 0.016759 ·O((q−1)^1) | 0.14208 ·O((q−1)^1) | 0.0067587 ·O((q−1)^2) | 0.00072424 ·O((q−1)^2) |
| W1sq_clasp | 1.0 | 0 (exact) | 4.0179e-5 ·O((q−1)^5) | 8.9001e-6 ·O((q−1)^5) | 0.0019291 ·O((q−1)^2) | 0.029704 ·O((q−1)^2) | 0.010102 ·O((q−1)^2) | 0.0018194 ·O((q−1)^2) |
| W2_two_same | 1.0 | 0 (exact) | 4.0179e-5 ·O((q−1)^5) | 8.9001e-6 ·O((q−1)^5) | 0.0019291 ·O((q−1)^2) | 0.029704 ·O((q−1)^2) | 0.010102 ·O((q−1)^2) | 0.0018194 ·O((q−1)^2) |
| W2b_two_opposite | 1.0 | 0 (exact) | 2.9513e-5 ·O((q−1)^5) | 5.9e-6 ·O((q−1)^5) | 2.9513e-5 ·O((q−1)^5) | 0 (exact) | 0.0086887 ·O((q−1)^2) | 0.001668 ·O((q−1)^2) |
| W3_loop_around_2 | 1.0002 | 0.00020776 ·O((q−1)^5) | 3.8243e-5 ·O((q−1)^5) | 8.4146e-6 ·O((q−1)^5) | 0.0039902 ·O((q−1)^2) | 0.065995 ·O((q−1)^2) | 0.011774 ·O((q−1)^2) | 0.0019992 ·O((q−1)^2) |
| W4_loop_around_3 | 1.0 | 6.5743e-5 ·O((q−1)^6) | 3.4535e-5 ·O((q−1)^5) | 6.6106e-6 ·O((q−1)^5) | 0.0062196 ·O((q−1)^2) | 0.10956 ·O((q−1)^2) | 0.013779 ·O((q−1)^2) | 0.0022201 ·O((q−1)^2) |
| W4b_two_pair_strands_loop | 1.0 | 0 (exact) | 4.1135e-5 ·O((q−1)^5) | 8.8714e-6 ·O((q−1)^5) | 0.0039931 ·O((q−1)^2) | 0.0038047 ·O((q−1)^3) | 0.012279 ·O((q−1)^2) | 0.0038542 ·O((q−1)^2) |
| W6_passage_and_return | 1.0 | 6.5743e-5 ·O((q−1)^6) | 3.4535e-5 ·O((q−1)^5) | 6.6106e-6 ·O((q−1)^5) | 0.0062196 ·O((q−1)^2) | 0.10956 ·O((q−1)^2) | 0.013779 ·O((q−1)^2) | 0.0022201 ·O((q−1)^2) |
| W7_passage_after_pair | 0.91368 | -0.019825 ·O((q−1)^2) | 0.0097438 ·O((q−1)^3) | 0.0017336 ·O((q−1)^3) | 0.097486 ·O((q−1)^1) | 0.083002 ·O((q−1)^1) | 0.0079383 ·O((q−1)^2) | 0.0013455 ·O((q−1)^2) |

| word (Borromean point) | one-term C | δlogR A | P4 D one-term | P4 D two-term A |
|---|---|---|---|---|
| W0_split | 0 (exact) | 5.9025e-5 ·O((q−1)^5) | 0 (exact) | 0.0086525 ·O((q−1)^2) |
| W1_one_bridge | 0 (exact) | 9.0343e-5 ·O((q−1)^5) | 0.14188 ·O((q−1)^1) | 0.0067432 ·O((q−1)^2) |
| W3_loop_around_2 | 0.00020746 ·O((q−1)^5) | 5.372e-5 ·O((q−1)^5) | 0.0659 ·O((q−1)^2) | 0.011731 ·O((q−1)^2) |
| W4b_two_pair_strands_loop | -0.001483 ·O((q−1)^4) | 0.00010299 ·O((q−1)^5) | 0.0036598 ·O((q−1)^3) | 0.012208 ·O((q−1)^2) |
| W7_passage_after_pair | -0.019797 ·O((q−1)^2) | 0.0096069 ·O((q−1)^3) | 0.082883 ·O((q−1)^1) | 0.0079211 ·O((q−1)^2) |

**Readings.**
1. **Split words stop being multiplicative.** W0 is the split product β ⊗ 1. Under the one-term
   trace its cross term is exactly 0. Under the H_N two-term trace it is not:
   `δlogR = 2.95·10⁻⁵`, order `(q−1)⁵`. The same holds for W1, W1², W2, W2b and W4b, the other
   words with one-term `C = 0`. The cause is the full twist hidden inside `E`, not the word.
2. **P4: n⊗ν and p⊗e⁻ are now separated on the factorised word.** On W0 the one-term `D` is
   exactly 0 (#8681). The covariant two-term `D` is `0.00869` (colouring A) or `0.00167`
   (colouring B), order `(q−1)²`, against the order-0 one-term values elsewhere.
   - Scaled by `S₆ = m_μ[6]!/q⁶ = 47390.9 MeV`, this is `411.8 MeV` per unit `c_em`.
   - Reaching CODATA `Q_β` would need `c_em = 0.00190`. That is a comparison row only; no
     `c_em` is derived.
3. **W7 has the largest two-term shift:** `δlogR = 0.00974`, order `(q−1)³`.

### P2

P2 family A (one-strand attachment; one-term is nucleon-blind):
| (j,k) | t₁(W)/t₁(nuc) p | n | t₂/t₁ p | t₂/t₁ n | t₂/t₁ β_Bor |
|---|---|---|---|---|---|
| (-1,-1) | 0.71136681 | 0.71136681 | 0.025904 ·O((q−1)^1) | 0.028574 ·O((q−1)^1) | 0.0052038 ·O((q−1)^1) |
| (-1,0) | 0.77692578 | 0.77692578 | 0.029288 ·O((q−1)^1) | 0.031921 ·O((q−1)^1) | 0.0087945 ·O((q−1)^1) |
| (-1,1) | 0.87644123 | 0.87644123 | 0.032034 ·O((q−1)^1) | 0.034637 ·O((q−1)^1) | 0.011709 ·O((q−1)^1) |
| (0,-1) | 0.77692578 | 0.77692578 | 0.033214 ·O((q−1)^1) | 0.03658 ·O((q−1)^1) | 0.0088157 ·O((q−1)^1) |
| (0,0) | 0.84852661 | 0.84852661 | 0.036922 ·O((q−1)^1) | 0.040282 ·O((q−1)^1) | 0.012566 ·O((q−1)^1) |
| (0,1) | 0.95721331 | 0.95721331 | 0.039931 ·O((q−1)^1) | 0.043286 ·O((q−1)^1) | 0.015611 ·O((q−1)^1) |
| (1,-1) | 0.87644123 | 0.87644123 | 0.039148 ·O((q−1)^1) | 0.043078 ·O((q−1)^1) | 0.011747 ·O((q−1)^1) |
| (1,0) | 0.95721331 | 0.95721331 | 0.043118 ·O((q−1)^1) | 0.047068 ·O((q−1)^1) | 0.015628 ·O((q−1)^1) |
| (1,1) | 1.0798216 | 1.0798216 | 0.046341 ·O((q−1)^1) | 0.050306 ·O((q−1)^1) | 0.018778 ·O((q−1)^1) |

| family D word | t₁ p | t₁ n | t₂/t₁ p | t₂/t₁ n | route-L δ(Q/κ)/c_em = −t₂/t₁(W_p) (vs one-term log t_n − log t_W) |
|---|---|---|---|---|---|
| D3_strands_2_4,t=-1,k=-1 | 0.26625 | 0.17982 | 0.026662 ·O((q−1)^1) | 0.033888 ·O((q−1)^1) | -0.026662 |
| D3_strands_2_4,t=-1,k=0 | 0.29079 | 0.19639 | 0.029537 ·O((q−1)^1) | 0.036557 ·O((q−1)^1) | -0.029537 |
| D3_strands_2_4,t=-1,k=1 | 0.32803 | 0.22154 | 0.03187 ·O((q−1)^1) | 0.038722 ·O((q−1)^1) | -0.03187 |
| D3_strands_2_4,t=1,k=-1 | 0.90542 | 0.72322 | 0.036818 ·O((q−1)^1) | 0.037832 ·O((q−1)^1) | -0.036818 |
| D3_strands_2_4,t=1,k=0 | 0.98886 | 0.78987 | 0.040983 ·O((q−1)^1) | 0.042014 ·O((q−1)^1) | -0.040983 |
| D3_strands_2_4,t=1,k=1 | 1.1155 | 0.89105 | 0.044364 ·O((q−1)^1) | 0.045408 ·O((q−1)^1) | -0.044364 |
| D4_strands_1_4,t=-1,k=-1 | 0.18969 | 0.13337 | 0.017583 ·O((q−1)^1) | 0.022653 ·O((q−1)^1) | -0.017583 |
| D4_strands_1_4,t=-1,k=0 | 0.20717 | 0.14566 | 0.020411 ·O((q−1)^1) | 0.025357 ·O((q−1)^1) | -0.020411 |
| D4_strands_1_4,t=-1,k=1 | 0.23371 | 0.16432 | 0.022706 ·O((q−1)^1) | 0.027552 ·O((q−1)^1) | -0.022706 |
| D4_strands_1_4,t=1,k=-1 | 1.428 | 1.1205 | 0.045166 ·O((q−1)^1) | 0.047017 ·O((q−1)^1) | -0.045166 |
| D4_strands_1_4,t=1,k=0 | 1.5596 | 1.2238 | 0.04951 ·O((q−1)^1) | 0.051376 ·O((q−1)^1) | -0.04951 |
| D4_strands_1_4,t=1,k=1 | 1.7593 | 1.3805 | 0.053037 ·O((q−1)^1) | 0.054914 ·O((q−1)^1) | -0.053037 |

**Readings.**
- The nucleons p, n, β_Bor and e⁻ are each one charge type, so `t₂ = 0` exactly for each of them
  (`pairSum_eq_of_total_eq`).
- **Family A: the one-term nucleon-blindness is broken.** Families A and B attach the leptons to
  one nucleon strand. Under the one-term trace `t(W)/t(nucleon)` is the same for p, n and β_Bor
  (P2 §1.2, Markov multiplicativity). Under the two-term trace it is not, and this includes the
  fully factorised (0,0): `t₂/t₁ = 0.03692` (p) against `0.04028` (n), order `(q−1)`.
- **Family D.** The one-term trace already separated p from n here. The two-term ratio adds
  `0.001–0.007` to the separation.

### Route L (read-only on #8693)

The additive energy is `κ·log|t|`. Under two terms, `log(t₁ + c_em t₂) = log t₁ + c_em t₂/t₁ + …`.
- **Split balance.** `Q/κ = log t_n − log t_p − log t_e` evaluated piecewise moves by
  `t₂/t₁(n) − t₂/t₁(p) − t₂/t₁(e) = 0` exactly, since each piece is one charge type.
- **The same balance evaluated as a 6-strand word** (family A (0,0)) moves by `−0.0369 c_em`.
- **So route L's additivity on disjoint unions fails at first order in `c_em`** under the H_N
  projection. Under the colour-block projection it holds.
- **Family D balances** move by `−t₂/t₁(W)`, which is between `−0.018` and `−0.053` per unit `c_em`.
  The sign of `Q` is still set by the twist sign `t`, as in the one-term run.
- **P1 `C_log`** moves by `δlogR` (table above).

### P3 (index character)

The index character is the trivial summand, i.e. the weight space `u…u`. That space is
one-dimensional, so every connected insertion vanishes on it. `χ(p) = q²χ(n)` is unchanged, and
P3's sign argument is unchanged.

### N2

N2's reading-3 selection is trace-free in the sense that matters here: it used no charge
insertion and no two-term quantity. Under the two-term trace, each reading-3 trace
`tr(Π_s^λ ρ(w))` (M4 model) gets a first-order term:

| N2 word | sector λ | one-term tr(Π ρ) | two-term cov coeff | c_em of sign change |
|---|---|---|---|---|
| V1V2 | N(3) | 0.40479 | 0.041287 ·O((q−1)^1) | -9.8041 |
| V1V2 | N(2,1) | 0.59521 | -0.031126 ·O((q−1)^1) | 19.123 |
| V1V2 | P(3) | 0.096494 | 0.027157 ·O((q−1)^1) | -3.5532 |
| V1V2 | P(2,1) | 0.8598 | -0.038318 ·O((q−1)^1) | 22.439 |
| V2V1 | N(3) | 0.40479 | 0.041287 ·O((q−1)^1) | -9.8041 |
| V2V1 | N(2,1) | 0.59521 | -0.031126 ·O((q−1)^1) | 19.123 |
| V2V1 | P(3) | 0.096494 | 0.027157 ·O((q−1)^1) | -3.5532 |
| V2V1 | P(2,1) | 0.8598 | -0.038318 ·O((q−1)^1) | 22.439 |
| V1V1V1 | N(3) | 1.0 | 0.041434 ·O((q−1)^1) | -24.134 |
| V1V1V1 | N(2,1) | 1.9942 | -0.03069 ·O((q−1)^1) | 64.979 |
| V1V1V1 | P(3) | 1.0 | 0.027381 ·O((q−1)^1) | -36.522 |
| V1V1V1 | P(2,1) | 1.9942 | -0.037925 ·O((q−1)^1) | 52.582 |


The two-term term does not change the selection while the sign of each trace is unchanged. The
first sign change is at `c_em = −3.55` (`P(3)` of V1V2 / V2V1). So the selection V1V2, V2V1 is
unchanged for any `|c_em| < 3.55`, and it stays identical for n and p.

## 3. Answers to the owner's questions

1. **Does the connected all-pairs QED term become non-zero once a lepton strand is included?**
   - **Under the H_N projection: yes.** It is non-zero at order `h` for a single quark–lepton
     crossing (`trace_conn_crossing`), and it is non-zero even with no crossing at all (the W0 and
     family A (0,0) rows).
   - **Under the colour-block projection: no, never**, for any word (`pairSum_union` +
     `pairSum_eq_of_total_eq`).
   - On the nucleon alone it is 0 under both, which agrees with the scored rows.
2. **Does it separate n and p where the one-term trace did not?**
   - **Under H_N: yes.** It separates n from p on the P4 split word W0 and on the P2 family-A words.
     In both places the separation comes from the full twist inside `E`, not from the word.
   - **Under the colour-block projection: no.**
3. **Scope (a).** No route reaches `Q_β` without choosing `c_em`. The `c_em` values that would land
   on CODATA are reported as comparisons only.

## 4. Decision for the owner: which covariance group defines "two-term" with lepton strands

> **Superseded 2026-11-21 (owner instruction, PR #8743).** The owner did not pick between the two readings below. He asked for the lepton case to be derived the same way the nucleon two-term was: from the Lagrangian, tracked through non-abelian Stokes. PR #8743 (`QOU.QBeta.LeptonTwoTermStokesCovariance`, `docs/audits/2026-11-21-lepton-two-term-from-lagrangian-stokes.md`) does that. Stokes carries the insertion round the closed boundary, which forces the **full braid group with each strand's charge carried with the strand**. The ruled pairs-only insertion is not carried at a quark–lepton crossing; the carried family adds a forced lepton self-energy weight 2/3 and reduces to the ruled all-pairs insertion on three quarks. Its connected part is **exactly 0 on every β route** (91 quantities). So the H_N-covariant non-zero columns of §2 are an **inadmissible comparison** (they hold the charge at a fixed position instead of moving it with the lepton strand), and scored two-term = one-term on every route. Nothing in this section is an open owner decision any more.


Both projections agree on the scored nucleon rows. They differ only once lepton strands are
present.

**Option 1 — H_N-covariant (the pre-registered generalisation).**
- *What it means:* the charge insertion is averaged over the full braid group of all N strands.
- *Costs:* nothing further; it is computed here.
- *Risks:* it makes split words non-multiplicative, which breaks route L's additivity, and its
  n/p separation is produced by `E` rather than by the word. Any number built on it inherits a
  hidden full twist.
- *Commits to:* treating that full twist as physical.

**Option 2 — colour-block-covariant.**
- *What it means:* the insertion is averaged only over braids that keep quark strands with quark
  strands and lepton strands with lepton strands.
- *Costs:* nothing; it is identically 0, which is proved.
- *Risks:* the two-term trace then adds nothing to any β route. Every one-term no-go stands
  unchanged.
- *Commits to:* finding the β-decay signal somewhere other than the pairwise charge insertion.

**Default (if nothing is chosen):** nothing changes. Nothing is wired, and the scored nucleon rows
are the same under both options.

**My judgement:** option 2. It is the projection that keeps split words split, which is the
property every route relied on. Under option 1 the signal comes from the projection rather than
from the braid.

## 5. Pre-registered priors, scored

| prior | outcome |
|---|---|
| PR1 colouring U ⇒ `t₂ ≡ 0` | held: exact 0 on every P1 word (`pairSum_eq_of_total_eq`) |
| PR2 sector-connected ≡ 0 | held for the colour-block sectors, on every colouring tested (probe check + `pairSum_union`) |
| PR3 raw connected ≠ 0 on W0 | held: −4.98·10⁻⁵ (A), 1.96·10⁻⁴ (B) |
| PR4 covariant ≠ 0, vanishes at q = 1 | held: every `c_λ − c̄ ∝ (q²−1)` |
| PR5 P4 two-term separates n⊗ν / p⊗e⁻ on W0 | held: 0.00869 (A) |
| PR6 P3 unchanged | held (one-dimensional space) |
| PR7 no `Q_β` without choosing `c_em` | held |

None of the numbers were used to choose between colourings, projections or words.
