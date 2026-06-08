# Spin-network state count as a q-dimension partition function — algebraic recasting of the LQG entropy count

**Date:** 2026-06-08 · **Branch:** `claude/vigilant-fermat-SROph` · **PR:** #1995
**Status:** derivation note (formalize-first). An *algebraic recasting* of a known
analytic result, in the UGB→PBW spirit. **Not** a from-scratch LQG derivation
(the repo's [`rem:lqg-adm-ashtekar-comparison`](../../content/quantum-observable-universe/gravity-spacetime/lqg-adm-ashtekar-comparison.md)
explicitly declines that), and **not** a claim that the Immirzi parameter equals
the substrate `q₀` (see §Honest scoping).

## The prior result being re-derived (analytic)

Loop quantum gravity computes black-hole entropy by **counting spin-network
states** that puncture the horizon (Rovelli, gr-qc/9603063; Ashtekar–Baez–
Corichi–Krasnov, gr-qc/9710007; Domagała–Lewandowski, gr-qc/0407051; Meissner,
gr-qc/0407052; number-theoretic refinements 0802.4077, 1101.3660). Each puncture `p`
carries an `SU(2)` spin `j_p`, contributing horizon area

$$
  a_p \;=\; 8\pi\gamma \ell_p^2 \,\sqrt{j_p(j_p+1)}
$$

— the `SU(2)` **Casimir** eigenvalue. The entropy is `S = \log N(A)`, where
`N(A)` counts admissible labellings `\{(j_p,m_p)\}` with total area `≈ A` and the
projection constraint `Σ_p m_p = 0`. The standard derivation is **analytic**: a
Laplace transform in the area + a saddle-point / number-theoretic count. The
outcome fixes the Immirzi parameter `γ` by demanding `S = A/(4\ell_p^2)`.

## The algebraic recasting (three moves)

Each analytic step is replaced by an algebraic one native to QOU.

### Move 1 — area spectrum = standard part of the `SU_q(2)` Casimir

`\sqrt{j(j+1)}` is the `SU(2)` Casimir on `V_j`, which is the `q→1` **standard
part** of the `SU_q(2)` Casimir `C_q(V_j)` (the categorical → archimedean bridge,
[`def:archimedean-realization-functor`](../../content/quantum-observable-universe/mass-theory/archimedean-realization-functor.md)).
*One line, QOU-native:* the area operator is the std of the q-deformed Casimir.

### Move 2 — state count = `q`-dimension partition function

The `m`-degeneracy of spin `j` is `\dim V_j = 2j+1`, the standard part of the
**`q`-dimension** `[2j+1]_q = \dim_q V_j`. Introduce `s` conjugate to area; the
per-puncture grand partition function is

$$
  Z_1(s) \;=\; \sum_{j\in\frac12\mathbb{N}} (2j+1)\, e^{-s\sqrt{j(j+1)}}
         \;=\; \operatorname{std}\!\sum_{j} \dim_q V_j \cdot e^{-s\,a(j)} .
$$

This is exactly the `Σ_λ \dim_q V_λ` transfer-matrix sum already native to QOU
(the linking-weight / vol-density machinery). For `n` independent punctures the
amplitude is `Z_1(s)^n`.

### Move 3 — entropy area law + Immirzi = a **pole** (not a saddle)

Summing over the unconstrained puncture number `n` gives a **geometric series**:

$$
  \sum_{n\ge 0} Z_1(s)^n \;=\; \frac{1}{1 - Z_1(s)},
$$

whose Laplace inversion is dominated by the **pole** at `Z_1(s_\star) = 1`, so
`N(A) \sim e^{s_\star A}` with

$$
  \boxed{\;\sum_{j\in\frac12\mathbb{N}} (2j+1)\, e^{-s_\star \sqrt{j(j+1)}} \;=\; 1.\;}
$$

The exact treatment of the projection constraint `Σ m_p = 0` is the
Domagała–Lewandowski number-theoretic count; it — together with the `SU(2)`
vs `U(1)` convention — selects the precise root and a sub-leading `O(\log A)`
term (the literature spreads `γ ≈ 0.127 / 0.2375 / 0.2740` across these
choices, so check the paper's convention). The **structural** recasting here is
independent of which exact count is used; the boxed equation is the *schematic
(unconstrained)* representative. Then `S = s_\star \cdot A/(8\pi\gamma\ell_p^2)`,
and imposing
`S = A/(4\ell_p^2)` forces `s_\star = 2\pi\gamma`. Hence the Immirzi parameter is

$$
  \gamma \;=\; \gamma_M \;:=\; \frac{s_\star}{2\pi},
  \qquad Z_1(s_\star) = 1 .
$$

*(Notation: `γ` is the standard **Barbero–Immirzi parameter** — the symbol used in
the DLM/Meissner papers. `γ_M` is **this note's shorthand** for its entropy-fixed
value, the root of `Z_1(s_\star)=1`; it is **not** a symbol from those papers.)*

**Can `γ_M` be related to `q₀`?** *Not at leading order — and that is itself
informative.* The criticality `Z_1(s_\star)=1` is fixed by the `SU(2)` Casimir
spectrum `√(j(j+1))` and the **plain** degeneracy `2j+1` — i.e. the `q→1` data —
so `γ_M` is a *universal constant of the spin spectrum*, **independent of `q₀`**.
A genuine `q₀`-dependence can only enter through the **`q`-deformation of the
degeneracy**: replacing `2j+1 = \dim V_j` by the `q`-dimension
`[2j+1]_{q_0} = \dim_{q_0} V_j` gives a `q`-deformed criticality

$$
  \sum_{j\in\frac12\mathbb{N}} [2j+1]_{q_0}\, e^{-2\pi\,\gamma(q_0)\sqrt{j(j+1)}} \;=\; 1,
$$

whose root `γ(q_0)` is a `q₀`-shifted **effective** Immirzi. *That* is the one
place a `γ(q_0)` relation could live — a computable QOU refinement (the
`q`-correction to Meissner), **not a known result**, and exactly where the
`q`/surreal structure enters rather than the `q`-independent leading count.

**The point:** the analytic Laplace/saddle becomes the algebraic statement *"the
`q`-dimension partition function reaches `1`"* — equivalently a transfer-matrix
**spectral-radius `= 1`** condition. The saddle is a pole. This is the
"surface the algebra analysis buries" move applied to the LQG count, in the same
spirit as the Gröbner–Shirshov proof of PBW.

(The repo's LQG dictionary records the roots numerically: `γ ≈ 0.2740` for the
full `SU(2)` count, `γ ≈ 0.2375` for the `U(1)` reduction — the projection
constraint selects the variant.)

## Honest scoping (guardrails)

- **It IS** an algebraic recasting of the *known* DLM/Meissner count — same
  `γ_M`, same area law — with the analytic saddle replaced by a partition-function
  pole. A re-derivation, not a new physical claim.
- **It is NOT** a from-scratch derivation of LQG, and **`γ_M ≠ q₀`**: the Immirzi
  root `γ_M` (`≈ 0.24`; conventions differ — projected/`U(1)` vs `SU(2)` counts
  give ≈ 0.2375 vs ≈ 0.2740, check the paper's convention) and the QOU substrate
  `q₀ ≈ 1.11` are *different numbers*
  that share a structural **role** (the single quantization-scale parameter), as
  the existing dictionary already states. QOU's distinctive content is that `q₀`
  is **derived** (substrate Reeb flow + Bring `χ = −6`), whereas `γ_M` is the
  value the entropy match selects; the recasting says both are fixed by the *same
  kind* of criticality condition, not that they coincide.
- **Three-calibration discipline:** no new fitted parameter is introduced. `γ_M`
  is the known LQG root; the projection-constraint-exact equation is DLM's, cited
  not re-derived.

## Promotion path (to content)

To land this as paper content (after canonical-watcher review, since it touches a
`γ`/`q₀` statement):

1. `def:horizon-puncture-partition-function` — `Z_1(s) = Σ_j \dim_q V_j\, e^{-s\,a(j)}`.
2. `prop:area-spectrum-is-std-casimir` — `a(j) = \operatorname{std} C_q(V_j)`
   (likely near-existing; small Lean over the Hoefsmit/`SU_q(2)` data).
3. `prop:lqg-entropy-from-qdim-pole` (or `conj:` if the constraint-exact step is
   deferred) — area law + `Z_1(s_\star)=1`, interpreting the LQG dictionary remark.

Lean: the std-Casimir and geometric-series/pole pieces are formalizable; gated on
toolchain restore (elan release server firewalled in-sandbox).

## References

Rovelli (gr-qc/9603063); Ashtekar–Baez–Corichi–Krasnov (gr-qc/9710007);
Domagała–Lewandowski (gr-qc/0407051); Meissner (gr-qc/0407052); number-theoretic counts
(0802.4077, 1101.3660); in-repo dictionary
[`rem:lqg-adm-ashtekar-comparison`](../../content/quantum-observable-universe/gravity-spacetime/lqg-adm-ashtekar-comparison.md).
