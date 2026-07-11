# Why multiplier = coordination number — the equal-weight limit of log-trace bond-extensivity

**Date:** 2026-07-11
**Branch:** `claude/bond-extensivity-equal-weight-2026-07-11`
**Compute:** [`computations/bond_extensivity_equal_weight.py`](../../computations/bond_extensivity_equal_weight.py)
**Witness:** [`computations/bond-extensivity-equal-weight.witness.json`](../../computations/bond-extensivity-equal-weight.witness.json)
**Builds on:** #2089 log-trace derivation
([`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`](2026-06-10-binding-bond-graph-compute-audit-and-derivation.md));
merged 𝓑_K coordination thread (#3549/#3551/#3555).

## The question

The 𝓑_K coordination thread established, fit-free, that the binding multiplier is
the **coordination number** of the building-block link (nucleon `z=A−1`; α-cluster
contact count). The open piece was *why* — the identification "multiplier =
coordination number" was carried as the **bond-extensive hypothesis** (conditional,
not derived).

## What is already derived (not re-derived here)

**Bond-extensivity is the #2089 log-trace result:**

$$
  B(q) = E_0 \cdot \log\!\frac{\mathrm{tr_{free}}}{\mathrm{tr_{atom}}}
       = E_0 \cdot \sum_{\text{bonds}} \log\frac{1}{f_{\text{bond}}(q)},
$$

the log of a product of per-bond Markov factors = a sum over bonds. The factors are
fibre-derived closed forms (δ→0): `z = √q/(q+1)`, `f_pp = z`,
`f_nn = (q^{3/2}−q³−q²+q+1)/(q(q+1))`, `f_pn = (q^{3/2}−(q+1)(q²−1)/2)/(q(q+1))`.

## Contribution — the coordination number is the equal-weight limit

Write `ε_bond = E₀·log(1/f_bond)`. Then `B = Σ_bonds ε_bond`. **If every bond has the
same `ε`,** then `B = N_bonds·ε = (coordination number)·const`. So "multiplier =
coordination number" is exactly the **equal-weight limit** of the derived extensive
sum. Where does equal-weight hold?

| level | bonds | `ε` (at q₀) | equal-weight |
|---|---|---|---|
| **α-cluster** | identical α–α (single `f_αα`) | one value | **exact** (particle symmetry) |
| **nucleon** | `pp/pn/nn` | 0.694 / 0.929 / 1.237 | **fails** — spread **1.78×** |

- **α level: equal-weight is exact** (all bonds identical by ⁴He↔⁴He symmetry), so the
  α-cluster contact-number counting is *genuinely derived* — this is why the merged
  α result closed to <0.5%.
- **Nucleon level: equal-weight fails** (derived 1.78× spread). The nucleon `z=A−1`
  match is therefore a **composition coincidence**, holding for the symmetric A=3
  mirror pair, not a general coordination law.

## The synthesis: `w_n = M · Vol`

For A=3, equal-weight predicts `B(³H) = B(³He) = 3⟨ε⟩` — **no mirror split**. The real
bond-sum gives `B(³H) = 2ε_pn+ε_nn = 3.10`, `B(³He) = ε_pp+2ε_pn = 2.55`; the split

$$ B({}^3\mathrm{H}) - B({}^3\mathrm{He}) = \varepsilon_{nn} - \varepsilon_{pp} = 0.542 $$

is the **isospin / CSB (mirror) asymmetry**. So the thread's weight factorisation
`w_n(K) = M·Vol_n(K)`, grounded in the single derived log-trace, is:

- **`M` = the equal-weight coordination skeleton** (bond count / vertex degree) — the
  magnitude;
- **`Vol` = the isospin bond-energy asymmetry** `ε_nn − ε_pp` that equal-weight drops
  — the T₃ carrier (the very thing option 1 identified as the isospin carrier).

## Verdict (scope-limited (a))

> "Multiplier = coordination number" is the **equal-weight limit** of the derived
> log-trace bond-extensivity — **exact** for identical α–α bonds (α-cluster counting
> derived), a **composition coincidence** for isospin-split nucleon bonds (1.78×
> spread; `z=A−1` holds only for the symmetric mirror). The piece equal-weight drops,
> `ε_nn−ε_pp`, is the isospin carrier `Vol`. This answers the "why" and bounds the
> scope; it is **not** a fit-free closure.

**Open (→ #3548 / #3534):** the per-bond `ε` magnitudes (`f_αα` at the α level; the
`f_bond` normalisation `E₀`) and the α-geometry selection remain the open inputs. The
`ε`-magnitude derivation is #3548's connected multi-bond `tr_M` (PROBE 2) and #3534's
linked-cluster `w_n` — not attempted here.
