# Handoff: Q_β Form A ≡ Form B bridge — paper + Lean closure

**To:** future agents (paper docs + Lean formalization + sibling-PR coordinators)
**From:** PR #637 (Carl Leitner / claude), commits up to `9291ae50`
**Status:** mathematical content derived; needs paper documentation + 100% Lean

## TL;DR for the next agent

The Q_β residual decomposition is mathematically settled in this session's audits:

- `docs/audits/2026-05-11-q-beta-residual-decomposition.md`
- `docs/audits/2026-05-11-q-beta-form-A-vs-form-B-canonical-choice.md`

**Key finding**: Form A ($\varepsilon \cdot E_0$, NF counit) and Form B (transfer-matrix log-ratio) are TWO REPRESENTATIONS of the SAME Q_β in different bases. The bridge is

$$\frac{\text{Form A}_\text{dimensionless}}{\text{Form B (log-ratio)}} = \frac{1}{z} + \frac{(z-1) \cdot h}{2z} + O(h^2)$$

where $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov parameter, $h = q - q^{-1}$.

Both finite-truncation predictions are justified by the **eigenfunction dampening** principle: `archimedean-remainder-exponential-decay.md` conjectures $\lvert R_n \rvert \le C(K) e^{-c(K) n}$ — exponential decay in GB filtration depth.

## TASK 1 — Paper content blocks (for documentation agent)

### 1A. New content block: `q-beta-spectral-bridge.md/.ts/.lean`

Location: `content/quantum-observable-universe/particle-interactions/`

**Statement (md content)**:

> **Proposition (Q_β spectral bridge).** The Q_β formula in the NF basis (Form A, `prop:neutron-qvalue-symbolic`) and in the torus-knot eigenfunction basis (Form B, `prop:beta-decay-transfer-matrix`) are equivalent representations of the same observable, with bridge identity
>
> $$\lvert \Delta(\text{net}) \rvert \cdot E_0 = \ln\frac{V_\text{pp}}{V_\text{nn}} \cdot \frac{E_0}{z} \cdot \bigl(1 + \tfrac{(z-1)h}{2} + O(h^2)\bigr)$$
>
> at single-wrap A=1. Both are finite-depth truncations of the infinite spectral decomposition, with exponential remainder per `archimedean-remainder-exponential-decay`.

**Proof outline** (md content):
1. Form A: $\lvert\Delta(\text{net})\rvert = h(2-h)/2 = h - h^2/2 + O(h^3)$
2. Form B: $\ln(1+zh) = zh - (zh)^2/2 + O((zh)^3)$
3. Ratio: $\frac{\text{A}}{\text{B}} = \frac{h - h^2/2}{zh - z^2h^2/2} \cdot \frac{1 + O(h)}{1 + O(h)} = \frac{1}{z} + \frac{(z-1)h}{2z} + O(h^2)$
4. ∎ (algebraic Taylor expansion)

**Uses**: `prop:neutron-qvalue-symbolic`, `prop:beta-decay-transfer-matrix`, `def:markov-parameter`, `conj:archimedean-remainder-exponential-decay`
**Tags**: `q-beta`, `spectral-bridge`, `basis-change`, `markov-parameter`, `eigenfunction-dampening`

### 1B. Edits to existing content blocks

**`beta-decay-transfer-matrix.md`** (line ~138, the "Q-value in log form" section):
- Reframe Form B as "Q-value in eigenfunction basis" — NOT a separate observable
- Cross-reference the new `q-beta-spectral-bridge` block
- Add caveat: the $1/z$ normalization factor is required to convert to MeV

**`neutron-qvalue-symbolic.md`**:
- Add cross-reference to `q-beta-spectral-bridge` — note Form A here equals Form B (spectral) up to the $1/z$ bridge.

**`archimedean-remainder-exponential-decay.md`**:
- Cross-reference Q_β closure: at depth $N$, $|Q_\beta^{(N)} - Q_\beta^\text{exact}| \le C \cdot e^{-cN}$.

### 1C. Author voice requirements

- Use `:defterm[...]{#slug}` / `:refterm[...]{#slug}` per AGENTS.md §4c (terminology contract)
- Cite all bibliographic refs in the Lean siblings per §1
- Math notation per the notation register (AGENTS.md §7aa)

## TASK 2 — Lean formalization (for Lean agent)

### 2A. New Lean file: `q-beta-spectral-bridge.lean`

Pair with `q-beta-spectral-bridge.md/.ts`. Provable in standard Mathlib:

```lean
namespace QOU.ParticleInteractions

/-- The Q_β spectral bridge: Form A (counit · E_0) and Form B
    (log-ratio · E_0/z) agree at leading order in h, with explicit
    correction (z-1)h/(2z) + O(h²). -/
theorem q_beta_spectral_bridge (q : ℝ) (hq : 1 < q) :
    let h := q - q⁻¹
    let z := 1 / (q.sqrt + (q.sqrt)⁻¹)
    let formA := abs (h * (h - 2) / 2)
    let formB := Real.log (1 + z * h)
    -- The bridge: formA / formB = 1/z + (z-1)h/(2z) + O(h²)
    abs (formA / formB - 1/z) ≤ abs ((z - 1) * h / (2 * z)) + h^2 := by
  -- Ref: [manuscript] prop:q-beta-spectral-bridge
  -- Ref: [manuscript] prop:neutron-qvalue-symbolic
  -- Ref: [manuscript] prop:beta-decay-transfer-matrix
  sorry

end QOU.ParticleInteractions
```

This is a **tractable Mathlib proof** (Taylor expansion + algebra). Should reduce to standard `Real.log_one_add_lt` lemmas.

### 2B. Close mechanical sorries in existing files

**`content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean`** (cycle 3, this branch):

2 mechanical zpow normalization sorries. Close via:
- Lemma 1: `zpow_neg_add_one` to rewrite $q^{-(k+1)}$ as $q^{-1} \cdot q^{-k}$
- Lemma 2: `abs_zpow_lt_one_of_pos` for the factor-non-zero proof

These require running the Lean compiler — better done with the formalizer skill.

### 2C. Open conjectures to formalize (deferred but on roadmap)

Per `MassComputationChainRoadmap.lean`:

- **Gap #12** (NEW from this session): prove `archimedean-remainder-exponential-decay`. **This is THE structural theorem** justifying all finite-truncation predictions. High value, multi-week R&D.
- **Gap #5**: n_⋆ existence — still tautological in current Lean.
- **Gap #4**: Φ_q convergence — partially closed (cycle 3), needs mechanical Mathlib glue.

### 2D. 100% Lean target

Realistically closing 100% Lean across all 12 gaps is **multi-month work**, not single-PR. Recommend the next Lean agent:

1. First close Gap #11 (q-beta-spectral-bridge theorem) — small, provable now
2. Then close the 2 PhiQConvergence mechanical sorries
3. Then tackle Gap #4 (full Φ_q Multipliable proof)
4. Defer Gaps #5, #12 to Workplan 2+ R&D (open conjectures)

## TASK 3 — Sibling coordination

### 3A. Post on PR #635 (Mikusiński WitnessBuilder migration)

After their merge, follow-up PR `claude/witnessbuilder-migration-cleanup` migrates the 7 PR-#637 scripts using `WitnessBuilder.wrap_legacy` pattern. Pinned in [coordination ledger](../coordination/2026-05-10-non-calibrated-q-beta-mass.md).

### 3B. Post on PR #636 (Plancherel weight audit)

Already coordinated this session ([comment 4422466834](https://github.com/litlfred/qou/pull/636#issuecomment-4422466834)): the dual-basis identity ($G^{-1} \cdot t = e_\gamma$) provides invariance under their R1 rename. No further action needed unless R1 lands.

### 3C. Compute-refinement requests for siblings

The next coordinator agent should ask sibling agents to:

1. **Refine the V̂_i definition** in `beta-decay-transfer-matrix.md`. Per cycle 6 audit, the simple $V̂_i = z M_{11} + M_{21}$ leads to a $1/z$ mismatch with Form A. Three structural options (V̂ redefinition, $1/z$ normalization factor, or reframe as decay amplitude) need framework decision.

2. **Compute Form B at higher truncation N=1, 2** properly via the cyclotomic projection at $n_\star$. The N=1 multiplicative ansatze in PR #637 commit `e1b005b2` all failed (42-134× worse). The correct N=1 form requires the open `brane-tower-z-habiro` $n_\star$ rule.

3. **Verify the dampening rate $c(K)$** for the β-decay sector: per `archimedean-remainder-exponential-decay`, $|R_n| \le C e^{-cn}$. Numerical sweep at depths $n = 0, 1, 2, 3$ would empirically pin $c$ for the free-neutron Q_β operator.

## TASK 4 — Out of session scope (this branch already has it)

PR #637's deliverables stand as-is. No further work needed on this branch beyond the items above:

- Form A canonical Q_β prediction (+0.17% / +1.31 keV)
- Phase 2 Path A derivation (replaces placeholder literals)
- ℏ_q audit + E_0_CONVENTIONS registry + Phase 3 Triton
- LP-dual H_3 negative finding (commit 1992c24d)
- Lean roadmap (Gaps 1-12 with partial closure on 4, 5)
- Frobenius factorization + dual-basis identity + Form A ≡ Form B unified picture
- Coordination ledger with cycles 1-7

## Pointers for next agent

| File | What it gives you |
|---|---|
| `docs/audits/2026-05-11-q-beta-residual-decomposition.md` | The Frobenius factorization 1.00744 = 1.00168 × 1.00579 |
| `docs/audits/2026-05-11-q-beta-form-A-vs-form-B-canonical-choice.md` | Form A vs Form B + bridge derivation + eigenfunction dampening (read cycles 5, 6, 7) |
| `docs/coordination/2026-05-10-non-calibrated-q-beta-mass.md` | Sibling PR map (cycles 1-3) |
| `content/quantum-observable-universe/lean/QOU/MassComputationChainRoadmap.lean` | 10+12 Lean gap inventory with citations |
| `content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean` | Gap 4 partial — 2 mechanical sorries to close |
| `content/quantum-observable-universe/lean/QOU/BraidKnot/BraneTowerNStar.lean` | Gap 5 partial — substantive predicate replacing tautological True |

## Conventions enforced by this branch

- **No fitting / no algebraic +1**
- **No float64** in production scripts (all mpmath 50 dps)
- **Three-calibration discipline** (CAL-1 m_e, CAL-2 q_0, CAL-3 𝔇_π as PREDICTION)
- **Form A as canonical Q_β** for free neutron (A=1)
- **No paper changes** in PR #637 beyond what's already committed (per owner directive)

Next agent: paper changes are now OK per latest directive, but stay in this audit framework's voice. Don't reintroduce calibrated $E_0 = Q_β$ as primary; keep derived $E_0 = m_e/(q(q-1))$ as canonical.

---

**Session context limit reached. Handing off.**
