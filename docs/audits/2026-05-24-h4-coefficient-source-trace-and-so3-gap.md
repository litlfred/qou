# h⁴ coefficient source trace + the SU(2) → SO(3) architectural gap

**Date:** 2026-05-24
**Trigger:** Author observation during the q-locality probe debrief:
*"there was supposed to be h⁴ terms (not sure if for this or not)
but related to full SO(3) action. SU(2) picked up quadratic terms."*
**Status:** Source trace + structural surprise + concrete next-step
probe definition.

> **Correction (2026-06-01, see
> [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md)).**
> The central premise below — that the discrete $S_3$ subgroup "sees
> only $\ell \le 1$", so that $\ell = 2$ (hence $h^4$) requires the
> full continuous $\mathrm{SO}(3)$ — is **falsified by a
> character-table check**: under $S_3 \subset \mathrm{SO}(3)$ the
> standard/$(2,1)$ irrep already appears at **both** $\ell = 1$
> (mult 1) and $\ell = 2$ (mult 2). The icosahedral $\ell = 2 \to
> h^4$ link is moreover not derivable as written, because the
> icosahedral story lives on $A_5 \subset S_5$ (5 strands) while
> $h^4 = -3/4$ lives on the $H_3$ Borromean trace (3 strands) —
> different representation rings, no canonical map. A genuine
> positive survives: spin-$\mathbb{Z}_2 \ne$ sign-$\mathbb{Z}_2$
> (binary icosahedral $2I$ perfect, $\not\cong S_5$). Read the
> 2026-06-01 audit before re-deriving the $h^4$-from-$\mathrm{SO}(3)$
> mechanism on this doc's terms.

## §1. Source trace for `Geom_leading = Vol(K)/ℏ_q²`

The current canonical mass formula is anchored in
[`derive_m_baryon_volume_form.py:12-15`](../../computations/derive_m_baryon_volume_form.py)
(PR #487 + PR #640):

```
Leptons:  m(K) = m_e · Vol(K) / ℏ_q²       ← muon cross-check K = 4_1
Baryons:  m(B) = m_e · [ Vol(𝓑_3) / ℏ_q² · λ_scale + S(B) ]
```

- `ℏ_q = (q − 1)/q` is **CAL-2-derived** (not free)
- `Vol(K)/ℏ_q²` validated by the muon: `Vol(4_1)/ℏ_q² = m_μ/m_e` to all 50 digits
- The `1/ℏ_q²` factor reflects the **SU(2)-quadratic Casimir** structure of the leading curvature contribution (quadratic in the Lie-algebra-valued connection)

This is not a guess; the leptonic cross-check anchors it.

## §2. The Yekutieli MI tessellation predicts h⁴ at level k=2

Per [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md)
§GB filtration connection (lines 86-91):

| jet grade | tessellation k | cells | contribution |
|---|---|---|---|
| **0** | coarsest | 1 | `Vol/ℏ_q²` — leading (SU(2) quadratic Casimir) |
| **1** | first refinement | 4 | h² correction (CBH ½[α,β]) |
| **2** | second refinement | 16 | **h⁴ correction** ← this trace |
| j | k=j | 4ʲ | h^{2j} correction |

The user's observation maps directly onto this table:
- **SU(2) → quadratic terms** = the k=0 leading `1/ℏ_q²` from the SU(2) Killing form
- **Full SO(3) action → h⁴** = the k=2 level, where the Yekutieli Riemann-product
  recursion adds 16 sub-cell contributions to the h⁴ coefficient

The SO(3) connection is made explicit in
[`knot-operator-bring-action.md:67-102`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md):

> **What the pipeline uses:** only the $S_3$ subgroup — the six
> discrete basis operators.
>
> **What the pipeline does NOT use:** the continuous
> $\mathrm{SO}(3)/S_3$ rotations. These would give:
> 1. Continuous families of Gram matrices $G(\theta)$
> 2. **Angular-momentum quantum numbers** from SO(3) irreps. The
>    irreps of SO(3) are labelled by angular momentum $\ell$;
>    restricting to $S_3$ gives the branching rule
>    $V_\ell|_{S_3} = \bigoplus_\lambda n_{\ell,\lambda} V_\lambda$
> 3. Spherical harmonics on the Bring surface

The pipeline's S_3 discrete subgroup only sees ℓ = 0, 1
(supplying terms up to h²); going to full SO(3) opens
ℓ = 2, 3, … which populate h⁴ and beyond via the spherical-harmonic
spectral decomposition.

## §3. Structural surprise — the Borromean Markov trace has NO h² term

The block
[`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md)
proves the exact closed form of the Borromean Markov trace:

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)
  = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}
$$

with Taylor expansion at h = 0:

$$
  \mathrm{tr}_M
  = 1
    + \underbrace{0}_{\text{no } h^2} \cdot h^2
    - \underbrace{\tfrac{3}{4}}_{h^4} \cdot h^4
    - \tfrac{1}{16} \cdot h^6
    + \tfrac{1}{64} \cdot h^8
    + \cdots
$$

**The h² coefficient is exactly zero.** The block's §3 ("The $h^2$
coefficient is exactly zero") notes this is a **non-trivial
cancellation**: the numerator HAS a +h² coefficient (+1), but the
denominator's +h² coefficient (+1) cancels it exactly. The first
non-trivial correction is **h⁴ with coefficient −3/4** — the *first
topological invariant* of the Borromean linking that distinguishes
$\mathcal{B}_3$ from the trivial 3-component unlink.

The block continues (§"Structural significance"):

> "The h² contribution to the linking weight 𝔴(𝓑₃) — whatever its
> categorical derivation — must come from the **Geom functor's
> evaluation layer** (the Vol/ℏ_q² denominator parametrization),
> not from the Markov trace itself."

This is structurally striking: **Family A's `5/2 + (3/4)·h²` linking
weight contains an h² coefficient that does NOT come from the
underlying topological invariant** (the Markov trace). It comes
from the H_4 → H_3 projection layer or from the Wedderburn
half-symmetric sum at H_4, but the H_3 Markov trace itself has
h² = 0.

## §4. Architectural implications

Three implications follow from §1-§3:

**(I1) The +2.89% gap is the gap between "h²-truncated production"
and "h⁴-included structural truth".** Even Family A's PROVED h²
coefficient (3/4) lives in a projection layer, not in the
topological invariant. The structurally-correct linking weight
might be:

$$
  \mathrm{linking\_weight}_{\text{structural}}(q)
  = \mathrm{const} + 0 \cdot h^2 - \tfrac{3}{4} \cdot h^4 - \tfrac{1}{16} \cdot h^6 + \cdots
$$

(i.e., proportional to the exact Markov trace, scaled by a `const`
that absorbs the Wedderburn 5/2-like factor).

**(I2) Q-locality failure is consistent with the h² being an
artifact.** My q-locality probe (commit `ae70f99af`, witness
`vol-density-borromean-q-locality-probe.witness.json`) shows
Family A's `5/2 + (3/4)·h²` fails with slope −1.565×10⁷ ppm/q —
matching all other h²-truncated probes (Strategy I, REPLACE, V_7,
etc.). If the structurally-correct linking weight has h² = 0, then
no h²-bearing candidate can be q-local, **which is exactly what we
see**.

**(I3) The SO(3) lift is the architectural answer.** Going from the
S_3 discrete subgroup to the full SO(3) action populates h⁴, h⁶,
… terms via angular-momentum spherical-harmonic decomposition.
The 8 ideal octahedral cells of 𝓑_3's tessellation correspond to
the discrete S_3 quotient; refining to SO(3)/S_3 gives the
continuous family of "averaged-crossing" conventions
(`knot-operator-bring-action.md` §"What the pipeline does NOT use").

## §5. Concrete next-step probes

**(P1) Empirical: solve-for-c_4 q-locality probe.** Compute
`m_p_pred(q) = m_e · Vol/ℏ_q² · (5/2 + c_4·h⁴)` and solve for c_4
such that the q-locality slope at q_0 → 0. Cross-check whether the
resulting c_4 matches:
- The Markov trace's natural h⁴: `-3/4 · 5/2 = -15/8 = -1.875` (if scaled by 5/2 factor)
- The Yekutieli k=2 categorical prediction (e.g., `-2G` from doubled cell count)
- The Borromean Jones polynomial's intrinsic h⁴ structure

**(P2) Empirical: structural-linking-weight probe.** Test
`linking_weight = 5/2 · (4 + h² - 3h⁴ - h⁶) / (h² + 4)` (i.e.,
the exact Markov trace scaled by 5/2). Compute slope; report
gap vs CODATA.

**(P3) Categorical: derive c_4 from Yekutieli MI k=2.** Compute
the categorical h⁴ coefficient from the 16-cell tessellation
recursion, CBH expansion at level k=2. Cross-check vs (P1)/(P2)
empirical values.

**(P4) Lean: formalize the h² = 0 exact identity** for the
Borromean Markov trace as a corollary of `prop:borromean-markov-trace-closed-form`,
making the structural separation between "topological invariant
(h² = 0)" and "projection-layer h² (from H_4 Wedderburn sum)"
explicit at the proof level.

## §6. Coordination

- This audit's framing is consistent with:
  - The on-main purge commit `71d674da1` (Yekutieli per-cell purged as non-canonical)
  - PR #1080 (λ_scale absorbed into `VolDensity(K)`)
  - The re-amended Family A gap audit (`2026-05-24-family-a-gap-audit.md`)
  - The q-locality probe (`vol-density-borromean-q-locality-probe.witness.json`)
- The new lens this audit adds: **the h² coefficient itself is a projection-layer artifact**, and the structurally-load-bearing correction is h⁴ via the Yekutieli MI k=2 + SO(3) lift.

## §7. Pointers

- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — **canonical framing reference** (post-PR #1080 merge); λ_scale is the *output* of VolDensity, not a separate object
- [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md) — Yekutieli MI tessellation jet grades
- [`docs/audits/2026-05-24-family-a-gap-audit.md`](2026-05-24-family-a-gap-audit.md) — Family A +2.89% gap re-amended
- [`content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md) — exact closed form, h² = 0
- [`content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md) — S_3 ⊂ SO(3) gap
- [`computations/derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py) — source of `Vol/ℏ_q²`
- [`computations/probes/vol_density_borromean_q_locality_probe.py`](../../computations/probes/vol_density_borromean_q_locality_probe.py) — q-locality probe (commit `ae70f99af`)
- [`computations/vol-density-borromean-q-locality-probe.witness.json`](../../computations/vol-density-borromean-q-locality-probe.witness.json) — witness data
