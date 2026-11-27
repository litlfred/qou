# RESULT — residual symmetry of the convention-D colour twist (bean `qou-ni4b`)

Owner question: what does the residual `U_q(gl₂) × U(1)` of the D twist mean? It looks
electroweak-like.

- Pre-registration: `PREREGISTRATION-d-residual-symmetry.md`, commit `3f7b5b43e13`. It was pushed
  before the probe existed.
- Probe: `qcd_d_residual_symmetry_probe.py` (commit `3b45170517a`).
- Output: `qcd_d_residual_symmetry_probe.out.json` (commit `055432050b4`).
- **27/28 checks pass.** The one FAIL is a pre-registered prediction that was wrong (R3, below).
  It is kept as a FAIL.
- Exact sympy over ℚ(q). No float, and `q₀` is not used.
- Calibration: the dual adjoint action reproduces two results of the T1 probe. The pivotal
  `diag(q⁻⁴,q⁻²,1)` is fully invariant, and the support-{1,2} twist has stabiliser
  `{E₁,F₁,K₁,K₂}`.

## Claim

**The residual symmetry does not read as electroweak.** It is what is left of the colour
`U_q(gl₃)` once one colour direction is projected out. Convention D on `(ℂ³)^⊗n` is the `U_q(gl₂)`
quantum trace on the sub-module `(ℂ²)^⊗n`, extended by zero.

The twist forces exactly two things:

1. a 2+1 split of the colour space;
2. the selection rule "only the `N₃ = 0` sector contributes", where `N₃` is the occupation number
   of the projected-out colour.

It forces none of the three things an electroweak reading would need:

- a U(1) charge normalisation;
- a nonzero U(1) charge on any corpus particle word;
- a parameter-free mixing ratio.

## Per test

| | result | scope |
|---|---|---|
| **R1** branching | `K_D = g·M`, with `g` the gl₃ pivotal and `M = q·P₁₂` (the projector off colour 3). `K_D` restricted to ℂ² is the `U_q(gl₂)` pivotal; the invariant twist space is 1-dimensional. `ℂ²⊗ℂ²` is Ř-stable and Ř restricted to it is the gl₂ Jimbo Ř. `tr_{(ℂ³)^n}(K_D^n X) = tr_{(ℂ²)^n}(g₂^n X|)` for every `T_w`, n ≤ 3. The Cartan elements commuting with gl₂ span `diag(1,1,0), diag(0,0,1)`; mod the centre (`= n` on a fixed tensor power) one U(1) is left, `N₃`. **Forced:** `K_D^{⊗n}·N₃ = 0`. **Not forced:** charge values. The traceless representative `∝ diag(1,1,−2)` is a convention. Orientation: the doublet twist ratio `d₁/d₂` is `q⁻²` under the T1 Ř (h on `e₁e₂`) and `q²` under the `OverStrandWeight` Ř (h on `e₂e₁`). This agrees with `ptr_markov` (`K = diag(q,q⁻¹)` there). | exact, n ≤ 3 for the trace identity; the structural statements are general |
| **R2** commutation and word charges | `N₃`, `Δ(K₁)` and `Δ(K₂)` commute with every `σᵢ` (n = 2, 3). `N₃` commutes with `Δ(E₁)` and `Δ(F₁)`, so it is central in the residual. `tr(K_D^n[N₃,T_w]) = tr(K_D^n N₃ T_w) = 0` for every `T_w`. **Adjoint U(1) charge `[N₃, ρ(w)]` is 0** for the photon `1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹` (φ symbolic), the electron `σ₀σ₁σ₀`, the trefoil backup `σ₀³`, the quark letters `σ₀^{±1}` and `σ₁^{±1}`, and `V³`. | **(b)** for every word in every `H_n`. Invariant: Schur–Weyl, so `ρ(H_n)` lies in the commutant of `U_q(gl₃) ∋ N₃`. This is consistent with `no_scaling_of_hecke`. The U(1) labels colour **states**, never braid words. |
| **R3** which colour is off | {1,2} keeps `E₁, F₁`; {2,3} keeps `E₂, F₂`; both keep `K₁, K₂` (n = 1, 2). **{1,3}: pre-registered prediction "Cartan only" FAILED.** The Chevalley generators that survive are only `K₁, K₂`, but `E₁₃ = E₁E₂ − qE₂E₁` and `F₁₃ = F₂F₁ − q⁻¹F₁F₂` are invariant at n = 1 and n = 2. Post-hoc check: they are `e₁₃` and `e₃₁` and satisfy `[E₁₃,F₁₃] = (K₁K₂ − (K₁K₂)⁻¹)/(q−q⁻¹)`. So a root-(α₁+α₂) `q`-sl₂ survives. **All three supports leave a rank-1 `U_q(gl₂) × U(1)`**, each for the colour pair kept. All three give identical `y_λ` (same eigenvalue multiset `{q⁻³, q⁻¹, 0}`, checked n ≤ 6, and true for all n since `s_λ` is symmetric). | Invisibility to `H_n`: **(b)** (symmetric functions). **The choice of which colour to switch off is not forced by anything on the Hecke side.** Using {1,2} is a **selection** (a colour-basis choice), flagged as such. It has no consequence for any `H_n` observable. |
| **R4** ratios (coincidence checks only) | Traceless U(1): singlet/doublet = **−2** on both simple-root supports. This is forced only by sl₃ tracelessness; adding the centre `t·Id` gives `t/(t+1)`, which is free. The would-be mixing `Tr T₃²/(Tr T₃² + Tr Y²) = 1/(12s²+1)` depends on the free U(1) scale `s`. `Tr(T₃·Y) = 0`. **No Weinberg angle is forced.** The −2 has the same arithmetic as flavour hypercharge `(1/3,1/3,−2/3)` and as `Q_u/Q_d = −2`. That match was declared in advance as a coincidence check and is not evidence. | (b) for "no normalisation-free ratio" (explicit one-parameter families) |

D-trace values recorded as data (normalised by `(tr K)^n`):

- quark letters `σᵢ`: `z_D`;
- quark letters `σᵢ⁻¹`: `1/(q(q²+1))`;
- electron `σ₀σ₁σ₀`: `q³(q⁴+1)/(q²+1)²`, which equals `z_D·tr(σ₀²)`, consistent with Markov;
- photon: `(q⁴+2q²+1 + (φ₀+φ₁)(q⁵+q³) + φ₀₁q²)/(q²+1)²`.

## What is established and what is not

Established (exact):

- The residual `U_q(gl₂) × U(1)` is a **subalgebra of colour** `U_q(gl₃)`.
- Its U(1) is `N₃`, the count of the switched-off colour, modulo the centre.
- D sees only `N₃ = 0`: D is the gl₂ quantum trace on `(ℂ²)^⊗n ⊂ (ℂ³)^⊗n`.
- No braid word carries U(1) charge (Schur–Weyl).
- The charge normalisation and any mixing ratio are free parameters, not outputs.
- All three choices of switched-off colour are invisible to `H_n`.

Not established, and stated as a **reading argument, not a proved invariant**: that the
residual is "not electroweak".

- Standard-Model SU(2)_L × U(1)_Y commutes with colour, and a subgroup of colour does not.
- This excludes the identification **only if** ℂ³ here is colour. If ℂ³ were reinterpreted as
  something else, that would be a new modelling choice.
- In the searched class (diagonal twists on ℂ³, Jimbo coproduct, n ≤ 3 explicit), no
  electroweak structure was found. Scope (a) beyond the (b) items above.

Not attempted:

- assigning colour states to corpus particles. The corpus does not fix one, and choosing one to
  produce a target charge would be selection;
- non-diagonal twists;
- ℂ³ ⊗ flavour.

The gluon is not identified.

## Post-hoc findings (labelled)

1. **Post-hoc. My pre-registered R3 prediction was wrong.** I reasoned that `M = g⁻¹K =
   diag(q,0,q⁻¹)` is not a projector and so only the Cartan survives. That heuristic is wrong
   for non-simple root vectors: the root-(α₁+α₂) `q`-sl₂ survives on {1,3}. The FAIL is kept in
   the output. The corrected statement is that all three supports have isomorphic residuals.
2. **Post-hoc.** On {1,2}, `E₁E₂` (c = 0) and, on {2,3}, `F₂F₁` show as invariant. This is
   trivial: anything of the form `x·E₁` is invariant once `E₁` is, because it lies in a left
   ideal. It is not a new symmetry.
3. **Post-hoc, a cross-check that also holds.** The doublet-twist orientation matches
   `OverStrandWeight.ptr_markov` once the Ř convention is aligned. The corpus's "u = e₁,
   T³ = +½" reading is the weight of `U_q(gl₂)` **inside colour**. Read through this probe, that
   T³ is a colour Cartan, not weak isospin. The flavour ↔ gl₂-weight identification in
   `OverStrandWeight` is still "stated, not derived".

## Implications

- **The electroweak reading of the D residual is not supported.** It is the stabiliser of a
  colour-breaking (rank-2) twist, i.e. the familiar SU(3) → SU(2) × U(1) pattern of a vector in
  the fundamental. It brings no charge normalisation and no Weinberg angle.
- The open hypercharge problem (`conj:sm-hypercharge-invariant`, `qou-kl39`) is untouched: the
  U(1) found here cannot label words, so it cannot be the missing word-level `Y`.
- The question for the owner is unchanged from T1: is colour read through D (rank-2, breaking) or
  through the level-3 trace (invariant)? This probe adds that D's breaking costs a free basis
  choice that no `H_n` observable sees.

## Verification

- `python3 -u qcd_d_residual_symmetry_probe.py` → `SUMMARY 27/28`, exit 1. The exit is 1 by design
  when any check fails; the single FAIL is the pre-registered R3 prediction.
- `scripts/precision-gates.sh --changed` was run. Its RED lines are repo-wide ratchets (q0-anchor
  flip/refill, never-raises-dps, reference-literal, witness-value copy, q0-value drift), and none
  names a file in this directory. The modified audit witnesses in the worktree predate this work
  and are not staged.
