# The non-compact arena cannot host `W_λ` — its Plancherel measures are continuous

**Date:** 2026-08-15
**Branch:** `claude/l2-1ppq-mass-binding-mh643j`
**Beans:** `qou-uqen` (keystone), follow-on to the s5-so3 ledger
**Sources:** owner-uploaded, commit `87e9eb6` —
[`library/arxiv-math-9808030v1/9808030v1.pdf`](../../library/arxiv-math-9808030v1/9808030v1.pdf) (Ahmedov–Duru, *Plancherel
Measure on E_q(2)*, arXiv:math/9808030),
[`library/arxiv-1108.5365v2/1108.5365v2.pdf`](../../library/arxiv-1108.5365v2/1108.5365v2.pdf) (Ip, *Representation of
the Quantum Plane … Harmonic Analysis on GL⁺_q(2,ℝ)*, arXiv:1108.5365),
[`library/9710022v2/9710022v2.pdf`](../../library/9710022v2/9710022v2.pdf) (Buffenoir–Roche, *Harmonic
Analysis on the quantum Lorentz group*, arXiv:q-alg/9710022)

---

## Bottom line

The keystone's open object is a **discrete** measure on Young diagrams,
`W_λ = d_q(λ)²/[n]_q!`, conjugation-symmetric (`W_λ = W_{λ'}`). The
[s5-so3 ledger](../coordination/s5-so3-keystone.md) names the arena as the
non-compact `SU_q(2) → E_q(2)` contraction (2026-06-22 reframe), after the
compact Sasakian/MTC route was excluded at real `q₀ > 1`.

**Read directly, the harmonic analysis of that arena delivers continuous
Plancherel measures — the wrong *type* of object.**

| source | group | Plancherel measure | type |
|---|---|---|---|
| Ahmedov–Duru §V (V.16–V.18) | `E_q(2)` | `dμ = p·dp`, `p ∈ (0,∞)` | **continuous**, 1 parameter |
| Ip, abstract + §on `Wm` | `GL⁺_q(2,ℝ)` | `\|S_b(Q+2iα)\|²` (quantum dilogarithm), continuous series | **continuous** |
| Buffenoir–Roche | quantum Lorentz `SL_q(2,ℂ)_ℝ` | Plancherel thm for the continuous principal series | **continuous** |

No partition index, no conjugation involution, no `[n]_q!` normalisation
anywhere in them.

## Why this is worth recording rather than filing as one more null

It supplies a **reason** where the ledger has a list. The ledger records four
independently-refuted realisation routes (Σ(2,3,5) golden `D=2`; Σ(3,4,5) `D=6`;
colored LR pure-sign; q-Bessel Tricomi + Hahn–Exton), each a scope-(a) numerical
screen. What it does not say is *why they all failed*, and a list of four
coincidental failures invites a fifth attempt.

The mechanism is the standard one and it is not about any particular family:

> **compact ⇒ discrete spectrum; non-compact ⇒ continuous spectrum.**
> `W_λ` is discrete, so it wants a compact object. The 2026-06-22 result excludes
> compact hosts at real `q₀ > 1`. The non-compact replacement then delivers a
> continuous measure. That is a **pincer**, not four accidents.

It also sharpens a detail the ledger's own reframe glosses: the
`SU_q(2) → E_q(2)` **contraction is the step that destroys the discreteness**.
`SU_q(2)` has a discrete spectrum (spins); contraction sends it to `p ∈ (0,∞)`.
So moving *into* the named arena moves *away* from the kind of measure the
keystone needs — the reframe was aimed at the regime problem (`q₀ > 1` growth)
and inherited a type problem in exchange.

## Scope (STRICT, per AGENTS.md §"Before declaring refuted")

**Scope-(a), with a named general mechanism — NOT scope-(b).**

What is established: the three non-compact real-`q` quantum groups whose harmonic
analysis is developed in the literature all carry continuous Plancherel measures,
so none of them hosts `W_λ` as a Plancherel measure.

What is **not** established: that no non-compact route can. A proved invariant
would be needed to upgrade this — e.g. a theorem that any `q`-deformed group
whose Plancherel measure is discrete and partition-indexed at real `q > 1` must
be compact. That is not proved here and is not cited.

Two escapes this does **not** close, stated so the next agent does not read the
finding as wider than it is:

1. **`W_λ` need not arise as a group Plancherel measure at all.** It could be an
   index, a multiplicity, or a trace — the ledger's redirect (iii) takes exactly
   this line, and nothing here touches it.
2. **A discrete sub-object inside a continuous decomposition.** Residual/discrete
   series, or a discrete subgroup's contribution, are not examined here.

## Consequence: redirect (iii) is the answer, not the consolation

The ledger's standing answer — `S_{0λ}/S_{00} = d_q` selected by Markov-trace
uniqueness / the Wenzl bridge / Perron–Frobenius (state positivity =
confinement SDP), already in the corpus — is a **categorical "why" that needs no
geometry**. This audit argues that is not a fallback after the geometric program
ran out of luck: the geometric program has a type obstruction, so the
non-geometric answer is the structurally correct one.

## Corpus-grep performed before writing

- `references.ts`: no Ahmedov, no Duru, no Ip, no `GL_q^+`, no quantum-Lorentz
  Plancherel — all three sources are new to the corpus. (Koelink's `E_q(2)`
  **matrix coefficients** and Koornwinder–Swarttouw's q-Bessel **orthogonality
  nodes** are cited; the invariant **measure** was not.)
- The 2026-07-04 q-Hankel refutation is **scope-(a)** and screened *eigenfunction
  families* against `d_q`; it did not examine the Haar/invariant measure, so this
  is a different object rather than a re-walk.
- Already cited and deliberately **not** re-bought: Féray–Méliot q-Plancherel CLT
  (arXiv:1001.2180), Kerov's q-hook walk, Vershik–Kerov, Koornwinder–Swarttouw,
  Koelink.

## Honest note on how this arose

The three sources were recommended by this session *because* the ledger names
`E_q(2)` as the arena and the corpus had the matrix coefficients but not the
measure. Read, they do not supply the keystone's object — the recommendation did
not pay off in the direction intended. The finding above is what it produced
instead, and it is a negative about the arena rather than a positive about any
construction.
