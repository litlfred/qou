---
# qou-48is
title: 'GAP: the canonical cross-species nucleon ordering p...pn...n is an unlicensed choice and tr_M depends on it by O(10%) for A>=3'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T04:34:20Z
updated_at: 2026-11-17T07:34:00Z
parent: qou-v2om
---


## Context (spun out of `qou-prjo` by PR #4850, 2026-08-09)

**The gap.** `atom_braid_word_3A(Z, N)` fixes the cross-species arrangement of
nucleons to the canonical string `p...pn...n`. Nothing in the corpus derives that
choice, and the canonical scalar observable depends on it.

**1. The orbit identity does NOT license it.** `tr_M(beta) = tr_M(rep)`
(`computations/atom_orbit_reduction.py`,
`docs/audits/2026-05-30-orbit-trace-identity-proof.md`) ranges over `S_Z x S_N`
only — protons among protons, neutrons among neutrons — and its Lemma 1
establishes it by showing such a permutation leaves the WORD unchanged. It says
nothing about the arrangement `pnn` vs `npn`, which is a different word.

**2. The stated reason is a COST property, not a selection rule.** The module
docstring justifies the canonical ordering as "interface-minimal (exactly one pn
crossing; every other ordering of the same multiset has >= 1 and generically
more)" and concludes "the cheapest (canonical) one is always valid" — but the
validity claim is the orbit identity, which only covers the orbit within which
the word never changes. The comparison ACROSS orderings is left unjustified.

**3. And it matters, measured** (PR #4850, certified Frobenius pairing:
tr_M(1) = 1, Markov M1 to 4e-16, constant M2 ratio to 6e-16; experimental proton
anchor; live `y_lambda_at_q0_mpmath`):

    T (1p2n)   tr_M(pnn) = tr_M(nnp) = 0.1040710573547   {pn:1, nn:1}
               tr_M(npn)             = 0.1415755179229   {pn:2}      -> +36.0 %
    He3 (2p1n) tr_M(ppn) = tr_M(npp) = 0.2065784335107   {pp:1, pn:1}
               tr_M(pnp)             = 0.1633620457246   {pn:2}      -> -20.9 %
    D (1p1n)   tr_M(pn)  = tr_M(np)                                  -> 1.5e-41

`tr_M` tracks the **interface multiset exactly** — bit-identical within a class,
O(10^-1) across classes. D is a null control: its two orderings share one
interface multiset, so its exact invariance (40 dps) shows the machinery does not
manufacture spurious differences.

**Consequence.** Every canonical mass/binding number for an `A >= 3` isotope
containing both species inherits an undetermined O(10 %) factor from an
arrangement convention.

**What would close this.** Either (a) promote interface-minimality to a derived
selection rule with an argument from the substrate (why does the physical nucleus
realise the minimal-interface arrangement?), or (b) build the observable so it
does not depend on the arrangement — e.g. an average over arrangements, which
would itself need deriving, and which is NOT the `S_Z x S_N` symmetrization
(that one is the identity map, Lean-proved in
`QOU/MassTheory/NucleonOrderingSymmetry.lean::sum_symmetrize_eq_nsmul`).

**Do NOT** pick an arrangement rule by which one lands nearest AME — that is the
forbidden fit. Derive it or report the ambiguity.

Reproducer: `computations/probes/nastokes_orbit_symmetric_readout_probe.py`
(Part B) -> `nastokes-orbit-symmetric-readout.witness.json`.
Audit: `docs/audits/2026-08-09-nastokes-orbit-symmetric-readout.md` s4, s7.

---
## Update 2026-08-09 — PR #4851 (branch claude/canonical-ordering-dof-2026-08-09)

Audit: `docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md`
Probe: `computations/probes/canonical_ordering_dof_probe.py` -> `canonical-ordering-dof.witness.json` (22/22, 41 s)
Lean:  `QOU/MassTheory/CanonicalOrderingSaddle.lean` (sorry-free, 6 decls, axioms clean)

### Q1 — LIVE IN PRODUCTION (settled)

mass_table_comprehensive.try_binding_symbolic_log_trace / try_binding_canonical
-> binding_canonical(use_closed_form=True) -> closed_form_tau_M ->
closed_form_ratio, whose interface product iterates a HARDCODED
`["p"]*Z + ["n"]*N` (closed_form_tau_M.py:290; also :233 in
canonical_interface_kinds). The appendix alg: block mba-step03-markov-trace.md
calls binding_canonical a "production binding consumer (A >= 3)".

14968 mixed-species A>=3 rows of mass-table-comprehensive.witness.json carry a
B_pred_MeV (hence m_symbolic_MeV, m_err_pct_sym) that moves. B_pred =
-alpha*ln(tau_M) so the shift is exactly additive, dB = -alpha*ln(ratio),
alpha = 3.744460 MeV. T: 1.152 MeV = 13.58% of B_AME. 6Li 7.20%, 12C 3.39%,
56Fe 1.79%. 60 rows above 1% of B_AME; largest absolute spread 33.9 MeV.

NOT affected (do not inflate): the L2 100x dashboard (all 7 rows A<=1;
m_D/m_T/m_3He/m_4He are CODATA targets with NO prediction row emitted -- count
stays 2/7), the L1 dashboard, canonical_mass.py (Borromean F_Bor has no
cross-species arrangement -- no nucleon mass moves), mass_table_ppb.py
(Kashaev volume law, never calls atom_braid_word_3A), and the deuteron
(exactly ordering-independent, one interface class).

### Q2 — the bean's premise is OVERTURNED by the corpus-grep

This bean recorded "interface-minimal is a cost property, not a selection rule".
True of atom_orbit_reduction.py -- and the wrong place to stop. A selection rule
DOES exist:

  prop:ground-state-ordering (mass-theory/ground-state-ordering{,-derivation}.md,
  nuclear-interactions/atomic-nf-witness.md): the ground state MINIMISES
  Phi_q = sum_i log|V_i|, and for A >= 4 it is INTERLEAVED + tail-packed;
  sorted is optimal ONLY for A <= 3. Realised in compute by
  hecke_core_symbolic._ground_state_ordering, ordering_cache.get_ordering,
  Rust HeckeEngine.ground_state_ordering, hadron_knot_table.

So there are TWO LIVE CONVENTIONS and production uses the other one. Measured
under the production trace, the corpus's ground-state ordering is strictly LESS
bound at every A >= 4: -0.272 (4He), -0.544 (6Li), -0.816 (9Be), -1.361 (12C),
-1.905 (16O), -5.171 (40Ca), -6.804 (56Fe) MeV. Opposed in sign.

The rule is STATED, NOT PROVED: QOU.ParticleInteractions.ground_state_ordering
is `def ... : Prop` with no discharging instance; the .md derivation is an
eigenvalue heuristic + exhaustive search for A <= 14 only; .ts carries
validation:"not_checked". So the DOF is SHARPENED, not closed.

### The exact structure (verified, 3140 orderings, 8e-51)

  P(o) = f_pp^(Z-b_p) f_nn^(N-b_n) f_pn^(b_p+b_n-1)
  P(o)/P(canonical) = (f_pn/f_pp)^(b_p-1) (f_pn/f_nn)^(b_n-1)

At the experimental proton anchor f_pn/f_pp = 0.7907 < 1 < 1.3601 = f_pn/f_nn
-- OPPOSITE sides of 1 -- so the sorted (1,1) corner is a SADDLE. Measured
neither argmin nor argmax on 4He/6Li/8Be/7Li/12C/16O. CANDIDATE 1 (extremal
principle selects the sorted ordering) is REFUTED, scope-(b), cited invariant =
the block factorisation + the straddle.

CANDIDATE 2 (multiset is the datum): premise TRUE (proved in closed form and in
Lean, ifaceProd_eq_of_ifaces_perm) but the multiset is NOT an isotope invariant
(4He has 4 distinct multisets over 6 arrangements) -- it re-coordinatises the
freedom as (b_p, b_n) rather than removing it.

Cross-check: two INDEPENDENT full H_{3A} trace pipelines reproduce the
closed-form single-interface ratio -- Wenzl bridge / strict_averaged (1.1e-8)
and #4850's y_lambda x Hoefsmit / bring_color_weighted (3.4e-14). Same-multiset
null floor 4.2e-10.

### Scope

scope-(b) for candidate 1 ONLY. scope-(a) for the headline: nothing is
DETERMINED. A selection rule of another kind (confinement/SDP over arrangements,
Markov move, normal form, coordination graph) is NOT excluded -- none was found,
which is not the same as none existing. free_parameters=0, no AME selector,
nothing wired, no ordering recommended. Bean stays OPEN.

### What would close it

1. Reconcile Phi_q (transfer-matrix, the ground-state rule's objective) with
   ln tau_M (closed-form Markov trace, production's objective). They disagree in
   SIGN about interleaving. Until settled, "the ground state" is ambiguous.
2. Prove or refute prop:ground-state-ordering. If right, production has the
   wrong arrangement for every A >= 4.
3. Or build the observable to not depend on the arrangement (NOT the S_Z x S_N
   symmetrization -- #4850 proved that is the identity map).
4. Either way, declare the convention explicitly instead of leaving it in a list
   literal at closed_form_tau_M.py:290.

### Small separate items surfaced

- hecke_core_symbolic._ground_state_ordering does not implement rule (iii): at
  3He it returns `pnp`, but prop:ground-state-ordering (iii) says sorted `ppn`
  wins for A <= 3. Helper and proposition disagree at A = 3.
- mass-table-comprehensive.witness.json has NO 3He (2,1) and NO 4He (2,2) rows,
  though 5He..12He are present.

---

## Update — PR #4854 (2026-08-09): both "small separate items" settled. Bean stays OPEN.

Diagnostic only. Production untouched; **no published number changed**.
Probe `computations/probes/ground_state_ordering_a3_probe.py` ->
`ground-state-ordering-a3.witness.json`; audit
`docs/audits/2026-08-09-ordering-loose-ends-a3-helper-and-missing-he-rows.md`;
Lean `QOU/MassTheory/TransferFactorCommute.lean`.

### Item 1 — helper vs prop rule (iii) at A=3: classification (a), the HELPER is defective

Computed the proposition's OWN objective `Phi_q = sum_i log|V_i|` via the corpus
implementation `_phi1_from_ordering_sym`, over EVERY arrangement, at the experimental
proton anchor:

    3He (2,1)   Phi_1(ppn) = -2.37519810839658325   <- argmin; = sorted; = rule (iii)
                Phi_1(npp) = -1.98321927125222633
                Phi_1(pnp) = -1.71732004705805955   <- the helper; LAST of 3
    T   (1,2)   Phi_1(pnn) = -2.46308887937445802   <- argmin = sorted = helper (no dispute)

Not only at A=3. The helper performs NO variational search -- it is a fixed
interleaving generator, bit-identical to `_alternating_ordering_sym` -- and is the
Phi_1 argmin in only **5/16** swept cases, the strict WORST of every arrangement at
(3,3), (5,5) and (7,7). Candidate (c) tested and rejected: it is the extremum of no
other objective the corpus states (phi_nuc 10/16, -phi_1 5/16, |phi_1| 5/16).

**Caveat, proved in Lean.** On the BARE NUCLEON chain `ppn` and `pnp` are EXACTLY
degenerate (both -0.878523297318204006). The transfer factors `T(d) = S + d.1` all
COMMUTE, so the chain product -- and the readout -- depends on the crossing
coefficients ONLY as a MULTISET. Rule (iii)'s "sorted BEATS interleaving" is therefore
a TIE at 3He, strict only after the electron tail is appended, and that separation is
generated entirely by `_crossing_coeff_sym` having NO `(n, e)` case (returns `None`,
silently skipped). Both readings put sorted at the optimum; neither supports `pnp`.
The same theorem explains why `atom_V_full_sym` is EXACTLY ordering-independent.

**NOT FIXED.** A fix leaves V0/V1 untouched but moves the Hecke NF vector: worst
relative delta 0.049 at (2,1), 2.52 at (2,2), 0.80 at (3,3) -- and `build_atom_nf_sym`
/ `build_atom_nf_mp` feed committed witnesses. Crosses the scope bar; left for the owner.

### Item 2 — 3He/4He absent from the mass table: GENERATOR BUG (false-premise guard)

`mass_table_comprehensive.py:153`:

    if a > 4:  # Avoid duplicates with explicitly added H, He isotopes

The premise is FALSE: `ISOTOPES = [("p",1,0), ("n",0,1), ("D",1,1), ("T",1,2)]` is
H-chain only (every Z <= 1) and the filtered grid starts at z = 2, so the intersection
is empty. Measured: 14974 grid rows -> 14968 kept, **6 dropped**, ZERO of them actual
duplicates:

    (2,0) 2He diproton (unbound)   (2,1) 3He BOUND   (2,2) 4He BOUND
    (3,0) 3Li (unbound)            (3,1) 4Li (unbound)   (4,0) 4Be (unbound)

Both the list and the guard were introduced in the same commit -- not drift. No
documented reason found in content/, computations/, docs/audits/, docs/coordination/.

**Collateral.** The witness's SOLE assertion `all_A_leq_4_masses_computed` ("All A <= 4
isotopes have absolute mass predictions") ranges over the POST-filter rows = {p,n,D,T}.
It passes precisely because the filter removed the rows it claims to cover -- true of
the emitted rows, false of its own wording.

**NOT REGENERATED** (moves published numbers).

### Three corrections to PR #4851 §2 / §3.4 — do not propagate

1. Rust `HeckeEngine.ground_state_ordering` **does not exist** (no `ground_state`
   symbol in `tools/hecke-engine/src/`; `hecke_rust_bridge.compute_nucleus` is absent
   from the live tree -- only `_deprecated/`). The Rust path returns `None` always.
2. `ordering_cache.get_ordering` falls back to **SORTED** (`[1]*Z + [0]*N`) off-cache,
   NOT interleaved.
3. The committed cache matches **neither** the proposition's formula **nor** the Phi_1
   argmin: (2,2)->`nppn` vs `npnp`; (3,3)->`npnppn` vs `npnpnp`; (6,6)->`npnpnpnpnppn`
   vs `npnpnpnpnpnp` (final two strands swapped each time). Argmin in 5/12 cases.

So there are **four** mutually inconsistent artefacts, not two conventions.

### Scope

scope-(a) throughout; **no scope-(b) exclusion is claimed** in this update. The
classification of both items is settled; WHICH arrangement production should use is
NOT determined and no ordering is recommended. `prop:ground-state-ordering` remains
stated-not-proved. free_parameters = 0; q0 = experimental proton anchor, layer-pure.

### Added to "what would close it"

5. Either make `_ground_state_ordering` actually minimise Phi_1 (a suffix-multiset DP,
   cheap given `chainProd_perm`) or RENAME it `_interleaved_ordering` so it stops
   claiming a variational status it does not have. The rename is free and honest; the
   fix moves witnesses and needs owner sign-off.
6. Decide whether Phi_1 or Phi_nuc is the ordering objective, and close the `(n, e)`
   hole in `_crossing_coeff_sym` deliberately. At 3He the whole strict/tie question
   turns on it.
7. Fix the `a > 4` guard, regenerate the mass table with the 3He/4He rows restored,
   and restate `all_A_leq_4_masses_computed` so its wording matches its range.

---

## PR #4855 (2026-08-09) — `prop:ground-state-ordering` truth-value SETTLED, per clause

The corpus's *stated* selection rule turns out not to be a `Φ_q`-minimality
rule at all, so reconciling the four ordering artefacts to it would relabel
the arbitrariness rather than remove it.

**Verdict.**

| clause | verdict |
|---|---|
| `A ≥ 4` interleaved + tail-packed minimises `Φ_q` | **FALSE** |
| `A ≤ 3` sorted beats interleaving | **TRUE at `A = 3`**, false as stated at `A = 2` |

**Evidence.** Exhaustive sweep over every `C(A,Z)` arrangement, `Z ≤ N`,
`A ≤ 16` (128 sweeps, 55 588 evaluations, 131 s), at the experimental
(proton) `q₀`, on **both** readouts (`Φ_nuc` bare chain; `Φ₁` with the
`["e"]*Z` tail). Probe `computations/probes/ground_state_ordering_argmin_sweep.py`,
witness `computations/ground-state-ordering-argmin-sweep.witness.json`,
cross-checked against `_phi1_from_ordering_sym` to 1.7e-55.

- Prescribed arrangement is argmin in **17/62** (`Φ_nuc`) / **10/62** (`Φ₁`)
  and strict **argmax** in 12/62 / 8/62.
- Sharpest counterexample `A=5, Z=1`: prescribed `npnnn` is rank **5/5** on
  both readouts; sorted `pnnnn` is the argmin, by **1.352 nats**.
- Rule (ii) (tail packing) refuted independently: the argmin **head**-packs
  — at `Z=1` the minimising proton sits at `A-5` for every `6 ≤ N ≤ 15`.
- `A=2` is an **exact tie** under `Φ_nuc` (multiset degeneracy from the
  commuting transfer factors) and a strict *loss* for sorted under `Φ₁`.

**Lean (sorry-free, umbrella-registered, `#print axioms` clean).**
`QOU.MassTheory.GroundStateOrderingRefutation` — the counterexample holds for
a whole interval of `q` above 1 (numerically `1 < q ≲ 1.22`, anchor well
inside), via the certificate `RHS − LHS = (t−1)·(deg-20 poly with all
coefficients positive)`, `t = √q`. `transferEigen_vieta` records the one
conjunct of the original proposition that survives: `λ₊λ₋ = −1`.

Audit: `docs/audits/2026-08-09-ground-state-ordering-truth-value.md`.

**Bean stays OPEN.** The precondition is now settled, but the underlying gap
is not: which ordering production should use is still underived and is the
owner's call. No production behaviour was changed and no published number
moved by #4855.

## 2026-09-04 — NARROWED: real for tr_M, nearly irrelevant for B

This bean's measurement stands: `tr_M` tracks the interface multiset and moves
20-36 % across orderings of the same `(Z,N)`. But for the BINDING law that
dependence almost cancels. Measured on 2548 AME nuclides
(`qbeta_tower_log_z_and_roast_probe.py`), p5-p95 residual of
`B = E_0.log(tr_free/tr_atom)`:

    segregated  p..p n..n   (atom_braid_word_3A)        1.22497
    alternating p n p n ..  (build_atom_nf_exact)       1.23227
    all-pairs, renormalised to A-1 bonds                1.22624

within **0.6 %** of each other. And the first-order asymmetry coefficient in
`e = q-1` is **exactly `N - Z` for all three** (all-pairs 31.76 vs 32 at
Z=50,N=82) — so the isospin content of the law is layout-INDEPENDENT at first
order. The layout choice moves `tr_M`; it does not move `B`.

**Worth recording separately:** the two canonical producers genuinely disagree.
`atom_braid_word_3A` uses `['p']*Z + ['n']*N` (segregated); `build_atom_nf_exact`
builds an ALTERNATING ordering. That is a live inconsistency for any `tr_M`
consumer even though it is nearly invisible to `B`.



## Reclassified 2026-09-05 — a derivational gap, not an owner decision

Triaged into owner-gated Cluster 7 on the ordering question. But what this bean
establishes is a **gap**: the canonical cross-species arrangement `p...pn...n`
is not derived, the orbit identity provably does not license it (it ranges over
`S_Z × S_N` and its Lemma 1 works by showing the word is *unchanged*, which
says nothing across `pnn` vs `npn`), and the stated justification is a
**cost** property rather than a selection rule.

Naming a gap honestly is agent work, and per AGENTS.md a visible gap is
information. Nothing here needs the author to pick between options. It is also
the same subject as **Cluster 1** (the inter-nucleon topology), where the real
open question lives. Off the owner-gated queue; merge the question into Cluster 1.


## ✅ ANSWERED AND DISCLOSED — closing (checked 2026-09-05)

This bean's question is settled, in the only way a non-derivable DOF can be:
characterised, measured, and disclosed. Carrier is
`computations/probes/canonical_ordering_dof_probe.py` + witness
`computations/probes/canonical-ordering-dof.witness.json` + audit
[`2026-08-09-canonical-ordering-dof-production-impact.md`](../docs/audits/2026-08-09-canonical-ordering-dof-production-impact.md),
with Lean in `QOU/MassTheory/NucleonOrderingSymmetry.lean`.

**Q1 — is it live in production?** Yes, and traced by *inspecting source*
rather than by assertion: `mass_table_comprehensive.try_binding_*` →
`binding_canonical(use_closed_form=True)` → `closed_form_tau_M` →
`closed_form_ratio`, whose interface product iterates a hardcoded
`["p"] * Z + ["n"] * N`.

**Q2 — the three candidate resolutions, all decided:**

1. *"An extremal principle selects it."* **REFUTED.** The interface product
   factorises as `(f_pn/f_pp)^(b_p−1) · (f_pn/f_nn)^(b_n−1)` relative to the
   canonical arrangement, where `b_p`/`b_n` count p-/n-**blocks**. At the
   substrate anchor `f_pn/f_pp < 1 < f_pn/f_nn` — the two base ratios sit on
   **opposite sides of 1** — so raising `b_p` lowers the trace while raising
   `b_n` raises it. The canonical `(b_p, b_n) = (1, 1)` is neither minimum nor
   maximum, so no extremal principle can select it.
2. *"The observable depends only on the interface multiset, so the ordering is
   redundant labelling."* Premise **TRUE and proved in closed form** — and it
   does **not** resolve the question, because the multiset is not an invariant
   of the isotope: one `(Z, N)` realises up to `min(Z,N)+1` distinct multisets.
   The DOF is re-coordinatised from "which ordering" to "which `(b_p, b_n)`",
   not removed.
3. *"A genuine undeclared DOF."* **What survives**, with its size measured.

**The size, on the production readout:** 14 968 exposed rows; worst-case spread
**1.15 MeV = 13.6 % of `B_AME`**; 60 rows above 1 % of `B_AME`; largest absolute
spread **33.874 MeV** (²³⁷Og). The L1/L2 dashboards are **not** affected.

The discipline is clean: `free_parameters = 0`, AME appears only as a
*denominator* expressing an already-computed spread and never as a selector,
q₀ is the experimental proton anchor matching production (no layer straddle),
and **nothing is wired — no ordering is recommended**.

**So this bean's premise stands and is now the corpus's stated position**: the
orbit identity ranges over `S_Z × S_N` and works by leaving the word unchanged,
so it cannot license `pnn` over `npn`; the "interface-minimal" justification is
a cost property, not a selection rule. That is exactly what the audit records.

**Relevance to Cluster 1 (decision D1).** This is direct evidence for the
proposed default there — *disclose, do not pick*. An ordering that is provably
**not an extremum** cannot be selected by principle, and selecting one because
it reproduces AME is the fit the audit explicitly refuses. Closing here; the
live question is D1.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 63 Update (PR #8257)
- Formalized in PR https://github.com/litlfred/qou/pull/8257 (head `18cf0bc120a9baf3be0677bec0817855b4de7a7a`, Commit 1 `2b12359f227b0dc628cdd0df3e8f7f2f6ff6c5ca`, `scriptHash: 1bf530249a70`).
