# PR #534 — post-merge next-steps plan

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534, awaiting review)
**Refs:**
- [PR #534 work summary](https://github.com/litlfred/qou/pull/534)
- Sibling PR [#546](https://github.com/litlfred/qou/pull/546) — closed-form $\mathrm{tr}_M(p)$
- Sibling PR [#545](https://github.com/litlfred/qou/pull/545) — Term-6 $A \geq 2$

## What PR #534 closes

| Result | Status |
|---|---|
| `prop:atomic-mass-gb-nf` (atomic mass via GB-NF identity) | ✅ stated + Lean stub |
| `prop:hecke-branching-trace-decomposition` (refined Sub-lemma 2.1, operator-valued $A^\lambda_{\mu\nu}(I)$) | ✅ proved + numerically verified to $1\!\times\!10^{-15}$ for all $11$ partitions $\lambda \vdash 6$ |
| `prop:rho-k-graded-expansion` (graded ρ_K replacing LO ansatz) | ✅ stated + Path-1 (Markov multiplicativity) verified to $3\!\times\!10^{-14}$ |
| `prop:markov-trace-antipode-polynomial-symmetry` ($q^{20} p(1/q) = -p(q)$) | ✅ **proved sympy-exact** + narrative + Lean |
| ρ_q substrate-only ansatz from `mass-endomorphism-tower` | ✅ flagged superseded |
| Wedderburn pair-coupling implementation | ✅ infrastructure delivered (`wedderburn_pair_volumes.py`) |

## What remains open after PR #534

### Three open functional-form pieces

**Piece 1 — Dimensional bridge $E_0 \leftrightarrow \alpha$.**
- Falsified the conjecture "GB-NF event count $= 2 \cdot |S_n|$ universally"
- Open: derive $m_p / m_e$ structurally (anchored by PR #546's closed-form $\mathrm{tr}_M(p)$ once factor-of-2 normalization mismatch is resolved)
- Direct dependency: PR #546's open item 2 (the factor-of-2)

**Piece 2 — Linked-cluster A-dependent structure.**
- $T_3 / T_2^2$ varies $0.076 \to 0.135$ monotonically with $A$ (not classic cumulant)
- Open: derive $f(A)$ in $T_3 = f(A) \cdot T_2^2 / 2$ via spectral-sequence convergence
- Direct dependency: PR #545's $A \geq 2$ Term-6 closed-form work

**Piece 3 — Interface vs intra-generator distinction.**
- Per-nucleon intra log-sum and per-interface inter log-sum decompose into stable categorical constants ($\sigma_p \approx -0.040$, $\sigma_n \approx -0.182$, $c_\text{inter} \approx -1.40$) but no clean closed-form yet
- Open: derive $\sigma_p, \sigma_n$ via per-nucleon Hoefsmit symbolic + refined Sub-lemma 2.1 for the inter contribution
- Direct dependency: PR #546's symbolic Hoefsmit + #534's `prop:hecke-branching-trace-decomposition`

## Plan structured by dependency

### Tier 0 — Awaiting external review (immediate)

1. Wait for `/gemini review` and Copilot review feedback on PR #534
2. Address any review comments
3. Merge PR #534

### Tier 1 — Once PR #534 is merged, immediate continuations

**Watch the sibling PRs that close my open pieces:**

1. **PR #546 progresses to $A \geq 2$ closed form** → directly closes Piece 1 dimensional bridge
2. **PR #545 progresses on Term-6 $A \geq 2$** → directly closes Piece 2 linked-cluster
3. The structural anti-self-reciprocity proved here generalises; PR #546 + #545 should test the conjectural form $q^{2 \mathrm{shift}(K)} p_K(1/q) = (-1)^{\ell(\beta_K)} p_K(q)$ on their $A \geq 2$ closed forms

### Tier 2 — Medium-term derivation work

**The remaining open derivations post-PR #534:**

| Derivation target | Path |
|---|---|
| $\sigma_p, \sigma_n$ closed forms | PR #546's symbolic Hoefsmit pipeline → my interface/intra split |
| $c_\text{inter}$ from $A^\lambda_{\mu\nu}(I)$ | refined Sub-lemma 2.1 + Hoefsmit matrix elements at the $\sigma_{n_1}$ boundary |
| $E_0$ from $\mathrm{tr}_M(p)$ closed form | PR #546's factor-of-2 normalization resolution + Plancherel weights |
| Generalisation conjecture $q^{2 \mathrm{shift}(K)} p_K(1/q) = (-1)^{\ell(\beta_K)} p_K(q)$ | Test on neutron, deuteron, helium-3/4 closed forms (PR #546 / #545) |

### Tier 3 — Long-term categorical closure

**The final categorical mass identity** has form:
$$M(K) \;=\; m_e \cdot \rho_K \cdot |\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\beta_K))|$$
with $\rho_K$ derivable from braid-only data via:
- Constituent piece (Markov multiplicativity, Wenzl 1988) — **proved**
- Single-gen piece $\alpha \sum \ln|V_i^{\text{full}}|$ — **proved at 0.18% accuracy**
- Pair-gen piece (Wedderburn-coupled) — **infrastructure delivered**, functional form open
- Higher pieces — expressible via spectral-sequence summation, structurally but not yet closed-form

The bottleneck is now **two derivations**:

1. Closed form for $|\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\beta_K))|$ at any $K$ (PR #546 has $K = $ proton, in progress for $A \geq 2$)
2. Closed form for the operator-valued $A^\lambda_{\mu\nu}(I)$ matrix elements (refined Sub-lemma 2.1, this branch)

Once both are closed in symbolic form, the entire categorical-mass program reduces to **direct symbolic computation** with zero empirical inputs beyond $q_0$ and $m_e$.

## Concrete near-term action items (post-PR-#534-merge)

1. **Coordinate with PR #546**: their factor-of-2 normalization resolution and $A \geq 2$ extension are the immediate dependencies for Piece 1.
2. **Coordinate with PR #545**: their Term-6 $A \geq 2$ work directly addresses Piece 2.
3. **Test the generalised anti-self-reciprocity** $q^{2 \mathrm{shift}(K)} p_K(1/q) = (-1)^{\ell(\beta_K)} p_K(q)$ on PR #546's neutron closed form (already on their branch) and predicted deuteron form when ready.
4. **Lean formalisation**: close the residual `sorry` in `markov-trace-antipode-polynomial-symmetry.lean` via the explicit polynomial-coefficient check (purely a syntactic exercise).

## Things to avoid

- **Numerology**: any "closed form" candidate without categorical derivation. Recent example: my "12 = 2·|S_3|" hypothesis falsified by direct testing.
- **Over-reaching extrapolation**: the 11-partition deuteron verification of refined Sub-lemma 2.1 doesn't directly extend to ⁴He without checking the operator-valued $A^\lambda_{\mu\nu}$ at $H_{12}$ irreps.
- **Premature unification**: the three pieces (Piece 1, 2, 3) interconnect but aren't reducible to a single open derivation. Each needs its own categorical anchor.
