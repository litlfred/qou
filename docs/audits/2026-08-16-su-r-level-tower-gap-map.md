# SU(r) level tower — gap-closure map

**Verdict: the tower is real, exact, and already largely in the corpus. It
closes one gap and closes off one line of speculation. It does not rescue
the Δ_λ magnitude, and the ℓ¹ ceiling it was expected to tighten in fact
loosens — 59 % → 69.2 %.**

Two premises the work was set up on turned out to be wrong, and both are
corrected below rather than worked around: the six Δ_λ ansätze were never
scored against `r*`, and restricting to the surviving blocks does not
tighten the ℓ¹ ceiling.

Prior art this rests on and does **not** re-derive:
[`2026-08-16-tl-all-n-weight-vanishing.md`](2026-08-16-tl-all-n-weight-vanishing.md),
[`2026-08-16-tl-n6-discriminator.md`](2026-08-16-tl-n6-discriminator.md),
[`2026-08-16-s2-gram-radical-independent-revalidation.md`](2026-08-16-s2-gram-radical-independent-revalidation.md),
`docs/audits/2026-08-16-wenzl-level-family.md` (sibling branch, PR #5229),
[`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).

---

## 0. The tower

```
z_r = q^r / [r]_q  =  q^(2r-1)(q^2 - 1) / (q^(2r) - 1),
      [r]_q = (q^r - q^-r)/(q - q^-1)
```

**Tier: symbolic-exact**, conditional on the same Wenzl 1988 external input
the weight-vanishing lemma already cites. Verified in
[`wenzl_level_tower_verify.py`](../../computations/probes/wenzl_level_tower_verify.py):
over ℚ(q), for **symbolic** `r`, `q^r/[r]_q − z_W(r)/q` simplifies to `0`,
where `z_W = Q^r(1−Q)/(1−Q^r)`, `Q = q²`, `z_W = q·z`. Both ingredients were
already in the corpus; what was not recorded is that eliminating them
collapses to the compact q-integer form. **The tower is a rearrangement of
an established relation, not a new hypothesis** — it adds no assumption.

At the proton pin `q₀ = 1.1099785827513808`, 30 dps:

| r | z_r | quotient | row cap |
|---|---|---|---|
| 1 | 1.109978582751380800 (= q) | abelian | ≤1 |
| 2 | 0.612688037146465244 (= z_D) | TL = SU(2) | ≤2 |
| 3 | 0.449304809090207852 | SU(3) | ≤3 |
| 4 | 0.369360232235604910 | SU(4) | ≤4 |
| 5 | 0.322749650471015782 | SU(5) | ≤5 |
| ∞ | 0.209060298795639302 (= h = q − q⁻¹) | full H_n | none |

`r = 1`, `r = 2` and the `r → ∞` limit are **exact**, not numerical:
`z_1 = q`, `z_2 = q³/(q²+1) = z_D`, `lim = q − 1/q`. `z_C = √q/(q+1)` solves
to `r = 2.5995155364`, reproducing the owner's figure.

### The tower already had a second derivation, and the sibling had a third leg

Not novel, and the audit should not imply otherwise:

- **Fibre dimension.** `z·[N]_q = q^N` for a fibre of quantum dimension
  `dim_q V = [N]_q` — Lean `QOU/BraidsAndKnots/FibreDimensionForcesTL.lean`,
  companion `computations/ocneanu_param_from_fibre_dimension.py` (bean
  `qou-n1dj`). Same rational function. So **fibre dimension N = Wenzl
  level r**.
- **Sibling PR #5229** reached that identification independently as [N1]
  (`N_eff ≡ Wenzl level` *as maps*, not merely at `q₀`), proved the
  normalisation `Q = q²`, `z_W = q·z` is *forced* (W0, unique solution), and
  has the tower as [N4].

On `z_C` the sibling's result is **strictly stronger than anything here**:
[N3] shows `z_C` is not `z_r` for **any** `r`, identically in q — a
scope-(b) exclusion on field membership (`√q ∉ ℚ(q)`, Eisenstein at `q`)
plus non-constancy of `r_C(q)`. The `2.5995` above is one root-find at one
anchor. **Cite [N3], not this.** That also answers the "which integer N?"
question outright: none, and not for want of looking.

---

## 1. Δ_λ — the six ansätze, re-scored. None is rescued.

### Two corrections to the premise, both load-bearing

**(i) The six were never scored against `r* ≈ 1.585`.** They were scored at
the deuteron against `target = −B_D/m_e = −4.353365 m_e`, at `n = 6`. `r*`
is a *later, separate, A = 3* object:
`r* = μ₃/c₃` with `μ₃ = B(³H)/B(²H) − [3]_q = 0.47077` and
`c₃ = 0.297` (the H₉ Borromean lift) — see
`computations/deltalambda/mu3_target_robustness_audit_probe.py`. Calling it
"the deuteron `C_knot` deficit" (AGENTS.md; the 2026-08-02 audit) conflates
two different numbers. The deuteron's own `C_knot = 5.852` is a third.

**(ii) The re-scoring largely already happened, on 2026-08-10.** The
`rho_k_h3a_*` witnesses were regenerated at the proton pin under convention
D. `y-lambda-at-q0.witness.json` at `n = 6` shows **4 of 11 blocks live**,
exactly `ℓ(λ) ≤ 2`. So the current committed scores *are* D-frame with
≤2-row support. What remained was to read them against the old ones.

**(iii) And the support restriction is a no-op on the value anyway.** Under
D the dropped weights are exactly zero (measured: `max |y_D|` off ≤2 rows is
`< 1.5e-67` for every `n = 2…8`), and adding zero-weight terms to a
y-weighted sum adds zero. The 81.7 % figure at `n = 6` is the **algebra**
mass (`dim²`: 132 of 720), which is what the Gram form lives on — not the
value of `B(K)`. Only the *frame* moves numbers, and it moves them by
`ℓ¹(D)/ℓ¹(C)` = 0.9983 (n=4), 0.9926 (n=5), **0.9805 (n=6)**, 0.9598 (n=7),
0.9289 (n=8) — a ~2 % effect at the deuteron.
([`two_row_support_recount.py`](../../computations/deltalambda/two_row_support_recount.py))

### The table

Target at the deuteron: `−4.353365 m_e`. "old" = pre-2026-08-10
(muon/C-era); "new" = current committed witness (proton/D, ≤2-row support).

| # | ansatz | old | new (D, ≤2-row) | verdict |
|---|---|---|---|---|
| 1 | Frobenius co-Casimir `1/dim_q(λ)` | `+0.144959` (−3.33 %) | `+0.248277` (**−5.70 %**) | **not rescued** — wrong sign, ~17× too small |
| 2 | Demazure-fibre `y_λ D_w/D_{w₀}` | — | never scored at the deuteron; best H₄ scheme `Δ = 1.4993` vs `1e-3`; the `D_w/D_{w₀}` evaluator gives `Δ_λ ~ 10⁻⁵`, i.e. tautological | **not rescued** — degenerate |
| 3 | LP-Plancherel `t_λ = 1/dim_q` | `y₀* = −1.01025`, obj `4.39799` | `y₀* = −0.754437`, obj `3.284340`, singleton `[5,1]`, `Δ = −17.145705` | closes **by construction** — an LP with one equality constraint always closes; zero information |
| 4 | LP-Frobenius `t_λ = \|χ^λ\|` | `y₀* = −16.8954`, obj `73.5519`, `Δ = −47.16` | `y₀* = −8.671205`, obj `37.748921`, singleton `[6]`, `Δ = −24.201770` | same; **the refutation is that 3 and 4 disagree** — different singleton support ⇒ the cost vector is a free parameter |
| 5 | crystal-graph `c_λ(q)` | `+1796.735` (−412.7×) | `+2550.846` (**−585.9×**) | **not rescued — worse.** Wrong sign, 2–3 orders out. Independently pruned scope-(b) by KL positivity vs `deltaSign_mixed` |
| 6 | Wenzl augmented Markov | — | uniform `Δ_λ = −11.211735`, rank 11, residual `0.0` | closes **by construction** via 10 auxiliary cycle-type anchors; witness itself says read it as a prior, "not as a measurement" |

**Not one is rescued, and the re-scoring could not have rescued one.** The
diagnosed cause — no per-block weight converts an intensive quantity into an
extensive one — is a *scaling* argument, indifferent to how many blocks
carry weight. Restricting 11 blocks to 4 does not make an intensive object
extensive. The frame shift is ~2 %; the misses are 5.7 %-of-target with the
wrong sign (1), and 586× with the wrong sign (5). Ansätze 3, 4 and 6 close
by construction in either frame, so a frame change cannot affect them.

**Scope: (a), scope-limited negative.** These constructions, alone, do not
reproduce the deuteron binding as-is. No ingredient is structurally
excluded here. (The separate scope-(b) prune of the crystal *sign* leg by KL
positivity stands on its own and is not restated.)

### Three durable artifacts still quote the pre-2026-08-10 numbers

Not fixed here — listed so they are not cited unwittingly:

- `content/.../lean/QOU/BraidKnot/DeltaLambdaRefutation.lean` L55/L64
  (`coCasimirSum := 0.144959224127`, `closureGap := 4.498326505997`) and
  L112 (`λ=[6], Δ=−47.16`). The theorems still hold — the gap is ≫ tol — but
  the literals no longer match the witness they cite.
- `docs/audits/2026-07-05-delta-lambda-ansatz-refutations-anchored.md`
  L23–25/L54/L64/L78–83/L111.
- `content/.../mass-theory/frobenius-cocasimir-refuted-deuteron.md` L3
  (`+0.145 m_e`).

Also: **"the six" is not a stable set.** AGENTS.md and the 2026-08-02 audit
list one set; `2026-05-18-delta-lambda-gating-context.md` has seven rows
(adds Occam single-support); `2026-06-04-m-lambda-closure-landscape.md:35`
lists a different six (adds Occam, drops crystal-graph).

---

## 2. The ℓ¹ ceiling — survives, but loosens. A prediction of mine was wrong.

**Question asked: does the ℓ¹ ceiling (`qou-kemt`, ≤ 59 % of target) survive
restriction to the surviving blocks? Answer: yes, and the conclusion it
supports holds — but the number gets worse, not better.**

The committed ceiling needed re-measuring:
`delta-lambda-l1-ceiling-sign-prune.witness.json` is `q0Anchor: "muon"`
(2026-07-17) and takes nonzero ℓ¹ mass from `ℓ(λ) ≥ 3` blocks — 13.3 % of
the deuteron's, 62.4 % of ⁴He's — which D annihilates exactly. Re-measured
at the proton pin
([`l1_ceiling_d_frame_remeasure.py`](../../computations/deltalambda/l1_ceiling_d_frame_remeasure.py)),
`ceiling = Σ|y χ Δ| / |B_AME/m_e|`:

| atom | n | C frame | **D frame** | D/C |
|---|---|---|---|---|
| deuteron | 6 | 0.51607 | **0.56614** | 1.097 |
| tritium | 9 | 0.35756 | **0.36041** | 1.008 |
| helium-3 | 9 | 0.59182 | **0.69249** | 1.170 |
| helium-4 | 12 | 0.40590 | **0.43347** | 1.068 |

Every D ceiling is still `< 1`, so the magnitude is **genuinely absent**,
not present-and-cancelling — and that now holds on the canonical frame
rather than a superseded one. But the headline moves: worst case is ³He at
**69.2 %**, not 59 %. Artifacts quoting "≤ 59 %" should say "≤ 69.2 %".

**I predicted the opposite and recorded the prediction before running.** The
argument was "dropping terms at fixed weights can only lower the sum". The
clause *at fixed weights* is false across a frame change: both frames
normalise to `Σ y_λ dim V_λ = 1`, so zeroing the `ℓ ≥ 3` blocks **forces** D
to concentrate all of that unit mass onto the ≤2-row blocks, where it meets
that subset's `|χ^λ|`. D drops terms and enlarges the survivors; the
enlargement wins.

This corrects an earlier claim in this same PR (the
`two_row_support_recount` commit) that the D ceiling is "tighter than the
C-frame bound twice over". Two objects were conflated:

- The **crude bound** `max_{ℓ≤2}|χ^λ| · Σ|y||Δ|` *does* tighten. `Σ|y||Δ|`
  falls `1.0199 → 1.0000` **exactly**, because `tr_M(1) = Σ y_λ dim V_λ = 1`
  and `|Δ_λ| = dim V_λ`, and under D every `y_λ ≥ 0` — the D weights are a
  probability distribution on the ≤2-row blocks. Under C they are not: 1
  negative-weight block at `n = 4`, 3 at `n = 6`, 8 at `n = 8`.
- The **actual ceiling** `Σ|y χ Δ|` — what the corpus means by the term —
  loosens.

A bound tightening while the quantity it bounds loosens is consistent. The
error was the identification, not either measurement. The `Σ|y||Δ| = 1`
exactness is a genuine structural fact and survives.

---

## 3. Mass — the cap is now a theorem; the implication runs the other way

The corpus chain is currently **fibre `dim V = 2` (posited) → row cap
`ℓ(λ) ≤ 2` (posited into the index set) → `y_{(1³)} = 0` → convention D**.
With `wenzlLevel_conventionD` (D *is* level 2, exactly) and
`schurPrincipal_eq_zero_iff` (`s_λ = 0 ⟺ ℓ(λ) > r`, all `r`, all `λ`), the
cap is a **theorem about level 2**, and the posits are no longer needed.

Listed, not edited. Each should gain a one-line citation.

**Primary POSIT sites — the root of the chain:**

| site | what it does | should cite |
|---|---|---|
| `content/.../mass-theory/feynman-eigenbasis-decomposition.md:6` | writes `ℓ(λ) ≤ 2` into the index set as a premise; `⌊n/2⌋+1` summands | `wenzlLevel_conventionD` + `schurPrincipal_eq_zero_iff` |
| `content/.../mass-theory/feynman-eigenbasis-decomposition-proof.md:9` | same cap, attributed to q-Schur–Weyl | same |

**Sites that explicitly infer D *from* the cap — direction now reversible:**

| site | quoted claim | should now say |
|---|---|---|
| `content/.../braids-and-knots/markov-axioms-primitive.md:26–30, :38` | "`y_{(1³)} = 0` is a restatement …, **not an extra assumption**"; "the loop value is a **consequence** of the fibre being two-dimensional" | the argument is now bidirectional; the cap need not be posited |
| `content/.../mass-theory/h3-markov-wenzl-weights-context.md:24–27, :51–58` | "`y_{(1³)} = 0` is **stated, not assumed**, and D follows" | "stated, not assumed" → **proved** |
| `docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md` (L32–36, L43, **L320**) | L320: "That `dim V = 2` is the right fibre on physical grounds. It is an **input** here." | the primary doc to carry the reverse-implication note |

**Already the right direction — cite as support, and refresh:**
`content/.../mass-theory/hecke-radical-is-temperley-lieb.md:1–9` (its `:43`
caveat "a **measurement, not a theorem of this paper**" is exactly what the
all-`n` lemma now closes); `content/.../mass-theory/two-row-stratum.md:24`;
`content/.../lean/QOU/QBeta/WenzlWeightVanishing.lean:238–241`;
`content/.../mass-theory/markov-trace-frobenius-selection.md:82, :89`.

**One live inconsistency found, not fixed:**
`content/.../mass-theory/he4-two-row-dominance.md:13, :22` still quotes
"at least 80 %" and "**86.6 %**". That 86.6 % is the convention-C value,
already withdrawn in `two-row-stratum.md:44` (2026-08-09) but not here.
Under D it is not a dominance figure at all — it is 100 %, an identity.

---

## 4. Standard model / 8-fold — measured, and the answer is no

The only test that counted: **does the colour / strong channel's actual
production `z` sit at `r = 3`?**

| channel | production site | `z` | level |
|---|---|---|---|
| colour: `bring_color_weighted` (**production**, canonical per ruling R3) | `closed_form_tau_M.py:307` via `markov_z` + δ bond shift | `q³/(q²+1)` | **2** |
| colour: `N = 3` fibre (**probe fixture only**) | `ocneanu_param_from_fibre_dimension.py:189` | `q⁵/(q⁴+q²+1) = q³/[3]_q` | 3 |

**It does not.** The production colour path runs `z_D` — the SU(2)/TL
parameter. Colour enters as a δ-perturbation on the p–n **bond factor**, not
as a change of fibre (mirrored in `hecke-engine/src/color_weight.rs`). The
level-3 parameter exists only as a positive-control fixture in
`convention-slip-registry.json` (`R3-trace-N3`): no registered channel, no
production consumer, no `evaluators` entry.

So the framework's colour sector is **not** tracing over a 3-dimensional
fibre, and "level 3 is SU(3), the eightfold way is SU(3)" has nothing in
production to attach to. **Dropped.** This closes the one channel where an
exception to the sibling's "no QOU channel sits at `r = 3` or above" would
most be expected.

**Flagging the numerology risk in my own reasoning, per the
critical-distance license.** Even had the measurement come out at `r = 3`,
it would not have supported the conclusion. SU(3) arises in representation
theory for many unrelated reasons; "the framework contains an SU(3)" and
"this is the SU(3) of colour" are different claims, and the second needs the
colour quantum numbers to *be* the SU(3) weights — a rank match is not
evidence. The measurement makes this moot, but the inference was unsound
before the measurement, not only after it. Existing homes for any further
SU(3) work: beans `qou-8p1x` (in-progress: 3-dimensional fibre / colour
SU(3) routes, already assessed) and `qou-8lxd` (eightfold EPIC).

---

## 5. Compute — `dim TL_n = Catalan(n)` vs `n!`

| n | Catalan(n) | n! | surviving `dim²` share |
|---|---|---|---|
| 4 | 14 | 24 | 58.3 % |
| 5 | 42 | 120 | 35.0 % |
| 6 | 132 | 720 | 18.3 % |
| 7 | 429 | 5 040 | 8.5 % |
| 8 | 1 430 | 40 320 | 3.5 % |

Any compute treating `G` as a form on `H_n` rather than on `TL_n` is working
in the kernel — 96.5 % of it at `n = 8`. This is now a theorem about every
`n`, not an observation at four of them.

**Bean correction: `qou-csdp` does not exist** (nor does `qou-rm47`). Both
were cited in the task; `beans show` returns "bean not found" for each, and
neither appears among the 3 570 beans. The nearest real IDs are the
convention-D tranche `qou-cds1`…`qou-cds4`. There is no existing bean
covering the n ≥ 6 consumer audit, so it cannot be "extended" — it has to be
opened. Filed as `qou-ii3w`.

---

## 6. Prioritised gap-closure map

| # | item | what the tower does | tier | status |
|---|---|---|---|---|
| 1 | `y_λ = 0 ⟺ ℓ(λ) > r`; D = level 2 | **CLOSES** — the two-row cap stops being a posit | proved (sorry-free) + symbolic-exact | done upstream; §3 lists the sites to re-cite |
| 2 | which fibre each channel traces over | **CLOSES** — every live channel at `r = 2`; `z_C` at no level | proved (sibling [N3]) + measured | done, PR #5229; §4 adds the colour rows |
| 3 | 8-fold / SU(3) at level 3 | **CLOSES NEGATIVELY** — production colour is level 2 | measured | done; drop the line of enquiry |
| 4 | ℓ¹ ceiling currency | **CORRECTS** — 59 % → 69.2 %, still < 1 | measured | done; downstream artifacts need updating |
| 5 | Δ_λ magnitude (`r*`, many-body) | **DOES NOT CLOSE** — support restriction is a value no-op; frame shift ~2 % vs misses of 5.7 %-wrong-sign and 586×-wrong-sign | measured, scope-(a) | **open.** The additive super-pairwise extensive term remains the gap |
| 6 | stale Δ_λ literals in 3 durable artifacts | — | — | open, §1 |
| 7 | `he4-two-row-dominance.md` C-frame 86.6 % | — | — | open, §3 |
| 8 | `pyhecke.gram` registry staleness | — | — | open — code is D, registry says C; R9 should be red |
| 9 | `n ≥ 6` `H_n`-vs-`TL_n` consumer audit | quantifies the waste | measured | open, `qou-ii3w` |

Beans opened: `qou-6snb` (item 5, the surviving Δ_λ gap), `qou-fx5g`
(item 4, propagate 69.2 %), `qou-ii3w` (item 9).

**The tower does not close the Δ_λ gap.** That is the honest headline. It
closes a foundational posit, settles the per-channel fibre question,
negatively closes the eightfold speculation, and corrects a live number in
the wrong direction. The many-body magnitude is untouched, and remains what
the 2026-08-02 audit said it was: a separate, super-pairwise, additive
extensive object that no per-block weight can supply.

## Verification

No Lean in this branch — disk was at 88 % on entry and 97 % at exit
(1.3 G free), below what an olean restore needs (a Lean worktree is 5.6 G).
Every claim here is Python/symbolic or a citation to already-verified Lean.
CI is `workflow_dispatch`-only, so the agent's own verification is the gate:
sympy exact over ℚ(q) for the tower; mpmath at 60–65 dps for every
measurement; proton pin throughout, no cached-witness accessor called
(`wedderburn_jones_markov.y_lambda_at` deliberately avoided in favour of the
live `schur_principal_mpmath.y_lambda_at_q0_mpmath`); no float64 serialized.
