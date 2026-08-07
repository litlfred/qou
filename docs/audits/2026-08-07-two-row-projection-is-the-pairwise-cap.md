# The two-row projection *is* the pairwise cap — and N=2 is why

**Date:** 2026-08-07 · **Branch:** `claude/1ppq-l2-closure-attacks-ufrfun` · **PR #4664**
**Owner steers:** *"are you looking at complex volume? we had mass for deuteron"* ·
*"how to resolve?"* · *"i thought we had formulas for binding and mass in terms of
projecting to free tensor products"*

All three land. The third is the important one — it says the missing term has been
sitting in the corpus's own formula, explicitly set to zero, the whole time.

**No fit, no compute run, nothing wired.**

---

## 1. The corpus formula the owner was pointing at

[`def:two-row-projection`](../../content/quantum-observable-universe/mass-theory/two-row-projection.md) —
the projection onto the Wedderburn blocks of the free tensor product `V^{⊗n}`:

$$\pi_{\mathrm{2\text{-}row}} : H_n(q) \to \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda)$$

and the trace **splits**:

$$\mathrm{tr}_M(\beta) = \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda \chi^\lambda_q(\beta)}_{\pi_{\mathrm{2\text{-}row}}\beta} \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda \chi^\lambda_q(\beta)}_{(1-\pi_{\mathrm{2\text{-}row}})\beta}$$

[`def:two-row-stratum`](../../content/quantum-observable-universe/mass-theory/two-row-stratum.md) L17–22,
verbatim:

> The two-row stratum carries the **SU(2)** Schur–Weyl image. … Partitions with
> `ℓ(λ) > 2` **map to zero**. They correspond to **higher-rank symmetry components
> absent from the SU(2) spin-pairing observable**. The q-deformed spin observables …
> **live strictly in the two-row sector.**

And L40: the two-row stratum carries **86.6 %** of `tr_M(β_{⁴He})` — so **13.4 % of the
trace is projected to zero**, measured, not estimated.

---

## 2. The identification

| algebraic | combinatorial | physical |
|---|---|---|
| `ℓ(λ) ≤ 2` (two-row stratum) | pairs | **SU(2) spin-pairing** — 2-body |
| `ℓ(λ) ≥ 3` (projected to **zero**) | triples and up | **irreducibly ≥3-body** |

> 🛑 **§2 SUPERSEDED — REFUTED by measurement, 2026-08-07.** See
> [`2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md`](2026-08-07-binding-is-three-row-dominated-hypothesis-refuted.md).
> **The binding formula does not truncate to two rows — it already sums all
> partitions.** Verified: the probe reproduces the corpus's own
> `B(D) = 0.380 MeV` (0.3801) and `C_knot = 5.852` (5.8530). So the claim below —
> that the missing term is a *discarded* stratum — is wrong; nothing was discarded.
>
> The measurement did find something better: the binding sum is **≥3-row *dominated***
> (26 % at D → 62 % at T/³He → **100 % at ⁴He**), *opposite* to `tr_M`, because
> `Δ_λ = ±f^λ` weights by the SYT count and **inverts** the stratum dominance. The
> `N=2 ⟺ ℓ(λ)≤2 ⟺ pairwise ⟺ ρ_A ≤ C(A,2)` identification (§3 below) **stands**; only
> the "binding inherits the truncation" inference is retracted.

**The proved pairwise cap `ρ_A ≤ C(A,2)` is the shadow of the two-row projection.**
The missing super-pairwise extensive term is not absent from the theory — it is the
**explicitly discarded complement** `(1 − π_{2\text{-row}})·\mathrm{tr}_M`.

Six ansätze failed because every one of them tried to reweight `Δ_λ` *inside* the
surviving sector. No reweighting of a two-row sum reaches a three-row object; the
three-row terms are multiplied by **zero**, and zero times any weight is zero. That is
also why the intensive/extensive obstruction is proved rather than merely observed.

---

## 3. Why the projection is there: `N = 2` — and this **revives A2 in corrected form**

The Schur–Weyl row cap: `dim V_\lambda = 0` whenever `ℓ(λ) > N`, for `V^{⊗n}` with
`dim V = N`. The framework has `dim V = 2` (Descartes). **So `N = 2` *forces* the
two-row restriction** — the projection is not a modelling choice, it is the row cap.

$$\boxed{\;N = 2 \iff \ell(\lambda) \le 2 \iff \text{pairwise-only} \iff \rho_A \le \tbinom{A}{2}\;}$$

**This corrects my own closure of bean `qou-fvzm`.** I closed A2 "premise-refuted"
because there is no flavour `N=3` to import into binding. That reasoning was right and
the conclusion was too strong. #4640 §4 proves, sorry-free:

> `weyl_dim_alt_eq_zero_iff` — `dim V_{(1³)} = C(N,3)` vanishes **iff `N < 3`**

Read for *binding* rather than for flavour, that is exactly: **three-body channels
exist if and only if `N ≥ 3`.** So the super-pairwise term the arc has hunted for a
year requires `N ≥ 3` — **for row-cap reasons, not flavour reasons.**

**This is the eightfold-way hint the owner originally asked for.** The octet's `N=3`
requirement and three-body binding's `N≥3` requirement are *the same row-cap
condition*, arrived at from two independent directions. #4640 calls its result
scope-(b) exclusion that "if anything sharpens the target" — this is the target it
sharpens. Bean `qou-8pl3` ("N=3 routes") is therefore **not only a flavour problem: it
is the binding blocker as well.**

A2 reopens as: *not* "import the flavour sector's `N=3`" (there is none), but
**"`N ≥ 3` is a proved necessary condition for the missing term, so the N=3-route
question is load-bearing for binding."**

---

## 4. The deuteron, complex volume, and #4591's objection inverted

**Owner: *"we had mass for deuteron."*** Correct —
[`binding_link_volumes.py`](../../computations/binding_link_volumes.py) matches the
deuteron at **+0.2 %**, but via the **`Hopf → Vol(𝓑₃)` substitution**, because
`²H → Hopf L2a1` is Seifert-fibred with `Vol = 0`. I called that substitution
"unjustified." The owner's *"are you looking at complex volume?"* suggests what it may
be standing in for.

**The inversion.** #4591's objection to a CS-carrying magnitude is that the anchor is
CS-blind: `CS(4₁) ≈ 0` (figure-eight amphichiral), so *"any `F(Vol,CS)` reducing to
`Vol` at `CS=0` is equally muon-consistent — a whole function's freedom."* True **for
the muon**. But the deuteron is its exact complement:

| anchor | `Vol` | `CS` | constrains |
|---|---|---|---|
| muon (4₁) | 2.0299 | **≈ 0** | `F` on the **`CS = 0` axis** |
| deuteron (Hopf) | **0** | ≠ 0 (to verify) | `F` on the **`Vol = 0` axis** |

`B_D = 2.224 MeV ≠ 0` while `Vol(Hopf) = 0`, so **any** `F(Vol, CS)` fitting the
deuteron is carrying it entirely on `CS`. Two orthogonal calibration points collapse
"a whole function's freedom" to something checkable — the muon fixes the `Vol` axis,
the deuteron fixes the `CS` axis.

**Gate before anything is built on this:** verify `CS` of the Hopf-link complement is
nonzero and well-defined. The complement is `T² × I`, a degenerate Seifert case, and
`CS` may be `0` or only defined modulo a period there. **If `CS(Hopf) = 0`, this
resolution dies immediately** and the `Vol(𝓑₃)` substitution stays unjustified. Bean
this as the gate; do **not** assume it.

---

## 5. Where this leaves the arc

The volume route was an import. The projection formula is the corpus's **own**
machinery, it already contains the missing sector as an explicit term, and it says
precisely why that term is zero. Reordered:

| # | Action | Why |
|---|---|---|
| 1 | Evaluate `(1 − π_{2\text{-row}})·tr_M` on `D / T / ³He / ⁴He` — the **discarded 13.4 %** | Measures the missing term *directly*, in corpus-native language. No new object. |
| 2 | Gate: is `CS(\text{Hopf}) ≠ 0`? | Decides §4 outright |
| 3 | Reopen `qou-fvzm` as *"`N ≥ 3` is necessary for the ≥3-body term"*; link `qou-8pl3` | The corrected A2 |
| 4 | Ask whether `ℓ(λ) ≥ 3` terms are **extensive** | The other half — super-pairwise is necessary, extensive is also required |

**Honest caveat on magnitude.** The discarded sector is **13.4 %** of `tr_M(β_{⁴He})`,
while the deuteron deficit is **−82.9 %** (`B = 0.380` vs AME `2.225`). 13.4 % does not
obviously supply an 83 % deficit, and the two figures are for different isotopes and
different quantities. What is established here is that the discarded sector is the
right **kind** of object (≥3-row ⟺ super-pairwise) and is **not** negligible — **not**
that its magnitude closes the gap. Step 1 is what would settle that, and it can fail.

---

## 7. RESOLVED upstream (2026-08-07, `f92a8b15`) — N = 2 is locked in, and that sharpens the conclusion

§3 above reopened bean `qou-fvzm` as *"`N ≥ 3` is a proved necessary condition for the
missing ≥3-body term, so the N=3-route question is load-bearing for binding."* **Main
has now settled the N question, and the answer closes that route.**

`compute(T3f): N = 2 is LOCKED IN for the mass pipeline — the soft constraint is hard`
turns T3f's *"GENUINELY OPEN"* into a **scope-(b)** result, using only objects the
framework already had:

- `tr_M = Σ_λ y_λ χ_λ` with the `χ_λ` **Hecke characters — N-independent**. All the
  `N`-dependence sits in the weights, which are **principal specialisations**
  `y_λ ~ s_λ(1, q, …, q^{N−1})`.
- **The row cap *is* the weight vanishing.** `y_{(1³)} = 0` at `N = 2` because the cell
  of content `−2` contributes `[N−2]_q = [0]_q = 0`; nonzero at `N = 3`. So "the row cap
  kills the singlet at `N=2`" and "the Ocneanu weight vanishes at `N=2`" are **one fact,
  not two** — and it is the `q → 1` shadow of `RowCapObstruction.lean`'s `weylDimAlt`.
- **The two traces are not proportional.** `y_{(2,1)}/y_{(3)} = q[2]_q[N−1]_q/[N+2]_q`
  differs at every `q` tested. Moving to `N = 3` does not merely *add* the singlet
  channel — it **re-weights the surviving channels**, so `tr_M` changes on elements the
  mass pipeline already evaluates.

**This confirms the §2–§3 identification and kills the route it suggested.** The
identification `N = 2 ⟺ ℓ(λ) ≤ 2 ⟺ pairwise ⟺ ρ_A ≤ C(A,2)` is now *mechanically*
established, not merely algebraic: the two-row restriction and the `N=2` Ocneanu weight
vanishing are the same phenomenon. But the corollary I drew — "so get the ≥3-body term
by going to `N ≥ 3`" — is **not available**: `N = 2` is locked for the mass pipeline,
and switching would move numbers the pipeline already reproduces.

### The sharper conclusion, from combining this with the ℓ¹ ceiling

Two independent results now bracket the missing term:

| result | what it excludes |
|---|---|
| **ℓ¹ ceiling** ([this branch](2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md)): `ℓ¹/target ∈ [0.36, 0.59] < 1`, all four light isotopes | no **reweighting** of the `N=2` partition sum reaches the target — including any `Δ_λ` re-derivation |
| **N = 2 locked** (`f92a8b15`, scope-(b)) | no move to a **larger `N`** to obtain the missing `ℓ(λ) ≥ 3` channels |

Together: **the missing additive term is not a Hecke-trace object at all.** Not at
`N = 2` (the ℓ¹ ceiling forecloses every reweighting), and not by escaping to `N ≥ 3`
(locked). That is a materially stronger statement than either result alone, and it is
where the six failed ansätze were always going to end up — every one of them looked for
the magnitude *inside* `Σ_λ y_λ χ^λ Δ_λ`.

**Consequence for the attack list:** A1–A5 all sought the term inside the trace or its
normalisation and are correspondingly narrowed. The candidates that survive are the ones
that were never trace objects — the extended-Bloch/geometric route (`qou-985x`), and
the untested question of whether the **atomic-braid → nucleus map itself** is the
defective step (`qou-imcd`, the ROAST's top meta-item).

**Not a contradiction with the eightfold programme.** `f92a8b15` also records the
*positive* half: the Hecke tower can carry an `N=2` Jones trace (mass) **and** an `N=3`
HOMFLY trace (flavour) as two functors on one algebra. Flavour is not blocked by this;
only the attempt to source *binding* magnitude from a larger `N` is.

**Bean `qou-fvzm` → closed**, this time on a proved upstream result rather than my own
inference.
