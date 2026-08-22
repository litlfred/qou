---
# qou-lrnd
title: QOU perpetual-obstruction instances quantify over p but conclude about a constant
status: todo
type: task
priority: normal
created_at: 2026-08-22T15:26:08Z
updated_at: 2026-08-22T15:26:34Z
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
