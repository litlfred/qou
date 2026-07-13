# Geometric `W_λ` derivation — the McKay 2I↔Ê₈ value-map route (gate open for explore)

**Date:** 2026-07-12 · **Axis:** s5-so3 keystone geometric `W_λ` (owner opened gate for exploration,
"no fit, derivation needed") · **Branch:** `claude/keystone-wlambda-derivation-2026-07-12` ·
**No fit; no physics claim; does not close the gate.**

## Where the derivation actually stands (corpus-grep, not a fresh start)

The owner opened the geometric `W_λ` gate for exploration. The correct starting point is **not** a
blank slate — the frontier is already pinned to **one precise open step** by existing merged compute.
Reading the corpus first (AGENTS.md corpus-grep discipline):

1. **`W_λ = d_q(λ)²/D² = |S_{0λ}|²`** is the Verlinde / q-Plancherel measure — the squared modular-S
   vacuum row. Its three consistency obligations C1 (Σ=1), C2 (`W_{λ'}=W_λ`), C6 (`>0`) are
   **Lean-proved** at the physical `n=4,5` blocks
   ([`WLambdaMTCLocalizationObligation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean),
   [`KeystoneWLambdaPhysicalBlocks.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneWLambdaPhysicalBlocks.lean)) —
   but those files **assume** the localization matches `d_q²/D²` (the `loc_matches` field). That
   assumption *is* the gate.

2. **The bare WRT(Σ(2,3,5)) is one number** — the Lawrence–Zagier false theta `Ψ(1/q₀)=2.3296`
   ([`keystone_habiro_wrt_s3_2i_probe.py`](scripts/keystone_habiro_wrt_s3_2i_probe.py)) —
   the wrong *type* for the λ-family `W_λ` (a scalar vs an S-matrix row). No `Ψ=W_λ` asserted (numerology trap).

3. **The colored Σ(2,3,5) family exists and is E₈-indexed**
   ([`keystone_colored_sigma235_wrt.py`](../../computations/probes/keystone_colored_sigma235_wrt.py)):
   coloring the order-5 icosahedral fibre by SU(2) colour `α` shifts the false-theta support
   `30(1±½±⅓±α/5) (mod 60)`. `α=1 → {1,11,19,29}` (= the **H₄ exponents**, bare); `α=2 → {7,13,17,23}`
   (the complement); the two lowest colours generate **all 8 E₈ exponents** `{1,7,11,13,17,19,23,29}`
   (`P=2·3·5=30=h(E₈)`). The 4 E₈ dual pairs `{e,30−e}` match the 4 bwS0 conjugation classes `λ↔λ'`
   (count 4↔4). **But the naive value map `d_q(λ) = [e]_q` (exponent quantum dimension) is REFUTED** —
   the ratio `d_q/[e]_q` is non-constant `(1.000, 0.539, 0.385, 0.359)`.

**The single open derivation step, verbatim from that probe:** *"the exact colour-α → partition-λ
assignment and the S-matrix normalization (D) that turns Ψ^{(α)} into bwS0(λ) — the genuine colored
Lawrence–Rozansky S-matrix amplitude (the real remaining derivation)."*

## Why NOT another root-of-unity `|·|²` check (anti-re-walk)

My own #3652 frontier-sharpening (recorded in the s5-so3 ledger) proved: any framed amplitude
`S_{0λ}·θ_λ^{f}` breaks the conjugation symmetry `d_q(λ)=d_q(λ')` has, **unless `|θ_λ|=1`** — i.e.
at a fibre root of unity, where the framing is a phase and `|S_{0λ}θ_λ^f|²=|S_{0λ}|²=W_λ` (the
Verlinde-measure definition, already shown at `|q|=1` in #3677). So a fresh finite-level `|·|²`
compute would only **re-confirm** the framing cancellation — the ledger explicitly warns *"do not
re-chase framing-cancellation as if it were new tractable ground."* The genuine open content is the
**value map** (which E₈ exponent / colour ↔ which λ, and the S-matrix amplitude), not another modulus.

## The route this branch explores: McKay 2I ↔ Ê₈, no fit

The value map is a **representation-theory** problem with a canonical, parameter-free answer:

- **McKay correspondence.** The binary icosahedral group `2I = ⟨2,3,5⟩` (the `S³/2I` fibre group) has
  its irreducible representations in bijection with the nodes of the **affine `Ê₈` Dynkin diagram**;
  the non-trivial nodes carry the **E₈ exponents** `{1,7,11,13,17,19,23,29}` (Coxeter number 30). This
  is *exactly* the E₈-exponent index set the colored-WRT family (probe 3) carries — so the colour-`α`
  index of the Seifert fibre insertion is the **2I-irrep / Ê₈-node** label, not a free choice.
- **The S-matrix amplitude, not `[e]_q`.** The colored Lawrence–Rozansky amplitude of a Seifert
  homology sphere with a Wilson line on the exceptional fibre is a genuine **S-matrix** object
  `∝ S_{λμ}/S_{0μ}`-weighted Seifert sum — *not* the false-theta scalar and *not* the exponent's bare
  quantum dimension `[e]_q` (refuted). The derivation target is: does the McKay-dictionary'd colored
  amplitude's value map reproduce `bwS0(λ)=d_q(λ)/D`?
- **A₅⊂S₅ branching.** The framework's `W_λ` blocks are `λ⊢5` (full Hecke `S₅`); the icosahedral
  `A₅≅2I/{±1}` acts through `A₅⊂S₅`. The colour(2I-irrep)→λ(S₅-partition) dictionary factors through
  the McKay Ê₈ labels and the `A₅⊂S₅` induction/restriction — a fixed representation-theoretic map,
  zero parameters.

**This is no-fit by construction:** McKay is a bijection, the S-matrix amplitude has no free constant,
and the A₅⊂S₅ branching is fixed. Either the composed value map reproduces `d_q(λ)/D` (a genuine
geometric derivation of the measure) or it does not (a sharp, quantified negative that supersedes the
refuted `[e]_q` map) — both outcomes are honest and advance the frontier.

## Result — the value map is `[mark]_q`, EXACT (no fit)

[`keystone_mckay_e8_valuemap.py`](../../computations/probes/keystone_mckay_e8_valuemap.py) /
[witness](../../computations/keystone-mckay-e8-valuemap.witness.json). Structural checks pass
(Σ marks = 30 = h(E₈) = P; Σ dim² = 120 = |2I|; A₅-factoring marks {1,3,3′,4,5}, Σdim² = 60 = |A₅|).
The explicit dictionary (McKay node ∘ A₅⊂S₅):

| bwS0 class `{λ,λ′}` | A₅/McKay mark | node | value `d_q(λ)` |
|---|--:|---|---|
| `{(5),(1⁵)}` | 1 | trivial | `[1]_q = 1` |
| `{(4,1),(2,1,1,1)}` | 4 | A₅ standard | `[4]_q` (= standard-rep thm #3640) |
| `{(3,2),(2,2,1)}` | 5 | A₅ 5-dim | **`[5]_q`** (new exact identity) |
| `{(3,1,1)}` self-conj | 6 (= 3+3′) | A₅ **split** | **`[5]_q + 1 = [3]_q[4]_q/[2]_q`** (not `[6]_q`) |

**The value map is `d_q(λ) = [mark]_q`, EXACT at generic `q`** (machine-zero to 60 dps at both `q₀`
and a second generic `q = 1.37` ⇒ a polynomial identity in `q`, not a `q₀` accident) for the **three
unsplit** A₅-McKay nodes. The **single deviation** is at the self-conjugate **electron** block
`(3,1,1)` — the A₅ `3⊕3′` split node — where `d_q = [5]_q + 1 = d_q((3,2)) + 1` exactly (the `+1` is
the split signature), **not** `[6]_q`.

**This resolves the refuted `[e]_q` map** (`keystone_colored_sigma235_wrt`): its error was indexing by
the wrong E₈ datum. The false-theta support is E₈-**exponent** indexed `{1,7,11,13,…}`; the **value**
lives on the E₈ **mark** (Coxeter label of the McKay node) `{1,3,4,5,…}`. Exponents ≠ marks. With the
correct index, `bwS0(λ) = [mark]_q / D` — a single global normalizer `D = √Σd_q²`, no per-block
tuning, no fit.

The generic-`q` identities `d_q((3,2)) = [5]_q` and `d_q((3,1,1)) = [5]_q + 1` are hook-formula
consequences (`[5]_q!/([4]_q[3]_q[2]_q[1]_q[1]_q) = [5]_q`; `[5]_q!/([5]_q[2]_q[2]_q[1]_q[1]_q) =
[3]_q[4]_q/[2]_q`) and are formalize-first Lean targets alongside the proved standard-rep identity.

**Still open** (not touched by this result): the colored Lawrence–Rozansky amplitude itself (deferred —
formula not rigorously pinned this pass) and the archimedean `q₀`-continuation of the whole vacuum row
(the #3681 Habiro/Stokes carriers). The value map derived here is at the categorical/`q`-algebraic
level; the `q₀`-observable passage is the orthogonal residual.

## Scope (STRICT — anti-laundering)

This branch **explores** the value-map derivation; it does **not** close the gate and wires **no**
constant to production (AGENTS.md §"Axiomatization is NOT a Proof"; §"open for all" grants permission
to *derive*, not to pass a fit as a derivation). The archimedean `q₀`-continuation residual (the
Habiro/Stokes carriers of #3681) is orthogonal and unchanged. No fit; no `Ψ^{(α)}=W_λ` numerology.
