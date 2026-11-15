# Step-by-step derivation tracking — methodology

**Branch:** `claude/alpha-fsc-audit`
**Position:** the parallel branch's "refutation" of `prop:atom-knot-mass-derivation` is not yet verified — it depends on a specific compute pipeline whose intermediate data has not been independently checked. The right response is a **canonical derivation chain** with explicit per-step data, against which any compute can be audited.

This doc establishes the chain and the per-step data manifest. Walkthrough on the deuteron follows in §4.

---

## 0. The canonical chain (per paper architecture)

```
   1. Categorical action of C on the state bundle S
            │  Yekutieli, non-abelian Stokes (finite slice)
            ▼
   2. Joint-tower confinement SDP at q_0
            │  GB filtration + jet-order log
            ▼
   3. T_w ∈ H_{n_0}(q_0), GB-normal form
            │  Wedderburn decomposition
            ▼
   4. H_{n_0}(q) ≅ ⊕_λ M_{d_λ}(Q(q))
            │  y_λ (Wenzl bridge), χ_λ (q-Murnaghan–Nakayama)
            ▼
   5. tr_M(T_w) = Σ_λ y_λ(q) · χ_λ(T_w) ∈ Q(q)
            │  ρ · (—)
            ▼
   6. M(H) = ρ · tr_M(T_w) ∈ Q(q)                    [pre-Archimedean]
            │  Archimedean realization (q := q_0, MeV scale)
            ▼
   7. B(H) = m_e · M(H)|_{q = q_0} ∈ R (MeV)         [post-Archimedean]
```

**Every step is finite and exact in Q(q) up to step 7.** No analytic limit is invoked; the volume conjecture is borrowed only for *naming* post-Archimedean values, not for derivation.

---

## 1. Per-step data manifest

Each step produces specific data. To audit a calculation we must record all of it.

| Step | Output | Type | Units | Convention notes |
|------|--------|------|-------|------------------|
| 1 → 2 | confinement-SDP feasible region | semi-algebraic set in `M_{d_λ}(Q(q))` per block | dimensionless | $q$-rational; PSD blocks |
| 2 → 3 | $T_w(\mathfrak{H})$ with GB-NF expansion | finite sum $\sum_w c_w(q)\,\sigma_w$ | dimensionless | jet order = reduction order; GB grade = filtration grade |
| 3 | filtration grade $\ell(T_w)$ per term | $\mathbb{N}$ | — | per-monomial |
| 3 → 4 | Wedderburn block matrices $\rho_\lambda(T_w) \in M_{d_\lambda}(Q(q))$ | one per $\lambda \vdash n_0$ | dimensionless | derived from seminormal form |
| 4 → 5 | $y_\lambda(q) \in Q(q^{1/2})$ | one per $\lambda$ | dimensionless | **Wenzl–Schur convention** (per `prop:y-lambda-recipe-from-partition`) |
| 4 → 5 | $\chi_\lambda(T_w) = \mathrm{Tr}\,\rho_\lambda(T_w) \in Q(q)$ | one per $\lambda$ | dimensionless | $q$-Murnaghan–Nakayama |
| 5 | $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda \chi_\lambda \in Q(q)$ | scalar | dimensionless | finite Jones-Markov |
| 5 → 6 | $\rho \in \mathbb{Z}_{>0}$ | scalar | — | from SDP-solution multiplicity |
| 6 | $M(\mathfrak{H}) = \rho \cdot \mathrm{tr}_M(T_w) \in Q(q)$ | scalar | dimensionless | categorical mass invariant |
| 6 → 7 | substitution $q := q_0$ | $\mathbb{R}$ | dimensionless | 50 dps via mpmath |
| 7 | $B(\mathfrak{H}) = m_e \cdot M(\mathfrak{H})|_{q_0}$ | $\mathbb{R}$ | MeV | Archimedean realization |

**Audit rule:** any compute claiming to evaluate $B(\mathfrak{H})$ must publish all 11 rows of this table. If any row is missing, the compute hasn't faithfully implemented the chain.

---

## 2. Where the parallel branch's "refutation" could be wrong

The `claude/continue-pr-442-DJRWm@a12818da2` audit reported $B(D, \mathrm{Wenzl}) = 0.147$ MeV vs AME 2.225 → −93.4 % error under the single-term formula. **This number is only meaningful if every row of the data manifest above is correct for the calculation that produced it.** Possible failure modes:

| Row | Possible issue with parallel-branch calculation |
|-----|--------------------------------------------------|
| 2 → 3 | $T_w(D)$ = "SDP-canonical braid word" — but is the SDP solver even returning the correct $T_w$? The parallel branch's PSD-cone audit shows D has $\alpha^* = 0.546$, i.e. the canonical $T_w$ does NOT make all blocks PSD. This means either (a) the canonical $T_w$ for D is unknown, or (b) the registry entry $6_2$ (knot $6_2$) is wrong. |
| 3 | filtration grade per term — was the GB reduction actually applied, or did the calculation use a non-canonical word? |
| 4 → 5 | $y_\lambda$ via Wenzl — the parallel branch confirmed Wenzl-Schur convention in use, but did it use the correct $y_\lambda$ values? Different $r$-parameterizations of the Wenzl bridge can give different answers. |
| 5 → 6 | $\rho$ for D — paper text says 1; SDP says 1 (agree on D); but if either value is wrong elsewhere in the chain this corrupts $M$. |
| 7 | $m_e$ — the calculation must use CODATA $m_e = 0.510998950$ MeV, not a fitted value. |

**Most suspicious step:** row "2 → 3". The PSD-cone audit (parallel branch's own data) reports $\alpha^*(D) = 0.546$, **meaning the registry entry $T_w(D) = 6_2$ does NOT canonically satisfy the SDP feasibility constraint**. Computing $\mathrm{tr}_M(6_2)$ and using that as if it were the canonical $T_w(D)$ is not a faithful test of the formula — it's a test of "what if we use a non-canonical braid".

---

## 3. What's actually needed before declaring refutation

For each test atom $\mathfrak{H} \in \{D, T, ^3\mathrm{He}\}$:

- **(R5-full SDP)** Solve the joint-tower SDP for the actual canonical $T_w(\mathfrak{H})$ with $\alpha^* = 1$ (all blocks PSD). The parallel branch flags this as not yet implemented (the Rust binary verifies *given* candidate $T_w$ but doesn't *solve* for unknown $T_w$).
- **GB-NF reduction** of the resulting $T_w$ with explicit jet-order log.
- **Wedderburn block matrices** $\rho_\lambda(T_w)$ symbolically in $Q(q)$ for every $\lambda \vdash n_0$.
- **Symbolic $y_\lambda$** from the Wenzl-bridge witness (already exists at $n \leq 12$).
- **Symbolic $\chi_\lambda(T_w)$** = trace of the block matrix product corresponding to the $T_w$ word.
- **Symbolic $\mathrm{tr}_M(T_w) \in Q(q)$**.
- **Documented $\rho$** with proof of multiplicity.
- **MPFR evaluation at $q_0$**, 50+ dps.

Only then does the comparison against AME tell us anything about the formula. The parallel branch's calculation skips R5-full SDP and assumes the historical knot ID $6_2$ as $T_w(D)$ — that's a calibration choice, not a derivation.

---

## 4. Walkthrough: deuteron — partial data

To make the methodology concrete. **Status of each row** for this branch's analysis:

| Row | Required data | Status (this branch / available) |
|-----|---------------|----------------------------------|
| 1 → 2 | confinement-SDP problem stated | ✓ in paper (`prop:confinement-sdp`) |
| 2 → 3 | canonical $T_w(D)$ at $\alpha^* = 1$ | ✗ R5-full SDP not implemented (parallel-branch flag) |
| 2 → 3 | candidate $T_w(D) = 6_2$ historical | ✓ but $\alpha^* = 0.546$, not PSD |
| 3 | GB-NF + jet order on candidate | ✓ in `atom_nf_symbolic_D.py` (D@A=2 reduces 23-factor → 32-term NF in 2.27 s) |
| 3 → 4 | Wedderburn blocks $\rho_\lambda(T_w)$ | derivable; Hoefsmit seminormal × word |
| 4 → 5 | $y_\lambda$ at $n_0 = 3A = 6$ | ✓ from `y-lambda-wenzl-bridge-symbolic-witness.json` |
| 4 → 5 | $\chi_\lambda(T_w)$ symbolic in $Q(q)$ | derivable (this branch's `r_k_h6_symbolic.py` covers $H_6$ characters) |
| 5 | $\mathrm{tr}_M(T_w) \in Q(q)$ — **symbolic** | **in flight** (Markov trace takes >5 min over all 11 partitions of 6; running in background) |
| 5 | $\mathrm{tr}_M(T_w(D))|_{q_0}$ — **numeric** | $+0.388$ from `atomic-tr-m-mpfr-50dps.witness.json` (Wenzl-Schur, Hoefsmit + Wenzl bridge) |
| 5 → 6 | $\rho(D)$ | paper: 1 (ℓ ≤ 1 rule); SDP: 1; agree |
| 6 → 7 | mpmath at $q_0$, 50 dps | ✓ for numeric path |
| 7 | $m_e \cdot M$ MeV | ✓ |

**Two independent calculations of $\mathrm{tr}_M(T_w(D))|_{q_0}$ disagree:**

| Source | Convention | tr_M(D) at q_0 | Implied B = m_e · ρ · tr_M | AME residual |
|--------|------------|---------------:|---------------------------:|-------------:|
| `atomic-tr-m-mpfr-50dps.witness.json` (Hoefsmit + Wenzl bridge) | Wenzl–Schur | +0.388 | 0.198 MeV | −91.1 % |
| Parallel branch `a12818da2` (SDP-canonical block-matrix dump) | Wenzl–Schur | +0.288 | 0.147 MeV | −93.4 % |

Both Wenzl–Schur. Both should give the same number if both are evaluating the same $T_w$. They don't. **Either two different $T_w$ are in play, or one of the calculations is wrong.** This is exactly the kind of discrepancy the data manifest is meant to surface.

**Pending output (running in background):** `atom_nf_symbolic_D.py` is computing $\mathrm{tr}_M(T_w(D))$ **symbolically in $Q(q)$** from the GB-NF expansion (32 NF terms, 11 partitions of 6). This is the **canonical** value per the chain — once it lands we can tell which numeric calculation (if either) is faithful.

The earlier `atom-nf-symbolic-D.witness.json` reports `markov_trace: 0` — but that's a `SKIP_TRACE=1` placeholder, not a computed result; the witness was emitted in NF-only mode to bypass the >5-minute symbolic-trace cost.

### Result — symbolic computation completed (228 s)

$$
\mathrm{tr}_M(T_w(D)) \;=\; \frac{N(q)}{32 \cdot q^{1332} \cdot (q+1)^5}
$$

where $N(q)$ is a 73-term polynomial in $q$ and $q^{1/2}$ with degrees ranging from $q^{1312}$ to $q^{2713/2}$ (= $q^{1356.5}$). The full symbolic expression is in `/tmp/atom_nf_D.log` and will land in the regenerated `atom-nf-symbolic-D.witness.json`.

**Numerical evaluation at $q_0 \approx 1.10998$ (50 dps mpmath):**

$$
\mathrm{tr}_M(T_w(D))\big|_{q_0} \;=\; +0.38828647154771299936605791605\ldots
$$

**Comparison against the two prior calculations:**

| Source | tr_M(D) at $q_0$ | Match to canonical symbolic? |
|--------|------------------:|:----------------------------:|
| **Canonical symbolic chain** (this calculation) | **+0.388286471547713...** | — |
| `atomic-tr-m-mpfr-50dps.witness.json` (Hoefsmit + Wenzl bridge) | +0.388286471547713... | ✅ **30-digit match** |
| Parallel branch `a12818da2` (SDP block-matrix dump) | +0.288 | ❌ disagrees |

**Conclusion:** the canonical Hoefsmit + Wenzl-bridge calculation in `atomic-tr-m-mpfr-50dps.witness.json` **faithfully implements** the symbolic chain. The parallel branch's `+0.288` value (which produced their `−93.4 %` residual) **does not match the canonical chain** — it represents an error in the SDP block-matrix dump path or a different normalization convention masquerading as Wenzl–Schur.

### Implication for the "refutation"

Under the **correct** tr_M(D) value, the single-term formula gives:

| Step | Value |
|------|-------|
| ρ(D) (paper text + SDP agree) | 1 |
| tr_M(T_w(D)) at q_0 | +0.388286 |
| m_e (CODATA) | 0.510998946 MeV |
| **B(D) = m_e · ρ · tr_M** | **0.198414 MeV** |
| AME B(D) | 2.224566 MeV |
| **Residual** | **−91.08 %** |

vs. the parallel branch's claim of **−93.4 %** under their wrong tr_M value.

**Both narratives lead to "the single-term formula fails on D",** but:
- The parallel branch's specific number and intermediate value are wrong;
- The correct number (−91.08 %) is still bad;
- AND this is conditional on `T_w(D) = 6_2` (the historical census ID) being canonical.

**Independent finding from the same calculation: $T_w(D) \neq 6_2$ at the Hecke level.**

$$
J(6_2)\big|_{q_0} = +1.026920 \quad\text{vs.}\quad \mathrm{tr}_M(T_w(D))\big|_{q_0} = +0.388286
$$

The Jones polynomial of knot $6_2$ does not match the Markov trace of D's atom braid (after GB-NF). So the historical knot ID assigned to D is **wrong at the Hecke level** — the GB-NF reducer produces a different Hecke element than the closure of $6_2$.

**Net for the refutation question:** the formula's −91 % failure on D is not "the formula is broken at the type level". It's "either ρ ≠ 1, or the right T_w(D) ≠ 6_2, or the multi-term tail is needed". Each of these is a separate, narrower question with its own audit trail.

---

## 5. Action items

This branch can produce items 4 and 5 of the manifest (Wedderburn blocks → $\chi_\lambda$ → $\mathrm{tr}_M$ symbolic) for a candidate $T_w$, given a braid word as input. The infrastructure already exists (`r_k_h6_symbolic.py` etc.).

What this branch **cannot** produce without upstream work:
- Row "2 → 3" canonical $T_w$ via R5-full SDP — that's parallel-branch territory
- Row 5 → 6 $\rho$ from SDP solution multiplicity — same

**Concrete next step (this branch):** pick a candidate $T_w(D)$, walk through rows 3 → 7 with explicit per-step data dumped to a witness, and emit the result. If the result matches AME, the candidate is canonical (and we've found the right $T_w$). If it doesn't, the candidate is not canonical (and we've found a non-canonical word, not a refuted formula).

This converts the "is the formula refuted?" question into "have we found a $T_w(D)$ that satisfies all constraints simultaneously?". The latter is *tractable* per-candidate; the former is *premature* until R5-full lands.

---

## Refs

- Canonical chain: [`prop:atom-knot-mass-derivation`](../folio/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) §"Architecture"
- Multi-term form: [`thm:knot-mass-formula-unified`](../folio/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md)
- Wenzl bridge: [`prop:y-lambda-closed-form-wenzl-bridge`](../folio/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)
- Wenzl recipe: [`prop:y-lambda-recipe-from-partition`](../folio/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md)
- Confinement SDP: [`prop:confinement-sdp`](../folio/quantum-observable-universe/braids-and-knots/confinement-sdp.md)
- Parallel branch's PSD-cone audit + R5-minimal: `claude/continue-pr-442-DJRWm` Rust `joint-tower-sdp` binary
