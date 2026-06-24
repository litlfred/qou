*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Status — what is canonical here.** This block records the **proved Family A
closed form** for the half-symmetric Wedderburn sum at $H_4(q)$, which is the
current production value of `linking_weight(𝓑_3, q)` inside `VolDensity(𝓑_3, q)`.
The earlier $\lambda_{\mathrm{scale}}$ conjecture ($5/2 - h^2 G$) was
**structurally falsified** and the CAL-4 framing **purged**;
$\lambda_{\mathrm{scale}}$ is no longer a separate object — it was
**absorbed into `VolDensity`**. The full falsification history (eight independent
structural searches, the Yekutieli/Bring–Bloch dead-ends) is kept in the audit
trail, **not in the paper**:
[`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](../../../docs/audits/2026-05-18-lambda-scale-derivation-search.md)
and the deprecation note on this block. **Do not revive** the
$5/2 - h^2 G$ form, the Yekutieli per-cell ADD form, or the Bring–Bloch identity.

## Family A theorem (the proved, canonical content)

*Let $q_0 \in \mathbb{R}$ be the substrate parameter
([def:substrate-parameter](#def:substrate-parameter)), $h = q_0 - q_0^{-1}$
the Hecke deformation, and $\dim_q V_\lambda$ the q-deformed dimension of the
irreducible $H_4(q)$-module indexed by $\lambda \vdash 4$ (Frame–Robinson–Thrall
hook-content formula).*

**Theorem (Family A closed form).** *The half-symmetric Wedderburn-sum
projection at $H_4$ has the closed form*

$$
  \lambda_A(q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
             = \frac{3 q^2 + 4 + 3 q^{-2}}{4}
             = \frac{5}{2} + \frac{3}{4}\,h^2,
$$

*with no $h^4, h^6, \ldots$ corrections; all odd-$h$ coefficients vanish by
$q \leftrightarrow q^{-1}$ symmetry.*

## Structural interpretation of the leading term

At $H_4(q)$ the partition spectrum is $p(4) = 5$; the half-symmetric count over
conjugate pairs (each pair weight $1$, the self-conjugate $(2,2)$ weight
$\tfrac12$) gives $1 + 1 + \tfrac12 = \tfrac52$. The structural identity
$\mathrm{Vol}(\mathcal{B}_3) = 8G$ ($G$ = Catalan; the Borromean complement is
8 ideal regular octahedra, $V_{\mathrm{oct}} = 4G$, per Adams 1985) is derived;
how the half-symmetric $H_4$ count drives the production `VolDensity(𝓑_3)`
refinement at higher $h^2$ order is the current research direction (not a
$\lambda_{\mathrm{scale}}$-from-substrate derivation).

## Witness

- [`lambda_scale_all_c_i_family_a.py`](../../computations/lambda_scale_all_c_i_family_a.py) — the proved Family A closed form.
- [`docs/audits/2026-05-18-lambda-scale-derivation-search.md`](../../../docs/audits/2026-05-18-lambda-scale-derivation-search.md) — the falsified-form audit trail (moved out of the paper).
