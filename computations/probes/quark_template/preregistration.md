# Quark template, tracked order by order in the tower: pre-registration

Written and committed **before any number in this directory was computed**.

Owner request, 2026-10-11: *"quarks are intermediary/non-observable objects, so wouldn't live at k=0?, so they should live at next order (or so) of the tower. The γγ prediction needs to track the towers at every step, not just observable. Work on deriving quark template."*

Nothing here is compared with Q_β, CODATA or any mass, and nothing is ranked by accuracy. The selection rule stays open (bean `qou-99qc`). The quark template is currently a declared choice, not a derivation (beans `qou-y2np`, `qou-ales`).

## 0. The object

The canonical nucleons, as `pyhecke.atom.build_nucleon_nf_mp` builds them in H₃(q), are

    proton  P = V³ · L(u,u)₀ · L(u,d)₀ · L(u,d)₁ · G
    neutron N = V³ · L(u,d)₀ · L(u,d)₀ · L(d,d)₁ · G

Here V = σ₀σ₁⁻¹ is the γγ vertex, G = σ₀σ₀ is the gluon dressing, and the subscript is the generator a letter sits on. The pairs are (0,1), (0,2), (1,2), and each sits on the generator with the lower index.

The template is the rule that turns a quark pair into a letter. The corpus uses uu → σ, dd → σ⁻¹, ud → ½(σ + σ⁻¹). Splitting it into two independent pieces makes it testable:

- **(B) a sign map** ε: {u, d} → {+1, −1}. The corpus uses ε_u = +1, ε_d = −1. This is the bar bit of bean `qou-y2np`: u ↔ eigenvalue +q, d ↔ eigenvalue −q⁻¹.
- **(A) a pair rule** combining the two signs. The corpus uses AVG, L(a,b) = ½(σ^{ε_a} + σ^{ε_b}).

Since σ⁻¹ = σ − h with h = q − q⁻¹, a single sign gives σ^ε = σ − (h/2)(1 − ε), and so every letter has the form

    AVG:  L(a,b) = σ + (h/4)(ε_a + ε_b − 2)
    LO:   L(a,b) = σ − (h/2)(1 − ε_a)

so **at order h⁰ every letter is σ, whatever the flavours.** The quark content is invisible at the order-zero (classical, q = 1) level of the tower and first appears at order h¹. This is a two-line identity, and it is the formal content of the owner's remark. It is checked symbolically below (check C2), not assumed.

## 1. The variant family (fixed now)

Sign maps:
- **S+**: u = +1, d = −1 (the corpus)
- **S−**: u = −1, d = +1 (bar-swapped)
- **S0**: all +1
- **S1**: all −1

Pair rules:
- **AVG**: ½(σ^{ε_a} + σ^{ε_b}) (the corpus)
- **LO**: σ^{ε_a}, the sign of the lower-index quark
- **HI**: σ^{ε_b}, the sign of the higher-index quark

Under S0 and S1 the pair rule makes no difference. That leaves 2 + 2×3 = **8 distinct templates per nucleon**.

Gluon dressing:
- **primary**: none (k = 0)
- **secondary**: G = σ₀σ₀, as in the builder

Generator placement is held fixed as in the builder. This is a choice, and it is stated as one. The corpus probe `qbeta_cost_minimal_budget_under_reading3_probe.py` did the complementary thing: template fixed at S+AVG, placement varied (8 words, 4 feasible). A **joint** run (8 templates × 8 placements = 64 per nucleon, k = 0) is reported as a tertiary table, and it must reproduce that probe's 4/8 on its S+AVG row (check C4).

## 2. What is computed (exact, symbolic)

Each variant is evaluated in H₃(q) over ℚ(q), with sympy, as an exact rational function of q. The quantities are:

- χ_(3) and χ_(1³), the one-dimensional characters σ ↦ q and σ ↦ −q⁻¹. Each is a product over the letters.
- χ_(2,1), the trace of the 2-dimensional irreducible ρ₂(σᵢ) = −q⁻¹·Sᵢ(q²), where S is reduced Burau. This is the same representation as `../bring_route2/b3_linear_probe.py`, which checked it against the Hecke relation and the builder.

Reading 3 (owner, 2026-09-12; whole element, 2026-09-13) requires χ_λ ≥ 0 on every block with Markov weight y_λ > 0. Under convention D, y_(1³) = 0, so the test is χ_(3) ≥ 0 and χ_(2,1) ≥ 0. χ_(1³) is recorded but does not enter the verdict.

**Tower tracking.** Put t = q − 1. For every variant, report:

1. the Taylor coefficients of χ_(2,1) and χ_(3) in t, through order t⁶;
2. the **leading nonzero order** of χ_(2,1) and its sign;
3. the sign of each partial sum at q₀ (truncation orders 0 through 6), so that the verdict is visible at every step of the tower and not only at the observable point;
4. the exact sign of χ_(2,1) on the whole interval q ∈ (1, ∞): real roots of its numerator are isolated with sympy, and the sign is reported on each sub-interval, including the one that contains q₀;
5. the value at q₀ (proton pin, `Q_50_DIGIT_STR`), at mpmath 60 dps.

## 3. Checks (pass/fail fixed in advance)

- **C1.** S+AVG with gluon G reproduces χ_(2,1) of `build_nucleon_nf_mp` at q₀ to 10⁻⁴⁰, for both nucleons.
- **C2.** At t = 0, all 8 templates give the same element, for both nucleons and both dressings (the order-zero invisibility of flavour).
- **C3.** χ_(3) and χ_(1³) equal the product formulas over the letters.
- **C4.** The joint table's S+AVG row reproduces the corpus k = 0 count of 4/8 feasible per nucleon.

## 4. Outcomes, stated before computing

The S+AVG cell **with** gluon dressing is already known to fail reading 3 for both nucleons: χ_(2,1) = −0.28059 (p) and −0.37196 (n) at q₀ (`../bring_route2/results_b3.md`). That cell is therefore a check, not a test. The informative cells are the k = 0 cells and the other templates.

For the primary family (k = 0, placement fixed):

- **(i) Derives.** S+AVG is the only template admissible for both nucleons. Reading 3 then derives the template within this family.
- **(ii) Narrows.** Several templates are admissible. Reading 3 restricts the template but does not derive it, and the survivors are listed.
- **(iii) Conflicts.** S+AVG is inadmissible. The corpus template then conflicts with the ruled SDP.
- **(iv) Decided only at order ≥ 1.** If χ_(2,1) vanishes at t = 0 for every template, the verdict is decided by the leading nonzero order. That order is reported, and so is whether it is the order at which the quark signs first appear. This is the owner's "next order of the tower" made precise. It is not an alternative to (i)–(iii): it says *where* in the tower (i)–(iii) is decided.

No outcome is preferred. If a template is admissible only at q₀ and not on the whole interval (1, ∞), or only for some truncation orders, that is reported as such and not resolved by picking an order.
