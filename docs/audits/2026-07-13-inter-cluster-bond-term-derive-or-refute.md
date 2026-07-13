# The inter-cluster bond term — derive-or-refute (pre-registered q-rotational test + structural characterization)

**Date:** 2026-07-13 · **Task:** R5-a · **Branch:** `claude/mass-binding-errors-9zqpal`
**Probe:** [`computations/deltalambda/inter_cluster_bond_term_probe.py`](../../computations/deltalambda/inter_cluster_bond_term_probe.py)
· **Witness:** [`inter-cluster-bond-term.witness.json`](../../computations/deltalambda/inter-cluster-bond-term.witness.json)
(allPassed: true, 10/10 assertions; witness-fed — no recompute, no census scan, nothing tuned; all `j` pre-registered)
**Discipline:** formalize-first (`compute-author.md` §3.3) — structure of the
deficit sought before any fit; scope-(a) phrasing throughout.

## 1. The object

Three independent 2026-07-13 results converged on one missing object:

1. **Alpha-cluster additivity is a zero-fit lower bound** (⁸Be +0.16%); the
   deficit `B_AME − B_add` *is* the inter-cluster bond term, with
   **non-constant** implied per-bond volumes (2.9 → 12.8, guarded)
   ([a5plus constraints](2026-07-13-atom-knot-rule-a5plus-constraints.md)).
2. **The n = 4 tower term is not one link volume** (census gap at ⁴He)
   ([Vol₄ test](2026-07-13-he4-vol4-prediction-test.md)).
3. **The θ_λ carrier is an intensive mean** — extensivity lives in the
   volume tower ([carrier saturation](2026-07-13-carrier-saturation-crossover-mechanism.md)).

This audit characterizes the deficit data structurally and executes the one
structurally motivated zero-freedom hypothesis: the **q-rotational bond
channel** — the corpus's own derived deuteron object
(`binding_qhamiltonian_rotational_scale.py`: `E = μ₀·ℏ_q·J_q²(j)`,
`μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.6295` MeV derived, `ℏ_q = 1−q⁻¹`,
`J_q²(j) = [j]_q[j+1]_q`; deuteron channel `j = 3` gives 2.0196 MeV = B_D −9%).

## 2. Pre-registered tests (zero freedom; deficits from the committed witness)

Three variants, all with every factor derived and every `j` fixed in advance
(cluster ground-state spins ENSDF/NNDC: α 0⁺, d 1⁺, t ½⁺, n ½⁺; witness
chain-bond counting, k−1 bonds):

| iso | bonds (chain) | deficit (MeV) | **H1** spin-j | r₁ | **H2** j=3/bond | r₂ | **H3** strand-j | r₃ |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| ⁶Li | α·d | +1.474 | 0.325 | 0.22 | 2.020 | 1.37 | 2.020 | 1.37 |
| ⁷Li | α·t | +2.468 | 0.121 | 0.05 | 2.020 | 0.82 | 4.360 | 1.77 |
| ⁸Be | α·α | −0.092 | 0.000 | ✓(0) | 2.020 | **✗** | 7.865 | ✗ |
| ⁹Be | α·α + α·n | +1.573 | 0.121 | 0.08 | 4.039 | 2.57 | 8.477 | 5.39 |
| ¹¹B | α·α + α·t | +11.132 | 0.121 | 0.01 | 4.039 | 0.36 | 12.225 | 1.10 |
| ¹²C | 2×α·α | +7.275 | **0.000** | ✗ | 4.039 | 0.56 | 15.729 | 2.16 |
| ¹⁴N | 2×α·α + α·d | +17.547 | 0.325 | 0.02 | 6.059 | 0.35 | 17.749 | 1.01 |
| ¹⁶O | 3×α·α | +14.437 | **0.000** | ✗ | 6.059 | 0.42 | 23.594 | 1.63 |
| ¹⁹F | 3×α·α + α·t | +26.137 | 0.121 | 0.00 | 8.078 | 0.31 | 27.954 | 1.07 |

(rᵢ = pred/deficit. ⁹Be alternative reading, two α·n bonds: H1 = 0.242,
H3 = 1.225 — same verdicts.)

- **H1 (cluster-spin j — the task's primary form): decisively NEGATIVE.**
  Undershoots the one-bond deficits ×4.5 (⁶Li) to ×20.4 (⁷Li) and predicts
  **exactly 0** for every α·α bond — the pure-α composites carrying the
  *largest* deficits (¹²C +7.27, ¹⁶O +14.44 MeV). Failure shape: with
  physical spins j ≤ 1 the channel is **intensively bounded** at
  μ₀·ℏ_q·J_q²(1) = 0.325 MeV/bond — the same intensive-vs-extensive
  obstruction the carrier-saturation result proved for the θ_λ mean. No
  constant offset or scale factor rescues it (required factors 4.5 → ∞).
- **H2 (fixed deuteron-channel quantum, j = 3 per bond — "the deuteron is
  the bond's model"): NEGATIVE as a universal quantum.** Right *order* at
  the one-bond composites (⁶Li +37%, ⁷Li −18%) — the only variant in the
  right magnitude window there — but ⁸Be is violated by 2.11 MeV (predicts
  2.02 vs the measured −0.09) and pred/deficit spans ×8.3 across isotopes.
- **H3 (strand-count j = 3·A_light/2, the corpus j = n/2 rule applied to
  the light cluster): NEGATIVE, informative failure shape.** pred/deficit
  rises strictly with light-cluster size: α·n 0.78 → α·d 1.37 → α·t 1.77 →
  α·α(k≥3) 3.26. The q-exponential Casimir `[j]_q[j+1]_q` grows too fast —
  the data grow ~linearly in A_light (below).
- **CAL-3 m_π-scale bond quanta** (continuum-EM family: α_der·m_π = 1.020,
  m_π·ℏ_q² = 1.370, (3/5)α·m_π/A^{1/3}): **no member matches at multiplier
  1** (every one deviates > 30% on at least one one-bond deficit).
  `m_π·ℏ_q²` vs the ⁶Li deficit alone is +7.6% — **single-point,
  quarantined as a numerology hazard** (deficit(⁷Li)/deficit(⁶Li) = 1.674
  also sits 0.5% from 5/3; equally quarantined — no structural argument,
  huge expression entropy).

## 3. Structural characterization — the failure shape IS the finding

From the committed deficits alone (descriptive, guarded; no model):

1. **Not a function of bond spin.** The two j = ½ bond types differ ×3.14
   (α·t 2.468 vs α·n 0.786/bond), and j = 0 (α·α) carries both the
   smallest (−0.09) and among the largest (2.4/pair) values. Any
   `deficit = f(j_bond)` is excluded by the data, independent of f.
2. **~Linear (extensive) in light-cluster nucleon count** for the one-bond
   family: deficit/A_light = 0.786 (α·n), 0.737 (α·d), 0.823 (α·t) —
   mean **0.78 MeV per light-cluster nucleon**, max dev 5.8%. GUARDED
   (3 points), but it is the quantity the q-rotor cannot produce: J_q² is
   q-exponential in j, the data are ~linear in size. Not the light
   cluster's own binding either (deficit/B_D = 0.66 vs deficit/B_t = 0.29).
3. **The α·α pair term is many-body-activated.** Under complete-graph
   C(k,2) recounting the pure-α composites are **pairwise-flat**:
   ¹²C 2.425 vs ¹⁶O 2.406 MeV/pair — agreement to **0.8%** (¹⁹F, with a t
   attached, 2.614) — while the *same* α·α pair at k = 2 (⁸Be) gives
   ≈ 0 (−0.092). And the flat ≈2.41 MeV value cannot be a universal pair
   quantum: at ⁹Be it would force a *negative* α·n term. So the pair term
   exists, is remarkably uniform inside the pure-α family at k ≥ 3, and is
   switched off at k = 2 — a genuinely many-body/contextual object,
   exactly the "compositional object is already many-body" pattern (the
   probe measures the size of the missing higher term, it does not exclude
   the pair ingredient). Guarded near-misses for 2.41 MeV: B_D = 2.2246
   (−8%), the deuteron rotor 2.0196 (−16%) — **not claimed**.
4. **Contact-nucleon count** (task item (a)) is not extractable from the
   committed data — the composite reading has disjoint clusters; the size
   characterization (item 2) is the operative version.

## 4. Verdict

**NEGATIVE (scope-(a))** for the pre-registered q-rotational inter-cluster
bond term `deficit(X·Y) = Σ_bonds μ₀·ℏ_q·J_q²(j)` — under all three
zero-freedom j-rules — and for a universal CAL-3 m_π-scale bond quantum.
Scope-(a) explicitly: this constrains these forms **as sole mechanisms**;
the rotor channel, the volume tower, and the pair graph remain admissible
ingredients of a many-body closure (permanence principle — the additivity
lower bound itself, and its cluster pieces, are untouched).

What is *established* (data-level, guarded where marked): the deficit is
(i) spin-blind, (ii) ~extensive in the light-cluster size at 0.78
MeV/nucleon (3 points, guarded), (iii) carried by a pairwise-flat-at-k≥3,
zero-at-k=2 α·α term (0.8% flatness ¹²C vs ¹⁶O — the sharpest new datum)
plus mixed-bond terms that break any universal pair quantum at ⁹Be.

## 5. Next steps (named, not run)

1. **Derive the k ≥ 3 activation.** The α·α pair term's on/off behaviour
   (0 at ⁸Be, 2.41 flat at ¹²C/¹⁶O) is the crispest structural target: in
   tower language, a 3-cluster (α·α·α) term that *projects onto* pairs —
   cross terms of a multiplicative/trace object, not a pairwise sum.
   Formalize-first: find the invariant that forces a vanishing 2-cluster
   term with a non-vanishing 3-cluster one (the Brunnian/Borromean pattern
   — pairwise-unlinked, triple-linked — is the corpus's own precedent and
   the obvious candidate mechanism; C5 of the a5plus constraints notes the
   4-component Brunnian analogue is non-hyperbolic, so the 3-cluster level
   is where volume can live).
2. **Explain 0.78 MeV/nucleon.** The one-bond deficit's linearity in
   A_light says the bond term counts *strands*, not spins — but linearly,
   not q-exponentially: a first-jet / leading-order object (cf. the jet
   filtration of `conj:binding-manybody-eq-jet-filtration`), not a Casimir.
3. **R5-full SDP knot-ID (#604)** remains the principled route to the
   composite interface (gated on its A ≤ 3 anchor non-confirmation).
4. The quarantined near-misses (2.41 ≈ B_D − 8%; m_π·ℏ_q² ≈ ⁶Li deficit
   +7.6%) may only be revived with a structural derivation, per the
   formalize-first rule — recorded here so they are not independently
   "re-discovered" as fits.

## Provenance

Inputs: committed [`alpha-cluster-volume-additivity.witness.json`](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(deficits consistency-checked against vendored AME2020 to 1e-9 MeV — no
recompute of the additivity test), `m_e` (CODATA 2022, CAL-1), `q₀`
(`q_parameter.Q_50_DIGIT_STR`), `m_π` (CAL-3, validation), cluster spins
(ENSDF/NNDC, pre-registered), derived scales from
[`binding_qhamiltonian_rotational_scale.py`](../../computations/binding_qhamiltonian_rotational_scale.py)
(μ₀ derived, 0 free params). No fitted constant; no census scan; no
production wiring; no tier change. Companions (same day, this branch):
[a5plus constraints](2026-07-13-atom-knot-rule-a5plus-constraints.md),
[Vol₄ test](2026-07-13-he4-vol4-prediction-test.md),
[carrier saturation](2026-07-13-carrier-saturation-crossover-mechanism.md);
ledger: [`binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md).
EXPLORATORY — audit + witness only.
