# Pre-registration: N1 — the charged W element, the n → p e⁻ ν̄ amplitude M(q) and the rate 𝔇_n(q)

Bean `qou-99qc` (also bears on `qou-g0jn`, `qou-0whz`). Owner (Carl), 2026-11-20 ~19:25: reject the premise
"the bar image of a photon is a photon" (φ₀, φ₁ stay underived); pursue N1. Re-aim 19:33: *"We are obviously
missing something in q. The β-decay rate should depend on q."* Primary output = the amplitude M(q) and the rate
𝔇_n(q) ∝ |M(q)|² × phase space, as exact functions of q.

**Honesty note on timing.** Before writing this file I ran exploratory sympy on one question: the block of the
braid "lepton strand passes three nucleon strands" between neutron⊗ν and e⁻⊗proton. It gave
`h·q·T⁺` with `T⁺ = Δ²(E)` (Jimbo). Everything below that is not that one block is written before computing,
and the Lean file re-proves that block from the matrices, it does not quote the exploration.

## Fixed inputs (corpus or standard, not chosen here)

* `V = K²`, basis `u` (`K u = q u`), `d`. Jimbo `Ř` (as in #8632 `Rc`): `uu ↦ q uu, ud ↦ du, du ↦ ud + h du,
  dd ↦ q dd`, `h = q − q⁻¹`. `σᵢ` acts as `Ř` on positions `(i, i+1)` of `V^{⊗n}`.
* Nucleon = three strands, neutron weight space `W₋` (one `u`), proton `W₊` (two `u`). `T⁺ = Δ²(E)`, `T⁻ = Δ²(F)`
  as in #8632.
* **Assumption, flagged (same as `qou-g0jn` PRE-REG 3):** the lepton is a fourth strand carrying a second copy
  of the doublet `V`, `ν = u`, `e⁻ = d`. Crossing symmetry: `n → p e⁻ ν̄` is read as `n ν → p e⁻`.

## Definitions (fixed now)

1. **Strand-tracked crossing.** `R := P·Ř` (`P` the swap) re-labels the output by strand identity rather than
   position. The **charged part** of a crossing is the component of `R` that shifts the charge of the strand
   entering on the left by `±1` (grading by `ad(K ⊗ 1)`). The **W exchange** of `σ` is that `+1` component; of
   `σ⁻¹` the `−1` component. No target is used to define it.
2. **β amplitude operator** `A(w) : W₋ → W₊` = the block of `ρ(w)` from `W₋ ⊗ ν` to `e⁻ ⊗ W₊`, for the passage
   words `w` of the lepton through the nucleon: leftward positive `σ₁σ₂σ₃`, leftward negative, rightward
   positive, rightward negative.
3. **|M|²** for a neutron state `v ∈ W₋`: `Σ_f |⟨f|A|v⟩|²` in the tensor basis (standard inner product, real q),
   = `vᵀ AᵀA v / vᵀv`. Reported separately on the isospin-½ eigenspace (the nucleon) and on isospin 3/2.
4. **Rate reading:** `𝔇_n(q) = G² · |M(q)|² · m_e⁵ · f(W₀)/(2π³)`, `f(W₀) = ∫₁^{W₀} p W (W₀ − W)² dW`
   (`F(Z,W) = 1`, Coulomb correction omitted), `W₀ = 1 + Q_β/m_e`. `G` (dimension MeV⁻²) is **not** supplied by
   the construction unless a scale emerges; if not, report the implied scale `Λ = G^{-1/2}` as a diagnostic only.
5. **Q_β inside f** from the same construction, never CODATA: the label-C (T⁺ round trip) closed form of #8623/#8632,
   `Q_β/m_e = (q+1)(q²+1)/(2q³) · [2]²/([2]²+2)` (order-zero `E₀`, posited), and, listed, the owner-scored cell
   0.325434 MeV (D1 = A). Both carried; none selected.

## Predictions, stated before computing (may be wrong)

* P1: the rightward-positive and leftward-negative passages give a zero n→p block (chirality); leftward-negative
  and rightward-positive give the reverse process `p e⁻ → n ν` with `∓q^{∓1}h·T⁻`.
* P2: `|M|² = (hq)²` on isospin ½ and `(hq)²[2]²` on isospin 3/2, so the rate vanishes as `h²` at `q → 1`, is not
  bar-symmetric (mirror passage gives `(h/q)²`), and is increasing in `q` for `q > 1`.
* P3: no MeV scale for `G` emerges (the construction is dimensionless); `Λ` stays a gap.
* P4: with `F = 1`, `d ln f / d ln Q_β` at the label-C Q is well below 5 (Sargent `Q⁵` is the `W₀ ≫ 1` limit).

## Comparison only

`𝔇_n = ħ/τ_n`, τ_n = 878.4 s → 7.493e-25 MeV; Q_β CODATA 0.78233 MeV. Not used anywhere upstream.

## Formalize-first

`QOU/QuarkState/ChargedCurrentW.lean`, generic `[Field K]`, sorry-free, before the probe is committed.
