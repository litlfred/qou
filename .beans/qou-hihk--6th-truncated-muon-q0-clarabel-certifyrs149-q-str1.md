---
# qou-hihk
title: '6th truncated-muon q0: clarabel_certify.rs:149 q_str=1.10998 feeds Stern-Brocot rationalisation (BLOCKED: no gfortran here)'
status: completed
type: task
priority: normal
created_at: 2026-08-19T21:19:18Z
updated_at: 2026-08-21T21:27:55Z
---

FOUND 2026-08-19 during the PR #5344 rebase, by grepping the truncated
spelling across ALL bins rather than the five the gram::Q_0 scope note named.

SITE. tools/hecke-engine/src/bin/clarabel_certify.rs:149

    let q_str = "1.10998";
    let q_max = 10_000_u64;
    let report = tighten_solution(&solver.solution, 3, q_str, q_max);

This is a SIXTH truncated-muon anchor, missed by both the qou-8q0u round-1
audit (which grepped only the full-precision spelling) and the corrected
gram::Q_0 scope note (which enumerated five bins). 1277 ppb off the proton
anchor.

WHY IT IS NOT FIXED IN #5344. The site takes a STRING, not an f64, because it
feeds a Stern-Brocot rationalisation of the SDP dual (q_max = 10_000). So the
replacement is not gram::Q_0 but the 50-dps decimal string
color_weight::convergence::Q0_50DPS
= "1.1099785827513808075916690956107688798744991218736".

That substitution is NOT safe to make blind: Stern-Brocot returns the best
rational approximation under a denominator cap, so changing the input digits
changes WHICH rational the dual is tightened to, and hence the certificate.
The gram::Q_0 scope note requires each site have "its output re-verified
rather than a blind substitution", and here that re-verification cannot be
run in this sandbox:

    cargo build --bin clarabel-certify --features clarabel-sdp
      -> netlib-src v0.8.0 build fails: "No CMAKE_Fortran_COMPILER could be
         found"; gfortran and f77 are both absent (make + cmake are present).

So the binary can be neither built nor run here, before or after. Changing it
would be exactly the blind substitution the discipline forbids.

TO CLOSE. On a host with gfortran: capture the certificate output before, swap
q_str to Q0_50DPS, capture after, and report which rationals moved and whether
any PSD block''s min_diag or max_denom_bits changed. If the tightened rationals
are unchanged at q_max = 10_000, say so -- that is the useful result either way.

ALSO NOTE. v9.rs:802 and v9.rs:888 already carry "WAS the 5-significant-digit
literal 1.10998" comments, i.e. a sibling fixed those two independently. The
truncated spelling has now bitten three separate audits; grep BOTH spellings.


FIXED 2026-08-21, and the blocker was liftable after all.

BLOCKER LIFTED: gfortran was simply installable (apt-get install -y gfortran ->
GNU Fortran 13.3.0). The bean recorded 'cannot be run in this sandbox' because
netlib-src failed for want of a Fortran compiler; I had not tried installing one.
With it, clarabel-certify builds under --features clarabel-sdp and runs.

FIX: clarabel_certify.rs:149 q_str '1.10998' -> the canonical 50-dps proton pin
'1.1099785827513808075916690956107688798744991218736'.

OUTPUT RE-VERIFIED as the gram::Q_0 scope note requires -- not a blind
substitution. Built and ran the certificate before and after:

    THE OUTPUT IS BYTE-IDENTICAL.

That is the useful result this bean asked for either way. Why: the Stern-Brocot
rationalisation runs at q_max = 10000 and the one tightened block is d=2 with
max_denom_bits=1 -- a rational of denominator ~2. A 1277 ppb shift in q does not
move it. alpha* = 1.0000000000, Sturm-chain PSD verified, aggregate unchanged.

SCOPE: this says the certificate is insensitive to the anchor error AT THIS
q_max WITH THESE BLOCKS. It does not say the literal did not matter -- it was
wrong, and is now right. A larger q_max or different blocks could differ.
