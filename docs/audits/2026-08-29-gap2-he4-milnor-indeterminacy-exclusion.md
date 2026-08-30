# GAP-2: the ⁴He magic surplus and the Milnor μ̄ term — CONDITIONAL, re-scoped (b) → (a) 2026-08-30

> **🛑 RE-SCOPED 2026-08-30 (b) → (a), by its own author. The premise is
> contradicted by the corpus one file over.**
>
> This audit claims a scope-(b) structural exclusion on the strength of *"a
> cluster in which every bonded pair is Hopf-linked (`lk = 1`) — which is
> exactly the max-contact nuclear contact graph"*. **The corpus does not
> establish that, and contradicts it at the triton.**
> [`binding_mn_milnor_linking.py:188`](../../computations/binding_mn_milnor_linking.py)
> models the triton as `BORROMEAN`, whose pairwise linking numbers are
> `[0, 0, 0]` (recomputed, not quoted), while
> [`gap2_borromean_triple_count.py`](../../computations/gap2_borromean_triple_count.py)
> gives the triton `M₂ = 3` — all three pairs **bonded**. So three bonded pairs
> are modelled with `lk = 0`.
>
> Neither branch of the resulting dichotomy leaves the exclusion standing:
>
> - **the triton model is right** ⇒ bonded pairs may have `lk = 0`, so ⁴He's
>   `K₄` may too, `μ̄` is determinate there, and `M₃`/`M₄` need **not** vanish;
> - **`bonded ⇒ lk = 1` is right** ⇒ the triton triple is indeterminate too,
>   `M₃(T) = 0`, and `e₃ = (B(T) − 3e₂)/M₃(T)` is a division by zero with a
>   **nonzero** numerator (1.8080976 MeV) — the corpus's own 3-body calibration
>   does not exist.
>
> **What survives is the conditional**, and it is untouched: *if* every bonded
> pair on a cluster has `lk = 1`, *then* every higher `μ̄` on it is
> content-free. Milnor's indeterminacy theorem is a theorem. What fails is my
> assertion of its **hypothesis** — the `conditional-proved ≠
> premise-established` failure mode, committed while citing a real invariant
> whose applicability I had not checked.
>
> The load-bearing open question this promotes: **what fixes the linking number
> of a bonded pair?** Until that is derived rather than assigned, every `μ̄`
> count in the tower — the overshoot and the vanishing alike — is conditional
> on an unforced choice. Demonstration:
> [`bonded_pair_linking_inconsistency_probe.py`](../../computations/probes/bonded_pair_linking_inconsistency_probe.py).

**Date:** 2026-08-29 · **Bean:** `qou-klgu` (GAP-2 open step, under `qou-ooqh` / `qou-vibo`) ·
**Compute:** [`computations/gap2_he4_borromean_mu_bar.py`](../../computations/gap2_he4_borromean_mu_bar.py)
· **Witness:** `computations/gap2-he4-borromean-mu-bar.witness.json` ·
**Status:** EXPLORATORY, scope-(b) structural exclusion (cited invariant). No fit, no wiring.

## What GAP-2 asked, and the open step this closes

The body-order binding tower is `B(K) = e₂·M₂(K) + e₃·M₃(K) + e₄·M₄(K)`, `eₙ = m_e·a_D^(n)·wₙ`
the per-order energy. The framework's proposed **geometric bond-count** `Mₙ(K)` is the order-`n`
**Milnor invariant** `μ̄` of the nucleus link `𝓑_K` (`binding_mn_milnor_linking.py`, validated:
Hopf `lk=1`, Borromean `μ̄₁₂₃=±1`, chain `μ̄₁₂₃=0`).

The prior GAP-2 probe ([`gap2_borromean_triple_count.py`](../../computations/gap2_borromean_triple_count.py),
[audit](2026-07-11-gap2-borromean-triple-count.md)) **refuted the 3-clique reading** (it overshoots
A≥5 by +13→24 %) and localized `M₃` to the Milnor-**irreducible** (Borromean, `μ̄₁₂₃≠0`) triple
count — leaving "compute the irreducible count for the contact-graph→framed-link promotion" as the
open step. This audit runs that step for ⁴He.

## The crux: Milnor μ̄ indeterminacy

Milnor's `μ̄(i₁…i_k)` is well-defined only **modulo the gcd of the lower-order invariants** (the
pairwise linking numbers `lk` among the indices). For the Borromean rings `lk_ij = 0`, so `μ̄₁₂₃`
is a genuine ℤ-invariant (`±1`). For a cluster in which **every bonded pair is Hopf-linked**
(`lk = 1`) — which is exactly the **max-contact** nuclear contact graph — the indeterminacy modulus
is `gcd(lk) = 1`, so every higher `μ̄` lives in `ℤ/1 = 0`: **it carries no invariant content beyond
the pairwise bonds.**

## Result — computed for ⁴He (all exact integer Magnus arithmetic)

⁴He = the max-contact **tetrahedron** `K₄` (all `C(4,2)=6` pairs bonded). Per-order energies pinned
per-order on the minimal nucleus of each order (anti-fit): `e₂ = B(D) = 2.2246 MeV`,
`e₃ = (B(T) − 3e₂)/M₃(T) = 1.8081 MeV` (triton, `M₃(T)=1`, its single triple is genuinely
Borromean: `lk=0`, `μ̄₁₂₃=+1`). Magic surplus `= B(⁴He) − 6e₂ = 28.296 − 13.347 = 14.948 MeV`.

| ⁴He link model | pairwise `lk` | `M₃` (irreducible) | `M₄` | `e₃·M₃` vs 14.95 |
|---|---|--:|--:|---|
| **(A) all-Hopf `K₄`** (the max-contact tetrahedron — the physical model) | all `= 1` | **0** | **0** | `0` — off by −14.95 |
| (B) Borromean-core + apex | mixed | 1 | 0 | `1.81` — off by −13.14 |
| (C) Brunnian 4-body | all `= 0` | 1 | 0 | `1.81` — off by −13.14 |

In the **physical** model (A) every triple has `lk=1` ⇒ `μ̄₁₂₃` indeterminate mod 1 ⇒ **every triple
reducible**, `M₃_irr = 0`; and `μ̄₁₂₃₄` is likewise indeterminate (`lk≠0`), `M₄ = 0`. So the Milnor
tower supplies **nothing** beyond the pairwise backbone `M₂ = 6`. The models that *do* carry an
irreducible triple (B, C) require **vanishing** pairwise linkings — i.e. **not** a max-contact
cluster — and even then reach only `1.81 MeV`, an eighth of the surplus.

## Reading — scope-(b) structural exclusion (cited invariant)

By **Milnor's indeterminacy theorem**, on any all-pairwise-bonded (max-contact) cluster every higher
`μ̄` (`n≥3`) is identically zero-content. Therefore **the Milnor-μ̄ realization of the geometric
bond-count `Mₙ(K)` cannot carry the ⁴He magic surplus** — not "does not with these numbers," but
*cannot*, for the structural reason that the tetrahedron's nonzero pairwise linkings annihilate the
entire higher tower. This is a genuine (b)-exclusion of the **Milnor route for tightly-bound clusters**;
the cited invariant is the μ̄ indeterminacy.

**What it does NOT exclude (scope discipline).** It excludes only the *Milnor-invariant* realization
of `M₃/M₄`. It does **not** exclude a **non-Milnor** super-pairwise object carrying the surplus — and
indeed the corpus already names one: the ⁴He surplus is a **non-transferable shell closure**
(`e₄` over-predicts ⁵Li's two tetrahedra, prior GAP-2 audit), i.e. the **Wigner spin-isospin SU(4)
`[1⁴]` α-cluster antisymmetrizer** (trace `= C(4,A)`, zero for `A>4` → ⁴He doubly-magic locality,
`SU4SupermultipletGate.lean`). That object is *not* a link invariant, so the indeterminacy argument
does not touch it.

## Consequence for the M_n(K) programme

The magnitude gap (bean `qou-vibo`) sharpens: the coordination-geometry route `Mₙ = μ̄` is the right
tool for the **loosely-bound / low-lk** many-body terms (the triton triple *is* a well-defined
Borromean `+1`), but is **structurally blind** to the tightly-bound ⁴He magic, whose surplus lives in
a **non-link-invariant** shell object (SU(4) `[1⁴]`). The two are complementary, not competing:
Milnor `μ̄` for `lk=0` irreducible many-body linking; the SU(4) supermultiplet for the max-contact
shell closure.

## Discipline

Scope-(b) exclusion with a **cited invariant** (Milnor μ̄ indeterminacy) — per the "refuted ≠ ruled
out" rule this is a permitted (b), not a bare numerical negative. `eₙ` pinned per-order on the
minimal nucleus (anti-fit), exact integer Magnus arithmetic, no float in the topology, no production
wiring. The triton `μ̄₁₂₃=+1` and the ⁴He `M₃_irr=0` are both honest computed facts.

## References
- [`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py) — the validated μ̄ tower.
- [`gap2_borromean_triple_count.py`](../../computations/gap2_borromean_triple_count.py) / [audit](2026-07-11-gap2-borromean-triple-count.md) — the 3-clique refutation this continues.
- [`docs/workplans/2026-07-11-mnk-derivation-gaps.md`](../workplans/2026-07-11-mnk-derivation-gaps.md) — GAP-2.
- [`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md) — the SU(4) `[1⁴]` non-transferable shell closure.
