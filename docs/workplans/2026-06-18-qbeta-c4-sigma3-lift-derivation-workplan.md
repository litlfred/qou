# Q_β c₄ Stage-C — derive the σ₃-lift Λ from the brane-tower map (workplan)

**Date:** 2026-06-18
**Branch:** `claude/qbeta-c4-stage-c-sigma3-lift-2026-06-18`
**Goal:** 1ppQ — Q_β; the `c₄` rung. Continues the merged #2465 (bridge + C13
+ H₄ preflight) and #2106 (Stage B). Owner directive: "start Stage-C σ₃-lift."

---

## 0. The open object (from #2465, now on main)

The merged preflight ([Stage-C scope](../scope/2026-06-18-qbeta-c4-h4-tower-stage-c-scope.md))
established, validated at 50 dps:

- H₄ Hoefsmit seminormal reps + the H₃⊂H₄ branching map are correct;
- **σ₃-gating**: a σ₃-free element carries no new H₄ DOF, so `c₄` is gated on a
  **length-4, σ₃-involving** element `Λ ∈ H₄(q)` lifting the decay operator
  `ΔT ∈ H₃(q)`.

The open question (the keystone of this branch):

> **Which `Λ` is the categorically-correct σ₃-lift of `ΔT`, such that its
> level-4 Markov-trace component yields `c₄`?**

## 1. STRICT discipline — derive, never fit

The refuted-class map + flip-flop guard forbid the obvious trap: enumerating
σ₃-extensions of `ΔT` until one's `c₄` matches the target. **That is fitting and
will be caught.** `Λ` must be **derived** from categorical content:

- **Source of `Λ`:** the brane-tower N→N+1 map (`prop:mass-endomorphism-tower`,
  generator `V̂_i`, the physical tower variable `z = |V̂_i|`). The decay
  operator's lift under adding one strand/cell is what specifies the σ₃ entry —
  not a free choice.
- **Anchor-stability gate (registry §8):** any `c₄` produced must pass
  proton+muon swing < 1%, else `empirical`, dead on arrival.
- **Bar-evenness + q=1 shadow** (refuted-class map §1 invariants) must hold.
- **Reduce to the #2465-validated H₄ machinery** (seminormal + branching).
- **Tiered reporting** (proved / near-match / fitted); no production wiring,
  no registry tier change unless a genuine, anchor-stable closure (→ owner
  escalation, not self-wire).

## 2. Coordinate — the Φ_q line is the same object

Commit `e451d436` (merged) wired the **Φ_q / z-Habiro** bridge and flagged the
same N=0-vs-tower split that my #2465 synthesis surfaced: its N=0→Φ_q correction
(9.36% at the *representative* scale `z=ℏ_q²`) is **not** the production
brane-tower `z`, and
*"pinning the production z and wiring it into the mass table is the next step."*
That production `z` is the **same `|V̂_i|`** the σ₃-lift must use. So Stage-C and
the Φ_q line share the open `z`; coordinate, do not duplicate.

## 3. Work plan (one principled step at a time)

1. **Identify the categorical specifier of `Λ`** — read
   `prop:mass-endomorphism-tower` + the N→N+1 map + the Φ_q `z` (research in
   flight). Output: the *derivation rule* for how σ₃ enters, with no free
   parameter. **If no rule exists, that is the finding** — `Λ` is genuinely
   underdetermined and Stage-C is blocked on new categorical content (report
   honestly, do not invent a rule).
2. **Construct the canonical lift candidate `Λ`** from that rule (if it exists).
3. **Compute its level-4 Markov-trace `c₄`** via the #2465 machinery; check the
   §1 invariants (anchor-stability first — kill early if it swings).
4. **Tier-report.** Closure (anchor-stable, derived) → owner. Near-match →
   refuted-class row. Underdetermined → state precisely what is missing.

## 3a. Step-1 finding — the σ₃-lift rule is identified (Λ not underdetermined at the rule level)

Research mapped the categorical specifier. The σ₃-lift is **not** a free choice:

1. **Canonical N→N+1 map = stabilisation / coface.** `prop:mass-endomorphism-tower`
   + [`markov-moves-brane-tower.md`](../../content/quantum-observable-universe/braids-and-knots/markov-moves-brane-tower.md):
   the vertical Markov move `β ↦ β·σ_n^{±1}` is the coface
   `δ^i : A_n ↪ J¹(A_n)=A_{n+1}` (jet prolongation). This is *the* canonical way
   σ₃ enters — no enumeration.
2. **…but the canonical stabilisation is trace-TRIVIAL.** By the Markov property
   `tr_M(x·σ_n^{±1}) = z^{±1}·tr_M(x)` (`z = 1/(q^{½}+q^{−½})`, the Markov
   parameter). So `tr_M^{H₄}(ΔT·σ₃) = z·tr_M^{H₃}(ΔT)` — exactly the **C12-refuted**
   scalar. The naive lift carries no new `c₄`. (Confirms C12 *categorically*, not
   just numerically — and matches #2465's σ₃-gating.)
3. **The non-trivial content is the subset-correction tower.** The
   mass-endomorphism-tower is `∏_i V̂_i^full + Σ_{∅≠S, |S|≤2} z^{|S|}·Vol_q^{(S)}`.
   The new `c₄` (level-4) content must come from the **`|S|=2`, σ₃-involving**
   subset corrections `z²·Vol_q^{(S)}`, not the leading product.
4. **Candidate Q_β rule (to VERIFY, not asserted):** Q_β is the bar-odd (`sinh`)
   partner of the bar-even (`cosh`) mass scale (cheat-sheet; counit `ε(Δ)=h²/2−h`
   bar-split, #2469). So the candidate derivation is **`c_k` = bar-odd projection
   of the mass-tower `Σ_{|S|≤2} z^{|S|} Vol_q^{(S)}` applied to the lifted `ΔT`**,
   read in `u_L`. Every choice (z, the `|S|≤2` structure, the sum over S, the
   bar-odd projection) is fixed by canonical content — *if* this rule holds, `Λ`
   is fully determined. **Not yet established** — it is the next compute's
   falsifiable hypothesis.
5. **Production-z pinned — resolves the Φ_q line's open "next step".** The
   Φ_q wiring (`e451d436`) left "pin the production z" open; the tower fixes it as
   `z = 1/(q^{½}+q^{−½}) ≈ 0.4993` at q₀ (the Markov parameter), **not** the
   representative `ℏ_q² ≈ 0.0098` the Φ_q probe used. Coordinate this back.

**Decisive next compute (defined, falsifiable, non-fitting):** build the `|S|=2`
σ₃-involving subset corrections `z²·Vol_q^{(S)}` of the stabilised `ΔT` via the
#2465 H₄ seminormal machinery, bar-odd project, change variable to `u_L`, read
`c₄`. Check anchor-stability FIRST (kill early). Tier-report. If the candidate
rule (§3a.4) gives an anchor-stable `c₄` matching the bias-corrected empirical →
closure (owner escalation); else → refuted-class row + the rule is wrong.

## 3b. 𝔙 complex-volume review (owner steer, 2026-06-18) — re-targets the compute, RETRACTS §3a.4

Owner asked whether the complex-volume `𝔙` perspective helps. **It does — decisively** — and it
**retracts §3a.4** (which was built on a superseded form). Findings:

1. **The c_k ladder is the Im leg of the fibre-level COMPLEX `𝔙(q)`.**
   [`complex-volume-ladder-intro.md`](../../content/quantum-observable-universe/mass-theory/complex-volume-ladder-intro.md):
   `𝔔_β = Im 𝔙` (bar-odd, sinh), `𝔈_bind = Re 𝔙` (bar-even, cosh); the ladder
   `𝔔_β = 𝔔_base·∏(1+c_k u_L^k)` is *"the Im leg of one complex-volume expansion whose Re leg is the
   binding ladder,"* and the `c_k` are *"Taylor coefficients of the fibre-level complex `𝔙(q)`."*
   This is **exactly** the fibre-level complex-analytic object the refuted-class map §1 required —
   and it **explains C13**: a real-q *trace* (`Δtr_M`) cannot be the complex `𝔙`, so the #2465 bridge
   was bound to fail. The cross-anchor near-match is one complex coefficient read along its two
   parities.

2. **RETRACT §3a.4 (twice).** (a) The `Σ_{|S|≤2} z^{|S|} Vol_q^{(S)}` form is the **SUPERSEDED**
   `ρ_q` ansatz of `prop:mass-endomorphism-tower` (top-of-file banner: "do NOT use for production");
   the corrected form is the operator-valued graded expansion
   [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/mass-endomorphism/rho-k-graded-expansion.md).
   (b) The bar-odd leg is **NOT** `Li_2^q`: `_li_2_q_util.py` documents `Li_2^q` as **bar-invariant**
   (bar-even) — it is the **Re/binding** leg (the `T₃ = −z²Σ Li_2^q(−|V̂ᵢV̂ⱼ|)` term). The bar-odd
   `Q_β` (Im) leg uses **`Φ_q` (Faddeev, bar-asymmetric)** — the cheat-sheet's `Φ_q`-vs-`Li_2^q`
   context-sorting.

3. **The Q_β c₄ compute IS the merged Φ_q line.** The bar-odd/Im leg is `Φ_q` — exactly what
   `e451d436` (`zhabiro_phiq_wiring.py`) computes. So Stage-C's `c₄` and the Φ_q line are the **same
   object**; the production argument of `Φ_q` is the generator norm `z = |V̂ᵢ^full|`
   (`wedderburn_pair_volumes.py` / `atom_per_generator_volumes`), **not** the Markov subset-weight
   `1/(q^{½}+q^{−½})` (correction to the prior commit's z claim — there are two distinct `z`'s).

4. **Unification (to verify):** `Q_β c₄` (Im/`Φ_q`) and the binding pair-gen correction
   (Re/`Li_2^q`, *also open* per `prop:rho-k-graded-expansion` "pair-gen piece (open)") are the two
   parities of one open `𝔙` pair-term — closing one informs the other.

**Re-targeted decisive compute:** the bar-odd `Φ_q` pair-gen term of `𝔙` for the decay braid, at the
production generator-norm `z = |V̂ᵢ^full|`, Im leg → `c₄`, anchor-stability first. This is the **open
frontier of the active Φ_q line** — coordinate with it (hand over the `𝔙`-leg-sorting + the
binding-unification), do not duplicate. The pair-gen functional form is open for *both* legs, so a
first-principles closure is the shared blocker; running the simple form would fit it.

## 3c. Step-2 VERDICT (c₄ attempt, 2026-06-19) — underdetermined; blocked on `conj:rho-k-pair-gen-canonical-form`

Acting on the owner directive "attempt the Φ_q bar-odd pair-gen c₄ now"
(coordinated with §2's consolidate directive). The corpus-grep checklist
(STRICT) resolves the attempt **without any new compute** — and the no-compute
outcome is itself the discipline working, not a shortcut:

**Finding — the c₄ closure reduces to an already-tracked open conjecture.**
The §3b re-target ("bar-odd `Φ_q` pair-gen term … Im leg → `c₄`") lands on the
**pair-gen functional form** `f_2(q, V̂_i, V̂_j)`, which is already a named,
tracked open object:
[`conj:rho-k-pair-gen-canonical-form`](../../content/quantum-observable-universe/mass-endomorphism/conj-rho-k-pair-gen-canonical-form.md)
(promoting the "pair-gen piece (open)" subsection of
[`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/mass-endomorphism/rho-k-graded-expansion.md)).

**Why no non-fitting compute can close it this session:**

1. **The simple forms are already refuted.** The naive log-additive
   `α z² Σ ln|V_iV_j|` and the Wedderburn-decomposed form (correct
   `w_sym/w_std/w_alt` weights, naive functional) both **degrade** accuracy
   across `Z=1..20` — recorded in `rho-k-pair-gen-extension.witness.json`,
   with the prior probes now under `computations/_deprecated/`. Re-running a
   simple form is re-treading refuted ground (a fit, gated).
2. **The expected form is `−z²·Li₂^q`, but its derivation is PENDING.** The
   six-term `T₃ = −z² Σ Li₂^q(−|V̂_iV̂_j|)` (`thm:knot-mass-formula-unified`,
   Kashaev limit) is the *believed-correct* `f_2` per the conjecture's evidence
   table, but the Kashaev-limit derivation — parallel to the **proved**
   single-gen `α Σ ln|V̂_i|` → `T₂` — has **not** been completed. Without it,
   asserting `f_2` is invention (the workplan §3 step-1 "do not invent a rule").
3. **Both parities share this one blocker (the §2 + §3b unification, now
   sharpened).** `Li₂^q` is bar-**even** (`_li_2_q_util.py`) ⇒ the **Re/binding**
   leg; the **Q_β c₄** is the bar-**odd** **Im/`Φ_q`** partner. They are the two
   parities of the *same* open `f_2` pair-term. ⇒ **the Kashaev-limit derivation
   of `f_2` closes BOTH the Q_β Im/`Φ_q` leg and the binding Re/`Li₂^q` leg
   simultaneously.** This is not two open problems — it is one.

**Tiered status of the c₄ attempt:** `underdetermined` (not `near-match`, not
`fitted`, not `refuted`). The precise missing categorical input is the
**Kashaev-limit / `O(ℏ_q)` derivation of the pair-gen functional `f_2`**
(equivalently: the explicit closed-form mass element `Φ_mass(W)` of
[`conj:mass-endomorphism`](../../content/quantum-observable-universe/mass-endomorphism/mass-endomorphism-conjecture.md) at pair level). c₄ is **not Lean-closable** and **not numerically closable** without it.

**Consolidation + handoff (the §2 directive, executed):** the `𝔙`-leg-sorting
(Im=`Φ_q`/Q_β, Re=`Li₂^q`/binding) and the both-legs-one-`f_2` unification are
recorded here and handed to the active **Φ_q / z-Habiro line** (PR #2475,
production `z = |V̂_i^full|` pin) and to `conj:rho-k-pair-gen-canonical-form` as
the shared blocker. Stage-C does **not** fork a fresh probe; it converges on the
Φ_q line. No production wiring; no registry tier change.

## 4. Honest forecast — discharged

Closure odds this session were **modest** — this is the open keystone after ~12
refuted classes, and `Λ` proved underdetermined by current categorical
content. The honest deliverable is *that*, sharply stated (§3c): c₄ is blocked
on the pending Kashaev-limit derivation of `conj:rho-k-pair-gen-canonical-form`,
which is one object with two parities (Q_β Im / binding Re). A principled
attempt that pins exactly the missing categorical input — not a fitted `Λ`.
