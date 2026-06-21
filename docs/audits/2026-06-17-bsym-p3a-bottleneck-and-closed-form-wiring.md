# B_sym p(3A) bottleneck — profile, projection, and the closed-form wiring (2026-06-17)

**Branch:** `claude/tender-brahmagupta-17txfq` (PR #2405)
**Trigger:** "the m_sym calculations get heavy around ¹⁶O — can we do a bottleneck
analysis."
**Discipline:** compute-speed audit + exploratory wiring; **no production rewire,
no fit, no witness emitted.** B_sym is the *generic* hyperbolic binding (the
accuracy gap is a separate physics problem — see §E).

## Summary

The heavy step in `m_sym` / `B_sym` is the **Frobenius/Markov pairing**
`tr_M(β) = Σ_{λ⊢3A} y_λ χ^λ(β)` — the **categorical-action pairing** over the
p(3A) Wedderburn blocks of `H_{3A}(q)`. It is intrinsically `O(p(3A))` (confirmed
independently by commit `61abcca9`), so it walls hard at ¹⁶O (~1.8 h) and is
hopeless beyond (²⁴Mg ~11 days, ⁴⁰Ca ~a century). **But for `B_sym` the pairing
is not needed at all:** the binding is *exactly* an additive (A−1)-bond linear
chain, computable from three A=2 constants in milliseconds for any isotope. This
audit profiles the bottleneck, projects the wall, measures the constant-factor
levers honestly, and records the closed-form wiring landed in PR #2405.

## A. The bottleneck IS the categorical-action pairing

The p(3A) is the number of Wedderburn blocks of `H_{3A}(q)` (3 strands/nucleon):

```
H_{3A}(q) ≅ ⊕_{λ⊢3A} End(V_λ)   ⇒   tr_M(β) = Σ_{λ⊢3A} y_λ · χ^λ(β)
```

i.e. **p(3A) = the number of terms in the Frobenius pairing**. The fine-Bratteli
transfer (`computations/chi_monotone_transfer.py`,
`computations/reduced_block_kernel.py`) is already optimal *within* this sum — it
produces all `χ^λ` in one Young-lattice sweep with **no `d_λ` materialisation**
(multiplicity-free, ~3 mpf ops per Bratteli edge). The cost is the size of the
transfer state space, which grows to ~p(3A).

**Live profile** (`8Be`, n=24, gmpy backend, `cProfile`), 5.79 s total:

| cost | tottime | share | what |
|---|---|---|---|
| mpmath bignum arith (`mpf_add`+`mpf_mul`+`gmpy_mpf_mul`+`normalize`) | ~4.0 s | **~70 %** | the `α·D(δ)+β` and `a·f` per Bratteli edge at 50 dps |
| Python loop/dict in `chi_all_lambda_reduced_block` | 0.84 s | ~14 % | iterating `amp.items()` × `_addable(shape)` |
| `mpf_pow_int`, misc | ~0.95 s | ~16 % | the `D(δ)` content factors + dict churn |

~1.36 M mpf add/mul for n=24; the op-count tracks the p(3A) state space.

## B. The exact wall

Exact `p(3A)` (Euler pentagonal recurrence) with the empirical fit
`wall ~ p(3A)^1.40` anchored at ¹²C = 333 s (warm):

| iso | A | n=3A | p(3A) | wall |
|---|---|---|---|---|
| ¹²C | 12 | 36 | 17,977 | 5.5 min (measured 333 s) |
| **¹⁶O** | 16 | 48 | 147,273 | **~1.8 h** |
| ²⁰Ne | 20 | 60 | 966,467 | ~1 day |
| ²⁴Mg | 24 | 72 | 5,392,783 | ~11 days |
| ⁴⁰Ca | 40 | 120 | 1.8×10¹¹ | ~a century |
| ⁵⁶Fe | 56 | 168 | 2.3×10¹⁴ | geologic |

Since `p(n) ~ exp(π√(2n/3))`, the wall is `exp(c√A)` — intrinsic to the lossless
full-partition sum. (Matches the `2026-06-16-bsym-residual-16o-feasibility-wall.md`
projection of ~1.5–3 h for ¹⁶O.)

## C. Constant-factor levers — measured, not guessed

- **gmpy2 backend: only ~1.3× at 50 dps.** Measured same-host A/B: `9Be`
  25.61 s (pure-python mpmath) → 19.69 s (gmpy); `7Li` 3.86 s → 3.03 s. One
  might assume 3–8×, but at 50 dps (~166-bit) the bignums are too small for
  gmpy2 to shine — it wins big only at much higher precision. *Worth confirming
  the production host has gmpy2, but don't expect more than ~1.3×.*
- **Truncation is banned.** `tr_m_atom_zn` is lossless by the 1-ppQ discipline
  (no `max_dim`, no active-set cap; `tr_m_atom_via_transfer.py:88-95`).
- **Rust:** the *existing* wheel (`markov_peel`/`laurent_q`) does **not** touch
  this path — `reduced_block_kernel` is pure mpmath (confirming the 06-16
  feasibility audit §B). A *new* MPFR port of the transfer kernel could give a
  ~20–100× constant factor (¹⁶O → minutes, ~²⁴Mg feasible) but still loses to
  `exp(c√A)`. Sibling `61abcca9` ruled out the *algorithmic* escapes
  (restricted-MPS / R-matrix / sparsity all fail to beat p(3A)).

Bottom line: no constant factor makes the heavy nuclei routinely feasible via the
exact sum. The win has to be structural — and for `B_sym` it is.

## D. The resolution — closed-form linear chain (landed PR #2405)

`B_sym` is **exactly** an additive (A−1)-bond linear chain. The atom word
`atom_braid_word_3A(Z,N)` orders strands `['p']·Z + ['n']·N` with one
inter-nucleon crossing on each *distinct* generator (monotone word), so the
log-binding factorizes over the (Z−1) p-p + 1 p-n + (N−1) n-n adjacency bonds:

```
B_sym(Z,N) = α[(Z−1)·L_pp + L_pn + (N−1)·L_nn],   L_X = ln(tr_free/tr_1-X-bond)
```

(full derivation: `2026-06-16-b-sym-linear-chain-closed-form.md`.) The three
`L_X` are the same 2-nucleon constants `mass_binding_dashboard._bond_type_L()`
already computes for the q-CLT. **Live demonstration** (this session):

```
bond constants:  b_pp=2.9072  b_pn=3.8897  b_nn=5.1780  MeV   (extraction: 0.01 s)
 4He  chain 11.97485 = exact-trace 11.97485   ✓
 7Li  chain 25.23798 = exact-trace 25.23798   ✓
 12C  chain 44.3155  = audit's 333 s sweep 44.32   ✓   (A=12, far past the A=2,3 fit)
 16O  chain 60.4858 MeV   [instant; vs ~1.8 h sweep]
 40Ca chain 157.51 MeV    [instant; vs ~century]
 56Fe chain 226.73 MeV    [instant]
```

**Wiring** (`computations/mass_binding_dashboard.py`): `B_sym` and
`m_sym_atom = B_sym + m_sym_free` now come from the chain for **every** isotope;
the exact p(3A) trace is still run for `n=3A ≤ --max-strands` purely to **validate**
the chain (float64 dashboard residual ≈ 1e-6 MeV; the 50-dps equivalence is the
audit's). The dashboard sweep now populates ¹⁶O…⁵⁶Fe with no wall.

**No tension with `61abcca9`.** That verdict is about the *full per-λ χ vector*
(irreducibly p(3A)). The closed form is about the *binding functional* `B_sym`, a
single scalar that factorizes because of the distinct-generator structure. An
observable that does **not** factorize would still hit the p(3A) wall — so the
Wenzl-A≥3 combiner work (#2371/#2392/#2403) speeding up the exact trace is not
obviated by this.

## E. Scope — compute-speed, NOT accuracy (critical-distance)

This removes a *compute wall*; it does **not** improve the prediction. `B_sym` is
the generic hyperbolic chain binding and **under-binds** (¹⁶O 60.5 vs AME 127.6,
ratio ~2.1; the whole ladder sits at 2.1–2.2 past the light nuclei). The accuracy
gap is the cooperative **α-cluster / shell-closure** term — the Δ_λ gate, which
AGENTS.md blocks from any fit-based ansatz. The 1.8 h ¹⁶O sweep was never going to
produce an accurate binding; it would only have produced the exact `B_sym`, which
the closed form already gives instantly. The α-unit magnitude remains the one open
lever (α-cluster recursion with ⁴He as the magic input), unchanged by this PR.

## F. Cross-links

- `docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` — the closed-form
  derivation (this audit is its compute/wiring sibling).
- `docs/audits/2026-06-16-bsym-residual-16o-feasibility-wall.md` — the ¹⁶O wall +
  per-nucleon-branching follow-up; §B "Rust does not help" (confirmed here §C).
- commit `61abcca9` — `χ_eff(k)=p(3k)` exactly; the p(3A) wall is intrinsic
  (independent confirmation of §A/§B).
- commit `17c3c9a2` — the atom-braid-beyond-12C 4-direction workplan that
  `61abcca9` closed.
- PR #2348 (atom→electron `m_atom`) — direct consumer of dashboard `m_sym`; now
  all-A via this wiring.
