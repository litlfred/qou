# Collatz "no-cycles" proof over-claims: multiplicative shadow vs. affine cycle

**Date:** 2026-07-18
**Branch:** `claude/q-collatz-status-1v0pxv`
**Scope:** re-scope of an over-claim (scope **(a)**, per AGENTS.md
§"Before declaring refuted / ruled out"). The numerical/algebraic
sub-result stands; only its advertised *scope* was wrong. This is **not**
a structural exclusion (b) and **not** a claim that the coprimality
identity is false.

## Summary

The block [`prf:collatz-no-cycles`](../../content/quantum-observable-universe/appendix-surreals/collatz-no-cycles-proof.md)
claims to "settle half the Collatz conjecture: no periodic cycles other
than `{1}`" using the coprimality identity `[3]_q − q[2]_q = 1`. The
argument reduces a periodic orbit to the *multiplicative* return
condition

```
[3]_q^{k_odd} = [2]_q^{k}      (k = k_odd + k_even)
```

and then kills it by `gcd([2]_q, [3]_q) = 1`. **This is the
multiplicative shadow of the map, not the affine map.** The Skein-Collatz
map's odd branch carries an additive `+1`:

```
C_q(P) = ([3]_q · P + 1) / [2]_q      (q-odd branch)
C_q(P) = P / [2]_q                     (q-even branch)
```

so it is an **affine** map `P ↦ aᵢ P + bᵢ`, not a linear one. Dropping
the `bᵢ` is exactly the step that makes classical nontrivial-cycle
exclusion look easy when it is in fact open.

## The gap

For a cycle `P₀ → P₁ → … → P_k = P₀` of an affine map, iterate:

```
P_k = A · P₀ + B,   A = ∏ᵢ aᵢ = [3]_q^{k_odd} / [2]_q^{k},   B = Σᵢ (∏_{j>i} aⱼ) bᵢ.
```

The cycle condition `P₀ = A·P₀ + B` gives

```
(1 − A) · P₀ = B.
```

Two cases:

- **`A = 1`** (i.e. `[3]_q^{k_odd} = [2]_q^{k}`): forces `B = 0`. Since
  every `bᵢ ≥ 0` and `bᵢ > 0` on odd steps (`bᵢ = 1/[2]_q^{…} > 0` for
  `q > 0`), `B = 0 ⟹ k_odd = 0`, i.e. an all-even chain `P₀ = P₀/[2]_q^k
  ⟹ P₀ = 0`. **This is the only case the corpus proof actually
  covers.** It is correct — but it is the degenerate balanced-holonomy
  case, not the general cycle.

- **`A ≠ 1`**: then `P₀ = B / (1 − A)` is a **unique, well-defined
  candidate cycle value** in the fraction field. Coprimality of
  `[2]_q, [3]_q` guarantees `A ≠ 1` for `k_odd ≥ 1, k ≥ 1` — so it
  **hands us the candidate rather than excluding it.** In the contractive
  regime `A < 1` (`[3]_q^{k_odd} < [2]_q^k`), we have `1 − A > 0` and
  `B > 0`, so `P₀ > 0`: a positive candidate sits in the cone.

**The corpus argument is therefore a non-sequitur in the direction it is
used:** `gcd = 1 ⟹ A ≠ 1` is precisely the hypothesis under which
`P₀ = B/(1−A)` is a single finite value. Coprimality makes the candidate
*solvable*, not impossible.

## What is actually true (the honest partial result)

Coprimality settles exactly the **balanced-holonomy sub-case**:

> The Skein-Collatz map has no periodic orbit whose multiplicative
> holonomy `A = ∏ aᵢ` equals `1`, other than the degenerate fixed
> points.

The genuine affine-cycle problem — does the candidate `P₀ = B/(1−A)`
ever land in `ℤ[q^{±1}]_{>0}` **and** stay consistent with the
parity/valuation pattern `(aᵢ, bᵢ)` that produced it? — is **open**,
with the same difficulty as classical nontrivial-cycle exclusion (where
the analogous rational-cycle-value formula is known and its
integrality/consistency is the hard part).

## Chip-away contribution (sharper reduction)

The affine iteration gives a **concrete, testable reduction** the corpus
did not state:

> **q-cycle-value formula.** Any period-`k` Skein-Collatz cycle with
> holonomy `A = [3]_q^{k_odd}/[2]_q^k ≠ 1` has its base point pinned to
> `P₀ = B / (1 − A) ∈ ℚ(q)`. Nontrivial-cycle exclusion is equivalent to:
> for every admissible parity word `w` of length `k` with `k_odd ≥ 1`,
> the value `B_w/(1 − A_w)` fails to be a positive element of the Skein
> module `ℤ[q^{±1}]` realising the word `w`'s own valuation pattern.

This is the q-analog of the classical cycle-value constraint (Böhm–Sontacchi /
Steiner-style), now over `ℤ[q^{±1}]`, and is a well-defined next probe:
enumerate short parity words `w`, form `B_w/(1−A_w)`, and check
Skein-integrality + cone-membership + self-consistency. It replaces the
false "coprimality closes it" with an honest, computable target.

## Corpus-grep checklist (per AGENTS.md §"Before declaring open")

- `docs/audits/` — no prior audit of the affine-vs-shadow gap (this is
  the first).
- `content/` — the over-claim is local to
  `collatz-no-cycles-proof.md`. Sibling blocks are already honest:
  [`collatz-three-forms.md`](../../content/quantum-observable-universe/appendix-surreals/collatz-three-forms.md)
  says "individual orbits might fail. The conjecture asserts they never
  do"; [`collatz-surreal-bound.md`](../../content/quantum-observable-universe/appendix-surreals/collatz-surreal-bound.md)
  says the classical recovery holds "only by assuming … a well-defined
  standard part." Only the no-cycles *proof* block over-claims.
- `computations/` — no compute realises an affine-cycle exclusion.
- coordination ledgers — none for the Collatz appendix material.

All four paths empty modulo the originating file ⇒ the gap declaration is
permitted.

## Computational census (period ≤ 18)

The `P₀ = B/(1−A)` reduction is directly testable. An exhaustive census
of primitive parity words up to period 18
([`computations/qcollatz_cycle_census.py`](../../computations/qcollatz_cycle_census.py),
witness [`qcollatz_cycle_census.witness.json`](../../computations/qcollatz_cycle_census.witness.json))
computes each candidate `P₀` by **exact integer Laurent-polynomial
division** — clearing the cycle equation to
`([2]_q^k − [3]_q^{k_odd}) · P₀ = n_k` in `ℤ[q^{±1}]` and testing exact
divisibility, then checking parity self-consistency and return.

**Result (523,131 primitive words, period ≤ 18):** the *only* integral,
self-consistent Skein-Collatz cycles are

| Cycle | `P₀` | classical limit `q=1` | in cone? |
|---|---|---|---|
| positive 2-cycle `{q⁻¹, 1+q⁻¹}` | `q⁻¹` | `{1, 2}` | ✓ |
| negative fixed point `{−q⁻²}` | `−q⁻²` | `{−1}` | ✗ (excluded) |

These are the exact `q`-lifts of the classical Collatz cycle structure
(the only positive cycle is `{1,2}`; the only negative fixed point is
`{−1}`). **No nontrivial positive `q`-cycle exists up to period 18** —
negative evidence *consistent with* the conjecture, but **not** a proof
(the census is bounded; the affine cycle problem stays open).

### Secondary finding — the unknot `1` is outside the map's domain

The census surfaced a precise correction. The conjecture states orbits
"reach `1`" ([`conj:q-collatz`](../../content/quantum-observable-universe/appendix-surreals/q-collatz-conjecture.md)),
but the literal element `P = 1` is **neither `q`-even nor `q`-odd**:
`1|_{q=-1} = 1 ∉ {0, −1}`, so `C_q(1)` is undefined. The genuine positive
attractor is the 2-cycle `{q⁻¹, 1+q⁻¹}` (the `q`-lift of `{1,2}`), which
degenerates to `1` only in the classical limit. "Reaches 1" is a
classical-limit shorthand; at the Skein level the target is the
fundamental 2-cycle. (Scope (a) clarification, not a refutation.)

## Action taken

1. Re-scope the prose of
   [`collatz-no-cycles-proof.md`](../../content/quantum-observable-universe/appendix-surreals/collatz-no-cycles-proof.md):
   the coprimality argument settles the `A = 1` sub-case; the affine
   cycle problem is stated as open with the `P₀ = B/(1−A)` reduction.
2. This audit doc.

## Not changed (deliberately)

- The Lean `collatz_no_cycles` (`§3b`-conditional context class) already
  carries `no_cycles_of_coprime` as an **axiom field**, so it is honest
  at the type level: it derives the conclusion *from* an assumed
  no-cycles hypothesis, it does not prove it. No Lean edit needed.
- The coprimality identity itself (`qInt_coprime`, `skein_divisibility`
  in `QOU/QCollatz.lean`) is correct and stays.

## Proof progress + honest walls (2026-07-24)

Lean tranche proved sorry-free this session (all in `QCollatz.lean` /
`collatz_no_cycles.lean`, `lean`-direct exit 0):

| Theorem | Content |
|---|---|
| `qi3_sub_q_qi2` | Skein-Bézout `[3]_q − q[2]_q = 1` |
| `balanced_holonomy_excluded` | `[3]_q^{k_odd} = [2]_q^k` impossible for `k≥1` (A=1 core) |
| `qcollatz_fundamental_odd_step` / `even_step` | `{q⁻¹,1+q⁻¹}` is a genuine 2-cycle |
| `qcollatz_odd_fixed_point` / `neg_qinv_sq_is_odd_fixed` | odd-branch fixed point is exactly `−q⁻²` (negative) |
| `qcollatz_even_fixed_point` | even-branch fixed point forces `q·P=0` (⟹ `P=0`) |
| `iterate_period_two_mem` / `qcollatz_attractor_orbit_bounded` | attractor orbit ⊆ `{attractor, C attractor}` (bounded invariant set) |
| `qcollatz_domain_not_forward_invariant` | domain is not forward-invariant |
| `reaches_cycle_of_descent` | convergence **reduces** to a strictly-descending measure `μ` |

**Period-1 case of nontrivial-cycle exclusion is fully closed**: the only
fixed points are `0` (even) and `−q⁻²` (odd), neither positive.

### The two genuine walls (not fabricated)

1. **Convergence (`reaches_cycle`).** `reaches_cycle_of_descent` reduces it
   to the existence of a measure `μ : Skein → ℕ` strictly decreasing off
   the attractor. Constructing `μ` is the hard content — the `q`-analog of
   a Collatz *stopping-time* bound. The intended witness is the `[2]_q`-adic
   valuation descent (`⟨v_[2]⟩ ≥ 2`, `prop:collatz-contact-boundary`), but
   turning it into a provably-well-founded `ℕ`-measure requires a Lean
   valuation on `ℤ[q^{±1}]` and a proof that the per-cycle contraction
   `[3]_q/[2]_q³ < 1` forces global descent — the same difficulty as the
   open classical problem. **No elementary construction is known.**

2. **Period-≥2 affine exclusion.** The candidate cycle value is
   `P₀ = n_w/([2]_q^k − [3]_q^{k_odd})`; exclusion requires
   `([2]_q^k − [3]_q^{k_odd}) ∤ n_w` (plus positivity + parity-word
   consistency) for every admissible word. This is the `q`-analog of the
   classical cycle-value bounds (Steiner; Simons–de Weger), which classically
   need deep transcendence input (linear forms in logarithms). The census
   (`qcollatz_cycle_census`, ≤ period 18) is negative evidence only.

Both are honestly **open**; neither is fabricated or wired to production.
The next real attack step for (1) is a Lean `[2]_q`-adic valuation over
`LaurentPolynomial ℤ`; for (2), a `q`-Steiner-style height/valuation bound.
