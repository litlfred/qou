---
# qou-vdvE
title: 'Bridge step 2: test van der Veen E against |tau_DG|^{-1/2} — the Gukov-Murakami conjecture, for links'
status: in-progress
type: task
priority: high
tags:
    - whitehead-link
    - borromean-rings
    - reorg-2026-10-04
    - one-loop
    - c-sigma
    - adjoint-torsion
    - van-der-veen
    - gukov-murakami
created_at: 2026-08-08T14:07:16Z
updated_at: 2026-10-04T15:14:40Z
parent: qou-n4nr
---

## The ask — RESTATED 2026-08-08, after qou-vdvS closed

The original ask ("evaluate E, then test it against |tau_DG|^{-1/2}") is
**substantially done**, and by a shorter route than expected. `qou-vdvS` closed
the bridge for the whole `b = 1` family:

    c_sigma(W_{a,1,c,d}) = 2^{1/2-n} (n^2+m^2)^{-1/4},   n = c+d,  m = 4a-c+d

which, under the corpus's law `c_sigma = 2^{-1/2}|tau_DG|^{-1/2}`, forces

    |tau_DG| = 2^{2n-2} sqrt(n^2+m^2)

and that was PRE-REGISTERED and then confirmed to 18 digits at L8n5 (3 cusps),
L10n100 and L10n103 (4 cusps), on top of exact agreement at L5a1 and L6a4. So
the Gukov-Murakami relation holds, on links, at three cusp numbers, with the
Jones side derived rather than fitted.

**What is left under this bean is the one thing worth doing that is not
mathematics: report the corrections upstream.** Three slips were found in a
published AGT paper:

  1. Lemma 2a stated in the distances `|n'|, |k'|` where its own Taylor
     expansion is signed;
  2. the Step-3 coefficient `A = (c+d) - (4a+c-d)i`, which should carry
     `4a-c+d` to match `chi^{4a-c+d}` in his own Lemma 1;
  3. the main theorem's `b >= 2` constant `E = +2pi(c+d)log 2`, which his own
     Lemma 5 contradicts (`Re E = -2pi(c+d)log 2`).

None affects his theorem — the volume conjecture needs only `Vol`, `D`, and
`E != 0`, and all three survive. All three affect the constant `E`, which is
exactly what the Gukov-Murakami conjecture he cites is about, and which he
explicitly deferred to a sequel he never wrote.

Roland van der Veen is at Groningen. Worth a short, precise note: the three
corrections, the closed form, and the pre-registered `tau_DG` confirmations.

## Do NOT re-derive

The evaluation is done and committed. Read the probe and audit first:
`computations/probes/one_loop_vdv_constant_closed_form_probe.py`,
`docs/audits/2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`.

## Definition of done

Either a note sent to the author, or a written decision not to, recorded here.

## Draft written 2026-08-08 — NOT SENT, awaiting the owner's decision

`docs/outreach/2026-08-08-van-der-veen-whitehead-chains-corrections.md`.

Sending is an outward-facing action to a named person and is the repository
owner's call, not the agent's, so the bean stays open until either it goes or a
decision not to send is recorded here — which is exactly what the original
"definition of done" asked for.

The draft covers, each with the check that detects it and against the paper's
verbatim text:

  1. Lemma 2a stated in the DISTANCES |n'|, |k'| where the Taylor expansion in
     the proof of Lemma 2 is signed. Table of log(S_{n,k}/S~_N) on the
     opposite-sign corner at N = 4000.
  2. `4a+c-d` should be `4a-c+d`, in Step 3's Gaussian coefficient A AND in
     both branches of the main theorem's CS (verbatim: "-(4a+c-d)/8 2pi^2 if
     c+d = 1 and -(4a-7c+7d)/8 2pi^2 otherwise"). Two tables: the six
     discriminating chains for A, and the measured N-linear phase for CS.
  3. The b >= 2 constant's real part: the main theorem says
     `E = 2pi(c+d) log 2 + ...` where Lemma 5 gives `-2pi(c+d) log 2`. Table of
     |J_N| N^-b e^{-Vol N/2pi} -> 2^{-(c+d)}.

Plus a remark that Lemma 3's own displayed `s_n` line drops the `-1/2 log 2pi`
Stirling term but that Lemma 3 itself is correct, since the two extreme terms
cancel it — worth saying so he does not think we are claiming Lemma 3 is wrong.

Then the payoff: `E` evaluated in closed form for the whole b=1 family, and the
Gukov-Murakami consequence `|tau_DG| = 2^{2n-2} sqrt(n^2+m^2)` with the
pre-registered SnapPy confirmations.

The note opens by stating that his theorem is unaffected — it needs only Vol, D
and E != 0, and all three survive — and closes with an explicit disclosure that
it was prepared with AI assistance and that the owner has reviewed it. Do not
send it without that review actually happening.

## Round 79 progress (PR #8358)
- Advanced in PR #8358 (`3d5e94f03a32259e850c4108650709877896bfd7`).
