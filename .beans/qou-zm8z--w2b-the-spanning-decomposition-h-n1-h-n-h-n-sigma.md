---
# qou-zm8z
title: 'W2b: the spanning decomposition H_{n+1} = H_n + H_n sigma_n H_n as a content-bearing 3b class (W2''s undelivered third deliverable)'
status: completed
type: task
priority: normal
created_at: 2026-08-26T14:05:48Z
updated_at: 2026-08-26T15:10:28Z
---

## Built 2026-08-26 — PR #5827

`HeckeCosetSpanning` in `QOU/Machinery/HeckeTowerBasicConstruction.lean` (its home:
this was W2's undelivered third deliverable, see the finding on qou-2017).

  spanning : forall w : Hn, exists a s b c,
    w = ilow a + sum_{i in s} ilow (b i) * sigma_n n * ilow (c i)

Content-bearing (one real forall-exists equation; not True, not empty). Binds
HeckeBraidedPresentation in its type = the 3b-tax dependency edge, matching the
three existing classes in that file. Independent of the conditional expectation:
mentions neither eps nor the Jones projection, so it can be discharged separately
and a proof needs no trace at all.

Consumer `gwg_trace_of_spanning` (MarkovTowerBridge): with the class plus the two
grounding shape lemmas, the two-generator Markov reduction holds for EVERY w,
not only pre-decomposed ones.

**The conclusion pins the witness to the decomposition** — it asserts both that w
splits and that the reduction holds with the expectation built from THAT split.
A bare `exists Ew, ...` would be weaker in a way that matters: tr = 0 satisfies
it for any Ew (see `markov_axioms_vacuous_of_weight_zero` upstream), so the
existential alone would carry no coset information. Caught and fixed before commit.

Also recorded as a CHECKED fact, not a caveat:
`spanning_shape_holds_for_identity_inclusion` — with ilow = id every w splits
trivially (a := w, empty sum). So the class is CONSISTENT (a degenerate model
exists, which is what makes conditional results non-vacuous) and is WEAKER than a
proper inclusion — an instance carries no information that Hlow is strict.
Anything needing properness must say so separately.

**Still open:** no instance. And the last gap to hgwg proper is `Ew = i (eps w)`,
which needs the Markov property `eps (b * sigma_n * c) = z . (b*c)` — NOT a field
of HeckeConditionalExpectation (it has exactly retract and bimodule). Not added:
that would relocate an assumption, not discharge one.

Verification: lean-direct exit 0 on both modules; #print axioms clean
(spanning_shape needs only propext + Quot.sound); guard rc=0 on 60 entries.


## (2) an INSTANCE — attempted, blocked one level lower (2026-08-26)

**Blocked, and not by the spanning mathematics.** `HeckeCosetSpanning` binds
`HeckeBraidedPresentation` instances in its type, and that class has **ZERO
instances corpus-wide** (only grep hit is a comment in HeckeH4StabilizationRung
saying one 'stays OPEN'). So no concrete algebra can even STATE a spanning
instance today.

Two facts, both proved (`HeckeTowerBasicConstruction.lean`), explain why:

1. `constant_generator_presentation` — the class IS satisfiable, from a SINGLE
   element satisfying the quadratic, with sigma constant. Braid and far-commute
   are then `rfl`. So an instance does not force two distinct generators, does
   not force the braid relation to carry content, does not force anything to
   fail to commute. **Much weaker than 'is a Hecke algebra'.**

2. `far_commute_zero` — far_commute forces sigma 0 to commute with sigma j for
   EVERY j >= 2. The fields quantify over all i : N, so H_n must supply
   generators beyond its rank. In H3 with sigma 0 = s1, sigma 1 = s2, that rules
   out padding with the last real generator (s1 s2 != s2 s1), and no eventually
   periodic padding works either. **The class describes H_inf, not H_n.**

Concrete targets exist and are NOT the problem: H3A is a genuine Fin 6 -> R ring
with proved normal-form multiplication (HeckeH3AlgebraInstance), H2A likewise.

**I did NOT build a degenerate instance off the constant family.** It would type-
check and be the corpus's 'first HeckeBraidedPresentation instance', and it would
say nothing — laundering, per AGENTS.md 'Axiomatization is NOT a Proof'.

**Route for whoever takes this:** re-state HeckeBraidedPresentation with a rank
bound (sigma : Fin n -> H, or relations guarded by i + 1 < n), then a genuine H2/H3
instance is reachable from the existing concrete algebras. That touches a class
three others bind, so it is its own change.


## RANK-BOUNDED CLASS + FIRST CONTENT-BEARING INSTANCE (2026-08-26)

`QOU/Machinery/HeckeBraidedPresentationRank.lean`. NEW class, not a mutation:
12 files bind HeckeBraidedPresentation and its signature change is a refactor
unrelated to this point.

  HeckeBraidedPresentationOfRank q n H sigma
    hecke_quadratic : forall i, i+1 < n -> ...
    braid_adjacent  : forall i, i+2 < n -> ...
    far_commute     : forall i j, i+1 < j -> j+1 < n -> ...

`ofRank_of_unbounded` : the unbounded class implies it at every rank (guards only
discard obligations), so existing consumers lose nothing by moving over.

**`heckePresentationOfRank_H3A` — the corpus's first presentation instance of any
kind, and it has real content.** Genuine H3(q) on the six-element NF basis, both
true generators s0/s1 (basis indices 1,2), Hecke quadratic for each, braid
relation between them. At rank 3 the guards leave exactly those three relations
and leave generators past rank unconstrained — sent to 0, never padded.

**Non-degeneracy CHECKED, not assumed** — this is what separates it from
`constant_generator_presentation`, where every relation is rfl because everything
commutes:
  s0_ne_s1                 : the generators are distinct
  s0_mul_s1_ne_s1_mul_s0   : they do NOT commute (axioms: [propext] only)

## CORRECTION to my earlier entry

I reported `far_commute_zero` as a finding. **It was already in the corpus** —
`HeckeH3AlgebraLaws.lean:34-36` states the obstruction in prose and covers BOTH
padding routes (sigma_i := 1 forces (q-q^-1).1 = 0 via the quadratic; sigma_i :=
s1 violates far commutation), where I had only the second. I greped for
INSTANCES, not for the OBSTRUCTION. The Lean lemma machine-checks half of a known
note; `constant_generator_presentation` (satisfiability, hence worthlessness of a
reachable instance) is the genuinely new half.

## Still NOT closed

HeckeCosetSpanning binds the UNBOUNDED presentation, so this instance does not
give it one. Re-pointing it is a further change, and the spanning statement would
still need proving for H2 subset H3 afterwards.

Verification: lean-direct exit 0; #print axioms clean on all seven new decls;
guard rc=0 on 71 entries (64 -> 71); guard --selftest PASS.


## FIRST SPANNING INSTANCE — H2 subset H3, concretely (2026-08-26)

`heckeCosetSpanning_H2_H3` — the class now has an instance. Sorry-free,
#print axioms clean.

Measured first, then built. The four sigma-1 coset products are EXACTLY the four
basis vectors iota23 does not reach, with no correction terms:

  s1            -> index 2
  s1 * s0       -> index 3
  s0 * s1       -> index 4        <-- note the SWAP vs my first guess
  s0 * s1 * s0  -> index 5

and iota23 a b = ![a,b,0,0,0,0] covers 0,1. So H3 = i(H2) + i(H2).sigma1.i(H2)
holds on the nose, and the instance is discharged by an EXPLICIT decomposition
reading off w's coordinates — no abstract argument.

My first index guess (s0*s1 -> 3, s1*s0 -> 4) was WRONG; Lean returned False at
those coordinates and the swap was correct. Worth recording: I would have written
a plausible-looking wrong decomposition if I had not asked the compiler.

Supporting: `heckePresentationOfRank_H2A` (rank 2 — only the sigma-0 quadratic;
braid and far-commute are vacuous by omega), `t0_mul_t0`.

Also this pass:
- `HeckeCosetSpanning` re-pointed at the bounded class and its INERT low-side
  binders dropped (sigma_low and the low presentation were never used in the
  statement). The rank class moved into HeckeTowerBasicConstruction so the
  spanning class can bind it without an import cycle.
- `gwg_trace_of_spanning` now carries `omit [HeckeBraidedPresentation R q Hn sigma_n]`
  — the linter confirmed the unbounded presentation had become inert there.

**The guard earned its keep this pass:** after the move it returned rc=2,
'declarations not found: HeckeRank.ofRank_of_unbounded' — the decl had moved to
HeckeTower and the registry was stale. Exactly the failure mode the registry
exists to catch.

Verification: lean-direct exit 0 on all three modules; #print axioms clean on
every new decl (t0_mul_t0 needs only propext); guard rc=0 on 74 entries (71 -> 74);
guard --selftest PASS; lean_freshness --selftest PASS.
