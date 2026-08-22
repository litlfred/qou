---
# qou-lrnd
title: QOU perpetual-obstruction instances quantify over p but conclude about a constant
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:26:08Z
updated_at: 2026-08-22T19:54:06Z
---

FOUND 2026-08-22 while resolving qou-oy4r (main red on
def:qou-motivic-galois-instance). File:
content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean
Sorry-free, so every sorry and axiom audit reports it clean.

Two theorems are docstring'd as the QOU instances:

  theorem qou_proton_perpetual_obstruction :
      exists S : Finset N, forall p : Nat.Primes, (p : N) not-in S -> not IsUnit (4 : Z) :=
    <empty, fun _ _ => galois_trace_not_unit 4 (by norm_num)>

  theorem qou_deuteron_perpetual_obstruction :
      ... -> not IsUnit (-32 : Z) := <empty, fun _ _ => ...>

The conclusion does not mention p or S. The binders are decoration: the
proof term discards both and takes S = empty. What is proved is
'4 is not a unit in Z' and '-32 is not a unit in Z' — norm_num facts about
two integers. The claim the docstrings make — that the QOU Frobenius,
Frob_p = f(u)|_{u=zeta_2p} from the Habiro expansion, is a non-unit at every
prime — is nowhere in either TYPE. It is entirely in the prose: the
derivation 'Frob_p == a0(-1) + a1(-1)(1-(-1)) = 4 (mod p-ideal)' appears only
in the docstring.

NOT a claim that the theorems are false. They are true and sorry-free.
The defect is that the p-quantifier makes them LOOK like statements about
almost-every prime while their content is a statement about a constant.
This is the 'sorry-free != derived' family, and the shape the da-arity-conflation
criterion exists to catch (STRICT section: 'Pointwise, or the universal
closure?' / 'a proposition provable without using any hypothesis about the
mathematical objects in question').

NOT affected: perpetual_obstruction_from_trace in the same file is honest —
it takes trace : Nat.Primes -> Z and a real hypothesis h_bound, and the
conclusion genuinely depends on trace. The gap is that the QOU instances
never instantiate it with an actual Habiro trace; they pass a constant.
perpetual_obstruction_from_collapse_invariant has the same decorative
binders but its hypothesis 1 < C.natAbs does the work, so it is defensible
as a general lemma.

WHAT WOULD CLOSE IT: instantiate perpetual_obstruction_from_trace with a
real trace function derived from the Habiro expansion, so that the type
carries the p-dependence the docstring describes. The numerical side already
exists — computations/probes/habiro_frobenius_probe.py with a 57 KB witness
carrying per-prime atoms.

BLOCKS: qou-oy4r cannot be closed by retargeting def:qou-motivic-galois-instance's
lean.ref at these theorems — that would record a definition as formalized by
a theorem whose type says nothing about it.

PARTLY CLOSED 2026-08-22. Added to
MotivicPerpetualObstructionFromTrace.lean, sorry-free, verified with
lean-direct against restored mathlib oleans (exit 0, 3.0s):

  theorem habiro_frobenius_not_unit
      {R : Nat.Primes -> Type*} [forall p, CommRing (R p)]
      (frob : forall p, R p) (reduce : forall p, R p ->+* Z)
      (C : Z) (hC : 1 < C.natAbs)
      (h_collapse : forall p, reduce p (frob p) = C) :
      forall p : Nat.Primes, not IsUnit (frob p)

plus qou_proton_frobenius_not_unit (C = 4) and
qou_deuteron_frobenius_not_unit (C = -32), and the supporting
not_isUnit_of_image (non-unitness transfers backwards along a ring map).

The conclusion is 'not IsUnit (frob p)' — the Frobenius itself, with p in the
statement. That is the defect this bean names, fixed: p is no longer
decoration.

#print axioms on all four: [propext, Classical.choice, Quot.sound]; no
sorryAx. 0 sorries in the file.

WHAT IS STILL OPEN, deliberately: h_collapse — that reduce p (frob p) = C —
is an explicit HYPOTHESIS, not a proved lemma. It is the symbolic derivation
(at q = zeta_2p: q == -1 mod p-ideal, (q;q)_m == 0 mod p-ideal for m >= 2, so
the expansion collapses to a0(-1) + 2*a1(-1)) which lives in
computations/probes/habiro_frobenius_probe.py and not in Lean. Stating it as
a hypothesis is what keeps that boundary visible; proving it needs cyclotomic
ring theory over Z[zeta_2p] and is the remaining work.

The four original theorems are KEPT — all four are cited externally — with
their docstrings corrected to say what their types actually prove. The
proton/deuteron ones now open with 'read the TYPE. The conclusion is
not IsUnit (4 : Z), which mentions neither p nor S'.
