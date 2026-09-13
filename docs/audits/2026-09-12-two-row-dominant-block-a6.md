# At A ≥ 5 the trace's dominant block is two-row, and its log-weight is NOT a bond functional — it carries connected many-edge terms at every order, non-local along the chain, whose net is anti-binding and ~3.5 MeV

**Date.** 2026-09-12
**Bean.** `qou-vn6h` — the A ≥ 6 remainder of `qou-brng` after `qou-m8f3` (PR #7200)
**Branch / PR.** `claude/two-row-dominant-block-a6-2026-09-12`, #7211
**Producer.** [`computations/brng_two_row_dominant_block_a6_probe.py`](../../computations/brng_two_row_dominant_block_a6_probe.py)
→ `brng-two-row-dominant-block-a6.witness.json`, 60 dps, proton pin
`Q_50_DIGIT_STR`, convention D `z = q³/(q²+1) = 0.6126880371…`, wall 677 s
(35 clusters × 2 words + 32 + 23 interface-subset words; n = 21 costs ~12 s
per word on the window transfer).
**Lean.** [`QOU/Mass/MixedSpectrumCharacterNotLetterMultiplicative.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/MixedSpectrumCharacterNotLetterMultiplicative.lean)
— generic `[Field R]`, five declarations, `lean -DautoImplicit=false -s 65536`
exit 0 against the restored Mathlib oleans, `#print axioms` on all five:
`[propext, Classical.choice, Quot.sound]`, no `sorryAx` (§6).
**Scope.** **(b)** for *"the one-row letter-product argument extends to the
two-row block"* — it does not, and the invariant is the Lean lemma (§6).
**(a)** for the physics: the two-row dominant summand's log-weight, *alone*,
does not reproduce the A = 5–7 bindings (§5). Nothing wired, nothing fitted, no
route selected by residual.

---

## 0. The question

PR #7200 (`qou-m8f3`) showed that for every typed cluster with `A ≤ 4` the
dominant summand of the partition sum

$$\mathrm{tr}_M(\beta_A) = \sum_{\lambda \vdash 3A} y_\lambda\,\chi^\lambda(\beta_A),
\qquad \lambda^* = \operatorname{argmax}_\lambda |y_\lambda \chi^\lambda(\beta_A)|$$

is the one-row block `[3A]`, whose character is a ring homomorphism
`σ_g ↦ q`, so `log|χ^{[3A]}|` is a sum over letters and the dominant
summand's log-weight `L(A) = log|y_{λ*} χ^{λ*}(β_A)|` is **exactly** chain-edge
additive — no connected many-body term (scope (b) at `A ≤ 4`). It stopped at
⁶Li, where the dominant block is two-row. A two-row character is the trace of
a representation of dimension `> 1`, not a ring homomorphism, so nothing in
#7200 says whether *its* log-weight carries a connected term. This is the
A ≥ 5 remainder of `qou-brng`'s dominant-summand channel (class C of the
2026-09-11 enumeration).

Two prior facts the corpus already holds and which this test uses rather than
re-derives: under convention D the two-row stratum is the **whole support**
(`y_λ = 0` for `ℓ(λ) ≥ 3`, `mass-theory/two-row-stratum.md`), so "the dominant
block" is always one- or two-row; and `he4-two-row-dominance` /
`active-set-trace-concentration` record two-row *stratum* dominance at ⁴He
(the stratum's share), which is a different statement from the *single*
dominant block's identity measured here.

## 1. What was computed

For every typed cluster `(Z, N)` with `1 ≤ Z + N ≤ 7` — 35 clusters, so every
sub-cluster of ⁷Li/⁷Be is in the inversion, and A = 5 (⁵He, ⁵Li: unbound to
nucleon emission, B > 0 against free nucleons) enters as a sub-cluster like any
other and is **flagged, not skipped** — on the live alternating-core word
`atom_braid_word_3A(Z, N)` (bean `qou-hu1f`, 2026-09-05) and its free word:

1. every `χ^λ` (`chi_general_word.chi_all_lambda_any`, 60 dps) and `y_λ`
   (`wedderburn_jones_markov.y_lambda_at(n, Q_MP)`); the dominant summand **as
   the trace defines it** (`argmax |y_λ χ^λ|`), its runner-up ratio, its share;
2. `L_atom`, `L_free`, `ΔL = L_free − L_atom`, the same-block difference
   `ΔL_sameblock` (free word in the atom's own block; `y_{λ*}` cancels) and the
   free-side argmax `switch = ΔL − ΔL_sameblock`, as in #7200;
3. **fixed-n chain-edge additivity, per block.** At fixed `A` the `A+1` typed
   words share every block of `H_{3A}`. For each `λ`,
   `X_λ(Z,N) = log|χ^λ(atom_{Z,N})| − log|χ^λ(free_{Z,N})|` is tested against
   `(Z−1)L_pp + [Z,N ≥ 1]L_pn + (N−1)L_nn` with the three constants
   *determined* by `(A,0)`, `(0,A)`, `(A−1,1)` and the other `A−2` words
   *predicted*. No parameter meets a residual; the residual is the measurement;
4. **the typed bond-set decomposition inside the dominant block.** The atom
   word has `A−1` interface letters, one per chain edge, each a single Hecke
   letter at generator `3k+2` (pp: `σ`; pn: `σ − h(½−δ/4)·1`; nn: `σ − h·1`).
   Deleting a subset leaves a word with exactly that interface set `S`. With
   `F_λ(S) = log|χ^λ(word_S)|`, the Möbius cumulants
   `c_λ(S) = Σ_{T⊆S} (−1)^{|S∖T|} F_λ(T)` are the connected (Ursell) cumulants
   of the block's log-weight over the typed bond set. **Letter-multiplicativity
   over the interfaces is exactly `c_λ(S) = 0` for all `|S| ≥ 2`.** All 32
   subsets at ⁶Li; singletons, all 15 pairs and the full set at ⁷Li (the 64
   subsets there are 12 minutes and the pairs already decide the question).
   Controls in the same run: the one-row block `[n]` (letter product ⇒ zero)
   and the full trace (bond rule ⇒ zero);
5. the typed Ursell inversion (complete-graph typed basis, one cumulant per
   composition `(z,n)`) of `ΔL`, `ΔL_sameblock`, `switch`, `log y_{λ*}` and the
   full-trace log ratio to order 7; the corpus uniform-`e₂` convention at
   `A ≤ 4` (where it is defined); per-cluster totals `E₀·ΔL` against AME2020.

Scale: `E₀ = m_e/(q₀(q₀−1)) = 4.18598136329447589694… MeV` from
`mass_binding_dashboard._constants()`, the constant the production dashboard
multiplies `ln(tr_free/tr_atom)` by. No new scale; every sign, ratio and
residual below is scale-free.

**Word provenance.** The live recompute reproduces #7200's four committed
post-ruling caches (`chi-{deuteron,tritium,helium-3,helium-4}-…-at-q0-50dps`,
`computedAt 2026-09-06`, `q0Anchor: proton`) to `< 1e-40` on every `χ^λ` and
`y_λ` (assertion). **The only committed ⁶Li per-partition cache,
`chi-lithium-6-h18-at-q0-50dps-matrix-m`, is a different object** — its wire
format is sign-only (`convention: sign-only-crossings`,
`pn_split_carried: False`; beans `qou-sgv5` / `qou-fv0s`), so the averaged
interface and intra letters are replaced by bare crossings and isobars are
degenerate. It differs from the live word by up to `3.3e3` in `χ^λ` (one-row
`χ^{[18]}`: cache `1649.44…` vs live) and is **not** a provenance check of
anything here; the probe records the difference and asserts only that the
cache declares the sign-only wire. The live word's own consistency check is
the one-row letter product at every cluster and both words: max error
`< 1e-40` (assertion).

## 2. Which block dominates, and by what margin

| A | n | p(n) | trace argmax (atom), all compositions | runner-up / dominant | share of Σ\|a_λ\| | free argmax |
|---|---|---|---|---|---|---|
| 1–4 | 3–12 | 3–77 | **one-row `[3A]`** (as #7200) | ≤ 0.968 (nnnn) | 0.28–0.91 | `[3A]` at A ≤ 2, `[9,3]` at A = 4 |
| 5 | 15 | 176 | **`[12,3]`** for all six `(Z,N)` | 0.992 (5,0), 0.955, 0.919, 0.833, 0.750, 0.773 (0,5) — runner-up `[15]` for Z ≥ 1, `[11,4]` at (0,5) | 0.25–0.35 | `[12,3]` (`[11,4]` at (5,0)) |
| 6 | 18 | 385 | **`[15,3]`** for all seven | 0.735, 0.720, 0.708, **0.718 (⁶Li, runner-up `[12,6]`)**, 0.779, 0.911, 0.939 | 0.21–0.33 (⁶Li 0.240) | `[13,5]` |
| 7 | 21 | 792 | **`[18,3]`** for Z ≥ 3, **`[15,6]`** for Z ≤ 2 | 0.814, 0.860, 0.883, 0.920 (⁷Be), **0.971 (⁷Li)**; 0.968, 0.977, 0.960 | 0.18–0.28 (⁷Li 0.190) | `[15,6]` |

So the one-row → two-row crossover happens at **A = 5**, not 6 — every A = 5
composition already has `[12,3]` dominant, though at (5,0) only by 0.8 %. The
dominant block is `[3A−3, 3]` from A = 5 to 7 for the proton-rich half and
moves to `[15,6]` at the neutron-rich A = 7 compositions; the margin at ⁷Li is
2.9 %, so "dominant" is a thin statement there. Every margin is `> 1e-3`
(assertion); none of this is an argmax tie.

## 3. Fixed-n chain-edge additivity: exactly the two one-dimensional blocks are additive, and nothing else

| A | n | blocks chain-additive to 1e-40 | which | full-trace residual | dominant two-row block: `L_pp / L_pn / L_nn` | max residual | worst block |
|---|---|---|---|---|---|---|---|
| 3 | 9 | 2 / 30 | `[9]`, `[1⁹]` | 1.1e-50 | (one-row dominant) | 2.8e-51 | `[5,2,1,1]` 2.35 |
| 4 | 12 | 2 / 77 | `[12]`, `[1¹²]` | 1.1e-50 | (one-row dominant) | 1.0e-50 | `[8,3,1]` 3.43 |
| 5 | 15 | 2 / 176 | `[15]`, `[1¹⁵]` | 1.1e-50 | `[12,3]`: −0.3432 / −0.3392 / −0.3765 | **0.0978** | `[7,4,2,2]` 5.38 |
| 6 | 18 | 2 / 385 | `[18]`, `[1¹⁸]` | 3.7e-50 | `[15,3]`: −0.3068 / −0.3256 / −0.3666 | **0.0922** | 8.43 |
| 7 | 21 | 2 / 792 | `[21]`, `[1²¹]` | 5.3e-50 | `[18,3]`: −0.2778 / −0.3136 / −0.3579; `[15,6]`: −0.4430 / −0.4026 / −0.4407 | **0.0962**; 0.158 | `[11,6,2,2]` 8.67 |

(The `[1ⁿ]` sign block is chain-additive because it is the other
one-dimensional character, `σ ↦ −q⁻¹`; under convention D its `y_λ = 0`, so it
never appears in the trace — it is in the table as the second instance of the
Lean invariant, not as a contributor. Identified at A = 3, 4 by direct
enumeration; the probe records the count `2` at every A.) The full trace is
chain-additive to `1e-50` at every A — the `tr_M` bond rule
(`MarkovBondRuleForcesPairwise`) confirmed on the live word up to 21 strands,
`L_pp = ln(1/z_D) = 0.48989938425513485141` to all printed digits.

The residuals of the two-row dominant block are all **negative** and all of
one size, `−0.07 … −0.10` log units (`0.3–0.4 MeV` at `E₀`), on every mixed
composition at A = 5, 6, 7 — the atom's two-row character is *smaller* than
the chain law predicts, i.e. the block binds slightly *more* than its three
edge constants say. So the two-row block's log-weight is **not** a bond
functional. The subset cumulants say what it is instead.

## 4. The typed bond-set decomposition of `log|χ^{λ*}|` at ⁶Li and ⁷Li

### 4a. ⁶Li, block `[15,3]`, interfaces `pp@0, pp@1, pn@2, nn@3, nn@4` (word positions 11, 23, 35, 47, 59); all 32 subsets

| order | cumulants `c(S)` (log units) |
|---|---|
| per edge | pp −0.35172 (both, identical to 8 digits), pn −0.51586, nn −0.69104 (both) |
| pairs, **adjacent** | (pp,pp) −0.0032, (pp,pn) **+0.0078**, (pn,nn) −0.0100, (nn,nn) −0.0268 |
| pairs, **non-adjacent** | (pp@0,pn) −0.0514, (pn,nn@4) −0.0663, **every pp–nn pair −0.0697** (four of them, identical) |
| triples | +0.020 … +0.181, all positive (e.g. (pn,nn,nn) +0.181, (pp,pp,pn) +0.097) |
| quadruples | +0.097 … +0.135, all positive |
| quintuple | **−0.235** — the largest single entry in the table |

Sums: edges `−2.6014`, pairs `−0.4287`, order ≥ 3 `+1.2655`; total
`−1.7646 = −ΔL_sameblock(⁶Li)` (round-trip, assertion). In MeV with the
binding sign (`−E₀ × F`): **edges +10.889, pairs +1.794, order ≥ 3 −5.297;
net connected (all orders ≥ 2) −3.503 MeV**, against the block's total
same-block binding-like value `+7.386 MeV` and AME `31.994 MeV`.

Controls in the same run: one-row `[18]` — every pair and higher cumulant
`≤ 2.9e-50`; full trace — `≤ 3.7e-50`, per-edge `ln z_D = −0.48990` (pp),
`−0.67682` (pn), `−0.90726` (nn), the #7204 bond factors read back as
logarithms.

### 4b. ⁷Li, block `[18,3]`, interfaces `pp, pp, pn, nn, nn, nn`; singletons, all 15 pairs, full set

Per edge: pp −0.29678, pn −0.45793, nn −0.61727 (each type identical across its
copies). Pairs: adjacent (pp,pp) −0.0159, (pp,pn) −0.0116, (pn,nn) −0.0318,
(nn,nn) −0.0470 ×2; non-adjacent (pp@0,pn) −0.0449, (pn,nn@4/5) −0.0590 ×2,
(nn@3,nn@5) **−0.0774**, every pp–nn pair −0.0582 (six). Sums: edges
`−2.9033`, pairs `−0.7425`, total `−2.0390` ⇒ order ≥ 3 (not enumerated
individually) `+1.6068`. MeV, binding sign: **edges +12.153, pairs +3.108,
order ≥ 3 −6.726; net connected −3.618 MeV** against the block's `+8.535 MeV`
and AME `39.245`.

### 4c. What the table says

1. **The two-row block is not letter-multiplicative, at any order.** Pair
   cumulants of `0.03–0.08` log units, triples and quadruples of `+0.1`, a
   quintuple of `−0.24` — none is at the `1e-50` floor the two controls sit
   at. The Lean lemma (§6) says this had to be so for *some* pair of
   letters; the measurement says it is so for every pair.
2. **It is non-local along the chain.** The largest pair cumulants are between
   interfaces that share **no** nucleon block (pp–nn, separated by the whole
   pn interface and two blocks): `−0.0697` at ⁶Li against `−0.0032` for the
   adjacent pp–pp pair — 22× larger. A trace of a `dim > 1` representation
   couples every letter to every other through the path sum; a bond model
   with nearest-neighbour cumulants cannot produce this shape, and a
   locality-based truncation would keep the small terms and drop the large.
3. **The connected series does not decrease with order.** `|c|` runs
   pairs ~0.05 → triples ~0.1 → quintuple 0.24 at ⁶Li. So "the many-body
   correction" is not a perturbative tail on the edge sum; the whole
   inclusion–exclusion is needed to recover the block value.
4. **Its net effect is anti-binding and small.** Pairs add `+1.8 / +3.1 MeV`
   (binding sign) but the higher orders subtract `−5.3 / −6.7 MeV`, so the
   connected content of the dominant block is **−3.5 MeV at ⁶Li and
   −3.6 MeV at ⁷Li**: the wrong sign for the AME shortfall (`+23.5` and
   `+27.8 MeV` beyond `E₀·ΔL`) and an order of magnitude too small. The edge
   sums (`+10.9 / +12.2 MeV`) are the block's largest part, and they are a
   chain-edge functional exactly as at `A ≤ 4`.

## 5. Growth with A, and the typed Ursell cumulants

| nuclide | AME B | `E₀·ΔL` (dominant) | AME / `E₀·ΔL` | same-block part | switch | full trace `E₀·ln(tr_f/tr_a)` | B/A AME | B/A dominant |
|---|---|---|---|---|---|---|---|---|
| ²H | 2.2246 | −0.0230 | −96.5 | −0.0230 | 0 | 2.833 | 1.112 | −0.012 |
| ³H | 8.4818 | 0.4137 | 20.5 | 0.4137 | 0 | 6.631 | 2.827 | 0.138 |
| ³He | 7.7180 | −0.4598 | −16.8 | −0.4598 | 0 | 4.884 | 2.573 | −0.153 |
| ⁴He | 28.2957 | 3.9286 | 7.20 | −0.0230 | 3.952 | 8.682 | 7.074 | 0.982 |
| ⁵He* | 27.5607 | 6.3787 | 4.32 | 6.3787 | 0 | 12.479 | 5.512 | 1.276 |
| ⁵Li* | 26.3307 | 6.1781 | 4.26 | 6.1781 | 0 | 10.732 | 5.266 | 1.236 |
| ⁶He | 29.2711 | 8.6483 | 3.38 | 7.6208 | 1.027 | 16.277 | 4.879 | 1.441 |
| ⁶Li | 31.9940 | 8.5083 | 3.76 | 7.3864 | 1.122 | 14.530 | 5.332 | 1.418 |
| ⁶Be* | 26.9235 | 8.2651 | 3.26 | 7.0516 | 1.213 | 12.783 | 4.487 | 1.378 |
| ⁷He* | 28.8614 | 11.5291 | 2.50 | 11.5291 | 0 | 20.075 | 4.123 | 1.647 |
| ⁷Li | 39.2451 | 11.4683 | 3.42 | 8.5354 | 2.933 | 18.328 | 5.606 | 1.638 |
| ⁷Be | 37.6008 | 11.2169 | 3.35 | 8.1972 | 3.020 | 16.581 | 5.372 | 1.602 |

(`*` = unbound to nucleon emission in AME2020; all MeV.) Two readings:

* **`B/A` of the dominant summand rises without a plateau** — 0.98, 1.26,
  1.43, 1.63 at A = 4, 5, 6, 7, about `+0.2 MeV` per nucleon per unit of A —
  while AME sits at 4.1–7.1 and saturates. The ratio AME / `E₀·ΔL` falls
  7.2 → 4.3 → 3.5 → 3.4, i.e. the gap narrows only because the model term
  keeps growing linearly in `A` beyond the edge count; it is not approaching
  the AME shape.
* **The `switch` (free-side argmax surplus) vanishes at A = 5 and at the
  neutron-rich A = 7 compositions** — there the free word's largest term is
  the same block as the atom's — and is `1.0–3.0 MeV` elsewhere. The
  same-block part `7.4–8.5 MeV` is the two-row block's own content (§4).

Typed complete-graph cumulants of `ΔL` to order 7 (log units; every
composition at a given A is within ±10 % of the others, so one representative
per order): `b₂ ≈ ∓0.104` (pp/nn) `−0.006` (pn); `b₃ ≈ +0.006` (mixed);
`b₄ ≈ +0.94`; **`b₅ ≈ −3.2`, `b₆ ≈ +7.1`, `b₇ ≈ −13.1`** — alternating and
growing (`E₀×`: `−13.4`, `+29.8`, `−54.9 MeV` for the ⁵Li/⁶Li/⁷Li
compositions). They are dominated by the `switch` column (`−4.9, +15.4,
−37.3`) with the same-block column alternating the other way (`+1.9, −8.8,
+25.6`). As #7200 noted at A ≤ 4, complete-graph cumulants of a *chain*
quantity are the missing-edge accounting and are not connected many-body
terms; at A ≥ 5 the fixed-n / subset decomposition of §3–4 is the honest
carrier of the question, and the Ursell table is recorded for completeness
and for the round-trip check (⁷Li, `< 1e-50` at 60 dps). The full-trace
control column stays `±0.49 / 0.68 / 0.91` at every order (`b₂ = ln(1/z_D)`),
as the bond rule predicts. The uniform-`e₂` frame is defined at `A ≤ 4`
only, where the numbers are #7200's (`e₂ = −0.023`, `b₃(³H) = +0.483`,
`b₃(³He) = −0.391`, `b₄ = +3.883 MeV` vs AME `2.225 / +1.808 / +1.044 /
+9.243`); it is not extended, because at A ≥ 5 it would need like-species
triple targets AME does not provide.

## 6. The Lean, and its verification

`QOU/Mass/MixedSpectrumCharacterNotLetterMultiplicative.lean`, generic
`[Field R]` (`q⁻¹` appears in the Hecke relation; no `ℝ`, no ordering, no log):

| declaration | statement |
|---|---|
| `quadratic_of_rightLetterMultiplicative` | if `χ : H →ₗ[R] R` satisfies `χ(xσ) = q'χ(x)` for all `x` and `σ² = (q−q⁻¹)σ + 1`, then `(q'² − (q−q⁻¹)q' − 1)·χ(1) = 0` |
| `root_of_rightLetterMultiplicative` | with `q ≠ 0`, `χ(1) ≠ 0`: `q' = q ∨ q' = −q⁻¹` |
| `mixedSpectrum_not_rightLetterMultiplicative` | if `χ(1) = d₊ + d₋`, `χ(σ) = d₊q − d₋q⁻¹` with `d₊ ≠ 0 ≠ d₋` and `q + q⁻¹ ≠ 0`, then **no** `q'` makes `χ` right-letter-multiplicative for `σ` |
| `twoRow_not_rightLetterMultiplicative` | the same with natural multiplicities `d₊, d₋ ≥ 1` over `CharZero R` — the shape of a two-row block `(n−k,k)`, `k ≥ 1`, `n−k ≥ 2`, where both eigenvalues `q` and `−q⁻¹` of `σ` occur |
| `letter_multiplicative_iff_sigma` | an affine letter `c·σ + d·1` (`c ≠ 0`) is right-multiplicative with scalar `φ` iff `σ` is with `(φ−d)/c` — so the pp / pn / nn interface letters inherit the obstruction verbatim |

Verified: `lean -DautoImplicit=false -s 65536` exit 0 with `LEAN_PATH` set to
the restored Mathlib olean tree only (Mathlib-only imports:
`Algebra.Algebra.Defs`, `Algebra.Module.LinearMap.Defs`, `Tactic.Ring`,
`Tactic.FieldSimp`, `Tactic.LinearCombination`); compiled to a scratch olean and
`#print axioms` on all five: `[propext, Classical.choice, Quot.sound]`.
`scripts/check-sidecars.sh`: *"library Lean — no ℝ, generic OK"*; its one ⚠ is
the pre-existing `docs/precision-goals.md` hit, untouched here. No `lake`, no
cache restore, no QOU import (the coordinator's disk constraint).

**What it proves and what it does not.** It proves the one-row argument of
#7200 is *structurally* confined to one-dimensional blocks: a character
carrying both Hecke eigenvalues admits no per-letter factor, so a two-row
block's log-weight is not a bond functional *by any general argument*. It does
**not** prove the connected term is non-zero for a given word (§4 measures
that), and it says nothing about the full trace, whose bond rule is a
statement about `tr_M` and stands (§3 control).

## 7. Scope verdict

* **(b) — the #7200 exclusion does not extend past A = 4.** Invariant:
  `mixedSpectrum_not_rightLetterMultiplicative` (Lean, sorry-free) + the
  measured two-row dominance at every composition with `5 ≤ A ≤ 7` (§2, margins
  `> 1e-3`). At `A ≥ 5` the dominant summand's log-weight is *not* a
  chain-edge functional plus a word-free weight, and a connected many-edge
  term *does* live there.
* **(a) — that term, alone, does not reproduce AME at A = 5–7.** Measured on
  one construction (the live word, the trace's argmax, convention D, proton
  pin): the connected content of the dominant block is anti-binding,
  `−3.5 MeV` (⁶Li) / `−3.6 MeV` (⁷Li), against shortfalls of `+23.5` /
  `+27.8 MeV`; `B/A` of the dominant summand grows linearly with no plateau.
  This constrains the magnitude and sign of *this* term; it does not exclude a
  two-row block from a multi-term closure, and it does not touch classes B or
  D of the enumeration.
* **Not asserted:** that the connected term is "the" extensive object.
  Its order-by-order growth and non-locality (§4c) are properties of a global
  trace, not of an additive extensive term, and are reported as such.

## 8. Implications

* **`qou-brng`'s dominant-summand channel is now measured on both sides of the
  one-row / two-row boundary.** `A ≤ 4`: no connected term (#7200, (b)).
  `A = 5–7`: connected terms at every order, net anti-binding, ~3.5 MeV, (a).
  The channel does not supply a positive extensive term at any A tested.
* **`MultiplicityNotExtensive.lean`'s header** (*"the dominant summand's own
  log-weight is untouched and is the live remainder"*) is now out of date in
  both directions; a follow-up docstring should read: *tested 2026-09-12 — at
  `A ≤ 4` the dominant block is one-row and its log-weight is a bond functional
  plus `log y_(3A)` (#7200); at `5 ≤ A ≤ 7` it is two-row, is not
  letter-multiplicative (`MixedSpectrumCharacterNotLetterMultiplicative`), and
  its connected content is anti-binding, `−3.5 MeV` at ⁶Li (#7211); the
  remainder moves to classes B/D.* Not edited here (ask-first rule; same as
  #7200's disposition).
* **`BindingConcentration.lean`'s header** lists the *binding-sum* argmax
  `(5,1)/(6,3)/(9,3)` and calls it the largest `|y·χ|`; #7200 already
  recorded that the two argmaxes disagree at `A ≤ 4`. This PR adds that the
  **trace's** argmax becomes two-row `[3A−3,3]` at A = 5 and `[15,6]` at
  neutron-rich A = 7 — so a docstring correction should state *which* argmax
  and at *which* A. Not edited here.
* **The sign-only `matrix-m` cache family is not the live word** (§1) — any
  consumer reading `chi-lithium-6-h18-at-q0-50dps-matrix-m` as "the ⁶Li
  characters" gets isobar-degenerate, colour-blind values that differ from the
  live word by up to `3.3e3`. Already known (`qou-sgv5`, `qou-fv0s`); recorded
  again because this session nearly asserted against it.
* **A non-local pair structure is a testable prediction of the trace
  picture** — the pp–nn cumulant between non-adjacent interfaces exceeding the
  adjacent pp–pp one by 22× would not arise in any bond-local model. It is
  recorded, not interpreted.

## 9. Options (judgement, not findings)

1. **Record and stop** (default; what this PR does). Both halves of the
   dominant-summand channel are measured; `qou-brng` stays open on classes
   B/D. Cost nil; nothing moves.
2. **Enumerate the 64 ⁷Li subsets and the ⁶He/⁶Be tables** to see whether the
   order-≥3 sum's sign is stable across isobars. One background run
   (~15 min), no new mathematics; buys a cross-isobar check of §4c(4).
   Recommended only if someone wants to cite "anti-binding" beyond two
   nuclides.
3. **Attack the non-locality structurally**: the pair cumulant between
   interfaces `e, f` on a two-row block is a function of the path sum through
   the blocks between them; a closed form for `c_{(n−k,k)}({e,f})` in terms of
   the Hoefsmit matrices would say whether the 22× ratio is a `k`-dependent
   universal or a word artefact. Cost: a session; risk: it is a statement
   about the block, not about binding, and the anti-fit rules apply if any
   number is compared to AME.
4. **Follow the pair term because it is positive (+1.8 MeV) and drop the
   higher orders.** Not recommended: it is a truncation chosen for its sign,
   the higher orders are larger than the pairs, and §NO FITTING names exactly
   this move.

Recommendation: **1**; **3** is the only continuation with content, and it is
mathematics about the two-row character rather than about the binding.
