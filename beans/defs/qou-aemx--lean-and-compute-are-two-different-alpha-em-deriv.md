---
# qou-aemx
title: The alpha_em Lean file holds TWO rival conjectures and the block cites only one; the 470 ppb figure compares the .md to the UNCITED one (corrected 2026-08-29)
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T16:32:49Z
updated_at: 2026-11-20T14:45:00Z
parent: qou-3l2l
---

Found while re-examining the two open knobs on `m_K/m_pi` (the framework's
only scoreable L2 result). Probe:
[`computations/alpha_em_lean_vs_compute_divergence_probe.py`](../computations/alpha_em_lean_vs_compute_divergence_probe.py).
Audit: `docs/audits/2026-08-28-alpha-em-lean-vs-compute-divergence.md`.

## The finding

Two constructions of `alpha_em^-1` live in the corpus and share **no**
ingredient:

| | prefactor | kappa | value | vs CODATA |
|---|---|---|---|---|
| `em-coupling-chern-simons.lean` | `45*[3]_q` = 136.9668 | `8*q` = 8.8798 | 137.035999532 | **+2.59 ppb** |
| `meson_em_sinh_closed_form.py` | `q*[9]_q*[10]_q` = 136.8232 | det ratio = 1.7216 | 137.035935094 | **-467.6 ppb** |

Prefactors differ by 1049 ppm; the kappas by a factor of 5.16; the results by
470 ppb.

Three consequences:

1. **The cited formalisation is not the computation.**
   `per_observable_100x_status.py` imports `alpha_em_inv_derived`, i.e. the
   -467.6 ppb one. So "m_K/m_pi is conditional on the Chern-Simons conjecture
   class in `em-coupling-chern-simons.lean`" names a premise the number does
   not rest on.
2. **The empirical form fits 180x better.** The .lean's own docstring says
   `kappa = 8q` is empirical -- *"The '8 = dim(su(3)) = gluon octet'
   interpretation is post-hoc; no structural derivation links su(3) gluon
   dimension to alpha_EM."* The derived Gram-ratio form is the one 467 ppb out.
   A more-empirical construction fitting better is the anti-fit signature.
3. **The .lean docstring contradicts its own def.** It describes kappa as "a
   Gram-determinant ratio from the Chern-Simons ..." while the `def` is
   `8 * q`. The producer computes the actual determinant ratio: 1.7216.

## What is NOT claimed

Not that either is wrong -- that is the open question. Not that the scorecard
moves: it does not, this is about what the number is conditional ON.

## Corrections to the red-team audit (2026-08-22) this implies

- **"imports experimental alpha_em" is STALE.** The literal
  `mp.mpf("137.035944")` is gone; alpha_em is computed from framework objects.
- **"conditional on an open Lean `sorry`" is STALE IN MECHANISM.**
  `em-coupling-chern-simons.lean` compiles exit 0 with **zero** sorries; the
  single `sorry` token in it is the word inside a comment describing its own
  past. It carries two unproved conjecture *classes* with no instance.
  **The epistemic status is UNCHANGED** -- a class-axiomatised conjecture is not
  a proof (AGENTS.md "Axiomatization is NOT a Proof") -- so **0/5 unconditional
  still stands**. Do not report the missing `sorry` as an improvement.

## Next

Decide which construction is canonical, or establish that they are the same
object under a reparametrisation (the 1049 ppm prefactor gap says they are not).
Until then the corpus asserts two incompatible alpha_em values.


## 2026-08-28 — half answered: NOT one object; and my own emphasis corrected

**"Are they the same object under a reparametrisation?" — NO, settled
symbolically.** Lean's prefactor is `45(q⁶−1)/(q²(q²−1))`; the compute's is a
degree-32 cyclotomic product over `q¹⁶`. They differ by 1.5× at q→1 and by
~1973× at q=2, and **cross at q\* = 1.11015574, 0.016 % from q₀**. The 1049 ppm
agreement is where the crossing sits, not shared structure — and is expected,
since both target ≈137 near the same point.

**Genericity test on both κ** (window giving |err| < 100 ppb):

| | claimed | window | width | % of claimed | inside? |
|---|---:|---|---:|---:|:--:|
| Lean `8q` | 8.8798 | [8.4744, 9.2648] | 0.790 | 8.9 % | yes |
| compute Gram | 1.7216 | [1.8739, 1.9567] | 0.083 | 4.8 % | no |

- `8q` is **in range, not forced** — the window also admits the integer 9
  (33 ppb).
- But bare `κ = 8`, the file's own *"dim su(3) gluon octet"* reading, gives
  **−220 ppb and misses**. The `q` factor does the work, not the 8.
- The Gram κ misses a *relatively tighter* window by 10 % — behaving like a
  prediction that is not quite right.

**RETRACTING MY OWN EMPHASIS.** The original entry (and PR #5886's body) called
the 181× gap an *"anti-fit signature pointing the wrong way"*. Over-stated: a
loosely-constrained empirical parameter beating a tightly-constrained derived
one is near what neutral assumptions predict. The measured facts stand; the
inference from them does not. Corrected in audit §8.

## Still open — the canonical question

Which construction is canonical is **not** settled. What is settled is that the
choice is real (they are different objects), and that the derived one is the
one making a falsifiable, currently-failing claim. Deciding it needs an owner
or a structural argument for one prefactor over the other — `45·[3]_q` vs
`q·[9]_q·[10]_q` — which nothing in the corpus currently supplies.


## 2026-08-28 (later) — the `8` IS structural, and I withdraw "nothing in the corpus argues"

I closed the previous entry with *"nothing in the corpus argues for `45·[3]_q`
over `q·[9]_q·[10]_q`."* I had not run all six grep paths. Running them:

**`8 = Vol(𝓑₃)/G`, exactly.** The Borromean rings `L6a4` — this framework's
**nucleon** knot — have `Vol = 2·V_oct = 8G` with `V_oct = 4G`, G Catalan.
Machine-checked to 30 digits; residual exactly 0. Already live and
load-bearing: the nucleon row of `fundamental-knots-operator-basis`, and the
binding scale `α = m_e·8G` in `binding-knots-visual-inventory`. And stated as
the κ reading outright in
`computations/_deprecated/alpha_em_q9_q10_derivation.py`: **`κ = 8q =
q · Vol(𝓑₃)/G`**.

**The live `.lean` carried the weaker of two available readings** — `dim su(3)
= gluon octet`, which it correctly called post-hoc — while the corpus held an
exact one it did not cite. Docstring corrected this tranche, caveats kept.

**This revises my own §7 framing.** *"The q does the work, not the 8"* is wrong
under the corpus reading: `q·Vol(𝓑₃)/G` is **one object**, so the `q` is part
of the claimed structure. Bare `κ = 8` missing at −220 ppb is *consistent with*
that, not damaging to it. The measurement is unchanged.

**A chronology also exists, and I missed it.** The same deprecated file shows
`45·[3]_q` **replaced** `q·[9]_q·[10]_q` — *"REFINED FORMULA (replaces the
troublesome 1.6 mystery constant)"*, the older form's correction needing a
`1.6` that PSLQ could not identify. So **production compute uses the superseded
prefactor**, now with a Gram κ instead of the 1.6 — a later, different
development.

## Still open, and now sharper

1. **The combination.** The identity fixes the `8`; it does not fix the power
   of `q` multiplying it. `Vol/G` and `q²·Vol/G` are not excluded.
2. **The cross-sector step — the load-bearing gap.** Why should a **nucleon**
   knot's volume set a coefficient in an **electromagnetic** coupling? Nothing
   found addresses this.
3. **Genericity unmoved.** κ ∈ [8.474, 9.265] still admits the integer 9
   (33 ppb): `8q` is in range, not forced.
4. **Does the revival supersede the supersession?** `q·[9]_q·[10]_q` was
   retired for needing an unidentifiable constant, then revived with a derived
   Gram κ. Whether that reinstates it is the canonical question, still open.


## 2026-08-28 (later still) — the cross-sector gap is a DILEMMA, and the corpus argues against the easy horn

Pursued the load-bearing open item. It does not close; it sharpens.

**The identity is not generic.** Only **2 of 9** corpus/standard hyperbolic
knots give an integer `Vol(K)/G` — Whitehead (4) and Borromean (8), both
octahedral. So the `8` is genuinely constrained, not a re-description. But the
constraint is *octahedral decomposability*, which has no bearing on EM.

**The corpus's own sector rule runs against the volume reading.**
`fundamental-knots-operator-basis` states, in the same table that carries the
`8G`: *"Torus knots carry zero hyperbolic volume, representing the massless,
force-carrying sector. Hyperbolic knots carry positive volume, which translates
to mass via Vol(K)/ℏ_q²."* — and places the **photon**, the EM carrier, as "not
a knot", `J = 1 (bare)`, in the **zero-volume** sector.

So a **nucleon** volume inside the **electromagnetic** coupling crosses the
framework's own volume↔mass / zero-volume↔carrier boundary.

**The dilemma:**

- If the **volume** does the work → it crosses that stated boundary.
- If only the **integer 8** does the work → the knot reading adds nothing over
  `κ = 8q` and the post-hoc charge returns, just aimed at a different gloss.

**This is not a numerical question and no probe will settle it.** It needs
either a structural argument for why a mass-channel invariant may enter a
force-carrier coupling, or an explicit statement that only the integer is
meant. That is an owner/structural call, which is why this bean stays open.

## 2026-08-29 — RETRACTION of the cross-sector dilemma: the block's .lean is STALE vs its own .md

I spent two tranches analysing `em-coupling-chern-simons.lean` without checking
it against `em-coupling-chern-simons.md`. They state **different formulas**.

| | formula | κ | value |
|---|---|---|---|
| **`.md`** (live) | `q·[9]_q·[10]_q·(1 + δ/(1−δκ))` | Gram ratio ≈ **1.7216** | 137.035935093976 |
| **`.lean`** | `45·[3]_q·(1 + δ + κδ²)` | **`8q`** ≈ 8.8798 | 137.035999531717 |

**470.2 ppb apart.** The `.md` reproduces the production compute *exactly*
(137.035935093976, byte-for-byte). And the `.md` names the `.lean`'s form as
its own **superseded** version: *"The order-δ² form … **which this proposition
previously displayed** … costs 11.06 ppb."*

**So the cross-sector dilemma is WITHDRAWN as a statement about the framework.**
The live formula uses **torus knots** `T_{2,9}`, `T_{3,5}`, and the `.md` says
outright: *"non-hyperbolic. Their τ-image geometric invariant is the
Chern–Simons functional, **not the hyperbolic volume**."* Zero volume, CS
invariant — exactly what the sector rule prescribes for a carrier. No nucleon
volume in the live formula at all.

**What survives:** `Vol(𝓑₃)/G = 8` is still exact and non-generic; `8q` is
forced within its ansatz family (below). Both are true statements about a
**superseded** coefficient.

**What is derivable** (measured on the superseded form; window `[8.4744, 9.2648]`):
`κ = c·q` → **c = 8 unique**; `κ = 8·q^n` → **n = 1 unique**; both free → three
pairs land, (8,1) best by ~13×.

**The lesson, and it is the corpus-grep discipline one level in:** a block's
`.lean` is not a primary source for the block's claim — the `.md` is. AGENTS.md
says as much ("the narrative/authoritative human-readable face"); I treated the
Lean as authoritative for two tranches and built a dilemma on it.

**The live block is honest about its own gap** — κ *"unproved"*, *"not computed
end-to-end"*, fit value *"≈ 1.8878"*, *"the entire ansatz uses the wrong
decomposition"* — matching this arc's independent finding that the Gram κ misses
(needs ≈ 1.9153). No over-claim there.

## Now open, and it is a different item

The defect is a **stale Lean sibling** (`proof-statement-integrity`): the `.lean`
does not state its `.md`'s claim. Fixing it means formalising the resummed
Gram-κ form. Not done here — it is a real content change and the target κ is
itself an unproved conjecture class, so the shape of the fix is an author call.
---

## Follow-on 2026-08-29 — the divergence is a CLASS (bean `qou-mdlv`, PR #5936)

PR #5931 retracted this bean's cross-sector dilemma on the finding that
`em-coupling-chern-simons`'s `.lean` states a formula its own `.md` supersedes.
The next question was whether that is a one-off. It is not.

Grepping content `.md` for blocks that announce their own supersession gives
six; of the four that have Lean, **two are divergent**. The second is
`prop:centered-hecke-variance-positive`, whose `.md` moved from convention C to
convention D on 2026-08-09 — explicitly withdrawing `Var(σ_i) ≈ 0.855` — while
its Lean sibling kept the C parameter, the dropped Wenzl hypothesis, and the
withdrawn figure, for 19 days.

That second case is worse than a stale docstring. The old encoding carried

    term1_pos : 0 < (q - q⁻¹) * z
    term2_pos : 0 < 1 - z²

as §3b context-class axioms. Under D they are not jointly satisfiable on the
`.md`'s domain: `term1_pos` forces `q > 1`, `term2_pos` forces `q < ψ` (the
supergolden ratio, `q³ = q²+1`, ψ ≈ 1.4655712319). So the class was inhabited
only on `q ∈ (1, ψ)` while the `.md` claims all `q > 0` — and `q = 1`, where the
`.md` says the minimum 3/4 is *attained*, is excluded. Fixed in #5936 by
deriving the closed form instead: six sorry-free, axiom-free declarations
replacing two class axioms.

**Both cases were invisible to every existing gate**, and the reason generalises:
the stale files type-check, so a compile does not catch them, and nothing
compares an `.md`'s displayed formula against its resolved `.lean`. The grep
above finds only blocks whose prose *says* it was superseded, so it is a lower
bound. Carried forward in `qou-mdlv`.


---

## CORRECTION 2026-08-29 — the 470 ppb compares the `.md` to a DIFFERENT conjecture

Re-read `em-coupling-chern-simons.lean` closely while writing up why its repair
is an author call, and found that this bean's own framing — including its title —
was imprecise in a way that matters.

**The file carries TWO conjecture classes for `1/α_EM`, and the block's
`lean.ref` points at only one of them:**

| class in the file | formula it is built on | `.ts` `lean.ref` points here? |
|---|---|---|
| `AlphaEmGluonOctetConjecture` | `alphaEmInvCorrected = 45·[3]_q·(1 + δ + κδ²)`, `κ = 8q` | **no** |
| `ChernSimonsCorrectionConjecture` | `q·[9]_q·[10]_q·(…)` | **yes** — `.ts` line 9 |

So the `45·[3]_q` / `κ = 8q` form this bean repeatedly calls *"the Lean"* belongs
to the **uncited** class. The class the block actually references carries the
**same prefactor as the `.md`** — `q·[9]_q·[10]_q` — and differed only in taking
the **truncated** `(1 + δ_CS + κδ_CS²)` where the `.md` gives the **resummed**
`(1 + δ_CS/(1 − δ_CS·κ))`.

**Measured cost of that real divergence: 11.07 ppb, not 470.** Re-derived at
50 dps at the proton pin with the Witten `κ ≈ 1.722`:

| form | `1/α` | vs CODATA-2022 |
|---|---|---|
| resummed (the `.md`) | `137.0359352` | −466.7 ppb |
| truncated (the docstring) | `137.0359337` | −477.8 ppb |

difference **11.0676 ppb**, reproducing the `.md`'s own stated `11.06`. The
`.md`'s other two figures check out independently too (`137.0359351`, `−468 ppb`).

**What stays true.** The file does contain a construction 470 ppb from the `.md`
— `alphaEmInvCorrected` — and the production compute does follow the `.md`. Two
rival conjectural formulas for one observable living in one file, only one cited,
is a real finding. What was wrong is calling the uncited one *"the block's
Lean"*, and therefore sizing the block's `.md`/`.lean` divergence at 470 ppb when
it is 11.

**Root cause, and it is the same one this bean already records.** I read the file
for *a* formula rather than for *which declaration the block cites*, exactly as I
earlier read the `.lean` instead of the `.md`. One level further in: **within a
file, the `lean.ref` names the declaration — a formula that merely shares the
file is not the block's claim.**

The docstring is corrected in the same tranche (resummed form + the measured
11.07 ppb). The `opaque` Prop and the absent instance are untouched: what the
conjecture asserts, which `κ` it asserts it of, and whether the tier is algebraic
or numerical remain author decisions.


---

## 2026-08-29 — TWO of the three stated causes of the -467 ppb are now CLOSED (PR #6000)

The block offered three explanations for its residual. It had already excluded
one itself (the truncation: the tower is geometric and resums, worth 11.07 ppb
against a 468 ppb gap). The other two were the ambiguities it names in `κ`.
Both are now closed, and neither closes the way the block expected.

**1. The basis choice is not an ambiguity at all.** The block lists *"the
choice of basis for the rank-2 sublattice"* as unfixed. A Gram matrix
transforms by congruence `G ↦ BᵀGB`, so `det` acquires `(det B)²` — the **same**
factor on the classical and the q-deformed side, where it cancels. `κ` is
independent of the basis for **every** invertible `B`: unimodular,
non-unimodular (a finite-index sublattice), or irrational.

Lean, sorry-free, `#print axioms` = the three standard ones:
`QOU/Archimedean/GramDetRatioCongruence.lean` — `det_congr_eq` (any `CommRing`),
`gramDetRatio_congr_invariant` (a `Field`), `gramDetRatio_indep_of_basis`.
Confirmed numerically to 60 digits under all three kinds of `B`.

This is the determinant analogue of `gauge_ratio_invariant` in
`QOU/Archimedean/GaugeGroupThreeScale.lean` — the corpus already held the
degree-0 ratio principle for Schur scalars and had **not** applied it here.
Nothing in the QOU tree carried a det-congruence lemma before this.

**2. The q-reading family is finite, and none of it lands.** The block's other
named ambiguity — *"the explicit form of `s_i, ℓ, c_i` in the q-deformed
setting"* — is enumerable: each of `s`, `ℓ`, `c` and `CS` admits two readings of
*"replace `m,n` with `[m]_q,[n]_q`"* (deform the composite, or deform its
constituents), giving **16** combinations, of which the shipped producer is one.

At the proton pin, `κ` spans `[-10.92, 144.61]` and **none** of the 16 falls in
the `[1.8739, 1.9567]` window that would bring `1/α` within 100 ppb.

| reading | κ | ppb |
|---|---:|---:|
| shipped (`s,ℓ,c` constituents, CS deformed) | 1.7216 | **−467.6** |
| `s` composite, rest as shipped | 2.1155 | +483.6 |
| all composite, CS classical | 3.2650 | +3266 |
| `s,ℓ,c` constituents, CS classical | 144.61 | +442899 |

Probe: `computations/alpha/alpha_em_kappa_qdeformation_family_probe.py`. Its
shipped row reproduces `_alpha_em_inv_derived` at **rel-diff 0.0** — without
that cross-check the table would be about the script, not the corpus.

**Do not read the bracketing as evidence.** The needed 1.9153 sits between the
shipped 1.7216 and the next reading's 2.1155. The map `κ ↦ 1/α` is monotone and
the 16 values span two orders of magnitude, so *some* adjacent pair brackets
almost any target in range. It carries no information.

**Nor is "the shipped reading is closest of 16" evidence for it.** That is what
selecting for closeness produces. It is the reading someone chose, and the
plausible reason they chose it.

**Scope, per AGENTS.md.** Scope-**(a)**: the `[m]_q` substitution family,
*alone*, does not supply the needed `κ`. **Not** scope-(b): a Gram-determinant
`κ` is not excluded, because a **different pairing** — different matrix entries,
rather than a different reading of these ones — is untouched by the enumeration.

**What survives.** Exactly the block's own third alternative, now the only one
left standing: *"the entire ansatz uses the wrong decomposition."* That is no
longer one hypothesis among three; it is the residual. Closing `κ` structurally
still requires deriving the pairing, which nothing in the corpus supplies.

**Not changed:** no number in the block moves. The prediction, the −467 ppb
residual, and the required `κ ≈ 1.9153` are all as they were. The `opaque` Prop
and its absent instance are untouched — which tier the conjecture belongs to
remains an author call, and the 0/5-unconditional L2 count is unaffected.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — On-`main` Verification of `.lean`/`.md` Alignment (`b36554ecec`, `9d726d6caa`, `114b24ba5b`) & `Q-3L2L-1 = 1` Cross-Link (`litlfred/qou#8141`)

- **Verified on `main`:**
  - `folio/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.lean` and `folio/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md` are now aligned on `main` (landed in `9d726d6caa` and `b36554ecec`, moved to `folio/` in `114b24ba5b`, updated in `e389b33b05`, `0` `sorry`):
    - Proves `carrierLinking_eq` ($\ell = 17$), `gramDetRatio_congr` (basis-invariance of $\kappa = \det G^{\mathrm{cl}}_{\mathrm{CS}} / \det G_q$ under $G \mapsto B^T G B$, also in `QOU/Archimedean/GramDetRatioCongruence.lean`), `csTower_resums` ($\sum_{j \ge 1} \delta^j \kappa^{j-1} = \delta / (1 - \delta \kappa)$ for $|\delta \kappa| < 1$), and `csTower_partialSum_two`.
    - States `ChernSimonsCorrectionConjecture` with `Gq : Matrix (Fin 2) (Fin 2) ℝ` carried as an explicit parameter and **no instance** (and no CODATA literal in any statement; the superseded `alphaEmInvGluonOctet` is retained only as a plain provenance definition).
  - Companion epic `qou-3l2l` formalization of the $(4,1)$ standard block Hoefsmit/Markov Gram and Schur reduction landed in `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`qou-mxnu`, `qou-vbz4`, commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`).
- Kept at `status: in-progress` per owner governance (structural derivation of the $q$-deformed CS pairing `Gq` / $\kappa$ remains open).

## 2026-11-20 (PR #8562, bean qou-q0pl)
Four alpha functionals measured side by side at the one-term proton / two-term
(#8554) / muon pins (docs/audits/2026-11-20-alpha-em-two-term-q0-pull.md):
form B -0.365/+75.970/+78.998 ppb; form A +0.994/+77.329/+80.357; CS tower
-467.636/-390.982/-387.942; ruled-out 45[3]_q +2.588/+5.885/+6.016. Form B and
the CS tower are different functions of q (additive term 8/(12 pi) constant vs
pi^2(98/45)[2]_q/2 hbar_q^2), coincident only at q0 — not truncations of one
another. The gram_kappa_numerical_value sorry was a false statement and is
replaced by a sorry-free refutation; kappa = 1.7216 is det G_cl/det G_q and
never used gramKappa (bean qou-wkgp). Status unchanged: the CS-tower conjecture
class still has no instance.

**2026-11-20T14:28:57Z — OWNER RULING (Carl, session 01VQDpPd): keep BOTH α_em forms, labelled; no pick by residual.**
Form B (q[9][10] + 8/(12π) + αH(1−h²α); scorecard α_em⁻¹ row, −0.365 ppb) and the CS tower
(meson_em_sinh_closed_form.alpha_em_inv_derived; m_K/m_π and c_em, −467.6 ppb) are structurally
different functions of q (PR #8562), so no truncation choice reconciles them. Each consumer keeps its
own, labelled, until one is derived. Bean stays open.

## 2026-11-20T14:39:28Z W13 — owner asked "if derived+proved, update compute; if not, work on it"

Form-B status for the default question: conditional + selected. Uses only q0 and Bring data (not circular), but H=[2]_q/(8pi) is 'empirical' in its own docstring; AlphaEmFixedPointNormalization carries codata_consistent as a field, no instance; the solver keeps the form with the smallest CODATA residual (alpha_em_4pi_fixed_point_solve.py:188); residual is +76 ppb at the q_2t pin. Not switched to default. Note: that witness compares against the Cs-recoil 137.035999084 (experimental_constants.py keeps it deliberately) — PR #8574 now names this in sm-params-gauge-couplings.
