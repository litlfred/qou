---
# qou-vdvE
title: 'Bridge step 2: test van der Veen E against |tau_DG|^{-1/2} — the Gukov-Murakami conjecture, for links'
status: todo
type: task
priority: high
tags:
    - one-loop
    - c-sigma
    - adjoint-torsion
    - van-der-veen
    - gukov-murakami
    - whitehead-link
    - borromean-rings
created_at: 2026-08-08T14:07:16Z
updated_at: 2026-08-08T18:40:00Z
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
