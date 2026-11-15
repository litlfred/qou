# Quark factor relations (colour ⊗ spin ⊗ flavour ⊗ chirality ⊗ momentum) and the colour channel

Bean `qou-qs4c` (epic `qou-qs0e`). Date 2026-11-15. PR #7823. Lean:
`folio/quantum-observable-universe/lean/QOU/SchurWeyl/ColourChannelSpinStatistics.lean`
(verification status in §6).

## 0. Result in four lines

1. **Settled, conditionally.** Given (i) four separate S₃ factors for colour, spin, flavour and
   space, (ii) Fermi statistics and (iii) the existence of the Δ⁺⁺ (an **empirical** input), the
   colour channel is forced to (1³). Colour (3) and colour (2,1) both give multiplicity 0 for the
   Δ⁺⁺ channel. This is Greenberg's 1964 argument written as a finite S₃ character computation,
   `colour_channel_forced`.
2. **Excluded by a proved invariant (scope b).** A convention-D (level-2) channel cannot host
   colour. The Wenzl weight of (1³) at level r is zero iff ℓ(1³) = 3 > r
   (`QOU.SchurWeyl.WenzlWeightLevelR.wenzlWeight_eq_zero_iff`, sorry-free, generic field). So
   colour needs a level r ≥ 3 factor, and that factor is **not** present in any registered QOU
   channel.
3. **Open.** Whether the substrate supplies a separate colour factor at all. A single three-strand
   Hecke word carries **one** S₃ action, not four. The only established colour-shaped fact is that
   μ̄₁₂₃ transforms in the sign representation; that is statement A of
   `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md` §4. Statement B, "the state's
   colour channel is (1³)", still needs the identification "colour is read off μ̄".
4. **Consequence for the epic hypothesis.** At level 2 the three-strand channels are **isospin**
   channels. (3) is I = 3/2 (Δ) and (2,1) is I = ½ (nucleon). So "project NF(γγ) to (2,1)"
   selects a **nucleon-type three-quark** channel, not a single quark. The two deformed-SL(2)
   papers in `qou-qs3l` place the mixed state at the same composite level.

## 1. Schur–Weyl bookkeeping: what each level can carry

Quantum Schur–Weyl duality says that H₃(q) acting on V^{⊗3} with dim V = N has image
⊕_{ℓ(λ) ≤ N} End(S^λ). At real q > 1, not a root of unity, the Wenzl weight is nonzero exactly
on ℓ(λ) ≤ r.

| level r = N | (3) | (2,1) | (1³) | what it can be |
|---|---|---|---|---|
| 2 (convention D, `z_D = q³/(q²+1)`) | dim 4 | dim 2 (×2) | **0** | one two-valued label: isospin u/d, *or* spin ↑/↓ |
| 3 | 10 | 8 (×2) | 1 | colour SU(3), *or* flavour SU(3) (u,d,s) |
| 6 (spin × flavour, SU(6)) | 56 | 70 (×2) | 20 | spin-flavour |

The dimensions are the hook-content products ∏(N + c)/h. Both 2⁽³⁾ = 4 + 2·2 and
3³ = 10 + 2·8 + 1 check.

**The ambiguity at level 3.** Colour and the eightfold way are **both** level-3 Schur–Weyl. The
octet/decuplet/singlet split (3) ↔ 10, (2,1) ↔ 8 twice, (1³) ↔ 1 is exactly the colour split, so
the Hecke channel alone cannot tell colour from three-flavour. A substrate that carries "level 3"
must still say *which* factor it is. This is the same as premise (i) above.

## 2. The S₃ character computation (Lean, `ColourChannelSpinStatistics.lean`)

The characters are taken from Mathlib data on `Equiv.Perm (Fin 3)`:
- `sym = 1`;
- `anti = sign`;
- `mixed = #fix − 1`.

`chars_orthonormal` checks that the three are orthonormal; with three conjugacy classes they are
the full set of irreducible characters. `signMult c s f x` is |S₃| times the multiplicity of sign
in c ⊗ s ⊗ f ⊗ x.

| colour c | spin s | flavour f | space x | 6 × mult(sign) | physical reading |
|---|---|---|---|---|---|
| (1³) | (3) | (3) | (3) | 6 | Δ, S = I = 3/2 ✓ |
| (1³) | (2,1) | (2,1) | (3) | 6 | N, S = I = ½ ✓ |
| (1³) | (3) | (2,1) | (3) | 0 | no S = 3/2, I = ½ ground state ✓ |
| (1³) | (2,1) | (3) | (3) | 0 | no S = ½, I = 3/2 ground state ✓ |
| (3) | (3) | (3) | (3) | 0 | colour (3) kills the Δ⁺⁺ |
| (2,1) | (3) | (3) | (3) | 0 | colour (2,1) kills the Δ⁺⁺ |
| (2,1) | (3) | (2,1) | (3) | 6 | colour (2,1) instead predicts S = 3/2, I = ½ |
| (1³) | (3) or (2,1) | (1³) | (3) | 0 | no ground-state flavour singlet (eightfold way: no Λ-singlet in the 56) |

**Theorems.**
- `signMult_anti`: with colour (1³) and space (3), the multiplicity is δ(spin, flavour). This is
  the SU(6) 56 = (10, S = 3/2) ⊕ (8, S = ½) structure; 40 + 16 = 56.
- `colour_channel_forced`: only colour (1³) admits spin (3), flavour (3), space (3).
- `no_groundstate_flavour_singlet`, `mixed_colour_excludes_symmetric_flavour`: as in the table.

### μ_p/μ_n = −3/2 follows from the δ(spin, flavour) row, with one more input

Once spin = flavour = (2,1), the nucleon is the unique symmetric combination of the two mixed
channels. With additive quark moments μ_q ∝ Q_q, this gives μ_p = (4μ_u − μ_d)/3 and
μ_n = (4μ_d − μ_u)/3. Taking μ_u = −2μ_d gives μ_p/μ_n = **−3/2**, against the measured
−1.4599 (2.7 %).

The extra input "moment ∝ charge" is **imported from physics** and is not derived here. The
substrate has no derived quark charge yet; see §3, hypercharge.

## 3. The other relations, mapped onto the substrate

**Status** is one of: derived in corpus / conditional / absent. Corpus citations come from
the companion map, `docs/audits/2026-11-15-standard-model-eightfold-way-corpus-map.md`.

| relation | physics content | substrate status |
|---|---|---|
| spin–statistics + colour antisymmetry | colour (1³) ⇒ spin–flavour–space symmetric (SU(6) 56) | **conditional**: §2, given four S₃ factors + Fermi + Δ⁺⁺ |
| μ_p/μ_n = −3/2 | from the 56 + μ ∝ Q | **conditional** + imported charges |
| Lorentz: chirality = helicity when massless; mass mixes L/R | needs momentum and a Dirac structure | **absent** in Hecke-word language. The chirality unit u is a point of S² that no structure fixes (#7818, #7820) |
| weak isospin acts on L only | SU(2)_L on left doublets | a level-2 factor exists (convention D) but nothing ties it to L-chirality. **absent** |
| Q = T₃ + Y, Y chirality-dependent | Y_Q = 1/6, Y_u = 2/3, Y_d = −1/3, Y_L = −½, Y_e = −1 | see corpus map (`sm-hypercharge-invariant`); μ̄₁₂₃ is the candidate second invariant |
| anomaly cancellation ⇒ N_c = 3 | see the note below | **absent** as a derivation |
| CKM | flavour ≠ mass eigenbasis | see corpus map (`sm-params-ckm`) |
| confinement | only colour singlets are asymptotic | the epic hypothesis reads it as "quark labels invisible at order t⁰"; that is not a derivation |
| colour-factor ratio | one-gluon 3̄ : 6 = −2/3 : +1/3, ratio 2 | **measured miss by exactly 2**: level-3 channel gives ratio 1 because \|det T\| = 1 (`computations/probes/level_three_colour_channel_probe.py`) |

### Note on anomaly cancellation (so it is not mis-cited)

Anomaly cancellation does **not** derive N_c = 3 from nothing. Per generation, with
Q_u − Q_d = 1, Q_ν − Q_e = 1 and Q_ν = 0, the condition N_c(Q_u + Q_d) + Q_ν + Q_e = 0 gives
Q_u + Q_d = 1/N_c. So the anomaly fixes the **charges given N_c**; equivalently it fixes N_c given
the measured charges. Writing "anomaly cancellation forces N_c = 3" is correct only with the
charges as input, which is a comparison-boundary statement. For the substrate it relates two
open items (colour level and quark charge); it closes neither.

## 4. Settling "is the colour channel (1³)?" — the scope

| claim | scope | invariant |
|---|---|---|
| colour (3), (2,1) cannot coexist with the Δ⁺⁺ in a four-factor Fermi state | (b) structural | the S₃ character table (`colour_channel_forced`) |
| a level-2 / convention-D channel cannot be the colour channel | (b) structural | `wenzlWeight_eq_zero_iff`: w_{(1³)} = 0 at r = 2 |
| the substrate's colour degree of freedom **is** in channel (1³) | **open** | needs premise (i), a separate colour factor; see §5 |

## 5. Decision for the owner: what carries colour

Measurement (§1, §2) has narrowed this to a structural choice. It needs the owner because it
fixes what the tower *is*.

**Option A: colour is a separate level-3 factor**, tensored with the level-2 isospin factor.
- *Means:* the three-strand word carries colour ⊗ isospin, i.e. the H₃(q) action on
  (ℂ³ ⊗ ℂ²)^{⊗3} at N = 6. §2 then applies verbatim.
- *Costs:* a new channel registration (z₆, or z₃ × z_D), plus a Lean statement that the
  product-level Markov trace factorises. Measured cost of level 3 alone: the probe already runs.
- *Risks:* the colour-factor ratio is already measured off by exactly 2. Making level 3 canonical
  makes that miss a live, framework-level discrepancy.
- *Commits to:* a fourth Hecke structure next to convention D; every convention-D result must be
  re-read as the isospin factor only.

**Option B: colour is read off μ̄₁₂₃** (the Milnor invariant), not off a Hecke channel.
- *Means:* colour is a link invariant, and the (1³) statement is A → B in the 2026-08-29 audit.
- *Costs:* one identification, plus a proof that μ̄ is a state label rather than just an
  alternating invariant.
- *Risks:* the arity-conflation trap (an invariant read as a state); the 2026-08-29 audit already
  warns about it.
- *Commits to:* making μ̄₁₂₃ load-bearing for both the hypercharge programme and colour.

**Option C: no change.**
- *Means:* colour stays an input. The epic's quark-state definition is written at level 2, and
  its (2,1) projection is read as an isospin (nucleon) channel.
- *Costs:* nothing now.
- *Risks:* the definition in `qou-qs1d` then defines a three-quark isospin state while being
  named a "quark state".
- *Commits to:* nothing.

**Recommendation (judgement).** Measure before choosing. Before picking A or B, `qou-qs1d` should
state whether "quark" means one strand or one channel. §0 item 4 and `qou-qs3l` §4 both show the
current hypothesis conflates the two. Choose A only if the factor-2 colour-ratio miss is accepted
as a live discrepancy.

**Default.** Option C: nothing changes, and colour remains an unstated input.

## 6. Verification

- **Lean.** `ColourChannelSpinStatistics.lean`, a library file importing Mathlib only. Status:
  *pending lean-direct verification*; this line is updated in the PR when the run completes.
- **Hand checks.** The S₃ multiplicities in §2 were computed by hand from the character table
  (3 classes, sizes 1/3/2), as independent confirmation of the Lean statements. The dimension
  identities in §1 were checked by hand.
