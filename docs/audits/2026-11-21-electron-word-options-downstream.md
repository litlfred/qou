# Electron word, option 1 vs option 2: downstream implications (measure only)

Date 2026-11-21. Follows [`2026-11-21-electron-word-gs-interactions.md`](2026-11-21-electron-word-gs-interactions.md)
(PR #8724). Owner question: *"Explore 1 2. What are downstream implications on particle
interaction/gröbner bases and on mass/compute?"*

## Owner ruling (recorded verbatim, 2026-11-21)

> *"I think it is hopf link so take. That as ruling for now, but keep trefoil as backup in case
> need to recisit"*

- **Option 1 is the ruling for now:** `e⁻ = σ₀σ₁σ₀ ∈ H₃(q)`; its closure in `B₃` is the **Hopf link**.
- **Option 2 is the documented backup:** `e⁻ = σ₀³` (the trefoil braid in `B₂ ⊂ B₃`; closure in `B₂`
  is the trefoil, in `B₃` it is trefoil ⊔ unknot).

This document is therefore the backup's dossier: it measures both options side by side, says
which differences are structural and which are labels, and lists the corpus sites that now
conflict with the ruling. **No corpus content, producer or witness was edited.** Nothing is
compared with experiment and no option is ranked by a number.

Conventions: `σᵢ² = hσᵢ + 1`, `h = q − q⁻¹`; photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`
(owner ruling 2026-11-20); Markov trace convention D, `z = q³/(q²+1)`; proton `q₀` from
`q_parameter.Q_MP`. `P = span{1, σ₀, σ₁, σ₀σ₁}` is the span of single-photon terms. `C` is the
corpus conjugation `σᵢ ↦ σᵢ⁻¹`.

## Method

Probe [`computations/probes/electron_word_options_downstream_probe.py`](../../computations/probes/electron_word_options_downstream_probe.py),
run as
`python3 -u computations/probes/electron_word_options_downstream_probe.py 2>&1 | tee /tmp/ewo.log`
(≈ 2 min). All algebra is exact over `ℚ(q)` (sympy), reusing the `H₃(q)` model of the merged
GS-interaction probe (which is cross-checked against `photon_operator_table.reduce_nf` to 1e-55).
mpmath is used only to evaluate exact expressions at `q₀` and inside the LP, which is imported
unchanged from `knot_operator_lp_selection.py` (that producer's solver is mpmath basis
enumeration by design). Checks the probe passes: `σ₀³ = h·1 + (h²+1)·σ₀`; the 2-dimensional
representation (rescaled reduced Burau, `t = q⁻²`) satisfies the Hecke and braid relations; the
free-neutron-decay nucleon normal forms recomputed as `B₃·(typed crossings)` equal the
witness's symbolic coefficients exactly, for both nucleons.

`scripts/precision-gates.sh --changed`: no gate names the probe; the RED gates it reports
(q₀-anchor flip, refill, reference-literal, q₀-value drift) are pre-existing witness stamps on
`main` (e.g. `hadron-knot-table.witness.json`, −0.0769 ppb), not this change.

## 1. Side-by-side table

| | **Option 1 (ruling)** `σ₀σ₁σ₀` | **Option 2 (backup)** `σ₀³` |
|---|---|---|
| Lives in | `H₃ ∖ P`; the one basis word outside the photon span | `H₂ ⊂ P`; `σ₀³ = h·γ((h²+1)/h, 0, 0)` |
| Closure | Hopf link in `B₃` (Jones `−t^{1/2}(t²+1)`) | trefoil in `B₂` (Jones `−t(t³−t²−1)`); trefoil ⊔ unknot in `B₃` |
| **A(i)** `γγ → e⁻` channel | defined: coefficient of `σ₀σ₁σ₀` in `NF(γ(φ)γ(ψ))` = `φ₀₁ψ₀ + φ₁ψ₀₁` | **undefined in the corpus basis.** Needs a new basis; replacing `σ₀` by `σ₀³` (basis `B′`) gives `(σ₀-coeff)/(h²+1)`, a long polynomial **with a term linear in each photon** — so **a single photon already has a nonzero "e⁻" coordinate** `q(φ₀q − φ₀₁(q²−1))/(q⁴−q²+1)`. Replacing `σ₁` by `σ₁³` (`B″`) gives a different channel. The channel depends on a choice of basis. |
| **A(ii)** `e⁻·e⁺`, `e⁺·e⁻` | `= 1` both ways (palindrome) | `= 1` both ways (palindrome) |
| `e⁻ + e⁺` in `P` | no (all six words) | **yes** (only `1`, `σ₀`) |
| `e⁺` NF | all six basis words | `−h(q⁴+1)/q² ·1 + (q⁴−q²+1)/q² ·σ₀` |
| **A(iii)** `NF(γX)` | support `{σ₁, L₊, L₋, σ₀σ₁σ₀}`, not in `P` | all six words, not in `P` |
| `NF(Xγ)` | support `{σ₀, L₊, L₋, σ₀σ₁σ₀}`, not in `P` | support `{1, σ₀, σ₁, L₊}`, **in `P`** |
| photons commuting with `X` | `φ₀ = φ₁, φ₀₁ = 0` (swap-symmetric, no chiral vertex) | `φ₁ = φ₀₁ = 0` (photons inside `H₂`) |
| **A(iv)** β-decay "e⁻ deficit" (sign of e-coefficient in nucleon NF) | defined. neutron `−(q²−1)²(q²+1)²/(4q⁴)` = −0.04418; proton = −0.04321; both negative ("deficit"); `Δe(n−p)` = −0.000976 (matches witness `delta_e`) | **undefined in the corpus basis.** Under `B′`: neutron +0.04611, proton +0.03423, **both positive — no deficit**; `Δe` = +0.01188 (12× larger, opposite sign) |
| `beta-decay-energy-scale.py` Scenario 4 denominator `|Δν|+|Δe|` | 0.1030222 | 0.1164118 under `B′` (+13 %) |
| **A(v)** reading 3, `χ_λ(X)` on blocks with `y_λ>0` (`y₃ = (q⁴+1)/(q²+1)²`, `y₂₁ = q²/(q²+1)²`, `y₁₁₁ = 0`) | `χ₃ = q³`, `χ₂₁ = 0`, `χ₁₁₁ = −q⁻³` → **pass** | `χ₃ = q³`, `χ₂₁ = (q⁶−1)/q³` = 0.6363, `χ₁₁₁ = −q⁻³` → **pass** |
| reading 3 on `C(X)` | `χ₃ = −q⁻³ < 0` → **fail** | `χ₃ = −q⁻³`, `χ₂₁ = −(q⁶−1)/q³` → **fail** |
| **A(vi)** `tr_D(X)` | `q³(q⁴+1)/(q²+1)²` = 0.691166 | `(q⁶+q²−1)/(q(q²+1))` = 0.848527 |
| `tr_D(C X)` | `(q⁴+1)/(q³(q²+1)²)` | `−(q⁶−q⁴−1)/(q³(q²+1))` |
| **A(vii)** `photon_operator_table`: pairs `(bᵢ,bⱼ)` with `σ₀σ₁σ₀`-coefficient of `bᵢ·T·bⱼ` ≠ 0 | 36/36 (the pinned `T_{2,3}` row) | 24/36; under `B′` the "e⁻" coordinate is ≠ 0 in 16/36 |
| **B** LP electron target | optimum 0 (no demand) | optimum 0 (no demand) |
| LP positron target | `σ₀⁻¹σ₁⁻¹σ₀⁻¹`: **19.6154195592** (active `T_{1,0},T_{2,3},T_{3,4},T_{3,5}`) — reproduces the witness | `σ₀⁻³`: **11.9254198590** (same active set and tight rows; `σ₁⁻³` gives the same value). Demand only on `1` (0.42726) vs `{1, L₊, L₋}` |
| H₂O trace excess `tr_D(lone) − z` (`h2o_bond_angle_shift_phi1.py`) | `q⁵(q²−1)/(q²+1)²` = 0.078478 (frac 12.81 %) | `(q²−1)(q⁴+1)/(q(q²+1))` = 0.235839 (frac 38.49 %) |
| Molecular `lone ↦ q^ℓ` weight (trivial character) | `q³` | `q³` (unchanged) |
| Palindrome property used by `h2s_*`, `hybridization_*` | palindrome | palindrome (unchanged) |
| Confinement candidate `X·(typed crossings)` net (`confinement-operator-selection.py`) | proton 1.244124, neutron 1.010927 | proton 1.259502, neutron 1.001689 |
| **C** in `H₂ = span{1,σ₀}` (the block that says "`H₂(q)` (leptons)") | **no** | yes |

All `@q₀` figures above were measured this session by the probe; full exact forms are in its
`JSON-SUMMARY` output.

## 2. Structural vs label

**Structural (a fact about the algebra element, independent of naming):**

1. Option 1's word is outside the photon span `P`; option 2's is a rescaled single photon.
   Everything below that says "option 2 is undefined" follows from this.
2. The `γγ → e⁻` channel and the β-decay "e⁻ deficit" reading are **coordinates** in the
   standard basis. They exist for option 1 because `σ₀σ₁σ₀` is a basis word; for option 2 they
   do not exist until a new basis is chosen, and the probe shows two natural choices (`B′`, `B″`)
   give different channels. Under `B′` a single photon has a nonzero e⁻ coordinate and the
   nucleon "deficit" changes sign. Choosing the basis that makes the reading come out a
   particular way would be selection against the target.
3. `e⁻ + e⁺ ∈ P` under option 2, not under option 1.
4. `tr_D`, `χ₂₁`, the positron's normal form and demand vector, and hence the LP positron optimum
   and the H₂O trace excess, differ.
5. **Not separating:** annihilation to `1` (both palindromes), reading 3 (both `X` pass, both
   `C(X)` fail — the positron fails reading 3 under **either** option because `χ₃(C X) = −q⁻³`),
   trivial-character weight `q³`, crossing energy `3q`, palindromy.

**Label only (the number does not move if the word is kept and only the name changes):** every
consumer that uses `σ₀σ₁σ₀` as *a basis word* and merely calls it "electron" or "trefoil":
`ocneanu_weights.py` / `markov/markov_trace_canonical.py` electron row (value `hz²+z` is the trace
of the basis word), `per_basis_row_invariants_probe.py`, `qbeta_net_as_trace_plus_longest_probe.py`
(index 5 = longest element), `shift_from_nf_basis.py`, `h2-integer-lp.py`, `lp-duality-check.py`,
`basis_knot_tables.py`, the 18 `.lean` files in the blast radius, and the `.md`/`.ts` prose.

**Number-moving, if option 2 were adopted (values in the table above):**

| consumer | quantity | opt 1 → opt 2 | reaches a reader? |
|---|---|---|---|
| `knot_operator_lp_selection.py` + witness | positron LP optimum | 19.6154195592 → 11.9254198590 | `prop:knot-operator-lp-selection` |
| `photon_operator_table.py` + witness | `T_{2,3}` e⁻ pair count (pinned 36) | 36 → 24 (σ₀σ₁σ₀-coeff) or 16 (`B′`) | `rem:knot-operator-basis-table` |
| `free-neutron-decay.py` / `beta-decay-energy-scale.py` | `delta_e`, Scenario 4 `E₀` denominator | −0.000976 → +0.011882 (`B′`); 0.10302 → 0.11641 | β-decay energy-scale audit; `rem:nucleon-nf-observability` sign pattern |
| `confinement-operator-selection.py` | the "e⁻" candidate row | nets in table | candidate table only (not the selected `B₃`) |
| `h2o_bond_angle_shift_phi1.py` + witness | `Δtr`, fractional excess | 0.07848 → 0.23584; 12.8 % → 38.5 % | H₂O angle sign/order-of-magnitude remark |
| `atom_mass_derived.py` | atom NF (attaches `Z` copies of the e⁻ word) | moves; **not recomputed here** (A-dependent `H_A` embedding not reproduced) | derived-atom table |
| `qbeta/qbeta_hoefsmit_tbeta_matrix_build_probe.py` | `χ^λ(electron word)` | `χ₂₁`: 0 → 0.63632 | probe only |

**Not consumers (checked):** `per_observable_100x_status.py` (the L2 dashboard) contains no
`(0,1,0)`, `e⁻` or `electron` (grep of that file only; the scored `Q_β` is the `z_D` trace of the
nucleon element difference, which has no e⁻ term). `m_μ/m_e = Vol(4₁)/ℏ_q²` involves no braid
word. `m_e` is CAL-1 and depends on no word. `gamma_gamma_pair_production_decomposition.py`
mentions the identification only in its docstring. The m_p/m_n `net_coefficient` read by
`derived_masses.py` is a sum over the standard basis and is unchanged by relabelling basis word 6.

**Lean.** No `.lean` theorem in the blast radius becomes false under either option as long as the
definitions are not rewritten: each states a fact about the word `σ₀σ₁σ₀` or about basis
coordinate 5 (e.g. `TrefoilVanishing.unit_nf_no_trefoil`, `MarkovPeelH3.trH3_e_minus`,
`HelicityCommonSource.electron_top`). They are **mislabelled** under the ruling where they call
that word "trefoil", and would be mislabelled again under option 2 where they call it
"electron". If `HelicityCommonSource.electron` were redefined to `σ₀³`, `electron_top` (`v 5 = 1`)
would become **false** (coordinate 5 of `σ₀³` is 0). No new Lean is added here: the one cleanly
discriminating fact (`σ₀³` is a scaled photon) is already `ElectronWordCandidates.cube_eq_smul_photon`.

## 3. Places that conflict with the ruling (label/prose fixes to propose — not made)

Under the ruling, the electron word is `σ₀σ₁σ₀` and its closure is the Hopf link. These sites say
otherwise. They are listed for the owner; none was edited.

1. **`def:electron-knot`** ([`predicted-spectra/electron-knot.md`](../../folio/quantum-observable-universe/predicted-spectra/electron-knot.md)):
   "The electron corresponds to the trefoil knot `T_{2,3}`", `e⁻ = T_{2,3}`, "the electron is the
   trefoil". Proposed: "the electron is `σ₀σ₁σ₀ ∈ H₃(q)`, whose closure is the Hopf link".
   This is the block every other site inherits from.
2. **`c-equals-bar-iff-all-1dim`** (`.md` line 3 "At `H₂(q)` (leptons)"; proof table row
   `H₂ | 1,1 | C = bar | leptons`). Measured: `σ₀σ₁σ₀ ∉ H₂`. Under the ruling the lepton word
   lives in `H₃`, so "leptons" is not the right label for the `H₂` row. Proposed: drop the
   "leptons" label from the `H₂` row, or restate which object is meant. Whether the
   proposition's *content* (C = bar ⇔ all irreps 1-dim) is affected is a separate question: it is
   not, since that is a statement about `H_n`, not about the electron.
3. **`prop:knot-operator-lp-selection`** (`mass-theory/knot-operator-lp-selection.md`) and its
   producer use `T_{2,3} ↦ σ₀³ ∈ B₂`. **Measured: the block does not call `T_{2,3}` the
   electron**, and the producer's electron target is `σ₀σ₁σ₀` with a note that its closure is the
   Hopf link. So this is consistent with the ruling; the only hazard is a reader identifying the
   operator `T_{2,3}` with `e⁻ = T_{2,3}` from `def:electron-knot` (fix 1 removes it).
4. **Prose calling `σ₀σ₁σ₀` the trefoil.** Regex
   `σ₀σ₁σ₀ … (trefoil|3_1|3₁)` within 80 characters (either order), `folio/` + `computations/`,
   excluding the two electron-word probes: **35 lines in 31 files** (approximate: it includes at
   least one negation, `knot-operator-table.py`, which already says "not the trefoil"). Content
   blocks among them: `nucleon-nf-observability.md` ("`σ₀σ₁σ₀` is the trefoil knot"),
   `breit-wheeler-pair-production.md`, `particle-nf-table(.md, -table-data.md)`,
   `knot-operator-basis-table-table1-data.md`, `categorical-proton-properties.md`,
   `nucleon-hecke-element-normal-form.md`, `quark-antiquark-production-reduction.md`,
   `gluon-stabiliser-ledger.md`, `covalent-bond-shared-trefoil.md`,
   `electron-shell-braid-capacity.md`, `qbeta-odd-carrier-hopf-cubic.md`,
   `gluon-model-comparison.md`; Lean docstrings/names in `hecke-normal-form.lean`,
   `NuclearOperatorRegimes.lean` (`trefoilMatrix`, `trefoil_eq_hopfPlus_gen0`),
   `TrefoilVanishing.lean`, `GramSignature.lean`, `DeltaLambdaSignRule.lean`,
   `QBetaZeta4ResidueRefutation.lean`. Command in the probe's companion grep, reproduced:
   `grep -rnE "(σ₀σ₁σ₀|sigma_0\\sigma_1\\sigma_0).{0,80}(trefoil|3_1|3₁)|(trefoil|3_1|3₁).{0,80}(σ₀σ₁σ₀|sigma_0\\sigma_1\\sigma_0)" folio computations`.
5. **Producer labels** (another agent is concurrently on the muon `T_{2,5}` labels in
   `photon_operator_table.py`, `gram-matrix-dual.py` and the photon-chiral probe; not touched
   here): `photon_operator_table.py:129` key `T_{2,3}` / "trefoil (electron)" for `σ₀σ₁σ₀`, and
   the pinned assertion names that repeat it.

## 4. Decision frame (option 2 as backup)

**The decision now:** none is pending on the word itself — the owner has ruled option 1. What the
owner may want to decide is (a) whether to authorise the label/prose fixes of §3, and (b) what
would trigger revisiting option 2.

**Default (no answer):** nothing changes. The word stays `σ₀σ₁σ₀`, no number moves, and the §3
sites keep saying "trefoil" while the ruling says Hopf link.

### Option 1 — the ruling (keep `σ₀σ₁σ₀`)
- **Means:** the electron is the longest basis word `T_{w₀}` of `H₃`, the one element outside the
  photon span; its closure is the Hopf link.
- **Costs:** the label/prose fixes of §3 (about 31 files, mostly one line each; no producer
  re-run, no number moves).
- **Risks:** none numeric. The corpus's "electron is the trefoil" framing and "`H₂` (leptons)"
  label become wrong until fixed.
- **Commits to:** an electron identified by algebraic role (basis word, γγ channel, β-decay
  coordinate), not by knot type; leptons live in `H₃`, not `H₂`.

### Option 2 — the backup (switch to `σ₀³`)
- **Means:** the electron is the trefoil braid in `B₂`, `h` times a single photon.
- **Costs:** redefining the γγ channel and the β-decay reading (both need a new basis, and the
  basis is a free choice: `B′` and `B″` disagree); re-running the five number-moving producers
  above; relabelling ~87 blast-radius files; `HelicityCommonSource.electron_top` false if the def
  is changed.
- **Risks:** the e⁻ coordinate becomes nonzero for a single photon (no pair production needed);
  the nucleon "deficit" sign flips under `B′`; positron LP 19.615 → 11.925; H₂O excess
  12.8 % → 38.5 %. Picking a basis because it restores a desired sign would be fitting.
- **Commits to:** a lepton sector in `H₂`; a new, owner-chosen definition of the pair channel.

**Revisit conditions** (observations or results that would make option 2 worth reopening):
1. A derivation that requires the electron closure to be a **knot** (one component), e.g. a
   complex-volume or Bloch-group argument that needs a hyperbolic or torus *knot* on the
   electron — option 1's closure is a 2-component link and cannot supply it (parity theorem,
   `ElectronWordCandidates.numCycles_permOf_of_odd`).
2. A **basis-independent** definition of the pair-production channel (e.g. a projector or a trace
   functional rather than a standard-basis coordinate) under which `σ₀³` is not
   indistinguishable from a photon.
3. A result that forces leptons into `H₂` structurally (e.g. `C = bar` being required of the
   electron itself, which under the ruling it cannot be read off from `H₂`).
4. A generic-`q` proof that **no** two-photon product equals a multiple of `σ₀σ₁σ₀` (the PR #8724
   measurement covers eight values of `q` only), if pair production is meant literally as a
   product.

**Recommendation (judgement, not a finding):** keep the ruling and authorise §3 fix 1
(`def:electron-knot`) and fix 2 (`H₂` "leptons" label) first, because every "electron is the
trefoil" sentence elsewhere inherits from fix 1, and the remaining ~29 one-line relabels can be
done as one mechanical tranche after that.

## 5. What is not established

- `atom_mass_derived.py` under option 2: classified number-moving, not recomputed.
- The option-2 channel and β-decay readings exist only after a basis choice; the `B′` values are
  one such choice, reported to show the size of the effect, not proposed.
- The "not a consumer" result for the L2 dashboard is a grep of `per_observable_100x_status.py`
  only, not of every module it imports.
