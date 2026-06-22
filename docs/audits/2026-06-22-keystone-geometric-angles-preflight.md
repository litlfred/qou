# Geometric angles made explicit + the W_λ target reproduced — the equivariant-index preflight

**Date:** 2026-06-22
**Branch:** `claude/keystone-geometric-angles-wrt-2026-06-22`
**Status:** Positive preflight — the geometric angles are now explicit and exactly validated; the
W_λ target is reproduced; the q-vs-classical structural gate is identified. No fit, nothing wired.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Owner-authorized:** the four-path geometric exploration (angles / WRT / McKay / Lean).
**Script:** [`scripts/keystone_geometric_angles_preflight.py`](scripts/keystone_geometric_angles_preflight.py)

## What this delivers

Three of the four owner-picked paths, in their computable form (the deep WRT/Lawrence–Zagier target
is a separate follow-up). It makes the owner-gated `irrepToRotation` angles of
`S5SO3FiberAction.lean` **explicit**, reproduces the forced `W_λ` target, and records the McKay/E₈
algebraic shadow.

## (1) The explicit geometric angles — exactly validated

A₅ ≅ icosahedral rotation group I ⊂ SO(3). The five conjugacy classes are rotations by definite
angles (class sizes sum to 60):

| class | size | angle |
|-------|------|-------|
| e | 1 | 0° |
| 2-fold | 15 | 180° |
| 3-fold | 20 | 120° |
| 5-fold | 12 | 72° |
| 5′-fold | 12 | 144° |

**SO(3)-restriction validation (parameter-free, exact):** the A₅ irreps T₁ and H are the
restrictions of the SO(3) spin-ℓ irreps ℓ=1 and ℓ=2. The character formula
`χ_ℓ(θ)=sin((2ℓ+1)θ/2)/sin(θ/2)` reproduces the A₅ character table to **5×10⁻⁴¹** (machine zero),
with the signature identity

$$\chi_{\ell=1}(72°)=1+2\cos 72° = \tfrac{1+\sqrt5}{2}=\varphi,\qquad |\chi-\varphi|=0.0\ \text{(exact)}.$$

So the angle assignment is *not* a free input — it is forced by the icosahedral group theory, and
the golden ratio is the exact fingerprint.

**The explicit per-irrep Reeb phase** `θ_λ = arccos(χ_λ(5-fold)/dim_λ)`:

| irrep | dim | χ(5-fold)/dim | θ_λ |
|-------|-----|---------------|-----|
| A | 1 | 1.0 | 0° |
| T₁ | 3 | 0.5393 | 57.36° |
| T₂ | 3 | −0.2060 | 101.89° |
| G | 4 | −0.25 | 104.48° |
| H | 5 | 0.0 | 90° |

These are the explicit values the owner-gated `irrepToRotation` map asserts exist
(`irrepToRotation_inj`); here they are computed.

## (3) The W_λ target — reproduced

`W_λ = d_q(λ)²/[n]_q!` (q-Plancherel / Ocneanu measure), via the balanced-q-integer hook-length
formula, at q₀ for n=5 — self-checked against
[`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md):

| λ | d_q(λ) | W_λ | role |
|---|--------|-----|------|
| (3,1,1) | 6.2204 | **0.29467** | electron |
| (3,2) | 5.2204 | **0.20754** | muon |
| (2,2,1) | 5.2204 | 0.20754 | (3,2)-twin |
| (4,1) / (2,1,1,1) | 4.1097 | 0.12862 | — |
| (5) / (1⁵) | 1.0 | 0.00762 | — |

`[5]_q! = 131.313` ✓ — matches the scope doc exactly.

## The structural gate this preflight exposes

**The angles are q-independent; W_λ is q-deformed.** The geometric angles above are pure (classical,
q=1) icosahedral group theory — they carry no q₀. The target `W_λ` is a genuinely q-deformed measure
(it depends on q₀; in the balanced convention `Σ_λ W_λ = 0.982 ≠ 1`, while the per-block values match
the corpus exactly). Therefore **the angles alone cannot produce W_λ** — any bridge `index = W_λ`
must itself be **q-deformed**. This is exactly why the corpus's own redirect
([`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md)
SUPERSEDED banner, #2406) abandons a *classical* finite Sasakian index and points at the **WRT TQFT
of S³/2I (Lawrence–Zagier)** — a q-deformed (Habiro-ring) invariant. The preflight thus **confirms the
direction**: the geometric data is classical and exact, but the W_λ-producing functor lives at the
q-deformed (WRT/Habiro) level, not the classical-angle level.

## (4) McKay / E₈ shadow

2I (binary icosahedral) is the McKay group of affine Ê₈: its irrep dimensions are the E₈ Coxeter
marks `{1,2,3,4,5,6,4,2,3}` (Σ=30=Coxeter number h). The A₅=I irreps (the SO(3) quotient) have dims
`[1,3,3,4,5]` (Σ dim²=60). The equivariant index over the C²/2I ALE resolution yields the E₈ marks as
Perron–Frobenius weights — the *finite, classical* shadow. The q-deformed lift of this (the WRT
invariant) is the target the next probe attacks.

## Net + next

- **Delivered:** the geometric angles are explicit and exactly validated (the φ pin); W_λ reproduced;
  the q-vs-classical gate identified; McKay/E₈ shadow recorded.
- **Confirmed direction:** the W_λ-producing bridge is q-deformed (WRT/Habiro), not a classical index —
  consistent with the corpus redirect.
- **Next (follow-up):** the WRT TQFT of S³/2I (Lawrence–Zagier) — does its q-series reproduce W_λ? —
  and a Lean formalization of the W_λ target + the exact angle/φ validation.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## (2) WRT / Lawrence–Zagier — the index = W_λ object dissolves into modular data

**Script:** [`scripts/keystone_wrt_modular_weight_probe.py`](scripts/keystone_wrt_modular_weight_probe.py)

Following the q-deformed gate above, the corpus redirect names the WRT TQFT of S³/2I. Making it
precise yields a reframing that is more useful than the original "do differential geometry" wording.

**The structural identity.** In a modular tensor category the natural weight of block λ is
`P_λ = d_λ²/D²` with `D² = Σ_μ d_μ²` the global quantum dimension — the *same form* as the target
`W_λ = d_q(λ)²/[n]_q!`. So `index = W_λ` reframes to: **`[n]_q!` is the global quantum dimension of
the relevant TQFT block system.** Testing that identification directly:

| n | `D² = Σ d_q²` | `[n]_q!` | `D²/[n]_q!` |
|---|---------------|----------|-------------|
| 3 | 6.0437 | 6.1206 | 0.98744 |
| 5 | 128.979 | 131.313 | 0.98222 |

So `W_λ` is the modular block weight `d²/D²` **up to the fixed factor `D²/[n]_q! ≠ 1`**, and the gap is
*explained*: the q-dimension `d_q(λ)` is the Markov trace of `1`, **not** the irrep dimension `f^λ`;
the classical identity `Σ(f^λ)² = n!` q-deforms to `Σ d_q² = D² ≠ [n]_q!`. (This is also why
`Σ_λ W_λ = 0.982 ≠ 1` — `W_λ` is a Markov-trace weight, not a probability measure.)

**Type-correct verdict.**
- `index = W_λ` reframes to: **`W_λ` are the modular-tensor-category block weights** of the SU(2)-type
  TQFT, up to the fixed factor `D²/[n]_q!`.
- The Poincaré sphere `S³/2I` (Seifert `(2,3,5)`, E₈ lattice; Lawrence–Zagier 1999) is the **geometric
  selector** of the icosahedral modular data — but its WRT invariant is *one q-series per level*, not the
  λ-family `W_λ`. So **`WRT(S³/2I) = W_λ` is a type mismatch and is NOT claimed.**
- **The genuine open content, now sharply posed:** pin the level/category whose quantum dimensions are the
  `d_q(λ)` above and whose global dimension `D²` supplies the normalisation — *then* `W_λ` is its block
  measure. This is **representation-theoretic (modular data), not finite-Sasakian geometry** — the
  q-deformed home the corpus redirect named, now made precise. The keystone's "owner-gated geometric
  object" is thereby reframed from Sasakian existence to **modular-category identification**, a more
  tractable target.

## Cross-references

- [`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md) — the forced W_λ target + the WRT/Habiro redirect (SUPERSEDED banner).
- [`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md) — the Reeb-phase `θ_λ=arccos(χ/dim)` identification.
- [`2026-06-22-keystone-geometric-level-route-reduction.md`](2026-06-22-keystone-geometric-level-route-reduction.md) — the route reduction this explores beyond.
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — the `irrepToRotation` map made explicit here.
