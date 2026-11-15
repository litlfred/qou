# The three-way wrong sign on `b₃` is one root — and the escape hatch as written is not sufficient

> **2026-11-15 scoping note.** The magnitudes below are computed on the single-crossing interface letters of `atom_braid_word_3A`, which the γγ rule (owner, 2026-11-15) no longer treats as canonical. They stay as a record. The Lean theorems take generic bond weights and still stand. See [`2026-11-15-gg-rule-rescopes-old-letter-binding.md`](2026-11-15-gg-rule-rescopes-old-letter-binding.md).

**Date.** 2026-09-12
**Bean.** `qou-q8vl`; parents `qou-brng`, `qou-rwhv`, `qou-ix0x`, `qou-m8f3`.
**Branch / PR.** `claude/b3-sign-one-root-2026-09-12`, #7226.
**Lean.** [`QOU/MassTheory/B3SignOneRoot.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/B3SignOneRoot.lean)
— `lake build QOU.MassTheory.B3SignOneRoot` exit 0; 13 declarations; `#print axioms`
`propext` / `Classical.choice` / `Quot.sound`, **no `sorryAx`**.
**Probe.** [`computations/probes/b3_sign_one_root_probe.py`](../../computations/probes/b3_sign_one_root_probe.py)
— **10/10**, exit 0; mpmath 60 dps, sympy exact for every algebraic identity, proton pin
`Q_50_DIGIT_STR`, convention D, `bring_color_weighted`. No witness; nothing wired.
**Scope.** **(b)** for the sign, invariant in §5. **(a)** for everything else.

---

## 0. The question

Three constructions give the connected three-body channel the wrong sign against AME2020:

| route | PR | what it gives | AME wants |
|---|---|---|---|
| count channel | #7193 | `countChannel > 0`, repulsive, and 25.27× short | attractive |
| Ursell / Mayer cumulant | #7198 | `b₃ = −φᵀ₃ < 0` | `+1.8081` (³H), `+1.0443` (³He) MeV |
| dominant summand | #7200 | exactly chain-edge additive, `b₃ = 0` | as above |

They read as three separate failures, and the arc has been treating them that way. They are
one, and the escape hatch that both the Ursell audit §4 and the AGENTS.md "Extensive-term
frontier" bullet name is **not sufficient** to get out of it.

## 1. The root: every derived bond scalar is confined to `(0,1)`

Measured from the live source of truth (`INTERFACE_COEFS`, `pyhecke.constants`):

| bond | `(c, d)` | what it is | `μ = z_D + d` | `g = μ − 1` |
|---|---|---|---|---|
| pp | `(1, 0)` | bare `σ` | `0.6126880371464652516` | `−0.3873119629` |
| pn | `(1, d_pn)` | colour-weighted (R3) | `0.5082297893767389626` | `−0.4917702106` |
| nn | `(1, −h)` | `σ⁻¹` via the Hecke relation | `0.4036277383508259362` | `−0.5963722616` |

`d ≤ 0` on all three — the family runs from `σ` at one end to `σ⁻¹` at the other — so
`μ ≤ z_D < 1` and every Mayer variable is negative. The `nn` letter is `σ⁻¹` on the nose:
`μ_nn = 1/(q(q²+1))` reproduces the live value with `|dev| = 0.0` at 50 dps (CHECK 2).

The confinement itself is **not new** — it is
`QBeta.SingleCrossingAlwaysBinds.interface_mem_Ioo`, sorry-free since 2026-08. What is new is
what it does to `b₃`.

## 2. 🛑 The correction: uniform attraction does not escape

The production `A = 3` word is a **chain**. `atom_braid_word_3A` lays `A−1` interfaces in a
line, so ³H `= p–n–n` carries `{pn, nn}` and ³He `= p–p–n` carries `{pp, pn}`; the third pair
carries no letter. On a chain the third Ursell function collapses from four connected spanning
graphs to one:

$$\varphi^T_3 = g_{01}\,g_{12}, \qquad b_3 = -\,g_{01}\,g_{12}.$$

A **product of two** Mayer variables does not change sign when both factors flip. Measured
(CHECK 4), reflecting every live bond to attractive (`μ > 1`, magnitudes kept):

| atom | live `b₃` | all bonds attractive |
|---|---|---|
| ³H | `−0.293278112721` | `−0.293278112721` |
| ³He | `−0.190468485549` | `−0.190468485549` |

Identical, because only the product enters. So the standing wording —

> "Within Mayer a positive term needs a bond factor above 1 (attractive channel; none in the
> production word)"

— is **necessary but not sufficient**. On a two-bond chain what is needed is that **exactly
one** bond exceed 1 (`b3corpus_chain_pos_iff`). A uniformly attractive word is still
wrong-signed, and reading the existing sentence as "find an attractive letter and the sign
follows" is a route that cannot work.

*(The live `φᵀ₃` figures reproduce the Ursell audit §3a exactly — `0.293278` and `0.190468` —
computed here through an independent path, which is why they are quoted rather than re-derived.)*

## 3. The chain is covered by neither standing theorem

| theorem | why it misses the production shape |
|---|---|
| `UrsellPartitionFunctionB3.b3corpus_neg` | hypothesis is `0 < f₁₃ < 1` **strictly**; the chain's absent bond sits at exactly `f = 1` |
| `AggregatorConvexity.wMult_b3_nonpos` | the **equal-bond** statement; measured, the two chain bonds differ by `0.1046` (³H) and `0.1045` (³He) — CHECK 10 |

`b3corpus_chain_neg` supplies the distinct-bond chain. This gap is why "the exclusion is
proved" has been said about a shape it was not proved for.

## 4. The required pattern is sign-mixed — and it is the two-nucleon spectrum

³H needs `sign(g_pn) ≠ sign(g_nn)`; ³He needs `sign(g_pp) ≠ sign(g_pn)`. Enumerating the four
sign assignments (CHECK 5), **exactly the two sign-mixed ones** make both chains positive:

| `(sign g_pn, sign g_like)` | both chains `b₃ > 0` |
|---|---|
| `(+, +)` | no |
| `(+, −)` | **yes** |
| `(−, +)` | **yes** |
| `(−, −)` | no |

Since `B_e = −α·log μ_e` is positive exactly when `μ_e < 1`, the branch `(−, +)` reads:
**the unlike pair binds and the like pairs do not.** That is the observed two-nucleon
spectrum — the deuteron is bound, the diproton and the dineutron are not.

So `b₃ > 0` and the correct two-body boundness pattern are **one condition**, not two. The
live model has all three `g < 0`: it binds the diproton and the dineutron, with `b₂(nn) >
b₂(pn) > b₂(pp)`, i.e. the dineutron *most* bound. The same defect that gets the two-body
isospin structure backwards is what forces `b₃ < 0`.

This is an observation about what the condition **is**. Nothing here constructs a letter to
meet it, and §6 says why that restraint is required rather than merely cautious.

## 5. Verdict and invariant

**Scope (b)**, invariant: **the chain product structure of `φᵀ₃` together with `(0,1)`
confinement of every derived bond scalar.** On a two-bond chain, bonds sharing a side of `1`
give `b₃ < 0` — attraction included — so no uniform change of the bond family escapes, and
both derived families are confined:

* **production letters** — `d ≤ 0` caps `μ` at `z_D < 1` (`interface_mem_Ioo`);
* **isospin projector channels** — excluded by an **identity, not an inequality**:
  `μ₊ + μ₋ = 1` (`InterfaceScalar.mu_sum_eq_one`, symbolic residual `0` in CHECK 9, for any
  `z` and any `q`). An attractive channel `μ₊ > 1` forces `μ₋ < 0`, where `−α·log μ₋` is not a
  real number. The isospin route cannot host a sign-mixed pair **even in principle**; measured
  values `μ₊ = 0.75270211325196540159`, `μ₋ = 0.24729788674803459841`.

## 6. What this does NOT claim — three, and two of them are corrections to me

**(a) A bond above 1 is NOT the only escape.** `AggregatorConvexity.b3Agg_nonneg_of_convexOn`
gives `b₃ ≥ 0` from an aggregator convex through the origin, with every bond still inside
`(0,1)`. Everything above is about the **multiplicative** assembly only. Writing "the only way
out is `μ > 1`" would be false, and the convexity route is a live and independent alternative
(bean `qou-82mc`).

**(b) `μ(σ^m)` does NOT alternate by parity — my own predicted pattern, refuted.** Having
derived `μ(σ²) = (q⁴+1)/(q²+1) > 1 > μ(σ³)` symbolically, the tempting reading is "even powers
attract, odd repel". Measured over `m = −2 … +8` (CHECK 7), `μ > 1` at
`m = 2, 4, 5, 6, 7, 8` — **`+5` and `+7` are odd**. The pattern is false, it was a
two-data-point extrapolation, and it is recorded here so it is not re-derived. The values
reproduce `stacked_interface_writhe_normalised_probe.py` independently.

**(c) `σ²` is NOT proposed as a letter.** `stacked_crossing_gt_one` does exhibit `μ > 1`, and
`σ²` is the minimal Hecke element reaching it. But the topological argument that would select
it assigns `σ²` to the **distinguishable** pair (identical particles already close a loop at
`σ`; distinguishable ones need `σ²`), and bean `qou-kj4v` records that this assignment runs
backwards — it **binds the diproton and unbinds the deuteron**, which
`content_keyed_interface_refuted` and `mu_singlet_lt_mu_triplet` already exclude. Adopting
`σ²` on the like pairs *because* it yields `b₃ > 0` is selection against the target, which
AGENTS.md §"NO FITTING" names explicitly. **The gap stays open.**

## 7. Proposed re-scoping (owner-facing — nothing edited)

Following the precedent the Ursell audit set for its own bullet, **AGENTS.md is not edited
here**; the proposed wording is put to the owner in the #7226 body. The sentence at issue is
the "Extensive-term frontier" bullet 4 parenthesis, *"within Mayer a positive term needs a
bond factor above 1"* — true, and incomplete in a way that makes the escape look reachable by
a uniform change of letter. A one-clause amendment naming the sign-mixing requirement would
close it.

## 8. What is still open

* **`qou-brng` is untouched.** This is a statement about the sign, not the magnitude. The
  chain `|b₃|` at the live bonds is `0.293` / `0.190` in bond units against AME targets that
  are 6.2× and 5.5× larger once scaled — the magnitude problem is unchanged.
* **Whether any admissible letter can supply the sign-mixed pattern from a derivation** rather
  than by selection. Both derived families are now excluded, so this needs a third family, and
  the corpus does not have one.
* **The convexity route** (`qou-82mc`) reaches `b₃ ≥ 0` without any bond leaving `(0,1)` and is
  not analysed here.
