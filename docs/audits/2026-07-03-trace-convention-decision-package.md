# Trace-convention decision package — production D (TL/Jones) vs canonical C (Wenzl z-trace)

**Status:** decision package for the owner — no production wiring changed.
**Input facts:** PR #3261 proved (Lean, sorry-free) that convention **D**
(the Borromean single-pipeline / `BorromeanMarkovTrace` closed form, =
SU(2)/Temperley–Lieb Jones decomposition) and convention **C** (the
canonical M1–M3 Jones–Markov trace = Wenzl z-trace, exactly) **differ as
rational functions**, gap `1.9554e-4` at q₀. Registry:
[`2026-06-09-binding-trace-convention-split.md`](2026-06-09-binding-trace-convention-split.md)
(addendum). Impact numbers below:
[`probe_trace_convention_production_impact.py`](../../computations/probes/probe_trace_convention_production_impact.py)
(witness, 2/2 assertions).

## 1. Who uses which convention (consumer map)

| Convention | Consumers | Role |
|---|---|---|
| **D** (TL/Jones) | `m_p_substrate_identity_50dps.trM_borromean` → `F_Bor` → **`canonical_mass.py`** (m_p/m_n facade); `borromean_binding_recompute.py` (the single pipeline); Lean `BorromeanMarkovTrace`; the q₀ **proton-anchor solver** (`constants.py::q_at` inverts the same F_Bor identity) | **absolute nucleon mass + the μ–p concordance** |
| **C** (= Wenzl z-trace) | `markov_trace_canonical.tr_M_element` (the stated "canonical trace"); `binding_canonical.py` (trace-canonical baseline); `y_lambda_wenzl_bridge` / step-5 Wedderburn infra; Lean `BorromeanTraceConventionSplit.trC_borromean` + `BorromeanCanonicalTraceDerivation` | binding baselines, per-λ machinery |

## 2. What switching the mass pipeline D → C would do (probe, 50 dps)

| Scenario | Result |
|---|---|
| **Muon anchor (canonical 3-CAL), q₀ fixed** | m_p prediction shifts **−0.185 MeV = −197 ppm** — destroys the CODATA match |
| **Proton anchor, q₀ re-pinned on C** | q₀ shifts −1.04e-5; the m_μ prediction then misses CODATA by **170,875 ppb (~0.017 %)** — **813.7×** the same-anchor D baseline (the probe's D proton re-pin gives ≈210 ppb, reproducing the dashboard's 209.8 ppb μ–p tension — both baselines computed internally, same anchor convention) |
| **Q_β** (at the re-pinned q₀) | 0.7836458 → 0.7836649 MeV (+24 ppm — negligible vs its 0.17 % scale) |
| **Binding tower** | per-nucleon τ ratio shift 1.96e-4 (A=16 compound ~3.1e-3) — noise vs the 2.3× 9b gap |

**Bottom line: convention D is load-bearing for the muon–proton
concordance.** No anchoring choice makes C compatible with both m_p and
m_μ at current precision.

## 3. Is D principled or a hidden degree of freedom? (both readings)

**Principled reading (supported by the corpus, a priori):** the mass
functor lives on **Rep(SU_q(2)) ≃ Temperley–Lieb** — and in TL the
3-row partition (1³) has no image (`V^⊗3` in TL carries only (3) and
(2,1)). The paper-side proof block
[`borromean-markov-trace-closed-form-proof.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form-proof.md)
states this explicitly ("through Temperley–Lieb, which annihilates the
3-row partition") — the y_(1³) = 0 choice was documented *before* the
D≠C split was discovered, so it is **not** a post-hoc fit to the
concordance. On this reading D is the categorically correct trace for
the SU_q(2) mass functor, and C is the correct trace for the *full*
H_n(q) algebra (Wedderburn/binding machinery). Two objects, two jobs.

**Critical-distance reading (recorded per the license):** the
convention is nonetheless a **1-bit discrete choice** that the μ–p
concordance is sharply sensitive to (197 ppm). Had TL not matched, the
full-H₃ trace was available as the alternative. The a-priori TL
documentation defuses most of this, but a referee will ask why the
*binding* side is allowed to use C/Wenzl machinery while the *mass*
side uses D — the honest answer must be the categorical one (TL is the
image category of the fibre functor), stated in the paper, not just in
a proof remark.

## 4. Recommendation (no owner reversal needed to adopt #1–#3)

1. **Keep D in the mass pipeline** (no wiring change) — it is a-priori
   documented and load-bearing.
2. **Scope the word "canonical"**: C is canonical *for H_n(q) as an
   algebra*; D is canonical *for the Rep(SU_q(2))/TL mass functor*.
   The `trM_borromean` docstring mislabel ("canonical Wenzl Markov
   trace" — false on both counts) is fixed in this PR; the registry
   rule (state your convention below 0.1 %) covers the rest.
3. **Paper-side follow-up** (owner judgment on wording): promote the
   TL-restriction sentence in the closed-form proof block to an
   explicit convention statement wherever `tr_M(β_Bor)` feeds mass
   (one sentence + a `uses[]` link).
4. 🟡 **Owner decision only if desired:** whether to rename registry
   labels (e.g. "C = algebra trace", "D = functor trace") corpus-wide —
   cosmetic, can wait.

Cross-refs: PR #3261 (proofs), PR #3200 (PROBE 4), `1ppq-qbeta.md`
(convention discipline precedent), AGENTS.md §q₀ anchor convention.

## Addendum (2026-07-03) — μ–p dressing vs the exact bar-even Q_β kernel: REFUTED-as-is

Follow-up probe
[`probe_mup_dressing_vs_even_kernel.py`](../../computations/probes/probe_mup_dressing_vs_even_kernel.py)
(witness, ratio table complete) transported the ORD-17 **exact** bar-even
kernel `E(ũ)` (8 witness-verbatim rungs, bean `08ds`) to the mass channel:
**no natural object** (full kernel, single rung, tail; either documented
ladder variable) reproduces the μ–p dressing within 1 % — the mass-channel
dressing is **not** the Q_β even kernel evaluated at the same substrate
argument. Scope (a). Sharpeners for the kernel search: (i) every kernel
object is **negative**, matching only the **muon-leg attribution**
(δ_μ ≈ −2.10e-7), never the proton-leg (+2.42e-7); (ii) the nearest
candidates are the k = 5 rung (0.654×) and the k ≥ 5 tail (0.687×) of
δ_μ — right order and sign, wrong magnitude by ~1.5×. Whatever the
mass-channel dressing is, it lives at the u⁵-order scale of a *different*
(mass-channel) kernel.

## Addendum 2 (2026-07-03) — attribution test: the dressing most economically lives on the F_Bor (Borromean) leg

[`probe_mup_dressing_attribution.py`](../../computations/probes/probe_mup_dressing_attribution.py)
(witness) exploits a decoupling: if the dressing multiplies the **muon**
identity (H_μ), the proton equation contains no δ and q₀ is pinned by the
pure Hecke factor `F_Bor(q₀^F) = (m_p+12m_e)/(2m_μ)` — a **third,
independent pin**. Result:

- **The F-pin lands OUTSIDE the muon–proton bracket**: q₀^F is −90.0 ppb
  from the muon pin and −78.5 ppb from the proton pin (same side). Because
  F_Bor is 6.8× less q-sensitive than the muon identity
  (dlnF/dlnq = −2.68 vs dlnA/dlnq = −18.2), H_μ forces
  **δ* = −1.64e-6** — ~7× LARGER than the minimal tension.
- **The F_Bor-leg attribution (H_F) is the economical one**:
  ε* = **+2.41e-7** with q₀ staying at the muon pin. Occam prefers the
  dressing on the **composite Borromean factor** — which is also where the
  known exact-vs-low-order gap lives (the 6.7% `tr_M_atomic` object) and
  physically sensible (the 3-strand composite truncates; the elementary
  4₁ lepton anchor is clean). This *reverses* Addendum 1's tentative
  sign-based lean toward the muon leg (consistently: the Q_β kernel was
  refuted as the mass kernel anyway, so its sign carried no authority).
- **Kashaev-subleading naturality: refuted-as-is** — the color N that
  would make the volume-conjecture subleading term `(3/2)·log N·(2π/N)`
  equal the dressing is N ≈ 5.03e7, matching no corpus scale (1/ℏ_q²,
  1/ũ, 1/ũ², 1/ℏ_q⁴ miss by 4.5e3–4.9e5×).

**Net target for the kernel program, sharpened twice:** derive a
multiplicative correction to **F_Bor** (the Borromean composite factor)
of **+2.41e-7 at the muon-pinned q₀** — positive sign, u⁵-order scale,
not the Q_β even kernel, not a Kashaev subleading log.

## Addendum 3 (2026-07-03) — provenance resolution: ε* IS the fitted Habiro tower; the tower is inside the production q₀ solver

Following a Copilot review question about which pin `Q_50_DIGIT_STR`
carries, direct inspection of
[`qou_substrate/constants.py`](../../tools/qou-substrate/python/qou_substrate/constants.py)
resolves the apparent contradiction — and surfaces a discipline item:

- **`q_at()` (the "proton pin") solves the proton identity MULTIPLIED by
  the fitted Habiro tower** `(1+46u⁴)(1+4u⁵)(1−29u⁶)` — the exact
  integer tower the [2026-05-28 floor
  audit](2026-05-28-mu-p-tension-substrate-floor.md) rejected as a fit
  ("46 is 46.02, no categorical identity; do not re-introduce such fits
  to production"). Because the tower was fitted to close the μ–p gap,
  the towered proton solve lands on the **muon value to sub-ppb** —
  which is why `Q_50_DIGIT_STR` fingerprints as muon-pinned (m_μ at it:
  1.36 ppb) while its docstring says m_p-pinned. **Both descriptions
  are true: proton data + fitted tower ≡ muon value.**
- **The attribution probe's ε* equals the tower's value**:
  ε*/(tower−1) = **0.9944** at the same q₀ (probe witness,
  `eps_star_over_tower_minus_1`). The "economical F_Bor-leg dressing"
  measured independently by the attribution geometry IS what the fit
  supplies, dominated by the **46u⁴ rung** (2.4208e-7 of the 2.4224e-7
  total). The 0.56% residual is the fit's own drift vs current CODATA
  inputs.
- **Kernel-program target, final sharpening:** derive the coefficient
  **c₄ ≈ 46 at u⁴** (legacy-u normalization; ũ-equivalent to be
  restated) of a mass-channel dressing on F_Bor, categorically. That
  single rung carries 99.9% of the μ–p tension.
- 🟡 **Owner attention (not adjudicated here):** the floor-audit-rejected
  tower sits in production `constants.py::q_at()` / `_solve_q_proton_f64`
  — i.e. the package-layer q₀ pin *inherits the fit*. If the 2026-05-28
  re-pin was authorized with the tower inside, the AGENTS §q₀-anchor
  narrative ("precision substitution") should say so explicitly; if not,
  the pin should be the raw proton identity (which lands 11.5 ppb away).
  Flagged for ruling; nothing changed in production by this PR.
