# Pre-registration: Q_β routes R2 / R5 / R3 (bean qou-99qc), 2026-11-20

Branch `claude/qbeta-derive-t3-flip-chirality-t35-2026-11-20`. Written before the numerical runs
of `r2_r5_isospin_round_trip_probe.py` and `r3_t35_crossing_budget_probe.py`.

**Disclosure (not blind).** A symbolic sympy exploration (`ℚ(q)` only, no q₀, no MeV) of the
R2 construction was run before this file was written. It fixed the closed form
`y₃^C = (q²+1)²/(q⁴+4q²+1)`. No numerical value at q₀ and no comparison with CODATA had been
computed when this file was committed. The construction below was fixed before that
exploration, from the task statement ("T³ is moved by E/F of U_q(gl₂)").

## R2 / R5 — the T³ flip on the Schur–Weyl dual side

* Model: `V = K²` (u = T³ +½, d = T³ −½), Jimbo `Ř` on `V⊗V`, coproduct
  `Δ(E) = E⊗K + 1⊗E`, `Δ(F) = F⊗1 + K⁻¹⊗F` (the one of the two standard choices that commutes
  with this `Ř`; checked, not chosen by any number). `σ₁ = Ř⊗1`, `σ₂ = 1⊗Ř` on `V^{⊗3}`.
* n weight space `W₋` (one u), p weight space `W₊` (two u). The n→p flip is `Δ²(E) : W₋ → W₊`
  (T⁺, the charged-current isospin raising operator); back is `Δ²(F)`.
* Functional (fixed now, the only one evaluated as "the" label-C value):
  `ε_C(X) = tr_{W₋}(F E X) / tr_{W₋}(F E)`, X ∈ H₃ acting on `W₋`.
  The normalisation `ε_C(1) = 1` is the same normalisation convention D uses; it is recorded
  as a remaining choice, not derived.
* Reported regardless of value, as comparison rows (not candidates for selection):
  (a) weight-restricted, no flip: `tr_{W₋}(X)/3`; (b) isospin-½ projection of ε_C;
  (c) full quantum trace (= Jones / z_D, to be checked); (d) ε_C evaluated from p (`tr_{W₊}(E F X)`).
* Q_β = (h[2]/2)·y₃·E₀ with both E₀ forms (order zero `m_e/(q(q−1))`, tower `E₀/(1−ℏ_q²)`),
  proton q₀ (`qou_substrate.constants.q_at()`), mpmath 70 dps. CODATA 0.78233341 MeV is a
  comparison only. No variant is promoted because of its residual.

## R3 — T(3,5) claims of `beta-decay-skein-properties`

Checks, each reported pass/fail as found:
1. `(σ₁σ₂)⁵` has 10 letters; its closure is a knot (permutation a 3-cycle).
2. `σ₁³` left-divides `(σ₁σ₂)⁵` in B₃⁺: enumerate all positive length-7 words P with
   `σ₁³P = (σ₁σ₂)⁵` (equality tested in the reduced Burau representation, faithful on B₃);
   also for σ₂³, and for a trefoil block at other positions. Report the count (uniqueness of
   the "3 + 7" split).
3. "R2 moves": a positive word has no σσ⁻¹ pair; report the free-reduction count of P.
4. Count quadratic-relation applications in the H₃ rewrite of `(σ₁σ₂)⁵` under two rewrite
   orders (leftmost-first, rightmost-first); report whether the count is order-independent.
5. `W(q) = tr_{z_D}((σ₁σ₂)⁵)` exactly; report whether it lies in ℤ[q^{±1/2}] (claimed).
6. Whether the H₃ normal form of `(σ₁σ₂)⁵` contains the basis element... (none has length > 3;
   report the normal form).
7. Algebra-level reduction claim: is there a scalar c with `B_n·(σ₁σ₂)⁵ = c·B_p` in H₃
   (block-wise test)? Report.
8. The Q formula of the block uses the excised convention-C pair-Skein scale: report it as
   not computable under convention D unless a derivation of every factor exists.
