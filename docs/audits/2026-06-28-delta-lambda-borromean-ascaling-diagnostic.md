# 2026-06-28 — Δ_λ frontier: the Borromean per-braid tower as a magnitude-adding A-scaling lever

> **⚠ CORRECTION (2026-08-24) — every `6.17×` / `17.90×` and every per-isotope
> net/target figure in this doc is **convention C**, and two of them were also
> mislabelled at the time of writing.** Found while excising convention C
> (`qou-cds1`, PR #5622).
>
> **1. The frame.** The producer's edge-set block
> ([`delta_lambda_borromean_ascaling.py:106`](../../computations/delta_lambda_borromean_ascaling.py))
> carried `z_C = √q/(q+1)`. Under the canonical `z_D = q³/(q²+1)`:
>
> | | all-pairs C(A,2) | | adjacent A−1 | |
> |---|--:|--:|--:|--:|
> | | **C** | **D** | **C** | **D** |
> | D (²H) | 1.115 | 0.927 | 1.1150 | 0.9274 |
> | ³H | 0.580 | 0.559 | 0.5339 | 0.5064 |
> | ³He | 0.557 | 0.511 | 0.5066 | 0.4530 |
> | ⁴He | 0.226 | 0.229 | 0.1843 | 0.1815 |
> | ⁶Li | 0.329 | 0.359 | 0.2009 | 0.2112 |
> | ¹²C | 0.354 | 0.408 | 0.1012 | 0.1123 |
> | ¹⁶O | 0.440 | 0.510 | 0.0880 | 0.0991 |
> | ⁵⁶Fe | 1.392 | 1.639 | 0.0623 | 0.0734 |
> | **spread** | **6.17×** | **7.16×** | **17.90×** | **12.64×** |
>
> **The conclusion below is unchanged.** Adjacent is still worse than all-pairs
> (12.64 vs 7.16), so the edge-set / sparsification hypothesis stays REFUTED,
> and the A-profile is still non-uniform and U-shaped.
>
> **2. The mislabel, which is the more interesting half.** The `6.17×` was
> never the *tower's* spread. `tower_net_over_target_spread` in
> [`delta-lambda-borromean-ascaling.witness.json`](../../computations/delta-lambda-borromean-ascaling.witness.json)
> was **7.1622294** in the C-frame committed copy too, with rows 0.927 / 0.229 /
> 0.408 / 1.639 — because the tower comes from
> [`borromean_binding_recompute.py:111`](../../computations/borromean_binding_recompute.py),
> which is `z = q**3/(q**2+1)` and whose docstring says *"NOT convention C"*.
> Only the *local re-run* in the edge-set block was C. So §2 and the
> extensive-bulk section below, which quote `6.17×` and `D 1.12 / ⁴He 0.23 /
> ⁵⁶Fe 1.39` as the tower's A-profile, are quoting the C-frame **edge-set
> re-run**, not the tower. This was an intra-file frame straddle: two
> computations of the same all-pairs sum disagreeing by 16 %.
>
> Under D the straddle dissolves — the edge-set re-run reproduces the tower
> **row by row and to all printed digits** (7.162229445453156 both), which is
> what a re-implementation of the same sum should always have done. The same
> defect and the same repair applied to
> [`borromean_per_lambda_fr_probe.py`](../../computations/probes/borromean_per_lambda_fr_probe.py),
> whose `tower()` is documented as a *"mirror of
> borromean_binding_recompute.borromean_binding"* and was not mirroring it.
>
> Figures updated in place below where they were re-measured. The ⁴⁰Ca row in
> the extensive-bulk table is **not** re-measured — ⁴⁰Ca is not in the
> producer's AME table, so that number is left at its C value and marked.

> **⚠ CORRECTION (2026-06-29) — the "extensive bulk = universal `2·m_e·8G·A`"
> claim in this doc (and its follow-on three-piece test) is WRONG; it contradicts
> existing corpus that I failed to grep.** Per
> [`2026-06-24-magic-a-truncation-overclaim-correction.md`](2026-06-24-magic-a-truncation-overclaim-correction.md),
> `2·m_e·A·8G` (8G = Vol(L6a4)) is the **⁴He-specific doubly-magic formula** (the
> n=4 body-order term of [`prop:binding-manybody-jet-filtration`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md)),
> **NOT** a universal A-linear bulk — extrapolating it to D / ⁶Li / ⁵⁶Fe is exactly
> the conflation that correction forbids. Moreover the body-order series
> **diverges** (`λ₊ = 2.185 > 1`, Lean `lambdaPlus_gt_one`), so there is no
> "bulk × kernel" product to close — binding is the additive (resummed) body-order
> series `B(K)=Σ_n B_n`, `B_n=m_e·a_D^(n)`, with **n=2** (`m_e·Vol(6₂)`, +1.09%)
> and **n=4** (the magic formula, +5.87%) derived and **n=3 open** (#1790). The
> "A-scaling diagnostic" below stands only as raw `B_AME/(A·8G)` ratios; their
> interpretation as a bulk-vs-kernel decomposition is retracted. See
> [`2026-06-25-sw-jet-prolongation-explicit-and-fork.md`](2026-06-25-sw-jet-prolongation-explicit-and-fork.md)
> for the resolved fork and the canonical body-order framing.

**Branch:** `claude/delta-lambda-borromean-ascaling-2026-06-28`
**Goal:** Δ_λ binding-closure (Track-A / Option-E)
**Scope tag:** (a) scope-limited — positions a magnitude-side lever + sharpens the open item to the A-scaling. **No 7th fit-based ansatz; no closure claimed.**
**Producer:** [`computations/delta_lambda_borromean_ascaling.py`](../../computations/delta_lambda_borromean_ascaling.py)
**Witness:** `computations/delta-lambda-borromean-ascaling.witness.json`
**Builds on (same day):** [`2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md`](2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md) (the ℓ¹-ceiling sign-only prune), [`2026-06-28-brane-tower-formalize-first-plan.md`](2026-06-28-brane-tower-formalize-first-plan.md) (the Borromean single pipeline, PR #3016 merged).

## Context

Today's ℓ¹-ceiling audit proved (Lean, sorry-free) that **sign-only** Δ_λ
re-derivations are excluded — the ℓ¹ ceiling of the canonical
`Δ_λ = sgn(w₀^{S_{λ'}})·dim` term set is 36–59 % of target for every light
isotope — so a **magnitude-adding** ingredient is *necessary*, and a *flat*
q-dim convention cannot reproduce binding's A-scaling: "the closure object must
carry A-/λ-dependent structure that bends the A-scaling" (route ii/iii / a
structured kernel, e.g. z2bn's q-Gaussian/Habiro EGF).

This diagnostic asks the obvious follow-up: the **Borromean per-braid tower**
just merged (PR #3016) **is** a structured, zero-parameter magnitude-adding
kernel (the per-braid Li₂^q tower over the Borromean nucleon `τ=0.9986`). Does it
bend the A-scaling toward closure?

## Result (fit-free — only reads the tower's output)

`net/target = B_tower / B_AME` (closure ⇒ 1.0):

| iso | A | tower net/target | canonical `sgn·dim` net/target |
|-----|--:|-----------------:|-------------------------------:|
| D   | 2 | **0.927** | 0.171 |
| T   | 3 | 0.559 | 0.225 |
| ³He | 3 | 0.511 | 0.304 |
| ⁴He | 4 | 0.229 | 0.107 |
| ⁶Li | 6 | 0.359 | — |
| ¹²C | 12 | 0.408 | — |
| ¹⁶O | 16 | 0.510 | — |
| ⁵⁶Fe | 56 | 1.639 | — |

> **Corrected 2026-08-24.** This column previously read 1.115 / 0.580 / 0.557 /
> 0.226 / 0.329 / 0.354 / 0.440 / 1.392. Those are the **convention-C edge-set
> re-run's** figures, not the tower's — the clearest instance of the mislabel
> described in the top banner, since the table is captioned *"tower net/target"*
> and the section says it *"only reads the tower's output"*. The values above are
> `rows[].tower_net_over_target` from the witness and are the **same in both
> frames**, the tower having always been convention D.

**Two findings:**

1. **The per-braid kernel supplies the missing magnitude.** On D/T/³He/⁴He it
   reaches `1.7–5.4×` higher net/target than the flat `sgn·dim` (D: 0.93 vs
   0.17). A *structured* kernel demonstrably escapes the sign-only ℓ¹ ceiling —
   concrete support for today's "magnitude-adding ingredient is necessary."
   (Caveat: the tower is a different formula — Path A/B trace tower, not a
   re-weighting of the Path-D `Σ_λ` vector — so this is "an alternative
   structured kernel reaches closure-grade magnitude," not "re-weights the same
   vector." The point stands: structure supplies what flat `sgn·dim` lacks.)

2. **But it does NOT close — the A-scaling is still non-uniform.** net/target
   spread over A is **7.16×** (D over at 0.93, mid under at ⁴He 0.23, ⁵⁶Fe over
   at 1.64) — see the 2026-08-24 banner: these are the edge-set re-run's
   figures, and the tower's own spread was 7.1622× in both frames. The per-braid kernel adds magnitude but its effective A-scaling
   over-binds the extremes and under-binds the middle — it does not bend to a
   *uniform* +1. So magnitude alone, even structured, is not closure; the
   A-/λ-shape is still wrong.

## Structural origin of the 7.16× spread — the edge-set hypothesis is REFUTED

A natural hypothesis: the tower's pair term sums over **all C(A,2) pairs**
(complete graph, ~A²), but nuclear binding is **extensive** (~A, saturation —
each nucleon binds only its neighbors), so sparsifying to **adjacent bonds**
(A−1, ~A) should flatten the A-scaling. **Tested and refuted:**

| edge set | net/target A-profile | spread |
|----------|----------------------|-------:|
| all-pairs C(A,2) ~A² | D 0.93, ⁴He 0.23, ¹²C 0.41, ⁵⁶Fe 1.64 (U-shaped) | **7.16×** |
| adjacent A−1 ~A | D 0.93, ⁴He 0.18, ¹²C 0.11, ⁵⁶Fe 0.073 (monotone ↓) | **12.64× (worse)** |

Sparsifying **worsens** the spread — adjacent monotonically *under*-binds heavy
nuclei (⁵⁶Fe 0.073). So the U-shape is **not** a pure edge-count artifact. It
decomposes into two distinct effects:

1. **A²-overscaling at the heavy end.** all-pairs ~A² grows faster than
   `B_AME` ~A, so net/target rises with A (⁵⁶Fe 1.39). The per-pair magnitude is
   only `~0.4 MeV` (vs the ~8 MeV/nucleon real binding), and all-pairs compensates
   for heavy nuclei by sheer pair count — overshooting.
2. **The ⁴He magic dip.** ⁴He is doubly-magic (anomalously tight, ~7 MeV/nucleon);
   the tower has **no shell/magic structure**, so even all-pairs (6 pairs ×0.4 MeV)
   reaches only 0.23 of `B_AME` — the known magic-A issue (`standard-part-functor.md`
   uses the shell-closure `2·m_e·A·8G` for ⁴He specifically).

**Consequence (sharpens the lever map):** the **edge-set lever alone (w5tg) cannot
bend this A-scaling** — sparsifying the graph makes it *worse*, not better. The
closure needs **magnitude-reshaping** (a per-λ/per-bond generating kernel that
lifts the ~0.4 MeV per-pair toward the saturated nuclear scale — exactly z2bn's
`R(q,x)`) **plus shell/magic structure** for the ⁴He-type dips. Neither pure
all-pairs nor pure adjacent is the right combinatorics.

## The bulk is EXTENSIVE (A-linear), not the A² pair tower — and q-Askey says why

Quantifying the ⁴He magic dip resolves the whole A-scaling. Compare the tower's
A² pair structure to the **extensive** shell term `2·m_e·8G` per nucleon
(`8G = Vol(L6a4)`, the Borromean shell residue, ≈ **7.49 MeV/nucleon** ≈ the
empirical ~8):

| iso | A | tower net/target (A²) | extensive net/target (A·8G) |
|-----|--:|--:|--:|
| ⁴He | 4 | 0.229 | **1.059** |
| ¹²C | 12 | 0.408 | 0.975 |
| ¹⁶O | 16 | 0.510 | 0.939 |
| ⁴⁰Ca | 40 | 1.004 † | 0.876 |
| ⁵⁶Fe | 56 | 1.639 | 0.852 |

† ⁴⁰Ca is not in the producer's AME table; this figure is **not** re-measured
and is left at its convention-C value.

The extensive A-linear form gives net/target **0.85–1.06 for A≥4 (spread 1.65×)**
— far flatter than the tower's **7.16×**. So **the bulk nuclear binding is
extensive (A-linear, a per-nucleon shell residue), NOT a q-deformed pair sum.**
The ⁴He "dip" is the tower missing ~23.6 MeV (83 %) of extensive bulk binding.
(The residual heavy under-bind of the flat form — ⁵⁶Fe 0.85 — is the
liquid-drop surface `~A^{2/3}` + Coulomb `~Z²/A^{1/3}` corrections, expected.)

**q-Askey connection (answers "can q-Askey polys help?", grounded in today's
[`q-askey-scheme-qclt-wlambda-applicability.md`](2026-06-28-q-askey-scheme-qclt-wlambda-applicability.md)).**
The tower's `C(A,2)~A²` pair scaling **is** the **q-Gaussian obstruction**: the
Bożejko–Speicher even moments `Σ_{π} q₀^{cr(π)} ≥ q₀^{C(n,2)} = exp(Θ(n²))`
diverge super-exponentially at `q₀>1`
([`prop:q-gaussian-obstruction-at-q0`](../../content/quantum-observable-universe/mass-theory/q-gaussian-obstruction-at-q0.md)).
So the per-braid pair tower over-binds heavy nuclei for the **same proved
reason** the q-Gaussian fails to exist at the substrate — the A² crossing-sum is
the obstructed object. The honest q-Askey verdict for binding:

- **q-Askey kernels (Hahn–Exton q-Bessel, continuous q-Hermite/Rogers–Szegő) are
  the FIBRE per-λ binding kernel** (`|q|≤1`, via the bar involution `q₀↔1/q₀`) —
  exactly z2bn's `R(q,x)` / `BindingQBesselKernel.lean`. They **organize** the
  per-λ magnitude.
- **They are NOT the A-scaling bulk.** The bulk is the extensive A-linear `8G`
  shell residue; trying to carry it with a q-deformed pair sum hits the
  q-Gaussian wall at `q₀>1`. q-Askey is a *fibre-kernel* lens, not a closure of
  the A-scaling (consistent with today's audit: "helps by organizing… does not
  close GAP 3 or GAP 5").

**Net for the lever map:** closure = **extensive bulk (A-linear 8G) + a fibre
q-Askey per-λ kernel (z2bn R(q,x), the magnitude shape) + liquid-drop
surface/Coulomb corrections** — three pieces. The per-braid A² pair tower is
**none** of them as the bulk; it is at most a small fibre-level correction, and
its A² scaling is the obstructed direction.

## Conclusion (scope (a))

The Borromean per-braid Li₂^q tower is a **genuine magnitude-side lever** for the
Δ_λ frontier — it joins z2bn (R(q,x) kernel), w5tg (edge-set), thb7 (universal-ρ),
PROBE-2 (A=4 interface) as a zero-parameter structured kernel that escapes the
sign-only ceiling. Its **derive-or-refute signature** is sharp and specific: the
**7.16× A-scaling spread** (over-binds light + ⁵⁶Fe, under-binds A=4–16). The open
item is unchanged in kind — *which* structured kernel bends the A-scaling to
uniform closure — but now has one more concrete, falsifiable candidate with a
measured A-profile, not a fit.

**Not claimed:** closure; a derivation of the tower's A-profile; that the
per-braid kernel is *the* Δ_λ. The q-dim-convention hidden-DOF caveat from the
ℓ¹ audit applies — magnitude size alone is a weak discriminator; the A-scaling
*shape* is the real test, and the tower fails it (non-uniform).
