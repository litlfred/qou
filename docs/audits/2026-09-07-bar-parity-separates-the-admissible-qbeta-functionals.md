# Bar parity separates the admissible `Q_β` functionals — and the published one fails on convention C's side

**Date:** 2026-09-07 · **Beans:** `qou-99qc` (Option E), `qou-37j2` · **Branch:** `claude/qbeta-element-collapse-2026-09-07`
**Probe:** [`qbeta_bar_parity_separates_admissible_functionals_probe.py`](../../computations/qbeta/qbeta_bar_parity_separates_admissible_functionals_probe.py) — 14/14, exact over ℚ(q)
**Tier:** scope-(a) prune with a derived invariant. **Nothing wired, no number moved, no functional adopted.**

Reached by starting §5 item 2 of the [1 ppQ reanalysis](2026-09-07-1ppq-reanalysis-what-moved-and-what-to-attack.md)
— the non-ladder `Q_β` derivation, which is **Option E** of
[the decision document](2026-09-05-qbeta-functional-decision-options.md): *keep an admissible
functional and derive the element it should act on.*

---

## 0. Three results, and the first one is a refutation of my own hypothesis

1. **The two candidate elements really are different — my collapse hypothesis is FALSE.**
2. **Closed forms for all three cells of the `Δ_S` column**, which the corpus carried as decimals.
3. **A bar-involution parity that both admissible roots satisfy exactly and both inadmissible
   functionals fail** — an anchor-free structural prune for Option E.

---

## 1. The collapse hypothesis, and why it fails

I posted intent on #6832 with this angle: `NF` is a **Gröbner–Shirshov normal form**, i.e. a
canonical basis representative and hence the identity on the algebra element. If so,
`NF(β_n) − NF(β_p)` and `β_n − β_p` are the *same element* of `H₃(q)`, every `χ_λ` must agree, and
the element question in the decision document is not a choice at all but an arithmetic discrepancy
to locate.

**Measured, and it does not hold.** With `h = q − 1/q`:

```
ε(Δ_S)     = (q−1)(q+1)(q²−2q−1) / (2q²)          [Δ_S = NF(n) − NF(p)]
χ_(3)(Δ_L) = −(q−1)(q+1)(q²+1)²  / (4q)           [Δ_L = β_n − β_p]

difference = (q−1)²(q+1)²(q³+3q+2)/(4q²)   ≠ 0 identically
ratio      = −q(q²+1)² / (2(q²−2q−1))      → 1 as q→1,  = 1.39090616920312 at q₀
```

That ratio reproduces `qou-avt5`'s recorded `1.39090616920312` **to all 15 digits it carries**, so
the computation is calibrated against the corpus's own measurement rather than free-standing.

**So the element question is real.** `Δ_S` and `Δ_L` are genuinely two elements, agreeing
classically (`q → 1`) and diverging at the substrate. Option E's "find the element" is a search,
not a bug hunt. **Recorded as a negative because it closes a cheap route** — nobody else needs to
try the collapse.

Two supporting facts, both verified rather than assumed:

- `chi_block_λ` **are** exactly `χ_λ(β_n − β_p)` symbolically in `q`, all three blocks
  ([`qbeta_chi_block_symbolic_closure_probe.py`](../../computations/qbeta/qbeta_chi_block_symbolic_closure_probe.py),
  re-run this session, 9/9). So the `Δ_L` side of the comparison is sound.
- `χ_(3)` **is** the counit (the 1-dimensional rep `σᵢ ↦ q`), so comparing `χ_(3)(Δ_L)` against
  `ε(Δ_S)` compares like with like.

## 2. Closed forms for the whole `Δ_S` column

The decision document's grid gives the three cells as percentages. They are elementary rational
functions, and **they share a factor**:

> `Q_β / m_e  =  (q+1)/(2q³) · M(q)`

| `z` | `M(q)` | palindromic? | admissible under D | err at `q₀` |
|---|---|:--:|:--:|---:|
| `z = 1` — **published** | `\|q² − 2q − 1\|` | **no** | **no** | +0.16775678 % |
| `z = q` — augmentation | `q² + 1` | yes | yes | +12.470022 % |
| `z_D = q³/(q²+1)` — Markov, D | `(q⁴ + 1)/(q² + 1)` | yes | yes | −43.157175 % |

All three reproduce the recorded percentages (CHECK 5). The `z = 1` row differs in its last digit
(`…678` vs `…687`), which is the CODATA reference the two computations use, not a disagreement in
the algebra.

**This is bookkeeping, not a new result** — but it turns three decimals into three formulas, and
the formulas are what the next section reads.

## 3. The parity, derived

`bar` is the involution `q ↦ 1/q`. Then `bar(h) = −h` **identically**, so for
`N(z) = tr_M(Δ_S) = h²/2 − h·z`:

```
bar(N) = h²/2 + h·bar(z)        hence        bar(N) = −N   ⟺   z − bar(z) = h
```

equivalently — the cleaner form — **`z − h/2` is bar-invariant**. Solved symbolically rather than
asserted (CHECK 2). Measured on the four functionals:

| `z` | `z − bar(z) − h` | parity | `bar(Q)/Q` | admissible |
|---|---|:--:|---|:--:|
| `z = 1` (published) | `−(q−1)(q+1)/q` | **FAIL** | not a monomial | no |
| `z_C = √q/(q+1)` (excised C) | `−(q−1)(q+1)/q` | **FAIL** | not a monomial | no |
| `z = q` (augmentation) | `0` | **PASS** | `q³` | yes |
| `z_D = q³/(q²+1)` (Markov D) | `0` | **PASS** | `q³` | yes |

**Parity agrees with admissibility on every functional tested**, and the two failures fail *the
same way*: both are bar-**invariant** (`bar(z) = z`) where the admissible ones are bar-**shifted**.

That `bar(z_C) = z_C` while `bar(z_D) = q⁻⁴·z_D` is already on the record in `qou-cds1`; this probe
reproduces both as a cross-check rather than importing them, and `bar(z_D) = 1/(q(q²+1)) =
q⁻⁴·z_D` ✓.

## 4. 🛑 What this does NOT establish

**It is not a characterisation of admissibility, and must not be quoted as one.** The condition
"`z − h/2` bar-invariant" defines an **infinite family** of rational `z(q)`. CHECK 4 exhibits a
member that is not an admissible root — take any bar-invariant `w` and set `z = w + h/2`; with
`w = q + 1/q` this gives

```
z = (3q² + 1)/(2q)        passes the parity,        is neither q nor z_D
```

So the honest scope is **scope-(a), necessary-not-sufficient**:

> A candidate `Q_β` functional **failing** the parity is excluded.
> One **passing** it is not thereby admissible.

The (b)-strength part is only the algebraic identity `bar(h) = −h` and the criterion derived from
it; the agreement with admissibility is measured on four points, not proved.

## 5. Why it is worth having for Option E

Option E is the only one of the decision document's seven that could produce a **parameter-free
admissible** result rather than a choice among existing misses (+12.470 % / −43.157 %). It is also
unbounded research. This gives it a test that:

- **uses no anchor and no experimental input** — it is an identity in `ℚ(q)`, so it runs before any
  number is computed and cannot be a fit;
- **prunes rather than scores** — which is the ranking the anti-fit rule asks for, since accuracy
  is a diagnostic here and not evidence;
- **is cheap** — one symbolic simplification per candidate.

That is the formalize-first shape: find the invariant the whole hypothesis class must satisfy
*before* running the wide search, and let it narrow the probe.

## 6. What was NOT done

- **No functional was adopted.** The seven-option decision remains the owner's (`qou-99qc`).
- **No element was derived.** §1 establishes only that the element question is real.
- **No claim that the parity is necessary *and* sufficient** — §4 refutes that outright.
- **The `Δ_L` column was not recomputed** under the parity; only the `Δ_S` column's three cells,
  which is where the decision document's grid and the published closed form live.

-- Ref: [manuscript] beans qou-99qc, qou-cds1, qou-avt5, qou-37j2
