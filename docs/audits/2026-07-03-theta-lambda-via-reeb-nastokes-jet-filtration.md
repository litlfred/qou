# θ_λ magnitude gate — the Reeb / na-Stokes super-exponential period (mechanism implemented, weight open)

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-07-03
**Branch:** `claude/mass-binding-gap-review-2026-07-03`
**Compute:** [`computations/binding_manybody_jet_filtration.py`](../../computations/binding_manybody_jet_filtration.py)
**Owner steer:** "θ_λ magnitude gate via Reeb based on the computational time required for
the knot operator" + "the actual hyperbolic volumes coming in via the non-abelian Stokes".

## The synthesis — four hints, one object

The owner's steer names the **A≥3 absolute-binding θ_λ magnitude gate** (the central open
9b gate: canonical trace-binding is *intensive* / saturates ~3–4 MeV, but nuclear binding is
*extensive* ∝A). The route "Reeb → computational time → hyperbolic volume → na-Stokes" is a
single corpus object, already assembled:

```
knot-operator holonomy   Hol(∂S_c) = ∮_{S_c} F           Yekutieli non-abelian Stokes
  → n-jet norm  |a_D^(n)| = |∮ λ_SW^(n)|                  QOU.Mass.NaStokesKeystone
  → mean quantum dimension  a_D^(n) = lw(n−1)              conj #1765
       = (1/n) Σ_{λ⊢n} dim_q V_λ                          prop:sw-period-residue-sum
  → residues = per-block Wedderburn dim_q, HYPERBOLIC (Vol>0) components only
```

- The **"computational time of the knot operator"** is the SW jet-prolongation period
  `a_D^(n) = ∮ λ_SW^(n)` — the Yekutieli **non-abelian-Stokes surface integral** of the
  boundary holonomy. Its per-block residues **are** the θ_λ (per-block `dim_q` at level n).
- The period grows **super-exponentially** (√-branch ⇒ falling-factorial `(1/2)_n`,
  `docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md`). Measured here:

  | n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  |---|--:|--:|--:|--:|--:|--:|--:|--:|
  | `a_D^(n)=lw(n−1)` | 1.000 | 1.000 | 1.337 | 2.533 | 5.376 | 13.560 | 37.368 | 115.826 |
  | ratio | — | 1.00 | 1.34 | 1.89 | 2.12 | 2.52 | 2.76 | 3.10 |

  This is **the extensive channel** the intensive `arccos(χ^λ/d_λ)` phase θ_λ structurally
  lacked (`probe_full_theta_binding.py`: the bounded rotation phase cannot track the ~13×
  D→⁴He growth; the depth-2 SL₂ `τ` is only an n≤4 effective fit).

## What was implemented (the unstaffed consumer)

`conj:binding-manybody-eq-jet-filtration` states
`B(K) = Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` and its `.md/.ts/.lean` blocks exist, but the
**compute consumer was unimplemented** (the §"Compute wire-up" step 2 of the fork audit).
This probe implements it and tests the weight-free (`w_n=1`) null against D/T/³He/⁴He, **no
per-isotope fit**.

## Result — mechanism present, weight open (honest, partial)

| | experiment | jet-filtration (`w_n=1`) |
|---|--:|--:|
| ⁴He/D binding-growth ratio | **12.72×** | **4.87×** |
| intensive arccos-phase (prior) | 12.72× | ~1× (flat — failed) |

- ✅ **The extensive mechanism is present and is the right kind of object.** Unit-weight
  jet-filtration produces a **4.87×** growth (vs the intensive phase's flat ~1×) purely from
  the super-exponential period — a qualitative advance over the refuted phase route.
- ❌ **It undershoots** (4.87× vs 12.72×; absolute −77%…−91%, one-scale shape worst 124%).
  Two structural reasons, both expected: (i) light nuclei (A≤4) sample only `a_D^(2,3,4)` —
  the *slow* head of the tower (super-exp onset is n≥5 / A≥5); (ii) the ⁴He magic-shell
  anchor `2·m_e·A·Vol(L6a4)` shows `w_n(K)` carries a **volume·A** factor far larger than
  `a_D^(n)` itself.

**So `a_D^(n)` is the extensive KERNEL; the per-atom residue weight `w_n(K)` (the "ρ·A scale
rule") is the remaining multiplier** — and per the conjecture it is a **q-difference
recursion output** `G(qx;q)=R(q,x)G(x;q)` (Dirac-type Archimedean image), **not** a fit.

## Verdict (critical-distance)

This **does not close** the θ_λ magnitude gate. It **closes the mechanism half**: the
extensive A-growth is supplied — derivably, no fit — by the na-Stokes / Reeb compute-time SW
period `a_D^(n)=lw(n−1)`, exactly as the owner steered; and the open problem is now localized
and sharpened to the **residue weight `w_n(K)`** (the q-difference kernel `R(q,x)`), which is
where the next work goes. The depth-2 SL₂ `τ` (an n≤4 fit) is superseded by the
super-exponential period for this purpose.

## Lean + paper (the provable core)

The *qualitative* extensivity — the property the intensive phase lacked — is now
**formalised sorry-free** and in the paper:
[`QOU.Mass.JetFiltrationExtensive`](../../content/quantum-observable-universe/lean/QOU/Mass/JetFiltrationExtensive.lean)
proves `jetBinding_mono` (the body-order binding is monotone non-decreasing in the
cutoff `A`) and `jetBinding_lt_succ` (strictly increasing when a body order
contributes positively), over generic non-negative period/weight data. Content
block: [`prop:jet-filtration-binding-extensive`](../../content/quantum-observable-universe/mass-theory/jet-filtration-binding-extensive.md).
The *quantitative* inputs (super-exponential `a_D^(n)` magnitude, the na-Stokes
`a_D^(n)=lw(n−1)` keystone, the residue weight `w_n(K)`) are carried as hypotheses,
**not** derived — the honest scope. Verified `lean`-direct (v4.24.0 + Mathlib).

## Options toward closure (the residue weight `w_n(K)`)

The *mechanism* (extensive super-exp period `a_D^(n)`) is done + Lean-proved; the open piece
is the per-atom weight `w_n(K)`. Options, most-tractable / most-decisive first:

1. **`w_n(K)` = hyperbolic link-volume of the `n`-body sub-cluster (recommended — the literal
   "hyperbolic volumes via na-Stokes").** The `n=4` anchor is `B_4(⁴He)=2·m_e·A·Vol(L6a4)` — a
   hyperbolic *volume*; and `a_D^(n)` is the na-Stokes surface integral over the **hyperbolic**
   (`Vol>0`) components. So `w_n(K)` is literally the hyperbolic volume of the `n`-body sub-link
   of `𝓑_K`. Concrete: enumerate the `n`-body inter-nucleon sub-links per atom, compute their
   hyperbolic volumes (SnapPy / the Reeb-flow volume machinery `reeb_flow_garside…`), use as
   `w_n(K)`. **This merges with gap #2** (3-body / whole-A link-volume) — one task closes both.
   Non-fit (volumes are topological invariants). Decisive.
2. **Derive-or-refute the q-difference kernel `R(q,x)`** (`G(qx;q)=R(q,x)G(x;q)`, the
   conjecture's own prescription). Extract `w_n(K)` from the six anchors (4 AME + n=2
   deuteron-bond + n=4 magic-shell) and test whether they solve **one** recursion with a
   *derived* `R(q,x)`; if they need a per-isotope constant it is a **fit ⇒ refute** (STRICT).
   Cherry-pick (owner-authorised): the q-Bessel contiguity kernel
   (`QBesselContiguityRecurrence.lean`) is the named engine, and #3265's Casoratian/bar-parity
   Q_β `c_k` kernel may *be* `R(q,x)` — pull it when it lands.
3. **Wire the q-Bessel fast engine + push to A≥5.** The super-exp onset is n≥5 (`a_D^(5)=5.38`,
   `a_D^(6)=13.56`); light nuclei sample only the slow head. Extend the jet-filtration to ⁶Li /
   ¹²C / ¹⁶O and re-run the L2 dashboard + mass-table sweep — tests whether the mechanism closes
   the achievable Subgoal-1 gaps where growth matters.
4. **The na-Stokes `= lw` keystone** (`a_D^(n)=lw(n−1)`, conj #1765) — full *derivation* (not
   just compute) is the owner-gated s5-so3 keystone. The compute path (using `lw`) does not need
   it; the theorem does. Gated — not a self-serve step.

**Recommendation:** #1 (hyperbolic link-volume `w_n`) as the primary — it is the literal
na-Stokes realisation, non-fit, and merges with gap #2; #2 as the derive-or-refute backstop
that catches a fit early.

## Provenance

Compute: `binding_manybody_jet_filtration.py` (reuses the `lw`/`dim_q` of
`sw_period_growth_probe.py`). Corpus: `QOU.Mass.NaStokesKeystone`,
`conj:binding-manybody-eq-jet-filtration`, `prop:sw-period-residue-sum`,
`prop:mi-sw-abelianisation`, `docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md`.
Supersedes the intensive-phase route of `probe_full_theta_binding.py` for the extensive channel.
EXPLORATORY — no production wiring, no fitted constant.
