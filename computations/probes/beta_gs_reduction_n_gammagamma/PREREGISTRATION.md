# Pre-registration — β decay as ONE Gröbner–Shirshov reduction (P1, then P4)

Written 2026-11-20, before any number in this directory was computed. Bean `qou-99qc`.
Owner (Carl, 2026-11-20 20:52): *"A beta decay is not standalone. It is a particle interaction.
Perhaps an entangled particle or something but it is a Gröbner basis calculation at the end of
the day."*

Today's no-gos (#8616, #8639, #8661, #8623, hypercharge) all assumed the nucleon and the leptons
FACTORISE: separate words, separate traces. This probe builds one word in which nucleon strands and
lepton/photon strands share a braid, reduces it to normal form, and asks whether the trace of the
entangled word differs from the product of traces (a "cross term"), and what Q the same energy
functional assigns.

## Engine and conventions (fixed now)

* `H_N(q)`, N ≤ 6, generators `σ_i` (0-based), `σ_i² = h σ_i + 1`, `h = q − q⁻¹`. Normal form =
  standard basis `T_w`, `w ∈ S_N` (the Gröbner–Shirshov normal form of the Hecke presentation:
  every word reduces uniquely to `Σ_w c_w T_w`). Exact over `ℚ(q)` (sympy), photon weights symbolic.
  Validated against the corpus before use: `NF(β_Bor)` of #8634, the `e⁻` coordinate
  `φ₀₁ψ₀ + φ₁ψ₀₁` of `pairNFChiral_eq`, and `tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`
  (`BorromeanMarkovTrace.lean`, used by `m_p_substrate_identity_50dps.trM_borromean`).
* Trace: Ocneanu–Markov, `tr(1) = 1`, `tr(x σ_{n}) = z tr(x)`, convention D `z = q³/(q² + 1)`
  (the owner-ruled convention; validated by the closed form above).
* Words. Nucleon `β_Bor = V³`, `V = σ₀σ₁⁻¹` (the γγ-selected core; #8636 proves the γγ + reading-3
  selection gives the SAME element for n and p on three strands, so n and p are one Hecke element and
  their flavour lives in states). Photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁ σ₀σ₁⁻¹` (owner-ruled),
  pair `Γ = γ(φ)γ(ψ)`, weights symbolic (owner: `φ₀, φ₁` underived). Electron: BOTH corpus readings —
  `e⁻_BW = σ₀σ₁σ₀` (breit-wheeler-pair-production) and `e⁻_K = σ₀³` on two strands (`T(2,3)`,
  def:electron-knot). Antineutrino: identity strand (`def:antineutrino-knot`, unknot; the `L₀`
  smoothing).

## P1 — the words

On six strands, nucleon on 0–2 (`σ₀, σ₁`), pair on 3–5 (`σ₃, σ₄`), bridge letters `σ₂`:

| id | word | inter-sector crossings |
|---|---|---|
| W0 | `β_Bor · Γ'` (split) | 0 |
| W1 | `β_Bor · σ₂ · Γ'` | 1 |
| W2 | `β_Bor · σ₂ · Γ' · σ₂` | 2 (same sign) |
| W2b | `β_Bor · σ₂ · Γ' · σ₂⁻¹` | 2 (opposite sign) |
| W5 | `β_Bor · Γ''` on FIVE strands, pair on 2–4 (shared strand 2) | shared strand |

(`Γ'`, `Γ''` = `Γ` with `σ₀ ↦ σ₃, σ₁ ↦ σ₄`, resp. `σ₀ ↦ σ₂, σ₁ ↦ σ₃`.)

**Cross term** `C(W) := tr(W) − tr(β_Bor)·tr(Γ)·tr(B)`, where `B` is the bridge letters alone
(`tr(1)=1`, `tr(σ)=z`, `tr(σ²) = hz + 1`, `tr(σσ⁻¹) = 1`). **Channel split of the normal form**:
the part of `NF(W)` on the parabolic `S₃ × S₃` (strands 0–2 | 3–5) versus the rest (cosets that mix
the sectors); and the `e⁻_BW` channel = the coefficient block on `T_u ⊗ T_{σ₃σ₄σ₃}`.

## Energy functional (the SAME one for initial and final)

`E_N(X) := m_μ · |tr(X)| · [N]_q!/q^N`, `m_μ = m_e Vol(4₁)/ℏ_q²` — at `N = 3, X = β_Bor` this is
`m_μ F_Bor` of the canonical nucleon identity `m_p = 2(m_μ F_Bor − 6 m_e)`. The `2(· − 6 m_e)`
dressing is defined only for three-strand nucleon words (and its 12 is owner-ruled a FIT), so it is
reported as an alternate, never folded into Q.

* **Principal Q.** `Q = E_6(W_init) − E_6(W_fin)`, `W_init` = a row of the table above,
  `W_fin = β_Bor ⊗ e⁻_K(σ₃³) ⊗ ν̄(strand 5)` (free products, same strand count). p and n are the same
  element (#8636), so this is the only place the leptons can enter.
* **Alternates (reported, not selected):** A1 `W_fin` with `e⁻_BW = σ₃σ₄σ₃`; A2 additive,
  `Q = Σ E_{N_i}(initial pieces) − Σ E_{N_i}(final pieces)`; A3 `E` applied to the `e⁻_BW` channel
  block of `NF(W_init)`.

## P4 — strand-colour reading with the derived charged current

Jimbo `Ř` on `V^{⊗N}` (`V = span(u, d)`, `u ↦` `T³ = +½`; `uu ↦ q uu, ud ↦ du, du ↦ ud + h du,
dd ↦ q dd`, as `ChargedCurrentW.Rc`, branch `claude/qbeta-n1-charged-w-element-2026-11-20`). Lepton
strands are a second doublet `ν = u, e⁻ = d` (an assumption carried over from #8638, not derived).
Words on N = 5 and N = 6: nucleon `β_Bor` on 0–2, lepton strand passing the nucleon with
`σ₂σ₁σ₀` (the #8638 passage), photon pair / spectator on the remaining strands. Sector traces
`τ_S(X) = Tr(Π_S ρ(X))` on the nucleon-`T³` sectors `n ⊗ ν` and `p ⊗ e⁻` inside one total-weight
space, both plain and `K`-weighted, each also normalised by `dim Π_S`. Energy difference
`Q₄ = S_N (τ̂_{n⊗ν}(W) − τ̂_{p⊗e⁻}(W))` with `S_N = m_μ [N]!/q^N`. First confirm that
`Σ_S τ_S^{K}` reproduces the Ocneanu trace at `z_D` (fixes the K normalisation), else report the
mismatch and stop that reading.

Cost profile first: time one `H_6` product and one `V^{⊗6}` evaluation; if `H_6` is infeasible in
< 60 min here, report the bottleneck and fall back to `H_5`.

## Priors (stated before computing)

* **PR1 (90 %).** `C(W0) = C(W1) = C(W5) = 0` identically in `q` and the photon weights — the Markov
  trace is multiplicative under split union and under a one-strand (connected-sum) join. Scope (b):
  the invariant is the Markov property. So "n ⊗ γγ" built by concatenating the two words does NOT
  escape the factorisation no-gos.
* **PR2 (85 %).** `C(W2) ≠ 0` (two inter-sector crossings close to a non-split, non-connected-sum
  link). `C(W2b)` uncertain (50 %).
* **PR3 (99 %).** `e⁻_BW = σ₀σ₁σ₀` closes to a TWO-component link (permutation `(0 2)`), not to
  `T(2,3)`; its trace is `z(hz + 1)`. Recorded as a corpus inconsistency with def:electron-knot.
* **PR4 (85 %).** `E_3(e⁻)` and `E_2(e⁻_K)` ≫ `m_e`: the mass functional does not reproduce CAL-1 on
  the electron word, so the principal Q is dominated by the lepton self-energy and is NOT near
  `Q_β^CODATA = 0.78233 MeV` (miss > 10×).
* **PR5 (70 %).** In the strand-colour reading the dimension-normalised sector traces of the
  entangled charged-current word differ between `n ⊗ ν` and `p ⊗ e⁻` (the escape #8616 forbids for
  factorised words); the resulting `Q₄` does not land within 10 % of CODATA (75 %).
* **PR6 (80 %).** `H_6` exact reduction of all P1 words is feasible in < 60 min on this container.

Nothing in this directory is wired to the dashboard. CODATA `Q_β` is read only in the final
comparison block. No value is chosen by its residual.
