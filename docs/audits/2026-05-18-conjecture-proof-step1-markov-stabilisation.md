# λ_scale Conjecture Proof — Step 1 (H_4 as proton's Markov-stabilised level)

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Conjecture:** [`conj:lambda-scale-substrate-form`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.md)
**Status:** Categorical argument written; formal proof open.

## The claim

Step 1 of the proof strategy:

> The proton's canonical 3-strand braid $\mathcal{N}_p \in B_3$,
> viewed at the next Markov-stabilisation level $H_4(q)$, has its
> Wedderburn-trace expansion controlled by the partition spectrum
> of $4$.

## Why H_4 (not H_3)?

The proton is canonically a **3-strand** braid (3 quarks, 3 colors).
A natural choice for the relevant Hecke level is **H_3(q)** — with
3 Wedderburn blocks: $(3), (2,1), (1,1,1)$.

But the half-symmetric count at H_3 is:
- (3) ↔ (1,1,1) — 1 conjugate pair (weight 1)
- (2,1) — 1 self-conjugate (weight 1/2)
- **hsc(3) = 1 + 1/2 = 3/2**

Numerically: $3/2 - h^2 G ≈ 1.46$ vs target $\lambda_p ≈ 2.46$.
**Off by exactly 1.** So H_3 is the wrong level.

H_4 gives `hsc(4) = 5/2` matching $\lambda_p$ to 5.4 ppm. So
**H_4 is the empirically correct level**, but Step 1 requires a
*categorical* reason for the level-up.

## The Markov-stabilisation argument

### Background: Markov moves

A braid $\beta \in B_n$ generates a Markov-equivalence class of
braids under two moves:
1. **Conjugation**: $\beta \mapsto \alpha \beta \alpha^{-1}$
2. **Stabilisation**: $\beta \mapsto \beta \cdot \sigma_n^{\pm 1}$
   (adding one strand)

The Markov trace is invariant under both moves. The natural
**level** of a braid for trace-computation purposes is the
*stabilised* form — adding one extra strand to expose the
Markov-stabilisation operator $\sigma_n$.

### The proton's natural stabilisation

For the proton's 3-strand braid $\mathcal{N}_p \in B_3$:

$$
  \mathcal{N}_p^{\mathrm{stab}} = \mathcal{N}_p \cdot \sigma_3 \in B_4.
$$

The Markov trace $\tau(\mathcal{N}_p^{\mathrm{stab}}) = z \cdot
\tau(\mathcal{N}_p)$ where $z = 1/(q^{1/2} + q^{-1/2})$ is the
Markov parameter.

But computing $\tau(\mathcal{N}_p^{\mathrm{stab}})$ requires the
**Wedderburn decomposition of H_4(q)** — 5 blocks indexed by
partitions of 4. This is where H_4 enters.

### Why ONE stabilisation, not zero or two?

For a *baryon* (3-quark composite), the canonical interpretation is:

- The 3 quarks form 3 strands in B_3.
- The **fourth strand** is the "vacuum line" — the Markov
  trace's closure operation requires one ambient strand for the
  closure to be well-defined.
- Equivalently: the **isospin axis** lifts the proton from a pure
  B_3 element to a B_4 element via the orientation tag.

This is the **Markov-stabilised level**: the smallest n such that
the braid + closure + orientation tag fits into H_n(q) as a
well-defined element.

For the proton, that's $n = 4$.

For higher baryons (Σ, Λ — see PR #683 probe results), the
**strange quark** adds an additional Hecke generator, lifting to
$H_5(q)$ or higher. The level-up matches the empirical observation
that strange baryons don't follow the p(4)/2 pattern.

## Why this is categorical, not just empirical

The hsc(4) = 5/2 numerical match doesn't *force* the level to be
H_4 — it just happens to match. The categorical argument for
H_4-specifically would be:

**Claim (Step 1 categorical):**
The Markov-trace generating function of the 3-strand proton braid,
under closure with orientation tag, is supported on the
$\mathbb{Z}[q^{\pm 1}]$-span of H_4(q)'s Wedderburn block characters,
and on no lower level.

**Proof sketch:**

1. The proton braid $\mathcal{N}_p = \sigma_1 \sigma_2^{-1} \sigma_1
   \cdot (\text{quark labels})$ in B_3 generates an H_3-trace.
2. The orientation tag (u, u, d) is a **labeling** of the 3
   strands; under the closure operation, the label becomes part of
   the cycle structure, requiring a 4th "ambient" strand for the
   labeling to embed into a closed surface.
3. The H_4 extension is the **minimum** level that supports both
   the 3-strand braid AND the orientation-tagged closure as a
   single algebraic object.

The "minimality" is the load-bearing claim. It requires:
- Showing that H_3-only (no stabilisation) doesn't admit the
  orientation closure.
- Showing that H_5-or-higher stabilisations are reducible to H_4
  (via Markov moves).

The minimality argument is plausible but not yet formalised. The
**empirical level matching at hsc(4) = 5/2** is the strongest
existing evidence.

## Concrete next R&D for full proof

1. **Explicit construction** of the orientation-tagged closure
   functor $B_3^{\mathrm{labeled}} \to H_4(q)$. Verify that:
   - 3-strand proton braids embed faithfully into H_4(q).
   - The Markov-stabilisation is unique (not multi-valued).
2. **Minimality theorem**: show H_3(q) + orientation tag is
   *insufficient* (the labeling doesn't lift), and H_5(q) is
   *redundant* (any stabilisation to H_5 collapses to H_4 via
   Markov moves).
3. **Cross-check at higher baryons.** Σ baryons should embed
   into H_5(q) at the analogous "Markov-stabilised level"; if
   their λ values match hsc(5) = 7/2 OR a refinement
   accounting for the strange quark, that's structural support.

The probe found Σ/Λ λ values DON'T match hsc(5)/2 = 7/2 directly
(Σ λ ≈ 3.12, hsc(5) = 7/2 = 3.5), suggesting the strange-baryon
case needs additional structure beyond simple stabilisation.

## Conjectural-proof closure summary (after Steps 1, 3, 4 in this PR)

| Step | Status | Method |
|------|--------|--------|
| **Step 1** | **Structural argument** (this audit) | Markov-stabilisation + minimality |
| Step 2 | ✅ Proved | Combinatorial enumeration (PR #683) |
| Step 3 | Structural argument | Yekutieli-Stokes + tessellation bijection (separate audit) |
| Step 4 | Open R&D | h^4 PSLQ search (this PR's probe) |
| Step 5 | ✅ Closed structurally | Anchor + substrate Q_β |

**Steps 1, 3, 4 advanced from "Open" to "Structural argument" or
"Open R&D with concrete bounds" in this PR.** Combined with
Step 2 (proved) and Step 5 (closed structurally), the conjecture
proof now has:

- 1 step fully proved (Step 2)
- 1 step closed structurally (Step 5)
- 2 steps with structural arguments (Steps 1, 3)
- 1 step open R&D with concrete bounds (Step 4)

The remaining gaps are clearly scoped:
1. Minimality theorem (Step 1)
2. Per-cell extraction bijection (Step 3)
3. Closed form for c_4 (Step 4)

Each is a tractable follow-on PR.
