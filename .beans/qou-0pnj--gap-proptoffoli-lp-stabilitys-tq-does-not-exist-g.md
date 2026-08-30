---
# qou-0pnj
title: 'GAP: prop:toffoli-lp-stability''s t(q) does not exist — G is 6x6 Hecke-NF, P_77/P_76 are 8x8 strand-ordering entries'
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:57:56Z
updated_at: 2026-08-30T12:39:03Z
---

FOUND 2026-08-30 investigating what the q-GoL "stability condition" actually
asserts (owner asked for options + pros/cons). The investigation did not end
where it was aimed: the positivity-vs-non-vanishing question is a PROXY for a
computation that has never been performed, and the two sides of the reduction
it rests on live in different index spaces.

## What prop:toffoli-lp-stability asserts

Statement:  "Express the q-Toffoli in normal-form coordinates as
             T_q = sum_{i=1..6} t_i(q) b_i"
Proof:      "Positivity of G.t(q) therefore reduces to the positivity of the
             product P_77(q) . W_std(q) with the appropriate sign from Phi(q)."

## MEASURED — t(q) does not exist anywhere in the corpus

computations/toffoli-lp-stability.py is the producer. Its main() computes, per
grid point: P_77, q_AND_P76, and the Gram eigenvalues. Witness scan-row keys,
read off the committed file:

    ['P_77','P_77_sign','gram_condition','gram_eigenvalues','gram_lambda_max',
     'gram_lambda_min','q','q_AND_P76','q_AND_P76_sign']

There is no t vector and no G.t anywhere in the producer or the witness. The
central quantity of the proposition has never been constructed, so the LP
feasibility of the q-Toffoli has never been tested -- by this producer or any
other. Grep for a Toffoli NF coordinate vector across computations/ returns
nothing.

## And the two sides have DIFFERENT INDEX SPACES

G is 6x6 over the Hecke normal-form basis. Confirmed by direct import:

    pyhecke.gram.NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]     len 6

  = dim H_3(q) = 3! = 6.

P_77 and P_76 are entries of an 8x8 matrix. The ONLY recorded construction is
computations/_deprecated/toffoli-braid.py::build_matrix, whose docstring reads
"8x8 massive Toffoli transfer matrix" and whose loop is

    for k in range(8):
        ordering_k = list(decode(k))
        M[k][k] = markov_trace(ordering_k)

so k indexes a STRAND-TYPE ORDERING (3 binary choices, 2^3 = 8), not a Hecke
basis word. Index 7 = (1,1,1), index 6 = (1,1,0) -- the control-control-target
semantics. The entries ARE Hecke scalars (Markov traces), but the MATRIX is
indexed by orderings.

So the reduction relates a 6-dimensional cone condition (G.t >= 0, six
inequalities over the NF basis) to two scalars drawn from an 8x8 matrix over a
different index set. No map between the two is recorded. That is WHY the
"appropriate sign from Phi(q)" clause could never be derived: there is no t,
and no bridge from the ordering-indexed matrix to the NF-indexed cone.

W_std = (q^2+1)^2/(q^4+4q^2+1) IS a Hecke object -- the Wedderburn weight of
the 2-dim standard rep of H_3(q) (dims 1,2,1 -> 1+4+1 = 6, checks out). So the
proof mixes three things: a Hecke NF Gram, a Hecke Wedderburn weight, and an
ordering-indexed transfer-matrix entry.

## Two further blockers on measuring it directly

1. The producer's own Gram uses the RETRACTED naive length rule --
   `tr += c * (z ** len(w))` at toffoli-lp-stability.py:205, i.e.
   tr_M(T_w) = z^len(w), which the content block itself calls "the retracted
   naive length rule ... the pre-2026-05-19 tr_M(e^-) = z^3 bug". So even the
   Gram that IS computed is not the production one. pyhecke.gram.gram_matrix_mp
   is the correct one and is available.
2. The only Toffoli construction is in _deprecated/.

## Consequence for the open item in prop:q-game-of-life

The block currently offers a choice between positivity (LP feasibility) and
non-vanishing (universality). That framing survives, but it understates the
situation: the LP-feasibility branch is not merely unsettled, its central
object is unconstructed. A ruling that picks positivity would be selecting a
criterion nothing can currently evaluate.

NOT filed as a refutation. Scope (a): what is established is that the
computation has not been done and the recorded reduction does not typecheck as
written. Whether a correct bridge exists -- e.g. t(q) obtained by expanding the
Toffoli braid word in NF and the 8x8 arising as its action on orderings -- is
open and is the natural next step.
