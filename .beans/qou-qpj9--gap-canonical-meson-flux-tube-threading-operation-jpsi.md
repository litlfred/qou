---
# qou-qpj9
title: 'GAP: define canonical meson flux-tube threading braid (J/ψ underived)'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-24T14:11:33Z
---

## The wall

J/ψ = c̄c targeted as a hyperbolic bound-state braid volume
(`computations/jpsi_boundstate_mass_probe.py`,
`docs/audits/2026-08-02-jpsi-boundstate-mass.md`, branch
`claude/jpsi-boundstate-mass-2026-08-02`).

**In-range but underived.** With the scale fixed only on the proton
(Borromean → 938 MeV, 128.044 MeV/Vol), J/ψ needs Vol ≈ 24.19 and η_c
needs Vol ≈ 23.30 — both reachable by simple hyperbolic braids (positive:
distinguishes J/ψ from the neutrino's scope-(b) volume exclusion). But **no
derived c̄c braid**:

1. The proton's own family `(σ₁σ₂⁻¹)^k` misses J/ψ at every integer winding
   (k=6→2770, k=7→3336; J/ψ=3097 falls between).
2. The volume spectrum is dense near target (~4% of 196 simple braids land in
   the 230-MeV band).
3. J/ψ and η_c — the same c̄c system split by only 3.7% hyperfine — are best-fit
   by DIFFERENT-topology braids (4-str `(σ₁σ₂⁻¹σ₃)⁴`→3085 vs 5-str
   `(σ₁σ₂⁻¹σ₃σ₄⁻¹)³`→2964). Per-state fitting signature.

## The precise open item

**"Thread c̄c through the gluon T(2,9) color tube" is topologically
under-defined.** Satellite/companion, cable, connected-sum (non-hyperbolic),
and strand-insertion each give a different volume; the framework specifies no
canonical operation. A prediction requires a **single canonical parameter-free
topological operation** that fixes strand count + insertion sites + winding from
the c̄c + gluon quantum numbers *without reference to 3097 MeV*, then check once
against J/ψ AND η_c jointly (same base braid, hyperfine as perturbation).

## Suggested next honest step

Derive the meson flux-tube operation from the proton's 3-tube Borromean vertex
by the Y-junction → single-tube reduction (baryon → meson). If that reduction
fixes a unique braid a priori, it is a genuine derivation; check it once.
Anything that picks the braid to land on 3097 is a fit and worthless.


## 2026-08-24 — this bean's "suggested next honest step" is ALREADY DONE, and one of its obstructions is phantom

**Read this before working the bean.** The step recorded above — *"Derive the meson
flux-tube operation from the proton's 3-tube Borromean vertex by the Y-junction →
single-tube reduction"* — was **attempted and closed** on 2026-08-02
(`docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md`, PR #4614,
sorry-free `MesonFluxTubeReduction.lean`). It is a **scope-(b) structural
exclusion**: the literal reduction takes strands 3 → 2, `B₂ ≅ ℤ` is abelian, so
every 2-strand closure is `T(2,k)` with `Vol = 0`. Do not redo it.

### Correction to that audit (PR #5659, this branch)

It records **two** independent obstructions. **One is not real.**

It claims the corpus assigns charm two incompatible windings — `T(2,5)` and
`T(2,7)` — and flags the conflict for canonical-watcher. Both tables say
**T(2,5)**. The reported `(2,7)`/`7₁` is the value on the **preceding line**:
line 8 is the **tau lepton** `| 𝔎_τ | septafoil | 7₁ | τ⁻ | τ⁺ |`. The audit read
line 9's label with line 8's knot.

Verified: `git log -L 9,9` shows the line was **created** as `(2,5)`
(`e54ffbca0a`); `git log -S` finds no commit that ever wrote a charm `7₁` row;
corpus-wide, charm maps to 7 nowhere.

**The correction makes the surviving obstruction HARDER.** With charm fixed at
n = 5 there is no n = 7 alternative, so `D {5,3}` is an **exact** multiset
collision with `K {3,5}`.

### The "missing" T₃ grading is in the corpus, as σ

Table 2 read whole:

    gen 1   u = T(2,3)      d = T(2,3)^σ
    gen 2   c = T(2,5)      s = T(2,5)^σ
    gen 3   (top deprec.)   b = T(2,7)^σ

**σ present iff down-type — 5/5 quark rows.** `T_{m,n}^σ = T_{m,-n}`. So charm
and strange are a knot and its mirror, not the same object. The degeneracy is
`windingContent` **discarding σ** in its projection to `Multiset ℕ` — a lossy
projection, not an absent structure.

**Caveat, do not over-read:** σ is overloaded (it also marks
particle/antiparticle — electron vs positron). Whether table 2's σ *is* T₃ or is
notation reuse aligning 5/5 is the open question. A pattern is not a derivation.

### What is actually still open here

The braid is still not canonically fixed and `m_D` / `m_J/ψ` are still un-checked
(deliberately — checking now would be the per-state fit). The refined target is
narrower than this bean states: **lift `windingContent` to carry σ**, rather than
import a `T₃` from the weak `T(3,5)` sector. That work is owned by `qou-mesont3` /
`qou-20sx` / `qou-2udt`; intent posted there.
