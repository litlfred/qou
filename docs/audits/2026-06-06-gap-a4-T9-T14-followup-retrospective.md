# GAP-A-4 functor-search follow-up: T9–T14 — 3 more refutations, q-modular direction structurally mismatched

**Date:** 2026-06-06
**Branches:** `claude/gap-a4-T4-schur-weyl-icosahedral-probe-2026-06-05`
(PR #1904 — merged) + `claude/gap-a4-T13-T14-q-icosahedral-2026-06-06`
(PR #1922 — in flight).
**Scope:** Follow-up to [2026-06-06 T4–T8 retrospective](2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md).
After T4–T8 closed the standard quantum-group / Schur-Weyl directions
and T9 scaffolded the non-Schur-Weyl alternatives (McKay-E_8 / Klein-J /
Bring), T10–T14 implemented the natural follow-up candidates.  All
three were REFUTED; the cumulative finding extends to: **all q-modular
/ icosahedral-algebraic routes are structurally mismatched to the
polynomial Borromean h⁴ = −3/4.**

---

## VERDICT (one line)

**8 candidate cross-algebra functors have now been REFUTED (T4–T14).
The Borromean h⁴ = −3/4 obstruction stays structurally OPEN.  The
remaining search space must point AWAY from both Schur-Weyl
representation theory AND q-modular forms — likely toward
non-modular polynomial-side mechanisms or genuinely new categorical
objects.**

---

## Cumulative T4–T14 verdicts

| # | Probe | PR | Candidate | Verdict |
|---|---|---|---|---|
| 1 | T5 F1 | #1904 | Young's branching Res^{S_5}_{S_3} | REFUTED |
| 2 | T5 F2 | #1904 | dim_q ratio 2·[5]_q / [3]_q | REFUTED |
| 3 | T5 F3 | #1904 | Wenzl-weight ratio at q=1 | REFUTED |
| 4 | T7 | #1904 | Bratteli/Markov stabilization | REFUTED |
| 5 | T8 | #1904 | RT / q-Schur duality (sl_2, sl_3) | REFUTED |
| 6 | T10 | #1904 | McKay-character spin-lift (2I) | REFUTED |
| 7 | **T13** | #1922 | **q-Eisenstein E_4, E_6** | **REFUTED** |
| 8 | **T14** | #1922 | **q-Hermite icosahedral resolvent** | **REFUTED** |

Plus three scaffolds that PINNED the classical structures without
proposing a derivation (per formalize-first discipline):
- T6: q-deformed icosahedral character matrix — Clifford excess identity
  derived; H-sector closed form Q_H(q) = 2·[5]_q = 10 + 10h² + 2h⁴
- T9: McKay E_8 / Klein degree triple (12, 20, 30) / Burnside checks
- T11: Klein invariants f, H, T; syzygy 1728·f^5 = T² + H³; J orbit
  values 0/1/∞; Riemann-Hurwitz 118 = 48 + 40 + 30
- T12: Brioschi-form discriminant 256·b^5 + 3125·c^4 verified; Bring
  form Δ = 800000 + 3125·α^4

---

## T13 q-Eisenstein — REFUTED at expansion-point level

The classical Eisenstein series (weight 2k, k ≥ 1) is

$$
  E_{2k}(q) = 1 - \frac{4k}{B_{2k}} \sum_{n \geq 1} \sigma_{2k-1}(n) \cdot q^n.
$$

Key facts:
- The ring of modular forms for $\mathrm{SL}_2(\mathbb{Z})$ is
  $\mathbb{C}[E_4, E_6]$.
- Convention note: T11 uses the Klein modular invariant
  $J = 1728 \cdot E_4^3 / (E_4^3 - E_6^2)$ whose orbit values are
  $\{0, 1, \infty\}$ under the icosahedral syzygy.  The modular
  $j$-invariant ($j(\tau) = 1/q + 744 + \cdots$) equals this $J$ via
  the standard normalisation.  Gemini's review (#1925) flags that an
  alternative convention writes $J = E_4^3 / (E_4^3 - E_6^2)$ (without
  the 1728) and $j = 1728 \cdot J$; that is a valid alternative
  normalisation but T11's choice is fixed for orbit-value consistency.
- The modular discriminant is $\Delta(q) = (E_4^3 - E_6^2) / 1728$.

**Obstruction.** Both $E_4(q)$ and $E_6(q)$ DIVERGE as $q \to 1^-$ along
the real axis.  (Technically the cusp of $\mathrm{SL}_2(\mathbb{Z})$ is
at $\tau \to i\infty \Leftrightarrow q = e^{2\pi i \tau} \to 0$; the
divergence we are looking at is on the boundary $|q| = 1$, at the
boundary point $q = 1$, which is NOT a cusp in the SL_2 sense but is
where the q-series fails to converge.)  Since $q = 1$ is the natural
$h = 0$ base point for the Borromean polynomial reference, there is
no finite Taylor h-coefficient of $E_4$ or $E_6$ comparable to the
$h^4 = -3/4$ coefficient of $\mathrm{tr}_M(\beta_\mathrm{Bor})$.

The icosahedral q-Eisenstein analogue (pullback through the icosahedral
covering $\mathbb{CP}^1 \to \mathbb{CP}^1 / I$) inherits the same
obstruction: the icosahedral modular discriminant $\Delta_I$, being a
polynomial in $E_4$ and $E_6$, also diverges as $q \to 1^-$.

**Verdict: REFUTED.**  7th candidate cross-algebra functor refuted.
Numerical sanity: $E_4(0.901) \approx 1.28 \times 10^7$, $E_6(0.901)
\approx -4.04 \times 10^{10}$, finite far from $q = 1$.

---

## T14 q-Hermite icosahedral resolvent — REFUTED by inheritance

The classical Hermite resolvent (1858) expresses the roots of the
Bring quintic $y^5 + 5y + \alpha = 0$ as rational functions of the
Klein invariants and the modular discriminant:

$$
  y(\alpha) = R(f, H, T, \Delta; \alpha),
$$

where $R$ is a rational function and $\Delta = (E_4^3 - E_6^2) / 1728$
is the SL_2(ℤ) modular discriminant.

**Inheritance.** Per T13, $\Delta(q)$ diverges at $q = 1$.  Therefore
any rational function of $\Delta$ (and the Klein invariants $f, H, T$
which are well-behaved as $q \to 1^-$) inherits the divergence at $h = 0$.

**Classical verification.** At $\alpha = 1$, the real root of
$y^5 + 5y + 1 = 0$ is computed to 40-digit precision via
`mpmath.polyroots`; residual at root $|y^5 + 5y + \alpha| < 10^{-40}$.
The Bring discriminant $\Delta_\mathrm{Bring}(\alpha=1) = 803125 \neq 0$
confirms non-degeneracy.

**Verdict: REFUTED at expansion-point level.**  8th candidate
cross-algebra functor refuted by inheritance from T13.

---

## Structural conclusion (the actionable finding)

> **All q-modular / icosahedral-algebraic routes that pull back through
> $q = 1$ as the $h = 0$ base point share the same $q \to 1^-$
> boundary-divergence obstruction.**
>
> The Borromean $h^4 = -3/4$ is a POLYNOMIAL coefficient of
> $\mathrm{tr}_M(\beta_\mathrm{Bor}) = (4 + h^2 - 3h^4 - h^6) / (h^2 + 4)$,
> NOT a transcendental q-series coefficient.  So the entire q-modular-form
> direction is STRUCTURALLY MISMATCHED to the $h^4$ obstruction.

This complements the T4–T8 conclusion (icosahedral H is non-Schur-Weyl):
neither standard rep theory NOR q-modular forms reach the obstruction.

---

## What's left in the search space

After T4–T14, the remaining open candidate functor directions are
constrained by the negative space the 8 refutations have carved out:

1. **Polynomial-side mechanisms.**  The Borromean reference IS a
   polynomial in $h$ (and a rational function in $q$).  Any mechanism
   linking the 5-strand A_5 fiber to the 3-strand H_3 trace must produce
   a polynomial relation, not a q-series expansion.  Candidates:
   - Direct polynomial identities involving the Klein invariants $f, H, T$
     (NOT their q-Eisenstein expansion).
   - Algebraic varieties (e.g. the Bring quintic itself as an affine
     variety in $\mathbb{C}^5$) — NOT viewed as modular curves.

2. **Combinatorial bijections without q-deformation.**  The
   Borromean $h^4$ coefficient is rational; bijections at the level of
   tableaux / standard Young tableaux / icosahedral orbit centers
   could produce $-3/4$ as a counting-type identity.

3. **Genuinely new categorical objects.**  Something neither in the
   Schur-Weyl tower NOR in the q-modular form tower — a possibility
   that T4–T14's negative space leaves on the table.

Per CLAUDE.md "no 7th ansatz" / formalize-first discipline, **no
specific candidate is proposed here**.  The pursuit of any of (1)-(3)
would be a separate, carefully-scoped follow-up.

---

## Cross-references

- T4–T8 retrospective (predecessor):
  [`2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md`](2026-06-06-gap-a4-T4-T8-functor-search-retrospective.md)
- 2026-06-01 audit (original missing-functor identification):
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)
- 2026-06-05 final retrospective (predecessor):
  [`2026-06-05-gap-a4-final-retrospective.md`](2026-06-05-gap-a4-final-retrospective.md)
- Borromean H_3 trace closed form (h⁴ = −3/4 source):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md)
- The SAME missing object on K_1 (inter-nucleon-color-tube):
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)
- Probes:
  - T10 [McKay-character / spin-lift](../../computations/probes/gap_a4_T10_mckay_character_2I_probe.py) (#1904, merged)
  - T11 [Klein J-invariant](../../computations/probes/gap_a4_T11_klein_J_invariant_probe.py) (#1904, merged)
  - T12 [Bring discriminant](../../computations/probes/gap_a4_T12_bring_discriminant_scaffold_probe.py) (#1904, merged)
  - T13 [q-Eisenstein](../../computations/probes/gap_a4_T13_q_eisenstein_probe.py) (#1922, in flight)
  - T14 [q-Hermite resolvent](../../computations/probes/gap_a4_T14_q_hermite_resolvent_probe.py) (#1922, in flight)
