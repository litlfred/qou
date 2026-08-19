---
# qou-x76e
title: 'Whitehead positive-sum reduction: transcribe+VALIDATE Habiro colored-Jones vs exact ⟨W⟩_N (state-sum tensor-cut ruled out; needs cyclotomic expansion)'
status: completed
type: task
priority: normal
created_at: 2026-08-01T19:45:01Z
updated_at: 2026-08-01T19:56:25Z
---


## Findings (2026-08-01) — approaches ruled out; still OPEN

The positive-sum form is NOT derivable by a simple cut of the validated
state-sum tensor network:
- **Single-edge cut** of ⟨W⟩_N: every cut summand has Im/|·| ≈ 0.9 and
  mixed signs — not positive.
- **Single-edge Fourier** (DFT of the cut, both signs): even for the
  FIGURE-EIGHT (ground truth Σ|(ω)_k|²) NO single-edge cut+DFT reproduces
  |(ω)_k|². So the positive/angle form is the FULL multi-edge Fourier
  transform of the edge state sum (Kashaev §3 p.4: "evident after Fourier
  transformation over the edge indices" — meaning ALL edges), i.e. a genuine
  basis change to the fusion/cyclotomic form, not a single cut.

**Concrete next step:** obtain the Whitehead colored-Jones CYCLOTOMIC
(Habiro) formula from the literature (candidate: Habiro / Garoufalidis-Le
q-holonomic, arXiv math/0309214, bean qou-j1ld; or a 2-bridge / double-twist
formula — Lovejoy-Osburn 1710.04865 is in library/), transcribe with citation,
and VALIDATE it against whitehead_state_sum's EXACT ⟨W⟩_N at N=3..23 before
trusting it (anti-guessing). Then evaluate at the Kashaev point q=e^{2πi/N},
n=N → the {N}²/{N}² cancellations give the positive terms (à la
habiro_borromean_colored_jones.py). Only then do the squeeze bricks (qou-t2sc).

Status: OPEN (in-progress). The invariant itself (qou-kkog) IS in hand and
validated — this bean is specifically the positive-sum RE-EXPRESSION needed
for the squeeze proof.

## CLOSED (2026-08-01) — positive-sum form found + validated

Superseding the "OPEN" note above: the positive-sum form WAS found — van der
Veen's colored-Jones formula (arXiv:math/0611181, Lemma 1), Whitehead = W_{0,1,1,0},
with the manifestly-positive kernel S_{n,k}=∏ 2 sin²((k+j)π/N)/sin(jπ/N) > 0.
Transcribed + VALIDATED against the exact state sum at N=3..11 (third
independent cross-check: state sum = U_q engine = van der Veen), in
computations/whitehead_van_der_veen.py. Status frontmatter = completed is
correct; this note reconciles the stale body. Squeeze-proof formalization
continues under qou-t2sc.
