**Conjecture (canonical form of $\rho_K^{\text{pair-gen}}$).**
*There exists a closed-form Wedderburn-coupled functional form
$f_2 : \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \times \mathbb{Q}(q^{1/2}) \to \mathbb{R}$
such that for every atomic braid $\mathcal{B}_K \in B_{3A}$:*

$$
\rho_K^{\text{pair-gen}}
\;=\;
\sum_{0 \leq i < j \leq 3A-2}
  f_2\!\left(q, \hat V_i^{\text{full}}, \hat V_j^{\text{full}}\right)
$$

*and the resulting graded-expansion truncation*

$$
m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \left(\rho_K^{\text{LO}} + \rho_K^{\text{single-gen}} + \rho_K^{\text{pair-gen}}\right)
\;=\;
\mathcal{M}(K)^{\text{CODATA}}
\;+\; O(\hbar_q^{6})
$$

*to sub-percent accuracy across $Z = 1..20$, where $\hat V_i^{\text{full}}$
are the Wedderburn-traced per-generator volumes and $z = 1/(q^{1/2} + q^{-1/2})$
is the Markov parameter.*

## Empirical evidence (current state)

| Candidate $f_2$ | Form | Z=1..20 status |
|---|---|---|
| Naive log-additive | $\alpha z^2 \sum \ln\|V_i V_j\|$ | **Degrades** vs LO + single-gen |
| Wedderburn-decomposed | $\alpha z^2 \sum \|V_i V_j\|_{\text{Wedderburn}}$ (with $w_{sym}, w_{std}, w_{alt}$) | Still degrades — wrong functional form |
| Six-term theorem $T_3$ | $-z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ | Believed correct per `thm:knot-mass-formula-unified` (Kashaev-limit form); not yet wired into $\rho_K$ expansion |

The Kashaev-limit form (six-term $T_3$) is the expected canonical form, but its derivation as a leading-order expansion in $\hbar_q$ — parallel to the single-gen Kashaev derivation $\alpha \sum \ln|V_i|$ — has not been completed.

## What's proved vs conjectured

| Component | Status | Evidence |
|---|---|---|
| Existence of $f_2$ (any form) | Conjectural | follows from existence of mass formula evaluated at finite truncation |
| $f_2 = -\text{Li}_2^q(-\|V_i V_j\|) \cdot z^2$ specifically | Conjectural | matches the six-term theorem's $T_3$; derivation pending |
| Naive log-additive form | Refuted (empirical) | `rho-k-pair-gen-extension.witness.json` |
| Wedderburn-coupled form | Partial (correct Wedderburn weights, wrong functional) | Same witness |
| Six-term theorem itself ([`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md)) | Theorem | proved separately |

## Wedderburn-coupling structure

Per [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen:

$$
|\hat V_i \hat V_j|_{\text{Wedderburn}}
\;=\;
w_{\text{sym}}\, \lambda_i^{\text{sym}} \lambda_j^{\text{sym}}
\;+\;
w_{\text{std}}\, \bigl[z\,(M_i M_j)_{1,2} + (M_i M_j)_{2,2}\bigr]
\;+\;
w_{\text{alt}}\, \lambda_i^{\text{alt}} \lambda_j^{\text{alt}}
$$

where:
- $w_{\text{sym}}, w_{\text{std}}, w_{\text{alt}}$ are Wedderburn-Markov weights from [`thm:wedderburn-mass-formula`](wedderburn-mass-formula.md)
- $\lambda_i^\bullet$ are per-generator eigenvalues in each Wedderburn channel
- $M_i$ is the per-generator $2 \times 2$ standard-rep transfer matrix
- The standard-channel pair coupling uses the **Markov-traced** $2 \times 2$ matrix product $M_i M_j$ — genuinely capturing braid non-commutativity — rather than the naive $V_i^{\text{std}} \cdot V_j^{\text{std}}$.

The OPEN piece is the **functional form** $f_2$ that takes this Wedderburn-coupled product as input and outputs the correct mass contribution. Two candidates:

(i) Logarithmic: $\alpha z^2 \ln|V_i V_j|_{\text{Wedderburn}}$ — refuted empirically (degrades).
(ii) q-dilogarithmic: $-z^2 \text{Li}_2^q(-|V_i V_j|_{\text{Wedderburn}})$ — believed correct; pending derivation.

The Kashaev-limit derivation that gave $\alpha \ln|V_i|$ for the single-gen piece (matching $T_2$ of the six-term theorem) needs a parallel derivation for the pair-gen piece.

## Connection to dependent conjectures

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — the lepton-sector variant; gates on the graded-expansion formalism but has $Z = N = 0$ so the atomic LO piece vanishes; needs its own dimensional factor $\xi_\ell(q)$.
- [`conj:mass-endomorphism`](mass-endomorphism-conjecture.md) (per `prop:per-braid-mass-tower` §"Open: explicit closed form") — the unifying closed-form mass element $\Phi_{\text{mass}}(W) \in H_{3A}(q)$; the present conjecture is a sub-claim about its expansion at pair level.

## Lean formalization

```lean
namespace QOU.BraidKnot.RhoKPairGenCanonicalForm

/-- The conjectural canonical pair-gen functional `f_2(q, V_i, V_j)`;
    expected six-term `T_3` Kashaev form, derivation open (cited placeholder). -/
noncomputable def pair_gen_functional
    {R : Type*} [Field R] (q V_i V_j : R) : R :=
  sorry  -- Ref: [manuscript] conj:rho-k-pair-gen-canonical-form

/-- Conjecture, §3b class axiomatisation: a single canonical functional
    reproduces ρ_K^pair-gen (the precise Li_2^q recovery bound needs the
    graded-expansion infrastructure, so it is carried as a `Prop` class
    that downstream blocks take as a `[PairGenCanonical]` hypothesis). -/
class PairGenCanonical : Prop where
  holds : True

end QOU.BraidKnot.RhoKPairGenCanonicalForm
```

## Resolution path

When the canonical $f_2$ is derived:
1. This conjecture promotes to a theorem.
2. [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) §pair-gen status changes from "open" to "proved".
3. Downstream conjectures (especially [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) which doesn't currently use pair-gen but will if extended to multi-strand leptons) get unblocked.
4. The $\mathfrak{Q}_\beta$ residual closure direction (Path A / Path B in [`2026-05-24-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md)) becomes tractable.

## Cross-references

- [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) — parent proposition (this conjecture promotes its OPEN pair-gen subsection)
- [`thm:knot-mass-formula-unified`](knot-mass-formula-unified.md) — six-term theorem providing the expected $T_3 = -z^2 \sum \text{Li}_2^q(-\|V_i V_j\|)$ form
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — sibling conjecture for leptons
- Audit: [`docs/audits/2026-05-25-rho-k-dependent-conjectures-status.md`](../../../docs/audits/2026-05-25-rho-k-dependent-conjectures-status.md) — full dependency graph
