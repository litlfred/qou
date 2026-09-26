---
# qou-zovy
title: 'ROUTE F: drain the three-depth notation collision in the notation register'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:42:09Z
updated_at: 2026-09-08T04:00:00Z
---

ROUTE F of epic qou-2q85. Cheap hygiene, worth doing regardless of which route is chosen, and it is the direct countermeasure to an error class that produced SEVEN corrections in one session.

THREE FILTRATIONS ARE ALL INDEXED BY SOMETHING CALLED 'DEPTH':
  1. TRANSCENDENCE / iterated-integral depth n - G^(n) adjoins Li_n^q; tau_arch(G^(n)) subset P_n. Moved ADDITIVELY by the q-shuffle.
  2. KNOT / Hecke cell K - refined by the partition cell lambda_K |- n_K.
  3. GB / CURVATURE-RANK k = depth(lambda) - 1 - where depth(lambda) is PARTITION depth (max hook length per conj:two-filtration-bridge).

PROPOSED FIX: name them distinctly in notation/notation-register-table3-data.md and notation-collisions.md - transcendence depth n, cell lambda_K, curvature-rank k - and stop using the bare word 'depth' for (3).

AND RECORD THE HARD FACT ALONGSIDE IT: filtration (3) is currently attached to NO well-defined object. docs/audits/2026-08-16-three-gb-filtrations-one-name.md finds three inequivalent readings of J^bullet (rewrite count - not obviously well defined; image of the l-th power of the rewrite ideal - PROVABLY ZERO for every l >= 1; Coxeter-length span - fails the dimension count), and the 2026-08-26 supersession (qou-wjbd) excludes the third for every n >= 2 with no re-indexing repairing it. A reader who fixes only the NAMES will still think there is a filtration there.

SEE ALSO qou-hnri, which carries the same finding from the collision side. This bean is the ACTION; that one is the measurement.


## MEASURED 2026-09-04 — this bean's PLAN is wrong in two ways. Measurement done; the EDIT needs the owner.

Audit: docs/audits/2026-09-04-route-f-depth-is-unregistered-not-miswritten.md

### 1. The target file has nothing to rename

notation-register-table3-data.md has NO depth row, and neither does any other
register table. "depth" occurs exactly THREE times in the whole notation
register, all incidental:

  notation-collisions.md:118          B_depth = sum_k alpha_k Phi_k (a TOWER row
                                      in a table about B)
  notation-register-table4-data.md:4  a cross-ref to conj:gb-depth-period-
                                      correspondence (a label, not a definition)
  notation-register-table7-data.md:5  "truncations E_0^{(N)} for depth N",
                                      inside the ENERGY row

So the collision is an ABSENCE from the register, not a defect in it -- which is
exactly why the name was available to be taken repeatedly with nothing flagging
the reuse. The correct edit is an ADDITION (a collision entry), not a rename.

### 2. Three senses is an undercount -- at least FIVE are distinct

  transcendence / iterated-integral n    G^(n) adjoins Li_n^q          (this bean)
  knot / Hecke cell lambda_K                                           (this bean)
  GB / curvature-rank k = depth(lambda)-1                              (this bean)
  cascade depth N_eff = floor(log_q Re_q^{3/4})   q-turbulence Reynolds
                                          cascade, Ch 7 -- not a filtration at all
  brane-tower / truncation depth N        E_0^{(N)}; conj:n-v-tower-depth-ninety
                                          ("depth from m_e to v equals 90");
                                          N_v = 120 q_0^90

The FIFTH is the one sense the register already carries (table7), and it is not
among this bean's three.

Two further names are identified with senses above BY PROPOSITIONS, so they are
one thing or two depending on those propositions' status:
  NF support depth  -- prop:phi-q-categorical-truncation asserts "brane-tower
                       truncation depth = NF support depth"
  slicing depth     -- mass-theory/atom-knot-mass-derivation-table1-data.md:
                       "slicing depth | GB filtration grade l(w) (Coxeter length)"

NOT counted as new senses: cyclotomic depth and Bring-natural depth. Both look
like the transcendence sense under a different adjective (Cl_3(2pi/5) as a
"Bring-natural depth-3 invariant"; beta(3) from "cyclotomic depth-n generators").
Recorded as PROBABLY SYNONYMOUS, not measured to be.

### 3. A claim I nearly wrote and did not

Having found "slicing depth = l(w)" in the mass derivation's dictionary, the
tempting write-up was "the mass derivation identifies its slicing depth with a
reading qou-wjbd refuted". FALSE. qou-wjbd refutes the BRIDGE
Z^(k) = Z cap F_k  <->  {lambda : gbDepth(lambda) = k} -- centre strata against
partition strata -- not the Coxeter-length filtration, which is untouched and
remains a fine filtration. Inferring the second from the first is reading a
property of a construction BUILT ON an object as a property of the object: the
same shape as AmbientInvolutionDoesNotDecideType, committed to this branch hours
earlier. It survived a topic-grep and was caught only by reading qou-wjbd's own
statement of what it excluded.

### 4. Status

MEASUREMENT DONE, EDIT NOT STARTED. The register edit is a content change to the
paper's authoritative notation register with corpus-wide reach, and two of the
seven names are one-or-two depending on a proposition's status -- so it is an
owner decision, not idle hygiene. Bean stays open on the edit.

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
