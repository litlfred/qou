# c₃ bar-odd S via the tetraplectic → Bruhat → Young → partitions reduction of Φ_b

**Date:** 2026-07-11 · **Axis:** Q_β c₃ (bar-odd part `S`) · **Branch:**
`claude/faddeev-phi-b-construction-e26myp` · **Tier:** structural reduction +
target characterization (scope-(a)). **Owner-directed Subgoal-2 exploration.**
**No c_k wired; registry untouched; flip-flop guard §8 respected; C14 anti-fitting.**

## The decision (owner-directed)

Closing c₃'s bar-odd part `S` = building the Faddeev **non-compact** `Φ_b`
(modular double; `sinh(zb)sinh(z/b)` kernel; self-dual `Φ_b = Φ_{1/b}`) and
finding the argument that reproduces the two `S`-values. Two routes were on the
table:

1. **Raw contour-integral machinery** — evaluate `log Φ_b` as the Faddeev
   integral directly. No Mathlib support; the `q₀ > 1` substrate regime needs
   `arg b = −π/4` analytic continuation (open); research-grade to formalize.
2. **Combinatorial evaluation** — reduce the contour integral by residues to a
   **finite q-sum over partitions**, landing on the framework's existing
   Hecke → Wedderburn (λ ⊢ n) → `tr_M` spine.

**Owner chose route 2, with the explicit reduction chain**

> contour integral → tetraplectic → Bruhat cell → Young diagram → partitions →
> combinatorial

This doc records that chain, verifies its combinatorial core, states the
*proposed* structural identification for `S`, and names the plug-in point into
the non-abelian (Yekutieli) Stokes step. It does **not** propose a c_k value or
fit anything.

## Existing corpus for Φ_b (checked — the object already exists)

| artifact | what it supplies | status |
|---|---|---|
| [`phi_b_evaluator.py`](../../computations/qbeta/phi_b_evaluator.py) | validated Faddeev integral `log Φ_b(z)=∫_{ℝ+iδ} e^{−2izw}/(4w·sinh(wb)·sinh(w/b)) dw`; V1–V6 battery, literature-verified vs Hikami math/0604094 | **built** |
| [`FaddeevModularDouble.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FaddeevModularDouble.lean) | structural axiomatisation: modular invariance `Φ_b=Φ_{1/b}`, Faddeev inversion, σ-unitary phase lemmas | **sorry-free** |
| [`prop:phi-b-unitary-bar-odd`](../../content/quantum-observable-universe/mass-theory/phi-b-unitary-bar-odd.md) | `|Φ_b|=1` on the fibre saddle ⇒ `Φ_b` is a bar-ODD (phase) carrier | content block |
| [channel-separation spec](2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md) | the `c_3` swing is a **phase-channel** quantity; PR #1821's smooth-real wall is magnitude-channel only | scope-(a) |
| [`…-barodd-sleak-phib-target.md`](../audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md) | the exact target: `S(muon)=+0.00968298`, `S(proton)=−0.03945936`, sign-flip | measurement |

So the numerical Φ_b **already exists and is validated**; what is missing is the
*combinatorial* form that (a) evaluates at the substrate anchors without the
divergent `|q₀|>1` product, and (b) plugs into the Hecke/λ spine.

## The exact target (must be reproduced by any S-derivation)

`S = c₃ + Vol(4₁)`, `Vol(4₁) = 2·Λ(π/3) = 2.02988321…`:

| anchor | c₃ | **S = c₃ + Vol(4₁)** |
|--------|-----|------|
| muon | −2.02020024 | **+0.00968298** |
| proton | −2.06934258 | **−0.03945936** |

`S` **sign-flips** (a hard fact, two measured values), `S(proton)/S(muon)≈−4.08`.
Any anchor-blind constant structurally cannot produce the flip.

## The reduction chain (each arrow: established vs proposed)

### 1. Contour integral → tetraplectic (residue lattice) — ESTABLISHED

Close the Faddeev contour and sum residues. The integrand's poles form the
**double lattice** `w = iπ(m·b + n/b)`, `m,n ≥ 0` (Hikami eq (2.5)); the residue
sum is exactly the **modular-double product**

$$\Phi_b(z)=\prod_{k\ge 0}\frac{1+q^{2k+1}e^{2\pi bz}}{1+\tilde q^{-(2k+1)}e^{2\pi z/b}},\qquad q=e^{2\pi i b^2},\ \tilde q=e^{-2\pi i/b^2}.$$

This is the **tetraplectic** structure — two dual `sinh`-lattices (`b` and
`1/b`). Verified in the evaluator as V5 (`P/Φ_b = 1` to `1.8×10⁻³⁷`).

### 2. Tetraplectic → Young diagram (elementary symmetric) — ESTABLISHED

Each factor is a compact q-Pochhammer; its `x^k` coefficient (`x=e^{2\pi bz}`) is
the **elementary symmetric polynomial**

$$[x^k]\prod_{n\ge0}(1+q^{2n+1}x)=e_k(q,q^3,q^5,\dots),$$

whose lowest term is `q^{k²}` (verified: k=1..4 → q¹,q⁴,q⁹,q¹⁶). This is the
generating function of **partitions into `k` distinct odd parts**.

### 3. Young diagram → partitions (Frobenius/Bruhat symmetric cells) — ESTABLISHED

**Classical Frobenius bijection:** partitions of `n` into distinct odd parts
↔ **self-conjugate partitions** of `n` (the principal hook lengths of a
self-conjugate λ are distinct odd; they determine it). Verified counts
(n=1,3,5,9,16,25 → 1,1,1,2,5,12) match the self-conjugate sequence. Under the
flag-variety **Bruhat decomposition** `G/B=⊔_{w∈W} BwB/B` (cells indexed by
`W=S_n`), self-conjugate partitions are the **symmetric (transpose-fixed)
cells** — the diagram is fixed by conjugation `λ ↔ λ'`.

### 4. The modular double b↔1/b IS conjugation λ↔λ' — PROPOSED (to test)

The self-duality `Φ_b=Φ_{1/b}` swaps the two dual `sinh`-lattices. Its
combinatorial image on `e_k(q,q³,…)` is transpose/conjugation. Hence the
**proposed** identification:

| face | combinatorial sector | dilog face | c₃ part |
|------|----------------------|-----------|---------|
| **bar-EVEN** | **self-conjugate** partitions (λ=λ', symmetric Young diagram) | compact `Φ_q` / mass / real | **−Vol(4₁)** (solved) |
| **bar-ODD** | **non-self-conjugate residual** (λ≠λ', the {λ,λ'} pairing) | `Φ_b` decay / CS phase | **`S`** (open target) |

This aligns the *proved* algebra (bar-even σ-unitaries are involutions,
`FaddeevModularDouble.lean`) with a *combinatorial* home: a genuine phase
(`u²≠1`, bar-odd) is the non-self-conjugate `{λ,λ'}` orbit sum.

### 5. → combinatorial (finite q-sum at the anchors) — the deliverable

At the fibre saddle (`b` real, `q` a root of unity) the product is **finite**
(Kashaev state-sum truncates at `[N]_q=0`), so `S` is evaluated as a **finite
sum over non-self-conjugate partitions** — no divergent `|q₀|>1` product, and
directly Lean-formalizable (the Wenzl–Pochhammer / root-of-unity phase channel
already flagged as the surviving one, [candidate-landscape doc](2026-07-07-qbeta-ck-special-function-candidate-landscape.md)).

## Plug-in point: non-abelian (Yekutieli) Stokes

Step 3 of the canonical chain (`substrate q₀ → 𝐂 → Yekutieli non-abelian
Stokes → H_n(q) Hecke`). The Faddeev `Φ_b` is the **q-holonomy** the non-abelian
Stokes theorem integrates around the braid closure; its residue/partition
expansion is the state-sum. Under
[`genus-filtration-derivation-chain`](../../content/quantum-observable-universe/brings-surface/genus-filtration-derivation-chain.md)
the **bar-odd (non-self-conjugate) residual is the Yekutieli obstruction class
`κ_n ≠ 0`** (`d_q² ≠ 0`) — the decay/CS face — while the bar-even
(self-conjugate) part is the smooth-liftable mass face. This is the structural
reason `S` is the CAL-2 (decay-width) leak: it is the Stokes obstruction, not a
holonomy magnitude.

## Discipline

- **Scope-(a)** throughout: characterizes the target + names the combinatorial
  object; does **not** construct a c₃ value or refute anything.
- **No fit (C14):** the probe compares the sector split to the *structure*
  (self-conjugate vs not), not to `c_k`/`Φ₁`/`A`. Reproducing `S` must come from
  a **derived** argument `z(q₀)` (the CS phase / complex volume), not a scan.
- **Owner-directed Subgoal-2:** the c₃ bar-odd part is Subgoal-2 (sub-CAL-2
  floor). This branch is the owner's explicit direction; no fit-based q₀
  derivation is attempted, and the "no seventh Δ_λ ansatz" rule is untouched.

## Cross-references

- Target: [`…-barodd-sleak-phib-target.md`](../audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md)
- Channel: [`…-phi-b-channel-separation-spec.md`](2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md)
- Candidates: [`…-ck-special-function-candidate-landscape.md`](2026-07-07-qbeta-ck-special-function-candidate-landscape.md)
- Registry: [`ck-dk-canonical-registry.md` §3](../coordination/ck-dk-canonical-registry.md)
- AGENTS.md §"Im(q) at fibre vs observable level"; §"Formalize-first probe discipline"; §"Before declaring refuted (a)/(b)".
