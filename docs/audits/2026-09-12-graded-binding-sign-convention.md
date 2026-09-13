# Graded binding: `+c_k` or `−c_k`? The corpus's functional makes the question empty

**Date:** 2026-09-12 · **Branch:** `claude/graded-binding-sign-convention-2026-09-12` · **PR:** #7223
**Bean:** `qou-zlra` (this), `qou-oooq` (origin), `qou-eqwg` (the within-generator question it left open),
`qou-brng` (row D of its escape enumeration — stays open)
**Lean:** `QOU/Mass/GradedBindingFunctionalPairTerm.lean` (sorry-free)
**Probe:** `computations/probes/graded_binding_sign_convention_probe.py` (21/21)

---

## 0. The claim, flatly

`the_asymmetry_term_lives_at_vassiliev_type_two_probe` (bean `qou-oooq`) found that
the chain trace, written as a product of bond factors `P(h) = ∏ᵢ fᵢ(h)`, has

```
c₂/c₀ = (N−Z)²/2 + (5−A)/8          (exact, chain, every A and Z)
```

and read binding as `−α c₂/c₀`, which makes the symmetric nucleus the most bound.
With `+c₂` it is the least bound. Bean `qou-zlra` asked which sign the framework
takes, and noted that `unified-iterative-correction`'s `ln|tr M_λ|` is a third
possibility.

**Answer.** Every binding law the corpus carries is a **logarithm** of a trace,
and for a logarithm — with either sign, at any scale — the type-two pair term is
absent. So the `+c_k / −c_k` question has no content for the functional the
corpus uses. It has content only for a **bare** (linear) functional of the trace,
and the corpus has exactly one bare *binding* law, `B = Q_β·(tr_free − tr_atom)`,
which was **refuted on 2026-09-05** on independent grounds (a product is not
extensive). The bare `|tr_M|` functionals that survive in the corpus are **mass**
functionals, not binding ones.

Formalised: for jets with unit constant term,

```
[h²] ∏ fᵢ      = Σᵢ cᵢ + Σ_{i<j} bᵢ bⱼ          (prod_c2)      — pair term present, for + and for −
[h²] F(∏ fᵢ)   = Σᵢ [h²] F(fᵢ)                    (additive_prod) — for ANY F with F(fg) = F f + F g
[h²] log ∏ fᵢ  = Σᵢ (cᵢ − bᵢ²/2)                  (logJet_c2_prod) — the pair term removed by (Σb)² = Σb² + 2e₂
```

and `−F`, `α•F` are additive whenever `F` is (`neg_additive`, `smul_additive`).
Measured on the corpus's own convention-D letters at the proton pin: the
second difference in `Z` of `[h²]P` is **4** at every `A = 3..12` (that is the
`(N−Z)²/2`), and of `[h²](±log P)` it is **0** at every `A` and every `Z`.

The 2026-09-04 audit `graded-scales-are-per-partition-not-per-type.md` had
already reached "moot for the chain" by measurement; this closes it by theorem
and removes the sign from the question entirely.

---

## 1. Corpus table — every site that reads an energy off a trace

Corpus-grep (paths 1–6): `docs/audits`, `content/`, `computations/`, the ledgers,
the library and `.beans/`. The prior conclusions sit in `qou-eqwg` (completed)
and the 2026-09-04 audit; the ruling in `2026-09-04-binding-law-options-decision-frame.md`
(§ "DECIDED", Option B) and `2026-09-05-binding-law-arc-synthesis.md` (§§1–5).

| site | functional | sign on the atom trace | status | Lean that fixes it |
|---|---|---|---|---|
| `computations/binding_log_free_energy.py` — the **live binding law** (owner ruling 2026-09-04 Option B; `E₀` ruling 2026-09-05) | `B = E₀·log(tr_free/tr_atom) = E₀·Σ_bonds (−ln b)` | **−log** (B > 0 since every `b ∈ (0,1)`) | **production** | `QOU.Mass.ChainTraceFactor.L_pp/L_nn/L_pn := −Real.log (…)`; `QOU.Mass.IntraOrderingInvariance.L_chain_eq_sum_of_intra`; `QOU.Mass.MarkovBondRuleForcesPairwise.bindingOfTrace` ("the production shape: `B = −α·ln(tr_atom/tr_free)`", generic `f` with the Cauchy condition); `QOU.Hecke.BondCutSymmetry` header ("adopted binding law … `e = −ln b`"), `BondCutSymmetryLogBound.energySlope_eq_log_form` |
| `rem:markov-trace-gibbs-free-energy` (interprets `prop:categorical-mass-markov`) | `𝔈_bind = E₀ ln(tr_free/tr_atom)` — "unaffected as a *definition*" | −log | content, remark | interprets `QOU.CategoricalMassMarkov` (single-level mass = `|∫ρ(β)|`, bare) |
| `rem:bond-log-ratio-is-a-free-energy`, `rem:canonical-trace-factorises-over-chain` | `L = Σ_interfaces −log(z + dᵢ)`; "that `B = αL` is the binding energy is an interpretation, not a result" | −log | content, remarks | `ChainTraceFactor.twoStrandTrace_eq`, `neg_log_prod`, `FreeEnergyReadingIsSigned` |
| `computations/binding_canonical.py::B_MeV` | `Q_β·(tr_free − tr_atom)` | **bare, linear** (`−tr_atom`) | production file, **REFUTED 2026-09-05** ("kept for provenance and comparison; do not quote") | none — the module banner is the carrier |
| `prop:unified-iterative-correction` + `hecke_core_legacy.unified_iterative_correction` | `B = Σ_λ m_e H_q(λ) y_λ (ln|tr M_λ^{(0..A)}| − ln d_λ)`, `y_λ = w_λ/d_λ − 1/[k]_q! ≥ 0` | **+log per Wedderburn block**, weighted | production accumulator (`mass-qvalue-by-level.witness.json`) | `QOU.Archimedean.ConfinedKnotBinding.Unified.unified_iterative_correction` — telescoping over an **abstract** `L : ℕ → F`; the logarithm is fixed by the `.md` and the producer, **not by Lean** |
| `prop:mass-coefficient-shadow-price` | coefficient = per-partition dual (no functional of a trace) | — | content | `mass-coefficient-shadow-price.lean` |
| `prop:per-braid-mass-tower` | **mass** `𝔪(W) = |tr_M(W)| + Σ Φ_q(|tr_M(ξ)|) + z² Σ Φ_q(|tr_M(ξξ')|)` | bare `+|tr|` | content (proposition) | `QOU.BraidKnot.PerBraidMassTower` — a **class** (conditional), and its `mark_z` is convention C |
| `thm:six-term-mass-formula-complete` | **mass** Term 1 `= |tr_M(T_w)|` + five terms | bare `+` | content (theorem) | `six_term_mass_formula_complete` — additive bookkeeping only, all six terms opaque (its own docstring) |
| `rem:vassiliev-filtration-mass-tower` | the expansion `tr_M = c₀ + c₁h + c₂h² + …`; per-type LP cost vectors | none stated | content (remark) | none |
| `rem:phi-q-resums-trace-series` | `Φ_q` resummation factors through Markov traces | none stated | content (remark) | none |
| `the_asymmetry_term_lives_at_vassiliev_type_two_probe` | `−α c₂/c₀` | **assumed −**, "not derived" (its own caveat) | probe | none |
| Mayer/Ursell arc — `2026-09-12-ursell-partition-function-for-b3.md` (#7198), `2026-09-12-dominant-summand-extensive-test.md` (#7200), #7204 class B | `B = −α ln(Ξ/Ξ_free)`; `E₀·ln(tr_free/tr_atom)`; `E₀·ΔL` of `log|y_λ* χ^λ*|`; `e = −ln b` | −log | probes / audits | `QOU.MassTheory.UrsellPartitionFunctionB3`; `BondCutSymmetryNoSignDefinite` |

**What the corpus fixes.** The binding functional is a logarithm — by owner
ruling (2026-09-04 Option B, "the functional with the right extensivity is
forced, not chosen"; 2026-09-05 `E₀ = 4.227483` MeV), by the production code, by
the content blocks, and by Lean (`bindingOfTrace` names it "the production
shape"). No content block, Lean declaration or producer reads *binding* as a
bare Vassiliev coefficient. The bare `|tr_M|` readings are the **mass**
formulae, and the difference of two masses — which is what a bare binding
functional would be — is exactly the refuted `Q_β·Δtr` law.

**Two log readings coexist, and they are inequivalent.** (i) The live law takes
the log of the **Markov-weighted total** trace, which on the chain is a scalar
product of bond factors — so the log is exactly additive over bonds
(`L_chain_eq_sum_of_intra`). (ii) `unified-iterative-correction` takes a
`y_λ`-weighted sum of logs of **single Wedderburn blocks** `tr_λ(∏(cσ+d))`; a
single block's trace is not multiplicative (§4c below), so this functional is
not additive over bonds even on the chain, and (ii) is not a re-expression of
(i). This is a collision the bean did not name; it is recorded here as a
finding, and **not** resolved by picking one (that would be selection against
the target, and neither functional was chosen for its numbers here).

---

## 2. The Lean

`content/quantum-observable-universe/lean/QOU/Mass/GradedBindingFunctionalPairTerm.lean`,
generic `[CommRing R]` throughout except the formal logarithm (`[Field K]`
`[NeZero (2 : K)]`, needs `1/2`). Verified `lean`-direct against the Mathlib
oleans with `-DautoImplicit=false -s 65536`, exit 0; `#print axioms` on
`prod_c2`, `two_mul_e2_census`, `additive_census`, `logJet_mul`, `logJet_c2_prod`,
`logJet_c2_census`, `neg_logJet_c2_census`: `propext`, `Classical.choice`,
`Quot.sound` only — no `sorryAx`.

| declaration | states |
|---|---|
| `Jet2`, `CommMonoid` instance | the ring `R[h]/(h³)` of 2-jets, so `List.prod` is available |
| `e2`, `e2_append` | `e₂(l₁ ++ l₂) = e₂ l₁ + e₂ l₂ + (Σ l₁)(Σ l₂)` — the **cross term** between bond classes |
| `two_mul_e2_replicate`, `two_mul_e2_census` | `2e₂` of the chain census is a quadratic form in `(n_pp, n_pn, n_nn)` with all three cross terms |
| `sq_sum_eq` | `(Σb)² = Σb² + 2e₂(b)` |
| `prod_c2`, `neg_prod_c2` | `[h²]∏ = Σc + e₂(b)`; negation flips it, does not remove it |
| `IsAdditiveOnProducts`, `additive_prod`, `additive_census` | any Cauchy functional of the product is the sum over factors, hence **linear in the counts** |
| `neg_additive`, `smul_additive` | `−F`, `α•F` are Cauchy when `F` is — the sign and the energy scale never enter |
| `logJet`, `logJet_mul`, `logJet_prod`, `logJet_c2_prod` | the formal log is Cauchy on unital jets; `[h²]log∏ = Σ(cᵢ − bᵢ²/2)` |
| `logJet_c2_census`, `neg_logJet_c2_census` | the type-two piece of `±log` of the chain product is linear in the counts |

What it does **not** formalise: that the chain's Markov trace is a scalar
product of bond factors. That is `rem:canonical-trace-factorises-over-chain`
(measured to `~10⁻⁵⁹`, resting on connected-sum multiplicativity, classical and
not formalised — as that block itself records). The Lean says what any
product-additive functional does *to* a product; the corpus supplies the product.

---

## 3. The probe (21/21, 41 s, `mp.dps = 70`, proton pin via `q_at()`, convention D, exact `Fraction` for every `h`-coefficient, no float64)

### S1 — the letters, recomputed

```
q₀    = 1.109978582751380807591669       h₀ = 0.2090602987956393154308462
b_pp  = 0.6126880371464652516            L_pp = 0.48989938425513485141
b_pn  = 0.50822978937673896258           L_pn = 0.67682159238634338966
b_nn  = 0.40362773835082593616           L_nn = 0.90726226553321290067
E₀(N=0) = 4.18598136329 MeV   E₀(full, ruled) = 4.22748335563 MeV
```

`b_nn = 1/(q(q²+1))`, `L_pp + L_nn = 2 log(q+1/q)`, `b_pp > b_pn > b_nn > 0`
(the `ChainTraceFactor` theorems) hold to `< 10⁻⁵⁸`; the `h`-series `q(h)`
satisfies `q − 1/q = h` exactly; all three factors share constant term `1/2`.

### S2 — exact `h`-series, the theorem's content on the corpus's letters

| A | `[h²]` of the product, 2nd diffs in Z | `[h²]` of `+log`, 2nd diffs | `[h²]` of `−log`, 2nd diffs |
|---|---|---|---|
| 4 … 12 | **{4}** at every A | **{0}** | **{0}** |

`c₂/c₀ = (N−Z)²/2 + (5−A)/8` reproduced exactly for `A = 3..12`, every `Z`;
`[h²]log P = Σ(cᵢ − bᵢ²/2)` and `[h²]P = Σcᵢ + e₂(b)`, `(Σb)² = Σb² + 2e₂`
verified exactly on the same data. (Normalised type-one coefficients
`b/z₀`: pp `1`, pn `0`, nn `−1`; type-two `c/z₀`: pp `1/4`, pn `−1/4`, nn `1/4`
— the pn letter is the exact midpoint at these orders, as `qou-oooq` recorded.)

### S3 — valley scan at `q₀`, `argmax_Z` at fixed `A = 3..12`

| functional | argmax_Z, A = 3..12 | interior maximum (a valley) at |
|---|---|---|
| **log-ratio, the live law** | `1,1,1,1,1,1,1,1,1,1` | none — endpoint (most neutron-rich) |
| bare difference `Q_β(tr_free − tr_atom)` (refuted) | `2,3,4,…,11` | none — endpoint |
| `−c₂/c₀` alone (the `qou-oooq` reading) | `1,2,2,3,3,4,4,5,5,6` | **A = 4..12, at N = Z** |
| `+c₂/c₀` alone | `1,1,…,1` | none |
| bare truncation `−(1 + c₁h + c₂h²)` | `1,1,1,1,1,2,2,3,3,4` | A = 8..12 |
| bare truncation `+(1 + c₁h + c₂h²)` | `2,3,…,11` | none |
| bare `∓∏(f/z₀)` resummed | endpoints | none |

So the valley the type-two probe found is real *for the reading it assumed*,
inverts under the opposite sign, and is absent under both signs of the
resummed bare product and under the live law — which is the theorem, seen
numerically.

### S4 — the `qou-eqwg` question: "the corpus multiplies transfer matrices *within* a generator and takes a scalar product *across* generators; can non-commutativity inside a generator carry a quadratic?"

**(a) There is no non-commutativity inside a generator.** The transfer
matrices `T(c,d) = [[ch+d, c],[c, d]]` of letters on one generator commute
exactly — checked at a rational `q = 3/2` and as `h`-series — because they are
the regular representation of the *commutative* algebra `R[σ]/(σ² − hσ − 1)`.
The retracted 2026-09-04 matrix test (`V = 1.128089` against the proved
`z = 0.612688`) was a transcription error on top of a question that was empty.

**(b) What is non-multiplicative inside a generator is the two-branch state
sum, and the chain never exercises it.** `tr₂(∏ᵢ(σ + dᵢ)) = w₊∏(q+dᵢ) +
w₋∏(−q⁻¹+dᵢ)` is not the product of the per-letter traces: two interface
letters stacked on one generator have `[h⁰]tr = 1` against `(1/2)²`, and
`[h²]log` cross terms `5/8` (pp,pp), `−1/32` (pp,pn), `−1/2` (pn,pn), `1/4`
(pp,nn), `−1/32` (pn,nn), `5/8` (nn,nn). This is the interface-multiplicity
effect `qou-ib3g` measured, and the canonical chain puts each interface letter
on its own generator `σ_{3k+2}`, so it does not arise there.

**(c) A single Wedderburn block is non-multiplicative even on the chain — and
that is the `unified-iterative-correction` functional's object.** Using a
rational Hoefsmit seminormal form (relations checked exactly on all 11 shapes;
characters agree with `hecke_core_legacy._build_ysn_matrices_exact` at `q₀` to
`< 10⁻⁵⁰` on four shapes and four words), the chain word (canonical eleven-letter
intra blocks, one interface letter per adjacent pair, generators mapped
cyclically into `H_k` as `_step_chain_generic` does):

| block λ | `[h²] log tr_λ`, second differences in Z, A = 4 / 5 / 6 |
|---|---|
| (2), (1,1), (3) — one-dimensional | 0 / 0 / 0 (characters multiply) |
| (2,1), (2,2), (3,1,1) | `tr_λ` vanishes at `h = 0` — log undefined at type two |
| (3,1) ≡ (2,1,1) | `−77/8` / `{−59/4, 213/8}` / `{−133/8, −63/4, 303/8}` |
| (3,2) ≡ (2,2,1) | `−69/8` / `{−35/8, 79/8}` / `{−31/4, 45/8, 65/8}` |
| (4,1) | `−15/8` / `{−9/4, 17/4}` / undefined |

Nonzero and **not constant**: the per-block log is neither linear nor quadratic
in `Z` on the chain — the cyclic generator map makes the word's structure depend
on `Z`. Its sign at type two is **computed** (mixed across `Z`), not a
convention. On the UIC's own all-pairs layout the same quantity is also
non-linear, but there the counts are already quadratic, so that layout does not
isolate the functional; the chain rows are the clean test.

Not done: a scan of the **production** accumulator
`hecke_core_legacy.unified_iterative_correction(Z, N)` over `A = 3..12`.
Measured this session: `(Z,N) = (2,2)` did not return within **300 s** and was
killed (exit 143). The single-block rows above are UIC-*shaped* (same letters,
same cyclic map, `k ≤ 5`), not the producer's `k ≤ 11` sum with its weights.

---

## 4. Scope, per the (a)/(b) rule

- **(b) structural.** *No product-additive functional of the chain trace — log,
  −log, α·log, any sign, any scale — carries the type-two pair term, hence no
  `(N−Z)²` from the pair convolution.* Invariant: `additive_census` /
  `logJet_c2_census` / `neg_logJet_c2_census` (sorry-free), applied to the
  chain's scalar-product form (`L_chain_eq_sum_of_intra`, measured `10⁻⁵⁹`).
  This excludes the *ingredient* "sign convention" from every log-type reading.
- **(b) structural.** *The bare coefficient carries the pair term for either
  sign.* Invariant: `prod_c2`, `neg_prod_c2`, `two_mul_e2_census`. Flipping the
  sign turns the valley into a hill (S3); it does not remove the curvature.
- **(b) structural.** *"Non-commutativity inside a generator" is empty.*
  Invariant: the transfer matrices are the regular representation of a
  commutative algebra (S4a, exact).
- **(a) scope-limited.** The S3 valley table (which functional is monotone at
  `q₀`, `A ≤ 12`), and the S4c single-block non-linearity (11 shapes, `A ≤ 8`,
  UIC-shaped word, not the producer). These constrain magnitudes and the specific
  constructions tested, not ingredients.

---

## 5. What this means for the valley of stability

The standing verdict "no sum-over-bonds model has a valley for any `q`" was
right, and `qou-oooq` explained it as "`−log` kills the pair term". This audit
sharpens both halves:

1. The killing is not specific to `−log` or to the sign. It is the Cauchy
   condition `F(fg) = F f + F g`, which the live law satisfies by owner ruling
   ("`log` is the unique map carrying multiplicative to additive"). **The
   functional the corpus chose for extensivity is, by the same theorem, the
   functional that cannot carry a pair term.** Extensivity and the symmetry
   energy are in tension at the level of the functional, not the letters: the
   `(N−Z)²` a valley needs is a two-bond correlation, and a functional that is
   additive over bonds has no two-bond correlations. This is the same fact
   `bindingOfTrace_isPairwise` states for the connected cumulants, seen at
   Vassiliev type two.
2. The valley `qou-oooq` found lives in a functional the corpus does not use
   for binding (a bare Vassiliev coefficient), under a sign nothing derives;
   the honest statement is that the type-two shape result was a property of the
   **product**, and the framework reads the **log**.
3. The one live functional outside the additive class is
   `unified-iterative-correction`'s per-block log. Its type-two piece on the
   chain is non-linear in `Z` with computed signs (S4c). Whether the production
   accumulator has an interior maximum in `Z` at fixed `A` is **unmeasured**
   (the producer exceeds 300 s at `A = 4` here). Nothing changes if that stays
   unmeasured: the live law is (i), not (ii), and no dashboard row reads (ii)
   for a valley. Recorded in `qou-zlra` as the next measurement, not as a
   decision.

Nothing is fitted, nothing is wired, no sign is chosen. The corpus's letters
enter only as derived closed forms; AME enters nowhere.

---

## 6. Verification

- Lean: `lean -DautoImplicit=false -s 65536` against the Mathlib oleans, exit 0;
  seven `#print axioms` on standard axioms only (§2).
- Probe: `PYTHONPATH=tools/qou-substrate/python:tools/pyhecke/python:computations:schemas/witness-schema/python python3 -u computations/probes/graded_binding_sign_convention_probe.py 2>&1 | tee /tmp/graded_binding_sign_convention_probe.log` — 21/21; witness
  `computations/probes/graded_binding_sign_convention_probe.witness.json`
  (`q0Anchor: proton`, no raw float anywhere in the file — checked by walking
  the JSON).
- `scripts/precision-gates.sh --changed` and `scripts/check-sidecars.sh`: see
  the PR body for the exit status and the offender lists (the tree-wide gate is
  red on `main` independently, bean `qou-v0t8`; what is reported is that no
  file of this branch appears in any offender list and the raw-float64 ratchet
  shows `NEW dirty: 0`).
