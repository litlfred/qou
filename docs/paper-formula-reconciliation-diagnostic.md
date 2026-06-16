# Paper-formula reconciliation — diagnostic (2026-04-28)

**Branch:** `claude/alpha-fsc-audit`
**Triggered by:** parallel branch's `claude/continue-pr-442-DJRWm@a12818da2` finding that the paper's flagship single-term mass formula is **refuted at 87–100% error** on D/T/³He under both Plancherel and Wenzl–Schur conventions.

This doc surveys the inconsistency between the paper's two mass formulas and the compute's actual implementation, and frames what reconciliation requires. **It does not claim to solve the open theory question.**

---

## TL;DR

| Source | Formula | D residual vs AME | Status |
|--------|---------|:-----------------:|:------:|
| `prop:atom-knot-mass-derivation` | $B = m_e \cdot \rho \cdot \mathrm{tr}_M(T_w)\big|_{q_0}$ | **−93.4 %** (Wenzl-Schur) | refuted |
| `thm:knot-mass-formula-unified` (naïve sum) | $\mathfrak{m} = \|\mathrm{tr}_M\| + \sum \Phi_q(\|V_i\|) + z^2\sum \Phi_q(\|V_i V_j\|) + m_e \mathrm{tr}_M(C) + a_K B_{\mathrm{bulk}} + \ldots$ | **−201,427 %** (sign + magnitude) | refuted |
| `mass_formula_6term.py` (compute heuristic) | $E_0 \cdot \|\mathrm{tr}_M^{\mathrm{free}} - \mathrm{tr}_M^{\mathrm{atom}}\| + T_4$ | **+18 %** (Wenzl-Schur, T2+T3 missing) | not in paper |

All three disagree. The compute's heuristic is the closest to AME but has **no formal derivation** in the paper.

---

## The two paper formulas

### Single-term: `prop:atom-knot-mass-derivation`

$$
B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot \mathrm{tr}_M(T_w)\big|_{q = q_0}
$$

- **Units**: $m_e$ = MeV, $\rho \in \mathbb{Z}_{>0}$, $\mathrm{tr}_M$ dimensionless. Net: MeV. ✓
- **Boxed in the prop**: yes.
- **SDP-canonical numerical test** (parallel branch `a12818da2`):

  | atom | tr_M (Pl) | tr_M (W) | B (Pl) | B (W) | AME | err Pl | err W |
  |------|----------:|---------:|-------:|------:|----:|-------:|------:|
  | D    | 0.049     | 0.288    | 0.025  | 0.147 | 2.225 | −98.9 % | −93.4 % |
  | T    | −0.001    | 0.013    | −0.001 | 0.013 | 8.482 | −100 %  | −99.8 % |
  | ³He  | 0.986     | 0.998    | 1.007  | 1.020 | 7.718 | −87.0 % | −86.8 % |

- **Verdict**: refuted. The single-term form gives B ≈ m_e (≈ 0.5 MeV) while AME values are 2–8 MeV.

### Multi-term: `thm:knot-mass-formula-unified`

$$
\mathfrak{m}(\varrho)
\;=\;
\underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
\;+\;
\underbrace{\sum_{i} \Phi_q\bigl(|\hat V_i|\bigr) + z^2 \sum_{i<j} \Phi_q\bigl(|\hat V_i \hat V_j|\bigr)}_{\text{brane tower}}
\;+\;
\underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}\bigr)}_{\text{Frobenius}}
\;+\;
\underbrace{a_K \cdot B_{\mathrm{bulk}}}_{\text{chirality (4-tier)}}
\;+\;
\text{jet-level}
$$

- **Units (as written)**:
  - Descended $|\mathrm{tr}_M(T_w)|$: dimensionless (~0.1–0.5).
  - Brane tower $\sum \Phi_q(\cdot)$: dimensionless (Φ_q is a power series).
  - Frobenius $m_e \cdot \mathrm{tr}_M(C_{\dim_q})$: MeV.
  - Chirality $a_K \cdot B_{\mathrm{bulk}}$: MeV (if $B_{\mathrm{bulk}}$ is energy).
  - Jet-level: unspecified.

  **The formula is dimensionally inhomogeneous as written.** Adding a dimensionless number (~0.3) to a MeV value (~1.3) requires an implicit conversion that isn't specified.

- **Naïve sum** (treating each term as the literal value): **−201,427 % off on D** (per parallel branch `a5135cd8b`).

- **Verdict**: dimensional ambiguity must be resolved before the formula can be meaningfully tested.

---

## The compute's actual implementation

`mass_formula_6term.py` (per parallel branch's `a12818da2` audit):

| Term | Paper claim | What compute does |
|------|-------------|-------------------|
| T1 (descended) | added | `E0 · |tr_M(free) − tr_M(atom)|` (NOT `|tr_M|` alone — a *trace deficit* with E0 prefactor) |
| T2 (single-gen brane) | added | **computed but not added** |
| T3 (pair-gen brane) | added | **computed but not added** |
| T4 (Frobenius co-Casimir) | added | added (per-3A canonical) |
| T5 (chirality) | added | added when valid (A ≥ 3) |
| T6 (Habiro residue) | added | placeholder = 0 |

The compute uses **E_0 not m_e** as the prefactor and the **trace deficit** form `|tr_M(free) − tr_M(atom)|` rather than the single `|tr_M|` of the paper. These are not in either paper formula.

The `+18 % D residual` quoted in the compute's witness is a 4-term sum (T1 + T4 + T5=0 + T6=0) under this heuristic, **not** a faithful evaluation of either paper formula.

---

## Three reconciliation options

Any one of these would close the gap; none is currently chosen by the paper.

### Option A: Restate the unified formula with explicit unit conversion

Replace each dimensionless term with `m_e · (term)` (or `E_0 · (term)`). Then the formula becomes

$$
\mathfrak{m}(\varrho) \;=\; m_e \cdot \Bigl[\, |\mathrm{tr}_M| + \sum \Phi_q(|V_i|) + z^2 \sum \Phi_q(|V_i V_j|) + \mathrm{tr}_M(C_{\dim_q}) + \tilde a_K \tilde b + \tilde J \,\Bigr]
$$

with all dimensionless content inside the brackets. **Naïvely sums to −201,427 %** on D, so this isn't sufficient on its own — but it makes the formula well-posed for further refinement.

### Option B: Replace the descended term with the trace-deficit form

The compute's `|tr_M(free) − tr_M(atom)|` is what gets within 50–80 % on D. Promote it to the paper:

$$
\mathfrak{m}(\mathfrak{H}) \;=\; E_0 \cdot \bigl|\mathrm{tr}_M(T_w^{\mathrm{free}}) - \mathrm{tr}_M(T_w^{\mathrm{atom}})\bigr| + (\text{brane tower}) + m_e \cdot \mathrm{tr}_M(C_{\dim_q}) + \ldots
$$

Requires defining what "free" vs "atom" $T_w$ means structurally (currently a compute-side choice). **Open**: a categorical derivation of why the trace-*deficit* — not the trace itself — is the descended observable.

### Option C: Drop the single-term formula; treat the multi-term as canonical with paper-internal corrections

Mark `prop:atom-knot-mass-derivation` as **deprecated** (or restate it as a degenerate case of the unified formula at $\rho = 0$ in the higher terms). Carry only `thm:knot-mass-formula-unified` forward, and resolve the dimensional ambiguity per Option A or B above.

---

## What this branch contributes

This diagnostic doc + the typed `MarkovTraceConvention` discriminator (landed in commit `8d2e418aa..447fc87a9`):

```lean
inductive MarkovTraceConvention | plancherel | wenzlSchur

structure MarkovTraceCoefficient where
  value      : ℝ
  convention : MarkovTraceConvention

noncomputable def jonesMarkovTagged (q : ℝ) (lam : List ℕ) :
    MarkovTraceCoefficient :=
  { value := JonesMarkovCoefficient q lam,
    convention := .wenzlSchur }
```

This makes the **convention bug** addressable at the type level (a downstream consumer can demand `(c : MarkovTraceCoefficient).convention = .wenzlSchur` and the compiler will reject Plancherel-derived inputs). It does **not** address the formula-reconciliation question; that's open research belonging to the paper.

---

## Open work (carried)

1. **Pick one of A / B / C** and rewrite the offending propositions.
2. **Wire T2 + T3** into `mass_formula_6term.py` to enable testing the literal multi-term formula (currently tests a 4-term sum).
3. **Reconcile ρ**: paper text says `ρ = 1` for D/T/³He under the ℓ ≤ 1 rule; SDP witness disagrees on T (says 2) and ³He (says 2). Either fix the rule or fix the witness.
4. **Reconcile compute's `E_0` vs paper's `m_e`** as the energy prefactor.

These are theory-level decisions for the paper; this branch's contribution is the diagnostic above plus the type-level convention discriminator.

---

## Refs

- [`prop:atom-knot-mass-derivation`](../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
- [`thm:knot-mass-formula-unified`](../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md)
- [`prop:y-lambda-recipe-from-partition`](../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md)
- Parallel-branch audit findings: `claude/continue-pr-442-DJRWm@a12818da2` (refutation), `@a5135cd8b` (naïve-sum failure), `@b2c0e4af75` (Plancherel-vs-Wenzl-Schur)
- Compute heuristic: `computations/mass_formula_6term.py`
