import QOU.BraidKnot.JonesNuclearQuotient

/-!
# QOU.BraidKnot.JHopfQOneProvenance — the provenance of `J_Hopf(q=1) = −2`

The `c_3` near-match in the `Q_β` truncation ladder is recorded (AGENTS.md
§"Critical framing — Q_β `c_k`") as `c_3 = -2 = J_Hopf(q=1)`. This file
**rigorizes the provenance of that `−2`** — it does *not* close a derivation gap
(the `c_3` value is proved measurement-limited; see
`SRigidity.no_anchor_invariant_realizes_swing`), it only pins where the number
`−2` comes from knot-theoretically, so the constant is not free-floating.

## The convention gap (stated honestly)

The framework's **reduced** Markov trace of the Hopf-link closure `σ₁²`
(`JonesNuclearQuotient.jonesHopfLink q = h·z + 1`, `h = q − q⁻¹`,
`z = 1/(√q+1/√q)`) evaluates at `q = 1` to **`1`, not `−2`** — proved below as
`jonesHopfLink_one`. So `−2` is *not* the raw reduced trace.

The `−2` is the **standard (V-normalized) Jones polynomial** of the Hopf link at
`t = 1`, via the classical evaluation
`V_L(1) = (−2)^{c−1}` (Jones 1985; `c` = number of link components). Both facts
are captured:

1. `loopValue q = −(√q + 1/√q)` is the **Jones loop factor** `δ` — the base of
   the `(δ)^{n−1}` prefactor in Jones's normalization
   `V_{β̂}(t) = (−(√t+1/√t))^{n−1}(√t)^e · \barπ_t(β)`. At `q = 1`,
   `δ = −2` (`loopValue_one`). The `−2` lives entirely in this loop factor; the
   trace part `\barπ_1(σ₁²) = 1` contributes nothing.

2. `classicalJonesAtOne c = δ(1)^{c−1} = (−2)^{c−1}` is the classical
   value at `t = 1` for a `c`-component link (`classicalJonesAtOne_eq`).
   The 2-component **Hopf** link gives `(−2)^{2−1} = −2` (`jonesHopf_atOne`);
   the 1-component unknot gives `(−2)^0 = 1` (`unknot_atOne`); a 1-component
   knot (trefoil) also gives `1`.

3. `jonesHopfStd q = −√q − (√q)^5` is the tabulated standard normalized Jones
   polynomial of the (negative) Hopf link `V(t) = −t^{1/2} − t^{5/2}` (Jones
   1987, standard link tables). Independently, `jonesHopfStd 1 = −2`
   (`jonesHopfStd_one`), cross-checking the `(−2)^{c−1}` route.

## Numerical witness cross-reference

The corpus probe `computations/qbeta/qbeta_c3_jhopf_q0_vs_q1_comparison.py`
(witness `computations/qbeta/qbeta-c3-jhopf-q0-vs-q1-comparison.witness.json`)
records the same `−2` from a **third** convention `J_Hopf(q) = −(q² + q⁻²)`,
also `= −2` at `q = 1`, and confirms it is `q_0`-independent ("Rule A:
`c_3 = J_Hopf(q=1) = −2`, passes the Taylor-coefficient stability test"; the
`q_0`-evaluation `J_Hopf(q_0) ≈ −2.044` is the near-match swing). That three
distinct Jones normalizations — the loop factor `δ^{c−1}`, the tabulated
`V(t)`, and `−(q²+q⁻²)` — all agree at `q = 1` is the **convention-robustness**
of the `−2` at the classical point: it is the loop/component-count invariant
`V_L(1) = (−2)^{c−1}`, not an artifact of one normalization.

Base ring (§7c): archimedean (`Real.sqrt`, Jones-variable evaluation), so `ℝ`.

Ref: [jones1987] https://www.jstor.org/stable/1971403
Ref: [leitner2026] quantum-observable-universe/mass-theory/jet-filtered-knot-factor.md
Ref: [leitner2026] computations/qbeta/qbeta_c3_jhopf_q0_vs_q1_comparison.py (numerical witness)
-/

namespace QOU.BraidKnot.JHopfQOneProvenance

open QOU.BraidKnot.JonesNuclearQuotient

/-- **The Jones loop factor** `δ(q) = −(√q + 1/√q)` — the value of a single
    unknotted loop, and the base of the `(δ)^{n−1}` prefactor in Jones's
    normalization of the Markov trace. -/
noncomputable def loopValue (q : ℝ) : ℝ := -(Real.sqrt q + 1 / Real.sqrt q)

/-- **`δ(1) = −2`.** The entire `J_Hopf(q=1) = −2` originates here: the loop
    factor at the classical point `t = 1`. -/
theorem loopValue_one : loopValue 1 = -2 := by
  unfold loopValue; rw [Real.sqrt_one]; norm_num

/-- **The framework's reduced Markov trace of the Hopf closure is `1` at `q=1`,
    NOT `−2`.** Makes the convention gap explicit: `h(1) = 0` kills the
    trace-dependent term, leaving the reduced-trace normalization `1`. The `−2`
    is therefore *not* the raw reduced trace but the loop-factor / V-normalized
    value. -/
theorem jonesHopfLink_one : jonesHopfLink 1 = 1 := by
  -- `markovZ`/`heckeH` are the sqrt-free convention-D forms (q³/(q²+1), q−1/q),
  -- so there is no `Real.sqrt` left to rewrite; `heckeH 1 = 0` kills the term.
  unfold jonesHopfLink heckeH markovZ; norm_num

/-- **The classical Jones value at `t = 1` for a `c`-component link**, as the
    `(c−1)`-th power of the loop factor `δ(1)`. This is the QOU-side statement of
    the classical identity `V_L(1) = (−2)^{c−1}`. -/
noncomputable def classicalJonesAtOne (c : ℕ) : ℝ := (loopValue 1) ^ (c - 1)

/-- `classicalJonesAtOne c = (−2)^{c−1}` — the classical `V_L(1) = (−2)^{c−1}`. -/
theorem classicalJonesAtOne_eq (c : ℕ) : classicalJonesAtOne c = (-2 : ℝ) ^ (c - 1) := by
  unfold classicalJonesAtOne; rw [loopValue_one]

/-- **`J_Hopf(q=1) = −2`.** The Hopf link has `c = 2` components, so
    `classicalJonesAtOne 2 = (−2)^{2−1} = −2`. This is the provenance of the
    `c_3` near-match constant. -/
theorem jonesHopf_atOne : classicalJonesAtOne 2 = -2 := by
  rw [classicalJonesAtOne_eq]; norm_num

/-- The unknot (`c = 1`) gives `(−2)^0 = 1` — consistent with the framework's
    normalization `V_unknot(1) = 1` in the V-convention. -/
theorem unknot_atOne : classicalJonesAtOne 1 = 1 := by
  rw [classicalJonesAtOne_eq]; norm_num

/-- **Tabulated standard normalized Jones polynomial of the (negative) Hopf
    link** `V(t) = −t^{1/2} − t^{5/2}` (Jones 1987; standard link tables), in
    `√q` form (`(√q)^5 = q^{5/2}`). Independent of the loop-factor route. -/
noncomputable def jonesHopfStd (q : ℝ) : ℝ := -(Real.sqrt q) - (Real.sqrt q) ^ 5

/-- **`V_Hopf(1) = −2`** from the tabulated closed form — cross-checks the
    `(−2)^{c−1}` route (`jonesHopf_atOne`). -/
theorem jonesHopfStd_one : jonesHopfStd 1 = -2 := by
  unfold jonesHopfStd; rw [Real.sqrt_one]; norm_num

/-- **The two routes agree at `t = 1`.** The tabulated closed form and the
    `(−2)^{c−1}` loop-factor value both give `−2` for the Hopf link. -/
theorem jonesHopf_provenance : jonesHopfStd 1 = classicalJonesAtOne 2 := by
  rw [jonesHopfStd_one, jonesHopf_atOne]

/-- **3-component Borromean / link evaluation at `q = 1` (`qou-itdn`):**
For `c = 3` components, `classicalJonesAtOne 3 = (-2)² = 4`. -/
theorem borromean_atOne : classicalJonesAtOne 3 = 4 := by
  rw [classicalJonesAtOne_eq]
  norm_num

/-- **Component-step recurrence at `q = 1` (`qou-itdn`):**
For every `c ≥ 1`, adding one link component multiplies `classicalJonesAtOne` by `-2`. -/
theorem classicalJonesAtOne_step (c : ℕ) (hc : 1 ≤ c) :
    classicalJonesAtOne (c + 1) = -2 * classicalJonesAtOne c := by
  rw [classicalJonesAtOne_eq, classicalJonesAtOne_eq]
  have hsub : c + 1 - 1 = (c - 1) + 1 := by omega
  rw [hsub, pow_succ']

/-- **Selectivity of the `q = 1` classical Jones evaluation by component count (`qou-itdn`):**
1-component knots (`1`), 2-component Hopf links (`-2`), and 3-component Borromean links (`4`)
take pairwise distinct values at `q = 1`. -/
theorem classicalJonesAtOne_selectivity :
    classicalJonesAtOne 1 = 1 ∧
    classicalJonesAtOne 2 = -2 ∧
    classicalJonesAtOne 3 = 4 ∧
    classicalJonesAtOne 2 ≠ classicalJonesAtOne 1 ∧
    classicalJonesAtOne 3 ≠ classicalJonesAtOne 1 ∧
    classicalJonesAtOne 3 ≠ classicalJonesAtOne 2 := by
  rw [unknot_atOne, jonesHopf_atOne, borromean_atOne]
  refine ⟨rfl, rfl, rfl, by norm_num, by norm_num, by norm_num⟩

end QOU.BraidKnot.JHopfQOneProvenance
