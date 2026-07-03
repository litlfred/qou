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
| **Proton anchor, q₀ re-pinned on C** | q₀ shifts −1.04e-5; the m_μ prediction then misses CODATA by **170,875 ppb (~0.017 %)** — ≈ **800× worse** than the current 209.8 ppb μ–p tension |
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
