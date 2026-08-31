---
# qou-o1dh
title: 'RESULT: the "23 MeV 4-body alpha-residual" is not 4-body -- 3-body dominates 3.05x'
status: todo
type: task
priority: high
created_at: 2026-08-31T17:05:03Z
updated_at: 2026-08-31T17:05:03Z
---


## Re-analysis through the GB filtration and the jet tower

Probe: `computations/probes/alpha_residual_gb_jet_bodyorder_probe.py` (4
assertions, all passing). Owner steer: redo the α-residual analysis on the full
tower with the Gröbner-base filtration and the jet.

### How the two filtrations meet

**GB filtration** (`gb_filtration_jet_tracker.py`): grade `H_n(q)` by Coxeter
length `ℓ(w)`, with

    T_w·T_i = T_{ws_i}                 (ascend)
            = h·T_w + T_{ws_i}         (descend),   h = q − q⁻¹

Writing `L` for word length, `g` for final grade, `a` for ascents, `b` for
`h`-terms: `g = 2a + b − L`, hence **`b ≡ g + L (mod 2)`** — the `h`-power and
the GB grade are locked mod 2. Verified against the corpus's own certificate for
`σ₁³ ∈ H₂`: grade 1 carries `q²−1+q⁻² = h²+1` (even, `g+L = 4`), grade 0 carries
`h` (odd, `g+L = 3`).

**So the ℏ_q expansion of `qou-zrx2` IS the GB filtration read by grade.** At
`q = 1`, `h = 0`, every descending term dies, `H_n(q) → ℂ[S_n]`, and the trace
becomes a permutation character — which is exactly the derived floor
`c₀(A) = 2^{−A} − 2^{1−2A}`. The floor is the top-grade associated graded,
nothing more exotic. That closes the conceptual gap between the two beans.

*(`GBFiltrationCollapsesAtE2` is now a `def`, not an `instance` — fixed
2026-08-24 under `qou-fngs` — so downstream theorems taking it are genuinely
conditional. Checked, not assumed.)*

**Jet tower** (`binding_manybody_jet_filtration.py`):

    B(K) = Σ_{n=2}^{A} m_e·a_D^{(n)}·w_n(K),   a_D^{(n)} = lw(n−1) = (1/n)Σ_{λ⊢n} dim_q V_λ

with `a_D = 1, 1, 1.3370, 2.5328, 5.3761, 13.5598, …` (super-exponential) and
`w_n(K)` **undetermined**. The α-residual is by construction the `n = 4` term.

## The finding: it is not 4-body

The corpus's residual is a **pairwise-chain** residual — everything the `(A−1)`
bond sum misses — which lumps all orders `≥ 3` together **and credits `pp` and
`nn` bonds at ~2.4–2.5 MeV each.**

⚠ **Nature binds neither.** The deuteron is the *only* bound two-nucleon system
(`³S₁`, 2.2246 MeV). The diproton and dineutron are unbound `¹S₀` virtual states:
`a_pp ≈ −17.3 fm` (Coulomb-corrected), `a_nn ≈ −18.7 fm`, `a_np(¹S₀) ≈ −23.7 fm`.

With `b₂(pn) = 2.2246`, `b₂(pp) = b₂(nn) = 0`, the cluster (Ursell–Mayer)
expansion of ⁴He — pairs `4pn + pp + nn`, triples `2ppn + 2pnn` — gives

| order | MeV | share |
|---|---|---|
| 2-body `4·b₂(pn)` | **8.8983** | 31.45 % |
| 3-body `2b₃(ppn) + 2b₃(pnn)` | **14.6032** | 51.61 % |
| 4-body irreducible α unit | **4.7942** | 16.94 % |

`b₃(pnn) = 4.0327` (from ³H), `b₃(ppn) = 3.2689` (from ³He); their difference
`0.7637` is largely Coulomb. **Three-body dominates four-body by 3.05×.**

**The genuine irreducible α-unit is ≈ 4.8 MeV, not ≈ 21 MeV.** This agrees with
standard nuclear physics: chiral-EFT three-nucleon forces are essential at
`A = 3,4`, genuine four-nucleon forces are small.

## A derived, unfitted constraint on the open weight `w_n(K)`

The empirical ⁴He profile **peaks at `n = 3`** (`8.90, 14.60, 4.79`). The jet
tower at unit weight is **monotone increasing** (`0.5110, 0.6832, 1.2943`). A
monotone profile cannot make a peak, so the shape must come from `w_n`:

    peak at n = 3   ⟹   w₄/w₃ < a_D^{(3)}/a_D^{(4)} = 0.52787
    match ⁴He       ⟹   w₄/w₃ = (b₄/b₃)(a_D^{(3)}/a_D^{(4)}) = 0.17330

Both sides are AME plus the corpus's own `a_D`; no free parameter. **Any
candidate `ρ·A` residue weight that is flat or rising in `n` is excluded before
it is evaluated** — it must fall by ≥ 1.9× from `n=3` to `n=4`, and by 5.8× to
reproduce ⁴He.

## What neither filtration can inform about — structurally

**The α-unit's categorical representation.**

* `a_D^{(n)} = (1/n)Σ_{λ⊢n} dim_q V_λ` depends **only on `n`**: an average over
  *all* partitions, carrying no flavour, no knot type, no linking data. It cannot
  distinguish ⁴He from any other 4-body cluster.
* The GB filtration grades a **word** by Coxeter length; its `q→1` graded piece
  is a permutation character whose floor depends **only on `A`** — ³H and ³He
  agree exactly, as do ⁵Li and ⁵He (`qou-zrx2`).
* So **every isotope- and α-specific fact lives entirely in `w_n(K)`**, the
  undetermined factor. The filtrations organise the expansion; they do not
  populate it.

⁴He is doubly magic (`N = Z = 2`, closed `s`-shell) with a first excited state at
20.21 MeV — the highest in any light nucleus. Neither `a_D` nor the GB grade has
a variable that could express that.

## What the Standard Model and the eightfold way say

**Eightfold way: nothing.** Flavour `SU(3)` classifies *hadrons* and constrains
their masses (Gell-Mann–Okubo). Nuclear binding is the residual colour force
between colour-singlet nucleons. There is no eightfold-way statement about
`B(⁴He)` and the corpus should not expect one.

**Standard Model: in principle, not in practice.** QCD fixes `B(⁴He)` but no
closed form exists. Lattice QCD binds light nuclei at unphysically heavy pion
masses and is at the edge of feasibility at the physical point. Chiral EFT
reproduces `A ≤ 4` **only with three-nucleon forces** whose LECs are fitted;
NN-only underbinds ⁴He by several MeV (the Tjon line is the ³H–⁴He diagnostic).
SEMF, fitted for `A ≳ 20`, gives 22.19 MeV at `A = 4` against 28.30 — **−21.6 %**,
quoted as context for how badly the collective picture does at the α, not as a
test.

**So the corpus is not failing to reproduce something the SM derives — nobody
derives it.** What it *can* be held to is the **shape**: a body-order profile
peaking at `n = 3`. That is a check the jet tower currently fails at unit weight,
and the `w₄/w₃` bound turns it into a target.

## Consequences for `t7qv`

1. The "4-body α-unit magnitude" gate is aimed at ~21 MeV; the four-body term is
   ~4.8 MeV. **The gate's target should be restated**, and most of what it was
   chasing is three-body.
2. `derive_binding_chain_cooperative`'s `pp`/`nn` bonds have no empirical
   counterpart. That is a modelling choice worth flagging wherever the chain's
   per-bond constants are quoted.
3. The `w₄/w₃ < 0.528` bound is the first falsifiable handle on the `ρ·A` rule.
