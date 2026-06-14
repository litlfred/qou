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
not indexed by atomic number via strand doubling. The categorical
mechanism is **OPEN** — neither of the two naive candidates explains it:

- **Not $z(q)^k$ interface.** Direct Habiro expansion of $z(q)^k$
  alone produces a pure monomial $u^k$ with no cyclotomic factor;
  the $\Phi_4(u) = u^2 + 1$ denominator of $z(q) = u/(u^2 + 1)$ clears
  into the normalisation prefactor.
- **Not the Pochhammer boundary.** The earliest mechanical Pochhammer
  contribution of $\Phi_8$ is at $m = 8$ via $(u; u)_8 \ni 1 - u^8$;
  the earliest mechanical $\Phi_8^2$ is at $m = 16$. But the observed
  $\Delta a_m$ partial sums acquire $\Phi_8$ already at $M = 7$
  (before $m = 8$) and $\Phi_8^2$ at $M = 12$ for $(\mathfrak{D} - \mathfrak{n})$
  or $M = 15$ for the helium pairs — strictly before the mechanical
  Pochhammer boundary.

The pre-$m{=}8$ $\Phi_8$ appearance is a **structural $\Delta a_m$
interference signature**: the cyclotomic structure must arise from
algebraic relations among the $a_m$ coefficients themselves, not from
the Pochhammer weighting or the closed-form $z(q)$ factor. The
categorical witness of $\zeta_8 = e^{i\pi/4}$ in the
proton/neutron/deuteron/helium Habiro coefficients is the next
question for investigation.

Cross-references:

- [Strand-doubling FALSIFIED](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md)
- [Phase~5q convention test — $\Phi_8^2$ survives](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md)
- [Mechanism investigation — $z(q)^2$ hypothesis refuted](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)

## Historical note — strand-doubling interpretation refuted

An earlier interpretation conjectured that the
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


**Mathematical Novelty:** The identity itself is a textbook algebraic cyclotomic composition identity ($\Phi_{2n}(X)=\Phi_n(X^2)$). Note that a previous categorical strand-doubling interpretation was refuted, leaving this purely as a standard but necessary foundational lemma with low inherent novelty.