# `q_cross(n)` is not a structured sequence, the Z=N isospin pattern breaks under a fixed-n control, and q₀'s position is COINCIDENTAL (0.31 bits)

**Date:** 2026-08-08 · **Branch:** `claude/deltalambda-qcross-trend-2026-08-08` · **PR #4836**
**Bean:** `qou-prjo` (stays **OPEN** — nothing here closes the binding magnitude) · **Tier:** analysis / structural probe
**Probes:** [`threerow_qcross_trend_probe.py`](../../computations/deltalambda/threerow_qcross_trend_probe.py) · [`threerow_isospin_parity_probe.py`](../../computations/deltalambda/threerow_isospin_parity_probe.py)
**Witnesses:** `threerow-qcross-trend.witness.json` · `threerow-isospin-parity.witness.json`
**Lean:** [`WenzlLevelStratum.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/WenzlLevelStratum.lean) (sorry-free, `lean`-direct exit 0)
**Predecessors:** #4829 (origin) · #4832 (A-dependence + ⁴He + Lean overtake). **This PR is stacked on #4832** — it imports `threerow_chi_sparse.py`, which is not on main.

`free_parameters = 0`. Experimental proton anchor. AME never used — not as input, not as target. Layer-pure.

---

## 0. Three questions, three negative answers — and the negatives are the result

The object is #4829's Δ_λ-weighted ≥3-row archimedean trace, with the PROVED
value-only `Δ_λ = (−1)^{n(λ)}·dim V_λ`:

```
F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3}  y_λ(q) · χ^λ(β_K; q) · Δ_λ
G_n(q) = Σ_{λ ⊢ n,   ℓ(λ) ≥ 3}  y_λ(q) · Δ_λ            (character-free companion)
```

| question | answer |
|---|---|
| **Is `q_cross(n)` monotone / structured?** | **NO** — existence is *sporadic*, values *oscillate*, no convergence |
| **Is it derivable?** | **Exactly algebraic, but no closed form** — irreducible degree 54 / 110 / 224 |
| **Is q₀'s position meaningful?** | **COINCIDENTAL** — 0.309 bits, 91 natural constants in the window |
| **Does the Z=N / Z≠N pattern survive?** | **NO — it breaks under a fixed-n control** (it is an n-effect) |

---

## 1. 🛑 Reframing first: half the prior "trend" was measured off-branch

**(BG-1) The `y_λ` normaliser is closed-form and never vanishes.** By dual Cauchy
(`Σ_μ f^μ s_μ = p_1^n`):

```
Z(q) = Σ_μ f^μ s_μ = ((1 − Q^r)/(1 − Q))^n        (max rel err 2.8·10⁻⁴¹)
⇒ y_λ = s_λ · ((1 − Q)/(1 − Q^r))^n
```

`Z > 0` throughout `(1, q*)`, so `sgn G_n = sgn S_n` with `S_n := Σ_{ℓ≥3} s_λ·Δ_λ`.
**The normaliser can neither create nor destroy a crossing** — which matters,
because a bisect-on-sign-change scan cannot by itself distinguish a zero from a
pole. This also gives an independent path to `y_λ` (used for all cross-validation
below) that never calls `y_lambda_at_q0_mpmath`.

**(BG-2) The Wenzl level eigenvalue has a POLE; above it the level is complex.**
With `u = √q`, `Q = u⁴`:

```
Q^r = u³ / D(u),      D(u) = −u⁶ − u⁴ + u³ + u² + 1
u*  = 1.13068544546204…      q* = u*² = 1.27844957657969…
```

| q | Q^r | effective level `r = log(Q^r)/log(Q)` |
|---|---|---|
| 1.05 | +1.2427 | 2.2267 |
| **q₀ = 1.10998** | +1.7203 | **2.5995 (real)** |
| 1.25 | +10.594 | 5.2887 |
| 1.30 | −14.147 | **5.049 + 5.987 i** |
| 1.45 | −1.8281 | **0.812 + 4.228 i** |

**`(1, q*)` is the real-level branch, and q₀ lies inside it.**

> **CORRECTION to the A-dependence read (#4832).** The n=9 crossings at
> q ≈ 1.4285 (³He) / 1.4617 (T) lie **above q\***, where `s_λ(1,Q,…,Q^{r−1})` has
> **no real level**. Comparing `q_cross(6) = 1.054` (r = 2.23, real) against
> `q_cross(9) ≈ 1.43` (r complex) samples two different analytic regimes, not one
> monotone trend. **The arithmetic of #4832 reproduces exactly here** — only its
> reading as a *trend* is withdrawn. On the real-level branch T and ³He have **no**
> crossing, which *extends* #4829's original scope-(a) statement rather than
> overturning it.

**(BG-3) The level-integer ladder — the sequence that IS structured.** `s_λ = 0`
whenever a cell has `r + c(x) = 0`; the minimum content of λ is `−(ℓ(λ)−1)`, so
**at integer level `r = k` every λ with `ℓ(λ) > k` is annihilated**. Solving
`r(q_k) = k` gives the explicit integer polynomial
`Σ_{j<k} u^{4j+3} = u^{4k} + u^{4k+2}`:

| k | q_k | k | q_k |
|---|---|---|---|
| 2 | **1.0 exactly** | 6 | 1.25949216919646 |
| 3 | **1.15416065226449** | 7 | 1.26749218993459 |
| 4 | 1.21589360027966 | 8 | 1.27199886488203 |
| 5 | 1.24473537017348 | 9 | 1.27460456690423 |

Strictly increasing, accumulating at `q*`. Verified: at `q_3` (r=3) the three-row
λ have `|s_λ| ≈ 4.8·10¹` while every `ℓ(λ) ≥ 4` gives `≈ 10⁻⁵⁰` (zero at 50 dps).

**This explains an observation #4829 recorded but could not account for.** Since
`r → 2⁺` as `q → 1⁺`, the **entire ℓ≥3 stratum degenerates at q=1** — which is
*why* `F_D(1.0001) = +8.05·10⁻⁵` and the `G` values sit at O(10⁻⁵)–O(10⁻⁴) there.
It is the k=2 rung, not a deuteron accident.

**q₀ on the ladder:** `r(q₀) = 2.5995155…` — **not an integer, on no rung**;
`q₀ ∈ (q_2, q_3) = (1, 1.15416…)`.

---

## 2. Q1 — MONOTONE? No: sporadic existence, oscillating values

Character-free `G_n` on the real-level branch, n = 3…23 (50-dps mpmath, 220-point
geometric grid):

| n | crossings | n | crossings | n | crossings |
|---|---|---|---|---|---|
| 3,4,5 | — | 12 | — | 18 | **1.100181** |
| 6 | **1.024447** | 13 | **1.159842** | 19 | **1.169716** |
| 7 | — | 14 | — | 20 | **1.151196** |
| 8 | **1.260370** | 15 | **1.155781** | 21 | **1.164540**, 1.229598 |
| 9, 10 | — | 16 | — | 22 | **1.163819** |
| 11 | **1.139658** | 17 | **1.163274** | 23 | **1.155959**, 1.220194 |

- **Existence is sporadic** — none at all for n ∈ {3,4,5,7,9,10,12,14,16}. Whether
  a crossing exists is a two-endpoint sign parity (`sgn S_n(1⁺)` vs `sgn S_n(q*⁻)`)
  that follows no pattern in n.
- **Values oscillate.** n=6 (1.0244) is the smallest, n=8 (1.2604) the largest;
  from n=11 on they wander inside ≈ [1.10, 1.17], with a second branch near
  1.22–1.23 appearing at n=21, 23.
- **No convergence**, no asymptotic law, and the sequence is not even
  everywhere-defined.

**`q_cross(n)` is NOT a structured sequence.** The n=6 → n=9 "increase" that
motivated the question was two points, one of them off-branch (§1).

Character-dressed isotopes on the real-level branch:

| K | n=3A | (Z,N) | F(q₀) | crossings on (1, q*) |
|---|---|---|---|---|
| **D** | 6 | (1,1) | −1.94966·10⁻¹ | **1.053650** |
| T | 9 | (1,2) | −2.31816 | **none** |
| ³He | 9 | (2,1) | −2.80646 | **none** |
| **⁴He** | 12 | (2,2) | −5.94688 | **1.020923** and **1.207893** (two) |

---

## 3. Q2 — DERIVABLE? Exactly algebraic, irreducible degree ≥ 54; no closed form

`Q = u⁴` and `Q^r = u³/D(u)` are **rational in `u = √q` with integer
coefficients**, so `S_n` is a rational function of `u` over ℤ and **every crossing
is an algebraic number** whose minimal polynomial is computable exactly.

Computed in sympy with exact rational arithmetic and certified VAS/Sturm real-root
isolation to 10⁻²⁸ — **no floating point anywhere in this section**:

| n | numerator deg | irreducible factor deg | q_cross (certified) | branch |
|---|---|---|---|---|
| 6 | 72 | **54** | 1.024447239875787785 | real-level |
| 6 | 72 | 54 | 4.177742152083630423 | off-branch |
| 8 | 128 | **110** | 1.260370429056439479 | real-level |
| 8 | 128 | 110 | 5.086995698462880355 | off-branch |
| 11 | 242 | **224** | 1.139658359490870021 | real-level |
| 11 | 242 | 224 | 2.411261903003387275 | off-branch |

Exactly matching the independent 50-dps sweep of §2.

- **Positive:** the crossing locus is *exactly characterised* by an explicit integer
  polynomial — a derived object, not a fitted number.
- **Negative:** irreducible of degree ≥ 54 ⇒ **not expressible in radicals**, not
  any recognisable constant. **No closed form, no asymptotic law.**

**The dominant-partition family.** #4829 §2 read the n=6 exchange as
(4,1,1)[Δ=−10] ↔ (3,2,1)[Δ=+16]. It generalises — but **not** as "hook vs
near-rectangle". The correct statement: the exchange is always between **two
`ℓ(λ) = 3` partitions adjacent in dominance order.**

| n | dominant pair | n | dominant pair |
|---|---|---|---|
| 6 | (3,2,1) ↔ (4,1,1) | 17 | (10,5,2) ↔ (9,6,2) |
| 8 | (5,2,1) ↔ (4,3,1) | 18 | (10,6,2) ↔ (11,5,2) |
| 11 | (7,3,1) ↔ (6,4,1) | 19 | (10,6,3) ↔ (11,6,2) |
| 13 | (8,4,1) ↔ (7,4,2) | 20 | (11,6,3) ↔ (10,7,3) |
| 15 | (8,5,2) ↔ (9,4,2) | | |

Every pair has **exactly three rows** — a direct consequence of the k=2 rung
(BG-3): near q=1 the level is 2, so `s_λ` vanishes to order (number of cells of
content −2), which is 1 for the minimal-length ℓ=3 stratum and higher for most
deeper λ.

**Lean, sorry-free.** [`WenzlLevelStratum.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/WenzlLevelStratum.lean)
formalises exactly the BG-3 mechanism and nothing beyond it, over a generic
`Field K` (§7c — no `ℝ`, no ordering; the field is needed only because `k + c` is
an integer that may be negative):

- `neg_mem_partitionContents_of_lt_length` — a partition with more than `k` rows
  (all rows nonempty) has a cell of content `−k`;
- `principalSpec_numerator_eq_zero_of_lt_length` — hence at integer level `k` the
  numerator `∏_x (1 − Q^{k+c(x)})` **vanishes** for every such λ, for any `Q`.

Two `decide` guards show the positivity hypothesis is **load-bearing, not
decorative**: `−1 ∉ partitionContents [3,0]` but `−1 ∈ partitionContents [3,2]`.
This is a statement about partitions and a formal product only — **not** evidence
for any binding magnitude, and it does not evaluate q₀.

---

## 4. The Z=N / Z≠N isospin pattern BREAKS under a fixed-n control

#4832 observed — and carefully declined to claim — that among {D, T, ³He, ⁴He} the
Z=N members cross below q₀ and the Z≠N members above. **That caution was correct.**

**The four-point set is confounded.** Isospin and strand count move together:

| iso | (Z,N) | A | n=3A | class | A parity |
|---|---|---|---|---|---|
| D | (1,1) | 2 | 6 | Z=N | even |
| T | (1,2) | 3 | 9 | Z≠N | odd |
| ³He | (2,1) | 3 | 9 | Z≠N | odd |
| ⁴He | (2,2) | 4 | 12 | Z=N | even |
| ⁶Li | (3,3) | 6 | 18 | Z=N | even |
| ⁷Li | (3,4) | 7 | 21 | Z≠N | odd |

`Z=N ⟺ A even ⟺ n ∈ {6,12,18}`. **Extending the ladder to ⁶Li/⁷Li preserves the
confound exactly** — it adds one more Z=N-even and one more Z≠N-odd point, so no
number of additional isotopes along A can separate the two hypotheses.

**The controlled test: hold n fixed, vary only (Z,N).** Same strand count, same
ℓ≥3 stratum, same partition set, same word length, same cost — only the isospin
content of the braid word changes.

| n | iso | (Z,N) | class | crossing on (1,q*) | vs q₀ | pattern predicts |
|---|---|---|---|---|---|---|
| 6 | D | (1,1) | **Z=N** | 1.0536500613654132 | **below** | below ✓ |
| 6 | pp | (2,0) | Z≠N | **1.0657734736958715** | **below** | above ✗ |
| 6 | nn | (0,2) | Z≠N | **1.0567721647692783** | **below** | above ✗ |
| 12 | ⁴He | (2,2) | **Z=N** | 1.020923 (and 1.207893) | **below** | below ✓ |
| 12 | ⁴Li | (3,1) | Z≠N | in **(1.01, 1.02)** | **below** | above ✗ |
| 12 | ⁴H | (1,3) | Z≠N | in **(1.02, 1.03)** | **below** | above ✗ |

**At fixed n, EVERY member crosses below q₀ regardless of isospin — at n=6 and
again at n=12.** Five of the six controlled points are Z≠N and every one of them
lands on the same side of q₀ as its Z=N partner, which is exactly what the pattern
forbids.
Isospin shifts the crossing by only ≈ 0.012 at n=6 (1.0537 → 1.0658) and ≈ 0.01 at
n=12, while changing n moves it far more, and changes even the *number* of
crossings (n=6 → one at 1.054; n=9 → none on the branch; n=12 → two, at 1.021 and
1.208).

The n=12 leg was run as a minimal side-test
([`threerow_n12_isospin_control.py`](../../computations/deltalambda/threerow_n12_isospin_control.py),
log committed alongside): no diagnostic ray and no bisection, since the only thing
the claim depends on is **which side of q₀ the first crossing falls on**. That is
the same economy the sibling adopted mid-flight in `threerow_4he_completion_probe.py`
(commit `ab927cd2ee`), and for the same reason — the f64 character path cannot
support the resolution that bisection was buying.

> **VERDICT: the Z=N / Z≠N split is an n-effect mislabelled as isospin.** It is a
> **first-class NEGATIVE result** — the pattern does not survive the one comparison
> that can test it. No isospin argument is needed or supported; the corpus's
> mirror/isospin machinery (`NeutronProtonEMSign`, `SaturationRhoCap`) was **not**
> invoked, because there is no surviving effect for it to explain.

**Raw n=12 control values** (F at the sampled q; the sign flip is the whole test):

| q | ⁴He (2,2) Z=N | ⁴Li (3,1) Z≠N | ⁴H (1,3) Z≠N |
|---|---|---|---|
| 1.000001 | +1.182745e-05 | +1.182736e-05 | +1.182755e-05 |
| 1.005 | +4.436546e-02 | +4.198951e-02 | +4.672301e-02 |
| 1.010 | +6.017693e-02 | +5.043935e-02 | +6.977368e-02 |
| 1.020 | +1.002043e-02 | **−3.046072e-02** | +4.950898e-02 |
| 1.030 | **−1.470950e-01** | −2.405688e-01 | **−5.642788e-02** |
| 1.060 | −1.301588e+00 | −1.674768e+00 | −9.344506e-01 |
| **q₀ = 1.109979** | −5.946880e+00 | −6.498576e+00 | −4.980725e+00 |
| 1.150 | −1.128361e+01 | −7.556090e+00 | −1.078985e+01 |

All three are positive near q=1 and negative by q₀ — **all three flip below q₀**,
and the flip locations differ by less than 0.01 in q. Isospin is a small
perturbation on a crossing whose position is set by n.

⚠ **pp(2,0), nn(0,2), ⁴Li(3,1), ⁴H(1,3) are COMBINATORIAL PROBES, not bound
nuclides** (the diproton and dineutron are unbound; ⁴H/⁴Li are unbound resonances).
No physical claim is made about them — `atom_braid_word_3A(Z,N)` is defined for any
(Z,N), and that is all this test uses. AME is never consulted.

### 4b. ⁶Li / ⁷Li are unaffordable — a hard bound, not a sandbox limitation

The batched-column trace costs `O(L · Σ_λ dim²)`, and

```
Σ_{λ ⊢ n} (dim V_λ)² = n!        (exact; verified n=12: 4.7879·10⁸ vs 12! = 4.7900·10⁸)
```

Against the measured n=12 cost of ~32 s per grid point:

| n | Σ_{ℓ≥3} dim² | × n=12 | projected |
|---|---|---|---|
| 12 | 4.788·10⁸ | 1 | 32 s / grid point |
| 15 | 1.308·10¹² | 2.73·10³ | ≈ 24 h / grid point |
| **18 (⁶Li)** | 6.402·10¹⁵ | **1.34·10⁷** | **≈ 14 years / grid point** |
| **21 (⁷Li)** | 5.109·10¹⁹ | **1.07·10¹¹** | **≈ 10⁵ years / grid point** |

#4832's sparse fix removed a `dim³ → dim²` factor; it does **not** touch the
factorial. ⁶Li and ⁷Li are out of reach by **7 and 11 orders of magnitude**. This
is a consequence of an exact identity, so it is a *bound*, not a "we ran out of
time" — and it is precisely why the fixed-n control above is the right experiment
rather than a substitute for a better one.

---

## 5. 🛑 Q3 — GENERICITY GATE: q₀'s position is COINCIDENTAL

The premise "q₀ lands between `q_cross(6)` and `q_cross(9)`" **does not survive
§1**: there is no n=9 crossing on the real-level branch. What survives is weaker
and one-sided — q₀ is merely *above* the deuteron crossing.

Maximal interval around q₀ on which the whole isotope sign-vector is constant:

| quantity | value |
|---|---|
| window | **(1.053650, 1.207893)** |
| width | **0.154243** |
| real-level branch width (`q*−1`) | 0.278450 |
| **window as fraction of branch** | **55.4 %** |
| **information content** `log₂(branch/window)` | **0.852 bits** |
| bounded below by | D crossing 1.053650 |
| bounded above by | ⁴He *second* crossing 1.207893 |

**Any q in 55.4 % of the branch reproduces the identical sign pattern.** Counting
natural constants inside the window with generator rules fixed *in advance*:

| family | count | examples |
|---|---|---|
| rationals `p/q`, `q ≤ 12` | 9 | 6/5, 7/6, 8/7, 9/8, 10/9, 11/10 |
| radicals `a^{1/b}`, `a ≤ 20`, `b ≤ 12` | 32 | 2^{1/4}=1.1892, 2^{1/5}=1.1487, 2^{1/6}=1.1225 |
| `{π,e,φ,√2,√3,√5,ln2,ln3,ζ(3),Vol(4₁)} × p/q`, `p,q ≤ 6` | 13 | e·2/5, φ·2/3, √3·2/3 = 1.1547 |
| **total** | **54** | |

**Robustness.** The verdict does not hinge on the exact upper bound. Sweeping it
across the whole plausible range:

| upper bound | width | % of branch | bits | constants |
|---|---|---|---|---|
| 1.168631 (tightest bracket) | 0.1150 | 41.3 % | 1.276 | 35 |
| **1.207893 (measured)** | **0.1542** | **55.4 %** | **0.852** | **54** |
| 1.278450 (`q*`, no upper crossing) | 0.2248 | 80.7 % | 0.309 | 91 |

Every row is a coincidence. **No value in the range makes q₀'s position informative.**

For completeness, the *character-free* family (n ≤ 23, a different object — not the
physical isotope set) gives a tighter window `(1.100181, 1.139658)`, width 0.0395 =
14.2 % of the branch = **2.82 bits**, still containing **11** natural constants.
Even on the most favourable reading available anywhere in this analysis, q₀'s
position buys under three bits and singles out nothing.

> **VERDICT: COINCIDENTAL.** q₀'s position in this window carries **0.31 bits** of
> constraint and is shared with **91** natural constants. **It is a coincidence** —
> not a derivation, not evidence, and it must not be cited as either. Nothing was
> inverted to obtain it: `free_parameters = 0`, q₀ is an input throughout, and no q
> was ever solved for to produce a desired sign pattern.

The one non-generic statement available is a **negative**: `r(q₀) = 2.5995` is not
an integer, so q₀ sits on **no rung** of the only genuinely structured sequence in
this problem (BG-3). Had it landed on a rung, that would have been a result. It
does not.

---

## 6. Verification status (honest)

- **Probes:** both ran to completion; witnesses emitted. Several assertions are
  recorded **expected-false** (`q_cross_sequence_monotone`,
  `crossings_exist_for_all_n`, `q0_position_informative`,
  `isospin_pattern_survives_fixed_n_control`) — the nulls *are* the results.
- **Cross-validation against #4829/#4832 through an independent normaliser path**
  (dual-Cauchy closed form, never `y_lambda_at_q0_mpmath`): D crossing
  **1.053650** vs 1.05365; character-free n=6 **1.024447** vs 1.02445; D's far
  diagnostic crossing **3.4101**, matching #4832's late correction commit.
- **Dual-Cauchy identity:** max rel err **2.8·10⁻⁴¹** over n ∈ {4,6,9,12} × three q.
- **Exact section:** sympy exact rational arithmetic + certified VAS/Sturm
  isolation — **no floating point**, so degrees and enclosures carry no numeric error.
- **Lean:** `lean`-direct **exit 0**, sorry-free, `#print axioms` =
  `[propext, Quot.sound]` on all three declarations, built against the real import
  cone. CI is `workflow_dispatch`-only repo-wide, so this local verification *is*
  the gate — no CI run exists and none is claimed.
- **Precision split:** branch geometry / ladder / `S_n` at 50-dps mpmath; `χ^λ` at
  f64 (pure-Python Hoefsmit seminormal via #4832's sparse kernel, exact-equal to
  the dense path to 1.4·10⁻¹⁵). **Isotope crossing q values carry f64 resolution
  only**; the sign verdicts sit at |F| = O(10⁻¹)–O(1), far above f64 noise.
- **Grid caveat — scope-(a).** "No crossing for this n" is a statement about the
  **swept interval and grid**: a geometric grid can miss an *even* number of zeros
  between adjacent points. **No invariant is proved to forbid a zero anywhere, so
  no scope-(b) exclusion is claimed anywhere in this document.**

## 7. What this does NOT do

`F_K` and `G_n` are **value-only** objects (`Δ_λ` carries no extensive magnitude);
this probe tests only the **SIGN** structure of the ≥3-row weighting. **The
super-pairwise extensive binding MAGNITUDE remains OPEN — bean `qou-prjo` is NOT
closed.** This is also **not** #4817's cross-isotope `(μ₃,μ₄)` cumulant window,
which is a different object over A.

## References
- Proved Δ_λ: `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`.
- #4829 + [`2026-08-08-deltalambda-threerow-sign-crossing-probe.md`](2026-08-08-deltalambda-threerow-sign-crossing-probe.md).
- #4832 + [`2026-08-08-threerow-sign-crossing-a-dependence-4he-and-lean.md`](2026-08-08-threerow-sign-crossing-a-dependence-4he-and-lean.md); kernel `threerow_chi_sparse.py` (reused here).
- q₀ anchor convention (proton default): AGENTS.md §q₀ anchor (owner 2026-08-07).
- Genericity requirement: AGENTS.md §"Defined residual ≠ derived decomposition" item 2.
- Scope-(a)/(b) discipline: AGENTS.md §"Before declaring refuted / ruled out / dead end".
