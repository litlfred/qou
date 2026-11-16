## Statement

> **Scope note (2026-11-15).** The single-generator piece was labelled "proved" and is not: its form and the scale $\alpha$ are chosen so that the result matches the mass table, and the $0.18\%$ mean error is a fit diagnostic, not a derivation. Only the leading-order piece is an identity. The empirical accuracy figure is a comparison, not part of the claim, and is recorded in [the accuracy remark](#rem:rho-k-graded-expansion-accuracy).


We expose the graded expansion of the categorical density $\rho_K$ by multiplying the GB-NF identity ([atomic mass via GB-NF](#prop:atomic-mass-gb-nf)) $\mathfrak{m}(K) = m_e \cdot \rho_K \cdot |\!\mathrm{tr}_M(\mathrm{NF}_{\mathrm{GS}}(\mathcal{B}_K))|$ through by $m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)|$:

$$
  \boxed{
  \begin{aligned}
    m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K
    \;=\;&
    \underbrace{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece (Markov mult.)}}
    \\[4pt]
    &+\; \underbrace{\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)}_{\rho_K^{\text{single-gen}}\text{-piece}}
    \\[4pt]
    &+\; \underbrace{\tfrac{\alpha\, z^2}{2}\!\!\sum_{i<j}\!\ln\bigl(\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}}\bigr)\!\big|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{-piece (open)}}
    \;+\; \dots
  \end{aligned}
  }
$$

where $\alpha = m_e \cdot 8G$ ([binding scale](#conj:binding-scale-catalan)) and $z = q^{3}/(q^{2}+1)$ forms the Markov parameter (**convention D**). Its comparison with measured masses is recorded in [the accuracy remark](#rem:rho-k-graded-expansion-accuracy).

## Proof

The graded expansion splits into three pieces.

### Leading-order piece (proved)

By [Wenzl 1988] Theorem 5 (Markov multiplicativity), disjoint braids $\beta_1 \in H_{n_1}(q)$ and $\beta_2 \in H_{n_2}(q)$ with image $\beta_1 \otimes \beta_2 \in H_{n_1 + n_2}(q)$ satisfy:

$$
  \mathrm{tr}_M(\beta_1 \otimes \beta_2)
  \;=\; \mathrm{tr}_M(\beta_1) \cdot \mathrm{tr}_M(\beta_2).
$$

Combined with mass additivity for free constituents, this categorically determines the leading-order piece:

$$
  \rho_K^{\mathrm{LO}}
  \;=\;
  \frac{Z m_{\mathfrak{p}} + N m_{\mathfrak{n}} + Z m_e}{m_e \cdot |\!\mathrm{tr}_M(\mathcal{B}_K)|}.
$$

The script `rho-k-markov-multiplicativity.witness.json` numerically verifies the [Wenzl 1988] branching identity $\chi^\lambda(\mathcal{B}_p \otimes \mathcal{B}_n) = \sum c^\lambda_{\mu, \nu} \chi^\mu(\mathcal{B}_p) \chi^\nu(\mathcal{B}_n)$ to machine precision ($3.2 \times 10^{-14}$) for all $\lambda \vdash 6$ in the deuteron case.

### Single-generator piece (fitted)

Per [atomic braid mass](#thm:wedderburn-mass-formula), the per-generator log-volume sum reads:

$$
  \tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)
$$

The overline denotes the Hecke bar-involution $q \leftrightarrow q^{-1}$. At real $q_0$ and real $\hat V_i$, this reduces to the archimedean form $\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|$. Using $\alpha = m_e \cdot 8G \approx 3.7445$ MeV (the Borromean binding scale, [Catalan binding](#conj:binding-scale-catalan)), this captures the leading binding correction. The mean error is $0.18\%$, with a $0.35\%$ maximum across $Z = 1..20$ (see `atomic-braid-mass-paper-formula.witness.json` and the `rho-k-pair-gen-extension.witness.json` table).

### Pair-generator piece (open)

The pair-generator term provides the log-volume analogue of $T_3 = -z^2 \sum_{i<j} \mathrm{Li}_2^q(-|\hat V_i \hat V_j|)$ from the [unified knot mass formula](#thm:knot-mass-formula-unified):

$$
  \alpha \cdot z^2 \cdot \sum_{i<j} \ln\bigl|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}\bigr|_{\mathrm{Wedderburn}}.
$$


$$
  \bigl|\hat V_i \hat V_j\bigr|_{\mathrm{Wedderburn}}
  \;=\;
  w_{\mathrm{sym}}\, \lambda_i^{\mathrm{sym}} \lambda_j^{\mathrm{sym}}
  + w_{\mathrm{std}}\, \bigl[\,z\,(M_i M_j)_{1,2} + (M_i M_j)_{2,2}\bigr]
  + w_{\mathrm{alt}}\, \lambda_i^{\mathrm{alt}} \lambda_j^{\mathrm{alt}}
$$

Here, $M_i$ provides the per-generator $2 \times 2$ standard-representation transfer matrix, and $w_\bullet$ are the Wedderburn-Markov weights from [Wedderburn mass](#thm:wedderburn-mass-formula). The standard-channel pair coupling uses the Markov-traced $2 \times 2$ matrix product $M_i M_j$ to capture braid non-commutativity, avoiding the naive product $V_i^{\mathrm{std}} \cdot V_j^{\mathrm{std}}$.

See [Table 1](#tbl:rho-k-graded-expansion-table1-data).

Both pair extensions degrade accuracy under the simple $\alpha z^2$ log-formula, even with the correct Wedderburn coupling. The gap lies in the functional form: $T_3$ in the six-term theorem requires $-z^2 \sum \mathrm{Li}_2^q(-|V_i V_j|)$, not $\alpha z^2 \sum \ln |V_i V_j|$. The single-generator Kashaev-limit derivation that yields $\alpha \sum \ln|V_i|$ (matching $T_2$) requires a parallel derivation for the pair piece to produce the correct functional form and prefactor. This remains open work.

## Identification with the six-term theorem

Each piece of the graded expansion corresponds to a term in the Kashaev limit of the [unified knot mass formula](#thm:knot-mass-formula-unified) (six-term theorem):

See [Table 2](#tbl:rho-k-graded-expansion-table2-data).

The graded $\rho_K$ expansion supplies the Kashaev specialisation of the six-term theorem (`thm:knot-mass-formula-unified`) expressed at the GB-NF level. The constituent-mass piece is explicitly factored out via the Markov-multiplicativity rewriting.

## References

- [Wenzl 1988] *Hecke algebras of type $A_n$ and subfactors*, Inventiones Math. **92**, 349–383. Theorem 5 (Markov multiplicativity for parabolic subalgebras).
