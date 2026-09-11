# γγ word selection — step 3: `SDPSelected` at `H₃`, the selection table, and the diproton sign

**Bean:** `qou-ales` (owner ruling 2026-09-08), step 3 of its closing plan.
**Branch:** `claude/ales-step3-h3-sdp-selector-2026-09-11`, stacked on PR #7184
(steps 1+2, [`2026-09-08-gamma-gamma-word-selection-step1.md`](2026-09-08-gamma-gamma-word-selection-step1.md)).
**Scope:** instantiate the step-1 predicate `SDPSelected` on the nucleon algebra
`H₃(q)`, run the selection over the γγ-produced candidates at the proton `q₀`,
compare to the template words, and compute the sign of the pp binding functional
with the selected bond. **The bean stays `in-progress`** (rule 13a): what is
selected depends on which reading of "PSD" is the confinement SDP's, and that is
stated below as the open point, not decided here.

Owner ruling, verbatim: *"All selection of great words should be done through
gamma gamma production and the semi-definite product solutions at q_0. Shouldn't
use census."*

Nothing below reads AME2020 or a CODATA binding energy. `m_e` (CAL-1) enters only
as the positive MeV scale `E₀`, which cannot move a sign.

## 0. What the corpus already held (corpus-grep, reused not re-derived)

| where | what | used as |
|---|---|---|
| `QOU/Mass/GammaGammaWordSelection.lean` (#7184) | `GammaGammaWord`, `SDPSelected` (`Matrix.PosSemidef` per block + cost-minimal), `altChar_eq_one`, `not_gammaGamma_single`, `h2_psdFeasible_iff_even` | the predicate being instantiated |
| `content/…/mass-theory/confinement-sdp.md` (`prop:confinement-sdp`), `QOU/Interactions/ConfinementSDP.lean` | primal `min ⟨T,Φ⟩` over `Φ ⪰ 0` with (1) per-block Frobenius positivity `⟨π_λ,Φ⟩ ≥ 0`, (2) adjacent-pair PSD, (3) trace normalisation; the Lean carries the primal–dual data as a typeclass | the source of reading (iii) below |
| `computations/sdp_gamma_gamma_to_qqbar.py` | `H₂` PSD-parity demo; "the SDP picks out the canonical `T_w` whose Wedderburn projections are PSD"; crossing count as the reported cost; "NO census" | the cost and the `H₂` precedent |
| bean `qou-1qsw` + owner ruling 2026-08-30 | `H₂` selector = PSD parity, `k = 0` is PSD, the selected vertex is the **minimal non-zero** PSD power `σ₀²`; nucleon crossing budget **11** (6 Borromean + 3 quark + 2 gluon) | the non-zero rule and the crossing budget |
| `computations/hoefsmit_mpmath.py`, `pyhecke.syt_prefix_cache.BlockCache` | Hoefsmit orthogonal form in mpmath: `a = h/(1−q^{−2ρ})`, `a' = h/(1−q^{2ρ})`, `b = √|aa'+1|` | the `(2,1)` and all `H₆` block images |
| `computations/y_lambda_su_n.py`, `wedderburn_jones_markov.y_lambda_at` | convention-D `y_λ` (`y_(1³) = 0`; `(3) → 0.5054`, `(2,1) → 0.2473`) | `tr_M = Σ y_λ χ_λ` |
| `computations/borromean_h3_2_1_irrep_derivation.py`, Lean closed form `(4+h²−3h⁴−h⁶)/(h²+4)` | `tr_M(β_Bor)` from the `(2,1)` irrep | cross-check target |
| `computations/binding_log_free_energy.py`; `binding_canonical.py` banner (ruling 2026-09-05) | live law `B = E₀·ln(tr_M(W_free)/tr_M(W_atom))`, `E₀ = m_e c_q² ℏ_q/(1−ℏ_q²) = 4.227483` MeV | the pp functional |
| `computations/mass_at_3A_proper.atom_braid_word_3A` | template inter-nucleon bond = one `σ` at gen `3k+2`; ratio `tr_M(W_atom)/tr_M(W_free) = ∏(z + dᵢ)` by connected-sum multiplicativity | the template pp bond and a cross-check |
| `computations/probes/frobenius_admissibility_net_row_probe.py` (#7184) | the 11-letter nucleon block, cross-checked to `build_atom_nf` at 5e−16 | the nucleon block on six strands |
| `computations/lp_dual_solver.py::solve_psd_operator_selection_sdp` | the generic PSD operator-selection SDP (needs a cost vector `t`, Gram `G`, `n_target`) | **not used**: it optimises coefficients on the NF basis, not a choice among words; its `n_target` is the circularity `qou-ales` names in `nucleus_operator_selection_sdp.py` |
| `QOU/QBeta/SingleCrossingAlwaysBinds.lean`, bean `qou-vbyi` | the template pp bond binds; every in-algebra sign direction closed; "structural change needed" | what the pp result is measured against |

## 1. Lean — what was instantiated and what the lemmas say

File: [`QOU/Mass/GammaGammaSelectorH3.lean`](https://github.com/litlfred/qou/blob/11942d17b7/content/quantum-observable-universe/lean/QOU/Mass/GammaGammaSelectorH3.lean)
(new; imports the step-1 module).

**Verification.** `lean -DautoImplicit=false -s 65536 <file>` against the restored
`LEAN_PATH` (Mathlib 3480 oleans; the step-1 module compiled with `-o` into the
paper's build dir first, since it is not in the cache): **exit 0, no warnings.**
`#print axioms` on all **26** theorems: `[propext, Classical.choice, Quot.sound]`
or none — **no `sorryAx`**. Library file, no sidecar; lean-direct is the gate.

`H₃` is instantiated as `h3Blocks q h S : WedderburnBlocks ℝ Word H3Block H3Block.dim`
with blocks `triv/std/sgn` of dimensions `1/2/1`: `(3)` by the trivial character
`σ ↦ q`, `(2,1)` by the left-to-right product of Hoefsmit images (`σ⁻¹ ↦ ρ(σ) − h·1`),
`(1³)` by step 1's alternating character. "Every Wedderburn block image is PSD"
for a candidate word `w` therefore means: the scalar `trivChar q w ≥ 0`, the `2×2`
`stdImage S h w` is `Matrix.PosSemidef` (symmetric with non-negative form), and
the scalar `altChar q w ≥ 0`.

| theorem | statement | why it is falsifiable |
|---|---|---|
| `gammaGamma_inH3_eq_vertexPow` | a γγ-word using only `σ₀, σ₁` is `(σ₀σ₁⁻¹)^k` for some `k` | a vertex `σ₁σ₂⁻¹` would be a γγ-word in `H₄` but not `H₃`; the lemma is what makes the probe's one-parameter scan complete rather than chosen |
| `trivChar_eq_one` (`q ≠ 0`) | the `(3)`-block image of every γγ-word is `1` | a bare `σ₀²` vertex would give `q²` |
| `psdFeasible_iff_std` (`0 < q`) | for a γγ-word, `PSDFeasible ↔ (2,1)-image PosSemidef` | reduces the three-block condition to one block — the task's suggested lemma, proved |
| `vertex_std_not_isHermitian` (`0 < q`, `b ≠ 0`) | the `(2,1)` image of `σ₀σ₁⁻¹` has entries `[[q(a−h), qb], [−q⁻¹b, −q⁻¹(a'−h)]]` and is not symmetric | would fail if `b = 0` or if the vertex were `σ₀σ₁` (both entries `qb`)… the off-diagonal ratio is `−q²`, checked numerically first |
| `vertex_not_psdFeasible` | hence the single vertex is not PSD-feasible on `H₃` | mirror of step 1's `σ₀` on `H₂` |
| `hoefsmitA_add_A'`, `hoefsmitA_mul_A'_add_one` (`0 < q ≠ 1`) | `a + a' = h` and `a·a' + 1 = [3]_q/[2]_q²` | exact closed forms for the Hoefsmit data; the probe checks them to `2e−61` |
| `hoefsmitB_pos` | `b = √([3]/[2]²) > 0` | so `b ≠ 0` is **derived** — `hoefsmit_vertex_not_psdFeasible` carries no `b` hypothesis |
| `hoefsmit_std_sigma1_hecke`, `hoefsmit_std_sigma0_hecke` | both generator matrices satisfy `σ² = hσ + 1` | a mistyped `a`, `a'` or `b` fails it |
| `nil_psdFeasible`, `sdpSelected_nil` | `[]` is PSD-feasible; under `cost = length` the literal `SDPSelected` selects `[]` over any candidate set containing it | true and deliberately stated: it is the `k = 0` of the `H₂` precedent, and the reason the corpus's rule is "minimal non-zero" |

Not proved in Lean (measured in the probe instead): that `(σ₀σ₁⁻¹)^k` has a
non-symmetric `(2,1)` image for every `k ≥ 1` — the `k = 1` case is the theorem;
`k ≤ 5` is the measurement.

## 2. Probe — the selection table at the proton pin

Probe: [`computations/probes/gamma_gamma_h3_psd_selector_probe.py`](https://github.com/litlfred/qou/blob/11d00bd72c/computations/probes/gamma_gamma_h3_psd_selector_probe.py)
+ witness `gamma-gamma-h3-psd-selector-probe.witness.json` (`q0Anchor = proton`,
mpmath 60 dps end to end, **8/8 assertions**, 5.5 s). Crossing budget: `2k ≤ 11`
(`qou-1qsw`) ⇒ `k ≤ 5`, exposed as `--kmax` — a scan parameter, not a choice.

Three readings of "PSD" are tested per block image `M`, because the literal one
has a Hermitian half that a braid word's image generically fails:

* **(i) literal** — `M` symmetric and eigenvalues `≥ 0` (`Matrix.PosSemidef`, the Lean `SDPSelected.psd`);
* **(ii) form** — the symmetric part `(M+Mᵀ)/2` has eigenvalues `≥ 0` (the `∀x, xᵀMx ≥ 0` half only);
* **(iii) frobenius** — `χ_λ(M) = tr M ≥ 0` on blocks with `y_λ > 0` (constraint (1) of `prop:confinement-sdp`, `⟨π_λ, Φ⟩ ≥ 0`; under D `y_(1³) = 0`).

Tolerance `1e−40`; cost = crossing count.

### 2.1 `H₃` nucleon candidates `V^k = (σ₀σ₁⁻¹)^k`

| k | crossings | `‖M−Mᵀ‖` (2,1) | min eig sym part | `χ_(2,1)` | `χ_(3)`, `χ_(1³)` | (i) | (ii) | (iii) | `‖V^k − I‖` |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 2 | 1, 1 | ✓ | ✓ | ✓ | 0 |
| 1 | 2 | 2.4673 | −0.7042 | −1.0437 | 1, 1 | ✗ | ✗ | ✗ | 2.494 |
| 2 | 4 | 2.5751 | −0.6457 | −0.9107 | 1, 1 | ✗ | ✗ | ✗ | 2.443 |
| **3** | **6** | 0.2204 | +0.9808 | **+1.9942** | 1, 1 | ✗ | **✓** | **✓** | 0.113 |
| 4 | 8 | 2.3451 | −0.7587 | −1.1707 | 1, 1 | ✗ | ✗ | ✗ | 2.542 |
| 5 | 10 | 2.6680 | −0.5834 | −0.7724 | 1, 1 | ✗ | ✗ | ✗ | 2.388 |

Selection (cost-minimal; "min non-zero" per the 2026-08-30 rule):

| reading | feasible `k` | literal minimum | **minimal non-zero** |
|---|---|---|---|
| (i) literal | {0} | `[]` | **none** |
| (ii) form | {0, 3} | `[]` | **k = 3 = β_Bor** |
| (iii) frobenius | {0, 3} | `[]` | **k = 3 = β_Bor** |

Cross-checks in the witness: the `(3)` and `(1³)` images are `1` to `1.6e−60`
(the two Lean character lemmas); `tr_M(V³) = 0.99856216383678726595` agrees with
the Lean Borromean closed form to `6.2e−61`; the Hoefsmit `(2,1)` data matches
`a = h/(1−q⁴)`, `b² = [3]/[2]²` to `2.3e−61`.

**Reading.** The vertex's `(2,1)` image lies in `SL₂(ℝ)` with trace `−1.0437`,
i.e. it is elliptic; `V³` is within `0.11` of the identity (at `q = 1` it *is* the
identity — `(12)(23)⁻¹` is a 3-cycle). That is why `k = 3` and only `k = 3` in the
budget has a positive block trace and a positive form, and why no `k ≥ 1` is
symmetric. Under (ii)/(iii) the minimal non-zero γγ-word of `H₃` at the proton pin
is **`β_Bor` — the template nucleon core** (6 of its 11 crossings; the quark and
gluon letters are not γγ-produced and are outside this scan). Under (i) the
selector returns the identity and no non-zero word.

### 2.2 pp bond candidates on the `H₆` interface

The template pp bond is a single `σ₂` (gen `3k+2`), not γγ-produced
(`not_gammaGamma_single`). γγ bond candidates are `G^m = (σ₂σ₃⁻¹)^m`. Tested on
all 11 blocks of `H₆` (D weights positive on `(6), (5,1), (4,2), (3,3)`):

| bond | crossings | (i) | (ii) | (iii) | worst `y>0` block: `χ` |
|---|---|---|---|---|---|
| template `σ₂` | 1 | ✗ | ✗ | ✓ | `(6)`: 1.1100 |
| `G⁰` | 0 | ✓ | ✓ | ✓ | `(6)`: 1 |
| `G¹` | 2 | ✗ | ✗ | ✗ | `(3,3)`: −1.0874 |
| `G²` | 4 | ✗ | ✗ | ✗ | `(3,3)`: −0.8214 |
| **`G³`** | **6** | ✗ | **✓** | **✓** | `(6)`: 1 |
| `G⁴` | 8 | ✗ | ✗ | ✗ | `(3,3)`: −1.3413 |
| `G⁵` | 10 | ✗ | ✗ | ✗ | `(3,3)`: −0.5447 |

Same shape as `H₃` (the bond word lives in the `⟨σ₂,σ₃⟩ ≅ H₃` subalgebra, and the
`H₆` blocks restrict to sums of `H₃` blocks): minimal non-zero survivor **`G³`**
under (ii)/(iii), none under (i). The template `σ₂` passes only Frobenius
positivity — its eigenvalues `q, −q⁻¹` fail both matrix readings.

### 2.3 The diproton sign

`W_free = p(σ₀,σ₁)·p(σ₃,σ₄)` (two 11-letter nucleon blocks, no bond),
`W_atom = W_free·bond`, `tr_M` over all 11 `H₆` blocks, `B = E₀ ln(tr_free/tr_atom)`,
`E₀ = 4.22748335563` MeV. `tr_M(W_free) = 0.39605423781928265702`.

| bond | `tr_M(W_atom)` | `tr_atom/tr_free` | **`B_pp` [MeV]** | sign |
|---|---|---|---|---|
| template `σ₂` | 0.242657693573 | 0.612688037146 (= `z_D`, dev 1.6e−61) | **+2.0710** | binds |
| `G¹` | 0.156693543813 | 0.395637 | +3.9200 | binds |
| `G²` | 0.147108466723 | 0.371435 | +4.1868 | binds |
| **`G³`** | 0.396473165197 | **1.001058** | **−0.004469** | **unbound** |
| `G⁴` | 0.145794758301 | 0.368118 | +4.2247 | binds |
| `G⁵` | 0.158064669450 | 0.399099 | +3.8831 | binds |

Cross-checks: the template ratio equals `z_D` (connected-sum multiplicativity,
`atom_braid_word_3A`); the template traces agree with
`tr_m_atom_via_transfer.tr_m_atom_zn(2, 0)` to `6.0e−50` relative.

**Result, stated as scope-(a).** *With the pp bond selected by the
Frobenius-positivity / quadratic-form reading of the confinement SDP — `G³`, the
minimal non-zero γγ bond — the log-law diproton is **unbound**, `B_pp = −4.47 keV`,
against `+2.07 MeV` for the template `σ₂` bond.* The sign flips. What this does
and does not say:

* It is the first pp sign change in the corpus that is not obtained by tuning
  anything: the bond is fixed by positivity + minimal cost + the `qou-1qsw`
  budget, and no measured binding value is consulted.
* The magnitude is small for a structural reason: `(σσ⁻¹)³` is within `0.11` of
  the identity in every irreducible block at `q₀`, so the bond barely perturbs
  the free trace (`tr_atom/tr_free = 1.00106`). The sign is set by that
  perturbation being *upward*. Nothing here compares `4.47 keV` to a measured
  diproton virtual-state energy, and nothing should — the point is the sign.
* It holds under readings (ii)/(iii) only. Under the literal
  `Matrix.PosSemidef` reading — the one the step-1 Lean states — **no non-zero
  bond is selected**, so the sign question is not posed by the literal predicate.
* `G¹`, `G²`, `G⁴`, `G⁵` all bind *harder* than the template (≈ 4 MeV). So "any
  γγ bond" does not unbind the diproton; the selected one does.

## 3. Precision preflight

`scripts/precision-gates.sh --changed` (`qou_substrate`, `pyhecke` on
`PYTHONPATH`): the new probe, witness and Lean file are **not named in any red**
(grep for `gamma-gamma-h3` / `GammaGammaSelectorH3` over the gate output: 0 hits).
The reds are the tree-wide ratchets already recorded on `main`
(`2026-09-08-raw-float64-ratchet-is-regressed-on-pristine-main.md`). The eleven
tree-measuring audit witnesses the gate regenerates were reverted and not
committed (`qou-v0t8`). The probe's own save-time raw-float64 warning
(`elapsed_seconds`) was fixed by dropping the field; the witness records no float.

## 4. What stays open — the bean does not close

1. **Which reading is the confinement SDP's.** `prop:confinement-sdp` constrains
   an *element* `Φ ⪰ 0` (and uses `⟨π_λ,Φ⟩ ≥ 0` as constraint (1)); applying
   "PSD" to the image of a *braid word* is the step-1 formalisation, and its
   literal form is never met by a non-trivial word because a word's image is not
   self-adjoint (`w* = reverse(w)`). The two weaker readings both select
   `β_Bor` / `G³`; the literal one selects the identity. Deciding this is
   deciding what the SDP means on words — an owner call, not a measurement.
   Default if nothing is decided: words stay template-assigned; this record
   stands as scope-(a).
2. **The non-γγ letters.** The nucleon's 3 quark and 2 gluon letters, and the
   colour-weighted pn bond, are outside the γγ class as step 1 defines it; a
   strictly γγ-selected nucleon is `β_Bor` alone (6 crossings), not the 11-letter
   block. The pp result above keeps the 11-letter blocks and selects only the
   bond.
3. **Generalisation in `k`.** Lean proves the single vertex is not symmetric in
   `(2,1)`; that no power is, is measured for `k ≤ 5`. A proof would go through
   "a symmetric element of `SL₂(ℝ)` with unit-circle spectrum is `±I`", so
   `V^k` symmetric ⇔ `V^k = I` ⇔ `kθ ∈ 2πℤ`, `cos θ = −0.5219`.
4. `qou-vbyi` is appended with the sign result and stays open.
