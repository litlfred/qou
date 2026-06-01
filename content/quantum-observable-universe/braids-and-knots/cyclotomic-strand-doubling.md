**Proposition (Cyclotomic doubling identity).**
*Let $\Phi_n(X) \in \mathbb{Z}[X]$ denote the $n$-th cyclotomic
polynomial. Then over $\mathbb{Z}[X]$:*

$$
  \Phi_8(X) \;=\; \Phi_4(X^2),
$$

*equivalently, $X^4 + 1 = (X^2 + 1) \circ X^2$ where $\circ$ denotes
polynomial composition.*

## Proof

By direct evaluation, $\Phi_4(X) = X^2 + 1$ and
$\Phi_8(X) = X^4 + 1$. Composing $\Phi_4$ with $X^2$ gives
$(X^2)^2 + 1 = X^4 + 1 = \Phi_8(X)$. ∎

## Empirical context (Habiro element of nucleon-binding pairs)

The factor $\Phi_8^2 = (X^4 + 1)^2$ appears as a cyclotomic
prefactor in the $\sum_m \Delta a_m(X - Y) \cdot (u; u)_m$ Habiro
element for every atomic-step pair tested:

| Pair (atomic step) | Cyclotomic prefactor observed |
|---|---|
| $(\mathfrak{D} - \mathfrak{n})$, $A=1 \to 2$ | $\Phi_8^2$ |
| $({}^3\mathrm{He} - \mathfrak{D})$, $A=2 \to 3$ | $\Phi_8^2$ |
| $({}^4\mathrm{He} - {}^3\mathrm{He})$, $A=3 \to 4$ | $\Phi_8^2$ |

The $\Phi_8^2$ factor is **convention-invariant** — it appears in
both the `include_inter=True` habiro-witness convention (used in PR
\#1579) and the Phase~5q canonical convention
$\mathrm{tr}_M(\mathfrak{D}, q) = \tau_p \cdot \tau_n \cdot z(q)$
(verified in [`2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)).

## Categorical interpretation — universal atomic-step cyclotomic

The $\Phi_8^2$ prefactor is **universal across atomic-step pairs**,
not indexed by atomic number via strand doubling. Most likely
algebraic origin: the $z(q)^k$ interface factor present in the
Phase~5q closed forms
$$
  \mathrm{tr}_M(X, q) \;=\; \tau_p^Z \cdot \tau_n^N \cdot z(q)^k \cdot (\text{interface corrections}),
$$
where $z(q) = 1/(\sqrt{q} + 1/\sqrt{q}) = u/(u^2 + 1)$ in the
$u = \sqrt{q}$ Habiro variable. The denominator $\Phi_4(u) = u^2 + 1$
of $z(q)$, squared by the universal $z(q)^2$ presence in
atomic-step formulas, propagates through the Pochhammer-division
Habiro extraction and surfaces as $\Phi_8(u) = \Phi_4(u^2)$ via the
algebraic identity proved here.

The mechanism details are under active investigation; see the
falsification + mechanism audits:

- [Strand-doubling FALSIFIED (2026-06-01)](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
- [Phase~5q convention test — $\Phi_8^2$ survives](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)

## Historical note — strand-doubling interpretation refuted

An earlier (2026-06-01) interpretation conjectured that the
substitution $X \mapsto X^2$ is a **strand-doubling map** lifting
$B_2$-representations (single nucleon, $\Phi_4$ denominator) to
$B_4$-representations (deuteron, $\Phi_8$ factor), and predicted a
powers-of-two cyclotomic tower:

$$
  (\mathrm{atom}_{A=k+1} - \mathrm{atom}_{A=k}) \;\rightsquigarrow\; \Phi_{2^{k+1}}(X) \;=\; \Phi_{2^k}(X^2)
  \qquad \text{(REFUTED)}.
$$

Direct test on the canonical Phase~5q ${}^3\mathrm{He}$ and
${}^4\mathrm{He}$ Habiro coefficients showed that
$({}^3\mathrm{He} - \mathfrak{D})$ does **not** carry $\Phi_{16}$
and $({}^4\mathrm{He} - {}^3\mathrm{He})$ does **not** carry
$\Phi_{32}$; both carry $\Phi_8^2$ like the deuteron pair. The
strand-doubling categorical hypothesis is therefore false. The
*algebraic* identity $\Phi_8(X) = \Phi_4(X^2)$ remains true and
useful — what's wrong is the categorical content attached to it.

The corresponding Lean lemma
[`cyclotomic_8_eq_cyclotomic_4_comp_X_sq`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean)
remains valid as a pure algebraic identity over $\mathbb{Z}[X]$.
