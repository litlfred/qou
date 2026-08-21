---
# qou-hah4
title: 'GAP: WedderburnDecomp needs the IsHeckeOfFullRank companion and a block_scaling field before an instance is worth building'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:32:36Z
updated_at: 2026-08-21T16:33:26Z
---

Branch `claude/wedderburn-instance-artin-2026-08-21`, PR #5387. Answers item 3
of bean `qou-luq7` ("the class still has no instance ... that is the larger
debt"): **do not build the instance yet — it would prove nothing.**

## MACHINE-CHECKED FINDING

`QOU/Hecke/WedderburnRankDegeneracy.lean` (new, this branch) constructs a
complete, sorry-free, axiom-clean `WedderburnDecomp (R := Q) n 1 Q` **at every
n**, on the ONE-dimensional algebra Q. Every field is the class's genuine
equation, discharged: `idempotent`, `orthogonal`, `central`, `complete`,
`trace_decomp`. No Prop-variable field, no `True`, no `PUnit` -- Q is
`Nontrivial`, so it is a strictly stronger witness than a PUnit one.

Headline: `wedderburnDecomp_does_not_pin_rank {n} (hn : 2 <= n) :
Nonempty (WedderburnDecomp (R := Q) n 1 Q) /\ ~ IsHeckeOfFullRank Q n Q`.

`#print axioms` on all six new declarations: [propext, Classical.choice,
Quot.sound]. lean-direct exit 0.

## MECHANISM

`WedderburnDecomp` takes `[HeckeAlgebra R n q A]`, and
`QOU.Hecke.InstanceH2.rankOneModel` inhabits THAT class at every n with
A = R = Q, q = 1, embed := fun _ => 1. PR #4857 found this degeneracy and
repaired it for `HeckeAlgebra` by adding the companion predicate
`IsHeckeOfFullRank` (`QOU/Hecke/FullRank.lean`), whose entire purpose is to
exclude the rank-one model. `WedderburnDecomp` never picked that companion up,
so it inherits the hole.

`y_lambda` is separately unconstrained: it appears in no field except
`trace_decomp`, and `trace_decomp` follows from `complete` alone at
`y_lambda := 1` -- which `QOU/QBeta/WedderburnTraceDecomposition.lean` already
records (`trace_eq_sum_blocks`, and `Hecke/Wedderburn.trace_exhaustive`
proves the same thing inside the defining file).

## THE FIX (two independent halves)

[ ] 1. Pair the class with the rank predicate at every hypothesis site:
       `variable [HeckeAlgebra R n q A] [IsHeckeOfFullRank R n A]
                [WedderburnDecomp n q A]`
       -- or make `WedderburnDecomp` extend it.
[ ] 2. Add the `block_scaling` field per `qou-luq7` items 1-2 and delete
       `trace_decomp`, so `y_lambda` is pinned by
       `tr(x * pi_lambda) = y_lambda * chi lam x`.
[ ] 3. ONLY THEN is an instance worth constructing.

## WHY MATHLIB DOES NOT SUPPLY THE INSTANCE ANYWAY (scoping, measured)

Mathlib's Artin-Wedderburn is
`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`
(`Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean`), plus
`..._of_isAlgClosed` in `SimpleModule/IsAlgClosed.lean`. Three gaps:

1. INDEX TYPE. It yields `Fin n` -- an anonymous index of unknown cardinality,
   obtained existentially. `all_parts : Finset (Partition n)` needs the blocks
   indexed BY PARTITIONS. Mathlib has no theorem identifying the simple modules
   of H_n(q) with partitions (Dipper-James / Hoefsmit); the corpus's own
   `SpechtDimension` docstring says the SYT count is awaited "when it lands".
2. EXISTENTIAL. `exists ... Nonempty (...)`. Extracting `pi_lambda` needs
   `Classical.choice` on a witness carrying no partition labelling, so the
   idempotents cannot be NAMED by lambda.
3. SEMISIMPLICITY IS A HYPOTHESIS. `[IsSemisimpleRing R]` is required. The
   corpus route is `QOU/MathlibExt/HeckeGenericSemisimple.lean
   ::isSemisimpleRing_of_qGeneric`, itself hypothesis-carrying: it takes
   `hgram : (regTraceForm nondegenerate) <-> qFactorial q n /= 0`, which its
   own docstring calls "the one thing the concrete Iwahori-Hecke construction
   must still supply". That is the Schur-element / Gram-determinant identity.

## CORRECTION TO A CLAIM IN CIRCULATION

"PR #4857 proved finrank H_n(q) = n!" is FALSE. #4857 added `IsHeckeOfFullRank`
as a PREDICATE (a hypothesis), proved `finrank_of_rank_recursion` (pure
arithmetic: d 0 = 1 and d(n+1) = (n+1) d n implies d n = n!), and discharged
full rank concretely at n = 2, 3, 4 ONLY -- its body says n = 4 is "the last
level worth instantiating by hand". Separately
`QOU/SchurWeyl/HeckeCoset.lean::finrank_le_factorial` proves
`finrank <= (m+1)!` for all m -- an UPPER BOUND. The all-n equality is not in
the tree.

Also measured: the claim that ten modules are gated on this class is not
supported. Over `content/**/lean/QOU`, exactly 4 files mention
`WedderburnDecomp` (its defining file, `Hecke.lean`'s index line, and two
docstring mentions), and ZERO carry it as a hypothesis binder outside the
defining file.
