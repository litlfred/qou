# Geometric W_λ construction — the index mechanism is Beasley–Witten Seifert–CS localization on S³/2I

**Date:** 2026-06-20
**Branch:** `claude/keystone-wlambda-beasley-witten-localization-2026-06-20`
**Status:** Structural reduction (owner-gated build → published TQFT-localization framework) + a C1 normalization finding. No fitting; no Lean closure claimed.
**Script:** [`scripts/keystone_wlambda_rt_plancherel.py`](scripts/keystone_wlambda_rt_plancherel.py) (arithmetic verified, exit 0)
**Builds on:** [`2026-06-16-keystone-index-necessary-conditions.md`](2026-06-16-keystone-index-necessary-conditions.md) (C1–C7), [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md) (target = q-Plancherel), [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md) (the construction program), [`2026-06-16-s5so3-markov-weighting-sasakian-scope.md`](2026-06-16-s5so3-markov-weighting-sasakian-scope.md) (Wu arena ruled out → S³/2I).

## The open object

The keystone `conj:s5-so3-fiber-action` is reduced to one owner-gated object: a
**Sasakian S¹-equivariant index reproducing the q-Plancherel weights**
`W_λ = d_q(λ)²/[n]_q!`. The corpus already ruled out the finite SU(3)/SO(3) Wu
arena (#2398, #2406) and named the corrected arena — *"the WRT TQFT of S³/2I
(Lawrence–Zagier)"* — but supplied **no index mechanism** connecting that arena
to the `d_q²` weights. This note supplies it.

## The mechanism (no fit)

**`W_λ` is the modular-tensor-category Plancherel measure.** For an MTC `C` (here
`Rep U_q(sl_N)` at the substrate q₀, whose simple objects are the partition
blocks λ), the Reshetikhin–Turaev / Verlinde TQFT assigns the colour-λ sector of
the `S²×S¹` Hilbert space the weight `d_q(λ)²/D²`, where `D² = Σ_λ d_q(λ)²` is
the total quantum dimension squared. This is `d_q² = q-dim End(V_λ)` — exactly
necessary-condition **C4** (block dimensions, not eigenvalues).

**The geometric index producing those weights is Beasley–Witten localization.**
Beasley–Witten, *Non-Abelian Localization for Chern–Simons Theory*
([hep-th/0503126](https://arxiv.org/abs/hep-th/0503126); Witten's earlier
[*Quantization of CS with complex gauge group*] context), prove that the CS
partition function on a **Seifert** 3-manifold `M` (an S¹ V-bundle over a
2-orbifold) **localizes along the Seifert S¹** to a finite-dimensional integral
over the moduli of flat connections, reproducing the RT invariant with quantum-
dimension weights. The Seifert S¹ **is** the Reeb field of the canonical
Sasakian/contact structure on `M`. So *"Sasakian S¹-equivariant index → d_q²
weights"* is precisely Beasley–Witten Seifert-CS localization.

**The arena is S³/2I.** The Poincaré homology sphere `S³/2I` (2I = binary
icosahedral) is Seifert-fibered over the `S²(2,3,5)` orbifold, so it carries the
Seifert/Sasakian S¹ the mechanism needs, and its π₁ = 2I supplies the binary-
icosahedral structure the keystone's `A₅ ⊂ S₅` lifts to (ingredient 1, settled).
Its RT invariant is exactly the Lawrence–Zagier object the ledger's q-side Habiro
note already pointed at. The localization on `S³/2I` is the index the keystone
asks for.

## What this buys against the necessary conditions

The MTC Plancherel measure satisfies all seven necessary conditions
**structurally** (verified arithmetically at q₀, n=5 in the script):

| # | condition | how the RT Plancherel measure meets it |
|---|-----------|----------------------------------------|
| C1 | normalization | see the finding below — `d_q²/D²` is Σ=1 (true Plancherel) |
| C2 | `W_λ = W_{λ'}` | MTC duality `d_q(λ)=d_q(λ')`; exact (max dev 0.0) |
| C3 | positivity | quantum dimensions > 0 (min 0.0078 at n=5) |
| C4 | `d_q²` block dim | the RT weight **is** `d_q² = q-dim End V_λ`, by construction |
| C5 | classical limit | level → ∞: `d_q→d_λ`, `D²→n!`; `Σd_λ²=120=5!` ✓ |
| C6 | full support | every `p(5)=7` sector carries nonzero RT weight |
| C7 | Seifert/Boothby–Wang | `S³/2I` is a closed Seifert 3-manifold (Reeb = Seifert S¹) |

## The C1 finding (genuinely new)

The necessary-conditions doc flagged C1 as *"a one-line owner choice:
`d_q²/[n]_q!` (Σ≈0.982) vs `d_q²/Σd_q²` (Σ=1)."* The localization mechanism
**answers it**: the RT/Verlinde measure the index produces is normalized by the
total quantum dimension `D² = Σ_λ d_q(λ)²`, **not** by `[n]_q!`. Computed at q₀,
n=5:

- `[5]_q! = 131.313`, `D² = Σ d_q² = 128.979`.
- `Σ_λ d_q²/[5]_q! = 0.98222` (the keystone form — not a probability measure).
- `Σ_λ d_q²/D² = 1` (the geometric / RT form — a genuine Plancherel measure).
- gap `D²/[5]_q! = 0.98222` exactly.

So the **geometrically-natural target is `W_λ^{geo} = d_q(λ)²/D²`** (Σ=1), and the
keystone's `[n]_q!` denominator is the convention that differs from it by the
fixed factor 0.98222. The owner choice is resolved in favour of `D²` by the
mechanism: an index/partition-function is a trace over a Hilbert space and is
normalized by that space's total dimension `D²`, never by `[n]_q!` (which is the
`q=1` value of `D²`, equal only in the classical limit).

## Honest scope (critical-distance)

This is a **reduction**, not a from-scratch construction or a closed proof:

- **It supplies the mechanism + arena + C1 answer**, and shows the target
  measure meets C1–C7. It does **not** re-derive Beasley–Witten (a published
  theorem) and does **not** write a Lean proof of ingredient 4's
  *"Reeb-thread = Res^{S₅}_{S₃} restriction functor"* identity — the localization
  gives the *trace/weights*, and the restriction structure is the Bratteli
  branching the localization sum runs over, but the explicit equality at the
  level of the keystone scaffold (`partition_to_rotation` / `GenerationBranchingFunctor.project`)
  is not formalized here.
- **MTC-matching residual.** The localization-Plancherel mechanism is general
  (any MTC). Pinning the specific MTC to the Hecke `Rep U_q(sl_N)` partition
  blocks — i.e. that the gauge group / level on `S³/2I` yields *these* `d_q(λ)`
  and not another category's — is the remaining identification. The arena fixes
  the *2I-equivariance*; the *colouring category* is the gauge datum.
- **210 ppb stays refuted.** Per the icosahedral-reeb scope §"Ingredient 5", no
  natural Wedderburn-projector knob is at the `2×10⁻⁷` scale; this note does not
  touch the muon fine shift (consumer-side: #2520, the frontier carries the
  O(1) generation skeleton, not the fine shift). No fit introduced.

## Net

The owner-gated *"build a Sasakian index from scratch"* is reduced to
*instantiate Beasley–Witten Seifert-CS localization on `S³/2I`*, a published
mechanism whose output — the RT/Verlinde Plancherel measure `d_q²/D²` — meets all
seven necessary conditions and **resolves C1 in favour of the `D²` normalization**.
The genuinely-open remainder is narrowed to (i) the MTC-matching identification
and (ii) the Lean formalization of the Reeb=restriction identity — both sharper
and smaller than the original "construct the index."
