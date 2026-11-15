# Neutron–proton splitting: error budget under convention D

Date: 2026-11-15. Repo `litlfred/qou` at main `232fae9bd`. Diagnostic only: CODATA is used here as a comparison point, never as a target and never in a proof.

Object: Δm = α·|Φ(udd) − Φ(uud)|, with Φ(K) = Σᵢ log|V̂ᵢ(K)|, V̂ᵢ = z·M₁₀ + M₁₁, M = ∏_{j>i} T(cᵢⱼ, dᵢⱼ), T(c,d) = [[c·h+d, c],[c, d]], h = q − q⁻¹ (`HeckeRational.traced_volume`, `computations/hecke/hecke_engine.py:80`).
Crossings: uu = σ (d = 0), dd = σ⁻¹ = σ − h (d = −h), ud = ½(σ + σ⁻¹) (d = −h/2).
Inputs: q₀ = 1.10997858275138… (50-digit, proton pin), α = m_e·8G = 3.744459660 (exact; the Lean pin 3.7449 is +0.012 %).
z_C = √q/(q+1) = 0.499320, z_D = q³/(q²+1) = 0.612688.
CODATA 1.29333378 MeV needs |ΔΦ| = 0.345399.

## 1. Exact closed forms (sympy, q and z symbolic)

The tower here is 3 strands, so 2 generators:
- **i = 0** (outer, H₃ level, 2 crossings)
- **i = 1** (inner, H₂ level, 1 crossing)

| factor | proton uud = [1,1,0] | neutron udd = [1,0,0] |
|---|---|---|
| V̂₀ (all pairs) | 1 + z·h/2 | (1 + h²/4) = (q²+1)²/(4q²), **independent of z** |
| V̂₁ | z − h/2 = tr ½(σ+σ⁻¹) | z − h = tr σ⁻¹ |

So ΔΦ = log[(1+h²/4)/(1+zh/2)] + log[(z−h)/(z−h/2)].

Under D everything collapses to polynomials in q:
- z_D − h = 1/(q(q²+1)) and z_D − h/2 = (q⁴+1)/(2q(q²+1)), so the i = 1 ratio is **2/(q⁴+1)**.
- e^{ΔΦ_D} = (q²+1)³ / (q²(q⁴+1)(q⁴+q²+2)).
- The adjacent-only reading under D gives e^{ΔΦ} = **q⁻⁴** exactly.

## 2. Level-by-level budget (all-pairs reading, the published one)

| | i = 0 (H₃) | i = 1 (H₂) | total ΔΦ | Δm (MeV) | vs CODATA |
|---|---|---|---|---|---|
| C | −0.04001 | −0.30758 | −0.34759 | 1.30153 | +0.63 % |
| D | −0.05121 | −0.23030 | −0.28151 | 1.05410 | −18.50 % |
| C→D change in \|ΔΦ\| | +0.01120 | **−0.07728** | −0.06608 | | |

**Where the error comes from.** All of the C→D loss, and more, sits in the inner H₂-level factor tr σ⁻¹ / tr ½(σ+σ⁻¹) = (z−h)/(z−h/2). The H₃ factor moves the other way by 0.0112. The H₂ factor is so sensitive because z − h is small at z_C (0.290). Raising z to z_D lifts it to 0.404, which pulls the ratio toward 1. Linear sensitivity at D: dΔΦ/dz = 0.411.

**Which z would match.** The construction agrees with CODATA only near z* = 0.50204, essentially z_C. So the old +0.63 % was a property of z ≈ ½. This is a diagnosis, not a proposal to set z.

## 3. What is ruled out as the source (all measured)

- **α input.** The pin is off by 0.012 %, and the exact m_e·8G changes Δm by 0.01 %. Closing the gap would need α × 1.2269, i.e. a different binding scale, not a rounding fix.
- **Input rounding.** The z = 4993/10000 vs exact z_C difference is 0.005 points (agrees with the Q_β thread).
- **Higher-order tail.** (r−1)/ℏ_q² = 23.1 under D, so the 18.5 % is not a perturbative ℏ_q² correction. (Under C it was about −0.65.)
- **Ordering.** Over all 3×3 quark orderings, only the canonical pair [1,1,0]/[1,0,0] is near. The others give −69.6 %, −30.2 % and +20.8 % under D. Picking one by its residual would be selection against the target anyway.
- **c_k ladder factor.** The missing factor here is 1.2269. The c_k ladder's needed 1.2002 differs by 2.2 %. Nothing links them, and I am not claiming a shared factor.

## 4. Pair rule and trace weight

| variant | C | D |
|---|---|---|
| all pairs, V̂ = z·M₁₀ + M₁₁ (published) | +0.63 % | **−18.50 %** |
| adjacent crossing only | +57.06 % | +20.83 % (= 4 ln q · α) |
| last crossing only | −10.95 % | −33.32 % |
| Wedderburn V̂_full (sym + std + alt, w = dim_q²/([2]²+2)) | +53.64 % | +16.36 % |
| Wedderburn with the alt channel dropped and renormalised (ad hoc) | −19.4 % | −27.64 % |

- **The −2.9 % reading, now reproduced.** It comes from `computations/pn_splitting_proof_provenance_probe.py`, in its "suffix-inclusive" mode. That mode takes the crossings along the word positions, t = [cross(s0,s1), cross(s1,s2)], and gives generator i the suffix t[i:].
  - It differs from all-pairs in **one factor only**: the neutron's outer H₃ factor.
  - That factor becomes (σ−h/2)(σ−h): tr = 1 − z·h/2 + h²/2. All-pairs has (σ−h/2)², with tr = 1 + h²/4.
  - Result: i = 0 term −0.10518, i = 1 term −0.23030, total −0.33548. That is **−2.87 % under D**, but +12.7 % under C.
  - So this reading recovers about 0.054 of the 0.077 lost at H₂, and it does so at H₃.
  - **Why it is suspect (my judgement, not a finding).** In udd = [1,0,0], strand 0 is a u quark. The half twist crosses strand 0 with strands 1 and 2, both d, so both of its crossings are ud. The suffix reading assigns strand 0's second crossing the dd type. That is the type of the pair (1,2), not of a pair strand 0 is in. So it labels crossings by word position rather than by the strands that actually cross. The engine's own `traced_volume` labels by strand pair (`ordering[gen_idx]` vs `ordering[j]`). Choosing the suffix reading because it lands at −2.9 % would be selection against the target.
- **The engine's own docstring** (`hecke_engine.py` around line 116) says *"ALL OBSERVABLES from H_3(q) MUST use V̂_i^full (not per-channel)"*. The published splitting uses per-channel `traced_volume`, not `V_full`. That is a corpus-internal inconsistency, independent of C vs D.

## 5. Context from sibling threads (not recomputed here)

- The Q_β route under D gives m_n − m_p = 0.9557 MeV (−26.11 %), on branch `claude/qbeta-convention-d-values-2026-11-15`. Same sign as this route.
- The gluon thread found that every 3-strand γγ nucleon gives Δ = 0. Under the one-rule γγ reading, the splitting cannot come from the 3-strand colour trace at all. That is consistent with the whole signal here sitting in the flavour crossings (σ vs σ⁻¹ vs ½(σ+σ⁻¹)).

## 6. Ways to tame it, derived and not fitted

**R1. Derive the mixed ud crossing.**
- What it means: the ud crossing is the hand-set average ½(σ+σ⁻¹) with d = −h/2. It controls the dominant H₂ term, 2/(q⁴+1) under D. A derivation from the weak/isospin vertex (left projector) would fix it.
- What it costs: research in the chirality/isospin epic.
- What it risks: it also moves every Level-1 Q-value in `level1-qvalues.py`.
- What it commits to: nothing until a derivation exists.

**R2. Use the corpus-declared V̂_full (Wedderburn).**
- What it means: this is derived from the corpus (the engine's own rule). It gives +16.4 % under D: the sign flips, but the miss is smaller.
- What it costs: re-running the producer and changing the block and the Lean pins.
- What it risks: the Wedderburn weights are dim_q²-based, and under D the (1³) block is killed. So the weights themselves may need re-deriving first (see R3).

**R3. Make the trace weights D-consistent.**
- What it means: write the z_D Markov trace as Σ_λ w_λ(z_D)·χ_λ with w_(1³) = 0, and build V̂ from that instead of the dim_q² weights.
- What it costs: a small exact computation. My crude proxy (drop alt and renormalise) gives −27.6 %, but it is not a derivation, so don't quote it.

**R4. Keep −18.5 % as the honest D value (the no-op).**
- What it means: record that the C-era agreement was a z ≈ ½ effect (z* = 0.502), and that the error is structural in the H₂ flavour crossing.
- This is what happens if nothing is chosen.

**Recommendation (my judgement):** R3 first, because it is cheap and decides whether R2 is even well-posed under D. Then R1 as the real fix. R4 stays the default meanwhile.

## Reproduce

Run with `python3 <file>` (needs mpmath and sympy), from `computations/probes/np_splitting/ (and project files) `:
- `np_error_budget_closed_forms.py`
- `np_error_budget_levels.py`
- `np_error_budget_pair_rules.py`

Output is in `probe_output.txt`.

## 7. Route R3 result: trace weights are not a free knob (2026-11-15)

Pre-registered in `np_trace_weights_probe.py`. Output is in `probe_output_routes.txt`.

**Structural fact (exact, sympy).** Every factor in `traced_volume` multiplies by the same generator σ. So each V̂ᵢ lives in the 2-dimensional commutative subalgebra ⟨σ⟩ ≅ H₂, not in a genuine H₃ word. On that subalgebra the Markov trace is exactly a two-channel sum:

V̂ᵢ = w₊·λ_sym + w₋·λ_alt, with w₊ = (z+q⁻¹)/(q+q⁻¹) and w₋ = (q−z)/(q+q⁻¹).

The identity was checked symbolically for 1 and 2 factors. It follows that every variant (traced_volume, the engine's V̂_full, and the drop-alt variant) is one function of the single number w₋, or equivalently of an effective z.

| variant | effective z | w₋ | result |
|---|---|---|---|
| traced_volume at z_D (Markov, convention D) | 0.612688 | q²/(q²+1)² = 0.24730 | −18.50 % |
| engine V̂_full applied with z_D | 0.444527 | — | +16.4 % |
| drop-alt Wedderburn (ad hoc) | 0.711284 | — | −27.6 % |
| what the CODATA comparison would need | 0.502037 | 0.30232 | 0 % |

V̂_full's effective z is (q⁴z + q³ + 2q²z − q + z)/(q⁴ + 4q² + 1). That is not z_D, so V̂_full is not the z_D Markov trace: using it would break the D ruling. The Markov property makes the D weights on H₂ the restriction of the D trace on H₃, so they are fixed.

**Verdict (scope-limited).** Under the D ruling the trace weights are fixed and give −18.5 %. Re-weighting is not an in-model lever. The only remaining levers are:
- the crossing elements, especially the mixed u–d one;
- replacing the ⟨σ⟩ collapse with a genuine H₃ word (σ₁, σ₂ distinct) traced by the D Markov trace on H₃. This is a new candidate route, R5. It is likely related to the gluon thread's "3-strand γγ nucleon gives Δ = 0".

## 8. Route R1, first pass: candidate u–d crossings (pre-registered, none selected)

Pre-registered in `np_ud_crossing_candidates_probe.py`. Results under D:

| rule | u–d element | D result |
|---|---|---|
| A, average (current) | ½(σ+σ⁻¹) | −18.50 % |
| B, distinct flavours don't braid | 1 | +20.83 % |
| C, oriented, earlier u over d | σ (and σ⁻¹ for d over u) | +20.83 % |
| D′, oriented the other way | σ⁻¹ (and σ for d over u) | −74.48 % |

- B and C both give ΔΦ = log tr_D(σ⁻¹)/tr_D(σ) = **−4 ln q exactly**. This is a convention-D-native closed form. It is the same value as the adjacent reading.
- None of these is derived from the weak vertex, so none is adopted. A real derivation of the u–d element is needed from the chirality/isospin work.

## 9. Weak-vertex input (from the weak-vertex thread, 2026-11-15)

**The corpus's u–d crossing is the weak vertex up to a scalar.**
- `WeakVertexLeftProjector.lean` (`weakVertex_eq_split`, sorry-free on main) gives W = σ·P_R + σ⁻¹·P_L = q⁻¹(2σ − h)/[2].
- This is now in Lean: PR #7948, `QuarkState/WeakVertexMidpoint.lean` (sorry-free). `weakVertex_eq_midpoint_of_one_lt` gives W = (2/(q²+1))·½(σ+σ⁻¹) for 1 < |q|. For |q| ≤ 1 the scalar is 2q²/(q²+1) instead. q₀ > 1, so the cancellation below is unaffected.

**The scalar cancels exactly in ΔΦ.**
- In the all-pairs reading, the proton has 2 u–d crossings: one at i = 0 and one at i = 1.
- The neutron also has 2: both at i = 0.
- Each occurrence shifts its generator's log-trace by ln(2/(q²+1)), so ΔΦ shifts by (2 − 2)·ln(2/(q²+1)) = 0.
- The per-level split does move: i = 0 by +ln s and i = 1 by −ln s, where s = 2/(q²+1). The total does not.

**Consequence.** Identifying the u–d crossing with W leaves the −18.5 % unchanged. It upgrades the hand-set ½(σ+σ⁻¹) from "arbitrary midpoint" to "σ on one chirality eigenline and σ⁻¹ on the other", conditional on the open conjecture D-H3 (bean qou-hlx7).
- The oriented alternatives (+20.8 % and −74.5 %) are chirality choices, not flavour choices (`ChiralityPairBit.lean`, PR #7941).
- So R1 does not tame the error. The error is not in the crossing labels.

**What is left.** R5: rebuild Φ from a genuine H₃ word, with σ₁ ≠ σ₂ and the D Markov trace on H₃, instead of collapsing everything onto ⟨σ⟩.

## 10. Route R5: a genuine H₃ word under the D trace (2026-11-15)

Pre-registered in `np_h3_genuine_word_probe.py` (exact sympy in H₃(q) on the 6-element T_w basis, Ocneanu trace). Output is in `probe_output_h3.txt`.

Check: the D trace kills the (1³) channel, w_(111)(z_D) = 0 ✓.

| word (strand-tracked flavour labels) | Φ(uud) at D | Φ(udd) at D | ratio under D | Δm at D | vs CODATA |
|---|---|---|---|---|---|
| half twist g₁g₂g₁ | −0.61489 | −0.72007 | (2q⁴+q²+1)/(q²(q⁴+q²+2)) | 0.3939 MeV | −69.6 % (C: −76.4 %) |
| full twist (g₁g₂g₁)² | +0.14226 | −0.06642 | **q⁻²** | 0.7814 MeV | −39.6 % (C: −53.1 %) |
| published transfer product | −0.6149 | −0.8964 | see §1 | 1.0541 MeV | −18.5 % |

### Main finding: the published Φ(udd) is not the Markov trace of the half twist

- **Proton.** The genuine half-twist trace equals the transfer product exactly. Φ(uud) = −0.61489, the same as #7927.
- **Neutron.** They differ.

Write Δ = (g₁+a)(g₂+b)(g₁+c). Strand tracking forces a = pair (0,1), b = pair (0,2), c = pair (1,2). The Markov property peels the middle letter:

- genuine trace: tr Δ = (z+b) · tr₂((g+a)(g+c))
- transfer product: tr₂((g+a)(g+b)) · (z+c)

These coincide when b and c have the same type. That holds for uud (both u–d), and fails for udd (b = u–d, c = d–d).

So the transfer construction effectively puts all of strand i's crossings on the letter σᵢ: it traces the product P = ∏ᵢ ∏_{j>i}(σᵢ + dᵢⱼ), not the braid. For udd, P is the strand-tracked word σ₁²σ₂, not the half twist.

**Where this sits in the corpus.** `thm:markov-trace-factorization` (`mass-theory/markov-trace-factorization.md`) is a correct identity about P. Its proof assumes that "the crossings at generator σᵢ reduce to aᵢσᵢ + bᵢ", and that identification is exactly the step that fails for udd. At nucleon level the same counterexample is ³H with ordering [p,n,n]: crossing types pn, pn, nn.

**Corpus check, partial.** I grepped docs/audits and computations for traced_volume together with "half twist". I found no prior record of this. That is not the full six-path check, so it is not yet a durable "open" claim.

### Consequences for the error budget

- The C-era +0.63 % agreement came from a neutron object that is not a braid trace.
- The strand-consistent braid traces under D give −69.6 % (half twist) and −39.6 % (full twist, with the clean ratio q⁻²).
- None of these is close, and none is selected.
- The −18.5 % is therefore a property of the product P, not of a braid invariant.
- Anything built on `traced_volume` products for words with mixed pair types (Level-1 Q-values, `markov_trace(ordering)`, the binding consumers) may carry the same identification gap. Measuring that blast radius is the natural next step.

## §11 Is the traced product a braid image? (option 2, 2026-11-15 18:30Z)
Pre-registered probe: `np_product_is_braid_image_probe.py`; output: `probe_output_braid_image.txt`. Exact, over Q(q). Search space: all positive words in g1, g2 of length ≤ 6, every flavour placement.
- **Neutron (udd).** P = ((q²+1)/(2q))² · g₂⁻¹ exactly. The two u–d crossings sit on the same generator, and ½(σ+σ⁻¹) = ([2]/2)·J with J² = 1, so they collapse to a scalar. P equals the strand-tracked image of exactly one word shape, g₁g₁g₂ (or g₂g₁g₁) with the u on the first strand. In that braid one u–d pair crosses twice and the other u–d pair never crosses.
- **Proton (uud).** P is not the exact image of any word in the search space. Its trace equals the half twist g₁g₂g₁ (and g₂g₁g₂).
- Consequence (scope a): the −18.5 % compares the proton's half-twist trace with the neutron's g₁²g₂ braid, which are two different braid shapes. On one shape for both: half twist −69.6 %, full twist −39.6 % (§9).

## §12 Coloured strands: two-colour Yokonuma–Hecke Y₂,₃ (option 1, 2026-11-15)
Pre-registered probe: `np_yokonuma_coloured_probe.py`; output: `probe_output_yokonuma.txt`. Exact over Q(q, z, x), Juyumaya trace solved from its defining linear system, z = z_D.
- **Placement is forced.** tr(π_c W) ≠ 0 needs the colour constant on each cycle of W's permutation. That gives half twist p = (u,d,u), n = (d,u,d), and full twist p = (u,u,d), n = (u,d,d). No ordering choice is left.
- **x is forced.** Of the three d = 2 E-system values, x = ±1 kills one colour sector (tr π = 0). Only x = 0 keeps both u and d alive.
- **Pure Yokonuma (Y0, every crossing g):** n − p = 0 exactly, for both the half and the full twist. At x = 0 the colour flip t ↦ −t preserves the trace, so u ↔ d is a symmetry of the algebra and the trace together.
- **With the old chirality rule imported (Y1, d–d crossings use g⁻¹):** half twist −45.84 %, full twist +35.19 %. Those numbers come entirely from the imported rule.
- Lean (generic ring): `YokonumaColourSplit.lean`. On the mixed-colour sector the crossing is an involution, ((1−e)g)² = 1−e; on the same-colour sector it is Hecke. This matches the grading involution J (J² = 1) of OneSidedWeakVertex.
- Reading (scope a): coloured strands fix the word and the placement and derive the u–d crossing, but they give n − p = 0. A nonzero splitting needs an explicit u/d asymmetry (a colour-dependent crossing, or x ≠ 0 outside the E-system). That asymmetry is an input, not something derived. Same conclusion as the γγ nucleon (Δ = 0).
- Asked by the weak-vertex thread (PR #7960: tr_D pulled back along ι is the transposed trace z_T, which differs from z_D): does "d = ι(u)" follow from the colour placement? **No.** In Y₂,ₙ the u ↔ d map is the colour flip t ↦ −t. It fixes every g_i (e_i is flip-invariant) and preserves the trace at x = 0. ι is not part of the colouring, so setting d = ι(u) would be a choice, and choosing it would be a fit. Not used.

## §13 Level-2 weight spaces: the quantum trace's own u/d asymmetry (bean qou-q1a4, step 3)
Pre-registered probe: `np_level2_weight_space_probe.py`; output: `probe_output_level2.txt`. Exact over Q(q). Jimbo R-matrix on (C²)^{⊗3}. **Corrected 2026-11-15:** only K = diag(q, 1/q) gives a Markov trace. The partial quantum trace tr₂((1⊗K)Ř) is z_D·1 for K = diag(q, 1/q), and is not a scalar for K = diag(1/q, q): it gives diag(q/(q²+1), (q⁴+q²−1)/(q³+q)). An earlier version of this section said both orientations give z = z_D. That came from a weaker test (full traces of 1 and Ř only), which both pass. The partial-trace test was raised by the weak-vertex thread and re-checked here with sympy. So convention D forces K = q on the highest-weight vector e₁ of Ř, which is T³ = +½.
- Restrict the D trace to the weight spaces: p = two u and one d, n = one u and two d. Then **n/p = q^{∓2} exactly**, for the half twist, the full twist and the γγ candidate V³ alike. It does not depend on the word. With K forced, the sign is set only by the labelling: u on e₁ gives n/p = q^{−2}.
- |ΔΦ| = 2 ln q, giving Δm = 0.7814 MeV against CODATA 1.2933 (−39.58 %). The magnitude depends on no labelling, no word and no ordering.
- **Mechanism:** on a weight space K^{⊗3} is a scalar, q^{+1} for p and q^{−1} for n. The plain trace of the braid action is the same on the two weight spaces. So the whole difference is the quantum-dimension weight of the isospin doublet. Normalising each sector by its own trace removes it, giving n/p = 1. Restricting the trace (raw) versus normalising per sector is a choice; both were pre-registered and are reported.
- **Reading:** the weight q^{±1} is the first place along the chain where u and d differ by something derived rather than imported. K's orientation is forced by D. What it still does not fix is which quark sits on e₁ (u = T³ = +½ would follow if a positive crossing is tied to K = q; that link is open, bean qou-q1a4 step 4). The full-twist value in §9 (ratio q^{−2}) is this same number.

## §14 Scale, higher level, and which quark is T³ = +½ (bean qou-q1a4)
- **Scale α.** α = m_e·8G is defined as the nuclear *binding* scale (prop:binding-scale-catalan). The n–p proof applies it to a log-trace difference with one sentence, "the scale … governing nuclear binding also dictates the quark-level confinement splitting". No corpus artifact derives that step. Matching CODATA would need |ΔΦ| = 0.3454, which is 1.655 × 2 ln q. For comparison: feeding the weight ratio q^{±1} or q^{±2} into the canonical nucleon-mass route m_p = 2(m_μF − 6m_e) gives 103.9 MeV or 219.2 MeV. So the weight cannot enter at the level of the nucleon mass, and the 0.7814 MeV figure is conditional on the asserted α. No alternative scale is tried here, because choosing one would be a fit.
- **Higher level.** Pre-registered probe `np_level3_weight_space_probe.py`: Jimbo R on (C³)^{⊗3}, K = q^{2ρ}. Adjacent (u,d), on (e₁,e₂) or on (e₂,e₃), gives n/p = q^{−2} for the half twist, the full twist and σ₁σ₂, the same as level 2. The reason holds at any level: weight spaces of permuted weights are isomorphic Hecke modules (permutation modules M^μ), so the plain traces agree and only K^{⊗3} = q^{2⟨μ,ρ⟩} differs. Weights one simple root apart differ by q². Non-adjacent placement (e₁,e₃) gives q^{−4} (+20.8 %), but that placement is a choice. In u,d,s ordering u and d are adjacent. **Higher levels do not change the result.**
- **Which quark is on e₁.** The corpus already fixes the knot side: u = T(2,3), d = its mirror, T₃ = ½ sgn κ (knot-notation-convention, Lean `MesonOperatorSelectionT3.T3`). The missing link is from a strand's knot to a weight vector. Tested the proposed link "positive crossing ↔ K = q": tr₂((1⊗K)Ř) and tr₂((1⊗K)Ř⁻¹) are both scalars for K = diag(q, 1/q) (q²·1 and q⁻²·1), and neither is a scalar for diag(1/q, q). **So the crossing sign does not select the vector.** The ribbon twist is a scalar on the irreducible V, so framing and writhe cannot separate e₁ from e₂ either. Only K does. "u on e₁" therefore reduces to identifying the writhe isospin T₃ with the Cartan weight in K = q^{2T³}. That identification is natural but not derived. If adopted it gives the neutron heavier, which is a check and is not used to select it.

## §15 Deriving the scale; Lean for the orientation (bean qou-q1a4)
Pre-registered probe `np_scale_candidates_probe.py`. Each candidate scale was taken from a corpus mass formula and fixed before running. None is selected by its residual.

| route | Δm (MeV) | vs CODATA |
|---|---|---|
| S0 asserted α·2 ln q, α = m_e·8G | 0.7814 | −39.58 % |
| S1 canonical facade, F_Bor scaled by q^{2} | 219.15 | +16845 % |
| S1 canonical facade, F_Bor scaled by q^{−2} | 177.87 | +13653 % |
| S2 linearised facade, 2m_μF·2 ln q | 197.08 | +15138 % |
| S3 unified formula m_e·8G·ρ/ℏ_q², ρ ratio q² | 88.51 | +6744 % |

**Reading (scope a).** Every route that puts the weight-space ratio into a corpus nucleon-mass formula gives a splitting of 89–219 MeV. So the restricted trace is not how those formulas see flavour: their canonical trace is the unrestricted one, which is the same for p and n. The only route at the MeV scale is S0, and S0's scale is asserted, not derived. **No corpus formula derives a MeV-scale multiplier for this ratio.** The −39.58 % stands as a conditional figure, and the scale is the open object.

**Lean** (`QOU/BraidsAndKnots/MarkovOrientationForced.lean`, generic `[Field R]`, lean-direct `-DautoImplicit=false` exit 0, no sorry, standard axioms only):
- `positive_crossing_markov_iff`, `negative_crossing_markov_iff`: tr₂((1⊗K)Ř) and tr₂((1⊗K)Ř⁻¹) are scalars iff a = b q², the same condition for both crossing signs (`same_condition_both_signs`).
- `markov_normalised`: with ab = 1 this gives a² = q².
- `adjacent_weight_ratio`: the K-weights of adjacent basis vectors differ by q² at every level. The equality of the plain traces on permuted weight spaces (the permutation-module half) is **not** formalised.

## §16 Sign from the over-strand result (draft PR #7971, weak-vertex thread)
PR #7971 (`QOU/QuarkState/OverStrandWeight.lean`, sorry-free, still a draft) proves this. Under D, a crossing is a pure transposition iff its over strand carries the K = q vector. That holds for σ and σ⁻¹ and for both R conventions. Add two corpus conventions: in σᵢ the lower strand passes over, and def:down-quark says u passes over d. Together these give **u = e₁ = T³ = +½**. That is derived from the corpus conventions; the orientation was not chosen by the result.

Consequence here: p = uud carries K^{⊗3} = q, n = udd carries q⁻¹. So **n/p = q⁻², Φ_n − Φ_p = −2 ln q**. Under the proof's reading (a more negative Φ is more confinement), the **neutron is heavier, which is the correct sign**. Sign: derived, conditional on #7971 landing. Magnitude: unchanged, 0.7814 MeV (−39.58 %), still conditional on the asserted scale α (§15).

## §17 Level-2 weight-space result fully in Lean; what the scale multiplies
**Lean** (`QOU/BraidsAndKnots/NucleonWeightSpaceTraces.lean`, generic `[Field R]`, lean-direct `-DautoImplicit=false` exit 0, no sorry, standard axioms). On the (2,1) and (1,2) weight spaces of (C²)^{⊗3}, σ₁ and σ₂ act by explicit 3×3 matrices. An explicit P with det P = −(q²+1)/q⁴ intertwines them (`intertwine₁`, `intertwine₂`, `intertwine_word`). Hence `trace_word_eq`: every braid word in σ₁, σ₂ has the same plain trace on the proton-type and the neutron-type weight space, for q ≠ 0 and q² + 1 ≠ 0. A side fact: σ₁ on one space is σ₂ on the other. Together with `MarkovOrientationForced.lean`, the level-2 statement "the restricted D trace gives n/p = q^{∓2} for every word" is now proved, apart from the bookkeeping that K^{⊗3} is the scalar q^{±1} on each space.

**What the scale multiplies (structural, scope a).** In the producer, Φ = Σᵢ log|V̂ᵢ|, the log of an algebraic quantum volume ∏V̂ᵢ (`quark_volume_provenance_probe.py`). The scale is α = m_e·|Vol_q(B₃)| = m_e·|∏V̂ᵢ^{B₃}| (prop:binding-scale-catalan), built from the same kind of object. So the asserted Δm = α·ΔΦ multiplies one quantum volume (the Borromean's) by a difference of logs of another (the quark ordering's). The corpus's own scale block is linear in the volume (m_e × Vol_q). Read with that form, a quark-ordering change would contribute m_e·ΔVol_q, not m_e·Vol_q(B₃)·Δlog Vol_q. No corpus artifact states which form applies to the splitting, so this is recorded as the reason the scale is underived. It is not used to pick a new formula.

## §18 Derivation attempt with the corpus's derived hadronic scale E₀ (owner: "both, derive first")
**Corpus search.** The corpus has a *derived* hadronic scale, E₀ = m_e/(q(q−1)) ≈ 4.186 MeV, from CAL-1 and CAL-2 only (notation-collisions, mass-formula-validation, interaction-sector-taxonomy: strong sector). Its tower-summed form is E₀^full = E₀/(1−ℏ_q²) ≈ 4.227 MeV. The corpus calls it "the MeV-per-dimensionless-trace-unit conversion for hadronic predictions", and it is used **linearly** on trace differences: Q_β = |Δnet|·E₀ and Q_β = |ε(Δ)|·E₀. No corpus block derives α = m_e·8G for this use, and none supports the log form α·ΔΦ. One related block, gluon-model-comparison, *calibrates* E₀ = Q/Δ ≈ 4.155 MeV. That is a fit and is not used.

**Pre-registered probe** `np_hadronic_scale_e0_probe.py` (output `probe_output_e0.txt`). Element: the ruled γγ nucleon V³, V = σ₁σ₂⁻¹; V⁶ also passes reading 3 and is reported too. Trace: the D quantum trace with K = diag(q, 1/q), normalised to tr(1) = 1, restricted to the p and n weights with u = e₁.

| candidate | Δm (MeV) | vs CODATA |
|---|---|---|
| D1, corpus linear form, E₀^full·\|t_n − t_p\|, V³ | 0.3254 | −74.84 % |
| D1, same, V⁶ | 0.3235 | −74.98 % |
| D1′, order-zero E₀, V³ | 0.3222 | −75.08 % |
| D2, log form kept, E₀^full·2 ln q | 0.8822 | −31.79 % |

t_n/t_p = q⁻² exactly for both words, as proved in Lean (§17).

**Reading (scope a).** The only derived scale in the corpus, used in the corpus's own linear form on the ruled element, gives −74.8 %. That is robust: V³ and V⁶ agree to 0.6 %. D2 is closer, but the log form has no corpus support, so ranking it higher would be selecting by residual. The sign under the linear form is not settled either. t_p is negative here, so whether the neutron is heavier depends on whether the mass reads t or |t|. **The derivation does not close.** Following the owner's card, the next step is a proposed conjecture wording for the n–p block, put up for review and not applied.
