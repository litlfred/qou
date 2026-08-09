---
# qou-48is
title: 'GAP: the canonical cross-species nucleon ordering p...pn...n is an unlicensed choice and tr_M depends on it by O(10%) for A>=3'
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T04:34:20Z
updated_at: 2026-08-09T05:18:49Z
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
