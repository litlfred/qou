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

## 4. Walkthrough: deuteron

To make the methodology concrete. **Status of each row** for this branch's analysis:

| Row | Required data | Status (this branch / available) |
|-----|---------------|----------------------------------|
| 1 → 2 | confinement-SDP problem stated | ✓ in paper (`prop:confinement-sdp`) |
| 2 → 3 | canonical $T_w(D)$ at $\alpha^* = 1$ | ✗ R5-full SDP not implemented (parallel-branch flag) |
| 2 → 3 | candidate $T_w(D) = 6_2$ historical | ✓ but $\alpha^* = 0.546$, not PSD |
| 3 | GB-NF + jet order on candidate | partial — parallel branch has Rust `gb_nf_reducer` |
| 3 → 4 | Wedderburn blocks $\rho_\lambda(6_2)$ | derivable; Hoefsmit seminormal × word |
| 4 → 5 | $y_\lambda$ at $n_0 = 3A = 6$ | ✓ from `y-lambda-wenzl-bridge-symbolic-witness.json` |
| 4 → 5 | $\chi_\lambda(6_2)$ symbolic in $Q(q)$ | derivable (this branch's `r_k_h6_symbolic.py` covers $H_6$ characters) |
| 5 | $\mathrm{tr}_M(6_2) \in Q(q)$ | derivable from above |
| 5 → 6 | $\rho(D)$ | paper: 1 (ℓ ≤ 1 rule); SDP: 1; agree |
| 6 → 7 | mpmath at $q_0$, 50 dps | this branch's $r_k_h{5,6,7}$ infrastructure handles this |
| 7 | $m_e \cdot M$ MeV | ✓ |

**What's missing for a faithful test of `prop:atom-knot-mass-derivation` on D**: row "2 → 3" — the canonical $T_w(D)$ from R5-full SDP. Without that, the test uses a non-canonical $T_w$ and the −93.4 % residual is at most a falsification of "$T_w(D) = 6_2$ is canonical", not a falsification of the formula itself.

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

- Canonical chain: [`prop:atom-knot-mass-derivation`](../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) §"Architecture"
- Multi-term form: [`thm:knot-mass-formula-unified`](../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md)
- Wenzl bridge: [`prop:y-lambda-closed-form-wenzl-bridge`](../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)
- Wenzl recipe: [`prop:y-lambda-recipe-from-partition`](../content/quantum-observable-universe/braids-and-knots/y-lambda-recipe-from-partition.md)
- Confinement SDP: [`prop:confinement-sdp`](../content/quantum-observable-universe/braids-and-knots/confinement-sdp.md)
- Parallel branch's PSD-cone audit + R5-minimal: `claude/continue-pr-442-DJRWm` Rust `joint-tower-sdp` binary
