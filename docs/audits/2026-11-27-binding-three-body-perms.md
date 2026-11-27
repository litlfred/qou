# Three-nucleon γγ bond words that are not pair products

**Date** 2026-11-27 · **Brief** C2 front A (compute-accuracy epic `qou-myts`) · **Bean** `qou-brng`
**Answers** open item 3 of `docs/audits/2026-11-27-classical-log-binding-cycle-count.md`
**Probe** [`computations/probes/binding_three_body_perms/`](../../computations/probes/binding_three_body_perms/): mpmath 40 dps, convention D, proton pin, corpus seminormal reading 3, independent Schur–Weyl trace on every passing word (max deviation 2.2e-40). 6/6 checks. 2727 words, about 30 min on one core.
**Scope** (a) throughout. Nothing fitted, selected or wired. AME is not read by the probe.

## 0. Result

On nine strands (A = 3, nucleons `V³` on strands 0–2, 3–5, 6–8), a bond word can fail to be a
product of its pair bonds, and 87 of the 116 words that pass reading 3 at `q₀` do fail. None of them
earns a positive **classical** `b₃`: every q₀-passing word has classical `b₃ ∈ {0, −2}` merge units.
The words with classical `b₃ = +2` exist (671 in the population, 30 of them pass reading 3 at `q = 1`)
and **all fail reading 3 at `q₀`**. No passing word merges more than 4 components, against
`3·m(²H) = 6`. Positive `b₃` does occur at `q₀` (93 of 116 passing words, up to +0.655 merge units),
but it is pure deformation: the classical part of every one of them is 0.

## 1. Definitions

Letters: `V(s) = σ_s σ_{s+1}⁻¹`, `s = 0…6`. `V0`, `V3`, `V6` lie inside nucleon 1, 2, 3; `V1`, `V2`
on the pair (12); `V4`, `V5` on the pair (23). No letter spans nucleons 1 and 3. Bond words contain
`V1` or `V2`, and `V4` or `V5`.

- **Word-level product** (the hypothesis of `classicalB3_nonpos_of_product`): `π(K)` equals the
  product, in either order, of the permutation of its (12) letters and of its (23) letters, for some
  placement of each `V3` on one side.
- **Intrinsically three-body**: `π(K) ∉ Sym{0..5}·Sym{3..8} ∪ Sym{3..8}·Sym{0..5}` (141048 of the
  362880 permutations are in the union). This is stronger: no pair words at all reproduce `π(K)`
  with two factors. Check K4: intrinsic implies word-level non-product.
- **`b₃`**, by inclusion–exclusion over the letters supported in each nucleon set:
  `b₃ = B(K) − B(K|12) − B(K|23) − B(K|13) + B(K|1) + B(K|2) + B(K|3)`, in merge units
  (`E₀ ln 2 = 2.930268` MeV). Classically each `B` is a merge count; at `q₀`, `B = −E₀ ln r`. For
  `V3`-free words this is exactly the Lean `classicalB3`, and check K3 confirms the Lean theorem on
  them (no `V3`-free word-level product has classical `b₃ > 0`).

Population: every bond word of length 1–4 (1360) and, at length 5, every word-level non-product word
plus every word with nonzero classical `b₃` (1367). The length-5 product words with classical
`b₃ = 0` were **not** run.

## 2. Classification (exact)

| length | non-product words | of which intrinsic | first appears |
|---|---|---|---|
| 3 | 2 | 0 | `V2V4V2`, `V4V2V4` |
| 4 | 52 | 0 | |
| 5 | 840 | 32 | intrinsic three-body needs length ≥ 5 |

Non-product words come from interleaving letters that share a strand: `V2` and `V4` (strand 4), and
`V3` against both junctions.

## 3. Reading 3 at q₀

| population | product? | intrinsic | merges | classical `b₃` | words | pass q₀ | pass `q = 1` | `−ln r / ln 2` (passing) | `b₃(q₀)` (passing) |
|---|---|---|---|---|---|---|---|---|---|
| len ≤ 4 | no | no | 2 | 0 | 10 | 4 | 2 | 1.523 … 2.467 | +0.218 … +0.480 |
| len ≤ 4 | no | no | 4 | 0 / +2 | 24 / 4 | 0 | 5 / 1 | — | — |
| len ≤ 4 | no | no | 6 | 0 | 16 | 0 | 0 | — | — |
| len ≤ 4 | yes | no | 2 | 0 | 61 | 24 | 25 | 1.542 … 2.446 | +0.173 … +0.218 |
| len ≤ 4 | yes | no | 4–8 | 0 / +2 | 1245 | 0 | 114 | — | — |
| len 5 | no | no | 2 | 0 | 84 | 58 | 59 | 1.512 … 2.505 | −0.302 … +0.655 |
| len 5 | no | no | 4 | 0 | 362 | **9** | 62 | 3.492 … 3.732 | +0.223 … +0.331 |
| len 5 | no | yes | 2 | 0 | 16 | 16 | 16 | 1.509 … 2.499 | −0.366 … +0.624 |
| len 5 | no | yes | 4 | 0 | 16 | 0 | 0 | — | — |
| len 5 | yes | no | 2 | −2 | 5 | 5 | 5 | 1.971 | −2.067 |
| len 5 | either | — | 2–8 | +2 | 620 | 0 | 26 | — | — |

(Rows with zero passing words at `q₀` and the same outcome are merged; the full table is in the
witness under `data.table`.)

Facts read off the table:

1. **Classical `b₃ > 0` is excluded by reading 3 at `q₀` in this population.** 671 words carry it,
   30 pass reading 3 classically, none passes at `q₀`. This is a measurement (scope a), not a theorem.
2. **Merges.** Every q₀-passing word merges 2 or 4. Four is reached only at length 5, by 9 words, all
   word-level non-products containing `V3` and `V6` (for example `V4V2V3V4V6`, `−ln r = 3.732·ln 2`).
   None reaches `3·m(²H) = 6`. This qualifies the ceiling audit's "the A = 3 cap is 2": that holds
   through length 4; at length 5 non-product words pass with 4 merges.
3. **Intrinsically three-body words** (16 pass, all merging 2) behave like the rest: `b₃(q₀)` from
   −0.366 to +0.624 merge units, classical part 0.
4. **Positive `b₃` at `q₀` is deformation only.** 93 of 116 passing words have `b₃(q₀) > 0`; their
   classical `b₃` is 0. The largest is `V4V2V4V4V2` at +0.655 merge units. The five pair-product
   words with classical `b₃ = −2` (e.g. `V2V3V3V4V3`) sit at −2.067.

## 4. Scorecard (not a derivation, not a selection)

AME symmetric `b₃` is 1.4262 MeV = 0.487 merge units. The passing `b₃(q₀)` range is −2.07 to +0.66
merge units, so it brackets that value, which says nothing: the range spans the target and no word is
chosen. Under part 1's framing the classical route to positive `b₃` is the one closed here; what
remains is the deformation term, which is of the right order (a few tenths of a merge unit) and of
either sign.

## 5. Open

1. Whether "classical `b₃ > 0` ⇒ reading 3 fails at `q₀`" holds beyond length 5. A structural route
   would be a theorem; nothing here proves one.
2. Run the remaining length-5 product words (classical `b₃ = 0`) to complete the length-5 merge table.
3. The selection question (which bond word is the nucleus) is unchanged and remains an owner decision;
   nothing here selects one.
