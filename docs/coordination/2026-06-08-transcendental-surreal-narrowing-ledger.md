# Transcendental-conjecture surreal-narrowing ledger

**Date:** 2026-06-08 · **Branch:** `claude/vigilant-fermat-SROph` · **PR:** #1995
**Status:** living ledger. Realizes the owner's directive — *"even if we can
narrow the transcendental conjectures to a statement on surreals in QOU, that is
worthwhile even if not able to prove the last bit; take the approach wherever
appropriate."*

## The approach (one line)

For each QOU transcendental conjecture, use the **surreal / iterated-integral
depth grading** to factor it into

```
   [ surreal-graded narrowing — provable / structural in QOU ]
                       +
   [ open residue — a NAMED external transcendence input ]
```

The narrowing is the worthwhile product even when the residue stays open. This
mirrors the keystone, which is already a *reduction* device (depth-2 theorem;
depth-≥3 reduced to Goncharov), not a proof engine.

## Classification axis (from the rank-2 probe)

Each narrowing is tagged by whether surreals are **essential** or **language**:

- **L (language):** the narrowing is single-axis / rank-1 (`ε`-powers only); the
  surreal statement re-describes an ordinary real asymptotic. Surreals are
  convenient, not necessary.
- **E? (essential candidate):** the narrowing involves `ε^ℓ` with `ℓ → ω`
  (infinitesimal to an infinite power) or an independent geometric divergence —
  an infinite-value-group object the `ε`-adic `ℝ` line cannot express. Surreals
  may be necessary. Decided by the finite-page-vs-perpetual check
  ([rank-2 probe](../audits/2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md)).

## The ledger (period / volume cluster — pass 1)

| # | Conjecture | Surreal-graded narrowing (the worthwhile part) | Open residue (named external input) | Surreal? |
|---|---|---|---|---|
| 1 | [`gb-depth-period-correspondence`](../../content/quantum-observable-universe/mass-theory/gb-depth-period-correspondence.md) (keystone) | `τ_arch(G^(n)(ℋ_q)) ⊆ 𝒫_n`, sharp. **Depth-2 = THEOREM** (Bloch–Suslin). | Goncharov motivic (depth≥3); Beilinson (depth≥4) | L (proof is K-theoretic) |
| 2 | [`depth-2-identification-bloch-suslin`](../../content/quantum-observable-universe/appendix-surreals/depth-2-identification-bloch-suslin.md) | `G^(2)/𝒫_1 ≅ K_3^ind(F)⊗ℚ` via Bloch group + Suslin + Borel | — (proved at depth 2) | L |
| 3 | [`qou-infra-discharges-goncharov-zeta5`](../../content/quantum-observable-universe/appendix-surreals/qou-infra-discharges-goncharov-zeta5.md) | 22-term relation at `ζ₅` = Markov trace of an explicit Hecke `β`, NF-reduces mod depth-2 ⇒ discharges Goncharov at `ℚ(ζ₅)` | the P2 specialization-commutes lemma + the pruned β-search ([Avenue B scaffold](../workplans/2026-06-08-zeta5-goncharov-avenue-b-scaffold.md)) | L |
| 4 | [`kashaev-surreal`](../../content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md) | `std`-part identity separating the algebraic (`tr_M`) from the transcendental (`Vol`) part of the volume conjecture | Volume Conjecture (open) | **L** (`q=e^{2πi/N}` ties the scales → rank-1) |
| 5 | `hyperbolic-volume-transcendence` (jet-order tower) | **Narrowed to finite-base-order by [PR #1990](https://github.com/litlfred/qou/pull/1990)** (jacobian rank = 3 at every `N≥3` via rank-monotonicity) — residual = surreal-bridge inputs I2/I3 only | I2 holonomy-shadow + I3 monodromy-shadow (physical, conjectural) | **L** — finite-page degeneration ⇒ rank-1 (a *worked instance* of the probe's rank-1 side) |
| 6 | [`two-filtration-bridge`](../../content/quantum-observable-universe/stochastic-mechanics/two-filtration-bridge-small-cases.md) | bar-class ⇒ depth: self-conjugate `λ`→depth 2 (`CS=0`), chiral pair→depth 3 (`CS≠0`); verified `n≤4` | general `n≥5` Vol/CS dictionary | L |
| 7 | [`dilogarithm-archimedean-limit`](../../content/quantum-observable-universe/mass-theory/dilogarithm-archimedean-limit.md) | `(1−q)·log Φ_n(x;q) → Li₂(x)` (Faddeev scaling); `q→1⁻` regime **proved elementary** | branch-cut compatibility on principal `Li₂` at `q→1⁺` + Mathlib Tauberian | L (single-`ε` rescaling ⇒ rank-1) |
| 8 | [`cs-evaluation-faithfulness`](../../content/quantum-observable-universe/predicted-spectra/cs-evaluation-faithfulness.md) | `κ_n≠0 ⇒ Φ_n≠0`: each volume grade non-degenerate; `Vol=Σ_nΦ_n` perpetual but **Mostow-convergent** | arithmetic independence of `{Φ_n}` (open) | **the `ε^ω` row** — narrows to "depth-`ω` tail"; resolved **L** by Mostow (see probe §RESOLUTION) |
| 9 | [`observables-algebraic-independence`](../../content/quantum-observable-universe/observations/observables-algebraic-independence.md) | no algebraic relation over `ℚ(q₀)` among `(m_p,m_n,m_Λ,…)`; 5 falsifiable classes (lattice ratios cleanest) | the transcendence itself (open; lattice `10⁻⁶` test) | L |
| 10 | [`kashaev-surreal`](../../content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md) — **Möbius-energy narrowing** (NEW, via [`lem:jones-mobius-diagonal`](../../content/quantum-observable-universe/climax-volume-mass/jones-mobius-diagonal.md)) | (a) **Embedding:** the fundamental Jones polynomial **is** the Möbius contact term, `J_K = T_reg − E_cat` (`tr_M = ` diagonal of the categorical 2-point kernel; PROVED in Lean from the Frobenius–Hopf kernel collapse + Jones–Markov). (b) **Bound:** the transcendental `Vol(K)` (= Kashaev target, row 4) is squeezed below a finite computable quantity, `Vol(K) ≤ c₀·E(K)` with `c₀ = v_oct/2π` explicit, via FHW `E ≳ 2π·c(K)` + Lackenby `Vol ≲ v_oct·c(K)`. | sharpness of the FHW / Lackenby constants off alternating knots; the Volume-Conjecture limit (= row 4 residue) | **L** (crossing-number bound = finite real constants; the embedding is the `N=2` rung — rank-1) |

> **Row 10 note.** Row 10 narrows the *same* Kashaev conjecture as row 4, but
> from the **Möbius / geometric-energy side** rather than the `std`-part side.
> Its distinctive product is the embedding (a): the surreal recast `E_cat =
> std(I₁−I₂)` ([`rem:mobius-surreal-renormalization`](../../content/quantum-observable-universe/appendix-surreals/mobius-surreal-renormalization.md))
> shows `I₁` (2-point) and `I₂` (contact) share the `ω^{+1}` leading divergence,
> and `lem:jones-mobius-diagonal` identifies that shared divergence with `J_K`.
> So Jones (Kashaev's `N=2` base) ↪ Möbius as the contact term — a *structural*
> link between two QOU transcendentals, surreal-graded but still **L** (the
> bound's constants are finite reals).

## The ledger (millennium-problem cluster — pass 2, 2026-06-09)

Retires the speculative `*-surreal-bound` framing: each former "bound" block is
re-indexed here as a narrowing row (narrowing + named residue + L/E? tag). The
blocks themselves stay as the worked statements; this is the re-scoped index.

| # | Conjecture (block) | Surreal-graded narrowing (the worthwhile part) | Open residue (named external input) | Surreal? |
|---|---|---|---|---|
| 11 | [`bsd-surreal-bound`](../../content/quantum-observable-universe/appendix-surreals/bsd-surreal-bound.md) → `conj:q-birch-swinnerton-dyer` | `ord_ω(L(𝓔_q,1+δ)) = r·ord_ω(δ)` — order-of-vanishing = Mordell–Weil rank `r` as a surreal `ω`-order identity; the squeeze forbids a hidden zero of order `> r` | the spectral `L`-value ↔ Reeb-period identification; BSD itself (rank = ord of vanishing) | L (single-`ε`, rank-1) |
| 12 | [`rh-surreal-bound`](../../content/quantum-observable-universe/appendix-surreals/rh-surreal-bound.md) → `conj:classical-riemann-hypothesis` | a rogue zero at `Re=½+δ` costs `E(δ) ≍ δ²·ε⁻¹`, exceeding the mass-gap budget `ε³` by `ε⁻⁴` — off-critical-line zeros are surreal-order-forbidden | Hasse–Weil alignment at every prime fibre; RH itself | L (single-`ε`, rank-1) |
| 13 | [`yang-mills-surreal-bound`](../../content/quantum-observable-universe/appendix-surreals/yang-mills-surreal-bound.md) → YM mass-gap | `Δ_q ≍ ε³ > 0` **is** the categorical mass gap (`ord_ω(Δ_q) = −3 > −∞ = ord_ω(0)`); definitional content of the substrate, not an auxiliary claim | identification of the categorical `Δ_q` with the physical `SU(N)` YM gap on `ℝ⁴`; massless-glueball exclusion | L (finite `ε`-order) |
| 14 | [`p-vs-np-surreal-bound`](../../content/quantum-observable-universe/appendix-surreals/p-vs-np-surreal-bound.md) → `conj:p-vs-np-qou` | classical simulation `2ⁿ·δ²·ε⁻¹` exceeds the classical budget `2ⁿ·ε³` by a full `ω`-order (`ord_ω = 1 > −3`); `st_{ε→0}` collapses the transfinite speed-up ⇒ `P≠NP` propagates from the quantum separation | **conditional** on `P ⊊ BQP_q` at positive `ε` (non-compressibility, Freedman TQC); Cook–Levin preservation | **L — conditional** (the one conditional row) |
| 15 | [`collatz-surreal-bound`](../../content/quantum-observable-universe/appendix-surreals/collatz-surreal-bound.md) → `conj:q-collatz` / `prop:collatz-no-cycles` | a rogue orbit's accumulated contact-volume `V(δ) ≍ δ²·ε⁻¹ > Δ_q ≍ ε³` (`ord_ω = 1 > −3`) ⇒ no rogue cycle / unbounded hailstone survives the squeeze | contact-boundary ↔ integer-orbit translation faithfulness (q-Collatz as skein resolution); Collatz itself | L (single-`ε`, rank-1) |

> **Pass-2 note.** All five are **rank-1 (L)**: each lives in the `ε`-adic line
> `ℝ(ε) ⊂ No` (a single valuation, finite `ε`-powers), so the surreal statement
> re-describes an ordinary real asymptotic — surreals are the *convenient
> language*, not load-bearing. P-vs-NP is additionally **conditional** (rides on
> the `BQP_q` non-compressibility input). Combined with pass-1 and the resolved
> essential candidate below, **every** ledger row is now **L** — the corpus
> carries no surreal-*necessary* narrowing. (See the keep/purge reading: keep as
> the narrowing language; nothing is load-bearing on surreals.)

## The ledger (Bring-trilog / ζ₅ depth-3 chain — pass 3, 2026-06-09)

Folds in the remaining `## Next passes` candidates. Rows 16–19 are the depth-3
chain that narrows B1's `ℚ(ζ₅)` row to a single PSLQ-certified element
(complements row 3, `qou-infra-discharges-goncharov-zeta5`). The other named
candidate, `cs-evaluation-faithfulness`, is **already row 8** (the volume-tower
faithfulness / `ε^ω` row) — not re-indexed here.

| # | Conjecture / proposition (block) | Surreal-graded narrowing (the worthwhile part) | Open residue (named external input) | Surreal? |
|---|---|---|---|---|
| 16 | [`bring-trilog-imaginary-tate-rational`](../../content/quantum-observable-universe/mass-theory/bring-trilog-imaginary-tate-rational.md) (**prop**) | `Im Li₃(ζ₅) = 4π³/125` is **Tate-rational** (PROVED, 50 dps Kummer reflection) ⇒ projects to 0 under the Beilinson quotient `𝒫₃ → 𝒫₃/Tate` — kills the imaginary part, leaving only `Re = Cl₃(2π/5)` as new depth-3 info | transcendence/newness of the real part `Cl₃(2π/5)` (rows 17–19) | L (Tate-rational identity, single-level) |
| 17 | [`cl3-zeta5-geometric-realization`](../../content/quantum-observable-universe/mass-theory/cl3-zeta5-geometric-realization.md) (**conj**) | identifies `Cl₃(2π/5) = Re Li₃(ζ₅)` as a depth-3 element of `𝒫₃/𝒫₂` (Goncharov filtration) at the `S₅`-Bring-natural input `ζ₅`; supplies a candidates list for its geometric realisation | **which** geometric/topological invariant realises it (open) | L (depth grading; `ζ₅` scales tie ⇒ rank-1, as rows 3/4) |
| 18 | [`cl3-zeta5-orbit-sum-identity`](../../content/quantum-observable-universe/mass-theory/cl3-zeta5-orbit-sum-identity.md) (**prop**) | orbit-sum identity (PROVED) reduces the 4 grouplike `Li₃(ζ₅^k)` to a **1-dim antisymmetric generator** `X = Cl₃(2π/5) − Cl₃(4π/5)`; the real-part sum is `ζ(3)`-fixed | transcendence of the 1-dim generator `X` (row 19) | L |
| 19 | [`cl3-zeta5-pslq-independence`](../../content/quantum-observable-universe/mass-theory/cl3-zeta5-pslq-independence.md) (**prop**) | PSLQ (50 dps, coefficient-norm `10⁸`) certifies `X` has **no `ℚ`-linear relation** with standard weight-3 periods — strong evidence `X` is genuinely-new depth-3 | the transcendence proper (PSLQ is bounded-norm *evidence*, not proof); the depth-3 Goncharov question (row 1) | L (numerical narrowing) |

> **Pass-3 note.** All four continue the all-L pattern: the depth-3 chain
> (16–19) lives in the `ζ₅`-scaled depth filtration (rank-1, like row 3). The
> corpus's narrowing ledger now covers the period/volume cluster (1–10), the
> millennium cluster (11–15), and the Bring-trilog/ζ₅ depth-3 chain (16–19) —
> **every row L.**

## The essential candidate — RESOLVED to *language* (2026-06-08)

The GS-tower compounding of the non-abelian-Stokes quadratic term was the one
rank-≥2 / `ε^ω` candidate. It is **settled** by the two-tower reading
([probe §RESOLUTION](../audits/2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md)):

- **Mass / GS tower collapses at E₁** ([`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/mass-theory/spectral-sequence-collapse.md),
  Whitehead / semisimple) → finite-order in `ε` → rank-1 → surreal-free. Production
  never needs surreals. **Rigorous by a standard cited result (2026-06-09):** the
  collapse is Whitehead's lemma (`HH^{≥1}=0` for semisimple `A`, Cartan–Eilenberg);
  the Lean sibling is sorry-free and encodes the structure (`WhiteheadHH` as a
  *cited axiom-class* via `-- Ref: [cartan1956]`, since Mathlib has no Hochschild
  framework), so the finite-page leg is settled *by citation*, **not** a
  from-scratch Lean proof — see
  [finite-page-vs-perpetual settle](../audits/2026-06-09-finite-page-vs-perpetual-settle.md).
- **Volume / lifting tower is genuinely perpetual** (`motivic-perpetual-obstruction`,
  `cs-evaluation-faithfulness`: `κ_n≠0 ∀n`) — the real `ε^ω` structure — **but
  Mostow rigidity makes `Vol=Σ_nΦ_n` converge** to a real value, so the
  infinitude is in the *grading*, not the *value*. No `ε^ω` element is *forced*.

**Verdict: `ε^ω` is the worthwhile *narrowing language* for the perpetual
obstruction (row 8), not a necessity.** Surreals are kept **as language**.

## Reading of the ledger (for the keep/purge decision)

- **By the owner's narrowing criterion, surreals already pass** (rows 1–6 are
  genuine reductions of open transcendental problems to named residues — the
  worthwhile product). ⇒ **keep, re-scoped as this ledger**, not as
  "millennium-problem bounds."
- **Surreal *necessity* is now resolved: language, not load-bearing** (the one
  `ε^ω` candidate settled to L by E₁-collapse + Mostow convergence, 2026-06-08,
  above). The ledger is the *language* in which the narrowings are written —
  still worthwhile per the owner's criterion; no theorem requires surreals.
- **Either way the speculative `*-surreal-bound` millennium framing is the part
  to retire** — replace each with its ledger row (narrowing + named residue).

## Next passes — DONE (2026-06-09)

All originally-named candidates are now folded into rows:
`dilogarithm-archimedean-limit` (row 7), `observables-algebraic-independence`
(row 9), `cs-evaluation-faithfulness` (already **row 8**),
`bring-trilog-imaginary-tate-rational` (row 16), `cl3-zeta5-*` (rows 17–19).
The ledger now spans the period/volume (1–10), millennium (11–15), and
Bring-trilog/ζ₅ depth-3 (16–19) clusters — **every row L**.

**Standing rule (not a backlog item):** any *new* transcendental conjecture added
to the corpus gets a ledger row (narrowing + named residue + L/E? tag). Do **not**
fabricate a residue — read the block first (corpus-grep discipline). If a future
candidate is **not** rank-1 (an `ε^ℓ`, `ℓ→ω` value manipulated as an element),
re-open the necessity question via the
[rank-2 probe](../audits/2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md).
