# Pre-registration — nucleon split from the position-labelled `V³` diagonal

Beans `qou-myts` (nucleon split, route list), related `qou-99qc`. Route named "not excluded" in
`docs/audits/2026-11-27-nucleon-charge-dressed-words.md` §4. Written before any MeV value of this
route is computed. Disclosure: the symbolic closed forms of the six diagonal entries are already on
`main` (`BorromeanRingColouredTrace.lean`), and the operator symmetry of §3 below was checked
symbolically in sympy while writing this file. The proton anchor `q₀ = 1.10997858…` and
`E₀ = 4.18598136329 MeV` were read from the sibling audits. No ratio `τ_p/τ_n` at `q₀`, no MeV value
of this route and no comparison with CODATA had been computed.

## Object

As in `computations/probes/borromean_ring_coloured_trace/PREREGISTRATION.md`: `V = K²`, level-2
Jimbo braiding, `V³ = (σ₁σ₂⁻¹)³`, colouring `c : Fin 3 → {u, d}`,

  `τ_c = q^{2T³(c)} ⟨c|V³|c⟩ / [2]_q³`   (`tauP` on `W_p = {uud, udu, duu}`, `tauN` on `W_n = {udd, dud, ddu}`).

Indices: `W_p` index `i` = `uud, udu, duu` (the `d` sits at strand `2 − i`); `W_n` index `j` =
`udd, dud, ddu` (the `u` sits at strand `j`).

## Formula (fixed in advance)

Gibbs map of route 1 (`NucleonSplitGibbsCoulomb`), with no Coulomb term:

  `m_n − m_p = E₀ · log(τ_p(c_p) / τ_n(c_n))`,  `E₀ = k_BT_q` (route T, `qbeta_e0.order_zero`).

The tower form `qbeta_e0.canonical` is printed as a labelled second column. `[2]_q³` cancels in
the ratio. A pairing whose ratio is `≤ 0` at `q₀` is reported as "log undefined", not dropped.

## Pairings reported (all of them, whatever the numbers)

The nine pairs `(c_p, c_n)` split as follows.

* **(a) Same position** (odd quark on the same strand `k`; `c_n` is the complement of `c_p`):
  `k = 0`: `duu ↔ udd`; `k = 1`: `udu ↔ dud`; `k = 2`: `uud ↔ ddu`.
* **(b) β-decay single-strand flips** (`c_p` obtained from `c_n` by turning exactly one `d` into
  `u`): `udd → uud, udu`; `dud → uud, duu`; `ddu → udu, duu`. These are the other six pairs.
* **(c) Class averages.**
  * class sums: `Σ τ_p / Σ τ_n = q²` (proved on main, `epsP_V3_eq_qsq_mul_epsN_V3`) — the cell
    `2E₀ log q` of #9475;
  * geometric mean: `(Π τ_p / Π τ_n)^{1/3}`. Any perfect matching of the three proton and three
    neutron colourings (in particular (a)), and the six pairs of (b) taken together, have this same
    mean log, so (a)-averaged and (b)-averaged coincide.

## Selection rule (fixed before numbers)

No pairing is selected by closeness to CODATA. A pairing is selected only by the structural
argument below; if the argument fails in Lean, no pairing is selected.

**Structural argument (strand reversal).** Let `J` reverse the strands (`i ↦ 2 − i`; on both weight
spaces it is the antidiagonal permutation). Symbolically:

  `J ρ(σ₁)(q) J = ρ(σ₂)(q⁻¹)⁻¹`, and since the `ρ(σᵢ)` are symmetric matrices,
  `J · V³(q) · J = V³(q⁻¹)ᵀ` on `W_p` and on `W_n`.

So the word `(σ₁σ₂⁻¹)³` is fixed by **strand reversal ∘ bar (`q ↦ q⁻¹`) ∘ word reversal**. On the
diagonal this reads `⟨rev c|V³|rev c⟩(q) = ⟨c|V³|c⟩(q⁻¹)`: strands 0 and 2 are exchanged together
with the chirality (`q ↦ q⁻¹` is the mirror), and strand 1 is the unique fixed strand. Of the nine
pairs, the only one fixed by this symmetry is the middle same-position pair **`udu ↔ dud`**, whose
braid part is bar-invariant (independent of the mirror choice of the word). Choosing strand 0 or 2
instead is a choice of chirality, which the word does not make.

Pre-registered headline: **pairing (a), `k = 1`, `udu ↔ dud`**. All other pairings are reported
beside it, unselected.

## Scope caveat (carried, not resolved)

`BorromeanRingColouredTrace` point 2: diagonal entries are not conjugation-invariant, so a
per-colouring `τ_c` is a boundary condition on the open braid, not an invariant of the closed
Borromean rings. The symmetry above is a symmetry of the chosen word, not of its conjugacy class.
Whatever the headline gives, it is labelled with this caveat; it is not a link-invariant prediction.

## Numbers (only after the Lean file checks)

80 dps, proton `q₀` (`q_at`), muon anchor as a cross-check, mpmath only. Columns: exact ratio,
ratio at `q₀`, `E₀ log(ratio)` (order zero and tower), then the CODATA column. Gap to CODATA is
printed for every row; it decides nothing.
